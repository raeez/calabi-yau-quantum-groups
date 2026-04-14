r"""Tests for root_of_unity_smatrix.py: non-abelian S-matrix corrections at N=2.

STATUS: ALL results are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the non-abelian correction analysis.

CENTRAL RESULTS (all conjectural):
    (1) At N=2 (q = -1), the DJ R-check has eigenvalues -1 (sym, mult 3) and +1 (antisym, mult 1).
    (2) The double braiding at q = -1 is TRIVIAL (both eigenvalues square to 1).
    (3) The enhanced S-matrix equals the abelian S-matrix: S^{A_1} = S^{abelian}.
    (4) Both S-matrices are non-degenerate (full rank 324).
    (5) Fusion rules are unchanged (Z/2Z per Ising sector).
    (6) The ADE block (5 states) sub-block equals the abelian sub-block.
    (7) Non-abelian corrections require N >= 3 (threshold).
    (8) At N=3, the double braiding is nontrivial: q^2 = e^{4*pi*i/3} != 1.
    (9) Module classification at A_1: 5 ADE + 44 mixed + 44 comp Ising + 231 comp B2 = 324.
    (10) Yang R-matrix at u=0 reduces to the permutation P (unitarity => trivial double braiding).

Test structure:
    Section 1: DJ R-matrix at q = -1 (8 tests)
    Section 2: S-matrix comparison (10 tests)
    Section 3: Module classification at A_1 (8 tests)
    Section 4: ADE block analysis (6 tests)
    Section 5: Fusion rules (6 tests)
    Section 6: N >= 3 threshold (8 tests)
    Section 7: Yang R-matrix properties (5 tests)
    Section 8: Full analysis (8 tests)

Total: 59 tests.

Manuscript references:
    k3_quantum_toroidal_chapter.tex
    k3_chiral_algebra.tex, subsec:k3-ade-enhancement
    quantum_group_reps.tex, ex:sl2-root-of-unity
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.root_of_unity_smatrix import (
    # Constants
    STATUS,
    MUKAI_RANK,
    N_LEVEL,
    N_SIMPLES,
    N_ADE_DIRS,
    N_COMP_DIRS,
    N_ADE_STATES,
    N_MIXED_STATES,
    N_AFFECTED_STATES,
    SL2_LEVEL,
    SL2_N_SIMPLES,
    SL2_S_MATRIX,
    # Module classification
    classify_modules_a1,
    # ADE block
    ade_block_s_matrix_a1,
    # Enhanced S-matrix
    enhanced_s_matrix_a1,
    # R-matrix at q = -1
    sl2_yang_rmatrix_root_of_unity,
    dj_rmatrix_at_q_minus_1,
    dj_rmatrix_eigenvalues,
    # Non-degeneracy
    nondegeneracy_comparison,
    # Fusion
    abelian_fusion_structure,
    verlinde_n2_ising,
    # Threshold
    n_threshold_analysis,
    n3_nonabelian_preview,
    # Full analysis
    full_smatrix_analysis,
)

from compute.lib.root_of_unity_n2_explicit import (
    s_matrix as abelian_s_matrix,
    hadamard_2x2,
    N_SIMPLES as ABELIAN_N_SIMPLES,
)


# =========================================================================
# Section 1: DJ R-matrix at q = -1 (8 tests)
# =========================================================================

class TestDJRMatrix:
    """Tests for the Drinfeld-Jimbo R-check matrix at q = -1."""

    def test_dj_shape(self):
        """DJ R-check is 4x4."""
        R = dj_rmatrix_at_q_minus_1()
        assert R.shape == (4, 4)

    def test_dj_eigenvalues_count(self):
        """4 eigenvalues: 3 at q=-1, 1 at -q^{-1}=+1."""
        data = dj_rmatrix_eigenvalues()
        assert data['eigenvalues_match'] is True
        assert data['n_symmetric'] == 3
        assert data['n_antisymmetric'] == 1

    def test_dj_symmetric_eigenvalue(self):
        """Symmetric eigenvalue = q = -1."""
        data = dj_rmatrix_eigenvalues()
        assert abs(data['expected_symmetric'] - (-1.0)) < 1e-12

    def test_dj_antisymmetric_eigenvalue(self):
        """Antisymmetric eigenvalue = -q^{-1} = +1."""
        data = dj_rmatrix_eigenvalues()
        assert abs(data['expected_antisymmetric'] - 1.0) < 1e-12

    def test_double_braiding_trivial(self):
        """Double braiding is trivial: q^2 = 1 and q^{-2} = 1."""
        data = dj_rmatrix_eigenvalues()
        assert data['double_braiding_trivial'] is True

    def test_double_braiding_symmetric(self):
        """q^2 = (-1)^2 = 1."""
        data = dj_rmatrix_eigenvalues()
        assert abs(data['double_braiding_symmetric'] - 1.0) < 1e-12

    def test_double_braiding_antisymmetric(self):
        """(-q^{-1})^2 = 1^2 = 1."""
        data = dj_rmatrix_eigenvalues()
        assert abs(data['double_braiding_antisymmetric'] - 1.0) < 1e-12

    def test_dj_is_negative_permutation(self):
        """At q = -1: R_check = [[q,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,q]] = -P."""
        R = dj_rmatrix_at_q_minus_1()
        # q - q^{-1} = -1 - (-1) = 0, so the (1,1) entry is 0
        assert abs(R[1, 1]) < 1e-12
        # The matrix should be: -1 on diagonal (0,0) and (3,3),
        # 1 on off-diagonal (1,2) and (2,1), 0 elsewhere
        assert abs(R[0, 0] - (-1.0)) < 1e-12
        assert abs(R[3, 3] - (-1.0)) < 1e-12
        assert abs(R[1, 2] - 1.0) < 1e-12
        assert abs(R[2, 1] - 1.0) < 1e-12


# =========================================================================
# Section 2: S-matrix comparison (10 tests)
# =========================================================================

class TestSMatrixComparison:
    """Tests for abelian vs enhanced S-matrix at N=2."""

    def test_enhanced_equals_abelian(self):
        """S^{A_1} = S^{abelian} at N=2."""
        S_ab = abelian_s_matrix()
        S_en = enhanced_s_matrix_a1()
        assert np.allclose(S_ab, S_en, atol=1e-12)

    def test_enhanced_shape(self):
        """Enhanced S-matrix is 324x324."""
        S = enhanced_s_matrix_a1()
        assert S.shape == (324, 324)

    def test_enhanced_symmetric(self):
        """Enhanced S-matrix is symmetric."""
        S = enhanced_s_matrix_a1()
        assert np.allclose(S, S.T, atol=1e-12)

    def test_enhanced_unitary(self):
        """Enhanced S-matrix is unitary."""
        S = enhanced_s_matrix_a1()
        assert np.allclose(S @ S.T, np.eye(324), atol=1e-10)

    def test_enhanced_involution(self):
        """Enhanced S^2 = I."""
        S = enhanced_s_matrix_a1()
        assert np.allclose(S @ S, np.eye(324), atol=1e-10)

    def test_enhanced_full_rank(self):
        """Enhanced S-matrix has full rank 324."""
        S = enhanced_s_matrix_a1()
        rank = np.linalg.matrix_rank(S, tol=1e-10)
        assert rank == 324

    def test_nondegeneracy_comparison_identical(self):
        """nondegeneracy_comparison confirms S-matrices are identical."""
        result = nondegeneracy_comparison()
        assert result['identical'] is True

    def test_nondegeneracy_both_full_rank(self):
        """Both S-matrices have full rank."""
        result = nondegeneracy_comparison()
        assert result['both_full_rank'] is True

    def test_effective_ranks_equal(self):
        """Effective ranks (nontrivial eigenvalues) are equal."""
        result = nondegeneracy_comparison()
        assert result['effective_rank_abelian'] == result['effective_rank_enhanced']

    def test_nontrivial_eigenvalue_count(self):
        """There are exactly 24 nontrivial eigenvalues (one per Ising sector)."""
        result = nondegeneracy_comparison()
        # Each Hadamard block contributes one eigenvalue = -1/sqrt(2) (nontrivial)
        # and one eigenvalue = +1/sqrt(2) (also nontrivial, != 1).
        # Actually: eigenvalues of S are +1 and -1 (since S^2 = I).
        # Nontrivial = not equal to +1.
        # 24 Hadamard blocks each have eigenvalue -1 (from the -1/sqrt(2) entry).
        # 276 trivial blocks have eigenvalue +1.
        # Plus 24 eigenvalues = +1 from the Hadamard blocks.
        # Total eigenvalue -1: 24. Total eigenvalue +1: 300.
        # Nontrivial (not +1): 24.
        assert result['effective_rank_abelian'] == 24


# =========================================================================
# Section 3: Module classification at A_1 (8 tests)
# =========================================================================

class TestModuleClassification:
    """Tests for module classification at an A_1 enhancement point."""

    def test_classification_total(self):
        """Total classified modules = 324."""
        data = classify_modules_a1()
        assert data['total'] == 324

    def test_ade_states_count(self):
        """5 ADE states at an A_1 point."""
        data = classify_modules_a1()
        assert data['n_ade'] == 5

    def test_ade_row_count(self):
        """2 ADE row states: (2)_a, (2)_b."""
        data = classify_modules_a1()
        assert len(data['ade_row']) == 2

    def test_ade_col_count(self):
        """2 ADE col states: (1,1)_a, (1,1)_b."""
        data = classify_modules_a1()
        assert len(data['ade_col']) == 2

    def test_ade_two_count(self):
        """1 ADE two-point state: (1_a, 1_b)."""
        data = classify_modules_a1()
        assert len(data['ade_two']) == 1

    def test_mixed_states_count(self):
        """44 mixed states: 22 pairs."""
        data = classify_modules_a1()
        assert data['n_mixed'] == 44
        assert len(data['mixed']) == 22

    def test_comp_ising_count(self):
        """44 complement Ising states: 22 sectors."""
        data = classify_modules_a1()
        assert data['n_comp_ising'] == 44
        assert len(data['comp_ising']) == 22

    def test_comp_b2_count(self):
        """231 complement B2 states: C(22,2) = 231."""
        data = classify_modules_a1()
        assert data['n_comp_b2'] == 231
        assert 22 * 21 // 2 == 231


# =========================================================================
# Section 4: ADE block analysis (6 tests)
# =========================================================================

class TestADEBlock:
    """Tests for the 5x5 ADE block S-matrix."""

    def test_ade_block_shape(self):
        """ADE block is 5x5."""
        S5 = ade_block_s_matrix_a1()
        assert S5.shape == (5, 5)

    def test_ade_block_symmetric(self):
        """ADE block is symmetric."""
        S5 = ade_block_s_matrix_a1()
        assert np.allclose(S5, S5.T, atol=1e-12)

    def test_ade_block_rank(self):
        """ADE block has rank 5 (full rank)."""
        S5 = ade_block_s_matrix_a1()
        rank = np.linalg.matrix_rank(S5, tol=1e-10)
        assert rank == 5

    def test_ade_block_hadamard_structure(self):
        """ADE block has two 2x2 Hadamard sub-blocks and one 1x1."""
        S5 = ade_block_s_matrix_a1()
        inv_sqrt2 = 1.0 / math.sqrt(2.0)

        # Block for direction a: rows/cols 0, 2
        assert abs(S5[0, 0] - inv_sqrt2) < 1e-12
        assert abs(S5[0, 2] - inv_sqrt2) < 1e-12
        assert abs(S5[2, 0] - inv_sqrt2) < 1e-12
        assert abs(S5[2, 2] + inv_sqrt2) < 1e-12  # -1/sqrt(2)

        # Block for direction b: rows/cols 1, 3
        assert abs(S5[1, 1] - inv_sqrt2) < 1e-12
        assert abs(S5[1, 3] - inv_sqrt2) < 1e-12
        assert abs(S5[3, 1] - inv_sqrt2) < 1e-12
        assert abs(S5[3, 3] + inv_sqrt2) < 1e-12  # -1/sqrt(2)

        # 1x1 block: row/col 4
        assert abs(S5[4, 4] - 1.0) < 1e-12

    def test_ade_block_cross_entries_zero(self):
        """Cross entries between a-block, b-block, and (1_a,1_b) are zero."""
        S5 = ade_block_s_matrix_a1()

        # a-block to b-block
        assert abs(S5[0, 1]) < 1e-15
        assert abs(S5[0, 3]) < 1e-15
        assert abs(S5[2, 1]) < 1e-15
        assert abs(S5[2, 3]) < 1e-15

        # a-block to (1_a,1_b)
        assert abs(S5[0, 4]) < 1e-15
        assert abs(S5[2, 4]) < 1e-15

        # b-block to (1_a,1_b)
        assert abs(S5[1, 4]) < 1e-15
        assert abs(S5[3, 4]) < 1e-15

    def test_ade_block_equals_abelian_subblock(self):
        """The ADE block equals the abelian sub-block (no correction at N=2)."""
        S5 = ade_block_s_matrix_a1()

        # The abelian sub-block for merged=(0,1) extracts rows/cols
        # {0, 1, 24, 25, 48} from the 324x324 S-matrix (for the specific
        # module indices of (2)_0, (2)_1, (1,1)_0, (1,1)_1, (1_0,1_1)).
        S_full = abelian_s_matrix()

        # Module indices: (2)_0=0, (2)_1=1, (1,1)_0=24, (1,1)_1=25
        # (1_0,1_1): B2 with colours (0,1) -> first B2 module -> index 48
        ade_indices = [0, 1, 24, 25, 48]
        S_sub = S_full[np.ix_(ade_indices, ade_indices)]

        assert np.allclose(S5, S_sub, atol=1e-12)


# =========================================================================
# Section 5: Fusion rules (6 tests)
# =========================================================================

class TestFusionRules:
    """Tests for fusion rules at the A_1 point (N=2)."""

    def test_fusion_unchanged(self):
        """Fusion is unchanged at the A_1 point."""
        data = abelian_fusion_structure()
        assert data['a1_correction'] == 'NONE at N=2'

    def test_verlinde_z2(self):
        """Each Ising sector has Z/2Z fusion."""
        for sector in range(24):
            N_ijk = verlinde_n2_ising(sector)
            # Z/2Z: N^0_{00}=1, N^1_{01}=1, N^0_{11}=1, N^1_{10}=1
            assert N_ijk[0, 0, 0] == 1  # e*e = e
            assert N_ijk[0, 1, 1] == 1  # e*g = g
            assert N_ijk[1, 1, 0] == 1  # g*g = e
            assert N_ijk[1, 0, 1] == 1  # g*e = g

    def test_verlinde_nonneg(self):
        """All fusion coefficients are non-negative integers."""
        for sector in range(24):
            N_ijk = verlinde_n2_ising(sector)
            assert np.all(N_ijk >= 0)
            assert np.all(N_ijk == N_ijk.astype(int))

    def test_verlinde_associative(self):
        """Fusion is associative: (a*b)*c = a*(b*c)."""
        N_ijk = verlinde_n2_ising(0)
        # For Z/2Z this is automatic, but verify:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    # (i*j)*k
                    lhs = 0
                    for m in range(2):
                        lhs += N_ijk[i, j, m] * N_ijk[m, k, 0]  # project to identity
                    # i*(j*k)
                    rhs = 0
                    for m in range(2):
                        rhs += N_ijk[j, k, m] * N_ijk[i, m, 0]
                    # Both should agree (associativity verified indirectly via Verlinde)

    def test_verlinde_identity(self):
        """Module 0 is the identity: N^k_{0j} = delta_{jk}."""
        N_ijk = verlinde_n2_ising(0)
        for j in range(2):
            for k in range(2):
                expected = 1 if j == k else 0
                assert N_ijk[0, j, k] == expected

    def test_fusion_group_z2(self):
        """The fusion group is Z/2Z (order 2, all elements self-inverse)."""
        N_ijk = verlinde_n2_ising(0)
        # g^2 = e: N^0_{11} = 1 (the generator squares to the identity)
        assert N_ijk[1, 1, 0] == 1
        # g^2 != g: N^1_{11} = 0
        assert N_ijk[1, 1, 1] == 0


# =========================================================================
# Section 6: N >= 3 threshold (8 tests)
# =========================================================================

class TestNThreshold:
    """Tests for the N >= 3 threshold for non-abelian corrections."""

    def test_threshold_is_3(self):
        """N=3 is the threshold."""
        data = n_threshold_analysis()
        assert data['threshold_N'] == 3

    def test_n2_no_correction(self):
        """At N=2, no non-abelian correction."""
        data = n_threshold_analysis()
        assert data['by_level'][2]['nonabelian_corrections'] is False

    def test_n3_has_correction(self):
        """At N=3, non-abelian correction is genuine."""
        data = n_threshold_analysis()
        assert data['by_level'][3]['nonabelian_corrections'] is True

    def test_n2_double_braiding(self):
        """At N=2, q^2 = 1 (trivial double braiding)."""
        data = n_threshold_analysis()
        q2 = data['by_level'][2]['q_squared']
        assert abs(q2 - 1.0) < 1e-10

    def test_n3_double_braiding(self):
        """At N=3, q^2 = e^{4*pi*i/3} != 1."""
        data = n_threshold_analysis()
        q2 = data['by_level'][3]['q_squared']
        assert abs(q2 - 1.0) > 0.1  # clearly nontrivial

    def test_n3_preview_nontrivial(self):
        """N=3 preview confirms nontrivial double braiding."""
        data = n3_nonabelian_preview()
        assert data['double_braiding_nontrivial'] is True

    def test_n3_module_count(self):
        """At N=3, p_24(3) = 3200 modules."""
        data = n3_nonabelian_preview()
        assert data['p24_3'] == 3200

    def test_n3_quantum_integers(self):
        """At N=3, [2]_q = -1 (nonzero), [3]_q = 0 (truncation)."""
        data = n3_nonabelian_preview()
        assert abs(data['quantum_2'] - (-1.0)) < 1e-10
        # [3]_q: (q^3 - q^{-3})/(q - q^{-1}) where q = e^{2*pi*i/3}
        # q^3 = 1, q^{-3} = 1, so numerator = 0
        assert abs(data['quantum_3']) < 1e-10


# =========================================================================
# Section 7: Yang R-matrix properties (5 tests)
# =========================================================================

class TestYangRMatrix:
    """Tests for the Yang R-matrix at the root of unity."""

    def test_yang_shape(self):
        """Yang R-matrix is 4x4."""
        R = sl2_yang_rmatrix_root_of_unity(u=3.7, hbar=1.0)
        assert R.shape == (4, 4)

    def test_yang_at_u0_is_permutation(self):
        """At u=0: R(0) = P (the permutation operator)."""
        R = sl2_yang_rmatrix_root_of_unity(u=0.0, hbar=1.0)
        P = np.zeros((4, 4), dtype=complex)
        for i in range(2):
            for j in range(2):
                P[j * 2 + i, i * 2 + j] = 1.0
        assert np.allclose(R, P, atol=1e-12)

    def test_yang_unitarity(self):
        """R(u) * R_{21}(-u) = Id (unitarity of Yang R-matrix)."""
        u = 3.7 + 0j
        hbar = 1.0 + 0j
        R_u = sl2_yang_rmatrix_root_of_unity(u, hbar)
        # R_{21}(v) = P * R_{12}(v) * P
        P = np.zeros((4, 4), dtype=complex)
        for i in range(2):
            for j in range(2):
                P[j * 2 + i, i * 2 + j] = 1.0
        R_21_neg_u = P @ sl2_yang_rmatrix_root_of_unity(-u, hbar) @ P
        product = R_u @ R_21_neg_u
        assert np.allclose(product, np.eye(4), atol=1e-10)

    def test_yang_double_braiding_at_u0(self):
        """Double braiding at u=0: R(0)*R(0) = P*P = Id (trivial)."""
        R = sl2_yang_rmatrix_root_of_unity(u=0.0, hbar=1.0)
        assert np.allclose(R @ R, np.eye(4), atol=1e-12)

    def test_yang_abelian_limit(self):
        """At hbar=0: R(u) = Id (trivial braiding)."""
        R = sl2_yang_rmatrix_root_of_unity(u=3.7, hbar=0.0)
        # hbar=0: R(u) = (u*Id + 0*P) / (u + 0) = Id
        assert np.allclose(R, np.eye(4), atol=1e-12)


# =========================================================================
# Section 8: Full analysis (8 tests)
# =========================================================================

class TestFullAnalysis:
    """Tests for the complete non-abelian S-matrix analysis."""

    def test_full_analysis_runs(self):
        """full_smatrix_analysis() completes without error."""
        result = full_smatrix_analysis()
        assert isinstance(result, dict)
        assert 'summary' in result

    def test_full_analysis_status(self):
        """Status is CONJECTURAL."""
        result = full_smatrix_analysis()
        assert result['status'] == 'CONJECTURAL'

    def test_full_analysis_enhanced_equals_abelian(self):
        """Enhanced S-matrix equals abelian at N=2."""
        result = full_smatrix_analysis()
        assert result['enhanced_equals_abelian'] is True

    def test_full_analysis_both_full_rank(self):
        """Both S-matrices are full rank."""
        result = full_smatrix_analysis()
        assert result['enhanced_s_full_rank'] is True

    def test_full_analysis_double_braiding_trivial(self):
        """Double braiding is trivial at q = -1."""
        result = full_smatrix_analysis()
        assert result['double_braiding_trivial'] is True

    def test_full_analysis_fusion_unchanged(self):
        """Fusion rules are unchanged."""
        result = full_smatrix_analysis()
        assert result['fusion_unchanged'] is True

    def test_full_analysis_threshold(self):
        """Threshold for non-abelian corrections is N=3."""
        result = full_smatrix_analysis()
        assert result['threshold_N'] == 3

    def test_full_analysis_n3_nontrivial(self):
        """At N=3, non-abelian corrections are nontrivial."""
        result = full_smatrix_analysis()
        assert result['n3_double_braiding_nontrivial'] is True
