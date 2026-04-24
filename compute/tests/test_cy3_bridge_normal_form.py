"""Tests for the CY3 bridge normal-form gates."""

import pytest

from compute.lib.cy3_bridge_normal_form import (
    BridgeShortcutError,
    BridgeStrength,
    SEVEN_RIGIDIFICATIONS,
    c3_local_datum,
    k3e_global_datum,
    monotone_strength_chain,
    validate_typed_path,
)


def test_c3_without_hcs_hall_map_is_normal_form_only():
    datum = c3_local_datum()
    missing = tuple(gate.key for gate in datum.missing_for("local_c3_to_yplus"))

    assert missing == ("hcs_hall_chart_map",)
    assert not datum.closes("local_c3_to_yplus")
    assert datum.strength() == BridgeStrength.NORMAL_FORM_ONLY


def test_c3_with_chart_map_closes_only_the_local_yplus_bridge():
    datum = c3_local_datum(supply_hcs_hall_map=True)

    assert datum.closes("local_c3_to_yplus")
    assert datum.closes("w_infty_representation")
    assert not datum.closes("global_hcs_hall")
    assert datum.strength() == BridgeStrength.LOCAL_C3_TO_YPLUS


def test_direct_coha_to_w_infty_shortcut_is_forbidden():
    with pytest.raises(BridgeShortcutError):
        validate_typed_path(("CoHA", "W_1_infty"))


def test_typed_coha_to_w_infty_path_factors_through_double():
    edges = validate_typed_path(("CoHA", "Y_plus", "Drinfeld_double", "W_1_infty"))

    assert edges == (
        ("CoHA", "Y_plus"),
        ("Y_plus", "Drinfeld_double"),
        ("Drinfeld_double", "W_1_infty"),
    )


def test_k3e_global_bridge_requires_dwr_descent():
    datum = k3e_global_datum(supply_hcs_hall_map=True)
    missing = tuple(gate.key for gate in datum.missing_for("global_hcs_hall"))

    assert missing == (
        "dwr_cover",
        "mc_descent",
        "orientation",
        "grading_tate",
        "thom_sebastiani",
        "factorization_descent",
    )
    assert datum.strength() == BridgeStrength.LOCAL_C3_TO_YPLUS


def test_bkm_claim_requires_hall_borcherds_data_after_global_bridge():
    datum = k3e_global_datum(
        supply_hcs_hall_map=True,
        supply_dwr_descent=True,
    )
    missing = tuple(gate.key for gate in datum.missing_for("hall_borcherds_bkm"))

    assert missing == (
        "hall_borcherds_bialgebra",
        "borcherds_denominator_normalization",
    )
    assert datum.strength() == BridgeStrength.GLOBAL_HCS_HALL


def test_protected_physics_requires_the_last_functor_gate():
    datum = k3e_global_datum(
        supply_hcs_hall_map=True,
        supply_dwr_descent=True,
        supply_hall_borcherds=True,
    )

    assert tuple(g.key for g in datum.missing_for("protected_physics")) == (
        "protected_bps_functor",
    )
    assert datum.strength() == BridgeStrength.HALL_BORCHERDS_BKM


def test_complete_package_reaches_protected_physics_strength():
    datum = k3e_global_datum(
        supply_hcs_hall_map=True,
        supply_dwr_descent=True,
        supply_hall_borcherds=True,
        supply_protected_physics=True,
    )

    assert datum.closes("protected_physics")
    assert datum.strength() == BridgeStrength.PROTECTED_PHYSICS


def test_seven_rigidifications_are_distinct_and_ordered():
    assert len(SEVEN_RIGIDIFICATIONS) == 7
    assert len(set(SEVEN_RIGIDIFICATIONS)) == 7
    assert SEVEN_RIGIDIFICATIONS == (
        "qme",
        "ordered_e3_bar",
        "stage1_formality",
        "hcs_hall_chart_map",
        "hall_borcherds_bialgebra",
        "protected_bps_functor",
        "factorization_descent",
    )


def test_adding_gates_is_monotone_in_bridge_strength():
    chain = (
        c3_local_datum(),
        c3_local_datum(supply_hcs_hall_map=True),
        k3e_global_datum(
            supply_hcs_hall_map=True,
            supply_dwr_descent=True,
        ),
        k3e_global_datum(
            supply_hcs_hall_map=True,
            supply_dwr_descent=True,
            supply_hall_borcherds=True,
        ),
        k3e_global_datum(
            supply_hcs_hall_map=True,
            supply_dwr_descent=True,
            supply_hall_borcherds=True,
            supply_protected_physics=True,
        ),
    )

    assert monotone_strength_chain(chain) == (
        BridgeStrength.NORMAL_FORM_ONLY,
        BridgeStrength.LOCAL_C3_TO_YPLUS,
        BridgeStrength.GLOBAL_HCS_HALL,
        BridgeStrength.HALL_BORCHERDS_BKM,
        BridgeStrength.PROTECTED_PHYSICS,
    )
