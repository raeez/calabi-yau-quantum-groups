"""Tests for bps_microstate_shadow.py.

BPS black hole microstate counts from the shadow partition function for K3 x E.
Multi-path verification: each claim verified by at least 2 independent methods.

Test organization:
  1.  Shadow invariants S_2 through S_10 (10 tests)
  2.  BPS degeneracies and phi_{0,1} coefficients (8 tests)
  3.  Shadow partial sums vs exact (8 tests)
  4.  Rademacher convergence rate (8 tests)
  5.  Subleading entropy corrections (8 tests)
  6.  OSV conjecture via bar complex (7 tests)
  7.  Comprehensive comparison table (6 tests)
  8.  Physical prediction (5 tests)
  9.  Cross-verifications (10 tests)
  10. Summary (2 tests)

Total: 72 tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.bps_microstate_shadow import (
    # Shadow invariants
    VIRASORO_SHADOW_TOWER,
    shadow_invariant,
    shadow_tower_contributions,
    shadow_partial_sum_through_k,
    # BPS degeneracies
    BPS_DEGENERACIES,
    PHI01_COEFFICIENTS,
    bps_degeneracy,
    microstate_count,
    # Shadow partial sums
    rademacher_term_jacobi,
    shadow_partial_sum_at_D,
    shadow_vs_exact_comparison,
    # Convergence
    rademacher_convergence,
    convergence_table,
    terms_for_1pct_accuracy,
    # Subleading
    A_HAT,
    KAPPA_CH, BORCHERDS_C0_N1, KAPPA_BKM, KAPPA_CAT, KAPPA_CAT_FIBER,
    KAPPA_FIBER,
    subleading_corrections,
    entropy_with_corrections,
    # OSV
    osv_genus_amplitudes,
    osv_bar_complex_chain,
    # Comprehensive
    comprehensive_comparison,
    # Physical prediction
    physical_prediction_subleading,
    # Verification
    verify_shadow_tower_signs,
    verify_shadow_growth,
    verify_kappa_spectrum_consistency,
    verify_discriminant_constraint,
    # Summary
    bps_microstate_shadow_summary,
)


# =========================================================================
# 1. SHADOW INVARIANTS S_2 THROUGH S_10
# =========================================================================

class TestShadowInvariants:
    """Verify shadow tower values from a_infinity_bar_w1inf.py."""

    def test_S2_equals_half(self):
        """S_2 = kappa_ch(Vir, c=1) = 1/2."""
        assert shadow_invariant(2) == Fraction(1, 2)

    def test_S3_equals_2(self):
        """S_3 = alpha/3 = 2 (cubic shadow)."""
        assert shadow_invariant(3) == Fraction(2)

    def test_S4_equals_10_over_27(self):
        """S_4 = 10/27 (quartic shadow)."""
        assert shadow_invariant(4) == Fraction(10, 27)

    def test_S5_negative(self):
        """S_5 = -16/9 (first negative term, class M signature)."""
        assert shadow_invariant(5) == Fraction(-16, 9)

    def test_S6_positive(self):
        """S_6 = 19040/2187 (positive)."""
        assert shadow_invariant(6) == Fraction(19040, 2187)

    def test_S7_through_S10_exist(self):
        """All shadow invariants S_7 through S_10 are available."""
        for k in range(7, 11):
            sk = shadow_invariant(k)
            assert isinstance(sk, Fraction)
            assert sk != 0  # class M: all nonzero

    def test_tower_has_9_entries(self):
        """Shadow tower has entries for k = 2, ..., 10."""
        assert len(VIRASORO_SHADOW_TOWER) == 9
        assert set(VIRASORO_SHADOW_TOWER.keys()) == set(range(2, 11))

    def test_alternating_signs_from_S5(self):
        """Signs alternate starting at S_5: -, +, -, +, -, +."""
        signs = verify_shadow_tower_signs()
        # S_2, S_3, S_4 are positive
        assert signs[2] == 1
        assert signs[3] == 1
        assert signs[4] == 1
        # S_5 onward alternates
        for k in range(5, 11):
            expected = -1 if (k - 5) % 2 == 0 else 1
            assert signs[k] == expected, f"S_{k} has wrong sign"

    def test_shadow_contributions_structure(self):
        """shadow_tower_contributions returns correct structure."""
        contribs = shadow_tower_contributions()
        assert len(contribs) == 9
        assert contribs[0].arity_k == 2
        assert contribs[0].conductor_c == 1
        assert contribs[-1].arity_k == 10

    def test_shadow_invariant_out_of_range_raises(self):
        """Requesting S_11 raises ValueError."""
        with pytest.raises(ValueError):
            shadow_invariant(11)


# =========================================================================
# 2. BPS DEGENERACIES AND PHI_{0,1} COEFFICIENTS
# =========================================================================

class TestBPSDegeneracies:
    """Verify BPS degeneracies and phi_{0,1} Fourier coefficients."""

    def test_omega_minus1_is_1(self):
        """Omega(-1) = 1: single ground state."""
        assert bps_degeneracy(-1) == 1

    def test_omega_3_is_248(self):
        """Omega(3) = 248: dim(E_8) coincidence."""
        assert bps_degeneracy(3) == 248

    def test_omega_7_is_4119(self):
        """Omega(7) = 4119."""
        assert bps_degeneracy(7) == 4119

    def test_phi01_D3_is_minus64(self):
        """c(3) = -64 for phi_{0,1} at discriminant D=3."""
        assert PHI01_COEFFICIENTS[3] == -64

    def test_phi01_Dminus1_is_1(self):
        """c(-1) = 1: the polar term."""
        assert PHI01_COEFFICIENTS[-1] == 1

    def test_microstate_count_D7(self):
        """log|Omega(7)| = log(4119) ~ 8.32."""
        mc = microstate_count(7)
        assert mc is not None
        assert abs(mc - math.log(4119)) < 1e-10

    def test_bps_degeneracies_grow(self):
        """BPS degeneracies |Omega(D)| grow with D."""
        D_vals = [3, 7, 11, 15]
        omegas = [abs(bps_degeneracy(D)) for D in D_vals]
        for i in range(len(omegas) - 1):
            assert omegas[i + 1] > omegas[i]

    def test_discriminant_constraint_valid(self):
        """Valid discriminants satisfy D = 0 or 3 mod 4."""
        for D in BPS_DEGENERACIES:
            if D >= 0:
                assert verify_discriminant_constraint(D), f"D={D} fails"


# =========================================================================
# 3. SHADOW PARTIAL SUMS VS EXACT
# =========================================================================

class TestShadowPartialSums:
    """Compare shadow partial sums with exact phi_{0,1} coefficients."""

    def test_leading_rademacher_positive(self):
        """R_1(D) > 0 for all D > 0."""
        for D in [3, 4, 7, 8, 11, 15]:
            assert rademacher_term_jacobi(D, 1) > 0

    def test_leading_term_approx_D3(self):
        """R_1(3) approximates |c(3)| = 64 within 5%."""
        R1 = rademacher_term_jacobi(3, 1)
        assert abs(R1 - 64) / 64 < 0.05

    def test_leading_term_approx_D7(self):
        """R_1(7) approximates |c(7)| = 513 within 2%."""
        R1 = rademacher_term_jacobi(7, 1)
        assert abs(R1 - 513) / 513 < 0.02

    def test_partial_sum_oscillates_after_leading_term(self):
        """At D=11 the leading term is already best among the first terms.

        The Rademacher series is oscillatory (Kloosterman phases), so
        convergence is NOT monotone at every step.  At D=11 the leading
        term already captures >99.9%, while adding the first few
        conductors worsens the small-discriminant approximation but keeps
        it below 0.5%.
        """
        ps = shadow_partial_sum_through_k(11, k_max=6)
        exact = 2752.0  # |c(11)|
        err_k2 = abs(ps[2] - exact) / exact
        err_k6 = abs(ps[6] - exact) / exact
        assert err_k2 < 0.001
        assert err_k6 > err_k2
        assert err_k6 < 0.005

    def test_shadow_partial_sum_at_D_matches(self):
        """shadow_partial_sum_at_D agrees with shadow_partial_sum_through_k."""
        D = 8
        ps_full = shadow_partial_sum_at_D(D, max_k=6)
        ps_dict = shadow_partial_sum_through_k(D, k_max=6)
        assert abs(ps_full - ps_dict[6]) < 1e-10

    def test_comparison_table_has_entries(self):
        """shadow_vs_exact_comparison returns rows for valid discriminants."""
        rows = shadow_vs_exact_comparison()
        assert len(rows) >= 5

    def test_exponential_suppression_c2(self):
        """|R_2(D)| / |R_1(D)| < 10% for D >= 3."""
        for D in [3, 7, 11, 15]:
            R1 = abs(rademacher_term_jacobi(D, 1))
            R2 = abs(rademacher_term_jacobi(D, 2))
            if R1 > 0:
                assert R2 / R1 < 0.10, f"D={D}: R2/R1 = {R2/R1}"

    def test_exponential_suppression_decreases_with_D(self):
        """The ratio |R_2/R_1| decreases as D grows."""
        ratios = []
        for D in [3, 7, 15]:
            R1 = abs(rademacher_term_jacobi(D, 1))
            R2 = abs(rademacher_term_jacobi(D, 2))
            if R1 > 0:
                ratios.append(R2 / R1)
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] < ratios[i]


# =========================================================================
# 4. RADEMACHER CONVERGENCE RATE
# =========================================================================

class TestRademacherConvergence:
    """How many shadow terms are needed for 1% accuracy?"""

    def test_convergence_data_structure(self):
        """rademacher_convergence returns well-formed data."""
        data = rademacher_convergence(7)
        assert data.D == 7
        assert data.exact_abs == 513.0
        assert 1 in data.partial_sums

    def test_c1_sufficient_at_D15(self):
        """At D=15, c=1 already gives < 1% error."""
        data = rademacher_convergence(15)
        assert data.c_for_1pct is not None
        assert data.c_for_1pct <= 2

    def test_residuals_are_oscillatory_but_small(self):
        """Residuals at D=7 are oscillatory but remain within a 1.1% envelope.

        The Rademacher series oscillates (Kloosterman phases), so
        individual partial sums are NOT monotonically closer.  For the
        stored small-D oracle, the c=1 truncation is the best among the
        first five conductors.
        """
        data = rademacher_convergence(7, max_c=5)
        rels = [data.residuals_rel[c] for c in range(1, 6)
                if data.residuals_rel.get(c) is not None]
        assert min(rels) == rels[0]
        assert max(rels) < 0.011

    def test_convergence_table_has_entries(self):
        """convergence_table returns data for all stored discriminants."""
        table = convergence_table()
        assert len(table) >= 8  # at least 8 discriminants in PHI01_COEFFICIENTS

    def test_terms_for_1pct_small(self):
        """For D >= 3, at most a few terms suffice for 1% accuracy."""
        t = terms_for_1pct_accuracy()
        for D, c_max in t.items():
            if c_max is not None:
                assert c_max <= 5, f"D={D} needs {c_max} terms"

    def test_D3_needs_at_most_3_terms(self):
        """At D=3, at most c=3 gives < 1% error.

        D=3 is the smallest discriminant: Rademacher convergence is slowest.
        The leading term has ~2% error; by c=3 the oscillatory partial
        sums dip below 1%.
        """
        data = rademacher_convergence(3)
        assert data.c_for_1pct is not None
        assert data.c_for_1pct <= 3

    def test_exponential_ratio_c2_at_D8(self):
        """|R_2/R_1| at D=8 matches Bessel prediction within factor 3."""
        data = rademacher_convergence(8)
        actual = data.exponential_ratios.get(2, 0.0)
        predicted = math.exp(-math.pi * math.sqrt(8) / 2)
        # Kloosterman phases can modify, so allow factor of 3
        assert actual < 3 * predicted

    def test_larger_D_needs_fewer_terms(self):
        """Larger D converges faster (fewer Rademacher terms needed)."""
        t = terms_for_1pct_accuracy()
        # D=3 may need 1-2; D=15 should need at most 1
        if t.get(3) is not None and t.get(15) is not None:
            assert t[15] <= t[3]


# =========================================================================
# 5. SUBLEADING ENTROPY CORRECTIONS
# =========================================================================

class TestSubleadingCorrections:
    """Verify subleading corrections to S_BH from the shadow tower."""

    def test_log_correction_sign(self):
        """The logarithmic correction is negative."""
        corrs = subleading_corrections(100)
        log_corr = corrs[0]
        assert log_corr.genus == 0
        assert log_corr.correction_value < 0

    def test_log_correction_value(self):
        """delta_S_log = -(3/2)*log(D) at D=100."""
        corrs = subleading_corrections(100)
        expected = -1.5 * math.log(100)
        assert abs(corrs[0].correction_value - expected) < 1e-10

    def test_genus1_positive(self):
        """Genus-1 correction is positive (kappa_ch > 0, A_hat_1 > 0)."""
        corrs = subleading_corrections(100)
        g1 = [c for c in corrs if c.genus == 1]
        assert len(g1) == 1
        assert g1[0].correction_value > 0

    def test_genus_corrections_decrease(self):
        """Higher-genus corrections decrease in magnitude."""
        corrs = subleading_corrections(100, max_genus=4)
        genus_corrs = [c for c in corrs if c.genus >= 1]
        for i in range(len(genus_corrs) - 1):
            assert abs(genus_corrs[i + 1].correction_value) < abs(genus_corrs[i].correction_value)

    def test_entropy_with_corrections_overshoots_stored_small_D(self):
        """The logarithmic correction overshoots on the stored small-D data.

        The Rademacher expansion is ASYMPTOTIC: corrections improve the
        fit only for D >> 1.  The stored exact table stops at small
        discriminants, where the -(3/2)*log(D) correction is still a
        large fraction of S_BH and worsens the absolute comparison.

        Multi-path: verify via both entropy_with_corrections and
        independent calculation of S_BH - 1.5*log(D).
        """
        for D in [15, 16]:
            result = entropy_with_corrections(D)
            if result["error_bare"] is not None and result["error_corrected"] is not None:
                assert result["error_corrected"] > result["error_bare"], \
                    f"D={D}: corrected {result['error_corrected']:.4f} <= bare {result['error_bare']:.4f}"
                # Multi-path: independent calculation
                S_BH = math.pi * math.sqrt(D)
                S_corrected_manual = S_BH - 1.5 * math.log(D)
                exact = microstate_count(D)
                if exact is not None:
                    err_manual = abs(S_corrected_manual - exact) / abs(exact)
                    assert abs(err_manual - result["error_corrected"]) < 0.05

    def test_a_hat_coefficients(self):
        """A-hat coefficients match known values."""
        assert A_HAT[1] == Fraction(1, 24)
        assert A_HAT[2] == Fraction(7, 5760)
        assert A_HAT[3] == Fraction(31, 967680)

    def test_no_corrections_for_D_le_0(self):
        """No corrections for D <= 0."""
        corrs = subleading_corrections(0)
        assert len(corrs) == 0

    def test_relative_corrections_small_at_large_D(self):
        """Genus-g corrections are small relative to S_BH at large D."""
        corrs = subleading_corrections(1000, max_genus=3)
        for c in corrs:
            if c.genus >= 1:
                assert abs(c.correction_relative) < 0.01


# =========================================================================
# 6. OSV CONJECTURE VIA BAR COMPLEX
# =========================================================================

class TestOSVConjecture:
    """Verify the OSV conjecture through the bar complex."""

    def test_osv_genus_amplitudes_count(self):
        """OSV genus amplitudes include g = 0, 1, ..., 5."""
        amps = osv_genus_amplitudes()
        assert len(amps) == 6  # g = 0 through 5

    def test_F1_shadow_matches_topstring(self):
        """F_1 from shadow = F_1 from topological string."""
        amps = osv_genus_amplitudes()
        g1 = [a for a in amps if a.genus == 1]
        assert len(g1) == 1
        assert g1[0].agreement is True

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa_ch / 24 = 3/24 = 1/8."""
        amps = osv_genus_amplitudes()
        g1 = amps[1]
        assert abs(g1.F_g_shadow - 0.125) < 1e-12

    def test_higher_genus_agreement(self):
        """F_g from shadow agrees with topological string for g >= 2."""
        amps = osv_genus_amplitudes()
        for a in amps:
            if a.genus >= 2 and a.agreement is not None:
                assert a.agreement is True

    def test_osv_chain_structure(self):
        """osv_bar_complex_chain returns the full mediation chain."""
        chain = osv_bar_complex_chain()
        assert "chain" in chain
        assert len(chain["chain"]) == 6
        assert chain["kappa_ch"] == 3.0
        assert chain["kappa_BKM"] == 5

    def test_osv_chain_cites_CY_A(self):
        """The OSV chain cites CY-A status (AP-CY8 compliance)."""
        chain = osv_bar_complex_chain()
        assert "CY_A_status" in chain
        assert chain["CY_A_status"]["d=2"] == "PROVED"

    def test_osv_chain_cites_bar_euler(self):
        """The OSV chain mentions the bar Euler product (AP-CY8)."""
        chain = osv_bar_complex_chain()
        assert chain["AP_CY8_check"] is not None


# =========================================================================
# 7. COMPREHENSIVE COMPARISON TABLE
# =========================================================================

class TestComprehensiveComparison:
    """Verify the comprehensive shadow vs exact comparison table."""

    def test_table_has_entries(self):
        """Table covers at least 8 discriminants."""
        comp = comprehensive_comparison()
        assert len(comp) >= 8

    def test_table_D7_omega(self):
        """D=7 row: Omega(7) = 4119."""
        comp = comprehensive_comparison([7])
        assert len(comp) == 1
        assert comp[0].omega == 4119

    def test_table_D7_phi01(self):
        """D=7 row: c(7) = -513."""
        comp = comprehensive_comparison([7])
        assert comp[0].phi01_coeff == -513

    def test_table_shadow_partial_sums_present(self):
        """Each row has shadow partial sums for k = 2..10."""
        comp = comprehensive_comparison([7])
        ps = comp[0].shadow_partial_sums
        assert 2 in ps
        assert 10 in ps

    def test_table_phi01_residuals_small_and_oscillatory(self):
        """phi_{0,1} residuals at D=8 are small but not monotone."""
        comp = comprehensive_comparison([8])
        res = comp[0].phi01_residuals
        if res.get(1) is not None and res.get(3) is not None:
            assert res[1] < res[3]
            assert max(v for v in res.values() if v is not None) < 0.02

    def test_table_c_for_1pct_bounded(self):
        """All c_for_1pct values are at most 5."""
        comp = comprehensive_comparison()
        for row in comp:
            if row.c_for_1pct is not None:
                assert row.c_for_1pct <= 5


# =========================================================================
# 8. PHYSICAL PREDICTION
# =========================================================================

class TestPhysicalPrediction:
    """Verify the physical prediction for subleading BH entropy."""

    def test_prediction_structure(self):
        """physical_prediction_subleading returns well-formed data."""
        pred = physical_prediction_subleading(100)
        assert "S_BH" in pred
        assert "delta_S_log" in pred
        assert "hierarchy" in pred

    def test_log_dominates_genus(self):
        """The log correction dominates over genus expansion at D=100."""
        pred = physical_prediction_subleading(100)
        assert abs(pred["delta_S_log"]) > abs(pred["delta_S_shadow_total"])

    def test_nonpert_tiny_at_D100(self):
        """Non-perturbative correction is tiny at D=100."""
        pred = physical_prediction_subleading(100)
        assert pred["delta_S_np_ratio"] < 1e-6

    def test_hierarchy_ordering(self):
        """S_BH >> |delta_S_log| >> |delta_S_shadow| >> delta_S_np."""
        pred = physical_prediction_subleading(100)
        assert pred["S_BH"] > abs(pred["delta_S_log"])
        assert abs(pred["delta_S_log"]) > abs(pred["delta_S_shadow_total"])
        assert abs(pred["delta_S_shadow_total"]) > pred["delta_S_np_ratio"]

    def test_physical_prediction_string(self):
        """The physical prediction string mentions kappa_BKM."""
        pred = physical_prediction_subleading(100)
        assert "kappa_BKM" in pred["physical_prediction"]


# =========================================================================
# 9. CROSS-VERIFICATIONS
# =========================================================================

class TestCrossVerifications:
    """Cross-verify results by multiple paths."""

    def test_kappa_spectrum_all_pass(self):
        """All kappa spectrum verifications pass."""
        checks = verify_kappa_spectrum_consistency()
        assert "borcherds_weight_derives_kappa_BKM_N1" in checks
        assert "identity_fiber_N1" not in checks
        assert all(checks.values())

    def test_total_space_kappa_identity_fails(self):
        """kappa_BKM != kappa_ch + kappa_cat(K3 x E): 5 != 3 + 0."""
        assert KAPPA_BKM != int(KAPPA_CH) + KAPPA_CAT

    def test_borcherds_weight_derives_kappa_BKM(self):
        """kappa_BKM(Delta_5) is c_1(0)/2 = 10/2 = 5."""
        assert BORCHERDS_C0_N1 == 10
        assert KAPPA_BKM == BORCHERDS_C0_N1 // 2

    def test_fiber_sum_is_only_N1_coincidence(self):
        """3 + 2 = 5 is the N=1 Heisenberg-fiber coincidence only."""
        assert KAPPA_BKM == int(KAPPA_CH) + KAPPA_CAT_FIBER
        checks = verify_kappa_spectrum_consistency()
        assert checks["fiber_sum_N1_heisenberg_coincidence_only"] is True

    def test_shadow_growth_class_M(self):
        """Shadow tower growth is consistent with class M (Gevrey-1)."""
        growth = verify_shadow_growth()
        # The ratios should be positive (growth) and roughly constant
        # for factorial scaling
        for k, ratio in growth.items():
            assert ratio > 0, f"S_{k}/S_{k-1} growth ratio should be positive"

    def test_phi01_rademacher_matches_stored(self):
        """Rademacher partial sum at D=3, c_max=3 matches |c(3)|=64 within 1%."""
        ps = sum(rademacher_term_jacobi(3, c) for c in range(1, 4))
        assert abs(ps - 64) / 64 < 0.01

    def test_shadow_entropy_and_bps_entropy_agree_on_BH(self):
        """Both engines agree on S_BH = pi*sqrt(D) for D=7."""
        from compute.lib.bps_entropy_shadow import bekenstein_hawking_k3e
        S_bps = bekenstein_hawking_k3e(7)
        S_here = math.pi * math.sqrt(7)
        assert abs(S_bps - S_here) < 1e-10

    def test_shadow_vs_bps_kappa_spectrum(self):
        """Both engines agree on kappa values."""
        from compute.lib.bps_entropy_shadow import K3E_KAPPA_SPECTRUM
        assert float(KAPPA_CH) == float(K3E_KAPPA_SPECTRUM.kappa_ch)
        assert KAPPA_BKM == K3E_KAPPA_SPECTRUM.kappa_BKM
        assert KAPPA_CAT == K3E_KAPPA_SPECTRUM.kappa_cat
        assert KAPPA_CAT_FIBER == K3E_KAPPA_SPECTRUM.kappa_cat_fiber
        assert KAPPA_FIBER == K3E_KAPPA_SPECTRUM.kappa_fiber

    def test_shadow_partial_sum_nonmonotone_but_accurate_D15(self):
        """At D=15, the first truncation is highly accurate but not monotone."""
        exact = 11775.0  # |c(15)|
        ps = shadow_partial_sum_through_k(15, k_max=5)
        err_2 = abs(ps[2] - exact) / exact
        err_3 = abs(ps[3] - exact) / exact
        assert err_2 < 0.001
        assert err_3 > err_2
        assert err_3 < 0.002

    def test_discriminant_constraint_all_stored(self):
        """All stored phi_{0,1} coefficients satisfy discriminant constraint."""
        for D in PHI01_COEFFICIENTS:
            assert verify_discriminant_constraint(D), f"D={D} fails"


# =========================================================================
# 10. SUMMARY
# =========================================================================

class TestSummary:
    """Verify the summary function runs and returns complete data."""

    def test_summary_runs(self):
        """bps_microstate_shadow_summary completes without error."""
        summary = bps_microstate_shadow_summary()
        assert "shadow_tower" in summary
        assert "convergence" in summary
        assert "physical_prediction" in summary
        assert "osv_chain" in summary

    def test_summary_shadow_tower_complete(self):
        """Summary includes all 9 shadow invariants."""
        summary = bps_microstate_shadow_summary()
        assert len(summary["shadow_tower"]) == 9
