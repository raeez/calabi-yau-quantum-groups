r"""Tests for root_of_unity_n3_mtc.py: N=3 MTC for the K3 quantum toroidal.

STATUS: ALL results are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the N=3 MTC computation.

CENTRAL RESULTS (all conjectural):
    (1) p_24(3) = 3200 simple modules of 6 types (A, B1, C1, B2, C2, D).
    (2) 2600 sectors: 24 Ising (3x3) + 552 Hadamard (2x2) + 2024 trivial (1x1).
    (3) The sl_2 level-2 (Ising) S-matrix: d_1 = sqrt(2) (NON-ABELIAN).
    (4) 24 Type B1 modules have d = sqrt(2); 3176 modules have d = 1.
    (5) D^2 = 3224 > 3200: the MTC is NOT pointed.
    (6) Double braiding at q = e^{2*pi*i/3}: q^2 = e^{4*pi*i/3} != 1 (NONTRIVIAL).
    (7) Ising fusion: V_1 x V_1 = V_0 + V_2.
    (8) Charge-1 sector (24x24): diagonal in abelian case, off-diagonal at A_1.
    (9) Full 3200x3200 S-matrix is non-degenerate (modular).
    (10) N=3 is the threshold for non-abelian MTC structure.

Test structure:
    Section 1: Module enumeration and counting (10 tests)
    Section 2: Sector decomposition (8 tests)
    Section 3: Ising (sl_2 level-2) S-matrix (10 tests)
    Section 4: Quantum dimensions (8 tests)
    Section 5: DJ R-matrix and double braiding (8 tests)
    Section 6: Full S-matrix properties (8 tests)
    Section 7: Charge-1 sector (8 tests)
    Section 8: Ising fusion rules (8 tests)
    Section 9: N=2 vs N=3 comparison (6 tests)
    Section 10: Full analysis (6 tests)

Total: 80 tests.

Manuscript references:
    k3_quantum_toroidal_chapter.tex
    quantum_group_reps.tex, ex:sl2-root-of-unity
    k3_chiral_algebra.tex, subsec:k3-ade-enhancement
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.root_of_unity_n3_mtc import (
    # Constants
    STATUS,
    MUKAI_RANK,
    N_LEVEL,
    N_SIMPLES,
    N_TYPE_A,
    N_TYPE_B1,
    N_TYPE_C1,
    N_TYPE_B2,
    N_TYPE_C2,
    N_TYPE_D,
    N_SECTORS,
    N_SECTORS_3x3,
    N_SECTORS_2x2,
    N_SECTORS_1x1,
    OMEGA_N3,
    Q_SQUARED,
    D_V0,
    D_V1,
    D_V2,
    D_SQUARED,
    SL2_LEVEL,
    SL2_N_SIMPLES,
    QUANTUM_2,
    QUANTUM_3,
    # Module enumeration
    enumerate_modules,
    module_type_counts,
    sector_decomposition,
    # Ising S-matrix
    ising_s_matrix,
    ising_fusion_rules,
    ising_quantum_dimensions,
    # Hadamard
    hadamard_2x2,
    # Full S-matrix
    s_matrix,
    verify_s_properties,
    # Quantum dimensions
    all_quantum_dimensions,
    # T-matrix
    t_matrix,
    # DJ R-matrix
    dj_rmatrix_at_n3,
    dj_rmatrix_eigenvalues,
    # Charge-1 sector
    charge1_sector_indices,
    charge1_s_matrix_abelian,
    charge1_nondegeneracy,
    charge1_enhanced_a1,
    # Non-degeneracy
    nondegeneracy_analysis,
    # Comparison
    n2_n3_comparison,
    # Full analysis
    full_n3_analysis,
)


# =========================================================================
# Section 1: Module enumeration and counting (10 tests)
# =========================================================================

class TestModuleEnumeration:
    """Tests for the 3200 simple modules at N=3."""

    def test_total_count(self):
        """p_24(3) = 3200."""
        assert N_SIMPLES == 3200

    def test_type_counts(self):
        """Module type counts sum to 3200."""
        counts = module_type_counts()
        assert counts['total'] == 3200
        assert (counts['A'] + counts['B1'] + counts['C1']
                + counts['B2'] + counts['C2'] + counts['D']) == 3200

    def test_type_a_count(self):
        """24 Type A modules: (3_a)."""
        assert N_TYPE_A == 24

    def test_type_b1_count(self):
        """24 Type B1 modules: (2_a, 1_a)."""
        assert N_TYPE_B1 == 24

    def test_type_c1_count(self):
        """24 Type C1 modules: (1_a^3)."""
        assert N_TYPE_C1 == 24

    def test_type_b2_count(self):
        """552 Type B2 modules: (2_a, 1_b) for a != b."""
        assert N_TYPE_B2 == 24 * 23

    def test_type_c2_count(self):
        """552 Type C2 modules: (1_a^2, 1_b) for a != b."""
        assert N_TYPE_C2 == 24 * 23

    def test_type_d_count(self):
        """2024 Type D modules: C(24,3) = 2024."""
        from math import comb
        assert N_TYPE_D == comb(24, 3)
        assert N_TYPE_D == 2024

    def test_enumerate_length(self):
        """enumerate_modules() returns 3200 modules."""
        modules = enumerate_modules()
        assert len(modules) == 3200

    def test_enumerate_indices_unique(self):
        """All module indices are unique and span [0..3199]."""
        modules = enumerate_modules()
        indices = [m.index for m in modules]
        assert sorted(indices) == list(range(3200))


# =========================================================================
# Section 2: Sector decomposition (8 tests)
# =========================================================================

class TestSectorDecomposition:
    """Tests for the 2600 sectors."""

    def test_total_sectors(self):
        """2600 total sectors."""
        assert N_SECTORS == 2600

    def test_3x3_sectors(self):
        """24 Ising (3x3) sectors."""
        assert N_SECTORS_3x3 == 24

    def test_2x2_sectors(self):
        """552 Hadamard (2x2) sectors."""
        assert N_SECTORS_2x2 == 552

    def test_1x1_sectors(self):
        """2024 trivial (1x1) sectors."""
        assert N_SECTORS_1x1 == 2024

    def test_sector_module_count(self):
        """Sectors account for all modules: 24*3 + 552*2 + 2024*1 = 3200."""
        total = N_SECTORS_3x3 * 3 + N_SECTORS_2x2 * 2 + N_SECTORS_1x1 * 1
        assert total == 3200

    def test_sector_decomposition_dict(self):
        """sector_decomposition() returns correct data."""
        data = sector_decomposition()
        assert data['n_sectors'] == 2600
        assert data['ising_sectors'] == 24
        assert data['hadamard_sectors'] == 552
        assert data['trivial_sectors'] == 2024

    def test_sectors_unique(self):
        """All modules have unique sector assignments."""
        modules = enumerate_modules()
        sector_offsets = [(m.sector, m.sector_offset) for m in modules]
        assert len(set(sector_offsets)) == 3200

    def test_d_squared(self):
        """D^2 = 3224."""
        assert abs(D_SQUARED - 3224.0) < 1e-10


# =========================================================================
# Section 3: Ising (sl_2 level-2) S-matrix (10 tests)
# =========================================================================

class TestIsingSMatrix:
    """Tests for the 3x3 Ising S-matrix."""

    def test_shape(self):
        """Ising S-matrix is 3x3."""
        S = ising_s_matrix()
        assert S.shape == (3, 3)

    def test_symmetric(self):
        """Ising S-matrix is symmetric."""
        S = ising_s_matrix()
        assert np.allclose(S, S.T, atol=1e-12)

    def test_unitary(self):
        """Ising S-matrix is unitary."""
        S = ising_s_matrix()
        assert np.allclose(S @ S.T, np.eye(3), atol=1e-10)

    def test_determinant(self):
        """det(S_Ising) = -1."""
        S = ising_s_matrix()
        assert abs(np.linalg.det(S) - (-1.0)) < 1e-10

    def test_s00(self):
        """S_{00} = 1/2."""
        S = ising_s_matrix()
        assert abs(S[0, 0] - 0.5) < 1e-12

    def test_s01(self):
        """S_{01} = 1/sqrt(2)."""
        S = ising_s_matrix()
        assert abs(S[0, 1] - 1.0 / math.sqrt(2.0)) < 1e-12

    def test_s11_zero(self):
        """S_{11} = 0."""
        S = ising_s_matrix()
        assert abs(S[1, 1]) < 1e-12

    def test_s12_negative(self):
        """S_{12} = -1/sqrt(2)."""
        S = ising_s_matrix()
        assert abs(S[1, 2] - (-1.0 / math.sqrt(2.0))) < 1e-12

    def test_s22(self):
        """S_{22} = 1/2."""
        S = ising_s_matrix()
        assert abs(S[2, 2] - 0.5) < 1e-12

    def test_s_squared_is_identity(self):
        """S^2 = I (all Ising objects are self-dual)."""
        S = ising_s_matrix()
        S2 = S @ S
        assert np.allclose(S2, np.eye(3), atol=1e-10)


# =========================================================================
# Section 4: Quantum dimensions (8 tests)
# =========================================================================

class TestQuantumDimensions:
    """Tests for quantum dimensions at N=3."""

    def test_d_v0(self):
        """d_0 = 1 (vacuum)."""
        assert abs(D_V0 - 1.0) < 1e-12

    def test_d_v1_sqrt2(self):
        """d_1 = sqrt(2) (non-abelian!)."""
        assert abs(D_V1 - math.sqrt(2.0)) < 1e-12

    def test_d_v2(self):
        """d_2 = 1."""
        assert abs(D_V2 - 1.0) < 1e-12

    def test_ising_quantum_dims(self):
        """ising_quantum_dimensions() returns correct values."""
        data = ising_quantum_dimensions()
        assert abs(data['d_V0'] - 1.0) < 1e-12
        assert abs(data['d_V1'] - math.sqrt(2.0)) < 1e-12
        assert abs(data['d_V2'] - 1.0) < 1e-12

    def test_d_squared_sector(self):
        """D^2 per Ising sector = 4."""
        data = ising_quantum_dimensions()
        assert abs(data['D_squared_sector'] - 4.0) < 1e-10

    def test_not_pointed(self):
        """The MTC is NOT pointed (d_1 > 1)."""
        data = all_quantum_dimensions()
        assert data['is_pointed'] is False

    def test_nonabelian_count(self):
        """24 modules have d = sqrt(2)."""
        data = all_quantum_dimensions()
        assert data['n_nonabelian'] == 24

    def test_d_squared_total(self):
        """D^2 = 3224 > 3200."""
        data = all_quantum_dimensions()
        assert abs(data['D_squared'] - 3224.0) < 1e-10
        assert data['D_squared'] > N_SIMPLES


# =========================================================================
# Section 5: DJ R-matrix and double braiding (8 tests)
# =========================================================================

class TestDJRMatrix:
    """Tests for the DJ R-matrix at q = e^{2*pi*i/3}."""

    def test_shape(self):
        """DJ R-check is 4x4."""
        R = dj_rmatrix_at_n3()
        assert R.shape == (4, 4)

    def test_q_value(self):
        """q = e^{2*pi*i/3}."""
        q = OMEGA_N3
        expected = cmath.exp(2j * cmath.pi / 3)
        assert abs(q - expected) < 1e-12

    def test_eigenvalue_count(self):
        """3 symmetric + 1 antisymmetric eigenvalues."""
        data = dj_rmatrix_eigenvalues()
        assert data['eigenvalues_match'] is True
        assert data['n_symmetric'] == 3
        assert data['n_antisymmetric'] == 1

    def test_symmetric_eigenvalue(self):
        """Symmetric eigenvalue = q = e^{2*pi*i/3}."""
        data = dj_rmatrix_eigenvalues()
        expected = cmath.exp(2j * cmath.pi / 3)
        assert abs(data['expected_symmetric'] - expected) < 1e-10

    def test_antisymmetric_eigenvalue(self):
        """Antisymmetric eigenvalue = -q^{-1} = e^{i*pi/3}."""
        data = dj_rmatrix_eigenvalues()
        q = cmath.exp(2j * cmath.pi / 3)
        expected = -1.0 / q
        assert abs(data['expected_antisymmetric'] - expected) < 1e-10

    def test_double_braiding_nontrivial(self):
        """q^2 = e^{4*pi*i/3} != 1 (NONTRIVIAL!)."""
        data = dj_rmatrix_eigenvalues()
        assert data['double_braiding_nontrivial'] is True

    def test_q_squared_value(self):
        """q^2 = e^{4*pi*i/3}."""
        q2 = Q_SQUARED
        expected = cmath.exp(4j * cmath.pi / 3)
        assert abs(q2 - expected) < 1e-12

    def test_q_cubed_is_one(self):
        """q^3 = 1 (q is a primitive cube root of unity)."""
        assert abs(OMEGA_N3 ** 3 - 1.0) < 1e-12


# =========================================================================
# Section 6: Full S-matrix properties (8 tests)
# =========================================================================

class TestFullSMatrix:
    """Tests for the full 3200 x 3200 S-matrix."""

    def test_shape(self):
        """S-matrix is 3200x3200."""
        props = verify_s_properties()
        assert props['shape'] == (3200, 3200)

    def test_symmetric(self):
        """S-matrix is symmetric."""
        props = verify_s_properties()
        assert props['symmetric'] is True

    def test_unitary(self):
        """S-matrix is unitary."""
        props = verify_s_properties()
        assert props['unitary'] is True

    def test_s_squared_is_c(self):
        """S^2 = C (charge conjugation)."""
        props = verify_s_properties()
        assert props['s_squared_is_c'] is True

    def test_full_rank(self):
        """S-matrix has full rank 3200."""
        props = verify_s_properties()
        assert props['full_rank'] is True
        assert props['rank'] == 3200

    def test_non_degenerate(self):
        """S-matrix is non-degenerate (modular)."""
        props = verify_s_properties()
        assert props['non_degenerate'] is True

    def test_block_diagonal_structure(self):
        """The S-matrix is block-diagonal with correct block sizes."""
        S = s_matrix()
        # Check that entries outside blocks are zero
        offset = 0
        for _ in range(N_SECTORS_3x3):
            offset += 3
        for _ in range(N_SECTORS_2x2):
            offset += 2

        # Check a cross-block entry (between first 3x3 and second 3x3)
        assert abs(S[0, 3]) < 1e-15
        assert abs(S[1, 4]) < 1e-15

        # Check a cross-block entry (between first 3x3 and first 2x2)
        first_2x2_start = N_SECTORS_3x3 * 3  # 72
        assert abs(S[0, first_2x2_start]) < 1e-15

    def test_ising_block_present(self):
        """The first 3x3 block is the Ising S-matrix."""
        S = s_matrix()
        S_block = S[0:3, 0:3]
        S_ising = ising_s_matrix()
        assert np.allclose(S_block, S_ising, atol=1e-12)


# =========================================================================
# Section 7: Charge-1 sector (8 tests)
# =========================================================================

class TestCharge1Sector:
    """Tests for the charge-1 (24x24) S-matrix."""

    def test_indices_count(self):
        """24 charge-1 indices."""
        indices = charge1_sector_indices()
        assert len(indices) == 24

    def test_indices_are_c1_modules(self):
        """Charge-1 indices correspond to Type C1 modules."""
        indices = charge1_sector_indices()
        modules = enumerate_modules()
        for idx in indices:
            assert modules[idx].module_type == 'C1'

    def test_abelian_shape(self):
        """Abelian charge-1 S-matrix is 24x24."""
        S24 = charge1_s_matrix_abelian()
        assert S24.shape == (24, 24)

    def test_abelian_is_diagonal(self):
        """Abelian charge-1 S-matrix is diagonal."""
        data = charge1_nondegeneracy()
        assert data['is_diagonal'] is True

    def test_abelian_diagonal_value(self):
        """Abelian diagonal entries are 1/2."""
        data = charge1_nondegeneracy()
        assert abs(data['diagonal_value'] - 0.5) < 1e-12

    def test_abelian_full_rank(self):
        """Abelian charge-1 S-matrix has full rank 24."""
        data = charge1_nondegeneracy()
        assert data['full_rank'] is True
        assert data['rank'] == 24

    def test_enhanced_offdiag_nonzero(self):
        """At A_1 enhancement, off-diagonal entry is nonzero."""
        data = charge1_enhanced_a1(merged=(0, 1))
        assert data['offdiag_nonzero'] is True
        assert data['delta_offdiag_abs'] > 0.1

    def test_enhanced_full_rank(self):
        """Enhanced charge-1 S-matrix has full rank 24."""
        data = charge1_enhanced_a1(merged=(0, 1))
        assert data['full_rank'] is True


# =========================================================================
# Section 8: Ising fusion rules (8 tests)
# =========================================================================

class TestIsingFusion:
    """Tests for Ising (sl_2 level-2) fusion rules."""

    def test_shape(self):
        """Fusion tensor is 3x3x3."""
        N = ising_fusion_rules()
        assert N.shape == (3, 3, 3)

    def test_identity(self):
        """V_0 is the identity: N^k_{0j} = delta_{jk}."""
        N = ising_fusion_rules()
        for j in range(3):
            for k in range(3):
                expected = 1 if j == k else 0
                assert N[0, j, k] == expected

    def test_v1_squared(self):
        """V_1 x V_1 = V_0 + V_2 (NON-ABELIAN fusion!)."""
        N = ising_fusion_rules()
        assert N[1, 1, 0] == 1  # V_0 appears
        assert N[1, 1, 1] == 0  # V_1 does not
        assert N[1, 1, 2] == 1  # V_2 appears

    def test_v2_squared(self):
        """V_2 x V_2 = V_0."""
        N = ising_fusion_rules()
        assert N[2, 2, 0] == 1
        assert N[2, 2, 1] == 0
        assert N[2, 2, 2] == 0

    def test_v1_v2(self):
        """V_1 x V_2 = V_1."""
        N = ising_fusion_rules()
        assert N[1, 2, 0] == 0
        assert N[1, 2, 1] == 1
        assert N[1, 2, 2] == 0

    def test_nonneg_integer(self):
        """All fusion coefficients are non-negative integers."""
        N = ising_fusion_rules()
        assert np.all(N >= 0)
        assert np.all(N == N.astype(int))

    def test_symmetric(self):
        """Fusion is commutative: N^k_{ij} = N^k_{ji}."""
        N = ising_fusion_rules()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    assert N[i, j, k] == N[j, i, k]

    def test_sum_d_consistency(self):
        """Verlinde consistency: sum_k N^k_{ij} d_k = d_i * d_j."""
        N = ising_fusion_rules()
        d = [D_V0, D_V1, D_V2]
        for i in range(3):
            for j in range(3):
                lhs = sum(N[i, j, k] * d[k] for k in range(3))
                rhs = d[i] * d[j]
                assert abs(lhs - rhs) < 1e-10, f"Failed for ({i},{j}): {lhs} != {rhs}"


# =========================================================================
# Section 9: N=2 vs N=3 comparison (6 tests)
# =========================================================================

class TestN2N3Comparison:
    """Tests for the comparison between N=2 and N=3."""

    def test_threshold_crossed(self):
        """N=3 crosses the non-abelian threshold."""
        data = n2_n3_comparison()
        assert data['threshold_crossed'] is True

    def test_n2_pointed(self):
        """N=2 is pointed."""
        data = n2_n3_comparison()
        assert data['N2']['is_pointed'] is True

    def test_n3_not_pointed(self):
        """N=3 is NOT pointed."""
        data = n2_n3_comparison()
        assert data['N3']['is_pointed'] is False

    def test_n2_trivial_double_braiding(self):
        """N=2 has trivial double braiding."""
        data = n2_n3_comparison()
        assert abs(data['N2']['q_squared'] - 1.0) < 1e-10

    def test_n3_nontrivial_double_braiding(self):
        """N=3 has nontrivial double braiding."""
        data = n2_n3_comparison()
        assert abs(data['N3']['q_squared'] - 1.0) > 0.1

    def test_module_count_growth(self):
        """N=3 has ~10x more modules than N=2."""
        data = n2_n3_comparison()
        ratio = data['N3']['n_simples'] / data['N2']['n_simples']
        assert ratio > 9.0  # 3200/324 ~ 9.88


# =========================================================================
# Section 10: Full analysis (6 tests)
# =========================================================================

class TestFullAnalysis:
    """Tests for the complete N=3 MTC analysis."""

    def test_runs(self):
        """full_n3_analysis() completes without error."""
        result = full_n3_analysis()
        assert isinstance(result, dict)
        assert 'summary' in result

    def test_status(self):
        """Status is CONJECTURAL."""
        result = full_n3_analysis()
        assert result['status'] == 'CONJECTURAL'

    def test_non_pointed(self):
        """MTC is not pointed."""
        result = full_n3_analysis()
        assert result['is_pointed'] is False

    def test_double_braiding(self):
        """Double braiding is nontrivial."""
        result = full_n3_analysis()
        assert result['double_braiding_nontrivial'] is True

    def test_fusion_nonabelian(self):
        """Fusion is non-abelian."""
        result = full_n3_analysis()
        assert result['fusion_nonabelian'] is True

    def test_s_full_rank(self):
        """S-matrix is full rank."""
        result = full_n3_analysis()
        assert result['s_full_rank'] is True
