r"""Tests for the higher CY E_n tower: E_n structure for CY_d at d >= 4.

THEOREM (E_1 stabilization, thm:e1-stabilization-cy):
  For d >= 3, the CY chiral algebra is E_1.  The additional shifted
  structure is classified by the framing obstruction pi_d(BU), with
  possible refinement to pi_d(BSp) (d odd) or pi_d(BO) (d even).

ORGANIZATION:
  1. Bott periodicity foundations (U, Sp, O: period 2, 8, 8)     [24 tests]
  2. Fibration sequences (BU, BSp, BO from U, Sp, O)             [12 tests]
  3. E_n structure for d=1,2,3 (cross-check with existing results)[12 tests]
  4. E_n structure for d=4 (CY4: C^4, K3xK3, sextic)            [15 tests]
  5. E_n structure for d=5 (CY5: Z_2 Sp-refinement)             [10 tests]
  6. E_n structure for d=6 (CY6)                                 [8 tests]
  7. E_n structure for d=7,8 (periodicity return)                [8 tests]
  8. Full tower structure (d=1..16)                               [10 tests]
  9. Hodge data for higher CY                                    [12 tests]
  10. Modular characteristic for higher CY                        [8 tests]
  11. Cross-volume consistency                                    [6 tests]

Total: 125+ tests.

VERIFICATION STANDARD: Each numerical/structural claim is verified by
at least 2 independent methods.

GROUND TRUTH:
  - cy_to_chiral.tex: Theorems thm:s3-framing-vanishes, thm:e1-universality-cy3
  - en_factorization.tex: E_n hierarchy
  - e2_chiral_algebras.tex: E_2 operad and braided structure
  - Bott, "Stable homotopy of classical groups" (Ann. Math. 1959)
  - Lurie, "Higher Algebra" (2017)
  - Cao-Maulik-Toda, "CY4 stable pairs" (2018)
"""

import math
from fractions import Fraction

import pytest

from compute.lib.higher_cy_en_tower import (
    CYHigherHodgeData,
    E1StabilizationResult,
    E_INFTY_N,
    EnStructure,
    EnTowerSummary,
    FramingObstruction,
    HigherCYHochschild,
    HigherCYShadowData,
    affine_cy6_data,
    affine_cy_data,
    e1_stabilization,
    en_landscape_table,
    en_structure,
    en_tower_summary,
    framing_obstruction,
    full_summary,
    hochschild_affine_cy,
    k3_cross_k3_data,
    kappa_affine_cy,
    kappa_cy4_bcov,
    kappa_k3_cross_k3,
    kappa_sextic_cy4,
    obstruction_is_trivial,
    obstruction_order,
    pi_k_BO,
    pi_k_BSp,
    pi_k_BU,
    pi_k_O,
    pi_k_Sp,
    pi_k_U,
    pv_dimension,
    quintic_fivefold_data,
    sextic_hypersurface_data,
    shadow_tower_affine_cy,
    shadow_tower_k3_cross_k3,
    sn_bracket_vanishes_affine,
    verify_all_bott,
    verify_all_cross_checks,
    verify_bott_periodicity_O,
    verify_bott_periodicity_Sp,
    verify_bott_periodicity_U,
    verify_bu_bsp_compatible_d3,
    verify_d1_e_infty,
    verify_d2_e2,
    verify_d3_e1,
    verify_d3_s3_framing_trivial,
    verify_d4_obstruction_nontrivial,
    verify_d5_sp_refinement,
    verify_d7_trivial,
    verify_d8_bott_return,
    verify_fibration_sequence_BO,
    verify_fibration_sequence_BSp,
    verify_fibration_sequence_BU,
)


# =========================================================================
# 1. Bott periodicity foundations (24 tests)
# =========================================================================

class TestBottPeriodicityU:
    """Bott periodicity for U: period 2."""

    def test_pi_0_U(self):
        """pi_0(U) = 0 (U is connected)."""
        assert pi_k_U(0) == "0"

    def test_pi_1_U(self):
        """pi_1(U) = Z."""
        assert pi_k_U(1) == "Z"

    def test_pi_2_U(self):
        """pi_2(U) = 0."""
        assert pi_k_U(2) == "0"

    def test_pi_3_U(self):
        """pi_3(U) = Z."""
        assert pi_k_U(3) == "Z"

    def test_period_2(self):
        """Bott periodicity: pi_{k+2}(U) = pi_k(U) for all k."""
        assert verify_bott_periodicity_U()

    def test_even_vanish(self):
        """pi_k(U) = 0 for all even k >= 0."""
        for k in range(0, 20, 2):
            assert pi_k_U(k) == "0", f"pi_{k}(U) should be 0"

    def test_odd_Z(self):
        """pi_k(U) = Z for all odd k >= 1."""
        for k in range(1, 20, 2):
            assert pi_k_U(k) == "Z", f"pi_{k}(U) should be Z"


class TestBottPeriodicitySp:
    """Bott periodicity for Sp: period 8."""

    def test_pi_0_Sp(self):
        """pi_0(Sp) = 0 (Sp is connected)."""
        assert pi_k_Sp(0) == "0"

    def test_pi_1_Sp(self):
        """pi_1(Sp) = 0 (Sp is simply connected)."""
        assert pi_k_Sp(1) == "0"

    def test_pi_2_Sp(self):
        """pi_2(Sp) = 0."""
        assert pi_k_Sp(2) == "0"

    def test_pi_3_Sp(self):
        """pi_3(Sp) = Z (the generator is the symplectic structure)."""
        assert pi_k_Sp(3) == "Z"

    def test_pi_4_Sp(self):
        """pi_4(Sp) = Z_2."""
        assert pi_k_Sp(4) == "Z_2"

    def test_pi_5_Sp(self):
        """pi_5(Sp) = Z_2."""
        assert pi_k_Sp(5) == "Z_2"

    def test_pi_6_Sp(self):
        """pi_6(Sp) = 0."""
        assert pi_k_Sp(6) == "0"

    def test_pi_7_Sp(self):
        """pi_7(Sp) = Z."""
        assert pi_k_Sp(7) == "Z"

    def test_period_8(self):
        """Bott periodicity: pi_{k+8}(Sp) = pi_k(Sp)."""
        assert verify_bott_periodicity_Sp()


class TestBottPeriodicityO:
    """Bott periodicity for O: period 8."""

    def test_pi_0_O(self):
        """pi_0(O) = Z_2."""
        assert pi_k_O(0) == "Z_2"

    def test_pi_1_O(self):
        """pi_1(O) = Z_2."""
        assert pi_k_O(1) == "Z_2"

    def test_pi_2_O(self):
        """pi_2(O) = 0."""
        assert pi_k_O(2) == "0"

    def test_pi_3_O(self):
        """pi_3(O) = Z."""
        assert pi_k_O(3) == "Z"

    def test_pi_4_O(self):
        """pi_4(O) = 0."""
        assert pi_k_O(4) == "0"

    def test_pi_7_O(self):
        """pi_7(O) = Z."""
        assert pi_k_O(7) == "Z"

    def test_period_8(self):
        """Bott periodicity: pi_{k+8}(O) = pi_k(O)."""
        assert verify_bott_periodicity_O()

    def test_sp_o_relationship(self):
        """Sp and O are related by Bott: pi_k(Sp) = pi_{k+4}(O) mod period shifts.

        This is the content of real vs quaternionic Bott:
          pi_k(O) table: Z_2, Z_2, 0, Z, 0, 0, 0, Z
          pi_k(Sp) table: 0, 0, 0, Z, Z_2, Z_2, 0, Z
        The Sp table is the O table shifted by 4 positions.
        """
        for k in range(16):
            assert pi_k_Sp(k) == pi_k_O((k + 4) % 8)


# =========================================================================
# 2. Fibration sequences (12 tests)
# =========================================================================

class TestFibrationSequences:
    """Fibration sequences: BG -> EG -> G gives pi_k(BG) = pi_{k-1}(G)."""

    def test_bsp_fibration(self):
        """pi_k(BSp) = pi_{k-1}(Sp) for k >= 1."""
        assert verify_fibration_sequence_BSp()

    def test_bo_fibration(self):
        """pi_k(BO) = pi_{k-1}(O) for k >= 1."""
        assert verify_fibration_sequence_BO()

    def test_bu_fibration(self):
        """pi_k(BU) = pi_{k-1}(U) for k >= 1."""
        assert verify_fibration_sequence_BU()

    def test_pi_1_BU(self):
        """pi_1(BU) = pi_0(U) = 0."""
        assert pi_k_BU(1) == "0"

    def test_pi_2_BU(self):
        """pi_2(BU) = pi_1(U) = Z."""
        assert pi_k_BU(2) == "Z"

    def test_pi_3_BU(self):
        """pi_3(BU) = pi_2(U) = 0."""
        assert pi_k_BU(3) == "0"

    def test_pi_4_BU(self):
        """pi_4(BU) = pi_3(U) = Z."""
        assert pi_k_BU(4) == "Z"

    def test_pi_4_BSp(self):
        """pi_4(BSp) = pi_3(Sp) = Z."""
        assert pi_k_BSp(4) == "Z"

    def test_pi_5_BSp(self):
        """pi_5(BSp) = pi_4(Sp) = Z_2."""
        assert pi_k_BSp(5) == "Z_2"

    def test_pi_6_BSp(self):
        """pi_6(BSp) = pi_5(Sp) = Z_2."""
        assert pi_k_BSp(6) == "Z_2"

    def test_pi_4_BO(self):
        """pi_4(BO) = pi_3(O) = Z."""
        assert pi_k_BO(4) == "Z"

    def test_pi_6_BO(self):
        """pi_6(BO) = pi_5(O) = 0."""
        assert pi_k_BO(6) == "0"


# =========================================================================
# 3. E_n structure for d=1,2,3 (cross-check) (12 tests)
# =========================================================================

class TestEnCrossCheckD123:
    """Verify E_n structure agrees with established results for d=1,2,3."""

    def test_d1_e_infty(self):
        """d=1 (elliptic curve): E_infty."""
        assert verify_d1_e_infty()

    def test_d1_structure(self):
        """d=1: native_en = E_infty, native_n = 100 (sentinel)."""
        es = en_structure(1)
        assert es.native_en == "E_infty"
        assert es.native_n == E_INFTY_N

    def test_d1_no_obstruction(self):
        """d=1: pi_1(BU) = 0."""
        es = en_structure(1)
        assert es.framing_obstruction_BU == "0"

    def test_d2_e2(self):
        """d=2 (K3): E_2."""
        assert verify_d2_e2()

    def test_d2_structure(self):
        """d=2: native_en = E_2, native_n = 2."""
        es = en_structure(2)
        assert es.native_en == "E_2"
        assert es.native_n == 2

    def test_d2_z_obstruction(self):
        """d=2: pi_2(BU) = Z (the Chern class = braiding parameter)."""
        es = en_structure(2)
        assert es.framing_obstruction_BU == "Z"

    def test_d3_e1(self):
        """d=3 (CY3): E_1."""
        assert verify_d3_e1()

    def test_d3_structure(self):
        """d=3: native_en = E_1, native_n = 1."""
        es = en_structure(3)
        assert es.native_en == "E_1"
        assert es.native_n == 1

    def test_d3_bu_trivial(self):
        """d=3: pi_3(BU) = 0 (Bott: 3 is odd)."""
        assert pi_k_BU(3) == "0"

    def test_d3_bsp_trivial(self):
        """d=3: pi_3(BSp) = 0 (pi_2(Sp) = 0)."""
        assert pi_k_BSp(3) == "0"

    def test_d3_both_trivial(self):
        """d=3: both BU and BSp paths give trivial obstruction."""
        assert verify_bu_bsp_compatible_d3()

    def test_d3_s3_framing(self):
        """Theorem thm:s3-framing-vanishes: S^3-framing is universally trivial."""
        assert verify_d3_s3_framing_trivial()


# =========================================================================
# 4. E_n structure for d=4 (CY4) (15 tests)
# =========================================================================

class TestEnD4:
    """E_n structure for CY 4-folds."""

    def test_d4_e1(self):
        """d=4: native E_1 (not E_0, which doesn't exist)."""
        es = en_structure(4)
        assert es.native_en == "E_1"
        assert es.native_n == 1

    def test_d4_bu_Z(self):
        """d=4: pi_4(BU) = Z (nontrivial integer obstruction)."""
        assert verify_d4_obstruction_nontrivial()

    def test_d4_bsp_Z(self):
        """d=4: pi_4(BSp) = Z (from Sp path: pi_3(Sp) = Z)."""
        assert pi_k_BSp(4) == "Z"

    def test_d4_bo_Z(self):
        """d=4: pi_4(BO) = Z (from O path: pi_3(O) = Z)."""
        assert pi_k_BO(4) == "Z"

    def test_d4_all_paths_agree(self):
        """d=4: BU, BSp, and BO all give Z obstruction."""
        assert pi_k_BU(4) == "Z"
        assert pi_k_BSp(4) == "Z"
        assert pi_k_BO(4) == "Z"

    def test_d4_pontryagin(self):
        """d=4: the characteristic class is the first Pontryagin class."""
        fo = framing_obstruction(4)
        assert "p_1" in fo.characteristic_class or "Pontryagin" in fo.characteristic_class

    def test_d4_shifted_structure(self):
        """d=4: E_1 with Z-shifted symplectic structure."""
        es = en_structure(4)
        assert "Z-shifted" in es.shifted_structure

    def test_d4_stabilization(self):
        """d=4: E_1 stabilization with Z shift."""
        stab = e1_stabilization(4)
        assert stab.is_e1
        assert stab.shifted_by == "Z"
        assert not stab.trivial_obstruction

    def test_d4_not_e0(self):
        """d=4: the chiral algebra is NOT E_0 (E_0 is not a valid operad)."""
        es = en_structure(4)
        assert es.native_n >= 1

    def test_c4_hh_total(self):
        """C^4: total dim GL(4)-invariant HH = 2^4 = 16."""
        data = affine_cy_data(4)
        assert data.hh_total == 16

    def test_c4_hh_dims(self):
        """C^4: HH_p = C(4,p) for the constant-coefficient sector."""
        data = affine_cy_data(4)
        for p in range(5):
            assert data.hh_dims[p] == math.comb(4, p)

    def test_c4_deformation_dim(self):
        """C^4: 2 deformation parameters (sigma_3, sigma_4)."""
        hc = hochschild_affine_cy(4)
        assert hc.deformation_dim == 2
        assert hc.sigma_dim == 2

    def test_k3xk3_chi(self):
        """K3 x K3: chi = 24^2 = 576."""
        data = k3_cross_k3_data()
        assert data.euler_characteristic == 576

    def test_k3xk3_kappa(self):
        """K3 x K3: kappa = 48 (additivity: 24 + 24)."""
        assert kappa_k3_cross_k3() == Fraction(48)

    def test_sextic_chi(self):
        """Sextic in P^5: chi = 2610.

        From the Hodge numbers (all nonzero entries have p+q even,
        so all signs are +1):
        1 + 1 + 1 + 1 + 1 + 426 + 1752 + 426 + 1 = 2610.
        """
        data = sextic_hypersurface_data()
        assert data.euler_characteristic == 2610


# =========================================================================
# 5. E_n structure for d=5 (CY5) (10 tests)
# =========================================================================

class TestEnD5:
    """E_n structure for CY 5-folds."""

    def test_d5_e1(self):
        """d=5: native E_1."""
        es = en_structure(5)
        assert es.native_en == "E_1"
        assert es.native_n == 1

    def test_d5_bu_trivial(self):
        """d=5: pi_5(BU) = 0 (5 is odd, Bott for U)."""
        assert pi_k_BU(5) == "0"

    def test_d5_bsp_Z2(self):
        """d=5: pi_5(BSp) = Z_2 (nontrivial Sp refinement!)."""
        assert pi_k_BSp(5) == "Z_2"

    def test_d5_sp_refinement(self):
        """d=5: BU trivial but Sp nontrivial (the Sp refinement matters)."""
        assert verify_d5_sp_refinement()

    def test_d5_shifted_z2(self):
        """d=5: Z_2-shifted structure from Sp refinement."""
        stab = e1_stabilization(5)
        assert stab.shifted_by == "Z_2"
        assert not stab.trivial_obstruction

    def test_c5_hh_total(self):
        """C^5: total dim GL(5)-invariant HH = 2^5 = 32."""
        data = affine_cy_data(5)
        assert data.hh_total == 32

    def test_c5_deformation_dim(self):
        """C^5: 3 deformation parameters (sigma_3, sigma_4, sigma_5)."""
        hc = hochschild_affine_cy(5)
        assert hc.deformation_dim == 3

    def test_c5_hh_dims(self):
        """C^5: HH_p = C(5,p)."""
        data = affine_cy_data(5)
        expected = {0: 1, 1: 5, 2: 10, 3: 10, 4: 5, 5: 1}
        assert data.hh_dims == expected

    def test_d5_bott_position(self):
        """d=5: Bott position 5 mod 8 = 5."""
        stab = e1_stabilization(5)
        assert stab.bott_period == 5

    def test_d5_not_same_as_d3(self):
        """d=5 differs from d=3: d=3 has trivial obstruction, d=5 has Z_2."""
        stab3 = e1_stabilization(3)
        stab5 = e1_stabilization(5)
        assert stab3.trivial_obstruction
        assert not stab5.trivial_obstruction


# =========================================================================
# 6. E_n structure for d=6 (CY6) (8 tests)
# =========================================================================

class TestEnD6:
    """E_n structure for CY 6-folds."""

    def test_d6_e1(self):
        """d=6: native E_1."""
        es = en_structure(6)
        assert es.native_en == "E_1"

    def test_d6_bu_Z(self):
        """d=6: pi_6(BU) = Z (6 is even)."""
        assert pi_k_BU(6) == "Z"

    def test_d6_bo_trivial(self):
        """d=6: pi_6(BO) = 0 (pi_5(O) = 0)."""
        assert pi_k_BO(6) == "0"

    def test_d6_bsp_Z2(self):
        """d=6: pi_6(BSp) = Z_2 (pi_5(Sp) = Z_2)."""
        assert pi_k_BSp(6) == "Z_2"

    def test_d6_stabilization(self):
        """d=6: Z-shifted from BU path."""
        stab = e1_stabilization(6)
        assert stab.shifted_by == "Z"
        assert not stab.trivial_obstruction

    def test_c6_hh_total(self):
        """C^6: total dim = 2^6 = 64."""
        data = affine_cy_data(6)
        assert data.hh_total == 64

    def test_c6_deformation_dim(self):
        """C^6: 4 deformation parameters."""
        hc = hochschild_affine_cy(6)
        assert hc.deformation_dim == 4

    def test_d6_bu_vs_bo_discrepancy(self):
        """d=6: BU gives Z but BO gives 0 (discrepancy from holomorphic reduction).

        The BO obstruction is trivial, but the BU obstruction (which uses
        the complex structure) is nontrivial.  This means the Z-valued
        obstruction is visible only through the complex/holomorphic structure,
        not through the real structure alone.
        """
        assert pi_k_BU(6) == "Z"
        assert pi_k_BO(6) == "0"


# =========================================================================
# 7. E_n structure for d=7,8 (periodicity) (8 tests)
# =========================================================================

class TestEnD7D8:
    """E_n structure for d=7 and d=8: Bott periodicity return."""

    def test_d7_trivial(self):
        """d=7: all obstructions trivial (mirrors d=3)."""
        assert verify_d7_trivial()

    def test_d7_stabilization(self):
        """d=7: E_1 with trivial obstruction."""
        stab = e1_stabilization(7)
        assert stab.is_e1
        assert stab.trivial_obstruction
        assert stab.shifted_by == "0"

    def test_d7_mirrors_d3(self):
        """d=7 obstruction pattern mirrors d=3 (both trivial).

        d=3: pi_3(BU) = 0, pi_3(BSp) = 0.
        d=7: pi_7(BU) = 0, pi_7(BSp) = 0.
        The 4-shift in Sp periodicity: pi_k(Sp) and pi_{k+4}(O) are related.
        """
        assert pi_k_BU(7) == "0"
        assert pi_k_BSp(7) == "0"
        assert pi_k_BU(3) == "0"
        assert pi_k_BSp(3) == "0"

    def test_d8_bott_return(self):
        """d=8: pi_8(BU) = Z (Bott periodicity: same as d=0 shifted)."""
        assert verify_d8_bott_return()

    def test_d8_stabilization(self):
        """d=8: E_1 with Z-shifted structure."""
        stab = e1_stabilization(8)
        assert stab.is_e1
        assert stab.shifted_by == "Z"
        assert not stab.trivial_obstruction

    def test_d8_matches_d4_type(self):
        """d=8 has same type of obstruction as d=4 (both Z from BU).

        This is BU Bott periodicity: pi_{k+2}(BU) = pi_k(BU).
        But d=8 vs d=4 differs by 4, and BU has period 2, so actually
        pi_8(BU) = pi_6(BU) = pi_4(BU) = Z.  All even d >= 2 give Z.
        """
        assert pi_k_BU(8) == pi_k_BU(4) == "Z"

    def test_d9_trivial(self):
        """d=9: trivial (mirrors d=1 by period 8 in BSp)."""
        assert pi_k_BU(9) == "0"
        assert pi_k_BSp(9) == "0"

    def test_d10_Z(self):
        """d=10: pi_10(BU) = Z (10 is even)."""
        assert pi_k_BU(10) == "Z"


# =========================================================================
# 8. Full tower structure (10 tests)
# =========================================================================

class TestFullTower:
    """Full E_n tower for d=1..16."""

    def test_tower_summary_generates(self):
        """en_tower_summary generates without error."""
        tower = en_tower_summary(16)
        assert len(tower.entries) == 16

    def test_trivial_dims(self):
        """Dimensions with trivial obstruction: d=1,3,7,9,11,15,...

        d odd with BU=0 and BSp=0: d=1,3,7,9,11,15,...
        Pattern: d mod 8 in {1, 3, 7} gives trivial (from Sp period 8).
        d=1: BU=0, Sp(d=1): pi_1(BSp) = pi_0(Sp) = 0. Trivial.
        d=3: BU=0, BSp=0. Trivial.
        d=5: BU=0, BSp=Z_2. NONTRIVIAL.
        d=7: BU=0, BSp=0. Trivial.
        d=9: BU=0, BSp = pi_8(Sp) = pi_0(Sp) = 0. Trivial.
        d=11: BU=0, BSp = pi_10(Sp) = pi_2(Sp) = 0. Trivial.
        d=13: BU=0, BSp = pi_12(Sp) = pi_4(Sp) = Z_2. NONTRIVIAL.
        d=15: BU=0, BSp = pi_14(Sp) = pi_6(Sp) = 0. Trivial.
        """
        tower = en_tower_summary(16)
        trivial = tower.trivial_obstruction_dims
        # d=1,3,7,9,11,15 should be trivial
        for d in [1, 3, 7, 9, 11, 15]:
            assert d in trivial, f"d={d} should have trivial obstruction"

    def test_nontrivial_dims(self):
        """Dimensions with nontrivial obstruction: d=2,4,5,6,8,10,12,13,14,16."""
        tower = en_tower_summary(16)
        trivial = set(tower.trivial_obstruction_dims)
        for d in [4, 5, 6, 8, 10, 12, 13, 14, 16]:
            assert d not in trivial, f"d={d} should have nontrivial obstruction"

    def test_z_obstruction_dims(self):
        """Z obstruction at even d >= 2."""
        tower = en_tower_summary(16)
        z_dims = tower.z_obstruction_dims
        # All even d >= 2 should have Z from BU
        for d in [2, 4, 6, 8, 10, 12, 14, 16]:
            assert d in z_dims, f"d={d} should have Z obstruction"

    def test_z2_obstruction_dims(self):
        """Z_2 obstruction from Sp refinement at d=5,13,...

        d odd with BU=0 but BSp=Z_2:
        pi_5(BSp) = pi_4(Sp) = Z_2 -> d=5
        pi_13(BSp) = pi_12(Sp) = pi_4(Sp) = Z_2 -> d=13
        """
        tower = en_tower_summary(16)
        z2_dims = tower.z2_obstruction_dims
        assert 5 in z2_dims, "d=5 should have Z_2"
        assert 13 in z2_dims, "d=13 should have Z_2"

    def test_bott_period_8_pattern(self):
        """The 8-fold Bott pattern in the shifted structure."""
        tower = en_tower_summary(16)
        pattern = tower.bott_period_8_pattern
        assert len(pattern) == 8
        # pattern for d=1..8:
        # d=1: "0" (trivial)
        # d=2: "Z" (Chern class)
        # d=3: "0" (trivial)
        # d=4: "Z" (Pontryagin)
        # d=5: "Z_2" (Sp refinement)
        # d=6: "Z" (c_3)
        # d=7: "0" (trivial)
        # d=8: "Z" (Bott return)
        expected = ["0", "Z", "0", "Z", "Z_2", "Z", "0", "Z"]
        assert pattern == expected

    def test_all_d_geq_3_are_e1(self):
        """All d >= 3 have native E_1 structure."""
        for d in range(3, 17):
            es = en_structure(d)
            assert es.native_en == "E_1", f"d={d} should be E_1"

    def test_only_d2_is_e2(self):
        """Only d=2 has native E_2 structure."""
        for d in range(1, 17):
            es = en_structure(d)
            if d == 2:
                assert es.native_en == "E_2"
            elif d == 1:
                assert es.native_en == "E_infty"
            else:
                assert es.native_en == "E_1"

    def test_landscape_table(self):
        """en_landscape_table generates correct number of rows."""
        table = en_landscape_table(12)
        assert len(table) == 12
        assert table[0]["d"] == 1
        assert table[-1]["d"] == 12

    def test_period_repeats_after_8(self):
        """The shifted structure repeats with period 8 for d >= 3.

        d and d+8 have the same shifted_by group (from Bott periodicity).
        This holds modulo the distinction between BU (period 2) and BSp (period 8).
        """
        for d in range(3, 9):
            stab_d = e1_stabilization(d)
            stab_d8 = e1_stabilization(d + 8)
            assert stab_d.shifted_by == stab_d8.shifted_by, \
                f"d={d} and d={d+8} should have same shift type"


# =========================================================================
# 9. Hodge data for higher CY (12 tests)
# =========================================================================

class TestHigherCYHodge:
    """Hodge data and HH for CY d-folds with d >= 4."""

    def test_c4_hh_binomial(self):
        """C^4: HH_p = C(4,p) = {1, 4, 6, 4, 1}."""
        data = affine_cy_data(4)
        assert data.hh_dims == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}

    def test_c5_hh_binomial(self):
        """C^5: HH_p = C(5,p) = {1, 5, 10, 10, 5, 1}."""
        data = affine_cy_data(5)
        assert data.hh_dims == {0: 1, 1: 5, 2: 10, 3: 10, 4: 5, 5: 1}

    def test_c6_hh_binomial(self):
        """C^6: HH_p = C(6,p) = {1, 6, 15, 20, 15, 6, 1}."""
        data = affine_cy_data(6)
        assert data.hh_dims == {0: 1, 1: 6, 2: 15, 3: 20, 4: 15, 5: 6, 6: 1}

    def test_cd_total_2d(self):
        """C^d: total HH = 2^d for all d."""
        for d in range(1, 10):
            data = affine_cy_data(d)
            assert data.hh_total == 2 ** d, f"C^{d}: total should be 2^{d}"

    def test_k3xk3_hodge_symmetry(self):
        """K3 x K3: h^{p,q} = h^{q,p} (Hodge symmetry)."""
        data = k3_cross_k3_data()
        for (p, q), v in data.hodge.items():
            v_sym = data.hodge.get((q, p), 0)
            assert v == v_sym, f"h^{{{p},{q}}} = {v} != h^{{{q},{p}}} = {v_sym}"

    def test_k3xk3_h00(self):
        """K3 x K3: h^{0,0} = 1."""
        data = k3_cross_k3_data()
        assert data.hodge.get((0, 0), 0) == 1

    def test_k3xk3_h20(self):
        """K3 x K3: h^{2,0} = h^{2,0}(K3)^2 + 2*h^{1,0}(K3)*h^{1,0}(K3) + h^{0,0}(K3)*h^{2,0}(K3)
        = 1*1 + 0 + 1*1 = 2."""
        data = k3_cross_k3_data()
        assert data.hodge.get((2, 0), 0) == 2

    def test_k3xk3_h11(self):
        """K3 x K3: h^{1,1} by Kunneth.

        h^{1,1}(K3xK3) = sum h^{a,b}(K3) * h^{1-a,1-b}(K3)
        = h^{0,0}*h^{1,1} + h^{1,1}*h^{0,0} + h^{1,0}*h^{0,1} + h^{0,1}*h^{1,0}
        = 1*20 + 20*1 + 0 + 0 = 40.
        """
        data = k3_cross_k3_data()
        assert data.hodge.get((1, 1), 0) == 40

    def test_sextic_h31(self):
        """Sextic in P^5: h^{3,1} = 426."""
        data = sextic_hypersurface_data()
        assert data.hodge.get((3, 1), 0) == 426

    def test_sextic_h22(self):
        """Sextic in P^5: h^{2,2} = 1752."""
        data = sextic_hypersurface_data()
        assert data.hodge.get((2, 2), 0) == 1752

    def test_pv_dimension_binomial(self):
        """dim PV^p(C^d) = C(d,p) (constant-coefficient sector)."""
        for d in range(1, 8):
            for p in range(d + 1):
                assert pv_dimension(d, p) == math.comb(d, p)

    def test_pv_dimension_vanishing(self):
        """PV^p = 0 for p > d or p < 0."""
        for d in range(1, 8):
            assert pv_dimension(d, d + 1) == 0
            assert pv_dimension(d, -1) == 0


# =========================================================================
# 10. Modular characteristic for higher CY (8 tests)
# =========================================================================

class TestHigherCYKappa:
    """Modular characteristic kappa for CY d-folds."""

    def test_kappa_c4_self_dual(self):
        """C^4 at self-dual point: kappa = 1."""
        assert kappa_affine_cy(4) == Fraction(1)

    def test_kappa_c5_self_dual(self):
        """C^5 at self-dual point: kappa = 1."""
        assert kappa_affine_cy(5) == Fraction(1)

    def test_kappa_c6_self_dual(self):
        """C^6 at self-dual point: kappa = 1."""
        assert kappa_affine_cy(6) == Fraction(1)

    def test_kappa_k3xk3(self):
        """K3 x K3: kappa = 48 (additivity: 24 + 24)."""
        assert kappa_k3_cross_k3() == Fraction(48)

    def test_kappa_sextic_cy4(self):
        """Sextic CY4: kappa = 1 (from chi(O) = 2)."""
        assert kappa_sextic_cy4() == Fraction(1)

    def test_kappa_cy4_bcov_formula(self):
        """CY4 BCOV-type formula: kappa = chi(O)/2."""
        # chi(O) for sextic = 2
        assert kappa_cy4_bcov(2) == Fraction(1)
        # chi(O) for K3 x K3: chi(O_{K3})^2 = 4
        assert kappa_cy4_bcov(4) == Fraction(2)

    def test_kappa_consistent_self_dual(self):
        """All C^d at self-dual have kappa = 1 (Heisenberg truncation)."""
        for d in range(3, 10):
            assert kappa_affine_cy(d) == Fraction(1), f"C^{d}: kappa should be 1"

    def test_shadow_tower_c4(self):
        """C^4 shadow tower: class G at self-dual point."""
        st = shadow_tower_affine_cy(4)
        assert st.shadow_class == "G"
        assert st.shadow_depth == 2
        assert st.kappa == Fraction(1)


# =========================================================================
# 11. Cross-volume consistency (6 tests)
# =========================================================================

class TestCrossVolumeConsistency:
    """Consistency with Vol I and Vol III existing results."""

    def test_sn_bracket_vanishes_d3(self):
        """SN bracket vanishes for d=3 (matches thm:c3-abelian-bracket)."""
        assert sn_bracket_vanishes_affine(3)

    def test_sn_bracket_vanishes_d4(self):
        """SN bracket vanishes for d>=4."""
        for d in range(4, 10):
            assert sn_bracket_vanishes_affine(d), f"d={d}: SN bracket should vanish"

    def test_shadow_k3xk3_class_G(self):
        """K3 x K3 shadow tower is class G (Gaussian, lattice VOA)."""
        st = shadow_tower_k3_cross_k3()
        assert st.shadow_class == "G"
        assert st.shadow_depth == 2

    def test_full_summary_generates(self):
        """full_summary() generates without error and all checks pass."""
        summary = full_summary()
        assert summary["bott_verified"]
        assert summary["cross_checks_verified"]

    def test_all_bott_checks(self):
        """All Bott periodicity checks pass."""
        checks = verify_all_bott()
        for name, result in checks.items():
            assert result, f"Bott check failed: {name}"

    def test_all_cross_checks(self):
        """All cross-checks with d <= 3 pass."""
        checks = verify_all_cross_checks()
        for name, result in checks.items():
            assert result, f"Cross-check failed: {name}"


# =========================================================================
# 12. Obstruction helper functions (5 tests)
# =========================================================================

class TestObstructionHelpers:
    """Test the obstruction classification helper functions."""

    def test_trivial_0(self):
        """'0' is trivial."""
        assert obstruction_is_trivial("0")

    def test_nontrivial_Z(self):
        """'Z' is nontrivial."""
        assert not obstruction_is_trivial("Z")

    def test_nontrivial_Z2(self):
        """'Z_2' is nontrivial."""
        assert not obstruction_is_trivial("Z_2")

    def test_order_Z(self):
        """Z has infinite order."""
        assert obstruction_order("Z") is None

    def test_order_Z2(self):
        """Z_2 has order 2."""
        assert obstruction_order("Z_2") == 2


# =========================================================================
# 13. Deformation space dimensions (5 tests)
# =========================================================================

class TestDeformationSpace:
    """Deformation space dimensions for C^d."""

    def test_c3_1dim(self):
        """C^3: 1 deformation parameter (sigma_3)."""
        hc = hochschild_affine_cy(3)
        assert hc.sigma_dim == 1

    def test_c4_2dim(self):
        """C^4: 2 deformation parameters (sigma_3, sigma_4)."""
        hc = hochschild_affine_cy(4)
        assert hc.sigma_dim == 2

    def test_c5_3dim(self):
        """C^5: 3 deformation parameters."""
        hc = hochschild_affine_cy(5)
        assert hc.sigma_dim == 3

    def test_cd_d_minus_2(self):
        """C^d: d-2 deformation parameters for d >= 3."""
        for d in range(3, 10):
            hc = hochschild_affine_cy(d)
            assert hc.sigma_dim == d - 2, f"C^{d}: should have {d-2} params"

    def test_btt_holds(self):
        """BTT (Bogomolov-Tian-Todorov) holds for all C^d."""
        for d in range(3, 10):
            hc = hochschild_affine_cy(d)
            assert hc.btt_holds


# =========================================================================
# 14. Framing obstruction detailed (6 tests)
# =========================================================================

class TestFramingObstructionDetailed:
    """Detailed tests of the framing obstruction structure."""

    def test_d3_trivial_all(self):
        """d=3: both BU and refined obstruction trivial."""
        fo = framing_obstruction(3)
        assert fo.bu_trivial
        assert fo.refined_trivial

    def test_d4_nontrivial_all(self):
        """d=4: BU nontrivial (Z), refined also Z."""
        fo = framing_obstruction(4)
        assert not fo.bu_trivial
        assert fo.bu_obstruction == "Z"
        assert fo.refined_group == "Z"

    def test_d5_mixed(self):
        """d=5: BU trivial, refined Z_2 (Sp refinement)."""
        fo = framing_obstruction(5)
        assert fo.bu_trivial
        assert fo.refined_group == "Z_2"
        assert not fo.refined_trivial

    def test_d6_bu_nontrivial_bo_trivial(self):
        """d=6: BU = Z (nontrivial), BO = 0 (trivial)."""
        fo = framing_obstruction(6)
        assert not fo.bu_trivial
        assert fo.bu_obstruction == "Z"
        assert fo.refined_group == "0"
        assert fo.refined_trivial

    def test_d7_both_trivial(self):
        """d=7: both BU and BSp trivial."""
        fo = framing_obstruction(7)
        assert fo.bu_trivial
        assert fo.refined_trivial

    def test_characteristic_class_d4(self):
        """d=4: characteristic class is first Pontryagin class."""
        fo = framing_obstruction(4)
        assert "p_1" in fo.characteristic_class
