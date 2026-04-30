r"""Tests for the repaired Tsygan/Costello obstruction engine.

The regression target is the false strengthening:

    Tsygan-Costello formality proves [m_k, B^{(2)}_term] = 0, or at least
    exact, and therefore closes the compact S^3-framing programme.

The corrected facts are:

* the raw termwise operator has a strict nonzero cyclic CY3 witness;
* Costello concerns a corrected TCFT operator with correction data;
* a cohomological statement is conditional on a named complex, comparison
  map, and hypotheses.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path

from compute.lib.tsygan_formality_obs_ainf import (
    COMPARISON_MAP,
    DERIVED_E1_COMPLEX,
    FILTERED_HYPOTHESIS,
    OBSTRUCTION_COMPLEX,
    ChainVsCohomologyDistinction,
    CostelloTCFTFormality,
    GapAnalysis,
    LocalP2Data,
    NonAdjacentContractionTerm,
    TsyganComparison,
    TsyganFormalityData,
    compute_commutator_m3_b2_local_p2,
    compute_non_adjacent_terms_local_p2,
    construct_proof,
    count_non_adjacent_terms,
    enumerate_non_adjacent_terms,
    non_adjacent_term_table,
    resolve_obs_ainf,
    strict_cyclic_cy3_witness,
    upgraded_obstruction_landscape,
    verify_tsygan_resolution,
)

F = Fraction

ROOT = Path(__file__).resolve().parents[2]
STANDALONE = ROOT / "standalone" / "m3_b2_obstruction_vol3.tex"

PAIRING = {
    ("e", "w"): F(1),
    ("w", "e"): F(1),
    ("a", "b"): F(1),
    ("b", "a"): F(1),
}


def terminal_slot_b2(word):
    """Independent terminal-slot B_term convention from the standalone."""
    word = tuple(word)
    terminal = word[-1]
    out = Counter()
    for idx, entry in enumerate(word[:-1]):
        coeff = PAIRING.get((entry, terminal), F(0))
        if coeff:
            reduced = word[:idx] + word[idx + 1:-1]
            out[reduced] += coeff
    return Counter({key: value for key, value in out.items() if value})


def m3_bar(word, alpha=F(1)):
    """Independent strict witness operation m_3(a,a,a)=alpha b."""
    word = tuple(word)
    out = Counter()
    for start in range(len(word) - 2):
        if word[start:start + 3] == ("a", "a", "a"):
            reduced = word[:start] + ("b",) + word[start + 3:]
            out[reduced] += alpha
    return Counter({key: value for key, value in out.items() if value})


def compose(first, second, word):
    total = Counter()
    for mid, coeff_mid in first(word).items():
        for out, coeff_out in second(mid).items():
            total[out] += coeff_mid * coeff_out
    return Counter({key: value for key, value in total.items() if value})


def subtract(left, right):
    total = Counter(left)
    for key, value in right.items():
        total[key] -= value
    return Counter({key: value for key, value in total.items() if value})


class TestTsyganMixedComplexScope:
    """Tsygan formality is not a raw B^{(2)}_term theorem."""

    def test_mixed_complex_applies_but_raw_b2_not_covered(self):
        data = TsyganFormalityData()
        assert data.applies_to_cy3()
        assert data.applies_to_cy_d(5)
        assert data.preserves_mixed_complex
        assert data.preserves_connes_operator
        assert not data.raw_b2_termwise_covered

    def test_no_chain_or_class_vanishing_from_tsygan_alone(self):
        data = TsyganFormalityData()
        assert not data.gives_chain_level_vanishing()
        assert not data.gives_cohomological_vanishing()
        assert data.requires_b2_comparison_data()
        assert data.formality_level == "mixed-complex quasi-isomorphism"


class TestCostelloCorrectedOperator:
    """Costello's theorem is a corrected total TCFT identity."""

    def test_corrected_b2_available_in_cy3(self):
        data = CostelloTCFTFormality(cy_dimension=3)
        assert data.connes_hierarchy_levels() == 4
        assert data.b2_is_formal()
        assert data.full_hierarchy_formal()
        assert data.total_tcft_identity_holds()

    def test_no_raw_or_per_k_identity(self):
        data = CostelloTCFTFormality(cy_dimension=3)
        assert not data.termwise_identity_holds()
        assert not data.raw_term_operator_identified()
        assert not data.formality_map_explicit()

    def test_b2_not_available_in_cy1(self):
        data = CostelloTCFTFormality(cy_dimension=1)
        assert data.connes_hierarchy_levels() == 2
        assert not data.b2_is_formal()
        assert not data.total_tcft_identity_holds()


class TestStrictCyclicCY3Witness:
    """Exact arithmetic for the strict nonzero witness."""

    def test_engine_witness_is_nonzero(self):
        result = strict_cyclic_cy3_witness()
        assert result["B_term_then_m3"] == Counter({("b",): F(4)})
        assert result["m3_then_B_term"] == Counter({("b",): F(2)})
        assert result["commutator"] == Counter({("b",): F(2)})
        assert result["commutator"] == result["expected"]
        assert not result["chain_level_vanishing"]
        assert not result["cohomological_vanishing_established"]
        assert result["comparison_data_required"]

    def test_independent_recomputation_matches_engine(self):
        word = ("a", "a", "a", "a", "b")
        b2_then_m3 = compose(terminal_slot_b2, m3_bar, word)
        m3_then_b2 = compose(m3_bar, terminal_slot_b2, word)
        commutator = subtract(b2_then_m3, m3_then_b2)
        assert terminal_slot_b2(word) == Counter({("a", "a", "a"): F(4)})
        assert b2_then_m3 == Counter({("b",): F(4)})
        assert m3_then_b2 == Counter({("b",): F(2)})
        assert commutator == strict_cyclic_cy3_witness()["commutator"]

    def test_alpha_scaling(self):
        result = strict_cyclic_cy3_witness(alpha=F(3, 2))
        assert result["commutator"] == Counter({("b",): F(3)})
        assert result["expected"] == Counter({("b",): F(3)})


class TestGapAndNonAdjacentTerms:
    """Raw non-adjacent contractions are not killed by cyclicity or Tsygan."""

    def test_gap_remains_for_raw_target(self):
        gap = GapAnalysis()
        assert gap.gap_exists_chain_level()
        assert not gap.gap_closed_cohomology()
        assert gap.chain_level_gap
        assert gap.cohomology_level_gap
        assert "HH^{-2}" in gap.why_cohomology_suffices()
        assert "theta_TCFT" in gap.why_cohomology_suffices()

    def test_non_adjacent_terms_start_at_bar_length_five(self):
        assert count_non_adjacent_terms(3, 3) == 0
        assert count_non_adjacent_terms(4, 3) == 0
        assert count_non_adjacent_terms(5, 3) > 0

    def test_non_adjacent_term_requires_comparison(self):
        term = NonAdjacentContractionTerm(
            bar_length=6,
            mk_arity=3,
            mk_start=1,
            contraction_inside=2,
            contraction_outside=5,
        )
        assert not term.is_adjacent()
        assert not term.controlled_by_cyclic_invariance()
        assert not term.controlled_by_tsygan_formality()
        assert term.requires_tcft_comparison()

    def test_table_matches_enumeration(self):
        table = non_adjacent_term_table(max_bar_length=8, mk_arity=3)
        assert len(table) == 6
        for row in table:
            terms = enumerate_non_adjacent_terms(row["bar_length"], 3)
            assert row["non_adjacent"] == len(terms)


class TestProofObligationChain:
    """The proof chain rejects the false theorem and names the conditional one."""

    def test_repaired_steps(self):
        steps = construct_proof()
        assert len(steps) == 6
        assert [step.number for step in steps] == [1, 2, 3, 4, 5, 6]
        statuses = [step.status for step in steps]
        assert "computed" in statuses
        assert "Costello" in statuses
        assert "conditional" in statuses
        assert "rejected" in statuses

    def test_no_step_asserts_universal_exactness(self):
        text = " ".join(step.statement + " " + step.justification for step in construct_proof())
        assert "d(h_k)" not in text
        assert "universal raw exactness" not in text.lower()
        assert "B_term^{(2)}" in text
        assert "B_TCFT^{(2)}" in text


class TestComparisonData:
    """Cohomological vanishing is conditional on named comparison data."""

    def test_default_comparison_is_not_sufficient(self):
        comp = TsyganComparison()
        assert comp.obstruction_complex == OBSTRUCTION_COMPLEX
        assert comp.comparison_map == COMPARISON_MAP
        assert comp.filtered_complex == DERIVED_E1_COMPLEX
        assert comp.filtered_hypothesis == FILTERED_HYPOTHESIS
        assert not comp.sufficient_for_programme()
        assert not comp.gap_resolved

    def test_corrected_tcft_comparison_is_conditionally_sufficient(self):
        comp = TsyganComparison.with_corrected_tcft_comparison()
        assert comp.obstruction_class_formulated
        assert comp.comparison_map_named
        assert comp.corrected_tcft_operator
        assert comp.sufficient_for_programme()

    def test_hh_minus_two_filtration_is_conditionally_sufficient(self):
        comp = TsyganComparison.with_hh_minus_two_filtration()
        assert comp.obstruction_class_formulated
        assert comp.hh_minus_two_filtration
        assert comp.sufficient_for_programme()

    def test_status_strings_name_the_distinction(self):
        comp = TsyganComparison()
        assert "strictly nonzero" in comp.chain_level_status()
        assert "B_TCFT" in comp.difference_from_strict_vanishing()
        assert "theta_TCFT" in comp.difference_from_strict_vanishing()


class TestChainVsCohomology:
    """No unconditional raw homotopy-coherent vanishing remains."""

    def test_raw_levels_are_not_resolved(self):
        distinction = ChainVsCohomologyDistinction()
        assert not distinction.chain_level_identity_holds()
        assert not distinction.cohomological_vanishing_holds()
        assert not distinction.homotopy_coherent_vanishing_holds()
        assert not distinction.non_formal_gap_resolved()

    def test_formal_case_remains_strict(self):
        distinction = ChainVsCohomologyDistinction()
        assert distinction.formal_algebras_are_strict()
        need = distinction.which_is_needed_for_programme()
        assert "HH^{-2}" in need
        assert "theta_TCFT" in need


class TestLocalP2AndSchematicComputation:
    """Local P2 remains a noncompact guide, not a compact closure theorem."""

    def test_local_p2_data_nonformal(self):
        data = LocalP2Data()
        dims = data.ext_dimensions()
        assert not data.is_formal()
        assert data.has_nontrivial_m3()
        assert sum(dims.values()) == data.generator_count()
        assert dims[0] == 3
        assert dims[3] == 3

    def test_local_p2_non_adjacent_report_is_conditional(self):
        result = compute_non_adjacent_terms_local_p2(bar_length=5)
        assert result["non_adjacent_count"] > 0
        assert not result["chain_level_vanishing"]
        assert not result["cohomological_vanishing"]
        assert not result["cohomological_vanishing_established"]
        assert result["comparison_data_required"]

    def test_commutator_report_contains_strict_witness(self):
        result = compute_commutator_m3_b2_local_p2(bar_length=5)
        assert result["non_adjacent_terms"] > 0
        assert not result["chain_level_vanishing"]
        assert not result["cohomological_vanishing"]
        assert result["strict_witness"]["commutator"] == Counter({("b",): F(2)})


class TestResolutionAndLandscape:
    """The master status is rejected by default and conditional with data."""

    def test_default_resolution_rejects_raw_target(self):
        res = resolve_obs_ainf()
        assert not res.obs_ainf_vanishes_cohomologically()
        assert "Rejected" in res.proposition_status()
        summary = res.summary()
        assert "rejected" in summary["main_result"].lower()
        assert "B_TCFT" in summary["costello"]
        assert any("termwise" in item for item in summary["does_NOT_prove"])

    def test_resolution_with_named_tcft_comparison_is_conditional(self):
        comp = TsyganComparison.with_corrected_tcft_comparison()
        res = resolve_obs_ainf(comparison=comp)
        assert res.obs_ainf_vanishes_cohomologically()
        assert "Conditional class statement" in res.proposition_status()

    def test_master_verification_reports_repair(self):
        result = verify_tsygan_resolution()
        assert "Universal raw termwise" in result["main_result"]
        assert "2 alpha [b]" in result["main_result"]
        assert "Conditional" in result["cohomological_statement"]

    def test_landscape_no_longer_closes_compact_cases_by_tsygan(self):
        landscape = upgraded_obstruction_landscape()
        assert "nonzero" in landscape["local_P^2"]["Obs_Ainf"]
        assert "not closed by Tsygan alone" in landscape["K3_x_E"]["Obs_Ainf"]
        assert "conditional" in landscape["quintic"]["Obs_Ainf"]
        assert "fully resolved" not in landscape["local_P^2"]["total"]


class TestStandaloneAlignment:
    """The engine stays aligned with the standalone obstruction note."""

    def test_standalone_names_three_carriers(self):
        text = STANDALONE.read_text()
        assert r"B^{(2)}_{\mathrm{term}}" in text
        assert r"B^{(2)}_{\TCFT}" in text
        assert r"\HH^{-2}_{E_1}(A,A)" in text
        assert "No equality" in text

    def test_standalone_rejects_per_k_strengthening(self):
        text = STANDALONE.read_text()
        assert r"\{\,\sum_k b_k,\ B^{(2)}_{\TCFT}\,\}=0" in text
        assert "stronger than the TCFT theorem" in text
