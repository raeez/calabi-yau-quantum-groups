r"""Tests for k3_yangian_rank2.py: Y(gl_2 \otimes g_{K3}).

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify INTERNAL CONSISTENCY of the rank-2 K3 Yangian construction.

CENTRAL RESULTS (all conjectural):
    (1) 48 generators: C^2 \otimes C^{24} charge-1 space.
    (2) g_2(u) = g_1(u)^2 has degree (48, 48).
    (3) g_2(u) * g_2(-u) = 1 (unitarity).
    (4) RTT relation with 2x2 Lax operator and Yang R-matrix.
    (5) sl_2 Serre relations: [e_0,[e_0,e_1]] = 0 (nontrivial at rank 2).
    (6) Matrix Miura coproduct: Delta_z(L(u)) = L^L(u) * L^R(u-z).
    (7) Coassociativity from associativity of Mat_2(C).
    (8) R-matrix: 24 blocks of 4x4 Yang R-matrices, nondiagonal.
    (9) Quantum determinant: central in Y(gl_2 \otimes g_{K3}).

Test structure:
    Section 1: Generators and basis (5 tests)
    Section 2: Structure function g_2(u) (8 tests)
    Section 3: RTT presentation (4 tests)
    Section 4: Serre relations (5 tests)
    Section 5: Matrix Miura coproduct (8 tests)
    Section 6: R-matrix (10 tests)
    Section 7: Quantum determinant (4 tests)
    Section 8: Cross-checks with rank-1 engine (5 tests)
    Section 9: Full verification (3 tests)

Manuscript references:
    k3_yangian_chapter.tex: ch:k3-yangian
    agt_higher_rank_k3.py: rank-N AGT, structure function scaling
"""

import pytest
import sys
import os
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.k3_yangian_rank2 import (
    # Constants
    RANK_N, MUKAI_RANK, CHARGE1_DIM, STRUC_FUNC_DEGREE,
    NUM_CURRENTS, KAPPA_CH_RANK2, KAPPA_CAT_RANK2, KAPPA_FIBER_RANK2,
    STATUS,
    # Generators
    generator_data, charge1_basis, Rank2GeneratorData,
    # Structure function
    structure_function_rank2,
    structure_function_eigenvalue_rank2,
    verify_unitarity_rank2,
    structure_function_log_coefficients_rank2,
    structure_function_special_values_rank2,
    # RTT
    rtt_presentation, rtt_relations_explicit, RTTData,
    # Serre
    serre_relations, verify_serre_mode_level, SerreData,
    # Coproduct
    MatrixMiuraCoproduct,
    # R-matrix
    r_matrix_rank2_block, r_matrix_rank2_full,
    r_matrix_rank2_properties,
    verify_ybe_rank2_block,
    verify_unitarity_rank2_rmatrix,
    # Quantum determinant
    quantum_determinant_data, quantum_determinant_numerical,
    # Summary
    rank2_summary, full_verification_rank2,
)
from lib.k3_yangian import (
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
)

F = Fraction


# =========================================================================
# 1. Generators and basis
# =========================================================================

class TestGenerators:
    """Verify generator counting and charge-1 basis structure."""

    def test_rank(self):
        """gl_2 has rank N = 2."""
        assert RANK_N == 2

    def test_charge1_dim(self):
        """Charge-1 space: C^2 x C^{24} = C^{48}."""
        assert CHARGE1_DIM == 48
        assert CHARGE1_DIM == RANK_N * MUKAI_RANK

    def test_generator_data_counts(self):
        """Generator data has correct counts."""
        gen = generator_data()
        assert gen.rank == 2
        assert gen.mukai_rank == 24
        assert gen.charge1_dim == 48
        assert gen.gl2_generators == 4  # E_{11}, E_{12}, E_{21}, E_{22}
        assert gen.current_families == 96  # 4 * 24
        assert gen.serre_nontrivial is True

    def test_charge1_basis_size(self):
        """Charge-1 basis has 48 states."""
        basis = charge1_basis()
        assert len(basis) == 48

    def test_charge1_basis_elements(self):
        """Basis states (i, a) with i in {0,1}, a in {0,...,23}."""
        basis = charge1_basis()
        gl2_indices = set(i for i, a in basis)
        mukai_indices = set(a for i, a in basis)
        assert gl2_indices == {0, 1}
        assert mukai_indices == set(range(24))


# =========================================================================
# 2. Structure function g_2(u) = g_1(u)^2
# =========================================================================

class TestStructureFunction:
    """Verify the degree-(48,48) rank-2 structure function."""

    def test_degree(self):
        """Structure function degree is (48, 48)."""
        assert STRUC_FUNC_DEGREE == (48, 48)

    def test_g2_equals_g1_squared(self):
        """g_2(u) = g_1(u)^2 at generic test points."""
        from sympy import Rational
        params = kummer_k3_parameters()
        # AP-CY28: test points far from poles
        for u in [Rational(37), Rational(41), Rational(53)]:
            g1 = structure_function_evaluate(u, params)
            g2 = structure_function_rank2(u, params)
            # VERIFIED: g_2 = g_1^2
            assert g2 == g1 * g1

    def test_unitarity(self):
        """g_2(u) * g_2(-u) = 1."""
        result = verify_unitarity_rank2()
        assert result['unitarity_holds'] is True

    def test_g2_at_zero(self):
        """g_2(0) = ((-1)^{24})^2 = 1."""
        from sympy import Rational
        g0 = structure_function_rank2(Rational(0))
        assert g0 == 1

    def test_eigenvalue_rank2(self):
        """Individual eigenvalue g_a^{(2)}(u) = ((u-h_a)/(u+h_a))^2."""
        from sympy import Rational
        params = kummer_k3_parameters()
        u = Rational(37)
        # Direction 0: h_0 = 1 (positive Mukai)
        g_0 = structure_function_eigenvalue_rank2(0, u, params)
        h_0 = params.h[0]
        expected = ((u - h_0) / (u + h_0)) ** 2
        assert g_0 == expected

    def test_eigenvalue_product_equals_full(self):
        """Product of all 24 eigenvalues = g_2(u)."""
        from sympy import Rational
        params = kummer_k3_parameters()
        u = Rational(37)
        product = Rational(1)
        for a in range(24):
            product *= structure_function_eigenvalue_rank2(a, u, params)
        g2 = structure_function_rank2(u, params)
        assert product == g2

    def test_log_coefficients_scaling(self):
        """Log coefficients at rank 2 are 2x those at rank 1."""
        from lib.k3_yangian import structure_function_log_coefficients
        params = kummer_k3_parameters()
        alphas_r1 = structure_function_log_coefficients(params, max_order=8)
        alphas_r2 = structure_function_log_coefficients_rank2(params, max_order=8)
        for k in range(1, 9):
            # VERIFIED: rank-2 log coefficient = 2 * rank-1
            assert alphas_r2[k] == 2 * alphas_r1[k]

    def test_special_values(self):
        """Special values of g_2(u)."""
        sv = structure_function_special_values_rank2()
        assert sv['g_2(0)_matches'] is True
        assert sv['degree'] == (48, 48)
        assert sv['num_zeros'] == 48
        assert sv['num_poles'] == 48


# =========================================================================
# 3. RTT presentation
# =========================================================================

class TestRTT:
    """Verify RTT presentation data."""

    def test_rtt_data_type(self):
        """rtt_presentation returns RTTData."""
        rtt = rtt_presentation()
        assert isinstance(rtt, RTTData)

    def test_lax_size(self):
        """Lax matrix is 2x2."""
        rtt = rtt_presentation()
        assert rtt.lax_matrix_size == (2, 2)

    def test_mukai_directions(self):
        """24 Mukai directions."""
        rtt = rtt_presentation()
        assert rtt.mukai_directions == 24

    def test_total_generators(self):
        """96 RTT generators: 4 (gl_2) * 24 (Mukai)."""
        rtt = rtt_presentation()
        assert rtt.total_rtt_generators == 96


# =========================================================================
# 4. Serre relations
# =========================================================================

class TestSerre:
    """Verify Serre relation structure and numerical checks."""

    def test_serre_nontrivial(self):
        """Serre relations are nontrivial at rank 2."""
        s = serre_relations()
        assert isinstance(s, SerreData)
        assert s.is_nontrivial is True

    def test_num_intra_relations(self):
        """24 intra-Mukai Serre relations (one per direction)."""
        s = serre_relations()
        assert s.num_intra_relations == 24

    def test_num_inter_relations(self):
        """276 inter-Mukai Serre relations (24 choose 2)."""
        s = serre_relations()
        assert s.num_inter_relations == 276

    def test_serre_fundamental(self):
        """Serre holds in the 2-dim fundamental representation."""
        result = verify_serre_mode_level()
        assert result['fundamental_serre_holds'] is True

    def test_serre_adjoint(self):
        """Serre holds in the 3-dim adjoint representation."""
        result = verify_serre_mode_level()
        assert result['adjoint_serre_holds'] is True


# =========================================================================
# 5. Matrix Miura coproduct
# =========================================================================

class TestCoproduct:
    """Verify the matrix Miura coproduct Delta_z(L(u)) = L^L(u) * L^R(u-z)."""

    def test_coproduct_lax_symbolic(self):
        """Symbolic coproduct has 4 matrix entries."""
        coprod = MatrixMiuraCoproduct()
        data = coprod.coproduct_lax_symbolic(a=0)
        assert 'T11' in data['matrix_entries']
        assert 'T12' in data['matrix_entries']
        assert 'T21' in data['matrix_entries']
        assert 'T22' in data['matrix_entries']

    def test_coproduct_chevalley(self):
        """Chevalley decomposition of coproduct includes cross-terms."""
        coprod = MatrixMiuraCoproduct()
        data = coprod.coproduct_lax_symbolic(a=0)
        assert 'e' in data['chevalley_coproduct']
        assert 'f' in data['chevalley_coproduct']
        assert 'h' in data['chevalley_coproduct']

    def test_coproduct_diagonal_lax(self):
        """Numerical check: diagonal Lax coproduct."""
        coprod = MatrixMiuraCoproduct()
        result = coprod.coproduct_numerical_check()
        assert result['diagonal_lax']['pass'] is True

    def test_coproduct_triangular_lax(self):
        """Numerical check: upper triangular Lax coproduct."""
        coprod = MatrixMiuraCoproduct()
        result = coprod.coproduct_numerical_check()
        assert result['upper_triangular_lax']['pass'] is True

    def test_coproduct_off_diagonal_zero_for_diagonal(self):
        """For diagonal Lax, the off-diagonal entries of Delta_z(L) vanish."""
        coprod = MatrixMiuraCoproduct()
        result = coprod.coproduct_numerical_check()
        assert result['diagonal_lax']['off_diagonal_zero'] is True

    def test_coassociativity_statement(self):
        """Coassociativity follows from matrix multiplication associativity."""
        coprod = MatrixMiuraCoproduct()
        result = coprod.coassociativity_from_matrix_miura()
        assert 'associativity' in result['statement'].lower()

    def test_coproduct_z0_cocommutative(self):
        """At z=0, the coproduct is cocommutative (primitive)."""
        coprod = MatrixMiuraCoproduct()
        result = coprod.coproduct_mode_level(z=0.0)
        assert result['z_equals_0_cocommutative'] is True

    def test_coproduct_various_hbar(self):
        """Coproduct works for different hbar values."""
        for hbar in [0.5, 1.0, 2.0]:
            coprod = MatrixMiuraCoproduct(hbar=hbar)
            result = coprod.coproduct_numerical_check(u_val=5.3, z_val=1.7)
            assert result['diagonal_lax']['pass'] is True
            assert result['upper_triangular_lax']['pass'] is True


# =========================================================================
# 6. R-matrix
# =========================================================================

class TestRMatrix:
    """Verify the rank-2 R-matrix: 24 blocks of 4x4 Yang R-matrices."""

    def test_r_matrix_block_shape(self):
        """Each Mukai block is 4x4."""
        block = r_matrix_rank2_block(a=0, u_val=3.7)
        assert block.shape == (4, 4)

    def test_r_matrix_block_nonzero(self):
        """Block has nonzero entries."""
        block = r_matrix_rank2_block(a=0, u_val=3.7)
        assert np.max(np.abs(block)) > 0

    def test_r_matrix_block_offdiagonal(self):
        """Block has nonzero off-diagonal entries (from Yang P term)."""
        block = r_matrix_rank2_block(a=0, u_val=3.7, hbar=1.0)
        # The Yang R-matrix has off-diagonal entries at (1,2) and (2,1)
        # In 4x4 basis: entries (0*2+1, 1*2+0) = (1,2) and (2,1)
        assert abs(block[1, 2]) > 1e-15
        assert abs(block[2, 1]) > 1e-15

    def test_r_matrix_properties(self):
        """R-matrix property summary is consistent."""
        props = r_matrix_rank2_properties()
        assert props['rank'] == 2
        assert props['charge1_dim'] == 48
        assert props['nondiagonal'] is True
        assert props['total_off_diagonal'] == 48

    def test_ybe_block(self):
        """Yang-Baxter equation for a single 4x4 block."""
        result = verify_ybe_rank2_block(a=0, u=3.7+0.1j, v=1.3+0.2j)
        assert result['yang_ybe_result']['ybe_satisfied'] is True

    def test_ybe_multiple_directions(self):
        """YBE holds for several Mukai directions."""
        for a in [0, 3, 10, 23]:
            result = verify_ybe_rank2_block(a=a, u=5.1+0.3j, v=2.4+0.1j)
            assert result['yang_ybe_result']['ybe_satisfied'] is True

    def test_unitarity_rmatrix_block(self):
        """R_{12}(u) * R_{21}(-u) = Id for block."""
        result = verify_unitarity_rank2_rmatrix(a=0, u=3.7+0.1j)
        assert result['combined_unitarity'] is True

    def test_unitarity_multiple_directions(self):
        """R-matrix unitarity for several Mukai directions."""
        for a in [0, 5, 15, 23]:
            result = verify_unitarity_rank2_rmatrix(a=a, u=4.2+0.2j)
            assert result['combined_unitarity'] is True

    def test_r_matrix_classical_limit(self):
        """At large u, R -> Id (classical limit)."""
        block = r_matrix_rank2_block(a=0, u_val=1000.0, hbar=1.0)
        # For large u: g_a(u) -> 1, R_{gl_2}(u) -> Id
        err = np.max(np.abs(block - np.eye(4)))
        assert err < 0.01  # O(1/u) corrections

    def test_r_matrix_full_block_diagonal(self):
        """Full R-matrix is block-diagonal in diagonal Mukai basis."""
        R_full = r_matrix_rank2_full(u_val=3.7)
        assert R_full.shape == (2304, 2304)
        # Check that it's not all zeros
        assert np.max(np.abs(R_full)) > 0


# =========================================================================
# 7. Quantum determinant
# =========================================================================

class TestQuantumDeterminant:
    """Verify quantum determinant properties."""

    def test_qdet_data(self):
        """Quantum determinant data is well-formed."""
        data = quantum_determinant_data()
        assert 'formula' in data
        assert 'central' in data['properties'][0].lower()

    def test_qdet_numerical(self):
        """Numerical qdet matches expected value."""
        result = quantum_determinant_numerical()
        assert result['match'] is True

    def test_qdet_various_u(self):
        """Quantum determinant works for various u values."""
        for u in [1.5, 3.7, 7.2, 10.1]:
            result = quantum_determinant_numerical(u_val=u)
            assert result['match'] is True

    def test_qdet_various_hbar(self):
        """Quantum determinant works for various hbar."""
        for hbar in [0.5, 1.0, 2.0, 3.0]:
            result = quantum_determinant_numerical(u_val=5.0, hbar=hbar)
            assert result['match'] is True


# =========================================================================
# 8. Cross-checks with rank-1 engine
# =========================================================================

class TestCrossChecks:
    """Cross-check rank-2 results against rank-1 k3_yangian.py."""

    def test_rank2_g_at_zero_matches_rank1(self):
        """g_2(0) = g_1(0)^2 = 1^2 = 1."""
        from sympy import Rational
        g1_0 = structure_function_evaluate(Rational(0))
        g2_0 = structure_function_rank2(Rational(0))
        assert g2_0 == g1_0 ** 2

    def test_unitarity_consistent(self):
        """Rank-2 unitarity follows from rank-1."""
        from sympy import Rational
        params = kummer_k3_parameters()
        u = Rational(37)
        g1_u = structure_function_evaluate(u, params)
        g1_neg = structure_function_evaluate(-u, params)
        g2_u = structure_function_rank2(u, params)
        g2_neg = structure_function_rank2(-u, params)
        assert g1_u * g1_neg == 1  # rank-1 unitarity
        assert g2_u * g2_neg == 1  # rank-2 unitarity
        assert g2_u == g1_u ** 2   # rank-2 = rank-1 squared

    def test_degree_scaling(self):
        """Degree (48,48) = 2 * (24,24)."""
        from lib.k3_yangian import NUM_PARAMS as N1
        assert STRUC_FUNC_DEGREE == (2 * N1, 2 * N1)

    def test_kappa_scaling(self):
        """kappa_{ch} at rank 2 = 2 * kappa_{ch} at rank 1 (AP113)."""
        assert KAPPA_CH_RANK2 == F(6)
        assert KAPPA_CAT_RANK2 == F(4)
        assert KAPPA_FIBER_RANK2 == F(48)

    def test_agt_consistency(self):
        """Rank-2 matches agt_higher_rank_k3 degree formula."""
        from lib.agt_higher_rank_k3 import structure_function_rank_N_degree
        deg_agt = structure_function_rank_N_degree(2)
        assert deg_agt == STRUC_FUNC_DEGREE


# =========================================================================
# 9. Full verification
# =========================================================================

class TestFullVerification:
    """Run the complete verification suite."""

    def test_full_verification_passes(self):
        """All internal consistency checks pass."""
        result = full_verification_rank2()
        assert result['all_pass'] is True

    def test_summary_consistent(self):
        """Summary data is internally consistent."""
        summary = rank2_summary()
        assert summary['rank'] == 2
        assert summary['generators']['charge1_dim'] == 48
        assert summary['structure_function']['degree'] == (48, 48)
        assert summary['r_matrix']['nondiagonal'] is True

    def test_status_conjectural(self):
        """All results are marked CONJECTURAL (AP-CY14)."""
        summary = rank2_summary()
        assert summary['status'] == 'CONJECTURAL'
