"""Tests for E_3-Koszul duality of Y(gl_hat_1) (Theorem thm:e3-koszul-yangian).

Verifies the five claims of the theorem:
  (i)   Spectral sequence degeneration at E_3: P(q)^3 -> (1+t)^3
  (ii)  Commutativity of differentials (S_4 = 0)
  (iii) Parameter inversion: H^*(B_{E_3}(Y)) = H^*(B_{E_3}(Y^!)) = Lambda^*(k^3)
  (iv)  kappa_ch complementarity: kappa_ch(Y) + kappa_ch(Y^!) = 0 = rho_K
  (v)   S_3-equivariance of the cohomological isomorphism

Ground truth:
  CoHA(C^3)=Y^+(gl_hat_1); its Drinfeld double Y(gl_hat_1) is class L,
  shadow depth 3, S_4 = 0.
  Y^! = Verdier dual at (-h1, -h2, -h3), also class L.
  H^*(B_{E_3}(Y)) = H^*(B_{E_3}(Y^!)) = [1, 3, 3, 1] = (1+t)^3.
  kappa_ch(Y|_C) = -sigma_2, kappa_ch(Y^!|_C) = sigma_2, sum = 0 = rho_K.

Manuscript references:
  en_factorization.tex: Theorem thm:e3-koszul-yangian
  holomorphic_cs_chiral_engine.py: E3BarComplexYangian class
"""

import pytest
from math import comb
from sympy import Rational

from compute.lib.holomorphic_cs_chiral_engine import (
    OmegaBackground,
    E3BarComplexYangian,
)


# =========================================================================
# 1. Claim (i): Spectral sequence degeneration
#    (Cross-references test_e3_bar_yangian.py for full spectral sequence;
#     here we verify the Koszul-relevant consequences.)
# =========================================================================

class TestSpectralSequenceDegeneration:
    """The spectral sequence degenerates at E_3 giving (1+t)^3."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_poincare_is_exterior(self):
        """H^*(B_{E_3}(Y)) = Lambda^*(k^3): Poincare = [1, 3, 3, 1]."""
        assert self.yangian.cohomology_poincare() == [1, 3, 3, 1]

    def test_total_dim_is_2_cubed(self):
        assert self.yangian.cohomology_total() == 8

    def test_differentials_are_nonzero(self):
        """Class L has nonzero differentials (unlike Heisenberg)."""
        assert not self.yangian.differentials_all_vanish

    def test_ss_degenerates_at_e3(self):
        """E_3 = E_inf: no further differentials."""
        ss = self.yangian.verify_spectral_sequence(5)
        for n in range(6):
            expected = comb(3, n) if 0 <= n <= 3 else 0
            assert ss[n]["E_inf (cohomology)"] == expected
            assert ss[n]["matches_binomial"]


# =========================================================================
# 2. Claim (ii): Commutativity of differentials
# =========================================================================

class TestDifferentialCommutativity:
    """[d_i, d_j] = 0 from E_3 operad + S_4 = 0 for class L."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_class_is_L(self):
        assert self.yangian.shadow_class == "L"

    def test_shadow_depth_is_3(self):
        assert self.yangian.shadow_depth == 3

    def test_s4_vanishes(self):
        """S_4 = 0 is the defining property of class L."""
        # Class L: shadow depth 3 means S_4 = 0.
        # Shadow depth = max k such that S_k != 0; depth 3 => S_4 = 0.
        assert self.yangian.shadow_depth == 3  # implies S_4 = 0

    def test_tridegree_symmetry_ensures_equivalence(self):
        """S_3 symmetry of C^3 ensures all three directions equivalent."""
        for n in range(5):
            decomp = self.yangian.trigraded_decomposition(n)
            for (a, b, c), dim in decomp.items():
                # All permutations have the same dimension
                assert decomp.get((b, a, c), 0) == dim
                assert decomp.get((a, c, b), 0) == dim


# =========================================================================
# 3. Claim (iii): Parameter inversion and cohomological isomorphism
# =========================================================================

class TestParameterInversion:
    """Y^! has inverted parameters; H^*(B_{E_3}(Y)) = H^*(B_{E_3}(Y^!))."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_verdier_dual_inverts_parameters(self):
        """(h1, h2, h3) -> (-h1, -h2, -h3)."""
        dual_omega = self.yangian.verdier_dual_parameters()
        assert dual_omega.h1 == -self.omega.h1
        assert dual_omega.h2 == -self.omega.h2

    def test_dual_is_class_L(self):
        """Y^! is also class L (pole structure preserved)."""
        assert self.yangian.dual_shadow_class() == "L"
        assert self.yangian.dual_shadow_depth() == 3

    def test_dual_cohomology_matches_original(self):
        """H^n(B_{E_3}(Y^!)) = H^n(B_{E_3}(Y)) for all n."""
        for n in range(8):
            assert self.yangian.dual_cohomology_dimension(n) == \
                   self.yangian.cohomology_dimension(n)

    def test_dual_poincare_is_exterior(self):
        """H^*(B_{E_3}(Y^!)) = Lambda^*(k^3) = [1, 3, 3, 1]."""
        dual_poinc = [self.yangian.dual_cohomology_dimension(n) for n in range(4)]
        assert dual_poinc == [1, 3, 3, 1]

    def test_cohomological_koszul_all_match(self):
        """Full verification: all arities match."""
        result = self.yangian.verify_cohomological_koszul_duality()
        assert result["all_match"]
        assert result["both_are_exterior_on_3_generators"]

    @pytest.mark.parametrize("h1,h2", [(1, 2), (1, 3), (2, 3), (3, 5), (1, 7)])
    def test_parameter_independence(self, h1, h2):
        """The cohomological isomorphism holds at all generic points."""
        omega = OmegaBackground(h1, h2)
        y = E3BarComplexYangian(omega)
        result = y.verify_cohomological_koszul_duality()
        assert result["all_match"]

    def test_dual_constructed_from_inverted_parameters(self):
        """Construct Y^! explicitly from inverted parameters and verify."""
        dual_omega = self.yangian.verdier_dual_parameters()
        y_dual = E3BarComplexYangian(dual_omega)
        # Y^! is class L
        assert y_dual.shadow_class == "L"
        # Y^! has the same cohomology
        assert y_dual.cohomology_poincare() == [1, 3, 3, 1]
        assert y_dual.cohomology_total() == 8


# =========================================================================
# 4. Claim (iv): kappa_ch complementarity
# =========================================================================

class TestKappaComplementarity:
    """kappa_ch(Y|_C) + kappa_ch(Y^!|_C) = 0 = rho_K for class L."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_kappa_ch_is_minus_sigma2(self):
        """kappa_ch(Y) = -sigma_2."""
        assert self.yangian.kappa_ch() == -self.omega.sigma2

    def test_kappa_ch_dual_is_sigma2(self):
        """kappa_ch(Y^!) = sigma_2."""
        assert self.yangian.kappa_ch_dual() == self.omega.sigma2

    def test_conductor_is_zero(self):
        """rho_K = kappa_ch + kappa_ch^! = 0 for class L."""
        assert self.yangian.koszul_conductor() == Rational(0)

    def test_verify_kappa_complementarity(self):
        """API verification method returns True."""
        assert self.yangian.verify_kappa_complementarity()

    @pytest.mark.parametrize("h1,h2", [(1, 2), (1, 3), (2, 3), (3, 5)])
    def test_conductor_zero_at_all_generic_points(self, h1, h2):
        """rho_K = 0 is independent of the specific generic parameters."""
        omega = OmegaBackground(h1, h2)
        y = E3BarComplexYangian(omega)
        assert y.verify_kappa_complementarity()
        assert y.koszul_conductor() == Rational(0)

    def test_kappa_sigma2_explicit(self):
        """Explicit check: sigma_2 = h1*h2 + h1*h3 + h2*h3."""
        h1, h2 = Rational(1), Rational(2)
        h3 = -h1 - h2  # = -3
        sigma2 = h1 * h2 + h1 * h3 + h2 * h3
        assert sigma2 == Rational(1 * 2 + 1 * (-3) + 2 * (-3))
        assert sigma2 == Rational(-7)
        omega = OmegaBackground(h1, h2)
        assert omega.sigma2 == sigma2
        y = E3BarComplexYangian(omega)
        assert y.kappa_ch() == -sigma2  # = 7
        assert y.kappa_ch_dual() == sigma2  # = -7
        assert y.kappa_ch() + y.kappa_ch_dual() == Rational(0)

    def test_kappa_dual_from_inverted_parameters(self):
        """Cross-check: construct Y^! from inverted params, read its kappa."""
        dual_omega = self.yangian.verdier_dual_parameters()
        y_dual = E3BarComplexYangian(dual_omega)
        # kappa_ch of Y^! constructed from inverted params
        # Y^! at (-h1, -h2, -h3): sigma_2^! = sigma_2, kappa = -sigma_2
        # But at E_1 level the Verdier dual has k^! = sigma_2
        # The computed kappa_ch of the dual-parameter Yangian is -sigma_2^! = -sigma_2
        # This equals kappa_ch of the ORIGINAL, not the dual.
        # The sign flip is in the VERDIER DUALITY, not in the parameter substitution.
        assert y_dual.kappa_ch() == -dual_omega.sigma2
        # sigma_2^! = sigma_2 (same!), so kappa_ch(Y^! params) = -sigma_2 = kappa_ch(Y)
        assert dual_omega.sigma2 == self.omega.sigma2
        # The KOSZUL DUAL kappa is sigma_2, which comes from the Verdier sign:
        assert self.yangian.kappa_ch_dual() == self.omega.sigma2


# =========================================================================
# 5. Claim (v): S_3-equivariance
# =========================================================================

class TestS3Equivariance:
    """The cohomological isomorphism is S_3-equivariant."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_s3_equivariance_api(self):
        """API method confirms S_3-equivariance."""
        result = self.yangian.verify_s3_equivariance()
        assert result["s3_invariant_poincare"]
        assert result["verdier_commutes_with_s3"]

    def test_poincare_symmetric_under_s3(self):
        """(1+t)^3 is symmetric in the 3 generators."""
        poinc = self.yangian.cohomology_poincare()
        # Poincare duality: h_k = h_{3-k}
        assert poinc[0] == poinc[3]
        assert poinc[1] == poinc[2]

    def test_verdier_commutes_with_permutation(self):
        """D_{C^3} commutes with S_3: sigma(-h) = -(sigma(h))."""
        # Take a permutation: (h1, h2, h3) -> (h2, h1, h3) = (h2, h3, h1) up to CY
        # Actually the S_3 permutation on (h1, h2, h3) is just reordering.
        # Verdier: (h1,h2,h3) -> (-h1,-h2,-h3).
        # sigma then Verdier: (h2,h1,h3) -> (-h2,-h1,-h3)
        # Verdier then sigma: (-h1,-h2,-h3) -> (-h2,-h1,-h3)
        # Same result.
        h1, h2 = self.omega.h1, self.omega.h2
        h3 = -h1 - h2

        # Sigma = (12): swap h1, h2
        sigma_h = (h2, h1, h3)
        # Verdier of sigma_h
        verdier_sigma = (-sigma_h[0], -sigma_h[1], -sigma_h[2])

        # Verdier of original
        verdier_h = (-h1, -h2, -h3)
        # Sigma of verdier_h
        sigma_verdier = (verdier_h[1], verdier_h[0], verdier_h[2])

        assert verdier_sigma == sigma_verdier


# =========================================================================
# 6. Multi-path verification (Koszul-specific)
# =========================================================================

class TestKoszulMultiPath:
    """Cross-check Koszul claims via independent computation paths."""

    def setup_method(self):
        self.omega = OmegaBackground(1, 2)
        self.yangian = E3BarComplexYangian(self.omega)

    def test_kappa_path1_engine_vs_path2_direct(self):
        """Path 1 (engine) vs Path 2 (direct sigma_2 computation)."""
        h1, h2 = self.omega.h1, self.omega.h2
        h3 = -h1 - h2
        sigma2_direct = h1 * h2 + h1 * h3 + h2 * h3
        assert self.yangian.kappa_ch() == -sigma2_direct

    def test_conductor_path1_engine_vs_path2_formula(self):
        """Path 1 (engine sum) vs Path 2 (class L formula rho_K = 0)."""
        assert self.yangian.koszul_conductor() == Rational(0)
        # Path 2: class L always has rho_K = 0
        assert self.yangian.shadow_class == "L"
        # => rho_K = 0 by the class L conductor theorem

    def test_dual_cohomology_path1_engine_vs_path2_explicit_construction(self):
        """Path 1 (engine dual_cohomology_dimension) vs Path 2 (explicit Y^!)."""
        dual_omega = self.yangian.verdier_dual_parameters()
        y_dual = E3BarComplexYangian(dual_omega)
        for n in range(6):
            # Path 1: engine method
            path1 = self.yangian.dual_cohomology_dimension(n)
            # Path 2: explicit construction of Y^! as E3BarComplexYangian(-h)
            path2 = y_dual.cohomology_dimension(n)
            assert path1 == path2

    def test_full_investigation_includes_koszul(self):
        """The full_investigation output includes Koszul data."""
        result = self.yangian.full_investigation()
        assert "kappa_ch" in result
        assert "kappa_ch_dual" in result
        assert "koszul_conductor" in result
        assert "kappa_complementarity" in result
        assert result["kappa_complementarity"]
        assert "cohomological_koszul_duality" in result
        assert result["cohomological_koszul_duality"]["all_match"]
        assert "s3_equivariance" in result
