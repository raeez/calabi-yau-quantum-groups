"""Registry for the eight homotopy-gluing / positive-cone obligations.

This is a structural oracle, not a proof assistant.  It checks that the
frontier package is stated in the only safe order:

    positive half -> motivic integration -> automorphic boundary
    -> Hall-BKM quotient -> Drinfeld double.

The registry prevents two common false shortcuts:

* treating the compact Hall-Drinfeld double as the homotopy colimit of
  local doubles;
* treating the Igusa Borcherds weight as a categorical or topological
  Euler characteristic.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Tuple


PROVED = "proved"
CONDITIONAL = "conditional"
CONJECTURAL = "conjectural"
VERIFICATION = "verification"
PROPAGATION = "propagation"


@dataclass(frozen=True)
class ResolutionObligation:
    key: str
    title: str
    status: str
    construction: str
    frontier_data: Tuple[str, ...]
    depends_on: Tuple[str, ...] = ()

    @property
    def is_frontier(self) -> bool:
        return self.status in {CONDITIONAL, CONJECTURAL}


OBLIGATIONS: Mapping[str, ResolutionObligation] = {
    "hall_cosheaf": ResolutionObligation(
        key="hall_cosheaf",
        title="compact K3 x E oriented critical Hall cosheaf",
        status=CONDITIONAL,
        construction="completed oriented motivic Hall cosheaf on the DWR/Cech/Ran site",
        frontier_data=(
            "oriented (-1)-shifted critical atlas",
            "orientation branch",
            "HN-sector local finiteness",
            "Thom-Sebastiani coherence",
        ),
    ),
    "theta_hcs_hall": ResolutionObligation(
        key="theta_hcs_hall",
        title="global oriented hCS-to-Hall comparison",
        status=CONDITIONAL,
        construction="continuous natural transformation on the full DWR/Cech/Ran nerve",
        frontier_data=(
            "local stationary-phase maps",
            "MC obstruction vanishing",
            "orientation transport",
            "grading and Tate compatibility",
            "factorisation compatibility",
        ),
        depends_on=("hall_cosheaf",),
    ),
    "autborch": ResolutionObligation(
        key="autborch",
        title="AutBorch functor",
        status=CONDITIONAL,
        construction="primitive BPS motive to automorphic denominator data",
        frontier_data=(
            "Jacobi input realization",
            "integrality",
            "discriminant boundedness",
            "orientation character compatibility",
        ),
    ),
    "hall_bkm": ResolutionObligation(
        key="hall_bkm",
        title="Hall-BKM comparison",
        status=CONDITIONAL,
        construction="automorphic radical quotient into U(Y+(g_Delta5))_num",
        frontier_data=(
            "primitive Hall motive equals phi_0,1 seed",
            "Lorentzian chamber",
            "automorphic radical quotient",
            "root multiplicity comparison",
        ),
        depends_on=("hall_cosheaf", "autborch"),
    ),
    "hall_drinfeld_double": ResolutionObligation(
        key="hall_drinfeld_double",
        title="compact Hall-Drinfeld double",
        status=CONJECTURAL,
        construction="Y- completed bowtie Y0 completed bowtie Y+",
        frontier_data=(
            "coproduct",
            "negative half",
            "Cartan completion",
            "continuous Hopf pairing",
            "radical quotient",
            "center compatibility",
        ),
        depends_on=("hall_cosheaf", "hall_bkm"),
    ),
    "wall_descent": ResolutionObligation(
        key="wall_descent",
        title="wall-crossing equals descent transport",
        status=CONDITIONAL,
        construction="Dec(T_DWR(path)) equals KS conjugation after motivic integration",
        frontier_data=(
            "finite truncations",
            "motivic integration functoriality",
            "admissible wall paths",
        ),
        depends_on=("hall_cosheaf",),
    ),
    "validation": ResolutionObligation(
        key="validation",
        title="manuscript validation",
        status=VERIFICATION,
        construction="targeted pytest plus make fast",
        frontier_data=("label surface", "macro surface", "build log classification"),
    ),
    "igusa_propagation": ResolutionObligation(
        key="igusa_propagation",
        title="cross-repo Igusa dictionary propagation",
        status=PROPAGATION,
        construction="short compatibility note in ~/igusa-cusp-form",
        frontier_data=("Gamma_eff", "alpha", "nu_Delta5", "Delta5 denominator"),
        depends_on=("autborch",),
    ),
}


def obligation_order() -> Tuple[str, ...]:
    return tuple(OBLIGATIONS)


def missing_dependencies() -> Dict[str, Tuple[str, ...]]:
    keys = set(OBLIGATIONS)
    return {
        key: tuple(dep for dep in obligation.depends_on if dep not in keys)
        for key, obligation in OBLIGATIONS.items()
        if any(dep not in keys for dep in obligation.depends_on)
    }


def unsafe_frontier_claims() -> Tuple[str, ...]:
    """Frontier objects must not be marked proved in this registry."""

    frontier_keys = {
        "hall_cosheaf",
        "theta_hcs_hall",
        "autborch",
        "hall_bkm",
        "hall_drinfeld_double",
        "wall_descent",
    }
    return tuple(
        key
        for key in frontier_keys
        if OBLIGATIONS[key].status == PROVED and OBLIGATIONS[key].frontier_data
    )


def depends_transitively(key: str, target: str) -> bool:
    seen = set()
    stack = list(OBLIGATIONS[key].depends_on)
    while stack:
        current = stack.pop()
        if current == target:
            return True
        if current in seen:
            continue
        seen.add(current)
        stack.extend(OBLIGATIONS[current].depends_on)
    return False


def kappa_bkm_delta5() -> Fraction:
    return Fraction(10, 2)


def igusa_dictionary() -> Mapping[str, str]:
    return {
        "charge_lattice": "Gamma_BPS = Z^3",
        "effective_chamber": "Gamma_eff",
        "degree_map": "alpha(n,l,m)=2n f2 - l f3 + 2m f_-2",
        "orientation": "epsilon_o = nu_Delta5",
        "autborch": "AutBorch(phi_0,1)=Delta5",
        "denominator": "den(g_Delta5)=64^-1 Delta5(2Z)",
        "scalar_square": "Z_square = C_square Delta5^-2",
        "kappa_bkm": "kappa_BKM(g_Delta5)=5",
    }


def all_frontier_data_nonempty(obligations: Iterable[ResolutionObligation] = OBLIGATIONS.values()) -> bool:
    return all(obligation.frontier_data for obligation in obligations)
