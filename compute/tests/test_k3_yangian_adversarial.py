r"""Tests for k3_yangian_adversarial.py: adversarial analysis of Y(g_{K3}).

STATUS: ALL results are CONJECTURAL (AP-CY14).
Tests verify that the adversarial analysis is internally consistent
and that the six attack vectors are correctly resolved.

ATTACK VECTORS:
    1. Indefinite signature (4,20): P_omega^2 spectrum (5 tests)
    2. Level-rank duality: inapplicability (3 tests)
    3. Infinite root multiplicity: bar complex vs generators (4 tests)
    4. Moduli dependence: flat deformation (5 tests)
    5. CY-A_3 obstruction: layer scoping (4 tests)
    6. Coassociativity at rank 24: scalar case (5 tests)
    7. Full adversarial report (3 tests)

Total: 29 tests.
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.k3_yangian_adversarial import (
    omega_twisted_permutation_spectrum,
    structure_function_positive_vs_negative,
    level_rank_duality_analysis,
    infinite_root_multiplicity_analysis,
    moduli_dependence_analysis,
    cy_a3_obstruction_analysis,
    coassociativity_rank24_analysis,
    full_adversarial_report,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
)


# =========================================================================
# Attack 1: Indefinite Signature Obstruction
# =========================================================================


class TestIndefiniteSignature:
    """Tests for Attack 1: indefinite signature (4,20)."""

    def test_p_omega_squared_dimension(self):
        """P_omega^2 eigenvalue counts sum to 24^2 = 576."""
        result = omega_twisted_permutation_spectrum()
        eigenvalues = result['P_omega_squared_eigenvalues']
        assert eigenvalues['+1'] + eigenvalues['-1'] == 576

    def test_p_omega_squared_positive_count(self):
        """Same-sign pairs: 4*4 + 20*20 = 416 with eigenvalue +1."""
        result = omega_twisted_permutation_spectrum()
        assert result['P_omega_squared_eigenvalues']['+1'] == 416

    def test_p_omega_squared_negative_count(self):
        """Mixed-sign pairs: 2*4*20 = 160 with eigenvalue -1."""
        result = omega_twisted_permutation_spectrum()
        assert result['P_omega_squared_eigenvalues']['-1'] == 160

    def test_p_omega_not_involution(self):
        """P_omega is NOT an involution (P_omega^2 != Id)."""
        result = omega_twisted_permutation_spectrum()
        assert result['P_omega_is_involution'] is False

    def test_abelian_safe(self):
        """The abelian (gl_1) case is safe from signature obstruction."""
        result = omega_twisted_permutation_spectrum()
        assert result['abelian_safe'] is True

    def test_structure_function_unitarity(self):
        """g_{K3}(z) * g_{K3}(-z) = 1 despite indefinite signature."""
        result = structure_function_positive_vs_negative()
        assert result['unitarity_holds'] is True

    def test_individual_direction_unitarity(self):
        """Each direction satisfies g_i(z)*g_i(-z) = 1 independently."""
        result = structure_function_positive_vs_negative()
        assert result['individual_unitarity_all_pass'] is True


# =========================================================================
# Attack 2: Level-Rank Duality
# =========================================================================


class TestLevelRankDuality:
    """Tests for Attack 2: level-rank duality inapplicability."""

    def test_duality_inapplicable(self):
        """Level-rank duality does not apply to abelian algebras."""
        result = level_rank_duality_analysis()
        assert result['level_rank_applicability'] is False

    def test_three_independent_ranks(self):
        """Lattice rank, Lie algebra rank, and CFT level are independent."""
        result = level_rank_duality_analysis()
        data = result['k3_cft_data']
        assert data['lattice_rank'] == 24
        assert data['lie_algebra_rank'] == 1
        assert data['heisenberg_level'] == 1
        # All three are different or independently determined
        assert data['lattice_rank'] != data['lie_algebra_rank']

    def test_central_charge(self):
        """K3 CFT has c = 6."""
        result = level_rank_duality_analysis()
        assert result['k3_cft_data']['central_charge'] == 6


# =========================================================================
# Attack 3: Infinite Root Multiplicity
# =========================================================================


class TestInfiniteRootMultiplicity:
    """Tests for Attack 3: infinite root multiplicities in BKM."""

    def test_input_is_finite_dimensional(self):
        """The input Lie algebra H_Muk is finite-dimensional (25-dim)."""
        result = infinite_root_multiplicity_analysis()
        assert 'FINITE' in result['input_lie_algebra']

    def test_bkm_is_not_input(self):
        """g_{Delta_5} is NOT the input to the Yangian construction."""
        result = infinite_root_multiplicity_analysis()
        assert 'NOT the input' in result['not_input']

    def test_root_multiplicities_grow(self):
        """BKM root multiplicities grow without bound."""
        result = infinite_root_multiplicity_analysis()
        mults = result['bkm_root_multiplicities']
        # c(0) = 24, c(1) = 324, ..., c(5) = 1073720
        assert mults[0] < mults[1] < mults[5]
        assert mults[5] > 1000000

    def test_bar_complex_mechanism(self):
        """Multiplicities appear in bar complex, not generators."""
        result = infinite_root_multiplicity_analysis()
        assert 'BAR COMPLEX' in result['bar_complex_role']


# =========================================================================
# Attack 4: Moduli Dependence
# =========================================================================


class TestModuliDependence:
    """Tests for Attack 4: moduli dependence of Y(g_{K3})."""

    def test_structure_functions_differ(self):
        """Different moduli points give different structure functions."""
        result = moduli_dependence_analysis()
        assert result['structure_functions_differ'] is True

    def test_both_unitary(self):
        """Both moduli points satisfy unitarity g(z)g(-z)=1."""
        result = moduli_dependence_analysis()
        assert result['both_satisfy_unitarity'] is True

    def test_bar_euler_invariant(self):
        """Bar Euler product is moduli-invariant."""
        result = moduli_dependence_analysis()
        assert result['bar_euler_invariant'] is True

    def test_flat_deformation(self):
        """The transition across moduli is a flat deformation."""
        result = moduli_dependence_analysis()
        assert result['deformation_type'] == 'FLAT (PBW-preserving)'

    def test_generic_vs_null_unitarity(self):
        """Verify unitarity at both generic and null parameter points."""
        z_test = Rational(7)
        for params in [kummer_k3_parameters(), null_kummer_parameters()]:
            g_z = structure_function_evaluate(z_test, params)
            g_neg_z = structure_function_evaluate(-z_test, params)
            assert g_z * g_neg_z == 1


# =========================================================================
# Attack 5: CY-A_3 Obstruction
# =========================================================================


class TestCYA3Obstruction:
    """Tests for Attack 5: CY-A_3 dependence scoping."""

    def test_four_layers(self):
        """The construction has exactly 4 layers with different CY-A dependence."""
        result = cy_a3_obstruction_analysis()
        assert len(result['layers']) == 4

    def test_layer1_no_cya(self):
        """Layer 1 (K3 DCA) has no CY-A dependence."""
        result = cy_a3_obstruction_analysis()
        layer1 = result['layers'][0]
        assert layer1['cy_a_dependence'] == 'NONE'
        assert layer1['status'] == 'PROVED'

    def test_abelian_standalone(self):
        """The abelian gl_1 Yangian is standalone (no CY-A_3 needed)."""
        result = cy_a3_obstruction_analysis()
        assert result['abelian_gl1_standalone'] is True

    def test_nonabelian_requires_cya3(self):
        """The nonabelian enhancement requires CY-A_3."""
        result = cy_a3_obstruction_analysis()
        assert result['nonabelian_requires_cy_a3'] is True

    def test_no_global_hodge_parity_upgrade(self):
        """The adversarial report keeps the compact super-Yangian conditional."""
        result = full_adversarial_report()
        assert '1_indefinite_signature' in result['genuine_obstructions']
        assert '5_cy_a3_obstruction' in result['genuine_obstructions']
        assert 'Layer 3-4' in result['recommendation']


# =========================================================================
# Attack 6: Coassociativity at Rank 24
# =========================================================================


class TestCoassociativityRank24:
    """Tests for Attack 6: coassociativity at rank 24 with sig (4,20)."""

    def test_transfer_coassociative(self):
        """Transfer matrix triple product is coassociative."""
        result = coassociativity_rank24_analysis()
        assert result['transfer_coassociative'] is True

    def test_structure_fn_coassociative(self):
        """Structure function triple product is coassociative."""
        result = coassociativity_rank24_analysis()
        assert result['structure_fn_coassociative'] is True

    def test_rank_24(self):
        """Verification is at rank 24."""
        result = coassociativity_rank24_analysis()
        assert result['rank'] == 24

    def test_correct_signature(self):
        """Signature is (4,20)."""
        result = coassociativity_rank24_analysis()
        assert result['signature'] == (4, 20)

    def test_path_equality(self):
        """Both coassociativity paths give the same value."""
        result = coassociativity_rank24_analysis()
        assert result['transfer_path_L'] == result['transfer_path_R']


# =========================================================================
# Full Adversarial Report
# =========================================================================


class TestFullAdversarialReport:
    """Tests for the combined adversarial report."""

    def test_six_attacks(self):
        """All six attack vectors are present."""
        result = full_adversarial_report()
        assert len(result['attacks']) == 6

    def test_genuine_obstructions_identified(self):
        """Genuine obstructions are correctly identified."""
        result = full_adversarial_report()
        assert len(result['genuine_obstructions']) >= 1
        # Attack 1 (indefinite sig) and Attack 5 (CY-A_3) are genuine
        assert any('signature' in o or 'cy_a3' in o
                    for o in result['genuine_obstructions'])

    def test_non_obstructions_identified(self):
        """Non-obstructions are correctly identified."""
        result = full_adversarial_report()
        assert len(result['non_obstructions']) >= 3
        # Level-rank, infinite roots, coassociativity are non-obstructions
        assert any('level_rank' in o for o in result['non_obstructions'])
