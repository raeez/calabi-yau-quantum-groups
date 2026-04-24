"""Residual gate for the C3 renormalised hCS-to-Hall extension.

The fixed abelian theorem proves only the positive torus-fixed finite-mode
shuffle chart.  This module records the extra gates needed before that chart
can be promoted to a map from the full Costello-Gwilliam/Costello-Li
renormalised hCS factorisation algebra to the oriented critical CoHA.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, FrozenSet, Iterable, Tuple


class ResidualStrength(IntEnum):
    """Increasing strength of the residual C3 theta gate."""

    NO_FIXED_CHART = 0
    FIXED_FINITE_MODE = 1
    RENORMALISED_LOCAL_CHART = 2
    DWR_DESCENDED_COMPARISON = 3


@dataclass(frozen=True)
class ResidualGate:
    key: str
    obstruction: str
    statement: str


GATES: Dict[str, ResidualGate] = {
    "fixed_shuffle_chart": ResidualGate(
        "fixed_shuffle_chart",
        "o_theta^fp,+",
        "positive torus-fixed abelian finite-mode shuffle map to CoHA(C3)=Y^+",
    ),
    "anomaly_free_qme": ResidualGate(
        "anomaly_free_qme",
        "o_QME",
        "all-scale hCS RG/QME package with the Costello-Li anomaly killed",
    ),
    "nuclear_continuity": ResidualGate(
        "nuclear_continuity",
        "o_theta^ren",
        "LF/DFS and charge-completed topologies make the transfer continuous",
    ),
    "renormalised_transfer": ResidualGate(
        "renormalised_transfer",
        "o_theta^ren",
        "BV/Feynman localization map is defined on all renormalised observables",
    ),
    "differential_compatibility": ResidualGate(
        "differential_compatibility",
        "o_theta^ren",
        "the transfer intertwines Q_hCS+{I[L],-}+hbar Delta_L with the Hall differential",
    ),
    "mc_multiplicativity": ResidualGate(
        "mc_multiplicativity",
        "o_theta^ren",
        "Maurer-Cartan, BV bracket, and product coherences hold on the full chart",
    ),
    "dwr_descent": ResidualGate(
        "dwr_descent",
        "o_theta^des",
        "the chart maps extend to a coherent DWR/Ran comparison family",
    ),
}

FINITE_FIXED_GATES: Tuple[str, ...] = ("fixed_shuffle_chart",)

RENORMALISED_LOCAL_GATES: Tuple[str, ...] = FINITE_FIXED_GATES + (
    "anomaly_free_qme",
    "nuclear_continuity",
    "renormalised_transfer",
    "differential_compatibility",
    "mc_multiplicativity",
)

DWR_DESCENT_GATES: Tuple[str, ...] = RENORMALISED_LOCAL_GATES + (
    "dwr_descent",
)

TARGETS: Dict[str, Tuple[str, ...]] = {
    "finite_fixed_projection": FINITE_FIXED_GATES,
    "renormalised_local_chart": RENORMALISED_LOCAL_GATES,
    "dwr_descended_comparison": DWR_DESCENT_GATES,
}


@dataclass(frozen=True)
class ResidualDatum:
    supplied: FrozenSet[str]

    def missing_for(self, target: str) -> Tuple[ResidualGate, ...]:
        required = TARGETS[target]
        return tuple(GATES[key] for key in required if key not in self.supplied)

    def closes(self, target: str) -> bool:
        return not self.missing_for(target)

    def with_gates(self, *keys: str) -> "ResidualDatum":
        unknown = tuple(key for key in keys if key not in GATES)
        if unknown:
            raise KeyError(f"unknown residual gate(s): {unknown!r}")
        return ResidualDatum(self.supplied.union(keys))

    def strength(self) -> ResidualStrength:
        if self.closes("dwr_descended_comparison"):
            return ResidualStrength.DWR_DESCENDED_COMPARISON
        if self.closes("renormalised_local_chart"):
            return ResidualStrength.RENORMALISED_LOCAL_CHART
        if self.closes("finite_fixed_projection"):
            return ResidualStrength.FIXED_FINITE_MODE
        return ResidualStrength.NO_FIXED_CHART

    def residual_obstructions(self) -> Tuple[str, ...]:
        residual = []
        if not self.closes("finite_fixed_projection"):
            residual.append("o_theta^fp,+")
        if not self.closes("renormalised_local_chart"):
            residual.append("o_theta^ren")
        if not self.closes("dwr_descended_comparison"):
            residual.append("o_theta^des")
        return tuple(residual)


def fixed_finite_chart() -> ResidualDatum:
    return ResidualDatum(frozenset(FINITE_FIXED_GATES))


def renormalised_local_chart() -> ResidualDatum:
    return ResidualDatum(frozenset(RENORMALISED_LOCAL_GATES))


def dwr_descended_comparison() -> ResidualDatum:
    return ResidualDatum(frozenset(DWR_DESCENT_GATES))


def monotone_strength_chain(data: Iterable[ResidualDatum]) -> Tuple[ResidualStrength, ...]:
    strengths = tuple(datum.strength() for datum in data)
    if any(left > right for left, right in zip(strengths, strengths[1:])):
        raise AssertionError(f"residual strength decreased: {strengths!r}")
    return strengths


__all__ = [
    "DWR_DESCENT_GATES",
    "FINITE_FIXED_GATES",
    "GATES",
    "RENORMALISED_LOCAL_GATES",
    "ResidualDatum",
    "ResidualGate",
    "ResidualStrength",
    "TARGETS",
    "dwr_descended_comparison",
    "fixed_finite_chart",
    "monotone_strength_chain",
    "renormalised_local_chart",
]
