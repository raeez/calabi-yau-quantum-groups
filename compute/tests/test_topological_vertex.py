from compute.lib.topological_vertex import C3_partition_function, LOCAL_P2_GV_GENUS0


def test_c3_partition_function_matches_macmahon_seed():
    assert C3_partition_function(6)[:7] == [1, 1, 3, 6, 13, 24, 48]


def test_local_p2_genus0_gv_seed_values():
    assert LOCAL_P2_GV_GENUS0[1] == 3
    assert LOCAL_P2_GV_GENUS0[2] == -6
    assert LOCAL_P2_GV_GENUS0[3] == 27
    assert LOCAL_P2_GV_GENUS0[4] == -192
