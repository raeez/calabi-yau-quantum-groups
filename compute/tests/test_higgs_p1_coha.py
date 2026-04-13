from compute.lib.higgs_p1_coha import (
    two_colored_partition_function,
    verify_coha_yangian_match,
)


def test_two_colored_partition_seed_values():
    coeffs = two_colored_partition_function(6)

    assert [int(coeffs[n]) for n in range(6)] == [1, 2, 5, 10, 20, 36]


def test_higgs_coha_matches_yangian_counts():
    result = verify_coha_yangian_match(12)

    assert result["hilb_chi_equals_yangian"]
    assert result["yangian_equals_2colored"]
    assert result["oeis_a000712_match"]
