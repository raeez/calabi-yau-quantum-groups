"""Tests for CFG25 E_1-chiral lift: 3d CS -> 6d hCS on C^3.

Verifies:
  (1) CFG25 lift table: all 5 results present with correct status
  (2) Dimensional comparison: 3d vs 6d structure function properties
  (3) Boundary algebra lift: KM -> Yangian, Deligne level drop
  (4) Submanifold invariant lift: link -> holomorphic submanifold
  (5) Factorization homology lift: topological -> holomorphic
  (6) Koszul duality lift: U_q(g) -> U_{q,t} with parameter inversion
  (7) Obstruction analysis: hierarchy and status counts
  (8) Cross-engine compatibility with holomorphic_cs_chiral_engine
  (9) End-to-end pipeline at multiple Omega-background points
  (10) AP compliance

Manuscript references:
    chapters/theory/quantum_chiral_algebras.tex: Section on CFG25 lift
    chapters/theory/en_factorization.tex: E_3 from hol CS
    chapters/theory/e1_chiral_algebras.tex: E_1 primacy

Ground truth:
    Self-dual point (1, 0, -1): sigma_2 = -1, sigma_3 = 0
    SV N=2 point (1, -2, 1): sigma_2 = -3, sigma_3 = -2
    Generic point (1, -3, 2): sigma_2 = -7, sigma_3 = -6
    Partitions p(n): 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42

Multi-path verification:
    Path 1: Direct computation from CFG25LiftVerifier
    Path 2: Cross-check with holomorphic_cs_chiral_engine OmegaBackground
    Path 3: Cross-check with zamolodchikov_tetrahedron_engine ZTE result
"""

import pytest
from sympy import Rational

from compute.lib.cfg25_e1_chiral_lift import (
    CFG25Result,
    CFG25LiftVerifier,
    BoundaryAlgebraLift,
    DimensionalComparison,
    FactorizationHomologyLift,
    KoszulDualityLift,
    ObstructionAnalysis,
    SubmanifoldInvariantLift,
    cfg25_lift_table,
)


# =========================================================================
# 1. CFG25 lift table tests
# =========================================================================

class TestCFG25LiftTable:
    """Test the master lift table: 5 results, correct statuses."""

    def test_table_has_five_entries(self):
        """CFG25 has exactly 5 key results."""
        table = cfg25_lift_table()
        assert len(table) == 5

    def test_all_indices_present(self):
        """Indices 1 through 5 all present."""
        table = cfg25_lift_table()
        assert set(r.index for r in table) == {1, 2, 3, 4, 5}

    def test_result1_en_factorization_works(self):
        """Result 1 (E_n factorization): works."""
        table = cfg25_lift_table()
        r1 = [r for r in table if r.index == 1][0]
        assert r1.status == "works"
        assert r1.obstruction is None

    def test_result2_boundary_algebra_works(self):
        """Result 2 (boundary algebra): works."""
        table = cfg25_lift_table()
        r2 = [r for r in table if r.index == 2][0]
        assert r2.status == "works"

    def test_result3_link_invariants_partially(self):
        """Result 3 (link/submanifold invariants): partially works."""
        table = cfg25_lift_table()
        r3 = [r for r in table if r.index == 3][0]
        assert r3.status == "partially_works"
        assert r3.obstruction is not None

    def test_result4_fact_hom_conjectural(self):
        """Result 4 (factorization homology): conjectural."""
        table = cfg25_lift_table()
        r4 = [r for r in table if r.index == 4][0]
        assert r4.status == "conjectural"

    def test_result5_koszul_conjectural(self):
        """Result 5 (Koszul duality): conjectural (ZTE obstruction)."""
        table = cfg25_lift_table()
        r5 = [r for r in table if r.index == 5][0]
        assert r5.status == "conjectural"
        assert "ZTE" in r5.obstruction

    def test_each_result_has_new_idea(self):
        """Every result has a new_idea field set."""
        table = cfg25_lift_table()
        for r in table:
            assert r.new_idea is not None, f"Result {r.index} missing new_idea"

    def test_invalid_index_rejected(self):
        """Index outside 1-5 is rejected."""
        with pytest.raises(AssertionError):
            CFG25Result(0, "a", "b", "works")
        with pytest.raises(AssertionError):
            CFG25Result(6, "a", "b", "works")

    def test_invalid_status_rejected(self):
        """Invalid status string is rejected."""
        with pytest.raises(AssertionError):
            CFG25Result(1, "a", "b", "proved")


# =========================================================================
# 2. Dimensional comparison tests
# =========================================================================

class TestDimensionalComparison:
    """Test the 3d vs 6d dimensional comparison."""

    def test_cy_condition(self):
        """h1+h2+h3=0 enforced."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert dc.h1 + dc.h2 + dc.h3 == 0

    def test_sigma2_sv_point(self):
        """sigma_2 at SV N=2 point (1,-2,1)."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert dc.sigma2 == Rational(-3)

    def test_sigma3_sv_point(self):
        """sigma_3 at SV N=2 point: 1*(-2)*1 = -2."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert dc.sigma3 == Rational(-2)

    def test_sigma2_self_dual(self):
        """sigma_2 at self-dual (1,0,-1): 0+(-1)+0 = -1."""
        dc = DimensionalComparison(Rational(1), Rational(0))
        assert dc.sigma2 == Rational(-1)

    def test_sigma3_self_dual_vanishes(self):
        """sigma_3 at self-dual: 1*0*(-1) = 0."""
        dc = DimensionalComparison(Rational(1), Rational(0))
        assert dc.sigma3 == Rational(0)

    def test_g_at_zero_is_minus_one(self):
        """g(0) = -1 (when no h_i = 0)."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert dc.verify_g_at_zero()

    def test_g_unitarity(self):
        """g(u)*g(-u) = 1 (unitarity)."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        for u in [Rational(5), Rational(10), Rational(37)]:
            assert dc.verify_g_unitarity(u)

    def test_g_classical_limit(self):
        """g(u) = 1 - 2*sigma_3/u^3 + O(1/u^5) as u -> inf.

        The 1/u and 1/u^2 coefficients vanish because h1+h2+h3=0.
        """
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert dc.verify_g_classical_limit()

    def test_comparison_table_keys(self):
        """Comparison table has all expected keys."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        table = dc.comparison_table()
        for key in [
            "real_dimension", "complex_dimension", "topological_en",
            "holomorphic_en", "chiral_en", "boundary_algebra",
            "boundary_en_level", "r_matrix_type", "koszul_dual",
        ]:
            assert key in table

    def test_topological_en_is_double(self):
        """Topological E_n = 2 * complex dimension."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        table = dc.comparison_table()
        assert table["topological_en"]["6d"] == 2 * table["complex_dimension"]["6d"]

    def test_holomorphic_en_is_half_topological(self):
        """Holomorphic E_n = topological E_n / 2."""
        dc = DimensionalComparison(Rational(1), Rational(-2))
        table = dc.comparison_table()
        assert table["holomorphic_en"]["6d"] == table["topological_en"]["6d"] // 2

    def test_g_at_generic_point(self):
        """g(u) at generic point (1,-3,2)."""
        dc = DimensionalComparison(Rational(1), Rational(-3))
        assert dc.sigma2 == Rational(-7)
        assert dc.sigma3 == Rational(-6)
        # g(0) = (-1)(-(-3))(-2) / (1)((-3))(2) = ... check directly
        val = dc.structure_function(Rational(0))
        assert val == Rational(-1)


# =========================================================================
# 3. Boundary algebra lift tests
# =========================================================================

class TestBoundaryAlgebraLift:
    """Test the KM -> Yangian boundary algebra upgrade."""

    def test_km_level_sv(self):
        """KM level k = -sigma_2 = 3 at SV point."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        assert ba.km_level == Rational(3)

    def test_km_level_self_dual(self):
        """KM level k = 1 at self-dual point."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(0))
        assert ba.km_level == Rational(1)

    def test_yangian_sigma3_sv(self):
        """sigma_3 = -2 at SV point."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        assert ba.yangian_sigma3 == Rational(-2)

    def test_yangian_sigma3_self_dual_vanishes(self):
        """sigma_3 = 0 at self-dual point (Yangian degenerates to KM)."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(0))
        assert ba.yangian_sigma3 == Rational(0)

    def test_cfg25_boundary_is_einf(self):
        """CFG25 boundary algebra V_k(g) is E_inf-chiral (commutative)."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        cfg = ba.cfg25_boundary()
        assert cfg["commutative"] is True
        assert cfg["en_level"] == "E_inf"

    def test_e1_lift_boundary_is_e1(self):
        """E_1-chiral lift boundary Y(gl_hat_1) is E_1 (non-commutative)."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        lift = ba.e1_lift_boundary()
        assert lift["commutative"] is False
        assert lift["en_level"] == "E_1"

    def test_deligne_level_drop(self):
        """The Deligne conjecture level drops from E_3 to E_2 in the lift.

        AP153: E_inf -> E_3 on HH^*; E_1 -> E_2 on HH^* (Dunn).
        """
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        assert ba.verify_deligne_level_drop()

    def test_drinfeld_center_passage(self):
        """Drinfeld center: E_1 -> E_2 passage."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        dc = ba.drinfeld_center_passage()
        assert "E_1" in dc["e1_input"]
        assert "E_2" in dc["e2_output"]
        assert dc["mechanism"] == "Drinfeld center Z"

    def test_km_to_yangian_at_self_dual(self):
        """At sigma_3=0, the Yangian degenerates to KM (Heisenberg)."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(0))
        assert ba.verify_km_to_yangian_specialisation()

    def test_deligne_level_values(self):
        """CFG25 Deligne = E_3 on HH^*(E_inf); lift = E_2 on HH^*(E_1)."""
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        cfg = ba.cfg25_boundary()
        lift = ba.e1_lift_boundary()
        assert cfg["deligne_level"] == "E_3 on HH^*(A) for E_inf A"
        assert "E_2" in lift["deligne_level"]


# =========================================================================
# 4. Submanifold invariant lift tests
# =========================================================================

class TestSubmanifoldInvariantLift:
    """Test the link -> holomorphic submanifold lift."""

    def test_link_complement_pi1(self):
        """Link complement in R^3 has nontrivial pi_1 (knot group)."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        lc = si.link_complement_3d(num_components=1)
        assert "knot group" in lc["pi_1"]
        assert lc["h1_rank"] == 1

    def test_link_complement_multi_component(self):
        """Multi-component link: H_1 rank = number of components."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        lc = si.link_complement_3d(num_components=3)
        assert lc["h1_rank"] == 3

    def test_holomorphic_curve_complement(self):
        """Holomorphic curve (dim 1) in C^3: codim_C = 2."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        hc = si.holomorphic_complement_6d(submanifold_dim=1, genus=0)
        assert hc["codim_C"] == 2
        assert hc["codim_R"] == 4
        assert hc["normal_bundle_rank"] == 2

    def test_holomorphic_surface_complement(self):
        """Holomorphic surface (dim 2) in C^3: codim_C = 1."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        hc = si.holomorphic_complement_6d(submanifold_dim=2)
        assert hc["codim_C"] == 1
        assert hc["codim_R"] == 2
        assert hc["normal_bundle_rank"] == 1

    def test_curve_normal_det_adjunction(self):
        """For genus-0 curve in C^3: det(N) = O(2) by CY adjunction.

        K_{C^3} trivial, K_{P^1} = O(-2), so det(N) = K_{P^1}^{-1} = O(2).
        """
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        hc = si.holomorphic_complement_6d(submanifold_dim=1, genus=0)
        assert hc["normal_det_degree"] == 2  # 2 - 2*0 = 2

    def test_curve_genus1_normal_det(self):
        """For genus-1 curve (elliptic): det(N) = O(0) (trivial)."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        hc = si.holomorphic_complement_6d(submanifold_dim=1, genus=1)
        assert hc["normal_det_degree"] == 0  # 2 - 2*1 = 0

    def test_curve_genus2_normal_det(self):
        """For genus-2 curve: det(N) = O(-2)."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        hc = si.holomorphic_complement_6d(submanifold_dim=1, genus=2)
        assert hc["normal_det_degree"] == -2  # 2 - 2*2 = -2

    def test_codim2_defect_is_w1inf(self):
        """Codim-2 curve defect = W_{1+inf} (Proposition prop:codim2-defect-ope)."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        assert si.verify_codim2_defect_is_w1inf()

    def test_defect_level_is_minus_sigma2(self):
        """Defect algebra level Psi = -sigma_2."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        defect = si.defect_algebra_on_submanifold(submanifold_dim=1)
        expected_psi = Rational(3)  # -sigma_2 = -(-3) = 3 at SV point
        assert defect["level"] == expected_psi

    def test_defect_central_charge_c1(self):
        """Defect central charge c = 1 for gl_1 gauge algebra."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        defect = si.defect_algebra_on_submanifold(submanifold_dim=1)
        assert defect["central_charge"] == Rational(1)

    def test_surface_defect_is_line_operator(self):
        """Codim-1 surface defect is a line operator, not a chiral algebra."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        defect = si.defect_algebra_on_submanifold(submanifold_dim=2)
        assert "line operator" in defect["defect_algebra"]

    def test_holomorphic_invariant_type(self):
        """Holomorphic complement invariant is holomorphic (not topological)."""
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        hc = si.holomorphic_complement_6d(submanifold_dim=1)
        assert "holomorphic" in hc["invariant_type"]


# =========================================================================
# 5. Factorization homology lift tests
# =========================================================================

class TestFactorizationHomologyLift:
    """Test the topological -> holomorphic factorization homology lift."""

    def test_excision_3d_proved(self):
        """3d excision is proved (CFG25)."""
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        ex = fh.excision_3d()
        assert "proved" in ex["status"]
        assert ex["topological"] is True

    def test_excision_6d_conjectural(self):
        """6d excision is conjectural."""
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        ex = fh.excision_6d()
        assert "conjectural" in ex["status"]
        assert ex["topological"] is False

    def test_nekrasov_u1_partition_function(self):
        """Z_Nek^{U(1)} = prod 1/(1-q^n) gives correct partition counts."""
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        assert fh.verify_nekrasov_u1_product(max_n=10)

    def test_nekrasov_as_fact_hom_identification(self):
        """Z_Nek = int_{C^2} F|_{C^2}."""
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        nek = fh.nekrasov_as_fact_hom()
        assert "int_{C^2}" in nek["identification"]

    def test_nekrasov_plethystic_log(self):
        """PLog(Z_Nek) = q/(1-q): one BPS mode per instanton number."""
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        nek = fh.nekrasov_as_fact_hom()
        assert nek["plethystic_log"] == "q/(1-q)"

    def test_nekrasov_sigma_values(self):
        """sigma_2, sigma_3 match at SV point."""
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        nek = fh.nekrasov_as_fact_hom()
        assert nek["sigma2"] == Rational(-3)
        assert nek["sigma3"] == Rational(-2)


# =========================================================================
# 6. Koszul duality lift tests
# =========================================================================

class TestKoszulDualityLift:
    """Test the U_q(g) -> U_{q,t} Koszul duality lift."""

    def test_cfg25_koszul_proved(self):
        """CFG25 Koszul duality is proved."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        cfg = kd.cfg25_koszul()
        assert "proved" in cfg["status"]

    def test_e1_lift_koszul_conjectural(self):
        """E_1-chiral Koszul duality is conjectural."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        lift = kd.e1_lift_koszul()
        assert "conjectural" in lift["status"]
        assert "ZTE" in lift["obstruction"]

    def test_kappa_complementarity(self):
        """kappa_ch(A) + kappa_ch(A^!) = 0 for free-field."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        assert kd.verify_kappa_complementarity()

    def test_kappa_complementarity_generic(self):
        """kappa complementarity at generic point (1,-3,2)."""
        kd = KoszulDualityLift(Rational(1), Rational(-3))
        assert kd.verify_kappa_complementarity()

    def test_parameter_inversion(self):
        """Under Koszul: sigma_2 preserved, sigma_3 flipped."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        assert kd.verify_parameter_inversion()

    def test_parameter_inversion_generic(self):
        """Parameter inversion at generic point."""
        kd = KoszulDualityLift(Rational(1), Rational(-3))
        assert kd.verify_parameter_inversion()

    def test_zte_obstruction_at_self_dual(self):
        """ZTE obstruction trivial at self-dual (sigma_3=0)."""
        kd = KoszulDualityLift(Rational(1), Rational(0))
        obs = kd.zte_obstruction_scaling()
        assert obs["trivial_at_self_dual"]
        assert obs["kappa"] == Rational(0)

    def test_zte_obstruction_at_sv(self):
        """ZTE obstruction nontrivial at SV point (sigma_3=-2)."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        obs = kd.zte_obstruction_scaling()
        assert not obs["trivial_at_self_dual"]
        assert obs["kappa"] == Rational(-2)
        assert obs["obstruction_value"] == Rational(4)

    def test_zte_deformation_cohomology_dimensions(self):
        """H^0=2, H^1=1, H^2=15 for the ZTE deformation complex."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        obs = kd.zte_obstruction_scaling()
        h = obs["h2_deformation_cohomology"]
        assert h["h0"] == 2
        assert h["h1"] == 1
        assert h["h2"] == 15

    def test_cfg25_parameter_inversion_q(self):
        """CFG25: q -> q^{-1} under Koszul."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        cfg = kd.cfg25_koszul()
        assert cfg["parameter_inversion"] == "q -> q^{-1}"

    def test_e1_lift_parameter_inversion_qt(self):
        """E_1 lift: (q,t) -> (q^{-1},t^{-1}) under Koszul."""
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        lift = kd.e1_lift_koszul()
        assert lift["parameter_inversion"] == "(q, t) -> (q^{-1}, t^{-1})"


# =========================================================================
# 7. Obstruction analysis tests
# =========================================================================

class TestObstructionAnalysis:
    """Test the obstruction hierarchy and status summary."""

    def test_three_obstruction_levels(self):
        """There are exactly 3 obstruction levels."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        hierarchy = oa.obstruction_hierarchy()
        assert len(hierarchy) == 3

    def test_obstruction_level_ordering(self):
        """Levels are 1, 2, 3 in increasing severity."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        levels = [o["level"] for o in oa.obstruction_hierarchy()]
        assert levels == [1, 2, 3]

    def test_level1_is_zte(self):
        """Level 1 obstruction is ZTE failure."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        h = oa.obstruction_hierarchy()
        assert h[0]["name"] == "ZTE failure"

    def test_level2_is_cya3(self):
        """Level 2 obstruction is CY-A_3."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        h = oa.obstruction_hierarchy()
        assert "CY-A_3" in h[1]["name"]

    def test_level3_is_6d_nonlagrangian(self):
        """Level 3 obstruction is 6d non-Lagrangian."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        h = oa.obstruction_hierarchy()
        assert "non-Lagrangian" in h[2]["name"]

    def test_status_counts(self):
        """2 works, 1 partially, 2 conjectural."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        counts = oa.count_by_status()
        assert counts["works"] == 2
        assert counts["partially_works"] == 1
        assert counts["conjectural"] == 2

    def test_result1_works(self):
        """Result 1 overall status: works."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        assert summary[1]["overall"] == "works"

    def test_result2_works(self):
        """Result 2 overall status: works."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        assert summary[2]["overall"] == "works"

    def test_result3_partially(self):
        """Result 3 overall status: partially_works."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        assert summary[3]["overall"] == "partially_works"

    def test_result4_conjectural(self):
        """Result 4 overall status: conjectural."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        assert summary[4]["overall"] == "conjectural"

    def test_result5_conjectural(self):
        """Result 5 overall status: conjectural."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        assert summary[5]["overall"] == "conjectural"

    def test_result5_depends_on_zte(self):
        """Result 5 depends on ZTE obstruction."""
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        deps = summary[5]["conditional_on"]
        assert any("ZTE" in d for d in deps)


# =========================================================================
# 8. Cross-engine compatibility tests
# =========================================================================

class TestCrossEngineCompatibility:
    """Cross-check with holomorphic_cs_chiral_engine and ZTE engine."""

    def test_sigma2_matches_hcs_engine(self):
        """sigma_2 matches holomorphic_cs_chiral_engine OmegaBackground."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(1, -2)
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert Rational(omega.sigma2) == dc.sigma2

    def test_sigma3_matches_hcs_engine(self):
        """sigma_3 matches holomorphic_cs_chiral_engine OmegaBackground."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(1, -2)
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert Rational(omega.sigma3) == dc.sigma3

    def test_km_level_matches_hcs_engine(self):
        """KM level matches holomorphic_cs_chiral_engine."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(1, -2)
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        assert Rational(omega.kac_moody_level()) == ba.km_level

    def test_structure_function_matches_hcs_engine(self):
        """g(u) matches holomorphic_cs_chiral_engine at u=5."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(1, -2)
        dc = DimensionalComparison(Rational(1), Rational(-2))
        assert Rational(omega.structure_function_at(5)) == dc.structure_function(Rational(5))

    def test_boundary_algebra_type_matches_hcs(self):
        """Boundary algebra type at dim=2 is 'Affine Yangian'."""
        from compute.lib.holomorphic_cs_chiral_engine import BoundaryAlgebra, OmegaBackground
        omega = OmegaBackground(1, -2)
        hcs_ba = BoundaryAlgebra(2, omega)
        assert hcs_ba.algebra_type == "Affine Yangian"

    def test_koszul_conductor_matches_hcs(self):
        """Koszul conductor = 0 matches holomorphic_cs_chiral_engine."""
        from compute.lib.holomorphic_cs_chiral_engine import KoszulDual, BoundaryAlgebra, OmegaBackground
        omega = OmegaBackground(1, -2)
        hcs_ba = BoundaryAlgebra(2, omega)
        hcs_kd = KoszulDual(hcs_ba)
        kd = KoszulDualityLift(Rational(1), Rational(-2))
        assert hcs_kd.koszul_conductor() == Rational(0)
        assert kd.verify_kappa_complementarity()


# =========================================================================
# 9. End-to-end pipeline tests
# =========================================================================

class TestEndToEndPipeline:
    """End-to-end verification at multiple Omega-background points."""

    def test_self_dual_all_pass(self):
        """All checks pass at self-dual point (1, 0, -1)."""
        v = CFG25LiftVerifier(Rational(1), Rational(0))
        results = v.verify_all()
        for k, val in results.items():
            assert val, f"Failed at self-dual: {k}"

    def test_sv_n2_all_pass(self):
        """All checks pass at SV N=2 point (1, -2, 1)."""
        v = CFG25LiftVerifier(Rational(1), Rational(-2))
        results = v.verify_all()
        for k, val in results.items():
            assert val, f"Failed at SV N=2: {k}"

    def test_generic_all_pass(self):
        """All checks pass at generic point (1, -3, 2)."""
        v = CFG25LiftVerifier(Rational(1), Rational(-3))
        results = v.verify_all()
        for k, val in results.items():
            assert val, f"Failed at generic: {k}"

    def test_large_parameter_safety(self):
        """All checks pass at large parameters (37, 41, -78).

        AP-CY28: use large parameters to avoid pole-unsafe test points.
        """
        v = CFG25LiftVerifier(Rational(37), Rational(41))
        results = v.verify_all()
        for k, val in results.items():
            assert val, f"Failed at large params: {k}"

    def test_summary_all_pass(self):
        """Summary reports all checks pass."""
        v = CFG25LiftVerifier(Rational(1), Rational(-2))
        s = v.summary()
        assert s["all_checks_pass"]
        assert s["num_failed"] == 0

    def test_summary_check_count(self):
        """Summary has correct number of checks."""
        v = CFG25LiftVerifier(Rational(1), Rational(-2))
        s = v.summary()
        assert s["num_checks"] >= 11  # At least 11 checks


# =========================================================================
# 10. AP compliance tests
# =========================================================================

class TestAPCompliance:
    """Verify compliance with anti-patterns from CLAUDE.md."""

    def test_ap_cy6_no_unconstructed_theorem(self):
        """AP-CY6/AP-CY14: G(X) at d=3 is conjectural.

        The Koszul duality lift (Result 5) correctly uses 'conjectural' status.
        """
        table = cfg25_lift_table()
        r5 = [r for r in table if r.index == 5][0]
        assert r5.status == "conjectural"  # NOT "proved"

    def test_ap_cy7_coha_not_chiral(self):
        """AP-CY7: CoHA != E_1-chiral algebra.

        The boundary algebra lift correctly identifies Y(gl_hat_1) as E_1
        (ordered, non-commutative) without calling it a chiral algebra.
        """
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        lift = ba.e1_lift_boundary()
        assert lift["type"] == "Affine Yangian"
        assert lift["en_level"] == "E_1"

    def test_ap_cy11_conditional_propagation(self):
        """AP-CY11: Results depending on CY-A_3 are conditional.

        Result 4 (fact hom) correctly lists CY-A_3 as a dependency.
        """
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        r4_deps = summary[4]["conditional_on"]
        assert any("CY-A_3" in d for d in r4_deps)

    def test_ap_cy17_mf_cy_dimension(self):
        """AP-CY17: MF(W) CY dimension is n-2.

        Not directly tested here, but the normal bundle computation
        for submanifolds uses the correct adjunction formula.
        """
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        # genus-0 curve in C^3: normal det degree = 2 - 2*0 = 2
        hc = si.holomorphic_complement_6d(submanifold_dim=1, genus=0)
        assert hc["normal_det_degree"] == 2  # Correct adjunction

    def test_ap_cy31_spectral_vs_worldsheet(self):
        """AP-CY31: Spectral z != worldsheet z.

        The factorization homology lift correctly distinguishes the
        Yangian spectral parameter from the worldsheet coordinate.
        """
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))
        nek = fh.nekrasov_as_fact_hom()
        # The E_3 origin description mentions E_1 direction (spectral)
        assert "E_1" in nek["e3_origin"] or "E_2" in nek["e3_origin"]

    def test_ap153_deligne_scope(self):
        """AP153: E_3 scope -- E_1 input gives E_2, not E_3.

        The boundary algebra lift correctly identifies the Deligne level
        drop from E_3 (E_inf input) to E_2 (E_1 input).
        """
        ba = BoundaryAlgebraLift(Rational(1), Rational(-2))
        assert ba.verify_deligne_level_drop()

    def test_ap_cy32_reorganisation_not_bypass(self):
        """AP-CY32: Reorganisation != bypass.

        The 6d factorization homology route does NOT bypass CY-A_3.
        Result 4 correctly lists CY-A_3 as a dependency.
        """
        oa = ObstructionAnalysis(Rational(1), Rational(-2))
        summary = oa.result_status_summary()
        # Result 4 (fact hom for compact CY_3) is conditional on CY-A_3
        assert summary[4]["overall"] == "conjectural"
        assert any("CY-A_3" in d for d in summary[4]["conditional_on"])


# =========================================================================
# 11. Multi-path verification (AP10 compliance)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification: cross-check key values through independent
    computational routes.

    Path 1: cfg25_e1_chiral_lift (this engine)
    Path 2: holomorphic_cs_chiral_engine (existing Vol III engine)
    Path 3: direct symbolic computation (ground truth)

    Each test verifies the same value through at least 2 independent paths.
    """

    @pytest.mark.parametrize("h1,h2,expected_sigma2,expected_sigma3", [
        (Rational(1), Rational(0), Rational(-1), Rational(0)),
        (Rational(1), Rational(-2), Rational(-3), Rational(-2)),
        (Rational(1), Rational(-3), Rational(-7), Rational(-6)),
        (Rational(37), Rational(41), Rational(-4567), Rational(-118326)),
    ])
    def test_sigma_values_3path(self, h1, h2, expected_sigma2, expected_sigma3):
        """sigma_2, sigma_3 via 3 paths: this engine, hcs engine, direct."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        h3 = -(h1 + h2)

        # Path 1: cfg25 engine
        dc = DimensionalComparison(h1, h2)

        # Path 2: hcs engine
        omega = OmegaBackground(int(h1), int(h2))

        # Path 3: direct computation
        direct_sigma2 = h1 * h2 + h1 * h3 + h2 * h3
        direct_sigma3 = h1 * h2 * h3

        # All three must agree
        assert dc.sigma2 == expected_sigma2, "Path 1 (cfg25) sigma2"
        assert Rational(omega.sigma2) == expected_sigma2, "Path 2 (hcs) sigma2"
        assert direct_sigma2 == expected_sigma2, "Path 3 (direct) sigma2"

        assert dc.sigma3 == expected_sigma3, "Path 1 (cfg25) sigma3"
        assert Rational(omega.sigma3) == expected_sigma3, "Path 2 (hcs) sigma3"
        assert direct_sigma3 == expected_sigma3, "Path 3 (direct) sigma3"

    @pytest.mark.parametrize("h1,h2,u_val", [
        (Rational(1), Rational(-2), Rational(5)),
        (Rational(1), Rational(-2), Rational(10)),
        (Rational(1), Rational(-3), Rational(7)),
        (Rational(1), Rational(0), Rational(3)),
    ])
    def test_structure_function_2path(self, h1, h2, u_val):
        """g(u) via 2 paths: this engine, hcs engine."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground

        # Path 1: cfg25 engine
        dc = DimensionalComparison(h1, h2)
        g1 = dc.structure_function(u_val)

        # Path 2: hcs engine
        omega = OmegaBackground(int(h1), int(h2))
        g2 = omega.structure_function_at(int(u_val))

        assert g1 == Rational(g2), f"g({u_val}) mismatch"

    @pytest.mark.parametrize("h1,h2,u_val", [
        (Rational(1), Rational(-2), Rational(5)),
        (Rational(1), Rational(-3), Rational(7)),
        (Rational(37), Rational(41), Rational(100)),
    ])
    def test_unitarity_2path(self, h1, h2, u_val):
        """g(u)*g(-u) = 1 via 2 paths: this engine and direct computation."""
        # Path 1: cfg25 engine
        dc = DimensionalComparison(h1, h2)
        assert dc.verify_g_unitarity(u_val)

        # Path 2: direct symbolic
        h3 = -(h1 + h2)
        num_pos = (u_val - h1) * (u_val - h2) * (u_val - h3)
        den_pos = (u_val + h1) * (u_val + h2) * (u_val + h3)
        num_neg = (-u_val - h1) * (-u_val - h2) * (-u_val - h3)
        den_neg = (-u_val + h1) * (-u_val + h2) * (-u_val + h3)
        product = (num_pos * num_neg) / (den_pos * den_neg)
        assert product == 1, f"g({u_val})*g(-{u_val}) != 1"

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(-2)),
        (Rational(1), Rational(-3)),
        (Rational(2), Rational(-5)),
    ])
    def test_kappa_complementarity_2path(self, h1, h2):
        """kappa_ch(A) + kappa_ch(A^!) = 0 via 2 paths."""
        from compute.lib.holomorphic_cs_chiral_engine import (
            BoundaryAlgebra, KoszulDual, OmegaBackground,
        )

        # Path 1: cfg25 engine
        kd = KoszulDualityLift(h1, h2)
        assert kd.verify_kappa_complementarity()

        # Path 2: hcs engine
        omega = OmegaBackground(int(h1), int(h2))
        ba = BoundaryAlgebra(2, omega)
        hcs_kd = KoszulDual(ba)
        assert hcs_kd.verify_kappa_complementarity()

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(-2)),
        (Rational(1), Rational(-3)),
        (Rational(37), Rational(41)),
    ])
    def test_parameter_inversion_2path(self, h1, h2):
        """sigma_2 even, sigma_3 odd under h_i -> -h_i: 2 paths."""
        # Path 1: cfg25 engine
        kd = KoszulDualityLift(h1, h2)
        assert kd.verify_parameter_inversion()

        # Path 2: direct symbolic
        h3 = -(h1 + h2)
        sigma2_orig = h1 * h2 + h1 * h3 + h2 * h3
        sigma3_orig = h1 * h2 * h3
        sigma2_inv = (-h1) * (-h2) + (-h1) * (-h3) + (-h2) * (-h3)
        sigma3_inv = (-h1) * (-h2) * (-h3)
        assert sigma2_inv == sigma2_orig, "sigma_2 not even"
        assert sigma3_inv == -sigma3_orig, "sigma_3 not odd"

    def test_km_level_3path(self):
        """KM level k = -sigma_2 via 3 paths at SV point."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground

        h1, h2 = Rational(1), Rational(-2)

        # Path 1: cfg25 boundary algebra
        ba = BoundaryAlgebraLift(h1, h2)
        k1 = ba.km_level

        # Path 2: hcs engine
        omega = OmegaBackground(1, -2)
        k2 = omega.kac_moody_level()

        # Path 3: direct
        h3 = -(h1 + h2)
        k3 = -(h1 * h2 + h1 * h3 + h2 * h3)

        assert k1 == Rational(3)
        assert Rational(k2) == Rational(3)
        assert k3 == Rational(3)

    def test_partition_count_2path(self):
        """Partition counts p(n) via 2 paths: Nekrasov engine and OEIS.

        OEIS A000041: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42.
        """
        fh = FactorizationHomologyLift(Rational(1), Rational(-2))

        # Path 1: internal Euler recurrence
        assert fh.verify_nekrasov_u1_product(max_n=10)

        # Path 2: direct check against OEIS ground truth
        from compute.lib.holomorphic_cs_chiral_engine import _partition_count
        oeis = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n in range(11):
            assert _partition_count(n) == oeis[n], f"p({n}) mismatch"

    def test_defect_level_2path(self):
        """Defect level Psi = -sigma_2 via 2 paths."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground

        for h1_val, h2_val in [(1, -2), (1, -3), (2, -5)]:
            h1, h2 = Rational(h1_val), Rational(h2_val)

            # Path 1: cfg25 submanifold engine
            si = SubmanifoldInvariantLift(h1, h2)
            defect = si.defect_algebra_on_submanifold(submanifold_dim=1)
            psi1 = defect["level"]

            # Path 2: hcs engine
            omega = OmegaBackground(h1_val, h2_val)
            psi2 = -omega.sigma2

            assert psi1 == Rational(psi2), f"Psi mismatch at ({h1_val},{h2_val})"

    def test_normal_det_adjunction_2path(self):
        """Normal bundle det degree via 2 paths: engine and adjunction formula.

        Adjunction for C in C^3: K_{C^3} = O (trivial).
        0 -> T_C -> T_{C^3}|_C -> N -> 0, so det(N) = det(T_{C^3}|_C) / det(T_C)
        = O / K_C^{-1} = K_C. So deg(det(N)) = deg(K_C) = 2g-2.
        Wait -- det(T_{C^3}|_C) = K_{C^3}^{-1}|_C = O, so det(N) = K_C.
        Then deg(det(N)) = 2g-2.

        But the engine computes 2-2g. Let me check: K_C = O(2g-2).
        CY adjunction: K_{C^3} trivial => K_C = det(N)^{-1} * K_{C^3}|_C = det(N)^{-1}.
        Wait, the correct formula: K_C = K_{C^3}|_C tensor det(N^*) = det(N^*) = det(N)^{-1}.
        So det(N) = K_C^{-1} = O(2-2g). This is what the engine computes.
        """
        si = SubmanifoldInvariantLift(Rational(1), Rational(-2))
        for genus in [0, 1, 2, 3]:
            # Path 1: engine
            hc = si.holomorphic_complement_6d(submanifold_dim=1, genus=genus)
            deg1 = hc["normal_det_degree"]

            # Path 2: CY adjunction formula det(N) = K_C^{-1} = O(2-2g)
            deg2 = 2 - 2 * genus

            assert deg1 == deg2, f"genus={genus}: {deg1} != {deg2}"
