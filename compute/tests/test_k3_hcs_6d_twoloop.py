"""Diagnostics for the K3 hCS two-loop/YBE probe."""

from __future__ import annotations

import numpy as np
import pytest

from compute.lib.k3_hcs_6d_oneloop import (
    R_oneloop_correction,
    R_tree_rational,
    embed_12,
    embed_13,
    embed_23,
    permutation,
)
from compute.lib.k3_hcs_6d_twoloop import (
    R_oneloop_normalization_counterterm,
    R_oneloop_normalized,
    feynman_rg_locality_obstruction_exact,
    legacy_twoloop_hbar5_obstruction_exact,
    one_loop_normalization_condition,
    twoloop_yang_normalization_condition,
    ybe_at_hbar5,
    ybe_twoloop_after_one_loop_normalization,
    ybe_with_one_loop_normalization,
)


def _ybe_residual(R12: np.ndarray, R13: np.ndarray, R23: np.ndarray) -> float:
    return float(np.max(np.abs(R12 @ R13 @ R23 - R23 @ R13 @ R12)))


def test_current_two_loop_probe_has_hbar3_not_hbar5_residual() -> None:
    """The advertised two-loop checker is blocked by a one-loop defect."""
    hbar = 1e-4
    u = 2.3
    v = 1.7
    c_v = 2.0
    result = ybe_at_hbar5(N=2, c_v=c_v, dim_g=3.0, hbar=hbar, u=u, v=v)

    residual = result["two_loop_YBE_residual"]
    expected_hbar3_coeff = (12.0 + c_v / 2.0) / (u * v * (u - v))

    assert result["two_loop_verification_passed"] is False
    assert residual / hbar**3 == pytest.approx(expected_hbar3_coeff, rel=2e-3)
    assert residual > 10.0 * hbar**5


def test_linearized_obstruction_is_permutation_commutator() -> None:
    """First nonzero term is c/(uv(u-v)) [P12, P23] at order hbar^3."""
    N = 2
    u = 2.3
    v = 1.7
    x = u - v
    c = 13.0

    identity = np.eye(N**3)
    P = permutation(N)
    P12 = embed_12(P, N)
    P13 = embed_13(P, N)
    P23 = embed_23(P, N)

    r12 = (P12 - identity) / x
    r13 = (P13 - identity) / u
    r23 = (P23 - identity) / v
    q12 = c * P12 / x**2
    q13 = c * P13 / u**2
    q23 = c * P23 / v**2

    lhs_hbar3 = (
        q12 @ r13
        + q12 @ r23
        + r12 @ q13
        + q13 @ r23
        + r12 @ q23
        + r13 @ q23
    )
    rhs_hbar3 = (
        q23 @ r13
        + q23 @ r12
        + r23 @ q13
        + q13 @ r12
        + r23 @ q12
        + r13 @ q12
    )
    defect = lhs_hbar3 - rhs_hbar3

    expected = c / (u * v * x) * (P12 @ P23 - P23 @ P12)
    assert np.max(np.abs(defect - expected)) < 1e-12
    assert np.max(np.abs(defect)) == pytest.approx(6500.0 / 1173.0)


def test_level_renormalized_yang_control_solves_ybe() -> None:
    """A true Yang-coupling renormalization preserves the difference-form YBE."""
    N = 2
    hbar = 0.01
    one_loop_shift = 13.0
    hbar_eff = hbar + one_loop_shift * hbar**2
    u = 2.3
    v = 1.7

    residual = _ybe_residual(
        embed_12(R_tree_rational(u - v, hbar_eff, N), N),
        embed_13(R_tree_rational(u, hbar_eff, N), N),
        embed_23(R_tree_rational(v, hbar_eff, N), N),
    )

    assert residual < 1e-14


def test_one_loop_normalization_condition_is_exact() -> None:
    """Naive fish fails in S3, while Yang normalization kills hbar^3 exactly."""
    condition = one_loop_normalization_condition(c_v=2.0, u=2.3, v=1.7)

    assert condition["one_loop_coefficient"] == "13"
    assert condition["naive_obstruction"] == {
        "P12P23": "6500/1173",
        "P23P12": "-6500/1173",
    }
    assert condition["naive_obstruction_vanishes"] is False
    assert condition["normalized_obstruction"] == {}
    assert condition["normalized_obstruction_vanishes"] is True
    assert condition["expected_naive_commutator_coefficient"] == "6500/1173"


def test_counterterm_identity_is_effective_yang_normalization() -> None:
    """CT1 is fixed by R_tree + fish + CT1 = R_tree(hbar_eff)."""
    N = 2
    hbar = 0.01
    c_v = 2.0
    u = 2.3

    lhs = (
        R_tree_rational(u, hbar, N)
        + R_oneloop_correction(u, hbar, N, c_v)
        + R_oneloop_normalization_counterterm(u, hbar, N, c_v)
    )
    rhs = R_oneloop_normalized(u, hbar, N, c_v)

    assert np.max(np.abs(lhs - rhs)) < 1e-15


def test_one_loop_normalized_rmatrix_satisfies_ybe() -> None:
    """The corrected one-loop object is again a normalized Yang R-matrix."""
    result = ybe_with_one_loop_normalization(N=2, c_v=2.0, hbar=0.01)
    assert result["one_loop_normalization_passed"] is True
    assert result["hbar_effective"] == pytest.approx(0.0113)
    assert result["one_loop_normalized_ybe_residual"] < 1e-14


def test_legacy_twoloop_after_CT1_still_has_hbar5_obstruction() -> None:
    """After the lower repair, the old sunset ansatz still is not a theorem."""
    exact = legacy_twoloop_hbar5_obstruction_exact(c_v=2.0, dim_g=3.0, u=2.3, v=1.7)
    numeric = ybe_twoloop_after_one_loop_normalization(
        N=2,
        c_v=2.0,
        dim_g=3.0,
        hbar=0.01,
        u=2.3,
        v=1.7,
    )

    assert exact["legacy_hbar5_obstruction_vanishes"] is False
    assert exact["two_loop_hbar5_restored"] is False
    assert exact["legacy_hbar5_obstruction"] != {}
    assert numeric["one_loop_normalization_applied"] is True
    assert numeric["two_loop_hbar5_restored"] is False
    assert numeric["two_loop_after_CT1_residual"] > 100.0 * 0.01**5


def test_two_loop_yang_normalization_counterterm_kills_hbar5_obstruction_exactly() -> None:
    """The only constructed CT2 repair is tangent Yang normalization."""
    condition = twoloop_yang_normalization_condition(c_v=2.0, dim_g=3.0, u=2.3, v=1.7)

    assert condition["A2_total_normalised"] == "506/3"
    assert condition["tangent_coefficient"] == "506/3"
    assert condition["legacy_hbar5_obstruction_vanishes"] is False
    assert condition["slot_12_counterterm_hbar4"] == {
        "I": "-837430/729",
        "P12": "226435/243",
    }
    assert condition["repaired_hbar5_obstruction"] == {}
    assert condition["repaired_hbar5_obstruction_vanishes"] is True
    assert condition["two_loop_ybe_normal_form_restored"] is True


def test_subtracting_legacy_sunset_is_the_zero_tangent_special_case() -> None:
    """Setting b=0 is exact subtraction of the non-Yang sunset component."""
    condition = twoloop_yang_normalization_condition(
        c_v=2.0,
        dim_g=3.0,
        u=2.3,
        v=1.7,
        tangent_coefficient=0,
    )

    assert condition["tangent_coefficient"] == "0"
    assert condition["legacy_hbar5_obstruction_vanishes"] is False
    assert condition["repaired_hbar5_obstruction"] == {}
    assert condition["two_loop_ybe_normal_form_restored"] is True


def test_feynman_rg_locality_obstructs_default_yang_counterterm_derivation() -> None:
    """Local two-loop RG data fixes only the pole-four subtraction."""
    witness = feynman_rg_locality_obstruction_exact(c_v=2.0, dim_g=3.0, u=2.3, v=1.7)

    assert witness["A2_total_normalised"] == "506/3"
    assert witness["yang_tangent_coefficient"] == "506/3"
    assert witness["local_pole_order"] == "4"
    assert witness["yang_tangent_pole_order"] == "1"
    assert witness["feynman_rg_local_counterterm_slot_12"] == {
        "I": "-632500/729",
        "P12": "158125/243",
    }
    assert witness["algebraic_yang_counterterm_slot_12"] == {
        "I": "-837430/729",
        "P12": "226435/243",
    }
    assert witness["missing_tangent_slot_12"] == {
        "I": "-2530/9",
        "P12": "2530/9",
    }
    assert witness["local_counterterm_equals_zero_tangent_oracle"] is True
    assert witness["local_counterterm_restores_ybe_by_subtraction"] is True
    assert witness["algebraic_yang_counterterm_restores_ybe"] is True
    assert witness["chosen_yang_counterterm_derived_from_local_rg"] is False
    assert witness["default_yang_counterterm_derived_from_local_rg"] is False


def test_zero_tangent_yang_oracle_is_the_local_feynman_rg_case() -> None:
    """With b=0 there is no missing finite tangent renormalisation."""
    witness = feynman_rg_locality_obstruction_exact(
        c_v=2.0,
        dim_g=3.0,
        u=2.3,
        v=1.7,
        tangent_coefficient=0,
    )

    assert witness["yang_tangent_coefficient"] == "0"
    assert witness["missing_tangent_slot_12"] == {}
    assert witness["feynman_rg_local_counterterm_slot_12"] == witness["algebraic_yang_counterterm_slot_12"]
    assert witness["chosen_yang_counterterm_derived_from_local_rg"] is True
    assert witness["default_yang_counterterm_derived_from_local_rg"] is False


def test_advertised_two_loop_ybe_mod_hbar5_is_rejected() -> None:
    """The old hbar^5 theorem is rejected by a positive negative-oracle test."""
    result = ybe_at_hbar5(N=2, c_v=2.0, dim_g=3.0)
    assert result["two_loop_verification_passed"] is False
    assert result["residual_order_detected"] == "hbar^3"
    assert result["missing_one_loop_ybe_counterterm"] is True
    assert result["one_loop_normalized_hbar3_obstruction_vanishes"] is True
    assert result["legacy_after_CT1_hbar5_obstruction_vanishes"] is False
    assert result["two_loop_hbar5_restored_after_CT1"] is False
