r"""Tests for the E_3 bar spectral sequence of the Virasoro at c=1 (class M).

THE ALTERNATIVE ROUTE TO delta^{(3)}(T_0): instead of the contracting
homotopy, use the d_4 differential on the E_3 page of the bar spectral
sequence.

Key result:
  delta^{(3)}(T_0) = d_4(omega_3) = 40/27

Mathematical facts:
  - Virasoro at c=1 is class M (infinite shadow depth)
  - Shadow data: kappa_ch = 1/2, alpha = 2, S_4 = 10/27
  - Critical discriminant: Delta = 8*kappa_ch*S_4 = 40/27
  - E_3 page = (1+t)^3 = [1, 3, 3, 1]  (SAME as class L Yangian)
  - d_4: Lambda^3 -> Lambda^0 is a nonzero scalar = Delta = 40/27
  - E_4 = E_inf = [0, 3, 3, 0]  (DIFFERENT from class L [1, 3, 3, 1])

Comparison across shadow classes:
  Class G (Heisenberg): S_4 = 0, d_4 = 0, E_inf = P(q)^3 (formal)
  Class L (Yangian):    S_4 = 0, d_4 = 0, E_inf = (1+t)^3 = [1,3,3,1]
  Class C (betagamma):  S_4 != 0, d_4 = 0 (charge conservation), E_inf = (1+t)^6
  Class M (Virasoro):   S_4 = 10/27, d_4 != 0, E_inf = [0,3,3,0]

The class M case is the ONLY case where d_4 acts nontrivially on the
E_3 page (for a single-generator algebra). This gives delta^{(3)}(T_0)
directly as the d_4 coefficient.

Manuscript references:
  a_infinity_bar_w1inf.py: S_4 = 10/27, m_4(T,T,T,T) = (40/27)T
  c3_shadow_tower.py: spin-2 shadow data (class M)
  holomorphic_cs_chiral_engine.py: E3BarSpectralSequenceVirasoro class
  Vol I: bar_cobar_adjunction_curved.tex (spectral sequence framework)
"""

from fractions import Fraction
from math import comb

import pytest
from sympy import Rational

from compute.lib.holomorphic_cs_chiral_engine import (
    E3BarComplexYangian,
    E3BarSpectralSequenceVirasoro,
    OmegaBackground,
    _partition_count,
)


# =========================================================================
# Ground truth
# =========================================================================

# Chain-level: P(q)^3 = tau_3(n) (same across all classes with 1 gen/direction)
TAU_3_GROUND_TRUTH = [1, 3, 9, 22, 51, 108, 221, 429]

# E_3 page: (1+t)^3 (same for class L and class M through E_3)
E3_PAGE_GROUND_TRUTH = [1, 3, 3, 1, 0, 0, 0, 0]

# E_4 = E_inf for class M: d_4 kills Lambda^0 and Lambda^3
E4_PAGE_GROUND_TRUTH = [0, 3, 3, 0, 0, 0, 0, 0]

# Shadow data at c=1
KAPPA_CH = Rational(1, 2)
ALPHA = Rational(2)
S4 = Rational(10, 27)
DELTA = Rational(40, 27)  # = 8 * kappa_ch * S_4


# =========================================================================
# 1. Shadow classification: class M, infinite depth
# =========================================================================

class TestVirasoroClassification:
    """Virasoro at c=1 is class M with infinite shadow depth."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro(c=Rational(1))

    def test_shadow_class(self):
        """Class M (infinite tower)."""
        # VERIFIED [DC] class M [LT] c3_shadow_tower spin-2 data
        assert self.vir.shadow_class == "M"

    def test_shadow_depth_infinite(self):
        """Shadow depth is infinite for class M."""
        # VERIFIED [DC] infinite depth [DA] Delta != 0 implies non-termination
        assert self.vir.shadow_depth == "infinite"

    def test_kappa_ch(self):
        """kappa_ch = c/2 = 1/2 at c=1 (AP113: subscripted)."""
        # VERIFIED [DC] kappa_ch formula [LT] spin-2 channel: k_s = c/s
        assert self.vir.kappa_ch == KAPPA_CH

    def test_alpha(self):
        """Cubic shadow alpha = 2 from m_3(T,T,T) = -2T."""
        # VERIFIED [DC] alpha = 2 [LT] a_infinity_bar_w1inf.py m_3(T,T,T)
        assert self.vir.alpha == ALPHA

    def test_S4(self):
        """Quartic shadow S_4 = 10/(c(5c+22)) = 10/27 at c=1."""
        # VERIFIED [DC] S_4 formula [LT] c3_shadow_tower.py spin2_shadow_data
        assert self.vir.S4 == S4

    def test_S4_is_10_over_27(self):
        """S_4 = 10/27 (the key number)."""
        # VERIFIED [DC] exact value [DA] 10/(1*(5+22)) = 10/27
        assert self.vir.S4 == Rational(10, 27)

    def test_critical_discriminant(self):
        """Delta = 8*kappa_ch*S_4 = 40/27."""
        # VERIFIED [DC] Delta formula [DA] 8*(1/2)*(10/27) = 40/27
        assert self.vir.Delta == DELTA

    def test_critical_discriminant_value(self):
        """Delta = 40/27 (matches a_infinity_bar_w1inf.py m_4 coefficient)."""
        # VERIFIED [DC] exact value [LT] m_4(T,T,T,T) = (40/27)*T
        assert self.vir.Delta == Rational(40, 27)

    def test_num_generators(self):
        """1 generator (T) per E_3 direction."""
        assert self.vir.num_generators == 1


# =========================================================================
# 2. Chain-level dimensions: P(q)^3 = tau_3(n) (same as Yangian)
# =========================================================================

class TestChainDimensions:
    """Chain level is P(q)^3, identical across classes G/L/M for 1 gen."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()

    @pytest.mark.parametrize("n", range(8))
    def test_chain_matches_tau3(self, n):
        """Chain dims match tripartition counts."""
        # VERIFIED [DC] tau_3(n) [LT] OEIS A000716
        assert self.vir.chain_dimension(n) == TAU_3_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_chain_matches_yangian(self, n):
        """Chain dims match Yangian (same generators, different differentials)."""
        # VERIFIED [DC] Virasoro chain [DA] Yangian chain (both P(q)^3)
        omega = OmegaBackground(1, 2)
        yangian = E3BarComplexYangian(omega)
        assert self.vir.chain_dimension(n) == yangian.chain_dimension(n)


# =========================================================================
# 3. E_3 page: (1+t)^3 = [1, 3, 3, 1] (same as Yangian through E_3)
# =========================================================================

class TestE3Page:
    """E_3 page is Lambda^*(k^3), identical to class L through this page."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()

    @pytest.mark.parametrize("n", range(8))
    def test_e3_matches_binomial(self, n):
        """E_3^n = C(3,n) for 0 <= n <= 3, else 0."""
        expected = comb(3, n) if 0 <= n <= 3 else 0
        # VERIFIED [DC] binomial [DA] Lambda^n(k^3) dimension
        assert self.vir.e3_page(n) == expected

    @pytest.mark.parametrize("n", range(8))
    def test_e3_matches_ground_truth(self, n):
        """E_3 page matches ground truth [1, 3, 3, 1, 0, ...]."""
        assert self.vir.e3_page(n) == E3_PAGE_GROUND_TRUTH[n]

    def test_e3_poincare(self):
        """Poincare polynomial (1+t)^3 = [1, 3, 3, 1]."""
        # VERIFIED [DC] (1+t)^3 expansion [DA] binomial theorem
        assert self.vir.e3_poincare() == [1, 3, 3, 1]

    def test_e3_matches_yangian(self):
        """E_3 page matches Yangian E_inf (they agree through E_3)."""
        omega = OmegaBackground(1, 2)
        yangian = E3BarComplexYangian(omega)
        # VERIFIED [DC] Virasoro E_3 = Yangian E_inf [DA] both (1+t)^3
        assert self.vir.e3_poincare() == yangian.cohomology_poincare()

    def test_e3_total_is_8(self):
        """Total E_3 dimension = 2^3 = 8."""
        assert sum(self.vir.e3_poincare()) == 8

    def test_e3_euler_char_zero(self):
        """Euler characteristic at E_3: 1 - 3 + 3 - 1 = 0."""
        poinc = self.vir.e3_poincare()
        chi = sum((-1)**n * poinc[n] for n in range(4))
        assert chi == 0


# =========================================================================
# 4. THE KEY COMPUTATION: d_4 on E_3 page
# =========================================================================

class TestD4Differential:
    """d_4 is nonzero on the E_3 page for class M (Virasoro)."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()

    def test_d4_is_nonzero(self):
        """d_4 != 0 for Virasoro (class M, S_4 = 10/27 != 0)."""
        # VERIFIED [DC] d_4 != 0 [DA] Delta = 40/27 != 0
        assert self.vir.d4_is_nonzero()

    def test_d4_coefficient_is_40_over_27(self):
        """d_4(omega_3) = 40/27 = 8 * (1/2) * (10/27)."""
        # VERIFIED [DC] d_4 coefficient [DA] Delta = 8*kappa_ch*S_4
        assert self.vir.d4_coefficient() == Rational(40, 27)

    def test_d4_coefficient_equals_delta(self):
        """d_4 coefficient = critical discriminant Delta."""
        # VERIFIED [DC] d_4 = Delta [LT] spectral sequence identification
        assert self.vir.d4_coefficient() == self.vir.Delta

    def test_d4_from_S4_and_kappa(self):
        """d_4 = 8 * kappa_ch * S_4 (the spectral sequence formula)."""
        # VERIFIED [DC] formula [DA] 8 * (1/2) * (10/27) = 40/27
        expected = 8 * self.vir.kappa_ch * self.vir.S4
        assert self.vir.d4_coefficient() == expected

    def test_d4_matches_m4_coefficient(self):
        """d_4 coefficient matches m_4(T,T,T,T) from a_infinity_bar_w1inf.py.

        m_4(T,T,T,T) = Delta * T = (40/27) * T.
        The spectral sequence extracts the same coefficient.
        """
        # VERIFIED [DC] spectral sequence [DA] a_infinity_bar_w1inf m_4
        from compute.lib.a_infinity_bar_w1inf import (
            AInfBarComplex,
            T,
        )
        bar_cx = AInfBarComplex()
        m4_result = bar_cx.m4(T, T, T, T)
        m4_simplified = m4_result.simplify()
        # m_4(T,T,T,T) should have a single T-valued term with coefficient Delta
        assert len(m4_simplified.terms) == 1
        assert m4_simplified.terms[0].factors == (T,)
        assert m4_simplified.terms[0].coeff == Fraction(40, 27)
        # This matches d_4 from the spectral sequence
        assert Rational(m4_simplified.terms[0].coeff.numerator,
                        m4_simplified.terms[0].coeff.denominator) == self.vir.d4_coefficient()

    def test_no_charge_conservation(self):
        """Virasoro has no charge grading to block d_4."""
        # VERIFIED [DC] no charge conservation [DA] single self-conjugate gen T
        assert not self.vir.charge_conservation_blocks_d4()


# =========================================================================
# 5. delta^{(3)}(T_0) = 40/27 (the main result)
# =========================================================================

class TestDelta3T0:
    """delta^{(3)}(T_0) = d_4(omega_3) = 40/27."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()

    def test_delta_3_T0_value(self):
        """delta^{(3)}(T_0) = 40/27."""
        # VERIFIED [DC] delta^(3) value [DA] 8 * (1/2) * (10/27) = 40/27
        assert self.vir.delta_3_T0() == Rational(40, 27)

    def test_delta_3_T0_equals_d4_coefficient(self):
        """delta^{(3)}(T_0) = d_4(omega_3) (the spectral sequence route)."""
        # VERIFIED [DC] identification [LT] spectral sequence => d_4 = delta^(3)
        assert self.vir.delta_3_T0() == self.vir.d4_coefficient()

    def test_delta_3_T0_equals_critical_discriminant(self):
        """delta^{(3)}(T_0) = Delta = 8*kappa_ch*S_4."""
        # VERIFIED [DC] identification [LT] shadow tower critical discriminant
        assert self.vir.delta_3_T0() == self.vir.Delta

    def test_delta_3_T0_factorization(self):
        """delta^{(3)}(T_0) = 8 * kappa_ch * S_4 factors correctly.

        8 * (1/2) * (10/27) = 4 * 10/27 = 40/27.
        """
        # VERIFIED [DC] factorization [DA] arithmetic
        assert 8 * Rational(1, 2) * Rational(10, 27) == Rational(40, 27)

    def test_delta_3_T0_consistency_with_S4(self):
        """S_4 = 10/27 is recovered from delta^{(3)}(T_0) via the inverse.

        S_4 = delta^{(3)}(T_0) / (8 * kappa_ch) = (40/27) / (8 * 1/2) = 10/27.
        """
        # VERIFIED [DC] inverse [DA] (40/27) / 4 = 10/27
        recovered_S4 = self.vir.delta_3_T0() / (8 * self.vir.kappa_ch)
        assert recovered_S4 == Rational(10, 27)


# =========================================================================
# 6. E_4 = E_inf page: [0, 3, 3, 0]
# =========================================================================

class TestE4Page:
    """E_4 = E_inf = [0, 3, 3, 0] after d_4 kills Lambda^0 and Lambda^3."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()

    @pytest.mark.parametrize("n", range(8))
    def test_e4_matches_ground_truth(self, n):
        """E_4 page matches [0, 3, 3, 0, 0, ...]."""
        # VERIFIED [DC] E_4 dimensions [DA] d_4 kills Lambda^{0,3}
        assert self.vir.e4_page(n) == E4_PAGE_GROUND_TRUTH[n]

    def test_e4_poincare(self):
        """E_4 Poincare polynomial = [0, 3, 3, 0]."""
        assert self.vir.e4_poincare() == [0, 3, 3, 0]

    def test_einf_equals_e4(self):
        """E_inf = E_4 (higher d_r vanish for degree reasons)."""
        # VERIFIED [DC] E_inf = E_4 [DA] d_r for r>=5 maps to negative degree
        assert self.vir.einf_poincare() == self.vir.e4_poincare()

    def test_cohomology_total_is_6(self):
        """Total dimension = 6 (was 8 at E_3, lost 2 from d_4)."""
        # VERIFIED [DC] dim = 6 [DA] 0 + 3 + 3 + 0 = 6
        assert self.vir.cohomology_total() == 6

    def test_deficit_from_class_L_is_2(self):
        """Deficit from class L: 8 - 6 = 2 (d_4 kills 2 dimensions)."""
        # VERIFIED [DC] deficit = 2 [DA] dim(Lambda^0) + dim(Lambda^3) = 1+1 = 2
        comparison = self.vir.compare_with_class_L()
        assert comparison["deficit_total"] == 2

    def test_euler_characteristic_preserved(self):
        """chi(E_4) = 0 = chi(E_3) (Euler char preserved by d_4)."""
        # VERIFIED [DC] chi preserved [LT] spectral sequence property
        assert self.vir.euler_characteristic() == 0

    def test_euler_char_e3_equals_e4(self):
        """Euler characteristic is same at E_3 and E_4."""
        e3_chi = sum((-1)**n * self.vir.e3_page(n) for n in range(4))
        e4_chi = self.vir.euler_characteristic()
        # VERIFIED [DC] chi invariance [DA] 1-3+3-1 = 0 = 0-3+3-0
        assert e3_chi == e4_chi == 0

    def test_poincare_duality_preserved(self):
        """Poincare duality h_k = h_{3-k} is preserved by d_4.

        E_3: [1, 3, 3, 1] symmetric
        E_4: [0, 3, 3, 0] symmetric
        """
        poinc = self.vir.e4_poincare()
        # VERIFIED [DC] symmetry [DA] [0,3,3,0] reversed = [0,3,3,0]
        assert poinc[0] == poinc[3]
        assert poinc[1] == poinc[2]


# =========================================================================
# 7. Spectral sequence page-by-page verification
# =========================================================================

class TestSpectralSequence:
    """Full spectral sequence: E_0 -> E_3 -> E_4 = E_inf."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()
        self.ss = self.vir.verify_spectral_sequence(7)

    @pytest.mark.parametrize("n", range(8))
    def test_e0_is_chain(self, n):
        """E_0 page = P(q)^3."""
        assert self.ss[n]["E_0 (chain)"] == TAU_3_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_e3_is_binomial(self, n):
        """E_3 page = C(3, n)."""
        assert self.ss[n]["E_3 (after d_1,d_2,d_3)"] == E3_PAGE_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_e4_is_final(self, n):
        """E_4 = E_inf = [0, 3, 3, 0, 0, ...]."""
        assert self.ss[n]["E_4 = E_inf (after d_4)"] == E4_PAGE_GROUND_TRUTH[n]

    def test_d4_acted_on_degree_0_and_3(self):
        """d_4 changed dimensions at degrees 0 and 3 only."""
        assert self.ss[0]["d4_acted"] is True   # 1 -> 0
        assert self.ss[1]["d4_acted"] is False  # 3 -> 3
        assert self.ss[2]["d4_acted"] is False  # 3 -> 3
        assert self.ss[3]["d4_acted"] is True   # 1 -> 0

    def test_monotone_decrease_across_pages(self):
        """Dimensions decrease (or stay) at each spectral sequence page."""
        for n in range(8):
            e0 = self.ss[n]["E_0 (chain)"]
            e3 = self.ss[n]["E_3 (after d_1,d_2,d_3)"]
            e4 = self.ss[n]["E_4 = E_inf (after d_4)"]
            assert e0 >= e3 >= e4 >= 0


# =========================================================================
# 8. Comparison with class L (Yangian) and class C (betagamma)
# =========================================================================

class TestClassComparison:
    """Virasoro (M) vs Yangian (L): diverge at E_4."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()
        omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(omega)

    def test_e3_pages_agree(self):
        """Virasoro and Yangian have the same E_3 page."""
        # VERIFIED [DC] E_3 agreement [DA] both (1+t)^3
        vir_e3 = self.vir.e3_poincare()
        yang_e3 = self.yangian.cohomology_poincare()
        assert vir_e3 == yang_e3 == [1, 3, 3, 1]

    def test_einf_pages_differ(self):
        """Virasoro and Yangian have DIFFERENT E_inf pages."""
        # VERIFIED [DC] E_inf divergence [DA] d_4 nonzero for M, zero for L
        vir_einf = self.vir.einf_poincare()
        yang_einf = self.yangian.cohomology_poincare()
        assert vir_einf != yang_einf
        assert vir_einf == [0, 3, 3, 0]
        assert yang_einf == [1, 3, 3, 1]

    def test_class_L_has_S4_zero(self):
        """Yangian (class L) has S_4 = 0, so d_4 = 0."""
        # VERIFIED [DC] S_4 = 0 for class L [LT] c3_shadow_tower.py
        assert self.yangian.shadow_class == "L"

    def test_class_M_has_S4_nonzero(self):
        """Virasoro (class M) has S_4 = 10/27 != 0."""
        # VERIFIED [DC] S_4 != 0 for class M [LT] c3_shadow_tower.py
        assert self.vir.S4 != 0
        assert self.vir.shadow_class == "M"

    def test_dimension_deficit(self):
        """Class M E_inf dimension is 2 less than class L."""
        # VERIFIED [DC] deficit = 2 [DA] 8 - 6 = 2
        assert self.yangian.cohomology_total() - self.vir.cohomology_total() == 2


# =========================================================================
# 9. Central charge dependence of d_4
# =========================================================================

class TestCentralChargeDependence:
    """d_4 coefficient as a function of central charge c."""

    def test_d4_at_c_equals_1(self):
        """At c=1: d_4 = 40/27."""
        vir = E3BarSpectralSequenceVirasoro(c=Rational(1))
        assert vir.d4_coefficient() == Rational(40, 27)

    def test_d4_at_c_equals_2(self):
        """At c=2: S_4 = 10/(2*(10+22)) = 10/64 = 5/32.
        kappa_ch = 1, Delta = 8*1*(5/32) = 5/4.
        """
        vir = E3BarSpectralSequenceVirasoro(c=Rational(2))
        assert vir.kappa_ch == Rational(1)
        assert vir.S4 == Rational(10, 64)
        assert vir.Delta == 8 * Rational(1) * Rational(10, 64)
        assert vir.d4_coefficient() == Rational(5, 4)

    def test_d4_at_c_equals_minus_2(self):
        """At c=-2 (betagamma central charge): S_4 = 10/((-2)*(-10+22))
        = 10/(-2*12) = 10/(-24) = -5/12.
        kappa_ch = -1, Delta = 8*(-1)*(-5/12) = 40/12 = 10/3.

        Note: for betagamma, charge conservation kills d_4 on the E_3
        page despite Delta != 0. But the VIRASORO at c=-2 (a different
        algebra!) has no charge conservation.
        """
        vir = E3BarSpectralSequenceVirasoro(c=Rational(-2))
        assert vir.kappa_ch == Rational(-1)
        assert vir.S4 == Rational(-5, 12)
        assert vir.d4_coefficient() == Rational(10, 3)

    def test_d4_vanishes_iff_c_zero(self):
        """d_4 = 0 iff c = 0 (trivial Virasoro).

        Delta = 8*(c/2)*10/(c*(5c+22)) = 40/(5c+22).
        This vanishes only if the numerator vanishes, which never happens.
        So d_4 != 0 for ALL nonzero c.

        At c=0: kappa_ch = 0, so Delta = 0 trivially.
        """
        # Nonzero c: d_4 != 0
        for c_val in [1, 2, -2, -22, Rational(1, 3)]:
            vir = E3BarSpectralSequenceVirasoro(c=Rational(c_val))
            if c_val != 0:
                assert vir.d4_is_nonzero(), f"d_4 should be nonzero at c={c_val}"

    def test_delta_formula_simplification(self):
        """Delta = 8*(c/2)*10/(c*(5c+22)) = 40/(5c+22).

        The c in kappa_ch = c/2 cancels the c in the denominator of S_4.
        """
        # VERIFIED [DC] simplification [DA] algebra
        for c_val in [1, 2, 3, 5, 7]:
            vir = E3BarSpectralSequenceVirasoro(c=Rational(c_val))
            expected = Rational(40, 5 * c_val + 22)
            assert vir.Delta == expected, f"Delta mismatch at c={c_val}"


# =========================================================================
# 10. Full investigation and self-consistency
# =========================================================================

class TestFullInvestigation:
    """Self-consistency of the full investigation output."""

    def setup_method(self):
        self.vir = E3BarSpectralSequenceVirasoro()
        self.data = self.vir.full_investigation()

    def test_key_result_contains_40_27(self):
        """The key result string mentions 40/27."""
        assert "40/27" in self.data["key_result"]

    def test_delta_3_T0_in_output(self):
        """delta^{(3)}(T_0) is in the output."""
        assert self.data["delta_3_T0"] == Rational(40, 27)

    def test_internal_consistency(self):
        """All representations of d_4 agree."""
        assert self.data["d4_coefficient"] == self.data["delta_3_T0"]
        assert self.data["d4_coefficient"] == self.data["Delta"]
        assert self.data["d4_is_nonzero"] is True

    def test_euler_char_preserved(self):
        """Euler characteristic is 0 at all pages."""
        assert self.data["euler_characteristic"] == 0

    def test_einf_is_0330(self):
        """E_inf = [0, 3, 3, 0]."""
        assert self.data["einf_poincare"] == [0, 3, 3, 0]

    def test_total_dim_6(self):
        """Total E_inf dimension = 6."""
        assert self.data["cohomology_total"] == 6


# =========================================================================
# 11. Cross-validation with a_infinity_bar_w1inf shadow tower
# =========================================================================

class TestCrossValidation:
    """Cross-validate d_4 computation with shadow tower data."""

    def test_S4_matches_shadow_tower(self):
        """S_4 from spectral sequence matches c3_shadow_tower value."""
        vir = E3BarSpectralSequenceVirasoro()
        # From c3_shadow_tower.py: spin2_shadow_data at c=1
        # S_4 = 10/(c(5c+22)) = 10/27
        # VERIFIED [DC] cross-check [LT] c3_shadow_tower.py
        assert vir.S4 == Rational(10, 27)

    def test_Delta_matches_a_inf_bar(self):
        """Delta from spectral sequence matches a_infinity_bar_w1inf."""
        vir = E3BarSpectralSequenceVirasoro()
        # From a_infinity_bar_w1inf.py line 754:
        # Delta = 8 * (c / 2) * S4_val
        # VERIFIED [DC] cross-check [LT] a_infinity_bar_w1inf.py
        assert vir.Delta == Rational(40, 27)

    def test_shadow_tower_kappa_alpha_S4_triple(self):
        """The (kappa, alpha, S4) triple matches the shadow tower."""
        vir = E3BarSpectralSequenceVirasoro()
        # From a_infinity_bar_w1inf.py AInfShadowTower:
        #   Spin 2: kappa=1/2, alpha=2, S_4=10/27
        # VERIFIED [DC] triple match [LT] AInfShadowTower.S4_per_channel
        from compute.lib.a_infinity_bar_w1inf import AInfBarComplex, AInfShadowTower
        bar_cx = AInfBarComplex()
        shadow = AInfShadowTower(bar_cx, max_spin=3)
        assert Rational(shadow.kappa_per_channel()[2].numerator,
                        shadow.kappa_per_channel()[2].denominator) == vir.kappa_ch
        assert Rational(shadow.alpha_per_channel()[2].numerator,
                        shadow.alpha_per_channel()[2].denominator) == vir.alpha
        assert Rational(shadow.S4_per_channel()[2].numerator,
                        shadow.S4_per_channel()[2].denominator) == vir.S4
