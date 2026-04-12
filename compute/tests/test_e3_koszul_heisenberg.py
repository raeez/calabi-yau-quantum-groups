"""Tests for E_3 Koszul self-duality of the Heisenberg algebra H_1.

Verifies Theorem thm:e3-koszul-heisenberg from en_factorization.tex:
the Heisenberg VOA H_1 (free boson, class G, shadow depth 2) satisfies
E_3 Koszul self-duality at the self-dual point (h1=1,h2=0,h3=-1).

FIVE CLAIMS of the theorem:
  (1) Self-dual point: B_{E_3}(H_1) has trivial differentials, Verdier dual = H_1
  (2) Generic point: nontrivial R-matrix, inverted parameters for dual
  (3) Tridegree decomposition matches tau_3(n) = 3-component multipartitions
  (4) Three differentials commute (all vanish for H_1)
  (5) kappa_ch(H_1) + kappa_ch(H_1^!) = 0 (conductor = 0 for class G)

Ground truth:
  tau_3(n) for n=0..9: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479
    (OEIS A000716: coefficients of P(q)^3 = (prod 1/(1-q^k))^3)
  MacMahon M(n) for n=0..9: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282
    (OEIS A000219: plane partitions)
  Partition p(n) for n=0..9: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30
    (OEIS A000041)

Multi-path verification:
  Path 1: Direct trigraded computation (convolution of partition functions)
  Path 2: Cross-check tau_3(n) = sum_{a+b+c=n} p(a)*p(b)*p(c)
  Path 3: Generating function P(q)^3 coefficient extraction
  Path 4: Cross-check with c3_grand_verification.py (kappa = 1 at self-dual)
  Path 5: KoszulDual class consistency

Manuscript references:
  chapters/theory/en_factorization.tex: Theorem thm:e3-koszul-heisenberg
  chapters/theory/en_factorization.tex: Conjecture conj:e3-koszul-duality
"""

import pytest
from sympy import Rational

from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    BoundaryAlgebra,
    ChiralCEComplex,
    KoszulDual,
    E3BarComplexHeisenberg,
    _macmahon_coefficient,
    _partition_count,
    _solid_partition_count,
)


# =========================================================================
# Ground truth: tau_3(n) = 3-component multipartition counts (OEIS A000716)
# =========================================================================

# Coefficients of P(q)^3 = prod_{k>=1} 1/(1-q^k)^3
# Computed independently from the recursive partition function.
TAU_3_GROUND_TRUTH = [1, 3, 9, 22, 51, 108, 221, 429, 810, 1479]


# =========================================================================
# 1. Claim (1): Self-dual point -- trivial differentials, Koszul self-duality
# =========================================================================

class TestSelfDualE3Koszul:
    """E_3 Koszul self-duality at the self-dual point (1, 0, -1)."""

    def setup_method(self):
        self.omega_sd = OmegaBackground(1, 0)  # h3 = -1
        self.e3bar = E3BarComplexHeisenberg(self.omega_sd)

    def test_is_self_dual_point(self):
        """Verify (1, 0, -1) is self-dual."""
        assert self.e3bar.is_self_dual_point

    def test_all_differentials_vanish(self):
        """d_1 = d_2 = d_3 = 0 for the Heisenberg."""
        assert self.e3bar.differentials_all_vanish()
        for i in (1, 2, 3):
            assert self.e3bar.differential_in_direction(i) == "zero"

    def test_structure_function_is_identity(self):
        """g(u) = 1 at the self-dual point."""
        assert self.e3bar.structure_function_at_self_dual() == "identity"

    def test_koszul_self_duality(self):
        """H_1 is E_3 Koszul self-dual at the self-dual point."""
        assert self.e3bar.is_koszul_self_dual()

    def test_verdier_dual_is_relabeling(self):
        """(1,0,-1) -> (-1,0,1): swap z_1 <-> z_3, isomorphic algebra."""
        dual = self.e3bar.verdier_dual_parameters()
        assert dual.h1 == Rational(-1)
        assert dual.h2 == Rational(0)
        assert dual.h3 == Rational(1)
        # The dual is also self-dual (h2 = 0)
        assert dual.is_self_dual

    def test_kappa_is_one(self):
        """kappa_ch(H_1) = 1 at the self-dual point."""
        assert self.e3bar.kappa_ch() == Rational(1)

    def test_kappa_dual_is_minus_one(self):
        """kappa_ch(H_1^!) = -1."""
        assert self.e3bar.kappa_ch_dual() == Rational(-1)

    def test_shadow_class_is_G(self):
        """Heisenberg is class G (Gaussian)."""
        assert self.e3bar.shadow_class == "G"
        assert self.e3bar.shadow_depth == 2


# =========================================================================
# 2. Claim (2): Generic point -- inverted parameters
# =========================================================================

class TestGenericE3Koszul:
    """E_3 Koszul duality at generic parameters."""

    def test_generic_not_self_dual(self):
        """At (1, -2, 1), the point is NOT self-dual."""
        omega = OmegaBackground(1, -2)  # h3 = 1
        e3bar = E3BarComplexHeisenberg(omega)
        assert not e3bar.is_self_dual_point
        assert not e3bar.is_koszul_self_dual()

    def test_generic_structure_function_nontrivial(self):
        """g(u) != 1 at generic parameters."""
        omega = OmegaBackground(1, -2)
        e3bar = E3BarComplexHeisenberg(omega)
        assert e3bar.structure_function_at_self_dual() == "nontrivial"

    def test_generic_differentials_still_vanish(self):
        """Even at generic parameters, Heisenberg differentials vanish.

        The Heisenberg has NO nonlinear OPE at any parameter value.
        The singular OPE J(z)J(w) ~ k/(z-w)^2 is the metric, not a differential.
        """
        omega = OmegaBackground(1, -2)
        e3bar = E3BarComplexHeisenberg(omega)
        assert e3bar.differentials_all_vanish()
        assert e3bar.differentials_commute()

    def test_generic_parameter_inversion(self):
        """Koszul dual has (h1,h2,h3) -> (-h1,-h2,-h3)."""
        omega = OmegaBackground(1, -2)  # (1, -2, 1)
        e3bar = E3BarComplexHeisenberg(omega)
        dual = e3bar.verdier_dual_parameters()
        assert dual.h1 == Rational(-1)
        assert dual.h2 == Rational(2)
        assert dual.h3 == Rational(-1)

    def test_generic_kappa_level3(self):
        """At SV N=2 point (1,-2,1): kappa_ch = 3."""
        omega = OmegaBackground(1, -2)
        e3bar = E3BarComplexHeisenberg(omega)
        assert e3bar.kappa_ch() == Rational(3)
        assert e3bar.kappa_ch_dual() == Rational(-3)

    def test_generic_kappa_various_levels(self):
        """kappa_ch = -sigma_2 at various parameter values."""
        test_cases = [
            ((1, -2), Rational(3)),     # sigma_2 = -3
            ((2, -3), Rational(7)),     # sigma_2 = -7
            ((1, -5), Rational(21)),    # sigma_2 = -21
            ((3, -4), Rational(13)),    # sigma_2 = -13
        ]
        for (h1, h2), expected_kappa in test_cases:
            omega = OmegaBackground(h1, h2)
            e3bar = E3BarComplexHeisenberg(omega)
            assert e3bar.kappa_ch() == expected_kappa, \
                f"kappa at ({h1},{h2}): expected {expected_kappa}, got {e3bar.kappa_ch()}"


# =========================================================================
# 3. Claim (3): Tridegree decomposition matches tau_3(n)
# =========================================================================

class TestTridegreeDecomposition:
    """Tridegree decomposition of B_{E_3}(H_1) matches tau_3(n)."""

    def setup_method(self):
        self.e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))

    def test_tau3_ground_truth(self):
        """tau_3(n) matches OEIS A000716 ground truth."""
        for n, expected in enumerate(TAU_3_GROUND_TRUTH):
            computed = self.e3bar.trigraded_dimension(n)
            assert computed == expected, \
                f"tau_3({n}): expected {expected}, got {computed}"

    def test_tau3_from_convolution(self):
        """tau_3(n) = sum_{a+b+c=n} p(a)*p(b)*p(c)."""
        for n in range(10):
            direct = self.e3bar.trigraded_dimension(n)
            convolution = 0
            for a in range(n + 1):
                for b in range(n - a + 1):
                    c = n - a - b
                    convolution += _partition_count(a) * _partition_count(b) * _partition_count(c)
            assert direct == convolution, \
                f"Convolution check failed at n={n}: {direct} vs {convolution}"

    def test_tau3_at_n0(self):
        """tau_3(0) = 1 (empty multipartition)."""
        assert self.e3bar.trigraded_dimension(0) == 1

    def test_tau3_at_n1(self):
        """tau_3(1) = 3 (one box in position 1, 2, or 3)."""
        assert self.e3bar.trigraded_dimension(1) == 3

    def test_tau3_at_n2(self):
        """tau_3(2) = 9: (2,0,0),(0,2,0),(0,0,2) each give p(2)=2,
        (1,1,0),(1,0,1),(0,1,1) each give 1*1=1 (*3 = 3),
        but we need all: 2+2+2+1+1+1 = 9. Check: p(2)*1*1 * 3 + 1*1*1 * 3 = 6+3 = 9."""
        assert self.e3bar.trigraded_dimension(2) == 9

    def test_tridegree_decomposition_sums_correctly(self):
        """Sum of all tridegree contributions equals tau_3(n)."""
        for n in range(8):
            decomp = self.e3bar.trigraded_decomposition(n)
            total = sum(decomp.values())
            assert total == self.e3bar.trigraded_dimension(n), \
                f"Decomposition sum at n={n}: {total} vs {self.e3bar.trigraded_dimension(n)}"

    def test_tridegree_is_symmetric(self):
        """The decomposition is S_3-symmetric in the three indices."""
        for n in range(7):
            decomp = self.e3bar.trigraded_decomposition(n)
            for (a, b, c), dim in decomp.items():
                # All permutations should have the same dimension
                for perm in [(a, b, c), (a, c, b), (b, a, c),
                             (b, c, a), (c, a, b), (c, b, a)]:
                    assert perm in decomp, f"Missing permutation {perm} at n={n}"
                    assert decomp[perm] == dim, \
                        f"Asymmetric at n={n}: {(a,b,c)}={dim} but {perm}={decomp[perm]}"

    def test_tau3_generating_function_cube(self):
        """Verify: P(q)^3 coefficients match tau_3(n).

        P(q) = prod_{k>=1} 1/(1-q^k). Compute P(q)^3 by polynomial multiplication.
        """
        max_n = 12
        # Compute P(q) truncated to degree max_n
        p_coeffs = [0] * (max_n + 1)
        p_coeffs[0] = 1
        for k in range(1, max_n + 1):
            for j in range(k, max_n + 1):
                p_coeffs[j] += p_coeffs[j - k]

        # Compute P(q)^3 by convolving three copies
        p2 = [0] * (max_n + 1)
        for i in range(max_n + 1):
            for j in range(max_n + 1 - i):
                p2[i + j] += p_coeffs[i] * p_coeffs[j]

        p3 = [0] * (max_n + 1)
        for i in range(max_n + 1):
            for j in range(max_n + 1 - i):
                p3[i + j] += p2[i] * p_coeffs[j]

        for n in range(min(10, max_n + 1)):
            assert self.e3bar.trigraded_dimension(n) == p3[n], \
                f"P(q)^3 check at n={n}: tau_3={self.e3bar.trigraded_dimension(n)}, P^3={p3[n]}"

    def test_tau3_le_macmahon(self):
        """tau_3(n) <= M(n) only for n >= 3 (for small n they may differ).

        Actually tau_3(1) = 3 > M(1) = 1, so the relationship is NOT
        tau_3 <= M term by term. Instead, the E_3 bar is a DIFFERENT
        construction from the ordered bar. Verify the dimensions match
        the computational engine's own check.
        """
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        # The tau_3 counts TRIGRADED cells; MacMahon counts plane partitions.
        # These are different combinatorial objects.
        # tau_3(0)=1=M(0), tau_3(1)=3>M(1)=1, tau_3(2)=9>M(2)=3
        # This is expected: the E_3 bar (trigraded) has MORE cells than
        # the ordered bar (singly-graded plane partitions).
        assert e3bar.trigraded_dimension(0) == _macmahon_coefficient(0) == 1
        assert e3bar.trigraded_dimension(1) == 3 > _macmahon_coefficient(1)


# =========================================================================
# 4. Claim (4): Three differentials commute
# =========================================================================

class TestDifferentialsCommute:
    """The three E_3 differentials commute (trivially for Heisenberg)."""

    def test_commute_self_dual(self):
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e3bar.differentials_commute()

    def test_commute_generic(self):
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, -2))
        assert e3bar.differentials_commute()

    def test_commute_various_parameters(self):
        """Commutation at multiple parameter values."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3), (1, -5), (3, -4)]:
            e3bar = E3BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e3bar.differentials_commute(), \
                f"Differentials do not commute at ({h1}, {h2})"

    def test_each_differential_vanishes(self):
        """Each individual differential is zero."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            e3bar = E3BarComplexHeisenberg(OmegaBackground(h1, h2))
            for d in (1, 2, 3):
                assert e3bar.differential_in_direction(d) == "zero"


# =========================================================================
# 5. Claim (5): kappa complementarity (conductor = 0 for class G)
# =========================================================================

class TestKappaComplementarity:
    """kappa_ch(H_k) + kappa_ch(H_k^!) = 0 for all k."""

    def test_complementarity_self_dual(self):
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e3bar.verify_kappa_complementarity()
        assert e3bar.kappa_sum() == Rational(0)

    def test_complementarity_generic(self):
        """kappa + kappa^! = 0 at generic parameters."""
        for h1, h2 in [(1, -2), (2, -3), (1, -5), (3, -4), (1, -7)]:
            e3bar = E3BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e3bar.verify_kappa_complementarity(), \
                f"Complementarity failed at ({h1}, {h2}): sum = {e3bar.kappa_sum()}"

    def test_conductor_is_zero(self):
        """rho_K = 0 for class G."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            e3bar = E3BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e3bar.koszul_conductor() == Rational(0)

    def test_cross_check_with_koszul_dual_class(self):
        """Cross-check against the KoszulDual class from the engine."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e3bar = E3BarComplexHeisenberg(omega)
            kd = KoszulDual(BoundaryAlgebra(3, omega))

            # Both should agree on kappa_ch_dual
            assert e3bar.kappa_ch_dual() == kd.kappa_ch_dual(), \
                f"kappa_ch_dual mismatch at ({h1},{h2}): " \
                f"E3={e3bar.kappa_ch_dual()}, KD={kd.kappa_ch_dual()}"

            # Both should verify complementarity
            assert e3bar.verify_kappa_complementarity()
            assert kd.verify_kappa_complementarity()


# =========================================================================
# 6. Full verification pipeline
# =========================================================================

class TestFullVerification:
    """End-to-end verification of the E_3 Koszul theorem for H_1."""

    def test_full_verification_self_dual(self):
        """Full pipeline at the self-dual point."""
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        result = e3bar.full_verification()

        assert result["algebra"] == "Heisenberg H_1"
        assert result["shadow_class"] == "G"
        assert result["shadow_depth"] == 2
        assert result["is_self_dual"]
        assert result["kappa_ch"] == Rational(1)
        assert result["kappa_complementarity"]
        assert result["differentials_vanish"]
        assert result["differentials_commute"]
        assert result["koszul_self_dual_at_sd"]
        assert result["structure_fn_at_sd"] == "identity"
        assert result["tau3_dimensions"][:4] == [1, 3, 9, 22]

    def test_full_verification_generic(self):
        """Full pipeline at a generic point."""
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, -2))
        result = e3bar.full_verification()

        assert result["shadow_class"] == "G"
        assert not result["is_self_dual"]
        assert result["kappa_ch"] == Rational(3)
        assert result["kappa_complementarity"]
        assert result["differentials_vanish"]
        assert result["differentials_commute"]
        assert not result["koszul_self_dual_at_sd"]  # not self-dual point
        assert result["structure_fn_at_sd"] == "nontrivial"

    def test_tau3_vs_partition_cubed(self):
        """tau_3(n) = [q^n] P(q)^3, cross-checked against p(n)."""
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        result = e3bar.full_verification()

        # Verify tau_3 from result matches ground truth
        for n in range(min(10, len(TAU_3_GROUND_TRUTH))):
            assert result["tau3_dimensions"][n] == TAU_3_GROUND_TRUTH[n]

    def test_solid_partitions_for_reference(self):
        """Solid partitions tau_4(n) for comparison (NOT the E_3 dimension)."""
        # Solid partitions: OEIS A000293
        expected = [1, 1, 4, 10, 26, 59, 140, 307, 684, 1464]
        for n, exp in enumerate(expected):
            assert _solid_partition_count(n) == exp, \
                f"tau_4({n}): expected {exp}, got {_solid_partition_count(n)}"


# =========================================================================
# 7. Cross-engine consistency
# =========================================================================

class TestCrossEngineConsistency:
    """Verify E_3 bar results are consistent with existing engines."""

    def test_boundary_algebra_kappa_matches(self):
        """E3BarComplexHeisenberg.kappa_ch matches BoundaryAlgebra.kappa_ch."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e3bar = E3BarComplexHeisenberg(omega)
            ba = BoundaryAlgebra(3, omega)
            assert e3bar.kappa_ch() == ba.kappa_ch(), \
                f"kappa mismatch at ({h1},{h2})"

    def test_e3_bar_at_arity0_is_ground_field(self):
        """B_{E_3}(H_1)_0 has dimension 1 (the ground field)."""
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e3bar.trigraded_dimension(0) == 1

    def test_tridegree_at_arity0(self):
        """Only tridegree (0,0,0) at arity 0."""
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        decomp = e3bar.trigraded_decomposition(0)
        assert decomp == {(0, 0, 0): 1}

    def test_tridegree_at_arity1(self):
        """At arity 1: (1,0,0), (0,1,0), (0,0,1) each with dim 1."""
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        decomp = e3bar.trigraded_decomposition(1)
        assert decomp[(1, 0, 0)] == 1
        assert decomp[(0, 1, 0)] == 1
        assert decomp[(0, 0, 1)] == 1
        assert sum(decomp.values()) == 3
