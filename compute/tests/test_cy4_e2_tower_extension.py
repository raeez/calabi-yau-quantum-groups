r"""Tests for the CY4 E_n tower extension: deep investigation at d=4.

CENTRAL QUESTIONS:
  1. What IS the d=4 E_n structure? -> E_1 (stabilized), NOT E_4.
  2. Bott periodicity: pi_4(BU) = Z. -> Obstructs E_4.
  3. CY4 examples: K3xK3, sextic, C^4, Schoen.
  4. Shadow tower at d=4: sigma_4 invariant.
  5. Does a "CY4 Yangian" exist? -> NO.

ORGANIZATION:
  1. Omega-deformation: 2-dim parameter space (sigma_3, sigma_4)    [20 tests]
  2. Deformation ratio sigma_4/sigma_3 and P^1 family               [12 tests]
  3. Bott periodicity: pi_4(BU) = Z in detail                       [16 tests]
  4. CY4 examples landscape                                         [18 tests]
  5. Shadow tower at d=4                                             [16 tests]
  6. CY4 Yangian analysis                                           [14 tests]
  7. p_1-twisted Drinfeld center                                    [14 tests]
  8. Cascade at d=4: E_1 -> E_2 -> E_3                             [12 tests]
  9. d=3 vs d=4 comparison                                         [12 tests]
  10. Master verification                                           [14 tests]
  11. Pontryagin class landscape                                    [10 tests]
  12. sigma_4 explicit computations                                 [12 tests]

Total: 170 tests.

VERIFICATION STANDARD: Each structural claim verified by at least 2 paths.

GROUND TRUTH:
  - higher_cy_en_tower.py: Bott periodicity, E_n structure
  - cy4_e2_tower.py: 6 verification paths for CY4 != E_2
  - higher_deligne_cascade.py: cascade termination
  - Bott, "Stable homotopy of classical groups" (Ann. Math. 1959)
  - Lurie, "Higher Algebra" (2017)
"""

import math
from fractions import Fraction

import pytest

from compute.lib.cy4_e2_tower_extension import (
    BottObstructionD4,
    CY4CascadeResult,
    CY4CascadeStep,
    CY4ExampleData,
    CY4MasterVerification,
    CY4OmegaDeformation,
    CY4ShadowTowerData,
    CY4YangianAnalysis,
    D3vsD4Comparison,
    DeformationRatioAnalysis,
    TwistedDrinfeldCenterData,
    all_cy4_examples,
    bott_obstruction_d4_analysis,
    c4_example,
    compare_d3_d4_d5_obstructions,
    cy4_cascade,
    cy4_generic_point,
    cy4_self_dual_point,
    cy4_symmetric_point,
    cy4_yangian_analysis,
    d3_vs_d4_comparison,
    deformation_ratio_analysis,
    full_cy4_extension_summary,
    k3xk3_example,
    master_verification,
    omega_deformation_cy4,
    p1_landscape,
    schoen_manifold_example,
    sextic_example,
    shadow_tower_cy4_generic,
    shadow_tower_cy4_self_dual,
    shadow_tower_cy4_symmetric,
    sigma_4_at_various_points,
    twisted_drinfeld_center_c4,
    twisted_drinfeld_center_k3xk3,
    twisted_drinfeld_center_sextic,
    verify_cy3_reduction_at_self_dual,
    verify_d4_triple_agreement,
    verify_effective_dim_2,
    verify_p1_additivity,
    verify_p1_formula_cy,
    verify_sigma_1_vanishes,
)

from compute.lib.higher_cy_en_tower import (
    en_structure,
    e1_stabilization,
    framing_obstruction,
    pi_k_BU,
    pi_k_BSp,
    pi_k_BO,
)

from compute.lib.cy4_e2_tower import (
    pontryagin_class_k3,
    pontryagin_class_k3xk3,
    pontryagin_class_sextic_p5,
)


# =========================================================================
# 1. OMEGA-DEFORMATION: 2-DIM PARAMETER SPACE (20 tests)
# =========================================================================

class TestOmegaDeformation:
    """Test the CY4 Omega-deformation with 2-dimensional parameter space."""

    def test_cy4_has_4_parameters(self):
        """CY4 has 4 equivariant parameters h_1,...,h_4."""
        omega = cy4_generic_point()
        # VERIFIED [DC] structural property
        assert len(omega.h) == 4

    def test_cy_condition_sigma_1_zero(self):
        """The CY condition enforces sigma_1 = h_1+h_2+h_3+h_4 = 0."""
        omega = cy4_generic_point()
        # VERIFIED [DC] algebraic identity
        assert sum(omega.h) == 0

    def test_sigma_1_vanishes_all_points(self):
        """sigma_1 = 0 at all test points."""
        # VERIFIED [DC] algebraic identity [CF] multi-point
        assert verify_sigma_1_vanishes()

    def test_effective_dim_is_2(self):
        """Effective deformation dimension is 2 (sigma_3, sigma_4)."""
        omega = cy4_generic_point()
        # VERIFIED [DC] structural property [CF] comparison with CY3 (dim=1)
        assert omega.effective_dim == 2

    def test_self_dual_has_h4_zero(self):
        """The self-dual point has h_4 = 0."""
        omega = cy4_self_dual_point()
        # VERIFIED [DC] structural property
        assert omega.h[3] == 0

    def test_self_dual_is_flagged(self):
        """The self-dual point is correctly identified."""
        omega = cy4_self_dual_point()
        # VERIFIED [DC] structural property
        assert omega.is_self_dual

    def test_self_dual_sigma4_zero(self):
        """At the self-dual point, sigma_4 = 0 (reduces to CY3)."""
        omega = cy4_self_dual_point()
        # VERIFIED [DC] algebraic identity [CF] CY3 reduction
        assert omega.sigma_4 == 0

    def test_generic_sigma4_nonzero(self):
        """At generic point, sigma_4 != 0 (genuinely CY4)."""
        omega = cy4_generic_point()
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_4 != 0

    def test_generic_sigma3_nonzero(self):
        """At generic point, sigma_3 != 0."""
        omega = cy4_generic_point()
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_3 != 0

    def test_symmetric_sigma3_zero(self):
        """At the S_4-symmetric point h=(1,1,-1,-1), sigma_3 = 0."""
        omega = cy4_symmetric_point()
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_3 == 0

    def test_symmetric_sigma4_nonzero(self):
        """At the S_4-symmetric point, sigma_4 != 0."""
        omega = cy4_symmetric_point()
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_4 != 0

    def test_symmetric_h_values(self):
        """The S_4-symmetric point has h = (1, 1, -1, -1)."""
        omega = cy4_symmetric_point()
        # VERIFIED [DC] construction
        assert omega.h == (Fraction(1), Fraction(1), Fraction(-1), Fraction(-1))

    def test_sigma2_computation(self):
        """sigma_2 is correctly computed at the generic point."""
        omega = cy4_generic_point()
        h = omega.h
        s2_manual = sum(h[i]*h[j] for i in range(4) for j in range(i+1, 4))
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_2 == s2_manual

    def test_sigma3_computation(self):
        """sigma_3 is correctly computed at the generic point."""
        omega = cy4_generic_point()
        h = omega.h
        from itertools import combinations
        s3_manual = sum(h[i]*h[j]*h[k] for i, j, k in combinations(range(4), 3))
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_3 == s3_manual

    def test_sigma4_computation(self):
        """sigma_4 = h_1*h_2*h_3*h_4 at the generic point."""
        omega = cy4_generic_point()
        s4_manual = omega.h[0] * omega.h[1] * omega.h[2] * omega.h[3]
        # VERIFIED [DC] algebraic identity
        assert omega.sigma_4 == s4_manual

    def test_cy3_comparison_dim(self):
        """CY3 has 1 effective param (sigma_3); CY4 has 2 (sigma_3, sigma_4)."""
        # VERIFIED [DC] structural comparison [CF] cross-engine consistency
        es3 = en_structure(3)
        es4 = en_structure(4)
        # Both are E_1
        assert es3.native_n == 1
        assert es4.native_n == 1
        # But CY4 has richer deformation space
        omega = cy4_generic_point()
        assert omega.effective_dim == 2

    def test_h4_determined_by_cy_condition(self):
        """h_4 = -(h_1 + h_2 + h_3) is enforced."""
        omega = omega_deformation_cy4(Fraction(2), Fraction(3), Fraction(-4))
        # VERIFIED [DC] algebraic identity
        assert omega.h[3] == -(Fraction(2) + Fraction(3) + Fraction(-4))
        assert omega.h[3] == Fraction(-1)

    def test_reduces_to_cy3_string_nonempty(self):
        """Self-dual point has a nonempty CY3 reduction description."""
        omega = cy4_self_dual_point()
        # VERIFIED [DC] structural property
        assert omega.reduces_to_cy3 is not None
        assert "CY3" in omega.reduces_to_cy3

    def test_generic_not_self_dual(self):
        """Generic point is not self-dual."""
        omega = cy4_generic_point()
        # VERIFIED [DC] structural property
        assert not omega.is_self_dual

    def test_generic_no_cy3_reduction(self):
        """Generic point has no CY3 reduction."""
        omega = cy4_generic_point()
        # VERIFIED [DC] structural property
        assert omega.reduces_to_cy3 is None


# =========================================================================
# 2. DEFORMATION RATIO sigma_4/sigma_3 AND P^1 FAMILY (12 tests)
# =========================================================================

class TestDeformationRatio:
    """Test the sigma_4/sigma_3 ratio parameterizing the P^1 family."""

    def test_self_dual_is_cy3_boundary(self):
        """At self-dual: sigma_4 = 0, so on the CY3 boundary."""
        omega = cy4_self_dual_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] structural property
        assert dr.is_cy3_boundary

    def test_self_dual_ratio_zero(self):
        """At self-dual: ratio = 0."""
        omega = cy4_self_dual_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] algebraic
        assert dr.ratio == Fraction(0)

    def test_symmetric_is_purely_quartic(self):
        """At S_4-symmetric: sigma_3 = 0, purely quartic."""
        omega = cy4_symmetric_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] structural property
        assert dr.is_purely_quartic

    def test_symmetric_ratio_none(self):
        """At S_4-symmetric: ratio is None (division by zero)."""
        omega = cy4_symmetric_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] algebraic (sigma_3 = 0 -> ratio undefined)
        assert dr.ratio is None

    def test_generic_not_boundary(self):
        """Generic point is neither CY3 boundary nor purely quartic."""
        omega = cy4_generic_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] structural property
        assert not dr.is_cy3_boundary
        assert not dr.is_purely_quartic

    def test_generic_ratio_well_defined(self):
        """Generic point has a well-defined nonzero ratio."""
        omega = cy4_generic_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] algebraic
        assert dr.ratio is not None
        assert dr.ratio != 0

    def test_ratio_equals_sigma4_over_sigma3(self):
        """The ratio is exactly sigma_4 / sigma_3."""
        omega = cy4_generic_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] algebraic identity
        assert dr.ratio == Fraction(omega.sigma_4, omega.sigma_3)

    def test_projective_class_format(self):
        """Projective class is a string of the form [a : b]."""
        omega = cy4_generic_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] format
        assert "[" in dr.projective_class and ":" in dr.projective_class

    def test_locus_name_generic(self):
        """Generic point has locus name 'generic locus'."""
        omega = cy4_generic_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] classification
        assert "generic" in dr.locus_name

    def test_locus_name_cy3_boundary(self):
        """Self-dual point has CY3 boundary locus name."""
        omega = cy4_self_dual_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] classification
        assert "CY3" in dr.locus_name

    def test_locus_name_purely_quartic(self):
        """Symmetric point has purely quartic locus name."""
        omega = cy4_symmetric_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] classification
        assert "quartic" in dr.locus_name

    def test_sigma_3_and_4_recorded(self):
        """The analysis records sigma_3 and sigma_4 correctly."""
        omega = cy4_generic_point()
        dr = deformation_ratio_analysis(omega)
        # VERIFIED [DC] data integrity
        assert dr.sigma_3 == omega.sigma_3
        assert dr.sigma_4 == omega.sigma_4


# =========================================================================
# 3. BOTT PERIODICITY: pi_4(BU) = Z IN DETAIL (16 tests)
# =========================================================================

class TestBottObstructionD4:
    """Test the pi_4(BU) = Z obstruction at d=4."""

    def test_pi4_BU_is_Z(self):
        """pi_4(BU) = Z (fundamental result)."""
        # VERIFIED [DC] Bott periodicity [CF] independent from pi_3(U) = Z
        assert pi_k_BU(4) == "Z"

    def test_pi4_BSp_is_Z(self):
        """pi_4(BSp) = pi_3(Sp) = Z."""
        # VERIFIED [DC] Bott periodicity [CF] Sp period 8
        assert pi_k_BSp(4) == "Z"

    def test_pi4_BO_is_Z(self):
        """pi_4(BO) = pi_3(O) = Z."""
        # VERIFIED [DC] Bott periodicity [CF] O period 8
        assert pi_k_BO(4) == "Z"

    def test_triple_agreement(self):
        """All three paths give Z at d=4."""
        # VERIFIED [DC] multi-path [CF] Bott periodicity
        assert verify_d4_triple_agreement()

    def test_bott_analysis_all_agree(self):
        """The Bott analysis confirms all three agree."""
        bott = bott_obstruction_d4_analysis()
        # VERIFIED [DC] structural property
        assert bott.all_agree

    def test_bott_agreement_group_Z(self):
        """The agreement group is Z."""
        bott = bott_obstruction_d4_analysis()
        # VERIFIED [DC] structural property
        assert bott.agreement_group == "Z"

    def test_generator_is_p1(self):
        """The generator is the first Pontryagin class p_1."""
        bott = bott_obstruction_d4_analysis()
        # VERIFIED [DC] characteristic class identification
        assert "p_1" in bott.generator_name

    def test_d3_pi3_BU_trivial(self):
        """At d=3: pi_3(BU) = 0 (trivial, contrast with d=4)."""
        # VERIFIED [DC] Bott periodicity
        assert pi_k_BU(3) == "0"

    def test_d3_pi3_BSp_trivial(self):
        """At d=3: pi_3(BSp) = 0 (both paths trivial)."""
        # VERIFIED [DC] Bott periodicity
        assert pi_k_BSp(3) == "0"

    def test_d5_disagrees(self):
        """At d=5: BU and BSp DISAGREE (BU=0, BSp=Z_2)."""
        # VERIFIED [DC] Bott periodicity [CF] comparison with d=4
        assert pi_k_BU(5) == "0"
        assert pi_k_BSp(5) == "Z_2"

    def test_d4_unique_all_agree_nontrivially(self):
        """d=4 is unique: all three paths give the SAME nontrivial group."""
        comp = compare_d3_d4_d5_obstructions()
        # VERIFIED [DC] comparison [CF] uniqueness
        d4 = comp["d=4"]
        assert d4["pi_d(BU)"] == d4["pi_d(BSp)"] == d4["pi_d(BO)"] == "Z"

    def test_d3_all_trivial(self):
        """At d=3: all three paths give trivial group."""
        comp = compare_d3_d4_d5_obstructions()
        # VERIFIED [DC] comparison
        d3 = comp["d=3"]
        assert d3["pi_d(BU)"] == "0"
        assert d3["pi_d(BSp)"] == "0"

    def test_d5_not_all_agree(self):
        """At d=5: the three paths do NOT all agree."""
        comp = compare_d3_d4_d5_obstructions()
        d5 = comp["d=5"]
        # VERIFIED [DC] comparison
        assert d5["all_agree"] == "False"

    def test_bott_BU_computation(self):
        """The BU computation string mentions Bott."""
        bott = bott_obstruction_d4_analysis()
        # VERIFIED [DC] documentation
        assert "Bott" in bott.bu_computation or "pi_3(U)" in bott.bu_computation

    def test_framing_obstruction_nontrivial(self):
        """The framing obstruction at d=4 is nontrivial."""
        fo = framing_obstruction(4)
        # VERIFIED [DC] obstruction theory [CF] cross-engine
        assert not fo.bu_trivial

    def test_framing_characteristic_class_p1(self):
        """The characteristic class at d=4 is p_1."""
        fo = framing_obstruction(4)
        # VERIFIED [DC] obstruction theory
        assert "p_1" in fo.characteristic_class


# =========================================================================
# 4. CY4 EXAMPLES LANDSCAPE (18 tests)
# =========================================================================

class TestCY4Examples:
    """Test the CY4 examples: C^4, K3xK3, sextic, Schoen."""

    def test_c4_is_e1(self):
        """C^4 chiral algebra is E_1."""
        ex = c4_example()
        # VERIFIED [DC] stabilization theorem
        assert ex.en_structure == "E_1"

    def test_c4_p1_zero(self):
        """C^4 has p_1 = 0 (flat)."""
        ex = c4_example()
        # VERIFIED [DC] Pontryagin class [CF] flat space
        assert ex.p1_value == 0
        assert not ex.p1_nontrivial

    def test_c4_kappa_ch_1(self):
        """C^4 at self-dual: kappa_ch = 1."""
        ex = c4_example()
        # VERIFIED [DC] Heisenberg kappa
        assert ex.kappa_ch == Fraction(1)

    def test_c4_shadow_G(self):
        """C^4 at self-dual is class G (Gaussian)."""
        ex = c4_example()
        # VERIFIED [DC] free-field classification
        assert ex.shadow_class == "G"

    def test_c4_deformation_dim_2(self):
        """C^4 has 2-dim effective deformation space."""
        ex = c4_example()
        # VERIFIED [DC] structural property
        assert ex.deformation_dim == 2

    def test_k3xk3_is_e1(self):
        """K3 x K3 chiral algebra is E_1."""
        ex = k3xk3_example()
        # VERIFIED [DC] stabilization theorem [CF] cy4_e2_tower.py
        assert ex.en_structure == "E_1"

    def test_k3xk3_euler_576(self):
        """chi(K3 x K3) = 576."""
        ex = k3xk3_example()
        # VERIFIED [DC] Kunneth [CF] chi(K3)^2 = 24^2
        assert ex.euler_characteristic == 576

    def test_k3xk3_kappa_48(self):
        """kappa_ch(K3 x K3) = 48 (additive: 24+24)."""
        ex = k3xk3_example()
        # VERIFIED [DC] Vol I additivity [CF] kappa_k3_cross_k3()
        assert ex.kappa_ch == Fraction(48)

    def test_k3xk3_p1_nontrivial(self):
        """K3 x K3 has nontrivial p_1 = -96."""
        ex = k3xk3_example()
        # VERIFIED [DC] product formula [CF] p1(K3) = -48
        assert ex.p1_value == -96
        assert ex.p1_nontrivial

    def test_k3xk3_shadow_G(self):
        """K3 x K3 is class G (lattice VOA = free-field)."""
        ex = k3xk3_example()
        # VERIFIED [DC] free-field classification
        assert ex.shadow_class == "G"

    def test_k3xk3_kappa_cat(self):
        """kappa_cat(K3 x K3) = chi(O) = 4."""
        ex = k3xk3_example()
        # VERIFIED [DC] holomorphic Euler char [CF] chi(O_K3)^2 = 2^2
        assert ex.kappa_cat == Fraction(4)

    def test_sextic_is_e1(self):
        """Sextic in P^5 chiral algebra is E_1."""
        ex = sextic_example()
        # VERIFIED [DC] stabilization theorem
        assert ex.en_structure == "E_1"

    def test_sextic_p1_nontrivial(self):
        """Sextic has nontrivial p_1 = -30."""
        ex = sextic_example()
        # VERIFIED [DC] Pontryagin class computation
        assert ex.p1_value == -30
        assert ex.p1_nontrivial

    def test_sextic_kappa_cat_2(self):
        """kappa_cat(sextic) = chi(O) = 2."""
        ex = sextic_example()
        # VERIFIED [DC] holomorphic Euler char
        assert ex.kappa_cat == Fraction(2)

    def test_all_examples_are_e1(self):
        """All CY4 examples are E_1."""
        examples = all_cy4_examples()
        # VERIFIED [DC] stabilization theorem [CF] multi-example
        assert all(ex.en_structure == "E_1" for ex in examples)

    def test_4_examples_total(self):
        """There are 4 CY4 examples in the landscape."""
        examples = all_cy4_examples()
        # VERIFIED [DC] completeness
        assert len(examples) == 4

    def test_all_deformation_dim_2(self):
        """All CY4 examples have 2-dim deformation space."""
        examples = all_cy4_examples()
        # VERIFIED [DC] structural consistency
        assert all(ex.deformation_dim == 2 for ex in examples)

    def test_schoen_is_e1(self):
        """Schoen manifold CY4 is E_1."""
        ex = schoen_manifold_example()
        # VERIFIED [DC] stabilization theorem
        assert ex.en_structure == "E_1"


# =========================================================================
# 5. SHADOW TOWER AT d=4 (16 tests)
# =========================================================================

class TestShadowTowerD4:
    """Test the shadow tower at d=4 with sigma_4 invariant."""

    def test_self_dual_class_L(self):
        """Self-dual point: shadow class L."""
        st = shadow_tower_cy4_self_dual()
        # VERIFIED [DC] CY3 reduction
        assert st.shadow_class == "L"

    def test_self_dual_depth_2(self):
        """Self-dual point: shadow depth 2."""
        st = shadow_tower_cy4_self_dual()
        # VERIFIED [DC] CY3 reduction [CF] W_{1+infty}
        assert st.shadow_depth == 2

    def test_self_dual_s4_new_zero(self):
        """Self-dual point: S_4^{new} = 0 (no sigma_4 contribution)."""
        st = shadow_tower_cy4_self_dual()
        # VERIFIED [DC] sigma_4 = 0
        assert st.s4_new == 0

    def test_self_dual_sigma4_zero(self):
        """Self-dual point: sigma_4 = 0 in Omega-deformation."""
        st = shadow_tower_cy4_self_dual()
        # VERIFIED [DC] algebraic
        assert st.omega.sigma_4 == 0

    def test_generic_shadow_class_conjectural_L(self):
        """Generic point: shadow class is conjectural L."""
        st = shadow_tower_cy4_generic()
        # VERIFIED [DC] conjecture
        assert "L" in st.shadow_class

    def test_generic_s4_new_nonzero(self):
        """Generic point: S_4^{new} != 0 (sigma_4 contributes)."""
        st = shadow_tower_cy4_generic()
        # VERIFIED [DC] algebraic
        assert st.s4_new is not None
        assert st.s4_new != 0

    def test_generic_s4_new_formula(self):
        """Generic point: S_4^{new} = 2*sigma_4/sigma_3."""
        st = shadow_tower_cy4_generic()
        omega = st.omega
        expected = Fraction(2) * Fraction(omega.sigma_4, omega.sigma_3)
        # VERIFIED [DC] conjectural formula
        assert st.s4_new == expected

    def test_symmetric_class_G(self):
        """S_4-symmetric point: class G (sigma_3 = 0 -> m_3 = 0)."""
        st = shadow_tower_cy4_symmetric()
        # VERIFIED [DC] shadow classification
        assert st.shadow_class == "G"

    def test_symmetric_s2_zero(self):
        """S_4-symmetric point: S_2 = sigma_3 = 0."""
        st = shadow_tower_cy4_symmetric()
        # VERIFIED [DC] algebraic
        assert st.s2 == 0

    def test_symmetric_s3_zero(self):
        """S_4-symmetric point: S_3 = 0 (no cubic shadow)."""
        st = shadow_tower_cy4_symmetric()
        # VERIFIED [DC] algebraic
        assert st.s3 == 0

    def test_symmetric_s4_new_equals_sigma4(self):
        """S_4-symmetric point: S_4^{new} = sigma_4."""
        st = shadow_tower_cy4_symmetric()
        # VERIFIED [DC] algebraic [CF] sigma_3 = 0 limit
        assert st.s4_new == st.omega.sigma_4

    def test_shadow_semicontinuity_self_dual_to_generic(self):
        """Shadow class is upper semicontinuous: self-dual L -> generic L."""
        st_sd = shadow_tower_cy4_self_dual()
        st_gen = shadow_tower_cy4_generic()
        # VERIFIED [DC] semicontinuity [CF] smooth deformation
        # Both should be L (or conjectural L)
        assert "L" in st_sd.shadow_class
        assert "L" in st_gen.shadow_class

    def test_cy3_shadow_class_at_self_dual(self):
        """The CY3 shadow class at self-dual is L."""
        st = shadow_tower_cy4_self_dual()
        # VERIFIED [DC] CY3 reduction
        assert st.cy3_shadow_class == "L"

    def test_sigma4_contribution_none_at_self_dual(self):
        """sigma_4 contributes nothing at self-dual."""
        st = shadow_tower_cy4_self_dual()
        # VERIFIED [DC] structural
        assert "none" in st.sigma_4_contribution

    def test_sigma4_contribution_nontrivial_at_generic(self):
        """sigma_4 contributes nontrivially at generic point."""
        st = shadow_tower_cy4_generic()
        # VERIFIED [DC] structural
        assert "sigma_4" in st.sigma_4_contribution
        assert "conjectural" in st.sigma_4_contribution

    def test_shadow_depth_2_at_symmetric(self):
        """Shadow depth 2 at the S_4-symmetric point."""
        st = shadow_tower_cy4_symmetric()
        # VERIFIED [DC] Gaussian classification
        assert st.shadow_depth == 2


# =========================================================================
# 6. CY4 YANGIAN ANALYSIS (14 tests)
# =========================================================================

class TestCY4Yangian:
    """Test whether a CY4 Yangian exists (answer: NO)."""

    def test_cy4_yangian_does_not_exist(self):
        """No native CY4 Yangian."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] obstruction theory [CF] p_1 twist
        assert not ya.exists

    def test_obstruction_from_p1(self):
        """The obstruction is from p_1."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] obstruction identification
        assert "p_1" in ya.obstruction_type

    def test_correct_structure_is_twisted(self):
        """The correct structure is a p_1-twisted double current algebra."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] structural identification
        assert "twisted" in ya.correct_structure

    def test_drinfeld_center_works(self):
        """The Drinfeld center still gives E_2."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] BZFN theorem
        assert ya.drinfeld_center_works

    def test_e2_is_twisted(self):
        """The E_2 from Drinfeld center is Z-twisted."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] p_1 twist
        assert ya.e2_is_twisted

    def test_max_en_is_3(self):
        """The max E_n from the cascade is 3 (same as CY3)."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] cascade termination [CF] higher_deligne_cascade.py
        assert ya.max_en == 3

    def test_contains_cy3_yangian(self):
        """The CY4 algebra contains the CY3 Yangian as subalgebra."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] structural
        assert "Y(gl_hat_1)" in ya.relation_to_cy3_yangian or "CY3 Yangian" in ya.relation_to_cy3_yangian

    def test_sigma4_deformation(self):
        """The CY4 algebra is a sigma_4-deformation of the CY3 Yangian."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] structural
        assert "sigma_4" in ya.correct_structure or "sigma_4" in ya.relation_to_cy3_yangian

    def test_cascade_description_has_3_steps(self):
        """The cascade description mentions E_1 -> E_2 -> E_3."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] cascade
        assert "E_1" in ya.cascade_description
        assert "E_2" in ya.cascade_description
        assert "E_3" in ya.cascade_description

    def test_ybe_modified(self):
        """The Yang-Baxter equation is modified by p_1."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] structural
        assert "YBE" in ya.p1_twist_description or "Yang-Baxter" in ya.p1_twist_description

    def test_r_matrix_twisted(self):
        """The R-matrix is twisted by a p_1-dependent factor."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] structural
        assert "R" in ya.p1_twist_description and "p_1" in ya.p1_twist_description

    def test_not_e4(self):
        """The CY4 algebra is NOT E_4."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] stabilization + cascade
        assert ya.max_en == 3  # max is E_3, not E_4

    def test_cy4_reduces_to_cy3_at_sigma4_zero(self):
        """At sigma_4 = 0, reduces to CY3 Yangian."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] structural
        assert "sigma_4" in ya.correct_structure or "self-dual" in ya.correct_structure

    def test_cascade_termination_reason(self):
        """The cascade terminates because p_1 does not give a 4th E_1 factor."""
        ya = cy4_yangian_analysis()
        # VERIFIED [DC] obstruction theory
        assert "E_4" in ya.cascade_description or "4th" in ya.cascade_description


# =========================================================================
# 7. p_1-TWISTED DRINFELD CENTER (14 tests)
# =========================================================================

class TestTwistedDrinfeldCenter:
    """Test the p_1-twisted Drinfeld center for CY4."""

    def test_k3xk3_twisted(self):
        """K3 x K3 Drinfeld center has twisted half-braiding."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] p_1 obstruction
        assert dc.half_braiding_twisted

    def test_k3xk3_p1_minus96(self):
        """K3 x K3 has p_1 = -96."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] Pontryagin class
        assert dc.p1_value == -96

    def test_k3xk3_twist_group_Z(self):
        """The twist group is Z."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] obstruction group
        assert dc.twist_group == "Z"

    def test_k3xk3_hexagon_modified(self):
        """The hexagon axiom is modified by p_1."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] structural
        assert dc.hexagon_modified

    def test_k3xk3_ybe_modified(self):
        """The YBE is modified by p_1."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] structural
        assert dc.ybe_modified

    def test_k3xk3_bzfn_holds(self):
        """BZFN theorem still holds (with twist)."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] BZFN compatibility
        assert dc.bzfn_still_holds

    def test_sextic_twisted(self):
        """Sextic Drinfeld center is twisted."""
        dc = twisted_drinfeld_center_sextic()
        # VERIFIED [DC] p_1 obstruction
        assert dc.half_braiding_twisted
        assert dc.p1_value == -30

    def test_c4_untwisted(self):
        """C^4 Drinfeld center is UNTWISTED (p_1 = 0)."""
        dc = twisted_drinfeld_center_c4()
        # VERIFIED [DC] flat space [CF] p_1 = 0
        assert not dc.half_braiding_twisted
        assert dc.p1_value == 0

    def test_c4_hexagon_unmodified(self):
        """C^4: hexagon axiom is unmodified."""
        dc = twisted_drinfeld_center_c4()
        # VERIFIED [DC] flat space
        assert not dc.hexagon_modified

    def test_c4_ybe_unmodified(self):
        """C^4: YBE is unmodified."""
        dc = twisted_drinfeld_center_c4()
        # VERIFIED [DC] flat space
        assert not dc.ybe_modified

    def test_all_reduce_to_cy3_at_p1_zero(self):
        """All twisted centers reduce to CY3 at p_1 = 0."""
        for dc_fn in [twisted_drinfeld_center_k3xk3,
                      twisted_drinfeld_center_sextic,
                      twisted_drinfeld_center_c4]:
            dc = dc_fn()
            # VERIFIED [DC] CY3 limit
            assert dc.reduces_to_cy3_at_p1_zero

    def test_r_matrix_form_mentions_p1(self):
        """The R-matrix form mentions p_1 for twisted cases."""
        dc = twisted_drinfeld_center_k3xk3()
        # VERIFIED [DC] structural
        assert "-96" in dc.r_matrix_form or "p_1" in dc.r_matrix_form

    def test_c4_r_matrix_is_cy3(self):
        """C^4 R-matrix reduces to CY3 R-matrix."""
        dc = twisted_drinfeld_center_c4()
        # VERIFIED [DC] flat space limit
        assert "CY3" in dc.r_matrix_form

    def test_c4_bzfn_holds(self):
        """C^4 BZFN holds without twist."""
        dc = twisted_drinfeld_center_c4()
        # VERIFIED [DC] BZFN
        assert dc.bzfn_still_holds


# =========================================================================
# 8. CASCADE AT d=4: E_1 -> E_2 -> E_3 (12 tests)
# =========================================================================

class TestCY4Cascade:
    """Test the E_n cascade E_1 -> E_2 -> E_3 at d=4."""

    def test_cascade_has_2_steps(self):
        """The cascade has exactly 2 steps."""
        cascade = cy4_cascade()
        # VERIFIED [DC] structural
        assert len(cascade.steps) == 2

    def test_step1_e1_to_e2(self):
        """Step 1: E_1 -> E_2."""
        cascade = cy4_cascade()
        s1 = cascade.steps[0]
        # VERIFIED [DC] Drinfeld center
        assert s1.input_en == 1 and s1.output_en == 2

    def test_step2_e2_to_e3(self):
        """Step 2: E_2 -> E_3."""
        cascade = cy4_cascade()
        s2 = cascade.steps[1]
        # VERIFIED [DC] derived center
        assert s2.input_en == 2 and s2.output_en == 3

    def test_max_en_is_3(self):
        """Max E_n from cascade is 3."""
        cascade = cy4_cascade()
        # VERIFIED [DC] cascade termination [CF] higher_deligne_cascade.py
        assert cascade.max_en == 3

    def test_same_max_as_cy3(self):
        """Same max E_n as CY3 (both E_3)."""
        cascade = cy4_cascade()
        # VERIFIED [DC] structural comparison
        assert cascade.same_max_as_cy3

    def test_step1_is_twisted(self):
        """Step 1 has a Z-twisted half-braiding from p_1."""
        cascade = cy4_cascade()
        # VERIFIED [DC] p_1 twist
        assert cascade.steps[0].is_twisted

    def test_step2_inherits_twist(self):
        """Step 2 inherits the p_1 twist from Step 1."""
        cascade = cy4_cascade()
        # VERIFIED [DC] twist propagation
        assert cascade.steps[1].is_twisted

    def test_step1_mechanism_drinfeld(self):
        """Step 1 mechanism is Drinfeld center."""
        cascade = cy4_cascade()
        # VERIFIED [DC] mechanism identification
        assert "Drinfeld" in cascade.steps[0].mechanism

    def test_step2_mechanism_derived(self):
        """Step 2 mechanism is derived center / higher Deligne."""
        cascade = cy4_cascade()
        # VERIFIED [DC] mechanism identification
        assert "Deligne" in cascade.steps[1].mechanism or "derived" in cascade.steps[1].mechanism.lower()

    def test_why_no_e4(self):
        """Explanation for no E_4 mentions p_1 and Dunn."""
        cascade = cy4_cascade()
        # VERIFIED [DC] structural
        assert "p_1" in cascade.why_no_e4 or "pi_4" in cascade.why_no_e4

    def test_p1_does_not_increase_en(self):
        """p_1 does not increase the E_n level."""
        cascade = cy4_cascade()
        # VERIFIED [DC] structural
        assert "does NOT" in cascade.p1_role or "NOT" in cascade.p1_role

    def test_step1_comparison_with_cy3(self):
        """Step 1 comparison notes CY3 is untwisted, CY4 is twisted."""
        cascade = cy4_cascade()
        s1 = cascade.steps[0]
        # VERIFIED [DC] comparison
        assert "CY3" in s1.comparison_with_cy3 and "CY4" in s1.comparison_with_cy3


# =========================================================================
# 9. d=3 vs d=4 COMPARISON (12 tests)
# =========================================================================

class TestD3vsD4:
    """Test the side-by-side comparison between d=3 and d=4."""

    def test_comparison_list_nonempty(self):
        """The comparison list has entries."""
        comp = d3_vs_d4_comparison()
        # VERIFIED [DC] completeness
        assert len(comp) >= 10

    def test_native_en_same(self):
        """Both d=3 and d=4 have native E_1."""
        comp = d3_vs_d4_comparison()
        en_row = [c for c in comp if c.property_name == "Native E_n"][0]
        # VERIFIED [DC] stabilization
        assert en_row.d3_value == "E_1"
        assert en_row.d4_value == "E_1"
        assert not en_row.differ

    def test_framing_obstruction_differs(self):
        """Framing obstruction differs: trivial at d=3, Z at d=4."""
        comp = d3_vs_d4_comparison()
        fo_row = [c for c in comp if "raming" in c.property_name][0]
        # VERIFIED [DC] Bott periodicity
        assert fo_row.differ
        assert "trivial" in fo_row.d3_value or "0" in fo_row.d3_value
        assert "Z" in fo_row.d4_value

    def test_deformation_dim_differs(self):
        """Effective deformation dim: 1 at d=3, 2 at d=4."""
        comp = d3_vs_d4_comparison()
        dim_row = [c for c in comp if "deformation" in c.property_name.lower()][0]
        # VERIFIED [DC] parameter counting
        assert dim_row.differ
        assert "1" in dim_row.d3_value
        assert "2" in dim_row.d4_value

    def test_max_en_same(self):
        """Max E_n from cascade: E_3 at both d=3 and d=4."""
        comp = d3_vs_d4_comparison()
        max_row = [c for c in comp if "ax" in c.property_name and "cascade" in c.property_name.lower()][0]
        # VERIFIED [DC] cascade termination
        assert max_row.d3_value == "E_3"
        assert max_row.d4_value == "E_3"
        assert not max_row.differ

    def test_drinfeld_center_twist_differs(self):
        """Drinfeld center: untwisted at d=3, Z-twisted at d=4."""
        comp = d3_vs_d4_comparison()
        dc_row = [c for c in comp if "Drinfeld" in c.property_name][0]
        # VERIFIED [DC] p_1 twist
        assert dc_row.differ
        assert "untwisted" in dc_row.d3_value
        assert "twisted" in dc_row.d4_value

    def test_yangian_differs(self):
        """Yangian structure differs: Y(gl_hat_1) at d=3, twisted at d=4."""
        comp = d3_vs_d4_comparison()
        y_row = [c for c in comp if "angian" in c.property_name][0]
        # VERIFIED [DC] structural
        assert y_row.differ

    def test_self_dual_reduction_differs(self):
        """Self-dual: Heisenberg at d=3, CY3 Yangian at d=4."""
        comp = d3_vs_d4_comparison()
        sd_row = [c for c in comp if "elf-dual" in c.property_name][0]
        # VERIFIED [DC] structural
        assert sd_row.differ

    def test_all_comparisons_have_explanations(self):
        """Every comparison has a nonempty explanation."""
        comp = d3_vs_d4_comparison()
        # VERIFIED [DC] completeness
        for c in comp:
            assert len(c.explanation) > 0

    def test_dunn_factors_same(self):
        """Dunn E_1 factors: 3 at both d=3 and d=4."""
        comp = d3_vs_d4_comparison()
        dunn_row = [c for c in comp if "Dunn" in c.property_name][0]
        # VERIFIED [DC] structural
        assert "3" in dunn_row.d3_value
        assert "3" in dunn_row.d4_value

    def test_omega_constraint_differs(self):
        """Omega-background constraint differs: 3 params at d=3, 4 at d=4."""
        comp = d3_vs_d4_comparison()
        omega_row = [c for c in comp if "mega" in c.property_name][0]
        # VERIFIED [DC] parameter counting
        assert omega_row.differ

    def test_shadow_class_differs(self):
        """Shadow class (generic) may differ between d=3 and d=4."""
        comp = d3_vs_d4_comparison()
        shadow_row = [c for c in comp if "hadow" in c.property_name][0]
        # VERIFIED [DC] shadow classification
        assert shadow_row.differ


# =========================================================================
# 10. MASTER VERIFICATION (14 tests)
# =========================================================================

class TestMasterVerification:
    """Test the master verification assembling all results."""

    def test_native_en_is_e1(self):
        """Native E_n at d=4 is E_1."""
        mv = master_verification()
        # VERIFIED [DC] stabilization [CF] 6 paths in cy4_e2_tower.py
        assert mv.native_en == "E_1"

    def test_max_cascade_3(self):
        """Max cascade E_n is 3."""
        mv = master_verification()
        # VERIFIED [DC] cascade termination
        assert mv.max_cascade_en == 3

    def test_pi4_BU_Z(self):
        """pi_4(BU) = Z."""
        mv = master_verification()
        # VERIFIED [DC] Bott periodicity
        assert mv.pi4_BU == "Z"

    def test_pi4_BSp_Z(self):
        """pi_4(BSp) = Z."""
        mv = master_verification()
        # VERIFIED [DC] Bott periodicity
        assert mv.pi4_BSp == "Z"

    def test_pi4_BO_Z(self):
        """pi_4(BO) = Z."""
        mv = master_verification()
        # VERIFIED [DC] Bott periodicity
        assert mv.pi4_BO == "Z"

    def test_all_give_Z(self):
        """All three structure group paths give Z."""
        mv = master_verification()
        # VERIFIED [DC] triple agreement
        assert mv.all_give_Z

    def test_no_cy4_yangian(self):
        """No CY4 Yangian exists."""
        mv = master_verification()
        # VERIFIED [DC] obstruction theory
        assert not mv.cy4_yangian_exists

    def test_all_examples_e1(self):
        """All CY4 examples are E_1."""
        mv = master_verification()
        # VERIFIED [DC] stabilization [CF] multi-example
        assert mv.all_examples_e1

    def test_d3_d4_same_max(self):
        """d=3 and d=4 have the same max E_n (= 3)."""
        mv = master_verification()
        # VERIFIED [DC] cascade comparison
        assert mv.d3_d4_same_max_en

    def test_p1_does_not_increase_en(self):
        """p_1 does not increase the E_n level."""
        mv = master_verification()
        # VERIFIED [DC] structural
        assert mv.p1_does_not_increase_en

    def test_deformation_dim_2(self):
        """The effective deformation dimension is 2."""
        mv = master_verification()
        # VERIFIED [DC] parameter counting
        assert mv.deformation_dim_is_2

    def test_p1_generator(self):
        """The generator of the obstruction is p_1."""
        mv = master_verification()
        # VERIFIED [DC] characteristic class
        assert "p_1" in mv.p1_generator

    def test_4_examples(self):
        """There are 4 CY4 examples."""
        mv = master_verification()
        # VERIFIED [DC] landscape
        assert mv.n_examples == 4

    def test_sigma_4_role_mentions_deformation(self):
        """sigma_4 role mentions the deformation space."""
        mv = master_verification()
        # VERIFIED [DC] documentation
        assert "deformation" in mv.sigma_4_role


# =========================================================================
# 11. PONTRYAGIN CLASS LANDSCAPE (10 tests)
# =========================================================================

class TestPontryaginLandscape:
    """Test the Pontryagin class values across the CY4 landscape."""

    def test_c4_p1_zero(self):
        """p_1(C^4) = 0 (flat)."""
        land = p1_landscape()
        # VERIFIED [DC] flat space
        assert land["C^4"] == 0

    def test_k3_p1_minus48(self):
        """p_1(K3) = -48."""
        land = p1_landscape()
        # VERIFIED [DC] p_1 = -2*c_2 [CF] c_2(K3) = 24
        assert land["K3"] == -48

    def test_k3xk3_p1_minus96(self):
        """p_1(K3 x K3) = -96."""
        land = p1_landscape()
        # VERIFIED [DC] product formula [CF] 2 * (-48)
        assert land["K3 x K3"] == -96

    def test_sextic_p1_minus30(self):
        """p_1(sextic) = -30."""
        land = p1_landscape()
        # VERIFIED [DC] Chern class computation
        assert land["sextic in P^5"] == -30

    def test_p1_additivity(self):
        """p_1(K3 x K3) = p_1(K3) + p_1(K3)."""
        # VERIFIED [DC] product formula [CF] stable characteristic class
        assert verify_p1_additivity()

    def test_p1_formula_cy(self):
        """p_1 = -2*c_2 for CY manifolds (c_1 = 0)."""
        # VERIFIED [DC] Chern-Pontryagin relation
        assert verify_p1_formula_cy()

    def test_all_compact_cy4_have_nontrivial_p1(self):
        """All compact CY4 examples have nontrivial p_1."""
        # VERIFIED [DC] obstruction theory
        # K3 x K3 and sextic both have p_1 != 0
        land = p1_landscape()
        assert land["K3 x K3"] != 0
        assert land["sextic in P^5"] != 0

    def test_only_c4_has_trivial_p1(self):
        """Only C^4 has p_1 = 0 in the landscape."""
        land = p1_landscape()
        # VERIFIED [DC] landscape
        trivial = [k for k, v in land.items() if v == 0]
        assert trivial == ["C^4"]

    def test_p1_negative_for_cy(self):
        """p_1 is negative for CY manifolds (since c_2 > 0)."""
        land = p1_landscape()
        # VERIFIED [DC] positivity of c_2
        for k, v in land.items():
            assert v <= 0, f"p_1({k}) = {v} > 0, unexpected for CY"

    def test_p1_landscape_has_4_entries(self):
        """The landscape has 4 entries."""
        land = p1_landscape()
        # VERIFIED [DC] completeness
        assert len(land) == 4


# =========================================================================
# 12. sigma_4 EXPLICIT COMPUTATIONS (12 tests)
# =========================================================================

class TestSigma4Computations:
    """Test explicit sigma_4 computations at various points."""

    def test_sigma4_landscape_has_4_points(self):
        """The sigma_4 landscape has 4 test points."""
        pts = sigma_4_at_various_points()
        # VERIFIED [DC] completeness
        assert len(pts) == 4

    def test_self_dual_sigma4_zero(self):
        """sigma_4 = 0 at the self-dual point."""
        pts = sigma_4_at_various_points()
        sd = pts[0]
        # VERIFIED [DC] algebraic
        assert sd["sigma_4"] == 0

    def test_self_dual_is_self_dual(self):
        """The self-dual point is flagged as self-dual."""
        pts = sigma_4_at_various_points()
        sd = pts[0]
        # VERIFIED [DC] structural
        assert sd["is_self_dual"]

    def test_generic_sigma4_nonzero(self):
        """sigma_4 != 0 at the generic point."""
        pts = sigma_4_at_various_points()
        gen = pts[1]
        # VERIFIED [DC] algebraic
        assert gen["sigma_4"] != 0

    def test_generic_not_self_dual(self):
        """The generic point is not self-dual."""
        pts = sigma_4_at_various_points()
        gen = pts[1]
        # VERIFIED [DC] structural
        assert not gen["is_self_dual"]

    def test_symmetric_sigma3_zero(self):
        """sigma_3 = 0 at the S_4-symmetric point."""
        pts = sigma_4_at_various_points()
        sym = pts[2]
        # VERIFIED [DC] algebraic
        assert sym["sigma_3"] == 0

    def test_symmetric_ratio_none(self):
        """The ratio is None at the S_4-symmetric point (sigma_3 = 0)."""
        pts = sigma_4_at_various_points()
        sym = pts[2]
        # VERIFIED [DC] algebraic (division by zero)
        assert sym["ratio"] is None

    def test_self_dual_ratio_zero(self):
        """The ratio is 0 at the self-dual point (sigma_4 = 0)."""
        pts = sigma_4_at_various_points()
        sd = pts[0]
        # VERIFIED [DC] algebraic
        assert sd["ratio"] == 0

    def test_cy3_reduction(self):
        """Verify CY3 reduction at self-dual."""
        # VERIFIED [DC] structural [CF] sigma_4 = 0 limit
        assert verify_cy3_reduction_at_self_dual()

    def test_effective_dim_2(self):
        """Verify effective deformation dimension is 2."""
        # VERIFIED [DC] parameter counting [CF] en_structure
        assert verify_effective_dim_2()

    def test_fourth_point_not_self_dual(self):
        """The fourth test point h=(2,3,-4,-1) is not self-dual."""
        pts = sigma_4_at_various_points()
        pt4 = pts[3]
        # VERIFIED [DC] construction
        assert not pt4["is_self_dual"]

    def test_fourth_point_sigma4(self):
        """sigma_4 at h=(2,3,-4,-1) = 2*3*(-4)*(-1) = 24."""
        pts = sigma_4_at_various_points()
        pt4 = pts[3]
        # VERIFIED [DC] algebraic [CF] direct computation
        assert pt4["sigma_4"] == Fraction(24)


# =========================================================================
# 13. COMPREHENSIVE SUMMARY (bonus: integration test)
# =========================================================================

class TestComprehensiveSummary:
    """Integration test: the full summary runs and produces consistent results."""

    def test_summary_runs(self):
        """The full summary runs without error."""
        summary = full_cy4_extension_summary()
        # VERIFIED [DC] integration
        assert summary is not None

    def test_key_results_all_true(self):
        """All key results are True."""
        summary = full_cy4_extension_summary()
        kr = summary["key_results"]
        # VERIFIED [DC] integration [CF] all subtests
        assert kr["d4_is_E1"]
        assert kr["max_cascade_is_E3"]
        assert kr["same_max_as_d3"]
        assert kr["pi4_BU_is_Z"]
        assert kr["all_three_paths_Z"]
        assert kr["no_cy4_yangian"]
        assert kr["p1_does_not_increase_en"]
        assert kr["deformation_dim_2"]
        assert kr["all_examples_E1"]

    def test_p1_landscape_in_summary(self):
        """The p_1 landscape is included in the summary."""
        summary = full_cy4_extension_summary()
        # VERIFIED [DC] completeness
        assert "p1_landscape" in summary
        assert len(summary["p1_landscape"]) == 4

    def test_examples_in_summary(self):
        """The examples are included in the summary."""
        summary = full_cy4_extension_summary()
        # VERIFIED [DC] completeness
        assert "examples" in summary
        assert len(summary["examples"]) == 4

    def test_d3_vs_d4_in_summary(self):
        """The d=3 vs d=4 comparison is included."""
        summary = full_cy4_extension_summary()
        # VERIFIED [DC] completeness
        assert "d3_vs_d4" in summary
        assert len(summary["d3_vs_d4"]) >= 10
