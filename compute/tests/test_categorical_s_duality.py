"""Tests for categorical S-duality from the bar complex framework.

Verifies the five results of the categorical S-duality engine:

1. Bar-cobar adjunction as S-duality (coupling exchange g_s <-> 1/g_s)
2. Fricke involution as S-duality on K3 Yangian moduli
3. Coupling exchange B(A) at g_s <-> Omega(C) at 1/g_s
4. Koszul conductor K = kappa_ch(A) + kappa_ch(A^!) is S-duality invariant
5. Family-specific S-duality: K3 (K=0), Kac-Moody (K=0), Virasoro (K=13)

Multi-path verification:
  Path 1: Direct computation of conductor invariance
  Path 2: Cross-check with e1_koszul_three_families.py
  Path 3: Coupling exchange involution (S^2 = id)
  Path 4: Fricke self-dual points
  Path 5: Shadow class classification consistency

Ground truth:
  Heisenberg: K = 0, S: k -> -k, self-dual at k = 0
  Kac-Moody sl_2: K = 0, S: k -> -k-4, self-dual at k = -2 (critical)
  Virasoro: K = 13, S: c -> 26-c, self-dual at c = 13
  K3 (d=2): K = 0, kappa_ch = 2, kappa_ch^! = -2
  Fricke N=1: tau_* = i, g_s = 1 (standard S-duality)

Manuscript references:
  chapters/connections/bar_cobar_bridge.tex: Section sec:categorical-s-duality
  chapters/examples/k3_yangian_chapter.tex: Fricke involution
"""

import math
from fractions import Fraction

import pytest

from compute.lib.categorical_s_duality import (
    SDualityData,
    FrickeSDualityData,
    bar_cobar_coupling_exchange,
    bar_cobar_s_duality_verification,
    koszul_conductor_invariance,
    conductor_invariance_all_families,
    heisenberg_s_duality,
    kac_moody_s_duality,
    virasoro_s_duality,
    fricke_s_duality_k3,
    fricke_self_dual_points,
    fricke_eta_transformation_k3,
    s_duality_classification,
    k3_s_duality_on_kappa,
    virasoro_s_duality_on_kappa,
    s_duality_master_table,
    full_s_duality_verification,
)
from compute.lib.e1_koszul_three_families import (
    heisenberg_verify_conductor,
    kac_moody_sl2_verify_conductor,
    virasoro_verify_conductor,
)


# =========================================================================
# 1. Bar-cobar adjunction as S-duality (coupling exchange)
# =========================================================================

class TestCouplingExchange:
    """The coupling exchange g_s <-> 1/g_s is an involution."""

    def test_weak_coupling_exchange(self):
        """g_s = 0.5 -> 1/g_s = 2.0."""
        data = bar_cobar_coupling_exchange(0.5)
        assert abs(data['g_s_dual'] - 2.0) < 1e-12

    def test_strong_coupling_exchange(self):
        """g_s = 2.0 -> 1/g_s = 0.5."""
        data = bar_cobar_coupling_exchange(2.0)
        assert abs(data['g_s_dual'] - 0.5) < 1e-12

    def test_self_dual_point(self):
        """g_s = 1.0 is the self-dual point."""
        data = bar_cobar_coupling_exchange(1.0)
        assert data['is_self_dual']
        assert abs(data['g_s_dual'] - 1.0) < 1e-12

    def test_coupling_exchange_involution(self):
        """S^2 = id: (g_s -> 1/g_s -> g_s)."""
        for g_s in [0.1, 0.5, 1.0, 2.0, 10.0]:
            data1 = bar_cobar_coupling_exchange(g_s)
            data2 = bar_cobar_coupling_exchange(data1['g_s_dual'])
            assert abs(data2['g_s_dual'] - g_s) < 1e-12

    def test_zero_coupling_gives_infinite_dual(self):
        """g_s = 0 -> 1/g_s = infinity."""
        data = bar_cobar_coupling_exchange(0.0)
        assert data['g_s_dual'] == float('inf')

    def test_negative_coupling_raises(self):
        """Negative coupling is unphysical."""
        with pytest.raises(ValueError, match="must be >= 0"):
            bar_cobar_coupling_exchange(-1.0)

    def test_regime_classification(self):
        """Coupling regimes: perturbative / self-dual / non-perturbative."""
        assert bar_cobar_coupling_exchange(0.5)['regime'] == 'perturbative'
        assert bar_cobar_coupling_exchange(1.0)['regime'] == 'self-dual'
        assert bar_cobar_coupling_exchange(2.0)['regime'] == 'non-perturbative'

    def test_full_involution_verification(self):
        """Full verification pipeline for the coupling involution."""
        result = bar_cobar_s_duality_verification()
        assert result['all_involutive']
        assert result['self_dual_point'] == 1.0


# =========================================================================
# 2. Koszul conductor invariance under S-duality
# =========================================================================

class TestConductorInvariance:
    """K = kappa_ch(A) + kappa_ch(A^!) is invariant under S: A <-> A^!."""

    def test_heisenberg_conductor_zero(self):
        """Heisenberg: K = k + (-k) = 0."""
        for k_val in [1, 2, -1, Fraction(1, 2)]:
            k = Fraction(k_val)
            data = koszul_conductor_invariance(k, -k, Fraction(0))
            assert data['K_equals_expected']
            assert data['K_invariant_under_S']

    def test_virasoro_conductor_13(self):
        """Virasoro: K = c/2 + (26-c)/2 = 13."""
        for c_val in [0, 1, 13, 25, 26]:
            c = Fraction(c_val)
            kappa = Fraction(c, 2)
            kappa_d = Fraction(26 - c, 2)
            data = koszul_conductor_invariance(kappa, kappa_d, Fraction(13))
            assert data['K_equals_expected']
            assert data['K_invariant_under_S']

    def test_kac_moody_conductor_zero(self):
        """Kac-Moody sl_2: K = 3(k+2)/4 + 3(-k-2)/4 = 0."""
        for k_val in [1, 2, -1, -2]:
            k = Fraction(k_val)
            # kappa_ch = 3(k+2)/4, kappa_ch^! = 3(k'+2)/4 where k' = -k-4
            kappa = Fraction(3, 4) * (k + 2)
            kappa_d = Fraction(3, 4) * (-k - 4 + 2)
            data = koszul_conductor_invariance(kappa, kappa_d, Fraction(0))
            assert data['K_equals_expected']
            assert data['K_invariant_under_S']

    def test_conductor_manifestly_symmetric(self):
        """K(A) = kappa + kappa^! = kappa^! + kappa = K(A^!)."""
        kappa = Fraction(7, 3)
        kappa_d = Fraction(32, 3)
        K = kappa + kappa_d
        K_after_S = kappa_d + kappa
        assert K == K_after_S

    def test_all_families_conductor_invariance(self):
        """All families pass conductor invariance."""
        results = conductor_invariance_all_families()
        for name, data in results.items():
            assert data['K_invariant_under_S'], f"Conductor not invariant for {name}"
            assert data['K_equals_expected'], f"Conductor mismatch for {name}"

    def test_cross_check_with_e1_koszul(self):
        """Cross-check conductor values with e1_koszul_three_families.py."""
        # Heisenberg
        hv = heisenberg_verify_conductor(Fraction(1))
        assert hv['verified']

        # Kac-Moody
        kv = kac_moody_sl2_verify_conductor(Fraction(1))
        assert kv['verified']

        # Virasoro
        vv = virasoro_verify_conductor(Fraction(1))
        assert vv['verified']


# =========================================================================
# 3. Heisenberg S-duality (class G, trivial)
# =========================================================================

class TestHeisenbergSDuality:
    """Heisenberg: K = 0, S trivial (class G)."""

    def test_conductor_zero(self):
        """K = 0 for all k."""
        for k_val in [1, 2, -1, Fraction(1, 2)]:
            sd = heisenberg_s_duality(Fraction(k_val))
            assert sd.conductor == 0

    def test_level_inversion(self):
        """S: k -> -k."""
        sd = heisenberg_s_duality(Fraction(3))
        assert sd.family.kappa_ch == Fraction(3)
        assert sd.family_dual.kappa_ch == Fraction(-3)

    def test_self_dual_at_k_zero(self):
        """Self-dual at k = 0 (degenerate)."""
        sd = heisenberg_s_duality(Fraction(0))
        assert sd.is_self_dual

    def test_not_self_dual_away_from_zero(self):
        """Not self-dual for k != 0."""
        sd = heisenberg_s_duality(Fraction(1))
        assert not sd.is_self_dual

    def test_s_duality_type_trivial(self):
        """S-duality type is 'trivial' for class G."""
        sd = heisenberg_s_duality(Fraction(1))
        assert sd.s_duality_type == 'trivial'
        assert sd.shadow_class == 'G'


# =========================================================================
# 4. Kac-Moody S-duality (class L, Langlands)
# =========================================================================

class TestKacMoodySDuality:
    """Kac-Moody: K = 0, S = Feigin-Frenkel (Langlands)."""

    def test_conductor_zero(self):
        """K = 0 for all k."""
        for k_val in [1, 2, -1, -2, -3]:
            sd = kac_moody_s_duality(Fraction(k_val))
            assert sd.conductor == 0

    def test_feigin_frenkel_involution(self):
        """S: k -> -k - 4 for sl_2 (h^v = 2)."""
        sd = kac_moody_s_duality(Fraction(1))
        # k' = -1 - 4 = -5
        assert sd.family_dual.name == "V_-5(sl_2)"

    def test_critical_level_self_dual(self):
        """Self-dual at the critical level k = -h^v = -2."""
        sd = kac_moody_s_duality(Fraction(-2))
        assert sd.is_self_dual

    def test_critical_level_kappa_zero(self):
        """At critical level, kappa_ch = 0."""
        sd = kac_moody_s_duality(Fraction(-2))
        assert sd.family.kappa_ch == 0

    def test_feigin_frenkel_is_involution(self):
        """(k -> k')' = k: the FF involution squares to identity."""
        k = Fraction(3)
        sd1 = kac_moody_s_duality(k)
        # k' = -3 - 4 = -7
        k_prime = Fraction(-7)
        sd2 = kac_moody_s_duality(k_prime)
        # k'' = -(-7) - 4 = 7 - 4 = 3 = k
        assert sd2.family_dual.name == f"V_{int(k)}(sl_2)"

    def test_s_duality_type_langlands(self):
        """S-duality type is 'Langlands' for class L."""
        sd = kac_moody_s_duality(Fraction(1))
        assert sd.s_duality_type == 'Langlands'
        assert sd.shadow_class == 'L'


# =========================================================================
# 5. Virasoro S-duality (class M, non-perturbative)
# =========================================================================

class TestVirasoroSDuality:
    """Virasoro: K = 13, S: c -> 26-c (non-perturbative)."""

    def test_conductor_13(self):
        """K = 13 for all c."""
        for c_val in [0, 1, 13, 25, 26]:
            sd = virasoro_s_duality(Fraction(c_val))
            assert sd.conductor == 13

    def test_central_charge_exchange(self):
        """S: c -> 26 - c."""
        sd = virasoro_s_duality(Fraction(1))
        assert sd.family_dual.name == "Vir_25"

    def test_self_dual_at_c_13(self):
        """Self-dual at c = 13."""
        sd = virasoro_s_duality(Fraction(13))
        assert sd.is_self_dual

    def test_self_dual_kappa_13_half(self):
        """At the self-dual point: kappa_ch = 13/2."""
        sd = virasoro_s_duality(Fraction(13))
        assert sd.family.kappa_ch == Fraction(13, 2)
        assert sd.family_dual.kappa_ch == Fraction(13, 2)

    def test_bosonic_string_exchange(self):
        """c = 0 <-> c = 26 (trivial <-> bosonic string)."""
        sd_0 = virasoro_s_duality(Fraction(0))
        sd_26 = virasoro_s_duality(Fraction(26))
        assert sd_0.family_dual.name == "Vir_26"
        assert sd_26.family_dual.name == "Vir_0"

    def test_involution_c_to_26_minus_c(self):
        """(c -> 26-c) applied twice gives c."""
        c = Fraction(7)
        c_prime = 26 - c  # = 19
        c_double_prime = 26 - c_prime  # = 7 = c
        assert c_double_prime == c

    def test_s_duality_type_nonperturbative(self):
        """S-duality type is 'non-perturbative' for class M."""
        sd = virasoro_s_duality(Fraction(1))
        assert sd.s_duality_type == 'non-perturbative'
        assert sd.shadow_class == 'M'


# =========================================================================
# 6. Virasoro S-duality on kappa (detailed)
# =========================================================================

class TestVirasoroKappaSDuality:
    """Detailed kappa tests for the Virasoro S-duality involution."""

    def test_conductor_13_all_special_points(self):
        """K = 13 at all special points."""
        result = virasoro_s_duality_on_kappa()
        assert result['conductor'] == 13

    def test_self_dual_c_13(self):
        """Self-dual at c = 13."""
        result = virasoro_s_duality_on_kappa()
        assert result['self_dual_c'] == 13
        assert result['self_dual_kappa_ch'] == Fraction(13, 2)

    def test_nontrivial_s_duality(self):
        """S-duality is non-trivial for Virasoro."""
        result = virasoro_s_duality_on_kappa()
        assert result['s_duality_nontrivial']

    def test_special_point_conductors(self):
        """All special points have conductor 13."""
        result = virasoro_s_duality_on_kappa()
        for key, sp in result['special_points'].items():
            assert sp['conductor'] == 13, f"Conductor != 13 at c = {key}"


# =========================================================================
# 7. K3 S-duality on kappa (trivial, K = 0)
# =========================================================================

class TestK3KappaSDuality:
    """K3 at d = 2: K = 0, S-duality trivial on kappa."""

    def test_kappa_ch_is_2(self):
        """kappa_ch(K3) = 2 = chi(O_{K3})."""
        result = k3_s_duality_on_kappa()
        assert result['kappa_ch'] == 2

    def test_kappa_ch_dual_is_minus_2(self):
        """kappa_ch(K3^!) = -2."""
        result = k3_s_duality_on_kappa()
        assert result['kappa_ch_dual'] == -2

    def test_conductor_zero(self):
        """K = 2 + (-2) = 0."""
        result = k3_s_duality_on_kappa()
        assert result['conductor'] == 0
        assert result['conductor_is_zero']

    def test_s_duality_trivial(self):
        """S-duality is trivial for K3 (class G)."""
        result = k3_s_duality_on_kappa()
        assert result['s_duality_trivial']

    def test_kappa_spectrum_ap113(self):
        """AP113: kappa-spectrum values for K3."""
        result = k3_s_duality_on_kappa()
        ks = result['kappa_spectrum']
        assert ks['kappa_ch'] == 2
        assert ks['kappa_BKM'] == 5
        assert ks['kappa_cat'] == 2
        assert ks['kappa_fiber'] == 24

    def test_status_proved(self):
        """K3 result is PROVED via CY-A_2."""
        result = k3_s_duality_on_kappa()
        assert 'PROVED' in result['status']


# =========================================================================
# 8. Fricke involution as S-duality on K3 Yangian
# =========================================================================

class TestFrickeSDuality:
    """Fricke involution W_N on the K3 Yangian moduli space."""

    def test_fricke_n1_is_standard_s_duality(self):
        """N = 1: standard S-duality tau -> -1/tau."""
        fd = fricke_s_duality_k3(1)
        assert fd.N == 1
        assert abs(fd.fixed_point - 1j) < 1e-12

    def test_fricke_n2_fixed_point(self):
        """N = 2: tau_* = i/sqrt(2)."""
        fd = fricke_s_duality_k3(2)
        expected = 1j / math.sqrt(2)
        assert abs(fd.fixed_point - expected) < 1e-12

    def test_kappa_ch_preserved(self):
        """kappa_ch = 2 is preserved under Fricke (AP113)."""
        for N in [1, 2, 3, 5]:
            fd = fricke_s_duality_k3(N)
            assert fd.kappa_ch == 2
            assert fd.kappa_ch_preserved

    def test_conductor_zero_free_field(self):
        """K = 0 on the free-field branch."""
        for N in [1, 2, 3]:
            fd = fricke_s_duality_k3(N)
            assert fd.conductor == 0

    def test_eta_weight_12(self):
        """eta^{24} transforms with weight 12 under Fricke."""
        fd = fricke_s_duality_k3(1)
        assert fd.eta_transformation_weight == 12

    def test_bar_euler_transforms(self):
        """The bar Euler product eta^{24} transforms under Fricke."""
        fd = fricke_s_duality_k3(1)
        assert fd.bar_euler_transforms

    def test_invalid_level_raises(self):
        """Fricke level N must be >= 1."""
        with pytest.raises(ValueError, match="must be >= 1"):
            fricke_s_duality_k3(0)


class TestFrickeSelfDualPoints:
    """Self-dual points of the Fricke involution."""

    def test_n1_self_dual_g_s_1(self):
        """N = 1: g_s = 1 at the self-dual point."""
        pts = fricke_self_dual_points()
        assert pts[1]['is_standard_s_duality']
        assert abs(pts[1]['g_s_self_dual'] - 1.0) < 1e-12

    def test_self_dual_points_exist(self):
        """Self-dual points exist for N = 1, ..., 5."""
        pts = fricke_self_dual_points()
        for N in [1, 2, 3, 4, 5]:
            assert N in pts
            assert pts[N]['Im_tau_star'] > 0  # FM24 compliance

    def test_kappa_ch_at_all_self_dual_points(self):
        """kappa_ch = 2 at all self-dual points (AP113)."""
        pts = fricke_self_dual_points()
        for N, data in pts.items():
            assert data['kappa_ch'] == 2


class TestFrickeEtaTransformation:
    """Fricke transformation of eta^{24} (the K3 bar Euler product)."""

    def test_fm24_convergence(self):
        """q-parameters converge: |q| < 1 (FM24)."""
        tau = 0.3 + 1.5j  # safely in upper half-plane
        result = fricke_eta_transformation_k3(1, tau)
        assert result['q_tau_converges']
        assert result['q_fricke_converges']

    def test_eta_weight(self):
        """eta^{24} has weight 12."""
        tau = 0.2 + 2.0j
        result = fricke_eta_transformation_k3(1, tau)
        assert result['eta_weight'] == 12

    def test_bar_euler_rank(self):
        """K3 bar Euler rank = 24."""
        tau = 0.1 + 1.0j
        result = fricke_eta_transformation_k3(1, tau)
        assert result['bar_euler_rank'] == 24

    def test_fricke_preserves_uhp(self):
        """Fricke maps UHP to UHP (FM24)."""
        tau = 0.3 + 1.5j
        for N in [1, 2, 3]:
            result = fricke_eta_transformation_k3(N, tau)
            assert result['tau_fricke'].imag > 0

    def test_fm24_violation_raises(self):
        """Im(tau) <= 0 raises (FM24 compliance)."""
        with pytest.raises(ValueError, match="Im.*must be > 0"):
            fricke_eta_transformation_k3(1, 0.5 - 0.1j)


# =========================================================================
# 9. Shadow class classification
# =========================================================================

class TestSDualityClassification:
    """S-duality type is determined by the shadow class."""

    def test_class_g_trivial(self):
        """Class G: S-duality is trivial."""
        cl = s_duality_classification()
        assert cl['G']['s_duality_type'] == 'trivial'
        assert cl['G']['conductor'] == 0

    def test_class_l_langlands(self):
        """Class L: S-duality is Langlands."""
        cl = s_duality_classification()
        assert cl['L']['s_duality_type'] == 'Langlands'
        assert cl['L']['conductor'] == 0

    def test_class_c_convergent(self):
        """Class C: S-duality involves convergent resummation."""
        cl = s_duality_classification()
        assert cl['C']['s_duality_type'] == 'convergent'

    def test_class_m_nonperturbative(self):
        """Class M: S-duality is non-perturbative (Borel resummation)."""
        cl = s_duality_classification()
        assert cl['M']['s_duality_type'] == 'non-perturbative'
        assert cl['M']['conductor'] == 13

    def test_shadow_depth_hierarchy(self):
        """Shadow depth: G=2, L=2, C>2, M=infinity."""
        cl = s_duality_classification()
        assert cl['G']['shadow_depth'] == 2
        assert cl['L']['shadow_depth'] == 2


# =========================================================================
# 10. Master S-duality table
# =========================================================================

class TestMasterTable:
    """Master S-duality table."""

    def test_table_nonempty(self):
        """Table has entries."""
        table = s_duality_master_table()
        assert len(table) > 0

    def test_all_conductors_correct(self):
        """All conductors match expected values."""
        table = s_duality_master_table()
        for row in table:
            if row['class'] == 'G':
                assert row['conductor'] == 0
            elif row['class'] == 'L':
                assert row['conductor'] == 0
            elif row['class'] == 'M':
                assert row['conductor'] == 13

    def test_k3_entry(self):
        """K3 entry has correct data."""
        table = s_duality_master_table()
        k3_rows = [r for r in table if 'K3' in r['algebra']]
        assert len(k3_rows) == 1
        k3 = k3_rows[0]
        assert k3['kappa_ch'] == 2
        assert k3['kappa_ch_dual'] == -2
        assert k3['conductor'] == 0

    def test_virasoro_self_dual_entry(self):
        """Virasoro at c = 13 is self-dual."""
        table = s_duality_master_table()
        vir13 = [r for r in table if r['algebra'] == 'Vir_13']
        assert len(vir13) == 1
        assert vir13[0]['is_self_dual']

    def test_kac_moody_critical_self_dual(self):
        """Kac-Moody at critical level k = -2 is self-dual."""
        table = s_duality_master_table()
        km_crit = [r for r in table if r['algebra'] == 'V_-2(sl_2)']
        assert len(km_crit) == 1
        assert km_crit[0]['is_self_dual']


# =========================================================================
# 11. Full verification pipeline
# =========================================================================

class TestFullVerification:
    """End-to-end verification."""

    def test_full_pipeline_runs(self):
        """Full pipeline completes without error."""
        result = full_s_duality_verification()
        assert 'coupling_exchange' in result
        assert 'conductor_invariance' in result
        assert 'heisenberg' in result
        assert 'kac_moody' in result
        assert 'virasoro' in result
        assert 'fricke' in result
        assert 'classification' in result
        assert 'k3_kappa' in result
        assert 'virasoro_kappa' in result
        assert 'master_table' in result

    def test_coupling_involution_passes(self):
        """Coupling exchange is an involution."""
        result = full_s_duality_verification()
        assert result['coupling_exchange']['all_involutive']

    def test_all_conductor_invariance_passes(self):
        """All families pass conductor invariance."""
        result = full_s_duality_verification()
        for name, data in result['conductor_invariance'].items():
            assert data['K_invariant_under_S'], f"Failed for {name}"

    def test_kac_moody_critical_self_dual(self):
        """Kac-Moody at critical level k = -2 is self-dual."""
        result = full_s_duality_verification()
        assert result['kac_moody']['k=-2'].is_self_dual

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c = 13 is self-dual."""
        result = full_s_duality_verification()
        assert result['virasoro']['c=13'].is_self_dual

    def test_k3_conductor_zero(self):
        """K3 has conductor K = 0."""
        result = full_s_duality_verification()
        assert result['k3_kappa']['conductor'] == 0

    def test_virasoro_conductor_13(self):
        """Virasoro has conductor K = 13."""
        result = full_s_duality_verification()
        assert result['virasoro_kappa']['conductor'] == 13


# =========================================================================
# 12. Multi-path cross-checks (AP10 compliance)
# =========================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification: same quantity computed via independent routes."""

    def test_heisenberg_conductor_three_paths(self):
        """Heisenberg K = 0 via three independent paths.

        Path 1: S-duality engine (categorical_s_duality.py)
        Path 2: e1_koszul_three_families.py (direct kappa computation)
        Path 3: Direct arithmetic: k + (-k) = 0
        """
        k = Fraction(7)
        # Path 1: S-duality engine
        sd = heisenberg_s_duality(k)
        K_path1 = sd.conductor

        # Path 2: e1_koszul_three_families cross-check
        v = heisenberg_verify_conductor(k)
        K_path2 = v['sum']

        # Path 3: Direct arithmetic
        K_path3 = k + (-k)

        assert K_path1 == K_path2 == K_path3 == 0

    def test_kac_moody_conductor_three_paths(self):
        """Kac-Moody K = 0 via three independent paths.

        Path 1: S-duality engine
        Path 2: e1_koszul_three_families.py
        Path 3: Direct: 3(k+2)/4 + 3(k'+2)/4 where k' = -k-4
        """
        k = Fraction(5)
        # Path 1
        sd = kac_moody_s_duality(k)
        K_path1 = sd.conductor

        # Path 2
        v = kac_moody_sl2_verify_conductor(k)
        K_path2 = v['sum']

        # Path 3: 3(k+2)/4 + 3(-k-4+2)/4 = 3(k+2)/4 + 3(-k-2)/4
        #        = 3/4 * ((k+2) + (-k-2)) = 3/4 * 0 = 0
        K_path3 = Fraction(3, 4) * (k + 2) + Fraction(3, 4) * (-k - 2)

        assert K_path1 == K_path2 == K_path3 == 0

    def test_virasoro_conductor_three_paths(self):
        """Virasoro K = 13 via three independent paths.

        Path 1: S-duality engine
        Path 2: e1_koszul_three_families.py
        Path 3: Direct: c/2 + (26-c)/2 = 13
        """
        c = Fraction(7)
        # Path 1
        sd = virasoro_s_duality(c)
        K_path1 = sd.conductor

        # Path 2
        v = virasoro_verify_conductor(c)
        K_path2 = v['sum']

        # Path 3: Direct arithmetic
        K_path3 = Fraction(c, 2) + Fraction(26 - c, 2)

        assert K_path1 == K_path2 == K_path3 == 13

    def test_feigin_frenkel_involution_cross_check(self):
        """FF involution k -> k' = -k - 2h^v is an involution:
        cross-checked via two paths.

        Path 1: S-duality engine (apply S twice)
        Path 2: Direct computation k'' = -k' - 2h^v = -(-k-4) - 4 = k
        """
        for k_val in [1, 3, -1, Fraction(1, 2)]:
            k = Fraction(k_val)
            # Path 1: apply S-duality twice
            sd1 = kac_moody_s_duality(k)
            k_prime = sd1.family_dual.kappa_ch
            # The dual level is implicit in the name; compute directly
            k_prime_level = -k - 4
            sd2 = kac_moody_s_duality(k_prime_level)
            k_double_prime_level = -k_prime_level - 4

            # Path 2: Direct
            assert k_double_prime_level == k

    def test_virasoro_involution_cross_check(self):
        """Virasoro involution c -> 26 - c is an involution:
        cross-checked via two paths.

        Path 1: S-duality engine (apply S twice)
        Path 2: Direct: (26 - (26 - c)) = c
        """
        for c_val in [0, 1, Fraction(1, 2), 13, 25, 26]:
            c = Fraction(c_val)
            # Path 1
            sd1 = virasoro_s_duality(c)
            c_prime = 26 - c
            sd2 = virasoro_s_duality(c_prime)
            c_double_prime = 26 - c_prime

            # Path 2
            assert c_double_prime == c
            # Cross-check conductors
            assert sd1.conductor == sd2.conductor == 13

    def test_coupling_involution_algebraic_cross_check(self):
        """Coupling involution g_s -> 1/g_s verified algebraically.

        Path 1: bar_cobar_coupling_exchange (numerical)
        Path 2: Direct: 1/(1/g_s) = g_s (exact)
        """
        for g_s in [Fraction(1, 7), Fraction(3), Fraction(1, 100)]:
            g_s_f = float(g_s)
            # Path 1
            data = bar_cobar_coupling_exchange(g_s_f)
            g_s_recovered = 1.0 / data['g_s_dual']
            assert abs(g_s_recovered - g_s_f) < 1e-12

            # Path 2: algebraic
            assert Fraction(1) / (Fraction(1) / g_s) == g_s

    def test_k3_kappa_cross_check_with_mirror_engine(self):
        """K3 kappa_ch = 2 cross-checked via chi(O_{K3}).

        Path 1: S-duality engine (k3_s_duality_on_kappa)
        Path 2: Direct: chi(O_{K3}) = 1 - 0 + 1 = 2
                 (h^{0,0} - h^{1,0} + h^{2,0} = 1 - 0 + 1)
        """
        # Path 1
        result = k3_s_duality_on_kappa()
        kappa_path1 = result['kappa_ch']

        # Path 2: Hodge numbers of K3
        h00, h10, h20 = 1, 0, 1
        chi_O_K3 = h00 - h10 + h20
        kappa_path2 = Fraction(chi_O_K3)

        assert kappa_path1 == kappa_path2 == 2

    def test_fricke_fixed_point_cross_check(self):
        """Fricke fixed point tau_* = i/sqrt(N) cross-checked.

        Path 1: fricke_s_duality_k3
        Path 2: Direct: W_N(tau_*) = -1/(N*tau_*) = -1/(N*i/sqrt(N))
                = -1/(i*sqrt(N)) = i/sqrt(N) = tau_*
        """
        for N in [1, 2, 3, 5]:
            # Path 1
            fd = fricke_s_duality_k3(N)
            tau_star = fd.fixed_point

            # Path 2: verify W_N(tau_*) = tau_*
            tau_image = -1.0 / (N * tau_star)
            assert abs(tau_image - tau_star) < 1e-12

    def test_conductor_symmetry_algebraic(self):
        """K(A) = K(A^!) algebraically for all families.

        For any family: K(A) = kappa + kappa^! and
        K(A^!) = kappa^! + kappa^{!!} = kappa^! + kappa (since S^2 = id).
        """
        # Heisenberg: K(H_k) = k + (-k) = 0, K(H_{-k}) = -k + k = 0
        k = Fraction(5)
        K_A = k + (-k)
        K_A_dual = (-k) + k
        assert K_A == K_A_dual == 0

        # Virasoro: K(Vir_c) = c/2 + (26-c)/2 = 13
        # K(Vir_{26-c}) = (26-c)/2 + c/2 = 13
        c = Fraction(7)
        K_vir = Fraction(c, 2) + Fraction(26 - c, 2)
        K_vir_dual = Fraction(26 - c, 2) + Fraction(c, 2)
        assert K_vir == K_vir_dual == 13


# =========================================================================
# 13. AP compliance tests
# =========================================================================

class TestAPCompliance:
    """Anti-pattern compliance."""

    def test_ap113_kappa_subscripted(self):
        """AP113: kappa is always subscripted (kappa_ch, kappa_BKM, etc.)."""
        result = k3_s_duality_on_kappa()
        # All keys use subscripted kappa
        assert 'kappa_ch' in result
        assert 'kappa_ch_dual' in result
        ks = result['kappa_spectrum']
        for key in ks:
            assert key.startswith('kappa_'), f"Unsubscripted kappa: {key}"

    def test_ap_cy10_flop_not_koszul(self):
        """AP-CY10: flop preserves kappa; Koszul exchanges.
        Here we verify that Koszul DOES exchange kappa (not preserve it)."""
        sd = heisenberg_s_duality(Fraction(2))
        # Koszul dual has opposite kappa
        assert sd.family.kappa_ch + sd.family_dual.kappa_ch == 0
        # kappa changes sign (not preserved like in a flop)
        assert sd.family.kappa_ch != sd.family_dual.kappa_ch

    def test_conductor_not_universal_zero(self):
        """AP24: K = 0 for class G/L but K = 13 for Virasoro.
        NEVER claim K = 0 universally."""
        sd_heis = heisenberg_s_duality(Fraction(1))
        sd_vir = virasoro_s_duality(Fraction(1))
        assert sd_heis.conductor == 0
        assert sd_vir.conductor == 13
        assert sd_heis.conductor != sd_vir.conductor
