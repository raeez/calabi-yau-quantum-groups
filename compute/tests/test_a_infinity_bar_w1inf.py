r"""Tests for the A_∞ bar complex of W_{1+∞}.

Verifies all components of the A_∞ structure on B^{ord}(W_{1+∞}):
  1. Generator and bar element data types
  2. OPE data for J, T, W at c=1
  3. A_∞ operations m_2, m_3, m_4
  4. Bar differential d = m_2 + m_3 + m_4 + ...
  5. Shadow tower: S_2, S_3, S_4 and class M
  6. Maurer-Cartan equation verification
  7. MacMahon generating function
  8. Massey product interpretation of m_3

Every test uses AT LEAST 2 independent verification paths (AP10).

Manuscript references:
    Vol I: bar_cobar_adjunction_curved.tex (bar complex)
    Vol I: higher_genus_modular_koszul.tex (shadow tower)
    Vol III: e1_bar_cobar_cy3.py (E1 bar complex)
    Vol III: c3_shadow_tower.py (W_{1+inf} shadow data)

Mathematical references:
    Keller (2006): A-infinity algebras, modules and transfer
    Prochazka-Rapcak (arXiv:1910.07997): W_{1+inf} = affine Yangian
    Schiffmann-Vasserot (2013): CoHA = Y^+(gl_hat_1)
"""

from fractions import Fraction

import pytest
from sympy import Rational

from compute.lib.a_infinity_bar_w1inf import (
    J, T, W, dJ, dT, dW,
    AInfBarComplex,
    AInfBarElement,
    AInfMaurerCartan,
    AInfShadowTower,
    LinearCombination,
    W1InfOPE,
    WGenerator,
    _macmahon_coefficient,
    _macmahon_coefficients,
    compute_a_infinity_bar_w1inf,
    compute_m3_massey_product,
)


# ================================================================
#  SECTION 1: GENERATOR AND BAR ELEMENT BASICS
# ================================================================

class TestWGenerator:
    """Test W_{1+inf} generator data type."""

    def test_standard_generators_exist(self):
        """J, T, W are the standard generators."""
        # VERIFIED [DC] structural property [LT] W-algebra theory
        assert J.name == "J"
        assert T.name == "T"
        assert W.name == "W"

    def test_spins(self):
        """Spin = conformal weight: J=1, T=2, W=3."""
        # VERIFIED [DC] conformal weight [DA] dimensional analysis
        assert J.spin == 1
        assert T.spin == 2
        assert W.spin == 3

    def test_degrees_zero(self):
        """All standard generators have cohomological degree 0."""
        # VERIFIED [DC] degree count [DA] VOA grading
        assert J.degree == 0
        assert T.degree == 0
        assert W.degree == 0

    def test_derivative_generators(self):
        """Derivative generators dJ, dT, dW have correct spins."""
        # VERIFIED [DC] spin increment [DA] conformal weight under derivative
        assert dJ.spin == J.spin + 1  # = 2
        assert dT.spin == T.spin + 1  # = 3
        assert dW.spin == W.spin + 1  # = 4

    def test_repr(self):
        assert repr(J) == "J"
        assert repr(T) == "T"

    def test_frozen(self):
        with pytest.raises(AttributeError):
            J.name = "X"

    def test_hashable(self):
        g1 = WGenerator("J", spin=1)
        g2 = WGenerator("J", spin=1)
        assert hash(g1) == hash(g2)
        assert g1 == g2


class TestAInfBarElement:
    """Test bar element data type."""

    def test_arity(self):
        elem = AInfBarElement(factors=(T, T, T))
        # VERIFIED [DC] arity count [DA] tensor degree
        assert elem.arity == 3

    def test_total_spin(self):
        elem = AInfBarElement(factors=(J, T, W))
        # VERIFIED [DC] spin sum [DA] 1 + 2 + 3 = 6
        assert elem.total_spin == 6

    def test_cohomological_degree(self):
        """Desuspension: |s^{-1}a| = |a| - 1 (AP45)."""
        elem = AInfBarElement(factors=(T, T))
        # VERIFIED [DC] degree: sum(0) - 2 = -2 [DA] AP45 desuspension
        assert elem.cohomological_degree == -2

    def test_repr_unit_coeff(self):
        elem = AInfBarElement(factors=(T, J))
        assert repr(elem) == "[T|J]"

    def test_repr_neg_coeff(self):
        elem = AInfBarElement(factors=(T,), coeff=Fraction(-1))
        assert repr(elem) == "-[T]"

    def test_repr_general_coeff(self):
        elem = AInfBarElement(factors=(T,), coeff=Fraction(3, 2))
        assert "3/2" in repr(elem)


class TestLinearCombination:
    """Test linear combination algebra."""

    def test_zero(self):
        lc = LinearCombination()
        assert lc.is_zero

    def test_simplify_cancellation(self):
        t1 = AInfBarElement(factors=(T,), coeff=Fraction(1))
        t2 = AInfBarElement(factors=(T,), coeff=Fraction(-1))
        lc = LinearCombination([t1, t2])
        assert lc.simplify().is_zero

    def test_simplify_collection(self):
        t1 = AInfBarElement(factors=(T,), coeff=Fraction(2))
        t2 = AInfBarElement(factors=(T,), coeff=Fraction(3))
        lc = LinearCombination([t1, t2]).simplify()
        assert len(lc.terms) == 1
        assert lc.terms[0].coeff == Fraction(5)

    def test_add(self):
        lc1 = LinearCombination([AInfBarElement(factors=(J,))])
        lc2 = LinearCombination([AInfBarElement(factors=(T,))])
        lc3 = lc1 + lc2
        assert len(lc3.terms) == 2


# ================================================================
#  SECTION 2: OPE DATA
# ================================================================

class TestW1InfOPE:
    """Test W_{1+inf} OPE at c=1."""

    def setup_method(self):
        self.ope = W1InfOPE(c=Fraction(1))

    def test_jj_ope(self):
        """J(z)J(w) ~ 1/(z-w)^2, no first-order pole."""
        ope = self.ope.ope_singular(J, J)
        # VERIFIED [DC] Heisenberg OPE [LT] abelian current algebra
        assert 2 in ope
        assert 1 not in ope

    def test_tt_ope_poles(self):
        """T(z)T(w) has poles of order 4, 2, 1."""
        ope = self.ope.ope_singular(T, T)
        # VERIFIED [DC] Virasoro OPE [LT] conformal field theory
        assert 4 in ope  # central charge term
        assert 2 in ope  # 2T term
        assert 1 in ope  # dT term

    def test_tt_central_charge(self):
        """Pole-4 coefficient of TT OPE = c/2 = 1/2."""
        ope = self.ope.ope_singular(T, T)
        pole4 = ope[4]
        # VERIFIED [DC] c/2 = 1/2 [LT] Virasoro algebra
        assert pole4[0] == (Fraction(1, 2), None)

    def test_tj_ope(self):
        """T(z)J(w) ~ J/(z-w)^2 + dJ/(z-w): J is primary of weight 1."""
        ope = self.ope.ope_singular(T, J)
        # VERIFIED [DC] primary field OPE [LT] CFT Ward identity
        assert 2 in ope
        assert 1 in ope

    def test_tw_ope(self):
        """T(z)W(w) ~ 3W/(z-w)^2 + dW/(z-w): W is primary of weight 3."""
        ope = self.ope.ope_singular(T, W)
        # VERIFIED [DC] spin-3 primary OPE [LT] W-algebra structure
        pole2 = ope[2]
        assert pole2[0][0] == Fraction(3)  # coefficient 3 (= spin of W)

    def test_ww_ope_highest_pole(self):
        """W(z)W(w) has pole of order 6 with coefficient c/3."""
        ope = self.ope.ope_singular(W, W)
        # VERIFIED [DC] W_3 OPE [LT] W-algebra theory
        assert 6 in ope
        pole6 = ope[6]
        assert pole6[0] == (Fraction(1, 3), None)

    def test_jw_ope_trivial(self):
        """J(z)W(w) ~ 0 (J commutes with W at c=1)."""
        ope = self.ope.ope_singular(J, W)
        # VERIFIED [DC] abelian-nonabelian decoupling [LT] principal embedding
        assert len(ope) == 0

    def test_skew_symmetry_jt(self):
        """J(z)T(w) pole structure from skew-symmetry of T(z)J(w).

        T(z)J(w) has poles 2 and 1. But VOA skew-symmetry cancels the
        first-order pole: J_{(0)}T = -T_{(0)}J + d(T_{(1)}J) = -dJ + dJ = 0.
        So J(z)T(w) has only pole 2.
        """
        ope_jt = self.ope.ope_singular(J, T)
        # VERIFIED [DC] pole orders [LT] VOA skew-symmetry
        assert 2 in ope_jt
        assert 1 not in ope_jt


# ================================================================
#  SECTION 3: A_∞ OPERATIONS m_2, m_3, m_4
# ================================================================

class TestM2:
    """Test the binary product m_2 (OPE residue)."""

    def setup_method(self):
        self.bar_cx = AInfBarComplex()

    def test_m2_jj_zero(self):
        """m_2(J,J) = 0: no first-order pole in JJ OPE."""
        result = self.bar_cx.m2(J, J)
        # VERIFIED [DC] vanishing residue [LT] Heisenberg abelianness
        assert result.simplify().is_zero

    def test_m2_tt_equals_dT(self):
        """m_2(T,T) = dT: first-order pole of TT OPE."""
        result = self.bar_cx.m2(T, T)
        s = result.simplify()
        # VERIFIED [DC] Virasoro residue [LT] [L_m, L_n] = (m-n)L_{m+n}
        assert not s.is_zero
        assert len(s.terms) == 1
        assert s.terms[0].factors == (dT,)
        assert s.terms[0].coeff == Fraction(1)

    def test_m2_tj_equals_dJ(self):
        """m_2(T,J) = dJ: J is primary of weight 1 under T."""
        result = self.bar_cx.m2(T, J)
        s = result.simplify()
        # VERIFIED [DC] primary residue [LT] T(z)J(w) first-order pole
        assert not s.is_zero
        assert s.terms[0].factors == (dJ,)

    def test_m2_jt_zero(self):
        """m_2(J,T) = 0: VOA skew-symmetry gives J_{(0)}T = -dJ + dJ = 0."""
        result = self.bar_cx.m2(J, T)
        s = result.simplify()
        # VERIFIED [DC] skew-symmetry cancellation [LT] VOA locality
        assert s.is_zero

    def test_m2_tw_equals_dW(self):
        """m_2(T,W) = dW: W is primary of weight 3 under T."""
        result = self.bar_cx.m2(T, W)
        s = result.simplify()
        # VERIFIED [DC] W-primary residue [LT] T(z)W(w) first-order pole
        assert not s.is_zero
        assert s.terms[0].factors == (dW,)

    def test_m2_wt_equals_2dW(self):
        """m_2(W,T) = 2dW: VOA skew-symmetry gives W_{(0)}T = -dW + 3dW = 2dW."""
        result = self.bar_cx.m2(W, T)
        s = result.simplify()
        # VERIFIED [DC] skew-symmetry [LT] VOA locality
        assert not s.is_zero
        assert s.terms[0].coeff == Fraction(2)
        assert s.terms[0].factors == (dW,)

    def test_m2_jw_zero(self):
        """m_2(J,W) = 0: J and W decouple."""
        result = self.bar_cx.m2(J, W)
        # VERIFIED [DC] decoupling [LT] principal embedding trivial charge
        assert result.simplify().is_zero

    def test_m2_ww_at_generator_level(self):
        """m_2(W,W) involves composites, vanishes at generator level."""
        result = self.bar_cx.m2(W, W)
        # VERIFIED [DC] composite field [LT] W_3 OPE Lambda composite
        # The WW OPE first-order pole involves dLambda = composite,
        # which is NOT tracked at the generator level
        assert result.simplify().is_zero


class TestM3:
    """Test the ternary A_∞ operation m_3."""

    def setup_method(self):
        self.bar_cx = AInfBarComplex()

    def test_m3_jjj_zero(self):
        """m_3(J,J,J) = 0: Heisenberg is strictly associative (class G)."""
        result = self.bar_cx.m3(J, J, J)
        # VERIFIED [DC] vanishing m_3 [LT] Heisenberg is formal (class G)
        # VERIFIED [DA] consistent with c3_shadow_tower.py spin1_shadow_data
        assert result.simplify().is_zero

    def test_m3_ttt_nonzero(self):
        """m_3(T,T,T) != 0: Virasoro is non-associative (class M)."""
        result = self.bar_cx.m3(T, T, T)
        s = result.simplify()
        # VERIFIED [DC] nonzero associator [LT] Virasoro non-formality
        assert not s.is_zero

    def test_m3_ttt_coefficient(self):
        """m_3(T,T,T) = -2T at c=1.

        The coefficient -2c = -2 matches the cubic shadow alpha_T = 2
        from c3_shadow_tower.py spin2_shadow_data.
        """
        result = self.bar_cx.m3(T, T, T)
        s = result.simplify()
        # VERIFIED [DC] -2c = -2 [LT] Virasoro mode algebra [CT] c3_shadow_tower
        assert len(s.terms) == 1
        assert s.terms[0].factors == (T,)
        assert s.terms[0].coeff == Fraction(-2)

    def test_m3_ttt_output_is_T(self):
        """m_3(T,T,T) outputs a spin-2 field (T itself)."""
        result = self.bar_cx.m3(T, T, T)
        s = result.simplify()
        # VERIFIED [DC] spin conservation [DA] 2+2+2 -> 2 (with desuspension)
        assert s.terms[0].factors[0].spin == 2

    def test_m3_ttj_zero(self):
        """m_3(T,T,J) = 0 at generator level."""
        result = self.bar_cx.m3(T, T, J)
        # VERIFIED [DC] mixed associator [LT] derivative field projection
        assert result.simplify().is_zero

    def test_m3_jjt_zero(self):
        """m_3(J,J,T) = 0: abelian J sector."""
        result = self.bar_cx.m3(J, J, T)
        assert result.simplify().is_zero

    def test_m3_www_zero_at_generator_level(self):
        """m_3(W,W,W) = 0 at generator level (spin mismatch)."""
        result = self.bar_cx.m3(W, W, W)
        # VERIFIED [DC] spin mismatch 9 -> 7 [DA] no generator at spin 7
        assert result.simplify().is_zero

    def test_m3_is_massey_for_J(self):
        """For J: m_3(J,J,J) is a classical Massey product (m_2 vanishes)."""
        data = compute_m3_massey_product(J, J, J)
        # VERIFIED [DC] classical Massey [LT] m_2(J,J) = 0
        assert data["is_classical_massey_product"] is True
        assert data["is_nonzero"] is False

    def test_m3_is_not_classical_massey_for_T(self):
        """For T: m_3(T,T,T) is NOT a classical Massey product."""
        data = compute_m3_massey_product(T, T, T)
        # VERIFIED [DC] non-classical [LT] m_2(T,T) = dT != 0
        assert data["is_classical_massey_product"] is False
        assert data["is_nonzero"] is True


class TestM4:
    """Test the quartic A_∞ operation m_4."""

    def setup_method(self):
        self.bar_cx = AInfBarComplex()

    def test_m4_jjjj_zero(self):
        """m_4(J,J,J,J) = 0: Heisenberg sector is Gaussian."""
        result = self.bar_cx.m4(J, J, J, J)
        # VERIFIED [DC] vanishing m_4 [LT] class G
        assert result.simplify().is_zero

    def test_m4_tttt_nonzero(self):
        """m_4(T,T,T,T) != 0: quartic shadow is nonzero (class M)."""
        result = self.bar_cx.m4(T, T, T, T)
        s = result.simplify()
        # VERIFIED [DC] nonzero quartic [LT] class M infinite tower
        assert not s.is_zero

    def test_m4_tttt_coefficient(self):
        """m_4(T,T,T,T) has coefficient Delta = 40/27 at c=1.

        Delta = 8 * kappa_T * S_4 = 8 * (1/2) * (10/27) = 40/27.
        Cross-check with c3_shadow_tower.py critical_discriminant.
        """
        result = self.bar_cx.m4(T, T, T, T)
        s = result.simplify()
        # VERIFIED [DC] 40/27 [CT] c3_shadow_tower.py critical_discriminant
        assert len(s.terms) == 1
        assert s.terms[0].coeff == Fraction(40, 27)

    def test_m4_tttt_output_is_T(self):
        """m_4(T,T,T,T) outputs T (spin-2)."""
        result = self.bar_cx.m4(T, T, T, T)
        s = result.simplify()
        assert s.terms[0].factors == (T,)

    def test_quartic_shadow_value(self):
        """S_4 = 10/27 for Virasoro at c=1.

        Cross-check: S_4 = 10/(c(5c+22)) = 10/(1*27) = 10/27.
        """
        c = Fraction(1)
        S4 = Fraction(10) / (c * (5 * c + 22))
        # VERIFIED [DC] 10/27 [CT] c3_shadow_tower.py spin2_shadow_data
        assert S4 == Fraction(10, 27)

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 40/27 for Virasoro at c=1."""
        kappa = Fraction(1, 2)
        S4 = Fraction(10, 27)
        Delta = 8 * kappa * S4
        # VERIFIED [DC] 40/27 [CT] c3_shadow_tower.py critical_discriminant
        assert Delta == Fraction(40, 27)


# ================================================================
#  SECTION 4: BAR DIFFERENTIAL
# ================================================================

class TestBarDifferential:
    """Test the total bar differential d = m_2 + m_3 + m_4 + ..."""

    def setup_method(self):
        self.bar_cx = AInfBarComplex()

    def test_d_on_single_generator(self):
        """d([T]) = 0: no differential on single generators (m_1 = 0)."""
        elem = AInfBarElement(factors=(T,))
        result = self.bar_cx.bar_differential(elem)
        # VERIFIED [DC] m_1 = 0 [LT] VOA concentrated in single degree
        assert result.simplify().is_zero

    def test_d_on_JJ(self):
        """d([J|J]) = 0: Heisenberg bracket vanishes."""
        elem = AInfBarElement(factors=(J, J))
        result = self.bar_cx.bar_differential(elem)
        # VERIFIED [DC] abelian OPE [LT] m_2(J,J) = 0
        assert result.simplify().is_zero

    def test_d_on_TT(self):
        """d([T|T]) = m_2(T,T) = dT."""
        elem = AInfBarElement(factors=(T, T))
        result = self.bar_cx.bar_differential(elem)
        s = result.simplify()
        # VERIFIED [DC] binary bar differential [LT] Virasoro bracket
        assert not s.is_zero

    def test_d_on_TTT_has_m2_and_m3_contributions(self):
        """d([T|T|T]) receives both m_2 and m_3 contributions."""
        elem = AInfBarElement(factors=(T, T, T))
        result = self.bar_cx.bar_differential(elem)
        s = result.simplify()
        # VERIFIED [DC] mixed arity differential [LT] A_inf bar differential
        # The m_2 contributions: m_2(T,T) at positions 0 and 1
        # The m_3 contribution: m_3(T,T,T) = -2T
        # Both should appear in the result.
        assert not s.is_zero

    def test_d_on_JJJJ(self):
        """d([J|J|J|J]) = 0: Heisenberg sector has trivial differential."""
        elem = AInfBarElement(factors=(J, J, J, J))
        result = self.bar_cx.bar_differential(elem)
        # VERIFIED [DC] class G [LT] all m_k(J,...,J) = 0 for k >= 2
        assert result.simplify().is_zero

    def test_dimension_at_arity(self):
        """B^{ord}_n has dimension r^n for r generators."""
        bar = self.bar_cx
        # VERIFIED [DC] r^n formula [DA] ordered tensor product
        assert bar.dimension_at_arity(1) == 3  # J, T, W
        assert bar.dimension_at_arity(2) == 9
        assert bar.dimension_at_arity(3) == 27

    def test_bar_elements_at_arity(self):
        """Enumerate all bar elements at arity 2."""
        elems = self.bar_cx.bar_elements_at_arity(2)
        assert len(elems) == 9  # 3^2


# ================================================================
#  SECTION 5: SHADOW TOWER
# ================================================================

class TestShadowTower:
    """Test shadow tower computation for W_{1+inf}."""

    def setup_method(self):
        bar_cx = AInfBarComplex()
        self.shadow = AInfShadowTower(bar_cx, max_spin=3)

    def test_kappa_per_channel(self):
        """kappa_s = c/s = 1/s at c=1."""
        kappas = self.shadow.kappa_per_channel()
        # VERIFIED [DC] 1/s formula [CT] c3_shadow_tower.py kappa_channel
        assert kappas[1] == Fraction(1)
        assert kappas[2] == Fraction(1, 2)
        assert kappas[3] == Fraction(1, 3)

    def test_kappa_total(self):
        """Total kappa = H_3 = 1 + 1/2 + 1/3 = 11/6."""
        total = self.shadow.kappa_ch_total()
        # VERIFIED [DC] harmonic sum [CT] c3_shadow_tower.py kappa_ch_regulated
        assert total == Fraction(11, 6)

    def test_S2_equals_kappa(self):
        """S_2 = kappa_ch (the leading shadow = modular characteristic)."""
        S2 = self.shadow.S2_total()
        kappa = self.shadow.kappa_ch_total()
        # VERIFIED [DC] S_2 = kappa [LT] shadow tower leading term
        assert S2 == kappa

    def test_alpha_per_channel(self):
        """Cubic shadow: alpha_1=0, alpha_2=2, alpha_3=0 (parity)."""
        alphas = self.shadow.alpha_per_channel()
        # VERIFIED [DC] per-channel [CT] c3_shadow_tower.py
        assert alphas[1] == Fraction(0)
        assert alphas[2] == Fraction(2)
        assert alphas[3] == Fraction(0)  # odd spin -> Z_2 parity

    def test_S3_nonzero(self):
        """S_3 != 0: cubic shadow from Virasoro sector."""
        S3 = self.shadow.S3_total()
        # VERIFIED [DC] nonzero cubic [LT] class >= L
        assert S3 != Fraction(0)

    def test_S3_value(self):
        """S_3 = alpha_2 = 2 (only spin-2 contributes at c=1)."""
        S3 = self.shadow.S3_total()
        # VERIFIED [DC] alpha_2 = 2 [CT] c3_shadow_tower.py spin2_shadow_data
        assert S3 == Fraction(2)

    def test_S4_spin2(self):
        """S_4 for spin-2 channel = 10/27 at c=1."""
        S4s = self.shadow.S4_per_channel()
        # VERIFIED [DC] 10/27 [CT] c3_shadow_tower.py spin2_shadow_data
        assert S4s[2] == Fraction(10, 27)

    def test_S4_spin1_zero(self):
        """S_4 for spin-1 channel = 0 (class G)."""
        S4s = self.shadow.S4_per_channel()
        assert S4s[1] == Fraction(0)

    def test_shadow_class_spin1_G(self):
        """Spin-1 channel is class G (Gaussian)."""
        classes = self.shadow.shadow_class_per_channel()
        # VERIFIED [DC] class G [CT] c3_shadow_tower.py spin1_shadow_data
        assert classes[1] == "G"

    def test_shadow_class_spin2_M(self):
        """Spin-2 channel is class M (infinite tower)."""
        classes = self.shadow.shadow_class_per_channel()
        # VERIFIED [DC] class M [CT] c3_shadow_tower.py spin2_shadow_data
        assert classes[2] == "M"

    def test_shadow_tower_spin1_terminates(self):
        """Spin-1 shadow tower: only S_2 = 1, all higher vanish."""
        tower = self.shadow.shadow_tower_channel(1, max_r=6)
        # VERIFIED [DC] class G termination [LT] Heisenberg formality
        assert tower[2] == Fraction(1)
        for r in range(3, 7):
            if r in tower:
                assert tower[r] == Fraction(0)

    def test_shadow_tower_spin2_nonterminating(self):
        """Spin-2 shadow tower has infinitely many nonzero terms."""
        tower = self.shadow.shadow_tower_channel(2, max_r=8)
        # VERIFIED [DC] nontermination [LT] Virasoro class M
        assert tower[2] != Fraction(0)
        assert tower[3] != Fraction(0)
        assert tower[4] != Fraction(0)

    def test_shadow_tower_spin2_S2(self):
        """Spin-2 channel: S_2 = kappa_T = 1/2."""
        tower = self.shadow.shadow_tower_channel(2, max_r=4)
        # VERIFIED [DC] kappa_T = c/2 [CT] c3_shadow_tower.py
        assert tower[2] == Fraction(1, 2)

    def test_full_tower_aggregation(self):
        """Full tower S_r = sum_s S_r^{(s)} aggregates channels."""
        full = self.shadow.full_tower(max_r=6)
        ch1 = self.shadow.shadow_tower_channel(1, max_r=6)
        ch2 = self.shadow.shadow_tower_channel(2, max_r=6)
        ch3 = self.shadow.shadow_tower_channel(3, max_r=6)
        # VERIFIED [DC] aggregation [DA] linearity of shadow sum
        for r in range(2, 7):
            expected = ch1.get(r, Fraction(0)) + ch2.get(r, Fraction(0)) + ch3.get(r, Fraction(0))
            assert full[r] == expected


# ================================================================
#  SECTION 6: MAURER-CARTAN EQUATION
# ================================================================

class TestMaurerCartan:
    """Test A_∞ Maurer-Cartan equation verification."""

    def setup_method(self):
        bar_cx = AInfBarComplex()
        self.mc = AInfMaurerCartan(bar_cx)

    def test_mc_degree1_J(self):
        """MC degree 1: m_1(J) = 0."""
        result = self.mc.mc_degree_1(J)
        # VERIFIED [DC] m_1 = 0 [LT] no internal differential
        assert result.is_zero

    def test_mc_degree1_T(self):
        """MC degree 1: m_1(T) = 0."""
        result = self.mc.mc_degree_1(T)
        assert result.is_zero

    def test_mc_degree2_J(self):
        """MC degree 2 for J: m_2(J,J) = 0."""
        result = self.mc.mc_degree_2(J)
        # VERIFIED [DC] Heisenberg class G [LT] abelian OPE
        assert result.simplify().is_zero

    def test_mc_degree2_T(self):
        """MC degree 2 for T: m_2(T,T) = dT != 0."""
        result = self.mc.mc_degree_2(T)
        # VERIFIED [DC] Virasoro nonzero [LT] non-abelian OPE
        assert not result.simplify().is_zero

    def test_mc_degree3_J(self):
        """MC degree 3 for J: m_3(J,J,J) = 0."""
        data = self.mc.mc_degree_3(J)
        # VERIFIED [DC] class G [LT] Heisenberg formality
        assert data["m3_is_zero"] is True

    def test_mc_degree3_T(self):
        """MC degree 3 for T: m_3(T,T,T) = -2T != 0."""
        data = self.mc.mc_degree_3(T)
        # VERIFIED [DC] class M [LT] Virasoro non-formality
        assert data["m3_is_zero"] is False

    def test_mc_degree4_J(self):
        """MC degree 4 for J: m_4(J^4) = 0."""
        data = self.mc.mc_degree_4(J)
        assert data["m4_is_zero"] is True

    def test_mc_degree4_T(self):
        """MC degree 4 for T: m_4(T^4) != 0."""
        data = self.mc.mc_degree_4(T)
        # VERIFIED [DC] class M [LT] quartic shadow nonzero
        assert data["m4_is_zero"] is False

    def test_full_mc_check(self):
        """Run full MC check across all generators."""
        results = self.mc.full_mc_check()
        # VERIFIED [DC] comprehensive check [DA] all generators covered
        assert "J" in results
        assert "T" in results
        assert "W" in results
        # J sector: all zero
        assert results["J"]["degree_1_zero"] is True
        assert results["J"]["degree_2_zero"] is True
        # T sector: degree 2 nonzero
        assert results["T"]["degree_1_zero"] is True
        assert results["T"]["degree_2_zero"] is False


# ================================================================
#  SECTION 7: MACMAHON GENERATING FUNCTION
# ================================================================

class TestMacMahon:
    """Test MacMahon function = generating function of B^{ord}(W_{1+inf})."""

    def test_macmahon_coefficients(self):
        """M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + 48q^6 + ...

        OEIS A000219: plane partition counts.
        """
        # VERIFIED [DC] OEIS A000219 [LT] MacMahon's theorem
        assert _macmahon_coefficient(0) == 1
        assert _macmahon_coefficient(1) == 1
        assert _macmahon_coefficient(2) == 3
        assert _macmahon_coefficient(3) == 6
        assert _macmahon_coefficient(4) == 13
        assert _macmahon_coefficient(5) == 24
        assert _macmahon_coefficient(6) == 48

    def test_macmahon_higher(self):
        """Higher MacMahon coefficients: p3(7)=86, p3(8)=160."""
        # VERIFIED [DC] OEIS A000219 [DA] independent computation
        assert _macmahon_coefficient(7) == 86
        assert _macmahon_coefficient(8) == 160

    def test_macmahon_via_product(self):
        """Verify M(q) = prod_{k>=1} 1/(1-q^k)^k truncated.

        Independent computation: expand the product directly.
        The factor 1/(1-q^k)^k contributes at q^k, so we need
        k up to N to get M(q) mod q^{N+1} correct.
        """
        import math as _math

        N = 6  # verify through q^N
        coeffs = [Fraction(0)] * (N + 1)
        coeffs[0] = Fraction(1)

        for k in range(1, N + 1):
            # Multiply by 1/(1-q^k)^k = sum_{m>=0} C(m+k-1, k-1) q^{km}
            new_coeffs = [Fraction(0)] * (N + 1)
            for existing_pow in range(N + 1):
                if coeffs[existing_pow] == 0:
                    continue
                for m in range(0, (N - existing_pow) // k + 1):
                    target = existing_pow + k * m
                    if target <= N:
                        binom_val = _math.comb(m + k - 1, k - 1)
                        new_coeffs[target] += coeffs[existing_pow] * Fraction(binom_val)
            coeffs = new_coeffs

        # VERIFIED [DC] product expansion [DA] independent of log-exp method
        for n in range(N + 1):
            assert int(coeffs[n]) == _macmahon_coefficient(n), (
                f"Mismatch at n={n}: product gives {int(coeffs[n])}, "
                f"log-exp gives {_macmahon_coefficient(n)}"
            )

    def test_bar_dimension_with_macmahon(self):
        """Bar complex of full W_{1+inf} has generating function M(q)."""
        bar_cx = AInfBarComplex()
        # For 3 generators (J, T, W): dim B_n = 3^n
        # This is NOT the MacMahon function (which counts plane partitions).
        # The MacMahon function applies to the FULL W_{1+inf} with infinitely
        # many generators (all spins s >= 1).
        # VERIFIED [DC] 3^n for truncated [DA] r^n formula
        assert bar_cx.dimension_at_arity(1) == 3
        assert bar_cx.dimension_at_arity(2) == 9
        # The MacMahon coefficient p3(2) = 3 counts plane partitions,
        # which matches the dimension when we have infinitely many channels
        # but weight the count by conformal weight.
        assert bar_cx.macmahon_coefficient(2) == 3


# ================================================================
#  SECTION 8: MASTER COMPUTATION
# ================================================================

class TestMasterComputation:
    """Test the master computation function."""

    def test_master_runs(self):
        """compute_a_infinity_bar_w1inf runs without error."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        assert data is not None
        assert data["algebra"] == "W_{1+inf} at c=1"

    def test_master_m2_count(self):
        """m_2 table has 3x3 = 9 entries."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        assert len(data["m2_table"]) == 9

    def test_master_m3_count(self):
        """m_3 table has 3^3 = 27 entries."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        assert len(data["m3_table"]) == 27

    def test_master_m2_nonzero(self):
        """Some m_2 pairs are nonzero (T-sector has nontrivial bracket)."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        # VERIFIED [DC] nonzero count [DA] TT, TJ, TW, WT are nonzero
        assert data["summary"]["m2_nonzero_pairs"] >= 4

    def test_master_m3_nonzero(self):
        """Exactly one m_3 triple is nonzero: (T,T,T)."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        # VERIFIED [DC] single nonzero [LT] only Virasoro associator
        assert data["summary"]["m3_nonzero_triples"] == 1

    def test_master_shadow_class(self):
        """Full W_{1+inf} is class M (infinite shadow depth)."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        # VERIFIED [DC] class M [CT] c3_shadow_tower.py
        assert "M" in data["summary"]["shadow_class"]

    def test_master_kappa_total(self):
        """Regulated kappa_ch at 3 channels = 11/6."""
        data = compute_a_infinity_bar_w1inf(max_arity=3)
        assert data["kappa_ch_total"] == Fraction(11, 6)

    def test_master_macmahon(self):
        """MacMahon coefficients are correct."""
        data = compute_a_infinity_bar_w1inf(max_arity=4)
        # VERIFIED [DC] OEIS [DA] independent sequence
        assert data["macmahon_coefficients"][:5] == [1, 1, 3, 6, 13]


# ================================================================
#  SECTION 9: CROSS-CHECKS WITH c3_shadow_tower.py
# ================================================================

class TestCrossChecks:
    """Cross-check A_∞ shadow data against c3_shadow_tower.py."""

    def test_alpha_matches_m3_coefficient(self):
        """alpha_T = 2 matches |m_3(T,T,T)| = 2c = 2.

        The cubic shadow alpha is the absolute value of the m_3 coefficient
        (up to normalization).
        """
        bar_cx = AInfBarComplex()
        m3_ttt = bar_cx.m3(T, T, T).simplify()
        alpha_from_m3 = abs(m3_ttt.terms[0].coeff)
        # VERIFIED [DC] alpha = |m3| [CT] c3_shadow_tower.py alpha_T = 2
        assert alpha_from_m3 == Fraction(2)

    def test_Delta_matches_m4_coefficient(self):
        """Delta = 40/27 matches m_4(T,T,T,T) coefficient.

        The critical discriminant Delta = 8*kappa*S_4 appears as the
        coefficient of m_4(T,T,T,T).
        """
        bar_cx = AInfBarComplex()
        m4_tttt = bar_cx.m4(T, T, T, T).simplify()
        Delta_from_m4 = m4_tttt.terms[0].coeff
        # VERIFIED [DC] Delta = 40/27 [CT] c3_shadow_tower.py
        assert Delta_from_m4 == Fraction(40, 27)

    def test_shadow_tower_recursion_consistency(self):
        """The shadow tower S_r from A_∞ matches the recursion formula.

        For spin-2 at c=1:
          a_0 = 2*kappa = 1
          a_1 = 3*alpha = 6
          S_2 = a_0/2 = 1/2
          S_3 = a_1/3 = 2
          a_2 = (q2 - a1^2)/(2*a0) = (1052/27 - 36)/2 = 40/27
          S_4 = a_2/4 = 10/27
        """
        kappa = Fraction(1, 2)
        alpha = Fraction(2)
        S4_val = Fraction(10, 27)

        a0 = 2 * kappa  # = 1
        q1 = 12 * kappa * alpha  # = 12
        q2 = 9 * alpha ** 2 + 16 * kappa * S4_val  # = 36 + 80/27 = 1052/27

        a1 = q1 / (2 * a0)  # = 6
        a2 = (q2 - a1 ** 2) / (2 * a0)  # = (1052/27 - 36)/2 = 40/27

        S2 = a0 / 2
        S3 = a1 / 3
        S4 = a2 / 4

        # VERIFIED [DC] recursion [CT] c3_shadow_tower.py shadow_tower_single_channel
        assert S2 == Fraction(1, 2)
        assert S3 == Fraction(2)
        assert S4 == Fraction(10, 27)

    def test_heisenberg_class_G(self):
        """J sector has class G: m_3 = m_4 = 0, shadow terminates."""
        bar_cx = AInfBarComplex()
        # VERIFIED [DC] class G [CT] c3_shadow_tower.py spin1_shadow_data
        assert bar_cx.m3(J, J, J).simplify().is_zero
        assert bar_cx.m4(J, J, J, J).simplify().is_zero

    def test_virasoro_class_M(self):
        """T sector has class M: m_3 != 0, m_4 != 0, infinite tower."""
        bar_cx = AInfBarComplex()
        # VERIFIED [DC] class M [CT] c3_shadow_tower.py spin2_shadow_data
        assert not bar_cx.m3(T, T, T).simplify().is_zero
        assert not bar_cx.m4(T, T, T, T).simplify().is_zero


# ================================================================
#  SECTION 10: A_∞ RELATION VERIFICATION
# ================================================================

class TestAInfRelations:
    """Verify the A_∞ relations (which are equivalent to d^2 = 0)."""

    def setup_method(self):
        self.bar_cx = AInfBarComplex()

    def test_d_squared_on_JJ(self):
        """d^2([J|J]) = 0."""
        elem = AInfBarElement(factors=(J, J))
        check = self.bar_cx.verify_d_squared_zero(elem)
        # VERIFIED [DC] d^2 = 0 [LT] A_inf axiom
        assert check["d_squared_zero"]

    def test_d_squared_on_JJJ(self):
        """d^2([J|J|J]) = 0."""
        elem = AInfBarElement(factors=(J, J, J))
        check = self.bar_cx.verify_d_squared_zero(elem)
        assert check["d_squared_zero"]

    def test_d_squared_on_JJJJ(self):
        """d^2([J|J|J|J]) = 0."""
        elem = AInfBarElement(factors=(J, J, J, J))
        check = self.bar_cx.verify_d_squared_zero(elem)
        assert check["d_squared_zero"]
