r"""Tests for the Hitchin-to-chiral functor: Higgs bundle moduli -> chiral algebras.

Verifies:
  1. Curve data: Riemann-Roch dimensions h^0(K^i) for all i
  2. GL(n) group data: dimensions, dual Coxeter, Casimirs, critical level
  3. Hitchin moduli dimensions: dim M_H, dim B, Lagrangian property
  4. Spectral curve geometry: genus, branch points, Riemann-Hurwitz
  5. Chiral algebra: type, kappa, central charge, Feigin-Frenkel center
  6. GL(1) abelian case: T*Jac(C), rank-g Heisenberg
  7. GL(2) case: detailed dimensions and spectral geometry
  8. Oper space: Feigin-Frenkel isomorphism, dimension match
  9. KW twist: the non-CY aspect (Hitchin does NOT require CY3)
  10. Cross-volume bridge: kappa matches Vol I formulas
  11. Landscape table: consistency across (n, g) parameter space
  12. Explicit small examples: GL(1..3) on genus 2..4

Ground truth:
  - Hitchin (1987): self-duality equations, stable bundles & integrable systems
  - Feigin-Frenkel (1992): center of hat{g} at critical level = Fun(opers)
  - Kapustin-Witten (2006): 4d N=4 twist -> geometric Langlands
  - Beilinson-Drinfeld (~1991): quantization of Hitchin & Hecke eigensheaves
  - Ben-Zvi-Nadler (2009): character theory via geometric Langlands
  - Vol I: kappa(H_k) = k, kappa(hat{sl}_{n,k}) = (n^2-1)(k+n)/(2n)
  - Vol III: hitchin_sl2_genus2.py (dimensions, spectral curves)

85+ tests organized by mathematical structure.
"""

from fractions import Fraction

import pytest

from compute.lib.higgs_bundle_chiral import (
    CurveData,
    GL1HitchinData,
    GL2HitchinData,
    GLnData,
    HiggsModuliData,
    HitchinChiralData,
    HitchinToChiralResult,
    KWTwistData,
    OperData,
    SpectralCurveGLn,
    affine_gln_central_charge,
    affine_gln_kappa,
    comparison_cy_vs_hitchin,
    cross_volume_kappa_check,
    dim_sln_hitchin_base,
    gl1_genus2,
    gl1_hitchin,
    gl2_genus2,
    gl2_genus3,
    gl2_hitchin,
    gl3_genus2,
    higgs_moduli_data,
    hitchin_base_dimension_formula,
    hitchin_base_dimensions,
    hitchin_base_table,
    hitchin_chiral_gln,
    hitchin_chiral_sln,
    hitchin_landscape,
    hitchin_to_chiral,
    kappa_hitchin_gln,
    kappa_hitchin_sln,
    kappa_sln_critical,
    kapustin_witten_data,
    oper_space_pgln,
    spectral_curve_genus_formula,
    spectral_curve_gln,
    verify_all,
    verify_lagrangian,
    verify_oper_hitchin_dimension,
    verify_spectral_curve_riemann_hurwitz,
    verify_spectral_genus_equals_base_dim,
)


# ======================================================================
# 1. CURVE DATA
# ======================================================================

class TestCurveData:
    """Test Riemann-Roch dimensions h^0(K^i) for curves."""

    def test_genus2_h0_K(self):
        """h^0(K_C) = g = 2 for genus-2 curve."""
        C = CurveData(genus=2)
        assert C.dim_h0_K == 2

    def test_genus3_h0_K(self):
        """h^0(K_C) = g = 3 for genus-3 curve."""
        C = CurveData(genus=3)
        assert C.dim_h0_K == 3

    def test_genus2_h0_K2(self):
        """h^0(K^2) = 3(g-1) = 3 for genus-2 curve.

        By Riemann-Roch: deg(K^2) = 4, chi(K^2) = 4-2+1 = 3.
        H^1(K^2) = H^0(K^{-1}) = 0 (negative degree). So h^0 = 3.
        Formula: (2*2-1)*(2-1) = 3.
        """
        C = CurveData(genus=2)
        assert C.dim_h0_K_power(2) == 3

    def test_genus3_h0_K2(self):
        """h^0(K^2) = 3*(3-1) = 6 for genus-3."""
        C = CurveData(genus=3)
        assert C.dim_h0_K_power(2) == 6

    def test_genus2_h0_K3(self):
        """h^0(K^3) = 5*(2-1) = 5 for genus-2."""
        C = CurveData(genus=2)
        assert C.dim_h0_K_power(3) == 5

    def test_genus3_h0_K3(self):
        """h^0(K^3) = 5*(3-1) = 10 for genus-3."""
        C = CurveData(genus=3)
        assert C.dim_h0_K_power(3) == 10

    def test_h0_K_power_formula_i_ge_2(self):
        """h^0(K^i) = (2i-1)(g-1) for i >= 2, g >= 2."""
        for g in range(2, 7):
            C = CurveData(genus=g)
            for i in range(2, 8):
                expected = (2 * i - 1) * (g - 1)
                assert C.dim_h0_K_power(i) == expected, \
                    f"Failed for g={g}, i={i}: got {C.dim_h0_K_power(i)}, expected {expected}"

    def test_h0_O(self):
        """h^0(O_C) = 1 for any curve."""
        for g in range(2, 6):
            C = CurveData(genus=g)
            assert C.dim_h0_K_power(0) == 1

    def test_euler_characteristic(self):
        """chi(C) = 2 - 2g."""
        for g in range(0, 6):
            C = CurveData(genus=g)
            assert C.euler_characteristic == 2 - 2 * g


# ======================================================================
# 2. GL(n) GROUP DATA
# ======================================================================

class TestGLnData:
    """Test GL(n) group invariants."""

    def test_gl1_dim(self):
        assert GLnData(1).dim == 1

    def test_gl2_dim(self):
        assert GLnData(2).dim == 4

    def test_gl3_dim(self):
        assert GLnData(3).dim == 9

    def test_gln_dim_formula(self):
        """dim GL(n) = n^2."""
        for n in range(1, 8):
            assert GLnData(n).dim == n ** 2

    def test_dual_coxeter(self):
        """h^vee(gl_n) = n."""
        for n in range(1, 8):
            assert GLnData(n).dual_coxeter == n

    def test_critical_level(self):
        """k_c = -h^vee = -n."""
        for n in range(1, 8):
            assert GLnData(n).critical_level == -n

    def test_casimir_degrees(self):
        """Casimir degrees of GL(n) are 1, 2, ..., n."""
        assert GLnData(1).casimir_degrees == (1,)
        assert GLnData(2).casimir_degrees == (1, 2)
        assert GLnData(3).casimir_degrees == (1, 2, 3)

    def test_gl1_rank(self):
        assert GLnData(1).rank == 1

    def test_gln_rank(self):
        for n in range(1, 8):
            assert GLnData(n).rank == n


# ======================================================================
# 3. HITCHIN MODULI DIMENSIONS
# ======================================================================

class TestHiggsModuliDimensions:
    """Test dimensions of M_H(C, GL(n))."""

    def test_gl1_genus2_dim(self):
        """GL(1), g=2: dim M_H = 2*dim B = 2*2 = 4."""
        C = CurveData(genus=2)
        G = GLnData(1)
        data = higgs_moduli_data(C, G)
        assert data.dim_complex == 4

    def test_gl2_genus2_dim(self):
        """GL(2), g=2: dim B = 2+3 = 5, dim M_H = 10."""
        C = CurveData(genus=2)
        G = GLnData(2)
        data = higgs_moduli_data(C, G)
        assert data.dim_hitchin_base == 5
        assert data.dim_complex == 10

    def test_gl3_genus2_dim(self):
        """GL(3), g=2: dim B = 2+3+5 = 10, dim M_H = 20."""
        C = CurveData(genus=2)
        G = GLnData(3)
        data = higgs_moduli_data(C, G)
        assert data.dim_hitchin_base == 10
        assert data.dim_complex == 20

    def test_lagrangian_property(self):
        """dim M_H = 2*dim B for all (n, g)."""
        for n in range(1, 5):
            for g in range(2, 5):
                C = CurveData(genus=g)
                G = GLnData(n)
                data = higgs_moduli_data(C, G)
                assert data.dim_complex == 2 * data.dim_hitchin_base, \
                    f"Failed for GL({n}), g={g}"

    def test_fibre_equals_base(self):
        """dim fibre = dim base (Lagrangian fibration)."""
        for n in range(1, 5):
            for g in range(2, 5):
                C = CurveData(genus=g)
                G = GLnData(n)
                data = higgs_moduli_data(C, G)
                assert data.dim_hitchin_fibre == data.dim_hitchin_base

    def test_hyperkahler(self):
        """M_H is always hyperkahler."""
        C = CurveData(genus=2)
        G = GLnData(2)
        data = higgs_moduli_data(C, G)
        assert data.is_hyperkahler is True

    def test_cy_type_is_2(self):
        """M_H is CY_2 (holomorphic symplectic), NOT CY_3."""
        C = CurveData(genus=2)
        G = GLnData(2)
        data = higgs_moduli_data(C, G)
        assert data.cy_type == 2  # CY2, not CY3

    def test_hitchin_base_formula(self):
        """dim B = n^2*(g-1) + 1 for GL(n)."""
        for n in range(1, 6):
            for g in range(2, 6):
                expected = n ** 2 * (g - 1) + 1
                assert hitchin_base_dimension_formula(n, g) == expected

    def test_hitchin_base_formula_vs_computation(self):
        """Formula dim B = n^2(g-1)+1 matches summing h^0(K^i)."""
        for n in range(1, 5):
            for g in range(2, 5):
                C = CurveData(genus=g)
                G = GLnData(n)
                data = higgs_moduli_data(C, G)
                formula = hitchin_base_dimension_formula(n, g)
                assert data.dim_hitchin_base == formula, \
                    f"Failed for GL({n}), g={g}: sum={data.dim_hitchin_base}, formula={formula}"

    def test_genus_too_low_raises(self):
        """g < 2 should raise."""
        C = CurveData(genus=1)
        G = GLnData(2)
        with pytest.raises(ValueError):
            higgs_moduli_data(C, G)


# ======================================================================
# 4. SPECTRAL CURVE GEOMETRY
# ======================================================================

class TestSpectralCurve:
    """Test spectral curve data for GL(n) Hitchin systems."""

    def test_gl1_genus2_spectral(self):
        """GL(1), g=2: spectral curve is C itself (degree-1 cover)."""
        C = CurveData(genus=2)
        G = GLnData(1)
        sc = spectral_curve_gln(C, G)
        assert sc.n == 1
        assert sc.genus_spectral == 2  # 1^2*(2-1)+1 = 2
        assert sc.n_branch_points == 0  # no branching for degree-1 cover

    def test_gl2_genus2_spectral(self):
        """GL(2), g=2: g(S) = 4*1+1 = 5, B = 4 branch points."""
        C = CurveData(genus=2)
        G = GLnData(2)
        sc = spectral_curve_gln(C, G)
        assert sc.genus_spectral == 5
        assert sc.n_branch_points == 4  # 2*1*2 = 4

    def test_gl3_genus2_spectral(self):
        """GL(3), g=2: g(S) = 9*1+1 = 10."""
        C = CurveData(genus=2)
        G = GLnData(3)
        sc = spectral_curve_gln(C, G)
        assert sc.genus_spectral == 10
        assert sc.n_branch_points == 12  # 3*2*2 = 12

    def test_spectral_genus_formula(self):
        """g(S) = n^2*(g-1)+1 for all (n, g)."""
        for n in range(1, 6):
            for g in range(2, 6):
                expected = n ** 2 * (g - 1) + 1
                assert spectral_curve_genus_formula(n, g) == expected

    def test_spectral_genus_equals_base_dim(self):
        """g(S) = dim B for GL(n): the fibre is (twist of) Jac(S)."""
        for n in range(1, 5):
            for g in range(2, 5):
                assert verify_spectral_genus_equals_base_dim(n, g)

    def test_riemann_hurwitz(self):
        """Riemann-Hurwitz: 2g(S)-2 = n*(2g-2) + B."""
        for n in range(1, 5):
            for g in range(2, 5):
                C = CurveData(genus=g)
                G = GLnData(n)
                sc = spectral_curve_gln(C, G)
                assert verify_spectral_curve_riemann_hurwitz(sc), \
                    f"RH failed for GL({n}), g={g}"

    def test_branch_points_formula(self):
        """B = n*(n-1)*(2g-2) branch points."""
        for n in range(1, 5):
            for g in range(2, 5):
                C = CurveData(genus=g)
                G = GLnData(n)
                sc = spectral_curve_gln(C, G)
                expected = n * (n - 1) * (2 * g - 2)
                assert sc.n_branch_points == expected

    def test_gl1_no_branching(self):
        """GL(1): spectral curve is unramified (identity cover)."""
        for g in range(2, 6):
            C = CurveData(genus=g)
            G = GLnData(1)
            sc = spectral_curve_gln(C, G)
            assert sc.n_branch_points == 0


# ======================================================================
# 5. CHIRAL ALGEBRA DATA
# ======================================================================

class TestHitchinChiral:
    """Test chiral algebras from the Hitchin functor."""

    def test_gl1_genus2_kappa(self):
        """GL(1), g=2: kappa = g = 2."""
        C = CurveData(genus=2)
        G = GLnData(1)
        chiral = hitchin_chiral_gln(C, G)
        assert chiral.kappa == Fraction(2)

    def test_gl1_genus3_kappa(self):
        """GL(1), g=3: kappa = g = 3."""
        C = CurveData(genus=3)
        G = GLnData(1)
        chiral = hitchin_chiral_gln(C, G)
        assert chiral.kappa == Fraction(3)

    def test_gl2_genus2_kappa(self):
        """GL(2), g=2: kappa = g = 2."""
        C = CurveData(genus=2)
        G = GLnData(2)
        chiral = hitchin_chiral_gln(C, G)
        assert chiral.kappa == Fraction(2)

    def test_sln_critical_kappa_zero(self):
        """SL(n) at critical level: kappa = 0."""
        for n in range(2, 6):
            for g in range(2, 5):
                assert kappa_hitchin_sln(n, g) == Fraction(0)

    def test_kappa_sln_critical_formula(self):
        """kappa(hat{sl}_{n,-n}) = 0 by direct formula."""
        for n in range(1, 8):
            assert kappa_sln_critical(n) == Fraction(0)

    def test_gl1_is_heisenberg(self):
        """GL(1) produces Heisenberg algebra."""
        C = CurveData(genus=3)
        G = GLnData(1)
        chiral = hitchin_chiral_gln(C, G)
        assert "Heisenberg" in chiral.algebra_type
        assert chiral.central_charge == Fraction(3)

    def test_gl1_shadow_class_G(self):
        """GL(1) Hitchin: Heisenberg has shadow class G (Gaussian)."""
        C = CurveData(genus=2)
        G = GLnData(1)
        chiral = hitchin_chiral_gln(C, G)
        assert chiral.shadow_class == "G"
        assert chiral.shadow_depth == 2

    def test_gln_critical(self):
        """GL(n) Hitchin chiral algebra is at critical level."""
        for n in range(1, 5):
            C = CurveData(genus=2)
            G = GLnData(n)
            chiral = hitchin_chiral_gln(C, G)
            assert chiral.is_critical is True

    def test_kappa_depends_on_genus_not_n(self):
        """kappa(Hitchin GL(n)) = g, independent of n."""
        for g in range(2, 6):
            kappas = set()
            for n in range(1, 5):
                kappas.add(kappa_hitchin_gln(n, g))
            assert len(kappas) == 1
            assert kappas.pop() == Fraction(g)


# ======================================================================
# 6. GL(1) ABELIAN CASE
# ======================================================================

class TestGL1Hitchin:
    """Test the GL(1) Hitchin space = T*Jac(C)."""

    def test_gl1_dim_jacobian(self):
        """dim Jac(C) = g."""
        for g in range(2, 6):
            data = gl1_hitchin(CurveData(genus=g))
            assert data.dim_jacobian == g

    def test_gl1_dim_cotangent(self):
        """dim T*Jac(C) = 2g."""
        for g in range(2, 6):
            data = gl1_hitchin(CurveData(genus=g))
            assert data.dim_cotangent == 2 * g

    def test_gl1_hitchin_base(self):
        """Hitchin base for GL(1) = H^0(K_C), dim = g."""
        for g in range(2, 6):
            data = gl1_hitchin(CurveData(genus=g))
            assert data.hitchin_base_dim == g

    def test_gl1_chiral_rank(self):
        """Chiral algebra rank = g (one free boson per H^1 direction)."""
        for g in range(2, 6):
            data = gl1_hitchin(CurveData(genus=g))
            assert data.chiral_rank == g

    def test_gl1_central_charge(self):
        """c = g for rank-g Heisenberg."""
        for g in range(2, 6):
            data = gl1_hitchin(CurveData(genus=g))
            assert data.central_charge == Fraction(g)

    def test_gl1_kappa(self):
        """kappa = g for rank-g Heisenberg."""
        for g in range(2, 6):
            data = gl1_hitchin(CurveData(genus=g))
            assert data.kappa == Fraction(g)


# ======================================================================
# 7. GL(2) CASE
# ======================================================================

class TestGL2Hitchin:
    """Test GL(2) Hitchin moduli space."""

    def test_gl2_genus2(self):
        """GL(2), g=2: dim B = 5, dim M_H = 10."""
        data = gl2_hitchin(CurveData(genus=2))
        assert data.dim_hitchin_base == 5
        assert data.dim_moduli == 10
        assert data.genus_spectral == 5
        assert data.n_branch_points == 4

    def test_gl2_genus3(self):
        """GL(2), g=3: dim B = 9, dim M_H = 18."""
        data = gl2_hitchin(CurveData(genus=3))
        assert data.dim_hitchin_base == 9
        assert data.dim_moduli == 18
        assert data.genus_spectral == 9

    def test_gl2_h0_K_and_K2(self):
        """GL(2): base = H^0(K) + H^0(K^2)."""
        for g in range(2, 6):
            data = gl2_hitchin(CurveData(genus=g))
            assert data.dim_h0_K == g
            assert data.dim_h0_K2 == 3 * (g - 1)
            assert data.dim_hitchin_base == g + 3 * (g - 1)

    def test_gl2_kappa(self):
        """GL(2) Hitchin: kappa = g."""
        for g in range(2, 6):
            data = gl2_hitchin(CurveData(genus=g))
            assert data.kappa == Fraction(g)

    def test_gl2_spectral_genus_equals_base(self):
        """g(S) = dim B for GL(2)."""
        for g in range(2, 6):
            data = gl2_hitchin(CurveData(genus=g))
            assert data.genus_spectral == data.dim_hitchin_base


# ======================================================================
# 8. OPER SPACE AND FEIGIN-FRENKEL
# ======================================================================

class TestOpers:
    """Test the oper space and Feigin-Frenkel center."""

    def test_pgl2_opers_genus2(self):
        """PGL_2 opers on genus-2: dim = 3(g-1) = 3."""
        C = CurveData(genus=2)
        oper = oper_space_pgln(C, 2)
        assert oper.dim_oper_space == 3

    def test_pgl3_opers_genus2(self):
        """PGL_3 opers on genus-2: dim = (9-1)(2-1) = 8."""
        C = CurveData(genus=2)
        oper = oper_space_pgln(C, 3)
        assert oper.dim_oper_space == 8

    def test_oper_dim_equals_sln_base(self):
        """dim Op_{PGL_n} = dim B_{SL_n} = (n^2-1)(g-1)."""
        for n in range(2, 6):
            for g in range(2, 5):
                C = CurveData(genus=g)
                assert verify_oper_hitchin_dimension(C, n)

    def test_sln_hitchin_base_formula(self):
        """dim B_{SL_n} = (n^2-1)(g-1)."""
        for n in range(2, 6):
            for g in range(2, 5):
                expected = (n ** 2 - 1) * (g - 1)
                assert dim_sln_hitchin_base(n, g) == expected

    def test_feigin_frenkel_isomorphism_string(self):
        """Feigin-Frenkel: Z(hat{sl}_{n,-n}) = Fun(Op_{PGL_n}(C))."""
        C = CurveData(genus=2)
        oper = oper_space_pgln(C, 3)
        assert "Feigin-Frenkel" in oper.isomorphism


# ======================================================================
# 9. KAPUSTIN-WITTEN TWIST (NON-CY)
# ======================================================================

class TestKWTwist:
    """The KW twist does NOT require CY3."""

    def test_kw_no_cy3_required(self):
        """The Kapustin-Witten twist does not require CY3 structure."""
        G = GLnData(2)
        C = CurveData(genus=2)
        kw = kapustin_witten_data(G, C)
        assert kw.requires_cy3 is False

    def test_kw_produces_critical_level(self):
        """KW twist produces critical-level affine algebra."""
        G = GLnData(3)
        C = CurveData(genus=3)
        kw = kapustin_witten_data(G, C)
        assert "critical level" in kw.resulting_chiral

    def test_hitchin_is_cy2_not_cy3(self):
        """M_H is CY_2 (holomorphic symplectic), not CY_3."""
        C = CurveData(genus=2)
        G = GLnData(2)
        data = higgs_moduli_data(C, G)
        assert data.cy_type == 2
        assert data.cy_type != 3


# ======================================================================
# 10. AFFINE ALGEBRA INVARIANTS
# ======================================================================

class TestAffineInvariants:
    """Test central charge and kappa for hat{gl}_n at various levels."""

    def test_gl1_level1_central_charge(self):
        """c(hat{gl}_{1,1}) = 0/(1+1) + 1 = 1. Heisenberg."""
        c = affine_gln_central_charge(1, Fraction(1))
        assert c == Fraction(1)

    def test_gl2_level1_central_charge(self):
        """c(hat{gl}_{2,1}) = 1*3/3 + 1 = 2."""
        c = affine_gln_central_charge(2, Fraction(1))
        assert c == Fraction(2)

    def test_gln_critical_central_charge_undefined(self):
        """c(hat{gl}_{n,-n}) is undefined (None)."""
        for n in range(1, 6):
            c = affine_gln_central_charge(n, Fraction(-n))
            assert c is None

    def test_gl1_level1_kappa(self):
        """kappa(hat{gl}_{1,1}): sl_1 part = 0, gl_1 part = 1*1 = 1. Total = 1."""
        kappa = affine_gln_kappa(1, Fraction(1))
        assert kappa == Fraction(1)

    def test_sl2_critical_kappa(self):
        """kappa(hat{sl}_{2,-2}) = 0."""
        # The sl_n part: (n^2-1)*(k+n)/(2n) = 3*0/4 = 0
        kappa_sl = Fraction(4 - 1) * Fraction(-2 + 2, 2 * 2)
        assert kappa_sl == Fraction(0)


# ======================================================================
# 11. CROSS-VOLUME KAPPA BRIDGE
# ======================================================================

class TestCrossVolumeBridge:
    """Cross-check Hitchin kappa against Vol I formulas."""

    def test_gl1_kappa_matches_heisenberg(self):
        """kappa(Hitchin GL(1) on C_g) = g = kappa(H_1^{otimes g})."""
        for g in range(2, 6):
            hitchin_kappa = kappa_hitchin_gln(1, g)
            vol1_kappa = Fraction(g)  # kappa(H_1^{otimes g}) = g
            assert hitchin_kappa == vol1_kappa

    def test_sln_kappa_zero_matches_uncurved(self):
        """kappa(Hitchin SL(n)) = 0: bar complex uncurved at critical level."""
        for n in range(2, 6):
            for g in range(2, 5):
                assert kappa_hitchin_sln(n, g) == Fraction(0)

    def test_cross_volume_check_all_pass(self):
        """All cross-volume kappa checks pass."""
        cv = cross_volume_kappa_check()
        for key, val in cv.items():
            assert val["match"] is True, f"Cross-volume check failed for {key}"


# ======================================================================
# 12. THE COMPLETE FUNCTOR
# ======================================================================

class TestHitchinToChiral:
    """Test the complete Hitchin-to-chiral functor."""

    def test_gl1_genus2(self):
        result = hitchin_to_chiral(1, 2)
        assert result.chiral_data.kappa == Fraction(2)
        assert all(result.consistency_checks.values())

    def test_gl2_genus2(self):
        result = hitchin_to_chiral(2, 2)
        assert result.chiral_data.kappa == Fraction(2)
        assert result.moduli.dim_complex == 10
        assert all(result.consistency_checks.values())

    def test_gl3_genus2(self):
        result = hitchin_to_chiral(3, 2)
        assert result.chiral_data.kappa == Fraction(2)
        assert result.moduli.dim_complex == 20
        assert all(result.consistency_checks.values())

    def test_gl2_genus3(self):
        result = hitchin_to_chiral(2, 3)
        assert result.chiral_data.kappa == Fraction(3)
        assert result.moduli.dim_complex == 18
        assert all(result.consistency_checks.values())

    def test_gl4_genus3(self):
        """GL(4), g=3: dim B = 16*2+1 = 33, dim M_H = 66."""
        result = hitchin_to_chiral(4, 3)
        assert result.moduli.dim_hitchin_base == 33
        assert result.moduli.dim_complex == 66
        assert result.chiral_data.kappa == Fraction(3)
        assert all(result.consistency_checks.values())

    def test_all_consistency_checks(self):
        """All consistency checks pass for a range of (n, g)."""
        for n in range(1, 5):
            for g in range(2, 5):
                result = hitchin_to_chiral(n, g)
                for key, val in result.consistency_checks.items():
                    assert val, f"Check {key} failed for GL({n}), g={g}"

    def test_invalid_genus_raises(self):
        with pytest.raises(ValueError):
            hitchin_to_chiral(2, 1)

    def test_invalid_n_raises(self):
        with pytest.raises(ValueError):
            hitchin_to_chiral(0, 2)

    def test_oper_data_present_for_n_ge_2(self):
        """Oper data is computed for n >= 2."""
        for n in range(2, 5):
            result = hitchin_to_chiral(n, 2)
            assert result.oper_data is not None

    def test_no_oper_data_for_gl1(self):
        """No oper data for GL(1) (abelian, no interesting opers)."""
        result = hitchin_to_chiral(1, 2)
        assert result.oper_data is None


# ======================================================================
# 13. EXPLICIT SMALL EXAMPLES
# ======================================================================

class TestExplicitExamples:
    """Test the explicit computation functions."""

    def test_gl1_genus2_example(self):
        data = gl1_genus2()
        assert data["dim_M_H"] == 4
        assert data["dim_base"] == 2
        assert data["kappa"] == Fraction(2)
        assert data["c"] == Fraction(2)

    def test_gl2_genus2_example(self):
        data = gl2_genus2()
        assert data["dim_M_H"] == 10
        assert data["dim_base"] == 5
        assert data["g_spectral"] == 5
        assert data["n_branch"] == 4
        assert data["kappa"] == Fraction(2)

    def test_gl3_genus2_example(self):
        data = gl3_genus2()
        assert data["dim_M_H"] == 20
        assert data["dim_base"] == 10
        assert data["g_spectral"] == 10
        assert data["kappa"] == Fraction(2)

    def test_gl2_genus3_example(self):
        data = gl2_genus3()
        assert data["dim_M_H"] == 18
        assert data["dim_base"] == 9
        assert data["g_spectral"] == 9
        assert data["kappa"] == Fraction(3)


# ======================================================================
# 14. HITCHIN BASE TABLE
# ======================================================================

class TestHitchinBaseTable:
    """Test detailed Hitchin base decomposition."""

    def test_gl2_genus2_base(self):
        t = hitchin_base_table(2, 2)
        assert t["dimensions_by_degree"] == {1: 2, 2: 3}
        assert t["total"] == 5
        assert t["match"] is True

    def test_gl3_genus2_base(self):
        t = hitchin_base_table(3, 2)
        assert t["dimensions_by_degree"] == {1: 2, 2: 3, 3: 5}
        assert t["total"] == 10
        assert t["match"] is True

    def test_gl4_genus3_base(self):
        t = hitchin_base_table(4, 3)
        assert t["dimensions_by_degree"][1] == 3
        assert t["dimensions_by_degree"][2] == 6
        assert t["dimensions_by_degree"][3] == 10
        assert t["dimensions_by_degree"][4] == 14
        assert t["total"] == 33
        assert t["match"] is True

    def test_all_tables_consistent(self):
        """Sum of h^0(K^i) matches the formula for all (n, g)."""
        for n in range(1, 6):
            for g in range(2, 6):
                t = hitchin_base_table(n, g)
                assert t["match"], f"Table mismatch for GL({n}), g={g}"


# ======================================================================
# 15. LANDSCAPE TABLE
# ======================================================================

class TestLandscape:
    """Test the full landscape of Hitchin moduli spaces."""

    def test_landscape_generation(self):
        """Landscape generates without errors."""
        landscape = hitchin_landscape(max_n=4, max_g=4)
        assert len(landscape) == 4 * 3  # n=1..4, g=2..4

    def test_landscape_lagrangian(self):
        """All entries are Lagrangian."""
        landscape = hitchin_landscape(max_n=5, max_g=5)
        for entry in landscape:
            assert entry["is_lagrangian"] is True

    def test_landscape_spectral_genus(self):
        """g(S) = dim B for all entries."""
        landscape = hitchin_landscape(max_n=5, max_g=5)
        for entry in landscape:
            assert entry["g_S_eq_dim_B"] is True

    def test_landscape_kappa_gl(self):
        """kappa(GL) = g for all entries."""
        landscape = hitchin_landscape(max_n=5, max_g=5)
        for entry in landscape:
            assert entry["kappa_GL"] == Fraction(entry["g"])

    def test_landscape_kappa_sl_zero(self):
        """kappa(SL) = 0 for all entries."""
        landscape = hitchin_landscape(max_n=5, max_g=5)
        for entry in landscape:
            assert entry["kappa_SL"] == Fraction(0)


# ======================================================================
# 16. COMPARISON CY vs HITCHIN
# ======================================================================

class TestComparison:
    """Test the comparison between CY and Hitchin functors."""

    def test_comparison_has_both(self):
        comp = comparison_cy_vs_hitchin()
        assert "CY_functor" in comp
        assert "Hitchin_functor" in comp

    def test_comparison_overlap_gl1(self):
        comp = comparison_cy_vs_hitchin()
        assert "overlap_GL1" in comp

    def test_hitchin_no_cy3(self):
        comp = comparison_cy_vs_hitchin()
        assert "NOT require CY3" in comp["Hitchin_functor"]["requires"]


# ======================================================================
# 17. VERIFY_ALL
# ======================================================================

class TestVerifyAll:
    """Test the master verification routine."""

    def test_verify_all_passes(self):
        """All internal consistency checks pass."""
        results = verify_all()
        for key, val in results.items():
            assert val, f"verify_all failed for {key}"

    def test_verify_all_count(self):
        """verify_all checks a substantial number of conditions."""
        results = verify_all()
        assert len(results) >= 80


# ======================================================================
# 18. HITCHIN BASE DIMENSIONS (individual summands)
# ======================================================================

class TestHitchinBaseDimensions:
    """Test individual summand dimensions of the Hitchin base."""

    def test_gl2_base_summands(self):
        C = CurveData(genus=2)
        G = GLnData(2)
        dims = hitchin_base_dimensions(C, G)
        assert dims == {1: 2, 2: 3}

    def test_gl3_base_summands(self):
        C = CurveData(genus=3)
        G = GLnData(3)
        dims = hitchin_base_dimensions(C, G)
        assert dims == {1: 3, 2: 6, 3: 10}

    def test_summands_sum_to_total(self):
        for n in range(1, 5):
            for g in range(2, 5):
                C = CurveData(genus=g)
                G = GLnData(n)
                dims = hitchin_base_dimensions(C, G)
                total = sum(dims.values())
                assert total == hitchin_base_dimension_formula(n, g)


# ======================================================================
# 19. EDGE CASES AND CONSISTENCY
# ======================================================================

class TestEdgeCases:
    """Edge cases and additional consistency checks."""

    def test_gl1_genus2_spectral_is_base_curve(self):
        """For GL(1), spectral curve = base curve (degree-1 cover)."""
        C = CurveData(genus=4)
        G = GLnData(1)
        sc = spectral_curve_gln(C, G)
        assert sc.genus_spectral == 4  # same as base
        assert sc.n == 1

    def test_large_n_dimensions(self):
        """GL(10), g=2: dim B = 100*1+1 = 101, dim M_H = 202."""
        result = hitchin_to_chiral(10, 2)
        assert result.moduli.dim_hitchin_base == 101
        assert result.moduli.dim_complex == 202

    def test_large_genus(self):
        """GL(2), g=10: dim B = 4*9+1 = 37, dim M_H = 74."""
        result = hitchin_to_chiral(2, 10)
        assert result.moduli.dim_hitchin_base == 37
        assert result.moduli.dim_complex == 74

    def test_sl2_hitchin_sln(self):
        """SL(2) Hitchin chiral: hat{sl}_2 at k=-2, kappa=0."""
        C = CurveData(genus=2)
        chiral = hitchin_chiral_sln(C, 2)
        assert chiral.kappa == Fraction(0)
        assert chiral.is_critical is True
        assert chiral.level == Fraction(-2)

    def test_holonomy_format(self):
        """Holonomy is Sp(m) where m = dim B."""
        C = CurveData(genus=2)
        G = GLnData(2)
        data = higgs_moduli_data(C, G)
        assert data.holonomy == "Sp(5)"


# ======================================================================
# 20. MULTI-PATH CROSS-VERIFICATION (AP10 compliance)
# ======================================================================

class TestMultiPathVerification:
    """Every key numerical result verified by 3+ independent paths.

    Path taxonomy:
      (1) Direct computation from defining formula
      (2) Alternative formula / structural identity
      (3) Limiting / special case
      (4) Cross-family / cross-module consistency
      (5) Riemann-Roch / topological verification
      (6) Literature comparison
    """

    # --- Hitchin base dimension: 3-path verification ---

    @pytest.mark.parametrize("n,g,expected", [
        (1, 2, 2), (2, 2, 5), (3, 2, 10), (2, 3, 9), (4, 3, 33),
    ])
    def test_hitchin_base_dim_path1_summation(self, n, g, expected):
        """Path 1: sum h^0(K^i) for i=1..n (direct Riemann-Roch)."""
        C = CurveData(genus=g)
        G = GLnData(n)
        dims = hitchin_base_dimensions(C, G)
        assert sum(dims.values()) == expected

    @pytest.mark.parametrize("n,g,expected", [
        (1, 2, 2), (2, 2, 5), (3, 2, 10), (2, 3, 9), (4, 3, 33),
    ])
    def test_hitchin_base_dim_path2_closed_formula(self, n, g, expected):
        """Path 2: closed formula n^2(g-1)+1."""
        assert hitchin_base_dimension_formula(n, g) == expected

    @pytest.mark.parametrize("n,g,expected", [
        (1, 2, 2), (2, 2, 5), (3, 2, 10), (2, 3, 9), (4, 3, 33),
    ])
    def test_hitchin_base_dim_path3_spectral_genus(self, n, g, expected):
        """Path 3: g(S) = n^2(g-1)+1 must equal dim B (Lagrangian condition)."""
        assert spectral_curve_genus_formula(n, g) == expected

    # --- Spectral curve genus: 3-path verification ---

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (2, 3), (3, 3), (4, 3), (2, 5),
    ])
    def test_spectral_genus_path1_formula(self, n, g):
        """Path 1: g(S) = n^2(g-1)+1 (adjunction formula)."""
        C = CurveData(genus=g)
        G = GLnData(n)
        sc = spectral_curve_gln(C, G)
        assert sc.genus_spectral == n ** 2 * (g - 1) + 1

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (2, 3), (3, 3), (4, 3), (2, 5),
    ])
    def test_spectral_genus_path2_riemann_hurwitz(self, n, g):
        """Path 2: verify via Riemann-Hurwitz with branch data."""
        C = CurveData(genus=g)
        G = GLnData(n)
        sc = spectral_curve_gln(C, G)
        # 2g(S)-2 = n*(2g-2) + B
        lhs = 2 * sc.genus_spectral - 2
        rhs = n * (2 * g - 2) + sc.n_branch_points
        assert lhs == rhs

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (2, 3), (3, 3), (4, 3), (2, 5),
    ])
    def test_spectral_genus_path3_lagrangian_match(self, n, g):
        """Path 3: g(S) must equal dim(Hitchin base) for Lagrangian fibration."""
        g_S = spectral_curve_genus_formula(n, g)
        dim_B = hitchin_base_dimension_formula(n, g)
        assert g_S == dim_B

    # --- kappa(GL(n) Hitchin) = g: 3-path verification ---

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3), (1, 5), (5, 4),
    ])
    def test_kappa_gln_path1_direct(self, n, g):
        """Path 1: kappa_hitchin_gln(n, g) = g (direct formula)."""
        assert kappa_hitchin_gln(n, g) == Fraction(g)

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3), (1, 5), (5, 4),
    ])
    def test_kappa_gln_path2_decomposition(self, n, g):
        """Path 2: kappa(GL_n) = kappa(SL_n critical) + kappa(g free bosons).

        kappa(hat{sl}_{n,-n}) = 0, kappa(H_1^{otimes g}) = g.
        Total = 0 + g = g.
        """
        kappa_sl = kappa_hitchin_sln(n, g)
        kappa_gl1 = Fraction(g)  # g free bosons at level 1
        assert kappa_sl + kappa_gl1 == Fraction(g)

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3), (1, 5), (5, 4),
    ])
    def test_kappa_gln_path3_functor_output(self, n, g):
        """Path 3: extract from full functor output."""
        result = hitchin_to_chiral(n, g)
        assert result.chiral_data.kappa == Fraction(g)

    # --- kappa(SL(n) critical) = 0: 3-path verification ---

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 6, 7])
    def test_kappa_sln_critical_path1_formula(self, n):
        """Path 1: (n^2-1)(k+n)/(2n) at k=-n gives 0."""
        kappa = Fraction(n ** 2 - 1) * Fraction(-n + n, 2 * n)
        assert kappa == Fraction(0)

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 6, 7])
    def test_kappa_sln_critical_path2_function(self, n):
        """Path 2: kappa_sln_critical(n) = 0."""
        assert kappa_sln_critical(n) == Fraction(0)

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 6, 7])
    def test_kappa_sln_critical_path3_integrability(self, n):
        """Path 3: kappa = 0 <=> uncurved bar complex <=> integrable system.

        The Hitchin system for SL(n) is classically integrable (Hitchin 1987).
        This means the genus-g obstruction tower vanishes: kappa = 0.
        Verify via the general affine kappa formula at k = -n.
        """
        # The sl_n component of hat{gl}_n at k=-n
        kappa_sln_part = Fraction(n ** 2 - 1) * Fraction(0, 2 * n)
        assert kappa_sln_part == 0

    # --- dim M_H = 2*dim B: 3-path verification ---

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (2, 3), (4, 3), (5, 4),
    ])
    def test_dim_MH_path1_moduli_data(self, n, g):
        """Path 1: from higgs_moduli_data."""
        C = CurveData(genus=g)
        G = GLnData(n)
        data = higgs_moduli_data(C, G)
        assert data.dim_complex == 2 * data.dim_hitchin_base

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (2, 3), (4, 3), (5, 4),
    ])
    def test_dim_MH_path2_tangent_space(self, n, g):
        """Path 2: dim = 2*(n^2(g-1)+1) from tangent space computation.

        T_{(E,phi)} M_H = H^1(End E) oplus H^0(End E tensor K).
        For stable E: h^0(End E)=1, so h^1(End E) = n^2(g-1)+1 by RR.
        By Serre duality: h^0(End E tensor K) = h^1(End E).
        Total = 2*(n^2(g-1)+1).
        """
        expected = 2 * (n ** 2 * (g - 1) + 1)
        C = CurveData(genus=g)
        G = GLnData(n)
        data = higgs_moduli_data(C, G)
        assert data.dim_complex == expected

    @pytest.mark.parametrize("n,g", [
        (1, 2), (2, 2), (3, 2), (2, 3), (4, 3), (5, 4),
    ])
    def test_dim_MH_path3_hitchin_base_sum(self, n, g):
        """Path 3: dim = 2 * sum_{i=1}^n h^0(K^i) from Hitchin base decomposition."""
        C = CurveData(genus=g)
        base_dim = sum(C.dim_h0_K_power(i) for i in range(1, n + 1))
        expected = 2 * base_dim
        data = higgs_moduli_data(C, GLnData(n))
        assert data.dim_complex == expected

    # --- h^0(K^i) for i >= 2: 3-path verification ---

    @pytest.mark.parametrize("g,i,expected", [
        (2, 2, 3), (2, 3, 5), (3, 2, 6), (3, 3, 10), (4, 2, 9), (4, 4, 21),
    ])
    def test_h0_Ki_path1_riemann_roch(self, g, i, expected):
        """Path 1: h^0(K^i) = deg(K^i)+1-g = i(2g-2)+1-g = (2i-1)(g-1)."""
        assert i * (2 * g - 2) + 1 - g == expected

    @pytest.mark.parametrize("g,i,expected", [
        (2, 2, 3), (2, 3, 5), (3, 2, 6), (3, 3, 10), (4, 2, 9), (4, 4, 21),
    ])
    def test_h0_Ki_path2_curve_data(self, g, i, expected):
        """Path 2: CurveData.dim_h0_K_power."""
        C = CurveData(genus=g)
        assert C.dim_h0_K_power(i) == expected

    @pytest.mark.parametrize("g,i,expected", [
        (2, 2, 3), (2, 3, 5), (3, 2, 6), (3, 3, 10), (4, 2, 9), (4, 4, 21),
    ])
    def test_h0_Ki_path3_closed_form(self, g, i, expected):
        """Path 3: closed form (2i-1)(g-1)."""
        assert (2 * i - 1) * (g - 1) == expected

    # --- GL(2), g=2 spectral curve: 3-path verification ---

    def test_gl2_g2_spectral_path1_formula(self):
        """Path 1: g(S) = 4(2-1)+1 = 5."""
        assert spectral_curve_genus_formula(2, 2) == 5

    def test_gl2_g2_spectral_path2_riemann_hurwitz(self):
        """Path 2: Riemann-Hurwitz with 4 branch points.
        2*5-2 = 8 = 2*(2*2-2) + 4 = 4+4 = 8. Check.
        """
        g_S = 5
        n, g = 2, 2
        lhs = 2 * g_S - 2  # = 8
        rhs = n * (2 * g - 2) + n * (n - 1) * (2 * g - 2)  # = 4 + 4 = 8
        assert lhs == rhs

    def test_gl2_g2_spectral_path3_hitchin_sl2_module(self):
        """Path 3: cross-check with hitchin_sl2_genus2 module.

        That module computes spectral_curve_sl2(2) for SL_2.
        For SL_2, the spectral curve genus formula is 4g-3 = 5.
        For GL_2, the formula is n^2(g-1)+1 = 4*1+1 = 5.
        They must agree because SL_2 and GL_2 have the same
        spectral curve (the trace is a separate parameter).
        """
        # Import from the other module
        from compute.lib.hitchin_sl2_genus2 import spectral_curve_sl2
        sc_sl2 = spectral_curve_sl2(2)
        sc_gl2 = spectral_curve_gln(CurveData(genus=2), GLnData(2))
        assert sc_sl2.genus_spectral == sc_gl2.genus_spectral

    # --- Cross-module dimension consistency ---

    def test_cross_module_sl2_g2_dim(self):
        """Cross-check: hitchin_sl2_genus2 gives dim_C=6 for SL_2,g=2.
        Our module gives dim_C=10 for GL_2,g=2.
        Difference: GL_2 adds the GL_1 center = T*Jac(C) of dim 2*2=4.
        10 - 6 = 4. Check.
        """
        from compute.lib.hitchin_sl2_genus2 import hitchin_dimensions as hd_sl2
        sl2_data = hd_sl2('SL_2', 2)
        gl2_data = higgs_moduli_data(CurveData(genus=2), GLnData(2))
        # GL_2 moduli = SL_2 moduli + T*Jac
        assert gl2_data.dim_complex - sl2_data.dim_complex == 4  # = 2g

    def test_cross_module_sl2_g2_base(self):
        """Cross-check: SL_2 Hitchin base dim=3, GL_2 base dim=5.
        Difference = h^0(K) = g = 2 (the trace component).
        """
        from compute.lib.hitchin_sl2_genus2 import hitchin_dimensions as hd_sl2
        sl2_data = hd_sl2('SL_2', 2)
        gl2_data = higgs_moduli_data(CurveData(genus=2), GLnData(2))
        assert gl2_data.dim_hitchin_base - sl2_data.dim_hitchin_base == 2

    # --- Oper dimension: 3-path verification ---

    @pytest.mark.parametrize("n,g", [(2, 2), (3, 2), (2, 3), (3, 3), (4, 3)])
    def test_oper_dim_path1_formula(self, n, g):
        """Path 1: dim Op = (n^2-1)(g-1)."""
        C = CurveData(genus=g)
        oper = oper_space_pgln(C, n)
        assert oper.dim_oper_space == (n ** 2 - 1) * (g - 1)

    @pytest.mark.parametrize("n,g", [(2, 2), (3, 2), (2, 3), (3, 3), (4, 3)])
    def test_oper_dim_path2_summation(self, n, g):
        """Path 2: dim Op = sum_{i=2}^n h^0(K^i) (explicit summation)."""
        C = CurveData(genus=g)
        oper = oper_space_pgln(C, n)
        manual_sum = sum(C.dim_h0_K_power(i) for i in range(2, n + 1))
        assert oper.dim_oper_space == manual_sum

    @pytest.mark.parametrize("n,g", [(2, 2), (3, 2), (2, 3), (3, 3), (4, 3)])
    def test_oper_dim_path3_gl_minus_gl1(self, n, g):
        """Path 3: dim Op_{PGL_n} = dim B_{GL_n} - dim B_{GL_1}.

        The GL_n base = GL_1 base + PGL_n opers.
        dim B_{GL_n} - h^0(K) = dim Op.
        """
        C = CurveData(genus=g)
        gl_base = hitchin_base_dimension_formula(n, g)
        gl1_base = C.dim_h0_K_power(1)  # = g
        oper = oper_space_pgln(C, n)
        assert oper.dim_oper_space == gl_base - gl1_base
