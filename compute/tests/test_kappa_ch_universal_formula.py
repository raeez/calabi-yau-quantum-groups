#!/usr/bin/env python3
r"""
test_kappa_ch_universal_formula.py -- Tests for the universal kappa_ch formula.

Tests the main result:
  kappa_ch(X) = chi_top(X)/24 + [h^{1,0}(X) > 0] * (h^{3,0}(X) + 2)

for all compact CY_3, plus the abelian surface bug fix and Beauville consistency.

Ground truth:
  chapters/theory/cy_to_chiral.tex (Prop cy-kappa-d2, Thm thm:chi-neq-kappa)
  chapters/connections/bar_cobar_bridge.tex (Grand atlas, Sec sec:grand-atlas)
  chapters/examples/k3_chiral_algebra.tex (kappa-spectrum items i-vii)
  CLAUDE.md (kappa-spectrum table, AP113)
"""

import unittest
from fractions import Fraction

from compute.lib.kappa_ch_universal_formula import (
    CY3Data,
    CY2Data,
    F,
    # CY3 library
    quintic,
    p5_33,
    p5_24,
    p6_223,
    p7_2222,
    bicubic,
    banana,
    bv_1_1_1,
    bv_10_0_0,
    bv_20_2_0,
    k3_times_e,
    enriques_times_e,
    t6_torus,
    c3_affine,
    resolved_conifold,
    local_p2,
    local_p1p1,
    local_f1,
    # CY2 library
    cy2_k3,
    cy2_enriques,
    cy2_abelian,
    # Formulas
    kappa_ch_compact,
    kappa_ch_noncompact,
    kappa_ch,
    kappa_ch_d2,
    # Beauville
    beauville_type,
    # Verification
    verify_formula_vs_beauville,
    verify_all,
    decompose_formula,
    h10_equals_2_impossible,
    # Landscape
    landscape_table,
    all_compact_cy3,
    all_noncompact_cy3,
)


# =========================================================================
# 1. The universal formula: compact strict CY_3 (h^{1,0}=0)
# =========================================================================

class TestUniversalFormulaStrictCY3(unittest.TestCase):
    """Test kappa_ch = chi_top/24 for strict CY_3 (h10=0)."""

    def test_quintic(self):
        """Quintic: kappa = -200/24 = -25/3."""
        self.assertEqual(kappa_ch(quintic()), F(-25, 3))

    def test_p5_33(self):
        """P^5[3,3]: kappa = -144/24 = -6."""
        self.assertEqual(kappa_ch(p5_33()), F(-6))

    def test_p5_24(self):
        """P^5[2,4]: kappa = -176/24 = -22/3."""
        self.assertEqual(kappa_ch(p5_24()), F(-22, 3))

    def test_p6_223(self):
        """P^6[2,2,3]: kappa = -144/24 = -6."""
        self.assertEqual(kappa_ch(p6_223()), F(-6))

    def test_p7_2222(self):
        """P^7[2,2,2,2]: kappa = -128/24 = -16/3."""
        self.assertEqual(kappa_ch(p7_2222()), F(-16, 3))

    def test_bicubic(self):
        """Bicubic P^2xP^2: kappa = -162/24 = -27/4."""
        self.assertEqual(kappa_ch(bicubic()), F(-27, 4))

    def test_banana(self):
        """Banana manifold: kappa = 0/24 = 0."""
        self.assertEqual(kappa_ch(banana()), F(0))

    def test_bv_1_1_1(self):
        """BV(1,1,1): kappa = -108/24 = -9/2."""
        self.assertEqual(kappa_ch(bv_1_1_1()), F(-9, 2))

    def test_bv_10_0_0(self):
        """BV(10,0,0): kappa = 0/24 = 0."""
        self.assertEqual(kappa_ch(bv_10_0_0()), F(0))

    def test_bv_20_2_0(self):
        """BV(20,2,0): kappa = 120/24 = 5."""
        self.assertEqual(kappa_ch(bv_20_2_0()), F(5))


# =========================================================================
# 2. The universal formula: product CY_3 (h^{1,0}>0)
# =========================================================================

class TestUniversalFormulaProductCY3(unittest.TestCase):
    """Test kappa_ch = h^{3,0}+2 for product CY_3 (h10>0)."""

    def test_k3_times_e(self):
        """K3xE: kappa = h30+2 = 1+2 = 3."""
        self.assertEqual(kappa_ch(k3_times_e()), F(3))

    def test_enriques_times_e(self):
        """EnrxE: kappa = h30+2 = 0+2 = 2."""
        self.assertEqual(kappa_ch(enriques_times_e()), F(2))

    def test_t6(self):
        """T^6: kappa = h30+2 = 1+2 = 3."""
        self.assertEqual(kappa_ch(t6_torus()), F(3))


# =========================================================================
# 3. Non-compact CY_3
# =========================================================================

class TestNoncompactCY3(unittest.TestCase):
    """Test kappa_ch for non-compact CY_3 (case-by-case)."""

    def test_c3(self):
        self.assertEqual(kappa_ch(c3_affine()), F(1))

    def test_resolved_conifold(self):
        self.assertEqual(kappa_ch(resolved_conifold()), F(1))

    def test_local_p2(self):
        self.assertEqual(kappa_ch(local_p2()), F(3, 2))

    def test_local_p1p1(self):
        self.assertEqual(kappa_ch(local_p1p1()), F(2))

    def test_local_f1(self):
        self.assertEqual(kappa_ch(local_f1()), F(2))

    def test_compact_rejected_by_noncompact(self):
        """kappa_ch_noncompact rejects compact manifolds."""
        with self.assertRaises(ValueError):
            kappa_ch_noncompact(quintic())

    def test_noncompact_rejected_by_compact(self):
        """kappa_ch_compact rejects non-compact manifolds."""
        with self.assertRaises(ValueError):
            kappa_ch_compact(c3_affine())


# =========================================================================
# 4. Beauville decomposition
# =========================================================================

class TestBeauvilleDecomposition(unittest.TestCase):
    """Test the Beauville type classification."""

    def test_quintic_is_strict(self):
        bt = beauville_type(quintic())
        self.assertEqual(bt.type_name, 'strict_CY3')
        self.assertEqual(bt.kappa_total, F(-25, 3))

    def test_k3xe_decomposition(self):
        bt = beauville_type(k3_times_e())
        self.assertEqual(bt.type_name, 'K3xE')
        self.assertEqual(bt.factors, ['K3', 'E'])
        self.assertEqual(bt.factor_kappas, [F(2), F(1)])
        self.assertEqual(bt.kappa_total, F(3))

    def test_enrxe_decomposition(self):
        bt = beauville_type(enriques_times_e())
        self.assertEqual(bt.type_name, 'EnrxE')
        self.assertEqual(bt.factors, ['Enr', 'E'])
        self.assertEqual(bt.factor_kappas, [F(1), F(1)])
        self.assertEqual(bt.kappa_total, F(2))

    def test_t6_decomposition(self):
        bt = beauville_type(t6_torus())
        self.assertEqual(bt.type_name, 'T6')
        self.assertEqual(bt.factors, ['E', 'E', 'E'])
        self.assertEqual(bt.kappa_total, F(3))

    def test_banana_is_strict(self):
        bt = beauville_type(banana())
        self.assertEqual(bt.type_name, 'strict_CY3')
        self.assertEqual(bt.kappa_total, F(0))


# =========================================================================
# 5. Formula-vs-Beauville consistency
# =========================================================================

class TestFormulaBeauvilleConsistency(unittest.TestCase):
    """The closed formula must agree with Beauville decomposition."""

    def test_all_compact_consistent(self):
        """For every compact CY_3, formula = Beauville sum."""
        for X in all_compact_cy3():
            v = verify_formula_vs_beauville(X)
            self.assertTrue(
                v['consistent'],
                f"Formula inconsistent with Beauville for {X.name}: "
                f"formula={v['formula_value']}, beauville={v['beauville_value']}",
            )

    def test_all_compact_match_known(self):
        """For every compact CY_3, formula = known value."""
        for X in all_compact_cy3():
            formula_val = kappa_ch_compact(X)
            self.assertEqual(
                formula_val, X.kappa_ch_known,
                f"Formula disagrees with known value for {X.name}: "
                f"formula={formula_val}, known={X.kappa_ch_known}",
            )


# =========================================================================
# 6. Abelian surface bug fix
# =========================================================================

class TestAbelianSurfaceBugFix(unittest.TestCase):
    """Test that kappa_ch(Ab) = 2, not chi(O_Ab) = 0."""

    def test_abelian_surface_kappa_is_2(self):
        """kappa_ch(Ab.surf) = 2 (from additivity: kappa(E)+kappa(E))."""
        ab = cy2_abelian()
        self.assertEqual(ab.kappa_ch(), F(2))

    def test_abelian_surface_chi_O_is_0(self):
        """chi(O_Ab) = 0 (which is WRONG for kappa_ch)."""
        ab = cy2_abelian()
        self.assertEqual(ab.chi_O, 0)

    def test_abelian_surface_kappa_ne_chi_O(self):
        """kappa_ch(Ab) != chi(O_Ab): the d=2 formula fails for h10>0."""
        ab = cy2_abelian()
        self.assertNotEqual(ab.kappa_ch(), F(ab.chi_O))

    def test_k3_kappa_equals_chi_O(self):
        """kappa_ch(K3) = chi(O_K3) = 2: d=2 formula holds for h10=0."""
        k3 = cy2_k3()
        self.assertEqual(k3.kappa_ch(), F(k3.chi_O))
        self.assertEqual(k3.kappa_ch(), F(2))

    def test_enriques_kappa_equals_chi_O(self):
        """kappa_ch(Enr) = chi(O_Enr) = 1: d=2 formula holds for h10=0."""
        enr = cy2_enriques()
        self.assertEqual(enr.kappa_ch(), F(enr.chi_O))
        self.assertEqual(enr.kappa_ch(), F(1))


# =========================================================================
# 7. Corrected d=2 formula
# =========================================================================

class TestCorrectedD2Formula(unittest.TestCase):
    """Test the corrected kappa_ch_d2."""

    def test_k3(self):
        """K3 (h10=0, h20=1): kappa = 2."""
        self.assertEqual(kappa_ch_d2(0, 1), F(2))

    def test_enriques(self):
        """Enriques (h10=0, h20=0): kappa = 1."""
        self.assertEqual(kappa_ch_d2(0, 0), F(1))

    def test_abelian_surface(self):
        """Abelian surface (h10=2, h20=1): kappa = 2, NOT 0."""
        self.assertEqual(kappa_ch_d2(2, 1), F(2))

    def test_d2_h10_zero_is_chi_O(self):
        """For h10=0: kappa = chi(O) = 1 + h20."""
        for h20 in range(5):
            self.assertEqual(kappa_ch_d2(0, h20), F(1 + h20))


# =========================================================================
# 8. T^6 consistency
# =========================================================================

class TestT6Consistency(unittest.TestCase):
    """T^6 = E^3 = Ab x E: kappa must be 3 by both decompositions."""

    def test_t6_as_e_cubed(self):
        """T^6 = E x E x E: kappa = 1+1+1 = 3."""
        self.assertEqual(kappa_ch(t6_torus()), F(3))

    def test_t6_as_ab_times_e(self):
        """T^6 = Ab x E: kappa = kappa(Ab)+kappa(E) = 2+1 = 3."""
        ab = cy2_abelian()
        self.assertEqual(ab.kappa_ch() + F(1), F(3))

    def test_two_decompositions_agree(self):
        """Both decompositions give the same result."""
        ab = cy2_abelian()
        three_factor = F(1) + F(1) + F(1)
        two_factor = ab.kappa_ch() + F(1)
        self.assertEqual(three_factor, two_factor)
        self.assertEqual(three_factor, F(3))


# =========================================================================
# 9. h^{1,0}=2 impossibility
# =========================================================================

class TestH10Impossibility(unittest.TestCase):
    """h^{1,0}=2 is impossible for compact CY_3."""

    def test_h10_2_impossible(self):
        r = h10_equals_2_impossible()
        self.assertTrue(r['impossible'])

    def test_allowed_h10_values(self):
        r = h10_equals_2_impossible()
        self.assertEqual(set(r['allowed_h10_values']), {0, 1, 3})

    def test_all_examples_have_allowed_h10(self):
        """Every compact CY_3 in the library has h10 in {0, 1, 3}."""
        for X in all_compact_cy3():
            self.assertIn(X.h10, {0, 1, 3}, f"{X.name} has h10={X.h10}")


# =========================================================================
# 10. Formula decomposition
# =========================================================================

class TestFormulaDecomposition(unittest.TestCase):
    """Test the two-branch decomposition of the formula."""

    def test_strict_cy3_uses_bcov(self):
        """Strict CY_3 (h10=0) uses the BCOV branch."""
        d = decompose_formula(quintic())
        self.assertEqual(d.active_branch, 'BCOV')
        self.assertEqual(d.proof_status, 'CONJECTURAL')
        self.assertEqual(d.kappa_ch, F(-25, 3))

    def test_product_cy3_uses_beauville(self):
        """Product CY_3 (h10>0) uses the Beauville branch."""
        d = decompose_formula(k3_times_e())
        self.assertEqual(d.active_branch, 'Beauville')
        self.assertEqual(d.proof_status, 'PROVED')
        self.assertEqual(d.kappa_ch, F(3))

    def test_enrxe_uses_beauville(self):
        d = decompose_formula(enriques_times_e())
        self.assertEqual(d.active_branch, 'Beauville')
        self.assertEqual(d.proof_status, 'PROVED')
        self.assertEqual(d.kappa_ch, F(2))

    def test_banana_uses_bcov(self):
        d = decompose_formula(banana())
        self.assertEqual(d.active_branch, 'BCOV')
        self.assertEqual(d.kappa_ch, F(0))


# =========================================================================
# 11. Specific numerical checks against manuscript
# =========================================================================

class TestManuscriptValues(unittest.TestCase):
    """Check against values in the manuscript tables."""

    def test_quintic_rational(self):
        """kappa_ch(quintic) = -25/3 is rational, not integer."""
        k = kappa_ch(quintic())
        self.assertEqual(k.numerator, -25)
        self.assertEqual(k.denominator, 3)

    def test_bicubic_rational(self):
        """kappa_ch(bicubic) = -27/4 is rational."""
        k = kappa_ch(bicubic())
        self.assertEqual(k.numerator, -27)
        self.assertEqual(k.denominator, 4)

    def test_bv_interpolation(self):
        """BV(r,a,delta): kappa = (r-10)/2 for the standard BV family."""
        # BV(1,1,1): (1-10)/2 = -9/2
        self.assertEqual(kappa_ch(bv_1_1_1()), F(-9, 2))
        # BV(10,0,0): (10-10)/2 = 0
        self.assertEqual(kappa_ch(bv_10_0_0()), F(0))
        # BV(20,2,0): (20-10)/2 = 5
        self.assertEqual(kappa_ch(bv_20_2_0()), F(5))

    def test_chi_top_vanishes_for_products(self):
        """chi_top = 0 for all product CY_3 (contains E factor)."""
        for X in [k3_times_e(), enriques_times_e(), t6_torus()]:
            self.assertEqual(X.chi_top, 0, f"chi_top should be 0 for {X.name}")

    def test_chi_24_integrality(self):
        """chi/24 integral iff 24 | chi."""
        for X in all_compact_cy3():
            if X.h10 == 0:  # strict CY3
                k = F(X.chi_top, 24)
                is_int = (k.denominator == 1)
                divides = (X.chi_top % 24 == 0)
                self.assertEqual(is_int, divides, f"Integrality check failed for {X.name}")

    def test_k3xe_kappa_spectrum(self):
        """K3xE kappa-spectrum: kappa_ch=3, kappa_cat=0."""
        k3e = k3_times_e()
        self.assertEqual(kappa_ch(k3e), F(3))
        # kappa_cat = chi(O) = 0 for all CY3 (d=3 odd)
        chi_O = sum((-1)**q for q in range(4))  # h^{0,q} = (1,1,1,1) all 1
        self.assertEqual(chi_O, 0)


# =========================================================================
# 12. Master verification
# =========================================================================

class TestMasterVerification(unittest.TestCase):
    """Test the master verification function."""

    def test_verify_all(self):
        r = verify_all()
        self.assertTrue(r['all_compact_pass'])
        self.assertTrue(r['all_noncompact_pass'])
        self.assertTrue(r['abelian_surface_fixed'])
        self.assertTrue(r['k3_d2_correct'])
        self.assertTrue(r['t6_ab_e_consistent'])

    def test_all_compact_match_known(self):
        r = verify_all()
        self.assertTrue(r['all_compact_match_known'])


# =========================================================================
# 13. Landscape table
# =========================================================================

class TestLandscapeTable(unittest.TestCase):
    """Test the landscape table."""

    def test_table_completeness(self):
        table = landscape_table()
        self.assertGreaterEqual(len(table), 18)

    def test_table_names(self):
        table = landscape_table()
        names = {e.name for e in table}
        expected = {
            'Quintic', 'P5[3,3]', 'P5[2,4]', 'P6[2,2,3]', 'P7[2,2,2,2]',
            'Bicubic', 'Banana', 'BV(1,1,1)', 'BV(10,0,0)', 'BV(20,2,0)',
            'K3xE', 'EnrxE', 'T^6',
            'C^3', 'ResCon', 'LocalP2', 'LocalP1P1', 'LocalF1',
        }
        self.assertEqual(names, expected)

    def test_table_values(self):
        table = {e.name: e for e in landscape_table()}
        self.assertEqual(table['Quintic'].kappa_ch, F(-25, 3))
        self.assertEqual(table['Quintic'].label, 'kappa_BCOV_shadow_conjectural')
        self.assertFalse(table['Quintic'].constructed)
        self.assertEqual(table['K3xE'].kappa_ch, F(3))
        self.assertEqual(table['K3xE'].label, 'kappa_ch')
        self.assertTrue(table['K3xE'].constructed)
        self.assertEqual(table['EnrxE'].kappa_ch, F(2))
        self.assertEqual(table['T^6'].kappa_ch, F(3))
        self.assertEqual(table['C^3'].kappa_ch, F(1))
        self.assertEqual(table['LocalP2'].kappa_ch, F(3, 2))


# =========================================================================
# 14. Additivity cross-checks
# =========================================================================

class TestAdditivity(unittest.TestCase):
    """Cross-check additivity with Beauville decomposition."""

    def test_k3xe_additivity(self):
        """kappa(K3xE) = kappa(K3) + kappa(E) = 2+1 = 3."""
        k3 = cy2_k3()
        self.assertEqual(k3.kappa_ch() + F(1), kappa_ch(k3_times_e()))

    def test_enrxe_additivity(self):
        """kappa(EnrxE) = kappa(Enr) + kappa(E) = 1+1 = 2."""
        enr = cy2_enriques()
        self.assertEqual(enr.kappa_ch() + F(1), kappa_ch(enriques_times_e()))

    def test_t6_additivity_three_factor(self):
        """kappa(T^6) = 3*kappa(E) = 3."""
        self.assertEqual(F(3) * F(1), kappa_ch(t6_torus()))

    def test_t6_additivity_two_factor(self):
        """kappa(T^6) = kappa(Ab) + kappa(E) = 2+1 = 3."""
        ab = cy2_abelian()
        self.assertEqual(ab.kappa_ch() + F(1), kappa_ch(t6_torus()))


# =========================================================================
# 15. Edge cases and error handling
# =========================================================================

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def test_noncompact_raises_for_compact_formula(self):
        with self.assertRaises(ValueError):
            kappa_ch_compact(c3_affine())

    def test_compact_raises_for_noncompact_formula(self):
        with self.assertRaises(ValueError):
            kappa_ch_noncompact(quintic())

    def test_beauville_rejects_noncompact(self):
        with self.assertRaises(ValueError):
            beauville_type(c3_affine())

    def test_kappa_ch_dispatches_correctly(self):
        """kappa_ch dispatches to correct formula based on compactness."""
        with self.assertRaises(NotImplementedError):
            kappa_ch(quintic())
        self.assertEqual(kappa_ch(k3_times_e()), kappa_ch_compact(k3_times_e()))
        self.assertEqual(kappa_ch(c3_affine()), kappa_ch_noncompact(c3_affine()))


if __name__ == "__main__":
    unittest.main()
