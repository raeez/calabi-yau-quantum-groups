r"""Adversarial stress tests for the CY-A_3 derived-framing theorem.

The corrected theorem separates three carriers.

* ``B_term^(2)`` is the raw bar pair-contraction operator.  It has the
  strict witness

      [m_3, B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0

  in characteristic zero.

* ``B_TCFT^(2)`` is Costello's corrected open-closed TCFT carrier.  The
  identity ``{b, B_TCFT^(2)} = 0`` is available only after the moduli-chain
  correction datum is supplied.  It is not a raw ``B_term^(2)`` shortcut.

* The derived obstruction class may be killed in ``HH^{-2}_{E_1}(A,A)``
  only after the comparison map to the obstruction complex and the complete,
  exhaustive, separated, strongly convergent filtration with empty total
  degree ``-2`` line have been supplied.

This module does not vote for the theorem.  It records pressure tests and
the proof obligations needed to pass them.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.derived_framing_obstruction import (
    HHMinusTwoFiltrationHypotheses,
    TCFTCorrectionDatum,
    complete_hh_minus_two_hypotheses,
    complete_tcft_correction_datum,
    compute_derived_framing_obstruction,
    strict_m3_b2_term_witness,
)

F = Fraction


# =========================================================================
# 1. ATTACK VECTOR DATA STRUCTURES
# =========================================================================


@dataclass
class AttackVector:
    r"""One adversarial attack on a proposed CY-A_3 proof step."""

    name: str
    target_proof: str
    target_step: str
    description: str
    severity: str
    survives: bool
    mitigation: str
    residual_gap: str
    proof_obligations: List[str] = field(default_factory=list)


@dataclass
class StressTestResult:
    r"""Complete result of the adversarial stress test."""

    attacks: List[AttackVector]
    proofs_survive: bool
    genuine_weaknesses: List[AttackVector]
    fatal_weaknesses: List[AttackVector]
    synthesis: str
    recommendation: str
    proof_obligations: List[str] = field(default_factory=list)


def _hh_minus_two_obligations(
    hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> List[str]:
    """Return missing hypotheses for the ``HH^{-2}`` vanishing theorem."""

    hyp = hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )
    return hyp.missing_hypotheses


def _tcft_obligations(
    hypotheses: Optional[TCFTCorrectionDatum] = None,
) -> List[str]:
    """Return missing hypotheses for the corrected Costello carrier."""

    datum = hypotheses or TCFTCorrectionDatum()
    return datum.missing_hypotheses


def strict_witness_summary(alpha: Fraction | int = F(1)) -> Dict[str, Any]:
    r"""Return the strict raw ``m_3``--``B_term^(2)`` witness.

    Normalization: terminal-slot ``B_term^(2)`` in characteristic zero.
    """

    witness = strict_m3_b2_term_witness(F(alpha))
    return {
        "input_word": witness.input_word,
        "commutator": witness.commutator,
        "coefficient_on_b": witness.coefficient_on_b,
        "nonzero": witness.nonzero,
        "formula": "[m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b]",
        "normalization": witness.convention,
    }


# =========================================================================
# 2. ATTACK 1: DUNN ADDITIVITY AND AUTOMATIC HH^{-2}
# =========================================================================


@dataclass
class DunnAdditivityCheck:
    r"""Check the exact scope of Dunn additivity."""

    ambient_category: str
    is_symmetric_monoidal: bool
    is_stable: bool
    dunn_applies: bool
    e3_in_chk_implies_e3_chiral: bool
    factorization_descent_proved: bool
    hh_minus_two_via_unit_connectedness: bool
    hh_minus_two_requires_filtration: bool
    space_contractible_established: bool
    gap_description: str
    required_hypotheses: List[str] = field(default_factory=list)


def check_dunn_additivity(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> DunnAdditivityCheck:
    r"""Check what Dunn additivity proves, and what it does not prove."""

    hyp = hh_hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )
    hh_zero = hyp.vanishing_established
    return DunnAdditivityCheck(
        ambient_category="Ch(k)",
        is_symmetric_monoidal=True,
        is_stable=True,
        dunn_applies=True,
        e3_in_chk_implies_e3_chiral=False,
        factorization_descent_proved=False,
        hh_minus_two_via_unit_connectedness=False,
        hh_minus_two_requires_filtration=True,
        space_contractible_established=False,
        gap_description=(
            "Dunn additivity applies in Ch(k).  It does not prove "
            "HH^{-2}_{E_1}(A,A)=0 from unit-connectedness, does not "
            "construct an E_3-chiral factorization algebra, and does not "
            "prove contractibility of the E_3-structure space.  The "
            "HH^{-2} claim needs the comparison map and the complete, "
            "exhaustive, separated, strongly convergent filtration with "
            "empty total degree -2 line."
        ),
        required_hypotheses=[] if hh_zero else hyp.missing_hypotheses,
    )


def attack_dunn_additivity() -> AttackVector:
    """Attack the stale Dunn/unit-connectedness shortcut."""

    check = check_dunn_additivity()
    return AttackVector(
        name="Dunn additivity does not prove HH^{-2}",
        target_proof="1",
        target_step="HH^{-2}_{E_1}(A,A)=0 from Dunn + unit-connectedness",
        description=(
            "The ambient category Ch(k) is valid for Dunn additivity, but "
            "the automatic negative Hochschild vanishing step is not.  "
            "Unit-connectedness is data for a model; it is not the spectral "
            "sequence comparison theorem."
        ),
        severity="fatal",
        survives=False,
        mitigation=(
            "Replace the shortcut by a conditional statement: the primary "
            "derived obstruction vanishes only after the comparison map and "
            "the named filtration hypotheses are supplied."
        ),
        residual_gap=(
            "Factorization descent and compact CY_3 closure remain outside "
            "Dunn additivity."
        ),
        proof_obligations=check.required_hypotheses,
    )


# =========================================================================
# 3. ATTACK 2: UNIT-CONNECTEDNESS CIRCULARITY
# =========================================================================


@dataclass
class UnitConnectednessCheck:
    r"""Check unit-connectedness without upgrading it to ``HH^{-2}``."""

    cat_hh0_dim: int
    cat_is_unit_connected: bool
    alg_hh0_dim: Optional[int]
    alg_is_unit_connected: Optional[bool]
    requires_phi: bool
    circularity_present: bool
    circularity_mitigated: bool
    hh_minus_two_vanishing_established: bool
    required_hypotheses: List[str]
    mitigation: str


def _unit_check(
    *,
    cat_hh0_dim: int,
    alg_hh0_dim: Optional[int],
    requires_phi: bool,
    circularity_present: bool,
    mitigation: str,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> UnitConnectednessCheck:
    hyp = hh_hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )
    return UnitConnectednessCheck(
        cat_hh0_dim=cat_hh0_dim,
        cat_is_unit_connected=(cat_hh0_dim == 1),
        alg_hh0_dim=alg_hh0_dim,
        alg_is_unit_connected=None if alg_hh0_dim is None else alg_hh0_dim == 1,
        requires_phi=requires_phi,
        circularity_present=circularity_present,
        circularity_mitigated=False,
        hh_minus_two_vanishing_established=hyp.vanishing_established,
        required_hypotheses=hyp.missing_hypotheses,
        mitigation=mitigation,
    )


def check_unit_connectedness_k3(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> UnitConnectednessCheck:
    """Check K3 as a CY_2 control, not as a CY_3 closure proof."""

    return _unit_check(
        cat_hh0_dim=2,
        alg_hh0_dim=1,
        requires_phi=True,
        circularity_present=False,
        mitigation=(
            "CY-A_2 supplies the K3 chiral algebra.  This is a control case; "
            "it does not prove compact CY_3 HH^{-2} vanishing."
        ),
        hh_hypotheses=hh_hypotheses,
    )


def check_unit_connectedness_local_p2(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> UnitConnectednessCheck:
    """Check local P^2 as a noncompact diagnostic, not a generic theorem."""

    return _unit_check(
        cat_hh0_dim=1,
        alg_hh0_dim=1,
        requires_phi=False,
        circularity_present=False,
        mitigation=(
            "The toric local model has a single degree-zero unit.  It still "
            "does not prove HH^{-2} without the derived filtration theorem."
        ),
        hh_hypotheses=hh_hypotheses,
    )


def check_unit_connectedness_quintic(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> UnitConnectednessCheck:
    """Check the compact quintic boundary."""

    return _unit_check(
        cat_hh0_dim=1,
        alg_hh0_dim=None,
        requires_phi=True,
        circularity_present=True,
        mitigation=(
            "The compact CY_3 chiral algebra is the object under "
            "construction.  HH^0(C)=k does not by itself establish "
            "HH^{-2}_{E_1}(A,A)=0."
        ),
        hh_hypotheses=hh_hypotheses,
    )


def check_unit_connectedness_k3xe(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> UnitConnectednessCheck:
    """Check the K3 x E product boundary."""

    return _unit_check(
        cat_hh0_dim=2,
        alg_hh0_dim=None,
        requires_phi=True,
        circularity_present=True,
        mitigation=(
            "K3 x E has categorical HH^0=k^2.  Product structure is useful "
            "diagnostic data, but it is not a replacement for the comparison "
            "map and filtration hypotheses."
        ),
        hh_hypotheses=hh_hypotheses,
    )


def attack_unit_connectedness() -> AttackVector:
    """Attack the generic unit-connectedness proof step."""

    obligations = _hh_minus_two_obligations()
    return AttackVector(
        name="Unit-connectedness is not HH^{-2} vanishing",
        target_proof="1, 2",
        target_step="unit-connectedness implies HH^{-2}_{E_1}(A,A)=0",
        description=(
            "The stale proof upgrades unit-connectedness to negative "
            "Hochschild vanishing.  The corrected theorem requires the "
            "explicit comparison and filtration statement.  For compact "
            "CY_3 objects, using HH^0(A,A) may also be circular because A "
            "is the object being constructed."
        ),
        severity="fatal",
        survives=False,
        mitigation=(
            "Record unit-connectedness as one input.  Do not let it close "
            "the obstruction group without the complete HH^{-2} hypotheses."
        ),
        residual_gap=(
            "Compact CY_3 examples still require the comparison map, empty "
            "total-degree -2 line, and convergence/separatedness checks."
        ),
        proof_obligations=obligations,
    )


# =========================================================================
# 4. ATTACK 3: ANDRE-QUILLEN / GOODWILLIE SHORTCUT
# =========================================================================


def attack_aq_cotangent() -> AttackVector:
    """Attack the stale AQ/Goodwillie automatic-vanishing claim."""

    return AttackVector(
        name="AQ and Goodwillie do not close the derived obstruction",
        target_proof="2",
        target_step="D^4_{E_2}(A,A)=0 from unit-connectedness/Goodwillie",
        description=(
            "The AQ and Goodwillie lanes may identify an obstruction carrier, "
            "but unit-connectedness and a connectivity slogan do not certify "
            "the comparison to HH^{-2}, strong convergence, or compact CY_3 "
            "closure."
        ),
        severity="moderate",
        survives=False,
        mitigation=(
            "Treat AQ/Goodwillie as a pressure test compatible with the "
            "filtration theorem, not as an independent automatic proof."
        ),
        residual_gap=(
            "The complete comparison map and filtration hypotheses remain "
            "load-bearing."
        ),
        proof_obligations=_hh_minus_two_obligations(),
    )


# =========================================================================
# 5. ATTACK 4: COSTELLO CARRIER DISTINCTION
# =========================================================================


@dataclass
class TCFTBIdentificationCheck:
    r"""Check ``B_term^(2)`` versus corrected ``B_TCFT^(2)``."""

    identification_valid: bool
    requires_strict_cyclicity: bool
    strict_cyclicity_known_formal: bool
    strict_cyclicity_known_nonformal: bool
    strictification_theorem_exists: bool
    explicit_strictification_for_compact_cy3: bool
    raw_term_identified_with_tcft: bool
    raw_termwise_commutator_vanishes: bool
    corrected_identity_available: bool
    strict_witness_coefficient: Fraction
    missing_correction_data: List[str] = field(default_factory=list)


def check_tcft_b_identification(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
) -> TCFTBIdentificationCheck:
    r"""Check the Costello carrier boundary."""

    datum = tcft_hypotheses or TCFTCorrectionDatum()
    witness = strict_m3_b2_term_witness()
    corrected = datum.total_tcft_identity_available
    return TCFTBIdentificationCheck(
        identification_valid=corrected,
        requires_strict_cyclicity=True,
        strict_cyclicity_known_formal=True,
        strict_cyclicity_known_nonformal=True,
        strictification_theorem_exists=True,
        explicit_strictification_for_compact_cy3=False,
        raw_term_identified_with_tcft=False,
        raw_termwise_commutator_vanishes=not witness.nonzero,
        corrected_identity_available=corrected,
        strict_witness_coefficient=witness.coefficient_on_b,
        missing_correction_data=datum.missing_hypotheses,
    )


def attack_tcft_b_identification() -> AttackVector:
    """Attack the raw Costello shortcut."""

    check = check_tcft_b_identification()
    return AttackVector(
        name="Raw B_term^(2) is not Costello B_TCFT^(2)",
        target_proof="3",
        target_step="{b,B^(2)}=0 via Costello TCFT",
        description=(
            "Costello supplies a corrected total TCFT identity, not the "
            "raw termwise identity for B_term^(2).  The strict witness has "
            "[m_3,B_term^(2)][a|a|a|a|b]=2 alpha [b] != 0."
        ),
        severity="fatal",
        survives=False,
        mitigation=(
            "Use B_TCFT^(2) only after the Costello moduli-chain correction "
            "datum, open-closed chain map, signs, and corrected representative "
            "are fixed."
        ),
        residual_gap=(
            "Without that datum, the TCFT carrier is absent and the raw "
            "operator fails."
        ),
        proof_obligations=check.missing_correction_data,
    )


# =========================================================================
# 6. ATTACK 5: COHOMOLOGICAL VS CHAIN-LEVEL
# =========================================================================


@dataclass
class CohomologicalVsChainCheck:
    r"""Check that obstruction vanishing is not a theorem vote."""

    existence_proved: bool
    explicit_construction_needed: bool
    construction_from_vanishing: bool
    primary_obstruction_conditionally_vanishes: bool
    corrected_tcft_identity_available: bool
    space_contractible_established: bool
    strict_witness_coefficient: Fraction
    what_proofs_actually_show: str
    what_cya3_actually_needs: str
    gap: str
    required_hypotheses: List[str] = field(default_factory=list)


def check_cohomological_vs_chain(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> CohomologicalVsChainCheck:
    """Check the boundary between conditional derived vanishing and closure."""

    result = compute_derived_framing_obstruction(
        algebra_name="Local P^2 strict witness",
        cy_dim=3,
        shadow_class="M",
        is_formal=False,
        has_nonzero_m3=True,
        tcft_hypotheses=tcft_hypotheses,
        hh_hypotheses=hh_hypotheses,
    )
    witness = result.raw_termwise_witness or strict_m3_b2_term_witness()
    return CohomologicalVsChainCheck(
        existence_proved=result.obstruction_vanishes,
        explicit_construction_needed=True,
        construction_from_vanishing=False,
        primary_obstruction_conditionally_vanishes=(
            result.derived_hh_vanishing_established
        ),
        corrected_tcft_identity_available=(
            result.corrected_tcft_identity_established
        ),
        space_contractible_established=False,
        strict_witness_coefficient=witness.coefficient_on_b,
        what_proofs_actually_show=(
            "The corrected statement is conditional: raw B_term^(2) fails; "
            "B_TCFT^(2) needs Costello correction data; HH^{-2} vanishing "
            "needs the comparison/filtration theorem."
        ),
        what_cya3_actually_needs=(
            "CY-A_3 still needs compact Phi_3/Hall/CoHA/PBW data, the "
            "chain-level comparison map, and non-perturbative convergence."
        ),
        gap=(
            "A killed primary class is not an explicit chain-level "
            "construction and does not prove contractibility of the space "
            "of E_3 structures."
        ),
        required_hypotheses=result.required_hypotheses,
    )


def attack_cohomological_vs_chain() -> AttackVector:
    """Attack automatic existence and contractibility claims."""

    check = check_cohomological_vs_chain()
    return AttackVector(
        name="Conditional vanishing is not E_3 contractibility",
        target_proof="all",
        target_step="space of E_3 structures is contractible",
        description=(
            "The corrected engines do not prove automatic existence or "
            "contractibility.  They record a conditional primary obstruction "
            "statement and an explicit strict raw counterexample."
        ),
        severity="fatal",
        survives=False,
        mitigation=(
            "State only the conditional primary obstruction result.  Keep "
            "explicit construction and contractibility as open obligations."
        ),
        residual_gap=check.gap,
        proof_obligations=check.required_hypotheses,
    )


# =========================================================================
# 7. MASTER STRESS TEST
# =========================================================================


def run_stress_test() -> StressTestResult:
    r"""Execute all adversarial attacks and synthesize."""

    attacks = [
        attack_dunn_additivity(),
        attack_unit_connectedness(),
        attack_aq_cotangent(),
        attack_tcft_b_identification(),
        attack_cohomological_vs_chain(),
    ]
    genuine = [a for a in attacks if a.severity in ("moderate", "fatal")]
    fatal = [a for a in attacks if a.severity == "fatal"]
    all_survive = all(a.survives for a in attacks)

    obligations: List[str] = []
    for attack in attacks:
        for obligation in attack.proof_obligations:
            if obligation not in obligations:
                obligations.append(obligation)

    synthesis = (
        "The stale automatic proof stack fails.  Dunn additivity holds in "
        "Ch(k), but it does not prove HH^{-2}=0, E_3-chiral descent, or "
        "contractibility.  Unit-connectedness is not a substitute for the "
        "comparison/filtration theorem.  Costello's carrier is corrected "
        "B_TCFT^(2), not raw B_term^(2).  The strict witness gives "
        "[m_3,B_term^(2)][a|a|a|a|b]=2 alpha [b] != 0."
    )
    recommendation = (
        "Use the stress test as a proof-obligation ledger: supply the "
        "Costello correction datum, the S^3 obstruction comparison map, "
        "and the complete/exhaustive/separated/strongly convergent "
        "filtration with empty total-degree -2 line before asserting "
        "derived vanishing.  Do not assert contractibility."
    )

    return StressTestResult(
        attacks=attacks,
        proofs_survive=all_survive,
        genuine_weaknesses=genuine,
        fatal_weaknesses=fatal,
        synthesis=synthesis,
        recommendation=recommendation,
        proof_obligations=obligations,
    )


# =========================================================================
# 8. SPECIFIC COMPUTATIONS FOR THE STRESS TEST
# =========================================================================


def compute_hh0_landscape() -> Dict[str, Dict[str, Any]]:
    r"""Record categorical ``HH^0`` data without deriving ``HH^{-2}``."""

    return {
        "C^3": {
            "cat_hh0_dim": 1,
            "hkr_decomposition": "H^0(O)=k",
            "unit_connected": True,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "toric control; still needs filtration theorem",
        },
        "Conifold": {
            "cat_hh0_dim": 1,
            "hkr_decomposition": "H^0(O)=k",
            "unit_connected": True,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "direct McKay/toric control; not compact CY_3 closure",
        },
        "Local P^2": {
            "cat_hh0_dim": 1,
            "hkr_decomposition": "H^0(O)=k",
            "unit_connected": True,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "noncompact strict witness surface",
        },
        "Quintic": {
            "cat_hh0_dim": 1,
            "hkr_decomposition": "H^0(O_Q)=k",
            "unit_connected": True,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "compact CY_3; Phi_3 not constructed by HH^0",
        },
        "K3 x E": {
            "cat_hh0_dim": 2,
            "hkr_decomposition": "HH^0(K3) tensor HH^0(E)=k^2 tensor k",
            "unit_connected": False,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "product diagnostic; not generic unit-connectedness",
        },
        "Local P^1 x P^1": {
            "cat_hh0_dim": 1,
            "hkr_decomposition": "H^0(O)=k",
            "unit_connected": True,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "noncompact toric control",
        },
        "Fermat quintic (CY3)": {
            "cat_hh0_dim": 1,
            "hkr_decomposition": "H^0(O)=k",
            "unit_connected": True,
            "hh_minus_two_vanishing_established": False,
            "mechanism": "compact CY_3; filtration/comparison still open",
        },
    }


def compute_obstruction_by_mechanism(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> Dict[str, Dict[str, Any]]:
    r"""Return conditional obstruction statuses by example."""

    examples: List[Tuple[str, bool, bool, str]] = [
        ("C^3", True, False, "G"),
        ("Conifold", True, False, "G"),
        ("Local P^2", False, True, "M"),
        ("Quintic", True, False, "G"),
        ("K3 x E", True, False, "G"),
        ("Local P^1 x P^1", True, False, "G"),
    ]
    out: Dict[str, Dict[str, Any]] = {}
    for name, is_formal, has_m3, shadow in examples:
        result = compute_derived_framing_obstruction(
            algebra_name=name,
            cy_dim=3,
            shadow_class=shadow,
            is_formal=is_formal,
            has_nonzero_m3=has_m3,
            tcft_hypotheses=tcft_hypotheses,
            hh_hypotheses=hh_hypotheses,
        )
        out[name] = {
            "mechanism": (
                "requires Costello correction plus HH^{-2} filtration theorem"
            ),
            "generic_argument": name != "K3 x E",
            "product_decomposition": name == "K3 x E",
            "obstruction_vanishes": result.obstruction_vanishes,
            "strict_commutator_vanishes": result.strict_commutator_vanishes,
            "raw_witness_nonzero": (
                result.raw_termwise_witness is not None
                and result.raw_termwise_witness.nonzero
            ),
            "status": (
                "conditional_obstruction_vanishes"
                if result.obstruction_vanishes
                else "open_requires_named_hypotheses"
            ),
            "required_hypotheses": result.required_hypotheses,
        }
    return out


def verify_k3xe_product_decomposition(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> Dict[str, Any]:
    r"""Record what the K3 x E product argument does and does not prove."""

    result = compute_derived_framing_obstruction(
        algebra_name="K3 x E",
        cy_dim=3,
        shadow_class="G",
        is_formal=True,
        has_nonzero_m3=False,
        tcft_hypotheses=tcft_hypotheses,
        hh_hypotheses=hh_hypotheses,
    )
    return {
        "k3_factor": {
            "cy_dim": 2,
            "framing": "S^2",
            "e_n_level": 2,
            "proved": True,
            "reference": "CY-A_2",
        },
        "e_factor": {
            "cy_dim": 1,
            "framing": "S^1",
            "e_n_level": 1,
            "proved": True,
            "reference": "classical Connes carrier",
        },
        "product": {
            "cy_dim": 3,
            "framing": "S^2 x S^1 diagnostic, not automatic S^3 closure",
            "e_n_level": "E_2 x E_1 diagnostic",
            "obstruction_vanishes": result.obstruction_vanishes,
            "status": (
                "conditional_obstruction_vanishes"
                if result.obstruction_vanishes
                else "open_requires_named_hypotheses"
            ),
        },
        "hopf_twist_absent": True,
        "unit_connectedness_needed": False,
        "proof_obligations": result.required_hypotheses,
    }


def count_generic_vs_special() -> Dict[str, int]:
    r"""Count generic/special diagnostic lanes, not theorem proofs."""

    by_mechanism = compute_obstruction_by_mechanism()
    generic = sum(1 for v in by_mechanism.values() if v["generic_argument"])
    special = sum(1 for v in by_mechanism.values() if not v["generic_argument"])
    return {"generic": generic, "special": special, "total": generic + special}


# =========================================================================
# 9. MANUSCRIPT / ENGINE RECOMMENDATIONS
# =========================================================================


@dataclass
class ManuscriptRecommendation:
    r"""Recommended repair to a stale proof step or engine assertion."""

    theorem_label: str
    current_claim: str
    issue: str
    recommended_edit: str
    severity: str


def generate_recommendations() -> List[ManuscriptRecommendation]:
    """Generate recommendations from the corrected stress test."""

    return [
        ManuscriptRecommendation(
            theorem_label="thm:derived-framing-obstruction",
            current_claim=(
                "HH^{-2}_{E_1}(A,A)=0 follows from Dunn additivity and "
                "unit-connectedness."
            ),
            issue=(
                "Dunn additivity supplies the ambient operadic comparison; "
                "it does not prove the negative Hochschild line is empty."
            ),
            recommended_edit=(
                "Require the comparison map and the complete, exhaustive, "
                "separated, strongly convergent filtration with empty total "
                "degree -2 line."
            ),
            severity="fatal",
        ),
        ManuscriptRecommendation(
            theorem_label="prop:cyclic-ainf-framing-compat",
            current_claim="{b,B^(2)}=0 by Costello's TCFT.",
            issue=(
                "Raw B_term^(2) is not Costello's corrected B_TCFT^(2); "
                "the strict witness gives 2 alpha [b]."
            ),
            recommended_edit=(
                "State the corrected total TCFT identity only after the "
                "Costello correction datum is part of the hypotheses."
            ),
            severity="fatal",
        ),
        ManuscriptRecommendation(
            theorem_label="prop:aq-e3-lifting-verification",
            current_claim="The space of E_3 structures is contractible.",
            issue=(
                "The corrected obstruction engines certify no such automatic "
                "contractibility statement."
            ),
            recommended_edit=(
                "Downgrade to a conditional primary-obstruction statement "
                "and keep contractibility as a separate proof obligation."
            ),
            severity="fatal",
        ),
    ]


# =========================================================================
# 10. CONVENIENCE ALIASES
# =========================================================================


def complete_conditional_obstruction_status() -> Dict[str, Dict[str, Any]]:
    """Return statuses after all named TCFT and HH hypotheses are supplied."""

    return compute_obstruction_by_mechanism(
        tcft_hypotheses=complete_tcft_correction_datum(),
        hh_hypotheses=complete_hh_minus_two_hypotheses(),
    )


def master_stress_test() -> StressTestResult:
    """Master entry point for the adversarial stress test."""

    return run_stress_test()
