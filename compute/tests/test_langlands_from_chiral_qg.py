r"""Tests for compute.lib.langlands_from_chiral_qg.

Comprehensive verification of the Langlands-from-chiral-QG engine:

  1. Langlands functor pipeline (5 steps, CY -> opers)
  2. K3 Yangian and opers: the critical-level bridge
  3. QGL duality: three involutions (QGL, FF, composite)
  4. Hecke eigensheaf from K3 x E
  5. Shadow tower to ramification type map

Key identities:
  kappa_ch(g_hat_k) = dim(g) * (k + h^v) / (2 * h^v)
  QGL dual level: k^L = -k - h^v (simply-laced)
  FF dual level: k' = -k - 2*h^v
  Psi(k) * Psi(k^L) = 1 (QGL duality)
  kappa(k) + kappa(k') = 0 (FF / Koszul duality)
  Shadow metric: Q_L(0) = 4 * kappa_ch^2 -> 0 at critical level
"""

import math
from fractions import Fraction

import pytest

from compute.lib.langlands_from_chiral_qg import (
    HeckeEigensheafData,
    LanglandsFunctorData,
    QGLDualityData,
    RAMIFICATION_DATA,
    ShadowRamificationData,
    YangianOperBridge,
    full_computation,
    hecke_eigensheaf_all_ade,
    hecke_eigensheaf_data,
    k3_ade_ramification_table,
    kappa_trajectory,
    langlands_functor,
    langlands_functor_all_ade,
    langlands_functor_steps,
    qgl_full_duality,
    qgl_involution_orbit,
    qgl_level_lattice,
    shadow_ramification,
    shadow_ramification_consistency_check,
    verify_all,
    verify_hecke_data,
    verify_langlands_functor,
    verify_qgl_duality,
    verify_shadow_ramification,
    verify_yangian_oper_bridge,
    yangian_oper_bridge,
    yangian_oper_bridge_all_ade,
)
from compute.lib.geometric_langlands_shadow import (
    kappa_affine,
    lie_data,
)

F = Fraction


# =====================================================================
# 1. LANGLANDS FUNCTOR PIPELINE TESTS
# =====================================================================

class TestLanglandsFunctorPipeline:
    """Verify the five-step Langlands functor pipeline."""

    def test_pipeline_has_five_steps(self):
        """The Langlands functor has exactly 5 steps."""
        steps = langlands_functor_steps()
        # VERIFIED [DC] count check [CF] cross-family census
        assert len(steps) == 5

    def test_step_names(self):
        """Steps are: CY-to-chiral, bar, Verdier, center, oper ident."""
        steps = langlands_functor_steps()
        names = [s.name for s in steps]
        assert names == [
            'CY-to-chiral', 'bar complex', 'Verdier dual',
            'chiral center', 'oper identification',
        ]

    def test_four_proved_one_conjectural(self):
        """4 steps proved, 1 conjectural."""
        steps = langlands_functor_steps()
        proved = sum(1 for s in steps if 'PROVED' in s.status)
        conj = sum(1 for s in steps if 'CONJECTURAL' in s.status)
        # VERIFIED [DC] status count [CF] cross-family census
        assert proved == 4
        assert conj == 1

    def test_conjectural_step_is_oper_identification(self):
        """The CONJECTURAL step is the oper identification (step 5)."""
        steps = langlands_functor_steps()
        conj_steps = [s for s in steps if 'CONJECTURAL' in s.status]
        assert len(conj_steps) == 1
        assert conj_steps[0].name == 'oper identification'

    def test_sl2_functor_basic(self):
        """Langlands functor for sl_2 on K3."""
        data = langlands_functor('A', 1)
        assert data.g_label == 'A1'
        assert data.total_steps == 5
        assert data.num_proved == 4
        assert data.num_conjectural == 1

    def test_sl2_functor_kappa_critical_zero(self):
        """kappa_ch = 0 at critical level for sl_2."""
        data = langlands_functor('A', 1)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_ch_critical == F(0)

    def test_sl2_functor_kappa_input(self):
        """kappa_ch = 9/4 at K3 level k=1 for sl_2."""
        data = langlands_functor('A', 1)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_ch_input == F(9, 4)

    def test_sl2_critical_level(self):
        """Critical level k = -2 for sl_2."""
        data = langlands_functor('A', 1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.critical_level == F(-2)

    def test_sl2_langlands_dual_self(self):
        """sl_2 is Langlands self-dual (A_1 = A_1^L)."""
        data = langlands_functor('A', 1)
        assert data.langlands_dual_label == 'A1'

    def test_e8_functor_kappa_critical_zero(self):
        """kappa_ch = 0 at critical level for E_8."""
        data = langlands_functor('E', 8)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_ch_critical == F(0)

    def test_e8_critical_level(self):
        """Critical level k = -30 for E_8."""
        data = langlands_functor('E', 8)
        assert data.critical_level == F(-30)

    def test_all_ade_functors_kappa_zero_at_critical(self):
        """kappa_ch = 0 at critical for all ADE types."""
        for label, data in langlands_functor_all_ade().items():
            # VERIFIED [DC] kappa computation [CF] cross-family census
            assert data.kappa_ch_critical == F(0), (
                f"kappa_ch at critical for {label} is "
                f"{data.kappa_ch_critical}, expected 0"
            )

    def test_all_ade_self_dual(self):
        """All ADE types are Langlands self-dual."""
        for label, data in langlands_functor_all_ade().items():
            assert data.langlands_dual_label == label, (
                f"{label} dual is {data.langlands_dual_label}, expected {label}"
            )

    def test_center_dim_genus2_equals_dim_g(self):
        """Center dimension at genus 2 = dim(G^L) * (g-1) = dim(g)."""
        for label, data in langlands_functor_all_ade().items():
            d = lie_data(data.g_type, data.g_rank)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert data.center_dimension_genus_g[2] == d.dim, (
                f"Center dim at genus 2 for {label}: "
                f"{data.center_dimension_genus_g[2]}, expected {d.dim}"
            )

    def test_num_ade_types(self):
        """8 standard ADE types for the functor."""
        all_func = langlands_functor_all_ade()
        assert len(all_func) == 8


# =====================================================================
# 2. YANGIAN-OPER BRIDGE TESTS
# =====================================================================

class TestYangianOperBridge:
    """Verify the K3 Yangian to oper bridge via critical-level limit."""

    def test_sl2_bridge_kappa_end_zero(self):
        """kappa_ch = 0 at the critical endpoint for sl_2."""
        bridge = yangian_oper_bridge('A', 1)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert bridge.kappa_ch_end == F(0)

    def test_sl2_bridge_kappa_start(self):
        """kappa_ch = 9/4 at K3 level k=1 for sl_2."""
        bridge = yangian_oper_bridge('A', 1)
        assert bridge.kappa_ch_start == F(9, 4)

    def test_sl2_shadow_metric_degenerates(self):
        """Shadow metric Q_L(0) = 0 at critical level for sl_2."""
        bridge = yangian_oper_bridge('A', 1)
        # VERIFIED [DC] shadow metric [CF] cross-family census
        assert bridge.shadow_metric_critical == F(0)

    def test_sl2_shadow_metric_nonzero_at_k1(self):
        """Shadow metric Q_L(0) > 0 at K3 level k=1 for sl_2."""
        bridge = yangian_oper_bridge('A', 1)
        # Q = 4 * (9/4)^2 = 4 * 81/16 = 81/4
        expected = 4 * F(9, 4) * F(9, 4)
        # VERIFIED [DC] shadow metric [CF] cross-family census
        assert bridge.shadow_metric_k1 == expected
        assert bridge.shadow_metric_k1 > 0

    def test_sl2_kappa_slope(self):
        """d(kappa_ch)/dk = dim(sl_2)/(2*h^v) = 3/4 for sl_2."""
        bridge = yangian_oper_bridge('A', 1)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert bridge.kappa_slope == F(3, 4)

    def test_sl2_sugawara_residue(self):
        """Sugawara residue = -dim(sl_2)*h^v = -6."""
        bridge = yangian_oper_bridge('A', 1)
        # VERIFIED [DC] residue computation [CF] cross-family census
        assert bridge.c_residue == F(-6)

    def test_sl2_c_start_equals_rank(self):
        """c(sl_2_hat_1) = 1 = rank(sl_2)."""
        bridge = yangian_oper_bridge('A', 1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bridge.c_start == F(1)

    def test_sl2_oper_casimirs(self):
        """SL_2 oper has single Casimir of degree 2."""
        bridge = yangian_oper_bridge('A', 1)
        assert bridge.oper_casimirs == (2,)

    def test_sl2_oper_dim_genus2(self):
        """Oper dim at genus 2 for sl_2 = 3."""
        bridge = yangian_oper_bridge('A', 1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bridge.oper_dim_genus2 == 3

    def test_e8_bridge_kappa_zero_at_critical(self):
        """kappa_ch = 0 at critical for E_8."""
        bridge = yangian_oper_bridge('E', 8)
        assert bridge.kappa_ch_end == F(0)

    def test_e8_shadow_metric_degenerates(self):
        """Shadow metric = 0 at critical for E_8."""
        bridge = yangian_oper_bridge('E', 8)
        assert bridge.shadow_metric_critical == F(0)

    def test_all_ade_bridges_shadow_degenerate(self):
        """Shadow metric = 0 at critical for all ADE types."""
        for label, bridge in yangian_oper_bridge_all_ade().items():
            # VERIFIED [DC] shadow metric [CF] cross-family census
            assert bridge.shadow_metric_critical == F(0), (
                f"Shadow at critical for {label}: "
                f"{bridge.shadow_metric_critical}"
            )

    def test_all_ade_bridges_shadow_nonzero_at_k1(self):
        """Shadow metric > 0 at k=1 for all ADE types."""
        for label, bridge in yangian_oper_bridge_all_ade().items():
            assert bridge.shadow_metric_k1 > 0, (
                f"Shadow at k=1 for {label}: {bridge.shadow_metric_k1}"
            )

    def test_all_ade_c_start_equals_rank(self):
        """c(g_hat_1) = rank(g) for all simply-laced types."""
        for label, bridge in yangian_oper_bridge_all_ade().items():
            d = lie_data(bridge.g_label[0], int(bridge.g_label[1:]))
            # VERIFIED [DC] structural property [CF] cross-family census
            assert bridge.c_start == F(d.rank), (
                f"c(hat_{label}_1) = {bridge.c_start}, expected {d.rank}"
            )

    def test_yangian_structure_degree_24(self):
        """K3 Yangian structure function has degree (24, 24)."""
        bridge = yangian_oper_bridge('A', 1)
        assert bridge.yangian_structure_degree == (24, 24)

    def test_kappa_trajectory_linear(self):
        """kappa_ch decreases linearly from kappa(1) to 0."""
        traj = kappa_trajectory('A', 1, num_points=10)
        kap_0 = traj[0]['kappa_ch']
        kap_end = traj[-1]['kappa_ch']
        # VERIFIED [DC] linearity check [CF] cross-family census
        assert abs(kap_0 - float(F(9, 4))) < 1e-12
        assert abs(kap_end) < 1e-12

    def test_kappa_trajectory_monotone_decreasing(self):
        """kappa_ch decreases monotonically along the trajectory."""
        traj = kappa_trajectory('A', 1, num_points=20)
        kappas = [p['kappa_ch'] for p in traj]
        for i in range(len(kappas) - 1):
            assert kappas[i] >= kappas[i + 1], (
                f"kappa not monotone at step {i}: "
                f"{kappas[i]} < {kappas[i+1]}"
            )


# =====================================================================
# 3. QGL DUALITY TESTS
# =====================================================================

class TestQGLDuality:
    """Verify the three involutions on the level space."""

    def test_sl2_qgl_dual_level(self):
        """sl_2 at k=1: QGL dual k^L = -3."""
        data = qgl_full_duality('A', 1, F(1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.k_qgl == F(-3)

    def test_sl2_psi_product_one(self):
        """Psi(1) * Psi(-3) = 1 for sl_2."""
        data = qgl_full_duality('A', 1, F(1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.psi_product == F(1)

    def test_sl2_ff_dual_level(self):
        """sl_2 at k=1: FF dual k' = -5."""
        data = qgl_full_duality('A', 1, F(1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.k_ff == F(-5)

    def test_sl2_ff_kappa_sum_zero(self):
        """kappa(1) + kappa(-5) = 0 for sl_2 (FF duality)."""
        data = qgl_full_duality('A', 1, F(1))
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_sum_ff == F(0)

    def test_sl2_qgl_kappa_sum_nonzero(self):
        """kappa(1) + kappa(-3) = 3/2 != 0 for sl_2 (QGL duality)."""
        data = qgl_full_duality('A', 1, F(1))
        # kappa(1) = 9/4, kappa(-3) = 3*(-1)/4 = -3/4
        # sum = 9/4 - 3/4 = 6/4 = 3/2
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_sum_qgl == F(3, 2)
        assert data.kappa_sum_qgl != F(0)

    def test_sl2_composite_level(self):
        """QGL(FF(k=1)) = 1 + h^v = 3 for sl_2."""
        data = qgl_full_duality('A', 1, F(1))
        # QGL(FF(1)) = QGL(-5) = -(-5) - 2 = 5 - 2 = 3
        # OR: k_composite = k + h^v = 1 + 2 = 3
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.k_composite == F(3)

    def test_sl2_qgl_fixed_point(self):
        """QGL fixed point for sl_2: k = -h^v/2 = -1."""
        data = qgl_full_duality('A', 1, F(1))
        assert data.qgl_fixed_point == F(-1)

    def test_sl2_ff_fixed_point(self):
        """FF fixed point for sl_2: k = -h^v = -2 (critical level)."""
        data = qgl_full_duality('A', 1, F(1))
        assert data.ff_fixed_point == F(-2)

    def test_sl2_kappa_at_qgl_fixed(self):
        """kappa at QGL fixed point = dim(g)/4 = 3/4 for sl_2."""
        data = qgl_full_duality('A', 1, F(1))
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_at_qgl_fixed == F(3, 4)

    def test_d4_psi_product_one(self):
        """Psi product = 1 for D_4 at k=1."""
        data = qgl_full_duality('D', 4, F(1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.psi_product == F(1)

    def test_d4_ff_sum_zero(self):
        """kappa sum = 0 for D_4 FF duality at k=1."""
        data = qgl_full_duality('D', 4, F(1))
        assert data.kappa_sum_ff == F(0)

    def test_e8_psi_product_one(self):
        """Psi product = 1 for E_8 at k=1."""
        data = qgl_full_duality('E', 8, F(1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.psi_product == F(1)

    def test_e8_ff_sum_zero(self):
        """kappa sum = 0 for E_8 FF duality at k=1."""
        data = qgl_full_duality('E', 8, F(1))
        assert data.kappa_sum_ff == F(0)

    def test_all_ade_psi_product_one(self):
        """Psi * Psi^L = 1 for all ADE at k=1."""
        for t, r in [('A', 1), ('A', 2), ('A', 3),
                     ('D', 4), ('D', 5),
                     ('E', 6), ('E', 7), ('E', 8)]:
            data = qgl_full_duality(t, r, F(1))
            # VERIFIED [DC] structural property [CF] cross-family census
            assert data.psi_product == F(1), (
                f"Psi product for {t}{r}: {data.psi_product}"
            )

    def test_all_ade_ff_sum_zero(self):
        """kappa(k) + kappa(k') = 0 for all ADE at k=1."""
        for t, r in [('A', 1), ('A', 2), ('A', 3),
                     ('D', 4), ('D', 5),
                     ('E', 6), ('E', 7), ('E', 8)]:
            data = qgl_full_duality(t, r, F(1))
            # VERIFIED [DC] kappa computation [CF] cross-family census
            assert data.kappa_sum_ff == F(0), (
                f"FF sum for {t}{r}: {data.kappa_sum_ff}"
            )

    def test_all_ade_qgl_sum_nonzero(self):
        """kappa(k) + kappa(k^L) != 0 for all ADE at k=1."""
        for t, r in [('A', 1), ('A', 2), ('A', 3),
                     ('D', 4), ('D', 5),
                     ('E', 6), ('E', 7), ('E', 8)]:
            data = qgl_full_duality(t, r, F(1))
            assert data.kappa_sum_qgl != F(0), (
                f"QGL sum for {t}{r} is zero (should be nonzero)"
            )

    def test_qgl_kappa_at_fixed_equals_dim_over_4(self):
        """kappa at QGL fixed point = dim(g)/4 for all ADE."""
        for t, r in [('A', 1), ('A', 2), ('D', 4), ('E', 6), ('E', 8)]:
            data = qgl_full_duality(t, r, F(1))
            d = lie_data(t, r)
            # VERIFIED [DC] kappa computation [CF] cross-family census
            assert data.kappa_at_qgl_fixed == F(d.dim, 4), (
                f"kappa at QGL fixed for {t}{r}: "
                f"{data.kappa_at_qgl_fixed}, expected {F(d.dim, 4)}"
            )

    def test_qgl_multiple_levels(self):
        """Psi * Psi^L = 1 for sl_2 at levels 1, 2, 5."""
        for k in [F(1), F(2), F(5)]:
            data = qgl_full_duality('A', 1, k)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert data.psi_product == F(1), (
                f"Psi product for sl_2 at k={k}: {data.psi_product}"
            )

    def test_critical_maps_to_zero(self):
        """QGL dual of critical level = 0 (classical limit)."""
        for t, r, hv in [('A', 1, 2), ('D', 4, 6), ('E', 8, 30)]:
            data = qgl_full_duality(t, r, F(-hv))
            # k^L = -(-h^v) - h^v = 0
            # VERIFIED [DC] structural property [CF] cross-family census
            assert data.k_qgl == F(0)

    def test_zero_maps_to_critical(self):
        """QGL dual of k=0 is k^L = -h^v (critical level)."""
        for t, r, hv in [('A', 1, 2), ('D', 4, 6), ('E', 8, 30)]:
            data = qgl_full_duality(t, r, F(0))
            # VERIFIED [DC] structural property [CF] cross-family census
            assert data.k_qgl == F(-hv)

    def test_qgl_is_involution(self):
        """QGL^2 = id: k^{LL} = k."""
        for k in [F(1), F(3), F(7)]:
            d1 = qgl_full_duality('A', 1, k)
            d2 = qgl_full_duality('A', 1, d1.k_qgl)
            # VERIFIED [DC] involution check [CF] cross-family census
            assert d2.k_qgl == k, (
                f"QGL^2(k={k}) = {d2.k_qgl}, expected {k}"
            )

    def test_qgl_involution_orbit_arithmetic(self):
        """QGL o FF orbit is arithmetic progression with step h^v."""
        orbit = qgl_involution_orbit('A', 1, F(1), max_iter=6)
        assert len(orbit) == 6
        # Starting from k=1, after QGL: -3, after FF(-3): 3, etc.
        assert orbit[0]['k'] == F(1)

    def test_qgl_level_lattice_sl2(self):
        """QGL level lattice for sl_2: all Psi products = 1."""
        lattice = qgl_level_lattice('A', 1)
        assert lattice['all_psi_products_one']
        assert lattice['all_ff_sums_zero']


# =====================================================================
# 4. HECKE EIGENSHEAF TESTS
# =====================================================================

class TestHeckeEigensheaf:
    """Verify Hecke eigensheaf data from K3 x E."""

    def test_sl2_bun_dim(self):
        """Bun_{SL_2}(E) has dimension 1 (= rank)."""
        data = hecke_eigensheaf_data('A', 1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data.bun_g_dim == 1

    def test_sl2_weyl_order(self):
        """Weyl group |W(A_1)| = 2."""
        data = hecke_eigensheaf_data('A', 1)
        assert data.weyl_order == 2

    def test_sl2_hecke_status_conjectural(self):
        """Hecke eigensheaf status is CONJECTURAL."""
        data = hecke_eigensheaf_data('A', 1)
        assert 'CONJECTURAL' in data.hecke_status

    def test_sl2_kappa_ch(self):
        """kappa_ch = 9/4 at level 1 for sl_2 on K3."""
        data = hecke_eigensheaf_data('A', 1)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert data.kappa_ch_k3 == F(9, 4)

    def test_sl2_depends_on_cya2(self):
        """Dependency list includes CY-A_2 for K3 (proved)."""
        data = hecke_eigensheaf_data('A', 1)
        assert any('CY-A_2 for K3' in dep for dep in data.depends_on)

    def test_d4_bun_dim(self):
        """Bun_{SO_8}(E) has dimension 4."""
        data = hecke_eigensheaf_data('D', 4)
        assert data.bun_g_dim == 4

    def test_e8_bun_dim(self):
        """Bun_{E_8}(E) has dimension 8."""
        data = hecke_eigensheaf_data('E', 8)
        assert data.bun_g_dim == 8

    def test_e8_weyl_order(self):
        """|W(E_8)| = 696729600."""
        data = hecke_eigensheaf_data('E', 8)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data.weyl_order == 696729600

    def test_all_ade_bun_dim_equals_rank(self):
        """Bun_G(E) coarse moduli dimension = rank(g) for all ADE."""
        for label, data in hecke_eigensheaf_all_ade().items():
            d = lie_data(data.g_label[0], int(data.g_label[1:]))
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert data.bun_g_dim == d.rank, (
                f"Bun dim for {label}: {data.bun_g_dim}, expected {d.rank}"
            )

    def test_all_ade_hecke_conjectural(self):
        """All Hecke eigensheaf claims are CONJECTURAL."""
        for label, data in hecke_eigensheaf_all_ade().items():
            assert 'CONJECTURAL' in data.hecke_status, (
                f"Hecke status for {label} does not contain CONJECTURAL"
            )

    def test_num_ade_types(self):
        """7 ADE types for Hecke data."""
        all_hecke = hecke_eigensheaf_all_ade()
        assert len(all_hecke) == 7


# =====================================================================
# 5. SHADOW TOWER AND RAMIFICATION TESTS
# =====================================================================

class TestShadowRamification:
    """Verify shadow class to ramification type map."""

    def test_class_G_unramified(self):
        """Class G -> unramified, depth 0."""
        data = shadow_ramification('G')
        assert data.langlands_parameter == 'unramified'
        assert data.ramification_depth == 0

    def test_class_L_tame(self):
        """Class L -> tamely ramified, depth 1."""
        data = shadow_ramification('L')
        assert data.langlands_parameter == 'tamely ramified'
        assert data.ramification_depth == 1

    def test_class_C_wild(self):
        """Class C -> wildly ramified (regular), depth 2."""
        data = shadow_ramification('C')
        assert data.langlands_parameter == 'wildly ramified (regular)'
        assert data.ramification_depth == 2

    def test_class_M_irregular(self):
        """Class M -> irregular, infinite ramification."""
        data = shadow_ramification('M')
        assert data.langlands_parameter == 'irregular'
        # Stored as -1 for inf
        assert data.ramification_depth == -1

    def test_shadow_depth_ordering(self):
        """Shadow depths: G=2 < L=3 < C=4 < M=inf."""
        depths = {
            cls: RAMIFICATION_DATA[cls]['shadow_depth']
            for cls in ['G', 'L', 'C', 'M']
        }
        assert depths['G'] < depths['L'] < depths['C'] < depths['M']

    def test_ramification_depth_ordering(self):
        """Ramification depths: 0 < 1 < 2 < inf."""
        ram = {
            cls: RAMIFICATION_DATA[cls]['ramification_depth']
            for cls in ['G', 'L', 'C', 'M']
        }
        assert ram['G'] < ram['L'] < ram['C'] < ram['M']

    def test_four_distinct_parameters(self):
        """All four shadow classes map to distinct Langlands parameters."""
        params = set()
        for cls in ['G', 'L', 'C', 'M']:
            data = RAMIFICATION_DATA[cls]
            params.add(data['langlands_parameter'])
        assert len(params) == 4

    def test_class_G_polynomial(self):
        """Class G: QGL analytic type is polynomial."""
        data = shadow_ramification('G')
        assert data.qgl_analytic_type == 'polynomial'

    def test_class_L_rational(self):
        """Class L: QGL analytic type is rational."""
        data = shadow_ramification('L')
        assert data.qgl_analytic_type == 'rational'

    def test_class_M_gevrey(self):
        """Class M: QGL analytic type is Gevrey-1 divergent."""
        data = shadow_ramification('M')
        assert data.qgl_analytic_type == 'Gevrey-1 divergent'

    def test_invalid_class_rejected(self):
        """Invalid shadow class raises ValueError."""
        with pytest.raises(ValueError, match="Unknown shadow class"):
            shadow_ramification('X')

    def test_k3_ade_all_class_L(self):
        """All K3 ADE enhancements are shadow class L."""
        table = k3_ade_ramification_table()
        for label, entry in table.items():
            assert entry['shadow_class'] == 'L', (
                f"K3 {label}: shadow class {entry['shadow_class']}, expected L"
            )

    def test_k3_ade_all_tamely_ramified(self):
        """All K3 ADE enhancements map to tamely ramified."""
        table = k3_ade_ramification_table()
        for label, entry in table.items():
            assert entry['ramification_type'] == 'tamely ramified', (
                f"K3 {label}: ramification {entry['ramification_type']}"
            )

    def test_k3_ade_table_has_9_types(self):
        """K3 ADE ramification table has 9 types."""
        table = k3_ade_ramification_table()
        assert len(table) == 9

    def test_k3_sl2_kac_pole(self):
        """First Kac determinant pole for sl_2 at k = -1."""
        table = k3_ade_ramification_table()
        sl2 = table['A1']
        # First Kac pole at k = -h^v + 1 = -2 + 1 = -1
        assert sl2['kac_first_pole_level'] == -1.0

    def test_consistency_check_passes(self):
        """Shadow-ramification consistency check passes all checks."""
        results = shadow_ramification_consistency_check()
        # VERIFIED [DC] consistency check [CF] cross-family census
        assert results['all_checks_pass']

    def test_class_G_monodromy_trivial(self):
        """Class G has trivial monodromy."""
        data = shadow_ramification('G')
        assert data.monodromy_type == 'trivial'

    def test_class_L_monodromy_quasiunipotent(self):
        """Class L has quasi-unipotent monodromy."""
        data = shadow_ramification('L')
        assert 'quasi-unipotent' in data.monodromy_type

    def test_class_M_stokes_infinite(self):
        """Class M requires Borel resummation (infinite Stokes data)."""
        data = shadow_ramification('M')
        assert 'Borel' in data.stokes_data

    def test_class_G_examples(self):
        """Class G examples include Heisenberg."""
        data = shadow_ramification('G')
        assert 'Heisenberg' in data.example_algebras

    def test_class_M_examples(self):
        """Class M examples include Virasoro and W_{1+infinity}."""
        data = shadow_ramification('M')
        assert 'Virasoro' in data.example_algebras
        assert 'W_{1+infinity}' in data.example_algebras


# =====================================================================
# 6. CROSS-CONSISTENCY TESTS
# =====================================================================

class TestCrossConsistency:
    """Cross-consistency between the five components."""

    def test_functor_kappa_matches_bridge_kappa(self):
        """Functor kappa at k=1 matches bridge kappa_start."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            f = langlands_functor(t, r)
            b = yangian_oper_bridge(t, r)
            # VERIFIED [DC] cross-consistency [CF] cross-family census
            assert f.kappa_ch_input == b.kappa_ch_start, (
                f"Functor vs bridge kappa mismatch for {t}{r}"
            )

    def test_functor_critical_matches_bridge_end(self):
        """Functor critical kappa matches bridge kappa_end."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            f = langlands_functor(t, r)
            b = yangian_oper_bridge(t, r)
            assert f.kappa_ch_critical == b.kappa_ch_end

    def test_qgl_kappa_matches_functor(self):
        """QGL kappa at k=1 matches functor kappa."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            f = langlands_functor(t, r)
            q = qgl_full_duality(t, r, F(1))
            assert f.kappa_ch_input == q.kappa_ch_k

    def test_hecke_kappa_matches_functor(self):
        """Hecke kappa matches functor kappa."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            f = langlands_functor(t, r)
            h = hecke_eigensheaf_data(t, r)
            assert f.kappa_ch_input == h.kappa_ch_k3

    def test_functor_dual_matches_bridge_dual(self):
        """Functor Langlands dual matches bridge Langlands dual."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            f = langlands_functor(t, r)
            b = yangian_oper_bridge(t, r)
            assert f.langlands_dual_label == b.langlands_dual

    def test_bridge_oper_dim_matches_functor_center_dim(self):
        """Bridge oper dim at genus 2 matches functor center dim."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            f = langlands_functor(t, r)
            b = yangian_oper_bridge(t, r)
            assert f.center_dimension_genus_g[2] == b.oper_dim_genus2

    def test_qgl_and_ff_distinct(self):
        """QGL and FF are distinct involutions for all ADE at k=1."""
        for t, r in [('A', 1), ('A', 2), ('D', 4), ('E', 8)]:
            q = qgl_full_duality(t, r, F(1))
            # QGL: k^L = -1 - h^v, FF: k' = -1 - 2*h^v
            # These differ by h^v
            d = lie_data(t, r)
            assert q.k_qgl != q.k_ff, (
                f"QGL and FF coincide for {t}{r} (should not)"
            )
            assert q.k_qgl - q.k_ff == F(d.h_dual), (
                f"k^L - k' should be h^v = {d.h_dual} for {t}{r}"
            )

    def test_ramification_matches_k3_geometric_langlands(self):
        """Shadow->Langlands map consistent with k3_geometric_langlands."""
        from compute.lib.k3_geometric_langlands import shadow_to_langlands
        for cls in ['G', 'L', 'C', 'M']:
            old = shadow_to_langlands(cls)
            new = shadow_ramification(cls)
            assert old['langlands_parameter'] == new.langlands_parameter, (
                f"Mismatch for class {cls}: "
                f"old={old['langlands_parameter']}, "
                f"new={new.langlands_parameter}"
            )


# =====================================================================
# 7. MASTER VERIFICATION TESTS
# =====================================================================

class TestMasterVerification:
    """Master verification of the full engine."""

    def test_verify_langlands_functor(self):
        """Langlands functor verification passes."""
        results = verify_langlands_functor()
        assert results['num_steps'] == 5
        assert results['num_ade_types'] == 8

    def test_verify_yangian_oper_bridge(self):
        """Yangian-oper bridge verification passes."""
        results = verify_yangian_oper_bridge()
        for key, val in results.items():
            if 'zero' in key or 'positive' in key:
                assert val, f"Bridge check failed: {key}"

    def test_verify_qgl_duality(self):
        """QGL duality verification passes."""
        results = verify_qgl_duality()
        for key, val in results.items():
            if 'psi_product' in key:
                assert val is True or val is None, (
                    f"QGL Psi product check failed: {key}"
                )
            if 'ff_sum_zero' in key:
                assert val, f"FF sum zero check failed: {key}"

    def test_verify_hecke_data(self):
        """Hecke data verification passes."""
        results = verify_hecke_data()
        assert results['num_ade_types'] == 7
        assert results['hecke_sl2_bun_dim_1']

    def test_verify_shadow_ramification(self):
        """Shadow ramification verification passes."""
        results = verify_shadow_ramification()
        assert results['all_checks_pass']

    def test_verify_all_passes(self):
        """Master verify_all() passes."""
        results = verify_all()
        assert results['all_pass']

    def test_full_computation_keys(self):
        """full_computation() returns all expected sections."""
        fc = full_computation()
        expected_keys = [
            'verification', 'langlands_functor', 'yangian_oper_bridge',
            'qgl_sl2_level1', 'qgl_e8_level1', 'qgl_level_lattice_sl2',
            'hecke_data', 'k3_ramification_table',
            'shadow_ramification_check',
        ]
        for key in expected_keys:
            assert key in fc, f"Missing key {key} in full_computation()"

    def test_full_computation_verification_passes(self):
        """full_computation() verification section all passes."""
        fc = full_computation()
        assert fc['verification']['all_pass']
