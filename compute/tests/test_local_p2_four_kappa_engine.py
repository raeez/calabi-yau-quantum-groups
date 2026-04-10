r"""
Tests for local_p2_four_kappa_engine.py: four-kappa spectrum of local P^2.

Covers all four kappa invariants, multi-path verification, shadow class
determination, inter-kappa relations, and the comparison table.

AP113 discipline: all kappa references use subscripts throughout.
AP10/HZ-6: every expected value has 2+ independent verification sources.

20+ tests organized by section.
"""

import os
import sys
import importlib.util
from fractions import Fraction

import pytest

F = Fraction

# Load module under test
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'local_p2_four_kappa_engine',
    os.path.join(_lib_dir, 'local_p2_four_kappa_engine.py')
)
eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(eng)


# =========================================================================
# 1. GEOMETRY CONSTANTS
# =========================================================================

class TestGeometryConstants:
    """Verify the topological invariants of P^2."""

    def test_euler_characteristic_p2(self):
        """chi(P^2) = 3.
        # VERIFIED: [DC] Gauss-Bonnet c_2 = 3; [LT] Griffiths-Harris p. 606.
        """
        assert eng.CHI_TOP_P2 == 3

    def test_chi_structure_sheaf(self):
        """chi(O_{P^2}) = 1.
        # VERIFIED: [DC] h^0=1, h^1=0, h^2=0; [LT] HRR (9+3)/12 = 1.
        """
        assert eng.CHI_O_P2 == 1

    def test_betti_numbers(self):
        """Betti numbers of P^2: (1, 0, 1, 0, 1, 0).
        # VERIFIED: [DC] cellular decomposition; [LT] Hatcher Ch. 3.
        """
        assert eng.BETTI_P2 == [1, 0, 1, 0, 1, 0]

    def test_betti_euler_consistency(self):
        """sum (-1)^i b_i = chi_top = 3."""
        alternating = sum((-1)**i * b for i, b in enumerate(eng.BETTI_P2))
        assert alternating == eng.CHI_TOP_P2

    def test_chern_numbers(self):
        """c_1^2 = 9, c_2 = 3 for P^2.
        # VERIFIED: [DC] c_1 = 3H, c_1^2 = 9; [LT] Griffiths-Harris.
        """
        assert eng.C1_SQUARED_P2 == 9
        assert eng.C2_P2 == 3

    def test_self_intersection(self):
        """H.H = 1 on P^2.
        # VERIFIED: [DC] degree of H^2 in H^4; [LT] standard intersection theory.
        """
        assert eng.SELF_INTERSECTION_H == 1


# =========================================================================
# 2. KAPPA_CH
# =========================================================================

class TestKappaCh:
    """Verify kappa_ch = 3/2 via four independent paths."""

    def test_kappa_ch_from_euler_char(self):
        """kappa_ch = chi(P^2)/2 = 3/2.
        # VERIFIED: [DC] 3/2; [LT] Szendroi math/0512556.
        """
        assert eng.kappa_ch_from_euler_char() == F(3, 2)

    def test_kappa_ch_from_chart_gluing(self):
        """kappa_ch = 3 * (1/2) = 3/2 from toric charts.
        # VERIFIED: [DC] 3 charts * 1/2; [CF] matches Euler char path.
        """
        assert eng.kappa_ch_from_chart_gluing() == F(3, 2)

    def test_kappa_ch_from_macmahon(self):
        """kappa_ch = MacMahon exponent / 2 = 3/2.
        # VERIFIED: [DC] exponent 3, divide 2; [LT] MNOP proved for toric.
        """
        assert eng.kappa_ch_from_macmahon_exponent() == F(3, 2)

    def test_kappa_ch_from_gv(self):
        """kappa_ch = 3/2 from genus-1 GV extraction.
        # VERIFIED: [DC] F_1 extraction; [CF] matches all other paths.
        """
        assert eng.kappa_ch_from_gv_genus1() == F(3, 2)

    def test_kappa_ch_four_paths_agree(self):
        """All four paths for kappa_ch yield 3/2."""
        result = eng.kappa_ch_verify_four_paths()
        assert result["all_agree"] is True
        assert result["canonical_value"] == F(3, 2)

    def test_kappa_ch_nonzero(self):
        """kappa_ch != 0 (required for class M)."""
        assert eng.kappa_ch_from_euler_char() != 0

    def test_kappa_ch_positive(self):
        """kappa_ch > 0 for local P^2 (positive chi base)."""
        assert eng.kappa_ch_from_euler_char() > 0


# =========================================================================
# 3. KAPPA_CAT
# =========================================================================

class TestKappaCat:
    """Verify kappa_cat = 1 via three independent paths."""

    def test_kappa_cat_from_structure_sheaf(self):
        """kappa_cat = chi(O_{P^2}) = 1.
        # VERIFIED: [DC] 1-0+0; [LT] standard algebraic geometry.
        """
        assert eng.kappa_cat_from_structure_sheaf() == F(1)

    def test_kappa_cat_from_hrr(self):
        """kappa_cat = (c_1^2 + c_2)/12 = (9+3)/12 = 1.
        # VERIFIED: [DC] arithmetic; [LT] Hirzebruch-Riemann-Roch theorem.
        """
        assert eng.kappa_cat_from_hrr() == F(1)

    def test_kappa_cat_from_todd(self):
        """kappa_cat = integral td(P^2) = 1.
        # VERIFIED: [DC] Todd class computation; [CF] matches HRR path.
        """
        assert eng.kappa_cat_from_todd_class() == F(1)

    def test_kappa_cat_three_paths_agree(self):
        """All three paths for kappa_cat yield 1."""
        result = eng.kappa_cat_verify_three_paths()
        assert result["all_agree"] is True
        assert result["canonical_value"] == F(1)

    def test_kappa_cat_is_integer(self):
        """kappa_cat is always an integer for smooth projective surfaces."""
        val = eng.kappa_cat_from_structure_sheaf()
        assert val.denominator == 1


# =========================================================================
# 4. KAPPA_BKM
# =========================================================================

class TestKappaBKM:
    """Verify kappa_BKM is undefined for local P^2."""

    def test_kappa_bkm_is_none(self):
        """kappa_BKM = None for toric CY3."""
        info = eng.kappa_bkm_status()
        assert info["kappa_BKM"] is None

    def test_kappa_bkm_not_defined(self):
        """kappa_BKM is not defined (no BKM algebra)."""
        info = eng.kappa_bkm_status()
        assert info["defined"] is False

    def test_kappa_bkm_has_obstructions(self):
        """At least 3 obstructions to defining kappa_BKM."""
        info = eng.kappa_bkm_status()
        assert len(info["obstructions"]) >= 3

    def test_kappa_bkm_k3xe_contrast(self):
        """K3 x E has kappa_BKM = 5 (for contrast).
        # VERIFIED: [DC] c(0)/2 = 10/2 = 5; [LT] Gritsenko-Nikulin.
        """
        info = eng.kappa_bkm_status()
        assert info["contrast_k3xe"]["kappa_BKM_k3xe"] == F(5)


# =========================================================================
# 5. KAPPA_FIBER
# =========================================================================

class TestKappaFiber:
    """Verify kappa_fiber = 1 via three independent paths."""

    def test_kappa_fiber_from_intersection(self):
        """kappa_fiber = rank H_2(P^2, Z) = 1.
        # VERIFIED: [DC] b_2(P^2) = 1; [LT] standard topology.
        """
        assert eng.kappa_fiber_from_intersection_form() == F(1)

    def test_kappa_fiber_from_picard(self):
        """kappa_fiber = rho(P^2) = 1.
        # VERIFIED: [DC] Picard rank computation; [CF] matches b_2.
        """
        assert eng.kappa_fiber_from_picard_rank() == F(1)

    def test_kappa_fiber_from_fan(self):
        """kappa_fiber = 3 rays - rank 2 = 1 from toric fan.
        # VERIFIED: [DC] toric geometry; [CF] matches Picard rank.
        """
        assert eng.kappa_fiber_from_fan() == F(1)

    def test_kappa_fiber_three_paths_agree(self):
        """All three paths for kappa_fiber yield 1."""
        result = eng.kappa_fiber_verify_three_paths()
        assert result["all_agree"] is True
        assert result["canonical_value"] == F(1)


# =========================================================================
# 6. SHADOW CLASS
# =========================================================================

class TestShadowClass:
    """Verify shadow depth class M for local P^2."""

    def test_shadow_class_is_M(self):
        """Local P^2 is class M (infinite shadow depth)."""
        assert eng.shadow_class_from_kappa_ch() == "M"

    def test_shadow_evidence_nonzero_delta(self):
        """Discriminant Delta != 0."""
        evidence = eng.shadow_class_evidence()
        assert evidence["Delta_nonzero"] is True

    def test_shadow_chart_lower_bound(self):
        """Chart decomposition gives depth >= 3."""
        evidence = eng.shadow_class_evidence()
        assert evidence["chart_lower_bound"] >= 3

    def test_shadow_r_max_infinite(self):
        """r_max is infinite (None)."""
        evidence = eng.shadow_class_evidence()
        assert evidence["r_max"] is None


# =========================================================================
# 7. FOUR-KAPPA SPECTRUM (INTEGRATION)
# =========================================================================

class TestFourKappaSpectrum:
    """Integration tests for the full spectrum."""

    def test_spectrum_values(self):
        """Four-kappa spectrum has correct values."""
        spec = eng.four_kappa_spectrum()
        assert spec["kappa_ch"] == F(3, 2)
        assert spec["kappa_cat"] == F(1)
        assert spec["kappa_BKM"] is None
        assert spec["kappa_fiber"] == F(1)

    def test_spectrum_tuple(self):
        """Spectrum tuple is (3/2, 1, None, 1)."""
        spec = eng.four_kappa_spectrum()
        assert spec["spectrum_tuple"] == (F(3, 2), F(1), None, F(1))

    def test_spectrum_shadow_class(self):
        """Spectrum includes shadow class M."""
        spec = eng.four_kappa_spectrum()
        assert spec["shadow_class"] == "M"

    def test_spectrum_bkm_undefined(self):
        """Spectrum correctly marks kappa_BKM as undefined."""
        spec = eng.four_kappa_spectrum()
        assert spec["kappa_BKM_defined"] is False

    def test_kappa_ch_not_equal_kappa_cat(self):
        """kappa_ch != kappa_cat (topological vs holomorphic).
        # VERIFIED: [DC] 3/2 != 1; [SY] they measure different things.
        """
        spec = eng.four_kappa_spectrum()
        assert spec["kappa_ch"] != spec["kappa_cat"]

    def test_kappa_cat_equals_kappa_fiber(self):
        """kappa_cat = kappa_fiber = 1 for P^2 (a coincidence).
        # VERIFIED: [DC] both equal 1; [DA] dimensional analysis compatible.
        """
        spec = eng.four_kappa_spectrum()
        assert spec["kappa_cat"] == spec["kappa_fiber"]


# =========================================================================
# 8. INTER-KAPPA RELATIONS
# =========================================================================

class TestKappaRelations:
    """Verify relations between the four kappas."""

    def test_noether_difference(self):
        """kappa_ch - kappa_cat = (5*c_2 - c_1^2)/12 = 1/2 (Noether).
        # VERIFIED: [DC] (15-9)/12 = 1/2; [LT] Noether's formula.
        """
        rel = eng.kappa_relations()
        assert rel["difference_ch_cat"] == F(1, 2)
        assert rel["noether_formula_check"] is True

    def test_cat_fiber_coincidence(self):
        """kappa_cat = kappa_fiber for P^2 (coincidence, not universal)."""
        rel = eng.kappa_relations()
        assert rel["kappa_cat_equals_kappa_fiber"] is True


# =========================================================================
# 9. COMPARISON TABLE
# =========================================================================

class TestComparisonTable:
    """Verify the comparison table across CY3 geometries."""

    def test_table_has_local_p2(self):
        """Table includes local P^2."""
        table = eng.four_kappa_comparison_table()
        names = [row["geometry"] for row in table]
        assert "local P^2" in names

    def test_table_c3_spectrum(self):
        """C^3 has kappa_ch = 1/2, kappa_fiber = 0.
        # VERIFIED: [DC] chi(pt)/2 = 1/2, rank H_2(pt) = 0;
        #           [LT] c3_grand_verification.py.
        """
        table = eng.four_kappa_comparison_table()
        c3 = [r for r in table if r["geometry"] == "C^3"][0]
        assert c3["kappa_ch"] == F(1, 2)
        assert c3["kappa_fiber"] == F(0)

    def test_table_k3xe_bkm(self):
        """K3 x E has kappa_BKM = 5.
        # VERIFIED: [DC] c(0)/2 = 5; [LT] k3e_e1_product_chain.py.
        """
        table = eng.four_kappa_comparison_table()
        k3xe = [r for r in table if r["geometry"] == "K3 x E"][0]
        assert k3xe["kappa_BKM"] == F(5)

    def test_table_spectra_distinct(self):
        """No two geometries share the full four-kappa spectrum."""
        table = eng.four_kappa_comparison_table()
        tuples = [
            (r["kappa_ch"], r["kappa_cat"], r["kappa_BKM"], r["kappa_fiber"])
            for r in table
        ]
        assert len(tuples) == len(set(tuples))


# =========================================================================
# 10. FULL REPORT
# =========================================================================

class TestFullReport:
    """Integration test for the full report."""

    def test_full_report_all_verified(self):
        """Full report passes all verifications."""
        report = eng.full_report()
        assert report["all_verified"] is True

    def test_full_report_has_all_sections(self):
        """Report contains spectrum, verification, class, relations."""
        report = eng.full_report()
        assert "spectrum" in report
        assert "verification" in report
        assert "shadow_class" in report
        assert "relations" in report
        assert "comparison_table" in report
