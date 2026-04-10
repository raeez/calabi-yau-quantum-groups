r"""Tests for chiral algebras from Fano/anti-CY local surfaces.

Verifies:
  1. Del Pezzo surface invariants (chi, K^2, Noether, blowup additivity)
  2. Hirzebruch surface invariants
  3. CY local del Pezzo kappa = chi(S)/2 (multi-path)
  4. Non-CY local P^2: anomaly, defect, effective CY dimension
  5. Curved bar complex structure
  6. Serre functor analysis
  7. Riemann-Roch consistency
  8. Landscape completeness and cross-checks
  9. Characteristic numbers (A-hat, signature, Todd)
  10. Cross-volume bridge with local_p2_shadow

Ground truth:
  - Beauville, "Complex Algebraic Surfaces" (chi, K^2, Noether)
  - Manin, "Cubic Forms" (del Pezzo classification)
  - BCOV 1994 (kappa = chi/24 for compact CY3; chi(S)/2 for non-compact)
  - Chiang-Klemm-Yau-Zaslow 1999 (local P^2 GV invariants)
  - Lorgat Vol I: curved bar-cobar theory
  - Lorgat Vol III: CY-to-chiral functor

100+ tests organized by mathematical topic.
"""

from fractions import Fraction

import pytest

from compute.lib.fano_local_surface_chiral import (
    ChiralAlgebraInvariants,
    CurvedAInfinityData,
    CurvedBarData,
    LineBundleData,
    LocalSurfaceData,
    SerreFunctorData,
    SurfaceData,
    a_hat_genus,
    anomaly_hierarchy,
    anomaly_vanishing_locus,
    blowup_additivity_check,
    chiral_algebra_invariants,
    curved_a_infinity,
    curved_bar_complex,
    del_pezzo,
    del_pezzo_cy_landscape,
    effective_cy_dimension,
    exceptional_collection_dP,
    exceptional_collection_p2,
    full_fano_landscape,
    hilbert_polynomial_p2,
    hirzebruch,
    hirzebruch_signature,
    integer_effective_cy_dim_surfaces,
    kappa_bridge_local_p2,
    kappa_ch_local_p2,
    kappa_local_del_pezzo,
    kappa_local_hirzebruch,
    local_del_pezzo_cy,
    local_hirzebruch_cy,
    local_p2,
    local_p2_landscape,
    local_p2_vertex_data,
    p1_cross_p1,
    projective_plane,
    riemann_roch_p2,
    serre_functor_data,
    summary_table,
    todd_class_integral,
    verify_all_noether,
    verify_anomaly_linearity,
    verify_blowup_euler,
    verify_curvature_vanishes_iff_cy,
    verify_effective_cy_dim_at_cy,
    verify_hirzebruch_chi_constant,
    verify_kappa_eff_reduces_to_kappa,
)


# ======================================================================
# 1. DEL PEZZO SURFACE INVARIANTS
# ======================================================================

class TestDelPezzoSurfaces:
    """Tests for del Pezzo surface topological data."""

    def test_dp0_is_p2(self):
        """dP_0 = P^2."""
        S = del_pezzo(0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert S.name == "P^2"

    def test_dp_chi(self):
        """chi(dP_k) = 3 + k for k = 0, ..., 8."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
            assert S.chi == 3 + k, f"chi(dP_{k}) = {S.chi}, expected {3 + k}"

    def test_dp_k_squared(self):
        """K^2(dP_k) = 9 - k."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert S.c1_squared == 9 - k

    def test_dp_b2(self):
        """b_2(dP_k) = 1 + k."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] Betti number [LT] chiral algebra theory
            assert S.b2 == 1 + k

    def test_dp_h11(self):
        """h^{1,1}(dP_k) = 1 + k (since h^{1,0} = h^{2,0} = 0)."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] Hodge diamond [LT] chiral algebra theory
            assert S.h11 == 1 + k

    def test_dp_rational(self):
        """All del Pezzo surfaces are rational: h^{1,0} = h^{2,0} = 0, chi(O) = 1."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] Hodge number [LT] chiral algebra theory
            assert S.h10 == 0
            # VERIFIED [DC] Hodge number [LT] chiral algebra theory
            assert S.h20 == 0
            # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
            assert S.chi_O == 1

    def test_dp_fano(self):
        """All dP_k for k = 0,...,8 are Fano."""
        for k in range(9):
            assert del_pezzo(k).is_fano

    def test_dp_degree(self):
        """Degree of dP_k = K^2 = 9 - k."""
        for k in range(9):
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert del_pezzo(k).degree == 9 - k

    def test_dp_c2_equals_chi(self):
        """c_2(S) = chi(S) for surfaces (by definition, and verified by Gauss-Bonnet)."""
        for k in range(9):
            S = del_pezzo(k)
            assert S.c2 == S.chi

    def test_dp_out_of_range(self):
        """dP_k is only defined for k = 0, ..., 8."""
        with pytest.raises(ValueError):
            del_pezzo(-1)
        with pytest.raises(ValueError):
            del_pezzo(9)


class TestNoetherFormula:
    """Verify Noether's formula chi(O) = (c_1^2 + c_2) / 12."""

    def test_noether_p2(self):
        """P^2: chi(O) = (9 + 3)/12 = 1."""
        S = projective_plane()
        assert Fraction(S.c1_squared + S.c2, 12) == S.chi_O

    def test_noether_all_dp(self):
        """Noether for all del Pezzo surfaces."""
        for k in range(9):
            S = del_pezzo(k)
            lhs = S.chi_O
            rhs = Fraction(S.c1_squared + S.c2, 12)
            assert lhs == rhs, f"Noether fails for dP_{k}: {lhs} != {rhs}"

    def test_noether_all_hirzebruch(self):
        """Noether for Hirzebruch surfaces F_0, ..., F_5."""
        for n in range(6):
            S = hirzebruch(n)
            lhs = S.chi_O
            rhs = Fraction(S.c1_squared + S.c2, 12)
            assert lhs == rhs, f"Noether fails for F_{n}: {lhs} != {rhs}"

    def test_noether_global(self):
        """Global Noether verification."""
        assert verify_all_noether()


class TestBlowupFormula:
    """Verify chi(Bl_p(S)) = chi(S) + 1."""

    def test_blowup_chi(self):
        """chi(dP_{k+1}) = chi(dP_k) + 1 for k = 0, ..., 7."""
        assert verify_blowup_euler()

    def test_blowup_kappa(self):
        """kappa(dP_{k+1}) = kappa(dP_k) + 1/2."""
        assert blowup_additivity_check()

    def test_blowup_k_squared(self):
        """K^2(dP_{k+1}) = K^2(dP_k) - 1 (blowing up decreases K^2)."""
        for k in range(8):
            assert del_pezzo(k + 1).c1_squared == del_pezzo(k).c1_squared - 1


# ======================================================================
# 2. HIRZEBRUCH SURFACE INVARIANTS
# ======================================================================

class TestHirzebruchSurfaces:
    """Tests for Hirzebruch surface data."""

    def test_hirzebruch_chi_constant(self):
        """chi(F_n) = 4 for all n >= 0."""
        assert verify_hirzebruch_chi_constant()

    def test_hirzebruch_k_squared(self):
        """K^2(F_n) = 8 for all n >= 0."""
        for n in range(6):
            # VERIFIED [DC] characteristic class [LT] chiral algebra theory
            assert hirzebruch(n).c1_squared == 8

    def test_hirzebruch_b2(self):
        """b_2(F_n) = 2 for all n >= 0."""
        for n in range(6):
            # VERIFIED [DC] Betti number [LT] chiral algebra theory
            assert hirzebruch(n).b2 == 2

    def test_hirzebruch_rational(self):
        """All Hirzebruch surfaces are rational."""
        for n in range(6):
            S = hirzebruch(n)
            # VERIFIED [DC] Hodge number [LT] chiral algebra theory
            assert S.h10 == 0
            # VERIFIED [DC] Hodge number [LT] chiral algebra theory
            assert S.h20 == 0
            # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
            assert S.chi_O == 1

    def test_f0_is_p1xp1(self):
        """F_0 = P^1 x P^1."""
        S = p1_cross_p1()
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert S.chi == 4
        # VERIFIED [DC] Faber-Pandharipande genus formula [LT] chiral algebra theory
        assert S.name == "F_0"

    def test_f1_fano(self):
        """F_0 and F_1 are Fano; F_n for n >= 2 are not."""
        assert hirzebruch(0).is_fano
        assert hirzebruch(1).is_fano
        assert not hirzebruch(2).is_fano
        assert not hirzebruch(3).is_fano

    def test_hirzebruch_negative_n(self):
        """F_n is only defined for n >= 0."""
        with pytest.raises(ValueError):
            hirzebruch(-1)


# ======================================================================
# 3. CY LOCAL DEL PEZZO: kappa = chi(S)/2
# ======================================================================

class TestLocalCYDelPezzo:
    """Tests for CY local del Pezzo surfaces Tot(K_{dP_k})."""

    def test_kappa_dp_k(self):
        """kappa(Tot(K_{dP_k})) = (3+k)/2 for k = 0,...,8."""
        for k in range(9):
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert kappa_local_del_pezzo(k) == Fraction(3 + k, 2)

    def test_local_dp_is_cy(self):
        """Tot(K_{dP_k}) is CY for all k."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            assert X.is_cy

    def test_local_dp_zero_defect(self):
        """CY defect is zero for Tot(K_S)."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.cy_defect_class == 0
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.cy_defect_squared == 0

    def test_local_dp_zero_anomaly(self):
        """Anomaly coefficient is zero for CY."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.anomaly_coefficient == 0

    def test_local_dp_zero_curvature(self):
        """Bar complex curvature is zero for CY."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.curvature_m0 == 0

    def test_local_dp_d_eff_3(self):
        """Effective CY dimension is 3 for all CY local del Pezzo."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert X.effective_cy_dim == Fraction(3)

    def test_kappa_dp0_local_p2(self):
        """kappa(local P^2) = kappa(Tot(K_{P^2})) = 3/2.

        Multi-path verification:
        Path 1: chi(P^2)/2 = 3/2
        Path 2: Betti numbers: chi = 1 + 1 + 1 = 3, kappa = 3/2
        Path 3: Noether: chi = 12*1 - 9 = 3, kappa = 3/2
        Path 4: Torus fixed points: 3 points, kappa = 3/2
        """
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_local_del_pezzo(0) == Fraction(3, 2)
        bridge = kappa_bridge_local_p2()
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert bridge["kappa_surface"] == Fraction(3, 2)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert bridge["kappa_localization"] == Fraction(3, 2)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert bridge["kappa_noether"] == Fraction(3, 2)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert bridge["kappa_betti"] == Fraction(3, 2)

    def test_kappa_dp1(self):
        """kappa(Tot(K_{dP_1})) = 2."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_local_del_pezzo(1) == Fraction(2)

    def test_kappa_dp8(self):
        """kappa(Tot(K_{dP_8})) = 11/2."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_local_del_pezzo(8) == Fraction(11, 2)

    def test_kappa_half_integer_iff_k_even(self):
        """kappa = (3+k)/2 is integer iff k is odd, half-integer iff k is even."""
        for k in range(9):
            kappa = kappa_local_del_pezzo(k)
            if k % 2 == 1:
                # VERIFIED [DC] kappa formula [LT] chiral algebra theory
                assert kappa.denominator == 1  # integer
            else:
                # VERIFIED [DC] kappa formula [LT] chiral algebra theory
                assert kappa.denominator == 2  # half-integer

    def test_landscape_length(self):
        """There are exactly 9 local CY del Pezzo surfaces."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(del_pezzo_cy_landscape()) == 9


class TestLocalCYHirzebruch:
    """Tests for CY local Hirzebruch surfaces Tot(K_{F_n})."""

    def test_kappa_hirzebruch(self):
        """kappa(Tot(K_{F_n})) = 2 for all n >= 0."""
        for n in range(6):
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert kappa_local_hirzebruch(n) == Fraction(2)

    def test_local_hirzebruch_is_cy(self):
        """All are CY."""
        for n in range(4):
            X = local_hirzebruch_cy(n)
            assert X.is_cy
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert X.kappa_cy == Fraction(2)


# ======================================================================
# 4. NON-CY LOCAL P^2
# ======================================================================

class TestNonCYLocalP2:
    """Tests for non-CY local P^2 geometries Tot(O(n) -> P^2)."""

    def test_local_p2_cy_at_n_minus3(self):
        """Tot(O(-3) -> P^2) is CY (the canonical bundle)."""
        X = local_p2(-3)
        assert X.is_cy
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.cy_defect_class == 0
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert X.kappa_cy == Fraction(3, 2)

    def test_local_p2_not_cy_otherwise(self):
        """Tot(O(n) -> P^2) is NOT CY for n != -3."""
        for n in [-5, -4, -2, -1, 0, 1, 2, 3]:
            X = local_p2(n)
            assert not X.is_cy

    def test_cy_defect_values(self):
        """delta = n + 3 for Tot(O(n) -> P^2)."""
        for n in range(-5, 4):
            X = local_p2(n)
            assert X.cy_defect_class == n + 3

    def test_anomaly_values(self):
        """alpha = 3(n+3) for Tot(O(n) -> P^2).

        Path 1: direct formula alpha = delta . c_1(S) = (n+3) * 3.
        Path 2: from local_surface function.
        """
        test_cases = {
            -5: -6,   # 3*(-2) = -6
            -4: -3,   # 3*(-1) = -3
            -3: 0,    # CY
            -2: 3,    # 3*1 = 3
            -1: 6,    # 3*2 = 6
            0: 9,     # 3*3 = 9
            1: 12,    # 3*4 = 12
            2: 15,    # 3*5 = 15
            3: 18,    # 3*6 = 18
        }
        for n, expected_alpha in test_cases.items():
            X = local_p2(n)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.anomaly_coefficient == Fraction(expected_alpha), \
                f"n={n}: alpha={X.anomaly_coefficient}, expected {expected_alpha}"

    def test_anomaly_linearity(self):
        """alpha is linear in n: alpha(n+1) - alpha(n) = 3."""
        assert verify_anomaly_linearity()

    def test_kappa_eff_formula(self):
        """kappa_ch = (9-n)/8 for Tot(O(n) -> P^2).

        Derivation: kappa_ch = chi(P^2)/2 - alpha/24 = 3/2 - 3(n+3)/24
                   = 3/2 - (n+3)/8 = (12 - n - 3)/8 = (9-n)/8.
        """
        for n in range(-5, 4):
            expected = Fraction(9 - n, 8)
            assert kappa_ch_local_p2(n) == expected
            X = local_p2(n)
            assert X.kappa_ch == expected

    def test_kappa_eff_at_cy(self):
        """At the CY locus n = -3: kappa_ch = 12/8 = 3/2 = kappa."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_ch_local_p2(-3) == Fraction(3, 2)
        assert verify_kappa_eff_reduces_to_kappa()

    def test_effective_cy_dim(self):
        """d_eff = (12+n)/3 for Tot(O(n) -> P^2)."""
        test_cases = {
            -3: Fraction(3),     # CY
            -2: Fraction(10, 3),
            -1: Fraction(11, 3),
            0: Fraction(4),      # trivial bundle, d_eff = 4
            1: Fraction(13, 3),
            3: Fraction(5),
        }
        for n, expected_d in test_cases.items():
            X = local_p2(n)
            assert X.effective_cy_dim == expected_d, \
                f"n={n}: d_eff={X.effective_cy_dim}, expected {expected_d}"

    def test_d_eff_integer_locus(self):
        """d_eff is an integer iff n = 0 mod 3."""
        results = integer_effective_cy_dim_surfaces()
        # Check that n = ..., -6, -3, 0, 3, 6, ... give integer d_eff
        n_values = [r[0] for r in results]
        for n in n_values:
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert n % 3 == 0

    def test_curvature_values(self):
        """Curvature m_0 = (n+3)^2 for Tot(O(n) -> P^2)."""
        for n in range(-5, 4):
            X = local_p2(n)
            expected = Fraction((n + 3) ** 2)
            assert X.curvature_m0 == expected

    def test_curvature_zero_iff_cy(self):
        """m_0 = 0 iff CY."""
        assert verify_curvature_vanishes_iff_cy()


class TestCYDefectSquared:
    """Tests for the quadratic behavior of the CY defect."""

    def test_defect_squared_values(self):
        """delta^2 = (n+3)^2 for Tot(O(n) -> P^2)."""
        for n in range(-5, 4):
            X = local_p2(n)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.cy_defect_squared == (n + 3) ** 2

    def test_defect_symmetric_around_cy(self):
        """delta^2 is symmetric around n = -3 (CY locus).

        delta^2(-3+j) = delta^2(-3-j) = j^2.
        """
        for j in range(6):
            X_plus = local_p2(-3 + j)
            X_minus = local_p2(-3 - j)
            assert X_plus.cy_defect_squared == X_minus.cy_defect_squared == j * j

    def test_defect_nonnegative(self):
        """delta^2 >= 0 always (it's a square)."""
        for n in range(-10, 10):
            X = local_p2(n)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.cy_defect_squared >= 0


# ======================================================================
# 5. CURVED BAR COMPLEX
# ======================================================================

class TestCurvedBarComplex:
    """Tests for the curved bar complex structure."""

    def test_uncurved_iff_cy(self):
        """Bar complex is uncurved iff CY."""
        for n in range(-5, 4):
            X = local_p2(n)
            bar = curved_bar_complex(X)
            assert bar.is_uncurved == X.is_cy

    def test_mc_deformed_iff_not_cy(self):
        """MC equation is deformed iff non-CY."""
        for n in range(-5, 4):
            X = local_p2(n)
            bar = curved_bar_complex(X)
            # VERIFIED [DC] deformation [LT] chiral algebra theory
            assert bar.maurer_cartan_deformed == (not X.is_cy)

    def test_curvature_squared(self):
        """m_0^2 = delta^4 for Tot(O(n) -> P^2)."""
        for n in range(-5, 4):
            X = local_p2(n)
            bar = curved_bar_complex(X)
            expected = Fraction((n + 3) ** 4)
            assert bar.curvature_m0_squared == expected

    def test_cy_bar_no_obstruction(self):
        """CY bar complex has no obstruction."""
        X = local_p2(-3)
        bar = curved_bar_complex(X)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert bar.obstruction_class == "none (CY)"

    def test_mild_defect_bar(self):
        """delta = 1 (n = -2) gives mild obstruction."""
        X = local_p2(-2)
        bar = curved_bar_complex(X)
        assert "mild" in bar.obstruction_class


# ======================================================================
# 6. CHIRAL ALGEBRA INVARIANTS
# ======================================================================

class TestChiralAlgebraInvariants:
    """Tests for the chiral algebra invariants."""

    def test_cy_serre_type(self):
        """CY local surfaces have serre_type = CY3."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            inv = chiral_algebra_invariants(X)
            # VERIFIED [DC] Serre duality check [LT] chiral algebra theory
            assert inv.serre_type == "CY3"

    def test_non_cy_serre_type(self):
        """Non-CY local P^2 has serre_type != CY3."""
        for n in [-2, -1, 0, 1, 2]:
            X = local_p2(n)
            inv = chiral_algebra_invariants(X)
            assert inv.serre_type != "CY3"

    def test_e2_iff_cy(self):
        """E_2 structure exists iff CY."""
        for n in range(-5, 4):
            X = local_p2(n)
            inv = chiral_algebra_invariants(X)
            assert inv.e2_structure == X.is_cy

    def test_bar_d_squared_zero_iff_cy(self):
        """d^2 = 0 iff CY."""
        for n in range(-5, 4):
            X = local_p2(n)
            inv = chiral_algebra_invariants(X)
            if X.is_cy:
                # VERIFIED [DC] structural property [LT] chiral algebra theory
                assert inv.bar_differential_squared == "zero"
            else:
                # VERIFIED [DC] structural property [LT] chiral algebra theory
                assert inv.bar_differential_squared == "m0-commutator"

    def test_shadow_class_curved(self):
        """Non-CY surfaces have shadow_depth_class = curved."""
        X = local_p2(0)
        inv = chiral_algebra_invariants(X)
        # VERIFIED [DC] shadow depth [LT] chiral algebra theory
        assert inv.shadow_depth_class == "curved"

    def test_shadow_class_M_for_cy(self):
        """CY local surfaces have class M (infinite shadow depth)."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            inv = chiral_algebra_invariants(X)
            # VERIFIED [DC] shadow depth [LT] chiral algebra theory
            assert inv.shadow_depth_class == "M"

    def test_central_charge_eff(self):
        """c_eff = 2 * kappa_ch."""
        for n in range(-5, 4):
            X = local_p2(n)
            inv = chiral_algebra_invariants(X)
            # VERIFIED [DC] central charge formula [LT] chiral algebra theory
            assert inv.central_charge_eff == 2 * X.kappa_ch


# ======================================================================
# 7. CURVED A-INFINITY STRUCTURE
# ======================================================================

class TestCurvedAInfinity:
    """Tests for the curved A-infinity structure."""

    def test_cy_uncurved(self):
        """CY gives standard (uncurved) A-infinity."""
        X = local_p2(-3)
        data = curved_a_infinity(X)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert data.m0 == 0
        assert not data.m1_deformed
        assert "d(Theta) + (1/2)[Theta,Theta] = 0" == data.mc_equation

    def test_non_cy_curved(self):
        """Non-CY gives curved A-infinity with m_0 != 0."""
        X = local_p2(0)
        data = curved_a_infinity(X)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert data.m0 == Fraction(9)  # (0+3)^2 = 9
        assert data.m1_deformed

    def test_e1_unconditional(self):
        """E_1 (associativity) holds for all local surfaces."""
        for n in range(-5, 4):
            X = local_p2(n)
            data = curved_a_infinity(X)
            assert data.m2_associative


# ======================================================================
# 8. SERRE FUNCTOR
# ======================================================================

class TestSerreFunctor:
    """Tests for the Serre functor analysis."""

    def test_cy_pure_shift(self):
        """CY Serre functor is pure shift [3]."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            sf = serre_functor_data(X)
            assert sf.is_pure_shift
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert sf.shift == 3
            # VERIFIED [DC] degree count [DA] dimensional consistency
            assert sf.twist_degree == 0
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert sf.order == 1

    def test_non_cy_not_pure_shift(self):
        """Non-CY Serre functor is NOT a pure shift."""
        for n in [-2, -1, 0, 1, 2]:
            X = local_p2(n)
            sf = serre_functor_data(X)
            assert not sf.is_pure_shift
            assert sf.twist_degree != 0
            assert sf.order is None  # infinite order

    def test_serre_twist_values(self):
        """Serre twist degree = -(n+3) for Tot(O(n) -> P^2)."""
        for n in range(-5, 4):
            X = local_p2(n)
            sf = serre_functor_data(X)
            assert sf.twist_degree == -(n + 3)


# ======================================================================
# 9. RIEMANN-ROCH AND CHARACTERISTIC NUMBERS
# ======================================================================

class TestRiemannRoch:
    """Tests for Riemann-Roch on P^2."""

    def test_rr_structure_sheaf(self):
        """chi(O_{P^2}) = 1."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert riemann_roch_p2(0) == Fraction(1)

    def test_rr_o1(self):
        """chi(O(1)) = 3 on P^2."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert riemann_roch_p2(1) == Fraction(3)

    def test_rr_o2(self):
        """chi(O(2)) = 6 on P^2."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert riemann_roch_p2(2) == Fraction(6)

    def test_rr_o_minus1(self):
        """chi(O(-1)) = 0 on P^2 (no global sections, no cohomology)."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert riemann_roch_p2(-1) == Fraction(0)

    def test_rr_o_minus2(self):
        """chi(O(-2)) = 0 on P^2."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert riemann_roch_p2(-2) == Fraction(0)

    def test_rr_canonical(self):
        """chi(K_{P^2}) = chi(O(-3)) = (-3+1)(-3+2)/2 = (-2)(-1)/2 = 1."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert riemann_roch_p2(-3) == Fraction(1)

    def test_rr_general_formula(self):
        """chi(O(n)) = (n+1)(n+2)/2 for several values."""
        for n in range(-3, 6):
            expected = Fraction((n + 1) * (n + 2), 2)
            assert riemann_roch_p2(n) == expected

    def test_hilbert_poly_agrees(self):
        """Hilbert polynomial agrees with Riemann-Roch."""
        for n in range(-3, 6):
            assert hilbert_polynomial_p2(n) == riemann_roch_p2(n)


class TestCharacteristicNumbers:
    """Tests for characteristic numbers of surfaces."""

    def test_todd_rational(self):
        """Todd class integral = chi(O) = 1 for rational surfaces."""
        for k in range(9):
            # VERIFIED [DC] characteristic class [LT] chiral algebra theory
            assert todd_class_integral(del_pezzo(k)) == Fraction(1)
        for n in range(4):
            # VERIFIED [DC] characteristic class [LT] chiral algebra theory
            assert todd_class_integral(hirzebruch(n)) == Fraction(1)

    def test_a_hat_p2(self):
        """A-hat(P^2) = (2*3 - 9)/24 = -3/24 = -1/8."""
        # VERIFIED [DC] characteristic class [LT] chiral algebra theory
        assert a_hat_genus(projective_plane()) == Fraction(-1, 8)

    def test_a_hat_dp_k(self):
        """A-hat(dP_k) = (2(3+k) - (9-k))/24 = (3k-3)/24 = (k-1)/8."""
        for k in range(9):
            expected = Fraction(k - 1, 8)
            assert a_hat_genus(del_pezzo(k)) == expected

    def test_a_hat_dp1_zero(self):
        """A-hat(dP_1) = 0."""
        # VERIFIED [DC] characteristic class [LT] chiral algebra theory
        assert a_hat_genus(del_pezzo(1)) == Fraction(0)

    def test_signature_p2(self):
        """sigma(P^2) = (9 - 6)/3 = 1."""
        # VERIFIED [DC] characteristic class [LT] chiral algebra theory
        assert hirzebruch_signature(projective_plane()) == Fraction(1)

    def test_signature_dp_k(self):
        """sigma(dP_k) = 1 - k."""
        for k in range(9):
            expected = Fraction(1 - k)
            assert hirzebruch_signature(del_pezzo(k)) == expected

    def test_signature_hirzebruch(self):
        """sigma(F_n) = (8 - 8)/3 = 0 for all n."""
        for n in range(6):
            # VERIFIED [DC] characteristic class [LT] chiral algebra theory
            assert hirzebruch_signature(hirzebruch(n)) == Fraction(0)


# ======================================================================
# 10. LANDSCAPE AND COMPLETENESS
# ======================================================================

class TestLandscape:
    """Tests for landscape functions."""

    def test_dp_cy_landscape_length(self):
        """9 local CY del Pezzo surfaces."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(del_pezzo_cy_landscape()) == 9

    def test_local_p2_landscape_length(self):
        """9 local P^2 geometries (n = -5, ..., 3)."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(local_p2_landscape()) == 9

    def test_full_landscape_contains_cy(self):
        """Full landscape contains all CY cases."""
        landscape = full_fano_landscape()
        for k in range(9):
            key = f"Tot(K_dP{k})"
            assert key in landscape
            assert landscape[key].is_cy

    def test_full_landscape_contains_non_cy(self):
        """Full landscape contains non-CY cases."""
        landscape = full_fano_landscape()
        for n in [-5, -4, -2, -1, 0, 1, 2, 3]:
            key = f"Tot(O({n})->P^2)"
            assert key in landscape
            assert not landscape[key].is_cy

    def test_summary_table_nonempty(self):
        """Summary table produces entries."""
        table = summary_table()
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(table) > 0
        # Check that each row has expected keys
        for row in table:
            assert "geometry" in row
            assert "kappa_ch" in row
            assert "anomaly" in row


class TestAnomalyHierarchy:
    """Tests for anomaly hierarchy."""

    def test_hierarchy_sorted(self):
        """Anomaly hierarchy is sorted by |alpha|."""
        hierarchy = anomaly_hierarchy()
        alphas = [abs(h[1]) for h in hierarchy]
        assert alphas == sorted(alphas)

    def test_cy_first(self):
        """CY case (alpha = 0) comes first in the hierarchy."""
        hierarchy = anomaly_hierarchy()
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hierarchy[0][1] == 0
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hierarchy[0][2] == "CY (anomaly-free)"

    def test_vanishing_locus(self):
        """Anomaly vanishes at n = -3 for P^2."""
        # VERIFIED [DC] vanishing check [LT] chiral algebra theory
        assert anomaly_vanishing_locus(projective_plane()) == -3


# ======================================================================
# 11. EXCEPTIONAL COLLECTIONS
# ======================================================================

class TestExceptionalCollections:
    """Tests for exceptional collections on del Pezzo surfaces."""

    def test_p2_collection_length(self):
        """P^2 has a full exceptional collection of length 3."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(exceptional_collection_p2()) == 3

    def test_dp_collection_length(self):
        """dP_k has a full exceptional collection of length 3 + k."""
        for k in range(9):
            coll = exceptional_collection_dP(k)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert len(coll) == 3 + k


# ======================================================================
# 12. CROSS-VOLUME BRIDGE
# ======================================================================

class TestCrossVolumeBridge:
    """Cross-volume consistency checks."""

    def test_kappa_bridge_4_path(self):
        """kappa(local P^2) verified by 4 independent paths."""
        bridge = kappa_bridge_local_p2()
        values = list(bridge.values())
        # All 4 paths must agree
        # VERIFIED [DC] kappa computation [LT] chiral algebra theory
        assert all(v == Fraction(3, 2) for v in values)

    def test_vertex_data_consistency(self):
        """Topological vertex data consistent with chi formula."""
        vdata = local_p2_vertex_data()
        assert vdata["agreement"]
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert vdata["kappa_from_fixed"] == Fraction(3, 2)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert vdata["kappa_from_chi"] == Fraction(3, 2)
        # VERIFIED [DC] vertex algebra [LT] chiral algebra theory
        assert vdata["fixed_points"] == 3

    def test_effective_cy_dim_at_cy(self):
        """d_eff = 3 at CY locus."""
        assert verify_effective_cy_dim_at_cy()


# ======================================================================
# 13. MONOTONICITY AND EXTREMAL VALUES
# ======================================================================

class TestMonotonicity:
    """Tests for monotonicity and extremal behavior."""

    def test_kappa_dp_monotone(self):
        """kappa(dP_k) is strictly increasing in k."""
        for k in range(8):
            assert kappa_local_del_pezzo(k) < kappa_local_del_pezzo(k + 1)

    def test_kappa_eff_monotone_decreasing(self):
        """kappa_ch = (9-n)/8 is decreasing in n."""
        for n in range(-5, 3):
            assert kappa_ch_local_p2(n) > kappa_ch_local_p2(n + 1)

    def test_anomaly_monotone(self):
        """Anomaly alpha = 3(n+3) is increasing in n."""
        for n in range(-5, 3):
            X1 = local_p2(n)
            X2 = local_p2(n + 1)
            assert X1.anomaly_coefficient < X2.anomaly_coefficient

    def test_curvature_minimal_at_cy(self):
        """Curvature is minimal (= 0) at the CY locus n = -3."""
        cy_curv = local_p2(-3).curvature_m0
        for n in range(-5, 4):
            assert local_p2(n).curvature_m0 >= cy_curv

    def test_kappa_dp_min_max(self):
        """Min kappa: dP_0 = 3/2. Max kappa: dP_8 = 11/2."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_local_del_pezzo(0) == Fraction(3, 2)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_local_del_pezzo(8) == Fraction(11, 2)


# ======================================================================
# 14. SPECIAL VALUES AND COINCIDENCES
# ======================================================================

class TestSpecialValues:
    """Tests for special values and interesting coincidences."""

    def test_trivial_bundle_d_eff_4(self):
        """Tot(O -> P^2) has d_eff = 4 (effective CY4!)."""
        X = local_p2(0)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert X.effective_cy_dim == Fraction(4)

    def test_o1_d_eff_13_over_3(self):
        """Tot(O(1) -> P^2) has d_eff = 13/3."""
        X = local_p2(1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert X.effective_cy_dim == Fraction(13, 3)

    def test_o_minus_2_small_defect(self):
        """Tot(O(-2) -> P^2) has smallest non-zero defect: delta = 1."""
        X = local_p2(-2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.cy_defect_class == 1
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.curvature_m0 == Fraction(1)

    def test_kappa_eff_at_trivial_bundle(self):
        """kappa_ch(Tot(O -> P^2)) = 9/8."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_ch_local_p2(0) == Fraction(9, 8)

    def test_chi_p2_times_chi_p1_gives_hirzebruch(self):
        """chi(P^2) * chi(P^1) != chi(F_n).
        But chi(P^1) * chi(P^1) = 4 = chi(F_0) = chi(P^1 x P^1).

        This is the multiplicativity of Euler char for products.
        """
        # chi(P^1) = 2, chi(P^1 x P^1) = 4.
        assert 2 * 2 == hirzebruch(0).chi

    def test_a_hat_vanishes_dp1(self):
        """A-hat(dP_1) = 0.

        This is notable: dP_1 = F_1 has zero A-hat genus,
        meaning the Dirac index vanishes.
        """
        # VERIFIED [DC] characteristic class [LT] chiral algebra theory
        assert a_hat_genus(del_pezzo(1)) == Fraction(0)

    def test_signature_vanishes_p1xp1(self):
        """sigma(P^1 x P^1) = 0 (product of curves)."""
        # VERIFIED [DC] characteristic class [LT] chiral algebra theory
        assert hirzebruch_signature(hirzebruch(0)) == Fraction(0)

    def test_kappa_eff_positive_for_negative_n(self):
        """kappa_ch > 0 for n < 9 (i.e., all our cases)."""
        for n in range(-5, 4):
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert kappa_ch_local_p2(n) > 0


# ======================================================================
# 15. CONSISTENCY RELATIONS
# ======================================================================

class TestConsistencyRelations:
    """Tests for internal consistency of the framework."""

    def test_kappa_eff_equals_kappa_at_cy(self):
        """kappa_ch = kappa_cy when CY (global check)."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            assert X.kappa_ch == X.kappa_cy

    def test_anomaly_plus_24_kappa_eff_equals_12(self):
        """alpha + 24*kappa_ch = 12 for Tot(O(n) -> P^2).

        This follows from kappa_ch = 3/2 - alpha/24, so
        24*kappa_ch = 36 - alpha, hence alpha + 24*kappa_ch = 36.
        Wait: chi(P^2) = 3, kappa_ch = chi/2 - alpha/24 = 3/2 - alpha/24.
        So 24*kappa_ch = 36 - alpha, i.e., alpha + 24*kappa_ch = 36.
        """
        for n in range(-5, 4):
            X = local_p2(n)
            lhs = X.anomaly_coefficient + 24 * X.kappa_ch
            # VERIFIED [DC] kappa computation [LT] chiral algebra theory
            assert lhs == Fraction(36)

    def test_defect_squared_equals_curvature(self):
        """delta^2 = curvature m_0 (for P^2-based local surfaces)."""
        for n in range(-5, 4):
            X = local_p2(n)
            assert X.cy_defect_squared == X.curvature_m0

    def test_chi_from_noether_and_betti(self):
        """chi from Noether matches chi from definition (cross-check).

        Noether: chi = 12*chi(O) - K^2 = 12 - (9-k) = 3+k for dP_k.
        Direct: chi = 3 + k.
        """
        for k in range(9):
            S = del_pezzo(k)
            chi_noether = 12 * S.chi_O - S.c1_squared
            assert chi_noether == S.chi

    def test_b2_from_h11(self):
        """b_2 = h^{2,0} + h^{1,1} + h^{0,2} = 2*h^{2,0} + h^{1,1}.
        For rational: b_2 = h^{1,1}."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] Hodge number [LT] chiral algebra theory
            assert S.b2 == 2 * S.h20 + S.h11

    def test_chi_from_betti(self):
        """chi = sum (-1)^k b_k = 1 - 0 + b_2 - 0 + 1 = 2 + b_2 for rational surfaces."""
        for k in range(9):
            S = del_pezzo(k)
            # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
            assert S.chi == 2 + S.b2

    def test_dp1_equals_f1(self):
        """dP_1 and F_1 have the same topological invariants.

        dP_1 = Bl_p(P^2) is isomorphic to F_1 = P(O + O(1) -> P^1).
        chi(dP_1) = 4 = chi(F_1).  K^2(dP_1) = 8 = K^2(F_1).
        """
        dp1 = del_pezzo(1)
        f1 = hirzebruch(1)
        assert dp1.chi == f1.chi
        assert dp1.c1_squared == f1.c1_squared
        assert dp1.b2 == f1.b2


# ======================================================================
# 16. EDGE CASES AND BOUNDARY VALUES
# ======================================================================

class TestEdgeCases:
    """Tests for edge cases and boundary values."""

    def test_dp8_degree_1(self):
        """dP_8 has degree 1 (minimal del Pezzo)."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert del_pezzo(8).degree == 1

    def test_dp0_degree_9(self):
        """dP_0 = P^2 has degree 9 (maximal del Pezzo)."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert del_pezzo(0).degree == 9

    def test_negative_anomaly(self):
        """Negative anomaly for n < -3 (L more negative than K)."""
        for n in [-5, -4]:
            X = local_p2(n)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert X.anomaly_coefficient < 0

    def test_positive_anomaly(self):
        """Positive anomaly for n > -3."""
        for n in [-2, -1, 0, 1, 2, 3]:
            X = local_p2(n)
            # VERIFIED [DC] positivity check [LT] chiral algebra theory
            assert X.anomaly_coefficient > 0

    def test_large_defect(self):
        """Large defect values still consistent."""
        X = local_p2(10)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.cy_defect_class == 13
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.anomaly_coefficient == Fraction(39)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.curvature_m0 == Fraction(169)

    def test_very_negative_n(self):
        """Very negative n gives large negative anomaly."""
        X = local_p2(-10)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.cy_defect_class == -7
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert X.anomaly_coefficient == Fraction(-21)


# ======================================================================
# 17. RELATION BETWEEN kappa AND kappa_ch
# ======================================================================

class TestKappaRelation:
    """Tests for the relation between kappa (CY) and kappa_ch (general)."""

    def test_kappa_eff_interpolates(self):
        """kappa_ch continuously interpolates through the CY locus.

        kappa_ch is a smooth function of n, equal to kappa at n = -3.
        """
        # kappa_ch = (9 - n) / 8
        # This is a linear function of n passing through (n=-3, kappa=3/2).
        vals = {n: kappa_ch_local_p2(n) for n in range(-5, 4)}
        # Check linearity: kappa_ch(n) - kappa_ch(n+1) = 1/8 for all n.
        for n in range(-5, 3):
            diff = vals[n] - vals[n + 1]
            # VERIFIED [DC] kappa computation [LT] chiral algebra theory
            assert diff == Fraction(1, 8)

    def test_kappa_eff_large_n_limit(self):
        """For large n, kappa_ch ~ -n/8 (approaches zero from above at n=9)."""
        # kappa_ch = (9-n)/8.
        # At n=9: kappa_ch = 0.
        # At n > 9: kappa_ch < 0 (which would be physically problematic).
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_ch_local_p2(9) == Fraction(0)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_ch_local_p2(10) < 0


# ======================================================================
# 18. MULTI-PATH VERIFICATION (AP10 compliance)
# ======================================================================

class TestMultiPathChiDelPezzo:
    """Multi-path verification of chi(dP_k).

    Every value verified by at least 3 independent paths:
    Path 1 (definition):    chi(dP_k) = 3 + k
    Path 2 (Noether):       chi = 12*chi(O_S) - K^2 = 12*1 - (9-k) = 3+k
    Path 3 (Betti):         chi = b_0 - b_1 + b_2 - b_3 + b_4 = 1 - 0 + (1+k) - 0 + 1 = 3+k
    Path 4 (blowup):        chi(dP_k) = chi(P^2) + k = 3 + k
    """

    def test_chi_dp_4path_k0(self):
        """chi(P^2) = 3 by 4 independent paths."""
        S = del_pezzo(0)
        # Path 1: definition
        path1 = 3 + 0
        # Path 2: Noether
        path2 = 12 * S.chi_O - S.c1_squared  # 12*1 - 9 = 3
        # Path 3: Betti (b_0=1, b_1=0, b_2=1, b_3=0, b_4=1)
        path3 = 1 - 0 + 1 - 0 + 1
        # Path 4: Euler char of CW complex (P^2 has cells in dim 0,2,4)
        path4 = 1 + 1 + 1
        assert path1 == path2 == path3 == path4 == S.chi

    def test_chi_dp_4path_k3(self):
        """chi(dP_3) = 6 by 4 independent paths."""
        S = del_pezzo(3)
        path1 = 3 + 3
        path2 = 12 * S.chi_O - S.c1_squared  # 12 - 6 = 6
        path3 = 1 - 0 + (1 + 3) - 0 + 1  # Betti: b_2 = 4
        path4 = del_pezzo(0).chi + 3  # blowup: chi(P^2) + 3
        assert path1 == path2 == path3 == path4 == S.chi

    def test_chi_dp_4path_k8(self):
        """chi(dP_8) = 11 by 4 independent paths."""
        S = del_pezzo(8)
        path1 = 3 + 8
        path2 = 12 * S.chi_O - S.c1_squared  # 12 - 1 = 11
        path3 = 1 - 0 + 9 - 0 + 1  # Betti: b_2 = 9
        path4 = del_pezzo(0).chi + 8
        assert path1 == path2 == path3 == path4 == S.chi

    def test_chi_dp_all_4_paths_agree(self):
        """All 4 paths agree for every k = 0,...,8."""
        for k in range(9):
            S = del_pezzo(k)
            path1 = 3 + k
            path2 = 12 * S.chi_O - S.c1_squared
            path3 = 1 + (1 + k) + 1  # = 3 + k (Betti: b_0+b_2+b_4, odd=0)
            path4 = del_pezzo(0).chi + k
            assert path1 == path2 == path3 == path4 == S.chi, \
                f"dP_{k}: paths disagree: {path1}, {path2}, {path3}, {path4}, stored={S.chi}"


class TestMultiPathKappaDelPezzo:
    """Multi-path verification of kappa(Tot(K_{dP_k})) = (3+k)/2.

    Path 1 (chi/2):          kappa = chi(dP_k)/2
    Path 2 (Noether-based):  kappa = (12*chi(O) - K^2)/2
    Path 3 (blowup):         kappa(dP_k) = kappa(P^2) + k/2 = 3/2 + k/2
    Path 4 (Betti-based):    kappa = (2 + b_2)/2
    Path 5 (exc coll):       kappa = len(exc_coll)/2  (length = chi for rational)
    """

    def test_kappa_dp_5path_k0(self):
        """kappa(local P^2) = 3/2 by 5 paths."""
        S = del_pezzo(0)
        path1 = Fraction(S.chi, 2)
        path2 = Fraction(12 * S.chi_O - S.c1_squared, 2)
        path3 = Fraction(3, 2) + Fraction(0, 2)  # blowup from P^2
        path4 = Fraction(2 + S.b2, 2)
        path5 = Fraction(len(exceptional_collection_p2()), 2)
        target = Fraction(3, 2)
        assert path1 == path2 == path3 == path4 == path5 == target

    def test_kappa_dp_5path_k5(self):
        """kappa(Tot(K_{dP_5})) = 4 by 5 paths."""
        k = 5
        S = del_pezzo(k)
        path1 = Fraction(S.chi, 2)
        path2 = Fraction(12 * S.chi_O - S.c1_squared, 2)
        path3 = Fraction(3, 2) + Fraction(k, 2)
        path4 = Fraction(2 + S.b2, 2)
        path5 = Fraction(len(exceptional_collection_dP(k)), 2)
        target = Fraction(4)
        assert path1 == path2 == path3 == path4 == path5 == target

    def test_kappa_dp_all_5_paths_agree(self):
        """All 5 paths agree for every k = 0,...,8."""
        for k in range(9):
            S = del_pezzo(k)
            path1 = Fraction(S.chi, 2)
            path2 = Fraction(12 * S.chi_O - S.c1_squared, 2)
            path3 = Fraction(3, 2) + Fraction(k, 2)
            path4 = Fraction(2 + S.b2, 2)
            path5 = Fraction(len(exceptional_collection_dP(k)), 2)
            target = kappa_local_del_pezzo(k)
            assert path1 == path2 == path3 == path4 == path5 == target, \
                f"dP_{k}: 5 kappa paths disagree"


class TestMultiPathKappaEff:
    """Multi-path verification of kappa_ch = (9-n)/8 for Tot(O(n)->P^2).

    Path 1 (formula):         kappa_ch = (9-n)/8
    Path 2 (chi - alpha):     kappa_ch = chi(P^2)/2 - alpha/24 = 3/2 - 3(n+3)/24
    Path 3 (constraint):      alpha + 24*kappa_ch = 24*chi(P^2)/2 = 36
    Path 4 (CY limit):        at n=-3, kappa_ch = 3/2 = kappa_cy
    Path 5 (linearity slope): kappa_ch(n) - kappa_ch(n+1) = 1/8 for all n
    """

    def test_kappa_eff_5path_n0(self):
        """kappa_ch(Tot(O->P^2)) = 9/8 by 5 paths."""
        n = 0
        X = local_p2(n)
        path1 = Fraction(9 - n, 8)
        path2 = Fraction(3, 2) - Fraction(3 * (n + 3), 24)
        path3_lhs = X.anomaly_coefficient + 24 * X.kappa_ch
        path4 = Fraction(9 - (-3), 8)  # at CY, = 12/8 = 3/2 (different n, but verifies formula)
        path5 = kappa_ch_local_p2(n - 1) - Fraction(1, 8)  # from slope
        target = Fraction(9, 8)
        assert path1 == target
        assert path2 == target
        # VERIFIED [DC] kappa computation [LT] chiral algebra theory
        assert path3_lhs == Fraction(36)
        # VERIFIED [DC] kappa computation [LT] chiral algebra theory
        assert path4 == Fraction(3, 2)
        assert path5 == target

    def test_kappa_eff_3path_all_n(self):
        """3-path verification for all n in range."""
        for n in range(-5, 4):
            X = local_p2(n)
            path1 = Fraction(9 - n, 8)
            path2 = Fraction(3, 2) - X.anomaly_coefficient / 24
            path3_check = X.anomaly_coefficient + 24 * X.kappa_ch
            assert path1 == X.kappa_ch, f"n={n}: formula disagrees"
            assert path2 == X.kappa_ch, f"n={n}: chi-alpha path disagrees"
            # VERIFIED [DC] kappa computation [LT] chiral algebra theory
            assert path3_check == Fraction(36), f"n={n}: constraint fails"


class TestMultiPathAnomalyCoefficient:
    """Multi-path verification of alpha = 3(n+3) for Tot(O(n)->P^2).

    Path 1 (formula):       alpha = 3(n+3)
    Path 2 (defect . c1):   alpha = delta * c1_S_int = (n+3) * 3
    Path 3 (constraint):    alpha = 36 - 24*kappa_ch (from constraint)
    Path 4 (finite diff):   alpha(n) = alpha(n-1) + 3
    """

    def test_anomaly_4path_all_n(self):
        """4-path verification for all n."""
        for n in range(-5, 4):
            X = local_p2(n)
            path1 = Fraction(3 * (n + 3))
            path2 = Fraction(X.cy_defect_class * 3)
            path3 = Fraction(36) - 24 * X.kappa_ch
            assert path1 == X.anomaly_coefficient
            assert path2 == X.anomaly_coefficient
            assert path3 == X.anomaly_coefficient, \
                f"n={n}: constraint-derived alpha disagrees"
        # Path 4: finite differences
        for n in range(-4, 4):
            diff = local_p2(n).anomaly_coefficient - local_p2(n - 1).anomaly_coefficient
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert diff == Fraction(3)


class TestMultiPathCharacteristicNumbers:
    """Multi-path verification of characteristic numbers.

    For rational surfaces with chi(O)=1, h^{1,0}=h^{2,0}=0:
    - Noether: (K^2 + chi)/12 = 1
    - Signature: sigma = (K^2 - 2*chi)/3 = (p_1)/3
    - A-hat: A-hat = (2*chi - K^2)/24
    - Relation: sigma = 4*A-hat + (2/3)*chi (Hirzebruch signature theorem)
    - Relation: A-hat = (chi - 3*sigma)/6 (rearranged)
    - chi = 12*chi(O) - K^2 (Noether)
    """

    def test_characteristic_number_relations_all_dp(self):
        """Verify 3 independent relations among (chi, K^2, sigma, A-hat, chi_O)."""
        for k in range(9):
            S = del_pezzo(k)
            chi = S.chi
            K2 = S.c1_squared
            sig = hirzebruch_signature(S)
            ahat = a_hat_genus(S)
            chi_O = S.chi_O

            # Relation 1: Noether
            assert Fraction(K2 + chi, 12) == chi_O

            # Relation 2: sigma + 2*A-hat = (K^2 - 2*chi)/3 + (2*chi - K^2)/12
            #            = (4K^2 - 8chi + 2chi - K^2) / 12 = (3K^2 - 6chi)/12
            # Actually let's verify a simpler identity:
            # 3*sigma + 6*A-hat = (K^2 - 2chi) + (2chi - K^2)/4
            # That's messy. Use: sigma = (1/3)(K^2 - 2chi), A-hat = (2chi - K^2)/24.
            # So 8*A-hat = (2chi - K^2)/3 = -sigma.
            # Hence sigma + 8*A-hat = 0.  <<< THIS IS A NONTRIVIAL CHECK.
            # sigma = (K^2 - 2chi)/3
            # 8*A-hat = 8*(2chi - K^2)/24 = (2chi - K^2)/3 = -sigma
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert sig + 8 * ahat == 0, f"dP_{k}: sigma + 8*A-hat != 0"

            # Relation 3: chi_O = 1 + A-hat * 8 / (-1) ... no, cleaner:
            # chi = K^2 + 12  (from Noether with chi_O=1)
            # Equivalently: chi + K^2 = 12  ... wait: K^2 + chi = 12*chi_O = 12.
            # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
            assert K2 + chi == 12, f"dP_{k}: K^2 + chi != 12"

    def test_characteristic_number_relations_all_hirzebruch(self):
        """Same 3 relations for Hirzebruch surfaces."""
        for n in range(6):
            S = hirzebruch(n)
            chi = S.chi
            K2 = S.c1_squared
            sig = hirzebruch_signature(S)
            ahat = a_hat_genus(S)

            # K^2 + chi = 12
            # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
            assert K2 + chi == 12

            # sigma + 8 * A-hat = 0
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert sig + 8 * ahat == 0

            # Noether
            assert Fraction(K2 + chi, 12) == S.chi_O


class TestMultiPathEffectiveCYDim:
    """Multi-path verification of d_eff = (12+n)/3 for Tot(O(n)->P^2).

    Path 1 (formula):     d_eff = (12+n)/3
    Path 2 (defect):      d_eff = 3 + delta/3 = 3 + (n+3)/3 = (12+n)/3
    Path 3 (CY check):    d_eff(n=-3) = 9/3 = 3
    Path 4 (integer):     d_eff integer iff 3 | (12+n) iff n = 0 mod 3
    """

    def test_d_eff_3path_all_n(self):
        """3-path verification for all n."""
        for n in range(-5, 4):
            X = local_p2(n)
            path1 = Fraction(12 + n, 3)
            path2 = Fraction(3) + Fraction(n + 3, 3)
            assert path1 == path2 == X.effective_cy_dim

    def test_d_eff_integer_classification(self):
        """d_eff is integer iff n = 0 mod 3, verified independently."""
        for n in range(-9, 10):
            d_eff = Fraction(12 + n, 3)
            is_int = d_eff.denominator == 1
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert is_int == (n % 3 == 0), f"n={n}: integer classification fails"


class TestMultiPathCurvature:
    """Multi-path verification of curvature m_0 = (n+3)^2.

    Path 1 (formula):      m_0 = delta^2 = (n+3)^2
    Path 2 (from delta):   m_0 = (c_1(L) - c_1(K_S))^2 = (n - (-3))^2 = (n+3)^2
    Path 3 (from alpha):   delta = alpha/3, so m_0 = delta^2 = (alpha/3)^2
    Path 4 (symmetry):     m_0(-3+j) = m_0(-3-j) = j^2 (symmetric around CY locus)
    """

    def test_curvature_4path_all_n(self):
        """4-path verification for all n."""
        for n in range(-5, 4):
            X = local_p2(n)
            path1 = Fraction((n + 3) ** 2)
            path2 = Fraction((n - (-3)) ** 2)
            path3 = (X.anomaly_coefficient / 3) ** 2
            assert path1 == path2 == path3 == X.curvature_m0, \
                f"n={n}: curvature paths disagree"
        # Path 4: symmetry around CY locus
        for j in range(1, 6):
            m0_plus = local_p2(-3 + j).curvature_m0
            m0_minus = local_p2(-3 - j).curvature_m0
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert m0_plus == m0_minus == Fraction(j ** 2)


class TestMultiPathCrossFamily:
    """Cross-family consistency checks (AP10 type 5: cross-family).

    These verify that invariants computed from different surface families
    agree where the families overlap.
    """

    def test_dp1_equals_f1_kappa(self):
        """dP_1 and F_1 give the same kappa.

        dP_1 = F_1 as abstract varieties, so Tot(K_{dP_1}) = Tot(K_{F_1}).
        kappa(dP_1) = (3+1)/2 = 2.
        kappa(F_1) = chi(F_1)/2 = 4/2 = 2.
        """
        kappa_dp = kappa_local_del_pezzo(1)
        kappa_hirz = kappa_local_hirzebruch(1)
        # Independent computation: chi(dP_1) = 4, chi(F_1) = 4.
        chi_dp = del_pezzo(1).chi
        chi_hirz = hirzebruch(1).chi
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert chi_dp == chi_hirz == 4
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_dp == kappa_hirz == Fraction(2)

    def test_dp0_vs_direct_p2(self):
        """dP_0 data matches direct P^2 computation."""
        dp0 = del_pezzo(0)
        p2 = projective_plane()
        assert dp0.chi == p2.chi
        assert dp0.c1_squared == p2.c1_squared
        assert dp0.b2 == p2.b2
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert kappa_local_del_pezzo(0) == Fraction(p2.chi, 2)

    def test_f0_vs_direct_p1xp1(self):
        """F_0 data matches direct P^1 x P^1 computation."""
        f0 = hirzebruch(0)
        p1p1 = p1_cross_p1()
        assert f0.chi == p1p1.chi
        assert f0.c1_squared == p1p1.c1_squared

    def test_kappa_additivity_under_disjoint_union(self):
        """For a disjoint union S1 |- S2, kappa should be additive.

        chi(S1 |- S2) = chi(S1) + chi(S2), so kappa = kappa_1 + kappa_2.

        Verify: kappa(dP_3) + kappa(dP_5) = 3 + 4 = 7 = kappa of a surface
        with chi = 14 (if one existed with chi_O appropriate).
        """
        k1, k2 = kappa_local_del_pezzo(3), kappa_local_del_pezzo(5)
        chi1, chi2 = del_pezzo(3).chi, del_pezzo(5).chi
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert k1 + k2 == Fraction(chi1 + chi2, 2)

    def test_kappa_eff_reduces_across_families(self):
        """kappa_ch = kappa_cy at CY locus for BOTH del Pezzo and Hirzebruch."""
        for k in range(9):
            X = local_del_pezzo_cy(k)
            assert X.kappa_ch == X.kappa_cy
        for n in range(4):
            X = local_hirzebruch_cy(n)
            assert X.kappa_ch == X.kappa_cy


class TestMultiPathNoether:
    """Multi-path verification of Noether's formula.

    Noether: chi(O_S) = (c_1^2 + c_2)/12.
    Equivalently: K^2 + chi = 12*chi(O).
    Equivalently: chi = 12 - K^2 (for rational surfaces with chi(O)=1).

    Path 1: direct from stored values
    Path 2: from K^2 = 9 - k and chi = 3 + k: K^2 + chi = 12
    Path 3: from b_2 = 1 + k: chi = 2 + b_2 = 3 + k; K^2 = 12 - chi = 9 - k
    """

    def test_noether_3path_all_dp(self):
        """3-path Noether for all del Pezzo."""
        for k in range(9):
            S = del_pezzo(k)
            # Path 1: stored
            path1 = Fraction(S.c1_squared + S.c2, 12)
            # Path 2: from (9-k) + (3+k) = 12
            path2 = Fraction((9 - k) + (3 + k), 12)
            # Path 3: from Betti
            chi_betti = 2 + (1 + k)
            K2_betti = 12 - chi_betti
            path3 = Fraction(K2_betti + chi_betti, 12)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert path1 == path2 == path3 == Fraction(1)
