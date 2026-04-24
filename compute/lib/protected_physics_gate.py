"""Typed gate for protected BPS-to-chiral/BKM physics.

This module is a guard, not a construction of the missing functor.  It records
which typed maps must be supplied before a protected index, BPS Hilbert space,
topological-string partition function, black-hole count, or holographic trace
can be promoted from a physics witness to a chiral or BKM statement.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Dict, FrozenSet, Tuple


class ProtectedPhysicsShortcutError(ValueError):
    """Raised when physics evidence is promoted past its typed support."""


class EpistemicStatus(IntEnum):
    """Increasing epistemic strength of the supplied evidence."""

    METAPHOR = 0
    HEURISTIC = 1
    CONJECTURAL = 2
    COMPUTED = 3
    THEOREM = 4


class EvidenceKind(str, Enum):
    """Sources that often appear in the protected physics lane."""

    PROTECTED_INDEX = "protected_index"
    BPS_HILBERT_SPACE = "bps_hilbert_space"
    TOPOLOGICAL_STRING_PARTITION = "topological_string_partition"
    BLACK_HOLE_COUNT = "black_hole_count"
    HOLOGRAPHIC_TRACE = "holographic_trace"
    BPS_CATEGORY_WITH_HALL = "bps_category_with_hall"
    HALL_BKM_DATUM = "hall_bkm_datum"


class ProtectedClaimLevel(IntEnum):
    """Increasing claim strength allowed by the protected comparison data."""

    WITNESS_ONLY = 0
    PROTECTED_INDEX = 1
    CHIRAL_CHARACTER = 2
    CHAMBER_INDEPENDENT_TRACE = 3
    HALL_TO_CHIRAL_FUNCTOR = 4
    BKM_CHIRAL_TRACE_PACKAGE = 5


@dataclass(frozen=True)
class ProtectedGate:
    key: str
    layer: str
    statement: str
    failure_mode: str


PROTECTED_GATES: Dict[str, ProtectedGate] = {
    "protected_sector_projection": ProtectedGate(
        "protected_sector_projection",
        "physics",
        "Q-cohomology or protected-sector idempotent is fixed before tracing",
        "full Hilbert-space dimension is being used as a protected index",
    ),
    "orientation_line_trivialization": ProtectedGate(
        "orientation_line_trivialization",
        "DT/Hall",
        "the BPS orientation line is trivialized compatibly with convolution",
        "without the orientation line, the BPS index and chiral trace live in different twisted K-groups",
    ),
    "charge_lattice_isometry": ProtectedGate(
        "charge_lattice_isometry",
        "lattice",
        "BPS charges are identified with the Hall/BKM root lattice, preserving pairings",
        "charge labels are being read as roots without a pairing-preserving map",
    ),
    "index_character_map": ProtectedGate(
        "index_character_map",
        "trace",
        "K_0(BPS, orientation) maps to the graded chiral character group",
        "a numerical BPS index is being identified with a chiral character",
    ),
    "wall_crossing_coherence": ProtectedGate(
        "wall_crossing_coherence",
        "stability",
        "KS wall-crossing maps to MC gauge equivalence of the chiral datum",
        "a chamber-dependent BPS count is being used as a global invariant",
    ),
    "hall_product_ope_functor": ProtectedGate(
        "hall_product_ope_functor",
        "functor",
        "an exact charge-preserving functor carries Hall convolution to boundary OPE",
        "a trace or partition function is being promoted to an algebra functor",
    ),
    "drinfeld_double_bkm_map": ProtectedGate(
        "drinfeld_double_bkm_map",
        "BKM",
        "the Hall-Drinfeld double is mapped to the BKM bialgebra datum",
        "positive-half Hall data or physics counts are being treated as a BKM algebra",
    ),
    "borcherds_denominator_normalization": ProtectedGate(
        "borcherds_denominator_normalization",
        "BKM",
        "the denominator product is normalized by kappa_BKM(Phi_N)=c_N(0)/2",
        "a partition-function weight is being substituted for the Borcherds weight",
    ),
}


REQUIRED_GATES: Dict[ProtectedClaimLevel, Tuple[str, ...]] = {
    ProtectedClaimLevel.WITNESS_ONLY: (),
    ProtectedClaimLevel.PROTECTED_INDEX: (
        "protected_sector_projection",
        "orientation_line_trivialization",
    ),
    ProtectedClaimLevel.CHIRAL_CHARACTER: (
        "protected_sector_projection",
        "orientation_line_trivialization",
        "charge_lattice_isometry",
        "index_character_map",
    ),
    ProtectedClaimLevel.CHAMBER_INDEPENDENT_TRACE: (
        "protected_sector_projection",
        "orientation_line_trivialization",
        "charge_lattice_isometry",
        "index_character_map",
        "wall_crossing_coherence",
    ),
    ProtectedClaimLevel.HALL_TO_CHIRAL_FUNCTOR: (
        "protected_sector_projection",
        "orientation_line_trivialization",
        "charge_lattice_isometry",
        "index_character_map",
        "wall_crossing_coherence",
        "hall_product_ope_functor",
    ),
    ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE: (
        "protected_sector_projection",
        "orientation_line_trivialization",
        "charge_lattice_isometry",
        "index_character_map",
        "wall_crossing_coherence",
        "hall_product_ope_functor",
        "drinfeld_double_bkm_map",
        "borcherds_denominator_normalization",
    ),
}

NUMERICAL_PHYSICS_EVIDENCE: FrozenSet[EvidenceKind] = frozenset(
    {
        EvidenceKind.PROTECTED_INDEX,
        EvidenceKind.TOPOLOGICAL_STRING_PARTITION,
        EvidenceKind.BLACK_HOLE_COUNT,
        EvidenceKind.HOLOGRAPHIC_TRACE,
    }
)


@dataclass(frozen=True)
class ProtectedEvidence:
    """A physics-lane datum before any promotion to chiral/BKM mathematics."""

    kind: EvidenceKind
    status: EpistemicStatus
    description: str = ""


@dataclass(frozen=True)
class ProtectedClaim:
    """A validated protected claim and the gates used to obtain it."""

    evidence: ProtectedEvidence
    level: ProtectedClaimLevel
    gates: Tuple[ProtectedGate, ...]


@dataclass(frozen=True)
class ProtectedBridgePackage:
    """Typed package for transferring protected data to the chiral/BKM side."""

    name: str
    supplied: FrozenSet[str]

    def missing_for(self, level: ProtectedClaimLevel) -> Tuple[ProtectedGate, ...]:
        required = REQUIRED_GATES[level]
        return tuple(PROTECTED_GATES[key] for key in required if key not in self.supplied)

    def supports(self, level: ProtectedClaimLevel) -> bool:
        return not self.missing_for(level)

    def with_gates(self, *keys: str) -> "ProtectedBridgePackage":
        unknown = tuple(key for key in keys if key not in PROTECTED_GATES)
        if unknown:
            raise KeyError(f"unknown protected physics gate(s): {unknown!r}")
        return ProtectedBridgePackage(self.name, self.supplied.union(keys))

    def strength(self) -> ProtectedClaimLevel:
        for level in reversed(tuple(ProtectedClaimLevel)):
            if self.supports(level):
                return level
        return ProtectedClaimLevel.WITNESS_ONLY


def witness_only_package(name: str = "physics witness only") -> ProtectedBridgePackage:
    return ProtectedBridgePackage(name, frozenset())


def protected_trace_package(name: str = "protected trace package") -> ProtectedBridgePackage:
    return ProtectedBridgePackage(
        name,
        frozenset(REQUIRED_GATES[ProtectedClaimLevel.CHAMBER_INDEPENDENT_TRACE]),
    )


def protected_bkm_functor_package(
    name: str = "protected BPS-to-chiral/BKM package",
) -> ProtectedBridgePackage:
    return ProtectedBridgePackage(
        name,
        frozenset(REQUIRED_GATES[ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE]),
    )


def validate_promotion(
    evidence: ProtectedEvidence,
    level: ProtectedClaimLevel,
    package: ProtectedBridgePackage,
) -> ProtectedClaim:
    """Validate promotion of physics evidence to a typed protected claim.

    Numerical physics evidence can support protected index/character claims only
    after the trace gates are present.  It never proves a Hall-to-chiral functor
    or a BKM algebra by itself; those claims require categorical Hall evidence.
    """

    if evidence.status <= EpistemicStatus.HEURISTIC and level > ProtectedClaimLevel.WITNESS_ONLY:
        raise ProtectedPhysicsShortcutError(
            f"{evidence.kind.value} with status {evidence.status.name} remains witness-only"
        )

    if (
        evidence.kind in NUMERICAL_PHYSICS_EVIDENCE
        and level >= ProtectedClaimLevel.HALL_TO_CHIRAL_FUNCTOR
    ):
        raise ProtectedPhysicsShortcutError(
            f"{evidence.kind.value} is numerical physics evidence, not an algebra functor"
        )

    if (
        evidence.kind == EvidenceKind.BPS_HILBERT_SPACE
        and level >= ProtectedClaimLevel.CHIRAL_CHARACTER
    ):
        raise ProtectedPhysicsShortcutError(
            "a BPS Hilbert space must first be replaced by its protected index"
        )

    missing = package.missing_for(level)
    if missing:
        modes = tuple(gate.failure_mode for gate in missing)
        raise ProtectedPhysicsShortcutError(
            f"{package.name} lacks gates for {level.name}: {modes!r}"
        )

    return ProtectedClaim(
        evidence=evidence,
        level=level,
        gates=tuple(PROTECTED_GATES[key] for key in REQUIRED_GATES[level]),
    )


__all__ = [
    "EpistemicStatus",
    "EvidenceKind",
    "ProtectedBridgePackage",
    "ProtectedClaim",
    "ProtectedClaimLevel",
    "ProtectedEvidence",
    "ProtectedGate",
    "ProtectedPhysicsShortcutError",
    "PROTECTED_GATES",
    "REQUIRED_GATES",
    "protected_bkm_functor_package",
    "protected_trace_package",
    "validate_promotion",
    "witness_only_package",
]
