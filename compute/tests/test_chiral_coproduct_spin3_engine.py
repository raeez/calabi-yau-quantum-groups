from compute.lib.chiral_coproduct_spin3_engine import (
    verify_cross_term_consistency,
    verify_vacuum_annihilation,
    verify_z0_reduction,
)


def test_spin3_cross_terms_and_vacuum_checks():
    assert verify_cross_term_consistency(1.0, 4)["ok"]
    assert verify_vacuum_annihilation(1.0, 4)["ok"]


def test_spin3_z0_reduction():
    assert verify_z0_reduction(1.0, 4)["ok"]
