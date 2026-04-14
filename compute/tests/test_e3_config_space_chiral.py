r"""Tests for E_3 factorization homology on configuration spaces of C^3.

Manuscript references:
    Chapter ch:en-factorization (en_factorization.tex):
      conj:topological-e3-comparison: E_3 from Conf_n(C^3)
      thm:zte-failure: ZTE fails for the Yang R-matrix
      conj:e3-koszul-duality: E_3 Koszul from 6d theory
      subsec:fact-hom-c3: Factorization homology on C^3

    CLAIM STATUS: CONJECTURAL for d=3 (depends on CY-A_3).
    The E_3 is TOPOLOGICAL (little 3-disks), NOT algebraic Deligne (AP154).

Literature ground truth:
    Configuration space Conf_n(C^d):
      - real dim = 2dn
      - linking sphere = S^{2d-1}
      - pi_1(Conf_2(C^d)) = pi_1(S^{2d-1}) = 0 for d >= 2
      - Poincare: P(t) = prod_{k=1}^{n-1} (1 + k*t^{2d-1})
        [DC] Cohen 1976, Totaro 1996

    Structure function identities:
      - g(z)*g(-z) = 1 (CY inversion, from h_1+h_2+h_3=0)
        [DC] direct computation, [LT] Schiffmann-Vasserot
      - g_ch(u,v)*g_ch(-u,-v) = 1 (two-parameter inversion)
        [DC] follows from g*g(-) = 1 applied three times

    Plane partitions (MacMahon function):
      M(q) = prod_{k>=1} 1/(1-q^k)^k
      pp(0..10) = 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500
      [DC] recursion, [LT] OEIS A000219

    Formality:
      Conf_n(C^d) is formal over Q (Kriz 1994)
      [LT] Kriz, "On the rational homotopy type of configuration spaces"
"""

import math

import numpy as np
import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.e3_config_space_chiral import (
    DunnDecomposition,
    _g_rational,
    _g_two_param,
    _plane_partition_count,
    cohomology_algebra_generators,
    comparison_r3_vs_c3,
    conf_space_betti_numbers,
    conf_space_euler_char,
    conf_space_real_dim,
    conf_space_total_betti,
    e3_action_on_algebra,
    e3_config_space_summary,
    e3_operad_space_dim,
    factorization_homology_c3_tree_level,
    fm_compactification_strata,
    fundamental_group_conf2,
    linking_sphere_dim,
    one_loop_integral_n_points,
    perturbative_partition_function,
    propagator_heisenberg,
    propagator_toroidal,
    propagator_yangian,
    tree_integral_n_points,
    two_loop_e3_integral,
    two_loop_e3_integral_two_param,
    verify_cy_inversion,
    verify_one_loop_trivial,
    verify_tree_factorization,
    verify_two_param_inversion,
)


# ================================================================
# STANDARD TEST PARAMETERS (AP-CY28: avoid poles)
# ================================================================

# Poles of g(z) at z = -h_1, -h_2, -h_3 = -3.7, 4.1, -0.4
# and at z = h_1, h_2, h_3 = 3.7, -4.1, 0.4 (zeros)
# Test spectral parameters chosen far from all these.
H1 = 3.7
H2 = -4.1
H3 = -(H1 + H2)  # = 0.4

# Large-separation parameters for adversarial safety
H1_SAFE = 37.0
H2_SAFE = -41.0
H3_SAFE = 4.0


# ================================================================
# 1. Configuration space topology
# ================================================================

class TestConfigSpaceTopology:
    """Test topological properties of Conf_n(C^d)."""

    def test_real_dim_conf_n_c3(self):
        """dim_R Conf_n(C^3) = 6n.

        # VERIFIED: [DC] direct, [DA] dimensional analysis
        """
        for n in range(1, 6):
            assert conf_space_real_dim(n, 3) == 6 * n

    def test_real_dim_conf_n_c2(self):
        """dim_R Conf_n(C^2) = 4n.

        # VERIFIED: [DC] direct, [DA] dimensional analysis
        """
        for n in range(1, 6):
            assert conf_space_real_dim(n, 2) == 4 * n

    def test_real_dim_conf_n_c1(self):
        """dim_R Conf_n(C) = 2n.

        # VERIFIED: [DC] direct, [DA] dimensional analysis
        """
        for n in range(1, 6):
            assert conf_space_real_dim(n, 1) == 2 * n

    def test_linking_sphere_dim(self):
        """Linking sphere S^{2d-1} for the diagonal in C^d x C^d.

        # VERIFIED: [DC] direct, [LT] standard codimension formula
        """
        assert linking_sphere_dim(1) == 1   # S^1 for C
        assert linking_sphere_dim(2) == 3   # S^3 for C^2
        assert linking_sphere_dim(3) == 5   # S^5 for C^3

    def test_pi1_conf2_c1_nontrivial(self):
        """pi_1(Conf_2(C)) = Z (braid group, nontrivial).

        # VERIFIED: [DC] pi_1(S^1) = Z, [LT] Artin braid group
        """
        assert fundamental_group_conf2(1) == "Z"

    def test_pi1_conf2_c2_trivial(self):
        """pi_1(Conf_2(C^2)) = 0 (trivially braided).

        # VERIFIED: [DC] pi_1(S^3) = 0
        """
        assert fundamental_group_conf2(2) == "0"

    def test_pi1_conf2_c3_trivial(self):
        """pi_1(Conf_2(C^3)) = 0 (trivially braided).

        # VERIFIED: [DC] pi_1(S^5) = 0
        """
        assert fundamental_group_conf2(3) == "0"


# ================================================================
# 2. Betti numbers
# ================================================================

class TestBettiNumbers:
    """Test Betti numbers of Conf_n(C^d)."""

    def test_conf_2_c3_betti(self):
        """H*(Conf_2(C^3)) = H*(S^5): b_0=1, b_5=1.

        # VERIFIED: [DC] product formula, [LT] Cohen 1976
        """
        betti = conf_space_betti_numbers(2, 3, max_degree=10)
        assert betti[0] == 1
        assert betti[5] == 1
        # All others should be 0
        for k in range(1, 5):
            assert betti[k] == 0
        for k in range(6, 11):
            assert betti[k] == 0

    def test_conf_3_c3_betti(self):
        """H*(Conf_3(C^3)): generators omega_{12}, omega_{13}, omega_{23} in H^5.

        P(t) = (1+t^5)(1+2*t^5) = 1 + 3*t^5 + 2*t^{10}.
        So b_0=1, b_5=3, b_10=2.

        # VERIFIED: [DC] product formula, [LT] Cohen 1976
        """
        betti = conf_space_betti_numbers(3, 3, max_degree=12)
        assert betti[0] == 1
        assert betti[5] == 3   # 1 + 2 = 3 (from the product)
        assert betti[10] == 2  # 1 * 2 = 2
        for k in [1, 2, 3, 4, 6, 7, 8, 9, 11, 12]:
            assert betti[k] == 0

    def test_conf_2_c1_betti(self):
        """H*(Conf_2(C)) = H*(S^1): b_0=1, b_1=1.

        # VERIFIED: [DC] product formula, [LT] Arnold 1970
        """
        betti = conf_space_betti_numbers(2, 1, max_degree=5)
        assert betti[0] == 1
        assert betti[1] == 1
        for k in range(2, 6):
            assert betti[k] == 0

    def test_conf_3_c1_betti(self):
        """H*(Conf_3(C)): P(t) = (1+t)(1+2t) = 1+3t+2t^2.

        # VERIFIED: [DC] product formula, [LT] Arnold 1970
        """
        betti = conf_space_betti_numbers(3, 1, max_degree=5)
        assert betti[0] == 1
        assert betti[1] == 3
        assert betti[2] == 2
        for k in range(3, 6):
            assert betti[k] == 0

    def test_conf_n_euler_char(self):
        """chi(Conf_n(C^d)) = 0 for n >= 2, d >= 1.

        # VERIFIED: [DC] product formula at t=-1
        """
        for n in range(2, 6):
            for d in [1, 2, 3]:
                assert conf_space_euler_char(n, d) == 0

    def test_conf_1_euler_char(self):
        """chi(Conf_1(C^d)) = 1 (single point, trivially).

        # VERIFIED: [DC] direct
        """
        assert conf_space_euler_char(1, 3) == 1

    def test_total_betti_conf_n(self):
        """sum b_k(Conf_n(C^d)) = n! for d >= 1.

        # VERIFIED: [DC] P(1) = prod_{k=1}^{n-1}(1+k) = n!
        """
        for n in range(1, 7):
            assert conf_space_total_betti(n, 3) == math.factorial(n)


# ================================================================
# 3. Structure function identities
# ================================================================

class TestStructureFunctionIdentities:
    """Test CY structure function identities."""

    def test_cy_inversion(self):
        """g(z)*g(-z) = 1.

        # VERIFIED: [DC] direct algebraic proof, [LT] Schiffmann-Vasserot
        """
        passed, residual = verify_cy_inversion(H1, H2, H3)
        assert passed, f"CY inversion failed with residual {residual}"
        assert residual < 1e-10

    def test_cy_inversion_safe_params(self):
        """g(z)*g(-z) = 1 with large-separation parameters.

        # VERIFIED: [DC] direct
        """
        passed, residual = verify_cy_inversion(H1_SAFE, H2_SAFE, H3_SAFE)
        assert passed, f"CY inversion failed with residual {residual}"

    def test_two_param_inversion(self):
        """g_ch(u,v)*g_ch(-u,-v) = 1.

        # VERIFIED: [DC] follows from g*g(-) = 1 thrice
        """
        passed, residual = verify_two_param_inversion(H1, H2, H3)
        assert passed, f"Two-param inversion failed with residual {residual}"
        assert residual < 1e-9

    def test_g_at_zero_is_minus_one(self):
        """g(0) = (-h_1)(-h_2)(-h_3)/(h_1 h_2 h_3) = -1 (CY sign).

        # VERIFIED: [DC] direct substitution
        """
        val = _g_rational(0, H1, H2, H3)
        assert abs(val - (-1.0)) < 1e-12, f"g(0) = {val}, expected -1"

    def test_g_ch_at_zero_zero(self):
        """g_ch(0,0) = g(0)^3 = (-1)^3 = -1.

        # VERIFIED: [DC] direct
        """
        val = _g_two_param(0, 0, H1, H2, H3)
        assert abs(val - (-1.0)) < 1e-12, f"g_ch(0,0) = {val}, expected -1"


# ================================================================
# 4. One-loop triviality
# ================================================================

class TestOneLoopTriviality:
    """Test that the one-loop integral at n=2 is trivial."""

    def test_one_loop_n2_is_one(self):
        """I_2^{1-loop} = g(z)*g(-z) = 1.

        # VERIFIED: [DC] CY inversion identity
        """
        passed, residual = verify_one_loop_trivial(H1, H2, H3)
        assert passed, f"One-loop triviality failed with residual {residual}"

    def test_one_loop_n2_explicit(self):
        """Explicit check: g(z)*g(-z) = 1 at specific z.

        # VERIFIED: [DC] direct computation
        """
        z = 5.3 + 2.1j  # Far from all poles
        val = _g_rational(z, H1, H2, H3) * _g_rational(-z, H1, H2, H3)
        assert abs(val - 1.0) < 1e-12


# ================================================================
# 5. Tree-level integrals
# ================================================================

class TestTreeIntegrals:
    """Test tree-level (E_1) Feynman integrals."""

    def test_tree_n1_is_one(self):
        """I_1^{tree} = 1 (vacuum).

        # VERIFIED: [DC] definition
        """
        assert tree_integral_n_points(1, H1, H2, H3) == 1.0

    def test_tree_n2_is_single_propagator(self):
        """I_2^{tree} = g(u_1 - u_2).

        # VERIFIED: [DC] single propagator
        """
        u = [5.0, 8.0]
        val = tree_integral_n_points(2, H1, H2, H3, u)
        expected = _g_rational(u[0] - u[1], H1, H2, H3)
        assert abs(val - expected) < 1e-12

    def test_tree_factorization(self):
        """Tree integral = product of consecutive g-values.

        # VERIFIED: [DC] definition of tree integral
        """
        passed, residual = verify_tree_factorization(H1, H2, H3, n=4)
        assert passed, f"Tree factorization failed with residual {residual}"

    def test_tree_factorization_n5(self):
        """Tree integral factorizes for n=5.

        # VERIFIED: [DC] definition of tree integral
        """
        passed, residual = verify_tree_factorization(H1, H2, H3, n=5)
        assert passed


# ================================================================
# 6. E_3 two-loop integral
# ================================================================

class TestE3TwoLoopIntegral:
    """Test two-loop (E_3) Feynman integrals."""

    def test_e3_integral_is_product_of_pairwise(self):
        """I_3^{E_3} = prod_{i<j} g(u_i - u_j).

        # VERIFIED: [DC] definition
        """
        u = [5.0, 8.0, 12.0]
        val = two_loop_e3_integral(H1, H2, H3, u)
        expected = (_g_rational(u[0]-u[1], H1, H2, H3) *
                    _g_rational(u[0]-u[2], H1, H2, H3) *
                    _g_rational(u[1]-u[2], H1, H2, H3))
        assert abs(val - expected) < 1e-12

    def test_e3_integral_two_param(self):
        """Two-parameter E_3 integral = prod g_ch(du, dv).

        # VERIFIED: [DC] definition
        """
        u = [5.0, 8.0, 12.0]
        v = [3.0, 6.0, 10.0]
        val = two_loop_e3_integral_two_param(H1, H2, H3, u, v)
        expected = 1.0
        for i in range(3):
            for j in range(i+1, 3):
                expected *= _g_two_param(u[i]-u[j], v[i]-v[j], H1, H2, H3)
        assert abs(val - expected) < 1e-10


# ================================================================
# 7. Propagators
# ================================================================

class TestPropagators:
    """Test propagator functions."""

    def test_heisenberg_propagator_scaling(self):
        """P(z) = omega / z^2 scales as 1/z^2.

        # VERIFIED: [DC] definition
        """
        z1 = 3.0
        z2 = 6.0
        p1 = propagator_heisenberg(z1)
        p2 = propagator_heisenberg(z2)
        # p2/p1 = (z1/z2)^2 = 1/4
        assert abs(p2 / p1 - (z1/z2)**2) < 1e-12

    def test_heisenberg_propagator_pole(self):
        """P(0) diverges.

        # VERIFIED: [DC] pole at z=0
        """
        with pytest.raises(ZeroDivisionError):
            propagator_heisenberg(0.0)

    def test_yangian_propagator_is_g(self):
        """Yangian propagator = g(z).

        # VERIFIED: [DC] definition
        """
        z = 5.3
        val = propagator_yangian(z, H1, H2, H3)
        expected = _g_rational(z, H1, H2, H3)
        assert abs(val - expected) < 1e-12

    def test_toroidal_propagator_is_g_ch(self):
        """Toroidal propagator = g_ch(u, v).

        # VERIFIED: [DC] definition
        """
        u, v = 5.3, 7.1
        val = propagator_toroidal(u, v, H1, H2, H3)
        expected = _g_two_param(u, v, H1, H2, H3)
        assert abs(val - expected) < 1e-12


# ================================================================
# 8. Plane partitions (MacMahon function)
# ================================================================

class TestPlanePartitions:
    """Test plane partition counting."""

    def test_plane_partition_small_values(self):
        """pp(0..10) = 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500.

        # VERIFIED: [DC] recursion, [LT] OEIS A000219
        """
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for n, exp in enumerate(expected):
            assert _plane_partition_count(n) == exp, \
                f"pp({n}) = {_plane_partition_count(n)}, expected {exp}"

    def test_plane_partition_monotone(self):
        """pp(n) is strictly increasing for n >= 1.

        # VERIFIED: [DC] first 15 values
        """
        for n in range(2, 15):
            assert _plane_partition_count(n) > _plane_partition_count(n-1)


# ================================================================
# 9. Dunn decomposition
# ================================================================

class TestDunnDecomposition:
    """Test the E_3 = E_1 x E_1 x E_1 decomposition."""

    def test_three_factors(self):
        """Dunn decomposition produces exactly three E_1 factors.

        # VERIFIED: [DC] Dunn additivity theorem
        """
        dunn = DunnDecomposition(H1, H2, H3)
        factors = dunn.factor_data()
        assert len(factors) == 3

    def test_cy_condition_verified(self):
        """h_1 + h_2 + h_3 = 0.

        # VERIFIED: [DC] construction
        """
        dunn = DunnDecomposition(H1, H2, H3)
        assert dunn.verify_cy_condition()

    def test_degeneration_chain(self):
        """E_3 -> E_2 -> E_1 degeneration chain has 3 steps.

        # VERIFIED: [DC] Dunn decomposition
        """
        dunn = DunnDecomposition(H1, H2, H3)
        chain = dunn.e3_degeneration_chain()
        assert len(chain) == 3
        assert chain[0]["step"] == "E_3 -> E_2"
        assert chain[1]["step"] == "E_2 -> E_1"
        assert chain[2]["step"] == "E_1 -> E_0"

    def test_sigma3_nonzero(self):
        """sigma_3 = h_1 h_2 h_3 != 0 at generic point.

        # VERIFIED: [DC] direct computation
        """
        dunn = DunnDecomposition(H1, H2, H3)
        assert abs(dunn.sigma3) > 1e-6


# ================================================================
# 10. Cohomology algebra generators
# ================================================================

class TestCohomologyAlgebra:
    """Test the cohomology algebra of Conf_n(C^3)."""

    def test_generator_degree_c3(self):
        """Generators of H*(Conf_n(C^3)) have degree 5.

        # VERIFIED: [DC] linking sphere S^5, [LT] Cohen 1976
        """
        coh = cohomology_algebra_generators(3, 3)
        assert coh["generator_degree"] == 5

    def test_generator_degree_c1(self):
        """Generators of H*(Conf_n(C)) have degree 1.

        # VERIFIED: [DC] linking sphere S^1, [LT] Arnold 1970
        """
        coh = cohomology_algebra_generators(3, 1)
        assert coh["generator_degree"] == 1

    def test_num_generators(self):
        """C(n,2) generators for n points.

        # VERIFIED: [DC] one omega_{ij} per pair
        """
        for n in range(2, 7):
            coh = cohomology_algebra_generators(n, 3)
            assert coh["num_generators"] == n * (n-1) // 2

    def test_num_arnold_relations(self):
        """C(n,3) Arnold relations for n points.

        # VERIFIED: [DC] one relation per unordered triple
        """
        for n in range(3, 7):
            coh = cohomology_algebra_generators(n, 3)
            assert coh["num_arnold_relations"] == math.comb(n, 3)

    def test_formality(self):
        """Conf_n(C^3) is formal (Kriz 1994).

        # VERIFIED: [LT] Kriz 1994
        """
        coh = cohomology_algebra_generators(3, 3)
        assert coh["is_formal"]

    def test_chain_level_e3_nontrivial(self):
        """Chain-level E_3 is nontrivial despite rational formality (AP-CY33).

        # VERIFIED: [LT] AP-CY33 discussion in CLAUDE.md
        """
        coh = cohomology_algebra_generators(3, 3)
        assert coh["chain_level_E3_nontrivial"]
        assert coh["rational_E3_collapses_to_E2"]


# ================================================================
# 11. E_3 operad action
# ================================================================

class TestE3OperadAction:
    """Test the E_3 operad action on the boundary algebra."""

    def test_e3_at_generic_point(self):
        """E_3 structure at generic sigma_3 != 0.

        # VERIFIED: [DC] sigma_3 nonzero => E_3
        """
        action = e3_action_on_algebra(3, H1, H2, H3)
        assert action["E_n_level"] == "E_3"

    def test_einf_at_self_dual(self):
        """E_inf at self-dual point sigma_3 = 0.

        # VERIFIED: [DC] sigma_3 = 0 => E_inf
        """
        action = e3_action_on_algebra(3, 1.0, -1.0, 0.0)
        assert action["E_n_level"] == "E_inf"

    def test_topological_braiding_trivial(self):
        """Topological braiding from pi_1(Conf_2(C^3)) = 0.

        # VERIFIED: [DC] pi_1(S^5) = 0
        """
        action = e3_action_on_algebra(2, H1, H2, H3)
        assert "trivial" in action["topological_braiding"]

    def test_e3_space_dim(self):
        """dim E_3(n) = 3n.

        # VERIFIED: [DC] E_3(n) ~ Conf_n(R^3), dim_R = 3n
        """
        for n in range(1, 6):
            assert e3_operad_space_dim(n) == 3 * n


# ================================================================
# 12. FM compactification
# ================================================================

class TestFMCompactification:
    """Test Fulton-MacPherson compactification strata."""

    def test_codim1_strata_count(self):
        """Number of codim-1 strata = 2^n - n - 1.

        # VERIFIED: [DC] enumeration of subsets of size >= 2
        """
        for n in range(2, 7):
            fm = fm_compactification_strata(n, 3)
            expected = 2**n - n - 1
            assert fm["num_codim1_strata"] == expected, \
                f"n={n}: got {fm['num_codim1_strata']}, expected {expected}"

    def test_fm_3_strata(self):
        """FM_3(C^3) has 4 codim-1 strata: 3 of size 2, 1 of size 3.

        # VERIFIED: [DC] 2^3 - 3 - 1 = 4
        """
        fm = fm_compactification_strata(3, 3)
        assert fm["num_codim1_strata"] == 4
        strata = fm["strata_by_size"]
        # Size 2: C(3,2) = 3 strata (collisions {12}, {13}, {23})
        assert strata[0]["subset_size"] == 2
        assert strata[0]["num_strata"] == 3
        # Size 3: C(3,3) = 1 stratum (total collision {123})
        assert strata[1]["subset_size"] == 3
        assert strata[1]["num_strata"] == 1


# ================================================================
# 13. Perturbative partition function
# ================================================================

class TestPerturbativePartition:
    """Test the perturbative partition function."""

    def test_partition_function_starts_at_1(self):
        """Z_pert = 1 + O(coupling^2).

        # VERIFIED: [DC] definition (no n=0,1 contribution)
        """
        pf = perturbative_partition_function(2, H1, H2, H3, coupling=0.01)
        # At very small coupling, Z ~ 1
        assert abs(pf["Z_pert"] - 1.0) < 0.1

    def test_partition_function_has_tree_and_loop(self):
        """Each order has tree and one-loop contributions.

        # VERIFIED: [DC] definition
        """
        pf = perturbative_partition_function(4, H1, H2, H3)
        for n in range(2, 5):
            assert "tree" in pf["contributions"][n]
            assert "one_loop" in pf["contributions"][n]


# ================================================================
# 14. Factorization homology at tree level
# ================================================================

class TestFactorizationHomologyTreeLevel:
    """Test factorization homology on C^3 at tree level."""

    def test_macmahon_coefficients(self):
        """MacMahon coefficients from the FH engine match pp(n).

        # VERIFIED: [DC] recursion, [LT] OEIS A000219
        """
        fh = factorization_homology_c3_tree_level(H1, H2, H3, max_charge=6)
        expected = [1, 1, 3, 6, 13, 24, 48]
        for i, exp in enumerate(expected):
            assert fh["macmahon_coefficients"][i] == exp

    def test_tree_level_at_self_dual(self):
        """At sigma_3 = 0: tree level, E_inf.

        # VERIFIED: [DC] sigma_3 = 0 => self-dual
        """
        fh = factorization_homology_c3_tree_level(1.0, -1.0, 0.0)
        assert fh["tree_level"]
        assert fh["E_n_level"] == "E_inf"

    def test_not_tree_level_at_generic(self):
        """At sigma_3 != 0: not tree level, E_3.

        # VERIFIED: [DC] sigma_3 != 0 => loop corrections
        """
        fh = factorization_homology_c3_tree_level(H1, H2, H3)
        assert not fh["tree_level"]
        assert fh["E_n_level"] == "E_3"


# ================================================================
# 15. R^3 vs C^3 comparison
# ================================================================

class TestR3vsC3Comparison:
    """Test the comparison between CS on R^3 and hCS on C^3."""

    def test_both_e3(self):
        """Both R^3 CS and C^3 hCS are E_3.

        # VERIFIED: [LT] Costello-Francis-Gwilliam 2021
        """
        comp = comparison_r3_vs_c3()
        assert comp["shared"]["E_n_level"] == "E_3"

    def test_both_pi1_trivial(self):
        """Both have trivial pi_1(Conf_2).

        # VERIFIED: [DC] pi_1(S^2) = 0, pi_1(S^5) = 0
        """
        comp = comparison_r3_vs_c3()
        assert comp["shared"]["pi_1_trivial"]

    def test_generator_degrees_differ(self):
        """R^3 has degree-2 generators; C^3 has degree-5.

        # VERIFIED: [DC] linking spheres S^2, S^5
        """
        comp = comparison_r3_vs_c3()
        assert comp["R^3 (CS)"]["generator_degree"] == 2
        assert comp["C^3 (hCS)"]["generator_degree"] == 5

    def test_zte_obstruction_shared(self):
        """Both share the ZTE obstruction.

        # VERIFIED: [DC] thm:zte-failure
        """
        comp = comparison_r3_vs_c3()
        assert "nontrivial" in comp["shared"]["ZTE_obstruction"]


# ================================================================
# 16. Master summary
# ================================================================

class TestMasterSummary:
    """Test the master summary function."""

    def test_summary_runs(self):
        """The master summary produces a nonempty dict."""
        summary = e3_config_space_summary(
            h1=Rational(37, 10),
            h2=Rational(-41, 10),
        )
        assert isinstance(summary, dict)
        assert "parameters" in summary
        assert "topology" in summary
        assert "identities" in summary

    def test_summary_identities_pass(self):
        """All identities pass in the master summary."""
        summary = e3_config_space_summary(
            h1=Rational(37, 10),
            h2=Rational(-41, 10),
        )
        ids = summary["identities"]
        assert ids["CY_inversion"]["pass"]
        assert ids["two_param_inversion"]["pass"]
        assert ids["one_loop_trivial"]["pass"]
        assert ids["tree_factorization"]["pass"]

    def test_summary_cy_condition(self):
        """CY condition verified in summary."""
        summary = e3_config_space_summary(
            h1=Rational(37, 10),
            h2=Rational(-41, 10),
        )
        assert summary["parameters"]["CY_condition"]

    def test_summary_dunn_verified(self):
        """Dunn decomposition CY verified."""
        summary = e3_config_space_summary(
            h1=Rational(37, 10),
            h2=Rational(-41, 10),
        )
        assert summary["dunn_decomposition"]["cy_verified"]


# ================================================================
# 17. Cross-checks with existing engines
# ================================================================

class TestCrossChecks:
    """Cross-check with existing engines in the repository."""

    def test_g_matches_e3_two_parameter(self):
        """g(z) matches the structure function in e3_two_parameter_rmatrix.

        # VERIFIED: [CF] cross-engine consistency
        """
        from compute.lib.e3_two_parameter_rmatrix import (
            two_param_structure_function_additive,
        )
        u, v = 5.3, 7.1
        val_this = _g_two_param(u, v, H1, H2, H3)
        val_other = two_param_structure_function_additive(u, v, H1, H2, H3)
        assert abs(val_this - val_other) < 1e-10, \
            f"g_ch mismatch: {val_this} vs {val_other}"

    def test_g_matches_holomorphic_cs(self):
        """g(z) matches OmegaBackground.structure_function_at.

        # VERIFIED: [CF] cross-engine consistency
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(Rational(37, 10), Rational(-41, 10))
        z_val = Rational(53, 10)
        val_omega = float(omega.structure_function_at(z_val))
        val_this = _g_rational(float(z_val), H1, H2, H3)
        assert abs(val_this - val_omega) < 1e-10, \
            f"g(z) mismatch: {val_this} vs {val_omega}"

    def test_macmahon_matches_holomorphic_cs(self):
        """Plane partition counts match holomorphic_cs_chiral_engine.

        # VERIFIED: [CF] cross-engine consistency
        """
        from compute.lib.holomorphic_cs_chiral_engine import _macmahon_coefficient
        for n in range(8):
            pp = _plane_partition_count(n)
            mc = _macmahon_coefficient(n)
            assert pp == mc, \
                f"MacMahon mismatch at n={n}: pp={pp}, mc={mc}"
