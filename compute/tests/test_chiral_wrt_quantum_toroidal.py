r"""Tests for chiral_wrt_quantum_toroidal.py: chiral Witten-Reshetikhin-Turaev
invariants from the K3 quantum toroidal algebra at root of unity.

STATUS: ALL results are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the construction, not its existence.

CENTRAL RESULTS (all conjectural):
    (1) Gauss sums |G(sigma, N)| = 1 for all sigma, N.
    (2) Z^{ch,ab}(K3; 2) = 4096 = 2^{12} = 2^{chi(K3)/2}.
    (3) |Z^{ch,ab}(K3; N)| = N^{12} for all N >= 2 (N^{chi/2} conjecture).
    (4) K3 x E: |Z^{ch}(K3 x E; N)| = N^{13} (product formula).
    (5) Phase at N=2 is trivial (from Mukai signature (4,20)).
    (6) Handle decomposition consistent with K3 topology.
    (7) 3d-6d dictionary has 8 entries.
    (8) Gottsche/VW comparison consistent at each level.

Test structure:
    Section 1: Gauss sums (6 tests)
    Section 2: K3 intersection data (4 tests)
    Section 3: N=2 explicit computation (6 tests)
    Section 4: N^{12} conjecture (5 tests)
    Section 5: K3 x E and Delta_5 (5 tests)
    Section 6: Phase analysis (4 tests)
    Section 7: 3d-6d dictionary (3 tests)
    Section 8: Gottsche/VW comparison (4 tests)
    Section 9: Programme status (3 tests)
    Section 10: Full verification (2 tests)

Total: 42 tests.

Manuscript references:
    chapters/theory/quantum_chiral_algebras.tex (sec:wrt-analogue)
    chapters/connections/k3_times_e.tex (conj:k3-quantum-toroidal)
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.chiral_wrt_quantum_toroidal import (
    # Constants
    STATUS,
    K3_CHI,
    K3_SIG,
    K3_B2,
    KAPPA_CH_K3,
    KAPPA_BKM_K3,
    KAPPA_CAT_K3,
    KAPPA_FIBER_K3,
    MUKAI_RANK,
    # Gauss sums
    gauss_sum_raw,
    gauss_sum_phase,
    gauss_phase_product,
    # Intersection data
    K3IntersectionData,
    k3_intersection_data,
    # Dictionary
    WRTDictionary,
    wrt_3d_6d_dictionary,
    # Abelian WRT
    abelian_chiral_wrt_k3,
    abelian_chiral_wrt_n2,
    # General N
    chiral_wrt_table,
    verify_n12_conjecture,
    # K3 x E
    chiral_wrt_k3xe,
    # Phase
    phase_analysis,
    # Gottsche/VW
    gottsche_vw_comparison,
    # Programme
    programme_status,
    # Full
    full_verification,
)

from compute.lib.handle_decomposition_fh import K3_BETTI


# =====================================================================
# Section 1: Gauss sums (6 tests)
# =====================================================================

class TestGaussSums:
    """Test the quadratic Gauss sums g(sigma, N) and their phases."""

    def test_gauss_raw_n2_values(self):
        """g(+1, 2) = 1+i, g(-1, 2) = 1-i (unnormalised)."""
        gp = gauss_sum_raw(+1, 2)
        gm = gauss_sum_raw(-1, 2)
        assert abs(gp - (1.0 + 1.0j)) < 1e-10
        assert abs(gm - (1.0 - 1.0j)) < 1e-10

    def test_gauss_phase_unit_modulus(self):
        """|phase(sigma, N)| = 1 for all N = 2, ..., 10 and sigma = +/- 1."""
        for N in range(2, 11):
            for sigma in [+1, -1]:
                p = gauss_sum_phase(sigma, N)
                assert abs(abs(p) - 1.0) < 1e-10, (
                    f"|phase({sigma}, {N})| = {abs(p)}, expected 1.0"
                )

    def test_gauss_phase_n2_values(self):
        """phase(+1, 2) = e^{i*pi/4}, phase(-1, 2) = e^{-i*pi/4}."""
        pp = gauss_sum_phase(+1, 2)
        pm = gauss_sum_phase(-1, 2)
        expected_p = cmath.exp(1j * math.pi / 4)
        expected_m = cmath.exp(-1j * math.pi / 4)
        assert abs(pp - expected_p) < 1e-10
        assert abs(pm - expected_m) < 1e-10

    def test_gauss_raw_conjugation(self):
        """g(-sigma, N) = conj(g(sigma, N)) for all N >= 2."""
        for N in range(2, 11):
            gp = gauss_sum_raw(+1, N)
            gm = gauss_sum_raw(-1, N)
            assert abs(gm - gp.conjugate()) < 1e-10, (
                f"g(-1, {N}) != conj(g(+1, {N}))"
            )

    def test_gauss_raw_squared_parity(self):
        """|g(+1, N)|^2 = N for even N, 1 for odd N (classical result)."""
        for N in range(2, 11):
            g = gauss_sum_raw(+1, N)
            g_sq = abs(g) ** 2
            if N % 2 == 0:
                assert abs(g_sq - N) < 1e-8, f"|g(+1,{N})|^2 = {g_sq}, expected {N}"
            else:
                assert abs(g_sq - 1.0) < 1e-8, f"|g(+1,{N})|^2 = {g_sq}, expected 1"

    def test_gauss_phase_product_mukai_trivial(self):
        """Gauss phase product over Mukai (4,20) is 1 for all N (sig=-16=0 mod 8)."""
        for N in range(2, 12):
            pp = gauss_phase_product(4, 20, N)
            assert abs(pp - 1.0) < 1e-10, (
                f"Phase product at N={N}: {pp}, expected 1.0"
            )

    def test_gauss_sum_invalid_N(self):
        """gauss_sum_raw raises for N < 2."""
        with pytest.raises(ValueError):
            gauss_sum_raw(+1, 1)
        with pytest.raises(ValueError):
            gauss_sum_raw(-1, 0)


# =====================================================================
# Section 2: K3 intersection data (4 tests)
# =====================================================================

class TestK3IntersectionData:
    """Test the K3 intersection form data."""

    def test_k3_rank(self):
        """K3 intersection form has rank 22."""
        data = k3_intersection_data()
        assert data.rank == 22

    def test_k3_signature(self):
        """K3 has signature (3, 19), total -16."""
        data = k3_intersection_data()
        assert data.sig_plus == 3
        assert data.sig_minus == 19
        assert data.signature == -16

    def test_k3_unimodular(self):
        """K3 lattice is unimodular (discriminant 1)."""
        data = k3_intersection_data()
        assert data.discriminant == 1

    def test_k3_lattice_type(self):
        """K3 lattice is 3U + 2E_8(-1)."""
        data = k3_intersection_data()
        assert '3U' in data.lattice_type
        assert 'E_8' in data.lattice_type


# =====================================================================
# Section 3: N=2 explicit computation (6 tests)
# =====================================================================

class TestN2Explicit:
    """Test the explicit N=2 chiral WRT computation via multiple paths."""

    def test_n2_is_4096(self):
        """Z^{ch,ab}(K3; 2) = 4096 = 2^{12}."""
        result = abelian_chiral_wrt_n2()
        assert result['is_4096'], (
            f"Z^{{ch,ab}}(K3; 2) = {result['z_ch_ab_n2_int']}, expected 4096"
        )

    def test_n2_is_integer(self):
        """Z^{ch,ab}(K3; 2) is an integer (vanishing imaginary part)."""
        result = abelian_chiral_wrt_n2()
        assert result['is_integer']

    def test_n2_phase_trivial(self):
        """Phase product at N=2 is trivial (= 1)."""
        result = abelian_chiral_wrt_n2()
        assert result['phase_is_one']

    def test_n2_gauss_raw_values(self):
        """Raw Gauss sums at N=2: g(+1)=1+i, g(-1)=1-i."""
        result = abelian_chiral_wrt_n2()
        assert result['gp_matches_expected']
        assert result['gm_matches_expected']

    def test_n2_handle_decomposition_path(self):
        """PATH 2: handle-by-handle decomposition gives 4096."""
        result = abelian_chiral_wrt_n2()
        assert result['decomposition']['handle_matches_4096']

    def test_n2_betti_path(self):
        """PATH 3: Betti-number product N^{sum b_k/2} gives 4096."""
        result = abelian_chiral_wrt_n2()
        assert result['betti_path']['betti_matches_4096']

    def test_n2_three_paths_agree(self):
        """Cross-check: all 3 computation paths give 4096."""
        result = abelian_chiral_wrt_n2()
        path1 = result['z_ch_ab_n2_int']                        # phase * magnitude
        path2 = result['decomposition']['handle_product_int']    # handle decomp
        path3 = result['betti_path']['betti_product_int']        # Betti product
        assert path1 == path2 == path3 == 4096, (
            f"Three paths disagree: {path1}, {path2}, {path3}"
        )

    def test_n2_chi_half_identity(self):
        """2^{chi(K3)/2} = 2^{12} = 4096 (cross-check with Euler char)."""
        # Path A: direct computation
        assert 2 ** (K3_CHI // 2) == 4096
        # Path B: from Betti numbers
        chi_from_betti = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        assert chi_from_betti == K3_CHI == 24
        assert 2 ** (chi_from_betti // 2) == 4096
        # Path C: from engine
        result = abelian_chiral_wrt_n2()
        assert result['z_ch_ab_n2_int'] == 2 ** (K3_CHI // 2)


# =====================================================================
# Section 4: N^{12} conjecture (5 tests)
# =====================================================================

class TestN12Conjecture:
    """Test |Z^{ch,ab}(K3; N)| = N^{12} for various N via multiple paths."""

    def test_n12_at_n2(self):
        """|Z^{ch,ab}(K3; 2)| = 2^{12} = 4096 (cross-check engine vs direct)."""
        result = abelian_chiral_wrt_k3(2)
        assert result['magnitude_matches']
        # Cross-check: engine value vs direct Python computation
        assert abs(result['z_ch_ab_abs'] - float(2 ** 12)) < 1e-6

    def test_n12_at_n3(self):
        """|Z^{ch,ab}(K3; 3)| = 3^{12} = 531441."""
        result = abelian_chiral_wrt_k3(3)
        assert result['magnitude_matches']
        assert abs(result['z_ch_ab_abs'] - float(3 ** 12)) < 1e-4

    def test_n12_at_n5(self):
        """|Z^{ch,ab}(K3; 5)| = 5^{12} = 244140625."""
        result = abelian_chiral_wrt_k3(5)
        assert result['magnitude_matches']
        assert abs(result['z_ch_ab_abs'] - float(5 ** 12)) < 1.0

    def test_n12_conjecture_range(self):
        """N^{12} conjecture holds for N = 2, ..., 8."""
        result = verify_n12_conjecture(8)
        assert result['all_pass'], (
            f"N^12 conjecture fails: {[d for d in result['data'] if not d['passes']]}"
        )

    def test_n12_exponent_is_chi_half(self):
        """The exponent 12 = chi(K3)/2 (two independent derivations)."""
        # Path A: chi(K3) = 24, half = 12
        assert K3_CHI // 2 == 12
        # Path B: sum of Betti numbers gives chi, then half
        chi = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        assert chi // 2 == 12
        # Path C: Mukai rank / 2 = 24 / 2 = 12
        assert MUKAI_RANK // 2 == 12
        result = verify_n12_conjecture(4)
        assert result['exponent'] == 12

    def test_n12_cross_check_handle_vs_phase(self):
        """Cross-check: N^{12} from handle product equals N^{12} from phase formula."""
        for N in [2, 3, 5, 7]:
            # Path 1: phase formula
            result = abelian_chiral_wrt_k3(N)
            z_phase = result['z_ch_ab_abs']
            # Path 2: handle product N^{b_0/2 + b_2/2 + b_4/2}
            handle_exp = sum(b / 2.0 for b in K3_BETTI)
            z_handle = N ** handle_exp
            assert abs(z_phase - z_handle) / z_handle < 1e-6, (
                f"N={N}: phase path {z_phase} != handle path {z_handle}"
            )


# =====================================================================
# Section 5: K3 x E and Delta_5 (5 tests)
# =====================================================================

class TestK3xE:
    """Test the K3 x E chiral WRT invariant and Delta_5 connection."""

    def test_k3xe_n13_at_n2(self):
        """|Z^{ch}(K3 x E; 2)| = 2^{13} = 8192 (cross-check vs direct)."""
        result = chiral_wrt_k3xe(2)
        assert result['magnitude_matches']
        assert abs(result['z_k3xe_abs'] - float(2 ** 13)) < 1e-4

    def test_k3xe_n13_at_n3(self):
        """|Z^{ch}(K3 x E; 3)| = 3^{13} = 1594323."""
        result = chiral_wrt_k3xe(3)
        assert result['magnitude_matches']
        assert abs(result['z_k3xe_abs'] - float(3 ** 13)) < 1.0

    def test_k3xe_factorisation(self):
        """Cross-check: Z^{ch}(K3 x E; N) = Z^{ch}(K3; N) * N (product formula)."""
        for N in range(2, 7):
            k3xe = chiral_wrt_k3xe(N)
            k3 = abelian_chiral_wrt_k3(N)
            z_product = abs(k3['z_ch_ab']) * N
            assert abs(k3xe['z_k3xe_abs'] - z_product) / z_product < 1e-8

    def test_k3xe_exponent_13(self):
        """The exponent 13 = chi(K3)/2 + 1 (two derivations)."""
        # Path A: from K3_CHI
        assert K3_CHI // 2 + 1 == 13
        # Path B: from Betti sum + 1
        chi = sum((-1)**k * b for k, b in enumerate(K3_BETTI))
        assert chi // 2 + 1 == 13

    def test_delta_5_connection_conjectural(self):
        """Delta_5 connection is correctly marked CONJECTURAL (AP-CY8)."""
        result = chiral_wrt_k3xe(3)
        assert 'CONJECTURAL' in result['delta_5_connection']['status']
        assert result['delta_5_connection']['kappa_BKM'] == KAPPA_BKM_K3


# =====================================================================
# Section 6: Phase analysis (4 tests)
# =====================================================================

class TestPhaseAnalysis:
    """Test the phase structure of Z^{ch,ab}(K3; N)."""

    def test_phase_n2_trivial(self):
        """Phase at N=2 is trivial (=1), from Mukai signature (4,20)."""
        result = phase_analysis(2)
        assert result['phase_is_trivial']

    def test_phase_signature(self):
        """The K3 signature sigma = -16 is correctly recorded."""
        result = phase_analysis(2)
        assert result['signature_K3'] == -16

    def test_phase_n_mod_8(self):
        """N mod 8 is correctly computed for phase classification."""
        for N in range(2, 11):
            result = phase_analysis(N)
            assert result['N_mod_8'] == N % 8

    def test_phase_bounded(self):
        """Phase angle is in [-pi, pi] for all N."""
        for N in range(2, 11):
            result = phase_analysis(N)
            assert -math.pi - 1e-10 <= result['total_phase_angle'] <= math.pi + 1e-10


# =====================================================================
# Section 7: 3d-6d dictionary (3 tests)
# =====================================================================

class TestDictionary:
    """Test the 3d-6d WRT dictionary."""

    def test_dictionary_length(self):
        """Dictionary has 8 entries (one per WRT ingredient)."""
        d = wrt_3d_6d_dictionary()
        assert len(d) == 8

    def test_dictionary_has_quantum_group(self):
        """Dictionary contains the quantum group entry."""
        d = wrt_3d_6d_dictionary()
        has_qg = any('Quantum group' in e.ingredient_3d for e in d)
        assert has_qg

    def test_dictionary_surgery_proved(self):
        """Handle decomposition entry is PROVED (topological result)."""
        d = wrt_3d_6d_dictionary()
        surgery = [e for e in d if 'Surgery' in e.ingredient_3d or 'Handle' in e.ingredient_6d]
        assert len(surgery) >= 1
        assert any('PROVED' in e.status_6d for e in surgery)


# =====================================================================
# Section 8: Gottsche/VW comparison (4 tests)
# =====================================================================

class TestGottscheVW:
    """Test the comparison with Gottsche and Vafa-Witten invariants."""

    def test_gottsche_p24_values(self):
        """Gottsche partition values p_{24}(n) at low n."""
        result = gottsche_vw_comparison(3)
        p24 = result['gottsche']['p24_values']
        assert p24[0] == 1
        assert p24[1] == 24
        assert p24[2] == 324

    def test_vw_weight(self):
        """VW modular weight = -chi(K3)/2 = -12."""
        result = gottsche_vw_comparison(2)
        assert result['vafa_witten']['weight'] == -12

    def test_truncated_partitions_at_n2(self):
        """Truncated 24-coloured partitions at N=2."""
        result = gottsche_vw_comparison(2)
        # At N=2, parts < 2, so only part size 1.
        # p_{24}^{<2}(0) = 1, p_{24}^{<2}(1) = 24
        dims = result['truncated_partitions']['p24_truncated']
        assert dims[0] == 1
        assert dims[1] == 24

    def test_chiral_wrt_matches_in_comparison(self):
        """Chiral WRT values match in the comparison."""
        result = gottsche_vw_comparison(2)
        assert result['chiral_wrt']['matches']


# =====================================================================
# Section 9: Programme status (3 tests)
# =====================================================================

class TestProgrammeStatus:
    """Test the programme status report."""

    def test_five_questions(self):
        """Programme status has exactly 5 questions."""
        status = programme_status()
        assert len(status) == 5

    def test_all_questions_have_status(self):
        """Each question has a status field."""
        status = programme_status()
        for key, val in status.items():
            assert 'status' in val, f"Question {key} missing status"

    def test_q1_conjectural(self):
        """Q1 (MTC existence) is CONJECTURAL."""
        status = programme_status()
        assert 'CONJECTURAL' in status['Q1_mtc']['status']


# =====================================================================
# Section 10: Full verification (2 tests)
# =====================================================================

class TestFullVerification:
    """Test the full verification suite."""

    def test_full_verification_passes(self):
        """Full verification passes at N_max = 6."""
        result = full_verification(N_max=6)
        assert result['all_pass'], (
            f"Full verification failed: "
            f"{[k for k, v in result.items() if isinstance(v, bool) and v is False]}"
        )

    def test_status_conjectural(self):
        """Engine status is CONJECTURAL (AP-CY14)."""
        result = full_verification(N_max=3)
        assert result['status'] == 'CONJECTURAL'

    def test_full_cross_check_n2_multiple_routes(self):
        """Cross-check: N=2 result from full_verification, abelian_chiral_wrt_n2,
        and abelian_chiral_wrt_k3 all agree on Z = 4096."""
        fv = full_verification(N_max=3)
        assert fv['n2_is_4096']
        n2 = abelian_chiral_wrt_n2()
        assert n2['z_ch_ab_n2_int'] == 4096
        k3 = abelian_chiral_wrt_k3(2)
        assert abs(k3['z_ch_ab_abs'] - 4096.0) < 1e-6
