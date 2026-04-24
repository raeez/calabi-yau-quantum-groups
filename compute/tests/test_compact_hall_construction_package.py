from fractions import Fraction

from compute.lib.compact_hall_construction_package import (
    AUTBORCH_DOMAIN_CONDITIONS,
    DOUBLE_REQUIRED_DATA,
    compact_double_data_missing,
    compact_double_ready,
    construction_has_chart_level_cosheaf,
    construction_has_full_nerve_theta,
    constructible_gates,
    cosheaf_structure_maps,
    duplicate_obstruction_names,
    finite_first_wall_data,
    finite_first_wall_statement,
    gate_order,
    igusa_boundary_normalization,
    kappa_bkm_delta5,
    missing_gate_dependencies,
    theta_full_nerve_equations,
    unsafe_unconditional_frontier_gates,
)


def test_gate_dependency_graph_is_closed():
    assert missing_gate_dependencies() == {}


def test_gate_order_keeps_double_after_positive_half_and_bkm():
    order = gate_order()
    assert order.index("compact_hall_cosheaf") < order.index("hall_bkm_comparison")
    assert order.index("hall_bkm_comparison") < order.index("compact_drinfeld_double")


def test_frontier_gates_are_not_unconditional():
    assert unsafe_unconditional_frontier_gates() == ()


def test_constructible_gates_respect_prerequisites():
    supplied = frozenset({"compact_hall_cosheaf", "autborch_functor"})
    constructible = constructible_gates(supplied)
    assert "hall_bkm_comparison" in constructible
    assert "compact_drinfeld_double" not in constructible


def test_double_requires_all_six_double_data():
    partial = frozenset({"negative half", "Cartan completion"})
    missing = compact_double_data_missing(partial)
    assert "continuous Hopf pairing" in missing
    assert "center compatibility" in missing
    assert not compact_double_ready(partial)
    assert compact_double_ready(DOUBLE_REQUIRED_DATA)


def test_igusa_boundary_normalization_and_kappa():
    normalization = igusa_boundary_normalization()
    assert normalization["autborch"] == "AutBorch(phi_0,1)=Delta5"
    assert normalization["denominator"] == "den(g_Delta5)=64^-1 Delta5(2Z)"
    assert kappa_bkm_delta5() == Fraction(5, 1)


def test_autborch_domain_conditions_are_not_empty():
    assert AUTBORCH_DOMAIN_CONDITIONS == (
        "integrality",
        "weak holomorphy",
        "discriminant boundedness",
        "lattice compatibility",
        "orientation-character compatibility",
    )


def test_wall_crossing_is_finite_first():
    statement = finite_first_wall_statement()
    assert "N,R" in statement
    assert "inverse limit" in statement


def test_chart_level_cosheaf_contains_all_structure_maps():
    assert construction_has_chart_level_cosheaf()
    assert cosheaf_structure_maps() == (
        "critical chart value",
        "orientation-line transport",
        "HN completed charge sum",
        "refinement push-pull",
        "Thom-Sebastiani factorization",
        "Hall extension convolution",
    )


def test_full_nerve_theta_contains_all_commuting_equations():
    assert construction_has_full_nerve_theta()
    assert theta_full_nerve_equations() == (
        "refinement naturality",
        "BV product to Hall convolution",
        "disjoint Ran factorization",
        "shift/Tate/orientation transport",
    )


def test_wall_crossing_records_finite_first_limit_data():
    assert finite_first_wall_data() == (
        "charge-height truncation",
        "central-charge-radius truncation",
        "finite Hall wall product",
        "finite KS product",
        "HN inverse limit",
    )


def test_duplicate_obstruction_names_are_intentional_orientation_overlap():
    assert duplicate_obstruction_names() == ("o_or",)
