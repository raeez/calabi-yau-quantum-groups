"""Tests for the deep 3d-to-6d obstruction catalogue.

Verifies quantitative obstruction measures, partial lift spectra,
cross-obstruction interaction matrices, and dimensional interpolation
across all 8 obstruction vectors.

Test count: 120 tests.
"""

from __future__ import annotations

import math

import numpy as np
import pytest
from sympy import Rational

# Import with importlib because the module name starts with a digit
import importlib
_mod = importlib.import_module("compute.lib.3d_6d_obstruction_catalogue")

FiniteDimDeep = _mod.FiniteDimDeep
KnotComplementDeep = _mod.KnotComplementDeep
SurgeryDeep = _mod.SurgeryDeep
RTFunctorDeep = _mod.RTFunctorDeep
CategorificationDeep = _mod.CategorificationDeep
UnitarityDeep = _mod.UnitarityDeep
VolumeConjectureDeep = _mod.VolumeConjectureDeep
RationalityDeep = _mod.RationalityDeep
CrossObstructionInteraction = _mod.CrossObstructionInteraction
DimensionalInterpolation = _mod.DimensionalInterpolation
DeepObstructionCatalogue3d6d = _mod.DeepObstructionCatalogue3d6d
ObstructionDepth = _mod.ObstructionDepth
LiftResult = _mod.LiftResult


# =========================================================================
# 1. Finite-dimensionality deep tests
# =========================================================================

class TestFiniteDimDeep:
    """Test deep finite-dimensionality obstruction analysis."""

    def setup_method(self):
        self.obs = FiniteDimDeep(Rational(1), Rational(-2))

    def test_truncation_ideal_3d_simples(self):
        """3d sl_2 at level k=N-2 has N-1 simples."""
        for N in range(2, 7):
            result = self.obs.truncation_ideal_dimension(N, N)
            assert result["three_d"]["n_simples"] == N - 1

    def test_truncation_ideal_3d_proved(self):
        """3d truncation is proved."""
        result = self.obs.truncation_ideal_dimension(4, 4)
        assert "PROVED" in result["three_d"]["status"]

    def test_truncation_ideal_6d_conjectural(self):
        """6d truncation is conjectural."""
        result = self.obs.truncation_ideal_dimension(4, 4)
        assert "CONJECTURAL" in result["six_d"]["status"]

    def test_truncation_6d_cells_equals_lcm(self):
        """6d charge lattice truncation has lcm(N,M) cells."""
        result = self.obs.truncation_ideal_dimension(3, 4)
        assert result["six_d"]["n_cells"] == 12  # lcm(3,4)

    def test_verlinde_growth_3d_varies_with_k(self):
        """3d Verlinde numbers vary with level k."""
        result = self.obs.verlinde_growth_comparison(g_max=2)
        # At genus 1, different k give different dims
        genus1 = [c for c in result["comparisons"] if c["genus"] == 1]
        dims = [c["dim_3d_verlinde"] for c in genus1]
        assert len(set(dims)) > 1

    def test_verlinde_growth_6d_independent_of_k(self):
        """6d E_3 bar dimensions do NOT depend on k."""
        result = self.obs.verlinde_growth_comparison(g_max=2)
        for g in range(3):
            class_L_dims = [
                c["dim_6d_class_L"] for c in result["comparisons"]
                if c["genus"] == g
            ]
            assert len(set(class_L_dims)) == 1  # All same

    def test_deformation_cohomology_3d_vanishes(self):
        """3d HH^2 vanishes (truncation works)."""
        result = self.obs.deformation_cohomology_dim(5)
        assert result["three_d"]["hh2_dim"] == 0
        assert result["three_d"]["obstruction_vanishes"] is True

    def test_deformation_cohomology_6d_nonzero(self):
        """6d HH^2 lower bound is positive for N >= 2."""
        result = self.obs.deformation_cohomology_dim(5)
        assert result["six_d"]["hh2_dim_lower_bound"] >= 4
        assert result["six_d"]["obstruction_vanishes"] is False

    def test_partial_lift_fraction(self):
        """Finite-dim partial lift: 2 of 4 structures lift."""
        result = self.obs.partial_lift_spectrum()
        assert result.generators_total == 4
        assert result.generators_lifted == 2
        assert result.lift_fraction == 0.5

    def test_partial_lift_obstruction_primary(self):
        """Finite-dim obstruction is primary."""
        result = self.obs.partial_lift_spectrum()
        assert result.obstruction_depth == ObstructionDepth.PRIMARY


# =========================================================================
# 2. Knot complement deep tests
# =========================================================================

class TestKnotComplementDeep:
    """Test deep knot complement topology analysis."""

    def test_boundary_homology_genus0_simply_connected(self):
        """Genus-0 curve boundary is simply connected (pi_1 = 0)."""
        result = KnotComplementDeep.boundary_homology(0)
        assert result["pi1_rank"] == 0

    def test_boundary_homology_genus1_toroidal(self):
        """Genus-1 curve boundary is T^4 (pi_1 = Z^4)."""
        result = KnotComplementDeep.boundary_homology(1)
        assert result["pi1_rank"] == 4
        assert "toroidal" in result["boundary_type"]

    def test_boundary_homology_genus2_non_toroidal(self):
        """Genus-2 curve boundary is non-toroidal."""
        result = KnotComplementDeep.boundary_homology(2)
        assert "non-toroidal" in result["boundary_type"]

    def test_3d_boundary_is_torus(self):
        """3d comparison: T^2 boundary with pi_1 = Z^2."""
        result = KnotComplementDeep.boundary_homology(0)
        assert result["comparison_3d"]["pi1_rank"] == 2

    def test_homological_gap_genus0(self):
        """Genus-0: homological gap = |0 - 2| = 2."""
        result = KnotComplementDeep.boundary_homology(0)
        assert result["homological_gap"] == 2

    def test_homological_gap_genus1(self):
        """Genus-1: homological gap = |4 - 2| = 2."""
        result = KnotComplementDeep.boundary_homology(1)
        assert result["homological_gap"] == 2

    def test_alexander_3d_one_variable(self):
        """3d Alexander polynomial has 1 variable."""
        result = KnotComplementDeep.alexander_polynomial_obstruction()
        assert result["three_d"]["variables"] == 1

    def test_alexander_6d_genus0_no_variables(self):
        """6d genus-0: no Alexander polynomial (simply connected)."""
        result = KnotComplementDeep.alexander_polynomial_obstruction()
        assert result["six_d_by_genus"][0]["variables"] == 0

    def test_alexander_6d_genus1_two_variables(self):
        """6d genus-1: two-variable Alexander polynomial."""
        result = KnotComplementDeep.alexander_polynomial_obstruction()
        assert result["six_d_by_genus"][1]["variables"] == 2

    def test_partial_lift_fraction(self):
        """Knot complement: 2 of 5 structures lift."""
        result = KnotComplementDeep.partial_lift_spectrum(KnotComplementDeep())
        assert result.generators_total == 5
        assert result.generators_lifted == 2
        assert abs(result.lift_fraction - 0.4) < 1e-10


# =========================================================================
# 3. Surgery formula deep tests
# =========================================================================

class TestSurgeryDeep:
    """Test deep surgery formula obstruction analysis."""

    def setup_method(self):
        self.obs = SurgeryDeep(Rational(1), Rational(-2))

    def test_zte_charge0_trivial(self):
        """Charge-0 sector: ZTE trivially satisfied."""
        result = self.obs.zte_obstruction_rank()
        assert result["charge_sectors"][0]["obs_rank"] == 0
        assert result["charge_sectors"][0]["trivial"] is True

    def test_zte_charge2_rank4(self):
        """Charge-2 sector: obstruction rank 4."""
        result = self.obs.zte_obstruction_rank()
        assert result["charge_sectors"][2]["obs_rank"] == 4

    def test_zte_total_obstruction_rank_8(self):
        """Total ZTE obstruction rank is 8."""
        result = self.obs.zte_obstruction_rank()
        assert result["total_obstruction_rank"] == 8

    def test_zte_obstruction_order_2(self):
        """ZTE obstruction is O(kappa^2)."""
        result = self.obs.zte_obstruction_rank()
        assert result["obstruction_order"] == 2

    def test_correction_space_exists(self):
        """ZTE correction space exists (nonempty)."""
        result = self.obs.zte_correction_space_dim()
        assert result["correction_exists"] is True

    def test_correction_physical_parameters(self):
        """ZTE correction has 1 physical parameter (normalization)."""
        result = self.obs.zte_correction_space_dim()
        assert result["physical_parameters"] == 1

    def test_handle_quintic_swaps(self):
        """Quintic: 204 handles give 20706 pairwise swaps."""
        result = self.obs.handle_rearrangement_obstruction(204)
        assert result["cy3_examples"]["quintic"]["n_swaps"] == 204 * 203 // 2

    def test_handle_obstruction_quadratic_growth(self):
        """Handle obstruction grows quadratically."""
        r1 = self.obs.handle_rearrangement_obstruction(10)
        r2 = self.obs.handle_rearrangement_obstruction(20)
        # Ratio of obs_dims should be approximately (20/10)^2 = 4
        ratio = r2["obstruction_dim"] / r1["obstruction_dim"]
        assert 3.5 < ratio < 4.5

    def test_partial_lift_secondary(self):
        """Surgery obstruction is secondary (O(kappa^2))."""
        result = self.obs.partial_lift_spectrum()
        assert result.obstruction_depth == ObstructionDepth.SECONDARY


# =========================================================================
# 4. RT functor deep tests
# =========================================================================

class TestRTFunctorDeep:
    """Test deep RT functor obstruction analysis."""

    def setup_method(self):
        self.obs = RTFunctorDeep()

    def test_mtc_two_definite_obstructions(self):
        """MTC checklist: 2 definite obstructions."""
        result = self.obs.mtc_checklist_quantitative()
        assert result["total_obstructions"] == 2

    def test_mtc_t_matrix_no_obstruction(self):
        """T-matrix structure has no obstruction."""
        result = self.obs.mtc_checklist_quantitative()
        assert result["modular_T_matrix"]["obstruction"] == "NONE"

    def test_mtc_finitely_many_simples_primary(self):
        """Finiteness obstruction is primary."""
        result = self.obs.mtc_checklist_quantitative()
        assert result["finitely_many_simples"]["obstruction"] == "PRIMARY"

    def test_non_ss_rt_overall_feasibility(self):
        """Non-semisimple RT feasibility: 24%."""
        result = self.obs.non_semisimple_rt_feasibility()
        assert abs(result["overall_feasibility"] - 0.24) < 0.01

    def test_non_ss_rt_typical_objects_exist(self):
        """Typical objects exist (measure-1 set)."""
        result = self.obs.non_semisimple_rt_feasibility()
        assert result["typical_objects"]["exists"] is True

    def test_partial_lift_fraction_one_third(self):
        """RT functor: 2 of 6 structures lift (~1/3)."""
        result = self.obs.partial_lift_spectrum()
        assert result.generators_total == 6
        assert result.generators_lifted == 2
        assert abs(result.lift_fraction - 1/3) < 0.01


# =========================================================================
# 5. Categorification deep tests
# =========================================================================

class TestCategorificationDeep:
    """Test deep categorification obstruction analysis."""

    def setup_method(self):
        self.obs = CategorificationDeep()

    def test_3d_to_4d_proved(self):
        """3d -> 4d categorification (Khovanov) is proved."""
        result = self.obs.categorification_obstruction_groups()
        step_3_4 = result["steps"][0]
        assert step_3_4["vanishes"] is True
        assert step_3_4["dim"] == 0

    def test_6d_to_7d_obstructed(self):
        """6d -> 7d categorification is obstructed (E_4 needed)."""
        result = self.obs.categorification_obstruction_groups()
        step_6_7 = result["steps"][3]
        assert step_6_7["vanishes"] is False

    def test_kunneth_holds_all_genera(self):
        """E_3 = E_2 x E_1 Kunneth holds at all genera."""
        result = self.obs.kunneth_dimension_check()
        assert result["all_consistent"] is True

    def test_kunneth_genus_2(self):
        """Genus 2: 2^6 = 2^4 * 2^2."""
        result = self.obs.kunneth_dimension_check()
        g2 = result["results"][2]
        assert g2["dim_E3"] == 64
        assert g2["dim_E2"] == 16
        assert g2["dim_E1"] == 4
        assert g2["kunneth_holds"] is True

    def test_partial_lift_low_fraction(self):
        """Categorification: only 1 of 5 structures lifts."""
        result = self.obs.partial_lift_spectrum()
        assert result.generators_lifted == 1
        assert result.lift_fraction == 0.2


# =========================================================================
# 6. Unitarity deep tests
# =========================================================================

class TestUnitarityDeep:
    """Test deep unitarity obstruction analysis."""

    def setup_method(self):
        self.obs = UnitarityDeep(Rational(1), Rational(-2))

    def test_shapovalov_not_positive_definite(self):
        """Shapovalov form is NOT positive-definite at h1=1, h2=-2, h3=1.

        At these parameters, phi(1) has a pole (u=h1=1), so the form is
        degenerate. The form is not positive-definite.
        """
        result = self.obs.shapovalov_signature(10)
        assert not result["positive_definite"]

    def test_shapovalov_has_degenerate_levels(self):
        """Some Shapovalov levels are degenerate (pole or zero) at h1=1."""
        result = self.obs.shapovalov_signature(10)
        assert result["has_degenerate_levels"] is True

    def test_shapovalov_generic_params_indefinite(self):
        """At truly generic parameters (h_i not integer), form is indefinite.

        Use h1=7/3, h2=-11/3, h3=4/3 (all thirds, no integer coincidences).
        phi(1) < 0 and phi(3) < 0 while phi(2) > 0 -> indefinite.
        """
        obs_generic = UnitarityDeep(Rational(7, 3), Rational(-11, 3))
        result = obs_generic.shapovalov_signature(10)
        assert result["indefinite"] is True
        assert result["total_negative"] > 0

    def test_shapovalov_signature_ratio_generic(self):
        """Signature ratio is between 0 and 1 at truly generic parameters."""
        obs_generic = UnitarityDeep(Rational(7, 3), Rational(-11, 3))
        result = obs_generic.shapovalov_signature(10)
        ratio = result["signature_ratio"]
        assert ratio is not None
        assert 0 < ratio < 1

    def test_first_negative_level_exists_generic(self):
        """First negative level exists at truly generic parameters."""
        obs_generic = UnitarityDeep(Rational(7, 3), Rational(-11, 3))
        result = obs_generic.shapovalov_signature(10)
        assert result["first_negative_level"] is not None
        assert result["first_negative_level"] >= 1

    def test_unitarity_deficit_positive_generic(self):
        """Unitarity deficit is positive at truly generic parameters."""
        obs_generic = UnitarityDeep(Rational(7, 3), Rational(-11, 3))
        result = obs_generic.shapovalov_signature(10)
        assert result["unitarity_deficit"] > 0

    def test_unitarity_locus_boundary_lines(self):
        """Unitarity boundary has lines for k=1,...,10."""
        result = self.obs.unitarity_locus_boundary()
        assert len(result["boundary_lines"]) == 10

    def test_self_dual_unitary(self):
        """Self-dual point (h1=h2=0) is unitary."""
        result = self.obs.unitarity_locus_boundary()
        assert result["self_dual_point"]["unitarity"] is True

    def test_partial_lift_fraction(self):
        """Unitarity: 2 of 5 structures lift."""
        result = self.obs.partial_lift_spectrum()
        assert result.lift_fraction == 0.4


# =========================================================================
# 7. Volume conjecture deep tests
# =========================================================================

class TestVolumeConjectureDeep:
    """Test deep volume conjecture obstruction analysis."""

    def setup_method(self):
        self.obs = VolumeConjectureDeep()

    def test_colored_jones_3_of_5_ingredients_lift(self):
        """Colored Jones: 3 of 5 ingredients lift to 6d."""
        result = self.obs.colored_jones_obstruction()
        assert result["n_ingredients_that_lift"] == 3
        assert result["n_ingredients_total"] == 5

    def test_curve_dependence_obstruction(self):
        """Curve dependence is a FUNDAMENTAL obstruction."""
        result = self.obs.colored_jones_obstruction()
        assert result["ingredients_6d"]["curve_dependence"]["obstruction"] == "FUNDAMENTAL"

    def test_holomorphic_volume_3d_zero_moduli(self):
        """3d hyperbolic volume has 0 moduli (Mostow rigidity)."""
        result = self.obs.holomorphic_volume_obstruction()
        assert result["three_d_moduli_dim"] == 0

    def test_quintic_moduli_dim(self):
        """Quintic: moduli dimension = 206."""
        result = self.obs.holomorphic_volume_obstruction()
        quintic = [e for e in result["six_d_examples"] if e["name"] == "quintic"][0]
        assert quintic["moduli_dim"] == 206

    def test_rigid_cy3_minimal_moduli(self):
        """Rigid CY3 have minimal moduli (just normalization, dim=2)."""
        result = self.obs.holomorphic_volume_obstruction()
        rigid = [e for e in result["six_d_examples"] if "rigid" in e["name"]]
        for r in rigid:
            assert r["moduli_dim"] == 2

    def test_asymptotic_class_G_polynomial(self):
        """Class G growth is polynomial (no volume conjecture)."""
        result = self.obs.asymptotic_growth_comparison()
        assert result["six_d_growth_by_class"]["G"]["type"] == "polynomial"

    def test_asymptotic_class_C_exponential(self):
        """Class C growth is exponential (closest to 3d)."""
        result = self.obs.asymptotic_growth_comparison()
        assert result["six_d_growth_by_class"]["C"]["type"] == "exponential"

    def test_asymptotic_class_M_super_exponential(self):
        """Class M growth is super-exponential (new phenomenon)."""
        result = self.obs.asymptotic_growth_comparison()
        assert result["six_d_growth_by_class"]["M"]["type"] == "super_exponential"

    def test_figure_eight_volume(self):
        """Figure-eight knot volume is approximately 2.0299."""
        vol = VolumeConjectureDeep.KNOT_VOLUMES["4_1"]
        assert abs(vol - 2.0298832) < 1e-4

    def test_trefoil_volume_zero(self):
        """Trefoil has zero volume (torus knot)."""
        vol = VolumeConjectureDeep.KNOT_VOLUMES["3_1"]
        assert vol == 0.0

    def test_partial_lift_zero(self):
        """Volume conjecture: 0 of 5 structures lift."""
        result = self.obs.partial_lift_spectrum()
        assert result.generators_lifted == 0
        assert result.lift_fraction == 0.0


# =========================================================================
# 8. Rationality deep tests
# =========================================================================

class TestRationalityDeep:
    """Test deep rationality obstruction analysis."""

    def setup_method(self):
        self.obs = RationalityDeep()

    def test_irrationality_dim_equals_moduli_dim(self):
        """Irrationality dimension = full moduli dimension for all CY3."""
        result = self.obs.irrationality_dimension()
        for ex in result["examples"]:
            assert ex["irrationality_dim"] == ex["dim_moduli"]

    def test_quintic_irrationality_dim_102(self):
        """Quintic: irrationality dimension = 102."""
        result = self.obs.irrationality_dimension()
        quintic = [e for e in result["examples"] if e["name"] == "quintic"][0]
        assert quintic["irrationality_dim"] == 102

    def test_c2_gap_3d_bounded(self):
        """3d C_2 quotient is bounded (finite)."""
        result = self.obs.c2_cofiniteness_gap()
        assert "finite" in result["three_d_c2_quotient"]["dim"]

    def test_c2_gap_6d_all_infinite(self):
        """6d C_2 quotient is infinite for all classes."""
        result = self.obs.c2_cofiniteness_gap()
        for cls in ["G", "L", "C", "M"]:
            assert result["six_d_c2_quotient_by_class"][cls]["dim"] == "infinite"

    def test_modular_deficit_class_G_zero(self):
        """Class G has zero modular deficit (genuine modular forms)."""
        result = self.obs.modular_transformation_deficit()
        assert result["six_d_by_class"]["G"]["deficit"] == 0

    def test_modular_deficit_class_M_infinite(self):
        """Class M has infinite modular deficit (full shadow tower)."""
        result = self.obs.modular_transformation_deficit()
        assert result["six_d_by_class"]["M"]["deficit"] == "infinite"

    def test_partial_lift_zero(self):
        """Rationality: 0 of 5 structures lift."""
        result = self.obs.partial_lift_spectrum()
        assert result.generators_lifted == 0
        assert result.lift_fraction == 0.0

    def test_obstruction_all_order(self):
        """Rationality obstruction is all-order."""
        result = self.obs.partial_lift_spectrum()
        assert result.obstruction_depth == ObstructionDepth.ALL_ORDER


# =========================================================================
# Cross-obstruction interaction tests
# =========================================================================

class TestCrossObstructionInteraction:
    """Test the cross-obstruction interaction matrix."""

    def test_matrix_is_8x8(self):
        """Interaction matrix is 8x8."""
        I = CrossObstructionInteraction.interaction_matrix()
        assert I.shape == (8, 8)

    def test_matrix_diagonal_zero(self):
        """Diagonal is zero (an obstruction doesn't interact with itself)."""
        I = CrossObstructionInteraction.interaction_matrix()
        for i in range(8):
            assert I[i, i] == 0.0

    def test_rationality_helps_finitedim(self):
        """Resolving rationality (8) strongly helps finite-dim (1)."""
        I = CrossObstructionInteraction.interaction_matrix()
        assert I[7, 0] >= 1.5  # Strong synergy

    def test_finitedim_helps_rt(self):
        """Resolving finite-dim (1) strongly helps RT (4)."""
        I = CrossObstructionInteraction.interaction_matrix()
        assert I[0, 3] >= 1.5

    def test_surgery_helps_rt(self):
        """Resolving surgery (3) strongly helps RT (4)."""
        I = CrossObstructionInteraction.interaction_matrix()
        assert I[2, 3] >= 1.5

    def test_unitarity_worsens_volconj(self):
        """Resolving unitarity (6) at imaginary h_i worsens vol conj (7)."""
        I = CrossObstructionInteraction.interaction_matrix()
        assert I[5, 6] < 0  # Antagonism

    def test_matrix_not_symmetric(self):
        """Interaction matrix is NOT symmetric."""
        I = CrossObstructionInteraction.interaction_matrix()
        assert not np.allclose(I, I.T)

    def test_block_diagonal_dominance(self):
        """Block-diagonal components dominate (>50%)."""
        result = CrossObstructionInteraction.block_structure()
        assert result["block_diagonal_dominance"] > 0.5

    def test_critical_path_has_8_entries(self):
        """Critical path orders all 8 obstructions."""
        result = CrossObstructionInteraction.critical_path()
        assert len(result["critical_order"]) == 8

    def test_rt_receives_most_synergy(self):
        """RT functor (4) receives the most incoming synergy."""
        result = CrossObstructionInteraction.critical_path()
        # RT = index 3 in 0-indexed -> "4:RT"
        assert result["incoming_sums"]["4:RT"] >= 4.0


# =========================================================================
# Dimensional interpolation tests
# =========================================================================

class TestDimensionalInterpolation:
    """Test dimensional interpolation engine."""

    def setup_method(self):
        self.interp = DimensionalInterpolation()

    def test_3d_zero_obstructions(self):
        """At n=1 (3d): zero obstructions active."""
        result = self.interp.obstruction_onset_by_dimension()
        assert result["onset_table"]["n=1 (3d)"]["n_active"] == 0

    def test_5d_three_obstructions(self):
        """At n=2 (5d): 3 obstructions active."""
        result = self.interp.obstruction_onset_by_dimension()
        assert result["onset_table"]["n=2 (5d)"]["n_active"] == 3

    def test_6d_all_obstructions(self):
        """At n=3 (6d): all 8 obstructions active."""
        result = self.interp.obstruction_onset_by_dimension()
        assert result["onset_table"]["n=3 (6d)"]["n_active"] == 8

    def test_five_discontinuous_obstructions(self):
        """5 obstructions are discontinuous (appear at n=3)."""
        result = self.interp.obstruction_onset_by_dimension()
        assert len(result["discontinuous_obstructions"]) == 5

    def test_three_continuous_obstructions(self):
        """3 obstructions are continuous (appear at n=2)."""
        result = self.interp.obstruction_onset_by_dimension()
        assert len(result["continuous_obstructions"]) == 3

    def test_e_n_structure_e1_no_obstruction(self):
        """E_1 (n=1): no simplex equation needed."""
        result = self.interp.e_n_structure_at_each_dimension()
        assert result["n=1"]["obstruction"] == 0

    def test_e_n_structure_e2_ybe_satisfied(self):
        """E_2 (n=2): YBE satisfied, no higher eq needed."""
        result = self.interp.e_n_structure_at_each_dimension()
        assert result["n=2"]["obstruction"] == 0

    def test_e_n_structure_e3_zte_fails(self):
        """E_3 (n=3): ZTE fails."""
        result = self.interp.e_n_structure_at_each_dimension()
        assert result["n=3"]["obstruction"] == 1


# =========================================================================
# Master catalogue tests
# =========================================================================

class TestDeepObstructionCatalogue:
    """Test the master deep obstruction catalogue."""

    def setup_method(self):
        self.cat = DeepObstructionCatalogue3d6d(Rational(1), Rational(-2))

    def test_all_8_partial_lifts(self):
        """All 8 partial lift spectra are returned."""
        lifts = self.cat.all_partial_lifts()
        assert len(lifts) == 8

    def test_all_lift_fractions_in_0_1(self):
        """All lift fractions are between 0 and 1."""
        lifts = self.cat.all_partial_lifts()
        for name, lr in lifts.items():
            assert 0 <= lr.lift_fraction <= 1, f"{name}: {lr.lift_fraction}"

    def test_aggregate_lift_fraction_low(self):
        """Aggregate lift fraction is below 50%."""
        result = self.cat.aggregate_lift_fraction()
        assert result["overall_lift_fraction"] < 0.5

    def test_total_generators_positive(self):
        """Total generators across all categories is positive."""
        result = self.cat.aggregate_lift_fraction()
        assert result["total_generators"] > 30  # Should be ~40

    def test_severity_ranking_has_8_entries(self):
        """Severity ranking has 8 entries."""
        result = self.cat.obstruction_severity_ranking()
        assert len(result["ranking"]) == 8

    def test_most_severe_is_volume_or_rationality(self):
        """Most severe obstruction is volume conjecture or rationality (0% lift)."""
        result = self.cat.obstruction_severity_ranking()
        most_severe = result["most_severe"]
        assert "volume" in most_severe or "rational" in most_severe

    def test_deep_verdict_exists(self):
        """Deep adversarial verdict is produced."""
        result = self.cat.deep_adversarial_verdict()
        assert "verdict" in result
        assert result["overall_lift_fraction"] < 0.5

    def test_deep_verdict_discontinuous_count(self):
        """5 discontinuous obstructions in verdict."""
        result = self.cat.deep_adversarial_verdict()
        assert result["n_discontinuous_obstructions"] == 5

    def test_deep_verdict_continuous_count(self):
        """3 continuous obstructions in verdict."""
        result = self.cat.deep_adversarial_verdict()
        assert result["n_continuous_obstructions"] == 3

    def test_interaction_block_dominance_in_verdict(self):
        """Block dominance is reported in verdict and > 50%."""
        result = self.cat.deep_adversarial_verdict()
        assert result["interaction_block_dominance"] > 0.5


# =========================================================================
# Cross-engine consistency tests
# =========================================================================

class TestCrossEngineConsistency:
    """Verify consistency between the deep catalogue and the survey catalogue."""

    def test_lift_fraction_ordered_by_severity(self):
        """Lift fractions are consistent with severity ordering."""
        cat = DeepObstructionCatalogue3d6d(Rational(1), Rational(-2))
        lifts = cat.all_partial_lifts()
        # Volume conjecture and rationality should have 0 lift fraction
        assert lifts["7_volume_conjecture"].lift_fraction == 0.0
        assert lifts["8_rationality"].lift_fraction == 0.0
        # Finite-dim should have positive lift fraction
        assert lifts["1_finite_dim"].lift_fraction > 0.0

    def test_zte_order_consistent(self):
        """ZTE obstruction order (2) is consistent across analyses."""
        surgery = SurgeryDeep(Rational(1), Rational(-2))
        rank = surgery.zte_obstruction_rank()
        assert rank["obstruction_order"] == 2
        correction = surgery.zte_correction_space_dim()
        assert "kappa^2" in correction["correction_order"]

    def test_kunneth_consistent_with_interpolation(self):
        """Kunneth E_3 = E_2 * E_1 is consistent at all levels."""
        cat_deep = CategorificationDeep()
        kunneth = cat_deep.kunneth_dimension_check()
        assert kunneth["all_consistent"]
        # Also check with interpolation
        interp = DimensionalInterpolation()
        e_n = interp.e_n_structure_at_each_dimension()
        # E_3 should have 1 obstruction
        assert e_n["n=3"]["obstruction"] == 1
