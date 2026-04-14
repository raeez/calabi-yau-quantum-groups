r"""Tests for sl_2 matrix Lax engine.

Verifies:
1. Yang R-matrix properties (unitarity, YBE)
2. RTT consequences: permutation intertwining, R-unitarity, transfer commutativity
3. RTT discrepancy structure for commuting evaluations
4. Matrix coproduct Delta_z(L) = L^L . L^R(u-z)
5. Trace-coassociativity
6. Entry-wise coassociativity failure mechanism
7. Quantum determinant centrality and Serre connection
8. Cross-check with Serre engine structure function
9. gl_1 vs sl_2 comparison
10. Full verification suite

AP-CY28 compliance: test points use large primes to avoid poles at z = +/- h_i.
"""

from fractions import Fraction as F

from compute.lib.sl2_matrix_lax_engine import (
    LaxOperator,
    MatrixCoproduct,
    RTTVerifier,
    SerreFromLax,
    gl1_vs_sl2_lax_comparison,
    sl2_matrix_lax_full_verification,
    yang_r_matrix,
    _mat4_mul,
    _L1_from_L,
    _L2_from_L,
    _mat2_mul,
)
from compute.lib.sl2_chiral_coproduct_engine import StructureFunction


# =========================================================================
# 1. YANG R-MATRIX
# =========================================================================

class TestYangRMatrix:
    """Tests for the 4x4 Yang R-matrix R(u) = u*Id + P."""

    def test_r_at_zero(self):
        """R(0) = P (the permutation operator)."""
        R = yang_r_matrix(F(0))
        assert R[0][0] == F(1)  # P_{00,00} = 1
        assert R[1][1] == F(0)  # P_{01,01} = 0
        assert R[1][2] == F(1)  # P_{01,10} = 1
        assert R[2][1] == F(1)  # P_{10,01} = 1
        assert R[2][2] == F(0)  # P_{10,10} = 0
        assert R[3][3] == F(1)  # P_{11,11} = 1

    def test_r_diagonal(self):
        """R(u) diagonal entries: u+1 for same-index, u for cross."""
        u = F(5)
        R = yang_r_matrix(u)
        assert R[0][0] == u + 1  # (00,00)
        assert R[1][1] == u      # (01,01)
        assert R[2][2] == u      # (10,10)
        assert R[3][3] == u + 1  # (11,11)

    def test_r_off_diagonal(self):
        """R(u) off-diagonal: 1 for swap, 0 otherwise."""
        u = F(5)
        R = yang_r_matrix(u)
        assert R[1][2] == F(1)  # (01,10) = 1 (permutation)
        assert R[2][1] == F(1)  # (10,01) = 1 (permutation)
        assert R[0][1] == F(0)  # (00,01) = 0
        assert R[0][2] == F(0)  # (00,10) = 0

    def test_r_product_unitarity(self):
        """R(u) R(-u) = (1 - u^2) Id_4 (from P^2 = Id)."""
        u = F(3)
        R_u = yang_r_matrix(u)
        R_neg_u = yang_r_matrix(-u)
        prod = _mat4_mul(R_u, R_neg_u)
        expected_diag = F(1) - u * u  # = -8
        for i in range(4):
            assert prod[i][i] == expected_diag
            for j in range(4):
                if i != j:
                    assert prod[i][j] == F(0)

    def test_ybe_yang(self):
        """Verify Yang-Baxter equation for R(u) = u*Id + P."""
        u, v, w = F(37), F(41), F(43)
        R12 = yang_r_matrix(u - v)
        R13 = yang_r_matrix(u - w)
        R23 = yang_r_matrix(v - w)
        lhs = _mat4_mul(_mat4_mul(R12, R13), R23)
        rhs = _mat4_mul(_mat4_mul(R23, R13), R12)
        for i in range(4):
            for j in range(4):
                assert lhs[i][j] == rhs[i][j], f"YBE fails at ({i},{j})"


# =========================================================================
# 2. LAX OPERATOR
# =========================================================================

class TestLaxOperator:
    """Tests for the 2x2 Lax operator L(u)."""

    def test_fund_hw_diagonal(self):
        """L(u) on fundamental HW state is diagonal."""
        lax = LaxOperator()
        L = lax.L_fund_highest_weight(F(5))
        assert L[0][0] == F(11, 2)  # u + 1/2
        assert L[1][1] == F(9, 2)   # u - 1/2
        assert L[0][1] == F(0)
        assert L[1][0] == F(0)

    def test_transfer_matrix(self):
        """Transfer matrix tr(L(u)) = 2u."""
        lax = LaxOperator()
        assert lax.transfer_matrix(F(7), F(1, 2), F(1, 2)) == F(14)
        assert lax.transfer_matrix(F(3), F(1), F(0)) == F(6)

    def test_transfer_weight_independent(self):
        """Transfer matrix is weight-independent."""
        lax = LaxOperator()
        u = F(37)
        for j in [F(1, 2), F(1), F(3, 2)]:
            m = j
            vals = []
            while m >= -j:
                vals.append(lax.transfer_matrix(u, j, m))
                m -= F(1)
            assert len(set(vals)) == 1, f"Transfer matrix varies with m at j={j}"

    def test_qdet_fundamental(self):
        """Quantum determinant for j=1/2: u^2 - u - 3/4."""
        lax = LaxOperator()
        u = F(37)
        expected = u * u - u - F(3, 4)
        assert lax.quantum_determinant(u, F(1, 2), F(1, 2)) == expected

    def test_qdet_spin1(self):
        """Quantum determinant for j=1: u^2 - u - 2."""
        lax = LaxOperator()
        u = F(41)
        expected = u * u - u - F(2)
        assert lax.quantum_determinant(u, F(1), F(1)) == expected

    def test_numerical_lax(self):
        """L_numerical produces correct 2x2 matrix."""
        lax = LaxOperator()
        L = lax.L_numerical(F(5), F(1, 2), F(3), F(7))
        assert L[0][0] == F(11, 2)  # u + h
        assert L[0][1] == F(7)      # f
        assert L[1][0] == F(3)      # e
        assert L[1][1] == F(9, 2)   # u - h


# =========================================================================
# 3. RTT CONSEQUENCES
# =========================================================================

class TestRTTConsequences:
    """Tests for numerically verifiable RTT consequences."""

    def test_permutation_intertwining_fund(self):
        """P * L_1(u) * P = L_2(u) for fundamental representation."""
        rtt = RTTVerifier()
        r = rtt.verify_permutation_intertwining(F(37), F(1, 2), F(1, 2))
        assert r["P_L1_P_eq_L2"]

    def test_permutation_intertwining_spin1(self):
        """P * L_1(u) * P = L_2(u) for spin-1."""
        rtt = RTTVerifier()
        r = rtt.verify_permutation_intertwining(F(41), F(1), F(0))
        assert r["P_L1_P_eq_L2"]

    def test_r_unitarity(self):
        """R(u)R(-u) = (1-u^2) Id verified through RTTVerifier."""
        rtt = RTTVerifier()
        r = rtt.verify_r_matrix_unitarity(F(37))
        assert r["unitarity_holds"]

    def test_r_unitarity_small(self):
        """R(u)R(-u) unitarity at small u."""
        rtt = RTTVerifier()
        r = rtt.verify_r_matrix_unitarity(F(3))
        assert r["unitarity_holds"]

    def test_transfer_commutativity_fund(self):
        """Transfer matrix weight-independent for j=1/2."""
        rtt = RTTVerifier()
        r = rtt.verify_transfer_commutativity(F(37), F(41), F(1, 2))
        assert r["commutativity_holds"]

    def test_transfer_commutativity_spin1(self):
        """Transfer matrix weight-independent for j=1."""
        rtt = RTTVerifier()
        r = rtt.verify_transfer_commutativity(F(43), F(47), F(1))
        assert r["commutativity_holds"]

    def test_rtt_discrepancy_structure(self):
        """RTT discrepancy = (u-v)*(J1-J2)*P for commuting evaluations."""
        rtt = RTTVerifier()
        r = rtt.verify_rtt_discrepancy_structure(F(37), F(41), F(1, 2), F(1, 2))
        assert r["discrepancy_matches_prediction"]

    def test_rtt_discrepancy_spin1(self):
        """RTT discrepancy structure for spin-1."""
        rtt = RTTVerifier()
        r = rtt.verify_rtt_discrepancy_structure(F(43), F(47), F(1), F(0))
        assert r["discrepancy_matches_prediction"]


# =========================================================================
# 4. MATRIX COPRODUCT
# =========================================================================

class TestMatrixCoproduct:
    """Tests for the matrix coproduct Delta_z(L) = L^L . L^R(u-z)."""

    def test_diagonal_coproduct(self):
        """Diagonal coproduct has correct tensor structure."""
        mc = MatrixCoproduct()
        r = mc.coproduct_diagonal(F(37), F(7), F(1, 2), F(1, 2))
        # delta_L_00 = (u + m_L, u - z + m_R) = (37.5, 30.5)
        assert r["delta_L_00"][0] == str(F(75, 2))
        assert r["delta_L_00"][1] == str(F(61, 2))

    def test_trace_coproduct_formula(self):
        """Trace of coproduct has correct value."""
        mc = MatrixCoproduct()
        r = mc.coproduct_diagonal(F(37), F(7), F(1, 2), F(1, 2))
        u, z, mL, mR = F(37), F(7), F(1, 2), F(1, 2)
        expected_trace = (u + mL) * (u - z + mR) + (u - mL) * (u - z - mR)
        assert r["trace_coproduct"] == str(expected_trace)


# =========================================================================
# 5. TRACE-COASSOCIATIVITY
# =========================================================================

class TestTraceCoassociativity:
    """Tests for trace-coassociativity of the matrix coproduct."""

    def test_coassoc_fundamental(self):
        """Trace-coassociativity for fundamental weights."""
        mc = MatrixCoproduct()
        r = mc.verify_trace_coassociativity(
            F(37), F(7), F(11), F(1, 2), F(1, 2), F(1, 2)
        )
        assert r["trace_coassociative"]

    def test_coassoc_mixed_weights(self):
        """Trace-coassociativity for mixed weights."""
        mc = MatrixCoproduct()
        r = mc.verify_trace_coassociativity(
            F(41), F(13), F(17), F(1, 2), F(-1, 2), F(1, 2)
        )
        assert r["trace_coassociative"]

    def test_coassoc_spin1(self):
        """Trace-coassociativity for spin-1 weights."""
        mc = MatrixCoproduct()
        r = mc.verify_trace_coassociativity(
            F(43), F(5), F(19), F(1), F(0), F(-1)
        )
        assert r["trace_coassociative"]

    def test_coassoc_large_params(self):
        """Trace-coassociativity at large parameters."""
        mc = MatrixCoproduct()
        r = mc.verify_trace_coassociativity(
            F(101), F(23), F(29), F(3, 2), F(1, 2), F(-3, 2)
        )
        assert r["trace_coassociative"]

    def test_coassoc_zero_z(self):
        """Trace-coassociativity at z=0 (basepoint)."""
        mc = MatrixCoproduct()
        r = mc.verify_trace_coassociativity(
            F(37), F(0), F(11), F(1, 2), F(1, 2), F(1, 2)
        )
        assert r["trace_coassociative"]


# =========================================================================
# 6. ENTRY-WISE COASSOCIATIVITY
# =========================================================================

class TestEntryCoassociativity:
    """Tests for entry-wise coassociativity failure mechanism."""

    def test_numerical_matrices_equal(self):
        """Numerical matrix associativity holds (trivially)."""
        mc = MatrixCoproduct()
        r = mc.verify_entry_coassociativity_failure(F(37), F(7), F(11))
        assert r["numerical_matrices_equal"]

    def test_tensor_paths_differ(self):
        """The two tensor decomposition paths have different structure."""
        mc = MatrixCoproduct()
        r = mc.verify_entry_coassociativity_failure(F(37), F(7), F(11))
        # Both paths should have 4 terms (2x2 summation)
        assert len(r["tensor_path_L_00"]) == 4
        assert len(r["tensor_path_R_00"]) == 4
        # The paths should have different symbolic forms
        assert r["tensor_path_L_00"] != r["tensor_path_R_00"]


# =========================================================================
# 7. QUANTUM DETERMINANT
# =========================================================================

class TestQuantumDeterminant:
    """Tests for quantum determinant centrality and Serre connection."""

    def test_qdet_weight_independent_j_half(self):
        """qdet is weight-independent for j=1/2."""
        serre = SerreFromLax()
        r = serre.qdet_centrality_check(F(37), F(41), F(1, 2))
        assert r["all_equal"]

    def test_qdet_weight_independent_j_1(self):
        """qdet is weight-independent for j=1."""
        serre = SerreFromLax()
        r = serre.qdet_centrality_check(F(37), F(41), F(1))
        assert r["all_equal"]

    def test_qdet_weight_independent_j_3half(self):
        """qdet is weight-independent for j=3/2."""
        serre = SerreFromLax()
        r = serre.qdet_centrality_check(F(37), F(41), F(3, 2))
        assert r["all_equal"]

    def test_qdet_factorization(self):
        """qdet(u) = (u - j - 1)(u + j)."""
        serre = SerreFromLax()
        for j in [F(1, 2), F(1), F(3, 2), F(2)]:
            u = F(37)
            qdet_val = serre.qdet_evaluation(u, j, j)
            factored = (u - j - F(1)) * (u + j)
            assert qdet_val == factored, f"qdet factorization fails at j={j}"

    def test_qdet_zeros(self):
        """qdet vanishes at u = -j and u = j+1."""
        serre = SerreFromLax()
        for j in [F(1, 2), F(1), F(3, 2)]:
            assert serre.qdet_evaluation(-j, j, j) == F(0)
            assert serre.qdet_evaluation(j + F(1), j, j) == F(0)

    def test_serre_from_qdet(self):
        """Serre null vectors from qdet factorization."""
        serre = SerreFromLax()
        r = serre.serre_from_qdet_factorization(F(1, 2))
        assert "-1/2" in r["zeros"]
        assert "3/2" in r["zeros"]


# =========================================================================
# 8. SERRE CROSS-CHECK
# =========================================================================

class TestSerreCrossCheck:
    """Cross-check between Lax qdet and Serre engine structure function."""

    def test_wheel_condition_zeros(self):
        """Wheel condition g_{00}(h_a) = 0 verified."""
        serre = SerreFromLax()
        r = serre.verify_null_vector_from_structure_function()
        assert r["all_wheel_zeros"]

    def test_wheel_custom_params(self):
        """Wheel condition with custom CY parameters."""
        sf = StructureFunction(F(37), F(41))
        serre = SerreFromLax(sf)
        r = serre.verify_null_vector_from_structure_function()
        assert r["all_wheel_zeros"]


# =========================================================================
# 9. gl_1 vs sl_2 COMPARISON
# =========================================================================

class TestGL1vsSL2:
    """Tests for the gl_1 vs sl_2 comparison."""

    def test_comparison_structure(self):
        """Comparison returns the expected structure."""
        r = gl1_vs_sl2_lax_comparison()
        assert "genuinely_new" in r
        assert "what_survives_from_gl1" in r
        assert len(r["genuinely_new"]) == 6

    def test_six_new_features(self):
        """All six genuinely new features are present."""
        r = gl1_vs_sl2_lax_comparison()
        keys = list(r["genuinely_new"].keys())
        assert "1_lax_dimension" in keys
        assert "2_coproduct_type" in keys
        assert "3_rtt_vs_exchange" in keys
        assert "4_quantum_determinant" in keys
        assert "5_trace_coassociativity" in keys
        assert "6_serre_from_lax" in keys


# =========================================================================
# 10. FULL VERIFICATION SUITE
# =========================================================================

class TestFullVerification:
    """Tests for the comprehensive verification suite."""

    def test_all_pass(self):
        """Full verification suite passes."""
        r = sl2_matrix_lax_full_verification()
        assert r["summary"]["all_pass"]

    def test_rtt_consequences_verified(self):
        """RTT consequences verified."""
        r = sl2_matrix_lax_full_verification()
        assert r["summary"]["rtt_consequences_verified"]

    def test_trace_coassoc_verified(self):
        """Trace-coassociativity verified."""
        r = sl2_matrix_lax_full_verification()
        assert r["summary"]["trace_coassociativity_verified"]

    def test_qdet_central(self):
        """Quantum determinant centrality verified."""
        r = sl2_matrix_lax_full_verification()
        assert r["summary"]["quantum_determinant_central"]

    def test_serre_cross_check(self):
        """Serre cross-check passed."""
        r = sl2_matrix_lax_full_verification()
        assert r["summary"]["serre_cross_check_passed"]

    def test_key_results_count(self):
        """Seven key results identified."""
        r = sl2_matrix_lax_full_verification()
        assert len(r["summary"]["key_results"]) == 7


# =========================================================================
# 11. HELPER FUNCTION TESTS
# =========================================================================

class TestHelpers:
    """Tests for helper functions."""

    def test_mat2_mul_identity(self):
        """2x2 identity multiplication."""
        I = [[F(1), F(0)], [F(0), F(1)]]
        A = [[F(3), F(7)], [F(11), F(13)]]
        result = _mat2_mul(I, A)
        assert result == A

    def test_mat2_mul_product(self):
        """2x2 matrix multiplication."""
        A = [[F(1), F(2)], [F(3), F(4)]]
        B = [[F(5), F(6)], [F(7), F(8)]]
        C = _mat2_mul(A, B)
        assert C[0][0] == F(19)  # 1*5 + 2*7
        assert C[0][1] == F(22)  # 1*6 + 2*8
        assert C[1][0] == F(43)  # 3*5 + 4*7
        assert C[1][1] == F(50)  # 3*6 + 4*8

    def test_mat4_mul_identity(self):
        """4x4 identity multiplication."""
        I = [[F(1) if i == j else F(0) for j in range(4)] for i in range(4)]
        A = [[F(i * 4 + j + 1) for j in range(4)] for i in range(4)]
        result = _mat4_mul(I, A)
        for i in range(4):
            for j in range(4):
                assert result[i][j] == A[i][j]

    def test_L1_L2_embedding(self):
        """L_1 and L_2 embeddings are correct."""
        L = [[F(1), F(2)], [F(3), F(4)]]
        L1 = _L1_from_L(L)
        L2 = _L2_from_L(L)

        # L_1 = L tensor Id: (L_1)_{(ia),(jb)} = L_{ij} * delta_{ab}
        assert L1[0][0] == F(1)  # (00,00): L_{00} * delta_{00} = 1
        assert L1[0][1] == F(0)  # (00,01): L_{00} * delta_{01} = 0
        assert L1[0][2] == F(2)  # (00,10): L_{01} * delta_{00} = 2
        assert L1[1][1] == F(1)  # (01,01): L_{00} * delta_{11} = 1

        # L_2 = Id tensor L: (L_2)_{(ia),(jb)} = delta_{ij} * L_{ab}
        assert L2[0][0] == F(1)  # (00,00): delta_{00} * L_{00} = 1
        assert L2[0][1] == F(2)  # (00,01): delta_{00} * L_{01} = 2
        assert L2[0][2] == F(0)  # (00,10): delta_{01} * L_{00} = 0
        assert L2[2][2] == F(1)  # (10,10): delta_{11} * L_{00} = 1

    def test_L1_L2_commute(self):
        """L_1 and L_2 commute: [L tensor Id, Id tensor L] = 0."""
        L = [[F(3), F(7)], [F(11), F(13)]]
        L1 = _L1_from_L(L)
        L2 = _L2_from_L(L)
        prod12 = _mat4_mul(L1, L2)
        prod21 = _mat4_mul(L2, L1)
        for i in range(4):
            for j in range(4):
                assert prod12[i][j] == prod21[i][j]

    def test_P_swaps_tensor_factors(self):
        """P * L_1 * P = L_2 (permutation swaps tensor factors)."""
        L = [[F(3), F(7)], [F(11), F(13)]]
        L1 = _L1_from_L(L)
        L2 = _L2_from_L(L)
        P = yang_r_matrix(F(0))
        PL1P = _mat4_mul(_mat4_mul(P, L1), P)
        for i in range(4):
            for j in range(4):
                assert PL1P[i][j] == L2[i][j]
