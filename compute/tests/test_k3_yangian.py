r"""Tests for k3_yangian.py: K3 Yangian Y(g_{K3}) for gl_1.

STATUS: ALL results in this module are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the construction, not its existence.

CENTRAL RESULTS (all conjectural):
    (1) The 24 parameters h_i satisfy sum h_i = 0 (CY_2 constraint).
    (2) g_{K3}(z) = prod (z-h_i)/(z+h_i) has degree (24,24).
    (3) g_{K3}(z) * g_{K3}(-z) = 1 (unitarity).
    (4) R_{K3}(z) is 24x24 diagonal for gl_1 (abelian).
    (5) Bar Euler product = eta(q)^{24}/q = Delta(q)/q (Ramanujan tau).
    (6) YBE is automatic for diagonal R-matrices.
    (7) Classical limit: R -> I + omega^{-1}/z + O(z^{-2}).

Test structure:
    Section 1: Parameters h_i (6 tests)
    Section 2: Structure function g_{K3}(z) (10 tests)
    Section 3: Unitarity (5 tests)
    Section 4: R-matrix (8 tests)
    Section 5: Yangian presentation (4 tests)
    Section 6: Bar Euler product (7 tests)
    Section 7: Comparison with C^3 (4 tests)
    Section 8: Elementary symmetric functions (3 tests)
    Section 9: Cross-verification with Drinfeld center (3 tests)
    Section 10: Full verification (2 tests)

Manuscript references:
    k3_times_e.tex, Definition k3-double-current-algebra (L1165)
    cy_to_chiral.tex, Conjecture cy-a-3 (K3 Yangian as quantization)
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, cancel

from compute.lib.k3_yangian import (
    # Constants
    STATUS,
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    # Parameters
    mukai_diagonal_eigenvalues,
    kummer_k3_parameters,
    null_kummer_parameters,
    custom_parameters,
    MukaiLatticeParams,
    # Structure function
    structure_function_symbolic,
    structure_function_evaluate,
    structure_function_log_coefficients,
    structure_function_coefficients,
    newton_power_sums,
    # Unitarity
    verify_unitarity_algebraic,
    verify_unitarity_from_log,
    # R-matrix
    r_matrix_charge_1,
    r_matrix_diagonal_entries,
    r_matrix_classical_limit,
    verify_ybe_diagonal,
    # Presentation
    yangian_presentation,
    # Bar Euler
    bar_euler_product_yangian,
    verify_bar_euler_matches_classical,
    verify_bar_euler_eta24,
    # Comparison
    compare_with_c3_yangian,
    # Special values and symmetry
    structure_function_special_values,
    structure_function_symmetry_properties,
    # Elementary symmetric
    elementary_symmetric_functions,
    # Verification
    verify_cy2_constraint,
    verify_structure_function_degree,
    verify_r_matrix_charge_1,
    full_verification,
)

from compute.lib.k3_double_current_algebra import (
    K3_TOTAL_DIM,
    MUKAI_RANK,
    MUKAI_SIG_PLUS,
    MUKAI_SIG_MINUS,
    bar_euler_generating_function,
)

F = Fraction


# =========================================================================
# Section 1: Parameters h_i
# =========================================================================

class TestParameters:
    """Tests for the 24 Yangian parameters h_i."""

    def test_num_params_is_24(self):
        """The K3 Yangian has 24 parameters (= Mukai rank)."""
        assert NUM_PARAMS == 24
        assert NUM_PARAMS == MUKAI_RANK

    def test_signature_matches_mukai(self):
        """Signature (4,20) matches the Mukai lattice."""
        assert SIG_PLUS == 4
        assert SIG_MINUS == 20
        assert SIG_PLUS == MUKAI_SIG_PLUS
        assert SIG_MINUS == MUKAI_SIG_MINUS

    def test_mukai_eigenvalues(self):
        """Diagonal Mukai eigenvalues: 4 positive, 20 negative."""
        eigs = mukai_diagonal_eigenvalues()
        assert len(eigs) == 24
        assert sum(1 for e in eigs if e == 1) == 4
        assert sum(1 for e in eigs if e == -1) == 20

    def test_kummer_cy2_constraint(self):
        """Kummer K3 parameters satisfy sum h_i = 0."""
        params = kummer_k3_parameters()
        assert params.cy2_sum == 0
        assert len(params.h) == 24
        assert params.signature == (4, 20)

    def test_kummer_parameters_nondegenerate(self):
        """Kummer parameters are all nonzero (nondegeneracy)."""
        params = kummer_k3_parameters()
        assert all(h != 0 for h in params.h)

    def test_custom_parameters_cy2(self):
        """Custom parameters must satisfy CY_2 constraint."""
        h_list = [Rational(1)] * 4 + [Rational(-1, 5)] * 20
        params = custom_parameters(h_list)
        assert params.cy2_sum == 0

    def test_custom_parameters_wrong_length_raises(self):
        """Custom parameters with wrong length raises ValueError."""
        with pytest.raises(ValueError, match="Need 24"):
            custom_parameters([Rational(1)] * 10)

    def test_custom_parameters_cy2_violation_raises(self):
        """Custom parameters violating CY_2 raises ValueError."""
        with pytest.raises(ValueError, match="CY_2 constraint"):
            custom_parameters([Rational(1)] * 24)

    def test_kummer_mukai_norm(self):
        """Kummer K3 Mukai norm is computed correctly."""
        params = kummer_k3_parameters()
        # 4 * 1^2 * (+1) + 20 * (1/5)^2 * (-1) = 4 - 20/25 = 4 - 4/5 = 16/5
        expected = Rational(16, 5)
        assert params.mukai_norm_sq == expected
        assert not params.is_null

    def test_null_parameters_are_null(self):
        """Null parameters have <h,h>_Muk = 0 and sum h_i = 0."""
        params = null_kummer_parameters()
        assert params.is_null
        assert params.mukai_norm_sq == 0
        assert params.cy2_sum == 0

    def test_null_parameters_unitarity(self):
        """Unitarity g(z)*g(-z) = 1 holds for null parameters too."""
        params = null_kummer_parameters()
        for z_val in [Rational(2), Rational(7, 3)]:
            g_z = structure_function_evaluate(z_val, params)
            g_neg_z = structure_function_evaluate(-z_val, params)
            assert g_z * g_neg_z == 1


# =========================================================================
# Section 2: Structure function g_{K3}(z)
# =========================================================================

class TestStructureFunction:
    """Tests for the K3 structure function g_{K3}(z)."""

    def test_degree_24_24(self):
        """g_{K3}(z) is a degree-(24,24) rational function."""
        result = verify_structure_function_degree()
        assert result['numerator_degree'] == 24
        assert result['denominator_degree'] == 24

    def test_phi_0_is_1(self):
        """phi_0 = 1 (leading coefficient of g(z) at z = infinity)."""
        phi = structure_function_coefficients(max_order=4)
        assert phi[0] == Rational(1)

    def test_phi_1_is_0(self):
        """phi_1 = 0 (CY_2 constraint: sum h_i = 0 => p_1 = 0)."""
        phi = structure_function_coefficients(max_order=4)
        assert phi[1] == Rational(0)

    def test_phi_2_is_0(self):
        """phi_2 = 0 (only odd log-coefficients contribute at order 2)."""
        phi = structure_function_coefficients(max_order=4)
        assert phi[2] == Rational(0)

    def test_phi_3_nonzero(self):
        """phi_3 is the first nonzero coefficient (from p_3)."""
        phi = structure_function_coefficients(max_order=4)
        assert phi[3] != Rational(0)

    def test_g_at_zero_is_1(self):
        """g_{K3}(0) = (-1)^{24} = 1 (even number of parameters)."""
        g_0 = structure_function_evaluate(Rational(0))
        assert g_0 == 1

    def test_g_at_large_z_approaches_1(self):
        """g_{K3}(z) -> 1 as z -> infinity (verified at z = 1000)."""
        g_large = structure_function_evaluate(Rational(1000))
        # Should be close to 1
        assert abs(float(g_large) - 1.0) < 0.01

    def test_newton_p1_vanishes(self):
        """p_1 = sum h_i = 0 (CY_2 constraint)."""
        p = newton_power_sums(max_k=4)
        assert p[1] == 0

    def test_newton_p2_nonzero(self):
        """p_2 = sum h_i^2 > 0 for nontrivial parameters."""
        p = newton_power_sums(max_k=4)
        assert p[2] != 0

    def test_log_coefficients_even_vanish(self):
        """Even log-expansion coefficients vanish (odd parity of log g)."""
        alphas = structure_function_log_coefficients(max_order=10)
        for k in range(0, 11, 2):
            assert alphas[k] == 0, f"alpha_{k} = {alphas[k]} should be 0"


# =========================================================================
# Section 3: Unitarity g(z)*g(-z) = 1
# =========================================================================

class TestUnitarity:
    """Tests for the unitarity identity g(z)*g(-z) = 1."""

    def test_unitarity_algebraic(self):
        """Algebraic verification of g(z)*g(-z) = 1."""
        result = verify_unitarity_algebraic()
        assert result['unitarity_holds']
        assert result['all_numerical_pass']

    def test_unitarity_from_log(self):
        """Unitarity from odd parity of log g(z)."""
        result = verify_unitarity_from_log()
        assert result['even_log_coefficients_zero']
        assert result['unitarity_from_odd_parity']

    def test_unitarity_numerical_specific_point(self):
        """g(3)*g(-3) = 1 for Kummer K3 parameters."""
        params = kummer_k3_parameters()
        g_3 = structure_function_evaluate(Rational(3), params)
        g_neg3 = structure_function_evaluate(Rational(-3), params)
        assert g_3 * g_neg3 == 1

    def test_unitarity_multiple_points(self):
        """g(z)*g(-z) = 1 at multiple test points (avoiding poles at z = +/-h_i)."""
        params = kummer_k3_parameters()
        # Kummer params: h_i = 1 (i=1..4), h_i = -1/5 (i=5..24).
        # Poles at z = -h_i, i.e. z = -1 and z = 1/5.  Avoid these.
        for z_val in [Rational(2), Rational(3), Rational(5), Rational(7, 3)]:
            g_z = structure_function_evaluate(z_val, params)
            g_neg_z = structure_function_evaluate(-z_val, params)
            assert g_z * g_neg_z == 1, f"Failed at z = {z_val}"

    def test_unitarity_custom_parameters(self):
        """Unitarity holds for arbitrary CY_2-satisfying parameters."""
        h_list = (
            [Rational(3), Rational(-1), Rational(2), Rational(-4)]
            + [Rational(0)] * 20
        )
        params = custom_parameters(h_list)
        for z_val in [Rational(5), Rational(7)]:
            g_z = structure_function_evaluate(z_val, params)
            g_neg_z = structure_function_evaluate(-z_val, params)
            assert g_z * g_neg_z == 1


# =========================================================================
# Section 4: R-matrix
# =========================================================================

class TestRMatrix:
    """Tests for the R-matrix R_{K3}(z) at charge 1."""

    def test_r_matrix_dimension_24(self):
        """R-matrix at charge 1 is 24x24."""
        r_data = r_matrix_charge_1()
        assert r_data.dimension == 24

    def test_r_matrix_is_diagonal(self):
        """R-matrix is diagonal for abelian gl_1."""
        r_data = r_matrix_charge_1()
        assert r_data.is_diagonal

    def test_r_matrix_entries_count(self):
        """R-matrix has 24 diagonal entries."""
        r_data = r_matrix_charge_1()
        assert len(r_data.entries) == 24

    def test_r_matrix_unitarity(self):
        """R(z)*R(-z) = I_{24} (diagonal unitarity)."""
        params = kummer_k3_parameters()
        entries_z = r_matrix_diagonal_entries(Rational(2), params)
        entries_neg_z = r_matrix_diagonal_entries(Rational(-2), params)
        for i in range(24):
            assert entries_z[i] * entries_neg_z[i] == 1

    def test_r_matrix_classical_limit_trace_zero(self):
        """Classical r-matrix has zero trace (from CY_2 constraint)."""
        cl = r_matrix_classical_limit()
        assert cl['trace_is_zero']

    def test_r_matrix_classical_limit_values(self):
        """Classical r-matrix diagonal entries are -2*h_i."""
        params = kummer_k3_parameters()
        cl = r_matrix_classical_limit(params)
        for i in range(24):
            assert cl['r_diagonal'][i] == -2 * params.h[i]

    def test_ybe_diagonal(self):
        """YBE holds (trivially) for diagonal R-matrices."""
        result = verify_ybe_diagonal()
        assert result['ybe_holds']
        assert result['is_abelian_case']

    def test_r_matrix_approaches_identity(self):
        """R(z) -> I as z -> infinity: each entry -> 1."""
        entries = r_matrix_diagonal_entries(Rational(10000))
        for i, entry in enumerate(entries):
            assert abs(float(entry) - 1.0) < 0.001, f"Entry {i}: {entry}"


# =========================================================================
# Section 5: Yangian presentation
# =========================================================================

class TestYangianPresentation:
    """Tests for the conjectural Yangian presentation."""

    def test_num_current_families(self):
        """24 current families (one per Mukai direction)."""
        pres = yangian_presentation()
        assert pres.num_current_families == 24

    def test_cartan_type_heisenberg(self):
        """Cartan type is Heisenberg (abelian gl_1)."""
        pres = yangian_presentation()
        assert 'Heisenberg' in pres.cartan_type

    def test_structure_function_degree_in_presentation(self):
        """Structure function degree matches parameters."""
        pres = yangian_presentation()
        assert pres.structure_function_degree == 24

    def test_conjectural_status(self):
        """Presentation is marked CONJECTURAL (AP-CY14)."""
        pres = yangian_presentation()
        assert pres.status == 'CONJECTURAL'
        assert STATUS == 'CONJECTURAL'


# =========================================================================
# Section 6: Bar Euler product
# =========================================================================

class TestBarEuler:
    """Tests for the bar Euler product = eta(q)^{24}/q."""

    def test_coefficient_q0_is_1(self):
        """Coefficient of q^0 in prod(1-q^n)^{24} is 1."""
        coeffs = bar_euler_product_yangian(5)
        assert coeffs[0] == 1

    def test_coefficient_q1_is_neg24(self):
        """Coefficient of q^1 is -24 (= -rank of Mukai lattice)."""
        coeffs = bar_euler_product_yangian(5)
        assert coeffs[1] == -24

    def test_coefficient_q2_is_252(self):
        """Coefficient of q^2 is 252 = C(24,2) - 24 + ... ."""
        coeffs = bar_euler_product_yangian(5)
        assert coeffs[2] == 252

    def test_ramanujan_tau_match(self):
        """Coefficients match Ramanujan tau function."""
        result = verify_bar_euler_eta24(8)
        assert result['all_match']

    def test_bar_euler_matches_classical(self):
        """Yangian bar Euler = classical bar Euler (flat deformation)."""
        result = verify_bar_euler_matches_classical(8)
        assert result['yangian_equals_classical']
        assert result['known_eta24_match']

    def test_bar_euler_cross_check_with_dca(self):
        """Cross-check with k3_double_current_algebra bar Euler."""
        yangian_coeffs = bar_euler_product_yangian(8)
        classical_coeffs = bar_euler_generating_function(8)
        for d in range(9):
            assert yangian_coeffs.get(d, 0) == classical_coeffs.get(d, 0), \
                f"Mismatch at degree {d}"

    def test_known_tau_values(self):
        """Verify against tabulated Ramanujan tau values."""
        coeffs = bar_euler_product_yangian(8)
        # prod(1-q^n)^{24} = sum tau(n+1) q^n
        tau = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
               6: -6048, 7: -16744, 8: 84480, 9: -113643}
        for n_plus_1, tau_val in tau.items():
            n = n_plus_1 - 1
            if n <= 8:
                assert coeffs.get(n, 0) == tau_val, \
                    f"tau({n_plus_1}): expected {tau_val}, got {coeffs.get(n, 0)}"


# =========================================================================
# Section 7: Comparison with C^3
# =========================================================================

class TestC3Comparison:
    """Tests comparing Y(g_{K3}) with Y(gl_hat_1)."""

    def test_c3_has_3_params(self):
        """C^3 Yangian has 3 parameters vs K3's 24."""
        cmp = compare_with_c3_yangian()
        assert cmp['c3']['num_params'] == 3
        assert cmp['k3']['num_params'] == 24

    def test_k3_bar_euler_is_eta24(self):
        """K3 bar Euler is eta^{24} (constant exponent), not MacMahon."""
        cmp = compare_with_c3_yangian()
        assert 'eta^{24}' in cmp['k3']['bar_euler']
        assert 'MacMahon' in cmp['c3']['bar_euler']

    def test_k3_is_class_G(self):
        """K3 Heisenberg Yangian is class G, not M."""
        cmp = compare_with_c3_yangian()
        assert 'G' in cmp['k3']['shadow_class']
        assert 'M' in cmp['c3']['shadow_class']

    def test_unitarity_holds_for_both(self):
        """Unitarity g(z)*g(-z) = 1 holds for both C^3 and K3."""
        cmp = compare_with_c3_yangian()
        assert 'g(z)*g(-z) = 1' in cmp['structural_analogy']


# =========================================================================
# Section 8: Elementary symmetric functions
# =========================================================================

class TestElementarySymmetric:
    """Tests for elementary symmetric functions of the h_i."""

    def test_e0_is_1(self):
        """e_0 = 1 (convention)."""
        e = elementary_symmetric_functions(max_k=4)
        assert e[0] == 1

    def test_e1_is_0(self):
        """e_1 = sum h_i = 0 (CY_2 constraint)."""
        e = elementary_symmetric_functions(max_k=4)
        assert e[1] == 0

    def test_e2_nonzero(self):
        """e_2 is nonzero for nontrivial parameters."""
        e = elementary_symmetric_functions(max_k=4)
        assert e[2] != 0


# =========================================================================
# Section 9: Cross-verification with Drinfeld center
# =========================================================================

class TestDrinfeldCenterCrossCheck:
    """Cross-verification with drinfeld_center_k3_heisenberg.py."""

    def test_mukai_rank_consistency(self):
        """Mukai rank 24 consistent across modules."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            DRINFELD_DOUBLE_DIM,
            DRINFELD_DOUBLE_GENERATORS,
        )
        assert NUM_PARAMS == MUKAI_RANK
        assert DRINFELD_DOUBLE_GENERATORS == 2 * NUM_PARAMS  # 48
        assert DRINFELD_DOUBLE_DIM == 2 * NUM_PARAMS + 1  # 49

    def test_signature_consistency(self):
        """Mukai signature (4,20) consistent across modules."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            r_matrix_drinfeld_center,
        )
        r_data = r_matrix_drinfeld_center()
        assert r_data.pairing_signature == (SIG_PLUS, SIG_MINUS)
        assert r_data.pairing_signature == (4, 20)

    def test_quantization_status_consistent(self):
        """Quantization status is CONJECTURAL in both modules."""
        from compute.lib.drinfeld_center_k3_heisenberg import (
            quantization_conjectural,
        )
        q = quantization_conjectural()
        assert q.status == STATUS  # Both 'CONJECTURAL'


# =========================================================================
# Section 10: Multi-path cross-verification (AP10 compliance)
# =========================================================================

class TestMultiPathCrossVerification:
    """Cross-verify values through independent computation paths.

    AP10 requires that key quantities be verified by computing the SAME
    value through two or more independent methods and checking agreement.
    """

    def test_phi_1_zero_two_paths(self):
        """phi_1 = 0: Path A (series expansion) vs Path B (Newton p_1 = 0).

        Path A: compute phi_1 from the recursion phi_j = (1/j) sum k*alpha_k*phi_{j-k}.
        Path B: phi_1 = alpha_1 = (-2/1)*p_1 = -2*sum(h_i) = 0 by CY_2.
        """
        params = kummer_k3_parameters()

        # Path A: series expansion
        phi = structure_function_coefficients(params, max_order=4)
        phi_1_path_a = phi[1]

        # Path B: direct Newton sum
        p = newton_power_sums(params, max_k=1)
        phi_1_path_b = Rational(-2) * p[1]  # alpha_1 = -2*p_1/1

        assert phi_1_path_a == phi_1_path_b == 0

    def test_phi_3_two_paths(self):
        """phi_3: Path A (recursion) vs Path B (direct: -2*p_3/3).

        phi_3 = alpha_3 = (-2/3) * p_3 where p_3 = sum h_i^3.
        This holds because alpha_1 = alpha_2 = 0, so the recursion
        3*phi_3 = 3*alpha_3*phi_0 = 3*alpha_3, giving phi_3 = alpha_3.
        """
        params = kummer_k3_parameters()

        # Path A: from full coefficient recursion
        phi = structure_function_coefficients(params, max_order=4)
        phi_3_path_a = phi[3]

        # Path B: direct Newton power sum
        p = newton_power_sums(params, max_k=3)
        phi_3_path_b = Rational(-2, 3) * p[3]

        assert phi_3_path_a == phi_3_path_b
        assert phi_3_path_a != 0  # nontrivial

    def test_g_at_zero_two_paths(self):
        """g(0) = 1: Path A (direct evaluation) vs Path B (parity argument).

        Path A: evaluate prod(-h_i / h_i) = prod(-1) = (-1)^24 = 1.
        Path B: g(0) = (-1)^N where N = num_params = 24 (even).
        """
        params = kummer_k3_parameters()

        # Path A: direct evaluation via structure_function_evaluate
        g_0_path_a = structure_function_evaluate(Rational(0), params)

        # Path B: parity count
        g_0_path_b = (-1)**len(params.h)

        assert g_0_path_a == g_0_path_b == 1

    def test_unitarity_two_proofs(self):
        """g(z)*g(-z) = 1: Path A (factor-by-factor) vs Path B (log parity).

        Path A: each (z-h)/(z+h) * (z+h)/(z-h) = 1.
        Path B: log g has only odd powers => log g(-z) = -log g(z) => product = 1.
        """
        result_a = verify_unitarity_algebraic()
        result_b = verify_unitarity_from_log()

        assert result_a['unitarity_holds']
        assert result_b['unitarity_from_odd_parity']

        # Both paths independently confirm the same identity
        assert result_a['unitarity_holds'] == result_b['unitarity_from_odd_parity']

    def test_e1_from_esf_vs_direct_sum(self):
        """e_1 = 0: Path A (Newton-to-esf recursion) vs Path B (direct sum of h_i).

        Path A: elementary_symmetric_functions computes e_1 via Newton identities.
        Path B: params.cy2_sum = sum h_i directly.
        """
        params = kummer_k3_parameters()

        # Path A: via Newton identity recursion
        e = elementary_symmetric_functions(params, max_k=2)
        e1_path_a = e[1]

        # Path B: direct parameter sum
        e1_path_b = params.cy2_sum

        assert e1_path_a == e1_path_b == 0

    def test_classical_r_matrix_trace_two_paths(self):
        """Tr(r) = 0: Path A (from classical limit) vs Path B (from CY_2).

        Path A: Tr(r) = sum(-2*h_i) = -2*sum(h_i), computed by r_matrix_classical_limit.
        Path B: -2 * cy2_sum = -2 * 0 = 0, computed from CY_2 constraint.
        """
        params = kummer_k3_parameters()

        # Path A: classical limit computation
        cl = r_matrix_classical_limit(params)
        trace_path_a = cl['trace_r']

        # Path B: from CY_2 constraint
        trace_path_b = Rational(-2) * params.cy2_sum

        assert trace_path_a == trace_path_b == 0

    def test_bar_euler_q1_two_paths(self):
        """Coefficient of q^1 = -24: Path A (bar Euler product) vs Path B (-rank).

        Path A: direct expansion of prod(1-q^n)^{24} gives coefficient of q^1.
        Path B: the q^1 coefficient of prod(1-q^n)^r equals -r (first factor only).
        Only (1-q)^{24} contributes to q^1, giving C(24,1)*(-1)^1 = -24.
        """
        # Path A: from bar Euler product engine
        coeffs = bar_euler_product_yangian(5)
        q1_path_a = coeffs[1]

        # Path B: from combinatorial argument
        # Coefficient of q^1 in prod(1-q^n)^{24} = coefficient of q^1 in (1-q)^{24}
        # = C(24,1) * (-1)^1 = -24
        import math
        q1_path_b = math.comb(24, 1) * (-1)

        assert q1_path_a == q1_path_b == -24

    def test_bar_euler_q2_two_paths(self):
        """Coefficient of q^2 = 252: Path A (product expansion) vs Path B (combinatorial).

        Path B: q^2 contributions from prod(1-q^n)^{24}:
          From (1-q)^{24}: C(24,2)*(-1)^2 = 276
          From (1-q^2)^{24}: C(24,1)*(-1)^1 = -24
          Total: 276 - 24 = 252.
        """
        # Path A: from bar Euler product engine
        coeffs = bar_euler_product_yangian(5)
        q2_path_a = coeffs[2]

        # Path B: combinatorial decomposition
        import math
        from_q1_factor = math.comb(24, 2)  # choosing 2 copies of q from (1-q)^24
        from_q2_factor = math.comb(24, 1) * (-1)  # one copy of q^2 from (1-q^2)^24
        q2_path_b = from_q1_factor + from_q2_factor  # 276 - 24 = 252

        assert q2_path_a == q2_path_b == 252

    def test_r_matrix_unitarity_vs_structure_fn_unitarity(self):
        """R-matrix unitarity R(z)R(-z)=I is equivalent to g(z)*g(-z)=1.

        Path A: check diagonal R entries satisfy R_ii(z)*R_ii(-z) = 1.
        Path B: check structure function g_i(z)*g_i(-z) = 1 for each i.
        Both should agree because R_ii(z) = g_i(z) = (z-h_i)/(z+h_i).
        """
        params = kummer_k3_parameters()
        z_val = Rational(3)

        # Path A: R-matrix diagonal entries
        entries_z = r_matrix_diagonal_entries(z_val, params)
        entries_neg_z = r_matrix_diagonal_entries(-z_val, params)
        unitarity_a = [entries_z[i] * entries_neg_z[i] for i in range(NUM_PARAMS)]

        # Path B: individual structure function factors
        unitarity_b = []
        for hi in params.h:
            gi_z = (z_val - hi) / (z_val + hi)
            gi_neg_z = (-z_val - hi) / (-z_val + hi)
            unitarity_b.append(gi_z * gi_neg_z)

        for i in range(NUM_PARAMS):
            assert unitarity_a[i] == 1, f"R-matrix unitarity failed at i={i}"
            assert unitarity_b[i] == 1, f"Structure fn unitarity failed at i={i}"
            assert unitarity_a[i] == unitarity_b[i]

    def test_bar_euler_yangian_vs_dca_full_range(self):
        """Bar Euler coefficients: Path A (Yangian) vs Path B (classical DCA).

        The Yangian deformation is flat, so both must agree to all orders.
        Verify through degree 10 (11 independent coefficient checks).
        """
        yangian_coeffs = bar_euler_product_yangian(10)
        classical_coeffs = bar_euler_generating_function(10)

        for d in range(11):
            y_val = yangian_coeffs.get(d, 0)
            c_val = classical_coeffs.get(d, 0)
            assert y_val == c_val, (
                f"Degree {d}: Yangian gives {y_val}, classical gives {c_val}"
            )

    def test_newton_esf_round_trip(self):
        """Newton power sums and elementary symmetric fns are consistent.

        Newton's identity: p_k = sum_{j=1}^{k} (-1)^{j-1} * j * e_j * p_{k-j} / ...
        More precisely: p_k - e_1*p_{k-1} + e_2*p_{k-2} - ... + (-1)^{k-1}*k*e_k = 0.

        We verify this identity at k=2 and k=3 as a cross-check between
        the Newton power sum computation and the elementary symmetric function
        computation, which use independent code paths.
        """
        params = kummer_k3_parameters()
        p = newton_power_sums(params, max_k=4)
        e = elementary_symmetric_functions(params, max_k=4)

        # Newton identity at k=2: p_2 - e_1*p_1 + 2*e_2 = 0
        # Since e_1 = 0 and p_1 = 0: p_2 + 2*e_2 = 0 => e_2 = -p_2/2
        newton_k2 = p[2] - e[1] * p[1] + 2 * e[2]
        assert newton_k2 == 0, f"Newton identity at k=2 failed: {newton_k2}"

        # Newton identity at k=3: p_3 - e_1*p_2 + e_2*p_1 - 3*e_3 = 0
        # Since e_1 = 0, p_1 = 0: p_3 - 3*e_3 = 0 => e_3 = p_3/3
        newton_k3 = p[3] - e[1] * p[2] + e[2] * p[1] - 3 * e[3]
        assert newton_k3 == 0, f"Newton identity at k=3 failed: {newton_k3}"


# =========================================================================
# Section 11: Full verification
# =========================================================================

class TestFullVerification:
    """Integration tests running the full verification suite."""

    def test_full_verification_runs(self):
        """Full verification suite runs without errors."""
        result = full_verification()
        assert result['status'] == 'CONJECTURAL'
        assert 'path1_cy2_constraint' in result
        assert 'path8_bar_euler_eta24' in result

    def test_all_paths_consistent(self):
        """All verification paths give consistent results."""
        result = full_verification()

        # CY_2 constraint
        assert result['path1_cy2_constraint']['is_zero']

        # Unitarity
        assert result['path2_unitarity_algebraic']['unitarity_holds']
        assert result['path3_unitarity_from_log']['unitarity_from_odd_parity']

        # Structure function
        assert result['path4_structure_function_degree']['phi_0_is_1']
        assert result['path4_structure_function_degree']['phi_1_is_0']

        # Special values
        assert result['path5_structure_function_values']['g_at_0_matches']

        # R-matrix
        assert result['path6_r_matrix_charge_1']['is_diagonal']
        assert result['path6_r_matrix_charge_1']['unitarity_at_z2']

        # YBE
        assert result['path7_ybe_diagonal']['ybe_holds']

        # Bar Euler
        assert result['path8_bar_euler_eta24']['all_match']
        assert result['path9_bar_euler_classical_match']['yangian_equals_classical']
