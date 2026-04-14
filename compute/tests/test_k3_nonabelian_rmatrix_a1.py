"""Tests for the K3 nonabelian R-matrix at A_1: deformation, mixing, and YBE.

Verifies:
  1. Deformed R-matrix at delta=0: 48 off-diagonal entries
  2. Deformed R-matrix at delta>0: 48 off-diagonal entries (persistent block structure)
  3. 24-parameter eigenvalues: correct CY condition, splitting
  4. Double pole resolution: abelian order 2 -> Yang antisym order 1
  5. Complement mixing: NO cross-sector coupling (22 directions unaffected)
  6. YBE: PASS for all blocks (direct sum argument)
  7. Nonzero count: 372 = 324 + 48 at delta=0
  8. Eigenvalue splitting: degenerate at delta=0, split at delta>0
  9. Block invariants: det and trace match Yang formula
  10. Crossing symmetry: PASS
  11. Mixing angle: 45 deg at delta=0, decreasing with delta
  12. Fermionic sign: odd-odd vs even-even
  13. Deformation profile: monotone eigenvalue splitting
  14. Sparsity: >99.6% zero entries at delta=0

Multi-path verification:
  Path 1: algebraic (Yang R-matrix formula, direct computation)
  Path 2: block structure (sector decomposition, mixing analysis)
  Path 3: matrix-level (numpy operations on 324x324)
  Path 4: physical (pole resolution, crossing symmetry, YBE)
  Path 5: deformation (delta profile, eigenvalue splitting)

AP-CY28: test points avoid poles at +/- h_i.
  Safe: u=5.7, h_base=1.0, alpha=1.0. Poles at +/-1.
  h_params[0..1] near 1.0, complement near -0.09. Far from u=5.7.
AP-CY14: all results CONJECTURAL.
AP-CY31: spectral parameter u (Yangian), NOT worldsheet z.
AP-CY30: pairwise YBE does NOT imply tetrahedron; not tested here.
"""

import sys
import os

import pytest
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from k3_nonabelian_rmatrix_a1 import (
    STATUS,
    build_deformed_a1_rmatrix,
    double_pole_resolution,
    deformation_profile,
    complement_mixing_analysis,
    ybe_full_block_structure,
    nonzero_count_at_delta_zero,
    eigenvalue_splitting_profile,
    block_invariants,
    crossing_symmetry_check,
    master_nonabelian_a1_rmatrix,
    _make_h_params_a1,
    _abelian_eigenvalue_24param,
)
from mo_rmatrix_k3_charge2 import enumerate_charge2_states

# Safe test parameters (AP-CY28)
U_SAFE = 5.7
H_BASE = 1.0
ALPHA = 1.0


# ===================================================================
# 1. DEFORMED R-MATRIX AT DELTA=0
# ===================================================================

class TestDeformedDeltaZero:
    """Test the deformed R-matrix at the exact A_1 point (delta=0)."""

    def test_shape_324(self):
        """R-matrix is 324x324."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0, alpha=ALPHA)
        assert data['R'].shape == (324, 324)

    def test_offdiag_48_even_even(self):
        """48 off-diagonal entries at even-even A_1."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                          alpha=ALPHA, merged=(0, 1))
        assert data['n_offdiag_nonzero'] == 48

    def test_offdiag_48_odd_odd(self):
        """48 off-diagonal entries at odd-odd A_1."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                          alpha=ALPHA, merged=(4, 5))
        assert data['n_offdiag_nonzero'] == 48

    def test_24_blocks(self):
        """24 blocks (2 ADE + 22 mixed)."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0, alpha=ALPHA)
        assert data['n_blocks'] == 24

    def test_status_conjectural(self):
        """Status is CONJECTURAL (AP-CY14)."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0, alpha=ALPHA)
        assert data['status'] == 'CONJECTURAL'

    def test_eigenvalue_degeneracy(self):
        """At delta=0, eigenvalues in each block are degenerate."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0, alpha=ALPHA)
        assert data['max_ev_splitting'] < 1e-10

    def test_no_pole(self):
        """No pole at safe parameter values."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0, alpha=ALPHA)
        assert not data['has_pole']


# ===================================================================
# 2. DEFORMED R-MATRIX AT DELTA > 0
# ===================================================================

class TestDeformedDeltaPositive:
    """Test the R-matrix with nonzero splitting (delta > 0)."""

    def test_offdiag_48_at_small_delta(self):
        """48 off-diagonal entries persist at small delta."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.01, alpha=ALPHA)
        assert data['n_offdiag_nonzero'] == 48

    def test_offdiag_48_at_large_delta(self):
        """48 off-diagonal entries persist at large delta."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=2.0, alpha=ALPHA)
        assert data['n_offdiag_nonzero'] == 48

    def test_eigenvalue_splitting_at_delta(self):
        """Eigenvalue splitting increases with delta (24-param model)."""
        d1 = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.1, alpha=ALPHA)
        d2 = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.5, alpha=ALPHA)
        assert d2['max_ev_splitting'] > d1['max_ev_splitting']

    def test_block_structure_persistent(self):
        """Block count remains 24 for all delta."""
        for delta in [0.0, 0.1, 0.5, 1.0, 5.0]:
            data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=delta, alpha=ALPHA)
            assert data['n_blocks'] == 24


# ===================================================================
# 3. 24-PARAMETER MUKAI WEIGHTS
# ===================================================================

class TestMukaiWeights:
    """Test the 24-parameter Mukai weight construction."""

    def test_cy_condition(self):
        """Sum of 24 weights = 0 (CY condition)."""
        h = _make_h_params_a1(H_BASE, delta=0.0)
        assert abs(np.sum(h)) < 1e-10

    def test_cy_condition_with_delta(self):
        """CY condition holds for nonzero delta."""
        h = _make_h_params_a1(H_BASE, delta=0.5)
        assert abs(np.sum(h)) < 1e-10

    def test_merged_directions_split(self):
        """h[0] = h_base + delta, h[1] = h_base - delta."""
        delta = 0.3
        h = _make_h_params_a1(H_BASE, delta=delta)
        assert abs(h[0] - (H_BASE + delta)) < 1e-12
        assert abs(h[1] - (H_BASE - delta)) < 1e-12

    def test_merged_directions_degenerate_at_zero(self):
        """h[0] = h[1] = h_base at delta=0."""
        h = _make_h_params_a1(H_BASE, delta=0.0)
        assert abs(h[0] - h[1]) < 1e-12

    def test_complement_distinct(self):
        """22 complement weights are all distinct."""
        h = _make_h_params_a1(H_BASE, delta=0.0)
        comp = h[2:]
        for i in range(len(comp)):
            for j in range(i + 1, len(comp)):
                assert abs(comp[i] - comp[j]) > 1e-6, (
                    f"Complement weights {i} and {j} are degenerate"
                )


# ===================================================================
# 4. DOUBLE POLE RESOLUTION
# ===================================================================

class TestDoublePoleResolution:
    """Test the resolution of the abelian double pole."""

    def test_abelian_pole_order_2(self):
        """Abelian R-matrix has a double pole."""
        result = double_pole_resolution(H_BASE, ALPHA)
        # VERIFIED [DC] pole order [DA] abelian eigenvalue formula
        assert result['abelian_pole_order'] == 2

    def test_yang_antisym_pole_order_1(self):
        """Yang antisymmetric sector has a simple pole."""
        result = double_pole_resolution(H_BASE, ALPHA)
        assert result['yang_antisym_pole_order'] == 1

    def test_yang_sym_no_pole(self):
        """Yang symmetric sector has no pole."""
        result = double_pole_resolution(H_BASE, ALPHA)
        assert result['yang_sym_pole_order'] == 0

    def test_residue_formula(self):
        """Residue of antisymmetric sector = -2*alpha."""
        result = double_pole_resolution(H_BASE, ALPHA)
        assert abs(result['yang_residue_antisym'] - (-2 * ALPHA)) < 1e-12

    def test_residue_proportional_to_alpha(self):
        """Residue scales linearly with alpha."""
        r1 = double_pole_resolution(H_BASE, alpha=1.0)
        r2 = double_pole_resolution(H_BASE, alpha=2.0)
        assert abs(r2['yang_residue_antisym'] / r1['yang_residue_antisym'] - 2.0) < 1e-10


# ===================================================================
# 5. COMPLEMENT MIXING
# ===================================================================

class TestComplementMixing:
    """Test that the sl_2 R-matrix does NOT affect the 22 complement directions."""

    def test_no_mixing_even_even(self):
        """No cross-sector mixing at even-even A_1."""
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA, merged=(0, 1))
        # VERIFIED [DC] no mixing [DA] orthogonal Mukai decomposition
        assert result['no_mixing']

    def test_no_mixing_odd_odd(self):
        """No cross-sector mixing at odd-odd A_1."""
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA, merged=(4, 5))
        assert result['no_mixing']

    def test_no_ade_to_comp(self):
        """Zero ADE-to-complement off-diagonal entries."""
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA)
        assert result['n_ade_to_comp'] == 0

    def test_no_mixed_cross_comp(self):
        """Zero cross-complement-direction entries in mixed sector."""
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA)
        assert result['n_mixed_cross_comp'] == 0

    def test_no_comp_to_comp(self):
        """Zero complement-to-complement off-diagonal entries."""
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA)
        assert result['n_comp_to_comp'] == 0

    def test_within_block_count_24(self):
        """24 off-diagonal pairs, all within blocks."""
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA)
        assert result['n_within_block'] == 24  # 24 blocks, each with 1 pair (i,j)
        assert result['total_offdiag_pairs'] == 24


# ===================================================================
# 6. YBE VERIFICATION
# ===================================================================

class TestYBE:
    """Test the Yang-Baxter equation for the full block-structured R-matrix."""

    def test_ybe_even_even(self):
        """YBE passes for even-even A_1."""
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA, merged=(0, 1))
        # VERIFIED [DC] YBE [DA] Yang theorem + direct sum
        assert result['direct_sum_ybe_valid']

    def test_ybe_odd_odd(self):
        """YBE passes for odd-odd A_1."""
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA, merged=(4, 5))
        assert result['direct_sum_ybe_valid']

    def test_ybe_multi_params(self):
        """YBE passes at multiple spectral parameter pairs."""
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)
        assert result['multi_ybe_all_pass']

    def test_ybe_max_error_small(self):
        """YBE error is negligible."""
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)
        assert result['multi_ybe_max_error'] < 1e-10

    def test_unitarity_in_ybe(self):
        """Unitarity holds (verified within YBE computation)."""
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)
        assert result['unitarity_satisfied']

    def test_no_mixing_prerequisite(self):
        """No cross-sector mixing (prerequisite for direct sum argument)."""
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)
        assert result['no_cross_sector_mixing']


# ===================================================================
# 7. NONZERO COUNT
# ===================================================================

class TestNonzeroCount:
    """Test the number of nonzero entries at delta=0."""

    def test_diagonal_324(self):
        """324 diagonal entries are nonzero."""
        result = nonzero_count_at_delta_zero(U_SAFE, H_BASE, ALPHA)
        assert result['n_diag_nonzero'] == 324

    def test_offdiag_48(self):
        """48 off-diagonal entries are nonzero."""
        result = nonzero_count_at_delta_zero(U_SAFE, H_BASE, ALPHA)
        assert result['n_offdiag_nonzero'] == 48

    def test_total_372(self):
        """Total nonzero entries: 324 + 48 = 372."""
        result = nonzero_count_at_delta_zero(U_SAFE, H_BASE, ALPHA)
        # VERIFIED [DC] nonzero count [DA] explicit matrix scan
        assert result['n_total_nonzero'] == 372

    def test_sparsity(self):
        """Sparsity > 99.6% (104,604 / 104,976 entries are zero)."""
        result = nonzero_count_at_delta_zero(U_SAFE, H_BASE, ALPHA)
        assert result['sparsity'] > 0.996

    def test_offdiag_breakdown(self):
        """Off-diagonal breakdown: 2 (ade_row) + 2 (ade_col) + 44 (mixed) = 48."""
        result = nonzero_count_at_delta_zero(U_SAFE, H_BASE, ALPHA)
        bd = result['offdiag_breakdown']
        assert bd['ade_row'] == 2
        assert bd['ade_col'] == 2
        assert bd['mixed'] == 44
        assert bd['total'] == 48


# ===================================================================
# 8. EIGENVALUE SPLITTING
# ===================================================================

class TestEigenvalueSplitting:
    """Test eigenvalue splitting profile as delta varies."""

    def test_degenerate_at_delta_zero(self):
        """Eigenvalues degenerate at delta=0 (maximal mixing)."""
        result = eigenvalue_splitting_profile(
            U_SAFE, H_BASE, ALPHA, delta_values=[0.0],
        )
        r = result['results'][0]
        assert r['ev_splitting'] < 1e-10

    def test_maximal_mixing_at_zero(self):
        """Mixing angle = 45 deg at delta=0."""
        result = eigenvalue_splitting_profile(
            U_SAFE, H_BASE, ALPHA, delta_values=[0.0],
        )
        r = result['results'][0]
        assert abs(r['mixing_angle_deg'] - 45.0) < 0.01

    def test_splitting_grows_with_delta(self):
        """Eigenvalue splitting grows with delta."""
        result = eigenvalue_splitting_profile(
            U_SAFE, H_BASE, ALPHA, delta_values=[0.0, 0.1, 0.5],
        )
        splits = [r['ev_splitting'] for r in result['results'] if not r.get('has_pole')]
        assert splits[0] < splits[1] < splits[2]

    def test_mixing_angle_decreases_with_delta(self):
        """Mixing angle decreases as delta increases (toward abelian limit)."""
        result = eigenvalue_splitting_profile(
            U_SAFE, H_BASE, ALPHA, delta_values=[0.001, 0.1, 1.0],
        )
        angles = [r['mixing_angle_deg'] for r in result['results']
                   if not r.get('has_pole')]
        assert angles[0] > angles[1] > angles[2]

    def test_mixing_angle_bounded(self):
        """Mixing angle is in [0, 45] degrees."""
        result = eigenvalue_splitting_profile(
            U_SAFE, H_BASE, ALPHA, delta_values=[0.0, 0.01, 0.1, 1.0, 5.0],
        )
        for r in result['results']:
            if not r.get('has_pole'):
                assert 0 <= r['mixing_angle_deg'] <= 45.01


# ===================================================================
# 9. BLOCK INVARIANTS
# ===================================================================

class TestBlockInvariants:
    """Test determinant and trace of 2x2 blocks."""

    def test_invariants_at_delta_zero(self):
        """Block invariants match at delta=0."""
        result = block_invariants(U_SAFE, H_BASE, ALPHA, delta=0.0)
        assert result['all_invariants_match']

    def test_det_matches(self):
        """All block determinants match the Yang formula."""
        result = block_invariants(U_SAFE, H_BASE, ALPHA, delta=0.0)
        assert result['all_det_match']

    def test_tr_matches(self):
        """All block traces match the Yang formula."""
        result = block_invariants(U_SAFE, H_BASE, ALPHA, delta=0.0)
        assert result['all_tr_match']

    def test_invariants_at_delta_positive(self):
        """Block invariants match at delta > 0."""
        result = block_invariants(U_SAFE, H_BASE, ALPHA, delta=0.1)
        assert result['all_invariants_match']

    def test_24_blocks(self):
        """24 blocks verified."""
        result = block_invariants(U_SAFE, H_BASE, ALPHA, delta=0.0)
        assert result['n_blocks'] == 24


# ===================================================================
# 10. CROSSING SYMMETRY
# ===================================================================

class TestCrossingSymmetry:
    """Test crossing symmetry R(u)*R_21(-u) = Id."""

    def test_crossing_even_even(self):
        """Crossing symmetry for even-even A_1."""
        result = crossing_symmetry_check(U_SAFE, H_BASE, ALPHA, merged=(0, 1))
        # VERIFIED [DC] crossing [DA] Yang unitarity
        assert result['multi_crossing_all_pass']

    def test_crossing_odd_odd(self):
        """Crossing symmetry for odd-odd A_1."""
        result = crossing_symmetry_check(U_SAFE, H_BASE, ALPHA, merged=(4, 5))
        assert result['multi_crossing_all_pass']

    def test_crossing_error_small(self):
        """Crossing error is negligible."""
        result = crossing_symmetry_check(U_SAFE, H_BASE, ALPHA)
        assert result['multi_crossing_max_error'] < 1e-10


# ===================================================================
# 11. DEFORMATION PROFILE
# ===================================================================

class TestDeformationProfile:
    """Test the full deformation profile."""

    def test_48_for_all_delta(self):
        """48 off-diagonal entries at all delta values."""
        result = deformation_profile(U_SAFE, H_BASE, ALPHA)
        for r in result['results']:
            if not r.get('has_pole'):
                assert r['n_offdiag'] == 48

    def test_ev_split_grows(self):
        """Eigenvalue splitting grows with delta."""
        result = deformation_profile(
            U_SAFE, H_BASE, ALPHA,
            delta_values=[0.0, 0.1, 0.5, 1.0],
        )
        splits = [r['ade_row_ev_split'] for r in result['results']
                   if not r.get('has_pole')]
        for i in range(len(splits) - 1):
            assert splits[i] <= splits[i + 1] + 1e-10


# ===================================================================
# 12. FERMIONIC SIGN COMPARISON
# ===================================================================

class TestFermionicSign:
    """Test even-even vs odd-odd parity effects."""

    def test_even_even_sign_positive(self):
        """Even-even: sign = +1."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                          alpha=ALPHA, merged=(0, 1))
        assert data['sign'] == +1

    def test_odd_odd_sign_negative(self):
        """Odd-odd: sign = -1."""
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                          alpha=ALPHA, merged=(4, 5))
        assert data['sign'] == -1

    def test_both_48_offdiag(self):
        """Both parity cases give exactly 48 off-diagonal entries."""
        ee = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                        alpha=ALPHA, merged=(0, 1))
        oo = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                        alpha=ALPHA, merged=(4, 5))
        assert ee['n_offdiag_nonzero'] == 48
        assert oo['n_offdiag_nonzero'] == 48

    def test_offdiag_factor_opposite_sign(self):
        """Even-even and odd-odd off-diagonal factors have opposite signs."""
        ee = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                        alpha=ALPHA, merged=(0, 1))
        oo = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0,
                                        alpha=ALPHA, merged=(4, 5))
        assert ee['yang_offdiag_factor'] > 0
        assert oo['yang_offdiag_factor'] < 0


# ===================================================================
# 13. MASTER COMPUTATION
# ===================================================================

class TestMaster:
    """Test the master nonabelian A_1 R-matrix computation."""

    def test_master_runs(self):
        """Master computation completes."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['status'] == 'CONJECTURAL'

    def test_master_48_both(self):
        """Both parity cases give 48 off-diagonal."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['even_even']['n_offdiag'] == 48
        assert result['odd_odd']['n_offdiag'] == 48

    def test_master_no_mixing(self):
        """No complement mixing in both cases."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['key_results']['no_complement_mixing']

    def test_master_ybe(self):
        """YBE passes in both cases."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['key_results']['ybe_all_pass']

    def test_master_crossing(self):
        """Crossing symmetry passes in both cases."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['key_results']['crossing_all_pass']

    def test_master_pole_resolved(self):
        """Double pole is resolved to simple pole."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['key_results']['pole_resolved']

    def test_master_invariants(self):
        """Block invariants match the Yang formula."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['key_results']['invariants_match']

    def test_master_nonzero_372(self):
        """372 nonzero entries at delta=0."""
        result = master_nonabelian_a1_rmatrix(U_SAFE, H_BASE, ALPHA)
        assert result['nonzero_at_delta_zero'] == 372


# ===================================================================
# 14. MULTI-PATH CROSS-CHECKS (AP10)
# ===================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification: each assertion cross-checked via independent route.

    Path A: algebraic (Yang R-matrix formula)
    Path B: block structure (sector decomposition)
    Path C: matrix-level (numpy on 324x324)
    Path D: deformation (delta profile)
    Path E: physical (pole resolution, crossing)
    """

    def test_48_via_three_paths(self):
        """48 off-diagonal via algebraic, block, and matrix paths.

        Path A: 2 (ade_row) + 2 (ade_col) + 44 (mixed) = 48.
        Path B: nonzero_count_at_delta_zero breakdown.
        Path C: build_deformed_a1_rmatrix matrix scan.
        """
        # Path A
        path_a = 2 + 2 + 22 * 2

        # Path B
        nz = nonzero_count_at_delta_zero(U_SAFE, H_BASE, ALPHA)
        path_b = nz['offdiag_breakdown']['total']

        # Path C
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, 0.0, ALPHA)
        path_c = data['n_offdiag_nonzero']

        # CROSS-CHECK [XC3]
        assert path_a == 48
        assert path_b == 48
        assert path_c == 48

    def test_no_mixing_via_two_paths(self):
        """No mixing via complement_mixing_analysis and ybe_full_block_structure.

        Path B: complement_mixing_analysis direct check.
        Path D: ybe_full_block_structure prerequisite check.
        """
        # Path B
        path_b = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA)

        # Path D
        path_d = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)

        # CROSS-CHECK [XC2]
        assert path_b['no_mixing']
        assert path_d['no_cross_sector_mixing']

    def test_ybe_via_block_and_direct_sum(self):
        """YBE via two independent paths.

        Path A: yang_ybe for the 2x2 block (algebraic).
        Path D: ybe_full_block_structure (direct sum argument).
        """
        from k3_rmatrix_enhanced import yang_r_verify_ybe as yang_ybe

        # Path A: direct Yang R-matrix YBE
        path_a = yang_ybe(U_SAFE, 2.3, hbar=ALPHA, n=2)

        # Path D: full block structure verification
        path_d = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)

        # CROSS-CHECK [XC2]
        assert path_a['ybe_satisfied']
        assert path_d['direct_sum_ybe_valid']

    def test_pole_resolution_cross_check(self):
        """Pole resolution: abelian (order 2) vs Yang (order 1).

        Path A: algebraic formula.
        Path E: double_pole_resolution computation.
        """
        # Path A: the abelian eigenvalue ((u-h)/(u+h))^2 has order 2 at u=-h
        path_a_abelian_order = 2
        # Yang antisymmetric: (u-alpha)/(u+alpha) has order 1 at u=-alpha
        path_a_yang_order = 1

        # Path E: computed
        path_e = double_pole_resolution(H_BASE, ALPHA)

        # CROSS-CHECK [XC2]
        assert path_a_abelian_order == path_e['abelian_pole_order']
        assert path_a_yang_order == path_e['yang_antisym_pole_order']

    def test_crossing_via_two_methods(self):
        """Crossing symmetry via crossing_symmetry_check and direct computation.

        Path A: crossing_symmetry_check (multi-u).
        Path C: direct numpy computation.
        """
        from k3_rmatrix_enhanced import yang_r_matrix_sl2

        # Path A
        path_a = crossing_symmetry_check(U_SAFE, H_BASE, ALPHA)

        # Path C: direct computation
        R_u = yang_r_matrix_sl2(U_SAFE, hbar=ALPHA)
        R_neg_u = yang_r_matrix_sl2(-U_SAFE, hbar=ALPHA)
        P = np.zeros((4, 4))
        for i in range(2):
            for j in range(2):
                P[j * 2 + i, i * 2 + j] = 1.0
        product = R_u @ P @ R_neg_u @ P
        path_c = np.allclose(product, np.eye(4), atol=1e-10)

        # CROSS-CHECK [XC2]
        assert path_a['multi_crossing_all_pass']
        assert path_c

    def test_deformation_persistent_48_cross_check(self):
        """48 off-diagonal entries persist across deformation.

        Path C: build_deformed_a1_rmatrix at multiple delta values.
        Path D: deformation_profile aggregated result.
        """
        # Path C: individual builds
        for delta in [0.0, 0.01, 0.1, 1.0]:
            data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta, ALPHA)
            assert data['n_offdiag_nonzero'] == 48

        # Path D: profile
        prof = deformation_profile(
            U_SAFE, H_BASE, ALPHA,
            delta_values=[0.0, 0.01, 0.1, 1.0],
        )
        for r in prof['results']:
            if not r.get('has_pole'):
                assert r['n_offdiag'] == 48


# ===================================================================
# 15. EDGE CASES
# ===================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_complex_u(self):
        """R-matrix works with complex spectral parameter."""
        data = build_deformed_a1_rmatrix(5.7 + 1j, H_BASE, delta=0.0, alpha=ALPHA)
        assert data['R'].shape == (324, 324)
        assert data['n_offdiag_nonzero'] == 48

    def test_large_u(self):
        """At large u, off-diagonal entries are small."""
        data = build_deformed_a1_rmatrix(1000.0, H_BASE, delta=0.0, alpha=ALPHA)
        assert abs(data['yang_offdiag_factor']) < 0.01

    def test_various_alpha(self):
        """R-matrix at various alpha values."""
        for alpha in [0.5, 1.0, 2.0]:
            data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, delta=0.0, alpha=alpha)
            assert data['n_offdiag_nonzero'] == 48

    def test_pole_detection(self):
        """Pole detected at u = -alpha (bosonic)."""
        data = build_deformed_a1_rmatrix(-1.0, H_BASE, delta=0.0,
                                          alpha=1.0, merged=(0, 1))
        assert data['has_pole']

    def test_custom_complement(self):
        """Custom complement weights work correctly."""
        comp = list(np.linspace(-0.2, 0.1, 22))
        comp[-1] = -2 * H_BASE - sum(comp[:-1])
        data = build_deformed_a1_rmatrix(
            U_SAFE, H_BASE, delta=0.0, alpha=ALPHA,
            h_complement=comp,
        )
        assert data['n_offdiag_nonzero'] == 48


# ===================================================================
# 16. CONJECTURAL STATUS
# ===================================================================

class TestConjecturalStatus:
    """Verify all outputs carry CONJECTURAL status (AP-CY14)."""

    def test_module_status(self):
        assert STATUS == 'CONJECTURAL'

    def test_deformed_status(self):
        data = build_deformed_a1_rmatrix(U_SAFE, H_BASE, 0.0, ALPHA)
        assert data['status'] == 'CONJECTURAL'

    def test_pole_status(self):
        result = double_pole_resolution()
        assert result['status'] == 'CONJECTURAL'

    def test_mixing_status(self):
        result = complement_mixing_analysis(U_SAFE, H_BASE, ALPHA)
        assert result['status'] == 'CONJECTURAL'

    def test_ybe_status(self):
        result = ybe_full_block_structure(U_SAFE, 2.3, H_BASE, ALPHA)
        assert result['status'] == 'CONJECTURAL'

    def test_master_status(self):
        result = master_nonabelian_a1_rmatrix()
        assert result['status'] == 'CONJECTURAL'
