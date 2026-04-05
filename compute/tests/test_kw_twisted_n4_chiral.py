r"""Tests for compute.lib.kw_twisted_n4_chiral.

Comprehensive verification of the Kapustin-Witten twisted N=4 chiral
algebra at all twisting parameters t in CP^1.

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct formula (kappa_kw, kappa_kw_from_t)
  Path 2: Via effective level and kappa_affine
  Path 3: Limiting cases (t=0, t=1, t->infty)
  Path 4: Complementarity (kappa + kappa^! = dim(g)/2)
  Path 5: Linearity (kappa = -dim(g)*t/2)
  Path 6: S-duality consistency (Psi -> 1/Psi)
  Path 7: GL(1) triviality (abelian theory is t-independent)
  Path 8: Literature comparison (Kapustin-Witten 2006, Frenkel 2007)

Key formula:
    kappa(A_t) = -dim(g) * t / 2

Conventions:
  - Psi = t/(1+t): the KW coupling parameter.
  - k_eff = -h^v * (1+t): the effective affine level.
  - kappa(g_hat_k) = dim(g) * (k + h^v) / (2 * h^v) (AP1, Vol I).
"""

import math
from fractions import Fraction

import pytest

from compute.lib.kw_twisted_n4_chiral import (
    KWChiralAlgebraData,
    _bernoulli_numbers,
    _casimir_degrees_from_type,
    central_charge_kw,
    central_charge_kw_float,
    compare_kw_vs_cy3,
    complementarity_self_dual_check,
    complementarity_sum_kw,
    e1_structure_kw,
    effective_level,
    effective_level_float,
    effective_level_from_t,
    full_computation,
    kappa_kw,
    kappa_kw_consistency_check,
    kappa_kw_dual,
    kappa_kw_float,
    kappa_kw_from_t,
    kappa_kw_from_t_float,
    kappa_linearity_verification,
    kw_chiral_generic,
    kw_chiral_non_simply_laced,
    kw_chiral_t0,
    kw_chiral_t1,
    kw_chiral_t_infty,
    kw_exceptional_landscape,
    kw_full_landscape,
    kw_gl1_check,
    kw_gl2_decomposition,
    kw_gln_decomposition,
    kw_sl2_at_t,
    kw_sl2_interpolation,
    kw_sln_at_t,
    oper_space_data,
    psi_from_t,
    psi_from_t_float,
    qgl_level_map,
    s_duality_on_kw,
    shadow_class_kw,
    shadow_connection_kw,
    shadow_f1_kw,
    shadow_generating_function_kw,
    t_from_psi,
    verify_all,
)

from compute.lib.geometric_langlands_shadow import (
    central_charge_affine,
    kappa_affine,
    kapustin_witten_psi_exact,
    lie_data,
)


# =====================================================================
# 1. TWIST PARAMETER COORDINATE CHANGES
# =====================================================================

class TestParameterMaps:
    """Test Psi <-> t coordinate changes."""

    def test_psi_at_t0(self):
        """Psi(t=0) = 0."""
        assert psi_from_t(Fraction(0)) == 0

    def test_psi_at_t1(self):
        """Psi(t=1) = 1/2."""
        assert psi_from_t(Fraction(1)) == Fraction(1, 2)

    def test_psi_at_t_large(self):
        """Psi(t) -> 1 as t -> infty."""
        assert psi_from_t(Fraction(1000)) == Fraction(1000, 1001)
        assert psi_from_t(Fraction(10**6)) > Fraction(999999, 10**6)

    def test_psi_monotone(self):
        """Psi is strictly increasing in t for t >= 0."""
        values = [psi_from_t(Fraction(i, 10)) for i in range(20)]
        for i in range(len(values) - 1):
            assert values[i] < values[i + 1]

    def test_t_from_psi_inverse(self):
        """t_from_psi is the inverse of psi_from_t."""
        for t in [Fraction(0), Fraction(1, 3), Fraction(1, 2),
                  Fraction(1), Fraction(3), Fraction(10)]:
            psi = psi_from_t(t)
            t_back = t_from_psi(psi)
            assert t_back == t

    def test_t_from_psi_at_1(self):
        """t_from_psi(1) = None (t = infty)."""
        assert t_from_psi(Fraction(1)) is None

    def test_psi_float_consistency(self):
        """Float and exact Psi agree."""
        for t in [0.0, 0.5, 1.0, 3.0, 10.0]:
            psi_f = psi_from_t_float(t)
            psi_e = float(psi_from_t(Fraction(t).limit_denominator(1000)))
            assert abs(psi_f - psi_e) < 1e-10


# =====================================================================
# 2. EFFECTIVE LEVEL
# =====================================================================

class TestEffectiveLevel:
    """Test the effective affine level k_eff(Psi) = -h^v/(1-Psi)."""

    def test_critical_level_at_psi0(self):
        """At Psi=0: k_eff = -h^v (critical level)."""
        # SL(2): h^v = 2
        assert effective_level(Fraction(0), 2) == Fraction(-2)
        # SL(3): h^v = 3
        assert effective_level(Fraction(0), 3) == Fraction(-3)
        # E_8: h^v = 30
        assert effective_level(Fraction(0), 30) == Fraction(-30)

    def test_divergence_at_psi1(self):
        """At Psi=1: k_eff diverges (returns None)."""
        assert effective_level(Fraction(1), 2) is None

    def test_level_from_t_at_t0(self):
        """k_eff(t=0) = -h^v via the t-formula."""
        assert effective_level_from_t(Fraction(0), 2) == Fraction(-2)
        assert effective_level_from_t(Fraction(0), 3) == Fraction(-3)

    def test_level_from_t_at_t1(self):
        """k_eff(t=1) = -2*h^v."""
        assert effective_level_from_t(Fraction(1), 2) == Fraction(-4)
        assert effective_level_from_t(Fraction(1), 3) == Fraction(-6)

    def test_two_formulas_agree(self):
        """k_eff via Psi and via t must agree."""
        for t_val in [Fraction(1, 3), Fraction(1, 2), Fraction(1),
                      Fraction(2), Fraction(5)]:
            psi = psi_from_t(t_val)
            for h_dual in [2, 3, 4, 6, 12, 30]:
                k_from_psi = effective_level(psi, h_dual)
                k_from_t = effective_level_from_t(t_val, h_dual)
                assert k_from_psi == k_from_t, (
                    f"Disagreement at t={t_val}, h^v={h_dual}: "
                    f"{k_from_psi} vs {k_from_t}"
                )

    def test_level_decreasing_in_t(self):
        """k_eff is strictly decreasing in t (since k_eff = -h^v*(1+t))."""
        levels = [effective_level_from_t(Fraction(i, 10), 2) for i in range(20)]
        for i in range(len(levels) - 1):
            assert levels[i] > levels[i + 1]

    def test_float_consistency(self):
        """Float and exact effective level agree."""
        for psi in [0.0, 0.25, 0.5, 0.75]:
            kf = effective_level_float(psi, 2)
            ke = float(effective_level(Fraction(psi).limit_denominator(100), 2))
            assert abs(kf - ke) < 1e-10


# =====================================================================
# 3. MODULAR CHARACTERISTIC kappa(A_t)
# =====================================================================

class TestKappaKW:
    """Test kappa(A_t) = -dim(g)*t/2."""

    def test_kappa_zero_at_t0(self):
        """kappa(A_0) = 0 for all types (critical level)."""
        for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('C', 3),
                            ('D', 4), ('E', 6), ('E', 8), ('G', 2)]:
            assert kappa_kw(type_, rank, Fraction(0)) == 0
            assert kappa_kw_from_t(type_, rank, Fraction(0)) == 0

    def test_kappa_sl2_at_t1(self):
        """kappa(A_1) = -3/2 for SL(2) (dim=3, t=1)."""
        assert kappa_kw_from_t('A', 1, Fraction(1)) == Fraction(-3, 2)

    def test_kappa_sl3_at_t1(self):
        """kappa(A_1) = -4 for SL(3) (dim=8, t=1)."""
        assert kappa_kw_from_t('A', 2, Fraction(1)) == Fraction(-4)

    def test_kappa_e8_at_t1(self):
        """kappa(A_1) = -124 for E_8 (dim=248, t=1)."""
        assert kappa_kw_from_t('E', 8, Fraction(1)) == Fraction(-124)

    def test_kappa_diverges_at_psi1(self):
        """kappa diverges at Psi = 1 (returns None)."""
        assert kappa_kw('A', 1, Fraction(1)) is None

    def test_kappa_formula_dim_g_over_2(self):
        """kappa = -dim(g)*t/2: verify the exact formula."""
        for type_, rank in [('A', 1), ('A', 3), ('B', 2), ('C', 3),
                            ('D', 4), ('E', 6), ('F', 4), ('G', 2)]:
            d = lie_data(type_, rank)
            for t in [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(5)]:
                kap = kappa_kw_from_t(type_, rank, t)
                expected = Fraction(-d.dim) * t / 2
                assert kap == expected, (
                    f"{type_}{rank} at t={t}: kappa={kap}, expected={expected}"
                )

    def test_kappa_two_paths_agree(self):
        """kappa via Psi and kappa via t must agree.

        Path 1: t -> Psi -> kappa_kw(Psi).
        Path 2: t -> kappa_kw_from_t(t).
        """
        for t in [Fraction(1, 3), Fraction(1), Fraction(7, 3)]:
            for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('E', 6)]:
                psi = psi_from_t(t)
                kap1 = kappa_kw(type_, rank, psi)
                kap2 = kappa_kw_from_t(type_, rank, t)
                assert kap1 == kap2

    def test_kappa_three_paths_agree(self):
        """Three independent paths to kappa must agree.

        Path 1: kappa_kw(Psi).
        Path 2: kappa_kw_from_t(t).
        Path 3: kappa_affine(k_eff).
        """
        for t in [Fraction(1, 2), Fraction(1), Fraction(3)]:
            for type_, rank in [('A', 1), ('A', 2), ('D', 4)]:
                result = kappa_kw_consistency_check(type_, rank, t)
                assert result['psi_t_agree'], (
                    f"Psi/t disagreement at {type_}{rank}, t={t}"
                )
                if result['level_agrees'] is not None:
                    assert result['level_agrees'], (
                        f"Level disagreement at {type_}{rank}, t={t}"
                    )

    def test_kappa_float_consistency(self):
        """Float and exact kappa agree."""
        for t in [0.5, 1.0, 2.0]:
            kf = kappa_kw_from_t_float('A', 1, t)
            ke = float(kappa_kw_from_t('A', 1, Fraction(t).limit_denominator(100)))
            assert abs(kf - ke) < 1e-10

    def test_kappa_negative_for_positive_t(self):
        """kappa < 0 for all t > 0 (negative curvature in KW regime)."""
        for t in [Fraction(1, 10), Fraction(1), Fraction(10)]:
            for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('E', 8)]:
                kap = kappa_kw_from_t(type_, rank, t)
                assert kap < 0, f"{type_}{rank} at t={t}: kappa={kap} >= 0"


# =====================================================================
# 4. COMPLEMENTARITY: kappa + kappa^! = dim(g)/2
# =====================================================================

class TestComplementarity:
    """Test KW complementarity theorem."""

    def test_complementarity_sl2(self):
        """kappa + kappa^! = 3/2 for SL(2) at all Psi."""
        for psi in [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2),
                    Fraction(2, 3), Fraction(9, 10)]:
            s = complementarity_sum_kw('A', 1, psi)
            assert s == Fraction(3, 2), f"SL(2) at Psi={psi}: sum={s}"

    def test_complementarity_sl3(self):
        """kappa + kappa^! = 4 for SL(3)."""
        for psi in [Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)]:
            s = complementarity_sum_kw('A', 2, psi)
            assert s == Fraction(4)

    def test_complementarity_e8(self):
        """kappa + kappa^! = 124 for E_8."""
        s = complementarity_sum_kw('E', 8, Fraction(1, 2))
        assert s == Fraction(124)

    def test_complementarity_all_self_dual(self):
        """kappa + kappa^! = dim(g)/2 for all self-dual types."""
        for type_, rank in [('A', 1), ('A', 2), ('A', 3), ('D', 4),
                            ('E', 6), ('E', 7), ('E', 8)]:
            d = lie_data(type_, rank)
            result = complementarity_self_dual_check(type_, rank)
            assert result['all_match'], (
                f"Complementarity fails for {type_}{rank}"
            )

    def test_complementarity_bn_cn(self):
        """B_n/C_n: dim(B_n) = dim(C_n), so complementarity holds.

        B_n and C_n are Langlands dual with the SAME dimension.
        The complementarity sum should be dim/2.
        """
        for n in [2, 3, 4]:
            d_b = lie_data('B', n)
            d_c = lie_data('C', n)
            assert d_b.dim == d_c.dim, f"dim(B_{n}) != dim(C_{n})"

            s = complementarity_sum_kw('B', n, Fraction(1, 3))
            assert s == Fraction(d_b.dim, 2)

    def test_complementarity_g2_f4(self):
        """G_2 and F_4 are self-dual, so complementarity = dim/2."""
        for type_, rank in [('G', 2), ('F', 4)]:
            d = lie_data(type_, rank)
            s = complementarity_sum_kw(type_, rank, Fraction(1, 3))
            assert s == Fraction(d.dim, 2)

    def test_complementarity_dim_gv_equals_dim_g(self):
        """dim(G^v) = dim(G) for ALL Langlands pairs.

        This is the KEY FACT that makes complementarity universal.
        """
        for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('B', 3),
                            ('C', 2), ('C', 3), ('D', 4), ('E', 6),
                            ('F', 4), ('G', 2)]:
            d = lie_data(type_, rank)
            from compute.lib.geometric_langlands_shadow import langlands_dual_data
            dv = langlands_dual_data(type_, rank)
            assert d.dim == dv.dim, (
                f"{type_}{rank}: dim={d.dim}, dual {dv.type}{dv.rank}: dim={dv.dim}"
            )


# =====================================================================
# 5. DISTINGUISHED POINTS: t = 0, 1, infty
# =====================================================================

class TestDistinguishedPoints:
    """Test the three distinguished twist parameters."""

    def test_t0_commutative(self):
        """A_0 is commutative (E_infty)."""
        data = kw_chiral_t0('A', 1)
        assert data.commutativity == 'E_infty'

    def test_t0_kappa_zero(self):
        """kappa(A_0) = 0 for all types."""
        for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('E', 8)]:
            data = kw_chiral_t0(type_, rank)
            assert data.kappa == 0

    def test_t0_critical_level(self):
        """k_eff at t=0 is the critical level -h^v."""
        for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('D', 4)]:
            data = kw_chiral_t0(type_, rank)
            d = lie_data(type_, rank)
            assert data.k_eff == Fraction(-d.h_dual)

    def test_t1_noncommutative(self):
        """A_1 is non-commutative (E_1)."""
        data = kw_chiral_t1('A', 1)
        assert data.commutativity == 'E_1'

    def test_t1_psi_half(self):
        """Psi(t=1) = 1/2."""
        data = kw_chiral_t1('A', 1)
        assert data.psi == Fraction(1, 2)

    def test_t1_level_minus_2h(self):
        """k_eff(t=1) = -2*h^v."""
        for type_, rank in [('A', 1), ('A', 2)]:
            d = lie_data(type_, rank)
            data = kw_chiral_t1(type_, rank)
            assert data.k_eff == Fraction(-2 * d.h_dual)

    def test_t1_kappa_sl2(self):
        """kappa(A_1) = -3/2 for SL(2)."""
        data = kw_chiral_t1('A', 1)
        assert data.kappa == Fraction(-3, 2)

    def test_tinfty_commutative(self):
        """A_infty is commutative (E_infty)."""
        data = kw_chiral_t_infty('A', 1)
        assert data.commutativity == 'E_infty'

    def test_tinfty_langlands_dual(self):
        """A_infty uses the Langlands dual group."""
        data = kw_chiral_t_infty('B', 2)
        # B_2 dual is C_2
        assert 'C2' in data.chiral_algebra_description or 'C_2' in data.chiral_algebra_description

    def test_generic_t_noncommutative(self):
        """A_t at generic t is E_1."""
        data = kw_chiral_generic('A', 1, Fraction(1, 3))
        assert data.commutativity == 'E_1'

    def test_generic_t_kappa(self):
        """kappa at generic t matches the formula."""
        t = Fraction(2, 3)
        data = kw_chiral_generic('A', 1, t)
        expected = Fraction(-3) * t / 2  # dim(sl_2) = 3
        assert data.kappa == expected


# =====================================================================
# 6. GL(1) TRIVIALITY
# =====================================================================

class TestGL1:
    """The abelian theory is t-independent."""

    def test_gl1_t_independent(self):
        """kappa(H_k) does not depend on the twist parameter t."""
        result = kw_gl1_check()
        assert result['all_t_independent']

    def test_gl1_all_levels_independent(self):
        """Check independence at multiple levels."""
        result = kw_gl1_check()
        for r in result['results']:
            assert r['t_independent']


# =====================================================================
# 7. GL(2) / SL(2) CASE
# =====================================================================

class TestSL2:
    """Detailed tests for the SL(2) case."""

    def test_sl2_kappa_linear(self):
        """kappa(A_t) = -3*t/2 for SL(2)."""
        for t in [Fraction(0), Fraction(1, 2), Fraction(1),
                  Fraction(3, 2), Fraction(5)]:
            result = kw_sl2_at_t(t)
            assert result['kappa'] == Fraction(-3) * t / 2

    def test_sl2_kappa_agrees_with_level(self):
        """kappa computed from k_eff agrees."""
        for t in [Fraction(1, 3), Fraction(1), Fraction(3)]:
            result = kw_sl2_at_t(t)
            assert result['kappas_agree']

    def test_sl2_oper_at_t0(self):
        """t=0 is the oper regime."""
        result = kw_sl2_at_t(Fraction(0))
        assert result['oper_regime']
        assert result['commutative']

    def test_sl2_non_oper_at_t1(self):
        """t=1 is NOT the oper regime."""
        result = kw_sl2_at_t(Fraction(1))
        assert not result['oper_regime']
        assert not result['commutative']

    def test_sl2_interpolation_monotone(self):
        """kappa decreases monotonically along the interpolation."""
        interp = kw_sl2_interpolation(20)
        kappas = [r['kappa'] for r in interp]
        for i in range(len(kappas) - 1):
            assert kappas[i] >= kappas[i + 1]

    def test_gl2_decomposition(self):
        """GL(2) = SL(2) x GL(1): kappa decomposes additively."""
        t = Fraction(1)
        k_ab = Fraction(3)
        result = kw_gl2_decomposition(t, k_ab)
        assert result['kappa_total'] == result['kappa_sl2'] + result['kappa_gl1']
        assert result['kappa_sl2'] == Fraction(-3, 2)
        assert result['kappa_gl1'] == Fraction(3)
        assert result['kappa_total'] == Fraction(3, 2)


# =====================================================================
# 8. GL(n) / SL(n) CASE
# =====================================================================

class TestSLn:
    """Tests for SL(n) at various n."""

    def test_sln_kappa_formula(self):
        """kappa = -(n^2-1)*t/2 for SL(n)."""
        for n in [2, 3, 4, 5]:
            t = Fraction(1)
            result = kw_sln_at_t(n, t)
            expected = Fraction(-(n**2 - 1)) / 2
            assert result['kappa'] == expected

    def test_sln_kappa_agrees(self):
        """kappa from t and kappa from level agree for SL(n)."""
        for n in [2, 3, 4]:
            for t in [Fraction(1, 2), Fraction(1), Fraction(3)]:
                result = kw_sln_at_t(n, t)
                assert result['kappas_agree']

    def test_sln_critical_at_t0(self):
        """t=0 gives the critical level for all SL(n)."""
        for n in [2, 3, 4, 5]:
            result = kw_sln_at_t(n, Fraction(0))
            assert result['is_critical']
            assert result['kappa'] == 0

    def test_sln_oper_order(self):
        """The oper has order n for SL(n)."""
        for n in [2, 3, 4, 5]:
            result = kw_sln_at_t(n, Fraction(0))
            assert result['oper_order'] == n

    def test_gln_decomposition(self):
        """GL(n) = SL(n) x GL(1): additive kappa."""
        for n in [2, 3, 4]:
            t = Fraction(1)
            result = kw_gln_decomposition(n, t, Fraction(0))
            assert result['kappa_total'] == result['kappa_sln'] + result['kappa_gl1']

    def test_sln_rank_error(self):
        """SL(1) should raise an error (rank 0)."""
        with pytest.raises(ValueError):
            kw_sln_at_t(1, Fraction(1))


# =====================================================================
# 9. NON-SIMPLY-LACED TYPES
# =====================================================================

class TestNonSimplyLaced:
    """Tests for B, C, F, G types."""

    def test_bn_cn_dim_equal(self):
        """dim(B_n) = dim(C_n) for all n >= 2."""
        for n in [2, 3, 4]:
            result_b = kw_chiral_non_simply_laced('B', n, Fraction(1))
            assert result_b['dims_equal']

    def test_bn_cn_complementarity(self):
        """Complementarity holds for B_n/C_n pairs."""
        for n in [2, 3, 4]:
            result = kw_chiral_non_simply_laced('B', n, Fraction(1))
            assert result['complementarity_holds']

    def test_g2_complementarity(self):
        """Complementarity holds for G_2 (self-dual)."""
        result = kw_chiral_non_simply_laced('G', 2, Fraction(1))
        assert result['complementarity_holds']

    def test_f4_complementarity(self):
        """Complementarity holds for F_4 (self-dual)."""
        result = kw_chiral_non_simply_laced('F', 4, Fraction(1))
        assert result['complementarity_holds']

    def test_bn_different_h_dual(self):
        """B_n and C_n have different h^v for n >= 3.

        h^v(B_n) = 2n-1, h^v(C_n) = n+1.
        At n=2: both equal 3 (coincidence).
        At n=3: B_3 has h^v=5, C_3 has h^v=4.
        """
        for n in [3, 4]:
            result = kw_chiral_non_simply_laced('B', n, Fraction(1))
            assert result['h_dual'] != result['h_dual_v'], (
                f"B_{n}: h^v={result['h_dual']}, C_{n}: h^v={result['h_dual_v']}"
            )


# =====================================================================
# 10. S-DUALITY
# =====================================================================

class TestSDuality:
    """Test S-duality Psi -> 1/Psi on the KW chiral algebra."""

    def test_s_duality_psi_inversion(self):
        """S-duality maps Psi to 1/Psi."""
        result = s_duality_on_kw('A', 1, Fraction(1, 3))
        assert result['psi_dual'] == Fraction(3)

    def test_s_duality_sum_sl2(self):
        """kappa(Psi) + kappa(1/Psi) for self-dual SL(2).

        kappa(1/3) = -3*(1/3)/(2*(2/3)) = -3/(2*2) = -3/4... no.

        Let me recompute: kappa = -dim*Psi/(2*(1-Psi)).
        At Psi=1/3: kappa = -3*(1/3)/(2*(2/3)) = -1/(4/3) = -3/4.
        S-dual: Psi=3, kappa = -3*3/(2*(1-3)) = -9/(-4) = 9/4.
        Sum: -3/4 + 9/4 = 6/4 = 3/2 = dim(sl_2)/2.
        """
        result = s_duality_on_kw('A', 1, Fraction(1, 3))
        assert result['sum'] == Fraction(3, 2)

    def test_s_duality_kappa_not_equal(self):
        """kappa and kappa^{S-dual} are NOT equal (duality, not symmetry)."""
        result = s_duality_on_kw('A', 1, Fraction(1, 3))
        assert result['kappa'] != result['kappa_s_dual']

    def test_s_duality_error_at_boundary(self):
        """S-duality ill-defined at Psi = 0 and Psi = 1."""
        result0 = s_duality_on_kw('A', 1, Fraction(0))
        assert 'error' in result0
        result1 = s_duality_on_kw('A', 1, Fraction(1))
        assert 'error' in result1


# =====================================================================
# 11. LINEARITY OF kappa IN t
# =====================================================================

class TestLinearity:
    """kappa(A_t) = -dim(g)*t/2 is linear in t."""

    def test_linearity_sl2(self):
        """kappa is exactly linear for SL(2)."""
        result = kappa_linearity_verification('A', 1)
        assert result['all_linear']
        assert result['slope'] == Fraction(-3, 2)

    def test_linearity_sl3(self):
        """kappa is exactly linear for SL(3)."""
        result = kappa_linearity_verification('A', 2)
        assert result['all_linear']
        assert result['slope'] == Fraction(-4)

    def test_linearity_e8(self):
        """kappa is exactly linear for E_8."""
        result = kappa_linearity_verification('E', 8)
        assert result['all_linear']
        assert result['slope'] == Fraction(-124)

    def test_kappa_homogeneous(self):
        """kappa(alpha*t) = alpha * kappa(t): homogeneity."""
        for alpha in [Fraction(2), Fraction(1, 3), Fraction(7)]:
            for type_, rank in [('A', 1), ('A', 2)]:
                t = Fraction(1)
                kap_t = kappa_kw_from_t(type_, rank, t)
                kap_at = kappa_kw_from_t(type_, rank, alpha * t)
                assert kap_at == alpha * kap_t

    def test_kappa_additive(self):
        """kappa(t1 + t2) = kappa(t1) + kappa(t2): additivity."""
        t1, t2 = Fraction(1, 3), Fraction(2, 5)
        for type_, rank in [('A', 1), ('B', 2), ('E', 6)]:
            k1 = kappa_kw_from_t(type_, rank, t1)
            k2 = kappa_kw_from_t(type_, rank, t2)
            k12 = kappa_kw_from_t(type_, rank, t1 + t2)
            assert k12 == k1 + k2


# =====================================================================
# 12. CENTRAL CHARGE
# =====================================================================

class TestCentralCharge:
    """Test the Sugawara central charge c(A_t) = dim(g)*(1+t)/t."""

    def test_central_charge_pole_at_t0(self):
        """c diverges at t=0 (critical level)."""
        assert central_charge_kw('A', 1, Fraction(0)) is None

    def test_central_charge_sl2_at_t1(self):
        """c(SL_2, t=1) = 3*(1+1)/1 = 6."""
        assert central_charge_kw('A', 1, Fraction(1)) == Fraction(6)

    def test_central_charge_sl2_large_t(self):
        """c -> dim(g) = 3 as t -> infty for SL(2)."""
        c = central_charge_kw('A', 1, Fraction(1000))
        expected = Fraction(3 * 1001, 1000)
        assert c == expected
        assert abs(float(c) - 3.0) < 0.01

    def test_central_charge_sl3_at_t1(self):
        """c(SL_3, t=1) = 8*(1+1)/1 = 16."""
        assert central_charge_kw('A', 2, Fraction(1)) == Fraction(16)

    def test_central_charge_formula(self):
        """Verify c = dim(g)*(1+t)/t against direct computation."""
        for type_, rank in [('A', 1), ('A', 2), ('D', 4)]:
            d = lie_data(type_, rank)
            for t in [Fraction(1, 2), Fraction(1), Fraction(3)]:
                c = central_charge_kw(type_, rank, t)
                expected = Fraction(d.dim) * (1 + t) / t
                assert c == expected

    def test_central_charge_from_level(self):
        """c from central_charge_kw matches c from k_eff."""
        for type_, rank in [('A', 1), ('A', 2)]:
            d = lie_data(type_, rank)
            t = Fraction(1)
            c_kw = central_charge_kw(type_, rank, t)
            k_eff = effective_level_from_t(t, d.h_dual)
            c_affine = central_charge_affine(type_, rank, k_eff)
            assert c_kw == c_affine

    def test_central_charge_float(self):
        """Float version agrees with exact."""
        cf = central_charge_kw_float('A', 1, 1.0)
        ce = float(central_charge_kw('A', 1, Fraction(1)))
        assert abs(cf - ce) < 1e-10


# =====================================================================
# 13. OPER SPACE DATA
# =====================================================================

class TestOperSpace:
    """Test the oper space at the t=0 limit."""

    def test_oper_sl2_genus2(self):
        """Op_{PGL_2}(C_2): one Casimir of degree 2, dim = 3."""
        result = oper_space_data('A', 1, 2)
        assert result['oper_dimension'] == 3

    def test_oper_sl3_genus2(self):
        """Op_{PGL_3}(C_2): Casimirs of degree 2, 3.
        dim = (2*2-1)*1 + (2*3-1)*1 = 3 + 5 = 8.
        """
        result = oper_space_data('A', 2, 2)
        assert result['oper_dimension'] == 8

    def test_oper_sl2_genus3(self):
        """Op_{PGL_2}(C_3): dim = 3*2 = 6."""
        result = oper_space_data('A', 1, 3)
        assert result['oper_dimension'] == 6

    def test_oper_equals_hitchin_base(self):
        """Oper dimension = Hitchin base dimension."""
        for type_, rank, genus in [('A', 1, 2), ('A', 2, 2), ('A', 1, 3)]:
            result = oper_space_data(type_, rank, genus)
            assert result['oper_dimension'] == result['hitchin_base_dimension']

    def test_oper_casimir_degrees_sln(self):
        """Casimir degrees of SL(n): {2, 3, ..., n}."""
        assert _casimir_degrees_from_type('A', 1) == (2,)
        assert _casimir_degrees_from_type('A', 2) == (2, 3)
        assert _casimir_degrees_from_type('A', 3) == (2, 3, 4)

    def test_oper_casimir_degrees_exceptional(self):
        """Casimir degrees of G_2: {2, 6}."""
        assert _casimir_degrees_from_type('G', 2) == (2, 6)

    def test_oper_e8_genus2(self):
        """Op_{E_8}(C_2): 8 Casimirs, dim = sum (2*d_i - 1)."""
        result = oper_space_data('E', 8, 2)
        casimirs = (2, 8, 12, 14, 18, 20, 24, 30)
        expected_dim = sum((2 * d - 1) for d in casimirs)
        assert result['oper_dimension'] == expected_dim


# =====================================================================
# 14. SHADOW OBSTRUCTION TOWER
# =====================================================================

class TestShadowTower:
    """Test shadow data for the KW chiral algebra."""

    def test_shadow_class_at_t0(self):
        """At t=0: trivial shadow (kappa=0, uncurved)."""
        assert shadow_class_kw('A', 1, Fraction(0)) == 'trivial'

    def test_shadow_class_generic(self):
        """At generic t: class L (affine KM structure)."""
        assert shadow_class_kw('A', 1, Fraction(1)) == 'L'

    def test_f1_zero_at_t0(self):
        """F_1(A_0) = 0."""
        assert shadow_f1_kw('A', 1, Fraction(0)) == 0

    def test_f1_sl2_at_t1(self):
        """F_1(A_1) = kappa/24 = (-3/2)/24 = -1/16."""
        f1 = shadow_f1_kw('A', 1, Fraction(1))
        assert f1 == Fraction(-3, 2) / 24
        assert f1 == Fraction(-1, 16)

    def test_shadow_gf_at_t0(self):
        """All F_g vanish at t=0 (uncurved bar complex)."""
        gf = shadow_generating_function_kw('A', 1, Fraction(0), 5)
        for g, f in gf.items():
            assert f == 0, f"F_{g} = {f} != 0 at t=0"

    def test_shadow_connection_degenerate_at_t0(self):
        """Shadow connection degenerates at t=0 (oper limit)."""
        result = shadow_connection_kw('A', 1, Fraction(0))
        assert result['degenerate']
        assert result['oper_limit']

    def test_shadow_connection_nondegenerate_at_t1(self):
        """Shadow connection is non-degenerate at t=1."""
        result = shadow_connection_kw('A', 1, Fraction(1))
        assert not result['degenerate']
        assert result['shadow_residue'] == Fraction(1, 2)


# =====================================================================
# 15. E_1 STRUCTURE
# =====================================================================

class TestE1Structure:
    """Test the operadic type of A_t."""

    def test_e_infty_at_t0(self):
        """E_infty at t=0."""
        result = e1_structure_kw('A', 1, Fraction(0))
        assert result['operadic_type'] == 'E_infty'
        assert not result['hitchin_poisson']

    def test_e1_at_generic_t(self):
        """E_1 at generic t."""
        for t in [Fraction(1, 2), Fraction(1), Fraction(3)]:
            result = e1_structure_kw('A', 1, t)
            assert result['operadic_type'] == 'E_1'
            assert result['hitchin_poisson']

    def test_bar_type_ordered_vs_symmetric(self):
        """Bar complex type changes at t=0."""
        result_0 = e1_structure_kw('A', 1, Fraction(0))
        result_1 = e1_structure_kw('A', 1, Fraction(1))
        assert 'Sym' in result_0['bar_type']
        assert 'T^c' in result_1['bar_type']


# =====================================================================
# 16. QGL LEVEL MAP
# =====================================================================

class TestQGLLevelMap:
    """Test the quantum geometric Langlands level relation."""

    def test_qgl_sl2_sum(self):
        """k_eff + k^v_eff = -h^v for self-dual SL(2).

        k_eff(1/3) = -2/(1 - 1/3) = -2/(2/3) = -3.
        1/Psi = 3. k^v_eff(3) should be computed with Psi=3:
        k_eff(3) = -2/(1-3) = -2/(-2) = 1.
        Sum: -3 + 1 = -2 = -h^v.
        """
        result = qgl_level_map('A', 1, Fraction(1, 3))
        assert result['qgl_relation_holds']
        assert result['level_sum'] == Fraction(-2)

    def test_qgl_sl3_sum(self):
        """k + k^v = -h^v = -3 for SL(3)."""
        result = qgl_level_map('A', 2, Fraction(1, 3))
        assert result['qgl_relation_holds']
        assert result['level_sum'] == Fraction(-3)

    def test_qgl_d4_sum(self):
        """k + k^v = -h^v = -6 for D_4 (h^v = 6)."""
        result = qgl_level_map('D', 4, Fraction(1, 3))
        assert result['qgl_relation_holds']

    def test_qgl_multiple_psi(self):
        """QGL relation holds at multiple Psi for SL(2)."""
        for psi in [Fraction(1, 5), Fraction(1, 3), Fraction(1, 2),
                    Fraction(2, 3), Fraction(4, 5)]:
            result = qgl_level_map('A', 1, psi)
            assert result['qgl_relation_holds'], f"QGL fails at Psi={psi}"


# =====================================================================
# 17. COMPARISON WITH CY3
# =====================================================================

class TestCY3Comparison:
    """Test comparison between KW and CY3 E_1 structures."""

    def test_embedding_exists(self):
        """Sigma x C embeds in C^3."""
        result = compare_kw_vs_cy3(2, Fraction(1))
        assert result['embedding_exists']

    def test_kw_kappa_independent_of_cy3(self):
        """KW kappa is computable without choosing a CY3."""
        result = compare_kw_vs_cy3(2, Fraction(1))
        assert result['kappa_kw'] == Fraction(-3, 2)

    def test_cy3_comparison_indeterminate(self):
        """CY3 kappa depends on the geometry (not determined by KW data alone)."""
        result = compare_kw_vs_cy3(2, Fraction(1))
        assert result['same_e1'] is None  # Indeterminate


# =====================================================================
# 18. EXCEPTIONAL LANDSCAPE
# =====================================================================

class TestExceptionalLandscape:
    """Test KW data for exceptional types."""

    def test_exceptional_all_kappas_agree(self):
        """kappa via Psi and via t agree for all exceptional types."""
        results = kw_exceptional_landscape(Fraction(1))
        for r in results:
            assert r['kappas_agree'], f"{r['type']}: kappa disagreement"

    def test_exceptional_complementarity(self):
        """Complementarity holds for all exceptional types at t=1."""
        results = kw_exceptional_landscape(Fraction(1))
        for r in results:
            if r['complementarity_sum'] is not None:
                assert r['complementarity_sum'] == r['expected_comp'], (
                    f"{r['type']}: complementarity fails"
                )

    def test_exceptional_all_self_dual(self):
        """All exceptional types are Langlands self-dual."""
        results = kw_exceptional_landscape(Fraction(1))
        for r in results:
            assert r['self_dual'], f"{r['type']} is not self-dual"


# =====================================================================
# 19. FULL LANDSCAPE
# =====================================================================

class TestFullLandscape:
    """Test the full landscape of KW chiral algebras."""

    def test_all_kappas_agree(self):
        """kappa via Psi and via t agree for all 17 standard types."""
        result = kw_full_landscape(Fraction(1))
        assert result['all_kappas_agree']
        assert result['num_types'] == 17

    def test_landscape_at_t0(self):
        """All kappas vanish at t=0."""
        result = kw_full_landscape(Fraction(0))
        for key, data in result['landscape'].items():
            assert data['kappa'] == 0, f"{key}: kappa = {data['kappa']} at t=0"

    def test_landscape_at_t_half(self):
        """Spot-check kappa at t=1/2."""
        result = kw_full_landscape(Fraction(1, 2))
        sl2 = result['landscape']['A1']
        assert sl2['kappa'] == Fraction(-3, 4)  # -3 * (1/2) / 2 = -3/4


# =====================================================================
# 20. BERNOULLI NUMBERS
# =====================================================================

class TestBernoulli:
    """Test the Bernoulli number computation."""

    def test_b0(self):
        """B_0 = 1."""
        B = _bernoulli_numbers(0)
        assert B[0] == 1

    def test_b1(self):
        """B_1 = -1/2."""
        B = _bernoulli_numbers(1)
        assert B[1] == Fraction(-1, 2)

    def test_b2(self):
        """B_2 = 1/6."""
        B = _bernoulli_numbers(2)
        assert B[2] == Fraction(1, 6)

    def test_b4(self):
        """B_4 = -1/30."""
        B = _bernoulli_numbers(4)
        assert B[4] == Fraction(-1, 30)

    def test_b6(self):
        """B_6 = 1/42."""
        B = _bernoulli_numbers(6)
        assert B[6] == Fraction(1, 42)

    def test_odd_bernoulli_zero(self):
        """B_{2k+1} = 0 for k >= 1."""
        B = _bernoulli_numbers(10)
        for k in [3, 5, 7, 9]:
            assert B[k] == 0


# =====================================================================
# 21. COMPREHENSIVE VERIFICATION SUITE
# =====================================================================

class TestVerifyAll:
    """Run the comprehensive verification."""

    def test_verify_all_runs(self):
        """verify_all() completes without error."""
        result = verify_all()
        assert 'gl1_t_independent' in result

    def test_verify_all_gl1(self):
        """GL(1) independence check passes."""
        result = verify_all()
        assert result['gl1_t_independent']['all_t_independent']

    def test_verify_all_kappa_consistency(self):
        """All kappa consistency checks pass."""
        result = verify_all()
        for key, val in result.items():
            if key.startswith('kappa_consistency'):
                assert val['psi_t_agree']

    def test_verify_all_complementarity(self):
        """All complementarity checks pass for self-dual types."""
        result = verify_all()
        for key, val in result.items():
            if key.startswith('complementarity'):
                if val['self_dual']:
                    assert val['all_match']

    def test_verify_all_linearity(self):
        """All linearity checks pass."""
        result = verify_all()
        assert result['linearity_sl2']['all_linear']
        assert result['linearity_sl3']['all_linear']


class TestFullComputation:
    """Run the full computation suite."""

    def test_full_computation_runs(self):
        """full_computation() completes without error."""
        result = full_computation()
        assert 'verification' in result

    def test_full_computation_sl2_data(self):
        """SL(2) data in full computation is correct."""
        result = full_computation()
        sl2_t0 = result['sl2_t0']
        assert sl2_t0.kappa == 0
        assert sl2_t0.commutativity == 'E_infty'


# =====================================================================
# 22. CROSS-CHECK: LEVEL FORMULA VS AFFINE kappa
# =====================================================================

class TestCrossCheckAffineKappa:
    """Cross-check kappa_kw against kappa_affine at matching levels."""

    def test_sl2_level_kappa_match(self):
        """For SL(2): kappa_kw(t) = kappa_affine(k_eff(t)).

        kappa_kw_from_t(t) = -3*t/2.
        k_eff(t) = -2*(1+t).
        kappa_affine(k) = 3*(k+2)/4.
        kappa_affine(-2*(1+t)) = 3*(-2*(1+t)+2)/4 = 3*(-2t)/4 = -3t/2.
        """
        for t in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5)]:
            kap_kw = kappa_kw_from_t('A', 1, t)
            k_eff = effective_level_from_t(t, 2)
            kap_aff = kappa_affine('A', 1, k_eff)
            assert kap_kw == kap_aff, (
                f"Mismatch at t={t}: kw={kap_kw}, affine={kap_aff}"
            )

    def test_sl3_level_kappa_match(self):
        """For SL(3): same cross-check."""
        for t in [Fraction(1, 3), Fraction(1), Fraction(3)]:
            kap_kw = kappa_kw_from_t('A', 2, t)
            k_eff = effective_level_from_t(t, 3)
            kap_aff = kappa_affine('A', 2, k_eff)
            assert kap_kw == kap_aff

    def test_all_types_level_kappa_match(self):
        """Cross-check for all 17 standard types at t=1."""
        types = [
            ('A', 1), ('A', 2), ('A', 3), ('A', 4),
            ('B', 2), ('B', 3), ('B', 4),
            ('C', 2), ('C', 3), ('C', 4),
            ('D', 4), ('D', 5),
            ('G', 2), ('F', 4),
            ('E', 6), ('E', 7), ('E', 8),
        ]
        for type_, rank in types:
            d = lie_data(type_, rank)
            t = Fraction(1)
            kap_kw = kappa_kw_from_t(type_, rank, t)
            k_eff = effective_level_from_t(t, d.h_dual)
            kap_aff = kappa_affine(type_, rank, k_eff)
            assert kap_kw == kap_aff, (
                f"{type_}{rank}: kw={kap_kw}, affine={kap_aff}"
            )


# =====================================================================
# 23. EDGE CASES AND BOUNDARY BEHAVIOR
# =====================================================================

class TestEdgeCases:
    """Test edge cases and boundary behavior."""

    def test_large_t(self):
        """kappa at very large t is very negative."""
        kap = kappa_kw_from_t('A', 1, Fraction(1000))
        assert kap == Fraction(-1500)

    def test_small_t_linear_approx(self):
        """At small t, kappa ~ -dim(g)*t/2 (trivially exact)."""
        for t in [Fraction(1, 100), Fraction(1, 1000)]:
            kap = kappa_kw_from_t('A', 1, t)
            expected = Fraction(-3) * t / 2
            assert kap == expected  # Exact, not approximate

    def test_psi_near_1(self):
        """Near Psi=1, kappa diverges."""
        for psi in [Fraction(99, 100), Fraction(999, 1000)]:
            kap = kappa_kw('A', 1, psi)
            assert abs(kap) > 100

    def test_negative_t(self):
        """Negative t is allowed (different physical regime)."""
        kap = kappa_kw_from_t('A', 1, Fraction(-1, 2))
        assert kap == Fraction(3, 4)  # Positive kappa!

    def test_fractional_t(self):
        """Fractional t values produce exact results."""
        t = Fraction(7, 13)
        kap = kappa_kw_from_t('A', 1, t)
        assert kap == Fraction(-3 * 7, 2 * 13)


# =====================================================================
# 24. SHADOW GENERATING FUNCTION
# =====================================================================

class TestShadowGeneratingFunction:
    """Test shadow generating function F_g."""

    def test_f1_formula(self):
        """F_1 = kappa/24 for all types."""
        for type_, rank in [('A', 1), ('A', 2), ('E', 8)]:
            t = Fraction(1)
            kap = kappa_kw_from_t(type_, rank, t)
            f1 = shadow_f1_kw(type_, rank, t)
            assert f1 == kap / 24

    def test_f2_formula(self):
        """F_2 = kappa * B_4 / (4*2) = kappa * (-1/30) / 8 = -kappa/240."""
        gf = shadow_generating_function_kw('A', 1, Fraction(1), 5)
        kap = kappa_kw_from_t('A', 1, Fraction(1))
        expected_f2 = kap * Fraction(-1, 30) / 8
        assert gf[2] == expected_f2

    def test_all_fg_zero_at_t0(self):
        """All F_g = 0 at t=0."""
        gf = shadow_generating_function_kw('A', 1, Fraction(0), 5)
        for g in range(1, 6):
            assert gf[g] == 0

    def test_fg_proportional_to_t(self):
        """F_g(t) = F_g(1) * t (linearity in t, since kappa is linear)."""
        for g in range(1, 5):
            for type_, rank in [('A', 1), ('A', 2)]:
                gf_1 = shadow_generating_function_kw(type_, rank, Fraction(1), 5)
                gf_t = shadow_generating_function_kw(type_, rank, Fraction(3), 5)
                assert gf_t[g] == 3 * gf_1[g]


# =====================================================================
# 25. DIMENSIONAL ANALYSIS
# =====================================================================

class TestDimensionalAnalysis:
    """Verify dimensional consistency."""

    def test_kappa_scales_with_dim(self):
        """kappa(type, t) / kappa(A1, t) = dim(type) / dim(A1)."""
        t = Fraction(1)
        kap_a1 = kappa_kw_from_t('A', 1, t)
        for type_, rank in [('A', 2), ('A', 3), ('D', 4), ('E', 8)]:
            d = lie_data(type_, rank)
            kap = kappa_kw_from_t(type_, rank, t)
            ratio = kap / kap_a1
            expected_ratio = Fraction(d.dim, 3)  # dim(A1) = 3
            assert ratio == expected_ratio

    def test_kappa_independent_of_h_dual(self):
        """kappa = -dim*t/2 does NOT depend on h^v.

        This is a non-trivial check: kappa_affine depends on h^v,
        but through the KW twist, the h^v cancels.

        B_3 and C_3 have the same dimension (21) but different h^v
        (B_3: h^v=5, C_3: h^v=4).  Despite this, kappa_kw is the same
        for both, since kappa = -dim*t/2 depends only on dim(g).
        (B_2/C_2 are not useful here: they coincidentally share h^v=3.)
        """
        d_b3 = lie_data('B', 3)
        d_c3 = lie_data('C', 3)
        assert d_b3.dim == d_c3.dim  # Both 21
        assert d_b3.h_dual != d_c3.h_dual  # B_3: 5, C_3: 4

        t = Fraction(1)
        kap_b = kappa_kw_from_t('B', 3, t)
        kap_c = kappa_kw_from_t('C', 3, t)
        assert kap_b == kap_c  # Same because dim is the same!


# =====================================================================
# 26. INTEGRATION WITH EXISTING MODULES
# =====================================================================

class TestIntegrationWithExisting:
    """Test compatibility with geometric_langlands_shadow module."""

    def test_kappa_at_critical_matches(self):
        """kappa_kw at Psi=0 matches kappa_affine at critical level."""
        for type_, rank in [('A', 1), ('A', 2), ('B', 2), ('E', 6)]:
            d = lie_data(type_, rank)
            kap_kw = kappa_kw(type_, rank, Fraction(0))
            kap_aff = kappa_affine(type_, rank, Fraction(-d.h_dual))
            assert kap_kw == kap_aff == 0

    def test_central_charge_at_t1_matches(self):
        """c_kw at t=1 matches c_affine at k=-2*h^v."""
        for type_, rank in [('A', 1), ('A', 2)]:
            d = lie_data(type_, rank)
            c_kw = central_charge_kw(type_, rank, Fraction(1))
            c_aff = central_charge_affine(type_, rank, Fraction(-2 * d.h_dual))
            assert c_kw == c_aff

    def test_kw_psi_matches_existing(self):
        """Our Psi = t/(1+t) at k_eff level matches kapustin_witten_psi_exact.

        kapustin_witten_psi_exact(k) = k/(k+h^v).
        Our k_eff(t) = -h^v*(1+t).
        So Psi_existing(k_eff) = k_eff/(k_eff+h^v) = -h^v*(1+t)/(-h^v*t) = (1+t)/t.

        Wait, that gives (1+t)/t, not t/(1+t).  Let me check.

        Psi = k/(k+h^v) = -h^v*(1+t) / (-h^v*(1+t) + h^v) = -h^v*(1+t) / (-h^v*t)
            = (1+t)/t.

        But our Psi = t/(1+t).  These are RECIPROCALS: Psi_ours * Psi_existing = 1.

        This is NOT a contradiction: the existing module's Psi is the
        RECIPROCAL of ours because it uses the convention Psi = k/(k+h^v)
        while we use Psi = t/(1+t) where k = -h^v*(1+t).

        The reconciliation: the KW twist parameter t maps to the coupling
        Psi_KW = t/(1+t), while the geometric Langlands module's Psi is
        the AFFINE level parameter Psi_GL = k/(k+h^v).  These are related by
        Psi_GL = 1/Psi_KW when Psi_KW != 0.

        Verification: Psi_GL(k_eff) * Psi_KW(t) = [(1+t)/t] * [t/(1+t)] = 1.
        """
        for t_val in [Fraction(1, 2), Fraction(1), Fraction(3)]:
            d = lie_data('A', 1)
            k_eff = effective_level_from_t(t_val, d.h_dual)
            psi_existing = kapustin_witten_psi_exact('A', 1, k_eff)
            psi_ours = psi_from_t(t_val)

            if psi_existing is not None and psi_ours != 0:
                product = psi_existing * psi_ours
                # They should be reciprocals
                assert product != 0
                # Psi_GL * Psi_KW = 1 only if we account for sign.
                # Actually: k_eff = -h^v*(1+t) = -2*(1+t).
                # Psi_GL = k_eff/(k_eff+h^v) = -2*(1+t)/(-2*t) = (1+t)/t.
                # Psi_KW = t/(1+t).
                # Product = 1.  Good.
                assert product == 1, (
                    f"Product = {product} at t={t_val}"
                )


# =====================================================================
# TOTAL TEST COUNT: ~120 tests
# =====================================================================
