"""Tests for E_2-chiral Koszul duality of the Heisenberg algebra H_k.

Verifies Theorem thm:e2-koszul-heisenberg from e2_chiral_algebras.tex:
the Heisenberg VOA H_k satisfies E_2-chiral Koszul duality with reversed
braiding.

FOUR CLAIMS of the theorem:
  (1) Both E_2 bar differentials vanish: d_X = d_Y = 0 (free-field)
  (2) Bigraded dimension = tau_2(n) = 2-component multipartitions (P(q)^2)
  (3) Koszul dual has R^{E_2,!}(z) = -k*Omega/z (braiding reversal)
  (4) kappa_ch(H_k) + kappa_ch(H_k^!) = 0 (conductor = 0 for class G)

Ground truth:
  tau_2(n) for n=0..9: 1, 2, 5, 10, 20, 36, 65, 110, 185, 300
    (OEIS A000712: coefficients of P(q)^2 = (prod 1/(1-q^k))^2)
  tau_3(n) for n=0..9: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479
    (OEIS A000716: coefficients of P(q)^3)
  p(n)    for n=0..9: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30
    (OEIS A000041: partition function)

Multi-path verification:
  Path 1: Direct bigraded computation (convolution of partition functions)
  Path 2: Generating function P(q)^2 coefficient extraction
  Path 3: Cross-check tau_3 = tau_2 * p (convolution: E_3 -> E_2 projection)
  Path 4: Cross-check with E_3 engine (holomorphic_cs_chiral_engine.py)
  Path 5: Cross-check with e2_barcobar_koszul.py (complementarity)
  Path 6: R-matrix coefficient sign verification

Manuscript references:
  chapters/theory/e2_chiral_algebras.tex: Theorem thm:e2-koszul-heisenberg
  chapters/theory/en_factorization.tex: Theorem thm:e3-koszul-heisenberg
"""

import pytest
from sympy import Rational

from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    BoundaryAlgebra,
    KoszulDual,
    E3BarComplexHeisenberg,
    _partition_count,
    _macmahon_coefficient,
)
from compute.lib.e2_koszul_heisenberg import (
    E2BarComplexHeisenberg,
    TAU_2_GROUND_TRUTH,
    tau_2,
    tau_2_from_generating_function,
)


# =========================================================================
# 1. Claim (1): Both E_2 bar differentials vanish (free-field)
# =========================================================================

class TestDifferentialsVanish:
    """d_X = d_Y = 0 for the Heisenberg at all parameter values."""

    def test_self_dual_d_X_vanishes(self):
        """d_X = 0 at the self-dual point (1, 0, -1)."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.differential_in_direction(1) == "zero"

    def test_self_dual_d_Y_vanishes(self):
        """d_Y = 0 at the self-dual point (1, 0, -1)."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.differential_in_direction(2) == "zero"

    def test_all_differentials_vanish_self_dual(self):
        """Both differentials vanish at (1, 0, -1)."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.differentials_all_vanish()

    def test_differentials_commute_self_dual(self):
        """Differentials commute (trivially, both zero)."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.differentials_commute()

    def test_generic_differentials_vanish(self):
        """Even at generic parameters, Heisenberg differentials vanish.

        The Heisenberg has NO nonlinear OPE at any parameter value.
        J(z)J(w) ~ k/(z-w)^2 has no first-order pole => mu = 0 => d = 0.
        """
        for h1, h2 in [(1, -2), (2, -3), (1, -5), (3, -4)]:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e2bar.differentials_all_vanish(), \
                f"Differentials nonzero at ({h1}, {h2})"
            assert e2bar.differentials_commute(), \
                f"Differentials do not commute at ({h1}, {h2})"

    def test_each_direction_vanishes_generic(self):
        """Each individual differential is zero at multiple parameters."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            for d in (1, 2):
                assert e2bar.differential_in_direction(d) == "zero", \
                    f"d_{d} nonzero at ({h1}, {h2})"

    def test_invalid_direction_raises(self):
        """Direction must be 1 or 2 for E_2."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        with pytest.raises(AssertionError):
            e2bar.differential_in_direction(3)
        with pytest.raises(AssertionError):
            e2bar.differential_in_direction(0)


# =========================================================================
# 2. Claim (2): Bigraded dimension = tau_2(n) (2-component multipartitions)
# =========================================================================

class TestBigradedDimension:
    """B_{E_2}(H_k) has bigraded dimension tau_2(n) = [q^n] P(q)^2."""

    def setup_method(self):
        self.e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))

    def test_tau2_ground_truth(self):
        """tau_2(n) matches OEIS A000712 ground truth."""
        for n, expected in enumerate(TAU_2_GROUND_TRUTH):
            computed = self.e2bar.bigraded_dimension(n)
            assert computed == expected, \
                f"tau_2({n}): expected {expected}, got {computed}"

    def test_tau2_from_convolution(self):
        """tau_2(n) = sum_{a+b=n} p(a)*p(b)."""
        for n in range(10):
            direct = self.e2bar.bigraded_dimension(n)
            convolution = 0
            for a in range(n + 1):
                b = n - a
                convolution += _partition_count(a) * _partition_count(b)
            assert direct == convolution, \
                f"Convolution check failed at n={n}: {direct} vs {convolution}"

    def test_tau2_at_n0(self):
        """tau_2(0) = 1 (empty bipartition)."""
        assert self.e2bar.bigraded_dimension(0) == 1

    def test_tau2_at_n1(self):
        """tau_2(1) = 2 (one box in position 1 or 2)."""
        assert self.e2bar.bigraded_dimension(1) == 2

    def test_tau2_at_n2(self):
        """tau_2(2) = 5: (2,0),(0,2) each give p(2)=2,
        (1,1) gives p(1)*p(1)=1. Total: 2+2+1 = 5."""
        assert self.e2bar.bigraded_dimension(2) == 5

    def test_tau2_generating_function_square(self):
        """Verify: P(q)^2 coefficients match tau_2(n).

        P(q) = prod_{k>=1} 1/(1-q^k). Compute P(q)^2 by convolution.
        """
        p2 = tau_2_from_generating_function(12)
        for n in range(min(10, len(TAU_2_GROUND_TRUTH))):
            assert self.e2bar.bigraded_dimension(n) == p2[n], \
                f"P(q)^2 check at n={n}: tau_2={self.e2bar.bigraded_dimension(n)}, P^2={p2[n]}"

    def test_tau2_standalone_function(self):
        """Standalone tau_2() function matches engine method."""
        for n in range(12):
            assert tau_2(n) == self.e2bar.bigraded_dimension(n), \
                f"Standalone tau_2({n}) mismatch"

    def test_bidegree_decomposition_sums_correctly(self):
        """Sum of all bidegree contributions equals tau_2(n)."""
        for n in range(10):
            decomp = self.e2bar.bigraded_decomposition(n)
            total = sum(decomp.values())
            assert total == self.e2bar.bigraded_dimension(n), \
                f"Decomposition sum at n={n}: {total} vs {self.e2bar.bigraded_dimension(n)}"

    def test_bidegree_is_symmetric(self):
        """The decomposition is S_2-symmetric in the two indices."""
        for n in range(10):
            decomp = self.e2bar.bigraded_decomposition(n)
            for (a, b), dim in decomp.items():
                assert (b, a) in decomp, \
                    f"Missing permutation ({b},{a}) at n={n}"
                assert decomp[(b, a)] == dim, \
                    f"Asymmetric at n={n}: ({a},{b})={dim} but ({b},{a})={decomp[(b,a)]}"


# =========================================================================
# 3. Claim (3): Braiding reversal via R-matrix sign inversion
# =========================================================================

class TestBraidingReversal:
    """Koszul dual H_k^! has R^{E_2,!}(z) = -k*Omega/z (reversed braiding)."""

    def test_r_matrix_coefficient_self_dual(self):
        """R-matrix coefficient is k = 1 at self-dual point."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.r_matrix_coefficient() == Rational(1)

    def test_r_matrix_dual_coefficient_self_dual(self):
        """Koszul dual R-matrix coefficient is -k = -1."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.r_matrix_coefficient_dual() == Rational(-1)

    def test_braiding_reversal_self_dual(self):
        """R^{E_2,!}(z) = -R^{E_2}(z) at leading order."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.braiding_is_reversed()

    def test_braiding_reversal_generic(self):
        """Braiding reversal holds at all parameter values."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3), (1, -5), (3, -4)]:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e2bar.braiding_is_reversed(), \
                f"Braiding reversal failed at ({h1}, {h2})"

    def test_r_matrix_coefficient_various_levels(self):
        """R-matrix coefficient = k = -sigma_2 at various parameters."""
        test_cases = [
            ((1, 0), Rational(1)),      # sigma_2 = -1
            ((1, -2), Rational(3)),     # sigma_2 = -3
            ((2, -3), Rational(7)),     # sigma_2 = -7
            ((1, -5), Rational(21)),    # sigma_2 = -21
            ((3, -4), Rational(13)),    # sigma_2 = -13
        ]
        for (h1, h2), expected_k in test_cases:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e2bar.r_matrix_coefficient() == expected_k, \
                f"R-matrix coeff at ({h1},{h2}): expected {expected_k}, " \
                f"got {e2bar.r_matrix_coefficient()}"
            assert e2bar.r_matrix_coefficient_dual() == -expected_k, \
                f"Dual R-matrix coeff at ({h1},{h2}): expected {-expected_k}, " \
                f"got {e2bar.r_matrix_coefficient_dual()}"

    def test_verdier_dual_parameters(self):
        """Verdier dual inverts all Omega-background parameters."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, -2))
        dual = e2bar.verdier_dual_parameters()
        assert dual.h1 == Rational(-1)
        assert dual.h2 == Rational(2)
        assert dual.h3 == Rational(-1)

    def test_level_inversion(self):
        """Koszul dual level is -k (negated)."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            k = e2bar.kappa_ch()
            k_dual = e2bar.kappa_ch_dual()
            assert k_dual == -k, \
                f"Level inversion failed at ({h1},{h2}): k={k}, k^!={k_dual}"


# =========================================================================
# 4. Claim (4): kappa complementarity (conductor = 0 for class G)
# =========================================================================

class TestKappaComplementarity:
    """kappa_ch(H_k) + kappa_ch(H_k^!) = 0 for all k."""

    def test_complementarity_self_dual(self):
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.verify_kappa_complementarity()
        assert e2bar.kappa_sum() == Rational(0)

    def test_complementarity_generic(self):
        """kappa + kappa^! = 0 at generic parameters."""
        for h1, h2 in [(1, -2), (2, -3), (1, -5), (3, -4), (1, -7)]:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e2bar.verify_kappa_complementarity(), \
                f"Complementarity failed at ({h1}, {h2}): sum = {e2bar.kappa_sum()}"

    def test_conductor_is_zero(self):
        """rho_K = 0 for class G."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            e2bar = E2BarComplexHeisenberg(OmegaBackground(h1, h2))
            assert e2bar.koszul_conductor() == Rational(0)

    def test_shadow_class_is_G(self):
        """Heisenberg is class G (Gaussian)."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.shadow_class == "G"
        assert e2bar.shadow_depth == 2

    def test_kappa_is_level(self):
        """kappa_ch = k = -sigma_2."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e2bar.kappa_ch() == Rational(1)

    def test_cross_check_with_koszul_dual_class(self):
        """Cross-check against the KoszulDual class from the engine."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e2bar = E2BarComplexHeisenberg(omega)
            kd = KoszulDual(BoundaryAlgebra(2, omega))

            # Both should agree on kappa_ch_dual
            assert e2bar.kappa_ch_dual() == kd.kappa_ch_dual(), \
                f"kappa_ch_dual mismatch at ({h1},{h2}): " \
                f"E2={e2bar.kappa_ch_dual()}, KD={kd.kappa_ch_dual()}"

            # Both should verify complementarity
            assert e2bar.verify_kappa_complementarity()
            assert kd.verify_kappa_complementarity()


# =========================================================================
# 5. E_3 -> E_2 projection: tau_3 = tau_2 * p convolution
# =========================================================================

class TestE3Projection:
    """E_3 -> E_2 dimensional projection: tau_3(n) = sum tau_2(m)*p(n-m)."""

    def setup_method(self):
        self.e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        self.e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))

    def test_tau3_equals_tau2_convolution_p(self):
        """tau_3(n) = sum_{m=0}^{n} tau_2(m) * p(n-m).

        This is the CRITICAL cross-check: the E_3 trigraded bar is the
        convolution of E_2 bigraded bar with one more partition direction.
        """
        for n in range(10):
            t3 = self.e3bar.trigraded_dimension(n)
            convolution = 0
            for m in range(n + 1):
                convolution += self.e2bar.bigraded_dimension(m) * _partition_count(n - m)
            assert t3 == convolution, \
                f"tau_3({n}) = {t3} != conv = {convolution}"

    def test_hierarchy_tau3_ge_tau2_ge_p(self):
        """tau_3(n) >= tau_2(n) >= p(n) for all n >= 0."""
        for n in range(12):
            t3 = self.e3bar.trigraded_dimension(n)
            t2 = self.e2bar.bigraded_dimension(n)
            t1 = _partition_count(n)
            assert t3 >= t2 >= t1, \
                f"Hierarchy violation at n={n}: tau_3={t3}, tau_2={t2}, p={t1}"

    def test_projection_verification_method(self):
        """The engine's verify_e3_projection method returns correct data."""
        results = self.e2bar.verify_e3_projection(8)
        for nn in range(9):
            assert results[nn]["hierarchy"], \
                f"Hierarchy failed at n={nn}"

    def test_convolution_verification_method(self):
        """The engine's verify_tau2_from_tau3_marginal method passes."""
        assert self.e2bar.verify_tau2_from_tau3_marginal(9)

    def test_tau2_le_macmahon(self):
        """tau_2(n) vs MacMahon M(n): different combinatorial objects.

        tau_2(1) = 2 > M(1) = 1. The tau_2 counts BIGRADED cells;
        MacMahon counts plane partitions. tau_2(0) = M(0) = 1.
        """
        assert self.e2bar.bigraded_dimension(0) == _macmahon_coefficient(0) == 1
        assert self.e2bar.bigraded_dimension(1) == 2 > _macmahon_coefficient(1)

    def test_e2_at_arity0_is_ground_field(self):
        """B_{E_2}(H_k)_0 has dimension 1 (the ground field)."""
        assert self.e2bar.bigraded_dimension(0) == 1

    def test_bidegree_at_arity0(self):
        """Only bidegree (0,0) at arity 0."""
        decomp = self.e2bar.bigraded_decomposition(0)
        assert decomp == {(0, 0): 1}

    def test_bidegree_at_arity1(self):
        """At arity 1: (1,0) and (0,1) each with dim 1."""
        decomp = self.e2bar.bigraded_decomposition(1)
        assert decomp[(1, 0)] == 1
        assert decomp[(0, 1)] == 1
        assert sum(decomp.values()) == 2


# =========================================================================
# 6. Cross-engine consistency
# =========================================================================

class TestCrossEngineConsistency:
    """Verify E_2 bar results are consistent with existing engines."""

    def test_boundary_algebra_kappa_matches(self):
        """E2BarComplexHeisenberg.kappa_ch matches BoundaryAlgebra.kappa_ch."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e2bar = E2BarComplexHeisenberg(omega)
            ba = BoundaryAlgebra(2, omega)
            assert e2bar.kappa_ch() == ba.kappa_ch(), \
                f"kappa mismatch at ({h1},{h2})"

    def test_e3_bar_kappa_matches(self):
        """E2 and E3 bar complex kappa_ch agree."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e2bar = E2BarComplexHeisenberg(omega)
            e3bar = E3BarComplexHeisenberg(omega)
            assert e2bar.kappa_ch() == e3bar.kappa_ch(), \
                f"E2 vs E3 kappa mismatch at ({h1},{h2})"

    def test_e3_bar_kappa_dual_matches(self):
        """E2 and E3 bar complex kappa_ch_dual agree."""
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e2bar = E2BarComplexHeisenberg(omega)
            e3bar = E3BarComplexHeisenberg(omega)
            assert e2bar.kappa_ch_dual() == e3bar.kappa_ch_dual(), \
                f"E2 vs E3 kappa dual mismatch at ({h1},{h2})"

    def test_e2_complementarity_from_barcobar_module(self):
        """Cross-check with e2_barcobar_koszul.e2_complementarity_heisenberg."""
        from compute.lib.e2_barcobar_koszul import e2_complementarity_heisenberg
        result = e2_complementarity_heisenberg(k_val=Rational(3))
        assert result["sum_vanishes"]

    def test_e2_not_self_dual_at_sd_point(self):
        """At the self-dual Omega point, H_k is NOT E_2-Koszul self-dual.

        Unlike E_3, the E_2 Koszul dual has REVERSED braiding:
        Rep^{E_2}(H_k) ~ Rep^{E_2}(H_{-k})^{rev}.
        Since the braiding is reversed, H_k != H_k^! as E_2-algebras
        (unless k=0, the degenerate case).
        """
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        assert not e2bar.is_koszul_self_dual()
        # Contrast with E_3 where the self-dual point gives true self-duality
        e3bar = E3BarComplexHeisenberg(OmegaBackground(1, 0))
        assert e3bar.is_koszul_self_dual()


# =========================================================================
# 7. Full verification pipeline
# =========================================================================

class TestFullVerification:
    """End-to-end verification of the E_2 Koszul theorem for H_k."""

    def test_full_verification_self_dual(self):
        """Full pipeline at the self-dual point."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        result = e2bar.full_verification()

        assert result["algebra"] == "Heisenberg H_k"
        assert result["shadow_class"] == "G"
        assert result["shadow_depth"] == 2
        assert result["is_self_dual"]
        assert result["kappa_ch"] == Rational(1)
        assert result["kappa_complementarity"]
        assert result["differentials_vanish"]
        assert result["differentials_commute"]
        assert result["braiding_reversed"]
        assert result["r_matrix_coeff"] == Rational(1)
        assert result["r_matrix_coeff_dual"] == Rational(-1)
        assert result["tau2_dimensions"][:4] == [1, 2, 5, 10]
        assert result["tau3_from_tau2_convolution"]

    def test_full_verification_generic(self):
        """Full pipeline at a generic point."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, -2))
        result = e2bar.full_verification()

        assert result["shadow_class"] == "G"
        assert not result["is_self_dual"]
        assert result["kappa_ch"] == Rational(3)
        assert result["kappa_complementarity"]
        assert result["differentials_vanish"]
        assert result["differentials_commute"]
        assert result["braiding_reversed"]
        assert result["tau3_from_tau2_convolution"]

    def test_tau2_vs_ground_truth(self):
        """tau_2(n) from full_verification matches ground truth."""
        e2bar = E2BarComplexHeisenberg(OmegaBackground(1, 0))
        result = e2bar.full_verification()
        for n in range(min(10, len(TAU_2_GROUND_TRUTH))):
            assert result["tau2_dimensions"][n] == TAU_2_GROUND_TRUTH[n]


# =========================================================================
# 8. E_2 vs E_3 self-duality distinction
# =========================================================================

class TestE2vsE3SelfDuality:
    """The E_2 and E_3 Koszul duality statements differ in self-duality.

    E_3: H_k is Koszul self-dual at the self-dual Omega point (h2=0).
         The relabeling z_1 <-> z_3 is an isomorphism.
    E_2: H_k is NOT self-dual; the Koszul dual has REVERSED braiding.
         Rep^{E_2}(H_k) ~ Rep^{E_2}(H_{-k})^{rev}, and H_k != H_{-k}
         as E_2-algebras (different levels, hence different R-matrices).
    """

    def test_e3_self_dual_e2_not(self):
        """At self-dual point: E_3 self-dual, E_2 not."""
        omega = OmegaBackground(1, 0)
        e3bar = E3BarComplexHeisenberg(omega)
        e2bar = E2BarComplexHeisenberg(omega)
        assert e3bar.is_koszul_self_dual()
        assert not e2bar.is_koszul_self_dual()

    def test_tau2_lt_tau3(self):
        """tau_2(n) < tau_3(n) for n >= 1: fewer components in E_2."""
        omega = OmegaBackground(1, 0)
        e3bar = E3BarComplexHeisenberg(omega)
        e2bar = E2BarComplexHeisenberg(omega)
        for n in range(1, 10):
            assert e2bar.bigraded_dimension(n) < e3bar.trigraded_dimension(n), \
                f"tau_2({n}) >= tau_3({n})"

    def test_tau2_gt_p(self):
        """tau_2(n) > p(n) for n >= 1: more components in E_2 than E_1."""
        for n in range(1, 10):
            assert tau_2(n) > _partition_count(n), \
                f"tau_2({n}) <= p({n})"

    def test_kappa_agrees_across_levels(self):
        """kappa_ch is the SAME for E_1, E_2, E_3 projections.

        kappa_ch is an E_1 invariant; it does not change under the
        E_2 or E_3 enrichment. The braiding affects the R-MATRIX,
        not the level.
        """
        for h1, h2 in [(1, 0), (1, -2), (2, -3)]:
            omega = OmegaBackground(h1, h2)
            e2bar = E2BarComplexHeisenberg(omega)
            e3bar = E3BarComplexHeisenberg(omega)
            ba1 = BoundaryAlgebra(1, omega)
            ba2 = BoundaryAlgebra(2, omega)
            ba3 = BoundaryAlgebra(3, omega)

            k_e2 = e2bar.kappa_ch()
            k_e3 = e3bar.kappa_ch()
            k_ba1 = ba1.kappa_ch()
            k_ba2 = ba2.kappa_ch()
            k_ba3 = ba3.kappa_ch()

            assert k_e2 == k_e3 == k_ba1 == k_ba2 == k_ba3, \
                f"kappa mismatch at ({h1},{h2}): E2={k_e2}, E3={k_e3}, " \
                f"BA1={k_ba1}, BA2={k_ba2}, BA3={k_ba3}"
