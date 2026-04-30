r"""Tsygan, Costello, and the m_3--B^{(2)} obstruction.

This engine records the repaired obstruction logic.

There are three distinct carriers:

* ``B^{(2)}_term``: the raw bar-desuspended pair-contraction operator.
  It has a strict nonzero cyclic CY3 witness:

      [m_3, B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0.

* ``B^{(2)}_TCFT``: Costello's corrected open--closed TCFT operator.
  The theorem is the total identity

      {sum_k b_k, B^{(2)}_TCFT} = 0,

  after the moduli-chain correction datum has been chosen.  It is not a
  termwise identity for ``B^{(2)}_term``.

* the derived E_1-Hochschild obstruction class.  Vanishing at this level
  is meaningful only after the target complex, comparison map, and
  hypotheses are named.

Consequently this module rejects the old assertion that
Tsygan-Costello formality universally proves termwise chain vanishing,
termwise exactness, or closure of the compact S^3-framing programme.

CONVENTIONS
===========
  - Characteristic zero.
  - Cohomological grading.
  - Bar variables are desuspended.
  - Strict witness: |e|=0, |a|=1, |b|=2, |w|=3,
    <e,w>=1, <a,b>=1, and m_3(a,a,a)=alpha b.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Tuple

F = Fraction


OBSTRUCTION_COMPLEX = (
    "C^bullet_End(CC_*(A)) = End(CC_*(A)) with differential "
    "d_End(T) = [b,T], b = sum_k b_k"
)

DERIVED_E1_COMPLEX = (
    "C^bullet_{E_1}(A,A) with the reduced bar-length filtration, "
    "targeting HH^{-2}_{E_1}(A,A)"
)

COMPARISON_MAP = (
    "theta_TCFT: B_term^{(2)} -> B_TCFT^{(2)}, witnessed by a homotopy "
    "H_TCFT with B_TCFT^{(2)} - B_term^{(2)} = d_End(H_TCFT)"
)

FILTERED_HYPOTHESIS = (
    "the reduced Hochschild cochain filtration is complete, exhaustive, "
    "separated, strongly convergent, and has empty E_1 total-degree -2 line"
)


# =========================================================================
# 0. TSYGAN FORMALITY THEOREM
# =========================================================================


@dataclass(frozen=True)
class TsyganFormalityData:
    r"""Tsygan's mixed-complex formality theorem.

    Tsygan formality applies to the cyclic mixed complex ``(CC_*(A), b, B)``.
    Here ``B`` is the ordinary Connes operator.  This theorem by itself does
    not identify the raw pair-contraction ``B^{(2)}_term`` with Costello's
    corrected TCFT operator and does not produce a homotopy killing
    ``[m_k, B^{(2)}_term]``.
    """

    requires_smooth: bool = True
    requires_char_zero: bool = True
    requires_proper: bool = False

    formality_level: str = "mixed-complex quasi-isomorphism"
    preserves_mixed_complex: bool = True
    preserves_connes_operator: bool = True
    chain_level_identity: bool = False

    costello_extension: bool = False
    connes_hierarchy_extension: bool = False
    raw_b2_termwise_covered: bool = False

    def applies_to_cy3(self) -> bool:
        """Tsygan's mixed-complex theorem applies over characteristic zero."""
        return True

    def applies_to_cy_d(self, d: int) -> bool:
        """The mixed-complex theorem is not dimension-specific."""
        return d >= 1

    def gives_chain_level_vanishing(self) -> bool:
        """It does not prove ``[m_k, B^{(2)}_term] = 0`` on chains."""
        return False

    def gives_cohomological_vanishing(self) -> bool:
        """It does not by itself prove the raw termwise obstruction class zero.

        A cohomological statement requires a named obstruction complex and
        either comparison data from ``B^{(2)}_term`` to ``B^{(2)}_TCFT`` or a
        separate ``HH^{-2}`` filtration theorem.
        """
        return False

    def requires_b2_comparison_data(self) -> bool:
        """The raw ``B^{(2)}_term`` target needs extra comparison data."""
        return True


# =========================================================================
# 1. COSTELLO'S CORRECTED TCFT OPERATOR
# =========================================================================


@dataclass(frozen=True)
class CostelloTCFTFormality:
    r"""Costello's corrected open--closed TCFT operator.

    Costello supplies a corrected TCFT representative after the relevant
    moduli-chain correction datum is chosen.  The identity is total in the
    Hochschild differential ``b = sum_k b_k``.  It is not a proof of
    ``[b_k, B^{(2)}_term] = 0`` and not a proof that the raw termwise
    operator equals the corrected TCFT representative.
    """

    cy_dimension: int
    smooth: bool = True
    proper: bool = True
    correction_datum_chosen: bool = True

    def connes_hierarchy_levels(self) -> int:
        """Number of hierarchy indices available in CY dimension ``d``."""
        return self.cy_dimension + 1

    def b2_is_formal(self) -> bool:
        """Whether a corrected ``B^{(2)}_TCFT`` datum is available."""
        return self.cy_dimension >= 2 and self.correction_datum_chosen

    def full_hierarchy_formal(self) -> bool:
        """The corrected TCFT hierarchy is available, not the raw hierarchy."""
        return self.correction_datum_chosen

    def total_tcft_identity_holds(self) -> bool:
        """Costello's theorem gives ``{sum_k b_k, B_TCFT^{(2)}} = 0``."""
        return self.b2_is_formal() and self.smooth and self.proper

    def termwise_identity_holds(self) -> bool:
        """No per-k identity is supplied by the TCFT theorem."""
        return False

    def raw_term_operator_identified(self) -> bool:
        """No equality ``B_term^{(2)} = B_TCFT^{(2)}`` is part of the theorem."""
        return False

    def formality_map_explicit(self) -> bool:
        """The corrected representative depends on explicit TCFT choices."""
        return False


# =========================================================================
# 2. GAP ANALYSIS
# =========================================================================


@dataclass(frozen=True)
class GapAnalysis:
    r"""The gap between cyclic invariance and bar-level compatibility."""

    g1_cyclic_invariance: str = (
        "<m_n(a_1,...,a_n), a_{n+1}> = +/- <a_1, m_n(a_2,...,a_{n+1})>"
    )
    g2_bar_compatibility: str = "[m_k, B^{(2)}_term] = 0 on CC_*(A)"

    chain_level_gap: bool = True
    cohomology_level_gap: bool = True
    resolution_mechanism: str = (
        "corrected TCFT comparison datum or HH^{-2} filtration theorem"
    )

    def gap_exists_chain_level(self) -> bool:
        """The strict witness shows the raw termwise gap is real."""
        return True

    def gap_closed_cohomology(self) -> bool:
        """No default cohomological closure is proved for the raw target."""
        return False

    def why_cohomology_suffices(self) -> str:
        """State the missing data for any cohomological claim."""
        return (
            "Cohomology suffices only after the obstruction is formulated as "
            f"a class in {OBSTRUCTION_COMPLEX} or {DERIVED_E1_COMPLEX}, and "
            f"after the comparison map {COMPARISON_MAP} or the filtration "
            f"hypothesis ({FILTERED_HYPOTHESIS}) is supplied."
        )


# =========================================================================
# 3. NON-ADJACENT CONTRACTIONS
# =========================================================================


@dataclass
class NonAdjacentContractionTerm:
    """A single term in the raw ``[m_k, B^{(2)}_term]`` commutator."""

    bar_length: int
    mk_arity: int
    mk_start: int
    contraction_inside: int
    contraction_outside: int

    def is_adjacent(self) -> bool:
        """Whether the outside factor is adjacent to the ``m_k`` block."""
        return (
            self.contraction_outside == self.mk_start - 1
            or self.contraction_outside == self.mk_start + self.mk_arity
        )

    def controlled_by_cyclic_invariance(self) -> bool:
        """Adjacent contractions are the part controlled by cyclicity."""
        return self.is_adjacent()

    def controlled_by_tsygan_formality(self) -> bool:
        """Tsygan formality does not control raw non-adjacent terms."""
        return False

    def requires_tcft_comparison(self) -> bool:
        """Non-adjacent raw terms require corrected TCFT comparison data."""
        return not self.is_adjacent()


def enumerate_non_adjacent_terms(
    bar_length: int,
    mk_arity: int,
) -> List[NonAdjacentContractionTerm]:
    """Enumerate raw terms with one contraction inside and one outside."""
    if bar_length < mk_arity + 2:
        return []

    terms: List[NonAdjacentContractionTerm] = []
    for start in range(bar_length - mk_arity + 1):
        mk_end = start + mk_arity - 1
        for inside in range(start, mk_end + 1):
            for outside in range(bar_length):
                if start <= outside <= mk_end:
                    continue
                if outside == start - 1 or outside == mk_end + 1:
                    continue
                terms.append(
                    NonAdjacentContractionTerm(
                        bar_length=bar_length,
                        mk_arity=mk_arity,
                        mk_start=start,
                        contraction_inside=inside,
                        contraction_outside=outside,
                    )
                )
    return terms


def count_non_adjacent_terms(bar_length: int, mk_arity: int) -> int:
    """Count raw non-adjacent contraction configurations."""
    return len(enumerate_non_adjacent_terms(bar_length, mk_arity))


# =========================================================================
# 4. PROOF-OBLIGATION STRUCTURE
# =========================================================================


@dataclass
class TsyganProofStep:
    """A single checked step in the repaired attack-heal chain."""

    number: int
    statement: str
    justification: str
    status: str

    def __repr__(self) -> str:
        return f"Step {self.number}: {self.statement} [{self.status}]"


def construct_proof() -> List[TsyganProofStep]:
    """Construct the repaired proof-obligation chain.

    This is not a proof of universal vanishing.  It is the verified chain
    rejecting the false strengthening and naming the conditional route.
    """
    return [
        TsyganProofStep(
            number=1,
            statement=(
                "Tsygan formality applies to the mixed complex "
                "(CC_*(A), b, B), with B the ordinary Connes operator."
            ),
            justification=(
                "Tsygan, arXiv:math/9904132.  The statement does not include "
                "the raw pair-contraction B_term^{(2)}."
            ),
            status="Tsygan",
        ),
        TsyganProofStep(
            number=2,
            statement=(
                "The raw termwise commutator [m_3, B_term^{(2)}] has a "
                "strict nonzero cyclic CY3 witness."
            ),
            justification=(
                "Direct exact arithmetic gives 4 alpha [b] - 2 alpha [b] = "
                "2 alpha [b] on [a|a|a|a|b]."
            ),
            status="computed",
        ),
        TsyganProofStep(
            number=3,
            statement=(
                "Costello's theorem concerns B_TCFT^{(2)}, the corrected "
                "open--closed TCFT representative."
            ),
            justification=(
                "The TCFT boundary relation gives the total identity "
                "{sum_k b_k, B_TCFT^{(2)}} = 0 after correction data."
            ),
            status="Costello",
        ),
        TsyganProofStep(
            number=4,
            statement=(
                "A cohomological obstruction statement must name its complex "
                "and comparison map."
            ),
            justification=(
                f"Use {OBSTRUCTION_COMPLEX} with {COMPARISON_MAP}, or use "
                f"{DERIVED_E1_COMPLEX} under the HH^(-2) filtration theorem."
            ),
            status="conditional",
        ),
        TsyganProofStep(
            number=5,
            statement=(
                "Tsygan-Costello formality does not close the compact "
                "S^3-framing programme without these hypotheses."
            ),
            justification=(
                "The strict witness is algebraic and does not construct a "
                "global Phi_3, compact Hall/CoHA data, or G(X)."
            ),
            status="rejected",
        ),
        TsyganProofStep(
            number=6,
            statement=(
                "The repaired verdict is rejection for the raw termwise "
                "target and conditionality for the derived class target."
            ),
            justification=(
                "Raw nonzero witness plus corrected-operator distinction."
            ),
            status="repaired",
        ),
    ]


# =========================================================================
# 5. COMPARISON DATA
# =========================================================================


@dataclass(frozen=True)
class TsyganComparison:
    r"""Comparison between raw, corrected, and derived targets."""

    obstruction_complex: str = OBSTRUCTION_COMPLEX
    comparison_map: str = COMPARISON_MAP
    filtered_complex: str = DERIVED_E1_COMPLEX
    filtered_hypothesis: str = FILTERED_HYPOTHESIS

    tsygan_gives_chain_level: bool = False
    tsygan_gives_cohomological: bool = False
    programme_needs_chain_level: bool = False
    programme_needs_cohomological: bool = True
    gap_resolved: bool = False

    obstruction_class_formulated: bool = False
    comparison_map_named: bool = False
    corrected_tcft_operator: bool = False
    hh_minus_two_filtration: bool = False

    @classmethod
    def with_corrected_tcft_comparison(cls) -> "TsyganComparison":
        """Comparison data sufficient for a conditional class statement."""
        return cls(
            obstruction_class_formulated=True,
            comparison_map_named=True,
            corrected_tcft_operator=True,
            gap_resolved=True,
        )

    @classmethod
    def with_hh_minus_two_filtration(cls) -> "TsyganComparison":
        """Filtration data sufficient for a conditional derived class result."""
        return cls(
            obstruction_class_formulated=True,
            hh_minus_two_filtration=True,
            gap_resolved=True,
        )

    def sufficient_for_programme(self) -> bool:
        """Whether the comparison data are enough for a class-level theorem."""
        corrected_route = self.comparison_map_named and self.corrected_tcft_operator
        filtered_route = self.hh_minus_two_filtration
        return self.obstruction_class_formulated and (corrected_route or filtered_route)

    def chain_level_status(self) -> str:
        """Raw chain-level status."""
        return (
            "[m_3, B_term^{(2)}] is strictly nonzero on the cyclic CY3 "
            "witness; no universal d(h_k) exactness is proved for the raw "
            "operator."
        )

    def difference_from_strict_vanishing(self) -> str:
        """Distinguish corrected TCFT cancellation from raw vanishing."""
        return (
            "Strict raw vanishing would assert [m_k, B_term^{(2)}] = 0. "
            "Costello gives the total corrected identity for B_TCFT^{(2)}. "
            "To compare them one must supply theta_TCFT or the HH^{-2} "
            "filtration theorem."
        )


# =========================================================================
# 6. EXPLICIT STRICT CY3 WITNESS AND LOCAL P2 GUIDE
# =========================================================================


DEGREES = {"e": 0, "a": 1, "b": 2, "w": 3}
PAIRING = {
    ("e", "w"): F(1),
    ("w", "e"): F(1),
    ("a", "b"): F(1),
    ("b", "a"): F(1),
}


def _clean(counter: Counter) -> Counter:
    return Counter({key: value for key, value in counter.items() if value})


def _terminal_slot_b2_term(word: Tuple[str, ...]) -> Counter:
    """Terminal-slot raw ``B^{(2)}_term`` from the standalone witness."""
    terminal = word[-1]
    out: Counter = Counter()
    for idx, entry in enumerate(word[:-1]):
        coeff = PAIRING.get((entry, terminal), F(0))
        if coeff:
            reduced = word[:idx] + word[idx + 1:-1]
            out[reduced] += coeff
    return _clean(out)


def _m3_bar(word: Tuple[str, ...], alpha: Fraction) -> Counter:
    """Minimal witness operation ``m_3(a,a,a)=alpha b``."""
    out: Counter = Counter()
    for start in range(len(word) - 2):
        if word[start:start + 3] == ("a", "a", "a"):
            reduced = word[:start] + ("b",) + word[start + 3:]
            out[reduced] += alpha
    return _clean(out)


def _compose(first, second, word: Tuple[str, ...]) -> Counter:
    """Apply ``first`` and then ``second`` to a linear combination."""
    total: Counter = Counter()
    for mid, coeff_mid in first(word).items():
        for out, coeff_out in second(mid).items():
            total[out] += coeff_mid * coeff_out
    return _clean(total)


def _subtract(left: Counter, right: Counter) -> Counter:
    total: Counter = Counter(left)
    for key, value in right.items():
        total[key] -= value
    return _clean(total)


def strict_cyclic_cy3_witness(alpha: Fraction = F(1)) -> Dict[str, Any]:
    """Compute the strict nonzero witness exactly.

    The word is ``[a|a|a|a|b]``.  The two routes are
    ``m_3 B_term^{(2)}`` and ``B_term^{(2)} m_3``.
    """
    alpha = F(alpha)
    word = ("a", "a", "a", "a", "b")
    b2_then_m3 = _compose(
        _terminal_slot_b2_term,
        lambda w: _m3_bar(w, alpha),
        word,
    )
    m3_then_b2 = _compose(
        lambda w: _m3_bar(w, alpha),
        _terminal_slot_b2_term,
        word,
    )
    commutator = _subtract(b2_then_m3, m3_then_b2)

    return {
        "word": word,
        "alpha": alpha,
        "B_term_then_m3": b2_then_m3,
        "m3_then_B_term": m3_then_b2,
        "commutator": commutator,
        "expected": Counter({("b",): 2 * alpha}),
        "chain_level_vanishing": not bool(commutator),
        "cohomological_vanishing_established": False,
        "comparison_data_required": True,
        "statement": (
            "[m_3, B_term^{(2)}][a|a|a|a|b] = 2 alpha [b] != 0 "
            "in characteristic zero."
        ),
    }


@dataclass
class LocalP2Data:
    r"""Noncompact local P2 guide for non-formal ``m_3`` behaviour."""

    generators: Dict[str, int] = field(default_factory=lambda: {
        "e_0": 0, "e_1": 0, "e_2": 0,
        "x_01": 1, "y_01": 1, "z_01": 1,
        "x_12": 1, "y_12": 1, "z_12": 1,
        "u_02": 2, "v_02": 2, "w_02": 2,
        "x_20": 2, "y_20": 2, "z_20": 2,
        "omega_0": 3, "omega_1": 3, "omega_2": 3,
    })
    cy_pairing: Dict[Tuple[str, str], Fraction] = field(default_factory=lambda: {
        ("e_0", "omega_0"): F(1),
        ("e_1", "omega_1"): F(1),
        ("e_2", "omega_2"): F(1),
        ("x_01", "x_20"): F(1),
        ("y_01", "y_20"): F(1),
        ("z_01", "z_20"): F(1),
        ("x_12", "u_02"): F(1),
        ("y_12", "v_02"): F(1),
        ("z_12", "w_02"): F(1),
    })
    m3_data: Dict[Tuple[str, str, str], List[Tuple[str, Fraction]]] = field(
        default_factory=lambda: {
            ("x_01", "y_12", "z_20"): [("e_0", F(1))],
            ("y_01", "z_12", "x_20"): [("e_0", F(1))],
            ("z_01", "x_12", "y_20"): [("e_0", F(1))],
            ("x_01", "z_12", "y_20"): [("e_0", F(-1))],
        }
    )

    def is_formal(self) -> bool:
        """Local P2 is non-formal in this diagnostic model."""
        return False

    def has_nontrivial_m3(self) -> bool:
        """The cubic potential supplies nonzero ``m_3`` terms."""
        return True

    def generator_count(self) -> int:
        return len(self.generators)

    def ext_dimensions(self) -> Dict[int, int]:
        dims: Dict[int, int] = {}
        for degree in self.generators.values():
            dims[degree] = dims.get(degree, 0) + 1
        return dims


def compute_non_adjacent_terms_local_p2(bar_length: int = 5) -> Dict[str, Any]:
    """Compute raw non-adjacent configurations for the local P2 guide."""
    terms = enumerate_non_adjacent_terms(bar_length, mk_arity=3)
    non_adjacent_count = len([term for term in terms if not term.is_adjacent()])

    return {
        "bar_length": bar_length,
        "mk_arity": 3,
        "total_terms": len(terms),
        "non_adjacent_count": non_adjacent_count,
        "adjacent_count": 0,
        "chain_level_vanishing": False,
        "cohomological_vanishing": False,
        "cohomological_vanishing_established": False,
        "comparison_data_required": True,
        "resolution": (
            "The local P2 guide shows non-adjacent raw terms.  It is not a "
            "compact CY3 construction and does not prove cohomological "
            "vanishing without TCFT comparison data or an HH^{-2} theorem."
        ),
    }


# =========================================================================
# 7. CHAIN LEVEL VS COHOMOLOGY
# =========================================================================


@dataclass(frozen=True)
class ChainVsCohomologyDistinction:
    """Precise status of raw chain and conditional class statements."""

    def chain_level_identity_holds(self) -> bool:
        """Raw termwise chain vanishing is false."""
        return False

    def cohomological_vanishing_holds(self) -> bool:
        """No unconditional class vanishing is proved for the raw target."""
        return False

    def homotopy_coherent_vanishing_holds(self) -> bool:
        """No universal raw homotopy ``d(h_k)`` is supplied."""
        return False

    def which_is_needed_for_programme(self) -> str:
        """Name the actual proof obligation."""
        return (
            "a class in C^bullet_End(CC_*(A)) or HH^{-2}_{E_1}(A,A), "
            "with theta_TCFT or the HH^{-2} filtration theorem"
        )

    def formal_algebras_are_strict(self) -> bool:
        """If all ``m_k`` for ``k>=3`` vanish, the target commutator is zero."""
        return True

    def non_formal_gap_resolved(self) -> bool:
        """Non-formal raw termwise failure is not resolved by formality alone."""
        return False


# =========================================================================
# 8. RESOLUTION OBJECT
# =========================================================================


@dataclass
class ObsAinfResolution:
    """Repaired status object for the ``Obs_Ainf`` target."""

    tsygan_data: TsyganFormalityData
    costello_data: CostelloTCFTFormality
    gap_analysis: GapAnalysis
    comparison: TsyganComparison
    chain_vs_cohomology: ChainVsCohomologyDistinction
    proof_steps: List[TsyganProofStep]

    def obs_ainf_vanishes_cohomologically(self) -> bool:
        """Default raw target: not established."""
        return self.comparison.sufficient_for_programme()

    def proposition_status(self) -> str:
        """Status of the old proposition after repair."""
        if self.obs_ainf_vanishes_cohomologically():
            return "Conditional class statement with named comparison data"
        return (
            "Rejected for raw B_term^{(2)}; conditional only after theta_TCFT "
            "or the HH^{-2} filtration theorem"
        )

    def impact_on_obstruction_landscape(self) -> Dict[str, str]:
        """Corrected landscape entries for the A_infinity obstruction."""
        return {
            "C^3": "0 [formal, chain-level]",
            "conifold": "0 [formal, chain-level]",
            "local_P^2": "nonzero for B_term^{(2)} [noncompact guide]",
            "quintic": "conditional [needs compact comparison or HH^{-2} theorem]",
            "K3_x_E": "not closed by Tsygan alone [compact TCFT/BV data required]",
        }

    def summary(self) -> Dict[str, Any]:
        """Full repaired summary."""
        return {
            "main_result": (
                "Universal raw termwise vanishing/exactness is rejected. "
                "The strict cyclic CY3 witness has "
                "[m_3, B_term^{(2)}][a|a|a|a|b] = 2 alpha [b] != 0."
            ),
            "costello": (
                "Costello gives the corrected total identity "
                "{sum_k b_k, B_TCFT^{(2)}} = 0 after correction data."
            ),
            "cohomological_statement": (
                f"Conditional: formulate the class in {OBSTRUCTION_COMPLEX} "
                f"with {COMPARISON_MAP}, or in {DERIVED_E1_COMPLEX} under "
                f"{FILTERED_HYPOTHESIS}."
            ),
            "proposition_status": self.proposition_status(),
            "landscape": self.impact_on_obstruction_landscape(),
            "proof_step_count": len(self.proof_steps),
            "dependencies": [
                "Tsygan (1999): mixed-complex formality for (CC,b,B)",
                "Costello (2007): corrected open--closed TCFT identity",
                "standalone/m3_b2_obstruction_vol3.tex: strict witness",
            ],
            "does_NOT_prove": [
                "termwise [m_k, B_term^{(2)}] = 0",
                "universal raw exactness [m_k, B_term^{(2)}] = d(h_k)",
                "compact S^3-framing programme closure without hypotheses",
            ],
        }


def resolve_obs_ainf(
    comparison: TsyganComparison | None = None,
) -> ObsAinfResolution:
    """Construct the repaired status object."""
    return ObsAinfResolution(
        tsygan_data=TsyganFormalityData(),
        costello_data=CostelloTCFTFormality(cy_dimension=3),
        gap_analysis=GapAnalysis(),
        comparison=comparison or TsyganComparison(),
        chain_vs_cohomology=ChainVsCohomologyDistinction(),
        proof_steps=construct_proof(),
    )


# =========================================================================
# 9. SCHEMATIC COMMUTATOR OUTPUT
# =========================================================================


@dataclass
class CommutatorTerm:
    """A schematic term in the raw commutator."""

    sign: int
    description: str
    is_adjacent: bool
    contributes_to_chain_level: bool
    vanishes_in_cohomology: bool


def compute_commutator_m3_b2_local_p2(bar_length: int = 5) -> Dict[str, Any]:
    """Return the raw nonzero status plus the strict witness.

    The function name is retained for compatibility.  The decisive oracle is
    the strict cyclic CY3 witness, not a compact local P2 theorem.
    """
    non_adj = enumerate_non_adjacent_terms(bar_length, mk_arity=3)
    witness = strict_cyclic_cy3_witness()
    all_terms = [
        CommutatorTerm(
            sign=1,
            description="m_3 after B_term^{(2)}: contributes to strict witness",
            is_adjacent=False,
            contributes_to_chain_level=True,
            vanishes_in_cohomology=False,
        ),
        CommutatorTerm(
            sign=-1,
            description="B_term^{(2)} after m_3: contributes to strict witness",
            is_adjacent=False,
            contributes_to_chain_level=True,
            vanishes_in_cohomology=False,
        ),
    ]

    return {
        "bar_length": bar_length,
        "total_terms_schematic": len(all_terms),
        "non_adjacent_terms": len([term for term in all_terms if not term.is_adjacent]),
        "chain_level_vanishing": False,
        "cohomological_vanishing": False,
        "cohomological_vanishing_established": False,
        "comparison_data_required": True,
        "non_adjacent_count_enumerated": len(non_adj),
        "strict_witness": witness,
        "explanation": (
            "The raw termwise commutator is strictly nonzero on the cyclic "
            "CY3 witness.  Costello's corrected TCFT operator or the "
            "HH^{-2} theorem is a separate input."
        ),
    }


# =========================================================================
# 10. MASTER VERIFICATION
# =========================================================================


def verify_tsygan_resolution() -> Dict[str, Any]:
    """Run the repaired verification."""
    resolution = resolve_obs_ainf()
    witness = strict_cyclic_cy3_witness()

    assert resolution.tsygan_data.applies_to_cy3()
    assert not resolution.tsygan_data.gives_chain_level_vanishing()
    assert not resolution.tsygan_data.gives_cohomological_vanishing()

    assert resolution.costello_data.b2_is_formal()
    assert resolution.costello_data.total_tcft_identity_holds()
    assert not resolution.costello_data.termwise_identity_holds()
    assert not resolution.costello_data.raw_term_operator_identified()

    assert resolution.gap_analysis.gap_exists_chain_level()
    assert not resolution.gap_analysis.gap_closed_cohomology()

    assert witness["commutator"] == witness["expected"]
    assert not witness["chain_level_vanishing"]
    assert not witness["cohomological_vanishing_established"]

    assert not resolution.comparison.sufficient_for_programme()
    assert not resolution.obs_ainf_vanishes_cohomologically()
    assert "Rejected" in resolution.proposition_status()

    return resolution.summary()


# =========================================================================
# 11. NON-ADJACENT TERM COUNTS BY BAR LENGTH
# =========================================================================


def non_adjacent_term_table(
    max_bar_length: int = 10,
    mk_arity: int = 3,
) -> List[Dict[str, int]]:
    """Table of raw non-adjacent term counts by bar length."""
    table = []
    for n in range(mk_arity, max_bar_length + 1):
        terms = enumerate_non_adjacent_terms(n, mk_arity)
        table.append({
            "bar_length": n,
            "mk_arity": mk_arity,
            "total_terms": len(terms),
            "non_adjacent": len([term for term in terms if not term.is_adjacent()]),
        })
    return table


# =========================================================================
# 12. OBSTRUCTION LANDSCAPE
# =========================================================================


def upgraded_obstruction_landscape() -> Dict[str, Dict[str, str]]:
    """Landscape after rejecting the false Tsygan/formality strengthening."""
    return {
        "C^3": {
            "Obs_top": "0 [proved: pi_3(BSp) = 0]",
            "Obs_Ainf": "0 [formal, chain-level]",
            "Obs_BV": "0 [proved: toric equivariance]",
            "total": "resolved on formal toric data",
        },
        "conifold": {
            "Obs_top": "0 [proved: pi_3(BSp) = 0]",
            "Obs_Ainf": "0 [formal, chain-level]",
            "Obs_BV": "0 [proved: toric equivariance]",
            "total": "resolved on formal toric data",
        },
        "local_P^2": {
            "Obs_top": "0 [proved: pi_3(BSp) = 0]",
            "Obs_Ainf": "nonzero for raw B_term^{(2)} [noncompact guide]",
            "Obs_BV": "0 [toric equivariance guide]",
            "total": "diagnostic only, not compact S^3 closure",
        },
        "quintic": {
            "Obs_top": "0 [proved: pi_3(BSp) = 0]",
            "Obs_Ainf": "conditional on theta_TCFT or HH^{-2} theorem",
            "Obs_BV": "perturbative: Cech-HTT convergence",
            "total": "open beyond stated hypotheses",
        },
        "K3_x_E": {
            "Obs_top": "0 [proved: pi_3(BSp) = 0]",
            "Obs_Ainf": "not closed by Tsygan alone",
            "Obs_BV": "conditional on compact correction data",
            "total": "conditional",
        },
    }
