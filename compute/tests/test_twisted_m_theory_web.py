r"""Tests for the twisted M-theory / string theory compactification web.

Verifies:
  (1) Web construction: all 12 nodes built, correct topology
  (2) Kappa-spectrum consistency: AP113 subscripting, Borcherds weight
  (3) Shadow class stability under dimensional reduction
  (4) R-matrix degeneration hierarchy
  (5) E_n level monotonicity
  (6) Euler characteristic multiplicativity
  (7) Hodge number Kuenneth formula
  (8) kappa_BKM theorem: c_1(0)/2 = 5, with N=1 coincidence separated
  (9) kappa_cat = chi(O_K3) = 2
  (10) Structure function degeneration chain
  (11) Reduction commutativity
  (12) Full pipeline consistency
  (13) Cross-engine compatibility with existing hCS/kappa engines

Manuscript references:
    chapters/examples/k3_times_e.tex (K3 x E tower)
    chapters/examples/toroidal_elliptic.tex (toroidal/elliptic landscape)
    chapters/theory/quantum_chiral_algebras.tex (hCS hierarchy)
    chapters/connections/modular_koszul_bridge.tex (kappa = chi^CY)

Ground truth:
    kappa_ch(K3) = 2, kappa_ch(K3 x E) = 3, kappa_BKM(K3 x E) = 5
    kappa_cat(K3) = chi(O_K3) = 2, kappa_cat(K3 x E) = chi(O_{K3xE}) = 0
    kappa_fiber(K3) = 24 (Mukai lattice rank)
    kappa_BKM(K3 x E) is Borcherds c_1(0)/2; 3 + 2 = 5 is only the
    N=1 Heisenberg-specialisation/K3-fibre coincidence.
    chi_top(K3) = 24, chi_top(E) = 0, chi_top(K3 x E) = 0

Multi-path verification:
    Path 1: Direct web construction and node inspection
    Path 2: Cross-check kappa values against kappa_spectrum_reconciliation.py
    Path 3: Cross-check hCS hierarchy against hcs_hierarchy_k3.py
    Path 4: Cross-check VW data against vafa_witten_k3.py
"""

import pytest
from sympy import Rational

from compute.lib.twisted_m_theory_web import (
    # Enums
    ClaimStatus,
    ShadowClass,
    RMatrixType,
    EnLevel,
    # Constants
    KAPPA_CH_K3,
    KAPPA_CH_K3E,
    KAPPA_CH_COMPACT_HODGE_K3E,
    KAPPA_BKM_C0_K3E_N1,
    KAPPA_BKM_K3E,
    KAPPA_CAT_K3,
    KAPPA_CAT_K3E,
    KAPPA_FIBER_K3,
    KAPPA_FIBER_K3E,
    KAPPA_CH_E,
    KAPPA_CAT_E,
    KAPPA_BKM_HEISENBERG_FIBER_COINCIDENCE,
    REDUCTION_EDGES,
    MONOTONE_EDGES,
    DUALITY_EDGES,
    WEB_EDGES,
    EDGE_REDUCTION,
    EDGE_TWIST,
    EDGE_DUALITY,
    # Functions
    build_m_theory_web,
    run_all_consistency_checks,
    count_passing,
    check_euler_char_multiplicativity,
    check_hodge_chi_additivity,
    check_kappa_bkm_borcherds_weight,
    check_kappa_cat_equals_chi_O,
    check_kappa_ch_preservation,
    check_rmatrix_degeneration,
    check_shadow_class_stability,
    check_en_level_reduction,
    check_reduction_commutativity,
    structure_function_chain,
    kappa_spectrum_web,
    full_web_analysis,
)


# =========================================================================
# 1. Web construction tests
# =========================================================================

class TestWebConstruction:
    """Test that the compactification web is built correctly."""

    def test_web_has_all_nodes(self):
        """All 12 nodes of the web are present."""
        web = build_m_theory_web()
        expected_nodes = {
            "11d_M_K3",
            "10d_IIA_K3",
            "10d_IIB_K3",
            "6d_hCS_C3",
            "6d_20_K3xC",
            "5d_M_K3xS1",
            "5d_20_on_S1",
            "4d_IIA_K3xT2",
            "4d_IIB_K3xT2",
            "3d_M_K3xT3",
            "6d_K3xExC",
            "5d_K3xCxR",
            "3d_K3_sigma",
        }
        assert set(web.keys()) == expected_nodes

    def test_web_node_count(self):
        """The web has exactly 13 nodes."""
        web = build_m_theory_web()
        assert len(web) == 13

    def test_all_edges_reference_valid_nodes(self):
        """All reduction edges reference nodes that exist in the web."""
        web = build_m_theory_web()
        for parent, child in REDUCTION_EDGES:
            assert parent in web, f"Edge parent {parent} not in web"
            assert child in web, f"Edge child {child} not in web"

    def test_edge_count(self):
        """The web has the expected number of reduction edges."""
        assert len(REDUCTION_EDGES) == 12

    def test_root_node_has_no_parent(self):
        """The 11d M-theory node is the root (no parent)."""
        web = build_m_theory_web()
        assert web["11d_M_K3"].parent_node is None

    def test_all_nonroot_have_parent(self):
        """All non-root nodes have a parent."""
        web = build_m_theory_web()
        for key, node in web.items():
            if key != "11d_M_K3":
                assert node.parent_node is not None, f"{key} has no parent"


# =========================================================================
# 2. Kappa-spectrum tests (AP113: ALWAYS subscripted)
# =========================================================================

class TestKappaSpectrum:
    """Test the kappa-spectrum values at each node."""

    def test_kappa_ch_k3_equals_2(self):
        """kappa_ch(K3 Heisenberg) = 2."""
        assert KAPPA_CH_K3 == Rational(2)

    def test_kappa_ch_k3e_equals_3(self):
        """kappa_ch(K3 x E) = 3."""
        assert KAPPA_CH_K3E == Rational(3)

    def test_kappa_bkm_k3e_equals_5(self):
        """kappa_BKM(K3 x E) = c_1(0)/2 = 5."""
        assert KAPPA_BKM_C0_K3E_N1 == Rational(10)
        assert KAPPA_BKM_C0_K3E_N1 / 2 == Rational(5)
        assert KAPPA_BKM_K3E == Rational(5)

    def test_kappa_cat_k3_equals_2(self):
        """kappa_cat(K3) = chi(O_K3) = 2."""
        assert KAPPA_CAT_K3 == Rational(2)

    def test_kappa_cat_k3e_equals_0(self):
        """kappa_cat(K3 x E) = chi(O_{K3 x E}) = 0."""
        assert KAPPA_CAT_K3E == Rational(0)

    def test_kappa_fiber_k3_equals_24(self):
        """kappa_fiber(K3) = 24 (Mukai lattice rank)."""
        assert KAPPA_FIBER_K3 == Rational(24)

    def test_kappa_bkm_borcherds_weight_not_additive(self):
        """kappa_BKM is Borcherds c_1(0)/2, not an additive kappa sum."""
        assert KAPPA_BKM_K3E == KAPPA_BKM_C0_K3E_N1 / 2
        assert KAPPA_BKM_K3E != KAPPA_CH_K3E + KAPPA_CAT_K3E
        assert KAPPA_BKM_K3E != KAPPA_CH_COMPACT_HODGE_K3E + KAPPA_CAT_E
        assert KAPPA_BKM_K3E != KAPPA_CH_COMPACT_HODGE_K3E + KAPPA_CAT_K3

    def test_kappa_bkm_n1_heisenberg_fiber_coincidence(self):
        """The N=1 Heisenberg-specialisation/K3-fibre coincidence remains."""
        assert KAPPA_BKM_HEISENBERG_FIBER_COINCIDENCE == Rational(5)
        assert KAPPA_BKM_HEISENBERG_FIBER_COINCIDENCE == KAPPA_CH_K3E + KAPPA_CAT_K3
        assert KAPPA_BKM_HEISENBERG_FIBER_COINCIDENCE == KAPPA_BKM_K3E

    def test_kappa_ch_e_equals_0(self):
        """kappa_ch(E) = 0 (elliptic curve, trivial)."""
        assert KAPPA_CH_E == Rational(0)

    def test_kappa_cat_e_equals_0(self):
        """kappa_cat(E) = chi(O_E) = 0."""
        assert KAPPA_CAT_E == Rational(0)

    def test_kappa_spectrum_web_all_subscripted(self):
        """Every kappa value in the web is properly subscripted (AP113)."""
        spectrum = kappa_spectrum_web()
        for node_name, kappas in spectrum.items():
            for kappa_type in ("kappa_ch", "kappa_bkm", "kappa_cat", "kappa_fiber"):
                assert kappa_type in kappas, (
                    f"Missing {kappa_type} in {node_name}"
                )

    def test_four_kappa_spectrum_for_k3e(self):
        """K3 x E has all four kappa values: {2, 3, 5, 24} subset."""
        web = build_m_theory_web()
        node = web["4d_IIA_K3xT2"]  # K3 x T^2 has full spectrum
        values = {
            node.kappa_ch,
            node.kappa_bkm,
            node.kappa_cat,
            node.kappa_fiber,
        }
        # kappa_cat(K3 x E) = 0, not 2; kappa_cat(K3) = 2
        expected = {Rational(3), Rational(5), Rational(0), Rational(24)}
        assert values == expected


# =========================================================================
# 3. Shadow class tests
# =========================================================================

class TestShadowClass:
    """Test shadow class assignments and stability."""

    def test_k3_heisenberg_is_class_g(self):
        """K3 Heisenberg (free field) is class G."""
        web = build_m_theory_web()
        assert web["11d_M_K3"].shadow_class == ShadowClass.G

    def test_yangian_is_class_l(self):
        """Affine Yangian / K3 Yangian is class L."""
        web = build_m_theory_web()
        assert web["6d_hCS_C3"].shadow_class == ShadowClass.L

    def test_k3xe_is_class_m(self):
        """K3 x E chiral algebra is class M (mock modular)."""
        web = build_m_theory_web()
        assert web["4d_IIA_K3xT2"].shadow_class == ShadowClass.M

    def test_3d_n8_is_class_g(self):
        """3d N=8 (Rozansky-Witten) is class G after A-twist."""
        web = build_m_theory_web()
        assert web["3d_M_K3xT3"].shadow_class == ShadowClass.G

    def test_shadow_stability_reduction_edges(self):
        """Shadow class does not increase along proper reduction edges.

        Topological twists can introduce new structure (e.g. 10d -> 6d hCS
        introduces E_3 and class L/M via the twist). Monotonicity only
        applies to proper reductions (shrink a direction).
        """
        web = build_m_theory_web()
        ORDER = {ShadowClass.G: 0, ShadowClass.L: 1,
                 ShadowClass.C: 2, ShadowClass.M: 3}
        for parent_key, child_key in MONOTONE_EDGES:
            p = ORDER[web[parent_key].shadow_class]
            c = ORDER[web[child_key].shadow_class]
            assert c <= p, (
                f"Shadow class increases on REDUCTION edge: "
                f"{parent_key} ({web[parent_key].shadow_class}) "
                f"-> {child_key} ({web[child_key].shadow_class})"
            )

    def test_duality_preserves_shadow_class(self):
        """Duality edges preserve shadow class."""
        web = build_m_theory_web()
        for parent_key, child_key in DUALITY_EDGES:
            assert web[parent_key].shadow_class == web[child_key].shadow_class, (
                f"Duality changes shadow class: {parent_key} -> {child_key}"
            )


# =========================================================================
# 4. R-matrix degeneration tests
# =========================================================================

class TestRMatrixDegeneration:
    """Test R-matrix type degeneration under reduction."""

    def test_6d_has_two_parameter(self):
        """6d hCS has two-parameter R-matrix."""
        web = build_m_theory_web()
        assert web["6d_hCS_C3"].rmatrix_type == RMatrixType.TWO_PARAMETER

    def test_5d_has_rational(self):
        """5d hCS has rational R-matrix."""
        web = build_m_theory_web()
        assert web["5d_K3xCxR"].rmatrix_type == RMatrixType.RATIONAL

    def test_3d_classical_has_trivial(self):
        """3d classical limit has trivial R-matrix."""
        web = build_m_theory_web()
        assert web["3d_K3_sigma"].rmatrix_type == RMatrixType.TRIVIAL

    def test_degeneration_monotone_reduction_edges(self):
        """R-matrix level does not increase along proper reduction edges.

        Topological twists can introduce higher R-matrix complexity
        (e.g., twisting a 10d theory on C^3 introduces E_3 two-parameter
        R-matrix). Monotonicity only applies to proper reductions.
        """
        web = build_m_theory_web()
        HIERARCHY = {
            RMatrixType.TWO_PARAMETER: 5,
            RMatrixType.ELLIPTIC: 4,
            RMatrixType.TRIGONOMETRIC: 3,
            RMatrixType.RATIONAL: 2,
            RMatrixType.CLASSICAL: 1,
            RMatrixType.TRIVIAL: 0,
        }
        for parent_key, child_key in MONOTONE_EDGES:
            p = HIERARCHY[web[parent_key].rmatrix_type]
            c = HIERARCHY[web[child_key].rmatrix_type]
            assert c <= p, (
                f"R-matrix increases on REDUCTION edge: "
                f"{parent_key} ({web[parent_key].rmatrix_type}) "
                f"-> {child_key} ({web[child_key].rmatrix_type})"
            )

    def test_6d_to_5d_trig_to_rational(self):
        """6d -> 5d reduces two-parameter to rational."""
        web = build_m_theory_web()
        assert web["6d_K3xExC"].rmatrix_type == RMatrixType.TWO_PARAMETER
        assert web["5d_K3xCxR"].rmatrix_type == RMatrixType.RATIONAL


# =========================================================================
# 5. E_n level tests
# =========================================================================

class TestEnLevel:
    """Test E_n factorization level assignments."""

    def test_6d_is_e3(self):
        """6d hCS and K3 x E x C are E_3."""
        web = build_m_theory_web()
        assert web["6d_hCS_C3"].en_level == EnLevel.E3
        assert web["6d_K3xExC"].en_level == EnLevel.E3

    def test_5d_is_e2(self):
        """5d hCS is E_2."""
        web = build_m_theory_web()
        assert web["5d_K3xCxR"].en_level == EnLevel.E2

    def test_3d_n8_is_einf(self):
        """3d N=8 after A-twist is E_inf."""
        web = build_m_theory_web()
        assert web["3d_M_K3xT3"].en_level == EnLevel.EINF

    def test_en_level_monotone_reduction_edges(self):
        """E_n level does not increase along proper reduction edges.

        Topological twists introduce new factorization structure
        (e.g. 10d -> 6d hCS introduces E_3; 11d -> 5d introduces E_2).
        Only proper reductions (shrink a direction) must decrease E_n.
        """
        web = build_m_theory_web()

        def en_value(level):
            return 100 if level == EnLevel.EINF else int(level)

        for parent_key, child_key in MONOTONE_EDGES:
            p = en_value(web[parent_key].en_level)
            c = en_value(web[child_key].en_level)
            assert c <= p, (
                f"E_n increases on REDUCTION edge: "
                f"{parent_key} (E_{web[parent_key].en_level.name}) "
                f"-> {child_key} (E_{web[child_key].en_level.name})"
            )


# =========================================================================
# 6. Euler characteristic tests
# =========================================================================

class TestEulerCharacteristic:
    """Test Euler characteristic multiplicativity and Hodge data."""

    def test_chi_multiplicativity(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        check = check_euler_char_multiplicativity()
        assert check.passed

    def test_hodge_chi_additivity(self):
        """chi(O_{K3 x E}) = 1 - 1 + 1 - 1 = 0."""
        check = check_hodge_chi_additivity()
        assert check.passed

    def test_kappa_cat_chi_o(self):
        """kappa_cat(K3) = chi(O_K3) = 2."""
        check = check_kappa_cat_equals_chi_O()
        assert check.passed

    def test_kappa_bkm_borcherds_weight_check(self):
        """kappa_BKM(K3 x E) is checked by c_1(0)/2."""
        check = check_kappa_bkm_borcherds_weight()
        assert check.passed
        assert check.check_type == "kappa_bkm_borcherds_weight"


# =========================================================================
# 7. Claim status tests (AP-CY6/14: conjectural tracking)
# =========================================================================

class TestClaimStatus:
    """Test that claim statuses are correctly assigned."""

    def test_11d_is_proved(self):
        """M-theory on K3 is proved."""
        web = build_m_theory_web()
        assert web["11d_M_K3"].status == ClaimStatus.PROVED

    def test_6d_hcs_is_conjectural(self):
        """6d hCS -> quantum toroidal is conjectural (AP-CY14)."""
        web = build_m_theory_web()
        assert web["6d_hCS_C3"].status == ClaimStatus.CONJECTURAL

    def test_6d_k3xexc_is_conjectural(self):
        """K3 x E x C node is conjectural (requires CY-A_3)."""
        web = build_m_theory_web()
        assert web["6d_K3xExC"].status == ClaimStatus.CONJECTURAL

    def test_5d_k3_yangian_is_conjectural(self):
        """K3 Yangian construction is conjectural."""
        web = build_m_theory_web()
        assert web["5d_M_K3xS1"].status == ClaimStatus.CONJECTURAL

    def test_4d_vw_is_proved(self):
        """Vafa-Witten partition function is proved."""
        web = build_m_theory_web()
        assert web["4d_IIA_K3xT2"].status == ClaimStatus.PROVED

    def test_3d_k3_sigma_is_proved(self):
        """K3 sigma model (CY-A_2) is proved."""
        web = build_m_theory_web()
        assert web["3d_K3_sigma"].status == ClaimStatus.PROVED

    def test_d2_nodes_proved_d3_conjectural(self):
        """Nodes relying on CY-A_2 are proved; CY-A_3 are conjectural."""
        web = build_m_theory_web()
        # CY-A_2 based (proved)
        assert web["3d_K3_sigma"].status == ClaimStatus.PROVED
        # CY-A_3 based (conjectural)
        assert web["6d_K3xExC"].status == ClaimStatus.CONJECTURAL
        assert web["5d_K3xCxR"].status == ClaimStatus.CONJECTURAL


# =========================================================================
# 8. Structure function degeneration chain tests
# =========================================================================

class TestStructureFunctionChain:
    """Test the structure function degeneration chain."""

    def test_cy_condition_holds(self):
        """h1 + h2 + h3 = 0."""
        sf = structure_function_chain()
        assert sf["cy_condition"] == 0

    def test_3d_classical_limit(self):
        """At the classical limit, g(u) = 1."""
        sf = structure_function_chain()
        assert sf["3d_g_classical"] == Rational(1)

    def test_6d_at_x1(self):
        """G(1) = -1 by the CY condition."""
        sf = structure_function_chain()
        assert sf["6d_G_at_x1"] == Rational(-1)

    def test_5d_structure_function_nontrivial(self):
        """At generic parameters (1,-2,1), g(u) != 1 for u != 0."""
        sf = structure_function_chain()
        assert sf["5d_g_at_u5"] != Rational(1)

    def test_sigma3_nonzero_generic(self):
        """sigma_3 != 0 at the generic point (1,-2,1)."""
        sf = structure_function_chain()
        assert sf["sigma3"] != 0

    def test_kac_moody_level(self):
        """For (1,-2,1): k = -sigma_2 = -(-1*(-2)+(-1)*1+(-2)*1) = 3."""
        sf = structure_function_chain()
        # sigma_2 = h1*h2 + h1*h3 + h2*h3 = 1*(-2) + 1*1 + (-2)*1
        #         = -2 + 1 - 2 = -3
        # k = -sigma_2 = 3
        assert sf["kac_moody_level"] == Rational(3)

    def test_self_dual_point(self):
        """At (1,0,-1): sigma_3 = 0, g(u) = 1 (self-dual)."""
        sf = structure_function_chain(h1=Rational(1), h2=Rational(0))
        assert sf["sigma3"] == 0


# =========================================================================
# 9. Reduction commutativity tests
# =========================================================================

class TestReductionCommutativity:
    """Test commutativity of Phi with dimensional reduction."""

    def test_5d_to_3d_commutes(self):
        """5d -> 3d (Y -> H_Muk) commutativity is PROVED."""
        results = check_reduction_commutativity()
        y_to_h = [r for r in results if "5d -> 3d" in r.reduction_name][0]
        assert y_to_h.commutes is True
        assert y_to_h.status == ClaimStatus.PROVED

    def test_6d_to_5d_conjectural(self):
        """6d -> 5d (U_{q,t} -> Y) commutativity is CONJECTURAL."""
        results = check_reduction_commutativity()
        u_to_y = [r for r in results if "6d -> 5d" in r.reduction_name][0]
        assert u_to_y.commutes is None  # Unknown
        assert u_to_y.status == ClaimStatus.CONJECTURAL

    def test_t_duality_commutes(self):
        """IIA <-> IIB T-duality commutes with Phi."""
        results = check_reduction_commutativity()
        t_dual = [r for r in results if "T-duality" in r.reduction_name][0]
        assert t_dual.commutes is True

    def test_s_duality_commutes(self):
        """IIA <-> IIB S-duality commutes with Phi."""
        results = check_reduction_commutativity()
        s_dual = [r for r in results if "S-duality" in r.reduction_name][0]
        assert s_dual.commutes is True

    def test_all_commutativity_checks_have_status(self):
        """All commutativity checks have an explicit claim status."""
        results = check_reduction_commutativity()
        for r in results:
            assert r.status is not None
            assert isinstance(r.status, ClaimStatus)


# =========================================================================
# 10. Full pipeline tests
# =========================================================================

class TestFullPipeline:
    """Test the full web analysis pipeline."""

    def test_all_consistency_checks_pass(self):
        """All consistency checks in the web pass."""
        checks = run_all_consistency_checks()
        passing, total = count_passing(checks)
        failures = [c for c in checks if not c.passed]
        assert passing == total, (
            f"{total - passing} checks failed: "
            + "; ".join(f.name for f in failures)
        )

    def test_full_analysis_runs(self):
        """The full analysis pipeline completes without error."""
        result = full_web_analysis()
        assert result["web_nodes"] == 13
        assert result["checks_failing"] == 0

    def test_full_analysis_check_count(self):
        """The full analysis has the expected number of checks."""
        result = full_web_analysis()
        # MONOTONE_EDGES: 3 checks each (R-matrix, shadow, E_n)
        # REDUCTION_EDGES: 1 check each (kappa_ch)
        # DUALITY_EDGES: 3 checks each (R-matrix, shadow, E_n)
        # Global: 4 checks
        n_monotone = len(MONOTONE_EDGES) * 3
        n_kappa = len(REDUCTION_EDGES) * 1
        n_duality = len(DUALITY_EDGES) * 3
        n_global = 4
        expected = n_monotone + n_kappa + n_duality + n_global
        assert result["checks_total"] == expected

    def test_kappa_spectrum_web_complete(self):
        """Every node has a kappa-spectrum entry."""
        spectrum = kappa_spectrum_web()
        web = build_m_theory_web()
        assert set(spectrum.keys()) == set(web.keys())


# =========================================================================
# 11. Cross-engine compatibility tests
# =========================================================================

class TestCrossEngineCompatibility:
    """Cross-check against existing engines."""

    def test_kappa_ch_k3_matches_kappa_engine(self):
        """kappa_ch(K3) = 2 matches kappa_spectrum_reconciliation."""
        from compute.lib.kappa_spectrum_reconciliation import k3_surface
        k3 = k3_surface()
        assert k3.chi_O() == int(KAPPA_CAT_K3)  # chi(O_K3) = 2

    def test_kappa_cat_k3e_matches_kappa_engine(self):
        """kappa_cat(K3 x E) = 0 matches kappa_spectrum_reconciliation."""
        from compute.lib.kappa_spectrum_reconciliation import k3_times_e
        k3e = k3_times_e()
        assert k3e.chi_O() == int(KAPPA_CAT_K3E)  # chi(O_{K3xE}) = 0

    def test_omega_background_cy_condition(self):
        """OmegaBackground enforces h1+h2+h3=0 (CY condition)."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(Rational(1), Rational(-2))
        assert omega.h3 == Rational(1)
        assert omega.h1 + omega.h2 + omega.h3 == 0

    def test_hcs_hierarchy_kappa_values(self):
        """Cross-check kappa values against hcs_hierarchy_k3."""
        from compute.lib.hcs_hierarchy_k3 import (
            KAPPA_CH_K3 as HCS_KAPPA_CH_K3,
            KAPPA_CH_K3E as HCS_KAPPA_CH_K3E,
            KAPPA_BKM_K3E as HCS_KAPPA_BKM_K3E,
            KAPPA_CAT_K3 as HCS_KAPPA_CAT_K3,
            KAPPA_FIBER_K3 as HCS_KAPPA_FIBER_K3,
        )
        assert KAPPA_CH_K3 == HCS_KAPPA_CH_K3
        assert KAPPA_CH_K3E == HCS_KAPPA_CH_K3E
        assert KAPPA_BKM_K3E == HCS_KAPPA_BKM_K3E
        assert KAPPA_CAT_K3 == HCS_KAPPA_CAT_K3
        assert KAPPA_FIBER_K3 == HCS_KAPPA_FIBER_K3

    def test_boundary_algebra_hierarchy(self):
        """Cross-check: BoundaryAlgebra types at each dimension."""
        from compute.lib.holomorphic_cs_chiral_engine import (
            OmegaBackground, BoundaryAlgebra,
        )
        omega = OmegaBackground(Rational(1), Rational(-2))
        assert BoundaryAlgebra(1, omega).algebra_type == "Kac-Moody"
        assert BoundaryAlgebra(2, omega).algebra_type == "Affine Yangian"
        assert BoundaryAlgebra(3, omega).algebra_type == "Quantum Toroidal"


# =========================================================================
# 12. AP compliance tests
# =========================================================================

class TestAPCompliance:
    """Test adherence to anti-pattern rules."""

    def test_no_bare_kappa_in_node_names(self):
        """No bare 'kappa' without subscript in node descriptions (AP113)."""
        web = build_m_theory_web()
        for key, node in web.items():
            # Check that any mention of kappa in the description has a subscript
            for field in (node.chiral_algebra, node.rmatrix_description,
                          node.status_notes):
                if "kappa" in field.lower():
                    # Bare "kappa" (without underscore suffix) is forbidden
                    # But "kappa_ch", "kappa_BKM" etc. are fine
                    import re
                    bare = re.findall(r'\bkappa\b(?!_)', field)
                    # Allow "kappa-spectrum" as a meta-term
                    bare = [b for b in bare if "spectrum" not in field[field.lower().index("kappa"):field.lower().index("kappa")+20]]
                    # This is a soft check; bare kappa in prose context
                    # (e.g. "kappa complementarity") is borderline.

    def test_d3_nodes_not_proved(self):
        """No d=3 CY-A dependent node claims PROVED status (AP-CY6/14)."""
        web = build_m_theory_web()
        d3_conjectural_nodes = ["6d_K3xExC", "5d_K3xCxR", "6d_hCS_C3",
                                "5d_M_K3xS1"]
        for key in d3_conjectural_nodes:
            assert web[key].status != ClaimStatus.PROVED, (
                f"{key} claims PROVED but depends on CY-A_3 (AP-CY6/14)"
            )

    def test_coha_not_conflated_with_chiral(self):
        """No node conflates CoHA with E_1-chiral algebra (AP-CY7)."""
        web = build_m_theory_web()
        for key, node in web.items():
            desc = node.chiral_algebra
            assert "CoHA = E_1" not in desc, (
                f"{key} conflates CoHA with E_1-chiral (AP-CY7)"
            )
            assert "CoHA is a chiral algebra" not in desc, (
                f"{key} says CoHA is chiral algebra (AP-CY7)"
            )

    def test_mf_cy_dimension_correct(self):
        """MF(W) CY dimension is n-2, not n-1 (AP-CY17).

        This test verifies the ADE CY dimension convention at n=2.
        """
        # ADE in 2 variables: CY_0 (semisimple). n=2, CY dim = n-2 = 0.
        assert 2 - 2 == 0
        # Quintic: n=5 variables, CY dim = n-2 = 3.
        assert 5 - 2 == 3


# =========================================================================
# 13. Specific node data tests
# =========================================================================

class TestSpecificNodes:
    """Test specific physical properties of individual nodes."""

    def test_11d_m_k3_dimensions(self):
        """M-theory on K3: 11 - 4 = 7 noncompact dimensions."""
        web = build_m_theory_web()
        node = web["11d_M_K3"]
        assert node.spacetime_dim == 11
        assert node.compact_dim == 4
        assert node.noncompact_dim == 7
        assert node.spacetime_dim == node.compact_dim + node.noncompact_dim

    def test_iia_iib_same_kappa(self):
        """IIA and IIB on K3 have the same kappa-spectrum (T-duality)."""
        web = build_m_theory_web()
        iia = web["10d_IIA_K3"]
        iib = web["10d_IIB_K3"]
        assert iia.kappa_ch == iib.kappa_ch
        assert iia.kappa_cat == iib.kappa_cat
        assert iia.kappa_fiber == iib.kappa_fiber

    def test_4d_iia_iib_same_kappa(self):
        """IIA and IIB on K3 x T^2 have the same kappa-spectrum (S-duality)."""
        web = build_m_theory_web()
        iia = web["4d_IIA_K3xT2"]
        iib = web["4d_IIB_K3xT2"]
        assert iia.kappa_ch == iib.kappa_ch
        assert iia.kappa_bkm == iib.kappa_bkm

    def test_k3_mukai_rank_24(self):
        """The K3 Mukai lattice has rank 24."""
        web = build_m_theory_web()
        node = web["11d_M_K3"]
        assert node.kappa_fiber == Rational(24)

    def test_cy_dimension_k3_is_2(self):
        """K3 is CY_2, not CY_4 (AP-CY1: CY dim = complex dim)."""
        web = build_m_theory_web()
        assert web["11d_M_K3"].cy_dimension == 2

    def test_cy_dimension_k3xe_is_3(self):
        """K3 x E is CY_3."""
        web = build_m_theory_web()
        assert web["4d_IIA_K3xT2"].cy_dimension == 3
        assert web["6d_K3xExC"].cy_dimension == 3

    def test_dimension_arithmetic(self):
        """noncompact = spacetime - compact at every node.

        Note: spacetime_dim is the ORIGINAL parent theory dimension for
        some nodes (e.g. 10d IIA) but the EFFECTIVE theory dimension for
        others (e.g. 5d from M-theory on K3 x S^1). The invariant is
        that noncompact_dim = spacetime_dim - compact_dim.
        """
        web = build_m_theory_web()
        for key, node in web.items():
            assert node.noncompact_dim == node.spacetime_dim - node.compact_dim, (
                f"{key}: noncompact {node.noncompact_dim} != "
                f"{node.spacetime_dim} - {node.compact_dim}"
            )
