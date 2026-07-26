from fractions import Fraction

import pytest

from compute.lib.hall_borcherds_gate import (
    ANTI_SHORTCUTS,
    DELTA5_DATUM,
    FiniteBorcherdsTargetPacketWitnesses,
    FiniteComparisonMatrixPacketWitnesses,
    FiniteMatrixDefectWitness,
    FiniteMatrixTransitionWitness,
    HallBorcherdsWitnesses,
    HeightMatrixDefectWitness,
    HeightRecognitionCertificateWitness,
    HeightRecognitionWitness,
    RecognitionEnvelopeWitnesses,
    SourceCompactDoubleGateWitnesses,
    SourceProRecognitionGateWitnesses,
    source_gate_boundary_report,
    source_gate_obstruction_taxonomy,
    source_gate_task_map,
    source_gate_obligation_matrix,
    additive_claim_status,
    all_shortcuts_rejected,
    associator_cocycle_defect_rank,
    borcherds_weight_from_c0,
    cartan_radical_defect_dimension,
    centrality_defect_rank,
    evaluate_gate,
    evaluate_finite_borcherds_target_packet,
    evaluate_finite_comparison_matrix_packet,
    evaluate_recognition_envelope,
    evaluate_source_compact_double_gate,
    evaluate_source_pro_recognition_gate,
    exact_matrix_rank,
    finite_coproduct_intertwining_gate,
    finite_source_pro_recognition_matrix_gate,
    finite_defect_vanishings,
    finite_comparison_shape_report,
    finite_recognition_certificate_report,
    finite_matrix_defect_report,
    finite_matrix_transition_report,
    heightwise_recognition_certificate_report,
    gauge_cocycle_defect_rank,
    green_identity_defect_rank,
    heightwise_matrix_defect_report,
    heightwise_recognition_report,
    imprimitive_borcherds_pt_gate,
    k3e_refined_ktheory_gate,
    k3xe_spectrum_tuple,
    ktheoretic_n46_closure_gate,
    gauge_constraint_defect_rank,
    parity_defect_rank,
    primitive_discriminant,
    primitive_root_key,
    quotient_kernel_defect_dimension,
    recognition_envelope_missing_witnesses,
    right_kernel_basis,
    resolved_comparison_matrix,
    resolved_comparison_matrices,
    pbw_hilbert_defect_rank,
    serre_inclusion_defect_rank,
    source_matrix_forces_faithfulness,
    shortcut_allowed,
    subspace_containment_defect_dimension,
    subspace_symmetric_defect_dimension,
    vector_in_row_span,
)


def _complete_recognition_witnesses() -> RecognitionEnvelopeWitnesses:
    return RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
        transition_compatible=True,
    )


def _complete_gate_witnesses() -> HallBorcherdsWitnesses:
    return HallBorcherdsWitnesses(
        oriented_critical_coha=True,
        hopf_pairing=True,
        drinfeld_double=True,
        denominator_normalization=True,
        root_multiplicity_map=True,
        k3xe_spectrum_separated=True,
        coha_positive_half_not_w=True,
        bkm_object_not_yangian=True,
    )


def _complete_compact_double_witnesses() -> SourceCompactDoubleGateWitnesses:
    return SourceCompactDoubleGateWitnesses(
        compact_ml_exactness=True,
        compact_critical_realization=True,
        compact_support_properness=True,
        double_coproduct=True,
        double_pairing=True,
        double_center=True,
    )


def _complete_pro_recognition_witnesses() -> SourceProRecognitionGateWitnesses:
    return SourceProRecognitionGateWitnesses(
        separated_completion=True,
        defect_ideal_exactness=True,
        heegner_borcherds_coefficient_comparison=True,
    )


def _complete_comparison_packet_witnesses(**overrides) -> FiniteComparisonMatrixPacketWitnesses:
    data = {
        "source_packet": True,
        "target_packet": True,
        "charge_block_bijection": True,
        "parity_block_bijection": True,
        "primitive_dimension_match": True,
        "source_quotient_bases": True,
        "target_root_bases": True,
        "comparison_matrices_supplied": True,
        "negative_half_dual_matrices_supplied": True,
        "quotient_maps_supplied": True,
        "transition_compatible": True,
        "defect_vanishing_separated": True,
    }
    data.update(overrides)
    return FiniteComparisonMatrixPacketWitnesses(**data)


def _finite_matrix_witness(**overrides) -> FiniteMatrixDefectWitness:
    data = {
        "radical_basis": ((0, 1),),
        "positive_pairing_matrix": ((1, 0), (0, 0)),
        "negative_pairing_matrix": ((1, 0), (0, 0)),
        "source_pairing_matrix": ((1, 0), (0, 1)),
        "target_pairing_matrix": ((1, 0), (0, 1)),
        "comparison_matrix": ((1, 0), (0, 1)),
        "hall_serre_kernel_basis": ((1, 0),),
        "borcherds_serre_basis": ((1, 0),),
        "hall_coproduct_matrix": ((1, 0), (0, 1)),
        "borcherds_coproduct_matrix": ((1, 0), (0, 1)),
        "primitive_center_basis": ((0, 1),),
        "allowed_center_basis": ((0, 1),),
        "hall_associator": (1, 2),
        "borcherds_associator": (1, 2),
        "gauge_coboundary_basis": (),
        "source_parity_signs": (1, -1),
        "target_parity_signs": (1, -1),
    }
    data.update(overrides)
    return FiniteMatrixDefectWitness(**data)


def test_delta5_weight_and_igusa_square_are_separated():
    assert borcherds_weight_from_c0(10) == Fraction(5)
    assert DELTA5_DATUM.kappa_BKM == Fraction(5)
    assert DELTA5_DATUM.square_weight == Fraction(10)
    assert DELTA5_DATUM.square_weight != DELTA5_DATUM.kappa_BKM


def test_k3xe_four_invariant_spectrum_is_ordered():
    assert k3xe_spectrum_tuple() == (
        Fraction(0),
        Fraction(3),
        Fraction(5),
        Fraction(24),
    )


def test_numeric_weight_does_not_close_typed_gate():
    report = evaluate_gate(HallBorcherdsWitnesses(denominator_normalization=True))
    assert report.status == "OPEN_TYPED_GATE"
    assert not report.closed
    assert report.implications["denominator_weight_verified"]
    assert "root_multiplicity_map" in report.missing_witnesses
    assert "oriented_critical_coha" in report.missing_witnesses


def test_all_witnesses_close_gate_as_implication_check():
    report = evaluate_gate(
        HallBorcherdsWitnesses(
            oriented_critical_coha=True,
            hopf_pairing=True,
            drinfeld_double=True,
            denominator_normalization=True,
            root_multiplicity_map=True,
            k3xe_spectrum_separated=True,
            coha_positive_half_not_w=True,
            bkm_object_not_yangian=True,
        )
    )
    assert report.status == "CLOSED_FROM_WITNESSES"
    assert report.closed
    assert report.missing_witnesses == ()
    assert all(report.implications.values())


def test_root_multiplicity_lane_exposes_key_not_coefficient_oracle():
    assert primitive_discriminant(1, 1, 1) == 3
    assert primitive_root_key(1, 1, 1) == 3
    with pytest.raises(ValueError, match="imprimitive"):
        primitive_root_key(2, 2, 2)


def test_imprimitive_borcherds_exponent_is_not_mobius_extracted():
    gate = imprimitive_borcherds_pt_gate(2, 2, 2)
    assert gate.charge == (2, 2, 2)
    assert gate.gcd == 2
    assert gate.discriminant == 12
    assert gate.borcherds_product_exponent == 4016
    assert gate.primitive_subcharge == (1, 1, 1)
    assert gate.primitive_subcharge_discriminant == 3
    assert gate.primitive_subcharge_exponent == -64
    assert gate.mobius_subtraction_applies_to_bkm_exponent is False


def test_imprimitive_stable_pair_and_dt_status_are_gated():
    gate = imprimitive_borcherds_pt_gate(2, 2, 2)
    assert gate.pt_multiple_cover_status == "CONDITIONAL_ON_OP_MULTIPLE_COVER_CONJECTURE"
    assert gate.dt_imprimitive_status == "CONDITIONAL_ON_IMPRIMITIVE_MOTIVIC_PT_DT_WALL_CROSSING"
    assert "Oberdieck-Pandharipande all-class reduced stable-pair multiple-cover rule" in gate.required_inputs
    assert "Behrend-weighted imprimitive PT/DT wall-crossing" in gate.required_inputs


def test_ktheoretic_n46_closure_is_conjectural_not_theorem():
    gate = ktheoretic_n46_closure_gate()
    assert gate.orders == (4, 6)
    assert set(gate.status_by_order.values()) == {
        "CONJECTURAL_NEEDS_EQUIVARIANT_K_THEORETIC_ORBIFOLD_GATE"
    }
    assert gate.euler_specialization_target == "Conjecture thm:k3e-orbifold-DT-N46"
    assert gate.euler_specialization_is_theorem is False


def test_ktheoretic_n46_rejects_untwined_source_promotion():
    gate = ktheoretic_n46_closure_gate()
    assert "untwined K3 x E" in gate.untwined_refined_source
    assert "Oberdieck 2018 refined PT/Jacobi formula" not in gate.untwined_refined_source
    assert gate.false_source_attribution_rejected is True
    missing = set(gate.missing_inputs)
    assert "g_N-linearized reduced obstruction theory on [K3 x E / Z_N]" in missing
    assert "twisted-sector K-theoretic correction from CHPV twining data" in missing
    assert "compatibility with reduced E-fibred multiplicative structure" in missing


def test_k3e_refined_ktheory_gate_rejects_false_theorem_promotion():
    gate = k3e_refined_ktheory_gate()
    assert gate.false_arxiv_2405_03418_rejected is True
    assert gate.torus_localization_available is False
    assert gate.numerical_primitive_scalar_status == "PROVED_BY_OBERDIECK_PIXTON_2018_AND_REDUCED_PT_DT"
    assert gate.all_class_scalar_status == "CONJECTURAL_IN_OBERDIECK_PANDHARIPANDE_ALL_CLASS_FORM"
    assert gate.refined_pt_status == "CONDITIONAL_ON_REFINED_REDUCED_PT_JACOBI_COMPARISON"
    assert gate.ideal_sheaf_kdt_status.startswith("CONDITIONAL_ON")
    assert gate.motivic_hodge_tate_status.startswith("CONDITIONAL_ON")
    assert gate.as_index_status.startswith("CONDITIONAL_ON")


def test_k3e_refined_ktheory_gate_names_missing_witnesses():
    missing = set(k3e_refined_ktheory_gate().missing_inputs)
    assert "K-theoretic PT/DT comparison for the reduced compact non-toric theory" in missing
    assert "motivic Igusa lift in K_0(MMHS) with Hodge-Tate character" in missing
    assert "Dirac operator construction on the twisted derived DT moduli stack" in missing
    assert "proof that the AS index series equals the reduced DT/PT partition function" in missing


def test_known_shortcuts_are_rejected():
    assert set(ANTI_SHORTCUTS) == {
        "coha_c3_is_w",
        "bkm_is_yangian",
        "phi10_weight_is_kappa_BKM",
        "additive_kappa_BKM",
        "six_phi_applications",
    }
    assert all_shortcuts_rejected()
    for shortcut in ANTI_SHORTCUTS:
        assert not shortcut_allowed(shortcut)


def test_unknown_shortcut_is_not_silently_accepted():
    with pytest.raises(KeyError):
        shortcut_allowed("unlisted_bridge")


def test_additive_kappa_bkm_match_is_not_bridge_proof():
    status = additive_claim_status(
        kappa_ch_Heis=Fraction(3),
        kappa_fiber=Fraction(2),
        kappa_BKM=Fraction(5),
        universal_claim=True,
    )
    assert status["numeric_match"]
    assert not status["accepted_as_bridge_proof"]
    assert status["reason"] == "numeric coincidence only"


def test_finite_envelope_does_not_imply_unquotiented_recognition():
    report = evaluate_recognition_envelope(
        RecognitionEnvelopeWitnesses(
            finite_compact_double=True,
            finite_borcherds_target=True,
            transition_compatible=True,
        )
    )
    assert report.status == "MISSING_SOURCE_PACKET"
    assert not report.envelope_constructed
    assert not report.completed_envelope_constructed
    assert not report.source_packet_constructed
    assert not report.source_faithfulness_forced
    assert not report.finite_unquotiented_recognized
    assert not report.completed_source_faithfulness
    assert not report.completed_unquotiented_recognized
    assert report.remaining_defects == ("R", "S", "D", "C", "A", "P")


def test_finite_borcherds_target_packet_requires_all_rows():
    report = evaluate_finite_borcherds_target_packet(
        FiniteBorcherdsTargetPacketWitnesses(
            current_quotient=True,
            root_parity_basis=True,
            invariant_form_and_cartan_radical=True,
            serre_presentation=True,
            pbw_basis=True,
            coproduct=True,
            primitive_center=True,
            associator_complex=False,
            transition_compatible=True,
        )
    )
    assert report.status == "MISSING_TARGET_PACKET_ROWS"
    assert not report.closed
    assert report.missing_witnesses == ("associator_complex",)


def test_complete_finite_borcherds_target_packet_is_not_source_faithfulness():
    target_report = evaluate_finite_borcherds_target_packet(
        FiniteBorcherdsTargetPacketWitnesses(
            current_quotient=True,
            root_parity_basis=True,
            invariant_form_and_cartan_radical=True,
            serre_presentation=True,
            pbw_basis=True,
            coproduct=True,
            primitive_center=True,
            associator_complex=True,
            transition_compatible=True,
        )
    )
    recognition_report = evaluate_recognition_envelope(
        RecognitionEnvelopeWitnesses(
            finite_compact_double=True,
            finite_borcherds_target=target_report.closed,
            transition_compatible=True,
        )
    )
    assert target_report.status == "FINITE_BORCHERDS_TARGET_PACKET"
    assert target_report.closed
    assert recognition_report.status == "MISSING_SOURCE_PACKET"
    assert not recognition_report.envelope_constructed
    assert not recognition_report.source_faithfulness_forced


def test_finite_comparison_matrix_packet_requires_basis_and_transition_rows():
    report = evaluate_finite_comparison_matrix_packet(
        FiniteComparisonMatrixPacketWitnesses(
            source_packet=True,
            target_packet=True,
            charge_block_bijection=True,
            parity_block_bijection=True,
            primitive_dimension_match=True,
            source_quotient_bases=True,
            target_root_bases=True,
            comparison_matrices_supplied=True,
            negative_half_dual_matrices_supplied=False,
            quotient_maps_supplied=True,
            transition_compatible=False,
            defect_vanishing_separated=True,
        )
    )
    assert report.status == "MISSING_COMPARISON_PACKET_ROWS"
    assert not report.closed
    assert report.missing_witnesses == (
        "negative_half_dual_matrices_supplied",
        "transition_compatible",
    )
    assert report.defect_vanishing_forced is False


def test_complete_comparison_matrix_packet_does_not_force_finite_defects():
    comparison_report = evaluate_finite_comparison_matrix_packet(
        FiniteComparisonMatrixPacketWitnesses(
            source_packet=True,
            target_packet=True,
            charge_block_bijection=True,
            parity_block_bijection=True,
            primitive_dimension_match=True,
            source_quotient_bases=True,
            target_root_bases=True,
            comparison_matrices_supplied=True,
            negative_half_dual_matrices_supplied=True,
            quotient_maps_supplied=True,
            transition_compatible=True,
            defect_vanishing_separated=True,
        )
    )
    recognition_report = evaluate_recognition_envelope(
        RecognitionEnvelopeWitnesses(
            finite_compact_double=True,
            finite_borcherds_target=True,
            compact_source_packet=comparison_report.closed,
            transition_compatible=True,
        )
    )
    assert comparison_report.status == "FINITE_COMPARISON_MATRIX_PACKET"
    assert comparison_report.closed
    assert comparison_report.defect_vanishing_forced is False
    assert recognition_report.status == "COMPLETED_RECOGNITION_ENVELOPE"
    assert recognition_report.source_packet_constructed
    assert not recognition_report.source_faithfulness_forced
    assert recognition_report.remaining_defects == ("R", "S", "D", "C", "A", "P")


def test_finite_comparison_shape_report_closes_literal_square_comparison_only():
    shape_report = finite_comparison_shape_report(_finite_matrix_witness())
    recognition_report = evaluate_recognition_envelope(
        RecognitionEnvelopeWitnesses(
            finite_compact_double=True,
            finite_borcherds_target=True,
            compact_source_packet=shape_report.closed,
            transition_compatible=True,
        )
    )
    assert shape_report.status == "FINITE_COMPARISON_SHAPE_CLOSED"
    assert shape_report.closed
    assert shape_report.remaining_components == ()
    assert shape_report.defect_vanishing_forced is False
    assert not recognition_report.source_faithfulness_forced
    assert recognition_report.remaining_defects == ("R", "S", "D", "C", "A", "P")


def test_finite_comparison_shape_report_closes_two_slot_quotient_comparison():
    witness = _finite_matrix_witness(
        positive_pairing_matrix=((0, 0), (1, 0)),
        negative_pairing_matrix=((0, 1), (0, 0)),
        source_pairing_matrix=((0, 1), (0, 0)),
        target_pairing_matrix=((1,),),
        comparison_matrix=((0, 0),),
        quotient_map=((1, 0),),
        post_quotient_comparison_matrix=((1,),),
        right_quotient_map=((0, 1),),
        right_post_quotient_comparison_matrix=((1,),),
        right_radical_basis=((1, 0),),
    )
    shape_report = finite_comparison_shape_report(witness)
    assert shape_report.closed
    assert shape_report.component_defects["left_quotient_rank"] == 0
    assert shape_report.component_defects["right_quotient_rank"] == 0
    assert shape_report.component_defects["left_post_rank"] == 0
    assert shape_report.component_defects["right_post_rank"] == 0
    assert shape_report.defect_vanishing_forced is False


def test_finite_comparison_shape_report_detects_deficient_quotient_rank():
    witness = _finite_matrix_witness(
        source_pairing_matrix=((1, 0), (0, 1)),
        target_pairing_matrix=((1, 0), (0, 1)),
        comparison_matrix=((0, 0), (0, 0)),
        quotient_map=((1, 0), (2, 0)),
        post_quotient_comparison_matrix=((1, 0), (0, 1)),
    )
    shape_report = finite_comparison_shape_report(witness)
    assert shape_report.status == "FINITE_COMPARISON_SHAPE_DEFECT"
    assert not shape_report.closed
    assert shape_report.component_defects["left_quotient_rank"] == 1
    assert shape_report.component_defects["left_rank"] == 1
    assert shape_report.component_defects["right_rank"] == 1
    assert "left_quotient_rank" in shape_report.remaining_components


def test_finite_recognition_certificate_closes_only_with_packet_shape_defects_and_transition():
    report = finite_recognition_certificate_report(
        _complete_comparison_packet_witnesses(),
        _finite_matrix_witness(),
    )
    assert report.status == "FINITE_RECOGNITION_CERTIFICATE"
    assert report.closed
    assert report.remaining_conditions == ()
    assert report.packet_report.closed
    assert report.shape_report.closed
    assert report.matrix_report is not None
    assert report.matrix_report.remaining_defects == ()
    assert report.recognition_report is not None
    assert report.recognition_report.completed_unquotiented_recognized


def test_finite_recognition_certificate_names_packet_failure_before_structural_promotion():
    report = finite_recognition_certificate_report(
        _complete_comparison_packet_witnesses(negative_half_dual_matrices_supplied=False),
        _finite_matrix_witness(),
    )
    assert report.status == "FINITE_RECOGNITION_CERTIFICATE_DEFECT"
    assert not report.closed
    assert report.remaining_conditions == ("packet:negative_half_dual_matrices_supplied",)
    assert report.matrix_report is None
    assert report.recognition_report is None


def test_finite_recognition_certificate_names_shape_failure_before_defect_check():
    report = finite_recognition_certificate_report(
        _complete_comparison_packet_witnesses(),
        _finite_matrix_witness(
            source_pairing_matrix=((1, 0), (0, 1)),
            target_pairing_matrix=((1, 0), (0, 1)),
            comparison_matrix=((0, 0), (0, 0)),
            quotient_map=((1, 0), (2, 0)),
            post_quotient_comparison_matrix=((1, 0), (0, 1)),
        ),
    )
    assert not report.closed
    assert "shape:left_quotient_rank" in report.remaining_conditions
    assert "shape:left_rank" in report.remaining_conditions
    assert report.matrix_report is None


def test_finite_recognition_certificate_names_structural_defect_after_shape_closes():
    report = finite_recognition_certificate_report(
        _complete_comparison_packet_witnesses(),
        _finite_matrix_witness(comparison_matrix=((2, 0), (0, 1))),
    )
    assert not report.closed
    assert report.shape_report.closed
    assert report.matrix_report is not None
    assert report.matrix_report.remaining_defects == ("R",)
    assert report.remaining_conditions == ("defect:R",)
    assert report.recognition_report is not None
    assert not report.recognition_report.source_faithfulness_forced


def test_heightwise_recognition_certificate_closes_with_transition_reports():
    report = heightwise_recognition_certificate_report(
        (
            HeightRecognitionCertificateWitness(
                2,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
            HeightRecognitionCertificateWitness(
                1,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
        ),
        transition_witnesses=(
            FiniteMatrixTransitionWitness(
                upper_height=2,
                lower_height=1,
                restricted_upper_witness=_finite_matrix_witness(),
                lower_witness=_finite_matrix_witness(),
            ),
        ),
    )
    assert report.status == "HEIGHTWISE_RECOGNITION_CERTIFICATE_COMPLETE"
    assert report.completed
    assert report.first_failure_height is None
    assert tuple(row.height for row in report.rows) == (1, 2)
    assert all(row.closed for row in report.rows)
    assert report.transition_reports[0].closed


def test_heightwise_recognition_certificate_names_first_structural_failure():
    report = heightwise_recognition_certificate_report(
        (
            HeightRecognitionCertificateWitness(
                1,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
            HeightRecognitionCertificateWitness(
                2,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(comparison_matrix=((2, 0), (0, 1))),
            ),
        )
    )
    assert report.status == "FIRST_CERTIFICATE_FAILURE_AT_HEIGHT"
    assert report.first_failure_height == 2
    assert report.first_failure_conditions == ("defect:R",)
    assert report.rows[1].failure_conditions == ("defect:R",)
    assert not report.completed


def test_heightwise_recognition_certificate_names_transition_component_failure():
    report = heightwise_recognition_certificate_report(
        (
            HeightRecognitionCertificateWitness(
                1,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
            HeightRecognitionCertificateWitness(
                2,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
        ),
        transition_witnesses=(
            FiniteMatrixTransitionWitness(
                upper_height=2,
                lower_height=1,
                restricted_upper_witness=_finite_matrix_witness(
                    hall_serre_kernel_basis=((1, 0),)
                ),
                lower_witness=_finite_matrix_witness(
                    hall_serre_kernel_basis=((0, 1),)
                ),
            ),
        ),
    )
    assert report.first_failure_height == 2
    assert report.first_failure_conditions == (
        "transition:hall_serre_kernel_basis",
    )
    assert report.transition_reports[0].remaining_components == (
        "hall_serre_kernel_basis",
    )
    assert not report.rows[1].closed


def test_heightwise_recognition_certificate_names_pro_envelope_exactness_failure():
    report = heightwise_recognition_certificate_report(
        (
            HeightRecognitionCertificateWitness(
                1,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
            HeightRecognitionCertificateWitness(
                2,
                _complete_comparison_packet_witnesses(),
                _finite_matrix_witness(),
            ),
        ),
        defect_ideal_transitions_commute=False,
        defect_ideal_derived_limit_vanishes=False,
    )
    assert report.status == "PRO_ENVELOPE_EXACTNESS_FAILURE"
    assert report.first_failure_height is None
    assert report.first_failure_conditions == (
        "defect_ideal_transition",
        "R1lim_defect_ideal",
    )
    assert report.pro_exactness_conditions == report.first_failure_conditions
    assert all(row.closed for row in report.rows)
    assert not report.completed


def test_all_six_defects_plus_ml_give_completed_recognition():
    witnesses = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
        transition_compatible=True,
    )
    assert all(finite_defect_vanishings(witnesses).values())
    assert source_matrix_forces_faithfulness(witnesses)
    report = evaluate_recognition_envelope(witnesses)
    assert report.status == "COMPLETED_UNQUOTIENTED_RECOGNITION"
    assert report.source_packet_constructed
    assert report.source_faithfulness_forced
    assert report.completed_source_faithfulness
    assert report.completed_unquotiented_recognized
    assert report.remaining_defects == ()


def test_source_matrix_faithfulness_without_ml_stops_before_completion():
    report = evaluate_recognition_envelope(
        RecognitionEnvelopeWitnesses(
            finite_compact_double=True,
            finite_borcherds_target=True,
            compact_source_packet=True,
            radical_isometry=True,
            serre_kernel_exact=True,
            green_adjoint_coproduct=True,
            primitive_center_reduction=True,
            associator_class_match=True,
            parity_fixture_match=True,
        )
    )
    assert report.status == "FINITE_UNQUOTIENTED_RECOGNITION"
    assert report.source_faithfulness_forced
    assert report.finite_unquotiented_recognized
    assert not report.completed_source_faithfulness
    assert not report.completed_unquotiented_recognized


def test_missing_source_matrix_row_does_not_force_faithfulness():
    witnesses = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        parity_fixture_match=True,
    )
    assert not source_matrix_forces_faithfulness(witnesses)
    report = evaluate_recognition_envelope(witnesses)
    assert report.status == "FINITE_RECOGNITION_ENVELOPE"
    assert not report.source_faithfulness_forced
    assert report.remaining_defects == ("A",)


def test_target_rows_without_compact_source_packet_do_not_force_faithfulness():
    witnesses = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
        transition_compatible=True,
    )
    assert all(finite_defect_vanishings(witnesses).values())
    assert not source_matrix_forces_faithfulness(witnesses)
    report = evaluate_recognition_envelope(witnesses)
    assert report.status == "MISSING_SOURCE_PACKET"
    assert not report.envelope_constructed
    assert not report.completed_envelope_constructed
    assert not report.source_packet_constructed
    assert not report.source_faithfulness_forced


def test_heightwise_recognition_names_first_defect_height():
    bad_serre = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=False,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
        transition_compatible=True,
    )
    report = heightwise_recognition_report(
        (
            HeightRecognitionWitness(1, _complete_recognition_witnesses()),
            HeightRecognitionWitness(2, bad_serre),
            HeightRecognitionWitness(3, _complete_recognition_witnesses()),
        )
    )
    assert report.status == "FIRST_FAILURE_AT_HEIGHT"
    assert report.first_failure_height == 2
    assert report.first_failure_modes == ("S",)
    assert report.rows[1].failure_modes == ("S",)
    assert not report.completed


def test_heightwise_recognition_records_transition_failure():
    no_transition = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
        transition_compatible=False,
    )
    report = heightwise_recognition_report(
        (
            HeightRecognitionWitness(1, _complete_recognition_witnesses()),
            HeightRecognitionWitness(2, no_transition),
        )
    )
    assert report.first_failure_height == 2
    assert report.first_failure_modes == ("transition",)
    assert report.rows[1].report.status == "FINITE_UNQUOTIENTED_RECOGNITION"
    assert not report.rows[1].closed


def test_heightwise_recognition_structural_gap_is_not_a_finite_defect():
    report = heightwise_recognition_report(
        (HeightRecognitionWitness(1, RecognitionEnvelopeWitnesses()),)
    )
    assert report.first_failure_height == 1
    assert report.first_failure_modes == (
        "finite_compact_double",
        "finite_borcherds_target",
        "compact_source_packet",
    )
    assert not {"R", "S", "D", "C", "A", "P"}.intersection(report.first_failure_modes)


def test_heightwise_recognition_completes_only_when_every_height_closes():
    report = heightwise_recognition_report(
        (
            HeightRecognitionWitness(2, _complete_recognition_witnesses()),
            HeightRecognitionWitness(1, _complete_recognition_witnesses()),
        )
    )
    assert report.status == "HEIGHTWISE_RECOGNITION_COMPLETE"
    assert report.completed
    assert report.first_failure_height is None
    assert tuple(row.height for row in report.rows) == (1, 2)
    assert all(row.closed for row in report.rows)


def test_heightwise_recognition_rejects_missing_or_ambiguous_height_data():
    with pytest.raises(ValueError, match="at least one"):
        heightwise_recognition_report(())
    with pytest.raises(ValueError, match="positive"):
        heightwise_recognition_report(
            (HeightRecognitionWitness(0, _complete_recognition_witnesses()),)
        )
    with pytest.raises(ValueError, match="duplicate"):
        heightwise_recognition_report(
            (
                HeightRecognitionWitness(1, _complete_recognition_witnesses()),
                HeightRecognitionWitness(1, _complete_recognition_witnesses()),
            )
        )


def test_exact_linear_algebra_primitives_are_rational():
    assert exact_matrix_rank(((1, 2), (2, 4))) == 1
    assert right_kernel_basis(((1, 1),)) == ((Fraction(-1), Fraction(1)),)
    assert subspace_symmetric_defect_dimension(
        ((1, 0), (0, 1)),
        ((1, 1),),
    ) == 1
    assert vector_in_row_span((2, 2), ((1, 1),))


def test_exact_linear_algebra_primitives_reject_malformed_ambient_data():
    with pytest.raises(ValueError, match="same width"):
        exact_matrix_rank(((1, 0), (1,)))
    with pytest.raises(ValueError, match="ambient dimensions"):
        vector_in_row_span((1, 0, 0), ((1, 0),))


def test_finite_matrix_defect_report_closes_all_six_defects():
    report = finite_matrix_defect_report(_finite_matrix_witness())
    assert report.radical_kernel_defect == 0
    assert report.quotient_kernel_defect == 0
    assert report.radical_isometry_defect == 0
    assert report.serre_defect == 0
    assert report.serre_inclusion_defect == 0
    assert report.pbw_hilbert_defect == 0
    assert report.coproduct_defect == 0
    assert report.green_identity_defect == 0
    assert report.center_defect == 0
    assert report.centrality_defect == 0
    assert report.cartan_radical_defect == 0
    assert report.associator_defect == 0
    assert report.parity_defect == 0
    assert report.vanished_defects == ("R", "S", "D", "C", "A", "P")
    assert report.remaining_defects == ()
    assert report.recognition_witnesses == _complete_recognition_witnesses()


def test_finite_matrix_defect_report_detects_subspace_and_associator_defects():
    report = finite_matrix_defect_report(
        _finite_matrix_witness(
            radical_basis=((1, 0),),
            hall_serre_kernel_basis=((1, 0),),
            borcherds_serre_basis=((0, 1),),
            primitive_center_basis=((1, 0),),
            allowed_center_basis=((0, 1),),
            hall_associator=(1, 0),
            borcherds_associator=(0, 0),
            gauge_coboundary_basis=((0, 1),),
        )
    )
    assert report.radical_kernel_defect == 2
    assert report.serre_defect == 2
    assert report.center_defect == 2
    assert report.associator_defect == 1
    assert report.remaining_defects == ("R", "S", "C", "A")
    assert not report.recognition_witnesses.radical_isometry
    assert not report.recognition_witnesses.serre_kernel_exact
    assert not report.recognition_witnesses.primitive_center_reduction
    assert not report.recognition_witnesses.associator_class_match


def test_finite_matrix_defect_report_requires_parity_fixture():
    witness = _finite_matrix_witness(
        source_parity_signs=None,
        target_parity_signs=None,
    )
    assert parity_defect_rank(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.parity_defect == 1
    assert report.remaining_defects == ("P",)
    assert not report.recognition_witnesses.parity_fixture_match


def test_finite_matrix_defect_report_detects_parity_mismatch():
    witness = _finite_matrix_witness(
        source_parity_signs=(1, -1),
        target_parity_signs=(-1, -1),
    )
    assert parity_defect_rank(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.parity_defect == 1
    assert report.remaining_defects == ("P",)
    assert not report.recognition_witnesses.parity_fixture_match


def test_finite_matrix_defect_report_rejects_incomplete_parity_data():
    with pytest.raises(ValueError, match="must be supplied together"):
        finite_matrix_defect_report(
            _finite_matrix_witness(target_parity_signs=None)
        )
    with pytest.raises(ValueError, match="parity signs must be"):
        finite_matrix_defect_report(
            _finite_matrix_witness(source_parity_signs=(1, 0))
        )


def test_finite_matrix_defect_report_accepts_serre_and_pbw_witnesses():
    witness = _finite_matrix_witness(
        serre_relation_matrix=((1, -1),),
        hall_bracket_evaluation_matrix=((1, 0), (1, 0)),
        borcherds_hilbert_vector=(1, 2, 3),
        hall_hilbert_vector=(1, 2, 3),
    )
    assert serre_inclusion_defect_rank(witness) == 0
    assert pbw_hilbert_defect_rank(witness) == 0
    report = finite_matrix_defect_report(witness)
    assert report.serre_inclusion_defect == 0
    assert report.pbw_hilbert_defect == 0
    assert "S" in report.vanished_defects


def test_finite_matrix_defect_report_detects_serre_inclusion_failure():
    witness = _finite_matrix_witness(
        serre_relation_matrix=((1, 0),),
        hall_bracket_evaluation_matrix=((1, 0), (0, 1)),
    )
    assert serre_inclusion_defect_rank(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.serre_defect == 0
    assert report.serre_inclusion_defect == 1
    assert "S" in report.remaining_defects


def test_finite_matrix_defect_report_accepts_centrality_and_cartan_radical_witnesses():
    witness = _finite_matrix_witness(
        centrality_matrix=((0, 0),),
        cartan_component_basis=((0, 1),),
        cartan_radical_basis=((0, 1),),
    )
    assert centrality_defect_rank(witness) == 0
    assert cartan_radical_defect_dimension(witness) == 0
    assert subspace_containment_defect_dimension(((0, 1),), ((0, 1),)) == 0
    report = finite_matrix_defect_report(witness)
    assert report.centrality_defect == 0
    assert report.cartan_radical_defect == 0
    assert "C" in report.vanished_defects


def test_finite_matrix_defect_report_detects_centrality_failure():
    witness = _finite_matrix_witness(
        centrality_matrix=((1, 0),),
    )
    assert centrality_defect_rank(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.center_defect == 0
    assert report.centrality_defect == 1
    assert "C" in report.remaining_defects


def test_finite_matrix_defect_report_detects_cartan_radical_failure():
    witness = _finite_matrix_witness(
        cartan_component_basis=((1, 0),),
        cartan_radical_basis=((0, 1),),
    )
    assert cartan_radical_defect_dimension(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.cartan_radical_defect == 1
    assert "C" in report.remaining_defects


def test_finite_matrix_defect_report_requires_complete_cartan_radical_data():
    with pytest.raises(ValueError, match="cartan_component_basis"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                cartan_component_basis=((0, 1),),
            )
        )


def test_finite_matrix_defect_report_detects_pbw_hilbert_failure():
    witness = _finite_matrix_witness(
        borcherds_hilbert_vector=(1, 2, 3),
        hall_hilbert_vector=(1, 2, 4),
    )
    assert pbw_hilbert_defect_rank(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.pbw_hilbert_defect == 1
    assert "S" in report.remaining_defects


def test_finite_matrix_defect_report_requires_complete_serre_and_pbw_data():
    with pytest.raises(ValueError, match="supplied together"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                serre_relation_matrix=((1, 0),),
            )
        )
    with pytest.raises(ValueError, match="supplied together"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                borcherds_hilbert_vector=(1, 2),
            )
        )


def test_finite_matrix_defect_report_detects_isometry_and_coproduct_mismatch():
    report = finite_matrix_defect_report(
        _finite_matrix_witness(
            comparison_matrix=((2, 0), (0, 1)),
            borcherds_coproduct_matrix=((1, 1), (0, 1)),
        )
    )
    assert report.radical_kernel_defect == 0
    assert report.radical_isometry_defect == 1
    assert report.coproduct_defect == 1
    assert report.remaining_defects == ("R", "D")
    assert not report.recognition_witnesses.radical_isometry
    assert not report.recognition_witnesses.green_adjoint_coproduct


def test_finite_matrix_defect_report_accepts_green_identity_data():
    witness = _finite_matrix_witness(
        hall_coproduct_matrix=((1, 0), (0, 1)),
        tensor_pairing_matrix=((1, 0), (0, 1)),
        negative_product_matrix=((1, 0), (0, 1)),
    )
    assert green_identity_defect_rank(witness) == 0
    report = finite_matrix_defect_report(witness)
    assert report.green_identity_defect == 0
    assert "D" in report.vanished_defects


def test_finite_matrix_defect_report_detects_green_identity_failure():
    witness = _finite_matrix_witness(
        hall_coproduct_matrix=((1, 0), (0, 1)),
        tensor_pairing_matrix=((1, 0), (0, 1)),
        negative_product_matrix=((1, 0), (0, 2)),
    )
    assert green_identity_defect_rank(witness) == 1
    report = finite_matrix_defect_report(witness)
    assert report.coproduct_defect == 0
    assert report.green_identity_defect == 1
    assert "D" in report.remaining_defects


def test_finite_matrix_defect_report_requires_complete_green_data():
    with pytest.raises(ValueError, match="supplied together"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                tensor_pairing_matrix=((1,),),
            )
        )


def test_finite_coproduct_intertwining_gate_closes_with_green_identity():
    gate = finite_coproduct_intertwining_gate(
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
        tensor_pairing_matrix=((1, 0), (0, 1)),
        source_pairing_matrix=((1, 0), (0, 1)),
        negative_product_matrix=((1, 0), (0, 1)),
    )
    assert gate.closed
    assert gate.coproduct_intertwines
    assert gate.green_adjoint
    assert gate.coproduct_defect_rank == 0
    assert gate.green_defect_rank == 0
    assert gate.status == "FINITE_COPRODUCT_INTERTWINING_GATE"


def test_finite_coproduct_intertwining_gate_detects_coproduct_defect():
    gate = finite_coproduct_intertwining_gate(
        ((1, 0), (0, 1)),
        ((1, 1), (0, 1)),
        tensor_pairing_matrix=((1, 0), (0, 1)),
        source_pairing_matrix=((1, 0), (0, 1)),
        negative_product_matrix=((1, 0), (0, 1)),
    )
    assert not gate.closed
    assert not gate.coproduct_intertwines
    assert gate.green_adjoint
    assert gate.coproduct_defect_rank == 1
    assert gate.green_defect_rank == 0
    assert gate.coproduct_difference == ((Fraction(0), Fraction(-1)), (Fraction(0), Fraction(0)))
    assert gate.status == "FINITE_COPRODUCT_INTERTWINING_DEFECT"


def test_finite_coproduct_intertwining_gate_detects_green_defect():
    gate = finite_coproduct_intertwining_gate(
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
        tensor_pairing_matrix=((1, 0), (0, 1)),
        source_pairing_matrix=((1, 0), (0, 1)),
        negative_product_matrix=((1, 0), (0, 2)),
    )
    assert not gate.closed
    assert gate.coproduct_intertwines
    assert not gate.green_adjoint
    assert gate.coproduct_defect_rank == 0
    assert gate.green_defect_rank == 1
    assert gate.green_difference == ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(-1)))
    assert gate.status == "FINITE_COPRODUCT_INTERTWINING_DEFECT"


def test_finite_coproduct_intertwining_gate_requires_green_data_for_closure():
    gate = finite_coproduct_intertwining_gate(
        ((1, 0), (0, 1)),
        ((1, 0), (0, 1)),
    )
    assert gate.coproduct_intertwines
    assert not gate.green_data_supplied
    assert not gate.green_adjoint
    assert not gate.closed
    assert gate.status == "FINITE_COPRODUCT_GREEN_DATA_MISSING"
    with pytest.raises(ValueError, match="supplied together"):
        finite_coproduct_intertwining_gate(
            ((1, 0), (0, 1)),
            ((1, 0), (0, 1)),
            tensor_pairing_matrix=((1, 0), (0, 1)),
        )


def test_finite_coproduct_intertwining_gate_rejects_shape_defects():
    with pytest.raises(ValueError, match="matrix dimensions must agree"):
        finite_coproduct_intertwining_gate(
            ((1, 0),),
            ((1, 0), (0, 1)),
            tensor_pairing_matrix=((1, 0), (0, 1)),
            source_pairing_matrix=((1, 0), (0, 1)),
            negative_product_matrix=((1, 0), (0, 1)),
        )
    with pytest.raises(ValueError, match="matrix dimensions do not compose"):
        finite_coproduct_intertwining_gate(
            ((1, 0), (0, 1)),
            ((1, 0), (0, 1)),
            tensor_pairing_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            source_pairing_matrix=((1, 0), (0, 1)),
            negative_product_matrix=((1, 0), (0, 1)),
        )


def test_finite_matrix_defect_report_accepts_literal_quotient_comparison():
    witness = _finite_matrix_witness(
        source_pairing_matrix=((1, 0), (0, 0)),
        target_pairing_matrix=((1,),),
        comparison_matrix=((0, 0),),
        quotient_map=((1, 0),),
        post_quotient_comparison_matrix=((1,),),
        source_parity_signs=(1, -1),
        target_parity_signs=(1,),
    )
    assert resolved_comparison_matrix(witness) == ((Fraction(1), Fraction(0)),)
    assert quotient_kernel_defect_dimension(witness) == 0
    report = finite_matrix_defect_report(witness)
    assert report.quotient_kernel_defect == 0
    assert report.radical_isometry_defect == 0
    assert "R" in report.vanished_defects


def test_finite_matrix_defect_report_rejects_wrong_quotient_kernel():
    witness = _finite_matrix_witness(
        source_pairing_matrix=((1, 0), (0, 0)),
        target_pairing_matrix=((1,),),
        comparison_matrix=((0, 0),),
        quotient_map=((0, 1),),
        post_quotient_comparison_matrix=((1,),),
        source_parity_signs=(1, -1),
        target_parity_signs=(1,),
    )
    assert quotient_kernel_defect_dimension(witness) == 2
    report = finite_matrix_defect_report(witness)
    assert report.quotient_kernel_defect == 2
    assert "R" in report.remaining_defects


def test_finite_matrix_defect_report_accepts_two_slot_quotient_comparison():
    witness = _finite_matrix_witness(
        positive_pairing_matrix=((0, 0), (1, 0)),
        negative_pairing_matrix=((0, 1), (0, 0)),
        source_pairing_matrix=((0, 1), (0, 0)),
        target_pairing_matrix=((1,),),
        comparison_matrix=((0, 0),),
        quotient_map=((1, 0),),
        post_quotient_comparison_matrix=((1,),),
        right_quotient_map=((0, 1),),
        right_post_quotient_comparison_matrix=((1,),),
        right_radical_basis=((1, 0),),
        source_parity_signs=(1, -1),
        target_parity_signs=(1,),
    )
    assert resolved_comparison_matrices(witness) == (
        ((Fraction(1), Fraction(0)),),
        ((Fraction(0), Fraction(1)),),
    )
    report = finite_matrix_defect_report(witness)
    assert report.quotient_kernel_defect == 0
    assert report.radical_isometry_defect == 0
    assert "R" in report.vanished_defects


def test_finite_matrix_defect_report_default_symmetric_comparison_does_not_fake_two_slot_pairing():
    report = finite_matrix_defect_report(
        _finite_matrix_witness(
            source_pairing_matrix=((0, 1), (0, 0)),
            target_pairing_matrix=((1,),),
            comparison_matrix=((1, 0),),
            source_parity_signs=(1, -1),
            target_parity_signs=(1,),
        )
    )
    assert report.radical_isometry_defect == 1
    assert "R" in report.remaining_defects


def test_finite_matrix_defect_report_rejects_wrong_composed_comparison():
    report = finite_matrix_defect_report(
        _finite_matrix_witness(
            source_pairing_matrix=((1, 0), (0, 0)),
            target_pairing_matrix=((1,),),
            comparison_matrix=((0, 0),),
            source_parity_signs=(1, -1),
            target_parity_signs=(1,),
        )
    )
    assert report.radical_isometry_defect == 1
    assert "R" in report.remaining_defects


def test_finite_matrix_defect_report_requires_complete_quotient_data():
    with pytest.raises(ValueError, match="supplied together"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                quotient_map=((1, 0),),
            )
        )
    with pytest.raises(ValueError, match="supplied together"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                right_quotient_map=((0, 1),),
            )
        )


def test_finite_matrix_defect_report_requires_matching_associator_lengths():
    with pytest.raises(ValueError, match="associator cochains"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                hall_associator=(1, 2, 3),
                borcherds_associator=(1, 2),
            )
        )


def test_finite_matrix_defect_report_requires_associator_complex_widths():
    with pytest.raises(ValueError, match="gauge coboundary"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                hall_associator=(1, 0),
                borcherds_associator=(0, 0),
                gauge_coboundary_basis=((1, 0, 0),),
            )
        )
    with pytest.raises(ValueError, match="cocycle matrix"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                hall_associator=(1, 0),
                borcherds_associator=(0, 0),
                associator_cocycle_matrix=((1, 0, 0),),
            )
        )
    with pytest.raises(ValueError, match="constraint matrix"):
        finite_matrix_defect_report(
            _finite_matrix_witness(
                hall_associator=(1, 0),
                borcherds_associator=(0, 0),
                gauge_constraint_matrix=((1, 0, 0),),
            )
        )


def test_finite_matrix_defect_report_accepts_associator_cocycle_and_gauge_constraints():
    witness = _finite_matrix_witness(
        hall_associator=(1, 1),
        borcherds_associator=(2, 2),
        gauge_coboundary_basis=((1, 1),),
        associator_cocycle_matrix=((1, -1),),
        gauge_constraint_matrix=((1, -1),),
    )
    assert associator_cocycle_defect_rank(witness) == 0
    assert gauge_cocycle_defect_rank(witness) == 0
    assert gauge_constraint_defect_rank(witness) == 0
    report = finite_matrix_defect_report(witness)
    assert report.associator_defect == 0
    assert report.associator_cocycle_defect == 0
    assert report.gauge_cocycle_defect == 0
    assert report.gauge_constraint_defect == 0
    assert "A" in report.vanished_defects


def test_finite_matrix_defect_report_detects_associator_cocycle_failure():
    witness = _finite_matrix_witness(
        hall_associator=(1, 0),
        borcherds_associator=(0, 0),
        gauge_coboundary_basis=((1, 0),),
        associator_cocycle_matrix=((1, 0),),
    )
    report = finite_matrix_defect_report(witness)
    assert report.associator_defect == 0
    assert report.associator_cocycle_defect == 1
    assert "A" in report.remaining_defects


def test_finite_matrix_defect_report_detects_gauge_row_not_a_cocycle():
    witness = _finite_matrix_witness(
        hall_associator=(0, 0),
        borcherds_associator=(0, 0),
        gauge_coboundary_basis=((1, 0),),
        associator_cocycle_matrix=((1, 0),),
    )
    report = finite_matrix_defect_report(witness)
    assert report.associator_defect == 0
    assert report.associator_cocycle_defect == 0
    assert report.gauge_cocycle_defect == 1
    assert "A" in report.remaining_defects


def test_finite_matrix_defect_report_detects_gauge_constraint_failure():
    witness = _finite_matrix_witness(
        hall_associator=(1, 0),
        borcherds_associator=(0, 0),
        gauge_coboundary_basis=((1, 0),),
        gauge_constraint_matrix=((1, 0),),
    )
    report = finite_matrix_defect_report(witness)
    assert report.associator_defect == 0
    assert report.gauge_constraint_defect == 1
    assert "A" in report.remaining_defects


def test_heightwise_matrix_defect_report_names_first_matrix_failure():
    report = heightwise_matrix_defect_report(
        (
            HeightMatrixDefectWitness(1, _finite_matrix_witness()),
            HeightMatrixDefectWitness(
                2,
                _finite_matrix_witness(
                    hall_serre_kernel_basis=((1, 0),),
                    borcherds_serre_basis=((0, 1),),
                ),
            ),
            HeightMatrixDefectWitness(3, _finite_matrix_witness()),
        )
    )
    assert report.recognition_report.first_failure_height == 2
    assert report.recognition_report.first_failure_modes == ("S",)
    assert report.matrix_rows[1].matrix_report.serre_defect == 2
    assert report.matrix_rows[1].recognition_row.failure_modes == ("S",)


def test_finite_matrix_transition_report_closes_equal_restricted_data():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(),
            lower_witness=_finite_matrix_witness(),
        )
    )
    assert transition.closed
    assert transition.remaining_components == ()
    assert all(defect == 0 for defect in transition.component_defects.values())


def test_finite_matrix_transition_report_names_component_failure():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(
                hall_serre_kernel_basis=((1, 0),)
            ),
            lower_witness=_finite_matrix_witness(
                hall_serre_kernel_basis=((0, 1),)
            ),
        )
    )
    assert not transition.closed
    assert transition.component_defects["hall_serre_kernel_basis"] == 2
    assert transition.remaining_components == ("hall_serre_kernel_basis",)


def test_finite_matrix_transition_report_checks_right_comparison():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(
                right_comparison_matrix=((0, 1),)
            ),
            lower_witness=_finite_matrix_witness(
                right_comparison_matrix=((1, 0),)
            ),
        )
    )
    assert not transition.closed
    assert transition.component_defects["right_comparison_matrix"] == 1
    assert transition.remaining_components == ("right_comparison_matrix",)


def test_finite_matrix_transition_report_checks_serre_and_hilbert_data():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(
                serre_relation_matrix=((1, 0),),
                hall_bracket_evaluation_matrix=((1, 0),),
                borcherds_hilbert_vector=(1, 2),
                hall_hilbert_vector=(1, 2),
            ),
            lower_witness=_finite_matrix_witness(
                serre_relation_matrix=((1, 0),),
                hall_bracket_evaluation_matrix=((0, 1),),
                borcherds_hilbert_vector=(1, 3),
                hall_hilbert_vector=(1, 2),
            ),
        )
    )
    assert not transition.closed
    assert transition.component_defects["hall_bracket_evaluation_matrix"] == 1
    assert transition.component_defects["borcherds_hilbert_vector"] == 1
    assert "hall_bracket_evaluation_matrix" in transition.remaining_components
    assert "borcherds_hilbert_vector" in transition.remaining_components


def test_finite_matrix_transition_report_checks_center_data():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(
                centrality_matrix=((1, 0),),
                cartan_component_basis=((0, 1),),
                cartan_radical_basis=((0, 1),),
            ),
            lower_witness=_finite_matrix_witness(
                centrality_matrix=((0, 1),),
                cartan_component_basis=((1, 0),),
                cartan_radical_basis=((0, 1),),
            ),
        )
    )
    assert not transition.closed
    assert transition.component_defects["centrality_matrix"] == 1
    assert transition.component_defects["cartan_component_basis"] == 2
    assert "centrality_matrix" in transition.remaining_components
    assert "cartan_component_basis" in transition.remaining_components


def test_finite_matrix_transition_report_checks_associator_cohomology_data():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(
                associator_cocycle_matrix=((1, 0),),
                gauge_constraint_matrix=((0, 1),),
            ),
            lower_witness=_finite_matrix_witness(
                associator_cocycle_matrix=((0, 1),),
                gauge_constraint_matrix=((1, 0),),
            ),
        )
    )
    assert not transition.closed
    assert transition.component_defects["associator_cocycle_matrix"] == 1
    assert transition.component_defects["gauge_constraint_matrix"] == 1
    assert "associator_cocycle_matrix" in transition.remaining_components
    assert "gauge_constraint_matrix" in transition.remaining_components


def test_finite_matrix_transition_report_checks_green_data():
    transition = finite_matrix_transition_report(
        FiniteMatrixTransitionWitness(
            upper_height=2,
            lower_height=1,
            restricted_upper_witness=_finite_matrix_witness(
                tensor_pairing_matrix=((1,),),
                negative_product_matrix=((1,),),
            ),
            lower_witness=_finite_matrix_witness(
                tensor_pairing_matrix=((1,),),
                negative_product_matrix=((2,),),
            ),
        )
    )
    assert not transition.closed
    assert transition.component_defects["negative_product_matrix"] == 1
    assert transition.remaining_components == ("negative_product_matrix",)


def test_heightwise_matrix_defect_report_propagates_transition_failure():
    report = heightwise_matrix_defect_report(
        (
            HeightMatrixDefectWitness(2, _finite_matrix_witness(transition_compatible=False)),
            HeightMatrixDefectWitness(1, _finite_matrix_witness()),
        )
    )
    assert tuple(row.height for row in report.matrix_rows) == (1, 2)
    assert report.recognition_report.first_failure_height == 2
    assert report.recognition_report.first_failure_modes == ("transition",)
    assert report.matrix_rows[1].matrix_report.remaining_defects == ()
    assert not report.matrix_rows[1].recognition_row.closed


def test_heightwise_matrix_defect_report_propagates_exact_transition_report():
    report = heightwise_matrix_defect_report(
        (
            HeightMatrixDefectWitness(1, _finite_matrix_witness()),
            HeightMatrixDefectWitness(2, _finite_matrix_witness()),
        ),
        transition_witnesses=(
            FiniteMatrixTransitionWitness(
                upper_height=2,
                lower_height=1,
                restricted_upper_witness=_finite_matrix_witness(
                    hall_serre_kernel_basis=((1, 0),)
                ),
                lower_witness=_finite_matrix_witness(
                    hall_serre_kernel_basis=((0, 1),)
                ),
            ),
        ),
    )
    assert report.transition_reports[0].remaining_components == (
        "hall_serre_kernel_basis",
    )
    assert report.recognition_report.first_failure_height == 2
    assert report.recognition_report.first_failure_modes == ("transition",)


def test_heightwise_matrix_defect_report_uses_height_validation():
    with pytest.raises(ValueError, match="duplicate"):
        heightwise_matrix_defect_report(
            (
                HeightMatrixDefectWitness(1, _finite_matrix_witness()),
                HeightMatrixDefectWitness(1, _finite_matrix_witness()),
            )
        )
    with pytest.raises(ValueError, match="larger height"):
        heightwise_matrix_defect_report(
            (
                HeightMatrixDefectWitness(1, _finite_matrix_witness()),
                HeightMatrixDefectWitness(2, _finite_matrix_witness()),
            ),
            transition_witnesses=(
                FiniteMatrixTransitionWitness(
                    upper_height=1,
                    lower_height=2,
                    restricted_upper_witness=_finite_matrix_witness(),
                    lower_witness=_finite_matrix_witness(),
                ),
            ),
        )
    with pytest.raises(ValueError, match="among matrix witnesses"):
        heightwise_matrix_defect_report(
            (HeightMatrixDefectWitness(1, _finite_matrix_witness()),),
            transition_witnesses=(
                FiniteMatrixTransitionWitness(
                    upper_height=2,
                    lower_height=1,
                    restricted_upper_witness=_finite_matrix_witness(),
                    lower_witness=_finite_matrix_witness(),
                ),
            ),
        )


def test_source_gate_obligation_matrix_is_explicit():
    matrix = source_gate_obligation_matrix()
    assert matrix.summary.startswith("source gate and recognition envelope are explicit")
    assert matrix.gate.target == "Hall-Drinfeld double / BKM denominator gate"
    assert "oriented_critical_coha" in matrix.gate.missing
    assert matrix.envelope.target == "finite recognition envelope / pro-completion"
    assert "finite_compact_double" in matrix.envelope.missing
    assert "finite_borcherds_target" in matrix.envelope.missing
    assert "compact_source_packet" in matrix.envelope.missing
    assert "R" in matrix.envelope.missing
    assert "transition_compatible" in matrix.envelope.missing


def test_recognition_envelope_missing_witnesses_include_structure_and_transition():
    defects_only_vanished = RecognitionEnvelopeWitnesses(
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
    )
    assert recognition_envelope_missing_witnesses(defects_only_vanished) == (
        "finite_compact_double",
        "finite_borcherds_target",
        "compact_source_packet",
        "transition_compatible",
    )
    defects_only_matrix = source_gate_obligation_matrix(
        envelope_witnesses=defects_only_vanished
    )
    assert defects_only_matrix.envelope.missing == (
        "finite_compact_double",
        "finite_borcherds_target",
        "compact_source_packet",
        "transition_compatible",
    )

    finite_without_transition = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
    )
    assert recognition_envelope_missing_witnesses(finite_without_transition) == (
        "transition_compatible",
    )
    finite_matrix = source_gate_obligation_matrix(
        envelope_witnesses=finite_without_transition
    )
    assert finite_matrix.envelope.status == "finite"
    assert finite_matrix.envelope.missing == ("transition_compatible",)


def test_source_gate_task_map_is_explicit():
    task_map = source_gate_task_map()
    assert task_map.summary.startswith("the source task map separates")
    assert task_map.tasks["source_hall_borcherds_gate"].tasks[0].startswith(
        "construct the oriented critical CoHA"
    )
    assert "faithful recognition" in task_map.tasks["source_recognition_envelope"].tasks[1]


def test_source_gate_obstruction_taxonomy_is_explicit():
    taxonomy = source_gate_obstruction_taxonomy()
    assert taxonomy.summary.startswith("compact Hall promotion first requires")
    assert tuple(cls.code for cls in taxonomy.compact_passage) == (
        "o_ML",
        "o_real",
        "o_cpt",
    )
    assert tuple(cls.code for cls in taxonomy.double_data) == (
        "o_Delta",
        "o_pair",
        "o_cent",
    )
    assert tuple(cls.code for cls in taxonomy.finite_recognition) == (
        "R",
        "S",
        "D",
        "C",
        "A",
        "P",
    )
    assert tuple(cls.code for cls in taxonomy.pro_recognition) == (
        "Q_H_sep",
        "L_H_ex",
        "H_H_HB",
    )
    assert taxonomy.by_code["o_ML"].required_vanishing == "o_ML = 0"
    assert taxonomy.by_code["o_pair"].tex == r"o_{\mathrm{pair}}"
    assert "gauge cocycle" in taxonomy.by_code["A"].meaning
    assert "admissible-gauge" in taxonomy.by_code["A"].meaning
    assert "parity" in taxonomy.by_code["P"].meaning
    assert taxonomy.by_code["Q_H_sep"].tex == r"Q_H^{\mathrm{sep}}"
    assert taxonomy.by_code["L_H_ex"].layer == "pro_recognition"
    assert "Heegner" in taxonomy.by_code["H_H_HB"].meaning
    assert taxonomy.compact_double_required_vanishings == (
        "o_ML = 0",
        "o_real = 0",
        "o_cpt = 0",
        "o_Delta = 0",
        "o_pair = 0",
        "o_cent = 0",
    )
    assert taxonomy.pro_required_vanishings == (
        "Q_H^sep = 0",
        "L_H^ex = 0",
        "H_H^HB = 0",
    )


def test_source_compact_double_gate_evaluator_is_explicit():
    default = evaluate_source_compact_double_gate(SourceCompactDoubleGateWitnesses())
    assert default.closed is False
    assert default.status == "SOURCE_COMPACT_DOUBLE_GATES_OPEN"
    assert default.missing_witnesses == (
        "compact_ml_exactness",
        "compact_critical_realization",
        "compact_support_properness",
        "double_coproduct",
        "double_pairing",
        "double_center",
    )
    assert default.remaining_defects == (
        "o_ML = 0",
        "o_real = 0",
        "o_cpt = 0",
        "o_Delta = 0",
        "o_pair = 0",
        "o_cent = 0",
    )

    partial = evaluate_source_compact_double_gate(
        SourceCompactDoubleGateWitnesses(
            compact_ml_exactness=True,
            compact_critical_realization=True,
            double_pairing=True,
        )
    )
    assert partial.closed is False
    assert partial.missing_witnesses == (
        "compact_support_properness",
        "double_coproduct",
        "double_center",
    )
    assert partial.remaining_defects == (
        "o_cpt = 0",
        "o_Delta = 0",
        "o_cent = 0",
    )

    closed = evaluate_source_compact_double_gate(
        SourceCompactDoubleGateWitnesses(
            compact_ml_exactness=True,
            compact_critical_realization=True,
            compact_support_properness=True,
            double_coproduct=True,
            double_pairing=True,
            double_center=True,
        )
    )
    assert closed.closed is True
    assert closed.status == "SOURCE_COMPACT_DOUBLE_GATES_CLOSED"
    assert closed.missing_witnesses == ()
    assert closed.remaining_defects == ()


def test_source_pro_recognition_gate_evaluator_is_explicit():
    default = evaluate_source_pro_recognition_gate(SourceProRecognitionGateWitnesses())
    assert default.closed is False
    assert default.status == "SOURCE_PRO_RECOGNITION_GATES_OPEN"
    assert default.missing_witnesses == (
        "separated_completion",
        "defect_ideal_exactness",
        "heegner_borcherds_coefficient_comparison",
    )
    assert default.remaining_defects == (
        "Q_H^sep = 0",
        "L_H^ex = 0",
        "H_H^HB = 0",
    )

    partial = evaluate_source_pro_recognition_gate(
        SourceProRecognitionGateWitnesses(
            separated_completion=True,
            defect_ideal_exactness=True,
        )
    )
    assert partial.closed is False
    assert partial.missing_witnesses == (
        "heegner_borcherds_coefficient_comparison",
    )
    assert partial.remaining_defects == ("H_H^HB = 0",)

    closed = evaluate_source_pro_recognition_gate(
        SourceProRecognitionGateWitnesses(
            separated_completion=True,
            defect_ideal_exactness=True,
            heegner_borcherds_coefficient_comparison=True,
        )
    )
    assert closed.closed is True
    assert closed.status == "SOURCE_PRO_RECOGNITION_GATES_CLOSED"
    assert closed.missing_witnesses == ()
    assert closed.remaining_defects == ()


def _source_pro_recognition_matrix_gate_kwargs(**overrides):
    data = {
        "completion_transition_matrix": ((1, 0), (0, 1)),
        "separation_defect_matrix": ((0,),),
        "defect_ideal_transition_matrix": ((1, 0),),
        "defect_ideal_landing_defect_matrix": ((0,),),
        "heegner_coefficient_matrix": ((1, 10, -64),),
        "borcherds_coefficient_matrix": ((1, 10, -64),),
    }
    data.update(overrides)
    return data


def test_finite_source_pro_recognition_matrix_gate_closes():
    gate = finite_source_pro_recognition_matrix_gate(
        **_source_pro_recognition_matrix_gate_kwargs()
    )
    assert gate.status == "FINITE_SOURCE_PRO_RECOGNITION_MATRIX_GATE"
    assert gate.closed is True
    assert gate.lower_completion_dimension == 2
    assert gate.completion_transition_rank == 2
    assert gate.separated_completion is True
    assert gate.lower_defect_ideal_dimension == 1
    assert gate.defect_ideal_transition_rank == 1
    assert gate.defect_ideal_exact is True
    assert gate.heegner_borcherds_coefficients_match is True
    assert gate.coefficient_defect_matrix == ((Fraction(0), Fraction(0), Fraction(0)),)


def test_finite_source_pro_recognition_matrix_gate_detects_completion_defect():
    rank_defect = finite_source_pro_recognition_matrix_gate(
        **_source_pro_recognition_matrix_gate_kwargs(
            completion_transition_matrix=((1, 0), (0, 0)),
        )
    )
    assert rank_defect.closed is False
    assert rank_defect.separated_completion is False
    assert rank_defect.completion_transition_rank == 1

    separation_defect = finite_source_pro_recognition_matrix_gate(
        **_source_pro_recognition_matrix_gate_kwargs(
            separation_defect_matrix=((1,),),
        )
    )
    assert separation_defect.closed is False
    assert separation_defect.separated_completion is False
    assert separation_defect.separation_defect_rank == 1


def test_finite_source_pro_recognition_matrix_gate_detects_ideal_defect():
    gate = finite_source_pro_recognition_matrix_gate(
        **_source_pro_recognition_matrix_gate_kwargs(
            defect_ideal_transition_matrix=((0, 0),),
            defect_ideal_landing_defect_matrix=((1,),),
        )
    )
    assert gate.closed is False
    assert gate.defect_ideal_exact is False
    assert gate.defect_ideal_transition_rank == 0
    assert gate.defect_ideal_landing_defect_rank == 1


def test_finite_source_pro_recognition_matrix_gate_detects_coefficient_defect():
    gate = finite_source_pro_recognition_matrix_gate(
        **_source_pro_recognition_matrix_gate_kwargs(
            borcherds_coefficient_matrix=((1, 10, -63),),
        )
    )
    assert gate.closed is False
    assert gate.heegner_borcherds_coefficients_match is False
    assert gate.coefficient_defect_matrix == ((Fraction(0), Fraction(0), Fraction(-1)),)
    assert gate.coefficient_defect_rank == 1


def test_finite_source_pro_recognition_matrix_gate_rejects_shape_defects():
    with pytest.raises(ValueError, match="matrix dimensions"):
        finite_source_pro_recognition_matrix_gate(
            **_source_pro_recognition_matrix_gate_kwargs(
                borcherds_coefficient_matrix=((1, 10),),
            )
        )
    with pytest.raises(ValueError, match="same width"):
        finite_source_pro_recognition_matrix_gate(
            **_source_pro_recognition_matrix_gate_kwargs(
                completion_transition_matrix=((1, 0), (0,)),
            )
        )


def test_source_gate_boundary_report_is_explicit():
    boundary = source_gate_boundary_report()
    assert boundary.summary.startswith("the source boundary is the union")
    assert boundary.required_conditions[0] == "oriented_critical_coha"
    assert "finite_compact_double" in boundary.required_conditions
    assert "finite_borcherds_target" in boundary.required_conditions
    assert "compact_source_packet" in boundary.required_conditions
    assert "transition_compatible" in boundary.required_conditions
    assert boundary.obstruction_taxonomy.by_code["o_cpt"].layer == "compact_passage"
    assert "o_ML = 0" in boundary.required_conditions
    assert "o_cent = 0" in boundary.required_conditions
    assert boundary.compact_double_report.status == "SOURCE_COMPACT_DOUBLE_GATES_OPEN"
    assert boundary.compact_double_report.remaining_defects == (
        "o_ML = 0",
        "o_real = 0",
        "o_cpt = 0",
        "o_Delta = 0",
        "o_pair = 0",
        "o_cent = 0",
    )
    assert "Q_H^sep = 0" in boundary.required_conditions
    assert "L_H^ex = 0" in boundary.required_conditions
    assert "H_H^HB = 0" in boundary.required_conditions
    assert boundary.pro_recognition_report.status == "SOURCE_PRO_RECOGNITION_GATES_OPEN"
    assert boundary.pro_recognition_report.remaining_defects == (
        "Q_H^sep = 0",
        "L_H^ex = 0",
        "H_H^HB = 0",
    )
    assert any(
        "source-recognition completeness" in task
        for task in boundary.task_map.tasks["source_hall_borcherds_gate"].tasks
    )
    assert not boundary.closed

    partial = source_gate_boundary_report(
        SourceProRecognitionGateWitnesses(
            separated_completion=True,
            defect_ideal_exactness=True,
        )
    )
    assert "Q_H^sep = 0" not in partial.required_conditions
    assert "L_H^ex = 0" not in partial.required_conditions
    assert "H_H^HB = 0" in partial.required_conditions
    assert partial.pro_recognition_report.remaining_defects == ("H_H^HB = 0",)

    compact_partial = source_gate_boundary_report(
        compact_double_witnesses=SourceCompactDoubleGateWitnesses(
            compact_ml_exactness=True,
            compact_critical_realization=True,
            double_pairing=True,
        )
    )
    assert "o_ML = 0" not in compact_partial.required_conditions
    assert "o_real = 0" not in compact_partial.required_conditions
    assert "o_pair = 0" not in compact_partial.required_conditions
    assert "o_cpt = 0" in compact_partial.required_conditions
    assert "o_Delta = 0" in compact_partial.required_conditions
    assert "o_cent = 0" in compact_partial.required_conditions
    assert compact_partial.compact_double_report.remaining_defects == (
        "o_cpt = 0",
        "o_Delta = 0",
        "o_cent = 0",
    )


def test_source_gate_boundary_report_closes_only_with_all_witness_layers():
    partial = source_gate_boundary_report(
        gate_witnesses=_complete_gate_witnesses(),
        envelope_witnesses=_complete_recognition_witnesses(),
    )
    assert partial.obligation_matrix.gate.status == "closed"
    assert partial.obligation_matrix.envelope.status == "completed"
    assert partial.closed is False
    assert "construct the oriented critical CoHA with negative half, Cartan, Hopf pairing, and coproduct" not in (
        partial.required_conditions
    )
    assert "construct the finite recognition envelope from compact source packets and finite targets" not in (
        partial.required_conditions
    )
    assert "o_ML = 0" in partial.required_conditions
    assert "Q_H^sep = 0" in partial.required_conditions

    closed = source_gate_boundary_report(
        gate_witnesses=_complete_gate_witnesses(),
        envelope_witnesses=_complete_recognition_witnesses(),
        compact_double_witnesses=_complete_compact_double_witnesses(),
        pro_recognition_witnesses=_complete_pro_recognition_witnesses(),
    )
    assert closed.closed is True
    assert closed.required_conditions == ()
    assert closed.obligation_matrix.gate.missing == ()
    assert closed.obligation_matrix.envelope.missing == ()
    assert closed.compact_double_report.closed is True
    assert closed.pro_recognition_report.closed is True
