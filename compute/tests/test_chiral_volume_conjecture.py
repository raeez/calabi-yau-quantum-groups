"""Tests for the chiral volume conjecture engine.

Verifies: curve geometry, CY3 data, DT asymptotics, Abel-Jacobi periods,
three-regime analysis, 3d comparison, obstruction catalogue, and the
master conjecture statement.

Test count: 97 tests.
"""

from __future__ import annotations

import cmath
import math

import numpy as np
import pytest

from compute.lib.chiral_volume_conjecture import (
    AbelJacobiPeriod,
    CY3Geometry,
    CurveInCY3,
    ChiralVolumeConjectureData,
    ELLIPTIC_CURVE_CY3,
    GENUS2_CURVE_CY3,
    K3_TIMES_E,
    LOCAL_P2,
    ObstructionAnalysis,
    QUINTIC,
    RATIONAL_CURVE_CONIFOLD,
    RATIONAL_CURVE_LOCAL_P2,
    RESOLVED_CONIFOLD,
    SCHOEN_MANIFOLD,
    ThreeDComparison,
    ThreeRegimeAnalysis,
    abel_jacobi_quintic,
    abel_jacobi_toric,
    dt_invariants_conifold,
    formulate_conjecture,
    large_N_growth_rate,
    master_conjecture_statement,
    partition_count,
    rational_curve_degree_d,
)


# =========================================================================
# 1. Partition function tests
# =========================================================================

class TestPartitionCount:
    """Test the partition counting function."""

    def test_p0(self):
        assert partition_count(0) == 1

    def test_p1(self):
        assert partition_count(1) == 1

    def test_p2(self):
        assert partition_count(2) == 2

    def test_p3(self):
        assert partition_count(3) == 3

    def test_p4(self):
        assert partition_count(4) == 5

    def test_p5(self):
        assert partition_count(5) == 7

    def test_p10(self):
        assert partition_count(10) == 42

    def test_p20(self):
        assert partition_count(20) == 627

    def test_p_negative(self):
        assert partition_count(-1) == 0

    def test_p_monotone(self):
        """Partition numbers are monotonically increasing for n >= 1."""
        for n in range(1, 25):
            assert partition_count(n) <= partition_count(n + 1)


# =========================================================================
# 2. Curve geometry tests
# =========================================================================

class TestCurveInCY3:
    """Test holomorphic curve data structures."""

    def test_rational_curve_normal_bundle(self):
        """Rational curve (g=0) in CY3: N = O(a)+O(b) with a+b = -2."""
        c = RATIONAL_CURVE_CONIFOLD
        assert c.genus == 0
        assert c.normal_bundle_degree == -2

    def test_elliptic_curve_normal_bundle(self):
        """Elliptic curve (g=1) in CY3: N = O+O (trivial), deg = 0."""
        c = ELLIPTIC_CURVE_CY3
        assert c.genus == 1
        assert c.normal_bundle_degree == 0
        assert c.normal_bundle == (0, 0)

    def test_genus2_normal_bundle(self):
        """Genus-2 curve in CY3: N has degree 2."""
        c = GENUS2_CURVE_CY3
        assert c.genus == 2
        assert c.normal_bundle_degree == 2

    def test_adjunction_formula(self):
        """Adjunction: deg(N_{C/X}) = 2g - 2 for curve C in CY3 X."""
        for g in range(5):
            a = g - 1
            b = g - 1
            c = CurveInCY3(genus=g, degree=1, normal_bundle=(a, b))
            assert c.normal_bundle_degree == 2 * g - 2

    def test_adjunction_violation_raises(self):
        """Normal bundle degree inconsistent with adjunction -> error."""
        with pytest.raises(ValueError, match="adjunction"):
            CurveInCY3(genus=0, degree=1, normal_bundle=(0, 0))

    def test_boundary_toroidal_only_genus1(self):
        """Only genus-1 curves have toroidal complement boundary."""
        assert not RATIONAL_CURVE_CONIFOLD.boundary_is_toroidal
        assert ELLIPTIC_CURVE_CY3.boundary_is_toroidal
        assert not GENUS2_CURVE_CY3.boundary_is_toroidal

    def test_complement_boundary_type_g0(self):
        assert "S^3" in RATIONAL_CURVE_CONIFOLD.complement_boundary_type

    def test_complement_boundary_type_g1(self):
        assert "T^4" in ELLIPTIC_CURVE_CY3.complement_boundary_type

    def test_degree_d_curve(self):
        """Degree-d rational curve factory."""
        c = rational_curve_degree_d(5)
        assert c.degree == 5
        assert c.genus == 0


# =========================================================================
# 3. CY3 geometry tests
# =========================================================================

class TestCY3Geometry:
    """Test CY3 geometry data."""

    def test_euler_formula(self):
        """chi = 2*(h11 - h21) for all examples."""
        for geom in [RESOLVED_CONIFOLD, LOCAL_P2, QUINTIC, K3_TIMES_E, SCHOEN_MANIFOLD]:
            assert geom.euler == 2 * (geom.h11 - geom.h21)

    def test_euler_violation_raises(self):
        with pytest.raises(ValueError, match="Euler"):
            CY3Geometry("bad", h11=1, h21=0, euler=999,
                        is_toric=False, is_rigid=True)

    def test_rigid_requires_h21_zero(self):
        with pytest.raises(ValueError, match="Rigid"):
            CY3Geometry("bad", h11=1, h21=5, euler=-8,
                        is_toric=False, is_rigid=True)

    def test_conifold_is_toric_rigid(self):
        assert RESOLVED_CONIFOLD.is_toric
        assert RESOLVED_CONIFOLD.is_rigid

    def test_quintic_not_rigid(self):
        assert not QUINTIC.is_rigid
        assert QUINTIC.h21 == 101

    def test_k3e_euler_zero(self):
        assert K3_TIMES_E.euler == 0

    def test_schoen_rigid(self):
        assert SCHOEN_MANIFOLD.is_rigid
        assert SCHOEN_MANIFOLD.h21 == 0

    def test_intermediate_jacobian_dim(self):
        assert RESOLVED_CONIFOLD.intermediate_jacobian_dim == 0
        assert QUINTIC.intermediate_jacobian_dim == 101
        assert K3_TIMES_E.intermediate_jacobian_dim == 21

    def test_abel_jacobi_trivial_for_rigid(self):
        assert RESOLVED_CONIFOLD.abel_jacobi_trivial
        assert SCHOEN_MANIFOLD.abel_jacobi_trivial
        assert not QUINTIC.abel_jacobi_trivial

    def test_kappa_ch_predicted(self):
        """kappa_ch = chi/24 (AP113 compliant)."""
        from fractions import Fraction
        assert K3_TIMES_E.kappa_ch_predicted == Fraction(0)
        assert QUINTIC.kappa_ch_predicted == Fraction(-200, 24)


# =========================================================================
# 4. DT invariant tests
# =========================================================================

class TestDTInvariants:
    """Test DT invariant computations."""

    def test_dt_degree0(self):
        d = dt_invariants_conifold(0)
        assert d["omega_dt"] == 1
        assert d["log_growth"] == 0.0

    def test_dt_degree1(self):
        d = dt_invariants_conifold(1)
        assert d["omega_dt"] == 1  # p(1) = 1

    def test_dt_degree5(self):
        d = dt_invariants_conifold(5)
        assert d["omega_dt"] == 7  # p(5) = 7

    def test_dt_negative_degree(self):
        d = dt_invariants_conifold(-1)
        assert d["omega_dt"] == 0

    def test_dt_growth_positive(self):
        """log growth is positive for N >= 2."""
        for N in range(2, 20):
            d = dt_invariants_conifold(N)
            assert d["log_growth"] > 0

    def test_hardy_ramanujan_ratio(self):
        """log p(N) / (pi*sqrt(2N/3)) -> 1 as N -> inf."""
        for N in [50, 100, 200]:
            d = dt_invariants_conifold(N)
            if d["ratio_to_hr"] is not None:
                # Should approach 1 for large N
                assert 0.5 < d["ratio_to_hr"] < 1.5

    def test_large_N_growth_subexponential(self):
        """(1/N) * log p(N) -> 0 as N -> inf (subexponential)."""
        N_values = [10, 50, 100, 200]
        result = large_N_growth_rate(N_values)
        data = result["data"]
        # Growth rate should decrease
        assert data[-1]["growth_1_over_N_log_pN"] < data[0]["growth_1_over_N_log_pN"]
        # Should be small for large N
        assert data[-1]["growth_1_over_N_log_pN"] < 0.5


# =========================================================================
# 5. Abel-Jacobi period tests
# =========================================================================

class TestAbelJacobiPeriod:
    """Test Abel-Jacobi period computations."""

    def test_toric_period_equals_kahler(self):
        """For toric CY3, AJ(C) = t (Kahler parameter)."""
        t = 2.0 + 1.0j
        assert abel_jacobi_toric(t) == t

    def test_toric_period_real(self):
        t = 3.0
        assert abel_jacobi_toric(t) == 3.0

    def test_quintic_period_large_psi(self):
        """For large |psi|, the quintic period is approximately log(z) ~ -5*log(5*psi)."""
        psi = 100.0
        period = abel_jacobi_quintic(psi)
        # At large psi, z -> 0, so w_0 -> 1, w_1 -> log(z) ~ -5*log(5*psi)
        expected_approx = -5 * cmath.log(5 * psi)
        assert abs(period - expected_approx) / abs(expected_approx) < 0.01

    def test_quintic_period_nonzero(self):
        """Quintic period is nonzero for generic psi."""
        period = abel_jacobi_quintic(10.0)
        assert abs(period) > 0.1

    def test_abel_jacobi_data_trivial_for_rigid(self):
        """AJ period is trivial for rigid CY3."""
        aj = AbelJacobiPeriod(
            geometry=SCHOEN_MANIFOLD,
            curve=CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1)),
            period_value=0.0 + 0.0j,
        )
        assert aj.is_trivial
        assert aj.predicted_growth_rate == 0.0

    def test_abel_jacobi_data_nontrivial_for_quintic(self):
        """AJ period is nontrivial for quintic."""
        period = abel_jacobi_quintic(10.0)
        aj = AbelJacobiPeriod(
            geometry=QUINTIC,
            curve=CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1)),
            period_value=period,
        )
        assert not aj.is_trivial
        assert aj.predicted_growth_rate > 0

    def test_period_norm_is_absolute_value(self):
        aj = AbelJacobiPeriod(
            geometry=QUINTIC,
            curve=CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1)),
            period_value=3.0 + 4.0j,
        )
        assert abs(aj.period_norm - 5.0) < 1e-10

    def test_predicted_growth_rate_formula(self):
        """Growth rate = |AJ|/(2*pi)."""
        aj = AbelJacobiPeriod(
            geometry=QUINTIC,
            curve=CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1)),
            period_value=2 * math.pi + 0.0j,
        )
        assert abs(aj.predicted_growth_rate - 1.0) < 1e-10


# =========================================================================
# 6. Three-regime analysis tests
# =========================================================================

class TestToricRegime:
    """Test the toric regime analysis."""

    def test_toric_converges(self):
        """Toric growth rate converges to t."""
        result = ThreeRegimeAnalysis.toric_regime(t=1.0, N_max=50)
        assert result["regime"] == "toric"
        assert result["predicted_growth_rate"] == 1.0
        # Last data point should be close to t=1
        last = result["data"][-1]
        assert abs(last["lhs"] - 1.0) < 0.3

    def test_toric_correction_decreases(self):
        """The partition correction log(p(N))/N decreases for large N."""
        result = ThreeRegimeAnalysis.toric_regime(t=1.0, N_max=50)
        corrections = [d["partition_correction"] for d in result["data"]]
        # For N >= 3 the correction is positive and decreasing
        # (N=1 has p(1)=1, log(1)=0, which is anomalously low)
        late = [c for c in corrections[2:]]  # skip N=1,2
        assert late[-1] < late[0]

    def test_toric_abel_jacobi_norm(self):
        """Abel-Jacobi norm = 2*pi*t for toric case."""
        result = ThreeRegimeAnalysis.toric_regime(t=2.0)
        assert abs(result["abel_jacobi_norm"] - 4 * math.pi) < 1e-10

    def test_toric_t_zero_subexponential(self):
        """At t=0, growth -> 0 (subexponential)."""
        result = ThreeRegimeAnalysis.toric_regime(t=0.0, N_max=30)
        last = result["data"][-1]
        assert last["lhs"] < 0.5  # Subexponential


class TestRigidRegime:
    """Test the rigid regime analysis."""

    def test_rigid_growth_to_zero(self):
        """For rigid CY3, growth rate -> 0."""
        result = ThreeRegimeAnalysis.rigid_regime(N_max=50)
        assert result["predicted_growth_rate"] == 0.0
        # Growth rate should be decreasing for N >= 3
        # (N=1 has p(1)=1, log(1)/1=0 which is anomalously low)
        data = result["data"]
        late = [d["growth_rate"] for d in data[2:]]  # skip N=1,2
        assert late[-1] < late[0]

    def test_rigid_hr_ratio(self):
        """Hardy-Ramanujan ratio approaches 1."""
        result = ThreeRegimeAnalysis.rigid_regime(N_max=200)
        last = result["data"][-1]
        assert last["ratio"] is not None
        # At N=200 the ratio is ~0.80; convergence is slow (O(1/sqrt(N)))
        assert 0.7 < last["ratio"] < 1.3

    def test_rigid_subexponential(self):
        """Growth rate < 0.5 at N=50."""
        result = ThreeRegimeAnalysis.rigid_regime(N_max=50)
        last = result["data"][-1]
        assert last["growth_rate"] < 0.5


class TestCompactRegime:
    """Test the compact regime analysis."""

    def test_compact_period_nonzero(self):
        """Quintic period is nonzero at generic psi."""
        result = ThreeRegimeAnalysis.compact_regime(psi=10.0)
        assert result["period_norm"] > 0

    def test_compact_predicted_rate_positive(self):
        result = ThreeRegimeAnalysis.compact_regime(psi=10.0)
        assert result["predicted_growth_rate"] > 0

    def test_compact_regime_label(self):
        result = ThreeRegimeAnalysis.compact_regime(psi=10.0)
        assert result["regime"] == "compact"


# =========================================================================
# 7. Formulate conjecture tests
# =========================================================================

class TestFormulateConjecture:
    """Test the conjecture formulation pipeline."""

    def test_conifold_toric_regime(self):
        cvc = formulate_conjecture(
            RESOLVED_CONIFOLD, RATIONAL_CURVE_CONIFOLD,
            kahler_param=1.0 + 0.0j, N_max=10,
        )
        assert cvc.regime == "toric"
        assert cvc.rhs_predicted > 0

    def test_schoen_rigid_regime(self):
        curve = CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1))
        cvc = formulate_conjecture(
            SCHOEN_MANIFOLD, curve,
            kahler_param=0.0j, N_max=10,
        )
        assert cvc.regime == "rigid"
        assert cvc.rhs_predicted == 0.0

    def test_quintic_compact_regime(self):
        curve = CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1))
        cvc = formulate_conjecture(
            QUINTIC, curve,
            kahler_param=1.0 + 0.5j, N_max=10,
        )
        assert cvc.regime == "compact"

    def test_convergence_data_nonempty(self):
        cvc = formulate_conjecture(
            RESOLVED_CONIFOLD, RATIONAL_CURVE_CONIFOLD,
            kahler_param=1.0 + 0.0j, N_max=10,
        )
        conv = cvc.convergence_data()
        assert len(conv) > 0

    def test_lhs_at_N(self):
        cvc = formulate_conjecture(
            RESOLVED_CONIFOLD, RATIONAL_CURVE_CONIFOLD,
            kahler_param=1.0 + 0.0j, N_max=10,
        )
        val = cvc.lhs_at_N(5)
        assert val is not None
        assert val > 0


# =========================================================================
# 8. 3d comparison tests
# =========================================================================

class TestThreeDComparison:
    """Test the 3d-6d comparison."""

    def test_comparison_table_complete(self):
        table = ThreeDComparison.comparison_table()
        assert "3d" in table
        assert "6d" in table
        assert "dictionary" in table

    def test_3d_uses_jones(self):
        table = ThreeDComparison.comparison_table()
        assert "Jones" in table["3d"]["quantum_invariant"]

    def test_6d_uses_dt(self):
        table = ThreeDComparison.comparison_table()
        assert "DT" in table["6d"]["quantum_invariant"]

    def test_6d_uses_abel_jacobi(self):
        table = ThreeDComparison.comparison_table()
        assert "Abel-Jacobi" in table["6d"]["classical_geometry"]

    def test_evidence_summary_keys(self):
        ev = ThreeDComparison.evidence_summary()
        assert "toric_evidence" in ev
        assert "attractor_evidence" in ev
        assert "mirror_evidence" in ev
        assert "rigid_evidence" in ev

    def test_knot_volumes(self):
        """Sanity check known knot volumes."""
        vols = ThreeDComparison.KNOT_VOLUMES
        assert abs(vols["4_1"] - 2.0298832128) < 1e-6
        assert vols["3_1"] == 0.0  # Torus knot, not hyperbolic


# =========================================================================
# 9. Obstruction tests
# =========================================================================

class TestObstructions:
    """Test the obstruction analysis."""

    def test_five_obstructions(self):
        obs = ObstructionAnalysis.list_obstructions()
        assert len(obs) == 5

    def test_each_has_resolution(self):
        for o in ObstructionAnalysis.list_obstructions():
            assert "resolution" in o
            assert len(o["resolution"]) > 0

    def test_adversarial_reconciliation(self):
        rec = ObstructionAnalysis.adversarial_reconciliation()
        assert rec["adversarial_assessment"] == "COMPLETE GAP (0% lift rate)"
        assert rec["assessment_correct"] is True

    def test_obstruction_severities(self):
        obs = ObstructionAnalysis.list_obstructions()
        severities = {o["severity"] for o in obs}
        assert "FUNDAMENTAL" in severities
        assert "RESOLVABLE" in severities


# =========================================================================
# 10. Master conjecture tests
# =========================================================================

class TestMasterConjecture:
    """Test the master conjecture statement."""

    def test_is_conjecture_not_theorem(self):
        """AP-CY14: must be conjecture, NEVER theorem."""
        stmt = master_conjecture_statement()
        assert stmt["environment"] == "conjecture"

    def test_claim_status_conjectured(self):
        """AP-CY11: claim status is conjectured."""
        stmt = master_conjecture_statement()
        assert stmt["claim_status"] == "ClaimStatusConjectured"

    def test_three_regimes(self):
        stmt = master_conjecture_statement()
        assert len(stmt["three_regimes"]) == 3
        assert "toric" in stmt["three_regimes"]
        assert "compact" in stmt["three_regimes"]
        assert "rigid" in stmt["three_regimes"]

    def test_relation_to_3d_is_analogue_not_lift(self):
        """The conjecture is an ANALOGUE, not a lift."""
        stmt = master_conjecture_statement()
        assert "ANALOGUE" in stmt["relation_to_3d"]
        assert "not lift" in stmt["relation_to_3d"].lower()

    def test_conjecture_statement_present(self):
        stmt = master_conjecture_statement()
        assert "AJ(C)" in stmt["statement"]["claim"]
        assert "Z_N" in stmt["statement"]["claim"]

    def test_evidence_level(self):
        stmt = master_conjecture_statement()
        assert "MODERATE" in stmt["evidence_level"]

    def test_dependencies_listed(self):
        stmt = master_conjecture_statement()
        assert len(stmt["dependencies"]) >= 2


# =========================================================================
# 11. Cross-consistency tests
# =========================================================================

class TestCrossConsistency:
    """Cross-consistency checks between different components."""

    def test_toric_growth_matches_period(self):
        """For toric CY3, the LHS growth rate should approach the RHS period."""
        t = 2.0
        toric = ThreeRegimeAnalysis.toric_regime(t=t, N_max=100)
        # The partition correction should be small
        last = toric["data"][-1]
        assert last["partition_correction"] < 0.3

    def test_rigid_growth_zero_matches_trivial_period(self):
        """For rigid CY3, growth -> 0 matches AJ = 0."""
        rigid = ThreeRegimeAnalysis.rigid_regime(N_max=100)
        assert rigid["predicted_growth_rate"] == 0.0
        assert rigid["data"][-1]["growth_rate"] < 0.25

    def test_conifold_dt_match_partitions(self):
        """DT invariants at degree N match p(N) for conifold."""
        for N in range(10):
            dt = dt_invariants_conifold(N)
            assert dt["omega_dt"] == partition_count(N)

    def test_adjunction_consistency_all_examples(self):
        """All curve examples satisfy adjunction."""
        curves = [
            RATIONAL_CURVE_CONIFOLD,
            ELLIPTIC_CURVE_CY3,
            GENUS2_CURVE_CY3,
            RATIONAL_CURVE_LOCAL_P2,
            rational_curve_degree_d(3),
        ]
        for c in curves:
            assert c.normal_bundle_degree == 2 * c.genus - 2

    def test_euler_consistency_all_geometries(self):
        """All CY3 examples satisfy chi = 2*(h11 - h21)."""
        geometries = [RESOLVED_CONIFOLD, LOCAL_P2, QUINTIC, K3_TIMES_E, SCHOEN_MANIFOLD]
        for g in geometries:
            assert g.euler == 2 * (g.h11 - g.h21)

    def test_k3e_kappa_zero(self):
        """K3 x E has chi=0, so kappa_ch = 0."""
        from fractions import Fraction
        assert K3_TIMES_E.kappa_ch_predicted == Fraction(0)

    def test_quintic_large_h21(self):
        """Quintic has large intermediate Jacobian."""
        assert QUINTIC.intermediate_jacobian_dim == 101

    def test_partition_count_used_consistently(self):
        """partition_count is used consistently in DT and growth."""
        for N in [5, 10, 15]:
            dt = dt_invariants_conifold(N)
            assert dt["omega_dt"] == partition_count(N)
            assert dt["log_growth"] == math.log(partition_count(N))


# =========================================================================
# 12. Multi-path cross-verification (AP10 compliance)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path cross-checks: verify each claim via two independent routes."""

    def test_partition_euler_recurrence_vs_direct(self):
        """Cross-check: partition count via Euler recurrence vs generating function.

        Path 1: partition_count (Euler pentagonal recurrence).
        Path 2: coefficient extraction from prod 1/(1-q^k) truncated.
        """
        N = 15
        # Path 1: our recurrence
        p1 = partition_count(N)
        # Path 2: generating function product
        coeffs = [0] * (N + 1)
        coeffs[0] = 1
        for k in range(1, N + 1):
            for n in range(k, N + 1):
                coeffs[n] += coeffs[n - k]
        p2 = coeffs[N]
        assert p1 == p2, f"Partition count mismatch at N={N}: {p1} vs {p2}"

    def test_adjunction_two_paths(self):
        """Cross-check adjunction: deg(N) = 2g-2 via two routes.

        Path 1: CurveInCY3 internal check (constructor validation).
        Path 2: Direct computation from c_1(T_C) + c_1(N) = c_1(T_X|_C) = 0.
        Since c_1(T_C) = 2-2g and c_1(X)=0 (CY), deg(N) = -(2-2g) = 2g-2.
        """
        for g in range(6):
            # Path 1: constructor accepts (g-1, g-1) as splitting
            c = CurveInCY3(genus=g, degree=1, normal_bundle=(g - 1, g - 1))
            path1 = c.normal_bundle_degree
            # Path 2: direct formula
            path2 = 2 * g - 2
            assert path1 == path2

    def test_euler_char_two_paths(self):
        """Cross-check: chi = 2(h11 - h21) via geometry and Hodge diamond.

        Path 1: CY3Geometry.euler (stored value, validated in constructor).
        Path 2: For CY3, chi = 2(h^{1,1} - h^{2,1}) from
                h^{0,0}=h^{3,3}=1, h^{1,0}=h^{2,0}=0 (simply connected).
        """
        for geom in [RESOLVED_CONIFOLD, QUINTIC, K3_TIMES_E, SCHOEN_MANIFOLD]:
            path1 = geom.euler
            # Path 2: full Hodge diamond for CY3
            # b0=1, b1=0, b2=h11, b3=2+2*h21, b4=h11, b5=0, b6=1
            b = [1, 0, geom.h11, 2 + 2 * geom.h21, geom.h11, 0, 1]
            path2 = sum((-1) ** k * b[k] for k in range(7))
            assert path1 == path2, f"{geom.name}: {path1} vs {path2}"

    def test_growth_rate_two_paths_toric(self):
        """Cross-check toric growth: direct computation vs ThreeRegimeAnalysis.

        Path 1: Direct (1/N)*log(p(N)) + t computation.
        Path 2: ThreeRegimeAnalysis.toric_regime output.
        """
        t = 1.5
        N = 30
        # Path 1: direct
        pN = partition_count(N)
        direct_lhs = math.log(pN) / N + t
        # Path 2: from the analysis engine
        result = ThreeRegimeAnalysis.toric_regime(t=t, N_max=N)
        engine_data = [d for d in result["data"] if d["N"] == N]
        assert len(engine_data) == 1
        engine_lhs = engine_data[0]["lhs"]
        assert abs(direct_lhs - engine_lhs) < 1e-12

    def test_abel_jacobi_toric_two_paths(self):
        """Cross-check: toric AJ via direct function and formulate_conjecture.

        Path 1: abel_jacobi_toric(t) directly.
        Path 2: formulate_conjecture -> abel_jacobi.period_value.
        """
        t = 2.5 + 0.7j
        # Path 1
        path1 = abel_jacobi_toric(t)
        # Path 2
        cvc = formulate_conjecture(
            RESOLVED_CONIFOLD, RATIONAL_CURVE_CONIFOLD,
            kahler_param=t, N_max=5,
        )
        path2 = cvc.abel_jacobi.period_value
        assert abs(path1 - path2) < 1e-12

    def test_predicted_growth_two_paths(self):
        """Cross-check predicted growth rate via AbelJacobiPeriod and formula.

        Path 1: AbelJacobiPeriod.predicted_growth_rate property.
        Path 2: Direct |period|/(2*pi) computation.
        """
        period = 3.0 + 4.0j
        aj = AbelJacobiPeriod(
            geometry=QUINTIC,
            curve=CurveInCY3(genus=0, degree=1, normal_bundle=(-1, -1)),
            period_value=period,
        )
        path1 = aj.predicted_growth_rate
        path2 = abs(period) / (2 * math.pi)
        assert abs(path1 - path2) < 1e-15

    def test_rigid_prediction_two_paths(self):
        """Cross-check: rigid CY3 prediction via two independent routes.

        Path 1: geometry.abel_jacobi_trivial implies growth=0.
        Path 2: ThreeRegimeAnalysis.rigid_regime gives predicted_rate=0.
        """
        # Path 1: from the geometry
        assert SCHOEN_MANIFOLD.abel_jacobi_trivial
        path1_prediction = 0.0  # AJ = 0 implies growth -> 0

        # Path 2: from the regime analysis
        result = ThreeRegimeAnalysis.rigid_regime(N_max=20)
        path2_prediction = result["predicted_growth_rate"]

        assert path1_prediction == path2_prediction

    def test_dt_log_growth_two_paths(self):
        """Cross-check DT log growth via dt_invariants_conifold and manual.

        Path 1: dt_invariants_conifold(N)["log_growth"].
        Path 2: math.log(partition_count(N)) directly.
        """
        for N in [3, 7, 12, 20]:
            path1 = dt_invariants_conifold(N)["log_growth"]
            path2 = math.log(partition_count(N))
            assert abs(path1 - path2) < 1e-14, f"Mismatch at N={N}"

    def test_quintic_period_mirror_map_consistency(self):
        """Cross-check: quintic period at large psi via two expansions.

        Path 1: abel_jacobi_quintic(psi) (our engine).
        Path 2: Direct asymptotic: for large psi, z ~ 0, w_0 ~ 1,
                period ~ log(z) = -5*log(5*psi).
        """
        psi = 500.0
        path1 = abel_jacobi_quintic(psi)
        # Path 2: asymptotic
        z = 1.0 / (5.0 * psi) ** 5
        path2 = cmath.log(z)  # ~ -5*log(5*psi) for large psi
        # At very large psi these should agree well (w_0 -> 1)
        assert abs(path1 - path2) / abs(path2) < 0.001

    def test_kappa_ch_cross_volume_consistency(self):
        """Cross-check kappa_ch = chi/24 against known values.

        Path 1: CY3Geometry.kappa_ch_predicted.
        Path 2: Direct chi/24 computation from Hodge numbers.
        """
        from fractions import Fraction
        for geom in [RESOLVED_CONIFOLD, QUINTIC, K3_TIMES_E, SCHOEN_MANIFOLD]:
            path1 = geom.kappa_ch_predicted
            path2 = Fraction(2 * (geom.h11 - geom.h21), 24)
            assert path1 == path2, f"{geom.name}: {path1} vs {path2}"

    def test_intermediate_jacobian_dim_two_paths(self):
        """Cross-check J^2(X) dimension via property and Hodge theory.

        Path 1: CY3Geometry.intermediate_jacobian_dim.
        Path 2: dim J^2(X) = h^{2,1} for CY3 (Griffiths: J^p(X) for
                odd-dim middle cohomology; for CY3, H^3 has h^{3,0}=1,
                h^{2,1}=h21, so dim_C J^2 = h^{2,1}).
        """
        for geom in [RESOLVED_CONIFOLD, QUINTIC, K3_TIMES_E, SCHOEN_MANIFOLD]:
            path1 = geom.intermediate_jacobian_dim
            path2 = geom.h21  # Direct from Hodge theory
            assert path1 == path2

    def test_conifold_convergence_monotone_approach(self):
        """Cross-check: the LHS approaches RHS monotonically for toric.

        For conifold at t>0, (1/N)*log(Z_N) = t + log(p(N))/N.
        The correction log(p(N))/N is eventually monotonically decreasing
        (for N >= 3), so the LHS approaches t from above.

        Path 1: compute directly from partition_count.
        Path 2: extract from formulate_conjecture convergence_data.
        """
        t = 1.0
        cvc = formulate_conjecture(
            RESOLVED_CONIFOLD, RATIONAL_CURVE_CONIFOLD,
            kahler_param=t + 0.0j, N_max=30,
        )
        conv = cvc.convergence_data()

        # Path 1: direct computation for N=10, N=20
        p10 = partition_count(10)
        p20 = partition_count(20)
        direct_10 = (math.log(p10) + 10 * t) / 10
        direct_20 = (math.log(p20) + 20 * t) / 20

        # Path 2: from convergence data
        engine_10 = [c for c in conv if c["N"] == 10]
        engine_20 = [c for c in conv if c["N"] == 20]
        assert len(engine_10) == 1 and len(engine_20) == 1

        assert abs(direct_10 - engine_10[0]["lhs"]) < 1e-10
        assert abs(direct_20 - engine_20[0]["lhs"]) < 1e-10

        # The correction decreases: N=20 closer to t than N=10
        assert engine_20[0]["difference"] < engine_10[0]["difference"]
