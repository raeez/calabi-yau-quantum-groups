r"""Tests for the E_3 bar complex of the bc system (fermionic class C, r=4).

Verifies the spectral sequence computation for the bc system
(the fermionic analogue of betagamma, also class C with shadow depth r_max = 4).

KEY RESULT: The (1+t)^{3g} formula holds for the bc system too.  Despite
fermionic statistics changing the chain-level dimensions from P(q)^6
(bosonic hexapartitions) to F(q)^6 (fermionic hexapartitions), the
E_3 bar cohomology is STILL (1+t)^6 = H*(T^6).

This confirms (1+t)^{3g} as universal for ALL standard class C algebras.

Mathematical facts:
  - bc OPE: b(z)c(w) ~ 1/(z-w)  (simple pole, same as betagamma)
  - Statistics: fermionic (b, c anticommute), unlike bosonic betagamma
  - Class C: shadow depth r_max = 4, quartic shadow S_4 != 0
  - 2 generators per direction (b, c), 3 directions => 6 total
  - Koszul algebra (Clifford algebra Cl_1), Koszul dual = Weyl algebra
  - E_1 bar cohomology per direction: Lambda(b*, c*) = (1+t)^2
    (SAME as betagamma: Ext^*(k,k) depends on generator/relation count,
     not on whether relation is commutator or anticommutator)
  - Charge conservation kills d_4: b has charge +1, c has charge -1,
    IDENTICAL grading to betagamma => same parity argument applies.

Chain-level difference from betagamma:
  - betagamma chain: [q^n] P(q)^6 = 1, 6, 27, 98, 315, 918, ...
  - bc chain:        [q^n] F(q)^6 = 1, 6, 21, 62, 162, 384, ...
  where F(q) = prod_{k>=1}(1+q^k) counts partitions into distinct parts.
  The fermionic chain is SMALLER (F(q)^6 < P(q)^6 for n >= 2).

Ground truth:
  Chain (F(q)^6):    1, 6, 21, 62, 162, 384, 855, 1806
  Cohomology:        [1, 6, 15, 20, 15, 6, 1] = C(6, n)
  Total:             2^6 = 64 = dim H*(T^6)
  Euler char:        0 = chi(T^6)

  E_1 page (H(d_1)):   (1+t)^2 * F(q)^4
  E_2 page (H(d_1,d_2)): (1+t)^4 * F(q)^2
  E_inf = E_3:          (1+t)^6

  Universal pattern (statistics-independent):
    Class G (Heisenberg, 1 gen, r=2): P(q)^3 (formal, no differentials)
    Class L (Yangian,    1 gen, r=3): (1+t)^3 = 8  = 2^3 = H*(T^3)
    Class C (betagamma,  2 gen, r=4): (1+t)^6 = 64 = 2^6 = H*(T^6)
    Class C (bc,         2 gen, r=4): (1+t)^6 = 64 = 2^6 = H*(T^6)  [THIS FILE]

Manuscript references:
  holomorphic_cs_chiral_engine.py: E3BarComplexBc class
  cross_volume_shadow_bridge.py: class C classification
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
    E3BarComplexBc,
    _partition_count,
    _bipartition_count,
    _hexapartition_count,
    _quadpartition_count,
    _distinct_partition_count,
    _fermionic_bipartition_count,
    _fermionic_quadpartition_count,
    _fermionic_hexapartition_count,
)


# =========================================================================
# Ground truth
# =========================================================================

# F(q)^6 coefficients (fermionic hexapartitions)
CHAIN_GROUND_TRUTH = [1, 6, 21, 62, 162, 384, 855, 1806]

# C(6, n) = binomial coefficients -- SAME as betagamma
COHOMOLOGY_GROUND_TRUTH = [1, 6, 15, 20, 15, 6, 1, 0]

# F(q) coefficients: partitions into distinct parts (OEIS A000009)
DISTINCT_PARTITION_GROUND_TRUTH = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12]

# F(q)^2 coefficients (fermionic bipartitions)
FERMIONIC_BIPARTITION_GROUND_TRUTH = [1, 2, 3, 6, 9, 14, 22, 32, 46, 66, 93, 128]

# F(q)^4 coefficients (fermionic quadpartitions)
FERMIONIC_QUADPARTITION_GROUND_TRUTH = [1, 4, 10, 24, 51, 100, 190, 344]

# P(q)^6 coefficients (bosonic hexapartitions, for comparison)
BOSONIC_CHAIN_GROUND_TRUTH = [1, 6, 27, 98, 315, 918, 2492, 6372]


# =========================================================================
# 1. Classification: class C, shadow depth 4, fermionic
# =========================================================================

class TestBcClassification:
    """bc is class C (contact), shadow depth 4, fermionic."""

    def setup_method(self):
        self.bc = E3BarComplexBc()

    def test_shadow_class(self):
        assert self.bc.shadow_class == "C"

    def test_shadow_depth(self):
        assert self.bc.shadow_depth == 4

    def test_num_generators(self):
        assert self.bc.num_generators == 2

    def test_statistics(self):
        """bc is fermionic, distinguishing it from bosonic betagamma."""
        assert self.bc.statistics == "fermionic"

    def test_p_max(self):
        """OPE has simple pole: p_max = 1 (same as betagamma)."""
        assert self.bc.p_max == 1

    def test_k_max(self):
        """No higher-order poles: k_max = 0."""
        assert self.bc.k_max == 0

    def test_differentials_nonzero(self):
        """Unlike Heisenberg (class G), differentials are nonzero."""
        assert self.bc.differentials_nonzero

    def test_quartic_shadow_nonzero(self):
        """S_4 != 0 distinguishes class C from class L."""
        assert self.bc.quartic_shadow_nonzero

    def test_cubic_shadow_zero(self):
        """alpha = 0 for bc (no cubic shadow, same as betagamma)."""
        assert self.bc.alpha == Rational(0)

    def test_central_charge(self):
        """c = 2 for bc (opposite sign from betagamma c = -2)."""
        assert self.bc.central_charge == Rational(2)

    def test_kappa_ch(self):
        """kappa_ch = 1/12 (AP113: always subscripted)."""
        assert self.bc.kappa_ch() == Rational(1, 12)

    def test_d4_vanishes_on_e3_page(self):
        """d_4 from S_4 vanishes on E_3 page by charge conservation."""
        assert self.bc.d4_vanishes_on_e3_page

    def test_same_class_as_betagamma(self):
        """bc and betagamma share the same shadow class C."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.shadow_class == bg.shadow_class
        assert self.bc.shadow_depth == bg.shadow_depth


# =========================================================================
# 2. Fermionic partition functions
# =========================================================================

class TestFermionicPartitionFunctions:
    """Verify the fermionic partition function utilities."""

    @pytest.mark.parametrize("n,expected",
                             list(enumerate(DISTINCT_PARTITION_GROUND_TRUTH)))
    def test_distinct_partition_count(self, n, expected):
        """F(q) = prod(1+q^k): partitions into distinct parts (OEIS A000009)."""
        assert _distinct_partition_count(n) == expected

    @pytest.mark.parametrize("n,expected",
                             list(enumerate(FERMIONIC_BIPARTITION_GROUND_TRUTH)))
    def test_fermionic_bipartition_count(self, n, expected):
        """F(q)^2 = convolution of distinct partition counts."""
        assert _fermionic_bipartition_count(n) == expected

    @pytest.mark.parametrize("n,expected",
                             list(enumerate(FERMIONIC_QUADPARTITION_GROUND_TRUTH)))
    def test_fermionic_quadpartition_count(self, n, expected):
        """F(q)^4 = convolution of fermionic bipartitions."""
        assert _fermionic_quadpartition_count(n) == expected

    @pytest.mark.parametrize("n,expected", list(enumerate(CHAIN_GROUND_TRUTH)))
    def test_fermionic_hexapartition_count(self, n, expected):
        """F(q)^6: chain-level dimension of bc E_3 bar."""
        assert _fermionic_hexapartition_count(n) == expected

    @pytest.mark.parametrize("n", range(8))
    def test_fermionic_bipartition_is_convolution(self, n):
        """fb(n) = sum_{a+b=n} f(a)*f(b)."""
        direct = _fermionic_bipartition_count(n)
        conv = sum(_distinct_partition_count(a) * _distinct_partition_count(n - a)
                   for a in range(n + 1))
        assert direct == conv

    @pytest.mark.parametrize("n", range(8))
    def test_fermionic_hexapartition_is_triple_bipartition(self, n):
        """[q^n] F(q)^6 = sum_{a+b+c=n} fb(a)*fb(b)*fb(c)."""
        direct = _fermionic_hexapartition_count(n)
        conv = sum(
            _fermionic_bipartition_count(a)
            * _fermionic_bipartition_count(b)
            * _fermionic_bipartition_count(n - a - b)
            for a in range(n + 1) for b in range(n - a + 1)
        )
        assert direct == conv

    @pytest.mark.parametrize("n", range(8))
    def test_fermionic_hexapartition_via_quad_times_bi(self, n):
        """F(q)^6 = F(q)^4 * F(q)^2."""
        direct = _fermionic_hexapartition_count(n)
        conv = sum(_fermionic_quadpartition_count(a)
                   * _fermionic_bipartition_count(n - a)
                   for a in range(n + 1))
        assert direct == conv

    @pytest.mark.parametrize("n", range(8))
    def test_fermionic_via_product_formula(self, n):
        """Independent: compute [q^n] prod_{k>=1} (1+q^k)^6 directly."""
        N = max(n, 1)
        a = [0] * (N + 1)
        a[0] = 1
        for k in range(1, N + 1):
            # Each of 6 fermionic modes at level k: multiply by (1+q^k) six times
            for _rep in range(6):
                for j in range(N, k - 1, -1):
                    a[j] += a[j - k]
        assert _fermionic_hexapartition_count(n) == a[n]

    def test_euler_identity_distinct_parts_equals_odd_parts(self):
        """Euler: partitions into distinct parts = partitions into odd parts."""
        for n in range(12):
            # Count partitions of n into odd parts via DP
            dp = [0] * (n + 1)
            dp[0] = 1
            for k in range(1, n + 1, 2):  # odd parts only
                for j in range(k, n + 1):
                    dp[j] += dp[j - k]
            assert _distinct_partition_count(n) == dp[n]


# =========================================================================
# 3. Chain-level dimensions = F(q)^6 (fermionic)
# =========================================================================

class TestChainDimensions:
    """Chain-level dimensions are fermionic hexapartitions [q^n] F(q)^6."""

    def setup_method(self):
        self.bc = E3BarComplexBc()

    @pytest.mark.parametrize("n", range(8))
    def test_chain_matches_ground_truth(self, n):
        assert self.bc.chain_dimension(n) == CHAIN_GROUND_TRUTH[n]

    def test_chain_at_n0(self):
        """At n=0: only the empty multipartition."""
        assert self.bc.chain_dimension(0) == 1

    def test_chain_at_n1(self):
        """At n=1: 6 = 3 directions x 2 generators (same as betagamma!)."""
        assert self.bc.chain_dimension(1) == 6

    def test_chain_agrees_with_betagamma_at_n0_n1(self):
        """At n=0,1: fermionic and bosonic chains agree."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.chain_dimension(0) == bg.chain_dimension(0) == 1
        assert self.bc.chain_dimension(1) == bg.chain_dimension(1) == 6

    @pytest.mark.parametrize("n", range(2, 8))
    def test_chain_strictly_smaller_than_bosonic(self, n):
        """F(q)^6 < P(q)^6 for n >= 2 (Pauli exclusion reduces states)."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.chain_dimension(n) < bg.chain_dimension(n)

    def test_trigraded_sum_equals_total(self):
        """Sum of trigraded decomposition equals total chain dimension."""
        for n in range(7):
            decomp = self.bc.trigraded_decomposition(n)
            assert sum(decomp.values()) == self.bc.chain_dimension(n)

    def test_tridegree_symmetry(self):
        """S_3 symmetry of C^3 implies tridegree symmetry."""
        for n in range(6):
            decomp = self.bc.trigraded_decomposition(n)
            for (a, b, c), dim in decomp.items():
                assert decomp.get((b, a, c), 0) == dim
                assert decomp.get((a, c, b), 0) == dim
                assert decomp.get((c, b, a), 0) == dim


# =========================================================================
# 4. E_1 bar cohomology per direction = (1+t)^2 (SAME as betagamma)
# =========================================================================

class TestE1BarPerDirection:
    """E_1 bar cohomology of bc = Lambda(b*, c*) = (1+t)^2.

    CRITICAL: this is the SAME as betagamma, because both Weyl and
    Clifford are Koszul with 2 generators and 1 relation.
    """

    def setup_method(self):
        self.bc = E3BarComplexBc()

    def test_h0(self):
        """H_0 = 1 (ground field)."""
        assert self.bc.e1_bar_cohomology_per_direction(0) == 1

    def test_h1(self):
        """H_1 = 2 (two generators: b, c)."""
        assert self.bc.e1_bar_cohomology_per_direction(1) == 2

    def test_h2(self):
        """H_2 = 1 (top exterior power: b* ^ c*)."""
        assert self.bc.e1_bar_cohomology_per_direction(2) == 1

    def test_h3_vanishes(self):
        """H_n = 0 for n >= 3 (Koszul: acyclic beyond arity 2)."""
        for n in range(3, 8):
            assert self.bc.e1_bar_cohomology_per_direction(n) == 0

    def test_total_per_direction(self):
        """Total per direction = 1+2+1 = 4 = 2^2."""
        total = sum(self.bc.e1_bar_cohomology_per_direction(n) for n in range(5))
        assert total == 4

    def test_euler_per_direction(self):
        """Euler char per direction = 1-2+1 = 0."""
        euler = sum((-1)**n * self.bc.e1_bar_cohomology_per_direction(n)
                    for n in range(5))
        assert euler == 0

    def test_matches_exterior_algebra(self):
        """H_n = C(2, n) = exterior algebra on 2 generators."""
        for n in range(5):
            assert self.bc.e1_bar_cohomology_per_direction(n) == comb(2, n)

    def test_identical_to_betagamma(self):
        """E_1 bar cohomology per direction is the same for bc and betagamma."""
        bg = E3BarComplexBetaGamma()
        for n in range(8):
            assert (self.bc.e1_bar_cohomology_per_direction(n)
                    == bg.e1_bar_cohomology_per_direction(n))


# =========================================================================
# 5. Cohomology dimensions = C(6, n) = H*(T^6)  [UNIVERSAL]
# =========================================================================

class TestCohomologyDimensions:
    """E_3 bar cohomology of bc is H*(T^6), same as betagamma.

    This is the KEY RESULT: (1+t)^{3g} is universal across statistics.
    """

    def setup_method(self):
        self.bc = E3BarComplexBc()

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_matches_binomial(self, n):
        expected = comb(6, n) if 0 <= n <= 6 else 0
        assert self.bc.cohomology_dimension(n) == expected

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_matches_ground_truth(self, n):
        assert self.bc.cohomology_dimension(n) == COHOMOLOGY_GROUND_TRUTH[n]

    def test_total_is_64(self):
        assert self.bc.cohomology_total() == 64

    def test_total_is_2_to_6(self):
        """2^6 = 64 = dim H*(T^6)."""
        assert self.bc.cohomology_total() == 2**6

    def test_total_is_2_to_3g(self):
        """2^{3g} with g = 2 generators."""
        assert self.bc.cohomology_total() == 2 ** (3 * self.bc.num_generators)

    def test_euler_characteristic_zero(self):
        """chi(T^6) = 0."""
        assert self.bc.euler_characteristic() == 0

    def test_poincare_polynomial(self):
        """Poincare polynomial (1+t)^6 = [1, 6, 15, 20, 15, 6, 1]."""
        assert self.bc.cohomology_poincare() == [1, 6, 15, 20, 15, 6, 1]

    def test_poincare_symmetry(self):
        """Poincare duality: h_k = h_{6-k}."""
        poinc = self.bc.cohomology_poincare()
        for k in range(7):
            assert poinc[k] == poinc[6 - k]

    def test_vanishes_above_6(self):
        """H^n = 0 for n >= 7."""
        for n in range(7, 12):
            assert self.bc.cohomology_dimension(n) == 0

    def test_identical_to_betagamma_cohomology(self):
        """bc and betagamma have IDENTICAL E_3 bar cohomology."""
        bg = E3BarComplexBetaGamma()
        for n in range(12):
            assert self.bc.cohomology_dimension(n) == bg.cohomology_dimension(n)
        assert self.bc.cohomology_total() == bg.cohomology_total()
        assert self.bc.euler_characteristic() == bg.euler_characteristic()
        assert self.bc.cohomology_poincare() == bg.cohomology_poincare()


# =========================================================================
# 6. Spectral sequence: F(q)^6 -> (1+t)^2 F(q)^4 -> (1+t)^4 F(q)^2 -> (1+t)^6
# =========================================================================

class TestSpectralSequence:
    """Three-page spectral sequence for the bc E_3 bar."""

    def setup_method(self):
        self.bc = E3BarComplexBc()
        self.ss = self.bc.verify_spectral_sequence(7)

    @pytest.mark.parametrize("n", range(8))
    def test_e0_is_chain(self, n):
        """E_0 page = full chain complex = [q^n] F(q)^6."""
        assert self.ss[n]["E_0 (chain)"] == CHAIN_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_e1_generating_function(self, n):
        """E_1 page = (1+t)^2 * F(q)^4."""
        expected = sum(
            comb(2, k) * _fermionic_quadpartition_count(n - k)
            for k in range(min(3, n + 1))
        )
        assert self.ss[n]["E_1 (H(d_1))"] == expected

    @pytest.mark.parametrize("n", range(8))
    def test_e2_generating_function(self, n):
        """E_2 page = (1+t)^4 * F(q)^2."""
        expected = sum(
            comb(4, k) * _fermionic_bipartition_count(n - k)
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
# 7. Charge conservation: d_4 = 0 on E_3 page
# =========================================================================

class TestChargeConservation:
    """d_4 vanishes on E_3 page by charge parity mismatch.

    The argument is IDENTICAL for bc and betagamma:
    - Both have charge grading (A: +1, B: -1)
    - Lambda^n has charge parity n mod 2
    - d_4: Lambda^n -> Lambda^{n-3} maps parity n to parity n+1 (mod 2)
    - Charge-preserving => forced to zero
    """

    def setup_method(self):
        self.bc = E3BarComplexBc()

    def test_d4_vanishes(self):
        assert self.bc.d4_vanishes_on_e3_page

    def test_charge_parity_mismatch(self):
        """For each n, Lambda^n and Lambda^{n-3} have opposite charge parity."""
        for n in range(7):
            n3 = n - 3
            if n3 < 0:
                continue  # Lambda^{n-3} = 0, d_4 trivially zero
            parity_n = n % 2
            parity_n3 = n3 % 2
            assert parity_n != parity_n3, (
                f"n={n}: parity mismatch expected but got same parity"
            )

    def test_charge_sets_disjoint(self):
        """Explicit: the set of charges in Lambda^n and Lambda^{n-3} are disjoint by parity."""
        for n in range(3, 7):
            charges_n = set(range(-n, n + 1, 2))
            charges_n3 = set(range(-(n - 3), (n - 3) + 1, 2))
            assert charges_n.isdisjoint(charges_n3)

    def test_same_argument_as_betagamma(self):
        """bc and betagamma share the same d4_vanishes property."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.d4_vanishes_on_e3_page == bg.d4_vanishes_on_e3_page


# =========================================================================
# 8. Chain vs cohomology: differentials kill F(q)^6 - C(6,n)
# =========================================================================

class TestChainVsCohomology:
    """The nonzero differentials kill most of the chain complex."""

    def setup_method(self):
        self.bc = E3BarComplexBc()

    def test_arity_0_survives(self):
        assert self.bc.chain_dimension(0) == self.bc.cohomology_dimension(0) == 1

    def test_arity_1_survives(self):
        """At arity 1, all 6 generators survive."""
        assert self.bc.chain_dimension(1) == self.bc.cohomology_dimension(1) == 6

    def test_arity_2_kills_6(self):
        """At arity 2: 21 chain - 15 cohomology = 6 killed."""
        assert self.bc.chain_dimension(2) - self.bc.cohomology_dimension(2) == 6

    def test_arity_3_kills_42(self):
        """At arity 3: 62 chain - 20 cohomology = 42 killed."""
        assert self.bc.chain_dimension(3) - self.bc.cohomology_dimension(3) == 42

    def test_high_arity_almost_all_killed(self):
        """At arity >= 7, chain is completely exact."""
        for n in range(7, 8):
            assert self.bc.cohomology_dimension(n) == 0
            assert self.bc.chain_dimension(n) > 0

    def test_less_killing_than_betagamma(self):
        """bc has smaller chain => fewer elements to kill.

        At each n >= 2, the differentials kill fewer elements for bc than
        for betagamma, but achieve the SAME cohomology.
        """
        bg = E3BarComplexBetaGamma()
        for n in range(2, 8):
            bc_killed = self.bc.chain_dimension(n) - self.bc.cohomology_dimension(n)
            bg_killed = bg.chain_dimension(n) - bg.cohomology_dimension(n)
            assert bc_killed < bg_killed


# =========================================================================
# 9. kappa and Koszul conductor
# =========================================================================

class TestKappaAndConductor:
    """kappa_ch = 1/12, conductor rho_K = -5/12 (same as from betagamma side)."""

    def setup_method(self):
        self.bc = E3BarComplexBc()

    def test_kappa_ch(self):
        assert self.bc.kappa_ch() == Rational(1, 12)

    def test_kappa_ch_dual(self):
        """Koszul dual (betagamma) has kappa_ch = -1/2."""
        assert self.bc.kappa_ch_dual() == Rational(-1, 2)

    def test_koszul_conductor(self):
        """rho_K = 1/12 + (-1/2) = -5/12."""
        assert self.bc.koszul_conductor() == Rational(-5, 12)

    def test_conductor_nonzero(self):
        """Nonzero conductor: hallmark of class C."""
        assert self.bc.koszul_conductor() != 0

    def test_kappa_complementarity(self):
        """kappa + kappa^! = rho_K."""
        assert self.bc.verify_kappa_complementarity()

    def test_conductor_symmetric(self):
        """Koszul conductor is the same from either side of the duality."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.koszul_conductor() == bg.koszul_conductor()

    def test_kappa_ch_different_from_betagamma(self):
        """kappa_ch(bc) = 1/12 != kappa_ch(bg) = -1/2."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.kappa_ch() != bg.kappa_ch()

    def test_kappa_ch_sum_is_conductor(self):
        """kappa_ch(bc) + kappa_ch(bg) = rho_K."""
        bg = E3BarComplexBetaGamma()
        assert self.bc.kappa_ch() + bg.kappa_ch() == self.bc.koszul_conductor()


# =========================================================================
# 10. Universal (1+t)^{3g} across statistics: bc vs betagamma
# =========================================================================

class TestUniversalFormula:
    """The central result: (1+t)^{3g} holds for BOTH bc and betagamma.

    This confirms that the formula depends on:
    1. Koszul property (2 generators, 1 relation)
    2. Charge conservation (b: +1, c: -1)
    and NOT on:
    3. Statistics (bosonic vs fermionic)
    4. Chain-level dimensions (P(q)^6 vs F(q)^6)
    """

    def setup_method(self):
        self.bc = E3BarComplexBc()
        self.bg = E3BarComplexBetaGamma()

    def test_same_cohomology_total(self):
        """Both give 2^6 = 64."""
        assert self.bc.cohomology_total() == self.bg.cohomology_total() == 64

    def test_same_cohomology_poincare(self):
        """Both give (1+t)^6 = [1, 6, 15, 20, 15, 6, 1]."""
        assert self.bc.cohomology_poincare() == self.bg.cohomology_poincare()

    def test_same_euler_characteristic(self):
        """Both give chi = 0."""
        assert self.bc.euler_characteristic() == self.bg.euler_characteristic() == 0

    def test_same_2_to_3g(self):
        """Both satisfy 2^{3g} with g=2."""
        assert self.bc.cohomology_total() == 2 ** (3 * 2)
        assert self.bg.cohomology_total() == 2 ** (3 * 2)

    def test_different_chain_level(self):
        """Chain-level dimensions DIFFER: F(q)^6 != P(q)^6 for n >= 2."""
        for n in range(2, 8):
            assert self.bc.chain_dimension(n) != self.bg.chain_dimension(n)
            assert self.bc.chain_dimension(n) < self.bg.chain_dimension(n)

    def test_same_chain_at_low_weight(self):
        """At n=0,1: F(q)^6 = P(q)^6 (first difference at n=2)."""
        assert self.bc.chain_dimension(0) == self.bg.chain_dimension(0) == 1
        assert self.bc.chain_dimension(1) == self.bg.chain_dimension(1) == 6

    def test_same_e1_bar_per_direction(self):
        """E_1 bar cohomology per direction is (1+t)^2 for BOTH."""
        for n in range(8):
            assert (self.bc.e1_bar_cohomology_per_direction(n)
                    == self.bg.e1_bar_cohomology_per_direction(n))

    def test_same_d4_vanishing(self):
        """Charge conservation kills d_4 for BOTH."""
        assert self.bc.d4_vanishes_on_e3_page
        assert self.bg.d4_vanishes_on_e3_page

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_dimension_by_dimension(self, n):
        """Cohomology agrees dimension by dimension."""
        assert self.bc.cohomology_dimension(n) == self.bg.cohomology_dimension(n)


# =========================================================================
# 11. Contrast across all shadow classes
# =========================================================================

class TestContrastAcrossClasses:
    """The four classes G, L, C(bosonic), C(fermionic) in one view."""

    def setup_method(self):
        self.bc = E3BarComplexBc()
        self.bg = E3BarComplexBetaGamma()
        self.heisenberg = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        self.yangian = E3BarComplexYangian(OmegaBackground(1, 2))

    def test_shadow_depth_progression(self):
        assert self.heisenberg.shadow_depth == 2
        assert self.yangian.shadow_depth == 3
        assert self.bg.shadow_depth == 4
        assert self.bc.shadow_depth == 4

    def test_shadow_class_progression(self):
        assert self.heisenberg.shadow_class == "G"
        assert self.yangian.shadow_class == "L"
        assert self.bg.shadow_class == "C"
        assert self.bc.shadow_class == "C"

    def test_class_l_cohomology_8(self):
        """Class L (1 generator): 2^3 = 8."""
        assert self.yangian.cohomology_total() == 8

    def test_class_c_cohomology_64_both(self):
        """Class C (2 generators): 2^6 = 64, regardless of statistics."""
        assert self.bg.cohomology_total() == 64
        assert self.bc.cohomology_total() == 64

    def test_pattern_2_to_3g(self):
        """Pattern: 2^{3g} for class >= L, independent of statistics."""
        assert self.yangian.cohomology_total() == 2**(3 * 1)
        assert self.bg.cohomology_total() == 2**(3 * 2)
        assert self.bc.cohomology_total() == 2**(3 * 2)

    def test_fermionic_chain_between_class_l_and_bosonic_c(self):
        """F(q)^6 is between P(q)^3 and P(q)^6 for n >= 2."""
        for n in range(2, 7):
            heisenberg_chain = self.heisenberg.trigraded_dimension(n)
            bc_chain = self.bc.chain_dimension(n)
            bg_chain = self.bg.chain_dimension(n)
            assert heisenberg_chain < bc_chain < bg_chain


# =========================================================================
# 12. Fermionic vs bosonic chain-level structure
# =========================================================================

class TestFermionicVsBosonicChain:
    """Detailed comparison of F(q)^6 vs P(q)^6 at the chain level."""

    def test_f_leq_p_at_each_level(self):
        """F(q) <= P(q) at each weight (distinct parts <= all parts)."""
        for n in range(12):
            assert _distinct_partition_count(n) <= _partition_count(n)

    def test_f_equals_p_at_0_1(self):
        """F(q) = P(q) at q^0 and q^1."""
        assert _distinct_partition_count(0) == _partition_count(0) == 1
        assert _distinct_partition_count(1) == _partition_count(1) == 1

    def test_f_strictly_less_from_2(self):
        """F(q) < P(q) at q^n for n >= 2 (partitions 2=1+1 exists but is not distinct)."""
        for n in range(2, 12):
            assert _distinct_partition_count(n) < _partition_count(n)

    @pytest.mark.parametrize("n", range(2, 8))
    def test_fermionic_hexapartition_strictly_less(self, n):
        """F(q)^6 < P(q)^6 for n >= 2."""
        assert _fermionic_hexapartition_count(n) < _hexapartition_count(n)

    def test_ratio_grows(self):
        """P(q)^6 / F(q)^6 increases with n (bosonic growth >> fermionic)."""
        for n in range(2, 7):
            ratio_n = _hexapartition_count(n) / _fermionic_hexapartition_count(n)
            ratio_n1 = _hexapartition_count(n+1) / _fermionic_hexapartition_count(n+1)
            assert ratio_n1 > ratio_n

    def test_both_agree_at_n0_n1(self):
        """At n=0,1: hexapartitions agree (no multi-occupation at weight 1)."""
        assert _fermionic_hexapartition_count(0) == _hexapartition_count(0)
        assert _fermionic_hexapartition_count(1) == _hexapartition_count(1)
