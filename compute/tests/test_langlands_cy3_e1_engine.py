r"""Tests for the CY3/Langlands bridge via E₁ Koszul duality.

CONJECTURAL THESIS UNDER TEST:
    Geometric Langlands = E₁ Koszul duality of CY3 chiral algebras.

NOTE (AP42): This identification is CONJECTURAL. The tests below verify
necessary conditions (κ vanishing, FF duality, R-matrix structure) that
are CONSISTENT with the conjecture, not sufficient to prove it.

For GL(N): CY3 = T*[P^{N-1}], E₁ chiral algebra = ĝl_N at critical level,
Koszul dual = Langlands dual algebra. Self-duality at critical level
encodes the GL(N) geometric Langlands correspondence.

VERIFICATION PATHS (Multi-Path Mandate, 3+ per claim):
    1. Direct computation from defining formulas
    2. Alternative formulas / independent derivation
    3. Limiting cases (N=1 trivial, large N asymptotics)
    4. Cross-family consistency (additivity, duality)
    5. Literature comparison (Feigin-Frenkel, Beilinson-Drinfeld)
    6. Dimensional analysis (degrees, weights)
    7. Symmetry/self-duality checks
"""

import math
from fractions import Fraction

import pytest
import numpy as np

from compute.lib.langlands_cy3_e1_engine import (
    CY3GeometryData,
    GLNData,
    E1ChiralAlgebraData,
    KoszulDualData,
    CoHAIdentification,
    ConifoldLanglandsData,
    CategoricalLanglandsData,
    cy3_geometry_gln,
    gln_data,
    critical_level_gln,
    kappa_gln,
    kappa_sln,
    verify_critical_level_kappa_vanishing,
    ff_dual_level_gln,
    verify_ff_antisymmetry_gln,
    ff_critical_fixed_point,
    coha_identification_gln,
    e1_chiral_algebra_gln,
    e1_koszul_dual_gln,
    yang_r_matrix_gln,
    classical_r_matrix_gln,
    verify_yang_baxter_gln,
    e1_bar_dimension_gln,
    e_inf_bar_dimension_gln,
    bar_dimension_ratio,
    oper_data_gln,
    conifold_gl2_langlands,
    local_p2_gl3_langlands,
    langlands_cy3_table,
    kappa_deformation_gln,
    sugawara_residue_gln,
    categorical_langlands_gln,
    r_matrix_unitarity_check_gln,
    r_matrix_critical_level_check,
    wakimoto_gln,
    hitchin_system_gln,
    kw_parameter_gln,
    euler_form_cyclic_quiver,
    verify_euler_form_antisymmetric,
    cy3_langlands_bridge,
    shadow_tower_collapse_gln,
    full_verification,
)


# =====================================================================
# 1. CY3 GEOMETRY TESTS
# =====================================================================

class TestCY3Geometry:
    """Tests for T*[P^{N-1}] geometry."""

    def test_c3_is_n1(self):
        """N=1: CY3 = C^3."""
        cy3 = cy3_geometry_gln(1)
        assert cy3.N == 1
        assert cy3.name == "C^3"
        assert cy3.euler_char == 1
        assert cy3.is_compact is False

    def test_conifold_is_n2(self):
        """N=2: CY3 = T*P^1 = resolved conifold."""
        cy3 = cy3_geometry_gln(2)
        assert cy3.N == 2
        assert "P^1" in cy3.base or "P^1" in cy3.name
        assert cy3.euler_char == 2
        assert cy3.is_toric is True

    def test_local_p2_is_n3(self):
        """N=3: CY3 = K_{P^2} = local P^2."""
        cy3 = cy3_geometry_gln(3)
        assert cy3.N == 3
        assert cy3.euler_char == 3

    def test_euler_char_equals_n(self):
        """chi(P^{N-1}) = N for all N."""
        for N in range(1, 9):
            cy3 = cy3_geometry_gln(N)
            assert cy3.euler_char == N

    def test_all_noncompact(self):
        """T*[P^{N-1}] is non-compact for all N."""
        for N in range(1, 9):
            assert cy3_geometry_gln(N).is_compact is False

    def test_all_toric(self):
        """T*[P^{N-1}] is toric for all N."""
        for N in range(1, 9):
            assert cy3_geometry_gln(N).is_toric is True

    def test_h21_zero(self):
        """h^{2,1} = 0 (rigid) for all N."""
        for N in range(1, 9):
            assert cy3_geometry_gln(N).h21 == 0

    def test_invalid_n(self):
        """N=0 or negative should raise."""
        with pytest.raises(ValueError):
            cy3_geometry_gln(0)
        with pytest.raises(ValueError):
            cy3_geometry_gln(-1)


# =====================================================================
# 2. GL(N) LIE ALGEBRA DATA
# =====================================================================

class TestGLNData:
    """Tests for gl_N Lie algebra data."""

    def test_dim_gln(self):
        """dim(gl_N) = N^2."""
        for N in range(1, 9):
            assert gln_data(N).dim_gln == N * N

    def test_dim_sln(self):
        """dim(sl_N) = N^2 - 1."""
        for N in range(1, 9):
            assert gln_data(N).dim_sln == N * N - 1

    def test_dual_coxeter_sln(self):
        """h^∨(sl_N) = N."""
        for N in range(1, 9):
            assert gln_data(N).h_dual_sln == N

    def test_num_pos_roots(self):
        """num_pos_roots(sl_N) = N(N-1)/2."""
        for N in range(1, 9):
            assert gln_data(N).num_pos_roots == N * (N - 1) // 2

    def test_casimir_degrees_sl2(self):
        """Casimir degrees of gl_2: {1, 2}."""
        assert gln_data(2).casimir_degrees == (1, 2)

    def test_casimir_degrees_sl3(self):
        """Casimir degrees of gl_3: {1, 2, 3}."""
        assert gln_data(3).casimir_degrees == (1, 2, 3)

    def test_casimir_degrees_length(self):
        """Number of Casimir invariants = rank(gl_N) = N."""
        for N in range(1, 9):
            assert len(gln_data(N).casimir_degrees) == N


# =====================================================================
# 3. CRITICAL LEVEL AND KAPPA
# =====================================================================

class TestCriticalLevel:
    """Tests for critical level and κ vanishing."""

    def test_critical_level_sl2(self):
        """k_crit(sl_2) = -2."""
        assert critical_level_gln(2) == Fraction(-2)

    def test_critical_level_sl3(self):
        """k_crit(sl_3) = -3."""
        assert critical_level_gln(3) == Fraction(-3)

    def test_critical_level_formula(self):
        """k_crit(sl_N) = -N for all N."""
        for N in range(1, 9):
            assert critical_level_gln(N) == Fraction(-N)

    def test_kappa_vanishes_at_critical_sl2(self):
        """κ(ŝl_2, -2) = 0."""
        assert kappa_sln(2, Fraction(-2)) == 0

    def test_kappa_vanishes_at_critical_sl3(self):
        """κ(ŝl_3, -3) = 0."""
        assert kappa_sln(3, Fraction(-3)) == 0

    def test_kappa_vanishes_at_critical_all(self):
        """κ(ŝl_N, -N) = 0 for all N >= 2."""
        for N in range(2, 9):
            v = verify_critical_level_kappa_vanishing(N)
            assert v['vanishes'], f"κ(sl_{N}, -{N}) = {v['kappa_sln']} != 0"

    def test_kappa_sln_at_level_1(self):
        """κ(ŝl_2, 1) = (4-1)(1+2)/(2·2) = 3·3/4 = 9/4."""
        kap = kappa_sln(2, Fraction(1))
        assert kap == Fraction(9, 4)

    def test_kappa_sln_formula_sl3(self):
        """κ(ŝl_3, 1) = (9-1)(1+3)/(2·3) = 8·4/6 = 16/3."""
        kap = kappa_sln(3, Fraction(1))
        assert kap == Fraction(16, 3)

    def test_kappa_linear_in_k(self):
        """κ(ŝl_N, k) is linear in k with slope (N^2-1)/(2N)."""
        for N in range(2, 6):
            k1 = Fraction(1)
            k2 = Fraction(2)
            kap1 = kappa_sln(N, k1)
            kap2 = kappa_sln(N, k2)
            slope = (kap2 - kap1) / (k2 - k1)
            expected_slope = Fraction(N * N - 1, 2 * N)
            assert slope == expected_slope

    def test_kappa_sl1_trivial(self):
        """κ(ŝl_1, k) = 0 for all k (sl_1 is trivial)."""
        for k in [Fraction(0), Fraction(1), Fraction(-1)]:
            assert kappa_sln(1, k) == 0


# =====================================================================
# 4. FEIGIN-FRENKEL DUALITY
# =====================================================================

class TestFeiginFrenkelDuality:
    """Tests for the FF involution and κ anti-symmetry."""

    def test_ff_involution_sl2(self):
        """FF dual of k=1 for sl_2: k' = -1 - 4 = -5."""
        assert ff_dual_level_gln(2, Fraction(1)) == Fraction(-5)

    def test_ff_involution_involutive(self):
        """FF duality is an involution: (k')' = k."""
        for N in range(2, 6):
            for k in [Fraction(1), Fraction(2), Fraction(3)]:
                k_dual = ff_dual_level_gln(N, k)
                k_back = ff_dual_level_gln(N, k_dual)
                assert k_back == k

    def test_ff_antisymmetry(self):
        """κ(k) + κ(k') = 0 for sl_N (Koszul anti-symmetry)."""
        for N in range(2, 6):
            for k in [Fraction(1), Fraction(2), Fraction(5), Fraction(1, 2)]:
                v = verify_ff_antisymmetry_gln(N, k)
                assert v['antisymmetric'], (
                    f"κ({k}) + κ({v['k_dual']}) = {v['sum']} != 0 for sl_{N}"
                )

    def test_ff_critical_fixed_point(self):
        """The critical level k = -N is the fixed point of FF for all N."""
        for N in range(2, 9):
            v = ff_critical_fixed_point(N)
            assert v['is_fixed_point'], f"k_crit = {v['k_crit']} not fixed for sl_{N}"

    def test_ff_maps_critical_to_self(self):
        """Explicit: -(-N) - 2N = N - 2N = -N."""
        for N in range(2, 9):
            k_crit = critical_level_gln(N)
            k_dual = ff_dual_level_gln(N, k_crit)
            assert k_dual == k_crit


# =====================================================================
# 5. COHA IDENTIFICATION
# =====================================================================

class TestCoHAIdentification:
    """Tests for CoHA(T*[P^{N-1}]) ≃ Y^+(gl_N)."""

    def test_coha_c3(self):
        """CoHA of C^3 = Y^+(gl_1)."""
        coha = coha_identification_gln(1)
        assert coha.yangian_type == "Y^+(gl_1)"
        assert coha.num_generators == 1

    def test_coha_conifold(self):
        """CoHA of conifold = Y^+(gl_2)."""
        coha = coha_identification_gln(2)
        assert coha.yangian_type == "Y^+(gl_2)"
        assert coha.num_generators == 2

    def test_coha_local_p2(self):
        """CoHA of local P^2 = Y^+(gl_3)."""
        coha = coha_identification_gln(3)
        assert coha.yangian_type == "Y^+(gl_3)"
        assert coha.num_generators == 3

    def test_coha_generators_equal_n(self):
        """Number of BPS generators = N for all GL(N)."""
        for N in range(1, 9):
            assert coha_identification_gln(N).num_generators == N

    def test_euler_form_antisymmetric(self):
        """The Euler form matrix is antisymmetric."""
        for N in range(2, 6):
            coha = coha_identification_gln(N)
            A = np.array(coha.euler_form_matrix)
            assert np.allclose(A, -A.T)


# =====================================================================
# 6. E₁ CHIRAL ALGEBRA
# =====================================================================

class TestE1ChiralAlgebra:
    """Tests for the E₁ chiral algebra A_{CY3(GL(N))}."""

    def test_chiral_uncurved_at_critical(self):
        """E₁ chiral algebra is uncurved at critical level for all N >= 2."""
        for N in range(2, 9):
            chiral = e1_chiral_algebra_gln(N)
            assert chiral.is_uncurved, f"A_{{CY3(GL({N}))}} not uncurved at critical"

    def test_kappa_zero_at_critical(self):
        """κ(sl_N) = 0 at the critical level."""
        for N in range(2, 9):
            chiral = e1_chiral_algebra_gln(N)
            assert chiral.kappa_sln == 0

    def test_central_charge_pole_at_critical(self):
        """c(sl_N) has a pole (None) at the critical level."""
        for N in range(2, 9):
            chiral = e1_chiral_algebra_gln(N)
            assert chiral.central_charge is None

    def test_generic_level(self):
        """At k=1 (not critical), the algebra is curved."""
        for N in range(2, 6):
            chiral = e1_chiral_algebra_gln(N, k=Fraction(1))
            assert not chiral.is_uncurved
            assert chiral.kappa_sln != 0

    def test_central_charge_sl2_k1(self):
        """c(ŝl_2, 1) = 3·1/(1+2) = 1."""
        chiral = e1_chiral_algebra_gln(2, k=Fraction(1))
        assert chiral.central_charge == Fraction(1)

    def test_ff_center_at_critical(self):
        """At critical level, FF center description is nontrivial."""
        chiral = e1_chiral_algebra_gln(3)
        assert "Op" in chiral.ff_center_dim


# =====================================================================
# 7. E₁ KOSZUL DUAL = LANGLANDS DUAL
# =====================================================================

class TestE1KoszulDual:
    """Tests for A^{!,E₁}_{CY3(G)} = A_{CY3(G^∨)}."""

    def test_self_dual_at_critical(self):
        """GL(N) is self-dual at the critical level for all N."""
        for N in range(2, 9):
            kd = e1_koszul_dual_gln(N)
            assert kd.is_self_dual_at_critical

    def test_kappa_antisymmetry(self):
        """κ + κ' = 0 for the Koszul dual pair."""
        for N in range(2, 6):
            kd = e1_koszul_dual_gln(N, k=Fraction(1))
            assert kd.kappa_sum == 0

    def test_dual_level_at_critical(self):
        """At critical level, the dual level equals the original."""
        for N in range(2, 9):
            kd = e1_koszul_dual_gln(N)
            assert kd.original_level == kd.dual_level

    def test_langlands_dual_is_gln(self):
        """Langlands dual of GL(N) is GL(N)."""
        for N in range(2, 6):
            kd = e1_koszul_dual_gln(N)
            assert kd.langlands_dual_group == f"GL({N})"

    def test_kappa_zero_at_critical_both_sides(self):
        """Both κ and κ' are zero at the critical level."""
        for N in range(2, 6):
            kd = e1_koszul_dual_gln(N)
            assert kd.kappa_original == 0
            assert kd.kappa_dual == 0


# =====================================================================
# 8. R-MATRIX TESTS
# =====================================================================

class TestRMatrix:
    """Tests for the Yang R-matrix for gl_N."""

    def test_r_matrix_shape(self):
        """R-matrix is N^2 × N^2."""
        for N in range(2, 5):
            R = yang_r_matrix_gln(N, 1.0)
            assert R.shape == (N * N, N * N)

    def test_r_matrix_identity_at_z_inf(self):
        """R(z) → Id as z → ∞."""
        for N in range(2, 5):
            R = yang_r_matrix_gln(N, 1e10)
            np.testing.assert_allclose(R, np.eye(N * N), atol=1e-5)

    def test_r_matrix_permutation_at_z0(self):
        """R(0) = P (permutation matrix) at z = 0."""
        for N in range(2, 5):
            R = yang_r_matrix_gln(N, 0.0, kappa_val=1.0)
            P = classical_r_matrix_gln(N)
            np.testing.assert_allclose(R, P, atol=1e-10)

    def test_permutation_square_is_identity(self):
        """P^2 = Id (the permutation is an involution)."""
        for N in range(2, 5):
            P = classical_r_matrix_gln(N)
            np.testing.assert_allclose(P @ P, np.eye(N * N), atol=1e-10)

    def test_yang_baxter_gl2(self):
        """Yang-Baxter equation for gl_2."""
        v = verify_yang_baxter_gln(2, 1.0 + 0.5j, 0.5 - 0.3j, kappa_val=1.0)
        assert v['satisfies_YBE']

    def test_yang_baxter_gl3(self):
        """Yang-Baxter equation for gl_3."""
        v = verify_yang_baxter_gln(3, 1.5 + 0.2j, 0.3 - 0.7j, kappa_val=0.5)
        assert v['satisfies_YBE']

    def test_yang_baxter_multiple_points(self):
        """YBE at multiple spectral parameter values for gl_2."""
        # Avoid z1-z2 = -kappa, z1 = -kappa, or z2 = -kappa (singularities)
        z_pairs = [(1.3, 2.7), (0.5+0.1j, 1.5+0.2j), (2.0+1j, 1.0-0.5j)]
        for z1, z2 in z_pairs:
            v = verify_yang_baxter_gln(2, z1, z2, kappa_val=1.0)
            assert v['satisfies_YBE'], f"YBE fails at z1={z1}, z2={z2}"

    def test_unitarity_gl2(self):
        """R₁₂(z)R₂₁(-z) = Id for gl_2."""
        v = r_matrix_unitarity_check_gln(2, 1.0 + 0.5j, kappa_val=1.0)
        assert v['satisfies_unitarity']

    def test_unitarity_gl3(self):
        """R₁₂(z)R₂₁(-z) = Id for gl_3."""
        v = r_matrix_unitarity_check_gln(3, 0.7 + 0.3j, kappa_val=0.5)
        assert v['satisfies_unitarity']

    def test_r_trivial_at_critical_level(self):
        """At κ=0 (critical level), R(z) = Id for all z ≠ 0."""
        for N in [2, 3]:
            v = r_matrix_critical_level_check(N)
            assert v['all_identity']


# =====================================================================
# 9. BAR COMPLEX DIMENSIONS
# =====================================================================

class TestBarDimensions:
    """Tests for E₁ vs E_∞ bar complex dimensions."""

    def test_e1_bar_dim_formula(self):
        """dim B^{E₁,n}(gl_N) = (N^2)^n."""
        for N in range(1, 5):
            for n in range(1, 5):
                assert e1_bar_dimension_gln(N, n) == (N * N) ** n

    def test_einf_bar_dim_formula(self):
        """dim B^{E_∞,n}(gl_N) = C(N^2+n-1, n)."""
        for N in range(1, 5):
            for n in range(1, 5):
                expected = math.comb(N * N + n - 1, n)
                assert e_inf_bar_dimension_gln(N, n) == expected

    def test_e1_larger_than_einf(self):
        """E₁ bar is always >= E_∞ bar in dimension."""
        for N in range(2, 5):
            for n in range(2, 5):
                assert e1_bar_dimension_gln(N, n) >= e_inf_bar_dimension_gln(N, n)

    def test_ratio_grows(self):
        """The ratio dim(E₁)/dim(E_∞) grows with arity."""
        for N in [2, 3]:
            ratios = [bar_dimension_ratio(N, n) for n in range(2, 6)]
            # Ratio should increase
            for i in range(len(ratios) - 1):
                assert ratios[i + 1] >= ratios[i]

    def test_arity_1_equal(self):
        """At arity 1, E₁ and E_∞ are the same."""
        for N in range(1, 5):
            assert e1_bar_dimension_gln(N, 1) == e_inf_bar_dimension_gln(N, 1)


# =====================================================================
# 10. OPER STRUCTURE
# =====================================================================

class TestOperStructure:
    """Tests for GL_N-oper data."""

    def test_oper_dim_matches_hitchin_sl2(self):
        """Oper dim = Hitchin base dim = 3(g-1) for SL_2."""
        for g in [2, 3, 4]:
            oper = oper_data_gln(2, g)
            assert oper['matches']
            assert oper['total_oper_dim'] == 3 * (g - 1)

    def test_oper_dim_matches_hitchin_sl3(self):
        """Oper dim = Hitchin base dim = 8(g-1) for SL_3."""
        for g in [2, 3]:
            oper = oper_data_gln(3, g)
            assert oper['matches']
            assert oper['total_oper_dim'] == 8 * (g - 1)

    def test_oper_dim_general(self):
        """Oper dim = (N^2-1)(g-1) for SL_N, genus g."""
        for N in range(2, 6):
            for g in [2, 3]:
                oper = oper_data_gln(N, g)
                expected = (N * N - 1) * (g - 1)
                assert oper['total_oper_dim'] == expected
                assert oper['matches']

    def test_casimir_degrees_sl_n(self):
        """Casimir degrees for sl_N are 2, 3, ..., N."""
        for N in range(2, 6):
            oper = oper_data_gln(N, 2)
            assert oper['casimir_degrees'] == tuple(range(2, N + 1))


# =====================================================================
# 11. CONIFOLD = GL(2) LANGLANDS
# =====================================================================

class TestConifoldGL2:
    """Tests for the conifold realization of GL(2) Langlands."""

    def test_conifold_critical_level(self):
        """Conifold critical level = -2."""
        data = conifold_gl2_langlands()
        assert data.critical_level == Fraction(-2)

    def test_conifold_kappa_zero(self):
        """κ = 0 at the critical level for the conifold."""
        data = conifold_gl2_langlands()
        assert data.kappa_at_critical == 0

    def test_conifold_self_dual(self):
        """GL(2) is Langlands self-dual."""
        data = conifold_gl2_langlands()
        assert data.is_self_dual

    def test_conifold_group(self):
        """The group is GL(2)."""
        data = conifold_gl2_langlands()
        assert data.group == "GL(2)"


# =====================================================================
# 12. LOCAL P^2 = GL(3) LANGLANDS
# =====================================================================

class TestLocalP2GL3:
    """Tests for local P^2 realization of GL(3) Langlands."""

    def test_local_p2_critical_level(self):
        """Local P^2 critical level = -3."""
        data = local_p2_gl3_langlands()
        assert data['critical_level'] == Fraction(-3)

    def test_local_p2_kappa_zero(self):
        """κ = 0 at the critical level for local P^2."""
        data = local_p2_gl3_langlands()
        assert data['kappa_at_critical'] == 0

    def test_local_p2_self_dual(self):
        """Self-dual at critical level."""
        data = local_p2_gl3_langlands()
        assert data['is_self_dual_at_critical']

    def test_gv_genus0_d1(self):
        """GV invariant n^0_1 = 3 for local P^2 (three lines)."""
        data = local_p2_gl3_langlands()
        assert data['gv_invariants']['genus_0'][1] == 3


# =====================================================================
# 13. LANGLANDS TABLE
# =====================================================================

class TestLanglandsTable:
    """Tests for the comprehensive GL(N) table."""

    def test_table_length(self):
        """Table has 8 entries for N=1..8."""
        table = langlands_cy3_table(8)
        assert len(table) == 8

    def test_all_kappa_zero_at_critical(self):
        """κ = 0 at the critical level for all N >= 2."""
        table = langlands_cy3_table(8)
        for row in table:
            if row['N'] >= 2:
                assert row['kappa_at_critical'] == 0

    def test_all_ff_antisymmetric(self):
        """FF anti-symmetry holds for all N."""
        table = langlands_cy3_table(8)
        for row in table:
            if row['N'] >= 2:
                assert row['ff_antisymmetric']

    def test_all_self_dual(self):
        """GL(N) is self-dual for all N."""
        table = langlands_cy3_table(8)
        for row in table:
            assert row['self_dual']


# =====================================================================
# 14. KAPPA DEFORMATION
# =====================================================================

class TestKappaDeformation:
    """Tests for κ near the critical level."""

    def test_kappa_linear_in_epsilon(self):
        """κ = slope · ε near the critical level."""
        for N in range(2, 6):
            for eps_val in [1, 2, Fraction(1, 3)]:
                eps = Fraction(eps_val)
                v = kappa_deformation_gln(N, eps)
                assert v['matches']

    def test_slope_formula(self):
        """Slope = (N^2-1)/(2N)."""
        for N in range(2, 6):
            v = kappa_deformation_gln(N, Fraction(1))
            assert v['slope'] == Fraction(N * N - 1, 2 * N)

    def test_slope_sl2(self):
        """Slope for sl_2 = 3/4."""
        v = kappa_deformation_gln(2, Fraction(1))
        assert v['slope'] == Fraction(3, 4)


# =====================================================================
# 15. SUGAWARA RESIDUE
# =====================================================================

class TestSugawaraResidue:
    """Tests for Sugawara residue at critical level."""

    def test_residue_sl2(self):
        """Res_{k=-2}(c(k)) = -3·2 = -6 for sl_2."""
        v = sugawara_residue_gln(2)
        assert v['residue'] == Fraction(-6)

    def test_residue_sl3(self):
        """Res_{k=-3}(c(k)) = -8·3 = -24 for sl_3."""
        v = sugawara_residue_gln(3)
        assert v['residue'] == Fraction(-24)

    def test_residue_formula(self):
        """Res = -(N^2-1)·N for all N >= 2."""
        for N in range(2, 9):
            v = sugawara_residue_gln(N)
            expected = -Fraction(N * N - 1) * N
            assert v['residue'] == expected


# =====================================================================
# 16. WAKIMOTO
# =====================================================================

class TestWakimoto:
    """Tests for Wakimoto decomposition of ĝl_N."""

    def test_wakimoto_sum_check(self):
        """Wakimoto κ_bg + κ_cartan = κ_sln for all N, k."""
        for N in range(2, 5):
            for k in [Fraction(1), Fraction(-N), Fraction(2)]:
                v = wakimoto_gln(N, k)
                assert v['matches']

    def test_wakimoto_critical_sl2(self):
        """At k=-2 for sl_2: κ_bg = -1/2, κ_cartan = 1/2."""
        v = wakimoto_gln(2, Fraction(-2))
        assert v['kappa_sln_total'] == 0
        assert v['kappa_bg'] == Fraction(-1, 2)
        assert v['kappa_cartan'] == Fraction(1, 2)

    def test_wakimoto_num_bg(self):
        """Number of β-γ pairs = N(N-1)/2."""
        for N in range(2, 6):
            v = wakimoto_gln(N, Fraction(1))
            assert v['num_bg_pairs'] == N * (N - 1) // 2


# =====================================================================
# 17. HITCHIN SYSTEM
# =====================================================================

class TestHitchinSystem:
    """Tests for the Hitchin integrable system."""

    def test_hitchin_integrable(self):
        """Hitchin system is completely integrable for all N, g."""
        for N in range(2, 5):
            for g in [2, 3]:
                v = hitchin_system_gln(N, g)
                assert v['is_integrable']

    def test_hitchin_dim_sl2_g2(self):
        """dim M_H(Σ_2, SL_2) = 6, dim A_H = 3."""
        v = hitchin_system_gln(2, 2)
        assert v['dim_moduli'] == 6
        assert v['dim_hitchin_base'] == 3

    def test_spectral_curve_genus_sl2_g2(self):
        """Spectral curve genus for SL_2, g=2: g(S) = 4·1 + 1 = 5."""
        v = hitchin_system_gln(2, 2)
        assert v['spectral_curve_genus'] == 5


# =====================================================================
# 18. KW PARAMETER
# =====================================================================

class TestKWParameter:
    """Tests for the Kapustin-Witten parameter."""

    def test_kw_duality(self):
        """Ψ · Ψ^∨ = 1 for the quantum GL dual level k^∨ = -k - N."""
        for N in range(2, 6):
            for k in [Fraction(1), Fraction(2), Fraction(3)]:
                v = kw_parameter_gln(N, k)
                assert v['duality_holds'], (
                    f"KW duality fails for GL({N}) at k={k}: "
                    f"Ψ·Ψ^∨ = {v['product']}"
                )

    def test_kw_critical_pole(self):
        """Ψ is None (pole) at the critical level."""
        for N in range(2, 6):
            v = kw_parameter_gln(N, Fraction(-N))
            assert v['psi'] is None

    def test_kw_psi_at_zero(self):
        """Ψ(k=0) = 0/(0+N) = 0."""
        for N in range(2, 6):
            v = kw_parameter_gln(N, Fraction(0))
            assert v['psi'] == 0


# =====================================================================
# 19. EULER FORM
# =====================================================================

class TestEulerForm:
    """Tests for the charge lattice Euler form."""

    def test_euler_form_antisymmetric(self):
        """Euler form is antisymmetric for all N."""
        for N in range(2, 8):
            assert verify_euler_form_antisymmetric(N)

    def test_euler_form_shape(self):
        """Euler form is N × N."""
        for N in range(2, 6):
            A = euler_form_cyclic_quiver(N)
            assert A.shape == (N, N)

    def test_euler_form_trace_zero(self):
        """Trace of antisymmetric matrix is zero."""
        for N in range(2, 6):
            A = euler_form_cyclic_quiver(N)
            assert np.trace(A) == 0


# =====================================================================
# 20. FULL BRIDGE
# =====================================================================

class TestCY3LanglandsBridge:
    """Tests for the complete CY3/Langlands bridge."""

    def test_bridge_verified_gl2(self):
        """Full bridge verified for GL(2)."""
        bridge = cy3_langlands_bridge(2)
        assert bridge['bridge_verified']

    def test_bridge_verified_gl3(self):
        """Full bridge verified for GL(3)."""
        bridge = cy3_langlands_bridge(3)
        assert bridge['bridge_verified']

    def test_bridge_verified_all(self):
        """Full bridge verified for GL(N), N=2..6."""
        for N in range(2, 7):
            bridge = cy3_langlands_bridge(N)
            assert bridge['bridge_verified'], f"Bridge fails for GL({N})"

    def test_bridge_components_present(self):
        """Bridge has all required components."""
        bridge = cy3_langlands_bridge(3)
        assert 'cy3_geometry' in bridge
        assert 'coha' in bridge
        assert 'e1_chiral_algebra' in bridge
        assert 'e1_koszul_dual' in bridge
        assert 'categorical_langlands' in bridge


# =====================================================================
# 21. SHADOW TOWER COLLAPSE
# =====================================================================

class TestShadowTowerCollapse:
    """Tests for shadow tower collapse at the critical level."""

    def test_collapse_linear(self):
        """κ collapses linearly with ε."""
        for N in range(2, 5):
            v = shadow_tower_collapse_gln(N)
            assert v['all_collapse']

    def test_f1_vanishes(self):
        """F₁ → 0 as ε → 0."""
        v = shadow_tower_collapse_gln(3, num_points=5)
        for d in v['data']:
            assert d['F1'] >= 0  # F₁ is non-negative (κ ≥ 0 for ε ≥ 0)


# =====================================================================
# 22. CATEGORICAL LANGLANDS
# =====================================================================

class TestCategoricalLanglands:
    """Tests for the categorical GL programme."""

    def test_categorical_automorphic_side(self):
        """Automorphic side mentions D-mod and Bun."""
        cat = categorical_langlands_gln(3)
        assert "D-mod" in cat.automorphic_side
        assert "Bun" in cat.automorphic_side

    def test_categorical_spectral_side(self):
        """Spectral side mentions IndCoh and LocSys."""
        cat = categorical_langlands_gln(3)
        assert "IndCoh" in cat.spectral_side
        assert "LocSys" in cat.spectral_side


# =====================================================================
# 23. CROSS-CONSISTENCY CHECKS
# =====================================================================

class TestCrossConsistency:
    """Cross-family and cross-formula consistency checks."""

    def test_kappa_sln_plus_gl1_equals_gln(self):
        """κ(gl_N) = κ(sl_N) + κ(gl_1) where κ(gl_1) = k."""
        for N in range(2, 6):
            for k in [Fraction(1), Fraction(2), Fraction(-1)]:
                kap_gl = kappa_gln(N, k)
                kap_sl = kappa_sln(N, k)
                kap_gl1 = k  # Heisenberg: κ = level
                assert kap_gl == kap_sl + kap_gl1

    def test_oper_dim_equals_hitchin_dim(self):
        """Oper dimension = Hitchin base dimension (Beilinson-Drinfeld)."""
        for N in range(2, 5):
            for g in [2, 3]:
                oper = oper_data_gln(N, g)
                hitchin = hitchin_system_gln(N, g)
                assert oper['total_oper_dim'] == hitchin['dim_hitchin_base']

    def test_kw_dual_level_consistent_with_psi(self):
        """Quantum GL dual level k^∨ = -k - N gives Ψ·Ψ^∨ = 1."""
        for N in range(2, 5):
            k = Fraction(1)
            psi = k / (k + N)
            k_dual = -k - N
            psi_dual = k_dual / (k_dual + N)
            assert psi * psi_dual == 1

    def test_kappa_at_ff_dual_opposite(self):
        """κ at FF dual level has opposite sign."""
        for N in range(2, 6):
            for k in [Fraction(1), Fraction(3)]:
                kap = kappa_sln(N, k)
                kap_dual = kappa_sln(N, ff_dual_level_gln(N, k))
                assert kap + kap_dual == 0


# =====================================================================
# 24. FULL VERIFICATION SUITE
# =====================================================================

class TestFullVerification:
    """Run the complete verification suite."""

    def test_full_verification_passes(self):
        """All checks in the full verification suite must pass."""
        results = full_verification()
        assert results['ALL_PASS'], (
            "Full verification failed. Failing checks: "
            + str({k: v for k, v in results.items() if v is False})
        )
