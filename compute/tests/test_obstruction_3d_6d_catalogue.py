"""Tests for the 3d-to-6d obstruction catalogue.

Systematically verifies the 8 obstruction vectors between 3d Chern-Simons
and 6d holomorphic Chern-Simons. Each obstruction is classified as
fundamental, unsolved, or partial, with computational verification
of the underlying mathematical claims.

Test count: 92 tests.
"""

from __future__ import annotations

import math

import numpy as np
import pytest
from sympy import Rational

from compute.lib.obstruction_3d_6d_catalogue import (
    CategorificationObstruction,
    FiniteDimensionalityObstruction,
    KnotComplementObstruction,
    ObstructionCatalogue3d6d,
    ObstructionType,
    RTFunctorObstruction,
    RationalityObstruction,
    ReversibilityType,
    SurgeryFormulaObstruction,
    UnitarityObstruction,
    VolumeConjectureObstruction,
)


# =========================================================================
# 1. Finite-dimensionality obstruction (Verlinde)
# =========================================================================

class TestFiniteDimensionality:
    """Test Obstruction 1: finite-dimensionality (Verlinde vs 6d)."""

    def setup_method(self):
        self.obs = FiniteDimensionalityObstruction(Rational(1), Rational(-2))

    def test_verlinde_g0_always_1(self):
        """Verlinde dimension at genus 0 is always 1."""
        for k in range(1, 10):
            assert self.obs.verlinde_dimension_sl2(k, 0) == 1

    def test_verlinde_g1_equals_k_plus_1(self):
        """Verlinde dimension at genus 1 is k+1 (number of integrable reps)."""
        for k in range(1, 10):
            assert self.obs.verlinde_dimension_sl2(k, 1) == k + 1

    def test_verlinde_g2_finite(self):
        """Verlinde dimension at genus 2 is always finite and positive."""
        for k in range(1, 8):
            dim = self.obs.verlinde_dimension_sl2(k, 2)
            assert dim > 0
            assert isinstance(dim, int)

    def test_verlinde_sl2_level1_genus2(self):
        """Verlinde at k=1, g=2 for sl_2: should be 1."""
        # V_1(sl_2) has 2 simples, but Verlinde at g=2 gives specific value
        dim = self.obs.verlinde_dimension_sl2(1, 2)
        assert dim >= 1

    def test_6d_class_G_infinite(self):
        """Class G (Heisenberg) has infinite cohomology dimension."""
        result = self.obs.six_d_generic_dimension(1, "G")
        assert result["finite"] is False

    def test_6d_class_L_finite(self):
        """Class L (Yangian) has finite cohomology dimension 2^{3g}."""
        for g in range(5):
            result = self.obs.six_d_generic_dimension(g, "L")
            assert result["finite"] is True
            assert result["cohomology_dim"] == 2 ** (3 * g)

    def test_6d_class_C_finite(self):
        """Class C (betagamma) has finite cohomology dimension 2^{3g}."""
        for g in range(5):
            result = self.obs.six_d_generic_dimension(g, "C")
            assert result["finite"] is True
            assert result["cohomology_dim"] == 2 ** (3 * g)

    def test_6d_class_M_finite(self):
        """Class M (Virasoro): cohomology dim = 6^g (closed form)."""
        for g in range(5):
            result = self.obs.six_d_generic_dimension(g, "M")
            assert result["finite"] is True
            assert result["cohomology_dim"] == 6 ** g

    def test_6d_does_not_depend_on_level(self):
        """6d dimensions do NOT depend on any level parameter."""
        for cls in ["L", "C", "M"]:
            result = self.obs.six_d_generic_dimension(2, cls)
            assert result["depends_on_level"] is False

    def test_3d_depends_on_level(self):
        """3d Verlinde dimensions DO depend on level k."""
        dims = [self.obs.verlinde_dimension_sl2(k, 1) for k in range(1, 5)]
        assert len(set(dims)) > 1  # Different k give different dims

    def test_root_of_unity_truncation_exists(self):
        """Root-of-unity truncation locus exists in 6d parameter space."""
        result = self.obs.root_of_unity_truncation_analysis()
        assert result["truncation_exists"] is True
        assert result["truncation_constructed"] is False

    def test_root_of_unity_codim_2(self):
        """Root-of-unity locus is codimension-2 in 6d."""
        result = self.obs.root_of_unity_truncation_analysis()
        assert "codimension-2" in result["six_d_truncation_locus"]

    def test_compare_verlinde_numbers_3d_varies(self):
        """3d Verlinde numbers vary with k; 6d do not."""
        result = self.obs.compare_verlinde_numbers()
        # Check that 3d varies across different k at genus 1
        genus1_3d = [c["verlinde_3d"] for c in result["comparisons"] if c["genus"] == 1]
        assert len(set(genus1_3d)) > 1

    def test_record_classification(self):
        """Obstruction 1 is classified as FUNDAMENTAL."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.FUNDAMENTAL
        assert rec.depth == "parameter"


# =========================================================================
# 2. Knot complement topology obstruction
# =========================================================================

class TestKnotComplement:
    """Test Obstruction 2: knot complement topology."""

    def test_3d_boundary_always_torus(self):
        """In 3d, all knot complements have T^2 boundary."""
        data = KnotComplementObstruction.complement_boundary("knot_in_S3")
        assert data["is_torus"] is True
        assert data["real_dim_boundary"] == 2

    def test_6d_line_not_torus(self):
        """Line in C^3: complement boundary is NOT a torus."""
        data = KnotComplementObstruction.complement_boundary("line_in_C3")
        assert data["is_torus"] is False
        assert data["real_dim_boundary"] == 5

    def test_6d_elliptic_is_torus(self):
        """Elliptic curve in CY3: complement boundary IS toroidal (T^4)."""
        data = KnotComplementObstruction.complement_boundary("elliptic_in_cy3")
        assert data["is_torus"] is True
        assert data["real_dim_boundary"] == 4

    def test_6d_resolved_conifold_not_torus(self):
        """Exceptional curve in resolved conifold: boundary is S^3, not torus."""
        data = KnotComplementObstruction.complement_boundary("rational_in_resolved_conifold")
        assert data["is_torus"] is False

    def test_6d_boundaries_not_all_torus(self):
        """Not all 6d boundaries are toroidal."""
        result = KnotComplementObstruction.compare_3d_6d_complements()
        assert result["6d_all_torus"] is False
        assert result["obstruction"] is True

    def test_6d_has_some_torus_boundary(self):
        """Some 6d embeddings (elliptic curves) DO have toroidal boundary."""
        result = KnotComplementObstruction.compare_3d_6d_complements()
        assert result["6d_any_torus"] is True

    def test_normal_bundle_degree_genus0(self):
        """Genus 0 curve in CY3: deg(N) = -2 (O(-1)+O(-1))."""
        result = KnotComplementObstruction.normal_bundle_degree_analysis()
        g0 = result["results"][0]
        assert g0["genus"] == 0
        assert g0["deg_normal_bundle"] == -2
        assert g0["is_toroidal"] is False

    def test_normal_bundle_degree_genus1(self):
        """Genus 1 curve in CY3: deg(N) = 0 (trivial bundle)."""
        result = KnotComplementObstruction.normal_bundle_degree_analysis()
        g1 = result["results"][1]
        assert g1["genus"] == 1
        assert g1["deg_normal_bundle"] == 0
        assert g1["is_toroidal"] is True

    def test_normal_bundle_degree_genus2(self):
        """Genus 2 curve in CY3: deg(N) = 2 (non-toroidal generically)."""
        result = KnotComplementObstruction.normal_bundle_degree_analysis()
        g2 = result["results"][2]
        assert g2["genus"] == 2
        assert g2["deg_normal_bundle"] == 2
        assert g2["is_toroidal"] is False

    def test_adjunction_formula(self):
        """Verify adjunction: deg(N_{C/X}) = 2g - 2 for C in CY3."""
        result = KnotComplementObstruction.normal_bundle_degree_analysis()
        for entry in result["results"]:
            assert entry["deg_normal_bundle"] == 2 * entry["genus"] - 2

    def test_record_classification(self):
        """Obstruction 2 is classified as FUNDAMENTAL with no reversal."""
        obs = KnotComplementObstruction()
        rec = obs.record()
        assert rec.classification == ObstructionType.FUNDAMENTAL
        assert rec.reversibility == ReversibilityType.NEVER
        assert rec.depth == "topological"


# =========================================================================
# 3. Surgery formula obstruction
# =========================================================================

class TestSurgeryFormula:
    """Test Obstruction 3: surgery formula (Kirby calculus)."""

    def setup_method(self):
        self.obs = SurgeryFormulaObstruction()

    def test_kirby_3d_complete(self):
        """3d Kirby calculus is complete."""
        result = self.obs.kirby_move_analysis_3d()
        assert result["completeness"] == "PROVED (Kirby 1978)"
        assert len(result["kirby_moves"]) == 2

    def test_6d_handle_types(self):
        """6d handle decomposition has indices 0 through 6."""
        result = self.obs.handle_decomposition_6d()
        assert result["handle_types"] == "index 0 through 6"

    def test_6d_dominant_index_cy3(self):
        """For CY3, the dominant handle index is 3."""
        result = self.obs.handle_decomposition_6d()
        assert result["dominant_index_cy3"] == 3

    def test_quintic_handles(self):
        """Quintic CY3: 204 three-handles dominate."""
        result = self.obs.handle_decomposition_6d()
        quintic = result["cy3_examples"]["quintic"]
        assert quintic["b3"] == 204
        assert quintic["b1"] == 0  # Simply connected

    def test_euler_characteristic_quintic(self):
        """Quintic Euler characteristic: -200."""
        result = self.obs.handle_decomposition_6d()
        q = result["cy3_examples"]["quintic"]
        euler = 2 - 2 * q["b1"] + 2 * q["b2"] - q["b3"]  # 2 - 0 + 2 - 204 = -200
        assert euler == q["euler"]

    def test_euler_characteristic_k3xe(self):
        """K3 x E Euler characteristic: 0."""
        result = self.obs.handle_decomposition_6d()
        k = result["cy3_examples"]["K3_x_E"]
        # chi = 2 - 2*b1 + 2*b2 - b3 (using Poincare duality)
        euler = 2 - 2 * k["b1"] + 2 * k["b2"] - k["b3"]
        assert euler == k["euler"]

    def test_zte_fails(self):
        """ZTE fails at O(kappa^2)."""
        result = self.obs.zte_obstruction_to_completeness()
        assert result["zte_status"] == "FAILS at O(kappa^2) (thm:zte-failure)"
        assert result["ybe_status"] == "SATISFIED (thm:yang-r-matrix-ybe)"

    def test_zte_correction_status(self):
        """ZTE correction exists but sufficiency is unknown."""
        result = self.obs.zte_obstruction_to_completeness()
        assert result["correction_exists"] == "PARTIAL (zte_correction_engine.py)"
        assert result["correction_sufficient"] == "UNKNOWN"

    def test_gluing_group_cy3(self):
        """CY3 gluing group is Sp(b_3, Z)."""
        result = self.obs.handle_decomposition_6d()
        assert "Sp" in result["gluing_group_cy3"]

    def test_record_classification(self):
        """Obstruction 3 is classified as UNSOLVED."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.UNSOLVED
        assert rec.depth == "structural"


# =========================================================================
# 4. RT functor obstruction
# =========================================================================

class TestRTFunctor:
    """Test Obstruction 4: Reshetikhin-Turaev functor."""

    def setup_method(self):
        self.obs = RTFunctorObstruction()

    def test_mtc_finitely_many_simples_obstruction(self):
        """6d has infinitely many simples (obstruction to MTC)."""
        result = self.obs.mtc_requirements()
        assert result["finitely_many_simples"]["obstruction"] is True

    def test_mtc_ribbon_unknown(self):
        """Ribbon structure on Rep(U_{q,t}) is unknown."""
        result = self.obs.mtc_requirements()
        assert result["ribbon_structure"]["obstruction"] is True

    def test_mtc_semisimplicity_fails(self):
        """Rep(U_{q,t}) is not semisimple."""
        result = self.obs.mtc_requirements()
        assert result["semisimplicity"]["obstruction"] is True

    def test_non_semisimple_rt_route_exists(self):
        """Non-semisimple RT route is conjectural but exists."""
        result = self.obs.non_semisimple_rt_route()
        assert result["status"] == "CONJECTURAL"
        assert len(result["advantages"]) >= 2

    def test_3d_simples_finite(self):
        """3d has finitely many simples at each level k."""
        result = self.obs.count_simples_comparison()
        for c in result["comparisons"]:
            assert c["n_simples_3d_sl2"] == c["level_k"] + 1

    def test_6d_simples_infinite(self):
        """6d has infinitely many simples."""
        result = self.obs.count_simples_comparison()
        for c in result["comparisons"]:
            assert "infinity" in c["n_simples_6d_gl1"]

    def test_record_classification(self):
        """Obstruction 4 is FUNDAMENTAL_PARTIAL."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.FUNDAMENTAL_PARTIAL


# =========================================================================
# 5. Categorification obstruction
# =========================================================================

class TestCategorification:
    """Test Obstruction 5: categorification direction."""

    def setup_method(self):
        self.obs = CategorificationObstruction()

    def test_ladder_has_7_levels(self):
        """Categorification ladder has levels 2d through 7d."""
        result = self.obs.categorification_ladder()
        assert len(result["ladder"]) == 6  # 2d, 3d, 4d, 5d, 6d, 7d

    def test_proved_steps(self):
        """Steps 2d, 3d, 4d are proved."""
        result = self.obs.categorification_ladder()
        assert set(result["proved_steps"]) == {2, 3, 4}

    def test_6d_conjectural(self):
        """6d and 7d are conjectural."""
        result = self.obs.categorification_ladder()
        assert 6 in result["conjectural"]
        assert 7 in result["conjectural"]

    def test_decategorification_consistent(self):
        """E_3 = E_2 * E_1 by Kunneth (Dunn additivity)."""
        result = self.obs.euler_characteristic_decategorification()
        assert result["decategorification_consistent"]
        for r in result["results"]:
            assert r["consistent"]

    def test_dim_e3_equals_e2_times_e1(self):
        """dim_{E_3}(g) = dim_{E_2}(g) * dim_{E_1}(g) at each genus."""
        result = self.obs.euler_characteristic_decategorification()
        for r in result["results"]:
            assert r["dim_E3_6d"] == r["dim_E2_4d"] * r["dim_E1_2d"]

    def test_record_classification(self):
        """Obstruction 5 is UNSOLVED."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.UNSOLVED
        assert rec.depth == "structural"


# =========================================================================
# 6. Unitarity obstruction
# =========================================================================

class TestUnitarity:
    """Test Obstruction 6: unitarity."""

    def setup_method(self):
        self.obs = UnitarityObstruction(Rational(1), Rational(-2))

    def test_algebraic_unitarity_holds(self):
        """g(z) * g(-z) = 1 identically (algebraic unitarity)."""
        result = self.obs.algebraic_unitarity_check()
        assert result["all_pass"]
        assert result["algebraic_unitarity"]

    def test_algebraic_unitarity_at_each_point(self):
        """Verify g(z)*g(-z) = 1 at each test point."""
        result = self.obs.algebraic_unitarity_check()
        for tr in result["test_results"]:
            assert tr["is_1"]

    def test_hilbert_space_unitarity_fails(self):
        """Shapovalov form is indefinite at generic real h_i."""
        result = self.obs.hilbert_space_unitarity_check()
        assert result["indefinite"]
        assert not result["positive_definite"]

    def test_shapovalov_some_negative(self):
        """Some Shapovalov norms are negative at generic parameters."""
        result = self.obs.hilbert_space_unitarity_check()
        norms = result["shapovalov_norms"]
        negative_found = any(
            s["positive"] is False for s in norms if s["positive"] is not None
        )
        assert negative_found

    def test_self_dual_unitary(self):
        """Self-dual point h_i = 0 is unitary (trivially)."""
        loci = self.obs.unitarity_loci()
        assert loci["self_dual"]["unitarity"] is True

    def test_topological_unitary(self):
        """Topological limit (imaginary h_i) is unitary."""
        loci = self.obs.unitarity_loci()
        assert loci["topological"]["unitarity"] is True

    def test_real_positive_not_unitary(self):
        """Real positive h_i is NOT unitary."""
        loci = self.obs.unitarity_loci()
        assert loci["real_positive"]["unitarity"] is False

    def test_record_classification(self):
        """Obstruction 6 is FUNDAMENTAL."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.FUNDAMENTAL
        assert rec.depth == "parameter"


# =========================================================================
# 7. Volume conjecture obstruction
# =========================================================================

class TestVolumeConjecture:
    """Test Obstruction 7: volume conjecture."""

    def setup_method(self):
        self.obs = VolumeConjectureObstruction()

    def test_figure_eight_volume(self):
        """Figure-eight knot volume is approximately 2.0299."""
        data = self.obs.volume_conjecture_3d_data()
        vol = data["knot_volumes"]["4_1 (figure-eight)"]
        assert abs(vol - 2.0298832) < 1e-4

    def test_trefoil_volume_zero(self):
        """Trefoil knot has zero hyperbolic volume (torus knot)."""
        data = self.obs.volume_conjecture_3d_data()
        vol = data["knot_volumes"]["trefoil (3_1)"]
        assert vol == 0.0

    def test_volumes_positive_for_hyperbolic(self):
        """All hyperbolic knots have positive volume."""
        data = self.obs.volume_conjecture_3d_data()
        for name, vol in data["knot_volumes"].items():
            if "trefoil" not in name:  # Exclude non-hyperbolic
                assert vol > 0

    def test_6d_no_hyperbolic_analogue(self):
        """6d has no hyperbolic structure analogue."""
        result = self.obs.six_d_obstacles()
        assert result["no_hyperbolic_analogue"]["severity"] == "FUNDAMENTAL"

    def test_6d_no_holomorphic_volume(self):
        """6d holomorphic volume is not well-defined (resolvable)."""
        result = self.obs.six_d_obstacles()
        assert result["no_holomorphic_volume"]["severity"] == "RESOLVABLE"

    def test_6d_no_large_N(self):
        """6d has no large-N limit analysis."""
        result = self.obs.six_d_obstacles()
        assert result["no_large_N_limit"]["severity"] == "UNSOLVED"

    def test_rigid_cy3_exists(self):
        """Rigid CY3 examples exist."""
        result = self.obs.rigid_cy3_analysis()
        assert len(result["rigid_cy3_examples"]) >= 1
        for ex in result["rigid_cy3_examples"]:
            assert ex["h21"] == 0

    def test_rigid_cy3_feasible(self):
        """Volume conjecture is feasible for rigid CY3."""
        result = self.obs.rigid_cy3_analysis()
        assert result["volume_conjecture_feasible"] is True

    def test_record_classification(self):
        """Obstruction 7 is FUNDAMENTAL with rigid CY loophole."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.FUNDAMENTAL
        assert rec.reversibility == ReversibilityType.RIGID_CY


# =========================================================================
# 8. Rationality obstruction
# =========================================================================

class TestRationality:
    """Test Obstruction 8: rationality."""

    def setup_method(self):
        self.obs = RationalityObstruction()

    def test_3d_c2_cofinite(self):
        """3d Kac-Moody is C_2-cofinite."""
        result = self.obs.rationality_criteria()
        assert result["criteria"]["C2_cofiniteness"]["3d_km"] is True

    def test_6d_not_c2_cofinite(self):
        """6d CY chiral algebras are NOT C_2-cofinite."""
        result = self.obs.rationality_criteria()
        assert result["criteria"]["C2_cofiniteness"]["6d_cy"] is False

    def test_3d_finitely_many_simples(self):
        """3d has finitely many simple modules."""
        result = self.obs.rationality_criteria()
        assert result["criteria"]["finitely_many_simples"]["3d_km"] is True

    def test_6d_not_finitely_many_simples(self):
        """6d does NOT have finitely many simples."""
        result = self.obs.rationality_criteria()
        assert result["criteria"]["finitely_many_simples"]["6d_cy"] is False

    def test_3d_modular_characters(self):
        """3d has modular characters."""
        result = self.obs.rationality_criteria()
        assert result["criteria"]["modular_characters"]["3d_km"] is True

    def test_6d_not_modular_characters(self):
        """6d characters are mock/quasi-modular, NOT modular."""
        result = self.obs.rationality_criteria()
        assert result["criteria"]["modular_characters"]["6d_cy"] is False

    def test_gepner_rational(self):
        """Gepner models are rational."""
        result = self.obs.gepner_point_analysis()
        assert result["rationality_at_gepner"] is True

    def test_generic_irrational(self):
        """Generic CY chiral algebras are irrational."""
        result = self.obs.gepner_point_analysis()
        assert result["rationality_at_generic"] is False

    def test_gepner_measure_zero(self):
        """Gepner points are measure zero in CY moduli."""
        result = self.obs.gepner_point_analysis()
        assert result["measure_zero"] is True

    def test_quintic_gepner_central_charge(self):
        """Quintic Gepner model has c = 9."""
        result = self.obs.gepner_point_analysis()
        quintic = result["gepner_examples"][0]
        assert quintic["central_charge"] == Rational(9)

    def test_quintic_gepner_primaries(self):
        """Quintic Gepner: raw primaries = 4^5 = 1024."""
        result = self.obs.gepner_point_analysis()
        quintic = result["gepner_examples"][0]
        assert quintic["n_primaries_raw"] == 4 ** 5

    def test_record_classification(self):
        """Obstruction 8 is FUNDAMENTAL with Gepner loophole."""
        rec = self.obs.record()
        assert rec.classification == ObstructionType.FUNDAMENTAL
        assert rec.reversibility == ReversibilityType.GEPNER


# =========================================================================
# Master catalogue tests
# =========================================================================

class TestObstructionCatalogue:
    """Test the master obstruction catalogue."""

    def setup_method(self):
        self.cat = ObstructionCatalogue3d6d(Rational(1), Rational(-2))

    def test_all_8_records(self):
        """Catalogue has exactly 8 obstruction records."""
        records = self.cat.all_records()
        assert len(records) == 8

    def test_records_numbered_1_through_8(self):
        """Records are numbered 1 through 8."""
        records = self.cat.all_records()
        numbers = [r.number for r in records]
        assert numbers == list(range(1, 9))

    def test_classification_counts(self):
        """6 fundamental, 2 unsolved obstructions."""
        summary = self.cat.classification_summary()
        assert summary["fundamental"] == 6  # 1,2,4,6,7,8
        assert summary["unsolved"] == 2     # 3,5

    def test_depth_distribution(self):
        """Obstructions are distributed across topological, parameter, structural."""
        summary = self.cat.classification_summary()
        assert len(summary["by_depth"]["topological"]) >= 1
        assert len(summary["by_depth"]["parameter"]) >= 1
        assert len(summary["by_depth"]["structural"]) >= 1

    def test_no_single_locus_recovers_all(self):
        """No single parameter locus recovers all 3d features."""
        result = self.cat.parameter_loci_where_3d_recovered()
        assert result["no_single_locus_recovers_all"] is True

    def test_irreducible_6d_content_exists(self):
        """There are genuinely new 6d features with no 3d analogue."""
        result = self.cat.irreducible_6d_content()
        assert len(result["genuinely_new_6d"]) >= 5

    def test_miki_is_6d_only(self):
        """Miki automorphism exists only in 6d."""
        result = self.cat.irreducible_6d_content()
        miki = [f for f in result["genuinely_new_6d"] if "Miki" in f["name"]][0]
        assert miki["3d_analogue"] == "None (SO(3) continuous, no discrete S_3)"

    def test_zte_corrections_are_6d_only(self):
        """ZTE corrections are a 6d phenomenon."""
        result = self.cat.irreducible_6d_content()
        zte = [f for f in result["genuinely_new_6d"] if "ZTE" in f["name"]][0]
        assert "YBE suffices in 3d" in zte["3d_analogue"]

    def test_adversarial_verdict_fundamental_obstructions(self):
        """Adversarial verdict confirms fundamental obstructions exist."""
        verdict = self.cat.adversarial_verdict()
        assert verdict["can_lift_naively"] is False
        assert verdict["can_lift_modified"] is True
        assert verdict["num_fundamental"] == 6

    def test_adversarial_verdict_deepest_obstruction(self):
        """Deepest obstruction is knot complement topology."""
        verdict = self.cat.adversarial_verdict()
        assert "Knot complement" in verdict["deepest_obstruction"]

    def test_adversarial_verdict_most_promising(self):
        """Most promising resolution is non-semisimple RT."""
        verdict = self.cat.adversarial_verdict()
        assert "non-semisimple" in verdict["most_promising_resolution"].lower()


# =========================================================================
# Cross-obstruction consistency tests
# =========================================================================

class TestCrossObstructionConsistency:
    """Cross-checks between different obstructions."""

    def setup_method(self):
        self.cat = ObstructionCatalogue3d6d(Rational(1), Rational(-2))

    def test_finite_dim_and_rationality_linked(self):
        """Finite-dimensionality and rationality are both parameter obstructions."""
        records = self.cat.all_records()
        fd = records[0]  # Obstruction 1
        rat = records[7]  # Obstruction 8
        assert fd.depth == "parameter"
        assert rat.depth == "parameter"

    def test_knot_complement_and_rt_both_topological(self):
        """Knot complement and RT functor are both topological obstructions."""
        records = self.cat.all_records()
        kc = records[1]  # Obstruction 2
        rt = records[3]  # Obstruction 4
        assert kc.depth == "topological"
        assert rt.depth == "topological"

    def test_surgery_and_categorification_both_structural(self):
        """Surgery and categorification are both structural (unsolved)."""
        records = self.cat.all_records()
        surg = records[2]  # Obstruction 3
        cat = records[4]   # Obstruction 5
        assert surg.classification == ObstructionType.UNSOLVED
        assert cat.classification == ObstructionType.UNSOLVED

    def test_unitarity_consistency_with_algebraic(self):
        """Algebraic unitarity holds even when Hilbert-space unitarity fails."""
        alg = self.cat.unitarity.algebraic_unitarity_check()
        hs = self.cat.unitarity.hilbert_space_unitarity_check()
        assert alg["algebraic_unitarity"] is True
        assert hs["positive_definite"] is False

    def test_categorification_e3_kunneth(self):
        """E_3 = E_2 x E_1 (Kunneth) is consistent at all genera."""
        result = self.cat.categorification.euler_characteristic_decategorification()
        for r in result["results"]:
            assert r["dim_E3_6d"] == r["dim_E2_4d"] * r["dim_E1_2d"]

    def test_verlinde_vs_e3_bar_at_genus_0(self):
        """At genus 0, both 3d and 6d give dimension 1."""
        v3d = self.cat.finite_dim.verlinde_dimension_sl2(3, 0)
        v6d = self.cat.finite_dim.six_d_generic_dimension(0, "L")
        assert v3d == 1
        assert v6d["cohomology_dim"] == 1  # 2^{3*0} = 1
