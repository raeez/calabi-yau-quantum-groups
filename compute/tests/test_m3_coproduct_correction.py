r"""Tests for the AP-CY34 m3/coproduct correction boundary.

The corrected oracle enforces:

* raw ``B_term^{(2)}`` / raw bar-coproduct cancellation fails by the
  strict witness ``[m_3,B_term^{(2)}][a|a|a|a|b] = 2 alpha [b]``;
* Costello's corrected carrier is ``B_TCFT^{(2)}``, not the raw term;
* closure is conditional on explicit TCFT comparison data or the precise
  ``HH^{-2}`` filtration theorem;
* diagnostic slogans do not imply universal compact CY3 conclusions.
"""

from fractions import Fraction

import pytest

from compute.lib.chain_level_m2_b2_cancellation import (
    strict_m3_bterm2_witness as chain_level_witness,
)
from compute.lib.m3_coproduct_correction_engine import (
    CORRECTED_OPERATOR,
    FORBIDDEN_DIAGNOSTICS,
    FORBIDDEN_UNIVERSAL_CONCLUSIONS,
    RAW_COPRODUCT,
    RAW_OPERATOR,
    STRICT_WITNESS_FORMULA,
    CorrectionDataRequired,
    HHMinusTwoFiltrationTheorem,
    M3CoproductCorrection,
    RawM3CoproductWitness,
    TCFTCorrectionDatum,
    complete_hh_minus_two_filtration_theorem,
    complete_tcft_correction_datum,
    compute_delta3_T0,
    compute_raw_witness,
    diagnostic_attempt,
    m3_coproduct_correction_verdict,
    strict_m3_coproduct_witness,
    verify_all,
)

F = Fraction


class TestStrictRawWitness:
    """The raw term has the exact nonzero AP-CY34 witness."""

    def test_exact_arithmetic_default_alpha(self):
        witness = strict_m3_coproduct_witness(F(1))
        assert isinstance(witness, RawM3CoproductWitness)
        assert witness.input_word == ("a", "a", "a", "a", "b")
        assert witness.raw_operator == RAW_OPERATOR
        assert witness.raw_coproduct == RAW_COPRODUCT
        assert witness.corrected_operator == CORRECTED_OPERATOR
        assert witness.raw_b_term_of_input == {("a", "a", "a"): F(4)}
        assert witness.m3_after_raw_b_term == {("b",): F(4)}
        assert witness.raw_b_term_after_m3 == {("b",): F(2)}
        assert witness.commutator == {("b",): F(2)}
        assert witness.coefficient_on_b == F(2)
        assert witness.nonzero_for_alpha_nonzero
        assert witness.raw_cancellation_blocked
        assert not witness.raw_equals_corrected
        assert witness.formula == STRICT_WITNESS_FORMULA

    @pytest.mark.parametrize("alpha", [F(1, 2), F(3, 5), F(-2), F(0)])
    def test_alpha_scaling(self, alpha):
        witness = strict_m3_coproduct_witness(alpha)
        assert witness.coefficient_on_b == F(2) * alpha
        assert witness.nonzero_for_alpha_nonzero is (alpha != 0)
        assert witness.raw_cancellation_blocked is (alpha != 0)

    def test_cross_check_against_chain_level_engine(self):
        alpha = F(7, 3)
        ours = strict_m3_coproduct_witness(alpha).summary()
        theirs = chain_level_witness(alpha)
        assert ours["formula"] == theirs["formula"]
        assert ours["coefficient_on_b"] == theirs["coefficient_of_[b]"]
        assert ours["expected_coefficient_on_b"] == theirs["expected_coefficient"]
        assert ours["nonzero_for_alpha_nonzero"] == theirs["nonzero_for_alpha_nonzero"]
        assert theirs["corrected_operator_used"] is False

    def test_compute_raw_witness_entry_point(self):
        report = compute_raw_witness(F(5, 4))
        assert report["coefficient_on_b"] == F(5, 2)
        assert report["raw_equals_corrected"] is False
        assert report["raw_cancellation_blocked"] is True


class TestConditionalClosureData:
    """Closure requires explicit corrected data."""

    def test_default_tcft_datum_is_incomplete(self):
        datum = TCFTCorrectionDatum()
        assert not datum.complete
        assert "supply B_TCFT^{(2)}" in datum.missing_hypotheses
        assert "comparison map from B_term^{(2)} to B_TCFT^{(2)}" in (
            datum.missing_hypotheses
        )

    def test_complete_tcft_datum_is_sufficient_for_conditional_identity(self):
        datum = complete_tcft_correction_datum()
        verdict = m3_coproduct_correction_verdict(F(1), tcft_datum=datum)
        assert datum.complete
        assert verdict.tcft_identity_established
        assert verdict.obs_ainf_zero_established
        assert verdict.status == "conditional closure by corrected B_TCFT^{(2)} route"
        assert not verdict.hh_minus_two_zero_established
        assert not verdict.compact_phi3_established
        assert not verdict.hall_coha_established
        assert not verdict.pbw_established
        assert not verdict.no_extra_relations_established

    def test_default_hh_theorem_is_incomplete(self):
        theorem = HHMinusTwoFiltrationTheorem(comparison_map=True)
        assert not theorem.complete
        assert "complete HH^{-2} filtration" in theorem.missing_hypotheses
        assert "exhaustive HH^{-2} filtration" in theorem.missing_hypotheses
        assert "separated HH^{-2} filtration" in theorem.missing_hypotheses
        assert "strong convergence to HH^{-2}" in theorem.missing_hypotheses
        assert "empty total-degree -2 line" in theorem.missing_hypotheses

    def test_complete_hh_theorem_is_sufficient_for_conditional_vanishing(self):
        theorem = complete_hh_minus_two_filtration_theorem()
        verdict = m3_coproduct_correction_verdict(F(1), hh_theorem=theorem)
        assert theorem.complete
        assert verdict.hh_minus_two_zero_established
        assert verdict.obs_ainf_zero_established
        assert verdict.status == "conditional closure by HH^{-2} filtration route"
        assert not verdict.tcft_identity_established
        assert not verdict.contractible_lifting_space_established
        assert not verdict.compact_phi3_established
        assert not verdict.hall_coha_established
        assert not verdict.pbw_established

    def test_default_verdict_keeps_closure_open(self):
        verdict = m3_coproduct_correction_verdict(F(1))
        assert not verdict.raw_cancellation_valid
        assert not verdict.raw_equals_corrected
        assert not verdict.tcft_identity_established
        assert not verdict.hh_minus_two_zero_established
        assert not verdict.obs_ainf_zero_established
        assert verdict.status == "open: raw witness blocks cancellation"
        assert "supply B_TCFT^{(2)}" in verdict.remaining_obligations
        assert "HH^{-2} comparison map" in verdict.remaining_obligations


class TestForbiddenDiagnostics:
    """Diagnostic slogans do not imply compact CY3 closure."""

    @pytest.mark.parametrize("diagnostic", FORBIDDEN_DIAGNOSTICS)
    @pytest.mark.parametrize("conclusion", FORBIDDEN_UNIVERSAL_CONCLUSIONS)
    def test_forbidden_diagnostic_conclusion_pairs_are_rejected(
        self,
        diagnostic,
        conclusion,
    ):
        attempt = diagnostic_attempt(diagnostic, conclusion)
        assert attempt["rejected"] is True
        assert attempt["allowed"] is False
        assert diagnostic in attempt["reason"]
        assert conclusion in attempt["reason"]

    def test_unknown_pairs_are_not_marked_as_ap_cy34_pairs(self):
        attempt = diagnostic_attempt("explicit B_TCFT datum", "Obs_Ainf=0")
        assert attempt["rejected"] is False
        assert attempt["allowed"] is True


class TestCompatibilityWrapper:
    """The legacy class now exposes the AP-CY34 boundary."""

    def test_psi_parameter_maps_to_alpha(self):
        engine = M3CoproductCorrection(Psi=F(2), N_max=4)
        witness = engine.strict_witness()
        assert engine.alpha == F(1, 2)
        assert witness.coefficient_on_b == F(1)
        assert witness.raw_cancellation_blocked

    def test_legacy_raw_delta3_matrix_is_rejected(self):
        engine = M3CoproductCorrection(alpha=F(1))
        with pytest.raises(CorrectionDataRequired, match="No raw matrix"):
            engine.delta3_T(0)

    def test_corrected_coproduct_requires_data(self):
        engine = M3CoproductCorrection(alpha=F(1))
        with pytest.raises(CorrectionDataRequired, match="requires B_TCFT"):
            engine.corrected_coproduct_T(0)

    def test_corrected_coproduct_records_conditional_route(self):
        engine = M3CoproductCorrection(alpha=F(1))
        record = engine.corrected_coproduct_T(
            0,
            tcft_datum=complete_tcft_correction_datum(),
        )
        assert record["operator"] == CORRECTED_OPERATOR
        assert record["conditional"] is True
        assert record["raw_matrix_supplied"] is False
        assert record["compact_phi3_established"] is False
        assert record["hall_coha_established"] is False
        assert record["pbw_established"] is False
        assert record["no_extra_relations_established"] is False

    def test_legacy_compute_delta3_T0_entry_point_is_boundary_report(self):
        report = compute_delta3_T0(Psi=F(2), N_max=4)
        assert report["legacy_entry_point"] == "compute_delta3_T0"
        assert report["raw_delta3_matrix_supplied"] is False
        assert report["witness"]["coefficient_on_b"] == F(1)
        assert report["raw_cancellation_valid"] is False
        assert report["obs_ainf_zero_established"] is False


class TestMasterVerification:
    """Top-level verification aggregates the AP-CY34 checks."""

    def test_verify_all(self):
        report = verify_all(F(1))
        assert report["all_ok"] is True
        assert report["strict_witness"]["coefficient_on_b"] == F(2)
        assert report["default_verdict"]["raw_cancellation_valid"] is False
        assert report["tcft_conditional_verdict"]["obs_ainf_zero_established"] is True
        assert report["hh_conditional_verdict"]["hh_minus_two_zero_established"] is True
        assert all(item["rejected"] for item in report["diagnostic_checks"])
