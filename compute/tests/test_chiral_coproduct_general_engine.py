from compute.lib.chiral_coproduct_general_engine import (
    verify_reproduces_spin2,
    verify_structural_predictions,
)


def test_general_engine_reproduces_spin2():
    result = verify_reproduces_spin2(1.0, 4, 0.3 + 0.2j)

    assert result["ok"]


def test_general_engine_structural_predictions_hold():
    result = verify_structural_predictions()

    assert result["ok"]
    assert 19 in result["spins_checked"]
