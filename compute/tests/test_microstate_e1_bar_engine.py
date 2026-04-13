from compute.lib.microstate_e1_bar_engine import (
    verify_conifold_spectrum,
    verify_growth_rate_hierarchy,
    verify_macmahon_three_methods,
    verify_oeis_values,
)


def test_plane_partition_counts_agree_across_three_methods():
    assert verify_macmahon_three_methods(12)["all_match"]
    assert verify_oeis_values(12)["all_match"]


def test_conifold_and_growth_hierarchy_checks():
    spectrum = verify_conifold_spectrum(12)
    growth = verify_growth_rate_hierarchy()

    assert spectrum["bps_indices_ok"]
    assert spectrum["partition_function_ok"]
    assert growth["alpha_C3"] > growth["alpha_K3E"] > growth["alpha_conifold"]
    assert growth["S_K3E"] > growth["S_C3"] > growth["S_conifold"]
