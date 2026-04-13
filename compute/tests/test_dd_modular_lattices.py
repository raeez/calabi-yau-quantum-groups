import numpy as np

from compute.lib.dd_modular_lattices import (
    gram_lambda_21_II,
    verify_gram_II_from_ambient,
    verify_null_elements,
    verify_weyl_vector,
)


def test_type_ii_gram_matrix_matches_ambient_computation():
    assert np.array_equal(verify_gram_II_from_ambient(), gram_lambda_21_II())


def test_weyl_vector_and_null_boundary_elements():
    assert verify_weyl_vector()
    assert verify_null_elements()
