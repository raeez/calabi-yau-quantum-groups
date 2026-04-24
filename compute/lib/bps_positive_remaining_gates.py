"""Executable gates for the remaining BPS-positive point obligations.

The chambered BPS positive geometry source object and the residual
derived zero-fiber schema are already finite-first.  This module records
the stricter point-construction gates for the five named closed
substacks:

* quintic ExCert;
* Schoen/banana compact Hall gluing;
* raw K3 x E Hall-Borcherds radical;
* external theta package comparison;
* compact hCS-to-Hall localization.

Every gate is exact as a finite witness predicate.  A gate closes only
when each named coordinate is supplied.  Supplying a coordinate here is
the executable proxy for a computed vanishing certificate in the named
geometry; it is not inferred from placeholder zeroes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Iterable, Literal, Mapping, Tuple


QUINTIC_EXCERT_COORDINATES: Tuple[str, ...] = (
    "Z_period_isolation",
    "support_Q",
    "active_sector",
    "HN_filtration_table",
    "hall_lower_saturation",
    "extension_closed_ideal",
    "ptvv_critical_atlas",
    "orientation_square_root",
    "vanishing_cycle_TS",
    "motivic_target",
    "realization_maps",
    "ML_transition",
    "T_eq_mode",
)

SCHOEN_BANANA_GLUING_COORDINATES: Tuple[str, ...] = (
    "semistable_restriction",
    "charge_pushforward_null_fiber",
    "beck_chevalley",
    "relative_orientation",
    "HN_overlap",
    "motivic_overlap",
    "hall_lower_saturation",
    "KS_monodromy",
    "pro_continuity",
)

K3E_HALL_BORCHERDS_RADICAL_COORDINATES: Tuple[str, ...] = (
    "pairing_kernel",
    "orientation_character",
    "protected_integration",
    "primitive_bracket",
    "Serre_imaginary_relations",
    "Hopf_pairing",
    "completion_separatedness",
)

THETA_COMPARISON_COORDINATES: Tuple[str, ...] = (
    "hall_joint_holonomy",
    "package_existence",
    "core_charge_identification",
    "wall_function_identification",
    "orientation_half_tate_match",
    "locality_comparison",
    "multiplication_comparison",
    "pro_saturation",
)

THETA_PACKAGE_COORDINATES: Mapping[str, Tuple[str, ...]] = {
    "broken_line": (
        "local_finiteness",
        "identity_joints",
        "height_growth",
        "finite_bending",
        "orientation_match",
        "triangularity",
        "saturated_labels",
    ),
    "GHKK": (
        "seed_atlas",
        "scattering_identification",
        "EGM_or_basis",
        "upper_algebra_target",
        "orientation_skew_form",
        "mutation_compatibility",
        "completion_compatibility",
    ),
    "GMN": (
        "spectral_cover",
        "period_identification",
        "sector_data",
        "detour_sums",
        "two_d_four_d_wall_crossing",
        "halo_hall_identification",
        "framed_lines",
        "spin_orientation",
        "abelianization",
        "OPE_closure",
        "completion_compatibility",
    ),
    "Hall_framed": (
        "framed_objects",
        "framed_critical_stacks",
        "orientation_transport",
        "framed_hall_action",
        "finite_truncation",
        "triangularity",
        "OPE_Hall_compatibility",
        "realization_compatibility",
    ),
}

HCS_HALL_LOCALIZATION_COORDINATES: Tuple[str, ...] = (
    "omega_QME",
    "omega_anom",
    "omega_gauge_fixing",
    "omega_DWR_source_target",
    "omega_critical_atlas",
    "omega_stationary_phase",
    "omega_vertex_quasi_iso",
    "o_MC",
    "o_or_rel",
    "o_gr",
    "o_TS",
    "o_fact",
    "o_cs",
    "o_wedge",
)

REMAINING_POINT_GATES: Mapping[str, Tuple[str, ...]] = {
    "quintic_excert": QUINTIC_EXCERT_COORDINATES,
    "schoen_banana_gluing": SCHOEN_BANANA_GLUING_COORDINATES,
    "k3e_raw_radical": K3E_HALL_BORCHERDS_RADICAL_COORDINATES,
    "theta_comparison": THETA_COMPARISON_COORDINATES,
    "hcs_named_zero_fiber": HCS_HALL_LOCALIZATION_COORDINATES,
}


@dataclass(frozen=True)
class CoordinateGateReport:
    """Exact finite report for one named point-construction gate."""

    name: str
    required_coordinates: Tuple[str, ...]
    supplied_coordinates: Tuple[str, ...]
    missing_coordinates: Tuple[str, ...]
    unknown_coordinates: Tuple[str, ...]

    @property
    def closed(self) -> bool:
        return not self.missing_coordinates and not self.unknown_coordinates

    @property
    def status(self) -> str:
        return "CLOSED_FROM_COORDINATES" if self.closed else "OPEN_COORDINATE_GATE"


def _normalize_supplied(supplied: Iterable[str]) -> Tuple[str, ...]:
    return tuple(dict.fromkeys(supplied))


def evaluate_coordinate_gate(
    name: str,
    required_coordinates: Tuple[str, ...],
    supplied_coordinates: Iterable[str] = (),
) -> CoordinateGateReport:
    """Evaluate one coordinate gate without inferring omitted data."""

    supplied = _normalize_supplied(supplied_coordinates)
    required_set = set(required_coordinates)
    supplied_set = set(supplied)
    missing = tuple(
        coordinate
        for coordinate in required_coordinates
        if coordinate not in supplied_set
    )
    unknown = tuple(
        coordinate
        for coordinate in supplied
        if coordinate not in required_set
    )
    return CoordinateGateReport(
        name=name,
        required_coordinates=required_coordinates,
        supplied_coordinates=supplied,
        missing_coordinates=missing,
        unknown_coordinates=unknown,
    )


ThetaPackage = Literal["broken_line", "GHKK", "GMN", "Hall_framed"]


def theta_package_required_coordinates(package: ThetaPackage) -> Tuple[str, ...]:
    """Return the full external theta package plus comparison vector."""

    return THETA_PACKAGE_COORDINATES[package] + THETA_COMPARISON_COORDINATES


def evaluate_theta_package_gate(
    package: ThetaPackage,
    supplied_coordinates: Iterable[str] = (),
) -> CoordinateGateReport:
    """Evaluate a concrete external theta comparison package."""

    return evaluate_coordinate_gate(
        f"theta_{package}",
        theta_package_required_coordinates(package),
        supplied_coordinates,
    )


@dataclass(frozen=True)
class RemainingPointWitnesses:
    """Coordinate witnesses supplied for all five residual point gates."""

    quintic_excert: FrozenSet[str] = frozenset()
    schoen_banana_gluing: FrozenSet[str] = frozenset()
    k3e_raw_radical: FrozenSet[str] = frozenset()
    theta_comparison: FrozenSet[str] = frozenset()
    hcs_named_zero_fiber: FrozenSet[str] = frozenset()

    def supplied_for(self, gate_name: str) -> FrozenSet[str]:
        if gate_name not in REMAINING_POINT_GATES:
            raise KeyError(f"unknown remaining point gate: {gate_name}")
        return getattr(self, gate_name)


def evaluate_remaining_point_gates(
    witnesses: RemainingPointWitnesses,
) -> Tuple[CoordinateGateReport, ...]:
    """Evaluate all remaining BPS-positive point gates."""

    return tuple(
        evaluate_coordinate_gate(name, required, witnesses.supplied_for(name))
        for name, required in REMAINING_POINT_GATES.items()
    )


def unresolved_point_gates(witnesses: RemainingPointWitnesses) -> Tuple[str, ...]:
    """Return the names of point gates not closed by supplied witnesses."""

    return tuple(
        report.name
        for report in evaluate_remaining_point_gates(witnesses)
        if not report.closed
    )


def complete_remaining_point_witnesses() -> RemainingPointWitnesses:
    """Return the formal all-coordinate witness package used in tests."""

    return RemainingPointWitnesses(
        quintic_excert=frozenset(QUINTIC_EXCERT_COORDINATES),
        schoen_banana_gluing=frozenset(SCHOEN_BANANA_GLUING_COORDINATES),
        k3e_raw_radical=frozenset(K3E_HALL_BORCHERDS_RADICAL_COORDINATES),
        theta_comparison=frozenset(THETA_COMPARISON_COORDINATES),
        hcs_named_zero_fiber=frozenset(HCS_HALL_LOCALIZATION_COORDINATES),
    )


__all__ = [
    "CoordinateGateReport",
    "HCS_HALL_LOCALIZATION_COORDINATES",
    "K3E_HALL_BORCHERDS_RADICAL_COORDINATES",
    "QUINTIC_EXCERT_COORDINATES",
    "REMAINING_POINT_GATES",
    "RemainingPointWitnesses",
    "SCHOEN_BANANA_GLUING_COORDINATES",
    "THETA_COMPARISON_COORDINATES",
    "THETA_PACKAGE_COORDINATES",
    "complete_remaining_point_witnesses",
    "evaluate_coordinate_gate",
    "evaluate_remaining_point_gates",
    "evaluate_theta_package_gate",
    "theta_package_required_coordinates",
    "unresolved_point_gates",
]
