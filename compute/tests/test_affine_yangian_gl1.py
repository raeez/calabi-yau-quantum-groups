from sympy import Rational

from compute.lib.affine_yangian_gl1 import (
    structure_function_coefficients,
    verify_antisymmetry_parity,
    verify_cy_condition_on_phi,
    verify_g_inversion,
)


def test_structure_function_seed_values():
    phi = structure_function_coefficients(Rational(1), Rational(2), max_order=4)
    assert phi[0] == 1
    assert phi[1] == 0
    assert phi[3] == 12


def test_basic_affine_yangian_identities():
    cy = verify_cy_condition_on_phi(Rational(1), Rational(2), max_order=8)
    inversion = verify_g_inversion(Rational(1), Rational(2), max_order=8)
    parity = verify_antisymmetry_parity(Rational(1), Rational(2), max_order=8)

    assert cy["phi_1_zero"]
    assert cy["phi_2_zero"]
    assert cy["phi_3_check"]
    assert inversion["all_pass"]
    assert all(parity["parity_checks"].values())
