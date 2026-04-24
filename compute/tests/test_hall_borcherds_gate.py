from fractions import Fraction

import pytest

from compute.lib.hall_borcherds_gate import (
    ANTI_SHORTCUTS,
    DELTA5_DATUM,
    HallBorcherdsWitnesses,
    additive_claim_status,
    all_shortcuts_rejected,
    borcherds_weight_from_c0,
    evaluate_gate,
    k3xe_spectrum_tuple,
    primitive_discriminant,
    primitive_root_key,
    shortcut_allowed,
)


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
