r"""Connes B / Obs_Ainf diagnostics for the CY3 strict term.

Corrected carrier distinction
=============================

There are three different objects in the S^3-framing obstruction lane.

1. ``B^{(2)}_term`` is the raw pair-contraction operator on a strict
   cyclic bar model.  It is not Costello's corrected TCFT operator.
2. ``B^{(2)}_TCFT`` is the corrected operator obtained only after a
   moduli-chain correction datum is chosen.
3. The derived obstruction class lives in ``HH^{-2}_{E_1}`` and vanishes
   only under an explicit filtration theorem.

The strict cyclic CY3 witness is the four-generator model

    |e| = 0, |a| = 1, |b| = 2, |w| = 3,
    <e,w> = 1, <a,b> = 1, m_3(a,a,a) = alpha b.

With the terminal-slot raw pair contraction,

    B^{(2)}_term[a|a|a|a|b] = 4[a|a|a],
    m_3 B^{(2)}_term[a|a|a|a|b] = 4 alpha [b],
    B^{(2)}_term m_3[a|a|a|a|b] = 2 alpha [b],

so

    [m_3,B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0

in characteristic zero.  Thus Connes identities and bidegree labels alone
do not prove compact CY3 S^3-framing closure.

This module preserves the valid facts:

* the classical Connes mixed-complex identity for ``B^{(0)}``;
* formal/Frobenius cases where higher ``m_k`` vanish or the binary
  Frobenius identity applies;
* Costello's corrected total TCFT identity under its correction datum;
* ``HH^{-2}`` vanishing under the explicit complete/separated/strongly
  convergent filtration and empty total degree ``-2`` line hypotheses.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

F = Fraction


# =========================================================================
# 0. Degree diagnostics
# =========================================================================


@dataclass(frozen=True)
class BidegreeShift:
    r"""Diagnostic degree label of an operation.

    ``proof_grading`` records whether the label is a genuine grading that can
    isolate an identity.  For the raw ``B^{(2)}_term`` target it is false:
    the pairing-weight label names which pairing component was used, but it
    is not an independent target grading proving termwise vanishing.
    """

    hochschild_shift: int
    pairing_weight: int
    proof_grading: bool = False
    normalization: str = "diagnostic"

    @property
    def determines_k(self) -> Optional[int]:
        """Legacy inverse for the old formal label, when applicable."""
        if self.normalization != "legacy_formal_label":
            return None
        return 2 - self.hochschild_shift - self.pairing_weight

    @property
    def determines_j(self) -> Optional[int]:
        """Legacy inverse for the old formal label, when applicable."""
        if self.normalization != "legacy_formal_label":
            return None
        return self.pairing_weight


def bidegree_of_mk(k: int) -> BidegreeShift:
    r"""Degree shift of ``m_k`` on Hochschild chains.

    ``m_k`` replaces ``k`` adjacent factors by one factor, hence shifts
    Hochschild degree by ``-(k-1)``.  It uses no CY pairing.
    """

    if k < 1:
        raise ValueError(f"m_k requires k >= 1, got k={k}")
    return BidegreeShift(
        hochschild_shift=-(k - 1),
        pairing_weight=0,
        proof_grading=True,
        normalization="bar_length",
    )


def bidegree_of_bj(j: int) -> BidegreeShift:
    r"""Diagnostic degree shift of ``B^{(j)}``.

    ``j=0`` is the classical Connes operator: it inserts the unit and raises
    Hochschild degree by one.

    For ``j>=1`` this engine records the raw one-pair contraction normalised
    by the strict witness.  The operator removes two tensor factors and has
    Hochschild shift ``-2``.  The ``pairing_weight`` is a label, not a proof
    grading.
    """

    if j < 0:
        raise ValueError(f"B^{{(j)}} requires j >= 0, got j={j}")
    if j == 0:
        return BidegreeShift(
            hochschild_shift=1,
            pairing_weight=0,
            proof_grading=True,
            normalization="classical_connes_B0",
        )
    return BidegreeShift(
        hochschild_shift=-2,
        pairing_weight=j,
        proof_grading=False,
        normalization="raw_pair_contraction",
    )


def bidegree_of_commutator(k: int, j: int) -> BidegreeShift:
    r"""Diagnostic degree shift of ``[m_k, B^{(j)}]``.

    The output is useful for arity bookkeeping.  It is not a vanishing proof
    for ``j>=1`` because the raw pair-contraction operator is not the
    corrected TCFT chain.
    """

    mk_bd = bidegree_of_mk(k)
    bj_bd = bidegree_of_bj(j)
    return BidegreeShift(
        hochschild_shift=mk_bd.hochschild_shift + bj_bd.hochschild_shift,
        pairing_weight=mk_bd.pairing_weight + bj_bd.pairing_weight,
        proof_grading=mk_bd.proof_grading and bj_bd.proof_grading,
        normalization=(
            "classical_connes_B0" if j == 0 else "raw_pair_contraction"
        ),
    )


# =========================================================================
# 1. Strict witness
# =========================================================================


@dataclass(frozen=True)
class StrictCY3Witness:
    """The strict cyclic CY3 witness for nonzero raw termwise commutator."""

    alpha: Fraction
    input_word: Tuple[str, ...] = ("a", "a", "a", "a", "b")
    b2_term_output_coeff: Fraction = Fraction(0)
    m3_after_b2_coeff: Fraction = Fraction(0)
    b2_after_m3_coeff: Fraction = Fraction(0)
    commutator_coeff: Fraction = Fraction(0)

    @property
    def nonzero(self) -> bool:
        return self.commutator_coeff != 0

    @property
    def statement(self) -> str:
        return (
            "[m_3,B_term^(2)][a|a|a|a|b] = "
            f"{self.commutator_coeff} [b]"
        )


def strict_cy3_witness(alpha: Fraction | int = F(1)) -> StrictCY3Witness:
    """Return the normalized strict CY3 ``m_3``--``B^{(2)}_term`` witness."""

    alpha = F(alpha)
    return StrictCY3Witness(
        alpha=alpha,
        b2_term_output_coeff=4,
        m3_after_b2_coeff=4 * alpha,
        b2_after_m3_coeff=2 * alpha,
        commutator_coeff=2 * alpha,
    )


def termwise_commutator_verdict(k: int = 3, j: int = 2) -> Dict[str, Any]:
    r"""Verdict for the universal termwise claim ``[m_k,B_term^(j)] = 0``."""

    if k == 3 and j == 2:
        witness = strict_cy3_witness()
        return {
            "claim": "[m_3, B_term^(2)] = 0 universally",
            "status": "false",
            "vanishes": False,
            "witness": witness,
            "reason": witness.statement + " != 0 in characteristic zero.",
        }
    return {
        "claim": f"[m_{k}, B_term^({j})] = 0 universally",
        "status": "not_established",
        "vanishes": False,
        "witness": None,
        "reason": (
            "No universal termwise theorem follows from Connes identities. "
            "Use a formal/Frobenius hypothesis, a corrected TCFT datum, or "
            "an HH^{-2} filtration theorem."
        ),
    }


# =========================================================================
# 2. Corrected positive mechanisms
# =========================================================================


def corrected_tcft_identity(
    has_moduli_chain_correction: bool,
) -> Dict[str, Any]:
    r"""Costello's corrected total TCFT identity.

    The positive statement is total:

        {b, B_TCFT^(2)} = 0,  b = sum_k b_k.

    It is not a per-``k`` identity and it does not identify
    ``B_TCFT^(2)`` with ``B_term^(2)``.
    """

    if has_moduli_chain_correction:
        return {
            "status": "proved_total_identity_under_correction_datum",
            "total_identity_holds": True,
            "per_k_identity_holds": False,
            "raw_operator_identified": False,
            "identity": "{sum_k b_k, B_TCFT^(2)} = 0",
            "reason": (
                "Costello's compactified moduli-chain boundary gives the "
                "total corrected anticommutator after non-principal faces "
                "are absorbed into B_TCFT^(2)."
            ),
        }
    return {
        "status": "missing_moduli_chain_correction",
        "total_identity_holds": False,
        "per_k_identity_holds": False,
        "raw_operator_identified": False,
        "identity": None,
        "reason": (
            "The correction datum is part of the theorem's hypotheses. "
            "The raw termwise contraction is not enough."
        ),
    }


def hh_minus_two_filtration_vanishes(
    *,
    complete: bool,
    exhaustive: bool,
    separated: bool,
    strongly_convergent: bool,
    empty_total_degree_minus_two_line: bool,
) -> Dict[str, Any]:
    r"""Check the explicit hypotheses for ``HH^{-2}_{E_1}`` vanishing."""

    hypotheses = {
        "complete": complete,
        "exhaustive": exhaustive,
        "separated": separated,
        "strongly_convergent": strongly_convergent,
        "empty_total_degree_minus_two_line": empty_total_degree_minus_two_line,
    }
    missing = [name for name, holds in hypotheses.items() if not holds]
    vanishes = not missing
    return {
        "status": (
            "proved_under_explicit_filtration_hypotheses"
            if vanishes
            else "not_established"
        ),
        "vanishes": vanishes,
        "missing_hypotheses": missing,
        "proof": (
            "The total degree -2 line is empty on E_1; every later page is "
            "a subquotient; strong convergence and separated completeness "
            "force HH^{-2}_{E_1}=0."
            if vanishes
            else "Connectivity and H^0=k do not replace the missing checks."
        ),
    }


def formal_frobenius_case(
    *,
    higher_operations_vanish: bool,
    frobenius_invariant_product: bool,
) -> Dict[str, Any]:
    r"""Formal/Frobenius cases where the termwise obstruction is harmless."""

    higher_target_zero = higher_operations_vanish
    binary_connes_ok = frobenius_invariant_product
    return {
        "status": (
            "proved_formal_frobenius_case"
            if higher_target_zero and binary_connes_ok
            else "not_established"
        ),
        "higher_commutators_vanish": higher_target_zero,
        "classical_binary_identity_holds": binary_connes_ok,
        "sufficient_for_termwise_target": higher_target_zero and binary_connes_ok,
        "reason": (
            "For k>=3 the operations m_k vanish; the remaining binary "
            "identity is the Frobenius/Connes mixed-complex identity."
            if higher_target_zero and binary_connes_ok
            else "A non-formal higher operation or non-Frobenius product "
            "requires separate data."
        ),
    }


# =========================================================================
# 3. Decomposition diagnostics
# =========================================================================


@dataclass
class CommutatorDecompositionEntry:
    """One diagnostic entry for a commutator term."""

    k: int
    j: int
    hochschild_shift: int
    pairing_weight: int
    vanishes_individually: bool
    reason: str
    status: str = "not_established"


@dataclass
class DecompositionResult:
    r"""Result of the rejected bidegree decomposition attempt."""

    entries: List[CommutatorDecompositionEntry]
    max_k: int
    max_j: int
    projection_is_proof: bool = False
    raw_termwise_universal_vanishing: bool = False

    @property
    def all_vanish_individually(self) -> bool:
        return all(e.vanishes_individually for e in self.entries)

    def obs_ainf_resolved(self) -> bool:
        """Whether raw termwise ``Obs_Ainf`` is resolved universally."""

        return self.raw_termwise_universal_vanishing

    def target_entry(self, k: int = 3, j: int = 2) -> CommutatorDecompositionEntry:
        for entry in self.entries:
            if entry.k == k and entry.j == j:
                return entry
        raise KeyError(f"No entry for k={k}, j={j}")


def _entry_status(k: int, j: int) -> Tuple[bool, str, str]:
    if k == 2 and j == 0:
        return (
            True,
            "proved_classical_connes",
            "[m_2,B^(0)] is the classical Rinehart/Connes identity.",
        )
    if k == 3 and j == 2:
        return (
            False,
            "false_for_raw_term",
            "Strict CY3 witness gives [m_3,B_term^(2)] != 0.",
        )
    if k >= 3 and j == 2:
        return (
            False,
            "not_established",
            "Degree labels do not prove raw termwise vanishing.",
        )
    return (
        False,
        "not_established",
        "No per-term vanishing follows from the total Connes/TCFT identity.",
    )


def decompose_b_B_identity(max_k: int = 8, max_j: int = 5) -> DecompositionResult:
    r"""Return the corrected verdict on the old bidegree proof.

    The table is retained as diagnostic data.  It deliberately does not mark
    raw higher commutators as vanishing.
    """

    entries: List[CommutatorDecompositionEntry] = []
    for k in range(2, max_k + 1):
        for j in range(0, max_j + 1):
            bd = bidegree_of_commutator(k, j)
            vanishes, status, reason = _entry_status(k, j)
            entries.append(
                CommutatorDecompositionEntry(
                    k=k,
                    j=j,
                    hochschild_shift=bd.hochschild_shift,
                    pairing_weight=bd.pairing_weight,
                    vanishes_individually=vanishes,
                    status=status,
                    reason=reason,
                )
            )
    return DecompositionResult(entries=entries, max_k=max_k, max_j=max_j)


def verify_bidegree_injectivity(max_k: int = 50, max_j: int = 20) -> Dict[str, Any]:
    r"""Verify the old formal label map and reject its proof use."""

    seen: Dict[Tuple[int, int], Tuple[int, int]] = {}
    collisions: List[Tuple[int, int, Tuple[int, int]]] = []
    for k in range(2, max_k + 1):
        for j in range(0, max_j + 1):
            key = (2 - k - j, j)
            if key in seen:
                collisions.append((k, j, seen[key]))
            else:
                seen[key] = (k, j)

    return {
        "injective": len(collisions) == 0,
        "inverse_valid": True,
        "num_pairs_checked": (max_k - 1) * (max_j + 1),
        "collisions": collisions,
        "projection_valid": False,
        "termwise_vanishing_established": False,
        "algebraic_proof": (
            "The formal label phi(k,j)=(2-k-j,j) is injective. "
            "This is only label bookkeeping: pairing weight is not an "
            "independent target grading for the raw termwise operator, and "
            "Costello's theorem applies to B_TCFT, not B_term."
        ),
    }


@dataclass
class TwoStepDecomposition:
    r"""The old two-step proof, kept as a rejected proof object."""

    step1_identity: str
    step1_proof: str
    step2_identity: str
    step2_proof: str
    conclusion: str
    valid: bool = False

    @classmethod
    def construct(cls) -> "TwoStepDecomposition":
        return cls(
            step1_identity="Rejected for B_term^(2)",
            step1_proof=(
                "Costello gives a corrected total TCFT identity only after "
                "moduli-chain correction data.  It does not give "
                "[b,B_term^(2)] = 0."
            ),
            step2_identity="Rejected as a vanishing projection",
            step2_proof=(
                "Bidegree labels are useful arity diagnostics, but they do "
                "not turn the corrected TCFT identity into per-k raw "
                "termwise identities."
            ),
            conclusion=(
                "The universal strict claim [m_k,B_term^(2)] = 0 is false; "
                "the strict CY3 witness has commutator 2 alpha [b]."
            ),
            valid=False,
        )


def bidegree_table(max_k: int = 8, max_j: int = 5) -> List[Dict[str, Any]]:
    """Generate the diagnostic table for ``[m_k,B^{(j)}]``."""

    result = decompose_b_B_identity(max_k=max_k, max_j=max_j)
    return [
        {
            "k": e.k,
            "j": e.j,
            "hochschild_shift": e.hochschild_shift,
            "pairing_weight": e.pairing_weight,
            "bidegree": (e.hochschild_shift, e.pairing_weight),
            "vanishes": e.vanishes_individually,
            "status": e.status,
            "reason": e.reason,
        }
        for e in result.entries
    ]


def single_grading_decomposition(max_k: int = 8, max_j: int = 5) -> Dict[str, Any]:
    """Show that Hochschild degree alone is insufficient."""

    groups: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    for k in range(2, max_k + 1):
        for j in range(0, max_j + 1):
            groups[2 - k - j].append((k, j))
    degenerate = {s: pairs for s, pairs in groups.items() if len(pairs) > 1}
    singleton = {s: pairs for s, pairs in groups.items() if len(pairs) == 1}
    return {
        "total_shifts": len(groups),
        "singleton_shifts": len(singleton),
        "degenerate_shifts": len(degenerate),
        "single_grading_sufficient": False,
        "pairing_weight_projection_sufficient": False,
        "example_degeneracy": dict(list(degenerate.items())[:3]),
        "conclusion": (
            "Hochschild degree alone is insufficient, and adding the "
            "pairing-weight label does not prove raw termwise vanishing."
        ),
    }


# =========================================================================
# 4. CY dimension summaries
# =========================================================================


@dataclass
class CYDimensionAnalysis:
    """Diagnostic CY-dimension summary for the raw termwise target."""

    cy_dim: int
    max_k: int
    target_j: int

    def relevant_commutators(self) -> List[Tuple[int, int]]:
        return [(k, self.target_j) for k in range(3, self.max_k + 1)]

    def all_bidegrees_unique(self) -> bool:
        labels = set()
        for k, j in self.relevant_commutators():
            bd = bidegree_of_commutator(k, j)
            labels.add((bd.hochschild_shift, bd.pairing_weight))
        return len(labels) == len(self.relevant_commutators())

    def obs_ainf_vanishes(self) -> Dict[str, Any]:
        return {
            "cy_dim": self.cy_dim,
            "target": f"[m_k, B_term^({self.target_j})] = 0 for k >= 3",
            "all_bidegrees_unique": self.all_bidegrees_unique(),
            "unique_bidegrees_prove_vanishing": False,
            "termwise_universal_vanishing": False,
            "status": "not_proved_termwise",
            "proof_obligation": (
                "Supply formal/Frobenius hypotheses, a Costello correction "
                "datum for the total TCFT operator, or an HH^{-2} filtration "
                "vanishing theorem."
            ),
        }


def obs_ainf_cy3(max_k: int = 50) -> Dict[str, Any]:
    """Raw termwise CY3 ``Obs_Ainf`` verdict."""

    return CYDimensionAnalysis(3, max_k, 2).obs_ainf_vanishes()


def obs_ainf_cy2(max_k: int = 50) -> Dict[str, Any]:
    """Raw termwise CY2 ``Obs_Ainf`` verdict."""

    return CYDimensionAnalysis(2, max_k, 1).obs_ainf_vanishes()


def obs_ainf_general(cy_dim: int, max_k: int = 50) -> Dict[str, Any]:
    """Raw termwise CYd ``Obs_Ainf`` verdict."""

    return CYDimensionAnalysis(cy_dim, max_k, cy_dim - 1).obs_ainf_vanishes()


# =========================================================================
# 5. Non-adjacent gap and manuscript implications
# =========================================================================


@dataclass
class NonAdjacentResolution:
    """Status of the non-adjacent contraction gap."""

    k: int
    j: int = 2
    gap_resolved: bool = False

    def adjacent_terms_description(self) -> str:
        return (
            f"Adjacent terms for m_{self.k} are the terms cyclic/Frobenius "
            "invariance can control in formal or binary settings."
        )

    def non_adjacent_terms_description(self) -> str:
        return (
            f"Non-adjacent terms pair one input inside the m_{self.k}-block "
            "with one outside it.  Cyclic invariance does not control them."
        )

    def resolution(self) -> str:
        return (
            f"The raw non-adjacent gap is not resolved by bidegree labels. "
            f"For k={self.k}, j={self.j}, the strict CY3 witness gives a "
            f"nonzero commutator when k=3, j=2.  Use B_TCFT^(2) with "
            f"moduli-chain correction data or an HH^(-2) filtration theorem."
        )


def resolve_non_adjacent_gap(k: int = 3) -> NonAdjacentResolution:
    """Construct the corrected non-adjacent-gap verdict."""

    return NonAdjacentResolution(k=k, j=2, gap_resolved=False)


@dataclass
class ManuscriptImplications:
    """Implications of the corrected engine."""

    prop_status_before: str = "ClaimStatusConditional"
    prop_status_after: str = "ClaimStatusConditional"
    proof_method_before: str = "cyclic invariance plus bidegree projection"
    proof_method_after: str = "termwise proof rejected; TCFT/HH hypotheses required"
    gap_resolved: bool = False

    def landscape_updates(self) -> List[Dict[str, str]]:
        return [
            {
                "geometry": "formal Frobenius examples",
                "before": "Obs_Ainf = 0 by universal bidegree proof",
                "after": "Obs_Ainf termwise harmless because m_k=0 for k>=3",
            },
            {
                "geometry": "strict non-formal CY3 model",
                "before": "Obs_Ainf = 0 by bidegree projection",
                "after": "[m_3,B_term^(2)] is nonzero on [a|a|a|a|b]",
            },
            {
                "geometry": "compact CY3 S^3-framing",
                "before": "closed by Connes identities alone",
                "after": "requires Costello correction data or HH^{-2} hypotheses",
            },
        ]


def manuscript_implications() -> ManuscriptImplications:
    """Construct corrected manuscript implications."""

    return ManuscriptImplications()


# =========================================================================
# 6. Mixed-complex prerequisite
# =========================================================================


def verify_mixed_complex_axiom_prerequisite() -> Dict[str, Any]:
    r"""Classical Connes mixed-complex fact and its boundary."""

    return {
        "axiom": "b B^(0) + B^(0) b = 0 for the classical mixed complex",
        "status": "proved_for_classical_B0",
        "classical_B0": True,
        "raw_hierarchy_connes_only": False,
        "corrected_tcft_requires_moduli_chain_correction": True,
        "used_in_decomposition": False,
        "references": [
            "Connes 1985 (associative cyclic complex)",
            "Loday 1992/1998 (cyclic homology mixed complexes)",
            "Keller 2006 (A_inf cyclic complexes)",
            "Costello 2007 (corrected TCFT operator with moduli chains)",
        ],
        "note": (
            "The classical mixed-complex identity is retained.  It does not "
            "identify B_term^(2) with B_TCFT^(2), does not prove per-k "
            "higher commutators, and does not close compact CY3 framing."
        ),
    }


# =========================================================================
# 7. Master verdict
# =========================================================================


@dataclass
class ConnesBObsAinfResolution:
    """Master verdict for the corrected Connes B / Obs_Ainf engine."""

    injectivity: Dict[str, Any]
    decomposition: DecompositionResult
    two_step: TwoStepDecomposition
    cy3_result: Dict[str, Any]
    non_adjacent: NonAdjacentResolution
    implications: ManuscriptImplications
    mixed_complex: Dict[str, Any]
    witness: StrictCY3Witness = field(default_factory=strict_cy3_witness)
    corrected_tcft: Dict[str, Any] = field(
        default_factory=lambda: corrected_tcft_identity(True)
    )
    hh_minus_two: Dict[str, Any] = field(
        default_factory=lambda: hh_minus_two_filtration_vanishes(
            complete=True,
            exhaustive=True,
            separated=True,
            strongly_convergent=True,
            empty_total_degree_minus_two_line=True,
        )
    )

    @property
    def resolved(self) -> bool:
        """Whether the old universal termwise claim is resolved as true."""

        return False

    @property
    def corrected_carriers_recorded(self) -> bool:
        return (
            self.witness.nonzero
            and self.corrected_tcft["total_identity_holds"]
            and self.hh_minus_two["vanishes"]
        )


def master_resolution() -> ConnesBObsAinfResolution:
    """Construct the complete corrected verdict."""

    return ConnesBObsAinfResolution(
        injectivity=verify_bidegree_injectivity(),
        decomposition=decompose_b_B_identity(),
        two_step=TwoStepDecomposition.construct(),
        cy3_result=obs_ainf_cy3(),
        non_adjacent=resolve_non_adjacent_gap(),
        implications=manuscript_implications(),
        mixed_complex=verify_mixed_complex_axiom_prerequisite(),
    )
