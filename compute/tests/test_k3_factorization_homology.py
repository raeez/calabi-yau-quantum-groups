r"""Tests for k3_factorization_homology.py: factorization homology of E_2-algebras over K3.

CENTRAL RESULTS:
    (1) E_inf FH of H_1 over K3 recovers H_Muk (rank 24, Mukai sig (4,20)).
    (2) Handle decomposition: 1+22+1 = 24 handles, chi = 24.
    (3) Tree-level character 1/eta^{24}: coefficients = Gottsche numbers.
    (4) Excision produces rank 24 with Mukai signature.
    (5) Shadow class transition: G -> L -> M through perturbative expansion.
    (6) Connection to U_{q,t}(gl_hat_hat_1) is CONJECTURAL (AP-CY32).
    (7) Intersection form trace: Tr(Q^2) = 22 = b_2(K3).
    (8) kappa-spectrum: kappa_cat=2, kappa_fiber=24 (AP113 compliant).

Manuscript references:
    en_factorization.tex (FH framework, conj:fact-hom-k3xe)
    k3_times_e.tex sec:k3-perturbative-fact-homology
    braided_factorization.tex (excision, def:factorization-homology)
"""

import pytest
from fractions import Fraction

from compute.lib.k3_factorization_homology import (
    # Constants
    K3_BETTI,
    K3_EULER_CHAR,
    K3_TOTAL_HOMOLOGY_DIM,
    K3_SIGNATURE,
    K3_ZERO_HANDLES,
    K3_ONE_HANDLES,
    K3_TWO_HANDLES,
    K3_THREE_HANDLES,
    K3_FOUR_HANDLES,
    K3_TOTAL_HANDLES,
    K3_H2_SIG_PLUS,
    K3_H2_SIG_MINUS,
    K3_CHI_O,
    # E_inf FH
    einf_factorization_homology_k3,
    einf_fh_pairing_signature,
    # Handle decomposition
    k3_handle_decomposition,
    iterative_excision_k3,
    # Tree level
    tree_level_fh_k3,
    tree_level_character_coefficients,
    # Toroidal structure
    toroidal_structure_k3xe,
    double_loop_generator_count,
    # One-loop
    one_loop_correction_k3,
    cup_product_structure_constants,
    # Perturbative
    perturbative_expansion_k3,
    # Quantum toroidal
    quantum_toroidal_connection,
    # Verification
    verify_betti_handle_consistency,
    verify_einf_fh_recovers_mukai,
    verify_tree_level_character,
    verify_excision_final_rank,
    verify_perturbative_shadow_classes,
    verify_conjectural_status,
    verify_intersection_trace,
    verify_kappa_spectrum,
    full_verification,
)

F = Fraction


# =========================================================================
# Section 1: K3 topology constants
# =========================================================================

class TestK3Topology:
    """Betti numbers, Euler characteristic, and topological invariants of K3."""

    def test_betti_numbers(self):
        """K3 Betti numbers: (1, 0, 22, 0, 1)."""
        assert K3_BETTI == (1, 0, 22, 0, 1)

    def test_euler_characteristic(self):
        """chi(K3) = 24."""
        assert K3_EULER_CHAR == 24

    def test_euler_from_betti(self):
        """chi = sum (-1)^k b_k = 1 - 0 + 22 - 0 + 1 = 24."""
        chi = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        assert chi == 24

    def test_total_homology_dimension(self):
        """dim H_*(K3; Q) = 1 + 0 + 22 + 0 + 1 = 24."""
        assert K3_TOTAL_HOMOLOGY_DIM == 24
        assert K3_TOTAL_HOMOLOGY_DIM == sum(K3_BETTI)

    def test_signature(self):
        """Hirzebruch signature tau(K3) = -16."""
        assert K3_SIGNATURE == -16
        # tau = b_2^+ - b_2^- = 3 - 19 = -16
        assert K3_H2_SIG_PLUS - K3_H2_SIG_MINUS == -16

    def test_holomorphic_euler(self):
        """chi(O_{K3}) = 2 = kappa_cat."""
        assert K3_CHI_O == 2

    def test_simply_connected(self):
        """K3 is simply connected: b_1 = 0."""
        assert K3_BETTI[1] == 0

    def test_odd_betti_vanish(self):
        """H^{odd}(K3) = 0: b_1 = b_3 = 0."""
        assert K3_BETTI[1] == 0
        assert K3_BETTI[3] == 0

    def test_poincare_duality(self):
        """Poincare duality: b_k = b_{4-k} for real dim 4."""
        assert K3_BETTI[0] == K3_BETTI[4]
        assert K3_BETTI[1] == K3_BETTI[3]


# =========================================================================
# Section 2: Handle decomposition
# =========================================================================

class TestHandleDecomposition:
    """Handle decomposition of K3: 1 + 0 + 22 + 0 + 1."""

    def test_handle_counts(self):
        """K3 has 1 zero-handle, 0 one-handles, 22 two-handles, 0 three-handles, 1 four-handle."""
        assert K3_ZERO_HANDLES == 1
        assert K3_ONE_HANDLES == 0
        assert K3_TWO_HANDLES == 22
        assert K3_THREE_HANDLES == 0
        assert K3_FOUR_HANDLES == 1

    def test_total_handles(self):
        """Total handles = 24 = chi(K3)."""
        assert K3_TOTAL_HANDLES == 24

    def test_euler_from_handles(self):
        """chi = n_0 - n_1 + n_2 - n_3 + n_4 = 1 - 0 + 22 - 0 + 1 = 24."""
        chi = (K3_ZERO_HANDLES - K3_ONE_HANDLES + K3_TWO_HANDLES
               - K3_THREE_HANDLES + K3_FOUR_HANDLES)
        assert chi == K3_EULER_CHAR

    def test_handle_decomposition_object(self):
        """HandleDecomposition NamedTuple consistency."""
        hd = k3_handle_decomposition()
        assert hd.euler_check is True
        assert hd.simply_connected is True
        assert hd.total_handles == 24
        assert hd.intersection_form_rank == 22
        assert hd.intersection_form_sig == (3, 19)

    def test_handles_match_betti(self):
        """Each handle count matches the corresponding Betti number."""
        hd = k3_handle_decomposition()
        for k in range(5):
            assert hd.num_handles[k] == K3_BETTI[k]

    def test_no_one_handles(self):
        """pi_1(K3) = 0 implies no 1-handles needed."""
        hd = k3_handle_decomposition()
        assert hd.num_handles[1] == 0
        assert hd.simply_connected

    def test_two_handles_from_intersection_form(self):
        """22 two-handles = rank of intersection form on H^2."""
        hd = k3_handle_decomposition()
        assert hd.num_handles[2] == hd.intersection_form_rank == 22


# =========================================================================
# Section 3: E_inf factorization homology
# =========================================================================

class TestEInfFH:
    """E_inf factorization homology: int_{K3} A = A tensor H_*(K3)."""

    def test_rank_1_heisenberg(self):
        """int_{K3} H_1 has rank 24."""
        fh = einf_factorization_homology_k3(algebra_rank=1)
        assert fh.output_rank == 24

    def test_rank_1_decomposition(self):
        """Decomposition by degree: 1 from H_0, 22 from H_2, 1 from H_4."""
        fh = einf_factorization_homology_k3(algebra_rank=1)
        assert fh.decomposition[0] == 1   # from H_0
        assert fh.decomposition[2] == 22  # from H_2
        assert fh.decomposition[4] == 1   # from H_4
        assert 1 not in fh.decomposition  # H_1 = 0
        assert 3 not in fh.decomposition  # H_3 = 0

    def test_rank_1_total(self):
        """Total rank = sum of contributions = 1 + 22 + 1 = 24."""
        fh = einf_factorization_homology_k3(algebra_rank=1)
        assert sum(fh.decomposition.values()) == 24

    def test_higher_rank(self):
        """int_{K3} H_k has rank k * 24."""
        for k in [1, 2, 3, 5]:
            fh = einf_factorization_homology_k3(algebra_rank=k)
            assert fh.output_rank == k * 24

    def test_pairing_signature_rank_1(self):
        """Pairing on int_{K3} H_1 has Mukai signature (4, 20)."""
        sig = einf_fh_pairing_signature(algebra_rank=1)
        assert sig['total_signature'] == (4, 20)
        assert sig['matches_mukai'] is True

    def test_h0_h4_hyperbolic_plane(self):
        """H_0-H_4 block contributes signature (1, 1) (hyperbolic plane)."""
        sig = einf_fh_pairing_signature(algebra_rank=1)
        assert sig['h0_h4_block_sig'] == (1, 1)

    def test_h2_intersection_sig(self):
        """H_2 block contributes signature (3, 19) (intersection form)."""
        sig = einf_fh_pairing_signature(algebra_rank=1)
        assert sig['h2_block_sig'] == (3, 19)

    def test_recovers_mukai_heisenberg(self):
        """E_inf FH of H_1 over K3 = H_Muk (rank 24, Mukai pairing)."""
        result = verify_einf_fh_recovers_mukai()
        assert result['cross_check'] is True
        assert result['rank_match'] is True
        assert result['signature_match'] is True


# =========================================================================
# Section 4: Iterative excision
# =========================================================================

class TestIterativeExcision:
    """Excision computation through handle decomposition."""

    def test_excision_starts_at_algebra(self):
        """Step 0 (0-handle): rank = input rank."""
        steps = iterative_excision_k3(input_rank=1)
        assert steps[0].cumulative_rank == 1
        assert steps[0].handle_index == 0

    def test_excision_final_rank(self):
        """Final step (4-handle): rank = 24 = Mukai rank."""
        steps = iterative_excision_k3(input_rank=1)
        assert steps[-1].cumulative_rank == 24

    def test_excision_final_signature(self):
        """Final signature = Mukai (4, 20)."""
        steps = iterative_excision_k3(input_rank=1)
        assert steps[-1].pairing_signature == (4, 20)

    def test_excision_higher_rank(self):
        """For input rank k, final rank = 24k."""
        for k in [1, 2, 3]:
            steps = iterative_excision_k3(input_rank=k)
            assert steps[-1].cumulative_rank == 24 * k

    def test_excision_monotone_rank(self):
        """Cumulative rank is non-decreasing."""
        steps = iterative_excision_k3(input_rank=1)
        ranks = [s.cumulative_rank for s in steps]
        assert all(ranks[i] <= ranks[i + 1] for i in range(len(ranks) - 1))

    def test_excision_four_handle_last(self):
        """The last step is a 4-handle."""
        steps = iterative_excision_k3(input_rank=1)
        assert steps[-1].handle_index == 4

    def test_verify_excision_final_rank(self):
        """Full verification of excision final rank."""
        result = verify_excision_final_rank()
        assert result['rank_match'] is True
        assert result['signature_match'] is True


# =========================================================================
# Section 5: Tree-level character
# =========================================================================

class TestTreeLevelCharacter:
    """Tree-level character 1/eta^{24} and Gottsche numbers."""

    def test_tree_level_algebra(self):
        """Tree level = lattice VOA V_{tilde{Lambda}_{K3}}."""
        tree = tree_level_fh_k3()
        assert tree.output_rank == 24
        assert tree.shadow_class == 'G'

    def test_tree_level_central_charge(self):
        """Central charge c = 24."""
        tree = tree_level_fh_k3()
        assert tree.output_central_charge == 24

    def test_character_p24_0(self):
        """p_{24}(0) = 1."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[0] == 1

    def test_character_p24_1(self):
        """p_{24}(1) = 24 = chi(K3) = chi(Hilb^1(K3))."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[1] == 24

    def test_character_p24_2(self):
        """p_{24}(2) = 324 = chi(Hilb^2(K3))."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[2] == 324

    def test_character_p24_3(self):
        """p_{24}(3) = 3200 = chi(Hilb^3(K3))."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[3] == 3200

    def test_character_p24_4(self):
        """p_{24}(4) = 25650 = chi(Hilb^4(K3))."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[4] == 25650

    def test_character_p24_5(self):
        """p_{24}(5) = 176256 = chi(Hilb^5(K3))."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[5] == 176256

    def test_character_p24_6(self):
        """p_{24}(6) = 1073720 = chi(Hilb^6(K3))."""
        coeffs = tree_level_character_coefficients(max_degree=6)
        assert coeffs[6] == 1073720

    def test_verify_tree_character(self):
        """Full verification of tree-level character."""
        result = verify_tree_level_character()
        assert result['all_match'] is True

    def test_tree_level_conditional(self):
        """Tree level is conditional on CY-A_3 framework."""
        tree = tree_level_fh_k3()
        assert tree.is_conditional is True


# =========================================================================
# Section 6: Toroidal structure
# =========================================================================

class TestToroidalStructure:
    """Double loop algebra and toroidal structure from K3 x E."""

    def test_two_loop_parameters(self):
        """Two loop parameters: s (K3) and t (E)."""
        ts = toroidal_structure_k3xe()
        assert ts.num_loop_parameters == 2

    def test_rank_24(self):
        """Toroidal algebra has rank 24 (Mukai)."""
        ts = toroidal_structure_k3xe()
        assert ts.rank == 24

    def test_conjectural(self):
        """Toroidal structure is conjectural."""
        ts = toroidal_structure_k3xe()
        assert ts.is_conjectural is True

    def test_conditions_nonempty(self):
        """Conditions list is non-empty."""
        ts = toroidal_structure_k3xe()
        assert len(ts.conditions) >= 3

    def test_double_loop_generators(self):
        """24 generators per mode in double loop."""
        dlg = double_loop_generator_count()
        assert dlg['lattice_directions'] == 24
        assert dlg['loop_parameters'] == 2


# =========================================================================
# Section 7: One-loop correction
# =========================================================================

class TestOneLoop:
    """One-loop correction from cup product on H^*(K3)."""

    def test_intersection_trace(self):
        """Tr(Q^2) = 3 + 19 = 22 = b_2(K3)."""
        olc = one_loop_correction_k3()
        assert olc.intersection_trace == 22

    def test_euler_contribution(self):
        """chi(K3) = 24 enters the two-loop correction."""
        olc = one_loop_correction_k3()
        assert olc.euler_contribution == 24

    def test_conditional(self):
        """One-loop correction is conditional on CY-A_3."""
        olc = one_loop_correction_k3()
        assert olc.is_conditional is True

    def test_verify_intersection_trace(self):
        """Verification of Tr(Q^2)."""
        result = verify_intersection_trace()
        assert result['match'] is True
        assert result['tr_q_squared'] == 22

    def test_cup_product_formality(self):
        """K3 is formal: m_k = 0 for k >= 3 (DGMS 1975)."""
        cps = cup_product_structure_constants()
        assert 'formal' in cps['formality'].lower()

    def test_cup_product_even_intersection(self):
        """Intersection form is even: all Q_{ii} = 0."""
        cps = cup_product_structure_constants()
        assert 'even' in cps['intersection_form']['type'].lower()

    def test_intersection_form_unimodular(self):
        """det(Q) = 1 (unimodular)."""
        cps = cup_product_structure_constants()
        assert cps['intersection_form']['determinant'] == 1


# =========================================================================
# Section 8: Perturbative expansion and shadow classes
# =========================================================================

class TestPerturbativeExpansion:
    """Perturbative expansion in sigma_3 and shadow class transitions."""

    def test_tree_level_class_g(self):
        """Tree level (sigma_3 = 0) is class G."""
        exp = perturbative_expansion_k3()
        assert exp[0].shadow_class == 'G'
        assert exp[0].shadow_depth == 2

    def test_one_loop_class_l(self):
        """One loop (sigma_3^1) is class L."""
        exp = perturbative_expansion_k3()
        assert exp[1].shadow_class == 'L'
        assert exp[1].shadow_depth == 3

    def test_all_loops_class_m(self):
        """All loops (non-perturbative) is class M."""
        exp = perturbative_expansion_k3()
        assert exp[-1].shadow_class == 'M'
        assert exp[-1].shadow_depth == 'infinity'

    def test_shadow_depth_monotone(self):
        """Shadow depth is non-decreasing (for finite depths)."""
        result = verify_perturbative_shadow_classes()
        assert result['depth_monotone'] is True

    def test_class_transition_g_to_m(self):
        """Full transition: G -> M."""
        result = verify_perturbative_shadow_classes()
        assert result['class_transition'] == 'G -> M'

    def test_four_perturbative_orders(self):
        """Four perturbative levels described."""
        exp = perturbative_expansion_k3()
        assert len(exp) == 4


# =========================================================================
# Section 9: Quantum toroidal connection (CONJECTURAL)
# =========================================================================

class TestQuantumToroidalConnection:
    """Connection to U_{q,t}(gl_hat_hat_1). ALL CONJECTURAL (AP-CY32)."""

    def test_status_conjectural(self):
        """Status is CONJECTURAL."""
        qtc = quantum_toroidal_connection()
        assert qtc.status == 'CONJECTURAL'

    def test_ap_cy32_warning(self):
        """AP-CY32 warning is stated: reorganisation != bypass."""
        qtc = quantum_toroidal_connection()
        assert 'reorganis' in qtc.ap_cy32_warning.lower()

    def test_three_subproblems(self):
        """Three open subproblems identified."""
        qtc = quantum_toroidal_connection()
        assert len(qtc.subproblems) == 3

    def test_all_subproblems_open(self):
        """All subproblems are open or conjectural."""
        qtc = quantum_toroidal_connection()
        for key, val in qtc.subproblems.items():
            assert any(w in val.lower() for w in ['open', 'conjectural', 'perturbative'])

    def test_quantum_structure_requires(self):
        """Quantum structure requires at least 4 ingredients."""
        qtc = quantum_toroidal_connection()
        assert len(qtc.quantum_structure_requires) >= 4

    def test_verify_conjectural_status(self):
        """Full verification of conjectural status."""
        result = verify_conjectural_status()
        assert result['is_conjectural'] is True
        assert result['toroidal_structure_conjectural'] is True


# =========================================================================
# Section 10: kappa-spectrum (AP113)
# =========================================================================

class TestKappaSpectrum:
    """kappa-spectrum values for K3 x E (AP113 compliance)."""

    def test_kappa_cat(self):
        """kappa_cat = chi(O_{K3}) = 2."""
        result = verify_kappa_spectrum()
        assert result['kappa_cat'] == 2
        assert result['kappa_cat_match'] is True

    def test_kappa_fiber(self):
        """kappa_fiber = 24 (Mukai lattice rank)."""
        result = verify_kappa_spectrum()
        assert result['kappa_fiber'] == 24
        assert result['kappa_fiber_match'] is True

    def test_kappa_ch(self):
        """kappa_ch = 3 (from chiral algebra via Phi)."""
        result = verify_kappa_spectrum()
        assert result['kappa_ch'] == 3

    def test_kappa_bkm(self):
        """kappa_BKM = 5 (weight of Delta_5)."""
        result = verify_kappa_spectrum()
        assert result['kappa_BKM'] == 5

    def test_ap113_compliant(self):
        """All kappa values properly subscripted (AP113)."""
        result = verify_kappa_spectrum()
        assert result['ap113_compliant'] is True


# =========================================================================
# Section 11: Betti-handle consistency
# =========================================================================

class TestBettiHandleConsistency:
    """Cross-checks between Betti numbers and handle decomposition."""

    def test_full_consistency(self):
        """Full Betti-handle consistency check."""
        result = verify_betti_handle_consistency()
        assert result['euler_match'] is True
        assert result['betti_handle_match'] is True
        assert result['simply_connected'] is True

    def test_total_homology_dim(self):
        """Total homology dimension = 24."""
        result = verify_betti_handle_consistency()
        assert result['total_homology_dim'] == 24


# =========================================================================
# Section 12: Full verification
# =========================================================================

class TestFullVerification:
    """Full 8-path verification suite."""

    def test_all_paths_pass(self):
        """All 8 verification paths produce consistent results."""
        v = full_verification()
        # Path 1: Betti-handle
        assert v['path1_betti_handle']['euler_match'] is True
        # Path 2: E_inf FH -> Mukai
        assert v['path2_einf_fh_mukai']['cross_check'] is True
        # Path 3: Tree character
        assert v['path3_tree_character']['all_match'] is True
        # Path 4: Excision rank
        assert v['path4_excision_rank']['rank_match'] is True
        # Path 5: Perturbative shadow
        assert v['path5_perturbative_shadow']['depth_monotone'] is True
        # Path 6: Conjectural status
        assert v['path6_conjectural_status']['is_conjectural'] is True
        # Path 7: Intersection trace
        assert v['path7_intersection_trace']['match'] is True
        # Path 8: kappa spectrum
        assert v['path8_kappa_spectrum']['kappa_cat_match'] is True
        assert v['path8_kappa_spectrum']['kappa_fiber_match'] is True
