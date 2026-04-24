from dataclasses import replace
from fractions import Fraction

from compute.lib.bps_positive_truncation import (
    BPSMotivicTruncation,
    Charge,
    FiniteChargeSet,
    FiniteLinearMap,
    ObstructionVector,
    OrientationData,
    TruncationBound,
    bms_compact_nontoric_solution_certificate,
    constructed_named_points_certificate,
    conifold_quantum_pentagon_certificate,
    derived_solution_stack_certificate,
    derived_solution_stack_factors,
    finite_lower_set_certificate,
    finite_rank2_truncation,
    full_hall_borcherds_radical_certificate,
    hall_associativity_certificate,
    igusa_normalization_certificate,
    ks_loop_holonomy_a2_certificate,
    master_truncation_certificate,
    obstruction_zero_certificate,
    orientation_certificate,
    radical_non_degeneracy_certificate,
    seven_extension_resolution_certificate,
    sector_descent_certificate,
    support_property_certificate,
    hcs_named_obstruction_certificate,
    k3e_unquotiented_radical_certificate,
    quintic_excert_surface_certificate,
    schoen_banana_gluing_certificate,
    theta_comparison_certificate,
    toric_c3_collapse_certificate,
    toric_conifold_collapse_certificate,
    transition_certificate,
)
from compute.lib.motivic_e1_algebra import MotivicClass
from compute.lib.phi01_fourier import phi01_coefficient


def _bound() -> TruncationBound:
    return TruncationBound(N=4, R_num=4)


def test_charge_set_support_property_is_finite():
    truncation = finite_rank2_truncation(4)
    certificate = support_property_certificate(truncation, _bound())

    assert certificate.passed
    assert certificate.exact
    assert certificate.checked_items == len(truncation.charges.charges)


def test_orientation_cech_delta_zero():
    truncation = finite_rank2_truncation(4)
    certificate = orientation_certificate(truncation)

    assert certificate.passed
    assert truncation.orientation.cech_delta_zero()
    assert set(truncation.orientation.obstruction_class().values()) == {0}


def test_orientation_quadratic_refinement_all_pairs():
    truncation = finite_rank2_truncation(4)
    charges = set(truncation.charges.charges)

    for alpha in charges:
        for beta in charges:
            total = alpha + beta
            if total not in charges:
                continue
            lhs = truncation.orientation.q(total)
            rhs = (
                (-1 if truncation.orientation.pairing(alpha, beta) % 2 else 1)
                * truncation.orientation.q(alpha)
                * truncation.orientation.q(beta)
            )
            assert lhs == rhs


def test_orientation_twisted_class_is_retained():
    truncation = finite_rank2_truncation(3)
    twisted_orientation = OrientationData(
        cech_signs={(0, 1): 1, (0, 2): 0, (1, 2): 0},
        quadratic_refinement=truncation.orientation.quadratic_refinement,
        pairing=truncation.orientation.pairing,
    )
    twisted = replace(truncation, orientation=twisted_orientation)
    certificate = orientation_certificate(twisted)

    assert certificate.passed
    assert twisted.orientation.cech_delta_zero()
    assert any(value == 1 for value in twisted.orientation.obstruction_class().values())


def test_hall_associativity_all_triples_to_bound():
    truncation = finite_rank2_truncation(4)
    certificate = hall_associativity_certificate(truncation)

    assert certificate.passed
    assert certificate.checked_items > 0


def test_hall_associativity_detects_boundary_zeroing_failure():
    a = Charge((1, 0))
    c = Charge((0, 1))
    ac = Charge((1, 1))
    aac = Charge((2, 1))
    charges = (a, c, ac, aac)
    charge_set = FiniteChargeSet(
        charges=charges,
        height=lambda charge: sum(charge.coords),
        central_abs_bound=lambda charge: Fraction(sum(charge.coords), 1),
        support_q=lambda charge: Fraction(sum(x * x for x in charge.coords), 1),
    )
    truncation = BPSMotivicTruncation(
        geometry="quotient_zeroing_falsifier",
        charges=charge_set,
        orientation=OrientationData(
            cech_signs={},
            quadratic_refinement={
                charge: (-1 if (charge.coords[0] * charge.coords[1]) % 2 else 1)
                for charge in charges
            },
            pairing=lambda left, right: (
                left.coords[0] * right.coords[1]
                - left.coords[1] * right.coords[0]
            ),
        ),
        sector_order=(),
        coefficients={charge: MotivicClass.one() for charge in charges},
        convention="hall",
    )
    certificate = hall_associativity_certificate(truncation)

    assert not certificate.passed
    assert any(
        entry["alpha"] == a.coords
        and entry["beta"] == a.coords
        and entry["gamma"] == c.coords
        for entry in certificate.discrepancies
    )


def test_sector_descent_two_sector_hn_product():
    truncation = finite_rank2_truncation(4)
    certificate = sector_descent_certificate(truncation)

    assert certificate.passed
    assert certificate.checked_items > 0


def test_finite_lower_set_certificate_for_rank2_model():
    truncation = finite_rank2_truncation(4)
    certificate = finite_lower_set_certificate(truncation)

    assert certificate.passed
    assert certificate.exact
    assert certificate.checked_items > 0


def test_finite_lower_set_certificate_detects_omitted_ambient_summands():
    gamma = Charge((1, 1))
    ambient = (Charge((1, 0)), Charge((0, 1)), gamma)
    charge_set = FiniteChargeSet(
        charges=(gamma,),
        height=lambda charge: sum(charge.coords),
        central_abs_bound=lambda charge: Fraction(sum(charge.coords), 1),
        support_q=lambda charge: Fraction(sum(x * x for x in charge.coords), 1),
    )
    truncation = BPSMotivicTruncation(
        geometry="non_lower_falsifier",
        charges=charge_set,
        orientation=OrientationData(
            cech_signs={},
            quadratic_refinement={gamma: 1},
            pairing=lambda left, right: 0,
        ),
        sector_order=(),
        coefficients={gamma: MotivicClass.one()},
        convention="hall",
    )
    certificate = finite_lower_set_certificate(truncation, ambient)

    assert not certificate.passed
    assert certificate.exact
    assert {
        entry["failure"] for entry in certificate.discrepancies
    } == {"retained charge has omitted ambient summand"}


def test_transition_certificate_for_nested_rank2_quotients():
    small = finite_rank2_truncation(3)
    big = finite_rank2_truncation(4)
    certificate = transition_certificate(small, big)

    assert certificate.passed
    assert certificate.exact
    assert certificate.checked_items > 0


def test_ks_loop_holonomy_a2_joint():
    certificate = ks_loop_holonomy_a2_certificate(5)

    assert certificate.passed
    assert certificate.exact


def test_conifold_quantum_pentagon_embedded():
    certificate = conifold_quantum_pentagon_certificate(N_q=10, max_charge=6)

    assert certificate.passed
    assert certificate.checked_items > 0


def test_toric_c3_collapse_macmahon_yplus():
    certificate = toric_c3_collapse_certificate(10)

    assert certificate.passed
    assert certificate.normalization == "MacMahon equals plane partitions equals Y^+ character"


def test_toric_conifold_collapse_dual_cauchy():
    certificate = toric_conifold_collapse_certificate(max_q=10, max_Q=4)

    assert certificate.passed


def test_igusa_c0_weight_normalization():
    assert phi01_coefficient(0, -1) == 1
    assert phi01_coefficient(0, 0) == 10
    assert phi01_coefficient(0, 1) == 1
    assert phi01_coefficient(0, 0) // 2 == 5


def test_igusa_product_theta_normalization():
    certificate = igusa_normalization_certificate(N_prod=10, N_theta=20, D_max=60)

    assert certificate.passed
    assert not certificate.exact
    assert "64^{-1}Delta_5(2Z)" in certificate.theorem_target


def test_master_certificate_c3():
    certificate = master_truncation_certificate("C3", _bound())

    assert certificate.passed
    assert certificate.exact


def test_master_certificate_conifold():
    certificate = master_truncation_certificate("conifold", _bound())

    assert certificate.passed
    assert certificate.exact


def test_master_certificate_k3e_boundary():
    certificate = master_truncation_certificate("K3xE_boundary", _bound())

    assert certificate.passed
    assert not certificate.exact


def test_product_refuses_outside_quotient_by_zeroing():
    truncation = finite_rank2_truncation(1)
    alpha = Charge((1, 0))
    beta = Charge((0, 1))

    assert truncation.product_class(alpha, beta) == MotivicClass.zero()


def test_hall_and_torus_conventions_are_distinct():
    hall = finite_rank2_truncation(2)
    torus = BPSMotivicTruncation(
        geometry=hall.geometry,
        charges=hall.charges,
        orientation=hall.orientation,
        sector_order=hall.sector_order,
        coefficients=hall.coefficients,
        convention="torus",
    )
    alpha = Charge((1, 0))
    beta = Charge((0, 1))

    assert hall.product_class(alpha, beta) != torus.product_class(alpha, beta)
    assert hall.product_class(alpha, beta) == -1 * MotivicClass.L_half(-1)
    assert torus.product_class(alpha, beta) == -1 * MotivicClass.L_half(1)


def test_quintic_excert_surface_certificate():
    certificate = quintic_excert_surface_certificate()

    assert certificate.passed
    assert not certificate.exact
    assert "Bridgeland/support/HN" in certificate.theorem_target


def test_schoen_banana_gluing_certificate():
    certificate = schoen_banana_gluing_certificate()

    assert certificate.passed
    assert not certificate.exact
    assert "compact Hall gluing" in certificate.normalization


def test_k3e_unquotiented_radical_certificate():
    certificate = k3e_unquotiented_radical_certificate()

    assert certificate.passed
    assert not certificate.exact
    assert "full Hall-Borcherds radical vector" in certificate.theorem_target
    assert "pairing coordinate" in certificate.normalization


def test_full_hall_borcherds_radical_certificate_is_not_gram_only():
    certificate = full_hall_borcherds_radical_certificate()

    assert certificate.passed
    assert not certificate.exact
    assert "full Hall-Borcherds radical vector" in certificate.theorem_target
    assert "pairing, orientation character, protected integration" in certificate.normalization
    assert "~/igusa-cusp-form/proj.tex" in certificate.source_modules


def test_theta_comparison_certificate():
    certificate = theta_comparison_certificate(_bound())

    assert certificate.passed
    assert not certificate.exact
    assert "Phi_KS" in certificate.normalization


def test_hcs_named_obstruction_certificate():
    certificate = hcs_named_obstruction_certificate()

    assert certificate.passed
    assert not certificate.exact
    assert certificate.checked_items == 14
    assert "primitive hCS package" in certificate.theorem_target
    factor = {
        factor.name: factor
        for factor in derived_solution_stack_factors(_bound())
    }["hcs_named_zero_fiber"]
    assert "o_or_rel" in factor.obstruction.names
    assert "o_or" not in factor.obstruction.names


def test_finite_linear_map_rank_and_nullity_are_exact():
    full_rank = FiniteLinearMap((
        (Fraction(2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(3), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(5)),
    ))
    singular = FiniteLinearMap((
        (Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(2), Fraction(2), Fraction(0)),
    ))

    assert full_rank.rank() == 3
    assert full_rank.nullity() == 0
    assert singular.rank() == 1
    assert singular.nullity() == 2
    assert full_rank.apply((Fraction(1), Fraction(2), Fraction(3))) == (
        Fraction(2),
        Fraction(6),
        Fraction(15),
    )


def test_obstruction_zero_certificate_detects_nonzero_coordinate():
    obstruction = ObstructionVector(
        names=("o_MC", "o_or"),
        values=(Fraction(0), Fraction(1)),
    )
    certificate = obstruction_zero_certificate("hcs_test", obstruction)

    assert not certificate.passed
    assert certificate.exact
    assert certificate.discrepancies == ({"obstruction": "o_or", "value": "1"},)


def test_obstruction_zero_certificate_detects_uncomputed_coordinates():
    obstruction = ObstructionVector(
        names=("sigma_support_HN",),
        values=(Fraction(0),),
        computed=False,
    )
    certificate = obstruction_zero_certificate("quintic_test", obstruction)

    assert not certificate.passed
    assert certificate.exact
    assert certificate.discrepancies == (
        {"obstruction": "sigma_support_HN", "value": "uncomputed"},
    )


def test_radical_non_degeneracy_certificate_detects_kernel():
    gram = FiniteLinearMap((
        (Fraction(1), Fraction(1)),
        (Fraction(2), Fraction(2)),
    ))
    certificate = radical_non_degeneracy_certificate("singular", gram)

    assert not certificate.passed
    assert certificate.exact
    assert certificate.discrepancies == ({"check": "Rad_Aut=0", "nullity": 1},)


def test_bms_compact_nontoric_solution_certificate():
    certificate = bms_compact_nontoric_solution_certificate()

    assert certificate.passed
    assert certificate.exact
    assert "Bayer-Macri-Stellari" in certificate.theorem_target


def test_derived_solution_stack_factors_are_zero_fibers():
    factors = derived_solution_stack_factors(_bound())
    by_name = {factor.name: factor for factor in factors}

    assert set(by_name) == {
        "compact_nontoric_bms",
        "quintic_excert",
        "schoen_banana_gluing",
        "k3e_raw_radical",
        "theta_comparison",
        "hcs_named_zero_fiber",
    }
    assert all(factor.certificate.passed for factor in factors)
    assert by_name["compact_nontoric_bms"].solved
    for name in set(by_name) - {"compact_nontoric_bms"}:
        assert not by_name[name].solved
        assert by_name[name].zero_fiber_defined
        assert not by_name[name].obstruction.computed


def test_derived_solution_stack_certificate():
    certificate = derived_solution_stack_certificate(_bound())

    assert certificate.passed
    assert certificate.exact
    assert "zero-fiber substacks" in certificate.theorem_target


def test_constructed_named_points_certificate_records_remaining_points():
    certificate = constructed_named_points_certificate(_bound())

    assert not certificate.passed
    assert not certificate.exact
    unresolved = {entry["factor"] for entry in certificate.discrepancies}
    assert unresolved == {
        "quintic_excert",
        "schoen_banana_gluing",
        "k3e_raw_radical",
        "theta_comparison",
        "hcs_named_zero_fiber",
    }


def test_seven_extension_resolution_certificate():
    certificate = seven_extension_resolution_certificate(_bound())

    assert certificate.passed
    assert not certificate.exact
    assert "all seven extension lanes" in certificate.theorem_target
