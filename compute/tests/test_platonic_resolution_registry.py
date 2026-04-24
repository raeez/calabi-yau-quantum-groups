"""Structural tests for the eight-object resolution package."""

from fractions import Fraction

from compute.lib.platonic_resolution_registry import (
    CONJECTURAL,
    CONDITIONAL,
    OBLIGATIONS,
    all_frontier_data_nonempty,
    depends_transitively,
    igusa_dictionary,
    kappa_bkm_delta5,
    missing_dependencies,
    obligation_order,
    unsafe_frontier_claims,
)


def test_eight_obligations_are_registered_in_user_order():
    assert obligation_order() == (
        "hall_cosheaf",
        "theta_hcs_hall",
        "autborch",
        "hall_bkm",
        "hall_drinfeld_double",
        "wall_descent",
        "validation",
        "igusa_propagation",
    )


def test_dependencies_are_closed():
    assert missing_dependencies() == {}


def test_frontier_objects_are_not_marked_proved():
    assert unsafe_frontier_claims() == ()
    assert OBLIGATIONS["hall_cosheaf"].status == CONDITIONAL
    assert OBLIGATIONS["theta_hcs_hall"].status == CONDITIONAL
    assert OBLIGATIONS["hall_drinfeld_double"].status == CONJECTURAL


def test_double_depends_on_positive_half_and_bkm_comparison():
    assert depends_transitively("hall_drinfeld_double", "hall_cosheaf")
    assert depends_transitively("hall_drinfeld_double", "hall_bkm")


def test_wall_descent_depends_on_hall_cosheaf():
    assert depends_transitively("wall_descent", "hall_cosheaf")


def test_all_obligations_have_frontier_or_validation_data():
    assert all_frontier_data_nonempty()


def test_igusa_dictionary_locks_normalization():
    dictionary = igusa_dictionary()
    assert dictionary["degree_map"] == "alpha(n,l,m)=2n f2 - l f3 + 2m f_-2"
    assert dictionary["orientation"] == "epsilon_o = nu_Delta5"
    assert dictionary["denominator"] == "den(g_Delta5)=64^-1 Delta5(2Z)"
    assert dictionary["scalar_square"] == "Z_square = C_square Delta5^-2"
    assert kappa_bkm_delta5() == Fraction(5)
