r"""Finite bridge witnesses for the K3 x E comparison chain.

This module packages the low-height data already computed in the tree.
It does not prove the missing finite-height theorem. It records the
finite-height pieces that the theorem would have to preserve:

* discriminant-graded scattering / Borcherds data
* finite Stokes hCS/Hall Maurer-Cartan and ordered product gates
* finite Rees-to-vanishing-cycle realization gates
* finite realized hCS/Hall composite gates
* finite realized CY3 shifted-bracket compatibility gates
* finite compact-support Beck-Chevalley gates
* finite compact Hall product associativity gates
* finite Hall-Drinfeld double datum gates
* finite realized hCS/Hall inverse-system transition gates
* finite total Cech/Ran Maurer-Cartan gates
* finite simplicial cyclic contraction face-compatibility gates
* finite scattering quantum-torus multiplication gates
* bar-Euler generators and rank-one exponents
* bar lattice-grading gates
* bar regularization / Weyl-vector gates
* Rademacher-growth, polar/Bessel, and truncation-error finite gates
* BRST central-charge balance
* BRST coefficient/parity fixture
* BRST no-ghost finite spectral-sequence gates
* BRST/Borcherds finite bracket and Serre-relation comparison gates
* BRST finite momentum-height projection gates
* Yangian finite current-candidate packets
* Yangian finite spectral kernel label packets
* Yangian formal OPE pole-layer packets
* Yangian finite BRST-residue descent gates
* Yangian finite OPE/Serre and PBW associated-graded gates
* Yangian finite spectral R-matrix equation gates
* Yangian finite spectral associator obstruction packets
* Yangian current templates

The point is to keep the finite witness layer explicit and machine-readable.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from typing import Any, Dict, Iterable, List, Optional, Tuple

from compute.lib import bar_euler_borcherds as _bar
from compute.lib.hall_borcherds_gate import (
    HallBorcherdsWitnesses,
    RecognitionEnvelopeWitnesses,
    SourceCompactDoubleGateWitnesses,
    SourceGateBoundaryReport,
    SourceGateObligationMatrix,
    SourceGateTaskMap,
    SourceProRecognitionGateWitnesses,
    evaluate_gate,
    evaluate_recognition_envelope,
    exact_matrix_rank,
    finite_defect_vanishings,
    source_matrix_forces_faithfulness,
    source_gate_boundary_report,
    source_gate_obligation_matrix,
    source_gate_task_map,
    vector_in_row_span,
)
from compute.lib import phi01_shadow_decomposition as _shadow
from compute.lib import shadow_rademacher_identification as _rad


BRST_LATTICE_C = 3
BRST_TRANSVERSE_C = 23
BRST_GHOST_C = -26
BRST_TOTAL_C = BRST_LATTICE_C + BRST_TRANSVERSE_C + BRST_GHOST_C

YANGIAN_WEIGHT_TEMPLATE = "h_eps = (D + 1) - D * eps"
YANGIAN_LIMIT_EPSILON_1 = 1
REQUIRED_BRIDGE_COMPONENTS = ("scatt", "bar", "rad", "BRST", "Yang")
K3E_CLOSURE_BRIDGES = (
    "source_hall_borcherds_gate",
    "framed_d3_assignment",
    "compact_hall_promotion",
    "scattering_root_identification",
    "bkm_bar_dictionary",
    "shadow_rademacher_comparison",
    "brst_realization",
    "vertex_operator_yangian",
)

Vector = Tuple[Fraction, ...]
Matrix = Tuple[Vector, ...]


def _fraction_vector(vector: Iterable[Any]) -> Vector:
    return tuple(Fraction(entry) for entry in vector)


def _fraction_matrix(matrix: Iterable[Iterable[Any]]) -> Matrix:
    normalized = tuple(_fraction_vector(row) for row in matrix)
    if not normalized:
        return ()
    width = len(normalized[0])
    if any(len(row) != width for row in normalized):
        raise ValueError("matrix rows must have common width")
    return normalized


def _matrix_width(matrix: Matrix) -> int:
    return len(matrix[0]) if matrix else 0


def _matrix_shape(matrix: Matrix) -> Tuple[int, int]:
    return (len(matrix), _matrix_width(matrix))


def _validate_matrix_shape(matrix: Matrix, expected_shape: Tuple[int, int], name: str) -> None:
    if _matrix_shape(matrix) != expected_shape:
        raise ValueError(f"{name} must have shape {expected_shape}")


def _matrix_transpose(matrix: Matrix) -> Matrix:
    matrix = _fraction_matrix(matrix)
    if not matrix:
        return ()
    width = _matrix_width(matrix)
    return tuple(tuple(row[column] for row in matrix) for column in range(width))


def _matrix_vector_product(matrix: Matrix, vector: Vector) -> Vector:
    if matrix and _matrix_width(matrix) != len(vector):
        raise ValueError("matrix width must equal vector length")
    return tuple(sum(entry * value for entry, value in zip(row, vector)) for row in matrix)


def _matrix_product(left: Matrix, right: Matrix) -> Matrix:
    if not left:
        return ()
    if not right:
        if _matrix_width(left) != 0:
            raise ValueError("left matrix width must equal right matrix height")
        return tuple(() for _ in left)
    if _matrix_width(left) != len(right):
        raise ValueError("left matrix width must equal right matrix height")
    right_columns = _matrix_transpose(right)
    return tuple(
        tuple(sum(entry * value for entry, value in zip(row, column)) for column in right_columns)
        for row in left
    )


def _vector_difference(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vectors must have the same length")
    return tuple(left_entry - right_entry for left_entry, right_entry in zip(left, right))


def _vector_sum(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vectors must have the same length")
    return tuple(left_entry + right_entry for left_entry, right_entry in zip(left, right))


def _matrix_difference(left: Matrix, right: Matrix) -> Matrix:
    left = _fraction_matrix(left)
    right = _fraction_matrix(right)
    if len(left) != len(right):
        raise ValueError("matrices must have the same height")
    if left and right and _matrix_width(left) != _matrix_width(right):
        raise ValueError("matrices must have the same width")
    return tuple(_vector_difference(left_row, right_row) for left_row, right_row in zip(left, right))


def _matrix_sum(left: Matrix, right: Matrix) -> Matrix:
    left = _fraction_matrix(left)
    right = _fraction_matrix(right)
    if len(left) != len(right):
        raise ValueError("matrices must have the same height")
    if left and right and _matrix_width(left) != _matrix_width(right):
        raise ValueError("matrices must have the same width")
    return tuple(
        tuple(left_entry + right_entry for left_entry, right_entry in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def _matrix_kronecker_product(left: Matrix, right: Matrix) -> Matrix:
    left = _fraction_matrix(left)
    right = _fraction_matrix(right)
    if not left or not right:
        return ()
    return tuple(
        tuple(left_entry * right_entry for left_entry in left_row for right_entry in right_row)
        for left_row in left
        for right_row in right
    )


def _matrix_horizontal_concat(left: Matrix, right: Matrix) -> Matrix:
    left = _fraction_matrix(left)
    right = _fraction_matrix(right)
    if len(left) != len(right):
        raise ValueError("matrices must have the same height")
    return tuple(left_row + right_row for left_row, right_row in zip(left, right))


def _matrix_rref(matrix: Matrix) -> Tuple[Matrix, Tuple[int, ...]]:
    matrix = _fraction_matrix(matrix)
    rows = [list(row) for row in matrix]
    if not rows:
        return (), ()
    height = len(rows)
    width = len(rows[0])
    pivot_columns: List[int] = []
    pivot_row = 0
    for column in range(width):
        pivot = None
        for candidate in range(pivot_row, height):
            if rows[candidate][column] != 0:
                pivot = candidate
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row_index in range(height):
            if row_index == pivot_row:
                continue
            factor = rows[row_index][column]
            if factor != 0:
                rows[row_index] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row_index], rows[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == height:
            break
    return tuple(tuple(row) for row in rows), tuple(pivot_columns)


def _matrix_nullspace_basis(matrix: Matrix) -> Tuple[Vector, ...]:
    matrix = _fraction_matrix(matrix)
    if not matrix:
        return ()
    rref, pivot_columns = _matrix_rref(matrix)
    width = _matrix_width(matrix)
    pivot_set = set(pivot_columns)
    basis: List[Vector] = []
    for free_column in range(width):
        if free_column in pivot_set:
            continue
        vector = [Fraction(0) for _ in range(width)]
        vector[free_column] = Fraction(1)
        for row_index, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -rref[row_index][free_column]
        basis.append(tuple(vector))
    return tuple(basis)


def _solve_square_linear_system(matrix: Matrix, rhs: Vector, name: str) -> Vector:
    matrix = _fraction_matrix(matrix)
    rhs = _fraction_vector(rhs)
    height, width = _matrix_shape(matrix)
    if height != width:
        raise ValueError(f"{name} matrix must be square")
    if len(rhs) != height:
        raise ValueError(f"{name} right-hand side has incompatible length")
    augmented = tuple(row + (rhs[index],) for index, row in enumerate(matrix))
    rref, pivot_columns = _matrix_rref(augmented)
    if pivot_columns != tuple(range(width)):
        raise ValueError(f"{name} matrix must be nonsingular")
    return tuple(rref[index][-1] for index in range(width))


def _column_vector_rank(vectors: Iterable[Vector]) -> int:
    vector_list = _fraction_matrix(vectors)
    if not vector_list:
        return 0
    return exact_matrix_rank(_matrix_transpose(vector_list))


def _validate_cochain_matrix_width(matrix: Matrix, width: int, name: str) -> None:
    matrix = _fraction_matrix(matrix)
    if matrix and _matrix_width(matrix) != width:
        raise ValueError(f"{name} must have spectral associator cochain width")


@dataclass(frozen=True)
class FiniteBridgeWitness:
    """Compact record of the finite-height witness layer."""

    scattering: "ScatteringWitness"
    bar: "BarWitness"
    rademacher: "RademacherWitness"
    brst: "BRSTWitness"
    yangian: "YangianWitness"
    open_lemmas: List[str]


@dataclass(frozen=True)
class ScatteringWitness:
    max_discriminant: int
    discriminant_table: Dict[int, int]
    support: List[int]
    contains_polar_root: bool
    contains_lightlike_root: bool
    contains_first_imaginary_root: bool
    status: str


@dataclass(frozen=True)
class FiniteScatteringRootRow:
    """One retained finite wall/root exponent comparison."""

    charge: str
    height: int
    discriminant: int
    bps_index: int
    borcherds_exponent: int
    exponent_match: bool


@dataclass(frozen=True)
class FiniteScatteringRootReport:
    """Finite KS-wall/Borcherds-denominator exponent comparison."""

    height_cutoff: int
    rows: Tuple[FiniteScatteringRootRow, ...]
    scattering_support: Tuple[str, ...]
    borcherds_support: Tuple[str, ...]
    missing_support: Tuple[str, ...]
    extra_support: Tuple[str, ...]
    exponent_defects: Tuple[str, ...]
    transition_commutes: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteScatteringQuantumTorusProductRow:
    """One finite quantum-torus product row."""

    left_charge: str
    right_charge: str
    left_height: int
    right_height: int
    supplied_sum: Optional[str]
    retained: bool
    exponent: Optional[Fraction]


@dataclass(frozen=True)
class FiniteScatteringQuantumTorusGate:
    """Finite gate for the truncated scattering quantum-torus product."""

    height_cutoff: int
    charges: Tuple[str, ...]
    product_rows: Tuple[FiniteScatteringQuantumTorusProductRow, ...]
    missing_pairings: Tuple[str, ...]
    missing_sums: Tuple[str, ...]
    skew_defects: Tuple[str, ...]
    height_defects: Tuple[str, ...]
    truncation_defects: Tuple[str, ...]
    associativity_defects: Tuple[str, ...]
    cocycle_defects: Tuple[str, ...]
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteStokesHCSHallSourceGate:
    """Finite Stokes/Maurer-Cartan and ordered-product source gate."""

    finite_bound: int
    source_dimension: int
    target_dimension: int
    source_differential_shape: Tuple[int, int]
    target_differential_shape: Tuple[int, int]
    theta_shape: Tuple[int, int]
    half_convolution_bracket_shape: Tuple[int, int]
    target_after_theta: Matrix
    theta_after_source: Matrix
    maurer_cartan_defect_matrix: Matrix
    maurer_cartan_defect_rank: int
    maurer_cartan_closed: bool
    source_product_shape: Tuple[int, int]
    target_product_shape: Tuple[int, int]
    left_theta_shape: Tuple[int, int]
    right_theta_shape: Tuple[int, int]
    union_theta_shape: Tuple[int, int]
    product_after_components: Matrix
    union_after_product: Matrix
    multiplicativity_defect_matrix: Matrix
    multiplicativity_defect_rank: int
    multiplicative: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteEquivarianceDefectReport:
    """One finite equivariance generator checked against a realization map."""

    label: str
    defect_matrix: Matrix
    defect_rank: int
    compatible: bool


@dataclass(frozen=True)
class FiniteReesVanishingCycleRealizationGate:
    """Finite chain, Thom-Sebastiani, and structure gate for RW."""

    finite_bound: int
    source_dimension: int
    target_dimension: int
    source_differential_shape: Tuple[int, int]
    target_differential_shape: Tuple[int, int]
    realization_shape: Tuple[int, int]
    chain_defect_matrix: Matrix
    thom_sebastiani_left_matrix: Matrix
    thom_sebastiani_right_matrix: Matrix
    thom_sebastiani_defect_matrix: Matrix
    proper_pushforward_defect_matrix: Matrix
    lci_pullback_defect_matrix: Matrix
    orientation_defect_matrix: Matrix
    tate_defect_matrix: Matrix
    support_defect_matrix: Matrix
    completion_defect_matrix: Matrix
    equivariance_reports: Tuple[FiniteEquivarianceDefectReport, ...]
    chain_defect_rank: int
    thom_sebastiani_defect_rank: int
    proper_pushforward_defect_rank: int
    lci_pullback_defect_rank: int
    orientation_defect_rank: int
    tate_defect_rank: int
    support_defect_rank: int
    completion_defect_rank: int
    chain_map: bool
    thom_sebastiani_compatible: bool
    proper_pushforward_compatible: bool
    lci_pullback_compatible: bool
    orientation_compatible: bool
    tate_compatible: bool
    support_compatible: bool
    completion_compatible: bool
    equivariant: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteRealizedHCSHallCompositeGate:
    """Finite gate for the composite RW theta from hCS to critical CoHA."""

    finite_bound: int
    source_dimension: int
    rees_dimension: int
    realized_dimension: int
    realized_theta_matrix: Matrix
    chain_transport_defect_matrix: Matrix
    rees_maurer_cartan_defect_matrix: Matrix
    bracket_transport_defect_matrix: Matrix
    realized_maurer_cartan_defect_matrix: Matrix
    rees_product_defect_matrix: Matrix
    product_transport_defect_matrix: Matrix
    realized_product_defect_matrix: Matrix
    chain_transport_defect_rank: int
    rees_maurer_cartan_defect_rank: int
    bracket_transport_defect_rank: int
    realized_maurer_cartan_defect_rank: int
    rees_product_defect_rank: int
    product_transport_defect_rank: int
    realized_product_defect_rank: int
    chain_transport_compatible: bool
    rees_maurer_cartan_closed: bool
    bracket_transported: bool
    realized_maurer_cartan_closed: bool
    rees_multiplicative: bool
    product_transport_compatible: bool
    realized_multiplicative: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteRealizedCompositeCohomologyTransitionReport:
    """One supplied cohomological transition in the realized composite tower."""

    degree: int
    transition_matrix: Matrix
    upper_dimension: int
    lower_dimension: int
    transition_rank: int
    surjective: bool
    defect: int


@dataclass(frozen=True)
class FiniteRealizedCompositeTransitionMLGate:
    """Finite transition and Mittag-Leffler gate for realized composites."""

    upper_bound: int
    lower_bound: int
    upper_composite_shape: Tuple[int, int]
    lower_composite_shape: Tuple[int, int]
    source_transition_shape: Tuple[int, int]
    realized_transition_shape: Tuple[int, int]
    target_after_upper_composite: Matrix
    lower_composite_after_source: Matrix
    transition_defect_matrix: Matrix
    transition_defect_rank: int
    cohomology_reports: Tuple[FiniteRealizedCompositeCohomologyTransitionReport, ...]
    transition_commutes: bool
    cohomology_mittag_leffler: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteRealizedCY3ShiftedBracketGate:
    """Finite shifted-bracket compatibility gate for realized composites."""

    finite_bound: int
    rees_bracket_defect_matrix: Matrix
    bracket_transport_defect_matrix: Matrix
    realized_bracket_defect_matrix: Matrix
    rees_bracket_defect_rank: int
    bracket_transport_defect_rank: int
    realized_bracket_defect_rank: int
    rees_bracket_compatible: bool
    bracket_transport_compatible: bool
    realized_bracket_compatible: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteCompactSupportBeckChevalleyGate:
    """Finite compact-support Beck-Chevalley square for Hall correspondences."""

    finite_bound: int
    source_dimension: int
    target_dimension: int
    pulled_source_dimension: int
    pulled_target_dimension: int
    beck_chevalley_left_matrix: Matrix
    beck_chevalley_right_matrix: Matrix
    beck_chevalley_defect_matrix: Matrix
    proper_support_defect_matrix: Matrix
    base_lci_support_defect_matrix: Matrix
    source_lci_support_defect_matrix: Matrix
    pulled_proper_support_defect_matrix: Matrix
    beck_chevalley_defect_rank: int
    proper_support_defect_rank: int
    base_lci_support_defect_rank: int
    source_lci_support_defect_rank: int
    pulled_proper_support_defect_rank: int
    beck_chevalley_compatible: bool
    compact_support_compatible: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteCompactHallProductGate:
    """Finite compact Hall product associativity and support gate."""

    finite_height: int
    input_dimensions: Tuple[int, int, int]
    intermediate_dimensions: Tuple[int, int]
    target_dimension: int
    left_product_matrix: Matrix
    right_product_matrix: Matrix
    product_associator_defect_matrix: Matrix
    thom_sebastiani_defect_matrix: Matrix
    orientation_defect_matrix: Matrix
    support_projection_defect_matrices: Tuple[Matrix, ...]
    support_intertwining_defect_matrices: Tuple[Matrix, ...]
    product_associator_defect_rank: int
    thom_sebastiani_defect_rank: int
    orientation_defect_rank: int
    support_projection_defect_ranks: Tuple[int, ...]
    support_intertwining_defect_ranks: Tuple[int, ...]
    product_associative: bool
    thom_sebastiani_associative: bool
    orientation_associative: bool
    compact_support_compatible: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteDrinfeldDoubleDatumGate:
    """Finite normal-form and cross-relation gate for Hall-Drinfeld doubles."""

    finite_height: int
    positive_dimension: int
    negative_dimension: int
    cartan_dimension: int
    double_dimension: int
    triangular_tensor_dimension: int
    triangular_normal_form_rank: int
    pairing_rank: int
    cross_relation_defect_matrix: Matrix
    coproduct_coassociator_defect_matrix: Matrix
    associator_pentagon_defect_matrix: Matrix
    center_compatibility_defect_matrix: Matrix
    cross_relation_defect_rank: int
    coproduct_coassociator_defect_rank: int
    associator_pentagon_defect_rank: int
    center_compatibility_defect_rank: int
    triangular_normal_form_isomorphism: bool
    reduced_pairing_nondegenerate: bool
    cross_relation_compatible: bool
    coproduct_coassociative: bool
    associator_pentagon_compatible: bool
    center_compatible: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteCyclicSDRBlockCompatibilityGate:
    """Finite cyclic SDR and Euler-corrected block multiplicativity gate."""

    finite_bound: int
    ambient_dimension: int
    model_dimension: int
    retraction_defect_matrix: Matrix
    inclusion_chain_defect_matrix: Matrix
    projection_chain_defect_matrix: Matrix
    homotopy_defect_matrix: Matrix
    cyclicity_defect_matrix: Matrix
    block_homotopy_defect_matrix: Matrix
    transferred_action_defect_matrix: Matrix
    hessian_symmetry_defect_matrix: Matrix
    odd_contraction_skew_defect_matrix: Matrix
    hessian_contraction_scalar: Fraction
    euler_product_after_components: Matrix
    union_after_source_product: Matrix
    euler_multiplicativity_defect_matrix: Matrix
    retraction_defect_rank: int
    inclusion_chain_defect_rank: int
    projection_chain_defect_rank: int
    homotopy_defect_rank: int
    cyclicity_defect_rank: int
    block_homotopy_defect_rank: int
    transferred_action_defect_rank: int
    hessian_symmetry_defect_rank: int
    odd_contraction_skew_defect_rank: int
    hessian_contraction_defect_rank: int
    euler_multiplicativity_defect_rank: int
    sdr_closed: bool
    cyclic_closed: bool
    block_transfer_closed: bool
    hessian_cancellation_closed: bool
    multiplicative: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteSimplicialCyclicContractionFaceReport:
    """One finite face-compatibility check for a simplicial contraction."""

    label: str
    inclusion_face_defect_matrix: Matrix
    projection_face_defect_matrix: Matrix
    homotopy_face_defect_matrix: Matrix
    inclusion_face_defect_rank: int
    projection_face_defect_rank: int
    homotopy_face_defect_rank: int
    compatible: bool


@dataclass(frozen=True)
class FiniteSimplicialCyclicContractionGate:
    """Finite simplicial cyclic contraction and face-compatibility gate."""

    finite_bound: int
    ambient_dimension: int
    model_dimension: int
    retraction_defect_matrix: Matrix
    inclusion_chain_defect_matrix: Matrix
    projection_chain_defect_matrix: Matrix
    homotopy_defect_matrix: Matrix
    homotopy_square_matrix: Matrix
    homotopy_inclusion_matrix: Matrix
    projection_homotopy_matrix: Matrix
    cyclicity_defect_matrix: Matrix
    face_reports: Tuple[FiniteSimplicialCyclicContractionFaceReport, ...]
    retraction_defect_rank: int
    inclusion_chain_defect_rank: int
    projection_chain_defect_rank: int
    homotopy_defect_rank: int
    homotopy_square_rank: int
    homotopy_inclusion_rank: int
    projection_homotopy_rank: int
    cyclicity_defect_rank: int
    sdr_closed: bool
    side_conditions_closed: bool
    cyclic_closed: bool
    faces_compatible: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteTotalCechRanMaurerCartanGate:
    """Finite total Cech/Ran convolution Maurer-Cartan gate."""

    finite_bound: int
    total_dimension: int
    differential_square_matrix: Matrix
    theta_vector: Vector
    half_bracket_vector: Vector
    differential_after_theta: Vector
    maurer_cartan_defect_vector: Vector
    obstruction_vector: Vector
    primitive_vector: Vector
    obstruction_cocycle_vector: Vector
    primitive_boundary_vector: Vector
    primitive_defect_vector: Vector
    differential_square_defect_rank: int
    maurer_cartan_defect_rank: int
    obstruction_cocycle_defect_rank: int
    primitive_defect_rank: int
    primitive_data_supplied: bool
    differential_closed: bool
    maurer_cartan_closed: bool
    primitive_closes_obstruction: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class BarWitness:
    max_degree: int
    rank1_root_multiplicities: Dict[tuple, int]
    rank1_values_constant_24: bool
    rank1_values: List[int]
    bar_product_discriminants: Dict[int, int]
    status: str


@dataclass(frozen=True)
class FiniteBarLatticeGradingRow:
    """One supplied finite bar charge checked against the BKM lattice."""

    charge: str
    height: int
    coordinates: Vector
    norm: Fraction
    computed_discriminant: Fraction
    expected_discriminant: Fraction
    integral_coordinates: bool
    discriminant_match: bool


@dataclass(frozen=True)
class FiniteBarLatticeGradingReport:
    """Finite check that supplied bar charges are Lambda^{2,1}_{II}-graded."""

    height_cutoff: int
    simple_root_gram: Matrix
    rows: Tuple[FiniteBarLatticeGradingRow, ...]
    integrality_defects: Tuple[str, ...]
    discriminant_defects: Tuple[str, ...]
    transition_commutes: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteBarCERow:
    """One retained finite bar/CE comparison row."""

    charge: str
    height: int
    discriminant: int
    bar_euler_exponent: int
    bkm_exponent: int
    exponent_match: bool
    differential_commutes: bool


@dataclass(frozen=True)
class FiniteBarCEReport:
    """Finite ordered-bar to Chevalley-Eilenberg comparison report."""

    height_cutoff: int
    rows: Tuple[FiniteBarCERow, ...]
    exponent_defects: Tuple[str, ...]
    differential_defects: Tuple[str, ...]
    transition_commutes: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteBarCEChainMapGate:
    """Finite length-two bar/CE chain-map square."""

    height_cutoff: int
    source_degree1_dimension: int
    source_degree2_dimension: int
    target_degree1_dimension: int
    target_degree2_dimension: int
    source_differential_shape: Tuple[int, int]
    target_differential_shape: Tuple[int, int]
    comparison_degree1_shape: Tuple[int, int]
    comparison_degree2_shape: Tuple[int, int]
    comparison_after_bar_differential: Matrix
    ce_differential_after_comparison: Matrix
    chain_commutator_matrix: Matrix
    chain_commutator_defect_rank: int
    chain_map: bool
    status: str


@dataclass(frozen=True)
class FiniteBarRegularizationReport:
    """Exact finite Weyl-vector gate for the BKM/bar prefactor."""

    simple_root_gram: Matrix
    weyl_equation_rhs: Vector
    borcherds_weyl_vector: Vector
    supplied_bar_regularization_vector: Vector
    supplied_pairings: Vector
    pairing_defect: Vector
    vector_difference: Vector
    supplied_normalization: Fraction
    expected_normalization: Fraction
    weyl_vector_matches: bool
    normalization_matches: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class RademacherWitness:
    max_n: int
    growth_ok: bool
    leading_term_D3: float
    leading_term_D4: float
    finite_height_certificate: "RademacherFiniteHeightCertificate"
    status: str


@dataclass(frozen=True)
class RademacherFiniteHeightRow:
    """One rank-one Jacobi/Rademacher finite-height certificate row."""

    discriminant: int
    exact_abs_coefficient: int
    max_conductor: int
    partial_sum: float
    residual_abs: float
    residual_rel: float
    leading_residual_rel: float
    conductor_to_arity: Tuple[Tuple[int, int], ...]


@dataclass(frozen=True)
class RademacherFiniteHeightCertificate:
    """Finite-height Rademacher packet on the rank-one Jacobi coefficient lane."""

    discriminants: Tuple[int, ...]
    max_conductor: int
    rows: Tuple[RademacherFiniteHeightRow, ...]
    max_residual_rel: float
    max_leading_residual_rel: float
    residual_improves_over_leading: bool
    conductor_projection_defects: Tuple[str, ...]
    transition_commutes: bool
    tolerance: float
    status: str


@dataclass(frozen=True)
class RademacherPolarBesselRow:
    """One supplied finite polar/Bessel row checked against the rank-one lane."""

    discriminant: int
    conductor: int
    supplied_polar_discriminant: int
    supplied_polar_coefficient: int
    supplied_multiplier: str
    supplied_bessel_order: Fraction
    supplied_arity: int
    supplied_signed_coefficient: int
    expected_signed_coefficient: int
    expected_absolute_coefficient: int
    bessel_argument: float
    bessel_value: float
    term_value: float
    polar_match: bool
    multiplier_match: bool
    bessel_order_match: bool
    arity_match: bool
    coefficient_match: bool


@dataclass(frozen=True)
class RademacherPolarBesselGateReport:
    """Exact finite gate for supplied rank-one polar/Bessel Rademacher rows."""

    discriminants: Tuple[int, ...]
    max_conductor: int
    rows: Tuple[RademacherPolarBesselRow, ...]
    missing_rows: Tuple[str, ...]
    polar_defects: Tuple[str, ...]
    multiplier_defects: Tuple[str, ...]
    bessel_order_defects: Tuple[str, ...]
    arity_defects: Tuple[str, ...]
    coefficient_defects: Tuple[str, ...]
    transition_commutes: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class RademacherTruncationErrorRow:
    """One finite residual bound row for the rank-one Rademacher lane."""

    discriminant: int
    conductor: int
    arity: int
    exact_absolute_coefficient: int
    partial_sum: float
    residual_abs: float
    residual_rel: float
    supplied_abs_bound: Optional[float]
    supplied_rel_bound: Optional[float]
    abs_bound_valid: bool
    rel_bound_valid: bool


@dataclass(frozen=True)
class RademacherTruncationErrorGateReport:
    """Finite gate for supplied Rademacher truncation-error majorants."""

    discriminants: Tuple[int, ...]
    max_conductor: int
    rows: Tuple[RademacherTruncationErrorRow, ...]
    missing_abs_bounds: Tuple[str, ...]
    missing_rel_bounds: Tuple[str, ...]
    abs_bound_defects: Tuple[str, ...]
    rel_bound_defects: Tuple[str, ...]
    max_terminal_residual_rel: float
    tolerance: float
    terminal_tolerance_met: bool
    transition_commutes: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class BRSTWitness:
    lattice_central_charge: int
    transverse_central_charge: int
    ghost_central_charge: int
    total_central_charge: int
    central_charge_balanced: bool
    coefficient_fixture: "BRSTCoefficientFixture"
    target_template: str
    status: str


@dataclass(frozen=True)
class BRSTCentralChargeGateReport:
    """Finite central-charge anomaly gate for the BRST template."""

    lattice_central_charge: Fraction
    transverse_central_charge: Fraction
    ghost_central_charge: Fraction
    expected_total_central_charge: Fraction
    required_transverse_central_charge: Fraction
    total_central_charge: Fraction
    total_defect: Fraction
    transverse_defect: Fraction
    anomaly_cancelled: bool
    transverse_matches_requirement: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class BRSTCoefficientFixtureRow:
    """One finite discriminant row in the transverse BRST coefficient fixture."""

    discriminant: int
    signed_coefficient: int
    bosonic_dimension: int
    fermionic_dimension: int
    ordinary_dimension: int
    superdimension: int
    parity: str
    supertrace_matches: bool


@dataclass(frozen=True)
class BRSTCoefficientFixture:
    """Minimal finite super-vector-space fixture for the transverse character."""

    max_discriminant: int
    rows: Tuple[BRSTCoefficientFixtureRow, ...]
    support: Tuple[int, ...]
    total_bosonic_dimension: int
    total_fermionic_dimension: int
    total_ordinary_dimension: int
    total_superdimension: int
    all_supertraces_match: bool
    status: str


@dataclass(frozen=True)
class BRSTCoefficientFixtureTransition:
    """Height restriction check for finite BRST coefficient fixtures."""

    upper_discriminant: int
    lower_discriminant: int
    retained_support: Tuple[int, ...]
    defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class BRSTNoGhostSpectralRow:
    """One finite discriminant row in the no-ghost spectral-sequence gate."""

    discriminant: int
    target_coefficient: Fraction
    transverse_supertrace: Fraction
    longitudinal_supertrace: Fraction
    ghost_supertrace: Fraction
    cancellation_defect: Fraction
    coefficient_defect: Fraction
    cancellation_ok: bool
    coefficient_ok: bool


@dataclass(frozen=True)
class BRSTNoGhostSpectralSequenceGate:
    """Finite no-ghost spectral-sequence collapse gate."""

    rows: Tuple[BRSTNoGhostSpectralRow, ...]
    missing_rows: Tuple[str, ...]
    cancellation_defects: Tuple[str, ...]
    coefficient_defects: Tuple[str, ...]
    higher_differential_shapes: Tuple[Tuple[int, int], ...]
    higher_differential_ranks: Tuple[int, ...]
    higher_differential_defects: Tuple[str, ...]
    no_ghost_cancellation: bool
    transverse_coefficients_match: bool
    spectral_sequence_collapses: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class BRSTBorcherdsBracketRow:
    """One retained finite BRST/Borcherds bracket coefficient."""

    left_label: str
    right_label: str
    output_label: str
    brst_coefficient: Fraction
    borcherds_coefficient: Fraction
    coefficient_match: bool


@dataclass(frozen=True)
class BRSTBorcherdsBracketGate:
    """Finite comparison between supplied BRST and Borcherds brackets."""

    finite_bound: int
    root_labels: Tuple[str, ...]
    rows: Tuple[BRSTBorcherdsBracketRow, ...]
    coefficient_defects: Tuple[str, ...]
    support_defects: Tuple[str, ...]
    super_skew_defects: Tuple[str, ...]
    super_jacobi_defects: Tuple[str, ...]
    coefficient_match: bool
    support_respected: bool
    super_skew: bool
    super_jacobi: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class BRSTBorcherdsSerreRelationRow:
    """One retained finite Borcherds-Serre relation word."""

    relation_type: str
    left_label: str
    right_label: str
    exponent: int
    output_coefficients: Tuple[Tuple[str, Fraction], ...]
    vanished: bool


@dataclass(frozen=True)
class BRSTBorcherdsSerreRelationGate:
    """Finite relation check for supplied BRST/Borcherds brackets."""

    finite_bound: int
    root_labels: Tuple[str, ...]
    real_serre_rows: Tuple[BRSTBorcherdsSerreRelationRow, ...]
    imaginary_supercommutativity_rows: Tuple[BRSTBorcherdsSerreRelationRow, ...]
    real_serre_defects: Tuple[str, ...]
    imaginary_supercommutativity_defects: Tuple[str, ...]
    real_serre_relations: bool
    imaginary_supercommutativity: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class BRSTMomentumHeightProjectionRow:
    """One finite BRST differential checked against momentum and height."""

    degree: int
    source_dimension: int
    target_dimension: int
    differential_shape: Tuple[int, int]
    lower_differential_shape: Tuple[int, int]
    retained_source_count: int
    killed_source_count: int
    retained_target_count: int
    killed_target_count: int
    momentum_defect_entries: Tuple[str, ...]
    retained_to_killed_rank: int
    killed_to_retained_rank: int


@dataclass(frozen=True)
class BRSTMomentumHeightProjectionGate:
    """Finite gate for BRST momentum preservation and height projection."""

    upper_height: int
    lower_height: int
    degrees: Tuple[int, ...]
    rows: Tuple[BRSTMomentumHeightProjectionRow, ...]
    upper_square_ranks: Tuple[Tuple[str, int], ...]
    lower_square_ranks: Tuple[Tuple[str, int], ...]
    momentum_defects: Tuple[str, ...]
    subcomplex_defects: Tuple[str, ...]
    quotient_defects: Tuple[str, ...]
    upper_square_defects: Tuple[str, ...]
    lower_square_defects: Tuple[str, ...]
    momentum_preserved: bool
    retained_is_subcomplex: bool
    killed_is_subcomplex: bool
    upper_is_complex: bool
    lower_is_complex: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class YangianWitness:
    max_discriminant: int
    current_template: str
    epsilon_limit: int
    weight_template: str
    sample_multiplicities: Dict[int, int]
    current_packet: "YangianCurrentCandidatePacket"
    spectral_kernel_packet: "YangianSpectralKernelLabelPacket"
    self_ope_pole_packet: "YangianSelfOPEPoleLayerPacket"
    spectral_associator_obstruction: "YangianSpectralAssociatorObstructionPacket"
    current_limit_weight_one: bool
    status: str


@dataclass(frozen=True)
class YangianCurrentCandidateRow:
    """One finite discriminant row in the Yangian current-candidate packet."""

    discriminant: int
    signed_coefficient: int
    multiplicity: int
    parity: str
    undeformed_weight: int
    deformed_weight_epsilon1: int
    modes: Tuple[int, ...]
    finite_dimension: int
    superdimension: int
    weight_one_at_epsilon1: bool


@dataclass(frozen=True)
class YangianCurrentCandidatePacket:
    """Finite discriminant and finite mode window for current candidates."""

    max_discriminant: int
    max_mode: int
    rows: Tuple[YangianCurrentCandidateRow, ...]
    support: Tuple[int, ...]
    total_dimension: int
    total_superdimension: int
    all_weight_one_at_epsilon1: bool
    status: str


@dataclass(frozen=True)
class YangianCurrentPacketTransition:
    """Two-axis truncation check for finite Yangian current-candidate packets."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    retained_support: Tuple[int, ...]
    retained_modes: Tuple[int, ...]
    defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class YangianSpectralKernelLabelRow:
    """One finite positive/negative-dual label row for the spectral kernel."""

    discriminant: int
    signed_coefficient: int
    parity: str
    parity_sign: int
    current_labels: int
    dual_labels: int
    tensor_monomials: int
    row_superdimension: int
    mode_count: int


@dataclass(frozen=True)
class YangianSpectralKernelLabelPacket:
    """Finite non-Cartan label packet for the formal spectral current kernel."""

    max_discriminant: int
    max_mode: int
    cartan_label_count: int
    rows: Tuple[YangianSpectralKernelLabelRow, ...]
    support: Tuple[int, ...]
    positive_label_count: int
    negative_label_count: int
    noncartan_kernel_labels: int
    tensor_monomials: int
    total_kernel_labels_with_cartan: int
    transition_ready: bool
    status: str


@dataclass(frozen=True)
class YangianSpectralKernelTransition:
    """Two-axis truncation check for finite spectral kernel label packets."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    upper_cartan_label_count: int
    lower_cartan_label_count: int
    retained_discriminants: Tuple[int, ...]
    defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class YangianSelfOPEPoleLayerRow:
    """One finite self-OPE pole-layer row for a retained discriminant."""

    discriminant: int
    signed_coefficient: int
    exponent: int
    singularity_type: str
    pole_order: int
    current_multiplicity: int
    mode_count: int
    ordered_pair_dimension: int
    pole_layer_dimension: int
    pole_layer_superdimension: int
    target_discriminant: int
    target_signed_coefficient: int


@dataclass(frozen=True)
class YangianSelfOPEPoleLayerPacket:
    """Finite formal self-OPE pole-layer packet from P(D,1)=D(D-4)."""

    max_discriminant: int
    max_mode: int
    rows: Tuple[YangianSelfOPEPoleLayerRow, ...]
    pole_discriminants: Tuple[int, ...]
    marginal_discriminants: Tuple[int, ...]
    regular_discriminants: Tuple[int, ...]
    total_pole_layers: int
    total_pole_layer_dimension: int
    transition_ready: bool
    status: str


@dataclass(frozen=True)
class YangianSelfOPEPoleTransition:
    """Two-axis truncation check for formal self-OPE pole-layer packets."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    retained_discriminants: Tuple[int, ...]
    defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class YangianSpectralAssociatorObstructionPacket:
    """Finite spectral H^3 obstruction packet for the Yangian current route."""

    max_discriminant: int
    max_mode: int
    current_dimension: int
    current_support: Tuple[int, ...]
    cochain_dimension: int
    associator_cochain: Vector
    pentagon_differential: Matrix
    gauge_coboundary_basis: Matrix
    gauge_constraint_matrix: Matrix
    associator_boundary: Vector
    gauge_cocycle_matrix: Matrix
    gauge_constraint_product: Matrix
    pentagon_equation_count: int
    gauge_generator_count: int
    gauge_constraint_count: int
    cocycle_defect_rank: int
    gauge_cocycle_defect_rank: int
    gauge_constraint_defect_rank: int
    strictification_defect: int
    quasi_factorization_criterion_satisfied: bool
    strict_r_matrix_criterion_satisfied: bool
    missing_inputs: Tuple[str, ...]
    status: str


@dataclass(frozen=True)
class YangianSpectralAssociatorTransition:
    """Finite heightwise compatibility check for spectral obstruction packets."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    upper: YangianSpectralAssociatorObstructionPacket
    lower: YangianSpectralAssociatorObstructionPacket
    cochain_projection_shape: Tuple[int, int]
    boundary_projection_shape: Tuple[int, int]
    projected_associator: Vector
    associator_projection_difference: Vector
    lower_after_projection: Matrix
    projection_after_upper: Matrix
    pentagon_commutator_matrix: Matrix
    projected_gauge_rows: Matrix
    gauge_projection_failures: Tuple[str, ...]
    associator_projection_defect: int
    pentagon_commutator_defect: int
    gauge_projection_defect: int
    upper_quasi_factorization: bool
    lower_quasi_factorization: bool
    defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class YangianOPESerreIdealSpanGate:
    """Finite row-span equality gate for OPE and Borcherds-Serre relations."""

    finite_bound: int
    max_mode: int
    ambient_dimension: int
    ope_relation_count: int
    serre_relation_count: int
    ope_relation_rank: int
    serre_relation_rank: int
    combined_relation_rank: int
    ope_rows_missing_from_serre_span: Tuple[int, ...]
    serre_rows_missing_from_ope_span: Tuple[int, ...]
    ope_span_contains_serre: bool
    serre_span_contains_ope: bool
    spans_equal: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class YangianPBWAssociatedGradedGate:
    """Finite PBW associated-graded isomorphism gate for Yangian windows."""

    finite_bound: int
    max_mode: int
    block_count: int
    source_hilbert_vector: Tuple[int, ...]
    target_hilbert_vector: Tuple[int, ...]
    source_total_dimension: int
    target_total_dimension: int
    hilbert_vector_difference: Tuple[int, ...]
    hilbert_vector_defect_rank: int
    block_ranks: Tuple[int, ...]
    block_surjectivity_defects: Tuple[int, ...]
    block_kernel_excess_dimensions: Tuple[int, ...]
    defective_blocks: Tuple[int, ...]
    hilbert_vectors_equal: bool
    associated_graded_surjective: bool
    associated_graded_isomorphism: bool
    finite_filtered_isomorphism: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class YangianSpectralRMatrixEquationGate:
    """Finite Yang-Baxter and unitarity equation gate for supplied R-data."""

    finite_bound: int
    max_mode: int
    matrix_dimension: int
    ybe_left: Matrix
    ybe_right: Matrix
    ybe_difference: Matrix
    unitarity_product: Matrix
    identity_matrix: Matrix
    unitarity_difference: Matrix
    ybe_defect_rank: int
    unitarity_defect_rank: int
    yang_baxter_satisfied: bool
    unitarity_satisfied: bool
    strict_r_matrix_equations_satisfied: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class YangianLabelTowerTransition:
    """Combined transition check for the finite Yangian label tower."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    current: YangianCurrentPacketTransition
    spectral_kernel: YangianSpectralKernelTransition
    self_ope_pole: YangianSelfOPEPoleTransition
    retained_discriminants: Tuple[int, ...]
    retained_modes: Tuple[int, ...]
    component_statuses: Dict[str, str]
    component_defects: Dict[str, Tuple[str, ...]]
    component_gates: Dict[str, bool]
    component_size_data: Dict[str, Dict[str, int]]
    defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class YangianResidueTransition:
    """Finite transition check for supplied vertex-operator residue maps."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    upper_vertex_dimension: int
    lower_vertex_dimension: int
    upper_current_dimension: int
    lower_current_dimension: int
    source_projection_shape: Tuple[int, int]
    target_projection_shape: Tuple[int, int]
    upper_residue_shape: Tuple[int, int]
    lower_residue_shape: Tuple[int, int]
    target_after_upper_residue: Matrix
    lower_residue_after_source: Matrix
    commutator_matrix: Matrix
    commutator_defect_rank: int
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class YangianBRSTResidueChainGate:
    """Finite chain-map gate for supplied Yangian residue operators."""

    max_discriminant: int
    max_mode: int
    degree0_dimension: int
    degree1_dimension: int
    degree2_dimension: int
    q0_shape: Tuple[int, int]
    q1_shape: Tuple[int, int]
    residue_degree0_shape: Tuple[int, int]
    residue_degree1_shape: Tuple[int, int]
    residue_degree2_shape: Tuple[int, int]
    brst_square: Matrix
    residue1_after_q0: Matrix
    q0_after_residue0: Matrix
    boundary_commutator_matrix: Matrix
    residue2_after_q1: Matrix
    q1_after_residue1: Matrix
    cycle_commutator_matrix: Matrix
    brst_square_defect_rank: int
    boundary_commutator_defect_rank: int
    cycle_commutator_defect_rank: int
    brst_complex: bool
    residue_commutes_with_brst: bool
    descends_to_h1: bool
    status: str


@dataclass(frozen=True)
class YangianOPECoefficientTransition:
    """Finite transition check for supplied OPE coefficient tensors."""

    upper_discriminant: int
    lower_discriminant: int
    upper_mode: int
    lower_mode: int
    upper_entry_count: int
    lower_entry_count: int
    projected_entry_count: int
    discarded_entry_count: int
    projected_coefficients: Dict[Tuple[str, str, str], Fraction]
    lower_coefficients_normalized: Dict[Tuple[str, str, str], Fraction]
    missing_projection_labels: Tuple[str, ...]
    noninjective_projection_labels: Tuple[str, ...]
    support_defects: Tuple[str, ...]
    coefficient_defects: Tuple[str, ...]
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class FiniteBridgeTransitionSquare:
    """Finite commutative-square check for one supplied bridge map."""

    bridge: str
    upper_height: int
    lower_height: int
    upper_map_shape: Tuple[int, int]
    lower_map_shape: Tuple[int, int]
    source_transition_shape: Tuple[int, int]
    target_transition_shape: Tuple[int, int]
    target_after_upper_map: Matrix
    lower_map_after_source: Matrix
    commutator_matrix: Matrix
    commutator_defect_rank: int
    transition_commutes: bool
    status: str


@dataclass(frozen=True)
class FiniteBridgeSystemTransitionReport:
    """Aggregate transition check for the five supplied bridge maps."""

    upper_height: int
    lower_height: int
    required_bridges: Tuple[str, ...]
    present_bridges: Tuple[str, ...]
    missing_bridges: Tuple[str, ...]
    defective_bridges: Tuple[str, ...]
    component_statuses: Dict[str, str]
    component_gates: Dict[str, bool]
    component_defect_ranks: Dict[str, int]
    component_square_data: Dict[str, Dict[str, Any]]
    all_squares_commute: bool
    status: str


@dataclass(frozen=True)
class FiniteBridgeExactnessStepReport:
    """Finite Mittag-Leffler exactness check for one bridge square."""

    bridge: str
    upper_height: int
    lower_height: int
    square: FiniteBridgeTransitionSquare
    upper_comparison_map: Matrix
    lower_comparison_map: Matrix
    source_transition_matrix: Matrix
    target_transition_matrix: Matrix
    upper_kernel_basis: Matrix
    lower_kernel_basis: Matrix
    kernel_image_vectors: Matrix
    kernel_landing_vectors: Matrix
    target_upper_image: Matrix
    image_span_matrix: Matrix
    cokernel_span_matrix: Matrix
    lower_source_dimension: int
    lower_target_dimension: int
    lower_image_rank: int
    lower_cokernel_dimension: int
    source_transition_rank: int
    target_transition_rank: int
    upper_kernel_dimension: int
    lower_kernel_dimension: int
    kernel_landing_defect_rank: int
    image_landing_defect_rank: int
    kernel_image_rank: int
    image_transition_rank: int
    cokernel_transition_rank: int
    source_surjectivity_defect: int
    target_surjectivity_defect: int
    kernel_surjectivity_defect: int
    image_surjectivity_defect: int
    cokernel_surjectivity_defect: int
    source_transition_surjective: bool
    target_transition_surjective: bool
    kernel_transition_well_defined: bool
    image_transition_well_defined: bool
    cokernel_transition_well_defined: bool
    kernel_transition_surjective: bool
    image_transition_surjective: bool
    cokernel_transition_surjective: bool
    defects: Tuple[str, ...]
    ml_exactness_gate: bool
    status: str


@dataclass(frozen=True)
class FiniteBridgeSystemExactnessReport:
    """Aggregate Mittag-Leffler exactness check for the five bridge maps."""

    upper_height: int
    lower_height: int
    required_bridges: Tuple[str, ...]
    present_bridges: Tuple[str, ...]
    missing_bridges: Tuple[str, ...]
    defective_bridges: Tuple[str, ...]
    component_statuses: Dict[str, str]
    component_defects: Dict[str, Tuple[str, ...]]
    component_gates: Dict[str, Dict[str, bool]]
    component_rank_data: Dict[str, Dict[str, int]]
    component_exactness_data: Dict[str, Dict[str, Any]]
    all_components_ml_exact: bool
    status: str


@dataclass(frozen=True)
class FiniteBridgeExactnessTowerReport:
    """Finite tower propagation of one bridge Mittag-Leffler gate."""

    bridge: str
    upper_height: int
    lower_height: int
    step_heights: Tuple[Tuple[int, int], ...]
    step_count: int
    step_reports: Tuple[FiniteBridgeExactnessStepReport, ...]
    composed_source_transition: Matrix
    composed_target_transition: Matrix
    composed_step_report: FiniteBridgeExactnessStepReport
    step_defects: Dict[str, Tuple[str, ...]]
    all_steps_ml_exact: bool
    tower_ml_exact: bool
    status: str


@dataclass(frozen=True)
class BridgeWitnessSplit:
    """Low-height witnessed finite data on scattering, bar, and Rademacher lanes."""

    scattering: ScatteringWitness
    bar: BarWitness
    rademacher: RademacherWitness


@dataclass(frozen=True)
class BridgeOperatorBoundarySplit:
    """Finite BRST/Yangian boundary packets with operator constructions still open."""

    brst: BRSTWitness
    yangian: YangianWitness


BridgeFormalTemplateSplit = BridgeOperatorBoundarySplit


@dataclass(frozen=True)
class BridgeMissingTheorems:
    """Missing theorem statements for each comparison bridge."""

    scattering: List[str]
    bar: List[str]
    rademacher: List[str]
    brst: List[str]
    yangian: List[str]

    @property
    def entries(self) -> Tuple[List[str], ...]:
        return (self.scattering, self.bar, self.rademacher, self.brst, self.yangian)

    @property
    def empty(self) -> bool:
        return all(not entry for entry in self.entries)


@dataclass(frozen=True)
class BridgeProofObligationEntry:
    """Typed proof-obligation entry for one bridge."""

    witness: Any
    finite_boundary_results: List[str]
    missing: List[str]
    target: str
    status: str

    @property
    def proved(self) -> bool:
        return self.status == "proved"


@dataclass(frozen=True)
class BridgeObstructionRecord:
    """Machine-readable split between finite data and missing theorem input."""

    witnessed: BridgeWitnessSplit
    operator_boundary: BridgeOperatorBoundarySplit
    missing_theorems: BridgeMissingTheorems
    finite_boundary_results: Dict[str, List[str]]
    uniform_gap: str

    @property
    def formal_templates(self) -> BridgeOperatorBoundarySplit:
        """Backward-compatible name for the operator-boundary split."""
        return self.operator_boundary


@dataclass(frozen=True)
class BridgeProofObligationMatrix:
    """Bridge-by-bridge proof obligations with witnessed and missing pieces."""

    scattering: BridgeProofObligationEntry
    bar: BridgeProofObligationEntry
    rademacher: BridgeProofObligationEntry
    brst: BridgeProofObligationEntry
    yangian: BridgeProofObligationEntry

    @property
    def entries(self) -> Tuple[BridgeProofObligationEntry, ...]:
        return (self.scattering, self.bar, self.rademacher, self.brst, self.yangian)

    @property
    def all_entries_proved(self) -> bool:
        return all(entry.proved for entry in self.entries)


@dataclass(frozen=True)
class SourceRecognitionRecord:
    """Source-side Hall/Borcherds recognition status at finite height."""

    gate: "GateReport"
    envelope: "RecognitionEnvelopeReport"
    obligation_matrix: "SourceGateObligationMatrix"
    task_map: "SourceGateTaskMap"
    boundary_report: "SourceGateBoundaryReport"
    missing_gate_witnesses: List[str]
    missing_envelope_defects: List[str]
    source_matrix_forces_faithfulness: bool


@dataclass(frozen=True)
class K3EBridgeAuditReport:
    """Combined audit of witnesses, source recognition, and comparison gaps."""

    finite_witness: FiniteBridgeWitness
    obstruction_record: BridgeObstructionRecord
    proof_matrix: BridgeProofObligationMatrix
    source_recognition: SourceRecognitionRecord
    summary: str


@dataclass(frozen=True)
class K3ECoreGapReport:
    """Top-level report of the seven core missing constructions."""

    audit: K3EBridgeAuditReport
    entries: List["K3ECoreGapEntry"]
    summary: str

    @property
    def core_gaps(self) -> Dict[str, "K3ECoreGapEntry"]:
        return {entry.gap: entry for entry in self.entries}


@dataclass(frozen=True)
class K3ECoreGapEntry:
    """Typed entry for one of the seven core missing constructions."""

    gap: str
    evidence: K3EGapEvidenceEntry
    status: K3EGapStatusRow
    missing: List[str]
    tasks: List[str]


@dataclass(frozen=True)
class K3EProofDependencyGraph:
    """Directed dependency graph for the missing K3 x E constructions."""

    nodes: List[str]
    edges: List[tuple]
    entries: List["K3EProofDependencyEntry"]
    topological_order: List[str]
    summary: str

    @property
    def prerequisites(self) -> Dict[str, "K3EProofDependencyEntry"]:
        return {entry.node: entry for entry in self.entries}


@dataclass(frozen=True)
class K3EInverseLimitGateRequirement:
    """Required obstruction package for passing finite bridges to the limit."""

    owner: str
    component_scope: Tuple[str, ...]
    heightwise_maps_realized: bool
    rank_zero_transition_squares: bool
    source_transition_surjective: bool
    target_transition_surjective: bool
    kernel_transition_well_defined: bool
    kernel_transition_surjective: bool
    image_transition_well_defined: bool
    image_transition_surjective: bool
    cokernel_transition_well_defined: bool
    cokernel_transition_surjective: bool
    proved_conditions: Tuple[str, ...] = ()

    @property
    def all_required(self) -> bool:
        return all((
            self.heightwise_maps_realized,
            self.rank_zero_transition_squares,
            self.source_transition_surjective,
            self.target_transition_surjective,
            self.kernel_transition_well_defined,
            self.kernel_transition_surjective,
            self.image_transition_well_defined,
            self.image_transition_surjective,
            self.cokernel_transition_well_defined,
            self.cokernel_transition_surjective,
        ))

    @property
    def required_conditions(self) -> Tuple[str, ...]:
        conditions: List[str] = []
        if self.heightwise_maps_realized:
            conditions.append("all heightwise comparison maps are realized")
        if self.rank_zero_transition_squares:
            conditions.append("every transition square has rank-zero commutator")
        if self.source_transition_surjective:
            conditions.append("source transition maps are surjective")
        if self.target_transition_surjective:
            conditions.append("target transition maps are surjective")
        if self.kernel_transition_well_defined:
            conditions.append("upper kernels land inside lower kernels")
        if self.kernel_transition_surjective:
            conditions.append("kernel transition maps are surjective")
        if self.image_transition_well_defined:
            conditions.append("upper images land inside lower images")
        if self.image_transition_surjective:
            conditions.append("image transition maps are surjective")
        if self.cokernel_transition_well_defined:
            conditions.append("cokernel transition maps are induced")
        if self.cokernel_transition_surjective:
            conditions.append("cokernel transition maps are surjective")
        return tuple(conditions)

    @property
    def open_conditions(self) -> Tuple[str, ...]:
        proved = set(self.proved_conditions)
        return tuple(condition for condition in self.required_conditions if condition not in proved)

    @property
    def all_proved(self) -> bool:
        return self.all_required and not self.open_conditions

    @property
    def status(self) -> str:
        return "PROVED" if self.all_proved else "OPEN_REQUIREMENT"


@dataclass(frozen=True)
class K3EProRecognitionGateRequirement:
    """Pro/automorphic gates beyond componentwise finite exactness."""

    owner: str
    separated_completion: bool
    defect_ideal_exactness: bool
    heegner_borcherds_coefficient_comparison: bool
    proved_conditions: Tuple[str, ...] = ()

    @property
    def all_required(self) -> bool:
        return all((
            self.separated_completion,
            self.defect_ideal_exactness,
            self.heegner_borcherds_coefficient_comparison,
        ))

    @property
    def required_conditions(self) -> Tuple[str, ...]:
        conditions: List[str] = []
        if self.separated_completion:
            conditions.append(
                "Q_H^sep: finite recognition quotients are separated and complete in the pro-cone topology"
            )
        if self.defect_ideal_exactness:
            conditions.append(
                "L_H^ex: defect ideals commute with height transitions and have exact inverse limit"
            )
        if self.heegner_borcherds_coefficient_comparison:
            conditions.append(
                "H_H^HB: Heegner/Borcherds coefficients agree with the finite denominator exponents heightwise"
            )
        return tuple(conditions)

    @property
    def open_conditions(self) -> Tuple[str, ...]:
        proved = set(self.proved_conditions)
        return tuple(condition for condition in self.required_conditions if condition not in proved)

    @property
    def all_proved(self) -> bool:
        return self.all_required and not self.open_conditions

    @property
    def status(self) -> str:
        return "PROVED" if self.all_proved else "OPEN_PRO_RECOGNITION_REQUIREMENT"


@dataclass(frozen=True)
class K3EClosureWitnesses:
    """Supplied proof evidence for the K3 x E bridge closure criterion.

    The booleans record theorem-level inputs.  The condition tuples name
    already-proved inverse-limit and pro-recognition hypotheses; they must
    match the canonical strings in the corresponding gate reports.
    """

    source_gate_closed: bool = False
    source_recognition_envelope_completed: bool = False
    bridge_constructions: Tuple[str, ...] = ()
    inverse_limit_proved_conditions: Tuple[str, ...] = ()
    pro_recognition_proved_conditions: Tuple[str, ...] = ()

    @property
    def bridge_construction_set(self) -> frozenset[str]:
        return frozenset(self.bridge_constructions)

    @property
    def all_bridge_constructions_closed(self) -> bool:
        return all(bridge in self.bridge_construction_set for bridge in K3E_CLOSURE_BRIDGES)


@dataclass(frozen=True)
class K3EBridgeConstructionRequirement:
    """Structured construction boundary for one open K3 x E bridge."""

    bridge: str
    finite_symbol: str
    source_object: str
    target_object: str
    construction_obligations: Tuple[str, ...]
    compatibility_obligations: Tuple[str, ...]
    existing_finite_witnesses: Tuple[str, ...]
    forbidden_promotions: Tuple[str, ...]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    status: str = "open"

    @property
    def all_obligations(self) -> Tuple[str, ...]:
        return self.construction_obligations + self.compatibility_obligations

    @property
    def open_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.open_conditions

    @property
    def proved_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.proved_conditions

    @property
    def inverse_limit_status(self) -> str:
        return self.inverse_limit_gate.status


@dataclass(frozen=True)
class K3EClosureCriterionReport:
    """Criterion for closing the K3 x E bridge construction."""

    audit: K3EBridgeAuditReport
    dependency_graph: K3EProofDependencyGraph
    required_conditions: List[str]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    pro_recognition_gate: K3EProRecognitionGateRequirement
    construction_requirements: Tuple[K3EBridgeConstructionRequirement, ...]
    closed: bool
    summary: str

    @property
    def open_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.open_conditions

    @property
    def proved_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.proved_conditions

    @property
    def inverse_limit_status(self) -> str:
        return self.inverse_limit_gate.status

    @property
    def open_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.open_conditions

    @property
    def proved_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.proved_conditions

    @property
    def pro_recognition_status(self) -> str:
        return self.pro_recognition_gate.status


@dataclass(frozen=True)
class K3EGapEvidenceEntryEntry:
    """Typed evidence entry for one core gap."""

    gap: str
    evidence: K3EGapEvidenceEntry


@dataclass(frozen=True)
class K3EGapCrosswalkReport:
    """Crosswalk from core gaps to current chapter/test evidence."""

    core_gap_report: K3ECoreGapReport
    entries: List[K3EGapEvidenceEntryEntry]
    summary: str

    @property
    def evidence_by_gap(self) -> Dict[str, "K3EGapEvidenceEntry"]:
        return {entry.gap: entry.evidence for entry in self.entries}


@dataclass(frozen=True)
class K3EGapEvidenceEntry:
    """Typed evidence bundle for one gap."""

    chapter: List[str]
    tests: List[str]


@dataclass(frozen=True)
class K3EGapStatusRow:
    """Four-way status split for a single gap."""

    established_boundary: List[str]
    finite_boundary_results: List[str]
    witnessed: List[str]
    formal: List[str]
    missing: List[str]
    status: str = "open"

    @property
    def proved(self) -> bool:
        return self.status == "proved"


@dataclass(frozen=True)
class K3EGapStatusEntry:
    """Typed status entry for one core gap."""

    gap: str
    row: K3EGapStatusRow


@dataclass(frozen=True)
class K3EGapStatusTable:
    """Status table for the seven core gaps."""

    entries: List[K3EGapStatusEntry]
    summary: str

    @property
    def rows(self) -> Dict[str, K3EGapStatusRow]:
        return {entry.gap: entry.row for entry in self.entries}


@dataclass(frozen=True)
class K3EProofRoadmapReport:
    """Roadmap from the current evidence to the missing theorem-level proofs."""

    audit: K3EBridgeAuditReport
    status_table: K3EGapStatusTable
    steps: List["K3EProofRoadmapStep"]
    task_map: "K3EProofTaskMap"
    inverse_limit_gate: K3EInverseLimitGateRequirement
    pro_recognition_gate: K3EProRecognitionGateRequirement
    construction_requirements: Tuple[K3EBridgeConstructionRequirement, ...]
    summary: str

    @property
    def open_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.open_conditions

    @property
    def proved_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.proved_conditions

    @property
    def inverse_limit_status(self) -> str:
        return self.inverse_limit_gate.status

    @property
    def open_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.open_conditions

    @property
    def proved_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.proved_conditions

    @property
    def pro_recognition_status(self) -> str:
        return self.pro_recognition_gate.status


@dataclass(frozen=True)
class K3EProofRoadmapStep:
    """Typed step in the proof roadmap."""

    name: str
    status: str
    current_evidence: K3EGapEvidenceEntry
    missing: List[str]
    proof_method: List[str]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    construction_requirement: K3EBridgeConstructionRequirement


@dataclass(frozen=True)
class K3EProofTaskMap:
    """Bridge-by-bridge task map with the missing technical ingredients."""

    entries: List["K3EProofTaskEntry"]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    pro_recognition_gate: K3EProRecognitionGateRequirement
    construction_requirements: Tuple[K3EBridgeConstructionRequirement, ...]
    summary: str

    @property
    def tasks(self) -> Dict[str, "K3EProofTaskEntry"]:
        return {entry.bridge: entry for entry in self.entries}

    @property
    def open_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.open_conditions

    @property
    def proved_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.proved_conditions

    @property
    def inverse_limit_status(self) -> str:
        return self.inverse_limit_gate.status

    @property
    def open_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.open_conditions

    @property
    def proved_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.proved_conditions

    @property
    def pro_recognition_status(self) -> str:
        return self.pro_recognition_gate.status

    @property
    def requirements(self) -> Dict[str, K3EBridgeConstructionRequirement]:
        return {entry.bridge: entry.construction_requirement for entry in self.entries}


@dataclass(frozen=True)
class K3EProofDependencyEntry:
    """Typed prerequisite list for one dependency-graph node."""

    node: str
    prerequisites: List[str]


@dataclass(frozen=True)
class K3EProofTaskEntry:
    """Typed task list for one open bridge."""

    bridge: str
    tasks: List[str]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    construction_requirement: K3EBridgeConstructionRequirement


@dataclass(frozen=True)
class K3EBridgeSpecification:
    """Theorem-specification object for the remaining bridge conjectures."""

    entries: List["K3EBridgeSpecificationEntry"]
    summary: str

    @property
    def bridges(self) -> Dict[str, "K3EBridgeSpecificationEntry"]:
        return {entry.bridge: entry for entry in self.entries}

    @property
    def open_entries(self) -> Dict[str, "K3EBridgeSpecificationEntry"]:
        return {
            entry.bridge: entry
            for entry in self.entries
            if entry.status == "OPEN_THEOREM_SCHEMA"
        }

    @property
    def all_entries_open(self) -> bool:
        return len(self.open_entries) == len(self.entries)

    @property
    def all_entries_proved(self) -> bool:
        return all(entry.proved_here for entry in self.entries)

    @property
    def open_schema_obligations(self) -> Tuple[str, ...]:
        obligations: List[str] = []
        for entry in self.entries:
            obligations.extend(entry.open_obligations)
        return tuple(obligations)


@dataclass(frozen=True)
class K3EBridgeSpecificationEntry:
    """Typed theorem schema for a single open bridge."""

    bridge: str
    hypotheses: List[str]
    conclusion: List[str]
    obstructions: List[str]
    construction_requirement: K3EBridgeConstructionRequirement
    summary: str
    status: str = "OPEN_THEOREM_SCHEMA"
    dependency_obligations: Tuple[str, ...] = ()
    local_obligations_satisfied: bool = False

    @property
    def proved_here(self) -> bool:
        return self.status == "PROVED_THEOREM_SCHEMA"

    @property
    def open_obligations(self) -> Tuple[str, ...]:
        if self.proved_here:
            return ()
        obligations: List[str] = []
        local_obligations_satisfied = (
            self.local_obligations_satisfied
            or self.construction_requirement.status == "proved"
        )
        if not local_obligations_satisfied:
            obligations.extend(
                f"establish theorem-schema hypothesis: {hypothesis}"
                for hypothesis in self.hypotheses
            )
        obligations.extend(self.dependency_obligations)
        obligations.extend(self.obstructions)
        if not local_obligations_satisfied:
            obligations.extend(self.construction_requirement.all_obligations)
        obligations.extend(self.construction_requirement.open_inverse_limit_conditions)
        return tuple(dict.fromkeys(obligations))


@dataclass(frozen=True)
class K3ESourceGateSpecification:
    """Theorem-specification object for the source Hall/Borcherds gate."""

    hypotheses: List[str]
    conclusion: List[str]
    obstructions: List[str]
    heightwise_compatibility: "K3EHeightwiseCompatibility"
    pro_recognition_gate: K3EProRecognitionGateRequirement
    construction_requirement: K3EBridgeConstructionRequirement
    summary: str
    status: str = "OPEN_THEOREM_SCHEMA"
    local_obligations_satisfied: bool = False

    @property
    def proved_here(self) -> bool:
        return self.status == "PROVED_THEOREM_SCHEMA"

    @property
    def open_obligations(self) -> Tuple[str, ...]:
        if self.proved_here:
            return ()
        obligations: List[str] = []
        local_obligations_satisfied = (
            self.local_obligations_satisfied
            or self.construction_requirement.status == "proved"
        )
        if not local_obligations_satisfied:
            obligations.extend(
                f"establish theorem-schema hypothesis: {hypothesis}"
                for hypothesis in self.hypotheses
            )
        obligations.extend(self.obstructions)
        if not local_obligations_satisfied:
            obligations.extend(self.heightwise_compatibility.transition_conditions)
            obligations.extend(self.heightwise_compatibility.inverse_limit_conditions)
            obligations.extend(
                self.heightwise_compatibility.inverse_limit_gate.open_conditions
            )
            obligations.extend(self.construction_requirement.all_obligations)
            obligations.extend(
                self.construction_requirement.open_inverse_limit_conditions
            )
        obligations.extend(self.pro_recognition_gate.open_conditions)
        return tuple(dict.fromkeys(obligations))


@dataclass(frozen=True)
class K3EHeightwiseCompatibility:
    """Typed source/target heightwise compatibility data for a bridge."""

    source_transition_map: str
    target_transition_map: str
    transition_conditions: List[str]
    inverse_limit_conditions: List[str]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    summary: str


@dataclass(frozen=True)
class K3EBridgeAxiomPack:
    """Explicit BD-axiom pack for the pro-bridge datum conjecture."""

    source_gate: K3ESourceGateSpecification
    entries: List["K3EBridgeAxiomEntry"]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    pro_recognition_gate: K3EProRecognitionGateRequirement
    construction_requirements: Tuple[K3EBridgeConstructionRequirement, ...]
    summary: str

    @property
    def bd_axioms(self) -> Dict[str, "K3EBridgeAxiomEntry"]:
        return {entry.label: entry for entry in self.entries}

    @property
    def open_entries(self) -> Dict[str, "K3EBridgeAxiomEntry"]:
        return {
            entry.label: entry
            for entry in self.entries
            if entry.status == "OPEN_THEOREM_SCHEMA"
        }

    @property
    def all_entries_open(self) -> bool:
        return (
            self.source_gate.status == "OPEN_THEOREM_SCHEMA"
            and len(self.open_entries) == len(self.entries)
        )

    @property
    def all_entries_proved(self) -> bool:
        return self.source_gate.proved_here and all(
            entry.proved_here for entry in self.entries
        )

    @property
    def open_schema_obligations(self) -> Tuple[str, ...]:
        obligations = list(self.source_gate.open_obligations)
        for entry in self.entries:
            obligations.extend(entry.open_obligations)
        return tuple(obligations)

    @property
    def requirements(self) -> Dict[str, K3EBridgeConstructionRequirement]:
        return {entry.bridge: entry.construction_requirement for entry in self.entries}

    @property
    def open_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.open_conditions

    @property
    def proved_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.proved_conditions

    @property
    def inverse_limit_status(self) -> str:
        return self.inverse_limit_gate.status

    @property
    def open_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.open_conditions

    @property
    def proved_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.proved_conditions

    @property
    def pro_recognition_status(self) -> str:
        return self.pro_recognition_gate.status


@dataclass(frozen=True)
class K3EBridgeAxiomEntry:
    """Typed BD axiom entry for a single labeled bridge."""

    label: str
    bridge: str
    hypotheses: List[str]
    conclusion: List[str]
    obstructions: List[str]
    heightwise_compatibility: K3EHeightwiseCompatibility
    construction_requirement: K3EBridgeConstructionRequirement
    status: str = "OPEN_THEOREM_SCHEMA"
    dependency_obligations: Tuple[str, ...] = ()
    local_obligations_satisfied: bool = False

    @property
    def proved_here(self) -> bool:
        return self.status == "PROVED_THEOREM_SCHEMA"

    @property
    def open_obligations(self) -> Tuple[str, ...]:
        if self.proved_here:
            return ()
        obligations: List[str] = []
        local_obligations_satisfied = (
            self.local_obligations_satisfied
            or self.construction_requirement.status == "proved"
        )
        if not local_obligations_satisfied:
            obligations.extend(
                f"establish theorem-schema hypothesis: {hypothesis}"
                for hypothesis in self.hypotheses
            )
        obligations.extend(self.dependency_obligations)
        obligations.extend(self.obstructions)
        if not local_obligations_satisfied:
            obligations.extend(self.heightwise_compatibility.transition_conditions)
            obligations.extend(self.heightwise_compatibility.inverse_limit_conditions)
            obligations.extend(
                self.heightwise_compatibility.inverse_limit_gate.open_conditions
            )
            obligations.extend(self.construction_requirement.all_obligations)
        elif self.construction_requirement.status != "proved":
            obligations.extend(self.heightwise_compatibility.transition_conditions)
            obligations.extend(self.heightwise_compatibility.inverse_limit_conditions)
            obligations.extend(
                self.heightwise_compatibility.inverse_limit_gate.open_conditions
            )
        obligations.extend(
            self.construction_requirement.open_inverse_limit_conditions
        )
        return tuple(dict.fromkeys(obligations))


@dataclass(frozen=True)
class K3ETheoremBoundaryReport:
    """Derived theorem boundary from all current witness and gap records."""

    source_conditions: List[str]
    comparison_conditions: List[str]
    inverse_limit_conditions: List[str]
    inverse_limit_gate: K3EInverseLimitGateRequirement
    pro_recognition_gate: K3EProRecognitionGateRequirement
    construction_requirements: Tuple[K3EBridgeConstructionRequirement, ...]
    all_conditions: List[str]
    summary: str

    @property
    def open_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.open_conditions

    @property
    def proved_inverse_limit_conditions(self) -> Tuple[str, ...]:
        return self.inverse_limit_gate.proved_conditions

    @property
    def inverse_limit_status(self) -> str:
        return self.inverse_limit_gate.status

    @property
    def open_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.open_conditions

    @property
    def proved_pro_recognition_conditions(self) -> Tuple[str, ...]:
        return self.pro_recognition_gate.proved_conditions

    @property
    def pro_recognition_status(self) -> str:
        return self.pro_recognition_gate.status


def k3e_inverse_limit_gate_requirement(
    owner: str = "k3e_bridge_chain",
    component_scope: Iterable[str] = REQUIRED_BRIDGE_COMPONENTS,
    proved_conditions: Iterable[str] = (),
) -> K3EInverseLimitGateRequirement:
    """Return the full finite-to-pro obstruction gate required by the bridge."""
    return K3EInverseLimitGateRequirement(
        owner=owner,
        component_scope=tuple(component_scope),
        heightwise_maps_realized=True,
        rank_zero_transition_squares=True,
        source_transition_surjective=True,
        target_transition_surjective=True,
        kernel_transition_well_defined=True,
        kernel_transition_surjective=True,
        image_transition_well_defined=True,
        image_transition_surjective=True,
        cokernel_transition_well_defined=True,
        cokernel_transition_surjective=True,
        proved_conditions=tuple(proved_conditions),
    )


def k3e_pro_recognition_gate_requirement(
    owner: str = "k3e_bridge_chain",
    proved_conditions: Iterable[str] = (),
) -> K3EProRecognitionGateRequirement:
    """Return the pro/automorphic recognition gates Q_H, L_H, and H_H."""
    return K3EProRecognitionGateRequirement(
        owner=owner,
        separated_completion=True,
        defect_ideal_exactness=True,
        heegner_borcherds_coefficient_comparison=True,
        proved_conditions=tuple(proved_conditions),
    )


def k3e_bridge_construction_requirement(bridge: str) -> K3EBridgeConstructionRequirement:
    """Return the structured open construction boundary for one bridge."""
    records: Dict[str, Dict[str, Tuple[str, ...] | str]] = {
        "source_hall_borcherds_gate": {
            "finite_symbol": r"D^{\mathrm{red},\leq H}_\hbar(K3\times E,\sigma)",
            "source_object": "oriented finite Rees Hall source and recognition envelope",
            "target_object": r"finite Serre--Borcherds current quotient Y^{\mathrm{SB},\leq H}_\hbar(\mathfrak g_{\Delta_5})",
            "construction_obligations": (
                "construct the oriented critical CoHA with negative half, Cartan, Hopf pairing, and coproduct",
                "prove source-recognition defect vanishing at each finite height",
                "identify the Borcherds Cartan radical and Serre kernel",
            ),
            "compatibility_obligations": (
                "make finite-height recognition functorial under Hall and target truncations",
                "prove compatibility with the pro-cone topology",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "compute/lib/hall_borcherds_gate.py",
                "Theorem~\\ref{thm:k3e-constructed-finite-double-recognition}",
            ),
            "forbidden_promotions": (
                "finite recognition envelope alone is not the unquotiented compact Hall double",
                "the scalar Borcherds denominator is not a compact Hall pairing or coproduct",
            ),
        },
        "framed_d3_assignment": {
            "finite_symbol": r"\Theta_{A,H}",
            "source_object": r"\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3\times E))",
            "target_object": r"A^{(\Sigma_2,C),\leq H}_{K3\times E}",
            "construction_obligations": (
                "construct a genuine stage-1 factorisation algebra on K3 x E",
                "prove the fixed (Sigma_2, C) specialisation under H1-H4",
                "identify the framed chiral output at finite height",
            ),
            "compatibility_obligations": (
                "commute with the height transition maps",
                "preserve the H1-H4 locus under restriction",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "Theorem~\\ref{thm:cy-to-chiral-d3}",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ),
            "forbidden_promotions": (
                "a candidate finite target packet is not a constructed stage-1 factorisation algebra",
            ),
        },
        "compact_hall_promotion": {
            "finite_symbol": r"\mathcal H^{\mathrm{comp},\leq H}_{K3\times E}",
            "source_object": "oriented Rees Hall windows",
            "target_object": "compact critical CoHA with Drinfeld-double data",
            "construction_obligations": (
                "complete the Rees Hall data to the compact Hall object",
                "construct the negative half, Cartan, Hopf pairing, and coproduct",
                "prove nondegeneracy modulo the Borcherds Cartan radical",
            ),
            "compatibility_obligations": (
                "identify the Serre kernel at finite height",
                "show compatibility with finite-double recognition and pro-cone completion",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "compute/lib/hall_borcherds_gate.py",
                "Corollary~\\ref{cor:k3e-finite-height-promotion-obstruction}",
            ),
            "forbidden_promotions": (
                "oriented finite Rees Hall layers are not compact critical CoHA",
                "finite source matrices do not by themselves prove compact promotion",
            ),
        },
        "scattering_root_identification": {
            "finite_symbol": r"\Xi_{\mathrm{scatt}}^{\leq H}",
            "source_object": r"\mathcal H^{\mathrm{comp},\leq H}_{K3\times E}",
            "target_object": r"\widehat{\mathbb C}[\Gamma]^{\leq H}",
            "construction_obligations": (
                "construct the motivic integration morphism from wall-crossing Hall data to the quantum torus",
                "prove the finite wall product equals the Borcherds denominator wall packet",
                "exclude extraneous walls and missing imaginary-root orbits",
            ),
            "compatibility_obligations": (
                "preserve initial walls, derived walls, parity, and chamber composition",
                "commute with source and target height truncations",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "finite_scattering_quantum_torus_gate",
                "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}",
                "finite_scattering_root_report",
                "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}",
            ),
            "forbidden_promotions": (
                "finite exponent equality is not the motivic integration natural transformation",
            ),
        },
        "bkm_bar_dictionary": {
            "finite_symbol": r"\Xi_{\mathrm{bar}}^{\leq H}",
            "source_object": r"B^{\mathrm{ord},\leq H}(A_{K3\times E}^{(\Sigma_2,C)})",
            "target_object": "finite Chevalley--Eilenberg / Euler-product target",
            "construction_obligations": (
                "construct a filtered morphism of ordered bar complexes",
                "prove the Lambda^{2,1}_{II} grading of the bar complex",
                "identify the alpha-primary Euler characteristic with the motivic DT index",
            ),
            "compatibility_obligations": (
                "commute with the bar differential and fixed (Sigma_2, C) specialisation",
                "match the Weyl vector and Borcherds multiplier-system normalisation",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "finite_bar_lattice_grading_report",
                "finite_bar_ce_chain_map_gate",
                "finite_bar_ce_report",
                "finite_bar_regularization_report",
                "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}",
                "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}",
                "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}",
                "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}",
            ),
            "forbidden_promotions": (
                "the bar Euler product is not the derived centre or bulk local-operator algebra",
            ),
        },
        "shadow_rademacher_comparison": {
            "finite_symbol": r"\Xi_{\mathrm{rad}}^{\leq H}",
            "source_object": r"\mathrm{Sh}_{\leq H}",
            "target_object": r"\mathcal R_{\leq H}",
            "construction_obligations": (
                "construct the protected compact-CY3 shadow-to-partition comparison map",
                "extend polar-data compatibility from the rank-one Jacobi lane to the compact shadow packet",
                "prove the compact Bessel recursion and uniform all-height truncation error theorem",
            ),
            "compatibility_obligations": (
                "preserve compact polar data and finite asymptotic class",
                "commute with height and conductor truncations",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "rademacher_polar_bessel_gate",
                "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}",
                "rademacher_truncation_error_gate",
                "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}",
                "rademacher_finite_height_certificate",
                "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}",
            ),
            "forbidden_promotions": (
                "the rank-one Jacobi certificate is not the compact-CY3 protected shadow theorem",
            ),
        },
        "brst_realization": {
            "finite_symbol": r"\Xi_{\mathrm{BRST}}^{\leq H}",
            "source_object": r"V_{\Lambda^{2,1}_{II}}\otimes V_{\mathrm{trans}}^{\leq H}\otimes V_{\mathrm{ghost}}",
            "target_object": r"H^1_{\mathrm{BRST}}(\cdot)",
            "construction_obligations": (
                "construct the worldsheet VOA and BRST differential",
                "prove Q_BRST squared is zero with the required transverse sector",
                "prove finite-height no-ghost convergence and root-multiplicity identification",
            ),
            "compatibility_obligations": (
                "realize the finite supertrace fixture in BRST cohomology with fixed ghost-number grading",
                "commute with the BRST differential and height transition maps",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "brst_central_charge_gate",
                "Proposition~\\ref{prop:k3e-brst-central-charge-gate}",
                "brst_coefficient_fixture",
                "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}",
                "brst_no_ghost_spectral_sequence_gate",
                "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}",
                "brst_borcherds_bracket_gate",
                "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}",
                "brst_borcherds_serre_relation_gate",
                "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}",
                "brst_momentum_height_projection_gate",
                "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}",
            ),
            "forbidden_promotions": (
                "the finite supertrace fixture is not a worldsheet VOA",
                "central-charge cancellation alone does not prove BRST cohomology",
            ),
        },
        "vertex_operator_yangian": {
            "finite_symbol": r"\Xi_{\mathrm{Yang}}^{\leq H}",
            "source_object": r"V_\varepsilon^{\leq H}(\alpha,z)",
            "target_object": r"\operatorname{Res}_{z=u}V_\varepsilon^{\leq H}(\alpha,z)",
            "construction_obligations": (
                "construct the Omega-deformed vertex operators to all orders at epsilon = 1",
                "show residues are genuine BRST cohomology operators",
                "derive the finite OPE coefficients, Serre quotient, coproduct, and Hall-Borcherds R-matrix comparison",
            ),
            "compatibility_obligations": (
                "commute with OPE, residue, and height truncation",
                "annihilate the spectral associator obstruction for a strict R-matrix statement",
                "satisfy the full inverse-limit exactness gate",
            ),
            "existing_finite_witnesses": (
                "yangian_current_candidate_packet",
                "yangian_residue_transition",
                "yangian_brst_residue_chain_gate",
                "yangian_ope_coefficient_transition",
                "yangian_ope_serre_ideal_span_gate",
                "yangian_pbw_associated_graded_gate",
                "yangian_spectral_r_matrix_equation_gate",
                "yangian_spectral_associator_obstruction_packet",
                "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}",
            ),
            "forbidden_promotions": (
                "formal residue formulas are not cohomological operators",
                "finite label packets are not a strict spectral R-matrix",
            ),
        },
    }
    if bridge not in records:
        raise ValueError(f"unknown K3 x E bridge: {bridge}")
    data = records[bridge]
    return K3EBridgeConstructionRequirement(
        bridge=bridge,
        finite_symbol=str(data["finite_symbol"]),
        source_object=str(data["source_object"]),
        target_object=str(data["target_object"]),
        construction_obligations=tuple(data["construction_obligations"]),
        compatibility_obligations=tuple(data["compatibility_obligations"]),
        existing_finite_witnesses=tuple(data["existing_finite_witnesses"]),
        forbidden_promotions=tuple(data["forbidden_promotions"]),
        inverse_limit_gate=k3e_inverse_limit_gate_requirement(bridge),
    )


def k3e_bridge_construction_requirements() -> Tuple[K3EBridgeConstructionRequirement, ...]:
    """Return all structured open construction boundaries in dependency order."""
    return tuple(
        k3e_bridge_construction_requirement(bridge)
        for bridge in K3E_CLOSURE_BRIDGES
    )


def k3e_bridge_construction_requirement_from_witnesses(
    bridge: str,
    closure_witnesses: K3EClosureWitnesses,
) -> K3EBridgeConstructionRequirement:
    """Return one bridge requirement with supplied proof evidence applied."""
    requirement = k3e_bridge_construction_requirement(bridge)
    inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        bridge,
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    if bridge == "source_hall_borcherds_gate":
        source = source_recognition_record(closure_witnesses=closure_witnesses)
        proved = source.boundary_report.closed and inverse_limit_gate.all_proved
    else:
        proved = (
            bridge in closure_witnesses.bridge_construction_set
            and inverse_limit_gate.all_proved
        )
    return replace(
        requirement,
        status="proved" if proved else "open",
        inverse_limit_gate=inverse_limit_gate,
    )


def k3e_bridge_construction_requirements_from_witnesses(
    closure_witnesses: K3EClosureWitnesses,
) -> Tuple[K3EBridgeConstructionRequirement, ...]:
    """Return all bridge requirements with supplied proof evidence applied."""
    return tuple(
        k3e_bridge_construction_requirement_from_witnesses(
            bridge,
            closure_witnesses,
        )
        for bridge in K3E_CLOSURE_BRIDGES
    )


def _complete_hall_borcherds_witnesses() -> HallBorcherdsWitnesses:
    return HallBorcherdsWitnesses(
        oriented_critical_coha=True,
        hopf_pairing=True,
        drinfeld_double=True,
        denominator_normalization=True,
        root_multiplicity_map=True,
        k3xe_spectrum_separated=True,
        coha_positive_half_not_w=True,
        bkm_object_not_yangian=True,
    )


def _complete_recognition_envelope_witnesses() -> RecognitionEnvelopeWitnesses:
    return RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=True,
        serre_kernel_exact=True,
        green_adjoint_coproduct=True,
        primitive_center_reduction=True,
        associator_class_match=True,
        parity_fixture_match=True,
        transition_compatible=True,
    )


def _source_compact_double_witnesses_from_closure(
    closure_witnesses: K3EClosureWitnesses,
) -> SourceCompactDoubleGateWitnesses:
    compact_double_closed = (
        "source_hall_borcherds_gate" in closure_witnesses.bridge_construction_set
    )
    return SourceCompactDoubleGateWitnesses(
        compact_ml_exactness=compact_double_closed,
        compact_critical_realization=compact_double_closed,
        compact_support_properness=compact_double_closed,
        double_coproduct=compact_double_closed,
        double_pairing=compact_double_closed,
        double_center=compact_double_closed,
    )


def _source_pro_recognition_witnesses_from_closure(
    closure_witnesses: K3EClosureWitnesses,
) -> SourceProRecognitionGateWitnesses:
    proved = set(closure_witnesses.pro_recognition_proved_conditions)
    return SourceProRecognitionGateWitnesses(
        separated_completion=any(
            condition.startswith("Q_H^sep:") for condition in proved
        ),
        defect_ideal_exactness=any(
            condition.startswith("L_H^ex:") for condition in proved
        ),
        heegner_borcherds_coefficient_comparison=any(
            condition.startswith("H_H^HB:") for condition in proved
        ),
    )


def _source_witness_layers_from_closure(
    closure_witnesses: Optional[K3EClosureWitnesses],
) -> Tuple[
    HallBorcherdsWitnesses,
    RecognitionEnvelopeWitnesses,
    SourceCompactDoubleGateWitnesses,
    SourceProRecognitionGateWitnesses,
]:
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    gate_witnesses = (
        _complete_hall_borcherds_witnesses()
        if closure_witnesses.source_gate_closed
        else HallBorcherdsWitnesses()
    )
    envelope_witnesses = (
        _complete_recognition_envelope_witnesses()
        if closure_witnesses.source_recognition_envelope_completed
        else RecognitionEnvelopeWitnesses()
    )
    return (
        gate_witnesses,
        envelope_witnesses,
        _source_compact_double_witnesses_from_closure(closure_witnesses),
        _source_pro_recognition_witnesses_from_closure(closure_witnesses),
    )


def scattering_witness(max_discriminant: int = 8) -> ScatteringWitness:
    r"""Discriminant-graded K3 x E data used as the scattering witness."""
    table = _bar.k3e_product_by_discriminant(max_discriminant)
    support = [D for D, c in sorted(table.items()) if c != 0]
    return ScatteringWitness(
        max_discriminant=max_discriminant,
        discriminant_table=table,
        support=support,
        contains_polar_root=table.get(-1) == 1,
        contains_lightlike_root=table.get(0) == 10,
        contains_first_imaginary_root=table.get(3) == -64,
        status="witnessed at finite discriminant",
    )


def finite_stokes_hcs_hall_source_gate(
    finite_bound: int,
    *,
    source_differential_matrix: Iterable[Iterable[Any]],
    target_differential_matrix: Iterable[Iterable[Any]],
    theta_matrix: Iterable[Iterable[Any]],
    half_convolution_bracket_matrix: Iterable[Iterable[Any]],
    source_product_matrix: Iterable[Iterable[Any]],
    target_product_matrix: Iterable[Iterable[Any]],
    left_theta_matrix: Iterable[Iterable[Any]],
    right_theta_matrix: Iterable[Iterable[Any]],
    union_theta_matrix: Iterable[Iterable[Any]],
) -> FiniteStokesHCSHallSourceGate:
    r"""Check the finite Stokes hCS/Hall source equations.

    The supplied finite map theta satisfies the Stokes/Maurer-Cartan
    equation precisely when D_T theta - theta D_S + B_theta = 0, where
    B_theta is the supplied half-convolution-bracket matrix.  The same
    finite data are ordered E_1 multiplicative precisely when
    m_T (theta_left \otimes theta_right) = theta_union m_S.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    source_differential = _fraction_matrix(source_differential_matrix)
    target_differential = _fraction_matrix(target_differential_matrix)
    theta = _fraction_matrix(theta_matrix)
    half_bracket = _fraction_matrix(half_convolution_bracket_matrix)

    source_dimension, source_width = _matrix_shape(source_differential)
    target_dimension, target_width = _matrix_shape(target_differential)
    if source_dimension != source_width:
        raise ValueError("source_differential_matrix must be square")
    if target_dimension != target_width:
        raise ValueError("target_differential_matrix must be square")
    _validate_matrix_shape(theta, (target_dimension, source_dimension), "theta_matrix")
    _validate_matrix_shape(
        half_bracket,
        (target_dimension, source_dimension),
        "half_convolution_bracket_matrix",
    )

    target_after_theta = _matrix_product(target_differential, theta)
    theta_after_source = _matrix_product(theta, source_differential)
    maurer_cartan_defect = _matrix_sum(
        _matrix_difference(target_after_theta, theta_after_source),
        half_bracket,
    )
    maurer_cartan_rank = exact_matrix_rank(maurer_cartan_defect)
    maurer_cartan_closed = maurer_cartan_rank == 0

    source_product = _fraction_matrix(source_product_matrix)
    target_product = _fraction_matrix(target_product_matrix)
    left_theta = _fraction_matrix(left_theta_matrix)
    right_theta = _fraction_matrix(right_theta_matrix)
    union_theta = _fraction_matrix(union_theta_matrix)

    left_target_dimension, left_source_dimension = _matrix_shape(left_theta)
    right_target_dimension, right_source_dimension = _matrix_shape(right_theta)
    union_target_dimension, union_source_dimension = _matrix_shape(union_theta)
    _validate_matrix_shape(
        source_product,
        (union_source_dimension, left_source_dimension * right_source_dimension),
        "source_product_matrix",
    )
    _validate_matrix_shape(
        target_product,
        (union_target_dimension, left_target_dimension * right_target_dimension),
        "target_product_matrix",
    )

    component_theta = _matrix_kronecker_product(left_theta, right_theta)
    product_after_components = _matrix_product(target_product, component_theta)
    union_after_product = _matrix_product(union_theta, source_product)
    multiplicativity_defect = _matrix_difference(product_after_components, union_after_product)
    multiplicativity_rank = exact_matrix_rank(multiplicativity_defect)
    multiplicative = multiplicativity_rank == 0
    closed = maurer_cartan_closed and multiplicative

    return FiniteStokesHCSHallSourceGate(
        finite_bound=finite_bound,
        source_dimension=source_dimension,
        target_dimension=target_dimension,
        source_differential_shape=_matrix_shape(source_differential),
        target_differential_shape=_matrix_shape(target_differential),
        theta_shape=_matrix_shape(theta),
        half_convolution_bracket_shape=_matrix_shape(half_bracket),
        target_after_theta=target_after_theta,
        theta_after_source=theta_after_source,
        maurer_cartan_defect_matrix=maurer_cartan_defect,
        maurer_cartan_defect_rank=maurer_cartan_rank,
        maurer_cartan_closed=maurer_cartan_closed,
        source_product_shape=_matrix_shape(source_product),
        target_product_shape=_matrix_shape(target_product),
        left_theta_shape=_matrix_shape(left_theta),
        right_theta_shape=_matrix_shape(right_theta),
        union_theta_shape=_matrix_shape(union_theta),
        product_after_components=product_after_components,
        union_after_product=union_after_product,
        multiplicativity_defect_matrix=multiplicativity_defect,
        multiplicativity_defect_rank=multiplicativity_rank,
        multiplicative=multiplicative,
        closed=closed,
        status=(
            "FINITE_STOKES_HCS_HALL_SOURCE_GATE"
            if closed
            else "FINITE_STOKES_HCS_HALL_SOURCE_DEFECT"
        ),
    )


def _finite_realization_intertwining_defect(
    target_operator: Matrix,
    realization: Matrix,
    source_operator: Matrix,
) -> Matrix:
    """Return T R - R S for a supplied finite structure operator."""
    return _matrix_difference(
        _matrix_product(target_operator, realization),
        _matrix_product(realization, source_operator),
    )


def finite_rees_vanishing_cycle_realization_gate(
    finite_bound: int,
    *,
    source_differential_matrix: Iterable[Iterable[Any]],
    target_differential_matrix: Iterable[Iterable[Any]],
    realization_matrix: Iterable[Iterable[Any]],
    rees_thom_sebastiani_matrix: Iterable[Iterable[Any]],
    vanishing_cycle_thom_sebastiani_matrix: Iterable[Iterable[Any]],
    left_realization_matrix: Iterable[Iterable[Any]],
    right_realization_matrix: Iterable[Iterable[Any]],
    union_realization_matrix: Iterable[Iterable[Any]],
    proper_pushforward_source_matrix: Iterable[Iterable[Any]],
    proper_pushforward_target_matrix: Iterable[Iterable[Any]],
    lci_pullback_source_matrix: Iterable[Iterable[Any]],
    lci_pullback_target_matrix: Iterable[Iterable[Any]],
    orientation_source_matrix: Iterable[Iterable[Any]],
    orientation_target_matrix: Iterable[Iterable[Any]],
    tate_source_matrix: Iterable[Iterable[Any]],
    tate_target_matrix: Iterable[Iterable[Any]],
    support_source_projection_matrix: Iterable[Iterable[Any]],
    support_target_projection_matrix: Iterable[Iterable[Any]],
    completion_source_projection_matrix: Iterable[Iterable[Any]],
    completion_target_projection_matrix: Iterable[Iterable[Any]],
    equivariance_data: Iterable[Dict[str, Any]] = (),
) -> FiniteReesVanishingCycleRealizationGate:
    r"""Check a supplied finite Rees-to-vanishing-cycle realization packet.

    The realization matrix R is a chain map precisely when
    D_V R = R D_K.  Its Thom-Sebastiani compatibility is the finite
    equality R_union TS_Rees = TS_phi (R_left \otimes R_right).  The
    proper pushforward, lci pullback, orientation, shift/Tate,
    Borel-Moore support, completion, and equivariance data are supplied
    endomorphisms or projections; the gate checks that each intertwines
    with R.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    source_differential = _fraction_matrix(source_differential_matrix)
    target_differential = _fraction_matrix(target_differential_matrix)
    realization = _fraction_matrix(realization_matrix)

    source_dimension, source_width = _matrix_shape(source_differential)
    target_dimension, target_width = _matrix_shape(target_differential)
    if source_dimension != source_width:
        raise ValueError("source_differential_matrix must be square")
    if target_dimension != target_width:
        raise ValueError("target_differential_matrix must be square")
    _validate_matrix_shape(
        realization,
        (target_dimension, source_dimension),
        "realization_matrix",
    )

    chain_defect = _finite_realization_intertwining_defect(
        target_differential,
        realization,
        source_differential,
    )
    chain_rank = exact_matrix_rank(chain_defect)
    chain_map = chain_rank == 0

    rees_ts = _fraction_matrix(rees_thom_sebastiani_matrix)
    vc_ts = _fraction_matrix(vanishing_cycle_thom_sebastiani_matrix)
    left_realization = _fraction_matrix(left_realization_matrix)
    right_realization = _fraction_matrix(right_realization_matrix)
    union_realization = _fraction_matrix(union_realization_matrix)

    left_target_dimension, left_source_dimension = _matrix_shape(left_realization)
    right_target_dimension, right_source_dimension = _matrix_shape(right_realization)
    union_target_dimension, union_source_dimension = _matrix_shape(union_realization)
    _validate_matrix_shape(
        rees_ts,
        (
            union_source_dimension,
            left_source_dimension * right_source_dimension,
        ),
        "rees_thom_sebastiani_matrix",
    )
    _validate_matrix_shape(
        vc_ts,
        (
            union_target_dimension,
            left_target_dimension * right_target_dimension,
        ),
        "vanishing_cycle_thom_sebastiani_matrix",
    )

    component_realization = _matrix_kronecker_product(left_realization, right_realization)
    thom_sebastiani_left = _matrix_product(union_realization, rees_ts)
    thom_sebastiani_right = _matrix_product(vc_ts, component_realization)
    thom_sebastiani_defect = _matrix_difference(
        thom_sebastiani_left,
        thom_sebastiani_right,
    )
    thom_sebastiani_rank = exact_matrix_rank(thom_sebastiani_defect)
    thom_sebastiani_compatible = thom_sebastiani_rank == 0

    proper_pushforward_source = _fraction_matrix(proper_pushforward_source_matrix)
    proper_pushforward_target = _fraction_matrix(proper_pushforward_target_matrix)
    lci_pullback_source = _fraction_matrix(lci_pullback_source_matrix)
    lci_pullback_target = _fraction_matrix(lci_pullback_target_matrix)
    orientation_source = _fraction_matrix(orientation_source_matrix)
    orientation_target = _fraction_matrix(orientation_target_matrix)
    tate_source = _fraction_matrix(tate_source_matrix)
    tate_target = _fraction_matrix(tate_target_matrix)
    support_source = _fraction_matrix(support_source_projection_matrix)
    support_target = _fraction_matrix(support_target_projection_matrix)
    completion_source = _fraction_matrix(completion_source_projection_matrix)
    completion_target = _fraction_matrix(completion_target_projection_matrix)

    _validate_matrix_shape(
        proper_pushforward_source,
        (source_dimension, source_dimension),
        "proper_pushforward_source_matrix",
    )
    _validate_matrix_shape(
        proper_pushforward_target,
        (target_dimension, target_dimension),
        "proper_pushforward_target_matrix",
    )
    _validate_matrix_shape(
        lci_pullback_source,
        (source_dimension, source_dimension),
        "lci_pullback_source_matrix",
    )
    _validate_matrix_shape(
        lci_pullback_target,
        (target_dimension, target_dimension),
        "lci_pullback_target_matrix",
    )
    _validate_matrix_shape(
        orientation_source,
        (source_dimension, source_dimension),
        "orientation_source_matrix",
    )
    _validate_matrix_shape(
        orientation_target,
        (target_dimension, target_dimension),
        "orientation_target_matrix",
    )
    _validate_matrix_shape(
        tate_source,
        (source_dimension, source_dimension),
        "tate_source_matrix",
    )
    _validate_matrix_shape(
        tate_target,
        (target_dimension, target_dimension),
        "tate_target_matrix",
    )
    _validate_matrix_shape(
        support_source,
        (source_dimension, source_dimension),
        "support_source_projection_matrix",
    )
    _validate_matrix_shape(
        support_target,
        (target_dimension, target_dimension),
        "support_target_projection_matrix",
    )
    _validate_matrix_shape(
        completion_source,
        (source_dimension, source_dimension),
        "completion_source_projection_matrix",
    )
    _validate_matrix_shape(
        completion_target,
        (target_dimension, target_dimension),
        "completion_target_projection_matrix",
    )

    proper_pushforward_defect = _finite_realization_intertwining_defect(
        proper_pushforward_target,
        realization,
        proper_pushforward_source,
    )
    lci_pullback_defect = _finite_realization_intertwining_defect(
        lci_pullback_target,
        realization,
        lci_pullback_source,
    )
    orientation_defect = _finite_realization_intertwining_defect(
        orientation_target,
        realization,
        orientation_source,
    )
    tate_defect = _finite_realization_intertwining_defect(
        tate_target,
        realization,
        tate_source,
    )
    support_defect = _finite_realization_intertwining_defect(
        support_target,
        realization,
        support_source,
    )
    completion_defect = _finite_realization_intertwining_defect(
        completion_target,
        realization,
        completion_source,
    )

    proper_pushforward_rank = exact_matrix_rank(proper_pushforward_defect)
    lci_pullback_rank = exact_matrix_rank(lci_pullback_defect)
    orientation_rank = exact_matrix_rank(orientation_defect)
    tate_rank = exact_matrix_rank(tate_defect)
    support_rank = exact_matrix_rank(support_defect)
    completion_rank = exact_matrix_rank(completion_defect)

    equivariance_reports: List[FiniteEquivarianceDefectReport] = []
    for index, entry in enumerate(equivariance_data):
        label = str(entry.get("label", f"g{index}"))
        if "source_matrix" not in entry or "target_matrix" not in entry:
            raise ValueError(
                f"equivariance datum {label} must supply source_matrix and target_matrix"
            )
        equiv_source = _fraction_matrix(entry["source_matrix"])
        equiv_target = _fraction_matrix(entry["target_matrix"])
        _validate_matrix_shape(
            equiv_source,
            (source_dimension, source_dimension),
            f"equivariance source_matrix {label}",
        )
        _validate_matrix_shape(
            equiv_target,
            (target_dimension, target_dimension),
            f"equivariance target_matrix {label}",
        )
        defect = _finite_realization_intertwining_defect(
            equiv_target,
            realization,
            equiv_source,
        )
        rank = exact_matrix_rank(defect)
        equivariance_reports.append(
            FiniteEquivarianceDefectReport(
                label=label,
                defect_matrix=defect,
                defect_rank=rank,
                compatible=rank == 0,
            )
        )

    proper_pushforward_compatible = proper_pushforward_rank == 0
    lci_pullback_compatible = lci_pullback_rank == 0
    orientation_compatible = orientation_rank == 0
    tate_compatible = tate_rank == 0
    support_compatible = support_rank == 0
    completion_compatible = completion_rank == 0
    equivariant = all(report.compatible for report in equivariance_reports)
    closed = (
        chain_map
        and thom_sebastiani_compatible
        and proper_pushforward_compatible
        and lci_pullback_compatible
        and orientation_compatible
        and tate_compatible
        and support_compatible
        and completion_compatible
        and equivariant
    )

    return FiniteReesVanishingCycleRealizationGate(
        finite_bound=finite_bound,
        source_dimension=source_dimension,
        target_dimension=target_dimension,
        source_differential_shape=_matrix_shape(source_differential),
        target_differential_shape=_matrix_shape(target_differential),
        realization_shape=_matrix_shape(realization),
        chain_defect_matrix=chain_defect,
        thom_sebastiani_left_matrix=thom_sebastiani_left,
        thom_sebastiani_right_matrix=thom_sebastiani_right,
        thom_sebastiani_defect_matrix=thom_sebastiani_defect,
        proper_pushforward_defect_matrix=proper_pushforward_defect,
        lci_pullback_defect_matrix=lci_pullback_defect,
        orientation_defect_matrix=orientation_defect,
        tate_defect_matrix=tate_defect,
        support_defect_matrix=support_defect,
        completion_defect_matrix=completion_defect,
        equivariance_reports=tuple(equivariance_reports),
        chain_defect_rank=chain_rank,
        thom_sebastiani_defect_rank=thom_sebastiani_rank,
        proper_pushforward_defect_rank=proper_pushforward_rank,
        lci_pullback_defect_rank=lci_pullback_rank,
        orientation_defect_rank=orientation_rank,
        tate_defect_rank=tate_rank,
        support_defect_rank=support_rank,
        completion_defect_rank=completion_rank,
        chain_map=chain_map,
        thom_sebastiani_compatible=thom_sebastiani_compatible,
        proper_pushforward_compatible=proper_pushforward_compatible,
        lci_pullback_compatible=lci_pullback_compatible,
        orientation_compatible=orientation_compatible,
        tate_compatible=tate_compatible,
        support_compatible=support_compatible,
        completion_compatible=completion_compatible,
        equivariant=equivariant,
        closed=closed,
        status=(
            "FINITE_REES_VANISHING_CYCLE_REALIZATION_GATE"
            if closed
            else "FINITE_REES_VANISHING_CYCLE_REALIZATION_DEFECT"
        ),
    )


def finite_realized_hcs_hall_composite_gate(
    finite_bound: int,
    *,
    source_differential_matrix: Iterable[Iterable[Any]],
    rees_differential_matrix: Iterable[Iterable[Any]],
    realized_differential_matrix: Iterable[Iterable[Any]],
    theta_rees_matrix: Iterable[Iterable[Any]],
    realization_matrix: Iterable[Iterable[Any]],
    rees_half_convolution_bracket_matrix: Iterable[Iterable[Any]],
    realized_half_convolution_bracket_matrix: Iterable[Iterable[Any]],
    source_product_matrix: Iterable[Iterable[Any]],
    rees_product_matrix: Iterable[Iterable[Any]],
    realized_product_matrix: Iterable[Iterable[Any]],
    left_theta_rees_matrix: Iterable[Iterable[Any]],
    right_theta_rees_matrix: Iterable[Iterable[Any]],
    union_theta_rees_matrix: Iterable[Iterable[Any]],
    left_realization_matrix: Iterable[Iterable[Any]],
    right_realization_matrix: Iterable[Iterable[Any]],
    union_realization_matrix: Iterable[Iterable[Any]],
) -> FiniteRealizedHCSHallCompositeGate:
    r"""Check the finite composite RW theta from hCS to critical CoHA.

    The gate verifies the supplied Rees comparison, the supplied
    realization, and the transported realized comparison at one finite
    bound.  It records both ingredient defects and direct composite
    defects, so accidental cancellation is not treated as a proof of
    the realized map.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    source_differential = _fraction_matrix(source_differential_matrix)
    rees_differential = _fraction_matrix(rees_differential_matrix)
    realized_differential = _fraction_matrix(realized_differential_matrix)
    theta_rees = _fraction_matrix(theta_rees_matrix)
    realization = _fraction_matrix(realization_matrix)
    rees_half_bracket = _fraction_matrix(rees_half_convolution_bracket_matrix)
    realized_half_bracket = _fraction_matrix(realized_half_convolution_bracket_matrix)

    source_dimension, source_width = _matrix_shape(source_differential)
    rees_dimension, rees_width = _matrix_shape(rees_differential)
    realized_dimension, realized_width = _matrix_shape(realized_differential)
    if source_dimension != source_width:
        raise ValueError("source_differential_matrix must be square")
    if rees_dimension != rees_width:
        raise ValueError("rees_differential_matrix must be square")
    if realized_dimension != realized_width:
        raise ValueError("realized_differential_matrix must be square")
    _validate_matrix_shape(
        theta_rees,
        (rees_dimension, source_dimension),
        "theta_rees_matrix",
    )
    _validate_matrix_shape(
        realization,
        (realized_dimension, rees_dimension),
        "realization_matrix",
    )
    _validate_matrix_shape(
        rees_half_bracket,
        (rees_dimension, source_dimension),
        "rees_half_convolution_bracket_matrix",
    )
    _validate_matrix_shape(
        realized_half_bracket,
        (realized_dimension, source_dimension),
        "realized_half_convolution_bracket_matrix",
    )

    realized_theta = _matrix_product(realization, theta_rees)
    chain_transport_defect = _finite_realization_intertwining_defect(
        realized_differential,
        realization,
        rees_differential,
    )
    rees_maurer_cartan_defect = _matrix_sum(
        _matrix_difference(
            _matrix_product(rees_differential, theta_rees),
            _matrix_product(theta_rees, source_differential),
        ),
        rees_half_bracket,
    )
    bracket_transport_defect = _matrix_difference(
        realized_half_bracket,
        _matrix_product(realization, rees_half_bracket),
    )
    realized_maurer_cartan_defect = _matrix_sum(
        _matrix_difference(
            _matrix_product(realized_differential, realized_theta),
            _matrix_product(realized_theta, source_differential),
        ),
        realized_half_bracket,
    )

    source_product = _fraction_matrix(source_product_matrix)
    rees_product = _fraction_matrix(rees_product_matrix)
    realized_product = _fraction_matrix(realized_product_matrix)
    left_theta_rees = _fraction_matrix(left_theta_rees_matrix)
    right_theta_rees = _fraction_matrix(right_theta_rees_matrix)
    union_theta_rees = _fraction_matrix(union_theta_rees_matrix)
    left_realization = _fraction_matrix(left_realization_matrix)
    right_realization = _fraction_matrix(right_realization_matrix)
    union_realization = _fraction_matrix(union_realization_matrix)

    left_rees_dimension, left_source_dimension = _matrix_shape(left_theta_rees)
    right_rees_dimension, right_source_dimension = _matrix_shape(right_theta_rees)
    union_rees_dimension, union_source_dimension = _matrix_shape(union_theta_rees)
    left_realized_dimension, left_realization_width = _matrix_shape(left_realization)
    right_realized_dimension, right_realization_width = _matrix_shape(right_realization)
    union_realized_dimension, union_realization_width = _matrix_shape(union_realization)
    if left_realization_width != left_rees_dimension:
        raise ValueError("left_realization_matrix width must match left_theta_rees_matrix height")
    if right_realization_width != right_rees_dimension:
        raise ValueError("right_realization_matrix width must match right_theta_rees_matrix height")
    if union_realization_width != union_rees_dimension:
        raise ValueError("union_realization_matrix width must match union_theta_rees_matrix height")

    _validate_matrix_shape(
        source_product,
        (union_source_dimension, left_source_dimension * right_source_dimension),
        "source_product_matrix",
    )
    _validate_matrix_shape(
        rees_product,
        (union_rees_dimension, left_rees_dimension * right_rees_dimension),
        "rees_product_matrix",
    )
    _validate_matrix_shape(
        realized_product,
        (
            union_realized_dimension,
            left_realized_dimension * right_realized_dimension,
        ),
        "realized_product_matrix",
    )

    component_theta_rees = _matrix_kronecker_product(left_theta_rees, right_theta_rees)
    component_realization = _matrix_kronecker_product(left_realization, right_realization)
    realized_left_theta = _matrix_product(left_realization, left_theta_rees)
    realized_right_theta = _matrix_product(right_realization, right_theta_rees)
    realized_union_theta = _matrix_product(union_realization, union_theta_rees)
    realized_component_theta = _matrix_kronecker_product(
        realized_left_theta,
        realized_right_theta,
    )

    rees_product_defect = _matrix_difference(
        _matrix_product(rees_product, component_theta_rees),
        _matrix_product(union_theta_rees, source_product),
    )
    product_transport_defect = _matrix_difference(
        _matrix_product(realized_product, component_realization),
        _matrix_product(union_realization, rees_product),
    )
    realized_product_defect = _matrix_difference(
        _matrix_product(realized_product, realized_component_theta),
        _matrix_product(realized_union_theta, source_product),
    )

    chain_transport_rank = exact_matrix_rank(chain_transport_defect)
    rees_maurer_cartan_rank = exact_matrix_rank(rees_maurer_cartan_defect)
    bracket_transport_rank = exact_matrix_rank(bracket_transport_defect)
    realized_maurer_cartan_rank = exact_matrix_rank(realized_maurer_cartan_defect)
    rees_product_rank = exact_matrix_rank(rees_product_defect)
    product_transport_rank = exact_matrix_rank(product_transport_defect)
    realized_product_rank = exact_matrix_rank(realized_product_defect)

    chain_transport_compatible = chain_transport_rank == 0
    rees_maurer_cartan_closed = rees_maurer_cartan_rank == 0
    bracket_transported = bracket_transport_rank == 0
    realized_maurer_cartan_closed = realized_maurer_cartan_rank == 0
    rees_multiplicative = rees_product_rank == 0
    product_transport_compatible = product_transport_rank == 0
    realized_multiplicative = realized_product_rank == 0
    closed = (
        chain_transport_compatible
        and rees_maurer_cartan_closed
        and bracket_transported
        and realized_maurer_cartan_closed
        and rees_multiplicative
        and product_transport_compatible
        and realized_multiplicative
    )

    return FiniteRealizedHCSHallCompositeGate(
        finite_bound=finite_bound,
        source_dimension=source_dimension,
        rees_dimension=rees_dimension,
        realized_dimension=realized_dimension,
        realized_theta_matrix=realized_theta,
        chain_transport_defect_matrix=chain_transport_defect,
        rees_maurer_cartan_defect_matrix=rees_maurer_cartan_defect,
        bracket_transport_defect_matrix=bracket_transport_defect,
        realized_maurer_cartan_defect_matrix=realized_maurer_cartan_defect,
        rees_product_defect_matrix=rees_product_defect,
        product_transport_defect_matrix=product_transport_defect,
        realized_product_defect_matrix=realized_product_defect,
        chain_transport_defect_rank=chain_transport_rank,
        rees_maurer_cartan_defect_rank=rees_maurer_cartan_rank,
        bracket_transport_defect_rank=bracket_transport_rank,
        realized_maurer_cartan_defect_rank=realized_maurer_cartan_rank,
        rees_product_defect_rank=rees_product_rank,
        product_transport_defect_rank=product_transport_rank,
        realized_product_defect_rank=realized_product_rank,
        chain_transport_compatible=chain_transport_compatible,
        rees_maurer_cartan_closed=rees_maurer_cartan_closed,
        bracket_transported=bracket_transported,
        realized_maurer_cartan_closed=realized_maurer_cartan_closed,
        rees_multiplicative=rees_multiplicative,
        product_transport_compatible=product_transport_compatible,
        realized_multiplicative=realized_multiplicative,
        closed=closed,
        status=(
            "FINITE_REALIZED_HCS_HALL_COMPOSITE_GATE"
            if closed
            else "FINITE_REALIZED_HCS_HALL_COMPOSITE_DEFECT"
        ),
    )


def finite_realized_composite_transition_ml_gate(
    upper_bound: int,
    lower_bound: int,
    *,
    upper_composite_matrix: Iterable[Iterable[Any]],
    lower_composite_matrix: Iterable[Iterable[Any]],
    source_transition_matrix: Iterable[Iterable[Any]],
    realized_transition_matrix: Iterable[Iterable[Any]],
    cohomology_transition_matrices: Iterable[Dict[str, Any]],
) -> FiniteRealizedCompositeTransitionMLGate:
    r"""Check one finite transition step for realized hCS/Hall composites.

    The inverse-system square is P_V X_U = X_L P_S.  The supplied
    cohomology transition matrices encode the finite Mittag-Leffler
    check degree by degree: each lower-by-upper matrix must be
    surjective onto the lower cohomology space.
    """
    if lower_bound < 0 or upper_bound < 0:
        raise ValueError("bounds must be nonnegative")
    if upper_bound <= lower_bound:
        raise ValueError("upper_bound must be greater than lower_bound")

    upper_composite = _fraction_matrix(upper_composite_matrix)
    lower_composite = _fraction_matrix(lower_composite_matrix)
    source_transition = _fraction_matrix(source_transition_matrix)
    realized_transition = _fraction_matrix(realized_transition_matrix)

    upper_target_dimension, upper_source_dimension = _matrix_shape(upper_composite)
    lower_target_dimension, lower_source_dimension = _matrix_shape(lower_composite)
    _validate_matrix_shape(
        source_transition,
        (lower_source_dimension, upper_source_dimension),
        "source_transition_matrix",
    )
    _validate_matrix_shape(
        realized_transition,
        (lower_target_dimension, upper_target_dimension),
        "realized_transition_matrix",
    )

    target_after_upper = _matrix_product(realized_transition, upper_composite)
    lower_after_source = _matrix_product(lower_composite, source_transition)
    transition_defect = _matrix_difference(target_after_upper, lower_after_source)
    transition_rank = exact_matrix_rank(transition_defect)
    transition_commutes = transition_rank == 0

    cohomology_reports: List[FiniteRealizedCompositeCohomologyTransitionReport] = []
    for entry in cohomology_transition_matrices:
        if "degree" not in entry or "transition_matrix" not in entry:
            raise ValueError("each cohomology transition must supply degree and transition_matrix")
        degree = int(entry["degree"])
        matrix = _fraction_matrix(entry["transition_matrix"])
        lower_dimension, upper_dimension = _matrix_shape(matrix)
        rank = exact_matrix_rank(matrix)
        defect = lower_dimension - rank
        cohomology_reports.append(
            FiniteRealizedCompositeCohomologyTransitionReport(
                degree=degree,
                transition_matrix=matrix,
                upper_dimension=upper_dimension,
                lower_dimension=lower_dimension,
                transition_rank=rank,
                surjective=defect == 0,
                defect=defect,
            )
        )
    if not cohomology_reports:
        raise ValueError("at least one cohomology transition must be supplied")

    cohomology_mittag_leffler = all(report.surjective for report in cohomology_reports)
    closed = transition_commutes and cohomology_mittag_leffler
    return FiniteRealizedCompositeTransitionMLGate(
        upper_bound=upper_bound,
        lower_bound=lower_bound,
        upper_composite_shape=_matrix_shape(upper_composite),
        lower_composite_shape=_matrix_shape(lower_composite),
        source_transition_shape=_matrix_shape(source_transition),
        realized_transition_shape=_matrix_shape(realized_transition),
        target_after_upper_composite=target_after_upper,
        lower_composite_after_source=lower_after_source,
        transition_defect_matrix=transition_defect,
        transition_defect_rank=transition_rank,
        cohomology_reports=tuple(cohomology_reports),
        transition_commutes=transition_commutes,
        cohomology_mittag_leffler=cohomology_mittag_leffler,
        closed=closed,
        status=(
            "FINITE_REALIZED_COMPOSITE_TRANSITION_ML_GATE"
            if closed
            else "FINITE_REALIZED_COMPOSITE_TRANSITION_ML_DEFECT"
        ),
    )


def finite_realized_cy3_shifted_bracket_gate(
    finite_bound: int,
    *,
    source_bracket_matrix: Iterable[Iterable[Any]],
    rees_bracket_matrix: Iterable[Iterable[Any]],
    realized_bracket_matrix: Iterable[Iterable[Any]],
    left_theta_rees_matrix: Iterable[Iterable[Any]],
    right_theta_rees_matrix: Iterable[Iterable[Any]],
    union_theta_rees_matrix: Iterable[Iterable[Any]],
    left_realization_matrix: Iterable[Iterable[Any]],
    right_realization_matrix: Iterable[Iterable[Any]],
    union_realization_matrix: Iterable[Iterable[Any]],
) -> FiniteRealizedCY3ShiftedBracketGate:
    r"""Check finite CY3 shifted-bracket compatibility after realization.

    The CY3 degree shift is encoded in the supplied bases.  The finite
    equations are the Rees bracket square, the bracket-transport square,
    and the direct realized bracket square.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    source_bracket = _fraction_matrix(source_bracket_matrix)
    rees_bracket = _fraction_matrix(rees_bracket_matrix)
    realized_bracket = _fraction_matrix(realized_bracket_matrix)
    left_theta_rees = _fraction_matrix(left_theta_rees_matrix)
    right_theta_rees = _fraction_matrix(right_theta_rees_matrix)
    union_theta_rees = _fraction_matrix(union_theta_rees_matrix)
    left_realization = _fraction_matrix(left_realization_matrix)
    right_realization = _fraction_matrix(right_realization_matrix)
    union_realization = _fraction_matrix(union_realization_matrix)

    left_rees_dimension, left_source_dimension = _matrix_shape(left_theta_rees)
    right_rees_dimension, right_source_dimension = _matrix_shape(right_theta_rees)
    union_rees_dimension, union_source_dimension = _matrix_shape(union_theta_rees)
    left_realized_dimension, left_realization_width = _matrix_shape(left_realization)
    right_realized_dimension, right_realization_width = _matrix_shape(right_realization)
    union_realized_dimension, union_realization_width = _matrix_shape(union_realization)
    if left_realization_width != left_rees_dimension:
        raise ValueError("left_realization_matrix width must match left_theta_rees_matrix height")
    if right_realization_width != right_rees_dimension:
        raise ValueError("right_realization_matrix width must match right_theta_rees_matrix height")
    if union_realization_width != union_rees_dimension:
        raise ValueError("union_realization_matrix width must match union_theta_rees_matrix height")

    _validate_matrix_shape(
        source_bracket,
        (union_source_dimension, left_source_dimension * right_source_dimension),
        "source_bracket_matrix",
    )
    _validate_matrix_shape(
        rees_bracket,
        (union_rees_dimension, left_rees_dimension * right_rees_dimension),
        "rees_bracket_matrix",
    )
    _validate_matrix_shape(
        realized_bracket,
        (
            union_realized_dimension,
            left_realized_dimension * right_realized_dimension,
        ),
        "realized_bracket_matrix",
    )

    component_theta_rees = _matrix_kronecker_product(left_theta_rees, right_theta_rees)
    component_realization = _matrix_kronecker_product(left_realization, right_realization)
    realized_left_theta = _matrix_product(left_realization, left_theta_rees)
    realized_right_theta = _matrix_product(right_realization, right_theta_rees)
    realized_union_theta = _matrix_product(union_realization, union_theta_rees)
    realized_component_theta = _matrix_kronecker_product(
        realized_left_theta,
        realized_right_theta,
    )

    rees_bracket_defect = _matrix_difference(
        _matrix_product(rees_bracket, component_theta_rees),
        _matrix_product(union_theta_rees, source_bracket),
    )
    bracket_transport_defect = _matrix_difference(
        _matrix_product(realized_bracket, component_realization),
        _matrix_product(union_realization, rees_bracket),
    )
    realized_bracket_defect = _matrix_difference(
        _matrix_product(realized_bracket, realized_component_theta),
        _matrix_product(realized_union_theta, source_bracket),
    )

    rees_bracket_rank = exact_matrix_rank(rees_bracket_defect)
    bracket_transport_rank = exact_matrix_rank(bracket_transport_defect)
    realized_bracket_rank = exact_matrix_rank(realized_bracket_defect)
    rees_bracket_compatible = rees_bracket_rank == 0
    bracket_transport_compatible = bracket_transport_rank == 0
    realized_bracket_compatible = realized_bracket_rank == 0
    closed = (
        rees_bracket_compatible
        and bracket_transport_compatible
        and realized_bracket_compatible
    )

    return FiniteRealizedCY3ShiftedBracketGate(
        finite_bound=finite_bound,
        rees_bracket_defect_matrix=rees_bracket_defect,
        bracket_transport_defect_matrix=bracket_transport_defect,
        realized_bracket_defect_matrix=realized_bracket_defect,
        rees_bracket_defect_rank=rees_bracket_rank,
        bracket_transport_defect_rank=bracket_transport_rank,
        realized_bracket_defect_rank=realized_bracket_rank,
        rees_bracket_compatible=rees_bracket_compatible,
        bracket_transport_compatible=bracket_transport_compatible,
        realized_bracket_compatible=realized_bracket_compatible,
        closed=closed,
        status=(
            "FINITE_REALIZED_CY3_SHIFTED_BRACKET_GATE"
            if closed
            else "FINITE_REALIZED_CY3_SHIFTED_BRACKET_DEFECT"
        ),
    )


def _finite_projection_intertwining_defect(
    target_projection: Matrix,
    map_matrix: Matrix,
    source_projection: Matrix,
) -> Matrix:
    return _matrix_difference(
        _matrix_product(target_projection, map_matrix),
        _matrix_product(map_matrix, source_projection),
    )


def finite_compact_support_beck_chevalley_gate(
    finite_bound: int,
    *,
    proper_pushforward_matrix: Iterable[Iterable[Any]],
    base_lci_pullback_matrix: Iterable[Iterable[Any]],
    source_lci_pullback_matrix: Iterable[Iterable[Any]],
    pulled_proper_pushforward_matrix: Iterable[Iterable[Any]],
    source_support_projection_matrix: Iterable[Iterable[Any]],
    target_support_projection_matrix: Iterable[Iterable[Any]],
    pulled_source_support_projection_matrix: Iterable[Iterable[Any]],
    pulled_target_support_projection_matrix: Iterable[Iterable[Any]],
) -> FiniteCompactSupportBeckChevalleyGate:
    r"""Check a finite compact-support Beck-Chevalley square.

    For a Cartesian square with proper pushforward F, lci pullbacks G_Y
    and G_X, and pulled pushforward F', the Beck-Chevalley defect is
    G_Y F - F' G_X.  Compact-support compatibility is checked by
    requiring each correspondence map to commute with the supplied
    support projections on source and target.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    proper_pushforward = _fraction_matrix(proper_pushforward_matrix)
    base_lci_pullback = _fraction_matrix(base_lci_pullback_matrix)
    source_lci_pullback = _fraction_matrix(source_lci_pullback_matrix)
    pulled_proper_pushforward = _fraction_matrix(pulled_proper_pushforward_matrix)

    target_dimension, source_dimension = _matrix_shape(proper_pushforward)
    pulled_target_dimension, base_target_width = _matrix_shape(base_lci_pullback)
    pulled_source_dimension, source_lci_width = _matrix_shape(source_lci_pullback)
    pulled_proper_height, pulled_proper_width = _matrix_shape(pulled_proper_pushforward)
    if base_target_width != target_dimension:
        raise ValueError("base_lci_pullback_matrix width must match proper_pushforward_matrix height")
    if source_lci_width != source_dimension:
        raise ValueError("source_lci_pullback_matrix width must match proper_pushforward_matrix width")
    if pulled_proper_height != pulled_target_dimension:
        raise ValueError("pulled_proper_pushforward_matrix height must match base_lci_pullback_matrix height")
    if pulled_proper_width != pulled_source_dimension:
        raise ValueError("pulled_proper_pushforward_matrix width must match source_lci_pullback_matrix height")

    source_support = _fraction_matrix(source_support_projection_matrix)
    target_support = _fraction_matrix(target_support_projection_matrix)
    pulled_source_support = _fraction_matrix(pulled_source_support_projection_matrix)
    pulled_target_support = _fraction_matrix(pulled_target_support_projection_matrix)
    _validate_matrix_shape(
        source_support,
        (source_dimension, source_dimension),
        "source_support_projection_matrix",
    )
    _validate_matrix_shape(
        target_support,
        (target_dimension, target_dimension),
        "target_support_projection_matrix",
    )
    _validate_matrix_shape(
        pulled_source_support,
        (pulled_source_dimension, pulled_source_dimension),
        "pulled_source_support_projection_matrix",
    )
    _validate_matrix_shape(
        pulled_target_support,
        (pulled_target_dimension, pulled_target_dimension),
        "pulled_target_support_projection_matrix",
    )

    beck_chevalley_left = _matrix_product(base_lci_pullback, proper_pushforward)
    beck_chevalley_right = _matrix_product(
        pulled_proper_pushforward,
        source_lci_pullback,
    )
    beck_chevalley_defect = _matrix_difference(
        beck_chevalley_left,
        beck_chevalley_right,
    )
    proper_support_defect = _finite_projection_intertwining_defect(
        target_support,
        proper_pushforward,
        source_support,
    )
    base_lci_support_defect = _finite_projection_intertwining_defect(
        pulled_target_support,
        base_lci_pullback,
        target_support,
    )
    source_lci_support_defect = _finite_projection_intertwining_defect(
        pulled_source_support,
        source_lci_pullback,
        source_support,
    )
    pulled_proper_support_defect = _finite_projection_intertwining_defect(
        pulled_target_support,
        pulled_proper_pushforward,
        pulled_source_support,
    )

    beck_chevalley_rank = exact_matrix_rank(beck_chevalley_defect)
    proper_support_rank = exact_matrix_rank(proper_support_defect)
    base_lci_support_rank = exact_matrix_rank(base_lci_support_defect)
    source_lci_support_rank = exact_matrix_rank(source_lci_support_defect)
    pulled_proper_support_rank = exact_matrix_rank(pulled_proper_support_defect)
    beck_chevalley_compatible = beck_chevalley_rank == 0
    compact_support_compatible = (
        proper_support_rank == 0
        and base_lci_support_rank == 0
        and source_lci_support_rank == 0
        and pulled_proper_support_rank == 0
    )
    closed = beck_chevalley_compatible and compact_support_compatible

    return FiniteCompactSupportBeckChevalleyGate(
        finite_bound=finite_bound,
        source_dimension=source_dimension,
        target_dimension=target_dimension,
        pulled_source_dimension=pulled_source_dimension,
        pulled_target_dimension=pulled_target_dimension,
        beck_chevalley_left_matrix=beck_chevalley_left,
        beck_chevalley_right_matrix=beck_chevalley_right,
        beck_chevalley_defect_matrix=beck_chevalley_defect,
        proper_support_defect_matrix=proper_support_defect,
        base_lci_support_defect_matrix=base_lci_support_defect,
        source_lci_support_defect_matrix=source_lci_support_defect,
        pulled_proper_support_defect_matrix=pulled_proper_support_defect,
        beck_chevalley_defect_rank=beck_chevalley_rank,
        proper_support_defect_rank=proper_support_rank,
        base_lci_support_defect_rank=base_lci_support_rank,
        source_lci_support_defect_rank=source_lci_support_rank,
        pulled_proper_support_defect_rank=pulled_proper_support_rank,
        beck_chevalley_compatible=beck_chevalley_compatible,
        compact_support_compatible=compact_support_compatible,
        closed=closed,
        status=(
            "FINITE_COMPACT_SUPPORT_BECK_CHEVALLEY_GATE"
            if closed
            else "FINITE_COMPACT_SUPPORT_BECK_CHEVALLEY_DEFECT"
        ),
    )


def finite_drinfeld_double_datum_gate(
    finite_height: int,
    *,
    cartan_dimension: int,
    reduced_pairing_matrix: Iterable[Iterable[Any]],
    triangular_normal_form_matrix: Iterable[Iterable[Any]],
    mixed_product_matrix: Iterable[Iterable[Any]],
    drinfeld_cross_relation_matrix: Iterable[Iterable[Any]],
    coproduct_coassociator_defect_matrix: Iterable[Iterable[Any]],
    associator_pentagon_defect_matrix: Iterable[Iterable[Any]],
    center_compatibility_defect_matrix: Iterable[Iterable[Any]],
) -> FiniteDrinfeldDoubleDatumGate:
    r"""Check a supplied finite Hall-Drinfeld double datum.

    The gate separates the vector-space normal form, the radical-quotient
    pairing, the mixed Drinfeld cross relation, and the remaining
    coassociator/associator/centre defects.  It is a finite criterion for
    supplied data, not a construction of the compact Hall double.
    """
    if finite_height <= 0:
        raise ValueError("finite_height must be positive")
    if cartan_dimension <= 0:
        raise ValueError("cartan_dimension must be positive")

    reduced_pairing = _fraction_matrix(reduced_pairing_matrix)
    positive_dimension, negative_dimension = _matrix_shape(reduced_pairing)
    if positive_dimension == 0 or negative_dimension == 0:
        raise ValueError("reduced_pairing_matrix must be nonempty")

    triangular_normal_form = _fraction_matrix(triangular_normal_form_matrix)
    double_dimension, triangular_tensor_dimension = _matrix_shape(triangular_normal_form)
    expected_triangular_width = negative_dimension * cartan_dimension * positive_dimension
    if triangular_tensor_dimension != expected_triangular_width:
        raise ValueError(
            "triangular_normal_form_matrix width must equal "
            "negative_dimension * cartan_dimension * positive_dimension"
        )

    mixed_product = _fraction_matrix(mixed_product_matrix)
    drinfeld_cross_relation = _fraction_matrix(drinfeld_cross_relation_matrix)
    mixed_domain_dimension = negative_dimension * positive_dimension
    _validate_matrix_shape(
        mixed_product,
        (double_dimension, mixed_domain_dimension),
        "mixed_product_matrix",
    )
    _validate_matrix_shape(
        drinfeld_cross_relation,
        (double_dimension, mixed_domain_dimension),
        "drinfeld_cross_relation_matrix",
    )

    coproduct_coassociator_defect = _fraction_matrix(coproduct_coassociator_defect_matrix)
    associator_pentagon_defect = _fraction_matrix(associator_pentagon_defect_matrix)
    center_compatibility_defect = _fraction_matrix(center_compatibility_defect_matrix)
    cross_relation_defect = _matrix_difference(mixed_product, drinfeld_cross_relation)

    triangular_rank = exact_matrix_rank(triangular_normal_form)
    pairing_rank = exact_matrix_rank(reduced_pairing)
    cross_relation_rank = exact_matrix_rank(cross_relation_defect)
    coproduct_coassociator_rank = exact_matrix_rank(coproduct_coassociator_defect)
    associator_pentagon_rank = exact_matrix_rank(associator_pentagon_defect)
    center_compatibility_rank = exact_matrix_rank(center_compatibility_defect)

    triangular_isomorphism = (
        double_dimension == triangular_tensor_dimension
        and triangular_rank == double_dimension
    )
    pairing_nondegenerate = (
        positive_dimension == negative_dimension
        and pairing_rank == positive_dimension
    )
    cross_relation_compatible = cross_relation_rank == 0
    coproduct_coassociative = coproduct_coassociator_rank == 0
    associator_pentagon_compatible = associator_pentagon_rank == 0
    center_compatible = center_compatibility_rank == 0
    closed = (
        triangular_isomorphism
        and pairing_nondegenerate
        and cross_relation_compatible
        and coproduct_coassociative
        and associator_pentagon_compatible
        and center_compatible
    )

    return FiniteDrinfeldDoubleDatumGate(
        finite_height=finite_height,
        positive_dimension=positive_dimension,
        negative_dimension=negative_dimension,
        cartan_dimension=cartan_dimension,
        double_dimension=double_dimension,
        triangular_tensor_dimension=triangular_tensor_dimension,
        triangular_normal_form_rank=triangular_rank,
        pairing_rank=pairing_rank,
        cross_relation_defect_matrix=cross_relation_defect,
        coproduct_coassociator_defect_matrix=coproduct_coassociator_defect,
        associator_pentagon_defect_matrix=associator_pentagon_defect,
        center_compatibility_defect_matrix=center_compatibility_defect,
        cross_relation_defect_rank=cross_relation_rank,
        coproduct_coassociator_defect_rank=coproduct_coassociator_rank,
        associator_pentagon_defect_rank=associator_pentagon_rank,
        center_compatibility_defect_rank=center_compatibility_rank,
        triangular_normal_form_isomorphism=triangular_isomorphism,
        reduced_pairing_nondegenerate=pairing_nondegenerate,
        cross_relation_compatible=cross_relation_compatible,
        coproduct_coassociative=coproduct_coassociative,
        associator_pentagon_compatible=associator_pentagon_compatible,
        center_compatible=center_compatible,
        closed=closed,
        status=(
            "FINITE_DRINFELD_DOUBLE_DATUM_GATE"
            if closed
            else "FINITE_DRINFELD_DOUBLE_DATUM_DEFECT"
        ),
    )


def _finite_projection_idempotence_defect(projection: Matrix) -> Matrix:
    return _matrix_difference(_matrix_product(projection, projection), projection)


def finite_compact_hall_product_gate(
    finite_height: int,
    *,
    product_12_matrix: Iterable[Iterable[Any]],
    product_23_matrix: Iterable[Iterable[Any]],
    product_12_then_3_matrix: Iterable[Iterable[Any]],
    product_1_then_23_matrix: Iterable[Iterable[Any]],
    thom_sebastiani_left_matrix: Iterable[Iterable[Any]],
    thom_sebastiani_right_matrix: Iterable[Iterable[Any]],
    orientation_left_matrix: Iterable[Iterable[Any]],
    orientation_right_matrix: Iterable[Iterable[Any]],
    support_1_projection_matrix: Iterable[Iterable[Any]],
    support_2_projection_matrix: Iterable[Iterable[Any]],
    support_3_projection_matrix: Iterable[Iterable[Any]],
    support_12_projection_matrix: Iterable[Iterable[Any]],
    support_23_projection_matrix: Iterable[Iterable[Any]],
    support_123_projection_matrix: Iterable[Iterable[Any]],
) -> FiniteCompactHallProductGate:
    r"""Check a finite compact Hall product associativity packet.

    The four product matrices represent
    m_12, m_23, m_{12,3}, and m_{1,23}.  The two-step compact Hall
    product is associative exactly when
    m_{12,3}(m_12 \otimes 1) = m_{1,23}(1 \otimes m_23), after the
    supplied Thom-Sebastiani and orientation transports also agree and
    all product maps preserve the retained compact-support summands.
    """
    if finite_height <= 0:
        raise ValueError("finite_height must be positive")

    support_1 = _fraction_matrix(support_1_projection_matrix)
    support_2 = _fraction_matrix(support_2_projection_matrix)
    support_3 = _fraction_matrix(support_3_projection_matrix)
    support_12 = _fraction_matrix(support_12_projection_matrix)
    support_23 = _fraction_matrix(support_23_projection_matrix)
    support_123 = _fraction_matrix(support_123_projection_matrix)
    support_matrices = (
        support_1,
        support_2,
        support_3,
        support_12,
        support_23,
        support_123,
    )
    support_names = (
        "support_1_projection_matrix",
        "support_2_projection_matrix",
        "support_3_projection_matrix",
        "support_12_projection_matrix",
        "support_23_projection_matrix",
        "support_123_projection_matrix",
    )
    for name, projection in zip(support_names, support_matrices):
        height, width = _matrix_shape(projection)
        if height != width:
            raise ValueError(f"{name} must be square")

    dim_1 = _matrix_width(support_1)
    dim_2 = _matrix_width(support_2)
    dim_3 = _matrix_width(support_3)
    dim_12 = _matrix_width(support_12)
    dim_23 = _matrix_width(support_23)
    dim_123 = _matrix_width(support_123)

    product_12 = _fraction_matrix(product_12_matrix)
    product_23 = _fraction_matrix(product_23_matrix)
    product_12_then_3 = _fraction_matrix(product_12_then_3_matrix)
    product_1_then_23 = _fraction_matrix(product_1_then_23_matrix)
    _validate_matrix_shape(
        product_12,
        (dim_12, dim_1 * dim_2),
        "product_12_matrix",
    )
    _validate_matrix_shape(
        product_23,
        (dim_23, dim_2 * dim_3),
        "product_23_matrix",
    )
    _validate_matrix_shape(
        product_12_then_3,
        (dim_123, dim_12 * dim_3),
        "product_12_then_3_matrix",
    )
    _validate_matrix_shape(
        product_1_then_23,
        (dim_123, dim_1 * dim_23),
        "product_1_then_23_matrix",
    )

    identity_1 = _identity_matrix(dim_1)
    identity_3 = _identity_matrix(dim_3)
    left_product = _matrix_product(
        product_12_then_3,
        _matrix_kronecker_product(product_12, identity_3),
    )
    right_product = _matrix_product(
        product_1_then_23,
        _matrix_kronecker_product(identity_1, product_23),
    )
    product_associator_defect = _matrix_difference(left_product, right_product)

    thom_sebastiani_left = _fraction_matrix(thom_sebastiani_left_matrix)
    thom_sebastiani_right = _fraction_matrix(thom_sebastiani_right_matrix)
    orientation_left = _fraction_matrix(orientation_left_matrix)
    orientation_right = _fraction_matrix(orientation_right_matrix)
    expected_transport_shape = _matrix_shape(left_product)
    _validate_matrix_shape(
        thom_sebastiani_left,
        expected_transport_shape,
        "thom_sebastiani_left_matrix",
    )
    _validate_matrix_shape(
        thom_sebastiani_right,
        expected_transport_shape,
        "thom_sebastiani_right_matrix",
    )
    _validate_matrix_shape(
        orientation_left,
        expected_transport_shape,
        "orientation_left_matrix",
    )
    _validate_matrix_shape(
        orientation_right,
        expected_transport_shape,
        "orientation_right_matrix",
    )
    thom_sebastiani_defect = _matrix_difference(
        thom_sebastiani_left,
        thom_sebastiani_right,
    )
    orientation_defect = _matrix_difference(orientation_left, orientation_right)

    support_projection_defects = tuple(
        _finite_projection_idempotence_defect(projection)
        for projection in support_matrices
    )
    support_intertwining_defects = (
        _finite_projection_intertwining_defect(
            support_12,
            product_12,
            _matrix_kronecker_product(support_1, support_2),
        ),
        _finite_projection_intertwining_defect(
            support_23,
            product_23,
            _matrix_kronecker_product(support_2, support_3),
        ),
        _finite_projection_intertwining_defect(
            support_123,
            product_12_then_3,
            _matrix_kronecker_product(support_12, support_3),
        ),
        _finite_projection_intertwining_defect(
            support_123,
            product_1_then_23,
            _matrix_kronecker_product(support_1, support_23),
        ),
    )

    product_associator_rank = exact_matrix_rank(product_associator_defect)
    thom_sebastiani_rank = exact_matrix_rank(thom_sebastiani_defect)
    orientation_rank = exact_matrix_rank(orientation_defect)
    support_projection_ranks = tuple(
        exact_matrix_rank(defect) for defect in support_projection_defects
    )
    support_intertwining_ranks = tuple(
        exact_matrix_rank(defect) for defect in support_intertwining_defects
    )
    product_associative = product_associator_rank == 0
    thom_sebastiani_associative = thom_sebastiani_rank == 0
    orientation_associative = orientation_rank == 0
    compact_support_compatible = (
        all(rank == 0 for rank in support_projection_ranks)
        and all(rank == 0 for rank in support_intertwining_ranks)
    )
    closed = (
        product_associative
        and thom_sebastiani_associative
        and orientation_associative
        and compact_support_compatible
    )

    return FiniteCompactHallProductGate(
        finite_height=finite_height,
        input_dimensions=(dim_1, dim_2, dim_3),
        intermediate_dimensions=(dim_12, dim_23),
        target_dimension=dim_123,
        left_product_matrix=left_product,
        right_product_matrix=right_product,
        product_associator_defect_matrix=product_associator_defect,
        thom_sebastiani_defect_matrix=thom_sebastiani_defect,
        orientation_defect_matrix=orientation_defect,
        support_projection_defect_matrices=support_projection_defects,
        support_intertwining_defect_matrices=support_intertwining_defects,
        product_associator_defect_rank=product_associator_rank,
        thom_sebastiani_defect_rank=thom_sebastiani_rank,
        orientation_defect_rank=orientation_rank,
        support_projection_defect_ranks=support_projection_ranks,
        support_intertwining_defect_ranks=support_intertwining_ranks,
        product_associative=product_associative,
        thom_sebastiani_associative=thom_sebastiani_associative,
        orientation_associative=orientation_associative,
        compact_support_compatible=compact_support_compatible,
        closed=closed,
        status=(
            "FINITE_COMPACT_HALL_PRODUCT_GATE"
            if closed
            else "FINITE_COMPACT_HALL_PRODUCT_DEFECT"
        ),
    )


def finite_total_cech_ran_maurer_cartan_gate(
    finite_bound: int,
    *,
    total_differential_matrix: Iterable[Iterable[Any]],
    theta_vector: Iterable[Any],
    half_bracket_vector: Iterable[Any],
    obstruction_vector: Optional[Iterable[Any]] = None,
    primitive_vector: Optional[Iterable[Any]] = None,
) -> FiniteTotalCechRanMaurerCartanGate:
    r"""Check the finite total Cech/Ran convolution Maurer-Cartan equation.

    The half_bracket_vector is the evaluated term 1/2[theta, theta] in
    the chosen finite total-convolution basis.  If obstruction_vector
    and primitive_vector are both supplied, the gate also checks that the
    obstruction is a cocycle and that the primitive kills it.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    differential = _fraction_matrix(total_differential_matrix)
    total_dimension, differential_width = _matrix_shape(differential)
    if total_dimension != differential_width:
        raise ValueError("total_differential_matrix must be square")
    theta = _fraction_vector(theta_vector)
    half_bracket = _fraction_vector(half_bracket_vector)
    if len(theta) != total_dimension:
        raise ValueError("theta_vector must have total dimension")
    if len(half_bracket) != total_dimension:
        raise ValueError("half_bracket_vector must have total dimension")

    differential_square = _matrix_product(differential, differential)
    differential_after_theta = _matrix_vector_product(differential, theta)
    maurer_cartan_defect = _vector_sum(differential_after_theta, half_bracket)
    differential_square_rank = exact_matrix_rank(differential_square)
    maurer_cartan_rank = _column_vector_rank((maurer_cartan_defect,))

    primitive_data_flags = (obstruction_vector is not None, primitive_vector is not None)
    if any(primitive_data_flags) and not all(primitive_data_flags):
        raise ValueError("obstruction_vector and primitive_vector must be supplied together")
    if all(primitive_data_flags):
        obstruction = _fraction_vector(obstruction_vector or ())
        primitive = _fraction_vector(primitive_vector or ())
        if len(obstruction) != total_dimension:
            raise ValueError("obstruction_vector must have total dimension")
        if len(primitive) != total_dimension:
            raise ValueError("primitive_vector must have total dimension")
        obstruction_cocycle = _matrix_vector_product(differential, obstruction)
        primitive_boundary = _matrix_vector_product(differential, primitive)
        primitive_defect = _vector_difference(primitive_boundary, obstruction)
        primitive_data_supplied = True
    else:
        obstruction = ()
        primitive = ()
        obstruction_cocycle = ()
        primitive_boundary = ()
        primitive_defect = ()
        primitive_data_supplied = False

    obstruction_cocycle_rank = _column_vector_rank((obstruction_cocycle,))
    primitive_rank = _column_vector_rank((primitive_defect,))
    differential_closed = differential_square_rank == 0
    maurer_cartan_closed = maurer_cartan_rank == 0
    primitive_closes = (
        primitive_data_supplied
        and obstruction_cocycle_rank == 0
        and primitive_rank == 0
    )
    closed = (
        differential_closed
        and maurer_cartan_closed
        and (not primitive_data_supplied or primitive_closes)
    )

    return FiniteTotalCechRanMaurerCartanGate(
        finite_bound=finite_bound,
        total_dimension=total_dimension,
        differential_square_matrix=differential_square,
        theta_vector=theta,
        half_bracket_vector=half_bracket,
        differential_after_theta=differential_after_theta,
        maurer_cartan_defect_vector=maurer_cartan_defect,
        obstruction_vector=obstruction,
        primitive_vector=primitive,
        obstruction_cocycle_vector=obstruction_cocycle,
        primitive_boundary_vector=primitive_boundary,
        primitive_defect_vector=primitive_defect,
        differential_square_defect_rank=differential_square_rank,
        maurer_cartan_defect_rank=maurer_cartan_rank,
        obstruction_cocycle_defect_rank=obstruction_cocycle_rank,
        primitive_defect_rank=primitive_rank,
        primitive_data_supplied=primitive_data_supplied,
        differential_closed=differential_closed,
        maurer_cartan_closed=maurer_cartan_closed,
        primitive_closes_obstruction=primitive_closes,
        closed=closed,
        status=(
            "FINITE_TOTAL_CECH_RAN_MAURER_CARTAN_GATE"
            if closed
            else "FINITE_TOTAL_CECH_RAN_MAURER_CARTAN_DEFECT"
        ),
    )


def finite_cyclic_sdr_block_compatibility_gate(
    finite_bound: int,
    *,
    ambient_differential_matrix: Iterable[Iterable[Any]],
    model_differential_matrix: Iterable[Iterable[Any]],
    inclusion_matrix: Iterable[Iterable[Any]],
    projection_matrix: Iterable[Iterable[Any]],
    homotopy_matrix: Iterable[Iterable[Any]],
    cyclic_pairing_matrix: Iterable[Iterable[Any]],
    expected_block_homotopy_matrix: Iterable[Iterable[Any]],
    total_action_matrix: Iterable[Iterable[Any]],
    split_action_matrix: Iterable[Iterable[Any]],
    action_boundary_matrix: Iterable[Iterable[Any]],
    off_hessian_matrix: Iterable[Iterable[Any]],
    odd_contraction_matrix: Iterable[Iterable[Any]],
    source_product_matrix: Iterable[Iterable[Any]],
    target_product_matrix: Iterable[Iterable[Any]],
    left_theta_matrix: Iterable[Iterable[Any]],
    right_theta_matrix: Iterable[Iterable[Any]],
    union_theta_matrix: Iterable[Iterable[Any]],
    rees_euler_matrix: Iterable[Iterable[Any]],
) -> FiniteCyclicSDRBlockCompatibilityGate:
    r"""Check finite cyclic SDR block compatibility and Hall multiplicativity.

    The finite SDR data are checked by the identities p i = 1,
    d i = i d, p d = d p, and i p + d h + h d = 1.  Cyclicity is the
    skew-adjointness equation h^t omega + omega h = 0.  The block and
    action conditions record that the supplied homotopy is the block
    homotopy and that the transferred action differs from the split
    action by the supplied boundary.  The product condition is the
    Euler-corrected Hall equation
    E m_T(theta_left tensor theta_right) = theta_union m_S.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    ambient_differential = _fraction_matrix(ambient_differential_matrix)
    model_differential = _fraction_matrix(model_differential_matrix)
    inclusion = _fraction_matrix(inclusion_matrix)
    projection = _fraction_matrix(projection_matrix)
    homotopy = _fraction_matrix(homotopy_matrix)
    pairing = _fraction_matrix(cyclic_pairing_matrix)
    expected_block_homotopy = _fraction_matrix(expected_block_homotopy_matrix)

    ambient_dimension, ambient_width = _matrix_shape(ambient_differential)
    model_dimension, model_width = _matrix_shape(model_differential)
    if ambient_dimension != ambient_width:
        raise ValueError("ambient_differential_matrix must be square")
    if model_dimension != model_width:
        raise ValueError("model_differential_matrix must be square")
    _validate_matrix_shape(inclusion, (ambient_dimension, model_dimension), "inclusion_matrix")
    _validate_matrix_shape(projection, (model_dimension, ambient_dimension), "projection_matrix")
    _validate_matrix_shape(homotopy, (ambient_dimension, ambient_dimension), "homotopy_matrix")
    _validate_matrix_shape(pairing, (ambient_dimension, ambient_dimension), "cyclic_pairing_matrix")
    _validate_matrix_shape(
        expected_block_homotopy,
        (ambient_dimension, ambient_dimension),
        "expected_block_homotopy_matrix",
    )

    retraction_defect = _matrix_difference(
        _matrix_product(projection, inclusion),
        _identity_matrix(model_dimension),
    )
    inclusion_chain_defect = _matrix_difference(
        _matrix_product(ambient_differential, inclusion),
        _matrix_product(inclusion, model_differential),
    )
    projection_chain_defect = _matrix_difference(
        _matrix_product(projection, ambient_differential),
        _matrix_product(model_differential, projection),
    )
    homotopy_defect = _matrix_difference(
        _matrix_sum(
            _matrix_product(inclusion, projection),
            _matrix_sum(
                _matrix_product(ambient_differential, homotopy),
                _matrix_product(homotopy, ambient_differential),
            ),
        ),
        _identity_matrix(ambient_dimension),
    )
    cyclicity_defect = _matrix_sum(
        _matrix_product(_matrix_transpose(homotopy), pairing),
        _matrix_product(pairing, homotopy),
    )
    block_homotopy_defect = _matrix_difference(homotopy, expected_block_homotopy)

    total_action = _fraction_matrix(total_action_matrix)
    split_action = _fraction_matrix(split_action_matrix)
    action_boundary = _fraction_matrix(action_boundary_matrix)
    transferred_action_defect = _matrix_difference(
        _matrix_difference(total_action, split_action),
        action_boundary,
    )

    off_hessian = _fraction_matrix(off_hessian_matrix)
    odd_contraction = _fraction_matrix(odd_contraction_matrix)
    hessian_dimension, hessian_width = _matrix_shape(off_hessian)
    if hessian_dimension != hessian_width:
        raise ValueError("off_hessian_matrix must be square")
    _validate_matrix_shape(
        odd_contraction,
        (hessian_dimension, hessian_dimension),
        "odd_contraction_matrix",
    )
    hessian_symmetry_defect = _matrix_difference(off_hessian, _matrix_transpose(off_hessian))
    odd_contraction_skew_defect = _matrix_sum(
        odd_contraction,
        _matrix_transpose(odd_contraction),
    )
    hessian_contraction_scalar = sum(
        off_hessian[row][column] * odd_contraction[row][column]
        for row in range(hessian_dimension)
        for column in range(hessian_dimension)
    )
    hessian_contraction_defect_rank = 0 if hessian_contraction_scalar == 0 else 1

    source_product = _fraction_matrix(source_product_matrix)
    target_product = _fraction_matrix(target_product_matrix)
    left_theta = _fraction_matrix(left_theta_matrix)
    right_theta = _fraction_matrix(right_theta_matrix)
    union_theta = _fraction_matrix(union_theta_matrix)
    rees_euler = _fraction_matrix(rees_euler_matrix)

    left_target_dimension, left_source_dimension = _matrix_shape(left_theta)
    right_target_dimension, right_source_dimension = _matrix_shape(right_theta)
    union_target_dimension, union_source_dimension = _matrix_shape(union_theta)
    _validate_matrix_shape(
        source_product,
        (union_source_dimension, left_source_dimension * right_source_dimension),
        "source_product_matrix",
    )
    _validate_matrix_shape(
        target_product,
        (union_target_dimension, left_target_dimension * right_target_dimension),
        "target_product_matrix",
    )
    _validate_matrix_shape(
        rees_euler,
        (union_target_dimension, union_target_dimension),
        "rees_euler_matrix",
    )
    component_theta = _matrix_kronecker_product(left_theta, right_theta)
    target_after_components = _matrix_product(target_product, component_theta)
    euler_product_after_components = _matrix_product(rees_euler, target_after_components)
    union_after_source_product = _matrix_product(union_theta, source_product)
    euler_multiplicativity_defect = _matrix_difference(
        euler_product_after_components,
        union_after_source_product,
    )

    retraction_rank = exact_matrix_rank(retraction_defect)
    inclusion_chain_rank = exact_matrix_rank(inclusion_chain_defect)
    projection_chain_rank = exact_matrix_rank(projection_chain_defect)
    homotopy_rank = exact_matrix_rank(homotopy_defect)
    cyclicity_rank = exact_matrix_rank(cyclicity_defect)
    block_homotopy_rank = exact_matrix_rank(block_homotopy_defect)
    transferred_action_rank = exact_matrix_rank(transferred_action_defect)
    hessian_symmetry_rank = exact_matrix_rank(hessian_symmetry_defect)
    odd_contraction_skew_rank = exact_matrix_rank(odd_contraction_skew_defect)
    multiplicativity_rank = exact_matrix_rank(euler_multiplicativity_defect)

    sdr_closed = (
        retraction_rank == 0
        and inclusion_chain_rank == 0
        and projection_chain_rank == 0
        and homotopy_rank == 0
    )
    cyclic_closed = cyclicity_rank == 0
    block_transfer_closed = block_homotopy_rank == 0 and transferred_action_rank == 0
    hessian_cancellation_closed = (
        hessian_symmetry_rank == 0
        and odd_contraction_skew_rank == 0
        and hessian_contraction_defect_rank == 0
    )
    multiplicative = multiplicativity_rank == 0
    closed = (
        sdr_closed
        and cyclic_closed
        and block_transfer_closed
        and hessian_cancellation_closed
        and multiplicative
    )

    return FiniteCyclicSDRBlockCompatibilityGate(
        finite_bound=finite_bound,
        ambient_dimension=ambient_dimension,
        model_dimension=model_dimension,
        retraction_defect_matrix=retraction_defect,
        inclusion_chain_defect_matrix=inclusion_chain_defect,
        projection_chain_defect_matrix=projection_chain_defect,
        homotopy_defect_matrix=homotopy_defect,
        cyclicity_defect_matrix=cyclicity_defect,
        block_homotopy_defect_matrix=block_homotopy_defect,
        transferred_action_defect_matrix=transferred_action_defect,
        hessian_symmetry_defect_matrix=hessian_symmetry_defect,
        odd_contraction_skew_defect_matrix=odd_contraction_skew_defect,
        hessian_contraction_scalar=hessian_contraction_scalar,
        euler_product_after_components=euler_product_after_components,
        union_after_source_product=union_after_source_product,
        euler_multiplicativity_defect_matrix=euler_multiplicativity_defect,
        retraction_defect_rank=retraction_rank,
        inclusion_chain_defect_rank=inclusion_chain_rank,
        projection_chain_defect_rank=projection_chain_rank,
        homotopy_defect_rank=homotopy_rank,
        cyclicity_defect_rank=cyclicity_rank,
        block_homotopy_defect_rank=block_homotopy_rank,
        transferred_action_defect_rank=transferred_action_rank,
        hessian_symmetry_defect_rank=hessian_symmetry_rank,
        odd_contraction_skew_defect_rank=odd_contraction_skew_rank,
        hessian_contraction_defect_rank=hessian_contraction_defect_rank,
        euler_multiplicativity_defect_rank=multiplicativity_rank,
        sdr_closed=sdr_closed,
        cyclic_closed=cyclic_closed,
        block_transfer_closed=block_transfer_closed,
        hessian_cancellation_closed=hessian_cancellation_closed,
        multiplicative=multiplicative,
        closed=closed,
        status=(
            "FINITE_CYCLIC_SDR_BLOCK_COMPATIBILITY_GATE"
            if closed
            else "FINITE_CYCLIC_SDR_BLOCK_COMPATIBILITY_DEFECT"
        ),
    )


def finite_simplicial_cyclic_contraction_gate(
    finite_bound: int,
    *,
    ambient_differential_matrix: Iterable[Iterable[Any]],
    model_differential_matrix: Iterable[Iterable[Any]],
    inclusion_matrix: Iterable[Iterable[Any]],
    projection_matrix: Iterable[Iterable[Any]],
    homotopy_matrix: Iterable[Iterable[Any]],
    cyclic_pairing_matrix: Iterable[Iterable[Any]],
    face_data: Iterable[Dict[str, Any]] = (),
) -> FiniteSimplicialCyclicContractionGate:
    r"""Check one finite simplicial cyclic contraction and its faces.

    Face packets use the keys ``ambient_restriction_matrix``,
    ``model_restriction_matrix``, ``face_inclusion_matrix``,
    ``face_projection_matrix``, and ``face_homotopy_matrix``.  The face
    equations are R_A i = i_face R_M, R_M p = p_face R_A, and
    R_A h = h_face R_A.
    """
    if finite_bound <= 0:
        raise ValueError("finite_bound must be positive")

    ambient_differential = _fraction_matrix(ambient_differential_matrix)
    model_differential = _fraction_matrix(model_differential_matrix)
    inclusion = _fraction_matrix(inclusion_matrix)
    projection = _fraction_matrix(projection_matrix)
    homotopy = _fraction_matrix(homotopy_matrix)
    pairing = _fraction_matrix(cyclic_pairing_matrix)

    ambient_dimension, ambient_width = _matrix_shape(ambient_differential)
    model_dimension, model_width = _matrix_shape(model_differential)
    if ambient_dimension != ambient_width:
        raise ValueError("ambient_differential_matrix must be square")
    if model_dimension != model_width:
        raise ValueError("model_differential_matrix must be square")
    _validate_matrix_shape(inclusion, (ambient_dimension, model_dimension), "inclusion_matrix")
    _validate_matrix_shape(projection, (model_dimension, ambient_dimension), "projection_matrix")
    _validate_matrix_shape(homotopy, (ambient_dimension, ambient_dimension), "homotopy_matrix")
    _validate_matrix_shape(pairing, (ambient_dimension, ambient_dimension), "cyclic_pairing_matrix")

    retraction_defect = _matrix_difference(
        _matrix_product(projection, inclusion),
        _identity_matrix(model_dimension),
    )
    inclusion_chain_defect = _matrix_difference(
        _matrix_product(ambient_differential, inclusion),
        _matrix_product(inclusion, model_differential),
    )
    projection_chain_defect = _matrix_difference(
        _matrix_product(projection, ambient_differential),
        _matrix_product(model_differential, projection),
    )
    homotopy_defect = _matrix_difference(
        _matrix_sum(
            _matrix_product(inclusion, projection),
            _matrix_sum(
                _matrix_product(ambient_differential, homotopy),
                _matrix_product(homotopy, ambient_differential),
            ),
        ),
        _identity_matrix(ambient_dimension),
    )
    homotopy_square = _matrix_product(homotopy, homotopy)
    homotopy_inclusion = _matrix_product(homotopy, inclusion)
    projection_homotopy = _matrix_product(projection, homotopy)
    cyclicity_defect = _matrix_sum(
        _matrix_product(_matrix_transpose(homotopy), pairing),
        _matrix_product(pairing, homotopy),
    )

    face_reports: List[FiniteSimplicialCyclicContractionFaceReport] = []
    for index, face in enumerate(face_data):
        label = str(face.get("label", f"face_{index}"))
        ambient_restriction = _fraction_matrix(face["ambient_restriction_matrix"])
        model_restriction = _fraction_matrix(face["model_restriction_matrix"])
        face_inclusion = _fraction_matrix(face["face_inclusion_matrix"])
        face_projection = _fraction_matrix(face["face_projection_matrix"])
        face_homotopy = _fraction_matrix(face["face_homotopy_matrix"])

        face_ambient_dimension, face_ambient_width = _matrix_shape(face_homotopy)
        if face_ambient_dimension != face_ambient_width:
            raise ValueError(f"{label} face_homotopy_matrix must be square")
        face_model_dimension = len(face_projection)
        _validate_matrix_shape(
            ambient_restriction,
            (face_ambient_dimension, ambient_dimension),
            f"{label} ambient_restriction_matrix",
        )
        _validate_matrix_shape(
            model_restriction,
            (face_model_dimension, model_dimension),
            f"{label} model_restriction_matrix",
        )
        _validate_matrix_shape(
            face_inclusion,
            (face_ambient_dimension, face_model_dimension),
            f"{label} face_inclusion_matrix",
        )
        _validate_matrix_shape(
            face_projection,
            (face_model_dimension, face_ambient_dimension),
            f"{label} face_projection_matrix",
        )

        inclusion_face_defect = _matrix_difference(
            _matrix_product(ambient_restriction, inclusion),
            _matrix_product(face_inclusion, model_restriction),
        )
        projection_face_defect = _matrix_difference(
            _matrix_product(model_restriction, projection),
            _matrix_product(face_projection, ambient_restriction),
        )
        homotopy_face_defect = _matrix_difference(
            _matrix_product(ambient_restriction, homotopy),
            _matrix_product(face_homotopy, ambient_restriction),
        )
        inclusion_face_rank = exact_matrix_rank(inclusion_face_defect)
        projection_face_rank = exact_matrix_rank(projection_face_defect)
        homotopy_face_rank = exact_matrix_rank(homotopy_face_defect)
        face_reports.append(
            FiniteSimplicialCyclicContractionFaceReport(
                label=label,
                inclusion_face_defect_matrix=inclusion_face_defect,
                projection_face_defect_matrix=projection_face_defect,
                homotopy_face_defect_matrix=homotopy_face_defect,
                inclusion_face_defect_rank=inclusion_face_rank,
                projection_face_defect_rank=projection_face_rank,
                homotopy_face_defect_rank=homotopy_face_rank,
                compatible=(
                    inclusion_face_rank == 0
                    and projection_face_rank == 0
                    and homotopy_face_rank == 0
                ),
            )
        )

    retraction_rank = exact_matrix_rank(retraction_defect)
    inclusion_chain_rank = exact_matrix_rank(inclusion_chain_defect)
    projection_chain_rank = exact_matrix_rank(projection_chain_defect)
    homotopy_rank = exact_matrix_rank(homotopy_defect)
    homotopy_square_rank = exact_matrix_rank(homotopy_square)
    homotopy_inclusion_rank = exact_matrix_rank(homotopy_inclusion)
    projection_homotopy_rank = exact_matrix_rank(projection_homotopy)
    cyclicity_rank = exact_matrix_rank(cyclicity_defect)
    sdr_closed = (
        retraction_rank == 0
        and inclusion_chain_rank == 0
        and projection_chain_rank == 0
        and homotopy_rank == 0
    )
    side_conditions_closed = (
        homotopy_square_rank == 0
        and homotopy_inclusion_rank == 0
        and projection_homotopy_rank == 0
    )
    cyclic_closed = cyclicity_rank == 0
    faces_compatible = all(report.compatible for report in face_reports)
    closed = sdr_closed and side_conditions_closed and cyclic_closed and faces_compatible

    return FiniteSimplicialCyclicContractionGate(
        finite_bound=finite_bound,
        ambient_dimension=ambient_dimension,
        model_dimension=model_dimension,
        retraction_defect_matrix=retraction_defect,
        inclusion_chain_defect_matrix=inclusion_chain_defect,
        projection_chain_defect_matrix=projection_chain_defect,
        homotopy_defect_matrix=homotopy_defect,
        homotopy_square_matrix=homotopy_square,
        homotopy_inclusion_matrix=homotopy_inclusion,
        projection_homotopy_matrix=projection_homotopy,
        cyclicity_defect_matrix=cyclicity_defect,
        face_reports=tuple(face_reports),
        retraction_defect_rank=retraction_rank,
        inclusion_chain_defect_rank=inclusion_chain_rank,
        projection_chain_defect_rank=projection_chain_rank,
        homotopy_defect_rank=homotopy_rank,
        homotopy_square_rank=homotopy_square_rank,
        homotopy_inclusion_rank=homotopy_inclusion_rank,
        projection_homotopy_rank=projection_homotopy_rank,
        cyclicity_defect_rank=cyclicity_rank,
        sdr_closed=sdr_closed,
        side_conditions_closed=side_conditions_closed,
        cyclic_closed=cyclic_closed,
        faces_compatible=faces_compatible,
        closed=closed,
        status=(
            "FINITE_SIMPLICIAL_CYCLIC_CONTRACTION_GATE"
            if closed
            else "FINITE_SIMPLICIAL_CYCLIC_CONTRACTION_DEFECT"
        ),
    )


def _charge_pair_key(key: Iterable[str]) -> Tuple[str, str]:
    key_tuple = tuple(str(entry) for entry in key)
    if len(key_tuple) != 2:
        raise ValueError("charge-pair keys must be pairs")
    return key_tuple  # type: ignore[return-value]


def finite_scattering_quantum_torus_gate(
    charges: Iterable[str],
    charge_heights: Dict[str, int],
    pairings: Dict[Tuple[str, str], Any],
    charge_sums: Dict[Tuple[str, str], Optional[str]],
    height_cutoff: int,
) -> FiniteScatteringQuantumTorusGate:
    r"""Check the finite truncated quantum-torus product on charge labels.

    The product is x_a x_b = q^{<a,b>} x_{a+b} when the supplied sum
    remains in the height window, and zero otherwise.  The gate checks
    that the pairing is skew, the supplied sum table respects height
    truncation, and the finite product is associative with the expected
    cocycle exponent identity.  It does not construct motivic integration
    or the KS wall product.
    """
    if height_cutoff <= 0:
        raise ValueError("height_cutoff must be positive")
    charge_tuple = tuple(str(charge) for charge in charges)
    if len(set(charge_tuple)) != len(charge_tuple):
        raise ValueError("charges must be distinct")
    charge_set = set(charge_tuple)
    missing_heights = sorted(charge_set - set(charge_heights))
    if missing_heights:
        raise ValueError(f"missing charge heights: {missing_heights}")
    if any(charge_heights[charge] <= 0 for charge in charge_tuple):
        raise ValueError("charge heights must be positive")

    normalized_pairings = {
        _charge_pair_key(key): Fraction(value)
        for key, value in pairings.items()
    }
    normalized_sums = {
        _charge_pair_key(key): (None if value is None else str(value))
        for key, value in charge_sums.items()
    }

    product_rows: List[FiniteScatteringQuantumTorusProductRow] = []
    missing_pairings = []
    missing_sums = []
    skew_defects = []
    height_defects = []
    truncation_defects = []

    for left in charge_tuple:
        if charge_heights[left] > height_cutoff:
            truncation_defects.append(f"{left}:height {charge_heights[left]}>H")
        for right in charge_tuple:
            pair_key = (left, right)
            exponent = normalized_pairings.get(pair_key)
            if exponent is None:
                missing_pairings.append(f"{left},{right}")
            supplied_sum = normalized_sums.get(pair_key, "__missing__")
            if supplied_sum == "__missing__":
                missing_sums.append(f"{left},{right}")
                row_sum = None
                retained = False
            else:
                row_sum = supplied_sum
                retained = row_sum is not None
                sum_height = charge_heights[left] + charge_heights[right]
                if row_sum is None:
                    if sum_height <= height_cutoff:
                        truncation_defects.append(f"{left},{right}:killed inside H")
                elif row_sum not in charge_set:
                    truncation_defects.append(f"{left},{right}:unknown sum {row_sum}")
                else:
                    if charge_heights[row_sum] != sum_height:
                        height_defects.append(
                            f"{left},{right}:{row_sum}:{charge_heights[row_sum]}!={sum_height}"
                        )
                    if sum_height > height_cutoff or charge_heights[row_sum] > height_cutoff:
                        truncation_defects.append(f"{left},{right}:{row_sum} survives above H")
            product_rows.append(
                FiniteScatteringQuantumTorusProductRow(
                    left_charge=left,
                    right_charge=right,
                    left_height=charge_heights[left],
                    right_height=charge_heights[right],
                    supplied_sum=row_sum,
                    retained=retained,
                    exponent=exponent,
                )
            )

    for index, left in enumerate(charge_tuple):
        diagonal = normalized_pairings.get((left, left))
        if diagonal is not None and diagonal != 0:
            skew_defects.append(f"{left},{left}:{diagonal}")
        for right in charge_tuple[index + 1:]:
            left_right = normalized_pairings.get((left, right))
            right_left = normalized_pairings.get((right, left))
            if left_right is not None and right_left is not None and left_right + right_left != 0:
                skew_defects.append(f"{left},{right}:{left_right}+{right_left}")

    def product_sum(left: str, right: str) -> Optional[str]:
        return normalized_sums.get((left, right))

    def pairing_value(left: str, right: str) -> Optional[Fraction]:
        return normalized_pairings.get((left, right))

    associativity_defects = []
    cocycle_defects = []
    for left in charge_tuple:
        for middle in charge_tuple:
            for right in charge_tuple:
                left_middle = product_sum(left, middle)
                middle_right = product_sum(middle, right)
                left_label = None if left_middle is None else product_sum(left_middle, right)
                right_label = None if middle_right is None else product_sum(left, middle_right)
                if left_label != right_label:
                    associativity_defects.append(
                        f"{left},{middle},{right}:{left_label}!={right_label}"
                    )
                    continue
                if left_label is None:
                    continue
                first = pairing_value(left, middle)
                second = pairing_value(left_middle, right) if left_middle is not None else None
                third = pairing_value(middle, right)
                fourth = pairing_value(left, middle_right) if middle_right is not None else None
                if None in (first, second, third, fourth):
                    continue
                left_exponent = first + second  # type: ignore[operator]
                right_exponent = third + fourth  # type: ignore[operator]
                if left_exponent != right_exponent:
                    cocycle_defects.append(
                        f"{left},{middle},{right}:{left_exponent}!={right_exponent}"
                    )

    closed = not (
        missing_pairings
        or missing_sums
        or skew_defects
        or height_defects
        or truncation_defects
        or associativity_defects
        or cocycle_defects
    )
    return FiniteScatteringQuantumTorusGate(
        height_cutoff=height_cutoff,
        charges=charge_tuple,
        product_rows=tuple(product_rows),
        missing_pairings=tuple(sorted(set(missing_pairings))),
        missing_sums=tuple(sorted(set(missing_sums))),
        skew_defects=tuple(skew_defects),
        height_defects=tuple(height_defects),
        truncation_defects=tuple(truncation_defects),
        associativity_defects=tuple(associativity_defects),
        cocycle_defects=tuple(cocycle_defects),
        closed=closed,
        status="FINITE_SCATTERING_QUANTUM_TORUS_GATE" if closed else "FINITE_SCATTERING_QUANTUM_TORUS_DEFECT",
    )


def finite_scattering_root_report(
    charge_discriminants: Dict[str, int],
    bps_indices: Dict[str, int],
    height_cutoff: int,
    *,
    charge_heights: Dict[str, int] | None = None,
    borcherds_coefficients: Dict[int, int] | None = None,
    lower_height_cutoff: int | None = None,
) -> FiniteScatteringRootReport:
    """Check the finite scattering exponents against Borcherds exponents."""
    if height_cutoff <= 0:
        raise ValueError("height_cutoff must be positive")
    if lower_height_cutoff is not None:
        if lower_height_cutoff <= 0:
            raise ValueError("lower_height_cutoff must be positive")
        if lower_height_cutoff > height_cutoff:
            raise ValueError("lower_height_cutoff cannot exceed height_cutoff")
    if charge_heights is None:
        charge_heights = {charge: index + 1 for index, charge in enumerate(charge_discriminants)}
    missing_height = sorted(set(charge_discriminants) - set(charge_heights))
    if missing_height:
        raise ValueError(f"missing charge heights: {missing_height}")
    if any(height <= 0 for height in charge_heights.values()):
        raise ValueError("charge heights must be positive")

    if borcherds_coefficients is None:
        max_discriminant = max((D for D in charge_discriminants.values() if D >= 0), default=0)
        borcherds_coefficients = _bar.k3e_product_by_discriminant(max_discriminant)

    rows = []
    for charge in sorted(charge_discriminants, key=lambda key: (charge_heights[key], charge_discriminants[key], key)):
        height = charge_heights[charge]
        if height > height_cutoff:
            continue
        discriminant = charge_discriminants[charge]
        bps_index = bps_indices.get(charge, 0)
        borcherds_exponent = borcherds_coefficients.get(discriminant, 0)
        rows.append(
            FiniteScatteringRootRow(
                charge=charge,
                height=height,
                discriminant=discriminant,
                bps_index=bps_index,
                borcherds_exponent=borcherds_exponent,
                exponent_match=bps_index == borcherds_exponent,
            )
        )

    scattering_support = tuple(row.charge for row in rows if row.bps_index != 0)
    borcherds_support = tuple(row.charge for row in rows if row.borcherds_exponent != 0)
    scattering_support_set = set(scattering_support)
    borcherds_support_set = set(borcherds_support)
    missing_support = tuple(row.charge for row in rows if row.charge in borcherds_support_set - scattering_support_set)
    extra_support = tuple(row.charge for row in rows if row.charge in scattering_support_set - borcherds_support_set)
    exponent_defects = tuple(row.charge for row in rows if not row.exponent_match)

    transition_commutes = True
    if lower_height_cutoff is not None:
        lower = finite_scattering_root_report(
            charge_discriminants,
            bps_indices,
            lower_height_cutoff,
            charge_heights=charge_heights,
            borcherds_coefficients=borcherds_coefficients,
        )
        projected = tuple(row for row in rows if row.height <= lower_height_cutoff)
        projected_key = tuple(
            (row.charge, row.height, row.discriminant, row.bps_index, row.borcherds_exponent)
            for row in projected
        )
        lower_key = tuple(
            (row.charge, row.height, row.discriminant, row.bps_index, row.borcherds_exponent)
            for row in lower.rows
        )
        transition_commutes = projected_key == lower_key

    closed = not missing_support and not extra_support and not exponent_defects and transition_commutes
    return FiniteScatteringRootReport(
        height_cutoff=height_cutoff,
        rows=tuple(rows),
        scattering_support=scattering_support,
        borcherds_support=borcherds_support,
        missing_support=missing_support,
        extra_support=extra_support,
        exponent_defects=exponent_defects,
        transition_commutes=transition_commutes,
        closed=closed,
        status=(
            "FINITE_SCATTERING_ROOT_COMPARISON"
            if closed
            else "FINITE_SCATTERING_ROOT_DEFECT"
        ),
    )


def bar_witness(max_degree: int = 5) -> BarWitness:
    r"""Rank-one bar witness and the finite-height K3 x E exponent data."""
    root_mults = _bar.k3e_root_multiplicities_1d(max_degree)
    values = [root_mults[(n,)] for n in range(1, max_degree + 1)]
    return BarWitness(
        max_degree=max_degree,
        rank1_root_multiplicities=root_mults,
        rank1_values_constant_24=all(v == 24 for v in values),
        rank1_values=values,
        bar_product_discriminants=_bar.k3e_product_by_discriminant(max_degree * 4),
        status="witnessed at finite degree",
    )


def finite_bar_lattice_grading_report(
    charge_coordinates: Dict[str, Iterable[Any]],
    expected_discriminants: Dict[str, Any],
    height_cutoff: int,
    *,
    charge_heights: Dict[str, int] | None = None,
    simple_root_gram: Iterable[Iterable[Any]] = (
        (2, -2, -2),
        (-2, 2, -2),
        (-2, -2, 2),
    ),
    lower_height_cutoff: int | None = None,
) -> FiniteBarLatticeGradingReport:
    r"""Check that supplied finite bar charges are BKM-lattice degrees.

    In the real-simple-root basis the BKM discriminant convention is
    \(D(v)=-\frac12(v,v)\).  This verifies supplied finite charge data;
    it does not construct the bar grading on the framed algebra.
    """
    if height_cutoff <= 0:
        raise ValueError("height_cutoff must be positive")
    if lower_height_cutoff is not None:
        if lower_height_cutoff <= 0:
            raise ValueError("lower_height_cutoff must be positive")
        if lower_height_cutoff > height_cutoff:
            raise ValueError("lower_height_cutoff cannot exceed height_cutoff")
    gram = _fraction_matrix(simple_root_gram)
    height, width = _matrix_shape(gram)
    if height == 0 or width == 0:
        raise ValueError("simple_root_gram must be nonempty")
    if height != width:
        raise ValueError("simple_root_gram must be square")
    if any(gram[i][j] != gram[j][i] for i in range(height) for j in range(width)):
        raise ValueError("simple_root_gram must be symmetric")
    if charge_heights is None:
        charge_heights = {charge: index + 1 for index, charge in enumerate(charge_coordinates)}
    missing_height = sorted(set(charge_coordinates) - set(charge_heights))
    if missing_height:
        raise ValueError(f"missing charge heights: {missing_height}")
    missing_discriminants = sorted(set(charge_coordinates) - set(expected_discriminants))
    if missing_discriminants:
        raise ValueError(f"missing expected discriminants: {missing_discriminants}")
    if any(level <= 0 for level in charge_heights.values()):
        raise ValueError("charge heights must be positive")

    rows: List[FiniteBarLatticeGradingRow] = []
    for charge in sorted(charge_coordinates, key=lambda key: (charge_heights[key], key)):
        level = charge_heights[charge]
        if level > height_cutoff:
            continue
        coordinates = _fraction_vector(charge_coordinates[charge])
        if len(coordinates) != width:
            raise ValueError(f"charge {charge} has incompatible coordinate length")
        norm = sum(
            coordinates[i] * gram[i][j] * coordinates[j]
            for i in range(width)
            for j in range(width)
        )
        computed_discriminant = -norm / 2
        expected = Fraction(expected_discriminants[charge])
        integral = all(entry.denominator == 1 for entry in coordinates)
        rows.append(
            FiniteBarLatticeGradingRow(
                charge=charge,
                height=level,
                coordinates=coordinates,
                norm=norm,
                computed_discriminant=computed_discriminant,
                expected_discriminant=expected,
                integral_coordinates=integral,
                discriminant_match=computed_discriminant == expected,
            )
        )

    integrality_defects = tuple(row.charge for row in rows if not row.integral_coordinates)
    discriminant_defects = tuple(row.charge for row in rows if not row.discriminant_match)
    transition_commutes = True
    if lower_height_cutoff is not None:
        lower = finite_bar_lattice_grading_report(
            charge_coordinates,
            expected_discriminants,
            lower_height_cutoff,
            charge_heights=charge_heights,
            simple_root_gram=gram,
        )
        projected_key = tuple(
            (
                row.charge,
                row.height,
                row.coordinates,
                row.norm,
                row.computed_discriminant,
                row.expected_discriminant,
            )
            for row in rows
            if row.height <= lower_height_cutoff
        )
        lower_key = tuple(
            (
                row.charge,
                row.height,
                row.coordinates,
                row.norm,
                row.computed_discriminant,
                row.expected_discriminant,
            )
            for row in lower.rows
        )
        transition_commutes = projected_key == lower_key

    closed = not integrality_defects and not discriminant_defects and transition_commutes
    return FiniteBarLatticeGradingReport(
        height_cutoff=height_cutoff,
        simple_root_gram=gram,
        rows=tuple(rows),
        integrality_defects=integrality_defects,
        discriminant_defects=discriminant_defects,
        transition_commutes=transition_commutes,
        closed=closed,
        status=(
            "FINITE_BAR_LATTICE_GRADING_MATCH"
            if closed
            else "FINITE_BAR_LATTICE_GRADING_DEFECT"
        ),
    )


def finite_bar_ce_chain_map_gate(
    height_cutoff: int,
    *,
    source_differential_matrix: Iterable[Iterable[Any]],
    target_differential_matrix: Iterable[Iterable[Any]],
    comparison_degree1_matrix: Iterable[Iterable[Any]],
    comparison_degree2_matrix: Iterable[Iterable[Any]],
) -> FiniteBarCEChainMapGate:
    r"""Check the finite length-two bar/CE chain-map square.

    The source differential maps the finite bar length-two piece to the
    length-one piece.  The target differential maps CE length two to CE
    length one.  The comparison maps F_1 and F_2 form a finite chain map
    precisely when F_1 d_B = d_CE F_2.  This function does not construct
    the bar complex, the CE complex, or the filtered comparison morphism.
    """
    if height_cutoff <= 0:
        raise ValueError("height_cutoff must be positive")

    source_differential = _fraction_matrix(source_differential_matrix)
    target_differential = _fraction_matrix(target_differential_matrix)
    comparison_degree1 = _fraction_matrix(comparison_degree1_matrix)
    comparison_degree2 = _fraction_matrix(comparison_degree2_matrix)

    source_degree1_dimension, source_degree2_dimension = _matrix_shape(source_differential)
    target_degree1_dimension, target_degree2_dimension = _matrix_shape(target_differential)
    _validate_matrix_shape(
        comparison_degree1,
        (target_degree1_dimension, source_degree1_dimension),
        "comparison_degree1_matrix",
    )
    _validate_matrix_shape(
        comparison_degree2,
        (target_degree2_dimension, source_degree2_dimension),
        "comparison_degree2_matrix",
    )

    comparison_after_bar = _matrix_product(comparison_degree1, source_differential)
    ce_after_comparison = _matrix_product(target_differential, comparison_degree2)
    commutator = _matrix_difference(comparison_after_bar, ce_after_comparison)
    defect_rank = exact_matrix_rank(commutator)
    chain_map = defect_rank == 0

    return FiniteBarCEChainMapGate(
        height_cutoff=height_cutoff,
        source_degree1_dimension=source_degree1_dimension,
        source_degree2_dimension=source_degree2_dimension,
        target_degree1_dimension=target_degree1_dimension,
        target_degree2_dimension=target_degree2_dimension,
        source_differential_shape=_matrix_shape(source_differential),
        target_differential_shape=_matrix_shape(target_differential),
        comparison_degree1_shape=_matrix_shape(comparison_degree1),
        comparison_degree2_shape=_matrix_shape(comparison_degree2),
        comparison_after_bar_differential=comparison_after_bar,
        ce_differential_after_comparison=ce_after_comparison,
        chain_commutator_matrix=commutator,
        chain_commutator_defect_rank=defect_rank,
        chain_map=chain_map,
        status="FINITE_BAR_CE_CHAIN_MAP_GATE" if chain_map else "FINITE_BAR_CE_CHAIN_MAP_DEFECT",
    )


def finite_bar_ce_report(
    charge_discriminants: Dict[str, int],
    bar_euler_exponents: Dict[str, int],
    differential_commutes_by_charge: Dict[str, bool],
    height_cutoff: int,
    *,
    charge_heights: Dict[str, int] | None = None,
    bkm_coefficients: Dict[int, int] | None = None,
    lower_height_cutoff: int | None = None,
) -> FiniteBarCEReport:
    """Check the finite ordered-bar/CE exponent and differential gates."""
    if height_cutoff <= 0:
        raise ValueError("height_cutoff must be positive")
    if lower_height_cutoff is not None:
        if lower_height_cutoff <= 0:
            raise ValueError("lower_height_cutoff must be positive")
        if lower_height_cutoff > height_cutoff:
            raise ValueError("lower_height_cutoff cannot exceed height_cutoff")
    if charge_heights is None:
        charge_heights = {charge: index + 1 for index, charge in enumerate(charge_discriminants)}
    missing_height = sorted(set(charge_discriminants) - set(charge_heights))
    if missing_height:
        raise ValueError(f"missing charge heights: {missing_height}")
    missing_differential = sorted(set(charge_discriminants) - set(differential_commutes_by_charge))
    if missing_differential:
        raise ValueError(f"missing differential witnesses: {missing_differential}")
    if any(height <= 0 for height in charge_heights.values()):
        raise ValueError("charge heights must be positive")

    if bkm_coefficients is None:
        max_discriminant = max((D for D in charge_discriminants.values() if D >= 0), default=0)
        bkm_coefficients = _bar.k3e_product_by_discriminant(max_discriminant)

    rows = []
    for charge in sorted(charge_discriminants, key=lambda key: (charge_heights[key], charge_discriminants[key], key)):
        height = charge_heights[charge]
        if height > height_cutoff:
            continue
        discriminant = charge_discriminants[charge]
        bar_euler_exponent = bar_euler_exponents.get(charge, 0)
        bkm_exponent = bkm_coefficients.get(discriminant, 0)
        rows.append(
            FiniteBarCERow(
                charge=charge,
                height=height,
                discriminant=discriminant,
                bar_euler_exponent=bar_euler_exponent,
                bkm_exponent=bkm_exponent,
                exponent_match=bar_euler_exponent == bkm_exponent,
                differential_commutes=differential_commutes_by_charge[charge],
            )
        )

    exponent_defects = tuple(row.charge for row in rows if not row.exponent_match)
    differential_defects = tuple(row.charge for row in rows if not row.differential_commutes)

    transition_commutes = True
    if lower_height_cutoff is not None:
        lower = finite_bar_ce_report(
            charge_discriminants,
            bar_euler_exponents,
            differential_commutes_by_charge,
            lower_height_cutoff,
            charge_heights=charge_heights,
            bkm_coefficients=bkm_coefficients,
        )
        projected = tuple(row for row in rows if row.height <= lower_height_cutoff)
        projected_key = tuple(
            (
                row.charge,
                row.height,
                row.discriminant,
                row.bar_euler_exponent,
                row.bkm_exponent,
                row.differential_commutes,
            )
            for row in projected
        )
        lower_key = tuple(
            (
                row.charge,
                row.height,
                row.discriminant,
                row.bar_euler_exponent,
                row.bkm_exponent,
                row.differential_commutes,
            )
            for row in lower.rows
        )
        transition_commutes = projected_key == lower_key

    closed = not exponent_defects and not differential_defects and transition_commutes
    return FiniteBarCEReport(
        height_cutoff=height_cutoff,
        rows=tuple(rows),
        exponent_defects=exponent_defects,
        differential_defects=differential_defects,
        transition_commutes=transition_commutes,
        closed=closed,
        status=(
            "FINITE_BAR_CE_COMPARISON"
            if closed
            else "FINITE_BAR_CE_DEFECT"
        ),
    )


def finite_bar_regularization_report(
    simple_root_gram: Iterable[Iterable[Any]] = (
        (2, -2, -2),
        (-2, 2, -2),
        (-2, -2, 2),
    ),
    bar_regularization_vector: Iterable[Any] = (
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(1, 2),
    ),
    *,
    supplied_normalization: Any = Fraction(1, 64),
    expected_normalization: Any = Fraction(1, 64),
) -> FiniteBarRegularizationReport:
    r"""Check the finite BKM/bar regularization against the Weyl vector.

    The Weyl vector is the unique solution of
    \(G\rho=-\operatorname{diag}(G)/2\) in the real-simple-root basis.
    This verifies supplied finite data; it does not construct the bar
    regularization vector or the multiplier-system normalization.
    """
    gram = _fraction_matrix(simple_root_gram)
    height, width = _matrix_shape(gram)
    if height == 0 or width == 0:
        raise ValueError("simple_root_gram must be nonempty")
    if height != width:
        raise ValueError("simple_root_gram must be square")
    if any(gram[i][j] != gram[j][i] for i in range(height) for j in range(width)):
        raise ValueError("simple_root_gram must be symmetric")
    supplied = _fraction_vector(bar_regularization_vector)
    if len(supplied) != width:
        raise ValueError("bar_regularization_vector has incompatible length")

    rhs = tuple(-gram[index][index] / 2 for index in range(height))
    target = _solve_square_linear_system(gram, rhs, "simple_root_gram")
    supplied_pairings = _matrix_vector_product(gram, supplied)
    pairing_defect = tuple(
        pairing - expected
        for pairing, expected in zip(supplied_pairings, rhs)
    )
    vector_difference = tuple(
        entry - target_entry
        for entry, target_entry in zip(supplied, target)
    )
    supplied_norm = Fraction(supplied_normalization)
    expected_norm = Fraction(expected_normalization)
    weyl_vector_matches = (
        all(entry == 0 for entry in pairing_defect)
        and all(entry == 0 for entry in vector_difference)
    )
    normalization_matches = supplied_norm == expected_norm
    closed = weyl_vector_matches and normalization_matches
    return FiniteBarRegularizationReport(
        simple_root_gram=gram,
        weyl_equation_rhs=rhs,
        borcherds_weyl_vector=target,
        supplied_bar_regularization_vector=supplied,
        supplied_pairings=supplied_pairings,
        pairing_defect=pairing_defect,
        vector_difference=vector_difference,
        supplied_normalization=supplied_norm,
        expected_normalization=expected_norm,
        weyl_vector_matches=weyl_vector_matches,
        normalization_matches=normalization_matches,
        closed=closed,
        status=(
            "FINITE_BAR_REGULARIZATION_MATCH"
            if closed
            else "FINITE_BAR_REGULARIZATION_DEFECT"
        ),
    )


def _rademacher_transition_commutes(discriminants: Tuple[int, ...], max_conductor: int) -> bool:
    """Check that finite conductor projections commute with partial sums."""
    return not _rademacher_transition_defects(discriminants, max_conductor)


def _rademacher_transition_defects(discriminants: Tuple[int, ...], max_conductor: int) -> Tuple[str, ...]:
    """Return the failed finite conductor projections, if any."""
    defects = []
    for D in discriminants:
        for conductor in range(2, max_conductor + 1):
            high = _rad.rademacher_partial_sum(D, conductor)
            projected = high - _rad.rademacher_term(D, conductor).term_value
            low = _rad.rademacher_partial_sum(D, conductor - 1)
            if abs(projected - low) > 1e-9:
                defects.append(f"D={D}:c={conductor}")
    return tuple(defects)


def rademacher_finite_height_certificate(
    discriminants: Tuple[int, ...] = (3, 4, 7, 8, 11, 12, 15, 16, 19, 20),
    max_conductor: int = 5,
    tolerance: float = 0.03,
) -> RademacherFiniteHeightCertificate:
    """Return the finite rank-one Rademacher packet and residual certificate.

    This is a certificate on the Jacobi coefficient lane of phi_{0,1}.  It
    does not assert the compact CY3 shadow/Rademacher comparison for
    (Phi_10^un)^{-1}; that comparison still requires the protected trace map.
    """
    rows: List[RademacherFiniteHeightRow] = []
    conductor_to_arity = tuple((conductor, conductor + 1) for conductor in range(1, max_conductor + 1))
    for D in discriminants:
        result = _rad.compute_identification(D, max_conductor + 1)
        if result.exact_c_D is None:
            raise ValueError(f"no phi_0,1 coefficient is available at discriminant {D}")
        rows.append(
            RademacherFiniteHeightRow(
                discriminant=D,
                exact_abs_coefficient=abs(result.exact_c_D),
                max_conductor=max_conductor,
                partial_sum=result.rademacher_partial_sums[-1],
                residual_abs=result.residuals_abs[-1],
                residual_rel=result.residuals_rel[-1],
                leading_residual_rel=result.residuals_rel[0],
                conductor_to_arity=conductor_to_arity,
            )
        )
    max_residual = max(row.residual_rel for row in rows)
    max_leading_residual = max(row.leading_residual_rel for row in rows)
    conductor_projection_defects = _rademacher_transition_defects(discriminants, max_conductor)
    transition_commutes = not conductor_projection_defects
    residual_improves = max_residual < max_leading_residual
    status = (
        "FINITE_RANK_ONE_RADEMACHER_CERTIFICATE"
        if transition_commutes and residual_improves and max_residual <= tolerance
        else "FINITE_RANK_ONE_RADEMACHER_RESIDUAL_EXCEEDS_TOLERANCE"
    )
    return RademacherFiniteHeightCertificate(
        discriminants=discriminants,
        max_conductor=max_conductor,
        rows=tuple(rows),
        max_residual_rel=max_residual,
        max_leading_residual_rel=max_leading_residual,
        residual_improves_over_leading=residual_improves,
        conductor_projection_defects=conductor_projection_defects,
        transition_commutes=transition_commutes,
        tolerance=tolerance,
        status=status,
    )


def _canonical_rademacher_polar_rows(
    discriminants: Tuple[int, ...],
    max_conductor: int,
) -> Dict[Tuple[int, int], Dict[str, Any]]:
    return {
        (D, conductor): {
            "polar_discriminant": -1,
            "polar_coefficient": 1,
            "multiplier": "eta^3",
            "bessel_order": Fraction(3, 2),
            "arity": conductor + 1,
            "signed_coefficient": _rad.PHI01_COEFFICIENTS[D],
        }
        for D in discriminants
        for conductor in range(1, max_conductor + 1)
    }


def rademacher_polar_bessel_gate(
    supplied_rows: Dict[Tuple[int, int], Dict[str, Any]] | None = None,
    discriminants: Tuple[int, ...] = (3, 4, 7, 8),
    max_conductor: int = 3,
    *,
    lower_max_conductor: int | None = None,
) -> RademacherPolarBesselGateReport:
    r"""Check supplied finite Rademacher rows against the rank-one kernel.

    The rank-one \(\phi_{0,1}\) lane is determined by polar discriminant
    \(-1\), polar coefficient \(1\), the \(\eta^3\)-multiplier, Bessel
    order \(3/2\), and the conductor-to-arity rule \(k=c+1\).  This
    verifies supplied finite rows; it does not construct the compact
    CY3 protected trace or the all-height Siegel Rademacher theorem.
    """
    if max_conductor <= 0:
        raise ValueError("max_conductor must be positive")
    if lower_max_conductor is not None:
        if lower_max_conductor <= 0:
            raise ValueError("lower_max_conductor must be positive")
        if lower_max_conductor > max_conductor:
            raise ValueError("lower_max_conductor cannot exceed max_conductor")
    missing_coefficients = sorted(set(discriminants) - set(_rad.PHI01_COEFFICIENTS))
    if missing_coefficients:
        raise ValueError(f"missing phi_0,1 coefficients: {missing_coefficients}")

    if supplied_rows is None:
        supplied_rows = _canonical_rademacher_polar_rows(discriminants, max_conductor)

    rows: List[RademacherPolarBesselRow] = []
    missing_rows = []
    for D in discriminants:
        if D <= 0:
            raise ValueError("discriminants must be positive")
        expected_signed = _rad.PHI01_COEFFICIENTS[D]
        for conductor in range(1, max_conductor + 1):
            key = (D, conductor)
            row_id = f"D={D}:c={conductor}"
            supplied = supplied_rows.get(key)
            if supplied is None:
                missing_rows.append(row_id)
                continue
            required_keys = {
                "polar_discriminant",
                "polar_coefficient",
                "multiplier",
                "bessel_order",
                "arity",
                "signed_coefficient",
            }
            missing_keys = sorted(required_keys - set(supplied))
            if missing_keys:
                raise ValueError(f"row {row_id} is missing fields: {missing_keys}")

            polar_discriminant = int(supplied["polar_discriminant"])
            polar_coefficient = int(supplied["polar_coefficient"])
            multiplier = str(supplied["multiplier"])
            bessel_order = Fraction(supplied["bessel_order"])
            arity = int(supplied["arity"])
            signed_coefficient = int(supplied["signed_coefficient"])
            term = _rad.rademacher_term(D, conductor)
            rows.append(
                RademacherPolarBesselRow(
                    discriminant=D,
                    conductor=conductor,
                    supplied_polar_discriminant=polar_discriminant,
                    supplied_polar_coefficient=polar_coefficient,
                    supplied_multiplier=multiplier,
                    supplied_bessel_order=bessel_order,
                    supplied_arity=arity,
                    supplied_signed_coefficient=signed_coefficient,
                    expected_signed_coefficient=expected_signed,
                    expected_absolute_coefficient=abs(expected_signed),
                    bessel_argument=term.bessel_arg,
                    bessel_value=term.bessel_value,
                    term_value=term.term_value,
                    polar_match=polar_discriminant == -1 and polar_coefficient == 1,
                    multiplier_match=multiplier == "eta^3",
                    bessel_order_match=bessel_order == Fraction(3, 2),
                    arity_match=arity == conductor + 1,
                    coefficient_match=signed_coefficient == expected_signed,
                )
            )

    polar_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.polar_match
    )
    multiplier_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.multiplier_match
    )
    bessel_order_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.bessel_order_match
    )
    arity_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.arity_match
    )
    coefficient_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.coefficient_match
    )

    transition_commutes = True
    if lower_max_conductor is not None:
        lower = rademacher_polar_bessel_gate(
            supplied_rows,
            discriminants,
            lower_max_conductor,
        )
        projected_key = tuple(
            (
                row.discriminant,
                row.conductor,
                row.supplied_polar_discriminant,
                row.supplied_polar_coefficient,
                row.supplied_multiplier,
                row.supplied_bessel_order,
                row.supplied_arity,
                row.supplied_signed_coefficient,
            )
            for row in rows
            if row.conductor <= lower_max_conductor
        )
        lower_key = tuple(
            (
                row.discriminant,
                row.conductor,
                row.supplied_polar_discriminant,
                row.supplied_polar_coefficient,
                row.supplied_multiplier,
                row.supplied_bessel_order,
                row.supplied_arity,
                row.supplied_signed_coefficient,
            )
            for row in lower.rows
        )
        transition_commutes = projected_key == lower_key

    closed = (
        not missing_rows
        and not polar_defects
        and not multiplier_defects
        and not bessel_order_defects
        and not arity_defects
        and not coefficient_defects
        and transition_commutes
    )
    return RademacherPolarBesselGateReport(
        discriminants=discriminants,
        max_conductor=max_conductor,
        rows=tuple(rows),
        missing_rows=tuple(missing_rows),
        polar_defects=polar_defects,
        multiplier_defects=multiplier_defects,
        bessel_order_defects=bessel_order_defects,
        arity_defects=arity_defects,
        coefficient_defects=coefficient_defects,
        transition_commutes=transition_commutes,
        closed=closed,
        status=(
            "FINITE_RADEMACHER_POLAR_BESSEL_GATE"
            if closed
            else "FINITE_RADEMACHER_POLAR_BESSEL_DEFECT"
        ),
    )


def _canonical_rademacher_error_bounds(
    discriminants: Tuple[int, ...],
    max_conductor: int,
) -> Tuple[Dict[Tuple[int, int], float], Dict[Tuple[int, int], float]]:
    abs_bounds: Dict[Tuple[int, int], float] = {}
    rel_bounds: Dict[Tuple[int, int], float] = {}
    for D in discriminants:
        exact = abs(_rad.PHI01_COEFFICIENTS[D])
        for conductor in range(1, max_conductor + 1):
            partial = _rad.rademacher_partial_sum(D, conductor)
            residual_abs = abs(partial - exact)
            abs_bounds[(D, conductor)] = residual_abs
            rel_bounds[(D, conductor)] = residual_abs / exact
    return abs_bounds, rel_bounds


def rademacher_truncation_error_gate(
    discriminants: Tuple[int, ...] = (3, 4, 7, 8),
    max_conductor: int = 3,
    *,
    abs_bounds: Dict[Tuple[int, int], Any] | None = None,
    rel_bounds: Dict[Tuple[int, int], Any] | None = None,
    tolerance: float = 0.03,
    lower_max_conductor: int | None = None,
) -> RademacherTruncationErrorGateReport:
    r"""Check supplied finite truncation-error bounds for the rank-one lane.

    The global compact Siegel theorem needs uniform all-height error
    control.  This finite gate checks the exact finite input: supplied
    absolute and relative majorants must dominate the residual of the
    conductor-\(c\) Rademacher partial sum against \(|c(D)|\).
    """
    if max_conductor <= 0:
        raise ValueError("max_conductor must be positive")
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")
    if lower_max_conductor is not None:
        if lower_max_conductor <= 0:
            raise ValueError("lower_max_conductor must be positive")
        if lower_max_conductor > max_conductor:
            raise ValueError("lower_max_conductor cannot exceed max_conductor")
    missing_coefficients = sorted(set(discriminants) - set(_rad.PHI01_COEFFICIENTS))
    if missing_coefficients:
        raise ValueError(f"missing phi_0,1 coefficients: {missing_coefficients}")
    if any(D <= 0 for D in discriminants):
        raise ValueError("discriminants must be positive")

    if abs_bounds is None or rel_bounds is None:
        default_abs, default_rel = _canonical_rademacher_error_bounds(
            discriminants,
            max_conductor,
        )
        if abs_bounds is None:
            abs_bounds = default_abs
        if rel_bounds is None:
            rel_bounds = default_rel

    rows: List[RademacherTruncationErrorRow] = []
    missing_abs_bounds = []
    missing_rel_bounds = []
    for D in discriminants:
        exact_abs = abs(_rad.PHI01_COEFFICIENTS[D])
        for conductor in range(1, max_conductor + 1):
            key = (D, conductor)
            row_id = f"D={D}:c={conductor}"
            partial = _rad.rademacher_partial_sum(D, conductor)
            residual_abs = abs(partial - exact_abs)
            residual_rel = residual_abs / exact_abs
            supplied_abs = abs_bounds.get(key)
            supplied_rel = rel_bounds.get(key)
            supplied_abs_float = None if supplied_abs is None else float(supplied_abs)
            supplied_rel_float = None if supplied_rel is None else float(supplied_rel)
            if supplied_abs is None:
                missing_abs_bounds.append(row_id)
            if supplied_rel is None:
                missing_rel_bounds.append(row_id)
            rows.append(
                RademacherTruncationErrorRow(
                    discriminant=D,
                    conductor=conductor,
                    arity=conductor + 1,
                    exact_absolute_coefficient=exact_abs,
                    partial_sum=partial,
                    residual_abs=residual_abs,
                    residual_rel=residual_rel,
                    supplied_abs_bound=supplied_abs_float,
                    supplied_rel_bound=supplied_rel_float,
                    abs_bound_valid=(
                        supplied_abs_float is not None
                        and residual_abs <= supplied_abs_float + 1e-12
                    ),
                    rel_bound_valid=(
                        supplied_rel_float is not None
                        and residual_rel <= supplied_rel_float + 1e-12
                    ),
                )
            )

    abs_bound_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.abs_bound_valid
    )
    rel_bound_defects = tuple(
        f"D={row.discriminant}:c={row.conductor}"
        for row in rows
        if not row.rel_bound_valid
    )
    terminal_rows = tuple(row for row in rows if row.conductor == max_conductor)
    max_terminal_residual_rel = max(
        (row.residual_rel for row in terminal_rows),
        default=0.0,
    )
    terminal_tolerance_met = max_terminal_residual_rel <= tolerance

    transition_commutes = True
    if lower_max_conductor is not None:
        lower = rademacher_truncation_error_gate(
            discriminants,
            lower_max_conductor,
            abs_bounds=abs_bounds,
            rel_bounds=rel_bounds,
            tolerance=tolerance,
        )
        projected_key = tuple(
            (
                row.discriminant,
                row.conductor,
                row.arity,
                row.exact_absolute_coefficient,
                row.supplied_abs_bound,
                row.supplied_rel_bound,
            )
            for row in rows
            if row.conductor <= lower_max_conductor
        )
        lower_key = tuple(
            (
                row.discriminant,
                row.conductor,
                row.arity,
                row.exact_absolute_coefficient,
                row.supplied_abs_bound,
                row.supplied_rel_bound,
            )
            for row in lower.rows
        )
        transition_commutes = projected_key == lower_key

    closed = (
        not missing_abs_bounds
        and not missing_rel_bounds
        and not abs_bound_defects
        and not rel_bound_defects
        and terminal_tolerance_met
        and transition_commutes
    )
    return RademacherTruncationErrorGateReport(
        discriminants=discriminants,
        max_conductor=max_conductor,
        rows=tuple(rows),
        missing_abs_bounds=tuple(missing_abs_bounds),
        missing_rel_bounds=tuple(missing_rel_bounds),
        abs_bound_defects=abs_bound_defects,
        rel_bound_defects=rel_bound_defects,
        max_terminal_residual_rel=max_terminal_residual_rel,
        tolerance=tolerance,
        terminal_tolerance_met=terminal_tolerance_met,
        transition_commutes=transition_commutes,
        closed=closed,
        status=(
            "FINITE_RADEMACHER_TRUNCATION_ERROR_GATE"
            if closed
            else "FINITE_RADEMACHER_TRUNCATION_ERROR_DEFECT"
        ),
    )


def rademacher_witness(max_n: int = 10) -> RademacherWitness:
    r"""Finite-height Rademacher growth witness."""
    return RademacherWitness(
        max_n=max_n,
        growth_ok=_shadow.verify_rademacher_growth(max_n, tolerance=0.01),
        leading_term_D3=_shadow.rademacher_leading_term(3),
        leading_term_D4=_shadow.rademacher_leading_term(4),
        finite_height_certificate=rademacher_finite_height_certificate(),
        status="rank-one finite-height packet certified; compact CY3 comparison still open",
    )


def brst_central_charge_gate(
    lattice_central_charge: Any = BRST_LATTICE_C,
    transverse_central_charge: Any = BRST_TRANSVERSE_C,
    ghost_central_charge: Any = BRST_GHOST_C,
    *,
    expected_total_central_charge: Any = 0,
) -> BRSTCentralChargeGateReport:
    r"""Check the finite BRST central-charge anomaly cancellation gate.

    The lattice VOA contributes its rank, the bosonic string ghost system
    contributes \(-26\), and relative BRST nilpotence requires total
    Virasoro central charge zero.  This is only the anomaly gate; it does
    not construct the BRST differential or prove no-ghost convergence.
    """
    lattice_c = Fraction(lattice_central_charge)
    transverse_c = Fraction(transverse_central_charge)
    ghost_c = Fraction(ghost_central_charge)
    expected_total = Fraction(expected_total_central_charge)
    required_transverse = expected_total - lattice_c - ghost_c
    total = lattice_c + transverse_c + ghost_c
    total_defect = total - expected_total
    transverse_defect = transverse_c - required_transverse
    anomaly_cancelled = total_defect == 0
    transverse_matches = transverse_defect == 0
    closed = anomaly_cancelled and transverse_matches
    return BRSTCentralChargeGateReport(
        lattice_central_charge=lattice_c,
        transverse_central_charge=transverse_c,
        ghost_central_charge=ghost_c,
        expected_total_central_charge=expected_total,
        required_transverse_central_charge=required_transverse,
        total_central_charge=total,
        total_defect=total_defect,
        transverse_defect=transverse_defect,
        anomaly_cancelled=anomaly_cancelled,
        transverse_matches_requirement=transverse_matches,
        closed=closed,
        status=(
            "FINITE_BRST_CENTRAL_CHARGE_GATE"
            if closed
            else "FINITE_BRST_CENTRAL_CHARGE_DEFECT"
        ),
    )


def brst_coefficient_fixture(max_discriminant: int = 8) -> BRSTCoefficientFixture:
    r"""Return the finite minimal supertrace fixture for the BRST transverse sector.

    The row at discriminant D is the minimal super-vector space T_D with
    sdim(T_D) = dim(T_D^0) - dim(T_D^1) = c(D).  This constructs the
    coefficient/parity fixture used by the finite BRST theorem boundary. It
    does not construct the transverse VOA or BRST differential.
    """
    table = _bar.k3e_product_by_discriminant(max_discriminant)
    retained = [
        (D, table[D])
        for D in sorted(table)
        if D <= max_discriminant and table[D] != 0
    ]
    rows = []
    for D, coefficient in retained:
        bosonic = coefficient if coefficient > 0 else 0
        fermionic = -coefficient if coefficient < 0 else 0
        superdimension = bosonic - fermionic
        rows.append(
            BRSTCoefficientFixtureRow(
                discriminant=D,
                signed_coefficient=coefficient,
                bosonic_dimension=bosonic,
                fermionic_dimension=fermionic,
                ordinary_dimension=abs(coefficient),
                superdimension=superdimension,
                parity="bosonic" if coefficient > 0 else "fermionic",
                supertrace_matches=superdimension == coefficient,
            )
        )
    total_bosonic = sum(row.bosonic_dimension for row in rows)
    total_fermionic = sum(row.fermionic_dimension for row in rows)
    return BRSTCoefficientFixture(
        max_discriminant=max_discriminant,
        rows=tuple(rows),
        support=tuple(row.discriminant for row in rows),
        total_bosonic_dimension=total_bosonic,
        total_fermionic_dimension=total_fermionic,
        total_ordinary_dimension=sum(row.ordinary_dimension for row in rows),
        total_superdimension=total_bosonic - total_fermionic,
        all_supertraces_match=all(row.supertrace_matches for row in rows),
        status="FINITE_BRST_COEFFICIENT_FIXTURE",
    )


def brst_coefficient_fixture_transition(
    upper_discriminant: int = 8,
    lower_discriminant: int = 4,
) -> BRSTCoefficientFixtureTransition:
    r"""Check that the finite BRST coefficient fixture restricts by height."""
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    upper = brst_coefficient_fixture(upper_discriminant)
    lower = brst_coefficient_fixture(lower_discriminant)
    upper_rows = {row.discriminant: row for row in upper.rows}
    defects = []
    for row in lower.rows:
        upper_row = upper_rows.get(row.discriminant)
        if upper_row is None:
            defects.append(f"missing:{row.discriminant}")
            continue
        if upper_row != row:
            defects.append(f"row_mismatch:{row.discriminant}")
    retained = tuple(D for D in upper.support if D <= lower_discriminant)
    if retained != lower.support:
        defects.append("support_mismatch")
    return BRSTCoefficientFixtureTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        retained_support=retained,
        defects=tuple(defects),
        transition_commutes=not defects,
        status="FINITE_BRST_FIXTURE_TRANSITION" if not defects else "FINITE_BRST_FIXTURE_TRANSITION_DEFECT",
    )


def brst_no_ghost_spectral_sequence_gate(
    *,
    target_coefficients: Dict[int, Any],
    transverse_supertraces: Dict[int, Any],
    longitudinal_supertraces: Dict[int, Any],
    ghost_supertraces: Dict[int, Any],
    higher_differential_matrices: Iterable[Iterable[Iterable[Any]]] = (),
) -> BRSTNoGhostSpectralSequenceGate:
    r"""Check a supplied finite no-ghost spectral-sequence packet.

    For each discriminant row the longitudinal and ghost supertraces
    must cancel, the transverse supertrace must equal the target Jacobi
    coefficient, and every supplied higher-page leakage matrix must have
    exact rank zero.  This does not construct the BRST complex.
    """
    support = tuple(
        sorted(
            set(target_coefficients)
            | set(transverse_supertraces)
            | set(longitudinal_supertraces)
            | set(ghost_supertraces)
        )
    )
    rows: List[BRSTNoGhostSpectralRow] = []
    missing_rows: List[str] = []
    cancellation_defects: List[str] = []
    coefficient_defects: List[str] = []

    for D in support:
        missing_parts = [
            name
            for name, table in (
                ("target", target_coefficients),
                ("transverse", transverse_supertraces),
                ("longitudinal", longitudinal_supertraces),
                ("ghost", ghost_supertraces),
            )
            if D not in table
        ]
        if missing_parts:
            missing_rows.append(f"D={D}:{','.join(missing_parts)}")
            continue
        target = Fraction(target_coefficients[D])
        transverse = Fraction(transverse_supertraces[D])
        longitudinal = Fraction(longitudinal_supertraces[D])
        ghost = Fraction(ghost_supertraces[D])
        cancellation_defect = longitudinal + ghost
        coefficient_defect = transverse - target
        cancellation_ok = cancellation_defect == 0
        coefficient_ok = coefficient_defect == 0
        if not cancellation_ok:
            cancellation_defects.append(f"D={D}:{cancellation_defect}")
        if not coefficient_ok:
            coefficient_defects.append(f"D={D}:{coefficient_defect}")
        rows.append(
            BRSTNoGhostSpectralRow(
                discriminant=D,
                target_coefficient=target,
                transverse_supertrace=transverse,
                longitudinal_supertrace=longitudinal,
                ghost_supertrace=ghost,
                cancellation_defect=cancellation_defect,
                coefficient_defect=coefficient_defect,
                cancellation_ok=cancellation_ok,
                coefficient_ok=coefficient_ok,
            )
        )

    higher_matrices = tuple(_fraction_matrix(matrix) for matrix in higher_differential_matrices)
    higher_shapes = tuple(_matrix_shape(matrix) for matrix in higher_matrices)
    higher_ranks = tuple(exact_matrix_rank(matrix) for matrix in higher_matrices)
    higher_defects = tuple(
        f"d_{index + 2}:rank={rank}"
        for index, rank in enumerate(higher_ranks)
        if rank != 0
    )
    no_ghost_cancellation = not missing_rows and not cancellation_defects
    transverse_coefficients_match = not missing_rows and not coefficient_defects
    spectral_sequence_collapses = not higher_defects
    closed = (
        no_ghost_cancellation
        and transverse_coefficients_match
        and spectral_sequence_collapses
    )
    return BRSTNoGhostSpectralSequenceGate(
        rows=tuple(rows),
        missing_rows=tuple(missing_rows),
        cancellation_defects=tuple(cancellation_defects),
        coefficient_defects=tuple(coefficient_defects),
        higher_differential_shapes=higher_shapes,
        higher_differential_ranks=higher_ranks,
        higher_differential_defects=higher_defects,
        no_ghost_cancellation=no_ghost_cancellation,
        transverse_coefficients_match=transverse_coefficients_match,
        spectral_sequence_collapses=spectral_sequence_collapses,
        closed=closed,
        status=(
            "FINITE_BRST_NO_GHOST_SPECTRAL_SEQUENCE_GATE"
            if closed
            else "FINITE_BRST_NO_GHOST_SPECTRAL_SEQUENCE_DEFECT"
        ),
    )


def brst_borcherds_bracket_gate(
    root_labels: Iterable[str],
    parities: Dict[str, int],
    brst_bracket_coefficients: Dict[Tuple[str, str, str], Any],
    borcherds_bracket_coefficients: Dict[Tuple[str, str, str], Any],
    *,
    root_sum_labels: Optional[Dict[Tuple[str, str], Optional[str]]] = None,
    finite_bound: int = 0,
) -> BRSTBorcherdsBracketGate:
    r"""Compare supplied finite BRST and Borcherds bracket tensors.

    The input is already a finite coefficient packet.  The gate checks
    coefficient equality, root-sum support, super-skew symmetry, and the
    super-Jacobi identity for the supplied BRST bracket.  It does not
    construct integrated vertex operators or OPE coefficients.
    """
    if finite_bound < 0:
        raise ValueError("finite_bound must be nonnegative")
    labels = tuple(root_labels)
    if not labels:
        raise ValueError("root_labels must be nonempty")
    if len(set(labels)) != len(labels):
        raise ValueError("root_labels must be distinct")
    label_set = set(labels)

    parity_by_label: Dict[str, int] = {}
    for label in labels:
        if label not in parities:
            raise ValueError(f"missing parity for root label {label!r}")
        parity = int(parities[label])
        if parity not in (0, 1):
            raise ValueError("parities must be 0 or 1")
        parity_by_label[label] = parity

    def normalize_bracket(
        coefficients: Dict[Tuple[str, str, str], Any],
        table_name: str,
    ) -> Dict[Tuple[str, str, str], Fraction]:
        normalized: Dict[Tuple[str, str, str], Fraction] = {}
        for key, value in coefficients.items():
            if len(key) != 3:
                raise ValueError(f"{table_name} bracket keys must have length 3")
            left, right, output = key
            unknown = tuple(label for label in (left, right, output) if label not in label_set)
            if unknown:
                raise ValueError(f"{table_name} bracket contains unknown label {unknown[0]!r}")
            normalized[(left, right, output)] = Fraction(value)
        return normalized

    brst = normalize_bracket(brst_bracket_coefficients, "brst")
    borcherds = normalize_bracket(borcherds_bracket_coefficients, "borcherds")

    normalized_support: Dict[Tuple[str, str], Optional[str]] = {}
    if root_sum_labels is not None:
        for key, value in root_sum_labels.items():
            if len(key) != 2:
                raise ValueError("root_sum_labels keys must have length 2")
            left, right = key
            unknown = tuple(label for label in (left, right) if label not in label_set)
            if unknown:
                raise ValueError(f"root_sum_labels contains unknown label {unknown[0]!r}")
            if value is not None and value not in label_set:
                raise ValueError(f"root_sum_labels contains unknown output label {value!r}")
            normalized_support[(left, right)] = value

    rows: List[BRSTBorcherdsBracketRow] = []
    coefficient_defects: List[str] = []
    retained_keys = tuple(sorted(set(brst) | set(borcherds)))
    for left, right, output in retained_keys:
        brst_value = brst.get((left, right, output), Fraction(0))
        borcherds_value = borcherds.get((left, right, output), Fraction(0))
        coefficient_match = brst_value == borcherds_value
        if brst_value != 0 or borcherds_value != 0 or not coefficient_match:
            rows.append(
                BRSTBorcherdsBracketRow(
                    left_label=left,
                    right_label=right,
                    output_label=output,
                    brst_coefficient=brst_value,
                    borcherds_coefficient=borcherds_value,
                    coefficient_match=coefficient_match,
                )
            )
        if not coefficient_match:
            coefficient_defects.append(
                f"{left},{right}->{output}:{brst_value}!={borcherds_value}"
            )

    support_defects: List[str] = []
    if root_sum_labels is not None:
        for (left, right, output), coefficient in sorted(brst.items()):
            if coefficient == 0:
                continue
            expected = normalized_support.get((left, right))
            if expected is None:
                support_defects.append(f"{left},{right}->{output}:killed")
            elif output != expected:
                support_defects.append(f"{left},{right}->{output}:expected {expected}")

    super_skew_defects: List[str] = []
    for left_index, left in enumerate(labels):
        for right_index, right in enumerate(labels):
            if right_index < left_index:
                continue
            sign = -1 if (parity_by_label[left] * parity_by_label[right]) % 2 else 1
            for output in labels:
                defect = (
                    brst.get((left, right, output), Fraction(0))
                    + sign * brst.get((right, left, output), Fraction(0))
                )
                if defect != 0:
                    super_skew_defects.append(f"{left},{right}->{output}:{defect}")

    super_jacobi_defects: List[str] = []
    for left in labels:
        for middle in labels:
            for right in labels:
                sign_l_r = -1 if (parity_by_label[left] * parity_by_label[right]) % 2 else 1
                sign_m_l = -1 if (parity_by_label[middle] * parity_by_label[left]) % 2 else 1
                sign_r_m = -1 if (parity_by_label[right] * parity_by_label[middle]) % 2 else 1
                for output in labels:
                    first = sum(
                        brst.get((middle, right, auxiliary), Fraction(0))
                        * brst.get((left, auxiliary, output), Fraction(0))
                        for auxiliary in labels
                    )
                    second = sum(
                        brst.get((right, left, auxiliary), Fraction(0))
                        * brst.get((middle, auxiliary, output), Fraction(0))
                        for auxiliary in labels
                    )
                    third = sum(
                        brst.get((left, middle, auxiliary), Fraction(0))
                        * brst.get((right, auxiliary, output), Fraction(0))
                        for auxiliary in labels
                    )
                    defect = sign_l_r * first + sign_m_l * second + sign_r_m * third
                    if defect != 0:
                        super_jacobi_defects.append(
                            f"{left},{middle},{right}->{output}:{defect}"
                        )

    coefficient_match = not coefficient_defects
    support_respected = not support_defects
    super_skew = not super_skew_defects
    super_jacobi = not super_jacobi_defects
    closed = coefficient_match and support_respected and super_skew and super_jacobi
    return BRSTBorcherdsBracketGate(
        finite_bound=finite_bound,
        root_labels=labels,
        rows=tuple(rows),
        coefficient_defects=tuple(coefficient_defects),
        support_defects=tuple(support_defects),
        super_skew_defects=tuple(super_skew_defects),
        super_jacobi_defects=tuple(super_jacobi_defects),
        coefficient_match=coefficient_match,
        support_respected=support_respected,
        super_skew=super_skew,
        super_jacobi=super_jacobi,
        closed=closed,
        status=(
            "FINITE_BRST_BORCHERDS_BRACKET_GATE"
            if closed
            else "FINITE_BRST_BORCHERDS_BRACKET_DEFECT"
        ),
    )


def brst_borcherds_serre_relation_gate(
    root_labels: Iterable[str],
    bracket_coefficients: Dict[Tuple[str, str, str], Any],
    *,
    real_serre_exponents: Optional[Dict[Tuple[str, str], int]] = None,
    imaginary_supercommuting_pairs: Iterable[Tuple[str, str]] = (),
    finite_bound: int = 0,
) -> BRSTBorcherdsSerreRelationGate:
    r"""Check finite Borcherds-Serre relations for a supplied bracket tensor.

    Real-root Serre relations are supplied as exponents
    \((i,j)\mapsto m_{ij}\) and tested as
    \((\operatorname{ad}e_i)^{m_{ij}}e_j=0\).  Imaginary
    supercommutativity pairs are tested as \([e_i,e_j]=0\).
    This is a relation checker for supplied coefficients, not an OPE
    construction.
    """
    if finite_bound < 0:
        raise ValueError("finite_bound must be nonnegative")
    labels = tuple(root_labels)
    if not labels:
        raise ValueError("root_labels must be nonempty")
    if len(set(labels)) != len(labels):
        raise ValueError("root_labels must be distinct")
    label_set = set(labels)

    bracket: Dict[Tuple[str, str, str], Fraction] = {}
    for key, value in bracket_coefficients.items():
        if len(key) != 3:
            raise ValueError("bracket keys must have length 3")
        left, right, output = key
        unknown = tuple(label for label in (left, right, output) if label not in label_set)
        if unknown:
            raise ValueError(f"bracket contains unknown label {unknown[0]!r}")
        bracket[(left, right, output)] = Fraction(value)

    def bracket_left(left: str, vector: Dict[str, Fraction]) -> Dict[str, Fraction]:
        result = {label: Fraction(0) for label in labels}
        for right, vector_coefficient in vector.items():
            if vector_coefficient == 0:
                continue
            for output in labels:
                result[output] += (
                    vector_coefficient
                    * bracket.get((left, right, output), Fraction(0))
                )
        return {label: coefficient for label, coefficient in result.items() if coefficient != 0}

    def format_vector(vector: Dict[str, Fraction]) -> Tuple[Tuple[str, Fraction], ...]:
        return tuple((label, vector[label]) for label in labels if vector.get(label, Fraction(0)) != 0)

    real_serre_rows: List[BRSTBorcherdsSerreRelationRow] = []
    real_serre_defects: List[str] = []
    for (left, right), exponent in sorted((real_serre_exponents or {}).items()):
        if left not in label_set:
            raise ValueError(f"real_serre_exponents contains unknown label {left!r}")
        if right not in label_set:
            raise ValueError(f"real_serre_exponents contains unknown label {right!r}")
        if exponent < 1:
            raise ValueError("real Serre exponents must be positive")
        vector = {right: Fraction(1)}
        for _ in range(exponent):
            vector = bracket_left(left, vector)
            if not vector:
                break
        output_coefficients = format_vector(vector)
        vanished = not output_coefficients
        real_serre_rows.append(
            BRSTBorcherdsSerreRelationRow(
                relation_type="real_serre",
                left_label=left,
                right_label=right,
                exponent=exponent,
                output_coefficients=output_coefficients,
                vanished=vanished,
            )
        )
        if not vanished:
            real_serre_defects.append(
                f"{left},{right}:ad^{exponent}="
                + ",".join(f"{label}:{coefficient}" for label, coefficient in output_coefficients)
            )

    imaginary_rows: List[BRSTBorcherdsSerreRelationRow] = []
    imaginary_defects: List[str] = []
    for left, right in tuple(imaginary_supercommuting_pairs):
        if left not in label_set:
            raise ValueError(f"imaginary_supercommuting_pairs contains unknown label {left!r}")
        if right not in label_set:
            raise ValueError(f"imaginary_supercommuting_pairs contains unknown label {right!r}")
        vector = {
            output: bracket.get((left, right, output), Fraction(0))
            for output in labels
            if bracket.get((left, right, output), Fraction(0)) != 0
        }
        output_coefficients = format_vector(vector)
        vanished = not output_coefficients
        imaginary_rows.append(
            BRSTBorcherdsSerreRelationRow(
                relation_type="imaginary_supercommutativity",
                left_label=left,
                right_label=right,
                exponent=1,
                output_coefficients=output_coefficients,
                vanished=vanished,
            )
        )
        if not vanished:
            imaginary_defects.append(
                f"{left},{right}:bracket="
                + ",".join(f"{label}:{coefficient}" for label, coefficient in output_coefficients)
            )

    real_serre_relations = not real_serre_defects
    imaginary_supercommutativity = not imaginary_defects
    closed = real_serre_relations and imaginary_supercommutativity
    return BRSTBorcherdsSerreRelationGate(
        finite_bound=finite_bound,
        root_labels=labels,
        real_serre_rows=tuple(real_serre_rows),
        imaginary_supercommutativity_rows=tuple(imaginary_rows),
        real_serre_defects=tuple(real_serre_defects),
        imaginary_supercommutativity_defects=tuple(imaginary_defects),
        real_serre_relations=real_serre_relations,
        imaginary_supercommutativity=imaginary_supercommutativity,
        closed=closed,
        status=(
            "FINITE_BRST_BORCHERDS_SERRE_RELATION_GATE"
            if closed
            else "FINITE_BRST_BORCHERDS_SERRE_RELATION_DEFECT"
        ),
    )


def brst_momentum_height_projection_gate(
    degree_heights: Dict[int, Iterable[int]],
    degree_momenta: Dict[int, Iterable[str]],
    differentials: Dict[int, Iterable[Iterable[Any]]],
    *,
    upper_height: int,
    lower_height: int,
) -> BRSTMomentumHeightProjectionGate:
    r"""Check that a finite BRST differential descends by height.

    Matrices are written target-by-source.  The gate checks that the
    supplied differential squares to zero, preserves momentum labels,
    carries retained height blocks to retained height blocks, and carries
    killed height blocks to killed height blocks.  It records the induced
    lower differential on retained coordinates.
    """
    if lower_height > upper_height:
        raise ValueError("lower_height must be <= upper_height")
    if not differentials:
        raise ValueError("differentials must be nonempty")

    heights = {degree: tuple(values) for degree, values in degree_heights.items()}
    momenta = {degree: tuple(values) for degree, values in degree_momenta.items()}
    matrices = {degree: _fraction_matrix(matrix) for degree, matrix in differentials.items()}
    for degree, degree_heights_tuple in heights.items():
        if any(height > upper_height for height in degree_heights_tuple):
            raise ValueError(f"degree {degree} has height above upper_height")
        if degree not in momenta:
            raise ValueError(f"missing momenta for degree {degree}")
        if len(momenta[degree]) != len(degree_heights_tuple):
            raise ValueError(f"degree {degree} heights and momenta must have the same length")

    def select_matrix(matrix: Matrix, row_indices: Tuple[int, ...], col_indices: Tuple[int, ...]) -> Matrix:
        return tuple(tuple(matrix[row][col] for col in col_indices) for row in row_indices)

    rows: List[BRSTMomentumHeightProjectionRow] = []
    lower_matrices: Dict[int, Matrix] = {}
    momentum_defects: List[str] = []
    subcomplex_defects: List[str] = []
    quotient_defects: List[str] = []

    for degree in sorted(matrices):
        if degree not in heights:
            raise ValueError(f"missing heights for source degree {degree}")
        if degree + 1 not in heights:
            raise ValueError(f"missing heights for target degree {degree + 1}")
        matrix = matrices[degree]
        source_heights = heights[degree]
        target_heights = heights[degree + 1]
        source_momenta = momenta[degree]
        target_momenta = momenta[degree + 1]
        _validate_matrix_shape(
            matrix,
            (len(target_heights), len(source_heights)),
            f"Q^{degree}",
        )
        retained_sources = tuple(
            index for index, height in enumerate(source_heights) if height <= lower_height
        )
        killed_sources = tuple(
            index for index, height in enumerate(source_heights) if height > lower_height
        )
        retained_targets = tuple(
            index for index, height in enumerate(target_heights) if height <= lower_height
        )
        killed_targets = tuple(
            index for index, height in enumerate(target_heights) if height > lower_height
        )

        degree_momentum_defects = []
        for row_index, row in enumerate(matrix):
            for col_index, value in enumerate(row):
                if value == 0:
                    continue
                if target_momenta[row_index] != source_momenta[col_index]:
                    degree_momentum_defects.append(
                        f"Q^{degree}:{row_index},{col_index}:{value}"
                    )
        momentum_defects.extend(degree_momentum_defects)

        retained_to_killed = select_matrix(matrix, killed_targets, retained_sources)
        killed_to_retained = select_matrix(matrix, retained_targets, killed_sources)
        retained_to_killed_rank = exact_matrix_rank(retained_to_killed)
        killed_to_retained_rank = exact_matrix_rank(killed_to_retained)
        if retained_to_killed_rank:
            subcomplex_defects.append(f"Q^{degree}:rank={retained_to_killed_rank}")
        if killed_to_retained_rank:
            quotient_defects.append(f"Q^{degree}:rank={killed_to_retained_rank}")

        lower_matrix = select_matrix(matrix, retained_targets, retained_sources)
        lower_matrices[degree] = lower_matrix
        rows.append(
            BRSTMomentumHeightProjectionRow(
                degree=degree,
                source_dimension=len(source_heights),
                target_dimension=len(target_heights),
                differential_shape=_matrix_shape(matrix),
                lower_differential_shape=_matrix_shape(lower_matrix),
                retained_source_count=len(retained_sources),
                killed_source_count=len(killed_sources),
                retained_target_count=len(retained_targets),
                killed_target_count=len(killed_targets),
                momentum_defect_entries=tuple(degree_momentum_defects),
                retained_to_killed_rank=retained_to_killed_rank,
                killed_to_retained_rank=killed_to_retained_rank,
            )
        )

    upper_square_ranks: List[Tuple[str, int]] = []
    upper_square_defects: List[str] = []
    lower_square_ranks: List[Tuple[str, int]] = []
    lower_square_defects: List[str] = []
    for degree in sorted(matrices):
        if degree + 1 not in matrices:
            continue
        upper_square = _matrix_product(matrices[degree + 1], matrices[degree])
        upper_rank = exact_matrix_rank(upper_square)
        upper_label = f"Q^{degree + 1}Q^{degree}"
        upper_square_ranks.append((upper_label, upper_rank))
        if upper_rank:
            upper_square_defects.append(f"{upper_label}:rank={upper_rank}")
        lower_square = _matrix_product(lower_matrices[degree + 1], lower_matrices[degree])
        lower_rank = exact_matrix_rank(lower_square)
        lower_square_ranks.append((upper_label, lower_rank))
        if lower_rank:
            lower_square_defects.append(f"{upper_label}:rank={lower_rank}")

    momentum_preserved = not momentum_defects
    retained_is_subcomplex = not subcomplex_defects
    killed_is_subcomplex = not quotient_defects
    upper_is_complex = not upper_square_defects
    lower_is_complex = not lower_square_defects
    closed = (
        momentum_preserved
        and retained_is_subcomplex
        and killed_is_subcomplex
        and upper_is_complex
        and lower_is_complex
    )
    return BRSTMomentumHeightProjectionGate(
        upper_height=upper_height,
        lower_height=lower_height,
        degrees=tuple(sorted(matrices)),
        rows=tuple(rows),
        upper_square_ranks=tuple(upper_square_ranks),
        lower_square_ranks=tuple(lower_square_ranks),
        momentum_defects=tuple(momentum_defects),
        subcomplex_defects=tuple(subcomplex_defects),
        quotient_defects=tuple(quotient_defects),
        upper_square_defects=tuple(upper_square_defects),
        lower_square_defects=tuple(lower_square_defects),
        momentum_preserved=momentum_preserved,
        retained_is_subcomplex=retained_is_subcomplex,
        killed_is_subcomplex=killed_is_subcomplex,
        upper_is_complex=upper_is_complex,
        lower_is_complex=lower_is_complex,
        closed=closed,
        status=(
            "FINITE_BRST_MOMENTUM_HEIGHT_PROJECTION_GATE"
            if closed
            else "FINITE_BRST_MOMENTUM_HEIGHT_PROJECTION_DEFECT"
        ),
    )


def brst_witness() -> BRSTWitness:
    r"""Finite BRST coefficient witness with the operator complex still open."""
    central_charge = brst_central_charge_gate()
    return BRSTWitness(
        lattice_central_charge=int(central_charge.lattice_central_charge),
        transverse_central_charge=int(central_charge.transverse_central_charge),
        ghost_central_charge=int(central_charge.ghost_central_charge),
        total_central_charge=int(central_charge.total_central_charge),
        central_charge_balanced=central_charge.anomaly_cancelled,
        coefficient_fixture=brst_coefficient_fixture(),
        target_template="H^1_BRST(V_{Lambda^{2,1}_{II}} tensor V_trans tensor V_ghost)",
        status="finite coefficient fixture; finite-height BRST differential still missing",
    )


def yangian_current_candidate_packet(
    max_discriminant: int = 8,
    max_mode: int = 2,
) -> YangianCurrentCandidatePacket:
    r"""Return the finite spectral-mode packet of Yangian current candidates.

    This is the vector-space part of the Yangian bridge.  It constructs
    e_{D,r}^{(a)} for retained discriminants D and modes 0 <= r <= M from
    the minimal BRST coefficient fixture.  It does not construct the OPE,
    residues, coproduct, Serre ideal, or R-matrix.
    """
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")
    fixture = brst_coefficient_fixture(max_discriminant)
    modes = tuple(range(max_mode + 1))
    rows = []
    for fixture_row in fixture.rows:
        multiplicity = fixture_row.ordinary_dimension
        row_superdimension = fixture_row.superdimension * len(modes)
        rows.append(
            YangianCurrentCandidateRow(
                discriminant=fixture_row.discriminant,
                signed_coefficient=fixture_row.signed_coefficient,
                multiplicity=multiplicity,
                parity=fixture_row.parity,
                undeformed_weight=fixture_row.discriminant + 1,
                deformed_weight_epsilon1=1,
                modes=modes,
                finite_dimension=multiplicity * len(modes),
                superdimension=row_superdimension,
                weight_one_at_epsilon1=True,
            )
        )
    return YangianCurrentCandidatePacket(
        max_discriminant=max_discriminant,
        max_mode=max_mode,
        rows=tuple(rows),
        support=fixture.support,
        total_dimension=sum(row.finite_dimension for row in rows),
        total_superdimension=sum(row.superdimension for row in rows),
        all_weight_one_at_epsilon1=all(row.weight_one_at_epsilon1 for row in rows),
        status="FINITE_YANGIAN_CURRENT_CANDIDATE_PACKET",
    )


def yangian_current_packet_transition(
    upper_discriminant: int = 8,
    lower_discriminant: int = 4,
    upper_mode: int = 2,
    lower_mode: int = 1,
) -> YangianCurrentPacketTransition:
    r"""Check two-axis truncation of finite Yangian current-candidate packets."""
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    if lower_mode > upper_mode:
        raise ValueError("lower_mode must be <= upper_mode")
    upper = yangian_current_candidate_packet(upper_discriminant, upper_mode)
    lower = yangian_current_candidate_packet(lower_discriminant, lower_mode)
    upper_rows = {row.discriminant: row for row in upper.rows}
    defects = []
    for lower_row in lower.rows:
        upper_row = upper_rows.get(lower_row.discriminant)
        if upper_row is None:
            defects.append(f"missing:{lower_row.discriminant}")
            continue
        if upper_row.signed_coefficient != lower_row.signed_coefficient:
            defects.append(f"coefficient_mismatch:{lower_row.discriminant}")
        if upper_row.parity != lower_row.parity:
            defects.append(f"parity_mismatch:{lower_row.discriminant}")
        if tuple(mode for mode in upper_row.modes if mode <= lower_mode) != lower_row.modes:
            defects.append(f"mode_mismatch:{lower_row.discriminant}")
        if upper_row.undeformed_weight != lower_row.undeformed_weight:
            defects.append(f"weight_mismatch:{lower_row.discriminant}")
    retained_support = tuple(D for D in upper.support if D <= lower_discriminant)
    retained_modes = tuple(mode for mode in range(upper_mode + 1) if mode <= lower_mode)
    if retained_support != lower.support:
        defects.append("support_mismatch")
    if retained_modes != tuple(range(lower_mode + 1)):
        defects.append("mode_support_mismatch")
    return YangianCurrentPacketTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        retained_support=retained_support,
        retained_modes=retained_modes,
        defects=tuple(defects),
        transition_commutes=not defects,
        status="FINITE_YANGIAN_PACKET_TRANSITION" if not defects else "FINITE_YANGIAN_PACKET_TRANSITION_DEFECT",
    )


def yangian_spectral_kernel_label_packet(
    max_discriminant: int = 8,
    max_mode: int = 2,
    cartan_label_count: int = 0,
) -> YangianSpectralKernelLabelPacket:
    r"""Return the finite label packet for the formal spectral current kernel.

    The packet constructs the non-Cartan labels in
    e_{D,r}^{(a)} tensor f_{D,r}^{(a)} + (-1)^p f_{D,r}^{(a)} tensor e_{D,r}^{(a)}
    from the finite current-candidate packet.  It does not construct the
    spectral connection, a Cartan kernel, a Hopf pairing, or an R-matrix.
    """
    if cartan_label_count < 0:
        raise ValueError("cartan_label_count must be nonnegative")
    current_packet = yangian_current_candidate_packet(max_discriminant, max_mode)
    rows = []
    for current_row in current_packet.rows:
        labels = current_row.finite_dimension
        parity_sign = 1 if current_row.parity == "bosonic" else -1
        rows.append(
            YangianSpectralKernelLabelRow(
                discriminant=current_row.discriminant,
                signed_coefficient=current_row.signed_coefficient,
                parity=current_row.parity,
                parity_sign=parity_sign,
                current_labels=labels,
                dual_labels=labels,
                tensor_monomials=2 * labels,
                row_superdimension=current_row.superdimension,
                mode_count=len(current_row.modes),
            )
        )
    noncartan_labels = sum(row.current_labels for row in rows)
    tensor_monomials = sum(row.tensor_monomials for row in rows)
    return YangianSpectralKernelLabelPacket(
        max_discriminant=max_discriminant,
        max_mode=max_mode,
        cartan_label_count=cartan_label_count,
        rows=tuple(rows),
        support=current_packet.support,
        positive_label_count=noncartan_labels,
        negative_label_count=noncartan_labels,
        noncartan_kernel_labels=noncartan_labels,
        tensor_monomials=tensor_monomials,
        total_kernel_labels_with_cartan=noncartan_labels + cartan_label_count,
        transition_ready=True,
        status="FINITE_YANGIAN_SPECTRAL_KERNEL_LABEL_PACKET",
    )


def yangian_spectral_kernel_transition(
    upper_discriminant: int = 8,
    lower_discriminant: int = 4,
    upper_mode: int = 2,
    lower_mode: int = 1,
    upper_cartan_label_count: int = 0,
    lower_cartan_label_count: int = 0,
) -> YangianSpectralKernelTransition:
    r"""Check two-axis truncation of finite spectral kernel label packets."""
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    if lower_mode > upper_mode:
        raise ValueError("lower_mode must be <= upper_mode")
    if lower_cartan_label_count > upper_cartan_label_count:
        raise ValueError("lower_cartan_label_count must be <= upper_cartan_label_count")
    upper = yangian_spectral_kernel_label_packet(
        upper_discriminant,
        upper_mode,
        upper_cartan_label_count,
    )
    lower = yangian_spectral_kernel_label_packet(
        lower_discriminant,
        lower_mode,
        lower_cartan_label_count,
    )
    upper_rows = {row.discriminant: row for row in upper.rows}
    defects = []
    for lower_row in lower.rows:
        upper_row = upper_rows.get(lower_row.discriminant)
        if upper_row is None:
            defects.append(f"missing:{lower_row.discriminant}")
            continue
        expected_labels = lower_row.current_labels
        if lower_row.dual_labels != expected_labels:
            defects.append(f"dual_label_mismatch:{lower_row.discriminant}")
        if lower_row.tensor_monomials != 2 * expected_labels:
            defects.append(f"tensor_monomial_mismatch:{lower_row.discriminant}")
        if upper_row.parity != lower_row.parity:
            defects.append(f"parity_mismatch:{lower_row.discriminant}")
        if upper_row.parity_sign != lower_row.parity_sign:
            defects.append(f"parity_sign_mismatch:{lower_row.discriminant}")
    retained = tuple(row.discriminant for row in upper.rows if row.discriminant <= lower_discriminant)
    if retained != tuple(row.discriminant for row in lower.rows):
        defects.append("support_mismatch")
    if lower.cartan_label_count > upper.cartan_label_count:
        defects.append("cartan_label_mismatch")
    return YangianSpectralKernelTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        upper_cartan_label_count=upper_cartan_label_count,
        lower_cartan_label_count=lower_cartan_label_count,
        retained_discriminants=retained,
        defects=tuple(defects),
        transition_commutes=not defects,
        status="FINITE_YANGIAN_SPECTRAL_KERNEL_TRANSITION" if not defects else "FINITE_YANGIAN_SPECTRAL_KERNEL_TRANSITION_DEFECT",
    )


def yangian_self_ope_pole_layer_packet(
    max_discriminant: int = 8,
    max_mode: int = 2,
) -> YangianSelfOPEPoleLayerPacket:
    r"""Return the finite formal self-OPE pole-layer packet.

    The exponent is the formal ansatz P_self(D,1)=D*(D-4).  A row with
    P<0 has -P pole layers.  The packet is an ordered-pair label space for
    possible OPE coefficients; it does not construct those coefficients,
    impose super-skew symmetry, or identify a Serre ideal.
    """
    current_packet = yangian_current_candidate_packet(max_discriminant, max_mode)
    coefficient_table = _bar.k3e_product_by_discriminant(max(4 * max_discriminant, max_discriminant))
    rows = []
    for current_row in current_packet.rows:
        D = current_row.discriminant
        exponent = D * (D - 4)
        pole_order = max(0, -exponent)
        if exponent < 0:
            singularity_type = "pole"
        elif exponent == 0:
            singularity_type = "marginal"
        else:
            singularity_type = "regular"
        ordered_pair_dimension = current_row.multiplicity * current_row.multiplicity * len(current_row.modes) ** 2
        target_discriminant = 4 * D
        rows.append(
            YangianSelfOPEPoleLayerRow(
                discriminant=D,
                signed_coefficient=current_row.signed_coefficient,
                exponent=exponent,
                singularity_type=singularity_type,
                pole_order=pole_order,
                current_multiplicity=current_row.multiplicity,
                mode_count=len(current_row.modes),
                ordered_pair_dimension=ordered_pair_dimension,
                pole_layer_dimension=ordered_pair_dimension * pole_order,
                pole_layer_superdimension=(current_row.signed_coefficient ** 2) * len(current_row.modes) ** 2 * pole_order,
                target_discriminant=target_discriminant,
                target_signed_coefficient=coefficient_table.get(target_discriminant, 0),
            )
        )
    return YangianSelfOPEPoleLayerPacket(
        max_discriminant=max_discriminant,
        max_mode=max_mode,
        rows=tuple(rows),
        pole_discriminants=tuple(row.discriminant for row in rows if row.singularity_type == "pole"),
        marginal_discriminants=tuple(row.discriminant for row in rows if row.singularity_type == "marginal"),
        regular_discriminants=tuple(row.discriminant for row in rows if row.singularity_type == "regular"),
        total_pole_layers=sum(row.pole_order for row in rows),
        total_pole_layer_dimension=sum(row.pole_layer_dimension for row in rows),
        transition_ready=True,
        status="FINITE_YANGIAN_SELF_OPE_POLE_LAYER_PACKET",
    )


def yangian_self_ope_pole_transition(
    upper_discriminant: int = 8,
    lower_discriminant: int = 4,
    upper_mode: int = 2,
    lower_mode: int = 1,
) -> YangianSelfOPEPoleTransition:
    r"""Check truncation of finite formal self-OPE pole-layer packets."""
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    if lower_mode > upper_mode:
        raise ValueError("lower_mode must be <= upper_mode")
    upper = yangian_self_ope_pole_layer_packet(upper_discriminant, upper_mode)
    lower = yangian_self_ope_pole_layer_packet(lower_discriminant, lower_mode)
    upper_rows = {row.discriminant: row for row in upper.rows}
    defects = []
    for lower_row in lower.rows:
        upper_row = upper_rows.get(lower_row.discriminant)
        if upper_row is None:
            defects.append(f"missing:{lower_row.discriminant}")
            continue
        if upper_row.exponent != lower_row.exponent:
            defects.append(f"exponent_mismatch:{lower_row.discriminant}")
        if upper_row.pole_order != lower_row.pole_order:
            defects.append(f"pole_order_mismatch:{lower_row.discriminant}")
        if upper_row.target_discriminant != lower_row.target_discriminant:
            defects.append(f"target_mismatch:{lower_row.discriminant}")
        expected_dimension = (
            lower_row.current_multiplicity
            * lower_row.current_multiplicity
            * (lower_mode + 1) ** 2
            * lower_row.pole_order
        )
        if lower_row.pole_layer_dimension != expected_dimension:
            defects.append(f"dimension_mismatch:{lower_row.discriminant}")
    retained = tuple(row.discriminant for row in upper.rows if row.discriminant <= lower_discriminant)
    if retained != tuple(row.discriminant for row in lower.rows):
        defects.append("support_mismatch")
    return YangianSelfOPEPoleTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        retained_discriminants=retained,
        defects=tuple(defects),
        transition_commutes=not defects,
        status="FINITE_YANGIAN_SELF_OPE_TRANSITION" if not defects else "FINITE_YANGIAN_SELF_OPE_TRANSITION_DEFECT",
    )


def yangian_label_tower_transition(
    upper_discriminant: int = 8,
    lower_discriminant: int = 4,
    upper_mode: int = 2,
    lower_mode: int = 1,
    upper_cartan_label_count: int = 0,
    lower_cartan_label_count: int = 0,
) -> YangianLabelTowerTransition:
    r"""Check simultaneous two-axis truncation of the finite Yangian labels."""
    current = yangian_current_packet_transition(
        upper_discriminant,
        lower_discriminant,
        upper_mode,
        lower_mode,
    )
    spectral_kernel = yangian_spectral_kernel_transition(
        upper_discriminant,
        lower_discriminant,
        upper_mode,
        lower_mode,
        upper_cartan_label_count,
        lower_cartan_label_count,
    )
    self_ope_pole = yangian_self_ope_pole_transition(
        upper_discriminant,
        lower_discriminant,
        upper_mode,
        lower_mode,
    )
    defects = []
    if not current.transition_commutes:
        defects.extend(f"current:{defect}" for defect in current.defects)
    if not spectral_kernel.transition_commutes:
        defects.extend(f"spectral_kernel:{defect}" for defect in spectral_kernel.defects)
    if not self_ope_pole.transition_commutes:
        defects.extend(f"self_ope_pole:{defect}" for defect in self_ope_pole.defects)
    retained_discriminants = current.retained_support
    retained_modes = current.retained_modes
    if spectral_kernel.retained_discriminants != retained_discriminants:
        defects.append("kernel_current_support_mismatch")
    if self_ope_pole.retained_discriminants != retained_discriminants:
        defects.append("pole_current_support_mismatch")
    upper_current_packet = yangian_current_candidate_packet(upper_discriminant, upper_mode)
    lower_current_packet = yangian_current_candidate_packet(lower_discriminant, lower_mode)
    upper_spectral_packet = yangian_spectral_kernel_label_packet(
        upper_discriminant,
        upper_mode,
        upper_cartan_label_count,
    )
    lower_spectral_packet = yangian_spectral_kernel_label_packet(
        lower_discriminant,
        lower_mode,
        lower_cartan_label_count,
    )
    upper_pole_packet = yangian_self_ope_pole_layer_packet(upper_discriminant, upper_mode)
    lower_pole_packet = yangian_self_ope_pole_layer_packet(lower_discriminant, lower_mode)
    component_statuses = {
        "current": current.status,
        "spectral_kernel": spectral_kernel.status,
        "self_ope_pole": self_ope_pole.status,
    }
    component_defects = {
        "current": current.defects,
        "spectral_kernel": spectral_kernel.defects,
        "self_ope_pole": self_ope_pole.defects,
    }
    component_gates = {
        "current": current.transition_commutes,
        "spectral_kernel": spectral_kernel.transition_commutes,
        "self_ope_pole": self_ope_pole.transition_commutes,
    }
    component_size_data = {
        "current": {
            "upper_support_size": len(upper_current_packet.support),
            "lower_support_size": len(lower_current_packet.support),
            "upper_total_dimension": upper_current_packet.total_dimension,
            "lower_total_dimension": lower_current_packet.total_dimension,
            "upper_total_superdimension": upper_current_packet.total_superdimension,
            "lower_total_superdimension": lower_current_packet.total_superdimension,
            "upper_mode_count": upper_mode + 1,
            "lower_mode_count": lower_mode + 1,
        },
        "spectral_kernel": {
            "upper_support_size": len(upper_spectral_packet.support),
            "lower_support_size": len(lower_spectral_packet.support),
            "upper_noncartan_kernel_labels": upper_spectral_packet.noncartan_kernel_labels,
            "lower_noncartan_kernel_labels": lower_spectral_packet.noncartan_kernel_labels,
            "upper_tensor_monomials": upper_spectral_packet.tensor_monomials,
            "lower_tensor_monomials": lower_spectral_packet.tensor_monomials,
            "upper_cartan_label_count": upper_spectral_packet.cartan_label_count,
            "lower_cartan_label_count": lower_spectral_packet.cartan_label_count,
        },
        "self_ope_pole": {
            "upper_support_size": len(upper_pole_packet.rows),
            "lower_support_size": len(lower_pole_packet.rows),
            "upper_total_pole_layers": upper_pole_packet.total_pole_layers,
            "lower_total_pole_layers": lower_pole_packet.total_pole_layers,
            "upper_total_pole_layer_dimension": upper_pole_packet.total_pole_layer_dimension,
            "lower_total_pole_layer_dimension": lower_pole_packet.total_pole_layer_dimension,
            "upper_pole_discriminant_count": len(upper_pole_packet.pole_discriminants),
            "lower_pole_discriminant_count": len(lower_pole_packet.pole_discriminants),
        },
    }
    transition_commutes = not defects
    return YangianLabelTowerTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        current=current,
        spectral_kernel=spectral_kernel,
        self_ope_pole=self_ope_pole,
        retained_discriminants=retained_discriminants,
        retained_modes=retained_modes,
        component_statuses=component_statuses,
        component_defects=component_defects,
        component_gates=component_gates,
        component_size_data=component_size_data,
        defects=tuple(defects),
        transition_commutes=transition_commutes,
        status="FINITE_YANGIAN_LABEL_TOWER_TRANSITION" if transition_commutes else "FINITE_YANGIAN_LABEL_TOWER_TRANSITION_DEFECT",
    )


def yangian_residue_transition(
    upper_discriminant: int,
    lower_discriminant: int,
    upper_mode: int,
    lower_mode: int,
    *,
    upper_residue_matrix: Iterable[Iterable[Any]],
    lower_residue_matrix: Iterable[Iterable[Any]],
    source_projection: Iterable[Iterable[Any]],
    target_projection: Iterable[Iterable[Any]],
) -> YangianResidueTransition:
    r"""Check heightwise transition compatibility of supplied residues.

    Residue matrices map finite vertex-operator labels to finite current
    labels. The criterion is the commutative square
    target_projection * upper_residue = lower_residue * source_projection.
    This check does not construct the residue maps.
    """
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    if lower_mode > upper_mode:
        raise ValueError("lower_mode must be <= upper_mode")

    upper_residue = _fraction_matrix(upper_residue_matrix)
    lower_residue = _fraction_matrix(lower_residue_matrix)
    source = _fraction_matrix(source_projection)
    target = _fraction_matrix(target_projection)

    upper_current_dimension, upper_vertex_dimension = _matrix_shape(upper_residue)
    lower_current_dimension, lower_vertex_dimension = _matrix_shape(lower_residue)
    _validate_matrix_shape(source, (lower_vertex_dimension, upper_vertex_dimension), "source_projection")
    _validate_matrix_shape(target, (lower_current_dimension, upper_current_dimension), "target_projection")

    left = _matrix_product(target, upper_residue)
    right = _matrix_product(lower_residue, source)
    commutator = _matrix_difference(left, right)
    defect_rank = exact_matrix_rank(commutator)
    transition_commutes = defect_rank == 0

    return YangianResidueTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        upper_vertex_dimension=upper_vertex_dimension,
        lower_vertex_dimension=lower_vertex_dimension,
        upper_current_dimension=upper_current_dimension,
        lower_current_dimension=lower_current_dimension,
        source_projection_shape=_matrix_shape(source),
        target_projection_shape=_matrix_shape(target),
        upper_residue_shape=_matrix_shape(upper_residue),
        lower_residue_shape=_matrix_shape(lower_residue),
        target_after_upper_residue=left,
        lower_residue_after_source=right,
        commutator_matrix=commutator,
        commutator_defect_rank=defect_rank,
        transition_commutes=transition_commutes,
        status="FINITE_YANGIAN_RESIDUE_TRANSITION" if transition_commutes else "FINITE_YANGIAN_RESIDUE_TRANSITION_DEFECT",
    )


def yangian_brst_residue_chain_gate(
    max_discriminant: int,
    max_mode: int,
    *,
    q0_matrix: Iterable[Iterable[Any]],
    q1_matrix: Iterable[Iterable[Any]],
    residue_degree0_matrix: Iterable[Iterable[Any]],
    residue_degree1_matrix: Iterable[Iterable[Any]],
    residue_degree2_matrix: Iterable[Iterable[Any]],
) -> YangianBRSTResidueChainGate:
    r"""Check that supplied finite residues descend to BRST H^1.

    The matrices q0 and q1 represent a finite ghost-number slice
    C^0 -> C^1 -> C^2.  The residue matrices are degree-preserving
    endomorphisms.  The residue packet acts on H^1 precisely when the
    BRST square vanishes and the two finite chain-map squares commute.
    This function does not construct the BRST differential or the
    residue operators.
    """
    if max_discriminant < 0:
        raise ValueError("max_discriminant must be nonnegative")
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")

    q0 = _fraction_matrix(q0_matrix)
    q1 = _fraction_matrix(q1_matrix)
    residue0 = _fraction_matrix(residue_degree0_matrix)
    residue1 = _fraction_matrix(residue_degree1_matrix)
    residue2 = _fraction_matrix(residue_degree2_matrix)

    degree1_dimension, degree0_dimension = _matrix_shape(q0)
    degree2_dimension, q1_source_dimension = _matrix_shape(q1)
    if q1_source_dimension != degree1_dimension:
        raise ValueError("q1_matrix width must equal q0_matrix height")
    _validate_matrix_shape(residue0, (degree0_dimension, degree0_dimension), "residue_degree0_matrix")
    _validate_matrix_shape(residue1, (degree1_dimension, degree1_dimension), "residue_degree1_matrix")
    _validate_matrix_shape(residue2, (degree2_dimension, degree2_dimension), "residue_degree2_matrix")

    brst_square = _matrix_product(q1, q0)
    residue1_after_q0 = _matrix_product(residue1, q0)
    q0_after_residue0 = _matrix_product(q0, residue0)
    boundary_commutator = _matrix_difference(residue1_after_q0, q0_after_residue0)
    residue2_after_q1 = _matrix_product(residue2, q1)
    q1_after_residue1 = _matrix_product(q1, residue1)
    cycle_commutator = _matrix_difference(residue2_after_q1, q1_after_residue1)

    brst_square_rank = exact_matrix_rank(brst_square)
    boundary_rank = exact_matrix_rank(boundary_commutator)
    cycle_rank = exact_matrix_rank(cycle_commutator)
    brst_complex = brst_square_rank == 0
    residue_commutes = boundary_rank == 0 and cycle_rank == 0
    descends = brst_complex and residue_commutes

    return YangianBRSTResidueChainGate(
        max_discriminant=max_discriminant,
        max_mode=max_mode,
        degree0_dimension=degree0_dimension,
        degree1_dimension=degree1_dimension,
        degree2_dimension=degree2_dimension,
        q0_shape=_matrix_shape(q0),
        q1_shape=_matrix_shape(q1),
        residue_degree0_shape=_matrix_shape(residue0),
        residue_degree1_shape=_matrix_shape(residue1),
        residue_degree2_shape=_matrix_shape(residue2),
        brst_square=brst_square,
        residue1_after_q0=residue1_after_q0,
        q0_after_residue0=q0_after_residue0,
        boundary_commutator_matrix=boundary_commutator,
        residue2_after_q1=residue2_after_q1,
        q1_after_residue1=q1_after_residue1,
        cycle_commutator_matrix=cycle_commutator,
        brst_square_defect_rank=brst_square_rank,
        boundary_commutator_defect_rank=boundary_rank,
        cycle_commutator_defect_rank=cycle_rank,
        brst_complex=brst_complex,
        residue_commutes_with_brst=residue_commutes,
        descends_to_h1=descends,
        status="FINITE_YANGIAN_BRST_RESIDUE_CHAIN_GATE" if descends else "FINITE_YANGIAN_BRST_RESIDUE_CHAIN_DEFECT",
    )


def _coefficient_key(key: Iterable[str]) -> Tuple[str, str, str]:
    key_tuple = tuple(key)
    if len(key_tuple) != 3:
        raise ValueError("OPE coefficient keys must be triples")
    return key_tuple  # type: ignore[return-value]


def yangian_ope_coefficient_transition(
    upper_discriminant: int,
    lower_discriminant: int,
    upper_mode: int,
    lower_mode: int,
    *,
    upper_coefficients: Dict[Tuple[str, str, str], Any],
    lower_coefficients: Dict[Tuple[str, str, str], Any],
    label_projection: Dict[str, Optional[str]],
) -> YangianOPECoefficientTransition:
    r"""Check finite heightwise transition of supplied OPE coefficients.

    Coefficients are keyed by (left_label, right_label, target_label).
    The projection either sends each upper label to a lower label or to
    None, in which case the term is discarded by truncation.  The finite
    OPE-square criterion is for coordinate truncations: surviving labels
    must project injectively.  If two surviving upper labels are identified,
    the aggregated tensor is only a coarse-grained pushforward and is
    reported as a defect.  The function does not derive the coefficients
    from an OPE.
    """
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    if lower_mode > upper_mode:
        raise ValueError("lower_mode must be <= upper_mode")

    projected: Dict[Tuple[str, str, str], Fraction] = {}
    discarded_entry_count = 0
    missing_projection_labels = set()
    surviving_preimages: Dict[str, set[str]] = {}
    for label, projected_label in label_projection.items():
        if projected_label is not None:
            surviving_preimages.setdefault(str(projected_label), set()).add(label)
    for raw_key, raw_coefficient in upper_coefficients.items():
        key = _coefficient_key(raw_key)
        projected_labels = []
        missing = False
        discarded = False
        for label in key:
            if label not in label_projection:
                missing_projection_labels.add(label)
                missing = True
                continue
            projected_label = label_projection[label]
            if projected_label is None:
                discarded = True
            projected_labels.append(projected_label)
        if missing:
            continue
        if discarded:
            discarded_entry_count += 1
            continue
        projected_key = tuple(projected_labels)
        if len(projected_key) != 3 or any(label is None for label in projected_key):
            raise ValueError("projected OPE coefficient keys must be triples")
        projected_key_typed = (str(projected_key[0]), str(projected_key[1]), str(projected_key[2]))
        projected[projected_key_typed] = projected.get(projected_key_typed, Fraction(0)) + Fraction(raw_coefficient)

    lower = {_coefficient_key(key): Fraction(value) for key, value in lower_coefficients.items()}
    projected_support = set(projected)
    lower_support = set(lower)
    missing_support = tuple(sorted(lower_support - projected_support))
    extra_support = tuple(sorted(projected_support - lower_support))
    coefficient_defects = []
    for key in sorted(projected_support & lower_support):
        if projected[key] != lower[key]:
            coefficient_defects.append(f"{key}:{projected[key]}!={lower[key]}")
    noninjective_projection_labels = tuple(
        sorted(label for label, preimages in surviving_preimages.items() if len(preimages) > 1)
    )
    support_defects = (
        tuple(f"missing:{key}" for key in missing_support)
        + tuple(f"extra:{key}" for key in extra_support)
    )
    transition_commutes = (
        not missing_projection_labels
        and not noninjective_projection_labels
        and not support_defects
        and not coefficient_defects
    )
    return YangianOPECoefficientTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        upper_entry_count=len(upper_coefficients),
        lower_entry_count=len(lower_coefficients),
        projected_entry_count=len(projected),
        discarded_entry_count=discarded_entry_count,
        projected_coefficients=projected,
        lower_coefficients_normalized=lower,
        missing_projection_labels=tuple(sorted(missing_projection_labels)),
        noninjective_projection_labels=noninjective_projection_labels,
        support_defects=support_defects,
        coefficient_defects=tuple(coefficient_defects),
        transition_commutes=transition_commutes,
        status="FINITE_YANGIAN_OPE_COEFFICIENT_TRANSITION" if transition_commutes else "FINITE_YANGIAN_OPE_COEFFICIENT_TRANSITION_DEFECT",
    )


def yangian_ope_serre_ideal_span_gate(
    ope_associativity_relation_matrix: Iterable[Iterable[Any]],
    borcherds_serre_relation_matrix: Iterable[Iterable[Any]],
    *,
    ambient_dimension: Optional[int] = None,
    finite_bound: int = 0,
    max_mode: int = 0,
) -> YangianOPESerreIdealSpanGate:
    r"""Check equality of finite OPE and Borcherds-Serre relation spans.

    Rows are relation vectors in a fixed finite word-coordinate space.
    Equality of the finite ideals in that bounded word space is equality
    of the two row spans.  The function does not derive either relation
    matrix from OPE coefficients.
    """
    if finite_bound < 0:
        raise ValueError("finite_bound must be nonnegative")
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")
    ope = _fraction_matrix(ope_associativity_relation_matrix)
    serre = _fraction_matrix(borcherds_serre_relation_matrix)
    inferred_widths = []
    if ope:
        inferred_widths.append(_matrix_width(ope))
    if serre:
        inferred_widths.append(_matrix_width(serre))
    if ambient_dimension is None:
        if not inferred_widths:
            raise ValueError("ambient_dimension is required when both relation matrices are empty")
        ambient_dimension = inferred_widths[0]
    if ambient_dimension < 0:
        raise ValueError("ambient_dimension must be nonnegative")
    for width in inferred_widths:
        if width != ambient_dimension:
            raise ValueError("relation matrices must have ambient_dimension columns")

    def row_in_span(row: Vector, span: Matrix) -> bool:
        if len(row) != ambient_dimension:
            raise ValueError("relation row has wrong ambient dimension")
        return exact_matrix_rank(span + (row,)) == exact_matrix_rank(span)

    for row in ope + serre:
        if len(row) != ambient_dimension:
            raise ValueError("relation row has wrong ambient dimension")

    ope_rank = exact_matrix_rank(ope)
    serre_rank = exact_matrix_rank(serre)
    combined = ope + serre
    combined_rank = exact_matrix_rank(combined)
    ope_missing = tuple(
        index for index, row in enumerate(ope) if not row_in_span(row, serre)
    )
    serre_missing = tuple(
        index for index, row in enumerate(serre) if not row_in_span(row, ope)
    )
    serre_span_contains_ope = not ope_missing
    ope_span_contains_serre = not serre_missing
    spans_equal = (
        ope_rank == serre_rank
        and ope_rank == combined_rank
        and serre_span_contains_ope
        and ope_span_contains_serre
    )
    return YangianOPESerreIdealSpanGate(
        finite_bound=finite_bound,
        max_mode=max_mode,
        ambient_dimension=ambient_dimension,
        ope_relation_count=len(ope),
        serre_relation_count=len(serre),
        ope_relation_rank=ope_rank,
        serre_relation_rank=serre_rank,
        combined_relation_rank=combined_rank,
        ope_rows_missing_from_serre_span=ope_missing,
        serre_rows_missing_from_ope_span=serre_missing,
        ope_span_contains_serre=ope_span_contains_serre,
        serre_span_contains_ope=serre_span_contains_ope,
        spans_equal=spans_equal,
        closed=spans_equal,
        status=(
            "FINITE_YANGIAN_OPE_SERRE_IDEAL_SPAN_GATE"
            if spans_equal
            else "FINITE_YANGIAN_OPE_SERRE_IDEAL_SPAN_DEFECT"
        ),
    )


def _nonnegative_integer_vector(values: Iterable[Any], name: str) -> Tuple[int, ...]:
    normalized = []
    for entry in values:
        value = Fraction(entry)
        if value.denominator != 1:
            raise ValueError(f"{name} entries must be integers")
        if value < 0:
            raise ValueError(f"{name} entries must be nonnegative")
        normalized.append(int(value))
    return tuple(normalized)


def yangian_pbw_associated_graded_gate(
    source_hilbert_vector: Iterable[Any],
    target_hilbert_vector: Iterable[Any],
    associated_graded_blocks: Iterable[Iterable[Iterable[Any]]],
    *,
    finite_bound: int = 0,
    max_mode: int = 0,
) -> YangianPBWAssociatedGradedGate:
    r"""Check the finite PBW associated-graded isomorphism criterion.

    The Hilbert vectors are ordinary block dimensions after the parity
    fixture has been fixed.  Each block matrix is the associated-graded
    comparison from the source PBW block to the target Borcherds block,
    written with target rows and source columns.
    """
    if finite_bound < 0:
        raise ValueError("finite_bound must be nonnegative")
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")
    source = _nonnegative_integer_vector(source_hilbert_vector, "source_hilbert_vector")
    target = _nonnegative_integer_vector(target_hilbert_vector, "target_hilbert_vector")
    if len(source) != len(target):
        raise ValueError("source and target Hilbert vectors must have the same length")
    blocks = tuple(_fraction_matrix(block) for block in associated_graded_blocks)
    if len(blocks) != len(source):
        raise ValueError("one associated-graded block is required for each Hilbert entry")

    ranks = []
    surjectivity_defects = []
    kernel_excess_dimensions = []
    for index, (source_dim, target_dim, block) in enumerate(zip(source, target, blocks)):
        if target_dim == 0:
            if block:
                raise ValueError(f"associated-graded block {index} must have zero rows")
        else:
            if len(block) != target_dim:
                raise ValueError(
                    f"associated-graded block {index} must have target_dim rows"
                )
            if _matrix_width(block) != source_dim:
                raise ValueError(
                    f"associated-graded block {index} must have source_dim columns"
                )
        rank = exact_matrix_rank(block)
        ranks.append(rank)
        surjectivity_defects.append(max(0, target_dim - rank))
        kernel_excess_dimensions.append(max(0, source_dim - rank))

    difference = tuple(left - right for left, right in zip(source, target))
    hilbert_defect_rank = exact_matrix_rank((difference,)) if difference else 0
    hilbert_equal = hilbert_defect_rank == 0
    gr_surjective = all(defect == 0 for defect in surjectivity_defects)
    gr_isomorphism = hilbert_equal and gr_surjective
    defective_blocks = tuple(
        index
        for index, (surj, kernel) in enumerate(
            zip(surjectivity_defects, kernel_excess_dimensions)
        )
        if surj != 0 or kernel != 0
    )
    return YangianPBWAssociatedGradedGate(
        finite_bound=finite_bound,
        max_mode=max_mode,
        block_count=len(source),
        source_hilbert_vector=source,
        target_hilbert_vector=target,
        source_total_dimension=sum(source),
        target_total_dimension=sum(target),
        hilbert_vector_difference=difference,
        hilbert_vector_defect_rank=hilbert_defect_rank,
        block_ranks=tuple(ranks),
        block_surjectivity_defects=tuple(surjectivity_defects),
        block_kernel_excess_dimensions=tuple(kernel_excess_dimensions),
        defective_blocks=defective_blocks,
        hilbert_vectors_equal=hilbert_equal,
        associated_graded_surjective=gr_surjective,
        associated_graded_isomorphism=gr_isomorphism,
        finite_filtered_isomorphism=gr_isomorphism,
        closed=gr_isomorphism,
        status=(
            "FINITE_YANGIAN_PBW_ASSOCIATED_GRADED_GATE"
            if gr_isomorphism
            else "FINITE_YANGIAN_PBW_ASSOCIATED_GRADED_DEFECT"
        ),
    )


def _identity_matrix(size: int) -> Matrix:
    if size < 0:
        raise ValueError("identity size must be nonnegative")
    return tuple(
        tuple(Fraction(1 if row == column else 0) for column in range(size))
        for row in range(size)
    )


def yangian_spectral_r_matrix_equation_gate(
    yang_baxter_left_matrix: Iterable[Iterable[Any]],
    yang_baxter_right_matrix: Iterable[Iterable[Any]],
    unitarity_product_matrix: Iterable[Iterable[Any]],
    *,
    identity_matrix: Optional[Iterable[Iterable[Any]]] = None,
    finite_bound: int = 0,
    max_mode: int = 0,
) -> YangianSpectralRMatrixEquationGate:
    r"""Check finite strict R-matrix equations from supplied composites.

    The inputs are the finite matrices for the two Yang-Baxter composites
    and for the pairwise unitarity product.  This function does not
    construct the spectral connection, holonomy, or the pairwise R-matrix.
    """
    if finite_bound < 0:
        raise ValueError("finite_bound must be nonnegative")
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")
    ybe_left = _fraction_matrix(yang_baxter_left_matrix)
    ybe_right = _fraction_matrix(yang_baxter_right_matrix)
    unitarity = _fraction_matrix(unitarity_product_matrix)
    if not ybe_left:
        raise ValueError("yang_baxter_left_matrix must be nonempty")
    dimension = len(ybe_left)
    expected_shape = (dimension, dimension)
    _validate_matrix_shape(ybe_left, expected_shape, "yang_baxter_left_matrix")
    _validate_matrix_shape(ybe_right, expected_shape, "yang_baxter_right_matrix")
    _validate_matrix_shape(unitarity, expected_shape, "unitarity_product_matrix")
    identity = (
        _identity_matrix(dimension)
        if identity_matrix is None
        else _fraction_matrix(identity_matrix)
    )
    _validate_matrix_shape(identity, expected_shape, "identity_matrix")

    ybe_difference = _matrix_difference(ybe_left, ybe_right)
    unitarity_difference = _matrix_difference(unitarity, identity)
    ybe_defect_rank = exact_matrix_rank(ybe_difference)
    unitarity_defect_rank = exact_matrix_rank(unitarity_difference)
    ybe_satisfied = ybe_defect_rank == 0
    unitarity_satisfied = unitarity_defect_rank == 0
    strict = ybe_satisfied and unitarity_satisfied
    return YangianSpectralRMatrixEquationGate(
        finite_bound=finite_bound,
        max_mode=max_mode,
        matrix_dimension=dimension,
        ybe_left=ybe_left,
        ybe_right=ybe_right,
        ybe_difference=ybe_difference,
        unitarity_product=unitarity,
        identity_matrix=identity,
        unitarity_difference=unitarity_difference,
        ybe_defect_rank=ybe_defect_rank,
        unitarity_defect_rank=unitarity_defect_rank,
        yang_baxter_satisfied=ybe_satisfied,
        unitarity_satisfied=unitarity_satisfied,
        strict_r_matrix_equations_satisfied=strict,
        closed=strict,
        status=(
            "FINITE_YANGIAN_SPECTRAL_R_MATRIX_EQUATION_GATE"
            if strict
            else "FINITE_YANGIAN_SPECTRAL_R_MATRIX_EQUATION_DEFECT"
        ),
    )


def yangian_spectral_associator_obstruction_packet(
    max_discriminant: int = 8,
    max_mode: int = 2,
    *,
    associator_cochain: Iterable[Any] | None = None,
    pentagon_differential: Iterable[Iterable[Any]] | None = None,
    gauge_coboundary_basis: Iterable[Iterable[Any]] | None = None,
    gauge_constraint_matrix: Iterable[Iterable[Any]] | None = None,
) -> YangianSpectralAssociatorObstructionPacket:
    r"""Evaluate the finite spectral associator obstruction for the Yangian lane.

    The supplied cochain is the finite spectral associator Phi_H in a chosen
    basis of C^3_spec.  The pentagon differential is d_3, and the gauge rows
    span the admissible B^3_spec.  Vanishing of d_3 Phi_H gives the finite
    quasi-factorization criterion.  Membership of Phi_H in the admissible
    gauge row span is the finite strict R-matrix criterion.  This function
    does not construct the spectral connection, its holonomy, or the OPE
    residue operators.
    """
    if max_mode < 0:
        raise ValueError("max_mode must be nonnegative")
    current_packet = yangian_current_candidate_packet(max_discriminant, max_mode)

    missing = []
    if associator_cochain is None:
        missing.append("spectral_associator_cochain")
    if pentagon_differential is None:
        missing.append("spectral_pentagon_differential")
    if gauge_coboundary_basis is None:
        missing.append("admissible_gauge_coboundary_basis")
    if missing:
        return YangianSpectralAssociatorObstructionPacket(
            max_discriminant=max_discriminant,
            max_mode=max_mode,
            current_dimension=current_packet.total_dimension,
            current_support=current_packet.support,
            cochain_dimension=0,
            associator_cochain=(),
            pentagon_differential=(),
            gauge_coboundary_basis=(),
            gauge_constraint_matrix=(),
            associator_boundary=(),
            gauge_cocycle_matrix=(),
            gauge_constraint_product=(),
            pentagon_equation_count=0,
            gauge_generator_count=0,
            gauge_constraint_count=0,
            cocycle_defect_rank=0,
            gauge_cocycle_defect_rank=0,
            gauge_constraint_defect_rank=0,
            strictification_defect=1,
            quasi_factorization_criterion_satisfied=False,
            strict_r_matrix_criterion_satisfied=False,
            missing_inputs=tuple(missing),
            status="FINITE_SPECTRAL_ASSOCIATOR_DATA_MISSING",
        )

    associator = _fraction_vector(associator_cochain)
    cochain_dimension = len(associator)
    pentagon = _fraction_matrix(pentagon_differential or ())
    gauge_basis = _fraction_matrix(gauge_coboundary_basis or ())
    gauge_constraint = _fraction_matrix(gauge_constraint_matrix or ())
    _validate_cochain_matrix_width(pentagon, cochain_dimension, "spectral pentagon differential")
    _validate_cochain_matrix_width(gauge_basis, cochain_dimension, "admissible gauge coboundary rows")
    _validate_cochain_matrix_width(gauge_constraint, cochain_dimension, "spectral gauge constraint matrix")

    associator_boundary = _matrix_vector_product(pentagon, associator)
    cocycle_defect = exact_matrix_rank((associator_boundary,))
    gauge_cocycle_matrix = _matrix_product(pentagon, _matrix_transpose(gauge_basis))
    gauge_constraint_product = _matrix_product(gauge_basis, _matrix_transpose(gauge_constraint))
    gauge_cocycle_defect = exact_matrix_rank(gauge_cocycle_matrix)
    gauge_constraint_defect = exact_matrix_rank(gauge_constraint_product)
    strictification_defect = 0 if vector_in_row_span(associator, gauge_basis) else 1
    quasi_factorization = (
        cocycle_defect == 0
        and gauge_cocycle_defect == 0
        and gauge_constraint_defect == 0
    )
    strict_r_matrix = quasi_factorization and strictification_defect == 0
    if cocycle_defect or gauge_cocycle_defect:
        status = "FINITE_SPECTRAL_ASSOCIATOR_COCYCLE_DEFECT"
    elif gauge_constraint_defect:
        status = "FINITE_SPECTRAL_ASSOCIATOR_GAUGE_DEFECT"
    elif strictification_defect:
        status = "FINITE_SPECTRAL_ASSOCIATOR_CLASS_NONTRIVIAL"
    else:
        status = "FINITE_SPECTRAL_STRICT_R_MATRIX_CRITERION_SATISFIED"
    return YangianSpectralAssociatorObstructionPacket(
        max_discriminant=max_discriminant,
        max_mode=max_mode,
        current_dimension=current_packet.total_dimension,
        current_support=current_packet.support,
        cochain_dimension=cochain_dimension,
        associator_cochain=associator,
        pentagon_differential=pentagon,
        gauge_coboundary_basis=gauge_basis,
        gauge_constraint_matrix=gauge_constraint,
        associator_boundary=associator_boundary,
        gauge_cocycle_matrix=gauge_cocycle_matrix,
        gauge_constraint_product=gauge_constraint_product,
        pentagon_equation_count=len(pentagon),
        gauge_generator_count=len(gauge_basis),
        gauge_constraint_count=len(gauge_constraint),
        cocycle_defect_rank=cocycle_defect,
        gauge_cocycle_defect_rank=gauge_cocycle_defect,
        gauge_constraint_defect_rank=gauge_constraint_defect,
        strictification_defect=strictification_defect,
        quasi_factorization_criterion_satisfied=quasi_factorization,
        strict_r_matrix_criterion_satisfied=strict_r_matrix,
        missing_inputs=(),
        status=status,
    )


def yangian_spectral_associator_transition(
    upper_discriminant: int,
    lower_discriminant: int,
    upper_mode: int,
    lower_mode: int,
    *,
    upper_associator_cochain: Iterable[Any],
    lower_associator_cochain: Iterable[Any],
    upper_pentagon_differential: Iterable[Iterable[Any]],
    lower_pentagon_differential: Iterable[Iterable[Any]],
    upper_gauge_coboundary_basis: Iterable[Iterable[Any]],
    lower_gauge_coboundary_basis: Iterable[Iterable[Any]],
    cochain_projection: Iterable[Iterable[Any]],
    boundary_projection: Iterable[Iterable[Any]],
    upper_gauge_constraint_matrix: Iterable[Iterable[Any]] | None = None,
    lower_gauge_constraint_matrix: Iterable[Iterable[Any]] | None = None,
) -> YangianSpectralAssociatorTransition:
    r"""Check finite heightwise compatibility of spectral obstruction packets."""
    if lower_discriminant > upper_discriminant:
        raise ValueError("lower_discriminant must be <= upper_discriminant")
    if lower_mode > upper_mode:
        raise ValueError("lower_mode must be <= upper_mode")

    upper_assoc = _fraction_vector(upper_associator_cochain)
    lower_assoc = _fraction_vector(lower_associator_cochain)
    upper_pentagon = _fraction_matrix(upper_pentagon_differential)
    lower_pentagon = _fraction_matrix(lower_pentagon_differential)
    upper_gauge = _fraction_matrix(upper_gauge_coboundary_basis)
    lower_gauge = _fraction_matrix(lower_gauge_coboundary_basis)
    cochain_proj = _fraction_matrix(cochain_projection)
    boundary_proj = _fraction_matrix(boundary_projection)

    upper = yangian_spectral_associator_obstruction_packet(
        upper_discriminant,
        upper_mode,
        associator_cochain=upper_assoc,
        pentagon_differential=upper_pentagon,
        gauge_coboundary_basis=upper_gauge,
        gauge_constraint_matrix=upper_gauge_constraint_matrix,
    )
    lower = yangian_spectral_associator_obstruction_packet(
        lower_discriminant,
        lower_mode,
        associator_cochain=lower_assoc,
        pentagon_differential=lower_pentagon,
        gauge_coboundary_basis=lower_gauge,
        gauge_constraint_matrix=lower_gauge_constraint_matrix,
    )

    if len(cochain_proj) != len(lower_assoc):
        raise ValueError("cochain_projection must have lower cochain height")
    if cochain_proj and _matrix_width(cochain_proj) != len(upper_assoc):
        raise ValueError("cochain_projection must have upper cochain width")
    if len(boundary_proj) != len(lower_pentagon):
        raise ValueError("boundary_projection must have lower pentagon height")
    if boundary_proj and _matrix_width(boundary_proj) != len(upper_pentagon):
        raise ValueError("boundary_projection must have upper pentagon height")

    projected_associator = _matrix_vector_product(cochain_proj, upper_assoc)
    associator_projection_difference = _vector_difference(projected_associator, lower_assoc)
    associator_projection_defect = exact_matrix_rank((associator_projection_difference,))
    lower_after_projection = _matrix_product(lower_pentagon, cochain_proj)
    projection_after_upper = _matrix_product(boundary_proj, upper_pentagon)
    pentagon_commutator_matrix = _matrix_difference(lower_after_projection, projection_after_upper)
    pentagon_commutator_defect = exact_matrix_rank(pentagon_commutator_matrix)
    gauge_projection_failures = []
    projected_gauge_rows = []
    for index, upper_row in enumerate(upper_gauge):
        projected_row = _matrix_vector_product(cochain_proj, upper_row)
        projected_gauge_rows.append(projected_row)
        if not vector_in_row_span(projected_row, lower_gauge):
            gauge_projection_failures.append(f"gauge:{index}")
    gauge_projection_defect = len(gauge_projection_failures)

    defects = []
    if associator_projection_defect:
        defects.append("associator_projection")
    if pentagon_commutator_defect:
        defects.append("pentagon_commutator")
    defects.extend(gauge_projection_failures)
    if not upper.quasi_factorization_criterion_satisfied:
        defects.append("upper_not_quasi_factorization")
    if not lower.quasi_factorization_criterion_satisfied:
        defects.append("lower_not_quasi_factorization")

    transition_commutes = not defects
    return YangianSpectralAssociatorTransition(
        upper_discriminant=upper_discriminant,
        lower_discriminant=lower_discriminant,
        upper_mode=upper_mode,
        lower_mode=lower_mode,
        upper=upper,
        lower=lower,
        cochain_projection_shape=(len(cochain_proj), _matrix_width(cochain_proj)),
        boundary_projection_shape=(len(boundary_proj), _matrix_width(boundary_proj)),
        projected_associator=projected_associator,
        associator_projection_difference=associator_projection_difference,
        lower_after_projection=lower_after_projection,
        projection_after_upper=projection_after_upper,
        pentagon_commutator_matrix=pentagon_commutator_matrix,
        projected_gauge_rows=tuple(projected_gauge_rows),
        gauge_projection_failures=tuple(gauge_projection_failures),
        associator_projection_defect=associator_projection_defect,
        pentagon_commutator_defect=pentagon_commutator_defect,
        gauge_projection_defect=gauge_projection_defect,
        upper_quasi_factorization=upper.quasi_factorization_criterion_satisfied,
        lower_quasi_factorization=lower.quasi_factorization_criterion_satisfied,
        defects=tuple(defects),
        transition_commutes=transition_commutes,
        status="FINITE_SPECTRAL_ASSOCIATOR_TRANSITION" if transition_commutes else "FINITE_SPECTRAL_ASSOCIATOR_TRANSITION_DEFECT",
    )


def finite_bridge_transition_square(
    bridge: str,
    upper_height: int,
    lower_height: int,
    *,
    upper_comparison_map: Iterable[Iterable[Any]],
    lower_comparison_map: Iterable[Iterable[Any]],
    source_transition: Iterable[Iterable[Any]],
    target_transition: Iterable[Iterable[Any]],
) -> FiniteBridgeTransitionSquare:
    r"""Check one supplied finite bridge square.

    The matrices represent Xi_upper: source_upper -> target_upper,
    Xi_lower: source_lower -> target_lower, T: source_upper -> source_lower,
    and R: target_upper -> target_lower. The square commutes exactly when
    R * Xi_upper = Xi_lower * T.

    The empty tuple represents the unique zero-dimensional matrix. Missing
    bridge data is represented at the system-report layer by an absent bridge
    label, not by an empty component matrix.
    """
    if lower_height > upper_height:
        raise ValueError("lower_height must be <= upper_height")

    upper_map = _fraction_matrix(upper_comparison_map)
    lower_map = _fraction_matrix(lower_comparison_map)
    source = _fraction_matrix(source_transition)
    target = _fraction_matrix(target_transition)

    target_upper_dimension, source_upper_dimension = _matrix_shape(upper_map)
    target_lower_dimension, source_lower_dimension = _matrix_shape(lower_map)
    _validate_matrix_shape(source, (source_lower_dimension, source_upper_dimension), "source_transition")
    _validate_matrix_shape(target, (target_lower_dimension, target_upper_dimension), "target_transition")

    left = _matrix_product(target, upper_map)
    right = _matrix_product(lower_map, source)
    commutator = _matrix_difference(left, right)
    defect_rank = exact_matrix_rank(commutator)
    transition_commutes = defect_rank == 0

    return FiniteBridgeTransitionSquare(
        bridge=bridge,
        upper_height=upper_height,
        lower_height=lower_height,
        upper_map_shape=_matrix_shape(upper_map),
        lower_map_shape=_matrix_shape(lower_map),
        source_transition_shape=_matrix_shape(source),
        target_transition_shape=_matrix_shape(target),
        target_after_upper_map=left,
        lower_map_after_source=right,
        commutator_matrix=commutator,
        commutator_defect_rank=defect_rank,
        transition_commutes=transition_commutes,
        status="FINITE_BRIDGE_TRANSITION_SQUARE" if transition_commutes else "FINITE_BRIDGE_TRANSITION_SQUARE_DEFECT",
    )


def finite_bridge_system_transition_report(
    squares: Iterable[FiniteBridgeTransitionSquare],
    required_bridges: Tuple[str, ...] = REQUIRED_BRIDGE_COMPONENTS,
) -> FiniteBridgeSystemTransitionReport:
    r"""Aggregate the five finite bridge-square tests at one transition.

    The bridge system commutes exactly when every required component is
    present at the same height transition and each component commutator
    has rank zero.
    """
    square_list = tuple(squares)
    if not square_list:
        raise ValueError("at least one bridge square is required")

    upper_height = square_list[0].upper_height
    lower_height = square_list[0].lower_height
    by_bridge: Dict[str, FiniteBridgeTransitionSquare] = {}
    for square in square_list:
        if square.upper_height != upper_height or square.lower_height != lower_height:
            raise ValueError("bridge squares must have common heights")
        if square.bridge in by_bridge:
            raise ValueError(f"duplicate bridge square: {square.bridge}")
        by_bridge[square.bridge] = square

    missing = tuple(bridge for bridge in required_bridges if bridge not in by_bridge)
    component_defect_ranks = {
        bridge: by_bridge[bridge].commutator_defect_rank
        for bridge in required_bridges
        if bridge in by_bridge
    }
    defective = tuple(
        bridge
        for bridge, defect_rank in component_defect_ranks.items()
        if defect_rank != 0
    )
    component_statuses = {
        bridge: by_bridge[bridge].status
        for bridge in required_bridges
        if bridge in by_bridge
    }
    component_gates = {
        bridge: by_bridge[bridge].transition_commutes
        for bridge in required_bridges
        if bridge in by_bridge
    }
    component_square_data = {
        bridge: {
            "upper_map_shape": by_bridge[bridge].upper_map_shape,
            "lower_map_shape": by_bridge[bridge].lower_map_shape,
            "source_transition_shape": by_bridge[bridge].source_transition_shape,
            "target_transition_shape": by_bridge[bridge].target_transition_shape,
            "target_after_upper_map": by_bridge[bridge].target_after_upper_map,
            "lower_map_after_source": by_bridge[bridge].lower_map_after_source,
            "commutator_matrix": by_bridge[bridge].commutator_matrix,
            "commutator_defect_rank": by_bridge[bridge].commutator_defect_rank,
        }
        for bridge in required_bridges
        if bridge in by_bridge
    }
    all_squares_commute = not missing and not defective

    return FiniteBridgeSystemTransitionReport(
        upper_height=upper_height,
        lower_height=lower_height,
        required_bridges=required_bridges,
        present_bridges=tuple(square.bridge for square in square_list),
        missing_bridges=missing,
        defective_bridges=defective,
        component_statuses=component_statuses,
        component_gates=component_gates,
        component_defect_ranks=component_defect_ranks,
        component_square_data=component_square_data,
        all_squares_commute=all_squares_commute,
        status=(
            "FINITE_BRIDGE_SYSTEM_TRANSITION"
            if all_squares_commute
            else "FINITE_BRIDGE_SYSTEM_TRANSITION_DEFECT"
        ),
    )


def finite_bridge_exactness_step_report(
    bridge: str,
    upper_height: int,
    lower_height: int,
    *,
    upper_comparison_map: Iterable[Iterable[Any]],
    lower_comparison_map: Iterable[Iterable[Any]],
    source_transition: Iterable[Iterable[Any]],
    target_transition: Iterable[Iterable[Any]],
) -> FiniteBridgeExactnessStepReport:
    r"""Check the finite Mittag-Leffler gate for one bridge component.

    The empty tuple is the legitimate zero-dimensional component. Absent
    component data is represented only by omitting the bridge from a system
    exactness report.
    """
    upper_map = _fraction_matrix(upper_comparison_map)
    lower_map = _fraction_matrix(lower_comparison_map)
    source = _fraction_matrix(source_transition)
    target = _fraction_matrix(target_transition)
    square = finite_bridge_transition_square(
        bridge,
        upper_height,
        lower_height,
        upper_comparison_map=upper_map,
        lower_comparison_map=lower_map,
        source_transition=source,
        target_transition=target,
    )

    target_lower_dimension, source_lower_dimension = _matrix_shape(lower_map)
    source_rank = exact_matrix_rank(source)
    target_rank = exact_matrix_rank(target)
    source_surjective = source_rank == source_lower_dimension
    target_surjective = target_rank == target_lower_dimension
    source_surjectivity_defect = source_lower_dimension - source_rank
    target_surjectivity_defect = target_lower_dimension - target_rank

    upper_kernel = _matrix_nullspace_basis(upper_map)
    lower_kernel = _matrix_nullspace_basis(lower_map)
    target_upper_image = _matrix_product(target, upper_map)
    lower_image_rank = exact_matrix_rank(lower_map)
    combined_image_rank = exact_matrix_rank(
        _matrix_horizontal_concat(lower_map, target_upper_image)
    )
    image_landing_defect_rank = combined_image_rank - lower_image_rank
    image_well_defined = image_landing_defect_rank == 0
    image_transition_rank = exact_matrix_rank(target_upper_image)
    image_surjective = image_well_defined and image_transition_rank == lower_image_rank
    lower_cokernel_dimension = target_lower_dimension - lower_image_rank
    combined_target_rank = exact_matrix_rank(_matrix_horizontal_concat(lower_map, target))
    cokernel_transition_rank = combined_target_rank - lower_image_rank
    cokernel_well_defined = image_well_defined
    cokernel_surjective = (
        cokernel_well_defined
        and cokernel_transition_rank == lower_cokernel_dimension
    )

    kernel_images = tuple(_matrix_vector_product(source, vector) for vector in upper_kernel)
    lower_kernel_landing = tuple(_matrix_vector_product(lower_map, vector) for vector in kernel_images)
    kernel_landing_defect_rank = _column_vector_rank(lower_kernel_landing)
    kernel_image_rank = _column_vector_rank(kernel_images)
    kernel_well_defined = kernel_landing_defect_rank == 0
    kernel_surjectivity_defect = max(0, len(lower_kernel) - kernel_image_rank)
    image_surjectivity_defect = max(0, lower_image_rank - image_transition_rank)
    cokernel_surjectivity_defect = max(0, lower_cokernel_dimension - cokernel_transition_rank)
    kernel_surjective = kernel_well_defined and kernel_image_rank == len(lower_kernel)

    defects: List[str] = []
    if not square.transition_commutes:
        defects.append("square_commutator_nonzero")
    if not source_surjective:
        defects.append("source_transition_not_surjective")
    if not target_surjective:
        defects.append("target_transition_not_surjective")
    if not image_well_defined:
        defects.append("image_transition_not_well_defined")
    if not kernel_well_defined:
        defects.append("kernel_transition_not_well_defined")
    if not kernel_surjective:
        defects.append("kernel_transition_not_surjective")
    if image_well_defined and not image_surjective:
        defects.append("image_transition_not_surjective")
    if cokernel_well_defined and not cokernel_surjective:
        defects.append("cokernel_transition_not_surjective")
    ml_exactness_gate = not defects

    return FiniteBridgeExactnessStepReport(
        bridge=bridge,
        upper_height=upper_height,
        lower_height=lower_height,
        square=square,
        upper_comparison_map=upper_map,
        lower_comparison_map=lower_map,
        source_transition_matrix=source,
        target_transition_matrix=target,
        upper_kernel_basis=upper_kernel,
        lower_kernel_basis=lower_kernel,
        kernel_image_vectors=kernel_images,
        kernel_landing_vectors=lower_kernel_landing,
        target_upper_image=target_upper_image,
        image_span_matrix=_matrix_horizontal_concat(lower_map, target_upper_image),
        cokernel_span_matrix=_matrix_horizontal_concat(lower_map, target),
        lower_source_dimension=source_lower_dimension,
        lower_target_dimension=target_lower_dimension,
        lower_image_rank=lower_image_rank,
        lower_cokernel_dimension=lower_cokernel_dimension,
        source_transition_rank=source_rank,
        target_transition_rank=target_rank,
        upper_kernel_dimension=len(upper_kernel),
        lower_kernel_dimension=len(lower_kernel),
        kernel_landing_defect_rank=kernel_landing_defect_rank,
        image_landing_defect_rank=image_landing_defect_rank,
        kernel_image_rank=kernel_image_rank,
        image_transition_rank=image_transition_rank,
        cokernel_transition_rank=cokernel_transition_rank,
        source_surjectivity_defect=source_surjectivity_defect,
        target_surjectivity_defect=target_surjectivity_defect,
        kernel_surjectivity_defect=kernel_surjectivity_defect,
        image_surjectivity_defect=image_surjectivity_defect,
        cokernel_surjectivity_defect=cokernel_surjectivity_defect,
        source_transition_surjective=source_surjective,
        target_transition_surjective=target_surjective,
        kernel_transition_well_defined=kernel_well_defined,
        image_transition_well_defined=image_well_defined,
        cokernel_transition_well_defined=cokernel_well_defined,
        kernel_transition_surjective=kernel_surjective,
        image_transition_surjective=image_surjective,
        cokernel_transition_surjective=cokernel_surjective,
        defects=tuple(defects),
        ml_exactness_gate=ml_exactness_gate,
        status=(
            "FINITE_BRIDGE_ML_EXACTNESS_STEP"
            if ml_exactness_gate
            else "FINITE_BRIDGE_ML_EXACTNESS_STEP_DEFECT"
        ),
    )


def finite_bridge_system_exactness_report(
    reports: Iterable[FiniteBridgeExactnessStepReport],
    required_bridges: Tuple[str, ...] = REQUIRED_BRIDGE_COMPONENTS,
) -> FiniteBridgeSystemExactnessReport:
    r"""Aggregate the finite Mittag-Leffler gates for all bridge components."""
    report_list = tuple(reports)
    if not report_list:
        raise ValueError("at least one bridge exactness report is required")

    upper_height = report_list[0].upper_height
    lower_height = report_list[0].lower_height
    by_bridge: Dict[str, FiniteBridgeExactnessStepReport] = {}
    for report in report_list:
        if report.upper_height != upper_height or report.lower_height != lower_height:
            raise ValueError("bridge exactness reports must have common heights")
        if report.bridge in by_bridge:
            raise ValueError(f"duplicate bridge exactness report: {report.bridge}")
        by_bridge[report.bridge] = report

    missing = tuple(bridge for bridge in required_bridges if bridge not in by_bridge)
    component_statuses = {
        bridge: by_bridge[bridge].status
        for bridge in required_bridges
        if bridge in by_bridge
    }
    component_defects = {
        bridge: by_bridge[bridge].defects
        for bridge in required_bridges
        if bridge in by_bridge
    }
    component_gates = {
        bridge: {
            "transition_square_commutes": by_bridge[bridge].square.transition_commutes,
            "source_transition_surjective": by_bridge[bridge].source_transition_surjective,
            "target_transition_surjective": by_bridge[bridge].target_transition_surjective,
            "kernel_transition_well_defined": by_bridge[bridge].kernel_transition_well_defined,
            "kernel_transition_surjective": by_bridge[bridge].kernel_transition_surjective,
            "image_transition_well_defined": by_bridge[bridge].image_transition_well_defined,
            "image_transition_surjective": by_bridge[bridge].image_transition_surjective,
            "cokernel_transition_well_defined": by_bridge[bridge].cokernel_transition_well_defined,
            "cokernel_transition_surjective": by_bridge[bridge].cokernel_transition_surjective,
        }
        for bridge in required_bridges
        if bridge in by_bridge
    }
    component_rank_data = {
        bridge: {
            "lower_source_dimension": by_bridge[bridge].lower_source_dimension,
            "lower_target_dimension": by_bridge[bridge].lower_target_dimension,
            "lower_image_rank": by_bridge[bridge].lower_image_rank,
            "lower_kernel_dimension": by_bridge[bridge].lower_kernel_dimension,
            "lower_cokernel_dimension": by_bridge[bridge].lower_cokernel_dimension,
            "source_transition_rank": by_bridge[bridge].source_transition_rank,
            "target_transition_rank": by_bridge[bridge].target_transition_rank,
            "kernel_landing_defect_rank": by_bridge[bridge].kernel_landing_defect_rank,
            "kernel_image_rank": by_bridge[bridge].kernel_image_rank,
            "image_landing_defect_rank": by_bridge[bridge].image_landing_defect_rank,
            "image_transition_rank": by_bridge[bridge].image_transition_rank,
            "cokernel_transition_rank": by_bridge[bridge].cokernel_transition_rank,
            "source_surjectivity_defect": by_bridge[bridge].source_surjectivity_defect,
            "target_surjectivity_defect": by_bridge[bridge].target_surjectivity_defect,
            "kernel_surjectivity_defect": by_bridge[bridge].kernel_surjectivity_defect,
            "image_surjectivity_defect": by_bridge[bridge].image_surjectivity_defect,
            "cokernel_surjectivity_defect": by_bridge[bridge].cokernel_surjectivity_defect,
        }
        for bridge in required_bridges
        if bridge in by_bridge
    }
    component_exactness_data = {
        bridge: {
            "upper_comparison_map": by_bridge[bridge].upper_comparison_map,
            "lower_comparison_map": by_bridge[bridge].lower_comparison_map,
            "source_transition_matrix": by_bridge[bridge].source_transition_matrix,
            "target_transition_matrix": by_bridge[bridge].target_transition_matrix,
            "upper_kernel_basis": by_bridge[bridge].upper_kernel_basis,
            "lower_kernel_basis": by_bridge[bridge].lower_kernel_basis,
            "kernel_image_vectors": by_bridge[bridge].kernel_image_vectors,
            "kernel_landing_vectors": by_bridge[bridge].kernel_landing_vectors,
            "target_upper_image": by_bridge[bridge].target_upper_image,
            "image_span_matrix": by_bridge[bridge].image_span_matrix,
            "cokernel_span_matrix": by_bridge[bridge].cokernel_span_matrix,
        }
        for bridge in required_bridges
        if bridge in by_bridge
    }
    defective = tuple(
        bridge
        for bridge in required_bridges
        if bridge in by_bridge and not by_bridge[bridge].ml_exactness_gate
    )
    all_components_ml_exact = not missing and not defective

    return FiniteBridgeSystemExactnessReport(
        upper_height=upper_height,
        lower_height=lower_height,
        required_bridges=required_bridges,
        present_bridges=tuple(report.bridge for report in report_list),
        missing_bridges=missing,
        defective_bridges=defective,
        component_statuses=component_statuses,
        component_defects=component_defects,
        component_gates=component_gates,
        component_rank_data=component_rank_data,
        component_exactness_data=component_exactness_data,
        all_components_ml_exact=all_components_ml_exact,
        status=(
            "FINITE_BRIDGE_SYSTEM_ML_EXACTNESS"
            if all_components_ml_exact
            else "FINITE_BRIDGE_SYSTEM_ML_EXACTNESS_DEFECT"
        ),
    )


def finite_bridge_exactness_tower_report(
    reports: Iterable[FiniteBridgeExactnessStepReport],
) -> FiniteBridgeExactnessTowerReport:
    r"""Compose adjacent finite Mittag-Leffler gates for one bridge component."""
    report_list = tuple(reports)
    if not report_list:
        raise ValueError("at least one bridge exactness report is required")

    bridge = report_list[0].bridge
    for report in report_list:
        if report.bridge != bridge:
            raise ValueError("bridge exactness reports must have a common bridge")
    for upper_step, lower_step in zip(report_list, report_list[1:]):
        if upper_step.lower_height != lower_step.upper_height:
            raise ValueError("bridge exactness reports must form a contiguous height tower")
        if upper_step.lower_comparison_map != lower_step.upper_comparison_map:
            raise ValueError("bridge exactness reports must identify adjacent comparison maps")

    composed_source = report_list[0].source_transition_matrix
    composed_target = report_list[0].target_transition_matrix
    for report in report_list[1:]:
        composed_source = _matrix_product(report.source_transition_matrix, composed_source)
        composed_target = _matrix_product(report.target_transition_matrix, composed_target)

    composed_step = finite_bridge_exactness_step_report(
        bridge,
        report_list[0].upper_height,
        report_list[-1].lower_height,
        upper_comparison_map=report_list[0].upper_comparison_map,
        lower_comparison_map=report_list[-1].lower_comparison_map,
        source_transition=composed_source,
        target_transition=composed_target,
    )
    step_defects = {
        f"{report.upper_height}->{report.lower_height}": report.defects
        for report in report_list
        if not report.ml_exactness_gate
    }
    all_steps_ml_exact = all(report.ml_exactness_gate for report in report_list)
    tower_ml_exact = all_steps_ml_exact and composed_step.ml_exactness_gate

    return FiniteBridgeExactnessTowerReport(
        bridge=bridge,
        upper_height=report_list[0].upper_height,
        lower_height=report_list[-1].lower_height,
        step_heights=tuple(
            (report.upper_height, report.lower_height) for report in report_list
        ),
        step_count=len(report_list),
        step_reports=report_list,
        composed_source_transition=composed_source,
        composed_target_transition=composed_target,
        composed_step_report=composed_step,
        step_defects=step_defects,
        all_steps_ml_exact=all_steps_ml_exact,
        tower_ml_exact=tower_ml_exact,
        status=(
            "FINITE_BRIDGE_ML_EXACTNESS_TOWER"
            if tower_ml_exact
            else "FINITE_BRIDGE_ML_EXACTNESS_TOWER_DEFECT"
        ),
    )


def yangian_witness(max_discriminant: int = 8) -> YangianWitness:
    r"""Finite Yangian boundary packets with the operator construction still open."""
    table = _bar.k3e_product_by_discriminant(max_discriminant)
    current_template = (
        "e_D^{(a)}(u) = Res_{z=u} V_eps(alpha_a, z), "
        "with h_eps = (D + 1) - D * eps"
    )
    return YangianWitness(
        max_discriminant=max_discriminant,
        current_template=current_template,
        epsilon_limit=YANGIAN_LIMIT_EPSILON_1,
        weight_template=YANGIAN_WEIGHT_TEMPLATE,
        sample_multiplicities={D: table[D] for D in sorted(table) if D in {-1, 0, 3, 4, 7, 8}},
        current_packet=yangian_current_candidate_packet(max_discriminant=max_discriminant),
        spectral_kernel_packet=yangian_spectral_kernel_label_packet(max_discriminant=max_discriminant),
        self_ope_pole_packet=yangian_self_ope_pole_layer_packet(max_discriminant=max_discriminant),
        spectral_associator_obstruction=yangian_spectral_associator_obstruction_packet(
            max_discriminant=max_discriminant,
        ),
        current_limit_weight_one=True,
        status=(
            "finite current, pole-layer, and spectral-obstruction "
            "boundary packets; all-orders deformation still missing"
        ),
    )


def finite_bridge_witness(max_discriminant: int = 8, max_degree: int = 5, max_n: int = 10) -> FiniteBridgeWitness:
    r"""Package the finite bridge witnesses into one record."""
    return FiniteBridgeWitness(
        scattering=scattering_witness(max_discriminant=max_discriminant),
        bar=bar_witness(max_degree=max_degree),
        rademacher=rademacher_witness(max_n=max_n),
        brst=brst_witness(),
        yangian=yangian_witness(max_discriminant=max_discriminant),
        open_lemmas=[
            "scattering lemma",
            "bar lemma",
            "rademacher lemma",
            "brst lemma",
            "yangian lemma",
        ],
    )


def bridge_obstruction_record(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> BridgeObstructionRecord:
    """Separate the low-height witnesses from the still-missing theorem input."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    witness = finite_bridge_witness(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
    )
    witnessed = BridgeWitnessSplit(
        scattering=witness.scattering,
        bar=witness.bar,
        rademacher=witness.rademacher,
    )
    operator_boundary = BridgeOperatorBoundarySplit(
        brst=witness.brst,
        yangian=witness.yangian,
    )
    missing_theorems = BridgeMissingTheorems(
        scattering=[
            "global motivic integration morphism construction",
            "heightwise chamber-composition theorem",
            "transition-map commutation theorem",
        ],
        bar=[
            "filtered bar-complex theorem",
            "associated-graded identification theorem",
            "specialisation compatibility theorem",
        ],
        rademacher=[
            "protected compact-CY3 comparison theorem",
            "uniform all-height truncation-error theorem beyond the rank-one certificate",
            "Bessel-recursion compatibility theorem for the compact shadow packet",
        ],
        brst=[
            "finite-height VOA/BRST construction",
            "differential functoriality in height",
            "cohomology-packet transition theorem",
        ],
        yangian=[
            "all-orders Omega-deformed vertex-operator construction",
            "residue-class theorem on cohomology",
            "OPE / Serre / Hall-Borcherds compatibility theorem",
        ],
    )
    witnessed_bridges = closure_witnesses.bridge_construction_set
    bridge_by_missing_entry = {
        "scattering": "scattering_root_identification",
        "bar": "bkm_bar_dictionary",
        "rademacher": "shadow_rademacher_comparison",
        "brst": "brst_realization",
        "yangian": "vertex_operator_yangian",
    }
    missing_by_entry = {
        entry_name: (
            []
            if bridge_name in witnessed_bridges
            else list(getattr(missing_theorems, entry_name))
        )
        for entry_name, bridge_name in bridge_by_missing_entry.items()
    }
    missing_theorems = BridgeMissingTheorems(**missing_by_entry)

    inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "bridge_obstruction_record",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    if missing_theorems.empty and inverse_limit_gate.all_proved:
        uniform_gap = "the supplied closure witness package closes the heightwise functorial theorem for the five comparison maps"
    elif missing_theorems.empty:
        uniform_gap = (
            "the five comparison-map theorem inputs are supplied; "
            "inverse-limit exactness remains tracked by K3EInverseLimitGateRequirement"
        )
    else:
        uniform_gap = "the bridge lacks a heightwise functorial theorem for the five comparison maps"
    finite_boundary_results = {
        "scattering": [
            "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}",
            "finite_scattering_quantum_torus_gate",
            "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}",
            "finite_scattering_root_report",
        ],
        "bar": [
            "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}",
            "finite_bar_lattice_grading_report",
            "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}",
            "finite_bar_ce_chain_map_gate",
            "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}",
            "finite_bar_ce_report",
            "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}",
            "finite_bar_regularization_report",
        ],
        "rademacher": [
            "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}",
            "rademacher_polar_bessel_gate",
            "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}",
            "rademacher_truncation_error_gate",
            "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}",
            "rademacher_finite_height_certificate",
        ],
        "brst": [
            "Proposition~\\ref{prop:k3e-brst-central-charge-gate}",
            "brst_central_charge_gate",
            "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}",
            "brst_coefficient_fixture",
            "brst_coefficient_fixture_transition",
            "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}",
            "brst_no_ghost_spectral_sequence_gate",
            "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}",
            "brst_borcherds_bracket_gate",
            "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}",
            "brst_borcherds_serre_relation_gate",
            "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}",
            "brst_momentum_height_projection_gate",
        ],
        "yangian": [
            "Proposition~\\ref{prop:k3e-finite-yangian-current-candidate-packet}",
            "Proposition~\\ref{prop:k3e-finite-spectral-kernel-label-packet}",
            "Proposition~\\ref{prop:k3e-finite-self-ope-pole-layer-packet}",
            "Proposition~\\ref{prop:k3e-finite-yangian-label-tower}",
            "Proposition~\\ref{prop:k3e-finite-residue-transition}",
            "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}",
            "yangian_brst_residue_chain_gate",
            "Proposition~\\ref{prop:k3e-finite-ope-coefficient-transition}",
            "Proposition~\\ref{prop:k3e-finite-yangian-ope-serre-ideal-span-gate}",
            "yangian_ope_serre_ideal_span_gate",
            "Proposition~\\ref{prop:k3e-finite-yangian-pbw-associated-graded-gate}",
            "yangian_pbw_associated_graded_gate",
            "Proposition~\\ref{prop:k3e-finite-spectral-associator-obstruction}",
            "Proposition~\\ref{prop:k3e-finite-spectral-r-matrix-equation-gate}",
            "yangian_spectral_r_matrix_equation_gate",
            "Proposition~\\ref{prop:k3e-finite-spectral-associator-transition}",
        ],
    }
    return BridgeObstructionRecord(
        witnessed=witnessed,
        operator_boundary=operator_boundary,
        missing_theorems=missing_theorems,
        finite_boundary_results=finite_boundary_results,
        uniform_gap=uniform_gap,
    )


def bridge_proof_obligation_matrix(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> BridgeProofObligationMatrix:
    """Return a bridge-by-bridge matrix of exact missing proof obligations."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    witness = finite_bridge_witness(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
    )

    scattering = BridgeProofObligationEntry(
        witness=witness.scattering,
        finite_boundary_results=[
            "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}",
            "finite_scattering_quantum_torus_gate",
            "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}",
            "finite_scattering_root_report",
        ],
        missing=[
            "construct the global motivic integration morphism",
            "prove chamber-product preservation",
            "prove heightwise compatibility with transition maps",
            "show that no extraneous walls appear in the finite-height limit",
        ],
        target="quantum torus wall product",
        status="finite exponent theorem after recognition; natural transformation open",
    )
    bar = BridgeProofObligationEntry(
        witness=witness.bar,
        finite_boundary_results=[
            "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}",
            "finite_bar_lattice_grading_report",
            "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}",
            "finite_bar_ce_chain_map_gate",
            "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}",
            "finite_bar_ce_report",
            "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}",
            "finite_bar_regularization_report",
        ],
        missing=[
            "construct the filtered bar-complex map",
            "identify the associated graded with the finite Euler product",
            "prove compatibility with the fixed (Sigma_2, C) specialisation",
        ],
        target="BKM denominator / bar Euler product",
        status="finite bar-CE criterion after recognition; filtered morphism open",
    )
    rademacher = BridgeProofObligationEntry(
        witness=witness.rademacher,
        finite_boundary_results=[
            "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}",
            "rademacher_polar_bessel_gate",
            "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}",
            "rademacher_truncation_error_gate",
            "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}",
            "rademacher_finite_height_certificate",
        ],
        missing=[
            "construct the protected compact-CY3 comparison theorem",
            "extend the rank-one residual certificate to a uniform all-height truncation theorem",
            "prove Bessel-recursion compatibility with the compact shadow filtration",
        ],
        target="shadow resummation / Rademacher asymptotics",
        status="rank-one finite certificate; compact-CY3 shadow theorem open",
    )
    brst = BridgeProofObligationEntry(
        witness=witness.brst,
        finite_boundary_results=[
            "Proposition~\\ref{prop:k3e-brst-central-charge-gate}",
            "brst_central_charge_gate",
            "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}",
            "brst_coefficient_fixture",
            "brst_coefficient_fixture_transition",
            "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}",
            "brst_no_ghost_spectral_sequence_gate",
            "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}",
            "brst_borcherds_bracket_gate",
            "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}",
            "brst_borcherds_serre_relation_gate",
            "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}",
            "brst_momentum_height_projection_gate",
        ],
        missing=[
            "construct the finite-height VOA and BRST differential",
            "prove functoriality in height",
            "prove the cohomology packet commutes with height transition maps",
        ],
        target="BRST cohomology packet",
        status="finite supertrace fixture; worldsheet VOA and BRST differential open",
    )
    yangian = BridgeProofObligationEntry(
        witness=witness.yangian,
        finite_boundary_results=[
            "Proposition~\\ref{prop:k3e-finite-yangian-current-candidate-packet}",
            "Proposition~\\ref{prop:k3e-finite-spectral-kernel-label-packet}",
            "Proposition~\\ref{prop:k3e-finite-self-ope-pole-layer-packet}",
            "Proposition~\\ref{prop:k3e-finite-yangian-label-tower}",
            "Proposition~\\ref{prop:k3e-finite-residue-transition}",
            "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}",
            "yangian_brst_residue_chain_gate",
            "Proposition~\\ref{prop:k3e-finite-ope-coefficient-transition}",
            "Proposition~\\ref{prop:k3e-finite-yangian-ope-serre-ideal-span-gate}",
            "yangian_ope_serre_ideal_span_gate",
            "Proposition~\\ref{prop:k3e-finite-yangian-pbw-associated-graded-gate}",
            "yangian_pbw_associated_graded_gate",
            "Proposition~\\ref{prop:k3e-finite-spectral-associator-obstruction}",
            "Proposition~\\ref{prop:k3e-finite-spectral-r-matrix-equation-gate}",
            "yangian_spectral_r_matrix_equation_gate",
            "Proposition~\\ref{prop:k3e-finite-spectral-associator-transition}",
        ],
        missing=[
            "construct the all-orders Omega-deformed vertex operators",
            "prove their residues define classes on BRST cohomology",
            "prove OPE / Serre / Hall-Borcherds compatibility",
        ],
        target="Yangian current packet",
        status="finite current and obstruction packets; operator-level Yangian construction open",
    )
    closure_bridge_by_entry = {
        "scattering": "scattering_root_identification",
        "bar": "bkm_bar_dictionary",
        "rademacher": "shadow_rademacher_comparison",
        "brst": "brst_realization",
        "yangian": "vertex_operator_yangian",
    }
    entries_by_name = {
        "scattering": scattering,
        "bar": bar,
        "rademacher": rademacher,
        "brst": brst,
        "yangian": yangian,
    }
    witnessed = closure_witnesses.bridge_construction_set
    for entry_name, bridge_name in closure_bridge_by_entry.items():
        if bridge_name in witnessed:
            entries_by_name[entry_name] = replace(
                entries_by_name[entry_name],
                missing=[],
                status="proved",
            )
    return BridgeProofObligationMatrix(
        scattering=entries_by_name["scattering"],
        bar=entries_by_name["bar"],
        rademacher=entries_by_name["rademacher"],
        brst=entries_by_name["brst"],
        yangian=entries_by_name["yangian"],
    )


def source_recognition_record(
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> SourceRecognitionRecord:
    """Return the current source-side Hall/Borcherds recognition obstruction record."""
    (
        gate_witnesses,
        envelope_witnesses,
        compact_double_witnesses,
        pro_recognition_witnesses,
    ) = _source_witness_layers_from_closure(closure_witnesses)
    gate = evaluate_gate(gate_witnesses)
    envelope = evaluate_recognition_envelope(envelope_witnesses)
    obligation_matrix = source_gate_obligation_matrix(
        gate_witnesses=gate_witnesses,
        envelope_witnesses=envelope_witnesses,
    )
    task_map = source_gate_task_map()
    boundary_report = source_gate_boundary_report(
        gate_witnesses=gate_witnesses,
        envelope_witnesses=envelope_witnesses,
        compact_double_witnesses=compact_double_witnesses,
        pro_recognition_witnesses=pro_recognition_witnesses,
    )
    return SourceRecognitionRecord(
        gate=gate,
        envelope=envelope,
        obligation_matrix=obligation_matrix,
        task_map=task_map,
        boundary_report=boundary_report,
        missing_gate_witnesses=list(gate.missing_witnesses),
        missing_envelope_defects=list(envelope.remaining_defects),
        source_matrix_forces_faithfulness=source_matrix_forces_faithfulness(envelope_witnesses),
    )


def k3e_bridge_audit_report(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EBridgeAuditReport:
    """Return the combined bridge audit report for K3 x E."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    witness = finite_bridge_witness(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
    )
    obstruction = bridge_obstruction_record(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    matrix = bridge_proof_obligation_matrix(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    source = source_recognition_record(closure_witnesses=closure_witnesses)
    source_core_closed = (
        source.gate.closed
        and source.envelope.completed_unquotiented_recognized
    )
    open_source_layers = []
    if not source.boundary_report.compact_double_report.closed:
        open_source_layers.append("compact/double source gates")
    if not source.boundary_report.pro_recognition_report.closed:
        open_source_layers.append("pro-recognition source gates")
    open_source_phrase = (
        " and ".join(open_source_layers) + " remain open"
        if open_source_layers
        else "source auxiliary gates remain open"
    )
    if source.boundary_report.closed and matrix.all_entries_proved:
        summary = (
            "low-height scattering/bar/Rademacher data and finite BRST/Yangian boundary packets are witnessed; "
            "Hall-Borcherds source recognition and the five comparison maps are closed from supplied witnesses"
        )
    elif source.boundary_report.closed:
        summary = (
            "low-height scattering/bar/Rademacher data and finite BRST/Yangian boundary packets are witnessed; "
            "Hall-Borcherds source recognition is closed from supplied witnesses; "
            "the remaining comparison maps still require theorem-level constructions"
        )
    elif source_core_closed and matrix.all_entries_proved:
        summary = (
            "low-height scattering/bar/Rademacher data and finite BRST/Yangian boundary packets are witnessed; "
            "the Hall-Borcherds gate, recognition envelope, and five comparison maps are closed from supplied witnesses; "
            f"{open_source_phrase}"
        )
    elif source_core_closed:
        summary = (
            "low-height scattering/bar/Rademacher data and finite BRST/Yangian boundary packets are witnessed; "
            "the Hall-Borcherds gate and recognition envelope are closed from supplied witnesses; "
            f"{open_source_phrase}; "
            "the remaining comparison maps still require theorem-level constructions"
        )
    elif matrix.all_entries_proved:
        summary = (
            "low-height scattering/bar/Rademacher data and finite BRST/Yangian boundary packets are witnessed; "
            "Hall-Borcherds source recognition is open; "
            "the five comparison maps are closed from supplied witnesses"
        )
    else:
        summary = (
            "low-height scattering/bar/Rademacher data and finite BRST/Yangian boundary packets are witnessed; "
            "Hall-Borcherds source recognition is open; "
            "the five comparison maps still require theorem-level constructions"
        )
    return K3EBridgeAuditReport(
        finite_witness=witness,
        obstruction_record=obstruction,
        proof_matrix=matrix,
        source_recognition=source,
        summary=summary,
    )


def k3e_core_gap_report(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3ECoreGapReport:
    """Return the top-level seven-part missing-mathematics report."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    audit = k3e_bridge_audit_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    status = k3e_gap_status_table(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    task_map = k3e_proof_task_map(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    evidence_entries = [
        K3EGapEvidenceEntryEntry(
            gap="framed_d3_assignment",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Theorem~\\ref{thm:cy-to-chiral-d3}",
                "Remark~\\ref{rem:k3e-core-proof-gaps}",
            ],
            tests=[
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
        ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="compact_hall_promotion",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Theorem~\\ref{thm:k3e-positive-half-hall-borcherds-criterion}",
                "Corollary~\\ref{cor:k3e-finite-height-promotion-obstruction}",
                "Theorem~\\ref{thm:k3e-constructed-finite-double-recognition}",
            ],
            tests=[
                "compute/tests/test_hall_borcherds_gate.py",
            ],
        ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="scattering_root_identification",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Conjecture~\\ref{conj:k3e-scattering-bkm}",
                "Remark~\\ref{rem:k3e-scattering-missing-inputs}",
            ],
            tests=[
                "compute/tests/test_k3e_finite_bridge_witness.py",
                "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
            ],
        ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="bkm_bar_dictionary",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Conjecture~\\ref{conj:bkm-bar-dictionary}",
                "Remark~\\ref{rem:bkm-bar-missing-inputs}",
            ],
            tests=[
                "compute/tests/test_k3e_finite_bridge_witness.py",
                "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
                "compute/tests/test_bkm_chiral_algebra.py",
            ],
        ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="shadow_rademacher_comparison",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Conjecture~\\ref{conj:k3e-shadow-rademacher}",
                "Remark~\\ref{rem:k3e-shadow-rademacher-missing}",
            ],
            tests=[
                "compute/tests/test_k3e_finite_bridge_witness.py",
                "compute/tests/test_phi01_shadow_decomposition.py",
                "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
            ],
        ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="brst_realization",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Equation~\\eqref{eq:bkm-brst}",
                "Remark~\\ref{rem:k3e-brst-missing}",
            ],
            tests=[
                "compute/tests/test_bkm_chiral_algebra.py",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
        ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="vertex_operator_yangian",
            evidence=K3EGapEvidenceEntry(
            chapter=[
                "Conjecture~\\ref{conj:vertex-op-yangian}",
                "Remark~\\ref{rem:k3e-vertex-op-yangian-missing}",
            ],
            tests=[
                "compute/tests/test_bkm_chiral_algebra.py",
                "compute/tests/test_borcherds_vertex_yangian.py",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
        ),
        ),
    ]
    evidence_by_gap = {entry.gap: entry.evidence for entry in evidence_entries}
    core_gap_names = [
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    ]
    entries = [
        K3ECoreGapEntry(
            gap=gap_name,
            evidence=evidence_by_gap[gap_name],
            status=status.rows[gap_name],
            missing=list(status.rows[gap_name].missing),
            tasks=list(task_map.tasks[gap_name].tasks),
        )
        for gap_name in core_gap_names
    ]
    if all(entry.status.proved for entry in entries):
        summary = (
            "the supplied closure witness package closes every core comparison gap; "
            "the report keeps the evidence, status, and task entries as theorem data"
        )
    elif any(entry.status.proved for entry in entries):
        summary = (
            "the report records the supplied closure witnesses for the proved core gaps "
            "and keeps the remaining gaps explicit with evidence, status, and tasks"
        )
    else:
        summary = (
            "the manuscript still lacks the source-side compact Hall construction, "
            "the five finite comparison maps, and the uniform inverse-limit theorem; "
            "the seven core gaps are now isolated explicitly with evidence, status, and tasks"
        )
    return K3ECoreGapReport(audit=audit, entries=entries, summary=summary)


def k3e_proof_dependency_graph(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
) -> K3EProofDependencyGraph:
    """Return the ordered dependency graph for the remaining mathematics."""
    gap_report = k3e_core_gap_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
    )
    nodes = [
        "source_hall_borcherds_gate",
        "source_recognition_envelope",
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    ]
    entries = [
        K3EProofDependencyEntry(
            node="source_recognition_envelope",
            prerequisites=["source_hall_borcherds_gate"],
        ),
        K3EProofDependencyEntry(
            node="framed_d3_assignment",
            prerequisites=["source_hall_borcherds_gate"],
        ),
        K3EProofDependencyEntry(
            node="compact_hall_promotion",
            prerequisites=["source_recognition_envelope", "framed_d3_assignment"],
        ),
        K3EProofDependencyEntry(
            node="scattering_root_identification",
            prerequisites=["compact_hall_promotion"],
        ),
        K3EProofDependencyEntry(
            node="bkm_bar_dictionary",
            prerequisites=["framed_d3_assignment", "compact_hall_promotion", "scattering_root_identification"],
        ),
        K3EProofDependencyEntry(
            node="shadow_rademacher_comparison",
            prerequisites=["bkm_bar_dictionary", "scattering_root_identification"],
        ),
        K3EProofDependencyEntry(
            node="brst_realization",
            prerequisites=["framed_d3_assignment", "compact_hall_promotion"],
        ),
        K3EProofDependencyEntry(
            node="vertex_operator_yangian",
            prerequisites=["brst_realization", "shadow_rademacher_comparison"],
        ),
    ]
    edges = [
        ("source_hall_borcherds_gate", "source_recognition_envelope"),
        ("source_hall_borcherds_gate", "framed_d3_assignment"),
        ("source_recognition_envelope", "compact_hall_promotion"),
        ("framed_d3_assignment", "compact_hall_promotion"),
        ("compact_hall_promotion", "scattering_root_identification"),
        ("framed_d3_assignment", "bkm_bar_dictionary"),
        ("compact_hall_promotion", "bkm_bar_dictionary"),
        ("scattering_root_identification", "bkm_bar_dictionary"),
        ("bkm_bar_dictionary", "shadow_rademacher_comparison"),
        ("scattering_root_identification", "shadow_rademacher_comparison"),
        ("framed_d3_assignment", "brst_realization"),
        ("compact_hall_promotion", "brst_realization"),
        ("brst_realization", "vertex_operator_yangian"),
        ("shadow_rademacher_comparison", "vertex_operator_yangian"),
    ]
    topological_order = [
        "source_hall_borcherds_gate",
        "source_recognition_envelope",
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    ]
    summary = (
        "source recognition feeds compact Hall promotion; compact Hall promotion "
        "feeds scattering and the bar dictionary; the bar dictionary feeds the "
        "shadow comparison; BRST and Yangian sit after the framed source and "
        "the compact Hall data"
    )
    return K3EProofDependencyGraph(
        nodes=nodes,
        edges=edges,
        entries=entries,
        topological_order=topological_order,
        summary=summary,
    )


def k3e_closure_criterion_report(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EClosureCriterionReport:
    """Return the exact closure criterion for the remaining bridge theorem."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    audit = k3e_bridge_audit_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    graph = k3e_proof_dependency_graph(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
    )
    required_conditions = [
        "close the source-side Hall/Borcherds gate",
        "complete the source recognition envelope",
        "construct the source Hall/Borcherds compact-double bridge",
        "construct the framed d=3 assignment",
        "construct the compact Hall promotion",
        "construct the scattering/root identification",
        "construct the BKM-bar dictionary",
        "construct the shadow/Rademacher comparison",
        "construct the BRST realization",
        "construct the vertex-operator Yangian",
        "prove all heightwise compatibility maps, rank-zero squares, and source/target/kernel/image/cokernel Mittag-Leffler exactness gates",
        "prove the Q_H^sep/L_H^ex/H_H^HB pro-recognition gates: separated completion, exact defect-ideal inverse limit, and Heegner/Borcherds coefficient comparison",
    ]
    inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "closure_criterion",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    pro_recognition_gate = k3e_pro_recognition_gate_requirement(
        "closure_criterion",
        proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
    )
    witnessed_bridges = closure_witnesses.bridge_construction_set
    construction_requirements = k3e_bridge_construction_requirements_from_witnesses(
        closure_witnesses
    )
    condition_by_bridge = {
        "source_hall_borcherds_gate": "construct the source Hall/Borcherds compact-double bridge",
        "framed_d3_assignment": "construct the framed d=3 assignment",
        "compact_hall_promotion": "construct the compact Hall promotion",
        "scattering_root_identification": "construct the scattering/root identification",
        "bkm_bar_dictionary": "construct the BKM-bar dictionary",
        "shadow_rademacher_comparison": "construct the shadow/Rademacher comparison",
        "brst_realization": "construct the BRST realization",
        "vertex_operator_yangian": "construct the vertex-operator Yangian",
    }
    proved_conditions = set()
    if closure_witnesses.source_gate_closed:
        proved_conditions.add("close the source-side Hall/Borcherds gate")
    if closure_witnesses.source_recognition_envelope_completed:
        proved_conditions.add("complete the source recognition envelope")
    for bridge, condition in condition_by_bridge.items():
        if bridge in witnessed_bridges:
            proved_conditions.add(condition)
    if inverse_limit_gate.all_proved:
        proved_conditions.add(
            "prove all heightwise compatibility maps, rank-zero squares, and source/target/kernel/image/cokernel Mittag-Leffler exactness gates"
        )
    if pro_recognition_gate.all_proved:
        proved_conditions.add(
            "prove the Q_H^sep/L_H^ex/H_H^HB pro-recognition gates: separated completion, exact defect-ideal inverse limit, and Heegner/Borcherds coefficient comparison"
        )
    required_conditions = [
        condition for condition in required_conditions if condition not in proved_conditions
    ]
    closed = (
        not required_conditions
        and closure_witnesses.source_gate_closed
        and closure_witnesses.source_recognition_envelope_completed
        and closure_witnesses.all_bridge_constructions_closed
        and inverse_limit_gate.all_proved
        and pro_recognition_gate.all_proved
    )
    summary = (
        "closure requires the source gate, the compact Hall promotion, the five "
        "comparison constructions, the inverse-limit compatibility and exactness theorem, "
        "and the separate Q_H^sep/L_H^ex/H_H^HB pro-recognition gates; "
        + (
            "the supplied witness package closes every condition"
            if closed
            else "the remaining conditions are the unwitnessed part of that package"
        )
    )
    return K3EClosureCriterionReport(
        audit=audit,
        dependency_graph=graph,
        required_conditions=required_conditions,
        inverse_limit_gate=inverse_limit_gate,
        pro_recognition_gate=pro_recognition_gate,
        construction_requirements=construction_requirements,
        closed=closed,
        summary=summary,
    )


def k3e_gap_crosswalk_report(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EGapCrosswalkReport:
    """Return the evidence crosswalk for each core gap."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    core = k3e_core_gap_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    evidence_entries = [
        K3EGapEvidenceEntryEntry(
            gap="framed_d3_assignment",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Theorem~\\ref{thm:cy-to-chiral-d3}",
                    "Remark~\\ref{rem:k3e-core-proof-gaps}",
                ],
                tests=[
                    "compute/tests/test_k3e_finite_bridge_witness.py",
                ],
            ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="compact_hall_promotion",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Theorem~\\ref{thm:k3e-positive-half-hall-borcherds-criterion}",
                    "Corollary~\\ref{cor:k3e-finite-height-promotion-obstruction}",
                    "Theorem~\\ref{thm:k3e-constructed-finite-double-recognition}",
                ],
                tests=[
                    "compute/tests/test_hall_borcherds_gate.py",
                ],
            ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="scattering_root_identification",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Conjecture~\\ref{conj:k3e-scattering-bkm}",
                    "Remark~\\ref{rem:k3e-scattering-missing-inputs}",
                ],
                tests=[
                    "compute/tests/test_k3e_finite_bridge_witness.py",
                    "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
                ],
            ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="bkm_bar_dictionary",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Conjecture~\\ref{conj:bkm-bar-dictionary}",
                    "Remark~\\ref{rem:bkm-bar-missing-inputs}",
                ],
                tests=[
                    "compute/tests/test_k3e_finite_bridge_witness.py",
                    "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
                    "compute/tests/test_bkm_chiral_algebra.py",
                ],
            ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="shadow_rademacher_comparison",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Conjecture~\\ref{conj:k3e-shadow-rademacher}",
                    "Remark~\\ref{rem:k3e-shadow-rademacher-missing}",
                ],
                tests=[
                    "compute/tests/test_k3e_finite_bridge_witness.py",
                    "compute/tests/test_phi01_shadow_decomposition.py",
                    "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
                ],
            ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="brst_realization",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Equation~\\eqref{eq:bkm-brst}",
                    "Remark~\\ref{rem:k3e-brst-missing}",
                ],
                tests=[
                    "compute/tests/test_bkm_chiral_algebra.py",
                    "compute/tests/test_k3e_finite_bridge_witness.py",
                ],
            ),
        ),
        K3EGapEvidenceEntryEntry(
            gap="vertex_operator_yangian",
            evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Conjecture~\\ref{conj:vertex-op-yangian}",
                    "Remark~\\ref{rem:k3e-vertex-op-yangian-missing}",
                ],
                tests=[
                    "compute/tests/test_bkm_chiral_algebra.py",
                    "compute/tests/test_borcherds_vertex_yangian.py",
                    "compute/tests/test_k3e_finite_bridge_witness.py",
                ],
            ),
        ),
    ]
    if all(entry.status.proved for entry in core.entries):
        summary = (
            "each core gap has explicit chapter labels and executable witnesses; "
            "the supplied closure witness package makes the crosswalk a record of "
            "proved theorem data"
        )
    else:
        summary = (
            "each core gap has explicit chapter labels and executable witnesses; "
            "the crosswalk shows where the current evidence stops and the missing "
            "theorems begin"
        )
    return K3EGapCrosswalkReport(
        core_gap_report=core,
        entries=evidence_entries,
        summary=summary,
    )


def k3e_gap_status_table(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EGapStatusTable:
    """Return a theorem-boundary status table for each core gap."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    entries = [
        K3EGapStatusEntry(
            gap="framed_d3_assignment",
            row=K3EGapStatusRow(
            established_boundary=[
                "Theorem~\\ref{thm:cy-to-chiral-d3} states the conditional assignment",
            ],
            finite_boundary_results=[
                "finite target packets are recorded as supplied data in Definition~\\ref{def:k3e-bridge-datum}",
            ],
            witnessed=[
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
            formal=[
                "candidate finite-height maps in Remark~\\ref{rem:k3e-formal-candidate-finite-maps}",
            ],
            missing=[
                "construct a genuine stage-1 factorisation algebra on K3 x E",
                "prove the fixed (Sigma_2, C) specialisation agrees with the framed chiral algebra",
                "prove compatibility with the H1-H4 locus and inverse limits",
            ],
        ),
        ),
        K3EGapStatusEntry(
            gap="compact_hall_promotion",
            row=K3EGapStatusRow(
            established_boundary=[
                "Theorem~\\ref{thm:k3e-positive-half-hall-borcherds-criterion}",
                "Theorem~\\ref{thm:k3e-constructed-finite-double-recognition}",
                "Corollary~\\ref{cor:k3e-finite-height-promotion-obstruction}",
            ],
            finite_boundary_results=[
                "Theorem~\\ref{thm:k3e-canonical-finite-source-packets}",
                "Theorem~\\ref{thm:k3e-canonical-finite-target-packets}",
                "Theorem~\\ref{thm:k3e-finite-comparison-matrix-packets}",
                "Theorem~\\ref{thm:k3e-finite-comparison-shape-criterion}",
                "Theorem~\\ref{thm:k3e-finite-recognition-certificate}",
                "Theorem~\\ref{thm:k3e-finite-recognition-envelope}",
            ],
            witnessed=[
                "compute/tests/test_hall_borcherds_gate.py",
            ],
            formal=[
                "source recognition gate and envelope records",
            ],
            missing=[
                "build the oriented critical CoHA with negative half, Cartan, Hopf pairing, coproduct, and finite-height truncations",
                "prove nondegeneracy modulo the Borcherds Cartan radical",
                "identify the Serre kernel and the pro-cone topology compatibility",
            ],
        ),
        ),
        K3EGapStatusEntry(
            gap="scattering_root_identification",
            row=K3EGapStatusRow(
            established_boundary=[
                "Conjecture~\\ref{conj:k3e-scattering-bkm} is stated as an explicit conjecture, not a theorem",
            ],
            finite_boundary_results=[
                "Proposition~\\ref{prop:k3e-finite-scattering-quantum-torus-gate}",
                "finite_scattering_quantum_torus_gate",
                "Theorem~\\ref{thm:k3e-finite-scattering-root-comparison}",
                "finite_scattering_root_report",
            ],
            witnessed=[
                "compute/tests/test_k3e_finite_bridge_witness.py",
                "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
            ],
            formal=[
                "candidate scattering map in the finite bridge witness module",
            ],
            missing=[
                "construct the motivic integration map from wall-crossing Hall data to the quantum torus",
                "prove wall products coincide with the Borcherds denominator walls",
                "exclude extraneous walls and missing imaginary-root orbits",
            ],
        ),
        ),
        K3EGapStatusEntry(
            gap="bkm_bar_dictionary",
            row=K3EGapStatusRow(
            established_boundary=[
                "Conjecture~\\ref{conj:bkm-bar-dictionary} is explicit and conditional",
            ],
            finite_boundary_results=[
                "Proposition~\\ref{prop:k3e-finite-bar-lattice-grading-gate}",
                "finite_bar_lattice_grading_report",
                "Proposition~\\ref{prop:k3e-finite-bar-ce-chain-map-gate}",
                "finite_bar_ce_chain_map_gate",
                "Theorem~\\ref{thm:k3e-finite-bar-ce-comparison}",
                "finite_bar_ce_report",
                "Proposition~\\ref{prop:k3e-finite-bar-regularization-gate}",
                "finite_bar_regularization_report",
            ],
            witnessed=[
                "compute/tests/test_bkm_chiral_algebra.py",
                "compute/tests/test_k3_elliptic_genus_bkm_bar.py",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
            formal=[
                "bar candidate and proof obligations in the witness module",
            ],
            missing=[
                "prove the bar complex is Lambda^{2,1}_{II}-graded",
                "identify the alpha-primary Euler characteristic with the motivic DT index",
                "match the regularization vector with the Weyl vector and Borcherds normalization",
            ],
        ),
        ),
        K3EGapStatusEntry(
            gap="shadow_rademacher_comparison",
            row=K3EGapStatusRow(
            established_boundary=[
                "Conjecture~\\ref{conj:k3e-shadow-rademacher} is conditional",
            ],
            finite_boundary_results=[
                "Proposition~\\ref{prop:k3e-rademacher-polar-bessel-gate}",
                "rademacher_polar_bessel_gate",
                "Proposition~\\ref{prop:k3e-rademacher-truncation-error-gate}",
                "rademacher_truncation_error_gate",
                "Corollary~\\ref{cor:k3e-rank-one-rademacher-arity-certificate}",
                "rademacher_finite_height_certificate",
            ],
            witnessed=[
                "rank-one finite-height Rademacher certificate",
                "compute/tests/test_phi01_shadow_decomposition.py",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
            formal=[
                "compact-CY3 shadow/Rademacher comparison schema in the witness module",
            ],
            missing=[
                "construct the protected compact-CY3 comparison map",
                "extend polar-data compatibility and Bessel recursion from the rank-one lane to the compact shadow packet",
                "prove a uniform all-height truncation error theorem beyond the rank-one certificate",
            ],
        ),
        ),
        K3EGapStatusEntry(
            gap="brst_realization",
            row=K3EGapStatusRow(
            established_boundary=[
                "Theorem~\\ref{thm:k3e-frenkel-kac-closure} is conditional on the supplied BRST package",
                "Remark~\\ref{rem:k3e-brst-conditional-status} prevents unconditional promotion",
            ],
            finite_boundary_results=[
                "Proposition~\\ref{prop:k3e-brst-central-charge-gate}",
                "brst_central_charge_gate",
                "Proposition~\\ref{prop:k3e-brst-finite-supertrace-fixture}",
                "brst_coefficient_fixture",
                "brst_coefficient_fixture_transition",
                "Proposition~\\ref{prop:k3e-brst-no-ghost-spectral-sequence-gate}",
                "brst_no_ghost_spectral_sequence_gate",
                "Proposition~\\ref{prop:k3e-brst-borcherds-bracket-gate}",
                "brst_borcherds_bracket_gate",
                "Proposition~\\ref{prop:k3e-brst-borcherds-serre-relation-gate}",
                "brst_borcherds_serre_relation_gate",
                "Proposition~\\ref{prop:k3e-brst-momentum-height-projection-gate}",
                "brst_momentum_height_projection_gate",
            ],
            witnessed=[
                "compute/tests/test_bkm_chiral_algebra.py",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
            formal=[
                "Equation~\\eqref{eq:bkm-brst} is a formal template until the worldsheet VOA and BRST differential are supplied",
            ],
            missing=[
                "construct the worldsheet VOA and BRST differential",
                "prove the cohomology produces the stated root multiplicities",
                "realize the finite supertrace fixture in the worldsheet VOA and fix ghost-number grading",
            ],
        ),
        ),
        K3EGapStatusEntry(
            gap="vertex_operator_yangian",
            row=K3EGapStatusRow(
            established_boundary=[
                "Conjecture~\\ref{conj:vertex-op-yangian} is an explicit conjecture",
                "Remark~\\ref{rem:k3e-yangian-current-missing} isolates the operator-level proof obligations",
            ],
            finite_boundary_results=[
                "Proposition~\\ref{prop:k3e-finite-yangian-current-candidate-packet}",
                "Proposition~\\ref{prop:k3e-finite-spectral-kernel-label-packet}",
                "Proposition~\\ref{prop:k3e-finite-self-ope-pole-layer-packet}",
                "Proposition~\\ref{prop:k3e-finite-yangian-label-tower}",
                "Proposition~\\ref{prop:k3e-finite-residue-transition}",
                "Proposition~\\ref{prop:k3e-finite-brst-residue-chain-gate}",
                "yangian_brst_residue_chain_gate",
                "Proposition~\\ref{prop:k3e-finite-ope-coefficient-transition}",
                "Proposition~\\ref{prop:k3e-finite-yangian-ope-serre-ideal-span-gate}",
                "yangian_ope_serre_ideal_span_gate",
                "Proposition~\\ref{prop:k3e-finite-yangian-pbw-associated-graded-gate}",
                "yangian_pbw_associated_graded_gate",
                "Proposition~\\ref{prop:k3e-finite-spectral-associator-obstruction}",
                "Proposition~\\ref{prop:k3e-finite-spectral-r-matrix-equation-gate}",
                "yangian_spectral_r_matrix_equation_gate",
                "Proposition~\\ref{prop:k3e-finite-spectral-associator-transition}",
            ],
            witnessed=[
                "compute/tests/test_bkm_chiral_algebra.py",
                "compute/tests/test_borcherds_vertex_yangian.py",
                "compute/tests/test_k3e_finite_bridge_witness.py",
            ],
            formal=[
                "Yangian witness record and current templates",
            ],
            missing=[
                "prove the Omega-deformed vertex operators exist to all orders at epsilon = 1",
                "show the residues are genuine BRST cohomology operators",
                "prove the OPE/Serre/Hall-Borcherds compatibility",
            ],
        ),
        ),
    ]
    witnessed_bridges = closure_witnesses.bridge_construction_set
    updated_entries = []
    for entry in entries:
        if entry.gap in witnessed_bridges:
            inverse_limit_gate = k3e_inverse_limit_gate_requirement(
                entry.gap,
                proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
            )
            row_proved = inverse_limit_gate.all_proved
            updated_entries.append(K3EGapStatusEntry(
                gap=entry.gap,
                row=replace(
                    entry.row,
                    witnessed=list(entry.row.witnessed)
                    + ["supplied closure witness proves the bridge construction"],
                    formal=[],
                    missing=list(inverse_limit_gate.open_conditions),
                    status="proved" if row_proved else "open",
                ),
            ))
        else:
            updated_entries.append(entry)
    entries = updated_entries
    if all(entry.row.proved for entry in entries):
        summary = (
            "each core gap has a five-way status split: established boundary, finite boundary result, "
            "witnessed, formal, missing; the supplied closure witness package marks every core gap proved"
        )
    elif any(entry.row.proved for entry in entries):
        summary = (
            "each core gap has a five-way status split: established boundary, finite boundary result, "
            "witnessed, formal, missing; supplied closure witnesses mark exactly the proved bridge rows"
        )
    elif witnessed_bridges:
        summary = (
            "each core gap has a five-way status split: established boundary, finite boundary result, "
            "witnessed, formal, missing; supplied bridge-construction witnesses clear construction rows "
            "but inverse-limit obligations keep the affected rows open"
        )
    else:
        summary = (
            "each core gap has a five-way status split: established boundary, finite boundary result, "
            "witnessed, formal, missing; the table makes the remaining theorem boundary explicit "
            "without marking the gap proved"
        )
    return K3EGapStatusTable(entries=entries, summary=summary)


def k3e_proof_roadmap_report(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EProofRoadmapReport:
    """Return a proof roadmap with evidence, missing theorems, and methods."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    audit = k3e_bridge_audit_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    status_table = k3e_gap_status_table(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    crosswalk = k3e_gap_crosswalk_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    boundary = k3e_theorem_boundary_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    task_map = k3e_proof_task_map(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "proof_roadmap",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    pro_recognition_gate = k3e_pro_recognition_gate_requirement(
        "proof_roadmap",
        proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
    )
    source_inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "source_hall_borcherds_gate",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    source_record = source_recognition_record(closure_witnesses=closure_witnesses)
    source_pro_recognition_gate = k3e_pro_recognition_gate_requirement(
        "source_hall_borcherds_gate",
        proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
    )
    source_missing = list(
        dict.fromkeys(
            list(boundary.source_conditions)
            + list(source_record.boundary_report.required_conditions)
            + list(source_pro_recognition_gate.open_conditions)
            + list(source_inverse_limit_gate.open_conditions)
        )
    )
    source_finite_layers_closed = (
        source_record.gate.closed
        and source_record.envelope.completed_unquotiented_recognized
        and source_record.boundary_report.compact_double_report.closed
    )
    source_base_method = [
        "construct the oriented critical CoHA with the negative half, Cartan, Hopf pairing, and coproduct",
        "prove defect-vanishing at each finite height and source-recognition completeness",
        "show compatibility with the Hall double and the pro-cone topology",
    ]
    source_task_method = (
        list(task_map.tasks["source_hall_borcherds_gate"].tasks)
        if source_finite_layers_closed
        else source_base_method
    )
    source_step_proved = (
        source_record.boundary_report.closed and source_inverse_limit_gate.all_proved
    )
    steps = [
        K3EProofRoadmapStep(
            name="source_hall_borcherds_gate",
            status="proved" if source_step_proved else "open",
            current_evidence=K3EGapEvidenceEntry(
                chapter=[
                    "Theorem~\\ref{thm:k3e-positive-half-hall-borcherds-criterion}",
                    "Theorem~\\ref{thm:k3e-constructed-finite-double-recognition}",
                ],
                tests=[
                    "compute/tests/test_hall_borcherds_gate.py",
            ],
            ),
            missing=(
                []
                if source_step_proved
                else source_missing
            ),
            proof_method=[] if source_step_proved else source_task_method,
            inverse_limit_gate=source_inverse_limit_gate,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "source_hall_borcherds_gate",
                closure_witnesses,
            ),
        ),
    ]
    for gap_name in [
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    ]:
        step_inverse_limit_gate = k3e_inverse_limit_gate_requirement(
            gap_name,
            proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
        )
        step_proved = (
            gap_name in closure_witnesses.bridge_construction_set
            and step_inverse_limit_gate.all_proved
        )
        construction_supplied = gap_name in closure_witnesses.bridge_construction_set
        missing = [] if step_proved else list(step_inverse_limit_gate.open_conditions)
        if not construction_supplied:
            missing = list(status_table.rows[gap_name].missing) + missing
        steps.append(
            K3EProofRoadmapStep(
                name=gap_name,
                status="proved" if step_proved else "open",
                current_evidence=crosswalk.evidence_by_gap[gap_name],
                missing=missing,
                proof_method=[] if step_proved else list(task_map.tasks[gap_name].tasks),
                inverse_limit_gate=step_inverse_limit_gate,
                construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                    gap_name,
                    closure_witnesses,
                ),
            )
        )
    summary = (
        "the roadmap pairs the source gate and each labeled BD bridge with the current witness data, "
        "the explicit missing theorem statements, the bridge-specific heightwise transition maps, "
        "and the source/target/kernel/image/cokernel exactness gates"
    )
    return K3EProofRoadmapReport(
        audit=audit,
        status_table=status_table,
        steps=steps,
        task_map=task_map,
        inverse_limit_gate=inverse_limit_gate,
        pro_recognition_gate=pro_recognition_gate,
        construction_requirements=k3e_bridge_construction_requirements_from_witnesses(
            closure_witnesses
        ),
        summary=summary,
    )


def k3e_proof_task_map(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EProofTaskMap:
    """Return the missing technical ingredients bridge by bridge."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    _ = k3e_bridge_audit_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    source_record = source_recognition_record(closure_witnesses=closure_witnesses)

    def task_entry(bridge: str, tasks: List[str]) -> K3EProofTaskEntry:
        witnessed = bridge in closure_witnesses.bridge_construction_set
        inverse_limit_gate = k3e_inverse_limit_gate_requirement(
            bridge,
            proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
        )
        remaining_tasks = [] if witnessed else list(tasks)
        remaining_tasks.extend(inverse_limit_gate.open_conditions)
        return K3EProofTaskEntry(
            bridge=bridge,
            tasks=remaining_tasks,
            inverse_limit_gate=inverse_limit_gate,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                bridge,
                closure_witnesses,
            ),
        )

    def source_task_entry(tasks: List[str]) -> K3EProofTaskEntry:
        bridge = "source_hall_borcherds_gate"
        inverse_limit_gate = k3e_inverse_limit_gate_requirement(
            bridge,
            proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
        )
        pro_recognition_gate = k3e_pro_recognition_gate_requirement(
            bridge,
            proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
        )
        remaining_tasks: List[str] = []
        source_boundary_closed = source_record.boundary_report.closed
        source_finite_layers_closed = (
            source_record.gate.closed
            and source_record.envelope.completed_unquotiented_recognized
            and source_record.boundary_report.compact_double_report.closed
        )
        if not source_boundary_closed:
            if not source_finite_layers_closed:
                remaining_tasks.extend(tasks)
            remaining_tasks.extend(source_record.boundary_report.required_conditions)
            remaining_tasks.extend(pro_recognition_gate.open_conditions)
        remaining_tasks.extend(inverse_limit_gate.open_conditions)
        remaining_tasks = list(dict.fromkeys(remaining_tasks))
        return K3EProofTaskEntry(
            bridge=bridge,
            tasks=remaining_tasks,
            inverse_limit_gate=inverse_limit_gate,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                bridge,
                closure_witnesses,
            ),
        )

    entries = [
        source_task_entry(
            tasks=[
                "construct the oriented critical CoHA with the negative half, Cartan, Hopf pairing, and coproduct",
                "prove defect-vanishing at each finite height and source-recognition completeness",
                "show compatibility with the Hall double and the pro-cone topology",
            ],
        ),
        task_entry(
            bridge="framed_d3_assignment",
            tasks=[
                "construct a genuine stage-1 factorisation algebra on K3 x E",
                "prove the fixed (Sigma_2, C) specialisation under H1-H4",
                "identify the framed chiral output and verify inverse-limit exactness",
            ],
        ),
        task_entry(
            bridge="compact_hall_promotion",
            tasks=[
                "complete the source Hall data to the compact Hall object",
                "prove nondegeneracy modulo the Borcherds Cartan radical and identify the Serre kernel",
                "show compatibility with the finite-double recognition and pro-cone topology",
            ],
        ),
        task_entry(
            bridge="scattering_root_identification",
            tasks=[
                "construct the motivic integration morphism to the quantum torus",
                "prove the wall-product and Borcherds denominator correspondence",
                "exclude extraneous walls, preserve imaginary-root orbits, and commute with height truncation",
            ],
        ),
        task_entry(
            bridge="bkm_bar_dictionary",
            tasks=[
                "prove the Lambda^{2,1}_{II} grading of the bar complex",
                "identify the alpha-primary Euler characteristic with the motivic DT index",
                "match the Weyl vector and the Borcherds multiplier-system normalization",
            ],
        ),
        task_entry(
            bridge="shadow_rademacher_comparison",
            tasks=[
                "construct the protected compact-CY3 shadow-to-partition comparison map",
                "extend the Bessel recursion and polar-data preservation from the rank-one lane to the compact shadow packet",
                "establish a uniform all-height truncation-error theorem",
            ],
        ),
        task_entry(
            bridge="brst_realization",
            tasks=[
                "construct the worldsheet VOA and BRST differential",
                "realize the finite supertrace fixture in BRST cohomology with the correct ghost-number grading",
                "prove the cohomology root multiplicities, heightwise functoriality, and source/target/kernel/image/cokernel exactness",
            ],
        ),
        task_entry(
            bridge="vertex_operator_yangian",
            tasks=[
                "construct the Omega-deformed vertex operators to all orders at epsilon = 1",
                "show the residues are BRST cohomology classes and commute with truncation",
                "prove the OPE/Serre/Hall-Borcherds compatibility and R-matrix match",
            ],
        ),
    ]
    summary = (
        "the task map breaks each open bridge into the precise constructions, compatibilities, "
        "and normalization checks still missing from the theorem package"
    )
    return K3EProofTaskMap(
        entries=entries,
        inverse_limit_gate=k3e_inverse_limit_gate_requirement(
            "proof_task_map",
            proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
        ),
        pro_recognition_gate=k3e_pro_recognition_gate_requirement(
            "proof_task_map",
            proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
        ),
        construction_requirements=k3e_bridge_construction_requirements_from_witnesses(
            closure_witnesses
        ),
        summary=summary,
    )


def k3e_bridge_specification(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EBridgeSpecification:
    """Return a theorem-specification object for each open bridge."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    boundary = k3e_theorem_boundary_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    task_map = k3e_proof_task_map(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    source_record = source_recognition_record(closure_witnesses=closure_witnesses)
    dependency_graph = k3e_proof_dependency_graph(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
    )
    inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "bridge_specification",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    pro_recognition_gate = k3e_pro_recognition_gate_requirement(
        "bridge_specification",
        proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
    )
    source_inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "source_hall_borcherds_gate",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    source_local_obligations_satisfied = (
        source_record.gate.closed
        and source_record.envelope.completed_unquotiented_recognized
        and source_record.boundary_report.compact_double_report.closed
        and source_inverse_limit_gate.all_proved
    )

    def schema_status(bridge: str) -> str:
        inverse_limit_proved = k3e_inverse_limit_gate_requirement(
            bridge,
            proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
        ).all_proved
        if bridge == "source_hall_borcherds_gate":
            proved = source_record.boundary_report.closed and inverse_limit_proved
        else:
            proved = (
                bridge in closure_witnesses.bridge_construction_set
                and inverse_limit_proved
                and dependencies_closed(bridge)
            )
        return "PROVED_THEOREM_SCHEMA" if proved else "OPEN_THEOREM_SCHEMA"

    def dependencies_closed(node: str) -> bool:
        prerequisites = dependency_graph.prerequisites.get(node)
        if prerequisites is None:
            return True
        return all(node_closed(prerequisite) for prerequisite in prerequisites.prerequisites)

    def node_closed(node: str) -> bool:
        if node == "source_hall_borcherds_gate":
            return (
                source_record.boundary_report.closed
                and k3e_inverse_limit_gate_requirement(
                    node,
                    proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
                ).all_proved
            )
        if node == "source_recognition_envelope":
            return (
                closure_witnesses.source_recognition_envelope_completed
                and dependencies_closed(node)
            )
        if node in K3E_CLOSURE_BRIDGES:
            return (
                node in closure_witnesses.bridge_construction_set
                and k3e_inverse_limit_gate_requirement(
                    node,
                    proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
                ).all_proved
                and dependencies_closed(node)
            )
        return False

    def dependency_obligations(bridge: str) -> Tuple[str, ...]:
        prerequisites = dependency_graph.prerequisites.get(bridge)
        if prerequisites is None:
            return ()
        return tuple(
            f"establish dependency theorem: {prerequisite}"
            for prerequisite in prerequisites.prerequisites
            if not node_closed(prerequisite)
        )

    entries = [
        K3EBridgeSpecificationEntry(
            bridge="source_hall_borcherds_gate",
            hypotheses=[
                "source-side Hall/Borcherds gate closed",
                "source recognition envelope completed",
                "finite-height source recognition established",
            ],
            conclusion=[
                "compact Hall source recognition becomes a theorem-level input",
                "finite-double recognition is functorial in height",
            ],
            obstructions=list(
                dict.fromkeys(
                    list(boundary.source_conditions)
                    + list(pro_recognition_gate.open_conditions)
                    + list(inverse_limit_gate.open_conditions)
                )
            ),
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "source_hall_borcherds_gate",
                closure_witnesses,
            ),
            summary="source gate boundary report for Hall/Borcherds recognition",
            status=schema_status("source_hall_borcherds_gate"),
            dependency_obligations=dependency_obligations(
                "source_hall_borcherds_gate"
            ),
            local_obligations_satisfied=source_local_obligations_satisfied,
        ),
        K3EBridgeSpecificationEntry(
            bridge="framed_d3_assignment",
            hypotheses=[
                "stage-1 factorisation algebra on K3 x E constructed",
                "fixed (Sigma_2, C) specialization under H1-H4 available",
                "inverse-limit compatibility maps exist",
            ],
            conclusion=[
                "Phi_3^(Sigma_2,C) is realized as a framed chiral output",
                "the framed output agrees with the chapter object on the H1-H4 locus",
            ],
            obstructions=task_map.tasks["framed_d3_assignment"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "framed_d3_assignment",
                closure_witnesses,
            ),
            summary="BD1 theorem schema for the framed d=3 assignment",
            status=schema_status("framed_d3_assignment"),
            dependency_obligations=dependency_obligations("framed_d3_assignment"),
            local_obligations_satisfied=(
                "framed_d3_assignment" in closure_witnesses.bridge_construction_set
            ),
        ),
        K3EBridgeSpecificationEntry(
            bridge="compact_hall_promotion",
            hypotheses=[
                "oriented critical CoHA exists with negative half, Cartan, pairing, and coproduct",
                "finite-height truncations are defined",
                "source Hall recognition data are compatible with the pro-cone topology",
            ],
            conclusion=[
                "the compact Hall object is defined as a theorem-level completion",
                "Borcherds radical quotient and Serre kernel identification hold",
            ],
            obstructions=task_map.tasks["compact_hall_promotion"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "compact_hall_promotion",
                closure_witnesses,
            ),
            summary="BD2 theorem schema for the compact Hall promotion",
            status=schema_status("compact_hall_promotion"),
            dependency_obligations=dependency_obligations("compact_hall_promotion"),
            local_obligations_satisfied=(
                "compact_hall_promotion" in closure_witnesses.bridge_construction_set
            ),
        ),
        K3EBridgeSpecificationEntry(
            bridge="scattering_root_identification",
            hypotheses=[
                "motivic integration morphism to the quantum torus exists",
                "Hall products are preserved by the finite-height map",
                "rank-zero transition and source/target/kernel/image/cokernel exactness gates are available",
            ],
            conclusion=[
                "wall products equal the Borcherds denominator walls",
                "the root-system identification closes without extraneous walls",
            ],
            obstructions=task_map.tasks["scattering_root_identification"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "scattering_root_identification",
                closure_witnesses,
            ),
            summary="BD3 theorem schema for the scattering/root identification",
            status=schema_status("scattering_root_identification"),
            dependency_obligations=dependency_obligations(
                "scattering_root_identification"
            ),
            local_obligations_satisfied=(
                "scattering_root_identification"
                in closure_witnesses.bridge_construction_set
            ),
        ),
        K3EBridgeSpecificationEntry(
            bridge="bkm_bar_dictionary",
            hypotheses=[
                "the bar complex of the framed algebra is available at finite height",
                "the Lambda^{2,1}_{II} grading is compatible with the specialization",
                "Euler-characteristic comparison is defined on the height filtration",
            ],
            conclusion=[
                "the alpha-primary bar Euler exponent equals the motivic DT index",
                "the Weyl vector and multiplier system match the Borcherds normalization",
            ],
            obstructions=task_map.tasks["bkm_bar_dictionary"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "bkm_bar_dictionary",
                closure_witnesses,
            ),
            summary="BD4 theorem schema for the BKM-bar dictionary",
            status=schema_status("bkm_bar_dictionary"),
            dependency_obligations=dependency_obligations("bkm_bar_dictionary"),
            local_obligations_satisfied=(
                "bkm_bar_dictionary" in closure_witnesses.bridge_construction_set
            ),
        ),
        K3EBridgeSpecificationEntry(
            bridge="shadow_rademacher_comparison",
            hypotheses=[
                "shadow coefficients and polar data are defined at finite height",
                "the truncation map is compatible with the height filtration",
                "the rank-one Rademacher certificate is installed and the compact comparison kernel carries the corresponding Bessel recursion",
            ],
            conclusion=[
                "the compact shadow tower resums to the Rademacher asymptotics at the same truncation level",
                "uniform all-height truncation error bounds exist beyond the rank-one certificate",
            ],
            obstructions=task_map.tasks["shadow_rademacher_comparison"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "shadow_rademacher_comparison",
                closure_witnesses,
            ),
            summary="BD5 theorem schema for the shadow/Rademacher comparison",
            status=schema_status("shadow_rademacher_comparison"),
            dependency_obligations=dependency_obligations(
                "shadow_rademacher_comparison"
            ),
            local_obligations_satisfied=(
                "shadow_rademacher_comparison"
                in closure_witnesses.bridge_construction_set
            ),
        ),
        K3EBridgeSpecificationEntry(
            bridge="brst_realization",
            hypotheses=[
                "worldsheet VOA is constructed at finite height",
                "BRST differential and ghost-number grading are fixed",
                "heightwise functoriality and source/target/kernel/image/cokernel exactness of the complex are established",
            ],
            conclusion=[
                "the BRST cohomology realizes the stated root multiplicities",
                "the finite-height packet commutes with the transition maps",
            ],
            obstructions=task_map.tasks["brst_realization"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "brst_realization",
                closure_witnesses,
            ),
            summary="BD6 theorem schema for the BRST realization",
            status=schema_status("brst_realization"),
            dependency_obligations=dependency_obligations("brst_realization"),
            local_obligations_satisfied=(
                "brst_realization" in closure_witnesses.bridge_construction_set
            ),
        ),
        K3EBridgeSpecificationEntry(
            bridge="vertex_operator_yangian",
            hypotheses=[
                "Omega-deformed vertex operators exist to all orders at epsilon = 1",
                "residue classes are BRST cohomology classes",
                "OPE and Hall-Borcherds pairing are defined at finite height",
            ],
            conclusion=[
                "the vertex-operator current gives the Yangian bridge",
                "the OPE/Serre/Hall-Borcherds compatibility and R-matrix match hold",
            ],
            obstructions=task_map.tasks["vertex_operator_yangian"].tasks,
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                "vertex_operator_yangian",
                closure_witnesses,
            ),
            summary="BD7 theorem schema for the vertex-operator/Yangian bridge",
            status=schema_status("vertex_operator_yangian"),
            dependency_obligations=dependency_obligations("vertex_operator_yangian"),
            local_obligations_satisfied=(
                "vertex_operator_yangian" in closure_witnesses.bridge_construction_set
            ),
        ),
    ]
    summary = (
        "the specification object writes each open bridge as a theorem schema with hypotheses, "
        "conclusion, and obstruction list"
    )
    return K3EBridgeSpecification(entries=entries, summary=summary)


def k3e_bridge_axiom_pack(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3EBridgeAxiomPack:
    """Return the BD-axiom pack obtained from the theorem specification."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    spec = k3e_bridge_specification(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    candidate_transition_maps = {
        "framed_d3_assignment": r"R^{\Phi_3}_{H+1,H,\mathrm{cand}} = \pi_{\Phi_3,\leq H}",
        "compact_hall_promotion": r"R^{\mathrm{Hall}}_{H+1,H,\mathrm{cand}} = \pi_{\mathrm{Hall},\leq H}",
        "scattering_root_identification": r"R^{\mathrm{scatt}}_{H+1,H,\mathrm{cand}} = \pi_{\Gamma,\leq H}",
        "bkm_bar_dictionary": r"R^{\mathrm{bar}}_{H+1,H,\mathrm{cand}} = \pi_{\mathrm{bar},\leq H}",
        "shadow_rademacher_comparison": r"R^{\mathrm{rad}}_{H+1,H,\mathrm{cand}} = \pi_{\mathrm{rad},\leq H}",
        "brst_realization": r"R^{\mathrm{BRST}}_{H+1,H,\mathrm{cand}} = \pi_{\mathrm{BRST},\leq H}",
        "vertex_operator_yangian": r"R^{\mathrm{Yang}}_{H+1,H,\mathrm{cand}} = \pi_{\mathrm{Yang},\leq H}",
    }
    source_gate = K3ESourceGateSpecification(
        hypotheses=list(spec.bridges["source_hall_borcherds_gate"].hypotheses),
        conclusion=list(spec.bridges["source_hall_borcherds_gate"].conclusion),
        obstructions=list(spec.bridges["source_hall_borcherds_gate"].obstructions),
        heightwise_compatibility=K3EHeightwiseCompatibility(
            source_transition_map="T_{H+1,H}^X",
            target_transition_map=r"R^{\mathrm{source}}_{H+1,H,\mathrm{cand}} = \pi_{\mathrm{source},\leq H}",
            transition_conditions=[
                "source-recognition defects vanish uniformly in height",
                "source finite-height gates commute with the transition maps",
            ],
            inverse_limit_conditions=[
                "source gate admits an inverse-limit lift with rank-zero transition squares",
                "source-side recognition satisfies the source/target/kernel/image/cokernel Mittag-Leffler gate",
            ],
            inverse_limit_gate=k3e_inverse_limit_gate_requirement(
                "source_hall_borcherds_gate",
                proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
            ),
            summary=(
                "the source gate records the source-side transition map, the candidate target truncation, "
                "and the inverse-limit exactness obstruction layer"
            ),
        ),
        pro_recognition_gate=k3e_pro_recognition_gate_requirement(
            "source_hall_borcherds_gate",
            proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
        ),
        construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
            "source_hall_borcherds_gate",
            closure_witnesses,
        ),
        summary=(
            "the source-gate boundary report packages the Hall/Borcherds recognition hypotheses, "
            "the finite-height transition compatibility, the inverse-limit exactness obstruction layer, "
            "and the Q_H^sep/L_H^ex/H_H^HB pro-recognition gates"
        ),
        status=spec.bridges["source_hall_borcherds_gate"].status,
        local_obligations_satisfied=(
            spec.bridges["source_hall_borcherds_gate"].local_obligations_satisfied
        ),
    )
    bd_entries = []
    bd_labels = {
        "framed_d3_assignment": "BD1",
        "compact_hall_promotion": "BD2",
        "scattering_root_identification": "BD3",
        "bkm_bar_dictionary": "BD4",
        "shadow_rademacher_comparison": "BD5",
        "brst_realization": "BD6",
        "vertex_operator_yangian": "BD7",
    }
    for name, label in bd_labels.items():
        data = spec.bridges[name]
        bd_entries.append(K3EBridgeAxiomEntry(
            label=label,
            bridge=name,
            hypotheses=list(data.hypotheses),
            conclusion=list(data.conclusion),
            obstructions=list(data.obstructions),
            heightwise_compatibility=K3EHeightwiseCompatibility(
                source_transition_map="T_{H+1,H}^X",
                target_transition_map=candidate_transition_maps[name],
                transition_conditions=[
                    f"{name} commutes with the height transition maps",
                    f"{label} preserves the finite-height filtration",
                ],
                inverse_limit_conditions=[
                    f"{label} admits an inverse-limit lift with rank-zero transition squares",
                    f"{label} satisfies the source/target/kernel/image/cokernel Mittag-Leffler gate",
                ],
                inverse_limit_gate=k3e_inverse_limit_gate_requirement(
                    name,
                    proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
                ),
                summary=(
                    f"{label} records the source transition map, the candidate target truncation, "
                    f"and the inverse-limit exactness obstruction layer"
                ),
            ),
            construction_requirement=k3e_bridge_construction_requirement_from_witnesses(
                name,
                closure_witnesses,
            ),
            status=data.status,
            dependency_obligations=data.dependency_obligations,
            local_obligations_satisfied=data.local_obligations_satisfied,
        ))
    summary = (
        "the axiom-pack boundary report separates the source gate from labeled BD1-BD7 bridge axioms "
        "and attaches heightwise compatibility conditions bridge by bridge"
    )
    return K3EBridgeAxiomPack(
        source_gate=source_gate,
        entries=bd_entries,
        inverse_limit_gate=k3e_inverse_limit_gate_requirement(
            "bridge_axiom_pack",
            proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
        ),
        pro_recognition_gate=k3e_pro_recognition_gate_requirement(
            "bridge_axiom_pack",
            proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
        ),
        construction_requirements=k3e_bridge_construction_requirements_from_witnesses(
            closure_witnesses
        ),
        summary=summary,
    )


def k3e_theorem_boundary_report(
    max_discriminant: int = 8,
    max_degree: int = 5,
    max_n: int = 10,
    closure_witnesses: Optional[K3EClosureWitnesses] = None,
) -> K3ETheoremBoundaryReport:
    """Derive the exact theorem boundary from the existing gap reports."""
    closure_witnesses = closure_witnesses or K3EClosureWitnesses()
    source = source_recognition_record(closure_witnesses=closure_witnesses)
    core = k3e_core_gap_report(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    status = k3e_gap_status_table(
        max_discriminant=max_discriminant,
        max_degree=max_degree,
        max_n=max_n,
        closure_witnesses=closure_witnesses,
    )
    source_conditions = []
    if not closure_witnesses.source_gate_closed:
        source_conditions.append("close the source-side Hall/Borcherds gate")
        source_conditions.extend(source.boundary_report.required_conditions)
    if not closure_witnesses.source_recognition_envelope_completed:
        source_conditions.append("complete the source recognition envelope")
    if not source.boundary_report.compact_double_report.closed:
        source_conditions.extend(
            source.boundary_report.compact_double_report.remaining_defects
        )
    source_conditions = list(dict.fromkeys(source_conditions))
    comparison_conditions = []
    witnessed_bridges = closure_witnesses.bridge_construction_set
    for gap_name in [
        "framed_d3_assignment",
        "compact_hall_promotion",
        "scattering_root_identification",
        "bkm_bar_dictionary",
        "shadow_rademacher_comparison",
        "brst_realization",
        "vertex_operator_yangian",
    ]:
        if gap_name not in witnessed_bridges:
            comparison_conditions.extend(status.rows[gap_name].missing)
    inverse_limit_conditions = [
        "prove all heightwise compatibility maps",
        "prove the rank-zero bridge-square criterion at every height",
        "prove the Mittag-Leffler source/target/kernel/image/cokernel exactness gate",
        "prove the inverse-limit compatibility and exactness theorem",
        "prove that transition maps on source and target sides commute",
    ]
    inverse_limit_gate = k3e_inverse_limit_gate_requirement(
        "theorem_boundary",
        proved_conditions=closure_witnesses.inverse_limit_proved_conditions,
    )
    pro_recognition_gate = k3e_pro_recognition_gate_requirement(
        "theorem_boundary",
        proved_conditions=closure_witnesses.pro_recognition_proved_conditions,
    )
    if inverse_limit_gate.all_proved:
        inverse_limit_conditions = []
    inverse_limit_conditions.extend(inverse_limit_gate.open_conditions)
    inverse_limit_conditions.extend(pro_recognition_gate.open_conditions)
    construction_requirements = k3e_bridge_construction_requirements_from_witnesses(
        closure_witnesses
    )
    all_conditions = []
    for seq in [source_conditions, comparison_conditions, inverse_limit_conditions]:
        for item in seq:
            if item not in all_conditions:
                all_conditions.append(item)
    summary = (
        "the theorem boundary is the union of the source-side recognition conditions, "
        "the seven core gap conditions, and the inverse-limit compatibilities"
    )
    return K3ETheoremBoundaryReport(
        source_conditions=source_conditions,
        comparison_conditions=comparison_conditions,
        inverse_limit_conditions=inverse_limit_conditions,
        inverse_limit_gate=inverse_limit_gate,
        pro_recognition_gate=pro_recognition_gate,
        construction_requirements=construction_requirements,
        all_conditions=all_conditions,
        summary=summary,
    )
