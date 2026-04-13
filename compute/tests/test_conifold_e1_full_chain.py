from compute.lib.conifold_e1_full_chain import (
    conifold_e1_full_chain,
    macmahon_leading_coeffs,
    step4b_kappa_conifold,
)


def test_conifold_kappa_resolution():
    result = step4b_kappa_conifold()

    assert result["paths_3_and_5_match"]
    assert result["matter_kappa"] == "1"
    assert result["full_super_kappa"] == "0"


def test_conifold_full_chain_summary_and_macmahon_seed():
    result = conifold_e1_full_chain(2)

    assert macmahon_leading_coeffs(6) == [1, 1, 3, 6, 13, 24]
    assert result["summary"]["ybe_satisfied"]
    assert result["summary"]["bialgebra_coassociative"]
