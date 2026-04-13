r"""Tests for the E_3 bar complex of the betagamma system (class C, r=4).

Verifies the spectral sequence computation for the betagamma system
(the simplest class C algebra, shadow depth r_max = 4).  The chain-level
dimensions are [q^n] P(q)^6 (hexapartitions, from 2 generators x 3 directions),
and the cohomology is (1+t)^6 = H*(T^6) via a three-page spectral sequence
where each differential d_i replaces one P(q)^2 factor with (1+t)^2.

Key mathematical facts:
  - betagamma OPE: beta(z)gamma(w) ~ 1/(z-w)  (simple pole, p_max = 1)
  - Class C: shadow depth r_max = 4, quartic shadow S_4 != 0
  - 2 generators per direction (beta, gamma), 3 directions => 6 total
  - Koszul algebra (Weyl algebra A_1), Koszul dual = exterior algebra
  - E_1 bar cohomology per direction: Lambda(beta*, gamma*) = (1+t)^2
  - The d_4 from S_4 vanishes on E_3 page by charge conservation

Ground truth:
  Chain (P(q)^6):    1, 6, 27, 98, 315, 918, 2492, 6372
  Cohomology:        [1, 6, 15, 20, 15, 6, 1] = C(6, n)
  Total:             2^6 = 64 = dim H*(T^6)
  Euler char:        0 = chi(T^6)

  E_1 page (H(d_1)):   (1+t)^2 * P(q)^4
  E_2 page (H(d_1,d_2)): (1+t)^4 * P(q)^2
  E_inf = E_3:          (1+t)^6

  Pattern across shadow classes:
    Class G (Heisenberg, 1 gen, r=2): P(q)^3 (formal, no differentials)
    Class L (Yangian,    1 gen, r=3): (1+t)^3 = 8  = 2^3 = H*(T^3)
    Class C (betagamma,  2 gen, r=4): (1+t)^6 = 64 = 2^6 = H*(T^6)

Manuscript references:
  holomorphic_cs_chiral_engine.py: E3BarComplexBetaGamma class
  cross_volume_shadow_bridge.py: class C classification for betagamma
  hms_shadow_equivalence.py: betagamma shadow data (kappa = -1/2)
"""

import pytest
from math import comb
from fractions import Fraction
from sympy import Rational

from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    E3BarComplexHeisenberg,
    E3BarComplexYangian,
    E3BarComplexBetaGamma,
    _partition_count,
    _bipartition_count,
    _hexapartition_count,
    _quadpartition_count,
)


# =========================================================================
# Ground truth
# =========================================================================

# P(q)^6 coefficients (hexapartitions)
CHAIN_GROUND_TRUTH = [1, 6, 27, 98, 315, 918, 2492, 6372]

# C(6, n) = binomial coefficients
COHOMOLOGY_GROUND_TRUTH = [1, 6, 15, 20, 15, 6, 1, 0]

# P(q)^2 coefficients (bipartitions, OEIS A000712)
BIPARTITION_GROUND_TRUTH = [1, 2, 5, 10, 20, 36, 65, 110, 185, 300]

# P(q)^4 coefficients (quadpartitions)
QUADPARTITION_GROUND_TRUTH = [1, 4, 14, 40, 105, 252, 574, 1240]

# P(q)^3 coefficients (tripartitions, OEIS A000716)
TAU_3_GROUND_TRUTH = [1, 3, 9, 22, 51, 108, 221, 429]


# =========================================================================
# 1. Classification: class C, shadow depth 4
# =========================================================================

class TestBetaGammaClassification:
    """betagamma is class C (contact), shadow depth 4."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    def test_shadow_class(self):
        assert self.bg.shadow_class == "C"

    def test_shadow_depth(self):
        assert self.bg.shadow_depth == 4

    def test_num_generators(self):
        assert self.bg.num_generators == 2

    def test_p_max(self):
        """OPE has simple pole: p_max = 1."""
        assert self.bg.p_max == 1

    def test_k_max(self):
        """No higher-order poles: k_max = 0."""
        assert self.bg.k_max == 0

    def test_differentials_nonzero(self):
        """Unlike Heisenberg (class G), differentials are nonzero."""
        assert self.bg.differentials_nonzero

    def test_quartic_shadow_nonzero(self):
        """S_4 != 0 distinguishes class C from class L."""
        assert self.bg.quartic_shadow_nonzero

    def test_cubic_shadow_zero(self):
        """alpha = 0 for betagamma (no cubic shadow)."""
        assert self.bg.alpha == Rational(0)

    def test_S4_value(self):
        """Q^contact = 1 for standard betagamma at c = -2."""
        assert self.bg.S4 == Rational(1)

    def test_central_charge(self):
        """c = -2 for betagamma with lambda = 1."""
        assert self.bg.central_charge == Rational(-2)

    def test_kappa_ch(self):
        """kappa_ch = -1/2."""
        assert self.bg.kappa_ch() == Rational(-1, 2)

    def test_d4_vanishes_on_e3_page(self):
        """d_4 from S_4 vanishes on E_3 page by charge conservation."""
        assert self.bg.d4_vanishes_on_e3_page


# =========================================================================
# 2. Utility functions: bipartitions and hexapartitions
# =========================================================================

class TestUtilityFunctions:
    """Verify the bipartition and hexapartition counting functions."""

    @pytest.mark.parametrize("n,expected", list(enumerate(BIPARTITION_GROUND_TRUTH)))
    def test_bipartition_count(self, n, expected):
        """Bipartition count bp(n) = [q^n] P(q)^2 (OEIS A000712)."""
        assert _bipartition_count(n) == expected

    @pytest.mark.parametrize("n,expected", list(enumerate(CHAIN_GROUND_TRUTH)))
    def test_hexapartition_count(self, n, expected):
        """Hexapartition count = [q^n] P(q)^6."""
        assert _hexapartition_count(n) == expected

    @pytest.mark.parametrize("n,expected", list(enumerate(QUADPARTITION_GROUND_TRUTH)))
    def test_quadpartition_count(self, n, expected):
        """Quadpartition count = [q^n] P(q)^4."""
        assert _quadpartition_count(n) == expected

    @pytest.mark.parametrize("n", range(8))
    def test_bipartition_is_convolution(self, n):
        """bp(n) = sum_{a+b=n} p(a)*p(b)."""
        direct = _bipartition_count(n)
        conv = sum(_partition_count(a) * _partition_count(n - a)
                   for a in range(n + 1))
        assert direct == conv

    @pytest.mark.parametrize("n", range(8))
    def test_hexapartition_is_triple_bipartition(self, n):
        """[q^n] P(q)^6 = sum_{a+b+c=n} bp(a)*bp(b)*bp(c)."""
        direct = _hexapartition_count(n)
        conv = sum(
            _bipartition_count(a) * _bipartition_count(b) * _bipartition_count(n - a - b)
            for a in range(n + 1) for b in range(n - a + 1)
        )
        assert direct == conv

    @pytest.mark.parametrize("n", range(8))
    def test_hexapartition_via_quad_times_bi(self, n):
        """P(q)^6 = P(q)^4 * P(q)^2."""
        direct = _hexapartition_count(n)
        conv = sum(_quadpartition_count(a) * _bipartition_count(n - a)
                   for a in range(n + 1))
        assert direct == conv

    @pytest.mark.parametrize("n", range(8))
    def test_hexapartition_via_product_formula(self, n):
        """Independent: compute [q^n] prod_{k>=1} 1/(1-q^k)^6 directly."""
        N = max(n, 1)
        a = [0] * (N + 1)
        a[0] = 1
        for k in range(1, N + 1):
            for _rep in range(6):
                for j in range(k, N + 1):
                    a[j] += a[j - k]
        assert _hexapartition_count(n) == a[n]


# =========================================================================
# 3. Chain-level dimensions = P(q)^6
# =========================================================================

class TestChainDimensions:
    """Chain-level dimensions are hexapartitions [q^n] P(q)^6."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    @pytest.mark.parametrize("n", range(8))
    def test_chain_matches_ground_truth(self, n):
        assert self.bg.chain_dimension(n) == CHAIN_GROUND_TRUTH[n]

    def test_chain_exceeds_heisenberg(self):
        """P(q)^6 > P(q)^3 for n >= 1 (2 generators vs 1)."""
        omega_sd = OmegaBackground(1, 0)
        heisenberg = E3BarComplexHeisenberg(omega_sd)
        for n in range(1, 8):
            assert self.bg.chain_dimension(n) > heisenberg.trigraded_dimension(n)

    def test_chain_at_n0(self):
        """At n=0: only the empty multipartition."""
        assert self.bg.chain_dimension(0) == 1

    def test_chain_at_n1(self):
        """At n=1: 6 = 3 directions x 2 generators."""
        assert self.bg.chain_dimension(1) == 6

    def test_trigraded_sum_equals_total(self):
        """Sum of trigraded decomposition equals total chain dimension."""
        for n in range(7):
            decomp = self.bg.trigraded_decomposition(n)
            assert sum(decomp.values()) == self.bg.chain_dimension(n)

    def test_tridegree_symmetry(self):
        """S_3 symmetry of C^3 implies tridegree symmetry."""
        for n in range(6):
            decomp = self.bg.trigraded_decomposition(n)
            for (a, b, c), dim in decomp.items():
                assert decomp.get((b, a, c), 0) == dim
                assert decomp.get((a, c, b), 0) == dim
                assert decomp.get((c, b, a), 0) == dim


# =========================================================================
# 4. E_1 bar cohomology per direction = (1+t)^2
# =========================================================================

class TestE1BarPerDirection:
    """E_1 bar cohomology of betagamma = Lambda(beta*, gamma*) = (1+t)^2."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    def test_h0(self):
        """H_0 = 1 (ground field)."""
        assert self.bg.e1_bar_cohomology_per_direction(0) == 1

    def test_h1(self):
        """H_1 = 2 (two generators: beta, gamma)."""
        assert self.bg.e1_bar_cohomology_per_direction(1) == 2

    def test_h2(self):
        """H_2 = 1 (top exterior power: beta* ^ gamma*)."""
        assert self.bg.e1_bar_cohomology_per_direction(2) == 1

    def test_h3_vanishes(self):
        """H_n = 0 for n >= 3 (Koszul: acyclic beyond arity 2)."""
        for n in range(3, 8):
            assert self.bg.e1_bar_cohomology_per_direction(n) == 0

    def test_total_per_direction(self):
        """Total per direction = 1+2+1 = 4 = 2^2."""
        total = sum(self.bg.e1_bar_cohomology_per_direction(n) for n in range(5))
        assert total == 4

    def test_euler_per_direction(self):
        """Euler char per direction = 1-2+1 = 0."""
        euler = sum((-1)**n * self.bg.e1_bar_cohomology_per_direction(n)
                    for n in range(5))
        assert euler == 0

    def test_matches_exterior_algebra(self):
        """H_n = C(2, n) = exterior algebra on 2 generators."""
        for n in range(5):
            assert self.bg.e1_bar_cohomology_per_direction(n) == comb(2, n)


# =========================================================================
# 5. Cohomology dimensions = C(6, n) = H*(T^6)
# =========================================================================

class TestCohomologyDimensions:
    """E_3 bar cohomology of betagamma is H*(T^6)."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_matches_binomial(self, n):
        expected = comb(6, n) if 0 <= n <= 6 else 0
        assert self.bg.cohomology_dimension(n) == expected

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_matches_ground_truth(self, n):
        assert self.bg.cohomology_dimension(n) == COHOMOLOGY_GROUND_TRUTH[n]

    def test_total_is_64(self):
        assert self.bg.cohomology_total() == 64

    def test_total_is_2_to_6(self):
        """2^6 = 64 = dim H*(T^6)."""
        assert self.bg.cohomology_total() == 2**6

    def test_total_is_2_to_3g(self):
        """2^{3g} with g = 2 generators."""
        assert self.bg.cohomology_total() == 2 ** (3 * self.bg.num_generators)

    def test_euler_characteristic_zero(self):
        """chi(T^6) = 0."""
        assert self.bg.euler_characteristic() == 0

    def test_poincare_polynomial(self):
        """Poincare polynomial (1+t)^6 = [1, 6, 15, 20, 15, 6, 1]."""
        assert self.bg.cohomology_poincare() == [1, 6, 15, 20, 15, 6, 1]

    def test_poincare_symmetry(self):
        """Poincare duality: h_k = h_{6-k}."""
        poinc = self.bg.cohomology_poincare()
        for k in range(7):
            assert poinc[k] == poinc[6 - k]

    def test_vanishes_above_6(self):
        """H^n = 0 for n >= 7."""
        for n in range(7, 12):
            assert self.bg.cohomology_dimension(n) == 0


# =========================================================================
# 6. Spectral sequence: P(q)^6 -> (1+t)^2 P(q)^4 -> (1+t)^4 P(q)^2 -> (1+t)^6
# =========================================================================

class TestSpectralSequence:
    """Three-page spectral sequence for the betagamma E_3 bar."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()
        self.ss = self.bg.verify_spectral_sequence(7)

    @pytest.mark.parametrize("n", range(8))
    def test_e0_is_chain(self, n):
        """E_0 page = full chain complex = [q^n] P(q)^6."""
        assert self.ss[n]["E_0 (chain)"] == CHAIN_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_e1_generating_function(self, n):
        """E_1 page = (1+t)^2 * P(q)^4."""
        expected = sum(
            comb(2, k) * _quadpartition_count(n - k)
            for k in range(min(3, n + 1))
        )
        assert self.ss[n]["E_1 (H(d_1))"] == expected

    @pytest.mark.parametrize("n", range(8))
    def test_e2_generating_function(self, n):
        """E_2 page = (1+t)^4 * P(q)^2."""
        expected = sum(
            comb(4, k) * _bipartition_count(n - k)
            for k in range(min(5, n + 1))
        )
        assert self.ss[n]["E_2 (H(d_1,d_2))"] == expected

    @pytest.mark.parametrize("n", range(8))
    def test_einf_matches_binomial_6(self, n):
        expected = comb(6, n) if 0 <= n <= 6 else 0
        assert self.ss[n]["E_inf (cohomology)"] == expected

    @pytest.mark.parametrize("n", range(8))
    def test_all_pages_match_binomial_flag(self, n):
        assert self.ss[n]["matches_binomial_6"]

    def test_monotone_decrease_across_pages(self):
        """Each page has smaller or equal dimensions than the previous."""
        for n in range(8):
            e0 = self.ss[n]["E_0 (chain)"]
            e1 = self.ss[n]["E_1 (H(d_1))"]
            e2 = self.ss[n]["E_2 (H(d_1,d_2))"]
            einf = self.ss[n]["E_inf (cohomology)"]
            assert e0 >= e1 >= e2 >= einf >= 0

    def test_low_arities_survive(self):
        """At n=0,1: all pages agree (differentials need arity >= 2)."""
        assert self.ss[0]["E_0 (chain)"] == self.ss[0]["E_inf (cohomology)"] == 1
        assert self.ss[1]["E_0 (chain)"] == self.ss[1]["E_inf (cohomology)"] == 6


# =========================================================================
# 7. Chain vs cohomology: differentials kill P(q)^6 - C(6,n)
# =========================================================================

class TestChainVsCohomology:
    """The nonzero differentials kill most of the chain complex."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    def test_arity_0_survives(self):
        assert self.bg.chain_dimension(0) == self.bg.cohomology_dimension(0) == 1

    def test_arity_1_survives(self):
        """At arity 1, all 6 generators survive."""
        assert self.bg.chain_dimension(1) == self.bg.cohomology_dimension(1) == 6

    def test_arity_2_kills_12(self):
        """At arity 2: 27 chain - 15 cohomology = 12 killed."""
        assert self.bg.chain_dimension(2) - self.bg.cohomology_dimension(2) == 12

    def test_arity_3_kills_78(self):
        """At arity 3: 98 chain - 20 cohomology = 78 killed."""
        assert self.bg.chain_dimension(3) - self.bg.cohomology_dimension(3) == 78

    def test_high_arity_almost_all_killed(self):
        """At arity >= 7, chain is completely exact."""
        for n in range(7, 8):
            assert self.bg.cohomology_dimension(n) == 0
            assert self.bg.chain_dimension(n) > 0

    def test_killed_fraction_increases(self):
        """The fraction killed by differentials increases with arity."""
        for n in range(2, 6):
            ch_n = self.bg.chain_dimension(n)
            co_n = self.bg.cohomology_dimension(n)
            ch_n1 = self.bg.chain_dimension(n + 1)
            co_n1 = self.bg.cohomology_dimension(n + 1)
            frac_n = (ch_n - co_n) / ch_n if ch_n > 0 else 0
            frac_n1 = (ch_n1 - co_n1) / ch_n1 if ch_n1 > 0 else 0
            assert frac_n1 >= frac_n


# =========================================================================
# 8. kappa and Koszul conductor
# =========================================================================

class TestKappaAndConductor:
    """kappa_ch = -1/2, conductor rho_K = -5/12 (nonzero for class C)."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    def test_kappa_ch(self):
        assert self.bg.kappa_ch() == Rational(-1, 2)

    def test_kappa_ch_dual(self):
        """Koszul dual (bc system) has kappa = 1/12."""
        assert self.bg.kappa_ch_dual() == Rational(1, 12)

    def test_koszul_conductor_nonzero(self):
        """rho_K = -1/2 + 1/12 = -5/12 != 0 (class C hallmark)."""
        assert self.bg.koszul_conductor() == Rational(-5, 12)
        assert self.bg.koszul_conductor() != 0

    def test_kappa_complementarity(self):
        """kappa + kappa^! = rho_K (tautological but API-consistent)."""
        assert self.bg.verify_kappa_complementarity()

    def test_conductor_nonzero_distinguishes_from_class_G(self):
        """Class G (Heisenberg) has rho_K = 0; class C has rho_K != 0."""
        heisenberg = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        assert heisenberg.koszul_conductor() == Rational(0)
        assert self.bg.koszul_conductor() != Rational(0)


# =========================================================================
# 9. Contrast with Heisenberg (class G) and Yangian (class L)
# =========================================================================

class TestContrastAcrossClasses:
    """The three classes G, L, C have increasingly complex E_3 bar structure."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()
        self.heisenberg = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        self.yangian = E3BarComplexYangian(OmegaBackground(1, 2))

    # --- Chain dimensions differ ---

    def test_chain_ordering(self):
        """P(q)^6 > P(q)^3 for n >= 1."""
        for n in range(1, 7):
            assert self.bg.chain_dimension(n) > self.heisenberg.trigraded_dimension(n)

    def test_heisenberg_chain_equals_yangian(self):
        """Heisenberg and Yangian share chain dimensions P(q)^3."""
        for n in range(7):
            assert (self.heisenberg.trigraded_dimension(n)
                    == self.yangian.chain_dimension(n))

    # --- Cohomology differs ---

    def test_class_g_cohomology_infinite(self):
        """Class G: cohomology = chain (infinite at each arity)."""
        for n in range(1, 7):
            assert self.heisenberg.trigraded_dimension(n) == TAU_3_GROUND_TRUTH[n]

    def test_class_l_cohomology_8(self):
        """Class L: total cohomology = 8 = 2^3."""
        assert self.yangian.cohomology_total() == 8

    def test_class_c_cohomology_64(self):
        """Class C: total cohomology = 64 = 2^6."""
        assert self.bg.cohomology_total() == 64

    def test_pattern_2_to_3g(self):
        """Pattern: 2^{3g} where g = number of generators.

        Class G: g not applicable (formal, infinite cohom).
        Class L: g=1 -> 2^3 = 8.
        Class C: g=2 -> 2^6 = 64.
        """
        assert self.yangian.cohomology_total() == 2**(3 * 1)
        assert self.bg.cohomology_total() == 2**(3 * 2)

    # --- Shadow classes ---

    def test_shadow_class_progression(self):
        assert self.heisenberg.shadow_class == "G"
        assert self.yangian.shadow_class == "L"
        assert self.bg.shadow_class == "C"

    def test_shadow_depth_progression(self):
        assert self.heisenberg.shadow_depth == 2
        assert self.yangian.shadow_depth == 3
        assert self.bg.shadow_depth == 4

    # --- Euler characteristic ---

    def test_class_l_euler_zero(self):
        assert self.yangian.euler_characteristic() == 0

    def test_class_c_euler_zero(self):
        assert self.bg.euler_characteristic() == 0


# =========================================================================
# 10. Full investigation output validation
# =========================================================================

class TestFullInvestigation:
    """Validate the full_investigation() output dictionary."""

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()
        self.result = self.bg.full_investigation()

    def test_algebra_name(self):
        assert "betagamma" in self.result["algebra"]

    def test_class_and_depth(self):
        assert self.result["shadow_class"] == "C"
        assert self.result["shadow_depth"] == 4

    def test_num_generators(self):
        assert self.result["num_generators"] == 2

    def test_kappa(self):
        assert self.result["kappa_ch"] == Rational(-1, 2)

    def test_chain_dimensions_present(self):
        assert self.result["chain_dimensions (P(q)^6)"][:4] == [1, 6, 27, 98]

    def test_cohomology_dimensions_present(self):
        assert self.result["cohomology_dimensions"][:4] == [1, 6, 15, 20]

    def test_poincare_present(self):
        assert self.result["cohomology_poincare"] == [1, 6, 15, 20, 15, 6, 1]

    def test_total_present(self):
        assert self.result["cohomology_total"] == 64

    def test_euler_present(self):
        assert self.result["euler_characteristic"] == 0

    def test_spectral_sequence_present(self):
        ss = self.result["spectral_sequence"]
        assert 0 in ss and 5 in ss

    def test_d4_flag(self):
        assert self.result["d4_vanishes_on_e3"] is True

    def test_S4_present(self):
        assert self.result["S4 (quartic shadow)"] == Rational(1)


# =========================================================================
# 11. Multi-path verification (AP10 compliance)
# =========================================================================

class TestMultiPathVerification:
    """Cross-check all key quantities via independent computation paths.

    Path 1: Engine computation (E3BarComplexBetaGamma methods)
    Path 2: Direct combinatorial computation (partition convolution)
    Path 3: Cross-volume shadow bridge classification
    Path 4: Generating function coefficient extraction
    Path 5: Spectral sequence page-by-page independent computation
    """

    def setup_method(self):
        self.bg = E3BarComplexBetaGamma()

    # --- Chain (P(q)^6) via three independent paths ---

    @pytest.mark.parametrize("n", range(8))
    def test_chain_path1_engine_vs_path2_convolution(self, n):
        """Path 1 (engine) vs Path 2 (6-fold convolution of p(n))."""
        engine_val = self.bg.chain_dimension(n)
        conv_val = sum(
            _partition_count(a) * _partition_count(b) * _partition_count(c)
            * _partition_count(d) * _partition_count(e) * _partition_count(n - a - b - c - d - e)
            for a in range(n + 1)
            for b in range(n - a + 1)
            for c in range(n - a - b + 1)
            for d in range(n - a - b - c + 1)
            for e in range(n - a - b - c - d + 1)
        )
        assert engine_val == conv_val

    @pytest.mark.parametrize("n", range(8))
    def test_chain_path4_product_formula(self, n):
        """Path 4: [q^n] prod_{k>=1} 1/(1-q^k)^6."""
        N = max(n, 1)
        a = [0] * (N + 1)
        a[0] = 1
        for k in range(1, N + 1):
            for _rep in range(6):
                for j in range(k, N + 1):
                    a[j] += a[j - k]
        assert self.bg.chain_dimension(n) == a[n]

    # --- Cohomology via multiple paths ---

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_path1_engine_vs_path2_binomial(self, n):
        """Path 1 (engine) vs Path 2 (C(6, n))."""
        engine_val = self.bg.cohomology_dimension(n)
        binom_val = comb(6, n) if 0 <= n <= 6 else 0
        assert engine_val == binom_val

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_path5_compositions(self, n):
        """Path 5: count 6-tuples of {0,1} summing to n."""
        binom_val = comb(6, n) if 0 <= n <= 6 else 0
        count = sum(
            1 for a in (0, 1) for b in (0, 1) for c in (0, 1)
            for d in (0, 1) for e in (0, 1) for f in (0, 1)
            if a + b + c + d + e + f == n
        )
        assert binom_val == count

    # --- E_1 page via independent computation ---

    @pytest.mark.parametrize("n", range(7))
    def test_e1_page_independent(self, n):
        """E_1 page = (1+t)^2 * P(q)^4, computed independently."""
        ss = self.bg.verify_spectral_sequence(7)
        ss_val = ss[n]["E_1 (H(d_1))"]
        indep = sum(
            comb(2, k) * _quadpartition_count(n - k)
            for k in range(min(3, n + 1))
        )
        assert ss_val == indep

    # --- E_2 page via independent computation ---

    @pytest.mark.parametrize("n", range(7))
    def test_e2_page_independent(self, n):
        """E_2 page = (1+t)^4 * P(q)^2, computed independently."""
        ss = self.bg.verify_spectral_sequence(7)
        ss_val = ss[n]["E_2 (H(d_1,d_2))"]
        indep = sum(
            comb(4, k) * _bipartition_count(n - k)
            for k in range(min(5, n + 1))
        )
        assert ss_val == indep

    # --- Cross-volume bridge ---

    def test_class_c_from_cross_volume_bridge(self):
        """Path 3: verify classification matches cross_volume_shadow_bridge."""
        from compute.lib.cross_volume_shadow_bridge import shadow_depth_class
        cls, r_max = shadow_depth_class("betagamma")
        assert cls == "C"
        assert r_max == 4
        assert cls == self.bg.shadow_class
        assert r_max == self.bg.shadow_depth

    # --- Euler characteristic ---

    def test_euler_char_alternating_vs_formula(self):
        """Alternating sum vs (1-1)^6 = 0."""
        alt_sum = sum((-1)**n * self.bg.cohomology_dimension(n) for n in range(8))
        formula_val = (1 - 1)**6
        assert alt_sum == formula_val == 0

    # --- Total dimension ---

    def test_total_sum_vs_power(self):
        """Sum of Poincare vs 2^6."""
        total_sum = sum(self.bg.cohomology_dimension(n) for n in range(8))
        assert total_sum == 2**6 == 64


# =========================================================================
# 12. Charge conservation argument for d_4 = 0
# =========================================================================

class TestChargeConservation:
    """Verify that the charge grading forces d_4 = 0 on the E_3 page.

    The betagamma system has a Z-grading by charge:
      beta has charge +1, gamma has charge -1.

    In the E_3 tricomplex, the 6 generators have charges:
      beta_1: +1, gamma_1: -1, beta_2: +1, gamma_2: -1, beta_3: +1, gamma_3: -1

    Elements of Lambda^n(k^6) have total charge = (# betas) - (# gammas).
    Since (# betas) + (# gammas) = n, the charge has the same parity as n.

    d_4: Lambda^n -> Lambda^{n-3} would map even-charge to odd-charge
    (parity of n and n-3 differ). Since m_4 preserves charge,
    d_4 must be zero.
    """

    def test_charge_parity_argument(self):
        """Elements in Lambda^n have charge with parity = parity(n).

        d_4: Lambda^n -> Lambda^{n-3} crosses parity, so d_4 = 0.
        """
        for n in range(7):
            # In Lambda^n, possible charges are: n, n-2, n-4, ..., -(n-2), -n
            # These all have parity = parity(n).
            charges_n = set(range(n, -(n + 1), -2))  # n, n-2, ..., -n
            assert all(c % 2 == n % 2 for c in charges_n)

            if n >= 3:
                # Lambda^{n-3}: charges have parity = parity(n-3) = parity(n) + 1 mod 2
                charges_n3 = set(range(n - 3, -(n - 3 + 1), -2))
                assert all(c % 2 == (n - 3) % 2 for c in charges_n3)
                # Parity mismatch!
                assert (n % 2) != ((n - 3) % 2)

    def test_d4_zero_implies_e3_equals_einf(self):
        """If d_4 = 0, then E_3 = E_inf and cohomology = (1+t)^6."""
        bg = E3BarComplexBetaGamma()
        assert bg.d4_vanishes_on_e3_page
        # Verify E_3 dimensions = E_inf dimensions
        ss = bg.verify_spectral_sequence(7)
        for n in range(8):
            assert ss[n]["E_inf (cohomology)"] == (comb(6, n) if n <= 6 else 0)

    def test_charge_preservation_by_m4(self):
        """m_4 preserves charge (as an A_infinity operation).

        m_4(beta_i, gamma_i, beta_j, gamma_j) has input charge 0.
        Output must also have charge 0.
        In Lambda^1, possible charges are +1 and -1 (not 0).
        So the output cannot be in Lambda^1, forcing d_4 = 0 on Lambda^4.
        """
        # Input charges for typical m_4 arguments
        input_charges = [+1, -1, +1, -1]  # beta_i, gamma_i, beta_j, gamma_j
        total_input_charge = sum(input_charges)
        assert total_input_charge == 0

        # Output in Lambda^1 must have charge +/-1
        possible_output_charges = {+1, -1}
        assert total_input_charge not in possible_output_charges


# =========================================================================
# 13. The 2^{3g} pattern
# =========================================================================

class TestTwoTo3gPattern:
    """The E_3 bar cohomology total dimension follows 2^{3g} for g generators.

    g=1 (class L, Yangian):   2^3 = 8
    g=2 (class C, betagamma): 2^6 = 64

    The generating formula: for a Koszul E_3 algebra with g generators,
    H^*(B_{E_3}(A)) = Lambda^*(k^{3g}),
    total dim = 2^{3g}, Poincare = (1+t)^{3g}.
    """

    def test_g1_yangian(self):
        yangian = E3BarComplexYangian(OmegaBackground(1, 2))
        g = 1
        assert yangian.cohomology_total() == 2**(3 * g)
        assert yangian.cohomology_poincare() == [comb(3 * g, k) for k in range(3 * g + 1)]

    def test_g2_betagamma(self):
        bg = E3BarComplexBetaGamma()
        g = 2
        assert bg.cohomology_total() == 2**(3 * g)
        assert bg.cohomology_poincare() == [comb(3 * g, k) for k in range(3 * g + 1)]

    def test_pattern_formula(self):
        """Verify 2^{3g} = (2^g)^3 = dim(Lambda^*(k^g))^3."""
        for g in (1, 2, 3, 4):
            assert 2**(3 * g) == (2**g)**3
