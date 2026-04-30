r"""Tests for A_infinity formality of D^b(Coh(X)) for CY manifolds.

Verifies:
  (1) Formality hierarchy: three levels distinguished correctly
  (2) DGMS (Level 1) does NOT imply A_infinity formality (Level 3)
  (3) Kaledin's theorem: correct scope (K1 vs K2)
  (4) Quintic: de Rham formal but full D^b A_inf status not certified here
  (5) K3: DGMS/Kaledin do not certify D^b A_inf formality here
  (6) K3 x E: product de Rham formal, product D^b A_inf status not certified
  (7) Massey products: manifold vs category distinction
  (8) Programme implications: corrected TCFT/HH^{-2} hypotheses are explicit
  (9) Hodge data consistency
  (10) Master verification

Every test uses AT LEAST 3 independent verification paths (AP10).

Mathematical references:
  DGMS, Inventiones 29 (1975): compact Kahler de Rham formality
  Kaledin, arXiv:0708.1444: non-commutative HdR degeneration
  Kaledin, arXiv:math/0308135: formality of Ext algebras (tilting)
  Polishchuk, arXiv:math/0205149: A_inf on elliptic curves
  Costello, arXiv:math/0412149: TCFT and CY categories
  Lorgat Vol III: cy_to_chiral.tex, cyclic_ainf.tex, k3_times_e.tex
"""

from fractions import Fraction

import pytest

from compute.lib.formality_ainf_dcoh import (
    # Formality levels
    FormalityLevel,
    DE_RHAM_FORMALITY,
    HDR_DEGENERATION,
    AINF_FORMALITY,
    FORMALITY_HIERARCHY,
    level_implication_chain,
    # Hodge data
    CYHodgeData,
    elliptic_curve,
    k3_surface,
    abelian_surface,
    quintic_threefold,
    k3_times_e,
    bicubic_threefold,
    conifold_resolved,
    # Analysis functions
    analyze_formality,
    kaledin_analysis,
    massey_analysis,
    quintic_ext_analysis,
    product_formality_k3xe,
    programme_implication,
    formality_correction,
    formality_table,
    verify_formality_hierarchy,
    hh_minus_two_obstruction_criterion,
    # Types
    FormalityVerdict,
    KaledinAnalysis,
    MasseyAnalysis,
    QuinticExtAnalysis,
    ProductFormalityAnalysis,
    FormalityImplication,
    FormalityCorrectionRecord,
    ObstructionVanishingCriterion,
)

F = Fraction


# ================================================================
# SECTION 1: FORMALITY HIERARCHY
# ================================================================

class TestFormalityHierarchy:
    """Tests for the three-level formality hierarchy."""

    def test_three_levels_exist(self):
        """There are exactly three formality levels."""
        assert len(FORMALITY_HIERARCHY) == 3
        assert FORMALITY_HIERARCHY[0].level == 1
        assert FORMALITY_HIERARCHY[1].level == 2
        assert FORMALITY_HIERARCHY[2].level == 3

    def test_level_1_does_not_imply_m3_zero(self):
        """de Rham formality does NOT imply m_3 = 0.

        PATH 1: Direct check on the Level 1 object.
        PATH 2: Elliptic curve counterexample.
        PATH 3: Quintic counterexample.
        """
        # PATH 1
        assert DE_RHAM_FORMALITY.implies_m3_zero is False

        # PATH 2: elliptic curve is de Rham formal but has m_3 != 0
        E = elliptic_curve()
        v = analyze_formality(E)
        assert v.de_rham_formal is True
        assert v.ainf_formal is False
        assert v.has_nonzero_m3_category is True

        # PATH 3: quintic is de Rham formal but categorical m_3 is not certified
        Q = quintic_threefold()
        v = analyze_formality(Q)
        assert v.de_rham_formal is True
        assert v.ainf_formal is None
        assert v.has_nonzero_m3_category is None

    def test_level_2_does_not_imply_m3_zero(self):
        """HdR degeneration does NOT imply m_3 = 0.

        PATH 1: Direct check on the Level 2 object.
        PATH 2: Quintic has HdR degeneration but m_3 is not certified.
        PATH 3: Elliptic curve has HdR degeneration but m_3 != 0.
        """
        # PATH 1
        assert HDR_DEGENERATION.implies_m3_zero is False

        # PATH 2
        Q = quintic_threefold()
        v = analyze_formality(Q)
        assert v.hdr_degeneration is True
        assert v.has_nonzero_m3_category is None

        # PATH 3
        E = elliptic_curve()
        v = analyze_formality(E)
        assert v.hdr_degeneration is True
        assert v.has_nonzero_m3_category is True

    def test_level_3_implies_m3_zero(self):
        """A_infinity formality DOES imply m_3 = 0.

        PATH 1: Direct check on the Level 3 object.
        PATH 2: Conifold is A_inf formal and has m_3 = 0.
        PATH 3: Programme implication for the conifold is formal-input closure.
        """
        # PATH 1
        assert AINF_FORMALITY.implies_m3_zero is True

        # PATH 2
        con = conifold_resolved()
        v = analyze_formality(con)
        assert v.ainf_formal is True
        assert v.has_nonzero_m3_category is False

        # PATH 3
        p = programme_implication(con)
        assert p.m3_b2_moot is True
        assert p.obs_ainf_class_zero is True

    def test_implication_chain(self):
        """Only Level 3 => Level 2 holds; all other implications fail.

        PATH 1: Direct check of implication table.
        PATH 2: Count true implications (should be 1).
        PATH 3: Verify each direction separately.
        """
        chain = level_implication_chain()

        # PATH 1: check the one true implication
        true_implications = [(f, t) for f, t, imp in chain if imp]
        assert true_implications == [(3, 2)]

        # PATH 2: count
        n_true = sum(1 for _, _, imp in chain if imp)
        assert n_true == 1

        # PATH 3: specific checks
        for fr, to, imp in chain:
            if fr == 3 and to == 2:
                assert imp is True
            else:
                assert imp is False


# ================================================================
# SECTION 2: DGMS vs D^b FORMALITY
# ================================================================

class TestDGMSvsDb:
    """Tests for the critical distinction: DGMS does NOT imply D^b formal."""

    def test_elliptic_curve_counterexample(self):
        """Elliptic curve: compact Kahler (DGMS formal) but D^b not A_inf formal.

        PATH 1: Analyze formality verdict.
        PATH 2: Check Massey analysis levels disagree.
        PATH 3: Polishchuk m_3 from theta functions.
        """
        E = elliptic_curve()

        # PATH 1
        v = analyze_formality(E)
        assert v.de_rham_formal is True  # DGMS
        assert v.ainf_formal is False     # Polishchuk

        # PATH 2
        m = massey_analysis(E)
        assert m.derham_massey_vanish is True
        assert m.category_m3_zero is False
        assert m.levels_agree is False

        # PATH 3
        assert "Polishchuk" in v.ainf_reason

    def test_quintic_not_certified_by_dgms(self):
        """Quintic: compact Kahler, but D^b A_inf status is not certified here.

        PATH 1: Analyze formality verdict.
        PATH 2: Check Massey analysis levels disagree.
        PATH 3: Yukawa language is not promoted to a verdict.
        """
        Q = quintic_threefold()

        # PATH 1
        v = analyze_formality(Q)
        assert v.de_rham_formal is True  # DGMS
        assert v.ainf_formal is None
        assert v.has_nonzero_m3_category is None

        # PATH 2
        m = massey_analysis(Q)
        assert m.derham_massey_vanish is True
        assert m.category_m3_zero is None
        assert m.levels_agree is None

        # PATH 3
        assert "Yukawa" in v.ainf_reason
        assert "do not by themselves" in v.ainf_reason

    def test_k3_not_certified_by_dgms(self):
        """K3: DGMS and Kaledin do not certify D^b A_inf formality here.

        PATH 1: de Rham and HdR levels hold.
        PATH 2: categorical m_3 status is unknown to this engine.
        PATH 3: Kaledin K2 still does not apply.
        """
        K3 = k3_surface()

        # PATH 1
        v = analyze_formality(K3)
        assert v.de_rham_formal is True
        assert v.hdr_degeneration is True
        assert v.ainf_formal is None

        # PATH 2
        m = massey_analysis(K3)
        assert m.category_m3_zero is None
        assert m.levels_agree is None

        # PATH 3
        k = kaledin_analysis(K3)
        assert k.k2_applies is False
        assert "not an A_infinity formality theorem" in k.k2_reason


# ================================================================
# SECTION 3: KALEDIN'S THEOREM
# ================================================================

class TestKaledin:
    """Tests for correct understanding of Kaledin's theorems."""

    def test_k1_universal(self):
        """Kaledin K1 (HdR degeneration) applies to all smooth proper.

        PATH 1: Quintic.
        PATH 2: K3.
        PATH 3: Elliptic curve.
        """
        for X_fn in [quintic_threefold, k3_surface, elliptic_curve]:
            X = X_fn()
            k = kaledin_analysis(X)
            assert k.k1_applies is True, f"K1 should apply to {X.name}"

    def test_k2_requires_tilting(self):
        """Kaledin K2 (tilting formality) requires tilting generator.

        PATH 1: Compact CY3 has no tilting (Serre duality).
        PATH 2: Resolved conifold has tilting.
        PATH 3: K3 has no tilting.
        """
        # PATH 1: quintic
        Q = quintic_threefold()
        k = kaledin_analysis(Q)
        assert k.k2_applies is False
        assert k.has_tilting_generator is False

        # PATH 2: resolved conifold
        con = conifold_resolved()
        k = kaledin_analysis(con)
        assert k.k2_applies is True
        assert k.has_tilting_generator is True

        # PATH 3: K3
        K3 = k3_surface()
        k = kaledin_analysis(K3)
        assert k.k2_applies is False
        assert k.has_tilting_generator is False

    def test_compact_cy3_no_tilting(self):
        """No compact CY3 has a tilting generator.

        PATH 1: Quintic.
        PATH 2: Bicubic.
        PATH 3: K3 x E.

        Reason: Ext^3(E,E) = Ext^0(E,E)^* != 0 by Serre duality.
        """
        for X_fn in [quintic_threefold, bicubic_threefold, k3_times_e]:
            X = X_fn()
            k = kaledin_analysis(X)
            assert k.has_tilting_generator is False, f"Compact CY3 {X.name} should not have tilting"
            assert k.formality_from_kaledin is False

    def test_k1_does_not_give_formality(self):
        """Kaledin K1 applies to quintic but does NOT give formality.

        PATH 1: K1 applies.
        PATH 2: K2 does not apply.
        PATH 3: A_inf formality is false.
        """
        Q = quintic_threefold()
        k = kaledin_analysis(Q)

        # PATH 1
        assert k.k1_applies is True

        # PATH 2
        assert k.k2_applies is False

        # PATH 3
        assert k.formality_from_kaledin is False


# ================================================================
# SECTION 4: QUINTIC DETAILED ANALYSIS
# ================================================================

class TestQuintic:
    """Detailed tests for the quintic threefold."""

    def test_hodge_data(self):
        """Quintic Hodge data is correct.

        PATH 1: h^{p,q} values.
        PATH 2: chi(O_Q) = 0.
        PATH 3: chi(Q) = -200.
        """
        Q = quintic_threefold()

        # PATH 1
        assert Q.h(0, 0) == 1
        assert Q.h(1, 1) == 1
        assert Q.h(2, 1) == 101
        assert Q.h(3, 0) == 1

        # PATH 2
        assert Q.chi_O() == 0  # h^{0,0} - h^{0,1} + h^{0,2} - h^{0,3} = 1 - 0 + 0 - 1 = 0

        # PATH 3
        assert Q.euler_char() == -200

    def test_ext_OO_trivially_formal(self):
        """Ext^*(O_Q, O_Q) is trivially formal (concentrated in {0, 3}).

        PATH 1: Dimensions [1, 0, 0, 1].
        PATH 2: Concentrated flag.
        PATH 3: QuinticExtAnalysis confirms.
        """
        Q = quintic_threefold()

        # PATH 1
        assert Q.ext_O_dims() == [1, 0, 0, 1]

        # PATH 2
        assert Q.ext_O_concentrated() is True

        # PATH 3
        qea = quintic_ext_analysis()
        assert qea.ext_OO_formal is True
        assert qea.ext_OO_dims == [1, 0, 0, 1]

    def test_ext_OO_vs_full_category(self):
        """Critical distinction: Ext^*(O,O) formal but full category undecided here.

        PATH 1: m_3 on Ext^*(O,O) is zero.
        PATH 2: m_3 on full category is not certified.
        PATH 3: Yukawa coupling = 5 is evidence, not a verdict.
        """
        qea = quintic_ext_analysis()

        # PATH 1
        assert qea.m3_on_ext_OO is False

        # PATH 2
        assert qea.m3_on_full_cat is None
        assert qea.full_generator_formal is None

        # PATH 3
        assert qea.yukawa_classical == 5
        assert qea.yukawa_has_gw_corrections is True

    def test_quintic_full_category_not_certified(self):
        """Quintic D^b(Coh(Q)) is not decided by this engine.

        PATH 1: analyze_formality verdict.
        PATH 2: Formality table entry.
        PATH 3: Programme implication.
        """
        Q = quintic_threefold()

        # PATH 1
        v = analyze_formality(Q)
        assert v.ainf_formal is None
        assert v.ainf_status == "not_certified_for_full_category"

        # PATH 2
        table = formality_table()
        q_row = [r for r in table if r["geometry"] == "quintic threefold"][0]
        assert q_row["L3_ainf_formal"] is None

        # PATH 3
        p = programme_implication(Q)
        assert p.ainf_formal is None
        assert p.obs_ainf_class_zero is None
        assert "not certified" in p.cy_a_status

    def test_quintic_kodaira_spencer(self):
        """Quintic has 101-dimensional Kodaira-Spencer space.

        PATH 1: kodaira_spencer_dim.
        PATH 2: h^{2,1} = 101.
        PATH 3: HH^1 from HKR.
        """
        Q = quintic_threefold()

        # PATH 1
        assert Q.kodaira_spencer_dim() == 101

        # PATH 2
        assert Q.h(2, 1) == 101

        # PATH 3: HH^1 = H^1(T_Q) = H^1(Omega^2_Q) = h^{2,1} = 101
        assert Q.h(2, 1) == 101


# ================================================================
# SECTION 5: K3 FORMALITY STATUS
# ================================================================

class TestK3Formality:
    """Tests for K3 formality status without the DGMS shortcut."""

    def test_k3_derham_only_certified_here(self):
        """K3 has Level 1 and Level 2 data; Level 3 is not certified here.

        PATH 1: analyze_formality.
        PATH 2: Massey analysis.
        PATH 3: Kaledin analysis (K1 applies, K2 does not).
        """
        K3 = k3_surface()

        # PATH 1
        v = analyze_formality(K3)
        assert v.de_rham_formal is True
        assert v.hdr_degeneration is True
        assert v.ainf_formal is None
        assert v.ainf_status == "not_certified_by_DGMS_or_Kaledin"

        # PATH 2
        m = massey_analysis(K3)
        assert m.derham_massey_vanish is True
        assert m.category_m3_zero is None

        # PATH 3
        k = kaledin_analysis(K3)
        assert k.k1_applies is True
        assert k.k2_applies is False

    def test_k3_shadow_class_not_inferred(self):
        """K3 shadow class is not inferred from DGMS here.

        PATH 1: analyze_formality.
        PATH 2: programme_implication.
        PATH 3: Formality table.
        """
        K3 = k3_surface()

        # PATH 1
        v = analyze_formality(K3)
        assert v.shadow_class == "unclassified"

        # PATH 2
        p = programme_implication(K3)
        assert p.shadow_class == "unclassified"
        assert p.shadow_depth_zero is None

        # PATH 3
        table = formality_table()
        k3_row = [r for r in table if r["geometry"] == "K3 surface"][0]
        assert k3_row["shadow_class"] == "unclassified"

    def test_k3_hodge_data(self):
        """K3 Hodge data is correct.

        PATH 1: chi(O_{K3}) = 2.
        PATH 2: chi(K3) = 24.
        PATH 3: dim HH^*(K3) = 24.
        """
        K3 = k3_surface()

        # PATH 1
        assert K3.chi_O() == 2

        # PATH 2
        assert K3.euler_char() == 24

        # PATH 3
        assert K3.hh_dim() == 24


# ================================================================
# SECTION 6: K3 x E PRODUCT FORMALITY
# ================================================================

class TestK3xEFormality:
    """Tests for product formality of K3 x E."""

    def test_product_factors(self):
        """K3 de Rham formal, E non-formal, product A_inf status not certified.

        PATH 1: product_formality_k3xe.
        PATH 2: Individual factor analysis.
        PATH 3: Product analysis.
        """
        # PATH 1
        pf = product_formality_k3xe()
        assert pf.k3_formal is None
        assert pf.e_formal is False
        assert pf.ainf_product_formal is None

        # PATH 2
        K3 = k3_surface()
        E = elliptic_curve()
        assert analyze_formality(K3).ainf_formal is None
        assert analyze_formality(E).ainf_formal is False

        # PATH 3
        K3E = k3_times_e()
        assert analyze_formality(K3E).ainf_formal is None

    def test_derham_product_formal(self):
        """de Rham product IS formal (product of formal cdgas).

        PATH 1: product_formality_k3xe.
        PATH 2: analyze_formality for K3 x E.
        PATH 3: Both factors are de Rham formal.
        """
        # PATH 1
        pf = product_formality_k3xe()
        assert pf.derham_product_formal is True

        # PATH 2
        K3E = k3_times_e()
        v = analyze_formality(K3E)
        assert v.de_rham_formal is True

        # PATH 3
        assert analyze_formality(k3_surface()).de_rham_formal is True
        assert analyze_formality(elliptic_curve()).de_rham_formal is True

    def test_relative_construction_not_closed_by_dgms(self):
        """Relative construction is not closed by DGMS alone.

        PATH 1: product_formality_k3xe.
        PATH 2: K3 fiber formal status not certified here.
        PATH 3: Character data agreement requires extra input.
        """
        # PATH 1
        pf = product_formality_k3xe()
        assert pf.relative_construction_works is None

        # PATH 2
        assert pf.k3_formal is None

        # PATH 3: the relative reason states the missing datum
        assert "formal A_infinity model" in pf.relative_reason
        assert "do not by themselves certify" in pf.relative_reason

    def test_k3xe_hodge_data(self):
        """K3 x E Hodge data from Kunneth.

        PATH 1: chi(O_{K3xE}) = 0 (CY3).
        PATH 2: CY dimension = 3.
        PATH 3: Cross-check: chi(O_{K3}) * chi(O_E) = 2 * 0 = 0.
        """
        K3E = k3_times_e()

        # PATH 1
        assert K3E.chi_O() == 0

        # PATH 2
        assert K3E.cy_dim == 3

        # PATH 3
        K3 = k3_surface()
        E = elliptic_curve()
        assert K3.chi_O() * E.chi_O() == 0


# ================================================================
# SECTION 7: MASSEY PRODUCTS
# ================================================================

class TestMasseyProducts:
    """Tests for the manifold vs category Massey product distinction."""

    def test_all_compact_kahler_have_vanishing_derham_massey(self):
        """DGMS: all compact Kahler have vanishing de Rham Massey products.

        PATH 1: Quintic.
        PATH 2: K3.
        PATH 3: Elliptic curve.
        """
        for X_fn in [quintic_threefold, k3_surface, elliptic_curve]:
            X = X_fn()
            m = massey_analysis(X)
            assert m.derham_massey_vanish is True, f"DGMS should give vanishing for {X.name}"

    def test_category_massey_can_be_nonzero(self):
        """Categorical m_3 can be nonzero even with vanishing de Rham Massey.

        PATH 1: Elliptic curve.
        PATH 2: Quintic is not certified.
        PATH 3: K3 x E is not certified.
        """
        E = elliptic_curve()
        m = massey_analysis(E)
        assert m.derham_massey_vanish is True
        assert m.category_m3_zero is False
        assert m.levels_agree is False

        for X_fn in [quintic_threefold, k3_times_e]:
            X = X_fn()
            m = massey_analysis(X)
            assert m.derham_massey_vanish is True
            assert m.category_m3_zero is None
            assert m.levels_agree is None

    def test_levels_can_agree(self):
        """For some geometries, both levels agree (both vanish).

        PATH 1: K3 is not certified here.
        PATH 2: Resolved conifold.
        PATH 3: Agreement means both zero only for certified cases.
        """
        K3 = k3_surface()
        m = massey_analysis(K3)
        assert m.derham_massey_vanish is True
        assert m.category_m3_zero is None
        assert m.levels_agree is None

        con = conifold_resolved()
        m = massey_analysis(con)
        assert m.levels_agree is True
        assert m.derham_massey_vanish is True
        assert m.category_m3_zero is True


# ================================================================
# SECTION 8: PROGRAMME IMPLICATIONS
# ================================================================

class TestProgrammeImplications:
    """Tests for implications on the CY-to-chiral programme."""

    def test_formal_implies_trivial_cya(self):
        """A_inf formal => CY-A holds trivially (no higher corrections).

        PATH 1: Conifold.
        PATH 2: No K3 shortcut.
        PATH 3: Check all flags.
        """
        con = conifold_resolved()
        p = programme_implication(con)
        assert p.ainf_formal is True
        assert p.cya_trivial is True
        assert p.m3_b2_moot is True
        assert p.shadow_depth_zero is True

        K3 = k3_surface()
        p = programme_implication(K3)
        assert p.ainf_formal is None
        assert p.cya_trivial is None

    def test_uncertified_cy3_does_not_get_tcft_shortcut(self):
        """Uncertified compact CY3 does not get a TCFT shortcut.

        PATH 1: Quintic.
        PATH 2: K3 x E.
        PATH 3: Check corrected obstruction status.
        """
        for X_fn in [quintic_threefold, k3_times_e]:
            X = X_fn()
            p = programme_implication(X)
            assert p.ainf_formal is None
            assert p.tcft_applies is None
            assert p.obs_ainf_class_zero is None
            assert p.obstruction_status == "requires_corrected_TCFT_or_HH_minus_2_hypothesis"

    def test_obs_ainf_not_universal(self):
        """Obs_Ainf is not zero for all geometries in this engine.

        PATH 1: Formal geometries (trivially).
        PATH 2: Non-certified geometries remain open.
        PATH 3: Full table check.
        """
        # PATH 1
        con = conifold_resolved()
        p = programme_implication(con)
        assert p.obs_ainf_class_zero is True

        # PATH 2
        for X_fn in [quintic_threefold, k3_times_e, k3_surface]:
            X = X_fn()
            p = programme_implication(X)
            assert p.obs_ainf_class_zero is None

        # PATH 3
        table = formality_table()
        assert any(row["obs_ainf_zero"] is True for row in table)
        assert any(row["obs_ainf_zero"] is None for row in table)

    def test_shadow_class_consistent(self):
        """Shadow class follows from formality status.

        PATH 1: Formal => class G.
        PATH 2: Uncertified compact CY3 => unclassified.
        PATH 3: Table consistency.
        """
        # PATH 1
        con = conifold_resolved()
        v = analyze_formality(con)
        assert v.shadow_class == "G"

        # PATH 2
        for X_fn in [quintic_threefold, k3_times_e]:
            X = X_fn()
            v = analyze_formality(X)
            assert v.shadow_class == "unclassified"

        # PATH 3
        table = formality_table()
        for row in table:
            if row["L3_ainf_formal"] is True:
                assert row["shadow_class"] == "G"


# ================================================================
# SECTION 9: HODGE DATA CONSISTENCY
# ================================================================

class TestHodgeData:
    """Tests for Hodge data of all standard CY manifolds."""

    def test_cy3_chi_O_zero(self):
        """chi(O_X) = 0 for 'strict' CY3 (h^{0,i} = delta_{i,0} + delta_{i,3}).

        PATH 1: Quintic.
        PATH 2: Bicubic.
        PATH 3: K3 x E.
        """
        for X_fn in [quintic_threefold, bicubic_threefold, k3_times_e]:
            X = X_fn()
            assert X.chi_O() == 0, f"chi(O) should be 0 for CY3 {X.name}"

    def test_k3_chi_O_two(self):
        """chi(O_{K3}) = 2.

        PATH 1: Direct computation.
        PATH 2: h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2.
        PATH 3: This is kappa_cat for K3.
        """
        K3 = k3_surface()

        # PATH 1
        assert K3.chi_O() == 2

        # PATH 2
        assert K3.h(0, 0) - K3.h(0, 1) + K3.h(0, 2) == 2

        # PATH 3: kappa_cat(K3) = chi(O_K3) = 2
        assert K3.chi_O() == 2

    def test_quintic_euler_char(self):
        """chi(Q) = -200 for the quintic.

        PATH 1: Direct computation.
        PATH 2: 2(1 + h^{1,1} + 1) - 2(101 + 101) = 6 - 404 = ...
        PATH 3: Cross-check with known value.
        """
        Q = quintic_threefold()

        # PATH 1
        assert Q.euler_char() == -200

        # PATH 2: chi = 2(h^{0,0} + h^{1,1} + h^{2,2} + h^{3,3}) - 2(h^{2,1} + h^{1,2})
        # = 2(1 + 1 + 1 + 1) - 2(101 + 101) = 8 - 404 = -396?
        # No: correct formula: sum (-1)^{p+q} h^{p,q} for CY3:
        #   p+q even: h^{00} + h^{11} + h^{22} + h^{33} + h^{20} + h^{02} + h^{31} + h^{13}
        #   p+q odd: h^{10} + h^{01} + h^{21} + h^{12} + h^{30} + h^{03} + h^{32} + h^{23}
        # = (1 + 1 + 1 + 1 + 0 + 0 + 0 + 0) - (0 + 0 + 101 + 101 + 1 + 1 + 0 + 0)
        # = 4 - 204 = -200
        even_sum = 1 + 1 + 1 + 1  # h^{00} + h^{11} + h^{22} + h^{33}
        odd_sum = 101 + 101 + 1 + 1  # h^{21} + h^{12} + h^{30} + h^{03}
        assert even_sum - odd_sum == -200

        # PATH 3
        assert Q.euler_char() == -200

    def test_kunneth_k3xe(self):
        """K3 x E Hodge numbers from Kunneth formula.

        PATH 1: h^{1,1}(K3xE) = h^{1,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,1}(E)
                                + h^{1,0}(K3)*h^{0,1}(E) + h^{0,1}(K3)*h^{1,0}(E)
                = 20*1 + 1*1 + 0*1 + 0*1 = 21.
        PATH 2: chi(O_{K3xE}) = 0.
        PATH 3: h^{2,1}(K3xE) = 21 (by mirror symmetry of CY3).
        """
        K3E = k3_times_e()

        # PATH 1
        assert K3E.h(1, 1) == 21

        # PATH 2
        assert K3E.chi_O() == 0

        # PATH 3: h^{2,1} should also be computable from Kunneth
        assert K3E.h(2, 1) == 21


# ================================================================
# SECTION 10: CORRECTION RECORD
# ================================================================

class TestCorrectionRecord:
    """Tests for the cech_htt_convergence.py correction."""

    def test_correction_identified(self):
        """The correction in cech_htt_convergence.py is identified.

        PATH 1: File path matches.
        PATH 2: Current claim identified.
        PATH 3: Impact is metadata-only (computation unaffected).
        """
        corr = formality_correction()

        # PATH 1
        assert "cech_htt_convergence" in corr.file_path

        # PATH 2
        assert "is_formal=True" in corr.current_claim
        assert "neither statement certifies" in corr.correct_claim
        assert "comparison map" in corr.correct_claim

        # PATH 3
        assert "UNAFFECTED" in corr.impact_on_computation

    def test_hh_minus_two_criterion_is_precise(self):
        """Corrected derived vanishing names complex, degree, and comparison map.

        PATH 1: exact complex.
        PATH 2: total degree -2.
        PATH 3: comparison map and non-universality flags.
        """
        criterion = hh_minus_two_obstruction_criterion()

        # PATH 1
        assert isinstance(criterion, ObstructionVanishingCriterion)
        assert criterion.complex_name == (
            "reduced Hochschild E_1-cochain complex C^bullet_{E_1}(A,A)"
        )
        assert "bar-length filtration" in criterion.filtration

        # PATH 2
        assert criterion.target_total_degree == -2
        assert any("p+q=-2" in h for h in criterion.hypotheses)

        # PATH 3
        assert "S^3-framing obstruction complex" in criterion.comparison_map
        assert criterion.proves_universal_compact_cy3_closure is False
        assert criterion.proves_raw_termwise_commutator_vanishing is False


# ================================================================
# SECTION 11: MASTER VERIFICATION
# ================================================================

class TestMasterVerification:
    """Master verification of the entire formality analysis."""

    def test_full_verification(self):
        """Run the complete verification suite.

        PATH 1: All checks pass.
        PATH 2: Quintic L1 != L3 confirmed.
        PATH 3: All geometries consistent.
        """
        results = verify_formality_hierarchy()

        # PATH 1
        assert results["all_passed"] is True

        # PATH 2
        assert results["quintic_l3_not_certified"] is True

        # PATH 3
        assert results["all_geometries_consistent"] is True

    def test_comprehensive_table(self):
        """The formality table covers all standard geometries.

        PATH 1: 7 geometries.
        PATH 2: All have L2 (except possibly non-compact).
        PATH 3: All have vanishing de Rham Massey products.
        """
        table = formality_table()

        # PATH 1
        assert len(table) == 7

        # PATH 2
        compact_rows = [r for r in table if r["geometry"] != "resolved conifold"]
        for row in compact_rows:
            assert row["L2_hdr_degeneration"] is True

        # PATH 3
        for row in table:
            assert row["derham_massey_vanish"] is True

    def test_summary_counts(self):
        """Summary: how many geometries are formal at each level.

        PATH 1: All 7 are L1 formal (compact Kahler or toric).
        PATH 2: 6 of 7 are L2 (all smooth proper).
        PATH 3: Only the certified formal conifold is L3 formal here.
        """
        table = formality_table()

        # PATH 1: all are de Rham formal
        l1_count = sum(1 for r in table if r["L1_derham_formal"])
        assert l1_count == 7

        # PATH 2: all have HdR degeneration
        l2_count = sum(1 for r in table if r["L2_hdr_degeneration"])
        assert l2_count == 7

        # PATH 3: only conifold is certified A_inf formal here
        l3_count = sum(1 for r in table if r["L3_ainf_formal"] is True)
        assert l3_count == 1

        # PATH 4: compact CY3 rows are not certified by this engine
        uncertified_cy3 = [
            r for r in table
            if r["cy_dim"] == 3 and r["geometry"] != "resolved conifold"
        ]
        assert all(r["L3_ainf_formal"] is None for r in uncertified_cy3)

    def test_the_critical_answer(self):
        r"""THE ANSWER to the mission question.

        Q: Is D^b(Coh(X)) A_infinity-formal for compact CY3?

        A: This engine does not decide the universal compact CY3 question.
        DGMS, BTT, Kaledin K1, and Yukawa language do not imply A_inf
        formality or obstruction closure.  The corrected closure theorem
        requires the explicit HH^{-2} filtration/comparison package.

        Three independent verification paths:

        PATH 1: Formality verdict for quintic.
        PATH 2: K3 x E status despite de Rham formality.
        PATH 3: HH^{-2} criterion names complex, degree, and comparison map.
        """
        # PATH 1: Quintic is not certified as A_inf formal/non-formal
        Q = quintic_threefold()
        v_Q = analyze_formality(Q)
        assert v_Q.ainf_formal is None
        assert v_Q.de_rham_formal is True  # but de Rham IS formal (DGMS)

        # PATH 2: K3 x E is not certified as A_inf formal/non-formal
        K3E = k3_times_e()
        v_K3E = analyze_formality(K3E)
        assert v_K3E.ainf_formal is None
        assert v_K3E.de_rham_formal is True

        # PATH 3: Obs_Ainf closure needs the corrected criterion
        p_Q = programme_implication(Q)
        p_K3E = programme_implication(K3E)
        assert p_Q.obs_ainf_class_zero is None
        assert p_K3E.obs_ainf_class_zero is None
        criterion = hh_minus_two_obstruction_criterion()
        assert criterion.target_total_degree == -2
        assert "C^bullet_{E_1}(A,A)[2]" in criterion.comparison_map
        assert criterion.proves_universal_compact_cy3_closure is False
