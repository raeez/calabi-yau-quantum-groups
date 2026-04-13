from compute.lib.chiral_coproduct_spin2_engine import (
    extract_c_eff,
    verify_heisenberg,
    verify_virasoro,
)


def test_spin2_heisenberg_and_virasoro_checks():
    virasoro = verify_virasoro()

    assert verify_heisenberg()["ok"]
    assert virasoro["ok"]
    assert virasoro["c"] == 1.0


def test_spin2_effective_central_charge_formula():
    result = extract_c_eff(2.0)

    assert result["c_eff_correct"]
    assert result["c_eff"] == 4.0
