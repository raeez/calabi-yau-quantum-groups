"""Finite gate oracle for the CY3 hCS-to-Hall DWR descent problem.

The fixed abelian C3 shuffle chart verifies only the projected local
component ``o_theta^{fp,+}``.  It does not construct the renormalised
hCS-to-Hall comparison map, does not extend maps to all Cech/Ran
simplices, and does not kill the orientation, grading/Tate,
Thom-Sebastiani, or factorisation obstruction classes.

This module records the finite implication lattice used by the
2026-04-24 descent audit.  It is a checkable gate, not a proof of the
comparison map.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Iterable, Tuple


class Gate(str, Enum):
    """Atomic gates for the DWR/Ran hCS-to-Hall descent criterion."""

    FIXED_C3_CHART = "fixed_c3_chart"
    SV_POSITIVE_HALF = "sv_positive_half"
    DRINFELD_DOUBLE_FOCK = "drinfeld_double_fock"
    DWR_GOOD_COVER = "dwr_good_cover"
    FULL_RENORMALISED_CHART_MAPS = "full_renormalised_chart_maps"
    MAPS_ON_ALL_SIMPLICES = "maps_on_all_simplices"
    CECH_MC_ZERO = "cech_mc_zero"
    VERTEX_QUASI_ISOMORPHISMS = "vertex_quasi_isomorphisms"
    H0_INVERTIBLE_ON_NERVE = "h0_invertible_on_nerve"
    RELATIVE_ORIENTATION_COCYCLE_ZERO = "relative_orientation_cocycle_zero"
    GRADING_TATE_COMPATIBLE = "grading_tate_compatible"
    THOM_SEBASTIANI_COHERENT = "thom_sebastiani_coherent"
    FACTORIZATION_PRODUCT_COMPATIBLE = "factorization_product_compatible"
    COMPLETIONS_CONTINUOUS = "completions_continuous"
    COMPACT_SUPPORT_REFINEMENT_COMPATIBLE = "compact_support_refinement_compatible"
    HALL_SIDE_ORIENTATION_TRIVIAL = "hall_side_orientation_trivial"
    HALL_SIDE_TS_ASSOCIATIVE = "hall_side_ts_associative"


REQUIRED_DESCENT_GATES: FrozenSet[Gate] = frozenset(
    {
        Gate.DWR_GOOD_COVER,
        Gate.FULL_RENORMALISED_CHART_MAPS,
        Gate.MAPS_ON_ALL_SIMPLICES,
        Gate.CECH_MC_ZERO,
        Gate.VERTEX_QUASI_ISOMORPHISMS,
        Gate.H0_INVERTIBLE_ON_NERVE,
        Gate.RELATIVE_ORIENTATION_COCYCLE_ZERO,
        Gate.GRADING_TATE_COMPATIBLE,
        Gate.THOM_SEBASTIANI_COHERENT,
        Gate.FACTORIZATION_PRODUCT_COMPATIBLE,
        Gate.COMPLETIONS_CONTINUOUS,
        Gate.COMPACT_SUPPORT_REFINEMENT_COMPATIBLE,
    }
)


SHORTCUTS: Tuple[Tuple[FrozenSet[Gate], str], ...] = (
    (
        frozenset({Gate.FIXED_C3_CHART}),
        "fixed C3 chart kills only o_theta^{fp,+}, not descent",
    ),
    (
        frozenset({Gate.SV_POSITIVE_HALF}),
        "CoHA(C3)=Y^+ is Hall-side cohomology, not an hCS-to-Hall map",
    ),
    (
        frozenset({Gate.HALL_SIDE_ORIENTATION_TRIVIAL}),
        "Hall-side orientation triviality is not relative comparison orientation",
    ),
    (
        frozenset({Gate.HALL_SIDE_TS_ASSOCIATIVE}),
        "Hall-side TS associativity is not comparison TS coherence",
    ),
    (
        frozenset({Gate.SV_POSITIVE_HALF, Gate.DRINFELD_DOUBLE_FOCK}),
        "the W shadow is typed after the double/Fock route, not DWR descent",
    ),
)


@dataclass(frozen=True)
class DescentGateState:
    """Finite state of a proposed DWR descent package."""

    gates: FrozenSet[Gate]

    @classmethod
    def from_iterable(cls, gates: Iterable[Gate | str]) -> "DescentGateState":
        return cls(frozenset(Gate(g) for g in gates))

    def missing_descent_gates(self) -> FrozenSet[Gate]:
        return REQUIRED_DESCENT_GATES.difference(self.gates)

    def has_descent(self) -> bool:
        """Exactly the finite gate form of the chapter's descent criterion."""
        return not self.missing_descent_gates()

    def fixed_chart_only(self) -> bool:
        return self.gates == frozenset({Gate.FIXED_C3_CHART})

    def has_w_shadow_route(self) -> bool:
        """The admissible route to W_{1+infty}; not a descent condition."""
        return {
            Gate.SV_POSITIVE_HALF,
            Gate.DRINFELD_DOUBLE_FOCK,
        }.issubset(self.gates)

    def has_direct_w_shortcut(self) -> bool:
        """No direct CoHA(C3)->W shortcut is admitted by the manuscript."""
        return Gate.SV_POSITIVE_HALF in self.gates and Gate.DRINFELD_DOUBLE_FOCK not in self.gates

    def shortcut_reasons(self) -> Tuple[str, ...]:
        reasons = []
        for shortcut_gates, reason in SHORTCUTS:
            if shortcut_gates.issubset(self.gates) and not self.has_descent():
                reasons.append(reason)
        if self.has_direct_w_shortcut():
            reasons.append("direct CoHA(C3)->W shortcut is forbidden")
        return tuple(reasons)

    def report(self) -> dict[str, object]:
        missing = tuple(sorted(g.value for g in self.missing_descent_gates()))
        return {
            "has_descent": self.has_descent(),
            "missing_descent_gates": missing,
            "has_w_shadow_route": self.has_w_shadow_route(),
            "shortcut_reasons": self.shortcut_reasons(),
        }


def complete_descent_state() -> DescentGateState:
    """Return the minimal finite state that passes DWR descent."""
    return DescentGateState(REQUIRED_DESCENT_GATES)


__all__ = [
    "DescentGateState",
    "Gate",
    "REQUIRED_DESCENT_GATES",
    "SHORTCUTS",
    "complete_descent_state",
]
