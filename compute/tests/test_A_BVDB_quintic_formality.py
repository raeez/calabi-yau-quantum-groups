"""Tests for the AP-CY34-safe quintic/BVDB diagnostic engine."""

from fractions import Fraction
from math import comb

from compute.lib.A_BVDB_quintic_formality import (
    AUTOMATIC_SOURCE_MECHANISMS,
    FORBIDDEN_AUTOMATIC_TARGETS,
    QUINTIC_BPS_GENUS_0,
    QUINTIC_HODGE,
    QUINTIC_TRIPLE_INTERSECTION,
    a_bvdb_curved_formality_conjecture,
    a_bvdb_dim_by_degree,
    a_bvdb_is_minus_3_cy,
    a_bvdb_strict_formality_status,
    a_bvdb_total_dimension,
    automatic_implication_firewall,
    b_tcft2_comparison_check,
    calaque_halbout_felder_applicability,
    healed_platonic_statement,
    hh_minus_two_filtration_check,
    hq_o_d_quintic,
    kodaira_spencer_dim_h1,
    kodaira_spencer_dim_h2,
    m3_kodaira_spencer_dimension,
    m3_obstruction_via_yukawa,
    positive_closure_gate,
    quintic_continuous_symmetry_group,
    raw_b_term2_witness,
    torus_action_p4_dimension,
    torus_action_preserves_quintic,
    verify_all,
    yukawa_classical,
    yukawa_is_nonvanishing,
    yukawa_q_expansion,
)


class TestABVDBStructure:
    """Exact BVDB dimension and Serre-duality diagnostics."""

    def test_line_bundle_cohomology_samples(self):
        assert hq_o_d_quintic(0) == [1, 0, 0, 1]
        assert hq_o_d_quintic(1) == [5, 0, 0, 0]
        assert hq_o_d_quintic(-1) == [0, 0, 0, 5]

    def test_a_bvdb_total_dim_420(self):
        assert a_bvdb_total_dimension() == 420

    def test_a_bvdb_dim_by_degree(self):
        by_deg = a_bvdb_dim_by_degree()
        assert by_deg == {0: 210, 1: 0, 2: 0, 3: 210}

    def test_a_bvdb_is_minus_3_cy_pairing_only(self):
        cy_data = a_bvdb_is_minus_3_cy()
        assert cy_data["serre_symmetry_0_3"] is True
        assert cy_data["serre_symmetry_1_2"] is True
        assert cy_data["cy_degree"] == -3
        assert "not an Obs_Ainf" in cy_data["scope"]


class TestYukawaCoupling:
    """Exact large-radius Yukawa coefficients."""

    def test_classical_value(self):
        assert QUINTIC_TRIPLE_INTERSECTION == 5
        assert yukawa_classical() == 5

    def test_bps_inputs(self):
        assert QUINTIC_BPS_GENUS_0[1] == 2875
        assert QUINTIC_BPS_GENUS_0[2] == 609250

    def test_q_expansion_coefficients(self):
        coeffs = yukawa_q_expansion(3)
        assert coeffs[0] == Fraction(5)
        assert coeffs[1] == Fraction(2875)
        assert coeffs[2] == Fraction(2875 + 8 * 609250)
        assert coeffs[2] == Fraction(4876875)

    def test_yukawa_nonzero_scope_is_large_radius_only(self):
        diagnostic = yukawa_is_nonvanishing()
        assert diagnostic["formal_series_not_identically_zero"] is True
        assert diagnostic["global_zero_locus_known_empty"] is False
        assert diagnostic["vanishing_locus_in_moduli"] == "not_computed_by_this_engine"


class TestKodairaSpencerCarrier:
    """Yukawa lives on the KS carrier until a BVDB comparison is supplied."""

    def test_hodge_dimensions(self):
        assert QUINTIC_HODGE[(2, 1)] == 101
        assert QUINTIC_HODGE[(2, 2)] == 1
        assert kodaira_spencer_dim_h1() == 101
        assert kodaira_spencer_dim_h2() == 1

    def test_m3_source_target_dims(self):
        m3 = m3_kodaira_spencer_dimension()
        assert m3["h1_T_dim"] == 101
        assert m3["h2_T_dim"] == 1
        assert m3["sym3_h1_dim"] == comb(103, 3)
        assert m3["sym3_h1_dim"] == 176851

    def test_m3_yukawa_does_not_transfer_automatically_to_bvdb(self):
        m3 = m3_kodaira_spencer_dimension()
        assert m3["m3_is_yukawa_coupling_on_ks_carrier"] is True
        assert m3["m3_is_zero_morphism_on_ks_carrier"] is False
        assert m3["a_bvdb_transfer_map_supplied"] is False

    def test_m3_obstruction_report_is_carrier_separated(self):
        obs = m3_obstruction_via_yukawa()
        assert obs["ks_yukawa_nonzero"] is True
        assert obs["a_bvdb_obstruction_nonzero_proved"] is False
        assert obs["requires_bvdb_ks_comparison_map"] is True
        assert "No strict A_BVDB formality verdict" in obs["consequence_for_formality"]


class TestTorusCriterion:
    """The ambient torus route fails without creating a closure theorem."""

    def test_ambient_torus_does_not_preserve_quintic(self):
        assert torus_action_p4_dimension() == 4
        assert torus_action_preserves_quintic() is False

    def test_quintic_connected_automorphism_group(self):
        sym = quintic_continuous_symmetry_group()
        assert sym["connected_component"] == "trivial"
        assert sym["continuous_torus_exists"] is False
        assert sym["discrete_aut_order"] == 15000
        assert "BTT is not used" in sym["reason"]

    def test_calaque_halbout_felder_fails_safely(self):
        chf = calaque_halbout_felder_applicability()
        assert chf["calaque_halbout_felder_applies"] is False
        assert chf["x5_is_toric"] is False
        assert chf["p4_torus_preserves_x5"] is False
        assert set(chf["does_not_imply"]) == set(FORBIDDEN_AUTOMATIC_TARGETS)


class TestAPCY34RawWitness:
    """Raw B_term^(2) is preserved and separated from B_TCFT^(2)."""

    def test_raw_witness_coefficients(self):
        witness = raw_b_term2_witness()
        assert witness["raw_operator"] == "B_term^(2)"
        assert witness["corrected_operator"] == "B_TCFT^(2)"
        assert witness["raw_is_corrected_tcft"] is False
        assert witness["B_term_then_m3_coeff"] == Fraction(4)
        assert witness["m3_then_B_term_coeff"] == Fraction(2)
        assert witness["commutator_coeff"] == Fraction(2)
        assert witness["nonzero"] is True
        assert witness["formula"] == (
            "[m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0"
        )

    def test_raw_witness_scales_with_alpha(self):
        witness = raw_b_term2_witness(Fraction(3, 5))
        assert witness["B_term_then_m3_coeff"] == Fraction(12, 5)
        assert witness["m3_then_B_term_coeff"] == Fraction(6, 5)
        assert witness["commutator_coeff"] == Fraction(6, 5)


class TestPositiveClosureGates:
    """Positive compact closure requires explicit supplied data."""

    def test_missing_b_tcft_data_does_not_close(self):
        tcft = b_tcft2_comparison_check()
        assert tcft["established"] is False
        assert tcft["raw_operator_identified_with_tcft"] is False
        assert tcft["per_k_identity_claimed"] is False
        assert "comparison_map_from_raw_B_term_to_B_TCFT" in tcft["missing_hypotheses"]

    def test_complete_b_tcft_data_closes_tcft_route(self):
        tcft = b_tcft2_comparison_check(
            corrected_operator_chosen=True,
            costello_moduli_chain_correction_terms=True,
            open_closed_tcft_chain_map=True,
            orientation_signs_fixed=True,
            comparison_map_from_raw_B_term_to_B_TCFT=True,
        )
        assert tcft["established"] is True
        assert tcft["total_identity"] == "{sum_k b_k, B_TCFT^(2)} = 0"
        assert tcft["raw_operator_identified_with_tcft"] is False

    def test_missing_hh_minus_two_data_does_not_vanish(self):
        hh = hh_minus_two_filtration_check()
        assert hh["vanishes"] is False
        assert "comparison_map_to_obstruction_complex" in hh["missing_hypotheses"]
        assert "empty_total_degree_minus_two_line" in hh["missing_hypotheses"]

    def test_complete_hh_minus_two_data_vanishes(self):
        hh = hh_minus_two_filtration_check(
            comparison_map_to_obstruction_complex=True,
            filtration_complete=True,
            filtration_exhaustive=True,
            filtration_separated=True,
            strong_convergence=True,
            empty_total_degree_minus_two_line=True,
        )
        assert hh["vanishes"] is True
        assert "empty on E_1" in hh["proof_summary"]

    def test_default_positive_closure_is_open(self):
        gate = positive_closure_gate()
        assert gate["raw_B_term_closes"] is False
        assert gate["positive_closure_established"] is False
        assert gate["status"] == "open"
        assert gate["raw_witness"]["nonzero"] is True

    def test_positive_closure_with_complete_hh_data(self):
        gate = positive_closure_gate(
            comparison_map_to_obstruction_complex=True,
            filtration_complete=True,
            filtration_exhaustive=True,
            filtration_separated=True,
            strong_convergence=True,
            empty_total_degree_minus_two_line=True,
        )
        assert gate["positive_closure_established"] is True
        assert gate["HH_minus_two_route"]["vanishes"] is True
        assert gate["raw_B_term_closes"] is False


class TestAutomaticImplicationFirewall:
    """DGMS/BTT/Kaledin/BVDB/Yukawa data do not imply closure targets."""

    def test_firewall_matrix_rejects_all_forbidden_implications(self):
        firewall = automatic_implication_firewall()
        assert firewall["all_forbidden_implications_rejected"] is True
        assert set(firewall["sources"]) == set(AUTOMATIC_SOURCE_MECHANISMS)
        assert set(firewall["targets"]) == set(FORBIDDEN_AUTOMATIC_TARGETS)
        for source in AUTOMATIC_SOURCE_MECHANISMS:
            for target in FORBIDDEN_AUTOMATIC_TARGETS:
                assert firewall["matrix"][source][target] is False

    def test_named_forbidden_targets_present(self):
        targets = set(FORBIDDEN_AUTOMATIC_TARGETS)
        assert "universal_compact_cy3_Obs_Ainf_zero" in targets
        assert "HH_minus_2_zero" in targets
        assert "contractible_S3_framing" in targets
        assert "compact_Phi_3_constructed" in targets
        assert "Hall_or_CoHA_constructed" in targets
        assert "PBW_flatness" in targets
        assert "no_extra_relations" in targets


class TestFormalityStatus:
    """The final reports stay open where the comparison data are absent."""

    def test_strict_formality_status_is_open(self):
        status = a_bvdb_strict_formality_status()
        assert status["is_formal_strict"] == "not_established"
        assert status["strict_formality_proved"] is False
        assert status["strict_nonformality_proved"] is False
        assert status["bvdb_ks_comparison_map_supplied"] is False
        assert status["compact_cy3_closure_gate"]["positive_closure_established"] is False

    def test_curved_formality_status_is_conditional(self):
        curved = a_bvdb_curved_formality_conjecture()
        assert curved["status"] == "OPEN_CONDITIONAL"
        assert curved["curved_formality_proved"] is False
        assert "comparison from BCOV cubic vertex" in curved["requires"][1]
        assert set(curved["does_not_imply"]) == set(FORBIDDEN_AUTOMATIC_TARGETS)

    def test_healed_statement_names_remaining_obligations(self):
        healed = healed_platonic_statement()
        assert "OPEN" in healed["current_status_strict"]
        assert healed["ingredient_d_bvdb_ks_transfer"] == "OPEN"
        assert "corrected TCFT or HH^{-2}" in healed["ingredient_e_compact_s3_closure"]


class TestVerifyAll:
    """Smoke test for the combined report."""

    def test_verify_all_runs(self):
        report = verify_all()
        assert report["a_bvdb_total_dim"] == 420
        assert report["yukawa_q_expansion_to_3"][2] == 4876875
        assert report["m3_obstruction"]["a_bvdb_obstruction_nonzero_proved"] is False
        assert report["raw_b_term2_witness"]["commutator_coeff"] == Fraction(2)
        assert report["positive_closure_gate"]["positive_closure_established"] is False
        assert report["strict_formality_status"]["strict_nonformality_proved"] is False
