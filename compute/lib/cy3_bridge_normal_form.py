"""Executable normal form for the CY3 chain-level bridge.

The module is deliberately modest: it does not construct the missing
hCS-to-Hall map.  It records the typed gates that must be supplied before a
claim may move from normal form to local C3 closure, global descent, BKM, or
protected physics.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, FrozenSet, Iterable, Sequence, Tuple


class BridgeShortcutError(ValueError):
    """Raised when a bridge path skips a typed comparison gate."""


class BridgeStrength(IntEnum):
    """Increasing proof strength for CY3 bridge claims."""

    NORMAL_FORM_ONLY = 0
    LOCAL_C3_TO_YPLUS = 1
    GLOBAL_HCS_HALL = 2
    HALL_BORCHERDS_BKM = 3
    PROTECTED_PHYSICS = 4


@dataclass(frozen=True)
class Gate:
    key: str
    layer: str
    statement: str


GATES: Dict[str, Gate] = {
    "qme": Gate(
        "qme",
        "BV/BRST",
        "all-scale hCS QME/RG package with anomaly cancelled",
    ),
    "ordered_e3_bar": Gate(
        "ordered_e3_bar",
        "chiral CE",
        "completed ordered chiral E3 bar; no exterior-CE shortcut",
    ),
    "stage1_formality": Gate(
        "stage1_formality",
        "factorization",
        "Stage-1 E3 formality point and Costello-Li holomorphic witness",
    ),
    "factorization_envelope": Gate(
        "factorization_envelope",
        "factorization",
        "Costello-Gwilliam factorization envelope of the E3 algebra",
    ),
    "hcs_hall_chart_map": Gate(
        "hcs_hall_chart_map",
        "comparison",
        "continuous multiplicative chartwise hCS-to-Hall chain map",
    ),
    "sv_positive_half": Gate(
        "sv_positive_half",
        "CoHA/Yangian",
        "Schiffmann-Vasserot identification CoHA(C3)=Y^+",
    ),
    "drinfeld_double_before_w": Gate(
        "drinfeld_double_before_w",
        "W-algebra",
        "W_{1+infty} is reached only after Drinfeld double/Fock passage",
    ),
    "dwr_cover": Gate(
        "dwr_cover",
        "descent",
        "Dolbeault-Weiss-Ran cover by Stein or toric C3 charts",
    ),
    "mc_descent": Gate(
        "mc_descent",
        "descent",
        "Maurer-Cartan descent equation for the comparison family",
    ),
    "orientation": Gate(
        "orientation",
        "descent",
        "KS/Joyce orientation compatibility",
    ),
    "grading_tate": Gate(
        "grading_tate",
        "descent",
        "cohomological grading and Tate twist compatibility",
    ),
    "thom_sebastiani": Gate(
        "thom_sebastiani",
        "descent",
        "Thom-Sebastiani compatibility on overlaps",
    ),
    "factorization_descent": Gate(
        "factorization_descent",
        "descent",
        "factorization compatibility on the full DWR nerve",
    ),
    "hall_borcherds_bialgebra": Gate(
        "hall_borcherds_bialgebra",
        "BKM",
        "Hall-Drinfeld double to BKM bialgebra datum",
    ),
    "borcherds_denominator_normalization": Gate(
        "borcherds_denominator_normalization",
        "BKM",
        "Borcherds product normalization kappa_BKM(Phi_N)=c_N(0)/2",
    ),
    "protected_bps_functor": Gate(
        "protected_bps_functor",
        "physics",
        "protected BPS-to-chiral/BKM comparison functor",
    ),
}

LOCAL_C3_GATES: Tuple[str, ...] = (
    "qme",
    "ordered_e3_bar",
    "stage1_formality",
    "factorization_envelope",
    "hcs_hall_chart_map",
    "sv_positive_half",
)

W_INFTY_GATES: Tuple[str, ...] = LOCAL_C3_GATES + (
    "drinfeld_double_before_w",
)

GLOBAL_HCS_HALL_GATES: Tuple[str, ...] = W_INFTY_GATES + (
    "dwr_cover",
    "mc_descent",
    "orientation",
    "grading_tate",
    "thom_sebastiani",
    "factorization_descent",
)

HALL_BORCHERDS_GATES: Tuple[str, ...] = GLOBAL_HCS_HALL_GATES + (
    "hall_borcherds_bialgebra",
    "borcherds_denominator_normalization",
)

PROTECTED_PHYSICS_GATES: Tuple[str, ...] = HALL_BORCHERDS_GATES + (
    "protected_bps_functor",
)

TARGETS: Dict[str, Tuple[str, ...]] = {
    "local_c3_to_yplus": LOCAL_C3_GATES,
    "w_infty_representation": W_INFTY_GATES,
    "global_hcs_hall": GLOBAL_HCS_HALL_GATES,
    "hall_borcherds_bkm": HALL_BORCHERDS_GATES,
    "protected_physics": PROTECTED_PHYSICS_GATES,
}

SEVEN_RIGIDIFICATIONS: Tuple[str, ...] = (
    "qme",
    "ordered_e3_bar",
    "stage1_formality",
    "hcs_hall_chart_map",
    "hall_borcherds_bialgebra",
    "protected_bps_functor",
    "factorization_descent",
)

TYPED_EDGES: FrozenSet[Tuple[str, str]] = frozenset(
    {
        ("BV_BRST", "chiral_CE"),
        ("chiral_CE", "factorization_algebra"),
        ("factorization_algebra", "hCS_observables"),
        ("hCS_observables", "CoHA"),
        ("CoHA", "Y_plus"),
        ("Y_plus", "Drinfeld_double"),
        ("Drinfeld_double", "W_1_infty"),
        ("Drinfeld_double", "Hall_Borcherds_bialgebra"),
        ("Hall_Borcherds_bialgebra", "BKM"),
        ("BKM", "protected_physics"),
    }
)


@dataclass(frozen=True)
class BridgeDatum:
    name: str
    supplied: FrozenSet[str]

    def missing_for(self, target: str) -> Tuple[Gate, ...]:
        required = TARGETS[target]
        return tuple(GATES[key] for key in required if key not in self.supplied)

    def closes(self, target: str) -> bool:
        return not self.missing_for(target)

    def with_gates(self, *keys: str) -> "BridgeDatum":
        unknown = tuple(key for key in keys if key not in GATES)
        if unknown:
            raise KeyError(f"unknown bridge gate(s): {unknown!r}")
        return BridgeDatum(self.name, self.supplied.union(keys))

    def strength(self) -> BridgeStrength:
        if self.closes("protected_physics"):
            return BridgeStrength.PROTECTED_PHYSICS
        if self.closes("hall_borcherds_bkm"):
            return BridgeStrength.HALL_BORCHERDS_BKM
        if self.closes("global_hcs_hall"):
            return BridgeStrength.GLOBAL_HCS_HALL
        if self.closes("local_c3_to_yplus"):
            return BridgeStrength.LOCAL_C3_TO_YPLUS
        return BridgeStrength.NORMAL_FORM_ONLY


def c3_local_datum(*, supply_hcs_hall_map: bool = False) -> BridgeDatum:
    supplied = {
        "qme",
        "ordered_e3_bar",
        "stage1_formality",
        "factorization_envelope",
        "sv_positive_half",
        "drinfeld_double_before_w",
    }
    if supply_hcs_hall_map:
        supplied.add("hcs_hall_chart_map")
    return BridgeDatum("C3 local bridge", frozenset(supplied))


def k3e_global_datum(
    *,
    supply_hcs_hall_map: bool = False,
    supply_dwr_descent: bool = False,
    supply_hall_borcherds: bool = False,
    supply_protected_physics: bool = False,
) -> BridgeDatum:
    datum = c3_local_datum(supply_hcs_hall_map=supply_hcs_hall_map)
    supplied = set(datum.supplied)
    if supply_dwr_descent:
        supplied.update(
            {
                "dwr_cover",
                "mc_descent",
                "orientation",
                "grading_tate",
                "thom_sebastiani",
                "factorization_descent",
            }
        )
    if supply_hall_borcherds:
        supplied.update(
            {
                "hall_borcherds_bialgebra",
                "borcherds_denominator_normalization",
            }
        )
    if supply_protected_physics:
        supplied.add("protected_bps_functor")
    return BridgeDatum("K3xE global bridge", frozenset(supplied))


def validate_typed_path(nodes: Sequence[str]) -> Tuple[Tuple[str, str], ...]:
    if len(nodes) < 2:
        return ()
    edges = tuple(zip(nodes, nodes[1:]))
    bad = tuple(edge for edge in edges if edge not in TYPED_EDGES)
    if bad:
        raise BridgeShortcutError(f"untyped bridge shortcut(s): {bad!r}")
    return edges


def monotone_strength_chain(data: Iterable[BridgeDatum]) -> Tuple[BridgeStrength, ...]:
    strengths = tuple(datum.strength() for datum in data)
    if any(a > b for a, b in zip(strengths, strengths[1:])):
        raise AssertionError(f"bridge strength decreased: {strengths!r}")
    return strengths


__all__ = [
    "BridgeDatum",
    "BridgeShortcutError",
    "BridgeStrength",
    "GATES",
    "SEVEN_RIGIDIFICATIONS",
    "TARGETS",
    "TYPED_EDGES",
    "c3_local_datum",
    "k3e_global_datum",
    "monotone_strength_chain",
    "validate_typed_path",
]
