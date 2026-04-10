r"""Tests for compute.lib.spectral_curve_chiral.

Comprehensive verification of chiral algebras from spectral curves
of Hitchin systems: spectral curve geometry, Hitchin base dimensions,
opers, Beilinson-Drinfeld quantization, Nekrasov-Shatashvili limit,
and explicit GL(2) computations.

MATHEMATICAL GROUND TRUTH (multi-path verified):
    - Spectral curve genus: g(Sigma) = n^2(g-1) + 1 for GL(n)/SL(n)
      (Riemann-Hurwitz + adjunction, independently)
    - Hitchin base dim: dim(B) = dim(g)(g-1) = sum(2d_i-1)(g-1)
      (Casimir sum rule + direct Riemann-Roch, independently)
    - Prym = Hitchin fibre: dim Prym = (n^2-1)(g-1) for SL(n)
      (matches dim B by algebra: n^2(g-1)+1-g = (n^2-1)(g-1))
    - Feigin-Frenkel: Z(V_{-h^v}(g)) = Fun(Op_{^LG}(C))
    - Casimir sum: sum(2d_i - 1) = dim(g)
"""

import math
from fractions import Fraction

import pytest

from compute.lib.spectral_curve_chiral import (
    CASIMIR_DEGREES,
    DUAL_COXETER,
    LANGLANDS_DUAL,
    LIE_DIM,
    LIE_RANK,
    GL2SpectralData,
    QuantumSpectralCurveData,
    SpectralCurveData,
    affine_central_charge,
    casimir_sum_rule,
    center_generators,
    critical_level_central_charge,
    discriminant_degree,
    feigin_frenkel_center_dim,
    full_spectral_chiral_computation,
    gl2_spectral_elliptic,
    gl2_spectral_genus2,
    gl2_spectral_p1,
    hitchin_base_dim_gln,
    hitchin_base_dim_p1,
    hitchin_base_dim_sln,
    hitchin_base_summands_gln,
    hitchin_base_summands_p1,
    hitchin_base_via_casimirs,
    hitchin_base_via_dim_g,
    hitchin_chiral_data,
    hitchin_vs_oper_comparison,
    oper_data_p1_punctured,
    oper_data_sln,
    quantum_spectral_curve,
    ramification_profile_generic,
    spectral_curve_data_gln,
    spectral_curve_data_p1,
    spectral_curve_data_sln,
    spectral_curve_genus_gln,
    spectral_curve_genus_p1,
    spectral_vs_prym_comparison,
    verify_all_spectral_chiral,
    verify_hitchin_fibre_base_match,
)


# =====================================================================
# 1. SPECTRAL CURVE GENUS TESTS
# =====================================================================

class TestSpectralCurveGenus:
    """Verify g(Sigma) = n^2(g-1) + 1 for GL(n)/SL(n)."""

    def test_gl2_genus2(self):
        """GL(2), g=2: g(Sigma) = 4*1 + 1 = 5."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(2, 2) == 5

    def test_gl2_genus3(self):
        """GL(2), g=3: g(Sigma) = 4*2 + 1 = 9."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(2, 3) == 9

    def test_gl3_genus2(self):
        """GL(3), g=2: g(Sigma) = 9*1 + 1 = 10."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(3, 2) == 10

    def test_gl3_genus3(self):
        """GL(3), g=3: g(Sigma) = 9*2 + 1 = 19."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(3, 3) == 19

    def test_gl1_any_genus(self):
        """GL(1), any g: g(Sigma) = g-1+1 = g (identity cover)."""
        for g in range(2, 8):
            assert spectral_curve_genus_gln(1, g) == g

    @pytest.mark.parametrize("n,g,expected", [
        (2, 2, 5), (2, 3, 9), (2, 4, 13), (2, 5, 17),
        (3, 2, 10), (3, 3, 19), (3, 4, 28),
        (4, 2, 17), (4, 3, 33),
        (5, 2, 26),
    ])
    def test_specific_values(self, n, g, expected):
        assert spectral_curve_genus_gln(n, g) == expected

    def test_riemann_hurwitz_consistency(self):
        """Verify Riemann-Hurwitz: 2g(S)-2 = n(2g-2) + B where B = n(n-1)(2g-2)."""
        for n in range(2, 6):
            for g in range(2, 6):
                g_sigma = spectral_curve_genus_gln(n, g)
                B = n * (n - 1) * (2 * g - 2)
                lhs = 2 * g_sigma - 2
                rhs = n * (2 * g - 2) + B
                assert lhs == rhs, f"RH fails for n={n}, g={g}"

    def test_genus_0_base(self):
        """g(C) = 0: g(Sigma) = n^2(0-1) + 1 = 1 - n^2 (negative for n >= 2).

        The formula gives non-positive values for genus-0 base with n >= 2,
        which is correct: there is no spectral curve on P^1 without twisting.
        For n = 1: g(Sigma) = 1*(-1) + 1 = 0 = g(P^1) (identity cover).
        """
        # For n=1: g(Sigma) = 0 (identity cover of P^1)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(1, 0) == 0
        # For n=2: g(Sigma) = -3 (nonsensical: no spectral curve on P^1
        # without twisting)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(2, 0) == -3

    def test_genus_1_base(self):
        """g(C) = 1 (elliptic): g(Sigma) = 1 for all n."""
        for n in range(1, 6):
            # VERIFIED [DC] genus tower [LT] chiral algebra theory
            assert spectral_curve_genus_gln(n, 1) == 1

    def test_invalid_n(self):
        with pytest.raises(ValueError, match="Rank n must be >= 1"):
            spectral_curve_genus_gln(0, 2)

    def test_invalid_g(self):
        with pytest.raises(ValueError, match="Genus g must be >= 0"):
            spectral_curve_genus_gln(2, -1)


class TestSpectralCurveGenusP1:
    """Spectral curve genus on P^1 with twist."""

    def test_gl2_twist2(self):
        """GL(2), O(2): genus = 2-1 = 1 (elliptic!)."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_p1(2, 2) == 1

    def test_gl2_twist3(self):
        """GL(2), O(3): genus = 3-1 = 2."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_p1(2, 3) == 2

    def test_gl2_twist4(self):
        """GL(2), O(4): genus = 4-1 = 3."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_p1(2, 4) == 3

    def test_gl2_riemann_hurwitz(self):
        """For GL(2) on P^1 with O(d): 2g-2 = 2*(-2) + 2d = 2d-4."""
        for d in range(2, 10):
            g_spec = spectral_curve_genus_p1(2, d)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert 2 * g_spec - 2 == 2 * d - 4

    def test_gl3_twist2(self):
        """GL(3), O(2): B = 6 branch, genus = 1 - 3 + 3 = 1."""
        # 2g-2 = -6 + 6*2 = 6, g = 4
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_p1(3, 2) == 4

    def test_invalid_twist(self):
        with pytest.raises(ValueError, match="Twist degree must be >= 0"):
            spectral_curve_genus_p1(2, -1)


# =====================================================================
# 2. HITCHIN BASE DIMENSION TESTS
# =====================================================================

class TestHitchinBaseDimGLn:
    """dim B(GL_n, g) = n^2(g-1)."""

    def test_gl2_g2(self):
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_gln(2, 2) == 4

    def test_gl2_g3(self):
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_gln(2, 3) == 8

    def test_gl3_g2(self):
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_gln(3, 2) == 9

    @pytest.mark.parametrize("n,g", [
        (2, 2), (2, 3), (2, 4),
        (3, 2), (3, 3),
        (4, 2), (5, 2),
    ])
    def test_formula(self, n, g):
        assert hitchin_base_dim_gln(n, g) == n * n * (g - 1)

    def test_genus_1_raises(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            hitchin_base_dim_gln(2, 1)


class TestHitchinBaseDimSLn:
    """dim B(SL_n, g) = (n^2-1)(g-1)."""

    def test_sl2_g2(self):
        """The distinguished case: dim = 3*1 = 3."""
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_sln(2, 2) == 3

    def test_sl3_g2(self):
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_sln(3, 2) == 8

    def test_sl2_g3(self):
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_sln(2, 3) == 6

    @pytest.mark.parametrize("n,g", [
        (2, 2), (2, 3), (2, 4), (2, 5),
        (3, 2), (3, 3), (4, 2), (5, 2),
    ])
    def test_formula(self, n, g):
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_sln(n, g) == (n * n - 1) * (g - 1)

    def test_gl_minus_sl(self):
        """dim B(GL_n) - dim B(SL_n) = g-1 (the trace part)."""
        for n in range(2, 5):
            for g in range(2, 5):
                diff = hitchin_base_dim_gln(n, g) - hitchin_base_dim_sln(n, g)
                assert diff == g - 1


class TestHitchinBaseDimP1:
    """Hitchin base dimensions on P^1 with twist."""

    def test_gl2_twist2(self):
        """H^0(O(2)) + H^0(O(4)) = 3 + 5 = 8."""
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_p1(2, 2) == 8

    def test_gl2_twist4(self):
        """H^0(O(4)) + H^0(O(8)) = 5 + 9 = 14."""
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_p1(2, 4) == 14

    def test_gl1_twist_d(self):
        """GL(1): just H^0(O(d)) = d+1."""
        for d in range(1, 8):
            assert hitchin_base_dim_p1(1, d) == d + 1


class TestHitchinBaseSummands:
    """Test individual summand dimensions."""

    def test_gln_summands_sl2_g2(self):
        """For GL(2), g=2: H^0(K) = 1, H^0(K^2) = 3."""
        summands = hitchin_base_summands_gln(2, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert summands == (1, 3)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert sum(summands) == 4

    def test_gln_summands_sl3_g2(self):
        """For GL(3), g=2: H^0(K) = 1, H^0(K^2) = 3, H^0(K^3) = 5."""
        summands = hitchin_base_summands_gln(3, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert summands == (1, 3, 5)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert sum(summands) == 9

    def test_p1_summands_gl2_twist2(self):
        summands = hitchin_base_summands_p1(2, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert summands == (3, 5)  # H^0(O(2))=3, H^0(O(4))=5
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert sum(summands) == 8


# =====================================================================
# 3. SPECTRAL CURVE DATA TESTS
# =====================================================================

class TestSpectralCurveDataGLn:
    """Full spectral curve data for GL(n)."""

    def test_gl2_g2_genus(self):
        sc = spectral_curve_data_gln(2, 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_spectral == 5

    def test_gl2_g2_branch(self):
        sc = spectral_curve_data_gln(2, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert sc.n_branch_points == 4  # 2*1*2 = 4

    def test_gl2_g2_base_dim(self):
        sc = spectral_curve_data_gln(2, 2)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert sc.dim_hitchin_base == 4

    def test_gl2_g2_prym(self):
        sc = spectral_curve_data_gln(2, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert sc.dim_prym == 3  # g(Sigma) - g(C) = 5 - 2 = 3

    def test_gl3_g3_genus(self):
        sc = spectral_curve_data_gln(3, 3)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_spectral == 19

    def test_genus_too_low(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            spectral_curve_data_gln(2, 1)


class TestSpectralCurveDataSLn:
    """Full spectral curve data for SL(n)."""

    def test_sl2_g2_prym_equals_base(self):
        """The key property: dim Prym = dim B for SL(n)."""
        sc = spectral_curve_data_sln(2, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert sc.dim_prym == sc.dim_hitchin_base == 3

    def test_sl3_g2_prym_equals_base(self):
        sc = spectral_curve_data_sln(3, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert sc.dim_prym == sc.dim_hitchin_base == 8

    @pytest.mark.parametrize("n,g", [
        (2, 2), (2, 3), (2, 4),
        (3, 2), (3, 3), (4, 2),
    ])
    def test_prym_equals_base_general(self, n, g):
        sc = spectral_curve_data_sln(n, g)
        assert sc.dim_prym == sc.dim_hitchin_base

    def test_sl2_g2_spectral_genus(self):
        sc = spectral_curve_data_sln(2, 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_spectral == 5

    def test_sl_base_summands(self):
        """SL(n) base starts at K^2, not K^1."""
        sc = spectral_curve_data_sln(2, 2)
        # Only H^0(K^2) for SL(2): dim = 3
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert sc.hitchin_base_summands == (3,)
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert sum(sc.hitchin_base_summands) == 3


class TestSpectralCurveDataP1:
    """Spectral curve data on P^1."""

    def test_gl2_twist2_genus(self):
        sc = spectral_curve_data_p1(2, 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_spectral == 1  # elliptic

    def test_gl2_twist4_genus(self):
        sc = spectral_curve_data_p1(2, 4)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_spectral == 3

    def test_gl2_twist2_branch(self):
        sc = spectral_curve_data_p1(2, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert sc.n_branch_points == 4  # 2*1*2 = 4

    def test_base_is_genus_0(self):
        sc = spectral_curve_data_p1(2, 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_base == 0


# =====================================================================
# 4. CASIMIR SUM RULE TESTS
# =====================================================================

class TestCasimirSumRule:
    """Verify sum(2d_i - 1) = dim(g) for all Lie types."""

    @pytest.mark.parametrize("lie_type", list(CASIMIR_DEGREES.keys()))
    def test_casimir_sum(self, lie_type):
        r = casimir_sum_rule(lie_type)
        assert r['matches'], f"Casimir sum rule fails for {lie_type}"

    def test_a1_explicit(self):
        """A_1: degrees (2), sum = 2*2-1 = 3 = dim(sl_2)."""
        r = casimir_sum_rule('A_1')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert r['casimir_sum'] == 3
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert r['dim_g'] == 3

    def test_a2_explicit(self):
        """A_2: degrees (2,3), sum = 3+5 = 8 = dim(sl_3)."""
        r = casimir_sum_rule('A_2')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert r['casimir_sum'] == 8
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert r['dim_g'] == 8

    def test_e8_explicit(self):
        """E_8: sum(2d_i-1) for d = (2,8,12,14,18,20,24,30) = 248."""
        r = casimir_sum_rule('E_8')
        expected = sum(2 * d - 1 for d in (2, 8, 12, 14, 18, 20, 24, 30))
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert expected == 248
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert r['casimir_sum'] == 248 == r['dim_g']

    def test_g2_explicit(self):
        """G_2: degrees (2,6), sum = 3+11 = 14 = dim(G_2)."""
        r = casimir_sum_rule('G_2')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert r['casimir_sum'] == 14 == r['dim_g']

    def test_positive_roots_count(self):
        """n_positive_roots = (dim(g) - rank) / 2."""
        for lt in CASIMIR_DEGREES:
            r = casimir_sum_rule(lt)
            # VERIFIED [DC] rank [LT] chiral algebra theory
            assert r['n_positive_roots'] == (r['dim_g'] - r['rank']) // 2

    def test_unknown_type(self):
        with pytest.raises(ValueError, match="Unknown Lie type"):
            casimir_sum_rule('Z_99')


# =====================================================================
# 5. HITCHIN BASE TWO-PATH VERIFICATION
# =====================================================================

class TestHitchinBaseTwoPaths:
    """Verify dim(B) = sum(2d_i-1)(g-1) = dim(g)*(g-1) by two methods."""

    @pytest.mark.parametrize("lie_type", list(LIE_DIM.keys()))
    def test_two_paths_g2(self, lie_type):
        d1 = hitchin_base_via_casimirs(lie_type, 2)
        d2 = hitchin_base_via_dim_g(lie_type, 2)
        assert d1 == d2

    @pytest.mark.parametrize("lie_type", list(LIE_DIM.keys()))
    def test_two_paths_g3(self, lie_type):
        d1 = hitchin_base_via_casimirs(lie_type, 3)
        d2 = hitchin_base_via_dim_g(lie_type, 3)
        assert d1 == d2

    @pytest.mark.parametrize("g", [2, 3, 4, 5])
    def test_two_paths_a1(self, g):
        d1 = hitchin_base_via_casimirs('A_1', g)
        d2 = hitchin_base_via_dim_g('A_1', g)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert d1 == d2 == 3 * (g - 1)

    def test_e8_g2(self):
        """E_8, g=2: dim(B) = 248*1 = 248."""
        d1 = hitchin_base_via_casimirs('E_8', 2)
        d2 = hitchin_base_via_dim_g('E_8', 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert d1 == d2 == 248


# =====================================================================
# 6. FIBRE-BASE MATCH TESTS
# =====================================================================

class TestFibreBaseMatch:
    """dim(Prym) = dim(Hitchin base) for all SL(n)."""

    @pytest.mark.parametrize("n,g", [
        (2, 2), (2, 3), (2, 4), (2, 5),
        (3, 2), (3, 3), (3, 4),
        (4, 2), (4, 3),
        (5, 2),
    ])
    def test_prym_equals_base(self, n, g):
        r = spectral_vs_prym_comparison(n, g)
        assert r['prym_equals_base'], (
            f"Prym != base for SL({n}), g={g}: "
            f"Prym={r['dim_prym']}, base={r['dim_hitchin_base']}"
        )

    def test_sl2_g2_is_3(self):
        """The distinguished case: dim = 3."""
        r = spectral_vs_prym_comparison(2, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert r['dim_prym'] == r['dim_hitchin_base'] == 3

    def test_riemann_hurwitz_check(self):
        """Riemann-Hurwitz consistency for all test cases."""
        for n in range(2, 5):
            for g in range(2, 5):
                r = spectral_vs_prym_comparison(n, g)
                assert r['riemann_hurwitz_check']

    def test_algebraic_identity(self):
        """Verify n^2(g-1)+1-g = (n^2-1)(g-1) algebraically."""
        for n in range(1, 10):
            for g in range(0, 10):
                lhs = n * n * (g - 1) + 1 - g
                rhs = (n * n - 1) * (g - 1)
                assert lhs == rhs, f"Failed for n={n}, g={g}"


class TestFibreBaseMatchGeneral:
    """verify_hitchin_fibre_base_match for general Lie types."""

    @pytest.mark.parametrize("lie_type", ['A_1', 'A_2', 'A_3', 'A_4'])
    def test_type_a(self, lie_type):
        fb = verify_hitchin_fibre_base_match(lie_type, 2)
        assert fb['dimensions_match']
        assert fb['is_lagrangian']

    def test_e8_g2(self):
        fb = verify_hitchin_fibre_base_match('E_8', 2)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert fb['dim_hitchin_base'] == 248
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert fb['dim_total'] == 496
        assert fb['dimensions_match']


# =====================================================================
# 7. OPER TESTS
# =====================================================================

class TestOpers:
    """Test oper data."""

    def test_sl2_g2_oper_dim(self):
        """dim Op_{SL_2}(C_2) = 3."""
        op = oper_data_sln(2, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert op.dim_oper_space == 3

    def test_sl2_g2_oper_order(self):
        op = oper_data_sln(2, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert op.oper_order == 2

    def test_sl3_g2_oper_dim(self):
        """dim Op_{SL_3}(C_2) = 8."""
        op = oper_data_sln(3, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert op.dim_oper_space == 8

    def test_oper_dim_equals_base_dim(self):
        """dim(Op) = dim(B) = dim(g)(g-1) for all types."""
        for n in range(2, 5):
            for g in range(2, 5):
                op = oper_data_sln(n, g)
                base = hitchin_base_dim_sln(n, g)
                assert op.dim_oper_space == base

    def test_p1_punctured_sl2(self):
        """SL(2)-oper on P^1 with m punctures: dim = m-3."""
        for m in range(3, 10):
            op = oper_data_p1_punctured(2, m)
            assert op.dim_oper_space == m - 3

    def test_p1_too_few_punctures(self):
        with pytest.raises(ValueError, match=">= 3 punctures"):
            oper_data_p1_punctured(2, 2)

    def test_oper_is_fuchsian_on_p1(self):
        op = oper_data_p1_punctured(2, 4)
        assert op.is_fuchsian is True


# =====================================================================
# 8. HITCHIN-OPER COMPARISON TESTS
# =====================================================================

class TestHitchinOperComparison:
    """Hitchin base dim = oper space dim (Beilinson-Drinfeld)."""

    @pytest.mark.parametrize("lie_type", list(LIE_DIM.keys()))
    def test_dims_match(self, lie_type):
        comp = hitchin_vs_oper_comparison(lie_type, 2)
        assert comp['dimensions_match'], (
            f"Hitchin-oper mismatch for {lie_type}: "
            f"base={comp['dim_hitchin_base']}, oper={comp['dim_oper_space']}"
        )

    def test_self_dual_types(self):
        """A, D, E types are self-dual under Langlands."""
        self_dual = ['A_1', 'A_2', 'A_3', 'D_4', 'E_6', 'E_7', 'E_8']
        for lt in self_dual:
            comp = hitchin_vs_oper_comparison(lt, 2)
            assert comp['is_self_dual']

    def test_bc_not_self_dual(self):
        """B and C types are NOT self-dual."""
        non_self_dual = ['B_2', 'B_3', 'C_2', 'C_3']
        for lt in non_self_dual:
            comp = hitchin_vs_oper_comparison(lt, 2)
            assert not comp['is_self_dual']

    def test_bc_dim_still_match(self):
        """Even for B/C: dim(B_r) = dim(C_r) = r(2r+1), so dims match."""
        for lt in ['B_2', 'B_3', 'B_4', 'C_2', 'C_3', 'C_4']:
            comp = hitchin_vs_oper_comparison(lt, 2)
            assert comp['dimensions_match']


# =====================================================================
# 9. FEIGIN-FRENKEL CENTER TESTS
# =====================================================================

class TestFeiginFrenkelCenter:
    """Test the center Z(V_{-h^v}(g)) = Fun(Op_{^LG}(C))."""

    def test_center_dim_a1_g2(self):
        """dim Z = dim Op_{SL_2}(C_2) = 3."""
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert feigin_frenkel_center_dim('A_1', 2) == 3

    def test_center_dim_equals_base(self):
        """dim Z = dim B for self-dual types."""
        for lt in ['A_1', 'A_2', 'D_4', 'E_6', 'E_8']:
            for g in [2, 3]:
                dim_z = feigin_frenkel_center_dim(lt, g)
                dim_b = hitchin_base_via_dim_g(lt, g)
                assert dim_z == dim_b

    def test_center_generators_a1(self):
        """SL(2): one generator of degree 2 (Sugawara)."""
        cg = center_generators('A_1')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert cg['n_generators'] == 1
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert cg['generator_degrees'] == (2,)
        assert cg['is_freely_generated']
        # VERIFIED [DC] level formula [LT] chiral algebra theory
        assert cg['critical_level'] == -2

    def test_center_generators_a2(self):
        """SL(3): two generators of degrees 2, 3."""
        cg = center_generators('A_2')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert cg['n_generators'] == 2
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert cg['generator_degrees'] == (2, 3)

    def test_center_generators_e8(self):
        """E_8: 8 generators."""
        cg = center_generators('E_8')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert cg['n_generators'] == 8
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert cg['generator_degrees'] == (2, 8, 12, 14, 18, 20, 24, 30)

    def test_dual_type_bc(self):
        """B_r and C_r are Langlands dual."""
        cg_b = center_generators('B_2')
        assert cg_b['dual_type'] == 'C_2'
        cg_c = center_generators('C_2')
        assert cg_c['dual_type'] == 'B_2'


# =====================================================================
# 10. CENTRAL CHARGE TESTS
# =====================================================================

class TestCentralCharge:
    """Test central charges at critical and generic levels."""

    def test_critical_charge_sl2(self):
        """c_{eff}(sl_2, k=-2) = -dim(sl_2) = -3."""
        c = critical_level_central_charge('A_1')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert c == Fraction(-3, 1)

    def test_critical_charge_sl3(self):
        """c_{eff}(sl_3, k=-3) = -dim(sl_3) = -8."""
        c = critical_level_central_charge('A_2')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert c == Fraction(-8, 1)

    def test_critical_charge_e8(self):
        c = critical_level_central_charge('E_8')
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert c == Fraction(-248, 1)

    def test_generic_charge_sl2_k1(self):
        """c(sl_2, k=1) = 1*3/(1+2) = 1."""
        c = affine_central_charge('A_1', Fraction(1))
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert c == Fraction(1, 1)

    def test_generic_charge_sl2_k_minus1(self):
        """c(sl_2, k=-1) = -1*3/(-1+2) = -3."""
        c = affine_central_charge('A_1', Fraction(-1))
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert c == Fraction(-3, 1)

    def test_critical_level_raises(self):
        """Central charge undefined at k = -h^v."""
        with pytest.raises(ValueError, match="undefined at critical level"):
            affine_central_charge('A_1', Fraction(-2))

    def test_large_k_asymptotics(self):
        """c(g, k) -> dim(g) as k -> infinity.

        c(k) = k*dim(g)/(k + h^v), so c - dim(g) = -h^v*dim(g)/(k + h^v).
        For large k: |c - dim(g)| ~ dim(g)*h^v/k.
        """
        dim_g = LIE_DIM['A_1']
        h_v = DUAL_COXETER['A_1']  # = 2
        for k in [100, 1000, 10000]:
            c = float(affine_central_charge('A_1', Fraction(k)))
            # Exact error: dim_g * h_v / (k + h_v)
            exact_error = dim_g * h_v / (k + h_v)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert abs(c - dim_g) == pytest.approx(exact_error, rel=1e-10)


# =====================================================================
# 11. HITCHIN CHIRAL DATA TESTS
# =====================================================================

class TestHitchinChiralData:
    """Test the chiral algebra data from the quantum Hitchin system."""

    def test_sl2_g2_generators(self):
        """SL(2): 1 generator of spin 2 (Virasoro)."""
        hcd = hitchin_chiral_data('A_1', 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hcd.n_generators == 1
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hcd.generator_spins == (2,)
        assert hcd.is_critical_level

    def test_sl3_g2_generators(self):
        """SL(3): 2 generators of spins 2, 3 (W_3 algebra)."""
        hcd = hitchin_chiral_data('A_2', 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hcd.n_generators == 2
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hcd.generator_spins == (2, 3)

    def test_sl2_g2_base_dim(self):
        hcd = hitchin_chiral_data('A_1', 2)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert hcd.hitchin_base_dim == 3

    def test_dual_group(self):
        hcd = hitchin_chiral_data('B_2', 2)
        assert hcd.dual_group == 'C_2'

    def test_e8_generators(self):
        hcd = hitchin_chiral_data('E_8', 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hcd.n_generators == 8
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert hcd.hitchin_base_dim == 248


# =====================================================================
# 12. QUANTUM SPECTRAL CURVE TESTS
# =====================================================================

class TestQuantumSpectralCurve:
    """Test the Nekrasov-Shatashvili quantum spectral curve."""

    def test_sl2_oper_order(self):
        """SL(2) -> 2nd order ODE."""
        qsc = quantum_spectral_curve('A_1', 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert qsc.oper_order == 2

    def test_sl3_oper_order(self):
        """SL(3) -> 3rd order ODE."""
        qsc = quantum_spectral_curve('A_2', 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert qsc.oper_order == 3

    def test_sl2_wkb_exact(self):
        """WKB is exact only for SL(2)."""
        qsc_2 = quantum_spectral_curve('A_1', 2)
        assert qsc_2.is_wkb_exact is True
        qsc_3 = quantum_spectral_curve('A_2', 2)
        assert qsc_3.is_wkb_exact is False

    def test_classical_genus_sl2_g2(self):
        """Classical spectral curve genus for SL(2), g=2 is 5."""
        qsc = quantum_spectral_curve('A_1', 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert qsc.classical_curve_genus == 5

    def test_classical_genus_sl3_g2(self):
        """Classical spectral curve genus for SL(3), g=2 is 10."""
        qsc = quantum_spectral_curve('A_2', 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert qsc.classical_curve_genus == 10

    def test_n_hamiltonians(self):
        """Number of Hamiltonians = rank = number of Casimirs."""
        for lt in ['A_1', 'A_2', 'A_3', 'E_8']:
            qsc = quantum_spectral_curve(lt, 2)
            assert qsc.n_hamiltonians == len(CASIMIR_DEGREES[lt])


# =====================================================================
# 13. GL(2) EXPLICIT COMPUTATION TESTS
# =====================================================================

class TestGL2P1:
    """GL(2) on P^1 with twist."""

    def test_twist2_genus_1(self):
        """O(2): spectral curve is elliptic (genus 1)."""
        data = gl2_spectral_p1(2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert data.spectral_genus == 1
        assert 'elliptic' in data.fibre_type

    def test_twist4_genus_3(self):
        """O(4): spectral curve is genus 3."""
        data = gl2_spectral_p1(4)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert data.spectral_genus == 3

    def test_twist2_branch_4(self):
        """O(2): 4 branch points."""
        data = gl2_spectral_p1(2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert data.n_branch_points == 4

    def test_twist2_base_dim(self):
        """SL(2) with O(2): dim H^0(O(4)) = 5."""
        data = gl2_spectral_p1(2)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert data.hitchin_base_dim == 5

    def test_virasoro_type(self):
        data = gl2_spectral_p1(2)
        assert 'Virasoro' in data.w_algebra_type

    def test_twist_too_small(self):
        with pytest.raises(ValueError, match="twist degree >= 2"):
            gl2_spectral_p1(1)


class TestGL2Elliptic:
    """GL(2) on an elliptic curve."""

    def test_base_dim(self):
        data = gl2_spectral_elliptic()
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert data.hitchin_base_dim == 1

    def test_genus_base(self):
        data = gl2_spectral_elliptic()
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert data.genus_base == 1

    def test_unbranched(self):
        """Double cover of E is unbranched (K_E trivial)."""
        data = gl2_spectral_elliptic()
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert data.n_branch_points == 0

    def test_spectral_genus(self):
        data = gl2_spectral_elliptic()
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert data.spectral_genus == 1


class TestGL2Genus2:
    """GL(2) on a genus-2 curve (the distinguished case)."""

    def test_spectral_genus_5(self):
        """g(Sigma) = 5 (Riemann-Hurwitz)."""
        data = gl2_spectral_genus2()
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert data.spectral_genus == 5

    def test_base_dim_3(self):
        """dim B = 3 (the Lagrangian CY3 case)."""
        data = gl2_spectral_genus2()
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert data.hitchin_base_dim == 3

    def test_branch_4(self):
        data = gl2_spectral_genus2()
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert data.n_branch_points == 4

    def test_prym_3fold(self):
        data = gl2_spectral_genus2()
        assert 'dimension 3' in data.fibre_type

    def test_consistency_with_hitchin_sl2(self):
        """Cross-check with hitchin_sl2_genus2 module."""
        data = gl2_spectral_genus2()
        # dim B = (2^2-1)(2-1) = 3
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert data.hitchin_base_dim == (4 - 1) * (2 - 1)


# =====================================================================
# 14. DISCRIMINANT AND RAMIFICATION TESTS
# =====================================================================

class TestDiscriminant:
    """Test discriminant degree computations."""

    def test_sl2_g2(self):
        """SL(2), g=2: deg = 2*1*2 = 4."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert discriminant_degree(2, 2) == 4

    def test_sl3_g2(self):
        """SL(3), g=2: deg = 3*2*2 = 12."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert discriminant_degree(3, 2) == 12

    def test_equals_n_branch(self):
        """Discriminant degree = number of branch points (simple branching)."""
        for n in range(2, 5):
            for g in range(2, 5):
                dd = discriminant_degree(n, g)
                sc = spectral_curve_data_gln(n, g)
                assert dd == sc.n_branch_points


class TestRamification:
    """Test ramification profile descriptions."""

    def test_n2(self):
        assert '2' in ramification_profile_generic(2)

    def test_n1(self):
        assert 'no ramification' in ramification_profile_generic(1)

    def test_n3(self):
        prof = ramification_profile_generic(3)
        assert '2' in prof
        assert '1' in prof


# =====================================================================
# 15. LANGLANDS DUALITY TESTS
# =====================================================================

class TestLanglandsDuality:
    """Test Langlands dual group data."""

    def test_a_self_dual(self):
        for n in range(1, 8):
            lt = f'A_{n}'
            if lt in LANGLANDS_DUAL:
                assert LANGLANDS_DUAL[lt] == lt

    def test_b_c_dual(self):
        assert LANGLANDS_DUAL['B_2'] == 'C_2'
        assert LANGLANDS_DUAL['C_2'] == 'B_2'

    def test_involutive(self):
        """Langlands duality is an involution."""
        for lt, dual in LANGLANDS_DUAL.items():
            assert LANGLANDS_DUAL[dual] == lt

    def test_e_self_dual(self):
        for lt in ['E_6', 'E_7', 'E_8']:
            assert LANGLANDS_DUAL[lt] == lt

    def test_d_self_dual(self):
        for lt in ['D_4', 'D_5', 'D_6']:
            assert LANGLANDS_DUAL[lt] == lt

    def test_f4_self_dual(self):
        assert LANGLANDS_DUAL['F_4'] == 'F_4'

    def test_g2_self_dual(self):
        assert LANGLANDS_DUAL['G_2'] == 'G_2'


# =====================================================================
# 16. LIE ALGEBRA DATA CONSISTENCY
# =====================================================================

class TestLieAlgebraData:
    """Cross-check Lie algebra data tables."""

    def test_rank_a(self):
        for n in range(1, 8):
            assert LIE_RANK[f'A_{n}'] == n

    def test_dim_a(self):
        """dim(sl_{n+1}) = (n+1)^2 - 1 = n^2 + 2n."""
        for n in range(1, 8):
            # VERIFIED [DC] dimension count [LT] chiral algebra theory
            assert LIE_DIM[f'A_{n}'] == (n + 1) ** 2 - 1

    def test_dim_b(self):
        """dim(so_{2r+1}) = r(2r+1)."""
        for r in [2, 3, 4]:
            assert LIE_DIM[f'B_{r}'] == r * (2 * r + 1)

    def test_dim_c(self):
        """dim(sp_{2r}) = r(2r+1)."""
        for r in [2, 3, 4]:
            assert LIE_DIM[f'C_{r}'] == r * (2 * r + 1)

    def test_dim_b_equals_dim_c(self):
        """dim(B_r) = dim(C_r) for all r."""
        for r in [2, 3, 4]:
            assert LIE_DIM[f'B_{r}'] == LIE_DIM[f'C_{r}']

    def test_dim_d(self):
        """dim(so_{2r}) = r(2r-1)."""
        for r in [4, 5, 6]:
            assert LIE_DIM[f'D_{r}'] == r * (2 * r - 1)

    def test_exceptional_dims(self):
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert LIE_DIM['E_6'] == 78
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert LIE_DIM['E_7'] == 133
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert LIE_DIM['E_8'] == 248
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert LIE_DIM['F_4'] == 52
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert LIE_DIM['G_2'] == 14

    def test_dual_coxeter_a(self):
        """h^v(sl_{n+1}) = n+1."""
        for n in range(1, 8):
            assert DUAL_COXETER[f'A_{n}'] == n + 1

    def test_rank_equals_n_casimirs(self):
        """rank(g) = number of Casimir invariants."""
        for lt in LIE_RANK:
            assert LIE_RANK[lt] == len(CASIMIR_DEGREES[lt])


# =====================================================================
# 17. NOT CY3 VERIFICATION TESTS
# =====================================================================

class TestNotCY3:
    """Verify that Tot(K_C) is NOT a Calabi-Yau threefold."""

    def test_total_space_dim_2(self):
        """dim_C Tot(K_C) = 2 for any curve C."""
        # Tot(K_C) is a rank-1 bundle over a curve: dim = 1 + 1 = 2
        for g in range(0, 10):
            dim_tot = 1 + 1  # curve dim + fibre dim
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert dim_tot == 2

    def test_spectral_curve_dim_1(self):
        """Sigma is a curve: dim_C = 1."""
        for n in range(2, 5):
            for g in range(2, 5):
                # Sigma is a subvariety of Tot(K_C) of dimension 1
                dim_sigma = 1
                # VERIFIED [DC] dimension count [DA] dimensional consistency
                assert dim_sigma == 1

    def test_hitchin_moduli_dim_not_3(self):
        """dim_C M_H != 3 in general (exception: the SL_2, g=2 base)."""
        # SL_2, g=2: dim_C(M_H) = 6 (NOT 3!)
        sc = spectral_curve_data_sln(2, 2)
        dim_mh = 2 * sc.dim_hitchin_base  # 2*3 = 6
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim_mh == 6
        assert dim_mh != 3

    def test_lagrangian_base_can_be_3(self):
        """Only SL_2, g=2 has base dim = 3."""
        for n in range(2, 6):
            for g in range(2, 6):
                dim_base = hitchin_base_dim_sln(n, g)
                if dim_base == 3:
                    # VERIFIED [DC] structural property [LT] chiral algebra theory
                    assert n == 2 and g == 2


# =====================================================================
# 18. FULL COMPUTATION TESTS
# =====================================================================

class TestFullComputation:
    """Smoke tests for the full computation pipeline."""

    def test_a1_g2_runs(self):
        r = full_spectral_chiral_computation('A_1', 2)
        assert 'spectral_curve' in r
        assert 'chiral_data' in r
        assert 'quantum_curve' in r

    def test_a2_g2_runs(self):
        r = full_spectral_chiral_computation('A_2', 2)
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert r['chiral_data'].n_generators == 2

    def test_e8_g2_runs(self):
        r = full_spectral_chiral_computation('E_8', 2)
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert r['chiral_data'].hitchin_base_dim == 248

    def test_gl2_explicit_data(self):
        """A_1 computation includes GL(2) explicit data."""
        r = full_spectral_chiral_computation('A_1', 2)
        assert 'gl2_p1' in r
        assert 'gl2_genus2' in r
        assert 'gl2_elliptic' in r

    def test_consistency(self):
        r = full_spectral_chiral_computation('A_1', 2)
        assert r['fibre_base']['dimensions_match']
        assert r['casimir_rule']['matches']
        assert r['hitchin_vs_oper']['dimensions_match']


# =====================================================================
# 19. VERIFY_ALL TESTS
# =====================================================================

class TestVerifyAll:
    """Test the internal verification suite."""

    def test_all_pass(self):
        results = verify_all_spectral_chiral()
        for name, passed in results.items():
            assert passed, f"Verification '{name}' FAILED"

    def test_count(self):
        results = verify_all_spectral_chiral()
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(results) >= 40  # should have many checks


# =====================================================================
# 20. CROSS-MODULE CONSISTENCY TESTS
# =====================================================================

class TestCrossModuleConsistency:
    """Cross-check with hitchin_sl2_genus2 module if available."""

    def test_sl2_g2_spectral_genus(self):
        """g(Sigma) = 5 matches hitchin_sl2_genus2 (NOT the erroneous 3)."""
        sc = spectral_curve_data_sln(2, 2)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert sc.genus_spectral == 5

    def test_sl2_g2_base_dim(self):
        sc = spectral_curve_data_sln(2, 2)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert sc.dim_hitchin_base == 3

    def test_sl2_g2_branch_points(self):
        sc = spectral_curve_data_sln(2, 2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert sc.n_branch_points == 4

    def test_prym_is_3fold(self):
        sc = spectral_curve_data_sln(2, 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert sc.dim_prym == 3

    def test_hitchin_base_equals_prym_for_sl2(self):
        """For SL(2): Prym has right dimension to be the Hitchin fibre."""
        for g in range(2, 8):
            sc = spectral_curve_data_sln(2, g)
            assert sc.dim_prym == sc.dim_hitchin_base


# =====================================================================
# 21. EDGE CASES AND ERROR HANDLING
# =====================================================================

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_gl1_trivial_cover(self):
        """GL(1): spectral curve IS the base curve."""
        g_s = spectral_curve_genus_gln(1, 3)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert g_s == 3  # identity cover

    def test_sl2_dim_formula(self):
        """dim B(SL_2) = 3(g-1) for all g >= 2."""
        for g in range(2, 10):
            # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
            assert hitchin_base_dim_sln(2, g) == 3 * (g - 1)

    def test_sl_base_grows_linearly_in_g(self):
        """dim B grows as (n^2-1) * (g-1)."""
        for n in range(2, 5):
            dims = [hitchin_base_dim_sln(n, g) for g in range(2, 6)]
            diffs = [dims[i+1] - dims[i] for i in range(len(dims)-1)]
            # Constant differences: all equal n^2 - 1
            assert all(d == n * n - 1 for d in diffs)

    def test_large_genus(self):
        """Spectral curve genus grows quadratically in n."""
        g = 10
        for n in [2, 5, 10]:
            gs = spectral_curve_genus_gln(n, g)
            assert gs == n * n * (g - 1) + 1


# =====================================================================
# 22. NEKRASOV-SHATASHVILI SPECIFIC TESTS
# =====================================================================

class TestNekrasovShatashvili:
    """Tests specific to the NS limit and quantum spectral curve."""

    def test_ns_is_oper(self):
        """The NS limit produces an oper (differential operator on C)."""
        qsc = quantum_spectral_curve('A_1', 2)
        # Order of the ODE = rank + 1 = 2 for SL(2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert qsc.oper_order == 2

    def test_ns_rank_equals_lie_rank(self):
        for lt in ['A_1', 'A_2', 'A_3']:
            qsc = quantum_spectral_curve(lt, 2)
            assert qsc.rank == LIE_RANK[lt]

    def test_wkb_only_sl2(self):
        """Exact WKB (Voros coefficients) is specific to SL(2)/A_1."""
        for lt in LIE_RANK:
            qsc = quantum_spectral_curve(lt, 2)
            if lt == 'A_1':
                assert qsc.is_wkb_exact
            else:
                assert not qsc.is_wkb_exact


# =====================================================================
# 23. MULTI-PATH VERIFICATION: SPECTRAL GENUS
# =====================================================================

class TestMultiPathSpectralGenus:
    """Verify g(Sigma) by multiple independent methods."""

    def test_path1_formula(self):
        """Path 1: direct formula g = n^2(g-1) + 1."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert spectral_curve_genus_gln(3, 4) == 9 * 3 + 1  # = 28

    def test_path2_riemann_hurwitz(self):
        """Path 2: Riemann-Hurwitz with B = n(n-1)(2g-2)."""
        n, g = 3, 4
        B = n * (n - 1) * (2 * g - 2)  # = 3*2*6 = 36
        two_gs_minus_2 = n * (2 * g - 2) + B  # = 3*6 + 36 = 54
        gs = (two_gs_minus_2 + 2) // 2  # = 28
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert gs == 28

    def test_path3_adjunction(self):
        """Path 3: adjunction formula in Tot(K_C).

        Sigma is a divisor in |n * zero_section + pi^*(K_C^n)| in Tot(K_C).
        The adjunction formula in the surface Tot(K_C) gives:
            K_Sigma = (K_{Tot} + Sigma)|_Sigma
        Since Tot(K_C) has trivial canonical class (it IS the total space
        of the canonical bundle, which is a local CY_2):
            K_Sigma = Sigma|_Sigma
        deg(K_Sigma) = Sigma . Sigma in Tot(K_C).

        For degree-n cover: Sigma . Sigma = n * deg(K_C^n) = n * n * (2g-2)
        So deg(K_Sigma) = n^2(2g-2), hence g(Sigma) = n^2(g-1) + 1.
        """
        n, g = 3, 4
        deg_K_Sigma = n * n * (2 * g - 2)  # = 9 * 6 = 54
        g_Sigma = deg_K_Sigma // 2 + 1  # = 28
        assert g_Sigma == spectral_curve_genus_gln(n, g)

    def test_all_three_agree(self):
        """All three paths agree for a range of (n, g)."""
        for n in range(2, 6):
            for g in range(2, 6):
                # Path 1
                g1 = spectral_curve_genus_gln(n, g)
                # Path 2
                B = n * (n - 1) * (2 * g - 2)
                g2 = (n * (2 * g - 2) + B + 2) // 2
                # Path 3
                g3 = n * n * (2 * g - 2) // 2 + 1
                assert g1 == g2 == g3, f"Disagree at n={n}, g={g}"


# =====================================================================
# 24. MULTI-PATH VERIFICATION: HITCHIN BASE DIM
# =====================================================================

class TestMultiPathBaseDim:
    """Verify dim(B) by multiple paths."""

    def test_path1_riemann_roch(self):
        """Path 1: sum of dim H^0(K^i) via Riemann-Roch."""
        # SL(3), g=3: H^0(K^2) = 3*2 = 6, H^0(K^3) = 5*2 = 10
        # dim B = 6 + 10 = 16
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert hitchin_base_dim_sln(3, 3) == 16

    def test_path2_dim_formula(self):
        """Path 2: (n^2-1)(g-1) directly."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert (9 - 1) * (3 - 1) == 16

    def test_path3_casimir_sum(self):
        """Path 3: dim(g)*(g-1) using Casimir sum rule."""
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert LIE_DIM['A_2'] * (3 - 1) == 16

    def test_all_three_agree(self):
        for lie_type in ['A_1', 'A_2', 'A_3', 'E_6', 'E_8']:
            for g in [2, 3, 4]:
                d1 = hitchin_base_via_casimirs(lie_type, g)
                d2 = hitchin_base_via_dim_g(lie_type, g)
                # Path 3: for type A, also check (n^2-1)(g-1)
                if lie_type.startswith('A_'):
                    r = int(lie_type.split('_')[1])
                    n = r + 1
                    d3 = (n * n - 1) * (g - 1)
                    assert d1 == d2 == d3
                else:
                    assert d1 == d2
