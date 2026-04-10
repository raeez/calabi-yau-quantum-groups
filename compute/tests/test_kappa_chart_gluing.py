r"""Tests for kappa_chart_gluing.py: local-to-global kappa computation.

Tests are organized into the following sections:

  1. NERVE FORMULA: basic inclusion-exclusion tests
  2. STANDARD CY3 ATLASES: each standard CY3 gives correct kappa
  3. ATLAS INDEPENDENCE: two presentations of the same CY3 agree
  4. chi/24 CONJECTURE: test failures and successes
  5. HODGE FORMULA: BCOV and toric formulas
  6. PRODUCT FORMULAS: additivity and cross-terms
  7. ORBIFOLD AND RESOLUTION: kappa under group actions
  8. SHADOW TOWER: F_g from glued kappa
  9. TORIC LANDSCAPE: all toric CY3s
  10. CROSS-VERIFICATION: consistency with modular_cy_characteristic
  11. WALL CROSSING: kappa continuity
  12. CICY TABLE: complete intersection CY3s
  13. PROOF STRUCTURE: homotopy invariance proof verification
  14. MULTI-PATH: independent verification paths for each CY3
"""

import pytest
from fractions import Fraction
from typing import Dict

from compute.lib.kappa_chart_gluing import (
    CY3Atlas,
    CY3Chart,
    KappaGluingResult,
    kappa_from_nerve,
    kappa_euler_formula,
    kappa_gluing_invariance_proof,
    c3_atlas,
    conifold_atlas,
    local_p2_atlas,
    local_p2_toric_atlas,
    local_p1xp1_atlas,
    local_hirzebruch_atlas,
    k3_times_e_atlas,
    quintic_atlas,
    quintic_two_phase_atlas,
    e_cubed_atlas,
    spp_atlas,
    c3_z3_orbifold_atlas,
    kappa_from_chi_top_over_24,
    kappa_from_chi_top_over_2,
    kappa_from_bcov_genus1,
    kappa_from_k3_fibration_weight,
    kappa_from_toric_vertex_count,
    kappa_from_macmahon_exponent,
    kappa_product_additive,
    kappa_product_cross_term,
    chi_over_24_conjecture_tests,
    correct_kappa_formula_analysis,
    cicy_kappa_table,
    kappa_orbifold,
    kappa_crepant_resolution,
    verify_all_standard_cy3s,
    shadow_amplitude,
    shadow_tower_from_gluing,
    refine_atlas,
    cross_verify_kappa_values,
    toric_landscape_table,
    f1_multi_path_verification,
    conifold_wall_crossing,
    kappa_hodge_candidates,
    A_HAT_COEFFS,
    STANDARD_CICYS,
    TORIC_CY3_LANDSCAPE,
    HomotopyInvarianceProof,
    ChiOver24Analysis,
    WallCrossingKappa,
)


# =====================================================================
# Section 1: NERVE FORMULA — basic inclusion-exclusion
# =====================================================================

class TestNerveFormula:
    """Test the fundamental inclusion-exclusion (nerve) formula."""

    def test_single_chart_kappa(self):
        """Single chart: kappa = kappa_local."""
        chart = CY3Chart("test", Fraction(7, 3), "G", 1, None)
        atlas = CY3Atlas("test", [chart], {}, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(7, 3)

    def test_two_charts_no_intersection(self):
        """Two disjoint charts: kappa = kappa_1 + kappa_2."""
        c1 = CY3Chart("a", Fraction(2), "G", 1, None)
        c2 = CY3Chart("b", Fraction(3), "G", 1, None)
        atlas = CY3Atlas("test", [c1, c2], {}, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(5)

    def test_two_charts_with_wall(self):
        """Two charts with wall: kappa = k1 + k2 - k_wall."""
        c1 = CY3Chart("a", Fraction(3), "G", 1, None)
        c2 = CY3Chart("b", Fraction(4), "G", 1, None)
        atlas = CY3Atlas("test", [c1, c2], {
            frozenset({0, 1}): Fraction(2),
        }, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(5)  # 3 + 4 - 2

    def test_three_charts_full_nerve(self):
        """Three charts with walls and triple intersection."""
        c0 = CY3Chart("a", Fraction(2), "G", 1, None)
        c1 = CY3Chart("b", Fraction(3), "G", 1, None)
        c2 = CY3Chart("c", Fraction(4), "G", 1, None)
        atlas = CY3Atlas("test", [c0, c1, c2], {
            frozenset({0, 1}): Fraction(1),
            frozenset({0, 2}): Fraction(1),
            frozenset({1, 2}): Fraction(1),
            frozenset({0, 1, 2}): Fraction(1),
        }, None, None)
        result = kappa_from_nerve(atlas)
        # 2+3+4 - 1-1-1 + 1 = 7
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(7)

    def test_euler_formula_basic(self):
        """Simplified nerve formula."""
        result = kappa_euler_formula(
            [Fraction(3), Fraction(4)],
            [Fraction(2)],
        )
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert result == Fraction(5)

    def test_euler_formula_with_triple(self):
        """Nerve formula with triple intersections."""
        result = kappa_euler_formula(
            [Fraction(2), Fraction(3), Fraction(4)],
            [Fraction(1), Fraction(1), Fraction(1)],
            [Fraction(1)],
        )
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert result == Fraction(7)

    def test_zero_kappa_charts(self):
        """Charts with zero kappa."""
        c1 = CY3Chart("a", Fraction(0), "G", 1, None)
        c2 = CY3Chart("b", Fraction(0), "G", 1, None)
        atlas = CY3Atlas("test", [c1, c2], {}, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(0)

    def test_negative_kappa_chart(self):
        """Chart with negative kappa (e.g., quintic)."""
        chart = CY3Chart("test", Fraction(-25, 3), "M", 1, None)
        atlas = CY3Atlas("test", [chart], {}, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(-25, 3)

    def test_nerve_terms_recorded(self):
        """Verify nerve terms are correctly recorded."""
        c0 = CY3Chart("a", Fraction(5), "G", 1, None)
        c1 = CY3Chart("b", Fraction(3), "G", 1, None)
        atlas = CY3Atlas("test", [c0, c1], {
            frozenset({0, 1}): Fraction(2),
        }, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_nerve_terms[0] == Fraction(8)   # 5 + 3
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_nerve_terms[1] == Fraction(2)    # wall
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(6)            # 8 - 2

    def test_four_charts_alternating(self):
        """Four charts with full nerve structure."""
        charts = [CY3Chart(f"c{i}", Fraction(1), "G", 1, None) for i in range(4)]
        atlas = CY3Atlas("test", charts, {
            frozenset({0, 1}): Fraction(1),
            frozenset({1, 2}): Fraction(1),
            frozenset({2, 3}): Fraction(1),
            frozenset({0, 3}): Fraction(1),
            frozenset({0, 1, 2}): Fraction(1),
            frozenset({1, 2, 3}): Fraction(1),
            frozenset({0, 1, 2, 3}): Fraction(1),
        }, None, None)
        result = kappa_from_nerve(atlas)
        # 4*1 - 4*1 + 2*1 - 1*1 = 1
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(1)


# =====================================================================
# Section 2: STANDARD CY3 ATLASES
# =====================================================================

class TestStandardCY3s:
    """Test kappa for each standard CY3 family."""

    def test_c3_kappa_equals_1(self):
        """C^3: kappa = 1 from W_{1+infty}."""
        result = kappa_from_nerve(c3_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(1)

    def test_conifold_kappa_equals_1(self):
        """Conifold: kappa = 1 from chi_top(P^1)/2."""
        result = kappa_from_nerve(conifold_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(1)

    def test_local_p2_kappa_equals_3_over_2(self):
        """Local P^2: kappa = 3/2 from McKay quiver."""
        result = kappa_from_nerve(local_p2_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(3, 2)

    def test_local_p2_toric_kappa(self):
        """Local P^2 toric: kappa = 3/2 from vertex counting."""
        result = kappa_from_nerve(local_p2_toric_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(3, 2)

    def test_local_p1xp1_kappa_equals_2(self):
        """Local P^1xP^1: kappa = 2."""
        result = kappa_from_nerve(local_p1xp1_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(2)

    def test_k3_times_e_kappa_equals_5(self):
        """K3 x E: kappa = 5 from BKM weight."""
        result = kappa_from_nerve(k3_times_e_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(5)

    def test_quintic_kappa_equals_minus_25_over_3(self):
        """Quintic: kappa = -25/3 (conjectural, from chi/24)."""
        result = kappa_from_nerve(quintic_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(-25, 3)

    def test_quintic_two_phase_kappa(self):
        """Quintic two-phase: same kappa as single chart."""
        result = kappa_from_nerve(quintic_two_phase_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(-25, 3)

    def test_e_cubed_kappa_equals_3(self):
        """E^3: kappa = 3 (additive)."""
        result = kappa_from_nerve(e_cubed_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(3)

    def test_spp_kappa_equals_3_over_2(self):
        """SPP: kappa = 3/2."""
        result = kappa_from_nerve(spp_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(3, 2)

    def test_c3_z3_orbifold_kappa(self):
        """C^3/Z_3 orbifold: kappa = 1/3."""
        result = kappa_from_nerve(c3_z3_orbifold_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(1, 3)

    def test_local_hirzebruch_f0(self):
        """Local F_0 = P^1xP^1: kappa = 2."""
        result = kappa_from_nerve(local_hirzebruch_atlas(0))
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(2)

    def test_local_hirzebruch_f1(self):
        """Local F_1: kappa = 2."""
        result = kappa_from_nerve(local_hirzebruch_atlas(1))
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(2)

    def test_local_hirzebruch_f2(self):
        """Local F_2: kappa = 2."""
        result = kappa_from_nerve(local_hirzebruch_atlas(2))
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(2)

    def test_local_hirzebruch_f3(self):
        """Local F_3: kappa = 2 (all F_n have chi=4)."""
        result = kappa_from_nerve(local_hirzebruch_atlas(3))
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(2)

    def test_all_standard_cy3s_pass(self):
        """Master verification: all standard CY3s match."""
        results = verify_all_standard_cy3s()
        for name, data in results.items():
            assert data["match"], f"{name}: got {data['kappa']}, expected {data['expected']}"


# =====================================================================
# Section 3: ATLAS INDEPENDENCE (thm:kappa-gluing-invariance)
# =====================================================================

class TestAtlasIndependence:
    """Verify that different atlas presentations give the same kappa."""

    def test_local_p2_two_presentations(self):
        """Local P^2: single McKay chart vs. 3-vertex toric."""
        assert refine_atlas(local_p2_atlas(), local_p2_toric_atlas())

    def test_quintic_one_vs_two_phase(self):
        """Quintic: single chart vs. LV + Gepner."""
        assert refine_atlas(quintic_atlas(), quintic_two_phase_atlas())

    def test_hirzebruch_f0_vs_p1xp1(self):
        """Local F_0 and local P^1xP^1 both give kappa = 2."""
        r1 = kappa_from_nerve(local_hirzebruch_atlas(0))
        r2 = kappa_from_nerve(local_p1xp1_atlas())
        assert r1.kappa_ch == r2.kappa_ch

    def test_conifold_single_vs_two_chart(self):
        """Conifold: single-chart vs. two-chart atlas."""
        single = CY3Atlas("conifold_single",
            [CY3Chart("con", Fraction(1), "G", 2, 2)],
            {}, 2, None)
        two = conifold_atlas()
        assert refine_atlas(single, two)

    def test_c3_trivial_refinement(self):
        """C^3: the trivial atlas has only one chart."""
        a1 = c3_atlas()
        a2 = CY3Atlas("C3_copy",
            [CY3Chart("C3", Fraction(1), "G", 1, None)],
            {}, None, None)
        assert refine_atlas(a1, a2)


# =====================================================================
# Section 4: chi/24 CONJECTURE analysis
# =====================================================================

class TestChiOver24:
    """Test the conjecture kappa = chi_top / 24."""

    def test_quintic_chi_over_24_matches(self):
        """Quintic: chi/24 = -200/24 = -25/3 matches."""
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert kappa_from_chi_top_over_24(-200) == Fraction(-25, 3)

    def test_k3xe_chi_over_24_fails(self):
        """K3 x E: chi/24 = 0 does NOT match kappa = 5."""
        assert kappa_from_chi_top_over_24(0) != Fraction(5)

    def test_e_cubed_chi_over_24_fails(self):
        """E^3: chi/24 = 0 does NOT match kappa = 3."""
        assert kappa_from_chi_top_over_24(0) != Fraction(3)

    def test_conifold_chi_over_24_fails(self):
        """Conifold: chi/24 = 1/12 does NOT match kappa = 1."""
        assert kappa_from_chi_top_over_24(2) != Fraction(1)

    def test_chi_over_24_conjecture_test_suite(self):
        """Run the full chi/24 conjecture test suite."""
        tests = chi_over_24_conjecture_tests()
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(tests) >= 5

        # Quintic should match
        quintic_test = [t for t in tests if t.name == "quintic"][0]
        assert quintic_test.matches

        # K3 x E should fail
        k3e_test = [t for t in tests if t.name == "K3 x E"][0]
        assert not k3e_test.matches
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert k3e_test.discrepancy == Fraction(5)

    def test_no_universal_formula_exists(self):
        """Verify that no single Hodge formula works universally."""
        analysis = correct_kappa_formula_analysis()
        assert analysis["universal_formula_exists"] is False

    def test_bicubic_chi_over_24(self):
        """Bicubic: chi = -144, chi/24 = -6."""
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert kappa_from_chi_top_over_24(-144) == Fraction(-6)

    def test_2222_chi_over_24(self):
        """(2,2,2,2) in P^7: chi = -128, chi/24 = -16/3."""
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert kappa_from_chi_top_over_24(-128) == Fraction(-16, 3)


# =====================================================================
# Section 5: HODGE FORMULAS
# =====================================================================

class TestHodgeFormulas:
    """Test the various Hodge-based kappa formulas."""

    def test_bcov_quintic(self):
        """BCOV genus-1 for quintic: (3+1+200/12)/2 = 31/3."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_bcov_genus1(-200, 1) == Fraction(31, 3)

    def test_bcov_k3xe(self):
        """BCOV genus-1 for K3xE: (3+21)/2 = 12."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_bcov_genus1(0, 21) == Fraction(12)

    def test_bcov_ne_kappa_quintic(self):
        """BCOV c_1 = 31/3 != kappa = -25/3 for the quintic.

        The BCOV coefficient includes holomorphic anomaly corrections
        beyond the constant-map contribution.
        """
        bcov = kappa_from_bcov_genus1(-200, 1)
        assert bcov != Fraction(-25, 3)

    def test_k3_fibration_weight(self):
        """K3 fibration: (24-4)/4 = 5."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_k3_fibration_weight(24) == Fraction(5)

    def test_toric_vertex_count_c3(self):
        """C^3: 1 vertex -> kappa = 1/2.
        BUT actual C^3 kappa = 1.  The vertex count formula
        applies to LOCAL CY3 = Tot(K_S -> S), not bare C^3.
        """
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_toric_vertex_count(1) == Fraction(1, 2)

    def test_toric_vertex_count_p2(self):
        """P^2: 3 vertices -> kappa = 3/2."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_toric_vertex_count(3) == Fraction(3, 2)

    def test_toric_vertex_count_p1xp1(self):
        """P^1xP^1: 4 vertices -> kappa = 2."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_toric_vertex_count(4) == Fraction(2)

    def test_macmahon_c3(self):
        """MacMahon: exponent 1 -> kappa = 1."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_macmahon_exponent(Fraction(1)) == Fraction(1)

    def test_chi_over_2_conifold(self):
        """chi_top/2 for conifold: 2/2 = 1."""
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert kappa_from_chi_top_over_2(2) == Fraction(1)

    def test_chi_over_2_p2(self):
        """chi_top/2 for P^2: 3/2."""
        # VERIFIED [DC] Euler characteristic [LC] Vol I landscape_census.tex
        assert kappa_from_chi_top_over_2(3) == Fraction(3, 2)

    def test_hodge_candidates_quintic(self):
        """Test Hodge candidate formulas for the quintic."""
        candidates = kappa_hodge_candidates(1, 101)
        # VERIFIED [DC] Euler characteristic formula [LC] Vol I landscape_census.tex
        assert candidates["chi_over_24"] == Fraction(-25, 3)
        # VERIFIED [DC] Euler characteristic formula [LC] Vol I landscape_census.tex
        assert candidates["chi_O_X"] == Fraction(1)  # arithmetic genus always 1

    def test_hodge_candidates_bicubic(self):
        """Test Hodge candidates for the bicubic."""
        candidates = kappa_hodge_candidates(1, 73)
        # VERIFIED [DC] Euler characteristic formula [LC] Vol I landscape_census.tex
        assert candidates["chi_over_24"] == Fraction(-6)


# =====================================================================
# Section 6: PRODUCT FORMULAS
# =====================================================================

class TestProductFormulas:
    """Test kappa behavior under products."""

    def test_additive_for_independent_sum(self):
        """kappa(A+B) = kappa(A) + kappa(B) for independent algebras."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_product_additive(Fraction(2), Fraction(3)) == Fraction(5)

    def test_e_cubed_is_additive(self):
        """E^3: kappa = 1 + 1 + 1 = 3."""
        kappa = kappa_product_additive(
            kappa_product_additive(Fraction(1), Fraction(1)),
            Fraction(1),
        )
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa == Fraction(3)

    def test_k3xe_not_additive(self):
        """K3 x E: kappa = 5 != 2 + 1 = 3."""
        kappa_additive = kappa_product_additive(Fraction(2), Fraction(1))
        assert kappa_additive != Fraction(5)

    def test_k3xe_cross_term(self):
        """K3 x E cross term: 5 - 2 - 1 = 2."""
        cross = kappa_product_cross_term(Fraction(2), Fraction(1), Fraction(5))
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert cross == Fraction(2)

    def test_e_squared_additive(self):
        """E x E: kappa = 1 + 1 = 2 (no cross-term for abelian varieties)."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_product_additive(Fraction(1), Fraction(1)) == Fraction(2)

    def test_cross_term_zero_for_abelian(self):
        """Abelian varieties: cross term = 0."""
        cross = kappa_product_cross_term(Fraction(1), Fraction(1), Fraction(2))
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert cross == Fraction(0)


# =====================================================================
# Section 7: ORBIFOLD AND RESOLUTION
# =====================================================================

class TestOrbifoldResolution:
    """Test kappa under orbifold and crepant resolution."""

    def test_c3_z3_orbifold(self):
        """C^3/Z_3: kappa = 1/3."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_orbifold(Fraction(1), 3) == Fraction(1, 3)

    def test_c3_z2_orbifold(self):
        """C^3/Z_2: kappa = 1/2."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_orbifold(Fraction(1), 2) == Fraction(1, 2)

    def test_c3_z5_orbifold(self):
        """C^3/Z_5: kappa = 1/5."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_orbifold(Fraction(1), 5) == Fraction(1, 5)

    def test_orbifold_preserves_sign(self):
        """Orbifold of negative kappa stays negative."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_orbifold(Fraction(-6), 3) == Fraction(-2)

    def test_crepant_resolution_generic(self):
        """Generic crepant resolution: add exceptional contributions."""
        result = kappa_crepant_resolution(
            Fraction(1, 3),  # orbifold kappa
            2,               # 2 exceptional curves
            Fraction(1, 2),  # 1/2 per curve
        )
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert result == Fraction(4, 3)  # 1/3 + 2 * 1/2

    def test_orbifold_trivial_group(self):
        """Trivial orbifold: kappa unchanged."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_orbifold(Fraction(5), 1) == Fraction(5)


# =====================================================================
# Section 8: SHADOW TOWER from glued kappa
# =====================================================================

class TestShadowTower:
    """Test genus-g shadow amplitudes from glued kappa."""

    def test_f1_c3(self):
        """C^3: F_1 = 1/24."""
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert shadow_amplitude(Fraction(1), 1) == Fraction(1, 24)

    def test_f2_c3(self):
        """C^3: F_2 = 7/5760."""
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert shadow_amplitude(Fraction(1), 2) == Fraction(7, 5760)

    def test_f1_conifold(self):
        """Conifold: F_1 = 1/24."""
        result = kappa_from_nerve(conifold_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert shadow_amplitude(result.kappa_ch, 1) == Fraction(1, 24)

    def test_f1_k3xe(self):
        """K3 x E: F_1 = 5/24."""
        result = kappa_from_nerve(k3_times_e_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert shadow_amplitude(result.kappa_ch, 1) == Fraction(5, 24)

    def test_f1_quintic(self):
        """Quintic: F_1 = -25/(3*24) = -25/72."""
        result = kappa_from_nerve(quintic_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert shadow_amplitude(result.kappa_ch, 1) == Fraction(-25, 72)

    def test_f1_e_cubed(self):
        """E^3: F_1 = 3/24 = 1/8."""
        result = kappa_from_nerve(e_cubed_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert shadow_amplitude(result.kappa_ch, 1) == Fraction(1, 8)

    def test_shadow_tower_c3(self):
        """Full shadow tower for C^3."""
        tower = shadow_tower_from_gluing(c3_atlas(), 5)
        # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
        assert tower[1] == Fraction(1, 24)
        # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
        assert tower[2] == Fraction(7, 5760)
        # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
        assert tower[3] == Fraction(31, 967680)

    def test_shadow_tower_k3xe(self):
        """Full shadow tower for K3 x E."""
        tower = shadow_tower_from_gluing(k3_times_e_atlas(), 3)
        # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
        assert tower[1] == Fraction(5, 24)
        # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
        assert tower[2] == Fraction(35, 5760)
        # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
        assert tower[3] == Fraction(155, 967680)

    def test_shadow_tower_linearity(self):
        """F_g(A) is linear in kappa: F_g(2A) = 2 F_g(A)."""
        for g in [1, 2, 3]:
            f_1 = shadow_amplitude(Fraction(1), g)
            f_5 = shadow_amplitude(Fraction(5), g)
            # VERIFIED [DC] Faber-Pandharipande genus formula [LC] Vol I landscape_census.tex
            assert f_5 == 5 * f_1

    def test_f_g_sign_from_kappa(self):
        """F_g > 0 when kappa > 0 (A-hat coefficients are positive)."""
        for g in range(1, 6):
            f = shadow_amplitude(Fraction(5), g)
            # VERIFIED [DC] kappa computation [LC] Vol I landscape_census.tex
            assert f > 0

    def test_f_g_negative_for_quintic(self):
        """F_g < 0 for the quintic (kappa < 0)."""
        for g in range(1, 6):
            f = shadow_amplitude(Fraction(-25, 3), g)
            # VERIFIED [DC] genus free energy [LC] Vol I landscape_census.tex
            assert f < 0

    def test_a_hat_coefficients_positive(self):
        """All tabulated A-hat coefficients are positive."""
        for g, coeff in A_HAT_COEFFS.items():
            # VERIFIED [DC] genus tower [LC] Vol I landscape_census.tex
            assert coeff > 0, f"A-hat coefficient at genus {g} not positive"


# =====================================================================
# Section 9: TORIC LANDSCAPE
# =====================================================================

class TestToricLandscape:
    """Test the toric CY3 landscape table."""

    def test_landscape_nonempty(self):
        """Landscape table has entries."""
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(TORIC_CY3_LANDSCAPE) >= 10

    def test_c3_in_landscape(self):
        """C^3 is in the landscape."""
        names = [e.name for e in TORIC_CY3_LANDSCAPE]
        assert "C^3" in names

    def test_all_kappas_positive(self):
        """All toric CY3 kappas are positive (non-compact, no negative chi)."""
        for entry in TORIC_CY3_LANDSCAPE:
            # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
            assert entry.kappa > 0, f"{entry.name} has non-positive kappa"

    def test_toric_table_generation(self):
        """Table generation works."""
        table = toric_landscape_table()
        # VERIFIED [DC] toric data [LC] Vol I landscape_census.tex
        assert len(table) >= 10

    def test_vertex_count_formula_for_local_surfaces(self):
        """Verify kappa = chi_base/2 for local surfaces in the landscape."""
        for entry in TORIC_CY3_LANDSCAPE:
            expected = Fraction(entry.chi_compact_base, 2)
            if entry.name not in ("C^3", "C^3/Z_3 orbifold", "C^3/Z_2"):
                # For local surfaces Tot(K_S -> S): kappa = chi(S)/2
                assert entry.kappa == expected, \
                    f"{entry.name}: kappa={entry.kappa} != chi/2={expected}"

    def test_del_pezzo_kappas(self):
        """Del Pezzo surfaces dP_k have chi = k+3, kappa = (k+3)/2."""
        dp_entries = {e.name: e for e in TORIC_CY3_LANDSCAPE
                      if "dP" in e.name}
        for name, entry in dp_entries.items():
            # dP_1: chi=4, dP_2: chi=5, dP_3: chi=6
            assert entry.chi_compact_base == entry.n_vertices


# =====================================================================
# Section 10: CROSS-VERIFICATION with modular_cy_characteristic
# =====================================================================

class TestCrossVerification:
    """Verify consistency with modular_cy_characteristic module."""

    def test_cross_verify_all(self):
        """All cross-verifications pass."""
        results = cross_verify_kappa_values()
        for name, ok in results.items():
            assert ok, f"Cross-verification failed for {name}"

    def test_conifold_kappa_from_nerve_matches(self):
        """Nerve formula for conifold matches known value."""
        result = kappa_from_nerve(conifold_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(1)

    def test_k3xe_kappa_from_nerve_matches(self):
        """Nerve formula for K3xE matches known value."""
        result = kappa_from_nerve(k3_times_e_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(5)

    def test_quintic_kappa_from_nerve_matches(self):
        """Nerve formula for quintic matches known value."""
        result = kappa_from_nerve(quintic_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(-25, 3)


# =====================================================================
# Section 11: WALL CROSSING
# =====================================================================

class TestWallCrossing:
    """Test kappa behavior under wall crossing."""

    def test_conifold_wall_crossing_continuous(self):
        """Kappa is continuous across the conifold wall."""
        wc = conifold_wall_crossing()
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert wc.delta_kappa == Fraction(0)
        assert wc.kappa_before == wc.kappa_after

    def test_wall_crossing_preserves_kappa(self):
        """Wall crossing preserves kappa (homotopy invariant)."""
        wc = conifold_wall_crossing()
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert wc.kappa_before == Fraction(1)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert wc.kappa_after == Fraction(1)


# =====================================================================
# Section 12: CICY TABLE
# =====================================================================

class TestCICY:
    """Test Complete Intersection CY3 kappa values."""

    def test_cicy_table_nonempty(self):
        """CICY table has entries."""
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(STANDARD_CICYS) >= 5

    def test_cicy_chi_consistency(self):
        """All CICYs have chi = 2(h11 - h21)."""
        table = cicy_kappa_table()
        for entry in table:
            assert entry["chi_consistent"], \
                f"{entry['name']}: chi check failed"

    def test_quintic_in_cicys(self):
        """Quintic is in the CICY list."""
        names = [c.name for c in STANDARD_CICYS]
        assert "quintic" in names

    def test_cicy_kappa_values(self):
        """All CICY kappas are chi/24."""
        for cicy in STANDARD_CICYS:
            # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
            assert cicy.kappa_conj == Fraction(cicy.chi_top, 24), \
                f"{cicy.name}: kappa_conj != chi/24"

    def test_bicubic_kappa(self):
        """Bicubic: chi = -144, kappa = -6."""
        bicubic = [c for c in STANDARD_CICYS if c.name == "bicubic"][0]
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert bicubic.kappa_conj == Fraction(-6)

    def test_quintic_kappa_not_integer(self):
        """Quintic kappa = -25/3 is NOT an integer."""
        quintic = [c for c in STANDARD_CICYS if c.name == "quintic"][0]
        assert quintic.kappa_conj.denominator != 1


# =====================================================================
# Section 13: PROOF STRUCTURE
# =====================================================================

class TestProofStructure:
    """Verify the homotopy invariance proof has all components."""

    def test_proof_has_four_steps(self):
        """The proof has steps a, b, c, d."""
        proof = kappa_gluing_invariance_proof()
        assert isinstance(proof, HomotopyInvarianceProof)
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(proof.step_a) > 0
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(proof.step_b) > 0
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(proof.step_c) > 0
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(proof.step_d) > 0
        # VERIFIED [DC] structural property [LC] Vol I landscape_census.tex
        assert len(proof.conclusion) > 0

    def test_proof_references_F1(self):
        """The proof mentions F_1 (the genus-1 shadow)."""
        proof = kappa_gluing_invariance_proof()
        assert "F_1" in proof.step_a or "F_1" in proof.step_b

    def test_proof_references_hocolim(self):
        """The proof mentions hocolim."""
        proof = kappa_gluing_invariance_proof()
        assert "hocolim" in proof.step_c or "Cech" in proof.step_c

    def test_proof_references_descent(self):
        """The proof mentions descent."""
        proof = kappa_gluing_invariance_proof()
        assert "descent" in proof.step_d


# =====================================================================
# Section 14: MULTI-PATH VERIFICATION
# =====================================================================

class TestMultiPath:
    """Multi-path verification of F_1 for each CY3."""

    def test_c3_multi_path(self):
        """C^3: F_1 = 1/24 by definition."""
        result = f1_multi_path_verification("C^3", Fraction(1))
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result["F1_from_kappa"] == Fraction(1, 24)

    def test_quintic_multi_path(self):
        """Quintic: F_1 from kappa and BCOV."""
        result = f1_multi_path_verification(
            "quintic", Fraction(-25, 3),
            chi_top=-200, h11=1,
        )
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result["F1_from_kappa"] == Fraction(-25, 72)
        # chi/24 path should match since kappa = chi/24
        assert result["chi_path_matches"]

    def test_k3xe_multi_path(self):
        """K3xE: chi path does NOT match (chi=0, kappa=5)."""
        result = f1_multi_path_verification(
            "K3xE", Fraction(5),
            chi_top=0, h11=21,
        )
        assert not result["chi_path_matches"]

    def test_conifold_multi_path(self):
        """Conifold: F_1 from two paths."""
        result = f1_multi_path_verification(
            "conifold", Fraction(1),
            chi_top=2, h11=1,
        )
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result["F1_from_kappa"] == Fraction(1, 24)

    def test_local_p2_multi_path(self):
        """Local P^2: F_1 = 3/48 = 1/16."""
        result = f1_multi_path_verification(
            "local_P^2", Fraction(3, 2),
        )
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result["F1_from_kappa"] == Fraction(3, 48)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result["F1_from_kappa"] == Fraction(1, 16)


# =====================================================================
# Additional targeted tests
# =====================================================================

class TestKappaProperties:
    """Test mathematical properties of kappa."""

    def test_kappa_is_rational(self):
        """All computed kappas are rational numbers."""
        atlases = [
            c3_atlas(), conifold_atlas(), local_p2_atlas(),
            k3_times_e_atlas(), quintic_atlas(), e_cubed_atlas(),
        ]
        for atlas in atlases:
            result = kappa_from_nerve(atlas)
            assert isinstance(result.kappa_ch, Fraction)

    def test_kappa_nonzero_for_nontrivial_cy3(self):
        """All non-product CY3s with compact geometry have nonzero kappa."""
        for atlas in [c3_atlas(), conifold_atlas(), local_p2_atlas(),
                      k3_times_e_atlas(), spp_atlas()]:
            result = kappa_from_nerve(atlas)
            assert result.kappa_ch != 0, \
                f"{atlas.name}: kappa should be nonzero"

    def test_kappa_positive_for_noncompact(self):
        """Non-compact CY3s have positive kappa."""
        for atlas in [c3_atlas(), conifold_atlas(), local_p2_atlas(),
                      spp_atlas()]:
            result = kappa_from_nerve(atlas)
            # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
            assert result.kappa_ch > 0, \
                f"{atlas.name}: non-compact should have positive kappa"

    def test_quintic_kappa_negative(self):
        """The quintic has negative kappa (chi < 0)."""
        result = kappa_from_nerve(quintic_atlas())
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch < 0

    def test_f1_from_kappa_universal(self):
        """F_1 = kappa/24 is the universal genus-1 formula."""
        for kappa_val in [Fraction(1), Fraction(5), Fraction(-25, 3),
                          Fraction(3, 2), Fraction(2), Fraction(3)]:
            f1 = shadow_amplitude(kappa_val, 1)
            assert f1 == kappa_val / 24

    def test_f2_from_kappa_universal(self):
        """F_2 = 7*kappa/5760 is the universal genus-2 formula."""
        for kappa_val in [Fraction(1), Fraction(5), Fraction(-25, 3)]:
            f2 = shadow_amplitude(kappa_val, 2)
            # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
            assert f2 == 7 * kappa_val / 5760


class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_empty_intersections(self):
        """Atlas with no intersections: kappa = sum of chart kappas."""
        charts = [CY3Chart(f"c{i}", Fraction(i + 1), "G", 1, None) for i in range(5)]
        atlas = CY3Atlas("test", charts, {}, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(15)  # 1+2+3+4+5

    def test_hirzebruch_large_n(self):
        """Hirzebruch surface F_n for large n: still kappa = 2."""
        for n in [5, 10, 20, 100]:
            result = kappa_from_nerve(local_hirzebruch_atlas(n))
            # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
            assert result.kappa_ch == Fraction(2), \
                f"F_{n}: kappa should be 2"

    def test_kappa_global_type(self):
        """kappa_ch is always a Fraction."""
        result = kappa_from_nerve(c3_atlas())
        assert type(result.kappa_ch) is Fraction

    def test_n_charts_recorded(self):
        """Number of charts is recorded in the result."""
        result = kappa_from_nerve(conifold_atlas())
        # VERIFIED [DC] chart decomposition [LC] Vol I landscape_census.tex
        assert result.n_charts == 2

    def test_atlas_name_recorded(self):
        """Atlas name is recorded in the result."""
        result = kappa_from_nerve(c3_atlas())
        # VERIFIED [DC] chart decomposition [LC] Vol I landscape_census.tex
        assert result.atlas_name == "C^3"


class TestConsistencyWithExistingModules:
    """Verify consistency with values in toric_cy3_e1_landscape.py and
    modular_cy_characteristic.py."""

    def test_c3_kappa_matches_w1inf(self):
        """C^3: kappa = 1 matches W_{1+inf} from e1_universality."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_nerve(c3_atlas()).kappa_ch == Fraction(1)

    def test_conifold_kappa_matches_gl11(self):
        """Conifold: kappa = 1 matches gl(1|1) VOA."""
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_nerve(conifold_atlas()).kappa_ch == Fraction(1)

    def test_local_p2_matches_toric_landscape(self):
        """Local P^2: kappa = 3/2 matches toric landscape."""
        # From toric_cy3_e1_landscape.py header
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_nerve(local_p2_atlas()).kappa_ch == Fraction(3, 2)

    def test_k3xe_matches_igusa_weight(self):
        """K3 x E: kappa = 5 matches weight of Delta_5."""
        # From modular_cy_characteristic.py
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_nerve(k3_times_e_atlas()).kappa_ch == Fraction(5)

    def test_quintic_matches_bcov(self):
        """Quintic: kappa = -25/3 matches chi/24."""
        # From modular_cy_characteristic.py: chi_cy_quintic
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert kappa_from_nerve(quintic_atlas()).kappa_ch == Fraction(-25, 3)

    def test_a_hat_coefficients_match_vol1(self):
        """A-hat coefficients match Vol I values."""
        # From Vol I: lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680
        # VERIFIED [DC] characteristic class [LC] Vol I
        assert A_HAT_COEFFS[1] == Fraction(1, 24)
        # VERIFIED [DC] characteristic class [LC] Vol I
        assert A_HAT_COEFFS[2] == Fraction(7, 5760)
        # VERIFIED [DC] characteristic class [LC] Vol I
        assert A_HAT_COEFFS[3] == Fraction(31, 967680)
        # VERIFIED [DC] characteristic class [LC] Vol I
        assert A_HAT_COEFFS[4] == Fraction(127, 154828800)


class TestNerveFormulaAlgebraicProperties:
    """Test algebraic properties of the nerve formula."""

    def test_nerve_formula_is_additive_on_disjoint_union(self):
        """For disjoint union: kappa(X sqcup Y) = kappa(X) + kappa(Y)."""
        a1 = c3_atlas()
        a2 = conifold_atlas()
        k1 = kappa_from_nerve(a1).kappa_ch
        k2 = kappa_from_nerve(a2).kappa_ch
        # Combined: just list all charts, no new intersections
        combined_charts = list(a1.charts) + list(a2.charts)
        # Shift intersection indices for the second atlas
        shifted = {frozenset({i + len(a1.charts) for i in S}): v
                   for S, v in a2.intersections.items()}
        combined = CY3Atlas("combined", combined_charts, shifted, None, None)
        k_combined = kappa_from_nerve(combined).kappa_ch
        assert k_combined == k1 + k2

    def test_nerve_formula_scales_with_kappa(self):
        """Scaling all chart kappas by c scales the result by c."""
        c = Fraction(7, 3)
        chart = CY3Chart("test", Fraction(5) * c, "G", 1, None)
        atlas = CY3Atlas("test", [chart], {}, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(5) * c

    def test_nerve_with_all_zero_walls(self):
        """When all wall kappas are zero, nerve = sum of charts."""
        charts = [CY3Chart(f"c{i}", Fraction(i + 1), "G", 1, None) for i in range(3)]
        atlas = CY3Atlas("test", charts, {
            frozenset({0, 1}): Fraction(0),
            frozenset({0, 2}): Fraction(0),
            frozenset({1, 2}): Fraction(0),
        }, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(6)  # 1+2+3

    def test_nerve_cancellation(self):
        """Charts + walls can cancel to zero."""
        c1 = CY3Chart("a", Fraction(3), "G", 1, None)
        c2 = CY3Chart("b", Fraction(4), "G", 1, None)
        atlas = CY3Atlas("test", [c1, c2], {
            frozenset({0, 1}): Fraction(7),  # wall kappa = sum of charts
        }, None, None)
        result = kappa_from_nerve(atlas)
        # VERIFIED [DC] kappa formula [LC] Vol I landscape_census.tex
        assert result.kappa_ch == Fraction(0)


class TestShadowAmplitudeProperties:
    """Test properties of shadow amplitudes."""

    def test_shadow_genus_invalid(self):
        """Invalid genus raises error."""
        with pytest.raises(ValueError):
            shadow_amplitude(Fraction(1), 0)

    def test_shadow_genus_too_high(self):
        """Genus beyond tabulated range raises error."""
        with pytest.raises(ValueError):
            shadow_amplitude(Fraction(1), 100)

    def test_shadow_zero_kappa(self):
        """F_g = 0 when kappa = 0."""
        for g in range(1, 6):
            # VERIFIED [DC] kappa computation [LC] Vol I landscape_census.tex
            assert shadow_amplitude(Fraction(0), g) == Fraction(0)

    def test_shadow_additivity(self):
        """F_g(kappa_1 + kappa_2) = F_g(kappa_1) + F_g(kappa_2)."""
        k1, k2 = Fraction(3), Fraction(7)
        for g in range(1, 6):
            f_sum = shadow_amplitude(k1 + k2, g)
            f_parts = shadow_amplitude(k1, g) + shadow_amplitude(k2, g)
            assert f_sum == f_parts
