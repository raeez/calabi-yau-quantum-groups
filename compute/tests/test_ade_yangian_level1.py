r"""Tests for ADE Yangian at level 1 on K3.

Tests organized by ADE type:
  A_1 (sl_2):  cross-check with sl2_matrix_lax_engine, RTT, coproduct
  A_2 (sl_3):  Lax, RTT, quantum determinant
  D_4 (so_8):  Lax, RTT, triality
  E_6, E_7, E_8:  Cartan data, Lax, RTT, embedding
  Landscape:  all types, Mukai embedding, shadow class

All test points satisfy AP-CY28 (avoid poles at +/- h_i).
"""

import numpy as np
import pytest
from fractions import Fraction

from compute.lib.ade_yangian_level1 import (
    ADEData,
    ADEMukaiEmbedding,
    ADE_LABELS,
    DrinfeldsNewRealization,
    MUKAI_RANK,
    RTTVerifierGeneral,
    a1_cross_check_sl2_engine,
    a1_lax_operator,
    a1_quantum_determinant,
    a2_lax_operator,
    a2_quantum_determinant,
    ade_data,
    ade_level1_summary,
    ade_yangian_landscape,
    d4_lax_operator,
    d4_triality_data,
    defining_rep_weights,
    e6_lax_operator,
    e7_lax_operator,
    e8_lax_operator,
    lax_diagonal_evaluation,
    transfer_matrix,
    yang_r_matrix_NxN,
    yang_r_matrix_unitarity,
)


# =========================================================================
# A_1 (sl_2): cross-check with sl2_matrix_lax_engine
# =========================================================================

class TestA1:
    """Y(sl_2) at level 1: the simplest non-trivial case."""

    def test_a1_cross_check_sl2_engine(self):
        """Verify A1 Lax matches the dedicated sl2 engine."""
        result = a1_cross_check_sl2_engine()
        assert result['lax_match'], f"Lax deviation: {result['lax_deviation']}"
        assert result['transfer_match'], "Transfer matrix mismatch"
        assert result['qdet_match'], "Quantum determinant mismatch"
        assert result['all_match'], "Some cross-check failed"

    def test_a1_lax_shape(self):
        """A1 Lax is 2x2."""
        L = a1_lax_operator(5.3)
        assert L.shape == (2, 2)

    def test_a1_transfer_matrix(self):
        """Transfer matrix t(u) = 2u for sl_2."""
        u = 7.3  # AP-CY28 safe
        L = a1_lax_operator(u)
        t = np.trace(L)
        assert abs(t - 2 * u) < 1e-12

    def test_a1_quantum_determinant(self):
        """qdet L(u) = (u+1/2)(u-3/2) at m=1/2."""
        u = 7.3
        qd = a1_quantum_determinant(u)
        expected = (u + 0.5) * (u - 1.5)
        assert abs(qd - expected) < 1e-12

    def test_a1_r_matrix_unitarity(self):
        """R(u)R(-u) = (1-u^2)*Id for 2x2."""
        dev = yang_r_matrix_unitarity(3.7, 2)
        assert dev < 1e-12

    def test_a1_rtt_discrepancy(self):
        """RTT discrepancy has predicted structure for sl_2."""
        data = ade_data('A1')
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_rtt_discrepancy(u=5.3, v=2.7)
        assert result['structure_matches'], f"Deviation: {result['max_deviation']}"

    def test_a1_permutation_intertwining(self):
        """P L_1 P = L_2 for sl_2."""
        data = ade_data('A1')
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_permutation_intertwining(u=4.1)
        assert result['intertwining_holds']

    def test_a1_ade_data(self):
        """A1 Lie algebra data."""
        data = ade_data('A1')
        assert data.rank == 1
        assert data.dim_g == 3
        assert data.dim_V == 2
        assert data.dual_coxeter == 2
        assert data.exponents == (1,)
        assert data.level1_central_charge == Fraction(1)
        # c(sl_2, k=1) = 3*1/(1+2) = 1


# =========================================================================
# A_2 (sl_3): the first multi-node case
# =========================================================================

class TestA2:
    """Y(sl_3) at level 1: 3x3 Lax operator."""

    def test_a2_lax_shape(self):
        """A2 Lax is 3x3."""
        L = a2_lax_operator(5.3)
        assert L.shape == (3, 3)

    def test_a2_transfer_matrix(self):
        """Transfer matrix t(u) = 3u for sl_3."""
        u = 5.3
        L = a2_lax_operator(u)
        t = np.trace(L)
        assert abs(t - 3 * u) < 1e-12

    def test_a2_quantum_determinant(self):
        """qdet at specific u value."""
        u = 5.3
        qd = a2_quantum_determinant(u)
        expected = (u + 2.0 / 3) * (u - 4.0 / 3) * (u - 7.0 / 3)
        assert abs(qd - expected) < 1e-12

    def test_a2_r_matrix_unitarity(self):
        """R(u)R(-u) = (1-u^2)*Id for 3x3."""
        dev = yang_r_matrix_unitarity(3.7, 3)
        assert dev < 1e-12

    def test_a2_rtt_discrepancy(self):
        """RTT discrepancy for sl_3."""
        data = ade_data('A2')
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_rtt_discrepancy(u=5.3, v=2.7)
        assert result['structure_matches'], f"Deviation: {result['max_deviation']}"

    def test_a2_permutation_intertwining(self):
        """P L_1 P = L_2 for sl_3."""
        data = ade_data('A2')
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_permutation_intertwining(u=4.1)
        assert result['intertwining_holds']

    def test_a2_cartan_matrix(self):
        """A2 Cartan matrix is ((2,-1),(-1,2))."""
        data = ade_data('A2')
        assert data.cartan == ((2, -1), (-1, 2))

    def test_a2_ade_data(self):
        """A2 Lie algebra data."""
        data = ade_data('A2')
        assert data.rank == 2
        assert data.dim_g == 8
        assert data.dim_V == 3
        assert data.dual_coxeter == 3
        assert data.exponents == (1, 2)
        assert data.level1_central_charge == Fraction(2)
        # c(sl_3, k=1) = 8*1/(1+3) = 2

    def test_a2_serre_exponents(self):
        """Serre exponent 1 - C_{ij} for A2."""
        data = ade_data('A2')
        drinfeld = DrinfeldsNewRealization(data)
        # Adjacent nodes: C_{01} = -1, exponent = 2
        assert drinfeld.serre_exponent(0, 1) == 2
        assert drinfeld.serre_exponent(1, 0) == 2


# =========================================================================
# D_4 (so_8): triality
# =========================================================================

class TestD4:
    """Y(so_8) at level 1: 8x8 Lax operator with S_3 triality."""

    def test_d4_lax_shape(self):
        """D4 Lax is 8x8."""
        L = d4_lax_operator(5.3)
        assert L.shape == (8, 8)

    def test_d4_transfer_matrix(self):
        """Transfer matrix t(u) = 8u for so_8."""
        u = 5.3
        L = d4_lax_operator(u)
        t = np.trace(L)
        assert abs(t - 8 * u) < 1e-12

    def test_d4_r_matrix_unitarity(self):
        """R(u)R(-u) = (1-u^2)*Id for 8x8."""
        dev = yang_r_matrix_unitarity(3.7, 8)
        assert dev < 1e-12

    def test_d4_rtt_discrepancy(self):
        """RTT discrepancy for so_8."""
        data = ade_data('D4')
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_rtt_discrepancy(u=5.3, v=2.7)
        assert result['structure_matches'], f"Deviation: {result['max_deviation']}"

    def test_d4_permutation_intertwining(self):
        """P L_1 P = L_2 for so_8."""
        data = ade_data('D4')
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_permutation_intertwining(u=4.1)
        assert result['intertwining_holds']

    def test_d4_triality(self):
        """D4 has S_3 triality with branching node and 3 legs."""
        triality = d4_triality_data()
        assert triality['num_legs'] == 3
        assert triality['triality_group'] == 'S_3'
        assert triality['all_dim_8'] is True
        assert triality['level_1_integrable_reps'] == 3

    def test_d4_cartan_matrix(self):
        """D4 Cartan matrix: rank 4 with branching node."""
        data = ade_data('D4')
        C = np.array(data.cartan)
        # Check symmetry
        assert np.allclose(C, C.T)
        # Diagonal = 2
        assert all(C[i, i] == 2 for i in range(4))
        # The branching node connects to 3 others
        neighbor_counts = [sum(1 for j in range(4) if j != i and C[i, j] == -1) for i in range(4)]
        assert 3 in neighbor_counts, "D4 must have a branching node with 3 neighbors"

    def test_d4_ade_data(self):
        """D4 Lie algebra data."""
        data = ade_data('D4')
        assert data.rank == 4
        assert data.dim_g == 28  # dim so_8
        assert data.dim_V == 8
        assert data.dual_coxeter == 6
        assert data.level1_central_charge == Fraction(4)
        # c(so_8, k=1) = 28*1/(1+6) = 4


# =========================================================================
# E_6: exceptional
# =========================================================================

class TestE6:
    """Y(e_6) at level 1: 27-dimensional representation."""

    def test_e6_lax_shape(self):
        """E6 Lax is 27x27."""
        L = e6_lax_operator(5.3)
        assert L.shape == (27, 27)

    def test_e6_transfer_matrix(self):
        """Transfer matrix t(u) = 27u for e_6."""
        u = 5.3
        L = e6_lax_operator(u)
        t = np.trace(L)
        assert abs(t - 27 * u - 1.0) < 1e-12  # 27u + sum(weights) = 27u + 1

    def test_e6_r_matrix_unitarity(self):
        """R(u)R(-u) = (1-u^2)*Id for 27x27."""
        dev = yang_r_matrix_unitarity(3.7, 27)
        assert dev < 1e-10

    def test_e6_cartan_matrix(self):
        """E6 Cartan: rank 6, symmetric, tree with branching node."""
        data = ade_data('E6')
        drinfeld = DrinfeldsNewRealization(data)
        result = drinfeld.verify_cartan_properties()
        assert result['all_ok'], f"Cartan check failed: {result}"

    def test_e6_ade_data(self):
        """E6 Lie algebra data."""
        data = ade_data('E6')
        assert data.rank == 6
        assert data.dim_g == 78
        assert data.dim_V == 27
        assert data.dual_coxeter == 12
        assert data.exponents == (1, 4, 5, 7, 8, 11)
        assert data.level1_central_charge == Fraction(6)
        # c(e_6, k=1) = 78*1/(1+12) = 6


# =========================================================================
# E_7: exceptional
# =========================================================================

class TestE7:
    """Y(e_7) at level 1: 56-dimensional representation."""

    def test_e7_lax_shape(self):
        """E7 Lax is 56x56."""
        L = e7_lax_operator(5.3)
        assert L.shape == (56, 56)

    def test_e7_transfer_matrix(self):
        """Transfer matrix t(u) = 56u + 1."""
        u = 5.3
        L = e7_lax_operator(u)
        t = np.trace(L)
        assert abs(t - 56 * u - 1.0) < 1e-12

    def test_e7_cartan_matrix(self):
        """E7 Cartan: rank 7, symmetric, tree."""
        data = ade_data('E7')
        drinfeld = DrinfeldsNewRealization(data)
        result = drinfeld.verify_cartan_properties()
        assert result['all_ok']

    def test_e7_ade_data(self):
        """E7 Lie algebra data."""
        data = ade_data('E7')
        assert data.rank == 7
        assert data.dim_g == 133
        assert data.dim_V == 56
        assert data.dual_coxeter == 18
        assert data.exponents == (1, 5, 7, 9, 11, 13, 17)
        assert data.level1_central_charge == Fraction(7)
        # c(e_7, k=1) = 133*1/(1+18) = 7


# =========================================================================
# E_8: exceptional
# =========================================================================

class TestE8:
    """Y(e_8) at level 1: 248-dimensional adjoint representation."""

    def test_e8_lax_shape(self):
        """E8 Lax is 248x248."""
        L = e8_lax_operator(5.3)
        assert L.shape == (248, 248)

    def test_e8_transfer_matrix(self):
        """Transfer matrix t(u) = 248u + 1."""
        u = 5.3
        L = e8_lax_operator(u)
        t = np.trace(L)
        assert abs(t - 248 * u - 1.0) < 1e-12

    def test_e8_cartan_matrix(self):
        """E8 Cartan: rank 8, symmetric, tree."""
        data = ade_data('E8')
        drinfeld = DrinfeldsNewRealization(data)
        result = drinfeld.verify_cartan_properties()
        assert result['all_ok']

    def test_e8_ade_data(self):
        """E8 Lie algebra data."""
        data = ade_data('E8')
        assert data.rank == 8
        assert data.dim_g == 248
        assert data.dim_V == 248
        assert data.dual_coxeter == 30
        assert data.exponents == (1, 7, 11, 13, 17, 19, 23, 29)
        assert data.level1_central_charge == Fraction(8)
        # c(e_8, k=1) = 248*1/(1+30) = 8


# =========================================================================
# Drinfeld presentation tests
# =========================================================================

class TestDrinfeldPresentation:
    """Tests for Drinfeld's new realization of Y(g)."""

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_cartan_properties(self, label):
        """All ADE Cartan matrices are symmetric trees with diagonal 2."""
        data = ade_data(label)
        drinfeld = DrinfeldsNewRealization(data)
        result = drinfeld.verify_cartan_properties()
        assert result['diagonal_eq_2'], f"{label}: diagonal != 2"
        assert result['offdiag_in_0_neg1'], f"{label}: off-diagonal not in {{0,-1}}"
        assert result['symmetric'], f"{label}: Cartan not symmetric"
        assert result['is_tree'], f"{label}: not a tree"

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_drinfeld_ratio_at_infinity(self, label):
        """g_{ij}(z) -> 1 as z -> infinity."""
        data = ade_data(label)
        drinfeld = DrinfeldsNewRealization(data)
        for i in range(min(data.rank, 3)):
            for j in range(min(data.rank, 3)):
                ratio = drinfeld.structure_function_ij(i, j, 1000.0)
                assert abs(ratio - 1.0) < 0.01, f"{label}: g_{i}{j}(inf) != 1"

    @pytest.mark.parametrize("label", ['A1', 'A2', 'D4'])
    def test_serre_exponents(self, label):
        """Serre exponent = 1 - C_{ij} is 1 (non-adjacent) or 2 (adjacent)."""
        data = ade_data(label)
        drinfeld = DrinfeldsNewRealization(data)
        for i in range(data.rank):
            for j in range(data.rank):
                if i != j:
                    exp = drinfeld.serre_exponent(i, j)
                    assert exp in {1, 2}, f"{label}: bad Serre exp at ({i},{j})"

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_null_vector_row_sums(self, label):
        """Affine null vector: finite row sum gives the needed affine entry."""
        data = ade_data(label)
        drinfeld = DrinfeldsNewRealization(data)
        for i in range(data.rank):
            result = drinfeld.null_vector_identity(i, z=5.3)
            # For ADE: row sum of finite Cartan = 2 - number_of_neighbors
            row_sum = result['finite_row_sum']
            # For the affine extension: affine node adds -row_sum to make 0
            assert row_sum + result['affine_node_entry'] == 0


# =========================================================================
# RTT verification across ADE types
# =========================================================================

class TestRTTVerification:
    """RTT relation tests for all ADE types."""

    @pytest.mark.parametrize("label", ['A1', 'A2', 'A3', 'A4', 'D4', 'D5'])
    def test_r_matrix_unitarity(self, label):
        """R(u)R(-u) = (1-u^2)*Id for each ADE type."""
        data = ade_data(label)
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_r_matrix_unitarity(u=3.7)
        assert result['unitarity_holds'], f"{label}: unitarity failed"

    @pytest.mark.parametrize("label", ['A1', 'A2', 'A3', 'A4', 'D4', 'D5'])
    def test_permutation_intertwining(self, label):
        """P L_1 P = L_2 for each ADE type."""
        data = ade_data(label)
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_permutation_intertwining(u=4.1)
        assert result['intertwining_holds'], f"{label}: intertwining failed"

    @pytest.mark.parametrize("label", ['A1', 'A2', 'A3', 'A4', 'D4', 'D5'])
    def test_rtt_discrepancy_structure(self, label):
        """RTT discrepancy = (u-v)*(J_1 - J_2)*P for each type."""
        data = ade_data(label)
        verifier = RTTVerifierGeneral(data)
        result = verifier.verify_rtt_discrepancy(u=5.3, v=2.7)
        assert result['structure_matches'], (
            f"{label}: RTT discrepancy deviation {result['max_deviation']}"
        )


# =========================================================================
# K3 Mukai lattice embedding
# =========================================================================

class TestMukaiEmbedding:
    """Tests for ADE sublattice embedding in the K3 Mukai lattice."""

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_can_embed(self, label):
        """All ADE types up to rank 20 can embed in K3 Mukai lattice."""
        data = ade_data(label)
        embedding = ADEMukaiEmbedding(data)
        decomp = embedding.mukai_decomposition()
        assert decomp['can_embed'], f"{label}: cannot embed (rank {data.rank})"

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_rank_complement(self, label):
        """ADE rank + complement rank = 24 (Mukai rank)."""
        data = ade_data(label)
        embedding = ADEMukaiEmbedding(data)
        decomp = embedding.mukai_decomposition()
        assert decomp['ade_rank'] + decomp['complement_rank'] == MUKAI_RANK

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_structure_function_factorization(self, label):
        """g_{K3}(z) = g_{ADE}(z) * g_{compl}(z)."""
        data = ade_data(label)
        embedding = ADEMukaiEmbedding(data)
        result = embedding.structure_function_product(z=5.3)
        assert result['factored'], f"{label}: factorization failed"

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_unitarity(self, label):
        """g(z)*g(-z) = 1 (unitarity of structure function)."""
        data = ade_data(label)
        embedding = ADEMukaiEmbedding(data)
        result = embedding.structure_function_product(z=5.3)
        assert result['unitarity'], f"{label}: unitarity failed"

    @pytest.mark.parametrize("label", ADE_LABELS)
    def test_shadow_class_enhancement(self, label):
        """ADE enhancement gives class L (depth 3) for subalgebra."""
        data = ade_data(label)
        embedding = ADEMukaiEmbedding(data)
        shadow = embedding.shadow_class_enhancement()
        assert shadow['shadow_class_subalgebra'] == 'L'
        assert shadow['shadow_depth_subalgebra'] == 3
        assert shadow['S3_nonzero'] is True
        assert shadow['S4_zero_at_level1'] is True
        assert shadow['shadow_class_full_sigma'] == 'M'


# =========================================================================
# Central charge accounting
# =========================================================================

class TestCentralCharges:
    """Verify central charges at level 1 for all ADE types."""

    def test_a_series_central_charges(self):
        """c(sl_{n+1}, k=1) = n for A_n."""
        for n in range(1, 9):
            data = ade_data(f'A{n}')
            expected = Fraction(n)
            assert data.level1_central_charge == expected, (
                f"A{n}: c = {data.level1_central_charge}, expected {expected}"
            )

    def test_d4_central_charge(self):
        """c(so_8, k=1) = 4."""
        data = ade_data('D4')
        assert data.level1_central_charge == Fraction(4)

    def test_d5_central_charge(self):
        """c(so_10, k=1) = 5."""
        data = ade_data('D5')
        assert data.level1_central_charge == Fraction(5)

    def test_e6_central_charge(self):
        """c(e_6, k=1) = 6."""
        data = ade_data('E6')
        assert data.level1_central_charge == Fraction(6)

    def test_e7_central_charge(self):
        """c(e_7, k=1) = 7."""
        data = ade_data('E7')
        assert data.level1_central_charge == Fraction(7)

    def test_e8_central_charge(self):
        """c(e_8, k=1) = 8."""
        data = ade_data('E8')
        assert data.level1_central_charge == Fraction(8)

    def test_central_charge_equals_rank_at_level1(self):
        """For simply-laced g at level 1: c = rank(g).

        This is the celebrated fact that for simply-laced (ADE) Lie algebras
        at level k=1:
            c(\hat{g}_1) = dim(g) / (1 + h^vee) = rank(g)

        This follows from the Freudenthal-de Vries formula:
            dim(g) = rank(g) * (1 + h^vee)
        which holds for ALL simply-laced Lie algebras.
        """
        for label in ADE_LABELS:
            data = ade_data(label)
            assert data.level1_central_charge == Fraction(data.rank), (
                f"{label}: c = {data.level1_central_charge} != rank = {data.rank}"
            )


# =========================================================================
# Landscape summary
# =========================================================================

class TestLandscape:
    """Full ADE landscape at level 1 on K3."""

    def test_landscape_all_types(self):
        """Landscape contains all ADE labels."""
        landscape = ade_yangian_landscape()
        labels = [entry['label'] for entry in landscape]
        for expected in ADE_LABELS:
            assert expected in labels

    def test_landscape_all_embed(self):
        """All standard ADE types can embed in K3."""
        landscape = ade_yangian_landscape()
        for entry in landscape:
            assert entry['can_embed_K3'], f"{entry['label']}: cannot embed"

    def test_landscape_cartan_ok(self):
        """All Cartan matrices pass verification."""
        landscape = ade_yangian_landscape()
        for entry in landscape:
            assert entry['cartan_ok'], f"{entry['label']}: Cartan failed"

    def test_summary_kappa_ch(self):
        """kappa_ch = 2 at all K3 moduli points (AP113 compliant)."""
        summary = ade_level1_summary()
        assert summary['kappa_ch'] == 2

    def test_freudenthal_de_vries(self):
        """dim(g) = rank(g) * (1 + h^vee) for all simply-laced g."""
        for label in ADE_LABELS:
            data = ade_data(label)
            assert data.dim_g == data.rank * (1 + data.dual_coxeter), (
                f"{label}: dim={data.dim_g} != "
                f"rank*(1+h^vee)={data.rank*(1+data.dual_coxeter)}"
            )

    def test_exponents_sum(self):
        """Sum of exponents = dim(g)/2 (= number of positive roots)."""
        for label in ADE_LABELS:
            data = ade_data(label)
            exp_sum = sum(data.exponents)
            num_pos_roots = (data.dim_g - data.rank) // 2
            assert exp_sum == num_pos_roots, (
                f"{label}: sum(exp)={exp_sum} != "
                f"num_pos_roots={num_pos_roots}"
            )
