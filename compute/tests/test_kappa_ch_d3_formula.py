#!/usr/bin/env python3
r"""
test_kappa_ch_d3_formula.py -- Tests for the corrected CY-D formula.

Tests the resolution of the CY-D inconsistency: kappa_ch != chi(O_X) at d != 2.

Ground truth:
  chapters/theory/cy_to_chiral.tex  (Proposition prop:cy-kappa-d2: d=2 PROVED)
  chapters/examples/k3_chiral_algebra.tex  (kappa-spectrum, items i-vii)
  chapters/theory/cy_to_chiral.tex  (Theorem thm:kappa-c3: C^3 PROVED)
  chapters/theory/cy_to_chiral.tex  (atlas table: landscape of kappa_ch values)
  CLAUDE.md  (kappa-spectrum, AP113: bare kappa FORBIDDEN)
"""

import unittest
from fractions import Fraction

from compute.lib.kappa_ch_d3_formula import (
    CYHodgeData,
    QuantumCorrection,
    point,
    elliptic_curve,
    abelian_surface,
    k3_surface,
    enriques_surface,
    k3_times_e,
    enriques_times_e,
    quintic_threefold,
    c3_affine,
    resolved_conifold,
    local_p2,
    local_p1p1,
    t6_abelian,
    kappa_cat,
    kappa_ch,
    quantum_correction,
    verify_cyd_refutation,
    cyd_status_table,
    kappa_ch_landscape,
    additivity_vs_multiplicativity,
    verify_all,
)


class TestCYDRefutation(unittest.TestCase):
    """Test that CY-D (kappa_ch = chi(O_X)) is refuted at d != 2."""

    def test_cyd_refuted_at_d1(self):
        """kappa_ch(E) = 1 != 0 = chi(O_E)."""
        e = elliptic_curve()
        self.assertEqual(kappa_ch(e), Fraction(1))
        self.assertEqual(kappa_cat(e), 0)
        self.assertNotEqual(kappa_ch(e), Fraction(kappa_cat(e)))

    def test_cyd_holds_at_d2_k3(self):
        """kappa_ch(K3) = 2 = chi(O_K3). PROVED."""
        k3 = k3_surface()
        self.assertEqual(kappa_ch(k3), Fraction(2))
        self.assertEqual(kappa_cat(k3), 2)
        self.assertEqual(kappa_ch(k3), Fraction(kappa_cat(k3)))

    def test_cyd_holds_at_d2_t4(self):
        """kappa_ch(T^4) = 0 = chi(O_{T^4}). PROVED."""
        t4 = abelian_surface()
        self.assertEqual(kappa_ch(t4), Fraction(0))
        self.assertEqual(kappa_cat(t4), 0)
        self.assertEqual(kappa_ch(t4), Fraction(kappa_cat(t4)))

    def test_cyd_holds_at_d2_enriques(self):
        """kappa_ch(Enr) = 1 = chi(O_Enr). PROVED."""
        enr = enriques_surface()
        self.assertEqual(kappa_ch(enr), Fraction(1))
        self.assertEqual(kappa_cat(enr), 1)

    def test_cyd_refuted_at_d3_k3xe(self):
        """kappa_ch(K3xE) = 3 != 0 = chi(O_{K3xE})."""
        k3e = k3_times_e()
        self.assertEqual(kappa_ch(k3e), Fraction(3))
        self.assertEqual(kappa_cat(k3e), 0)
        self.assertNotEqual(kappa_ch(k3e), Fraction(kappa_cat(k3e)))

    def test_cyd_refuted_at_d3_quintic(self):
        """kappa_ch(Quintic) = -25/3 != 0 = chi(O_Quintic)."""
        q = quintic_threefold()
        self.assertEqual(kappa_ch(q), Fraction(-25, 3))
        self.assertEqual(kappa_cat(q), 0)
        self.assertNotEqual(kappa_ch(q), Fraction(kappa_cat(q)))

    def test_chi_O_vanishes_for_all_strict_CY3(self):
        """For ANY strict CY3 with d odd: chi(O_X) = 0."""
        for X in [quintic_threefold(), k3_times_e(), t6_abelian()]:
            self.assertEqual(X.chi_O(), 0, f"chi(O) should be 0 for {X.name}")


class TestKappaCHValues(unittest.TestCase):
    """Test all known kappa_ch values."""

    def test_point(self):
        self.assertEqual(kappa_ch(point()), Fraction(0))

    def test_elliptic_curve(self):
        self.assertEqual(kappa_ch(elliptic_curve()), Fraction(1))

    def test_k3(self):
        self.assertEqual(kappa_ch(k3_surface()), Fraction(2))

    def test_abelian_surface(self):
        self.assertEqual(kappa_ch(abelian_surface()), Fraction(0))

    def test_enriques(self):
        self.assertEqual(kappa_ch(enriques_surface()), Fraction(1))

    def test_c3(self):
        self.assertEqual(kappa_ch(c3_affine()), Fraction(1))

    def test_resolved_conifold(self):
        self.assertEqual(kappa_ch(resolved_conifold()), Fraction(1))

    def test_local_p2(self):
        self.assertEqual(kappa_ch(local_p2()), Fraction(3, 2))

    def test_local_p1p1(self):
        self.assertEqual(kappa_ch(local_p1p1()), Fraction(2))

    def test_k3_times_e(self):
        self.assertEqual(kappa_ch(k3_times_e()), Fraction(3))

    def test_enriques_times_e(self):
        self.assertEqual(kappa_ch(enriques_times_e()), Fraction(2))

    def test_quintic(self):
        self.assertEqual(kappa_ch(quintic_threefold()), Fraction(-25, 3))

    def test_t6(self):
        self.assertEqual(kappa_ch(t6_abelian()), Fraction(3))


class TestAdditivity(unittest.TestCase):
    """Test that kappa_ch is additive under products."""

    def test_k3_times_e_additivity(self):
        """kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3."""
        k3 = k3_surface()
        e = elliptic_curve()
        k3e = k3_times_e()
        self.assertEqual(
            kappa_ch(k3e),
            kappa_ch(k3) + kappa_ch(e),
        )

    def test_enriques_times_e_additivity(self):
        """kappa_ch(Enr x E) = kappa_ch(Enr) + kappa_ch(E) = 1 + 1 = 2."""
        enr = enriques_surface()
        e = elliptic_curve()
        enre = enriques_times_e()
        self.assertEqual(
            kappa_ch(enre),
            kappa_ch(enr) + kappa_ch(e),
        )


class TestMultiplicativity(unittest.TestCase):
    """Test that chi(O_X) is multiplicative under products (Kunneth)."""

    def test_k3_times_e_multiplicativity(self):
        """chi(O_{K3xE}) = chi(O_K3) * chi(O_E) = 2 * 0 = 0."""
        k3 = k3_surface()
        e = elliptic_curve()
        k3e = k3_times_e()
        self.assertEqual(
            kappa_cat(k3e),
            kappa_cat(k3) * kappa_cat(e),
        )

    def test_additivity_multiplicativity_clash(self):
        """The additive kappa_ch != the multiplicative chi(O) for K3xE."""
        k3 = k3_surface()
        e = elliptic_curve()
        additive_value = kappa_ch(k3) + kappa_ch(e)      # 3
        multiplicative_value = kappa_cat(k3) * kappa_cat(e)  # 0
        self.assertNotEqual(additive_value, Fraction(multiplicative_value))


class TestQuantumCorrection(unittest.TestCase):
    """Test the quantum correction delta_kappa = kappa_ch - chi(O_X)."""

    def test_delta_vanishes_at_d2(self):
        """At d=2: delta_kappa = 0 (Serre duality kills it)."""
        for X in [k3_surface(), abelian_surface(), enriques_surface()]:
            qc = quantum_correction(X)
            self.assertEqual(qc.delta_kappa, Fraction(0), f"delta should be 0 for {X.name}")
            self.assertTrue(qc.delta_vanishes)

    def test_delta_nonzero_at_d1(self):
        """At d=1: delta_kappa = 1 for E."""
        qc = quantum_correction(elliptic_curve())
        self.assertEqual(qc.delta_kappa, Fraction(1))
        self.assertFalse(qc.delta_vanishes)

    def test_delta_nonzero_at_d3_k3xe(self):
        """At d=3: delta_kappa = 3 for K3xE."""
        qc = quantum_correction(k3_times_e())
        self.assertEqual(qc.delta_kappa, Fraction(3))
        self.assertFalse(qc.delta_vanishes)

    def test_delta_nonzero_at_d3_quintic(self):
        """At d=3: delta_kappa = -25/3 for quintic."""
        qc = quantum_correction(quintic_threefold())
        self.assertEqual(qc.delta_kappa, Fraction(-25, 3))
        self.assertFalse(qc.delta_vanishes)

    def test_delta_for_c3(self):
        """C^3 is non-compact; chi(O) is computed from h^{0,0}=1 only."""
        qc = quantum_correction(c3_affine())
        # chi(O) = 1 (only h^{0,0}=1), kappa_ch = 1, delta = 0
        self.assertEqual(qc.chi_O, 1)
        self.assertEqual(qc.kappa_ch, Fraction(1))
        self.assertEqual(qc.delta_kappa, Fraction(0))


class TestHodgeData(unittest.TestCase):
    """Test Hodge data for standard manifolds."""

    def test_chi_O_elliptic(self):
        """chi(O_E) = 1 - 1 = 0."""
        self.assertEqual(elliptic_curve().chi_O(), 0)

    def test_chi_O_k3(self):
        """chi(O_K3) = 1 - 0 + 1 = 2."""
        self.assertEqual(k3_surface().chi_O(), 2)

    def test_chi_O_k3xe(self):
        """chi(O_{K3xE}) = 1 - 1 + 1 - 1 = 0."""
        self.assertEqual(k3_times_e().chi_O(), 0)

    def test_chi_O_quintic(self):
        """chi(O_Quintic) = 1 - 0 + 0 - 1 = 0."""
        self.assertEqual(quintic_threefold().chi_O(), 0)

    def test_chi_O_t4(self):
        """chi(O_{T^4}) = 1 - 2 + 1 = 0."""
        self.assertEqual(abelian_surface().chi_O(), 0)

    def test_chi_O_t6(self):
        """chi(O_{T^6}) = 1 - 3 + 3 - 1 = 0."""
        self.assertEqual(t6_abelian().chi_O(), 0)

    def test_chi_O_point(self):
        """chi(O_pt) = 1."""
        self.assertEqual(point().chi_O(), 1)


class TestDimensionStratification(unittest.TestCase):
    """Test the dimension-stratified formula."""

    def test_d0(self):
        """d=0: kappa_ch = 0."""
        self.assertEqual(kappa_ch(point()), Fraction(0))

    def test_d1_formula(self):
        """d=1: kappa_ch = h^{1,0}."""
        e = elliptic_curve()
        self.assertEqual(kappa_ch(e), Fraction(e.h0q[1]))

    def test_d2_formula(self):
        """d=2: kappa_ch = chi(O_X)."""
        for X in [k3_surface(), abelian_surface(), enriques_surface()]:
            self.assertEqual(kappa_ch(X), Fraction(X.chi_O()))

    def test_d3_bcov_formula(self):
        """d=3 compact h^{1,0}=0: kappa_ch = chi_top/24."""
        q = quintic_threefold()
        self.assertEqual(kappa_ch(q), Fraction(q.chi_top, 24))

    def test_d3_product_formula(self):
        """d=3 product: kappa_ch = kappa_ch(factor1) + kappa_ch(factor2)."""
        k3e = k3_times_e()
        self.assertEqual(kappa_ch(k3e), Fraction(3))

    def test_d3_local_surface_formula(self):
        """d=3 local surface: kappa_ch = chi_top(base)/2."""
        lp2 = local_p2()
        self.assertEqual(kappa_ch(lp2), Fraction(3, 2))

    def test_d3_c3(self):
        """d=3 C^3: kappa_ch = 1."""
        self.assertEqual(kappa_ch(c3_affine()), Fraction(1))


class TestCYDStatusTable(unittest.TestCase):
    """Test the CY-D status table."""

    def test_table_completeness(self):
        """Status table covers dimensions 0-3."""
        table = cyd_status_table()
        self.assertIn(0, table)
        self.assertIn(1, table)
        self.assertIn(2, table)
        self.assertIn(3, table)

    def test_d2_proved(self):
        """d=2 is the only PROVED case."""
        table = cyd_status_table()
        self.assertEqual(table[2].status, "PROVED")

    def test_d3_conjectural(self):
        """d=3 is conjectural (except for specific proved cases)."""
        table = cyd_status_table()
        self.assertIn("CONJECTURAL", table[3].status)


class TestLandscapeTable(unittest.TestCase):
    """Test the complete landscape table."""

    def test_landscape_has_all_manifolds(self):
        """The landscape covers all standard manifolds."""
        table = kappa_ch_landscape()
        names = {e.name for e in table}
        expected = {
            "point", "E", "T^4", "K3", "Enr",
            "C^3", "ResCon", "LocalP2", "LocalP1P1",
            "K3xE", "EnrxE", "Quintic", "T^6",
        }
        self.assertEqual(names, expected)

    def test_landscape_kappa_values(self):
        """Spot-check kappa_ch values in the landscape."""
        table = {e.name: e for e in kappa_ch_landscape()}
        self.assertEqual(table["E"].kappa_ch, Fraction(1))
        self.assertEqual(table["K3"].kappa_ch, Fraction(2))
        self.assertEqual(table["K3xE"].kappa_ch, Fraction(3))
        self.assertEqual(table["Quintic"].kappa_ch, Fraction(-25, 3))
        self.assertEqual(table["C^3"].kappa_ch, Fraction(1))
        self.assertEqual(table["LocalP2"].kappa_ch, Fraction(3, 2))

    def test_landscape_delta_at_d2(self):
        """All d=2 entries have delta = 0."""
        table = kappa_ch_landscape()
        for e in table:
            if e.dim_C == 2:
                self.assertEqual(
                    e.delta_kappa, Fraction(0),
                    f"delta should be 0 for {e.name} at d=2",
                )

    def test_landscape_delta_at_d3_nonzero(self):
        """Most d=3 entries have delta != 0."""
        table = {e.name: e for e in kappa_ch_landscape()}
        self.assertNotEqual(table["K3xE"].delta_kappa, Fraction(0))
        self.assertNotEqual(table["Quintic"].delta_kappa, Fraction(0))


class TestAdditivityVsMultiplicativity(unittest.TestCase):
    """Test the additivity vs multiplicativity analysis."""

    def test_k3xe_analysis(self):
        result = additivity_vs_multiplicativity()
        k3xe = result["K3xE"]
        self.assertEqual(k3xe["kappa_ch_additive"], Fraction(3))
        self.assertEqual(k3xe["chi_O_multiplicative"], 0)
        self.assertTrue(k3xe["additivity_holds"])
        self.assertTrue(k3xe["multiplicativity_holds"])
        self.assertTrue(k3xe["clash"])

    def test_t4xe_hypothetical(self):
        result = additivity_vs_multiplicativity()
        t4xe = result["T4xE_hypothetical"]
        self.assertEqual(t4xe["kappa_ch_predicted"], Fraction(1))
        self.assertEqual(t4xe["chi_O_predicted"], 0)
        self.assertTrue(t4xe["clash"])


class TestMasterVerification(unittest.TestCase):
    """Test the master verification function."""

    def test_verify_all_runs(self):
        """verify_all() completes without error."""
        results = verify_all()
        self.assertIn("cyd_refutation", results)
        self.assertIn("landscape", results)
        self.assertIn("add_vs_mult", results)
        self.assertIn("status_table", results)
        self.assertIn("quantum_corrections", results)
        self.assertIn("numerical_checks", results)

    def test_all_numerical_checks_pass(self):
        """All numerical checks in verify_all() are True."""
        results = verify_all()
        for key, value in results["numerical_checks"].items():
            self.assertTrue(value, f"Numerical check {key} failed")

    def test_cyd_refutation_consistent(self):
        """The CY-D refutation data is internally consistent."""
        results = verify_all()
        ref = results["cyd_refutation"]
        self.assertTrue(ref["E_refutes_CYD"])
        self.assertTrue(ref["K3_CYD_holds"])
        self.assertTrue(ref["T4_CYD_holds"])
        self.assertTrue(ref["K3xE_refutes_CYD"])
        self.assertTrue(ref["Quintic_refutes_CYD"])
        self.assertTrue(ref["additivity_test"])
        self.assertTrue(ref["multiplicativity_test"])
        self.assertTrue(ref["clash"])


class TestSpecificNumerics(unittest.TestCase):
    """Specific numerical checks against manuscript values."""

    def test_k3xe_kappa_spectrum(self):
        """The K3xE kappa-spectrum is {0, 2, 3, 5, 24}."""
        k3e = k3_times_e()
        k3 = k3_surface()
        self.assertEqual(kappa_cat(k3e), 0)
        self.assertEqual(kappa_cat(k3), 2)
        self.assertEqual(int(kappa_ch(k3e)), 3)
        # kappa_BKM = 5, kappa_fiber = 24 are tested in kappa_spectrum_reconciliation

    def test_quintic_kappa_ch_rational(self):
        """kappa_ch(Quintic) = -25/3 is rational, not integer."""
        q = quintic_threefold()
        k = kappa_ch(q)
        self.assertEqual(k.numerator, -25)
        self.assertEqual(k.denominator, 3)

    def test_quintic_chi_top_over_24(self):
        """kappa_ch(Quintic) = chi_top/24 = -200/24 = -25/3."""
        q = quintic_threefold()
        self.assertEqual(kappa_ch(q), Fraction(-200, 24))

    def test_local_p2_chi_top_over_2(self):
        """kappa_ch(LocalP2) = chi_top(P^2)/2 = 3/2."""
        lp2 = local_p2()
        self.assertEqual(kappa_ch(lp2), Fraction(3, 2))

    def test_k3xe_additivity_decomposition(self):
        """kappa_ch(K3xE) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3."""
        self.assertEqual(kappa_ch(k3_surface()), Fraction(2))
        self.assertEqual(kappa_ch(elliptic_curve()), Fraction(1))
        self.assertEqual(kappa_ch(k3_times_e()), Fraction(3))

    def test_enrxe_additivity_decomposition(self):
        """kappa_ch(EnrxE) = kappa_ch(Enr) + kappa_ch(E) = 1 + 1 = 2."""
        self.assertEqual(kappa_ch(enriques_surface()), Fraction(1))
        self.assertEqual(kappa_ch(enriques_times_e()), Fraction(2))

    def test_t6_kappa_ch(self):
        """kappa_ch(T^6) = 3 (from 3 copies of E, each contributing 1)."""
        self.assertEqual(kappa_ch(t6_abelian()), Fraction(3))

    def test_c3_five_paths(self):
        """kappa_ch(C^3) = 1 (proved by five paths)."""
        self.assertEqual(kappa_ch(c3_affine()), Fraction(1))


class TestCYDProofAtD2(unittest.TestCase):
    """Verify the d=2 case is genuinely proved."""

    def test_k3_serre_duality_mechanism(self):
        """At d=2: S_C=[2] kills the quantum correction."""
        k3 = k3_surface()
        qc = quantum_correction(k3)
        self.assertEqual(qc.delta_kappa, Fraction(0))
        self.assertIn("Serre duality", qc.mechanism)

    def test_all_d2_manifolds_agree(self):
        """All d=2 manifolds satisfy kappa_ch = chi(O_X)."""
        for X in [k3_surface(), abelian_surface(), enriques_surface()]:
            self.assertEqual(
                kappa_ch(X), Fraction(X.chi_O()),
                f"CY-D should hold for {X.name} at d=2",
            )


class TestNonCompactCases(unittest.TestCase):
    """Test non-compact CY3 cases where chi(O_X) is not well-defined."""

    def test_c3_kappa_ch(self):
        """C^3: kappa_ch = 1 from MacMahon/Heisenberg."""
        self.assertEqual(kappa_ch(c3_affine()), Fraction(1))

    def test_resolved_conifold_kappa_ch(self):
        """Resolved conifold: kappa_ch = 1 from single BPS cycle."""
        self.assertEqual(kappa_ch(resolved_conifold()), Fraction(1))

    def test_local_p2_kappa_ch(self):
        """Local P^2: kappa_ch = 3/2 from chi_top(P^2)/2."""
        self.assertEqual(kappa_ch(local_p2()), Fraction(3, 2))

    def test_local_p1p1_kappa_ch(self):
        """Local P^1xP^1: kappa_ch = 2 from chi_top(P^1xP^1)/2."""
        self.assertEqual(kappa_ch(local_p1p1()), Fraction(2))


if __name__ == "__main__":
    unittest.main()
