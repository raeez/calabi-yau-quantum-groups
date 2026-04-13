from compute.lib.deformed_chiral_ce_engine import (
    verify_d_CE_arity1,
    verify_d_h_nontrivial_axis,
    verify_d_h_squared_zero,
)


def test_ce_differential_vanishes_on_arity_one():
    assert verify_d_CE_arity1(k=1.0)["ok"]


def test_cy_deformation_square_zero_and_general_embedding():
    assert verify_d_h_squared_zero(k=1.0)["ok"]
    assert verify_d_h_nontrivial_axis(k=1.0)["ok"]
