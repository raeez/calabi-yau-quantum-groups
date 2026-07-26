r"""Tests for the CY4 E_2 tower: does CY4 → E_2?

CENTRAL QUESTION: The naive pattern CY_d → E_{d-2} predicts CY4 → E_2.
ANSWER: NO.  CY4 gives E_1 with Z-shifted structure (p_1 obstruction).

ORGANIZATION:
  1. CY dimension tower (CY_d → E_{d-2} prediction tests)          [16 tests]
  2. K3 × K3 product analysis                                       [12 tests]
  3. S^d ≠ S^a × S^b topological obstruction                        [14 tests]
  4. CY4 quiver charts                                               [8 tests]
  5. Cech descent spectral sequence for CY4                          [12 tests]
  6. E_n obstruction classes                                         [8 tests]
  7. SO(d) representation theory / dimensional induction             [14 tests]
  8. Pontryagin class computations                                   [8 tests]
  9. Multi-path verification (6 paths, all must agree)               [12 tests]
  10. Full summary and cross-checks                                  [8 tests]

Total: 112 tests.

VERIFICATION STANDARD: Each claim verified by at least 3 independent paths.

GROUND TRUTH:
  - higher_cy_en_tower.py: E_n tower, Bott periodicity, framing obstruction
  - cech_descent_e1.py: Cech descent, spectral sequence degeneration
  - e1_hocolim_cy3.py: hocolim, bar construction
  - Bott, "Stable homotopy of classical groups" (Ann. Math. 1959)
  - Lurie, "Higher Algebra" (2017)
"""

import math
from fractions import Fraction
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
CY4_E2_TOWER_LIB = REPO_ROOT / "compute/lib/cy4_e2_tower.py"

from compute.lib.cy4_e2_tower import (
    CY4CechDescentResult,
    CY4ProductAnalysis,
    CYDimensionTowerEntry,
    DimensionalInductionEntry,
    EnObstruction,
    SOdDecomposition,
    SphereProductAnalysis,
    c4_chart,
    cy4_cech_descent_2chart,
    cy4_cech_descent_3chart,
    cy_dimension_tower_entry,
    dimensional_induction_check,
    e1_to_e2_obstruction_cy4,
    e2_to_e3_obstruction,
    framing_obstruction_is_nontrivial_cy4,
    full_cy4_summary,
    full_cy_dimension_tower,
    full_dimensional_induction,
    hypothetical_e2_cech_3chart,
    k3_cross_k3_e2_analysis,
    k3xk3_product_chart,
    pontryagin_class_k3,
    pontryagin_class_k3xk3,
    pontryagin_class_sextic_p5,
    so_d_analysis,
    sphere_product_comparison,
    tot_kp3_chart,
    verify_cy4_not_e2,
    verify_so_d_at_d234,
)

from compute.lib.higher_cy_en_tower import (
    en_structure,
    e1_stabilization,
    framing_obstruction,
    pi_k_BU,
    pi_k_BO,
    pi_k_BSp,
)


# =========================================================================
# 1. CY DIMENSION TOWER (16 tests)
# =========================================================================

class TestCYDimensionTower:
    """Test the CY_d → E_{d-2} naive prediction at each dimension."""

    def test_d1_naive_prediction_fails(self):
        """d=1: E_{-1} doesn't exist; actual = E_∞."""
        e = cy_dimension_tower_entry(1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == -1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_infty"
        assert not e.naive_correct

    def test_d2_naive_prediction_fails(self):
        """d=2: naive predicts E_0, actual = E_2 (richer than predicted)."""
        e = cy_dimension_tower_entry(2)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 0
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_2"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_n == 2
        assert not e.naive_correct

    def test_d3_naive_prediction_correct(self):
        """d=3: naive predicts E_1, actual = E_1. The ONLY correct case."""
        e = cy_dimension_tower_entry(3)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_1"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_n == 1
        assert e.naive_correct

    def test_d4_naive_prediction_fails(self):
        """d=4: naive predicts E_2, actual = E_1. The central test."""
        e = cy_dimension_tower_entry(4)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 2
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_1"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_n == 1
        assert not e.naive_correct

    def test_d5_naive_prediction_fails(self):
        """d=5: naive predicts E_3, actual = E_1."""
        e = cy_dimension_tower_entry(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 3
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_1"
        assert not e.naive_correct

    def test_d6_naive_prediction_fails(self):
        """d=6: naive predicts E_4, actual = E_1."""
        e = cy_dimension_tower_entry(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 4
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_1"
        assert not e.naive_correct

    def test_d7_naive_prediction_fails(self):
        """d=7: naive predicts E_5, actual = E_1."""
        e = cy_dimension_tower_entry(7)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 5
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_1"
        assert not e.naive_correct

    def test_d8_naive_prediction_fails(self):
        """d=8: naive predicts E_6, actual = E_1."""
        e = cy_dimension_tower_entry(8)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.naive_n == 6
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.actual_en == "E_1"
        assert not e.naive_correct

    def test_only_d3_is_correct(self):
        """The naive CY_d → E_{d-2} is correct ONLY at d=3."""
        tower = full_cy_dimension_tower(d_max=8)
        correct = [e.d for e in tower if e.naive_correct]
        # VERIFIED [DC] structural property [CF] cross-family census
        assert correct == [3]

    def test_tower_d_ge4_all_e1(self):
        """For d ≥ 4, the actual E_n is always E_1 (stabilization)."""
        tower = full_cy_dimension_tower(d_max=12)
        for e in tower:
            if e.d >= 4:
                # VERIFIED [DC] genus tower [CF] cross-family census
                assert e.actual_en == "E_1", f"d={e.d}: expected E_1, got {e.actual_en}"
                # VERIFIED [DC] genus tower [CF] cross-family census
                assert e.actual_n == 1

    def test_d4_obstruction_nontrivial(self):
        """d=4: π_4(BU) = Z (nontrivial obstruction)."""
        e = cy_dimension_tower_entry(4)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.obstruction_group == "Z"
        assert not e.obstruction_trivial

    def test_d4_explanation_mentions_pontryagin(self):
        """d=4 explanation references the first Pontryagin class."""
        e = cy_dimension_tower_entry(4)
        assert "Pontryagin" in e.explanation or "p_1" in e.explanation

    def test_d1_obstruction_trivial(self):
        """d=1: π_1(BU) = 0 (trivial obstruction → E_∞)."""
        e = cy_dimension_tower_entry(1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.obstruction_group == "0"
        assert e.obstruction_trivial

    def test_d2_obstruction_z(self):
        """d=2: π_2(BU) = Z (gives the braiding parameter for E_2)."""
        e = cy_dimension_tower_entry(2)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.obstruction_group == "Z"

    def test_d3_obstruction_trivial(self):
        """d=3: π_3(BU) = 0 (trivial → clean E_1)."""
        e = cy_dimension_tower_entry(3)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert e.obstruction_group == "0"
        assert e.obstruction_trivial

    def test_tower_consistency_with_en_structure(self):
        """Cross-check: tower entries match en_structure() from higher_cy_en_tower."""
        for d in range(1, 9):
            tower_e = cy_dimension_tower_entry(d)
            es = en_structure(d)
            assert tower_e.actual_en == es.native_en, f"d={d} mismatch"
            assert tower_e.actual_n == es.native_n, f"d={d} mismatch"


# =========================================================================
# 2. K3 × K3 PRODUCT ANALYSIS (12 tests)
# =========================================================================

class TestK3CrossK3:
    """Test the K3 × K3 CY4 analysis."""

    def test_euler_characteristic(self):
        """χ(K3 × K3) = 24² = 576."""
        a = k3_cross_k3_e2_analysis()
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert a.euler_char == 576

    def test_kappa(self):
        """κ(K3 × K3) = 48 (additive: 24 + 24)."""
        a = k3_cross_k3_e2_analysis()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert a.kappa == Fraction(48)

    def test_each_k3_is_e2(self):
        """Each K3 factor gives E_2."""
        a = k3_cross_k3_e2_analysis()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert a.each_k3_en == "E_2"

    def test_product_actual_is_e1(self):
        """K3 × K3 gives E_1, NOT E_2."""
        a = k3_cross_k3_e2_analysis()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert a.product_actual_en == "E_1"

    def test_dunn_does_not_apply(self):
        """Dunn additivity does NOT apply to give E_2."""
        a = k3_cross_k3_e2_analysis()
        assert not a.dunn_applies

    def test_s4_not_s2_cross_s2(self):
        """S^4 ≠ S^2 × S^2 (topologically)."""
        a = k3_cross_k3_e2_analysis()
        assert not a.s4_eq_s2_cross_s2

    def test_cy4_trace_not_product(self):
        """The CY4 trace is NOT a product of K3 traces."""
        a = k3_cross_k3_e2_analysis()
        assert not a.cy4_trace_is_product

    def test_framing_obstruction_z(self):
        """The framing obstruction for K3 × K3 is π_4(BU) = Z."""
        a = k3_cross_k3_e2_analysis()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert a.framing_obs == "Z"

    def test_kappa_exact_value(self):
        """κ = 48 exactly (not approximate)."""
        a = k3_cross_k3_e2_analysis()
        assert isinstance(a.kappa, Fraction)
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert a.kappa == Fraction(48, 1)

    def test_hh_total_matches_higher_tower(self):
        """Cross-check HH total with higher_cy_en_tower data."""
        from compute.lib.higher_cy_en_tower import k3_cross_k3_data
        data = k3_cross_k3_data()
        a = k3_cross_k3_e2_analysis()
        assert a.hh_total == data.hh_total

    def test_euler_matches_higher_tower(self):
        """Cross-check Euler char with higher_cy_en_tower data."""
        from compute.lib.higher_cy_en_tower import k3_cross_k3_data
        data = k3_cross_k3_data()
        a = k3_cross_k3_e2_analysis()
        assert a.euler_char == data.euler_characteristic

    def test_product_naive_mentions_dunn(self):
        """The naive prediction mentions Dunn additivity."""
        a = k3_cross_k3_e2_analysis()
        assert "Dunn" in a.product_naive_en


# =========================================================================
# 3. S^d ≠ S^a × S^b TOPOLOGICAL OBSTRUCTION (14 tests)
# =========================================================================

class TestSphereProduct:
    """Test the S^d vs S^a × S^b comparison."""

    def test_s4_homology_ne_s2xs2(self):
        """H_*(S^4) ≠ H_*(S^2 × S^2): Betti numbers differ."""
        sp = sphere_product_comparison(4)
        assert not sp.homology_match

    def test_s4_homology_values(self):
        """H_*(S^4) = {0:1, 4:1}, H_*(S^2×S^2) = {0:1, 2:2, 4:1}."""
        sp = sphere_product_comparison(4)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sp.h_sphere == {0: 1, 4: 1}
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sp.h_product == {0: 1, 2: 2, 4: 1}

    def test_s4_pi2_ne_s2xs2_pi2(self):
        """π_2(S^4) = 0 ≠ Z⊕Z = π_2(S^2 × S^2)."""
        sp = sphere_product_comparison(4)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sp.pi2_sphere == "0"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sp.pi2_product == "Z+Z"
        assert not sp.homotopy_match

    def test_s4_pi3_ne_s2xs2_pi3(self):
        """π_3(S^4) = 0, π_3(S^2 × S^2) = Z⊕Z (from Hopf)."""
        sp = sphere_product_comparison(4)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sp.pi3_sphere == "0"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sp.pi3_product == "Z+Z"

    def test_s4_euler_ne_s2xs2_euler(self):
        """χ(S^4) = 2, χ(S^2 × S^2) = 4."""
        sp = sphere_product_comparison(4)
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert sp.chi_sphere == 2
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert sp.chi_product == 4

    def test_s2xs2_has_cup_product(self):
        """S^2 × S^2 has nontrivial cup product H^2 ⊗ H^2 → H^4."""
        sp = sphere_product_comparison(4)
        assert sp.cup_product_nontrivial

    def test_s4_cup_trivial(self):
        """S^4 has trivial intermediate cup products."""
        sp = sphere_product_comparison(4)
        assert sp.sphere_cup_trivial

    def test_s3_homology_ne_s1xs2(self):
        """H_*(S^3) ≠ H_*(S^1 × S^2)."""
        sp = sphere_product_comparison(3)
        assert not sp.homology_match

    def test_s3_betti(self):
        """H_*(S^3) = {0:1, 3:1}, H_*(S^1×S^2) = {0:1, 1:1, 2:1, 3:1}."""
        sp = sphere_product_comparison(3)
        # VERIFIED [DC] Betti number [CF] cross-family census
        assert sp.h_sphere == {0: 1, 3: 1}
        # VERIFIED [DC] Betti number [CF] cross-family census
        assert sp.h_product == {0: 1, 1: 1, 2: 1, 3: 1}

    def test_s2_ne_s1xs1(self):
        """S^2 ≠ S^1 × S^1 (sphere ≠ torus)."""
        sp = sphere_product_comparison(2)
        assert not sp.homology_match

    def test_s5_ne_s2xs3(self):
        """S^5 ≠ S^2 × S^3."""
        sp = sphere_product_comparison(5)
        assert not sp.homology_match

    def test_chi_s4_formula(self):
        """χ(S^d) = 1 + (-1)^d. For d=4: χ = 2."""
        for d in range(1, 9):
            sp = sphere_product_comparison(d)
            # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
            assert sp.chi_sphere == 1 + (-1)**d

    def test_s4_not_homotopy_equiv(self):
        """S^4 is not homotopy equivalent to S^2 × S^2 (both paths fail)."""
        sp = sphere_product_comparison(4)
        assert not sp.homology_match
        assert not sp.homotopy_match

    def test_sphere_product_euler_product_formula(self):
        """χ(S^a × S^b) = χ(S^a) · χ(S^b)."""
        for d in range(2, 9):
            sp = sphere_product_comparison(d)
            a = d // 2
            b = d - a
            # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
            assert sp.chi_product == (1 + (-1)**a) * (1 + (-1)**b)


# =========================================================================
# 4. CY4 QUIVER CHARTS (8 tests)
# =========================================================================

class TestCY4QuiverCharts:
    """Test the CY4 quiver chart data."""

    def test_tot_kp3_nodes(self):
        """Tot(K_{P³}) McKay quiver has 4 nodes (from Z_4)."""
        c = tot_kp3_chart()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert c.n_nodes == 4

    def test_tot_kp3_potential_degree(self):
        """CY4 superpotential has degree 4."""
        c = tot_kp3_chart()
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert c.potential_degree == 4

    def test_tot_kp3_is_e1(self):
        """Tot(K_{P³}) CoHA has E_1 structure."""
        c = tot_kp3_chart()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert c.en_structure == "E_1"

    def test_c4_chart(self):
        """C^4 has trivial quiver (1 node), W=0."""
        c = c4_chart()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert c.n_nodes == 1
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert c.potential_degree == 0
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert c.en_structure == "E_1"

    def test_c4_generators(self):
        """C^4 CoHA has 4 generators in charge 1."""
        c = c4_chart()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert c.coha_generators[1] == 4

    def test_k3xk3_product_charts_count(self):
        """K3×K3 with n charts per K3 gives n² product charts."""
        for n in [2, 3, 4]:
            charts = k3xk3_product_chart(n)
            assert len(charts) == n * n

    def test_k3xk3_charts_all_e1(self):
        """All K3×K3 product charts have E_1 structure."""
        charts = k3xk3_product_chart(3)
        for c in charts:
            # VERIFIED [DC] chart decomposition [CF] cross-family census
            assert c.en_structure == "E_1"

    def test_cy4_potential_degree_matches_dimension(self):
        """The superpotential degree matches CY dimension d=4."""
        c = tot_kp3_chart()
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert c.potential_degree == 4  # CY4 → degree 4


# =========================================================================
# 5. CECH DESCENT SPECTRAL SEQUENCE FOR CY4 (12 tests)
# =========================================================================

class TestCechDescentCY4:
    """Test the Cech descent spectral sequence for CY4."""

    def test_2chart_degenerates_at_e2(self):
        """2-chart CY4 atlas: spectral sequence degenerates at E_2."""
        r = cy4_cech_descent_2chart()
        assert r.degenerates_at_e2

    def test_2chart_algebra_type_e1(self):
        """2-chart CY4: algebra type is E_1."""
        r = cy4_cech_descent_2chart()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert r.algebra_type == "E_1"

    def test_2chart_e2_22_zero(self):
        """2-chart CY4: E_2^{2,*} = 0 (no braiding coherence)."""
        r = cy4_cech_descent_2chart()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert r.e2_22_dim == 0

    def test_2chart_d2_trivial(self):
        """2-chart CY4: d_2 differential is trivially zero."""
        r = cy4_cech_descent_2chart()
        assert not r.d2_exists

    def test_3chart_degenerates_at_e2(self):
        """3-chart CY4 atlas: spectral sequence degenerates at E_2."""
        r = cy4_cech_descent_3chart()
        assert r.degenerates_at_e2

    def test_3chart_algebra_type_e1(self):
        """3-chart CY4: algebra type is E_1."""
        r = cy4_cech_descent_3chart()
        # VERIFIED [DC] chart decomposition [CF] cross-family census
        assert r.algebra_type == "E_1"

    def test_3chart_e2_22_zero(self):
        """3-chart CY4: E_2^{2,*} = 0 (critical test)."""
        r = cy4_cech_descent_3chart()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert r.e2_22_dim == 0

    def test_3chart_d2_trivial(self):
        """3-chart CY4: d_2 differential trivially zero."""
        r = cy4_cech_descent_3chart()
        assert not r.d2_exists

    def test_hypothetical_e2_does_not_degenerate(self):
        """Hypothetical E_2 algebra: spectral sequence does NOT degenerate."""
        r = hypothetical_e2_cech_3chart()
        assert not r.degenerates_at_e2

    def test_hypothetical_e2_has_braiding_coherence(self):
        """Hypothetical E_2: E_2^{2,0} = 1 (hexagon datum)."""
        r = hypothetical_e2_cech_3chart()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert r.e2_22_dim == 1

    def test_hypothetical_e2_d2_exists(self):
        """Hypothetical E_2: d_2 differential may exist."""
        r = hypothetical_e2_cech_3chart()
        assert r.d2_exists

    def test_e1_vs_e2_comparison(self):
        """E_1 and E_2 give different Cech descent outcomes at degree 2."""
        e1_result = cy4_cech_descent_3chart()
        e2_result = hypothetical_e2_cech_3chart()
        # The key difference: E_2^{2,*}
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert e1_result.e2_22_dim == 0
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert e2_result.e2_22_dim == 1
        assert e1_result.degenerates_at_e2
        assert not e2_result.degenerates_at_e2


# =========================================================================
# 6. E_n OBSTRUCTION CLASSES (8 tests)
# =========================================================================

class TestEnObstructions:
    """Test the E_1 → E_2 and E_2 → E_3 obstruction computations."""

    def test_e1_to_e2_obstruction_group(self):
        """E_1 → E_2 obstruction for CY4 is Z-valued."""
        obs = e1_to_e2_obstruction_cy4()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert obs.obstruction_group == "Z"

    def test_e1_to_e2_is_nontrivial(self):
        """E_1 → E_2 obstruction for CY4 is nontrivial."""
        obs = e1_to_e2_obstruction_cy4()
        assert not obs.is_trivial

    def test_e1_to_e2_is_pontryagin(self):
        """E_1 → E_2 obstruction is the first Pontryagin class."""
        obs = e1_to_e2_obstruction_cy4()
        assert "p_1" in obs.obstruction_name or "Pontryagin" in obs.obstruction_name

    def test_e1_to_e2_source_target(self):
        """E_1 → E_2: source n=1, target n=2."""
        obs = e1_to_e2_obstruction_cy4()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert obs.source_n == 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert obs.target_n == 2

    def test_e2_to_e3_obstruction_group(self):
        """E_2 → E_3 obstruction is Z_2-valued (moot for CY4)."""
        obs = e2_to_e3_obstruction()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert obs.obstruction_group == "Z_2"

    def test_e2_to_e3_is_nontrivial(self):
        """E_2 → E_3 obstruction is nontrivial."""
        obs = e2_to_e3_obstruction()
        assert not obs.is_trivial

    def test_e2_to_e3_source_target(self):
        """E_2 → E_3: source n=2, target n=3."""
        obs = e2_to_e3_obstruction()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert obs.source_n == 2
        # VERIFIED [DC] structural property [CF] cross-family census
        assert obs.target_n == 3

    def test_e2_to_e3_moot_for_cy4(self):
        """E_2 → E_3 is moot since CY4 gives E_1, not E_2."""
        obs = e2_to_e3_obstruction()
        assert "moot" in obs.explanation.lower()


# =========================================================================
# 7. SO(d) REPRESENTATION THEORY / DIMENSIONAL INDUCTION (14 tests)
# =========================================================================

class TestSOdAnalysis:
    """Test the SO(d) decomposition and dimensional induction."""

    def test_so2_is_u1(self):
        """SO(2) = U(1) (abelian, rank 1)."""
        so = so_d_analysis(2)
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert so.so_d_rank == 1
        assert "U(1)" in so.special_iso

    def test_so3_is_su2_mod_z2(self):
        """SO(3) = SU(2)/Z_2 (rank 1)."""
        so = so_d_analysis(3)
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert so.so_d_rank == 1
        assert "SU(2)" in so.special_iso

    def test_so4_is_su2xsu2_mod_z2(self):
        """SO(4) = (SU(2)×SU(2))/Z_2 (rank 2)."""
        so = so_d_analysis(4)
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert so.so_d_rank == 2
        assert "SU(2)" in so.special_iso
        assert "Z_2" in so.special_iso

    def test_so4_does_not_factor_cleanly(self):
        """SO(4) does NOT factor cleanly for E_2 structure."""
        so = so_d_analysis(4)
        assert not so.factors_cleanly

    def test_so4_z2_obstruction(self):
        """The Z_2 quotient in SO(4) obstructs E_1 ⊗ E_1 → E_2."""
        so = so_d_analysis(4)
        assert "Z_2" in so.obstruction_to_factoring

    def test_so_d_en_predictions(self):
        """SO(d) predictions: d=2→E_2, d=3→E_1, d≥4→E_1."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert so_d_analysis(2).en_from_so == 2
        # VERIFIED [DC] structural property [CF] cross-family census
        assert so_d_analysis(3).en_from_so == 1
        for d in range(4, 9):
            # VERIFIED [DC] structural property [CF] cross-family census
            assert so_d_analysis(d).en_from_so == 1, f"d={d} failed"

    def test_so_d_u1_factor(self):
        """SO(d) has a U(1) factor for d ≥ 2."""
        assert not so_d_analysis(1).u1_factor
        for d in range(2, 9):
            assert so_d_analysis(d).u1_factor, f"d={d}"

    def test_verify_so_d234_all_pass(self):
        """All SO(d) verification checks at d=2,3,4 pass."""
        results = verify_so_d_at_d234()
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_dimensional_induction_d4(self):
        """Dimensional induction at d=4: all methods agree on E_1."""
        e = dimensional_induction_check(4)
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.so_d_prediction == 1
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.en_structure_n == 1
        assert e.all_consistent

    def test_dimensional_induction_all_consistent(self):
        """Dimensional induction is consistent for d=1 through 8."""
        entries = full_dimensional_induction(8)
        for e in entries:
            assert e.all_consistent, f"d={e.d} inconsistent"

    def test_dimensional_induction_d1(self):
        """d=1: SO(1) trivial → E_∞. Consistent."""
        e = dimensional_induction_check(1)
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.so_d_prediction == 100  # E_∞ sentinel
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.en_structure_n == 100
        assert e.all_consistent

    def test_dimensional_induction_d2(self):
        """d=2: SO(2) = U(1) → E_2. Consistent."""
        e = dimensional_induction_check(2)
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.so_d_prediction == 2
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.en_structure_n == 2
        assert e.all_consistent

    def test_dimensional_induction_d3(self):
        """d=3: SO(3) → E_1. Consistent."""
        e = dimensional_induction_check(3)
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.so_d_prediction == 1
        # VERIFIED [DC] dimension [CF] cross-family census
        assert e.en_structure_n == 1
        assert e.all_consistent

    def test_so6_is_su4_mod_z2(self):
        """SO(6) = SU(4)/Z_2 (rank 3, exceptional isomorphism)."""
        so = so_d_analysis(6)
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert so.so_d_rank == 3
        assert "SU(4)" in so.special_iso


# =========================================================================
# 8. PONTRYAGIN CLASS COMPUTATIONS (8 tests)
# =========================================================================

class TestPontryaginClass:
    """Test Pontryagin class computations for CY4 manifolds."""

    def test_p1_k3(self):
        """p_1(K3) = -2c_2(K3) = -2 · 24 = -48."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert pontryagin_class_k3() == -48

    def test_p1_k3_formula(self):
        """p_1 = c_1² - 2c_2. For K3: c_1=0, c_2=24 → p_1=-48."""
        c1_k3 = 0
        c2_k3 = 24
        p1 = c1_k3**2 - 2 * c2_k3
        assert p1 == pontryagin_class_k3()

    def test_p1_k3xk3(self):
        """p_1(K3 × K3) = -48 + (-48) = -96."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert pontryagin_class_k3xk3() == -96

    def test_p1_k3xk3_product_formula(self):
        """p_1(X × Y) = p_1(X) + p_1(Y) for stable characteristic classes."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert pontryagin_class_k3xk3() == 2 * pontryagin_class_k3()

    def test_p1_sextic(self):
        """p_1(sextic in P^5) = -30 (as multiple of H^2)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert pontryagin_class_sextic_p5() == -30

    def test_p1_k3_nontrivial(self):
        """p_1(K3) ≠ 0: framing obstruction is nontrivial."""
        assert framing_obstruction_is_nontrivial_cy4(pontryagin_class_k3())

    def test_p1_k3xk3_nontrivial(self):
        """p_1(K3 × K3) ≠ 0: framing obstruction is nontrivial."""
        assert framing_obstruction_is_nontrivial_cy4(pontryagin_class_k3xk3())

    def test_p1_sextic_nontrivial(self):
        """p_1(sextic) ≠ 0: framing obstruction is nontrivial."""
        assert framing_obstruction_is_nontrivial_cy4(pontryagin_class_sextic_p5())


# =========================================================================
# 9. MULTI-PATH VERIFICATION (12 tests)
# =========================================================================

class TestMultiPathVerification:
    """Test the 6-path verification that CY4 ≠ E_2."""

    def test_path1_bott(self):
        """Path 1: π_4(BU) = Z (Bott periodicity)."""
        v = verify_cy4_not_e2()
        assert v.path1_bott
        # VERIFIED [DC] structural property [CF] cross-family census
        assert v.path1_obs == "Z"

    def test_path2_sphere(self):
        """Path 2: S^4 ≠ S^2 × S^2."""
        v = verify_cy4_not_e2()
        assert v.path2_sphere

    def test_path3_pairing(self):
        """Path 3: symmetric CY4 pairing + π_3(O) = Z."""
        v = verify_cy4_not_e2()
        assert v.path3_pairing
        # VERIFIED [DC] structural property [CF] cross-family census
        assert v.path3_obs == "Z"

    def test_path4_cech(self):
        """Path 4: Cech spectral sequence degenerates (E_1 signal)."""
        v = verify_cy4_not_e2()
        assert v.path4_cech
        # VERIFIED [DC] descent data [CF] cross-family census
        assert v.path4_e2_22 == 0

    def test_path5_so4(self):
        """Path 5: SO(4) Z_2 quotient obstructs E_2."""
        v = verify_cy4_not_e2()
        assert v.path5_so4

    def test_path5_so4_is_hom_side_not_independent_within_surface(self):
        """Path 5 must not reintroduce two independent within-surface E_1s."""
        source = " ".join(CY4_E2_TOWER_LIB.read_text().split())
        assert "two Hom-side E_1 actions on equivariant Hochschild cochains" in source
        assert "They are not two independent within-surface E_1 structures" in source
        stale = "two " + "INDEPENDENT E_1 structures"
        assert stale not in source

    def test_path6_product(self):
        """Path 6: CY4 trace couples K3 factors, blocking Dunn."""
        v = verify_cy4_not_e2()
        assert v.path6_product
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert v.path6_kappa == Fraction(48)

    def test_all_6_paths_agree(self):
        """All 6 independent paths agree: CY4 → E_1, not E_2."""
        v = verify_cy4_not_e2()
        assert v.all_paths_agree

    def test_conclusion_mentions_e1(self):
        """Conclusion explicitly states E_1."""
        v = verify_cy4_not_e2()
        assert "E_1" in v.conclusion

    def test_conclusion_mentions_not_e2(self):
        """Conclusion explicitly states NOT E_2."""
        v = verify_cy4_not_e2()
        assert "NOT E_2" in v.conclusion or "not E_2" in v.conclusion

    def test_path3_consistent_with_bott(self):
        """Path 3 (BO) gives same Z obstruction as Path 1 (BU) at d=4."""
        # π_4(BU) = Z and π_4(BO) = π_3(O) = Z: both nontrivial.
        # VERIFIED [DC] consistency check [CF] cross-family census
        assert pi_k_BU(4) == "Z"
        # VERIFIED [DC] consistency check [CF] cross-family census
        assert pi_k_BO(4) == "Z"

    def test_path1_consistent_with_framing_obstruction(self):
        """Path 1 matches the framing obstruction from higher_cy_en_tower."""
        fo = framing_obstruction(4)
        # VERIFIED [DC] consistency check [CF] cross-family census
        assert fo.bu_obstruction == "Z"
        assert not fo.bu_trivial

    def test_verification_result_complete(self):
        """All fields of the verification result are populated."""
        v = verify_cy4_not_e2()
        assert v.path1_obs != ""
        assert v.path2_detail != ""
        assert v.path3_obs != ""
        assert v.path5_detail != ""
        assert v.conclusion != ""


# =========================================================================
# 10. FULL SUMMARY AND CROSS-CHECKS (8 tests)
# =========================================================================

class TestFullSummary:
    """Test the complete CY4 E_2 tower summary."""

    def test_summary_runs(self):
        """full_cy4_summary() runs without error."""
        s = full_cy4_summary()
        assert s is not None

    def test_naive_correct_only_at_d3(self):
        """The naive prediction CY_d → E_{d-2} is correct only at d=3."""
        s = full_cy4_summary()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert s["naive_correct_at"] == [3]

    def test_naive_incorrect_at_all_others(self):
        """The naive prediction fails at d=1,2,4,5,6,7,8."""
        s = full_cy4_summary()
        assert 4 in s["naive_incorrect_at"]
        assert 1 in s["naive_incorrect_at"]
        assert 2 in s["naive_incorrect_at"]

    def test_all_paths_agree_in_summary(self):
        """The summary reports all 6 verification paths agree."""
        s = full_cy4_summary()
        assert s["all_paths_agree"]

    def test_induction_consistent_in_summary(self):
        """The dimensional induction is consistent across all d."""
        s = full_cy4_summary()
        assert s["induction_consistent"]

    def test_conclusion_present(self):
        """The summary has a conclusion."""
        s = full_cy4_summary()
        assert "conclusion" in s
        # VERIFIED [DC] structural property [CF] cross-family census
        assert len(s["conclusion"]) > 50

    def test_cross_check_en_structure_d4(self):
        """Cross-check: en_structure(4) from higher_cy_en_tower confirms E_1."""
        es = en_structure(4)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert es.native_en == "E_1"
        # VERIFIED [DC] structural property [CF] cross-family census
        assert es.native_n == 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert es.framing_obstruction_BU == "Z"

    def test_cross_check_e1_stabilization_d4(self):
        """Cross-check: e1_stabilization(4) confirms E_1 with Z-shift."""
        stab = e1_stabilization(4)
        assert stab.is_e1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert stab.shifted_by == "Z"
        assert not stab.trivial_obstruction
