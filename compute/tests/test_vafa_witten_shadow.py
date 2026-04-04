r"""
Tests for Vafa-Witten invariants from the shadow tower.

Verifies:
    1. Z_VW on K3 for SU(2): eta^{-24}, Hilbert scheme chi, kappa, F_1
    2. S-duality = Koszul duality: SU(2) <-> SO(3), weight matching
    3. Modularity: weight = -chi(S)/2 for K3 and P^2
    4. P^2: mock modular from half-integer weight, shadow completion
    5. Higher rank SU(N) on K3: kappa scaling
    6. Instanton counting: chi(M_k) for SU(2) on K3
    7. Hilbert scheme: chi(Hilb^n(K3)) = coefficients of 1/eta^{24}
    8. Wall-crossing for P^2: binomial jumps, stability chambers

Ground truth:
    - Gottsche (1990): chi(Hilb^n(S)) from prod 1/(1-q^k)^{chi(S)}
    - Vafa-Witten (1994): S-duality, modularity, mock modularity
    - Yoshioka (1994): rank-2 moduli on K3
    - Manschot (2011): VW on P^2, mock modular forms
    - Tanaka-Thomas (2017): rigorous VW invariants for P^2
    - Gottsche-Kool (2020): virtual refinements

Manuscript references:
    Vol I: higher_genus_modular_koszul.tex (shadow tower, kappa, F_g)
    Vol III: k3_times_e.tex (K3 BKM, DMVV)
"""

import pytest
import sys
import os
import math
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.vafa_witten_shadow import (
    # Constants
    K3_CHI, K3_B2, K3_PG, K3_CHI_O,
    VW_WEIGHT_K3, KAPPA_K3_CHI, KAPPA_K3_B2,
    P2_CHI, P2_WEIGHT,
    KNOWN_HILB_K3, KNOWN_HILB,
    LANGLANDS_DUAL,
    # Functions: VW on K3
    vw_hilb_euler_k3,
    vw_modular_weight,
    vw_kappa_from_chi,
    vw_F1,
    # Functions: S-duality
    langlands_dual,
    s_duality_kappa_relation,
    su2_so3_s_duality_k3,
    # Functions: Modularity
    verify_modularity_weight,
    verify_eta24_weight,
    # Functions: P^2 mock modular
    mock_modular_shadow_weight,
    p2_vw_data,
    mock_modular_completion_integral,
    # Functions: Higher rank
    vw_su_n_on_k3_weight,
    vw_su_n_instanton_chi_k3,
    su_n_vw_kappa_k3,
    # Functions: Instanton counting
    instanton_euler_su2_k3,
    instanton_shadow_amplitude,
    # Functions: Hilbert scheme
    hilb_generating_function_surface,
    # Functions: Wall-crossing
    wall_crossing_chambers_p2,
    wall_crossing_jump_p2,
    # Functions: Verification
    verify_hilb_k3_equals_eta_inverse,
    verify_vw_weight_k3,
    verify_p2_mock_modular,
    verify_shadow_amplitude_consistency,
    verify_wall_crossing_pattern,
    # Functions: Bridge
    shadow_vw_bridge_k3,
    shadow_vw_bridge_p2,
    # Functions: Higher genus
    shadow_genus_g_amplitude,
    verify_shadow_genus_amplitudes,
    # Functions: Eta utilities
    eta_power_coeffs,
)


# =========================================================================
# 1. VW ON K3 FOR SU(2): Z = 1/eta^{24}
# =========================================================================

class TestVWK3SU2:
    """Z_VW(K3, SU(2)) = 1/eta(tau)^{24} and associated shadow data."""

    # 1a. K3 surface invariants
    def test_k3_euler_characteristic(self):
        """chi(K3) = 24."""
        assert K3_CHI == 24

    def test_k3_second_betti(self):
        """b_2(K3) = 22."""
        assert K3_B2 == 22

    def test_k3_geometric_genus(self):
        """p_g(K3) = h^{2,0}(K3) = 1."""
        assert K3_PG == 1

    def test_k3_holomorphic_euler(self):
        """chi(O_K3) = 2."""
        assert K3_CHI_O == 2

    # 1b. Hilbert scheme Euler characteristics
    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 24),
        (2, 324),
        (3, 3200),
        (4, 25650),
        (5, 176256),
    ])
    def test_hilb_euler_known(self, n, expected):
        """chi(Hilb^n(K3)) matches Gottsche's formula."""
        hilb = vw_hilb_euler_k3(n)
        assert hilb[n] == expected

    def test_hilb0_is_point(self):
        """chi(Hilb^0(K3)) = 1 (a single point)."""
        assert vw_hilb_euler_k3(0)[0] == 1

    def test_hilb1_is_chi_k3(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        assert vw_hilb_euler_k3(1)[1] == 24

    def test_hilb_all_positive(self):
        """All chi(Hilb^n(K3)) are positive for n >= 0."""
        hilb = vw_hilb_euler_k3(10)
        for n in range(11):
            assert hilb[n] > 0, f"chi(Hilb^{n}) = {hilb[n]} <= 0"

    def test_hilb_strictly_increasing(self):
        """chi(Hilb^n(K3)) strictly increases for n >= 1."""
        hilb = vw_hilb_euler_k3(8)
        for n in range(2, 9):
            assert hilb[n] > hilb[n-1]

    # 1c. kappa and F_1
    def test_kappa_k3_chi(self):
        """kappa = chi(K3) = 24 (Vol I: kappa(lattice rank r) = r)."""
        assert KAPPA_K3_CHI == Fraction(24)

    def test_kappa_k3_b2(self):
        """kappa from b_2 = 22 (H^2 lattice rank)."""
        assert KAPPA_K3_B2 == Fraction(22)

    def test_kappa_from_chi_function(self):
        """vw_kappa_from_chi(24) = 24."""
        assert vw_kappa_from_chi(24) == Fraction(24)

    def test_F1_with_kappa_24(self):
        """F_1 = kappa/24 = 24/24 = 1 for kappa = 24."""
        assert vw_F1(Fraction(24)) == Fraction(1)

    def test_F1_with_kappa_22(self):
        """F_1 = 22/24 = 11/12 for kappa = 22."""
        assert vw_F1(Fraction(22)) == Fraction(22, 24)

    def test_kappa_determines_eta_exponent(self):
        """kappa = chi(K3) = 24 = exponent of eta^{-24}."""
        assert KAPPA_K3_CHI == K3_CHI

    # 1d. Verification functions
    def test_verify_hilb_equals_eta_inverse(self):
        """Full verification: chi(Hilb^n(K3)) = coefficients of 1/eta^{24}."""
        result = verify_hilb_k3_equals_eta_inverse(6)
        assert result['all_pass']

    def test_verify_vw_weight_k3(self):
        """VW weight on K3 is -12."""
        result = verify_vw_weight_k3()
        assert result['match']


# =========================================================================
# 2. S-DUALITY = KOSZUL DUALITY
# =========================================================================

class TestSDualityKoszul:
    """S-duality (tau -> -1/tau) = Koszul duality (A <-> A!)."""

    def test_langlands_dual_su2(self):
        """SU(2)^v = SO(3)."""
        assert langlands_dual('SU(2)') == 'SO(3)'

    def test_langlands_dual_so3(self):
        """SO(3)^v = SU(2)."""
        assert langlands_dual('SO(3)') == 'SU(2)'

    def test_langlands_dual_e8(self):
        """E_8 is self-dual."""
        assert langlands_dual('E_8') == 'E_8'

    def test_langlands_dual_u1(self):
        """U(1) is self-dual."""
        assert langlands_dual('U(1)') == 'U(1)'

    def test_su2_so3_s_duality_data(self):
        """S-duality data for SU(2) <-> SO(3) on K3."""
        data = su2_so3_s_duality_k3()
        assert data['kappa_SU2'] == Fraction(24)
        assert data['kappa_SO3'] == Fraction(24)
        assert data['weight_SU2'] == Fraction(-12)
        assert data['weight_SO3'] == Fraction(-12)
        assert data['weights_match'] is True

    def test_kappa_relation_su2_so3(self):
        """kappa(SU(2)) = kappa(SO(3)) on K3 (same surface chi)."""
        rel = s_duality_kappa_relation(Fraction(24), Fraction(24))
        assert rel['same_weight'] is True
        assert rel['kappa_sum'] == Fraction(48)

    def test_s_duality_preserves_modular_weight(self):
        """S-duality maps weight-w forms to weight-w forms."""
        data = su2_so3_s_duality_k3()
        assert data['weight_SU2'] == data['weight_SO3']


# =========================================================================
# 3. MODULARITY: weight = -chi(S)/2
# =========================================================================

class TestModularity:
    """Z_VW has modular weight -chi(S)/2."""

    def test_weight_k3(self):
        """K3: chi=24, weight=-12."""
        assert vw_modular_weight(24) == Fraction(-12)

    def test_weight_p2(self):
        """P^2: chi=3, weight=-3/2."""
        assert vw_modular_weight(3) == Fraction(-3, 2)

    def test_weight_p1xp1(self):
        """P^1 x P^1: chi=4, weight=-2."""
        assert vw_modular_weight(4) == Fraction(-2)

    def test_weight_abelian_surface(self):
        """Abelian surface: chi=0, weight=0."""
        assert vw_modular_weight(0) == Fraction(0)

    def test_weight_enriques(self):
        """Enriques surface: chi=12, weight=-6."""
        assert vw_modular_weight(12) == Fraction(-6)

    def test_eta24_weight_verification(self):
        """Verify eta^{-24} has weight -12."""
        result = verify_eta24_weight()
        assert result['match']
        assert result['eta_neg24_weight'] == Fraction(-12)

    def test_k3_weight_matches_eta(self):
        """K3 VW weight = weight of eta^{-24}."""
        vw_wt = vw_modular_weight(K3_CHI)
        eta_wt = Fraction(-K3_CHI, 2)
        assert vw_wt == eta_wt == Fraction(-12)

    def test_weight_formula_is_minus_chi_over_2(self):
        """Generic verification: weight = -chi/2."""
        for chi in [0, 3, 4, 12, 24, 48]:
            assert vw_modular_weight(chi) == Fraction(-chi, 2)


# =========================================================================
# 4. P^2: MOCK MODULARITY FROM THE SHADOW
# =========================================================================

class TestP2MockModular:
    """VW on P^2 produces mock modular forms (half-integer weight)."""

    def test_p2_chi(self):
        """chi(P^2) = 3."""
        assert P2_CHI == 3

    def test_p2_weight_half_integer(self):
        """weight = -3/2 is half-integer."""
        assert P2_WEIGHT == Fraction(-3, 2)
        assert P2_WEIGHT.denominator == 2

    def test_p2_is_mock_modular(self):
        """Half-integer weight => mock modular form."""
        data = p2_vw_data()
        assert data['is_mock_modular'] is True
        assert data['weight_is_half_integer'] is True

    def test_p2_kappa(self):
        """kappa(P^2) = chi(P^2) = 3."""
        data = p2_vw_data()
        assert data['kappa'] == Fraction(3)

    def test_p2_F1(self):
        """F_1(P^2) = 3/24 = 1/8."""
        data = p2_vw_data()
        assert data['F_1'] == Fraction(1, 8)

    def test_mock_shadow_weight(self):
        """Shadow of weight -3/2 mock modular form has weight 7/2."""
        assert mock_modular_shadow_weight(Fraction(-3, 2)) == Fraction(7, 2)

    def test_mock_shadow_weight_formula(self):
        """shadow weight = 2 - k."""
        for k in [Fraction(-3, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(3, 2)]:
            assert mock_modular_shadow_weight(k) == Fraction(2) - k

    def test_p2_leading_coefficients(self):
        """Leading VW coefficients on P^2 (Manschot)."""
        data = p2_vw_data()
        lc = data['leading_coefficients']
        assert lc[0] == 3
        assert lc[1] == -6

    def test_mock_completion_integral(self):
        """The Eichler integral coefficients are computed."""
        shadow = {1: 1, 2: -1, 3: 2}
        eichler = mock_modular_completion_integral(shadow, 5)
        assert 1 in eichler
        assert eichler[1] == Fraction(1)  # 1 * 1/1

    def test_verify_p2_mock_modular(self):
        """Full verification of P^2 mock modularity."""
        result = verify_p2_mock_modular()
        assert result['is_half_integer'] is True
        assert result['is_mock_modular'] is True

    def test_integer_chi_gives_integer_weight(self):
        """Even chi gives integer weight (genuine modular)."""
        assert vw_modular_weight(24).denominator == 1
        assert vw_modular_weight(4).denominator == 1

    def test_odd_chi_gives_half_integer_weight(self):
        """Odd chi gives half-integer weight (mock modular)."""
        assert vw_modular_weight(3).denominator == 2
        assert vw_modular_weight(1).denominator == 2


# =========================================================================
# 5. HIGHER RANK SU(N) ON K3
# =========================================================================

class TestHigherRankK3:
    """SU(N) VW on K3 for N >= 2."""

    def test_su2_weight(self):
        """SU(2) on K3: weight = -12."""
        assert vw_su_n_on_k3_weight(2) == Fraction(-12)

    def test_su3_weight(self):
        """SU(3) on K3: weight = -12 (rank-1 sector)."""
        assert vw_su_n_on_k3_weight(3) == Fraction(-12)

    def test_su2_kappa_data(self):
        """SU(2) kappa data: rank-1 = 24, adjoint = 24*3 = 72."""
        data = su_n_vw_kappa_k3(2)
        assert data['N'] == 2
        assert data['dim_SU_N'] == 3
        assert data['kappa_rank1'] == Fraction(24)
        assert data['kappa_adjoint'] == Fraction(72)

    def test_su3_kappa_data(self):
        """SU(3) kappa data: rank-1 = 24, adjoint = 24*8 = 192."""
        data = su_n_vw_kappa_k3(3)
        assert data['N'] == 3
        assert data['dim_SU_N'] == 8
        assert data['kappa_rank1'] == Fraction(24)
        assert data['kappa_adjoint'] == Fraction(192)

    def test_su_n_dim(self):
        """dim(SU(N)) = N^2 - 1."""
        for N in [2, 3, 4, 5]:
            data = su_n_vw_kappa_k3(N)
            assert data['dim_SU_N'] == N * N - 1

    def test_su_n_adjoint_kappa_formula(self):
        """kappa_adj = (N^2-1) * chi = 24(N^2-1)."""
        for N in [2, 3, 4]:
            data = su_n_vw_kappa_k3(N)
            assert data['kappa_adjoint'] == Fraction(24 * (N * N - 1))

    def test_su1_rank1_instanton_chi(self):
        """SU(1) = rank 1: instanton chi = Hilbert scheme chi."""
        chi_inst = vw_su_n_instanton_chi_k3(1, 5)
        hilb = vw_hilb_euler_k3(5)
        for k in range(6):
            assert chi_inst[k] == hilb[k]


# =========================================================================
# 6. INSTANTON COUNTING: chi(M_k) FOR SU(2) ON K3
# =========================================================================

class TestInstantonCounting:
    """Euler characteristics of SU(2) instanton moduli on K3."""

    @pytest.mark.parametrize("k,expected", [
        (0, 1),
        (1, 24),
        (2, 324),
        (3, 3200),
    ])
    def test_instanton_chi_known(self, k, expected):
        """chi(M(2, k; K3)) matches known values."""
        chi_inst = instanton_euler_su2_k3(k)
        assert chi_inst[k] == expected

    def test_instanton_chi_matches_hilb(self):
        """chi(M(2, k; K3)) = chi(Hilb^k(K3)) in our convention."""
        chi_inst = instanton_euler_su2_k3(5)
        hilb = vw_hilb_euler_k3(5)
        for k in range(6):
            assert chi_inst[k] == hilb[k]

    def test_shadow_amplitude_matches_hilb_kappa24(self):
        """Shadow amplitude with kappa=24: prod 1/(1-q^n)^{24} = chi(Hilb^n(K3))."""
        kappa = Fraction(24)
        hilb = vw_hilb_euler_k3(5)
        for k in range(6):
            amp = instanton_shadow_amplitude(kappa, k)
            assert int(amp) == hilb[k], (
                f"Shadow amplitude at k={k}: {amp} != chi(Hilb^{k}) = {hilb[k]}"
            )

    def test_shadow_amplitude_k0(self):
        """Shadow amplitude at k=0 is 1 (empty instanton)."""
        assert instanton_shadow_amplitude(Fraction(24), 0) == Fraction(1)

    def test_shadow_amplitude_k1(self):
        """Shadow amplitude at k=1 is 24 = chi(K3)."""
        assert instanton_shadow_amplitude(Fraction(24), 1) == Fraction(24)

    def test_verify_shadow_consistency(self):
        """Full shadow amplitude consistency check."""
        result = verify_shadow_amplitude_consistency(5)
        assert result['all_pass']
        assert result['kappa'] == Fraction(24)


# =========================================================================
# 7. HILBERT SCHEME GENERATING FUNCTION
# =========================================================================

class TestHilbGenerating:
    """chi(Hilb^n(S)) = coefficients of prod 1/(1-q^k)^{chi(S)} (Gottsche)."""

    def test_hilb_k3_from_general(self):
        """chi(Hilb^n(K3)) from the general surface formula."""
        hilb_general = hilb_generating_function_surface(24, 5)
        hilb_k3 = vw_hilb_euler_k3(5)
        for n in range(6):
            assert hilb_general[n] == hilb_k3[n]

    def test_hilb_abelian_surface(self):
        """Abelian surface: chi = 0, so chi(Hilb^n) = delta_{n,0}."""
        hilb = hilb_generating_function_surface(0, 5)
        assert hilb[0] == 1
        for n in range(1, 6):
            assert hilb[n] == 0

    def test_hilb_p2_first_values(self):
        """chi(Hilb^n(P^2)) from prod 1/(1-q^k)^3."""
        hilb = hilb_generating_function_surface(3, 5)
        # prod 1/(1-q^k)^3: coefficients
        # q^0: 1
        # q^1: 3  (from 3 copies of 1/(1-q))
        # q^2: 9  (= 3 + 6 from partitions of 2 with weight 3)
        assert hilb[0] == 1
        assert hilb[1] == 3
        # For chi=3: 1/(1-q)^3 * 1/(1-q^2)^3 * ...
        # q^2 coeff = C(4,2) + 3 = 6 + 3 = 9? Let's check:
        # 1/(1-q)^3 = sum C(n+2,2) q^n = 1, 3, 6, 10, ...
        # multiplying by 1/(1-q^2)^3 at order q^2:
        # C(4,2) from (1-q)^{-3} alone = 6
        # plus 3 * 1 from (1-q^2)^{-3} contributing q^2 * (1-q)^{-3}|_{q^0}
        # = 6 + 3 = 9
        assert hilb[2] == 9

    def test_hilb_chi1(self):
        """chi = 1: chi(Hilb^n) = partition function p(n)."""
        hilb = hilb_generating_function_surface(1, 10)
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n in range(11):
            assert hilb[n] == expected[n], f"p({n}) = {hilb[n]}, expected {expected[n]}"

    def test_hilb_chi2(self):
        """chi = 2: prod 1/(1-q^k)^2."""
        hilb = hilb_generating_function_surface(2, 5)
        # 1/(1-q)^2 * 1/(1-q^2)^2 * ...
        # q^0: 1, q^1: 2, q^2: 5 (from 2+2+1), q^3: 10
        assert hilb[0] == 1
        assert hilb[1] == 2
        assert hilb[2] == 5

    def test_hilb_positive_for_positive_chi(self):
        """All chi(Hilb^n(S)) > 0 for chi(S) > 0."""
        for chi_S in [1, 3, 12, 24]:
            hilb = hilb_generating_function_surface(chi_S, 5)
            for n in range(6):
                assert hilb[n] > 0

    def test_known_hilb_k3_dict(self):
        """KNOWN_HILB_K3 matches computation."""
        hilb = vw_hilb_euler_k3(5)
        for n, expected in KNOWN_HILB_K3.items():
            if n <= 5:
                assert hilb[n] == expected


# =========================================================================
# 8. WALL-CROSSING FOR P^2 WITH SU(2)
# =========================================================================

class TestWallCrossingP2:
    """Wall-crossing for VW on P^2: binomial jumps and stability chambers."""

    def test_wall_crossing_data_exists(self):
        """wall_crossing_chambers_p2 returns data."""
        data = wall_crossing_chambers_p2()
        assert 'walls' in data
        assert 'jumps' in data
        assert data['mock_modular'] is True

    def test_wall_crossing_jump_k0(self):
        """Jump at wall 0: +1 (trivial connection)."""
        assert wall_crossing_jump_p2(0) == 1

    def test_wall_crossing_jump_k1(self):
        """Jump at wall 1: -3."""
        assert wall_crossing_jump_p2(1) == -3

    def test_wall_crossing_jump_k2(self):
        """Jump at wall 2: +6."""
        assert wall_crossing_jump_p2(2) == 6

    def test_wall_crossing_jump_k3(self):
        """Jump at wall 3: -10."""
        assert wall_crossing_jump_p2(3) == -10

    def test_wall_crossing_jump_k4(self):
        """Jump at wall 4: +15."""
        assert wall_crossing_jump_p2(4) == 15

    def test_wall_crossing_binomial_pattern(self):
        """Jumps follow |Delta Z_k| = C(k+2, 2) = (k+1)(k+2)/2."""
        for k in range(10):
            jump = wall_crossing_jump_p2(k)
            expected = ((-1) ** k) * (k + 1) * (k + 2) // 2
            assert jump == expected, f"k={k}: {jump} != {expected}"

    def test_wall_crossing_alternating_signs(self):
        """Jumps alternate in sign."""
        for k in range(10):
            jump = wall_crossing_jump_p2(k)
            if k % 2 == 0:
                assert jump > 0
            else:
                assert jump < 0

    def test_wall_crossing_abs_increasing(self):
        """Absolute values of jumps are strictly increasing."""
        for k in range(1, 10):
            assert abs(wall_crossing_jump_p2(k)) > abs(wall_crossing_jump_p2(k - 1))

    def test_verify_wall_crossing_pattern(self):
        """Full verification of wall-crossing pattern."""
        result = verify_wall_crossing_pattern(8)
        assert result['all_pass']


# =========================================================================
# 9. SHADOW TOWER: HIGHER GENUS AMPLITUDES
# =========================================================================

class TestShadowGenusAmplitudes:
    """F_g = kappa * lambda_g^{FP} from the shadow tower."""

    def test_F1_k3(self):
        """F_1(K3) = 12/24 = 1/2 for kappa = 12."""
        assert shadow_genus_g_amplitude(Fraction(12), 1) == Fraction(1, 2)

    def test_F2_k3(self):
        """F_2(K3) = kappa/240 = 12/240 = 1/20."""
        f2 = shadow_genus_g_amplitude(Fraction(12), 2)
        assert f2 == Fraction(12, 240)
        assert f2 == Fraction(1, 20)

    def test_F3_k3(self):
        """F_3(K3) = kappa * |B_6| / (6 * 4!) = 12/(42*144) = 12/6048 = 1/504."""
        f3 = shadow_genus_g_amplitude(Fraction(12), 3)
        assert f3 == Fraction(12, 6048)
        assert f3 == Fraction(1, 504)

    def test_F1_p2(self):
        """F_1(P^2) = (3/2)/24 = 1/16."""
        assert shadow_genus_g_amplitude(Fraction(3, 2), 1) == Fraction(1, 16)

    def test_Fg_positive(self):
        """All F_g > 0 for kappa > 0."""
        for g in range(1, 6):
            fg = shadow_genus_g_amplitude(Fraction(12), g)
            assert fg > 0, f"F_{g} = {fg} <= 0"

    def test_Fg_decreasing(self):
        """F_g decreases rapidly with g (Bernoulli number decay)."""
        kappa = Fraction(12)
        for g in range(2, 6):
            assert shadow_genus_g_amplitude(kappa, g) < shadow_genus_g_amplitude(kappa, g - 1)

    def test_Fg_linearity_in_kappa(self):
        """F_g is linear in kappa: F_g(2*kappa) = 2*F_g(kappa)."""
        for g in range(1, 5):
            fg1 = shadow_genus_g_amplitude(Fraction(6), g)
            fg2 = shadow_genus_g_amplitude(Fraction(12), g)
            assert fg2 == 2 * fg1

    def test_Fg_vanishes_for_kappa_zero(self):
        """F_g = 0 when kappa = 0."""
        for g in range(1, 5):
            assert shadow_genus_g_amplitude(Fraction(0), g) == Fraction(0)

    def test_verify_shadow_genus_amplitudes(self):
        """Full verification of shadow amplitudes."""
        result = verify_shadow_genus_amplitudes(Fraction(12), 4)
        assert 1 in result and 2 in result

    def test_F2_formula_explicit(self):
        """F_2 = kappa * |B_4| / (4 * 2!) = kappa * (1/30) / 8 = kappa/240."""
        kappa = Fraction(7)
        f2 = shadow_genus_g_amplitude(kappa, 2)
        assert f2 == kappa * Fraction(1, 240)

    def test_genus_raises_for_g0(self):
        """g = 0 raises ValueError."""
        with pytest.raises(ValueError):
            shadow_genus_g_amplitude(Fraction(12), 0)


# =========================================================================
# 10. ETA FUNCTION UTILITIES
# =========================================================================

class TestEtaUtilities:
    """eta(q)^N product expansion."""

    def test_eta_inverse_24_matches_hilb(self):
        """Coefficients of prod 1/(1-q^k)^{24} match Hilbert scheme chi."""
        coeffs = eta_power_coeffs(-24, 5)
        for n, expected in KNOWN_HILB_K3.items():
            if n <= 5:
                assert int(coeffs[n]) == expected

    def test_eta_24_first_coeffs(self):
        """prod (1-q^k)^{24}: the Ramanujan tau function (up to q-shift).

        Delta(q) = q * prod (1-q^n)^{24} = sum tau(n) q^n.
        So prod (1-q^n)^{24} = sum tau(n) q^{n-1}.
        Coefficients: q^0: 1, q^1: -24, q^2: 252, q^3: -1472, ...
        (these are tau(1), tau(2), tau(3), tau(4))
        """
        coeffs = eta_power_coeffs(24, 5)
        assert int(coeffs[0]) == 1
        assert int(coeffs[1]) == -24
        assert int(coeffs[2]) == 252
        assert int(coeffs[3]) == -1472

    def test_eta0_is_1(self):
        """eta^0 = 1."""
        coeffs = eta_power_coeffs(0, 5)
        assert coeffs[0] == Fraction(1)
        for n in range(1, 6):
            assert coeffs.get(n, Fraction(0)) == Fraction(0)

    def test_eta_inverse_1_is_partition_function(self):
        """1/eta = prod 1/(1-q^k) gives partition numbers."""
        coeffs = eta_power_coeffs(-1, 10)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n in range(11):
            assert int(coeffs[n]) == expected[n]


# =========================================================================
# 11. BRIDGE FUNCTIONS
# =========================================================================

class TestBridgeFunctions:
    """Shadow-VW bridge comprehensive tests."""

    def test_bridge_k3(self):
        """K3 bridge data is consistent."""
        data = shadow_vw_bridge_k3()
        assert data['chi'] == 24
        assert data['kappa'] == Fraction(24)
        assert data['F_1'] == Fraction(1)
        assert data['weight'] == Fraction(-12)
        assert data['eta_exponent'] == -24
        assert data['Z_first_5'][0] == 1
        assert data['Z_first_5'][1] == 24

    def test_bridge_p2(self):
        """P^2 bridge data is consistent."""
        data = shadow_vw_bridge_p2()
        assert data['chi'] == 3
        assert data['kappa'] == Fraction(3)
        assert data['F_1'] == Fraction(1, 8)
        assert data['weight'] == Fraction(-3, 2)
        assert data['is_mock_modular'] is True


# =========================================================================
# 12. CROSS-CONSISTENCY CHECKS
# =========================================================================

class TestCrossConsistency:
    """Cross-consistency between different computations."""

    def test_weight_equals_minus_kappa_over_2(self):
        """weight = -chi/2 and kappa = chi, so weight = -kappa/2."""
        for chi_S in [3, 4, 12, 24]:
            w = vw_modular_weight(chi_S)
            k = vw_kappa_from_chi(chi_S)
            assert w == -k / 2

    def test_eta_exponent_is_kappa(self):
        """The exponent N in eta^{-N} is N = kappa = chi."""
        for chi_S in [3, 4, 12, 24]:
            k = vw_kappa_from_chi(chi_S)
            assert k == chi_S

    def test_hilb_from_two_methods_agree(self):
        """vw_hilb_euler_k3 and hilb_generating_function_surface(24) agree."""
        h1 = vw_hilb_euler_k3(6)
        h2 = hilb_generating_function_surface(24, 6)
        for n in range(7):
            assert h1[n] == h2[n]

    def test_instanton_chi_from_two_methods(self):
        """instanton_euler_su2_k3 and vw_hilb_euler_k3 agree."""
        chi_inst = instanton_euler_su2_k3(5)
        hilb = vw_hilb_euler_k3(5)
        for k in range(6):
            assert chi_inst[k] == hilb[k]

    def test_F1_two_conventions(self):
        """F_1 differs between kappa = 12 and kappa = 11."""
        f1_12 = vw_F1(Fraction(12))
        f1_11 = vw_F1(Fraction(11))
        assert f1_12 == Fraction(1, 2)
        assert f1_11 == Fraction(11, 24)
        assert f1_12 != f1_11

    def test_shadow_amplitude_is_integer_for_k3(self):
        """Shadow amplitudes with kappa = 12 are integers (since 2*kappa = 24)."""
        for k in range(8):
            amp = instanton_shadow_amplitude(Fraction(12), k)
            assert amp.denominator == 1, f"Non-integer amplitude at k={k}: {amp}"
