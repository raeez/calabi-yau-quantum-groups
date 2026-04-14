r"""Tests for mukai_indefinite_yangian.py: signature (4,20) decomposition.

CENTRAL QUESTION: Does the Yangian construction work for INDEFINITE inner
products (Mukai pairing of signature (4,20))?

ANSWER: YES.  The tests verify:
    (1)  Sector decomposition: V_+ (dim 4, k=+1) + V_- (dim 20, k=-1)
    (2)  Cross-sector vanishing: [V_+, V_-] = 0 in diagonal basis
    (3)  Negative-level Heisenberg H_- at k=-1 is well-defined
    (4)  Fock space has indefinite Shapovalov form: signature (4,20) at level 1
    (5)  R-matrix formula is signature-independent
    (6)  Coproduct is algebraic (no inner product needed)
    (7)  Unitarity g(z)*g(-z)=1 per sector
    (8)  Structure function factorises: g = g_+ * g_-
    (9)  Effective level Psi_eff = Tr(omega) = -16 (nonzero)
    (10) Positive sub-Yangian Y(H_+) is genuine (standard positive-definite)
    (11) Negative sub-Yangian Y(H_-)_{k=-1} exists (k != 0 suffices)
    (12) Mukai-twisted permutation P_omega^2 != Id for mixed-sign pairs
    (13) Coproduct factorises across sectors
    (14) GSO projection analogue controls indefiniteness

STATUS: The WELL-DEFINEDNESS results are PROVED (for abelian gl_1 with
diagonal Mukai pairing).  The K3 Yangian itself remains CONJECTURAL (AP-CY14).

Test structure:
    Section 1: Sector decomposition (7 tests)
    Section 2: Negative-level Heisenberg (6 tests)
    Section 3: R-matrix signature independence (5 tests)
    Section 4: Coproduct well-definedness (4 tests)
    Section 5: Sector unitarity (5 tests)
    Section 6: Structure function factorisation (5 tests)
    Section 7: Effective level (5 tests)
    Section 8: Shapovalov form (5 tests)
    Section 9: Sub-Yangians (6 tests)
    Section 10: Mukai-twisted permutation (4 tests)
    Section 11: Full verification (3 tests)

Manuscript references:
    k3_times_e.tex, subsec:k3-yangian
    k3_times_e.tex, Conjecture conj:k3-yangian
    k3_times_e.tex, Remark rem:k3-yangian-obstruction
    k3_times_e.tex, Proposition prop:mukai-indefinite-yangian
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.mukai_indefinite_yangian import (
    # Constants
    POSITIVE_DIM,
    NEGATIVE_DIM,
    TOTAL_DIM,
    POSITIVE_LEVEL,
    NEGATIVE_LEVEL,
    EFFECTIVE_LEVEL,
    # Sector decomposition
    sector_decomposition,
    positive_sector_parameters,
    negative_sector_parameters,
    sector_structure_functions,
    sector_unitarity,
    # Negative-level Heisenberg
    negative_level_heisenberg,
    shapovalov_form_level_n,
    # R-matrix
    r_matrix_signature_independence,
    mukai_twisted_permutation,
    # Coproduct
    coproduct_well_definedness,
    coproduct_sector_factorisation,
    # Sub-Yangians
    positive_sub_yangian,
    negative_sub_yangian,
    # Mixed sector
    mixed_sector_vanishing,
    # Effective level
    effective_level_analysis,
    # GSO
    gso_analogue,
    # Verification
    verify_sector_decomposition,
    verify_negative_heisenberg,
    verify_r_matrix_independence,
    verify_coproduct,
    verify_mixed_sector,
    verify_sector_unitarity_all,
    verify_sector_factorisation,
    verify_effective_level,
    verify_shapovalov_level1,
    verify_positive_sub_yangian,
    verify_negative_sub_yangian,
    full_verification,
)

from compute.lib.k3_yangian import (
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
)

F = Fraction


# =========================================================================
# Section 1: Sector decomposition (7 tests)
# =========================================================================

class TestSectorDecomposition:
    """Tests for the Mukai signature sector decomposition."""

    def test_dimensions(self):
        """V_+ has dim 4, V_- has dim 20, total 24."""
        sd = sector_decomposition()
        assert sd.positive_dim == 4
        assert sd.negative_dim == 20
        assert sd.total_dim == 24
        assert sd.positive_dim + sd.negative_dim == sd.total_dim

    def test_levels(self):
        """Positive sector level +1, negative sector level -1."""
        sd = sector_decomposition()
        assert sd.positive_level == 1
        assert sd.negative_level == -1

    def test_effective_level(self):
        """Effective level Psi_eff = 4*(+1) + 20*(-1) = -16."""
        sd = sector_decomposition()
        assert sd.effective_level == -16
        assert sd.effective_level == (
            sd.positive_dim * sd.positive_level +
            sd.negative_dim * sd.negative_level
        )

    def test_cross_sector_vanishes(self):
        """No mixing between positive and negative sectors."""
        sd = sector_decomposition()
        assert sd.cross_sector_vanishes is True

    def test_positive_parameters_count(self):
        """Positive sector has 4 parameters."""
        h_pos = positive_sector_parameters()
        assert len(h_pos) == 4

    def test_negative_parameters_count(self):
        """Negative sector has 20 parameters."""
        h_neg = negative_sector_parameters()
        assert len(h_neg) == 20

    def test_parameter_union_is_full(self):
        """Positive + negative parameters = full 24 parameters."""
        params = kummer_k3_parameters()
        h_pos = positive_sector_parameters(params)
        h_neg = negative_sector_parameters(params)
        assert len(h_pos) + len(h_neg) == 24
        assert h_pos + h_neg == list(params.h)


# =========================================================================
# Section 2: Negative-level Heisenberg (6 tests)
# =========================================================================

class TestNegativeLevelHeisenberg:
    """Tests for the negative-level Heisenberg algebra."""

    def test_well_defined(self):
        """Heisenberg at k = -1 is well-defined (k != 0)."""
        nh = negative_level_heisenberg()
        assert nh.is_well_defined is True
        assert nh.level == -1
        assert nh.level != 0  # The key condition

    def test_rank(self):
        """Negative Heisenberg has rank 20."""
        nh = negative_level_heisenberg()
        assert nh.rank == 20

    def test_central_charge(self):
        """Central charge c = 20 (one boson per direction)."""
        nh = negative_level_heisenberg()
        assert nh.central_charge == 20

    def test_fock_indefinite(self):
        """Fock space has indefinite inner product."""
        nh = negative_level_heisenberg()
        assert 'indefinite' in nh.fock_inner_product

    def test_shapovalov_level1_all_negative(self):
        """At level 1, all 20 states have negative norm."""
        nh = negative_level_heisenberg()
        assert nh.shapovalov_signature_level1 == (0, 20)

    def test_level_enters_through_sigma2(self):
        """The level k enters through sigma_2 = -k."""
        nh = negative_level_heisenberg()
        sigma_2 = -nh.level  # sigma_2 = -k = -(-1) = 1
        assert sigma_2 == 1
        assert sigma_2 != 0  # Non-degenerate


# =========================================================================
# Section 3: R-matrix signature independence (5 tests)
# =========================================================================

class TestRMatrixIndependence:
    """Tests for R-matrix signature independence."""

    def test_formula_independent(self):
        """R-matrix formula (z-h)/(z+h) does not involve Mukai sign."""
        result = r_matrix_signature_independence()
        assert result['formula_is_signature_independent'] is True

    def test_entries_computed(self):
        """R-matrix entries are computed for sample directions."""
        result = r_matrix_signature_independence()
        entries = result['r_matrix_entries_sample']
        assert len(entries) == 6
        # First 4 are positive, next 2 are negative Mukai directions
        assert entries[0]['mukai_sign'] == 1
        assert entries[4]['mukai_sign'] == -1

    def test_signature_not_in_formula(self):
        """The formula list correctly identifies what is signature-independent."""
        result = r_matrix_signature_independence()
        independent_items = result['where_signature_does_NOT_enter']
        assert 'R-matrix formula (z-h)/(z+h)' in independent_items
        assert 'Yang-Baxter equation' in independent_items
        assert any('Unitarity' in item for item in independent_items)

    def test_signature_enters_elsewhere(self):
        """Signature enters through Mukai norm, effective level, Shapovalov."""
        result = r_matrix_signature_independence()
        dependent_items = result['where_signature_enters']
        assert any('Mukai norm' in item for item in dependent_items)
        assert any('Effective level' in item for item in dependent_items)
        assert any('Shapovalov' in item for item in dependent_items)

    def test_positive_negative_same_formula(self):
        """R-matrix entries for positive and negative directions use same formula."""
        result = r_matrix_signature_independence()
        entries = result['r_matrix_entries_sample']
        # For Kummer K3: h_pos = 1, h_neg = -1/5
        # R(3) for h=1: (3-1)/(3+1) = 2/4 = 1/2
        # R(3) for h=-1/5: (3-(-1/5))/(3+(-1/5)) = (16/5)/(14/5) = 16/14 = 8/7
        pos_entry = entries[0]['R_ii(z_test)']
        neg_entry = entries[4]['R_ii(z_test)']
        # Both are valid rational numbers; different values but same formula
        assert pos_entry == Rational(1, 2)  # (3-1)/(3+1)
        assert neg_entry == Rational(8, 7)  # (3+1/5)/(3-1/5) = (16/5)/(14/5)


# =========================================================================
# Section 4: Coproduct well-definedness (4 tests)
# =========================================================================

class TestCoproductWellDefinedness:
    """Tests for coproduct well-definedness on indefinite Fock space."""

    def test_coproduct_well_defined(self):
        """Drinfeld coproduct is well-defined (algebraic, no inner product)."""
        result = coproduct_well_definedness()
        assert result['coproduct_well_defined'] is True

    def test_no_inner_product_needed(self):
        """Coproduct does not require inner product."""
        result = coproduct_well_definedness()
        no_ip = result['what_does_NOT_require_inner_product']
        assert 'Coproduct formula Delta_z' in no_ip
        assert 'Coassociativity' in no_ip

    def test_inner_product_for_unitarity_only(self):
        """Inner product needed only for representation-theoretic unitarity."""
        result = coproduct_well_definedness()
        needs_ip = result['what_requires_inner_product']
        assert any('Unitarity of representations' in item for item in needs_ip)
        assert any('Hermiticity' in item for item in needs_ip)

    def test_coproduct_sector_factorisation(self):
        """Coproduct factorises across Mukai sectors."""
        result = coproduct_sector_factorisation()
        assert result['coproduct_factorises'] is True
        assert result['generator_sets_disjoint'] is True
        assert result['structure_function_factorises'] is True


# =========================================================================
# Section 5: Sector unitarity (5 tests)
# =========================================================================

class TestSectorUnitarity:
    """Tests for per-sector unitarity g(z)*g(-z) = 1."""

    def test_positive_sector_unitary(self):
        """g_+(z) * g_+(-z) = 1."""
        result = sector_unitarity()
        assert result['positive_sector_unitary'] is True

    def test_negative_sector_unitary(self):
        """g_-(z) * g_-(-z) = 1."""
        result = sector_unitarity()
        assert result['negative_sector_unitary'] is True

    def test_multiple_test_points(self):
        """Unitarity verified at multiple test points."""
        result = sector_unitarity()
        assert len(result['positive_checks']) >= 3
        assert len(result['negative_checks']) >= 3

    def test_unitarity_direct_positive(self):
        """Direct computation: g_+(3) * g_+(-3) = 1."""
        params = kummer_k3_parameters()
        h_pos = positive_sector_parameters(params)
        z = Rational(3)
        g_z = Rational(1)
        g_neg_z = Rational(1)
        for hi in h_pos:
            g_z *= (z - hi) / (z + hi)
            g_neg_z *= (-z - hi) / (-z + hi)
        assert g_z * g_neg_z == 1

    def test_unitarity_direct_negative(self):
        """Direct computation: g_-(3) * g_-(-3) = 1."""
        params = kummer_k3_parameters()
        h_neg = negative_sector_parameters(params)
        z = Rational(3)
        g_z = Rational(1)
        g_neg_z = Rational(1)
        for hi in h_neg:
            g_z *= (z - hi) / (z + hi)
            g_neg_z *= (-z - hi) / (-z + hi)
        assert g_z * g_neg_z == 1


# =========================================================================
# Section 6: Structure function factorisation (5 tests)
# =========================================================================

class TestStructureFunctionFactorisation:
    """Tests for g_{K3} = g_+ * g_-."""

    def test_factorisation_at_z3(self):
        """g_{K3}(3) = g_+(3) * g_-(3)."""
        sf = sector_structure_functions(Rational(3))
        assert sf['product_equals_full'] is True

    def test_factorisation_at_z7(self):
        """g_{K3}(7) = g_+(7) * g_-(7)."""
        sf = sector_structure_functions(Rational(7))
        assert sf['product_equals_full'] is True

    def test_factorisation_at_z11_3(self):
        """g_{K3}(11/3) = g_+(11/3) * g_-(11/3)."""
        sf = sector_structure_functions(Rational(11, 3))
        assert sf['product_equals_full'] is True

    def test_positive_sector_degree(self):
        """Positive sector structure function has degree (4,4)."""
        h_pos = positive_sector_parameters()
        assert len(h_pos) == 4  # 4 zeros and 4 poles

    def test_negative_sector_degree(self):
        """Negative sector structure function has degree (20,20)."""
        h_neg = negative_sector_parameters()
        assert len(h_neg) == 20  # 20 zeros and 20 poles


# =========================================================================
# Section 7: Effective level (5 tests)
# =========================================================================

class TestEffectiveLevel:
    """Tests for the effective level Psi_eff = Tr(omega) = -16."""

    def test_effective_level_value(self):
        """Psi_eff = 4 - 20 = -16."""
        result = effective_level_analysis()
        assert result['effective_level'] == -16

    def test_effective_level_nonzero(self):
        """Psi_eff != 0 (Sugawara construction is well-defined)."""
        result = effective_level_analysis()
        assert result['is_nonzero'] is True

    def test_central_charge_24(self):
        """Central charge c = 24 (signature-independent)."""
        result = effective_level_analysis()
        assert result['central_charge'] == 24

    def test_miura_coefficient(self):
        """Miura cross-term (Psi-1)/Psi = 17/16."""
        result = effective_level_analysis()
        assert result['miura_cross_term_coefficient'] == '17/16'

    def test_constant_values(self):
        """Module constants match expected values."""
        assert EFFECTIVE_LEVEL == -16
        assert POSITIVE_DIM == 4
        assert NEGATIVE_DIM == 20
        assert TOTAL_DIM == 24


# =========================================================================
# Section 8: Shapovalov form (5 tests)
# =========================================================================

class TestShapovalovForm:
    """Tests for the Shapovalov form on the indefinite Fock space."""

    def test_level0_vacuum(self):
        """Level 0: vacuum |0> has positive norm."""
        result = shapovalov_form_level_n(0)
        assert result['num_states'] == 1
        assert result['signature'] == (1, 0)
        assert result['is_positive_definite'] is True

    def test_level1_signature(self):
        """Level 1: signature matches Mukai (4, 20)."""
        result = shapovalov_form_level_n(1)
        assert result['num_states'] == 24
        assert result['signature'] == (4, 20)
        assert result['is_positive_definite'] is False

    def test_level2_states(self):
        """Level 2: correct state count."""
        result = shapovalov_form_level_n(2)
        # 24 single-oscillator + C(25,2) = 300 double-oscillator = 324 total
        assert result['single_oscillator_states'] == 24
        assert result['double_oscillator_states'] == 300
        assert result['is_positive_definite'] is False

    def test_level2_single_oscillator_signature(self):
        """Level 2 single-oscillator block: signature (4, 20)."""
        result = shapovalov_form_level_n(2)
        assert result['single_oscillator_signature'] == (4, 20)

    def test_higher_level_indefinite(self):
        """All levels >= 1 have indefinite Shapovalov form."""
        for n in [1, 2, 3]:
            result = shapovalov_form_level_n(n)
            assert result['is_positive_definite'] is False


# =========================================================================
# Section 9: Sub-Yangians (6 tests)
# =========================================================================

class TestSubYangians:
    """Tests for the positive and negative sub-Yangians."""

    def test_positive_genuine(self):
        """Positive sub-Yangian is a genuine Yangian."""
        result = positive_sub_yangian()
        assert result['is_genuine_yangian'] is True

    def test_positive_rank(self):
        """Positive sub-Yangian has rank 4."""
        result = positive_sub_yangian()
        assert result['rank'] == 4

    def test_positive_fock_definite(self):
        """Positive sector Fock space is positive-definite."""
        result = positive_sub_yangian()
        assert result['fock_inner_product'] == 'positive-definite'

    def test_negative_well_defined(self):
        """Negative sub-Yangian Y(H_-)_{k=-1} is well-defined."""
        result = negative_sub_yangian()
        assert result['is_well_defined'] is True

    def test_negative_rank(self):
        """Negative sub-Yangian has rank 20."""
        result = negative_sub_yangian()
        assert result['rank'] == 20

    def test_negative_sigma2(self):
        """Negative sector: sigma_2 = -k = 1 (nonzero, well-defined)."""
        result = negative_sub_yangian()
        assert result['sigma_2_value'] == 1


# =========================================================================
# Section 10: Mukai-twisted permutation (4 tests)
# =========================================================================

class TestMukaiTwistedPermutation:
    """Tests for the Mukai-twisted permutation operator."""

    def test_ordinary_p_squared_is_id(self):
        """Ordinary permutation P^2 = Id."""
        result = mukai_twisted_permutation(rank=4)
        assert result['p_squared_is_identity'] is True

    def test_p_omega_squared_formula(self):
        """P_omega^2 diagonal matches s_i * s_j formula."""
        result = mukai_twisted_permutation(rank=4)
        assert result['p_omega_squared_matches_formula'] is True

    def test_p_omega_not_involution_for_indefinite(self):
        """For signature (4,0) at rank 4: P_omega IS an involution.
        For mixed signature: P_omega is NOT an involution."""
        result = mukai_twisted_permutation(rank=6)
        # rank 6 with sig_plus = min(4,6) = 4, sig_minus = 2
        # Has mixed signs, so P_omega^2 != Id on mixed pairs
        assert result['p_omega_is_involution'] is False

    def test_p_omega_squared_mixed_sign(self):
        """P_omega^2 has -1 entries for mixed-sign index pairs."""
        result = mukai_twisted_permutation(rank=6)
        diag = result['p_omega_squared_diagonal']
        # For rank 6 with signs [+1,+1,+1,+1,-1,-1]:
        # (i=0,j=4): s_0*s_4 = (+1)(-1) = -1
        # The diagonal list is [s_i*s_j for i,j in range(6)]
        # Position (0,4) = 0*6+4 = 4th entry
        assert diag[4] == -1  # s_0 * s_4 = +1 * -1 = -1


# =========================================================================
# Section 11: Full verification (3 tests)
# =========================================================================

class TestFullVerification:
    """Integration tests for the full verification suite."""

    def test_full_verification_runs(self):
        """Full verification suite completes without error."""
        result = full_verification()
        assert isinstance(result, dict)
        assert len(result) == 11  # 11 verification paths

    def test_all_paths_pass(self):
        """All 11 verification paths pass."""
        result = full_verification()
        for path_name, path_result in result.items():
            for check_name, check_value in path_result.items():
                if isinstance(check_value, bool):
                    assert check_value, f"FAILED: {path_name}.{check_name}"

    def test_gso_analogue(self):
        """GSO analogue confirms indefiniteness is controlled."""
        result = gso_analogue()
        assert result['has_indefinite_inner_product'] is True
        assert result['is_pathological'] is False
        assert len(result['control_mechanisms']) >= 4


# =========================================================================
# Section 12: Cross-verification with existing engines (5 tests)
# =========================================================================

class TestCrossVerification:
    """Cross-verification with k3_yangian.py and k3_double_current_algebra.py."""

    def test_full_unitarity_matches_sector_product(self):
        """g(z)*g(-z) = 1 for the full function matches sector-by-sector."""
        params = kummer_k3_parameters()
        z = Rational(3)
        g_full = structure_function_evaluate(z, params)
        g_full_neg = structure_function_evaluate(-z, params)
        assert g_full * g_full_neg == 1

        sf = sector_structure_functions(z, params)
        g_product = sf['g_plus'] * sf['g_minus']
        assert g_product == g_full

    def test_effective_level_from_eigenvalues(self):
        """Psi_eff computed from eigenvalues matches EFFECTIVE_LEVEL constant."""
        from compute.lib.k3_yangian import mukai_diagonal_eigenvalues
        eigenvalues = mukai_diagonal_eigenvalues()
        psi_eff = sum(eigenvalues)
        assert psi_eff == EFFECTIVE_LEVEL
        assert psi_eff == -16

    def test_sector_dims_match_k3_constants(self):
        """Sector dimensions match k3_double_current_algebra constants."""
        from compute.lib.k3_double_current_algebra import (
            MUKAI_RANK, MUKAI_SIG_PLUS, MUKAI_SIG_MINUS,
        )
        assert POSITIVE_DIM == MUKAI_SIG_PLUS
        assert NEGATIVE_DIM == MUKAI_SIG_MINUS
        assert TOTAL_DIM == MUKAI_RANK

    def test_null_parameters_both_sectors(self):
        """Null Kummer parameters involve both positive and negative sectors."""
        params = null_kummer_parameters()
        h_pos = positive_sector_parameters(params)
        h_neg = negative_sector_parameters(params)
        # Null params: h_1=eps, h_2=-eps, h_5=eps, h_6=-eps, rest 0
        # Positive sector (indices 0-3): h_0=eps, h_1=-eps, h_2=0, h_3=0
        assert h_pos[0] != 0  # epsilon
        assert h_pos[1] != 0  # -epsilon
        # Negative sector (indices 4-23): h_4=eps, h_5=-eps, rest 0
        assert h_neg[0] != 0  # epsilon (index 4 in full array)
        assert h_neg[1] != 0  # -epsilon (index 5 in full array)

    def test_mixed_sector_agrees_with_drinfeld_center(self):
        """Cross-sector vanishing is consistent with Drinfeld center engine."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            r_matrix_on_fock_modules,
        )
        # In the diagonal basis, orthogonal directions have zero R-matrix exponent
        lam = [1, 0, 0, 0] + [0] * 20  # pure positive direction
        mu = [0, 0, 0, 0] + [1] + [0] * 19  # pure negative direction
        exp = r_matrix_on_fock_modules(lam, mu)
        assert exp == 0  # Orthogonal: no braiding between sectors
