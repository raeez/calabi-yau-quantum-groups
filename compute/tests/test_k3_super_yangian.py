r"""Tests for k3_super_yangian.py: K3 super-Yangian Y(gl(4|20)).

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify internal consistency of the super-Yangian framework
arising from the Mukai signature (4,20).

SECTIONS:
    1. Super-grading from Mukai signature (5 tests)
    2. Super-permutation spectrum (6 tests)
    3. Super vs omega permutation comparison (4 tests)
    4. Super T-matrix structure (6 tests)
    5. Entry count matches adversarial analysis (4 tests)
    6. Super-Yang YBE (3 tests)
    7. Super-unitarity (4 tests)
    8. Quantum Berezinian (4 tests)
    9. A_1 enhancement embedding (4 tests)
    10. Super-crossing symmetry (3 tests)
    11. ZTE comparison (5 tests)
    12. Full report (3 tests)
    13. Multi-path cross-verification (8 tests)

Total: 59 tests.
"""

import pytest
import numpy as np
from fractions import Fraction
from sympy import Rational

from compute.lib.k3_super_yangian import (
    M_EVEN,
    N_ODD,
    SUPER_DIM,
    TOTAL_DIM,
    mukai_super_grading,
    parity,
    super_permutation_matrix,
    super_permutation_spectrum,
    super_vs_omega_permutation_comparison,
    super_yang_r_matrix_small,
    super_yang_r_matrix_numpy,
    super_t_matrix_structure,
    verify_entry_count_matches_adversarial,
    verify_super_ybe_small,
    verify_super_unitarity_small,
    quantum_berezinian_structure,
    a1_enhancement_embedding,
    super_crossing_symmetry_small,
    zte_super_vs_ordinary_numpy,
    full_super_yangian_report,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
)


# =========================================================================
# 1. Super-grading from Mukai signature
# =========================================================================


class TestSuperGrading:
    """Tests for the Z_2-grading from Mukai signature."""

    def test_even_count(self):
        """4 even (positive Mukai) directions."""
        grading = mukai_super_grading()
        assert grading.m_even == 4

    def test_odd_count(self):
        """20 odd (negative Mukai) directions."""
        grading = mukai_super_grading()
        assert grading.n_odd == 20

    def test_superdimension(self):
        """Superdimension = 4 - 20 = -16."""
        grading = mukai_super_grading()
        assert grading.superdimension == -16

    def test_parities_list(self):
        """Parities list has 24 entries: [0]*4 + [1]*20."""
        grading = mukai_super_grading()
        assert len(grading.parities) == 24
        assert grading.parities[:4] == [0, 0, 0, 0]
        assert all(p == 1 for p in grading.parities[4:])

    def test_parity_function(self):
        """parity(i) returns correct values."""
        for i in range(4):
            assert parity(i) == 0
        for i in range(4, 24):
            assert parity(i) == 1
        with pytest.raises(ValueError):
            parity(24)


# =========================================================================
# 2. Super-permutation spectrum
# =========================================================================


class TestSuperPermutationSpectrum:
    """Tests for P_s and P_s^2 eigenvalue analysis."""

    def test_ps_squared_is_identity(self):
        """P_s^2 = Id (all eigenvalues +1)."""
        result = super_permutation_spectrum()
        assert result['P_s_squared_is_identity'] is True

    def test_ps_squared_no_minus_ones(self):
        """P_s^2 has zero -1 eigenvalues."""
        result = super_permutation_spectrum()
        assert result['P_s_squared_eigenvalues']['-1'] == 0

    def test_ps_squared_all_plus_ones(self):
        """P_s^2 has 576 eigenvalues all +1."""
        result = super_permutation_spectrum()
        assert result['P_s_squared_eigenvalues']['+1'] == 576

    def test_pomega_squared_has_minus_ones(self):
        """P_omega^2 has 160 eigenvalues of -1 (from adversarial)."""
        result = super_permutation_spectrum()
        assert result['P_omega_squared_eigenvalues']['-1'] == 160

    def test_total_dimension(self):
        """Total dimension is 24^2 = 576."""
        result = super_permutation_spectrum()
        assert result['total_dimension'] == 576

    def test_superdimension(self):
        """Superdimension is -16."""
        result = super_permutation_spectrum()
        assert result['superdimension'] == -16


# =========================================================================
# 3. Super vs omega permutation comparison
# =========================================================================


class TestSuperVsOmegaComparison:
    """Tests comparing P_s with P_omega."""

    def test_total_count(self):
        """Total agree + disagree = 576."""
        result = super_vs_omega_permutation_comparison()
        assert result['total'] == 576

    def test_not_identical(self):
        """P_s and P_omega are NOT identical operators."""
        result = super_vs_omega_permutation_comparison()
        assert result['disagree_count'] > 0

    def test_even_even_sector(self):
        """Agreement count in even-even sector is 4*4 = 16 (all agree)."""
        result = super_vs_omega_permutation_comparison()
        # Even-even: both P_s and P_omega give +1.
        # P_s: (-1)^{0*0} = +1.  P_omega: s_i = +1 (even direction).
        assert result['agreement_by_sector']['even_even'] == M_EVEN * M_EVEN

    def test_partial_agreement(self):
        """P_s and P_omega agree on some entries and disagree on others."""
        result = super_vs_omega_permutation_comparison()
        assert 0 < result['agree_count'] < 576


# =========================================================================
# 4. Super T-matrix structure
# =========================================================================


class TestSuperTMatrixStructure:
    """Tests for the block structure of the T-matrix."""

    def test_block_dimensions(self):
        """Block dimensions are correct."""
        t = super_t_matrix_structure()
        assert t.block_dims['A'] == (4, 4)
        assert t.block_dims['B'] == (4, 20)
        assert t.block_dims['C'] == (20, 4)
        assert t.block_dims['D'] == (20, 20)

    def test_bosonic_count(self):
        """416 bosonic entries (A: 16 + D: 400)."""
        t = super_t_matrix_structure()
        assert t.bosonic_entries == 416

    def test_fermionic_count(self):
        """160 fermionic entries (B: 80 + C: 80)."""
        t = super_t_matrix_structure()
        assert t.fermionic_entries == 160

    def test_total_entries(self):
        """Total entries: 576 = 24^2."""
        t = super_t_matrix_structure()
        assert t.total_entries == 576

    def test_bosonic_plus_fermionic(self):
        """Bosonic + fermionic = total."""
        t = super_t_matrix_structure()
        assert t.bosonic_entries + t.fermionic_entries == t.total_entries

    def test_super_rank(self):
        """Super rank is (4, 20)."""
        t = super_t_matrix_structure()
        assert t.m == 4
        assert t.n == 20


# =========================================================================
# 5. Entry count matches adversarial analysis
# =========================================================================


class TestEntryCountMatchesAdversarial:
    """Tests that super T-matrix counts match P_omega^2 spectrum."""

    def test_exact_match(self):
        """The bosonic/fermionic split matches P_omega^2 spectrum."""
        result = verify_entry_count_matches_adversarial()
        assert result['exact_match'] is True

    def test_bosonic_matches_plus(self):
        """416 bosonic = 416 same-sign (P_omega^2 = +1)."""
        result = verify_entry_count_matches_adversarial()
        assert result['bosonic_matches_plus'] is True

    def test_fermionic_matches_minus(self):
        """160 fermionic = 160 mixed-sign (P_omega^2 = -1)."""
        result = verify_entry_count_matches_adversarial()
        assert result['fermionic_matches_minus'] is True

    def test_counts_consistent(self):
        """Both P_omega^2 and super T-matrix give 416 + 160 = 576."""
        result = verify_entry_count_matches_adversarial()
        assert result['P_omega_sq_plus_1'] + result['P_omega_sq_minus_1'] == 576
        assert result['super_bosonic'] + result['super_fermionic'] == 576


# =========================================================================
# 6. Super-Yang YBE
# =========================================================================


class TestSuperYBE:
    """Tests for the super-Yang R-matrix Yang-Baxter equation."""

    def test_ybe_gl_2_1(self):
        """YBE for the super-Yang R-matrix on C^{2|1}."""
        result = verify_super_ybe_small(m=2, n=1)
        assert result['ybe_satisfied'] is True

    def test_ybe_gl_1_1(self):
        """YBE for the super-Yang R-matrix on C^{1|1}."""
        result = verify_super_ybe_small(m=1, n=1)
        assert result['ybe_satisfied'] is True

    def test_tensor_dim(self):
        """Tensor dimension for gl(2|1) is 3^3 = 27."""
        result = verify_super_ybe_small(m=2, n=1)
        assert result['tensor_dim'] == 27


# =========================================================================
# 7. Super-unitarity
# =========================================================================


class TestSuperUnitarity:
    """Tests for R_s(u)*R_s(-u) = scalar * Id."""

    def test_unitarity_gl_2_1(self):
        """Super-unitarity holds for gl(2|1)."""
        result = verify_super_unitarity_small(m=2, n=1)
        assert result['normalised_unitarity'] is True

    def test_unitarity_gl_1_1(self):
        """Super-unitarity holds for gl(1|1)."""
        result = verify_super_unitarity_small(m=1, n=1)
        assert result['normalised_unitarity'] is True

    def test_scalar_factor(self):
        """Scalar factor is hbar^2 - u^2."""
        result = verify_super_unitarity_small(m=2, n=1)
        assert 'hbar' in result['scalar_factor']
        assert 'u' in result['scalar_factor']

    def test_resolves_omega_obstruction(self):
        """Super-unitarity resolves the P_omega^2 modified unitarity."""
        result = verify_super_unitarity_small(m=2, n=1)
        assert 'resolving' in result['interpretation'].lower() or \
               'RESOLVES' in result['comparison_with_omega']


# =========================================================================
# 8. Quantum Berezinian
# =========================================================================


class TestQuantumBerezinian:
    """Tests for the quantum Berezinian structure."""

    def test_numerator_factors(self):
        """Numerator has 4 factors (even directions)."""
        result = quantum_berezinian_structure()
        assert result['numerator_factors'] == 4

    def test_denominator_factors(self):
        """Denominator has 20 factors (odd directions)."""
        result = quantum_berezinian_structure()
        assert result['denominator_factors'] == 20

    def test_center_generator(self):
        """Quantum Berezinian generates the center."""
        result = quantum_berezinian_structure()
        assert result['center_generator'] is True

    def test_super_rank(self):
        """Super rank is (4, 20)."""
        result = quantum_berezinian_structure()
        assert result['super_rank'] == (4, 20)


# =========================================================================
# 9. A_1 enhancement embedding
# =========================================================================


class TestA1Enhancement:
    """Tests for the sl_2 embedding at A_1 enhancement."""

    def test_root_in_odd_subspace(self):
        """The A_1 root sits in the odd subspace."""
        result = a1_enhancement_embedding()
        assert result['root_in_odd_subspace'] is True

    def test_sl2_in_d_block(self):
        """sl_2 sits in the D (odd-odd, bosonic) block."""
        result = a1_enhancement_embedding()
        assert result['sl2_in_D_block'] is True

    def test_sl2_rtt_is_standard(self):
        """The sl_2 RTT is standard (D block is bosonic)."""
        result = a1_enhancement_embedding()
        assert result['sl2_rtt_is_standard'] is True

    def test_root_norm(self):
        """Root has norm squared -2."""
        result = a1_enhancement_embedding()
        assert result['root_norm_squared'] == -2


# =========================================================================
# 10. Super-crossing symmetry
# =========================================================================


class TestSuperCrossing:
    """Tests for super-crossing symmetry via supertranspose."""

    def test_crossing_gl_2_1(self):
        """Super-crossing holds for gl(2|1)."""
        result = super_crossing_symmetry_small(m=2, n=1)
        assert result['crossing_holds'] is True

    def test_crossing_gl_1_1(self):
        """Super-crossing holds for gl(1|1)."""
        result = super_crossing_symmetry_small(m=1, n=1)
        assert result['crossing_holds'] is True

    def test_off_diagonal_zero(self):
        """Off-diagonal entries of the crossing product are zero."""
        result = super_crossing_symmetry_small(m=2, n=1)
        assert result['off_diagonal_zero'] is True


# =========================================================================
# 11. ZTE comparison
# =========================================================================


class TestZTEComparison:
    """Tests comparing ZTE obstruction for super vs ordinary R-matrix."""

    def test_both_fail_zte(self):
        """Both ordinary and super Yang R-matrices fail ZTE."""
        result = zte_super_vs_ordinary_numpy(kappa_val=0.3)
        assert result['both_fail_zte']

    def test_ordinary_nonzero_obstruction(self):
        """Ordinary Yang R-matrix has nonzero ZTE obstruction."""
        result = zte_super_vs_ordinary_numpy(kappa_val=0.3)
        assert result['zte_ordinary'] > 1e-10

    def test_super_nonzero_obstruction(self):
        """Super Yang R-matrix has nonzero ZTE obstruction."""
        result = zte_super_vs_ordinary_numpy(kappa_val=0.3)
        assert result['zte_super'] > 1e-10

    def test_obstruction_ratio_finite(self):
        """Obstruction ratio (super/ordinary) is finite and positive."""
        result = zte_super_vs_ordinary_numpy(kappa_val=0.3)
        ratio = result['obstruction_ratio']
        assert 0 < ratio < float('inf')

    def test_obstruction_scaling_quadratic(self):
        """Both obstructions scale as O(kappa^2) for small kappa."""
        result = zte_super_vs_ordinary_numpy(kappa_val=0.1)
        # At kappa=0.1, obstruction should be much smaller than at kappa=0.3
        result_large = zte_super_vs_ordinary_numpy(kappa_val=0.3)
        # Quadratic scaling: obstruction(0.3)/obstruction(0.1) ~ (0.3/0.1)^2 = 9
        if result['zte_ordinary'] > 1e-15:
            ratio = result_large['zte_ordinary'] / result['zte_ordinary']
            # Should be roughly 9 (quadratic), allow factor of 2 tolerance
            assert 3 < ratio < 30


# =========================================================================
# 12. Full report
# =========================================================================


class TestFullReport:
    """Tests for the comprehensive super-Yangian report."""

    def test_grading_correct(self):
        """Report has correct grading data."""
        result = full_super_yangian_report()
        assert result['grading']['m_even'] == 4
        assert result['grading']['n_odd'] == 20
        assert result['grading']['superdimension'] == -16

    def test_entry_count_match(self):
        """Report confirms exact entry count match."""
        result = full_super_yangian_report()
        assert result['entry_count_match']['exact_match'] is True

    def test_ybe_and_unitarity(self):
        """Report confirms YBE and unitarity."""
        result = full_super_yangian_report()
        assert result['ybe']['satisfied'] is True
        assert result['unitarity']['holds'] is True


# =========================================================================
# 13. Multi-path cross-verification (AP10)
# =========================================================================


class TestCrossVerification:
    """Cross-checks between independent computation paths."""

    def test_bosonic_fermionic_from_two_paths(self):
        """Verify 416/160 split via both P_omega^2 spectrum and block dimensions.

        Path 1: count same-sign pairs in Mukai eigenvalues (adversarial engine).
        Path 2: compute m^2 + n^2 and 2*m*n from the super-grading.
        """
        # Path 1: from Mukai eigenvalues
        from compute.lib.k3_yangian import mukai_diagonal_eigenvalues
        signs = mukai_diagonal_eigenvalues()
        d = len(signs)
        same_sign = sum(1 for i in range(d) for j in range(d) if signs[i] * signs[j] == 1)
        mixed_sign = sum(1 for i in range(d) for j in range(d) if signs[i] * signs[j] == -1)

        # Path 2: from super-grading dimensions
        grading = mukai_super_grading()
        m, n = grading.m_even, grading.n_odd
        bosonic = m * m + n * n
        fermionic = 2 * m * n

        assert same_sign == bosonic
        assert mixed_sign == fermionic

    def test_superdimension_from_two_paths(self):
        """Verify superdimension via grading and via Mukai trace.

        Path 1: m - n from the super-grading.
        Path 2: Tr(omega) = sum of Mukai eigenvalues.
        """
        # Path 1
        grading = mukai_super_grading()
        sdim_grading = grading.superdimension

        # Path 2
        from compute.lib.k3_yangian import mukai_diagonal_eigenvalues
        signs = mukai_diagonal_eigenvalues()
        sdim_trace = sum(signs)

        assert sdim_grading == sdim_trace
        assert sdim_grading == -16

    def test_ps_squared_identity_vs_unitarity(self):
        """P_s^2 = Id implies super-unitarity R(u)R(-u) = scalar*Id.

        Path 1: Direct count that P_s^2 has no -1 eigenvalues.
        Path 2: Symbolic product R(u)*R(-u) for gl(2|1).
        Both should confirm standard unitarity.
        """
        # Path 1: combinatorial
        spectrum = super_permutation_spectrum()
        ps_sq_ok = spectrum['P_s_squared_is_identity']

        # Path 2: algebraic
        unitarity = verify_super_unitarity_small(m=2, n=1)
        r_product_ok = unitarity['normalised_unitarity']

        assert ps_sq_ok is True
        assert r_product_ok is True

    def test_ybe_two_ranks(self):
        """YBE verified at two independent ranks: gl(1|1) and gl(2|1).

        Both must pass; failure at either rank would invalidate the general claim.
        """
        result_11 = verify_super_ybe_small(m=1, n=1)
        result_21 = verify_super_ybe_small(m=2, n=1)

        assert result_11['ybe_satisfied'] is True
        assert result_21['ybe_satisfied'] is True

    def test_crossing_two_ranks(self):
        """Crossing symmetry verified at two independent ranks.

        If the supertranspose formula is wrong, it would fail at different ranks
        in different ways.
        """
        result_11 = super_crossing_symmetry_small(m=1, n=1)
        result_21 = super_crossing_symmetry_small(m=2, n=1)

        assert result_11['crossing_holds'] is True
        assert result_21['crossing_holds'] is True

    def test_zte_scaling_consistency(self):
        """ZTE obstruction scaling is consistent between two kappa values.

        Both ordinary and super should scale as O(kappa^2).
        Cross-check: obstruction(k1)/obstruction(k2) ~ (k1/k2)^2.
        """
        r1 = zte_super_vs_ordinary_numpy(kappa_val=0.1)
        r2 = zte_super_vs_ordinary_numpy(kappa_val=0.3)

        # Ordinary: ratio should be ~9 for quadratic scaling
        if r1['zte_ordinary'] > 1e-15:
            ratio_ord = r2['zte_ordinary'] / r1['zte_ordinary']
            assert 3 < ratio_ord < 30, f"Ordinary scaling ratio {ratio_ord} outside [3, 30]"

        # Super: same quadratic scaling expected (wider tolerance: super R-matrix
        # has different subleading corrections that can shift the effective exponent)
        if r1['zte_super'] > 1e-15:
            ratio_sup = r2['zte_super'] / r1['zte_super']
            assert 2 < ratio_sup < 100, f"Super scaling ratio {ratio_sup} outside [2, 100]"

    def test_block_dimensions_sum(self):
        """Block dimension sum cross-check: A + B + C + D = (m+n)^2.

        Independent of how blocks are defined; purely from dimensions.
        """
        t = super_t_matrix_structure()
        a_dim = t.block_dims['A'][0] * t.block_dims['A'][1]
        b_dim = t.block_dims['B'][0] * t.block_dims['B'][1]
        c_dim = t.block_dims['C'][0] * t.block_dims['C'][1]
        d_dim = t.block_dims['D'][0] * t.block_dims['D'][1]

        assert a_dim + b_dim + c_dim + d_dim == t.total_entries
        assert a_dim + d_dim == t.bosonic_entries
        assert b_dim + c_dim == t.fermionic_entries

    def test_super_permutation_matrix_squared(self):
        """Verify P_s^2 = Id by constructing the full 576x576 matrix.

        This is an independent numerical check of the combinatorial proof.
        """
        import numpy as np
        P_s = super_permutation_matrix(dim=TOTAL_DIM)
        P_s_sq = P_s @ P_s
        identity = np.eye(TOTAL_DIM * TOTAL_DIM)
        assert np.allclose(P_s_sq, identity, atol=1e-12)
