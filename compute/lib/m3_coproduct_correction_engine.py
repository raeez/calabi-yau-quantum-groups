r"""AP-CY34 boundary for the ``m_3`` coproduct-correction claim.

This engine records what the local computation proves and, more
importantly, what it does not prove.

Raw carrier.  The raw bar pair-contraction ``B_term^{(2)}`` has the
strict witness

    [m_3,B_term^{(2)}][a|a|a|a|b] = 2*alpha*[b].

For ``alpha != 0`` this blocks raw cancellation.  It also blocks the
legacy shortcut that identifies a raw bar-coproduct correction with
Costello's corrected open-closed TCFT operator.

Corrected carrier.  Costello's operator is ``B_TCFT^{(2)}``, not the raw
``B_term^{(2)}``.  A closure statement is available only after one of
the following pieces of data has been supplied:

1. an explicit corrected TCFT datum and comparison map, or
2. a precise ``HH^{-2}`` filtration theorem with comparison map, complete
   / exhaustive / separated filtration, strong convergence, and empty
   total-degree ``-2`` line.

No cyclicity, bidegree, topology, unit-connectedness, Dunn,
Goodwillie, DGMS/BTT/Kaledin, Cech-HTT, or Borel diagnostic in this file
proves universal compact CY3 ``Obs_Ainf=0``, ``HH^{-2}=0``, a
contractible lifting space, compact ``Phi_3``, Hall/CoHA, PBW, or
no-extra-relations.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

F = Fraction
Word = Tuple[str, ...]
LinComb = Dict[Word, Fraction]

RAW_OPERATOR = "B_term^{(2)}"
RAW_COPRODUCT = "raw bar-coproduct"
CORRECTED_OPERATOR = "B_TCFT^{(2)}"
STRICT_WITNESS_FORMULA = (
    "[m_3,B_term^{(2)}][a|a|a|a|b] = 2*alpha*[b]"
)

FORBIDDEN_DIAGNOSTICS = (
    "cyclicity",
    "bidegree",
    "topology",
    "unit-connectedness",
    "Dunn",
    "Goodwillie",
    "DGMS/BTT/Kaledin",
    "Cech-HTT",
    "Borel",
)

FORBIDDEN_UNIVERSAL_CONCLUSIONS = (
    "Obs_Ainf=0",
    "HH^{-2}=0",
    "contractible lifting space",
    "compact Phi_3",
    "Hall/CoHA",
    "PBW",
    "no-extra-relations",
)

ALLOWED_CLOSURE_ROUTES = (
    "explicit B_TCFT^{(2)} correction/comparison datum",
    (
        "HH^{-2} filtration theorem with comparison map, complete, "
        "exhaustive, separated, strongly convergent filtration, and "
        "empty total-degree -2 line"
    ),
)


class CorrectionDataRequired(RuntimeError):
    """Raised when a caller asks for a corrected operator without data."""


def _clean(lc: LinComb) -> LinComb:
    """Remove zero coefficients from a linear combination."""

    return {word: coeff for word, coeff in lc.items() if coeff != 0}


def _sub(left: LinComb, right: LinComb) -> LinComb:
    """Subtract two exact bar-word linear combinations."""

    out: Dict[Word, Fraction] = dict(left)
    for word, coeff in right.items():
        out[word] = out.get(word, F(0)) - coeff
    return _clean(out)


@dataclass(frozen=True)
class RawM3CoproductWitness:
    r"""Exact witness against raw ``m_3`` / coproduct cancellation."""

    alpha: Fraction
    input_word: Word
    raw_b_term_of_input: LinComb
    m3_after_raw_b_term: LinComb
    m3_of_input: LinComb
    raw_b_term_after_m3: LinComb
    commutator: LinComb
    raw_operator: str = RAW_OPERATOR
    raw_coproduct: str = RAW_COPRODUCT
    corrected_operator: str = CORRECTED_OPERATOR
    convention: str = "terminal-slot raw B_term^{(2)}, characteristic zero"

    @property
    def coefficient_on_b(self) -> Fraction:
        """Coefficient of the output word ``[b]``."""

        return self.commutator.get(("b",), F(0))

    @property
    def nonzero_for_alpha_nonzero(self) -> bool:
        """Whether the strict witness blocks raw cancellation."""

        return self.alpha != 0 and self.coefficient_on_b != 0

    @property
    def raw_cancellation_blocked(self) -> bool:
        """Alias for the AP-CY34 blocking condition."""

        return self.nonzero_for_alpha_nonzero

    @property
    def raw_equals_corrected(self) -> bool:
        """The raw pair-contraction is not Costello's corrected operator."""

        return False

    @property
    def formula(self) -> str:
        """Human-readable strict witness formula."""

        return STRICT_WITNESS_FORMULA

    def summary(self) -> Dict[str, Any]:
        """Return a stable dictionary form for tests and reports."""

        return {
            "alpha": self.alpha,
            "input_word": self.input_word,
            "raw_operator": self.raw_operator,
            "raw_coproduct": self.raw_coproduct,
            "corrected_operator": self.corrected_operator,
            "raw_equals_corrected": self.raw_equals_corrected,
            "raw_b_term_of_input": self.raw_b_term_of_input,
            "m3_after_raw_b_term": self.m3_after_raw_b_term,
            "m3_of_input": self.m3_of_input,
            "raw_b_term_after_m3": self.raw_b_term_after_m3,
            "commutator": self.commutator,
            "coefficient_on_b": self.coefficient_on_b,
            "expected_coefficient_on_b": F(2) * self.alpha,
            "nonzero_for_alpha_nonzero": self.nonzero_for_alpha_nonzero,
            "raw_cancellation_blocked": self.raw_cancellation_blocked,
            "formula": self.formula,
            "convention": self.convention,
        }


def strict_m3_coproduct_witness(alpha: Fraction = F(1)) -> RawM3CoproductWitness:
    r"""Return the exact AP-CY34 raw-coproduct witness.

    Normalization:

    * ``B_term^{(2)}[a|a|a|a|b] = 4[a|a|a]``;
    * ``m_3(a,a,a) = alpha*b``;
    * ``m_3 B_term^{(2)}`` gives ``4*alpha [b]``;
    * ``B_term^{(2)} m_3`` gives ``2*alpha [b]``.

    The commutator is therefore ``2*alpha [b]``.
    """

    alpha = F(alpha)
    raw_b_term_of_input = {("a", "a", "a"): F(4)}
    m3_after_raw_b_term = {("b",): F(4) * alpha}
    m3_of_input = {
        ("b", "a", "b"): alpha,
        ("a", "b", "b"): alpha,
    }
    raw_b_term_after_m3 = {("b",): F(2) * alpha}
    commutator = _sub(m3_after_raw_b_term, raw_b_term_after_m3)
    return RawM3CoproductWitness(
        alpha=alpha,
        input_word=("a", "a", "a", "a", "b"),
        raw_b_term_of_input=_clean(raw_b_term_of_input),
        m3_after_raw_b_term=_clean(m3_after_raw_b_term),
        m3_of_input=_clean(m3_of_input),
        raw_b_term_after_m3=_clean(raw_b_term_after_m3),
        commutator=commutator,
    )


@dataclass(frozen=True)
class TCFTCorrectionDatum:
    r"""Data required to use Costello's corrected ``B_TCFT^{(2)}``."""

    corrected_operator_supplied: bool = False
    raw_to_tcft_comparison_map: bool = False
    moduli_chain_boundary_corrections: bool = False
    open_closed_tcft_chain_map: bool = False
    orientation_signs_fixed: bool = False
    obstruction_complex_comparison: bool = False

    @property
    def complete(self) -> bool:
        """Whether the corrected TCFT route may be used."""

        return all(
            [
                self.corrected_operator_supplied,
                self.raw_to_tcft_comparison_map,
                self.moduli_chain_boundary_corrections,
                self.open_closed_tcft_chain_map,
                self.orientation_signs_fixed,
                self.obstruction_complex_comparison,
            ]
        )

    @property
    def missing_hypotheses(self) -> List[str]:
        """Missing TCFT inputs."""

        checks = [
            (self.corrected_operator_supplied, "supply B_TCFT^{(2)}"),
            (
                self.raw_to_tcft_comparison_map,
                "comparison map from B_term^{(2)} to B_TCFT^{(2)}",
            ),
            (
                self.moduli_chain_boundary_corrections,
                "Costello moduli-chain boundary corrections",
            ),
            (self.open_closed_tcft_chain_map, "open-closed TCFT chain map"),
            (self.orientation_signs_fixed, "Costello orientation/sign data"),
            (
                self.obstruction_complex_comparison,
                "comparison to the S^3-framing obstruction complex",
            ),
        ]
        return [label for ok, label in checks if not ok]


def complete_tcft_correction_datum() -> TCFTCorrectionDatum:
    """Return the complete conditional TCFT datum."""

    return TCFTCorrectionDatum(
        corrected_operator_supplied=True,
        raw_to_tcft_comparison_map=True,
        moduli_chain_boundary_corrections=True,
        open_closed_tcft_chain_map=True,
        orientation_signs_fixed=True,
        obstruction_complex_comparison=True,
    )


@dataclass(frozen=True)
class HHMinusTwoFiltrationTheorem:
    r"""Hypotheses for the ``HH^{-2}`` vanishing route."""

    comparison_map: bool = False
    filtration_complete: bool = False
    filtration_exhaustive: bool = False
    filtration_separated: bool = False
    strong_convergence: bool = False
    empty_total_degree_minus_two_line: bool = False
    obstruction_complex_comparison: bool = False

    @property
    def complete(self) -> bool:
        """Whether the HH route proves the primary vanishing statement."""

        return all(
            [
                self.comparison_map,
                self.filtration_complete,
                self.filtration_exhaustive,
                self.filtration_separated,
                self.strong_convergence,
                self.empty_total_degree_minus_two_line,
                self.obstruction_complex_comparison,
            ]
        )

    @property
    def missing_hypotheses(self) -> List[str]:
        """Missing HH^{-2} inputs."""

        checks = [
            (self.comparison_map, "HH^{-2} comparison map"),
            (self.filtration_complete, "complete HH^{-2} filtration"),
            (self.filtration_exhaustive, "exhaustive HH^{-2} filtration"),
            (self.filtration_separated, "separated HH^{-2} filtration"),
            (self.strong_convergence, "strong convergence to HH^{-2}"),
            (
                self.empty_total_degree_minus_two_line,
                "empty total-degree -2 line",
            ),
            (
                self.obstruction_complex_comparison,
                "comparison to the S^3-framing obstruction complex",
            ),
        ]
        return [label for ok, label in checks if not ok]


def complete_hh_minus_two_filtration_theorem() -> HHMinusTwoFiltrationTheorem:
    """Return the complete conditional HH^{-2} filtration theorem."""

    return HHMinusTwoFiltrationTheorem(
        comparison_map=True,
        filtration_complete=True,
        filtration_exhaustive=True,
        filtration_separated=True,
        strong_convergence=True,
        empty_total_degree_minus_two_line=True,
        obstruction_complex_comparison=True,
    )


def diagnostic_attempt(
    diagnostic: str,
    conclusion: str,
) -> Dict[str, Any]:
    """Reject diagnostic-only proofs of compact CY3 closure."""

    diagnostic_is_forbidden = diagnostic in FORBIDDEN_DIAGNOSTICS
    conclusion_is_forbidden = conclusion in FORBIDDEN_UNIVERSAL_CONCLUSIONS
    rejected = diagnostic_is_forbidden and conclusion_is_forbidden
    return {
        "diagnostic": diagnostic,
        "conclusion": conclusion,
        "allowed": not rejected,
        "rejected": rejected,
        "reason": (
            f"{diagnostic} does not imply universal compact CY3 {conclusion}"
            if rejected
            else "not an AP-CY34 forbidden diagnostic/conclusion pair"
        ),
    }


@dataclass(frozen=True)
class M3CoproductCorrectionVerdict:
    """Carrier-separated verdict for the m3/coproduct correction."""

    witness: RawM3CoproductWitness
    tcft_datum: TCFTCorrectionDatum
    hh_theorem: HHMinusTwoFiltrationTheorem
    raw_cancellation_valid: bool
    raw_equals_corrected: bool
    tcft_identity_established: bool
    hh_minus_two_zero_established: bool
    obs_ainf_zero_established: bool
    contractible_lifting_space_established: bool
    compact_phi3_established: bool
    hall_coha_established: bool
    pbw_established: bool
    no_extra_relations_established: bool
    allowed_closure_routes: Tuple[str, ...]
    rejected_diagnostics: Tuple[str, ...]
    remaining_obligations: Tuple[str, ...]
    status: str

    def summary(self) -> Dict[str, Any]:
        """Return a stable dictionary form for tests and reports."""

        return {
            "witness": self.witness.summary(),
            "raw_cancellation_valid": self.raw_cancellation_valid,
            "raw_equals_corrected": self.raw_equals_corrected,
            "tcft_identity_established": self.tcft_identity_established,
            "hh_minus_two_zero_established": self.hh_minus_two_zero_established,
            "obs_ainf_zero_established": self.obs_ainf_zero_established,
            "contractible_lifting_space_established": (
                self.contractible_lifting_space_established
            ),
            "compact_phi3_established": self.compact_phi3_established,
            "hall_coha_established": self.hall_coha_established,
            "pbw_established": self.pbw_established,
            "no_extra_relations_established": self.no_extra_relations_established,
            "allowed_closure_routes": self.allowed_closure_routes,
            "rejected_diagnostics": self.rejected_diagnostics,
            "remaining_obligations": self.remaining_obligations,
            "status": self.status,
        }


def m3_coproduct_correction_verdict(
    alpha: Fraction = F(1),
    tcft_datum: Optional[TCFTCorrectionDatum] = None,
    hh_theorem: Optional[HHMinusTwoFiltrationTheorem] = None,
) -> M3CoproductCorrectionVerdict:
    """Return the AP-CY34 verdict for the chosen data."""

    witness = strict_m3_coproduct_witness(alpha)
    tcft = tcft_datum or TCFTCorrectionDatum()
    hh = hh_theorem or HHMinusTwoFiltrationTheorem()

    tcft_ok = tcft.complete
    hh_ok = hh.complete
    obs_zero = tcft_ok or hh_ok

    remaining: List[str] = []
    if not tcft_ok:
        remaining.extend(tcft.missing_hypotheses)
    if not hh_ok:
        remaining.extend(hh.missing_hypotheses)
    remaining.extend(
        [
            "construct compact Phi_3 chain-level data separately",
            "supply compact Hall/CoHA comparison separately",
            "prove compact PBW/no-extra-relations separately",
        ]
    )

    if tcft_ok and hh_ok:
        status = "conditional closure by TCFT and HH^{-2} routes"
    elif tcft_ok:
        status = "conditional closure by corrected B_TCFT^{(2)} route"
    elif hh_ok:
        status = "conditional closure by HH^{-2} filtration route"
    elif witness.raw_cancellation_blocked:
        status = "open: raw witness blocks cancellation"
    else:
        status = "degenerate alpha=0: corrected data still required"

    return M3CoproductCorrectionVerdict(
        witness=witness,
        tcft_datum=tcft,
        hh_theorem=hh,
        raw_cancellation_valid=False,
        raw_equals_corrected=False,
        tcft_identity_established=tcft_ok,
        hh_minus_two_zero_established=hh_ok,
        obs_ainf_zero_established=obs_zero,
        contractible_lifting_space_established=False,
        compact_phi3_established=False,
        hall_coha_established=False,
        pbw_established=False,
        no_extra_relations_established=False,
        allowed_closure_routes=ALLOWED_CLOSURE_ROUTES,
        rejected_diagnostics=FORBIDDEN_DIAGNOSTICS,
        remaining_obligations=tuple(dict.fromkeys(remaining)),
        status=status,
    )


class M3CoproductCorrection:
    r"""Compatibility wrapper for the repaired AP-CY34 oracle.

    The old matrix-valued ``delta3_T`` interpretation is deliberately not
    provided as a raw correction.  Use ``strict_witness`` to see the
    obstruction and ``closure_verdict`` to check whether enough corrected
    data has been supplied.
    """

    def __init__(
        self,
        alpha: Fraction = F(1),
        *,
        Psi: Optional[Fraction] = None,
        N_max: Optional[int] = None,
    ):
        if Psi is not None:
            psi = F(Psi)
            if psi == 0:
                raise ValueError("Psi must be nonzero")
            alpha = (psi - F(1)) / psi
        self.alpha = F(alpha)
        self.Psi = None if Psi is None else F(Psi)
        self.N_max = N_max

    def strict_witness(self) -> RawM3CoproductWitness:
        """Return the exact raw witness for this ``alpha``."""

        return strict_m3_coproduct_witness(self.alpha)

    def closure_verdict(
        self,
        tcft_datum: Optional[TCFTCorrectionDatum] = None,
        hh_theorem: Optional[HHMinusTwoFiltrationTheorem] = None,
    ) -> M3CoproductCorrectionVerdict:
        """Return the corrected-data closure verdict."""

        return m3_coproduct_correction_verdict(
            self.alpha,
            tcft_datum=tcft_datum,
            hh_theorem=hh_theorem,
        )

    def delta3_T(self, n: int) -> None:
        """Reject the legacy raw sign-flip correction."""

        raise CorrectionDataRequired(
            "No raw matrix delta^(3)(T_n) is certified here. "
            f"The raw witness is {STRICT_WITNESS_FORMULA}; use "
            "B_TCFT^{(2)} correction/comparison data or the HH^{-2} "
            "filtration theorem."
        )

    def corrected_coproduct_T(
        self,
        n: int,
        z: complex = 0.0,
        *,
        tcft_datum: Optional[TCFTCorrectionDatum] = None,
        hh_theorem: Optional[HHMinusTwoFiltrationTheorem] = None,
    ) -> Dict[str, Any]:
        """Return a conditional corrected-coproduct record, not a raw matrix."""

        verdict = self.closure_verdict(
            tcft_datum=tcft_datum,
            hh_theorem=hh_theorem,
        )
        if not verdict.obs_ainf_zero_established:
            raise CorrectionDataRequired(
                "corrected coproduct requires B_TCFT^{(2)} comparison data "
                "or the HH^{-2} filtration theorem"
            )
        return {
            "mode": n,
            "spectral_parameter": z,
            "operator": (
                CORRECTED_OPERATOR
                if verdict.tcft_identity_established
                else "HH^{-2} route"
            ),
            "conditional": True,
            "status": verdict.status,
            "raw_matrix_supplied": False,
            "compact_phi3_established": False,
            "hall_coha_established": False,
            "pbw_established": False,
            "no_extra_relations_established": False,
        }


def compute_raw_witness(alpha: Fraction = F(1)) -> Dict[str, Any]:
    """Convenience entry point for the exact strict witness."""

    return strict_m3_coproduct_witness(alpha).summary()


def compute_delta3_T0(
    Psi: Fraction = F(2),
    N_max: int = 4,
) -> Dict[str, Any]:
    """Legacy entry point rewritten as an AP-CY34 boundary report."""

    engine = M3CoproductCorrection(Psi=Psi, N_max=N_max)
    verdict = engine.closure_verdict()
    report = verdict.summary()
    report["legacy_entry_point"] = "compute_delta3_T0"
    report["Psi"] = engine.Psi
    report["N_max"] = engine.N_max
    report["raw_delta3_matrix_supplied"] = False
    return report


def verify_all(alpha: Fraction = F(1)) -> Dict[str, Any]:
    """Run the targeted AP-CY34 verification surface."""

    default = m3_coproduct_correction_verdict(alpha)
    tcft = m3_coproduct_correction_verdict(
        alpha,
        tcft_datum=complete_tcft_correction_datum(),
    )
    hh = m3_coproduct_correction_verdict(
        alpha,
        hh_theorem=complete_hh_minus_two_filtration_theorem(),
    )
    diagnostic_checks = [
        diagnostic_attempt(diagnostic, conclusion)
        for diagnostic in FORBIDDEN_DIAGNOSTICS
        for conclusion in FORBIDDEN_UNIVERSAL_CONCLUSIONS
    ]

    all_ok = all(
        [
            default.witness.coefficient_on_b == F(2) * F(alpha),
            default.witness.raw_cancellation_blocked == (F(alpha) != 0),
            not default.raw_cancellation_valid,
            not default.raw_equals_corrected,
            not default.obs_ainf_zero_established,
            tcft.tcft_identity_established,
            tcft.obs_ainf_zero_established,
            not tcft.compact_phi3_established,
            hh.hh_minus_two_zero_established,
            hh.obs_ainf_zero_established,
            not hh.contractible_lifting_space_established,
            all(check["rejected"] for check in diagnostic_checks),
        ]
    )
    return {
        "strict_witness": default.witness.summary(),
        "default_verdict": default.summary(),
        "tcft_conditional_verdict": tcft.summary(),
        "hh_conditional_verdict": hh.summary(),
        "diagnostic_checks": diagnostic_checks,
        "all_ok": all_ok,
    }
