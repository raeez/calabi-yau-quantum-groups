from compute.lib.coassociativity_spin3_engine import (
    verify_coassociativity_spin1,
    verify_coassociativity_spin2_via_psi,
)


def test_spin1_primitive_coassociativity():
    result = verify_coassociativity_spin1(1.0, 4, 0, 0.3, 0.5)

    assert result["ok"]


def test_spin2_psi_level_coassociativity():
    result = verify_coassociativity_spin2_via_psi(1.0, 4, 0, 0.3, 0.5)

    assert result["ok"]
