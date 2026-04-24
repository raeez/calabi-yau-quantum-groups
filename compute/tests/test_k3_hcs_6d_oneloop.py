"""One-loop YBE diagnostics for the K3 hCS rational-limit probe."""

from __future__ import annotations

import numpy as np
import pytest

from compute.lib.k3_hcs_6d_oneloop import (
    R_oneloop_yang_renormalized,
    R_oneloop_yang_tangent_correction,
    R_oneloop_yang_tangent_full,
    R_tree_rational,
    embed_12,
    embed_13,
    embed_23,
    k3_yang_one_loop_shift,
    permutation,
    ybe_at_order,
)


def _ybe_residual(R12: np.ndarray, R13: np.ndarray, R23: np.ndarray) -> float:
    return float(np.max(np.abs(R12 @ R13 @ R23 - R23 @ R13 @ R12)))


def _hbar3_coefficient(
    N: int,
    c_v: float,
    u: float,
    v: float,
    one_loop_kind: str,
) -> np.ndarray:
    """Coefficient of hbar^3 for R=I+hbar r+hbar^2 q+O(hbar^3)."""
    x = u - v
    c = k3_yang_one_loop_shift(c_v)
    identity = np.eye(N**3)
    P = permutation(N)
    P12 = embed_12(P, N)
    P13 = embed_13(P, N)
    P23 = embed_23(P, N)

    r12 = (P12 - identity) / x
    r13 = (P13 - identity) / u
    r23 = (P23 - identity) / v

    q_tree_12 = (identity - P12) / x**2
    q_tree_13 = (identity - P13) / u**2
    q_tree_23 = (identity - P23) / v**2

    if one_loop_kind == "naive_fish":
        q12 = q_tree_12 + c * P12 / x**2
        q13 = q_tree_13 + c * P13 / u**2
        q23 = q_tree_23 + c * P23 / v**2
    elif one_loop_kind == "yang_tangent":
        q12 = q_tree_12 + c * (P12 - identity) / x
        q13 = q_tree_13 + c * (P13 - identity) / u
        q23 = q_tree_23 + c * (P23 - identity) / v
    else:
        raise ValueError(one_loop_kind)

    lhs = (
        q12 @ r13
        + q12 @ r23
        + r12 @ q13
        + q13 @ r23
        + r12 @ q23
        + r13 @ q23
        + r12 @ r13 @ r23
    )
    rhs = (
        q23 @ r13
        + q23 @ r12
        + r23 @ q13
        + q13 @ r12
        + r23 @ q12
        + r13 @ q12
        + r23 @ r13 @ r12
    )
    return lhs - rhs


def test_naive_fish_has_the_hbar3_permutation_commutator() -> None:
    N = 2
    c_v = 2.0
    u = 2.3
    v = 1.7
    x = u - v
    c = k3_yang_one_loop_shift(c_v)

    defect = _hbar3_coefficient(N, c_v, u, v, "naive_fish")
    P = permutation(N)
    expected = c / (u * v * x) * (embed_12(P, N) @ embed_23(P, N) - embed_23(P, N) @ embed_12(P, N))

    assert np.max(np.abs(defect - expected)) < 1e-12
    assert np.max(np.abs(defect)) == pytest.approx(6500.0 / 1173.0)


def test_yang_tangent_kills_the_hbar3_coefficient() -> None:
    defect = _hbar3_coefficient(N=2, c_v=2.0, u=2.3, v=1.7, one_loop_kind="yang_tangent")
    assert np.max(np.abs(defect)) < 1e-12


@pytest.mark.parametrize(("N", "c_v"), [(2, 2.0), (3, 3.0)])
def test_exact_yang_coupling_renormalization_solves_ybe(N: int, c_v: float) -> None:
    hbar = 0.01
    u = 2.3
    v = 1.7
    residual = _ybe_residual(
        embed_12(R_oneloop_yang_renormalized(u - v, hbar, N, c_v), N),
        embed_13(R_oneloop_yang_renormalized(u, hbar, N, c_v), N),
        embed_23(R_oneloop_yang_renormalized(v, hbar, N, c_v), N),
    )
    assert residual < 1e-14


def test_formal_tangent_is_first_order_of_exact_renormalization() -> None:
    N = 2
    c_v = 2.0
    u = 2.3

    errors = []
    for hbar in (1e-2, 5e-3):
        exact_delta = R_oneloop_yang_renormalized(u, hbar, N, c_v) - R_tree_rational(u, hbar, N)
        tangent = R_oneloop_yang_tangent_correction(u, hbar, N, c_v)
        errors.append(float(np.max(np.abs(exact_delta - tangent))))

    assert errors[1] < errors[0] / 3.5


def test_formal_tangent_residual_starts_at_hbar4_not_hbar3() -> None:
    N = 2
    c_v = 2.0
    u = 2.3
    v = 1.7

    def residual(hbar: float) -> float:
        return _ybe_residual(
            embed_12(R_oneloop_yang_tangent_full(u - v, hbar, N, c_v), N),
            embed_13(R_oneloop_yang_tangent_full(u, hbar, N, c_v), N),
            embed_23(R_oneloop_yang_tangent_full(v, hbar, N, c_v), N),
        )

    r1 = residual(1e-2)
    r2 = residual(5e-3)

    assert r1 / r2 == pytest.approx(16.0, rel=0.12)
    assert ybe_at_order(N, c_v, hbar=1e-3)["naive_fish_ybe_preserved_at_hbar3"] is False
    assert ybe_at_order(N, c_v, hbar=1e-3)["renormalized_yang_exact_ybe"] is True
