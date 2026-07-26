"""Independent checks for the weight-11/12 motivic arithmetic engine."""

from fractions import Fraction
from itertools import permutations
from math import factorial

import pytest

from compute.lib.k3_yangian_pentagon_coboundary_hbar11_12 import (
    borcherds_leg_weight_raw,
    borcherds_scalar_section,
    delta5_pure_q_log_coefficient,
    first_depth_4_entry_at_weight_12,
    hoffman_words,
    kz_denominator,
    kz_normalization_status,
    mittag_leffler_at_weight,
    mzv_has_depth_4_irreducible,
    obs_g_formula,
    obs_infty_pro_limit_well_defined_through_weight_12,
    padovan_dim,
    padovan_dim_11,
    padovan_dim_12,
    phi_n_symbolic,
    repeated_mzv_newton,
    run_tests,
    zeta3333_newton_identity,
    zeta3333_status,
)


def _independent_hoffman_count(weight: int) -> int:
    """Count 2/3-compositions by a recursion separate from the engine."""
    if weight < 0:
        return 0
    if weight == 0:
        return 1
    return (
        _independent_hoffman_count(weight - 2)
        + _independent_hoffman_count(weight - 3)
    )


def _cycle_lengths(permutation):
    seen = set()
    lengths = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        length = 0
        current = start
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return lengths


def _permutation_oracle(single_weight: int, depth: int):
    r"""Elementary symmetric polynomial from the permutation formula.

    e_r = (1/r!) sum_{sigma in S_r} sign(sigma) p_sigma.
    This route is independent of the engine's Newton recurrence.
    """
    result = {}
    for permutation in permutations(range(depth)):
        cycles = _cycle_lengths(permutation)
        sign = -1 if (depth - len(cycles)) % 2 else 1
        monomial = tuple(sorted(single_weight * size for size in cycles))
        result[monomial] = result.get(monomial, Fraction(0)) + Fraction(
            sign, factorial(depth)
        )
    return {key: value for key, value in result.items() if value}


class TestHoffmanDimensions:
    def test_dimensions_11_and_12(self):
        assert padovan_dim_11() == 9
        assert padovan_dim_12() == 12

    @pytest.mark.parametrize("weight", range(0, 16))
    def test_independent_composition_count(self, weight):
        assert padovan_dim(weight) == _independent_hoffman_count(weight)

    def test_words_have_correct_weight(self):
        for weight in range(2, 16):
            assert all(sum(word) == weight for word in hoffman_words(weight))
            assert all(set(word) <= {2, 3} for word in hoffman_words(weight))


class TestRepeatedZetaNewtonIdentity:
    def test_permutation_oracle(self):
        assert zeta3333_newton_identity() == _permutation_oracle(3, 4)

    def test_literal_coefficients(self):
        assert zeta3333_newton_identity() == {
            (3, 3, 3, 3): Fraction(1, 24),
            (3, 3, 6): Fraction(-1, 4),
            (6, 6): Fraction(1, 8),
            (3, 9): Fraction(1, 3),
            (12,): Fraction(-1, 4),
        }

    def test_limiting_depths(self):
        assert repeated_mzv_newton(5, 1) == {(5,): Fraction(1)}
        assert repeated_mzv_newton(5, 2) == {
            (5, 5): Fraction(1, 2),
            (10,): Fraction(-1, 2),
        }

    def test_primitive_status(self):
        status = zeta3333_status()
        assert status["decomposable"]
        assert status["primitive_projection"] == 0
        assert not status["first_depth_four_primitive"]
        assert first_depth_4_entry_at_weight_12() is None
        assert mzv_has_depth_4_irreducible(12) is None


class TestExactBorcherdsScalar:
    @pytest.mark.parametrize("height", range(1, 9))
    def test_pure_q_log_by_direct_factor_expansion(self, height):
        direct = sum(
            -Fraction(10, height // divisor)
            for divisor in range(1, height + 1)
            if height % divisor == 0
        )
        assert delta5_pure_q_log_coefficient(height) == direct

    def test_resolved_weights_and_characters(self):
        odd = borcherds_scalar_section(11)
        even = borcherds_scalar_section(12)
        assert borcherds_leg_weight_raw(11) == -11
        assert borcherds_leg_weight_raw(12) == -12
        assert odd["delta5_character"] == "nu_Delta5"
        assert even["delta5_character"] == "trivial"
        assert odd["product_exponent_scale"] == 11
        assert even["product_exponent_scale"] == 12

    def test_scalar_to_cochain_gate(self):
        section = borcherds_scalar_section(12)
        assert not section["coefficient_to_cochain_map_constructed"]
        assert not section["cyclic_closure_verified"]
        assert not section["maurer_cartan_verified"]


class TestCochainAndProLimitStatus:
    def test_kz_simplex_scope(self):
        assert kz_denominator(12) == factorial(12)
        status = kz_normalization_status(12)
        assert not status["word_specified"]
        assert not status["regularised_word_integral_computed"]
        assert not status["word_to_cochain_map_constructed"]

    def test_phi12_remains_open(self):
        phi12 = phi_n_symbolic(12)
        assert phi12["motivic_dimension"] == 12
        assert not phi12["phi_n_constructed"]
        assert not phi12["rotation_equation_verified"]
        assert not phi12["maurer_cartan_equation_verified"]
        assert not phi12["zeta3333"]["grt_action_computed"]

    def test_motivic_projection_and_cyclic_transition_are_separate(self):
        level = mittag_leffler_at_weight(12)
        assert level["motivic_quotient_projection_surjective"]
        assert not level["cyclic_obstruction_transition_constructed"]
        assert level["cyclic_obstruction_transition_surjective"] is None
        assert level["cyclic_lim1"] is None

    def test_pro_limit_status(self):
        status = obs_infty_pro_limit_well_defined_through_weight_12()
        assert status["motivic_projections_surjective"]
        assert not status["cyclic_inverse_system_constructed"]
        assert status["lim1"] is None
        assert status["pro_limit_well_defined"] is None

    def test_genus_11_requires_independent_graph_class(self):
        genus = obs_g_formula(11)
        assert genus["gamma12_required"]
        assert not genus["zeta3333_primitive_contribution"]
        assert not genus["phi12_cochain_constructed"]
        assert not genus["obs_g_constructed"]

    def test_internal_checks(self):
        checks = run_tests()
        assert checks
        assert all(checks.values())


class TestInputValidation:
    @pytest.mark.parametrize(
        "call",
        [
            lambda: repeated_mzv_newton(1, 4),
            lambda: repeated_mzv_newton(3, -1),
            lambda: delta5_pure_q_log_coefficient(0),
            lambda: borcherds_scalar_section(-1),
            lambda: phi_n_symbolic(-1),
        ],
    )
    def test_invalid_inputs(self, call):
        with pytest.raises(ValueError):
            call()
