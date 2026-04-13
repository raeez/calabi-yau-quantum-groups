from compute.lib.chiral_coproduct_universal_engine import (
    compute_spin456_tables,
    verify_against_spin2,
    verify_against_spin3,
    verify_structural_consistency,
)


def test_universal_engine_matches_low_spin_engines():
    assert verify_against_spin2()["ok"]
    assert verify_against_spin3()["ok"]


def test_universal_engine_spin456_tables_have_expected_shape():
    tables = compute_spin456_tables()

    assert verify_structural_consistency()["ok"]
    assert tables[4]["z_degree"] == 3
    assert tables[5]["cross_at_z0"] == 4
    assert tables[6]["terms_per_z_power"][5] == 1
