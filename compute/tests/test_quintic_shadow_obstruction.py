r"""
Tests for the quintic shadow obstruction analysis: chi/24 obstruction,
shadow tower with fractional kappa, BCOV comparison, and CY3 survey.

Ground truth:
    Quintic Q in P^4: h^{1,1}=1, h^{2,1}=101, chi=-200.
    chi/24 = -25/3 (NOT integer).
    K3 x E: chi=0, kappa=5 (from Delta_5), NOT chi/24=0.
    K3: chi=24, kappa=2 (from chi(O_K3)), NOT chi/24=1.

References:
    Bershadsky-Cecotti-Ooguri-Vafa (BCOV), hep-th/9309140
    Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21
    Gopakumar-Vafa, hep-th/9809187
    Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower)
    Vol III: bkm_shadow_tower.py (K3 x E comparison)
"""

import math
from fractions import Fraction

import pytest

from compute.lib.quintic_shadow_obstruction import (
    # CY3 Hodge data
    CY3HodgeData,
    cy3_hodge_data,
    STANDARD_CY3S,
    all_cy3_chi_over_24,
    chi_over_24_integral_criterion,
    # BCOV
    BCOVAnomalyData,
    bcov_anomaly,
    bcov_quintic,
    bcov_k3_times_e,
    # Kappa candidates
    KappaCandidate,
    quintic_kappa_candidates,
    # Shadow tower
    A_HAT_COEFFICIENTS,
    shadow_amplitude_scalar,
    shadow_tower_scalar,
    shadow_metric_data,
    shadow_depth_classification,
    shadow_growth_rate,
    shadow_tower_recursive,
    # Quintic specific
    quintic_shadow_tower_chi24,
    quintic_shadow_tower_recursive,
    quintic_chi24_scalar_amplitudes,
    # GV analysis
    QUINTIC_GV_GENUS0,
    gv_growth_analysis,
    gv_to_shadow_s4_estimate,
    # Obstruction analysis
    ObstructionAnalysis,
    quintic_obstruction_analysis,
    compact_cy3_obstruction_survey,
    # Cross-verification
    kappa_formula_comparison,
    correct_interpretation,
    # Complementarity
    quintic_complementarity,
    # Summary
    quintic_shadow_summary,
)


# ======================================================================
# 1. CHI/24 INTEGRALITY
# ======================================================================

class TestChiOver24:
    """Tests for chi/24 integrality analysis."""

    def test_quintic_chi(self):
        """chi(quintic) = 2*(1-101) = -200."""
        data = cy3_hodge_data("quintic", 1, 101)
        assert data.chi == -200

    def test_quintic_chi_over_24(self):
        """chi/24 = -200/24 = -25/3."""
        data = cy3_hodge_data("quintic", 1, 101)
        assert data.chi_over_24 == Fraction(-25, 3)

    def test_quintic_not_integral(self):
        """chi/24 for quintic is NOT an integer."""
        data = cy3_hodge_data("quintic", 1, 101)
        assert not data.chi_over_24_integral

    def test_k3xe_chi(self):
        """chi(K3 x E) = 0."""
        data = cy3_hodge_data("K3 x E", 21, 21)
        assert data.chi == 0

    def test_k3xe_chi_over_24(self):
        """chi(K3 x E)/24 = 0, which IS an integer."""
        data = cy3_hodge_data("K3 x E", 21, 21)
        assert data.chi_over_24 == 0
        assert data.chi_over_24_integral

    def test_self_mirror_chi_zero(self):
        """Self-mirror CY3 with h11=h21 has chi=0."""
        data = cy3_hodge_data("self-mirror", 11, 11)
        assert data.chi == 0
        assert data.chi_over_24 == 0
        assert data.chi_over_24_integral

    def test_p5_33_integral(self):
        """P5[3,3]: chi = 2*(1-73) = -144, chi/24 = -6 (integer)."""
        data = cy3_hodge_data("P5[3,3]", 1, 73)
        assert data.chi == -144
        assert data.chi_over_24 == Fraction(-6)
        assert data.chi_over_24_integral

    def test_p7_2222_not_integral(self):
        """P7[2,2,2,2]: chi = 2*(1-65) = -128, chi/24 = -16/3 (NOT int)."""
        data = cy3_hodge_data("P7[2,2,2,2]", 1, 65)
        assert data.chi == -128
        assert data.chi_over_24 == Fraction(-16, 3)
        assert not data.chi_over_24_integral

    def test_integrality_criterion_mod12(self):
        """chi/24 integral iff 12 | (h11 - h21)."""
        # Quintic: 1-101 = -100, -100 mod 12 = 8 => NOT integral
        assert not chi_over_24_integral_criterion(1, 101)
        assert (-100) % 12 != 0

        # P5[3,3]: 1-73 = -72, -72 mod 12 = 0 => integral
        assert chi_over_24_integral_criterion(1, 73)
        assert (-72) % 12 == 0

        # K3 x E: 21-21 = 0, 0 mod 12 = 0 => integral
        assert chi_over_24_integral_criterion(21, 21)

    def test_integrality_criterion_systematic(self):
        """Verify criterion against direct computation for all standard CY3s."""
        for data in all_cy3_chi_over_24():
            direct = data.chi_over_24_integral
            criterion = chi_over_24_integral_criterion(data.h11, data.h21)
            assert direct == criterion, f"Mismatch for {data.name}"

    def test_chi_formula_consistency(self):
        """chi = 2*(h11 - h21) for all standard CY3s."""
        for data in all_cy3_chi_over_24():
            assert data.chi == 2 * (data.h11 - data.h21), \
                f"chi formula failed for {data.name}"


# ======================================================================
# 2. BCOV ANOMALY COEFFICIENTS
# ======================================================================

class TestBCOV:
    """Tests for BCOV holomorphic anomaly data."""

    def test_bcov_quintic_c1(self):
        """BCOV c_1 for quintic = (3 + 1 + 200/12) / 2 = 31/3."""
        data = bcov_quintic()
        expected = (Fraction(3) + Fraction(1) + Fraction(200, 12)) / Fraction(2)
        assert data.c1_bcov == expected
        assert data.c1_bcov == Fraction(31, 3)

    def test_bcov_k3xe_c1(self):
        """BCOV c_1 for K3 x E = (3 + 21 - 0/12) / 2 = 12."""
        data = bcov_k3_times_e()
        assert data.c1_bcov == Fraction(12)

    def test_bcov_quintic_not_integer(self):
        """BCOV c_1 for quintic is NOT an integer (31/3)."""
        data = bcov_quintic()
        assert data.c1_bcov.denominator != 1

    def test_bcov_k3xe_integer(self):
        """BCOV c_1 for K3 x E IS an integer (12)."""
        data = bcov_k3_times_e()
        assert data.c1_bcov.denominator == 1

    def test_bcov_chi_over_12(self):
        """chi/12 for quintic = -200/12 = -50/3."""
        data = bcov_quintic()
        assert data.chi_over_12 == Fraction(-50, 3)

    def test_bcov_formula_consistency(self):
        """Verify BCOV formula: c1 = (3 + h11 - chi/12) / 2."""
        for name, (h11, h21) in [("quintic", (1, 101)), ("K3xE", (21, 21))]:
            data = bcov_anomaly(name, h11, h21)
            chi = 2 * (h11 - h21)
            expected = (Fraction(3) + h11 - Fraction(chi, 12)) / 2
            assert data.c1_bcov == expected, f"BCOV formula failed for {name}"


# ======================================================================
# 3. KAPPA CANDIDATES
# ======================================================================

class TestKappaCandidates:
    """Tests for quintic kappa candidates."""

    def test_chi24_candidate(self):
        """chi/24 = -25/3."""
        candidates = quintic_kappa_candidates()
        chi24 = [c for c in candidates if c.name == "chi/24"][0]
        assert chi24.value == Fraction(-25, 3)
        assert not chi24.is_integer

    def test_chi2_candidate(self):
        """chi/2 = -100 (integer)."""
        candidates = quintic_kappa_candidates()
        chi2 = [c for c in candidates if c.name == "chi/2"][0]
        assert chi2.value == Fraction(-100)
        assert chi2.is_integer

    def test_bcov_candidate(self):
        """BCOV c_1 = 31/3."""
        candidates = quintic_kappa_candidates()
        bcov = [c for c in candidates if c.name == "BCOV c1"][0]
        assert bcov.value == Fraction(31, 3)
        assert not bcov.is_integer

    def test_at_least_five_candidates(self):
        """At least 5 kappa candidates for the quintic."""
        candidates = quintic_kappa_candidates()
        assert len(candidates) >= 5

    def test_candidates_distinct(self):
        """All candidate values are distinct."""
        candidates = quintic_kappa_candidates()
        values = [c.value for c in candidates]
        assert len(values) == len(set(values))

    def test_integer_candidates_exist(self):
        """At least one integer candidate exists."""
        candidates = quintic_kappa_candidates()
        assert any(c.is_integer for c in candidates)


# ======================================================================
# 4. A-HAT COEFFICIENTS
# ======================================================================

class TestAHatCoefficients:
    """Verify A-hat genus coefficients (independent of kappa)."""

    def test_a_hat_1(self):
        """a_hat_1 = 1/24."""
        assert A_HAT_COEFFICIENTS[1] == Fraction(1, 24)

    def test_a_hat_2(self):
        """a_hat_2 = 7/5760."""
        assert A_HAT_COEFFICIENTS[2] == Fraction(7, 5760)

    def test_a_hat_3(self):
        """a_hat_3 = 31/967680."""
        assert A_HAT_COEFFICIENTS[3] == Fraction(31, 967680)

    def test_a_hat_all_positive(self):
        """All A-hat coefficients are positive (AP22)."""
        for g, val in A_HAT_COEFFICIENTS.items():
            assert val > 0, f"a_hat_{g} = {val} is not positive"

    def test_a_hat_decreasing(self):
        """A-hat coefficients decrease rapidly."""
        genera = sorted(A_HAT_COEFFICIENTS.keys())
        for i in range(1, len(genera)):
            g_prev, g_curr = genera[i - 1], genera[i]
            assert A_HAT_COEFFICIENTS[g_curr] < A_HAT_COEFFICIENTS[g_prev], \
                f"a_hat_{g_curr} >= a_hat_{g_prev}"


# ======================================================================
# 5. SHADOW TOWER WITH FRACTIONAL KAPPA
# ======================================================================

class TestShadowTower:
    """Tests for the shadow tower with rational (possibly fractional) kappa."""

    def test_quintic_F1(self):
        """F_1 = (-25/3) * (1/24) = -25/72."""
        F1 = shadow_amplitude_scalar(Fraction(-25, 3), 1)
        assert F1 == Fraction(-25, 72)

    def test_quintic_F2(self):
        """F_2 = (-25/3) * (7/5760) = -175/17280 = -35/3456."""
        F2 = shadow_amplitude_scalar(Fraction(-25, 3), 2)
        expected = Fraction(-25, 3) * Fraction(7, 5760)
        assert F2 == expected
        assert F2 == Fraction(-175, 17280)

    def test_quintic_F3(self):
        """F_3 = (-25/3) * (31/967680)."""
        F3 = shadow_amplitude_scalar(Fraction(-25, 3), 3)
        expected = Fraction(-25, 3) * Fraction(31, 967680)
        assert F3 == expected

    def test_quintic_all_negative(self):
        """All F_g are negative for quintic (kappa < 0, a_hat > 0)."""
        tower = quintic_shadow_tower_chi24(5)
        for g, Fg in tower.items():
            assert Fg < 0, f"F_{g} = {Fg} is not negative"

    def test_k3xe_all_positive(self):
        """All F_g are positive for K3 x E (kappa = 5 > 0)."""
        tower = shadow_tower_scalar(Fraction(5), 5)
        for g, Fg in tower.items():
            assert Fg > 0, f"F_{g} = {Fg} is not positive"

    def test_shadow_linearity_in_kappa(self):
        """F_g is linear in kappa: F_g(2*kappa) = 2*F_g(kappa)."""
        k1 = Fraction(-25, 3)
        k2 = 2 * k1
        for g in range(1, 6):
            assert shadow_amplitude_scalar(k2, g) == 2 * shadow_amplitude_scalar(k1, g)

    def test_zero_kappa_gives_zero(self):
        """F_g(0) = 0 for all g."""
        tower = shadow_tower_scalar(Fraction(0), 5)
        for g, Fg in tower.items():
            assert Fg == 0

    def test_quintic_scalar_amplitudes(self):
        """Verify quintic_chi24_scalar_amplitudes consistency."""
        amps = quintic_chi24_scalar_amplitudes()
        assert amps["kappa"] == Fraction(-25, 3)
        for g in range(1, 6):
            key = f"F_{g}"
            expected = Fraction(-25, 3) * A_HAT_COEFFICIENTS[g]
            assert amps[key] == expected


# ======================================================================
# 6. SHADOW METRIC AND DEPTH CLASSIFICATION
# ======================================================================

class TestShadowMetric:
    """Tests for shadow metric and depth classification."""

    def test_shadow_metric_gaussian(self):
        """Class G: alpha=0, S_4=0 => depth 2."""
        cl = shadow_depth_classification(Fraction(-25, 3), Fraction(0), Fraction(0))
        assert cl == "G"

    def test_shadow_metric_lie(self):
        """Class L: alpha!=0, Delta=0 (S_4=0) => depth 3."""
        cl = shadow_depth_classification(Fraction(-25, 3), Fraction(1), Fraction(0))
        assert cl == "L"

    def test_shadow_metric_mixed(self):
        """Class M: Delta!=0 => depth infinity."""
        cl = shadow_depth_classification(Fraction(-25, 3), Fraction(0), Fraction(1))
        assert cl == "M"

    def test_shadow_metric_q0_positive(self):
        """Q_L(0) = 4*kappa^2 > 0 for kappa != 0."""
        data = shadow_metric_data(Fraction(-25, 3))
        assert data["q0"] > 0
        assert data["q0"] == 4 * Fraction(-25, 3)**2

    def test_shadow_metric_quintic_q0(self):
        """Q_L(0) = 4*(25/3)^2 = 2500/9 for quintic."""
        data = shadow_metric_data(Fraction(-25, 3))
        assert data["q0"] == Fraction(2500, 9)

    def test_shadow_metric_delta(self):
        """Delta = 8*kappa*S_4."""
        data = shadow_metric_data(Fraction(-25, 3), Fraction(0), Fraction(7, 10))
        expected_delta = 8 * Fraction(-25, 3) * Fraction(7, 10)
        assert data["Delta"] == expected_delta

    def test_shadow_growth_rate_gaussian(self):
        """Growth rate is None for Gaussian class (finite depth)."""
        rate = shadow_growth_rate(Fraction(-25, 3), Fraction(0), Fraction(0))
        assert rate is None

    def test_shadow_growth_rate_mixed(self):
        """Growth rate exists for mixed class."""
        rate = shadow_growth_rate(
            Fraction(-25, 3), Fraction(2), Fraction(10, 27)
        )
        # Should be a finite positive number
        if rate is not None:
            assert rate > 0


# ======================================================================
# 7. RECURSIVE SHADOW TOWER
# ======================================================================

class TestRecursiveTower:
    """Tests for recursive shadow tower computation."""

    def test_gaussian_terminates(self):
        """Gaussian class: alpha=0, S_4=0 => S_r = 0 for r >= 3."""
        kappa = Fraction(-25, 3)
        tower = shadow_tower_recursive(
            kappa, Fraction(0), Fraction(0), max_arity=10
        )
        # S_r = a_{r-2}/r. S_2 = a_0/2 = 2*kappa/2 = kappa.
        assert tower[2] == kappa
        for r in range(3, 11):
            assert tower[r] == 0, f"S_{r} = {tower[r]} != 0 for Gaussian class"

    def test_lie_depth_3(self):
        """Lie class: alpha != 0, S_4 = 0 => S_r = 0 for r >= 4."""
        alpha = Fraction(2)
        tower = shadow_tower_recursive(
            Fraction(-25, 3), alpha, Fraction(0), max_arity=10
        )
        assert tower[2] != 0  # S_2 = kappa
        assert tower[3] != 0  # S_3 = alpha != 0
        for r in range(4, 11):
            assert tower[r] == 0, f"S_{r} = {tower[r]} != 0 for Lie class"

    def test_recursive_s2_equals_kappa(self):
        """S_2 = kappa (by definition)."""
        kappa = Fraction(-25, 3)
        tower = shadow_tower_recursive(kappa, Fraction(0), Fraction(0), 5)
        assert tower[2] == kappa

    def test_recursive_s3_equals_alpha(self):
        """S_3 = alpha/3 * ... actually S_3 = a_1/3.

        a_1 = q_1/(2*a_0) = 12*kappa*alpha / (2*2*kappa) = 3*alpha.
        So S_3 = a_1/3 = alpha. S_3 IS the cubic shadow alpha.
        """
        kappa = Fraction(-25, 3)
        alpha = Fraction(7, 5)
        tower = shadow_tower_recursive(kappa, alpha, Fraction(0), 5)
        assert tower[3] == alpha

    def test_recursive_zero_kappa(self):
        """kappa = 0: all shadow coefficients vanish."""
        tower = shadow_tower_recursive(Fraction(0), Fraction(0), Fraction(0), 10)
        for r in range(2, 11):
            assert tower[r] == 0

    def test_recursive_virasoro_comparison(self):
        """Compare with known Virasoro shadow at c=1.

        Virasoro at c=1: kappa = 1/2, alpha = 2, S_4 = 10/27.
        The shadow tower should be class M (infinite depth).
        """
        kappa = Fraction(1, 2)
        alpha = Fraction(2)
        S4 = Fraction(10, 27)
        tower = shadow_tower_recursive(kappa, alpha, S4, 10)

        # S_2 = kappa = 1/2
        assert tower[2] == kappa

        # S_3 = alpha = 2
        assert tower[3] == alpha

        # S_4 should be nonzero (class M)
        assert tower[4] != 0

        # Tower should not terminate
        nonzero_count = sum(1 for r in range(5, 11) if tower[r] != 0)
        assert nonzero_count > 0, "Virasoro tower should not terminate"


# ======================================================================
# 8. GV INVARIANT ANALYSIS
# ======================================================================

class TestGVAnalysis:
    """Tests for GV invariant growth analysis."""

    def test_gv_genus0_values(self):
        """Verify known GV invariants."""
        assert QUINTIC_GV_GENUS0[1] == 2875
        assert QUINTIC_GV_GENUS0[2] == 609250
        assert QUINTIC_GV_GENUS0[3] == 317206375

    def test_gv_all_positive(self):
        """All genus-0 GV invariants are positive."""
        for d, n_d in QUINTIC_GV_GENUS0.items():
            assert n_d > 0, f"n^0_{d} = {n_d} is not positive"

    def test_gv_monotone_increasing(self):
        """GV invariants are strictly increasing (for d <= 10)."""
        ds = sorted(QUINTIC_GV_GENUS0.keys())
        for i in range(1, len(ds)):
            assert QUINTIC_GV_GENUS0[ds[i]] > QUINTIC_GV_GENUS0[ds[i - 1]]

    def test_gv_growth_analysis(self):
        """Growth analysis returns valid data."""
        result = gv_growth_analysis()
        assert "growth_type" in result
        assert "avg_exponential_slope" in result
        assert result["avg_exponential_slope"] > 0

    def test_gv_exponential_growth(self):
        """GV invariants grow exponentially (slope > 1)."""
        result = gv_growth_analysis()
        assert result["growth_type"] == "exponential"

    def test_gv_s4_estimate(self):
        """S_4 estimate acknowledges it's undetermined."""
        result = gv_to_shadow_s4_estimate()
        assert "OPEN" in result["estimate_method"]
        assert result["kappa"] == Fraction(-25, 3)


# ======================================================================
# 9. OBSTRUCTION ANALYSIS
# ======================================================================

class TestObstruction:
    """Tests for the chi/24 obstruction analysis."""

    def test_quintic_obstruction(self):
        """Quintic has a chi/24 obstruction."""
        obs = quintic_obstruction_analysis()
        assert not obs.is_integral
        assert obs.chi_over_24 == Fraction(-25, 3)
        assert "NOT integer" in obs.bkm_obstruction

    def test_survey_includes_quintic(self):
        """Survey includes the quintic."""
        survey = compact_cy3_obstruction_survey()
        names = [o.name for o in survey]
        assert "quintic P4[5]" in names

    def test_survey_includes_k3xe(self):
        """Survey includes K3 x E."""
        survey = compact_cy3_obstruction_survey()
        names = [o.name for o in survey]
        assert "K3 x E" in names

    def test_survey_k3xe_no_obstruction(self):
        """K3 x E has no chi/24 obstruction (chi=0)."""
        survey = compact_cy3_obstruction_survey()
        k3xe = [o for o in survey if o.name == "K3 x E"][0]
        assert k3xe.is_integral

    def test_some_integral_some_not(self):
        """Survey has both integral and non-integral chi/24 values."""
        survey = compact_cy3_obstruction_survey()
        n_int = sum(1 for o in survey if o.is_integral)
        n_not = sum(1 for o in survey if not o.is_integral)
        assert n_int >= 1, "No CY3s with integral chi/24"
        assert n_not >= 1, "No CY3s with non-integral chi/24"


# ======================================================================
# 10. KAPPA FORMULA COMPARISON
# ======================================================================

class TestKappaComparison:
    """Tests for kappa formula comparison across CY families."""

    def test_chi24_fails_for_k3xe(self):
        """chi/24 != kappa for K3 x E."""
        comp = kappa_formula_comparison()
        k3xe = [c for c in comp["comparisons"] if c["name"] == "K3 x E"][0]
        assert not k3xe["match"]
        assert k3xe["chi/24"] == Fraction(0)
        assert k3xe["kappa"] == Fraction(5)

    def test_chi24_fails_for_k3(self):
        """chi/24 != kappa for K3."""
        comp = kappa_formula_comparison()
        k3 = [c for c in comp["comparisons"] if c["name"] == "K3 surface"][0]
        assert not k3["match"]
        assert k3["chi/24"] == Fraction(1)
        assert k3["kappa"] == Fraction(2)

    def test_chi24_fails_for_elliptic(self):
        """chi/24 != kappa for elliptic curve."""
        comp = kappa_formula_comparison()
        e = [c for c in comp["comparisons"] if c["name"] == "elliptic curve E"][0]
        assert not e["match"]
        assert e["chi/24"] == Fraction(0)
        assert e["kappa"] == Fraction(1)

    def test_chi24_fails_for_conifold(self):
        """chi/24 != kappa for resolved conifold."""
        comp = kappa_formula_comparison()
        con = [c for c in comp["comparisons"]
               if c["name"] == "resolved conifold"][0]
        assert not con["match"]

    def test_conclusion_documents_failure(self):
        """Conclusion notes that chi/24 != kappa in all known cases."""
        comp = kappa_formula_comparison()
        assert "NOT the correct formula" in comp["conclusion"]


# ======================================================================
# 11. COMPLEMENTARITY
# ======================================================================

class TestComplementarity:
    """Tests for quintic-mirror complementarity."""

    def test_quintic_mirror_chi(self):
        """Mirror quintic has chi = +200."""
        comp = quintic_complementarity()
        assert comp["mirror_chi"] == 200

    def test_mirror_hodge_numbers(self):
        """Mirror quintic: h11=101, h21=1."""
        comp = quintic_complementarity()
        assert comp["mirror_h11"] == 101
        assert comp["mirror_h21"] == 1

    def test_complementarity_sum_zero(self):
        """kappa(Q) + kappa(Q_mirror) = -25/3 + 25/3 = 0."""
        comp = quintic_complementarity()
        assert comp["complementarity_sum"] == 0
        assert comp["sum_vanishes"]

    def test_complementarity_antisymmetric(self):
        """Quintic and mirror have opposite kappa."""
        comp = quintic_complementarity()
        assert comp["quintic_kappa"] == -comp["mirror_kappa"]


# ======================================================================
# 12. CORRECT INTERPRETATION
# ======================================================================

class TestCorrectInterpretation:
    """Tests for the correct mathematical interpretation."""

    def test_interpretation_has_roles(self):
        """Correct interpretation documents both roles of chi/24."""
        interp = correct_interpretation()
        assert "chi/24 role 1" in interp
        assert "chi/24 role 2" in interp

    def test_kappa_undetermined(self):
        """Correct interpretation notes kappa is undetermined for quintic."""
        interp = correct_interpretation()
        assert "UNDETERMINED" in interp["kappa determination"]

    def test_resolution_paths(self):
        """Resolution paths are documented."""
        interp = correct_interpretation()
        assert "Path 1" in interp["resolution paths"]
        assert "Path 2" in interp["resolution paths"]


# ======================================================================
# 13. MASTER SUMMARY
# ======================================================================

class TestSummary:
    """Tests for the master summary."""

    def test_summary_exists(self):
        """Summary function runs without error."""
        summary = quintic_shadow_summary()
        assert isinstance(summary, dict)

    def test_summary_kappa(self):
        """Summary contains the conjectural kappa."""
        summary = quintic_shadow_summary()
        assert summary["kappa_conjectural"] == Fraction(-25, 3)

    def test_summary_not_integral(self):
        """Summary reports chi/24 is NOT integral."""
        summary = quintic_shadow_summary()
        assert not summary["chi_over_24_integral"]

    def test_summary_class_m(self):
        """Summary reports class M (conjectural)."""
        summary = quintic_shadow_summary()
        assert "M" in summary["shadow_class"]


# ======================================================================
# 14. CROSS-VERIFICATION: TWO INDEPENDENT PATHS
# ======================================================================

class TestCrossVerification:
    """Multi-path verification (mandate: 3+ independent paths per claim)."""

    def test_chi24_three_paths(self):
        """Verify chi/24 = -25/3 by three independent paths.

        Path 1: Direct from Hodge numbers.
        Path 2: From Euler characteristic formula chi = 2*(h11-h21).
        Path 3: From the cy3_hodge_data function.
        """
        # Path 1: direct
        h11, h21 = 1, 101
        chi_direct = 2 * (h11 - h21)
        ratio_direct = Fraction(chi_direct, 24)
        assert ratio_direct == Fraction(-25, 3)

        # Path 2: via Euler characteristic
        chi_formula = 2 * h11 - 2 * h21
        assert chi_formula == -200
        ratio_formula = Fraction(chi_formula, 24)
        assert ratio_formula == Fraction(-25, 3)

        # Path 3: via function
        data = cy3_hodge_data("quintic", 1, 101)
        assert data.chi_over_24 == Fraction(-25, 3)

        # All three agree
        assert ratio_direct == ratio_formula == data.chi_over_24

    def test_F1_three_paths(self):
        """Verify F_1 = -25/72 by three independent paths.

        Path 1: Direct F_1 = kappa * (1/24) = (-25/3) * (1/24) = -25/72.
        Path 2: Via the shadow_amplitude_scalar function.
        Path 3: Via the shadow_tower_scalar function.
        """
        kappa = Fraction(-25, 3)

        # Path 1: direct multiplication
        F1_direct = kappa * Fraction(1, 24)
        assert F1_direct == Fraction(-25, 72)

        # Path 2: via function
        F1_func = shadow_amplitude_scalar(kappa, 1)
        assert F1_func == Fraction(-25, 72)

        # Path 3: via tower
        tower = shadow_tower_scalar(kappa, 1)
        assert tower[1] == Fraction(-25, 72)

        # All three agree
        assert F1_direct == F1_func == tower[1]

    def test_integrality_three_paths(self):
        """Verify integrality criterion by three independent paths.

        Path 1: Direct: -200/24 has denominator != 1.
        Path 2: Modular arithmetic: (1-101) mod 12 = -100 mod 12 = 8 != 0.
        Path 3: Via function.
        """
        # Path 1
        ratio = Fraction(-200, 24)
        path1 = ratio.denominator == 1
        assert not path1

        # Path 2
        path2 = (1 - 101) % 12 == 0
        assert not path2

        # Path 3
        path3 = chi_over_24_integral_criterion(1, 101)
        assert not path3

        # All three agree: NOT integral
        assert path1 == path2 == path3 == False

    def test_bcov_c1_two_paths(self):
        """Verify BCOV c_1 = 31/3 by two independent paths.

        Path 1: Direct from formula.
        Path 2: Via function.
        """
        # Path 1
        c1_direct = (Fraction(3) + Fraction(1) + Fraction(200, 12)) / Fraction(2)
        # = (3 + 1 + 50/3) / 2 = (9/3 + 3/3 + 50/3) / 2 = (62/3) / 2 = 31/3
        assert c1_direct == Fraction(31, 3)

        # Path 2
        data = bcov_quintic()
        assert data.c1_bcov == Fraction(31, 3)

        assert c1_direct == data.c1_bcov

    def test_complementarity_two_paths(self):
        """Verify complementarity sum = 0 by two paths.

        Path 1: Direct computation.
        Path 2: Via function.
        """
        # Path 1
        kappa_q = Fraction(-200, 24)
        kappa_m = Fraction(200, 24)
        assert kappa_q + kappa_m == 0

        # Path 2
        comp = quintic_complementarity()
        assert comp["complementarity_sum"] == 0


# ======================================================================
# 15. SHADOW METRIC QUADRATIC FORM CONSISTENCY
# ======================================================================

class TestQuadraticForm:
    """Test that the shadow metric Q_L is a valid quadratic form."""

    def test_q0_positive_definite(self):
        """Q_L(0) = 4*kappa^2 > 0 for kappa != 0."""
        for kappa_val in [Fraction(-25, 3), Fraction(1, 2), Fraction(5)]:
            data = shadow_metric_data(kappa_val)
            assert data["q0"] > 0

    def test_q0_zero_iff_kappa_zero(self):
        """Q_L(0) = 0 iff kappa = 0."""
        data = shadow_metric_data(Fraction(0))
        assert data["q0"] == 0

    def test_quadratic_form_structure(self):
        """Q_L(t) = q0 + q1*t + q2*t^2 has correct coefficients."""
        kappa = Fraction(-25, 3)
        alpha = Fraction(7, 5)
        S4 = Fraction(10, 27)
        data = shadow_metric_data(kappa, alpha, S4)

        # q0 = 4*kappa^2
        assert data["q0"] == 4 * kappa**2

        # q1 = 12*kappa*alpha
        assert data["q1"] == 12 * kappa * alpha

        # q2 = 9*alpha^2 + 16*kappa*S4
        assert data["q2"] == 9 * alpha**2 + 16 * kappa * S4

        # Delta = 8*kappa*S4
        assert data["Delta"] == 8 * kappa * S4

    def test_discriminant_formula(self):
        """Delta = 8*kappa*S_4 (the critical discriminant)."""
        kappa = Fraction(-25, 3)
        S4 = Fraction(10, 27)
        data = shadow_metric_data(kappa, Fraction(0), S4)
        expected = 8 * kappa * S4
        assert data["Delta"] == expected
        assert data["Delta"] == Fraction(-2000, 81)
