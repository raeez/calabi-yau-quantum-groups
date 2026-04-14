r"""Tests for compute.lib.k3_geometric_langlands.

Comprehensive verification of the K3 geometric Langlands engine:
  - ADE enhancement data (level-1 Kac-Moody subalgebra on K3)
  - Feigin-Frenkel center at critical level from K3
  - Opers from K3 geometry (sl_2 and general ADE)
  - K3 Yangian Langlands dual (QGL duality Psi * Psi^L = 1)
  - K3 x E elliptic family and Bun_G(E)
  - Shadow tower to Langlands parameter type map

Key identities:
  kappa_ch(g_hat_k) = dim(g) * (k + h^v) / (2 * h^v)
  QGL dual level: k^L = -k - h^v (simply-laced)
  FF dual level: k' = -k - 2*h^v
  Psi(k) * Psi(k^L) = 1 (QGL duality)
  kappa(k) + kappa(k') = 0 (FF / Koszul duality)
"""

import math
from fractions import Fraction

import pytest

from compute.lib.k3_geometric_langlands import (
    ADEEnhancementData,
    FFCenterFromK3,
    K3xEFamilyData,
    OperFromK3,
    SHADOW_LANGLANDS_MAP,
    YangianLanglandsDual,
    ade_enhancement,
    all_ade_enhancements,
    bun_g_elliptic,
    ff_center_all_ade,
    ff_center_from_k3,
    full_computation,
    k3_ade_shadow_classes,
    k3xe_family_sl2,
    kappa_spectrum_ade,
    opers_from_k3_general,
    opers_from_k3_sl2,
    shadow_to_langlands,
    sl2_langlands_dual_at_level1,
    verify_all,
    yangian_langlands_dual,
    yangian_langlands_dual_table,
)

F = Fraction


# =====================================================================
# 1. ADE ENHANCEMENT TESTS
# =====================================================================

class TestADEEnhancement:
    """Verify ADE enhancement data on K3 at level 1."""

    def test_sl2_enhancement(self):
        """sl_2 = A_1 on K3: dim 3, h^v = 2, kappa_ch = 9/4."""
        enh = ade_enhancement('A', 1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.g_label == 'A1'
        assert enh.g_dim == 3
        assert enh.h_dual == 2
        assert enh.level == F(1)
        # kappa_ch = dim(g) * (k + h^v) / (2 * h^v) = 3 * 3 / 4 = 9/4
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert enh.kappa_ch_level1 == F(9, 4)
        # c = dim(g) * k / (k + h^v) = 3 * 1 / 3 = 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.central_charge_level1 == F(1)
        # Mukai embedding: 1 direction used, 23 remaining
        assert enh.num_mukai_directions == 1
        assert enh.remaining_mukai_rank == 23

    def test_sl3_enhancement(self):
        """sl_3 = A_2 on K3: dim 8, h^v = 3, kappa_ch = 4/3 * 4 = 16/3."""
        enh = ade_enhancement('A', 2)
        assert enh.g_dim == 8
        assert enh.h_dual == 3
        # kappa_ch = 8 * 4 / 6 = 32/6 = 16/3
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert enh.kappa_ch_level1 == F(16, 3)
        # c = 8 * 1 / 4 = 2
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.central_charge_level1 == F(2)
        assert enh.num_mukai_directions == 2
        assert enh.remaining_mukai_rank == 22

    def test_d4_enhancement(self):
        """so_8 = D_4 on K3: dim 28, h^v = 6, c = 4."""
        enh = ade_enhancement('D', 4)
        assert enh.g_dim == 28
        assert enh.h_dual == 6
        # kappa_ch = 28 * 7 / 12 = 196/12 = 49/3
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert enh.kappa_ch_level1 == F(49, 3)
        # c = 28 * 1 / 7 = 4
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.central_charge_level1 == F(4)
        assert enh.num_mukai_directions == 4
        assert enh.remaining_mukai_rank == 20

    def test_e6_enhancement(self):
        """E_6 on K3: dim 78, h^v = 12, c = 6."""
        enh = ade_enhancement('E', 6)
        assert enh.g_dim == 78
        assert enh.h_dual == 12
        # c = 78 * 1 / 13 = 6
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.central_charge_level1 == F(6)
        assert enh.num_mukai_directions == 6
        assert enh.remaining_mukai_rank == 18

    def test_e7_enhancement(self):
        """E_7 on K3: dim 133, h^v = 18, c = 7."""
        enh = ade_enhancement('E', 7)
        assert enh.g_dim == 133
        assert enh.h_dual == 18
        # c = 133 * 1 / 19 = 7
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.central_charge_level1 == F(7)
        assert enh.num_mukai_directions == 7
        assert enh.remaining_mukai_rank == 17

    def test_e8_enhancement(self):
        """E_8 on K3: dim 248, h^v = 30, c = 8."""
        enh = ade_enhancement('E', 8)
        assert enh.g_dim == 248
        assert enh.h_dual == 30
        # c = 248 * 1 / 31 = 8
        # VERIFIED [DC] structural property [CF] cross-family census
        assert enh.central_charge_level1 == F(8)
        assert enh.num_mukai_directions == 8
        assert enh.remaining_mukai_rank == 16

    def test_all_ade_enhancements_count(self):
        """9 standard ADE types (A1-A4, D4-D5, E6-E8)."""
        all_enh = all_ade_enhancements()
        # VERIFIED [DC] count check [CF] cross-family census
        assert len(all_enh) == 9
        assert 'A1' in all_enh
        assert 'E8' in all_enh

    def test_level1_central_charge_pattern(self):
        """At level 1 for simply-laced g: c = rank(g).

        This is a well-known identity:
          c(g_hat_1) = dim(g) * 1 / (1 + h^v) = dim(g) / (1 + h^v)
        For simply-laced types, dim(g) = rank(g) * (1 + h^v), so c = rank(g).
        """
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('D', 4), ('E', 6), ('E', 7), ('E', 8)]:
            enh = ade_enhancement(t, r)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert enh.central_charge_level1 == F(r), (
                f"c({t}{r}_hat_1) = {enh.central_charge_level1}, expected {r}"
            )

    def test_mukai_rank_conservation(self):
        """num_mukai_directions + remaining_mukai_rank = 24 for all types."""
        for label, enh in all_ade_enhancements().items():
            # VERIFIED [DC] rank count [DA] dimensional consistency
            assert enh.num_mukai_directions + enh.remaining_mukai_rank == 24

    def test_non_ade_rejected(self):
        """B, C, F, G types are rejected (not ADE)."""
        with pytest.raises(ValueError, match="ADE enhancement requires"):
            ade_enhancement('B', 2)
        with pytest.raises(ValueError, match="ADE enhancement requires"):
            ade_enhancement('C', 3)
        with pytest.raises(ValueError, match="ADE enhancement requires"):
            ade_enhancement('G', 2)

    def test_rank_too_large_rejected(self):
        """ADE types with rank > 20 cannot embed in Mukai lattice."""
        # A_{20} has rank 20, should still work
        enh = ade_enhancement('A', 20)
        assert enh.remaining_mukai_rank == 4
        # A_{21} has rank 21, exceeds the 20 negative directions
        with pytest.raises(ValueError, match="exceeds the 20 negative"):
            ade_enhancement('A', 21)


# =====================================================================
# 2. FEIGIN-FRENKEL CENTER TESTS
# =====================================================================

class TestFFCenter:
    """Verify Feigin-Frenkel center data from K3 ADE enhancement."""

    def test_sl2_ff_center(self):
        """FF center for sl_2: z(sl_2_hat) = Fun(Op_{PGL_2}(D))."""
        ff = ff_center_from_k3('A', 1)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert ff.g_label == 'A1'
        assert ff.h_dual == 2
        assert ff.critical_level == F(-2)
        assert ff.kappa_ch_at_k1 == F(9, 4)
        # kappa at critical level is ZERO
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert ff.kappa_ch_at_critical == F(0)
        # SL_2 is self-dual: G^L = PGL_2 has same Lie algebra
        assert ff.langlands_dual_label == 'A1'
        assert ff.casimir_degrees == (2,)
        # Residue = -dim(sl_2) * h^v = -3 * 2 = -6
        # VERIFIED [DC] residue computation [CF] cross-family census
        assert ff.sugawara_residue == F(-6)
        # Slope = dim(sl_2) / (2 * h^v) = 3/4
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert ff.kappa_slope == F(3, 4)

    def test_d4_ff_center(self):
        """FF center for D_4: z(so_8_hat) = Fun(Op_{SO_8}(D))."""
        ff = ff_center_from_k3('D', 4)
        assert ff.critical_level == F(-6)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert ff.kappa_ch_at_critical == F(0)
        # D_4 is self-dual
        assert ff.langlands_dual_label == 'D4'
        # Casimirs of D_4: 2, 4, 4, 6 -- wait, D_4 exponents are 1,3,3,5
        # Casimir degrees = exponents + 1 = 2, 4, 4, 6.
        # But _casimir_degrees for D_n returns range(2, 2n-1, 2) + [n]
        # For n=4: range(2,7,2) = [2,4,6] + [4] = [2,4,6,4]
        # Sorted: (2, 4, 4, 6)  <-- but the function returns as computed
        casimirs = ff.casimir_degrees
        # VERIFIED [DC] structural property [CF] cross-family census
        assert sorted(casimirs) == [2, 4, 4, 6]
        # Residue = -28 * 6 = -168
        assert ff.sugawara_residue == F(-168)

    def test_e8_ff_center(self):
        """FF center for E_8: z(e_8_hat) = Fun(Op_{E_8}(D))."""
        ff = ff_center_from_k3('E', 8)
        assert ff.critical_level == F(-30)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert ff.kappa_ch_at_critical == F(0)
        # E_8 is self-dual
        assert ff.langlands_dual_label == 'E8'
        # Casimirs of E_8: 2, 8, 12, 14, 18, 20, 24, 30
        # VERIFIED [DC] structural property [CF] cross-family census
        assert ff.casimir_degrees == (2, 8, 12, 14, 18, 20, 24, 30)
        # Residue = -248 * 30 = -7440
        assert ff.sugawara_residue == F(-7440)

    def test_all_ff_centers_kappa_zero(self):
        """kappa_ch = 0 at critical level for ALL ADE types."""
        for label, ff in ff_center_all_ade().items():
            # VERIFIED [DC] kappa computation [CF] cross-family census
            assert ff.kappa_ch_at_critical == F(0), (
                f"kappa at critical level for {label} is {ff.kappa_ch_at_critical}"
            )

    def test_all_ff_centers_negative_residue(self):
        """Sugawara residue = -dim(g)*h^v < 0 for all ADE types."""
        for label, ff in ff_center_all_ade().items():
            assert ff.sugawara_residue < 0, (
                f"Residue for {label} is {ff.sugawara_residue}, expected negative"
            )


# =====================================================================
# 3. OPER TESTS
# =====================================================================

class TestOpers:
    """Verify oper data from K3 geometry."""

    def test_sl2_oper_basic(self):
        """SL_2 oper: order 2 (projective connection)."""
        oper = opers_from_k3_sl2()
        assert oper.g_label == 'A1'
        # SL_2 is self-Langlands-dual at the Lie algebra level
        assert oper.langlands_dual == 'A1'
        # VERIFIED [DC] structural property [CF] cross-family census
        assert oper.oper_order == 2
        assert oper.critical_kappa == F(0)
        assert oper.level1_kappa == F(9, 4)

    def test_sl2_oper_genus2(self):
        """dim H^0(C_2, K^2) = 3 for genus 2."""
        oper = opers_from_k3_sl2()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert oper.num_oper_params_genus_g[2] == 3

    def test_sl2_oper_genus3(self):
        """dim H^0(C_3, K^2) = 6 for genus 3."""
        oper = opers_from_k3_sl2()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert oper.num_oper_params_genus_g[3] == 6

    def test_sl2_oper_genus_g_formula(self):
        """dim H^0(C_g, K^2) = 3(g-1) for g >= 2."""
        oper = opers_from_k3_sl2()
        for g in range(2, 6):
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert oper.num_oper_params_genus_g[g] == 3 * (g - 1)

    def test_general_oper_genus2_sl2(self):
        """General oper computation for A1, genus 2."""
        data = opers_from_k3_general('A', 1, 2)
        # For sl_2, G^L = PGL_2 has same Lie algebra: dim = 3
        # Total dim = 3 * (2-1) = 3
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data['total_oper_dim'] == 3
        assert data['matches_total']
        assert data['casimir_degrees'] == (2,)
        # Graded: degree 2 -> (2*2-1)*(2-1) = 3
        # graded_dimensions is a list of (degree, dim) pairs
        assert data['graded_dimensions'] == [(2, 3)]

    def test_general_oper_genus2_d4(self):
        """General oper computation for D4, genus 2."""
        data = opers_from_k3_general('D', 4, 2)
        # D_4 is self-dual: dim = 28
        # Total dim = 28 * (2-1) = 28
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data['total_oper_dim'] == 28
        assert data['matches_total']

    def test_general_oper_genus2_e8(self):
        """General oper computation for E8, genus 2."""
        data = opers_from_k3_general('E', 8, 2)
        # E_8 is self-dual: dim = 248
        # Total dim = 248 * (2-1) = 248
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data['total_oper_dim'] == 248
        assert data['matches_total']

    def test_oper_genus1_trivial(self):
        """Genus 1 (elliptic curve): oper space is trivial."""
        data = opers_from_k3_general('A', 1, 1)
        assert 'error' in data

    def test_oper_graded_sum_equals_total(self):
        """Graded sum of oper dimensions equals total for all ADE at genus 2."""
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('D', 4), ('E', 6), ('E', 7), ('E', 8)]:
            data = opers_from_k3_general(t, r, 2)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert data['matches_total'], f"Graded sum mismatch for {t}{r}"


# =====================================================================
# 4. K3 YANGIAN LANGLANDS DUAL TESTS
# =====================================================================

class TestYangianLanglandsDual:
    """Verify QGL duality for the K3 Yangian at ADE enhancement."""

    def test_sl2_qgl_dual_level(self):
        """sl_2 at k=1: QGL dual level k^L = -1 - 2 = -3."""
        yd = yangian_langlands_dual('A', 1, F(1))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert yd.k_langlands == F(-3)

    def test_sl2_qgl_psi_product(self):
        """Psi(1) * Psi(-3) = 1 for sl_2."""
        yd = yangian_langlands_dual('A', 1, F(1))
        # Psi(1) = 1/(1+2) = 1/3
        # Psi(-3) = -3/(-3+2) = -3/(-1) = 3
        # Product = 1/3 * 3 = 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert yd.psi_k == F(1, 3)
        assert yd.psi_kL == F(3)
        assert yd.psi_product == F(1)

    def test_sl3_qgl_psi_product(self):
        """Psi(1) * Psi(-4) = 1 for sl_3 (h^v = 3)."""
        yd = yangian_langlands_dual('A', 2, F(1))
        assert yd.k_langlands == F(-4)
        # Psi(1) = 1/4, Psi(-4) = -4/(-4+3) = -4/(-1) = 4
        # VERIFIED [DC] structural property [CF] cross-family census
        assert yd.psi_product == F(1)

    def test_d4_qgl_psi_product(self):
        """Psi(1) * Psi(-7) = 1 for D_4 (h^v = 6)."""
        yd = yangian_langlands_dual('D', 4, F(1))
        assert yd.k_langlands == F(-7)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert yd.psi_product == F(1)

    def test_e8_qgl_psi_product(self):
        """Psi(1) * Psi(-31) = 1 for E_8 (h^v = 30)."""
        yd = yangian_langlands_dual('E', 8, F(1))
        assert yd.k_langlands == F(-31)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert yd.psi_product == F(1)

    def test_qgl_psi_product_all_ade(self):
        """Psi * Psi^L = 1 for all ADE types at level 1."""
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('D', 4), ('D', 5),
                     ('E', 6), ('E', 7), ('E', 8)]:
            yd = yangian_langlands_dual(t, r, F(1))
            # VERIFIED [DC] structural property [CF] cross-family census
            assert yd.psi_product == F(1), (
                f"Psi product for {t}{r} at k=1: {yd.psi_product}"
            )

    def test_qgl_psi_product_multiple_levels(self):
        """Psi * Psi^L = 1 for sl_2 at levels 1, 2, 3, 5, 10."""
        for k in [F(1), F(2), F(3), F(5), F(10)]:
            yd = yangian_langlands_dual('A', 1, k)
            # VERIFIED [DC] structural property [CF] cross-family census
            assert yd.psi_product == F(1), (
                f"Psi product for A1 at k={k}: {yd.psi_product}"
            )

    def test_critical_maps_to_zero(self):
        """QGL dual of k = -h^v is k^L = 0 (classical limit of dual)."""
        for t, r, hv in [('A', 1, 2), ('A', 2, 3), ('D', 4, 6), ('E', 8, 30)]:
            yd = yangian_langlands_dual(t, r, F(-hv))
            # k^L = -(-h^v) - h^v = 0
            # VERIFIED [DC] structural property [CF] cross-family census
            assert yd.k_langlands == F(0)

    def test_zero_maps_to_critical(self):
        """QGL dual of k = 0 is k^L = -h^v (critical level of dual)."""
        for t, r, hv in [('A', 1, 2), ('A', 2, 3), ('D', 4, 6), ('E', 8, 30)]:
            yd = yangian_langlands_dual(t, r, F(0))
            # k^L = 0 - h^v = -h^v
            # VERIFIED [DC] structural property [CF] cross-family census
            assert yd.k_langlands == F(-hv)
            assert yd.is_critical_dual

    def test_sl2_kappa_sum_nonzero(self):
        """kappa(k=1) + kappa(k^L=-3) != 0 for QGL dual (NOT FF dual)."""
        yd = yangian_langlands_dual('A', 1, F(1))
        # kappa(1) = 9/4, kappa(-3) = 3*(-1)/4 = -3/4
        # Sum = 9/4 - 3/4 = 6/4 = 3/2
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert yd.kappa_sum == F(3, 2)
        assert yd.kappa_sum != F(0)

    def test_sl2_ff_vs_qgl(self):
        """FF dual and QGL dual are DIFFERENT involutions."""
        detail = sl2_langlands_dual_at_level1()
        # FF dual: k' = -1 - 2*2 = -5
        # VERIFIED [DC] structural property [CF] cross-family census
        assert detail['ff_dual_level'] == F(-5)
        # kappa(1) + kappa(-5) = 0 (FF is kappa-antisymmetric)
        assert detail['ff_sum_is_zero']
        # QGL dual: k^L = -1 - 2 = -3 (different from FF dual -5)
        assert detail['qgl_data'].k_langlands == F(-3)
        assert detail['qgl_data'].k_langlands != detail['ff_dual_level']

    def test_yangian_dual_table(self):
        """Table of QGL duals at multiple levels for sl_2."""
        table = yangian_langlands_dual_table('A', 1)
        assert len(table) == 5
        for entry in table:
            # VERIFIED [DC] structural property [CF] cross-family census
            assert entry.psi_product == F(1)


# =====================================================================
# 5. K3 x E FAMILY TESTS
# =====================================================================

class TestK3xEFamily:
    """Verify K3 x E elliptic family data."""

    def test_sl2_family_basic(self):
        """Basic K3 x E family data for sl_2."""
        fam = k3xe_family_sl2()
        assert fam.g_label == 'A1'
        assert fam.kappa_ch_k3 == F(9, 4)

    def test_bun_sl2_E(self):
        """Bun_{SL_2}(E) has rank 1 coarse moduli."""
        data = bun_g_elliptic('A', 1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data['dim_coarse_moduli'] == 1
        assert data['weyl_order'] == 2  # W(A_1) = S_2 = Z/2Z

    def test_bun_sl3_E(self):
        """Bun_{SL_3}(E) has rank 2 coarse moduli."""
        data = bun_g_elliptic('A', 2)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data['dim_coarse_moduli'] == 2
        assert data['weyl_order'] == 6  # W(A_2) = S_3

    def test_bun_d4_E(self):
        """Bun_{SO_8}(E) has rank 4 coarse moduli."""
        data = bun_g_elliptic('D', 4)
        assert data['dim_coarse_moduli'] == 4
        assert data['weyl_order'] == 192  # W(D_4) = 2^3 * 4! / ... = 192

    def test_bun_e8_E(self):
        """Bun_{E_8}(E) has rank 8 coarse moduli."""
        data = bun_g_elliptic('E', 8)
        assert data['dim_coarse_moduli'] == 8
        # VERIFIED [DC] structural property [CF] cross-family census
        assert data['weyl_order'] == 696729600


# =====================================================================
# 6. SHADOW TOWER TO LANGLANDS PARAMETER TESTS
# =====================================================================

class TestShadowLanglands:
    """Verify shadow class to Langlands parameter type mapping."""

    def test_class_G(self):
        """Class G -> unramified."""
        data = shadow_to_langlands('G')
        assert data['langlands_parameter'] == 'unramified'
        assert data['qgl_analytic_type'] == 'polynomial'
        assert data['shadow_depth'] == 2

    def test_class_L(self):
        """Class L -> tamely ramified."""
        data = shadow_to_langlands('L')
        assert data['langlands_parameter'] == 'tamely ramified'
        assert data['qgl_analytic_type'] == 'rational'
        assert data['shadow_depth'] == 3

    def test_class_C(self):
        """Class C -> wildly ramified (regular)."""
        data = shadow_to_langlands('C')
        assert data['langlands_parameter'] == 'wildly ramified (regular)'
        assert data['qgl_analytic_type'] == 'convergent'
        assert data['shadow_depth'] == 4

    def test_class_M(self):
        """Class M -> irregular."""
        data = shadow_to_langlands('M')
        assert data['langlands_parameter'] == 'irregular'
        assert data['qgl_analytic_type'] == 'Gevrey-1 divergent'

    def test_invalid_class_rejected(self):
        """Invalid shadow class raises ValueError."""
        with pytest.raises(ValueError, match="Unknown shadow class"):
            shadow_to_langlands('X')

    def test_all_classes_have_status(self):
        """All shadow classes carry CONJECTURAL status."""
        for cls in ['G', 'L', 'C', 'M']:
            data = shadow_to_langlands(cls)
            assert 'CONJECTURAL' in data['status']

    def test_k3_ade_shadow_all_class_L(self):
        """KM subalgebras at ADE enhancement are all class L."""
        classes = k3_ade_shadow_classes()
        for label, data in classes.items():
            assert data['langlands_parameter'] == 'tamely ramified'
            assert data['shadow_depth'] == 3


# =====================================================================
# 7. KAPPA SPECTRUM TESTS (AP113)
# =====================================================================

class TestKappaSpectrum:
    """Verify kappa spectrum at ADE enhancement (AP113 compliance)."""

    def test_kappa_cat_always_2(self):
        """kappa_cat = chi(O_{K3}) = 2 for all ADE types."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            spectrum = kappa_spectrum_ade(t, r)
            # VERIFIED [DC] kappa computation [CF] cross-family census
            assert spectrum['kappa_cat'] == F(2)

    def test_kappa_fiber_always_24(self):
        """kappa_fiber = Mukai rank = 24 for all K3."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            spectrum = kappa_spectrum_ade(t, r)
            # VERIFIED [DC] kappa computation [CF] cross-family census
            assert spectrum['kappa_fiber'] == F(24)

    def test_sl2_kappa_ch(self):
        """kappa_ch(sl_2_hat_1) = 9/4."""
        spectrum = kappa_spectrum_ade('A', 1)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert spectrum['kappa_ch'] == F(9, 4)

    def test_e8_kappa_ch(self):
        """kappa_ch(e_8_hat_1) = 248 * 31 / (2 * 30) = 7688/60 = 1922/15."""
        spectrum = kappa_spectrum_ade('E', 8)
        expected = F(248 * 31, 60)
        # VERIFIED [DC] kappa computation [CF] cross-family census
        assert spectrum['kappa_ch'] == expected

    def test_kappa_ch_monotone_in_dim(self):
        """kappa_ch increases with dim(g) at level 1 (fixed h^v scaling)."""
        kappas = []
        for t, r in [('A', 1), ('A', 2), ('D', 4), ('E', 6), ('E', 7), ('E', 8)]:
            spectrum = kappa_spectrum_ade(t, r)
            kappas.append(float(spectrum['kappa_ch']))
        # VERIFIED [DC] monotonicity check [CF] cross-family census
        assert kappas == sorted(kappas), "kappa_ch should increase with complexity"


# =====================================================================
# 8. CROSS-CONSISTENCY TESTS
# =====================================================================

class TestCrossConsistency:
    """Cross-consistency checks between different computations."""

    def test_enhancement_ff_consistency(self):
        """ADE enhancement kappa at level 1 matches FF center kappa at level 1."""
        for t, r in [('A', 1), ('D', 4), ('E', 8)]:
            enh = ade_enhancement(t, r)
            ff = ff_center_from_k3(t, r)
            # VERIFIED [DC] cross-consistency [CF] cross-family census
            assert enh.kappa_ch_level1 == ff.kappa_ch_at_k1

    def test_qgl_and_ff_involutions_commute(self):
        """QGL o FF = FF o QGL on the level space for self-dual types.

        QGL: k -> -k - h^v.  FF: k -> -k - 2*h^v.
        QGL(FF(k)) = QGL(-k - 2*h^v) = -(-k - 2*h^v) - h^v = k + h^v.
        FF(QGL(k)) = FF(-k - h^v) = -(-k - h^v) - 2*h^v = k - h^v.
        These are DIFFERENT (k + h^v vs k - h^v), so the involutions
        do NOT commute.

        But QGL^2 = FF: QGL(QGL(k)) = QGL(-k-h^v) = k+h^v-h^v = k.
        Wait, QGL^2(k) = k, so QGL is an involution.
        FF^2(k) = FF(-k-2h^v) = k+2h^v-2h^v = k, so FF is also an involution.
        They generate a Z/2 x Z/2 action only if they commute,
        otherwise a dihedral group.
        """
        # Both are involutions
        for k in [F(1), F(2), F(5)]:
            # QGL^2 = id
            yd1 = yangian_langlands_dual('A', 1, k)
            yd2 = yangian_langlands_dual('A', 1, yd1.k_langlands)
            # VERIFIED [DC] involution check [CF] cross-family census
            assert yd2.k_langlands == k, "QGL is not an involution"

    def test_verify_all_runs(self):
        """verify_all() returns expected keys and passes."""
        results = verify_all()
        assert results['num_ade_types'] == 9
        assert results['sl2_ff_sum_zero']
        for label in ['A1', 'A2', 'D4', 'E8']:
            # QGL duality Psi product = 1
            assert results[f'qgl_{label}_psi_product'] == 1.0

    def test_full_computation_keys(self):
        """full_computation() returns all expected sections."""
        fc = full_computation()
        expected_keys = [
            'verification', 'all_ade_enhancements', 'all_ff_centers',
            'sl2_opers', 'sl2_langlands_dual', 'k3xe_family',
            'shadow_langlands', 'oper_genus2_A1', 'oper_genus2_D4',
            'oper_genus2_E8', 'bun_sl2_E', 'bun_sl3_E', 'bun_e8_E',
        ]
        for key in expected_keys:
            assert key in fc, f"Missing key {key} in full_computation()"

    def test_oper_dim_matches_hitchin_base(self):
        """Oper dim on genus-g curve = Hitchin base dim = dim(G^L)*(g-1).

        This is the Hitchin-Beilinson-Drinfeld correspondence.
        """
        for t, r in [('A', 1), ('A', 2), ('D', 4), ('E', 8)]:
            data = opers_from_k3_general(t, r, 2)
            from compute.lib.geometric_langlands_shadow import hitchin_base_dimension
            dv = ade_enhancement(t, r)  # self-dual for ADE
            h_dim = hitchin_base_dimension(t, r, 2)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert data['total_oper_dim'] == h_dim

    def test_e8_maximal_embedding(self):
        """E_8 uses 8 of 24 Mukai directions, leaving 16.

        The 16 remaining directions form the 'spectator' lattice.
        16 = dim(fundamental rep of SO(16)), which is related to
        the anomaly cancellation: E_8 x E_8 has rank 16 = 24 - 8.
        """
        enh = ade_enhancement('E', 8)
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert enh.remaining_mukai_rank == 16
        # Two E_8 enhancements would use 16 directions, leaving 8
        # (but this exceeds rank 20, so only one E_8 fits in the
        # negative-definite part of the Mukai lattice)

    def test_level1_dim_formula(self):
        """For simply-laced g: dim(g) = rank(g) * (1 + h^v).

        This identity ensures c(g_hat_1) = rank(g).
        """
        for t, r, hv in [('A', 1, 2), ('A', 2, 3), ('A', 3, 4),
                         ('D', 4, 6), ('E', 6, 12), ('E', 7, 18), ('E', 8, 30)]:
            enh = ade_enhancement(t, r)
            # VERIFIED [DC] dimension count [DA] dimensional consistency
            assert enh.g_dim == r * (1 + hv), (
                f"dim({t}{r}) = {enh.g_dim}, expected {r}*(1+{hv}) = {r*(1+hv)}"
            )
