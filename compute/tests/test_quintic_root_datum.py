from compute.lib.quintic_root_datum import CHI, H11, gv_invariant, verify_all


def test_quintic_hodge_and_degree_one_gv_data():
    assert H11 == 1
    assert CHI == -200
    assert gv_invariant(0, 1) == 2875


def test_quintic_verification_suite():
    assert all(verify_all().values())
