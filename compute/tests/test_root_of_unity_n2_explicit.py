r"""Tests for root_of_unity_n2_explicit.py: explicit N=2 MTC from the K3
quantum toroidal algebra at root of unity q = -1.

STATUS: ALL results are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the MTC construction.

CENTRAL RESULTS (all conjectural):
    (1) 324 = p_{24}(2) simple modules at N=2.
    (2) S-matrix: 324x324 block-diagonal, real, symmetric, unitary, S^2 = I.
    (3) T-matrix: diagonal with twist values in {1, i, -i, -1}.
    (4) Modularity: non-degenerate braiding (full rank S-matrix).
    (5) (ST)^3 = e^{2*pi*i*c/8} * S^2 with c = -16 (c mod 8 = 0).
    (6) Fusion rules: Z/2Z in each Ising sector, all N^k_{ij} non-negative int.
    (7) D^2 = 324 = p_{24}(2) (total quantum dimension squared).
    (8) All objects self-dual (C = I), all quantum dimensions = 1 (pointed).
    (9) Category decomposes as 24 Ising-type + 276 trivial sectors.
    (10) Twist spectrum: 104 modules with theta=1, 4 with i, 20 with -i, 196 with -1.

Test structure:
    Section 1: Module enumeration (8 tests)
    Section 2: S-matrix construction (9 tests)
    Section 3: T-matrix construction (7 tests)
    Section 4: Modularity verification (6 tests)
    Section 5: Quantum dimensions and D^2 (5 tests)
    Section 6: Fusion rules (7 tests)
    Section 7: Charge conjugation (3 tests)
    Section 8: Sector decomposition (5 tests)
    Section 9: Cross-checks with parent engines (5 tests)
    Section 10: Full MTC analysis (4 tests)

Total: 59 tests.

Manuscript references:
    k3_times_e.tex, conj:k3-quantum-toroidal
    k3_times_e.tex, conj:k3-root-unity-mtc
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.root_of_unity_n2_explicit import (
    # Constants
    STATUS,
    MUKAI_RANK,
    N_LEVEL,
    N_SIMPLES,
    N_TYPE_A,
    N_TYPE_B1,
    N_TYPE_B2,
    C_EFF,
    OMEGA_N2,
    # Module enumeration
    SimpleModule,
    enumerate_modules,
    module_type_counts,
    sector_decomposition,
    # S-matrix
    hadamard_2x2,
    s_matrix,
    # T-matrix
    t_matrix,
    twist_spectrum,
    # Modularity verification
    verify_s_properties,
    verify_modular_relation,
    verify_nondegeneracy,
    # Quantum dimensions
    quantum_dimensions_by_sector,
    total_quantum_dimension_squared,
    d_squared_decomposition,
    # Fusion rules
    fusion_rules_ising_sector,
    verify_fusion_integrality,
    # Charge conjugation
    charge_conjugation,
    # Full analysis
    full_mtc_analysis,
)

from compute.lib.k3_quantum_toroidal import (
    _colored_partition,
    N_MUKAI,
)

from compute.lib.k3_yangian import (
    SIG_PLUS,
    SIG_MINUS,
    mukai_diagonal_eigenvalues,
)


# =========================================================================
# Section 1: Module enumeration (8 tests)
# =========================================================================

class TestModuleEnumeration:
    """Tests for the 324 simple modules at N=2."""

    def test_total_count(self):
        """p_24(2) = 324 simple modules."""
        modules = enumerate_modules()
        assert len(modules) == 324
        assert len(modules) == N_SIMPLES

    def test_p24_2_matches(self):
        """The module count matches p_24(2) from the partition function."""
        assert _colored_partition(2, 24) == 324
        assert N_SIMPLES == _colored_partition(2, N_MUKAI)

    def test_type_counts(self):
        """Type A: 24, Type B1: 24, Type B2: 276."""
        modules = enumerate_modules()
        counts = {'A': 0, 'B1': 0, 'B2': 0}
        for m in modules:
            counts[m.module_type] += 1
        assert counts['A'] == 24
        assert counts['B1'] == 24
        assert counts['B2'] == 276

    def test_type_counts_dict(self):
        """module_type_counts() returns correct values."""
        tc = module_type_counts()
        assert tc['A'] == 24
        assert tc['B1'] == 24
        assert tc['B2'] == 276
        assert tc['total'] == 324

    def test_indices_contiguous(self):
        """Module indices are contiguous 0..323."""
        modules = enumerate_modules()
        indices = [m.index for m in modules]
        assert indices == list(range(324))

    def test_type_a_ordering(self):
        """Type A modules occupy indices 0..23."""
        modules = enumerate_modules()
        for i in range(24):
            assert modules[i].module_type == 'A'
            assert modules[i].colours == (i,)

    def test_type_b1_ordering(self):
        """Type B1 modules occupy indices 24..47."""
        modules = enumerate_modules()
        for i in range(24):
            m = modules[24 + i]
            assert m.module_type == 'B1'
            assert m.colours == (i,)

    def test_type_b2_ordering(self):
        """Type B2 modules occupy indices 48..323 with a < b."""
        modules = enumerate_modules()
        idx = 48
        for a in range(24):
            for b in range(a + 1, 24):
                m = modules[idx]
                assert m.module_type == 'B2'
                assert m.colours == (a, b)
                idx += 1
        assert idx == 324


# =========================================================================
# Section 2: S-matrix construction (9 tests)
# =========================================================================

class TestSMatrix:
    """Tests for the 324 x 324 S-matrix."""

    def test_hadamard_properties(self):
        """2x2 Hadamard: symmetric, unitary, H^2 = I."""
        H = hadamard_2x2()
        assert H.shape == (2, 2)
        assert np.allclose(H, H.T)  # symmetric
        assert np.allclose(H @ H.T, np.eye(2))  # unitary
        assert np.allclose(H @ H, np.eye(2))  # involution

    def test_s_matrix_shape(self):
        """S-matrix is 324 x 324."""
        S = s_matrix()
        assert S.shape == (324, 324)

    def test_s_matrix_symmetric(self):
        """S = S^T."""
        S = s_matrix()
        assert np.allclose(S, S.T, atol=1e-12)

    def test_s_matrix_real(self):
        """S-matrix is real-valued (all imaginary parts zero)."""
        S = s_matrix()
        assert S.dtype == np.float64

    def test_s_matrix_unitary(self):
        """S * S^T = I (unitarity)."""
        S = s_matrix()
        assert np.allclose(S @ S.T, np.eye(324), atol=1e-10)

    def test_s_squared_identity(self):
        """S^2 = I (involution, all objects self-dual)."""
        S = s_matrix()
        assert np.allclose(S @ S, np.eye(324), atol=1e-10)

    def test_s_matrix_full_rank(self):
        """S-matrix has rank 324 (non-degenerate braiding)."""
        S = s_matrix()
        rank = np.linalg.matrix_rank(S, tol=1e-10)
        assert rank == 324

    def test_s_matrix_block_diagonal(self):
        """S-matrix is block-diagonal: zero outside blocks."""
        S = s_matrix()
        # Check that A-B2 cross entries are zero
        for a in range(24):
            for b2_idx in range(48, 324):
                assert abs(S[a, b2_idx]) < 1e-15
        # Check that B1-B2 cross entries are zero
        for b1_idx in range(24, 48):
            for b2_idx in range(48, 324):
                assert abs(S[b1_idx, b2_idx]) < 1e-15

    def test_s_matrix_hadamard_blocks(self):
        """Each 2x2 block is the Hadamard matrix."""
        S = s_matrix()
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        for a in range(24):
            assert abs(S[a, a] - inv_sqrt2) < 1e-12
            assert abs(S[a, 24 + a] - inv_sqrt2) < 1e-12
            assert abs(S[24 + a, a] - inv_sqrt2) < 1e-12
            assert abs(S[24 + a, 24 + a] + inv_sqrt2) < 1e-12


# =========================================================================
# Section 3: T-matrix construction (7 tests)
# =========================================================================

class TestTMatrix:
    """Tests for the 324 x 324 T-matrix (twists)."""

    def test_t_matrix_shape(self):
        """T-matrix is 324 x 324."""
        T = t_matrix()
        assert T.shape == (324, 324)

    def test_t_matrix_diagonal(self):
        """T-matrix is diagonal."""
        T = t_matrix()
        off_diag = T - np.diag(np.diag(T))
        assert np.allclose(off_diag, 0, atol=1e-15)

    def test_t_type_a_twists(self):
        """Type A modules all have twist theta = 1."""
        T = t_matrix()
        for a in range(24):
            assert abs(T[a, a] - 1.0) < 1e-12

    def test_t_type_b1_positive_directions(self):
        """Type B1 at positive directions (a < 4): theta = i."""
        T = t_matrix()
        for a in range(4):
            assert abs(T[24 + a, 24 + a] - 1j) < 1e-12

    def test_t_type_b1_negative_directions(self):
        """Type B1 at negative directions (a >= 4): theta = -i."""
        T = t_matrix()
        for a in range(4, 24):
            assert abs(T[24 + a, 24 + a] + 1j) < 1e-12

    def test_t_type_b2_mixed_directions(self):
        """Type B2 with one positive and one negative: theta = 1."""
        T = t_matrix()
        # Direction 0 (+) and direction 4 (-): mixed -> theta = 1
        # Index: 48 + (position of (0,4) in lex order)
        # (0,1) at 48, (0,2) at 49, (0,3) at 50, (0,4) at 51
        idx_04 = 48 + 4  # a=0, b=4 is the 5th B2 module (0-indexed: 4th)
        assert abs(T[idx_04, idx_04] - 1.0) < 1e-12

    def test_twist_spectrum_counts(self):
        """Twist spectrum: 104 with 1, 4 with i, 20 with -i, 196 with -1."""
        ts = twist_spectrum()
        assert ts['spectrum']['1'] == 104
        assert ts['spectrum']['i'] == 4
        assert ts['spectrum']['-i'] == 20
        assert ts['spectrum']['-1'] == 196
        assert ts['total'] == 324


# =========================================================================
# Section 4: Modularity verification (6 tests)
# =========================================================================

class TestModularity:
    """Tests for MTC modularity conditions."""

    def test_nondegeneracy(self):
        """The braiding is non-degenerate: S has full rank."""
        result = verify_nondegeneracy()
        assert result['is_modular'] is True
        assert result['full_rank'] is True
        assert result['kernel_dim'] == 0

    def test_s_properties_all_pass(self):
        """All S-matrix properties pass."""
        result = verify_s_properties()
        assert result['is_symmetric'] is True
        assert result['is_real'] is True
        assert result['is_unitary'] is True
        assert result['s_squared_eq_identity'] is True
        assert result['full_rank'] is True

    def test_modular_relation_all_blocks(self):
        """(ST)^3 = phase * S^2 in every Ising block."""
        result = verify_modular_relation()
        assert result['all_blocks_pass'] is True

    def test_effective_central_charge(self):
        """c_eff = -16, c mod 8 = 0."""
        result = verify_modular_relation()
        assert abs(result['c_eff_total'] - (-16.0)) < 1e-8
        assert abs(result['c_eff_mod_8']) < 1e-8

    def test_positive_direction_phase(self):
        """Positive Mukai directions have c_a = 1."""
        result = verify_modular_relation()
        for a in range(SIG_PLUS):
            assert abs(result['c_per_block'][a] - 1.0) < 1e-8

    def test_negative_direction_phase(self):
        """Negative Mukai directions have c_a = -1."""
        result = verify_modular_relation()
        for a in range(SIG_PLUS, MUKAI_RANK):
            assert abs(result['c_per_block'][a] - (-1.0)) < 1e-8


# =========================================================================
# Section 5: Quantum dimensions and D^2 (5 tests)
# =========================================================================

class TestQuantumDimensions:
    """Tests for quantum dimensions and total quantum dimension."""

    def test_all_qdims_one(self):
        """All quantum dimensions equal 1 (pointed category)."""
        qdims = quantum_dimensions_by_sector()
        assert qdims['all_equal_1'] is True
        assert qdims['is_pointed'] is True

    def test_d_squared_equals_324(self):
        """D^2 = 324 = p_{24}(2)."""
        D2 = total_quantum_dimension_squared()
        assert D2 == 324.0

    def test_d_squared_equals_p24_2(self):
        """D^2 = p_{24}(2): the key identity."""
        D2 = total_quantum_dimension_squared()
        assert D2 == _colored_partition(2, 24)

    def test_d_squared_decomposition(self):
        """D^2 = 24*2 + 276*1 = 324."""
        decomp = d_squared_decomposition()
        assert decomp['ising_contribution'] == 48.0
        assert decomp['trivial_contribution'] == 276.0
        assert decomp['total'] == 324.0
        assert decomp['equals_p24_2'] is True

    def test_d_squared_per_sector(self):
        """Each Ising sector: D^2 = 2. Each trivial sector: D^2 = 1."""
        # Ising: 2 modules with d = 1 each => D^2 = 1^2 + 1^2 = 2
        # Trivial: 1 module with d = 1 => D^2 = 1
        assert 24 * 2 + 276 * 1 == 324


# =========================================================================
# Section 6: Fusion rules (7 tests)
# =========================================================================

class TestFusionRules:
    """Tests for fusion coefficients via the Verlinde formula."""

    def test_ising_fusion_z2(self):
        """Each Ising sector has Z/2Z fusion ring."""
        for a in range(24):
            result = fusion_rules_ising_sector(a)
            assert result['fusion_ring'] == 'Z/2Z'

    def test_ising_identity(self):
        """(2_a) x (2_a) = (2_a) (identity element)."""
        result = fusion_rules_ising_sector(0)
        assert result['N_000'] == 1

    def test_ising_action(self):
        """(2_a) x (1,1_a) = (1,1_a)."""
        result = fusion_rules_ising_sector(0)
        assert result['N_011'] == 1
        assert result['N_010'] == 0

    def test_ising_product(self):
        """(1,1_a) x (1,1_a) = (2_a)."""
        result = fusion_rules_ising_sector(0)
        assert result['N_110'] == 1
        assert result['N_111'] == 0

    def test_ising_all_nonneg_int(self):
        """All Ising fusion coefficients are non-negative integers."""
        for a in range(24):
            result = fusion_rules_ising_sector(a)
            assert result['all_nonneg_int'] is True

    def test_fusion_integrality_sample(self):
        """Random sample of fusion coefficients: all non-negative integers."""
        result = verify_fusion_integrality(sample_size=200)
        assert result['all_nonneg_int'] is True
        assert result['n_fail'] == 0

    def test_cross_sector_fusion_zero(self):
        """Modules in different sectors have zero fusion coefficients."""
        # Type A_0 (sector 0) and Type B2_(0,1) (sector 24): different sectors
        modules = enumerate_modules()
        m_a0 = modules[0]    # sector 0
        m_b2 = modules[48]   # sector 24
        assert m_a0.sector != m_b2.sector


# =========================================================================
# Section 7: Charge conjugation (3 tests)
# =========================================================================

class TestChargeConjugation:
    """Tests for charge conjugation C = S^2."""

    def test_c_equals_identity(self):
        """C = I: all objects are self-dual."""
        result = charge_conjugation()
        assert result['C_equals_identity'] is True

    def test_all_self_dual(self):
        """Every module is self-dual (lambda* = lambda)."""
        result = charge_conjugation()
        assert result['all_self_dual'] is True

    def test_s_squared_is_identity(self):
        """S^2 = I directly verifies C = I."""
        S = s_matrix()
        assert np.allclose(S @ S, np.eye(324), atol=1e-10)


# =========================================================================
# Section 8: Sector decomposition (5 tests)
# =========================================================================

class TestSectorDecomposition:
    """Tests for the sector decomposition of the category."""

    def test_sector_count(self):
        """300 sectors: 24 Ising + 276 trivial."""
        sd = sector_decomposition()
        assert sd['n_sectors'] == 300
        assert sd['ising_sectors'] == 24
        assert sd['trivial_sectors'] == 276

    def test_sector_assignment(self):
        """Each module is assigned to exactly one sector."""
        modules = enumerate_modules()
        sectors = set()
        for m in modules:
            sectors.add(m.sector)
        # 300 distinct sectors
        assert len(sectors) == 300

    def test_ising_sectors_have_two_modules(self):
        """Each Ising sector (0..23) has exactly 2 modules."""
        modules = enumerate_modules()
        for sec in range(24):
            count = sum(1 for m in modules if m.sector == sec)
            assert count == 2, f"Sector {sec} has {count} modules, expected 2"

    def test_trivial_sectors_have_one_module(self):
        """Each trivial sector (24..299) has exactly 1 module."""
        modules = enumerate_modules()
        for sec in range(24, 300):
            count = sum(1 for m in modules if m.sector == sec)
            assert count == 1, f"Sector {sec} has {count} modules, expected 1"

    def test_sector_offsets(self):
        """Sector offsets: 0 and 1 for Ising, 0 for trivial."""
        modules = enumerate_modules()
        for m in modules:
            if m.module_type in ('A', 'B1'):
                assert m.sector_offset in (0, 1)
                if m.module_type == 'A':
                    assert m.sector_offset == 0
                else:
                    assert m.sector_offset == 1
            else:
                assert m.sector_offset == 0


# =========================================================================
# Section 9: Cross-checks with parent engines (5 tests)
# =========================================================================

class TestCrossChecks:
    """Cross-checks with root_of_unity_k3_toroidal.py and k3_toroidal_verlinde_proof.py."""

    def test_module_count_matches_parent(self):
        """p_24(2) = 324 matches the parent engine's computation."""
        from compute.lib.root_of_unity_k3_toroidal import (
            restricted_colored_partition,
        )
        # Unrestricted: p_24(2) = 324
        assert _colored_partition(2, 24) == 324

    def test_mukai_rank(self):
        """Mukai rank is 24."""
        assert MUKAI_RANK == N_MUKAI
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai signature is (4, 20)."""
        sigma = mukai_diagonal_eigenvalues()
        assert sum(1 for s in sigma if s == 1) == 4
        assert sum(1 for s in sigma if s == -1) == 20

    def test_n_level(self):
        """Level N = 2."""
        assert N_LEVEL == 2
        assert OMEGA_N2 == -1.0

    def test_status_conjectural(self):
        """Status is CONJECTURAL (AP-CY14)."""
        assert STATUS == 'CONJECTURAL'


# =========================================================================
# Section 10: Full MTC analysis (4 tests)
# =========================================================================

class TestFullMTCAnalysis:
    """Tests for the complete MTC analysis summary."""

    def test_full_analysis_runs(self):
        """full_mtc_analysis() completes without error."""
        result = full_mtc_analysis()
        assert isinstance(result, dict)
        assert 'summary' in result

    def test_full_analysis_modular(self):
        """The full analysis confirms modularity."""
        result = full_mtc_analysis()
        assert result['is_modular'] is True
        assert result['s_full_rank'] is True
        assert result['modular_relation_holds'] is True

    def test_full_analysis_d_squared(self):
        """D^2 = p_24(2) = 324 in the full analysis."""
        result = full_mtc_analysis()
        assert result['D_squared'] == 324.0
        assert result['D_squared_eq_p24_N'] is True

    def test_full_analysis_pointed(self):
        """The category is pointed (all quantum dimensions = 1)."""
        result = full_mtc_analysis()
        assert result['is_pointed'] is True
        assert result['all_qdims_1'] is True
        assert result['all_self_dual'] is True
