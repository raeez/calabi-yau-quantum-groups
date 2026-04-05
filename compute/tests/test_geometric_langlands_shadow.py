r"""Tests for compute.lib.geometric_langlands_shadow.

Comprehensive verification of the geometric Langlands programme
from the shadow obstruction tower perspective:
  - Critical level kappa vanishing for all simple types
  - Feigin-Frenkel duality and kappa anti-symmetry
  - Langlands dual shadow comparison (self-dual and non-self-dual)
  - Shadow connection degeneration at critical level
  - Wakimoto module decomposition
  - Kapustin-Witten parameter and quantum geometric Langlands
  - Hitchin system dimensions
  - Oper structure
  - Automorphic shadow amplitudes

Key formula (Vol I, AP1 verified):
    kappa(g_hat_k) = dim(g) * (k + h^v) / (2 * h^v)
"""

import math
from fractions import Fraction

import pytest

import numpy as np

from compute.lib.geometric_langlands_shadow import (
    KWLimitData,
    LieAlgebraData,
    automorphic_shadow_P1,
    central_charge_affine,
    central_charge_residue,
    critical_level,
    critical_level_shadow_tower,
    ff_dual_level,
    ff_duality_table,
    full_computation,
    hitchin_base_dimension,
    hitchin_base_graded_dimension,
    hitchin_hamiltonians_sl2_genus2,
    is_self_dual,
    kappa_affine,
    kappa_affine_float,
    kappa_beta_gamma,
    kappa_heisenberg,
    kappa_near_critical,
    kappa_slope_at_critical,
    kapustin_witten_A_model,
    kapustin_witten_B_model,
    kapustin_witten_full_analysis,
    kapustin_witten_psi,
    kapustin_witten_psi_exact,
    kw_duality_check,
    langlands_dual_data,
    langlands_dual_kappa_table,
    langlands_kappa_ratio_bc,
    langlands_shadow_comparison,
    lie_data,
    oper_connection_sl2,
    oper_from_shadow_degeneration,
    oper_structure,
    quantum_langlands_levels,
    shadow_amplitude_genus1,
    shadow_amplitude_genus2,
    shadow_connection_residue,
    shadow_generating_function_coefficients,
    shadow_metric_affine,
    so5_sp4_shadow_comparison,
    sugawara_residue_and_pole,
    verify_all,
    verify_ff_kappa_antisymmetry,
    wakimoto_decomposition_general,
    wakimoto_decomposition_sl2,
)


# =====================================================================
# 1. LIE ALGEBRA DATA TESTS
# =====================================================================

class TestLieAlgebraData:
    """Verify root datum for simple Lie algebras."""

    def test_sl2_data(self):
        """sl_2 = A_1: dim 3, h = h^v = 2."""
        d = lie_data('A', 1)
        assert d.type == 'A'
        assert d.rank == 1
        assert d.dim == 3
        assert d.h == 2
        assert d.h_dual == 2
        assert d.num_pos_roots == 1

    def test_sl3_data(self):
        """sl_3 = A_2: dim 8, h = h^v = 3."""
        d = lie_data('A', 2)
        assert d.dim == 8
        assert d.h == 3
        assert d.h_dual == 3
        assert d.num_pos_roots == 3
        assert d.rank == 2

    def test_sl4_data(self):
        """sl_4 = A_3: dim 15, h = h^v = 4."""
        d = lie_data('A', 3)
        assert d.dim == 15
        assert d.h == 4
        assert d.h_dual == 4

    def test_so5_data(self):
        """so_5 = B_2: dim 10, h = 4, h^v = 3."""
        d = lie_data('B', 2)
        assert d.dim == 10
        assert d.h == 4
        assert d.h_dual == 3
        assert d.num_pos_roots == 4
        assert d.lacing == 2

    def test_sp4_data(self):
        """sp_4 = C_2: dim 10, h = 4, h^v = 3."""
        d = lie_data('C', 2)
        assert d.dim == 10
        assert d.h == 4
        assert d.h_dual == 3
        assert d.num_pos_roots == 4

    def test_g2_data(self):
        """G_2: dim 14, h = 6, h^v = 4."""
        d = lie_data('G', 2)
        assert d.dim == 14
        assert d.h == 6
        assert d.h_dual == 4
        assert d.num_pos_roots == 6
        assert d.lacing == 3

    def test_e8_data(self):
        """E_8: dim 248, h = h^v = 30."""
        d = lie_data('E', 8)
        assert d.dim == 248
        assert d.h == 30
        assert d.h_dual == 30
        assert d.rank == 8

    def test_f4_data(self):
        """F_4: dim 52, h = 12, h^v = 9."""
        d = lie_data('F', 4)
        assert d.dim == 52
        assert d.h == 12
        assert d.h_dual == 9

    def test_dim_formula_A(self):
        """dim(sl_N) = N^2 - 1 for several N."""
        for n in range(1, 5):
            d = lie_data('A', n)
            assert d.dim == (n + 1)**2 - 1

    def test_simply_laced_h_equals_h_dual(self):
        """For simply-laced types (ADE), h = h^v."""
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('D', 4), ('E', 6), ('E', 7), ('E', 8)]:
            d = lie_data(t, r)
            assert d.h == d.h_dual, f"{t}{r}: h={d.h} != h^v={d.h_dual}"

    def test_non_simply_laced_h_neq_h_dual(self):
        """For non-simply-laced types (BCF G), h != h^v."""
        for t, r in [('B', 2), ('C', 2), ('G', 2), ('F', 4)]:
            d = lie_data(t, r)
            assert d.h != d.h_dual, f"{t}{r}: h should differ from h^v"

    def test_bc_same_dimension(self):
        """B_n and C_n have the same dimension: n(2n+1)."""
        for n in [2, 3, 4]:
            d_b = lie_data('B', n)
            d_c = lie_data('C', n)
            assert d_b.dim == d_c.dim == n * (2 * n + 1)


# =====================================================================
# 2. CRITICAL LEVEL TESTS
# =====================================================================

class TestCriticalLevel:
    """Verify kappa vanishing at critical level k = -h^v."""

    def test_kappa_zero_sl2(self):
        """kappa(sl_2_hat_{-2}) = 0."""
        kap = kappa_affine('A', 1, Fraction(-2))
        assert kap == 0

    def test_kappa_zero_sl3(self):
        """kappa(sl_3_hat_{-3}) = 0."""
        kap = kappa_affine('A', 2, Fraction(-3))
        assert kap == 0

    def test_kappa_zero_so5(self):
        """kappa(B_2_hat_{-3}) = 0. h^v(B_2) = 3."""
        kap = kappa_affine('B', 2, Fraction(-3))
        assert kap == 0

    def test_kappa_zero_sp4(self):
        """kappa(C_2_hat_{-3}) = 0. h^v(C_2) = 3."""
        kap = kappa_affine('C', 2, Fraction(-3))
        assert kap == 0

    def test_kappa_zero_g2(self):
        """kappa(G_2_hat_{-4}) = 0. h^v(G_2) = 4."""
        kap = kappa_affine('G', 2, Fraction(-4))
        assert kap == 0

    def test_kappa_zero_e8(self):
        """kappa(E_8_hat_{-30}) = 0. h^v(E_8) = 30."""
        kap = kappa_affine('E', 8, Fraction(-30))
        assert kap == 0

    def test_kappa_zero_f4(self):
        """kappa(F_4_hat_{-9}) = 0. h^v(F_4) = 9."""
        kap = kappa_affine('F', 4, Fraction(-9))
        assert kap == 0

    def test_critical_level_value_sl2(self):
        """Critical level for sl_2 is k = -2."""
        assert critical_level('A', 1) == Fraction(-2)

    def test_critical_level_value_g2(self):
        """Critical level for G_2 is k = -4."""
        assert critical_level('G', 2) == Fraction(-4)

    def test_sugawara_pole_sl2(self):
        """Sugawara c is None at critical level for sl_2."""
        c = central_charge_affine('A', 1, Fraction(-2))
        assert c is None

    def test_sugawara_pole_sl3(self):
        """Sugawara c is None at critical level for sl_3."""
        c = central_charge_affine('A', 2, Fraction(-3))
        assert c is None


# =====================================================================
# 3. KAPPA FORMULA TESTS (AP1 VERIFIED)
# =====================================================================

class TestKappaFormula:
    """Verify kappa = dim(g) * (k + h^v) / (2 * h^v) at specific levels."""

    def test_sl2_level1(self):
        """kappa(sl_2_hat_1) = 3 * 3 / 4 = 9/4."""
        kap = kappa_affine('A', 1, Fraction(1))
        assert kap == Fraction(9, 4)

    def test_sl2_level2(self):
        """kappa(sl_2_hat_2) = 3 * 4 / 4 = 3."""
        kap = kappa_affine('A', 1, Fraction(2))
        assert kap == Fraction(3)

    def test_sl3_level1(self):
        """kappa(sl_3_hat_1) = 8 * 4 / 6 = 16/3."""
        kap = kappa_affine('A', 2, Fraction(1))
        assert kap == Fraction(16, 3)

    def test_sl3_level3(self):
        """kappa(sl_3_hat_3) = 8 * 6 / 6 = 8."""
        kap = kappa_affine('A', 2, Fraction(3))
        assert kap == Fraction(8)

    def test_central_charge_sl2_level1(self):
        """c(sl_2_hat_1) = 3 * 1 / 3 = 1."""
        c = central_charge_affine('A', 1, Fraction(1))
        assert c == Fraction(1)

    def test_central_charge_sl2_level_minus1(self):
        """c(sl_2_hat_{-1}) = 3 * (-1) / 1 = -3."""
        c = central_charge_affine('A', 1, Fraction(-1))
        assert c == Fraction(-3)

    def test_central_charge_residue_sl2(self):
        """Residue of c at critical for sl_2: -3 * 2 = -6."""
        res = central_charge_residue('A', 1)
        assert res == Fraction(-6)

    def test_central_charge_residue_sl3(self):
        """Residue of c at critical for sl_3: -8 * 3 = -24."""
        res = central_charge_residue('A', 2)
        assert res == Fraction(-24)


# =====================================================================
# 4. FEIGIN-FRENKEL DUALITY TESTS
# =====================================================================

class TestFeiginFrenkelDuality:
    """Verify FF duality: k' = -k - 2h^v and kappa(k) + kappa(k') = 0."""

    def test_ff_involution_sl2(self):
        """FF dual level for sl_2: k' = -k - 4."""
        assert ff_dual_level('A', 1, Fraction(1)) == Fraction(-5)
        assert ff_dual_level('A', 1, Fraction(2)) == Fraction(-6)

    def test_ff_involution_is_involution(self):
        """(k')' = k for all types."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('C', 2), ('G', 2)]:
            for k in [Fraction(1), Fraction(3), Fraction(-1)]:
                k_dual = ff_dual_level(t, r, k)
                k_back = ff_dual_level(t, r, k_dual)
                assert k_back == k, f"{t}{r}, k={k}: (k')' = {k_back} != k"

    def test_ff_fixed_point_critical(self):
        """Critical level is the fixed point of FF involution."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('G', 2), ('E', 8)]:
            k_crit = critical_level(t, r)
            k_dual = ff_dual_level(t, r, k_crit)
            assert k_dual == k_crit, f"{t}{r}: critical level not fixed by FF"

    def test_kappa_antisymmetry_sl2(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0 for k = 1, 2, 3, 10."""
        for k in [Fraction(1), Fraction(2), Fraction(3), Fraction(10)]:
            check = verify_ff_kappa_antisymmetry('A', 1, k)
            assert check['antisymmetric'], f"k={k}: sum = {check['sum']}"

    def test_kappa_antisymmetry_sl3(self):
        """kappa(sl_3, k) + kappa(sl_3, -k-6) = 0."""
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            check = verify_ff_kappa_antisymmetry('A', 2, k)
            assert check['antisymmetric'], f"k={k}: sum = {check['sum']}"

    def test_kappa_antisymmetry_b2(self):
        """kappa(B_2, k) + kappa(B_2, -k-6) = 0."""
        for k in [Fraction(1), Fraction(3)]:
            check = verify_ff_kappa_antisymmetry('B', 2, k)
            assert check['antisymmetric'], f"k={k}: sum = {check['sum']}"

    def test_kappa_antisymmetry_g2(self):
        """kappa(G_2, k) + kappa(G_2, -k-8) = 0."""
        check = verify_ff_kappa_antisymmetry('G', 2, Fraction(1))
        assert check['antisymmetric']

    def test_kappa_antisymmetry_half_integer(self):
        """FF anti-symmetry at half-integer level."""
        check = verify_ff_kappa_antisymmetry('A', 1, Fraction(1, 2))
        assert check['antisymmetric']

    def test_ff_duality_table_all_pass(self):
        """Full duality table for sl_2 all pass."""
        table = ff_duality_table('A', 1)
        for entry in table:
            assert entry['antisymmetric'], f"k={entry['k']}: failed"


# =====================================================================
# 5. LANGLANDS DUAL TESTS
# =====================================================================

class TestLanglandsDual:
    """Test Langlands dual shadow comparison."""

    def test_sl_n_self_dual(self):
        """sl_N is Langlands self-dual for all N."""
        for n in range(1, 5):
            assert is_self_dual('A', n), f"A{n} should be self-dual"

    def test_d_n_self_dual(self):
        """so_{2n} (D_n) is self-dual."""
        for n in [4, 5]:
            assert is_self_dual('D', n)

    def test_e_self_dual(self):
        """E_6, E_7, E_8 are self-dual."""
        for n in [6, 7, 8]:
            assert is_self_dual('E', n)

    def test_g2_self_dual(self):
        """G_2 is Langlands self-dual."""
        assert is_self_dual('G', 2)

    def test_b2_not_self_dual(self):
        """B_2 (so_5) is NOT self-dual: B_2^v = C_2 (sp_4)."""
        assert not is_self_dual('B', 2)
        d = lie_data('B', 2)
        assert d.langlands_dual_type == 'C'
        assert d.langlands_dual_rank == 2

    def test_c2_not_self_dual(self):
        """C_2 (sp_4) is NOT self-dual: C_2^v = B_2 (so_5)."""
        assert not is_self_dual('C', 2)
        d = lie_data('C', 2)
        assert d.langlands_dual_type == 'B'
        assert d.langlands_dual_rank == 2

    def test_f4_self_dual(self):
        """F_4 is Langlands self-dual."""
        assert is_self_dual('F', 4)

    def test_langlands_kappa_ratio_b2c2(self):
        """kappa(C_2, k=1) / kappa(B_2, k=1) uses h^v ratio."""
        ratio = langlands_kappa_ratio_bc(2, Fraction(1))
        # B_2: h^v=3, C_2: h^v=3. Same! So ratio = (1+3)*3/((1+3)*3) = 1.
        # Wait: B_2 h^v = 3 and C_2 h^v = 3 as well (both rank 2).
        # Actually C_2: h^v = n+1 = 3. B_2: h^v = 2n-1 = 3. So both = 3.
        assert ratio == 1

    def test_langlands_kappa_ratio_b3c3(self):
        """B_3 and C_3 have different h^v: h^v(B_3)=5, h^v(C_3)=4."""
        ratio = langlands_kappa_ratio_bc(3, Fraction(1))
        # ratio = (k + h^v_C) * h^v_B / ((k + h^v_B) * h^v_C)
        # = (1 + 4) * 5 / ((1 + 5) * 4) = 25/24
        assert ratio == Fraction(25, 24)

    def test_langlands_comparison_self_dual(self):
        """For self-dual sl_2, kappa(G) = kappa(G^v) at same level."""
        comp = langlands_shadow_comparison('A', 1, Fraction(1))
        assert comp.is_self_dual
        assert comp.kappa_g == comp.kappa_gv

    def test_langlands_comparison_b2c2(self):
        """B_2/C_2 have same dim, so kappa ratio = h^v ratio."""
        comp = langlands_shadow_comparison('B', 2, Fraction(1))
        assert not comp.is_self_dual
        # Both have dim = 10 and h^v = 3, so kappa values are identical
        assert comp.kappa_g == comp.kappa_gv


# =====================================================================
# 6. SHADOW CONNECTION TESTS
# =====================================================================

class TestShadowConnection:
    """Shadow connection degeneration at critical level."""

    def test_shadow_metric_positive_level(self):
        """Shadow metric at t=0 is 4*kappa^2 > 0 for positive level."""
        Q = shadow_metric_affine('A', 1, Fraction(1))
        kap = float(kappa_affine('A', 1, Fraction(1)))
        assert abs(Q - 4 * kap**2) < 1e-10

    def test_shadow_metric_critical_vanishes(self):
        """Shadow metric vanishes at critical level (kappa = 0)."""
        Q = shadow_metric_affine('A', 1, Fraction(-2))
        assert abs(Q) < 1e-15

    def test_connection_residue_generic(self):
        """Shadow connection residue is 1/2 at generic level."""
        res = shadow_connection_residue('A', 1, Fraction(1))
        assert res == Fraction(1, 2)

    def test_connection_residue_critical_degenerate(self):
        """Shadow connection is degenerate at critical level."""
        res = shadow_connection_residue('A', 1, Fraction(-2))
        assert res is None


# =====================================================================
# 7. WAKIMOTO MODULE TESTS
# =====================================================================

class TestWakimotoDecomposition:
    """Wakimoto free-field realization from shadow perspective."""

    def test_beta_gamma_kappa(self):
        """kappa(beta-gamma) = -1/2."""
        assert kappa_beta_gamma() == Fraction(-1, 2)

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        assert kappa_heisenberg(Fraction(3)) == Fraction(3)

    def test_wakimoto_sl2_level1(self):
        """Wakimoto for sl_2 at k=1: kappa_bg + kappa_H = 9/4."""
        w = wakimoto_decomposition_sl2(Fraction(1))
        assert w['matches']
        assert w['kappa_total'] == Fraction(9, 4)
        assert w['kappa_beta_gamma'] == Fraction(-1, 2)
        assert w['kappa_heisenberg'] == Fraction(11, 4)

    def test_wakimoto_sl2_critical(self):
        """Wakimoto at critical level k=-2: total kappa = 0."""
        w = wakimoto_decomposition_sl2(Fraction(-2))
        assert w['matches']
        assert w['kappa_total'] == 0
        assert w['kappa_heisenberg'] == Fraction(1, 2)

    def test_wakimoto_sl3_level1(self):
        """Wakimoto for sl_3 at k=1: 3 bg pairs + 2 Heisenberg fields."""
        w = wakimoto_decomposition_general('A', 2, Fraction(1))
        assert w['matches']
        assert w['num_bg_pairs'] == 3
        assert w['kappa_total'] == Fraction(16, 3)
        assert w['kappa_bg_total'] == Fraction(-3, 2)
        # cartan = 16/3 + 3/2 = 32/6 + 9/6 = 41/6
        assert w['kappa_cartan'] == Fraction(41, 6)

    def test_wakimoto_general_critical(self):
        """At critical level, bg + Cartan = 0 for all types."""
        for t, r in [('A', 1), ('A', 2), ('B', 2)]:
            k_crit = critical_level(t, r)
            w = wakimoto_decomposition_general(t, r, k_crit)
            assert w['matches']
            assert w['kappa_total'] == 0


# =====================================================================
# 8. KAPUSTIN-WITTEN TESTS
# =====================================================================

class TestKapustinWitten:
    """Kapustin-Witten parameter Psi = k/(k+h^v)."""

    def test_psi_sl2_level1(self):
        """Psi(sl_2, k=1) = 1/3."""
        psi = kapustin_witten_psi_exact('A', 1, Fraction(1))
        assert psi == Fraction(1, 3)

    def test_psi_critical_undefined(self):
        """Psi is undefined at critical level."""
        psi = kapustin_witten_psi_exact('A', 1, Fraction(-2))
        assert psi is None

    def test_psi_zero_at_k_zero(self):
        """Psi = 0 at k = 0 (A-model / Hitchin limit)."""
        psi = kapustin_witten_psi_exact('A', 1, Fraction(0))
        assert psi == 0

    def test_psi_approaches_one_large_k(self):
        """Psi -> 1 as k -> infinity."""
        psi = kapustin_witten_psi('A', 1, 1000.0)
        assert abs(psi - 1.0) < 0.01

    def test_psi_float_consistency(self):
        """Float and exact Psi agree."""
        psi_exact = kapustin_witten_psi_exact('A', 1, Fraction(3))
        psi_float = kapustin_witten_psi('A', 1, 3.0)
        assert abs(float(psi_exact) - psi_float) < 1e-12

    def test_kw_duality_sl2_self_dual(self):
        """Quantum GL duality for sl_2 (self-dual): Psi * Psi^v = 1."""
        check = kw_duality_check('A', 1, Fraction(1))
        # k^v = -1 - 2 = -3 for the quantum GL level map
        # Psi = 1/3, Psi^v = -3/(-3+2) = -3/(-1) = 3.
        # Product = 1/3 * 3 = 1.
        assert check['is_dual']

    def test_kw_duality_sl2_level3(self):
        """Quantum GL duality at k=3 for sl_2."""
        check = kw_duality_check('A', 1, Fraction(3))
        assert check['is_dual']


# =====================================================================
# 9. HITCHIN SYSTEM TESTS
# =====================================================================

class TestHitchinSystem:
    """Hitchin base dimensions from critical-level shadow."""

    def test_hitchin_base_sl2_g2(self):
        """Hitchin base for SL_2 on genus-2 curve: dim = 3."""
        assert hitchin_base_dimension('A', 1, 2) == 3

    def test_hitchin_base_sl3_g2(self):
        """Hitchin base for SL_3 on genus-2 curve: dim = 8."""
        assert hitchin_base_dimension('A', 2, 2) == 8

    def test_hitchin_base_e8_g2(self):
        """Hitchin base for E_8 on genus-2 curve: dim = 248."""
        assert hitchin_base_dimension('E', 8, 2) == 248

    def test_hitchin_graded_sl2_g2(self):
        """Graded Hitchin base for SL_2, g=2: one component of degree 2."""
        graded = hitchin_base_graded_dimension('A', 1, 2)
        # Casimir degree 2: dim = (2*2-1)*(2-1) = 3
        assert graded == {2: 3}

    def test_hitchin_graded_sl3_g2(self):
        """Graded Hitchin base for SL_3, g=2: degrees 2 and 3."""
        graded = hitchin_base_graded_dimension('A', 2, 2)
        # Degree 2: (3)*(1) = 3; Degree 3: (5)*(1) = 5; total = 8.
        assert graded[2] == 3
        assert graded[3] == 5
        assert sum(graded.values()) == 8

    def test_hitchin_graded_total_equals_dim(self):
        """Sum of graded dimensions equals total Hitchin base dimension."""
        for (t, r), g in [(('A', 1), 2), (('A', 2), 2), (('A', 2), 3),
                          (('B', 2), 2), (('E', 6), 2)]:
            graded = hitchin_base_graded_dimension(t, r, g)
            total = hitchin_base_dimension(t, r, g)
            assert sum(graded.values()) == total, \
                f"{t}{r}, g={g}: graded sum {sum(graded.values())} != {total}"


# =====================================================================
# 10. OPER STRUCTURE TESTS
# =====================================================================

class TestOperStructure:
    """Oper data for the Langlands dual group."""

    def test_oper_sl2_g2(self):
        """Oper for PGL_2 (dual of SL_2) on genus-2: dim = 3."""
        op = oper_structure('A', 1, 2)
        assert op.rank == 1
        assert op.num_oper_parameters == 3  # = dim(SL_2) * (2-1)
        assert 2 in op.casimir_degrees  # quadratic differential

    def test_oper_sl3_g2(self):
        """Oper for PGL_3 (dual of SL_3) on genus-2: dim = 8."""
        op = oper_structure('A', 2, 2)
        assert op.num_oper_parameters == 8
        assert op.casimir_degrees == (2, 3)

    def test_oper_dimension_equals_hitchin(self):
        """Oper space dimension = Hitchin base dimension (BD theorem)."""
        for (t, r), g in [(('A', 1), 2), (('A', 2), 2), (('B', 2), 3)]:
            op = oper_structure(t, r, g)
            hb = hitchin_base_dimension(t, r, g)
            assert op.num_oper_parameters == hb


# =====================================================================
# 11. CRITICAL LEVEL SHADOW TOWER TESTS
# =====================================================================

class TestCriticalLevelShadowTower:
    """Shadow obstruction tower collapse at the critical level."""

    def test_shadow_tower_sl2_kappa_sequence(self):
        """kappa -> 0 as epsilon -> 0 for sl_2."""
        tower = critical_level_shadow_tower('A', 1)
        data = tower['data']
        kappas = [d['kappa'] for d in data]
        # Should be decreasing toward 0
        for i in range(len(kappas) - 1):
            assert kappas[i] > kappas[i + 1]
        assert kappas[-1] < 1e-3

    def test_shadow_tower_sl2_F1_vanishes(self):
        """F_1 -> 0 as we approach critical level."""
        tower = critical_level_shadow_tower('A', 1)
        data = tower['data']
        assert data[-1]['F_1'] < 1e-3  # Last epsilon = 0.0001, F_1 ~ 1e-5

    def test_shadow_tower_central_charge_diverges(self):
        """Central charge diverges as epsilon -> 0."""
        tower = critical_level_shadow_tower('A', 1)
        data = tower['data']
        # |c| should increase
        c_abs = [abs(d['central_charge']) for d in data]
        for i in range(len(c_abs) - 1):
            assert c_abs[i] < c_abs[i + 1]

    def test_kappa_near_critical_exact(self):
        """kappa at k = -h^v + eps is dim*eps/(2*h^v)."""
        # sl_2: dim=3, h^v=2. eps=1/10: kappa = 3/(2*2*10) = 3/40.
        kap = kappa_near_critical('A', 1, Fraction(1, 10))
        assert kap == Fraction(3, 40)


# =====================================================================
# 12. AUTOMORPHIC SHADOW TESTS
# =====================================================================

class TestAutomorphicShadow:
    """Shadow amplitudes at integral levels."""

    def test_F1_sl2_level1(self):
        """F_1(sl_2, k=1) = kappa/24 = (9/4)/24 = 3/32."""
        F1 = shadow_amplitude_genus1('A', 1, 1)
        assert F1 == Fraction(3, 32)

    def test_F1_sl2_level2(self):
        """F_1(sl_2, k=2) = 3/24 = 1/8."""
        F1 = shadow_amplitude_genus1('A', 1, 2)
        assert F1 == Fraction(1, 8)

    def test_F2_sl2_level1(self):
        """F_2(sl_2, k=1) = (9/4)/1152 = 3/1536 = 1/512."""
        F2 = shadow_amplitude_genus2('A', 1, 1)
        assert F2 == Fraction(9, 4) / 1152
        # Simplify: 9/(4*1152) = 9/4608 = 3/1536 = 1/512
        assert F2 == Fraction(1, 512)

    def test_generating_function_sl2_level1(self):
        """Shadow generating function for sl_2, k=1."""
        gf = shadow_generating_function_coefficients('A', 1, 1, max_genus=2)
        assert gf[1] == Fraction(3, 32)
        # F_2 = kappa * lambda_2^FP = (9/4) * (1/1152) = 9/4608 = 1/512
        assert gf[2] == Fraction(1, 512)

    def test_generating_function_consistency(self):
        """GF coefficients match direct F_g computations."""
        gf = shadow_generating_function_coefficients('A', 1, 1, max_genus=2)
        assert gf[1] == shadow_amplitude_genus1('A', 1, 1)
        assert gf[2] == shadow_amplitude_genus2('A', 1, 1)


# =====================================================================
# 13. QUANTUM GEOMETRIC LANGLANDS TESTS
# =====================================================================

class TestQuantumGeometricLanglands:
    """Quantum geometric Langlands level correspondence."""

    def test_qgl_sl2_critical_maps_to_zero(self):
        """Critical level of G maps to level 0 of G^v (for self-dual)."""
        result = quantum_langlands_levels('A', 1, Fraction(-2))
        # k = -2 (critical for sl_2), k^v = -(-2) - 2 = 0
        assert result['k_dual'] == 0

    def test_qgl_sl2_kappa_sum(self):
        """kappa(G, k) + kappa(G^v, k^v) for quantum GL."""
        result = quantum_langlands_levels('A', 1, Fraction(1))
        # k = 1: kappa(sl_2, 1) = 9/4
        # k^v = -1 - 2 = -3: kappa(sl_2, -3) = 3*(-3+2)/4 = 3*(-1)/4 = -3/4
        # Sum = 9/4 - 3/4 = 6/4 = 3/2
        assert result['kappa_sum'] == Fraction(3, 2)

    def test_qgl_b2_critical_maps_to_zero(self):
        """Critical level of B_2 maps to level 0 of C_2."""
        result = quantum_langlands_levels('B', 2, Fraction(-3))
        assert result['k_dual'] == 0

    def test_qgl_zero_maps_to_critical(self):
        """Level 0 of G maps to critical level of G^v (for self-dual)."""
        result = quantum_langlands_levels('A', 1, Fraction(0))
        # k = 0: k^v = -0 - 2 = -2 (critical!)
        assert result['k_dual'] == Fraction(-2)


# =====================================================================
# 14. CROSS-CONSISTENCY TESTS
# =====================================================================

class TestCrossConsistency:
    """Cross-checks between different computations."""

    def test_wakimoto_critical_all_types(self):
        """Wakimoto gives kappa=0 at critical level for all tested types."""
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('G', 2)]:
            k_crit = critical_level(t, r)
            w = wakimoto_decomposition_general(t, r, k_crit)
            assert w['kappa_total'] == 0, f"{t}{r} failed"
            assert w['matches'], f"{t}{r} decomposition failed"

    def test_oper_hitchin_all_types(self):
        """Oper dim = Hitchin base dim for several (G, g) pairs."""
        for (t, r), g in [(('A', 1), 2), (('A', 2), 2), (('A', 3), 2),
                           (('B', 2), 2), (('C', 2), 2), (('D', 4), 2),
                           (('E', 6), 2)]:
            op = oper_structure(t, r, g)
            hb = hitchin_base_dimension(t, r, g)
            assert op.num_oper_parameters == hb, \
                f"{t}{r}, g={g}: oper={op.num_oper_parameters} != hitchin={hb}"

    def test_kappa_float_exact_agreement(self):
        """Float and exact kappa agree within tolerance."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('G', 2)]:
            for k in [1, 2, 5, -1]:
                kap_exact = float(kappa_affine(t, r, Fraction(k)))
                kap_float = kappa_affine_float(t, r, float(k))
                assert abs(kap_exact - kap_float) < 1e-12, \
                    f"{t}{r}, k={k}: exact={kap_exact}, float={kap_float}"


# =====================================================================
# 15. INTEGRATION TESTS
# =====================================================================

class TestIntegration:
    """Full computation and verify_all integration tests."""

    def test_verify_all_runs(self):
        """verify_all() runs without error."""
        results = verify_all()
        assert len(results) > 0

    def test_verify_all_critical_kappa_zero(self):
        """All critical-level kappa values in verify_all are zero."""
        results = verify_all()
        for key, val in results.items():
            if key.startswith('kappa_critical_'):
                assert val['is_zero'], f"{key}: kappa = {val['kappa']}"

    def test_verify_all_ff_antisymmetric(self):
        """All FF entries in verify_all are antisymmetric."""
        results = verify_all()
        for key, val in results.items():
            if key.startswith('ff_'):
                assert val['antisymmetric'], f"{key} failed"

    def test_full_computation_runs(self):
        """full_computation() runs without error."""
        result = full_computation()
        assert 'verification' in result
        assert 'critical_tower_sl2' in result
        assert 'opers_sl2_g2' in result
        assert 'so5_sp4' in result
        assert 'kw_sl2' in result
        assert 'hitchin_sl2_g2' in result
        assert 'automorphic_P1_sl2' in result


# =====================================================================
# 16. CRITICAL LEVEL RESIDUE TESTS
# =====================================================================

class TestCriticalLevelResidues:
    """Residue analysis at the critical level k = -h^v."""

    def test_kappa_slope_sl2(self):
        """d(kappa)/dk for sl_2 = dim/(2*h^v) = 3/4."""
        slope = kappa_slope_at_critical('A', 1)
        assert slope == Fraction(3, 4)

    def test_kappa_slope_sl3(self):
        """d(kappa)/dk for sl_3 = 8/(2*3) = 4/3."""
        slope = kappa_slope_at_critical('A', 2)
        assert slope == Fraction(4, 3)

    def test_kappa_slope_so5(self):
        """d(kappa)/dk for B_2 (so_5) = 10/(2*3) = 5/3."""
        slope = kappa_slope_at_critical('B', 2)
        assert slope == Fraction(5, 3)

    def test_kappa_slope_sp4(self):
        """d(kappa)/dk for C_2 (sp_4) = 10/(2*3) = 5/3.
        Same as B_2 since dim and h^v coincide at rank 2."""
        slope = kappa_slope_at_critical('C', 2)
        assert slope == Fraction(5, 3)

    def test_kappa_slope_e8(self):
        """d(kappa)/dk for E_8 = 248/(2*30) = 124/30 = 62/15."""
        slope = kappa_slope_at_critical('E', 8)
        assert slope == Fraction(248, 60)
        assert slope == Fraction(62, 15)

    def test_kappa_slope_matches_kappa_near_critical(self):
        """kappa at k = -h^v + epsilon should be slope * epsilon."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('G', 2)]:
            slope = kappa_slope_at_critical(t, r)
            eps = Fraction(1, 100)
            kap = kappa_near_critical(t, r, eps)
            assert kap == slope * eps, f"{t}{r}: {kap} != {slope * eps}"

    def test_sugawara_residue_sl2(self):
        """Sugawara residue at critical for sl_2: -dim*h^v = -6."""
        res = sugawara_residue_and_pole('A', 1)
        assert res['residue'] == Fraction(-6)
        assert res['pole_order'] == 1
        assert res['regular_limit'] == Fraction(3)

    def test_sugawara_residue_sl3(self):
        """Sugawara residue at critical for sl_3: -8*3 = -24."""
        res = sugawara_residue_and_pole('A', 2)
        assert res['residue'] == Fraction(-24)

    def test_sugawara_residue_g2(self):
        """Sugawara residue at critical for G_2: -14*4 = -56."""
        res = sugawara_residue_and_pole('G', 2)
        assert res['residue'] == Fraction(-56)

    def test_sugawara_residue_matches_central_charge_residue(self):
        """sugawara_residue_and_pole matches central_charge_residue."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('C', 2), ('G', 2), ('E', 8)]:
            res_new = sugawara_residue_and_pole(t, r)['residue']
            res_old = central_charge_residue(t, r)
            assert res_new == res_old, f"{t}{r}: {res_new} != {res_old}"


# =====================================================================
# 17. OPER FROM SHADOW DEGENERATION TESTS
# =====================================================================

class TestOperFromShadow:
    """Oper connection derived from shadow metric degeneration."""

    def test_oper_matrix_sl2_structure(self):
        """SL_2 oper matrix has correct [[0,q],[1,0]] structure."""
        A = oper_connection_sl2(3.0)
        assert A.shape == (2, 2)
        assert abs(A[0, 0]) < 1e-15
        assert abs(A[0, 1] - 3.0) < 1e-15
        assert abs(A[1, 0] - 1.0) < 1e-15
        assert abs(A[1, 1]) < 1e-15

    def test_oper_matrix_eigenvalues(self):
        """Eigenvalues of [[0,q],[1,0]] are pm sqrt(q)."""
        for q in [1.0, 4.0, 9.0]:
            A = oper_connection_sl2(q)
            evals = sorted(np.linalg.eigvals(A).real)
            assert abs(evals[0] + math.sqrt(q)) < 1e-10
            assert abs(evals[1] - math.sqrt(q)) < 1e-10

    def test_oper_matrix_traceless(self):
        """SL_2 oper matrix is traceless (in sl_2)."""
        A = oper_connection_sl2(2.5)
        assert abs(np.trace(A)) < 1e-15

    def test_oper_matrix_determinant(self):
        """det([[0,q],[1,0]]) = -q."""
        for q in [1.0, 3.5, 7.0]:
            A = oper_connection_sl2(q)
            assert abs(np.linalg.det(A) + q) < 1e-10

    def test_shadow_degeneration_kappa_vanishes(self):
        """kappa -> 0 as epsilon -> 0 in shadow degeneration."""
        for eps in [1.0, 0.1, 0.01, 0.001]:
            result = oper_from_shadow_degeneration('A', 1, eps)
            expected_kappa = 3.0 * eps / 4.0
            assert abs(result['kappa'] - expected_kappa) < 1e-12

    def test_shadow_degeneration_Q0_quadratic(self):
        """Shadow metric Q_L(0) = 4*kappa^2 vanishes quadratically."""
        eps_values = [1.0, 0.1, 0.01]
        Q_values = [oper_from_shadow_degeneration('A', 1, e)['shadow_metric_Q0']
                    for e in eps_values]
        # Q should scale as epsilon^2
        ratio_1 = Q_values[0] / Q_values[1]
        ratio_2 = Q_values[1] / Q_values[2]
        assert abs(ratio_1 - 100.0) < 1.0  # (1/0.1)^2 = 100
        assert abs(ratio_2 - 100.0) < 1.0  # (0.1/0.01)^2 = 100

    def test_shadow_degeneration_oper_diverges(self):
        """Oper parameter q diverges as 1/epsilon."""
        result_1 = oper_from_shadow_degeneration('A', 1, 1.0)
        result_01 = oper_from_shadow_degeneration('A', 1, 0.1)
        # q ~ -dim*h^v/(12*eps), so q(0.1)/q(1.0) should be ~ 10
        assert result_1['oper_q'] is not None
        assert result_01['oper_q'] is not None
        ratio = result_01['oper_q'] / result_1['oper_q']
        assert abs(ratio - 10.0) < 0.1

    def test_shadow_degeneration_sl3_no_oper(self):
        """Oper parameter q only computed for sl_2."""
        result = oper_from_shadow_degeneration('A', 2, 0.1)
        assert result['oper_q'] is None
        assert result['oper_matrix'] is None

    def test_shadow_degeneration_central_charge_pole(self):
        """Central charge diverges as 1/epsilon near critical level."""
        result = oper_from_shadow_degeneration('A', 1, 0.01)
        # c = 3*(-2+0.01)/0.01 = 3*(-1.99)/0.01 = -597
        assert result['central_charge'] < -500


# =====================================================================
# 18. LANGLANDS DUAL (so_5, sp_4) SHADOW TESTS
# =====================================================================

class TestSo5Sp4Shadow:
    """Langlands dual shadow for (so_5, sp_4) = (B_2, C_2)."""

    def test_b2_c2_same_hdual(self):
        """B_2 and C_2 both have h^v = 3 (rank-2 coincidence)."""
        d_b = lie_data('B', 2)
        d_c = lie_data('C', 2)
        assert d_b.h_dual == 3
        assert d_c.h_dual == 3

    def test_b2_c2_kappa_identical_level1(self):
        """kappa(B_2, k=1) = kappa(C_2, k=1) since dim and h^v coincide."""
        kap_b = kappa_affine('B', 2, Fraction(1))
        kap_c = kappa_affine('C', 2, Fraction(1))
        assert kap_b == kap_c
        assert kap_b == Fraction(20, 3)

    def test_b2_c2_kappa_identical_all_levels(self):
        """kappa(B_2, k) = kappa(C_2, k) for all k (same dim and h^v)."""
        comp = so5_sp4_shadow_comparison()
        assert comp['all_equal_at_rank2']

    def test_b3_c3_kappa_differ(self):
        """kappa(B_3, k=1) != kappa(C_3, k=1): coincidence breaks at rank 3."""
        comp = so5_sp4_shadow_comparison()
        assert not comp['breaks_at_rank3']['equal']
        assert comp['breaks_at_rank3']['kappa_B3_k1'] == Fraction(63, 5)
        assert comp['breaks_at_rank3']['kappa_C3_k1'] == Fraction(105, 8)

    def test_langlands_dual_table_b2(self):
        """Langlands dual kappa table for B_2 at multiple levels."""
        table = langlands_dual_kappa_table('B', 2)
        for row in table:
            if row['kappa_G'] != 0:
                assert row['ratio'] == 1, \
                    f"k={row['level']}: ratio should be 1 for B_2/C_2"

    def test_langlands_dual_table_b3_nontrivial(self):
        """Langlands dual kappa table for B_3 has non-unit ratio."""
        table = langlands_dual_kappa_table('B', 3, [Fraction(1), Fraction(2)])
        for row in table:
            if row['kappa_G'] != 0:
                assert row['ratio'] != 1, \
                    f"k={row['level']}: ratio should differ from 1 for B_3/C_3"

    def test_so5_sp4_critical_level_same(self):
        """B_2 and C_2 have the same critical level k = -3."""
        assert critical_level('B', 2) == Fraction(-3)
        assert critical_level('C', 2) == Fraction(-3)


# =====================================================================
# 19. EXTENDED FEIGIN-FRENKEL DUALITY TESTS
# =====================================================================

class TestFeiginFrenkelExtended:
    """Extended FF duality verification at specific levels."""

    def test_ff_sl2_k1(self):
        """kappa(sl_2, 1) + kappa(sl_2, -5) = 0."""
        kap1 = kappa_affine('A', 1, Fraction(1))
        kap5 = kappa_affine('A', 1, Fraction(-5))
        assert kap1 == Fraction(9, 4)
        assert kap5 == Fraction(-9, 4)
        assert kap1 + kap5 == 0

    def test_ff_sl2_k2(self):
        """kappa(sl_2, 2) + kappa(sl_2, -6) = 0."""
        kap2 = kappa_affine('A', 1, Fraction(2))
        kap6 = kappa_affine('A', 1, Fraction(-6))
        assert kap2 == Fraction(3)
        assert kap6 == Fraction(-3)
        assert kap2 + kap6 == 0

    def test_ff_sl2_k3(self):
        """kappa(sl_2, 3) + kappa(sl_2, -7) = 0."""
        kap3 = kappa_affine('A', 1, Fraction(3))
        kap7 = kappa_affine('A', 1, Fraction(-7))
        assert kap3 == Fraction(15, 4)
        assert kap7 == Fraction(-15, 4)
        assert kap3 + kap7 == 0

    def test_ff_sl2_k10(self):
        """kappa(sl_2, 10) + kappa(sl_2, -14) = 0."""
        kap10 = kappa_affine('A', 1, Fraction(10))
        kap14 = kappa_affine('A', 1, Fraction(-14))
        assert kap10 == Fraction(9)
        assert kap14 == Fraction(-9)
        assert kap10 + kap14 == 0

    def test_ff_sl3_at_specified_levels(self):
        """Verify FF for sl_3 at levels 1, 2, 3, 10."""
        for k in [1, 2, 3, 10]:
            kap = kappa_affine('A', 2, Fraction(k))
            k_dual = ff_dual_level('A', 2, Fraction(k))
            kap_dual = kappa_affine('A', 2, k_dual)
            assert kap + kap_dual == 0, \
                f"sl_3, k={k}: {kap} + {kap_dual} = {kap + kap_dual} != 0"


# =====================================================================
# 20. EXTENDED WAKIMOTO DECOMPOSITION TESTS
# =====================================================================

class TestWakimotoExtended:
    """Extended Wakimoto module decomposition verification."""

    def test_wakimoto_sl2_all_levels(self):
        """Wakimoto decomposition matches for sl_2 at k = 1, 2, 3, 10."""
        for k in [1, 2, 3, 10]:
            w = wakimoto_decomposition_sl2(Fraction(k))
            assert w['matches'], f"sl_2 k={k} failed"
            assert w['kappa_beta_gamma'] == Fraction(-1, 2)

    def test_wakimoto_heisenberg_level_formula_sl2(self):
        """Heisenberg level in sl_2 Wakimoto is (3k+8)/4."""
        for k in [1, 2, 5]:
            w = wakimoto_decomposition_sl2(Fraction(k))
            expected = Fraction(3 * k + 8, 4)
            assert w['heisenberg_level'] == expected, \
                f"k={k}: H_level = {w['heisenberg_level']} != {expected}"

    def test_wakimoto_sl3_bg_count(self):
        """sl_3 Wakimoto uses 3 beta-gamma pairs (= num positive roots)."""
        w = wakimoto_decomposition_general('A', 2, Fraction(1))
        assert w['num_bg_pairs'] == 3

    def test_wakimoto_e8_bg_count(self):
        """E_8 Wakimoto uses 120 beta-gamma pairs."""
        w = wakimoto_decomposition_general('E', 8, Fraction(1))
        assert w['num_bg_pairs'] == 120
        assert w['matches']

    def test_wakimoto_total_kappa_consistency(self):
        """Wakimoto total kappa matches kappa_affine for all tested types."""
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2),
                     ('D', 4), ('G', 2), ('F', 4), ('E', 6)]:
            for k in [1, 3]:
                w = wakimoto_decomposition_general(t, r, Fraction(k))
                assert w['matches'], f"{t}{r} k={k}: decomposition failed"
                expected = kappa_affine(t, r, Fraction(k))
                assert w['kappa_total'] == expected, \
                    f"{t}{r} k={k}: total {w['kappa_total']} != {expected}"


# =====================================================================
# 21. HITCHIN HAMILTONIANS TESTS
# =====================================================================

class TestHitchinHamiltonians:
    """Hitchin system data from critical-level shadow."""

    def test_hitchin_sl2_g2_dimensions(self):
        """SL_2 genus-2 Hitchin: dim_moduli=6, base=3, fibre=3."""
        h = hitchin_hamiltonians_sl2_genus2()
        assert h['dim_moduli'] == 6
        assert h['dim_hitchin_base'] == 3
        assert h['num_hamiltonians'] == 3

    def test_hitchin_sl2_g2_spectral_curve(self):
        """Spectral curve for SL_2 genus-2: genus 5 (Riemann-Hurwitz)."""
        h = hitchin_hamiltonians_sl2_genus2()
        assert h['spectral_curve_genus'] == 5
        # 2g(S)-2 = 2*(2*2-2) + deg(K^2) = 4 + 4 = 8, g(S) = 5

    def test_hitchin_sl2_g2_prym(self):
        """Prym dimension = g(Sigma) - g(C) = 5 - 2 = 3."""
        h = hitchin_hamiltonians_sl2_genus2()
        assert h['prym_dimension'] == 3

    def test_hitchin_sl2_g2_integrable_system(self):
        """The Hitchin system is a completely integrable system."""
        h = hitchin_hamiltonians_sl2_genus2()
        assert h['integrable_system'] is True
        # Base and fibre dimensions must match for complete integrability
        assert h['dim_hitchin_base'] == h['prym_dimension']

    def test_hitchin_kappa_slope(self):
        """Shadow collapse rate matches kappa_slope."""
        h = hitchin_hamiltonians_sl2_genus2()
        assert h['kappa_slope'] == Fraction(3, 4)

    def test_hitchin_casimir_grading(self):
        """Hitchin base for SL_2 has single Casimir of degree 2."""
        h = hitchin_hamiltonians_sl2_genus2()
        assert h['hitchin_casimir_grading'] == {2: 3}


# =====================================================================
# 22. AUTOMORPHIC SHADOW ON P^1 TESTS
# =====================================================================

class TestAutomorphicP1:
    """Automorphic shadow amplitudes on P^1."""

    def test_automorphic_sl2_level1_kappa(self):
        """kappa(sl_2, k=1) = 9/4 on P^1."""
        result = automorphic_shadow_P1('A', 1, 1)
        assert result['kappa'] == Fraction(9, 4)
        assert result['genus'] == 0
        assert result['curve'] == 'P^1'

    def test_automorphic_sl2_level1_integrable_reps(self):
        """sl_2 at level 1 has 2 integrable representations."""
        result = automorphic_shadow_P1('A', 1, 1)
        assert result['num_integrable_representations'] == 2

    def test_automorphic_sl2_level2_integrable_reps(self):
        """sl_2 at level 2 has 3 integrable representations."""
        result = automorphic_shadow_P1('A', 1, 2)
        assert result['num_integrable_representations'] == 3

    def test_automorphic_sl3_level1_integrable_reps(self):
        """sl_3 at level 1 has 3 integrable representations.
        binomial(3+1-1, 1) = binomial(3, 1) = 3."""
        result = automorphic_shadow_P1('A', 2, 1)
        assert result['num_integrable_representations'] == 3

    def test_automorphic_sl3_level2_integrable_reps(self):
        """sl_3 at level 2 has 6 integrable representations.
        binomial(3+2-1, 2) = binomial(4, 2) = 6."""
        result = automorphic_shadow_P1('A', 2, 2)
        assert result['num_integrable_representations'] == 6

    def test_automorphic_vacuum_block(self):
        """Vacuum block dimension is always 1 on P^1."""
        for t, r, k in [('A', 1, 1), ('A', 2, 3), ('B', 2, 2)]:
            result = automorphic_shadow_P1(t, r, k)
            assert result['vacuum_block_dim'] == 1


# =====================================================================
# 23. KAPUSTIN-WITTEN A/B MODEL TESTS
# =====================================================================

class TestKapustinWittenModels:
    """Kapustin-Witten A-model and B-model shadow limits."""

    def test_A_model_sl2_kappa(self):
        """A-model (k=0) for sl_2: kappa = dim/2 = 3/2."""
        kw = kapustin_witten_A_model('A', 1)
        assert kw.kappa == Fraction(3, 2)
        assert kw.regime == 'A-model'
        assert kw.psi_value == '0'

    def test_A_model_sl3_kappa(self):
        """A-model (k=0) for sl_3: kappa = dim/2 = 4."""
        kw = kapustin_witten_A_model('A', 2)
        assert kw.kappa == Fraction(4)

    def test_A_model_kappa_equals_dim_over_2(self):
        """A-model kappa = dim(g)/2 for all types (k=0 formula)."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('C', 2), ('G', 2), ('E', 8)]:
            kw = kapustin_witten_A_model(t, r)
            d = lie_data(t, r)
            assert kw.kappa == Fraction(d.dim, 2), \
                f"{t}{r}: A-model kappa {kw.kappa} != {Fraction(d.dim, 2)}"

    def test_B_model_sl2_large_kappa(self):
        """B-model (k=1000) for sl_2: kappa is large."""
        kw = kapustin_witten_B_model('A', 1)
        assert kw.kappa > 100

    def test_B_model_psi_near_one(self):
        """B-model has Psi near 1."""
        psi = kapustin_witten_psi('A', 1, 1000.0)
        assert abs(psi - 1.0) < 0.01

    def test_kw_full_analysis_three_regimes(self):
        """Full KW analysis identifies three distinguished regimes."""
        result = kapustin_witten_full_analysis('A', 1)
        assert result['kappa_A_model'] == Fraction(3, 2)
        assert result['kappa_critical'] == 0
        assert result['kappa_B_model_proxy'] > 0

    def test_kw_full_analysis_interpolation(self):
        """KW interpolation table has monotonically increasing kappa."""
        result = kapustin_witten_full_analysis('A', 1)
        kappas = [entry['kappa'] for entry in result['interpolation']]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1], \
                f"kappa not monotone at index {i}: {kappas[i]} >= {kappas[i+1]}"

    def test_kw_A_B_duality(self):
        """A-model at k=0 and B-model at k=infty are Langlands dual.
        For self-dual sl_2: k=0 maps to k^v = -0-2 = -2 (critical).
        The duality is NOT k=0 <-> k=infty directly, but via
        Psi -> 1/Psi, which maps Psi=0 to Psi=infty."""
        psi_0 = kapustin_witten_psi_exact('A', 1, Fraction(0))
        assert psi_0 == 0  # A-model: Psi = 0
        # Dual: Psi = infinity = B-model
        # In terms of levels: quantum GL maps k=0 to k^v = -h^v (critical)
        qgl = quantum_langlands_levels('A', 1, Fraction(0))
        assert qgl['k_dual'] == Fraction(-2)  # critical level


# =====================================================================
# 24. CROSS-CONSISTENCY TESTS (EXTENDED)
# =====================================================================

class TestCrossConsistencyExtended:
    """Extended cross-checks between old and new computations."""

    def test_kappa_slope_times_epsilon_equals_kappa(self):
        """slope * epsilon = kappa at k = -h^v + epsilon for all types."""
        for t, r in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2),
                     ('G', 2), ('F', 4), ('E', 6)]:
            slope = kappa_slope_at_critical(t, r)
            for eps_num in [1, 5, 10]:
                eps = Fraction(eps_num, 100)
                kap_from_slope = slope * eps
                kap_direct = kappa_near_critical(t, r, eps)
                assert kap_from_slope == kap_direct, \
                    f"{t}{r}, eps={eps}: {kap_from_slope} != {kap_direct}"

    def test_sugawara_residue_formula_consistency(self):
        """Residue computed two ways: -dim*h^v vs function."""
        for t, r in [('A', 1), ('A', 2), ('B', 2), ('C', 2), ('G', 2), ('E', 8)]:
            d = lie_data(t, r)
            res_formula = Fraction(-d.dim * d.h_dual)
            res_function = sugawara_residue_and_pole(t, r)['residue']
            assert res_formula == res_function

    def test_oper_degeneration_matches_shadow_metric(self):
        """Shadow metric at degeneration epsilon matches Q0 = 4*kappa^2."""
        for eps in [1.0, 0.5, 0.1]:
            result = oper_from_shadow_degeneration('A', 1, eps)
            kap = result['kappa']
            Q0 = result['shadow_metric_Q0']
            assert abs(Q0 - 4 * kap**2) < 1e-12

    def test_hitchin_oper_consistency(self):
        """Hitchin Hamiltonians data is consistent with oper structure."""
        h = hitchin_hamiltonians_sl2_genus2()
        op = h['oper_data']
        assert op.num_oper_parameters == h['dim_hitchin_base']
        assert 2 in op.casimir_degrees

    def test_full_computation_extended_keys(self):
        """Extended full_computation has all new keys."""
        result = full_computation()
        assert 'so5_sp4' in result
        assert result['so5_sp4']['all_equal_at_rank2'] is True
        assert 'kw_sl2' in result
        assert result['kw_sl2']['kappa_critical'] == 0
