r"""Tests for categorical DT theory via the bar complex.

CONJECTURE (at d=2 PROVED, at d=3 CONDITIONAL on CY-A_3):
The charge-graded bar complex B_gamma(A_C) IS the categorical DT moduli,
with chi(B_gamma) = Omega(gamma) at Level 0 and D^b(B_gamma) ~ D^b(M_gamma)
at Level 2.

Multi-path verification across five levels:
    Level 0:  Omega(gamma) = chi(B_gamma(A))  (numerical DT)
    Level 1:  BPS cohomology H^*(B_gamma) = categorified DT
    Level 2:  D^b(B_gamma) ~ D^b(moduli)  (categorical moduli)
    Level 3:  Motivic bar = Joyce-Song motivic DT
    Level 4:  Wall-crossing = derived equivalences of B_gamma

Test suites:
    Suite 1:  Numerical DT (Level 0): C^3, K3, conifold
    Suite 2:  BPS cohomology (Level 1): purity, Euler char
    Suite 3:  Categorical moduli (Level 2): Hilb^n identification
    Suite 4:  Motivic bar / Joyce-Song (Level 3): bar Euler product
    Suite 5:  Wall-crossing (Level 4): derived equivalences
    Suite 6:  Cross-volume bridge: bar Euler product = DT partition function
    Suite 7:  Beauville-Yoshioka: higher rank moduli on K3
    Suite 8:  Plethystic operations: PLog/PExp round-trip
    Suite 9:  p_24(n) ground truth (OEIS A006922)
    Suite 10: Master verification: full five-level consistency
    Suite 11: AP compliance: AP-CY6, AP-CY8, AP-CY10, AP113, AP155

Ground truth:
    - p_24(n): 1, 24, 324, 3200, 25650, 176256, 1073720 (OEIS A006922)
    - PLog(M(q)) = sum n q^n  (BPS of C^3)
    - PLog(1/eta^{24}) = 24 sum q^n  (BPS of K3 rank 0)
    - MacMahon: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500 (OEIS A000219)
    - Omega(n*beta, conifold) = 1 for all n >= 1
    - Hilb^n(K3) is hyperkahler (0-shifted symplectic) for d=2
    - Hilb^n(C^3) has (-1)-shifted symplectic for d=3

Manuscript references:
    conj:categorical-ks-bar (e1_chiral_algebras.tex)
    prop:crystal-melting-bar-cohomology (cy_to_chiral.tex)
    conj:shadow-bps-dt (cy_to_chiral.tex)
    rem:shadow-bps-evidence-detail (cy_to_chiral.tex)
    subsec:bps-categories (braided_factorization.tex)
"""

import pytest
from fractions import Fraction

from compute.lib.categorical_dt_bar import (
    # Power series
    _fps_zero, _fps_one, _fps_mul, _fps_inv, _fps_log, _fps_exp,
    # Plethystic
    plethystic_log, plethystic_exp,
    # Partition functions
    macmahon_coefficients, p_24, inverse_eta_24_coeffs,
    # Charge lattice
    K3_CHARGE_LATTICE, C3_CHARGE_LATTICE, CONIFOLD_CHARGE_LATTICE,
    K3_EULER_CHAR, MUKAI_RANK,
    KAPPA_CH_K3, KAPPA_BKM_K3XE, KAPPA_CAT_K3, KAPPA_FIBER_K3,
    # Level 0: Numerical DT
    numerical_dt_c3, numerical_dt_k3_rank0, numerical_dt_conifold,
    # Level 1: BPS cohomology
    bps_cohomology_c3, bps_cohomology_k3_rank0,
    # Level 2: Categorical DT moduli
    categorical_dt_k3_rank0, categorical_dt_c3,
    # Level 3: Motivic bar
    motivic_bar_k3_rank0, motivic_bar_c3,
    # Joyce-Song
    joyce_song_c3, joyce_song_k3_rank0,
    # Level 4: Wall-crossing
    wall_crossing_conifold, wall_crossing_k3_rank0, wall_crossing_k3xe,
    # Cross-volume bridge
    bar_euler_dt_bridge_k3, bar_euler_dt_bridge_c3,
    # Higher rank
    beauville_k3_rank2,
    # Master
    verify_categorical_dt_c3, verify_categorical_dt_k3,
    full_categorical_dt_summary,
)


# ===========================================================================
# Suite 1: NUMERICAL DT (Level 0)
# ===========================================================================

class TestNumericalDT:
    """Level 0: Omega(gamma) = chi(B_gamma(A))."""

    def test_c3_omega_equals_n(self):
        """C^3: Omega(n) = n for n = 1, ..., 15."""
        dt = numerical_dt_c3(16)
        for n in range(1, 16):
            assert dt.omega[n] == n, f"Omega({n}) = {dt.omega[n]}, expected {n}"

    def test_c3_status_proved(self):
        """C^3 DT is PROVED (Schiffmann-Vasserot)."""
        dt = numerical_dt_c3(10)
        assert dt.status == "PROVED"

    def test_c3_partition_function_macmahon(self):
        """C^3 partition function = MacMahon M(q)."""
        dt = numerical_dt_c3(12)
        mac = macmahon_coefficients(12)
        for n in range(12):
            assert int(dt.partition_function[n]) == mac[n]

    def test_k3_rank0_omega_24(self):
        """K3 rank 0: Omega(n) = 24 for all n >= 1.

        This means 24 BPS generators per charge, one per Mukai lattice
        direction.  Matches kappa_fiber = 24 (AP113).
        """
        dt = numerical_dt_k3_rank0(12)
        for n in range(1, 12):
            assert dt.omega[n] == 24, f"Omega({n}) = {dt.omega[n]}, expected 24"

    def test_k3_rank0_pf_inverse_eta_24(self):
        """K3 rank 0: Z = 1/eta^{24}, first coefficients = p_24(n)."""
        dt = numerical_dt_k3_rank0(8)
        expected = [1, 24, 324, 3200, 25650, 176256, 1073720]
        for n in range(min(7, len(expected))):
            assert int(dt.partition_function[n]) == expected[n]

    def test_k3_rank0_status_proved(self):
        """K3 rank 0 DT is PROVED (CY-A_2 + Goettsche)."""
        dt = numerical_dt_k3_rank0(5)
        assert dt.status == "PROVED"

    def test_conifold_omega_1(self):
        """Conifold: Omega(n*beta) = 1 for all n >= 1."""
        dt = numerical_dt_conifold(10)
        for n in range(1, 10):
            assert dt.omega[n] == 1

    def test_conifold_status_proved(self):
        """Conifold DT is PROVED."""
        dt = numerical_dt_conifold(5)
        assert dt.status == "PROVED"

    def test_c3_charge_lattice(self):
        """C^3 charge lattice is Z (rank 1)."""
        dt = numerical_dt_c3(5)
        assert dt.charge_lattice.rank == 1

    def test_k3_charge_lattice_mukai(self):
        """K3 charge lattice is Mukai (rank 24, sig (4,20))."""
        dt = numerical_dt_k3_rank0(5)
        assert dt.charge_lattice.rank == 24
        assert dt.charge_lattice.signature == (4, 20)


# ===========================================================================
# Suite 2: BPS COHOMOLOGY (Level 1)
# ===========================================================================

class TestBPSCohomology:
    """Level 1: BPS cohomology H^*(B_gamma)."""

    def test_c3_pure(self):
        """C^3 BPS cohomology is pure (no wall-crossing)."""
        bps = bps_cohomology_c3(10)
        for n in range(1, 10):
            assert bps.is_pure[n], f"BPS at n={n} should be pure"

    def test_c3_dim_n(self):
        """C^3: dim H^0(B_n) = n (the only nonzero cohomology)."""
        bps = bps_cohomology_c3(10)
        for n in range(1, 10):
            assert bps.bps_betti[n] == [n]

    def test_c3_euler_char_match(self):
        """C^3: chi(H^*) = Omega(n) = n."""
        bps = bps_cohomology_c3(10)
        assert bps.euler_char_matches_omega

    def test_k3_chi_p24(self):
        """K3: chi(H^*(Hilb^n(K3))) = p_24(n)."""
        bps = bps_cohomology_k3_rank0(6)
        assert bps.euler_char_matches_omega

    def test_k3_hilb1_betti(self):
        """K3: Hilb^1(K3) = K3, Betti = (1, 0, 22, 0, 1)."""
        bps = bps_cohomology_k3_rank0(5)
        assert bps.bps_betti[1] == [1, 0, 22, 0, 1]

    def test_k3_hilb1_not_pure(self):
        """K3: Hilb^1(K3) = K3 is NOT pure (multiple Betti)."""
        bps = bps_cohomology_k3_rank0(5)
        assert not bps.is_pure[1]

    def test_k3_hilb1_chi_24(self):
        """K3: chi(K3) = 1 - 0 + 22 - 0 + 1 = 24 = p_24(1)."""
        bps = bps_cohomology_k3_rank0(5)
        betti = bps.bps_betti[1]
        chi = sum((-1)**k * b for k, b in enumerate(betti))
        assert chi == 24 == p_24(1)


# ===========================================================================
# Suite 3: CATEGORICAL DT MODULI (Level 2)
# ===========================================================================

class TestCategoricalDTModuli:
    """Level 2: D^b(B_gamma) as categorified DT moduli."""

    def test_k3_identification_hilb(self):
        """K3: B_n(H_Muk) identified with Hilb^n(K3)."""
        cat = categorical_dt_k3_rank0(6)
        assert cat.moduli_identification[1] == "D^b(Hilb^1(K3))"
        assert cat.moduli_identification[3] == "D^b(Hilb^3(K3))"

    def test_k3_moduli_dimension(self):
        """K3: dim(Hilb^n(K3)) = 2n (complex dimension)."""
        cat = categorical_dt_k3_rank0(8)
        for n in range(1, 8):
            assert cat.moduli_dimension[n] == 2 * n

    def test_k3_euler_chars_p24(self):
        """K3: chi(Hilb^n(K3)) = p_24(n) for all n."""
        cat = categorical_dt_k3_rank0(8)
        for n in range(1, 8):
            assert cat.euler_chars[n] == p_24(n)

    def test_k3_hyperkahler(self):
        """K3: Hilb^n(K3) is hyperkahler (0-shifted symplectic)."""
        cat = categorical_dt_k3_rank0(5)
        assert cat.shifted_symplectic_degree == 0

    def test_c3_shifted_symplectic_minus1(self):
        """C^3: Hilb^n(C^3) has (-1)-shifted symplectic (PTVV, CY_3)."""
        cat = categorical_dt_c3(5)
        assert cat.shifted_symplectic_degree == -1

    def test_c3_euler_chars_macmahon(self):
        """C^3: chi(Hilb^n(C^3)) = p_3d(n) (plane partition count)."""
        cat = categorical_dt_c3(10)
        mac = macmahon_coefficients(10)
        for n in range(1, 10):
            assert cat.euler_chars[n] == mac[n]

    def test_c3_moduli_identification(self):
        """C^3: B_n identified with Hilb^n(C^3)^{virt}."""
        cat = categorical_dt_c3(3)
        assert "Hilb" in cat.moduli_identification[1]

    def test_k3_status_proved(self):
        """K3 categorical DT is PROVED (CY-A_2)."""
        cat = categorical_dt_k3_rank0(3)
        assert cat.status == "PROVED"
        assert "CY-A_2" in cat.dependencies[0]


# ===========================================================================
# Suite 4: MOTIVIC BAR / JOYCE-SONG (Level 3)
# ===========================================================================

class TestMotivicBar:
    """Level 3: motivic bar complex and Joyce-Song integration."""

    def test_k3_bps_24(self):
        """K3: PLog(1/eta^{24}) = 24 * sum q^n, so Omega(n) = 24."""
        mot = motivic_bar_k3_rank0(10)
        for n in range(1, 10):
            assert int(mot.bps_omega[n]) == 24

    def test_k3_bar_euler_matches(self):
        """K3: bar Euler product matches 1/eta^{24}."""
        mot = motivic_bar_k3_rank0(10)
        assert mot.bar_euler_product_matches

    def test_c3_bps_n(self):
        """C^3: PLog(M(q)) = sum n q^n, so Omega(n) = n."""
        mot = motivic_bar_c3(12)
        for n in range(1, 12):
            assert int(mot.bps_omega[n]) == n

    def test_c3_bar_euler_matches(self):
        """C^3: bar Euler product matches MacMahon."""
        mot = motivic_bar_c3(12)
        assert mot.bar_euler_product_matches

    def test_js_c3_integration_n(self):
        """Joyce-Song for C^3: I^{JS}(B_n) = n."""
        js = joyce_song_c3(10)
        for n in range(1, 10):
            assert js.integration_values[n] == Fraction(n)

    def test_js_c3_ring_hom(self):
        """Joyce-Song map for C^3 is a ring homomorphism."""
        js = joyce_song_c3(5)
        assert js.is_ring_hom

    def test_js_k3_integration_24(self):
        """Joyce-Song for K3: I^{JS}(B_n) = 24."""
        js = joyce_song_k3_rank0(8)
        for n in range(1, 8):
            assert js.integration_values[n] == Fraction(24)

    def test_js_k3_matches_bar(self):
        """Joyce-Song invariants match bar Euler chars for K3."""
        js = joyce_song_k3_rank0(5)
        assert js.matches_bar_euler

    def test_k3_motivic_status(self):
        """K3 motivic bar is PROVED."""
        mot = motivic_bar_k3_rank0(5)
        assert mot.status == "PROVED"


# ===========================================================================
# Suite 5: WALL-CROSSING (Level 4)
# ===========================================================================

class TestWallCrossing:
    """Level 4: wall-crossing as derived equivalences."""

    def test_conifold_two_chambers(self):
        """Conifold has two chambers."""
        wc = wall_crossing_conifold()
        assert wc.n_chambers == 2

    def test_conifold_flop_equivalence(self):
        """Conifold wall-crossing is a Bondal-Orlov flop."""
        wc = wall_crossing_conifold()
        assert "Bondal-Orlov" in wc.equivalence_types["flop wall"]

    def test_conifold_omega_independent(self):
        """Conifold: Omega is chamber-independent."""
        wc = wall_crossing_conifold()
        assert wc.omega_chamber_independent

    def test_conifold_no_nonprimitive_wc(self):
        """Conifold: no wall-crossing for non-primitive charges."""
        wc = wall_crossing_conifold()
        assert not wc.non_primitive_wall_crossing

    def test_k3_rank0_single_chamber(self):
        """K3 rank 0: single chamber (no walls)."""
        wc = wall_crossing_k3_rank0()
        assert wc.n_chambers == 1
        assert len(wc.walls) == 0

    def test_k3_rank0_omega_independent(self):
        """K3 rank 0: Omega is trivially chamber-independent."""
        wc = wall_crossing_k3_rank0()
        assert wc.omega_chamber_independent

    def test_k3xe_conditional(self):
        """K3 x E wall-crossing is CONDITIONAL on CY-A_3."""
        wc = wall_crossing_k3xe()
        assert wc.status == "CONDITIONAL"

    def test_k3xe_infinitely_many_chambers(self):
        """K3 x E: infinitely many chambers from BKM root system."""
        wc = wall_crossing_k3xe()
        assert wc.n_chambers == -1  # sentinel for infinity

    def test_k3xe_has_nonprimitive_wc(self):
        """K3 x E: non-primitive charges have wall-crossing."""
        wc = wall_crossing_k3xe()
        assert wc.non_primitive_wall_crossing


# ===========================================================================
# Suite 6: CROSS-VOLUME BRIDGE
# ===========================================================================

class TestBarEulerDTBridge:
    """Cross-volume: bar Euler product = DT partition function."""

    def test_k3_bridge_exact_match(self):
        """K3: bar Euler product exactly matches DT partition function."""
        bridge = bar_euler_dt_bridge_k3(12)
        assert bridge.match

    def test_k3_bridge_agreement_order(self):
        """K3: agreement to full computed order."""
        bridge = bar_euler_dt_bridge_k3(12)
        assert bridge.agreement_order == 12

    def test_c3_bridge_exact_match(self):
        """C^3: PExp(sum n q^n) = M(q) exactly."""
        bridge = bar_euler_dt_bridge_c3(15)
        assert bridge.match

    def test_c3_bridge_agreement_order(self):
        """C^3: agreement to full computed order."""
        bridge = bar_euler_dt_bridge_c3(15)
        assert bridge.agreement_order == 15

    def test_k3_bridge_first_coeffs(self):
        """K3: first coefficients of bridge match p_24."""
        bridge = bar_euler_dt_bridge_k3(6)
        expected = [1, 24, 324, 3200, 25650, 176256]
        for n in range(6):
            assert int(bridge.bar_euler_coeffs[n]) == expected[n]
            assert int(bridge.dt_pf_coeffs[n]) == expected[n]

    def test_c3_bridge_first_coeffs(self):
        """C^3: first coefficients of bridge match MacMahon."""
        bridge = bar_euler_dt_bridge_c3(8)
        expected = [1, 1, 3, 6, 13, 24, 48, 86]
        for n in range(8):
            assert int(bridge.bar_euler_coeffs[n]) == expected[n]


# ===========================================================================
# Suite 7: BEAUVILLE-YOSHIOKA
# ===========================================================================

class TestBeauville:
    """Beauville theorem: higher rank K3 moduli ~ Hilb^n(K3)."""

    def test_rank2_s0(self):
        """v = (2,0,0): <v,v> = 0, Hilb^1(K3), chi = 24."""
        bv = beauville_k3_rank2(0)
        assert bv.mukai_self_pairing == 0
        assert bv.hilb_n == 1
        assert bv.euler_char == p_24(1)
        assert bv.euler_char == 24

    def test_rank2_s1(self):
        """v = (2,0,1): <v,v> = 4, Hilb^3(K3), chi = p_24(3) = 3200."""
        bv = beauville_k3_rank2(1)
        assert bv.mukai_self_pairing == 4
        assert bv.hilb_n == 3
        assert bv.euler_char == p_24(3)
        assert bv.euler_char == 3200

    def test_rank2_s2(self):
        """v = (2,0,2): <v,v> = 8, Hilb^5(K3), chi = p_24(5)."""
        bv = beauville_k3_rank2(2)
        assert bv.hilb_n == 5
        assert bv.euler_char == p_24(5)

    def test_rank2_status_proved(self):
        """Beauville theorem is PROVED."""
        bv = beauville_k3_rank2(1)
        assert bv.status == "PROVED"

    def test_rank2_deformation_type(self):
        """Deformation type is Hilb^n(K3)."""
        bv = beauville_k3_rank2(1)
        assert bv.deformation_type == "Hilb^3(K3)"


# ===========================================================================
# Suite 8: PLETHYSTIC OPERATIONS
# ===========================================================================

class TestPlethystic:
    """Plethystic logarithm and exponential round-trip."""

    def test_plog_macmahon(self):
        """PLog(M(q)) = sum_{n>=1} n q^n."""
        mac = [Fraction(x) for x in macmahon_coefficients(15)]
        plog = plethystic_log(mac, 15)
        for n in range(1, 15):
            assert plog[n] == Fraction(n), f"PLog(M)[{n}] = {plog[n]}, expected {n}"

    def test_plog_inverse_eta_24(self):
        """PLog(1/eta^{24}) = 24 * sum q^n."""
        pf = inverse_eta_24_coeffs(12)
        plog = plethystic_log(pf, 12)
        for n in range(1, 12):
            assert plog[n] == Fraction(24), f"PLog(1/eta^24)[{n}] = {plog[n]}"

    def test_pexp_roundtrip(self):
        """PExp(PLog(f)) = f for f = M(q)."""
        N = 12
        mac = [Fraction(x) for x in macmahon_coefficients(N)]
        plog = plethystic_log(mac, N)
        reconstructed = plethystic_exp(plog, N)
        for n in range(N):
            assert reconstructed[n] == mac[n], f"PExp(PLog(M))[{n}] mismatch"

    def test_pexp_sum_n(self):
        """PExp(sum n q^n) = M(q)."""
        N = 12
        g = _fps_zero(N)
        for n in range(1, N):
            g[n] = Fraction(n)
        result = plethystic_exp(g, N)
        mac = [Fraction(x) for x in macmahon_coefficients(N)]
        for n in range(N):
            assert result[n] == mac[n]

    def test_pexp_24(self):
        """PExp(24 * sum q^n) = 1/eta^{24}."""
        N = 10
        g = _fps_zero(N)
        for n in range(1, N):
            g[n] = Fraction(24)
        result = plethystic_exp(g, N)
        expected = inverse_eta_24_coeffs(N)
        for n in range(N):
            assert result[n] == expected[n]


# ===========================================================================
# Suite 9: p_24(n) GROUND TRUTH
# ===========================================================================

class TestP24:
    """p_24(n) = chi(Hilb^n(K3)) ground truth (OEIS A006922)."""

    def test_p24_0(self):
        """p_24(0) = 1."""
        assert p_24(0) == 1

    def test_p24_1(self):
        """p_24(1) = 24 = chi(K3)."""
        assert p_24(1) == 24

    def test_p24_2(self):
        """p_24(2) = 324."""
        assert p_24(2) == 324

    def test_p24_3(self):
        """p_24(3) = 3200."""
        assert p_24(3) == 3200

    def test_p24_4(self):
        """p_24(4) = 25650."""
        assert p_24(4) == 25650

    def test_p24_5(self):
        """p_24(5) = 176256."""
        assert p_24(5) == 176256

    def test_p24_6(self):
        """p_24(6) = 1073720."""
        assert p_24(6) == 1073720

    def test_p24_negative(self):
        """p_24(n) = 0 for n < 0."""
        assert p_24(-1) == 0
        assert p_24(-5) == 0

    def test_p24_sum_formula(self):
        """p_24(1) = chi(K3) = 2 + 22 = 24 (from Hodge numbers)."""
        # b_0 + b_2 + b_4 = 1 + 22 + 1 = 24 (alternating: 1 - 0 + 22 - 0 + 1 = 24)
        assert p_24(1) == K3_EULER_CHAR


# ===========================================================================
# Suite 10: MASTER VERIFICATION
# ===========================================================================

class TestMasterVerification:
    """Full five-level consistency checks."""

    def test_c3_all_levels(self):
        """C^3: all five levels pass."""
        result = verify_categorical_dt_c3(10)
        assert result.level0_ok, "Level 0 failed"
        assert result.level1_ok, "Level 1 failed"
        assert result.level2_ok, "Level 2 failed"
        assert result.level3_ok, "Level 3 failed"
        assert result.level4_ok, "Level 4 failed"
        assert result.all_passed

    def test_k3_all_levels(self):
        """K3: all five levels pass."""
        result = verify_categorical_dt_k3(8)
        assert result.level0_ok, "Level 0 failed"
        assert result.level1_ok, "Level 1 failed"
        assert result.level2_ok, "Level 2 failed"
        assert result.level3_ok, "Level 3 failed"
        assert result.level4_ok, "Level 4 failed"
        assert result.all_passed

    def test_c3_nontrivial_checks(self):
        """C^3: verification has substantive checks (not vacuous)."""
        result = verify_categorical_dt_c3(10)
        assert result.n_checks >= 20

    def test_k3_nontrivial_checks(self):
        """K3: verification has substantive checks (not vacuous)."""
        result = verify_categorical_dt_k3(8)
        assert result.n_checks >= 15

    def test_full_summary(self):
        """Full summary: all geometries pass."""
        summary = full_categorical_dt_summary(8)
        assert summary['all_passed']
        assert summary['C3']['all_passed']
        assert summary['K3']['all_passed']
        assert summary['bridge']['K3_match']
        assert summary['bridge']['C3_match']

    def test_full_summary_check_count(self):
        """Full summary has a non-trivial number of total checks."""
        summary = full_categorical_dt_summary(8)
        assert summary['total_checks'] >= 30


# ===========================================================================
# Suite 11: AP COMPLIANCE
# ===========================================================================

class TestAPCompliance:
    """Verify compliance with Anti-Patterns."""

    def test_ap113_kappa_subscripts(self):
        """AP113: all kappa values are subscripted, never bare.

        kappa_ch(K3) = 2, kappa_BKM(K3xE) = 5,
        kappa_cat(K3) = 2, kappa_fiber(K3) = 24.
        """
        assert KAPPA_CH_K3 == Fraction(2)
        assert KAPPA_BKM_K3XE == Fraction(5)
        assert KAPPA_CAT_K3 == Fraction(2)
        assert KAPPA_FIBER_K3 == Fraction(24)

    def test_ap_cy6_d3_conditional(self):
        """AP-CY6: K3 x E wall-crossing is CONDITIONAL on CY-A_3."""
        wc = wall_crossing_k3xe()
        assert wc.status == "CONDITIONAL"

    def test_ap_cy8_bar_euler_requires_cya(self):
        """AP-CY8: bar Euler = DT requires CY-A.  K3 (d=2) is PROVED."""
        bridge = bar_euler_dt_bridge_k3(5)
        assert bridge.status == "PROVED"

    def test_ap_cy10_flop_preserves_kappa(self):
        """AP-CY10: flop preserves kappa_ch.  Conifold flop is derived equiv."""
        wc = wall_crossing_conifold()
        # Flop equivalence, NOT Koszul dual
        assert "flop" in wc.equivalence_types.get("flop wall", "").lower()
        assert "Koszul" not in wc.equivalence_types.get("flop wall", "")

    def test_ap155_not_novel_invariant(self):
        """AP155: the bar complex recovers KNOWN DT invariants via NEW path.

        p_24(n) is known (Goettsche 1990).  The bar complex path is new.
        """
        # The identification is: bar complex RECOVERS p_24, does not discover it.
        cat = categorical_dt_k3_rank0(5)
        for n in range(1, 5):
            # The euler chars equal known p_24 values
            assert cat.euler_chars[n] == p_24(n)

    def test_ap_cy7_coha_not_chiral(self):
        """AP-CY7: CoHA is associative, NOT chiral.  C^3 DT uses Y^+."""
        dt = numerical_dt_c3(5)
        # Dependencies mention CoHA identification, not direct chiral
        assert any("CoHA" in dep for dep in dt.dependencies)

    def test_ap_cy14_k3xe_not_theorem(self):
        """AP-CY14: K3 x E results use CONDITIONAL, not PROVED."""
        wc = wall_crossing_k3xe()
        assert wc.status != "PROVED"

    def test_k3_d2_proved_not_conditional(self):
        """K3 at d=2: status is PROVED (CY-A_2 is proved)."""
        cat = categorical_dt_k3_rank0(3)
        assert cat.status == "PROVED"
        dt = numerical_dt_k3_rank0(3)
        assert dt.status == "PROVED"


# ===========================================================================
# Suite 12: MACMAHON GROUND TRUTH
# ===========================================================================

class TestMacMahon:
    """MacMahon function M(q) ground truth (OEIS A000219)."""

    def test_first_11_values(self):
        """M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + 48q^6 + 86q^7 + 160q^8 + 282q^9 + 500q^{10}."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        mac = macmahon_coefficients(11)
        for n in range(11):
            assert mac[n] == expected[n], f"M[{n}] = {mac[n]}, expected {expected[n]}"

    def test_macmahon_positive(self):
        """All MacMahon coefficients are positive."""
        mac = macmahon_coefficients(20)
        for n in range(20):
            assert mac[n] > 0


# ===========================================================================
# Suite 13: FPS ARITHMETIC
# ===========================================================================

class TestFPSArithmetic:
    """Basic power series arithmetic."""

    def test_fps_mul_identity(self):
        """1 * f = f."""
        N = 8
        one = _fps_one(N)
        f = [Fraction(i) for i in range(N)]
        result = _fps_mul(one, f, N)
        for i in range(N):
            assert result[i] == f[i]

    def test_fps_inv_roundtrip(self):
        """f * (1/f) = 1."""
        N = 8
        f = [Fraction(1), Fraction(2), Fraction(3), Fraction(1),
             Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
        inv_f = _fps_inv(f, N)
        product = _fps_mul(f, inv_f, N)
        assert product[0] == Fraction(1)
        for i in range(1, N):
            assert product[i] == Fraction(0), f"f * inv(f) at q^{i} = {product[i]}"

    def test_fps_log_exp_roundtrip(self):
        """exp(log(f)) = f for f with f[0] = 1."""
        N = 8
        f = [Fraction(1), Fraction(3), Fraction(-1), Fraction(2),
             Fraction(0), Fraction(1), Fraction(0), Fraction(0)]
        log_f = _fps_log(f, N)
        exp_log_f = _fps_exp(log_f, N)
        for i in range(N):
            assert exp_log_f[i] == f[i], f"exp(log(f))[{i}] = {exp_log_f[i]}, expected {f[i]}"
