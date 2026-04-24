"""Gate calculus for the compact K3 x E Hall construction package.

The module is deliberately small.  It mirrors the construction theorem in
``chapters/theory/gluing/sec_10_unifying.tex`` and guards the order of
dependencies:

    Hall cosheaf -> global Theta -> AutBorch/Hall-BKM -> double
    Hall cosheaf + motivic integration -> KS wall equality.

It does not prove the frontier data.  It records exactly which gates must
be supplied before the package is an actual compact CY-C construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import FrozenSet, Mapping, Sequence, Tuple


GateKey = str


@dataclass(frozen=True)
class ConstructionGate:
    key: GateKey
    output: str
    supplies: Tuple[str, ...]
    requires: FrozenSet[GateKey] = frozenset()
    obstruction: Tuple[str, ...] = ()
    status: str = "conditional"

    @property
    def is_unconditional(self) -> bool:
        return self.status == "proved"


GATES: Mapping[GateKey, ConstructionGate] = {
    "compact_hall_cosheaf": ConstructionGate(
        key="compact_hall_cosheaf",
        output="H^{mot,or}_{K3xE,sigma,-} on the DWR/Cech/Ran nerve",
        supplies=(
            "oriented critical Hall charts",
            "restriction/refinement maps",
            "Hall convolution",
            "HN completion",
        ),
        obstruction=("o_atlas", "o_or", "o_HN", "o_TS"),
    ),
    "global_theta": ConstructionGate(
        key="global_theta",
        output="Theta^{or}_{hCS->Hall} as a continuous natural transformation",
        supplies=(
            "local stationary-phase maps",
            "orientation transport",
            "grading/Tate compatibility",
            "factorisation compatibility",
        ),
        requires=frozenset({"compact_hall_cosheaf"}),
        obstruction=("o_MC", "o_or", "o_gr", "o_fact"),
    ),
    "autborch_functor": ConstructionGate(
        key="autborch_functor",
        output="AutBorch: primitive BPS motive -> automorphic denominator",
        supplies=(
            "Jacobi realization",
            "Borcherds lift",
            "orientation character",
            "Delta5 boundary",
        ),
        obstruction=("o_jac", "o_integral", "o_disc", "o_character"),
    ),
    "hall_bkm_comparison": ConstructionGate(
        key="hall_bkm_comparison",
        output="CoHA^{or}_{crit}(K3xE) -> U(Y+(g_Delta5))_num",
        supplies=(
            "primitive seed",
            "Lorentzian chamber",
            "automorphic radical quotient",
            "root multiplicities",
        ),
        requires=frozenset({"compact_hall_cosheaf", "autborch_functor"}),
        obstruction=("o_prim", "o_rad"),
    ),
    "compact_drinfeld_double": ConstructionGate(
        key="compact_drinfeld_double",
        output="D_hbar(CoHA^{or}_{crit}(K3xE))",
        supplies=(
            "negative half",
            "Cartan completion",
            "continuous Hopf pairing",
            "radical quotient",
            "bracket comparison",
            "center compatibility",
        ),
        requires=frozenset({"compact_hall_cosheaf", "hall_bkm_comparison"}),
        obstruction=("o_Delta", "o_pair", "o_cent"),
    ),
    "wall_descent_ks": ConstructionGate(
        key="wall_descent_ks",
        output="Dec(T_DWR(path)) = Ad_KS(path)",
        supplies=(
            "finite truncation equality",
            "motivic integration functoriality",
            "inverse-limit HN completion",
        ),
        requires=frozenset({"compact_hall_cosheaf"}),
        obstruction=("o_finite", "o_int", "o_limit"),
    ),
    "build_hygiene": ConstructionGate(
        key="build_hygiene",
        output="targeted tests plus make fast",
        supplies=("label check", "macro check", "citation check"),
        status="verification",
    ),
    "igusa_reconciliation": ConstructionGate(
        key="igusa_reconciliation",
        output="Igusa chamber/denominator dictionary synchronized",
        supplies=("Gamma_eff", "alpha", "nu_Delta5", "Delta5 denominator"),
        requires=frozenset({"autborch_functor"}),
        status="propagation",
    ),
}


DOUBLE_REQUIRED_DATA: FrozenSet[str] = frozenset(
    {
        "negative half",
        "Cartan completion",
        "continuous Hopf pairing",
        "radical quotient",
        "bracket comparison",
        "center compatibility",
    }
)


AUTBORCH_DOMAIN_CONDITIONS: Tuple[str, ...] = (
    "integrality",
    "weak holomorphy",
    "discriminant boundedness",
    "lattice compatibility",
    "orientation-character compatibility",
)

COSHEAF_STRUCTURE_MAPS: Tuple[str, ...] = (
    "critical chart value",
    "orientation-line transport",
    "HN completed charge sum",
    "refinement push-pull",
    "Thom-Sebastiani factorization",
    "Hall extension convolution",
)


THETA_FULL_NERVE_EQUATIONS: Tuple[str, ...] = (
    "refinement naturality",
    "BV product to Hall convolution",
    "disjoint Ran factorization",
    "shift/Tate/orientation transport",
)


FINITE_FIRST_WALL_DATA: Tuple[str, ...] = (
    "charge-height truncation",
    "central-charge-radius truncation",
    "finite Hall wall product",
    "finite KS product",
    "HN inverse limit",
)


def gate_order() -> Tuple[GateKey, ...]:
    return tuple(GATES)


def missing_gate_dependencies() -> Mapping[GateKey, Tuple[GateKey, ...]]:
    keys = set(GATES)
    return {
        key: tuple(sorted(gate.requires - keys))
        for key, gate in GATES.items()
        if gate.requires - keys
    }


def constructible_gates(supplied: FrozenSet[GateKey]) -> Tuple[GateKey, ...]:
    """Return gates whose prerequisites are present in ``supplied``."""

    return tuple(
        key for key, gate in GATES.items() if gate.requires.issubset(supplied)
    )


def compact_double_data_missing(supplied_data: FrozenSet[str]) -> Tuple[str, ...]:
    return tuple(sorted(DOUBLE_REQUIRED_DATA - supplied_data))


def compact_double_ready(supplied_data: FrozenSet[str]) -> bool:
    return not compact_double_data_missing(supplied_data)


def unsafe_unconditional_frontier_gates() -> Tuple[GateKey, ...]:
    frontier = {
        "compact_hall_cosheaf",
        "global_theta",
        "autborch_functor",
        "hall_bkm_comparison",
        "compact_drinfeld_double",
        "wall_descent_ks",
    }
    return tuple(key for key in frontier if GATES[key].is_unconditional)


def kappa_bkm_delta5() -> Fraction:
    return Fraction(10, 2)


def igusa_boundary_normalization() -> Mapping[str, str]:
    return {
        "autborch": "AutBorch(phi_0,1)=Delta5",
        "denominator": "den(g_Delta5)=64^-1 Delta5(2Z)",
        "orientation": "epsilon_o=nu_Delta5",
        "kappa_bkm": "kappa_BKM(g_Delta5)=5",
        "degree_map": "alpha(n,l,m)=2n f2 - l f3 + 2m f_-2",
    }


def finite_first_wall_statement() -> str:
    return "Dec(T_DWR,N,R(path)) = Ad_KS,N,R(path), then inverse limit"


def cosheaf_structure_maps() -> Tuple[str, ...]:
    return COSHEAF_STRUCTURE_MAPS


def theta_full_nerve_equations() -> Tuple[str, ...]:
    return THETA_FULL_NERVE_EQUATIONS


def finite_first_wall_data() -> Tuple[str, ...]:
    return FINITE_FIRST_WALL_DATA


def construction_has_chart_level_cosheaf() -> bool:
    required = {
        "critical chart value",
        "orientation-line transport",
        "HN completed charge sum",
        "refinement push-pull",
        "Thom-Sebastiani factorization",
        "Hall extension convolution",
    }
    return required.issubset(COSHEAF_STRUCTURE_MAPS)


def construction_has_full_nerve_theta() -> bool:
    required = {
        "refinement naturality",
        "BV product to Hall convolution",
        "disjoint Ran factorization",
        "shift/Tate/orientation transport",
    }
    return required.issubset(THETA_FULL_NERVE_EQUATIONS)


def all_obstruction_names() -> Tuple[str, ...]:
    names = []
    for gate in GATES.values():
        names.extend(gate.obstruction)
    return tuple(names)


def duplicate_obstruction_names() -> Tuple[str, ...]:
    names = all_obstruction_names()
    return tuple(sorted({name for name in names if names.count(name) > 1}))
