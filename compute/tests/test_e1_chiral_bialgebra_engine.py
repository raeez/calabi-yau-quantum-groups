from compute.lib.e1_chiral_bialgebra_engine import (
    BialgebraCompatibilityVerifier,
    E1AlgebraVerifier,
    E1CoalgebraVerifier,
)


def test_e1_algebra_associativity_and_macmahon_grading():
    algebra = E1AlgebraVerifier(Psi=2.0, N_max=5)
    coalgebra = E1CoalgebraVerifier(Psi=2.0, N_max=5)
    grading = coalgebra.verify_macmahon_grading()

    assert algebra.verify_ordered_product_associativity()["ok"]
    assert grading["ok"]
    assert grading["grading_matches"]


def test_e1_bialgebra_virasoro_homomorphism():
    result = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5).verify_homomorphism_virasoro()

    assert result["ok"]
    assert abs(result["c_eff"] - 4.0) < 1e-12
