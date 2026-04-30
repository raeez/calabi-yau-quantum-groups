r"""Tests for the corrected Connes B / Obs_Ainf diagnostic engine.

The direct contract is negative for the old universal termwise claim:
``B^{(2)}_term`` is not ``B^{(2)}_TCFT`` and the strict cyclic CY3 witness
has ``[m_3,B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0``.

The positive facts retained here are classical Connes ``B^{(0)}``, formal
Frobenius cases, Costello's corrected total TCFT identity under correction
data, and ``HH^{-2}`` filtration vanishing under explicit hypotheses.
"""

from fractions import Fraction

import pytest

from compute.lib.connes_b_obs_ainf import (
    BidegreeShift,
    CYDimensionAnalysis,
    CommutatorDecompositionEntry,
    ConnesBObsAinfResolution,
    DecompositionResult,
    ManuscriptImplications,
    NonAdjacentResolution,
    StrictCY3Witness,
    TwoStepDecomposition,
    bidegree_of_bj,
    bidegree_of_commutator,
    bidegree_of_mk,
    bidegree_table,
    corrected_tcft_identity,
    decompose_b_B_identity,
    formal_frobenius_case,
    hh_minus_two_filtration_vanishes,
    manuscript_implications,
    master_resolution,
    obs_ainf_cy2,
    obs_ainf_cy3,
    obs_ainf_general,
    resolve_non_adjacent_gap,
    single_grading_decomposition,
    strict_cy3_witness,
    termwise_commutator_verdict,
    verify_bidegree_injectivity,
    verify_mixed_complex_axiom_prerequisite,
)

F = Fraction


class TestDegreeDiagnostics:
    """The degree helpers are diagnostics, not a vanishing proof."""

    def test_mk_bar_length_shift(self):
        assert bidegree_of_mk(2) == BidegreeShift(-1, 0, True, "bar_length")
        assert bidegree_of_mk(3).hochschild_shift == -2
        assert bidegree_of_mk(3).pairing_weight == 0

    def test_b0_is_classical_connes_operator(self):
        bd = bidegree_of_bj(0)
        assert bd.hochschild_shift == 1
        assert bd.pairing_weight == 0
        assert bd.proof_grading
        assert bd.normalization == "classical_connes_B0"

    def test_b2_term_is_raw_pair_contraction_label(self):
        bd = bidegree_of_bj(2)
        assert bd.hochschild_shift == -2
        assert bd.pairing_weight == 2
        assert not bd.proof_grading
        assert bd.normalization == "raw_pair_contraction"

    def test_m3_b2_term_commutator_shift_matches_witness_arity(self):
        bd = bidegree_of_commutator(3, 2)
        assert bd.hochschild_shift == -4
        assert bd.pairing_weight == 2
        assert not bd.proof_grading

    def test_invalid_indices_rejected(self):
        with pytest.raises(ValueError):
            bidegree_of_mk(0)
        with pytest.raises(ValueError):
            bidegree_of_bj(-1)


class TestStrictWitness:
    """The strict cyclic CY3 witness is the falsifier."""

    def test_strict_witness_coefficients(self):
        w = strict_cy3_witness()
        assert isinstance(w, StrictCY3Witness)
        assert w.input_word == ("a", "a", "a", "a", "b")
        assert w.b2_term_output_coeff == 4
        assert w.m3_after_b2_coeff == 4
        assert w.b2_after_m3_coeff == 2
        assert w.commutator_coeff == 2
        assert w.nonzero

    def test_strict_witness_scales_with_alpha(self):
        w = strict_cy3_witness(F(3, 2))
        assert w.alpha == F(3, 2)
        assert w.m3_after_b2_coeff == 6
        assert w.b2_after_m3_coeff == 3
        assert w.commutator_coeff == 3
        assert w.statement.endswith("3 [b]")

    def test_termwise_verdict_rejects_universal_claim(self):
        verdict = termwise_commutator_verdict(3, 2)
        assert verdict["status"] == "false"
        assert verdict["vanishes"] is False
        assert verdict["witness"].commutator_coeff == 2
        assert "!=" in verdict["reason"]

    def test_other_termwise_claims_not_established_by_default(self):
        verdict = termwise_commutator_verdict(4, 2)
        assert verdict["status"] == "not_established"
        assert verdict["vanishes"] is False
        assert verdict["witness"] is None


class TestRejectedBidegreeProof:
    """The old projection remains visible only as rejected bookkeeping."""

    def test_formal_label_injective_but_not_a_proof(self):
        result = verify_bidegree_injectivity(max_k=8, max_j=5)
        assert result["injective"]
        assert result["inverse_valid"]
        assert result["num_pairs_checked"] == 7 * 6
        assert result["projection_valid"] is False
        assert result["termwise_vanishing_established"] is False

    def test_decomposition_does_not_resolve_obs_ainf(self):
        result = decompose_b_B_identity(max_k=5, max_j=3)
        assert isinstance(result, DecompositionResult)
        assert result.projection_is_proof is False
        assert result.raw_termwise_universal_vanishing is False
        assert result.all_vanish_individually is False
        assert result.obs_ainf_resolved() is False

    def test_classical_entry_preserved(self):
        result = decompose_b_B_identity(max_k=3, max_j=2)
        entry = result.target_entry(k=2, j=0)
        assert isinstance(entry, CommutatorDecompositionEntry)
        assert entry.vanishes_individually
        assert entry.status == "proved_classical_connes"

    def test_strict_target_entry_is_false(self):
        result = decompose_b_B_identity(max_k=5, max_j=3)
        entry = result.target_entry(k=3, j=2)
        assert entry.vanishes_individually is False
        assert entry.status == "false_for_raw_term"
        assert "witness" in entry.reason.lower()

    def test_bidegree_table_marks_j2_target_nonvanishing(self):
        table = bidegree_table(max_k=5, max_j=3)
        target = [row for row in table if row["k"] == 3 and row["j"] == 2]
        assert len(target) == 1
        assert target[0]["vanishes"] is False
        assert target[0]["status"] == "false_for_raw_term"

    def test_single_grading_and_pairing_label_are_insufficient(self):
        result = single_grading_decomposition(max_k=8, max_j=5)
        assert result["single_grading_sufficient"] is False
        assert result["pairing_weight_projection_sufficient"] is False
        assert result["degenerate_shifts"] > 0

    def test_two_step_decomposition_is_rejected(self):
        ts = TwoStepDecomposition.construct()
        assert isinstance(ts, TwoStepDecomposition)
        assert ts.valid is False
        assert "Rejected" in ts.step1_identity
        assert "2 alpha [b]" in ts.conclusion


class TestPositiveMechanisms:
    """The true positive lanes remain available with their hypotheses."""

    def test_corrected_tcft_identity_requires_correction_data(self):
        missing = corrected_tcft_identity(False)
        assert missing["status"] == "missing_moduli_chain_correction"
        assert missing["total_identity_holds"] is False

        corrected = corrected_tcft_identity(True)
        assert corrected["status"] == "proved_total_identity_under_correction_datum"
        assert corrected["total_identity_holds"] is True
        assert corrected["per_k_identity_holds"] is False
        assert corrected["raw_operator_identified"] is False

    def test_hh_minus_two_vanishes_only_under_all_hypotheses(self):
        proved = hh_minus_two_filtration_vanishes(
            complete=True,
            exhaustive=True,
            separated=True,
            strongly_convergent=True,
            empty_total_degree_minus_two_line=True,
        )
        assert proved["vanishes"] is True
        assert proved["missing_hypotheses"] == []

        missing = hh_minus_two_filtration_vanishes(
            complete=True,
            exhaustive=True,
            separated=True,
            strongly_convergent=False,
            empty_total_degree_minus_two_line=True,
        )
        assert missing["vanishes"] is False
        assert missing["status"] == "not_established"
        assert missing["missing_hypotheses"] == ["strongly_convergent"]

    def test_formal_frobenius_case_preserved(self):
        formal = formal_frobenius_case(
            higher_operations_vanish=True,
            frobenius_invariant_product=True,
        )
        assert formal["status"] == "proved_formal_frobenius_case"
        assert formal["sufficient_for_termwise_target"] is True

        nonformal = formal_frobenius_case(
            higher_operations_vanish=False,
            frobenius_invariant_product=True,
        )
        assert nonformal["status"] == "not_established"
        assert nonformal["higher_commutators_vanish"] is False

    def test_mixed_complex_axiom_boundary(self):
        result = verify_mixed_complex_axiom_prerequisite()
        assert result["status"] == "proved_for_classical_B0"
        assert result["classical_B0"] is True
        assert result["raw_hierarchy_connes_only"] is False
        assert result["corrected_tcft_requires_moduli_chain_correction"] is True
        assert result["used_in_decomposition"] is False


class TestCYDimensionVerdicts:
    """CY dimension summaries must not assert universal strict vanishing."""

    def test_cy3_not_proved_termwise(self):
        result = obs_ainf_cy3(max_k=8)
        assert result["status"] == "not_proved_termwise"
        assert result["all_bidegrees_unique"] is True
        assert result["unique_bidegrees_prove_vanishing"] is False
        assert result["termwise_universal_vanishing"] is False

    def test_cy2_not_promoted_by_projection(self):
        result = obs_ainf_cy2(max_k=8)
        assert result["status"] == "not_proved_termwise"
        assert result["unique_bidegrees_prove_vanishing"] is False

    def test_general_cy_requires_tcft_or_hh_hypotheses(self):
        for d in range(3, 7):
            result = obs_ainf_general(d, max_k=8)
            assert result["status"] == "not_proved_termwise"
            assert "HH^{-2}" in result["proof_obligation"]

    def test_dimension_analysis_relevant_pairs(self):
        analysis = CYDimensionAnalysis(cy_dim=3, max_k=10, target_j=2)
        assert analysis.relevant_commutators() == [
            (3, 2),
            (4, 2),
            (5, 2),
            (6, 2),
            (7, 2),
            (8, 2),
            (9, 2),
            (10, 2),
        ]
        assert analysis.all_bidegrees_unique()


class TestNonAdjacentAndManuscript:
    """The non-adjacent gap is named, not erased."""

    def test_non_adjacent_gap_not_resolved_by_bidegree(self):
        res = resolve_non_adjacent_gap(3)
        assert isinstance(res, NonAdjacentResolution)
        assert res.k == 3
        assert res.j == 2
        assert res.gap_resolved is False
        assert "not resolved by bidegree" in res.resolution()
        assert "moduli-chain" in res.resolution()

    def test_adjacent_and_non_adjacent_descriptions(self):
        res = NonAdjacentResolution(k=4)
        assert "cyclic" in res.adjacent_terms_description().lower()
        assert "outside" in res.non_adjacent_terms_description().lower()

    def test_manuscript_implications_do_not_upgrade(self):
        impl = manuscript_implications()
        assert isinstance(impl, ManuscriptImplications)
        assert impl.prop_status_before == "ClaimStatusConditional"
        assert impl.prop_status_after == "ClaimStatusConditional"
        assert impl.gap_resolved is False
        assert "rejected" in impl.proof_method_after

    def test_landscape_updates_record_repair(self):
        updates = manuscript_implications().landscape_updates()
        assert len(updates) == 3
        assert any("nonzero" in row["after"] for row in updates)
        assert any("HH^{-2}" in row["after"] for row in updates)


class TestMasterResolution:
    """The master object records the corrected carriers without reviving the old claim."""

    def test_master_is_not_universal_termwise_resolution(self):
        res = master_resolution()
        assert isinstance(res, ConnesBObsAinfResolution)
        assert res.resolved is False
        assert res.decomposition.obs_ainf_resolved() is False
        assert res.cy3_result["status"] == "not_proved_termwise"
        assert res.non_adjacent.gap_resolved is False

    def test_master_records_all_corrected_carriers(self):
        res = master_resolution()
        assert res.corrected_carriers_recorded is True
        assert res.witness.nonzero
        assert res.corrected_tcft["total_identity_holds"]
        assert res.hh_minus_two["vanishes"]
        assert res.mixed_complex["classical_B0"]
