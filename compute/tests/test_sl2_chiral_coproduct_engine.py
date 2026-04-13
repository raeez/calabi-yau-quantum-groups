from fractions import Fraction

from compute.lib.sl2_chiral_coproduct_engine import StructureFunction, gl1_vs_sl2_comparison


def test_matrix_structure_function_still_satisfies_inversion():
    result = StructureFunction().verify_inversion(Fraction(3))

    assert result["is_one"]


def test_sl2_adds_genuine_cross_node_noncommutativity():
    comparison = gl1_vs_sl2_comparison(Fraction(3))

    assert comparison["shuffle_product"]["non_commutative"]
    assert comparison["affine_relations"]["all_relations_hold"]
    assert comparison["r_matrix"]["inversion"] == "R^{00} * R^{01} = 1"
