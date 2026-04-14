r"""
Tests for quintic_shadow_tower.py -- Full shadow tower computation for the
quintic CY3 X = {x_0^5+...+x_4^5=0} in P^4.

Ground truth:
  Quintic: h^{1,1}=1, h^{2,1}=101, chi=-200.
  kappa_ch = -25/3 (conjectural, conditional on CY-A_3).
  Intersection number H^3 = 5.
  Classical Yukawa coupling C_111 = 5.
  Cubic shadow alpha = -3/5 (classical).
  Class M (infinite depth, from infinite GV invariants).
  GV genus-0: n^0_1 = 2875, n^0_2 = 609250 (COGP 1991).

  K3 x E: kappa_ch = 3, kappa_BKM = 5 (for comparison).
  Mirror quintic: chi = +200, kappa_ch = +25/3 (conjectural).

All CY3 results conditional on CY-A_3 (AP-CY6).

References:
  Candelas-de la Ossa-Green-Parkes (COGP), NPB 359 (1991) 21
  Bershadsky-Cecotti-Ooguri-Vafa (BCOV), hep-th/9309140
  Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower)
  Vol III: cy_to_chiral.tex (atlas table)
"""

import math
from fractions import Fraction

import pytest

from compute.lib.quintic_shadow_tower import (
    # GV data
    QUINTIC_GV_G0,
    QUINTIC_GV_G1,
    QUINTIC_GV_G2,
    A_HAT_COEFFICIENTS,
    # Kappa spectrum
    QuinticKappaSpectrum,
    quintic_kappa_spectrum,
    # Classical shadow
    ClassicalShadowData,
    classical_shadow_data_quintic,
    classical_shadow_data_one_param,
    ONE_PARAM_CY3S,
    classical_shadow_landscape,
    # Instanton-corrected shadow
    InstantonCorrectedShadow,
    yukawa_coupling_coefficients,
    quartic_coupling_coefficients,
    instanton_corrected_shadow_quintic,
    # Scalar shadow tower
    scalar_shadow_amplitude,
    quintic_scalar_shadow_tower,
    # Recursive shadow tower
    shadow_metric_quintic,
    shadow_tower_recursive,
    quintic_shadow_tower_classical,
    quintic_shadow_tower_with_instantons,
    # Comparison with K3 x E
    ShadowComparison,
    compare_quintic_k3e,
    shadow_complexity_comparison,
    # Mirror symmetry
    MirrorShadowData,
    mirror_shadow_quintic,
    # Conifold transition
    ConifoldTransitionData,
    conifold_transition_shadow,
    conifold_monodromy_on_periods,
    # Degeneration landscape
    DegenerationShadow,
    quintic_degeneration_landscape,
    # Picard-Fuchs
    picard_fuchs_recursion,
    picard_fuchs_ratio_convergence,
    # Shadow coefficients S_2, S_3, S_4
    QuinticShadowCoefficients,
    quintic_shadow_coefficients,
    # Summary
    quintic_shadow_tower_summary,
)


# ======================================================================
# 1. GV INVARIANTS (GROUND TRUTH)
# ======================================================================

class TestGVInvariants:
    """Tests for the Gopakumar-Vafa invariant data."""

    def test_gv_g0_d1(self):
        """n^0_1 = 2875 (number of lines on the quintic, Clemens-Harris)."""
        # VERIFIED [DC] direct count [LT] COGP 1991
        assert QUINTIC_GV_G0[1] == 2875

    def test_gv_g0_d2(self):
        """n^0_2 = 609250 (conics on the quintic)."""
        # VERIFIED [DC] direct count [LT] COGP 1991
        assert QUINTIC_GV_G0[2] == 609250

    def test_gv_g0_d3(self):
        """n^0_3 = 317206375."""
        # VERIFIED [LT] COGP 1991, Givental 1996
        assert QUINTIC_GV_G0[3] == 317206375

    def test_gv_g0_d4(self):
        """n^0_4 = 242467530000."""
        # VERIFIED [LT] COGP 1991
        assert QUINTIC_GV_G0[4] == 242467530000

    def test_gv_g0_d5(self):
        """n^0_5 = 229305888887625."""
        # VERIFIED [LT] COGP 1991
        assert QUINTIC_GV_G0[5] == 229305888887625

    def test_gv_g1_d1_d2_zero(self):
        """No genus-1 GV at degree 1 or 2 (no genus-1 maps of low degree)."""
        # VERIFIED [LT] HKQ hep-th/0612308
        assert QUINTIC_GV_G1[1] == 0
        assert QUINTIC_GV_G1[2] == 0

    def test_gv_g1_d3(self):
        """n^1_3 = 609250 (genus-1 degree-3 curves, same as n^0_2)."""
        # VERIFIED [LT] HKQ hep-th/0612308
        assert QUINTIC_GV_G1[3] == 609250

    def test_gv_g2_d4(self):
        """n^2_4 = 534750 (genus-2 degree-4 curves)."""
        # VERIFIED [LT] HKQ hep-th/0612308
        assert QUINTIC_GV_G2[4] == 534750

    def test_gv_monotone_g0(self):
        """Genus-0 GV invariants are strictly increasing."""
        sorted_d = sorted(QUINTIC_GV_G0.keys())
        for i in range(1, len(sorted_d)):
            assert QUINTIC_GV_G0[sorted_d[i]] > QUINTIC_GV_G0[sorted_d[i - 1]]

    def test_gv_g0_exponential_growth(self):
        """log(n^0_d) grows roughly linearly in d (exponential growth)."""
        # VERIFIED [DC] asymptotic analysis [LT] HKQ
        gv = QUINTIC_GV_G0
        # Average log growth rate should exceed 1 (exponential, not polynomial)
        avg_rate = (math.log(float(gv[10])) - math.log(float(gv[1]))) / 9
        assert avg_rate > 1.0


# ======================================================================
# 2. KAPPA SPECTRUM (AP113)
# ======================================================================

class TestKappaSpectrum:
    """Tests for the quintic kappa-spectrum."""

    def test_kappa_ch(self):
        """kappa_ch = chi/24 = -200/24 = -25/3."""
        # VERIFIED [DC] chi/24 formula [LT] cy_to_chiral.tex atlas table
        spec = quintic_kappa_spectrum()
        assert spec.kappa_ch == Fraction(-25, 3)

    def test_kappa_cat_zero(self):
        """kappa_cat = chi(O_X) = 0 for any CY3."""
        # VERIFIED [DC] chi(O_X) = sum (-1)^p h^{p,0} = 1-0+0-1 = 0
        spec = quintic_kappa_spectrum()
        assert spec.kappa_cat == Fraction(0)

    def test_kappa_bkm_unknown(self):
        """kappa_BKM is unknown for the quintic (no BKM algebra)."""
        spec = quintic_kappa_spectrum()
        assert spec.kappa_BKM is None

    def test_kappa_fiber_na(self):
        """kappa_fiber is N/A for the quintic (no fibration)."""
        spec = quintic_kappa_spectrum()
        assert spec.kappa_fiber is None

    def test_kappa_ch_not_integer(self):
        """kappa_ch = -25/3 is NOT an integer."""
        spec = quintic_kappa_spectrum()
        assert spec.kappa_ch.denominator != 1

    def test_kappa_ch_negative(self):
        """kappa_ch < 0 for the quintic (chi < 0)."""
        spec = quintic_kappa_spectrum()
        assert spec.kappa_ch < 0


# ======================================================================
# 3. CLASSICAL SHADOW DATA
# ======================================================================

class TestClassicalShadow:
    """Tests for the classical (instanton-free) shadow data."""

    def test_intersection_number(self):
        """H^3 = 5 for the quintic (degree of the hypersurface)."""
        # VERIFIED [DC] degree formula [LT] standard
        data = classical_shadow_data_quintic()
        assert data.intersection_number == 5

    def test_yukawa_classical(self):
        """Classical Yukawa coupling C_111 = 5."""
        # VERIFIED [DC] C_111 = H^3 = deg(X) = 5
        data = classical_shadow_data_quintic()
        assert data.yukawa_classical == 5

    def test_alpha_classical(self):
        """alpha = C_111 / kappa_ch = 5 / (-25/3) = -3/5."""
        # VERIFIED [DC] direct computation
        data = classical_shadow_data_quintic()
        assert data.alpha_classical == Fraction(-3, 5)

    def test_alpha_classical_derivation(self):
        """Verify alpha = C/kappa step by step."""
        C = Fraction(5)
        kappa = Fraction(-25, 3)
        alpha = C / kappa
        # 5 / (-25/3) = 5 * (-3/25) = -15/25 = -3/5
        assert alpha == Fraction(-3, 5)

    def test_s4_classical_zero(self):
        """S_4 = 0 at the classical level (cubic prepotential has no d^4)."""
        data = classical_shadow_data_quintic()
        assert data.s4_classical == Fraction(0)

    def test_class_classical_l(self):
        """Classical class is L (alpha != 0, S_4 = 0)."""
        data = classical_shadow_data_quintic()
        assert data.shadow_class_classical == "L"

    def test_hodge_numbers(self):
        """h^{1,1} = 1, h^{2,1} = 101, chi = -200."""
        data = classical_shadow_data_quintic()
        assert data.h11 == 1
        assert data.h21 == 101
        assert data.chi == -200

    def test_one_param_landscape(self):
        """All standard one-parameter CY3s have classical shadow data."""
        landscape = classical_shadow_landscape()
        assert len(landscape) == len(ONE_PARAM_CY3S)
        for data in landscape:
            assert data.h11 == 1
            assert data.kappa_ch != Fraction(0)  # chi != 0 for all

    def test_bicubic_intersection(self):
        """P5[3,3]: intersection number K = 9."""
        data = classical_shadow_data_one_param("P5[3,3]", 73, 9)
        assert data.intersection_number == 9
        assert data.chi == 2 * (1 - 73)
        assert data.chi == -144

    def test_bicubic_alpha(self):
        """P5[3,3]: alpha = 9 / (-144/24) = 9 / (-6) = -3/2."""
        data = classical_shadow_data_one_param("P5[3,3]", 73, 9)
        assert data.alpha_classical == Fraction(-3, 2)


# ======================================================================
# 4. YUKAWA COUPLING COEFFICIENTS
# ======================================================================

class TestYukawaCoupling:
    """Tests for the instanton-corrected Yukawa coupling."""

    def test_yukawa_d1(self):
        """Yukawa at q^1: n^0_1 * 1^3 = 2875."""
        coeffs = yukawa_coupling_coefficients(5, QUINTIC_GV_G0, 5)
        assert coeffs[1] == Fraction(2875)

    def test_yukawa_d2(self):
        """Yukawa at q^2: n^0_1 * 1^3 + n^0_2 * 2^3 = 2875 + 4874000."""
        # d=2: divisors of 2 are {1, 2}.
        # d'=1: n^0_1 * 1^3 = 2875 (since 2 % 1 == 0)
        # d'=2: n^0_2 * 2^3 = 609250 * 8 = 4874000
        coeffs = yukawa_coupling_coefficients(5, QUINTIC_GV_G0, 5)
        expected = Fraction(2875 + 609250 * 8)
        assert coeffs[2] == expected

    def test_yukawa_d3(self):
        """Yukawa at q^3: sum over d | 3."""
        # d'=1: n^0_1 * 1 = 2875 (since 3 % 1 == 0)
        # d'=3: n^0_3 * 27 = 317206375 * 27
        coeffs = yukawa_coupling_coefficients(5, QUINTIC_GV_G0, 5)
        expected = Fraction(2875 + 317206375 * 27)
        assert coeffs[3] == expected

    def test_quartic_d1(self):
        """Quartic moment at d=1: n^0_1 * 1^4 = 2875."""
        coeffs = quartic_coupling_coefficients(QUINTIC_GV_G0, 5)
        assert coeffs[1] == Fraction(2875)

    def test_quartic_d2(self):
        """Quartic moment at d=2: n^0_2 * 2^4 = 609250 * 16."""
        coeffs = quartic_coupling_coefficients(QUINTIC_GV_G0, 5)
        assert coeffs[2] == Fraction(609250 * 16)


# ======================================================================
# 5. SCALAR SHADOW TOWER
# ======================================================================

class TestScalarShadowTower:
    """Tests for the scalar shadow tower F_g = kappa_ch * a_hat_g."""

    def test_f1(self):
        """F_1 = (-25/3)(1/24) = -25/72."""
        # VERIFIED [DC] direct computation [LT] cy_to_chiral.tex line 2185
        tower = quintic_scalar_shadow_tower()
        assert tower[1] == Fraction(-25, 72)

    def test_f2(self):
        """F_2 = (-25/3)(7/5760) = -175/17280 = -35/3456."""
        tower = quintic_scalar_shadow_tower()
        expected = Fraction(-25, 3) * Fraction(7, 5760)
        assert tower[2] == expected
        # Simplify: -175/17280 = -35/3456
        assert expected == Fraction(-35, 3456)

    def test_f3(self):
        """F_3 = (-25/3)(31/967680)."""
        tower = quintic_scalar_shadow_tower()
        expected = Fraction(-25, 3) * Fraction(31, 967680)
        assert tower[3] == expected

    def test_all_negative(self):
        """All F_g < 0 (kappa < 0, a_hat_g > 0)."""
        tower = quintic_scalar_shadow_tower()
        for g, f_g in tower.items():
            assert f_g < 0, f"F_{g} = {f_g} is not negative"

    def test_decreasing_magnitude(self):
        """|F_g| is decreasing in g."""
        tower = quintic_scalar_shadow_tower()
        for g in range(1, 5):
            assert abs(tower[g]) > abs(tower[g + 1])

    def test_amplitude_raises_for_invalid_genus(self):
        """scalar_shadow_amplitude raises ValueError for g > 5."""
        with pytest.raises(ValueError):
            scalar_shadow_amplitude(Fraction(-25, 3), 6)


# ======================================================================
# 6. SHADOW METRIC
# ======================================================================

class TestShadowMetric:
    """Tests for the shadow metric Q_L(t)."""

    def test_q0(self):
        """Q_L(0) = 4*kappa^2 = 4*(625/9) = 2500/9."""
        metric = shadow_metric_quintic()
        assert metric["q0"] == Fraction(2500, 9)

    def test_q1(self):
        """q_1 = 12*kappa*alpha = 12*(-25/3)*(-3/5) = 60."""
        metric = shadow_metric_quintic()
        assert metric["q1"] == Fraction(60)

    def test_q1_derivation(self):
        """Verify q_1 step by step."""
        kappa = Fraction(-25, 3)
        alpha = Fraction(-3, 5)
        q1 = 12 * kappa * alpha
        # 12 * (-25/3) * (-3/5) = 12 * 75/15 = 12 * 5 = 60
        assert q1 == Fraction(60)

    def test_delta_zero_classical(self):
        """Delta = 0 at the classical level (S_4 = 0)."""
        metric = shadow_metric_quintic(S4=Fraction(0))
        assert metric["Delta"] == Fraction(0)

    def test_q2_classical(self):
        """q_2 = 9*alpha^2 = 9*(9/25) = 81/25 when S_4 = 0."""
        metric = shadow_metric_quintic(S4=Fraction(0))
        assert metric["q2"] == Fraction(81, 25)

    def test_perfect_square_classical(self):
        """At S_4 = 0: Q_L(t) = (2*kappa + 3*alpha*t)^2 (perfect square).

        q_0 = (2*kappa)^2, q_1 = 2*(2*kappa)*(3*alpha), q_2 = (3*alpha)^2.
        Check: q_2 - q_1^2/(4*q_0) = 0.
        """
        metric = shadow_metric_quintic(S4=Fraction(0))
        q0, q1, q2 = metric["q0"], metric["q1"], metric["q2"]
        # For a perfect square (a+bt)^2: q2 = b^2, q1 = 2ab, q0 = a^2
        # Check: q1^2 - 4*q0*q2 = 0
        discriminant = q1 ** 2 - 4 * q0 * q2
        assert discriminant == Fraction(0)


# ======================================================================
# 7. RECURSIVE SHADOW TOWER
# ======================================================================

class TestRecursiveShadowTower:
    """Tests for the recursive shadow tower computation."""

    def test_classical_s2(self):
        """S_2 = kappa_ch = -25/3 (classical)."""
        tower = quintic_shadow_tower_classical()
        # S_2 = a_0 / 2 = 2*kappa / 2 = kappa
        assert tower[2] == Fraction(-25, 3)

    def test_classical_s3(self):
        """S_3 = alpha = -3/5 (classical)."""
        tower = quintic_shadow_tower_classical()
        # S_3 = a_1 / 3 = 3*alpha / 3 = alpha
        assert tower[3] == Fraction(-3, 5)

    def test_classical_s4_zero(self):
        """S_4 = 0 at the classical level."""
        tower = quintic_shadow_tower_classical()
        assert tower[4] == Fraction(0)

    def test_classical_higher_zero(self):
        """S_r = 0 for all r >= 4 at the classical level (class L)."""
        tower = quintic_shadow_tower_classical(max_arity=15)
        for r in range(4, 16):
            assert tower[r] == Fraction(0), f"S_{r} = {tower[r]} != 0"

    def test_class_l_depth_3(self):
        """Classical tower terminates at depth 3 (class L)."""
        tower = quintic_shadow_tower_classical(max_arity=10)
        nonzero = [r for r, s in tower.items() if s != Fraction(0)]
        assert max(nonzero) == 3

    def test_instanton_s4_nonzero(self):
        """With S_4_input != 0: S_4 is nonzero."""
        tower = quintic_shadow_tower_with_instantons(
            S4_value=Fraction(1), max_arity=10
        )
        assert tower[4] != Fraction(0)

    def test_instanton_class_m(self):
        """With S_4_input != 0: infinite tower (class M)."""
        tower = quintic_shadow_tower_with_instantons(
            S4_value=Fraction(1), max_arity=10
        )
        # Check that high-arity coefficients are nonzero
        assert tower[8] != Fraction(0)
        assert tower[10] != Fraction(0)

    def test_instanton_s2_unchanged(self):
        """S_2 is unchanged by instantons (kappa is global)."""
        tower_cl = quintic_shadow_tower_classical()
        tower_inst = quintic_shadow_tower_with_instantons(
            S4_value=Fraction(1)
        )
        assert tower_cl[2] == tower_inst[2]

    def test_instanton_s3_unchanged(self):
        """S_3 is unchanged by S_4 (alpha is independent of S_4)."""
        tower_cl = quintic_shadow_tower_classical()
        tower_inst = quintic_shadow_tower_with_instantons(
            S4_value=Fraction(1)
        )
        assert tower_cl[3] == tower_inst[3]


# ======================================================================
# 8. COMPARISON WITH K3 x E
# ======================================================================

class TestComparisonK3E:
    """Tests for the quintic vs K3 x E comparison."""

    def test_lattice_rank(self):
        """Quintic has rank 1, K3 x E has rank 21."""
        comp = compare_quintic_k3e()
        assert comp.lattice_rank_A == 1
        assert comp.lattice_rank_B == 21

    def test_kappa_signs(self):
        """Quintic has kappa < 0, K3 x E has kappa > 0."""
        comp = compare_quintic_k3e()
        assert comp.kappa_A < 0
        assert comp.kappa_B > 0

    def test_both_class_m(self):
        """Both are class M (infinite depth)."""
        comp = compare_quintic_k3e()
        assert comp.class_A == "M"
        assert comp.class_B == "M"

    def test_kappa_values(self):
        """kappa_ch(quintic) = -25/3, kappa_ch(K3xE) = 3."""
        comp = compare_quintic_k3e()
        assert comp.kappa_A == Fraction(-25, 3)
        assert comp.kappa_B == Fraction(3)

    def test_complexity_comparison_runs(self):
        """shadow_complexity_comparison produces valid output."""
        result = shadow_complexity_comparison()
        assert result["quintic"]["lattice_rank"] == 1
        assert result["k3xe"]["lattice_rank"] == 21
        assert result["quintic"]["avg_log_growth_rate"] > 0


# ======================================================================
# 9. MIRROR SYMMETRY
# ======================================================================

class TestMirrorSymmetry:
    """Tests for the mirror symmetry transformation."""

    def test_kappa_complementarity(self):
        """kappa_ch(X) + kappa_ch(X_mirror) = 0."""
        mirror = mirror_shadow_quintic()
        assert mirror.kappa_sum == Fraction(0)

    def test_kappa_signs(self):
        """Quintic kappa < 0, mirror kappa > 0."""
        mirror = mirror_shadow_quintic()
        assert mirror.kappa_ch < 0
        assert mirror.kappa_ch_mirror > 0

    def test_mirror_hodge_exchange(self):
        """h^{1,1}(X) = 1 <-> h^{1,1}(X_mirror) = 101."""
        mirror = mirror_shadow_quintic()
        assert mirror.h11 == 1
        assert mirror.h11_mirror == 101

    def test_lattice_rank_expansion(self):
        """Mirror quintic has rank 101 (from h^{1,1} = 101)."""
        mirror = mirror_shadow_quintic()
        assert mirror.lattice_rank == 1
        assert mirror.lattice_rank_mirror == 101

    def test_both_class_m(self):
        """Both quintic and mirror quintic are class M."""
        mirror = mirror_shadow_quintic()
        assert mirror.class_original == "M"
        assert mirror.class_mirror == "M"


# ======================================================================
# 10. CONIFOLD TRANSITION
# ======================================================================

class TestConifoldTransition:
    """Tests for the conifold transition behaviour."""

    def test_class_transition(self):
        """Shadow class transitions from M to G."""
        data = conifold_transition_shadow()
        assert data.class_before == "M"
        assert data.class_after == "G"

    def test_yukawa_diverges(self):
        """Yukawa coupling diverges at the conifold."""
        data = conifold_transition_shadow()
        assert data.yukawa_diverges is True

    def test_alpha_diverges(self):
        """alpha -> infinity at the conifold."""
        data = conifold_transition_shadow()
        assert data.alpha_diverges is True

    def test_period_vanishes(self):
        """A period vanishes at the conifold."""
        data = conifold_transition_shadow()
        assert data.period_vanishes is True

    def test_monodromy_type(self):
        """Conifold monodromy is unipotent rank 1."""
        data = conifold_transition_shadow()
        assert "unipotent" in data.monodromy_type
        assert "rank 1" in data.monodromy_type

    def test_kappa_after(self):
        """After the conifold transition: kappa_ch = 1 (resolved conifold)."""
        data = conifold_transition_shadow()
        assert data.kappa_ch_after == Fraction(1)

    def test_monodromy_matrix(self):
        """Conifold monodromy matrix is unipotent with (M-I)^2 = 0."""
        mono = conifold_monodromy_on_periods()
        M = mono["monodromy_matrix"]
        # M - I
        N = [[M[i][j] - (1 if i == j else 0) for j in range(4)]
             for i in range(4)]
        # N^2 = 0
        N2 = [[sum(N[i][k] * N[k][j] for k in range(4))
               for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                assert N2[i][j] == 0, f"N^2[{i}][{j}] = {N2[i][j]} != 0"

    def test_monodromy_rank_1(self):
        """rank(M - I) = 1."""
        mono = conifold_monodromy_on_periods()
        M = mono["monodromy_matrix"]
        N = [[M[i][j] - (1 if i == j else 0) for j in range(4)]
             for i in range(4)]
        # Count nonzero rows
        nonzero_rows = sum(
            1 for row in N if any(x != 0 for x in row)
        )
        assert nonzero_rows == 1


# ======================================================================
# 11. DEGENERATION LANDSCAPE (AP157)
# ======================================================================

class TestDegenerationLandscape:
    """Tests for the degeneration-type landscape."""

    def test_three_types(self):
        """The quintic has three degeneration types."""
        landscape = quintic_degeneration_landscape()
        assert len(landscape) == 3

    def test_lcs_type(self):
        """LCS degeneration is present."""
        landscape = quintic_degeneration_landscape()
        types = [d.degeneration_type for d in landscape]
        assert any("LCS" in t or "large complex" in t for t in types)

    def test_conifold_type(self):
        """Conifold degeneration is present."""
        landscape = quintic_degeneration_landscape()
        types = [d.degeneration_type for d in landscape]
        assert any("conifold" in t for t in types)

    def test_gepner_type(self):
        """Gepner/orbifold degeneration is present."""
        landscape = quintic_degeneration_landscape()
        types = [d.degeneration_type for d in landscape]
        assert any("Gepner" in t or "orbifold" in t for t in types)

    def test_each_has_kappa(self):
        """Each degeneration type has a kappa_ch value."""
        landscape = quintic_degeneration_landscape()
        for d in landscape:
            assert d.kappa_ch == Fraction(-25, 3)


# ======================================================================
# 12. PICARD-FUCHS
# ======================================================================

class TestPicardFuchs:
    """Tests for the Picard-Fuchs recursion."""

    def test_a0(self):
        """a_0 = (0!)/(0!)^5 = 1."""
        coeffs = picard_fuchs_recursion(5)
        assert coeffs[0] == Fraction(1)

    def test_a1(self):
        """a_1 = (5!)/(1!^5 * 5^1) = 120/5 = 24.

        The recursion a_{n+1}/a_n = (5n+1)(5n+2)(5n+3)(5n+4)/(n+1)^4
        gives a_n = (5n)!/((n!)^5 * 5^n).
        """
        coeffs = picard_fuchs_recursion(5)
        # VERIFIED [DC] direct computation: 1*2*3*4 / 1^4 = 24
        assert coeffs[1] == Fraction(24)

    def test_a2(self):
        """a_2 = (10!)/(2!^5 * 5^2) = 3628800/(32*25) = 4536."""
        coeffs = picard_fuchs_recursion(5)
        expected = Fraction(math.factorial(10), math.factorial(2) ** 5 * 5 ** 2)
        # VERIFIED [DC] (10!)/(32*25) = 3628800/800 = 4536
        assert coeffs[2] == expected

    def test_a_n_formula(self):
        """a_n = (5n)! / ((n!)^5 * 5^n) for n = 0, ..., 5.

        Multi-path verification: the recursion output matches the closed-form.
        Path 1: recursive computation from the PF operator.
        Path 2: closed-form (5n)!/((n!)^5 * 5^n).
        """
        coeffs = picard_fuchs_recursion(5)
        for n in range(6):
            expected = Fraction(
                math.factorial(5 * n), math.factorial(n) ** 5 * 5 ** n
            )
            assert coeffs[n] == expected, f"a_{n}: {coeffs[n]} != {expected}"

    def test_ratio_convergence(self):
        """a_{n+1}/a_n -> 625 = 5^4 as n -> infinity.

        The recursion (5n+1)(5n+2)(5n+3)(5n+4)/(n+1)^4 -> 5^4 = 625
        by Stirling / direct asymptotics.
        """
        ratios = picard_fuchs_ratio_convergence(50)
        last_ratio = ratios[-1]["ratio_float"]
        # Convergence is slow (O(1/n)), so at n=50 within ~25 of 625
        assert abs(last_ratio - 625.0) < 30.0

    def test_radius_of_convergence(self):
        """Radius of convergence is 1/625 in the recursion variable.

        The asymptotic ratio a_{n+1}/a_n -> 625, so R = 1/625.
        In the standard COGP variable z = psi^{-5}, the coefficients are
        (5n)!/(n!)^5 with ratio -> 3125 and radius 1/3125. The difference
        is the 5^n normalization factor.
        """
        ratios = picard_fuchs_ratio_convergence(50)
        last_ratio = ratios[-1]["ratio_float"]
        radius = 1.0 / last_ratio
        # 1/625 = 0.0016, allow ~10% tolerance from slow convergence
        assert abs(radius - 1.0 / 625) < 2e-4


# ======================================================================
# 13. SHADOW COEFFICIENTS S_2, S_3, S_4
# ======================================================================

class TestShadowCoefficients:
    """Tests for the main shadow coefficient computation."""

    def test_s2(self):
        """S_2 = kappa_ch = -25/3."""
        coeffs = quintic_shadow_coefficients()
        assert coeffs.S_2 == Fraction(-25, 3)

    def test_s3_classical(self):
        """S_3 (classical) = alpha = -3/5."""
        coeffs = quintic_shadow_coefficients()
        assert coeffs.S_3_classical == Fraction(-3, 5)

    def test_s3_instanton_leading(self):
        """Leading instanton correction to S_3 is -345."""
        coeffs = quintic_shadow_coefficients()
        # 2875 * (-3/25) = -345
        assert coeffs.S_3_instanton_leading == Fraction(-345)

    def test_s4_classical_zero(self):
        """S_4 = 0 classically."""
        coeffs = quintic_shadow_coefficients()
        assert coeffs.S_4_classical == Fraction(0)

    def test_shadow_class_m(self):
        """Shadow class is M (promoted by instantons)."""
        coeffs = quintic_shadow_coefficients()
        assert "M" in coeffs.shadow_class

    def test_degeneration_type_specified(self):
        """Degeneration type is specified (AP157)."""
        coeffs = quintic_shadow_coefficients()
        assert "LCS" in coeffs.degeneration_type or "large" in coeffs.degeneration_type

    def test_s2_matches_tower(self):
        """S_2 from coefficients matches S_2 from recursive tower."""
        coeffs = quintic_shadow_coefficients()
        tower = quintic_shadow_tower_classical()
        assert coeffs.S_2 == tower[2]

    def test_s3_matches_tower(self):
        """S_3 from coefficients matches S_3 from recursive tower."""
        coeffs = quintic_shadow_coefficients()
        tower = quintic_shadow_tower_classical()
        assert coeffs.S_3_classical == tower[3]


# ======================================================================
# 14. INSTANTON-CORRECTED SHADOW
# ======================================================================

class TestInstantonCorrectedShadow:
    """Tests for the instanton-corrected shadow coefficients."""

    def test_alpha_classical(self):
        """Classical alpha = -3/5."""
        data = instanton_corrected_shadow_quintic()
        assert data.alpha_classical == Fraction(-3, 5)

    def test_alpha_inst_d1(self):
        """Alpha instanton at d=1: 2875 / (-25/3) = -345."""
        data = instanton_corrected_shadow_quintic()
        assert data.alpha_instanton_coeffs[1] == Fraction(-345)

    def test_alpha_inst_d1_derivation(self):
        """Verify alpha_1 derivation: n^0_1 * 1^3 / kappa = 2875/(-25/3)."""
        # Yukawa coefficient at q^1: c_1 = n^0_1 * 1^3 = 2875
        # alpha_1 = c_1 / kappa = 2875 / (-25/3) = 2875 * (-3/25) = -345
        result = Fraction(2875) / Fraction(-25, 3)
        assert result == Fraction(-345)

    def test_s4_inst_d1(self):
        """S_4 instanton at d=1: 2875 / (-25/3) = -345."""
        data = instanton_corrected_shadow_quintic()
        # n^0_1 * 1^4 / kappa = 2875 / (-25/3) = -345
        assert data.s4_instanton_coeffs[1] == Fraction(-345)

    def test_shadow_class(self):
        """Shadow class is M."""
        data = instanton_corrected_shadow_quintic()
        assert data.shadow_class == "M"


# ======================================================================
# 15. MASTER SUMMARY
# ======================================================================

class TestMasterSummary:
    """Tests for the master summary function."""

    def test_summary_runs(self):
        """Summary function produces output without error."""
        summary = quintic_shadow_tower_summary()
        assert "kappa_spectrum" in summary
        assert "shadow_coefficients" in summary
        assert "comparison_with_k3e" in summary

    def test_summary_conditional(self):
        """All results are marked conditional on CY-A_3."""
        summary = quintic_shadow_tower_summary()
        assert "CY-A_3" in summary["all_conditional_on"]

    def test_summary_degeneration_types(self):
        """Summary includes all degeneration types."""
        summary = quintic_shadow_tower_summary()
        types = summary["degeneration_types"]
        assert len(types) == 3

    def test_summary_kappa_ch(self):
        """Summary has kappa_ch = -25/3."""
        summary = quintic_shadow_tower_summary()
        assert summary["kappa_spectrum"]["kappa_ch"] == "-25/3"

    def test_summary_mirror_sum(self):
        """Mirror kappa sum = 0."""
        summary = quintic_shadow_tower_summary()
        assert summary["mirror_kappa_sum"] == "0"


# ======================================================================
# 16. CROSS-CHECKS AND CONSISTENCY
# ======================================================================

class TestCrossChecks:
    """Cross-checks between different computations."""

    def test_alpha_sign_consistency(self):
        """alpha = C/kappa: C > 0, kappa < 0, so alpha < 0."""
        data = classical_shadow_data_quintic()
        assert data.yukawa_classical > 0
        assert data.kappa_ch < 0
        assert data.alpha_classical < 0

    def test_f1_matches_bcov(self):
        """F_1 = kappa_ch/24 = -25/72 matches BCOV constant map."""
        # cy_to_chiral.tex line 2185: "F_1 = -25/72 matches"
        tower = quintic_scalar_shadow_tower()
        assert tower[1] == Fraction(-25, 72)

    def test_shadow_metric_positive_at_origin(self):
        """Q_L(0) > 0 (positive definite at t=0)."""
        metric = shadow_metric_quintic()
        assert metric["q0"] > 0

    def test_kappa_spectrum_consistent(self):
        """kappa_ch from spectrum matches kappa from classical data."""
        spec = quintic_kappa_spectrum()
        data = classical_shadow_data_quintic()
        assert spec.kappa_ch == data.kappa_ch

    def test_tower_s2_equals_kappa(self):
        """S_2 = kappa_ch from the recursive tower."""
        tower = quintic_shadow_tower_classical()
        kappa = Fraction(-25, 3)
        assert tower[2] == kappa

    def test_tower_s3_equals_alpha(self):
        """S_3 = alpha from the recursive tower."""
        tower = quintic_shadow_tower_classical()
        alpha = Fraction(-3, 5)
        assert tower[3] == alpha

    def test_chi_from_hodge(self):
        """chi = 2*(h^{1,1} - h^{2,1}) = 2*(1-101) = -200."""
        data = classical_shadow_data_quintic()
        assert data.chi == 2 * (data.h11 - data.h21)
        assert data.chi == -200

    def test_kappa_from_chi(self):
        """kappa_ch = chi/24 = -200/24 = -25/3."""
        data = classical_shadow_data_quintic()
        assert data.kappa_ch == Fraction(data.chi, 24)
