r"""Conditional Lurie/Goodwillie diagnostics for the E_2 -> E_3 lane.

This engine records the corrected boundary for the derived S^3-framing
obstruction.

It preserves the useful structural maps:

* Lurie/Francis-Gaitsgory obstruction theory places the E_2 -> E_3 target
  in D^4_{E_2}(A, A).
* Dunn additivity identifies the relative cotangent target with the
  HH^{-2}_{E_1}(A, A) target after the comparison map has been fixed.
* Goodwillie layer language records the E_3/E_2 layer and its convergence
  obligations.

It rejects the stale strengthening:

* unit-connectedness does not by itself prove HH^{-2}_{E_1}(A, A)=0;
* Dunn additivity does not by itself prove contractibility of the lifting
  space;
* Goodwillie layers do not by themselves kill the derived limit terms;
* none of these slogans identifies B_term^(2) with Costello's corrected
  B_TCFT^(2), or constructs compact CY3 Phi_3, Hall/CoHA, PBW, or
  no-extra-relations data.

The strict raw witness is normalized by the terminal-slot convention:

    [m_3, B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0.

Derived obstruction vanishing is recorded only under the explicit package:
comparison map to the obstruction complex, complete/exhaustive/separated/
strongly convergent filtration, empty total-degree -2 first-page line, and
the obstruction cocycle landing in that degree.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

F = Fraction
Word = Tuple[str, ...]


# ============================================================================
# 0. RAW WITNESS, CARRIER SEPARATION, AND HH^{-2} HYPOTHESES
# ============================================================================


@dataclass(frozen=True)
class RawM3B2Witness:
    """Strict nonzero witness for the raw termwise operator B_term^(2)."""

    alpha: Fraction
    input_word: Word
    b_term_of_input: Dict[Word, Fraction]
    m3_after_b_term: Dict[Word, Fraction]
    m3_of_input: Dict[Word, Fraction]
    b_term_after_m3: Dict[Word, Fraction]
    commutator: Dict[Word, Fraction]
    convention: str

    @property
    def coefficient_on_b(self) -> Fraction:
        return self.commutator.get(("b",), F(0))

    @property
    def nonzero(self) -> bool:
        return any(coeff != 0 for coeff in self.commutator.values())

    @property
    def formula(self) -> str:
        return (
            "[m_3,B_term^(2)][a|a|a|a|b] = "
            f"{self.coefficient_on_b} [b]"
        )


def raw_m3_b2_witness(alpha: Fraction = F(1)) -> RawM3B2Witness:
    r"""Return the normalized strict witness for raw ``B_term^(2)``.

    Terminal-slot normalization:

    * ``B_term^(2)[a|a|a|a|b] = 4[a|a|a]``;
    * ``m_3 B_term^(2)`` gives ``4 alpha [b]``;
    * ``m_3`` first gives ``alpha([b|a|b] + [a|b|b])``;
    * ``B_term^(2) m_3`` gives ``2 alpha [b]``.
    """

    alpha = F(alpha)
    return RawM3B2Witness(
        alpha=alpha,
        input_word=("a", "a", "a", "a", "b"),
        b_term_of_input={("a", "a", "a"): F(4)},
        m3_after_b_term={("b",): F(4) * alpha},
        m3_of_input={("b", "a", "b"): alpha, ("a", "b", "b"): alpha},
        b_term_after_m3={("b",): F(2) * alpha},
        commutator={("b",): F(2) * alpha},
        convention="terminal-slot B_term^(2), characteristic zero",
    )


@dataclass(frozen=True)
class CarrierSeparationResult:
    """Separation of raw, TCFT-corrected, and derived obstruction carriers."""

    raw_operator: str
    corrected_operator: str
    derived_target: str
    raw_equals_corrected: bool
    raw_witness: RawM3B2Witness
    tcft_identity_requires_correction_datum: bool
    derived_target_requires_comparison_map: bool
    compact_cy3_closure_follows: bool


def carrier_separation(alpha: Fraction = F(1)) -> CarrierSeparationResult:
    """Return the corrected carrier separation datum."""

    return CarrierSeparationResult(
        raw_operator="B_term^(2)",
        corrected_operator="B_TCFT^(2)",
        derived_target="HH^{-2}_{E_1}(A,A)",
        raw_equals_corrected=False,
        raw_witness=raw_m3_b2_witness(alpha),
        tcft_identity_requires_correction_datum=True,
        derived_target_requires_comparison_map=True,
        compact_cy3_closure_follows=False,
    )


@dataclass(frozen=True)
class HHMinusTwoFiltrationHypotheses:
    """Exact hypothesis package for derived HH^{-2} vanishing."""

    connective_unit_connected_model: bool = False
    dunn_additivity_identification: bool = False
    goodwillie_layer_identified: bool = False
    comparison_to_obstruction_complex: bool = False
    obstruction_cocycle_degree_minus_two: bool = False
    filtration_complete: bool = False
    filtration_exhaustive: bool = False
    filtration_separated: bool = False
    strong_convergence: bool = False
    empty_total_degree_minus_two_line: bool = False

    @property
    def structural_identifications_available(self) -> bool:
        return (
            self.dunn_additivity_identification
            and self.goodwillie_layer_identified
        )

    @property
    def vanishing_established(self) -> bool:
        return all(
            [
                self.connective_unit_connected_model,
                self.dunn_additivity_identification,
                self.goodwillie_layer_identified,
                self.comparison_to_obstruction_complex,
                self.obstruction_cocycle_degree_minus_two,
                self.filtration_complete,
                self.filtration_exhaustive,
                self.filtration_separated,
                self.strong_convergence,
                self.empty_total_degree_minus_two_line,
            ]
        )

    @property
    def missing_hypotheses(self) -> Tuple[str, ...]:
        checks = [
            (self.connective_unit_connected_model, "connective unit-connected model"),
            (self.dunn_additivity_identification, "Dunn additivity identification"),
            (self.goodwillie_layer_identified, "Goodwillie layer identification"),
            (self.comparison_to_obstruction_complex, "comparison map to S^3 obstruction complex"),
            (self.obstruction_cocycle_degree_minus_two, "obstruction cocycle lands in total degree -2"),
            (self.filtration_complete, "complete filtration"),
            (self.filtration_exhaustive, "exhaustive filtration"),
            (self.filtration_separated, "separated filtration"),
            (self.strong_convergence, "strong convergence"),
            (self.empty_total_degree_minus_two_line, "empty total-degree -2 first-page line"),
        ]
        return tuple(label for ok, label in checks if not ok)


def default_hh_minus_two_hypotheses() -> HHMinusTwoFiltrationHypotheses:
    """Return the structural slogan package, deliberately not a proof."""

    return HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True,
        dunn_additivity_identification=True,
        goodwillie_layer_identified=True,
    )


def complete_hh_minus_two_hypotheses() -> HHMinusTwoFiltrationHypotheses:
    """Return the complete package under which HH^{-2} vanishing is proved."""

    return HHMinusTwoFiltrationHypotheses(
        connective_unit_connected_model=True,
        dunn_additivity_identification=True,
        goodwillie_layer_identified=True,
        comparison_to_obstruction_complex=True,
        obstruction_cocycle_degree_minus_two=True,
        filtration_complete=True,
        filtration_exhaustive=True,
        filtration_separated=True,
        strong_convergence=True,
        empty_total_degree_minus_two_line=True,
    )


# ============================================================================
# 1. ANDRE-QUILLEN AND COTANGENT DATA
# ============================================================================


@dataclass
class AQCohomologyData:
    r"""Andre-Quillen target data for an E_2-algebra.

    Low-degree deformation dimensions are model diagnostics.  The critical
    D^4_{E_2} target is identified with HH^{-2}_{E_1} only conditionally;
    it is not set to zero from unit-connectedness alone.
    """

    algebra_name: str
    shadow_class: str
    cy_dim: int
    is_formal: bool
    is_unit_connected: bool
    aq_dims: Dict[int, Optional[int]]
    d4_dim: Optional[int]
    d4_vanishes: bool
    d4_status: str
    hh_hypotheses: HHMinusTwoFiltrationHypotheses
    proves_compact_cy3_closure: bool
    mechanism: str

    def dim_at(self, degree: int) -> Optional[int]:
        """Dimension of D^degree_{E_2}(A,A), when established."""

        return self.aq_dims.get(degree)


@dataclass
class CotangentComplexData:
    r"""Structural cotangent-complex data for the E_2 -> E_3 target."""

    algebra_name: str
    min_degree: int
    is_concentrated_positive: bool
    relative_shift: int
    relative_min_degree: int
    structural_identification: str
    proves_hh_minus_two: bool
    proves_compact_cy3_closure: bool
    required_hypotheses: Tuple[str, ...]


def compute_cotangent_complex(
    algebra_name: str,
    is_unit_connected: bool = True,
) -> CotangentComplexData:
    r"""Return the Dunn-shifted cotangent target data.

    This records the structural shift.  It is not the HH^{-2} vanishing
    theorem unless the filtration and comparison hypotheses are supplied
    elsewhere.
    """

    if is_unit_connected:
        min_degree = 1
        concentrated = True
        relative_min = 3
    else:
        min_degree = 0
        concentrated = False
        relative_min = 2

    return CotangentComplexData(
        algebra_name=algebra_name,
        min_degree=min_degree,
        is_concentrated_positive=concentrated,
        relative_shift=2,
        relative_min_degree=relative_min,
        structural_identification="L_{E_3/E_2}(A) = Sigma^2 L_{E_1}(A)",
        proves_hh_minus_two=False,
        proves_compact_cy3_closure=False,
        required_hypotheses=(
            "comparison map to S^3 obstruction complex",
            "complete/exhaustive/separated/strongly convergent filtration",
            "empty total-degree -2 first-page line",
        ),
    )


def _low_degree_aq_dims(shadow_class: str) -> Dict[int, Optional[int]]:
    d1 = {"G": 1, "L": 2, "C": 2, "M": 3}
    d2 = {"G": 0, "L": 1, "C": 1, "M": 3}
    if shadow_class not in d1:
        raise ValueError(f"unknown shadow class {shadow_class!r}")
    return {0: 0, 1: d1[shadow_class], 2: d2[shadow_class]}


def compute_aq_cohomology(
    algebra_name: str,
    shadow_class: str = "G",
    cy_dim: int = 3,
    is_formal: bool = True,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> AQCohomologyData:
    r"""Compute the E_2-AQ target data under explicit hypotheses."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    aq_dims = _low_degree_aq_dims(shadow_class)

    if hypotheses.vanishing_established:
        d4_dim: Optional[int] = 0
        d4_status = "proved_under_HH_minus_two_filtration_hypotheses"
        for degree in range(3, 11):
            aq_dims[degree] = 0
    else:
        d4_dim = None
        d4_status = "not_established_by_unit_connectedness_Dunn_or_Goodwillie"
        for degree in range(3, 11):
            aq_dims[degree] = None

    mechanism = (
        f"For {algebra_name}, Lurie/Francis-Gaitsgory identifies the "
        "E_2 -> E_3 target as D^4_{E_2}(A,A), and Dunn identifies this "
        "target with HH^{-2}_{E_1}(A,A) after the comparison map. "
        "Vanishing is established only when the comparison map and the "
        "complete/exhaustive/separated/strongly convergent filtration with "
        "empty total-degree -2 line are supplied."
    )

    return AQCohomologyData(
        algebra_name=algebra_name,
        shadow_class=shadow_class,
        cy_dim=cy_dim,
        is_formal=is_formal,
        is_unit_connected=hypotheses.connective_unit_connected_model,
        aq_dims=aq_dims,
        d4_dim=d4_dim,
        d4_vanishes=(d4_dim == 0),
        d4_status=d4_status,
        hh_hypotheses=hypotheses,
        proves_compact_cy3_closure=False,
        mechanism=mechanism,
    )


# ============================================================================
# 2. GOODWILLIE LAYER DATA
# ============================================================================


@dataclass
class GoodwillieDerivativeData:
    r"""The kth Goodwillie layer of the identity functor on E_2-algebras."""

    k: int
    coefficient_space: str
    coefficient_dim: int
    tensor_power: int
    symmetry_group: str
    symmetry_order: int
    input_connectivity: int
    sphere_shift: int
    total_connectivity: int
    pi_0_vanishes: Optional[bool]
    convergence_hypotheses_supplied: bool
    derived_limits_killed: bool
    proves_hh_minus_two: bool
    proves_compact_cy3_closure: bool
    missing_hypotheses: Tuple[str, ...]
    mechanism: str


def compute_goodwillie_derivative(
    k: int,
    is_unit_connected: bool = True,
    strong_convergence: bool = False,
    derived_limits_killed: bool = False,
) -> GoodwillieDerivativeData:
    r"""Compute Goodwillie layer metadata with convergence obligations."""

    coefficient_dim = k - 1
    symmetry_order = 1
    for i in range(1, k + 1):
        symmetry_order *= i

    if is_unit_connected:
        input_conn = 0
        sphere_shift = -(k - 1)
        total_conn = max(input_conn + sphere_shift, -(k - 1))
    else:
        input_conn = -1
        sphere_shift = -(k - 1)
        total_conn = input_conn + sphere_shift

    missing: List[str] = []
    if not strong_convergence:
        missing.append("Goodwillie tower strong convergence")
    if not derived_limits_killed:
        missing.append("vanishing of derived limit terms")

    if not is_unit_connected:
        pi_0_vanishes: Optional[bool] = False
        mechanism = "Non-unit-connected input may have a nonzero layer."
    elif not missing and k >= 2:
        pi_0_vanishes = True
        mechanism = (
            f"partial_{k}(Id)(A) is evaluated under strong convergence and "
            "vanishing derived limits, so the pi_0 layer is killed."
        )
    else:
        pi_0_vanishes = None
        mechanism = (
            f"partial_{k}(Id)(A) = Map(S^{{{k-1}}}, A^{{tensor {k}}})"
            f"_{{h S_{k}}} is the correct layer, but connectivity language "
            "does not by itself prove HH^{-2}_{E_1}=0."
        )

    proves_hh = pi_0_vanishes is True and not missing
    return GoodwillieDerivativeData(
        k=k,
        coefficient_space=f"S^{{{k-1}}}",
        coefficient_dim=coefficient_dim,
        tensor_power=k,
        symmetry_group=f"S_{k}",
        symmetry_order=symmetry_order,
        input_connectivity=input_conn,
        sphere_shift=sphere_shift,
        total_connectivity=total_conn,
        pi_0_vanishes=pi_0_vanishes,
        convergence_hypotheses_supplied=strong_convergence,
        derived_limits_killed=derived_limits_killed,
        proves_hh_minus_two=proves_hh,
        proves_compact_cy3_closure=False,
        missing_hypotheses=tuple(missing),
        mechanism=mechanism,
    )


def compute_goodwillie_tower(
    max_k: int = 6,
    is_unit_connected: bool = True,
    strong_convergence: bool = False,
    derived_limits_killed: bool = False,
) -> List[GoodwillieDerivativeData]:
    """Return Goodwillie layers 1 through ``max_k``."""

    return [
        compute_goodwillie_derivative(
            k,
            is_unit_connected=is_unit_connected,
            strong_convergence=strong_convergence,
            derived_limits_killed=derived_limits_killed,
        )
        for k in range(1, max_k + 1)
    ]


# ============================================================================
# 3. FRANCIS-GAITSGORY DEFORMATION COMPLEX
# ============================================================================


@dataclass
class FGDeformationResult:
    """Francis-Gaitsgory relative deformation data via AQ targets."""

    source_operad: str
    target_operad: str
    algebra_name: str
    shadow_class: str
    fiber_h0: Optional[int]
    fiber_h1: Optional[int]
    fiber_h2: Optional[int]
    is_unobstructed: bool
    status: str
    missing_hypotheses: Tuple[str, ...]
    mechanism: str


def compute_fg_deformation_aq(
    algebra_name: str,
    shadow_class: str = "G",
    is_unit_connected: bool = True,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> FGDeformationResult:
    """Compute the relative FG obstruction data conditionally."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    if hypotheses.vanishing_established and is_unit_connected:
        return FGDeformationResult(
            source_operad="E_2",
            target_operad="E_3",
            algebra_name=algebra_name,
            shadow_class=shadow_class,
            fiber_h0=0,
            fiber_h1=0,
            fiber_h2=0,
            is_unobstructed=True,
            status="proved_under_HH_minus_two_filtration_hypotheses",
            missing_hypotheses=(),
            mechanism=(
                "The relative FG target is identified with HH^{-2}_{E_1}; "
                "the complete filtration/comparison package kills it."
            ),
        )

    return FGDeformationResult(
        source_operad="E_2",
        target_operad="E_3",
        algebra_name=algebra_name,
        shadow_class=shadow_class,
        fiber_h0=None,
        fiber_h1=None,
        fiber_h2=None,
        is_unobstructed=False,
        status="not_established",
        missing_hypotheses=hypotheses.missing_hypotheses,
        mechanism=(
            "The relative FG target has been identified, but the "
            "HH^{-2} vanishing theorem has not been supplied."
        ),
    )


# ============================================================================
# 4. CY3 LANDSCAPE
# ============================================================================


@dataclass
class AQLandscapeEntry:
    """One conditional AQ entry for a standard CY3 example."""

    name: str
    shadow_class: str
    is_formal: bool
    d4_dim: Optional[int]
    d4_vanishes: bool
    d2_dim: int
    goodwillie_3rd_vanishes: Optional[bool]
    agrees_with_dunn: bool
    dunn_identification_available: bool
    compact_cy3_closed: bool
    status: str


_CY3_GEOMETRIES = [
    ("C^3 (Jordan quiver)", "G", True),
    ("Conifold (resolved)", "G", True),
    ("Local P^2", "M", False),
    ("Local P^1 x P^1", "G", True),
    ("Quintic threefold", "G", True),
    ("K3 x E", "G", True),
    ("Local P^2 (Fermat)", "M", False),
]


def compute_aq_landscape(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> List[AQLandscapeEntry]:
    """Compute conditional AQ target data for the standard CY3 list."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    entries: List[AQLandscapeEntry] = []

    for name, shadow_class, is_formal in _CY3_GEOMETRIES:
        aq = compute_aq_cohomology(
            algebra_name=name,
            shadow_class=shadow_class,
            cy_dim=3,
            is_formal=is_formal,
            hh_hypotheses=hypotheses,
        )
        gw3 = compute_goodwillie_derivative(
            3,
            is_unit_connected=True,
            strong_convergence=hypotheses.strong_convergence,
            derived_limits_killed=hypotheses.empty_total_degree_minus_two_line,
        )
        eq = verify_dunn_equivalence(
            name,
            shadow_class,
            is_formal,
            hh_hypotheses=hypotheses,
        )
        entries.append(
            AQLandscapeEntry(
                name=name,
                shadow_class=shadow_class,
                is_formal=is_formal,
                d4_dim=aq.d4_dim,
                d4_vanishes=aq.d4_vanishes,
                d2_dim=aq.dim_at(2) or 0,
                goodwillie_3rd_vanishes=gw3.pi_0_vanishes,
                agrees_with_dunn=eq.agree,
                dunn_identification_available=eq.structural_identification_available,
                compact_cy3_closed=False,
                status=aq.d4_status,
            )
        )

    return entries


# ============================================================================
# 5. EXPLICIT K3 x E AND LOCAL P^2 DIAGNOSTICS
# ============================================================================


@dataclass
class K3EAQResult:
    """K3 x E AQ target data with de Rham/categorical separation."""

    k3_formal: bool
    k3_categorical_formality_certified: bool
    k3_e2_structure: str
    e_formal: bool
    e_categorical_formality_certified: bool
    e_einf_structure: str
    product_e2: bool
    product_a_infinity_model_certified: bool
    d4_k3: Optional[int]
    d4_e: Optional[int]
    d4_product: Optional[int]
    d4_product_vanishes: bool
    kappa_ch: int
    kappa_ch_Heis: int
    mukai_rank: int
    compact_cy3_closed: bool
    mechanism: str


def compute_k3e_aq(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> K3EAQResult:
    """Compute the K3 x E conditional target data."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    critical_dim: Optional[int] = 0 if hypotheses.vanishing_established else None
    return K3EAQResult(
        k3_formal=True,
        k3_categorical_formality_certified=False,
        k3_e2_structure="proved CY-A_2 structure on the K3-side input",
        e_formal=True,
        e_categorical_formality_certified=False,
        e_einf_structure="d=1 E_infty structure; categorical formality separate",
        product_e2=True,
        product_a_infinity_model_certified=False,
        d4_k3=critical_dim,
        d4_e=critical_dim,
        d4_product=critical_dim,
        d4_product_vanishes=(critical_dim == 0),
        kappa_ch=0,
        kappa_ch_Heis=3,
        mukai_rank=24,
        compact_cy3_closed=False,
        mechanism=(
            "K3 and E are de Rham formal, but this engine does not promote "
            "that to categorical A_infinity formality of D^b(Coh(K3 x E)). "
            "D^4 vanishing is recorded only under the HH^{-2} filtration/"
            "comparison hypotheses.  kappa_ch(K3 x E)=0, the Heisenberg "
            "shadow value is 3, and the Mukai/fiber rank is 24."
        ),
    )


@dataclass
class LocalP2AQResult:
    """Local P^2 diagnostic separating raw chain failure from derived target."""

    is_formal: bool
    shadow_class: str
    has_m3: bool
    chain_level_fails: bool
    raw_witness: RawM3B2Witness
    d4_dim: Optional[int]
    d4_vanishes: bool
    d2_dim: int
    is_unit_connected: bool
    cotangent_min_degree: int
    relative_cotangent_min_degree: int
    obstruction_degree: int
    compact_cy3_closed: bool
    mechanism: str


def compute_local_p2_aq(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> LocalP2AQResult:
    """Compute the local P^2 conditional obstruction diagnostic."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    critical_dim: Optional[int] = 0 if hypotheses.vanishing_established else None
    witness = raw_m3_b2_witness()
    return LocalP2AQResult(
        is_formal=False,
        shadow_class="M",
        has_m3=True,
        chain_level_fails=witness.nonzero,
        raw_witness=witness,
        d4_dim=critical_dim,
        d4_vanishes=(critical_dim == 0),
        d2_dim=3,
        is_unit_connected=hypotheses.connective_unit_connected_model,
        cotangent_min_degree=1,
        relative_cotangent_min_degree=3,
        obstruction_degree=4,
        compact_cy3_closed=False,
        mechanism=(
            "Local P^2 has a nonzero raw chain witness for B_term^(2). "
            "That witness is not a compact CY3 construction and not the "
            "corrected TCFT operator.  The D^4/HH^{-2} target vanishes only "
            "under the explicit comparison and filtration package."
        ),
    )


# ============================================================================
# 6. DUNN IDENTIFICATION
# ============================================================================


@dataclass
class DunnEquivalenceResult:
    """Dunn structural identification between D^4 and HH^{-2} targets."""

    algebra_name: str
    shadow_class: str
    d4_e2_dim: Optional[int]
    hh_minus2_e1_dim: Optional[int]
    agree: bool
    structural_identification_available: bool
    vanishing_established: bool
    missing_hypotheses: Tuple[str, ...]
    proves_compact_cy3_closure: bool
    identification_chain: List[str]


def verify_dunn_equivalence(
    algebra_name: str,
    shadow_class: str = "G",
    is_formal: bool = True,
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> DunnEquivalenceResult:
    r"""Record the Dunn identification; prove vanishing only conditionally."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    aq = compute_aq_cohomology(
        algebra_name,
        shadow_class,
        3,
        is_formal,
        hh_hypotheses=hypotheses,
    )
    hh_minus2 = 0 if hypotheses.vanishing_established else None
    d4 = aq.d4_dim

    identification = [
        f"D^4_{{E_2}}({algebra_name}, {algebra_name})",
        "= pi_0 Map_{Mod_A^{E_2}}(Sigma^2 L_{E_1}(A), A)",
        "= HH^{-2}_{E_1}(A,A) after the comparison map",
        (
            "= 0 under complete/separated/strongly convergent filtration "
            "with empty total-degree -2 line"
            if hypotheses.vanishing_established
            else "vanishing not established by Dunn additivity alone"
        ),
    ]

    return DunnEquivalenceResult(
        algebra_name=algebra_name,
        shadow_class=shadow_class,
        d4_e2_dim=d4,
        hh_minus2_e1_dim=hh_minus2,
        agree=(d4 is not None and d4 == hh_minus2),
        structural_identification_available=(
            hypotheses.dunn_additivity_identification
        ),
        vanishing_established=hypotheses.vanishing_established,
        missing_hypotheses=hypotheses.missing_hypotheses,
        proves_compact_cy3_closure=False,
        identification_chain=identification,
    )


def verify_dunn_equivalence_landscape(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> Dict[str, bool]:
    """Return numerical D^4/HH^{-2} agreement status for the standard list."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    results: Dict[str, bool] = {}
    for name, shadow_class, is_formal in _CY3_GEOMETRIES:
        eq = verify_dunn_equivalence(
            name,
            shadow_class,
            is_formal,
            hh_hypotheses=hypotheses,
        )
        results[name] = eq.agree
    return results


# ============================================================================
# 7. MASTER ANALYSIS
# ============================================================================


@dataclass
class LurieE3ObstructionResult:
    """Master conditional AQ/Goodwillie/Dunn analysis."""

    aq_landscape: List[AQLandscapeEntry]
    k3e_result: K3EAQResult
    local_p2_result: LocalP2AQResult
    goodwillie_tower: List[GoodwillieDerivativeData]
    fg_deformation: FGDeformationResult
    dunn_equivalence: Dict[str, bool]
    cotangent_data: CotangentComplexData
    carrier_separation: CarrierSeparationResult
    hh_hypotheses: HHMinusTwoFiltrationHypotheses
    d4_vanishes_all_cy3: bool
    goodwillie_3rd_vanishes: Optional[bool]
    agrees_with_dunn_approach: bool
    obstruction_space_contractible: bool
    compact_cy3_closed: bool
    compact_closure_by_slogan: bool
    remaining_obligations: Tuple[str, ...]
    proposition_statement: str


def master_lurie_e3_analysis(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> LurieE3ObstructionResult:
    """Run the corrected conditional master analysis."""

    hypotheses = hh_hypotheses or default_hh_minus_two_hypotheses()
    landscape = compute_aq_landscape(hypotheses)
    k3e = compute_k3e_aq(hypotheses)
    p2 = compute_local_p2_aq(hypotheses)
    gw_tower = compute_goodwillie_tower(
        max_k=6,
        strong_convergence=hypotheses.strong_convergence,
        derived_limits_killed=hypotheses.empty_total_degree_minus_two_line,
    )
    fg = compute_fg_deformation_aq("Local P^2", "M", hh_hypotheses=hypotheses)
    dunn = verify_dunn_equivalence_landscape(hypotheses)
    cotangent = compute_cotangent_complex("Local P^2")
    carriers = carrier_separation()

    d4_all = all(entry.d4_vanishes for entry in landscape)
    dunn_all = all(dunn.values())
    gw3 = gw_tower[2].pi_0_vanishes

    proposition = (
        "PROPOSITION (conditional Lurie/Goodwillie obstruction target). "
        "For a fixed strictified Hochschild E_1-model A equipped with a "
        "comparison map from the S^3-framing obstruction complex to "
        "C^bullet_{E_1}(A,A)[2], and with a complete, exhaustive, "
        "separated, strongly convergent filtration whose first page has "
        "empty total-degree -2 line, the identified target "
        "D^4_{E_2}(A,A) = HH^{-2}_{E_1}(A,A) vanishes. "
        "Without these hypotheses, unit-connectedness, Dunn additivity, "
        "and Goodwillie layer language identify targets and obligations "
        "but do not prove vanishing.  The raw operator B_term^(2) is not "
        "Costello's B_TCFT^(2): "
        f"{carriers.raw_witness.formula} != 0 for alpha != 0. "
        "No compact CY3 Phi_3, Hall/CoHA, PBW, or no-extra-relations "
        "closure follows from this calculation."
    )

    return LurieE3ObstructionResult(
        aq_landscape=landscape,
        k3e_result=k3e,
        local_p2_result=p2,
        goodwillie_tower=gw_tower,
        fg_deformation=fg,
        dunn_equivalence=dunn,
        cotangent_data=cotangent,
        carrier_separation=carriers,
        hh_hypotheses=hypotheses,
        d4_vanishes_all_cy3=d4_all,
        goodwillie_3rd_vanishes=gw3,
        agrees_with_dunn_approach=dunn_all,
        obstruction_space_contractible=False,
        compact_cy3_closed=False,
        compact_closure_by_slogan=False,
        remaining_obligations=(
            "compact CY3 strictified Hochschild model",
            "global Phi_3 functoriality",
            "compact Hall/CoHA correspondence",
            "PBW and no-extra-relations theorem",
            "contractibility of the whole lifting space",
        ),
        proposition_statement=proposition,
    )


# ============================================================================
# 8. CONVENIENCE ALIASES
# ============================================================================


def d4_vanishes_for_all_cy3(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> bool:
    """Return whether D^4 vanishing is established for the standard list."""

    return all(entry.d4_vanishes for entry in compute_aq_landscape(hh_hypotheses))


def the_proposition(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> str:
    """Return the corrected conditional proposition statement."""

    return master_lurie_e3_analysis(hh_hypotheses).proposition_statement


def cross_check_with_dunn(
    hh_hypotheses: Optional[HHMinusTwoFiltrationHypotheses] = None,
) -> bool:
    """Return whether numerical D^4/HH^{-2} agreement is established."""

    return all(verify_dunn_equivalence_landscape(hh_hypotheses).values())
