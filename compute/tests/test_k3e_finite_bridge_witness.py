from dataclasses import replace
from fractions import Fraction

import compute.lib.k3e_finite_bridge_witness as k3e_witness_module
from compute.lib.k3e_finite_bridge_witness import (
    K3E_CLOSURE_BRIDGES,
    K3EClosureWitnesses,
    bar_witness,
    brst_central_charge_gate,
    brst_coefficient_fixture,
    brst_coefficient_fixture_transition,
    brst_borcherds_bracket_gate,
    brst_borcherds_serre_relation_gate,
    brst_no_ghost_spectral_sequence_gate,
    brst_momentum_height_projection_gate,
    brst_witness,
    bridge_obstruction_record,
    bridge_proof_obligation_matrix,
    k3e_theorem_boundary_report,
    k3e_gap_status_table,
    k3e_gap_crosswalk_report,
    k3e_closure_criterion_report,
    k3e_bridge_specification,
    k3e_bridge_axiom_pack,
    k3e_proof_dependency_graph,
    k3e_proof_roadmap_report,
    k3e_proof_task_map,
    k3e_core_gap_report,
    k3e_bridge_audit_report,
    finite_bridge_exactness_step_report,
    finite_bridge_system_exactness_report,
    finite_bridge_exactness_tower_report,
    finite_cyclic_sdr_block_compatibility_gate,
    finite_drinfeld_double_datum_gate,
    finite_total_cech_ran_maurer_cartan_gate,
    finite_simplicial_cyclic_contraction_gate,
    finite_bridge_witness,
    finite_bridge_system_transition_report,
    finite_bridge_transition_square,
    finite_bar_ce_report,
    finite_bar_ce_chain_map_gate,
    finite_bar_lattice_grading_report,
    finite_bar_regularization_report,
    finite_compact_hall_product_gate,
    finite_compact_support_beck_chevalley_gate,
    finite_realized_cy3_shifted_bracket_gate,
    finite_realized_hcs_hall_composite_gate,
    finite_realized_composite_transition_ml_gate,
    finite_rees_vanishing_cycle_realization_gate,
    finite_scattering_quantum_torus_gate,
    finite_scattering_root_report,
    finite_stokes_hcs_hall_source_gate,
    rademacher_polar_bessel_gate,
    rademacher_truncation_error_gate,
    source_recognition_record,
    rademacher_finite_height_certificate,
    rademacher_witness,
    scattering_witness,
    yangian_witness,
    yangian_current_candidate_packet,
    yangian_current_packet_transition,
    yangian_label_tower_transition,
    yangian_brst_residue_chain_gate,
    yangian_ope_coefficient_transition,
    yangian_ope_serre_ideal_span_gate,
    yangian_pbw_associated_graded_gate,
    yangian_residue_transition,
    yangian_spectral_kernel_label_packet,
    yangian_spectral_kernel_transition,
    yangian_self_ope_pole_layer_packet,
    yangian_self_ope_pole_transition,
    yangian_spectral_associator_obstruction_packet,
    yangian_spectral_associator_transition,
    yangian_spectral_r_matrix_equation_gate,
)


def assert_full_inverse_limit_gate(gate, owner=None):
    if owner is not None:
        assert gate.owner == owner
    assert gate.component_scope == ("scatt", "bar", "rad", "BRST", "Yang")
    assert gate.all_required
    assert gate.heightwise_maps_realized
    assert gate.rank_zero_transition_squares
    assert gate.source_transition_surjective
    assert gate.target_transition_surjective
    assert gate.kernel_transition_well_defined
    assert gate.kernel_transition_surjective
    assert gate.image_transition_well_defined
    assert gate.image_transition_surjective
    assert gate.cokernel_transition_well_defined
    assert gate.cokernel_transition_surjective
    assert gate.proved_conditions == ()
    assert gate.open_conditions == gate.required_conditions
    assert gate.all_proved is False
    assert gate.status == "OPEN_REQUIREMENT"
    assert "upper kernels land inside lower kernels" in gate.required_conditions
    assert "upper images land inside lower images" in gate.required_conditions
    assert "cokernel transition maps are surjective" in gate.required_conditions


def assert_full_pro_recognition_gate(gate, owner=None):
    if owner is not None:
        assert gate.owner == owner
    assert gate.all_required
    assert gate.separated_completion
    assert gate.defect_ideal_exactness
    assert gate.heegner_borcherds_coefficient_comparison
    assert gate.proved_conditions == ()
    assert gate.open_conditions == gate.required_conditions
    assert gate.all_proved is False
    assert gate.status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert any(condition.startswith("Q_H^sep:") for condition in gate.required_conditions)
    assert any(condition.startswith("L_H^ex:") for condition in gate.required_conditions)
    assert any(condition.startswith("H_H^HB:") for condition in gate.required_conditions)


def assert_bridge_requirement(requirement, bridge):
    assert requirement.bridge == bridge
    assert requirement.status == "open"
    assert requirement.finite_symbol
    assert requirement.source_object
    assert requirement.target_object
    assert requirement.construction_obligations
    assert requirement.compatibility_obligations
    assert requirement.existing_finite_witnesses
    assert requirement.forbidden_promotions
    assert requirement.all_obligations == (
        requirement.construction_obligations + requirement.compatibility_obligations
    )
    assert_full_inverse_limit_gate(requirement.inverse_limit_gate, bridge)
    assert requirement.inverse_limit_status == "OPEN_REQUIREMENT"
    assert requirement.proved_inverse_limit_conditions == ()
    assert requirement.open_inverse_limit_conditions == requirement.inverse_limit_gate.required_conditions


def assert_proved_bridge_requirement(requirement, bridge):
    assert requirement.bridge == bridge
    assert requirement.status == "proved"
    assert requirement.all_obligations == (
        requirement.construction_obligations + requirement.compatibility_obligations
    )
    assert requirement.inverse_limit_status == "PROVED"
    assert requirement.proved_inverse_limit_conditions == requirement.inverse_limit_gate.required_conditions
    assert requirement.open_inverse_limit_conditions == ()


def complete_closure_witnesses(report):
    return K3EClosureWitnesses(
        source_gate_closed=True,
        source_recognition_envelope_completed=True,
        bridge_constructions=K3E_CLOSURE_BRIDGES,
        inverse_limit_proved_conditions=report.inverse_limit_gate.required_conditions,
        pro_recognition_proved_conditions=report.pro_recognition_gate.required_conditions,
    )


def assert_open_theorem_schema(entry):
    assert entry.status == "OPEN_THEOREM_SCHEMA"
    assert entry.proved_here is False
    assert entry.open_obligations
    assert entry.open_obligations[0].startswith(
        "establish theorem-schema hypothesis:"
    )
    assert any(
        "cokernel transition maps are surjective" == obligation
        for obligation in entry.open_obligations
    )


def assert_proved_theorem_schema(entry):
    assert entry.status == "PROVED_THEOREM_SCHEMA"
    assert entry.proved_here is True
    assert entry.open_obligations == ()


def test_finite_matrix_helpers_reject_dimension_truncation():
    import pytest

    with pytest.raises(ValueError, match="matrix width"):
        k3e_witness_module._matrix_vector_product(
            ((Fraction(1), Fraction(2)),),
            (Fraction(1),),
        )
    with pytest.raises(ValueError, match="left matrix width"):
        k3e_witness_module._matrix_product(
            ((Fraction(1), Fraction(2)),),
            ((Fraction(1),),),
        )
    with pytest.raises(ValueError, match="left matrix width"):
        k3e_witness_module._matrix_product(
            ((Fraction(1),),),
            (),
        )
    with pytest.raises(ValueError, match="common width"):
        k3e_witness_module._matrix_transpose(
            ((Fraction(1), Fraction(0)), (Fraction(1),)),
        )
    with pytest.raises(ValueError, match="common width"):
        k3e_witness_module._column_vector_rank(
            ((Fraction(1), Fraction(0)), (Fraction(1),)),
        )
    with pytest.raises(ValueError, match="common width"):
        k3e_witness_module._matrix_difference(
            ((Fraction(1), Fraction(0)), (Fraction(1),)),
            ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(1))),
        )
    with pytest.raises(ValueError, match="common width"):
        k3e_witness_module._matrix_horizontal_concat(
            ((Fraction(1), Fraction(0)), (Fraction(1),)),
            ((Fraction(0),), (Fraction(1),)),
        )
    with pytest.raises(ValueError, match="common width"):
        k3e_witness_module._matrix_rref(
            ((Fraction(1), Fraction(0)), (Fraction(1),)),
        )
    with pytest.raises(ValueError, match="common width"):
        k3e_witness_module._matrix_nullspace_basis(
            ((Fraction(1), Fraction(0)), (Fraction(1),)),
        )


def test_inverse_limit_gate_requirement_distinguishes_required_from_proved():
    gate = k3e_witness_module.k3e_inverse_limit_gate_requirement("gate_status_test")
    assert gate.status == "OPEN_REQUIREMENT"
    assert gate.all_required is True
    assert gate.all_proved is False
    assert gate.proved_conditions == ()
    assert gate.open_conditions == gate.required_conditions

    partial = replace(gate, proved_conditions=gate.required_conditions[:2])
    assert partial.status == "OPEN_REQUIREMENT"
    assert partial.all_proved is False
    assert partial.open_conditions == gate.required_conditions[2:]

    proved = replace(gate, proved_conditions=gate.required_conditions)
    assert proved.status == "PROVED"
    assert proved.all_proved is True
    assert proved.open_conditions == ()


def test_pro_recognition_gate_requirement_distinguishes_required_from_proved():
    gate = k3e_witness_module.k3e_pro_recognition_gate_requirement("pro_gate_status_test")
    assert_full_pro_recognition_gate(gate, "pro_gate_status_test")

    partial = replace(gate, proved_conditions=gate.required_conditions[:1])
    assert partial.status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert partial.all_proved is False
    assert partial.open_conditions == gate.required_conditions[1:]

    proved = replace(gate, proved_conditions=gate.required_conditions)
    assert proved.status == "PROVED"
    assert proved.all_proved is True
    assert proved.open_conditions == ()


def test_scattering_witness_low_height():
    witness = scattering_witness(8)
    assert witness.contains_polar_root is True
    assert witness.contains_lightlike_root is True
    assert witness.contains_first_imaginary_root is True
    assert -1 in witness.support
    assert 0 in witness.support
    assert 3 in witness.support
    assert 4 in witness.support


def _rank_two_torus_fixture(height_cutoff=3):
    vectors = [
        (i, j)
        for i in range(height_cutoff + 1)
        for j in range(height_cutoff + 1)
        if 0 < i + j <= height_cutoff
    ]
    labels = tuple(f"{i},{j}" for i, j in vectors)
    vector_by_label = dict(zip(labels, vectors))
    heights = {label: sum(vector_by_label[label]) for label in labels}
    pairings = {}
    sums = {}
    for left in labels:
        i, j = vector_by_label[left]
        for right in labels:
            k, l = vector_by_label[right]
            pairings[(left, right)] = i * l - j * k
            total = (i + k, j + l)
            if sum(total) <= height_cutoff:
                sums[(left, right)] = f"{total[0]},{total[1]}"
            else:
                sums[(left, right)] = None
    return labels, heights, pairings, sums


def _finite_stokes_source_gate_kwargs(**overrides):
    data = {
        "source_differential_matrix": ((0, 0), (0, 0)),
        "target_differential_matrix": ((0, 0), (0, 0)),
        "theta_matrix": ((1, 0), (0, 1)),
        "half_convolution_bracket_matrix": ((0, 0), (0, 0)),
        "source_product_matrix": ((1,),),
        "target_product_matrix": ((1,),),
        "left_theta_matrix": ((2,),),
        "right_theta_matrix": ((3,),),
        "union_theta_matrix": ((6,),),
    }
    data.update(overrides)
    return data


def test_finite_stokes_hcs_hall_source_gate_closes_for_mc_and_product():
    gate = finite_stokes_hcs_hall_source_gate(4, **_finite_stokes_source_gate_kwargs())
    assert gate.status == "FINITE_STOKES_HCS_HALL_SOURCE_GATE"
    assert gate.closed is True
    assert gate.maurer_cartan_closed is True
    assert gate.multiplicative is True
    assert gate.maurer_cartan_defect_rank == 0
    assert gate.multiplicativity_defect_rank == 0
    assert gate.product_after_components == ((Fraction(6),),)
    assert gate.union_after_product == gate.product_after_components


def test_finite_stokes_hcs_hall_source_gate_detects_mc_defect():
    gate = finite_stokes_hcs_hall_source_gate(
        4,
        **_finite_stokes_source_gate_kwargs(
            target_differential_matrix=((1, 0), (0, 0)),
        ),
    )
    assert gate.status == "FINITE_STOKES_HCS_HALL_SOURCE_DEFECT"
    assert gate.closed is False
    assert gate.maurer_cartan_closed is False
    assert gate.multiplicative is True
    assert gate.maurer_cartan_defect_matrix == (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    assert gate.maurer_cartan_defect_rank == 1


def test_finite_stokes_hcs_hall_source_gate_detects_product_defect():
    gate = finite_stokes_hcs_hall_source_gate(
        4,
        **_finite_stokes_source_gate_kwargs(union_theta_matrix=((5,),)),
    )
    assert gate.status == "FINITE_STOKES_HCS_HALL_SOURCE_DEFECT"
    assert gate.closed is False
    assert gate.maurer_cartan_closed is True
    assert gate.multiplicative is False
    assert gate.multiplicativity_defect_matrix == ((Fraction(1),),)
    assert gate.multiplicativity_defect_rank == 1


def test_finite_stokes_hcs_hall_source_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="theta_matrix"):
        finite_stokes_hcs_hall_source_gate(
            4,
            **_finite_stokes_source_gate_kwargs(theta_matrix=((1,),)),
        )
    with pytest.raises(ValueError, match="source_product_matrix"):
        finite_stokes_hcs_hall_source_gate(
            4,
            **_finite_stokes_source_gate_kwargs(source_product_matrix=((1, 0),)),
        )


def _finite_rees_vc_gate_kwargs(**overrides):
    data = {
        "source_differential_matrix": ((0,),),
        "target_differential_matrix": ((0,),),
        "realization_matrix": ((2,),),
        "rees_thom_sebastiani_matrix": ((1,),),
        "vanishing_cycle_thom_sebastiani_matrix": ((1,),),
        "left_realization_matrix": ((2,),),
        "right_realization_matrix": ((3,),),
        "union_realization_matrix": ((6,),),
        "proper_pushforward_source_matrix": ((1,),),
        "proper_pushforward_target_matrix": ((1,),),
        "lci_pullback_source_matrix": ((1,),),
        "lci_pullback_target_matrix": ((1,),),
        "orientation_source_matrix": ((1,),),
        "orientation_target_matrix": ((1,),),
        "tate_source_matrix": ((1,),),
        "tate_target_matrix": ((1,),),
        "support_source_projection_matrix": ((1,),),
        "support_target_projection_matrix": ((1,),),
        "completion_source_projection_matrix": ((1,),),
        "completion_target_projection_matrix": ((1,),),
        "equivariance_data": (
            {
                "label": "g",
                "source_matrix": ((1,),),
                "target_matrix": ((1,),),
            },
        ),
    }
    data.update(overrides)
    return data


def test_finite_rees_vanishing_cycle_realization_gate_closes():
    gate = finite_rees_vanishing_cycle_realization_gate(
        4,
        **_finite_rees_vc_gate_kwargs(),
    )
    assert gate.status == "FINITE_REES_VANISHING_CYCLE_REALIZATION_GATE"
    assert gate.closed is True
    assert gate.chain_map is True
    assert gate.thom_sebastiani_compatible is True
    assert gate.proper_pushforward_compatible is True
    assert gate.lci_pullback_compatible is True
    assert gate.orientation_compatible is True
    assert gate.tate_compatible is True
    assert gate.support_compatible is True
    assert gate.completion_compatible is True
    assert gate.equivariant is True
    assert gate.thom_sebastiani_left_matrix == ((Fraction(6),),)
    assert gate.thom_sebastiani_right_matrix == gate.thom_sebastiani_left_matrix
    assert gate.equivariance_reports[0].label == "g"
    assert gate.equivariance_reports[0].defect_rank == 0


def test_finite_rees_vanishing_cycle_realization_gate_detects_chain_defect():
    gate = finite_rees_vanishing_cycle_realization_gate(
        4,
        **_finite_rees_vc_gate_kwargs(
            target_differential_matrix=((1,),),
        ),
    )
    assert gate.status == "FINITE_REES_VANISHING_CYCLE_REALIZATION_DEFECT"
    assert gate.closed is False
    assert gate.chain_map is False
    assert gate.chain_defect_matrix == ((Fraction(2),),)
    assert gate.chain_defect_rank == 1
    assert gate.thom_sebastiani_compatible is True


def test_finite_rees_vanishing_cycle_realization_gate_detects_ts_defect():
    gate = finite_rees_vanishing_cycle_realization_gate(
        4,
        **_finite_rees_vc_gate_kwargs(
            union_realization_matrix=((5,),),
        ),
    )
    assert gate.closed is False
    assert gate.chain_map is True
    assert gate.thom_sebastiani_compatible is False
    assert gate.thom_sebastiani_defect_matrix == ((Fraction(-1),),)
    assert gate.thom_sebastiani_defect_rank == 1


def test_finite_rees_vanishing_cycle_realization_gate_detects_structure_defects():
    gate = finite_rees_vanishing_cycle_realization_gate(
        4,
        **_finite_rees_vc_gate_kwargs(
            proper_pushforward_target_matrix=((-1,),),
            lci_pullback_target_matrix=((-1,),),
            orientation_target_matrix=((-1,),),
            tate_target_matrix=((-1,),),
            support_target_projection_matrix=((0,),),
            completion_target_projection_matrix=((0,),),
        ),
    )
    assert gate.closed is False
    assert gate.proper_pushforward_compatible is False
    assert gate.lci_pullback_compatible is False
    assert gate.orientation_compatible is False
    assert gate.tate_compatible is False
    assert gate.support_compatible is False
    assert gate.completion_compatible is False
    assert gate.proper_pushforward_defect_matrix == ((Fraction(-4),),)
    assert gate.lci_pullback_defect_matrix == ((Fraction(-4),),)
    assert gate.orientation_defect_matrix == ((Fraction(-4),),)
    assert gate.tate_defect_matrix == ((Fraction(-4),),)
    assert gate.support_defect_matrix == ((Fraction(-2),),)
    assert gate.completion_defect_matrix == ((Fraction(-2),),)
    assert gate.proper_pushforward_defect_rank == 1
    assert gate.lci_pullback_defect_rank == 1
    assert gate.orientation_defect_rank == 1
    assert gate.tate_defect_rank == 1
    assert gate.support_defect_rank == 1
    assert gate.completion_defect_rank == 1


def test_finite_rees_vanishing_cycle_realization_gate_detects_equivariance_defect():
    gate = finite_rees_vanishing_cycle_realization_gate(
        4,
        **_finite_rees_vc_gate_kwargs(
            equivariance_data=(
                {
                    "label": "bad",
                    "source_matrix": ((1,),),
                    "target_matrix": ((-1,),),
                },
            ),
        ),
    )
    assert gate.closed is False
    assert gate.equivariant is False
    assert gate.equivariance_reports[0].label == "bad"
    assert gate.equivariance_reports[0].defect_matrix == ((Fraction(-4),),)
    assert gate.equivariance_reports[0].defect_rank == 1
    assert gate.equivariance_reports[0].compatible is False


def test_finite_rees_vanishing_cycle_realization_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="realization_matrix"):
        finite_rees_vanishing_cycle_realization_gate(
            4,
            **_finite_rees_vc_gate_kwargs(realization_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="rees_thom_sebastiani_matrix"):
        finite_rees_vanishing_cycle_realization_gate(
            4,
            **_finite_rees_vc_gate_kwargs(rees_thom_sebastiani_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="proper_pushforward_source_matrix"):
        finite_rees_vanishing_cycle_realization_gate(
            4,
            **_finite_rees_vc_gate_kwargs(
                proper_pushforward_source_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="equivariance source_matrix"):
        finite_rees_vanishing_cycle_realization_gate(
            4,
            **_finite_rees_vc_gate_kwargs(
                equivariance_data=(
                    {
                        "label": "bad",
                        "source_matrix": ((1, 0),),
                        "target_matrix": ((1,),),
                    },
                ),
            ),
        )
    with pytest.raises(ValueError, match="source_matrix and target_matrix"):
        finite_rees_vanishing_cycle_realization_gate(
            4,
            **_finite_rees_vc_gate_kwargs(
                equivariance_data=({"label": "bad", "source_matrix": ((1,),)},),
            ),
        )


def _finite_beck_chevalley_gate_kwargs(**overrides):
    data = {
        "proper_pushforward_matrix": ((2,),),
        "base_lci_pullback_matrix": ((3,),),
        "source_lci_pullback_matrix": ((3,),),
        "pulled_proper_pushforward_matrix": ((2,),),
        "source_support_projection_matrix": ((1,),),
        "target_support_projection_matrix": ((1,),),
        "pulled_source_support_projection_matrix": ((1,),),
        "pulled_target_support_projection_matrix": ((1,),),
    }
    data.update(overrides)
    return data


def test_finite_compact_support_beck_chevalley_gate_closes():
    gate = finite_compact_support_beck_chevalley_gate(
        4,
        **_finite_beck_chevalley_gate_kwargs(),
    )
    assert gate.status == "FINITE_COMPACT_SUPPORT_BECK_CHEVALLEY_GATE"
    assert gate.closed is True
    assert gate.beck_chevalley_compatible is True
    assert gate.compact_support_compatible is True
    assert gate.beck_chevalley_left_matrix == ((Fraction(6),),)
    assert gate.beck_chevalley_right_matrix == gate.beck_chevalley_left_matrix
    assert gate.beck_chevalley_defect_rank == 0
    assert gate.proper_support_defect_rank == 0
    assert gate.base_lci_support_defect_rank == 0
    assert gate.source_lci_support_defect_rank == 0
    assert gate.pulled_proper_support_defect_rank == 0


def test_finite_compact_support_beck_chevalley_gate_detects_base_change_defect():
    gate = finite_compact_support_beck_chevalley_gate(
        4,
        **_finite_beck_chevalley_gate_kwargs(
            pulled_proper_pushforward_matrix=((1,),),
        ),
    )
    assert gate.status == "FINITE_COMPACT_SUPPORT_BECK_CHEVALLEY_DEFECT"
    assert gate.closed is False
    assert gate.beck_chevalley_compatible is False
    assert gate.compact_support_compatible is True
    assert gate.beck_chevalley_defect_matrix == ((Fraction(3),),)
    assert gate.beck_chevalley_defect_rank == 1


def test_finite_compact_support_beck_chevalley_gate_detects_support_defect():
    gate = finite_compact_support_beck_chevalley_gate(
        4,
        **_finite_beck_chevalley_gate_kwargs(
            target_support_projection_matrix=((0,),),
        ),
    )
    assert gate.closed is False
    assert gate.beck_chevalley_compatible is True
    assert gate.compact_support_compatible is False
    assert gate.proper_support_defect_matrix == ((Fraction(-2),),)
    assert gate.base_lci_support_defect_matrix == ((Fraction(3),),)
    assert gate.proper_support_defect_rank == 1
    assert gate.base_lci_support_defect_rank == 1


def test_finite_compact_support_beck_chevalley_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="base_lci_pullback_matrix width"):
        finite_compact_support_beck_chevalley_gate(
            4,
            **_finite_beck_chevalley_gate_kwargs(
                base_lci_pullback_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="pulled_proper_pushforward_matrix width"):
        finite_compact_support_beck_chevalley_gate(
            4,
            **_finite_beck_chevalley_gate_kwargs(
                pulled_proper_pushforward_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="source_support_projection_matrix"):
        finite_compact_support_beck_chevalley_gate(
            4,
            **_finite_beck_chevalley_gate_kwargs(
                source_support_projection_matrix=((1, 0),),
            ),
        )


def _finite_drinfeld_double_datum_gate_kwargs(**overrides):
    data = {
        "cartan_dimension": 1,
        "reduced_pairing_matrix": ((1,),),
        "triangular_normal_form_matrix": ((1,),),
        "mixed_product_matrix": ((2,),),
        "drinfeld_cross_relation_matrix": ((2,),),
        "coproduct_coassociator_defect_matrix": ((0,),),
        "associator_pentagon_defect_matrix": ((0,),),
        "center_compatibility_defect_matrix": ((0,),),
    }
    data.update(overrides)
    return data


def test_finite_drinfeld_double_datum_gate_closes():
    gate = finite_drinfeld_double_datum_gate(
        5,
        **_finite_drinfeld_double_datum_gate_kwargs(),
    )
    assert gate.status == "FINITE_DRINFELD_DOUBLE_DATUM_GATE"
    assert gate.closed is True
    assert gate.positive_dimension == 1
    assert gate.negative_dimension == 1
    assert gate.cartan_dimension == 1
    assert gate.triangular_normal_form_isomorphism is True
    assert gate.reduced_pairing_nondegenerate is True
    assert gate.cross_relation_compatible is True
    assert gate.coproduct_coassociative is True
    assert gate.associator_pentagon_compatible is True
    assert gate.center_compatible is True


def test_finite_drinfeld_double_datum_gate_detects_normal_form_defect():
    gate = finite_drinfeld_double_datum_gate(
        5,
        **_finite_drinfeld_double_datum_gate_kwargs(
            triangular_normal_form_matrix=((0,),),
        ),
    )
    assert gate.status == "FINITE_DRINFELD_DOUBLE_DATUM_DEFECT"
    assert gate.closed is False
    assert gate.triangular_normal_form_isomorphism is False
    assert gate.triangular_normal_form_rank == 0


def test_finite_drinfeld_double_datum_gate_detects_pairing_defect():
    gate = finite_drinfeld_double_datum_gate(
        5,
        **_finite_drinfeld_double_datum_gate_kwargs(
            reduced_pairing_matrix=((0,),),
        ),
    )
    assert gate.closed is False
    assert gate.reduced_pairing_nondegenerate is False
    assert gate.pairing_rank == 0
    assert gate.cross_relation_compatible is True


def test_finite_drinfeld_double_datum_gate_detects_cross_relation_defect():
    gate = finite_drinfeld_double_datum_gate(
        5,
        **_finite_drinfeld_double_datum_gate_kwargs(
            drinfeld_cross_relation_matrix=((3,),),
        ),
    )
    assert gate.closed is False
    assert gate.cross_relation_compatible is False
    assert gate.cross_relation_defect_matrix == ((Fraction(-1),),)
    assert gate.cross_relation_defect_rank == 1


def test_finite_drinfeld_double_datum_gate_detects_coherence_defects():
    gate = finite_drinfeld_double_datum_gate(
        5,
        **_finite_drinfeld_double_datum_gate_kwargs(
            coproduct_coassociator_defect_matrix=((1,),),
            associator_pentagon_defect_matrix=((2,),),
            center_compatibility_defect_matrix=((3,),),
        ),
    )
    assert gate.closed is False
    assert gate.coproduct_coassociative is False
    assert gate.associator_pentagon_compatible is False
    assert gate.center_compatible is False
    assert gate.coproduct_coassociator_defect_rank == 1
    assert gate.associator_pentagon_defect_rank == 1
    assert gate.center_compatibility_defect_rank == 1


def test_finite_drinfeld_double_datum_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="cartan_dimension"):
        finite_drinfeld_double_datum_gate(
            5,
            **_finite_drinfeld_double_datum_gate_kwargs(cartan_dimension=0),
        )
    with pytest.raises(ValueError, match="triangular_normal_form_matrix width"):
        finite_drinfeld_double_datum_gate(
            5,
            **_finite_drinfeld_double_datum_gate_kwargs(
                triangular_normal_form_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="mixed_product_matrix"):
        finite_drinfeld_double_datum_gate(
            5,
            **_finite_drinfeld_double_datum_gate_kwargs(
                mixed_product_matrix=((1, 0),),
            ),
        )


def _finite_compact_hall_product_gate_kwargs(**overrides):
    data = {
        "product_12_matrix": ((2,),),
        "product_23_matrix": ((3,),),
        "product_12_then_3_matrix": ((3,),),
        "product_1_then_23_matrix": ((2,),),
        "thom_sebastiani_left_matrix": ((5,),),
        "thom_sebastiani_right_matrix": ((5,),),
        "orientation_left_matrix": ((-1,),),
        "orientation_right_matrix": ((-1,),),
        "support_1_projection_matrix": ((1,),),
        "support_2_projection_matrix": ((1,),),
        "support_3_projection_matrix": ((1,),),
        "support_12_projection_matrix": ((1,),),
        "support_23_projection_matrix": ((1,),),
        "support_123_projection_matrix": ((1,),),
    }
    data.update(overrides)
    return data


def test_finite_compact_hall_product_gate_closes():
    gate = finite_compact_hall_product_gate(
        5,
        **_finite_compact_hall_product_gate_kwargs(),
    )
    assert gate.status == "FINITE_COMPACT_HALL_PRODUCT_GATE"
    assert gate.closed is True
    assert gate.input_dimensions == (1, 1, 1)
    assert gate.intermediate_dimensions == (1, 1)
    assert gate.target_dimension == 1
    assert gate.left_product_matrix == ((Fraction(6),),)
    assert gate.right_product_matrix == gate.left_product_matrix
    assert gate.product_associator_defect_rank == 0
    assert gate.thom_sebastiani_defect_rank == 0
    assert gate.orientation_defect_rank == 0
    assert gate.support_projection_defect_ranks == (0, 0, 0, 0, 0, 0)
    assert gate.support_intertwining_defect_ranks == (0, 0, 0, 0)


def test_finite_compact_hall_product_gate_detects_associator_defect():
    gate = finite_compact_hall_product_gate(
        5,
        **_finite_compact_hall_product_gate_kwargs(
            product_1_then_23_matrix=((1,),),
        ),
    )
    assert gate.status == "FINITE_COMPACT_HALL_PRODUCT_DEFECT"
    assert gate.closed is False
    assert gate.product_associative is False
    assert gate.product_associator_defect_matrix == ((Fraction(3),),)
    assert gate.product_associator_defect_rank == 1
    assert gate.compact_support_compatible is True


def test_finite_compact_hall_product_gate_detects_transport_defects():
    gate = finite_compact_hall_product_gate(
        5,
        **_finite_compact_hall_product_gate_kwargs(
            thom_sebastiani_right_matrix=((4,),),
            orientation_right_matrix=((1,),),
        ),
    )
    assert gate.closed is False
    assert gate.product_associative is True
    assert gate.thom_sebastiani_associative is False
    assert gate.orientation_associative is False
    assert gate.thom_sebastiani_defect_matrix == ((Fraction(1),),)
    assert gate.orientation_defect_matrix == ((Fraction(-2),),)


def test_finite_compact_hall_product_gate_detects_support_defect():
    gate = finite_compact_hall_product_gate(
        5,
        **_finite_compact_hall_product_gate_kwargs(
            support_12_projection_matrix=((0,),),
        ),
    )
    assert gate.closed is False
    assert gate.product_associative is True
    assert gate.compact_support_compatible is False
    assert gate.support_projection_defect_ranks == (0, 0, 0, 0, 0, 0)
    assert gate.support_intertwining_defect_matrices[0] == ((Fraction(-2),),)
    assert gate.support_intertwining_defect_matrices[2] == ((Fraction(3),),)
    assert gate.support_intertwining_defect_ranks == (1, 0, 1, 0)


def test_finite_compact_hall_product_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="product_12_matrix"):
        finite_compact_hall_product_gate(
            5,
            **_finite_compact_hall_product_gate_kwargs(
                product_12_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="thom_sebastiani_left_matrix"):
        finite_compact_hall_product_gate(
            5,
            **_finite_compact_hall_product_gate_kwargs(
                thom_sebastiani_left_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="support_1_projection_matrix"):
        finite_compact_hall_product_gate(
            5,
            **_finite_compact_hall_product_gate_kwargs(
                support_1_projection_matrix=((1, 0),),
            ),
        )


def _finite_realized_composite_gate_kwargs(**overrides):
    data = {
        "source_differential_matrix": ((0,),),
        "rees_differential_matrix": ((0,),),
        "realized_differential_matrix": ((0,),),
        "theta_rees_matrix": ((2,),),
        "realization_matrix": ((3,),),
        "rees_half_convolution_bracket_matrix": ((0,),),
        "realized_half_convolution_bracket_matrix": ((0,),),
        "source_product_matrix": ((1,),),
        "rees_product_matrix": ((1,),),
        "realized_product_matrix": ((1,),),
        "left_theta_rees_matrix": ((2,),),
        "right_theta_rees_matrix": ((5,),),
        "union_theta_rees_matrix": ((10,),),
        "left_realization_matrix": ((3,),),
        "right_realization_matrix": ((7,),),
        "union_realization_matrix": ((21,),),
    }
    data.update(overrides)
    return data


def test_finite_realized_hcs_hall_composite_gate_closes():
    gate = finite_realized_hcs_hall_composite_gate(
        4,
        **_finite_realized_composite_gate_kwargs(),
    )
    assert gate.status == "FINITE_REALIZED_HCS_HALL_COMPOSITE_GATE"
    assert gate.closed is True
    assert gate.realized_theta_matrix == ((Fraction(6),),)
    assert gate.chain_transport_compatible is True
    assert gate.rees_maurer_cartan_closed is True
    assert gate.bracket_transported is True
    assert gate.realized_maurer_cartan_closed is True
    assert gate.rees_multiplicative is True
    assert gate.product_transport_compatible is True
    assert gate.realized_multiplicative is True
    assert gate.realized_product_defect_matrix == ((Fraction(0),),)


def test_finite_realized_hcs_hall_composite_gate_detects_chain_transport_defect():
    gate = finite_realized_hcs_hall_composite_gate(
        4,
        **_finite_realized_composite_gate_kwargs(
            realized_differential_matrix=((1,),),
        ),
    )
    assert gate.status == "FINITE_REALIZED_HCS_HALL_COMPOSITE_DEFECT"
    assert gate.closed is False
    assert gate.chain_transport_compatible is False
    assert gate.realized_maurer_cartan_closed is False
    assert gate.chain_transport_defect_matrix == ((Fraction(3),),)
    assert gate.realized_maurer_cartan_defect_matrix == ((Fraction(6),),)
    assert gate.chain_transport_defect_rank == 1
    assert gate.realized_maurer_cartan_defect_rank == 1


def test_finite_realized_hcs_hall_composite_gate_detects_bracket_transport_defect():
    gate = finite_realized_hcs_hall_composite_gate(
        4,
        **_finite_realized_composite_gate_kwargs(
            realized_half_convolution_bracket_matrix=((1,),),
        ),
    )
    assert gate.closed is False
    assert gate.rees_maurer_cartan_closed is True
    assert gate.bracket_transported is False
    assert gate.realized_maurer_cartan_closed is False
    assert gate.bracket_transport_defect_matrix == ((Fraction(1),),)
    assert gate.realized_maurer_cartan_defect_matrix == ((Fraction(1),),)
    assert gate.bracket_transport_defect_rank == 1


def test_finite_realized_hcs_hall_composite_gate_detects_rees_product_defect():
    gate = finite_realized_hcs_hall_composite_gate(
        4,
        **_finite_realized_composite_gate_kwargs(
            union_theta_rees_matrix=((9,),),
        ),
    )
    assert gate.closed is False
    assert gate.rees_multiplicative is False
    assert gate.product_transport_compatible is True
    assert gate.realized_multiplicative is False
    assert gate.rees_product_defect_matrix == ((Fraction(1),),)
    assert gate.realized_product_defect_matrix == ((Fraction(21),),)
    assert gate.rees_product_defect_rank == 1


def test_finite_realized_hcs_hall_composite_gate_detects_product_transport_defect():
    gate = finite_realized_hcs_hall_composite_gate(
        4,
        **_finite_realized_composite_gate_kwargs(
            union_realization_matrix=((20,),),
        ),
    )
    assert gate.closed is False
    assert gate.rees_multiplicative is True
    assert gate.product_transport_compatible is False
    assert gate.realized_multiplicative is False
    assert gate.product_transport_defect_matrix == ((Fraction(1),),)
    assert gate.realized_product_defect_matrix == ((Fraction(10),),)
    assert gate.product_transport_defect_rank == 1


def test_finite_realized_hcs_hall_composite_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="theta_rees_matrix"):
        finite_realized_hcs_hall_composite_gate(
            4,
            **_finite_realized_composite_gate_kwargs(theta_rees_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="realization_matrix"):
        finite_realized_hcs_hall_composite_gate(
            4,
            **_finite_realized_composite_gate_kwargs(realization_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="source_product_matrix"):
        finite_realized_hcs_hall_composite_gate(
            4,
            **_finite_realized_composite_gate_kwargs(source_product_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="left_realization_matrix width"):
        finite_realized_hcs_hall_composite_gate(
            4,
            **_finite_realized_composite_gate_kwargs(
                left_realization_matrix=((1, 0),),
            ),
        )


def _finite_realized_cy3_bracket_gate_kwargs(**overrides):
    data = {
        "source_bracket_matrix": ((1,),),
        "rees_bracket_matrix": ((1,),),
        "realized_bracket_matrix": ((1,),),
        "left_theta_rees_matrix": ((2,),),
        "right_theta_rees_matrix": ((5,),),
        "union_theta_rees_matrix": ((10,),),
        "left_realization_matrix": ((3,),),
        "right_realization_matrix": ((7,),),
        "union_realization_matrix": ((21,),),
    }
    data.update(overrides)
    return data


def test_finite_realized_cy3_shifted_bracket_gate_closes():
    gate = finite_realized_cy3_shifted_bracket_gate(
        4,
        **_finite_realized_cy3_bracket_gate_kwargs(),
    )
    assert gate.status == "FINITE_REALIZED_CY3_SHIFTED_BRACKET_GATE"
    assert gate.closed is True
    assert gate.rees_bracket_compatible is True
    assert gate.bracket_transport_compatible is True
    assert gate.realized_bracket_compatible is True
    assert gate.rees_bracket_defect_matrix == ((Fraction(0),),)
    assert gate.bracket_transport_defect_matrix == ((Fraction(0),),)
    assert gate.realized_bracket_defect_matrix == ((Fraction(0),),)


def test_finite_realized_cy3_shifted_bracket_gate_detects_rees_defect():
    gate = finite_realized_cy3_shifted_bracket_gate(
        4,
        **_finite_realized_cy3_bracket_gate_kwargs(
            union_theta_rees_matrix=((9,),),
        ),
    )
    assert gate.status == "FINITE_REALIZED_CY3_SHIFTED_BRACKET_DEFECT"
    assert gate.closed is False
    assert gate.rees_bracket_compatible is False
    assert gate.bracket_transport_compatible is True
    assert gate.realized_bracket_compatible is False
    assert gate.rees_bracket_defect_matrix == ((Fraction(1),),)
    assert gate.realized_bracket_defect_matrix == ((Fraction(21),),)
    assert gate.rees_bracket_defect_rank == 1


def test_finite_realized_cy3_shifted_bracket_gate_detects_transport_defect():
    gate = finite_realized_cy3_shifted_bracket_gate(
        4,
        **_finite_realized_cy3_bracket_gate_kwargs(
            union_realization_matrix=((20,),),
        ),
    )
    assert gate.closed is False
    assert gate.rees_bracket_compatible is True
    assert gate.bracket_transport_compatible is False
    assert gate.realized_bracket_compatible is False
    assert gate.bracket_transport_defect_matrix == ((Fraction(1),),)
    assert gate.realized_bracket_defect_matrix == ((Fraction(10),),)
    assert gate.bracket_transport_defect_rank == 1


def test_finite_realized_cy3_shifted_bracket_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="source_bracket_matrix"):
        finite_realized_cy3_shifted_bracket_gate(
            4,
            **_finite_realized_cy3_bracket_gate_kwargs(
                source_bracket_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="realized_bracket_matrix"):
        finite_realized_cy3_shifted_bracket_gate(
            4,
            **_finite_realized_cy3_bracket_gate_kwargs(
                realized_bracket_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="left_realization_matrix width"):
        finite_realized_cy3_shifted_bracket_gate(
            4,
            **_finite_realized_cy3_bracket_gate_kwargs(
                left_realization_matrix=((1, 0),),
            ),
        )


def _finite_realized_transition_ml_kwargs(**overrides):
    data = {
        "upper_composite_matrix": ((2, 0, 0), (0, 3, 0)),
        "lower_composite_matrix": ((2, 0), (0, 3)),
        "source_transition_matrix": ((1, 0, 0), (0, 1, 0)),
        "realized_transition_matrix": ((1, 0), (0, 1)),
        "cohomology_transition_matrices": (
            {"degree": 0, "transition_matrix": ((1, 0),)},
            {"degree": 1, "transition_matrix": ((1, 0), (0, 1))},
            {"degree": 2, "transition_matrix": ()},
        ),
    }
    data.update(overrides)
    return data


def test_finite_realized_composite_transition_ml_gate_closes():
    gate = finite_realized_composite_transition_ml_gate(
        5,
        3,
        **_finite_realized_transition_ml_kwargs(),
    )
    assert gate.status == "FINITE_REALIZED_COMPOSITE_TRANSITION_ML_GATE"
    assert gate.closed is True
    assert gate.transition_commutes is True
    assert gate.cohomology_mittag_leffler is True
    assert gate.transition_defect_matrix == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    assert gate.transition_defect_rank == 0
    assert tuple(report.degree for report in gate.cohomology_reports) == (0, 1, 2)
    assert tuple(report.defect for report in gate.cohomology_reports) == (0, 0, 0)
    assert gate.cohomology_reports[2].lower_dimension == 0
    assert gate.cohomology_reports[2].surjective is True


def test_finite_realized_composite_transition_ml_gate_detects_square_defect():
    gate = finite_realized_composite_transition_ml_gate(
        5,
        3,
        **_finite_realized_transition_ml_kwargs(
            lower_composite_matrix=((2, 0), (0, 4)),
        ),
    )
    assert gate.status == "FINITE_REALIZED_COMPOSITE_TRANSITION_ML_DEFECT"
    assert gate.closed is False
    assert gate.transition_commutes is False
    assert gate.cohomology_mittag_leffler is True
    assert gate.transition_defect_matrix == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(0)),
    )
    assert gate.transition_defect_rank == 1


def test_finite_realized_composite_transition_ml_gate_detects_ml_defect():
    gate = finite_realized_composite_transition_ml_gate(
        5,
        3,
        **_finite_realized_transition_ml_kwargs(
            cohomology_transition_matrices=(
                {"degree": 0, "transition_matrix": ((1, 0),)},
                {"degree": 1, "transition_matrix": ((1, 0), (0, 0))},
            ),
        ),
    )
    assert gate.closed is False
    assert gate.transition_commutes is True
    assert gate.cohomology_mittag_leffler is False
    assert gate.cohomology_reports[1].degree == 1
    assert gate.cohomology_reports[1].lower_dimension == 2
    assert gate.cohomology_reports[1].transition_rank == 1
    assert gate.cohomology_reports[1].defect == 1
    assert gate.cohomology_reports[1].surjective is False


def test_finite_realized_composite_transition_ml_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="upper_bound"):
        finite_realized_composite_transition_ml_gate(
            3,
            5,
            **_finite_realized_transition_ml_kwargs(),
        )
    with pytest.raises(ValueError, match="source_transition_matrix"):
        finite_realized_composite_transition_ml_gate(
            5,
            3,
            **_finite_realized_transition_ml_kwargs(
                source_transition_matrix=((1, 0),),
            ),
        )
    with pytest.raises(ValueError, match="realized_transition_matrix"):
        finite_realized_composite_transition_ml_gate(
            5,
            3,
            **_finite_realized_transition_ml_kwargs(
                realized_transition_matrix=((1,),),
            ),
        )
    with pytest.raises(ValueError, match="degree and transition_matrix"):
        finite_realized_composite_transition_ml_gate(
            5,
            3,
            **_finite_realized_transition_ml_kwargs(
                cohomology_transition_matrices=({"degree": 0},),
            ),
        )
    with pytest.raises(ValueError, match="at least one cohomology transition"):
        finite_realized_composite_transition_ml_gate(
            5,
            3,
            **_finite_realized_transition_ml_kwargs(
                cohomology_transition_matrices=(),
            ),
        )


def test_finite_total_cech_ran_maurer_cartan_gate_closes():
    gate = finite_total_cech_ran_maurer_cartan_gate(
        4,
        total_differential_matrix=((0, 1), (0, 0)),
        theta_vector=(3, 0),
        half_bracket_vector=(0, 0),
    )
    assert gate.status == "FINITE_TOTAL_CECH_RAN_MAURER_CARTAN_GATE"
    assert gate.closed is True
    assert gate.differential_closed is True
    assert gate.maurer_cartan_closed is True
    assert gate.primitive_data_supplied is False
    assert gate.primitive_closes_obstruction is False
    assert gate.differential_square_defect_rank == 0
    assert gate.differential_after_theta == (Fraction(0), Fraction(0))
    assert gate.maurer_cartan_defect_vector == (Fraction(0), Fraction(0))
    assert gate.maurer_cartan_defect_rank == 0


def test_finite_total_cech_ran_maurer_cartan_gate_detects_mc_defect():
    gate = finite_total_cech_ran_maurer_cartan_gate(
        4,
        total_differential_matrix=((0, 1), (0, 0)),
        theta_vector=(0, 1),
        half_bracket_vector=(0, 0),
    )
    assert gate.status == "FINITE_TOTAL_CECH_RAN_MAURER_CARTAN_DEFECT"
    assert gate.closed is False
    assert gate.differential_after_theta == (Fraction(1), Fraction(0))
    assert gate.maurer_cartan_defect_vector == (Fraction(1), Fraction(0))
    assert gate.maurer_cartan_defect_rank == 1


def test_finite_total_cech_ran_maurer_cartan_gate_checks_primitive():
    gate = finite_total_cech_ran_maurer_cartan_gate(
        4,
        total_differential_matrix=((0, 1), (0, 0)),
        theta_vector=(0, 0),
        half_bracket_vector=(0, 0),
        obstruction_vector=(1, 0),
        primitive_vector=(0, 1),
    )
    assert gate.closed is True
    assert gate.primitive_data_supplied is True
    assert gate.primitive_closes_obstruction is True
    assert gate.obstruction_cocycle_vector == (Fraction(0), Fraction(0))
    assert gate.primitive_boundary_vector == (Fraction(1), Fraction(0))
    assert gate.primitive_defect_vector == (Fraction(0), Fraction(0))
    assert gate.obstruction_cocycle_defect_rank == 0
    assert gate.primitive_defect_rank == 0


def test_finite_total_cech_ran_maurer_cartan_gate_detects_primitive_defect():
    gate = finite_total_cech_ran_maurer_cartan_gate(
        4,
        total_differential_matrix=((0, 1), (0, 0)),
        theta_vector=(0, 0),
        half_bracket_vector=(0, 0),
        obstruction_vector=(1, 0),
        primitive_vector=(0, 0),
    )
    assert gate.closed is False
    assert gate.primitive_data_supplied is True
    assert gate.primitive_closes_obstruction is False
    assert gate.primitive_defect_vector == (Fraction(-1), Fraction(0))
    assert gate.primitive_defect_rank == 1


def test_finite_total_cech_ran_maurer_cartan_gate_detects_bad_differential():
    gate = finite_total_cech_ran_maurer_cartan_gate(
        4,
        total_differential_matrix=((1,),),
        theta_vector=(0,),
        half_bracket_vector=(0,),
    )
    assert gate.closed is False
    assert gate.differential_closed is False
    assert gate.differential_square_matrix == ((Fraction(1),),)
    assert gate.differential_square_defect_rank == 1
    assert gate.maurer_cartan_closed is True


def test_finite_total_cech_ran_maurer_cartan_gate_accepts_zero_dimensional_complex():
    gate = finite_total_cech_ran_maurer_cartan_gate(
        4,
        total_differential_matrix=(),
        theta_vector=(),
        half_bracket_vector=(),
    )
    assert gate.status == "FINITE_TOTAL_CECH_RAN_MAURER_CARTAN_GATE"
    assert gate.closed is True
    assert gate.total_dimension == 0
    assert gate.differential_square_defect_rank == 0
    assert gate.maurer_cartan_defect_rank == 0


def test_finite_total_cech_ran_maurer_cartan_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="theta_vector"):
        finite_total_cech_ran_maurer_cartan_gate(
            4,
            total_differential_matrix=((0, 1), (0, 0)),
            theta_vector=(0,),
            half_bracket_vector=(0, 0),
        )
    with pytest.raises(ValueError, match="supplied together"):
        finite_total_cech_ran_maurer_cartan_gate(
            4,
            total_differential_matrix=((0, 1), (0, 0)),
            theta_vector=(0, 0),
            half_bracket_vector=(0, 0),
            obstruction_vector=(1, 0),
        )
    with pytest.raises(ValueError, match="finite_bound"):
        finite_total_cech_ran_maurer_cartan_gate(
            0,
            total_differential_matrix=(),
            theta_vector=(),
            half_bracket_vector=(),
        )


def _finite_cyclic_sdr_block_gate_kwargs(**overrides):
    data = {
        "ambient_differential_matrix": ((0,),),
        "model_differential_matrix": ((0,),),
        "inclusion_matrix": ((1,),),
        "projection_matrix": ((1,),),
        "homotopy_matrix": ((0,),),
        "cyclic_pairing_matrix": ((1,),),
        "expected_block_homotopy_matrix": ((0,),),
        "total_action_matrix": ((1, 2),),
        "split_action_matrix": ((1, 2),),
        "action_boundary_matrix": ((0, 0),),
        "off_hessian_matrix": ((1, 0), (0, 2)),
        "odd_contraction_matrix": ((0, 1), (-1, 0)),
        "source_product_matrix": ((1,),),
        "target_product_matrix": ((1,),),
        "left_theta_matrix": ((2,),),
        "right_theta_matrix": ((3,),),
        "union_theta_matrix": ((30,),),
        "rees_euler_matrix": ((5,),),
    }
    data.update(overrides)
    return data


def test_finite_cyclic_sdr_block_compatibility_gate_closes():
    gate = finite_cyclic_sdr_block_compatibility_gate(
        4,
        **_finite_cyclic_sdr_block_gate_kwargs(),
    )
    assert gate.status == "FINITE_CYCLIC_SDR_BLOCK_COMPATIBILITY_GATE"
    assert gate.closed is True
    assert gate.sdr_closed is True
    assert gate.cyclic_closed is True
    assert gate.block_transfer_closed is True
    assert gate.hessian_cancellation_closed is True
    assert gate.multiplicative is True
    assert gate.retraction_defect_rank == 0
    assert gate.inclusion_chain_defect_rank == 0
    assert gate.projection_chain_defect_rank == 0
    assert gate.homotopy_defect_rank == 0
    assert gate.cyclicity_defect_rank == 0
    assert gate.block_homotopy_defect_rank == 0
    assert gate.transferred_action_defect_rank == 0
    assert gate.hessian_symmetry_defect_rank == 0
    assert gate.odd_contraction_skew_defect_rank == 0
    assert gate.hessian_contraction_scalar == 0
    assert gate.hessian_contraction_defect_rank == 0
    assert gate.euler_product_after_components == ((Fraction(30),),)
    assert gate.union_after_source_product == gate.euler_product_after_components
    assert gate.euler_multiplicativity_defect_rank == 0


def test_finite_cyclic_sdr_block_compatibility_gate_detects_sdr_defect():
    gate = finite_cyclic_sdr_block_compatibility_gate(
        4,
        **_finite_cyclic_sdr_block_gate_kwargs(projection_matrix=((0,),)),
    )
    assert gate.status == "FINITE_CYCLIC_SDR_BLOCK_COMPATIBILITY_DEFECT"
    assert gate.closed is False
    assert gate.sdr_closed is False
    assert gate.retraction_defect_matrix == ((Fraction(-1),),)
    assert gate.retraction_defect_rank == 1
    assert gate.homotopy_defect_rank == 1


def test_finite_cyclic_sdr_block_compatibility_gate_detects_cyclicity_defect():
    gate = finite_cyclic_sdr_block_compatibility_gate(
        4,
        **_finite_cyclic_sdr_block_gate_kwargs(
            homotopy_matrix=((1,),),
            expected_block_homotopy_matrix=((1,),),
        ),
    )
    assert gate.sdr_closed is True
    assert gate.cyclic_closed is False
    assert gate.block_transfer_closed is True
    assert gate.cyclicity_defect_matrix == ((Fraction(2),),)
    assert gate.cyclicity_defect_rank == 1


def test_finite_cyclic_sdr_block_compatibility_gate_detects_action_defect():
    gate = finite_cyclic_sdr_block_compatibility_gate(
        4,
        **_finite_cyclic_sdr_block_gate_kwargs(
            total_action_matrix=((2, 2),),
            split_action_matrix=((1, 2),),
            action_boundary_matrix=((0, 0),),
        ),
    )
    assert gate.block_transfer_closed is False
    assert gate.transferred_action_defect_matrix == ((Fraction(1), Fraction(0)),)
    assert gate.transferred_action_defect_rank == 1


def test_finite_cyclic_sdr_block_compatibility_gate_detects_hessian_defect():
    gate = finite_cyclic_sdr_block_compatibility_gate(
        4,
        **_finite_cyclic_sdr_block_gate_kwargs(
            off_hessian_matrix=((0, 1), (2, 0)),
        ),
    )
    assert gate.hessian_cancellation_closed is False
    assert gate.hessian_symmetry_defect_rank == 2
    assert gate.odd_contraction_skew_defect_rank == 0
    assert gate.hessian_contraction_scalar == Fraction(-1)
    assert gate.hessian_contraction_defect_rank == 1


def test_finite_cyclic_sdr_block_compatibility_gate_detects_euler_product_defect():
    gate = finite_cyclic_sdr_block_compatibility_gate(
        4,
        **_finite_cyclic_sdr_block_gate_kwargs(union_theta_matrix=((29,),)),
    )
    assert gate.multiplicative is False
    assert gate.euler_product_after_components == ((Fraction(30),),)
    assert gate.union_after_source_product == ((Fraction(29),),)
    assert gate.euler_multiplicativity_defect_matrix == ((Fraction(1),),)
    assert gate.euler_multiplicativity_defect_rank == 1


def test_finite_cyclic_sdr_block_compatibility_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="inclusion_matrix"):
        finite_cyclic_sdr_block_compatibility_gate(
            4,
            **_finite_cyclic_sdr_block_gate_kwargs(inclusion_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="rees_euler_matrix"):
        finite_cyclic_sdr_block_compatibility_gate(
            4,
            **_finite_cyclic_sdr_block_gate_kwargs(rees_euler_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="finite_bound"):
        finite_cyclic_sdr_block_compatibility_gate(
            0,
            **_finite_cyclic_sdr_block_gate_kwargs(),
        )


def _finite_simplicial_contraction_face(**overrides):
    data = {
        "label": "d0",
        "ambient_restriction_matrix": ((1,),),
        "model_restriction_matrix": ((1,),),
        "face_inclusion_matrix": ((1,),),
        "face_projection_matrix": ((1,),),
        "face_homotopy_matrix": ((0,),),
    }
    data.update(overrides)
    return data


def _finite_simplicial_contraction_kwargs(**overrides):
    data = {
        "ambient_differential_matrix": ((0,),),
        "model_differential_matrix": ((0,),),
        "inclusion_matrix": ((1,),),
        "projection_matrix": ((1,),),
        "homotopy_matrix": ((0,),),
        "cyclic_pairing_matrix": ((1,),),
        "face_data": (_finite_simplicial_contraction_face(),),
    }
    data.update(overrides)
    return data


def test_finite_simplicial_cyclic_contraction_gate_closes_with_face():
    gate = finite_simplicial_cyclic_contraction_gate(
        4,
        **_finite_simplicial_contraction_kwargs(),
    )
    assert gate.status == "FINITE_SIMPLICIAL_CYCLIC_CONTRACTION_GATE"
    assert gate.closed is True
    assert gate.sdr_closed is True
    assert gate.side_conditions_closed is True
    assert gate.cyclic_closed is True
    assert gate.faces_compatible is True
    assert gate.retraction_defect_rank == 0
    assert gate.inclusion_chain_defect_rank == 0
    assert gate.projection_chain_defect_rank == 0
    assert gate.homotopy_defect_rank == 0
    assert gate.homotopy_square_rank == 0
    assert gate.homotopy_inclusion_rank == 0
    assert gate.projection_homotopy_rank == 0
    assert gate.cyclicity_defect_rank == 0
    assert len(gate.face_reports) == 1
    assert gate.face_reports[0].compatible is True
    assert gate.face_reports[0].inclusion_face_defect_rank == 0
    assert gate.face_reports[0].projection_face_defect_rank == 0
    assert gate.face_reports[0].homotopy_face_defect_rank == 0


def test_finite_simplicial_cyclic_contraction_gate_accepts_zero_simplex():
    gate = finite_simplicial_cyclic_contraction_gate(
        4,
        **_finite_simplicial_contraction_kwargs(face_data=()),
    )
    assert gate.status == "FINITE_SIMPLICIAL_CYCLIC_CONTRACTION_GATE"
    assert gate.face_reports == ()
    assert gate.faces_compatible is True
    assert gate.closed is True


def test_finite_simplicial_cyclic_contraction_gate_detects_sdr_defect():
    gate = finite_simplicial_cyclic_contraction_gate(
        4,
        **_finite_simplicial_contraction_kwargs(projection_matrix=((0,),)),
    )
    assert gate.status == "FINITE_SIMPLICIAL_CYCLIC_CONTRACTION_DEFECT"
    assert gate.closed is False
    assert gate.sdr_closed is False
    assert gate.retraction_defect_matrix == ((Fraction(-1),),)
    assert gate.retraction_defect_rank == 1
    assert gate.homotopy_defect_rank == 1


def test_finite_simplicial_cyclic_contraction_gate_detects_side_and_cyclic_defect():
    gate = finite_simplicial_cyclic_contraction_gate(
        4,
        **_finite_simplicial_contraction_kwargs(
            homotopy_matrix=((1,),),
            face_data=(),
        ),
    )
    assert gate.sdr_closed is True
    assert gate.side_conditions_closed is False
    assert gate.cyclic_closed is False
    assert gate.homotopy_square_matrix == ((Fraction(1),),)
    assert gate.homotopy_inclusion_matrix == ((Fraction(1),),)
    assert gate.projection_homotopy_matrix == ((Fraction(1),),)
    assert gate.cyclicity_defect_matrix == ((Fraction(2),),)


def test_finite_simplicial_cyclic_contraction_gate_detects_face_defect():
    gate = finite_simplicial_cyclic_contraction_gate(
        4,
        **_finite_simplicial_contraction_kwargs(
            face_data=(
                _finite_simplicial_contraction_face(
                    face_inclusion_matrix=((0,),),
                ),
            )
        ),
    )
    assert gate.closed is False
    assert gate.faces_compatible is False
    assert gate.face_reports[0].compatible is False
    assert gate.face_reports[0].inclusion_face_defect_matrix == ((Fraction(1),),)
    assert gate.face_reports[0].inclusion_face_defect_rank == 1
    assert gate.face_reports[0].projection_face_defect_rank == 0
    assert gate.face_reports[0].homotopy_face_defect_rank == 0


def test_finite_simplicial_cyclic_contraction_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="homotopy_matrix"):
        finite_simplicial_cyclic_contraction_gate(
            4,
            **_finite_simplicial_contraction_kwargs(homotopy_matrix=((1, 0),)),
        )
    with pytest.raises(ValueError, match="d0 ambient_restriction_matrix"):
        finite_simplicial_cyclic_contraction_gate(
            4,
            **_finite_simplicial_contraction_kwargs(
                face_data=(
                    _finite_simplicial_contraction_face(
                        ambient_restriction_matrix=((1, 0),),
                    ),
                )
            ),
        )
    with pytest.raises(ValueError, match="finite_bound"):
        finite_simplicial_cyclic_contraction_gate(
            0,
            **_finite_simplicial_contraction_kwargs(),
        )


def test_finite_scattering_quantum_torus_gate_closes_for_bilinear_truncation():
    labels, heights, pairings, sums = _rank_two_torus_fixture(3)
    gate = finite_scattering_quantum_torus_gate(labels, heights, pairings, sums, 3)
    assert gate.status == "FINITE_SCATTERING_QUANTUM_TORUS_GATE"
    assert gate.closed is True
    assert gate.skew_defects == ()
    assert gate.truncation_defects == ()
    assert gate.associativity_defects == ()
    assert gate.cocycle_defects == ()
    retained_rows = [row for row in gate.product_rows if row.retained]
    assert any(
        row.left_charge == "1,0"
        and row.right_charge == "0,1"
        and row.supplied_sum == "1,1"
        and row.exponent == Fraction(1)
        for row in retained_rows
    )


def test_finite_scattering_quantum_torus_gate_detects_pairing_defect():
    labels, heights, pairings, sums = _rank_two_torus_fixture(3)
    pairings = dict(pairings)
    pairings[("1,0", "0,1")] = 2
    gate = finite_scattering_quantum_torus_gate(labels, heights, pairings, sums, 3)
    assert gate.status == "FINITE_SCATTERING_QUANTUM_TORUS_DEFECT"
    assert gate.closed is False
    assert gate.skew_defects == ("0,1,1,0:-1+2",)
    assert gate.cocycle_defects


def test_finite_scattering_quantum_torus_gate_detects_truncation_defect():
    labels, heights, pairings, sums = _rank_two_torus_fixture(3)
    sums = dict(sums)
    sums[("1,0", "0,1")] = None
    gate = finite_scattering_quantum_torus_gate(labels, heights, pairings, sums, 3)
    assert gate.status == "FINITE_SCATTERING_QUANTUM_TORUS_DEFECT"
    assert "1,0,0,1:killed inside H" in gate.truncation_defects
    assert gate.associativity_defects


def test_finite_scattering_root_report_closes_on_recognized_exponents():
    report = finite_scattering_root_report(
        charge_discriminants={
            "alpha": -1,
            "delta": 4,
            "gamma": 3,
            "lambda": 0,
        },
        bps_indices={
            "alpha": 1,
            "delta": 108,
            "gamma": -64,
            "lambda": 10,
        },
        charge_heights={
            "alpha": 1,
            "lambda": 1,
            "gamma": 2,
            "delta": 3,
        },
        height_cutoff=3,
        lower_height_cutoff=2,
    )
    assert report.status == "FINITE_SCATTERING_ROOT_COMPARISON"
    assert report.closed
    assert report.transition_commutes
    assert report.scattering_support == report.borcherds_support
    assert report.exponent_defects == ()
    assert tuple(row.discriminant for row in report.rows) == (-1, 0, 3, 4)


def test_finite_scattering_root_report_names_exponent_and_support_defects():
    report = finite_scattering_root_report(
        charge_discriminants={
            "alpha": -1,
            "extra": 1,
            "gamma": 3,
        },
        bps_indices={
            "alpha": 1,
            "extra": 7,
            "gamma": -63,
        },
        charge_heights={
            "alpha": 1,
            "extra": 1,
            "gamma": 2,
        },
        height_cutoff=2,
    )
    assert report.status == "FINITE_SCATTERING_ROOT_DEFECT"
    assert not report.closed
    assert "extra" in report.extra_support
    assert "extra" in report.exponent_defects
    assert "gamma" in report.exponent_defects


def test_bar_witness_rank_one_constant_24():
    witness = bar_witness(5)
    assert witness.rank1_values_constant_24 is True
    assert witness.rank1_values == [24, 24, 24, 24, 24]


def test_finite_bar_lattice_grading_report_matches_discriminants():
    report = finite_bar_lattice_grading_report(
        charge_coordinates={
            "alpha": (1, 0, 0),
            "lambda": (1, 1, 0),
            "gamma": (1, 1, 1),
        },
        expected_discriminants={
            "alpha": -1,
            "lambda": 0,
            "gamma": 3,
        },
        charge_heights={
            "alpha": 1,
            "lambda": 1,
            "gamma": 2,
        },
        height_cutoff=2,
        lower_height_cutoff=1,
    )
    assert report.status == "FINITE_BAR_LATTICE_GRADING_MATCH"
    assert report.closed
    assert report.transition_commutes
    assert report.integrality_defects == ()
    assert report.discriminant_defects == ()
    assert tuple(row.computed_discriminant for row in report.rows) == (-1, 0, 3)
    assert tuple(row.norm for row in report.rows) == (2, 0, -6)


def test_finite_bar_lattice_grading_report_detects_defects():
    report = finite_bar_lattice_grading_report(
        charge_coordinates={
            "bad_discriminant": (1, 1, 1),
            "nonintegral": (Fraction(1, 2), 0, 0),
        },
        expected_discriminants={
            "bad_discriminant": 4,
            "nonintegral": Fraction(-1, 4),
        },
        charge_heights={
            "bad_discriminant": 1,
            "nonintegral": 1,
        },
        height_cutoff=1,
    )
    assert report.status == "FINITE_BAR_LATTICE_GRADING_DEFECT"
    assert not report.closed
    assert report.discriminant_defects == ("bad_discriminant",)
    assert report.integrality_defects == ("nonintegral",)


def test_finite_bar_ce_chain_map_gate_closes_for_commuting_square():
    gate = finite_bar_ce_chain_map_gate(
        3,
        source_differential_matrix=((1, 0), (0, 1)),
        target_differential_matrix=((2, 0), (0, 3)),
        comparison_degree1_matrix=((2, 0), (0, 3)),
        comparison_degree2_matrix=((1, 0), (0, 1)),
    )
    assert gate.status == "FINITE_BAR_CE_CHAIN_MAP_GATE"
    assert gate.chain_map is True
    assert gate.chain_commutator_defect_rank == 0
    assert gate.comparison_after_bar_differential == (
        (Fraction(2), Fraction(0)),
        (Fraction(0), Fraction(3)),
    )
    assert gate.ce_differential_after_comparison == gate.comparison_after_bar_differential
    assert gate.source_differential_shape == (2, 2)
    assert gate.target_differential_shape == (2, 2)


def test_finite_bar_ce_chain_map_gate_detects_differential_square_defect():
    gate = finite_bar_ce_chain_map_gate(
        3,
        source_differential_matrix=((1, 0), (0, 1)),
        target_differential_matrix=((2, 0), (0, 4)),
        comparison_degree1_matrix=((2, 0), (0, 3)),
        comparison_degree2_matrix=((1, 0), (0, 1)),
    )
    assert gate.status == "FINITE_BAR_CE_CHAIN_MAP_DEFECT"
    assert gate.chain_map is False
    assert gate.chain_commutator_matrix == (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    assert gate.chain_commutator_defect_rank == 1


def test_finite_bar_ce_chain_map_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="comparison_degree1_matrix"):
        finite_bar_ce_chain_map_gate(
            3,
            source_differential_matrix=((1, 0), (0, 1)),
            target_differential_matrix=((1, 0), (0, 1)),
            comparison_degree1_matrix=((1,),),
            comparison_degree2_matrix=((1, 0), (0, 1)),
        )
    with pytest.raises(ValueError, match="common width"):
        finite_bar_ce_chain_map_gate(
            3,
            source_differential_matrix=((1, 0), (0,)),
            target_differential_matrix=((1,),),
            comparison_degree1_matrix=((1,),),
            comparison_degree2_matrix=((1, 0),),
        )


def test_finite_bar_ce_report_closes_with_exponents_and_differential():
    report = finite_bar_ce_report(
        charge_discriminants={
            "alpha": -1,
            "delta": 4,
            "gamma": 3,
            "lambda": 0,
        },
        bar_euler_exponents={
            "alpha": 1,
            "delta": 108,
            "gamma": -64,
            "lambda": 10,
        },
        differential_commutes_by_charge={
            "alpha": True,
            "delta": True,
            "gamma": True,
            "lambda": True,
        },
        charge_heights={
            "alpha": 1,
            "lambda": 1,
            "gamma": 2,
            "delta": 3,
        },
        height_cutoff=3,
        lower_height_cutoff=2,
    )
    assert report.status == "FINITE_BAR_CE_COMPARISON"
    assert report.closed
    assert report.transition_commutes
    assert report.exponent_defects == ()
    assert report.differential_defects == ()
    assert tuple(row.discriminant for row in report.rows) == (-1, 0, 3, 4)


def test_finite_bar_ce_report_separates_exponent_from_differential_defect():
    report = finite_bar_ce_report(
        charge_discriminants={
            "alpha": -1,
            "gamma": 3,
        },
        bar_euler_exponents={
            "alpha": 1,
            "gamma": -63,
        },
        differential_commutes_by_charge={
            "alpha": True,
            "gamma": False,
        },
        charge_heights={
            "alpha": 1,
            "gamma": 2,
        },
        height_cutoff=2,
    )
    assert report.status == "FINITE_BAR_CE_DEFECT"
    assert not report.closed
    assert report.exponent_defects == ("gamma",)
    assert report.differential_defects == ("gamma",)


def test_finite_bar_regularization_report_solves_weyl_vector_exactly():
    report = finite_bar_regularization_report()
    assert report.status == "FINITE_BAR_REGULARIZATION_MATCH"
    assert report.closed
    assert report.borcherds_weyl_vector == (
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(1, 2),
    )
    assert report.weyl_equation_rhs == (-1, -1, -1)
    assert report.supplied_pairings == (-1, -1, -1)
    assert report.pairing_defect == (0, 0, 0)
    assert report.vector_difference == (0, 0, 0)
    assert report.supplied_normalization == Fraction(1, 64)
    assert report.normalization_matches


def test_finite_bar_regularization_report_detects_vector_and_normalization_defects():
    vector_defect = finite_bar_regularization_report(
        bar_regularization_vector=(1, 0, 0),
    )
    assert vector_defect.status == "FINITE_BAR_REGULARIZATION_DEFECT"
    assert not vector_defect.closed
    assert vector_defect.pairing_defect != (0, 0, 0)
    assert vector_defect.vector_difference != (0, 0, 0)
    assert not vector_defect.weyl_vector_matches

    normalization_defect = finite_bar_regularization_report(
        supplied_normalization=1,
    )
    assert normalization_defect.status == "FINITE_BAR_REGULARIZATION_DEFECT"
    assert normalization_defect.weyl_vector_matches
    assert not normalization_defect.normalization_matches
    assert not normalization_defect.closed


def test_rademacher_witness_growth():
    witness = rademacher_witness(10)
    assert witness.growth_ok is True
    assert witness.leading_term_D3 > 0
    assert witness.leading_term_D4 > witness.leading_term_D3
    assert witness.finite_height_certificate.status == "FINITE_RANK_ONE_RADEMACHER_CERTIFICATE"
    assert witness.finite_height_certificate.max_residual_rel < 0.03
    assert witness.finite_height_certificate.transition_commutes is True


def test_rademacher_finite_height_certificate():
    certificate = rademacher_finite_height_certificate()
    assert certificate.discriminants == (3, 4, 7, 8, 11, 12, 15, 16, 19, 20)
    assert certificate.max_conductor == 5
    assert certificate.status == "FINITE_RANK_ONE_RADEMACHER_CERTIFICATE"
    assert certificate.max_residual_rel < certificate.tolerance
    assert certificate.max_leading_residual_rel > certificate.max_residual_rel
    assert certificate.residual_improves_over_leading is True
    assert certificate.conductor_projection_defects == ()
    assert certificate.rows[0].conductor_to_arity == (
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
    )
    assert certificate.rows[0].exact_abs_coefficient == 64
    assert certificate.rows[-1].discriminant == 20


def test_rademacher_polar_bessel_gate_closes_canonical_rows():
    report = rademacher_polar_bessel_gate(
        discriminants=(3, 4),
        max_conductor=2,
        lower_max_conductor=1,
    )
    assert report.status == "FINITE_RADEMACHER_POLAR_BESSEL_GATE"
    assert report.closed
    assert report.transition_commutes
    assert report.missing_rows == ()
    assert report.polar_defects == ()
    assert report.multiplier_defects == ()
    assert report.bessel_order_defects == ()
    assert report.arity_defects == ()
    assert report.coefficient_defects == ()
    assert tuple((row.discriminant, row.conductor) for row in report.rows) == (
        (3, 1),
        (3, 2),
        (4, 1),
        (4, 2),
    )
    assert report.rows[0].supplied_polar_discriminant == -1
    assert report.rows[0].supplied_polar_coefficient == 1
    assert report.rows[0].supplied_multiplier == "eta^3"
    assert report.rows[0].supplied_bessel_order == Fraction(3, 2)
    assert report.rows[0].supplied_arity == 2
    assert report.rows[0].supplied_signed_coefficient == -64
    assert report.rows[0].expected_absolute_coefficient == 64
    assert report.rows[0].bessel_argument > 0
    assert report.rows[0].bessel_value > 0


def test_rademacher_polar_bessel_gate_names_defects():
    report = rademacher_polar_bessel_gate(
        supplied_rows={
            (3, 1): {
                "polar_discriminant": 0,
                "polar_coefficient": 2,
                "multiplier": "trivial",
                "bessel_order": 1,
                "arity": 99,
                "signed_coefficient": -63,
            },
        },
        discriminants=(3,),
        max_conductor=2,
    )
    assert report.status == "FINITE_RADEMACHER_POLAR_BESSEL_DEFECT"
    assert not report.closed
    assert report.missing_rows == ("D=3:c=2",)
    assert report.polar_defects == ("D=3:c=1",)
    assert report.multiplier_defects == ("D=3:c=1",)
    assert report.bessel_order_defects == ("D=3:c=1",)
    assert report.arity_defects == ("D=3:c=1",)
    assert report.coefficient_defects == ("D=3:c=1",)


def test_rademacher_truncation_error_gate_closes_tight_bounds():
    report = rademacher_truncation_error_gate(
        discriminants=(3, 4),
        max_conductor=5,
        lower_max_conductor=3,
    )
    assert report.status == "FINITE_RADEMACHER_TRUNCATION_ERROR_GATE"
    assert report.closed
    assert report.transition_commutes
    assert report.terminal_tolerance_met
    assert report.max_terminal_residual_rel < report.tolerance
    assert report.missing_abs_bounds == ()
    assert report.missing_rel_bounds == ()
    assert report.abs_bound_defects == ()
    assert report.rel_bound_defects == ()
    assert len(report.rows) == 10
    assert report.rows[0].discriminant == 3
    assert report.rows[0].conductor == 1
    assert report.rows[0].arity == 2
    assert report.rows[0].exact_absolute_coefficient == 64
    assert report.rows[0].supplied_abs_bound == report.rows[0].residual_abs
    assert report.rows[0].supplied_rel_bound == report.rows[0].residual_rel


def test_rademacher_truncation_error_gate_names_bound_defects():
    report = rademacher_truncation_error_gate(
        discriminants=(3,),
        max_conductor=2,
        abs_bounds={(3, 1): 0.0},
        rel_bounds={(3, 1): 0.0},
        tolerance=1.0,
    )
    assert report.status == "FINITE_RADEMACHER_TRUNCATION_ERROR_DEFECT"
    assert not report.closed
    assert report.missing_abs_bounds == ("D=3:c=2",)
    assert report.missing_rel_bounds == ("D=3:c=2",)
    assert report.abs_bound_defects == ("D=3:c=1", "D=3:c=2")
    assert report.rel_bound_defects == ("D=3:c=1", "D=3:c=2")


def test_brst_witness_central_charge_balance():
    witness = brst_witness()
    assert witness.central_charge_balanced is True
    assert witness.total_central_charge == 0
    assert "BRST" in witness.target_template
    assert witness.coefficient_fixture.status == "FINITE_BRST_COEFFICIENT_FIXTURE"
    assert witness.coefficient_fixture.all_supertraces_match is True


def test_brst_central_charge_gate_closes_exactly():
    gate = brst_central_charge_gate()
    assert gate.status == "FINITE_BRST_CENTRAL_CHARGE_GATE"
    assert gate.closed
    assert gate.lattice_central_charge == 3
    assert gate.ghost_central_charge == -26
    assert gate.required_transverse_central_charge == 23
    assert gate.transverse_central_charge == 23
    assert gate.total_central_charge == 0
    assert gate.total_defect == 0
    assert gate.transverse_defect == 0
    assert gate.anomaly_cancelled
    assert gate.transverse_matches_requirement


def test_brst_central_charge_gate_detects_transverse_defect():
    gate = brst_central_charge_gate(transverse_central_charge=24)
    assert gate.status == "FINITE_BRST_CENTRAL_CHARGE_DEFECT"
    assert not gate.closed
    assert gate.required_transverse_central_charge == 23
    assert gate.transverse_defect == 1
    assert gate.total_defect == 1
    assert not gate.anomaly_cancelled
    assert not gate.transverse_matches_requirement


def test_brst_coefficient_fixture_minimal_supertrace_rows():
    fixture = brst_coefficient_fixture(8)
    rows = {row.discriminant: row for row in fixture.rows}
    assert fixture.support == (-1, 0, 3, 4, 7, 8)
    assert rows[-1].bosonic_dimension == 1
    assert rows[-1].fermionic_dimension == 0
    assert rows[0].superdimension == 10
    assert rows[3].bosonic_dimension == 0
    assert rows[3].fermionic_dimension == 64
    assert rows[3].superdimension == -64
    assert rows[4].ordinary_dimension == 108
    assert rows[7].parity == "fermionic"
    assert rows[8].parity == "bosonic"
    assert fixture.total_bosonic_dimension == 1 + 10 + 108 + 808
    assert fixture.total_fermionic_dimension == 64 + 513
    assert fixture.total_superdimension == sum(row.signed_coefficient for row in fixture.rows)


def test_brst_coefficient_fixture_transition_commutes():
    transition = brst_coefficient_fixture_transition(8, 4)
    assert transition.status == "FINITE_BRST_FIXTURE_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.defects == ()
    assert transition.retained_support == (-1, 0, 3, 4)


def test_brst_coefficient_fixture_transition_rejects_reversed_bounds():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        brst_coefficient_fixture_transition(4, 8)


def test_brst_no_ghost_spectral_sequence_gate_closes_for_supplied_collapse():
    target = {-1: 1, 0: 10, 3: -64}
    gate = brst_no_ghost_spectral_sequence_gate(
        target_coefficients=target,
        transverse_supertraces=target,
        longitudinal_supertraces={-1: 2, 0: 4, 3: 6},
        ghost_supertraces={-1: -2, 0: -4, 3: -6},
        higher_differential_matrices=(
            ((0, 0), (0, 0)),
            ((0,),),
        ),
    )
    assert gate.status == "FINITE_BRST_NO_GHOST_SPECTRAL_SEQUENCE_GATE"
    assert gate.closed is True
    assert gate.no_ghost_cancellation is True
    assert gate.transverse_coefficients_match is True
    assert gate.spectral_sequence_collapses is True
    assert gate.higher_differential_ranks == (0, 0)
    assert tuple(row.discriminant for row in gate.rows) == (-1, 0, 3)


def test_brst_no_ghost_spectral_sequence_gate_detects_cancellation_defect():
    gate = brst_no_ghost_spectral_sequence_gate(
        target_coefficients={3: -64},
        transverse_supertraces={3: -64},
        longitudinal_supertraces={3: 6},
        ghost_supertraces={3: -5},
    )
    assert gate.status == "FINITE_BRST_NO_GHOST_SPECTRAL_SEQUENCE_DEFECT"
    assert gate.closed is False
    assert gate.no_ghost_cancellation is False
    assert gate.transverse_coefficients_match is True
    assert gate.cancellation_defects == ("D=3:1",)


def test_brst_no_ghost_spectral_sequence_gate_detects_coefficient_defect():
    gate = brst_no_ghost_spectral_sequence_gate(
        target_coefficients={3: -64},
        transverse_supertraces={3: -63},
        longitudinal_supertraces={3: 6},
        ghost_supertraces={3: -6},
    )
    assert gate.status == "FINITE_BRST_NO_GHOST_SPECTRAL_SEQUENCE_DEFECT"
    assert gate.closed is False
    assert gate.no_ghost_cancellation is True
    assert gate.transverse_coefficients_match is False
    assert gate.coefficient_defects == ("D=3:1",)


def test_brst_no_ghost_spectral_sequence_gate_detects_higher_page_leakage():
    gate = brst_no_ghost_spectral_sequence_gate(
        target_coefficients={3: -64},
        transverse_supertraces={3: -64},
        longitudinal_supertraces={3: 6},
        ghost_supertraces={3: -6},
        higher_differential_matrices=(((1, 0), (0, 0)),),
    )
    assert gate.status == "FINITE_BRST_NO_GHOST_SPECTRAL_SEQUENCE_DEFECT"
    assert gate.closed is False
    assert gate.spectral_sequence_collapses is False
    assert gate.higher_differential_ranks == (1,)
    assert gate.higher_differential_defects == ("d_2:rank=1",)


def test_brst_borcherds_bracket_gate_closes_for_supplied_bracket():
    coefficients = {("a", "b", "c"): 1, ("b", "a", "c"): -1}
    gate = brst_borcherds_bracket_gate(
        ("a", "b", "c"),
        {"a": 0, "b": 0, "c": 0},
        coefficients,
        coefficients,
        root_sum_labels={("a", "b"): "c", ("b", "a"): "c"},
        finite_bound=3,
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_BRACKET_GATE"
    assert gate.closed is True
    assert gate.coefficient_match is True
    assert gate.support_respected is True
    assert gate.super_skew is True
    assert gate.super_jacobi is True
    assert gate.finite_bound == 3
    assert gate.root_labels == ("a", "b", "c")
    assert len(gate.rows) == 2


def test_brst_borcherds_bracket_gate_detects_coefficient_defect():
    brst = {("a", "b", "c"): 1, ("b", "a", "c"): -1}
    target = {("a", "b", "c"): 2, ("b", "a", "c"): -2}
    gate = brst_borcherds_bracket_gate(
        ("a", "b", "c"),
        {"a": 0, "b": 0, "c": 0},
        brst,
        target,
        root_sum_labels={("a", "b"): "c", ("b", "a"): "c"},
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_BRACKET_DEFECT"
    assert gate.closed is False
    assert gate.coefficient_match is False
    assert "a,b->c:1!=2" in gate.coefficient_defects
    assert gate.support_respected is True
    assert gate.super_skew is True
    assert gate.super_jacobi is True


def test_brst_borcherds_bracket_gate_detects_support_defect():
    coefficients = {("a", "a", "c"): 1}
    gate = brst_borcherds_bracket_gate(
        ("a", "c"),
        {"a": 1, "c": 0},
        coefficients,
        coefficients,
        root_sum_labels={("a", "a"): None},
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_BRACKET_DEFECT"
    assert gate.closed is False
    assert gate.coefficient_match is True
    assert gate.support_respected is False
    assert gate.support_defects == ("a,a->c:killed",)
    assert gate.super_skew is True
    assert gate.super_jacobi is True


def test_brst_borcherds_bracket_gate_detects_super_skew_defect():
    coefficients = {("a", "b", "c"): 1, ("b", "a", "c"): 1}
    gate = brst_borcherds_bracket_gate(
        ("a", "b", "c"),
        {"a": 0, "b": 0, "c": 0},
        coefficients,
        coefficients,
        root_sum_labels={("a", "b"): "c", ("b", "a"): "c"},
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_BRACKET_DEFECT"
    assert gate.closed is False
    assert gate.super_skew is False
    assert gate.super_skew_defects == ("a,b->c:2",)
    assert gate.coefficient_match is True
    assert gate.support_respected is True


def test_brst_borcherds_bracket_gate_detects_super_jacobi_defect():
    coefficients = {
        ("x", "y", "x"): 1,
        ("y", "x", "x"): -1,
        ("y", "z", "y"): 1,
        ("z", "y", "y"): -1,
        ("z", "x", "z"): 1,
        ("x", "z", "z"): -1,
    }
    gate = brst_borcherds_bracket_gate(
        ("x", "y", "z"),
        {"x": 0, "y": 0, "z": 0},
        coefficients,
        coefficients,
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_BRACKET_DEFECT"
    assert gate.closed is False
    assert gate.coefficient_match is True
    assert gate.support_respected is True
    assert gate.super_skew is True
    assert gate.super_jacobi is False
    assert "x,y,z->x:1" in gate.super_jacobi_defects


def test_brst_borcherds_bracket_gate_rejects_unknown_labels():
    import pytest

    with pytest.raises(ValueError, match="unknown label"):
        brst_borcherds_bracket_gate(
            ("a", "b", "c"),
            {"a": 0, "b": 0, "c": 0},
            {("a", "b", "d"): 1},
            {},
        )


def test_brst_borcherds_serre_relation_gate_closes_for_supplied_relations():
    coefficients = {("e", "f", "g"): 1, ("f", "e", "g"): -1}
    gate = brst_borcherds_serre_relation_gate(
        ("e", "f", "g", "u"),
        coefficients,
        real_serre_exponents={("e", "f"): 2},
        imaginary_supercommuting_pairs=(("g", "u"),),
        finite_bound=4,
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_SERRE_RELATION_GATE"
    assert gate.closed is True
    assert gate.real_serre_relations is True
    assert gate.imaginary_supercommutativity is True
    assert gate.finite_bound == 4
    assert gate.real_serre_rows[0].output_coefficients == ()
    assert gate.imaginary_supercommutativity_rows[0].output_coefficients == ()


def test_brst_borcherds_serre_relation_gate_detects_real_serre_defect():
    coefficients = {
        ("e", "f", "g"): 1,
        ("e", "g", "f"): 1,
    }
    gate = brst_borcherds_serre_relation_gate(
        ("e", "f", "g"),
        coefficients,
        real_serre_exponents={("e", "f"): 2},
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_SERRE_RELATION_DEFECT"
    assert gate.closed is False
    assert gate.real_serre_relations is False
    assert gate.real_serre_defects == ("e,f:ad^2=f:1",)
    assert gate.real_serre_rows[0].output_coefficients == (("f", Fraction(1)),)


def test_brst_borcherds_serre_relation_gate_detects_imaginary_supercommutativity_defect():
    coefficients = {("u", "v", "w"): 3}
    gate = brst_borcherds_serre_relation_gate(
        ("u", "v", "w"),
        coefficients,
        imaginary_supercommuting_pairs=(("u", "v"),),
    )
    assert gate.status == "FINITE_BRST_BORCHERDS_SERRE_RELATION_DEFECT"
    assert gate.closed is False
    assert gate.real_serre_relations is True
    assert gate.imaginary_supercommutativity is False
    assert gate.imaginary_supercommutativity_defects == ("u,v:bracket=w:3",)
    assert gate.imaginary_supercommutativity_rows[0].output_coefficients == (
        ("w", Fraction(3)),
    )


def test_brst_borcherds_serre_relation_gate_rejects_bad_relation_input():
    import pytest

    with pytest.raises(ValueError, match="positive"):
        brst_borcherds_serre_relation_gate(
            ("e", "f"),
            {},
            real_serre_exponents={("e", "f"): 0},
        )
    with pytest.raises(ValueError, match="unknown label"):
        brst_borcherds_serre_relation_gate(
            ("e", "f"),
            {},
            imaginary_supercommuting_pairs=(("e", "x"),),
        )


def test_brst_momentum_height_projection_gate_closes_for_block_diagonal_complex():
    gate = brst_momentum_height_projection_gate(
        degree_heights={0: (0, 2), 1: (0, 2), 2: (0, 2)},
        degree_momenta={0: ("a", "b"), 1: ("a", "b"), 2: ("a", "b")},
        differentials={
            0: ((1, 0), (0, 0)),
            1: ((0, 0), (0, 0)),
        },
        upper_height=2,
        lower_height=0,
    )
    assert gate.status == "FINITE_BRST_MOMENTUM_HEIGHT_PROJECTION_GATE"
    assert gate.closed is True
    assert gate.momentum_preserved is True
    assert gate.retained_is_subcomplex is True
    assert gate.killed_is_subcomplex is True
    assert gate.upper_is_complex is True
    assert gate.lower_is_complex is True
    assert gate.upper_square_ranks == (("Q^1Q^0", 0),)
    assert gate.lower_square_ranks == (("Q^1Q^0", 0),)
    assert gate.rows[0].lower_differential_shape == (1, 1)


def test_brst_momentum_height_projection_gate_detects_momentum_defect():
    gate = brst_momentum_height_projection_gate(
        degree_heights={0: (0, 2), 1: (0, 2)},
        degree_momenta={0: ("a", "b"), 1: ("a", "b")},
        differentials={0: ((0, 1), (0, 0))},
        upper_height=2,
        lower_height=0,
    )
    assert gate.status == "FINITE_BRST_MOMENTUM_HEIGHT_PROJECTION_DEFECT"
    assert gate.closed is False
    assert gate.momentum_preserved is False
    assert gate.momentum_defects == ("Q^0:0,1:1",)
    assert gate.quotient_defects == ("Q^0:rank=1",)


def test_brst_momentum_height_projection_gate_detects_retained_to_killed_defect():
    gate = brst_momentum_height_projection_gate(
        degree_heights={0: (0, 2), 1: (0, 2)},
        degree_momenta={0: ("a", "b"), 1: ("a", "b")},
        differentials={0: ((0, 0), (1, 0))},
        upper_height=2,
        lower_height=0,
    )
    assert gate.closed is False
    assert gate.retained_is_subcomplex is False
    assert gate.subcomplex_defects == ("Q^0:rank=1",)


def test_brst_momentum_height_projection_gate_detects_killed_to_retained_defect():
    gate = brst_momentum_height_projection_gate(
        degree_heights={0: (0, 2), 1: (0, 2)},
        degree_momenta={0: ("a", "b"), 1: ("a", "b")},
        differentials={0: ((0, 1), (0, 0))},
        upper_height=2,
        lower_height=0,
    )
    assert gate.closed is False
    assert gate.killed_is_subcomplex is False
    assert gate.quotient_defects == ("Q^0:rank=1",)


def test_brst_momentum_height_projection_gate_detects_upper_square_defect():
    gate = brst_momentum_height_projection_gate(
        degree_heights={0: (0,), 1: (0,), 2: (0,)},
        degree_momenta={0: ("a",), 1: ("a",), 2: ("a",)},
        differentials={
            0: ((1,),),
            1: ((1,),),
        },
        upper_height=0,
        lower_height=0,
    )
    assert gate.closed is False
    assert gate.upper_is_complex is False
    assert gate.lower_is_complex is False
    assert gate.upper_square_defects == ("Q^1Q^0:rank=1",)
    assert gate.lower_square_defects == ("Q^1Q^0:rank=1",)


def test_brst_momentum_height_projection_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="lower_height"):
        brst_momentum_height_projection_gate(
            degree_heights={0: (0,), 1: (0,)},
            degree_momenta={0: ("a",), 1: ("a",)},
            differentials={0: ((0,),)},
            upper_height=0,
            lower_height=1,
        )
    with pytest.raises(ValueError, match="heights and momenta"):
        brst_momentum_height_projection_gate(
            degree_heights={0: (0,), 1: (0,)},
            degree_momenta={0: ("a", "b"), 1: ("a",)},
            differentials={0: ((0,),)},
            upper_height=0,
            lower_height=0,
        )
    with pytest.raises(ValueError, match="Q\\^0"):
        brst_momentum_height_projection_gate(
            degree_heights={0: (0, 1), 1: (0,)},
            degree_momenta={0: ("a", "b"), 1: ("a",)},
            differentials={0: ((0,),)},
            upper_height=1,
            lower_height=0,
        )


def test_yangian_witness_templates():
    witness = yangian_witness(8)
    assert witness.current_limit_weight_one is True
    assert witness.sample_multiplicities[-1] == 1
    assert witness.sample_multiplicities[0] == 10
    assert witness.sample_multiplicities[3] == -64
    assert witness.sample_multiplicities[4] == 108
    assert witness.current_packet.status == "FINITE_YANGIAN_CURRENT_CANDIDATE_PACKET"
    assert witness.current_packet.all_weight_one_at_epsilon1 is True
    assert witness.spectral_kernel_packet.status == "FINITE_YANGIAN_SPECTRAL_KERNEL_LABEL_PACKET"
    assert witness.spectral_kernel_packet.noncartan_kernel_labels == witness.current_packet.total_dimension
    assert witness.self_ope_pole_packet.status == "FINITE_YANGIAN_SELF_OPE_POLE_LAYER_PACKET"
    assert witness.self_ope_pole_packet.pole_discriminants == (3,)
    assert witness.spectral_associator_obstruction.status == "FINITE_SPECTRAL_ASSOCIATOR_DATA_MISSING"
    assert witness.spectral_associator_obstruction.strict_r_matrix_criterion_satisfied is False


def test_yangian_current_candidate_packet_dimensions():
    packet = yangian_current_candidate_packet(max_discriminant=4, max_mode=2)
    rows = {row.discriminant: row for row in packet.rows}
    assert packet.support == (-1, 0, 3, 4)
    assert rows[-1].undeformed_weight == 0
    assert rows[0].undeformed_weight == 1
    assert rows[3].undeformed_weight == 4
    assert rows[4].undeformed_weight == 5
    assert rows[3].deformed_weight_epsilon1 == 1
    assert rows[3].modes == (0, 1, 2)
    assert rows[3].finite_dimension == 64 * 3
    assert rows[3].superdimension == -64 * 3
    assert packet.total_dimension == (1 + 10 + 64 + 108) * 3
    assert packet.total_superdimension == (1 + 10 - 64 + 108) * 3


def test_yangian_current_packet_transition_commutes():
    transition = yangian_current_packet_transition(8, 4, 3, 1)
    assert transition.status == "FINITE_YANGIAN_PACKET_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.defects == ()
    assert transition.retained_support == (-1, 0, 3, 4)
    assert transition.retained_modes == (0, 1)


def test_yangian_current_packet_transition_rejects_reversed_bounds():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        yangian_current_packet_transition(4, 8, 3, 1)
    with pytest.raises(ValueError, match="lower_mode"):
        yangian_current_packet_transition(8, 4, 1, 3)


def test_yangian_spectral_kernel_label_packet_counts_positive_negative_duals():
    packet = yangian_spectral_kernel_label_packet(
        max_discriminant=4,
        max_mode=2,
        cartan_label_count=5,
    )
    rows = {row.discriminant: row for row in packet.rows}
    assert packet.status == "FINITE_YANGIAN_SPECTRAL_KERNEL_LABEL_PACKET"
    assert packet.support == (-1, 0, 3, 4)
    assert packet.positive_label_count == (1 + 10 + 64 + 108) * 3
    assert packet.negative_label_count == packet.positive_label_count
    assert packet.noncartan_kernel_labels == packet.positive_label_count
    assert packet.tensor_monomials == 2 * packet.positive_label_count
    assert packet.total_kernel_labels_with_cartan == packet.positive_label_count + 5
    assert rows[3].current_labels == 64 * 3
    assert rows[3].dual_labels == 64 * 3
    assert rows[3].tensor_monomials == 2 * 64 * 3
    assert rows[3].parity == "fermionic"
    assert rows[3].parity_sign == -1
    assert rows[4].parity == "bosonic"
    assert rows[4].parity_sign == 1


def test_yangian_spectral_kernel_transition_commutes():
    transition = yangian_spectral_kernel_transition(8, 4, 3, 1, 7, 5)
    assert transition.status == "FINITE_YANGIAN_SPECTRAL_KERNEL_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.defects == ()
    assert transition.retained_discriminants == (-1, 0, 3, 4)


def test_yangian_spectral_kernel_transition_rejects_reversed_bounds():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        yangian_spectral_kernel_transition(4, 8, 3, 1)
    with pytest.raises(ValueError, match="lower_mode"):
        yangian_spectral_kernel_transition(8, 4, 1, 3)
    with pytest.raises(ValueError, match="lower_cartan_label_count"):
        yangian_spectral_kernel_transition(8, 4, 3, 1, 2, 3)


def test_yangian_self_ope_pole_layer_packet():
    packet = yangian_self_ope_pole_layer_packet(max_discriminant=8, max_mode=2)
    rows = {row.discriminant: row for row in packet.rows}
    assert packet.status == "FINITE_YANGIAN_SELF_OPE_POLE_LAYER_PACKET"
    assert packet.pole_discriminants == (3,)
    assert packet.marginal_discriminants == (0, 4)
    assert packet.regular_discriminants == (-1, 7, 8)
    assert packet.total_pole_layers == 3
    assert packet.total_pole_layer_dimension == 64 * 64 * 3 * 3 * 3

    assert rows[3].exponent == -3
    assert rows[3].singularity_type == "pole"
    assert rows[3].pole_order == 3
    assert rows[3].ordered_pair_dimension == 64 * 64 * 3 * 3
    assert rows[3].pole_layer_dimension == 64 * 64 * 3 * 3 * 3
    assert rows[3].pole_layer_superdimension == 64 * 64 * 3 * 3 * 3
    assert rows[3].target_discriminant == 12
    assert rows[3].target_signed_coefficient == 4016
    assert rows[0].singularity_type == "marginal"
    assert rows[4].target_discriminant == 16
    assert rows[7].singularity_type == "regular"


def test_yangian_self_ope_pole_transition_commutes():
    transition = yangian_self_ope_pole_transition(8, 4, 3, 1)
    assert transition.status == "FINITE_YANGIAN_SELF_OPE_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.defects == ()
    assert transition.retained_discriminants == (-1, 0, 3, 4)


def test_yangian_self_ope_pole_transition_rejects_reversed_bounds():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        yangian_self_ope_pole_transition(4, 8, 3, 1)
    with pytest.raises(ValueError, match="lower_mode"):
        yangian_self_ope_pole_transition(8, 4, 1, 3)


def test_yangian_label_tower_transition_commutes_across_three_packets():
    transition = yangian_label_tower_transition(8, 4, 3, 1, 7, 5)
    assert transition.status == "FINITE_YANGIAN_LABEL_TOWER_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.defects == ()
    assert transition.retained_discriminants == (-1, 0, 3, 4)
    assert transition.retained_modes == (0, 1)
    assert transition.current.transition_commutes is True
    assert transition.spectral_kernel.transition_commutes is True
    assert transition.self_ope_pole.transition_commutes is True
    assert transition.component_statuses == {
        "current": "FINITE_YANGIAN_PACKET_TRANSITION",
        "spectral_kernel": "FINITE_YANGIAN_SPECTRAL_KERNEL_TRANSITION",
        "self_ope_pole": "FINITE_YANGIAN_SELF_OPE_TRANSITION",
    }
    assert transition.component_defects == {
        "current": (),
        "spectral_kernel": (),
        "self_ope_pole": (),
    }
    assert transition.component_gates == {
        "current": True,
        "spectral_kernel": True,
        "self_ope_pole": True,
    }
    assert transition.component_size_data["current"] == {
        "upper_support_size": 6,
        "lower_support_size": 4,
        "upper_total_dimension": (1 + 10 + 64 + 108 + 513 + 808) * 4,
        "lower_total_dimension": (1 + 10 + 64 + 108) * 2,
        "upper_total_superdimension": (1 + 10 - 64 + 108 - 513 + 808) * 4,
        "lower_total_superdimension": (1 + 10 - 64 + 108) * 2,
        "upper_mode_count": 4,
        "lower_mode_count": 2,
    }
    assert transition.component_size_data["spectral_kernel"] == {
        "upper_support_size": 6,
        "lower_support_size": 4,
        "upper_noncartan_kernel_labels": (1 + 10 + 64 + 108 + 513 + 808) * 4,
        "lower_noncartan_kernel_labels": (1 + 10 + 64 + 108) * 2,
        "upper_tensor_monomials": 2 * (1 + 10 + 64 + 108 + 513 + 808) * 4,
        "lower_tensor_monomials": 2 * (1 + 10 + 64 + 108) * 2,
        "upper_cartan_label_count": 7,
        "lower_cartan_label_count": 5,
    }
    assert transition.component_size_data["self_ope_pole"] == {
        "upper_support_size": 6,
        "lower_support_size": 4,
        "upper_total_pole_layers": 3,
        "lower_total_pole_layers": 3,
        "upper_total_pole_layer_dimension": 64 * 64 * 4 * 4 * 3,
        "lower_total_pole_layer_dimension": 64 * 64 * 2 * 2 * 3,
        "upper_pole_discriminant_count": 1,
        "lower_pole_discriminant_count": 1,
    }


def test_yangian_label_tower_transition_preserves_component_defects(monkeypatch):
    original_transition = k3e_witness_module.yangian_spectral_kernel_transition

    def defective_spectral_kernel_transition(*args, **kwargs):
        clean = original_transition(*args, **kwargs)
        return replace(
            clean,
            defects=("synthetic_kernel_defect",),
            transition_commutes=False,
            status="FINITE_YANGIAN_SPECTRAL_KERNEL_TRANSITION_DEFECT",
        )

    monkeypatch.setattr(
        k3e_witness_module,
        "yangian_spectral_kernel_transition",
        defective_spectral_kernel_transition,
    )
    transition = yangian_label_tower_transition(8, 4, 3, 1, 7, 5)
    assert transition.status == "FINITE_YANGIAN_LABEL_TOWER_TRANSITION_DEFECT"
    assert transition.transition_commutes is False
    assert transition.defects == ("spectral_kernel:synthetic_kernel_defect",)
    assert transition.component_defects["current"] == ()
    assert transition.component_defects["spectral_kernel"] == ("synthetic_kernel_defect",)
    assert transition.component_defects["self_ope_pole"] == ()
    assert transition.component_gates == {
        "current": True,
        "spectral_kernel": False,
        "self_ope_pole": True,
    }


def test_yangian_label_tower_transition_rejects_reversed_bounds():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        yangian_label_tower_transition(4, 8, 3, 1)
    with pytest.raises(ValueError, match="lower_mode"):
        yangian_label_tower_transition(8, 4, 1, 3)
    with pytest.raises(ValueError, match="lower_cartan_label_count"):
        yangian_label_tower_transition(8, 4, 3, 1, 2, 3)


def test_yangian_residue_transition_commutes_for_coordinate_projection():
    transition = yangian_residue_transition(
        8,
        4,
        3,
        1,
        upper_residue_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        lower_residue_matrix=((1, 0), (0, 1)),
        source_projection=((1, 0, 0), (0, 1, 0)),
        target_projection=((1, 0, 0), (0, 1, 0)),
    )
    assert transition.status == "FINITE_YANGIAN_RESIDUE_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.commutator_defect_rank == 0
    assert transition.upper_residue_shape == (3, 3)
    assert transition.lower_residue_shape == (2, 2)
    assert transition.source_projection_shape == (2, 3)
    assert transition.target_projection_shape == (2, 3)
    assert transition.target_after_upper_residue == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert transition.lower_residue_after_source == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert transition.commutator_matrix == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def test_yangian_residue_transition_detects_commutator_defect():
    transition = yangian_residue_transition(
        8,
        4,
        3,
        1,
        upper_residue_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        lower_residue_matrix=((1, 0), (0, 0)),
        source_projection=((1, 0, 0), (0, 1, 0)),
        target_projection=((1, 0, 0), (0, 1, 0)),
    )
    assert transition.status == "FINITE_YANGIAN_RESIDUE_TRANSITION_DEFECT"
    assert transition.transition_commutes is False
    assert transition.target_after_upper_residue == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert transition.lower_residue_after_source == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    assert transition.commutator_matrix == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert transition.commutator_defect_rank == 1


def test_yangian_residue_transition_rejects_reversed_bounds_and_shape_defect():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        yangian_residue_transition(
            4,
            8,
            3,
            1,
            upper_residue_matrix=((1,),),
            lower_residue_matrix=((1,),),
            source_projection=((1,),),
            target_projection=((1,),),
        )
    with pytest.raises(ValueError, match="lower_mode"):
        yangian_residue_transition(
            8,
            4,
            1,
            3,
            upper_residue_matrix=((1,),),
            lower_residue_matrix=((1,),),
            source_projection=((1,),),
            target_projection=((1,),),
        )
    with pytest.raises(ValueError, match="source_projection"):
        yangian_residue_transition(
            8,
            4,
            3,
            1,
            upper_residue_matrix=((1, 0), (0, 1)),
            lower_residue_matrix=((1,),),
            source_projection=((1,),),
            target_projection=((1, 0),),
        )
    with pytest.raises(ValueError, match="common width"):
        yangian_residue_transition(
            8,
            4,
            3,
            1,
            upper_residue_matrix=((1, 0), (0,)),
            lower_residue_matrix=((1,),),
            source_projection=((1, 0),),
            target_projection=((1, 0),),
        )


def test_yangian_brst_residue_chain_gate_descends_to_cohomology():
    gate = yangian_brst_residue_chain_gate(
        8,
        3,
        q0_matrix=((1,), (0,)),
        q1_matrix=((0, 1),),
        residue_degree0_matrix=((2,),),
        residue_degree1_matrix=((2, 0), (0, 3)),
        residue_degree2_matrix=((3,),),
    )
    assert gate.status == "FINITE_YANGIAN_BRST_RESIDUE_CHAIN_GATE"
    assert gate.brst_complex is True
    assert gate.residue_commutes_with_brst is True
    assert gate.descends_to_h1 is True
    assert gate.degree0_dimension == 1
    assert gate.degree1_dimension == 2
    assert gate.degree2_dimension == 1
    assert gate.brst_square == ((Fraction(0),),)
    assert gate.residue1_after_q0 == ((Fraction(2),), (Fraction(0),))
    assert gate.q0_after_residue0 == ((Fraction(2),), (Fraction(0),))
    assert gate.boundary_commutator_defect_rank == 0
    assert gate.cycle_commutator_defect_rank == 0


def test_yangian_brst_residue_chain_gate_detects_chain_defects():
    gate = yangian_brst_residue_chain_gate(
        8,
        3,
        q0_matrix=((1,), (0,)),
        q1_matrix=((0, 1),),
        residue_degree0_matrix=((2,),),
        residue_degree1_matrix=((2, 0), (0, 4)),
        residue_degree2_matrix=((3,),),
    )
    assert gate.status == "FINITE_YANGIAN_BRST_RESIDUE_CHAIN_DEFECT"
    assert gate.brst_complex is True
    assert gate.residue_commutes_with_brst is False
    assert gate.descends_to_h1 is False
    assert gate.boundary_commutator_defect_rank == 0
    assert gate.cycle_commutator_matrix == ((Fraction(0), Fraction(-1)),)
    assert gate.cycle_commutator_defect_rank == 1


def test_yangian_brst_residue_chain_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="q1_matrix width"):
        yangian_brst_residue_chain_gate(
            8,
            3,
            q0_matrix=((1,), (0,)),
            q1_matrix=((1, 0, 0),),
            residue_degree0_matrix=((1,),),
            residue_degree1_matrix=((1, 0), (0, 1)),
            residue_degree2_matrix=((1,),),
        )
    with pytest.raises(ValueError, match="residue_degree1_matrix"):
        yangian_brst_residue_chain_gate(
            8,
            3,
            q0_matrix=((1,), (0,)),
            q1_matrix=((0, 1),),
            residue_degree0_matrix=((1,),),
            residue_degree1_matrix=((1,),),
            residue_degree2_matrix=((1,),),
        )


def test_finite_bridge_transition_square_commutes_for_projection_square():
    square = finite_bridge_transition_square(
        "bar",
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0), (0, 1)),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0), (0, 1)),
    )
    assert square.status == "FINITE_BRIDGE_TRANSITION_SQUARE"
    assert square.transition_commutes is True
    assert square.commutator_defect_rank == 0
    assert square.upper_map_shape == (2, 3)
    assert square.lower_map_shape == (2, 2)
    assert square.source_transition_shape == (2, 3)
    assert square.target_transition_shape == (2, 2)
    assert square.target_after_upper_map == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert square.lower_map_after_source == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert square.commutator_matrix == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def test_finite_bridge_transition_square_accepts_zero_dimensional_square():
    square = finite_bridge_transition_square(
        "zero",
        5,
        3,
        upper_comparison_map=(),
        lower_comparison_map=(),
        source_transition=(),
        target_transition=(),
    )
    assert square.status == "FINITE_BRIDGE_TRANSITION_SQUARE"
    assert square.transition_commutes is True
    assert square.upper_map_shape == (0, 0)
    assert square.lower_map_shape == (0, 0)
    assert square.source_transition_shape == (0, 0)
    assert square.target_transition_shape == (0, 0)
    assert square.target_after_upper_map == ()
    assert square.lower_map_after_source == ()
    assert square.commutator_matrix == ()
    assert square.commutator_defect_rank == 0


def test_finite_bridge_transition_square_detects_rank_defect():
    square = finite_bridge_transition_square(
        "scattering",
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0), (0, 0)),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0), (0, 1)),
    )
    assert square.status == "FINITE_BRIDGE_TRANSITION_SQUARE_DEFECT"
    assert square.transition_commutes is False
    assert square.target_after_upper_map == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert square.lower_map_after_source == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    assert square.commutator_matrix == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert square.commutator_defect_rank == 1


def test_finite_bridge_transition_square_rejects_shape_and_height_defects():
    import pytest

    with pytest.raises(ValueError, match="lower_height"):
        finite_bridge_transition_square(
            "brst",
            3,
            5,
            upper_comparison_map=((1,),),
            lower_comparison_map=((1,),),
            source_transition=((1,),),
            target_transition=((1,),),
        )
    with pytest.raises(ValueError, match="source_transition"):
        finite_bridge_transition_square(
            "rademacher",
            5,
            3,
            upper_comparison_map=((1, 0),),
            lower_comparison_map=((1,),),
            source_transition=((1,),),
            target_transition=((1,),),
        )
    with pytest.raises(ValueError, match="common width"):
        finite_bridge_transition_square(
            "Yang",
            5,
            3,
            upper_comparison_map=((1, 0), (0,)),
            lower_comparison_map=((1,),),
            source_transition=((1, 0),),
            target_transition=((1, 0),),
        )


def _commuting_bridge_square(bridge):
    return finite_bridge_transition_square(
        bridge,
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0), (0, 1)),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0), (0, 1)),
    )


def test_finite_bridge_system_transition_report_closes_all_five_components():
    report = finite_bridge_system_transition_report(
        _commuting_bridge_square(bridge)
        for bridge in ("scatt", "bar", "rad", "BRST", "Yang")
    )
    assert report.status == "FINITE_BRIDGE_SYSTEM_TRANSITION"
    assert report.upper_height == 5
    assert report.lower_height == 3
    assert report.required_bridges == ("scatt", "bar", "rad", "BRST", "Yang")
    assert report.present_bridges == ("scatt", "bar", "rad", "BRST", "Yang")
    assert report.missing_bridges == ()
    assert report.defective_bridges == ()
    assert report.all_squares_commute is True
    assert report.component_defect_ranks == {
        "scatt": 0,
        "bar": 0,
        "rad": 0,
        "BRST": 0,
        "Yang": 0,
    }
    assert report.component_statuses["bar"] == "FINITE_BRIDGE_TRANSITION_SQUARE"
    assert report.component_gates == {
        "scatt": True,
        "bar": True,
        "rad": True,
        "BRST": True,
        "Yang": True,
    }
    assert report.component_square_data["bar"]["target_after_upper_map"] == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.component_square_data["bar"]["lower_map_after_source"] == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.component_square_data["bar"]["commutator_matrix"] == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    assert report.component_square_data["bar"]["commutator_defect_rank"] == 0


def test_finite_bridge_system_transition_report_detects_missing_and_defective_components():
    defective_rad = finite_bridge_transition_square(
        "rad",
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0), (0, 0)),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0), (0, 1)),
    )
    report = finite_bridge_system_transition_report(
        (
            _commuting_bridge_square("scatt"),
            _commuting_bridge_square("bar"),
            defective_rad,
            _commuting_bridge_square("BRST"),
        )
    )
    assert report.status == "FINITE_BRIDGE_SYSTEM_TRANSITION_DEFECT"
    assert report.missing_bridges == ("Yang",)
    assert report.defective_bridges == ("rad",)
    assert report.component_statuses["rad"] == "FINITE_BRIDGE_TRANSITION_SQUARE_DEFECT"
    assert report.component_gates["rad"] is False
    assert report.component_defect_ranks["rad"] == 1
    assert report.all_squares_commute is False
    assert report.component_square_data["rad"]["commutator_matrix"] == (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert "Yang" not in report.component_square_data


def test_finite_bridge_system_transition_report_rejects_inconsistent_input():
    import pytest

    with pytest.raises(ValueError, match="at least one"):
        finite_bridge_system_transition_report(())
    with pytest.raises(ValueError, match="common heights"):
        finite_bridge_system_transition_report(
            (
                _commuting_bridge_square("scatt"),
                finite_bridge_transition_square(
                    "bar",
                    6,
                    3,
                    upper_comparison_map=((1, 0, 0), (0, 1, 0)),
                    lower_comparison_map=((1, 0), (0, 1)),
                    source_transition=((1, 0, 0), (0, 1, 0)),
                    target_transition=((1, 0), (0, 1)),
                ),
            )
        )
    with pytest.raises(ValueError, match="duplicate bridge"):
        finite_bridge_system_transition_report(
            (_commuting_bridge_square("scatt"), _commuting_bridge_square("scatt"))
        )


def _exact_bridge_step(bridge):
    return finite_bridge_exactness_step_report(
        bridge,
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0), (0, 1)),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0), (0, 1)),
    )


def _exact_bridge_step_7_to_5(bridge):
    return finite_bridge_exactness_step_report(
        bridge,
        7,
        5,
        upper_comparison_map=((1, 0, 0, 0), (0, 1, 0, 0)),
        lower_comparison_map=((1, 0, 0), (0, 1, 0)),
        source_transition=((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)),
        target_transition=((1, 0), (0, 1)),
    )


def test_finite_bridge_exactness_step_report_checks_full_ml_gate():
    report = _exact_bridge_step("bar")
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_STEP"
    assert report.ml_exactness_gate is True
    assert report.square.transition_commutes is True
    assert report.source_transition_surjective is True
    assert report.target_transition_surjective is True
    assert report.kernel_transition_surjective is True
    assert report.upper_comparison_map == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.lower_comparison_map == (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    assert report.source_transition_matrix == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.target_transition_matrix == (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    assert report.upper_kernel_basis == ((Fraction(0), Fraction(0), Fraction(1)),)
    assert report.lower_kernel_basis == ()
    assert report.kernel_image_vectors == ((Fraction(0), Fraction(0)),)
    assert report.kernel_landing_vectors == ((Fraction(0), Fraction(0)),)
    assert report.target_upper_image == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.image_span_matrix == (
        (Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.cokernel_span_matrix == (
        (Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(1)),
    )
    assert report.lower_source_dimension == 2
    assert report.lower_target_dimension == 2
    assert report.lower_image_rank == 2
    assert report.lower_cokernel_dimension == 0
    assert report.source_transition_rank == report.lower_source_dimension
    assert report.target_transition_rank == report.lower_target_dimension
    assert report.upper_kernel_dimension == 1
    assert report.lower_kernel_dimension == 0
    assert report.kernel_landing_defect_rank == 0
    assert report.image_landing_defect_rank == 0
    assert report.kernel_transition_well_defined is True
    assert report.image_transition_well_defined is True
    assert report.image_transition_rank == report.lower_image_rank
    assert report.cokernel_transition_rank == report.lower_cokernel_dimension
    assert report.image_transition_surjective is True
    assert report.cokernel_transition_well_defined is True
    assert report.cokernel_transition_surjective is True
    assert report.source_surjectivity_defect == 0
    assert report.target_surjectivity_defect == 0
    assert report.kernel_surjectivity_defect == 0
    assert report.image_surjectivity_defect == 0
    assert report.cokernel_surjectivity_defect == 0
    assert report.kernel_image_rank == 0
    assert report.defects == ()


def test_finite_bridge_exactness_step_report_accepts_zero_dimensional_component():
    report = finite_bridge_exactness_step_report(
        "zero",
        5,
        3,
        upper_comparison_map=(),
        lower_comparison_map=(),
        source_transition=(),
        target_transition=(),
    )
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_STEP"
    assert report.ml_exactness_gate is True
    assert report.square.transition_commutes is True
    assert report.upper_comparison_map == ()
    assert report.lower_comparison_map == ()
    assert report.source_transition_matrix == ()
    assert report.target_transition_matrix == ()
    assert report.upper_kernel_basis == ()
    assert report.lower_kernel_basis == ()
    assert report.kernel_image_vectors == ()
    assert report.kernel_landing_vectors == ()
    assert report.target_upper_image == ()
    assert report.image_span_matrix == ()
    assert report.cokernel_span_matrix == ()
    assert report.lower_source_dimension == 0
    assert report.lower_target_dimension == 0
    assert report.lower_image_rank == 0
    assert report.lower_cokernel_dimension == 0
    assert report.source_transition_rank == 0
    assert report.target_transition_rank == 0
    assert report.upper_kernel_dimension == 0
    assert report.lower_kernel_dimension == 0
    assert report.kernel_landing_defect_rank == 0
    assert report.image_landing_defect_rank == 0
    assert report.kernel_image_rank == 0
    assert report.image_transition_rank == 0
    assert report.cokernel_transition_rank == 0
    assert report.source_surjectivity_defect == 0
    assert report.target_surjectivity_defect == 0
    assert report.kernel_surjectivity_defect == 0
    assert report.image_surjectivity_defect == 0
    assert report.cokernel_surjectivity_defect == 0
    assert report.source_transition_surjective is True
    assert report.target_transition_surjective is True
    assert report.kernel_transition_well_defined is True
    assert report.image_transition_well_defined is True
    assert report.cokernel_transition_well_defined is True
    assert report.kernel_transition_surjective is True
    assert report.image_transition_surjective is True
    assert report.cokernel_transition_surjective is True
    assert report.defects == ()


def test_finite_bridge_exactness_step_report_detects_kernel_transition_defect():
    report = finite_bridge_exactness_step_report(
        "Yang",
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0),),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0),),
    )
    assert report.square.transition_commutes is True
    assert report.source_transition_surjective is True
    assert report.target_transition_surjective is True
    assert report.kernel_transition_surjective is False
    assert report.lower_source_dimension == 2
    assert report.lower_target_dimension == 1
    assert report.lower_cokernel_dimension == 0
    assert report.source_transition_rank == report.lower_source_dimension
    assert report.target_transition_rank == report.lower_target_dimension
    assert report.upper_kernel_dimension == 1
    assert report.lower_kernel_dimension == 1
    assert report.upper_kernel_basis == ((Fraction(0), Fraction(0), Fraction(1)),)
    assert report.lower_kernel_basis == ((Fraction(0), Fraction(1)),)
    assert report.kernel_image_vectors == ((Fraction(0), Fraction(0)),)
    assert report.kernel_landing_vectors == ((Fraction(0),),)
    assert report.kernel_landing_defect_rank == 0
    assert report.image_landing_defect_rank == 0
    assert report.kernel_transition_well_defined is True
    assert report.image_transition_well_defined is True
    assert report.image_transition_rank == 1
    assert report.cokernel_transition_rank == 0
    assert report.image_transition_surjective is True
    assert report.cokernel_transition_well_defined is True
    assert report.cokernel_transition_surjective is True
    assert report.source_surjectivity_defect == 0
    assert report.target_surjectivity_defect == 0
    assert report.kernel_surjectivity_defect == 1
    assert report.image_surjectivity_defect == 0
    assert report.cokernel_surjectivity_defect == 0
    assert report.kernel_image_rank == 0
    assert report.defects == ("kernel_transition_not_surjective",)
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_STEP_DEFECT"


def test_finite_bridge_exactness_step_report_detects_kernel_landing_defect():
    report = finite_bridge_exactness_step_report(
        "BRST",
        5,
        3,
        upper_comparison_map=((1, 0, 0),),
        lower_comparison_map=((1, 0),),
        source_transition=((1, 1, 0), (0, 0, 1)),
        target_transition=((1,),),
    )
    assert report.square.transition_commutes is False
    assert report.source_transition_surjective is True
    assert report.target_transition_surjective is True
    assert report.upper_kernel_dimension == 2
    assert report.lower_kernel_dimension == 1
    assert report.kernel_landing_defect_rank == 1
    assert report.image_landing_defect_rank == 0
    assert report.kernel_transition_well_defined is False
    assert report.image_transition_well_defined is True
    assert report.image_transition_rank == 1
    assert report.cokernel_transition_rank == 0
    assert report.image_transition_surjective is True
    assert report.cokernel_transition_well_defined is True
    assert report.cokernel_transition_surjective is True
    assert report.kernel_transition_surjective is False
    assert report.kernel_surjectivity_defect == 0
    assert report.image_surjectivity_defect == 0
    assert report.cokernel_surjectivity_defect == 0
    assert report.defects == (
        "square_commutator_nonzero",
        "kernel_transition_not_well_defined",
        "kernel_transition_not_surjective",
    )


def test_finite_bridge_exactness_step_report_detects_image_landing_defect():
    report = finite_bridge_exactness_step_report(
        "scatt",
        5,
        3,
        upper_comparison_map=((1,),),
        lower_comparison_map=((0,),),
        source_transition=((1,),),
        target_transition=((1,),),
    )
    assert report.square.transition_commutes is False
    assert report.source_transition_surjective is True
    assert report.target_transition_surjective is True
    assert report.image_landing_defect_rank == 1
    assert report.image_transition_well_defined is False
    assert report.image_transition_rank == 1
    assert report.lower_cokernel_dimension == 1
    assert report.cokernel_transition_rank == 1
    assert report.image_transition_surjective is False
    assert report.cokernel_transition_well_defined is False
    assert report.cokernel_transition_surjective is False
    assert report.kernel_landing_defect_rank == 0
    assert report.kernel_transition_well_defined is True
    assert report.kernel_transition_surjective is False
    assert report.defects == (
        "square_commutator_nonzero",
        "image_transition_not_well_defined",
        "kernel_transition_not_surjective",
    )


def test_finite_bridge_exactness_step_report_detects_image_surjectivity_defect():
    report = finite_bridge_exactness_step_report(
        "rad",
        5,
        3,
        upper_comparison_map=((0, 0),),
        lower_comparison_map=((1, 0),),
        source_transition=((0, 0), (1, 0)),
        target_transition=((1,),),
    )
    assert report.square.transition_commutes is True
    assert report.source_transition_surjective is False
    assert report.target_transition_surjective is True
    assert report.kernel_transition_well_defined is True
    assert report.kernel_transition_surjective is True
    assert report.image_landing_defect_rank == 0
    assert report.image_transition_well_defined is True
    assert report.image_transition_rank == 0
    assert report.image_transition_surjective is False
    assert report.lower_cokernel_dimension == 0
    assert report.cokernel_transition_rank == 0
    assert report.cokernel_transition_well_defined is True
    assert report.cokernel_transition_surjective is True
    assert report.source_surjectivity_defect == 1
    assert report.image_surjectivity_defect == 1
    assert report.cokernel_surjectivity_defect == 0
    assert report.defects == (
        "source_transition_not_surjective",
        "image_transition_not_surjective",
    )


def test_finite_bridge_exactness_step_report_detects_cokernel_surjectivity_defect():
    report = finite_bridge_exactness_step_report(
        "bar",
        5,
        3,
        upper_comparison_map=((1,),),
        lower_comparison_map=((1, 0), (0, 0)),
        source_transition=((1,), (0,)),
        target_transition=((1,), (0,)),
    )
    assert report.square.transition_commutes is True
    assert report.source_transition_surjective is False
    assert report.target_transition_surjective is False
    assert report.image_transition_well_defined is True
    assert report.image_transition_surjective is True
    assert report.lower_cokernel_dimension == 1
    assert report.cokernel_transition_rank == 0
    assert report.cokernel_transition_well_defined is True
    assert report.cokernel_transition_surjective is False
    assert report.kernel_transition_well_defined is True
    assert report.kernel_transition_surjective is False
    assert report.source_surjectivity_defect == 1
    assert report.target_surjectivity_defect == 1
    assert report.kernel_surjectivity_defect == 1
    assert report.image_surjectivity_defect == 0
    assert report.cokernel_surjectivity_defect == 1
    assert report.defects == (
        "source_transition_not_surjective",
        "target_transition_not_surjective",
        "kernel_transition_not_surjective",
        "cokernel_transition_not_surjective",
    )


def test_finite_bridge_system_exactness_report_aggregates_all_five_components():
    report = finite_bridge_system_exactness_report(
        _exact_bridge_step(bridge)
        for bridge in ("scatt", "bar", "rad", "BRST", "Yang")
    )
    assert report.status == "FINITE_BRIDGE_SYSTEM_ML_EXACTNESS"
    assert report.missing_bridges == ()
    assert report.defective_bridges == ()
    assert report.component_defects == {
        "scatt": (),
        "bar": (),
        "rad": (),
        "BRST": (),
        "Yang": (),
    }
    assert all(
        all(component_gate.values())
        for component_gate in report.component_gates.values()
    )
    assert report.component_gates["bar"] == {
        "transition_square_commutes": True,
        "source_transition_surjective": True,
        "target_transition_surjective": True,
        "kernel_transition_well_defined": True,
        "kernel_transition_surjective": True,
        "image_transition_well_defined": True,
        "image_transition_surjective": True,
        "cokernel_transition_well_defined": True,
        "cokernel_transition_surjective": True,
    }
    assert report.component_rank_data["bar"]["source_transition_rank"] == (
        report.component_rank_data["bar"]["lower_source_dimension"]
    )
    assert report.component_rank_data["bar"]["target_transition_rank"] == (
        report.component_rank_data["bar"]["lower_target_dimension"]
    )
    assert report.component_rank_data["bar"]["kernel_image_rank"] == (
        report.component_rank_data["bar"]["lower_kernel_dimension"]
    )
    assert report.component_rank_data["bar"]["image_transition_rank"] == (
        report.component_rank_data["bar"]["lower_image_rank"]
    )
    assert report.component_rank_data["bar"]["cokernel_transition_rank"] == (
        report.component_rank_data["bar"]["lower_cokernel_dimension"]
    )
    assert report.component_rank_data["bar"]["source_surjectivity_defect"] == 0
    assert report.component_rank_data["bar"]["target_surjectivity_defect"] == 0
    assert report.component_rank_data["bar"]["kernel_surjectivity_defect"] == 0
    assert report.component_rank_data["bar"]["image_surjectivity_defect"] == 0
    assert report.component_rank_data["bar"]["cokernel_surjectivity_defect"] == 0
    assert report.component_exactness_data["bar"]["upper_kernel_basis"] == (
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    assert report.component_exactness_data["bar"]["kernel_image_vectors"] == (
        (Fraction(0), Fraction(0)),
    )
    assert report.component_exactness_data["bar"]["target_upper_image"] == (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.component_exactness_data["bar"]["image_span_matrix"] == (
        (Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
    )
    assert report.component_exactness_data["bar"]["cokernel_span_matrix"] == (
        (Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(1)),
    )
    assert report.all_components_ml_exact is True


def test_finite_bridge_system_exactness_report_detects_missing_and_defective_components():
    defective_yang = finite_bridge_exactness_step_report(
        "Yang",
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0),),
        source_transition=((1, 0, 0), (0, 1, 0)),
        target_transition=((1, 0),),
    )
    report = finite_bridge_system_exactness_report(
        (
            _exact_bridge_step("scatt"),
            _exact_bridge_step("bar"),
            _exact_bridge_step("rad"),
            defective_yang,
        )
    )
    assert report.status == "FINITE_BRIDGE_SYSTEM_ML_EXACTNESS_DEFECT"
    assert report.missing_bridges == ("BRST",)
    assert report.defective_bridges == ("Yang",)
    assert report.component_defects["Yang"] == ("kernel_transition_not_surjective",)
    assert report.component_gates["Yang"]["transition_square_commutes"] is True
    assert report.component_gates["Yang"]["kernel_transition_well_defined"] is True
    assert report.component_gates["Yang"]["kernel_transition_surjective"] is False
    assert report.component_gates["Yang"]["image_transition_surjective"] is True
    assert report.component_rank_data["Yang"]["kernel_image_rank"] == 0
    assert report.component_rank_data["Yang"]["lower_kernel_dimension"] == 1
    assert report.component_rank_data["Yang"]["kernel_surjectivity_defect"] == 1
    assert report.component_rank_data["Yang"]["source_surjectivity_defect"] == 0
    assert report.component_rank_data["Yang"]["target_surjectivity_defect"] == 0
    assert report.component_rank_data["Yang"]["image_surjectivity_defect"] == 0
    assert report.component_rank_data["Yang"]["cokernel_surjectivity_defect"] == 0
    assert report.component_rank_data["Yang"]["source_transition_rank"] == (
        report.component_rank_data["Yang"]["lower_source_dimension"]
    )
    assert report.component_rank_data["Yang"]["image_transition_rank"] == (
        report.component_rank_data["Yang"]["lower_image_rank"]
    )
    assert report.component_exactness_data["Yang"]["upper_kernel_basis"] == (
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    assert report.component_exactness_data["Yang"]["lower_kernel_basis"] == (
        (Fraction(0), Fraction(1)),
    )
    assert report.component_exactness_data["Yang"]["kernel_image_vectors"] == (
        (Fraction(0), Fraction(0)),
    )
    assert report.component_exactness_data["Yang"]["kernel_landing_vectors"] == (
        (Fraction(0),),
    )
    assert "BRST" not in report.component_exactness_data
    assert report.all_components_ml_exact is False


def test_finite_bridge_system_exactness_report_rejects_inconsistent_input():
    import pytest

    with pytest.raises(ValueError, match="at least one"):
        finite_bridge_system_exactness_report(())
    with pytest.raises(ValueError, match="common heights"):
        finite_bridge_system_exactness_report(
            (
                _exact_bridge_step("scatt"),
                finite_bridge_exactness_step_report(
                    "bar",
                    6,
                    3,
                    upper_comparison_map=((1, 0, 0), (0, 1, 0)),
                    lower_comparison_map=((1, 0), (0, 1)),
                    source_transition=((1, 0, 0), (0, 1, 0)),
                    target_transition=((1, 0), (0, 1)),
                ),
            )
        )
    with pytest.raises(ValueError, match="duplicate bridge"):
        finite_bridge_system_exactness_report(
            (_exact_bridge_step("scatt"), _exact_bridge_step("scatt"))
        )


def test_finite_bridge_exactness_tower_report_composes_exact_steps():
    report = finite_bridge_exactness_tower_report(
        (_exact_bridge_step_7_to_5("bar"), _exact_bridge_step("bar"))
    )
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_TOWER"
    assert report.bridge == "bar"
    assert report.upper_height == 7
    assert report.lower_height == 3
    assert report.step_heights == ((7, 5), (5, 3))
    assert report.step_count == 2
    assert report.all_steps_ml_exact is True
    assert report.tower_ml_exact is True
    assert report.step_defects == {}
    assert report.composed_source_transition == (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    )
    assert report.composed_target_transition == (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    assert report.composed_step_report.status == "FINITE_BRIDGE_ML_EXACTNESS_STEP"
    assert report.composed_step_report.ml_exactness_gate is True
    assert report.composed_step_report.upper_height == 7
    assert report.composed_step_report.lower_height == 3
    assert report.composed_step_report.square.transition_commutes is True


def test_finite_bridge_exactness_tower_report_detects_defective_step():
    defective_step = finite_bridge_exactness_step_report(
        "bar",
        5,
        3,
        upper_comparison_map=((1, 0, 0), (0, 1, 0)),
        lower_comparison_map=((1, 0), (0, 1)),
        source_transition=((1, 0, 0), (0, 0, 0)),
        target_transition=((1, 0), (0, 1)),
    )
    report = finite_bridge_exactness_tower_report(
        (_exact_bridge_step_7_to_5("bar"), defective_step)
    )
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_TOWER_DEFECT"
    assert report.all_steps_ml_exact is False
    assert report.tower_ml_exact is False
    assert report.step_defects == {
        "5->3": (
            "square_commutator_nonzero",
            "source_transition_not_surjective",
        )
    }
    assert report.composed_step_report.ml_exactness_gate is False
    assert report.composed_step_report.defects == defective_step.defects


def test_finite_bridge_exactness_tower_report_accepts_single_step():
    step = _exact_bridge_step("rad")
    report = finite_bridge_exactness_tower_report((step,))
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_TOWER"
    assert report.step_count == 1
    assert report.step_heights == ((5, 3),)
    assert report.composed_source_transition == step.source_transition_matrix
    assert report.composed_target_transition == step.target_transition_matrix
    assert report.composed_step_report.ml_exactness_gate is True


def test_finite_bridge_exactness_tower_report_accepts_zero_dimensional_tower():
    upper = finite_bridge_exactness_step_report(
        "zero",
        7,
        5,
        upper_comparison_map=(),
        lower_comparison_map=(),
        source_transition=(),
        target_transition=(),
    )
    lower = finite_bridge_exactness_step_report(
        "zero",
        5,
        3,
        upper_comparison_map=(),
        lower_comparison_map=(),
        source_transition=(),
        target_transition=(),
    )
    report = finite_bridge_exactness_tower_report((upper, lower))
    assert report.status == "FINITE_BRIDGE_ML_EXACTNESS_TOWER"
    assert report.composed_source_transition == ()
    assert report.composed_target_transition == ()
    assert report.composed_step_report.ml_exactness_gate is True
    assert report.tower_ml_exact is True


def test_finite_bridge_exactness_tower_report_rejects_inconsistent_input():
    import pytest

    with pytest.raises(ValueError, match="at least one"):
        finite_bridge_exactness_tower_report(())
    with pytest.raises(ValueError, match="common bridge"):
        finite_bridge_exactness_tower_report(
            (_exact_bridge_step_7_to_5("bar"), _exact_bridge_step("rad"))
        )
    with pytest.raises(ValueError, match="contiguous height tower"):
        finite_bridge_exactness_tower_report(
            (
                _exact_bridge_step_7_to_5("bar"),
                finite_bridge_exactness_step_report(
                    "bar",
                    4,
                    3,
                    upper_comparison_map=((1, 0, 0), (0, 1, 0)),
                    lower_comparison_map=((1, 0), (0, 1)),
                    source_transition=((1, 0, 0), (0, 1, 0)),
                    target_transition=((1, 0), (0, 1)),
                ),
            )
        )
    with pytest.raises(ValueError, match="identify adjacent comparison maps"):
        finite_bridge_exactness_tower_report(
            (
                _exact_bridge_step_7_to_5("bar"),
                finite_bridge_exactness_step_report(
                    "bar",
                    5,
                    3,
                    upper_comparison_map=((1, 0, 0), (0, 0, 1)),
                    lower_comparison_map=((1, 0), (0, 1)),
                    source_transition=((1, 0, 0), (0, 0, 1)),
                    target_transition=((1, 0), (0, 1)),
                ),
            )
        )


def test_yangian_ope_coefficient_transition_commutes_for_injective_truncation():
    transition = yangian_ope_coefficient_transition(
        8,
        4,
        3,
        1,
        upper_coefficients={
            ("e3_a", "e0_b", "e3_c"): 2,
            ("e7_r0_a", "e0_r0_b", "e7_r0_c"): 11,
        },
        lower_coefficients={
            ("e3_a", "e0_b", "e3_c"): 2,
        },
        label_projection={
            "e3_a": "e3_a",
            "e0_b": "e0_b",
            "e3_c": "e3_c",
            "e7_r0_a": None,
            "e0_r0_b": "e0_r0_b",
            "e7_r0_c": None,
        },
    )
    assert transition.status == "FINITE_YANGIAN_OPE_COEFFICIENT_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.upper_entry_count == 2
    assert transition.lower_entry_count == 1
    assert transition.projected_entry_count == 1
    assert transition.discarded_entry_count == 1
    assert transition.projected_coefficients == {
        ("e3_a", "e0_b", "e3_c"): Fraction(2),
    }
    assert transition.lower_coefficients_normalized == {
        ("e3_a", "e0_b", "e3_c"): Fraction(2),
    }
    assert transition.noninjective_projection_labels == ()
    assert transition.support_defects == ()
    assert transition.coefficient_defects == ()


def test_yangian_ope_coefficient_transition_rejects_many_to_one_aggregation():
    transition = yangian_ope_coefficient_transition(
        8,
        4,
        3,
        1,
        upper_coefficients={
            ("e3_r0_a", "e0_r0_b", "e3_r0_c"): 2,
            ("e3_r1_a", "e0_r0_b", "e3_r0_c"): 5,
        },
        lower_coefficients={
            ("e3_a", "e0_b", "e3_c"): 7,
        },
        label_projection={
            "e3_r0_a": "e3_a",
            "e3_r1_a": "e3_a",
            "e0_r0_b": "e0_b",
            "e3_r0_c": "e3_c",
        },
    )
    assert transition.status == "FINITE_YANGIAN_OPE_COEFFICIENT_TRANSITION_DEFECT"
    assert transition.transition_commutes is False
    assert transition.projected_coefficients == {
        ("e3_a", "e0_b", "e3_c"): Fraction(7),
    }
    assert transition.lower_coefficients_normalized == {
        ("e3_a", "e0_b", "e3_c"): Fraction(7),
    }
    assert transition.noninjective_projection_labels == ("e3_a",)
    assert transition.support_defects == ()
    assert transition.coefficient_defects == ()


def test_yangian_ope_coefficient_transition_detects_coefficient_defect():
    transition = yangian_ope_coefficient_transition(
        8,
        4,
        3,
        1,
        upper_coefficients={
            ("e3_r0_a", "e0_r0_b", "e3_r0_c"): 2,
        },
        lower_coefficients={
            ("e3_a", "e0_b", "e3_c"): 3,
        },
        label_projection={
            "e3_r0_a": "e3_a",
            "e0_r0_b": "e0_b",
            "e3_r0_c": "e3_c",
        },
    )
    assert transition.status == "FINITE_YANGIAN_OPE_COEFFICIENT_TRANSITION_DEFECT"
    assert transition.transition_commutes is False
    assert transition.projected_coefficients == {
        ("e3_a", "e0_b", "e3_c"): Fraction(2),
    }
    assert transition.lower_coefficients_normalized == {
        ("e3_a", "e0_b", "e3_c"): Fraction(3),
    }
    assert transition.noninjective_projection_labels == ()
    assert transition.coefficient_defects == ("('e3_a', 'e0_b', 'e3_c'):2!=3",)


def test_yangian_ope_coefficient_transition_detects_support_and_projection_defects():
    transition = yangian_ope_coefficient_transition(
        8,
        4,
        3,
        1,
        upper_coefficients={
            ("e3_r0_a", "e0_r0_b", "e3_r0_c"): 2,
            ("e4_r0_a", "e0_r0_b", "e4_r0_c"): 1,
        },
        lower_coefficients={
            ("e3_a", "e0_b", "e3_c"): 2,
            ("missing_lower", "e0_b", "missing_target"): 1,
        },
        label_projection={
            "e3_r0_a": "e3_a",
            "e0_r0_b": "e0_b",
            "e3_r0_c": "e3_c",
            "e4_r0_a": "e4_a",
        },
    )
    assert transition.status == "FINITE_YANGIAN_OPE_COEFFICIENT_TRANSITION_DEFECT"
    assert transition.missing_projection_labels == ("e4_r0_c",)
    assert transition.noninjective_projection_labels == ()
    assert transition.projected_coefficients == {
        ("e3_a", "e0_b", "e3_c"): Fraction(2),
    }
    assert transition.lower_coefficients_normalized == {
        ("e3_a", "e0_b", "e3_c"): Fraction(2),
        ("missing_lower", "e0_b", "missing_target"): Fraction(1),
    }
    assert transition.support_defects == (
        "missing:('missing_lower', 'e0_b', 'missing_target')",
    )


def test_yangian_ope_coefficient_transition_rejects_reversed_bounds():
    import pytest

    with pytest.raises(ValueError, match="lower_discriminant"):
        yangian_ope_coefficient_transition(
            4,
            8,
            3,
            1,
            upper_coefficients={},
            lower_coefficients={},
            label_projection={},
        )
    with pytest.raises(ValueError, match="lower_mode"):
        yangian_ope_coefficient_transition(
            8,
            4,
            1,
            3,
            upper_coefficients={},
            lower_coefficients={},
            label_projection={},
        )


def test_yangian_ope_serre_ideal_span_gate_closes_for_equal_relation_spans():
    gate = yangian_ope_serre_ideal_span_gate(
        ((1, 0, 0), (0, 1, 0)),
        ((1, 1, 0), (1, -1, 0)),
        finite_bound=4,
        max_mode=2,
    )
    assert gate.status == "FINITE_YANGIAN_OPE_SERRE_IDEAL_SPAN_GATE"
    assert gate.closed is True
    assert gate.spans_equal is True
    assert gate.ambient_dimension == 3
    assert gate.ope_relation_rank == 2
    assert gate.serre_relation_rank == 2
    assert gate.combined_relation_rank == 2
    assert gate.ope_rows_missing_from_serre_span == ()
    assert gate.serre_rows_missing_from_ope_span == ()


def test_yangian_ope_serre_ideal_span_gate_detects_ope_extra_relation():
    gate = yangian_ope_serre_ideal_span_gate(
        ((1, 0), (0, 1)),
        ((1, 0),),
    )
    assert gate.status == "FINITE_YANGIAN_OPE_SERRE_IDEAL_SPAN_DEFECT"
    assert gate.closed is False
    assert gate.serre_span_contains_ope is False
    assert gate.ope_span_contains_serre is True
    assert gate.ope_rows_missing_from_serre_span == (1,)
    assert gate.serre_rows_missing_from_ope_span == ()
    assert gate.combined_relation_rank == 2


def test_yangian_ope_serre_ideal_span_gate_detects_missing_serre_relation():
    gate = yangian_ope_serre_ideal_span_gate(
        ((1, 0),),
        ((1, 0), (0, 1)),
    )
    assert gate.status == "FINITE_YANGIAN_OPE_SERRE_IDEAL_SPAN_DEFECT"
    assert gate.closed is False
    assert gate.serre_span_contains_ope is True
    assert gate.ope_span_contains_serre is False
    assert gate.ope_rows_missing_from_serre_span == ()
    assert gate.serre_rows_missing_from_ope_span == (1,)
    assert gate.combined_relation_rank == 2


def test_yangian_ope_serre_ideal_span_gate_accepts_empty_zero_span():
    gate = yangian_ope_serre_ideal_span_gate(
        (),
        (),
        ambient_dimension=2,
    )
    assert gate.status == "FINITE_YANGIAN_OPE_SERRE_IDEAL_SPAN_GATE"
    assert gate.closed is True
    assert gate.ambient_dimension == 2
    assert gate.ope_relation_rank == 0
    assert gate.serre_relation_rank == 0
    assert gate.combined_relation_rank == 0


def test_yangian_ope_serre_ideal_span_gate_rejects_width_defects():
    import pytest

    with pytest.raises(ValueError, match="ambient_dimension is required"):
        yangian_ope_serre_ideal_span_gate((), ())
    with pytest.raises(ValueError, match="ambient_dimension columns"):
        yangian_ope_serre_ideal_span_gate(((1, 0),), ((1, 0),), ambient_dimension=3)
    with pytest.raises(ValueError, match="ambient_dimension columns"):
        yangian_ope_serre_ideal_span_gate(((1, 0),), ((1, 0, 0),))


def test_yangian_pbw_associated_graded_gate_closes_for_blockwise_isomorphism():
    gate = yangian_pbw_associated_graded_gate(
        (1, 2),
        (1, 2),
        (
            ((1,),),
            ((1, 0), (0, 1)),
        ),
        finite_bound=4,
        max_mode=2,
    )
    assert gate.status == "FINITE_YANGIAN_PBW_ASSOCIATED_GRADED_GATE"
    assert gate.closed is True
    assert gate.finite_filtered_isomorphism is True
    assert gate.hilbert_vectors_equal is True
    assert gate.associated_graded_surjective is True
    assert gate.associated_graded_isomorphism is True
    assert gate.source_total_dimension == 3
    assert gate.target_total_dimension == 3
    assert gate.block_ranks == (1, 2)
    assert gate.block_surjectivity_defects == (0, 0)
    assert gate.block_kernel_excess_dimensions == (0, 0)
    assert gate.defective_blocks == ()


def test_yangian_pbw_associated_graded_gate_detects_extra_source_normal_forms():
    gate = yangian_pbw_associated_graded_gate(
        (2,),
        (1,),
        (
            ((1, 0),),
        ),
    )
    assert gate.status == "FINITE_YANGIAN_PBW_ASSOCIATED_GRADED_DEFECT"
    assert gate.closed is False
    assert gate.associated_graded_surjective is True
    assert gate.hilbert_vectors_equal is False
    assert gate.hilbert_vector_difference == (1,)
    assert gate.hilbert_vector_defect_rank == 1
    assert gate.block_surjectivity_defects == (0,)
    assert gate.block_kernel_excess_dimensions == (1,)
    assert gate.defective_blocks == (0,)


def test_yangian_pbw_associated_graded_gate_detects_nonsurjective_block():
    gate = yangian_pbw_associated_graded_gate(
        (2,),
        (2,),
        (
            ((1, 0), (0, 0)),
        ),
    )
    assert gate.status == "FINITE_YANGIAN_PBW_ASSOCIATED_GRADED_DEFECT"
    assert gate.closed is False
    assert gate.hilbert_vectors_equal is True
    assert gate.associated_graded_surjective is False
    assert gate.associated_graded_isomorphism is False
    assert gate.block_ranks == (1,)
    assert gate.block_surjectivity_defects == (1,)
    assert gate.block_kernel_excess_dimensions == (1,)
    assert gate.defective_blocks == (0,)


def test_yangian_pbw_associated_graded_gate_accepts_zero_block():
    gate = yangian_pbw_associated_graded_gate(
        (0,),
        (0,),
        ((),),
    )
    assert gate.closed is True
    assert gate.source_total_dimension == 0
    assert gate.target_total_dimension == 0
    assert gate.block_ranks == (0,)


def test_yangian_pbw_associated_graded_gate_rejects_malformed_blocks():
    import pytest

    with pytest.raises(ValueError, match="nonnegative"):
        yangian_pbw_associated_graded_gate((-1,), (0,), ((),))
    with pytest.raises(ValueError, match="same length"):
        yangian_pbw_associated_graded_gate((1, 1), (1,), (((1,),),))
    with pytest.raises(ValueError, match="one associated-graded block"):
        yangian_pbw_associated_graded_gate((1,), (1,), ())
    with pytest.raises(ValueError, match="target_dim rows"):
        yangian_pbw_associated_graded_gate((1,), (2,), (((1,),),))
    with pytest.raises(ValueError, match="source_dim columns"):
        yangian_pbw_associated_graded_gate((2,), (1,), (((1,),),))
    with pytest.raises(ValueError, match="zero rows"):
        yangian_pbw_associated_graded_gate((0,), (0,), (((1,),),))


def test_yangian_spectral_associator_missing_data_reports_open_boundary():
    packet = yangian_spectral_associator_obstruction_packet(4, 1)
    assert packet.status == "FINITE_SPECTRAL_ASSOCIATOR_DATA_MISSING"
    assert packet.current_support == (-1, 0, 3, 4)
    assert packet.current_dimension == (1 + 10 + 64 + 108) * 2
    assert packet.missing_inputs == (
        "spectral_associator_cochain",
        "spectral_pentagon_differential",
        "admissible_gauge_coboundary_basis",
    )
    assert packet.pentagon_differential == ()
    assert packet.gauge_coboundary_basis == ()
    assert packet.gauge_constraint_matrix == ()
    assert packet.associator_boundary == ()
    assert packet.gauge_cocycle_matrix == ()
    assert packet.gauge_constraint_product == ()
    assert packet.quasi_factorization_criterion_satisfied is False
    assert packet.strict_r_matrix_criterion_satisfied is False


def test_yangian_spectral_associator_strict_r_matrix_criterion():
    packet = yangian_spectral_associator_obstruction_packet(
        4,
        1,
        associator_cochain=(1, 1),
        pentagon_differential=((1, -1),),
        gauge_coboundary_basis=((1, 1),),
        gauge_constraint_matrix=((1, -1),),
    )
    assert packet.status == "FINITE_SPECTRAL_STRICT_R_MATRIX_CRITERION_SATISFIED"
    assert packet.cochain_dimension == 2
    assert packet.associator_cochain == (Fraction(1), Fraction(1))
    assert packet.pentagon_differential == ((Fraction(1), Fraction(-1)),)
    assert packet.gauge_coboundary_basis == ((Fraction(1), Fraction(1)),)
    assert packet.gauge_constraint_matrix == ((Fraction(1), Fraction(-1)),)
    assert packet.associator_boundary == (Fraction(0),)
    assert packet.gauge_cocycle_matrix == ((Fraction(0),),)
    assert packet.gauge_constraint_product == ((Fraction(0),),)
    assert packet.pentagon_equation_count == 1
    assert packet.gauge_generator_count == 1
    assert packet.gauge_constraint_count == 1
    assert packet.cocycle_defect_rank == 0
    assert packet.gauge_cocycle_defect_rank == 0
    assert packet.gauge_constraint_defect_rank == 0
    assert packet.strictification_defect == 0
    assert packet.quasi_factorization_criterion_satisfied is True
    assert packet.strict_r_matrix_criterion_satisfied is True


def test_yangian_spectral_associator_detects_pentagon_defect():
    packet = yangian_spectral_associator_obstruction_packet(
        4,
        1,
        associator_cochain=(1, 0),
        pentagon_differential=((1, -1),),
        gauge_coboundary_basis=((1, 1),),
        gauge_constraint_matrix=((1, -1),),
    )
    assert packet.status == "FINITE_SPECTRAL_ASSOCIATOR_COCYCLE_DEFECT"
    assert packet.associator_boundary == (Fraction(1),)
    assert packet.gauge_cocycle_matrix == ((Fraction(0),),)
    assert packet.gauge_constraint_product == ((Fraction(0),),)
    assert packet.cocycle_defect_rank == 1
    assert packet.quasi_factorization_criterion_satisfied is False
    assert packet.strict_r_matrix_criterion_satisfied is False


def test_yangian_spectral_associator_detects_nontrivial_class():
    packet = yangian_spectral_associator_obstruction_packet(
        4,
        1,
        associator_cochain=(1, 0),
        pentagon_differential=((0, 0),),
        gauge_coboundary_basis=((0, 1),),
        gauge_constraint_matrix=((1, 0),),
    )
    assert packet.status == "FINITE_SPECTRAL_ASSOCIATOR_CLASS_NONTRIVIAL"
    assert packet.associator_boundary == (Fraction(0),)
    assert packet.gauge_cocycle_matrix == ((Fraction(0),),)
    assert packet.gauge_constraint_product == ((Fraction(0),),)
    assert packet.cocycle_defect_rank == 0
    assert packet.gauge_cocycle_defect_rank == 0
    assert packet.gauge_constraint_defect_rank == 0
    assert packet.strictification_defect == 1
    assert packet.quasi_factorization_criterion_satisfied is True
    assert packet.strict_r_matrix_criterion_satisfied is False


def test_yangian_spectral_associator_validates_cochain_widths():
    import pytest

    with pytest.raises(ValueError, match="cochain width"):
        yangian_spectral_associator_obstruction_packet(
            4,
            1,
            associator_cochain=(1, 0),
            pentagon_differential=((1, -1, 0),),
            gauge_coboundary_basis=((1, 1),),
        )


def test_yangian_spectral_r_matrix_equation_gate_closes_for_exact_equations():
    gate = yangian_spectral_r_matrix_equation_gate(
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
        finite_bound=4,
        max_mode=2,
    )
    assert gate.status == "FINITE_YANGIAN_SPECTRAL_R_MATRIX_EQUATION_GATE"
    assert gate.closed is True
    assert gate.matrix_dimension == 2
    assert gate.ybe_defect_rank == 0
    assert gate.unitarity_defect_rank == 0
    assert gate.yang_baxter_satisfied is True
    assert gate.unitarity_satisfied is True
    assert gate.strict_r_matrix_equations_satisfied is True
    assert gate.ybe_difference == (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    assert gate.unitarity_difference == (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )


def test_yangian_spectral_r_matrix_equation_gate_detects_ybe_defect():
    gate = yangian_spectral_r_matrix_equation_gate(
        ((1, 1), (0, 1)),
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
    )
    assert gate.status == "FINITE_YANGIAN_SPECTRAL_R_MATRIX_EQUATION_DEFECT"
    assert gate.closed is False
    assert gate.ybe_defect_rank == 1
    assert gate.unitarity_defect_rank == 0
    assert gate.yang_baxter_satisfied is False
    assert gate.unitarity_satisfied is True


def test_yangian_spectral_r_matrix_equation_gate_detects_unitarity_defect():
    gate = yangian_spectral_r_matrix_equation_gate(
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
        ((1, 0), (0, 2)),
    )
    assert gate.status == "FINITE_YANGIAN_SPECTRAL_R_MATRIX_EQUATION_DEFECT"
    assert gate.closed is False
    assert gate.ybe_defect_rank == 0
    assert gate.unitarity_defect_rank == 1
    assert gate.yang_baxter_satisfied is True
    assert gate.unitarity_satisfied is False


def test_yangian_spectral_r_matrix_equation_gate_accepts_custom_identity():
    gate = yangian_spectral_r_matrix_equation_gate(
        ((2, 0), (0, 2)),
        ((2, 0), (0, 2)),
        ((2, 0), (0, 2)),
        identity_matrix=((2, 0), (0, 2)),
    )
    assert gate.closed is True
    assert gate.identity_matrix == (
        (Fraction(2), Fraction(0)),
        (Fraction(0), Fraction(2)),
    )


def test_yangian_spectral_r_matrix_equation_gate_rejects_shape_defects():
    import pytest

    with pytest.raises(ValueError, match="nonempty"):
        yangian_spectral_r_matrix_equation_gate((), (), ())
    with pytest.raises(ValueError, match="yang_baxter_left_matrix must have shape"):
        yangian_spectral_r_matrix_equation_gate(((1, 0),), ((1, 0),), ((1, 0),))
    with pytest.raises(ValueError, match="yang_baxter_right_matrix must have shape"):
        yangian_spectral_r_matrix_equation_gate(
            ((1, 0), (0, 1)),
            ((1,),),
            ((1, 0), (0, 1)),
        )
    with pytest.raises(ValueError, match="unitarity_product_matrix must have shape"):
        yangian_spectral_r_matrix_equation_gate(
            ((1, 0), (0, 1)),
            ((1, 0), (0, 1)),
            ((1,),),
        )
    with pytest.raises(ValueError, match="identity_matrix must have shape"):
        yangian_spectral_r_matrix_equation_gate(
            ((1, 0), (0, 1)),
            ((1, 0), (0, 1)),
            ((1, 0), (0, 1)),
            identity_matrix=((1,),),
        )


def test_yangian_spectral_associator_transition_commutes():
    transition = yangian_spectral_associator_transition(
        8,
        4,
        3,
        1,
        upper_associator_cochain=(1, 1, 0),
        lower_associator_cochain=(1, 1),
        upper_pentagon_differential=((1, -1, 0), (0, 0, 1)),
        lower_pentagon_differential=((1, -1),),
        upper_gauge_coboundary_basis=((1, 1, 0),),
        lower_gauge_coboundary_basis=((1, 1),),
        cochain_projection=((1, 0, 0), (0, 1, 0)),
        boundary_projection=((1, 0),),
        upper_gauge_constraint_matrix=((1, -1, 0),),
        lower_gauge_constraint_matrix=((1, -1),),
    )
    assert transition.status == "FINITE_SPECTRAL_ASSOCIATOR_TRANSITION"
    assert transition.transition_commutes is True
    assert transition.defects == ()
    assert transition.projected_associator == (Fraction(1), Fraction(1))
    assert transition.associator_projection_difference == (Fraction(0), Fraction(0))
    assert transition.lower_after_projection == ((Fraction(1), Fraction(-1), Fraction(0)),)
    assert transition.projection_after_upper == ((Fraction(1), Fraction(-1), Fraction(0)),)
    assert transition.pentagon_commutator_matrix == ((Fraction(0), Fraction(0), Fraction(0)),)
    assert transition.projected_gauge_rows == ((Fraction(1), Fraction(1)),)
    assert transition.gauge_projection_failures == ()
    assert transition.associator_projection_defect == 0
    assert transition.pentagon_commutator_defect == 0
    assert transition.gauge_projection_defect == 0
    assert transition.upper_quasi_factorization is True
    assert transition.lower_quasi_factorization is True


def test_yangian_spectral_associator_transition_detects_associator_defect():
    transition = yangian_spectral_associator_transition(
        8,
        4,
        3,
        1,
        upper_associator_cochain=(1, 1, 0),
        lower_associator_cochain=(0, 1),
        upper_pentagon_differential=((1, -1, 0), (0, 0, 1)),
        lower_pentagon_differential=((1, -1),),
        upper_gauge_coboundary_basis=((1, 1, 0),),
        lower_gauge_coboundary_basis=((1, 1),),
        cochain_projection=((1, 0, 0), (0, 1, 0)),
        boundary_projection=((1, 0),),
        upper_gauge_constraint_matrix=((1, -1, 0),),
        lower_gauge_constraint_matrix=((1, -1),),
    )
    assert transition.status == "FINITE_SPECTRAL_ASSOCIATOR_TRANSITION_DEFECT"
    assert transition.projected_associator == (Fraction(1), Fraction(1))
    assert transition.associator_projection_difference == (Fraction(1), Fraction(0))
    assert transition.associator_projection_defect == 1
    assert "associator_projection" in transition.defects


def test_yangian_spectral_associator_transition_detects_pentagon_defect():
    transition = yangian_spectral_associator_transition(
        8,
        4,
        3,
        1,
        upper_associator_cochain=(1, 1, 0),
        lower_associator_cochain=(1, 1),
        upper_pentagon_differential=((1, -1, 0), (0, 0, 1)),
        lower_pentagon_differential=((1, -1),),
        upper_gauge_coboundary_basis=((1, 1, 0),),
        lower_gauge_coboundary_basis=((1, 1),),
        cochain_projection=((1, 0, 0), (0, 1, 0)),
        boundary_projection=((0, 1),),
        upper_gauge_constraint_matrix=((1, -1, 0),),
        lower_gauge_constraint_matrix=((1, -1),),
    )
    assert transition.status == "FINITE_SPECTRAL_ASSOCIATOR_TRANSITION_DEFECT"
    assert transition.lower_after_projection == ((Fraction(1), Fraction(-1), Fraction(0)),)
    assert transition.projection_after_upper == ((Fraction(0), Fraction(0), Fraction(1)),)
    assert transition.pentagon_commutator_matrix == ((Fraction(1), Fraction(-1), Fraction(-1)),)
    assert transition.pentagon_commutator_defect == 1
    assert "pentagon_commutator" in transition.defects


def test_yangian_spectral_associator_transition_detects_gauge_projection_defect():
    transition = yangian_spectral_associator_transition(
        8,
        4,
        3,
        1,
        upper_associator_cochain=(1, 1, 0),
        lower_associator_cochain=(1, 1),
        upper_pentagon_differential=((1, -1, 0), (0, 0, 1)),
        lower_pentagon_differential=((1, -1),),
        upper_gauge_coboundary_basis=((1, 1, 0),),
        lower_gauge_coboundary_basis=((0, 1),),
        cochain_projection=((1, 0, 0), (0, 1, 0)),
        boundary_projection=((1, 0),),
        upper_gauge_constraint_matrix=((1, -1, 0),),
        lower_gauge_constraint_matrix=((1, 0),),
    )
    assert transition.status == "FINITE_SPECTRAL_ASSOCIATOR_TRANSITION_DEFECT"
    assert transition.projected_gauge_rows == ((Fraction(1), Fraction(1)),)
    assert transition.gauge_projection_failures == ("gauge:0",)
    assert transition.gauge_projection_defect == 1
    assert "gauge:0" in transition.defects


def test_finite_bridge_witness_packaging():
    witness = finite_bridge_witness(8, 5, 10)
    assert witness.open_lemmas == [
        "scattering lemma",
        "bar lemma",
        "rademacher lemma",
        "brst lemma",
        "yangian lemma",
    ]
    assert witness.brst.central_charge_balanced is True
    assert witness.bar.rank1_values_constant_24 is True


def test_bridge_obstruction_record_splits_witness_and_gap():
    record = bridge_obstruction_record(8, 5, 10)
    assert record.witnessed.scattering.status == "witnessed at finite discriminant"
    assert record.witnessed.bar.rank1_values_constant_24 is True
    assert record.witnessed.rademacher.status.startswith("rank-one finite-height packet")
    assert record.witnessed.rademacher.finite_height_certificate.max_residual_rel < 0.03
    assert record.operator_boundary.brst.status.startswith("finite coefficient fixture")
    assert record.operator_boundary.yangian.status.startswith("finite current")
    assert record.formal_templates is record.operator_boundary
    assert set(record.finite_boundary_results) == {
        "scattering",
        "bar",
        "rademacher",
        "brst",
        "yangian",
    }
    assert "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}" in (
        record.finite_boundary_results["scattering"]
    )
    assert "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}" in (
        record.finite_boundary_results["scattering"]
    )
    assert "finite_scattering_quantum_torus_gate" in record.finite_boundary_results["scattering"]
    assert "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}" in (
        record.finite_boundary_results["bar"]
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}" in (
        record.finite_boundary_results["bar"]
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}" in (
        record.finite_boundary_results["bar"]
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}" in (
        record.finite_boundary_results["bar"]
    )
    assert "finite_bar_ce_chain_map_gate" in record.finite_boundary_results["bar"]
    assert "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}" in (
        record.finite_boundary_results["rademacher"]
    )
    assert "rademacher_polar_bessel_gate" in record.finite_boundary_results["rademacher"]
    assert "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}" in (
        record.finite_boundary_results["rademacher"]
    )
    assert "rademacher_truncation_error_gate" in record.finite_boundary_results["rademacher"]
    assert "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}" in (
        record.finite_boundary_results["rademacher"]
    )
    assert "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}" in (
        record.finite_boundary_results["brst"]
    )
    assert "Proposition~\\ref{prop:k3e-brst-central-charge-gate}" in (
        record.finite_boundary_results["brst"]
    )
    assert "brst_central_charge_gate" in record.finite_boundary_results["brst"]
    assert "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}" in (
        record.finite_boundary_results["brst"]
    )
    assert "brst_no_ghost_spectral_sequence_gate" in record.finite_boundary_results["brst"]
    assert "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}" in (
        record.finite_boundary_results["brst"]
    )
    assert "brst_borcherds_bracket_gate" in record.finite_boundary_results["brst"]
    assert "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}" in (
        record.finite_boundary_results["brst"]
    )
    assert "brst_borcherds_serre_relation_gate" in (
        record.finite_boundary_results["brst"]
    )
    assert "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}" in (
        record.finite_boundary_results["brst"]
    )
    assert "brst_momentum_height_projection_gate" in (
        record.finite_boundary_results["brst"]
    )
    assert "Proposition~\\ref{prop:k3e-finite-spectral-associator-transition}" in (
        record.finite_boundary_results["yangian"]
    )
    assert "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}" in (
        record.finite_boundary_results["yangian"]
    )
    assert "yangian_brst_residue_chain_gate" in record.finite_boundary_results["yangian"]
    assert "Proposition~\\ref{prop:k3e-finite-yangian-ope-serre-ideal-span-gate}" in (
        record.finite_boundary_results["yangian"]
    )
    assert "yangian_ope_serre_ideal_span_gate" in record.finite_boundary_results["yangian"]
    assert "Proposition~\\ref{prop:k3e-finite-yangian-pbw-associated-graded-gate}" in (
        record.finite_boundary_results["yangian"]
    )
    assert "yangian_pbw_associated_graded_gate" in record.finite_boundary_results["yangian"]
    assert "Proposition~\\ref{prop:k3e-finite-spectral-r-matrix-equation-gate}" in (
        record.finite_boundary_results["yangian"]
    )
    assert "yangian_spectral_r_matrix_equation_gate" in (
        record.finite_boundary_results["yangian"]
    )
    assert "global motivic integration morphism construction" in record.missing_theorems.scattering
    assert "uniform all-height truncation-error theorem beyond the rank-one certificate" in record.missing_theorems.rademacher
    assert "all-orders Omega-deformed vertex-operator construction" in record.missing_theorems.yangian
    assert "heightwise functorial theorem" in record.uniform_gap


def test_bridge_obstruction_record_is_evaluable_from_witnesses():
    partial = bridge_obstruction_record(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    assert partial.missing_theorems.brst == []
    assert partial.missing_theorems.yangian
    assert partial.missing_theorems.empty is False
    assert "heightwise functorial theorem" in partial.uniform_gap

    comparison_only = bridge_obstruction_record(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=(
                "scattering_root_identification",
                "bkm_bar_dictionary",
                "shadow_rademacher_comparison",
                "brst_realization",
                "vertex_operator_yangian",
            ),
        ),
    )
    assert comparison_only.missing_theorems.empty is True
    assert "inverse-limit exactness remains tracked" in comparison_only.uniform_gap

    default = k3e_closure_criterion_report(8, 5, 10)
    closed = bridge_obstruction_record(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.missing_theorems.empty is True
    assert "closes the heightwise functorial theorem" in closed.uniform_gap


def test_bridge_proof_obligation_matrix():
    matrix = bridge_proof_obligation_matrix(8, 5, 10)
    assert matrix.scattering.status.startswith("finite exponent theorem")
    assert matrix.bar.status.startswith("finite bar-CE criterion")
    assert matrix.rademacher.status == "rank-one finite certificate; compact-CY3 shadow theorem open"
    assert matrix.brst.status == "finite supertrace fixture; worldsheet VOA and BRST differential open"
    assert matrix.yangian.status == "finite current and obstruction packets; operator-level Yangian construction open"
    assert "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}" in matrix.scattering.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}" in (
        matrix.scattering.finite_boundary_results
    )
    assert "finite_scattering_quantum_torus_gate" in matrix.scattering.finite_boundary_results
    assert "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}" in matrix.bar.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}" in (
        matrix.bar.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}" in (
        matrix.bar.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}" in (
        matrix.bar.finite_boundary_results
    )
    assert "finite_bar_ce_chain_map_gate" in matrix.bar.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}" in (
        matrix.rademacher.finite_boundary_results
    )
    assert "rademacher_polar_bessel_gate" in matrix.rademacher.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}" in (
        matrix.rademacher.finite_boundary_results
    )
    assert "rademacher_truncation_error_gate" in matrix.rademacher.finite_boundary_results
    assert "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}" in (
        matrix.rademacher.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}" in (
        matrix.brst.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-central-charge-gate}" in (
        matrix.brst.finite_boundary_results
    )
    assert "brst_central_charge_gate" in matrix.brst.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}" in (
        matrix.brst.finite_boundary_results
    )
    assert "brst_no_ghost_spectral_sequence_gate" in matrix.brst.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}" in (
        matrix.brst.finite_boundary_results
    )
    assert "brst_borcherds_bracket_gate" in matrix.brst.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}" in (
        matrix.brst.finite_boundary_results
    )
    assert "brst_borcherds_serre_relation_gate" in matrix.brst.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}" in (
        matrix.brst.finite_boundary_results
    )
    assert "brst_momentum_height_projection_gate" in matrix.brst.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-finite-yangian-label-tower}" in (
        matrix.yangian.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-spectral-associator-obstruction}" in (
        matrix.yangian.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-yangian-ope-serre-ideal-span-gate}" in (
        matrix.yangian.finite_boundary_results
    )
    assert "yangian_ope_serre_ideal_span_gate" in matrix.yangian.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-finite-yangian-pbw-associated-graded-gate}" in (
        matrix.yangian.finite_boundary_results
    )
    assert "yangian_pbw_associated_graded_gate" in matrix.yangian.finite_boundary_results
    assert "Proposition~\\ref{prop:k3e-finite-spectral-r-matrix-equation-gate}" in (
        matrix.yangian.finite_boundary_results
    )
    assert "yangian_spectral_r_matrix_equation_gate" in matrix.yangian.finite_boundary_results
    assert "global motivic integration morphism" in matrix.scattering.missing[0]
    assert "filtered bar-complex map" in matrix.bar.missing[0]
    assert "rank-one residual certificate" in matrix.rademacher.missing[1]
    assert "finite-height VOA and BRST differential" in matrix.brst.missing[0]
    assert "all-orders Omega-deformed vertex operators" in matrix.yangian.missing[0]
    assert matrix.all_entries_proved is False


def test_bridge_proof_obligation_matrix_is_evaluable_from_witnesses():
    partial = bridge_proof_obligation_matrix(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    assert partial.brst.proved is True
    assert partial.brst.missing == []
    assert partial.yangian.proved is False
    assert partial.yangian.missing
    assert partial.all_entries_proved is False

    default = k3e_closure_criterion_report(8, 5, 10)
    closed = bridge_proof_obligation_matrix(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.all_entries_proved is True
    assert all(entry.missing == [] for entry in closed.entries)
    assert all(entry.status == "proved" for entry in closed.entries)


def test_source_recognition_record():
    record = source_recognition_record()
    assert record.gate.closed is False
    assert "oriented_critical_coha" in record.missing_gate_witnesses
    assert "drinfeld_double" in record.missing_gate_witnesses
    assert record.obligation_matrix.gate.target == "Hall-Drinfeld double / BKM denominator gate"
    assert "oriented_critical_coha" in record.obligation_matrix.gate.missing
    assert record.task_map.tasks["source_hall_borcherds_gate"].tasks[0].startswith(
        "construct the oriented critical CoHA"
    )
    assert record.boundary_report.summary.startswith("the source boundary is the union")
    assert record.boundary_report.obstruction_taxonomy.by_code["o_ML"].layer == "compact_passage"
    assert record.envelope.completed_unquotiented_recognized is False
    assert "R" in record.missing_envelope_defects
    assert "A" in record.missing_envelope_defects
    assert record.source_matrix_forces_faithfulness is False


def test_source_recognition_record_is_evaluable_from_witnesses():
    source_only = source_recognition_record(
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
        ),
    )
    assert source_only.gate.closed is True
    assert source_only.envelope.completed_unquotiented_recognized is True
    assert source_only.obligation_matrix.gate.missing == ()
    assert source_only.obligation_matrix.envelope.missing == ()
    assert source_only.missing_gate_witnesses == []
    assert source_only.missing_envelope_defects == []
    assert source_only.source_matrix_forces_faithfulness is True
    assert source_only.boundary_report.closed is False
    assert source_only.boundary_report.compact_double_report.closed is False
    assert "o_ML = 0" in source_only.boundary_report.required_conditions
    assert "Q_H^sep = 0" in source_only.boundary_report.required_conditions

    source_bridge = source_recognition_record(
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
        ),
    )
    assert source_bridge.boundary_report.compact_double_report.closed is True
    assert source_bridge.boundary_report.pro_recognition_report.closed is False
    assert "o_ML = 0" not in source_bridge.boundary_report.required_conditions
    assert "Q_H^sep = 0" in source_bridge.boundary_report.required_conditions

    default = k3e_closure_criterion_report(8, 5, 10)
    closed = source_recognition_record(
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.boundary_report.closed is True
    assert closed.boundary_report.required_conditions == ()


def test_combined_bridge_audit_report():
    report = k3e_bridge_audit_report(8, 5, 10)
    assert report.finite_witness.bar.rank1_values_constant_24 is True
    assert report.obstruction_record.uniform_gap.startswith("the bridge lacks")
    assert report.proof_matrix.brst.status.startswith("finite supertrace fixture")
    assert "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}" in (
        report.proof_matrix.brst.finite_boundary_results
    )
    assert report.source_recognition.gate.closed is False
    assert "witnessed" in report.summary
    assert "finite BRST/Yangian boundary packets" in report.summary


def test_combined_bridge_audit_report_is_evaluable_from_witnesses():
    source_only = k3e_bridge_audit_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
        ),
    )
    assert source_only.source_recognition.gate.closed is True
    assert source_only.source_recognition.boundary_report.closed is False
    assert source_only.proof_matrix.all_entries_proved is False
    assert "gate and recognition envelope are closed" in source_only.summary
    assert "compact/double source gates and pro-recognition source gates remain open" in source_only.summary

    source_bridge = k3e_bridge_audit_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
        ),
    )
    assert source_bridge.source_recognition.boundary_report.compact_double_report.closed is True
    assert source_bridge.source_recognition.boundary_report.pro_recognition_report.closed is False
    assert "pro-recognition source gates remain open" in source_bridge.summary
    assert "compact/double source gates and pro-recognition" not in source_bridge.summary

    default = k3e_closure_criterion_report(8, 5, 10)
    closed = k3e_bridge_audit_report(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.source_recognition.boundary_report.closed is True
    assert closed.proof_matrix.all_entries_proved is True
    assert closed.obstruction_record.missing_theorems.empty is True
    assert "closes the heightwise functorial theorem" in closed.obstruction_record.uniform_gap
    assert "closed from supplied witnesses" in closed.summary


def test_core_gap_report():
    report = k3e_core_gap_report(8, 5, 10)
    assert "evidence, status, and tasks" in report.summary
    assert len(report.core_gaps) == 7
    assert "framed_d3_assignment" in report.core_gaps
    assert "compact_hall_promotion" in report.core_gaps
    assert "vertex_operator_yangian" in report.core_gaps
    assert "construct a genuine stage-1 factorisation algebra on K3 x E" in report.core_gaps["framed_d3_assignment"].missing[0]
    assert "prove the OPE/Serre/Hall-Borcherds compatibility" in report.core_gaps["vertex_operator_yangian"].missing[2]
    assert "Theorem~\\ref{thm:cy-to-chiral-d3}" in report.core_gaps["framed_d3_assignment"].evidence.chapter
    assert report.core_gaps["compact_hall_promotion"].status.established_boundary[0].startswith("Theorem~\\ref{thm:k3e-positive-half-hall-borcherds-criterion}")
    assert "Theorem~\\ref{thm:k3e-finite-recognition-envelope}" in (
        report.core_gaps["compact_hall_promotion"].status.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}" in (
        report.core_gaps["brst_realization"].status.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-spectral-associator-obstruction}" in (
        report.core_gaps["vertex_operator_yangian"].status.finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}" in (
        report.core_gaps["vertex_operator_yangian"].status.finite_boundary_results
    )
    assert "build the oriented critical CoHA" in report.core_gaps["compact_hall_promotion"].status.missing[0]
    assert report.core_gaps["compact_hall_promotion"].status.proved is False


def test_core_gap_report_is_evaluable_from_witnesses():
    default = k3e_closure_criterion_report(8, 5, 10)
    source_only = k3e_core_gap_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
        ),
    )
    assert all(entry.status.proved is False for entry in source_only.entries)
    assert source_only.core_gaps["compact_hall_promotion"].missing
    assert source_only.core_gaps["compact_hall_promotion"].tasks

    partial = k3e_core_gap_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    brst_gap = partial.core_gaps["brst_realization"]
    assert brst_gap.status.proved is False
    assert "cokernel transition maps are surjective" in brst_gap.missing
    assert "cokernel transition maps are surjective" in brst_gap.tasks

    closed = k3e_core_gap_report(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert all(entry.status.proved for entry in closed.entries)
    assert all(entry.missing == [] for entry in closed.entries)
    assert all(entry.tasks == [] for entry in closed.entries)
    assert closed.core_gaps["vertex_operator_yangian"].status.formal == []
    assert "closes every core comparison gap" in closed.summary


def test_proof_dependency_graph():
    graph = k3e_proof_dependency_graph(8, 5, 10)
    assert graph.topological_order[0] == "source_hall_borcherds_gate"
    assert graph.topological_order[-1] == "vertex_operator_yangian"
    assert ("compact_hall_promotion", "scattering_root_identification") in graph.edges
    assert ("bkm_bar_dictionary", "shadow_rademacher_comparison") in graph.edges
    assert graph.prerequisites["compact_hall_promotion"].prerequisites == [
        "source_recognition_envelope",
        "framed_d3_assignment",
    ]
    assert graph.prerequisites["vertex_operator_yangian"].prerequisites == [
        "brst_realization",
        "shadow_rademacher_comparison",
    ]
    order = {node: index for index, node in enumerate(graph.topological_order)}
    assert all(order[source] < order[target] for source, target in graph.edges)
    assert graph.prerequisites["bkm_bar_dictionary"].prerequisites == [
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
    ]


def test_closure_criterion_report():
    report = k3e_closure_criterion_report(8, 5, 10)
    assert report.closed is False
    assert "source gate" in report.summary
    assert "inverse-limit compatibility and exactness theorem" in report.summary
    assert report.required_conditions[0] == "close the source-side Hall/Borcherds gate"
    assert report.required_conditions[-2] == (
        "prove all heightwise compatibility maps, rank-zero squares, and source/target/kernel/image/cokernel Mittag-Leffler exactness gates"
    )
    assert report.required_conditions[-1].startswith("prove the Q_H^sep/L_H^ex/H_H^HB pro-recognition gates")
    assert_full_inverse_limit_gate(report.inverse_limit_gate, "closure_criterion")
    assert report.inverse_limit_status == "OPEN_REQUIREMENT"
    assert report.proved_inverse_limit_conditions == ()
    assert report.open_inverse_limit_conditions == report.inverse_limit_gate.required_conditions
    assert_full_pro_recognition_gate(report.pro_recognition_gate, "closure_criterion")
    assert report.pro_recognition_status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert report.proved_pro_recognition_conditions == ()
    assert report.open_pro_recognition_conditions == report.pro_recognition_gate.required_conditions
    assert len(report.construction_requirements) == 8
    assert_bridge_requirement(report.construction_requirements[0], "source_hall_borcherds_gate")
    assert_bridge_requirement(report.construction_requirements[-1], "vertex_operator_yangian")
    assert report.dependency_graph.topological_order[-1] == "vertex_operator_yangian"


def test_closure_criterion_report_is_evaluable_from_witnesses():
    default = k3e_closure_criterion_report(8, 5, 10)
    source_only = k3e_closure_criterion_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
        ),
    )
    assert source_only.closed is False
    assert "close the source-side Hall/Borcherds gate" not in source_only.required_conditions
    assert "complete the source recognition envelope" not in source_only.required_conditions
    assert "construct the source Hall/Borcherds compact-double bridge" in (
        source_only.required_conditions
    )
    assert "construct the framed d=3 assignment" in source_only.required_conditions
    assert source_only.construction_requirements[0].status == "open"
    assert source_only.inverse_limit_status == "OPEN_REQUIREMENT"

    closed = k3e_closure_criterion_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=K3E_CLOSURE_BRIDGES,
            inverse_limit_proved_conditions=default.inverse_limit_gate.required_conditions,
            pro_recognition_proved_conditions=default.pro_recognition_gate.required_conditions,
        ),
    )
    assert closed.closed is True
    assert closed.required_conditions == []
    assert all(requirement.status == "proved" for requirement in closed.construction_requirements)
    assert closed.inverse_limit_status == "PROVED"
    assert closed.open_inverse_limit_conditions == ()
    assert closed.pro_recognition_status == "PROVED"
    assert closed.open_pro_recognition_conditions == ()
    assert "closes every condition" in closed.summary


def test_gap_crosswalk_report():
    report = k3e_gap_crosswalk_report(8, 5, 10)
    assert "crosswalk shows where the current evidence stops" in report.summary
    assert "Theorem~\\ref{thm:cy-to-chiral-d3}" in report.evidence_by_gap["framed_d3_assignment"].chapter
    assert "compute/tests/test_hall_borcherds_gate.py" in report.evidence_by_gap["compact_hall_promotion"].tests
    assert "Conjecture~\\ref{conj:k3e-scattering-bkm}" in report.evidence_by_gap["scattering_root_identification"].chapter
    assert "compute/tests/test_borcherds_vertex_yangian.py" in report.evidence_by_gap["vertex_operator_yangian"].tests


def test_gap_crosswalk_report_is_evaluable_from_witnesses():
    default = k3e_closure_criterion_report(8, 5, 10)
    report = k3e_gap_crosswalk_report(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert all(entry.status.proved for entry in report.core_gap_report.entries)
    assert report.core_gap_report.core_gaps["brst_realization"].missing == []
    assert "proved theorem data" in report.summary


def test_gap_status_table():
    table = k3e_gap_status_table(8, 5, 10)
    assert "established boundary" in table.summary
    assert "finite boundary result" in table.summary
    assert "without marking the gap proved" in table.summary
    assert set(table.rows.keys()) == {
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    }
    assert "Theorem~\\ref{thm:k3e-constructed-finite-double-recognition}" in table.rows["compact_hall_promotion"].established_boundary
    assert "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}" in (
        table.rows["scattering_root_identification"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}" in (
        table.rows["scattering_root_identification"].finite_boundary_results
    )
    assert "finite_scattering_quantum_torus_gate" in (
        table.rows["scattering_root_identification"].finite_boundary_results
    )
    assert "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}" in (
        table.rows["bkm_bar_dictionary"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}" in (
        table.rows["bkm_bar_dictionary"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}" in (
        table.rows["bkm_bar_dictionary"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}" in (
        table.rows["bkm_bar_dictionary"].finite_boundary_results
    )
    assert "finite_bar_ce_chain_map_gate" in (
        table.rows["bkm_bar_dictionary"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}" in (
        table.rows["shadow_rademacher_comparison"].finite_boundary_results
    )
    assert "rademacher_polar_bessel_gate" in (
        table.rows["shadow_rademacher_comparison"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}" in (
        table.rows["shadow_rademacher_comparison"].finite_boundary_results
    )
    assert "rademacher_truncation_error_gate" in (
        table.rows["shadow_rademacher_comparison"].finite_boundary_results
    )
    assert "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}" in (
        table.rows["shadow_rademacher_comparison"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-central-charge-gate}" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "brst_central_charge_gate" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "brst_no_ghost_spectral_sequence_gate" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "brst_borcherds_bracket_gate" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "brst_borcherds_serre_relation_gate" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "brst_momentum_height_projection_gate" in (
        table.rows["brst_realization"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-yangian-current-candidate-packet}" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-spectral-associator-transition}" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "yangian_brst_residue_chain_gate" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-yangian-ope-serre-ideal-span-gate}" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "yangian_ope_serre_ideal_span_gate" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-yangian-pbw-associated-graded-gate}" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "yangian_pbw_associated_graded_gate" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "Proposition~\\ref{prop:k3e-finite-spectral-r-matrix-equation-gate}" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "yangian_spectral_r_matrix_equation_gate" in (
        table.rows["vertex_operator_yangian"].finite_boundary_results
    )
    assert "build the oriented critical CoHA" in table.rows["compact_hall_promotion"].missing[0]
    assert "candidate finite-height maps" in table.rows["framed_d3_assignment"].formal[0]
    assert "uniform all-height truncation error theorem" in table.rows["shadow_rademacher_comparison"].missing[2]
    assert "rank-one finite-height Rademacher certificate" in table.rows["shadow_rademacher_comparison"].witnessed
    assert table.rows["brst_realization"].established_boundary[0].startswith(
        "Theorem~\\ref{thm:k3e-frenkel-kac-closure} is conditional"
    )
    assert "residues are genuine BRST cohomology operators" in table.rows["vertex_operator_yangian"].missing[1]
    assert table.rows["vertex_operator_yangian"].proved is False


def test_gap_status_table_is_evaluable_from_witnesses():
    default = k3e_closure_criterion_report(8, 5, 10)
    source_only = k3e_gap_status_table(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
        ),
    )
    assert all(row.proved is False for row in source_only.rows.values())
    assert source_only.rows["compact_hall_promotion"].missing

    partial = k3e_gap_status_table(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("shadow_rademacher_comparison",),
        ),
    )
    assert partial.rows["shadow_rademacher_comparison"].proved is False
    assert "cokernel transition maps are surjective" in (
        partial.rows["shadow_rademacher_comparison"].missing
    )
    assert partial.rows["shadow_rademacher_comparison"].formal == []
    assert partial.rows["vertex_operator_yangian"].proved is False
    assert partial.rows["vertex_operator_yangian"].missing
    assert "inverse-limit obligations keep the affected rows open" in partial.summary

    closed = k3e_gap_status_table(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert all(row.proved for row in closed.rows.values())
    assert all(row.missing == [] for row in closed.rows.values())
    assert all(row.formal == [] for row in closed.rows.values())
    assert "marks every core gap proved" in closed.summary


def test_theorem_boundary_report():
    boundary = k3e_theorem_boundary_report(8, 5, 10)
    assert "the theorem boundary is the union" in boundary.summary
    assert "close the source-side Hall/Borcherds gate" in boundary.source_conditions
    assert "oriented_critical_coha" in boundary.source_conditions
    assert "o_ML = 0" in boundary.source_conditions
    assert "o_cent = 0" in boundary.source_conditions
    assert "construct a genuine stage-1 factorisation algebra on K3 x E" in boundary.comparison_conditions
    assert "prove the OPE/Serre/Hall-Borcherds compatibility" in boundary.comparison_conditions
    assert "prove the inverse-limit compatibility and exactness theorem" in boundary.inverse_limit_conditions
    assert "prove the Mittag-Leffler source/target/kernel/image/cokernel exactness gate" in (
        boundary.inverse_limit_conditions
    )
    assert any(condition.startswith("Q_H^sep:") for condition in boundary.inverse_limit_conditions)
    assert any(condition.startswith("L_H^ex:") for condition in boundary.inverse_limit_conditions)
    assert any(condition.startswith("H_H^HB:") for condition in boundary.inverse_limit_conditions)
    assert "upper images land inside lower images" in boundary.inverse_limit_conditions
    assert "cokernel transition maps are surjective" in boundary.inverse_limit_conditions
    assert_full_inverse_limit_gate(boundary.inverse_limit_gate, "theorem_boundary")
    assert boundary.inverse_limit_status == "OPEN_REQUIREMENT"
    assert boundary.proved_inverse_limit_conditions == ()
    assert boundary.open_inverse_limit_conditions == boundary.inverse_limit_gate.required_conditions
    assert_full_pro_recognition_gate(boundary.pro_recognition_gate, "theorem_boundary")
    assert boundary.pro_recognition_status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert boundary.proved_pro_recognition_conditions == ()
    assert boundary.open_pro_recognition_conditions == boundary.pro_recognition_gate.required_conditions
    assert len(boundary.construction_requirements) == 8
    assert_bridge_requirement(boundary.construction_requirements[3], "scattering_root_identification")
    assert "finite exponent equality is not the motivic integration natural transformation" in (
        boundary.construction_requirements[3].forbidden_promotions
    )
    assert len(boundary.all_conditions) == len(set(boundary.all_conditions))
    assert "prove that transition maps on source and target sides commute" in boundary.all_conditions


def test_theorem_boundary_report_is_evaluable_from_witnesses():
    default = k3e_theorem_boundary_report(8, 5, 10)
    source_only = k3e_theorem_boundary_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
        ),
    )
    assert "close the source-side Hall/Borcherds gate" not in source_only.source_conditions
    assert "complete the source recognition envelope" not in source_only.source_conditions
    assert "oriented_critical_coha" not in source_only.source_conditions
    assert "o_ML = 0" in source_only.source_conditions
    assert "o_cent = 0" in source_only.source_conditions
    assert "construct a genuine stage-1 factorisation algebra on K3 x E" in (
        source_only.comparison_conditions
    )
    assert "prove all heightwise compatibility maps" in source_only.inverse_limit_conditions
    assert source_only.all_conditions

    closed = k3e_theorem_boundary_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=K3E_CLOSURE_BRIDGES,
            inverse_limit_proved_conditions=default.inverse_limit_gate.required_conditions,
            pro_recognition_proved_conditions=default.pro_recognition_gate.required_conditions,
        ),
    )
    assert closed.source_conditions == []
    assert closed.comparison_conditions == []
    assert closed.inverse_limit_conditions == []
    assert closed.all_conditions == []
    assert closed.inverse_limit_status == "PROVED"
    assert closed.pro_recognition_status == "PROVED"
    assert all(requirement.status == "proved" for requirement in closed.construction_requirements)


def test_proof_roadmap_report():
    roadmap = k3e_proof_roadmap_report(8, 5, 10)
    assert "source gate and each labeled BD bridge" in roadmap.summary
    assert "source/target/kernel/image/cokernel exactness gates" in roadmap.summary
    assert roadmap.steps[0].name == "source_hall_borcherds_gate"
    assert roadmap.steps[-1].name == "vertex_operator_yangian"
    assert roadmap.steps[0].proof_method == [
        "construct the oriented critical CoHA with the negative half, Cartan, Hopf pairing, and coproduct",
        "prove defect-vanishing at each finite height and source-recognition completeness",
        "show compatibility with the Hall double and the pro-cone topology",
    ]
    assert roadmap.steps[0].current_evidence.chapter[0] == (
        "Theorem~\\ref{thm:k3e-positive-half-hall-borcherds-criterion}"
    )
    assert roadmap.steps[1].current_evidence.chapter == [
        "Theorem~\\ref{thm:cy-to-chiral-d3}",
        "Remark~\\ref{rem:k3e-core-proof-gaps}",
    ]
    assert roadmap.steps[-1].missing[0] == (
        "prove the Omega-deformed vertex operators exist to all orders at epsilon = 1"
    )
    assert roadmap.status_table.rows["framed_d3_assignment"].formal[0].startswith(
        "candidate finite-height maps"
    )
    assert roadmap.task_map.summary.startswith("the task map breaks each open bridge")
    assert roadmap.task_map.tasks["scattering_root_identification"].tasks[0] == (
        "construct the motivic integration morphism to the quantum torus"
    )
    assert_full_inverse_limit_gate(roadmap.inverse_limit_gate, "proof_roadmap")
    assert roadmap.inverse_limit_status == "OPEN_REQUIREMENT"
    assert roadmap.proved_inverse_limit_conditions == ()
    assert roadmap.open_inverse_limit_conditions == roadmap.inverse_limit_gate.required_conditions
    assert_full_pro_recognition_gate(roadmap.pro_recognition_gate, "proof_roadmap")
    assert roadmap.pro_recognition_status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert roadmap.proved_pro_recognition_conditions == ()
    assert roadmap.open_pro_recognition_conditions == roadmap.pro_recognition_gate.required_conditions
    assert_full_inverse_limit_gate(roadmap.steps[0].inverse_limit_gate, "source_hall_borcherds_gate")
    assert_full_inverse_limit_gate(roadmap.steps[-1].inverse_limit_gate, "vertex_operator_yangian")
    assert len(roadmap.construction_requirements) == 8
    assert_bridge_requirement(roadmap.steps[0].construction_requirement, "source_hall_borcherds_gate")
    assert_bridge_requirement(roadmap.steps[-1].construction_requirement, "vertex_operator_yangian")
    assert "formal residue formulas are not cohomological operators" in (
        roadmap.steps[-1].construction_requirement.forbidden_promotions
    )


def test_proof_roadmap_report_is_evaluable_from_witnesses():
    partial = k3e_proof_roadmap_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    brst_step = {step.name: step for step in partial.steps}["brst_realization"]
    assert brst_step.status == "open"
    assert brst_step.construction_requirement.status == "open"
    assert brst_step.inverse_limit_gate.status == "OPEN_REQUIREMENT"
    assert "cokernel transition maps are surjective" in brst_step.missing

    default = k3e_proof_roadmap_report(8, 5, 10)
    source_bridge_only = k3e_proof_roadmap_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("source_hall_borcherds_gate",),
        ),
    )
    source_step = source_bridge_only.steps[0]
    assert source_step.status == "open"
    assert source_step.construction_requirement.status == "open"
    assert "oriented_critical_coha" in source_step.missing
    assert any(condition.startswith("Q_H^sep:") for condition in source_step.missing)
    assert source_step.proof_method[0].startswith("construct the oriented critical CoHA")

    source_without_pro_recognition = k3e_proof_roadmap_report(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
            inverse_limit_proved_conditions=default.inverse_limit_gate.required_conditions,
        ),
    )
    source_step = source_without_pro_recognition.steps[0]
    assert source_step.status == "open"
    assert source_step.construction_requirement.status == "open"
    assert source_step.proof_method[0] == "Q_H^sep = 0"
    assert any(condition.startswith("H_H^HB:") for condition in source_step.missing)
    assert not any(
        task.startswith("construct the oriented critical CoHA")
        for task in source_step.proof_method
    )

    closed = k3e_proof_roadmap_report(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert all(step.status == "proved" for step in closed.steps)
    assert all(step.missing == [] for step in closed.steps)
    assert all(step.proof_method == [] for step in closed.steps)
    assert closed.inverse_limit_status == "PROVED"
    assert closed.open_inverse_limit_conditions == ()
    assert closed.pro_recognition_status == "PROVED"
    assert closed.open_pro_recognition_conditions == ()
    assert all(step.inverse_limit_gate.status == "PROVED" for step in closed.steps)
    assert_proved_bridge_requirement(
        closed.steps[0].construction_requirement,
        "source_hall_borcherds_gate",
    )
    assert_proved_bridge_requirement(
        closed.steps[-1].construction_requirement,
        "vertex_operator_yangian",
    )
    assert all(
        requirement.status == "proved"
        for requirement in closed.construction_requirements
    )
    assert closed.task_map.tasks["vertex_operator_yangian"].tasks == []


def test_proof_task_map():
    task_map = k3e_proof_task_map(8, 5, 10)
    assert "precise constructions" in task_map.summary
    assert task_map.tasks["source_hall_borcherds_gate"].tasks[0].startswith(
        "construct the oriented critical CoHA"
    )
    assert "source/target/kernel/image/cokernel exactness" in task_map.tasks["brst_realization"].tasks[2]
    assert "R-matrix match" in task_map.tasks["vertex_operator_yangian"].tasks[2]
    assert_full_inverse_limit_gate(task_map.inverse_limit_gate, "proof_task_map")
    assert task_map.inverse_limit_status == "OPEN_REQUIREMENT"
    assert task_map.proved_inverse_limit_conditions == ()
    assert task_map.open_inverse_limit_conditions == task_map.inverse_limit_gate.required_conditions
    assert_full_pro_recognition_gate(task_map.pro_recognition_gate, "proof_task_map")
    assert task_map.pro_recognition_status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert task_map.proved_pro_recognition_conditions == ()
    assert task_map.open_pro_recognition_conditions == task_map.pro_recognition_gate.required_conditions
    assert_full_inverse_limit_gate(
        task_map.tasks["brst_realization"].inverse_limit_gate,
        "brst_realization",
    )
    assert_full_inverse_limit_gate(
        task_map.tasks["vertex_operator_yangian"].inverse_limit_gate,
        "vertex_operator_yangian",
    )
    assert len(task_map.construction_requirements) == 8
    assert_bridge_requirement(
        task_map.tasks["brst_realization"].construction_requirement,
        "brst_realization",
    )
    assert "the finite supertrace fixture is not a worldsheet VOA" in (
        task_map.tasks["brst_realization"].construction_requirement.forbidden_promotions
    )
    assert_bridge_requirement(
        task_map.requirements["vertex_operator_yangian"],
        "vertex_operator_yangian",
    )


def test_proof_task_map_is_evaluable_from_witnesses():
    partial = k3e_proof_task_map(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    brst_task = partial.tasks["brst_realization"]
    assert brst_task.construction_requirement.status == "open"
    assert brst_task.inverse_limit_gate.status == "OPEN_REQUIREMENT"
    assert "cokernel transition maps are surjective" in brst_task.tasks
    assert "construct the worldsheet VOA and BRST differential" not in brst_task.tasks

    default = k3e_proof_task_map(8, 5, 10)
    source_bridge_only = k3e_proof_task_map(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("source_hall_borcherds_gate",),
        ),
    )
    source_task = source_bridge_only.tasks["source_hall_borcherds_gate"]
    assert source_task.construction_requirement.status == "open"
    assert source_task.tasks[0].startswith("construct the oriented critical CoHA")
    assert "oriented_critical_coha" in source_task.tasks
    assert any(condition.startswith("Q_H^sep:") for condition in source_task.tasks)

    source_without_pro_recognition = k3e_proof_task_map(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
            inverse_limit_proved_conditions=default.inverse_limit_gate.required_conditions,
        ),
    )
    source_task = source_without_pro_recognition.tasks["source_hall_borcherds_gate"]
    assert source_task.construction_requirement.status == "open"
    assert source_task.tasks[0] == "Q_H^sep = 0"
    assert any(condition.startswith("H_H^HB:") for condition in source_task.tasks)
    source_coha_task = (
        "construct the oriented critical CoHA with the negative half, Cartan, "
        "Hopf pairing, and coproduct"
    )
    assert source_coha_task not in source_task.tasks

    closed = k3e_proof_task_map(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.inverse_limit_status == "PROVED"
    assert closed.pro_recognition_status == "PROVED"
    assert closed.open_inverse_limit_conditions == ()
    assert closed.open_pro_recognition_conditions == ()
    assert all(entry.tasks == [] for entry in closed.entries)
    assert all(entry.inverse_limit_gate.status == "PROVED" for entry in closed.entries)
    assert_proved_bridge_requirement(
        closed.tasks["source_hall_borcherds_gate"].construction_requirement,
        "source_hall_borcherds_gate",
    )
    assert_proved_bridge_requirement(
        closed.tasks["vertex_operator_yangian"].construction_requirement,
        "vertex_operator_yangian",
    )
    assert all(
        requirement.status == "proved"
        for requirement in closed.construction_requirements
    )


def test_bridge_specification_report():
    spec = k3e_bridge_specification(8, 5, 10)
    assert "theorem schema" in spec.summary
    assert spec.all_entries_open is True
    assert set(spec.open_entries) == {
        "source_hall_borcherds_gate",
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    }
    assert spec.open_schema_obligations
    assert spec.bridges["source_hall_borcherds_gate"].summary.startswith("source gate boundary report")
    assert_open_theorem_schema(spec.bridges["source_hall_borcherds_gate"])
    assert spec.bridges["source_hall_borcherds_gate"].hypotheses[0] == (
        "source-side Hall/Borcherds gate closed"
    )
    assert (
        "establish theorem-schema hypothesis: source-side Hall/Borcherds gate closed"
        in spec.bridges["source_hall_borcherds_gate"].open_obligations
    )
    assert spec.bridges["framed_d3_assignment"].summary.startswith("BD1 theorem schema")
    assert_open_theorem_schema(spec.bridges["framed_d3_assignment"])
    assert spec.bridges["framed_d3_assignment"].hypotheses[0] == (
        "stage-1 factorisation algebra on K3 x E constructed"
    )
    assert spec.bridges["framed_d3_assignment"].conclusion[0] == (
        "Phi_3^(Sigma_2,C) is realized as a framed chiral output"
    )
    assert "construct the motivic integration morphism" in (
        spec.bridges["scattering_root_identification"].obstructions[0]
    )
    assert "Omega-deformed vertex operators exist to all orders" in (
        spec.bridges["vertex_operator_yangian"].hypotheses[0]
    )
    assert_open_theorem_schema(spec.bridges["vertex_operator_yangian"])
    assert_bridge_requirement(
        spec.bridges["bkm_bar_dictionary"].construction_requirement,
        "bkm_bar_dictionary",
    )
    assert "the bar Euler product is not the derived centre or bulk local-operator algebra" in (
        spec.bridges["bkm_bar_dictionary"].construction_requirement.forbidden_promotions
    )


def test_bridge_specification_report_is_evaluable_from_witnesses():
    partial_bridge = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    assert partial_bridge.bridges["brst_realization"].status == "OPEN_THEOREM_SCHEMA"
    assert partial_bridge.bridges["brst_realization"].proved_here is False
    assert "cokernel transition maps are surjective" in (
        partial_bridge.bridges["brst_realization"].open_obligations
    )

    brst_without_dependencies = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    brst_entry = brst_without_dependencies.bridges["brst_realization"]
    assert brst_entry.status == "OPEN_THEOREM_SCHEMA"
    assert brst_entry.proved_here is False
    assert "establish dependency theorem: framed_d3_assignment" in (
        brst_entry.dependency_obligations
    )
    assert "establish dependency theorem: compact_hall_promotion" in (
        brst_entry.dependency_obligations
    )
    assert brst_entry.open_obligations == brst_entry.dependency_obligations

    bar_without_dependencies = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("bkm_bar_dictionary",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    bar_entry = bar_without_dependencies.bridges["bkm_bar_dictionary"]
    assert bar_entry.status == "OPEN_THEOREM_SCHEMA"
    assert bar_entry.proved_here is False
    assert bar_entry.dependency_obligations == (
        "establish dependency theorem: framed_d3_assignment",
        "establish dependency theorem: compact_hall_promotion",
        "establish dependency theorem: scattering_root_identification",
    )
    assert bar_entry.open_obligations == bar_entry.dependency_obligations

    yangian_without_dependencies = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("vertex_operator_yangian",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    yangian_entry = yangian_without_dependencies.bridges["vertex_operator_yangian"]
    assert yangian_entry.status == "OPEN_THEOREM_SCHEMA"
    assert yangian_entry.proved_here is False
    assert yangian_entry.dependency_obligations == (
        "establish dependency theorem: brst_realization",
        "establish dependency theorem: shadow_rademacher_comparison",
    )
    assert yangian_entry.open_obligations == yangian_entry.dependency_obligations

    scattering_without_inverse = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("scattering_root_identification",),
        ),
    )
    scattering_entry = scattering_without_inverse.bridges[
        "scattering_root_identification"
    ]
    assert scattering_entry.status == "OPEN_THEOREM_SCHEMA"
    assert scattering_entry.local_obligations_satisfied is True
    assert "establish dependency theorem: compact_hall_promotion" in (
        scattering_entry.open_obligations
    )
    assert "all heightwise comparison maps are realized" in (
        scattering_entry.open_obligations
    )
    assert not any(
        obligation.startswith("construct the motivic integration morphism")
        for obligation in scattering_entry.open_obligations
    )

    partial_source = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
        ),
    )
    source_entry = partial_source.bridges["source_hall_borcherds_gate"]
    assert source_entry.status == "OPEN_THEOREM_SCHEMA"
    assert source_entry.proved_here is False
    assert any(
        obligation.startswith("H_H^HB:")
        for obligation in source_entry.open_obligations
    )

    source_without_pro_recognition = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    source_entry = source_without_pro_recognition.bridges["source_hall_borcherds_gate"]
    assert source_entry.status == "OPEN_THEOREM_SCHEMA"
    assert source_entry.local_obligations_satisfied is True
    assert source_entry.open_obligations == tuple(source_entry.obstructions)
    assert not any(
        obligation.startswith("construct the oriented critical CoHA")
        for obligation in source_entry.open_obligations
    )

    default = k3e_closure_criterion_report(8, 5, 10)
    closed = k3e_bridge_specification(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.all_entries_open is False
    assert closed.all_entries_proved is True
    assert closed.open_entries == {}
    assert closed.open_schema_obligations == ()
    for entry in closed.entries:
        assert_proved_theorem_schema(entry)
        assert_proved_bridge_requirement(entry.construction_requirement, entry.bridge)
    assert closed.bridges["source_hall_borcherds_gate"].obstructions == []
    assert closed.bridges["vertex_operator_yangian"].obstructions == []


def test_bridge_axiom_pack():
    pack = k3e_bridge_axiom_pack(8, 5, 10)
    assert "axiom-pack boundary report" in pack.summary
    assert pack.all_entries_open is True
    assert set(pack.open_entries) == {
        "BD1",
        "BD2",
        "BD3",
        "BD4",
        "BD5",
        "BD6",
        "BD7",
    }
    assert pack.open_schema_obligations
    assert pack.source_gate.summary.startswith("the source-gate boundary report")
    assert_open_theorem_schema(pack.source_gate)
    assert pack.source_gate.hypotheses[0] == (
        "source-side Hall/Borcherds gate closed"
    )
    assert pack.source_gate.heightwise_compatibility.source_transition_map == "T_{H+1,H}^X"
    assert pack.source_gate.heightwise_compatibility.target_transition_map == (
        "R^{\\mathrm{source}}_{H+1,H,\\mathrm{cand}} = \\pi_{\\mathrm{source},\\leq H}"
    )
    assert pack.source_gate.heightwise_compatibility.inverse_limit_conditions[0] == (
        "source gate admits an inverse-limit lift with rank-zero transition squares"
    )
    assert pack.source_gate.heightwise_compatibility.inverse_limit_conditions[1] == (
        "source-side recognition satisfies the source/target/kernel/image/cokernel Mittag-Leffler gate"
    )
    assert (
        "source-recognition defects vanish uniformly in height"
        in pack.source_gate.open_obligations
    )
    assert_full_inverse_limit_gate(pack.inverse_limit_gate, "bridge_axiom_pack")
    assert pack.inverse_limit_status == "OPEN_REQUIREMENT"
    assert pack.proved_inverse_limit_conditions == ()
    assert pack.open_inverse_limit_conditions == pack.inverse_limit_gate.required_conditions
    assert_full_pro_recognition_gate(pack.pro_recognition_gate, "bridge_axiom_pack")
    assert pack.pro_recognition_status == "OPEN_PRO_RECOGNITION_REQUIREMENT"
    assert pack.proved_pro_recognition_conditions == ()
    assert pack.open_pro_recognition_conditions == pack.pro_recognition_gate.required_conditions
    assert_full_pro_recognition_gate(
        pack.source_gate.pro_recognition_gate,
        "source_hall_borcherds_gate",
    )
    assert any(
        obligation.startswith("H_H^HB:")
        for obligation in pack.source_gate.open_obligations
    )
    assert_full_inverse_limit_gate(
        pack.source_gate.heightwise_compatibility.inverse_limit_gate,
        "source_hall_borcherds_gate",
    )
    assert len(pack.construction_requirements) == 8
    assert_bridge_requirement(
        pack.source_gate.construction_requirement,
        "source_hall_borcherds_gate",
    )
    assert pack.bd_axioms["BD1"].bridge == "framed_d3_assignment"
    assert_open_theorem_schema(pack.bd_axioms["BD1"])
    assert pack.bd_axioms["BD1"].conclusion[0] == (
        "Phi_3^(Sigma_2,C) is realized as a framed chiral output"
    )
    assert (
        pack.bd_axioms["BD1"].heightwise_compatibility.source_transition_map
        == "T_{H+1,H}^X"
    )
    assert pack.bd_axioms["BD1"].heightwise_compatibility.target_transition_map == (
        "R^{\\Phi_3}_{H+1,H,\\mathrm{cand}} = \\pi_{\\Phi_3,\\leq H}"
    )
    assert pack.bd_axioms["BD7"].bridge == "vertex_operator_yangian"
    assert_open_theorem_schema(pack.bd_axioms["BD7"])
    assert "R-matrix match" in pack.bd_axioms["BD7"].obstructions[2]
    assert pack.bd_axioms["BD7"].heightwise_compatibility.inverse_limit_conditions[1] == (
        "BD7 satisfies the source/target/kernel/image/cokernel Mittag-Leffler gate"
    )
    assert (
        "BD7 satisfies the source/target/kernel/image/cokernel Mittag-Leffler gate"
        in pack.bd_axioms["BD7"].open_obligations
    )
    assert_full_inverse_limit_gate(
        pack.bd_axioms["BD1"].heightwise_compatibility.inverse_limit_gate,
        "framed_d3_assignment",
    )
    assert_full_inverse_limit_gate(
        pack.bd_axioms["BD7"].heightwise_compatibility.inverse_limit_gate,
        "vertex_operator_yangian",
    )
    assert_bridge_requirement(
        pack.bd_axioms["BD1"].construction_requirement,
        "framed_d3_assignment",
    )
    assert_bridge_requirement(
        pack.bd_axioms["BD7"].construction_requirement,
        "vertex_operator_yangian",
    )
    assert "finite label packets are not a strict spectral R-matrix" in (
        pack.requirements["vertex_operator_yangian"].forbidden_promotions
    )


def test_bridge_axiom_pack_is_evaluable_from_witnesses():
    partial_bridge = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
        ),
    )
    assert partial_bridge.bd_axioms["BD6"].status == "OPEN_THEOREM_SCHEMA"
    assert partial_bridge.bd_axioms["BD6"].proved_here is False
    assert "cokernel transition maps are surjective" in (
        partial_bridge.bd_axioms["BD6"].open_obligations
    )

    brst_without_dependencies = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("brst_realization",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    bd6 = brst_without_dependencies.bd_axioms["BD6"]
    assert bd6.status == "OPEN_THEOREM_SCHEMA"
    assert bd6.proved_here is False
    assert "establish dependency theorem: framed_d3_assignment" in (
        bd6.dependency_obligations
    )
    assert "establish dependency theorem: compact_hall_promotion" in (
        bd6.dependency_obligations
    )
    assert bd6.open_obligations == bd6.dependency_obligations

    bar_without_dependencies = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("bkm_bar_dictionary",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    bd4 = bar_without_dependencies.bd_axioms["BD4"]
    assert bd4.status == "OPEN_THEOREM_SCHEMA"
    assert bd4.proved_here is False
    assert bd4.dependency_obligations == (
        "establish dependency theorem: framed_d3_assignment",
        "establish dependency theorem: compact_hall_promotion",
        "establish dependency theorem: scattering_root_identification",
    )
    assert bd4.open_obligations == bd4.dependency_obligations

    yangian_without_dependencies = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("vertex_operator_yangian",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    bd7 = yangian_without_dependencies.bd_axioms["BD7"]
    assert bd7.status == "OPEN_THEOREM_SCHEMA"
    assert bd7.proved_here is False
    assert bd7.dependency_obligations == (
        "establish dependency theorem: brst_realization",
        "establish dependency theorem: shadow_rademacher_comparison",
    )
    assert bd7.open_obligations == bd7.dependency_obligations

    scattering_without_inverse = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            bridge_constructions=("scattering_root_identification",),
        ),
    )
    bd3 = scattering_without_inverse.bd_axioms["BD3"]
    assert bd3.status == "OPEN_THEOREM_SCHEMA"
    assert bd3.local_obligations_satisfied is True
    assert "establish dependency theorem: compact_hall_promotion" in (
        bd3.open_obligations
    )
    assert "BD3 admits an inverse-limit lift with rank-zero transition squares" in (
        bd3.open_obligations
    )
    assert not any(
        obligation.startswith("construct the motivic integration morphism")
        for obligation in bd3.open_obligations
    )

    partial_source = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
        ),
    )
    assert partial_source.source_gate.status == "OPEN_THEOREM_SCHEMA"
    assert partial_source.source_gate.proved_here is False
    assert any(
        obligation.startswith("H_H^HB:")
        for obligation in partial_source.source_gate.open_obligations
    )

    source_without_pro_recognition = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=K3EClosureWitnesses(
            source_gate_closed=True,
            source_recognition_envelope_completed=True,
            bridge_constructions=("source_hall_borcherds_gate",),
            inverse_limit_proved_conditions=(
                k3e_closure_criterion_report(8, 5, 10)
                .inverse_limit_gate
                .required_conditions
            ),
        ),
    )
    source_gate = source_without_pro_recognition.source_gate
    assert source_gate.status == "OPEN_THEOREM_SCHEMA"
    assert source_gate.local_obligations_satisfied is True
    assert source_gate.open_obligations == source_gate.pro_recognition_gate.open_conditions
    assert not any(
        obligation.startswith("construct the oriented critical CoHA")
        for obligation in source_gate.open_obligations
    )

    default = k3e_bridge_axiom_pack(8, 5, 10)
    closed = k3e_bridge_axiom_pack(
        8,
        5,
        10,
        closure_witnesses=complete_closure_witnesses(default),
    )
    assert closed.all_entries_open is False
    assert closed.all_entries_proved is True
    assert closed.open_entries == {}
    assert closed.open_schema_obligations == ()
    assert closed.inverse_limit_status == "PROVED"
    assert closed.pro_recognition_status == "PROVED"
    assert_proved_theorem_schema(closed.source_gate)
    assert_proved_bridge_requirement(
        closed.source_gate.construction_requirement,
        "source_hall_borcherds_gate",
    )
    for entry in closed.entries:
        assert_proved_theorem_schema(entry)
        assert entry.heightwise_compatibility.inverse_limit_gate.status == "PROVED"
        assert_proved_bridge_requirement(entry.construction_requirement, entry.bridge)
    assert all(
        requirement.status == "proved"
        for requirement in closed.construction_requirements
    )
