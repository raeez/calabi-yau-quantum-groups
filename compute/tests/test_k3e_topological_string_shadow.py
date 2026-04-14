r"""
Tests for the topological string / shadow partition function comparison on K3 x E.

Verifies:
    1. Gottsche formula: chi(Hilb^n(K3)) = p_{24}(n) against known values
    2. Ramanujan tau function against known values
    3. eta^{24} and 1/eta^{24} product expansions
    4. Bar Euler product (rank 1) = Gottsche formula (exact match)
    5. kappa-spectrum: four distinct values {2, 3, 5, 24}
    6. Degree-zero DT triviality: Z_{DT,0} = 1 from chi(K3xE) = 0
    7. DT = PT identity from chi = 0
    8. BPS / shadow tower dictionary: discriminant classification
    9. Borcherds weight formula: c(0)/2 = 10/2 = 5
   10. Shadow class: rank 1 = G, full = M
   11. Rank-1 bar Euler exponents are constant (-24)
   12. BKM diagonal exponents are non-constant (class M)
   13. Wall-crossing / shadow tower structural correspondence
   14. First fermionic root at D=3, c(3) = -64

Ground truth:
    - Gottsche (1990): chi(Hilb^n(K3)) = p_{24}(n)
    - Ramanujan (1916): tau(n) values
    - Eichler-Zagier (1985): phi_{0,1} coefficients
    - Dijkgraaf-Moore-Verlinde-Verlinde (1997): DMVV formula
    - Oberdieck-Pixton (2019): Z^X = C / Delta_5^2
    - Bridgeland (2011), Toda (2010): DT/PT correspondence
    - Kontsevich-Soibelman (2008): wall-crossing formula

AP constraints:
    - AP-CY8: Borcherds denominator != bar Euler product (bridge required)
    - AP-CY6: A_{K3xE} not constructed at d=3 (conditional results)
    - AP155: Known invariants recovered through new construction path
    - AP113: All kappa values carry subscripts (ch, BKM, cat, fiber)

Manuscript references:
    k3_times_e.tex: sec:k3e-topological-string-shadow
    Gottsche: thm:k3e-yau-zaslow
    DT triviality: thm:k3e-dt-degree0
    Borcherds product: thm:k3e-borcherds-product
"""

import pytest
import sys
import os
import math
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.k3e_topological_string_shadow import (
    # Constants
    CHI_K3,
    KAPPA_CH_K3,
    KAPPA_CH_E,
    KAPPA_CH_K3E,
    KAPPA_BKM,
    KAPPA_FIBER,
    # Gottsche / eta
    gottsche_product_coefficients,
    eta_power_coefficients,
    ramanujan_tau,
    KNOWN_RAMANUJAN_TAU,
    KNOWN_HILB_CHI,
    # Bar Euler
    bar_euler_product_exponents_rank1,
    bar_euler_product_class_g,
    bar_euler_exponents_bkm,
    # Borcherds
    borcherds_denominator_exponents,
    borcherds_weight,
    # DT
    dt_partition_function_k3e_rank0,
    dt_partition_function_k3e_rank1,
    dt_vs_pt_identity,
    # Comparison
    compare_gottsche_vs_bar_euler,
    kappa_spectrum_k3e,
    bps_exponent_identification,
    wall_crossing_shadow_tower_dictionary,
    topological_string_shadow_comparison_summary,
    # Verification
    verify_gottsche_vs_known,
    verify_ramanujan_tau_vs_known,
)


# ===========================================================================
# 1. GOTTSCHE FORMULA
# ===========================================================================

class TestGottscheFormula:
    """Test chi(Hilb^n(K3)) = prod 1/(1-q^k)^{24} coefficients."""

    def test_hilb0(self):
        """chi(Hilb^0(K3)) = 1 (a point)."""
        coeffs = gottsche_product_coefficients(0)
        assert coeffs[0] == 1

    def test_hilb1(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        coeffs = gottsche_product_coefficients(1)
        assert coeffs[1] == 24

    def test_hilb2(self):
        """chi(Hilb^2(K3)) = 324."""
        coeffs = gottsche_product_coefficients(2)
        assert coeffs[2] == 324

    def test_hilb3(self):
        """chi(Hilb^3(K3)) = 3200."""
        coeffs = gottsche_product_coefficients(3)
        assert coeffs[3] == 3200

    def test_hilb4(self):
        """chi(Hilb^4(K3)) = 25650."""
        coeffs = gottsche_product_coefficients(4)
        assert coeffs[4] == 25650

    def test_hilb5(self):
        """chi(Hilb^5(K3)) = 176256."""
        coeffs = gottsche_product_coefficients(5)
        assert coeffs[5] == 176256

    def test_hilb6(self):
        """chi(Hilb^6(K3)) = 1073720."""
        coeffs = gottsche_product_coefficients(6)
        assert coeffs[6] == 1073720

    def test_all_known_values(self):
        """Verify all known chi(Hilb^n(K3)) values."""
        result = verify_gottsche_vs_known()
        assert result['passed'], f"Mismatches: {result['mismatches']}"

    def test_positive_coefficients(self):
        """All chi(Hilb^n(K3)) are positive for n >= 0."""
        coeffs = gottsche_product_coefficients(15)
        for n in range(16):
            assert coeffs[n] > 0, f"chi(Hilb^{n}) = {coeffs[n]} <= 0"

    def test_monotone_increasing(self):
        """chi(Hilb^n(K3)) is strictly increasing for n >= 1."""
        coeffs = gottsche_product_coefficients(15)
        for n in range(2, 16):
            assert coeffs[n] > coeffs[n - 1], (
                f"chi(Hilb^{n}) = {coeffs[n]} <= chi(Hilb^{n-1}) = {coeffs[n-1]}"
            )


# ===========================================================================
# 2. RAMANUJAN TAU FUNCTION
# ===========================================================================

class TestRamanujanTau:
    """Test Delta(q) = q * prod (1-q^k)^{24} coefficients."""

    def test_tau1(self):
        """tau(1) = 1."""
        taus = ramanujan_tau(2)
        assert taus[0] == 1

    def test_tau2(self):
        """tau(2) = -24."""
        taus = ramanujan_tau(3)
        assert taus[1] == -24

    def test_tau3(self):
        """tau(3) = 252."""
        taus = ramanujan_tau(4)
        assert taus[2] == 252

    def test_tau4(self):
        """tau(4) = -1472."""
        taus = ramanujan_tau(5)
        assert taus[3] == -1472

    def test_tau5(self):
        """tau(5) = 4830."""
        taus = ramanujan_tau(6)
        assert taus[4] == 4830

    def test_all_known_tau(self):
        """Verify all known Ramanujan tau values."""
        result = verify_ramanujan_tau_vs_known()
        assert result['passed'], f"Mismatches: {result['mismatches']}"

    def test_tau_multiplicativity(self):
        """tau is multiplicative for coprime arguments: tau(mn) = tau(m)*tau(n)."""
        taus = ramanujan_tau(16)
        # tau(6) = tau(2)*tau(3) = -24 * 252 = -6048
        assert taus[5] == taus[1] * taus[2], (
            f"tau(6)={taus[5]} != tau(2)*tau(3)={taus[1]*taus[2]}"
        )
        # tau(10) = tau(2)*tau(5) = -24 * 4830 = -115920
        assert taus[9] == taus[1] * taus[4], (
            f"tau(10)={taus[9]} != tau(2)*tau(5)={taus[1]*taus[4]}"
        )
        # tau(15) = tau(3)*tau(5) = 252 * 4830 = 1217160
        assert taus[14] == taus[2] * taus[4], (
            f"tau(15)={taus[14]} != tau(3)*tau(5)={taus[2]*taus[4]}"
        )


# ===========================================================================
# 3. ETA PRODUCTS
# ===========================================================================

class TestEtaProducts:
    """Test eta(q)^k product expansions."""

    def test_eta24_leading(self):
        """prod (1-q^k)^{24}: leading coefficient is 1."""
        coeffs = eta_power_coefficients(5, 24)
        assert coeffs[0] == 1

    def test_eta24_second(self):
        """prod (1-q^k)^{24}: coefficient of q^1 is -24."""
        coeffs = eta_power_coefficients(5, 24)
        assert coeffs[1] == -24

    def test_inverse_eta24_leading(self):
        """prod 1/(1-q^k)^{24}: leading coefficient is 1."""
        coeffs = eta_power_coefficients(5, -24)
        assert coeffs[0] == 1

    def test_inverse_eta24_second(self):
        """prod 1/(1-q^k)^{24}: coefficient of q^1 is 24 = chi(K3)."""
        coeffs = eta_power_coefficients(5, -24)
        assert coeffs[1] == 24

    def test_eta_inverse_identity(self):
        """prod (1-q^k)^{24} * prod 1/(1-q^k)^{24} = 1 through q^10."""
        max_n = 10
        eta = eta_power_coefficients(max_n, 24)
        inv_eta = eta_power_coefficients(max_n, -24)
        # Convolve
        for n in range(1, max_n + 1):
            conv = sum(eta[k] * inv_eta[n - k] for k in range(n + 1))
            assert conv == 0, f"Convolution at q^{n} = {conv} != 0"


# ===========================================================================
# 4. BAR EULER PRODUCT = GOTTSCHE
# ===========================================================================

class TestBarEulerGottsche:
    """Test that rank-1 bar Euler product reproduces Gottsche formula."""

    def test_exact_agreement(self):
        """Bar Euler product (rank 1) = Gottsche formula exactly."""
        result = compare_gottsche_vs_bar_euler(15)
        assert result['passed'], f"Mismatches: {result['mismatches']}"

    def test_rank1_exponents_constant(self):
        """Rank-1 bar Euler exponents are all -24."""
        exponents = bar_euler_product_exponents_rank1(10)
        assert all(e == -24 for e in exponents), (
            f"Non-constant exponents: {exponents}"
        )

    def test_rank1_exponent_equals_neg_chi(self):
        """Rank-1 bar Euler exponent = -chi(K3) = -24."""
        exponents = bar_euler_product_exponents_rank1(1)
        assert exponents[0] == -CHI_K3

    def test_bar_euler_first_terms(self):
        """First terms of bar Euler product match known Hilb^n(K3)."""
        bar = bar_euler_product_class_g(6)
        for n, expected in KNOWN_HILB_CHI.items():
            assert int(bar[n]) == expected, (
                f"bar_euler[{n}] = {bar[n]}, expected {expected}"
            )


# ===========================================================================
# 5. KAPPA-SPECTRUM
# ===========================================================================

class TestKappaSpectrum:
    """Test the four-valued kappa-spectrum of K3 x E."""

    def test_kappa_ch_k3xe(self):
        """kappa_ch(K3 x E) = 3 by additivity."""
        assert KAPPA_CH_K3E == KAPPA_CH_K3 + KAPPA_CH_E
        assert KAPPA_CH_K3E == 3

    def test_kappa_bkm(self):
        """kappa_BKM = 5 = weight of Delta_5."""
        assert KAPPA_BKM == 5

    def test_kappa_cat(self):
        """kappa_cat = chi(O_{K3}) = 2."""
        assert KAPPA_CH_K3 == 2

    def test_kappa_fiber(self):
        """kappa_fiber = chi(K3) = 24."""
        assert KAPPA_FIBER == 24

    def test_all_four_distinct(self):
        """All four kappa values are distinct."""
        spectrum = kappa_spectrum_k3e()
        assert spectrum['all_distinct']

    def test_kappa_ch_neq_kappa_bkm(self):
        """kappa_ch = 3 != 5 = kappa_BKM. The source of the subscript confusion."""
        assert KAPPA_CH_K3E != KAPPA_BKM

    def test_borcherds_weight_formula(self):
        """wt(Delta_5) = c(0)/2 = 10/2 = 5."""
        assert borcherds_weight() == 5

    def test_chi_top_over_24_wrong(self):
        """chi_top(K3 x E)/24 = 0, which is WRONG for kappa_ch."""
        chi_top = CHI_K3 * 0  # chi(E) = 0
        assert chi_top // 24 == 0
        assert chi_top // 24 != KAPPA_CH_K3E  # 0 != 3
        assert chi_top // 24 != KAPPA_BKM     # 0 != 5


# ===========================================================================
# 6. DT PARTITION FUNCTION
# ===========================================================================

class TestDTPartitionFunction:
    """Test DT partition function of K3 x E."""

    def test_degree0_trivial(self):
        """Z_{DT,0}(K3 x E) = 1 because chi(K3 x E) = 0."""
        z0 = dt_partition_function_k3e_rank0(5)
        assert z0[0] == 1
        assert all(z0[n] == 0 for n in range(1, 6))

    def test_rank1_equals_gottsche(self):
        """Rank-1 DT = chi(Hilb^n(K3)) = Gottsche formula."""
        dt1 = dt_partition_function_k3e_rank1(6)
        gottsche = gottsche_product_coefficients(6)
        for n in range(7):
            assert dt1[n] == gottsche[n], (
                f"DT rank-1 at n={n}: {dt1[n]} != Gottsche {gottsche[n]}"
            )

    def test_dt_pt_identity(self):
        """Z_DT = Z_PT for K3 x E (from chi = 0)."""
        result = dt_vs_pt_identity()
        assert result['dt_equals_pt']
        assert result['chi_K3xE'] == 0
        assert result['macmahon_exponent'] == 0

    def test_chi_k3xe_vanishes(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert CHI_K3 * 0 == 0  # chi(E) = 0


# ===========================================================================
# 7. BPS / SHADOW TOWER IDENTIFICATION
# ===========================================================================

class TestBPSShadowIdentification:
    """Test the BPS counting / shadow tower correspondence."""

    def test_bps_rank1_class_g(self):
        """Rank-1 BPS sector is class G (Gaussian)."""
        result = bps_exponent_identification(10)
        assert result['rank1_class'] == 'G'

    def test_bps_rank1_exponents_constant(self):
        """Rank-1 bar Euler exponents are all equal to -24."""
        result = bps_exponent_identification(10)
        assert result['rank1_exponent_constant']

    def test_bps_full_class_m(self):
        """Full BKM theory is class M (mixed, infinite depth)."""
        result = bps_exponent_identification(10)
        assert result['bkm_class'] == 'M'

    def test_bps_conditional_on_cy_a3(self):
        """Full identification is conditional on CY-A_3."""
        result = bps_exponent_identification(10)
        assert result['conditional_on'] == 'CY-A_3'

    def test_bkm_exponents_nonconstant(self):
        """BKM diagonal exponents are NOT constant (class M indicator)."""
        result = bps_exponent_identification(10)
        assert not result['bkm_exponents_all_equal']


# ===========================================================================
# 8. BORCHERDS PRODUCT
# ===========================================================================

class TestBorcherdsProduct:
    """Test Borcherds product properties."""

    def test_f_neg1_equals_1(self):
        """f(-1) = 1 (real root, the simple root contribution)."""
        exps = borcherds_denominator_exponents(10)
        assert exps[-1] == 1

    def test_f_0_equals_10(self):
        """f(0) = 10 (null root multiplicity)."""
        exps = borcherds_denominator_exponents(10)
        assert exps[0] == 10

    def test_f_3_equals_neg64(self):
        """f(3) = -64 (first fermionic root)."""
        exps = borcherds_denominator_exponents(10)
        assert exps[3] == -64

    def test_f_4_equals_108(self):
        """f(4) = 108."""
        exps = borcherds_denominator_exponents(10)
        assert exps[4] == 108

    def test_weight_5(self):
        """Weight of Borcherds lift = 5."""
        assert borcherds_weight() == 5

    def test_weight_from_c0(self):
        """Weight = c(0)/2 = 10/2 = 5."""
        exps = borcherds_denominator_exponents(2)
        assert exps[0] // 2 == 5

    def test_discriminant_constraint(self):
        """Only D = -1 or D >= 0 with D equiv 0,3 mod 4 have nonzero f(D).

        AP-CY9: Jacobi form discriminant constraint.
        """
        exps = borcherds_denominator_exponents(60)
        for D, fD in exps.items():
            if fD != 0:
                if D >= 0:
                    assert D % 4 in (0, 3), (
                        f"f({D}) = {fD} nonzero but D mod 4 = {D % 4}"
                    )
                else:
                    assert D == -1, f"Negative D = {D} != -1 has f(D) = {fD}"


# ===========================================================================
# 9. WALL-CROSSING / SHADOW TOWER DICTIONARY
# ===========================================================================

class TestWallCrossingShadowDictionary:
    """Test the KS wall-crossing / shadow tower structural correspondence."""

    def test_first_fermionic_at_d3(self):
        """First fermionic root at discriminant D = 3."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        assert wc['first_fermionic'] == 3

    def test_first_fermionic_mult_neg64(self):
        """First fermionic multiplicity: c(3) = -64."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        assert wc['first_fermionic_mult'] == -64

    def test_shadow_class_m(self):
        """Full shadow class is M (infinite depth)."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        assert wc['shadow_class'] == 'M'

    def test_kappa_values_in_dictionary(self):
        """Dictionary records both kappa_ch and kappa_BKM."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        assert wc['kappa_ch'] == 3
        assert wc['kappa_BKM'] == 5

    def test_real_root_at_d_neg1(self):
        """D = -1 entry is real, bosonic, multiplicity 1."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        d_neg1 = [e for e in wc['entries'] if e['discriminant'] == -1]
        assert len(d_neg1) == 1
        assert d_neg1[0]['root_type'] == 'real'
        assert d_neg1[0]['parity'] == 'bosonic'
        assert d_neg1[0]['c(D)'] == 1

    def test_d0_entry(self):
        """D = 0 entry: imaginary, bosonic, c(0) = 10."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        d0 = [e for e in wc['entries'] if e['discriminant'] == 0]
        assert len(d0) == 1
        assert d0[0]['root_type'] == 'imaginary'
        assert d0[0]['parity'] == 'bosonic'
        assert d0[0]['c(D)'] == 10

    def test_conditionality(self):
        """Results are conditional on CY-A_3."""
        wc = wall_crossing_shadow_tower_dictionary(20)
        assert 'CY-A_3' in wc['conditional_on']


# ===========================================================================
# 10. FULL COMPARISON SUMMARY
# ===========================================================================

class TestFullComparison:
    """Integration tests: full topological string vs shadow comparison."""

    def test_summary_rank1(self):
        """Summary rank-1 agreement: topological string = bar Euler."""
        summary = topological_string_shadow_comparison_summary(6)
        ts = summary['rank1_agreement']['topological_string']
        be = summary['rank1_agreement']['bar_euler_product']
        assert ts == be

    def test_summary_kappa_spectrum(self):
        """Summary records correct kappa-spectrum."""
        summary = topological_string_shadow_comparison_summary(6)
        ks = summary['kappa_spectrum']
        assert ks['kappa_ch'] == 3
        assert ks['kappa_BKM'] == 5
        assert ks['kappa_cat'] == 2
        assert ks['kappa_fiber'] == 24

    def test_summary_dt_vanishing(self):
        """Summary records chi(K3xE) = 0 and Z_{DT,0} = 1."""
        summary = topological_string_shadow_comparison_summary(6)
        dt = summary['dt_vanishing']
        assert dt['chi_K3xE'] == 0
        assert dt['Z_DT0'] == 1

    def test_summary_shadow_classes(self):
        """Summary records rank-1 = G, full = M."""
        summary = topological_string_shadow_comparison_summary(6)
        sc = summary['shadow_class']
        assert 'G' in sc['rank1']
        assert 'M' in sc['full']

    def test_summary_conditionality_stated(self):
        """Summary explicitly states CY-A_3 conditionality (AP-CY6)."""
        summary = topological_string_shadow_comparison_summary(6)
        cond = summary['conditionality']
        assert 'CY-A_3' in cond['full_shadow']
        assert 'AP-CY8' in cond['borcherds_identification']

    def test_summary_borcherds_weight(self):
        """Summary records Borcherds weight = 5."""
        summary = topological_string_shadow_comparison_summary(6)
        assert summary['borcherds_bridge']['weight'] == 'c(0)/2 = 10/2 = 5'

    def test_rank1_first_term_is_1(self):
        """First term of rank-1 partition function is 1 = chi(Hilb^0)."""
        summary = topological_string_shadow_comparison_summary(6)
        assert summary['rank1_agreement']['topological_string'][0] == 1

    def test_rank1_second_term_is_24(self):
        """Second term of rank-1 partition function is 24 = chi(K3)."""
        summary = topological_string_shadow_comparison_summary(6)
        assert summary['rank1_agreement']['topological_string'][1] == 24
