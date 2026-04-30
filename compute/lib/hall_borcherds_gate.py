"""Executable gate for the Hall-Drinfeld-double to Borcherds comparison.

The gate separates three statements that are often conflated:

* the Borcherds weight identity
  kappa_BKM(Delta_5) = c_1(0) / 2 = 5;
* the K3 x E four-invariant spectrum
  (kappa_cat, kappa_ch_Heis, kappa_BKM, kappa_fiber) = (0, 3, 5, 24);
* the still-typed Hall/Borcherds comparison from an oriented critical
  CoHA and its Hall-Drinfeld double to the BKM denominator datum.

The first two are exact local checks.  The third is an implication gate:
it is closed only when the orientation, Hopf pairing, Drinfeld double,
denominator normalization, root-multiplicity map, and anti-shortcut
separations are all supplied as witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, Iterable, Tuple


def borcherds_weight_from_c0(c0: int) -> Fraction:
    """Return the Borcherds lift weight c0 / 2."""
    return Fraction(c0, 2)


@dataclass(frozen=True)
class DenominatorDatum:
    """Primitive denominator normalization data."""

    primitive_form: str
    input_constant_c0: int
    square_form: str
    source: str

    @property
    def kappa_BKM(self) -> Fraction:
        return borcherds_weight_from_c0(self.input_constant_c0)

    @property
    def square_weight(self) -> Fraction:
        return 2 * self.kappa_BKM


DELTA5_DATUM = DenominatorDatum(
    primitive_form="Delta_5",
    input_constant_c0=10,
    square_form="Phi_10 = Delta_5^2",
    source="Borcherds weight theorem with the Gritsenko-Nikulin Delta_5 normalization",
)


K3XE_INVARIANT_SPECTRUM: Dict[str, Fraction] = {
    "kappa_cat_total": Fraction(0),
    "kappa_ch_Heis": Fraction(3),
    "kappa_BKM_Delta_5": Fraction(5),
    "kappa_fiber_Mukai_rank": Fraction(24),
}


def k3xe_spectrum_tuple() -> Tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return the ordered K3 x E spectrum (0, 3, 5, 24)."""
    return (
        K3XE_INVARIANT_SPECTRUM["kappa_cat_total"],
        K3XE_INVARIANT_SPECTRUM["kappa_ch_Heis"],
        K3XE_INVARIANT_SPECTRUM["kappa_BKM_Delta_5"],
        K3XE_INVARIANT_SPECTRUM["kappa_fiber_Mukai_rank"],
    )


@dataclass(frozen=True)
class HallBorcherdsWitnesses:
    """Boolean witnesses required before the Hall/Borcherds bridge is closed."""

    oriented_critical_coha: bool = False
    hopf_pairing: bool = False
    drinfeld_double: bool = False
    denominator_normalization: bool = False
    root_multiplicity_map: bool = False
    k3xe_spectrum_separated: bool = False
    coha_positive_half_not_w: bool = False
    bkm_object_not_yangian: bool = False


REQUIRED_WITNESSES: Tuple[str, ...] = (
    "oriented_critical_coha",
    "hopf_pairing",
    "drinfeld_double",
    "denominator_normalization",
    "root_multiplicity_map",
    "k3xe_spectrum_separated",
    "coha_positive_half_not_w",
    "bkm_object_not_yangian",
)


@dataclass(frozen=True)
class GateReport:
    """Result of evaluating the comparison gate."""

    status: str
    closed: bool
    missing_witnesses: Tuple[str, ...]
    implications: Dict[str, bool]


def missing_witnesses(witnesses: HallBorcherdsWitnesses) -> Tuple[str, ...]:
    """List the witnesses not present in a Hall/Borcherds package."""
    return tuple(name for name in REQUIRED_WITNESSES if not getattr(witnesses, name))


def evaluate_gate(witnesses: HallBorcherdsWitnesses) -> GateReport:
    """Evaluate the Hall/Borcherds implication lattice."""
    missing = missing_witnesses(witnesses)
    implications = {
        "positive_half_constructed": witnesses.oriented_critical_coha,
        "drinfeld_double_constructed": (
            witnesses.oriented_critical_coha
            and witnesses.hopf_pairing
            and witnesses.drinfeld_double
        ),
        "denominator_weight_verified": (
            witnesses.denominator_normalization
            and DELTA5_DATUM.kappa_BKM == Fraction(5)
            and DELTA5_DATUM.square_weight == Fraction(10)
        ),
        "root_multiplicity_lane_available": (
            witnesses.denominator_normalization and witnesses.root_multiplicity_map
        ),
        "spectrum_not_used_as_bridge": witnesses.k3xe_spectrum_separated,
        "anti_shortcuts_cleared": (
            witnesses.coha_positive_half_not_w and witnesses.bkm_object_not_yangian
        ),
    }
    closed = not missing and all(implications.values())
    status = "CLOSED_FROM_WITNESSES" if closed else "OPEN_TYPED_GATE"
    return GateReport(status=status, closed=closed, missing_witnesses=missing, implications=implications)


@dataclass(frozen=True)
class RecognitionEnvelopeWitnesses:
    """Finite data separating the universal envelope from faithful recognition."""

    finite_compact_double: bool = False
    finite_borcherds_target: bool = False
    compact_source_packet: bool = False
    radical_isometry: bool = False
    serre_kernel_exact: bool = False
    green_adjoint_coproduct: bool = False
    primitive_center_reduction: bool = False
    associator_class_match: bool = False
    transition_compatible: bool = False


FINITE_DEFECT_WITNESSES: Dict[str, str] = {
    "R": "radical_isometry",
    "S": "serre_kernel_exact",
    "D": "green_adjoint_coproduct",
    "C": "primitive_center_reduction",
    "A": "associator_class_match",
}


@dataclass(frozen=True)
class RecognitionEnvelopeReport:
    """Status of the finite Hall-Borcherds recognition envelope."""

    envelope_constructed: bool
    source_packet_constructed: bool
    source_faithfulness_forced: bool
    finite_unquotiented_recognized: bool
    completed_envelope_constructed: bool
    completed_source_faithfulness: bool
    completed_unquotiented_recognized: bool
    vanished_defects: Tuple[str, ...]
    remaining_defects: Tuple[str, ...]
    status: str


def finite_defect_vanishings(witnesses: RecognitionEnvelopeWitnesses) -> Dict[str, bool]:
    """Return the five finite defect vanishings R, S, D, C, A."""
    return {
        defect: getattr(witnesses, field)
        for defect, field in FINITE_DEFECT_WITNESSES.items()
    }


def source_matrix_forces_faithfulness(witnesses: RecognitionEnvelopeWitnesses) -> bool:
    """Return True exactly when finite source matrices force J_H cap D_H^X = 0."""
    finite_objects = witnesses.finite_compact_double and witnesses.finite_borcherds_target
    return (
        finite_objects
        and witnesses.compact_source_packet
        and all(finite_defect_vanishings(witnesses).values())
    )


def evaluate_recognition_envelope(
    witnesses: RecognitionEnvelopeWitnesses,
) -> RecognitionEnvelopeReport:
    """Evaluate finite envelope construction versus faithful recognition."""
    finite_objects = witnesses.finite_compact_double and witnesses.finite_borcherds_target
    source_packet = witnesses.finite_compact_double and witnesses.compact_source_packet
    vanishings = finite_defect_vanishings(witnesses)
    vanished = tuple(defect for defect, ok in vanishings.items() if ok)
    remaining = tuple(defect for defect, ok in vanishings.items() if not ok)
    source_faithful = source_matrix_forces_faithfulness(witnesses)
    finite_recognized = source_faithful
    completed_envelope = finite_objects and witnesses.transition_compatible
    completed_source_faithful = source_faithful and witnesses.transition_compatible
    completed_recognized = completed_source_faithful
    if completed_recognized:
        status = "COMPLETED_UNQUOTIENTED_RECOGNITION"
    elif finite_recognized:
        status = "FINITE_UNQUOTIENTED_RECOGNITION"
    elif completed_envelope:
        status = "COMPLETED_RECOGNITION_ENVELOPE"
    elif finite_objects:
        status = "FINITE_RECOGNITION_ENVELOPE"
    else:
        status = "MISSING_FINITE_OBJECTS"
    return RecognitionEnvelopeReport(
        envelope_constructed=finite_objects,
        source_packet_constructed=source_packet,
        source_faithfulness_forced=source_faithful,
        finite_unquotiented_recognized=finite_recognized,
        completed_envelope_constructed=completed_envelope,
        completed_source_faithfulness=completed_source_faithful,
        completed_unquotiented_recognized=completed_recognized,
        vanished_defects=vanished,
        remaining_defects=remaining,
        status=status,
    )


def primitive_discriminant(n: int, ell: int, m: int) -> int:
    """Return D = 4 n m - ell^2 for a rank-three BKM charge."""
    return 4 * n * m - ell * ell


def primitive_root_key(n: int, ell: int, m: int) -> int:
    """Return the Jacobi-coefficient key for a primitive BKM root.

    The value is only a key.  A coefficient oracle for phi_{0,1} or its
    CHL/twined variant must still be supplied before a multiplicity is
    claimed.
    """
    if gcd(gcd(abs(n), abs(ell)), abs(m)) != 1:
        raise ValueError("root is imprimitive; use a divisor-sum lane")
    return primitive_discriminant(n, ell, m)


ANTI_SHORTCUTS: Dict[str, str] = {
    "coha_c3_is_w": "CoHA(C^3) is Y^+; W_{1+infty} appears only after double/center/evaluation data.",
    "bkm_is_yangian": "The K3 BKM object is the Hall-Drinfeld double, not a strict Drinfeld Yangian.",
    "phi10_weight_is_kappa_BKM": "Phi_10 has weight 10; primitive kappa_BKM(Delta_5) is 5.",
    "additive_kappa_BKM": "kappa_BKM is c_N(0)/2, not kappa_ch plus a fibre Euler term.",
    "six_phi_applications": "The six K3 x E routes are distinct constructions, not six Phi applications.",
}


def shortcut_allowed(shortcut: str) -> bool:
    """Return whether a named shortcut is allowed in the bridge package."""
    if shortcut not in ANTI_SHORTCUTS:
        raise KeyError(f"unknown shortcut: {shortcut}")
    return False


def additive_claim_status(
    *,
    kappa_ch_Heis: Fraction,
    kappa_fiber: Fraction,
    kappa_BKM: Fraction,
    universal_claim: bool,
) -> Dict[str, object]:
    """Classify the common additive kappa_BKM claim.

    At N = 1 the Heisenberg-fibre numbers may match, but the match is
    not a proof of the BKM denominator identity and cannot be promoted
    to a universal formula.
    """
    numeric_match = kappa_ch_Heis + kappa_fiber == kappa_BKM
    return {
        "numeric_match": numeric_match,
        "accepted_as_bridge_proof": False,
        "universal_claim": universal_claim,
        "reason": (
            "numeric coincidence only"
            if numeric_match
            else "wrong invariant lane"
        ),
    }


def all_shortcuts_rejected(shortcuts: Iterable[str] = ANTI_SHORTCUTS.keys()) -> bool:
    """Return True when every known bridge shortcut is rejected."""
    return all(not shortcut_allowed(shortcut) for shortcut in shortcuts)
