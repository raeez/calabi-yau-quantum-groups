from fractions import Fraction

from compute.lib.entropy_koszul_complement_cy3 import (
    verify_complementarity_consistency,
    verify_faber_pandharipande,
)


def test_faber_pandharipande_seed_values():
    checks = verify_faber_pandharipande()

    assert checks[1] == (Fraction(1, 24), Fraction(1, 24))
    assert checks[2] == (Fraction(7, 5760), Fraction(7, 5760))
    assert checks[3] == (Fraction(31, 967680), Fraction(31, 967680))


def test_complementarity_landscape_internal_consistency():
    assert all(verify_complementarity_consistency().values())
