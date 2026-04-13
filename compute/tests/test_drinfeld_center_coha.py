from sympy import Rational

from compute.lib.drinfeld_center_coha import (
    character_identity_check,
    verify_structure_function_inversion,
)


def test_structure_function_inversion_identity():
    assert verify_structure_function_inversion(Rational(1), Rational(2))["is_one"]


def test_drinfeld_center_character_identity():
    result = character_identity_check(12)

    assert result["all_match"]
    assert result["first_discrepancy"] is None
