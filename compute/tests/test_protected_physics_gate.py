"""Tests for the protected physics gate."""

import pytest

from compute.lib.protected_physics_gate import (
    EpistemicStatus,
    EvidenceKind,
    ProtectedClaimLevel,
    ProtectedEvidence,
    ProtectedPhysicsShortcutError,
    protected_bkm_functor_package,
    protected_trace_package,
    validate_promotion,
    witness_only_package,
)


def test_witness_only_package_cannot_promote_a_protected_index():
    evidence = ProtectedEvidence(
        EvidenceKind.PROTECTED_INDEX,
        EpistemicStatus.COMPUTED,
        "DVV protected index",
    )

    with pytest.raises(ProtectedPhysicsShortcutError) as err:
        validate_promotion(
            evidence,
            ProtectedClaimLevel.PROTECTED_INDEX,
            witness_only_package(),
        )

    assert "orientation line" in str(err.value)


def test_complete_trace_package_promotes_index_to_chiral_trace():
    evidence = ProtectedEvidence(
        EvidenceKind.PROTECTED_INDEX,
        EpistemicStatus.THEOREM,
        "oriented BPS index",
    )
    claim = validate_promotion(
        evidence,
        ProtectedClaimLevel.CHAMBER_INDEPENDENT_TRACE,
        protected_trace_package(),
    )

    assert claim.level == ProtectedClaimLevel.CHAMBER_INDEPENDENT_TRACE
    assert tuple(gate.key for gate in claim.gates) == (
        "protected_sector_projection",
        "orientation_line_trivialization",
        "charge_lattice_isometry",
        "index_character_map",
        "wall_crossing_coherence",
    )


def test_heuristic_holography_stays_witness_only():
    evidence = ProtectedEvidence(
        EvidenceKind.HOLOGRAPHIC_TRACE,
        EpistemicStatus.HEURISTIC,
        "AdS/CFT trace comparison",
    )

    with pytest.raises(ProtectedPhysicsShortcutError) as err:
        validate_promotion(
            evidence,
            ProtectedClaimLevel.CHIRAL_CHARACTER,
            protected_trace_package(),
        )

    assert "remains witness-only" in str(err.value)


def test_physics_numbers_do_not_prove_algebra_functors():
    evidence = ProtectedEvidence(
        EvidenceKind.BLACK_HOLE_COUNT,
        EpistemicStatus.THEOREM,
        "Rademacher/Sen degeneracy formula",
    )

    with pytest.raises(ProtectedPhysicsShortcutError) as err:
        validate_promotion(
            evidence,
            ProtectedClaimLevel.HALL_TO_CHIRAL_FUNCTOR,
            protected_bkm_functor_package(),
        )

    assert "not an algebra functor" in str(err.value)


def test_bps_hilbert_space_must_first_be_indexed():
    evidence = ProtectedEvidence(
        EvidenceKind.BPS_HILBERT_SPACE,
        EpistemicStatus.COMPUTED,
        "full BPS Hilbert space",
    )

    with pytest.raises(ProtectedPhysicsShortcutError) as err:
        validate_promotion(
            evidence,
            ProtectedClaimLevel.CHIRAL_CHARACTER,
            protected_bkm_functor_package(),
        )

    assert "protected index" in str(err.value)


def test_hall_category_evidence_can_reach_bkm_package_with_all_gates():
    evidence = ProtectedEvidence(
        EvidenceKind.BPS_CATEGORY_WITH_HALL,
        EpistemicStatus.THEOREM,
        "oriented DT Hall category",
    )
    claim = validate_promotion(
        evidence,
        ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE,
        protected_bkm_functor_package(),
    )

    assert claim.level == ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE
    assert claim.gates[-2].key == "drinfeld_double_bkm_map"
    assert claim.gates[-1].key == "borcherds_denominator_normalization"


def test_conjectural_hall_category_keeps_its_status_when_typed():
    evidence = ProtectedEvidence(
        EvidenceKind.BPS_CATEGORY_WITH_HALL,
        EpistemicStatus.CONJECTURAL,
        "conjectural protected Hall category",
    )
    claim = validate_promotion(
        evidence,
        ProtectedClaimLevel.HALL_TO_CHIRAL_FUNCTOR,
        protected_bkm_functor_package(),
    )

    assert claim.evidence.status == EpistemicStatus.CONJECTURAL
    assert claim.level == ProtectedClaimLevel.HALL_TO_CHIRAL_FUNCTOR


def test_bkm_package_missing_double_map_is_rejected():
    evidence = ProtectedEvidence(
        EvidenceKind.BPS_CATEGORY_WITH_HALL,
        EpistemicStatus.THEOREM,
        "oriented DT Hall category",
    )
    package = protected_trace_package().with_gates("hall_product_ope_functor")

    with pytest.raises(ProtectedPhysicsShortcutError) as err:
        validate_promotion(
            evidence,
            ProtectedClaimLevel.BKM_CHIRAL_TRACE_PACKAGE,
            package,
        )

    assert "positive-half Hall data" in str(err.value)
    assert "Borcherds weight" in str(err.value)
