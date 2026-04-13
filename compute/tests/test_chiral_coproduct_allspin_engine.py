from compute.lib.chiral_coproduct_allspin_engine import (
    verify_cross_term_table,
    verify_structural_predictions,
)


def test_allspin_structural_predictions_hold():
    result = verify_structural_predictions()

    assert result["ok"]
    assert result["spins_checked"][0] == 2


def test_allspin_cross_term_table_is_consistent():
    result = verify_cross_term_table()

    assert result["ok"]
    assert 10 in result["spins_checked"]
