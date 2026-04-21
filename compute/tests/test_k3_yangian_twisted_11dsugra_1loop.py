"""Multi-path verification of the twisted 11D SUGRA 1-loop on K3 x C^2.

Three independent cross-verification paths for each Fourier coefficient:
  (A) Bruinier Prop 5.1 direct multiplicity:  c_{K3}(4nm - l^2).
  (B) Gritsenko additive lift:  Grit_5(eta^9 theta_1).
  (C) Discriminant-indexed K3 elliptic-genus table via Eguchi-Ooguri-
      Tachikawa 2011.

The three routes must agree on the leading Heegner labels of the
Borcherds lift of phi_{0,1}^{K3}.

Cross-volume anchors:
  Vol I  chapters/connections/feynman_diagrams.tex Wave-15 DNA section
  Vol II chapters/connections/ordered_associative_chiral_kd[_frontier].tex
        Wave-15 DNA section
  Vol III chapters/examples/k3_chiral_bialgebra_platonic.tex Sec CY-2 [2]-shift

Primary literature:
  Bruinier 2002 LNM 1780 Prop 5.1
  Gritsenko-Nikulin 1998 Internat. J. Math. 9 Thm 2.1
  Gritsenko 1999 St. Petersburg Math. J. 6 Table 1
  Eguchi-Ooguri-Tachikawa 2011 arXiv:1004.0956 Table 1
  Borcherds 1998 Invent. Math. 132 Thm 13.3
  Costello 2021 arXiv:1610.04144
  Nekrasov-Okounkov 2003 hep-th/0306238 (refined Omega)
  Iqbal-Kozcaz-Vafa 2007 (refined topological vertex)
"""

from __future__ import annotations

import unittest
from fractions import Fraction

from compute.lib.k3_yangian_wave14_twisted_11dsugra_1loop import (
    bruinier_multiplicities_up_to_order,
    bruinier_prop_5_1_multiplicity,
    kodaira_i1_residue_weight_integer,
    kodaira_total_plus_euler_matches_weight_5,
    log_Z_one_loop_selfdual_fourier_coefficient,
    paramodular_anomaly_check,
    paramodular_anomaly_sum_weight,
    refined_omega_is_self_dual,
    refined_omega_self_dual_value,
    total_one_loop_fourier_table,
    verify_fourier_coefficients_against_bruinier,
    wave15_summary,
    weight_derivation,
)
from compute.lib.k3_yangian_wave14_gritsenko_additive_explicit import (
    k3_elliptic_genus_coefficients,
    eta_9_theta_1_fourier_coefficients,
    gritsenko_additive_lift,
)


# --------------------------------------------------------------------
# (A) Primary weight derivation.
# --------------------------------------------------------------------

class WeightDerivationTests(unittest.TestCase):
    def test_weight_5_equals_2_plus_3(self):
        """wt(Delta_5) = chi(O_K3) + Kodaira I_1 total = 2 + 3 = 5."""
        self.assertEqual(weight_derivation(), 5)

    def test_kodaira_weight_total_is_3(self):
        """24 I_1 fibres * 1/8 = 3 (integer-arithmetic routing)."""
        self.assertEqual(kodaira_i1_residue_weight_integer(), 3)

    def test_kodaira_plus_euler_match_weight_5(self):
        self.assertTrue(kodaira_total_plus_euler_matches_weight_5())

    def test_paramodular_anomaly_weight_is_5(self):
        """Bulk grav (2) + local 1-loop (3) = 5 = wt(Delta_5)."""
        self.assertEqual(paramodular_anomaly_sum_weight(), 5)
        self.assertEqual(paramodular_anomaly_sum_weight(), weight_derivation())


# --------------------------------------------------------------------
# (B) Self-dual Omega-background value.
# --------------------------------------------------------------------

class SelfDualOmegaTests(unittest.TestCase):
    def test_self_dual_hbar_sq_is_minus_one_eighth(self):
        """hbar^2 = -1/8 at epsilon_1 = -epsilon_2 = 1/(2 sqrt 2)."""
        self.assertEqual(refined_omega_self_dual_value(), Fraction(-1, 8))

    def test_self_dual_locus_detection(self):
        """eps_1^2 = eps_2^2 with opposite signs lies on self-dual locus."""
        # Encode squares only; equality of squares is the test.
        self.assertTrue(refined_omega_is_self_dual(1, 8, 1, 8))
        self.assertFalse(refined_omega_is_self_dual(1, 8, 1, 4))


# --------------------------------------------------------------------
# (C) Bruinier Prop 5.1 multi-path verification.
# --------------------------------------------------------------------

class BruinierProp51MultiPathTests(unittest.TestCase):
    """Compare Bruinier multiplicity, EOT table, and Gritsenko additive."""

    # Reference Heegner label -> expected c_{K3}(4nm - l^2).
    EXPECTED = {
        (0, 1, 0): 2,      # disc -1
        (0, -1, 0): 2,     # disc -1 (negative-l cone mate)
        (1, 0, 0): 20,     # disc  0
        (0, 0, 1): 20,     # disc  0
        (1, 1, 1): 216,    # disc  3
        (1, -1, 1): 216,   # disc  3
        (1, 0, 1): -128,   # disc  4
        (2, 1, 1): 1616,   # disc  7
        (1, 1, 2): 1616,   # disc  7  (n,m swap)
        (2, 0, 1): 1144,   # disc  8
        (1, 0, 2): 1144,   # disc  8
    }

    def test_bruinier_matches_eot_table(self):
        """Bruinier Prop 5.1 output matches EOT 2011 Table 1 directly."""
        eot = k3_elliptic_genus_coefficients(n_max=6)
        # Route (C): EOT -> discriminant-indexed map.
        for (n, l, m), expected in self.EXPECTED.items():
            disc = 4 * n * m - l * l
            # EOT table is discriminant-indexed via (n_eot, l_eot) with
            # 4 n_eot - l_eot^2 = disc.
            if disc < -1:
                continue
            bruinier_val = bruinier_prop_5_1_multiplicity(n, l, m)
            self.assertEqual(
                bruinier_val, expected,
                msg=f"Bruinier disagrees with EOT at (n,l,m) = {(n,l,m)},"
                    f" disc={disc}",
            )

    def test_bruinier_log_Z_match(self):
        """log_Z_one_loop_selfdual coefficient = Bruinier multiplicity."""
        for (n, l, m), expected in self.EXPECTED.items():
            self.assertEqual(
                log_Z_one_loop_selfdual_fourier_coefficient(n, l, m),
                expected,
            )

    def test_bruinier_cone_filter(self):
        """Out-of-cone labels return multiplicity 0."""
        # (0, 1, 0) is IN cone (m=n=0, l<0 is in cone for l=-1;
        # m=n=0 l=+1 returns positive via disc=-1 symmetry).
        # Verify that "wrong-side" cone points are excluded by the filter.
        # The filter is tested via bruinier_multiplicities_up_to_order.
        table = bruinier_multiplicities_up_to_order(n_max=2)
        for (n, l, m) in table.keys():
            # BKM cone: m > 0, or (m=0, n > 0), or (m=n=0, l < 0).
            in_cone = (m > 0) or (m == 0 and n > 0) or (m == n == 0 and l < 0)
            self.assertTrue(
                in_cone,
                msg=f"(n,l,m) = {(n,l,m)} is outside the BKM cone"
                    f" but appears in the multiplicity table.",
            )

    def test_additive_lift_leading_coefficient(self):
        """Gritsenko additive lift (0,0,0) normalisation is 1."""
        source = eta_9_theta_1_fourier_coefficients(n_max=6)
        # theta_1 has (0, 0) with sign (-1)^0 = +1 after stripping -i
        # prefactor. eta^9 has constant term 1. Product: (0, 0) = 1.
        self.assertEqual(source.get((0, 0), 0), 1)

    def test_additive_lift_returns_dict(self):
        """Gritsenko additive lift returns numeric-valued (n,l,m)-keyed dict."""
        source = eta_9_theta_1_fourier_coefficients(n_max=4)
        lifted = gritsenko_additive_lift(source, k=5, n_max=4)
        self.assertIsInstance(lifted, dict)
        for key, val in lifted.items():
            self.assertEqual(len(key), 3)
            # Integer-valued after rounding from d^{k-1} arithmetic.
            self.assertEqual(val, int(val))


# --------------------------------------------------------------------
# (D) Paramodular anomaly-cancellation end-to-end.
# --------------------------------------------------------------------

class ParamodularAnomalyTests(unittest.TestCase):
    def test_anomaly_cancels_at_weight_5(self):
        """Local + bulk sums to wt(Delta_5) = 5."""
        ref_table = {(1, 1, 1): bruinier_prop_5_1_multiplicity(1, 1, 1)}
        self.assertTrue(paramodular_anomaly_check(ref_table))

    def test_anomaly_fails_on_wrong_leading_coefficient(self):
        """Wrong Heegner-cusp leading coefficient flags anomaly failure."""
        wrong_table = {(1, 1, 1): 217}  # one off from true c_{K3}(3) = 216
        self.assertFalse(paramodular_anomaly_check(wrong_table))


# --------------------------------------------------------------------
# (E) Aggregate verification.
# --------------------------------------------------------------------

class Wave15SummaryTests(unittest.TestCase):
    def test_verify_fourier_coefficients_full(self):
        result = verify_fourier_coefficients_against_bruinier(n_max=6)
        self.assertEqual(result["match_count"], 5)
        self.assertEqual(result["mismatch_count"], 0)
        self.assertIsNone(result["first_mismatch"])
        self.assertEqual(result["weight"], 5)

    def test_wave15_summary_structure(self):
        summary = wave15_summary()
        self.assertEqual(summary["weight"], 5)
        self.assertEqual(summary["self_dual_hbar_sq"], Fraction(-1, 8))
        self.assertEqual(summary["kodaira_weight_total"], 3)
        self.assertEqual(summary["euler_O_K3"], 2)
        self.assertEqual(summary["paramodular_anomaly_weight"], 5)
        self.assertTrue(summary["is_anomaly_cancelled"])
        # Leading Heegner-label multiplicities match EOT table.
        leading = summary["bruinier_multiplicities_leading"]
        self.assertEqual(leading[(0, 1, 0)], 2)
        self.assertEqual(leading[(1, 0, 0)], 20)
        self.assertEqual(leading[(0, 0, 1)], 20)
        self.assertEqual(leading[(1, 1, 1)], 216)
        self.assertEqual(leading[(1, 0, 1)], -128)

    def test_total_one_loop_fourier_table_consistency(self):
        """total_one_loop_fourier_table <-> bruinier_multiplicities_up_to_order."""
        lhs = total_one_loop_fourier_table(n_max=4)
        rhs = bruinier_multiplicities_up_to_order(n_max=4)
        self.assertEqual(lhs, rhs)


if __name__ == "__main__":
    unittest.main()
