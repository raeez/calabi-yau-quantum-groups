r"""Tests for k3_abelian_yangian_presentation.py: complete generators-and-relations
presentation of the abelian K3 Yangian Y(g_{K3}) for gl_1.

Manuscript reference:
    k3_times_e.tex, Theorem thm:k3-abelian-yangian-presentation

Test structure:
    Section 1: OPE and Heisenberg structure (7 tests)
    Section 2: Transfer matrix and Miura (5 tests)
    Section 3: Structure function (8 tests)
    Section 4: RTT and Lax operator (4 tests)
    Section 5: Coproduct (9 tests)
    Section 6: Koszul dual (6 tests)
    Section 7: Full presentation assembly (3 tests)
    Section 8: Cross-verification with existing engines (5 tests)
    Total: 47 tests.
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.k3_abelian_yangian_presentation import (
    # Constants
    RANK,
    SIGNATURE,
    PSI_EFF,
    KOSZUL_CONDUCTOR,
    # OPE
    heisenberg_ope,
    verify_ope_consistency,
    # Transfer matrix
    transfer_matrix_data,
    verify_transfer_matrix_truncation,
    # Structure function
    structure_function_data,
    verify_structure_function,
    # Lax / RTT
    lax_operator_data,
    verify_rtt_diagonal,
    verify_ybe_diagonal,
    # Coproduct
    coproduct_data,
    verify_coproduct_structural,
    verify_coassociativity_miura,
    verify_spin2_cross_term_coefficient,
    # Koszul
    koszul_dual_presentation,
    verify_koszul_dual,
    # Full presentation
    full_presentation,
    full_verification,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
    mukai_diagonal_eigenvalues,
)

from compute.lib.k3_double_current_algebra import (
    MUKAI_RANK,
    bar_euler_generating_function,
)

F = Fraction


# =========================================================================
# Section 1: OPE and Heisenberg structure
# =========================================================================

class TestHeisenbergOPE:
    """Tests for the 24 Heisenberg currents and their OPE."""

    def test_rank_is_24(self):
        """The K3 Yangian has 24 currents."""
        ope = heisenberg_ope()
        assert ope.rank == 24

    def test_signature_is_4_20(self):
        """Mukai pairing has signature (4, 20)."""
        ope = heisenberg_ope()
        assert ope.signature == (4, 20)

    def test_effective_level_is_minus_16(self):
        """Tr(omega) = 4 - 20 = -16."""
        ope = heisenberg_ope()
        assert ope.effective_level == -16

    def test_pairing_diagonal_length(self):
        """Pairing diagonal has 24 entries."""
        ope = heisenberg_ope()
        assert len(ope.pairing_diagonal) == 24

    def test_pairing_positive_count(self):
        """4 positive entries in Mukai pairing."""
        ope = heisenberg_ope()
        assert sum(1 for s in ope.pairing_diagonal if s == 1) == 4

    def test_pairing_negative_count(self):
        """20 negative entries in Mukai pairing."""
        ope = heisenberg_ope()
        assert sum(1 for s in ope.pairing_diagonal if s == -1) == 20

    def test_ope_consistency_full(self):
        """Full OPE consistency check."""
        result = verify_ope_consistency()
        assert result['ok']


# =========================================================================
# Section 2: Transfer matrix and Miura
# =========================================================================

class TestTransferMatrix:
    """Tests for the transfer matrix and Miura factorisation."""

    def test_rank_is_24(self):
        """Transfer matrix has rank 24."""
        data = transfer_matrix_data()
        assert data.rank == 24

    def test_truncation_at_24(self):
        """psi_s = 0 for s > 24."""
        data = transfer_matrix_data()
        assert data.truncation_spin == 24

    def test_truncation_verification(self):
        """Truncation properties verified."""
        result = verify_transfer_matrix_truncation()
        assert result['ok']

    def test_total_operator_products(self):
        """Total operator products across spins 1-24."""
        result = verify_transfer_matrix_truncation()
        expected = sum(s * (s + 1) // 2 - 1 for s in range(1, 25))
        assert result['total_operator_products'] == expected

    def test_z_degree_sum(self):
        """Total z-degree = 24*23/2 = 276."""
        result = verify_transfer_matrix_truncation()
        assert result['total_z_degree_sum'] == 24 * 23 // 2


# =========================================================================
# Section 3: Structure function
# =========================================================================

class TestStructureFunction:
    """Tests for the structure function g_{K3}(u)."""

    def test_degree_is_24_24(self):
        """g_{K3} has degree (24, 24)."""
        data = structure_function_data()
        assert data.degree == (24, 24)

    def test_g_at_0_is_1(self):
        """g_{K3}(0) = (-1)^{24} = 1."""
        data = structure_function_data()
        assert data.g_at_0 == 1

    def test_g_at_inf_is_1(self):
        """g_{K3}(inf) = 1."""
        data = structure_function_data()
        assert data.g_at_inf == 1

    def test_phi_1_is_0(self):
        """phi_1 = 0 from CY_2 constraint."""
        data = structure_function_data()
        assert data.phi_1 == 0

    def test_unitarity_algebraic(self):
        """g(u)*g(-u) = 1 verified at test points."""
        result = verify_structure_function()
        assert result['unitarity_ok']

    def test_koszul_inversion(self):
        """g(u)*g^!(u) = 1."""
        result = verify_structure_function()
        assert result['koszul_inversion_ok']

    def test_is_diagonal(self):
        """g_{ij} is diagonal for gl_1."""
        data = structure_function_data()
        assert data.is_diagonal

    def test_full_structure_function_check(self):
        """Full structure function verification passes."""
        result = verify_structure_function()
        assert result['ok']


# =========================================================================
# Section 4: RTT and Lax operator
# =========================================================================

class TestRTTLax:
    """Tests for the RTT relation and Lax operator."""

    def test_lax_rank(self):
        """Lax operator is 24x24."""
        data = lax_operator_data()
        assert data.rank == 24

    def test_rtt_trivial_for_abelian(self):
        """RTT is trivial for the abelian case."""
        data = lax_operator_data()
        assert data.rtt_trivial_for_abelian

    def test_rtt_verification(self):
        """RTT verification passes."""
        result = verify_rtt_diagonal()
        assert result['ok']

    def test_ybe_verification(self):
        """YBE verification passes."""
        result = verify_ybe_diagonal()
        assert result['ok']


# =========================================================================
# Section 5: Coproduct
# =========================================================================

class TestCoproduct:
    """Tests for the coproduct Delta_z."""

    def test_max_spin_is_24(self):
        """Max spin for coproduct is 24."""
        data = coproduct_data()
        assert data.max_spin == 24

    def test_spin1_is_primitive(self):
        """Spin 1 coproduct is primitive."""
        data = coproduct_data()
        assert 'primitive' in data.primitive_generator.lower()

    def test_spin2_cross_coeff_is_17_over_16(self):
        """Spin-2 cross-term coefficient is 17/16."""
        result = verify_spin2_cross_term_coefficient()
        assert result['ok']
        assert result['alpha'] == F(17, 16)

    def test_spin2_alpha_greater_than_1(self):
        """alpha > 1 because Psi_eff < 0."""
        result = verify_spin2_cross_term_coefficient()
        assert result['alpha_greater_than_1']

    def test_coproduct_structural_spin1(self):
        """Spin 1: z-degree 0, 0 cross-terms."""
        result = verify_coproduct_structural(max_spin=1)
        assert result['ok']

    def test_coproduct_structural_spin2(self):
        """Spin 2: z-degree 1, 1 cross-term."""
        result = verify_coproduct_structural(max_spin=2)
        assert result['ok']

    def test_coproduct_structural_spin6(self):
        """Spins 1-6: all structural properties hold."""
        result = verify_coproduct_structural(max_spin=6)
        assert result['ok']

    def test_coassociativity(self):
        """Coassociativity from Miura multiplicativity."""
        result = verify_coassociativity_miura()
        assert result['ok']

    def test_coassociativity_rank_24(self):
        """Coassociativity at rank 24."""
        result = verify_coassociativity_miura()
        assert result['rank'] == 24


# =========================================================================
# Section 6: Koszul dual
# =========================================================================

class TestKoszulDual:
    """Tests for the Koszul dual Y(g_{K3})^!."""

    def test_dual_params_negated(self):
        """Dual parameters are -h_i."""
        kd = koszul_dual_presentation()
        for i in range(len(kd.original_params)):
            assert kd.dual_params[i] == -kd.original_params[i]

    def test_conductor_is_0(self):
        """Koszul conductor K = 0."""
        kd = koszul_dual_presentation()
        assert kd.conductor == 0

    def test_dual_cy2(self):
        """Dual parameters satisfy CY_2."""
        kd = koszul_dual_presentation()
        assert sum(kd.dual_params) == 0

    def test_koszul_inversion(self):
        """g * g^! = 1 at test points."""
        result = verify_koszul_dual()
        assert result['inversion_ok']

    def test_reflection_equals_dual(self):
        """g^!(z) = g(-z) (from unitarity)."""
        result = verify_koszul_dual()
        assert result['reflection_g_dual_equals_g_neg']

    def test_full_koszul_verification(self):
        """Full Koszul verification passes."""
        result = verify_koszul_dual()
        assert result['ok']


# =========================================================================
# Section 7: Full presentation assembly
# =========================================================================

class TestFullPresentation:
    """Tests for the complete presentation assembly."""

    def test_presentation_rank(self):
        """Presentation has rank 24."""
        pres = full_presentation()
        assert pres.rank == 24

    def test_presentation_signature(self):
        """Presentation has signature (4, 20)."""
        pres = full_presentation()
        assert pres.signature == (4, 20)

    def test_presentation_conductor(self):
        """Koszul conductor is 0."""
        pres = full_presentation()
        assert pres.koszul_conductor == 0


# =========================================================================
# Section 8: Cross-verification with existing engines
# =========================================================================

class TestCrossVerification:
    """Cross-verification against k3_yangian.py and k3_double_current_algebra.py."""

    def test_rank_matches_mukai(self):
        """RANK matches MUKAI_RANK."""
        assert RANK == MUKAI_RANK
        assert RANK == 24

    def test_signature_matches(self):
        """Signature matches k3_yangian constants."""
        assert SIGNATURE == (SIG_PLUS, SIG_MINUS)
        assert SIGNATURE == (4, 20)

    def test_psi_eff_matches(self):
        """PSI_EFF matches eigenvalue sum."""
        eigenvalues = mukai_diagonal_eigenvalues()
        assert PSI_EFF == sum(eigenvalues)
        assert PSI_EFF == -16

    def test_bar_euler_first_coefficients(self):
        """Bar Euler product matches eta^{24} coefficients."""
        coeffs = bar_euler_generating_function(5)
        assert coeffs[0] == 1
        assert coeffs[1] == -24
        assert coeffs[2] == 252

    def test_full_verification_suite(self):
        """Full verification suite passes."""
        result = full_verification()
        assert result['all_ok']
