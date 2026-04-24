"""Cheap verification-surface invariants for the CY3 bridge gates."""

from compute.lib.c3_hcs_hall_theta import continuity_bound_for_modes
from compute.lib.cy3_bridge_normal_form import (
    GATES,
    PROTECTED_PHYSICS_GATES,
    SEVEN_RIGIDIFICATIONS,
    TARGETS,
)


def test_bridge_targets_use_declared_gates_and_are_nested() -> None:
    ordered_targets = (
        "local_c3_to_yplus",
        "w_infty_representation",
        "global_hcs_hall",
        "hall_borcherds_bkm",
        "protected_physics",
    )

    previous = set()
    for target in ordered_targets:
        current = TARGETS[target]
        assert all(key in GATES for key in current)
        assert previous.issubset(current)
        previous = set(current)

    assert TARGETS["protected_physics"] == PROTECTED_PHYSICS_GATES


def test_seven_rigidifications_are_declared_inside_protected_package() -> None:
    protected = set(TARGETS["protected_physics"])

    assert set(SEVEN_RIGIDIFICATIONS).issubset(protected)
    assert all(GATES[key].layer for key in SEVEN_RIGIDIFICATIONS)
    assert all(GATES[key].statement for key in SEVEN_RIGIDIFICATIONS)


def test_c3_theta_continuity_bound_covers_ternary_case() -> None:
    assert continuity_bound_for_modes(()) == (0, 0, 0)
    assert continuity_bound_for_modes((0, 1, 2)) == (3, 3, 3)
