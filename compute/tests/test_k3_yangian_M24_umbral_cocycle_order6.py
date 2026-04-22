"""Tests for the M_24 order-6 umbral cocycle compute module.

Wave 15 extension: 6A vs 6B class distinction for the pentagon-hbar^3
cocycle on the K3-stable-W Schur cocycle.
"""
# Raeez Lorgat -- Wave 15 compute tests for the 6A / 6B distinction.

from __future__ import annotations

import pytest

from compute.lib.k3_yangian_M24_umbral_cocycle_order6 import (
    character_chi23_order6,
    cocycle_class_order6,
    cocycle_order_verification,
    distinguishability_6A_vs_6B,
    m_sigma_mod24_phase,
    order6_cycle_shape,
    pentagon_hbar3_cocycle_sum_order6,
    restriction_bockstein_consistency,
    schur_multiplier_M24,
    serre_cocycle_order_on_K3,
    umbral_phase_order,
    umbral_shift_order6,
    umbral_shift_signatures,
)


# ----------------------------------------------------------------------
# Baseline Wave 14 facts (preserved across Wave 15 upgrade)
# ----------------------------------------------------------------------


def test_schur_multiplier_is_Z_mod_12() -> None:
    """H^2(M_24, U(1)) = Z/12 (ATLAS 1985)."""
    m = schur_multiplier_M24()
    assert m["group"] == "Z/12"
    assert m["factorisation"] == "Z/2 x Z/2 x Z/3"


def test_serre_cocycle_order_is_6() -> None:
    """Serre-functor Schur cocycle has order 6 in Z/12."""
    assert serre_cocycle_order_on_K3() == 6
    assert cocycle_order_verification()


def test_anomalous_classes_count() -> None:
    """Five anomalous (non-Mukai) classes per Gaberdiel-Hohenegger-Volpato 2012."""
    sig = umbral_shift_signatures()
    assert len(sig["anomalous_classes"]) == 5
    assert sig["count_classes"] == 26


# ----------------------------------------------------------------------
# Wave 15: 6A vs 6B cycle-shape and umbral-shift primary facts
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "cls,expected_shape",
    [("6A", "1^2 2^2 3^2 6^2"), ("6B", "6^4")],
)
def test_order6_cycle_shape(cls: str, expected_shape: str) -> None:
    """Cycle shapes from ATLAS p. 96."""
    assert order6_cycle_shape(cls) == expected_shape


@pytest.mark.parametrize(
    "cls,expected_m",
    [("6A", 2), ("6B", 6)],
)
def test_umbral_shift_from_CDH_Table1(cls: str, expected_m: int) -> None:
    """Umbral shifts m_{6A} = 2, m_{6B} = 6 from CDH 2014 Table 1."""
    assert umbral_shift_order6(cls) == expected_m


@pytest.mark.parametrize(
    "cls,expected_chi",
    [("6A", -1), ("6B", 1)],
)
def test_chi23_from_ATLAS(cls: str, expected_chi: int) -> None:
    """chi_{23}(6A) = -1, chi_{23}(6B) = +1 from ATLAS p. 96."""
    assert character_chi23_order6(cls) == expected_chi


# ----------------------------------------------------------------------
# Wave 15: pentagon-hbar^3 cocycle class in H^3(Z/6, U(1)) = Z/6
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "cls,expected_class",
    [("6A", 2), ("6B", 3)],
)
def test_cocycle_class_mod6(cls: str, expected_class: int) -> None:
    """Cocycle class in Z/6: [coc(6A)] = 2, [coc(6B)] = 3."""
    assert cocycle_class_order6(cls) == expected_class


@pytest.mark.parametrize("cls", ["6A", "6B"])
def test_bockstein_CRT_consistency(cls: str) -> None:
    """Cocycle class is consistent with CRT Z/6 = Z/2 x Z/3 decomposition."""
    assert restriction_bockstein_consistency(cls)


def test_universal_identity_match_mod6() -> None:
    """[coc(6A)] + [coc(6B)] = 5 = -1 mod 6 matches universal identity."""
    assert pentagon_hbar3_cocycle_sum_order6() == 5


def test_full_distinguishability_surface() -> None:
    """The assembled 6A-vs-6B surface passes all consistency checks."""
    report = distinguishability_6A_vs_6B()
    assert set(report["classes"].keys()) == {"6A", "6B"}
    for cls in ("6A", "6B"):
        entry = report["classes"][cls]
        assert entry["bockstein_consistent"]
    assert report["universal_identity_match"]
    assert report["pentagon_hbar3_sum_mod6"] == 5
    assert report["universal_identity_residue_minus1_mod6"] == 5


# ----------------------------------------------------------------------
# Wave 15: umbral phase orders and Miki-mode phases
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "cls,expected_order",
    [("6A", 12), ("6B", 4)],
)
def test_umbral_phase_order(cls: str, expected_order: int) -> None:
    """Phase exp(2 pi i m_sigma / 24): order(6A) = 12, order(6B) = 4.

    lcm(12, 4) = 12 exhausts H^2(M_24, U(1)) = Z/12.
    """
    assert umbral_phase_order(cls) == expected_order


def test_umbral_phase_orders_span_Z_mod_12() -> None:
    """lcm of umbral phase orders for {6A, 6B} spans the full Z/12."""
    from math import lcm

    assert lcm(umbral_phase_order("6A"), umbral_phase_order("6B")) == 12


@pytest.mark.parametrize(
    "cls,r,expected_phase",
    [
        ("6A", 1, 2),
        ("6A", 6, 12),
        ("6A", 12, 0),
        ("6B", 1, 6),
        ("6B", 2, 12),
        ("6B", 4, 0),
    ],
)
def test_phase_numerators_mod24(cls: str, r: int, expected_phase: int) -> None:
    """r * m_sigma mod 24 for Miki mode r."""
    assert m_sigma_mod24_phase(cls, r) == expected_phase


# ----------------------------------------------------------------------
# Cross-cutting: 6A vs 6B classes are genuinely distinct
# ----------------------------------------------------------------------


def test_6A_and_6B_are_distinct() -> None:
    """Every characteristic distinguishes 6A from 6B."""
    assert order6_cycle_shape("6A") != order6_cycle_shape("6B")
    assert umbral_shift_order6("6A") != umbral_shift_order6("6B")
    assert character_chi23_order6("6A") != character_chi23_order6("6B")
    assert cocycle_class_order6("6A") != cocycle_class_order6("6B")
    assert umbral_phase_order("6A") != umbral_phase_order("6B")
