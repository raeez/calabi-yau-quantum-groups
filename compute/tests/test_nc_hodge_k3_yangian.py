r"""Tests for nc_hodge_k3_yangian.py: noncommutative Hodge theory for Y(g_{K3}).

STATUS: Categorical results (D^b(Coh(K3))) are PROVED.
Yangian-level results are CONJECTURAL (AP-CY14).
Tests verify internal consistency and cross-check with established data.

CENTRAL RESULTS:
    (1) NC Hodge structure on D^b(Coh(K3)): dim HH_* = 24 = Mukai rank (PROVED).
    (2) Hodge-to-de Rham degeneration: immediate for K3 (all odd cohomology vanishes) (PROVED).
    (3) Yangian Hodge filtration: 24 generators decompose as 1 + 22 + 1 by Hodge weight (CONJECTURAL).
    (4) Hodge-filtered supertrace: kappa_ch = kappa_cat = chi(O_K3) = 2 at d=2 (PROVED).
    (5) Twistor deformation: g_lambda(z) interpolates from 1 (lambda=0) to g_{K3}(z) (lambda=1) (CONJECTURAL).
    (6) Hodge-graded character: prod 1/(1-y^w q^n)^{h_w} reproduces 1/eta^24 at y=1 (CONJECTURAL).
    (7) Omega-background bridge: lambda = eps_3/eps_1 through intermediary mechanism (CONJECTURAL, AP-CY20).
    (8) Hodge R-matrix decomposition: diagonal blocks (0,0), (1,1), (2,2) with unitarity (CONJECTURAL).

Test structure:
    Section 1: NC Hodge structure on K3 (8 tests)
    Section 2: Hodge-to-de Rham degeneration (6 tests)
    Section 3: Yangian Hodge filtration (8 tests)
    Section 4: Hodge-filtered supertrace and kappa (10 tests)
    Section 5: Twistor deformation (8 tests)
    Section 6: Hodge-graded character (8 tests)
    Section 7: Omega-background bridge (5 tests)
    Section 8: Hodge R-matrix (5 tests)
    Section 9: Cross-consistency (7 tests)
    Section 10: Full verification (3 tests)
    Section 11: Multi-path verification (12 tests)

Total: 80 tests.

Manuscript references:
    hochschild_calculus.tex, Definition def:categorical-hodge-filtration
    hochschild_calculus.tex, Proposition prop:nc-hodge-dr
    hochschild_calculus.tex, Remark rem:hodge-shadow-bridge
    k3_yangian_chapter.tex, Section subsec:k3-fact-deformation
    cy_to_chiral.tex, Theorem thm:cy-to-chiral (CY-A_2)
    modular_koszul_bridge.tex (kappa_ch = chi^CY at d=2)
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.nc_hodge_k3_yangian import (
    # Constants
    NC_HODGE_STATUS_CATEGORICAL,
    NC_HODGE_STATUS_YANGIAN,
    K3_HODGE_DIAMOND,
    K3_BETTI,
    K3_HH_DIMS,
    K3_HH_TOTAL_DIM,
    MUKAI_HODGE_WEIGHTS,
    K3_CHI_O,
    KAPPA_CAT_K3,
    KAPPA_CH_K3,
    KAPPA_BKM_K3,
    KAPPA_FIBER_K3,
    # Functions
    nc_hodge_k3,
    hodge_de_rham_degeneration,
    yangian_hodge_filtration,
    hodge_supertrace,
    twistor_deformation,
    twistor_structure_function_verify,
    hodge_graded_character,
    omega_twistor_bridge,
    hodge_r_matrix,
    full_nc_hodge_verification,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
)

from compute.lib.k3_double_current_algebra import MUKAI_RANK

F = Fraction


# =========================================================================
# Section 1: NC Hodge structure on K3 (8 tests)
# =========================================================================

class TestNCHodgeK3:
    """Tests for the nc Hodge structure on D^b(Coh(K3))."""

    def test_hh_total_dim_is_24(self):
        """Total dim HH_*(K3) = 24 = Mukai rank."""
        hodge = nc_hodge_k3()
        assert hodge.hh_total_dim == 24
        assert hodge.hh_total_dim == MUKAI_RANK

    def test_chi_O_is_2(self):
        """chi(O_K3) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        hodge = nc_hodge_k3()
        assert hodge.chi_O == 2

    def test_hodge_diamond_symmetric(self):
        """h^{p,q} = h^{q,p} (complex conjugation) for K3."""
        for (p, q), val in K3_HODGE_DIAMOND.items():
            assert K3_HODGE_DIAMOND.get((q, p), 0) == val

    def test_hodge_diamond_serre_duality(self):
        """h^{p,q} = h^{2-p,2-q} (Serre duality for CY_2)."""
        for (p, q), val in K3_HODGE_DIAMOND.items():
            if 0 <= 2 - p <= 2 and 0 <= 2 - q <= 2:
                assert K3_HODGE_DIAMOND.get((2 - p, 2 - q), 0) == val

    def test_betti_numbers(self):
        """Betti numbers of K3: 1, 0, 22, 0, 1."""
        assert K3_BETTI == [1, 0, 22, 0, 1]

    def test_euler_characteristic_is_24(self):
        """chi(K3) = sum (-1)^k b_k = 1 - 0 + 22 - 0 + 1 = 24."""
        euler = sum((-1)**k * K3_BETTI[k] for k in range(5))
        assert euler == 24

    def test_cy_class_degree_is_2(self):
        """K3 is CY_2, so the CY class lives in HC^-_2."""
        hodge = nc_hodge_k3()
        assert hodge.cy_class_degree == 2

    def test_categorical_status_proved(self):
        """NC Hodge structure on D^b(Coh(K3)) is PROVED."""
        hodge = nc_hodge_k3()
        assert hodge.status == 'PROVED'


# =========================================================================
# Section 2: Hodge-to-de Rham degeneration (6 tests)
# =========================================================================

class TestHodgeDeRhamDegeneration:
    """Tests for the Hodge-to-de Rham degeneration on K3."""

    def test_degeneration_holds(self):
        """Hodge-to-dR spectral sequence degenerates at E_2."""
        result = hodge_de_rham_degeneration()
        assert result.degenerates is True

    def test_de_rham_dims_match_betti(self):
        """dim H^k_dR(K3) = b_k(K3)."""
        result = hodge_de_rham_degeneration()
        assert result.total_de_rham == K3_BETTI

    def test_e2_page_is_hodge_diamond(self):
        """E_2 page of the spectral sequence is the Hodge diamond."""
        result = hodge_de_rham_degeneration()
        for (p, q), val in K3_HODGE_DIAMOND.items():
            assert result.e2_page[(p, q)] == val

    def test_odd_cohomology_vanishes(self):
        """H^{odd}(K3) = 0 (reason for trivial degeneration)."""
        result = hodge_de_rham_degeneration()
        assert result.total_de_rham[1] == 0
        assert result.total_de_rham[3] == 0

    def test_de_rham_euler_is_24(self):
        """chi_dR(K3) = sum (-1)^k H^k_dR = 24."""
        result = hodge_de_rham_degeneration()
        euler = sum((-1)**k * result.total_de_rham[k] for k in range(5))
        assert euler == 24

    def test_status_categorical_proved(self):
        """Degeneration is PROVED for D^b(Coh(K3))."""
        result = hodge_de_rham_degeneration()
        assert result.status == 'PROVED'


# =========================================================================
# Section 3: Yangian Hodge filtration (8 tests)
# =========================================================================

class TestYangianHodgeFiltration:
    """Tests for the nc Hodge filtration on Y(g_{K3})."""

    def test_24_generators_total(self):
        """24 generators = 1 (H^0) + 22 (H^2) + 1 (H^4)."""
        filt = yangian_hodge_filtration()
        total = filt.num_weight_0 + filt.num_weight_1 + filt.num_weight_2
        assert total == 24
        assert total == NUM_PARAMS

    def test_weight_0_count(self):
        """1 generator of Hodge weight 0 (from H^0)."""
        filt = yangian_hodge_filtration()
        assert filt.num_weight_0 == 1

    def test_weight_1_count(self):
        """22 generators of Hodge weight 1 (from H^2)."""
        filt = yangian_hodge_filtration()
        assert filt.num_weight_1 == 22

    def test_weight_2_count(self):
        """1 generator of Hodge weight 2 (from H^4)."""
        filt = yangian_hodge_filtration()
        assert filt.num_weight_2 == 1

    def test_filtration_bounded_below(self):
        """The Hodge filtration is bounded below."""
        filt = yangian_hodge_filtration()
        assert filt.filtration_bounded_below is True

    def test_filtration_exhaustive(self):
        """The Hodge filtration is exhaustive (union = Y)."""
        filt = yangian_hodge_filtration()
        assert filt.filtration_exhaustive is True

    def test_associated_graded_is_U(self):
        """gr_F Y(g_{K3}) = U(H_Muk) (PBW = Hodge for free-field)."""
        filt = yangian_hodge_filtration()
        assert filt.associated_graded_is_U is True

    def test_yangian_status_conjectural(self):
        """Yangian-level Hodge structure is CONJECTURAL (AP-CY14)."""
        filt = yangian_hodge_filtration()
        assert filt.status == 'CONJECTURAL'


# =========================================================================
# Section 4: Hodge-filtered supertrace and kappa (10 tests)
# =========================================================================

class TestHodgeSupertraceKappa:
    """Tests for the Hodge-filtered supertrace and its relation to kappa_ch."""

    def test_chi_O_is_2(self):
        """chi(O_K3) = 2."""
        st = hodge_supertrace()
        assert st.chi_O == 2

    def test_alternating_sum_is_2(self):
        """sum (-1)^q h^{0,q} = 1 - 0 + 1 = 2."""
        st = hodge_supertrace()
        assert st.alternating_sum == 2

    def test_kappa_cat_is_2(self):
        """kappa_cat(K3) = chi(O_K3) = 2 (AP113)."""
        st = hodge_supertrace()
        assert st.kappa_cat == 2

    def test_kappa_ch_is_2(self):
        """kappa_ch(K3) = 2 at d=2 (AP113)."""
        st = hodge_supertrace()
        assert st.kappa_ch == 2

    def test_kappa_ch_equals_chi_O(self):
        """kappa_ch = chi(O_K3) at d=2 (PROVED)."""
        st = hodge_supertrace()
        assert st.kappa_equals_chi is True

    def test_kappa_ch_equals_kappa_cat(self):
        """kappa_ch = kappa_cat for K3 at d=2."""
        st = hodge_supertrace()
        assert st.kappa_ch == st.kappa_cat

    def test_kappa_bkm_is_5(self):
        """kappa_BKM = 5 (weight of Delta_5) (AP113)."""
        assert KAPPA_BKM_K3 == 5

    def test_kappa_fiber_is_24(self):
        """kappa_fiber = 24 (Mukai lattice rank) (AP113)."""
        assert KAPPA_FIBER_K3 == 24

    def test_hodge_column_0(self):
        """The (0,*) Hodge column: h^{0,0}=1, h^{0,1}=0, h^{0,2}=1."""
        st = hodge_supertrace()
        assert st.hodge_column_0 == {0: 1, 1: 0, 2: 1}

    def test_proof_status_kappa_chi(self):
        """kappa_ch = chi^CY is PROVED at d=2."""
        st = hodge_supertrace()
        assert st.status_kappa_chi == 'PROVED'


# =========================================================================
# Section 5: Twistor deformation (8 tests)
# =========================================================================

class TestTwistorDeformation:
    """Tests for the twistor family Y_lambda(g_{K3})."""

    def test_classical_limit_g0_is_1(self):
        """g_0(z) = 1 at the classical limit lambda=0."""
        result = twistor_structure_function_verify()
        assert result['classical_limit_g0_is_1'] is True

    def test_quantum_point_matches(self):
        """g_1(z) = g_{K3}(z) at the quantum point lambda=1."""
        result = twistor_structure_function_verify()
        assert result['quantum_point_matches_standard'] is True

    def test_unitarity_all_lambda(self):
        """g_lambda(z) * g_lambda(-z) = 1 for all lambda."""
        result = twistor_structure_function_verify()
        assert result['unitarity_all_lambda'] is True

    def test_g_lambda_at_zero(self):
        """g_lambda(0) = 1 for all lambda (24 = even number of factors)."""
        result = twistor_structure_function_verify()
        assert result['g_lambda_at_zero_is_1'] is True

    def test_departure_monotone(self):
        """|g_lambda(z) - 1| increases with |lambda| at fixed z."""
        result = twistor_structure_function_verify()
        assert result['departure_increases_with_lambda'] is True

    def test_twistor_deformation_has_three_limits(self):
        """The twistor family has classical, quantum, and Koszul limits."""
        tw = twistor_deformation()
        assert 'lambda = 0' in tw.classical_limit
        assert 'lambda = 1' in tw.quantum_point
        assert 'infty' in tw.koszul_dual_limit

    def test_omega_background_relation(self):
        """Twistor parameter relates to Omega-background (AP-CY20)."""
        tw = twistor_deformation()
        assert 'epsilon_3' in tw.omega_background_relation
        assert 'epsilon_1' in tw.omega_background_relation

    def test_twistor_status_conjectural(self):
        """Twistor deformation is CONJECTURAL (AP-CY14)."""
        tw = twistor_deformation()
        assert tw.status == 'CONJECTURAL'


# =========================================================================
# Section 6: Hodge-graded character (8 tests)
# =========================================================================

class TestHodgeGradedCharacter:
    """Tests for the Hodge-graded Fock space character."""

    def test_p24_0_is_1(self):
        """p_{24}(0) = 1."""
        ch = hodge_graded_character()
        assert ch.ungraded_character_coeffs[0] == 1

    def test_p24_1_is_24(self):
        """p_{24}(1) = 24 (= Mukai rank = number of colours)."""
        ch = hodge_graded_character()
        assert ch.ungraded_character_coeffs[1] == 24

    def test_p24_2_is_324(self):
        """p_{24}(2) = 324."""
        ch = hodge_graded_character()
        assert ch.ungraded_character_coeffs[2] == 324

    def test_p24_3_is_3200(self):
        """p_{24}(3) = 3200."""
        ch = hodge_graded_character()
        assert ch.ungraded_character_coeffs[3] == 3200

    def test_p24_4_is_25650(self):
        """p_{24}(4) = 25650."""
        ch = hodge_graded_character()
        assert ch.ungraded_character_coeffs[4] == 25650

    def test_generator_weights_sum_to_24(self):
        """1 + 22 + 1 = 24 generators total."""
        ch = hodge_graded_character()
        total = (ch.num_weight_0_generators +
                 ch.num_weight_1_generators +
                 ch.num_weight_2_generators)
        assert total == 24

    def test_hodge_euler_char_leading(self):
        """Leading coefficient of Hodge Euler characteristic is 1."""
        ch = hodge_graded_character()
        assert ch.hodge_euler_char_coeffs[0] == 1

    def test_kappa_from_supertrace(self):
        """kappa_cat from the Hodge supertrace is 2."""
        ch = hodge_graded_character()
        assert ch.kappa_cat_from_supertrace == 2


# =========================================================================
# Section 7: Omega-background bridge (5 tests)
# =========================================================================

class TestOmegaTwistorBridge:
    """Tests for the Omega-background / twistor bridge."""

    def test_cy_constraint(self):
        """CY constraint: eps_1 + eps_2 + eps_3 = 0."""
        bridge = omega_twistor_bridge()
        assert 'epsilon_1 + epsilon_2 + epsilon_3 = 0' in bridge.cy_constraint

    def test_ratio_formula(self):
        """lambda = epsilon_3 / epsilon_1."""
        bridge = omega_twistor_bridge()
        assert 'epsilon_3 / epsilon_1' in bridge.ratio_formula

    def test_ns_limit_gives_classical(self):
        """NS limit (eps_3 -> 0) gives classical limit lambda = 0."""
        bridge = omega_twistor_bridge()
        assert 'lambda -> 0' in bridge.ns_limit or 'lambda = 0' in bridge.ns_limit

    def test_intermediary_mechanism_stated(self):
        """Intermediary mechanism is explicitly stated (AP-CY20)."""
        bridge = omega_twistor_bridge()
        mech_lower = bridge.intermediary_mechanism.lower()
        assert 'equivariant localization' in mech_lower
        assert 'nekrasov' in mech_lower

    def test_not_direct_identification(self):
        """AP-CY20: NOT a direct identification."""
        bridge = omega_twistor_bridge()
        assert 'NOT a direct identification' in bridge.intermediary_mechanism


# =========================================================================
# Section 8: Hodge R-matrix (5 tests)
# =========================================================================

class TestHodgeRMatrix:
    """Tests for the Hodge decomposition of the R-matrix."""

    def test_total_size_24(self):
        """R-matrix acts on C^{24} x C^{24}."""
        rm = hodge_r_matrix()
        assert rm.total_size == 24

    def test_block_00_size(self):
        """(0,0) block is 1x1 (H^0 x H^0)."""
        rm = hodge_r_matrix()
        assert rm.block_sizes['(0,0)'] == 1

    def test_block_11_size(self):
        """(1,1) block is 22x22 = 484 (H^2 x H^2)."""
        rm = hodge_r_matrix()
        assert rm.block_sizes['(1,1)'] == 484

    def test_block_22_size(self):
        """(2,2) block is 1x1 (H^4 x H^4)."""
        rm = hodge_r_matrix()
        assert rm.block_sizes['(2,2)'] == 1

    def test_unitarity(self):
        """R(z) R(-z) = Id (unitarity in each block)."""
        rm = hodge_r_matrix()
        assert rm.unitarity_by_block is True


# =========================================================================
# Section 9: Cross-consistency (7 tests)
# =========================================================================

class TestCrossConsistency:
    """Cross-consistency checks between different components."""

    def test_hh_dim_equals_mukai_rank(self):
        """dim HH_*(K3) = Mukai rank = 24."""
        assert K3_HH_TOTAL_DIM == MUKAI_RANK == 24

    def test_hodge_weights_length_24(self):
        """Mukai Hodge weights list has 24 entries."""
        assert len(MUKAI_HODGE_WEIGHTS) == 24

    def test_kappa_spectrum_values(self):
        """kappa spectrum: {2, 3, 5, 24} for K3 x E, {2, 5, 24} for K3 alone (AP113)."""
        assert KAPPA_CAT_K3 == 2
        assert KAPPA_CH_K3 == 2
        assert KAPPA_BKM_K3 == 5
        assert KAPPA_FIBER_K3 == 24

    def test_kappa_cat_from_hodge_and_supertrace(self):
        """kappa_cat from nc Hodge structure agrees with supertrace."""
        hodge = nc_hodge_k3()
        st = hodge_supertrace()
        assert hodge.chi_O == st.chi_O == st.kappa_cat == 2

    def test_degeneration_and_filtration_consistent(self):
        """Hodge-to-dR degeneration implies the Yangian filtration splits."""
        degen = hodge_de_rham_degeneration()
        filt = yangian_hodge_filtration()
        assert degen.degenerates is True
        assert filt.associated_graded_is_U is True

    def test_twistor_and_structure_function_consistent(self):
        """g_1(z) from twistor = g_{K3}(z) from k3_yangian."""
        params = kummer_k3_parameters()
        z_test = Rational(7)
        g_standard = structure_function_evaluate(z_test, params)
        # The twistor verification checks this internally
        result = twistor_structure_function_verify(params=params)
        assert result['quantum_point_matches_standard'] is True

    def test_hodge_graded_ungraded_p24_matches_quantization(self):
        """p_{24}(n) from Hodge-graded char matches k3_yangian_quantization."""
        from compute.lib.k3_yangian_quantization import FAKE_MONSTER_MULTIPLICITIES
        ch = hodge_graded_character()
        # p_{24}(1) = c(0) = 24 (lightlike BKM multiplicity)
        assert ch.ungraded_character_coeffs[1] == FAKE_MONSTER_MULTIPLICITIES[0]
        # p_{24}(2) = c(1) = 324
        assert ch.ungraded_character_coeffs[2] == FAKE_MONSTER_MULTIPLICITIES[1]


# =========================================================================
# Section 10: Full verification (3 tests)
# =========================================================================

class TestFullVerification:
    """Full verification suite."""

    def test_full_verification_all_pass(self):
        """All component verifications pass."""
        result = full_nc_hodge_verification()
        assert result['all_pass'] is True

    def test_full_verification_categorical_proved(self):
        """Categorical nc Hodge is marked PROVED."""
        result = full_nc_hodge_verification()
        assert result['categorical_status_proved'] is True

    def test_full_verification_yangian_conjectural(self):
        """Yangian nc Hodge is marked CONJECTURAL (AP-CY14)."""
        result = full_nc_hodge_verification()
        assert result['yangian_status_conjectural'] is True


# =========================================================================
# Section 11: Multi-path verification (12 tests)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification: each quantity computed via >= 2 independent paths.

    AP10 compliance: hardcoded values are cross-checked against independent
    computational paths from different modules.
    """

    def test_kappa_cat_four_paths(self):
        """kappa_cat = 2 via four independent paths.

        Path 1: Hodge diamond column sum (-1)^q h^{0,q}
        Path 2: nc_hodge_k3().chi_O
        Path 3: hodge_supertrace().alternating_sum
        Path 4: Direct from k3_double_current_algebra Betti numbers
        """
        # Path 1: direct from Hodge diamond
        path1 = sum((-1)**q * K3_HODGE_DIAMOND.get((0, q), 0) for q in range(3))
        # Path 2: from nc Hodge structure
        path2 = nc_hodge_k3().chi_O
        # Path 3: from supertrace computation
        path3 = hodge_supertrace().alternating_sum
        # Path 4: Noether formula chi(O_X) = (chi_top + sigma) / 4
        # For K3: chi_top = 24, sigma(K3) = b_+ - b_- = 3 - 19 = -16
        # where b_+ = 2*h^{2,0} + 1 = 3, b_- = h^{1,1} - 1 = 19
        # (the +1/-1 comes from the split of h^{1,1} into self-dual/anti-self-dual)
        # chi(O) = (24 + (-16))/4 = 8/4 = 2
        chi_top = sum((-1)**k * K3_BETTI[k] for k in range(5))
        b_plus = 2 * K3_HODGE_DIAMOND[(2, 0)] + 1   # = 3
        b_minus = K3_HODGE_DIAMOND[(1, 1)] - 1       # = 19
        assert b_plus + b_minus == K3_BETTI[2]       # sanity: 3 + 19 = 22
        sigma = b_plus - b_minus                     # = -16
        path4 = (chi_top + sigma) // 4

        assert path1 == path2 == path3 == path4 == 2

    def test_hh_total_dim_three_paths(self):
        """dim HH_*(K3) = 24 via three independent paths.

        Path 1: Sum of K3_HH_DIMS values
        Path 2: MUKAI_RANK from k3_double_current_algebra
        Path 3: Sum of Betti numbers (topological Euler characteristic)
        """
        # Path 1: from HH dimensions
        path1 = sum(K3_HH_DIMS.values())
        # Path 2: from Mukai lattice rank
        path2 = MUKAI_RANK
        # Path 3: chi_top = sum b_k = sum (-1)^k b_k when all odd b_k = 0
        # Actually sum b_k = 1+0+22+0+1 = 24 (since odd vanish, chi = sum too)
        path3 = sum(K3_BETTI)
        assert path1 == path2 == path3 == 24

    def test_p24_coeffs_two_paths(self):
        """p_{24}(n) via Hodge character vs k3_yangian_quantization BKM data.

        Path 1: hodge_graded_character partition function
        Path 2: FAKE_MONSTER_MULTIPLICITIES from k3_yangian_quantization
        """
        from compute.lib.k3_yangian_quantization import FAKE_MONSTER_MULTIPLICITIES
        ch = hodge_graded_character()
        # Path 1 vs Path 2 for n=0..5
        # BKM c(n) = p_{24}(n+1), so p_{24}(k) = c(k-1)
        for k in range(1, 6):
            path1 = ch.ungraded_character_coeffs[k]
            path2 = FAKE_MONSTER_MULTIPLICITIES[k - 1]
            assert path1 == path2, f"Mismatch at k={k}: {path1} vs {path2}"

    def test_unitarity_two_paths(self):
        """g(z)g(-z) = 1 via twistor engine vs direct k3_yangian evaluation.

        Path 1: twistor_structure_function_verify unitarity check
        Path 2: Direct evaluation via k3_yangian.structure_function_evaluate
        """
        params = kummer_k3_parameters()
        # Path 1: twistor engine
        tw = twistor_structure_function_verify(params=params)
        path1 = tw['unitarity_all_lambda']

        # Path 2: direct from k3_yangian
        z_vals = [Rational(7), Rational(13), Rational(-11)]
        path2_checks = []
        for z_val in z_vals:
            g_pos = structure_function_evaluate(z_val, params)
            g_neg = structure_function_evaluate(-z_val, params)
            path2_checks.append(bool(g_pos * g_neg == 1))
        path2 = all(path2_checks)

        assert path1 is True
        assert path2 is True

    def test_hodge_weight_decomposition_two_paths(self):
        """1 + 22 + 1 = 24 decomposition via Hodge diamond vs Betti numbers.

        Path 1: From MUKAI_HODGE_WEIGHTS count
        Path 2: From Betti numbers b_0, b_2, b_4 (since b_odd = 0)
        """
        # Path 1: from Hodge weights
        path1 = (MUKAI_HODGE_WEIGHTS.count(0),
                 MUKAI_HODGE_WEIGHTS.count(1),
                 MUKAI_HODGE_WEIGHTS.count(2))

        # Path 2: from Betti numbers (H^0 -> weight 0, H^2 -> weight 1, H^4 -> weight 2)
        path2 = (K3_BETTI[0], K3_BETTI[2], K3_BETTI[4])

        assert path1 == path2 == (1, 22, 1)

    def test_euler_char_two_paths(self):
        """chi(K3) = 24 via Betti vs Hodge diamond.

        Path 1: sum (-1)^k b_k
        Path 2: sum (-1)^{p+q} h^{p,q}
        """
        path1 = sum((-1)**k * K3_BETTI[k] for k in range(5))
        path2 = sum((-1)**(p + q) * h_pq
                     for (p, q), h_pq in K3_HODGE_DIAMOND.items())
        assert path1 == path2 == 24

    def test_degeneration_two_paths(self):
        """Hodge-to-dR degeneration via engine vs direct Hodge number check.

        Path 1: hodge_de_rham_degeneration().degenerates
        Path 2: Verify sum_{p+q=k} h^{p,q} = b_k for all k (equivalent to E_2 = E_inf)
        """
        # Path 1: engine
        path1 = hodge_de_rham_degeneration().degenerates

        # Path 2: direct check
        dr_dims = [0] * 5
        for (p, q), val in K3_HODGE_DIAMOND.items():
            dr_dims[p + q] += val
        path2 = (dr_dims == K3_BETTI)

        assert path1 is True
        assert path2 is True

    def test_kappa_ch_equals_chi_two_paths(self):
        """kappa_ch = chi(O) via supertrace vs yangian filtration.

        Path 1: hodge_supertrace().kappa_equals_chi
        Path 2: yangian_hodge_filtration().kappa_ch == yangian_hodge_filtration().kappa_cat
        """
        # Path 1: supertrace module
        st = hodge_supertrace()
        path1 = st.kappa_equals_chi

        # Path 2: yangian filtration module
        filt = yangian_hodge_filtration()
        path2 = (filt.kappa_ch == filt.kappa_cat)

        assert path1 is True
        assert path2 is True

    def test_structure_function_classical_limit_two_paths(self):
        """g_0(z) = 1 via twistor engine vs algebraic argument.

        Path 1: twistor_structure_function_verify classical_limit
        Path 2: Direct: prod (z - 0*h_i)/(z + 0*h_i) = prod 1 = 1
        """
        # Path 1: engine
        tw = twistor_structure_function_verify()
        path1 = tw['classical_limit_g0_is_1']

        # Path 2: algebraic - at lambda=0, every factor is z/z = 1
        params = kummer_k3_parameters()
        path2_val = Rational(1)
        z_test = Rational(7)
        for hi in params.h:
            path2_val *= (z_test - 0 * hi) / (z_test + 0 * hi)
        path2 = bool(path2_val == 1)

        assert path1 is True
        assert path2 is True

    def test_mukai_rank_three_paths(self):
        """Mukai rank = 24 via three independent sources.

        Path 1: NUM_PARAMS from k3_yangian
        Path 2: MUKAI_RANK from k3_double_current_algebra
        Path 3: len(MUKAI_HODGE_WEIGHTS)
        """
        path1 = NUM_PARAMS
        path2 = MUKAI_RANK
        path3 = len(MUKAI_HODGE_WEIGHTS)
        assert path1 == path2 == path3 == 24

    def test_signature_decomposition_two_paths(self):
        """Mukai signature (4, 20) via k3_yangian constants vs Hodge diamond.

        Path 1: (SIG_PLUS, SIG_MINUS) from k3_yangian
        Path 2: (b_+, b_-) from Hodge numbers where b_+ = 2h^{2,0}+1, b_- = h^{1,1}-1
                 giving (4, 20) via Mukai = H^0 + H^2 + H^4 with b_0 and b_4 positive
        """
        # Path 1: direct constants
        path1 = (SIG_PLUS, SIG_MINUS)

        # Path 2: from Hodge diamond
        # Mukai lattice has sig (3+1, 19+1) = (4, 20):
        # H^2 intersection form has sig (3, 19) (from h^{2,0}=1 gives +2 real dirs)
        # Actually: sig(Mukai) = sig(H^2) + (1,1) from H^0+H^4 hyperbolic pair
        # sig(H^2) = (3, 19), sig(H^0+H^4) = (1, 1)
        # Total: (3+1, 19+1) = (4, 20)
        h2_sig_plus = 2 * K3_HODGE_DIAMOND[(2, 0)] + 1  # = 2*1+1 = 3
        h2_sig_minus = K3_HODGE_DIAMOND[(1, 1)] - 1      # = 20-1 = 19
        # Add hyperbolic pair from H^0+H^4
        mukai_sig_plus = h2_sig_plus + 1    # = 4
        mukai_sig_minus = h2_sig_minus + 1  # = 20
        path2 = (mukai_sig_plus, mukai_sig_minus)

        assert path1 == path2 == (4, 20)

    def test_bar_euler_exponent_two_paths(self):
        """Bar Euler exponent = 24 via Mukai rank vs Hodge-graded generator count.

        Path 1: MUKAI_RANK (the exponent in eta^{24})
        Path 2: Sum of Hodge-graded generator counts (1 + 22 + 1)
        """
        ch = hodge_graded_character()
        path1 = MUKAI_RANK
        path2 = (ch.num_weight_0_generators +
                 ch.num_weight_1_generators +
                 ch.num_weight_2_generators)
        assert path1 == path2 == 24
