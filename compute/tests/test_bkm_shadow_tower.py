from fractions import Fraction

from compute.lib.bkm_shadow_tower import WEYL_VECTOR, get_f, verify_weyl_vector


def test_weyl_vector_and_phi01_seed_coefficients():
    assert WEYL_VECTOR == (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    assert verify_weyl_vector()
    assert get_f(0, 1) == 1
    assert get_f(0, 0) == 10
