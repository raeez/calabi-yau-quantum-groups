"""Tests for the Humbert monodromy order-8 compute module (Wave 14/15).

Verifies:
  - Wave-14 triple-face identity K^{kappa_ch} = 2c_+(Mukai) = ord(H_1 mon) = ell_Lusztig = 8.
  - Wave-14 universal identity hbar^2 * K^{kappa_ch} = -1 on the B-family.
  - Wave-15 Deligne canonical-extension residue eigenvalues at H_1.
  - Wave-15 c_{2d} = -312 anchor via c_{4d} = 26 and chi(K3) = 24.
  - Wave-15 class-M shadow tower (S_2, S_4, S_5) at c = -312.
  - Wave-15 mock-modular weight 13 and effective c_eff = -264.

Author: Raeez Lorgat.
"""
# Raeez Lorgat -- Wave 15 Polyakov compute tests.

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_humbert_monodromy_8 import (
    K_kappa_ch_Mukai_K3,
    bruinier_reciprocity_classes_coincide,
    c_2d_chi_K3_factorisation_check,
    c_2d_classS_A1_Sigma_024,
    c_4d_classS_A1_Sigma_024,
    c_plus_Mukai_K3,
    c_minus_Mukai_K3,
    deligne_canonical_residue_eigenvalues,
    deligne_eigenvalue_sum,
    deligne_eigenvalue_sum_expected,
    deligne_residue_minimal_polynomial_degree,
    deligne_sum_check,
    effective_central_charge_K3_BKM,
    hbar_squared_at_specialisation,
    humbert_H1_monodromy_order,
    humbert_H4_monodromy_order,
    lusztig_ell_specialisation,
    mock_modular_weight_K3_BKM,
    universal_identity_check,
    virasoro_S2_at_c_minus_312,
    virasoro_S4_at_c_minus_312,
    virasoro_S5_at_c_minus_312,
    wave15_all_checks,
    wave15_spectrum_summary,
    zamolodchikov_norm_at_c_minus_312,
)


# ----------------------------------------------------------------------
# Wave 14: triple-face identity
# ----------------------------------------------------------------------


class TestTripleFaceOf8:
    def test_mukai_positive_signature(self):
        assert c_plus_Mukai_K3() == 4

    def test_mukai_negative_signature(self):
        assert c_minus_Mukai_K3() == 20

    def test_mukai_signature_sum_is_Mukai_lattice_rank(self):
        assert c_plus_Mukai_K3() + c_minus_Mukai_K3() == 24

    def test_koszul_conductor_is_8(self):
        assert K_kappa_ch_Mukai_K3() == 8

    def test_humbert_H1_monodromy_order_is_8(self):
        assert humbert_H1_monodromy_order() == 8

    def test_lusztig_ell_is_8(self):
        assert lusztig_ell_specialisation() == 8

    def test_bruinier_reciprocity(self):
        assert bruinier_reciprocity_classes_coincide()

    def test_H4_order_is_twice_H1(self):
        assert humbert_H4_monodromy_order() == 2 * humbert_H1_monodromy_order()


# ----------------------------------------------------------------------
# Wave 14: universal identity hbar^2 * K^{kappa_ch} = -1
# ----------------------------------------------------------------------


class TestUniversalIdentity:
    def test_hbar_squared_minus_one_eighth(self):
        assert hbar_squared_at_specialisation() == Fraction(-1, 8)

    def test_product_is_minus_one(self):
        assert universal_identity_check()

    def test_universal_identity_exact(self):
        """Rational arithmetic, no floating-point tolerance."""
        product = hbar_squared_at_specialisation() * K_kappa_ch_Mukai_K3()
        assert product == Fraction(-1, 1)


# ----------------------------------------------------------------------
# Wave 15: Deligne canonical-extension residue
# ----------------------------------------------------------------------


class TestDeligneCanonicalExtension:
    def test_eigenvalues_have_8_entries(self):
        assert len(deligne_canonical_residue_eigenvalues()) == 8

    def test_eigenvalues_in_fundamental_domain(self):
        for e in deligne_canonical_residue_eigenvalues():
            assert 0 <= e < 1, f"Eigenvalue {e} not in [0, 1)"

    def test_eigenvalues_are_rational_eighths(self):
        expected = [Fraction(k, 8) for k in range(8)]
        assert deligne_canonical_residue_eigenvalues() == expected

    def test_residue_is_semisimple(self):
        """Minimal polynomial of nilpotent part is x^1 (trivial nilpotent)."""
        assert deligne_residue_minimal_polynomial_degree() == 1

    def test_trace_formula_ell_minus_1_half(self):
        """Trace of residue = sum_{k=0}^{ell-1} k/ell = (ell-1)/2."""
        assert deligne_eigenvalue_sum() == Fraction(7, 2)
        assert deligne_eigenvalue_sum() == deligne_eigenvalue_sum_expected()

    def test_residue_sum_check(self):
        assert deligne_sum_check()


# ----------------------------------------------------------------------
# Wave 15: c_{2d} = -312 anchor and shadow-tower spectrum
# ----------------------------------------------------------------------


class TestChiralCentralCharge:
    def test_c_4d_is_26_Chacaltana_Distler(self):
        assert c_4d_classS_A1_Sigma_024() == 26

    def test_c_2d_is_minus_312(self):
        assert c_2d_classS_A1_Sigma_024() == -312

    def test_c_2d_equals_minus_12_times_c_4d(self):
        assert c_2d_classS_A1_Sigma_024() == -12 * c_4d_classS_A1_Sigma_024()

    def test_chi_K3_factorisation(self):
        """c_{2d} = -chi(K3) * c_{4d}/2 = -24 * 13 = -312."""
        assert c_2d_chi_K3_factorisation_check()


class TestShadowTowerAtMinus312:
    def test_S_2_is_minus_156(self):
        """S_2(Vir_c) = c/2, so S_2(-312) = -156."""
        assert virasoro_S2_at_c_minus_312() == Fraction(-156, 1)

    def test_S_4_formula(self):
        """S_4 = 10 / [c(5c+22)] at c=-312 gives 10/479856 = 5/239928."""
        assert virasoro_S4_at_c_minus_312() == Fraction(5, 239928)

    def test_S_5_formula(self):
        """S_5 = -48 / [c^2 (5c+22)] at c=-312. c^2 = 97344, 5c+22 = -1538."""
        c = -312
        expected = Fraction(-48, c * c * (5 * c + 22))
        assert virasoro_S5_at_c_minus_312() == expected

    def test_S_5_positive_sign(self):
        """S_5 is positive at c=-312 despite -48 coefficient: c^2(5c+22)<0."""
        assert virasoro_S5_at_c_minus_312() > 0

    def test_zamolodchikov_norm_is_positive(self):
        """c(5c+22)/10 at c=-312: both factors negative so product positive."""
        assert zamolodchikov_norm_at_c_minus_312() > 0

    def test_zamolodchikov_norm_value(self):
        """<Lambda|Lambda> = c(5c+22)/10 at c=-312 = 479856/10 = 239928/5."""
        assert zamolodchikov_norm_at_c_minus_312() == Fraction(239928, 5)

    def test_no_minimal_model_degeneracy(self):
        """5c+22 = -1538 != 0, so c=-312 is outside minimal-model lattice."""
        assert 5 * (-312) + 22 == -1538
        assert virasoro_S4_at_c_minus_312() != 0
        assert virasoro_S5_at_c_minus_312() != 0


# ----------------------------------------------------------------------
# Wave 15: mock modular weight and effective central charge
# ----------------------------------------------------------------------


class TestMockModularBPS:
    def test_mock_modular_weight_is_13(self):
        """w = -c/24 = -(-312)/24 = 13."""
        assert mock_modular_weight_K3_BKM() == 13

    def test_effective_c_with_h_min_minus_2(self):
        """c_eff = c - 24 h_min = -312 + 48 = -264."""
        assert effective_central_charge_K3_BKM() == -264

    def test_c_eff_still_negative(self):
        """Gravitational-anomaly sign preserved: c_eff < 0."""
        assert effective_central_charge_K3_BKM() < 0


# ----------------------------------------------------------------------
# Aggregate sanity
# ----------------------------------------------------------------------


class TestAggregate:
    def test_all_wave15_checks_pass(self):
        checks = wave15_all_checks()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Failed checks: {failed}"

    def test_spectrum_summary_shape(self):
        summary = wave15_spectrum_summary()
        expected_keys = {
            "c_4d",
            "c_2d",
            "c_factorisation",
            "S_2",
            "S_3",
            "S_4",
            "S_5",
            "Zamolodchikov_norm",
            "5c_plus_22",
            "mock_modular_weight",
            "c_eff",
        }
        assert set(summary.keys()) == expected_keys
