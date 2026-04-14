r"""Tests for k3_structure_function_explicit.py.

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify INTERNAL CONSISTENCY of the construction, not existence.

CENTRAL RESULTS (all conjectural):
    (1) g_{K3}(u) has degree (24,24) with explicit factored form.
    (2) g(u)*g(-u) = 1 (reflection identity, parameter-independent).
    (3) phi_j = 0 for j even; phi_3 is the first nontrivial OPE coefficient.
    (4) Koszul dual: g^!(u) = 1/g(u), conductor rho_K = 0.
    (5) No single hbar: the K3 R-matrix is diagonal (gl_1).
    (6) Structure function NOT uniquely determined by Mukai pairing (23-dim moduli).
    (7) Signature (4,20) shapes the structure: g_+ * g_- factorization.
    (8) Null parametrization gives g(u) = 1 identically (trivial Yangian).

Test structure:
    Section 1: Explicit structure function (8 tests)
    Section 2: Reflection identity (6 tests)
    Section 3: OPE coefficients phi_j (10 tests)
    Section 4: Koszul dual (6 tests)
    Section 5: R-matrix parameter analysis (5 tests)
    Section 6: Moduli of structure functions (5 tests)
    Section 7: Signature analysis (4 tests)
    Section 8: Special parametrizations (5 tests)
    Section 9: Cross-verification with k3_yangian.py (4 tests)
    Section 10: Full verification (2 tests)

Manuscript references:
    k3_times_e.tex, Conjecture k3-yangian (L2483)
    k3_times_e.tex, Remark k3-yangian-obstruction (L2501)
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.k3_structure_function_explicit import (
    # Explicit form
    explicit_structure_function,
    structure_function_closed_form,
    expanded_polynomials,
    # Reflection identity
    verify_reflection_identity,
    # OPE coefficients
    ope_coefficients_explicit,
    # Koszul dual
    koszul_dual_structure_function,
    # R-matrix
    r_matrix_parameter_analysis,
    # Moduli
    moduli_of_structure_functions,
    # Special parametrizations
    kummer_structure_function_values,
    null_structure_function_values,
    # Signature
    signature_analysis,
    # Full verification
    full_explicit_verification,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    STATUS,
    kummer_k3_parameters,
    null_kummer_parameters,
    custom_parameters,
    structure_function_evaluate,
    structure_function_coefficients,
    newton_power_sums,
    elementary_symmetric_functions,
)

F = Fraction


# =========================================================================
# Section 1: Explicit structure function
# =========================================================================

class TestExplicitStructureFunction:
    """Tests for the explicit factored form of g_{K3}(u)."""

    def test_degree_24_24(self):
        """g_{K3}(u) has degree (24, 24)."""
        esf = explicit_structure_function()
        assert esf.degree == (24, 24)

    def test_g_at_0_is_1(self):
        """g_{K3}(0) = (-1)^{24} = 1."""
        esf = explicit_structure_function()
        assert esf.g_at_0 == 1

    def test_g_at_inf_is_1(self):
        """g_{K3}(infinity) = 1."""
        esf = explicit_structure_function()
        assert esf.g_at_inf == 1

    def test_kummer_has_two_distinct_zeros(self):
        """Kummer parametrization has 2 distinct zeros: 1 (mult 4) and -1/5 (mult 20)."""
        esf = explicit_structure_function()
        assert esf.is_kummer
        zeros = esf.zeros
        assert len(zeros) == 2
        multiplicities = sorted(zeros.values())
        assert multiplicities == [SIG_PLUS, SIG_MINUS]

    def test_kummer_has_two_distinct_poles(self):
        """Kummer parametrization has 2 distinct poles: -1 (mult 4) and 1/5 (mult 20)."""
        esf = explicit_structure_function()
        poles = esf.poles
        assert len(poles) == 2
        multiplicities = sorted(poles.values())
        assert multiplicities == [SIG_PLUS, SIG_MINUS]

    def test_closed_form_data(self):
        """Closed form at Kummer eps=1 gives correct power sums."""
        data = structure_function_closed_form(Rational(1))
        p = data['newton_power_sums']
        assert p[1] == 0  # CY_2
        assert p[2] == Rational(24, 5)  # 4*1 + 20*(1/25) = 4 + 4/5 = 24/5
        assert p[3] == Rational(96, 25)  # 4*1 + 20*(-1/125) = 4 - 4/25 = 96/25

    def test_expanded_polynomials_even_match(self):
        """Numerator and denominator match at even elementary symmetric indices."""
        data = expanded_polynomials(Rational(1))
        assert data['even_e_k_match']

    def test_expanded_polynomials_leading_coefficients(self):
        """Both N(u) and D(u) have leading coefficient 1 (monic)."""
        data = expanded_polynomials(Rational(1))
        assert data['leading_coefficient_N'] == 1
        assert data['leading_coefficient_D'] == 1


# =========================================================================
# Section 2: Reflection identity
# =========================================================================

class TestReflectionIdentity:
    """Tests for g(u)*g(-u) = 1."""

    def test_reflection_kummer(self):
        """g(u)*g(-u) = 1 at Kummer parametrization."""
        result = verify_reflection_identity()
        assert result['all_pass']

    def test_reflection_parameter_independent(self):
        """The reflection identity holds for ANY parameters."""
        result = verify_reflection_identity()
        assert result['parameter_independent']

    def test_reflection_no_cy_needed(self):
        """CY constraint is NOT needed for reflection identity."""
        result = verify_reflection_identity()
        assert not result['cy_constraint_needed']

    def test_reflection_koszul_consequence(self):
        """Reflection gives Koszul dual: g^!(u) = g(-u) = 1/g(u)."""
        result = verify_reflection_identity()
        assert result['consequences']['koszul_dual'] == 'g^!(u) = g(-u) = 1/g(u)'

    def test_reflection_custom_parameters(self):
        """Reflection at non-Kummer parameters."""
        # AP-CY28: parameters chosen with poles far from test points.
        h_list = (
            [Rational(3), Rational(2), Rational(-1), Rational(-4)]
            + [Rational(0)] * 20
        )
        params = custom_parameters(h_list)
        # Test at points far from poles at +/-3, +/-2, +/-1, +/-4
        result = verify_reflection_identity(
            params,
            test_points=[Rational(7), Rational(11), Rational(13)]
        )
        assert result['all_pass']

    def test_reflection_numerical_exact(self):
        """Exact rational arithmetic gives product = 1 (not approximate)."""
        params = kummer_k3_parameters()
        u_val = Rational(17, 4)  # AP-CY28: far from poles at -1, 1/5
        g_u = structure_function_evaluate(u_val, params)
        g_neg_u = structure_function_evaluate(-u_val, params)
        assert g_u * g_neg_u == 1  # Exact equality, not approximate


# =========================================================================
# Section 3: OPE coefficients phi_j
# =========================================================================

class TestOPECoefficients:
    """Tests for the OPE coefficients phi_j."""

    def test_phi_0_is_1(self):
        """phi_0 = 1 (normalization)."""
        ope = ope_coefficients_explicit()
        assert ope['coefficients'][0] == 1

    def test_phi_1_is_0(self):
        """phi_1 = 0 (CY_2 constraint: p_1 = 0)."""
        ope = ope_coefficients_explicit()
        assert ope['coefficients'][1] == 0

    def test_phi_2_is_0(self):
        """phi_2 = 0 (even coefficients vanish)."""
        ope = ope_coefficients_explicit()
        assert ope['coefficients'][2] == 0

    def test_phi_3_nonzero(self):
        """phi_3 is the first nontrivial OPE coefficient."""
        ope = ope_coefficients_explicit()
        assert ope['coefficients'][3] != 0

    def test_phi_3_explicit_value(self):
        """phi_3 = (-2/3)*p_3 = (-2/3)*(96/25) = -64/25 at Kummer eps=1."""
        ope = ope_coefficients_explicit()
        expected = Rational(-2, 3) * Rational(96, 25)
        assert expected == Rational(-64, 25)
        assert ope['coefficients'][3] == expected

    def test_log_even_vanish(self):
        """Log coefficients alpha_k = 0 for all even k."""
        ope = ope_coefficients_explicit(max_order=12)
        assert ope['log_even_vanish']

    def test_initial_vanishing(self):
        """phi_1 = phi_2 = phi_4 = 0 (initial vanishing pattern)."""
        ope = ope_coefficients_explicit(max_order=12)
        assert ope['initial_vanishing']

    def test_phi_5_from_formula(self):
        """phi_5 = alpha_5 (since phi_2 = 0, only alpha_5 contributes)."""
        ope = ope_coefficients_explicit()
        assert ope['derivations']['phi_5']['matches']

    def test_phi_6_nonzero(self):
        """phi_6 = alpha_3^2/2 != 0 (even phi can be nonzero for j >= 6)."""
        ope = ope_coefficients_explicit()
        assert ope['derivations']['phi_6']['matches']
        assert ope['coefficients'][6] == Rational(2048, 625)

    def test_phi_7_from_formula(self):
        """phi_7 = alpha_7 (since phi_4 = phi_2 = 0)."""
        ope = ope_coefficients_explicit()
        assert ope['derivations']['phi_7']['matches']

    def test_power_sums_correct(self):
        """Newton power sums p_k are computed correctly."""
        ope = ope_coefficients_explicit()
        p = ope['power_sums']
        assert p[1] == 0  # CY_2
        assert p[2] == Rational(24, 5)
        assert p[3] == Rational(96, 25)

    def test_phi_4_vanishes_but_phi_6_does_not(self):
        """phi_4 = 0 but phi_6 != 0 (products of odd log terms)."""
        ope = ope_coefficients_explicit()
        assert ope['coefficients'][4] == 0
        assert ope['coefficients'][6] != 0


# =========================================================================
# Section 4: Koszul dual
# =========================================================================

class TestKoszulDual:
    """Tests for the Koszul dual structure function g^!(u) = 1/g(u)."""

    def test_koszul_is_reciprocal(self):
        """g^!(u) = 1/g(u) verified numerically."""
        result = koszul_dual_structure_function()
        for check in result['reciprocal_checks']:
            assert check['is_reciprocal']

    def test_koszul_conductor_is_zero(self):
        """Koszul conductor rho_K = 0 for K3 Heisenberg (class G)."""
        result = koszul_dual_structure_function()
        assert result['koszul_conductor']['value'] == 0

    def test_koszul_odd_sign_flip(self):
        """phi^!_j = -phi_j for odd j."""
        result = koszul_dual_structure_function()
        assert result['odd_sign_flip_verified']

    def test_koszul_phi3_negated(self):
        """phi^!_3 = -phi_3."""
        result = koszul_dual_structure_function()
        phi_3 = result['koszul_coefficients'][3]
        # phi^!_3 should be -(phi_3 of original)
        params = kummer_k3_parameters()
        original_phi = structure_function_coefficients(params, max_order=3)
        assert phi_3 == -original_phi[3]

    def test_koszul_even_phi_unchanged(self):
        """phi^!_j = phi_j for even j (unchanged under Koszul duality)."""
        result = koszul_dual_structure_function()
        coeffs = result['koszul_coefficients']
        params = kummer_k3_parameters()
        original_phi = structure_function_coefficients(params, max_order=len(coeffs) - 1)
        for j in range(0, len(coeffs), 2):
            assert coeffs[j] == original_phi[j], f"Mismatch at even j={j}"

    def test_koszul_not_flop(self):
        """AP-CY10: Koszul duality != birational flop."""
        result = koszul_dual_structure_function()
        assert 'Flop preserves kappa_ch' in result['ap_cy10_reminder']


# =========================================================================
# Section 5: R-matrix parameter analysis
# =========================================================================

class TestRMatrixParameter:
    """Tests for the R-matrix coupling parameter."""

    def test_no_single_hbar(self):
        """The K3 R-matrix has no single hbar (diagonal, gl_1)."""
        result = r_matrix_parameter_analysis()
        assert result['no_single_hbar']

    def test_e1_vanishes(self):
        """e_1 = sum h_i = 0 (CY_2 constraint)."""
        result = r_matrix_parameter_analysis()
        assert result['collective_parameters']['e_1'] == 0

    def test_e2_computed(self):
        """e_2 = sum_{i<j} h_i h_j is computed correctly for Kummer."""
        result = r_matrix_parameter_analysis()
        e2 = result['collective_parameters']['e_2']
        # Independently: e_2 = binom(4,2)*1*1 + 4*20*1*(-1/5) + binom(20,2)*(-1/5)*(-1/5)
        # = 6 + 80*(-1/5) + 190*(1/25)
        # = 6 - 16 + 190/25
        # = 6 - 16 + 38/5
        # = -10 + 38/5 = -50/5 + 38/5 = -12/5
        assert e2 == Rational(-12, 5)

    def test_classical_r_matrix_trace_zero(self):
        """Trace of classical r-matrix is 0 (from CY_2)."""
        result = r_matrix_parameter_analysis()
        assert result['classical_r_matrix']['trace_is_zero']

    def test_full_product_e24(self):
        """Full product h_1*...*h_{24} computed."""
        result = r_matrix_parameter_analysis()
        h_product = result['collective_parameters']['h_product (e_24)']
        # h_product = 1^4 * (-1/5)^{20} = (1/5)^{20} = 1/5^{20}
        expected = Rational(1, 5**20)
        assert h_product == expected


# =========================================================================
# Section 6: Moduli of structure functions
# =========================================================================

class TestModuli:
    """Tests for the moduli space of structure functions."""

    def test_not_uniquely_determined(self):
        """g(u) is NOT uniquely determined by the Mukai pairing."""
        result = moduli_of_structure_functions()
        assert not result['uniquely_determined']

    def test_moduli_dimension_23(self):
        """Moduli space is 23-dimensional (24 params - 1 CY_2 constraint)."""
        result = moduli_of_structure_functions()
        assert result['moduli_space']['dimension'] == 23

    def test_different_eps_gives_different_g(self):
        """Different eps values give different structure functions."""
        result = moduli_of_structure_functions()
        assert result['non_uniqueness_demonstration']['all_different']

    def test_degree_determined_by_mukai(self):
        """The degree 24 IS determined by the Mukai rank."""
        result = moduli_of_structure_functions()
        assert result['determined_by_mukai_pairing']['degree'] == 24

    def test_cy_constraint_determined(self):
        """The CY_2 constraint IS determined by the Mukai pairing."""
        result = moduli_of_structure_functions()
        assert result['determined_by_mukai_pairing']['cy_constraint'] == 'sum h_i = 0'


# =========================================================================
# Section 7: Signature analysis
# =========================================================================

class TestSignatureAnalysis:
    """Tests for the signature (4,20) analysis."""

    def test_cy2_by_blocks(self):
        """CY_2 holds: positive block sum + negative block sum = 0."""
        result = signature_analysis()
        assert result['cy2_constraint_by_block']['is_zero']

    def test_positive_block_count(self):
        """4 positive Mukai directions."""
        result = signature_analysis()
        assert result['positive_parameters']['count'] == SIG_PLUS

    def test_negative_block_count(self):
        """20 negative Mukai directions."""
        result = signature_analysis()
        assert result['negative_parameters']['count'] == SIG_MINUS

    def test_factorization_consistent(self):
        """g(u) = g_+(u) * g_-(u) at test point."""
        result = signature_analysis()
        assert result['factorization_at_u_2']['product_check']


# =========================================================================
# Section 8: Special parametrizations
# =========================================================================

class TestSpecialParametrizations:
    """Tests for Kummer and null parametrizations."""

    def test_kummer_g_at_0(self):
        """Kummer g(0) = 1."""
        data = kummer_structure_function_values()
        assert data['g_at_0'] == '1'

    def test_kummer_phi3_value(self):
        """Kummer phi_3 = -64/25."""
        data = kummer_structure_function_values()
        assert data['ope_coefficients'][3] == Rational(-64, 25)

    def test_kummer_p2_value(self):
        """Kummer p_2 = 24/5."""
        data = kummer_structure_function_values()
        assert data['power_sums'][2] == Rational(24, 5)

    def test_null_g_is_1(self):
        """Null parametrization gives g(u) = 1 identically."""
        data = null_structure_function_values()
        assert data['g_is_identically_1']
        assert data['all_phi_vanish']

    def test_null_is_undeformed(self):
        """Null parametrization is the classical (unquantized) limit."""
        data = null_structure_function_values()
        assert 'undeformed' in data['interpretation']


# =========================================================================
# Section 9: Cross-verification with k3_yangian.py
# =========================================================================

class TestCrossVerification:
    """Cross-checks with the parent k3_yangian.py module."""

    def test_phi_coefficients_match(self):
        """OPE coefficients match k3_yangian.structure_function_coefficients."""
        params = kummer_k3_parameters()
        phi_from_parent = structure_function_coefficients(params, max_order=8)
        ope = ope_coefficients_explicit(params, max_order=8)
        for j in range(9):
            assert ope['coefficients'][j] == phi_from_parent[j], f"Mismatch at phi_{j}"

    def test_power_sums_match(self):
        """Power sums match k3_yangian.newton_power_sums."""
        params = kummer_k3_parameters()
        p_from_parent = newton_power_sums(params, max_k=8)
        ope = ope_coefficients_explicit(params, max_order=8)
        for k in range(1, 9):
            assert ope['power_sums'][k] == p_from_parent[k], f"Mismatch at p_{k}"

    def test_e_functions_match(self):
        """Elementary symmetric functions match k3_yangian.elementary_symmetric_functions."""
        params = kummer_k3_parameters()
        e_from_parent = elementary_symmetric_functions(params, max_k=6)
        data = structure_function_closed_form(Rational(1))
        for k in range(7):
            assert data['elementary_symmetric'][k] == e_from_parent[k], f"Mismatch at e_{k}"

    def test_evaluation_consistency(self):
        """Direct evaluation matches g computed from phi coefficients."""
        params = kummer_k3_parameters()
        u_val = Rational(3)
        g_direct = structure_function_evaluate(u_val, params)
        # Also compute from factored form
        g_factored = Rational(1)
        for hi in params.h:
            g_factored *= (u_val - hi) / (u_val + hi)
        assert g_direct == g_factored


# =========================================================================
# Section 10: Full verification
# =========================================================================

class TestFullVerification:
    """Full verification suite."""

    def test_all_checks_pass(self):
        """All internal consistency checks pass."""
        result = full_explicit_verification()
        assert result['all_checks_pass']

    def test_conjectural_status(self):
        """Status is CONJECTURAL (AP-CY14)."""
        result = full_explicit_verification()
        assert result['status'] == 'CONJECTURAL'
