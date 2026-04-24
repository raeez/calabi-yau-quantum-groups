from compute.lib.bps_positive_remaining_gates import (
    HCS_HALL_LOCALIZATION_COORDINATES,
    K3E_HALL_BORCHERDS_RADICAL_COORDINATES,
    QUINTIC_EXCERT_COORDINATES,
    REMAINING_POINT_GATES,
    RemainingPointWitnesses,
    SCHOEN_BANANA_GLUING_COORDINATES,
    THETA_COMPARISON_COORDINATES,
    THETA_PACKAGE_COORDINATES,
    complete_remaining_point_witnesses,
    evaluate_coordinate_gate,
    evaluate_remaining_point_gates,
    evaluate_theta_package_gate,
    theta_package_required_coordinates,
    unresolved_point_gates,
)
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    derived_solution_stack_factors,
)


def test_remaining_point_gates_are_the_five_closed_substacks():
    assert tuple(REMAINING_POINT_GATES) == (
        "quintic_excert",
        "schoen_banana_gluing",
        "k3e_raw_radical",
        "theta_comparison",
        "hcs_named_zero_fiber",
    )
    assert len(QUINTIC_EXCERT_COORDINATES) == 13
    assert len(SCHOEN_BANANA_GLUING_COORDINATES) == 9
    assert "beck_chevalley" in SCHOEN_BANANA_GLUING_COORDINATES
    assert "compact_support_BC" not in SCHOEN_BANANA_GLUING_COORDINATES
    assert len(K3E_HALL_BORCHERDS_RADICAL_COORDINATES) == 7
    assert len(THETA_COMPARISON_COORDINATES) == 8
    assert "package_existence" in THETA_COMPARISON_COORDINATES
    assert "broken_line_package" not in THETA_COMPARISON_COORDINATES
    assert len(HCS_HALL_LOCALIZATION_COORDINATES) == 14
    assert "o_or_rel" in HCS_HALL_LOCALIZATION_COORDINATES
    assert "o_or" not in HCS_HALL_LOCALIZATION_COORDINATES


def test_empty_witnesses_leave_all_point_gates_open():
    reports = evaluate_remaining_point_gates(RemainingPointWitnesses())

    assert all(not report.closed for report in reports)
    assert {report.status for report in reports} == {"OPEN_COORDINATE_GATE"}
    assert unresolved_point_gates(RemainingPointWitnesses()) == tuple(REMAINING_POINT_GATES)


def test_unknown_coordinate_does_not_close_gate():
    report = evaluate_coordinate_gate(
        "quintic_excert",
        QUINTIC_EXCERT_COORDINATES,
        (*QUINTIC_EXCERT_COORDINATES, "ambient_torus_rank_positive"),
    )

    assert not report.closed
    assert report.missing_coordinates == ()
    assert report.unknown_coordinates == ("ambient_torus_rank_positive",)


def test_complete_formal_witnesses_close_all_gates():
    witnesses = complete_remaining_point_witnesses()
    reports = evaluate_remaining_point_gates(witnesses)

    assert all(report.closed for report in reports)
    assert {report.status for report in reports} == {"CLOSED_FROM_COORDINATES"}
    assert unresolved_point_gates(witnesses) == ()


def test_theta_package_gate_requires_package_and_comparison_data():
    broken_line_required = theta_package_required_coordinates("broken_line")
    report = evaluate_theta_package_gate("broken_line", THETA_PACKAGE_COORDINATES["broken_line"])

    assert broken_line_required == (
        THETA_PACKAGE_COORDINATES["broken_line"] + THETA_COMPARISON_COORDINATES
    )
    assert not report.closed
    assert report.missing_coordinates == THETA_COMPARISON_COORDINATES


def test_solution_stack_factors_use_remaining_gate_coordinate_lists():
    factors = {
        factor.name: factor
        for factor in derived_solution_stack_factors(TruncationBound(4, 4))
    }

    assert factors["quintic_excert"].obstruction.names == QUINTIC_EXCERT_COORDINATES
    assert factors["schoen_banana_gluing"].obstruction.names == SCHOEN_BANANA_GLUING_COORDINATES
    assert factors["k3e_raw_radical"].obstruction.names == K3E_HALL_BORCHERDS_RADICAL_COORDINATES
    assert factors["theta_comparison"].obstruction.names == THETA_COMPARISON_COORDINATES
    assert factors["hcs_named_zero_fiber"].obstruction.names == HCS_HALL_LOCALIZATION_COORDINATES
    assert all(
        not factors[name].obstruction.computed
        for name in REMAINING_POINT_GATES
    )
