from __future__ import annotations

import pytest

from compute.lib.cy3_dwr_descent_gate import (
    REQUIRED_DESCENT_GATES,
    DescentGateState,
    Gate,
    complete_descent_state,
)


def state(*gates: Gate) -> DescentGateState:
    return DescentGateState(frozenset(gates))


def test_complete_gate_passes_descent() -> None:
    package = complete_descent_state()

    assert package.has_descent()
    assert package.missing_descent_gates() == frozenset()
    assert package.report()["missing_descent_gates"] == ()


@pytest.mark.parametrize("missing_gate", sorted(REQUIRED_DESCENT_GATES, key=lambda g: g.value))
def test_each_descent_gate_is_independent(missing_gate: Gate) -> None:
    package = DescentGateState(REQUIRED_DESCENT_GATES - {missing_gate})

    assert not package.has_descent()
    assert package.missing_descent_gates() == frozenset({missing_gate})


def test_fixed_c3_chart_does_not_imply_descent() -> None:
    package = state(Gate.FIXED_C3_CHART, Gate.SV_POSITIVE_HALF)

    assert not package.has_descent()
    assert Gate.FULL_RENORMALISED_CHART_MAPS in package.missing_descent_gates()
    assert Gate.MAPS_ON_ALL_SIMPLICES in package.missing_descent_gates()
    assert any("o_theta^{fp,+}" in reason for reason in package.shortcut_reasons())


def test_vertex_maps_without_all_simplices_do_not_descend() -> None:
    package = DescentGateState(
        REQUIRED_DESCENT_GATES
        - {
            Gate.MAPS_ON_ALL_SIMPLICES,
            Gate.CECH_MC_ZERO,
        }
    )

    assert not package.has_descent()
    assert package.missing_descent_gates() == frozenset(
        {
            Gate.MAPS_ON_ALL_SIMPLICES,
            Gate.CECH_MC_ZERO,
        }
    )


def test_hall_side_orientation_is_not_relative_orientation() -> None:
    package = DescentGateState(
        (REQUIRED_DESCENT_GATES - {Gate.RELATIVE_ORIENTATION_COCYCLE_ZERO})
        | {Gate.HALL_SIDE_ORIENTATION_TRIVIAL}
    )

    assert not package.has_descent()
    assert Gate.RELATIVE_ORIENTATION_COCYCLE_ZERO in package.missing_descent_gates()
    assert any("relative comparison orientation" in reason for reason in package.shortcut_reasons())


def test_hall_side_ts_is_not_comparison_ts() -> None:
    package = DescentGateState(
        (REQUIRED_DESCENT_GATES - {Gate.THOM_SEBASTIANI_COHERENT})
        | {Gate.HALL_SIDE_TS_ASSOCIATIVE}
    )

    assert not package.has_descent()
    assert Gate.THOM_SEBASTIANI_COHERENT in package.missing_descent_gates()
    assert any("comparison TS coherence" in reason for reason in package.shortcut_reasons())


def test_positive_half_does_not_give_direct_w_shortcut() -> None:
    package = state(Gate.SV_POSITIVE_HALF)

    assert not package.has_descent()
    assert not package.has_w_shadow_route()
    assert package.has_direct_w_shortcut()
    assert any("direct CoHA(C3)->W shortcut" in reason for reason in package.shortcut_reasons())


def test_w_shadow_route_is_typed_but_not_descent() -> None:
    package = state(Gate.SV_POSITIVE_HALF, Gate.DRINFELD_DOUBLE_FOCK)

    assert package.has_w_shadow_route()
    assert not package.has_descent()
    assert Gate.DWR_GOOD_COVER in package.missing_descent_gates()


def test_string_gate_inputs_are_normalized() -> None:
    package = DescentGateState.from_iterable(g.value for g in REQUIRED_DESCENT_GATES)

    assert package == complete_descent_state()
