from fractions import Fraction

from compute.lib.ordered_chiral_e3_bar import (
    OrderedBarElement,
    completed_ordered_virasoro_controller,
    completed_ordered_yangian_controller,
    ordered_virasoro_controller,
    ordered_yangian_controller,
)


def test_ordered_words_keep_repeated_inputs_that_exterior_ce_kills():
    controller = ordered_virasoro_controller()
    ttt = OrderedBarElement.basis(controller.word(["T", "T", "T"]))

    assert not ttt.is_zero()
    assert controller.exterior_projection(ttt).is_zero()
    assert controller.ordered_dimension(3) == 1
    assert controller.exterior_shadow_dimension(3) == 0


def test_virasoro_l3_repeated_input_correction_survives_ordered_bar():
    controller = ordered_virasoro_controller()
    ttt = controller.word(["T", "T", "T"])

    correction = controller.higher_block_correction(ttt)

    assert correction.terms == {controller.word(["T"]): Fraction(-2)}
    assert controller.exterior_projection(OrderedBarElement.basis(ttt)).is_zero()


def test_virasoro_l4_quartic_correction_is_exact_rational():
    controller = ordered_virasoro_controller()
    tttt = controller.word(["T", "T", "T", "T"])

    correction = controller.higher_block_correction(tttt)

    assert correction.terms == {controller.word(["T"]): Fraction(40, 27)}
    assert controller.exterior_projection(OrderedBarElement.basis(tttt)).is_zero()


def test_yangian_ordered_to_exterior_projection_is_nontrivial_for_distinct_words():
    controller = ordered_yangian_controller()
    word = controller.word(["e0", "e1", "e2"])
    elem = OrderedBarElement.basis(word)

    projected = controller.exterior_projection(elem)

    assert not projected.is_zero()
    assert projected.terms == {word: Fraction(1)}
    assert controller.ordered_dimension(3) == 27
    assert controller.exterior_shadow_dimension(3) == 1


def test_shadow_report_separates_controller_from_shadow():
    controller = ordered_yangian_controller()
    report = controller.shadow_report(max_arity=3)

    assert report["model"] == "ordered_vertex_bar_controller"
    assert report["shadow"] == "exterior_CE_is_quotient"
    assert report["ordered_dimensions"][3] == 27
    assert report["exterior_dimensions"][3] == 1
    assert report["repeated_inputs_detected"][3] is True


def test_finite_completed_stage_has_fm_boundary_square_zero():
    controller = completed_ordered_yangian_controller(arity_cutoff=4)
    elem = OrderedBarElement.basis(controller.word(["e0", "e1", "e2"]))

    assert controller.cellular_boundary_squared(elem).is_zero()


def test_finite_completed_stage_counts_partial_diagonals():
    controller = completed_ordered_yangian_controller(arity_cutoff=4)
    word = controller.word(["e0", "e1", "e2"])
    faces = controller.fm_boundary_faces(word)

    assert len(faces) == 4
    assert sorted(face.codimension for face in faces) == [1, 1, 1, 2]


def test_finite_completed_stage_records_higher_partial_diagonal_residue():
    controller = completed_ordered_virasoro_controller(arity_cutoff=4)
    ttt = controller.word(["T", "T", "T"])
    residues = controller.partial_diagonal_residues(ttt)

    assert residues[(0, 3)].terms == {controller.word(["T"]): Fraction(-2)}


def test_completed_report_has_finite_stage_and_cech_ran_layers():
    controller = completed_ordered_yangian_controller(arity_cutoff=3)
    report = controller.completed_report(charts=3)

    assert report["controller_kind"] == "finite_arity_stage_of_completed_pro_object"
    assert report["finite_stage_exact"] is True
    assert report["completed_claim"] == "inverse_system_of_all_finite_arity_stages"
    assert report["pro_compatibility_checked"] is True
    assert report["analytic_dolbeault_completion_status"] == "requires_external_functional_analysis"
    assert report["completion_layers"] == {0: 1, 1: 3, 2: 9, 3: 27}
    assert report["cech_ran_simplex_counts"] == {0: 3, 1: 3, 2: 1}
    assert report["keeps_repeated_inputs"][3] is True
