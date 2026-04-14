r"""Tests for the explicit evaluation of Phi on D^b(Coh(K3)).

Verifies: Phi(D^b(Coh(K3))) = H_{Muk} (rank-24 Heisenberg at Mukai pairing).

Theorem used: CY-A_2 (PROVED at d=2).
Manuscript: Theorem thm:phi-k3-explicit in cy_to_chiral.tex.
Engine: compute/lib/phi_k3_explicit_evaluation.py.

AP113 compliance: all kappa references subscripted (kappa_ch, kappa_cat, kappa_fiber).
AP-CY2 compliance: CY trace in HC^-_2, not just HH_2 -> k.
AP-CY6 compliance: d=2, Phi IS constructed.
"""

from fractions import Fraction

import pytest

from compute.lib.phi_k3_explicit_evaluation import (
    # Step 1
    step1_hkr_computation,
    verify_hkr_dimensions,
    # Step 2
    step2_gerstenhaber_bracket,
    # Step 3
    step3_s2_framing,
    # Step 4
    step4_quantization,
    # kappa
    verify_kappa_ch,
    # Full evaluation
    evaluate_phi_on_k3,
    # Cross-checks
    cross_check_with_k3_dca,
    cross_check_character,
    cross_check_formality,
    kummer_route_comparison,
    evaluate_phi_on_abelian_surface,
    full_verification,
    # Constants
    EXPECTED_RANK,
    EXPECTED_SIG,
    EXPECTED_KAPPA_CH,
    EXPECTED_SHADOW_CLASS,
)

F = Fraction


# =========================================================================
# Step 1: HKR decomposition
# =========================================================================

class TestStep1HKR:
    """Tests for HH_*(D^b(Coh(K3))) via HKR."""

    def test_hh_dimensions(self):
        """HH_{-2}=1, HH_{-1}=0, HH_0=22, HH_1=0, HH_2=1."""
        result = step1_hkr_computation()
        assert result.hh_dims.get(-2, 0) == 1
        assert result.hh_dims.get(-1, 0) == 0
        assert result.hh_dims.get(0, 0) == 22
        assert result.hh_dims.get(1, 0) == 0
        assert result.hh_dims.get(2, 0) == 1

    def test_total_dimension_24(self):
        """Total dim HH_*(K3) = 24 = dim H^*(K3, C)."""
        result = step1_hkr_computation()
        assert result.total_dim == 24

    def test_generator_count(self):
        """24 generators for the output chiral algebra."""
        result = step1_hkr_computation()
        assert result.generator_count == 24

    def test_odd_hh_vanishes(self):
        """HH_{odd} = 0 since K3 is simply connected."""
        result = step1_hkr_computation()
        assert result.hh_dims.get(-1, 0) == 0
        assert result.hh_dims.get(1, 0) == 0

    def test_serre_duality(self):
        """HH_n = HH_{d-n} for d=2: HH_{-2} = HH_2, HH_{-1} = HH_1."""
        result = step1_hkr_computation()
        assert result.hh_dims.get(-2, 0) == result.hh_dims.get(2, 0)
        assert result.hh_dims.get(-1, 0) == result.hh_dims.get(1, 0)

    def test_hkr_hodge_decomposition_hh0(self):
        """HH_0 = h^{0,2} + h^{1,1} + h^{2,0} = 1 + 20 + 1 = 22."""
        result = step1_hkr_computation()
        # HH_0 contributions: from (p,q) with q-p=0
        hh0_pieces = result.hodge_decomposition.get(0, [])
        # Should have three contributions summing to 22
        total = sum(piece[2] for piece in hh0_pieces)
        assert total == 22

    def test_multi_path_verification(self):
        """All four verification paths pass."""
        check = verify_hkr_dimensions()
        assert check['path1_direct_hkr']
        assert check['path2_betti_sum']
        assert check['path3_odd_vanishing']
        assert check['path4_serre_duality']
        assert check['all_pass']


# =========================================================================
# Step 2: Gerstenhaber bracket
# =========================================================================

class TestStep2Gerstenhaber:
    """Tests for the Lie conformal algebra being abelian."""

    def test_lie_conformal_abelian(self):
        """L_C is abelian for C = D^b(Coh(K3))."""
        result = step2_gerstenhaber_bracket()
        assert result.lie_conformal_is_abelian

    def test_no_global_vector_fields(self):
        """H^0(T_{K3}) = 0 (h^{1,0} = 0)."""
        result = step2_gerstenhaber_bracket()
        assert result.hh1_dim == 0

    def test_bracket_trivial(self):
        """Bracket type is trivial."""
        result = step2_gerstenhaber_bracket()
        assert result.bracket_type == 'trivial'


# =========================================================================
# Step 3: S^2-framing
# =========================================================================

class TestStep3Framing:
    """Tests for the S^2-framing and E_2 enhancement."""

    def test_cy_dimension(self):
        """CY dimension is 2."""
        result = step3_s2_framing()
        assert result.cy_dim == 2

    def test_framing_sphere(self):
        """Framing sphere is S^2."""
        result = step3_s2_framing()
        assert result.framing_sphere_dim == 2

    def test_operadic_level_e2(self):
        """Output is E_2-chiral algebra."""
        result = step3_s2_framing()
        assert result.operadic_level == 'E_2'

    def test_cy_trace_in_negative_cyclic(self):
        """CY trace lives in HC^-_2, not just HH_2 (AP-CY2)."""
        result = step3_s2_framing()
        assert result.cy_trace_target == 'HC^-_2'

    def test_produces_free_field(self):
        """Abelian L_C produces free-field theory."""
        result = step3_s2_framing()
        assert result.produces_free_field


# =========================================================================
# Step 4: Quantization
# =========================================================================

class TestStep4Quantization:
    """Tests for the output being H_{Muk}."""

    def test_output_is_heisenberg(self):
        """Output algebra is H_{Muk}."""
        result = step4_quantization()
        assert result.output_algebra == 'H_{Muk}'

    def test_rank_24(self):
        """Rank of H_{Muk} is 24."""
        result = step4_quantization()
        assert result.rank == 24

    def test_mukai_signature(self):
        """Mukai pairing has signature (4, 20)."""
        result = step4_quantization()
        assert result.pairing_signature == (4, 20)

    def test_mukai_pairing_type(self):
        """Pairing is of Mukai type."""
        result = step4_quantization()
        assert result.pairing_type == 'Mukai'

    def test_free_field(self):
        """H_{Muk} is a free-field algebra."""
        result = step4_quantization()
        assert result.is_free_field

    def test_shadow_class_G(self):
        """Shadow class is G (Gaussian)."""
        result = step4_quantization()
        assert result.shadow_class == 'G'


# =========================================================================
# kappa_ch verification
# =========================================================================

class TestKappaCh:
    """Tests for kappa_ch(Phi(D^b(Coh(K3)))) = chi(O_{K3}) = 2.

    AP113: all kappa subscripted.
    """

    def test_kappa_ch_equals_2(self):
        """kappa_ch = 2."""
        result = verify_kappa_ch()
        assert result.kappa_ch == F(2)

    def test_chi_O_K3_equals_2(self):
        """chi(O_{K3}) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        result = verify_kappa_ch()
        assert result.chi_O_K3 == 2

    def test_kappa_ch_matches_chi_O(self):
        """kappa_ch = chi(O_{K3}): the proved identification."""
        result = verify_kappa_ch()
        assert result.match

    def test_kappa_cat_equals_kappa_ch(self):
        """For K3: kappa_cat = kappa_ch = 2."""
        result = verify_kappa_ch()
        assert result.kappa_cat == result.kappa_ch

    def test_kappa_fiber_is_24(self):
        """kappa_fiber = 24 (lattice rank, distinct from kappa_ch)."""
        result = verify_kappa_ch()
        assert result.kappa_fiber == 24

    def test_kappa_ch_not_24(self):
        """kappa_ch != 24 (common confusion with kappa_fiber)."""
        result = verify_kappa_ch()
        assert result.kappa_ch != F(24)

    def test_kappa_ch_not_3(self):
        """kappa_ch(K3) != 3 (that is kappa_ch(K3 x E) = 2 + 1)."""
        result = verify_kappa_ch()
        assert result.kappa_ch != F(3)


# =========================================================================
# Full evaluation
# =========================================================================

class TestFullEvaluation:
    """Tests for the complete evaluation Phi(D^b(Coh(K3))) = H_{Muk}."""

    def test_all_steps_verified(self):
        """All four steps pass verification."""
        result = evaluate_phi_on_k3()
        assert result.all_steps_verified

    def test_output_algebra(self):
        """Output is H_{Muk}."""
        result = evaluate_phi_on_k3()
        assert result.output_algebra == 'H_{Muk}'

    def test_output_rank(self):
        """Output rank is 24."""
        result = evaluate_phi_on_k3()
        assert result.output_rank == EXPECTED_RANK

    def test_output_signature(self):
        """Output signature is (4, 20)."""
        result = evaluate_phi_on_k3()
        assert result.output_signature == EXPECTED_SIG


# =========================================================================
# Cross-checks
# =========================================================================

class TestCrossChecks:
    """Cross-checks against existing engines."""

    def test_k3_dca_rank(self):
        """Rank matches k3_double_current_algebra.py."""
        check = cross_check_with_k3_dca()
        assert check['rank_match']

    def test_k3_dca_signature(self):
        """Signature matches k3_double_current_algebra.py."""
        check = cross_check_with_k3_dca()
        assert check['sig_match']

    def test_k3_dca_shadow_class(self):
        """Shadow class matches k3_double_current_algebra.py."""
        check = cross_check_with_k3_dca()
        assert check['shadow_class_match']

    def test_character_partition_numbers(self):
        """Character coefficients 1, 24, 324, 3200, 25650."""
        check = cross_check_character()
        assert check['partition_match']

    def test_bar_euler_ramanujan_tau(self):
        """Bar Euler product gives Ramanujan tau: 1, -24, 252, -1472, 4830."""
        check = cross_check_character()
        assert check['bar_euler_match']

    def test_character_all_match(self):
        """All character cross-checks pass."""
        check = cross_check_character()
        assert check['all_match']

    def test_formality(self):
        """K3 is formal (DGMS): Massey products vanish."""
        check = cross_check_formality()
        assert check['dgms_applies']
        assert check['massey_products_vanish']
        assert check['shadow_class'] == 'G'
        assert check['shadow_depth'] == 2

    def test_kummer_route_agreement(self):
        """Phi evaluation agrees with Kummer route construction."""
        check = kummer_route_comparison()
        assert check['rank_match']
        assert check['pairing_match']
        assert check['kappa_ch_match']
        assert check['character_match']


# =========================================================================
# Abelian surface comparison
# =========================================================================

class TestAbelianSurface:
    """Cross-check: Phi on abelian surface A gives kappa_ch = 0."""

    def test_abelian_total_dim_16(self):
        """dim H^*(A, C) = 16 for abelian surface."""
        result = evaluate_phi_on_abelian_surface()
        assert result.total_dim == 16

    def test_abelian_kappa_ch_zero(self):
        """kappa_ch(A) = chi(O_A) = 0 for abelian surface."""
        result = evaluate_phi_on_abelian_surface()
        assert result.kappa_ch == F(0)

    def test_abelian_chi_O_zero(self):
        """chi(O_A) = 1 - 2 + 1 = 0."""
        result = evaluate_phi_on_abelian_surface()
        assert result.chi_O_A == 0

    def test_abelian_hh_dimensions(self):
        """HH dimensions for abelian surface: (1, 4, 6, 4, 1)."""
        result = evaluate_phi_on_abelian_surface()
        assert result.hh_dims.get(-2, 0) == 1
        assert result.hh_dims.get(-1, 0) == 4
        assert result.hh_dims.get(0, 0) == 6
        assert result.hh_dims.get(1, 0) == 4
        assert result.hh_dims.get(2, 0) == 1

    def test_abelian_shadow_class_G(self):
        """Abelian surface is formal => shadow class G."""
        result = evaluate_phi_on_abelian_surface()
        assert result.shadow_class == 'G'


# =========================================================================
# Master verification
# =========================================================================

class TestMasterVerification:
    """Full 8-path verification."""

    def test_all_paths_pass(self):
        """All 8 verification paths pass."""
        result = full_verification()
        assert result['all_pass']

    def test_path1_hkr(self):
        result = full_verification()
        assert result['verification_paths']['path1_hkr']

    def test_path2_abelian_lca(self):
        result = full_verification()
        assert result['verification_paths']['path2_abelian_lca']

    def test_path3_kappa_ch(self):
        result = full_verification()
        assert result['verification_paths']['path3_kappa_ch']

    def test_path4_character(self):
        result = full_verification()
        assert result['verification_paths']['path4_character']

    def test_path5_kummer(self):
        result = full_verification()
        assert result['verification_paths']['path5_kummer']

    def test_path6_dca_cross(self):
        result = full_verification()
        assert result['verification_paths']['path6_dca_cross']

    def test_path7_formality(self):
        result = full_verification()
        assert result['verification_paths']['path7_formality']

    def test_path8_abelian_surface(self):
        result = full_verification()
        assert result['verification_paths']['path8_abelian_surface']

    def test_summary_content(self):
        """Summary records the correct theorem."""
        result = full_verification()
        s = result['summary']
        assert s['kappa_ch'] == 2
        assert s['kappa_cat'] == 2
        assert s['kappa_fiber'] == 24
        assert s['shadow_class'] == 'G'
        assert s['operadic_level'] == 'E_2'
        assert 'CY-A_2' in s['theorem_used']
        assert 'PROVED' in s['theorem_used']
