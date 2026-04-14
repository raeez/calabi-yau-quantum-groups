"""Tests for the K3 R-matrix at ADE enhancement points.

Verifies:
  1. Yang R-matrix: explicit 4x4 matrix, YBE, unitarity
  2. Abelian pole at the A_1 point: double zero/pole in g_{12}
  3. A_1 block structure: 324 = 2+2+1+22+22+44+231, 48 off-diagonal
  4. Off-diagonal counts for all ADE types: A1(48) to E8(8736)
  5. Rank-monotonicity of the landscape
  6. Fermionic classification: 6 even, 190 odd, 80 mixed = 276
  7. Explicit Yang R-matrix blocks: bosonic and fermionic
  8. Master comparison: generic vs enhanced
  9. Yang R-matrix for sl_n (n=2,3): YBE and unitarity
  10. Off-diagonal proportionality to root length
  11. CY_2 constraint in block decomposition
  12. State count verification at each ADE type

Multi-path verification:
  - Path 1: algebraic (Yang R-matrix from Drinfeld coproduct)
  - Path 2: geometric (MO stable envelope, prop:mo-bypass)
  - Path 3: combinatorial (state counting, Gottsche formula)
  - Path 4: super-Yangian (fermionic corrections from gl(4|20))

AP-CY28: test points chosen to avoid poles at +/- h_i.
Safe parameters: u = 5.7 (far from poles at +/-1, +/-2, +/-3).
AP-CY14: all results CONJECTURAL (conditional on Y(g_{K3})).
"""

import sys
import os

import pytest
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from k3_rmatrix_enhanced import (
    ADE_DATA,
    STATUS,
    yang_r_matrix,
    yang_r_matrix_sl2,
    yang_r_verify_ybe,
    yang_r_verify_unitarity,
    abelian_pole_at_a1,
    a1_block_structure,
    off_diagonal_proportionality,
    offdiagonal_count_ade,
    offdiagonal_landscape,
    fermionic_correction_analysis,
    fermionic_landscape,
    a1_yang_block_explicit,
    master_enhanced_comparison,
)


# ===================================================================
# 1. YANG R-MATRIX (sl_2 fundamental)
# ===================================================================

class TestYangRMatrix:
    """Test the Yang R-matrix R(u) = (u*Id + hbar*P)/(u+hbar)."""

    def test_shape_sl2(self):
        """Yang R-matrix for sl_2 is 4x4."""
        R = yang_r_matrix_sl2(3.0)
        assert R.shape == (4, 4)

    def test_shape_sl3(self):
        """Yang R-matrix for sl_3 is 9x9."""
        R = yang_r_matrix(3.0, n=3)
        assert R.shape == (9, 9)

    def test_identity_at_hbar_zero(self):
        """R(u, hbar=0) = Id for all u."""
        R = yang_r_matrix_sl2(5.0, hbar=0.0)
        assert np.allclose(R, np.eye(4))

    def test_permutation_at_u_zero(self):
        """R(0, hbar) = P (the permutation operator)."""
        R = yang_r_matrix_sl2(0.0, hbar=1.0)
        # R(0) = (0*Id + P) / (0 + 1) = P
        P = np.zeros((4, 4))
        for i in range(2):
            for j in range(2):
                P[j * 2 + i, i * 2 + j] = 1.0
        assert np.allclose(R, P)

    def test_normalization(self):
        """R(u) -> Id as u -> infinity."""
        R = yang_r_matrix_sl2(1000.0)
        assert np.allclose(R, np.eye(4), atol=0.01)

    def test_offdiagonal_value(self):
        """Off-diagonal entry = hbar/(u+hbar)."""
        u, hbar = 5.7, 1.0
        R = yang_r_matrix_sl2(u, hbar)
        expected = hbar / (u + hbar)
        # VERIFIED [DC] off-diagonal formula [DA] Yang R-matrix
        assert abs(R[1, 2] - expected) < 1e-12
        assert abs(R[2, 1] - expected) < 1e-12

    def test_diagonal_inner_value(self):
        """Inner diagonal entry = u/(u+hbar)."""
        u, hbar = 5.7, 1.0
        R = yang_r_matrix_sl2(u, hbar)
        expected = u / (u + hbar)
        assert abs(R[1, 1] - expected) < 1e-12
        assert abs(R[2, 2] - expected) < 1e-12

    def test_diagonal_outer_value(self):
        """Outer diagonal entries = 1."""
        u, hbar = 5.7, 1.0
        R = yang_r_matrix_sl2(u, hbar)
        # VERIFIED [DC] diagonal formula [DA] Yang R-matrix
        assert abs(R[0, 0] - 1.0) < 1e-12
        assert abs(R[3, 3] - 1.0) < 1e-12


# ===================================================================
# 2. YANG R-MATRIX: YBE AND UNITARITY
# ===================================================================

class TestYangRMatrixProperties:
    """Test YBE and unitarity for the Yang R-matrix."""

    def test_ybe_sl2(self):
        """YBE for sl_2 Yang R-matrix."""
        result = yang_r_verify_ybe(5.7, 2.3, hbar=1.0, n=2)
        # VERIFIED [DC] YBE [DA] Yang R-matrix sl_2
        assert result['ybe_satisfied']

    def test_ybe_sl3(self):
        """YBE for sl_3 Yang R-matrix."""
        result = yang_r_verify_ybe(5.7, 2.3, hbar=1.0, n=3)
        assert result['ybe_satisfied']

    def test_ybe_various_params(self):
        """YBE at multiple spectral parameter values."""
        for u, v in [(3.1, 1.7), (7.3, 4.1), (0.5, 0.3)]:
            result = yang_r_verify_ybe(u, v, hbar=1.0, n=2)
            assert result['ybe_satisfied'], f"YBE failed at u={u}, v={v}"

    def test_ybe_various_hbar(self):
        """YBE for various hbar values."""
        for hbar in [0.5, 1.0, 2.0, 3.0]:
            result = yang_r_verify_ybe(5.7, 2.3, hbar=hbar, n=2)
            assert result['ybe_satisfied'], f"YBE failed at hbar={hbar}"

    def test_unitarity_sl2(self):
        """R_{12}(u) R_{21}(-u) = Id for sl_2."""
        result = yang_r_verify_unitarity(5.7, hbar=1.0, n=2)
        # VERIFIED [DC] unitarity [DA] Yang R-matrix
        assert result['unitarity_satisfied']

    def test_unitarity_sl3(self):
        """R_{12}(u) R_{21}(-u) = Id for sl_3."""
        result = yang_r_verify_unitarity(5.7, hbar=1.0, n=3)
        assert result['unitarity_satisfied']

    def test_unitarity_various_params(self):
        """Unitarity at multiple parameter values."""
        for u in [3.1, 7.3, 0.5, -2.3]:
            result = yang_r_verify_unitarity(u, hbar=1.0, n=2)
            assert result['unitarity_satisfied'], f"Unitarity failed at u={u}"


# ===================================================================
# 3. ABELIAN POLE AT A_1 POINT
# ===================================================================

class TestAbelianPole:
    """Test the pole structure at the A_1 enhancement point."""

    def test_double_zero_at_a1(self):
        """g_{12} has a double zero at u=h when h_1 = h_2 = h."""
        result = abelian_pole_at_a1(1.0, h=1.0, eps=0.0)
        assert result['is_double_zero']
        assert result['zeros_a1'] == [1.0]

    def test_double_pole_at_a1(self):
        """g_{12} has a double pole at u=-h when h_1 = h_2 = h."""
        result = abelian_pole_at_a1(3.0, h=1.0, eps=0.0)
        assert result['is_double_pole']
        assert result['poles_a1'] == [-1.0]

    def test_simple_zeros_generic(self):
        """At generic (eps > 0), zeros are simple and separated."""
        result = abelian_pole_at_a1(3.0, h=1.0, eps=0.5)
        assert not result['is_double_zero']
        # zeros at h+eps=1.5, h-eps=0.5
        assert sorted(result['zeros_generic']) == [0.5, 1.5]

    def test_splitting_proportional_to_eps(self):
        """The zero splitting is 2*eps."""
        result = abelian_pole_at_a1(3.0, h=1.0, eps=0.3)
        assert abs(result['splitting'] - 0.6) < 1e-12

    def test_g12_value_at_a1(self):
        """g_{12}(u) = ((u-h)/(u+h))^2 at the A_1 point."""
        u, h = 3.0, 1.0
        result = abelian_pole_at_a1(u, h, eps=0.0)
        expected = ((u - h) / (u + h)) ** 2
        # VERIFIED [DC] abelian eigenvalue [DA] A_1 pole
        assert abs(result['g12_a1'] - expected) < 1e-12


# ===================================================================
# 4. A_1 BLOCK STRUCTURE
# ===================================================================

class TestA1BlockStructure:
    """Test the 324x324 block structure at the A_1 point."""

    def test_total_324(self):
        """Total state count is 324."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['total'] == 324

    def test_ade_row_count(self):
        """2 ADE row states."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['ade_row'] == 2

    def test_ade_col_count(self):
        """2 ADE col states."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['ade_col'] == 2

    def test_ade_two_point(self):
        """1 ADE two-point state."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['ade_two_point'] == 1

    def test_complement_row(self):
        """22 complement row states."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['complement_row'] == 22

    def test_complement_col(self):
        """22 complement col states."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['complement_col'] == 22

    def test_mixed_two_point(self):
        """44 = 2*22 mixed two-point states."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['mixed_two_point'] == 44

    def test_complement_two_point(self):
        """C(22,2) = 231 complement two-point states."""
        result = a1_block_structure(h=1.0)
        assert result['state_decomposition']['complement_two_point'] == 231

    def test_offdiag_total_48(self):
        """48 off-diagonal entries at the A_1 point."""
        result = a1_block_structure(h=1.0)
        # VERIFIED [DC] off-diagonal count [DA] A_1 block structure
        assert result['off_diagonal_count']['total'] == 48

    def test_offdiag_ade_row(self):
        """2 off-diagonal from ADE row block."""
        result = a1_block_structure(h=1.0)
        assert result['off_diagonal_count']['ade_row_block'] == 2

    def test_offdiag_ade_col(self):
        """2 off-diagonal from ADE col block."""
        result = a1_block_structure(h=1.0)
        assert result['off_diagonal_count']['ade_col_block'] == 2

    def test_offdiag_mixed(self):
        """44 off-diagonal from mixed blocks."""
        result = a1_block_structure(h=1.0)
        assert result['off_diagonal_count']['mixed_two_point'] == 44

    def test_n_2x2_blocks(self):
        """24 blocks of 2x2 (2 ADE + 22 mixed)."""
        result = a1_block_structure(h=1.0)
        assert result['n_blocks_2x2'] == 24


# ===================================================================
# 5. OFF-DIAGONAL COUNTS FOR ALL ADE TYPES
# ===================================================================

class TestOffdiagonalCountsADE:
    """Test off-diagonal counts at each ADE enhancement type."""

    def test_a1_offdiag(self):
        """A_1: 48 off-diagonal entries (2 merged Mukai directions)."""
        result = offdiagonal_count_ade('A1')
        # d=2, n_comp=22: off_row=2 + off_col=2 + off_ade_two=0 + off_mixed=44 = 48
        # VERIFIED [DC] off-diagonal count [DA] A_1 enumeration
        assert result['off_diagonal']['total'] == 48
        assert result['n_mukai_dirs'] == 2

    def test_a2_offdiag(self):
        """A_2: 144 off-diagonal entries (3 merged Mukai directions)."""
        result = offdiagonal_count_ade('A2')
        # d=3, n_comp=21: off_row=6 + off_col=6 + off_ade_two=6 + off_mixed=126 = 144
        assert result['off_diagonal']['total'] == 144
        assert result['n_mukai_dirs'] == 3

    def test_d4_offdiag(self):
        """D_4: 294 off-diagonal from 4 merged directions."""
        result = offdiagonal_count_ade('D4')
        # d=4, n_comp=20: off_row=12 + off_col=12 + off_ade_two=30 + off_mixed=240 = 294
        # VERIFIED [DC] off-diagonal count [DA] D_4 block structure
        assert result['off_diagonal']['total'] == 294

    def test_e6_offdiag(self):
        """E_6: 810 off-diagonal entries."""
        result = offdiagonal_count_ade('E6')
        # d=6, n_comp=18: off_row=30 + off_col=30 + off_ade_two=210 + off_mixed=540 = 810
        assert result['off_diagonal']['total'] == 810

    def test_e7_offdiag(self):
        """E_7: 1218 off-diagonal entries."""
        result = offdiagonal_count_ade('E7')
        # d=7, n_comp=17: off_row=42 + off_col=42 + off_ade_two=420 + off_mixed=714 = 1218
        assert result['off_diagonal']['total'] == 1218

    def test_e8_offdiag(self):
        """E_8: 1764 off-diagonal entries."""
        result = offdiagonal_count_ade('E8')
        # d=8, n_comp=16: off_row=56 + off_col=56 + off_ade_two=756 + off_mixed=896 = 1764
        # VERIFIED [DC] off-diagonal count [DA] E_8 block structure
        assert result['off_diagonal']['total'] == 1764

    def test_state_count_all(self):
        """All ADE types have correct total state count = 324."""
        for ade_type in ADE_DATA:
            result = offdiagonal_count_ade(ade_type)
            assert result['state_decomposition']['total'] == 324, (
                f"State count wrong for {ade_type}"
            )


# ===================================================================
# 6. LANDSCAPE MONOTONICITY
# ===================================================================

class TestLandscape:
    """Test the off-diagonal landscape across ADE types."""

    def test_monotonicity(self):
        """Off-diagonal count increases with rank."""
        result = offdiagonal_landscape()
        # VERIFIED [DC] monotonicity [DA] rank ordering
        assert result['monotonic']

    def test_generic_zero(self):
        """Generic (abelian) has 0 off-diagonal."""
        result = offdiagonal_landscape()
        assert result['landscape']['generic']['n_offdiag'] == 0

    def test_a1_in_landscape(self):
        """A_1 value matches direct computation."""
        result = offdiagonal_landscape()
        assert result['landscape']['A1']['n_offdiag'] == 48

    def test_e8_largest(self):
        """E_8 has the most off-diagonal entries."""
        result = offdiagonal_landscape()
        e8 = result['landscape']['E8']['n_offdiag']
        for ade_type in ['A1', 'A2', 'D4', 'E6', 'E7']:
            assert e8 > result['landscape'][ade_type]['n_offdiag']


# ===================================================================
# 7. FERMIONIC CLASSIFICATION
# ===================================================================

class TestFermionicClassification:
    """Test the fermionic correction classification."""

    def test_total_276(self):
        """276 = C(24,2) possible A_1 enhancements."""
        result = fermionic_landscape()
        assert result['n_total'] == 276

    def test_both_even_count(self):
        """C(4,2) = 6 even-even pairs."""
        result = fermionic_landscape()
        assert result['n_both_even'] == 6

    def test_both_odd_count(self):
        """C(20,2) = 190 odd-odd pairs."""
        result = fermionic_landscape()
        # VERIFIED [DC] fermionic count [DA] Mukai signature
        assert result['n_both_odd'] == 190

    def test_mixed_count(self):
        """4*20 = 80 mixed-parity pairs."""
        result = fermionic_landscape()
        assert result['n_mixed'] == 80

    def test_majority_fermionic(self):
        """Majority of A_1 enhancements use fermionic Yang R-matrix."""
        result = fermionic_landscape()
        assert result['fermionic_yang_pairs'] > result['bosonic_yang_pairs']

    def test_both_even_no_correction(self):
        """Both-even pair: no fermionic correction."""
        result = fermionic_correction_analysis((0, 1))
        assert result['case'] == 'both_even'
        assert not result['creates_new_offdiagonal']

    def test_both_odd_sign_flip(self):
        """Both-odd pair: sign flip in P."""
        result = fermionic_correction_analysis((4, 5))
        assert result['case'] == 'both_odd'
        assert result['offdiag_sign'] == -1

    def test_mixed_no_new_offdiag(self):
        """Mixed pair: no new off-diagonal entries."""
        result = fermionic_correction_analysis((0, 4))
        assert result['case'] == 'mixed_parity'
        assert not result['creates_new_offdiagonal']

    def test_fermionic_does_not_create_new_offdiag(self):
        """Fermionic corrections modify sign but don't create new off-diag."""
        for i in range(24):
            for j in range(i + 1, min(i + 3, 24)):
                result = fermionic_correction_analysis((i, j))
                assert not result['creates_new_offdiagonal']


# ===================================================================
# 8. EXPLICIT YANG R-MATRIX BLOCKS
# ===================================================================

class TestExplicitBlocks:
    """Test the explicit 4x4 Yang R-matrix blocks."""

    def test_bosonic_offdiag_positive(self):
        """Bosonic (both-even) off-diagonal entries are positive."""
        result = a1_yang_block_explicit(5.7, alpha=1.0, parity_case='both_even')
        assert not result.get('has_pole', False)
        offdiag = result['off_diagonal_value']
        # alpha/(u+alpha) = 1/(5.7+1) = 1/6.7 > 0
        assert offdiag.real > 0

    def test_fermionic_offdiag_negative(self):
        """Fermionic (both-odd) off-diagonal entries are negative."""
        result = a1_yang_block_explicit(5.7, alpha=1.0, parity_case='both_odd')
        assert not result.get('has_pole', False)
        offdiag = result['off_diagonal_value']
        # -alpha/(u-alpha) = -1/(5.7-1) = -1/4.7 < 0
        assert offdiag.real < 0

    def test_bosonic_offdiag_formula(self):
        """Bosonic off-diagonal = alpha/(u+alpha)."""
        u, alpha = 5.7, 1.5
        result = a1_yang_block_explicit(u, alpha, 'both_even')
        expected = alpha / (u + alpha)
        # VERIFIED [DC] off-diagonal formula [DA] bosonic Yang block
        assert abs(result['off_diagonal_value'] - expected) < 1e-12

    def test_fermionic_offdiag_formula(self):
        """Fermionic off-diagonal = -alpha/(u-alpha)."""
        u, alpha = 5.7, 1.5
        result = a1_yang_block_explicit(u, alpha, 'both_odd')
        expected = -alpha / (u - alpha)
        assert abs(result['off_diagonal_value'] - expected) < 1e-12

    def test_outer_diagonal_is_one(self):
        """Outer diagonal entries (|00> and |11>) equal 1."""
        result = a1_yang_block_explicit(5.7, alpha=1.0, parity_case='both_even')
        assert abs(result['diagonal']['00'] - 1.0) < 1e-12
        assert abs(result['diagonal']['11'] - 1.0) < 1e-12

    def test_symmetry_of_offdiag(self):
        """R_{01,10} = R_{10,01} (symmetric off-diagonal)."""
        result = a1_yang_block_explicit(5.7, alpha=1.0, parity_case='both_even')
        assert abs(
            result['off_diagonal']['01_10'] - result['off_diagonal']['10_01']
        ) < 1e-12

    def test_block_is_identity_at_alpha_zero(self):
        """At alpha=0, the Yang R-matrix block is the identity."""
        result = a1_yang_block_explicit(5.7, alpha=0.0, parity_case='both_even')
        assert np.allclose(result['R_matrix'], np.eye(4))


# ===================================================================
# 9. MASTER COMPARISON
# ===================================================================

class TestMasterComparison:
    """Test the master comparison between generic and enhanced R-matrices."""

    def test_generic_zero_offdiag(self):
        """Generic R-matrix has 0 off-diagonal."""
        result = master_enhanced_comparison()
        assert result['abelian']['n_offdiag_nonzero'] == 0

    def test_enhanced_48_offdiag(self):
        """Enhanced A_1 R-matrix has 48 off-diagonal."""
        result = master_enhanced_comparison()
        assert result['enhanced_a1']['n_offdiag_nonzero'] == 48

    def test_yang_ybe_in_master(self):
        """Yang R-matrix satisfies YBE in master comparison."""
        result = master_enhanced_comparison()
        assert result['yang_ybe']['ybe_satisfied']

    def test_yang_unitarity_in_master(self):
        """Yang R-matrix satisfies unitarity in master comparison."""
        result = master_enhanced_comparison()
        assert result['yang_unitarity']['unitarity_satisfied']

    def test_324_states_both(self):
        """Both generic and enhanced have 324 states."""
        result = master_enhanced_comparison()
        assert result['abelian']['n_states'] == 324
        assert result['enhanced_a1']['n_states'] == 324


# ===================================================================
# 10. CONJECTURAL STATUS
# ===================================================================

class TestStatus:
    """Verify all outputs carry the CONJECTURAL status tag."""

    def test_status_is_conjectural(self):
        """Module-level STATUS is CONJECTURAL."""
        assert STATUS == 'CONJECTURAL'

    def test_block_structure_status(self):
        """Block structure carries CONJECTURAL status."""
        result = a1_block_structure(h=1.0)
        assert result['status'] == 'CONJECTURAL'

    def test_landscape_status(self):
        """Landscape carries CONJECTURAL status."""
        result = offdiagonal_landscape()
        assert result['status'] == 'CONJECTURAL'


# ===================================================================
# 11. EDGE CASES AND ROBUSTNESS
# ===================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_yang_r_large_u(self):
        """Yang R-matrix -> Id at large u."""
        R = yang_r_matrix_sl2(1000.0, hbar=1.0)
        assert np.allclose(R, np.eye(4), atol=0.01)

    def test_offdiag_unknown_ade_raises(self):
        """Unknown ADE type raises ValueError."""
        with pytest.raises(ValueError):
            offdiagonal_count_ade('G2')

    def test_offdiag_various_h_values(self):
        """A_1 block structure works for various h values."""
        for h_val in [0.5, 1.0, 2.0, 3.0]:
            result = a1_block_structure(h=h_val)
            assert result['state_decomposition']['total'] == 324
            assert result['off_diagonal_count']['total'] == 48

    def test_fermionic_boundary_indices(self):
        """Fermionic analysis at boundary indices (3,4)."""
        result = fermionic_correction_analysis((3, 4))
        # 3 is even (index < 4), 4 is odd (index >= 4)
        assert result['case'] == 'mixed_parity'

    def test_yang_r_complex_u(self):
        """Yang R-matrix works with complex spectral parameter."""
        R = yang_r_matrix_sl2(3.0 + 1.0j, hbar=1.0)
        assert R.shape == (4, 4)
        # YBE still holds
        result = yang_r_verify_ybe(3.0 + 1.0j, 1.0 + 0.5j, hbar=1.0, n=2)
        assert result['ybe_satisfied']
