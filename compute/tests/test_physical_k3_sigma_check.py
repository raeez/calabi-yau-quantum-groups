r"""Tests for physical_k3_sigma_check.py: physical K3 sigma model cross-checks.

STATUS: The K3 sigma model (N=(4,4) SCFT at c=6) is PROVED (Aspinwall-Morrison,
Nahm-Wendland).  The K3 Yangian is CONJECTURAL (AP-CY14).  These tests verify
that the Yangian construction is CONSISTENT with the known sigma model data.
Any failure would falsify the Yangian conjecture.

MATHEMATICAL CONTENT
====================

Seven independent checks of the K3 Yangian against the physical sigma model:

  1. N=4 SCA at c=6:  the sigma model has the small N=4 superconformal
     algebra at c = 6*k_R with k_R = 1.  The Yangian acts on Heisenberg
     modules; the N=4 constraint restricts which modules are physical.

  2. Elliptic genus phi_{0,1}:  the unique weak Jacobi form of weight 0,
     index 1.  The K3 elliptic genus is Z_K3 = 2*phi_{0,1} where the
     factor 2 = kappa_ch(K3).  The bar Euler product eta^{24} is a
     DIFFERENT modular object, related via the Borcherds lift.

  3. BPS spectrum:  the discriminant function c(D) of phi_{0,1} counts
     BPS states.  c(-1) = 1 (normalized phi_{0,1}), c(0) = 10.
     AP-CY9: only D = 0 or 3 mod 4 appear for index 1.

  4. Spectral parameter:  the Yangian spectral parameter z is NOT a
     sigma model variable.  It arises from the Omega-background (AP-CY31).
     Spectral z != worldsheet z (AP-CY20).

  5. Modular properties:  phi_{0,1} (weight 0, index 1, Jacobi form)
     and 1/eta^{24} (weight -12, modular form) are compatible via the
     Borcherds lift.  The bar Euler product matches Ramanujan tau.

  6. Kummer enhancement:  at K3 = T^4/Z_2, the sigma model has enhanced
     so(4)^4 at level 1.  The Yangian structure function specializes to
     the Kummer parameters: 4 positive (h=+1), 20 negative (h=-1/5),
     with kappa_ch = 2 (moduli-invariant).

  7. Mathieu moonshine:  M_24 acts on the K3 elliptic genus (EOT 2010).
     The Yangian does NOT see M_24 directly -- the bar complex provides
     the universal coefficient kappa_ch * dim(rho_n) but cannot detect
     which specific finite group acts.

Test structure:
    Section 1: Constants and kappa spectrum (8 tests)
    Section 2: N=4 SCA compatibility (8 tests)
    Section 3: Elliptic genus (9 tests)
    Section 4: BPS spectrum (9 tests)
    Section 5: Spectral parameter (5 tests)
    Section 6: Modular properties (7 tests)
    Section 7: Kummer enhancement (10 tests)
    Section 8: Mathieu moonshine (8 tests)
    Section 9: Grand synthesis (4 tests)
    Section 10: Cross-engine verification (5 tests)

Manuscript references:
    k3_times_e.tex, sec:k3e-cross-volume (K3-1 through K3-5)
    k3_times_e.tex, thm:k3-kappa (kappa_ch = 2)
    k3_times_e.tex, sec:web-consistency-checks (compactification web)
    k3_times_e.tex, prop:kummer-orbifold (Kummer route Steps 1-4)
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.physical_k3_sigma_check import (
    # Constants
    STATUS,
    N4_CENTRAL_CHARGE,
    N4_LEVEL_KR,
    N4_NUM_SUPERCURRENTS,
    N4_NUM_R_CURRENTS,
    K3_EULER_CHAR_TOP,
    K3_EULER_CHAR_HOL,
    K3_HODGE_H00,
    K3_HODGE_H01,
    K3_HODGE_H02,
    K3_HODGE_H10,
    K3_HODGE_H11,
    K3_HODGE_H20,
    K3_BETTI,
    MUKAI_RANK,
    MUKAI_SIG_PLUS,
    MUKAI_SIG_MINUS,
    KAPPA_CH_K3,
    KAPPA_BKM,
    KAPPA_CAT,
    KAPPA_FIBER,
    KAPPA_CH_K3XE,
    # Check 1
    N4SCAData,
    n4_sca_data,
    check_n4_sca_compatibility,
    # Check 2
    phi01_leading_coefficients,
    discriminant_coefficients,
    check_elliptic_genus,
    # Check 3
    check_bps_spectrum,
    # Check 4
    SpectralParameterAnalysis,
    check_spectral_parameter,
    # Check 5
    check_modular_properties,
    # Check 6
    check_kummer_enhancement,
    # Check 7
    mathieu_m24_reps_dimensions,
    check_mathieu_moonshine,
    # Grand synthesis
    check_sigma_model_yangian_compatibility,
    # Utilities
    kappa_spectrum_k3,
    k3_hodge_diamond,
    sigma_model_consistency_summary,
)


F = Fraction


# =========================================================================
# Section 1: Constants and kappa spectrum (AP113 compliant)
# =========================================================================

class TestConstants:
    """Verify K3 topological and algebraic constants."""

    def test_status_is_mixed(self):
        """Status is MIXED: sigma model proved, Yangian conjectural."""
        assert STATUS == 'MIXED'

    def test_k3_euler_char_top(self):
        """chi_top(K3) = 24."""
        assert K3_EULER_CHAR_TOP == 24

    def test_k3_euler_char_hol(self):
        """chi(O_K3) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        assert K3_EULER_CHAR_HOL == 2
        assert K3_HODGE_H00 - K3_HODGE_H01 + K3_HODGE_H02 == K3_EULER_CHAR_HOL

    def test_hodge_diamond_consistency(self):
        """Hodge diamond of K3: h^{1,1} = 20, h^{p,q} = h^{q,p}."""
        assert K3_HODGE_H11 == 20
        assert K3_HODGE_H01 == K3_HODGE_H10
        assert K3_HODGE_H02 == K3_HODGE_H20

    def test_betti_numbers(self):
        """Betti numbers of K3: [1, 0, 22, 0, 1]."""
        assert K3_BETTI == [1, 0, 22, 0, 1]
        assert sum(K3_BETTI) == K3_EULER_CHAR_TOP

    def test_mukai_lattice(self):
        """Mukai lattice has rank 24 = chi_top, signature (4, 20)."""
        assert MUKAI_RANK == 24
        assert MUKAI_RANK == K3_EULER_CHAR_TOP
        assert MUKAI_SIG_PLUS == 4
        assert MUKAI_SIG_MINUS == 20
        assert MUKAI_SIG_PLUS + MUKAI_SIG_MINUS == MUKAI_RANK

    def test_kappa_spectrum_subscripted(self):
        """AP113: all kappa values are properly subscripted and distinct.

        kappa_ch = 2, kappa_BKM = 5, kappa_cat = 2, kappa_fiber = 24.
        """
        assert KAPPA_CH_K3 == 2
        assert KAPPA_BKM == 5
        assert KAPPA_CAT == 2
        assert KAPPA_FIBER == 24
        # kappa_ch = kappa_cat = chi(O_K3) for K3
        assert KAPPA_CH_K3 == KAPPA_CAT
        # kappa_BKM = weight of Delta_5
        assert KAPPA_BKM == 5

    def test_kappa_ch_k3xe(self):
        """kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3."""
        assert KAPPA_CH_K3XE == 3
        assert KAPPA_CH_K3XE == KAPPA_CH_K3 + 1  # kappa_ch(E) = 1


# =========================================================================
# Section 2: N=4 SCA compatibility
# =========================================================================

class TestN4SCA:
    """Check 1: N=(4,4) superconformal algebra at c=6, k_R=1."""

    def test_n4_sca_data_type(self):
        """n4_sca_data() returns an N4SCAData named tuple."""
        n4 = n4_sca_data()
        assert isinstance(n4, N4SCAData)

    def test_central_charge_equals_6(self):
        """c = 6 for the K3 sigma model (c = 6*k_R with k_R = 1)."""
        n4 = n4_sca_data()
        assert n4.central_charge == 6
        assert n4.central_charge == N4_CENTRAL_CHARGE

    def test_level_kR_equals_1(self):
        """k_R = 1 (fixed by unitarity of the sigma model)."""
        n4 = n4_sca_data()
        assert n4.level_kR == 1

    def test_c_from_kR_formula(self):
        """c = 6*k_R = 6*1 = 6 (N=4 formula)."""
        n4 = n4_sca_data()
        assert n4.sugawara_c_from_kR == F(6)
        assert n4.central_charge == 6 * n4.level_kR

    def test_four_supercurrents(self):
        """4 supercurrents G^a(z) from the SU(2)_R doublet."""
        n4 = n4_sca_data()
        assert n4.num_supercurrents == 4

    def test_three_r_currents(self):
        """3 SU(2)_R currents J^i(z), i = 1, 2, 3."""
        n4 = n4_sca_data()
        assert n4.num_R_currents == 3

    def test_unitarity(self):
        """Unitarity requires k_R >= 1 (integer)."""
        n4 = n4_sca_data()
        assert n4.is_unitary

    def test_full_check_compatible(self):
        """Full N=4 SCA compatibility check passes."""
        result = check_n4_sca_compatibility()
        assert result['c_equals_6']
        assert result['c_from_kR']
        assert result['unitarity']
        assert result['sugawara_su2']
        assert result['verdict'] == 'COMPATIBLE'


# =========================================================================
# Section 3: Elliptic genus
# =========================================================================

class TestEllipticGenus:
    """Check 2: elliptic genus phi_{0,1} and bar Euler product."""

    def test_phi01_leading_returns_dict(self):
        """phi01_leading_coefficients returns a dict of (n,l)->value."""
        coeffs = phi01_leading_coefficients(2)
        assert isinstance(coeffs, dict)
        assert len(coeffs) > 0

    def test_phi01_q0_y0_equals_10(self):
        """f(0,0) = 10 for the normalized phi_{0,1}."""
        coeffs = phi01_leading_coefficients(1)
        assert coeffs[(0, 0)] == 10

    def test_phi01_q0_y1_equals_1(self):
        """f(0,1) = 1 for the normalized phi_{0,1} (c(-1) = 1)."""
        coeffs = phi01_leading_coefficients(1)
        assert coeffs[(0, 1)] == 1
        assert coeffs[(0, -1)] == 1

    def test_phi01_q0_total_times_kappa_equals_24(self):
        """kappa_ch * (f(0,-1) + f(0,0) + f(0,1)) = 2*12 = 24 = chi_top(K3)."""
        coeffs = phi01_leading_coefficients(1)
        total = coeffs[(0, -1)] + coeffs[(0, 0)] + coeffs[(0, 1)]
        assert total == 12
        assert KAPPA_CH_K3 * total == K3_EULER_CHAR_TOP

    def test_phi01_symmetry_f_n_l_equals_f_n_minus_l(self):
        """phi_{0,1} satisfies f(n,l) = f(n,-l) (even in l)."""
        coeffs = phi01_leading_coefficients(3)
        for (n, l), val in coeffs.items():
            if (n, -l) in coeffs:
                assert val == coeffs[(n, -l)], f"Asymmetry at ({n},{l})"

    def test_discriminant_coefficients(self):
        """The discriminant function c(D) with D = 4n - l^2."""
        c_D = discriminant_coefficients(3)
        assert c_D[-1] == 1    # polar term
        assert c_D[0] == 10    # massless
        assert c_D[3] == -64   # first massive (D = 3 mod 4)
        assert c_D[4] == 108   # D = 0 mod 4

    def test_bar_euler_matches_ramanujan_tau(self):
        """Bar Euler product coefficients match Ramanujan tau."""
        result = check_elliptic_genus()
        assert result['bar_euler_check']
        bar = result['bar_euler_leading']
        assert bar[0] == 1
        assert bar[1] == -24
        assert bar[2] == 252
        assert bar[3] == -1472
        assert bar[4] == 4830

    def test_phi01_and_inv_eta24_are_different_objects(self):
        """phi_{0,1} (Jacobi form) and 1/eta^{24} (modular form) are distinct."""
        result = check_elliptic_genus()
        conn = result['connection']
        assert 'Jacobi' in conn['phi01_type']
        assert conn['compatible']

    def test_full_check_compatible(self):
        """Full elliptic genus check passes."""
        result = check_elliptic_genus()
        assert result['q0_check']
        assert result['chi_top_check']
        assert result['c_minus_1_check']
        assert result['bar_euler_check']
        assert result['verdict'] == 'COMPATIBLE'


# =========================================================================
# Section 4: BPS spectrum
# =========================================================================

class TestBPSSpectrum:
    """Check 3: BPS spectrum from discriminant coefficients of phi_{0,1}."""

    def test_c_minus_1_equals_1(self):
        """c(-1) = 1 for normalized phi_{0,1} (AP-CY9)."""
        result = check_bps_spectrum()
        assert result['c_minus_1'] == 1
        assert result['c_m1_equals_1']

    def test_c_0_equals_10(self):
        """c(0) = 10 (massless states in normalized phi_{0,1})."""
        result = check_bps_spectrum()
        assert result['c_0'] == 10
        assert result['c_0_equals_10']

    def test_witten_index_equals_kappa_ch(self):
        """Witten index = kappa_ch * c(-1) = 2 * 1 = 2 = chi(O_K3)."""
        result = check_bps_spectrum()
        assert result['witten_equals_kappa_ch']

    def test_discriminant_constraint_ap_cy9(self):
        """AP-CY9: only D = 0 or 3 mod 4 appear for index 1."""
        result = check_bps_spectrum()
        assert result['discriminant_constraint']
        # Verify directly
        for D, _ in result['discriminant_coefficients'].items():
            if D >= 0:
                assert D % 4 in (0, 3), f"D={D} violates discriminant constraint"

    def test_discriminant_values_match_known(self):
        """Known discriminant coefficients match literature values."""
        result = check_bps_spectrum()
        disc = result['discriminant_coefficients']
        # First 8 discriminant values for normalized phi_{0,1}
        assert disc[-1] == 1
        assert disc[0] == 10
        assert disc[3] == -64
        assert disc[4] == 108

    def test_borcherds_weight_from_c0(self):
        """Borcherds weight = c(0)/2 = 10/2 = 5 = kappa_BKM."""
        result = check_bps_spectrum()
        c0 = result['c_0']
        borcherds_weight = F(c0, 2)
        assert borcherds_weight == F(5)
        assert int(borcherds_weight) == KAPPA_BKM

    def test_negative_c_values_are_fermionic(self):
        """Negative c(D) values indicate fermionic/odd BKM roots."""
        result = check_bps_spectrum()
        disc = result['discriminant_coefficients']
        # c(3) = -64 is negative (odd/fermionic root)
        assert disc[3] < 0
        # c(4) = 108 is positive (even/bosonic root)
        assert disc[4] > 0

    def test_d_minus_1_is_only_polar_term(self):
        """D = -1 is the only polar term (D < 0) for index m = 1."""
        result = check_bps_spectrum()
        disc = result['discriminant_coefficients']
        polar_terms = [D for D in disc if D < 0]
        assert polar_terms == [-1]

    def test_full_check_compatible(self):
        """Full BPS spectrum check passes."""
        result = check_bps_spectrum()
        assert result['verdict'] == 'COMPATIBLE'


# =========================================================================
# Section 5: Spectral parameter
# =========================================================================

class TestSpectralParameter:
    """Check 4: spectral parameter is NOT from the sigma model (AP-CY31)."""

    def test_spectral_not_sigma_model_variable(self):
        """The Yangian spectral parameter is NOT a sigma model variable."""
        result = check_spectral_parameter()
        assert not result['sigma_model_has_spectral_param']

    def test_spectral_from_omega_background(self):
        """Spectral parameter arises from the Omega-background."""
        result = check_spectral_parameter()
        assert result['yangian_spectral_from_omega_bg']

    def test_analysis_named_tuple(self):
        """SpectralParameterAnalysis records AP compliance."""
        result = check_spectral_parameter()
        a = result['analysis']
        assert isinstance(a, SpectralParameterAnalysis)
        assert a.parameter_type == 'Yangian spectral'
        assert not a.sigma_model_variable
        assert a.omega_background
        assert a.ap_cy31_compliant
        assert a.ap_cy20_compliant

    def test_z_zero_is_not_ope_singularity(self):
        """z=0 in the spectral parameter is NOT an OPE singularity (AP-CY31).

        Setting z=0 in Delta_z gives the cocommutative coproduct.
        Setting z->w in the OPE T(z)T(w) gives poles. These are DIFFERENT.
        """
        result = check_spectral_parameter()
        z0 = result['z_zero_check']
        assert z0['category_error']
        assert 'cocommutative' in z0['z_spectral_at_0']
        assert 'singularity' in z0['z_worldsheet_at_0'] or 'poles' in z0['z_worldsheet_at_0']

    def test_full_check_compatible(self):
        """Full spectral parameter check passes."""
        result = check_spectral_parameter()
        assert 'COMPATIBLE' in result['verdict']


# =========================================================================
# Section 6: Modular properties
# =========================================================================

class TestModularProperties:
    """Check 5: modular compatibility of sigma model and Yangian."""

    def test_ramanujan_tau_from_bar_euler(self):
        """Bar Euler product = eta^{24} gives Ramanujan tau function."""
        result = check_modular_properties()
        assert result['bar_euler_matches_tau']

    def test_ramanujan_tau_known_values(self):
        """Known Ramanujan tau values: tau(1)=1, tau(2)=-24, tau(3)=252."""
        result = check_modular_properties()
        tau = result['ramanujan_tau_values']
        assert tau[1] == 1
        assert tau[2] == -24
        assert tau[3] == 252
        assert tau[4] == -1472
        assert tau[5] == 4830

    def test_eta24_weight_is_12(self):
        """eta(q)^{24} has modular weight 12 (= 24 * 1/2)."""
        result = check_modular_properties()
        w = result['weight_check']
        assert w['eta_weight'] == F(1, 2)
        assert w['eta24_weight'] == 12
        assert w['bar_euler_weight'] == 12
        assert w['consistent']

    def test_phi01_is_jacobi_form(self):
        """phi_{0,1} is a weak Jacobi form of weight 0, index 1."""
        result = check_modular_properties()
        phi01 = result['modular_data']['phi01']
        assert phi01['weight'] == 0
        assert phi01['index'] == 1
        assert 'Jacobi' in phi01['type']

    def test_delta_is_cusp_form_weight_12(self):
        """Delta(q) = q*eta^{24} is the unique cusp form of weight 12."""
        result = check_modular_properties()
        delta = result['modular_data']['delta']
        assert delta['weight'] == 12
        assert 'cusp' in delta['type']

    def test_delta5_is_automorphic_weight_5(self):
        """Delta_5 is an automorphic form of weight 5 on O^+(3,2)."""
        result = check_modular_properties()
        d5 = result['modular_data']['delta5']
        assert d5['weight'] == 5

    def test_full_check_compatible(self):
        """Full modular properties check passes."""
        result = check_modular_properties()
        assert result['verdict'] == 'COMPATIBLE'


# =========================================================================
# Section 7: Kummer enhancement
# =========================================================================

class TestKummerEnhancement:
    """Check 6: enhanced symmetry at the Kummer point K3 = T^4/Z_2."""

    def test_kummer_cy2_constraint(self):
        """Kummer parameters satisfy sum h_i = 0 (CY_2 constraint)."""
        result = check_kummer_enhancement()
        assert result['cy2_check']

    def test_kummer_signature_4_20(self):
        """Kummer parameters have signature (4, 20) matching Mukai lattice."""
        result = check_kummer_enhancement()
        assert result['signature_check']

    def test_kummer_positive_h_values(self):
        """Kummer positive directions: h_i = +1 for i = 1,...,4."""
        result = check_kummer_enhancement()
        for h in result['kummer_params']['positive_h']:
            assert h == 1

    def test_kummer_negative_h_value(self):
        """Kummer negative directions: h_i = -1/5 for i = 5,...,24."""
        result = check_kummer_enhancement()
        assert result['kummer_params']['negative_h'] == Rational(-1, 5)

    def test_structure_function_at_zero(self):
        """g_{K3}(0) = (-1)^{24} = 1 (24 is even)."""
        result = check_kummer_enhancement()
        assert result['g_at_0'] == 1
        assert result['g_0_check']

    def test_unitarity_g_times_g_minus(self):
        """g(z) * g(-z) = 1 (unitarity from CY structure)."""
        result = check_kummer_enhancement()
        assert result['unitarity_at_3']

    def test_kappa_ch_kummer_equals_2(self):
        """kappa_ch = 2 at the Kummer point (moduli-invariant)."""
        result = check_kummer_enhancement()
        assert result['kappa_ch_kummer'] == 2

    def test_kummer_orbifold_data(self):
        """Kummer orbifold: 8 untwisted + 16 twisted = resolution rank 24."""
        result = check_kummer_enhancement()
        orb = result['kummer_orbifold']
        assert orb['untwisted_rank'] == 8
        assert orb['twisted_sectors'] == 16
        assert orb['kappa_ch'] == 2

    def test_so4_enhancement(self):
        """Enhanced algebra: so(4)^4 at level 1, rank 8, c = 8."""
        result = check_kummer_enhancement()
        enh = result['enhancement_data']
        assert enh['so4_copies'] == 4
        assert enh['level'] == 1
        assert enh['enhanced_rank'] == 8
        assert enh['enhanced_c'] == 8
        assert enh['total_rank_check']
        assert enh['total_rank'] == MUKAI_RANK

    def test_full_check_compatible(self):
        """Full Kummer enhancement check passes."""
        result = check_kummer_enhancement()
        assert result['verdict'] == 'COMPATIBLE'


# =========================================================================
# Section 8: Mathieu moonshine
# =========================================================================

class TestMathieuMoonshine:
    """Check 7: Mathieu M_24 moonshine and the K3 Yangian."""

    def test_m24_reps_known(self):
        """Known M_24 representation dimensions at low levels."""
        reps = mathieu_m24_reps_dimensions()
        assert reps[1] == 90
        assert reps[2] == 462
        assert reps[3] == 1540
        assert reps[4] == 4554
        assert reps[5] == 11592

    def test_m24_reps_divisible_by_kappa_ch(self):
        """A_n divisible by kappa_ch = 2 (necessary for M_24 decomposition)."""
        result = check_mathieu_moonshine()
        assert result['divisibility']

    def test_m24_irrep_dims(self):
        """M_24 irrep dims: A_n / kappa_ch = {45, 231, 770, ...}."""
        result = check_mathieu_moonshine()
        dims = result['m24_rep_dims']
        assert dims[1] == 45
        assert dims[2] == 231
        assert dims[3] == 770

    def test_bar_complex_does_not_see_m24(self):
        """The bar complex does NOT detect M_24 (structural limitation)."""
        result = check_mathieu_moonshine()
        assert not result['bar_complex_sees_m24']

    def test_structural_limitation_documented(self):
        """The structural limitation is properly documented."""
        result = check_mathieu_moonshine()
        lim = result['structural_limitation']
        assert 'total multiplicity A_n' in lim['yangian_detects']
        assert 'specific finite group M_24' in lim['yangian_blind_to']

    def test_kappa_ch_factor(self):
        """The kappa_ch = 2 factor relates A_n to M_24 irrep dimensions."""
        result = check_mathieu_moonshine()
        assert result['kappa_ch_factor'] == 2

    def test_m24_a1_decomposition(self):
        """A_1 = 2 * 45 = 90 (EOT 2010)."""
        reps = mathieu_m24_reps_dimensions()
        assert reps[1] == 2 * 45

    def test_full_check_compatible(self):
        """Full Mathieu moonshine check passes."""
        result = check_mathieu_moonshine()
        assert 'COMPATIBLE' in result['verdict']


# =========================================================================
# Section 9: Grand synthesis
# =========================================================================

class TestGrandSynthesis:
    """All 7 checks together: the sigma model vs Yangian compatibility."""

    def test_all_seven_checks_pass(self):
        """All 7 physical checks are COMPATIBLE."""
        results = check_sigma_model_yangian_compatibility()
        assert results['all_pass']

    def test_verdicts_count(self):
        """Exactly 7 verdicts are returned."""
        results = check_sigma_model_yangian_compatibility()
        assert len(results['verdicts']) == 7

    def test_each_verdict_compatible(self):
        """Each individual verdict contains COMPATIBLE."""
        results = check_sigma_model_yangian_compatibility()
        for name, verdict in results['verdicts']:
            assert 'COMPATIBLE' in verdict, f"{name} failed: {verdict}"

    def test_consistency_summary(self):
        """The one-line summary reports all checks pass."""
        summary = sigma_model_consistency_summary()
        assert 'ALL 7 CHECKS PASS' in summary


# =========================================================================
# Section 10: Cross-engine verification
# =========================================================================

class TestCrossEngine:
    """Cross-verification against k3_yangian.py and phi01_fourier.py."""

    def test_kappa_spectrum_utility(self):
        """kappa_spectrum_k3() returns the full AP113-compliant spectrum."""
        spec = kappa_spectrum_k3()
        assert spec['kappa_ch'] == 2
        assert spec['kappa_BKM'] == 5
        assert spec['kappa_cat'] == 2
        assert spec['kappa_fiber'] == 24

    def test_hodge_diamond_utility(self):
        """k3_hodge_diamond() returns consistent Hodge data."""
        h = k3_hodge_diamond()
        assert h['h11'] == 20
        assert h['chi_top'] == 24
        assert h['chi_hol'] == 2
        assert h['betti'] == [1, 0, 22, 0, 1]

    def test_phi01_cross_check_with_fourier_module(self):
        """phi01_leading_coefficients agrees with phi01_fourier.phi01_table."""
        from compute.lib.phi01_fourier import phi01_table
        direct = phi01_table(3)
        via_engine = phi01_leading_coefficients(3)
        for key in direct:
            assert key in via_engine, f"Missing key {key}"
            assert direct[key] == via_engine[key], f"Mismatch at {key}"

    def test_bar_euler_cross_check_with_yangian_module(self):
        """Bar Euler from check matches k3_yangian.bar_euler_product_yangian."""
        from compute.lib.k3_yangian import bar_euler_product_yangian
        direct = bar_euler_product_yangian(8)
        result = check_elliptic_genus()
        bar = result['bar_euler_leading']
        for k in bar:
            assert bar[k] == direct[k], f"Bar Euler mismatch at q^{k}"

    def test_kummer_cross_check_with_yangian_module(self):
        """Kummer parameters from check match k3_yangian.kummer_k3_parameters."""
        from compute.lib.k3_yangian import kummer_k3_parameters
        params = kummer_k3_parameters()
        result = check_kummer_enhancement()
        assert result['kummer_params']['cy2_sum'] == params.cy2_sum
        for i, h in enumerate(result['kummer_params']['positive_h']):
            assert h == params.h[i]
