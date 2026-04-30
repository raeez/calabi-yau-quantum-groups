r"""Tests for the attack-healed derived framing obstruction engine.

The test surface enforces the repaired claims:

* raw ``B^{(2)}_term`` has a strict nonzero ``m_3`` witness;
* Costello supplies only the corrected total TCFT identity after a
  correction datum;
* ``HH^{-2}`` vanishing is conditional on explicit filtration/comparison
  hypotheses;
* formal higher-carrier absence is preserved;
* Hopf/derived Level 3 data do not automatically close the strict compact
  CY_3 problem.
"""

from fractions import Fraction

from compute.lib.derived_framing_obstruction import (
    BottPeriodicityData,
    CrossCheckResult,
    CY3LandscapeEntry,
    DerivedFramingObstructionResult,
    EnHochschildData,
    ExplicitHomotopyData,
    FrancisGaitsgoryComplex,
    GoodwillieLayerData,
    HHMinusTwoFiltrationHypotheses,
    LiftingObstruction,
    MasterDerivedFramingResult,
    TCFTCorrectionDatum,
    TermwiseCommutatorWitness,
    complete_hh_minus_two_hypotheses,
    complete_tcft_correction_datum,
    compute_bott_periodicity,
    compute_cy3_landscape,
    compute_derived_framing_obstruction,
    compute_en_hochschild,
    compute_fg_complex,
    compute_goodwillie_layers,
    construct_explicit_homotopy,
    master_derived_framing_analysis,
    master_verification,
    obstruction_vanishes_for_all_cy3,
    perform_cross_checks,
    strict_m3_b2_term_witness,
    the_theorem,
    verify_bott_periodicity_tower,
    verify_negative_degree_vanishing,
    verify_unit_connectedness_landscape,
)
from compute.lib.derived_vs_drinfeld_infty import framing_obstruction_boundary
from compute.lib.stasheff_cancellation_obs_ainf import (
    strict_m3_b2_term_witness as stasheff_witness,
)

F = Fraction


# ================================================================
# SECTION 1: RAW TERMwise WITNESS
# ================================================================


class TestRawTermwiseWitness:
    """Raw ``B^{(2)}_term`` is not a TCFT vanishing theorem."""

    def test_witness_exact_arithmetic(self):
        witness = strict_m3_b2_term_witness(alpha=F(1))
        assert isinstance(witness, TermwiseCommutatorWitness)
        assert witness.input_word == ("a", "a", "a", "a", "b")
        assert witness.b2_term_of_input == {("a", "a", "a"): F(4)}
        assert witness.m3_after_b2_term == {("b",): F(4)}
        assert witness.b2_term_after_m3 == {("b",): F(2)}
        assert witness.commutator == {("b",): F(2)}
        assert witness.coefficient_on_b == F(2)
        assert witness.nonzero

    def test_witness_scales_with_alpha(self):
        witness = strict_m3_b2_term_witness(alpha=F(3, 5))
        assert witness.coefficient_on_b == F(6, 5)
        assert witness.nonzero

    def test_witness_matches_repaired_stasheff_engine(self):
        ours = strict_m3_b2_term_witness(alpha=F(7, 3))
        theirs = stasheff_witness(alpha=F(7, 3))
        assert ours.input_word == theirs.input_word
        assert ours.coefficient_on_b == theirs.coefficient_on_b
        assert ours.nonzero == theirs.nonzero


# ================================================================
# SECTION 2: HYPOTHESIS OBJECTS
# ================================================================


class TestHypotheses:
    """TCFT and HH hypotheses are explicit data."""

    def test_default_tcft_datum_does_not_prove_identity(self):
        datum = TCFTCorrectionDatum()
        assert not datum.total_tcft_identity_available
        assert "Costello moduli-chain correction terms" in datum.missing_hypotheses
        assert "chosen corrected representative B^{(2)}_TCFT" in datum.missing_hypotheses

    def test_complete_tcft_datum_proves_corrected_total_identity(self):
        datum = complete_tcft_correction_datum()
        assert datum.total_tcft_identity_available
        assert datum.missing_hypotheses == []

    def test_unit_connectedness_alone_is_not_hh_minus_two_theorem(self):
        hyp = HHMinusTwoFiltrationHypotheses(connective_unit_connected_model=True)
        assert not hyp.vanishing_established
        assert "empty total degree -2 first-page line" in hyp.missing_hypotheses
        assert "comparison map to S^3 obstruction complex" in hyp.missing_hypotheses

    def test_complete_hh_minus_two_hypotheses(self):
        hyp = complete_hh_minus_two_hypotheses()
        assert hyp.vanishing_established
        assert hyp.missing_hypotheses == []


# ================================================================
# SECTION 3: E_1-HOCHSCHILD DATA
# ================================================================


class TestEnHochschildData:
    """Negative-degree vanishing is conditional, not automatic."""

    def test_unit_connected_default_records_unknown_hh_minus_two(self):
        hh = compute_en_hochschild("Local P^2", "M", 3, is_formal=False)
        assert isinstance(hh, EnHochschildData)
        assert hh.is_unit_connected
        assert hh.dim_at(0) == 1
        assert hh.dim_at(-2) is None
        assert not hh.negative_degrees_vanish()
        assert hh.obstruction_group_e2_to_e3() is None

    def test_complete_hypotheses_give_hh_minus_two_zero(self):
        hh = compute_en_hochschild(
            "Local P^2",
            "M",
            3,
            is_formal=False,
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert hh.dim_at(-2) == 0
        assert hh.obstruction_group_e2_to_e3() == 0
        assert hh.negative_degrees_vanish()

    def test_positive_class_g_data_is_retained(self):
        hh = compute_en_hochschild("C^3", "G", 3)
        assert hh.dim_at(1) == 1
        assert hh.dim_at(2) == 2
        assert hh.dim_at(3) == 3

    def test_verify_negative_degree_vanishing_requires_hypotheses(self):
        default = verify_negative_degree_vanishing("G", max_neg=3)
        proved = verify_negative_degree_vanishing(
            "G",
            max_neg=3,
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert list(default.values()) == [None, None, None]
        assert list(proved.values()) == [0, 0, 0]


# ================================================================
# SECTION 4: DERIVED FRAMING OBSTRUCTION RESULT
# ================================================================


class TestDerivedFramingObstruction:
    """The main result separates formal, raw, TCFT, and HH carriers."""

    def test_nonformal_default_rejects_universal_vanishing(self):
        result = compute_derived_framing_obstruction(
            "Local P^2", 3, "M", is_formal=False, has_nonzero_m3=True
        )
        assert isinstance(result, DerivedFramingObstructionResult)
        assert not result.strict_commutator_vanishes
        assert result.raw_termwise_witness is not None
        assert result.raw_termwise_witness.coefficient_on_b == F(2)
        assert not result.total_commutator_vanishes
        assert not result.derived_hh_vanishing_established
        assert not result.obstruction_vanishes
        assert result.universal_vanishing_claim_rejected
        assert not result.strict_compact_cy3_closed
        assert "HH^{-2}" in result.derived_explanation

    def test_formal_case_preserves_higher_carrier_absence(self):
        result = compute_derived_framing_obstruction(
            "C^3", 3, "G", is_formal=True, has_nonzero_m3=False
        )
        assert result.strict_commutator_vanishes
        assert result.raw_termwise_witness is None
        assert "formal" in result.strict_explanation.lower()
        assert not result.obstruction_vanishes
        assert not result.strict_compact_cy3_closed

    def test_complete_hypotheses_give_conditional_primary_vanishing(self):
        result = compute_derived_framing_obstruction(
            "Local P^2",
            3,
            "M",
            is_formal=False,
            has_nonzero_m3=True,
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert result.total_commutator_vanishes
        assert result.corrected_tcft_identity_established
        assert result.derived_hh_vanishing_established
        assert result.obstruction_group_dim == 0
        assert result.obstruction_vanishes
        assert result.required_hypotheses == []
        assert result.lifting_obstruction.primary_obs_dim == 0
        assert not result.lifting_obstruction.space_contractible
        assert not result.lifting_obstruction.higher_obs_all_zero

    def test_cross_arity_cancellation_not_claimed_for_raw_term(self):
        result = compute_derived_framing_obstruction(
            "Local P^2",
            3,
            "M",
            is_formal=False,
            has_nonzero_m3=True,
            tcft_hypotheses=complete_tcft_correction_datum(),
        )
        assert result.total_commutator_vanishes
        assert not result.cross_arity_cancellation
        assert "carrier conflation" in result.reconciliation

    def test_lifting_obstruction_default_is_open(self):
        result = compute_derived_framing_obstruction(
            "Local P^2", 3, "M", is_formal=False, has_nonzero_m3=True
        )
        obstruction = result.lifting_obstruction
        assert isinstance(obstruction, LiftingObstruction)
        assert obstruction.primary_obs_degree == -2
        assert obstruction.primary_obs_dim is None
        assert obstruction.status == "open_requires_HH_minus_two_hypotheses"


# ================================================================
# SECTION 5: CY_3 LANDSCAPE
# ================================================================


class TestCY3Landscape:
    """The landscape is diagnostic, not a universal closure table."""

    def test_landscape_size_and_types(self):
        landscape = compute_cy3_landscape()
        assert len(landscape) == 7
        assert all(isinstance(entry, CY3LandscapeEntry) for entry in landscape)
        assert any("P^2" in entry.name and entry.has_m3 for entry in landscape)
        assert any("C^3" in entry.name and entry.is_formal for entry in landscape)

    def test_default_landscape_does_not_vanish_universally(self):
        landscape = compute_cy3_landscape()
        assert all(entry.derived_level == "requires_HH_minus_two_hypotheses" for entry in landscape)
        assert all(entry.homotopy_level == "requires_tcft_correction_datum" for entry in landscape)
        assert all(entry.obstruction_group_dim is None for entry in landscape)
        assert not obstruction_vanishes_for_all_cy3()

    def test_nonformal_entries_record_raw_nonzero(self):
        landscape = compute_cy3_landscape()
        nonformal = [entry for entry in landscape if entry.has_m3]
        assert len(nonformal) >= 1
        assert all(entry.strict_level == "raw_nonzero" for entry in nonformal)

    def test_complete_hypotheses_make_the_statement_conditional(self):
        assert obstruction_vanishes_for_all_cy3(
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        landscape = compute_cy3_landscape(
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert all(entry.homotopy_level == "conditional_corrected_total" for entry in landscape)
        assert all(entry.derived_level == "conditional_primary_class_vanishes" for entry in landscape)
        assert all(entry.obstruction_group_dim == 0 for entry in landscape)


# ================================================================
# SECTION 6: GOODWILLIE AND FRANCIS-GAITSGORY
# ================================================================


class TestGoodwillieLayers:
    """Goodwillie layers do not all vanish from unit-connectedness."""

    def test_default_layers_are_open(self):
        layers = compute_goodwillie_layers("Local P^2", max_layer=4)
        assert all(isinstance(layer, GoodwillieLayerData) for layer in layers)
        assert all(not layer.vanishes for layer in layers)
        assert all(layer.obstruction_dim is None for layer in layers)

    def test_hh_hypothesis_kills_primary_layer_only(self):
        layers = compute_goodwillie_layers(
            "Local P^2",
            max_layer=4,
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert layers[0].vanishes
        assert layers[0].obstruction_dim == 0
        assert all(not layer.vanishes for layer in layers[1:])
        assert any("Goodwillie convergence" in layers[i].required_hypotheses[-1] for i in range(1, 4))

    def test_goodwillie_convergence_is_explicit_extra_hypothesis(self):
        layers = compute_goodwillie_layers(
            "Local P^2",
            max_layer=4,
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
            goodwillie_convergence_hypothesis=True,
        )
        assert all(layer.vanishes for layer in layers)


class TestFrancisGaitsgoryComplex:
    """The FG complex is conditional at H^2."""

    def test_unit_connected_alone_is_not_unobstructed(self):
        fg = compute_fg_complex("Local P^2", is_unit_connected=True)
        assert isinstance(fg, FrancisGaitsgoryComplex)
        assert not fg.is_unobstructed
        assert fg.h2 is None
        assert "unit_connected_but_HH_minus_two_not_proved" == fg.status

    def test_complete_hh_hypotheses_kill_h2(self):
        fg = compute_fg_complex(
            "Local P^2",
            is_unit_connected=True,
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert fg.is_unobstructed
        assert fg.h2 == 0
        assert fg.h0 is None
        assert fg.h1 is None

    def test_non_unit_connected_can_have_obstructions(self):
        fg = compute_fg_complex("non-CY", is_unit_connected=False)
        assert not fg.is_unobstructed
        assert fg.h2 == 2
        assert "unit-connected" in fg.required_hypotheses[0]


# ================================================================
# SECTION 7: HOMOTOPY AND BOTT DIAGNOSTICS
# ================================================================


class TestExplicitHomotopy:
    """Corrected homotopy data is not raw termwise cancellation."""

    def test_formal_homotopy_is_trivial_absence(self):
        homotopy = construct_explicit_homotopy(is_formal=True, has_m3=False)
        assert isinstance(homotopy, ExplicitHomotopyData)
        assert homotopy.exists
        assert not homotopy.is_costello_tcft
        assert homotopy.uses_raw_b2_term
        assert homotopy.status == "formal_trivial_higher_carrier_absent"

    def test_nonformal_default_homotopy_is_open(self):
        homotopy = construct_explicit_homotopy(is_formal=False, has_m3=True)
        assert not homotopy.exists
        assert not homotopy.total_cancellation
        assert not homotopy.uses_raw_b2_term
        assert "Costello" in " ".join(homotopy.required_hypotheses)

    def test_complete_tcft_gives_corrected_total_homotopy(self):
        homotopy = construct_explicit_homotopy(
            is_formal=False,
            has_m3=True,
            tcft_hypotheses=complete_tcft_correction_datum(),
        )
        assert homotopy.exists
        assert homotopy.is_costello_tcft
        assert homotopy.total_cancellation
        assert not homotopy.uses_raw_b2_term
        assert homotopy.cancellation_pairs == []


class TestBottPeriodicity:
    """Topological vanishing is not compact CY_3 closure."""

    def test_d3_topological_vanishes_but_does_not_close(self):
        bott = compute_bott_periodicity(3)
        assert isinstance(bott, BottPeriodicityData)
        assert bott.pi_d_BU == 0
        assert bott.pi_d_BSp == 0
        assert bott.topological_obstruction_vanishes
        assert not bott.closes_strict_compact_cy3

    def test_d2_has_nontrivial_bu(self):
        bott = compute_bott_periodicity(2)
        assert bott.pi_d_BU == 1
        assert not bott.topological_obstruction_vanishes

    def test_bott_tower_records_no_compact_closure(self):
        tower = verify_bott_periodicity_tower(max_d=6)
        assert tower[3]["topological_vanishes"]
        assert not tower[3]["closes_strict_compact_cy3"]
        assert tower[5]["pi_d_BSp"] == 2


# ================================================================
# SECTION 8: CROSS-CHECKS AND BOUNDARY
# ================================================================


class TestCrossChecks:
    """Neighboring repaired engines agree on the proof boundary."""

    def test_cross_checks_pass_by_rejecting_overclaims(self):
        result = compute_derived_framing_obstruction(
            "Local P^2", 3, "M", is_formal=False, has_nonzero_m3=True
        )
        checks = perform_cross_checks(result)
        assert isinstance(checks, CrossCheckResult)
        assert checks.all_consistent
        assert checks.raw_termwise_rejected
        assert checks.no_compact_cy3_closure_claim
        assert checks.zte_independent

    def test_derived_vs_drinfeld_boundary_matches(self):
        boundary = framing_obstruction_boundary()
        result = compute_derived_framing_obstruction(
            "Local P^2", 3, "M", is_formal=False, has_nonzero_m3=True
        )
        assert not boundary.raw_termwise_vanishing
        assert not boundary.compact_cy3_global_construction_proved
        assert result.universal_vanishing_claim_rejected
        assert not result.strict_compact_cy3_closed
        assert any("degree -2" in hyp or "HH" in hyp for hyp in boundary.required_hypotheses)


# ================================================================
# SECTION 9: MASTER RESULT AND ALIASES
# ================================================================


class TestMasterResult:
    """The master result states the corrected conditional theorem."""

    def test_master_default_rejects_universal_closure(self):
        result = master_derived_framing_analysis()
        assert isinstance(result, MasterDerivedFramingResult)
        assert result.chain_level_nonvanishing_is_obstruction
        assert not result.derived_obstruction_vanishes
        assert result.universal_vanishing_claim_rejected
        assert not result.strict_compact_cy3_closed
        assert len(result.remaining_proof_obligations) >= 3
        assert "Conditional corrected proposition" in result.theorem_statement

    def test_master_with_complete_primary_hypotheses_is_still_not_contractibility(self):
        result = master_derived_framing_analysis(
            tcft_hypotheses=complete_tcft_correction_datum(),
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )
        assert result.derived_obstruction_vanishes
        assert result.local_p2_result.obstruction_group_dim == 0
        assert not result.local_p2_result.lifting_obstruction.space_contractible
        assert not result.strict_compact_cy3_closed

    def test_master_verification_alias(self):
        result = master_verification()
        assert isinstance(result, MasterDerivedFramingResult)
        assert result.universal_vanishing_claim_rejected

    def test_the_theorem_is_conditional(self):
        statement = the_theorem()
        assert "Conditional corrected proposition" in statement
        assert "B^(2)_term" in statement
        assert "HH^{-2}" in statement
        assert "None of this constructs compact CY_3" in statement

    def test_unit_connectedness_landscape_is_not_hh_proof(self):
        data = verify_unit_connectedness_landscape()
        assert all(data.values())
        assert len(data) >= 5
        hh = compute_en_hochschild("generic CY3", "G", 3)
        assert hh.dim_at(-2) is None
