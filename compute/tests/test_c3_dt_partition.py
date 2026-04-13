from compute.lib.c3_dt_partition import (
    plane_partition_counts,
    verify_macmahon_two_methods,
    verify_yangian_coha_dimensions,
)


def test_plane_partition_seed_values():
    assert plane_partition_counts(6) == [1, 1, 3, 6, 13, 24]


def test_macmahon_and_yangian_cross_checks():
    yangian = verify_yangian_coha_dimensions(15)

    assert verify_macmahon_two_methods(15)["match"]
    assert yangian["dimensions_match_pp_counts"]
    assert yangian["character_equals_macmahon"]
