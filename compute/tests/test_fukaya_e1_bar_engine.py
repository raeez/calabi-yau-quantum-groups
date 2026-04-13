from fractions import Fraction

from compute.lib.fukaya_e1_bar_engine import ConifoldE1Engine, conifold_s3_floer


def test_conifold_s3_floer_basics():
    floer = conifold_s3_floer()

    assert floer.rank == 2
    assert floer.poincare_duality_holds()


def test_conifold_e1_engine_bar_and_open_closed_data():
    engine = ConifoldE1Engine()
    match = engine.genus_0_open_closed_match()

    assert engine.e1_bar_dimensions(3) == {1: 2, 2: 4, 3: 8}
    assert engine.e1_bar_differential_vanishes()
    assert match["disc_count_d1"] == Fraction(1)
    assert match["disc_count_d2"] == Fraction(-1, 4)
