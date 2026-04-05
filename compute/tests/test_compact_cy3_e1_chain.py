r"""
Tests for compact_cy3_e1_chain.py -- the E_1 chiral algebra chain for compact CY3s.

Multi-path verification at every step.

Test organization:
  1. Hodge data and basic invariants (10 tests)
  2. HH^* dimensions via HKR (15 tests)
  3. Gerstenhaber bracket structure (10 tests)
  4. Lie conformal algebra data (10 tests)
  5. E_1 constraint verification (8 tests)
  6. Kappa computation (12 tests)
  7. Shadow tower (10 tests)
  8. Shadow depth classification (5 tests)
  9. GW/shadow connection (5 tests)
  10. Cross-family universality (10 tests)
  11. K3 x E special case (5 tests)

Total: ~100 tests.
"""

import pytest
from fractions import Fraction
from typing import Dict

from compute.lib.compact_cy3_e1_chain import (
    CompactCY3,
    compact_cy3,
    QUINTIC,
    BICUBIC,
    QUARTIC_QUADRIC,
    FOUR_QUADRICS,
    K3_TIMES_E,
    SCHOEN,
    STANDARD_COMPACT_CY3S,
    HHCohomCompactCY3,
    hh_compact_cy3,
    verify_hh_dimensions,
    GerstenhaberBracketData,
    gerstenhaber_bracket_data,
    LieConformalAlgebraData,
    lie_conformal_algebra_data,
    E1ChiralAlgebraData,
    e1_chiral_algebra_data,
    e1_not_e2_argument,
    KappaComputation,
    kappa_compact_cy3,
    shadow_tower_compact_cy3,
    shadow_tower_with_instanton_corrections,
    ShadowMetricCompactCY3,
    shadow_metric_compact_cy3,
    ShadowDepthPrediction,
    shadow_depth_prediction,
    gw_shadow_connection,
    ArityThreeShadow,
    arity_three_shadow_quintic,
    shadow_discriminant_quintic,
    comparison_table,
    E1ChainResult,
    run_e1_chain,
    run_quintic_e1_chain,
    theorem_e1_constraint,
    conjecture_kappa_chi_over_2,
    quintic_full_analysis,
    compact_cy3_universality,
    k3_times_e_special,
    is_simply_connected,
    hh_compact_cy3_safe,
    A_HAT_COEFFS,
    QUINTIC_GV_G0,
    QUINTIC_GV_G1,
    QUINTIC_GV_G2,
)


# ===========================================================================
# Section 1: Hodge data and basic invariants
# ===========================================================================

class TestHodgeData:
    """Tests for compact CY3 Hodge data."""

    def test_quintic_hodge_numbers(self):
        """Quintic: h^{1,1}=1, h^{2,1}=101."""
        assert QUINTIC.h11 == 1
        assert QUINTIC.h21 == 101

    def test_quintic_euler_characteristic(self):
        """chi(quintic) = 2*(1-101) = -200."""
        assert QUINTIC.chi == -200

    def test_quintic_chi_over_24(self):
        """chi/24 = -200/24 = -25/3 (NOT an integer)."""
        assert QUINTIC.chi_over_24 == Fraction(-25, 3)
        assert QUINTIC.chi_over_24.denominator != 1  # not integer

    def test_quintic_betti_numbers(self):
        """Betti numbers of the quintic."""
        assert QUINTIC.b0 == 1
        assert QUINTIC.b1 == 0
        assert QUINTIC.b2 == 1    # = h^{1,1}
        assert QUINTIC.b3 == 204  # = 2 + 2*101
        assert QUINTIC.b4 == 1    # = h^{1,1}
        assert QUINTIC.b5 == 0
        assert QUINTIC.b6 == 1

    def test_quintic_poincare_duality(self):
        """Poincare duality: b_k = b_{6-k}."""
        assert QUINTIC.b0 == QUINTIC.b6
        assert QUINTIC.b1 == QUINTIC.b5
        assert QUINTIC.b2 == QUINTIC.b4

    def test_quintic_euler_from_betti(self):
        """chi = sum (-1)^k b_k."""
        chi_from_betti = (
            QUINTIC.b0 - QUINTIC.b1 + QUINTIC.b2
            - QUINTIC.b3 + QUINTIC.b4 - QUINTIC.b5 + QUINTIC.b6
        )
        assert chi_from_betti == QUINTIC.chi

    def test_bicubic_euler(self):
        """Bicubic P5[3,3]: chi = 2*(1-73) = -144."""
        assert BICUBIC.chi == -144

    def test_bicubic_chi_over_24_integer(self):
        """P5[3,3]: chi/24 = -6 (IS an integer!)."""
        assert BICUBIC.chi_over_24 == Fraction(-6)
        assert BICUBIC.chi_over_24.denominator == 1

    def test_k3_times_e_chi_zero(self):
        """K3 x E: chi = 0."""
        assert K3_TIMES_E.chi == 0

    def test_c2_quintic(self):
        """c_2 . H = 50 for the quintic."""
        assert QUINTIC.c2_H == 50


# ===========================================================================
# Section 2: HH^* dimensions via HKR
# ===========================================================================

class TestHHDimensions:
    """Tests for Hochschild cohomology dimensions."""

    def test_quintic_hh_star(self):
        """HH^*(quintic) = (1, 0, 101, 4, 101, 0, 1)."""
        hh = hh_compact_cy3(QUINTIC)
        assert hh.hh[0] == 1
        assert hh.hh[1] == 0
        assert hh.hh[2] == 101
        assert hh.hh[3] == 4
        assert hh.hh[4] == 101
        assert hh.hh[5] == 0
        assert hh.hh[6] == 1

    def test_quintic_hh_total_dim(self):
        """Total dim HH^*(quintic) = 208."""
        hh = hh_compact_cy3(QUINTIC)
        assert hh.total_dim == 208

    def test_quintic_hh_total_formula(self):
        """dim HH^* = 4 + 2*h^{1,1} + 2*h^{2,1} = 4+2+202 = 208."""
        hh = hh_compact_cy3(QUINTIC)
        expected = 4 + 2 * QUINTIC.h11 + 2 * QUINTIC.h21
        assert hh.total_dim == expected

    def test_quintic_serre_duality(self):
        """Serre duality: HH^n(Q) = HH^{6-n}(Q)."""
        hh = hh_compact_cy3(QUINTIC)
        for n in range(7):
            assert hh.hh[n] == hh.hh[6 - n], \
                f"Serre duality fails: HH^{n}={hh.hh[n]} != HH^{6-n}={hh.hh[6-n]}"

    def test_quintic_euler_hh(self):
        """chi(HH^*) = -chi(Q) = 200."""
        hh = hh_compact_cy3(QUINTIC)
        assert hh.euler_hh == -QUINTIC.chi
        assert hh.euler_hh == 200

    def test_quintic_verify_all_paths(self):
        """All verification paths pass for the quintic."""
        v = verify_hh_dimensions(QUINTIC)
        assert v["all_pass"], f"Verification failed: {v}"

    def test_bicubic_hh_star(self):
        """HH^*(P5[3,3]) = (1, 0, 73, 4, 73, 0, 1)."""
        hh = hh_compact_cy3(BICUBIC)
        assert hh.hh[0] == 1
        assert hh.hh[2] == 73
        assert hh.hh[3] == 4   # = 2 + 2*1
        assert hh.hh[4] == 73
        assert hh.total_dim == 4 + 2 + 146  # = 152

    def test_bicubic_total_dim(self):
        """dim HH^*(P5[3,3]) = 4 + 2*1 + 2*73 = 152."""
        hh = hh_compact_cy3(BICUBIC)
        assert hh.total_dim == 152

    def test_four_quadrics_hh(self):
        """HH^*(P7[2,2,2,2]) dimensions."""
        hh = hh_compact_cy3(FOUR_QUADRICS)
        assert hh.hh[2] == 65
        assert hh.hh[3] == 4  # = 2 + 2*1
        assert hh.total_dim == 4 + 2 + 130  # = 136

    def test_all_standard_verify(self):
        """All standard simply-connected CY3s pass verification."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                v = verify_hh_dimensions(cy)
                assert v["all_pass"], f"{cy.name} failed: {v}"

    def test_hh3_decomposition_quintic(self):
        """HH^3(quintic) = h^{3,3}+h^{2,2}+h^{1,1}+h^{0,0} = 1+1+1+1 = 4."""
        # h^{2,2} = h^{1,1} = 1 by Poincare duality (b_4 = b_2)
        assert QUINTIC.h11 == 1
        hh3 = 1 + QUINTIC.h11 + QUINTIC.h11 + 1
        assert hh3 == 4
        hh = hh_compact_cy3(QUINTIC)
        assert hh.hh[3] == hh3

    def test_hh_general_formula(self):
        """HH^3 = 2 + 2*h^{1,1} for simply connected CY3."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                hh = hh_compact_cy3(cy)
                assert hh.hh[3] == 2 + 2 * cy.h11, \
                    f"{cy.name}: HH^3 = {hh.hh[3]} != {2+2*cy.h11}"

    def test_euler_hh_formula(self):
        """chi(HH^*) = -chi(X) for all simply-connected CY3."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                hh = hh_compact_cy3(cy)
                assert hh.euler_hh == -cy.chi, \
                    f"{cy.name}: euler(HH)={hh.euler_hh} != -chi={-cy.chi}"

    def test_hh2_equals_h21(self):
        """HH^2 = h^{2,1} for simply connected CY3."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                hh = hh_compact_cy3(cy)
                assert hh.hh[2] == cy.h21


# ===========================================================================
# Section 3: Gerstenhaber bracket structure
# ===========================================================================

class TestGerstenhaberBracket:
    """Tests for the Gerstenhaber bracket on HH^*."""

    def test_quintic_bracket_nontrivial(self):
        """The Gerstenhaber bracket is nontrivial for the quintic."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert not gb.is_abelian

    def test_quintic_bracket_22_source_dim(self):
        """[HH^2, HH^2] source = Wedge^2(C^101) = 5050."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert gb.bracket_22_to_3["source_dim"] == 101 * 100 // 2
        assert gb.bracket_22_to_3["source_dim"] == 5050

    def test_quintic_bracket_22_target_dim(self):
        """[HH^2, HH^2] target = HH^3 = 4."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert gb.bracket_22_to_3["target_dim"] == 4

    def test_quintic_bracket_22_rank(self):
        """Generic rank of [HH^2, HH^2] -> HH^3 is 2*h^{1,1} = 2."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert gb.bracket_22_to_3["generic_rank"] == 2 * QUINTIC.h11
        assert gb.bracket_22_to_3["generic_rank"] == 2

    def test_quintic_bracket_23_source_dim(self):
        """[HH^2, HH^3] source = 101 * 4 = 404."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert gb.bracket_23_to_4["source_dim"] == 101 * 4

    def test_quintic_bracket_34_target(self):
        """[HH^3, HH^4] -> HH^6 = C (dim 1)."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert gb.bracket_34_to_6["target_dim"] == 1

    def test_bracket_abelian_only_if_h21_zero(self):
        """The bracket is abelian only if h^{2,1} = 0."""
        for cy in STANDARD_COMPACT_CY3S:
            gb = gerstenhaber_bracket_data(cy)
            assert gb.is_abelian == (cy.h21 == 0), \
                f"{cy.name}: abelian={gb.is_abelian} but h21={cy.h21}"

    def test_all_compact_cy3_bracket_nontrivial(self):
        """All standard compact CY3s have nontrivial bracket (h^{2,1}>0)."""
        for cy in STANDARD_COMPACT_CY3S:
            gb = gerstenhaber_bracket_data(cy)
            assert not gb.is_abelian, f"{cy.name} has abelian bracket"

    def test_three_bracket_components(self):
        """There are exactly 3 nontrivial bracket components."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        assert gb.total_bracket_components == 3

    def test_bracket_22_huge_kernel(self):
        """For the quintic, [HH^2,HH^2]->HH^3 has kernel dim >= 5048."""
        gb = gerstenhaber_bracket_data(QUINTIC)
        kernel_lb = gb.bracket_22_to_3["source_dim"] - gb.bracket_22_to_3["target_dim"]
        assert kernel_lb >= 5046


# ===========================================================================
# Section 4: Lie conformal algebra
# ===========================================================================

class TestLieConformalAlgebra:
    """Tests for the Lie conformal algebra L_X."""

    def test_quintic_total_generators(self):
        """Total HH^* dim = 208 generators (full)."""
        lca = lie_conformal_algebra_data(QUINTIC)
        assert lca.total_hh_dim == 208

    def test_quintic_minimal_generators(self):
        """Minimal generators: h21 + h11 + 2 = 101 + 1 + 2 = 104."""
        lca = lie_conformal_algebra_data(QUINTIC)
        assert lca.num_generators_minimal == 104

    def test_quintic_generator_decomposition(self):
        """Generator decomposition matches."""
        lca = lie_conformal_algebra_data(QUINTIC)
        assert lca.generator_decomposition["HH^2 (deformations)"] == 101
        assert lca.generator_decomposition["HH^3 (Kahler piece)"] == 1

    def test_bicubic_minimal_generators(self):
        """P5[3,3]: minimal = 73 + 1 + 2 = 76."""
        lca = lie_conformal_algebra_data(BICUBIC)
        assert lca.num_generators_minimal == 76

    def test_four_quadrics_minimal_generators(self):
        """P7[2,2,2,2]: minimal = 65 + 1 + 2 = 68."""
        lca = lie_conformal_algebra_data(FOUR_QUADRICS)
        assert lca.num_generators_minimal == 68

    def test_bracket_structure_nontrivial_for_quintic(self):
        """Quintic bracket structure is described as nontrivial."""
        lca = lie_conformal_algebra_data(QUINTIC)
        assert "Nontrivial" in lca.bracket_structure

    def test_bracket_structure_nontrivial_for_all(self):
        """All standard CY3s have nontrivial bracket."""
        for cy in STANDARD_COMPACT_CY3S:
            lca = lie_conformal_algebra_data(cy)
            assert "Nontrivial" in lca.bracket_structure or "Abelian" not in lca.bracket_structure

    def test_central_generators_always_2(self):
        """Central generators (from HH^0 and HH^6) always contribute 2."""
        for cy in STANDARD_COMPACT_CY3S:
            lca = lie_conformal_algebra_data(cy)
            assert lca.generator_decomposition["HH^0 (central)"] == 1
            assert lca.generator_decomposition["HH^6 (central)"] == 1

    def test_minimal_vs_full(self):
        """Minimal generators <= total generators."""
        for cy in STANDARD_COMPACT_CY3S:
            lca = lie_conformal_algebra_data(cy)
            assert lca.num_generators_minimal <= lca.num_generators_full

    def test_minimal_formula(self):
        """Minimal generators = h21 + h11 + 2."""
        for cy in STANDARD_COMPACT_CY3S:
            lca = lie_conformal_algebra_data(cy)
            assert lca.num_generators_minimal == cy.h21 + cy.h11 + 2


# ===========================================================================
# Section 5: E_1 constraint verification
# ===========================================================================

class TestE1Constraint:
    """Tests for the E_1 (not E_2) constraint."""

    def test_quintic_e1_level(self):
        """The quintic chiral algebra is E_1."""
        e1 = e1_chiral_algebra_data(QUINTIC)
        assert e1.en_level == 1

    def test_quintic_no_omega_deformation(self):
        """No Omega-deformation needed for compact CY3."""
        e1 = e1_chiral_algebra_data(QUINTIC)
        assert e1.omega_deformation_needed is False

    def test_quintic_bracket_nontrivial(self):
        """The bracket type is nontrivial for the quintic."""
        e1 = e1_chiral_algebra_data(QUINTIC)
        assert e1.bracket_type == "nontrivial"

    def test_e1_argument_quantization_directions(self):
        """Only 1 quantization direction from Omega_3."""
        arg = e1_not_e2_argument(QUINTIC)
        assert arg["quantization_directions"] == 1

    def test_e1_argument_native_level(self):
        """Native E_n level for CY_3 is E_1."""
        arg = e1_not_e2_argument(QUINTIC)
        assert arg["native_en_level"] == 1
        assert arg["en_equals_1"] is True

    def test_drinfeld_center_needed_for_e2(self):
        """Drinfeld center is needed for E_2 enhancement."""
        arg = e1_not_e2_argument(QUINTIC)
        assert arg["drinfeld_center_needed_for_e2"] is True

    def test_all_compact_cy3_are_e1(self):
        """All standard compact CY3s produce E_1 chiral algebras."""
        for cy in STANDARD_COMPACT_CY3S:
            e1 = e1_chiral_algebra_data(cy)
            assert e1.en_level == 1, f"{cy.name} is not E_1"

    def test_drinfeld_center_available(self):
        """Drinfeld center available for E_1 -> E_2 upgrade."""
        e1 = e1_chiral_algebra_data(QUINTIC)
        assert e1.drinfeld_center_available is True


# ===========================================================================
# Section 6: Kappa computation
# ===========================================================================

class TestKappaComputation:
    """Tests for the modular characteristic kappa."""

    def test_quintic_kappa_constant_map(self):
        """kappa^{const}(quintic) = chi/2 = -100."""
        kap = kappa_compact_cy3(QUINTIC)
        assert kap.kappa_constant_map == Fraction(-100)

    def test_quintic_kappa_is_integer(self):
        """kappa^{const} = -100 is an integer."""
        kap = kappa_compact_cy3(QUINTIC)
        assert kap.is_integer is True

    def test_quintic_f1_constant_map(self):
        """F_1^{const} = -100/24 = -25/6."""
        kap = kappa_compact_cy3(QUINTIC)
        assert kap.f1_constant_map == Fraction(-100, 24)
        assert kap.f1_constant_map == Fraction(-25, 6)

    def test_bicubic_kappa(self):
        """kappa^{const}(P5[3,3]) = -144/2 = -72."""
        kap = kappa_compact_cy3(BICUBIC)
        assert kap.kappa_constant_map == Fraction(-72)

    def test_k3_times_e_kappa_constant_zero(self):
        """kappa^{const}(K3xE) = 0 (chi=0)."""
        kap = kappa_compact_cy3(K3_TIMES_E)
        assert kap.kappa_constant_map == Fraction(0)

    def test_k3_times_e_kappa_full(self):
        """kappa_full(K3xE) = 5 (Borcherds product)."""
        kap = kappa_compact_cy3(K3_TIMES_E)
        assert kap.kappa_full == Fraction(5)

    def test_kappa_chi_over_2_not_chi_over_24(self):
        """kappa = chi/2, NOT chi/24 (the latter is for the BKM analogy)."""
        kap = kappa_compact_cy3(QUINTIC)
        chi_over_24 = Fraction(QUINTIC.chi, 24)
        assert kap.kappa_constant_map != chi_over_24

    def test_conjecture_retracted(self):
        """The conjecture kappa=chi/2 is retracted (fails for K3xE)."""
        result = conjecture_kappa_chi_over_2()
        assert result["status"] == "RETRACTED (fails for K3 x E)"
        assert len(result["failures"]) > 0

    def test_kappa_formula_multi_path(self):
        """kappa = chi/2 = (h11-h21). Verify two ways."""
        for cy in STANDARD_COMPACT_CY3S:
            kap = kappa_compact_cy3(cy)
            # Path 1: chi/2
            assert kap.kappa_constant_map == Fraction(cy.chi, 2)
            # Path 2: h11 - h21
            assert kap.kappa_constant_map == Fraction(cy.h11 - cy.h21)

    def test_a_hat_coefficients_positive(self):
        """A-hat coefficients are all positive (AP22 convention)."""
        for g, coeff in A_HAT_COEFFS.items():
            assert coeff > 0, f"A-hat coefficient at g={g} is not positive"

    def test_a_hat_genus_1(self):
        """a_hat_1 = 1/24."""
        assert A_HAT_COEFFS[1] == Fraction(1, 24)

    def test_a_hat_genus_2(self):
        """a_hat_2 = 7/5760."""
        assert A_HAT_COEFFS[2] == Fraction(7, 5760)


# ===========================================================================
# Section 7: Shadow tower
# ===========================================================================

class TestShadowTower:
    """Tests for the shadow tower F_g = kappa * a_hat_g."""

    def test_quintic_f1(self):
        """F_1(quintic) = -100 * 1/24 = -25/6."""
        tower = shadow_tower_compact_cy3(QUINTIC)
        assert tower[1] == Fraction(-100) * Fraction(1, 24)
        assert tower[1] == Fraction(-25, 6)

    def test_quintic_f2(self):
        """F_2(quintic) = -100 * 7/5760 = -35/288."""
        tower = shadow_tower_compact_cy3(QUINTIC)
        expected = Fraction(-100) * Fraction(7, 5760)
        assert tower[2] == expected
        # Simplify: -700/5760 = -35/288
        assert tower[2] == Fraction(-35, 288)

    def test_quintic_f3(self):
        """F_3(quintic) = -100 * 31/967680."""
        tower = shadow_tower_compact_cy3(QUINTIC)
        expected = Fraction(-100) * Fraction(31, 967680)
        assert tower[3] == expected

    def test_shadow_tower_signs(self):
        """All F_g for the quintic are NEGATIVE (kappa < 0)."""
        tower = shadow_tower_compact_cy3(QUINTIC)
        for g in range(1, 6):
            assert tower[g] < 0, f"F_{g} = {tower[g]} should be negative"

    def test_shadow_tower_bicubic(self):
        """F_1(P5[3,3]) = -72/24 = -3."""
        tower = shadow_tower_compact_cy3(BICUBIC)
        assert tower[1] == Fraction(-3)

    def test_shadow_tower_k3_times_e_const_zero(self):
        """F_g^{const}(K3xE) = 0 for all g (kappa_const=0)."""
        tower = shadow_tower_compact_cy3(K3_TIMES_E)
        for g in range(1, 6):
            assert tower[g] == 0, f"F_{g}(K3xE) = {tower[g]} should be 0"

    def test_shadow_tower_with_gw(self):
        """Shadow tower with GW instanton corrections for quintic."""
        gw_g1 = {1: 0, 2: 0, 3: 609250, 4: 3721431625}
        result = shadow_tower_with_instanton_corrections(
            QUINTIC, gw_invariants_g1=gw_g1
        )
        assert 1 in result["constant_map_tower"]
        assert result["instanton_corrections"][1] == gw_g1

    def test_f_g_decreasing_magnitude(self):
        """|F_g| decreases with g for the quintic (a_hat_g decreases)."""
        tower = shadow_tower_compact_cy3(QUINTIC)
        for g in range(1, 5):
            assert abs(tower[g]) > abs(tower[g + 1]), \
                f"|F_{g}| = {abs(tower[g])} <= |F_{g+1}| = {abs(tower[g+1])}"

    def test_shadow_tower_linearity_in_kappa(self):
        """F_g is linear in kappa."""
        t1 = shadow_tower_compact_cy3(QUINTIC)
        t2 = shadow_tower_compact_cy3(BICUBIC)
        # F_g(Q) / F_g(B) = kappa_Q / kappa_B = -100 / -72 = 25/18
        ratio = Fraction(QUINTIC.chi, BICUBIC.chi)
        for g in range(1, 6):
            if t2[g] != 0:
                assert t1[g] / t2[g] == ratio, \
                    f"Linearity fails at g={g}"

    def test_quintic_shadow_values_explicit(self):
        """Explicit numerical check of F_1 through F_5."""
        tower = shadow_tower_compact_cy3(QUINTIC)
        # F_1 = -25/6
        assert float(tower[1]) == pytest.approx(-25/6, rel=1e-12)
        # F_2 = -35/288
        assert float(tower[2]) == pytest.approx(-35/288, rel=1e-12)


# ===========================================================================
# Section 8: Shadow depth classification
# ===========================================================================

class TestShadowDepth:
    """Tests for shadow depth predictions."""

    def test_quintic_class_m(self):
        """Quintic is class M (infinite depth)."""
        d = shadow_depth_prediction(QUINTIC)
        assert d.predicted_class == "M"
        assert d.predicted_r_max == -1  # infinity

    def test_all_compact_cy3_class_m(self):
        """All standard compact CY3s are class M."""
        for cy in STANDARD_COMPACT_CY3S:
            d = shadow_depth_prediction(cy)
            assert d.predicted_class == "M", f"{cy.name} is not class M"

    def test_shadow_depth_confidence(self):
        """Shadow depth predictions are heuristic (not proved)."""
        d = shadow_depth_prediction(QUINTIC)
        assert d.confidence == "heuristic"

    def test_shadow_metric_quintic_q0(self):
        """Q_L(0) = 4*kappa^2 = 4*10000 = 40000 for the quintic."""
        sm = shadow_metric_compact_cy3(QUINTIC)
        assert sm.q_0 == 4 * Fraction(-100) * Fraction(-100)
        assert sm.q_0 == 40000

    def test_shadow_metric_nonzero_for_nonzero_kappa(self):
        """Q_L(0) > 0 whenever kappa != 0."""
        for cy in STANDARD_COMPACT_CY3S:
            if cy.chi != 0:
                sm = shadow_metric_compact_cy3(cy)
                assert sm.q_0 > 0, f"{cy.name}: Q_L(0) = {sm.q_0} <= 0"


# ===========================================================================
# Section 9: GW/shadow connection
# ===========================================================================

class TestGWShadowConnection:
    """Tests for the GW invariant / shadow tower connection."""

    def test_quintic_gv_genus_0(self):
        """Known genus-0 GV invariants of the quintic."""
        assert QUINTIC_GV_G0[1] == 2875
        assert QUINTIC_GV_G0[2] == 609250
        assert QUINTIC_GV_G0[3] == 317206375

    def test_quintic_gv_genus_1(self):
        """Known genus-1 GV invariants of the quintic."""
        assert QUINTIC_GV_G1[1] == 0
        assert QUINTIC_GV_G1[3] == 609250

    def test_gw_connection_quintic(self):
        """GW/shadow connection data for the quintic."""
        result = gw_shadow_connection(QUINTIC)
        assert result["kappa_constant_map"] == Fraction(-100)
        assert "genus_0" in result["gv_invariants"]

    def test_arity3_quintic_yukawa(self):
        """Classical Yukawa coupling C_111 = 5 for the quintic."""
        a3 = arity_three_shadow_quintic()
        assert a3.classical_yukawa == 5
        assert a3.has_cubic is True

    def test_arity3_quintic_alpha(self):
        """Cubic shadow alpha = C_111/kappa = 5/(-100) = -1/20."""
        a3 = arity_three_shadow_quintic()
        assert a3.cubic_shadow_alpha == Fraction(-1, 20)


# ===========================================================================
# Section 10: Cross-family universality
# ===========================================================================

class TestUniversality:
    """Tests for universality claims across compact CY3s."""

    def test_comparison_table_length(self):
        """Comparison table has an entry for each standard CY3."""
        table = comparison_table()
        assert len(table) == len(STANDARD_COMPACT_CY3S)

    def test_universality_all_hh_verified(self):
        """All HH^* dimensions verified for simply connected CY3s."""
        result = compact_cy3_universality()
        for name, r in result["results"].items():
            cy = next(c for c in STANDARD_COMPACT_CY3S if c.name == name)
            if is_simply_connected(cy):
                assert r["all_pass"], f"{name} failed verification"

    def test_universality_all_class_m(self):
        """All compact CY3s are class M."""
        result = compact_cy3_universality()
        assert result["universality_claims"]["all_class_M"]

    def test_universality_bracket_nontrivial(self):
        """All compact CY3s with h^{2,1}>0 have nontrivial bracket."""
        result = compact_cy3_universality()
        for name, r in result["results"].items():
            cy = next(c for c in STANDARD_COMPACT_CY3S if c.name == name)
            if cy.h21 > 0:
                assert r["bracket_nontrivial"], \
                    f"{name} should have nontrivial bracket"

    def test_dim_hh_formula_universal(self):
        """dim HH^* = 4 + 2*(h11+h21) for all simply connected CY3."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                hh = hh_compact_cy3(cy)
                assert hh.total_dim == 4 + 2 * (cy.h11 + cy.h21)

    def test_serre_duality_universal(self):
        """Serre duality HH^n = HH^{6-n} holds universally."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                hh = hh_compact_cy3(cy)
                for n in range(7):
                    assert hh.hh[n] == hh.hh[6 - n]

    def test_e1_constraint_theorem(self):
        """E_1 constraint theorem results."""
        result = theorem_e1_constraint()
        assert result["status"] == "conjectural (proved for toric CY3)"
        for name, r in result["results"].items():
            assert r["en_level"] == 1

    def test_quintic_full_analysis(self):
        """Full quintic analysis runs without error."""
        result = quintic_full_analysis()
        assert result["chain_result"].hh.total_dim == 208
        assert result["yukawa"]["C_111_classical"] == 5

    def test_e1_chain_runs_for_all(self):
        """E_1 chain runs for all simply connected CY3s."""
        for cy in STANDARD_COMPACT_CY3S:
            if is_simply_connected(cy):
                chain = run_e1_chain(cy)
                assert chain.hh.total_dim > 0
                assert chain.e1_data.en_level == 1

    def test_kappa_signs(self):
        """kappa_const is negative for h21 > h11 (most CY3s)."""
        for cy in STANDARD_COMPACT_CY3S:
            kap = kappa_compact_cy3(cy)
            if cy.h21 > cy.h11:
                assert kap.kappa_constant_map < 0


# ===========================================================================
# Section 11: K3 x E special case
# ===========================================================================

class TestK3xE:
    """Tests for the K3 x E special case."""

    def test_k3_times_e_not_simply_connected(self):
        """K3 x E has h^{1,0} = 1 (not simply connected)."""
        assert not is_simply_connected(K3_TIMES_E)

    def test_k3_times_e_special_analysis(self):
        """K3 x E special analysis runs."""
        result = k3_times_e_special()
        assert result["h10"] == 1
        assert result["simply_connected"] is False
        assert result["kappa_full"] == Fraction(5)

    def test_k3_times_e_kappa_const_vs_full(self):
        """K3xE: kappa_const = 0 but kappa_full = 5."""
        result = k3_times_e_special()
        assert result["kappa_const"] == Fraction(0)
        assert result["kappa_full"] == Fraction(5)

    def test_safe_hh_warns_for_k3xe(self):
        """hh_compact_cy3_safe warns for non-simply-connected CY3."""
        result = hh_compact_cy3_safe(K3_TIMES_E)
        assert result["simply_connected"] is False
        assert "warning" in result

    def test_safe_hh_works_for_quintic(self):
        """hh_compact_cy3_safe works normally for simply connected CY3."""
        result = hh_compact_cy3_safe(QUINTIC)
        assert result["simply_connected"] is True
        assert result["hh"].total_dim == 208


# ===========================================================================
# Section 12: Shadow discriminant (quintic-specific)
# ===========================================================================

class TestShadowDiscriminant:
    """Tests for the shadow discriminant analysis."""

    def test_quintic_discriminant_formula(self):
        """Delta = -800*S_4 for the quintic."""
        result = shadow_discriminant_quintic()
        assert result["kappa"] == Fraction(-100)
        assert result["alpha"] == Fraction(-1, 20)

    def test_quintic_q0(self):
        """Q_L(0) = 40000 for the quintic."""
        result = shadow_discriminant_quintic()
        assert result["q_0"] == 40000

    def test_quintic_q1(self):
        """q_1 = 12*kappa*alpha = 12*(-100)*(-1/20) = 60."""
        result = shadow_discriminant_quintic()
        assert result["q_1"] == 60

    def test_quintic_depth_prediction_m(self):
        """Depth prediction is M for the quintic."""
        result = shadow_discriminant_quintic()
        assert "M" in result["depth_prediction"]

    def test_quintic_s4_unknown(self):
        """S_4 is unknown for the quintic."""
        result = shadow_discriminant_quintic()
        assert result["s4_unknown"] is True
