from __future__ import annotations

import pytest
from sympy import Symbol, cancel, simplify

from compute.lib.c3_hcs_hall_theta import (
    C3EquivariantParameters,
    continuity_bound_for_modes,
    differential,
    direct_binary_localization,
    hcs_mode,
    shuffle_product,
    sv_kernel,
    theta_c3_fixed_modes,
    zvars,
)


PARAMS = C3EquivariantParameters(1, 2, -3)


def assert_rational_equal(left, right) -> None:
    assert simplify(cancel(left - right)) == 0


def test_cy_equivariant_condition_is_enforced() -> None:
    with pytest.raises(ValueError):
        C3EquivariantParameters(1, 2, 3)


def test_schiffmann_vasserot_kernel_uses_cy3_parameters() -> None:
    z = Symbol("z")
    kernel = sv_kernel(z, PARAMS)

    assert_rational_equal(
        kernel,
        ((z + 1) * (z + 2) * (z - 3)) / (z * (z + 3) * (z - 1)),
    )


def test_single_hcs_mode_maps_to_positive_shuffle_monomial() -> None:
    (z0,) = zvars(1)
    image = theta_c3_fixed_modes((4,), PARAMS)

    assert image.arity == 1
    assert image.mode_weight == 4
    assert image.pair_pole_bound == 0
    assert_rational_equal(image.expr, z0**4)


def test_binary_theta_equals_direct_two_point_localization_formula() -> None:
    image = theta_c3_fixed_modes((0, 2), PARAMS)

    assert image.arity == 2
    assert image.pair_pole_bound == 1
    assert_rational_equal(image.expr, direct_binary_localization(0, 2, PARAMS))


def test_binary_shuffle_product_records_ordered_source_product() -> None:
    a = hcs_mode(0)
    b = hcs_mode(1)

    product = shuffle_product(a, b, PARAMS)
    image = theta_c3_fixed_modes((0, 1), PARAMS)
    reverse_image = theta_c3_fixed_modes((1, 0), PARAMS)
    z0, z1 = zvars(2)

    assert product.arity == image.arity == 2
    assert product.mode_weight == image.mode_weight == 1
    assert product.pair_pole_bound == image.pair_pole_bound == 1
    assert_rational_equal(product.expr, image.expr)
    assert simplify(cancel((image.expr - reverse_image.expr).subs({z0: 10, z1: 20}))) != 0


def test_fixed_abelian_sector_has_zero_chain_differential() -> None:
    image = theta_c3_fixed_modes((0, 1), PARAMS)

    assert differential(hcs_mode(0)).is_zero()
    assert differential(image).is_zero()


def test_theta_continuity_bound_matches_filtration_metadata() -> None:
    modes = (0, 3)
    image = theta_c3_fixed_modes(modes, PARAMS)

    assert (
        image.arity,
        image.mode_weight,
        image.pair_pole_bound,
    ) == continuity_bound_for_modes(modes)
