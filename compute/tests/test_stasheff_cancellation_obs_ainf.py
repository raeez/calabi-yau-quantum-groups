r"""Tests for the attack-healed Stasheff--B^{(2)} obstruction engine.

The test surface enforces the corrected claims:

* raw ``B^{(2)}_term`` has a strict nonzero ``m_3`` witness;
* the old per-k and bidegree proofs do not establish universal closure;
* degree bookkeeping survives only as diagnostic partner-slot data;
* a total cancellation statement is conditional on corrected TCFT and
  HH^{-2} comparison hypotheses.
"""

from fractions import Fraction

from compute.lib.stasheff_cancellation_obs_ainf import (
    BidegreeDecomposition,
    ConnesHierarchySpec,
    TCFTCorrectionData,
    analyze_corrected_tcft,
    analyze_obs_ainf_formal,
    analyze_obs_ainf_nonformal,
    build_formal_cyclic_algebra,
    compute_stasheff_cancellation_obs_ainf,
    corrected_proposition,
    strict_m3_b2_term_witness,
    verify_formal_algebra,
    weight_identities_cy3,
)

F = Fraction


# ================================================================
#  SECTION 1: DEGREE BOOKKEEPING
# ================================================================


class TestConnesHierarchyDiagnostic:
    """Degree arithmetic retained as diagnostic data."""

    def test_cy3_has_four_corrected_hierarchy_levels(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        assert spec.levels == [0, 1, 2, 3]

    def test_bk_bar_length_degrees(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        assert spec.b_k_degree(1) == 0
        assert spec.b_k_degree(2) == -1
        assert spec.b_k_degree(3) == -2

    def test_corrected_hierarchy_degree_shifts(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        assert spec.degree_shift(0) == 1
        assert spec.degree_shift(1) == -1
        assert spec.degree_shift(2) == -3
        assert spec.degree_shift(3) == -5

    def test_commutator_degree(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        assert spec.commutator_degree(3, 2) == -5
        assert spec.commutator_output(3, 2, 10) == 5

    def test_same_weight_same_output(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        pairs = spec.bidegree_grouping(7)
        assert set(pairs) == {(7, 0), (5, 1), (3, 2), (1, 3)}
        outputs = {spec.commutator_output(k, j, 10) for k, j in pairs}
        assert outputs == {5}

    def test_different_weight_different_output(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        outputs = {}
        for s in range(1, 8):
            pairs = spec.bidegree_grouping(s)
            if pairs:
                k, j = pairs[0]
                outputs[s] = spec.commutator_output(k, j, 10)
        assert len(set(outputs.values())) == len(outputs)


class TestBidegreeDiagnostic:
    """Same-degree partner slots are not cancellation proofs."""

    def test_b3_b2_has_same_degree_partner_slots(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        decomp = BidegreeDecomposition(cy_dim=3, hierarchy=spec)
        result = decomp.b2_cancellation_partners(3)
        assert result["total_weight"] == 7
        assert set(result["same_degree_partners"]) == {(7, 0), (5, 1), (1, 3)}
        assert not result["termwise_cancellation_established"]
        assert result["requires_tcft_correction_datum"]

    def test_identity_at_weight_is_conditional(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        decomp = BidegreeDecomposition(cy_dim=3, hierarchy=spec)
        identity = decomp.identity_at_weight(7)
        assert (3, 2) in identity["pairs"]
        assert identity["identity_status"] == "conditional_tcft"
        assert not identity["proves_termwise_vanishing"]

    def test_formal_case_is_limited(self):
        spec = ConnesHierarchySpec(cy_dim=3)
        decomp = BidegreeDecomposition(cy_dim=3, hierarchy=spec)
        formal = decomp.formal_case()
        assert formal["formal"]
        assert not formal["termwise_universal_vanishing"]
        assert "m_k=0 for k>=3" in formal["consequence"]


# ================================================================
#  SECTION 2: FORMAL ALGEBRA SANITY CHECK
# ================================================================


class TestFormalAlgebra:
    """The formal Frobenius algebra remains a valid bookkeeping check."""

    def test_generators(self):
        alg = build_formal_cyclic_algebra()
        assert alg.N == 2
        assert alg.cy_dim == 1

    def test_m2_product(self):
        alg = build_formal_cyclic_algebra()
        assert alg.m_k((0, 0)) == [(0, F(1))]
        assert alg.m_k((0, 1)) == [(1, F(1))]
        assert alg.m_k((1, 0)) == [(1, F(1))]
        assert alg.m_k((1, 1)) == []

    def test_associativity(self):
        alg = build_formal_cyclic_algebra()
        result = alg.verify_stasheff(max_arity=4)
        assert result[3]["passed"]
        assert result[4]["passed"]

    def test_cyclic_invariance(self):
        alg = build_formal_cyclic_algebra()
        assert alg.verify_cyclic_invariance(2)["passed"]

    def test_pairing_nondegeneracy(self):
        alg = build_formal_cyclic_algebra()
        assert alg.pairing(0, 1) == F(1)
        assert alg.pairing(1, 0) == F(1)
        assert alg.pairing(0, 0) == F(0)
        assert alg.pairing(1, 1) == F(0)


# ================================================================
#  SECTION 3: STRICT NONZERO WITNESS
# ================================================================


class TestTermwiseWitness:
    """Raw B^{(2)}_term has a strict nonzero witness."""

    def test_exact_witness_arithmetic(self):
        witness = strict_m3_b2_term_witness(alpha=F(1))
        assert witness.input_word == ("a", "a", "a", "a", "b")
        assert witness.b2_term_of_input == {("a", "a", "a"): F(4)}
        assert witness.m3_after_b2_term == {("b",): F(4)}
        assert witness.m3_of_input == {("b", "a", "b"): F(1), ("a", "b", "b"): F(1)}
        assert witness.b2_term_after_m3 == {("b",): F(2)}
        assert witness.commutator == {("b",): F(2)}

    def test_witness_scales_with_alpha(self):
        witness = strict_m3_b2_term_witness(alpha=F(3, 5))
        assert witness.coefficient_on_b == F(6, 5)
        assert witness.nonzero


# ================================================================
#  SECTION 4: OBSTRUCTION ANALYSIS
# ================================================================


class TestObsAinfAnalysis:
    """Formal, non-formal, and corrected-TCFT statuses are separated."""

    def test_formal_higher_obstruction_absent(self):
        analysis = analyze_obs_ainf_formal()
        assert analysis.obs_ainf_zero
        assert analysis.is_formal
        assert analysis.individual_mk_b2_vanish
        assert not analysis.raw_termwise_witness_nonzero

    def test_nonformal_raw_termwise_does_not_vanish(self):
        analysis = analyze_obs_ainf_nonformal()
        assert not analysis.obs_ainf_zero
        assert not analysis.is_formal
        assert not analysis.individual_mk_b2_vanish
        assert analysis.raw_termwise_witness_nonzero
        assert "strict" in analysis.mechanism.lower()

    def test_corrected_tcft_requires_all_data_for_derived_vanishing(self):
        partial = analyze_corrected_tcft(
            TCFTCorrectionData(
                moduli_chain_corrections=True,
                open_closed_tcft_chain_map=True,
                comparison_to_obstruction_complex=False,
                hh_minus_two_filtration_theorem=False,
            )
        )
        assert partial.corrected_tcft_identity_established
        assert not partial.derived_hh_vanishing_established
        assert not partial.obs_ainf_zero

        complete = analyze_corrected_tcft(
            TCFTCorrectionData(
                moduli_chain_corrections=True,
                open_closed_tcft_chain_map=True,
                comparison_to_obstruction_complex=True,
                hh_minus_two_filtration_theorem=True,
            )
        )
        assert complete.corrected_tcft_identity_established
        assert complete.derived_hh_vanishing_established
        assert complete.obs_ainf_zero


# ================================================================
#  SECTION 5: CORRECTED PROPOSITION STATUS
# ================================================================


class TestCorrectedProposition:
    """The old closure theorem is rejected, not silently re-proved."""

    def test_original_claim_incorrect(self):
        result = corrected_proposition()
        assert "INCORRECT" in result["original_status"]
        assert result["termwise_witness"]["coefficient_on_b"] == F(2)

    def test_old_proofs_rejected(self):
        result = corrected_proposition()
        assert result["old_per_k_proof_status"] == "REJECTED"
        assert result["old_bidegree_proof_status"] == "REJECTED"

    def test_corrected_claim_is_conditional(self):
        result = corrected_proposition()
        assert result["corrected_status"] == "Conditional"
        assert not result["universal_obs_ainf_zero"]
        assert "Costello correction data" in result["corrected_claim"]


# ================================================================
#  SECTION 6: CY_3 WEIGHT DIAGNOSTICS
# ================================================================


class TestWeightIdentities:
    """CY_3 weight groups are conditional TCFT diagnostics."""

    def test_weight_7_contains_target(self):
        ids = weight_identities_cy3()
        assert 7 in ids
        assert (3, 2) in ids[7]["pairs"]
        assert set(ids[7]["pairs"]) == {(7, 0), (5, 1), (3, 2), (1, 3)}

    def test_weight_entries_do_not_prove_vanishing(self):
        ids = weight_identities_cy3()
        for data in ids.values():
            assert data["identity_status"] == "conditional_tcft"
            assert not data["proves_termwise_vanishing"]
            assert "corrected TCFT" in data["requires"]


# ================================================================
#  SECTION 7: MASTER VERDICT
# ================================================================


class TestMasterResult:
    """The top-level engine reports rejection plus proof obligations."""

    def test_gap_classified_but_not_universally_resolved(self):
        result = compute_stasheff_cancellation_obs_ainf()
        assert result.gap_classified
        assert not result.gap_resolved
        assert result.universal_closure_rejected

    def test_universal_obs_ainf_zero_rejected(self):
        result = compute_stasheff_cancellation_obs_ainf()
        assert not result.obs_ainf_vanishes
        assert result.formal_analysis.obs_ainf_zero
        assert not result.nonformal_analysis.obs_ainf_zero
        assert result.termwise_witness.nonzero

    def test_original_claim_corrected(self):
        result = compute_stasheff_cancellation_obs_ainf()
        assert not result.original_claim_correct
        assert not result.nonformal_analysis.individual_mk_b2_vanish

    def test_proof_steps_name_the_failure(self):
        result = compute_stasheff_cancellation_obs_ainf()
        assert any("2 alpha [b]" in step for step in result.proof_steps)
        assert any("Costello correction data" in step for step in result.proof_steps)

    def test_formal_algebra_passes_all_checks(self):
        result = verify_formal_algebra()
        for data in result["stasheff"].values():
            assert data["passed"]
        assert result["cyclic_invariance_m2"]["passed"]

    def test_summary_keys(self):
        result = compute_stasheff_cancellation_obs_ainf()
        summary = result.summary()
        expected_keys = {
            "gap_classified",
            "gap_resolved",
            "original_claim_correct",
            "corrected_claim",
            "mechanism",
            "obs_ainf_vanishes",
            "universal_closure_rejected",
            "formal_obs_ainf",
            "nonformal_obs_ainf",
            "raw_witness_nonzero",
            "remaining_proof_obligations",
        }
        assert expected_keys <= set(summary.keys())
        assert len(summary["remaining_proof_obligations"]) == 3
