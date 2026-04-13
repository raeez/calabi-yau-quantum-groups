from fractions import Fraction

from compute.lib.celestial_cy3_e1_engine import (
    standard_quantum_omega,
    verify_celestial_ope_c3,
    verify_cy_condition,
    verify_rmatrix_matches_ope_c3,
)


def test_standard_quantum_omega_satisfies_cy_condition():
    result = verify_cy_condition(standard_quantum_omega(Fraction(1, 10)))

    assert result["cy_condition_satisfied"]
    assert result["sigma_1"] == 0


def test_c3_ope_and_rmatrix_bridge():
    ope = verify_celestial_ope_c3(3)
    rmatrix = verify_rmatrix_matches_ope_c3()

    assert ope["all_rmatrix_poles_odd"]
    assert ope["spin_data"][3]["rmatrix_leading_pole"] == 5
    assert rmatrix["spin_1"]["matches"]
    assert rmatrix["spin_2"]["matches"]
    assert rmatrix["overall_match"]
