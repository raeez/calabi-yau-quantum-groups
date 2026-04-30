r"""Tests for the corrected Lurie E_3 obstruction engine.

These tests assert the attack-healed boundary:

* raw B_term^(2) has the strict nonzero witness
  [m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b];
* B_term^(2), Costello's B_TCFT^(2), and the derived HH^{-2} carrier are
  distinct;
* Lurie/Dunn/Goodwillie data identify conditional targets, not automatic
  compact CY3 closure;
* HH^{-2} vanishing is recorded only under the explicit comparison and
  filtration hypotheses.
"""

from fractions import Fraction as F

from compute.lib.lurie_e3_obstruction import (
    carrier_separation,
    complete_hh_minus_two_hypotheses,
    compute_aq_cohomology,
    compute_aq_landscape,
    compute_cotangent_complex,
    compute_fg_deformation_aq,
    compute_goodwillie_derivative,
    compute_goodwillie_tower,
    compute_k3e_aq,
    compute_local_p2_aq,
    cross_check_with_dunn,
    d4_vanishes_for_all_cy3,
    default_hh_minus_two_hypotheses,
    master_lurie_e3_analysis,
    raw_m3_b2_witness,
    the_proposition,
    verify_dunn_equivalence,
    verify_dunn_equivalence_landscape,
)


class TestRawCarrierBoundary:
    """Raw termwise witness and carrier separation."""

    def test_raw_witness_nonzero(self):
        witness = raw_m3_b2_witness()

        assert witness.input_word == ("a", "a", "a", "a", "b")
        assert witness.b_term_of_input == {("a", "a", "a"): F(4)}
        assert witness.m3_after_b_term == {("b",): F(4)}
        assert witness.b_term_after_m3 == {("b",): F(2)}
        assert witness.coefficient_on_b == F(2)
        assert witness.nonzero
        assert "2 [b]" in witness.formula

    def test_raw_witness_scales_by_alpha(self):
        witness = raw_m3_b2_witness(F(3, 2))

        assert witness.coefficient_on_b == F(3)
        assert witness.m3_after_b_term == {("b",): F(6)}
        assert witness.b_term_after_m3 == {("b",): F(3)}
        assert witness.nonzero

    def test_carrier_separation(self):
        carriers = carrier_separation()

        assert carriers.raw_operator == "B_term^(2)"
        assert carriers.corrected_operator == "B_TCFT^(2)"
        assert carriers.derived_target == "HH^{-2}_{E_1}(A,A)"
        assert not carriers.raw_equals_corrected
        assert carriers.raw_witness.nonzero
        assert carriers.tcft_identity_requires_correction_datum
        assert carriers.derived_target_requires_comparison_map
        assert not carriers.compact_cy3_closure_follows


class TestConditionalHHMinusTwo:
    """HH^{-2} is conditional on the full filtration/comparison package."""

    def test_default_hypotheses_are_not_a_proof(self):
        hypotheses = default_hh_minus_two_hypotheses()

        assert hypotheses.structural_identifications_available
        assert not hypotheses.vanishing_established
        assert "comparison map to S^3 obstruction complex" in hypotheses.missing_hypotheses
        assert "empty total-degree -2 first-page line" in hypotheses.missing_hypotheses

    def test_complete_hypotheses_prove_only_derived_target(self):
        hypotheses = complete_hh_minus_two_hypotheses()
        aq = compute_aq_cohomology(
            "Local P^2",
            "M",
            3,
            False,
            hh_hypotheses=hypotheses,
        )

        assert hypotheses.vanishing_established
        assert aq.d4_dim == 0
        assert aq.d4_vanishes
        assert aq.d4_status == "proved_under_HH_minus_two_filtration_hypotheses"
        assert not aq.proves_compact_cy3_closure

    def test_unit_connectedness_alone_keeps_d4_unknown(self):
        aq = compute_aq_cohomology("Local P^2", "M", 3, False)

        assert aq.is_unit_connected
        assert aq.d4_dim is None
        assert not aq.d4_vanishes
        assert aq.dim_at(2) == 3
        assert aq.dim_at(4) is None
        assert "not_established" in aq.d4_status


class TestGoodwillieAndDunn:
    """Goodwillie/Dunn structures survive as conditional identifications."""

    def test_goodwillie_metadata_without_convergence_is_not_vanishing(self):
        gw3 = compute_goodwillie_derivative(3, is_unit_connected=True)

        assert gw3.k == 3
        assert gw3.coefficient_space == "S^{2}"
        assert gw3.tensor_power == 3
        assert gw3.symmetry_group == "S_3"
        assert gw3.symmetry_order == 6
        assert gw3.pi_0_vanishes is None
        assert not gw3.proves_hh_minus_two
        assert not gw3.proves_compact_cy3_closure
        assert "Goodwillie tower strong convergence" in gw3.missing_hypotheses

    def test_goodwillie_layer_conditional_vanishing(self):
        gw3 = compute_goodwillie_derivative(
            3,
            is_unit_connected=True,
            strong_convergence=True,
            derived_limits_killed=True,
        )

        assert gw3.pi_0_vanishes is True
        assert gw3.proves_hh_minus_two
        assert not gw3.proves_compact_cy3_closure

    def test_goodwillie_tower_preserves_layer_metadata(self):
        tower = compute_goodwillie_tower(max_k=6)

        assert len(tower) == 6
        assert [layer.k for layer in tower] == [1, 2, 3, 4, 5, 6]
        assert [layer.symmetry_order for layer in tower] == [1, 2, 6, 24, 120, 720]
        assert tower[2].pi_0_vanishes is None

    def test_dunn_identification_without_hh_hypotheses(self):
        eq = verify_dunn_equivalence("Local P^2", "M", False)

        assert eq.structural_identification_available
        assert eq.d4_e2_dim is None
        assert eq.hh_minus2_e1_dim is None
        assert not eq.agree
        assert not eq.vanishing_established
        assert not eq.proves_compact_cy3_closure
        assert "vanishing not established" in eq.identification_chain[-1]

    def test_dunn_identification_under_complete_hypotheses(self):
        hypotheses = complete_hh_minus_two_hypotheses()
        eq = verify_dunn_equivalence(
            "Local P^2",
            "M",
            False,
            hh_hypotheses=hypotheses,
        )

        assert eq.structural_identification_available
        assert eq.d4_e2_dim == 0
        assert eq.hh_minus2_e1_dim == 0
        assert eq.agree
        assert eq.vanishing_established
        assert not eq.proves_compact_cy3_closure


class TestExamplesAndLandscape:
    """Example-level boundaries: local P^2, K3 x E, and the standard list."""

    def test_local_p2_raw_failure_not_compact_closure(self):
        p2 = compute_local_p2_aq()

        assert p2.shadow_class == "M"
        assert p2.has_m3
        assert p2.chain_level_fails
        assert p2.raw_witness.coefficient_on_b == F(2)
        assert p2.d4_dim is None
        assert not p2.d4_vanishes
        assert p2.d2_dim == 3
        assert not p2.compact_cy3_closed

    def test_local_p2_conditional_d4_vanishing_keeps_raw_failure(self):
        p2 = compute_local_p2_aq(complete_hh_minus_two_hypotheses())

        assert p2.chain_level_fails
        assert p2.raw_witness.nonzero
        assert p2.d4_dim == 0
        assert p2.d4_vanishes
        assert not p2.compact_cy3_closed

    def test_k3e_keeps_de_rham_and_categorical_formality_separate(self):
        k3e = compute_k3e_aq()

        assert k3e.k3_formal
        assert k3e.e_formal
        assert not k3e.k3_categorical_formality_certified
        assert not k3e.e_categorical_formality_certified
        assert not k3e.product_a_infinity_model_certified
        assert k3e.d4_product is None
        assert not k3e.d4_product_vanishes
        assert k3e.kappa_ch == 0
        assert k3e.kappa_ch_Heis == 3
        assert k3e.mukai_rank == 24
        assert not k3e.compact_cy3_closed

    def test_landscape_default_has_no_slogan_vanishing(self):
        landscape = compute_aq_landscape()

        assert len(landscape) == 7
        assert any(entry.shadow_class == "M" for entry in landscape)
        assert all(entry.dunn_identification_available for entry in landscape)
        assert all(entry.d4_dim is None for entry in landscape)
        assert not any(entry.d4_vanishes for entry in landscape)
        assert not any(entry.compact_cy3_closed for entry in landscape)

    def test_landscape_complete_hypotheses_are_conditional(self):
        landscape = compute_aq_landscape(complete_hh_minus_two_hypotheses())

        assert len(landscape) == 7
        assert all(entry.d4_dim == 0 for entry in landscape)
        assert all(entry.d4_vanishes for entry in landscape)
        assert all(entry.agrees_with_dunn for entry in landscape)
        assert not any(entry.compact_cy3_closed for entry in landscape)


class TestMasterAndConvenience:
    """Master result and compatibility aliases."""

    def test_master_default_rejects_compact_closure_by_slogan(self):
        result = master_lurie_e3_analysis()

        assert result.carrier_separation.raw_witness.nonzero
        assert not result.d4_vanishes_all_cy3
        assert result.goodwillie_3rd_vanishes is None
        assert not result.agrees_with_dunn_approach
        assert not result.obstruction_space_contractible
        assert not result.compact_cy3_closed
        assert not result.compact_closure_by_slogan
        assert "compact Hall/CoHA correspondence" in result.remaining_obligations

    def test_master_complete_hypotheses_still_do_not_close_compact_cy3(self):
        result = master_lurie_e3_analysis(complete_hh_minus_two_hypotheses())

        assert result.d4_vanishes_all_cy3
        assert result.goodwillie_3rd_vanishes is True
        assert result.agrees_with_dunn_approach
        assert not result.obstruction_space_contractible
        assert not result.compact_cy3_closed
        assert not result.compact_closure_by_slogan

    def test_proposition_is_conditional_and_names_raw_boundary(self):
        prop = the_proposition()

        assert "conditional" in prop.lower()
        assert "comparison map" in prop
        assert "empty total-degree -2 line" in prop
        assert "B_term^(2)" in prop
        assert "B_TCFT^(2)" in prop
        assert "2 [b]" in prop
        assert "No compact CY3" in prop

    def test_convenience_checks_default_false_complete_true(self):
        complete = complete_hh_minus_two_hypotheses()

        assert not d4_vanishes_for_all_cy3()
        assert not cross_check_with_dunn()
        assert not any(verify_dunn_equivalence_landscape().values())
        assert d4_vanishes_for_all_cy3(complete)
        assert cross_check_with_dunn(complete)
        assert all(verify_dunn_equivalence_landscape(complete).values())


class TestCotangentAndFG:
    """Cotangent and FG targets are structural, not compact closure proofs."""

    def test_cotangent_shift_preserved_but_not_a_vanishing_theorem(self):
        ct = compute_cotangent_complex("Local P^2")

        assert ct.min_degree == 1
        assert ct.is_concentrated_positive
        assert ct.relative_shift == 2
        assert ct.relative_min_degree == 3
        assert "Sigma^2" in ct.structural_identification
        assert not ct.proves_hh_minus_two
        assert not ct.proves_compact_cy3_closure

    def test_fg_default_is_not_unobstructed(self):
        fg = compute_fg_deformation_aq("Local P^2", "M")

        assert fg.source_operad == "E_2"
        assert fg.target_operad == "E_3"
        assert fg.fiber_h2 is None
        assert not fg.is_unobstructed
        assert fg.status == "not_established"
        assert "comparison map to S^3 obstruction complex" in fg.missing_hypotheses

    def test_fg_complete_hypotheses_unobstructed_only_conditionally(self):
        fg = compute_fg_deformation_aq(
            "Local P^2",
            "M",
            hh_hypotheses=complete_hh_minus_two_hypotheses(),
        )

        assert fg.fiber_h0 == 0
        assert fg.fiber_h1 == 0
        assert fg.fiber_h2 == 0
        assert fg.is_unobstructed
        assert fg.status == "proved_under_HH_minus_two_filtration_hypotheses"
