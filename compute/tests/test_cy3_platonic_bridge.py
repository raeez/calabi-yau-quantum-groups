from fractions import Fraction

from compute.lib.cy3_platonic_bridge import (
    CHL_C0,
    CHL_KAPPA_BKM,
    FRONTIER_REQUEST_ORDER,
    GRITSENKO_CLERY_ATLAS,
    GLOBAL_WITNESS_REQUIREMENTS,
    NORMAL_FORM,
    OBSTRUCTION_ORDER,
    PHI3_KERNEL_COMPONENTS,
    PROVED_ALGEBRAIC,
    STRICTIFICATION_ORDER,
    all_phi3_kernel_cases_close,
    analytic_global_primitive_closure,
    anomaly_free_hcs_package,
    compact_nonformal_strictification_witness,
    complete_k3e_bridge_package,
    construct_oriented_dwr_ran_map,
    formal_global_primitive_closure,
    frontier_realisation_package,
    global_witness_attack_index,
    global_witness_attack_ledger,
    hcs_two_loop_counterterm_witness,
    invalid_global_shortcuts_blocked,
    k3e_hall_borcherds_bialgebra_datum,
    phi3_casewise_kernel_witnesses,
    protected_k3e_physics_functor,
    pure_mathematical_holographic_functor,
    quintic_curved_witness,
    remaining_analytic_global_obligations,
    supplied_witnesses_close_global_gate,
    universal_formal_primitive_system,
    universal_global_primitive_envelope,
)


def test_oriented_dwr_ran_map_is_defined_simplex_by_simplex():
    dwr = construct_oriented_dwr_ran_map(("U0", "U1", "U2"))

    assert dwr.expected_simplex_count() == 7
    assert dwr.is_defined_on_full_nerve()
    assert set(dwr.nullhomotopies) == set(OBSTRUCTION_ORDER)


def test_oriented_dwr_ran_obstruction_tuple_has_nullhomotopies():
    dwr = construct_oriented_dwr_ran_map(("U0", "U1", "U2"))

    assert dwr.obstruction_tuple_vanishes()
    assert dwr.obstruction_tuple() == {name: Fraction(0) for name in OBSTRUCTION_ORDER}


def test_nonformal_strictification_witness_has_zero_obstruction_tuple():
    witness = compact_nonformal_strictification_witness(m3_rank=2)

    assert witness.is_nonformal()
    assert set(witness.primitives) == set(STRICTIFICATION_ORDER)
    assert witness.obstruction_tuple_vanishes()


def test_phi3_casewise_kernel_witnesses_cover_four_requested_cases():
    witnesses = phi3_casewise_kernel_witnesses()

    assert tuple(w.case for w in witnesses) == (
        "HMS/SYZ",
        "flop",
        "McKay",
        "wall_crossing",
    )
    assert all_phi3_kernel_cases_close()
    assert all(set(w.components) == set(PHI3_KERNEL_COMPONENTS) for w in witnesses)


def test_quintic_curved_witness_absorbs_yukawa_five():
    witness = quintic_curved_witness()

    assert witness.yukawa == 5
    assert witness.absorbs_yukawa()
    assert witness.closes()


def test_all_scale_hcs_package_has_rg_semigroup_and_qme():
    hcs = anomaly_free_hcs_package()

    assert hcs.rg_semigroup_holds()
    assert hcs.qme_holds_at_all_scales()
    assert hcs.anomaly_cancelled()
    assert hcs.propagator(Fraction(1, 4), Fraction(1)) == Fraction(9, 20)


def test_k3e_hall_borcherds_bialgebra_has_chl_weights():
    datum = k3e_hall_borcherds_bialgebra_datum()

    assert datum.compatible()
    assert datum.finite_witness_compatible()
    assert not datum.global_completion_compatible()
    assert datum.denominator_weights == CHL_KAPPA_BKM
    assert {n: datum.c0(n) for n in CHL_KAPPA_BKM} == CHL_C0
    assert datum.c0(1) == 10
    assert datum.c0(6) == 2


def test_gritsenko_clery_atlas_is_distinct_from_chl_ladder():
    weights = tuple(entry.weight for entry in GRITSENKO_CLERY_ATLAS)
    constants = tuple(entry.c0 for entry in GRITSENKO_CLERY_ATLAS)

    assert constants == (
        Fraction(10),
        Fraction(4),
        Fraction(6),
        Fraction(2),
        Fraction(4),
        Fraction(1),
        Fraction(3),
        Fraction(2),
    )
    assert weights == (
        Fraction(5),
        Fraction(2),
        Fraction(3),
        Fraction(1),
        Fraction(2),
        Fraction(1, 2),
        Fraction(3, 2),
        Fraction(1),
    )
    assert Fraction(0) not in weights
    assert Fraction(1, 4) not in weights


def test_protected_physics_functor_preserves_index_and_wall_crossing():
    functor = protected_k3e_physics_functor()

    assert functor.preserves_index()
    assert functor.preserves_wall_crossing()
    assert functor.cardy_leading_log("gamma12") == 2


def test_pure_mathematical_holographic_functor_is_product_orientation_coherent():
    functor = pure_mathematical_holographic_functor()

    assert functor.product_coherent
    assert functor.orientation_coherent
    assert functor.compatible()


def test_two_loop_counterterm_witness_uses_yang_normalisation():
    witness = hcs_two_loop_counterterm_witness()

    assert witness.coefficient == Fraction(506, 3)
    assert witness.legacy_obstruction_nonzero
    assert witness.repaired_obstruction_zero
    assert witness.closes()


def test_complete_k3e_bridge_package_is_exact():
    package = complete_k3e_bridge_package()

    assert package.is_exact()
    assert package.dwr_map.is_defined_on_full_nerve()
    assert package.hall_borcherds.compatible()


def test_frontier_realisation_package_closes_all_requested_gates():
    package = frontier_realisation_package()
    status = package.gate_status()

    assert tuple(status) == FRONTIER_REQUEST_ORDER
    assert status == {
        "Phi3_casewise_kernels": True,
        "CY_C_double_assembly": True,
        "oriented_hCS_Hall_DWR_Ran": True,
        "quintic_curved_witness": True,
        "Hall_Drinfeld_Super_Yangian_BKM": True,
        "pure_mathematical_holography": True,
        "hCS_two_loop_counterterm": True,
    }
    assert package.all_requested_gates_close()


def test_frontier_realisation_separates_normal_form_from_global_theorem():
    package = frontier_realisation_package()

    normal = package.normal_form_status()
    assert tuple(normal) == FRONTIER_REQUEST_ORDER
    assert normal["hCS_two_loop_counterterm"] == PROVED_ALGEBRAIC
    assert all(
        normal[key] == NORMAL_FORM
        for key in FRONTIER_REQUEST_ORDER
        if key != "hCS_two_loop_counterterm"
    )
    assert package.global_witness_requirements() == GLOBAL_WITNESS_REQUIREMENTS
    assert package.unconditional_global_theorem_claims() == ()
    assert package.all_requested_global_theorems_close() is False


def test_global_witness_attack_ledger_covers_all_seven_promotions():
    attacks = global_witness_attack_ledger()

    assert tuple(attack.gate for attack in attacks) == FRONTIER_REQUEST_ORDER
    assert len(attacks) == 7
    assert all(attack.normal_form_closes for attack in attacks)
    assert all(attack.requires_global_witness() for attack in attacks)
    assert invalid_global_shortcuts_blocked()


def test_global_witness_attacks_name_controlling_complexes_and_first_obstructions():
    attacks = global_witness_attack_index()

    assert "witnessed-kernel deformation" in attacks["Phi3_casewise_kernels"].controlling_complex
    assert "pairing-radical" in attacks["CY_C_double_assembly"].first_obstruction
    assert "Maurer-Cartan" in attacks["oriented_hCS_Hall_DWR_Ran"].first_obstruction
    assert "Y_3=5" in attacks["quintic_curved_witness"].first_obstruction
    assert "PBW mismatch" in attacks["Hall_Drinfeld_Super_Yangian_BKM"].first_obstruction
    assert "dynamical R-matrix" in attacks["Hall_Drinfeld_Super_Yangian_BKM"].healed_datum
    assert "product, orientation" in attacks["pure_mathematical_holography"].first_obstruction
    assert "Drinfeld-centre half-braidings" in attacks["pure_mathematical_holography"].healed_datum
    assert "Feynman/RG" in attacks["hCS_two_loop_counterterm"].first_obstruction


def test_global_gate_closes_only_when_all_required_witnesses_are_supplied():
    requirements = GLOBAL_WITNESS_REQUIREMENTS["Hall_Drinfeld_Super_Yangian_BKM"]

    assert supplied_witnesses_close_global_gate(
        "Hall_Drinfeld_Super_Yangian_BKM",
        requirements[:-1],
    ) is False
    assert supplied_witnesses_close_global_gate(
        "Hall_Drinfeld_Super_Yangian_BKM",
        requirements,
    )


def test_hdyb_and_holography_require_extra_coherence_from_swarm_attack():
    assert "associator and dynamical R-matrix coherence" in GLOBAL_WITNESS_REQUIREMENTS[
        "Hall_Drinfeld_Super_Yangian_BKM"
    ]
    assert "coproduct and Drinfeld-centre half-braiding coherence" in GLOBAL_WITNESS_REQUIREMENTS[
        "pure_mathematical_holography"
    ]


def test_universal_primitive_envelope_formally_closes_all_seven_gates():
    envelope = universal_global_primitive_envelope()

    assert tuple(system.gate for system in envelope) == FRONTIER_REQUEST_ORDER
    assert all(system.supplies_exactly_required_obligations() for system in envelope)
    assert all(system.formally_closes() for system in envelope)
    assert formal_global_primitive_closure()


def test_universal_primitive_envelope_does_not_fake_analytic_realisation():
    envelope = universal_global_primitive_envelope()

    assert all(not system.analytically_realised() for system in envelope)
    assert analytic_global_primitive_closure() is False
    assert remaining_analytic_global_obligations() == GLOBAL_WITNESS_REQUIREMENTS


def test_single_gate_primitive_system_records_each_required_boundary():
    system = universal_formal_primitive_system("oriented_hCS_Hall_DWR_Ran")

    assert system.required_obligations() == GLOBAL_WITNESS_REQUIREMENTS["oriented_hCS_Hall_DWR_Ran"]
    assert system.completion_compatible
    assert system.orientation_compatible
    assert all(certificate.formally_kills_obstruction() for certificate in system.certificates)
    assert tuple(c.primitive_name for c in system.certificates) == (
        "h_oriented_hCS_Hall_DWR_Ran_1",
        "h_oriented_hCS_Hall_DWR_Ran_2",
    )
