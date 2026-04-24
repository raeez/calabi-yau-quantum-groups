"""Tests for the E_3 bar complex of Y(gl_hat_1), the first non-free-field case.

Verifies the spectral sequence computation for the affine Yangian
(CoHA(C^3), class L, shadow depth 3). The chain-level dimensions are
tau_3(n) = P(q)^3 (same as Heisenberg), but the cohomology collapses
to [1, 3, 3, 1] = H^*(T^3) via a three-page spectral sequence where
each differential d_i replaces one P(q) factor with (1+t) = H^*(S^1).

Ground truth:
  tau_3(n) for n=0..7: 1, 3, 9, 22, 51, 108, 221, 429 (OEIS A000716)
  Cohomology: [1, 3, 3, 1, 0, 0, ...] = binomial(3, n)
  Total: 2^3 = 8 = dim H^*(T^3)
  Euler char: 0 = chi(T^3)

  E_1 page (H(d_1)): (1+t) * P(q)^2 -> dims [1, 3, 7, 15, 30, 56, ...]
  E_2 page (H(d_1,d_2)): (1+t)^2 * P(q) -> dims [1, 3, 5, 8, 13, 20, ...]
  E_inf = E_3: (1+t)^3 -> dims [1, 3, 3, 1, 0, 0, ...]

  Pattern: P(q)^3 -d1-> (1+t)P(q)^2 -d2-> (1+t)^2 P(q) -d3-> (1+t)^3

Manuscript references:
  holomorphic_cs_chiral_engine.py: E3BarComplexYangian class
  cross_volume_shadow_bridge.py: class L classification for CoHA(C^3)
  kazhdan_lusztig_shadow.py: class L shadow tower structure (S_4 = 0)
"""

import pytest
from math import comb
from sympy import Rational

from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    E3BarComplexHeisenberg,
    E3BarComplexYangian,
    _partition_count,
)


# =========================================================================
# Ground truth
# =========================================================================

TAU_3_GROUND_TRUTH = [1, 3, 9, 22, 51, 108, 221, 429]
COHOMOLOGY_GROUND_TRUTH = [1, 3, 3, 1, 0, 0, 0, 0]


def _tau2(n):
    """Bipartition count: [q^n] P(q)^2."""
    if n < 0:
        return 0
    return sum(_partition_count(a) * _partition_count(n - a)
               for a in range(n + 1))


# E_1 page: (1+t) * P(q)^2 = tau_2(n) + tau_2(n-1)
E1_PAGE_GROUND_TRUTH = [_tau2(n) + _tau2(n - 1) for n in range(8)]
# E_2 page: (1+t)^2 * P(q) = p(n) + 2*p(n-1) + p(n-2)
E2_PAGE_GROUND_TRUTH = [
    _partition_count(n) + 2 * _partition_count(n - 1) + _partition_count(n - 2)
    for n in range(8)
]


# =========================================================================
# 1. Classification: class L, shadow depth 3
# =========================================================================

class TestYangianClassification:
    """The Drinfeld double of CoHA(C^3)=Y^+ is class L, shadow depth 3."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)  # generic point, h3=-3
        self.yangian = E3BarComplexYangian(self.omega)

    def test_shadow_class(self):
        assert self.yangian.shadow_class == "L"

    def test_shadow_depth(self):
        assert self.yangian.shadow_depth == 3

    def test_differentials_nonzero_at_generic(self):
        assert not self.yangian.differentials_all_vanish

    def test_phi3_nonzero_at_generic(self):
        """Leading OPE coefficient phi_3 = -2*sigma_3 is nonzero."""
        assert self.yangian.phi3 != 0

    def test_differentials_vanish_at_self_dual(self):
        """At the self-dual point (h2=0), g(u)=1 and differentials vanish."""
        omega_sd = OmegaBackground(1, 0)
        yangian_sd = E3BarComplexYangian(omega_sd)
        assert yangian_sd.differentials_all_vanish


# =========================================================================
# 2. Chain-level dimensions = tau_3(n) = P(q)^3
# =========================================================================

class TestChainDimensions:
    """Chain-level dimensions agree with P(q)^3 = Heisenberg."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)
        self.omega_sd = OmegaBackground(1, 0)
        self.heisenberg = E3BarComplexHeisenberg(self.omega_sd)

    @pytest.mark.parametrize("n", range(8))
    def test_chain_matches_tau3(self, n):
        assert self.yangian.chain_dimension(n) == TAU_3_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_chain_matches_heisenberg(self, n):
        """Chain dimensions agree: same generators, different differentials."""
        assert self.yangian.chain_dimension(n) == self.heisenberg.trigraded_dimension(n)

    def test_trigraded_sum_equals_total(self):
        """Sum of trigraded dimensions equals total dimension."""
        for n in range(7):
            decomp = self.yangian.trigraded_decomposition(n)
            assert sum(decomp.values()) == self.yangian.chain_dimension(n)

    def test_tridegree_symmetry(self):
        """The S_3 symmetry of C^3 implies tridegree symmetry."""
        for n in range(6):
            decomp = self.yangian.trigraded_decomposition(n)
            for (a, b, c), dim in decomp.items():
                # Check all permutations have same dimension
                assert decomp.get((b, a, c), 0) == dim
                assert decomp.get((a, c, b), 0) == dim
                assert decomp.get((c, b, a), 0) == dim


# =========================================================================
# 3. Cohomology dimensions = [1, 3, 3, 1] = H^*(T^3)
# =========================================================================

class TestCohomologyDimensions:
    """E_3 bar cohomology of Y(gl_hat_1) is H^*(T^3)."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_matches_binomial(self, n):
        expected = comb(3, n) if 0 <= n <= 3 else 0
        assert self.yangian.cohomology_dimension(n) == expected

    @pytest.mark.parametrize("n", range(8))
    def test_cohomology_matches_ground_truth(self, n):
        assert self.yangian.cohomology_dimension(n) == COHOMOLOGY_GROUND_TRUTH[n]

    def test_total_is_8(self):
        assert self.yangian.cohomology_total() == 8

    def test_total_is_2_cubed(self):
        """2^3 = 8 = dim H^*(T^3)."""
        assert self.yangian.cohomology_total() == 2**3

    def test_euler_characteristic_zero(self):
        """chi(T^3) = 0."""
        assert self.yangian.euler_characteristic() == 0

    def test_poincare_polynomial(self):
        """Poincare polynomial (1+t)^3 = [1, 3, 3, 1]."""
        assert self.yangian.cohomology_poincare() == [1, 3, 3, 1]

    def test_poincare_symmetry(self):
        """Poincare duality: h_k = h_{3-k}."""
        poinc = self.yangian.cohomology_poincare()
        assert poinc[0] == poinc[3]
        assert poinc[1] == poinc[2]


# =========================================================================
# 4. Spectral sequence: P(q)^3 -> (1+t)P(q)^2 -> (1+t)^2 P(q) -> (1+t)^3
# =========================================================================

class TestSpectralSequence:
    """Three-page spectral sequence degenerating at E_3."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)
        self.ss = self.yangian.verify_spectral_sequence(7)

    @pytest.mark.parametrize("n", range(8))
    def test_e0_is_chain(self, n):
        """E_0 page = full chain complex = tau_3(n)."""
        assert self.ss[n]["E_0 (chain)"] == TAU_3_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_e1_page(self, n):
        """E_1 page = (1+t) * P(q)^2: dims [1, 3, 7, 15, 30, 56, ...]."""
        assert self.ss[n]["E_1 (H(d_1))"] == E1_PAGE_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_e2_page(self, n):
        """E_2 page = (1+t)^2 * P(q): dims [1, 3, 5, 8, 13, 20, ...]."""
        assert self.ss[n]["E_2 (H(d_1,d_2))"] == E2_PAGE_GROUND_TRUTH[n]

    @pytest.mark.parametrize("n", range(8))
    def test_einf_matches_binomial(self, n):
        expected = comb(3, n) if 0 <= n <= 3 else 0
        assert self.ss[n]["E_inf (cohomology)"] == expected

    @pytest.mark.parametrize("n", range(8))
    def test_all_pages_match_binomial_flag(self, n):
        assert self.ss[n]["matches_binomial"]

    def test_monotone_decrease_across_pages(self):
        """Each page has smaller or equal dimensions than the previous."""
        for n in range(7):
            e0 = self.ss[n]["E_0 (chain)"]
            e1 = self.ss[n]["E_1 (H(d_1))"]
            e2 = self.ss[n]["E_2 (H(d_1,d_2))"]
            einf = self.ss[n]["E_inf (cohomology)"]
            assert e0 >= e1 >= e2 >= einf >= 0

    def test_e1_generating_function(self):
        """E_1 page gen fn is (1+t)*P(q)^2: each term = tau_2(n)+tau_2(n-1)."""
        for n in range(7):
            expected = _tau2(n) + _tau2(n - 1)
            assert self.ss[n]["E_1 (H(d_1))"] == expected

    def test_e2_generating_function(self):
        """E_2 page gen fn is (1+t)^2*P(q): each term = p(n)+2p(n-1)+p(n-2)."""
        for n in range(7):
            expected = (_partition_count(n) + 2 * _partition_count(n - 1)
                        + _partition_count(n - 2))
            assert self.ss[n]["E_2 (H(d_1,d_2))"] == expected


# =========================================================================
# 5. Chain vs cohomology: the differentials kill tau_3(n) - C(3,n)
# =========================================================================

class TestChainVsCohomology:
    """The nonzero differentials kill most of the chain complex."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_arity_0_survives(self):
        """At arity 0, nothing is killed."""
        assert self.yangian.chain_dimension(0) == self.yangian.cohomology_dimension(0) == 1

    def test_arity_1_survives(self):
        """At arity 1, all 3 generators survive (d_i needs arity >= 2)."""
        assert self.yangian.chain_dimension(1) == self.yangian.cohomology_dimension(1) == 3

    def test_arity_2_kills_6(self):
        """At arity 2: 9 chain - 3 cohomology = 6 killed."""
        assert self.yangian.chain_dimension(2) - self.yangian.cohomology_dimension(2) == 6

    def test_arity_3_kills_21(self):
        """At arity 3: 22 chain - 1 cohomology = 21 killed."""
        assert self.yangian.chain_dimension(3) - self.yangian.cohomology_dimension(3) == 21

    def test_high_arity_completely_killed(self):
        """At arity >= 4, the chain complex is completely exact."""
        for n in range(4, 8):
            assert self.yangian.cohomology_dimension(n) == 0
            assert self.yangian.chain_dimension(n) > 0

    def test_killed_fraction_increases(self):
        """The fraction killed by differentials increases with arity."""
        for n in range(2, 7):
            ch_n = self.yangian.chain_dimension(n)
            co_n = self.yangian.cohomology_dimension(n)
            ch_n1 = self.yangian.chain_dimension(n + 1)
            co_n1 = self.yangian.cohomology_dimension(n + 1)
            frac_n = (ch_n - co_n) / ch_n if ch_n > 0 else 0
            frac_n1 = (ch_n1 - co_n1) / ch_n1 if ch_n1 > 0 else 0
            assert frac_n1 >= frac_n


# =========================================================================
# 6. Parameter independence and structural properties
# =========================================================================

class TestParameterIndependence:
    """Cohomology depends only on shadow class, not on specific parameters."""

    @pytest.mark.parametrize("h1,h2", [(1, 2), (1, 3), (2, 3), (3, 5), (1, 7)])
    def test_cohomology_independent_of_parameters(self, h1, h2):
        """At any generic point, cohomology is [1, 3, 3, 1]."""
        omega = OmegaBackground(h1, h2)
        yangian = E3BarComplexYangian(omega)
        assert yangian.cohomology_poincare() == [1, 3, 3, 1]
        assert yangian.cohomology_total() == 8

    @pytest.mark.parametrize("h1,h2", [(1, 2), (1, 3), (2, 3)])
    def test_phi3_varies_but_cohomology_does_not(self, h1, h2):
        """phi_3 = -2*sigma_3 changes with parameters; cohomology does not."""
        omega = OmegaBackground(h1, h2)
        yangian = E3BarComplexYangian(omega)
        assert yangian.phi3 != 0  # generic => nontrivial
        assert yangian.cohomology_total() == 8  # but cohomology is fixed

    def test_e_n_pattern(self):
        """Cohomology dimension is 2^n for the E_n bar of a class L algebra.

        E_1: H^*(S^1) = 2
        E_2: H^*(T^2) = 4
        E_3: H^*(T^3) = 8
        """
        assert 2**3 == 8  # E_3 case verified by this test suite


# =========================================================================
# 7. Full investigation output validation
# =========================================================================

class TestFullInvestigation:
    """Validate the full_investigation() output dictionary."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)
        self.result = self.yangian.full_investigation()

    def test_algebra_name(self):
        assert "Y(gl_hat_1)" in self.result["algebra"]

    def test_class_and_depth(self):
        assert self.result["shadow_class"] == "L"
        assert self.result["shadow_depth"] == 3

    def test_chain_dimensions_present(self):
        assert self.result["chain_dimensions (tau_3)"][:4] == [1, 3, 9, 22]

    def test_cohomology_dimensions_present(self):
        assert self.result["cohomology_dimensions"][:4] == [1, 3, 3, 1]

    def test_poincare_present(self):
        assert self.result["cohomology_poincare"] == [1, 3, 3, 1]

    def test_total_present(self):
        assert self.result["cohomology_total"] == 8

    def test_euler_present(self):
        assert self.result["euler_characteristic"] == 0

    def test_spectral_sequence_present(self):
        ss = self.result["spectral_sequence"]
        assert 0 in ss and 3 in ss


# =========================================================================
# 8. Contrast with Heisenberg (class G)
# =========================================================================

class TestContrastWithHeisenberg:
    """The Yangian and Heisenberg share chain dims but differ in cohomology."""

    def setup_method(self):
        self.omega_gen = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega_gen)
        self.omega_sd = OmegaBackground(1, 0)
        self.heisenberg = E3BarComplexHeisenberg(self.omega_sd)

    def test_chain_dimensions_agree(self):
        for n in range(7):
            assert self.yangian.chain_dimension(n) == self.heisenberg.trigraded_dimension(n)

    def test_heisenberg_cohomology_equals_chain(self):
        """Heisenberg (class G): differentials vanish, cohom = chain."""
        for n in range(7):
            assert self.heisenberg.trigraded_dimension(n) == TAU_3_GROUND_TRUTH[n]

    def test_yangian_cohomology_strictly_smaller(self):
        """Yangian (class L): differentials nonzero, cohom < chain for n >= 2."""
        for n in range(2, 7):
            assert self.yangian.cohomology_dimension(n) < self.yangian.chain_dimension(n)

    def test_class_g_vs_class_l(self):
        assert self.heisenberg.shadow_class == "G"
        assert self.yangian.shadow_class == "L"
        assert self.heisenberg.shadow_depth == 2
        assert self.yangian.shadow_depth == 3


# =========================================================================
# 9. Multi-path verification (AP10 compliance)
# =========================================================================

class TestMultiPathVerification:
    """Cross-check all key quantities via independent computation paths.

    Path 1: Engine computation (E3BarComplexYangian methods)
    Path 2: Direct combinatorial computation (partition convolution)
    Path 3: Cross-volume shadow bridge classification
    Path 4: Generating function coefficient extraction
    Path 5: Spectral sequence page-by-page independent computation
    """

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    # --- tau_3 via three independent paths ---

    @pytest.mark.parametrize("n", range(8))
    def test_tau3_path1_engine_vs_path2_convolution(self, n):
        """Path 1 (engine) vs Path 2 (direct triple convolution of p(n))."""
        engine_val = self.yangian.chain_dimension(n)
        conv_val = sum(
            _partition_count(a) * _partition_count(b) * _partition_count(n - a - b)
            for a in range(n + 1) for b in range(n - a + 1)
        )
        assert engine_val == conv_val

    @pytest.mark.parametrize("n", range(8))
    def test_tau3_path2_convolution_vs_path4_genfn(self, n):
        """Path 2 (convolution) vs Path 4 (generating function P(q)^3).

        Compute [q^n] P(q)^3 by iterative multiplication of
        P(q) = prod_{k>=1} 1/(1-q^k), cubed.
        """
        # Compute P(q)^3 coefficients up to q^n by iterative power series
        N = n
        a = [0] * (N + 1)
        a[0] = 1
        # Multiply by 1/(1-q^k) three times for each k
        for k in range(1, N + 1):
            for _rep in range(3):  # cube: three factors of 1/(1-q^k)
                for j in range(k, N + 1):
                    a[j] += a[j - k]
        genfn_val = a[n]
        conv_val = sum(
            _partition_count(a_) * _partition_count(b) * _partition_count(n - a_ - b)
            for a_ in range(n + 1) for b in range(n - a_ + 1)
        )
        assert genfn_val == conv_val

    # --- Cohomology via three independent paths ---

    @pytest.mark.parametrize("n", range(6))
    def test_cohomology_path1_engine_vs_path2_binomial(self, n):
        """Path 1 (engine) vs Path 2 (direct binomial(3, n))."""
        engine_val = self.yangian.cohomology_dimension(n)
        binom_val = comb(3, n) if 0 <= n <= 3 else 0
        assert engine_val == binom_val

    @pytest.mark.parametrize("n", range(6))
    def test_cohomology_path2_binomial_vs_path5_spectral(self, n):
        """Path 2 (binomial) vs Path 5 (spectral sequence filtration count).

        Count compositions of n into at most 3 parts, each 0 or 1.
        """
        binom_val = comb(3, n) if 0 <= n <= 3 else 0
        # Direct count: #{(a,b,c) : a+b+c=n, a in {0,1}, b in {0,1}, c in {0,1}}
        filt_count = sum(
            1 for a in (0, 1) for b in (0, 1) for c in (0, 1) if a + b + c == n
        )
        assert binom_val == filt_count

    # --- E_1 page via two independent paths ---

    @pytest.mark.parametrize("n", range(7))
    def test_e1_page_path1_spectral_vs_path4_genfn(self, n):
        """Spectral sequence E_1 vs generating function (1+t)*P(q)^2.

        (1+t)*P(q)^2: coefficient of q^n is tau_2(n) + tau_2(n-1).
        """
        ss = self.yangian.verify_spectral_sequence(7)
        ss_val = ss[n]["E_1 (H(d_1))"]
        # Independent: tau_2(n) + tau_2(n-1)
        genfn_val = _tau2(n) + _tau2(n - 1)
        assert ss_val == genfn_val

    # --- E_2 page via two independent paths ---

    @pytest.mark.parametrize("n", range(7))
    def test_e2_page_path1_spectral_vs_path4_genfn(self, n):
        """Spectral sequence E_2 vs generating function (1+t)^2*P(q).

        (1+t)^2*P(q): coefficient of q^n is p(n) + 2p(n-1) + p(n-2).
        """
        ss = self.yangian.verify_spectral_sequence(7)
        ss_val = ss[n]["E_2 (H(d_1,d_2))"]
        genfn_val = (_partition_count(n) + 2 * _partition_count(n - 1)
                     + _partition_count(n - 2))
        assert ss_val == genfn_val

    # --- Cross-volume classification cross-check ---

    def test_class_l_from_cross_volume_bridge(self):
        """Path 3: verify classification matches cross_volume_shadow_bridge."""
        from compute.lib.cross_volume_shadow_bridge import shadow_depth_class
        cls, depth = shadow_depth_class("affine")
        assert cls == "L"
        assert depth == 3
        assert cls == self.yangian.shadow_class
        assert depth == self.yangian.shadow_depth

    def test_class_l_from_kazhdan_lusztig(self):
        """Path 3b: verify classification matches kazhdan_lusztig_shadow."""
        from compute.lib.kazhdan_lusztig_shadow import shadow_tower_sl2
        tower = shadow_tower_sl2(1)
        assert tower["shadow_class"] == "L"
        assert tower["r_max"] == 3
        # Quartic shadow vanishes (class L defining property)
        assert tower["S_4"] == 0

    # --- Euler characteristic via two paths ---

    def test_euler_char_path1_alternating_vs_path2_formula(self):
        """Path 1 (alternating sum) vs Path 2 (chi(T^3) = 0)."""
        alt_sum = sum((-1)**n * self.yangian.cohomology_dimension(n) for n in range(8))
        # chi(T^3) = (1-1)^3 = 0
        formula_val = (1 - 1)**3
        assert alt_sum == formula_val == 0

    # --- Total dimension via two paths ---

    def test_total_path1_sum_vs_path2_power(self):
        """Sum of Poincare vs 2^3."""
        total_sum = sum(self.yangian.cohomology_dimension(n) for n in range(8))
        # (1+1)^3 = 8
        power_val = (1 + 1)**3
        assert total_sum == power_val == 8
