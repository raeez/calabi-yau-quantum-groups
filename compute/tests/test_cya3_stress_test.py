r"""Tests for the CY-A_3 adversarial stress-test engine.

The boundary under test:

* raw ``B_term^(2)`` has the strict witness
  ``[m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0``;
* unit-connectedness, Dunn additivity, and Goodwillie connectivity do not
  automatically prove ``HH^{-2}_{E_1}(A,A)=0``;
* Costello's identity applies to corrected ``B_TCFT^(2)`` only after its
  correction datum is supplied;
* the stress test is a proof-obligation ledger, not a theorem vote.
"""

from fractions import Fraction

from compute.lib.connes_b_obs_ainf import (
    corrected_tcft_identity,
    hh_minus_two_filtration_vanishes,
    strict_cy3_witness,
)
from compute.lib.cya3_stress_test import (
    AttackVector,
    CohomologicalVsChainCheck,
    DunnAdditivityCheck,
    ManuscriptRecommendation,
    StressTestResult,
    TCFTBIdentificationCheck,
    UnitConnectednessCheck,
    attack_aq_cotangent,
    attack_cohomological_vs_chain,
    attack_dunn_additivity,
    attack_tcft_b_identification,
    attack_unit_connectedness,
    check_cohomological_vs_chain,
    check_dunn_additivity,
    check_tcft_b_identification,
    check_unit_connectedness_k3xe,
    check_unit_connectedness_local_p2,
    check_unit_connectedness_quintic,
    complete_conditional_obstruction_status,
    compute_hh0_landscape,
    compute_obstruction_by_mechanism,
    count_generic_vs_special,
    generate_recommendations,
    master_stress_test,
    run_stress_test,
    strict_witness_summary,
    verify_k3xe_product_decomposition,
)
from compute.lib.derived_framing_obstruction import (
    HHMinusTwoFiltrationHypotheses,
    complete_hh_minus_two_hypotheses,
    complete_tcft_correction_datum,
)


# ================================================================
# SECTION 1: STRICT RAW WITNESS
# ================================================================


class TestStrictWitness:
    """Tests for the raw ``m_3``--``B_term^(2)`` witness."""

    def test_stress_engine_records_exact_witness(self):
        witness = strict_witness_summary()
        assert witness["input_word"] == ("a", "a", "a", "a", "b")
        assert witness["commutator"] == {("b",): Fraction(2)}
        assert witness["coefficient_on_b"] == Fraction(2)
        assert witness["nonzero"]
        assert "2 alpha [b]" in witness["formula"]

    def test_alpha_scales_witness(self):
        witness = strict_witness_summary(Fraction(3, 2))
        assert witness["coefficient_on_b"] == Fraction(3)
        assert witness["nonzero"]

    def test_independent_connes_oracle_agrees(self):
        connes = strict_cy3_witness(alpha=5)
        stress = strict_witness_summary(5)
        assert connes.commutator_coeff == Fraction(10)
        assert stress["coefficient_on_b"] == connes.commutator_coeff
        assert connes.nonzero


# ================================================================
# SECTION 2: DUNN AND UNIT-CONNECTEDNESS BOUNDARIES
# ================================================================


class TestNoAutomaticHHMinusTwo:
    """Tests that connectivity slogans do not prove ``HH^{-2}``."""

    def test_dunn_applies_but_does_not_prove_hh_minus_two(self):
        check = check_dunn_additivity()
        assert isinstance(check, DunnAdditivityCheck)
        assert check.dunn_applies
        assert check.is_symmetric_monoidal
        assert not check.hh_minus_two_via_unit_connectedness
        assert check.hh_minus_two_requires_filtration
        assert not check.space_contractible_established
        assert "empty total degree -2" in check.gap_description

    def test_complete_hypotheses_close_only_the_hh_line(self):
        check = check_dunn_additivity(complete_hh_minus_two_hypotheses())
        assert check.required_hypotheses == []
        assert check.hh_minus_two_requires_filtration
        assert not check.space_contractible_established

    def test_unit_connected_quintic_still_has_open_hh_obligation(self):
        check = check_unit_connectedness_quintic()
        assert isinstance(check, UnitConnectednessCheck)
        assert check.cat_hh0_dim == 1
        assert check.cat_is_unit_connected
        assert check.requires_phi
        assert check.circularity_present
        assert not check.hh_minus_two_vanishing_established
        assert "complete bar-length filtration" in check.required_hypotheses

    def test_local_p2_unit_connectedness_is_not_hh_minus_two_proof(self):
        check = check_unit_connectedness_local_p2()
        assert check.cat_hh0_dim == 1
        assert check.alg_hh0_dim == 1
        assert not check.hh_minus_two_vanishing_established

    def test_k3xe_is_not_generic_unit_connectedness_case(self):
        check = check_unit_connectedness_k3xe()
        assert check.cat_hh0_dim == 2
        assert not check.cat_is_unit_connected
        assert check.requires_phi
        assert not check.hh_minus_two_vanishing_established
        assert "product" in check.mitigation.lower()

    def test_independent_filtration_oracle_requires_all_hypotheses(self):
        missing = hh_minus_two_filtration_vanishes(
            complete=True,
            exhaustive=True,
            separated=True,
            strongly_convergent=False,
            empty_total_degree_minus_two_line=True,
        )
        assert not missing["vanishes"]
        assert missing["missing_hypotheses"] == ["strongly_convergent"]

        complete = hh_minus_two_filtration_vanishes(
            complete=True,
            exhaustive=True,
            separated=True,
            strongly_convergent=True,
            empty_total_degree_minus_two_line=True,
        )
        assert complete["vanishes"]


# ================================================================
# SECTION 3: COSTELLO CARRIER BOUNDARY
# ================================================================


class TestTCFTCarrierBoundary:
    """Tests for raw ``B_term^(2)`` versus corrected ``B_TCFT^(2)``."""

    def test_default_tcft_check_rejects_raw_shortcut(self):
        check = check_tcft_b_identification()
        assert isinstance(check, TCFTBIdentificationCheck)
        assert not check.identification_valid
        assert not check.raw_term_identified_with_tcft
        assert not check.raw_termwise_commutator_vanishes
        assert not check.corrected_identity_available
        assert check.strict_witness_coefficient == Fraction(2)
        assert "Costello moduli-chain correction terms" in check.missing_correction_data

    def test_complete_tcft_datum_supplies_corrected_identity_only(self):
        check = check_tcft_b_identification(complete_tcft_correction_datum())
        assert check.identification_valid
        assert check.corrected_identity_available
        assert not check.raw_term_identified_with_tcft
        assert not check.raw_termwise_commutator_vanishes
        assert check.missing_correction_data == []

    def test_independent_connes_tcft_oracle_is_conditional(self):
        missing = corrected_tcft_identity(has_moduli_chain_correction=False)
        assert not missing["total_identity_holds"]
        assert not missing["raw_operator_identified"]

        supplied = corrected_tcft_identity(has_moduli_chain_correction=True)
        assert supplied["total_identity_holds"]
        assert not supplied["per_k_identity_holds"]
        assert not supplied["raw_operator_identified"]


# ================================================================
# SECTION 4: COHOMOLOGICAL VS CHAIN-LEVEL
# ================================================================


class TestCohomologicalVsChain:
    """Tests that conditional vanishing is not contractibility."""

    def test_default_check_does_not_prove_existence_or_contractibility(self):
        check = check_cohomological_vs_chain()
        assert isinstance(check, CohomologicalVsChainCheck)
        assert not check.existence_proved
        assert not check.primary_obstruction_conditionally_vanishes
        assert not check.corrected_tcft_identity_available
        assert not check.space_contractible_established
        assert check.strict_witness_coefficient == Fraction(2)
        assert not check.construction_from_vanishing

    def test_complete_inputs_still_do_not_prove_contractibility(self):
        check = check_cohomological_vs_chain(
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert check.existence_proved
        assert check.primary_obstruction_conditionally_vanishes
        assert check.corrected_tcft_identity_available
        assert not check.space_contractible_established
        assert not check.construction_from_vanishing


# ================================================================
# SECTION 5: ATTACK VECTORS AND MASTER RESULT
# ================================================================


class TestAttackVectors:
    """Tests for attack pass/fail semantics."""

    def test_attack_vector_types(self):
        attacks = [
            attack_dunn_additivity(),
            attack_unit_connectedness(),
            attack_aq_cotangent(),
            attack_tcft_b_identification(),
            attack_cohomological_vs_chain(),
        ]
        assert all(isinstance(a, AttackVector) for a in attacks)
        assert all(not a.survives for a in attacks)
        assert {a.severity for a in attacks} == {"fatal", "moderate"}

    def test_dunn_attack_names_missing_hh_hypotheses(self):
        attack = attack_dunn_additivity()
        assert attack.severity == "fatal"
        assert not attack.survives
        assert "complete bar-length filtration" in attack.proof_obligations
        assert "empty total degree -2 first-page line" in attack.proof_obligations

    def test_tcft_attack_names_correction_datum(self):
        attack = attack_tcft_b_identification()
        assert attack.severity == "fatal"
        assert not attack.survives
        assert "chosen corrected representative B^{(2)}_TCFT" in attack.proof_obligations

    def test_master_stress_test_is_failure_ledger(self):
        result = run_stress_test()
        assert isinstance(result, StressTestResult)
        assert len(result.attacks) == 5
        assert not result.proofs_survive
        assert len(result.fatal_weaknesses) == 4
        assert len(result.genuine_weaknesses) == 5
        assert "2 alpha [b]" in result.synthesis
        assert "Do not assert contractibility" in result.recommendation

    def test_master_alias(self):
        result = master_stress_test()
        assert isinstance(result, StressTestResult)
        assert not result.proofs_survive


# ================================================================
# SECTION 6: LANDSCAPE AND MECHANISM DIAGNOSTICS
# ================================================================


class TestLandscapeDiagnostics:
    """Tests for example classification without theorem votes."""

    def test_hh0_landscape_records_no_hh_minus_two_vote(self):
        landscape = compute_hh0_landscape()
        assert len(landscape) == 7
        assert landscape["K3 x E"]["cat_hh0_dim"] == 2
        assert not landscape["K3 x E"]["unit_connected"]
        for data in landscape.values():
            assert not data["hh_minus_two_vanishing_established"]

    def test_default_obstruction_statuses_are_open(self):
        by_mech = compute_obstruction_by_mechanism()
        assert len(by_mech) == 6
        for data in by_mech.values():
            assert not data["obstruction_vanishes"]
            assert data["status"] == "open_requires_named_hypotheses"
            assert data["required_hypotheses"]

    def test_complete_obstruction_statuses_are_conditional(self):
        by_mech = complete_conditional_obstruction_status()
        for data in by_mech.values():
            assert data["obstruction_vanishes"]
            assert data["status"] == "conditional_obstruction_vanishes"
            assert data["required_hypotheses"] == []
        assert by_mech["Local P^2"]["raw_witness_nonzero"]

    def test_count_is_diagnostic_not_proof_count(self):
        counts = count_generic_vs_special()
        assert counts == {"generic": 5, "special": 1, "total": 6}


# ================================================================
# SECTION 7: K3 x E PRODUCT BOUNDARY
# ================================================================


class TestK3xEProductBoundary:
    """Tests for K3 x E product decomposition status."""

    def test_product_decomposition_does_not_auto_close(self):
        decomp = verify_k3xe_product_decomposition()
        assert decomp["k3_factor"]["proved"]
        assert decomp["e_factor"]["proved"]
        assert decomp["hopf_twist_absent"]
        assert not decomp["unit_connectedness_needed"]
        assert not decomp["product"]["obstruction_vanishes"]
        assert decomp["product"]["status"] == "open_requires_named_hypotheses"
        assert "complete bar-length filtration" in decomp["proof_obligations"]

    def test_product_decomposition_closes_only_conditionally(self):
        decomp = verify_k3xe_product_decomposition(
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert decomp["product"]["obstruction_vanishes"]
        assert decomp["product"]["status"] == "conditional_obstruction_vanishes"
        assert decomp["proof_obligations"] == []


# ================================================================
# SECTION 8: RECOMMENDATIONS
# ================================================================


class TestRecommendations:
    """Tests for stale-claim repair recommendations."""

    def test_three_recommendations_cover_failure_targets(self):
        recs = generate_recommendations()
        assert len(recs) == 3
        assert all(isinstance(r, ManuscriptRecommendation) for r in recs)
        claims = " ".join(r.current_claim for r in recs)
        assert "HH^{-2}" in claims
        assert "{b,B^(2)}=0" in claims
        assert "contractible" in claims

    def test_recommendations_are_fatal_repairs(self):
        recs = generate_recommendations()
        assert {r.severity for r in recs} == {"fatal"}
        edits = " ".join(r.recommended_edit for r in recs)
        assert "empty total degree -2 line" in edits
        assert "Costello correction datum" in edits
        assert "contractibility" in edits


# ================================================================
# SECTION 9: FILTRATION HYPOTHESIS CONTROL
# ================================================================


class TestFiltrationHypothesisControl:
    """Tests that partial HH hypotheses are not accepted."""

    def test_partial_hh_hypotheses_do_not_close_stress_engine(self):
        partial = HHMinusTwoFiltrationHypotheses(
            connective_unit_connected_model=True,
            filtration_complete=True,
            filtration_exhaustive=True,
            filtration_separated=True,
            strong_convergence=True,
            empty_total_degree_minus_two_line=False,
            comparison_to_obstruction_complex=True,
            obstruction_cocycle_degree_minus_two=True,
        )
        by_mech = compute_obstruction_by_mechanism(
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=partial,
        )
        for data in by_mech.values():
            assert not data["obstruction_vanishes"]
            assert "empty total degree -2 first-page line" in data["required_hypotheses"]
