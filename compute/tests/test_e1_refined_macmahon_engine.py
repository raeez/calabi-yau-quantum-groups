"""Tests for e1_refined_macmahon_engine: refined MacMahon partition function
at generic Omega-background parameter alpha.

Claims tested:
1. Staircase multiplicity mu(n; alpha) = floor((n-1)/alpha) + 1
2. alpha=1 recovers MacMahon M(q) (OEIS A000219)
3. alpha->inf recovers Euler P(q) (OEIS A000041)
4. Two independent implementations (cumulative-sum vs binomial) agree
5. Shadow invariants: sigma_2 = -(alpha^2+alpha+1), sigma_3 = -alpha*(alpha+1)
6. E1 correction is negative at degrees >= 2 for alpha >= 2
7. Bar Euler characteristic: 1/Z has integer coefficients
8. Total multiplicity at alpha=1 equals n*(n+1)/2

Ground truth:
    MacMahon: OEIS A000219 = 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500
    Partitions: OEIS A000041 = 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
"""

import pytest

from compute.lib.e1_refined_macmahon_engine import (
    staircase_multiplicity,
    staircase_multiplicities,
    shadow_invariants,
    e1_partition_function,
    e1_partition_function_binomial,
    macmahon_coefficients,
    partition_coefficients,
    e1_correction,
    limiting_correction,
    bar_euler_characteristic,
    total_multiplicity,
)


# ======================================================================
# 1. Staircase multiplicity
# ======================================================================

class TestStaircaseMultiplicity:
    """Verify mu(n; alpha) = floor((n-1)/alpha) + 1."""

    def test_alpha_1_gives_n(self):
        """At alpha=1, mu(n;1) = n for all n >= 1."""
        for n in range(1, 20):
            # VERIFIED [DC] staircase formula [LT] refined MacMahon theory
            assert staircase_multiplicity(n, 1) == n

    def test_alpha_2_values(self):
        """At alpha=2: mu = 1,1,2,2,3,3,4,4,..."""
        expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        for n in range(1, 11):
            assert staircase_multiplicity(n, 2) == expected[n - 1]

    def test_alpha_3_values(self):
        """At alpha=3: mu = 1,1,1,2,2,2,3,3,3,..."""
        expected = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
        for n in range(1, 11):
            assert staircase_multiplicity(n, 3) == expected[n - 1]

    def test_large_alpha_gives_1(self):
        """At alpha >= n, mu(n; alpha) = 1."""
        for n in range(1, 10):
            assert staircase_multiplicity(n, 100) == 1

    def test_invalid_inputs(self):
        """n < 1 or alpha < 1 should raise ValueError."""
        with pytest.raises(ValueError):
            staircase_multiplicity(0, 1)
        with pytest.raises(ValueError):
            staircase_multiplicity(1, 0)

    def test_multiplicities_list_starts_with_zero(self):
        """staircase_multiplicities includes mu(0) = 0."""
        mults = staircase_multiplicities(1, 5)
        assert mults[0] == 0
        assert mults[1:] == [1, 2, 3, 4, 5]


# ======================================================================
# 2. Shadow invariants
# ======================================================================

class TestShadowInvariants:
    """Verify sigma_2, sigma_3, kappa at the SV point."""

    def test_alpha_1_isotropic(self):
        """At alpha=1: sigma_2=-3, sigma_3=-2, kappa=3."""
        inv = shadow_invariants(1)
        # VERIFIED [DC] shadow invariant [LT] E1 refined MacMahon theory
        assert inv['sigma2'] == -3
        assert inv['sigma3'] == -2
        assert inv['kappa'] == 3

    def test_alpha_2(self):
        """At alpha=2: sigma_2=-7, sigma_3=-6, kappa=7."""
        inv = shadow_invariants(2)
        assert inv['sigma2'] == -7
        assert inv['sigma3'] == -6
        assert inv['kappa'] == 7

    def test_h_sum_zero(self):
        """CY condition: h1 + h2 + h3 = 0 for all alpha."""
        for alpha in range(1, 10):
            inv = shadow_invariants(alpha)
            assert sum(inv['h']) == 0

    def test_kappa_formula(self):
        """kappa = alpha^2 + alpha + 1 for all alpha."""
        for alpha in range(1, 10):
            inv = shadow_invariants(alpha)
            assert inv['kappa'] == alpha ** 2 + alpha + 1

    def test_sigma3_formula(self):
        """sigma_3 = -alpha*(alpha+1)."""
        for alpha in range(1, 10):
            inv = shadow_invariants(alpha)
            assert inv['sigma3'] == -alpha * (alpha + 1)

    def test_depth_nonzero_sigma3(self):
        """Depth is 'M' when sigma_3 != 0 (all alpha >= 1)."""
        for alpha in range(1, 10):
            inv = shadow_invariants(alpha)
            assert inv['depth'] == 'M'


# ======================================================================
# 3. Partition function: alpha=1 -> MacMahon
# ======================================================================

class TestMacMahonRecovery:
    """Verify Z^{E1}(q; alpha=1) = M(q) = plane partition generating function."""

    OEIS_A000219 = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]

    def test_macmahon_oeis(self):
        """MacMahon coefficients match OEIS A000219."""
        M = macmahon_coefficients(10)
        # VERIFIED [DC] partition function coefficient [LT] MacMahon theory
        assert M[:11] == self.OEIS_A000219

    def test_alpha_1_equals_macmahon(self):
        """e1_partition_function(alpha=1) = macmahon_coefficients."""
        Z1 = e1_partition_function(1, 15)
        M = macmahon_coefficients(15)
        assert Z1 == M


# ======================================================================
# 4. Partition function: large alpha -> Euler partitions
# ======================================================================

class TestEulerRecovery:
    """Verify large-alpha limit recovers ordinary partition function."""

    OEIS_A000041 = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]

    def test_partition_oeis(self):
        """Partition coefficients match OEIS A000041."""
        P = partition_coefficients(10)
        # VERIFIED [DC] partition function coefficient [LT] Euler partition theory
        assert P[:11] == self.OEIS_A000041

    def test_large_alpha_approaches_partitions(self):
        """Z^{E1}(q; alpha) -> P(q) as alpha -> inf (checked at alpha=100)."""
        Z_large = e1_partition_function(100, 10)
        P = partition_coefficients(10)
        assert Z_large[:11] == P[:11]


# ======================================================================
# 5. Two-path agreement
# ======================================================================

class TestTwoPathAgreement:
    """Verify cumulative-sum and binomial implementations agree."""

    def test_path_agreement_alpha_1(self):
        """Paths 1 and 2 agree at alpha=1 through q^20."""
        Z1 = e1_partition_function(1, 20)
        Z2 = e1_partition_function_binomial(1, 20)
        assert Z1 == Z2

    def test_path_agreement_alpha_2(self):
        """Paths 1 and 2 agree at alpha=2 through q^20."""
        Z1 = e1_partition_function(2, 20)
        Z2 = e1_partition_function_binomial(2, 20)
        assert Z1 == Z2

    def test_path_agreement_alpha_3(self):
        """Paths 1 and 2 agree at alpha=3 through q^20."""
        Z1 = e1_partition_function(3, 20)
        Z2 = e1_partition_function_binomial(3, 20)
        assert Z1 == Z2

    def test_path_agreement_alpha_5(self):
        """Paths 1 and 2 agree at alpha=5 through q^15."""
        Z1 = e1_partition_function(5, 15)
        Z2 = e1_partition_function_binomial(5, 15)
        assert Z1 == Z2


# ======================================================================
# 6. E1 correction negativity
# ======================================================================

class TestE1Correction:
    """Verify Delta^{E1} is negative at degrees >= 2 for alpha >= 2."""

    def test_correction_negative_alpha_2(self):
        """E1 correction negative at all degrees 2..15 for alpha=2."""
        delta = e1_correction(2, 15)
        assert delta[0] == 0
        assert delta[1] == 0
        for k in range(2, 16):
            assert delta[k] < 0, f"delta[{k}] = {delta[k]} should be < 0"

    def test_correction_negative_alpha_3(self):
        """E1 correction negative at all degrees 2..15 for alpha=3."""
        delta = e1_correction(3, 15)
        for k in range(2, 16):
            assert delta[k] < 0

    def test_limiting_correction_values(self):
        """lim_{alpha->inf} Delta = P(q) - M(q) known values."""
        lim = limiting_correction(10)
        assert lim[0] == 0
        assert lim[1] == 0
        # P(2) - M(2) = 2 - 3 = -1
        assert lim[2] == -1
        # P(3) - M(3) = 3 - 6 = -3
        assert lim[3] == -3


# ======================================================================
# 7. Bar Euler characteristic integrality
# ======================================================================

class TestBarEulerCharacteristic:
    """Verify 1/Z has integer coefficients (bar differential structure)."""

    def test_integrality_alpha_1(self):
        """Bar Euler characteristic at alpha=1 is integer-valued."""
        chi = bar_euler_characteristic(1, 15)
        for k in range(16):
            assert isinstance(chi[k], int)

    def test_integrality_alpha_2(self):
        """Bar Euler characteristic at alpha=2 is integer-valued."""
        chi = bar_euler_characteristic(2, 15)
        for k in range(16):
            assert isinstance(chi[k], int)

    def test_chi_starts_1(self):
        """chi[0] = 1 (constant term of 1/Z)."""
        for alpha in [1, 2, 3]:
            chi = bar_euler_characteristic(alpha, 5)
            assert chi[0] == 1


# ======================================================================
# 8. Total multiplicity
# ======================================================================

class TestTotalMultiplicity:
    """Verify sum of multiplicities at special values."""

    def test_alpha_1_triangular(self):
        """At alpha=1, total = n*(n+1)/2."""
        for N in [5, 10, 20]:
            assert total_multiplicity(1, N) == N * (N + 1) // 2

    def test_large_alpha_linear(self):
        """At alpha >= max_n, total = max_n."""
        for N in [5, 10, 20]:
            assert total_multiplicity(1000, N) == N
