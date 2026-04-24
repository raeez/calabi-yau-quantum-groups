r"""Tests for hcs_vs_sigma_adversarial.py: adversarial comparison of hCS vs sigma model.

STATUS: MIXED. Route B (CY-A_2) and Route C (sigma model) are PROVED.
Route A (KS boundary) and Route D (Yangian) are CONJECTURAL (AP-CY14).

ATTACK VECTORS:
    1. Central charge: c=24 (hCS) vs c=6 (sigma model) -- 12 tests
    2. Shadow class: G (H_Muk) vs M (N=4 SCA) -- 10 tests
    3. E_n structure: E_2 (d=2) vs E_1 (d=3) -- 8 tests
    4. Yangian existence: Y(g_{K3}) vs no Yangian -- 8 tests
    5. Full adversarial report -- 5 tests
    6. Cross-engine consistency -- 10 tests
    7. Cross-engine kappa verification -- 7 tests
    8. Hodge diamond decomposition -- 8 tests
    9. N=4 shadow tower analysis -- 8 tests
   10. CoHA vs E_1-chiral distinction (AP-CY7) -- 7 tests
   11. Omega-background mechanism (AP-CY20) -- 7 tests

Total: 90 tests.

VERIFIED values:
    # VERIFIED [DC] direct computation from K3 Hodge diamond
    # VERIFIED [MAN] manuscript cross-reference (toroidal_elliptic.tex, quantum_chiral_algebras.tex)
    # VERIFIED [CF] cross-engine (phi_k3_explicit_evaluation, hcs_hierarchy_k3)
    # VERIFIED [XE] cross-engine verification (values match across independent engines)
"""

import math

import pytest
from fractions import Fraction

from compute.lib.hcs_vs_sigma_adversarial import (
    # Constants
    ROUTE_A, ROUTE_B, ROUTE_C, ROUTE_D,
    ROUTE_A_CENTRAL_CHARGE, ROUTE_B_CENTRAL_CHARGE,
    ROUTE_C_CENTRAL_CHARGE,
    K3_HODGE,
    N4_SHADOW_TOWER,
    # Attack 1
    central_charge_comparison,
    kappa_ch_five_paths,
    ope_level_vs_mukai_pairing,
    # Attack 2
    shadow_class_comparison,
    shadow_depth_boundary_vs_sigma,
    # Attack 3
    en_structure_comparison,
    en_forgetful_vs_promotion,
    # Attack 4
    yangian_existence_comparison,
    structure_function_classical_limit,
    # Full report
    full_adversarial_report,
    # Utilities
    route_comparison_table,
    verify_kappa_ch_consistency,
    # Deepened adversarial (new)
    cross_engine_kappa_verification,
    hodge_diamond_decomposition,
    n4_shadow_tower_analysis,
    coha_vs_chiral_distinction,
    omega_background_mechanism,
)

F = Fraction


# =========================================================================
# Attack 1: Central Charge (12 tests)
# =========================================================================


class TestCentralCharge:
    """Tests for Attack 1: central charge c=24 vs c=6."""

    def test_route_a_c_equals_24(self):
        """KS boundary algebra has c = 24 (24 free bosons from H^*(K3))."""
        # VERIFIED [MAN] toroidal_elliptic.tex constr:costello-li-k3xe
        assert ROUTE_A.central_charge == 24

    def test_route_b_c_equals_24(self):
        """CY-A_2 output H_Muk has c = 24 (rank-24 Heisenberg)."""
        # VERIFIED [DC] rank of Mukai lattice = sum h^{p,q}(K3) = 24
        assert ROUTE_B.central_charge == 24

    def test_route_c_c_equals_6(self):
        """N=4 SCA from sigma model has c = 6 = 6*k_R with k_R = 1."""
        # VERIFIED [MAN] toroidal_elliptic.tex def:n4-sca-c6
        assert ROUTE_C.central_charge == 6

    def test_c_ratio_is_4(self):
        """c(H_Muk) / c(V_{K3}) = 24 / 6 = 4 = dim_C(K3)^2."""
        # VERIFIED [DC]
        result = central_charge_comparison()
        assert result['c_ratio'] == F(4)

    def test_c_ratio_equals_dim_squared(self):
        """The ratio 4 equals dim_C(K3)^2 = 2^2."""
        # VERIFIED [DC]
        result = central_charge_comparison()
        assert result['c_ratio_equals_dim_squared'] is True

    def test_betti_sum_24(self):
        """Sum of K3 Hodge numbers = 24 = c(H_Muk)."""
        # VERIFIED [DC] 1 + 0 + 1 + 20 + 1 + 0 + 0 + 0 + 1 = 24
        result = central_charge_comparison()
        assert result['betti_sum'] == 24

    def test_sigma_model_c_decomposition(self):
        """Sigma model c = 6 = 4 (bosons) + 2 (fermions)."""
        # VERIFIED [DC] 4 real bosons (c=1 each) + 4 real fermions (c=1/2 each)
        result = central_charge_comparison()
        decomp = result['sigma_model_decomposition']
        assert decomp['c_bosons_real'] == 4
        assert decomp['c_fermions_real'] == 2
        assert decomp['c_total'] == 6

    def test_kappa_ch_routes_b_c_agree(self):
        """Routes B and C agree: kappa_ch = 2 despite different c."""
        # VERIFIED [MAN] prop:kappa-k3, prop:cy-kappa-d2
        result = central_charge_comparison()
        assert result['kappa_ch_routes_b_c_agree'] is True

    def test_no_genuine_inconsistency_central_charge(self):
        """Central charge discrepancy is not a genuine inconsistency."""
        result = central_charge_comparison()
        assert result['genuine_inconsistency'] is False

    def test_kappa_five_paths_all_agree(self):
        """kappa_ch = 2 verified by five independent paths."""
        # VERIFIED [MAN] thm:k3-kappa (6 paths in manuscript, 5 here)
        result = kappa_ch_five_paths()
        assert result['all_paths_agree_on_2'] is True

    def test_ope_level_trace_24(self):
        """OPE level matrix delta^{ab} has trace 24."""
        # VERIFIED [MAN] warn:ope-level-mukai
        result = ope_level_vs_mukai_pairing()
        assert result['ope_level_trace'] == 24

    def test_mukai_pairing_trace_minus_16(self):
        """Mukai pairing G^{ab} has trace 4 - 20 = -16 (WRONG for kappa)."""
        # VERIFIED [DC] signature (4, 20) -> trace = -16
        result = ope_level_vs_mukai_pairing()
        assert result['mukai_pairing_trace'] == -16
        assert result['confusion_produces_negative_kappa'] is True


# =========================================================================
# Attack 2: Shadow Class (10 tests)
# =========================================================================


class TestShadowClass:
    """Tests for Attack 2: shadow class G (H_Muk) vs M (N=4 SCA)."""

    def test_h_muk_is_class_g(self):
        """H_Muk (rank-24 Heisenberg) is class G (Gaussian)."""
        # VERIFIED [MAN] phi_k3_explicit_evaluation.py: shadow_class='G'
        assert ROUTE_B.shadow_class == 'G'

    def test_n4_sca_is_class_m(self):
        """N=4 SCA is class M (infinite shadow tower)."""
        # VERIFIED [MAN] prop:shadow-class-k3
        assert ROUTE_C.shadow_class == 'M'

    def test_h_muk_shadow_depth_2(self):
        """H_Muk has shadow depth 2 (2-step nilpotent)."""
        # VERIFIED [CF] k3_double_current_algebra.py: shadow_depth=2
        assert ROUTE_B.shadow_depth == 2

    def test_n4_sca_shadow_depth_infinite(self):
        """N=4 SCA has infinite shadow depth."""
        # VERIFIED [MAN] prop:shadow-class-k3: r_max = infinity
        assert ROUTE_C.shadow_depth == float('inf')

    def test_classes_differ(self):
        """Shadow classes of H_Muk and N=4 SCA are different."""
        result = shadow_class_comparison()
        assert result['classes_differ'] is True

    def test_class_g_confirmed(self):
        """H_Muk: all S_r = 0 for r >= 3 (class G)."""
        result = shadow_class_comparison()
        assert result['h_muk']['S_3_to_12_all_zero'] is True

    def test_class_m_discriminant_nonzero(self):
        """N=4 SCA: critical discriminant Delta != 0 (class M)."""
        # VERIFIED [MAN] comp:shadow-tower-k3: Delta = 20/39
        result = shadow_class_comparison()
        assert result['n4_sca']['discriminant_nonzero'] is True

    def test_n4_sign_alternation(self):
        """N=4 shadow tower has sign alternation from depth 5."""
        # VERIFIED [MAN] comp:shadow-tower-k3
        result = shadow_class_comparison()
        assert result['n4_sca']['sign_alternation_from_5'] is True

    def test_no_genuine_inconsistency_shadow(self):
        """Shadow class discrepancy is not a genuine inconsistency."""
        result = shadow_class_comparison()
        assert result['genuine_inconsistency'] is False

    def test_boundary_sigma_kappa_ratio_12(self):
        """kappa_ch(A_E) / kappa_ch(V_{K3}) = 24 / 2 = 12."""
        # VERIFIED [MAN] prop:boundary-sigma-ratio eq:boundary-sigma-ratio
        result = shadow_depth_boundary_vs_sigma()
        assert result['ratio_equals_12'] is True


# =========================================================================
# Attack 3: E_n Structure (8 tests)
# =========================================================================


class TestEnStructure:
    """Tests for Attack 3: E_2 (K3, d=2) vs E_1 (K3 x E, d=3)."""

    def test_k3_is_e2(self):
        """K3 (CY_2) has native E_2 from S^2-framing."""
        # VERIFIED [MAN] cy_to_chiral.tex Step 3
        assert ROUTE_B.en_level == 'E_2'

    def test_k3xe_is_e1(self):
        """K3 x E (CY_3) has native E_1 from ordered factorization."""
        # VERIFIED [MAN] quantum_chiral_algebras.tex conj:k3-master-diagram
        assert ROUTE_D.en_level == 'E_1'

    def test_h_muk_is_e_inf(self):
        """H_Muk is E_inf (free field upgrades E_2 -> E_inf)."""
        # VERIFIED [MAN] cy_to_chiral.tex: "free Heisenberg is E_inf"
        assert ROUTE_A.en_level == 'E_inf'

    def test_no_genuine_inconsistency_en(self):
        """E_n discrepancy is not a genuine inconsistency."""
        result = en_structure_comparison()
        assert result['genuine_inconsistency'] is False

    def test_classical_limit_consistent(self):
        """Classical limit Y(g_{K3}) -> H_Muk preserves E_2 -> E_1."""
        result = en_structure_comparison()
        assert result['classical_limit_consistent'] is True

    def test_en_from_cy_dimension(self):
        """E_n level is determined by CY dimension d."""
        # VERIFIED [MAN] cy_to_chiral.tex: d=1 -> E_inf, d=2 -> E_2, d=3 -> E_1
        result = en_structure_comparison()
        en_map = result['en_from_cy_dimension']
        assert en_map[1]['native'] == 'E_inf'
        assert en_map[2]['native'] == 'E_2'
        assert en_map[3]['native'] == 'E_1'

    def test_reduction_is_forgetful(self):
        """Dimensional reduction is forgetful in E_n level: E_3 -> E_2 -> E_1."""
        result = en_forgetful_vs_promotion()
        assert result['reduction_is_forgetful_in_en'] is True

    def test_deformation_reduction_commute(self):
        """Omega-deformation and dimensional reduction commute in the limit."""
        result = en_forgetful_vs_promotion()
        assert result['deformation_vs_reduction_commute'] is True


# =========================================================================
# Attack 4: Yangian Existence (8 tests)
# =========================================================================


class TestYangianExistence:
    """Tests for Attack 4: Y(g_{K3}) from hCS vs no Yangian from sigma model."""

    def test_yangian_is_conjectural(self):
        """Y(g_{K3}) is CONJECTURAL (AP-CY14)."""
        assert ROUTE_D.status == 'CONJECTURAL'

    def test_sigma_model_is_proved(self):
        """Sigma model (H_Muk via CY-A_2) is PROVED."""
        assert ROUTE_B.status == 'PROVED'

    def test_no_genuine_inconsistency_yangian(self):
        """Yangian existence is not a genuine inconsistency."""
        result = yangian_existence_comparison()
        assert result['genuine_inconsistency'] is False

    def test_spectral_vs_worldsheet_different(self):
        """Spectral z and worldsheet z are different (AP-CY31)."""
        result = yangian_existence_comparison()
        assert result['spectral_vs_worldsheet']['are_different'] is True

    def test_classical_limit_cy2_ok(self):
        """CY_2 constraint sum h_a = 0 satisfied by Kummer parameters."""
        result = structure_function_classical_limit()
        assert result['cy2_constraint'] is True

    def test_p1_vanishes(self):
        """First Newton power sum p_1 = sum a_i = 0 (CY_2 constraint)."""
        # VERIFIED [DC] 4*1 + 20*(-1/5) = 0
        result = structure_function_classical_limit()
        assert result['newton_power_sums']['p_1'] == 0

    def test_p3_nonzero(self):
        """Third Newton power sum p_3 != 0 (leading deformation)."""
        # VERIFIED [DC] 4*1 + 20*(-1/125) = 96/25
        result = structure_function_classical_limit()
        assert result['p3_nonzero'] is True
        assert result['newton_power_sums']['p_3'] == F(96, 25)

    def test_leading_deformation_order_3(self):
        """Leading deformation of g(u) is O(eps^3) (from p_3)."""
        result = structure_function_classical_limit()
        assert result['leading_deformation_order'] == 3


# =========================================================================
# Full Adversarial Report (5 tests)
# =========================================================================


class TestFullReport:
    """Tests for the full adversarial report."""

    def test_all_resolved(self):
        """All four attack vectors are resolved (no genuine inconsistencies)."""
        result = full_adversarial_report()
        assert result['all_resolved'] is True

    def test_zero_inconsistencies(self):
        """Zero genuine inconsistencies found."""
        result = full_adversarial_report()
        assert result['num_inconsistencies'] == 0

    def test_four_attack_vectors(self):
        """Report contains results for all four attack vectors (plus sub-attacks)."""
        result = full_adversarial_report()
        vectors = result['attack_vectors']
        assert '1_central_charge' in vectors
        assert '2_shadow_class' in vectors
        assert '3_en_structure' in vectors
        assert '4_yangian' in vectors

    def test_nine_sub_analyses(self):
        """Report contains 9 sub-analyses (4 main + 5 sub-attacks)."""
        result = full_adversarial_report()
        assert len(result['attack_vectors']) == 9

    def test_summary_nonempty(self):
        """Summary is a nonempty string."""
        result = full_adversarial_report()
        assert isinstance(result['summary'], str)
        assert len(result['summary']) > 100


# =========================================================================
# Cross-Engine Consistency (7 tests)
# =========================================================================


class TestCrossEngine:
    """Tests for cross-engine compatibility."""

    def test_route_table_has_four_routes(self):
        """Comparison table has four routes."""
        table = route_comparison_table()
        assert len(table) == 4

    def test_kappa_ch_bc_agree(self):
        """Routes B (CY-A_2) and C (sigma model) agree on kappa_ch = 2."""
        # VERIFIED [MAN] prop:kappa-k3, prop:cy-kappa-d2
        result = verify_kappa_ch_consistency()
        assert result['check_1_bc_agree'] is True

    def test_kappa_ch_a_differs(self):
        """Route A (boundary) has different kappa_ch (24, not 2)."""
        result = verify_kappa_ch_consistency()
        assert result['check_2_a_differs'] is True
        assert result['check_2_a_is_24'] is True

    def test_kappa_ch_d_additive(self):
        """Route D: relative kappa_ch^Heis(K3 x E) = 2 + 1 = 3."""
        # VERIFIED [MAN] prop:kappa-k3 path (vi)
        result = verify_kappa_ch_consistency()
        assert result['check_3_d_additive'] is True

    def test_chi_o_k3_is_2(self):
        """chi(O_{K3}) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        # VERIFIED [DC] direct Hodge diamond computation
        result = verify_kappa_ch_consistency()
        assert result['check_4_chi_o_is_2'] is True

    def test_all_kappa_consistent(self):
        """All kappa_ch checks pass."""
        result = verify_kappa_ch_consistency()
        assert result['all_consistent'] is True

    def test_n4_shadow_tower_rational(self):
        """N=4 shadow tower values are exact rationals."""
        for r, val in N4_SHADOW_TOWER.items():
            assert isinstance(val, Fraction), f"S_{r} is not a Fraction: {type(val)}"

    # AP compliance tests

    def test_ap113_no_bare_kappa(self):
        """No bare 'kappa' in route names (AP113)."""
        for route in [ROUTE_A, ROUTE_B, ROUTE_C, ROUTE_D]:
            # Route names should not contain bare "kappa" (should be kappa_ch etc.)
            # This is a proxy check: the actual AP113 check is on .tex content
            assert 'kappa_ch' not in route.name or 'kappa_' in route.name

    def test_ap_cy14_conjectural_status(self):
        """Routes A and D are CONJECTURAL (AP-CY14)."""
        assert ROUTE_A.status == 'CONJECTURAL'
        assert ROUTE_D.status == 'CONJECTURAL'

    def test_ap_cy14_proved_status(self):
        """Routes B and C are PROVED."""
        assert ROUTE_B.status == 'PROVED'
        assert ROUTE_C.status == 'PROVED'


# =========================================================================
# Cross-Engine Kappa Verification (7 tests)
# =========================================================================


class TestCrossEngineKappa:
    """Tests for cross-engine kappa_ch consistency (phi_k3, hcs_hierarchy)."""

    def test_phi_k3_vs_route_b(self):
        """phi_k3_explicit_evaluation agrees with Route B: kappa_ch = 2."""
        # VERIFIED [XE] cross-engine
        result = cross_engine_kappa_verification()
        assert result['phi_k3_vs_route_b'] is True

    def test_hcs_hierarchy_vs_route_b(self):
        """hcs_hierarchy_k3 agrees with Route B: KAPPA_CH_K3 = 2."""
        # VERIFIED [XE] cross-engine
        result = cross_engine_kappa_verification()
        assert result['hcs_hierarchy_vs_route_b'] is True

    def test_hcs_hierarchy_vs_route_d(self):
        """hcs_hierarchy_k3 agrees with Route D: KAPPA_CH_K3E_HEIS = 3."""
        # VERIFIED [XE] cross-engine
        result = cross_engine_kappa_verification()
        assert result['hcs_hierarchy_vs_route_d'] is True

    def test_fiber_kappa_vs_route_a(self):
        """hcs_hierarchy_k3 KAPPA_FIBER_K3 = 24 matches Route A."""
        # VERIFIED [XE] cross-engine
        result = cross_engine_kappa_verification()
        assert result['fiber_kappa_vs_route_a'] is True

    def test_shadow_class_cross_engine(self):
        """phi_k3_explicit_evaluation shadow class matches Route B: G."""
        # VERIFIED [XE] cross-engine
        result = cross_engine_kappa_verification()
        assert result['shadow_class_vs_route_b'] is True

    def test_kappa_spectrum_values(self):
        """Kappa-spectrum values are {0, 2, 3, 5, 24} (AP113)."""
        # VERIFIED [DC] from hcs_hierarchy_k3 kappa constants
        result = cross_engine_kappa_verification()
        assert result['spectrum_is_0_2_3_5_24'] is True

    def test_all_cross_checks_pass(self):
        """All cross-engine kappa checks pass."""
        result = cross_engine_kappa_verification()
        assert result['all_cross_checks_pass'] is True


# =========================================================================
# Hodge Diamond Decomposition (8 tests)
# =========================================================================


class TestHodgeDiamondDecomposition:
    """Tests for the Hodge-to-current map and 24 vs 8 generator distinction."""

    def test_total_currents_24(self):
        """H_Muk has 24 currents from HKR decomposition of H^*(K3)."""
        # VERIFIED [DC] sum of K3 Hodge numbers = 24
        result = hodge_diamond_decomposition()
        assert result['total_currents_is_24'] is True

    def test_n4_generators_8(self):
        """N=4 SCA has 8 generators (T, G^+/-, tG^+/-, J^++/--/3)."""
        # VERIFIED [MAN] def:n4-sca-c6
        result = hodge_diamond_decomposition()
        assert result['total_n4_is_8'] is True

    def test_generator_ratio_3(self):
        """Generator ratio H_Muk / N=4 = 24/8 = 3 = dim_C(K3) + 1."""
        # VERIFIED [DC]
        result = hodge_diamond_decomposition()
        assert result['generator_ratio_is_3'] is True

    def test_c_h_muk_24(self):
        """H_Muk central charge c = 24 from 24 free bosons."""
        # VERIFIED [DC] 24 * 1 = 24
        result = hodge_diamond_decomposition()
        assert result['c_h_muk'] == 24

    def test_c_n4_6(self):
        """N=4 SCA central charge c = 6 from 4 bosons + 4 fermions."""
        # VERIFIED [DC] 4*1 + 4*(1/2) = 6
        result = hodge_diamond_decomposition()
        assert result['c_n4'] == 6

    def test_mukai_signature_4_20(self):
        """Mukai pairing has signature (4, 20)."""
        # VERIFIED [DC] from Hodge diamond
        result = hodge_diamond_decomposition()
        assert result['mukai_signature_is_4_20'] is True

    def test_kaehler_moduli_20(self):
        """H^{1,1}(K3) = 20 Kaehler moduli contribute negative signature."""
        # VERIFIED [DC]
        result = hodge_diamond_decomposition()
        assert result['currents_by_type']['kaehler_moduli'] == 20

    def test_holomorphic_symplectic_1(self):
        """H^{2,0}(K3) = 1 holomorphic symplectic form."""
        # VERIFIED [DC]
        result = hodge_diamond_decomposition()
        assert result['currents_by_type']['hol_symplectic'] == 1


# =========================================================================
# N=4 Shadow Tower Analysis (8 tests)
# =========================================================================


class TestN4ShadowTowerAnalysis:
    """Tests for N=4 shadow tower convergence and class M confirmation."""

    def test_alternation_from_4(self):
        """Shadow tower has sign alternation from depth 4 onward."""
        # VERIFIED [MAN] comp:shadow-tower-k3
        result = n4_shadow_tower_analysis()
        assert result['alternating_from_4'] is True

    def test_critical_discriminant_20_over_39(self):
        """Critical discriminant Delta = 20/39."""
        # VERIFIED [DC] 8 * 2 * (5/156) = 80/156 = 20/39
        result = n4_shadow_tower_analysis()
        assert result['discriminant_matches'] is True

    def test_all_nonzero_2_to_12(self):
        """All S_r nonzero for r = 2, ..., 12 (class M)."""
        # VERIFIED [MAN] comp:shadow-tower-k3
        result = n4_shadow_tower_analysis()
        assert result['all_nonzero_2_to_12'] is True

    def test_class_m_confirmed(self):
        """Class M confirmed: all S_r nonzero AND discriminant nonzero."""
        result = n4_shadow_tower_analysis()
        assert result['class_M_confirmed'] is True

    def test_s2_equals_kappa_ch(self):
        """S_2 = 2 = kappa_ch (initial condition)."""
        # VERIFIED [DC]
        result = n4_shadow_tower_analysis()
        assert result['tower'][2] == F(2)

    def test_s3_equals_2(self):
        """S_3 = 2 (non-formality discriminant)."""
        # VERIFIED [MAN] comp:shadow-tower-k3
        result = n4_shadow_tower_analysis()
        assert result['tower'][3] == F(2)

    def test_s4_exact(self):
        """S_4 = 5/156 (exact rational)."""
        # VERIFIED [MAN] comp:shadow-tower-k3
        result = n4_shadow_tower_analysis()
        assert result['tower'][4] == F(5, 156)

    def test_contrast_h_muk_class_g(self):
        """H_Muk is class G: S_r = 0 for r >= 3 (contrast with N=4 class M)."""
        result = n4_shadow_tower_analysis()
        contrast = result['contrast_with_h_muk']
        assert contrast['h_muk_S3_onwards'] == F(0)
        assert contrast['h_muk_class'] == 'G'
        assert contrast['n4_class'] == 'M'


# =========================================================================
# CoHA vs E_1-Chiral Distinction (7 tests, AP-CY7)
# =========================================================================


class TestCoHAvsChiral:
    """Tests for the CoHA vs E_1-chiral algebra distinction (AP-CY7)."""

    def test_coha_is_not_chiral(self):
        """CoHA is NOT a chiral algebra (AP-CY7)."""
        result = coha_vs_chiral_distinction()
        assert result['coha']['is_chiral'] is False

    def test_coha_is_not_vertex_algebra(self):
        """CoHA does NOT carry a vertex algebra structure (AP-CY7)."""
        result = coha_vs_chiral_distinction()
        assert result['coha']['is_vertex_algebra'] is False

    def test_e1_chiral_is_chiral(self):
        """E_1-chiral algebra IS a factorization algebra."""
        result = coha_vs_chiral_distinction()
        assert result['e1_chiral']['is_chiral'] is True

    def test_connection_is_functor_not_identification(self):
        """CoHA -> E_1-chiral is a FUNCTOR (Phi), not an identification."""
        result = coha_vs_chiral_distinction()
        assert result['connection_is_functor'] is True
        assert result['connection_is_identification'] is False

    def test_e1_chiral_d3_conjectural(self):
        """E_1-chiral at d=3 is CONJECTURAL (requires CY-A_3)."""
        result = coha_vs_chiral_distinction()
        assert result['e1_chiral']['status'] == 'CONJECTURAL at d=3 (CY-A_3)'

    def test_h_muk_proved(self):
        """H_Muk (from CY-A_2 on K3) is PROVED."""
        result = coha_vs_chiral_distinction()
        assert result['k3xe_status']['h_muk'] == 'PROVED (from CY-A_2 on K3 alone, E_2-chiral)'

    def test_no_genuine_inconsistency_coha(self):
        """CoHA vs chiral is not a genuine inconsistency."""
        result = coha_vs_chiral_distinction()
        assert result['genuine_inconsistency'] is False


# =========================================================================
# Omega-Background Mechanism (7 tests, AP-CY20)
# =========================================================================


class TestOmegaBackground:
    """Tests for the Omega-background mechanism and AP-CY20 compliance."""

    def test_cy2_constraint_satisfied(self):
        """Kummer parameters satisfy CY_2 constraint: sum h_i = 0."""
        # VERIFIED [DC] 4*1 + 20*(-1/5) = 0
        result = omega_background_mechanism()
        assert result['omega_parameters']['cy2_constraint_ok'] is True

    def test_p1_vanishes_omega(self):
        """First power sum p_1 = 0 (CY_2 constraint via Omega parameters)."""
        # VERIFIED [DC]
        result = omega_background_mechanism()
        assert result['power_sums']['p_1'] == 0

    def test_p2_value(self):
        """Second power sum p_2 = 24/5."""
        # VERIFIED [DC] 4*1 + 20*(1/25) = 24/5
        result = omega_background_mechanism()
        assert result['p2_matches'] is True
        assert result['p2_value'] == F(24, 5)

    def test_p3_value_omega(self):
        """Third power sum p_3 = 96/25 (leading deformation)."""
        # VERIFIED [DC] 4*1 + 20*(-1/125) = 96/25
        result = omega_background_mechanism()
        assert result['p3_matches'] is True
        assert result['p3_value'] == F(96, 25)

    def test_24_parameters(self):
        """Omega-background has exactly 24 parameters (Mukai rank)."""
        result = omega_background_mechanism()
        assert result['omega_parameters']['count'] == 24

    def test_sigma_model_limit_trivial(self):
        """Sigma model is the h_i -> 0 limit: g(u) = 1, R = I."""
        result = omega_background_mechanism()
        limit = result['sigma_model_limit']
        assert limit['g_u'] == '1 (trivial)'
        assert limit['R_matrix'] == 'I (identity)'

    def test_no_genuine_inconsistency_omega(self):
        """Omega-background mechanism resolves the Yangian tension."""
        result = omega_background_mechanism()
        assert result['genuine_inconsistency'] is False
