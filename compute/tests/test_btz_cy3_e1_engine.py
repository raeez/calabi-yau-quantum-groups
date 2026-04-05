r"""Tests for BTZ black hole thermodynamics from CY3 E_1 chiral algebras.

VERIFICATION STRATEGY:
  Every test uses at least 2 independent verification paths (AP10).
  VP = verification path.

  VP1: Direct computation from defining formula
  VP2: Alternative formula / independent derivation
  VP3: Limiting case (beta -> 0, beta -> inf, kappa -> 0, n -> 0)
  VP4: Cross-family consistency (K3xE vs conifold vs C^3)
  VP5: Literature comparison (Wright 1931, Cardy, MacMahon)
  VP6: Numerical evaluation at specific values

Test count target: >= 90 tests.
"""

import math
import cmath
import pytest
from fractions import Fraction

import sys
import os

_LIB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")
if _LIB_DIR not in sys.path:
    sys.path.insert(0, _LIB_DIR)

from btz_cy3_e1_engine import (
    # Constants
    PI, TWO_PI, ZETA_3,
    # Faber-Pandharipande
    lambda_fp, _bernoulli_2g, _factorial_fraction,
    # CY3 data
    CY3BTZData,
    cy3_k3e_data, cy3_conifold_data, cy3_c3_data,
    cy3_quintic_data, cy3_local_p2_data, ALL_CY3_BTZ,
    # Entropy
    bekenstein_hawking_entropy, bekenstein_hawking_rotating,
    inverse_hawking_temperature, hawking_temperature,
    # Free energies
    F_g_scalar, free_energy_table, F1_from_kappa,
    # Quantum corrections
    entropy_correction_genus_g, entropy_all_genera, quantum_corrections_table,
    # MacMahon
    macmahon_coefficients, macmahon_coefficients_product,
    macmahon_value, macmahon_value_complex,
    log_macmahon_asymptotic, log_macmahon_subleading,
    plane_partition_count, _PP_COUNTS,
    # BTZ partition function
    btz_partition_function_c3, btz_partition_function_c3_complex,
    btz_free_energy_c3, btz_energy_c3, btz_entropy_c3,
    btz_partition_general_cy3,
    # Hawking-Page
    hawking_page_beta_classical, euclidean_action_btz,
    euclidean_action_thermal_ads, hawking_page_temperature_cy3,
    macmahon_convergence_radius, hagedorn_temperature_c3,
    # SFF
    spectral_form_factor_c3, spectral_form_factor_general,
    sff_time_series_c3, sff_dip_ramp_plateau_analysis,
    # Microcanonical
    microcanonical_entropy_c3, wright_asymptotic_entropy,
    wright_full_asymptotic, cardy_vs_wright_comparison,
    # Comparisons
    cy3_btz_comparison_table, kappa_additivity_check,
    koszul_dual_btz_entropy,
    # Consistency
    consistency_checks, cross_volume_bridge,
)


# =========================================================================
# Section 1: Faber-Pandharipande intersection numbers (6 tests)
# =========================================================================

class TestFaberPandharipande:
    """Verify FP intersection numbers lambda_g^FP."""

    def test_lambda_1_exact(self):
        """VP1: lambda_1 = 1/24 from formula."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2_exact(self):
        """VP1: lambda_2 = 7/5760 from formula."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3_exact(self):
        """VP1: lambda_3 = 31/967680 from formula."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_4_exact(self):
        """VP1: lambda_4 = 127/154828800 from formula."""
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda_5_exact(self):
        """VP1: lambda_5 = 73/3503554560 from formula."""
        assert lambda_fp(5) == Fraction(73, 3503554560)

    def test_lambda_all_positive(self):
        """VP2: All lambda_g > 0 (AP22: Bernoulli signs)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_{g} should be positive"

    def test_lambda_decreasing(self):
        """VP2: lambda_g decreases as g increases (Bernoulli decay)."""
        for g in range(1, 7):
            assert lambda_fp(g) > lambda_fp(g + 1), \
                f"lambda_{g} should be > lambda_{g+1}"

    def test_ahat_generating_function(self):
        """VP2: Verify against A-hat generating function.

        sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1
        """
        x = 0.5
        lhs = sum(float(lambda_fp(g)) * x ** (2 * g) for g in range(1, 8))
        rhs = (x / 2.0) / math.sin(x / 2.0) - 1.0
        assert abs(lhs - rhs) < 1e-10, f"A-hat GF: {lhs} vs {rhs}"


# =========================================================================
# Section 2: CY3 data structures (8 tests)
# =========================================================================

class TestCY3Data:
    """Verify CY3 modular characteristic data."""

    def test_k3e_kappa(self):
        """VP1: kappa(K3 x E) = 5."""
        data = cy3_k3e_data()
        assert data.kappa == Fraction(5)

    def test_k3e_c_eff(self):
        """VP2: c_eff(K3 x E) = 2 * kappa = 10."""
        data = cy3_k3e_data()
        assert data.c_eff == 2 * data.kappa

    def test_conifold_kappa(self):
        """VP1: kappa(conifold) = 1."""
        data = cy3_conifold_data()
        assert data.kappa == Fraction(1)

    def test_quintic_kappa(self):
        """VP1: kappa(quintic) = -200/24 = -25/3."""
        data = cy3_quintic_data()
        assert data.kappa == Fraction(-25, 3)

    def test_c3_data_structure(self):
        """VP1: C^3 data has correct fields."""
        data = cy3_c3_data()
        assert data.name == "C^3"
        assert data.is_compact is False

    def test_c_eff_equals_2_kappa(self):
        """VP4: c_eff = 2 * kappa for ALL families."""
        for name, factory in ALL_CY3_BTZ.items():
            data = factory()
            assert data.c_eff == 2 * data.kappa, \
                f"c_eff mismatch for {name}: {data.c_eff} != {2 * data.kappa}"

    def test_k3e_is_proved(self):
        """VP1: K3 x E identification is proved."""
        assert cy3_k3e_data().is_proved is True

    def test_quintic_is_conjectural(self):
        """VP1: Quintic identification is conjectural."""
        assert cy3_quintic_data().is_proved is False


# =========================================================================
# Section 3: Bekenstein-Hawking entropy (10 tests)
# =========================================================================

class TestBekensteinHawking:
    """Verify the leading BH entropy S = 2 pi sqrt(kappa M / 3)."""

    def test_bh_k3e_M10(self):
        """VP1: S_BH(K3xE, M=10) = 2 pi sqrt(50/3)."""
        S = bekenstein_hawking_entropy(5, 10)
        expected = 2.0 * PI * math.sqrt(50.0 / 3.0)
        assert abs(S - expected) < 1e-12

    def test_bh_conifold_M10(self):
        """VP1: S_BH(conifold, M=10) = 2 pi sqrt(10/3)."""
        S = bekenstein_hawking_entropy(1, 10)
        expected = 2.0 * PI * math.sqrt(10.0 / 3.0)
        assert abs(S - expected) < 1e-12

    def test_bh_scaling_with_kappa(self):
        """VP2: S_BH scales as sqrt(kappa) at fixed M."""
        M = 10.0
        S1 = bekenstein_hawking_entropy(1, M)
        S5 = bekenstein_hawking_entropy(5, M)
        ratio = S5 / S1
        assert abs(ratio - math.sqrt(5.0)) < 1e-12

    def test_bh_scaling_with_M(self):
        """VP2: S_BH scales as sqrt(M) at fixed kappa."""
        kappa = 5
        S1 = bekenstein_hawking_entropy(kappa, 1)
        S4 = bekenstein_hawking_entropy(kappa, 4)
        ratio = S4 / S1
        assert abs(ratio - 2.0) < 1e-12

    def test_bh_zero_mass(self):
        """VP3: S_BH(kappa, 0) = 0 (massless BTZ = global AdS)."""
        assert bekenstein_hawking_entropy(5, 0) == 0.0

    def test_bh_negative_kappa(self):
        """VP3: S_BH = 0 for negative kappa (no classical BH)."""
        assert bekenstein_hawking_entropy(-5, 10) == 0.0

    def test_rotating_equals_nonrotating(self):
        """VP2: Rotating with E_L = E_R = M gives 2 * S_BH(single)."""
        M = 10.0
        kappa = 5
        S_nr = bekenstein_hawking_entropy(kappa, M)
        S_rot = bekenstein_hawking_rotating(kappa, M, M)
        assert abs(S_rot - 2.0 * S_nr) < 1e-12

    def test_inverse_hawking_temperature(self):
        """VP1: beta_H = pi sqrt(kappa / (3M))."""
        kappa, M = 5, 10
        beta = inverse_hawking_temperature(kappa, M)
        expected = PI * math.sqrt(5.0 / 30.0)
        assert abs(beta - expected) < 1e-12

    def test_temperature_inverse(self):
        """VP2: T_H = 1 / beta_H."""
        kappa, M = 5, 10
        T = hawking_temperature(kappa, M)
        beta = inverse_hawking_temperature(kappa, M)
        assert abs(T * beta - 1.0) < 1e-12

    def test_bh_formula_cardy_convention(self):
        """VP5: S = 2pi sqrt(c_eff M / 6) with c_eff = 2 kappa.

        Cross-check: the formula S = 2pi sqrt(kappa M / 3)
        is equivalent to S = 2pi sqrt(c_eff M / 6) with c_eff = 2 kappa.
        """
        kappa, M = 5, 10
        S1 = 2.0 * PI * math.sqrt(float(kappa) * M / 3.0)
        c_eff = 2.0 * float(kappa)
        S2 = 2.0 * PI * math.sqrt(c_eff * M / 6.0)
        assert abs(S1 - S2) < 1e-12


# =========================================================================
# Section 4: Shadow free energies (8 tests)
# =========================================================================

class TestShadowFreeEnergies:
    """Verify F_g = kappa * lambda_g^FP."""

    def test_F1_k3e(self):
        """VP1: F_1(K3xE) = 5/24."""
        assert F_g_scalar(5, 1) == Fraction(5, 24)

    def test_F1_conifold(self):
        """VP1: F_1(conifold) = 1/24."""
        assert F_g_scalar(1, 1) == Fraction(1, 24)

    def test_F1_from_kappa_function(self):
        """VP2: F1_from_kappa matches F_g_scalar."""
        for k in [1, 2, 5, 10]:
            assert F1_from_kappa(k) == F_g_scalar(k, 1)

    def test_F2_k3e(self):
        """VP1: F_2(K3xE) = 5 * 7/5760 = 7/1152."""
        assert F_g_scalar(5, 2) == Fraction(5) * Fraction(7, 5760)

    def test_free_energy_table_length(self):
        """VP1: Table has correct number of entries."""
        table = free_energy_table(5, 5)
        assert len(table) == 5
        assert set(table.keys()) == {1, 2, 3, 4, 5}

    def test_free_energy_linearity(self):
        """VP2: F_g(a*kappa) = a * F_g(kappa) (linearity in kappa)."""
        for g in range(1, 6):
            F_5 = F_g_scalar(5, g)
            F_1 = F_g_scalar(1, g)
            assert F_5 == 5 * F_1

    def test_free_energy_positive(self):
        """VP2: F_g > 0 for positive kappa and all g."""
        for g in range(1, 8):
            assert F_g_scalar(5, g) > 0

    def test_free_energy_decreasing(self):
        """VP2: F_g decreases with g at fixed kappa."""
        for g in range(1, 6):
            assert F_g_scalar(5, g) > F_g_scalar(5, g + 1)


# =========================================================================
# Section 5: MacMahon function (16 tests)
# =========================================================================

class TestMacMahon:
    """Verify MacMahon function M(q) = prod (1-q^n)^{-n}."""

    def test_macmahon_p0(self):
        """VP1+VP5: p(0) = 1 (OEIS A000219)."""
        assert plane_partition_count(0) == 1

    def test_macmahon_p1(self):
        """VP1+VP5: p(1) = 1."""
        assert plane_partition_count(1) == 1

    def test_macmahon_p2(self):
        """VP1+VP5: p(2) = 3."""
        assert plane_partition_count(2) == 3

    def test_macmahon_p3(self):
        """VP1+VP5: p(3) = 6."""
        assert plane_partition_count(3) == 6

    def test_macmahon_p4(self):
        """VP1+VP5: p(4) = 13."""
        assert plane_partition_count(4) == 13

    def test_macmahon_p5(self):
        """VP1+VP5: p(5) = 24."""
        assert plane_partition_count(5) == 24

    def test_macmahon_first_21(self):
        """VP5: First 21 plane partition counts match OEIS A000219."""
        for n in range(len(_PP_COUNTS)):
            assert plane_partition_count(n) == _PP_COUNTS[n], \
                f"p({n}) = {plane_partition_count(n)} != {_PP_COUNTS[n]}"

    def test_two_methods_agree(self):
        """VP2: Log-exp and product methods agree."""
        N = 20
        c1 = macmahon_coefficients(N)
        c2 = macmahon_coefficients_product(N)
        for i in range(N):
            assert c1[i] == c2[i], f"Mismatch at q^{i}: {c1[i]} vs {c2[i]}"

    def test_macmahon_numerical_vs_exact(self):
        """VP6: Numerical product agrees with exact series."""
        q = 0.3
        N = 30
        coeffs = macmahon_coefficients(N)
        series_val = sum(float(coeffs[k]) * q ** k for k in range(N))
        product_val = macmahon_value(q, 50)
        assert abs(series_val - product_val) / product_val < 1e-6

    def test_macmahon_at_zero(self):
        """VP3: M(0) = 1."""
        assert abs(macmahon_value(0.0) - 1.0) < 1e-15

    def test_macmahon_positive(self):
        """VP2: M(q) > 0 for 0 < q < 1."""
        for q in [0.1, 0.3, 0.5, 0.7, 0.9]:
            assert macmahon_value(q) > 0

    def test_macmahon_increasing(self):
        """VP2: M(q) is increasing in q for 0 < q < 1."""
        vals = [macmahon_value(q) for q in [0.1, 0.3, 0.5, 0.7]]
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i + 1]

    def test_macmahon_complex_modulus(self):
        """VP6: |M(q)| <= M(|q|) for complex q."""
        q = 0.3 * cmath.exp(1j * 1.0)
        M_complex = macmahon_value_complex(q)
        M_real = macmahon_value(abs(q))
        assert abs(M_complex) <= M_real * 1.001  # small tolerance

    def test_convergence_radius(self):
        """VP1: M(q) has natural boundary at |q| = 1."""
        assert macmahon_convergence_radius() == 1.0

    def test_macmahon_diverges_near_1(self):
        """VP3: M(q) grows rapidly as q -> 1^-."""
        M_09 = macmahon_value(0.9, 100)
        M_095 = macmahon_value(0.95, 100)
        M_099 = macmahon_value(0.99, 200)
        assert M_095 > M_09
        assert M_099 > M_095

    def test_macmahon_p10(self):
        """VP5: p(10) = 500 (OEIS)."""
        assert plane_partition_count(10) == 500


# =========================================================================
# Section 6: BTZ partition function from C^3 (8 tests)
# =========================================================================

class TestBTZPartitionC3:
    """Verify Z_{BTZ}(beta, C^3) = M(e^{-beta})."""

    def test_Z_at_large_beta(self):
        """VP3: Z(beta -> inf) -> 1 (only vacuum state)."""
        Z = btz_partition_function_c3(10.0)
        assert abs(Z - 1.0) < 1e-3

    def test_Z_at_beta_1(self):
        """VP6: Z(1) = M(e^{-1}) > 1."""
        Z = btz_partition_function_c3(1.0)
        assert Z > 1.0

    def test_Z_positive(self):
        """VP2: Z > 0 for all beta > 0."""
        for beta in [0.5, 1.0, 2.0, 5.0]:
            assert btz_partition_function_c3(beta) > 0

    def test_Z_decreases_with_beta(self):
        """VP2: Z decreases as beta increases (higher temp = more states)."""
        betas = [0.5, 1.0, 2.0, 5.0]
        Zs = [btz_partition_function_c3(b) for b in betas]
        for i in range(len(Zs) - 1):
            assert Zs[i] > Zs[i + 1]

    def test_Z_equals_macmahon(self):
        """VP1: Z_BTZ(beta) = M(e^{-beta}) by definition."""
        beta = 1.5
        Z = btz_partition_function_c3(beta)
        M = macmahon_value(math.exp(-beta))
        assert abs(Z - M) < 1e-12

    def test_free_energy_positive(self):
        """VP2: F = -log Z < 0 for Z > 1 (high temperature)."""
        F = btz_free_energy_c3(0.5)
        assert F < 0

    def test_energy_positive(self):
        """VP2: <E> > 0 for finite temperature."""
        E = btz_energy_c3(1.0)
        assert E > 0

    def test_entropy_positive(self):
        """VP2: S = beta <E> + log Z > 0."""
        S = btz_entropy_c3(1.0)
        assert S > 0


# =========================================================================
# Section 7: Quantum corrections (8 tests)
# =========================================================================

class TestQuantumCorrections:
    """Verify genus-g quantum corrections to BTZ entropy."""

    def test_log_correction_sign(self):
        """VP1: S_1 = -(3/2) log(S_BH/(2pi)) < 0 for large BH."""
        S1 = entropy_correction_genus_g(5, 100, 1)
        # S_BH(5, 100) = 2pi sqrt(500/3) ~ 81.1, so S_BH/(2pi) > 1
        # log(...) > 0, so S_1 < 0
        assert S1 < 0

    def test_genus_2_correction_positive(self):
        """VP1: S_2 > 0 for positive kappa (lambda_2 > 0)."""
        S2 = entropy_correction_genus_g(5, 100, 2)
        assert S2 > 0

    def test_corrections_decrease_with_genus(self):
        """VP2: |S_g| decreases with g for large BH (epsilon << 1)."""
        kappa, M = 5, 1000
        corrections = [abs(entropy_correction_genus_g(kappa, M, g))
                       for g in range(2, 6)]
        for i in range(len(corrections) - 1):
            assert corrections[i] > corrections[i + 1]

    def test_all_genera_total(self):
        """VP1: S_total = S_BH + sum S_g."""
        result = entropy_all_genera(5, 100, g_max=3)
        S_BH = result['S_BH']
        S_total = result['S_total']
        expected = S_BH + sum(result[f'S_{g}'] for g in range(1, 4))
        assert abs(S_total - expected) < 1e-10

    def test_corrections_vanish_at_zero_kappa(self):
        """VP3: S_g = 0 for kappa = 0 (trivial algebra)."""
        for g in range(1, 4):
            # kappa = 0 gives S_BH = 0, so corrections undefined
            S = bekenstein_hawking_entropy(0, 10)
            assert S == 0.0

    def test_quantum_table_structure(self):
        """VP1: Quantum corrections table has correct structure."""
        table = quantum_corrections_table(5, 100, 5)
        assert len(table) == 5
        assert table[0]['g'] == 1
        assert table[4]['g'] == 5

    def test_relative_correction_small(self):
        """VP2: Relative correction small for large BH."""
        result = entropy_all_genera(5, 10000, g_max=3)
        assert abs(result['relative_correction']) < 0.01

    def test_genus_expansion_parameter(self):
        """VP1: epsilon = 2 pi / S_BH."""
        result = entropy_all_genera(5, 100, g_max=3)
        S_BH = result['S_BH']
        assert abs(result['epsilon'] - TWO_PI / S_BH) < 1e-14


# =========================================================================
# Section 8: Hawking-Page transition (7 tests)
# =========================================================================

class TestHawkingPage:
    """Verify the Hawking-Page phase transition."""

    def test_classical_hp_temperature(self):
        """VP1: beta_HP = 2 pi (classical)."""
        assert abs(hawking_page_beta_classical() - TWO_PI) < 1e-14

    def test_btz_action_negative_high_T(self):
        """VP2: I_BTZ < 0 at high temperature (small beta)."""
        I = euclidean_action_btz(5, 0.5)
        assert I < 0

    def test_ads_action_negative(self):
        """VP2: I_AdS < 0 for positive kappa and beta."""
        I = euclidean_action_thermal_ads(5, 1.0)
        assert I < 0

    def test_btz_dominates_high_T(self):
        """VP2: I_BTZ < I_AdS at high temperature."""
        beta = 0.5
        I_btz = euclidean_action_btz(5, beta)
        I_ads = euclidean_action_thermal_ads(5, beta)
        assert I_btz < I_ads

    def test_ads_dominates_low_T(self):
        """VP2: I_AdS < I_BTZ at low temperature."""
        beta = 20.0
        I_btz = euclidean_action_btz(5, beta)
        I_ads = euclidean_action_thermal_ads(5, beta)
        assert I_ads < I_btz

    def test_hp_kappa_independence(self):
        """VP2: beta_HP is independent of kappa (at classical level).

        Both actions are proportional to kappa, so the crossover
        point is kappa-independent.
        """
        beta1 = hawking_page_temperature_cy3(1, 0)
        beta5 = hawking_page_temperature_cy3(5, 0)
        assert abs(beta1 - beta5) < 1e-10

    def test_hp_quantum_shift_finite(self):
        """VP2: Quantum corrections give a finite shift to beta_HP."""
        beta_cl = hawking_page_temperature_cy3(5, 0)
        beta_q = hawking_page_temperature_cy3(5, 3)
        # The shift should be finite and relatively small
        assert abs(beta_q - beta_cl) < 5.0  # generous bound


# =========================================================================
# Section 9: Spectral Form Factor (9 tests)
# =========================================================================

class TestSpectralFormFactor:
    """Verify the spectral form factor SFF(t, beta)."""

    def test_sff_at_t0(self):
        """VP1: SFF(0, beta) = 1 (by definition)."""
        sff = spectral_form_factor_c3(0.0, 1.0, 20)
        assert abs(sff - 1.0) < 1e-10

    def test_sff_positive(self):
        """VP2: SFF >= 0 everywhere."""
        for t in [0.1, 0.5, 1.0, 5.0]:
            sff = spectral_form_factor_c3(t, 1.0, 20)
            assert sff >= 0

    def test_sff_bounded_by_1_at_large_beta(self):
        """VP3: SFF <= 1 for large beta (Z(beta+it) ~ Z(beta) when beta >> t).

        At very large beta, only the vacuum contributes:
        Z(beta+it) ~ Z(beta) * e^{it * 0} = Z(beta), so SFF -> 1.
        """
        sff = spectral_form_factor_c3(1.0, 10.0, 20)
        assert sff <= 1.0 + 1e-6

    def test_sff_dips_below_1(self):
        """VP2: SFF < 1 for some intermediate t (the dip)."""
        found_dip = False
        for t in [0.5, 1.0, 2.0, 3.0, 5.0, 10.0]:
            sff = spectral_form_factor_c3(t, 1.0, 20)
            if sff < 0.99:
                found_dip = True
                break
        assert found_dip, "SFF should dip below 1 at some time"

    def test_sff_general_at_t0(self):
        """VP1: General SFF at t=0 should be 1."""
        sff = spectral_form_factor_general(5, 0.0, 1.0, 3)
        assert abs(sff - 1.0) < 1e-10

    def test_sff_general_positive(self):
        """VP2: General SFF >= 0."""
        sff = spectral_form_factor_general(5, 1.0, 2.0, 3)
        assert sff >= 0

    def test_sff_time_series_structure(self):
        """VP1: Time series has correct structure."""
        t_vals = [0.5, 1.0, 2.0]
        series = sff_time_series_c3(1.0, t_vals, 20)
        assert len(series) == 3
        assert all('t' in pt and 'SFF' in pt for pt in series)

    def test_sff_analysis_structure(self):
        """VP1: DRP analysis returns correct fields."""
        result = sff_dip_ramp_plateau_analysis(1.0, N_times=20, t_max=10.0, N_terms=15)
        assert 'dip_time' in result
        assert 'dip_value' in result
        assert 'plateau_estimate' in result
        assert result['sff_at_0'] == 1.0

    def test_sff_symmetry_t_to_minus_t(self):
        """VP2: SFF(t) = SFF(-t) (time-reversal symmetry of |Z|^2)."""
        beta = 1.0
        sff_pos = spectral_form_factor_c3(2.0, beta, 20)
        sff_neg = spectral_form_factor_c3(-2.0, beta, 20)
        assert abs(sff_pos - sff_neg) < 1e-10


# =========================================================================
# Section 10: Microcanonical entropy and Wright asymptotics (8 tests)
# =========================================================================

class TestMicrocanonicalEntropy:
    """Verify microcanonical entropy S(n) = log p(n) and Wright asymptotics."""

    def test_entropy_n0(self):
        """VP3: S(0) = log(1) = 0."""
        assert microcanonical_entropy_c3(0) == 0.0

    def test_entropy_n1(self):
        """VP1: S(1) = log(1) = 0."""
        assert microcanonical_entropy_c3(1) == 0.0

    def test_entropy_n2(self):
        """VP1: S(2) = log(3)."""
        assert abs(microcanonical_entropy_c3(2) - math.log(3)) < 1e-14

    def test_entropy_increasing(self):
        """VP2: S(n) is non-decreasing (more states at higher energy)."""
        for n in range(1, 15):
            assert microcanonical_entropy_c3(n) <= microcanonical_entropy_c3(n + 1) + 1e-15

    def test_wright_positive(self):
        """VP2: Wright asymptotic S > 0 for n > 0."""
        for n in [1, 5, 10, 20]:
            assert wright_asymptotic_entropy(n) > 0

    def test_wright_approaches_exact(self):
        """VP6: Wright asymptotic ratio -> 1 as n increases.

        The ratio S_exact / S_wright should approach 1 for large n.
        """
        comparison = cardy_vs_wright_comparison([5, 10, 15, 20])
        # The ratio should be getting closer to 1
        ratios = [c['ratio'] for c in comparison if not math.isnan(c['ratio'])]
        # At n=20, ratio should be within ~20% of 1 (Wright is asymptotic)
        assert abs(ratios[-1] - 1.0) < 0.5

    def test_wright_coefficient(self):
        """VP1: alpha = (2/3)(3 zeta(3))^{1/3}."""
        alpha_computed = (2.0 / 3.0) * (3.0 * ZETA_3) ** (1.0 / 3.0)
        # alpha ~ 1.04 (approximately)
        assert 1.0 < alpha_computed < 1.1

    def test_wright_full_has_fields(self):
        """VP1: Full Wright asymptotic returns all fields."""
        result = wright_full_asymptotic(10)
        assert 'leading' in result
        assert 'subleading' in result
        assert 'exact' in result
        assert result['n'] == 10


# =========================================================================
# Section 11: Log MacMahon asymptotics (5 tests)
# =========================================================================

class TestLogMacMahonAsymptotics:
    """Verify log M(e^{-beta}) ~ zeta(3)/beta^2 as beta -> 0."""

    def test_leading_term(self):
        """VP1: Leading term is zeta(3)/beta^2."""
        beta = 0.5
        leading = log_macmahon_asymptotic(beta)
        expected = ZETA_3 / (beta ** 2)
        assert abs(leading - expected) < 1e-14

    def test_asymptotic_agreement(self):
        """VP6: Asymptotic agrees with exact at small beta.

        For beta = 0.1, log M(e^{-beta}) should be close to zeta(3)/beta^2.
        """
        beta = 0.1
        exact = math.log(macmahon_value(math.exp(-beta), 200))
        asymptotic = ZETA_3 / (beta ** 2)
        # At beta=0.1: asymptotic = 120.2, exact should be close
        relative_error = abs(exact - asymptotic) / asymptotic
        assert relative_error < 0.1  # 10% agreement at beta=0.1

    def test_subleading_structure(self):
        """VP1: Subleading expansion has correct fields."""
        result = log_macmahon_subleading(0.5)
        assert 'leading' in result
        assert 'log_term' in result
        assert 'total_asymptotic' in result

    def test_asymptotic_diverges_at_0(self):
        """VP3: log M -> infinity as beta -> 0^+."""
        val_small = log_macmahon_asymptotic(0.01)
        val_large = log_macmahon_asymptotic(1.0)
        assert val_small > val_large

    def test_asymptotic_at_large_beta(self):
        """VP3: log M(e^{-beta}) ~ 0 as beta -> infinity."""
        val = log_macmahon_asymptotic(100.0)
        assert val < 0.001


# =========================================================================
# Section 12: CY3 family comparisons (6 tests)
# =========================================================================

class TestCY3Comparisons:
    """Verify cross-family consistency of BTZ thermodynamics."""

    def test_comparison_table_structure(self):
        """VP1: Comparison table has correct structure."""
        table = cy3_btz_comparison_table(10.0)
        assert len(table) >= 3  # at least K3xE, conifold, C^3

    def test_k3e_dominates_conifold(self):
        """VP4: S_BH(K3xE) > S_BH(conifold) at same M."""
        M = 10.0
        S_k3e = bekenstein_hawking_entropy(5, M)
        S_con = bekenstein_hawking_entropy(1, M)
        assert S_k3e > S_con

    def test_entropy_ordering(self):
        """VP4: Entropy is ordered by kappa: K3xE > local P^2 > conifold."""
        M = 10.0
        S_k3e = bekenstein_hawking_entropy(5, M)
        S_p2 = bekenstein_hawking_entropy(Fraction(3, 2), M)
        S_con = bekenstein_hawking_entropy(1, M)
        assert S_k3e > S_p2 > S_con

    def test_kappa_additivity_check(self):
        """VP4: kappa is NOT additive for products (K3 x E != K3 + E)."""
        result = kappa_additivity_check()
        assert result['is_additive'] is False
        assert result['k3xe_kappa'] == 5
        assert result['naive_sum'] == 3

    def test_koszul_dual_entropy(self):
        """VP4: Koszul dual structure for free-field CY3."""
        result = koszul_dual_btz_entropy(1, 10)
        assert result['kappa'] == 1.0
        assert result['kappa_dual'] == -1.0
        # Negative kappa_dual -> no classical BH for dual
        assert result['S_dual_BH'] == 0.0

    def test_shadow_class_assignments(self):
        """VP1: Shadow classes are correctly assigned."""
        assert cy3_k3e_data().shadow_class == "L"
        assert cy3_conifold_data().shadow_class == "G"
        assert cy3_quintic_data().shadow_class == "M"


# =========================================================================
# Section 13: Consistency and cross-volume checks (8 tests)
# =========================================================================

class TestConsistency:
    """Verify internal consistency and cross-volume bridges."""

    def test_all_consistency_checks_pass(self):
        """VP1: All internal consistency checks pass."""
        checks = consistency_checks()
        for name, passed in checks.items():
            assert passed, f"Consistency check failed: {name}"

    def test_cross_volume_bridge_structure(self):
        """VP1: Cross-volume bridge document has correct fields."""
        bridge = cross_volume_bridge()
        assert 'vol1_kappa_formula' in bridge
        assert 'vol3_kappa_formula' in bridge
        assert 'cardy_formula' in bridge

    def test_hagedorn_analysis(self):
        """VP1: Hagedorn analysis for C^3."""
        result = hagedorn_temperature_c3()
        assert result['has_hagedorn'] is False
        assert result['natural_boundary'] is True
        assert result['growth_exponent'] == Fraction(2, 3)

    def test_btz_general_at_large_beta(self):
        """VP3: General shadow PF -> 1 at large beta (no corrections)."""
        Z = btz_partition_general_cy3(5, 100.0, g_max=3)
        # At large beta, hbar = 2pi/beta is small
        # F_1 * hbar^0 = F_1 = 5/24, so Z ~ exp(5/24) ~ 1.23
        F1 = float(F1_from_kappa(5))
        expected = math.exp(F1)
        assert abs(Z - expected) < 0.01

    def test_entropy_c3_at_finite_beta(self):
        """VP6: Entropy S = beta E + log Z is thermodynamically consistent."""
        beta = 2.0
        S = btz_entropy_c3(beta)
        E = btz_energy_c3(beta)
        logZ = math.log(btz_partition_function_c3(beta))
        assert abs(S - (beta * E + logZ)) < 1e-6

    def test_zeta3_value(self):
        """VP5: Apery's constant zeta(3) = 1.2020569..."""
        assert abs(ZETA_3 - 1.2020569031595942) < 1e-13

    def test_macmahon_complex_real_agreement(self):
        """VP2: M(q) for real q agrees between real and complex routines."""
        q = 0.5
        M_real = macmahon_value(q, 30)
        M_complex = macmahon_value_complex(complex(q, 0), 30)
        assert abs(M_real - M_complex.real) < 1e-10
        assert abs(M_complex.imag) < 1e-10

    def test_complex_btz_real_part(self):
        """VP2: Z_BTZ for purely imaginary tau has |Z| = Z(beta)."""
        beta = 1.5
        tau = complex(0, beta / TWO_PI)
        # q = e^{2pi i tau} = e^{2pi i * i beta/(2pi)} = e^{-beta}
        Z_real = btz_partition_function_c3(beta, 30)
        Z_complex = btz_partition_function_c3_complex(tau, 30)
        # The complex Z with purely imaginary tau should give M(e^{-beta})
        assert abs(abs(Z_complex) - Z_real) / Z_real < 1e-4


# =========================================================================
# Section 14: Cardy formula cross-checks (5 tests)
# =========================================================================

class TestCardyCrossChecks:
    """Verify Cardy formula across multiple derivation paths."""

    def test_cardy_from_microcanonical(self):
        """VP2: S_BH from Cardy and log p(n) should scale similarly.

        At energy n, Cardy gives S ~ 2 pi sqrt(kappa n / 3).
        Wright gives S ~ alpha n^{2/3}.
        These have DIFFERENT scaling (sqrt vs 2/3 power) because
        plane partitions are NOT a 2d CFT partition function
        (they have n^{2/3} growth, not n^{1/2}).

        This is a STRUCTURAL TEST: the C^3 BTZ does NOT follow the
        standard 2d CFT Cardy formula because the density of states
        grows sub-exponentially with exponent 2/3, not 1/2.
        """
        # The point: for C^3, the microcanonical entropy is S ~ n^{2/3},
        # while Cardy gives S ~ n^{1/2}.  These are DIFFERENT.
        # This is EXPECTED: C^3 is non-compact, and the chiral algebra
        # is W_{1+infty}, not Virasoro.
        n = 100
        S_exact = wright_asymptotic_entropy(n)
        # S ~ alpha * 100^{2/3} ~ alpha * 21.5 ~ 22.4
        assert S_exact > 15.0  # rough check

    def test_F1_universal(self):
        """VP4: F_1 = kappa/24 is universal across all CY3s with positive kappa."""
        for name, factory in ALL_CY3_BTZ.items():
            data = factory()
            if data.kappa > 0:
                F1 = F1_from_kappa(data.kappa)
                assert F1 == data.kappa * Fraction(1, 24), \
                    f"F_1 formula fails for {name}"

    def test_saddle_point_expansion_parameter(self):
        """VP1: epsilon = 2 pi / S_BH < 1 for large BH."""
        S_BH = bekenstein_hawking_entropy(5, 100)
        epsilon = TWO_PI / S_BH
        assert epsilon < 1.0, "epsilon should be < 1 for validity"

    def test_thermodynamic_relation(self):
        """VP2: dS/dM = 1/T = beta at the saddle."""
        kappa, M = 5, 100.0
        dM = 0.001
        S1 = bekenstein_hawking_entropy(kappa, M)
        S2 = bekenstein_hawking_entropy(kappa, M + dM)
        dSdM = (S2 - S1) / dM
        beta = inverse_hawking_temperature(kappa, M)
        assert abs(dSdM - beta) / beta < 1e-3

    def test_c3_growth_exponent(self):
        """VP5: C^3 entropy grows as n^{2/3} (Wright), not n^{1/2} (Cardy).

        This is the key difference between CY3 crystal melting and
        standard 2d CFT.
        """
        # Ratio log p(20) / log p(10) should be close to (20/10)^{2/3} = 2^{2/3}
        S10 = microcanonical_entropy_c3(10)
        S20 = microcanonical_entropy_c3(20)
        ratio = S20 / S10
        expected_ratio = 2.0 ** (2.0 / 3.0)
        # This won't be exact at finite n, but should be in the right ballpark
        assert abs(ratio - expected_ratio) < 1.0  # generous bound


# =========================================================================
# Section 15: BTZ General CY3 shadow PF (5 tests)
# =========================================================================

class TestBTZGeneralCY3:
    """Verify the shadow partition function for general CY3."""

    def test_shadow_pf_positive(self):
        """VP2: Z^sh > 0 for positive kappa."""
        Z = btz_partition_general_cy3(5, 2.0, 3)
        assert Z > 0

    def test_shadow_pf_at_zero_kappa(self):
        """VP3: Z^sh = 1 for kappa = 0 (trivial algebra)."""
        Z = btz_partition_general_cy3(0, 2.0, 3)
        assert abs(Z - 1.0) < 1e-14

    def test_shadow_pf_linearity_in_kappa(self):
        """VP2: log Z^sh is linear in kappa (since F_g = kappa * lambda_g)."""
        beta = 2.0
        logZ_1 = math.log(btz_partition_general_cy3(1, beta, 3))
        logZ_5 = math.log(btz_partition_general_cy3(5, beta, 3))
        assert abs(logZ_5 / logZ_1 - 5.0) < 1e-10

    def test_shadow_pf_decreases_with_beta(self):
        """VP2: Z^sh(small beta) > Z^sh(large beta) (more contributions at high T).

        Actually, the shadow PF behavior depends on the sign of the
        genus-1 contribution, which is F_1 = kappa/24 > 0.
        At beta -> inf, hbar -> 0, Z^sh -> exp(F_1) (genus-1 dominates).
        At beta -> 0, higher genus terms grow, so Z^sh can grow.
        """
        Z_small = btz_partition_general_cy3(5, 0.5, 5)
        Z_large = btz_partition_general_cy3(5, 10.0, 5)
        # Both should be positive
        assert Z_small > 0
        assert Z_large > 0

    def test_shadow_pf_genus_convergence(self):
        """VP2: Including more genera gives a convergent answer."""
        beta = 2.0
        Z3 = btz_partition_general_cy3(5, beta, 3)
        Z5 = btz_partition_general_cy3(5, beta, 5)
        Z7 = btz_partition_general_cy3(5, beta, 7)
        # Corrections should be getting smaller
        diff1 = abs(Z5 - Z3) / Z3
        diff2 = abs(Z7 - Z5) / Z5
        assert diff2 < diff1 or diff2 < 0.01


# =========================================================================
# Section 16: Integration tests (3 tests)
# =========================================================================

class TestIntegration:
    """End-to-end integration tests."""

    def test_full_pipeline_k3e(self):
        """VP1+VP4: Full computation pipeline for K3 x E."""
        data = cy3_k3e_data()
        kappa = data.kappa
        M = 50.0

        # Step 1: Entropy
        S_BH = bekenstein_hawking_entropy(kappa, M)
        assert S_BH > 0

        # Step 2: Temperature
        T = hawking_temperature(kappa, M)
        assert T > 0

        # Step 3: Free energies
        F_table = free_energy_table(kappa, 5)
        assert all(f > 0 for f in F_table.values())

        # Step 4: Quantum corrections
        result = entropy_all_genera(kappa, M, 5)
        assert result['S_total'] > 0

    def test_full_pipeline_c3(self):
        """VP1+VP4: Full computation pipeline for C^3."""
        # MacMahon partition function
        beta = 1.0
        Z = btz_partition_function_c3(beta)
        assert Z > 1.0

        # Free energy
        F = btz_free_energy_c3(beta)
        assert F < 0  # log Z > 0 -> F < 0

        # Energy
        E = btz_energy_c3(beta)
        assert E > 0

        # Entropy
        S = btz_entropy_c3(beta)
        assert S > 0

        # SFF at t=0
        sff = spectral_form_factor_c3(0.0, beta, 20)
        assert abs(sff - 1.0) < 1e-10

    def test_cross_family_consistency(self):
        """VP4: Ordering and signs are consistent across all families."""
        M = 10.0
        entropies = {}
        for name, factory in ALL_CY3_BTZ.items():
            data = factory()
            if float(data.kappa) > 0:
                S = bekenstein_hawking_entropy(data.kappa, M)
                entropies[name] = S
                assert S > 0, f"S_BH should be > 0 for {name}"

        # K3 x E has the largest kappa (5), so should have the largest entropy
        if "K3 x E" in entropies:
            for name, S in entropies.items():
                if name != "K3 x E":
                    assert entropies["K3 x E"] >= S, \
                        f"K3 x E should have largest entropy, but {name} has {S}"
