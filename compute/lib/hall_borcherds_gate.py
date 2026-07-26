"""Executable gate for the Hall-Drinfeld-double to Borcherds comparison.

The gate separates three statements that are often conflated:

* the Borcherds weight identity
  kappa_BKM(Delta_5) = c_1(0) / 2 = 5;
* the K3 x E four-invariant spectrum
  (kappa_cat, kappa_ch_Heis, kappa_BKM, kappa_fiber) = (0, 3, 5, 24);
* the still-typed Hall/Borcherds comparison from an oriented critical
  CoHA and its Hall-Drinfeld double to the BKM denominator datum.

The first two are exact local checks.  The third is an implication gate:
it is closed only when the orientation, Hopf pairing, Drinfeld double,
denominator normalization, root-multiplicity map, and anti-shortcut
separations are all supplied as witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from math import gcd
from typing import Any, Dict, Iterable, Optional, Tuple

Vector = Tuple[Fraction, ...]
Matrix = Tuple[Vector, ...]


def borcherds_weight_from_c0(c0: int) -> Fraction:
    """Return the Borcherds lift weight c0 / 2."""
    return Fraction(c0, 2)


@dataclass(frozen=True)
class DenominatorDatum:
    """Primitive denominator normalization data."""

    primitive_form: str
    input_constant_c0: int
    square_form: str
    source: str

    @property
    def kappa_BKM(self) -> Fraction:
        return borcherds_weight_from_c0(self.input_constant_c0)

    @property
    def square_weight(self) -> Fraction:
        return 2 * self.kappa_BKM


DELTA5_DATUM = DenominatorDatum(
    primitive_form="Delta_5",
    input_constant_c0=10,
    square_form="Phi_10 = Delta_5^2",
    source="Borcherds weight theorem with the Gritsenko-Nikulin Delta_5 normalization",
)


K3XE_INVARIANT_SPECTRUM: Dict[str, Fraction] = {
    "kappa_cat_total": Fraction(0),
    "kappa_ch_Heis": Fraction(3),
    "kappa_BKM_Delta_5": Fraction(5),
    "kappa_fiber_Mukai_rank": Fraction(24),
}


def k3xe_spectrum_tuple() -> Tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return the ordered K3 x E spectrum (0, 3, 5, 24)."""
    return (
        K3XE_INVARIANT_SPECTRUM["kappa_cat_total"],
        K3XE_INVARIANT_SPECTRUM["kappa_ch_Heis"],
        K3XE_INVARIANT_SPECTRUM["kappa_BKM_Delta_5"],
        K3XE_INVARIANT_SPECTRUM["kappa_fiber_Mukai_rank"],
    )


@dataclass(frozen=True)
class HallBorcherdsWitnesses:
    """Boolean witnesses required before the Hall/Borcherds bridge is closed."""

    oriented_critical_coha: bool = False
    hopf_pairing: bool = False
    drinfeld_double: bool = False
    denominator_normalization: bool = False
    root_multiplicity_map: bool = False
    k3xe_spectrum_separated: bool = False
    coha_positive_half_not_w: bool = False
    bkm_object_not_yangian: bool = False


REQUIRED_WITNESSES: Tuple[str, ...] = (
    "oriented_critical_coha",
    "hopf_pairing",
    "drinfeld_double",
    "denominator_normalization",
    "root_multiplicity_map",
    "k3xe_spectrum_separated",
    "coha_positive_half_not_w",
    "bkm_object_not_yangian",
)


@dataclass(frozen=True)
class GateReport:
    """Result of evaluating the comparison gate."""

    status: str
    closed: bool
    missing_witnesses: Tuple[str, ...]
    implications: Dict[str, bool]


def missing_witnesses(witnesses: HallBorcherdsWitnesses) -> Tuple[str, ...]:
    """List the witnesses not present in a Hall/Borcherds package."""
    return tuple(name for name in REQUIRED_WITNESSES if not getattr(witnesses, name))


def evaluate_gate(witnesses: HallBorcherdsWitnesses) -> GateReport:
    """Evaluate the Hall/Borcherds implication lattice."""
    missing = missing_witnesses(witnesses)
    implications = {
        "positive_half_constructed": witnesses.oriented_critical_coha,
        "drinfeld_double_constructed": (
            witnesses.oriented_critical_coha
            and witnesses.hopf_pairing
            and witnesses.drinfeld_double
        ),
        "denominator_weight_verified": (
            witnesses.denominator_normalization
            and DELTA5_DATUM.kappa_BKM == Fraction(5)
            and DELTA5_DATUM.square_weight == Fraction(10)
        ),
        "root_multiplicity_lane_available": (
            witnesses.denominator_normalization and witnesses.root_multiplicity_map
        ),
        "spectrum_not_used_as_bridge": witnesses.k3xe_spectrum_separated,
        "anti_shortcuts_cleared": (
            witnesses.coha_positive_half_not_w and witnesses.bkm_object_not_yangian
        ),
    }
    closed = not missing and all(implications.values())
    status = "CLOSED_FROM_WITNESSES" if closed else "OPEN_TYPED_GATE"
    return GateReport(status=status, closed=closed, missing_witnesses=missing, implications=implications)


@dataclass(frozen=True)
class RecognitionEnvelopeWitnesses:
    """Finite data separating the universal envelope from faithful recognition."""

    finite_compact_double: bool = False
    finite_borcherds_target: bool = False
    compact_source_packet: bool = False
    radical_isometry: bool = False
    serre_kernel_exact: bool = False
    green_adjoint_coproduct: bool = False
    primitive_center_reduction: bool = False
    associator_class_match: bool = False
    parity_fixture_match: bool = False
    transition_compatible: bool = False


FINITE_DEFECT_WITNESSES: Dict[str, str] = {
    "R": "radical_isometry",
    "S": "serre_kernel_exact",
    "D": "green_adjoint_coproduct",
    "C": "primitive_center_reduction",
    "A": "associator_class_match",
    "P": "parity_fixture_match",
}


@dataclass(frozen=True)
class RecognitionEnvelopeReport:
    """Status of the finite Hall-Borcherds recognition envelope."""

    envelope_constructed: bool
    source_packet_constructed: bool
    source_faithfulness_forced: bool
    finite_unquotiented_recognized: bool
    completed_envelope_constructed: bool
    completed_source_faithfulness: bool
    completed_unquotiented_recognized: bool
    vanished_defects: Tuple[str, ...]
    remaining_defects: Tuple[str, ...]
    status: str


@dataclass(frozen=True)
class HeightRecognitionWitness:
    """Witness packet for one finite Borcherds height."""

    height: int
    witnesses: RecognitionEnvelopeWitnesses


@dataclass(frozen=True)
class HeightRecognitionRow:
    """Finite-height recognition row with its obstruction labels."""

    height: int
    report: RecognitionEnvelopeReport
    failure_modes: Tuple[str, ...]
    closed: bool


@dataclass(frozen=True)
class HeightwiseRecognitionReport:
    """Heightwise obstruction report and first failure height H0."""

    rows: Tuple[HeightRecognitionRow, ...]
    first_failure_height: Optional[int]
    first_failure_modes: Tuple[str, ...]
    completed: bool
    status: str


@dataclass(frozen=True)
class FiniteBorcherdsTargetPacketWitnesses:
    """Witnesses that the finite Serre-Borcherds target packet is present."""

    current_quotient: bool = False
    root_parity_basis: bool = False
    invariant_form_and_cartan_radical: bool = False
    serre_presentation: bool = False
    pbw_basis: bool = False
    coproduct: bool = False
    primitive_center: bool = False
    associator_complex: bool = False
    transition_compatible: bool = False


TARGET_PACKET_WITNESSES: Tuple[str, ...] = (
    "current_quotient",
    "root_parity_basis",
    "invariant_form_and_cartan_radical",
    "serre_presentation",
    "pbw_basis",
    "coproduct",
    "primitive_center",
    "associator_complex",
    "transition_compatible",
)


@dataclass(frozen=True)
class FiniteBorcherdsTargetPacketReport:
    """Status of the finite Serre-Borcherds target packet."""

    closed: bool
    missing_witnesses: Tuple[str, ...]
    status: str


@dataclass(frozen=True)
class FiniteComparisonMatrixPacketWitnesses:
    """Witnesses that finite Hall-to-Borcherds comparison matrices are present.

    This packet records the existence of blockwise candidate matrices only.
    It does not assert that those matrices preserve the Hall pairing, Serre
    rows, coproduct, centre, or associator class.
    """

    source_packet: bool = False
    target_packet: bool = False
    charge_block_bijection: bool = False
    parity_block_bijection: bool = False
    primitive_dimension_match: bool = False
    source_quotient_bases: bool = False
    target_root_bases: bool = False
    comparison_matrices_supplied: bool = False
    negative_half_dual_matrices_supplied: bool = False
    quotient_maps_supplied: bool = False
    transition_compatible: bool = False
    defect_vanishing_separated: bool = False


COMPARISON_PACKET_WITNESSES: Tuple[str, ...] = (
    "source_packet",
    "target_packet",
    "charge_block_bijection",
    "parity_block_bijection",
    "primitive_dimension_match",
    "source_quotient_bases",
    "target_root_bases",
    "comparison_matrices_supplied",
    "negative_half_dual_matrices_supplied",
    "quotient_maps_supplied",
    "transition_compatible",
    "defect_vanishing_separated",
)


@dataclass(frozen=True)
class FiniteComparisonMatrixPacketReport:
    """Status of the finite Hall-to-Borcherds comparison-matrix packet."""

    closed: bool
    missing_witnesses: Tuple[str, ...]
    defect_vanishing_forced: bool
    status: str


@dataclass(frozen=True)
class FiniteComparisonShapeReport:
    """Exact row, column, quotient-rank, and comparison-rank shape report."""

    component_defects: Dict[str, int]
    remaining_components: Tuple[str, ...]
    closed: bool
    defect_vanishing_forced: bool
    status: str


@dataclass(frozen=True)
class FiniteRecognitionCertificateReport:
    """Finite recognition certificate combining packet, shape, and defects."""

    packet_report: FiniteComparisonMatrixPacketReport
    shape_report: FiniteComparisonShapeReport
    matrix_report: Optional["FiniteMatrixDefectReport"]
    recognition_report: Optional[RecognitionEnvelopeReport]
    remaining_conditions: Tuple[str, ...]
    closed: bool
    status: str


@dataclass(frozen=True)
class FiniteMatrixDefectWitness:
    """Exact finite matrices for the six Hall/Borcherds defects.

    Bases are row-vector bases over Q.  The comparison matrices send
    source column coordinates to target column coordinates, so the target
    form pulls back as L^t G R.  If no right comparison is supplied, the
    engine uses the left comparison on both sides.  Equivalently, each
    side may be supplied as a quotient map Q followed by a post-quotient
    comparison A; the engine then uses A Q on that side.
    """

    radical_basis: Matrix
    positive_pairing_matrix: Matrix
    negative_pairing_matrix: Matrix
    source_pairing_matrix: Matrix
    target_pairing_matrix: Matrix
    comparison_matrix: Matrix
    hall_serre_kernel_basis: Matrix
    borcherds_serre_basis: Matrix
    hall_coproduct_matrix: Matrix
    borcherds_coproduct_matrix: Matrix
    primitive_center_basis: Matrix
    allowed_center_basis: Matrix
    hall_associator: Vector
    borcherds_associator: Vector
    gauge_coboundary_basis: Matrix
    transition_compatible: bool = True
    quotient_map: Optional[Matrix] = None
    post_quotient_comparison_matrix: Optional[Matrix] = None
    right_comparison_matrix: Optional[Matrix] = None
    right_quotient_map: Optional[Matrix] = None
    right_post_quotient_comparison_matrix: Optional[Matrix] = None
    right_radical_basis: Optional[Matrix] = None
    tensor_pairing_matrix: Optional[Matrix] = None
    negative_product_matrix: Optional[Matrix] = None
    serre_relation_matrix: Optional[Matrix] = None
    hall_bracket_evaluation_matrix: Optional[Matrix] = None
    borcherds_hilbert_vector: Optional[Vector] = None
    hall_hilbert_vector: Optional[Vector] = None
    centrality_matrix: Optional[Matrix] = None
    cartan_component_basis: Optional[Matrix] = None
    cartan_radical_basis: Optional[Matrix] = None
    associator_cocycle_matrix: Optional[Matrix] = None
    gauge_constraint_matrix: Optional[Matrix] = None
    source_parity_signs: Optional[Vector] = None
    target_parity_signs: Optional[Vector] = None


@dataclass(frozen=True)
class FiniteMatrixDefectReport:
    """Exact finite-matrix report for R, S, D, C, A, P."""

    radical_kernel_defect: int
    right_radical_kernel_defect: int
    quotient_kernel_defect: int
    radical_isometry_defect: int
    serre_defect: int
    serre_inclusion_defect: int
    pbw_hilbert_defect: int
    coproduct_defect: int
    green_identity_defect: int
    center_defect: int
    centrality_defect: int
    cartan_radical_defect: int
    associator_cocycle_defect: int
    gauge_cocycle_defect: int
    gauge_constraint_defect: int
    associator_defect: int
    parity_defect: int
    vanished_defects: Tuple[str, ...]
    remaining_defects: Tuple[str, ...]
    recognition_witnesses: RecognitionEnvelopeWitnesses


@dataclass(frozen=True)
class FiniteCoproductIntertwiningGate:
    """Exact finite coproduct and Green-adjunction gate for D."""

    coproduct_left: Matrix
    coproduct_right: Matrix
    coproduct_difference: Matrix
    green_left: Matrix
    green_right: Matrix
    green_difference: Matrix
    coproduct_defect_rank: int
    green_defect_rank: int
    green_data_supplied: bool
    coproduct_intertwines: bool
    green_adjoint: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class HeightMatrixDefectWitness:
    """Exact matrix witness packet at one finite Borcherds height."""

    height: int
    witness: FiniteMatrixDefectWitness


@dataclass(frozen=True)
class HeightMatrixDefectRow:
    """One matrix-derived finite-height defect row."""

    height: int
    matrix_report: FiniteMatrixDefectReport
    recognition_row: HeightRecognitionRow


@dataclass(frozen=True)
class HeightwiseMatrixDefectReport:
    """Heightwise H0 report derived from exact finite matrix witnesses."""

    matrix_rows: Tuple[HeightMatrixDefectRow, ...]
    recognition_report: HeightwiseRecognitionReport
    transition_reports: Tuple["FiniteMatrixTransitionReport", ...] = ()


@dataclass(frozen=True)
class FiniteMatrixTransitionWitness:
    """Restricted upper-height data and lower-height target data."""

    upper_height: int
    lower_height: int
    restricted_upper_witness: FiniteMatrixDefectWitness
    lower_witness: FiniteMatrixDefectWitness


@dataclass(frozen=True)
class FiniteMatrixTransitionReport:
    """Exact transition-compatibility report between two finite heights."""

    upper_height: int
    lower_height: int
    component_defects: Dict[str, int]
    remaining_components: Tuple[str, ...]
    closed: bool


@dataclass(frozen=True)
class HeightRecognitionCertificateWitness:
    """Packet and matrix witnesses for one finite recognition certificate."""

    height: int
    comparison_witnesses: FiniteComparisonMatrixPacketWitnesses
    matrix_witness: FiniteMatrixDefectWitness


@dataclass(frozen=True)
class HeightRecognitionCertificateRow:
    """One heightwise certificate row with its failure conditions."""

    height: int
    certificate_report: FiniteRecognitionCertificateReport
    transition_conditions: Tuple[str, ...]
    failure_conditions: Tuple[str, ...]
    closed: bool


@dataclass(frozen=True)
class HeightwiseRecognitionCertificateReport:
    """Heightwise certificate report with first failure height H0."""

    rows: Tuple[HeightRecognitionCertificateRow, ...]
    transition_reports: Tuple[FiniteMatrixTransitionReport, ...]
    first_failure_height: Optional[int]
    first_failure_conditions: Tuple[str, ...]
    pro_exactness_conditions: Tuple[str, ...]
    completed: bool
    status: str


@dataclass(frozen=True)
class SourceGateObligationEntry:
    """Typed source-side proof obligation entry."""

    witness: Any
    missing: Tuple[str, ...]
    target: str
    status: str


@dataclass(frozen=True)
class SourceGateObligationMatrix:
    """Source-side proof obligations for the Hall/Borcherds gate."""

    gate: SourceGateObligationEntry
    envelope: SourceGateObligationEntry
    summary: str


@dataclass(frozen=True)
class SourceGateTaskEntry:
    """Typed source-side task entry."""

    node: str
    tasks: Tuple[str, ...]


@dataclass(frozen=True)
class SourceGateTaskMap:
    """Bridge-by-bridge task map for the source Hall/Borcherds gate."""

    entries: Tuple[SourceGateTaskEntry, ...]
    summary: str

    @property
    def tasks(self) -> Dict[str, SourceGateTaskEntry]:
        return {entry.node: entry for entry in self.entries}


@dataclass(frozen=True)
class SourceGateObstructionClass:
    """Named source-side obstruction class for compact Hall promotion."""

    code: str
    tex: str
    layer: str
    meaning: str
    required_vanishing: str


@dataclass(frozen=True)
class SourceGateObstructionTaxonomy:
    """Compact, finite, and pro-recognition obstruction split."""

    compact_passage: Tuple[SourceGateObstructionClass, ...]
    double_data: Tuple[SourceGateObstructionClass, ...]
    finite_recognition: Tuple[SourceGateObstructionClass, ...]
    pro_recognition: Tuple[SourceGateObstructionClass, ...]
    summary: str

    @property
    def classes(self) -> Tuple[SourceGateObstructionClass, ...]:
        return self.compact_passage + self.double_data + self.finite_recognition + self.pro_recognition

    @property
    def compact_double_required_vanishings(self) -> Tuple[str, ...]:
        return tuple(
            cls.required_vanishing
            for cls in self.compact_passage + self.double_data
        )

    @property
    def required_vanishings(self) -> Tuple[str, ...]:
        return tuple(cls.required_vanishing for cls in self.classes)

    @property
    def pro_required_vanishings(self) -> Tuple[str, ...]:
        return tuple(cls.required_vanishing for cls in self.pro_recognition)

    @property
    def by_code(self) -> Dict[str, SourceGateObstructionClass]:
        return {cls.code: cls for cls in self.classes}


@dataclass(frozen=True)
class SourceCompactDoubleGateWitnesses:
    """Witnesses for compact-passage and double-data gates."""

    compact_ml_exactness: bool = False
    compact_critical_realization: bool = False
    compact_support_properness: bool = False
    double_coproduct: bool = False
    double_pairing: bool = False
    double_center: bool = False


@dataclass(frozen=True)
class SourceCompactDoubleGateReport:
    """Evaluation of compact-passage and double-data obstruction gates."""

    closed: bool
    missing_witnesses: Tuple[str, ...]
    remaining_defects: Tuple[str, ...]
    status: str


@dataclass(frozen=True)
class SourceProRecognitionGateWitnesses:
    """Witnesses for the three source-side pro-recognition gates."""

    separated_completion: bool = False
    defect_ideal_exactness: bool = False
    heegner_borcherds_coefficient_comparison: bool = False


@dataclass(frozen=True)
class SourceProRecognitionGateReport:
    """Evaluation of Q_H^sep, L_H^ex, and H_H^HB."""

    closed: bool
    missing_witnesses: Tuple[str, ...]
    remaining_defects: Tuple[str, ...]
    status: str


@dataclass(frozen=True)
class FiniteSourceProRecognitionMatrixGate:
    """Finite matrix gate for Q_H^sep, L_H^ex, and H_H^HB."""

    lower_completion_dimension: int
    completion_transition_rank: int
    separation_defect_matrix: Matrix
    separation_defect_rank: int
    lower_defect_ideal_dimension: int
    defect_ideal_transition_rank: int
    defect_ideal_landing_defect_matrix: Matrix
    defect_ideal_landing_defect_rank: int
    coefficient_defect_matrix: Matrix
    coefficient_defect_rank: int
    separated_completion: bool
    defect_ideal_exact: bool
    heegner_borcherds_coefficients_match: bool
    closed: bool
    status: str


@dataclass(frozen=True)
class SourceGateBoundaryReport:
    """Derived boundary report for the source Hall/Borcherds gate."""

    obligation_matrix: SourceGateObligationMatrix
    task_map: SourceGateTaskMap
    obstruction_taxonomy: SourceGateObstructionTaxonomy
    compact_double_report: SourceCompactDoubleGateReport
    pro_recognition_report: SourceProRecognitionGateReport
    required_conditions: Tuple[str, ...]
    closed: bool
    summary: str


def finite_defect_vanishings(witnesses: RecognitionEnvelopeWitnesses) -> Dict[str, bool]:
    """Return the six finite defect vanishings R, S, D, C, A, P."""
    return {
        defect: getattr(witnesses, field)
        for defect, field in FINITE_DEFECT_WITNESSES.items()
    }


def evaluate_finite_borcherds_target_packet(
    witnesses: FiniteBorcherdsTargetPacketWitnesses,
) -> FiniteBorcherdsTargetPacketReport:
    """Evaluate whether the finite Serre-Borcherds target packet is complete."""
    missing = tuple(
        name for name in TARGET_PACKET_WITNESSES if not getattr(witnesses, name)
    )
    closed = not missing
    status = "FINITE_BORCHERDS_TARGET_PACKET" if closed else "MISSING_TARGET_PACKET_ROWS"
    return FiniteBorcherdsTargetPacketReport(
        closed=closed,
        missing_witnesses=missing,
        status=status,
    )


def evaluate_finite_comparison_matrix_packet(
    witnesses: FiniteComparisonMatrixPacketWitnesses,
) -> FiniteComparisonMatrixPacketReport:
    """Evaluate whether the finite source-to-target comparison packet is complete."""
    missing = tuple(
        name for name in COMPARISON_PACKET_WITNESSES if not getattr(witnesses, name)
    )
    closed = not missing
    status = "FINITE_COMPARISON_MATRIX_PACKET" if closed else "MISSING_COMPARISON_PACKET_ROWS"
    return FiniteComparisonMatrixPacketReport(
        closed=closed,
        missing_witnesses=missing,
        defect_vanishing_forced=False,
        status=status,
    )


def _fraction_vector(vector: Iterable[Any]) -> Vector:
    return tuple(Fraction(entry) for entry in vector)


def _fraction_matrix(matrix: Iterable[Iterable[Any]]) -> Matrix:
    rows = tuple(_fraction_vector(row) for row in matrix)
    if not rows:
        return ()
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have the same width")
    return rows


def _matrix_width(matrix: Matrix) -> int:
    return len(matrix[0]) if matrix else 0


def _matrix_transpose(matrix: Matrix) -> Matrix:
    matrix = _fraction_matrix(matrix)
    if not matrix:
        return ()
    return tuple(tuple(row[column] for row in matrix) for column in range(len(matrix[0])))


def _matrix_difference(left: Matrix, right: Matrix) -> Matrix:
    left = _fraction_matrix(left)
    right = _fraction_matrix(right)
    if len(left) != len(right) or _matrix_width(left) != _matrix_width(right):
        raise ValueError("matrix dimensions must agree")
    return tuple(
        tuple(left_row[column] - right_row[column] for column in range(_matrix_width(left)))
        for left_row, right_row in zip(left, right)
    )


def _matrix_product(left: Matrix, right: Matrix) -> Matrix:
    left = _fraction_matrix(left)
    right = _fraction_matrix(right)
    if not left or not right:
        raise ValueError("matrix product requires nonempty matrices")
    if _matrix_width(left) != len(right):
        raise ValueError("matrix dimensions do not compose")
    right_t = _matrix_transpose(right)
    return tuple(
        tuple(sum(a * b for a, b in zip(left_row, right_column)) for right_column in right_t)
        for left_row in left
    )


def _matrix_vector_product(matrix: Matrix, vector: Vector) -> Vector:
    matrix = _fraction_matrix(matrix)
    vector = _fraction_vector(vector)
    if not matrix:
        return ()
    if _matrix_width(matrix) != len(vector):
        raise ValueError("matrix and vector dimensions do not compose")
    return tuple(sum(entry * value for entry, value in zip(row, vector)) for row in matrix)


def exact_matrix_rank(matrix: Iterable[Iterable[Any]]) -> int:
    """Return the rank over Q by Gaussian elimination."""
    rows = [list(row) for row in _fraction_matrix(matrix)]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if rows[row][column] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor != 0:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def _rref(matrix: Iterable[Iterable[Any]]) -> Tuple[Matrix, Tuple[int, ...]]:
    rows = [list(row) for row in _fraction_matrix(matrix)]
    if not rows:
        return (), ()
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    pivot_columns = []
    for column in range(column_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if rows[row][column] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor != 0:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    nonzero_rows = tuple(
        tuple(row)
        for row in rows
        if any(entry != 0 for entry in row)
    )
    return nonzero_rows, tuple(pivot_columns)


def row_space_basis(vectors: Iterable[Iterable[Any]]) -> Matrix:
    """Return a row-space basis over Q in reduced echelon form."""
    return _rref(vectors)[0]


def right_kernel_basis(
    matrix: Iterable[Iterable[Any]],
    ambient_dim: Optional[int] = None,
) -> Matrix:
    """Return a row basis for the right kernel of a rational matrix."""
    matrix = _fraction_matrix(matrix)
    if not matrix:
        if ambient_dim is None:
            raise ValueError("ambient_dim is required for the kernel of an empty matrix")
        return tuple(
            tuple(Fraction(1) if i == j else Fraction(0) for i in range(ambient_dim))
            for j in range(ambient_dim)
        )
    column_count = _matrix_width(matrix)
    rref_rows, pivot_columns = _rref(matrix)
    pivot_set = set(pivot_columns)
    free_columns = [column for column in range(column_count) if column not in pivot_set]
    basis = []
    for free_column in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free_column] = Fraction(1)
        for row_index, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -rref_rows[row_index][free_column]
        basis.append(tuple(vector))
    return tuple(basis)


def intersection_basis(
    left_basis: Iterable[Iterable[Any]],
    right_basis: Iterable[Iterable[Any]],
) -> Matrix:
    """Return a row basis for the intersection of two row spans."""
    left = row_space_basis(left_basis)
    right = row_space_basis(right_basis)
    if not left or not right:
        return ()
    width = _matrix_width(left)
    if _matrix_width(right) != width:
        raise ValueError("subspaces must have the same ambient dimension")
    equations = tuple(
        tuple(left_row[column] for left_row in left)
        + tuple(-right_row[column] for right_row in right)
        for column in range(width)
    )
    coefficient_basis = right_kernel_basis(
        equations,
        ambient_dim=len(left) + len(right),
    )
    intersection_vectors = []
    for coefficients in coefficient_basis:
        left_coefficients = coefficients[: len(left)]
        vector = tuple(
            sum(coefficient * row[column] for coefficient, row in zip(left_coefficients, left))
            for column in range(width)
        )
        intersection_vectors.append(vector)
    return row_space_basis(intersection_vectors)


def subspace_symmetric_defect_dimension(
    left_basis: Iterable[Iterable[Any]],
    right_basis: Iterable[Iterable[Any]],
) -> int:
    """Return dim(U/(U cap V)) + dim(V/(U cap V)) for row spans."""
    left = row_space_basis(left_basis)
    right = row_space_basis(right_basis)
    if not left and not right:
        return 0
    if left and right and _matrix_width(left) != _matrix_width(right):
        raise ValueError("subspaces must have the same ambient dimension")
    intersection = intersection_basis(left, right)
    return len(left) + len(right) - 2 * len(intersection)


def subspace_containment_defect_dimension(
    subspace_basis: Iterable[Iterable[Any]],
    containing_basis: Iterable[Iterable[Any]],
) -> int:
    """Return dim(U/(U cap V)) for row spans U and V."""
    subspace = row_space_basis(subspace_basis)
    containing = row_space_basis(containing_basis)
    if not subspace:
        return 0
    if not containing:
        return len(subspace)
    if _matrix_width(subspace) != _matrix_width(containing):
        raise ValueError("subspaces must have the same ambient dimension")
    return len(subspace) - len(intersection_basis(subspace, containing))


def vector_in_row_span(vector: Iterable[Any], basis: Iterable[Iterable[Any]]) -> bool:
    """Return whether a vector lies in the row span over Q."""
    vector = _fraction_vector(vector)
    basis = row_space_basis(basis)
    if not basis:
        return all(entry == 0 for entry in vector)
    if len(vector) != _matrix_width(basis):
        raise ValueError("vector and basis ambient dimensions must agree")
    return exact_matrix_rank(basis + (vector,)) == len(basis)


def pullback_pairing_matrix(
    comparison_matrix: Iterable[Iterable[Any]],
    target_pairing_matrix: Iterable[Iterable[Any]],
) -> Matrix:
    """Return A^t G A for a source-to-target comparison matrix A."""
    return pullback_bilinear_pairing_matrix(
        comparison_matrix,
        target_pairing_matrix,
        comparison_matrix,
    )


def pullback_bilinear_pairing_matrix(
    left_comparison_matrix: Iterable[Iterable[Any]],
    target_pairing_matrix: Iterable[Iterable[Any]],
    right_comparison_matrix: Iterable[Iterable[Any]],
) -> Matrix:
    """Return L^t G R for a two-slot source-to-target comparison."""
    left = _fraction_matrix(left_comparison_matrix)
    target = _fraction_matrix(target_pairing_matrix)
    right = _fraction_matrix(right_comparison_matrix)
    return _matrix_product(
        _matrix_product(_matrix_transpose(left), target),
        right,
    )


def _resolved_side_comparison(
    comparison_matrix: Optional[Matrix],
    quotient_map: Optional[Matrix],
    post_quotient_comparison_matrix: Optional[Matrix],
    side_name: str,
) -> Optional[Matrix]:
    if quotient_map is None and post_quotient_comparison_matrix is None:
        return None if comparison_matrix is None else _fraction_matrix(comparison_matrix)
    if quotient_map is None or post_quotient_comparison_matrix is None:
        raise ValueError(f"{side_name} quotient and post-quotient comparison must be supplied together")
    return _matrix_product(
        _fraction_matrix(post_quotient_comparison_matrix),
        _fraction_matrix(quotient_map),
    )


def resolved_comparison_matrix(witness: FiniteMatrixDefectWitness) -> Matrix:
    """Return the source-to-target comparison matrix, using A Q when supplied."""
    resolved = _resolved_side_comparison(
        witness.comparison_matrix,
        witness.quotient_map,
        witness.post_quotient_comparison_matrix,
        "left",
    )
    if resolved is None:
        raise ValueError("comparison_matrix is required")
    return resolved


def resolved_comparison_matrices(witness: FiniteMatrixDefectWitness) -> Tuple[Matrix, Matrix]:
    """Return the left and right comparison matrices for the bilinear pairing."""
    left = resolved_comparison_matrix(witness)
    right = _resolved_side_comparison(
        witness.right_comparison_matrix,
        witness.right_quotient_map,
        witness.right_post_quotient_comparison_matrix,
        "right",
    )
    return left, (left if right is None else right)


def _dimension_defect(actual: int, expected: int) -> int:
    return abs(actual - expected)


def _rank_defect(matrix: Matrix, expected_rank: int) -> int:
    return abs(exact_matrix_rank(matrix) - expected_rank)


def _quotient_shape_defects(
    prefix: str,
    quotient_map: Optional[Matrix],
    post_quotient_comparison_matrix: Optional[Matrix],
    source_dimension: int,
    target_dimension: int,
) -> Dict[str, int]:
    if quotient_map is None and post_quotient_comparison_matrix is None:
        return {}
    if quotient_map is None or post_quotient_comparison_matrix is None:
        raise ValueError(f"{prefix} quotient and post-quotient comparison must be supplied together")
    quotient = _fraction_matrix(quotient_map)
    post = _fraction_matrix(post_quotient_comparison_matrix)
    quotient_dimension = len(quotient)
    return {
        f"{prefix}_quotient_width": _dimension_defect(_matrix_width(quotient), source_dimension),
        f"{prefix}_quotient_dimension": _dimension_defect(quotient_dimension, target_dimension),
        f"{prefix}_quotient_rank": _rank_defect(quotient, quotient_dimension),
        f"{prefix}_post_rows": _dimension_defect(len(post), target_dimension),
        f"{prefix}_post_columns": _dimension_defect(_matrix_width(post), quotient_dimension),
        f"{prefix}_post_rank": _rank_defect(post, target_dimension),
    }


def finite_comparison_shape_report(
    witness: FiniteMatrixDefectWitness,
) -> FiniteComparisonShapeReport:
    """Check exact source/target dimensions for the candidate comparison matrices."""
    source_pairing = _fraction_matrix(witness.source_pairing_matrix)
    target_pairing = _fraction_matrix(witness.target_pairing_matrix)
    source_left_dimension = len(source_pairing)
    source_right_dimension = _matrix_width(source_pairing)
    target_left_dimension = len(target_pairing)
    target_right_dimension = _matrix_width(target_pairing)
    left_comparison, right_comparison = resolved_comparison_matrices(witness)
    component_defects: Dict[str, int] = {
        "left_rows": _dimension_defect(len(left_comparison), target_left_dimension),
        "left_columns": _dimension_defect(_matrix_width(left_comparison), source_left_dimension),
        "left_rank": _rank_defect(left_comparison, target_left_dimension),
        "right_rows": _dimension_defect(len(right_comparison), target_right_dimension),
        "right_columns": _dimension_defect(_matrix_width(right_comparison), source_right_dimension),
        "right_rank": _rank_defect(right_comparison, target_right_dimension),
    }
    component_defects.update(
        _quotient_shape_defects(
            "left",
            witness.quotient_map,
            witness.post_quotient_comparison_matrix,
            source_left_dimension,
            target_left_dimension,
        )
    )
    component_defects.update(
        _quotient_shape_defects(
            "right",
            witness.right_quotient_map,
            witness.right_post_quotient_comparison_matrix,
            source_right_dimension,
            target_right_dimension,
        )
    )
    remaining = tuple(
        component for component, defect in component_defects.items() if defect != 0
    )
    closed = not remaining
    return FiniteComparisonShapeReport(
        component_defects=component_defects,
        remaining_components=remaining,
        closed=closed,
        defect_vanishing_forced=False,
        status="FINITE_COMPARISON_SHAPE_CLOSED" if closed else "FINITE_COMPARISON_SHAPE_DEFECT",
    )


def right_radical_basis(witness: FiniteMatrixDefectWitness) -> Matrix:
    """Return the right-slot radical basis, defaulting to the left basis."""
    return (
        _fraction_matrix(witness.radical_basis)
        if witness.right_radical_basis is None
        else _fraction_matrix(witness.right_radical_basis)
    )


def quotient_kernel_defect_dimension(witness: FiniteMatrixDefectWitness) -> int:
    """Return the defect measuring whether explicit quotient maps kill exactly K."""
    defect = 0
    if witness.quotient_map is not None:
        defect += subspace_symmetric_defect_dimension(
            right_kernel_basis(witness.quotient_map),
            witness.radical_basis,
        )
    if witness.right_quotient_map is not None:
        defect += subspace_symmetric_defect_dimension(
            right_kernel_basis(witness.right_quotient_map),
            right_radical_basis(witness),
        )
    return defect


def green_identity_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return rank(Delta^t T - G M) when Green identity data are supplied."""
    if witness.tensor_pairing_matrix is None and witness.negative_product_matrix is None:
        return 0
    if witness.tensor_pairing_matrix is None or witness.negative_product_matrix is None:
        raise ValueError("tensor_pairing_matrix and negative_product_matrix must be supplied together")
    left = _matrix_product(
        _matrix_transpose(_fraction_matrix(witness.hall_coproduct_matrix)),
        _fraction_matrix(witness.tensor_pairing_matrix),
    )
    right = _matrix_product(
        _fraction_matrix(witness.source_pairing_matrix),
        _fraction_matrix(witness.negative_product_matrix),
    )
    return exact_matrix_rank(_matrix_difference(left, right))


def finite_coproduct_intertwining_gate(
    hall_coproduct_matrix: Matrix,
    borcherds_coproduct_matrix: Matrix,
    *,
    tensor_pairing_matrix: Optional[Matrix] = None,
    source_pairing_matrix: Optional[Matrix] = None,
    negative_product_matrix: Optional[Matrix] = None,
) -> FiniteCoproductIntertwiningGate:
    """Evaluate the finite coproduct square and Green adjunction exactly.

    The coproduct part checks rank(Delta_Hall - Delta_Borcherds).  The
    Green part checks rank(Delta_Hall^t T - G M) only when the tensor
    pairing, source pairing, and negative product matrices are all supplied.
    Missing Green data keeps the gate open instead of promoting a bare
    coproduct equality to a bialgebra comparison.
    """
    hall = _fraction_matrix(hall_coproduct_matrix)
    borcherds = _fraction_matrix(borcherds_coproduct_matrix)
    coproduct_difference = _matrix_difference(hall, borcherds)
    coproduct_defect_rank = exact_matrix_rank(coproduct_difference)

    supplied = (
        tensor_pairing_matrix is not None,
        source_pairing_matrix is not None,
        negative_product_matrix is not None,
    )
    if any(supplied) and not all(supplied):
        raise ValueError(
            "tensor_pairing_matrix, source_pairing_matrix, and "
            "negative_product_matrix must be supplied together"
        )

    if all(supplied):
        tensor_pairing = _fraction_matrix(tensor_pairing_matrix or ())
        source_pairing = _fraction_matrix(source_pairing_matrix or ())
        negative_product = _fraction_matrix(negative_product_matrix or ())
        green_left = _matrix_product(_matrix_transpose(hall), tensor_pairing)
        green_right = _matrix_product(source_pairing, negative_product)
        green_difference = _matrix_difference(green_left, green_right)
        green_defect_rank = exact_matrix_rank(green_difference)
        green_data_supplied = True
    else:
        green_left = ()
        green_right = ()
        green_difference = ()
        green_defect_rank = 0
        green_data_supplied = False

    coproduct_intertwines = coproduct_defect_rank == 0
    green_adjoint = green_data_supplied and green_defect_rank == 0
    closed = coproduct_intertwines and green_adjoint
    if not green_data_supplied:
        status = "FINITE_COPRODUCT_GREEN_DATA_MISSING"
    elif closed:
        status = "FINITE_COPRODUCT_INTERTWINING_GATE"
    else:
        status = "FINITE_COPRODUCT_INTERTWINING_DEFECT"
    return FiniteCoproductIntertwiningGate(
        coproduct_left=hall,
        coproduct_right=borcherds,
        coproduct_difference=coproduct_difference,
        green_left=green_left,
        green_right=green_right,
        green_difference=green_difference,
        coproduct_defect_rank=coproduct_defect_rank,
        green_defect_rank=green_defect_rank,
        green_data_supplied=green_data_supplied,
        coproduct_intertwines=coproduct_intertwines,
        green_adjoint=green_adjoint,
        closed=closed,
        status=status,
    )


def serre_inclusion_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return rank(R E) for supplied Serre rows R and Hall evaluation E."""
    if witness.serre_relation_matrix is None and witness.hall_bracket_evaluation_matrix is None:
        return 0
    if witness.serre_relation_matrix is None or witness.hall_bracket_evaluation_matrix is None:
        raise ValueError("serre_relation_matrix and hall_bracket_evaluation_matrix must be supplied together")
    return exact_matrix_rank(
        _matrix_product(
            _fraction_matrix(witness.serre_relation_matrix),
            _fraction_matrix(witness.hall_bracket_evaluation_matrix),
        )
    )


def pbw_hilbert_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return rank of the finite Hilbert-vector difference when supplied."""
    if witness.borcherds_hilbert_vector is None and witness.hall_hilbert_vector is None:
        return 0
    if witness.borcherds_hilbert_vector is None or witness.hall_hilbert_vector is None:
        raise ValueError("borcherds_hilbert_vector and hall_hilbert_vector must be supplied together")
    return _vector_difference_rank(
        witness.borcherds_hilbert_vector,
        witness.hall_hilbert_vector,
    )


def parity_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return rank(A Pi_source - Pi_target A) for finite parity signs."""
    if witness.source_parity_signs is None and witness.target_parity_signs is None:
        return 1
    if witness.source_parity_signs is None or witness.target_parity_signs is None:
        raise ValueError("source_parity_signs and target_parity_signs must be supplied together")
    source_signs = _fraction_vector(witness.source_parity_signs)
    target_signs = _fraction_vector(witness.target_parity_signs)
    if any(sign not in (Fraction(1), Fraction(-1)) for sign in source_signs + target_signs):
        raise ValueError("parity signs must be +1 or -1")
    comparison = resolved_comparison_matrices(witness)[0]
    if len(target_signs) != len(comparison):
        raise ValueError("target_parity_signs must have one entry for each comparison row")
    if comparison and len(source_signs) != _matrix_width(comparison):
        raise ValueError("source_parity_signs must have one entry for each comparison column")
    if not comparison and source_signs:
        raise ValueError("source_parity_signs require a nonempty comparison matrix")
    target_scaled = tuple(
        tuple(target_signs[row_index] * entry for entry in row)
        for row_index, row in enumerate(comparison)
    )
    source_scaled = tuple(
        tuple(entry * source_signs[column_index] for column_index, entry in enumerate(row))
        for row in comparison
    )
    return exact_matrix_rank(_matrix_difference(target_scaled, source_scaled))


def centrality_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return the rank of retained-root centrality equations when supplied."""
    if witness.centrality_matrix is None:
        return 0
    return exact_matrix_rank(witness.centrality_matrix)


def cartan_radical_defect_dimension(witness: FiniteMatrixDefectWitness) -> int:
    """Return the defect for Cartan components lying in the Borcherds radical."""
    if witness.cartan_component_basis is None and witness.cartan_radical_basis is None:
        return 0
    if witness.cartan_component_basis is None or witness.cartan_radical_basis is None:
        raise ValueError("cartan_component_basis and cartan_radical_basis must be supplied together")
    return subspace_containment_defect_dimension(
        witness.cartan_component_basis,
        witness.cartan_radical_basis,
    )


def associator_cocycle_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return the rank of finite pentagon-cocycle violations when supplied."""
    if witness.associator_cocycle_matrix is None:
        return 0
    hall_boundary = _matrix_vector_product(
        witness.associator_cocycle_matrix,
        witness.hall_associator,
    )
    borcherds_boundary = _matrix_vector_product(
        witness.associator_cocycle_matrix,
        witness.borcherds_associator,
    )
    return exact_matrix_rank((hall_boundary, borcherds_boundary))


def gauge_constraint_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return the defect for charge/parity admissibility of gauge rows."""
    if witness.gauge_constraint_matrix is None:
        return 0
    gauge_basis = _fraction_matrix(witness.gauge_coboundary_basis)
    constraint = _fraction_matrix(witness.gauge_constraint_matrix)
    if not gauge_basis or not constraint:
        return 0
    return exact_matrix_rank(_matrix_product(gauge_basis, _matrix_transpose(constraint)))


def gauge_cocycle_defect_rank(witness: FiniteMatrixDefectWitness) -> int:
    """Return the defect for gauge-coboundary rows being pentagon cocycles."""
    if witness.associator_cocycle_matrix is None:
        return 0
    gauge_basis = _fraction_matrix(witness.gauge_coboundary_basis)
    cocycle_matrix = _fraction_matrix(witness.associator_cocycle_matrix)
    if not gauge_basis or not cocycle_matrix:
        return 0
    return exact_matrix_rank(_matrix_product(cocycle_matrix, _matrix_transpose(gauge_basis)))


def validate_associator_complex_shapes(witness: FiniteMatrixDefectWitness) -> None:
    """Check that A-defect data live in one finite associator cochain space."""
    cochain_dim = len(_fraction_vector(witness.hall_associator))
    if len(_fraction_vector(witness.borcherds_associator)) != cochain_dim:
        raise ValueError("associator cochains must have the same length")
    gauge_basis = _fraction_matrix(witness.gauge_coboundary_basis)
    if gauge_basis and _matrix_width(gauge_basis) != cochain_dim:
        raise ValueError("gauge coboundary rows must have associator cochain width")
    if witness.associator_cocycle_matrix is not None:
        cocycle_matrix = _fraction_matrix(witness.associator_cocycle_matrix)
        if cocycle_matrix and _matrix_width(cocycle_matrix) != cochain_dim:
            raise ValueError("associator cocycle matrix must have associator cochain width")
    if witness.gauge_constraint_matrix is not None:
        constraint_matrix = _fraction_matrix(witness.gauge_constraint_matrix)
        if constraint_matrix and _matrix_width(constraint_matrix) != cochain_dim:
            raise ValueError("gauge constraint matrix must have associator cochain width")


def _optional_matrix_transition_defect(
    left: Optional[Matrix],
    right: Optional[Matrix],
) -> int:
    if left is None and right is None:
        return 0
    if left is None or right is None:
        present = _fraction_matrix(left or right or ())
        return max(1, exact_matrix_rank(present))
    return exact_matrix_rank(_matrix_difference(_fraction_matrix(left), _fraction_matrix(right)))


def _optional_vector_transition_defect(
    left: Optional[Vector],
    right: Optional[Vector],
) -> int:
    if left is None and right is None:
        return 0
    if left is None or right is None:
        present = _fraction_vector(left or right or ())
        return 1 if any(entry != 0 for entry in present) else 0
    return _vector_difference_rank(left, right)


def _optional_subspace_transition_defect(
    left: Optional[Matrix],
    right: Optional[Matrix],
) -> int:
    if left is None and right is None:
        return 0
    if left is None or right is None:
        present = row_space_basis(left or right or ())
        return len(present)
    return subspace_symmetric_defect_dimension(left, right)


def finite_matrix_defect_report(
    witness: FiniteMatrixDefectWitness,
) -> FiniteMatrixDefectReport:
    """Evaluate the finite matrix reductions for R, S, D, C, A, P exactly."""
    positive_kernel = right_kernel_basis(witness.positive_pairing_matrix)
    negative_dual_kernel = right_kernel_basis(
        _matrix_transpose(_fraction_matrix(witness.negative_pairing_matrix))
    )
    expected_radical = intersection_basis(positive_kernel, negative_dual_kernel)
    radical_kernel_defect = subspace_symmetric_defect_dimension(
        witness.radical_basis,
        expected_radical,
    )
    expected_right_radical = intersection_basis(
        right_kernel_basis(witness.negative_pairing_matrix),
        right_kernel_basis(_matrix_transpose(_fraction_matrix(witness.positive_pairing_matrix))),
    )
    right_radical_kernel_defect = subspace_symmetric_defect_dimension(
        right_radical_basis(witness),
        expected_right_radical,
    )
    quotient_kernel_defect = quotient_kernel_defect_dimension(witness)

    left_comparison, right_comparison = resolved_comparison_matrices(witness)
    pulled_back_pairing = pullback_bilinear_pairing_matrix(
        left_comparison,
        witness.target_pairing_matrix,
        right_comparison,
    )
    radical_isometry_defect = exact_matrix_rank(
        _matrix_difference(_fraction_matrix(witness.source_pairing_matrix), pulled_back_pairing)
    )
    serre_defect = subspace_symmetric_defect_dimension(
        witness.hall_serre_kernel_basis,
        witness.borcherds_serre_basis,
    )
    serre_inclusion_defect = serre_inclusion_defect_rank(witness)
    pbw_hilbert_defect = pbw_hilbert_defect_rank(witness)
    coproduct_defect = exact_matrix_rank(
        _matrix_difference(
            _fraction_matrix(witness.hall_coproduct_matrix),
            _fraction_matrix(witness.borcherds_coproduct_matrix),
        )
    )
    green_identity_defect = green_identity_defect_rank(witness)
    center_defect = subspace_symmetric_defect_dimension(
        witness.primitive_center_basis,
        witness.allowed_center_basis,
    )
    centrality_defect = centrality_defect_rank(witness)
    cartan_radical_defect = cartan_radical_defect_dimension(witness)
    validate_associator_complex_shapes(witness)
    associator_cocycle_defect = associator_cocycle_defect_rank(witness)
    gauge_cocycle_defect = gauge_cocycle_defect_rank(witness)
    gauge_constraint_defect = gauge_constraint_defect_rank(witness)
    associator_difference = tuple(
        left - right
        for left, right in zip(
            _fraction_vector(witness.hall_associator),
            _fraction_vector(witness.borcherds_associator),
        )
    )
    associator_defect = (
        0
        if vector_in_row_span(associator_difference, witness.gauge_coboundary_basis)
        else 1
    )
    parity_defect = parity_defect_rank(witness)
    defect_values = {
        "R": (
            radical_kernel_defect
            + right_radical_kernel_defect
            + quotient_kernel_defect
            + radical_isometry_defect
        ),
        "S": serre_defect + serre_inclusion_defect + pbw_hilbert_defect,
        "D": coproduct_defect + green_identity_defect,
        "C": center_defect + centrality_defect + cartan_radical_defect,
        "A": (
            associator_defect
            + associator_cocycle_defect
            + gauge_cocycle_defect
            + gauge_constraint_defect
        ),
        "P": parity_defect,
    }
    vanished = tuple(defect for defect, value in defect_values.items() if value == 0)
    remaining = tuple(defect for defect, value in defect_values.items() if value != 0)
    recognition_witnesses = RecognitionEnvelopeWitnesses(
        finite_compact_double=True,
        finite_borcherds_target=True,
        compact_source_packet=True,
        radical_isometry=defect_values["R"] == 0,
        serre_kernel_exact=defect_values["S"] == 0,
        green_adjoint_coproduct=defect_values["D"] == 0,
        primitive_center_reduction=defect_values["C"] == 0,
        associator_class_match=defect_values["A"] == 0,
        parity_fixture_match=defect_values["P"] == 0,
        transition_compatible=witness.transition_compatible,
    )
    return FiniteMatrixDefectReport(
        radical_kernel_defect=radical_kernel_defect,
        right_radical_kernel_defect=right_radical_kernel_defect,
        quotient_kernel_defect=quotient_kernel_defect,
        radical_isometry_defect=radical_isometry_defect,
        serre_defect=serre_defect,
        serre_inclusion_defect=serre_inclusion_defect,
        pbw_hilbert_defect=pbw_hilbert_defect,
        coproduct_defect=coproduct_defect,
        green_identity_defect=green_identity_defect,
        center_defect=center_defect,
        centrality_defect=centrality_defect,
        cartan_radical_defect=cartan_radical_defect,
        associator_cocycle_defect=associator_cocycle_defect,
        gauge_cocycle_defect=gauge_cocycle_defect,
        gauge_constraint_defect=gauge_constraint_defect,
        associator_defect=associator_defect,
        parity_defect=parity_defect,
        vanished_defects=vanished,
        remaining_defects=remaining,
        recognition_witnesses=recognition_witnesses,
    )


def finite_recognition_certificate_report(
    comparison_witnesses: FiniteComparisonMatrixPacketWitnesses,
    matrix_witness: FiniteMatrixDefectWitness,
) -> FiniteRecognitionCertificateReport:
    """Evaluate the finite recognition certificate without promoting partial data."""
    packet_report = evaluate_finite_comparison_matrix_packet(comparison_witnesses)
    shape_report = finite_comparison_shape_report(matrix_witness)
    remaining = []
    remaining.extend(f"packet:{name}" for name in packet_report.missing_witnesses)
    remaining.extend(f"shape:{name}" for name in shape_report.remaining_components)

    matrix_report: Optional[FiniteMatrixDefectReport] = None
    recognition_report: Optional[RecognitionEnvelopeReport] = None
    if packet_report.closed and shape_report.closed:
        matrix_report = finite_matrix_defect_report(matrix_witness)
        recognition_report = evaluate_recognition_envelope(
            matrix_report.recognition_witnesses
        )
        remaining.extend(f"defect:{name}" for name in matrix_report.remaining_defects)
        if not matrix_witness.transition_compatible:
            remaining.append("transition")

    closed = not remaining
    return FiniteRecognitionCertificateReport(
        packet_report=packet_report,
        shape_report=shape_report,
        matrix_report=matrix_report,
        recognition_report=recognition_report,
        remaining_conditions=tuple(remaining),
        closed=closed,
        status="FINITE_RECOGNITION_CERTIFICATE" if closed else "FINITE_RECOGNITION_CERTIFICATE_DEFECT",
    )


def _vector_difference_rank(left: Vector, right: Vector) -> int:
    left = _fraction_vector(left)
    right = _fraction_vector(right)
    if len(left) != len(right):
        raise ValueError("vectors must have the same length")
    return exact_matrix_rank((tuple(a - b for a, b in zip(left, right)),))


def finite_matrix_transition_report(
    witness: FiniteMatrixTransitionWitness,
) -> FiniteMatrixTransitionReport:
    """Check that restricted upper-height matrix data equal lower-height data."""
    restricted = witness.restricted_upper_witness
    lower = witness.lower_witness
    component_defects = {
        "radical_basis": subspace_symmetric_defect_dimension(
            restricted.radical_basis,
            lower.radical_basis,
        ),
        "positive_pairing_matrix": exact_matrix_rank(
            _matrix_difference(
                _fraction_matrix(restricted.positive_pairing_matrix),
                _fraction_matrix(lower.positive_pairing_matrix),
            )
        ),
        "negative_pairing_matrix": exact_matrix_rank(
            _matrix_difference(
                _fraction_matrix(restricted.negative_pairing_matrix),
                _fraction_matrix(lower.negative_pairing_matrix),
            )
        ),
        "source_pairing_matrix": exact_matrix_rank(
            _matrix_difference(
                _fraction_matrix(restricted.source_pairing_matrix),
                _fraction_matrix(lower.source_pairing_matrix),
            )
        ),
        "target_pairing_matrix": exact_matrix_rank(
            _matrix_difference(
                _fraction_matrix(restricted.target_pairing_matrix),
                _fraction_matrix(lower.target_pairing_matrix),
            )
        ),
        "comparison_matrix": exact_matrix_rank(
            _matrix_difference(
                resolved_comparison_matrices(restricted)[0],
                resolved_comparison_matrices(lower)[0],
            )
        ),
        "right_comparison_matrix": exact_matrix_rank(
            _matrix_difference(
                resolved_comparison_matrices(restricted)[1],
                resolved_comparison_matrices(lower)[1],
            )
        ),
        "hall_serre_kernel_basis": subspace_symmetric_defect_dimension(
            restricted.hall_serre_kernel_basis,
            lower.hall_serre_kernel_basis,
        ),
        "borcherds_serre_basis": subspace_symmetric_defect_dimension(
            restricted.borcherds_serre_basis,
            lower.borcherds_serre_basis,
        ),
        "serre_relation_matrix": _optional_matrix_transition_defect(
            restricted.serre_relation_matrix,
            lower.serre_relation_matrix,
        ),
        "hall_bracket_evaluation_matrix": _optional_matrix_transition_defect(
            restricted.hall_bracket_evaluation_matrix,
            lower.hall_bracket_evaluation_matrix,
        ),
        "borcherds_hilbert_vector": (
            _optional_vector_transition_defect(
                restricted.borcherds_hilbert_vector,
                lower.borcherds_hilbert_vector,
            )
        ),
        "hall_hilbert_vector": (
            _optional_vector_transition_defect(
                restricted.hall_hilbert_vector,
                lower.hall_hilbert_vector,
            )
        ),
        "hall_coproduct_matrix": exact_matrix_rank(
            _matrix_difference(
                _fraction_matrix(restricted.hall_coproduct_matrix),
                _fraction_matrix(lower.hall_coproduct_matrix),
            )
        ),
        "borcherds_coproduct_matrix": exact_matrix_rank(
            _matrix_difference(
                _fraction_matrix(restricted.borcherds_coproduct_matrix),
                _fraction_matrix(lower.borcherds_coproduct_matrix),
            )
        ),
        "tensor_pairing_matrix": (
            _optional_matrix_transition_defect(
                restricted.tensor_pairing_matrix,
                lower.tensor_pairing_matrix,
            )
        ),
        "negative_product_matrix": (
            _optional_matrix_transition_defect(
                restricted.negative_product_matrix,
                lower.negative_product_matrix,
            )
        ),
        "primitive_center_basis": subspace_symmetric_defect_dimension(
            restricted.primitive_center_basis,
            lower.primitive_center_basis,
        ),
        "allowed_center_basis": subspace_symmetric_defect_dimension(
            restricted.allowed_center_basis,
            lower.allowed_center_basis,
        ),
        "centrality_matrix": _optional_matrix_transition_defect(
            restricted.centrality_matrix,
            lower.centrality_matrix,
        ),
        "cartan_component_basis": _optional_subspace_transition_defect(
            restricted.cartan_component_basis,
            lower.cartan_component_basis,
        ),
        "cartan_radical_basis": _optional_subspace_transition_defect(
            restricted.cartan_radical_basis,
            lower.cartan_radical_basis,
        ),
        "hall_associator": _vector_difference_rank(
            restricted.hall_associator,
            lower.hall_associator,
        ),
        "borcherds_associator": _vector_difference_rank(
            restricted.borcherds_associator,
            lower.borcherds_associator,
        ),
        "gauge_coboundary_basis": subspace_symmetric_defect_dimension(
            restricted.gauge_coboundary_basis,
            lower.gauge_coboundary_basis,
        ),
        "associator_cocycle_matrix": _optional_matrix_transition_defect(
            restricted.associator_cocycle_matrix,
            lower.associator_cocycle_matrix,
        ),
        "gauge_constraint_matrix": _optional_matrix_transition_defect(
            restricted.gauge_constraint_matrix,
            lower.gauge_constraint_matrix,
        ),
        "source_parity_signs": _optional_vector_transition_defect(
            restricted.source_parity_signs,
            lower.source_parity_signs,
        ),
        "target_parity_signs": _optional_vector_transition_defect(
            restricted.target_parity_signs,
            lower.target_parity_signs,
        ),
    }
    remaining = tuple(
        component
        for component, defect in component_defects.items()
        if defect != 0
    )
    return FiniteMatrixTransitionReport(
        upper_height=witness.upper_height,
        lower_height=witness.lower_height,
        component_defects=component_defects,
        remaining_components=remaining,
        closed=not remaining,
    )


def heightwise_matrix_defect_report(
    witnesses_by_height: Iterable[HeightMatrixDefectWitness],
    transition_witnesses: Iterable[FiniteMatrixTransitionWitness] = (),
) -> HeightwiseMatrixDefectReport:
    """Evaluate exact finite matrix defects and scan them for the first H0."""
    ordered = tuple(sorted(witnesses_by_height, key=lambda item: item.height))
    matrix_pairs = tuple(
        (item.height, finite_matrix_defect_report(item.witness))
        for item in ordered
    )
    heights = {height for height, _ in matrix_pairs}
    transition_reports = tuple(
        finite_matrix_transition_report(transition)
        for transition in sorted(
            transition_witnesses,
            key=lambda item: (item.upper_height, item.lower_height),
        )
    )
    incompatible_transition_heights = set()
    for report in transition_reports:
        if report.upper_height not in heights or report.lower_height not in heights:
            raise ValueError("transition heights must occur among matrix witnesses")
        if report.upper_height <= report.lower_height:
            raise ValueError("transition must go from a larger height to a smaller height")
        if not report.closed:
            incompatible_transition_heights.add(report.upper_height)

    recognition_report = heightwise_recognition_report(
        HeightRecognitionWitness(
            height,
            replace(
                report.recognition_witnesses,
                transition_compatible=(
                    report.recognition_witnesses.transition_compatible
                    and height not in incompatible_transition_heights
                ),
            ),
        )
        for height, report in matrix_pairs
    )
    rows_by_height = {row.height: row for row in recognition_report.rows}
    matrix_rows = tuple(
        HeightMatrixDefectRow(
            height=height,
            matrix_report=report,
            recognition_row=rows_by_height[height],
        )
        for height, report in matrix_pairs
    )
    return HeightwiseMatrixDefectReport(
        matrix_rows=matrix_rows,
        recognition_report=recognition_report,
        transition_reports=transition_reports,
    )


def heightwise_recognition_certificate_report(
    witnesses_by_height: Iterable[HeightRecognitionCertificateWitness],
    transition_witnesses: Iterable[FiniteMatrixTransitionWitness] = (),
    *,
    defect_ideal_transitions_commute: bool = True,
    defect_ideal_derived_limit_vanishes: bool = True,
) -> HeightwiseRecognitionCertificateReport:
    """Evaluate certificates and the exact pro-envelope obstruction."""
    ordered = tuple(sorted(witnesses_by_height, key=lambda item: item.height))
    if not ordered:
        raise ValueError("at least one heightwise certificate witness is required")
    seen = set()
    certificates = []
    for item in ordered:
        if item.height <= 0:
            raise ValueError("finite heights must be positive")
        if item.height in seen:
            raise ValueError(f"duplicate finite height {item.height}")
        seen.add(item.height)
        certificates.append(
            (
                item.height,
                finite_recognition_certificate_report(
                    item.comparison_witnesses,
                    item.matrix_witness,
                ),
            )
        )

    transition_reports = tuple(
        finite_matrix_transition_report(transition)
        for transition in sorted(
            transition_witnesses,
            key=lambda item: (item.upper_height, item.lower_height),
        )
    )
    transition_conditions_by_height: Dict[int, Tuple[str, ...]] = {}
    for report in transition_reports:
        if report.upper_height not in seen or report.lower_height not in seen:
            raise ValueError("transition heights must occur among certificate witnesses")
        if report.upper_height <= report.lower_height:
            raise ValueError("transition must go from a larger height to a smaller height")
        if report.remaining_components:
            transition_conditions_by_height[report.upper_height] = (
                transition_conditions_by_height.get(report.upper_height, ())
                + tuple(f"transition:{name}" for name in report.remaining_components)
            )

    rows = []
    first_failure_height: Optional[int] = None
    first_failure_conditions: Tuple[str, ...] = ()
    for height, certificate in certificates:
        transition_conditions = transition_conditions_by_height.get(height, ())
        failure_conditions = certificate.remaining_conditions + transition_conditions
        closed = not failure_conditions
        rows.append(
            HeightRecognitionCertificateRow(
                height=height,
                certificate_report=certificate,
                transition_conditions=transition_conditions,
                failure_conditions=failure_conditions,
                closed=closed,
            )
        )
        if first_failure_height is None and failure_conditions:
            first_failure_height = height
            first_failure_conditions = failure_conditions

    pro_exactness_conditions = ()
    if not defect_ideal_transitions_commute:
        pro_exactness_conditions += ("defect_ideal_transition",)
    if not defect_ideal_derived_limit_vanishes:
        pro_exactness_conditions += ("R1lim_defect_ideal",)
    if first_failure_height is None and pro_exactness_conditions:
        first_failure_conditions = pro_exactness_conditions

    completed = first_failure_height is None and not pro_exactness_conditions
    return HeightwiseRecognitionCertificateReport(
        rows=tuple(rows),
        transition_reports=transition_reports,
        first_failure_height=first_failure_height,
        first_failure_conditions=first_failure_conditions,
        pro_exactness_conditions=pro_exactness_conditions,
        completed=completed,
        status=(
            "HEIGHTWISE_RECOGNITION_CERTIFICATE_COMPLETE"
            if completed
            else (
                "PRO_ENVELOPE_EXACTNESS_FAILURE"
                if first_failure_height is None
                else "FIRST_CERTIFICATE_FAILURE_AT_HEIGHT"
            )
        ),
    )


def source_gate_obstruction_taxonomy() -> SourceGateObstructionTaxonomy:
    """Return the compact, finite, and pro-recognition obstruction split."""
    compact_passage = (
        SourceGateObstructionClass(
            code="o_ML",
            tex=r"o_{\mathrm{ML}}",
            layer="compact_passage",
            meaning="Mittag-Leffler exactness for the finite Rees Hall inverse system",
            required_vanishing="o_ML = 0",
        ),
        SourceGateObstructionClass(
            code="o_real",
            tex=r"o_{\mathrm{real}}",
            layer="compact_passage",
            meaning="monoidal critical realisation of the finite Rees Hall layer",
            required_vanishing="o_real = 0",
        ),
        SourceGateObstructionClass(
            code="o_cpt",
            tex=r"o_{\mathrm{cpt}}",
            layer="compact_passage",
            meaning="compact-support and properness functoriality for Hall convolution",
            required_vanishing="o_cpt = 0",
        ),
    )
    double_data = (
        SourceGateObstructionClass(
            code="o_Delta",
            tex=r"o_\Delta",
            layer="double_data",
            meaning="continuous coproduct and completed double compatibility",
            required_vanishing="o_Delta = 0",
        ),
        SourceGateObstructionClass(
            code="o_pair",
            tex=r"o_{\mathrm{pair}}",
            layer="double_data",
            meaning="nondegenerate completed Hopf pairing with radical quotient",
            required_vanishing="o_pair = 0",
        ),
        SourceGateObstructionClass(
            code="o_cent",
            tex=r"o_{\mathrm{cent}}",
            layer="double_data",
            meaning="centre compatibility for Cartan radical and declared group-like parameters",
            required_vanishing="o_cent = 0",
        ),
    )
    finite_recognition = (
        SourceGateObstructionClass(
            code="R",
            tex=r"\mathcal R_H",
            layer="finite_recognition",
            meaning="radical-isometry defect",
            required_vanishing="R = 0",
        ),
        SourceGateObstructionClass(
            code="S",
            tex=r"\mathcal S_H",
            layer="finite_recognition",
            meaning="Serre/PBW kernel defect",
            required_vanishing="S = 0",
        ),
        SourceGateObstructionClass(
            code="D",
            tex=r"\mathcal D_H",
            layer="finite_recognition",
            meaning="coproduct/Green-adjunction defect",
            required_vanishing="D = 0",
        ),
        SourceGateObstructionClass(
            code="C",
            tex=r"\mathcal C_H",
            layer="finite_recognition",
            meaning="primitive-centre defect",
            required_vanishing="C = 0",
        ),
        SourceGateObstructionClass(
            code="A",
            tex=r"\mathcal A_H",
            layer="finite_recognition",
            meaning="associator/gauge cocycle, admissible-gauge, and class defect",
            required_vanishing="A = 0",
        ),
        SourceGateObstructionClass(
            code="P",
            tex=r"\mathcal P_H",
            layer="finite_recognition",
            meaning="parity-fixture defect",
            required_vanishing="P = 0",
        ),
    )
    pro_recognition = (
        SourceGateObstructionClass(
            code="Q_H_sep",
            tex=r"Q_H^{\mathrm{sep}}",
            layer="pro_recognition",
            meaning="separated pro-cone completion of the finite recognition quotients",
            required_vanishing="Q_H^sep = 0",
        ),
        SourceGateObstructionClass(
            code="L_H_ex",
            tex=r"L_H^{\mathrm{ex}}",
            layer="pro_recognition",
            meaning="transition-compatible exact inverse limit of the finite defect ideals",
            required_vanishing="L_H^ex = 0",
        ),
        SourceGateObstructionClass(
            code="H_H_HB",
            tex=r"H_H^{\mathrm{HB}}",
            layer="pro_recognition",
            meaning="heightwise Heegner--Borcherds coefficient comparison",
            required_vanishing="H_H^HB = 0",
        ),
    )
    summary = (
        "compact Hall promotion first requires compact-passage and double-data "
        "obstruction vanishings; finite recognition then requires the six "
        "finite defects R, S, D, C, A, P to vanish heightwise; pro-recognition "
        "then requires separated completion, exact defect-ideal limits, and "
        "Heegner--Borcherds coefficient comparison"
    )
    return SourceGateObstructionTaxonomy(
        compact_passage=compact_passage,
        double_data=double_data,
        finite_recognition=finite_recognition,
        pro_recognition=pro_recognition,
        summary=summary,
    )


COMPACT_DOUBLE_GATE_WITNESSES: Tuple[Tuple[str, str], ...] = (
    ("compact_ml_exactness", "o_ML = 0"),
    ("compact_critical_realization", "o_real = 0"),
    ("compact_support_properness", "o_cpt = 0"),
    ("double_coproduct", "o_Delta = 0"),
    ("double_pairing", "o_pair = 0"),
    ("double_center", "o_cent = 0"),
)


def evaluate_source_compact_double_gate(
    witnesses: SourceCompactDoubleGateWitnesses,
) -> SourceCompactDoubleGateReport:
    """Evaluate compact-passage and double-data gates."""
    missing = tuple(
        field
        for field, _defect in COMPACT_DOUBLE_GATE_WITNESSES
        if not getattr(witnesses, field)
    )
    remaining = tuple(
        defect
        for field, defect in COMPACT_DOUBLE_GATE_WITNESSES
        if not getattr(witnesses, field)
    )
    closed = not missing
    return SourceCompactDoubleGateReport(
        closed=closed,
        missing_witnesses=missing,
        remaining_defects=remaining,
        status=(
            "SOURCE_COMPACT_DOUBLE_GATES_CLOSED"
            if closed
            else "SOURCE_COMPACT_DOUBLE_GATES_OPEN"
        ),
    )


PRO_RECOGNITION_GATE_WITNESSES: Tuple[Tuple[str, str], ...] = (
    ("separated_completion", "Q_H^sep = 0"),
    ("defect_ideal_exactness", "L_H^ex = 0"),
    ("heegner_borcherds_coefficient_comparison", "H_H^HB = 0"),
)


def evaluate_source_pro_recognition_gate(
    witnesses: SourceProRecognitionGateWitnesses,
) -> SourceProRecognitionGateReport:
    """Evaluate the source-side pro-recognition gates Q_H^sep, L_H^ex, H_H^HB."""
    missing = tuple(
        field
        for field, _defect in PRO_RECOGNITION_GATE_WITNESSES
        if not getattr(witnesses, field)
    )
    remaining = tuple(
        defect
        for field, defect in PRO_RECOGNITION_GATE_WITNESSES
        if not getattr(witnesses, field)
    )
    closed = not missing
    return SourceProRecognitionGateReport(
        closed=closed,
        missing_witnesses=missing,
        remaining_defects=remaining,
        status=(
            "SOURCE_PRO_RECOGNITION_GATES_CLOSED"
            if closed
            else "SOURCE_PRO_RECOGNITION_GATES_OPEN"
        ),
    )


def finite_source_pro_recognition_matrix_gate(
    *,
    completion_transition_matrix: Iterable[Iterable[Any]],
    separation_defect_matrix: Iterable[Iterable[Any]],
    defect_ideal_transition_matrix: Iterable[Iterable[Any]],
    defect_ideal_landing_defect_matrix: Iterable[Iterable[Any]],
    heegner_coefficient_matrix: Iterable[Iterable[Any]],
    borcherds_coefficient_matrix: Iterable[Iterable[Any]],
) -> FiniteSourceProRecognitionMatrixGate:
    r"""Evaluate the finite matrix form of the source pro-recognition gates.

    \(Q_H^{\mathrm{sep}}\) is represented by surjectivity of the
    finite completion transition together with a supplied separation
    defect. \(L_H^{\mathrm{ex}}\) is represented by surjectivity of the
    finite defect-ideal transition together with a supplied landing
    defect. \(H_H^{\mathrm{HB}}\) is represented by equality of the
    finite Heegner and Borcherds coefficient matrices.
    """
    completion_transition = _fraction_matrix(completion_transition_matrix)
    separation_defect = _fraction_matrix(separation_defect_matrix)
    defect_ideal_transition = _fraction_matrix(defect_ideal_transition_matrix)
    defect_ideal_landing_defect = _fraction_matrix(defect_ideal_landing_defect_matrix)
    heegner_coefficients = _fraction_matrix(heegner_coefficient_matrix)
    borcherds_coefficients = _fraction_matrix(borcherds_coefficient_matrix)

    lower_completion_dimension = len(completion_transition)
    completion_transition_rank = exact_matrix_rank(completion_transition)
    separation_defect_rank = exact_matrix_rank(separation_defect)
    lower_defect_ideal_dimension = len(defect_ideal_transition)
    defect_ideal_transition_rank = exact_matrix_rank(defect_ideal_transition)
    defect_ideal_landing_defect_rank = exact_matrix_rank(defect_ideal_landing_defect)
    coefficient_defect = _matrix_difference(heegner_coefficients, borcherds_coefficients)
    coefficient_defect_rank = exact_matrix_rank(coefficient_defect)

    separated_completion = (
        completion_transition_rank == lower_completion_dimension
        and separation_defect_rank == 0
    )
    defect_ideal_exact = (
        defect_ideal_transition_rank == lower_defect_ideal_dimension
        and defect_ideal_landing_defect_rank == 0
    )
    heegner_borcherds_coefficients_match = coefficient_defect_rank == 0
    closed = (
        separated_completion
        and defect_ideal_exact
        and heegner_borcherds_coefficients_match
    )
    return FiniteSourceProRecognitionMatrixGate(
        lower_completion_dimension=lower_completion_dimension,
        completion_transition_rank=completion_transition_rank,
        separation_defect_matrix=separation_defect,
        separation_defect_rank=separation_defect_rank,
        lower_defect_ideal_dimension=lower_defect_ideal_dimension,
        defect_ideal_transition_rank=defect_ideal_transition_rank,
        defect_ideal_landing_defect_matrix=defect_ideal_landing_defect,
        defect_ideal_landing_defect_rank=defect_ideal_landing_defect_rank,
        coefficient_defect_matrix=coefficient_defect,
        coefficient_defect_rank=coefficient_defect_rank,
        separated_completion=separated_completion,
        defect_ideal_exact=defect_ideal_exact,
        heegner_borcherds_coefficients_match=heegner_borcherds_coefficients_match,
        closed=closed,
        status=(
            "FINITE_SOURCE_PRO_RECOGNITION_MATRIX_GATE"
            if closed
            else "FINITE_SOURCE_PRO_RECOGNITION_MATRIX_DEFECT"
        ),
    )


def source_matrix_forces_faithfulness(witnesses: RecognitionEnvelopeWitnesses) -> bool:
    """Return True exactly when finite source matrices force J_H cap D_H^X = 0."""
    finite_objects = witnesses.finite_compact_double and witnesses.finite_borcherds_target
    return (
        finite_objects
        and witnesses.compact_source_packet
        and all(finite_defect_vanishings(witnesses).values())
    )


def evaluate_recognition_envelope(
    witnesses: RecognitionEnvelopeWitnesses,
) -> RecognitionEnvelopeReport:
    """Evaluate finite envelope construction versus faithful recognition."""
    finite_objects = witnesses.finite_compact_double and witnesses.finite_borcherds_target
    source_packet = witnesses.finite_compact_double and witnesses.compact_source_packet
    envelope_constructed = finite_objects and witnesses.compact_source_packet
    vanishings = finite_defect_vanishings(witnesses)
    vanished = tuple(defect for defect, ok in vanishings.items() if ok)
    remaining = tuple(defect for defect, ok in vanishings.items() if not ok)
    source_faithful = source_matrix_forces_faithfulness(witnesses)
    finite_recognized = source_faithful
    completed_envelope = envelope_constructed and witnesses.transition_compatible
    completed_source_faithful = source_faithful and witnesses.transition_compatible
    completed_recognized = completed_source_faithful
    if completed_recognized:
        status = "COMPLETED_UNQUOTIENTED_RECOGNITION"
    elif finite_recognized:
        status = "FINITE_UNQUOTIENTED_RECOGNITION"
    elif completed_envelope:
        status = "COMPLETED_RECOGNITION_ENVELOPE"
    elif envelope_constructed:
        status = "FINITE_RECOGNITION_ENVELOPE"
    elif finite_objects:
        status = "MISSING_SOURCE_PACKET"
    else:
        status = "MISSING_FINITE_OBJECTS"
    return RecognitionEnvelopeReport(
        envelope_constructed=envelope_constructed,
        source_packet_constructed=source_packet,
        source_faithfulness_forced=source_faithful,
        finite_unquotiented_recognized=finite_recognized,
        completed_envelope_constructed=completed_envelope,
        completed_source_faithfulness=completed_source_faithful,
        completed_unquotiented_recognized=completed_recognized,
        vanished_defects=vanished,
        remaining_defects=remaining,
        status=status,
    )


def recognition_envelope_missing_witnesses(
    witnesses: RecognitionEnvelopeWitnesses,
    report: Optional[RecognitionEnvelopeReport] = None,
) -> Tuple[str, ...]:
    """Return structural and finite-defect witnesses missing from the envelope."""
    report = report or evaluate_recognition_envelope(witnesses)
    missing = []
    if not witnesses.finite_compact_double:
        missing.append("finite_compact_double")
    if not witnesses.finite_borcherds_target:
        missing.append("finite_borcherds_target")
    if not witnesses.compact_source_packet:
        missing.append("compact_source_packet")
    missing.extend(report.remaining_defects)
    if not witnesses.transition_compatible:
        missing.append("transition_compatible")
    return tuple(dict.fromkeys(missing))


def height_failure_modes(
    witnesses: RecognitionEnvelopeWitnesses,
    report: RecognitionEnvelopeReport,
) -> Tuple[str, ...]:
    """Return theorem-level obstruction labels for one finite height."""
    structural_modes = []
    if not witnesses.finite_compact_double:
        structural_modes.append("finite_compact_double")
    if not witnesses.finite_borcherds_target:
        structural_modes.append("finite_borcherds_target")
    if not witnesses.compact_source_packet:
        structural_modes.append("compact_source_packet")
    if structural_modes:
        return tuple(dict.fromkeys(structural_modes))

    modes = []
    modes.extend(report.remaining_defects)
    if not witnesses.transition_compatible:
        modes.append("transition")
    return tuple(dict.fromkeys(modes))


def heightwise_recognition_report(
    witnesses_by_height: Iterable[HeightRecognitionWitness],
) -> HeightwiseRecognitionReport:
    """Evaluate finite recognition heightwise and expose the first failure H0."""
    ordered = tuple(sorted(witnesses_by_height, key=lambda item: item.height))
    if not ordered:
        raise ValueError("at least one finite-height witness is required")

    seen = set()
    rows = []
    first_failure_height: Optional[int] = None
    first_failure_modes: Tuple[str, ...] = ()
    for item in ordered:
        if item.height <= 0:
            raise ValueError("finite heights must be positive")
        if item.height in seen:
            raise ValueError(f"duplicate finite height {item.height}")
        seen.add(item.height)

        report = evaluate_recognition_envelope(item.witnesses)
        failure_modes = height_failure_modes(item.witnesses, report)
        closed = failure_modes == ()
        rows.append(
            HeightRecognitionRow(
                height=item.height,
                report=report,
                failure_modes=failure_modes,
                closed=closed,
            )
        )
        if first_failure_height is None and failure_modes:
            first_failure_height = item.height
            first_failure_modes = failure_modes

    completed = first_failure_height is None
    status = (
        "HEIGHTWISE_RECOGNITION_COMPLETE"
        if completed
        else "FIRST_FAILURE_AT_HEIGHT"
    )
    return HeightwiseRecognitionReport(
        rows=tuple(rows),
        first_failure_height=first_failure_height,
        first_failure_modes=first_failure_modes,
        completed=completed,
        status=status,
    )


def source_gate_obligation_matrix(
    gate_witnesses: Optional[HallBorcherdsWitnesses] = None,
    envelope_witnesses: Optional[RecognitionEnvelopeWitnesses] = None,
) -> SourceGateObligationMatrix:
    """Return the source-side Hall/Borcherds theorem boundary as an obligation matrix."""
    gate_report = evaluate_gate(gate_witnesses or HallBorcherdsWitnesses())
    envelope_witnesses = envelope_witnesses or RecognitionEnvelopeWitnesses()
    envelope_report = evaluate_recognition_envelope(
        envelope_witnesses
    )
    gate = SourceGateObligationEntry(
        witness=gate_report,
        missing=tuple(gate_report.missing_witnesses),
        target="Hall-Drinfeld double / BKM denominator gate",
        status="closed" if gate_report.closed else "open",
    )
    envelope = SourceGateObligationEntry(
        witness=envelope_report,
        missing=recognition_envelope_missing_witnesses(envelope_witnesses, envelope_report),
        target="finite recognition envelope / pro-completion",
        status=(
            "completed"
            if envelope_report.completed_unquotiented_recognized
            else ("finite" if envelope_report.finite_unquotiented_recognized else "open")
        ),
    )
    summary = (
        "source gate and recognition envelope are explicit theorem obligations: "
        "the gate closes only after the Hall/Borcherds witnesses are supplied, "
        "and the envelope closes only after the finite defects and transition compatibility vanish"
    )
    return SourceGateObligationMatrix(gate=gate, envelope=envelope, summary=summary)


def source_gate_task_map() -> SourceGateTaskMap:
    """Return the source-side task map for the Hall/Borcherds gate."""
    gate_tasks = SourceGateTaskEntry(
        node="source_hall_borcherds_gate",
        tasks=(
            "construct the oriented critical CoHA with negative half, Cartan, Hopf pairing, and coproduct",
            "prove source-recognition completeness from the Hall/Drinfeld data",
            "show compatibility with the Hall double, the denominator normalization, and the pro-cone topology",
        ),
    )
    envelope_tasks = SourceGateTaskEntry(
        node="source_recognition_envelope",
        tasks=(
            "construct the finite recognition envelope from compact source packets and finite targets",
            "prove the six defect vanishings R, S, D, C, A, P imply faithful recognition",
            "show the completed envelope respects transition compatibility and inverse limits",
        ),
    )
    summary = (
        "the source task map separates the Hall/Borcherds gate from the recognition envelope and "
        "lists the exact constructions and compatibilities still missing on each side"
    )
    return SourceGateTaskMap(entries=(gate_tasks, envelope_tasks), summary=summary)


def source_gate_boundary_report(
    pro_recognition_witnesses: Optional[SourceProRecognitionGateWitnesses] = None,
    compact_double_witnesses: Optional[SourceCompactDoubleGateWitnesses] = None,
    gate_witnesses: Optional[HallBorcherdsWitnesses] = None,
    envelope_witnesses: Optional[RecognitionEnvelopeWitnesses] = None,
) -> SourceGateBoundaryReport:
    """Derive the source-side theorem boundary from the gate and task map."""
    obligation_matrix = source_gate_obligation_matrix(
        gate_witnesses=gate_witnesses,
        envelope_witnesses=envelope_witnesses,
    )
    task_map = source_gate_task_map()
    obstruction_taxonomy = source_gate_obstruction_taxonomy()
    compact_double_report = evaluate_source_compact_double_gate(
        compact_double_witnesses or SourceCompactDoubleGateWitnesses()
    )
    pro_recognition_report = evaluate_source_pro_recognition_gate(
        pro_recognition_witnesses or SourceProRecognitionGateWitnesses()
    )
    required_conditions = tuple(
        dict.fromkeys(
            tuple(obligation_matrix.gate.missing)
            + tuple(obligation_matrix.envelope.missing)
            + tuple(compact_double_report.remaining_defects)
            + tuple(pro_recognition_report.remaining_defects)
            + (
                tuple(task_map.tasks["source_hall_borcherds_gate"].tasks)
                if obligation_matrix.gate.status != "closed"
                else ()
            )
            + (
                tuple(task_map.tasks["source_recognition_envelope"].tasks)
                if obligation_matrix.envelope.status != "completed"
                else ()
            )
        )
    )
    closed = (
        not required_conditions
        and obligation_matrix.gate.status == "closed"
        and obligation_matrix.envelope.status == "completed"
        and compact_double_report.closed
        and pro_recognition_report.closed
    )
    summary = (
        "the source boundary is the union of the Hall/Borcherds gate obligations, "
        "the recognition-envelope defects, the pro-recognition gates, and the source task map"
    )
    return SourceGateBoundaryReport(
        obligation_matrix=obligation_matrix,
        task_map=task_map,
        obstruction_taxonomy=obstruction_taxonomy,
        compact_double_report=compact_double_report,
        pro_recognition_report=pro_recognition_report,
        required_conditions=required_conditions,
        closed=closed,
        summary=summary,
    )


def primitive_discriminant(n: int, ell: int, m: int) -> int:
    """Return D = 4 n m - ell^2 for a rank-three BKM charge."""
    return 4 * n * m - ell * ell


def primitive_root_key(n: int, ell: int, m: int) -> int:
    """Return the Jacobi-coefficient key for a primitive BKM root.

    The value is only a key.  A coefficient oracle for phi_{0,1} or its
    CHL/twined variant must still be supplied before a multiplicity is
    claimed.
    """
    if gcd(gcd(abs(n), abs(ell)), abs(m)) != 1:
        raise ValueError("root is imprimitive; use a divisor-sum lane")
    return primitive_discriminant(n, ell, m)


PHI01_EZ_COEFFICIENTS: Dict[int, int] = {
    -1: 1,
    0: 10,
    3: -64,
    4: 108,
    7: -513,
    8: 808,
    11: -2752,
    12: 4016,
    15: -11775,
}


@dataclass(frozen=True)
class ImprimitiveBorcherdsPTGate:
    """Lane separation for imprimitive BKM exponents and PT multiple covers."""

    charge: Tuple[int, int, int]
    gcd: int
    discriminant: int
    borcherds_product_exponent: int
    primitive_subcharge: Tuple[int, int, int]
    primitive_subcharge_discriminant: int
    primitive_subcharge_exponent: int
    mobius_subtraction_applies_to_bkm_exponent: bool
    pt_multiple_cover_status: str
    dt_imprimitive_status: str
    required_inputs: Tuple[str, ...]


def imprimitive_borcherds_pt_gate(
    n: int = 2,
    ell: int = 2,
    m: int = 2,
    coefficients: Dict[int, int] = PHI01_EZ_COEFFICIENTS,
) -> ImprimitiveBorcherdsPTGate:
    """Separate the BKM product exponent from stable-pair multiple covers.

    The Borcherds product reads the exponent at the charge discriminant,
    even for an imprimitive charge.  Multiple-cover Möbius extraction is a
    reduced stable-pair operation and does not subtract the primitive
    subcharge exponent from the BKM product exponent.
    """
    g = gcd(gcd(abs(n), abs(ell)), abs(m))
    if g <= 1:
        raise ValueError("charge is primitive; use primitive_root_key")
    discriminant = primitive_discriminant(n, ell, m)
    primitive = (n // g, ell // g, m // g)
    primitive_discriminant_key = primitive_discriminant(*primitive)
    return ImprimitiveBorcherdsPTGate(
        charge=(n, ell, m),
        gcd=g,
        discriminant=discriminant,
        borcherds_product_exponent=coefficients[discriminant],
        primitive_subcharge=primitive,
        primitive_subcharge_discriminant=primitive_discriminant_key,
        primitive_subcharge_exponent=coefficients[primitive_discriminant_key],
        mobius_subtraction_applies_to_bkm_exponent=False,
        pt_multiple_cover_status="CONDITIONAL_ON_OP_MULTIPLE_COVER_CONJECTURE",
        dt_imprimitive_status="CONDITIONAL_ON_IMPRIMITIVE_MOTIVIC_PT_DT_WALL_CROSSING",
        required_inputs=(
            "Oberdieck-Pandharipande all-class reduced stable-pair multiple-cover rule",
            "Behrend-weighted imprimitive PT/DT wall-crossing",
            "orientation and sign convention for imprimitive DT classes",
        ),
    )


@dataclass(frozen=True)
class KTheoreticN46ClosureGate:
    """Status gate for the N=4,6 K-theoretic twisted-sector closure."""

    orders: Tuple[int, ...]
    untwined_refined_source: str
    status_by_order: Dict[int, str]
    euler_specialization_target: str
    euler_specialization_is_theorem: bool
    false_source_attribution_rejected: bool
    missing_inputs: Tuple[str, ...]


@dataclass(frozen=True)
class K3ERefinedKTheoryGate:
    """Boundary between refined PT, K-theoretic DT, and AS-index readings."""

    object: str
    numerical_primitive_scalar_status: str
    all_class_scalar_status: str
    refined_pt_status: str
    ideal_sheaf_kdt_status: str
    motivic_hodge_tate_status: str
    as_index_status: str
    false_arxiv_2405_03418_rejected: bool
    torus_localization_available: bool
    missing_inputs: Tuple[str, ...]


def ktheoretic_n46_closure_gate() -> KTheoreticN46ClosureGate:
    """Separate untwined refined K3 x E theory from N=4,6 orbifold closure."""
    status_by_order = {
        4: "CONJECTURAL_NEEDS_EQUIVARIANT_K_THEORETIC_ORBIFOLD_GATE",
        6: "CONJECTURAL_NEEDS_EQUIVARIANT_K_THEORETIC_ORBIFOLD_GATE",
    }
    return KTheoreticN46ClosureGate(
        orders=(4, 6),
        untwined_refined_source=(
            "untwined K3 x E reduced refined PT/Jacobi comparison target"
        ),
        status_by_order=status_by_order,
        euler_specialization_target="Conjecture thm:k3e-orbifold-DT-N46",
        euler_specialization_is_theorem=False,
        false_source_attribution_rejected=True,
        missing_inputs=(
            "g_N-linearized reduced obstruction theory on [K3 x E / Z_N]",
            "twisted-sector K-theoretic correction from CHPV twining data",
            "compatibility with reduced E-fibred multiplicative structure",
            "Euler-specialization compatibility with the N=4,6 orbifold DT conjecture",
        ),
    )


def k3e_refined_ktheory_gate() -> K3ERefinedKTheoryGate:
    """Return the K3 x E refined K-theory theorem-status boundary."""
    return K3ERefinedKTheoryGate(
        object="K3 x E refined reduced PT / K-theoretic DT / AS-index boundary",
        numerical_primitive_scalar_status="PROVED_BY_OBERDIECK_PIXTON_2018_AND_REDUCED_PT_DT",
        all_class_scalar_status="CONJECTURAL_IN_OBERDIECK_PANDHARIPANDE_ALL_CLASS_FORM",
        refined_pt_status="CONDITIONAL_ON_REFINED_REDUCED_PT_JACOBI_COMPARISON",
        ideal_sheaf_kdt_status="CONDITIONAL_ON_REDUCED_K_THEORETIC_PT_DT_AND_ORIENTATION",
        motivic_hodge_tate_status="CONDITIONAL_ON_COMPACT_K3XE_MOTIVIC_IGUSA_LIFT",
        as_index_status="CONDITIONAL_ON_TWISTED_VIRTUAL_DIRAC_INDEX_CONSTRUCTION",
        false_arxiv_2405_03418_rejected=True,
        torus_localization_available=False,
        missing_inputs=(
            "compact K3 x E orientation data for the reduced ideal-sheaf K-theory class",
            "K-theoretic PT/DT comparison for the reduced compact non-toric theory",
            "motivic Igusa lift in K_0(MMHS) with Hodge-Tate character",
            "Dirac operator construction on the twisted derived DT moduli stack",
            "proof that the AS index series equals the reduced DT/PT partition function",
        ),
    )


ANTI_SHORTCUTS: Dict[str, str] = {
    "coha_c3_is_w": "CoHA(C^3) is Y^+; W_{1+infty} appears only after double/center/evaluation data.",
    "bkm_is_yangian": "The K3 BKM object is the Hall-Drinfeld double, not a strict Drinfeld Yangian.",
    "phi10_weight_is_kappa_BKM": "Phi_10 has weight 10; primitive kappa_BKM(Delta_5) is 5.",
    "additive_kappa_BKM": "kappa_BKM is c_N(0)/2, not kappa_ch plus a fibre Euler term.",
    "six_phi_applications": "The six K3 x E routes are distinct constructions, not six Phi applications.",
}


def shortcut_allowed(shortcut: str) -> bool:
    """Return whether a named shortcut is allowed in the bridge package."""
    if shortcut not in ANTI_SHORTCUTS:
        raise KeyError(f"unknown shortcut: {shortcut}")
    return False


def additive_claim_status(
    *,
    kappa_ch_Heis: Fraction,
    kappa_fiber: Fraction,
    kappa_BKM: Fraction,
    universal_claim: bool,
) -> Dict[str, object]:
    """Classify the common additive kappa_BKM claim.

    At N = 1 the Heisenberg-fibre numbers may match, but the match is
    not a proof of the BKM denominator identity and cannot be promoted
    to a universal formula.
    """
    numeric_match = kappa_ch_Heis + kappa_fiber == kappa_BKM
    return {
        "numeric_match": numeric_match,
        "accepted_as_bridge_proof": False,
        "universal_claim": universal_claim,
        "reason": (
            "numeric coincidence only"
            if numeric_match
            else "wrong invariant lane"
        ),
    }


def all_shortcuts_rejected(shortcuts: Iterable[str] = ANTI_SHORTCUTS.keys()) -> bool:
    """Return True when every known bridge shortcut is rejected."""
    return all(not shortcut_allowed(shortcut) for shortcut in shortcuts)
