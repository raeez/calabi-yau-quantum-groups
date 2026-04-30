r"""Diagnostics for the Stasheff--B^{(2)} obstruction.

This module is an attack-healed replacement for the old
``Obs_{A_inf}=0`` bidegree proof.

The corrected facts are separated into three carriers.

1.  The raw terminal-slot pair contraction ``B^{(2)}_term`` is not a
    chain-level cancellation theorem.  In the strict cyclic CY_3 witness
    used by ``standalone/m3_b2_obstruction_vol3.tex``,

        [m_3, B^{(2)}_term] [a|a|a|a|b] = 2 alpha [b] != 0.

2.  Degree bookkeeping for ``b_k`` and a corrected TCFT hierarchy remains
    useful as a diagnostic.  Same-degree partner slots tell where a total
    TCFT boundary identity would have to place correction terms.  They do
    not prove termwise vanishing.

3.  A vanishing statement is conditional data, not a universal output of
    this engine: either a Costello TCFT correction datum supplies the total
    corrected anticommutator, or an explicit HH^{-2} filtration theorem
    kills the derived obstruction class.

All arithmetic is exact.  The file intentionally keeps the public names of
the old engine so downstream tests fail on mathematical content rather than
on import churn.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product as cartesian_product
from typing import Any, Dict, List, Tuple

F = Fraction
Word = Tuple[str, ...]


# =========================================================================
# 0.  ABSTRACT CYCLIC A-INFINITY ALGEBRA
# =========================================================================


@dataclass(frozen=True)
class Generator:
    """A generator of a cyclic A-infinity algebra."""

    index: int
    degree: int = 0
    label: str = ""

    def __repr__(self) -> str:
        return self.label if self.label else f"a_{self.index}"


class CyclicAInfAlgebra:
    r"""A finite cyclic A-infinity algebra oracle.

    The oracle only checks Stasheff and cyclic-invariance identities for
    explicitly stored operations.  It is not a proof that a raw
    ``B^{(2)}_term`` commutator vanishes.
    """

    def __init__(
        self,
        generators: List[Generator],
        cy_dim: int,
        m_data: Dict[Tuple[int, ...], List[Tuple[int, Fraction]]],
        pairing_data: Dict[Tuple[int, int], Fraction],
        max_k: int = 4,
    ):
        self.generators = generators
        self.gen_by_index = {g.index: g for g in generators}
        self.N = len(generators)
        self.cy_dim = cy_dim
        self.m_data = m_data
        self.pairing_data = pairing_data
        self.max_k = max_k

    def pairing(self, i: int, j: int) -> Fraction:
        """The CY pairing ``<a_i, a_j>``."""

        return self.pairing_data.get((i, j), F(0))

    def m_k(self, indices: Tuple[int, ...]) -> List[Tuple[int, Fraction]]:
        """Evaluate ``m_k(a_{i_1}, ..., a_{i_k})``."""

        return self.m_data.get(indices, [])

    def stasheff_identity(self, input_indices: Tuple[int, ...]) -> Dict[int, Fraction]:
        r"""Evaluate the Stasheff identity at arity ``len(input_indices)``."""

        n = len(input_indices)
        result: Dict[int, Fraction] = defaultdict(F)

        for q in range(2, n + 1):
            p = n + 1 - q
            if p < 2:
                continue
            for s0 in range(p):
                if s0 + q > n:
                    continue
                inner = input_indices[s0:s0 + q]
                inner_result = self.m_k(inner)
                if not inner_result:
                    continue
                sign = F((-1) ** (s0 * (q - 1)))
                for io, ic in inner_result:
                    outer = input_indices[:s0] + (io,) + input_indices[s0 + q:]
                    for oo, oc in self.m_k(outer):
                        result[oo] += sign * ic * oc

        return dict(result)

    def verify_stasheff(self, max_arity: int) -> Dict[int, Dict[str, Any]]:
        """Verify Stasheff identities at all arities up to ``max_arity``."""

        results: Dict[int, Dict[str, Any]] = {}
        for n in range(3, max_arity + 1):
            violations = []
            for indices in cartesian_product(range(self.N), repeat=n):
                for idx, coeff in self.stasheff_identity(indices).items():
                    if coeff != F(0):
                        violations.append({"input": indices, "output": idx, "residual": coeff})
            results[n] = {"passed": len(violations) == 0, "violations": violations[:5]}
        return results

    def verify_cyclic_invariance(self, k: int) -> Dict[str, Any]:
        r"""Verify the stored cyclic invariance identity for ``m_k``."""

        violations = []
        for indices in cartesian_product(range(self.N), repeat=k + 1):
            lhs = sum(c * self.pairing(o, indices[k]) for o, c in self.m_k(indices[:k]))
            sign = F((-1) ** k)
            rhs = sign * sum(c * self.pairing(indices[0], o) for o, c in self.m_k(indices[1:k + 1]))
            if lhs != rhs:
                violations.append({"indices": indices, "lhs": lhs, "rhs": rhs})
        return {"k": k, "passed": len(violations) == 0, "violations": violations[:5]}


# =========================================================================
# 1.  DEGREE BOOKKEEPING AS DIAGNOSTIC DATA
# =========================================================================


@dataclass(frozen=True)
class ConnesHierarchySpec:
    r"""Degree bookkeeping for a corrected TCFT hierarchy.

    The diagnostic convention matches the repaired bidegree engine:

    * ``b_k`` has bar-length degree ``-(k-1)``.
    * ``B^{(j)}`` in the corrected hierarchy has degree ``1 - 2j``.
    * ``[b_k, B^{(j)}]`` has degree ``2 - k - 2j``.

    Equal values of ``k + 2j`` identify same-degree partner slots.  This
    table is not a vanishing proof for ``B^{(2)}_term``.
    """

    cy_dim: int

    @property
    def levels(self) -> List[int]:
        return list(range(self.cy_dim + 1))

    def b_k_degree(self, k: int) -> int:
        if k < 1:
            raise ValueError(f"A-infinity arity k must be >= 1, got {k}")
        return -(k - 1)

    def degree_shift(self, j: int) -> int:
        """Bar-length degree of the corrected hierarchy operator ``B^{(j)}``."""

        if j < 0:
            raise ValueError(f"Hierarchy level j must be >= 0, got {j}")
        return 1 - 2 * j

    def commutator_degree(self, k: int, j: int) -> int:
        """Bar-length degree of ``[b_k, B^{(j)}]``."""

        return self.b_k_degree(k) + self.degree_shift(j)

    def commutator_output(self, k: int, j: int, n: int) -> int:
        """Output bar length of ``[b_k, B^{(j)}]`` on bar length ``n``."""

        return n + self.commutator_degree(k, j)

    def total_weight(self, k: int, j: int) -> int:
        """Same-degree weight ``s = k + 2j``."""

        return k + 2 * j

    def bidegree_grouping(self, s: int, k_min: int = 1) -> List[Tuple[int, int]]:
        """All ``(k, j)`` with same diagnostic weight ``s = k + 2j``."""

        pairs = []
        for j in self.levels:
            k = s - 2 * j
            if k >= k_min:
                pairs.append((k, j))
        return pairs

    def mixed_complex_identity(self, k_min: int = 1, s_max: int = 8) -> Dict[int, List[Tuple[int, int]]]:
        """Return same-degree groups only; no vanishing is asserted."""

        result = {}
        for s in range(k_min, s_max + 1):
            pairs = self.bidegree_grouping(s, k_min=k_min)
            if pairs:
                result[s] = pairs
        return result


@dataclass(frozen=True)
class BidegreeDecomposition:
    r"""Same-degree partner slots for a corrected TCFT hierarchy.

    Partner slots become cancellation terms only after a corrected TCFT
    representative and comparison data have been supplied.
    """

    cy_dim: int
    hierarchy: ConnesHierarchySpec

    def identity_at_weight(self, s: int) -> Dict[str, Any]:
        pairs = self.hierarchy.bidegree_grouping(s)
        terms = [f"[b_{{{k}}}, B^{{({j})}}]" for k, j in pairs]
        return {
            "weight": s,
            "pairs": pairs,
            "num_terms": len(terms),
            "degree": 2 - s,
            "identity_if_tcft_data": " + ".join(terms) + " = 0" if terms else "0 = 0",
            "identity_status": "conditional_tcft",
            "proves_termwise_vanishing": False,
            "requires": "corrected TCFT hierarchy and comparison data",
        }

    def b2_cancellation_partners(self, k: int) -> Dict[str, Any]:
        r"""Return same-degree partner slots for ``[b_k, B^{(2)}]``.

        The legacy name is retained for imports.  The result explicitly
        records that cancellation is not established for the raw termwise
        operator.
        """

        s = self.hierarchy.total_weight(k, 2)
        all_pairs = self.hierarchy.bidegree_grouping(s)
        partners = [(kp, jp) for kp, jp in all_pairs if (kp, jp) != (k, 2)]
        partner_terms = [f"[b_{{{kp}}}, B^{{({jp})}}]" for kp, jp in partners]
        return {
            "k": k,
            "target": (k, 2),
            "total_weight": s,
            "same_degree_partners": partners,
            "partners": partners,
            "num_partners": len(partners),
            "conditional_identity": (
                f"[b_{{{k}}}, B^{{(2)}}] = -(" + " + ".join(partner_terms) + ")"
                if partner_terms
                else f"[b_{{{k}}}, B^{{(2)}}] = 0"
            ),
            "termwise_cancellation_established": False,
            "requires_tcft_correction_datum": True,
            "claim": "same-degree diagnostic only; no raw termwise cancellation follows",
        }

    def formal_case(self) -> Dict[str, Any]:
        return {
            "formal": True,
            "consequence": (
                "If m_k=0 for k>=3, the higher A-infinity part of the "
                "m_k--B^{(2)} obstruction is absent.  This is a formal-case "
                "diagnostic, not a universal non-formal theorem."
            ),
            "termwise_universal_vanishing": False,
        }

    def nonformal_case(self, max_k: int = 5) -> Dict[str, Any]:
        identities = {k: self.b2_cancellation_partners(k) for k in range(3, max_k + 1)}
        return {
            "formal": False,
            "consequence": (
                "The strict m_3 witness shows raw termwise nonvanishing. "
                "Same-degree partners mark where corrected TCFT terms would "
                "enter after the required datum is supplied."
            ),
            "identities": identities,
        }


# =========================================================================
# 2.  FORMAL SANITY CHECK
# =========================================================================


def build_formal_cyclic_algebra() -> CyclicAInfAlgebra:
    r"""The formal Frobenius algebra ``k[x]/(x^2)``.

    This is a sanity check for Stasheff and cyclic bookkeeping.  Since
    ``m_k=0`` for ``k>=3``, it has no higher A-infinity obstruction term.
    """

    gens = [Generator(0, label="e"), Generator(1, label="x")]
    pairing = {(0, 1): F(1), (1, 0): F(1), (0, 0): F(0), (1, 1): F(0)}
    m_data: Dict[Tuple[int, ...], List[Tuple[int, Fraction]]] = {
        (0, 0): [(0, F(1))],
        (0, 1): [(1, F(1))],
        (1, 0): [(1, F(1))],
        (1, 1): [],
    }
    return CyclicAInfAlgebra(gens, cy_dim=1, m_data=m_data, pairing_data=pairing, max_k=2)


def verify_formal_algebra() -> Dict[str, Any]:
    """Verify the formal Frobenius algebra sanity check."""

    alg = build_formal_cyclic_algebra()
    stasheff = alg.verify_stasheff(max_arity=5)
    cyclic = alg.verify_cyclic_invariance(2)
    return {
        "algebra": "k[x]/(x^2), formal Frobenius algebra",
        "stasheff": stasheff,
        "cyclic_invariance_m2": cyclic,
        "higher_ainf_obstruction": "absent because m_k=0 for k>=3",
    }


# =========================================================================
# 3.  STRICT TERMwise WITNESS
# =========================================================================


@dataclass(frozen=True)
class TermwiseCommutatorWitness:
    """Exact strict witness for raw ``[m_3, B^{(2)}_term]`` nonvanishing."""

    alpha: Fraction
    input_word: Word
    b2_term_of_input: Dict[Word, Fraction]
    m3_after_b2_term: Dict[Word, Fraction]
    m3_of_input: Dict[Word, Fraction]
    b2_term_after_m3: Dict[Word, Fraction]
    commutator: Dict[Word, Fraction]
    convention: str

    @property
    def coefficient_on_b(self) -> Fraction:
        return self.commutator.get(("b",), F(0))

    @property
    def nonzero(self) -> bool:
        return any(coeff != F(0) for coeff in self.commutator.values())

    def summary(self) -> Dict[str, Any]:
        return {
            "input_word": self.input_word,
            "m3_after_b2_term": self.m3_after_b2_term,
            "b2_term_after_m3": self.b2_term_after_m3,
            "commutator": self.commutator,
            "coefficient_on_b": self.coefficient_on_b,
            "nonzero": self.nonzero,
            "convention": self.convention,
        }


def strict_m3_b2_term_witness(alpha: Fraction = F(1)) -> TermwiseCommutatorWitness:
    r"""Return the strict nonzero witness from the standalone theorem.

    With terminal-slot normalization,

    * ``B^{(2)}_term [a|a|a|a|b] = 4 [a|a|a]``;
    * ``m_3 B^{(2)}_term`` gives ``4 alpha [b]``;
    * ``m_3`` first gives ``alpha([b|a|b] + [a|b|b])``;
    * ``B^{(2)}_term m_3`` gives ``2 alpha [b]``.
    """

    input_word = ("a", "a", "a", "a", "b")
    return TermwiseCommutatorWitness(
        alpha=alpha,
        input_word=input_word,
        b2_term_of_input={("a", "a", "a"): F(4)},
        m3_after_b2_term={("b",): F(4) * alpha},
        m3_of_input={("b", "a", "b"): alpha, ("a", "b", "b"): alpha},
        b2_term_after_m3={("b",): F(2) * alpha},
        commutator={("b",): F(2) * alpha},
        convention="terminal-slot B^{(2)}_term, characteristic zero",
    )


# =========================================================================
# 4.  OBSTRUCTION ANALYSIS
# =========================================================================


@dataclass(frozen=True)
class TCFTCorrectionData:
    """Hypotheses needed before a corrected total cancellation may be claimed."""

    moduli_chain_corrections: bool = False
    open_closed_tcft_chain_map: bool = False
    comparison_to_obstruction_complex: bool = False
    hh_minus_two_filtration_theorem: bool = False

    @property
    def total_tcft_identity_available(self) -> bool:
        return self.moduli_chain_corrections and self.open_closed_tcft_chain_map

    @property
    def derived_obstruction_vanishes(self) -> bool:
        return self.comparison_to_obstruction_complex and self.hh_minus_two_filtration_theorem


@dataclass(frozen=True)
class ObsAinfAnalysis:
    """Verdict for a specific obstruction carrier."""

    is_formal: bool
    individual_mk_b2_vanish: bool
    obstruction_vanishing_established: bool
    raw_termwise_witness_nonzero: bool
    corrected_tcft_identity_established: bool
    derived_hh_vanishing_established: bool
    mechanism: str
    proof_steps: List[str]

    @property
    def obs_ainf_zero(self) -> bool:
        """Backward-compatible name for established obstruction vanishing."""

        return self.obstruction_vanishing_established


def analyze_obs_ainf_formal() -> ObsAinfAnalysis:
    """Formal sanity case: no higher ``m_k`` obstruction terms are present."""

    return ObsAinfAnalysis(
        is_formal=True,
        individual_mk_b2_vanish=True,
        obstruction_vanishing_established=True,
        raw_termwise_witness_nonzero=False,
        corrected_tcft_identity_established=False,
        derived_hh_vanishing_established=False,
        mechanism="Formal case: m_k=0 for k>=3, so the higher A-infinity obstruction term is absent.",
        proof_steps=[
            "Formal input: m_k=0 for k>=3.",
            "The strict m_3 witness cannot occur in this class.",
            "This does not imply raw termwise cancellation for non-formal algebras.",
        ],
    )


def analyze_obs_ainf_nonformal() -> ObsAinfAnalysis:
    """Non-formal raw termwise verdict."""

    witness = strict_m3_b2_term_witness()
    return ObsAinfAnalysis(
        is_formal=False,
        individual_mk_b2_vanish=False,
        obstruction_vanishing_established=False,
        raw_termwise_witness_nonzero=witness.nonzero,
        corrected_tcft_identity_established=False,
        derived_hh_vanishing_established=False,
        mechanism=(
            "Raw B^{(2)}_term fails on a strict non-formal CY_3 witness; "
            "corrected TCFT data or an HH^{-2} filtration theorem is required."
        ),
        proof_steps=[
            "Witness input x=[a|a|a|a|b].",
            "m_3 B^{(2)}_term x = 4 alpha [b].",
            "B^{(2)}_term m_3 x = 2 alpha [b].",
            "[m_3,B^{(2)}_term]x = 2 alpha [b] != 0.",
            "Same-degree partner slots are diagnostic until a corrected TCFT representative is supplied.",
        ],
    )


def analyze_corrected_tcft(data: TCFTCorrectionData) -> ObsAinfAnalysis:
    """Conditional corrected-TCFT/HH obstruction analysis."""

    total_identity = data.total_tcft_identity_available
    derived_zero = data.derived_obstruction_vanishes
    established = total_identity and derived_zero
    return ObsAinfAnalysis(
        is_formal=False,
        individual_mk_b2_vanish=False,
        obstruction_vanishing_established=established,
        raw_termwise_witness_nonzero=True,
        corrected_tcft_identity_established=total_identity,
        derived_hh_vanishing_established=derived_zero,
        mechanism=(
            "Corrected total cancellation is available only for B^{(2)}_TCFT "
            "with Costello correction data; derived obstruction vanishing also "
            "requires the HH^{-2} filtration comparison."
        ),
        proof_steps=[
            f"TCFT moduli-chain corrections supplied: {data.moduli_chain_corrections}.",
            f"Open-closed TCFT chain map supplied: {data.open_closed_tcft_chain_map}.",
            f"Comparison to obstruction complex supplied: {data.comparison_to_obstruction_complex}.",
            f"HH^(-2) filtration theorem supplied: {data.hh_minus_two_filtration_theorem}.",
        ],
    )


# =========================================================================
# 5.  CORRECTED CLAIM STATUS
# =========================================================================


def corrected_proposition() -> Dict[str, Any]:
    r"""Return the healed claim status for the old proposition."""

    witness = strict_m3_b2_term_witness()
    return {
        "original_claim": "[m_k, B^{(2)}_term] = 0 for all k>=3",
        "original_status": "INCORRECT for non-formal algebras",
        "termwise_witness": witness.summary(),
        "old_per_k_proof_status": "REJECTED",
        "old_bidegree_proof_status": "REJECTED",
        "corrected_claim": (
            "A total cancellation may be asserted only for the corrected "
            "operator B^{(2)}_TCFT after Costello correction data and the "
            "comparison to the obstruction complex are supplied.  Derived "
            "vanishing additionally requires the HH^{-2} filtration theorem."
        ),
        "corrected_status": "Conditional",
        "universal_obs_ainf_zero": False,
        "formal_case": "Higher A-infinity obstruction terms are absent when m_k=0 for k>=3.",
        "nonformal_case": "Raw termwise commutator has a strict nonzero witness.",
        "resolves": "old universal closure claim rejected; proof obligations named",
        "mechanism": "strict witness + diagnostic degree bookkeeping + conditional TCFT/HH hypotheses",
    }


def weight_identities_cy3() -> Dict[int, Dict[str, Any]]:
    """Same-degree groups for the corrected CY_3 hierarchy.

    The entries are conditional TCFT identities, not raw termwise
    identities.  The target ``[b_3, B^{(2)}]`` lies at weight ``7``.
    """

    spec = ConnesHierarchySpec(cy_dim=3)
    decomp = BidegreeDecomposition(cy_dim=3, hierarchy=spec)
    identities: Dict[int, Dict[str, Any]] = {}
    for s in range(1, 8):
        identities[s] = decomp.identity_at_weight(s)
    return identities


# =========================================================================
# 6.  MASTER RESULT
# =========================================================================


@dataclass(frozen=True)
class StasheffCancellationResult:
    """Top-level verdict for the Stasheff cancellation engine."""

    gap_classified: bool
    gap_resolved: bool
    original_claim_correct: bool
    corrected_claim: str
    mechanism: str
    obs_ainf_vanishes: bool
    universal_closure_rejected: bool
    formal_analysis: ObsAinfAnalysis
    nonformal_analysis: ObsAinfAnalysis
    weight_identities: Dict[int, Dict[str, Any]]
    termwise_witness: TermwiseCommutatorWitness
    proof_steps: List[str]
    remaining_proof_obligations: List[str] = field(default_factory=list)

    def summary(self) -> Dict[str, Any]:
        return {
            "gap_classified": self.gap_classified,
            "gap_resolved": self.gap_resolved,
            "original_claim_correct": self.original_claim_correct,
            "corrected_claim": self.corrected_claim,
            "mechanism": self.mechanism,
            "obs_ainf_vanishes": self.obs_ainf_vanishes,
            "universal_closure_rejected": self.universal_closure_rejected,
            "formal_obs_ainf": self.formal_analysis.obs_ainf_zero,
            "nonformal_obs_ainf": self.nonformal_analysis.obs_ainf_zero,
            "raw_witness_nonzero": self.termwise_witness.nonzero,
            "remaining_proof_obligations": self.remaining_proof_obligations,
        }


def compute_stasheff_cancellation_obs_ainf() -> StasheffCancellationResult:
    """Compute the attack-healed Stasheff obstruction verdict."""

    formal = analyze_obs_ainf_formal()
    nonformal = analyze_obs_ainf_nonformal()
    identities = weight_identities_cy3()
    witness = strict_m3_b2_term_witness()

    formal_alg = build_formal_cyclic_algebra()
    stasheff_check = formal_alg.verify_stasheff(max_arity=4)
    cyclic_check = formal_alg.verify_cyclic_invariance(2)
    stasheff_ok = all(r["passed"] for r in stasheff_check.values())
    cyclic_ok = cyclic_check["passed"]

    proof_steps = [
        "Step 1: Formal sanity check k[x]/(x^2) verifies Stasheff and cyclic bookkeeping.",
        f"Step 2: Formal check results: Stasheff={stasheff_ok}, cyclic={cyclic_ok}.",
        "Step 3: The non-formal strict witness has [m_3,B^{(2)}_term]x=2 alpha [b].",
        "Step 4: Therefore the original per-k raw termwise vanishing claim is false.",
        "Step 5: Same-degree partner slots for the corrected hierarchy are diagnostic only.",
        "Step 6: Total cancellation requires B^{(2)}_TCFT with Costello correction data.",
        "Step 7: Derived obstruction vanishing requires the HH^{-2} filtration comparison.",
    ]

    return StasheffCancellationResult(
        gap_classified=True,
        gap_resolved=False,
        original_claim_correct=False,
        corrected_claim=(
            "Universal raw Obs_Ainf closure is rejected.  Conditional closure "
            "requires corrected TCFT hierarchy data and the HH^{-2} comparison theorem."
        ),
        mechanism="strict nonzero witness; degree bookkeeping retained as diagnostic",
        obs_ainf_vanishes=False,
        universal_closure_rejected=True,
        formal_analysis=formal,
        nonformal_analysis=nonformal,
        weight_identities=identities,
        termwise_witness=witness,
        proof_steps=proof_steps,
        remaining_proof_obligations=[
            "Specify the Costello moduli-chain correction datum for B^{(2)}_TCFT.",
            "Give the chain-level comparison map to the S^3-framing obstruction complex.",
            "Prove the HH^{-2} filtration hypotheses for the strictified model under study.",
        ],
    )
