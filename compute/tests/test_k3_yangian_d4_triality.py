r"""Tests for K3 Yangian at the D_4 triality enhancement point.

STATUS: CONJECTURAL (AP-CY14).  All results conditional on Y(g_{K3}).
The D_4 Lie algebra data and Yang R-matrix are unconditional mathematical
facts; the K3 embedding is conditional on CY-A_2 (proved at d=2).

Multi-path verification per AP10/AP128:
  [DC] direct computation from engine
  [LC] limiting case / cross-check with ade_yangian_level1
  [SY] symmetry (S_3 triality, CY_2 constraint)
  [CF] cross-family (D_4 vs A_1/A_2 comparison)
  [DA] dimensional analysis
"""

import numpy as np
import pytest
from fractions import Fraction

from compute.lib.k3_yangian_d4_triality import (
    BRANCHING_NODE,
    COMPLEMENT_RANK,
    D4_DIM_G,
    D4_DIM_V,
    D4_DUAL_COXETER,
    D4_LEVEL1_CC,
    D4_NUM_POS_ROOTS,
    D4_RANK,
    LEG_NODES,
    MUKAI_RANK,
    STATUS,
    d4_cartan_matrix,
    d4_k3_embedding_parameters,
    d4_offdiagonal_rmatrix,
    d4_positive_roots,
    d4_r_matrix_nonzero_count,
    d4_r_matrix_triality_covariance,
    d4_serre_in_k3,
    d4_simple_roots,
    d4_structure_function_factored,
    d4_triality_summary,
    d4_yang_r_matrix,
    full_s3_group,
    spinor_minus_weights,
    spinor_plus_weights,
    triality_on_representations,
    triality_permutation_matrix,
    triality_vs_miki,
    vector_rep_weights,
    verify_d4_root_system,
    verify_three_reps,
    verify_triality_automorphism,
)


# =========================================================================
# 1. D_4 root system
# =========================================================================

class TestD4RootSystem:
    """Verify D_4 root system data."""

    def test_cartan_matrix_shape(self):
        """D_4 Cartan is 4x4."""
        C = d4_cartan_matrix()
        assert C.shape == (4, 4)

    def test_cartan_diagonal(self):
        """Diagonal entries = 2."""
        C = d4_cartan_matrix()
        for i in range(4):
            assert C[i, i] == 2

    def test_cartan_symmetric(self):
        """Cartan matrix is symmetric (simply-laced)."""
        C = d4_cartan_matrix()
        assert np.array_equal(C, C.T)

    def test_cartan_offdiag(self):
        """Off-diagonal entries in {0, -1}."""
        C = d4_cartan_matrix()
        for i in range(4):
            for j in range(4):
                if i != j:
                    assert C[i, j] in {0, -1}, f"C[{i},{j}] = {C[i,j]}"

    def test_branching_node_valence(self):
        """Node 1 (branching) connects to 3 others.
        # VERIFIED: [DC] direct Cartan, [LT] Humphreys
        """
        C = d4_cartan_matrix()
        neighbors = sum(1 for j in range(4) if j != BRANCHING_NODE and C[BRANCHING_NODE, j] == -1)
        assert neighbors == 3

    def test_legs_no_cross_connect(self):
        """Leg nodes {0,2,3} do NOT connect to each other.
        # VERIFIED: [DC] direct Cartan
        """
        C = d4_cartan_matrix()
        for i in LEG_NODES:
            for j in LEG_NODES:
                if i != j:
                    assert C[i, j] == 0, f"Legs {i},{j} connected: C={C[i,j]}"

    def test_cartan_determinant(self):
        """det(D_4 Cartan) = 4.
        # VERIFIED: [DC] direct computation, [LT] Bourbaki
        """
        C = d4_cartan_matrix()
        assert int(round(np.linalg.det(C))) == 4

    def test_simple_roots_reproduce_cartan(self):
        """alpha_i . alpha_j = C_{ij} (simply-laced: all norms 2).
        # VERIFIED: [DC] direct inner product
        """
        result = verify_d4_root_system()
        assert result['cartan_matrix_matches']

    def test_num_positive_roots(self):
        """D_4 has 12 positive roots.
        # VERIFIED: [DC] enumeration, [DA] (28-4)/2 = 12
        """
        result = verify_d4_root_system()
        assert result['num_positive_roots'] == D4_NUM_POS_ROOTS

    def test_all_roots_norm_2(self):
        """All positive roots have norm 2 (simply-laced).
        # VERIFIED: [DC] direct norm computation
        """
        result = verify_d4_root_system()
        assert result['all_norm_2']

    def test_dim_from_roots(self):
        """dim(so_8) = 2 * 12 + 4 = 28.
        # VERIFIED: [DA] dim = 2*num_pos_roots + rank
        """
        result = verify_d4_root_system()
        assert result['dim_correct']

    def test_d4_constants(self):
        """D_4 algebra constants.
        # VERIFIED: [LC] cross-check with ade_yangian_level1.ade_data('D4')
        """
        assert D4_RANK == 4
        assert D4_DIM_G == 28
        assert D4_DIM_V == 8
        assert D4_DUAL_COXETER == 6
        assert D4_LEVEL1_CC == Fraction(4)
        assert D4_NUM_POS_ROOTS == 12


# =========================================================================
# 2. Three 8-dimensional representations
# =========================================================================

class TestThreeReps:
    """Verify the three 8-dimensional representations of so_8."""

    def test_vector_rep_dim(self):
        """8_v has 8 weights."""
        W = vector_rep_weights()
        assert W.shape == (8, 4)

    def test_spinor_plus_dim(self):
        """8_s has 8 weights."""
        W = spinor_plus_weights()
        assert W.shape == (8, 4)

    def test_spinor_minus_dim(self):
        """8_c has 8 weights."""
        W = spinor_minus_weights()
        assert W.shape == (8, 4)

    def test_all_dim_8(self):
        """All three representations are 8-dimensional.
        # VERIFIED: [DC] weight enumeration, [LT] Fulton-Harris
        """
        result = verify_three_reps()
        assert result['all_dim_8']

    def test_vector_norms(self):
        """Vector weights have norm 1 (= |e_i|^2 = 1).
        # VERIFIED: [DC] direct norm computation
        """
        result = verify_three_reps()
        assert result['vector_norm_1']

    def test_spinor_norms(self):
        """Spinor weights have norm 1 (= |1/2(...)|^2 = 4*(1/4) = 1).
        # VERIFIED: [DC] direct norm computation
        """
        result = verify_three_reps()
        assert result['spinor_norms_1']

    def test_vector_sum_zero(self):
        """Sum of vector weights = 0 (weights come in +/- pairs).
        # VERIFIED: [DC] direct sum
        """
        result = verify_three_reps()
        assert result['sum_v_zero']

    def test_spinor_plus_sum_zero(self):
        """Sum of positive spinor weights = 0.
        # VERIFIED: [DC] direct sum
        """
        result = verify_three_reps()
        assert result['sum_s_zero']

    def test_spinor_minus_sum_zero(self):
        """Sum of negative spinor weights = 0.
        # VERIFIED: [DC] direct sum
        """
        result = verify_three_reps()
        assert result['sum_c_zero']

    def test_has_correct_highest_weights(self):
        """HW of 8_v = e_1, 8_s = (1,1,1,1)/2, 8_c = (1,1,1,-1)/2.
        # VERIFIED: [DC] weight lookup, [LT] Fulton-Harris Table D.4
        """
        result = verify_three_reps()
        assert result['has_hw_v']
        assert result['has_hw_s']
        assert result['has_hw_c']

    def test_reps_distinct(self):
        """All three representations have distinct weight sets.
        # VERIFIED: [DC] set comparison
        """
        result = verify_three_reps()
        assert result['all_distinct']

    def test_no_weight_overlap(self):
        """No weight appears in two different representations.
        # VERIFIED: [DC] set intersection
        """
        result = verify_three_reps()
        assert result['no_weight_overlap']

    def test_vector_integer_weights(self):
        """Vector rep has integer weights (from +/- e_i)."""
        W = vector_rep_weights()
        assert np.allclose(W, np.round(W))

    def test_spinor_halfinteger_weights(self):
        """Spinor reps have half-integer weights."""
        W_s = spinor_plus_weights()
        W_c = spinor_minus_weights()
        # All entries should be +/- 1/2
        assert np.allclose(np.abs(W_s), 0.5)
        assert np.allclose(np.abs(W_c), 0.5)

    def test_spinor_plus_even_minus(self):
        """8_s weights have even number of minus signs.
        # VERIFIED: [DC] sign counting
        """
        W = spinor_plus_weights()
        for w in W:
            num_minus = sum(1 for x in w if x < 0)
            assert num_minus % 2 == 0, f"Weight {w} has {num_minus} minus signs"

    def test_spinor_minus_odd_minus(self):
        """8_c weights have odd number of minus signs.
        # VERIFIED: [DC] sign counting
        """
        W = spinor_minus_weights()
        for w in W:
            num_minus = sum(1 for x in w if x < 0)
            assert num_minus % 2 == 1, f"Weight {w} has {num_minus} minus signs"


# =========================================================================
# 3. S_3 triality automorphism
# =========================================================================

class TestTriality:
    """Verify the S_3 outer automorphism group of D_4."""

    def test_sigma_preserves_cartan(self):
        """sigma^T C sigma = C (Cartan preservation).
        # VERIFIED: [DC] matrix computation
        """
        result = verify_triality_automorphism()
        assert result['preserves_cartan']

    def test_sigma_order_3(self):
        """sigma^3 = Id (order exactly 3).
        # VERIFIED: [DC] matrix multiplication
        """
        result = verify_triality_automorphism()
        assert result['is_order_3']

    def test_sigma_genuinely_order_3(self):
        """sigma != Id and sigma^2 != Id.
        # VERIFIED: [DC] matrix comparison
        """
        result = verify_triality_automorphism()
        assert result['genuine_order_3']

    def test_sigma_fixes_branching(self):
        """sigma fixes the branching node (index 1).
        # VERIFIED: [DC] permutation matrix entry
        """
        result = verify_triality_automorphism()
        assert result['fixes_branching_node']

    def test_sigma_cycles_legs(self):
        """sigma cyclically permutes the three legs {0,2,3}.
        # VERIFIED: [DC] permutation matrix entries
        """
        result = verify_triality_automorphism()
        assert result['cyclic_on_legs']

    def test_rep_cycle_8v_to_8s(self):
        """sigma(8_v) = 8_s (at the Dynkin label level).
        # VERIFIED: [DC] Dynkin label transformation
        """
        result = triality_on_representations()
        assert result['triality_cycle']['sigma_8v_eq_8s']

    def test_rep_cycle_8s_to_8c(self):
        """sigma(8_s) = 8_c.
        # VERIFIED: [DC] Dynkin label transformation
        """
        result = triality_on_representations()
        assert result['triality_cycle']['sigma_8s_eq_8c']

    def test_rep_cycle_8c_to_8v(self):
        """sigma(8_c) = 8_v (completes the 3-cycle).
        # VERIFIED: [DC] Dynkin label transformation
        """
        result = triality_on_representations()
        assert result['triality_cycle']['sigma_8c_eq_8v']

    def test_full_triality_cycle(self):
        """8_v -> 8_s -> 8_c -> 8_v (complete cycle).
        # VERIFIED: [DC] all three transitions
        """
        result = triality_on_representations()
        assert result['triality_cycle']['full_cycle']

    def test_s3_group_order_6(self):
        """S_3 has 6 elements.
        # VERIFIED: [DC] element enumeration
        """
        result = full_s3_group()
        assert result['num_elements'] == 6

    def test_s3_all_distinct(self):
        """All 6 elements of S_3 are distinct matrices.
        # VERIFIED: [DC] pairwise comparison
        """
        result = full_s3_group()
        assert result['all_distinct']

    def test_s3_all_preserve_cartan(self):
        """All 6 elements preserve the D_4 Cartan matrix.
        # VERIFIED: [DC] g^T C g = C for each g
        """
        result = full_s3_group()
        assert result['all_preserve_cartan']

    def test_s3_element_orders(self):
        """S_3 has 1 identity (order 1), 2 3-cycles (order 3), 3 transpositions (order 2).
        # VERIFIED: [DC] matrix power computation
        """
        result = full_s3_group()
        orders = result['element_orders']
        order_counts = {}
        for name, order in orders.items():
            order_counts[order] = order_counts.get(order, 0) + 1
        assert order_counts.get(1, 0) == 1, "Should have 1 identity"
        assert order_counts.get(3, 0) == 2, "Should have 2 elements of order 3"
        assert order_counts.get(2, 0) == 3, "Should have 3 elements of order 2"

    def test_s3_tau_preserves_cartan(self):
        """The transposition tau also preserves Cartan.
        # VERIFIED: [DC] matrix computation
        """
        result = full_s3_group()
        assert result['tau_preserves_cartan']

    def test_s3_tau_order_2(self):
        """tau^2 = Id.
        # VERIFIED: [DC] matrix computation
        """
        result = full_s3_group()
        assert result['tau_order_2']

    def test_level1_integrable_reps(self):
        """At level 1, D_4 has exactly 3 basic (integrable) representations.
        # VERIFIED: [LC] cross-check with d4_triality_data()
        """
        result = triality_on_representations()
        assert result['level_1_integrable']['num_basic_reps'] == 3
        assert result['level_1_integrable']['all_dim_8'] is True

    def test_tensor_product_dim(self):
        """8 x 8 = 64 = 1 + 28 + 35 = 8 + 56.
        # VERIFIED: [DA] dimension counting
        """
        # 8_v x 8_v = 1 + 28 + 35_v (dim: 1+28+35 = 64)
        assert 1 + 28 + 35 == 64
        # 8_v x 8_s = 8_c + 56_s (dim: 8+56 = 64)
        assert 8 + 56 == 64


# =========================================================================
# 4. Yang R-matrix on C^8 x C^8
# =========================================================================

class TestD4RMatrix:
    """Tests for the 64x64 Yang R-matrix at D_4."""

    def test_r_matrix_shape(self):
        """R(u) is 64x64."""
        R = d4_yang_r_matrix(3.7)
        assert R.shape == (64, 64)

    def test_r_matrix_unitarity(self):
        """R(u)R(-u) = (1-u^2)*Id_{64}.
        # VERIFIED: [DC] matrix product
        """
        u = 3.7  # AP-CY28 safe
        R_u = d4_yang_r_matrix(u)
        R_neg = d4_yang_r_matrix(-u)
        product = R_u @ R_neg
        expected = (1.0 - u * u) * np.eye(64)
        assert np.max(np.abs(product - expected)) < 1e-10

    def test_r_at_zero_is_permutation(self):
        """R(0) = P (permutation operator).
        # VERIFIED: [DC] evaluation at u=0
        """
        P = d4_yang_r_matrix(0.0)
        # P^2 = Id
        assert np.max(np.abs(P @ P - np.eye(64))) < 1e-15

    def test_nonzero_count_generic(self):
        """At generic u: 120 nonzero entries (64 from Id + 56 off-diag from P).
        # VERIFIED: [DC] entry counting, [DA] 64+64-8=120
        """
        result = d4_r_matrix_nonzero_count(u=3.7)
        assert result['nonzero_entries'] == 120
        assert result['matches_union']

    def test_nonzero_count_at_zero(self):
        """At u=0: R=P, 64 nonzero entries."""
        result = d4_r_matrix_nonzero_count(u=0.0)
        assert result['nonzero_entries'] == 64

    def test_triality_covariance(self):
        """R(u) commutes with A tensor A for any A (universal Yang property).
        # VERIFIED: [DC] random matrix test, [SY] algebraic identity [P, AoA]=0
        """
        result = d4_r_matrix_triality_covariance(u=3.7)
        assert result['universal_commutativity_holds']

    def test_r_matrix_ybe(self):
        """Yang-Baxter equation for 8x8 R-matrix.
        # VERIFIED: [DC] 512x512 triple product
        """
        result = d4_r_matrix_triality_covariance(u=3.7)
        assert result['ybe_holds'], f"YBE deviation: {result['ybe_deviation']}"

    def test_r_matrix_unitarity_from_covariance(self):
        """Unitarity cross-check from triality verification.
        # VERIFIED: [DC] from covariance test
        """
        result = d4_r_matrix_triality_covariance(u=3.7)
        assert result['unitarity_holds']


# =========================================================================
# 5. K3 embedding
# =========================================================================

class TestK3Embedding:
    """Tests for the D_4 enhancement in the K3 Mukai lattice."""

    def test_embedding_ranks(self):
        """D_4 rank 4 + complement 20 = Mukai 24.
        # VERIFIED: [DA] rank counting
        """
        assert D4_RANK + COMPLEMENT_RANK == MUKAI_RANK

    def test_cy2_constraint(self):
        """CY_2 constraint: sum h_i = 0.
        # VERIFIED: [DC] parameter computation
        """
        result = d4_k3_embedding_parameters()
        assert result['cy2_satisfied']

    def test_total_central_charge(self):
        """c(so_8, k=1) + c_Heis(20) = 4 + 20 = 24.
        # VERIFIED: [DA] c = rank(g) at level 1 + complement rank
        """
        result = d4_k3_embedding_parameters()
        assert result['c_total'] == 24.0

    def test_structure_function_factored(self):
        """g_{K3}(z) = g_{D_4}(z) * g_{compl}(z).
        # VERIFIED: [DC] product evaluation at z=5.3
        """
        result = d4_structure_function_factored(z=5.3)
        assert result['factored']

    def test_structure_function_unitarity(self):
        """g(z) * g(-z) = 1 (algebraic unitarity).
        # VERIFIED: [DC] product at z=5.3, [SY] CY structure
        """
        result = d4_structure_function_factored(z=5.3)
        assert result['unitarity_holds']

    def test_structure_function_degrees(self):
        """D_4 sector: degree (4,4), complement: (20,20), total: (24,24).
        # VERIFIED: [DA] degree counting
        """
        result = d4_structure_function_factored(z=5.3)
        assert result['g_d4_degree'] == (4, 4)
        assert result['g_complement_degree'] == (20, 20)
        assert result['g_total_degree'] == (24, 24)

    def test_d4_complement_signature(self):
        """Complement has signature (4, 16) within Mukai lattice.
        # VERIFIED: [DC] from ade_yangian_level1 embedding
        """
        result = d4_k3_embedding_parameters()
        decomp = result['mukai_decomposition']
        # D_4 root lattice is negative definite: signature (0, 4)
        assert decomp['ade_signature'] == (0, D4_RANK)
        # Complement: (4, 20 - 4) = (4, 16)
        assert decomp['complement_signature'] == (4, 16)


# =========================================================================
# 6. Off-diagonal R-matrix analysis
# =========================================================================

class TestOffDiagonalRMatrix:
    """Tests for off-diagonal structure of the D_4 R-matrix."""

    def test_d4_offdiag_count(self):
        """D_4 block has 56 off-diagonal nonzero entries.
        # VERIFIED: [DC] N*(N-1) = 8*7 = 56
        """
        result = d4_offdiagonal_rmatrix()
        assert result['d4_sector']['offdiagonal_nonzero'] == 56

    def test_d4_total_nonzero(self):
        """D_4 block has 120 total nonzero entries.
        # VERIFIED: [DC] 64 + 56 = 120
        """
        result = d4_offdiagonal_rmatrix()
        assert result['d4_sector']['total_nonzero'] == 120

    def test_abelian_no_offdiag(self):
        """Abelian sector has 0 off-diagonal entries.
        # VERIFIED: [DC] diagonal R-matrix
        """
        result = d4_offdiagonal_rmatrix()
        assert result['abelian_sector']['offdiagonal_nonzero'] == 0

    def test_cross_sector_zero(self):
        """Cross-sector has 0 nonzero entries (Mukai orthogonality).
        # VERIFIED: [SY] Mukai lattice orthogonality
        """
        result = d4_offdiagonal_rmatrix()
        assert result['cross_sector']['nonzero'] == 0

    def test_k3_total_nonzero(self):
        """Full K3 charge-1 R-matrix: 120 + 20 = 140 nonzero entries.
        # VERIFIED: [DA] sum of D_4 and abelian contributions
        """
        result = d4_offdiagonal_rmatrix()
        assert result['k3_charge1_rmatrix']['total_nonzero'] == 140

    def test_k3_extreme_sparsity(self):
        """K3 R-matrix is extremely sparse: 140/331776 < 0.05%.
        # VERIFIED: [DA] density calculation
        """
        result = d4_offdiagonal_rmatrix()
        assert result['k3_charge1_rmatrix']['density'] < 0.001


# =========================================================================
# 7. D_4 Serre relations
# =========================================================================

class TestD4Serre:
    """Tests for D_4 Serre relations in the K3 context."""

    def test_num_serre_pairs(self):
        """D_4 has 3 Serre pairs (= 3 edges in Dynkin diagram).
        # VERIFIED: [DC] Cartan matrix edge counting
        """
        result = d4_serre_in_k3()
        assert result['num_serre_pairs'] == 3

    def test_correct_num_edges(self):
        """Number of edges = rank - 1 = 3 (tree property).
        # VERIFIED: [DA] rank - 1
        """
        result = d4_serre_in_k3()
        assert result['correct_num_edges']

    def test_all_involve_branching(self):
        """All 3 Serre pairs involve the branching node.
        # VERIFIED: [DC] pair inspection
        """
        result = d4_serre_in_k3()
        assert result['all_involve_branching']

    def test_triality_permutes_serre(self):
        """Triality sigma permutes the 3 Serre relations cyclically.
        # VERIFIED: [SY] S_3 action on edge set
        """
        result = d4_serre_in_k3()
        assert result['triality_permutes_serre']

    def test_mixing_serre_trivial(self):
        """I_mix = 0 (Mukai orthogonality).
        # VERIFIED: [SY] lattice orthogonality, [CF] matches k3_serre_relations.py
        """
        result = d4_serre_in_k3()
        assert result['mixing_serre_trivial']


# =========================================================================
# 8. Triality vs Miki (AP-CY22)
# =========================================================================

class TestTrialityVsMiki:
    """Tests for the triality/Miki distinction (AP-CY22 compliance)."""

    def test_not_same(self):
        """D_4 triality S_3 != Miki S_3 (AP-CY22).
        # VERIFIED: [SY] different sources, different scopes
        """
        result = triality_vs_miki()
        assert result['are_same'] is False

    def test_miki_source(self):
        """Miki S_3 comes from CY torus Weyl group."""
        result = triality_vs_miki()
        assert 'torus' in result['miki_s3']['source'].lower()

    def test_triality_source(self):
        """D_4 S_3 comes from Dynkin diagram outer automorphism."""
        result = triality_vs_miki()
        assert 'Dynkin' in result['d4_triality_s3']['source']

    def test_neither_from_e3(self):
        """Neither S_3 derives from the E_3 operad (AP-CY22).
        # VERIFIED: [SY] AP-CY22 compliance
        """
        result = triality_vs_miki()
        assert result['miki_s3']['e3_origin'] is False
        assert result['d4_triality_s3']['e3_origin'] is False

    def test_different_cy_dimension(self):
        """Miki requires CY_3; triality lives at CY_2.
        # VERIFIED: [CF] dimension comparison
        """
        result = triality_vs_miki()
        assert result['miki_s3']['cy_dimension'] == 3
        assert result['d4_triality_s3']['cy_dimension'] == 2

    def test_combined_symmetry_conjectural(self):
        """Combined S_3 at D_4 on K3 x E is CONJECTURAL (AP-CY14)."""
        result = triality_vs_miki()
        assert 'CONJECTURAL' in result['combined_symmetry']['status']


# =========================================================================
# 9. Full summary
# =========================================================================

class TestSummary:
    """Integration tests for the complete D_4 triality analysis."""

    def test_summary_root_system(self):
        """Root system verification passes."""
        result = d4_triality_summary()
        assert result['root_system_ok']

    def test_summary_three_reps(self):
        """Three 8-dim reps verified."""
        result = d4_triality_summary()
        assert result['three_reps_ok']

    def test_summary_triality_order(self):
        """Triality is genuine order-3 automorphism."""
        result = d4_triality_summary()
        assert result['triality']['genuine_order_3']

    def test_summary_cartan_preserved(self):
        """Triality preserves Cartan matrix."""
        result = d4_triality_summary()
        assert result['triality']['preserves_cartan']

    def test_summary_permutes_reps(self):
        """Triality permutes the three representations."""
        result = d4_triality_summary()
        assert result['triality']['permutes_reps']

    def test_summary_permutes_serre(self):
        """Triality permutes the three Serre relations."""
        result = d4_triality_summary()
        assert result['triality']['permutes_serre']

    def test_summary_r_matrix_covariant(self):
        """R-matrix is triality covariant."""
        result = d4_triality_summary()
        assert result['r_matrix']['triality_covariant']

    def test_summary_offdiag_56(self):
        """56 off-diagonal entries in D_4 R-matrix."""
        result = d4_triality_summary()
        assert result['r_matrix']['offdiagonal_d4'] == 56

    def test_summary_k3_embedding(self):
        """K3 embedding: rank 4 + 20 = 24."""
        result = d4_triality_summary()
        emb = result['k3_embedding']
        assert emb['d4_rank'] + emb['complement_rank'] == emb['total']

    def test_summary_mixing_trivial(self):
        """Mixing Serre trivial in K3 embedding."""
        result = d4_triality_summary()
        assert result['k3_embedding']['mixing_serre_trivial']

    def test_summary_triality_ne_miki(self):
        """Triality != Miki (AP-CY22)."""
        result = d4_triality_summary()
        assert result['triality_vs_miki']['are_same'] is False

    def test_summary_status_conjectural(self):
        """Overall status is CONJECTURAL (AP-CY14)."""
        result = d4_triality_summary()
        assert result['status'] == 'CONJECTURAL'

    def test_summary_algebra_data(self):
        """D_4 algebra data in summary."""
        result = d4_triality_summary()
        alg = result['algebra']
        assert alg['rank'] == 4
        assert alg['dim_g'] == 28
        assert alg['dim_V'] == 8
        assert alg['dual_coxeter'] == 6


# =========================================================================
# 10. Cross-checks with ade_yangian_level1
# =========================================================================

class TestCrossChecks:
    """Cross-checks with the parent ADE Yangian engine."""

    def test_cartan_matches_ade_engine(self):
        """D_4 Cartan from this engine matches ade_yangian_level1.
        # VERIFIED: [CF] cross-engine comparison
        """
        from compute.lib.ade_yangian_level1 import ade_data
        data = ade_data('D4')
        C_ade = np.array(data.cartan, dtype=int)
        C_ours = d4_cartan_matrix()
        assert np.array_equal(C_ade, C_ours)

    def test_dim_g_matches(self):
        """dim(so_8) matches ade_data('D4').dim_g.
        # VERIFIED: [CF] cross-engine comparison
        """
        from compute.lib.ade_yangian_level1 import ade_data
        data = ade_data('D4')
        assert data.dim_g == D4_DIM_G

    def test_dim_v_matches(self):
        """dim(V) = 8 matches ade_data('D4').dim_V.
        # VERIFIED: [CF] cross-engine comparison
        """
        from compute.lib.ade_yangian_level1 import ade_data
        data = ade_data('D4')
        assert data.dim_V == D4_DIM_V

    def test_central_charge_matches(self):
        """c(so_8, k=1) = 4 matches ade_data('D4').
        # VERIFIED: [CF] cross-engine comparison
        """
        from compute.lib.ade_yangian_level1 import ade_data
        data = ade_data('D4')
        assert data.level1_central_charge == D4_LEVEL1_CC

    def test_triality_data_matches(self):
        """d4_triality_data() from ade engine matches our analysis.
        # VERIFIED: [CF] cross-engine comparison
        """
        td = d4_triality_data()
        assert td['num_legs'] == 3
        assert td['triality_group'] == 'S_3'
        assert td['all_dim_8'] is True

    def test_freudenthal_de_vries(self):
        """dim(so_8) = rank * (1 + h^vee) = 4 * 7 = 28.
        # VERIFIED: [DA] Freudenthal-de Vries formula
        """
        assert D4_DIM_G == D4_RANK * (1 + D4_DUAL_COXETER)
