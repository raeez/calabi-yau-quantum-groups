r"""Tests for k3_yangian_borcherds_weight_theta_refinement.

Verifies the two honest kappa_BKM ladders on the CHL slice
N in {1, 2, 3, 4, 6} -- Mathieu-twined (10, 4, 3, 2, 1) and
Govindarajan-Krishna square-root (5, 3, 2, 3/2, 1) with Jatkar-Sen
doubles (10, 6, 4, 3, 2) -- computed from frame shapes and the K3
Hodge diamond, and the two negative results: the mixed tuple
(5, 4, 3, 2, 1) matches no single family, and no integer-weight
Sp_4(Z) cusp forms of weights <= 4 exist.
"""

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_borcherds_weight_theta_refinement import (
    ALL_ORDERS,
    CHL_SLICE,
    FRAME_SHAPES,
    a1,
    delta5_c0,
    ell_genus_q0_row,
    frame_dimension,
    frame_power,
    gk_ladder,
    gk_sqrt_weight,
    js_ladder,
    js_weight,
    mixed_tuple_matches_no_family,
    sp4z_integer_weight_claim_impossible,
    twined_c0,
    twined_ladder,
    twined_weight,
    twining_genus_q0_row,
    verify_ell_genus_row,
    verify_frame_dimensions,
    verify_js_prime_frame_identity,
    verify_ladders,
    verify_power_map_closure,
    verify_squaring_relation,
)


class TestFrameShapes:
    """Primary data: frame shapes and their arithmetic."""

    @pytest.mark.parametrize("N", ALL_ORDERS)
    def test_frame_dimension_24(self, N):
        assert frame_dimension(N) == 24

    @pytest.mark.parametrize(
        "N,expected_a1",
        [(1, 24), (2, 8), (3, 6), (4, 4), (5, 4), (6, 2), (7, 3), (8, 2)],
    )
    def test_a1_values(self, N, expected_a1):
        assert a1(N) == expected_a1

    def test_power_map_closure(self):
        assert verify_power_map_closure()

    def test_6A_squared_is_3A(self):
        assert frame_power(FRAME_SHAPES[6], 2) == FRAME_SHAPES[3]

    def test_6A_cubed_is_2A(self):
        assert frame_power(FRAME_SHAPES[6], 3) == FRAME_SHAPES[2]


class TestEllipticGenusRow:
    """c(0,0) = 20 computed from the K3 Hodge diamond; half-genus 10."""

    def test_q0_row(self):
        assert ell_genus_q0_row() == {-1: 2, 0: 20, 1: 2}

    def test_delta5_input_constant(self):
        assert delta5_c0() == 10

    def test_verify_path(self):
        assert verify_ell_genus_row()

    @pytest.mark.parametrize(
        "N,const", [(2, 4), (3, 2), (4, 0), (6, -2)]
    )
    def test_twining_genus_row_constant(self, N, const):
        """The twining-genus q^0 row constant is a_1 - 4; it is NOT
        the twined Siegel weight constant a_1 (twisted-sector
        completion) -- the distinction the engine documents."""
        assert twining_genus_q0_row(N)[0] == const


class TestTwinedLadder:
    """Mathieu-twined family: weights (10, 4, 3, 2, 1)."""

    @pytest.mark.parametrize(
        "N,c0", [(1, 20), (2, 8), (3, 6), (4, 4), (6, 2)]
    )
    def test_constants(self, N, c0):
        assert twined_c0(N) == c0

    @pytest.mark.parametrize(
        "N,wt",
        [(1, Fraction(10)), (2, Fraction(4)), (3, Fraction(3)),
         (4, Fraction(2)), (6, Fraction(1))],
    )
    def test_weights(self, N, wt):
        assert twined_weight(N) == wt

    def test_ladder_table(self):
        assert twined_ladder() == [
            (1, 20, Fraction(10)),
            (2, 8, Fraction(4)),
            (3, 6, Fraction(3)),
            (4, 4, Fraction(2)),
            (6, 2, Fraction(1)),
        ]

    def test_weakly_decreasing(self):
        wts = [twined_weight(N) for N in CHL_SLICE]
        assert all(a >= b for a, b in zip(wts, wts[1:]))


class TestSquareRootAndJatkarSenLadders:
    """GK square roots (5, 3, 2, 3/2, 1); JS doubles (10, 6, 4, 3, 2)."""

    def test_js_ladder(self):
        assert js_ladder() == [(1, 10), (2, 6), (3, 4), (4, 3), (6, 2)]

    def test_gk_ladder(self):
        assert gk_ladder() == [
            (1, Fraction(5)),
            (2, Fraction(3)),
            (3, Fraction(2)),
            (4, Fraction(3, 2)),
            (6, Fraction(1)),
        ]

    def test_js_prime_frame_identity(self):
        """Computed 24/(N+1) - 2 equals a_1 - 2 at prime N."""
        assert verify_js_prime_frame_identity()

    @pytest.mark.parametrize("N", [1, 2, 3, 4, 6])
    def test_gk_squares_to_js(self, N):
        assert 2 * gk_sqrt_weight(N) == js_weight(N)

    def test_squaring_relation_at_N1(self):
        """chi_10 = Delta_5^2: twined N = 1 weight equals JS N = 1
        weight equals twice the GK N = 1 weight."""
        assert verify_squaring_relation()


class TestNegativeResults:
    """The falsified claims stay falsified."""

    def test_mixed_tuple_matches_no_family(self):
        assert mixed_tuple_matches_no_family()

    def test_no_low_weight_sp4z_cusp_forms(self):
        assert sp4z_integer_weight_claim_impossible()

    def test_all_ladders(self):
        assert verify_ladders()

    def test_all_frame_dimensions(self):
        assert verify_frame_dimensions()
