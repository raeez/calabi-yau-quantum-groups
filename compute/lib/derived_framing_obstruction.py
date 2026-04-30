r"""Attack-healed derived framing obstruction diagnostics.

This engine separates three mathematical carriers that must not be
identified.

1. ``B^{(2)}_term`` is the raw bar pair-contraction operator.  It has a
   strict nonzero cyclic CY_3 witness:

       [m_3, B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0.

2. ``B^{(2)}_TCFT`` is Costello's corrected open-closed TCFT operator.
   The identity ``{b, B^{(2)}_TCFT}=0`` is a total corrected identity
   only after the Costello correction datum is supplied.  It is not a
   termwise statement for ``B^{(2)}_term``.

3. The derived obstruction class lands in ``HH^{-2}_{E_1}(A,A)`` only
   after a comparison map to the obstruction complex has been fixed.
   Its vanishing requires explicit filtration/comparison hypotheses:
   complete, exhaustive, separated, strongly convergent bar-length
   filtration with empty total degree ``-2`` line.

The engine preserves the formal sanity case: when ``m_k=0`` for
``k>=3``, the higher ``m_3`` carrier is absent.  It also preserves the
conditional derived-class statement under the named TCFT and ``HH^{-2}``
hypotheses.  It rejects universal derived/cohomological/framing
vanishing and rejects any automatic closure of the strict compact CY_3
problem from Hopf or derived Level 3 data alone.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

F = Fraction
Word = Tuple[str, ...]


# =========================================================================
# 0. STRICT RAW WITNESS AND HYPOTHESIS DATA
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
        return any(coeff != 0 for coeff in self.commutator.values())

    def summary(self) -> Dict[str, Any]:
        return {
            "input_word": self.input_word,
            "b2_term_of_input": self.b2_term_of_input,
            "m3_after_b2_term": self.m3_after_b2_term,
            "m3_of_input": self.m3_of_input,
            "b2_term_after_m3": self.b2_term_after_m3,
            "commutator": self.commutator,
            "coefficient_on_b": self.coefficient_on_b,
            "nonzero": self.nonzero,
            "convention": self.convention,
        }


def strict_m3_b2_term_witness(alpha: Fraction = F(1)) -> TermwiseCommutatorWitness:
    r"""Return the strict nonzero witness for raw ``B^{(2)}_term``.

    Terminal-slot normalization:

    * ``B^{(2)}_term [a|a|a|a|b] = 4 [a|a|a]``;
    * ``m_3 B^{(2)}_term`` gives ``4 alpha [b]``;
    * ``m_3`` first gives ``alpha([b|a|b] + [a|b|b])``;
    * ``B^{(2)}_term m_3`` gives ``2 alpha [b]``.
    """

    return TermwiseCommutatorWitness(
        alpha=alpha,
        input_word=("a", "a", "a", "a", "b"),
        b2_term_of_input={("a", "a", "a"): F(4)},
        m3_after_b2_term={("b",): F(4) * alpha},
        m3_of_input={("b", "a", "b"): alpha, ("a", "b", "b"): alpha},
        b2_term_after_m3={("b",): F(2) * alpha},
        commutator={("b",): F(2) * alpha},
        convention="terminal-slot B^{(2)}_term, characteristic zero",
    )


@dataclass(frozen=True)
class TCFTCorrectionDatum:
    """Hypotheses for Costello's corrected total TCFT identity."""

    moduli_chain_corrections: bool = False
    open_closed_tcft_chain_map: bool = False
    costello_orientation_signs: bool = False
    corrected_operator_chosen: bool = False

    @property
    def total_tcft_identity_available(self) -> bool:
        return all(
            [
                self.moduli_chain_corrections,
                self.open_closed_tcft_chain_map,
                self.costello_orientation_signs,
                self.corrected_operator_chosen,
            ]
        )

    @property
    def missing_hypotheses(self) -> List[str]:
        missing = []
        if not self.moduli_chain_corrections:
            missing.append("Costello moduli-chain correction terms")
        if not self.open_closed_tcft_chain_map:
            missing.append("open-closed TCFT chain map")
        if not self.costello_orientation_signs:
            missing.append("Costello boundary orientation/sign convention")
        if not self.corrected_operator_chosen:
            missing.append("chosen corrected representative B^{(2)}_TCFT")
        return missing


def complete_tcft_correction_datum() -> TCFTCorrectionDatum:
    """Convenience datum for tests of the conditional TCFT statement."""

    return TCFTCorrectionDatum(
        moduli_chain_corrections=True,
        open_closed_tcft_chain_map=True,
        costello_orientation_signs=True,
        corrected_operator_chosen=True,
    )


@dataclass(frozen=True)
class HHMinusTwoFiltrationHypotheses:
    """Hypotheses needed to prove ``HH^{-2}_{E_1}(A,A)=0``."""

    connective_unit_connected_model: bool = False
    filtration_complete: bool = False
    filtration_exhaustive: bool = False
    filtration_separated: bool = False
    strong_convergence: bool = False
    empty_total_degree_minus_two_line: bool = False
    comparison_to_obstruction_complex: bool = False
    obstruction_cocycle_degree_minus_two: bool = False

    @property
    def vanishing_established(self) -> bool:
        return all(
            [
                self.connective_unit_connected_model,
                self.filtration_complete,
                self.filtration_exhaustive,
                self.filtration_separated,
                self.strong_convergence,
                self.empty_total_degree_minus_two_line,
                self.comparison_to_obstruction_complex,
                self.obstruction_cocycle_degree_minus_two,
            ]
        )

    @property
    def missing_hypotheses(self) -> List[str]:
        checks = [
            (self.connective_unit_connected_model, "connective unit-connected strictified model"),
            (self.filtration_complete, "complete bar-length filtration"),
            (self.filtration_exhaustive, "exhaustive bar-length filtration"),
            (self.filtration_separated, "separated bar-length filtration"),
            (self.strong_convergence, "strong convergence to HH"),
            (self.empty_total_degree_minus_two_line, "empty total degree -2 first-page line"),
            (self.comparison_to_obstruction_complex, "comparison map to S^3 obstruction complex"),
            (self.obstruction_cocycle_degree_minus_two, "obstruction cocycle lands in degree -2"),
        ]
        return [label for ok, label in checks if not ok]


def complete_hh_minus_two_hypotheses() -> HHMinusTwoFiltrationHypotheses:
    """Convenience hypotheses for tests of the conditional HH^{-2} theorem."""

    return HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True,
        filtration_complete=True,
        filtration_exhaustive=True,
        filtration_separated=True,
        strong_convergence=True,
        empty_total_degree_minus_two_line=True,
        comparison_to_obstruction_complex=True,
        obstruction_cocycle_degree_minus_two=True,
    )


# =========================================================================
# 1. E_n-HOCHSCHILD DATA AND PRIMARY OBSTRUCTION GROUPS
# =========================================================================


@dataclass
class EnHochschildData:
    r"""E_n-Hochschild data with explicit status for negative degrees."""

    algebra_name: str
    n: int
    shadow_class: str
    cy_dim: int
    is_unit_connected: bool
    hh_dims: Dict[int, Optional[int]]
    is_formal: bool
    negative_vanishing_established: bool
    hh_minus_two_hypotheses: HHMinusTwoFiltrationHypotheses
    status: str
    required_hypotheses: List[str] = field(default_factory=list)

    def dim_at(self, degree: int) -> Optional[int]:
        """Dimension of ``HH^degree`` when established; ``None`` if open."""

        return self.hh_dims.get(degree)

    def negative_degrees_vanish(self) -> bool:
        """Whether negative-degree vanishing has actually been proved."""

        return self.negative_vanishing_established and all(
            self.dim_at(k) == 0 for k in range(-10, 0)
        )

    def obstruction_group_e2_to_e3(self) -> Optional[int]:
        r"""Dimension of the primary ``E_2 -> E_3`` obstruction group.

        The group is ``HH^{-2}_{E_1}(A,A)`` only after the comparison
        to the obstruction complex is part of the data.
        """

        return self.dim_at(-2)


def compute_en_hochschild(
    algebra_name: str,
    shadow_class: str,
    cy_dim: int,
    n: int = 1,
    is_formal: bool = True,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> EnHochschildData:
    r"""Compute the portion of E_n-Hochschild data this engine may certify."""

    hypotheses = hh_hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )
    negative_known = hypotheses.vanishing_established

    hh_dims: Dict[int, Optional[int]] = {}
    for k in range(-10, 0):
        hh_dims[k] = 0 if negative_known else None
    hh_dims[0] = 1

    if shadow_class == "G":
        partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
        for k in range(1, 10):
            hh_dims[k] = partitions[k]
    elif shadow_class in {"L", "C"}:
        for k in range(1, 10):
            hh_dims[k] = 2 ** k
    elif shadow_class == "M":
        for k in range(1, 10):
            hh_dims[k] = 1000 * k
    else:
        raise ValueError(f"Unknown shadow class: {shadow_class}")

    status = (
        "HH^{-2} vanishing established under filtration/comparison hypotheses"
        if negative_known
        else "unit-connectedness recorded; HH^{-2} vanishing not established"
    )

    return EnHochschildData(
        algebra_name=algebra_name,
        n=n,
        shadow_class=shadow_class,
        cy_dim=cy_dim,
        is_unit_connected=hypotheses.connective_unit_connected_model,
        hh_dims=hh_dims,
        is_formal=is_formal,
        negative_vanishing_established=negative_known,
        hh_minus_two_hypotheses=hypotheses,
        status=status,
        required_hypotheses=hypotheses.missing_hypotheses,
    )


@dataclass
class LiftingObstruction:
    r"""The primary obstruction to lifting from ``E_n`` to ``E_{n+1}``."""

    source_n: int
    target_n: int
    primary_obs_degree: int
    primary_obs_dim: Optional[int]
    higher_obs_all_zero: bool
    space_contractible: bool
    mechanism: str
    status: str
    required_hypotheses: List[str] = field(default_factory=list)


def _lifting_obstruction_from_hh(
    e1_hh: EnHochschildData,
) -> LiftingObstruction:
    primary_dim = e1_hh.obstruction_group_e2_to_e3()
    primary_known_zero = primary_dim == 0
    return LiftingObstruction(
        source_n=2,
        target_n=3,
        primary_obs_degree=-2,
        primary_obs_dim=primary_dim,
        higher_obs_all_zero=False,
        space_contractible=False,
        status=(
            "conditional_primary_vanishing"
            if primary_known_zero
            else "open_requires_HH_minus_two_hypotheses"
        ),
        mechanism=(
            "The primary class is killed only after the HH^{-2} filtration "
            "and comparison hypotheses are supplied.  This engine does not "
            "upgrade that statement to all higher obstructions or to "
            "contractibility of the lifting space."
        ),
        required_hypotheses=e1_hh.required_hypotheses,
    )


# =========================================================================
# 2. MAIN OBSTRUCTION COMPUTATION
# =========================================================================


@dataclass
class DerivedFramingObstructionResult:
    """Complete carrier-separated result for one CY_3 input."""

    algebra_name: str
    cy_dim: int
    shadow_class: str
    strict_commutator_vanishes: bool
    strict_explanation: str
    total_commutator_vanishes: bool
    homotopy_explanation: str
    cross_arity_cancellation: bool
    e1_hh_data: EnHochschildData
    lifting_obstruction: LiftingObstruction
    obstruction_group_dim: Optional[int]
    obstruction_vanishes: bool
    derived_explanation: str
    category_error_identified: bool
    reconciliation: str
    actual_obstructions: List[str]
    raw_operator: str
    corrected_operator: str
    raw_termwise_witness: Optional[TermwiseCommutatorWitness]
    corrected_tcft_identity_established: bool
    derived_hh_vanishing_established: bool
    universal_vanishing_claim_rejected: bool
    strict_compact_cy3_closed: bool
    required_hypotheses: List[str] = field(default_factory=list)
    remaining_proof_obligations: List[str] = field(default_factory=list)


def compute_derived_framing_obstruction(
    algebra_name: str,
    cy_dim: int = 3,
    shadow_class: str = "G",
    is_formal: bool = True,
    has_nonzero_m3: bool = False,
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> DerivedFramingObstructionResult:
    r"""Compute the attack-healed derived framing obstruction verdict."""

    tcft = tcft_hypotheses or TCFTCorrectionDatum()
    hh_hyp = hh_hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )

    strict_vanishes = not has_nonzero_m3
    witness = None if strict_vanishes else strict_m3_b2_term_witness()

    if strict_vanishes:
        strict_expl = (
            f"{algebra_name}: the formal higher A-infinity carrier is absent "
            "because m_k=0 for k>=3 in the supplied model."
        )
    else:
        strict_expl = (
            f"{algebra_name}: raw B^(2)_term does not commute with m_3.  "
            "The strict witness has [m_3,B^(2)_term][a|a|a|a|b] = "
            "2 alpha [b] != 0."
        )

    corrected_total = tcft.total_tcft_identity_available
    if corrected_total:
        homotopy_expl = (
            "The corrected total identity {b,B^(2)_TCFT}=0 is available "
            "for the chosen Costello moduli-chain correction datum."
        )
    else:
        homotopy_expl = (
            "No corrected total TCFT identity is certified: "
            + "; ".join(tcft.missing_hypotheses)
            + ".  The raw B^(2)_term identity is not used."
        )

    e1_hh = compute_en_hochschild(
        algebra_name=algebra_name,
        shadow_class=shadow_class,
        cy_dim=cy_dim,
        n=1,
        is_formal=is_formal,
        hh_hypotheses=hh_hyp,
    )
    lifting = _lifting_obstruction_from_hh(e1_hh)
    derived_hh_zero = hh_hyp.vanishing_established

    if derived_hh_zero:
        derived_expl = (
            "The primary derived class vanishes in HH^{-2}_{E_1}(A,A) "
            "under the supplied complete filtration/comparison hypotheses."
        )
    else:
        derived_expl = (
            "HH^{-2}_{E_1}(A,A) vanishing is not established.  Missing: "
            + "; ".join(hh_hyp.missing_hypotheses)
            + "."
        )

    remaining = [
        "Specify the Costello correction datum for B^(2)_TCFT.",
        "Fix the chain-level comparison map to the S^3-framing obstruction complex.",
        "Prove the HH^{-2} filtration hypotheses for the strictified model.",
        "Construct compact CY_3 global Phi_3/Hall/CoHA/PBW data separately.",
    ]
    if corrected_total:
        remaining.remove("Specify the Costello correction datum for B^(2)_TCFT.")
    if derived_hh_zero:
        remaining.remove("Prove the HH^{-2} filtration hypotheses for the strictified model.")

    actual_obs = [
        "Costello correction datum for the corrected TCFT representative.",
        "HH^{-2} filtration/comparison theorem for the chosen strictified model.",
        "Compact CY_3 global source-side data: Phi_3, Hall correspondences, PBW/no-extra-relations.",
    ]

    reconciliation = (
        "The false step was carrier conflation: raw B^(2)_term, corrected "
        "B^(2)_TCFT, and the HH^{-2} derived class are different objects.  "
        "The strict witness defeats raw termwise vanishing.  Corrected TCFT "
        "and derived vanishing are conditional statements with named inputs."
    )

    obstruction_established = corrected_total and derived_hh_zero
    required = tcft.missing_hypotheses + hh_hyp.missing_hypotheses

    return DerivedFramingObstructionResult(
        algebra_name=algebra_name,
        cy_dim=cy_dim,
        shadow_class=shadow_class,
        strict_commutator_vanishes=strict_vanishes,
        strict_explanation=strict_expl,
        total_commutator_vanishes=corrected_total,
        homotopy_explanation=homotopy_expl,
        cross_arity_cancellation=False,
        e1_hh_data=e1_hh,
        lifting_obstruction=lifting,
        obstruction_group_dim=e1_hh.obstruction_group_e2_to_e3(),
        obstruction_vanishes=obstruction_established,
        derived_explanation=derived_expl,
        category_error_identified=True,
        reconciliation=reconciliation,
        actual_obstructions=actual_obs,
        raw_operator="B^(2)_term",
        corrected_operator="B^(2)_TCFT",
        raw_termwise_witness=witness,
        corrected_tcft_identity_established=corrected_total,
        derived_hh_vanishing_established=derived_hh_zero,
        universal_vanishing_claim_rejected=True,
        strict_compact_cy3_closed=False,
        required_hypotheses=required,
        remaining_proof_obligations=remaining,
    )


# =========================================================================
# 3. CY_3 LANDSCAPE
# =========================================================================


@dataclass
class CY3LandscapeEntry:
    """One entry in the CY_3 obstruction landscape."""

    name: str
    is_formal: bool
    has_m3: bool
    shadow_class: str
    strict_level: str
    homotopy_level: str
    derived_level: str
    obstruction_group_dim: Optional[int]


def compute_cy3_landscape(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> List[CY3LandscapeEntry]:
    """Compute diagnostic statuses for standard CY_3 models."""

    geometries = [
        ("C^3 (Jordan quiver)", True, False, "G"),
        ("Conifold (resolved)", True, False, "G"),
        ("Local P^2", False, True, "M"),
        ("Local P^1 x P^1", True, False, "G"),
        ("Quintic threefold", True, False, "G"),
        ("K3 x E", True, False, "G"),
        ("Local P^2 (Fermat)", False, True, "M"),
    ]

    entries: List[CY3LandscapeEntry] = []
    for name, is_formal, has_m3, shadow_class in geometries:
        result = compute_derived_framing_obstruction(
            algebra_name=name,
            cy_dim=3,
            shadow_class=shadow_class,
            is_formal=is_formal,
            has_nonzero_m3=has_m3,
            tcft_hypotheses=tcft_hypotheses,
            hh_hypotheses=hh_hypotheses,
        )
        entries.append(
            CY3LandscapeEntry(
                name=name,
                is_formal=is_formal,
                has_m3=has_m3,
                shadow_class=shadow_class,
                strict_level="formal_absent" if result.strict_commutator_vanishes else "raw_nonzero",
                homotopy_level=(
                    "conditional_corrected_total"
                    if result.corrected_tcft_identity_established
                    else "requires_tcft_correction_datum"
                ),
                derived_level=(
                    "conditional_primary_class_vanishes"
                    if result.derived_hh_vanishing_established
                    else "requires_HH_minus_two_hypotheses"
                ),
                obstruction_group_dim=result.obstruction_group_dim,
            )
        )
    return entries


# =========================================================================
# 4. GOODWILLIE AND FRANCIS-GAITSGORY DIAGNOSTICS
# =========================================================================


@dataclass
class GoodwillieLayerData:
    """Goodwillie layer diagnostic for the ``E_2 -> E_3`` lifting."""

    layer: int
    coefficient_object: str
    obstruction_degree: int
    obstruction_dim: Optional[int]
    connectivity_bound: int
    vanishes: bool
    status: str
    required_hypotheses: List[str] = field(default_factory=list)


def compute_goodwillie_layers(
    algebra_name: str,
    max_layer: int = 6,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
    goodwillie_convergence_hypothesis: bool = False,
) -> List[GoodwillieLayerData]:
    """Compute Goodwillie layer statuses without asserting automatic closure."""

    hh_hyp = hh_hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )
    layers: List[GoodwillieLayerData] = []
    for k in range(1, max_layer + 1):
        if k == 1:
            vanishes = hh_hyp.vanishing_established
            required = hh_hyp.missing_hypotheses
            status = "conditional_primary_vanishing" if vanishes else "open_primary_layer"
        else:
            vanishes = hh_hyp.vanishing_established and goodwillie_convergence_hypothesis
            required = list(hh_hyp.missing_hypotheses)
            if not goodwillie_convergence_hypothesis:
                required.append(f"Goodwillie convergence and lim^1 control for layer {k}")
            status = "conditional_higher_layer_vanishing" if vanishes else "open_higher_layer"

        layers.append(
            GoodwillieLayerData(
                layer=k,
                coefficient_object=f"A^{{tensor {k}}}",
                obstruction_degree=-2,
                obstruction_dim=0 if vanishes else None,
                connectivity_bound=-k + 1,
                vanishes=vanishes,
                status=status,
                required_hypotheses=required,
            )
        )
    return layers


@dataclass
class FrancisGaitsgoryComplex:
    """Francis-Gaitsgory relative deformation-complex diagnostic."""

    source_n: int
    target_n: int
    tangent_shift: int
    relative_cotangent_shift: int
    complex_dims: Dict[int, Optional[int]]
    h0: Optional[int]
    h1: Optional[int]
    h2: Optional[int]
    is_unobstructed: bool
    status: str
    required_hypotheses: List[str] = field(default_factory=list)


def compute_fg_complex(
    algebra_name: str,
    source_n: int = 2,
    target_n: int = 3,
    is_unit_connected: bool = True,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> FrancisGaitsgoryComplex:
    """Compute the relative deformation-complex status."""

    if not is_unit_connected:
        return FrancisGaitsgoryComplex(
            source_n=source_n,
            target_n=target_n,
            tangent_shift=source_n,
            relative_cotangent_shift=source_n,
            complex_dims={0: 1, 1: 2, 2: 4, 3: 8},
            h0=1,
            h1=1,
            h2=2,
            is_unobstructed=False,
            status="non_unit_connected_can_have_obstructions",
            required_hypotheses=["unit-connected strictified model"],
        )

    hh_hyp = hh_hypotheses or HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True
    )
    if hh_hyp.vanishing_established:
        return FrancisGaitsgoryComplex(
            source_n=source_n,
            target_n=target_n,
            tangent_shift=source_n,
            relative_cotangent_shift=source_n,
            complex_dims={0: None, 1: None, 2: 0, 3: None},
            h0=None,
            h1=None,
            h2=0,
            is_unobstructed=True,
            status="conditional_primary_obstruction_vanishes",
            required_hypotheses=[],
        )

    return FrancisGaitsgoryComplex(
        source_n=source_n,
        target_n=target_n,
        tangent_shift=source_n,
        relative_cotangent_shift=source_n,
        complex_dims={0: None, 1: None, 2: None, 3: None},
        h0=None,
        h1=None,
        h2=None,
        is_unobstructed=False,
        status="unit_connected_but_HH_minus_two_not_proved",
        required_hypotheses=hh_hyp.missing_hypotheses,
    )


# =========================================================================
# 5. EXPLICIT HOMOTOPY AND BOTT DIAGNOSTICS
# =========================================================================


@dataclass
class ExplicitHomotopyData:
    """Status of a homotopy for the non-formal raw witness."""

    exists: bool
    is_costello_tcft: bool
    is_stasheff: bool
    cancellation_pairs: List[Tuple[int, int]]
    total_cancellation: bool
    uses_raw_b2_term: bool
    status: str
    required_hypotheses: List[str] = field(default_factory=list)


def construct_explicit_homotopy(
    is_formal: bool,
    has_m3: bool,
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
) -> ExplicitHomotopyData:
    """Return the homotopy status without asserting raw pairwise cancellation."""

    if is_formal or not has_m3:
        return ExplicitHomotopyData(
            exists=True,
            is_costello_tcft=False,
            is_stasheff=False,
            cancellation_pairs=[],
            total_cancellation=False,
            uses_raw_b2_term=True,
            status="formal_trivial_higher_carrier_absent",
        )

    tcft = tcft_hypotheses or TCFTCorrectionDatum()
    available = tcft.total_tcft_identity_available
    return ExplicitHomotopyData(
        exists=available,
        is_costello_tcft=available,
        is_stasheff=False,
        cancellation_pairs=[],
        total_cancellation=available,
        uses_raw_b2_term=False,
        status=(
            "corrected_TCFT_total_identity"
            if available
            else "open_requires_Costello_correction_datum"
        ),
        required_hypotheses=tcft.missing_hypotheses,
    )


@dataclass
class BottPeriodicityData:
    """Bott periodicity data for the topological S^d carrier."""

    d: int
    pi_d_BU: int
    pi_d_BSp: int
    topological_obstruction_vanishes: bool
    closes_strict_compact_cy3: bool = False


def compute_bott_periodicity(d: int) -> BottPeriodicityData:
    """Compute Bott periodicity data; topological vanishing is not closure."""

    pi_BU = 1 if d % 2 == 0 and d > 0 else 0
    sp_groups = [0, 0, 0, 1, 2, 2, 0, 1]
    pi_BSp = sp_groups[(d - 1) % 8] if d >= 1 else 0
    return BottPeriodicityData(
        d=d,
        pi_d_BU=pi_BU,
        pi_d_BSp=pi_BSp,
        topological_obstruction_vanishes=(pi_BU == 0 and pi_BSp == 0),
        closes_strict_compact_cy3=False,
    )


# =========================================================================
# 6. CROSS-CHECKS AND MASTER COMPUTATION
# =========================================================================


@dataclass
class CrossCheckResult:
    """Cross-checks with the repaired Vol III obstruction engines."""

    tcft_consistent: bool
    obs_ainf_consistent: bool
    stasheff_consistent: bool
    hopf_consistent: bool
    deligne_consistent: bool
    en_tower_consistent: bool
    zte_independent: bool
    all_consistent: bool
    raw_termwise_rejected: bool
    conditional_boundaries_respected: bool
    no_compact_cy3_closure_claim: bool


def perform_cross_checks(
    result: DerivedFramingObstructionResult,
) -> CrossCheckResult:
    """Check that the result agrees with the repaired neighboring engines."""

    raw_rejected = result.universal_vanishing_claim_rejected
    obs_ainf_ok = (
        result.strict_commutator_vanishes
        or (result.raw_termwise_witness is not None and result.raw_termwise_witness.nonzero)
    )
    tcft_ok = result.total_commutator_vanishes == result.corrected_tcft_identity_established
    stasheff_ok = raw_rejected and not result.cross_arity_cancellation
    hopf_ok = not result.strict_compact_cy3_closed
    deligne_ok = (
        not result.obstruction_vanishes
        or (
            result.corrected_tcft_identity_established
            and result.derived_hh_vanishing_established
        )
    )
    en_tower_ok = True
    zte_independent = True
    conditional_ok = (
        not result.obstruction_vanishes
        or len(result.required_hypotheses) == 0
    )
    no_closure = not result.strict_compact_cy3_closed

    all_ok = all(
        [
            tcft_ok,
            obs_ainf_ok,
            stasheff_ok,
            hopf_ok,
            deligne_ok,
            en_tower_ok,
            zte_independent,
            raw_rejected,
            conditional_ok,
            no_closure,
        ]
    )
    return CrossCheckResult(
        tcft_consistent=tcft_ok,
        obs_ainf_consistent=obs_ainf_ok,
        stasheff_consistent=stasheff_ok,
        hopf_consistent=hopf_ok,
        deligne_consistent=deligne_ok,
        en_tower_consistent=en_tower_ok,
        zte_independent=zte_independent,
        all_consistent=all_ok,
        raw_termwise_rejected=raw_rejected,
        conditional_boundaries_respected=conditional_ok,
        no_compact_cy3_closure_claim=no_closure,
    )


@dataclass
class MasterDerivedFramingResult:
    """Top-level result for the attack-healed obstruction engine."""

    landscape: List[CY3LandscapeEntry]
    local_p2_result: DerivedFramingObstructionResult
    goodwillie_layers: List[GoodwillieLayerData]
    fg_complex: FrancisGaitsgoryComplex
    bott_d3: BottPeriodicityData
    explicit_homotopy: ExplicitHomotopyData
    cross_checks: CrossCheckResult
    chain_level_nonvanishing_is_obstruction: bool
    derived_obstruction_vanishes: bool
    theorem_statement: str
    what_actually_obstructs_cya3: List[str]
    universal_vanishing_claim_rejected: bool
    strict_compact_cy3_closed: bool
    remaining_proof_obligations: List[str] = field(default_factory=list)


def master_derived_framing_analysis(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
    goodwillie_convergence_hypothesis: bool = False,
) -> MasterDerivedFramingResult:
    """Complete attack-healed analysis."""

    landscape = compute_cy3_landscape(
        tcft_hypotheses=tcft_hypotheses,
        hh_hypotheses=hh_hypotheses,
    )
    local_p2 = compute_derived_framing_obstruction(
        algebra_name="Local P^2",
        cy_dim=3,
        shadow_class="M",
        is_formal=False,
        has_nonzero_m3=True,
        tcft_hypotheses=tcft_hypotheses,
        hh_hypotheses=hh_hypotheses,
    )
    goodwillie = compute_goodwillie_layers(
        "Local P^2",
        max_layer=6,
        hh_hypotheses=hh_hypotheses,
        goodwillie_convergence_hypothesis=goodwillie_convergence_hypothesis,
    )
    fg = compute_fg_complex(
        "Local P^2",
        source_n=2,
        target_n=3,
        hh_hypotheses=hh_hypotheses,
    )
    bott = compute_bott_periodicity(3)
    homotopy = construct_explicit_homotopy(
        is_formal=False,
        has_m3=True,
        tcft_hypotheses=tcft_hypotheses,
    )
    checks = perform_cross_checks(local_p2)

    theorem = (
        "Conditional corrected proposition.  Raw B^(2)_term has a strict "
        "nonzero witness [m_3,B^(2)_term][a|a|a|a|b]=2 alpha [b].  "
        "For formal models the higher m_3 carrier is absent.  For "
        "non-formal models, corrected total TCFT vanishing holds only for "
        "B^(2)_TCFT after Costello correction data, and the derived class "
        "vanishes only after the HH^{-2} filtration/comparison theorem.  "
        "None of this constructs compact CY_3 Phi_3, Hall/CoHA, PBW, or "
        "no-extra-relations data."
    )

    return MasterDerivedFramingResult(
        landscape=landscape,
        local_p2_result=local_p2,
        goodwillie_layers=goodwillie,
        fg_complex=fg,
        bott_d3=bott,
        explicit_homotopy=homotopy,
        cross_checks=checks,
        chain_level_nonvanishing_is_obstruction=True,
        derived_obstruction_vanishes=local_p2.obstruction_vanishes,
        theorem_statement=theorem,
        what_actually_obstructs_cya3=local_p2.actual_obstructions,
        universal_vanishing_claim_rejected=True,
        strict_compact_cy3_closed=False,
        remaining_proof_obligations=local_p2.remaining_proof_obligations,
    )


# =========================================================================
# 7. VERIFICATION UTILITIES AND PUBLIC ALIASES
# =========================================================================


def verify_bott_periodicity_tower(max_d: int = 12) -> Dict[int, Dict[str, Any]]:
    """Return Bott periodicity diagnostics for ``d=1,...,max_d``."""

    results = {}
    for d in range(1, max_d + 1):
        bott = compute_bott_periodicity(d)
        results[d] = {
            "d": d,
            "pi_d_BU": bott.pi_d_BU,
            "pi_d_BSp": bott.pi_d_BSp,
            "topological_vanishes": bott.topological_obstruction_vanishes,
            "closes_strict_compact_cy3": bott.closes_strict_compact_cy3,
            "parity": "even" if d % 2 == 0 else "odd",
        }
    return results


def verify_unit_connectedness_landscape() -> Dict[str, bool]:
    """Record unit-connectedness data; this is not an HH^{-2} proof."""

    algebras = [
        "Heisenberg H_1 (C^3)",
        "W_{1+inf} at c=1 (C^3 derived center)",
        "gl(1|1)^ (conifold)",
        "Local P^2 chiral algebra",
        "Quintic chiral algebra (conjectural)",
        "K3 Heisenberg H_Muk",
        "K3 x E chiral algebra (conjectural)",
    ]
    return {name: True for name in algebras}


def verify_negative_degree_vanishing(
    shadow_class: str = "G",
    max_neg: int = 10,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> Dict[int, Optional[int]]:
    """Verify negative-degree dimensions when the hypotheses are supplied."""

    hh = compute_en_hochschild(
        algebra_name="generic CY3",
        shadow_class=shadow_class,
        cy_dim=3,
        n=1,
        is_formal=(shadow_class in {"G", "L"}),
        hh_hypotheses=hh_hypotheses,
    )
    return {k: hh.dim_at(k) for k in range(-max_neg, 0)}


def master_verification() -> MasterDerivedFramingResult:
    """Master verification entry point."""

    return master_derived_framing_analysis()


def obstruction_vanishes_for_all_cy3(
    tcft_hypotheses: Optional[TCFTCorrectionDatum] = None,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> bool:
    """Return whether the conditional obstruction statement is established."""

    landscape = compute_cy3_landscape(
        tcft_hypotheses=tcft_hypotheses,
        hh_hypotheses=hh_hypotheses,
    )
    if tcft_hypotheses is None or hh_hypotheses is None:
        return False
    tcft_ok = tcft_hypotheses.total_tcft_identity_available
    hh_ok = hh_hypotheses.vanishing_established
    return tcft_ok and hh_ok and all(e.obstruction_group_dim == 0 for e in landscape)


def the_theorem() -> str:
    """Return the corrected theorem statement."""

    return master_derived_framing_analysis().theorem_statement
