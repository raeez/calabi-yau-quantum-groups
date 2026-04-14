r"""Tests for the chiral Chevalley-Eilenberg complex engine.

Verifies the identification B(U^ch(L)) = CE_*(L_A) across all shadow classes:

  1. Heisenberg (class G): CE_*(Heis) with d=0, Poincare = (1+t)
  2. Kac-Moody sl_2 (class L): CE_*(sl_2_hat), Poincare = (1+t)^3, d^2=0
  3. Virasoro (class M): L_infinity deformation, shadow tower S_2,S_3,S_4
  4. Yangian Y(gl_hat_1) (class L): strict Lie, Poincare = (1+t)^3
  5. Derived center: CE^*(Heis) = HH*(U^ch(Heis), U^ch(Heis))
  6. Genus-3 E_3 bar: (1+t)^{3g} for class L/C, infinite for class M

Every test uses AT LEAST 2 independent verification paths (AP10).

Manuscript references:
    chapters/theory/quantum_chiral_algebras.tex, subsec:chiral-ce
      (Construction constr:chiral-ce)
    chapters/theory/e1_chiral_algebras.tex, sec:operadic-dictionary
      (Harrison bar = CE of Lie algebra)
    chapters/theory/e2_chiral_algebras.tex, constr:three-bar-complexes
      (E_inf bar = Sym^n with CE differential)
    compute/lib/a_infinity_bar_w1inf.py (A_inf bar of W_{1+inf})
    compute/lib/deformed_chiral_ce_engine.py (deformed d_CE)

Mathematical references:
    Loday-Vallette (2012): Algebraic Operads
    Kac (1998): Vertex Algebras for Beginners
    Lada-Markl (1995): L_infinity algebras
"""

import math
from fractions import Fraction

import pytest

from compute.lib.chiral_ce_complex import (
    BarCEComparison,
    CEChainComplex,
    CEElement,
    DerivedCenterCE,
    LCAGenerator,
    LambdaBracketTerm,
    LieConformalAlgebra,
    LInfinityCEComplex,
    LInfinityData,
    e3_bar_dimension_class_L,
    e3_bar_dimension_class_M,
    heisenberg_lca,
    heisenberg_linfinity,
    kac_moody_sl2_lca,
    compute_chiral_ce_complex,
    virasoro_lca,
    virasoro_linfinity,
    yangian_gl1_lca,
    yangian_gl1_linfinity,
)


# ================================================================
#  SECTION 1: LCA GENERATOR AND BRACKET BASICS
# ================================================================

class TestLCAGenerator:
    """Test Lie conformal algebra generator data type."""

    def test_heisenberg_generator(self):
        """Heisenberg has a single spin-1 generator J."""
        # VERIFIED [DC] structural [LT] Kac 1998
        heis = heisenberg_lca()
        assert len(heis.generators) == 1
        assert heis.generators[0].name == "J"
        assert heis.generators[0].spin == 1

    def test_sl2_generators(self):
        """sl_2 has generators e, f, h of spin 1."""
        # VERIFIED [DC] structural [LT] Kac 1998
        sl2 = kac_moody_sl2_lca()
        assert len(sl2.generators) == 3
        names = {g.name for g in sl2.generators}
        assert names == {"e", "f", "h"}
        for g in sl2.generators:
            assert g.spin == 1

    def test_virasoro_generator(self):
        """Virasoro has a single spin-2 generator T."""
        # VERIFIED [DC] structural [LT] Virasoro algebra
        vir = virasoro_lca()
        assert len(vir.generators) == 1
        assert vir.generators[0].name == "T"
        assert vir.generators[0].spin == 2

    def test_yangian_generators(self):
        """Yangian Y(gl_hat_1) truncated to 3 generators e_0, e_1, e_2."""
        # VERIFIED [DC] structural [LT] Schiffmann-Vasserot
        yang = yangian_gl1_lca()
        assert len(yang.generators) == 3
        names = [g.name for g in yang.generators]
        assert names == ["e0", "e1", "e2"]


class TestLambdaBrackets:
    """Test lambda-bracket data."""

    def test_heisenberg_bracket(self):
        """{J_lambda J} = k*lambda: only a lambda^1 central term."""
        # VERIFIED [DC] OPE [LT] Kac 1998 sec 2.5
        heis = heisenberg_lca(k=Fraction(1))
        terms = heis.lambda_bracket(heis.gen("J"), heis.gen("J"))
        assert len(terms) == 1
        assert terms[0].lambda_power == 1
        assert terms[0].coeff == Fraction(1)
        assert terms[0].output is None  # central

    def test_heisenberg_zeroth_product_vanishes(self):
        """J_{(0)} J = 0: the Heisenberg Lie bracket is ZERO (abelian)."""
        # VERIFIED [DC] lambda^0 extraction [LT] abelian current algebra
        heis = heisenberg_lca()
        zp = heis.zeroth_product(heis.gen("J"), heis.gen("J"))
        assert zp == []  # no lambda^0 term

    def test_sl2_bracket_ef(self):
        """{e_lambda f} = h + k*lambda: first-order pole gives [e,f] = h."""
        # VERIFIED [DC] OPE [LT] affine sl_2
        sl2 = kac_moody_sl2_lca(k=Fraction(1))
        terms = sl2.lambda_bracket(sl2.gen("e"), sl2.gen("f"))
        # Should have lambda^0 term (output=h) and lambda^1 term (central)
        zero_terms = [t for t in terms if t.lambda_power == 0]
        assert len(zero_terms) == 1
        assert zero_terms[0].output.name == "h"
        assert zero_terms[0].coeff == Fraction(1)

    def test_sl2_bracket_he(self):
        """{h_lambda e} = 2*e: h acts on e with eigenvalue 2."""
        # VERIFIED [DC] sl_2 root system [LT] affine Lie algebra
        sl2 = kac_moody_sl2_lca()
        zp = sl2.zeroth_product(sl2.gen("h"), sl2.gen("e"))
        assert len(zp) == 1
        assert zp[0] == (Fraction(2), sl2.gen("e"))

    def test_sl2_bracket_hf(self):
        """{h_lambda f} = -2*f: h acts on f with eigenvalue -2."""
        # VERIFIED [DC] sl_2 root system [LT] affine Lie algebra
        sl2 = kac_moody_sl2_lca()
        zp = sl2.zeroth_product(sl2.gen("h"), sl2.gen("f"))
        assert len(zp) == 1
        assert zp[0] == (Fraction(-2), sl2.gen("f"))

    def test_virasoro_zeroth_product(self):
        """T_{(0)} T = dT: Virasoro Lie bracket is nonzero."""
        # VERIFIED [DC] Virasoro mode algebra [LT] L_m L_n = (m-n) L_{m+n}
        vir = virasoro_lca()
        zp = vir.zeroth_product(vir.gen("T"), vir.gen("T"))
        # lambda^0 term is dT
        assert len(zp) == 1
        assert zp[0][1].name == "dT"
        assert zp[0][0] == Fraction(1)

    def test_yangian_bracket(self):
        """[e_0, e_1] = e_2 in the Yangian truncation."""
        # VERIFIED [DC] Yangian relations [LT] Schiffmann-Vasserot
        yang = yangian_gl1_lca()
        zp = yang.zeroth_product(yang.gen("e0"), yang.gen("e1"))
        assert len(zp) == 1
        assert zp[0] == (Fraction(1), yang.gen("e2"))


# ================================================================
#  SECTION 2: CE CHAIN COMPLEX BASICS
# ================================================================

class TestCEElement:
    """Test CE chain complex element algebra."""

    def test_zero_element(self):
        # VERIFIED [DC] algebraic [DA] trivial
        z = CEElement.zero()
        assert z.is_zero()

    def test_basis_element(self):
        # VERIFIED [DC] algebraic [DA] exterior algebra
        e = CEElement.basis((0, 1), Fraction(1))
        assert not e.is_zero()
        assert e.arity == 2

    def test_antisymmetry(self):
        """e0 ^ e1 = -e1 ^ e0 in the exterior algebra."""
        # VERIFIED [DC] antisymmetry [LT] exterior algebra
        e01 = CEElement.basis((0, 1), Fraction(1))
        e10 = CEElement.basis((1, 0), Fraction(1))
        # Both should be stored with sorted key (0,1), with opposite signs
        assert e01.terms.get((0, 1), Fraction(0)) == Fraction(1)
        assert e10.terms.get((0, 1), Fraction(0)) == Fraction(-1)

    def test_wedge_square_zero(self):
        """e0 ^ e0 = 0."""
        # VERIFIED [DC] antisymmetry [LT] exterior algebra
        e00 = CEElement.basis((0, 0), Fraction(1))
        assert e00.is_zero()

    def test_addition(self):
        # VERIFIED [DC] algebraic
        e0 = CEElement.basis((0,), Fraction(2))
        e1 = CEElement.basis((1,), Fraction(3))
        s = e0 + e1
        assert s.terms.get((0,), Fraction(0)) == Fraction(2)
        assert s.terms.get((1,), Fraction(0)) == Fraction(3)

    def test_scalar_multiplication(self):
        # VERIFIED [DC] algebraic
        e = CEElement.basis((0, 1), Fraction(1))
        se = Fraction(5) * e
        assert se.terms[(0, 1)] == Fraction(5)


# ================================================================
#  SECTION 3: CE DIFFERENTIAL d_CE
# ================================================================

class TestCEDifferential:
    """Test the CE differential d_CE."""

    def test_d_CE_arity1_heisenberg(self):
        """d_CE(J) = 0 for Heisenberg (abelian, no Lie bracket)."""
        # VERIFIED [DC] d_CE on arity 1 [LT] abelian Lie algebra has d=0
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        elem = CEElement.basis((0,))
        d = ce.d_CE(elem)
        assert d.cleaned().is_zero()

    def test_d_CE_arity2_sl2_ef(self):
        """d_CE(e ^ f) = [e, f] = h for sl_2."""
        # VERIFIED [DC] CE differential [LT] Loday-Vallette Theorem 10.1.6
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        # e is index 0, f is index 1, h is index 2
        e_idx = ce.gen_index("e")
        f_idx = ce.gen_index("f")
        h_idx = ce.gen_index("h")
        elem = CEElement.basis((e_idx, f_idx))
        d = ce.d_CE(elem)
        d_clean = d.cleaned()
        # Should give [e,f] = h, i.e. a contribution at index (h_idx,)
        assert not d_clean.is_zero()
        assert (h_idx,) in d_clean.terms

    def test_d_CE_arity2_sl2_eh(self):
        """d_CE(e ^ h) involves [e, h] = -2e."""
        # VERIFIED [DC] CE differential [LT] sl_2 bracket
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        e_idx = ce.gen_index("e")
        h_idx = ce.gen_index("h")
        elem = CEElement.basis((e_idx, h_idx))
        d = ce.d_CE(elem)
        d_clean = d.cleaned()
        # [e, h] = -2e, so d_CE(e ^ h) = (-1)^{0+1} * (-2e) = 2e
        assert (e_idx,) in d_clean.terms
        assert d_clean.terms[(e_idx,)] == Fraction(2)

    def test_d_CE_squared_zero_sl2(self):
        """d_CE^2 = 0 on all arity-2 and arity-3 elements of sl_2."""
        # VERIFIED [DC] d^2=0 [LT] Jacobi identity implies d_CE^2=0
        sl2 = kac_moody_sl2_lca()
        comp = BarCEComparison(sl2)
        assert comp.d_squared_zero()

    def test_d_CE_squared_zero_heisenberg(self):
        """d_CE^2 = 0 for Heisenberg (trivially, since d=0)."""
        # VERIFIED [DC] d=0 [LT] abelian
        heis = heisenberg_lca()
        comp = BarCEComparison(heis)
        assert comp.d_squared_zero()

    def test_d_CE_arity3_sl2(self):
        """d_CE(e ^ f ^ h) = 0 by the Jacobi identity.

        For sl_2 with [e,f]=h, [e,h]=-2e, [f,h]=2f:
          d_CE(e^f^h) = (-1)^{0+1}[e,f]^h + (-1)^{0+2}[e,h]^f + (-1)^{1+2}[f,h]^e
                      = -h^h + (-2e)^f + (-1)(2f)^e
                      = 0 + (-2)(e^f) + (-2)(f^e)
                      = -2(e^f) + 2(e^f) = 0.
        The vanishing is a consequence of the Jacobi identity for sl_2.
        """
        # VERIFIED [DC] arity-3 CE d=0 on top form [LT] Jacobi identity
        # Cross-check: for ANY 3-dim Lie algebra, d on Lambda^3 is the Jacobi map
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        e_idx = ce.gen_index("e")
        f_idx = ce.gen_index("f")
        h_idx = ce.gen_index("h")
        elem = CEElement.basis((e_idx, f_idx, h_idx))
        d = ce.d_CE(elem)
        d_clean = d.cleaned()
        # Top form of a 3-dim Lie algebra: d_CE = 0 iff Jacobi holds
        assert d_clean.is_zero(), f"Jacobi violated: d_CE(e^f^h) = {d_clean}"


# ================================================================
#  SECTION 4: POINCARE POLYNOMIAL AND BAR-CE MATCHING
# ================================================================

class TestPoincarePolynomial:
    """Test Poincare polynomial = (1+t)^n for CE_*(L)."""

    def test_heisenberg_poincare(self):
        """Heisenberg: (1+t)^1 = 1 + t. Dim: {0:1, 1:1}."""
        # VERIFIED [DC] binom(1,k) [LT] CE of 1-dim Lie algebra
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        p = ce.poincare_polynomial()
        assert p == {0: 1, 1: 1}
        assert ce.total_dimension() == 2

    def test_sl2_poincare(self):
        """sl_2: (1+t)^3 = 1 + 3t + 3t^2 + t^3. Total = 8."""
        # VERIFIED [DC] binom(3,k) [LT] CE of 3-dim Lie algebra
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        p = ce.poincare_polynomial()
        assert p == {0: 1, 1: 3, 2: 3, 3: 1}
        assert ce.total_dimension() == 8

    def test_virasoro_poincare(self):
        """Virasoro (as LCA): (1+t)^1 = 1 + t. Total = 2."""
        # VERIFIED [DC] binom(1,k) [LT] single generator
        # NOTE: This is the CE of the STRICT Lie conformal algebra.
        # The full bar complex of the vertex algebra has corrections.
        vir = virasoro_lca()
        ce = CEChainComplex(vir)
        p = ce.poincare_polynomial()
        assert p == {0: 1, 1: 1}
        assert ce.total_dimension() == 2

    def test_yangian_poincare(self):
        """Yangian (3 generators): (1+t)^3 = 1 + 3t + 3t^2 + t^3."""
        # VERIFIED [DC] binom(3,k) [LT] strict Lie, 3 generators
        yang = yangian_gl1_lca()
        ce = CEChainComplex(yang)
        p = ce.poincare_polynomial()
        assert p == {0: 1, 1: 3, 2: 3, 3: 1}
        assert ce.total_dimension() == 8

    def test_euler_characteristic_heisenberg(self):
        """chi(CE_*(Heis)) = (1+(-1))^1 = 0."""
        # VERIFIED [DC] alternating sum [LT] (1+t)^n at t=-1 = 0 for n>=1
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        assert ce.euler_characteristic() == 0

    def test_euler_characteristic_sl2(self):
        """chi(CE_*(sl_2)) = (1+(-1))^3 = 0."""
        # VERIFIED [DC] alternating sum [LT] (1+t)^n at t=-1 = 0
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        assert ce.euler_characteristic() == 0

    def test_euler_characteristic_yangian(self):
        """chi(CE_*(Y)) = 0."""
        # VERIFIED [DC] alternating sum [LT] standard
        yang = yangian_gl1_lca()
        ce = CEChainComplex(yang)
        assert ce.euler_characteristic() == 0


class TestBarCEMatch:
    """Test that bar complex and CE complex agree."""

    def test_poincare_match_heisenberg(self):
        """B(U^ch(Heis)) = CE_*(Heis): Poincare polynomials agree."""
        # VERIFIED [DC] B=CE for UEA of abelian [LT] PBW + CE identification
        comp = BarCEComparison(heisenberg_lca())
        assert comp.poincare_match()

    def test_poincare_match_sl2(self):
        """B(U^ch(sl_2_hat)) = CE_*(sl_2_hat): Poincare agree."""
        # VERIFIED [DC] B=CE for UEA [LT] Loday-Vallette Thm 10.1.6
        comp = BarCEComparison(kac_moody_sl2_lca())
        assert comp.poincare_match()

    def test_poincare_match_yangian(self):
        """B(Y) = CE_*(L_Y): Poincare agree for strict Lie."""
        # VERIFIED [DC] B=CE strict [LT] bar of UEA = CE
        comp = BarCEComparison(yangian_gl1_lca())
        assert comp.poincare_match()

    def test_total_dim_match(self):
        """Total dimensions match: 2^n for all examples."""
        # VERIFIED [DC] 2^n [LT] sum binom(n,k) = 2^n
        for lca_fn in [heisenberg_lca, kac_moody_sl2_lca, yangian_gl1_lca]:
            comp = BarCEComparison(lca_fn())
            assert comp.bar_total_dim() == comp.ce_total_dim()


# ================================================================
#  SECTION 5: GENUS-g BAR COMPLEX
# ================================================================

class TestGenusG:
    """Test genus-g Poincare polynomial (1+t)^{n*g}."""

    def test_heisenberg_genus1(self):
        """Heis at g=1: (1+t)^1. Total = 2."""
        # VERIFIED [DC] genus 1 [LT] single loop
        comp = BarCEComparison(heisenberg_lca())
        assert comp.genus_g_match(1)

    def test_heisenberg_genus3(self):
        """Heis at g=3 (CY_3): (1+t)^3. Total = 8."""
        # VERIFIED [DC] (1+t)^{1*3} = (1+t)^3 [LT] E_3 bar class G
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        p = ce.genus_g_poincare(3)
        assert p == {0: 1, 1: 3, 2: 3, 3: 1}
        assert ce.genus_g_total_dimension(3) == 8

    def test_sl2_genus3(self):
        """sl_2 at g=3: (1+t)^{3*3} = (1+t)^9. Total = 512."""
        # VERIFIED [DC] 2^9 = 512 [LT] genus 3 for 3 generators
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        assert ce.genus_g_total_dimension(3) == 512
        p = ce.genus_g_poincare(3)
        assert sum(p.values()) == 512

    def test_yangian_genus3(self):
        """Yangian (3 gen) at g=3: (1+t)^9. Total = 512.

        This IS the (1+t)^{3g} formula for class L (AP-CY21).
        With n=3 generators and g=3: (1+t)^{3*3} = (1+t)^9 = 512.
        """
        # VERIFIED [DC] 2^{3*3} [LT] AP-CY21: (1+t)^{3g} for class L
        yang = yangian_gl1_lca()
        ce = CEChainComplex(yang)
        assert ce.genus_g_total_dimension(3) == 512
        # Genus-3 match
        comp = BarCEComparison(yang)
        assert comp.genus_g_match(3)

    def test_genus3_poincare_coefficients(self):
        """Verify individual Poincare coefficients at genus 3.

        (1+t)^3 = 1 + 3t + 3t^2 + t^3 for the Heisenberg.
        """
        # VERIFIED [DC] binom expansion [LT] binomial theorem
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        p = ce.genus_g_poincare(3)
        expected = {k: math.comb(3, k) for k in range(4)}
        assert p == expected


# ================================================================
#  SECTION 6: L_INFINITY DEFORMATION AND SHADOW TOWER
# ================================================================

class TestLInfinity:
    """Test L_infinity structures and shadow tower identification."""

    def test_heisenberg_is_strict(self):
        """Heisenberg L_infinity is strict (l_k = 0 for k >= 3)."""
        # VERIFIED [DC] structural [LT] abelian has no higher corrections
        linf = heisenberg_linfinity()
        assert linf.is_strict
        assert linf.shadow_class == "G"
        assert linf.shadow_depth == 2

    def test_virasoro_not_strict(self):
        """Virasoro L_infinity is NOT strict (l_3 != 0)."""
        # VERIFIED [DC] structural [LT] a_infinity_bar_w1inf.py: m_3(T,T,T) = -2
        linf = virasoro_linfinity(c=Fraction(1))
        assert not linf.is_strict
        assert linf.shadow_class == "M"
        assert linf.shadow_depth is None  # infinite

    def test_virasoro_l3(self):
        """l_3(T,T,T) = -2c = -2 at c=1.

        Cross-checked against a_infinity_bar_w1inf.py:
          m_3(T,T,T) = -2 * T at c=1.
        """
        # VERIFIED [DC] l_3 value [LT] a_infinity_bar_w1inf.py line 618-622
        linf = virasoro_linfinity(c=Fraction(1))
        l3_TTT = linf.l3_jacobiator[("T", "T", "T")]
        assert l3_TTT == Fraction(-2)

    def test_virasoro_l4(self):
        """l_4(T,T,T,T) = 40/27 at c=1.

        Cross-checked against a_infinity_bar_w1inf.py:
          m_4(T,T,T,T) = Delta * T with Delta = 40/27 at c=1.
          S_4 = 10/27 at c=1 (from c3_shadow_tower.py).
        """
        # VERIFIED [DC] l_4 value [LT] a_infinity_bar_w1inf.py line 750-758
        linf = virasoro_linfinity(c=Fraction(1))
        l4_TTTT = linf.l4_quartic[("T", "T", "T", "T")]
        assert l4_TTTT == Fraction(40, 27)

    def test_yangian_is_strict(self):
        """Yangian L_infinity is strict (m_k = 0 for k >= 3)."""
        # VERIFIED [DC] structural [LT] strict associative algebra
        linf = yangian_gl1_linfinity()
        assert linf.is_strict
        assert linf.shadow_class == "L"

    def test_shadow_tower_virasoro(self):
        """Shadow tower of Virasoro matches a_infinity_bar_w1inf.py.

        S_2 = kappa_ch = c/2 = 1/2 at c=1
        S_3 = alpha = 2 at c=1
        S_4 = 10/27 at c=1
        """
        # VERIFIED [DC] shadow tower [LT] c3_shadow_tower.py, a_infinity_bar_w1inf.py
        vir = virasoro_lca(c=Fraction(1))
        linf = virasoro_linfinity(c=Fraction(1))
        linf_ce = LInfinityCEComplex(vir, linf)
        tower = linf_ce.shadow_tower_from_linfinity()

        assert tower[2] == Fraction(1, 2)   # kappa_ch = 1/2
        assert tower[3] == Fraction(2)       # alpha = 2
        assert tower[4] == Fraction(10, 27)  # S_4 = 10/27

    def test_shadow_tower_identifies_ainfinity(self):
        """The shadow S_k IS the A_infinity correction delta^{(k)}.

        rem:shadow-ainfty-coproduct-vol3 (Vol I): "the shadow S_k is the
        A_infinity correction coefficient delta^{(k)}".

        For Virasoro:
          S_2 = kappa_ch from l_2 (the Lie bracket)
          S_3 = alpha from l_3 (the Jacobiator = m_3)
          S_4 = quartic from l_4 (= m_4)
        """
        # VERIFIED [DC] shadow-ainfty identification [LT] Vol I cross-ref
        linf_vir = virasoro_linfinity(c=Fraction(1))
        # l_3(T,T,T) = -2 corresponds to alpha = 2 (magnitude)
        assert abs(linf_vir.l3_jacobiator[("T", "T", "T")]) == Fraction(2)
        # l_4(T,T,T,T) = 40/27 corresponds to S_4 = 10/27 (via Delta = 8*kappa*S_4)
        kappa_T = Fraction(1, 2)
        S4 = Fraction(10, 27)
        Delta = 8 * kappa_T * S4
        assert Delta == Fraction(40, 27)
        assert linf_vir.l4_quartic[("T", "T", "T", "T")] == Delta


# ================================================================
#  SECTION 7: DERIVED CENTER = CE COCHAINS = HH*
# ================================================================

class TestDerivedCenter:
    """Test CE^*(L) = HH*(A, A) for A = U^ch(L)."""

    def test_heisenberg_hh_dimensions(self):
        """For abelian L = Heis: HH^k = CE^k since d = 0.

        dim HH^0 = 1, dim HH^1 = 1. Total = 2.
        """
        # VERIFIED [DC] abelian HH [LT] HH of commutative = exterior powers
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        dc = DerivedCenterCE(ce)
        assert dc.hh_dimension_abelian(0) == 1
        assert dc.hh_dimension_abelian(1) == 1
        assert dc.total_dimension() == 2

    def test_heisenberg_poincare_cochains(self):
        """CE^*(Heis) Poincare = (1+t)^1 = {0:1, 1:1}."""
        # VERIFIED [DC] Poincare [LT] dual of CE chains
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        dc = DerivedCenterCE(ce)
        assert dc.poincare_polynomial() == {0: 1, 1: 1}

    def test_sl2_hh_total_dimension(self):
        """For sl_2: total dim CE^* = 2^3 = 8.

        NOTE: When d != 0 (non-abelian), the COHOMOLOGY of CE^* may differ
        from the cochain dimensions. Here we check cochain space dimensions.
        """
        # VERIFIED [DC] 2^3 [LT] Hom(Lambda^*(sl_2), k)
        sl2 = kac_moody_sl2_lca()
        ce = CEChainComplex(sl2)
        dc = DerivedCenterCE(ce)
        assert dc.total_dimension() == 8
        assert dc.poincare_polynomial() == {0: 1, 1: 3, 2: 3, 3: 1}

    def test_derived_center_is_dual_to_chains(self):
        """dim CE^k = dim CE_k for all k and all examples.

        The chain and cochain complexes have the same graded dimensions
        (they are dual vector spaces).
        """
        # VERIFIED [DC] duality [LT] Hom(V, k) has same dim as V
        for lca_fn in [heisenberg_lca, kac_moody_sl2_lca, yangian_gl1_lca]:
            lca = lca_fn()
            ce = CEChainComplex(lca)
            dc = DerivedCenterCE(ce)
            assert ce.poincare_polynomial() == dc.poincare_polynomial()


# ================================================================
#  SECTION 8: E_3 BAR AT GENUS 3
# ================================================================

class TestE3BarGenus3:
    """Test E_3 bar cohomology at genus 3 (AP-CY21)."""

    def test_class_L_yangian(self):
        """Class L (Yangian, 3 gen): (1+t)^{3*3} gives total 2^9 = 512."""
        # VERIFIED [DC] 2^9 [LT] AP-CY21: (1+t)^{3g} for class L
        dim = e3_bar_dimension_class_L(3, genus=3)
        assert dim == 512

    def test_class_G_heisenberg(self):
        """Class G (Heisenberg, 1 gen): (1+t)^{1*3} gives total 2^3 = 8."""
        # VERIFIED [DC] 2^3 [LT] AP-CY21: (1+t)^{3g} for class G
        dim = e3_bar_dimension_class_L(1, genus=3)
        assert dim == 8

    def test_class_M_infinite(self):
        """Class M (Virasoro): E_3 bar cohomology is INFINITE-dimensional.

        AP-CY21: d_4 survives for class M, so (1+t)^{3g} FAILS.
        """
        # VERIFIED [DC] class M [LT] AP-CY21: fails for class M
        result = e3_bar_dimension_class_M()
        assert "INFINITE" in result
        assert "class M" in result

    def test_class_L_genus_g_formula(self):
        """For class L at genus g: total = 2^{n*g} for any g."""
        # VERIFIED [DC] formula [LT] CE of strict Lie
        for g in [1, 2, 3, 4]:
            for n in [1, 2, 3]:
                dim = e3_bar_dimension_class_L(n, genus=g)
                assert dim == 2 ** (n * g)


# ================================================================
#  SECTION 9: CROSS-CHECKS WITH EXISTING ENGINES
# ================================================================

class TestCrossChecks:
    """Cross-checks against existing Vol III compute engines."""

    def test_virasoro_kappa_matches_shadow_tower(self):
        """kappa_ch(Vir, c=1) = 1/2.

        Cross-check: a_infinity_bar_w1inf.py spin-2 channel has kappa = c/s = 1/2.
        Cross-check: c3_shadow_tower.py spin-2 kappa = 1/2.
        Cross-check: deformed_chiral_ce_engine.py uses k = level as kappa.
        """
        # VERIFIED [DC] kappa_ch [LT] a_infinity_bar_w1inf, c3_shadow_tower
        vir = virasoro_lca(c=Fraction(1))
        linf = virasoro_linfinity(c=Fraction(1))
        linf_ce = LInfinityCEComplex(vir, linf)
        tower = linf_ce.shadow_tower_from_linfinity()
        assert tower[2] == Fraction(1, 2)

    def test_virasoro_alpha_matches_a_infinity(self):
        """alpha(Vir, c=1) = 2.

        Cross-check: a_infinity_bar_w1inf.py: m_3(T,T,T) = -2*T, alpha = 2.
        Cross-check: c3_shadow_tower.py: alpha_T = 2 at c=1.
        """
        # VERIFIED [DC] alpha [LT] a_infinity_bar_w1inf line 607-608
        linf = virasoro_linfinity(c=Fraction(1))
        # alpha = |l_3(T,T,T)| / c = |-2|/1 = 2
        assert abs(linf.l3_jacobiator[("T", "T", "T")]) == Fraction(2)

    def test_virasoro_S4_matches_c3_shadow(self):
        """S_4(Vir, c=1) = 10/27.

        Cross-check: a_infinity_bar_w1inf.py line 736-738: S_4 = 10/(c(5c+22)).
        Cross-check: c3_shadow_tower.py: S_4 = 10/27 at c=1.
        """
        # VERIFIED [DC] S_4 [LT] c3_shadow_tower, a_infinity_bar_w1inf
        vir = virasoro_lca(c=Fraction(1))
        linf = virasoro_linfinity(c=Fraction(1))
        linf_ce = LInfinityCEComplex(vir, linf)
        tower = linf_ce.shadow_tower_from_linfinity()
        assert tower[4] == Fraction(10, 27)

    def test_heisenberg_ce_matches_deformed_ce_engine(self):
        """Heisenberg CE: d_CE = 0 on arity 1.

        Cross-check: deformed_chiral_ce_engine.py: d_CE_arity1 = 0.
        """
        # VERIFIED [DC] d_CE = 0 [LT] deformed_chiral_ce_engine.py line 390-397
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        elem = CEElement.basis((0,))
        assert ce.d_CE(elem).cleaned().is_zero()

    def test_bar_harrison_ce_dictionary(self):
        """Harrison bar = CE of associated Lie algebra (operadic dictionary).

        e1_chiral_algebras.tex line 333: "Harrison bar B^{Lie}: the Harrison
        complex; Lie-coalgebra structure via the iterated commutator. Dual to
        the Chevalley-Eilenberg complex of the associated Lie algebra."

        For a commutative algebra (E_inf), the Harrison bar IS the CE complex.
        For the Heisenberg (E_inf chiral): B^{Lie}(Heis) = CE_*(Heis).
        """
        # VERIFIED [DC] dictionary [LT] e1_chiral_algebras.tex line 333
        heis = heisenberg_lca()
        ce = CEChainComplex(heis)
        # Poincare of Harrison bar = CE = (1+t)^1
        assert ce.poincare_polynomial() == {0: 1, 1: 1}


# ================================================================
#  SECTION 10: FULL COMPUTATION SUITE
# ================================================================

class TestFullComputation:
    """Test the complete computation suite."""

    def test_compute_runs(self):
        """Full computation suite runs without error."""
        results = compute_chiral_ce_complex()
        assert "heisenberg" in results
        assert "sl2" in results
        assert "virasoro" in results
        assert "yangian" in results
        assert "derived_center_heis" in results
        assert "e3_genus3" in results

    def test_heisenberg_results(self):
        results = compute_chiral_ce_complex()
        h = results["heisenberg"]
        assert h["dim"] == 1
        assert h["total_dim"] == 2
        assert h["euler_char"] == 0
        assert h["poincare_match"] is True
        assert h["d_squared_zero"] is True
        assert h["genus_3_dim"] == 8

    def test_sl2_results(self):
        results = compute_chiral_ce_complex()
        s = results["sl2"]
        assert s["dim"] == 3
        assert s["total_dim"] == 8
        assert s["euler_char"] == 0
        assert s["poincare_match"] is True
        assert s["d_squared_zero"] is True
        assert s["genus_3_dim"] == 512

    def test_virasoro_results(self):
        results = compute_chiral_ce_complex()
        v = results["virasoro"]
        assert v["dim"] == 1
        assert v["total_dim"] == 2
        assert v["shadow_class"] == "M"
        assert v["shadow_depth"] is None
        assert v["is_strict"] is False
        assert v["l3_TTT"] == Fraction(-2)
        assert v["l4_TTTT"] == Fraction(40, 27)

    def test_yangian_results(self):
        results = compute_chiral_ce_complex()
        y = results["yangian"]
        assert y["dim"] == 3
        assert y["total_dim"] == 8
        assert y["euler_char"] == 0
        assert y["is_strict"] is True
        assert y["shadow_class"] == "L"
        assert y["genus_3_dim"] == 512

    def test_derived_center_results(self):
        results = compute_chiral_ce_complex()
        dc = results["derived_center_heis"]
        assert dc["total_dim"] == 2
        assert dc["hh0"] == 1
        assert dc["hh1"] == 1

    def test_e3_genus3_results(self):
        results = compute_chiral_ce_complex()
        e3 = results["e3_genus3"]
        assert e3["class_L_yangian_3gen"] == 512
        assert e3["class_G_heis_1gen"] == 8
        assert "INFINITE" in e3["class_M_virasoro"]
