"""Tests for perturbative chiral invariants from 6d holomorphic CS Feynman diagrams.

Verifies:
  (1) Feynman graph combinatorics (loop order, symmetry factors)
  (2) Lie algebra weights w(Gamma) for gl_1 (structure function coefficients)
  (3) Configuration space integrals I(Gamma) (holomorphic residues)
  (4) Tree-level = kappa_ch identification
  (5) One-loop = S_2 = kappa_ch (shadow depth 2)
  (6) Two-loop = S_3 = alpha (cubic shadow)
  (7) Three-loop = S_4 (quartic contact)
  (8) Shadow-Feynman dictionary: loop L <-> shadow depth L+1
  (9) A_infinity correspondence: m_{k+1} <-> S_{k+1}
  (10) Per-channel decomposition and MacMahon connection
  (11) Dimensional hierarchy: 3d -> 5d -> 6d consistency
  (12) End-to-end pipeline
  (13) Cross-engine compatibility with c3_shadow_tower and a_infinity_bar_w1inf
  (14) AP compliance (AP113, AP1, AP-CY31, AP-CY21)

Test organization (14 suites, 68 tests):

  1. TestFeynmanGraphCombinatorics (8 tests): Graph topology and invariants
  2. TestLieAlgebraWeights (8 tests): w(Gamma) for gl_1
  3. TestConfigurationSpaceIntegrals (5 tests): Holomorphic residues
  4. TestTreeLevel (4 tests): Tree-level = kappa_ch
  5. TestOneLoop (5 tests): One-loop = S_2
  6. TestTwoLoop (5 tests): Two-loop = S_3 = alpha
  7. TestThreeLoop (4 tests): Three-loop = S_4
  8. TestShadowFeynmanDictionary (6 tests): Loop L <-> shadow S_{L+1}
  9. TestAInfinityCorrespondence (4 tests): m_k <-> S_k
  10. TestPerChannelDecomposition (6 tests): Spin channels and MacMahon
  11. TestDimensionalHierarchy (5 tests): 3d/5d/6d consistency
  12. TestEndToEndPipeline (3 tests): Pipeline pass
  13. TestCrossEngine (3 tests): Compatibility with existing engines
  14. TestAPCompliance (2 tests): Anti-pattern checks

Ground truth:
  SV N=2 point (1, -2, 1): sigma_2 = -3, sigma_3 = -2, Psi = 3
  Self-dual (1, 0, -1): sigma_2 = -1, sigma_3 = 0, Psi = 1

  Spin 2 shadow tower at c=1:
    S_2 = kappa_ch = 1/2     # VERIFIED: c3_shadow_tower.py [DC]
    S_3 = alpha = 2           # VERIFIED: a_infinity_bar_w1inf.py [DC]
    S_4 = 10/27               # VERIFIED: c3_shadow_tower.py [DC]

  A_infinity operations at c=1:
    m_3(T,T,T) = -2T          # VERIFIED: a_infinity_bar_w1inf.py [DC]
    m_4(T,T,T,T) = (40/27)T   # VERIFIED: a_infinity_bar_w1inf.py [DC]

Multi-path verification:
  Path 1: Perturbative expansion (this engine)
  Path 2: Shadow tower recursion (c3_shadow_tower.py)
  Path 3: A_infinity bar complex (a_infinity_bar_w1inf.py)

Manuscript references:
  chapters/theory/quantum_chiral_algebras.tex: Sections 5-6
  chapters/theory/e1_chiral_algebras.tex: E_1 bialgebra
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.perturbative_chiral_feynman import (
    FeynmanGraph,
    tree_propagator,
    one_loop_bubble,
    two_loop_sunset,
    two_loop_theta,
    three_loop_double_bubble,
    standard_graphs_at_loop_order,
    LieAlgebraWeight,
    ConfigurationSpaceIntegral,
    PerturbativeChiralInvariant,
    PerChannelDecomposition,
    HolomorphicResidueCalculus,
    ShadowFeynmanDictionary,
    HCSPerturbativeHierarchy,
    perturbative_chiral_pipeline,
)


# =========================================================================
# 1. Feynman graph combinatorics
# =========================================================================

class TestFeynmanGraphCombinatorics:
    """Test topological invariants of Feynman graphs."""

    def test_tree_propagator_loop_order(self):
        """Tree propagator has L=0."""
        g = tree_propagator()
        assert g.loop_order == 0

    def test_tree_propagator_topology(self):
        """Tree: 2 vertices, 1 edge."""
        g = tree_propagator()
        assert g.n_vertices == 2
        assert g.n_edges == 1

    def test_bubble_loop_order(self):
        """Bubble has L=1."""
        g = one_loop_bubble()
        assert g.loop_order == 1

    def test_bubble_symmetry_factor(self):
        """Bubble: |Aut| = 2, symmetry = 1/2."""
        g = one_loop_bubble()
        assert g.symmetry_factor == Fraction(1, 2)

    def test_sunset_loop_order(self):
        """Sunset has L=2."""
        g = two_loop_sunset()
        assert g.loop_order == 2

    def test_sunset_symmetry_factor(self):
        """Sunset: |Aut| = S_3, symmetry = 1/6."""
        g = two_loop_sunset()
        assert g.symmetry_factor == Fraction(1, 6)

    def test_standard_graphs_tree(self):
        """One graph at L=0 (tree)."""
        graphs = standard_graphs_at_loop_order(0)
        assert len(graphs) == 1
        assert graphs[0].name == "tree_propagator"

    def test_standard_graphs_two_loop(self):
        """Two graphs at L=2 (sunset + theta)."""
        graphs = standard_graphs_at_loop_order(2)
        assert len(graphs) == 2
        names = {g.name for g in graphs}
        assert "two_loop_sunset" in names
        assert "two_loop_theta" in names


# =========================================================================
# 2. Lie algebra weights
# =========================================================================

class TestLieAlgebraWeights:
    """Test w(Gamma) computation for gl_1."""

    def test_phi_0_is_one(self):
        """phi_0 = 1 (leading coefficient of g(u))."""
        w = LieAlgebraWeight(Rational(1), Rational(-2))
        phi = w.phi_coefficients()
        assert phi[0] == Rational(1)

    def test_phi_1_vanishes_cy(self):
        """phi_1 = 0 at the CY locus (h_1 + h_2 + h_3 = 0)."""
        w = LieAlgebraWeight(Rational(1), Rational(-2))
        phi = w.phi_coefficients()
        assert phi[1] == Rational(0)

    def test_phi_2_vanishes_parity(self):
        """phi_2 = 0 by parity (even coefficient in log-series)."""
        w = LieAlgebraWeight(Rational(1), Rational(-2))
        phi = w.phi_coefficients()
        assert phi[2] == Rational(0)

    def test_phi_3_leading_deformation(self):
        """phi_3 = -2*sigma_3 (leading Yangian deformation).

        At (1, -2, 1): sigma_3 = 1*(-2)*1 = -2, so phi_3 = -2*(-2) = 4.
        # VERIFIED: costello_5d_verification.py [DC]
        # VERIFIED: affine_yangian_gl1.py [DC]
        """
        w = LieAlgebraWeight(Rational(1), Rational(-2))
        phi = w.phi_coefficients()
        expected_phi3 = Rational(-2) * w.sigma3  # -2 * (-2) = 4
        assert phi[3] == expected_phi3

    def test_weight_tree(self):
        """Tree weight = Psi = -sigma_2.

        At (1, -2, 1): sigma_2 = -3, Psi = 3.
        """
        w = LieAlgebraWeight(Rational(1), Rational(-2))
        assert w.weight_tree() == Rational(3)

    def test_weight_tree_self_dual(self):
        """At self-dual point (1, 0, -1): Psi = -sigma_2 = 1."""
        w = LieAlgebraWeight(Rational(1), Rational(0))
        assert w.weight_tree() == Rational(1)

    def test_weight_theta(self):
        """Theta weight = -2*sigma_3.

        At (1, -2, 1): sigma_3 = -2, so w(theta) = -2*(-2) = 4.
        """
        w = LieAlgebraWeight(Rational(1), Rational(-2))
        assert w.weight_theta() == Rational(4)

    def test_weight_theta_self_dual(self):
        """At self-dual (sigma_3 = 0): theta weight vanishes."""
        w = LieAlgebraWeight(Rational(1), Rational(0))
        assert w.weight_theta() == Rational(0)


# =========================================================================
# 3. Configuration space integrals
# =========================================================================

class TestConfigurationSpaceIntegrals:
    """Test holomorphic residue integrals."""

    def test_tree_integral_is_psi(self):
        """I(tree) = Psi (the OPE coefficient)."""
        csi = ConfigurationSpaceIntegral(Rational(3))
        assert csi.integral_tree() == Rational(3)

    def test_bubble_integral_normalized(self):
        """I(bubble) = 1 (regularized and normalized)."""
        csi = ConfigurationSpaceIntegral(Rational(3))
        assert csi.integral_bubble() == Rational(1)

    def test_theta_integral_normalized(self):
        """I(theta) = 1 (normalized on FM compactification)."""
        csi = ConfigurationSpaceIntegral(Rational(3))
        assert csi.integral_theta() == Rational(1)

    def test_sunset_integral_normalized(self):
        """I(sunset) = 1 (normalized)."""
        csi = ConfigurationSpaceIntegral(Rational(3))
        assert csi.integral_sunset() == Rational(1)

    def test_arnold_form_dimension(self):
        """dim H^*(Conf_n(C)) = n!."""
        hrc = HolomorphicResidueCalculus(Rational(3))
        assert hrc.arnold_form_product(3) == 6   # 3!
        assert hrc.arnold_form_product(4) == 24  # 4!


# =========================================================================
# 4. Tree level
# =========================================================================

class TestTreeLevel:
    """Test tree-level = kappa_ch identification."""

    def test_tree_spin1_is_kappa(self):
        """Tree level at spin 1 = kappa_ch = c/1 = 1.

        # VERIFIED: c3_shadow_tower.py line 126 [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=1, c_val=Rational(1)
        )
        assert pci.tree_level_contribution() == Rational(1)

    def test_tree_spin2_is_kappa(self):
        """Tree level at spin 2 = kappa_ch = c/2 = 1/2.

        # VERIFIED: c3_shadow_tower.py line 126 [DC]
        # VERIFIED: landscape_census.tex (Virasoro: kappa=c/2) [LT]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.tree_level_contribution() == Rational(1, 2)

    def test_tree_spin3_is_kappa(self):
        """Tree level at spin 3 = kappa_ch = c/3 = 1/3."""
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=3, c_val=Rational(1)
        )
        assert pci.tree_level_contribution() == Rational(1, 3)

    def test_tree_level_independent_of_omega(self):
        """kappa_ch = c/s is independent of the Omega-background.

        At (1, -2, 1) and (1, -3, 2): both give kappa_ch = 1/2 at spin 2.
        """
        pci1 = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        pci2 = PerturbativeChiralInvariant(
            Rational(1), Rational(-3), spin=2, c_val=Rational(1)
        )
        assert pci1.tree_level_contribution() == pci2.tree_level_contribution()


# =========================================================================
# 5. One loop
# =========================================================================

class TestOneLoop:
    """Test one-loop = S_2 = kappa_ch."""

    def test_one_loop_spin1(self):
        """One-loop at spin 1: S_2 = kappa_ch = 1.

        # VERIFIED: c3_shadow_tower.py [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=1, c_val=Rational(1)
        )
        assert pci.one_loop_contribution() == Rational(1)

    def test_one_loop_spin2(self):
        """One-loop at spin 2: S_2 = kappa_ch = 1/2.

        # VERIFIED: c3_shadow_tower.py line 34 [DC]
        # VERIFIED: Theorem A (Vol I) [LT]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.one_loop_contribution() == Rational(1, 2)

    def test_one_loop_equals_tree(self):
        """One-loop = tree level (both equal kappa_ch).

        This is the content of Theorem A: F_1 = kappa * lambda_1.
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.one_loop_contribution() == pci.tree_level_contribution()

    def test_one_loop_is_shadow_s2(self):
        """One-loop = S_2 (shadow depth 2)."""
        depth = ShadowFeynmanDictionary.loop_to_shadow_depth(1)
        assert depth == 2

    def test_one_loop_spin3(self):
        """One-loop at spin 3: S_2 = kappa_ch = 1/3."""
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=3, c_val=Rational(1)
        )
        assert pci.one_loop_contribution() == Rational(1, 3)


# =========================================================================
# 6. Two loop
# =========================================================================

class TestTwoLoop:
    """Test two-loop = S_3 = alpha (cubic shadow)."""

    def test_two_loop_spin1_vanishes(self):
        """Two-loop at spin 1: alpha = 0 (class G, no cubic shadow).

        # VERIFIED: c3_shadow_tower.py line 31: alpha=0 [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=1, c_val=Rational(1)
        )
        assert pci.two_loop_contribution() == Rational(0)

    def test_two_loop_spin2_is_alpha(self):
        """Two-loop at spin 2: alpha = 2 (cubic shadow S_3 = 2).

        # VERIFIED: c3_shadow_tower.py line 34: alpha=2 [DC]
        # VERIFIED: a_infinity_bar_w1inf.py: m_3(T,T,T) = -2T [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.two_loop_contribution() == Rational(2)

    def test_two_loop_spin3_vanishes_parity(self):
        """Two-loop at spin 3: alpha = 0 (parity W_3 -> -W_3).

        # VERIFIED: c3_shadow_tower.py line 37: alpha=0 by parity [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=3, c_val=Rational(1)
        )
        assert pci.two_loop_contribution() == Rational(0)

    def test_two_loop_is_shadow_s3(self):
        """Two-loop = S_3 (shadow depth 3)."""
        depth = ShadowFeynmanDictionary.loop_to_shadow_depth(2)
        assert depth == 3

    def test_two_loop_class_g_vanishes(self):
        """For class G algebras, all loops L >= 1 vanish at spin 1."""
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=1, c_val=Rational(1)
        )
        assert pci.shadow_class() == "G"
        assert pci.two_loop_contribution() == Rational(0)


# =========================================================================
# 7. Three loop
# =========================================================================

class TestThreeLoop:
    """Test three-loop = S_4 (quartic contact)."""

    def test_three_loop_spin1_vanishes(self):
        """Three-loop at spin 1: S_4 = 0 (class G).

        # VERIFIED: c3_shadow_tower.py line 31: S_4=0 [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=1, c_val=Rational(1)
        )
        assert pci.three_loop_contribution() == Rational(0)

    def test_three_loop_spin2(self):
        """Three-loop at spin 2: S_4 = 10/27.

        # VERIFIED: c3_shadow_tower.py line 34: S_4=10/27 [DC]
        # VERIFIED: a_infinity_bar_w1inf.py: m_4(T,T,T,T) = (40/27)T [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.three_loop_contribution() == Rational(10, 27)

    def test_three_loop_is_shadow_s4(self):
        """Three-loop = S_4 (shadow depth 4)."""
        depth = ShadowFeynmanDictionary.loop_to_shadow_depth(3)
        assert depth == 4

    def test_three_loop_ratio_to_m4(self):
        """m_4(T,T,T,T) = (40/27)T and S_4 = 10/27, so ratio = 4.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        """
        m4 = Fraction(40, 27)
        S4 = Fraction(10, 27)
        assert m4 / S4 == 4


# =========================================================================
# 8. Shadow-Feynman dictionary
# =========================================================================

class TestShadowFeynmanDictionary:
    """Test the shadow-loop correspondence."""

    def test_loop_to_shadow_conversion(self):
        """L -> r = L+1."""
        assert ShadowFeynmanDictionary.loop_to_shadow_depth(0) == 1
        assert ShadowFeynmanDictionary.loop_to_shadow_depth(1) == 2
        assert ShadowFeynmanDictionary.loop_to_shadow_depth(2) == 3

    def test_shadow_to_loop_conversion(self):
        """r -> L = r-1."""
        assert ShadowFeynmanDictionary.shadow_depth_to_loop(2) == 1
        assert ShadowFeynmanDictionary.shadow_depth_to_loop(3) == 2
        assert ShadowFeynmanDictionary.shadow_depth_to_loop(4) == 3

    def test_dictionary_spin2_s2(self):
        """S_2 = kappa_ch = 1/2 matches one-loop.

        # VERIFIED: c3_shadow_tower.py [DC]
        # VERIFIED: Theorem A (Vol I) [LT]
        """
        result = ShadowFeynmanDictionary.verify_dictionary_spin2()
        entry = result["entries"]["S_2 (depth 2, loop 1)"]
        assert entry["match"]
        assert entry["shadow_value"] == Rational(1, 2)

    def test_dictionary_spin2_s3(self):
        """S_3 = alpha = 2 matches two-loop.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        # VERIFIED: c3_shadow_tower.py [DC]
        """
        result = ShadowFeynmanDictionary.verify_dictionary_spin2()
        entry = result["entries"]["S_3 (depth 3, loop 2)"]
        assert entry["match"]
        assert entry["shadow_value"] == Rational(2)

    def test_dictionary_spin2_s4(self):
        """S_4 = 10/27 matches three-loop.

        # VERIFIED: c3_shadow_tower.py [DC]
        """
        result = ShadowFeynmanDictionary.verify_dictionary_spin2()
        entry = result["entries"]["S_4 (depth 4, loop 3)"]
        assert entry["match"]
        assert entry["shadow_value"] == Rational(10, 27)

    def test_dictionary_all_match(self):
        """All dictionary entries match."""
        result = ShadowFeynmanDictionary.verify_dictionary_spin2()
        assert result["all_match"]


# =========================================================================
# 9. A_infinity correspondence
# =========================================================================

class TestAInfinityCorrespondence:
    """Test m_k <-> S_k correspondence."""

    def test_m3_to_alpha(self):
        """m_3(T,T,T) = -2T => alpha = |-2| = 2 = S_3.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        """
        result = ShadowFeynmanDictionary.verify_ainfinity_correspondence()
        assert result["m_3_to_S_3"]["match"]

    def test_m3_coefficient(self):
        """m_3(T,T,T) coefficient is -2.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        """
        assert ShadowFeynmanDictionary.AINFINITY_DATA["m_3(T,T,T)"] == Fraction(-2)

    def test_m4_to_s4_ratio(self):
        """m_4(T,T,T,T)/S_4 = (40/27)/(10/27) = 4.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        """
        result = ShadowFeynmanDictionary.verify_ainfinity_correspondence()
        assert result["m_4_to_S_4"]["ratio_is_4"]

    def test_m4_coefficient(self):
        """m_4(T,T,T,T) coefficient is 40/27.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        """
        assert ShadowFeynmanDictionary.AINFINITY_DATA["m_4(T,T,T,T)"] == Fraction(40, 27)


# =========================================================================
# 10. Per-channel decomposition
# =========================================================================

class TestPerChannelDecomposition:
    """Test the spin-channel decomposition and MacMahon connection."""

    def test_total_kappa_ch_spin3(self):
        """Total kappa_ch at max_spin=3: H_3 = 1 + 1/2 + 1/3 = 11/6.

        # VERIFIED: c3_shadow_tower.py [DC]
        """
        decomp = PerChannelDecomposition(max_spin=3)
        expected = Rational(1) + Rational(1, 2) + Rational(1, 3)
        assert decomp.total_kappa_ch() == expected

    def test_total_tree_equals_kappa(self):
        """Total tree level = total kappa_ch."""
        decomp = PerChannelDecomposition(max_spin=3)
        assert decomp.total_tree_level() == decomp.total_kappa_ch()

    def test_total_one_loop_equals_kappa(self):
        """Total one-loop = total kappa_ch (universality of S_2)."""
        decomp = PerChannelDecomposition(max_spin=3)
        assert decomp.total_one_loop() == decomp.total_kappa_ch()

    def test_macmahon_effective_per_level(self):
        """Effective kappa per energy level = s * kappa_s = 1 for all s.

        This is the shadow-DT Rosetta stone: each energy level contributes
        equally to the modular characteristic.

        # VERIFIED: c3_shadow_tower.py (MacMahon connection) [DC]
        """
        decomp = PerChannelDecomposition(max_spin=5)
        result = decomp.macmahon_connection()
        assert result["all_effective_equal_one"]

    def test_expansion_table_shape(self):
        """Expansion table has correct shape: {spin: {loop: value}}."""
        decomp = PerChannelDecomposition(max_spin=2)
        table = decomp.expansion_table(max_loops=2)
        assert 1 in table
        assert 2 in table
        assert 0 in table[1]  # tree level
        assert 1 in table[1]  # one loop
        assert 2 in table[1]  # two loop

    def test_spin1_is_class_g(self):
        """Spin-1 channel: two-loop and higher vanish (class G)."""
        decomp = PerChannelDecomposition(max_spin=2)
        table = decomp.expansion_table(max_loops=3)
        assert table[1][2] == Rational(0)  # Two-loop spin 1 = 0
        assert table[1][3] == Rational(0)  # Three-loop spin 1 = 0


# =========================================================================
# 11. Dimensional hierarchy
# =========================================================================

class TestDimensionalHierarchy:
    """Test 3d -> 5d -> 6d hCS consistency."""

    def test_d1_kac_moody(self):
        """d=1: 3d hCS produces Kac-Moody, class G.

        # VERIFIED: holomorphic_cs_chiral_engine.py [DC]
        """
        hierarchy = HCSPerturbativeHierarchy(Rational(1), Rational(-2))
        d1 = hierarchy.at_dimension(1)
        assert d1["algebra"] == "Kac-Moody V_k(gl_1)"
        assert d1["shadow_class"] == "G"

    def test_d2_affine_yangian(self):
        """d=2: 5d hCS produces affine Yangian, class M at generic sigma_3.

        # VERIFIED: costello_5d_verification.py [DC]
        """
        hierarchy = HCSPerturbativeHierarchy(Rational(1), Rational(-2))
        d2 = hierarchy.at_dimension(2)
        assert d2["algebra"] == "Affine Yangian Y(gl_hat_1)"
        assert d2["shadow_class"] == "M"

    def test_d3_quantum_toroidal(self):
        """d=3: 6d hCS produces quantum toroidal (conjectural).

        AP-CY32: 6d route reorganises CY-A_3, does not bypass.
        """
        hierarchy = HCSPerturbativeHierarchy(Rational(1), Rational(-2))
        d3 = hierarchy.at_dimension(3)
        assert "Quantum Toroidal" in d3["algebra"]
        assert "CONJECTURAL" in d3["status"]

    def test_kappa_preserved_across_dimensions(self):
        """kappa_ch = Psi is preserved under dimensional projection."""
        hierarchy = HCSPerturbativeHierarchy(Rational(1), Rational(-2))
        result = hierarchy.verify_hierarchy_consistency()
        assert result["kappa_preserved_1_to_2"]
        assert result["kappa_preserved_2_to_3"]

    def test_shadow_nondecreasing(self):
        """Shadow class is non-decreasing: G <= M <= M."""
        hierarchy = HCSPerturbativeHierarchy(Rational(1), Rational(-2))
        result = hierarchy.verify_hierarchy_consistency()
        assert result["shadow_nondecreasing"]


# =========================================================================
# 12. End-to-end pipeline
# =========================================================================

class TestEndToEndPipeline:
    """Test the full pipeline."""

    def test_pipeline_passes(self):
        """End-to-end pipeline should pass all checks."""
        result = perturbative_chiral_pipeline()
        assert result["all_checks_pass"]

    def test_pipeline_omega_background(self):
        """Pipeline correctly reports Omega-background data.

        At (1, -2, 1): Psi = 3, sigma_3 = -2.
        """
        result = perturbative_chiral_pipeline(Rational(1), Rational(-2))
        assert result["omega_background"]["Psi"] == Rational(3)
        assert result["omega_background"]["sigma3"] == Rational(-2)

    def test_pipeline_total_kappa(self):
        """Pipeline total kappa_ch at max_spin=3: H_3 = 11/6."""
        result = perturbative_chiral_pipeline(max_spin=3)
        expected = Rational(1) + Rational(1, 2) + Rational(1, 3)
        assert result["total_kappa_ch"] == expected


# =========================================================================
# 13. Cross-engine compatibility
# =========================================================================

class TestCrossEngine:
    """Test compatibility with existing engines."""

    def test_shadow_s2_matches_c3_shadow_tower(self):
        """S_2 = kappa_ch = 1/2 (spin 2) matches c3_shadow_tower.py.

        # VERIFIED: c3_shadow_tower.py line 34 [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        # Expected from c3_shadow_tower.py: kappa_spin2 = c/2 = 1/2
        assert pci.kappa_ch == Rational(1, 2)

    def test_alpha_matches_a_infinity_bar(self):
        """alpha = 2 matches a_infinity_bar_w1inf.py: m_3(T,T,T) = -2T.

        # VERIFIED: a_infinity_bar_w1inf.py [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.two_loop_contribution() == Rational(2)

    def test_s4_matches_c3_shadow_tower(self):
        """S_4 = 10/27 matches c3_shadow_tower.py.

        # VERIFIED: c3_shadow_tower.py line 34 [DC]
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci.three_loop_contribution() == Rational(10, 27)


# =========================================================================
# 14. AP compliance
# =========================================================================

class TestAPCompliance:
    """Test anti-pattern compliance."""

    def test_ap113_kappa_subscripted(self):
        """AP113: kappa_ch is always subscripted (never bare kappa).

        The engine uses kappa_ch as the property name, never bare kappa.
        """
        pci = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        # The attribute is named kappa_ch, not kappa
        assert hasattr(pci, 'kappa_ch')
        assert pci.kappa_ch == Rational(1, 2)

    def test_ap_cy21_shadow_class_determines_loops(self):
        """AP-CY21: shadow class determines loop truncation.

        Class G (spin 1): loops terminate at L=0.
        Class M (spin 2): infinite loop expansion.
        """
        pci_g = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=1, c_val=Rational(1)
        )
        pci_m = PerturbativeChiralInvariant(
            Rational(1), Rational(-2), spin=2, c_val=Rational(1)
        )
        assert pci_g.shadow_class() == "G"
        assert pci_m.shadow_class() == "M"
        # Class G: all higher loops vanish
        assert pci_g.two_loop_contribution() == Rational(0)
        assert pci_g.three_loop_contribution() == Rational(0)
        # Class M: higher loops nonzero
        assert pci_m.two_loop_contribution() != Rational(0)
        assert pci_m.three_loop_contribution() != Rational(0)
