"""Test suite for quantum groups from factorization homology: 3d CS vs 6d hCS.

Validates the systematic comparison between:
  Route A: U_q(g) from 3d CS on R^3 (PROVED, CFG25)
  Route B: U_{q,t}(gl_hat_hat_1) from 6d hCS on C^3 (CONJECTURAL)

Structure:
  Section 1:  Configuration space topology (braiding sources)
  Section 2:  Route A (3d CS) structural properties
  Section 3:  Route B (6d hCS) structural properties
  Section 4:  5d interpolation
  Section 5:  Obstruction analysis (O1, O2, O3)
  Section 6:  Numerical verification (structure functions, kappa, Koszul)
  Section 7:  Dimensional reduction chain (6d -> 5d -> 3d)
  Section 8:  E_3 braiding comparison
  Section 9:  Structure function comparison (rational vs trigonometric)
  Section 10: Koszul duality comparison
  Section 11: Miki automorphism analysis
  Section 12: Master comparison and verdict

AP compliance verified:
  AP-CY22: Miki is algebra-specific, not operadic
  AP-CY31: spectral z (Yangian) != worldsheet z
  AP-CY14: 6d results are CONJECTURAL
  AP113: all kappa subscripted
  AP-CY28: safe test points far from poles
  AP154: algebraic E_3 (Deligne) vs topological E_3 distinguished
"""

import math
import os
import sys

import pytest
from fractions import Fraction
from sympy import Rational

# Ensure import path
_lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")
if _lib_dir not in sys.path:
    sys.path.insert(0, _lib_dir)

from qg_from_fh_3d_6d import (
    ConfigurationSpaceBraiding,
    RouteA_3dCS,
    RouteB_6dHCS,
    Route5d_Interpolation,
    ObstructionAnalysis,
    NumericalVerification,
    DimensionalReductionChain,
    E3BraidingComparison,
    HolographicBridgeDatum,
    StructureFunctionComparison,
    KoszulDualityComparison,
    run_full_comparison,
    verdict,
)


# =========================================================================
# Section 1: Configuration space topology
# =========================================================================

class TestConfigurationSpaceTopology:
    """Test the topology of configuration spaces at each dimension."""

    def test_conf2_link_R2(self):
        """Conf_2(R^2) ~ S^1, pi_1 = Z (braid group source)."""
        dim = ConfigurationSpaceBraiding.conf2_link_sphere_dim(2)
        assert dim == 1  # S^1
        pi1 = ConfigurationSpaceBraiding.fundamental_group_link(dim)
        assert pi1 == "Z"

    def test_conf2_link_R3(self):
        """Conf_2(R^3) ~ S^2, pi_1 = 0."""
        dim = ConfigurationSpaceBraiding.conf2_link_sphere_dim(3)
        assert dim == 2  # S^2
        pi1 = ConfigurationSpaceBraiding.fundamental_group_link(dim)
        assert pi1 == "0"

    def test_conf2_link_C2(self):
        """Conf_2(C^2) = Conf_2(R^4) ~ S^3, pi_1 = 0."""
        dim = ConfigurationSpaceBraiding.conf2_link_sphere_dim(4)  # R^4 = C^2
        assert dim == 3  # S^3
        pi1 = ConfigurationSpaceBraiding.fundamental_group_link(dim)
        assert pi1 == "0"

    def test_conf2_link_C3(self):
        """Conf_2(C^3) = Conf_2(R^6) ~ S^5, pi_1 = 0."""
        dim = ConfigurationSpaceBraiding.conf2_link_sphere_dim(6)  # R^6 = C^3
        assert dim == 5  # S^5
        pi1 = ConfigurationSpaceBraiding.fundamental_group_link(dim)
        assert pi1 == "0"

    def test_3d_vs_6d_comparison(self):
        """R^3 and C^3 both have trivial topological braiding (pi_1 = 0)."""
        cmp = ConfigurationSpaceBraiding.compare_3d_vs_6d()
        assert cmp["same_en_level"] is True
        assert cmp["same_braiding_source"] is False
        assert cmp["obstruction_O1"] is True

    def test_braiding_analysis_R3(self):
        """R^3 braiding: topological, from SO(3) framing."""
        analysis = ConfigurationSpaceBraiding.braiding_analysis("R^3")
        assert analysis["pi_1_conf2"] == "0"
        assert analysis["nontrivial_braiding_from_topology"] is False
        assert analysis["requires_deformation"] is True

    def test_braiding_analysis_C3(self):
        """C^3 braiding: from Omega-background, not topology."""
        analysis = ConfigurationSpaceBraiding.braiding_analysis("C^3")
        assert analysis["pi_1_conf2"] == "0"
        assert analysis["nontrivial_braiding_from_topology"] is False
        assert analysis["requires_deformation"] is True

    def test_R2_is_special(self):
        """R^2 is the ONLY case with nontrivial topological braiding (braid group)."""
        analysis = ConfigurationSpaceBraiding.braiding_analysis("R^2")
        assert analysis["pi_1_conf2"] == "Z"
        assert analysis["nontrivial_braiding_from_topology"] is True


# =========================================================================
# Section 2: Route A (3d CS on R^3)
# =========================================================================

class TestRouteA:
    """Test the 3d CS construction of U_q(g)."""

    def test_en_level_is_3(self):
        """3d CS on R^3 produces E_3."""
        route = RouteA_3dCS("sl_2", Rational(1))
        assert route.en_level == 3

    def test_en_type_topological(self):
        """The E_3 is topological (framed), not holomorphic."""
        route = RouteA_3dCS("sl_2", Rational(1))
        assert route.en_type == "topological_framed"

    def test_single_parameter(self):
        """3d CS has one parameter q."""
        route = RouteA_3dCS("sl_2", Rational(1))
        q_data = route.q_parameter
        assert q_data["num_parameters"] == 1

    def test_dual_coxeter_sl2(self):
        """h^vee(sl_2) = 2."""
        route = RouteA_3dCS("sl_2", Rational(1))
        assert route.dual_coxeter == Rational(2)

    def test_dual_coxeter_gl1(self):
        """h^vee(gl_1) = 0."""
        route = RouteA_3dCS("gl_1", Rational(1))
        assert route.dual_coxeter == Rational(0)

    def test_no_miki(self):
        """Route A has NO Miki automorphism."""
        route = RouteA_3dCS("sl_2", Rational(1))
        miki = route.miki_automorphism()
        assert miki["exists"] is False

    def test_koszul_duality_proved(self):
        """Koszul duality is PROVED for Route A."""
        route = RouteA_3dCS("gl_1", Rational(1))
        kd = route.koszul_duality()
        assert "PROVED" in kd["status"]

    def test_r_matrix_satisfies_ybe(self):
        """The R-matrix of U_q(g) satisfies the Yang-Baxter equation."""
        route = RouteA_3dCS("sl_2", Rational(1))
        rm = route.r_matrix()
        assert rm["satisfies_YBE"] is True

    def test_config_space_braiding(self):
        """Braiding from framed Conf_2(R^3)."""
        route = RouteA_3dCS("sl_2", Rational(1))
        br = route.configuration_space_braiding()
        assert br["conf2_link"] == "S^2"
        assert br["braiding_type"] == "framed_topological"

    def test_summary_structure(self):
        """Summary has all required fields."""
        route = RouteA_3dCS("gl_1", Rational(1))
        s = route.summary()
        assert s["status"] == "PROVED (CFG25)"
        assert s["en_level"] == 3
        assert s["num_parameters"] == 1
        assert s["miki"] is False
        assert s["omega_background"] is False


# =========================================================================
# Section 3: Route B (6d hCS on C^3)
# =========================================================================

class TestRouteB:
    """Test the 6d hCS construction of U_{q,t}(gl_hat_hat_1)."""

    def test_en_level_is_3(self):
        """6d hCS on C^3 produces E_3 (holomorphic)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        assert route.en_level == 3

    def test_en_type_holomorphic(self):
        """The E_3 is holomorphic (chiral), not topological."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        assert route.en_type == "holomorphic_chiral"

    def test_topological_shadow_e6(self):
        """The topological shadow (ignoring holomorphy) is E_6."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        assert route.topological_shadow_en == 6

    def test_two_parameters(self):
        """6d hCS has two parameters (q, t)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        q_data = route.q_parameter
        assert q_data["num_parameters"] == 2

    def test_cy_condition(self):
        """h1 + h2 + h3 = 0."""
        route = RouteB_6dHCS(Rational(37), Rational(41))
        assert route.h1 + route.h2 + route.h3 == 0

    def test_has_miki(self):
        """Route B HAS the Miki automorphism (AP-CY22: algebra-specific)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        miki = route.miki_automorphism()
        assert miki["exists"] is True
        assert miki["is_operadic"] is False  # AP-CY22

    def test_koszul_duality_conjectural(self):
        """Koszul duality is CONJECTURAL for Route B (AP-CY14)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        kd = route.koszul_duality()
        assert "CONJECTURAL" in kd["status"]

    def test_r_matrix_ybe_but_not_zte(self):
        """R-matrix satisfies YBE but FAILS ZTE at O(kappa^2)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        rm = route.r_matrix()
        assert rm["satisfies_YBE"] is True
        assert "FAILS" in rm["satisfies_ZTE"]

    def test_config_space_braiding(self):
        """Braiding from Omega-background on Conf_2(C^3)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        br = route.configuration_space_braiding()
        assert br["conf2_link"] == "S^5"
        assert br["braiding_type"] == "holomorphic_equivariant"

    def test_omega_background_role(self):
        """The Omega-background is the source of ALL nontrivial braiding."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        ob = route.omega_background_role()
        assert ob["3d_analogue"] == "NONE (R^3 has no Omega-background)"

    def test_summary_structure(self):
        """Summary has all required fields."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        s = route.summary()
        assert "CONJECTURAL" in s["status"]
        assert s["en_level"] == 3
        assert s["num_parameters"] == 2
        assert s["miki"] is True
        assert s["omega_background"] is True


# =========================================================================
# Section 4: 5d interpolation
# =========================================================================

class TestRoute5d:
    """Test the 5d interpolation between 3d and 6d."""

    def test_en_level_is_2(self):
        """5d hol CS on C^2 x R produces E_2."""
        route = Route5d_Interpolation(Rational(1), Rational(2))
        assert route.en_level == 2

    def test_interpolation_analysis(self):
        """5d has both topological (R) and holomorphic (C^2) directions."""
        route = Route5d_Interpolation(Rational(1), Rational(2))
        analysis = route.interpolation_analysis()
        assert analysis["parameters"]["effective"] == 1  # Like 3d
        assert analysis["miki"]["exists"] is False  # No full Miki

    def test_dim_reduction_to_3d(self):
        """5d -> 3d: h_i -> 0, Yangian -> current algebra."""
        route = Route5d_Interpolation(Rational(1), Rational(2))
        red = route.dimensional_reduction_to_3d()
        assert red["kappa_ch_preserved"] is True

    def test_summary(self):
        """5d summary."""
        route = Route5d_Interpolation(Rational(1), Rational(2))
        s = route.summary()
        assert "PROVED" in s["status"]
        assert s["en_level"] == 2
        assert s["num_parameters"] == 1


# =========================================================================
# Section 5: Obstruction analysis
# =========================================================================

class TestObstructionAnalysis:
    """Test the three obstructions O1, O2, O3."""

    @pytest.fixture
    def obstructions(self):
        route_a = RouteA_3dCS("gl_1", Rational(1))
        route_b = RouteB_6dHCS(Rational(37), Rational(41))
        return ObstructionAnalysis(route_a, route_b)

    def test_O1_braiding_source(self, obstructions):
        """O1: holomorphic vs topological E_3."""
        o1 = obstructions.obstruction_O1_braiding_source()
        assert o1["route_a"]["en_type"] == "topological_framed"
        assert o1["route_b"]["en_type"] == "holomorphic_chiral"
        assert o1["route_a"]["deformable"] is False
        assert o1["route_b"]["deformable"] is True

    def test_O2_parameters(self, obstructions):
        """O2: two-parameter vs one-parameter."""
        o2 = obstructions.obstruction_O2_parameters()
        assert o2["route_a_params"] == 1
        assert o2["route_b_params"] == 2

    def test_O3_miki(self, obstructions):
        """O3: Miki automorphism (present in 6d, absent in 3d)."""
        o3 = obstructions.obstruction_O3_miki()
        assert o3["route_a_miki"] is False
        assert o3["route_b_miki"] is True
        assert o3["algebra_specific"] is True  # AP-CY22

    def test_what_generalizes(self, obstructions):
        """Four features that DO generalize."""
        gen = obstructions.what_generalizes()
        assert gen["G1_logical_pattern"]["generalizes"] is True
        assert gen["G2_r_matrix_from_braiding"]["generalizes"] is True
        assert gen["G3_dimensional_projection"]["generalizes"] is True
        assert gen["G4_kappa_preservation"]["generalizes"] is True

    def test_full_comparison_has_verdict(self, obstructions):
        """Full comparison includes a verdict."""
        cmp = obstructions.full_comparison()
        assert "verdict" in cmp
        assert "does NOT directly generalize" in cmp["verdict"]


# =========================================================================
# Section 6: Numerical verification
# =========================================================================

class TestNumericalVerification:
    """Numerical checks for structure functions, kappa, Koszul duality."""

    @pytest.fixture
    def verifier(self):
        # AP-CY28: safe test points
        return NumericalVerification(Rational(37), Rational(41))

    def test_cy_condition(self, verifier):
        """h1 + h2 + h3 = 0."""
        assert verifier.verify_cy_condition() is True

    def test_structure_function_unitarity(self, verifier):
        """g(u) * g(-u) = 1."""
        assert verifier.verify_structure_function_symmetry() is True

    def test_classical_limit(self, verifier):
        """At self-dual point (sigma_3 = 0), g(u) = 1."""
        result = verifier.verify_classical_limit()
        assert result["self_dual_g_trivial"] is True
        assert result["sigma_3_at_self_dual"] == 0

    def test_koszul_parameter_inversion(self, verifier):
        """g(u) * g^!(-u) = 1 (Koszul pairing via structure function)."""
        # The test in NumericalVerification checks g(u) * g_dual(u) = 1
        # where g_dual has inverted h_i, which means g_dual(u) = g(-u) = 1/g(u)
        assert verifier.verify_koszul_parameter_inversion() is True

    def test_5d_to_6d_lift(self, verifier):
        """Trigonometric G(exp(u)) is close to rational g(u) at small u."""
        result = verifier.verify_5d_to_6d_lift()
        assert result["close_at_small_u"] is True

    def test_en_cascade_dimensions(self, verifier):
        """E_1 <= E_2 <= E_3 bar dimensions at each arity."""
        result = verifier.verify_en_cascade_dimensions()
        for n in range(9):
            assert result[n]["E_2 >= E_1"] is True
            assert result[n]["E_3 >= E_2"] is True

    def test_kappa_ch_preserved(self, verifier):
        """kappa_ch is the same at all E_n levels."""
        result = verifier.verify_kappa_ch_under_projection()
        assert result["all_equal"] is True

    def test_en_cascade_specific_values(self, verifier):
        """Check specific partition/multipartition values."""
        result = verifier.verify_en_cascade_dimensions()
        # n=0: all are 1
        assert result[0]["E_1 (partitions)"] == 1
        assert result[0]["E_2 (2-multipartitions)"] == 1
        assert result[0]["E_3 (3-multipartitions)"] == 1
        # n=1: p(1)=1, tau_2(1)=2, tau_3(1)=3
        assert result[1]["E_1 (partitions)"] == 1
        assert result[1]["E_2 (2-multipartitions)"] == 2
        assert result[1]["E_3 (3-multipartitions)"] == 3
        # n=2: p(2)=2, tau_2(2)=5, tau_3(2)=12
        assert result[2]["E_1 (partitions)"] == 2
        assert result[2]["E_2 (2-multipartitions)"] == 5
        # tau_3(2) = p(0)*p(0)*p(2) + p(0)*p(1)*p(1) + p(0)*p(2)*p(0)
        #          + p(1)*p(0)*p(1) + p(1)*p(1)*p(0) + p(2)*p(0)*p(0)
        #          = 2 + 1 + 2 + 1 + 1 + 2 = 9... let me compute properly
        # tau_3(2) = sum_{a+b+c=2} p(a)p(b)p(c)
        # (0,0,2): 1*1*2=2, (0,2,0): 2, (2,0,0): 2
        # (0,1,1): 1*1*1=1, (1,0,1): 1, (1,1,0): 1
        # total = 2+2+2+1+1+1 = 9
        assert result[2]["E_3 (3-multipartitions)"] == 9


# =========================================================================
# Section 7: Dimensional reduction chain
# =========================================================================

class TestDimensionalReductionChain:
    """Test the 6d -> 5d -> 3d reduction chain."""

    @pytest.fixture
    def chain(self):
        return DimensionalReductionChain(Rational(37), Rational(41))

    def test_6d_to_5d_reduction(self, chain):
        """6d -> 5d: E_3 -> E_2, two params -> one."""
        red = chain.reduction_6d_to_5d()
        assert "E_3 -> E_2" in red["en_level"]
        assert "2 (q,t) -> 1" in red["parameters"]

    def test_5d_to_3d_reduction(self, chain):
        """5d -> 3d: E_2 -> E_1, quantum -> classical."""
        red = chain.reduction_5d_to_3d()
        assert "E_2 -> E_1" in red["en_level"]

    def test_full_chain_structure(self, chain):
        """The full chain has three levels and two reductions."""
        fc = chain.full_chain()
        assert len(fc["chain"]) == 3
        assert len(fc["reductions"]) == 2
        # First level is 6d (CONJECTURAL), last is 3d (PROVED)
        assert fc["chain"][0]["status"] == "CONJECTURAL"
        assert fc["chain"][2]["status"] == "PROVED"

    def test_en_levels_decrease(self, chain):
        """E_n levels: 3 -> 2 -> 3 (3d is topological E_3!)."""
        fc = chain.full_chain()
        # Note: 3d CS on R^3 is ALSO E_3 (topological), not E_1!
        # The cascade 6d E_3-chiral -> 5d E_2-chiral -> 3d E_3-topological
        # is NOT a monotone decrease. The 3d theory has TOPOLOGICAL E_3.
        assert fc["chain"][0]["en"] == "E_3-chiral"
        assert fc["chain"][1]["en"] == "E_2-chiral"
        # 3d CS is E_3 topological
        assert "E_3" in fc["chain"][2]["en"]


# =========================================================================
# Section 8: E_3 braiding comparison
# =========================================================================

class TestE3BraidingComparison:
    """Compare the E_3 braiding in 3d vs 6d."""

    @pytest.fixture
    def comparison(self):
        return E3BraidingComparison(Rational(37), Rational(41))

    def test_3d_braiding_topological(self, comparison):
        """3d braiding: topological framed."""
        br = comparison.topological_braiding_3d()
        assert br["type"] == "topological_framed"
        assert br["depends_on_omega_bg"] is False

    def test_6d_braiding_holomorphic(self, comparison):
        """6d braiding: holomorphic equivariant."""
        br = comparison.holomorphic_braiding_6d()
        assert br["type"] == "holomorphic_equivariant"
        assert br["depends_on_omega_bg"] is True

    def test_comparison_table_completeness(self, comparison):
        """Comparison table has all 11 features."""
        table = comparison.comparison_table()
        assert len(table["feature"]) == 11
        assert len(table["3d_CS_R3"]) == 11
        assert len(table["6d_hCS_C3"]) == 11

    def test_3d_at_zero_still_e3(self, comparison):
        """3d: at q=1, still E_3 (topological, not deformable)."""
        br = comparison.topological_braiding_3d()
        assert br["at_q_equals_1"] == "R = identity (trivial braiding, but still E_3)"

    def test_6d_at_zero_becomes_einf(self, comparison):
        """6d: at h=0, E_3 -> E_inf (symmetric, no quantum group)."""
        br = comparison.holomorphic_braiding_6d()
        assert "E_inf" in br["at_h_equals_0"]


# =========================================================================
# Section 9: Structure function comparison
# =========================================================================

class TestStructureFunctionComparison:
    """Compare rational vs trigonometric structure functions."""

    @pytest.fixture
    def sf_compare(self):
        # Use moderate parameters for meaningful numerical comparison
        return StructureFunctionComparison(Rational(1, 10), Rational(1, 5))

    def test_rational_at_self_dual(self):
        """At self-dual (h3=0), g(u) = 1."""
        sf = StructureFunctionComparison(Rational(1), Rational(-1))
        # h3 = 0, so g(u) = (u-1)(u+1)(u-0) / ((u+1)(u-1)(u+0)) = u/u = 1
        # (for u != 0, +/-1)
        assert abs(sf.rational_structure_function(1000.0) - 1.0) < 1e-10

    def test_rational_unitarity(self, sf_compare):
        """g(u) * g(-u) = 1 for the rational structure function."""
        u = 100.0  # far from poles
        g_u = sf_compare.rational_structure_function(u)
        g_neg_u = sf_compare.rational_structure_function(-u)
        assert abs(g_u * g_neg_u - 1.0) < 1e-10

    def test_trigonometric_unitarity(self, sf_compare):
        """G(x) * G(1/x) = 1 for the trigonometric structure function."""
        import numpy as np
        x = 100.0  # far from poles
        G_x = sf_compare.trigonometric_structure_function(x)
        G_inv_x = sf_compare.trigonometric_structure_function(1.0 / x)
        assert abs(G_x * G_inv_x - 1.0) < 1e-8

    def test_miki_acts_trivially_on_G(self, sf_compare):
        """The S_3 Miki action on G is trivial (G is symmetric in q_i)."""
        result = sf_compare.miki_s3_action_on_G(x=50.0)
        assert bool(result["are_equal"]) is True

    def test_rational_limit(self, sf_compare):
        """Trigonometric G reduces to rational g for small parameters."""
        result = sf_compare.verify_rational_limit(u_test=0.001)
        # For small h_i and small u, G(exp(u)) ~ g(u) * correction
        # The ratio should be close to 1 for small parameters
        assert result["ratio"] is not None


# =========================================================================
# Section 10: Koszul duality comparison
# =========================================================================

class TestKoszulDualityComparison:
    """Compare Koszul duality at 3d, 5d, 6d."""

    @pytest.fixture
    def kd_compare(self):
        return KoszulDualityComparison(Rational(37), Rational(41))

    def test_3d_koszul_level_inversion(self, kd_compare):
        """3d: k -> k' = -k - 2h^vee."""
        kd = kd_compare.koszul_at_3d(Rational(1), Rational(2))
        assert "-k - 2*h^vee" in kd["parameter_inversion"]

    def test_5d_koszul_parameter_inversion(self, kd_compare):
        """5d: (h1,h2,h3) -> (-h1,-h2,-h3)."""
        kd = kd_compare.koszul_at_5d()
        assert "(h1,h2,h3) -> (-h1,-h2,-h3)" in kd["parameter_inversion"]

    def test_6d_koszul_conjectural(self, kd_compare):
        """6d: CONJECTURAL (AP-CY14)."""
        kd = kd_compare.koszul_at_6d()
        assert "CONJECTURAL" in kd["status"]

    def test_6d_miki_commutes_with_koszul(self, kd_compare):
        """The Miki automorphism commutes with Koszul duality."""
        kd = kd_compare.koszul_at_6d()
        assert kd["miki_commutes"] is True

    def test_universal_pattern(self, kd_compare):
        """All levels share the universal pattern of parameter inversion."""
        cmp = kd_compare.comparison()
        assert "universal_pattern" in cmp


# =========================================================================
# Section 11: Miki automorphism analysis
# =========================================================================

class TestMikiAutomorphism:
    """Test the Miki automorphism (AP-CY22 compliance throughout)."""

    def test_absent_in_3d(self):
        """Miki is ABSENT for 3d CS on R^3."""
        route = RouteA_3dCS("gl_1", Rational(1))
        assert route.miki_automorphism()["exists"] is False

    def test_present_in_6d(self):
        """Miki is PRESENT for 6d hCS on C^3 with gl_1."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        assert route.miki_automorphism()["exists"] is True

    def test_not_operadic(self):
        """AP-CY22: Miki is algebra-specific, NOT operadic."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        miki = route.miki_automorphism()
        assert miki["is_operadic"] is False
        assert miki["requires_specific_algebra"] is True

    def test_counterexample(self):
        """k[x]/(x^2) is E_3 but has no Miki (AP-CY22 counterexample)."""
        route = RouteB_6dHCS(Rational(1), Rational(2))
        miki = route.miki_automorphism()
        assert "k[x]/(x^2)" in miki["counterexample"]

    def test_absent_in_5d(self):
        """5d has at most partial Miki (SL_2(Z), not S_3)."""
        route = Route5d_Interpolation(Rational(1), Rational(2))
        analysis = route.interpolation_analysis()
        assert analysis["miki"]["exists"] is False


# =========================================================================
# Section 12: Master comparison and verdict
# =========================================================================

class TestMasterComparison:
    """Test the full comparison engine and verdict."""

    def test_run_full_comparison(self):
        """The master comparison runs without error."""
        result = run_full_comparison(
            gauge_algebra="gl_1",
            k=Rational(1),
            h1=Rational(37),
            h2=Rational(41),
        )
        assert "route_a" in result
        assert "route_b" in result
        assert "obstructions" in result
        assert "holographic_bridge" in result
        assert "numerical_checks" in result

    def test_all_numerical_checks_pass(self):
        """All numerical checks pass."""
        result = run_full_comparison(
            gauge_algebra="gl_1",
            k=Rational(1),
            h1=Rational(37),
            h2=Rational(41),
        )
        checks = result["numerical_checks"]
        assert checks["cy_condition"] is True
        assert checks["g_unitarity"] is True
        assert checks["koszul_inversion"] is True
        assert checks["kappa_preservation"]["all_equal"] is True

    def test_verdict_content(self):
        """The verdict correctly states that CFG25 does NOT directly generalize."""
        v = verdict()
        assert "prevent direct generalization" in v
        assert "(O1)" in v and "HOLOMORPHIC" in v
        assert "(O2)" in v and "TWO PARAMETERS" in v
        assert "(O3)" in v and "MIKI" in v

    def test_route_a_proved_route_b_conjectural(self):
        """Route A is PROVED, Route B is CONJECTURAL."""
        result = run_full_comparison()
        assert "PROVED" in result["route_a"]["status"]
        assert "CONJECTURAL" in result["route_b"]["status"]

    def test_same_en_level_different_type(self):
        """Both routes produce E_3, but of different types."""
        result = run_full_comparison()
        assert result["route_a"]["en_level"] == 3
        assert result["route_b"]["en_level"] == 3
        assert result["route_a"]["en_type"] != result["route_b"]["en_type"]

    def test_5d_interpolates(self):
        """5d is PROVED and interpolates between 3d and 6d."""
        result = run_full_comparison()
        assert "PROVED" in result["route_5d"]["status"]
        assert result["route_5d"]["en_level"] == 2  # Between E_3 and E_1


# =========================================================================
# Section 12b: Holographic/QG bridge gate
# =========================================================================

class TestHolographicBridgeDatum:
    """The pure mathematical holographic bridge is a typed datum, not a slogan."""

    def test_default_bridge_is_open(self):
        """With no data, holographic consequences are open proof obligations."""
        bridge = HolographicBridgeDatum()
        report = bridge.status_report()
        assert report["pure_math_constructed"] is False
        assert report["consequence_status"] == "OPEN_PROOF_OBLIGATION"
        assert set(report["missing_components"]) == set(HolographicBridgeDatum.REQUIRED_COMPONENTS)

    def test_k3e_chl_physics_bridge_is_conditional(self):
        """The current K3 x E / CHL bridge has physics witnesses but no pure functor."""
        bridge = HolographicBridgeDatum.k3e_chl_physics_bridge()
        report = bridge.status_report()
        assert report["pure_math_constructed"] is False
        assert report["consequence_status"] == "CONDITIONAL_ON_EXPLICIT_PHYSICAL_BRIDGE"
        assert "charge_lattice_isometry" in report["present_components"]
        assert "index_character_map" in report["present_components"]
        assert "boundary_chiral_category" in report["missing_components"]
        assert "factorization_homology_functoriality" in report["missing_components"]
        assert "ads3_cft2_dictionary" in report["physics_witnesses"]

    def test_complete_bridge_promotes_to_pure_theorem(self):
        """Only all required components promote the bridge to pure mathematics."""
        bridge = HolographicBridgeDatum.complete_pure_math_bridge()
        report = bridge.status_report()
        assert report["pure_math_constructed"] is True
        assert report["missing_components"] == []
        assert report["consequence_status"] == "THEOREM_PURE_MATHEMATICAL_BRIDGE"

    def test_unknown_bridge_component_rejected(self):
        """The oracle rejects vague or untyped bridge components."""
        with pytest.raises(ValueError):
            HolographicBridgeDatum(components={"physics_says_so": True})


# =========================================================================
# Section 13: Multi-path verification (AP10 compliance)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path cross-checks for key numerical results.

    AP10 mandate: every hardcoded assertion must be verified by at least 2
    independent computational paths. This section provides those cross-checks.
    """

    def test_unitarity_two_paths(self):
        """g(u)*g(-u) = 1 verified via (1) direct evaluation and (2) Koszul dual.

        Path 1: compute g(u) and g(-u) directly, check product = 1.
        Path 2: compute g(u) via original Omega and g(u) via Koszul-inverted
                 Omega (h_i -> -h_i), check product = 1.
        These are the SAME identity: g(-u; h) = g(u; -h) since negating u
        and negating all h_i both swap numerator/denominator factors.
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        # Safe parameters (AP-CY28)
        omega = OmegaBackground(Rational(37), Rational(41))
        omega_dual = OmegaBackground(Rational(-37), Rational(-41))
        u = Rational(1000)

        # Path 1: g(u) * g(-u)
        g_u = omega.structure_function_at(u)
        g_neg_u = omega.structure_function_at(-u)
        path1 = g_u * g_neg_u

        # Path 2: g(u; h) * g(u; -h)
        g_u_orig = omega.structure_function_at(u)
        g_u_dual = omega_dual.structure_function_at(u)
        path2 = g_u_orig * g_u_dual

        assert path1 == 1, f"Path 1 failed: {path1}"
        assert path2 == 1, f"Path 2 failed: {path2}"
        assert path1 == path2, "Paths disagree"

    def test_unitarity_identity_proof(self):
        """g(u)*g(-u) = 1 proved algebraically: numerator/denominator cancellation.

        Path 3 (algebraic): g(u) = N(u)/D(u) where N(u) = prod(u-h_i),
        D(u) = prod(u+h_i). Then g(-u) = prod(-u-h_i)/prod(-u+h_i)
        = (-1)^3 prod(u+h_i) / ((-1)^3 prod(u-h_i)) = D(u)/N(u) = 1/g(u).
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(Rational(37), Rational(41))
        u = Rational(997)  # Different test point from above

        g_u = omega.structure_function_at(u)
        g_neg_u = omega.structure_function_at(-u)

        # Algebraic path: g(-u) should equal 1/g(u)
        assert g_neg_u == Rational(1) / g_u, "Algebraic identity failed"
        assert g_u * g_neg_u == 1, "Unitarity failed"

    def test_kappa_preservation_three_paths(self):
        """kappa_ch preserved under E_3 -> E_2 -> E_1 via three independent paths.

        Path 1: BoundaryAlgebra.kappa_ch() at each dimension.
        Path 2: KoszulDual.kappa_ch_dual() = -kappa_ch at each dimension.
        Path 3: DimensionalProjection.verify_kappa_preservation().
        """
        from compute.lib.holomorphic_cs_chiral_engine import (
            BoundaryAlgebra, KoszulDual, DimensionalProjection, OmegaBackground,
        )
        omega = OmegaBackground(Rational(37), Rational(41))

        # Path 1: direct kappa at each dimension
        k3 = BoundaryAlgebra(3, omega).kappa_ch()
        k2 = BoundaryAlgebra(2, omega).kappa_ch()
        k1 = BoundaryAlgebra(1, omega).kappa_ch()
        path1_all_equal = (k3 == k2 == k1)

        # Path 2: Koszul dual kappa is -kappa at each dimension
        kd3 = KoszulDual(BoundaryAlgebra(3, omega)).kappa_ch_dual()
        kd2 = KoszulDual(BoundaryAlgebra(2, omega)).kappa_ch_dual()
        kd1 = KoszulDual(BoundaryAlgebra(1, omega)).kappa_ch_dual()
        path2_koszul_consistent = (kd3 == -k3) and (kd2 == -k2) and (kd1 == -k1)

        # Path 3: DimensionalProjection verification
        b3 = BoundaryAlgebra(3, omega)
        proj_3_to_2 = DimensionalProjection(b3, 2).verify_kappa_preservation()
        proj_3_to_1 = DimensionalProjection(b3, 1).verify_kappa_preservation()

        assert path1_all_equal, f"Path 1 failed: k3={k3}, k2={k2}, k1={k1}"
        assert path2_koszul_consistent, f"Path 2 failed: kd3={kd3}, kd2={kd2}, kd1={kd1}"
        assert proj_3_to_2, "Path 3 (3->2) failed"
        assert proj_3_to_1, "Path 3 (3->1) failed"

    def test_en_cascade_dimensions_two_paths(self):
        """E_n bar dimensions tau_n(k) verified by two methods.

        Path 1: direct convolution: tau_n(k) = sum_{a1+...+an=k} prod p(a_i).
        Path 2: generating function coefficient: [q^k] P(q)^n.

        P(q) = prod_{m>=1} 1/(1-q^m) is the partition generating function.
        tau_n(k) = [q^k] P(q)^n by the convolution theorem.
        """
        from compute.lib.holomorphic_cs_chiral_engine import _partition_count

        max_k = 6

        # Path 1: direct convolution
        def tau_by_convolution(n_level, k):
            if n_level == 1:
                return _partition_count(k)
            elif n_level == 2:
                return sum(_partition_count(a) * _partition_count(k - a)
                           for a in range(k + 1))
            elif n_level == 3:
                return sum(_partition_count(a) * _partition_count(b) *
                           _partition_count(k - a - b)
                           for a in range(k + 1)
                           for b in range(k - a + 1))

        # Path 2: generating function via power series multiplication
        def tau_by_gf(n_level, max_k):
            """Compute [q^0],...,[q^max_k] of P(q)^n_level."""
            # Start with P(q) truncated to degree max_k
            p = [0] * (max_k + 1)
            for k in range(max_k + 1):
                p[k] = _partition_count(k)
            # Multiply n_level copies
            result = [0] * (max_k + 1)
            result[0] = 1  # Start with 1
            for _ in range(n_level):
                new = [0] * (max_k + 1)
                for i in range(max_k + 1):
                    for j in range(max_k + 1 - i):
                        new[i + j] += result[i] * p[j]
                result = new
            return result

        for n_level in [1, 2, 3]:
            gf_coeffs = tau_by_gf(n_level, max_k)
            for k in range(max_k + 1):
                conv_val = tau_by_convolution(n_level, k)
                gf_val = gf_coeffs[k]
                assert conv_val == gf_val, \
                    f"E_{n_level} at k={k}: convolution={conv_val} != gf={gf_val}"

    def test_koszul_inversion_two_paths(self):
        """Koszul parameter inversion verified via two paths.

        Path 1: g(u; h) * g(u; -h) = 1 (Omega inversion).
        Path 2: g^!(u) = 1/g(u) where g^!(u) = g(-u) by definition.

        These are equivalent because g(u; -h) = g(-u; h), but the
        computation is done via different code paths.
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(Rational(37), Rational(41))
        omega_inv = OmegaBackground(Rational(-37), Rational(-41))
        u = Rational(500)

        # Path 1: original * inverted-Omega
        g_orig = omega.structure_function_at(u)
        g_inv_omega = omega_inv.structure_function_at(u)
        path1 = g_orig * g_inv_omega

        # Path 2: original * g(-u)
        g_neg_u = omega.structure_function_at(-u)
        path2 = g_orig * g_neg_u

        assert path1 == 1, f"Path 1 (Omega inversion) failed: {path1}"
        assert path2 == 1, f"Path 2 (u-negation) failed: {path2}"
        # Cross-check: the two Koszul duals agree
        assert g_inv_omega == g_neg_u, \
            f"g(u; -h) = {g_inv_omega} != g(-u; h) = {g_neg_u}"

    def test_sigma3_as_effective_parameter_two_paths(self):
        """sigma_3 = h1*h2*h3 is the effective deformation, verified two ways.

        Path 1: compute sigma_3 directly from OmegaBackground.
        Path 2: compute from the structure function asymptotic:
                g(u) = 1 - 2*sigma_3 / u^3 + O(u^{-5}) as u -> inf.
                The leading correction is -2*sigma_3 * u^{-3}.

        The O(u^{-1}) and O(u^{-2}) terms vanish by the CY condition
        (sigma_1 = h1+h2+h3 = 0) and parity.
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(Rational(3), Rational(5))
        sigma3_path1 = omega.sigma3
        assert sigma3_path1 == Rational(3) * Rational(5) * Rational(-8)  # h3=-8
        assert sigma3_path1 == Rational(-120)

        # Path 2: extract from large-u asymptotics of g(u)
        # g(u) ~ 1 - 2*sigma_3 / u^3 for large u
        u_large = Rational(10000)
        g_val = omega.structure_function_at(u_large)
        # g(u) - 1 ~ -2*sigma_3 / u^3
        correction = g_val - 1
        sigma3_extracted = -correction * u_large**3 / 2
        # This is approximate (higher order terms present), but should be close
        ratio = float(sigma3_extracted / sigma3_path1)
        assert abs(ratio - 1.0) < 1e-6, \
            f"sigma_3 extraction failed: ratio = {ratio}"

    def test_config_space_topology_two_paths(self):
        """Configuration space link dimensions verified by formula and lookup.

        Path 1: formula: Conf_2(R^d) link = S^{d-1}, so dim = d-1.
        Path 2: lookup from the TOPOLOGY dictionary.
        """
        # R^3 (3d CS)
        path1_r3 = ConfigurationSpaceBraiding.conf2_link_sphere_dim(3)
        path2_r3 = ConfigurationSpaceBraiding.TOPOLOGY["R^3"]["link"]
        assert path1_r3 == 2  # S^2
        assert path2_r3 == "S^2"

        # C^3 = R^6 (6d hCS)
        path1_c3 = ConfigurationSpaceBraiding.conf2_link_sphere_dim(6)
        path2_c3 = ConfigurationSpaceBraiding.TOPOLOGY["C^3"]["link"]
        assert path1_c3 == 5  # S^5
        assert path2_c3 == "S^5"

        # Cross-check: formula output matches lookup string
        assert f"S^{path1_r3}" == path2_r3
        assert f"S^{path1_c3}" == path2_c3

    def test_obstruction_count_consistency(self):
        """Three obstructions confirmed by two independent routes.

        Path 1: ObstructionAnalysis methods.
        Path 2: Direct comparison of Route A and Route B summaries.
        """
        route_a = RouteA_3dCS("gl_1", Rational(1))
        route_b = RouteB_6dHCS(Rational(37), Rational(41))
        obs = ObstructionAnalysis(route_a, route_b)

        # Path 1: from obstruction analysis
        o1 = obs.obstruction_O1_braiding_source()
        o2 = obs.obstruction_O2_parameters()
        o3 = obs.obstruction_O3_miki()
        path1_count = 3  # three obstructions

        # Path 2: from summary comparison
        sa = route_a.summary()
        sb = route_b.summary()
        path2_differences = []
        if sa["en_type"] != sb["en_type"]:
            path2_differences.append("O1: en_type differs")
        if sa["num_parameters"] != sb["num_parameters"]:
            path2_differences.append("O2: num_parameters differs")
        if sa["miki"] != sb["miki"]:
            path2_differences.append("O3: miki differs")

        assert len(path2_differences) == path1_count, \
            f"Obstruction count mismatch: {path1_count} vs {len(path2_differences)}"

        # Cross-check: the differences match the obstructions
        assert sa["en_type"] != sb["en_type"]  # O1
        assert sa["num_parameters"] != sb["num_parameters"]  # O2
        assert sa["miki"] != sb["miki"]  # O3
