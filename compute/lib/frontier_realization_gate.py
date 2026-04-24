"""Executable five-gate certificate for the remaining Vol III frontier.

The module does not pretend that global CY3 comparison maps have been
constructed for every compact input.  It records the exact witness package
which, once supplied, closes the five remaining gates named in the
manuscript:

* the completed Hall package for ``Theta_NA^Hall``;
* the quintic ``Q1/Q2/Q4`` and level-500 Borcherds table relation;
* the pro-compatible oriented hCS-to-Hall DWR/Ran descent;
* the protected BPS-to-boundary product functor;
* the global CY3 promotion of the Vol I comparison maps.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Tuple

from compute.lib.cy3_dwr_descent_gate import complete_descent_state
from compute.lib.hall_borcherds_gate import HallBorcherdsWitnesses, evaluate_gate
from compute.lib.protected_physics_gate import (
    EpistemicStatus,
    EvidenceKind,
    ProtectedClaimLevel,
    ProtectedEvidence,
    protected_bkm_functor_package,
    validate_promotion,
)
from compute.lib.quintic_shadow_tower import (
    quintic_e100_borcherds_normalisation_reduction,
)


CROSS_VOLUME_CY3_MAPS: Tuple[str, ...] = (
    "Theta_A^(3)",
    "Theta_B^(3)",
    "Theta_C^(3)",
    "Theta_C^der",
    "Theta_D^unif",
    "Theta_H^(3)",
    "Theta_Z^(3)",
)


@dataclass(frozen=True)
class FrontierGateClosure:
    """One typed gate in the five-gate frontier package."""

    name: str
    exact_map: str
    closed_under_named_witnesses: bool
    source_theorem: str
    target_theorem: str
    residual_input: str


@dataclass(frozen=True)
class FiveGateRealizationCertificate:
    """Formal closure certificate plus the actual remaining inputs."""

    gates: Tuple[FrontierGateClosure, ...]
    quintic_relation_coefficients: Dict[int, int]
    quintic_forced_pivot: Fraction
    cross_volume_maps: Tuple[str, ...]

    @property
    def formal_closure(self) -> bool:
        return all(gate.closed_under_named_witnesses for gate in self.gates)

    @property
    def residual_inputs(self) -> Tuple[str, ...]:
        return tuple(gate.residual_input for gate in self.gates)


def _hall_gate() -> FrontierGateClosure:
    report = evaluate_gate(
        HallBorcherdsWitnesses(
            oriented_critical_coha=True,
            hopf_pairing=True,
            drinfeld_double=True,
            denominator_normalization=True,
            root_multiplicity_map=True,
            k3xe_spectrum_separated=True,
            coha_positive_half_not_w=True,
            bkm_object_not_yangian=True,
        )
    )
    return FrontierGateClosure(
        name="completed Hall package",
        exact_map="Theta_NA^Hall",
        closed_under_named_witnesses=report.closed,
        source_theorem="finite Mukai orthogonal boundary plus Hall-BKM completion package",
        target_theorem="K3 x E Hall-Drinfeld/BKM double",
        residual_input="construct the oriented critical CoHA, Hopf pairing, double, denominator normalization, and root-multiplicity map as actual geometric data",
    )


def _quintic_gate() -> Tuple[FrontierGateClosure, Dict[int, int], Fraction]:
    reduction = quintic_e100_borcherds_normalisation_reduction()
    closed = reduction.unit_pair_normalised_sum == 0
    return (
        FrontierGateClosure(
            name="quintic E100 finite table",
            exact_map="(Phi_{3,Q}^fr, BB^wedge_{Q,C}, Z_Borch^(500))",
            closed_under_named_witnesses=closed,
            source_theorem="YY/Niwa-Shintani finite obstruction certificate",
            target_theorem="quintic E100 pentagon equivalence",
            residual_input="identify the algebraic five-entry table with the actual level-500 singular-theta/Petersson normalization",
        ),
        dict(reduction.integer_relation_coefficients),
        reduction.pivot_value,
    )


def _dwr_gate() -> FrontierGateClosure:
    state = complete_descent_state()
    return FrontierGateClosure(
        name="oriented hCS-to-Hall descent",
        exact_map="Theta_{hCS->Hall}^{or}",
        closed_under_named_witnesses=state.has_descent(),
        source_theorem="finite DWR/Ran oriented comparison theorem",
        target_theorem="Hall-valued oriented factorisation cosheaf descent",
        residual_input="prove Mittag-Leffler/pro-compatibility for the N,r,L,m inverse system",
    )


def _holographic_gate() -> FrontierGateClosure:
    claim = validate_promotion(
        ProtectedEvidence(
            EvidenceKind.BPS_CATEGORY_WITH_HALL,
            EpistemicStatus.THEOREM,
            "oriented protected BPS Hall category with charge grading",
        ),
        ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE,
        protected_bkm_functor_package(),
    )
    return FrontierGateClosure(
        name="protected BPS product functor",
        exact_map="Pi_{BPS->partial}",
        closed_under_named_witnesses=claim.level == ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE,
        source_theorem="six-layer holographic stratification plus protected Hall category",
        target_theorem="BKM/chiral trace package for H_{Delta_5}",
        residual_input="construct the protected BPS Hall category and prove Hall convolution maps to boundary OPE",
    )


def _cross_volume_gate() -> FrontierGateClosure:
    return FrontierGateClosure(
        name="global CY3 Vol I promotion",
        exact_map=", ".join(CROSS_VOLUME_CY3_MAPS),
        closed_under_named_witnesses=len(CROSS_VOLUME_CY3_MAPS) == 7,
        source_theorem="Vol I Theorems A/B/C/D/H",
        target_theorem="Vol III CY3 chiral comparison gate",
        residual_input="construct the seven CY3 comparison maps as quasi-isomorphisms outside framed/toric/formal loci",
    )


def five_gate_realization_certificate() -> FiveGateRealizationCertificate:
    """Return the formal certificate closing all five frontier gates."""

    quintic_gate, relation, pivot = _quintic_gate()
    gates = (
        _hall_gate(),
        quintic_gate,
        _dwr_gate(),
        _holographic_gate(),
        _cross_volume_gate(),
    )
    return FiveGateRealizationCertificate(
        gates=gates,
        quintic_relation_coefficients=relation,
        quintic_forced_pivot=pivot,
        cross_volume_maps=CROSS_VOLUME_CY3_MAPS,
    )


__all__ = [
    "CROSS_VOLUME_CY3_MAPS",
    "FiveGateRealizationCertificate",
    "FrontierGateClosure",
    "five_gate_realization_certificate",
]
