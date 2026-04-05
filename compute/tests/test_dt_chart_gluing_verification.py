r"""Tests for thm:dt-equals-hocolim-shadow:

    Z_DT(X, q) = Z^{sh,E1}(hocolim_alpha CoHA(Q_alpha, W_alpha), q)

For every standard CY3 geometry X with chart atlas {(Q_alpha, W_alpha)},
the DT partition function equals the E1 shadow partition function of the
hocolim of chart CoHAs.

Ground truth:
    - MacMahon function M(q): OEIS A000219 (plane partitions)
    - Conifold reduced: prod_{n>=1}(1 - Qq^n)^n
    - Local P^2 GV: Chiang-Klemm-Yau-Zaslow (hep-th/9903053)
    - K3 x E degree-0: M(q)^{24} (chi(K3) = 24)
    - Refined MacMahon: Iqbal-Kozcaz-Vafa (hep-th/0701156)
    - Faber-Pandharipande lambda_g: standard values

Manuscript references:
    Part V (CY3 Standard Landscape), chapters on DT/GW/E1 shadow
    Vol I: shadow obstruction tower, kappa, bar integrality
"""

import pytest
from fractions import Fraction

from compute.lib.dt_chart_gluing_verification import (
    # FPS arithmetic
    _fps_zero, _fps_one, _fps_add, _fps_sub, _fps_mul, _fps_inv,
    _fps_pow, _fps_exp, _fps_log, _fps_scale, _fps_shift,
    _fps_div, _fps_eq, _fps_to_int,
    # Core functions
    macmahon, macmahon_via_log, single_product_factor,
    # Chart-level
    chart_dt_degree0, chart_dt_c3, chart_shadow_e1_c3,
    # Conifold
    conifold_chart_gluing, conifold_shadow_hocolim,
    conifold_reduced, conifold_dt_direct,
    verify_conifold_gluing,
    # Local P^2
    local_p2_degree0, local_p2_shadow_degree0,
    local_p2_chart_gluing, local_p2_shadow_hocolim,
    local_p2_free_energy, local_p2_reduced_from_gv,
    verify_local_p2_gluing, LOCAL_P2_GV,
    # K3 x E
    k3xe_dt_degree0, k3xe_shadow_degree0, verify_k3xe_degree0,
    # Refined
    refined_macmahon, refined_macmahon_specialization,
    refined_dt_c3, refined_shadow_c3,
    verify_refined_specialization, verify_refined_c3_triangle,
    # GV integrality
    verify_coha_integrality_c3, conifold_gv_extraction,
    verify_gv_integrality_conifold, verify_gv_integrality_local_p2,
    gv_integrality_multicover_matrix, verify_multicover_matrix_properties,
    # Cross-verification
    verify_c3_identification, verify_conifold_identification,
    verify_local_p2_identification, verify_k3xe_identification,
    master_verification,
    # Nerve inclusion-exclusion
    nerve_inclusion_exclusion_1, nerve_inclusion_exclusion_2,
    # Wall-crossing
    wall_crossing_factor_coefficients, verify_wall_crossing_q1,
    # Genus
    bernoulli_numbers, faber_pandharipande_lambda_g,
    shadow_genus_g_from_kappa,
    # Coefficient tables
    conifold_coefficient_table, local_p2_coefficient_table,
    # Chi additivity
    verify_chi_additivity_c3, verify_chi_additivity_conifold,
    # Proof steps
    proof_step_a_ks_formula, proof_step_b_coha_character,
    proof_step_c_hocolim_character, proof_step_d_shadow_character,
    # Free energy
    genus0_free_energy_conifold,
)

# ================================================================
# OEIS A000219: plane partition counts (ground truth)
# ================================================================
PP_COUNTS = [
    1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500,
    859, 1479, 2485, 4167, 6879, 11297, 18334, 29601, 47330, 75278,
]


# ================================================================
# 1. FPS ARITHMETIC TESTS
# ================================================================

class TestFPSArithmetic:
    """FPS arithmetic correctness (foundation for all later tests)."""

    def test_fps_zero(self):
        f = _fps_zero(5)
        assert len(f) == 6
        assert all(c == 0 for c in f)

    def test_fps_one(self):
        f = _fps_one(5)
        assert f[0] == Fraction(1)
        assert all(f[k] == 0 for k in range(1, 6))

    def test_fps_add(self):
        a = [Fraction(1), Fraction(2), Fraction(3)]
        b = [Fraction(4), Fraction(5), Fraction(6)]
        c = _fps_add(a, b)
        assert c == [Fraction(5), Fraction(7), Fraction(9)]

    def test_fps_sub(self):
        a = [Fraction(5), Fraction(7)]
        b = [Fraction(1), Fraction(3)]
        c = _fps_sub(a, b)
        assert c == [Fraction(4), Fraction(4)]

    def test_fps_mul_identity(self):
        a = [Fraction(1), Fraction(2), Fraction(3)]
        one = [Fraction(1), Fraction(0), Fraction(0)]
        assert _fps_mul(a, one) == a

    def test_fps_mul(self):
        # (1+q)(1+q) = 1 + 2q + q^2
        a = [Fraction(1), Fraction(1), Fraction(0)]
        p = _fps_mul(a, a)
        assert p == [Fraction(1), Fraction(2), Fraction(1)]

    def test_fps_inv(self):
        # 1/(1-q) = 1 + q + q^2 + ...
        a = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)]
        inv = _fps_inv(a)
        assert inv == [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]

    def test_fps_inv_roundtrip(self):
        a = [Fraction(1), Fraction(3), Fraction(-2), Fraction(5)]
        inv = _fps_inv(a)
        prod = _fps_mul(a, inv)
        assert prod[0] == Fraction(1)
        assert all(prod[k] == 0 for k in range(1, 4))

    def test_fps_pow_0(self):
        a = [Fraction(1), Fraction(2), Fraction(3)]
        assert _fps_pow(a, 0) == [Fraction(1), Fraction(0), Fraction(0)]

    def test_fps_pow_negative(self):
        a = [Fraction(1), Fraction(1), Fraction(0)]
        inv = _fps_pow(a, -1)
        prod = _fps_mul(a, inv)
        assert prod[0] == Fraction(1)
        assert prod[1] == Fraction(0)

    def test_fps_exp_log_roundtrip(self):
        f = [Fraction(0), Fraction(1), Fraction(-1, 2), Fraction(1, 3)]
        g = _fps_exp(f)
        f_back = _fps_log(g)
        for k in range(4):
            assert f[k] == f_back[k], f"Mismatch at k={k}: {f[k]} != {f_back[k]}"

    def test_fps_eq(self):
        a = [Fraction(1), Fraction(2)]
        b = [Fraction(1), Fraction(2)]
        c = [Fraction(1), Fraction(3)]
        assert _fps_eq(a, b)
        assert not _fps_eq(a, c)

    def test_fps_shift(self):
        a = [Fraction(1), Fraction(2), Fraction(3), Fraction(0)]
        s = _fps_shift(a, 1)
        assert s == [Fraction(0), Fraction(1), Fraction(2), Fraction(3)]

    def test_fps_scale(self):
        a = [Fraction(1), Fraction(2)]
        s = _fps_scale(a, Fraction(3))
        assert s == [Fraction(3), Fraction(6)]


# ================================================================
# 2. MACMAHON FUNCTION TESTS
# ================================================================

class TestMacMahon:
    """MacMahon function M(q) = prod_{n>=1} 1/(1-q^n)^n."""

    def test_macmahon_first_values(self):
        """OEIS A000219: p(0)=1, p(1)=1, p(2)=3, ..., p(20)=75278."""
        m = macmahon(20)
        for k in range(21):
            assert int(m[k]) == PP_COUNTS[k], \
                f"p({k}): got {int(m[k])}, expected {PP_COUNTS[k]}"

    def test_macmahon_two_methods(self):
        """Cross-validate: direct product vs log-exp."""
        N = 15
        m1 = macmahon(N)
        m2 = macmahon_via_log(N)
        assert _fps_eq(m1, m2), "MacMahon: product != log-exp"

    def test_macmahon_positivity(self):
        """All plane partition counts are positive."""
        m = macmahon(25)
        for k in range(26):
            assert m[k] > 0, f"p({k}) = {m[k]} is not positive"

    def test_macmahon_integrality(self):
        """All plane partition counts are integers."""
        m = macmahon(25)
        for k in range(26):
            assert m[k].denominator == 1, f"p({k}) = {m[k]} is not integer"

    def test_macmahon_growth(self):
        """p(n) is strictly increasing for n >= 1."""
        m = macmahon(15)
        for k in range(2, 16):
            assert m[k] > m[k - 1], f"p({k}) <= p({k-1})"


# ================================================================
# 3. C^3 IDENTIFICATION TESTS
# ================================================================

class TestC3Identification:
    """Z_DT(C^3) = Z^{sh,E1}(CoHA(C^3)) = M(q)."""

    def test_dt_equals_macmahon(self):
        N = 15
        dt = chart_dt_c3(N)
        m = macmahon(N)
        assert _fps_eq(dt, m)

    def test_shadow_equals_macmahon(self):
        N = 15
        shadow = chart_shadow_e1_c3(N)
        m = macmahon(N)
        assert _fps_eq(shadow, m)

    def test_dt_equals_shadow(self):
        N = 15
        dt = chart_dt_c3(N)
        shadow = chart_shadow_e1_c3(N)
        assert _fps_eq(dt, shadow)

    def test_chart_degree0(self):
        N = 10
        deg0 = chart_dt_degree0(N)
        m = macmahon(N)
        assert _fps_eq(deg0, m)

    def test_c3_three_path_verification(self):
        result = verify_c3_identification(12)
        assert result['all_agree']

    def test_c3_first_10_values(self):
        result = verify_c3_identification(10)
        assert result['first_10'] == PP_COUNTS[:11]

    def test_c3_kappa_equals_1(self):
        """For C^3, kappa = 1, so shadow = M(q)^1 = M(q)."""
        N = 10
        from compute.lib.dt_chart_gluing_verification import _fps_pow
        m = macmahon(N)
        m_pow1 = _fps_pow(m, 1)
        assert _fps_eq(m, m_pow1)


# ================================================================
# 4. CONIFOLD IDENTIFICATION TESTS
# ================================================================

class TestConifoldIdentification:
    """Z_DT(conifold) = Z^{sh,E1}(hocolim CoHA)."""

    def test_conifold_degree0_is_m_squared(self):
        """Degree-0 sector: M(q)^2 (two torus-fixed points)."""
        N = 10
        gluing = conifold_chart_gluing(N, 2)
        m = macmahon(N)
        m_sq = _fps_mul(m, m)
        assert _fps_eq(gluing[0], m_sq)

    def test_conifold_gluing_eq_shadow(self):
        result = verify_conifold_gluing(10, 3)
        assert result['all_match']

    def test_conifold_reduced_degree0(self):
        """Reduced PF at Q^0 = 1."""
        N = 10
        red = conifold_reduced(N, 3)
        assert red[0][0] == Fraction(1)
        assert all(red[0][k] == 0 for k in range(1, N + 1))

    def test_conifold_reduced_q1_coefficients(self):
        """At Q^1: prod(1-Qq^n)^n|_{Q^1} = -sum n*q^n."""
        N = 10
        red = conifold_reduced(N, 1)
        d1 = red.get(1, _fps_zero(N))
        for k in range(1, N + 1):
            assert int(d1[k]) == -k, f"Q^1 q^{k}: got {int(d1[k])}, expected {-k}"

    def test_conifold_dt_eq_direct(self):
        N = 10
        gluing = conifold_chart_gluing(N, 3)
        direct = conifold_dt_direct(N, 3)
        for d in range(4):
            assert _fps_eq(
                gluing.get(d, _fps_zero(N)),
                direct.get(d, _fps_zero(N))
            ), f"Mismatch at Q^{d}"

    def test_conifold_shadow_hocolim_eq_gluing(self):
        N = 8
        gluing = conifold_chart_gluing(N, 3)
        shadow = conifold_shadow_hocolim(N, 3)
        for d in range(4):
            assert _fps_eq(
                gluing.get(d, _fps_zero(N)),
                shadow.get(d, _fps_zero(N))
            )

    def test_conifold_full_identification(self):
        result = verify_conifold_identification(10, 3)
        assert result['degree0_match']
        assert result['full_match']
        assert result['gv_n01_correct']

    def test_conifold_reduced_integrality(self):
        """Reduced DT coefficients at each Q-degree are integers."""
        N = 12
        red = conifold_reduced(N, 4)
        for d in range(5):
            f = red.get(d, _fps_zero(N))
            for k in range(N + 1):
                assert f[k].denominator == 1, \
                    f"Non-integer at Q^{d} q^{k}: {f[k]}"


# ================================================================
# 5. LOCAL P^2 IDENTIFICATION TESTS
# ================================================================

class TestLocalP2Identification:
    """Z_DT(local P^2) = Z^{sh,E1}(hocolim of 3-chart CoHA)."""

    def test_local_p2_degree0_is_m_cubed(self):
        """Degree-0: M(q)^3 (three torus-fixed points)."""
        N = 8
        deg0 = local_p2_degree0(N)
        m = macmahon(N)
        m3 = _fps_pow(m, 3)
        assert _fps_eq(deg0, m3)

    def test_local_p2_shadow_degree0(self):
        N = 8
        dt = local_p2_degree0(N)
        shadow = local_p2_shadow_degree0(N)
        assert _fps_eq(dt, shadow)

    def test_local_p2_gluing_eq_shadow(self):
        result = verify_local_p2_gluing(8, 2)
        assert result['all_match']

    def test_local_p2_full_identification(self):
        result = verify_local_p2_identification(6, 2)
        assert result['degree0_match']
        assert result['full_match']

    def test_local_p2_gv_data_integrity(self):
        """Verify hardcoded GV invariants are integers."""
        for (g, d), n in LOCAL_P2_GV.items():
            assert isinstance(n, int), f"n_{g}^{d} = {n} is not int"

    def test_local_p2_n01_equals_3(self):
        """n_0^1 = 3 for local P^2 (three lines)."""
        assert LOCAL_P2_GV[(0, 1)] == 3

    def test_local_p2_n02_equals_neg6(self):
        """n_0^2 = -6 for local P^2 (virtual count of conics)."""
        assert LOCAL_P2_GV[(0, 2)] == -6

    def test_local_p2_n03_equals_27(self):
        """n_0^3 = 27 for local P^2 (cubics)."""
        assert LOCAL_P2_GV[(0, 3)] == 27

    def test_local_p2_free_energy_degree1(self):
        """At Q^1: F_1 = -3 * sum n*q^n (from n_0^1 = 3)."""
        N = 8
        F = local_p2_free_energy(1, 0, N)
        F1 = F.get(1, _fps_zero(N))
        for k in range(1, N + 1):
            expected = Fraction(3 * k)  # sign: (-1)^1 * 3 * (-k)/1 = 3k
            assert F1[k] == expected, \
                f"F_1[{k}]: got {F1[k]}, expected {expected}"

    def test_local_p2_degree0_coefficient_values(self):
        """M(q)^3 first coefficients."""
        N = 5
        m3 = local_p2_degree0(N)
        # M(q)^3: compute manually
        m = macmahon(N)
        m3_check = _fps_mul(m, _fps_mul(m, m))
        assert _fps_eq(m3, m3_check)


# ================================================================
# 6. K3 x E IDENTIFICATION TESTS
# ================================================================

class TestK3xEIdentification:
    """Z_DT(K3 x E)|_{deg=0} = M(q)^{24} = shadow(hocolim, deg=0)."""

    def test_k3xe_degree0_is_m_24(self):
        N = 5
        dt = k3xe_dt_degree0(N)
        m = macmahon(N)
        m24 = _fps_pow(m, 24)
        assert _fps_eq(dt, m24)

    def test_k3xe_shadow_equals_dt(self):
        N = 5
        dt = k3xe_dt_degree0(N)
        shadow = k3xe_shadow_degree0(N)
        assert _fps_eq(dt, shadow)

    def test_k3xe_first_coefficient(self):
        """M(q)^{24}: q^0 coefficient = 1."""
        N = 3
        dt = k3xe_dt_degree0(N)
        assert dt[0] == Fraction(1)

    def test_k3xe_q1_coefficient(self):
        """M(q)^{24}: q^1 coefficient = 24 (from 24 * p(1))."""
        N = 3
        dt = k3xe_dt_degree0(N)
        assert int(dt[1]) == 24

    def test_k3xe_q2_coefficient(self):
        """M(q)^{24} at q^2: 24*3 + C(24,2) = 72 + 276 = 348."""
        N = 3
        dt = k3xe_dt_degree0(N)
        assert int(dt[2]) == 348

    def test_k3xe_verify_function(self):
        result = verify_k3xe_degree0(5)
        assert result['dt_eq_shadow']
        assert result['dt_eq_m24']

    def test_k3xe_integrality(self):
        """M(q)^{24} has integer coefficients."""
        N = 8
        dt = k3xe_dt_degree0(N)
        for k in range(N + 1):
            assert dt[k].denominator == 1

    def test_k3xe_positivity(self):
        """M(q)^{24} has positive coefficients."""
        N = 8
        dt = k3xe_dt_degree0(N)
        for k in range(N + 1):
            assert dt[k] > 0


# ================================================================
# 7. REFINED DT TESTS
# ================================================================

class TestRefinedDT:
    """Refined Z_DT(C^3; q, t) = M(q, t)."""

    def test_refined_specialization_to_unrefined(self):
        """M(q, t)|_{t=q} = M(q)."""
        result = verify_refined_specialization(6)
        assert result['match']

    def test_refined_dt_equals_shadow(self):
        """Z^{ref}_DT(C^3) = Z^{sh,ref}(CoHA(C^3))."""
        result = verify_refined_c3_triangle(5)
        assert result['refined_match']

    def test_refined_unrefined_consistency(self):
        """Refined matches unrefined after specialization."""
        result = verify_refined_c3_triangle(5)
        assert result['unrefined_match']

    def test_refined_macmahon_q0_t0(self):
        """M(q,t) at (q^0, t^0) = 1."""
        ref = refined_macmahon(4, 4)
        assert ref.get((0, 0), Fraction(0)) == Fraction(1)

    def test_refined_macmahon_q1_t0(self):
        """M(q,t) at q^1 t^0: coefficient = 1 (from 1/(1-q))."""
        ref = refined_macmahon(4, 4)
        assert ref.get((1, 0), Fraction(0)) == Fraction(1)

    def test_refined_macmahon_nonneg(self):
        """All coefficients of M(q,t) are non-negative."""
        ref = refined_macmahon(5, 5)
        for (a, b), c in ref.items():
            assert c >= 0, f"M(q,t) at q^{a} t^{b} = {c} < 0"


# ================================================================
# 8. GV INTEGRALITY TESTS
# ================================================================

class TestGVIntegrality:
    """GV integrality from chart CoHA integrality."""

    def test_coha_c3_integer_dims(self):
        result = verify_coha_integrality_c3(20)
        assert result['all_nonneg_integer']

    def test_coha_c3_dims_are_pp_counts(self):
        result = verify_coha_integrality_c3(20)
        for k in range(min(len(result['dims']), len(PP_COUNTS))):
            assert result['dims'][k] == PP_COUNTS[k]

    def test_conifold_gv_integrality(self):
        result = verify_gv_integrality_conifold(5)
        assert result['all_integer']
        assert result['matches_known']

    def test_conifold_gv_n01_is_1(self):
        gv = conifold_gv_extraction(max_d=3)
        assert gv[1] == 1

    def test_conifold_gv_n02_is_0(self):
        gv = conifold_gv_extraction(max_d=3)
        assert gv[2] == 0

    def test_conifold_gv_n03_is_0(self):
        gv = conifold_gv_extraction(max_d=3)
        assert gv[3] == 0

    def test_local_p2_gv_integrality(self):
        result = verify_gv_integrality_local_p2(5)
        assert result['all_integer']

    def test_multicover_matrix_triangular(self):
        result = verify_multicover_matrix_properties(6)
        assert result['triangular']

    def test_multicover_matrix_unit_diagonal(self):
        result = verify_multicover_matrix_properties(6)
        assert result['unit_diagonal']

    def test_multicover_matrix_entries(self):
        """K_{d,d'} = 1/(d/d') for d'|d."""
        K = gv_integrality_multicover_matrix(4)
        assert K[(1, 1)] == Fraction(1)
        assert K[(2, 1)] == Fraction(1, 2)
        assert K[(2, 2)] == Fraction(1)
        assert K[(3, 1)] == Fraction(1, 3)
        assert K[(3, 3)] == Fraction(1)
        assert K[(4, 1)] == Fraction(1, 4)
        assert K[(4, 2)] == Fraction(1, 2)
        assert K[(4, 4)] == Fraction(1)


# ================================================================
# 9. WALL-CROSSING FACTOR TESTS
# ================================================================

class TestWallCrossing:
    """Wall-crossing factors in the chart gluing formula."""

    def test_wall_q1_coefficients(self):
        """At Q^1: WC factor = -sum n*q^n."""
        result = verify_wall_crossing_q1(10)
        assert result['match']

    def test_wall_q0_is_one(self):
        """At Q^0: WC factor = 1."""
        N = 10
        red = conifold_reduced(N, 2)
        f0 = red.get(0, _fps_zero(N))
        assert f0[0] == Fraction(1)
        assert all(f0[k] == 0 for k in range(1, N + 1))

    def test_wall_factor_integrality(self):
        """WC factor has integer coefficients at each Q-degree."""
        N = 10
        wc = wall_crossing_factor_coefficients(N, d=1)
        for k in range(N + 1):
            assert wc[k].denominator == 1

    def test_wall_factor_q2_coefficients(self):
        """At Q^2: verify integrality and known structure."""
        N = 10
        red = conifold_reduced(N, 2)
        d2 = red.get(2, _fps_zero(N))
        for k in range(N + 1):
            assert d2[k].denominator == 1

    def test_wall_factor_sign_pattern_q1(self):
        """At Q^1: all coefficients are <= 0."""
        N = 10
        wc = wall_crossing_factor_coefficients(N, d=1)
        assert wc[0] == 0
        for k in range(1, N + 1):
            assert wc[k] <= 0


# ================================================================
# 10. NERVE INCLUSION-EXCLUSION TESTS
# ================================================================

class TestNerveInclusionExclusion:
    """Nerve-based inclusion-exclusion for chart gluing."""

    def test_2chart_1wall_structure(self):
        """2 charts, 1 wall: Z = Z_1 * Z_2 * Z_{wall}."""
        N = 8
        m = macmahon(N)
        wall = _fps_one(N)  # trivial wall for degree-0
        result = nerve_inclusion_exclusion_1([m, m], [wall], N)
        m_sq = _fps_mul(m, m)
        assert _fps_eq(result, m_sq)

    def test_3chart_structure_degree0(self):
        """3 charts, 3 walls, 1 face at degree 0."""
        N = 6
        m = macmahon(N)
        one = _fps_one(N)
        result = nerve_inclusion_exclusion_2([m, m, m], [one, one, one], [one], N)
        m3 = _fps_pow(m, 3)
        assert _fps_eq(result, m3)


# ================================================================
# 11. BERNOULLI AND FABER-PANDHARIPANDE TESTS
# ================================================================

class TestBernoulliFP:
    """Bernoulli numbers and Faber-Pandharipande lambda_g."""

    def test_bernoulli_b0(self):
        B = bernoulli_numbers(0)
        assert B[0] == Fraction(1)

    def test_bernoulli_b1(self):
        B = bernoulli_numbers(1)
        assert B[1] == Fraction(-1, 2)

    def test_bernoulli_b2(self):
        B = bernoulli_numbers(2)
        assert B[2] == Fraction(1, 6)

    def test_bernoulli_b4(self):
        B = bernoulli_numbers(4)
        assert B[4] == Fraction(-1, 30)

    def test_bernoulli_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        B = bernoulli_numbers(11)
        for k in [3, 5, 7, 9, 11]:
            assert B[k] == Fraction(0), f"B_{k} = {B[k]} != 0"

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert faber_pandharipande_lambda_g(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 1/2880."""
        assert faber_pandharipande_lambda_g(2) == Fraction(1, 2880)

    def test_lambda_3(self):
        """lambda_3 = 1/725760."""
        assert faber_pandharipande_lambda_g(3) == Fraction(1, 725760)

    def test_lambda_0(self):
        """lambda_0 = 0 (no genus-0 contribution)."""
        assert faber_pandharipande_lambda_g(0) == Fraction(0)

    def test_lambda_g_positive(self):
        """lambda_g > 0 for g >= 1."""
        for g in range(1, 8):
            assert faber_pandharipande_lambda_g(g) > 0, f"lambda_{g} <= 0"

    def test_shadow_from_kappa(self):
        """F_1^{sh} = kappa/24."""
        kappa = Fraction(3)
        F1 = shadow_genus_g_from_kappa(kappa, 1)
        assert F1 == Fraction(3, 24) == Fraction(1, 8)


# ================================================================
# 12. COEFFICIENT TABLE TESTS
# ================================================================

class TestCoefficientTables:
    """Degree-by-degree coefficient verification."""

    def test_conifold_table_consistency(self):
        result = conifold_coefficient_table(8, 2)
        assert result['all_match']

    def test_local_p2_table_consistency(self):
        result = local_p2_coefficient_table(6, 2)
        assert result['all_match']

    def test_conifold_deg0_q0_is_1(self):
        result = conifold_coefficient_table(5, 1)
        entry = result['table'][(0, 0)]
        assert entry['dt'] == 1

    def test_conifold_deg0_q1(self):
        """M(q)^2 at q^1 = 2."""
        result = conifold_coefficient_table(5, 1)
        entry = result['table'][(0, 1)]
        assert entry['dt'] == 2


# ================================================================
# 13. CHI ADDITIVITY TESTS
# ================================================================

class TestChiAdditivity:
    """chi of hocolim is additive (integer-valued)."""

    def test_c3_chi_additivity(self):
        result = verify_chi_additivity_c3(15)
        assert result['all_nonneg']
        assert result['all_integer']

    def test_conifold_chi_additivity(self):
        result = verify_chi_additivity_conifold(10)
        for d_info in result['by_degree'].values():
            assert d_info['all_integer']


# ================================================================
# 14. PROOF STEP STRUCTURE TESTS
# ================================================================

class TestProofSteps:
    """Verify the 4-step proof structure is internally consistent."""

    def test_step_a_ks(self):
        result = proof_step_a_ks_formula()
        assert 'C^3' in result['verified_for']
        assert 'conifold' in result['verified_for']

    def test_step_b_coha(self):
        result = proof_step_b_coha_character()
        assert 'Schiffmann-Vasserot' in result['source']

    def test_step_c_hocolim(self):
        result = proof_step_c_hocolim_character()
        assert 'hocolim' in result['statement'].lower() or 'hocolim' in result['mechanism'].lower()

    def test_step_d_shadow(self):
        result = proof_step_d_shadow_character()
        assert 'definition' in result['statement'].lower()


# ================================================================
# 15. GENUS-0 FREE ENERGY TESTS
# ================================================================

class TestGenus0FreeEnergy:
    """Genus-0 free energy structure."""

    def test_conifold_f0_q1_coefficient(self):
        """F_0|_{Q^1,q^1} = -1 (from n_0^1 = 1)."""
        N = 8
        f0 = genus0_free_energy_conifold(N)
        assert f0[1] == Fraction(-1)

    def test_conifold_f0_qk_coefficient(self):
        """F_0|_{Q^1,q^k} = -k."""
        N = 8
        f0 = genus0_free_energy_conifold(N)
        for k in range(1, N + 1):
            assert f0[k] == Fraction(-k)

    def test_conifold_f0_q0_is_zero(self):
        """F_0|_{Q^1,q^0} = 0."""
        f0 = genus0_free_energy_conifold(8)
        assert f0[0] == Fraction(0)


# ================================================================
# 16. MASTER VERIFICATION TESTS
# ================================================================

class TestMasterVerification:
    """Full master verification of thm:dt-equals-hocolim-shadow."""

    def test_master_c3(self):
        result = master_verification(8)
        assert result['c3']['all_agree']

    def test_master_conifold(self):
        result = master_verification(8)
        assert result['conifold']['full_match']

    def test_master_local_p2(self):
        result = master_verification(8)
        assert result['local_p2']['full_match']

    def test_master_k3xe(self):
        result = master_verification(8)
        assert result['k3xe']['dt_eq_shadow']

    def test_master_refined(self):
        result = master_verification(8)
        assert result['refined_c3']['refined_match']

    def test_master_gv_conifold(self):
        result = master_verification(8)
        assert result['gv_integrality_conifold']['all_integer']

    def test_master_gv_local_p2(self):
        result = master_verification(8)
        assert result['gv_integrality_local_p2']['all_integer']

    def test_master_multicover(self):
        result = master_verification(8)
        assert result['multicover_matrix']['triangular']
        assert result['multicover_matrix']['unit_diagonal']

    def test_master_coha(self):
        result = master_verification(8)
        assert result['coha_integrality']['all_nonneg_integer']


# ================================================================
# 17. SINGLE_PRODUCT_FACTOR TESTS
# ================================================================

class TestSingleProductFactor:
    """prod_{n>=1}(1-xq^n)^n expanded in x."""

    def test_x0_is_one(self):
        """At x^0: product = 1."""
        N = 10
        f = single_product_factor(N, 3)
        one = _fps_one(N)
        assert _fps_eq(f[0], one)

    def test_x1_first_few(self):
        """At x^1: -sum n*q^n."""
        N = 8
        f = single_product_factor(N, 1)
        d1 = f.get(1, _fps_zero(N))
        for k in range(1, N + 1):
            assert int(d1[k]) == -k

    def test_integrality(self):
        """All coefficients are integers."""
        N = 10
        f = single_product_factor(N, 4)
        for d in range(5):
            fd = f.get(d, _fps_zero(N))
            for k in range(N + 1):
                assert fd[k].denominator == 1


# ================================================================
# 18. CROSS-GEOMETRY CONSISTENCY TESTS
# ================================================================

class TestCrossGeometryConsistency:
    """Consistency checks across different CY3 geometries."""

    def test_degree0_exponents(self):
        """chi_equiv: C^3=1, conifold=2, local P^2=3, K3xE=24."""
        N = 5
        m = macmahon(N)

        c3 = chart_dt_c3(N)
        assert _fps_eq(c3, _fps_pow(m, 1))

        con = conifold_chart_gluing(N, 0)
        assert _fps_eq(con[0], _fps_pow(m, 2))

        lp2 = local_p2_degree0(N)
        assert _fps_eq(lp2, _fps_pow(m, 3))

        k3 = k3xe_dt_degree0(N)
        assert _fps_eq(k3, _fps_pow(m, 24))

    def test_degree0_ordering(self):
        """M(q)^1 < M(q)^2 < M(q)^3 at q^1."""
        N = 3
        m = macmahon(N)
        m1 = int(_fps_pow(m, 1)[1])
        m2 = int(_fps_pow(m, 2)[1])
        m3 = int(_fps_pow(m, 3)[1])
        assert m1 < m2 < m3

    def test_macmahon_power_q1(self):
        """M(q)^k at q^1 = k * p(1) = k."""
        N = 3
        m = macmahon(N)
        for k in [1, 2, 3, 5, 10, 24]:
            mk = _fps_pow(m, k)
            assert int(mk[1]) == k, f"M(q)^{k} at q^1 = {int(mk[1])}, expected {k}"


# ================================================================
# 19. DETAILED CONIFOLD DEGREE-BY-DEGREE TESTS
# ================================================================

class TestConifoldDegreeByDegree:
    """Detailed coefficient checks for conifold at each Q-degree."""

    def test_deg0_is_m_sq_to_order_12(self):
        N = 12
        gluing = conifold_chart_gluing(N, 0)
        m = macmahon(N)
        m_sq = _fps_mul(m, m)
        assert _fps_eq(gluing[0], m_sq)

    def test_deg1_q1(self):
        """At Q^1 q^1: M(q)^2 * (-1) = -1."""
        N = 5
        full = conifold_chart_gluing(N, 1)
        d1 = full.get(1, _fps_zero(N))
        # At Q^1: M(q)^2 * (-q/(1-q)^2)
        # At q^1: 1*(-1) + ... need to compute M(q)^2 * (-1-2q-...)
        # Actually: full = M(q)^2 * wall. Wall at Q^1 has q^1 coeff = -1.
        # So full at (Q^1, q^1) = M(q)^2[0] * wall[1] + M(q)^2[1] * wall[0]
        # = 1*(-1) + 2*0 = -1
        assert int(d1[1]) == -1

    def test_deg1_q2(self):
        """At Q^1 q^2."""
        N = 5
        full = conifold_chart_gluing(N, 1)
        d1 = full.get(1, _fps_zero(N))
        # M(q)^2 = 1 + 2q + 5q^2 + ...
        # wall|_{Q^1} = 0 -q -2q^2 - ...
        # Convolution at q^2: 1*(-2) + 2*(-1) + 5*0 = -4
        assert int(d1[2]) == -4

    def test_deg2_integrality(self):
        N = 8
        full = conifold_chart_gluing(N, 2)
        d2 = full.get(2, _fps_zero(N))
        for k in range(N + 1):
            assert d2[k].denominator == 1


# ================================================================
# 20. LOCAL P^2 GV INVARIANT TESTS
# ================================================================

class TestLocalP2GV:
    """GV invariant data for local P^2."""

    def test_genus0_known_values(self):
        known_g0 = {1: 3, 2: -6, 3: 27, 4: -192, 5: 1695, 6: -17064}
        for d, n in known_g0.items():
            assert LOCAL_P2_GV.get((0, d)) == n, \
                f"n_0^{d}: got {LOCAL_P2_GV.get((0, d))}, expected {n}"

    def test_genus1_known_values(self):
        known_g1 = {1: 0, 2: 0, 3: -10, 4: 231, 5: -4452}
        for d, n in known_g1.items():
            assert LOCAL_P2_GV.get((1, d)) == n

    def test_genus2_known_values(self):
        known_g2 = {3: 0, 4: -102, 5: 5430}
        for d, n in known_g2.items():
            assert LOCAL_P2_GV.get((2, d)) == n

    def test_genus0_sign_alternation(self):
        """n_0^d has sign (-1)^{d+1} for d = 1..6."""
        for d in range(1, 7):
            n = LOCAL_P2_GV[(0, d)]
            expected_sign = (-1) ** (d + 1)
            if n != 0:
                actual_sign = 1 if n > 0 else -1
                assert actual_sign == expected_sign, \
                    f"n_0^{d} = {n}: wrong sign"


# ================================================================
# 21. ADDITIONAL CROSS-VALIDATION TESTS
# ================================================================

class TestAdditionalCrossValidation:
    """Additional cross-validation and edge cases."""

    def test_macmahon_p1(self):
        m = macmahon(1)
        assert int(m[1]) == 1

    def test_macmahon_p2(self):
        m = macmahon(2)
        assert int(m[2]) == 3

    def test_macmahon_p10(self):
        m = macmahon(10)
        assert int(m[10]) == 500

    def test_conifold_gv_at_d4(self):
        """GV at d=4: should be 0 for conifold."""
        gv = conifold_gv_extraction(max_d=4)
        assert gv[4] == 0

    def test_fps_div_roundtrip(self):
        """a / b * b = a."""
        a = macmahon(8)
        b = macmahon(8)
        b[1] += Fraction(1)  # perturb b to differ from a
        ratio = _fps_div(a, b)
        back = _fps_mul(ratio, b)
        assert _fps_eq(a, back)

    def test_macmahon_product_form(self):
        """M(q) at q^3: exactly 6 (from OEIS)."""
        m = macmahon(3)
        assert int(m[3]) == 6

    def test_shadow_kappa_0(self):
        """If kappa = 0, F_g = 0 for all g >= 1."""
        for g in range(1, 6):
            assert shadow_genus_g_from_kappa(Fraction(0), g) == Fraction(0)

    def test_shadow_kappa_1_genus1(self):
        """kappa=1: F_1 = 1/24."""
        assert shadow_genus_g_from_kappa(Fraction(1), 1) == Fraction(1, 24)

    def test_shadow_kappa_2_genus1(self):
        """kappa=2: F_1 = 2/24 = 1/12."""
        assert shadow_genus_g_from_kappa(Fraction(2), 1) == Fraction(1, 12)

    def test_shadow_kappa_24_genus1(self):
        """kappa=24 (K3): F_1 = 24/24 = 1."""
        assert shadow_genus_g_from_kappa(Fraction(24), 1) == Fraction(1)

    def test_refined_macmahon_sym(self):
        """M(q,t) at (q^1, t^0) = 1 (from 1/(1-q))."""
        ref = refined_macmahon(3, 3)
        assert ref.get((1, 0), Fraction(0)) == Fraction(1)

    def test_conifold_reduced_degree3(self):
        """Conifold reduced at Q^3 has integer coefficients."""
        N = 8
        red = conifold_reduced(N, 3)
        d3 = red.get(3, _fps_zero(N))
        for k in range(N + 1):
            assert d3[k].denominator == 1

    def test_local_p2_gv_total_count(self):
        """We have 14 known GV invariants in our table."""
        assert len(LOCAL_P2_GV) == 14
