"""Finite-mode witness for the abelian C3 hCS-to-Hall chart map.

This is the torus-fixed, abelian sector.  It proves the algebraic
shuffle-localization part of the chart map; it does not claim to construct the
full analytic hCS-to-Hall morphism on all renormalised observables.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from math import factorial
from typing import Iterable, Tuple

from sympy import Symbol, cancel, simplify


def zvars(n: int) -> Tuple[Symbol, ...]:
    return tuple(Symbol(f"z{i}") for i in range(n))


@dataclass(frozen=True)
class C3EquivariantParameters:
    eps1: int
    eps2: int
    eps3: int

    def __post_init__(self) -> None:
        if self.eps1 + self.eps2 + self.eps3 != 0:
            raise ValueError("C3 equivariant parameters must satisfy eps1+eps2+eps3=0")


def sv_kernel(delta, params: C3EquivariantParameters):
    """Schiffmann-Vasserot C3 kernel in the manuscript convention."""
    e1, e2, e3 = params.eps1, params.eps2, params.eps3
    return cancel(
        ((delta + e1) * (delta + e2) * (delta + e3))
        / (delta * (delta + e1 + e2) * (delta + e2 + e3))
    )


@dataclass(frozen=True)
class ShuffleElement:
    arity: int
    expr: object
    mode_weight: int = 0
    pair_pole_bound: int = 0

    def is_zero(self) -> bool:
        return simplify(self.expr) == 0


def unit() -> ShuffleElement:
    return ShuffleElement(0, 1, 0, 0)


def zero(arity: int = 0) -> ShuffleElement:
    return ShuffleElement(arity, 0, 0, 0)


def hcs_mode(mode: int) -> ShuffleElement:
    if mode < 0:
        raise ValueError("hCS modes in the positive fixed-point sector are nonnegative")
    z0 = zvars(1)[0]
    return ShuffleElement(1, z0**mode, mode, 0)


def _substitute_to_arity(expr, old_arity: int, offset: int, total_arity: int):
    old = zvars(old_arity)
    new = zvars(total_arity)[offset:offset + old_arity]
    return expr.subs(dict(zip(old, new)), simultaneous=True)


def _permute_expr(expr, perm: Tuple[int, ...]):
    variables = zvars(len(perm))
    repl = {variables[i]: variables[perm[i]] for i in range(len(perm))}
    return expr.subs(repl, simultaneous=True)


def symmetrise(expr, arity: int):
    if arity <= 1:
        return cancel(expr)
    total = 0
    for perm in permutations(range(arity)):
        total += _permute_expr(expr, perm)
    return cancel(total / factorial(arity))


def shuffle_product(
    left: ShuffleElement,
    right: ShuffleElement,
    params: C3EquivariantParameters,
) -> ShuffleElement:
    if left.is_zero() or right.is_zero():
        return zero(left.arity + right.arity)
    if left.arity == 0:
        return right
    if right.arity == 0:
        return left

    total_arity = left.arity + right.arity
    variables = zvars(total_arity)
    left_expr = _substitute_to_arity(left.expr, left.arity, 0, total_arity)
    right_expr = _substitute_to_arity(right.expr, right.arity, left.arity, total_arity)

    kernel = 1
    for i in range(left.arity):
        for j in range(left.arity, total_arity):
            kernel *= sv_kernel(variables[j] - variables[i], params)

    expr = symmetrise(left_expr * right_expr * kernel, total_arity)
    return ShuffleElement(
        total_arity,
        cancel(expr),
        left.mode_weight + right.mode_weight,
        left.pair_pole_bound + right.pair_pole_bound + left.arity * right.arity,
    )


def theta_c3_fixed_modes(
    modes: Iterable[int],
    params: C3EquivariantParameters,
) -> ShuffleElement:
    result = unit()
    for mode in modes:
        result = shuffle_product(result, hcs_mode(mode), params)
    return result


def direct_binary_localization(mode_left: int, mode_right: int, params: C3EquivariantParameters):
    z0, z1 = zvars(2)
    first = z0**mode_left * z1**mode_right * sv_kernel(z1 - z0, params)
    second = z1**mode_left * z0**mode_right * sv_kernel(z0 - z1, params)
    return cancel((first + second) / 2)


def differential(element: ShuffleElement) -> ShuffleElement:
    """Abelian torus-fixed sector differential."""
    return zero(element.arity)


def continuity_bound_for_modes(modes: Tuple[int, ...]) -> Tuple[int, int, int]:
    """Return (arity, mode-weight, pair-pole bound) for the filtered map."""
    arity = len(modes)
    mode_weight = sum(modes)
    pair_pole_bound = arity * (arity - 1) // 2
    return arity, mode_weight, pair_pole_bound


__all__ = [
    "C3EquivariantParameters",
    "ShuffleElement",
    "continuity_bound_for_modes",
    "differential",
    "direct_binary_localization",
    "hcs_mode",
    "shuffle_product",
    "sv_kernel",
    "theta_c3_fixed_modes",
    "unit",
    "zero",
    "zvars",
]
