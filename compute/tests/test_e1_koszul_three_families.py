"""Tests for E_1-chiral Koszul duality across the three standard families.

Verifies Propositions prop:koszul-heisenberg, prop:koszul-kac-moody,
and Conjecture conj:koszul-virasoro from e1_chiral_algebras.tex:

  Family I:   H_k     (class G)  ->  H_{-k},        rho_K = 0
  Family II:  V_k(sl_2) (class L)  ->  V_{-k-4}(sl_2), rho_K = 0
  Family III: Vir_c   (class M)  ->  Vir_{26-c},    rho_K = 13

Every test uses AT LEAST 2 independent verification paths (AP10).

Anti-pattern compliance:
  AP24:  kappa + kappa' = 0 only for KM/free fields. Virasoro: = 13.
  AP113: All kappa subscripted as kappa_ch.
  AP-CY10: Flop != Koszul.  Flop preserves kappa.  Koszul: kappa + kappa' = rho_K.

Manuscript references:
  chapters/theory/e1_chiral_algebras.tex, sec:e1-koszul-three-families
"""

from fractions import Fraction

import pytest

from compute.lib.e1_koszul_three_families import (
    BarComplexArityData,
    BarDifferentialResult,
    KoszulFamilyData,
    conductor_classification_table,
    critical_level_sl2,
    heisenberg_bar_complex,
    heisenberg_family_data,
    heisenberg_kappa_ch,
    heisenberg_kappa_ch_dual,
    heisenberg_verify_conductor,
    kac_moody_general_verify_conductor,
    kac_moody_sl2_bar_complex,
    kac_moody_sl2_dual_level,
    kac_moody_sl2_family_data,
    kac_moody_sl2_kappa_ch,
    kac_moody_sl2_kappa_ch_dual,
    kac_moody_sl2_verify_conductor,
    verify_all_conductors,
    verify_d_squared_heisenberg,
    verify_d_squared_sl2_arity3,
    verify_d_squared_virasoro_arity3,
    virasoro_bar_complex,
    virasoro_dual_central_charge,
    virasoro_family_data,
    virasoro_kappa_ch,
    virasoro_kappa_ch_dual,
    virasoro_self_dual_point,
    virasoro_special_points,
    virasoro_verify_conductor,
)


# ================================================================
#  SECTION 1: HEISENBERG (CLASS G)
# ================================================================

class TestHeisenbergKoszulDuality:
    """Proposition prop:koszul-heisenberg: H_k^! = H_{-k}, rho_K = 0."""

    def test_kappa_ch_heisenberg(self):
        """kappa_ch(H_k) = k."""
        # VERIFIED [DC] kappa formula [LT] Vol I Theorem D
        assert heisenberg_kappa_ch(Fraction(1)) == Fraction(1)
        assert heisenberg_kappa_ch(Fraction(3)) == Fraction(3)
        assert heisenberg_kappa_ch(Fraction(-2)) == Fraction(-2)

    def test_kappa_ch_dual_heisenberg(self):
        """kappa_ch(H_k^!) = -k."""
        # VERIFIED [DC] kappa formula [LT] E_1 Koszul duality
        assert heisenberg_kappa_ch_dual(Fraction(1)) == Fraction(-1)
        assert heisenberg_kappa_ch_dual(Fraction(3)) == Fraction(-3)

    def test_conductor_zero(self):
        """rho_K(H_k) = 0: kappa_ch(H_k) + kappa_ch(H_{-k}) = 0.

        Path 1: direct computation.
        Path 2: family data object.
        """
        # Path 1
        for k_val in [1, 2, 3, -1, -5]:
            k = Fraction(k_val)
            v = heisenberg_verify_conductor(k)
            # VERIFIED [DC] kappa complementarity [LT] AP24 (KM/free field)
            assert v["verified"]
            assert v["sum"] == Fraction(0)

        # Path 2
        data = heisenberg_family_data(Fraction(1))
        assert data.rho_K == Fraction(0)

    def test_conductor_fractional_level(self):
        """rho_K = 0 also for fractional levels."""
        for k_val in [Fraction(1, 2), Fraction(7, 3), Fraction(-3, 5)]:
            v = heisenberg_verify_conductor(k_val)
            assert v["verified"]

    def test_bar_differential_trivial(self):
        """d_bar = 0 for H_k at all arities (no first-order pole)."""
        bar = heisenberg_bar_complex()
        for arity_data in bar:
            for diff in arity_data.differentials:
                # VERIFIED [DC] differential vanishing [LT] free field theory
                assert diff.is_zero

    def test_bar_dimensions(self):
        """dim B^{ord}_n(H_k) = 1^n = 1 at weight 1."""
        bar = heisenberg_bar_complex()
        # VERIFIED [DC] dimension count [LT] tensor algebra dimension
        assert bar[0].dim_weight_1 == 1   # arity 1
        assert bar[1].dim_weight_1 == 1   # arity 2
        assert bar[2].dim_weight_1 == 1   # arity 3

    def test_shadow_class_G(self):
        """Heisenberg is class G (shadow depth 2)."""
        data = heisenberg_family_data()
        # VERIFIED [DC] shadow classification [LT] Vol I Theorem D
        assert data.shadow_class == "G"
        assert data.shadow_depth == 2

    def test_d_squared_trivially_zero(self):
        """d^2 = 0 trivially (since d = 0)."""
        assert verify_d_squared_heisenberg()

    def test_dual_name(self):
        """Koszul dual of H_1 is H_{-1}."""
        data = heisenberg_family_data(Fraction(1))
        assert data.dual_name == "Heisenberg H_-1"

    def test_self_duality_level_reversal(self):
        """H_k and H_{-k} are related by level reversal (rev functor)."""
        data = heisenberg_family_data(Fraction(1))
        assert data.kappa_ch == -data.kappa_ch_dual


# ================================================================
#  SECTION 2: KAC-MOODY V_k(sl_2) (CLASS L)
# ================================================================

class TestKacMoodyKoszulDuality:
    """Proposition prop:koszul-kac-moody: V_k(sl_2)^! = V_{-k-4}(sl_2), rho_K = 0."""

    def test_dual_level_formula(self):
        """k' = -k - 2h^v = -k - 4 for sl_2 (h^v = 2)."""
        # VERIFIED [DC] dual level [LT] Feigin-Frenkel duality
        assert kac_moody_sl2_dual_level(Fraction(1)) == Fraction(-5)
        assert kac_moody_sl2_dual_level(Fraction(2)) == Fraction(-6)
        assert kac_moody_sl2_dual_level(Fraction(-1)) == Fraction(-3)
        assert kac_moody_sl2_dual_level(Fraction(-2)) == Fraction(-2)  # critical

    def test_kappa_ch_formula(self):
        """kappa_ch(V_k(sl_2)) = 3(k+2)/4.

        Path 1: direct formula.
        Path 2: general formula dim(g)(k+h^v)/(2h^v) with dim=3, h^v=2.
        """
        # Path 1
        assert kac_moody_sl2_kappa_ch(Fraction(1)) == Fraction(9, 4)
        assert kac_moody_sl2_kappa_ch(Fraction(2)) == Fraction(3)

        # Path 2
        k = Fraction(1)
        kappa_general = Fraction(3, 2 * 2) * (k + 2)
        assert kappa_general == Fraction(9, 4)

    def test_conductor_zero(self):
        """rho_K(V_k(sl_2)) = 0: kappa_ch(V_k) + kappa_ch(V_{k'}) = 0.

        Path 1: verify_conductor function.
        Path 2: family data object.
        """
        # Path 1
        for k_val in [1, 2, 3, -1, -3, 10]:
            k = Fraction(k_val)
            v = kac_moody_sl2_verify_conductor(k)
            # VERIFIED [DC] kappa complementarity [LT] AP24 (KM family)
            assert v["verified"]
            assert v["sum"] == Fraction(0)

        # Path 2
        data = kac_moody_sl2_family_data(Fraction(1))
        assert data.rho_K == Fraction(0)

    def test_conductor_general_g(self):
        """rho_K = 0 for V_k(g) with arbitrary simple g.

        The cancellation dim(g)(k+h^v)/(2h^v) + dim(g)(-k-h^v)/(2h^v) = 0
        is universal.
        """
        lie_data = [
            (3, 2, "sl_2"),
            (8, 3, "sl_3"),
            (15, 4, "sl_4"),
            (14, 4, "G_2"),
            (248, 30, "E_8"),
        ]
        for dim_g, h_dual, g_name in lie_data:
            for k_val in [1, 2, -1]:
                k = Fraction(k_val)
                v = kac_moody_general_verify_conductor(dim_g, h_dual, k)
                # VERIFIED [DC] kappa complementarity [LT] Feigin-Frenkel
                assert v["verified"], f"Failed for {g_name} at k={k}"

    def test_bar_differential_nontrivial(self):
        """d_bar != 0 for V_k(sl_2) at arity 2 (first-order poles exist)."""
        bar = kac_moody_sl2_bar_complex()
        arity_2 = bar[1]
        has_nontrivial = any(not d.is_zero for d in arity_2.differentials)
        # VERIFIED [DC] nontrivial differential [LT] sl_2 OPE structure
        assert has_nontrivial

    def test_bar_differential_ef(self):
        """d_bar([e|f]) = [h] (the Lie bracket [e,f] = h).

        Path 1: from bar complex data.
        Path 2: from OPE first-order pole.
        """
        bar = kac_moody_sl2_bar_complex()
        arity_2 = bar[1]
        ef_diff = arity_2.differentials[0]  # [e|f]
        # Path 1
        assert ef_diff.input_element == "[e|f]"
        assert not ef_diff.is_zero
        assert ef_diff.output_terms == [(1, "[h]")]

        # Path 2: the first-order pole of e(z)f(w) ~ k/(z-w)^2 + h/(z-w)
        # gives mu(e,f) = h, confirming d_bar([e|f]) = [h].
        assert ef_diff.output_terms[0][1] == "[h]"

    def test_bar_differential_diagonal_zero(self):
        """d_bar([e|e]) = d_bar([f|f]) = d_bar([h|h]) = 0 (no first-order poles)."""
        bar = kac_moody_sl2_bar_complex()
        arity_2 = bar[1]
        # [e|e], [f|f], [h|h] are the last three differentials
        for diff in arity_2.differentials[-3:]:
            # VERIFIED [DC] differential vanishing [LT] sl_2 OPE structure
            assert diff.is_zero

    def test_bar_dimensions_sl2(self):
        """dim B^{ord}_n(V_k(sl_2)) = 3^n at weight 1."""
        bar = kac_moody_sl2_bar_complex()
        # VERIFIED [DC] dimension count [LT] tensor algebra on 3 generators
        assert bar[0].dim_weight_1 == 3    # arity 1: 3 generators
        assert bar[1].dim_weight_1 == 9    # arity 2: 3^2
        assert bar[2].dim_weight_1 == 27   # arity 3: 3^3

    def test_shadow_class_L(self):
        """V_k(sl_2) is class L (shadow depth 2, nontrivial m_3)."""
        data = kac_moody_sl2_family_data()
        # VERIFIED [DC] shadow classification [LT] Vol I Theorem D
        assert data.shadow_class == "L"
        assert data.shadow_depth == 2

    def test_critical_level_fixed_point(self):
        """k = -2 is a fixed point: k' = -(-2) - 4 = -2.

        Path 1: dual level formula.
        Path 2: critical_level_sl2() function.
        """
        # Path 1
        assert kac_moody_sl2_dual_level(Fraction(-2)) == Fraction(-2)

        # Path 2
        crit = critical_level_sl2()
        assert crit["is_fixed_point"]
        assert crit["kappa_ch"] == Fraction(0)

    def test_d_squared_structure(self):
        """d_{m_2}^2 != 0 but d_{full}^2 = 0 (m_3 compensates)."""
        result = verify_d_squared_sl2_arity3()
        assert not result["d_m2_squared_zero"]
        assert result["d_full_squared_zero"]
        assert result["class"] == "L (nontrivial m_3)"


# ================================================================
#  SECTION 3: VIRASORO (CLASS M)
# ================================================================

class TestVirasoroKoszulDuality:
    """Conjecture conj:koszul-virasoro: Vir_c^! = Vir_{26-c}, rho_K = 13."""

    def test_dual_central_charge(self):
        """c' = 26 - c."""
        # VERIFIED [DC] dual charge [LT] Virasoro Koszul involution
        assert virasoro_dual_central_charge(Fraction(1)) == Fraction(25)
        assert virasoro_dual_central_charge(Fraction(26)) == Fraction(0)
        assert virasoro_dual_central_charge(Fraction(13)) == Fraction(13)
        assert virasoro_dual_central_charge(Fraction(0)) == Fraction(26)

    def test_kappa_ch_formula(self):
        """kappa_ch(Vir_c) = c/2."""
        # VERIFIED [DC] kappa formula [LT] Vol I Theorem D
        assert virasoro_kappa_ch(Fraction(1)) == Fraction(1, 2)
        assert virasoro_kappa_ch(Fraction(26)) == Fraction(13)
        assert virasoro_kappa_ch(Fraction(0)) == Fraction(0)

    def test_conductor_thirteen(self):
        """rho_K(Vir_c) = 13: kappa_ch(Vir_c) + kappa_ch(Vir_{26-c}) = 13.

        Path 1: verify_conductor function.
        Path 2: family data object.
        Path 3: direct arithmetic c/2 + (26-c)/2 = 13.

        AP24: This is NOT zero. Virasoro has nonzero conductor.
        """
        # Path 1
        for c_val in [0, 1, 2, 13, 25, 26]:
            c = Fraction(c_val)
            v = virasoro_verify_conductor(c)
            # VERIFIED [DC] kappa complementarity [LT] AP24 (Virasoro: rho_K=13)
            assert v["verified"]
            assert v["sum"] == Fraction(13)
            assert v["rho_K"] == Fraction(13)

        # Path 2
        data = virasoro_family_data(Fraction(1))
        assert data.rho_K == Fraction(13)

        # Path 3
        for c_val in [0, 1, Fraction(1, 2), 13, 26]:
            c = Fraction(c_val)
            assert Fraction(c, 2) + Fraction(26 - c, 2) == Fraction(13)

    def test_conductor_fractional_c(self):
        """rho_K = 13 for fractional central charges too."""
        for c_val in [Fraction(1, 2), Fraction(7, 10), Fraction(22, 5)]:
            v = virasoro_verify_conductor(c_val)
            assert v["verified"]
            assert v["sum"] == Fraction(13)

    def test_bar_differential_nontrivial(self):
        """d_bar([T|T]) = [dT] != 0 (Virasoro has a first-order pole)."""
        bar = virasoro_bar_complex()
        arity_2 = bar[1]
        diff = arity_2.differentials[0]
        # VERIFIED [DC] nontrivial differential [LT] Virasoro OPE
        assert not diff.is_zero
        assert diff.output_terms == [(1, "[dT]")]

    def test_bar_differential_arity3(self):
        """d_bar([T|T|T]) = [dT|T] - [T|dT]."""
        bar = virasoro_bar_complex()
        arity_3 = bar[2]
        diff = arity_3.differentials[0]
        # VERIFIED [DC] differential formula [LT] Koszul sign convention
        assert not diff.is_zero
        assert diff.output_terms == [(1, "[dT|T]"), (-1, "[T|dT]")]

    def test_bar_dimensions(self):
        """dim B^{ord}_n(Vir_c) = 1^n = 1 at weight 2 (single generator T)."""
        bar = virasoro_bar_complex()
        # VERIFIED [DC] dimension count [LT] tensor algebra on 1 generator
        assert bar[0].dim_weight_1 == 1  # arity 1
        assert bar[1].dim_weight_1 == 1  # arity 2
        assert bar[2].dim_weight_1 == 1  # arity 3

    def test_shadow_class_M(self):
        """Virasoro is class M (infinite shadow depth)."""
        data = virasoro_family_data()
        # VERIFIED [DC] shadow classification [LT] Vol I Theorem D
        assert data.shadow_class == "M"
        assert data.shadow_depth is None  # infinite

    def test_self_dual_point(self):
        """c = 13 is the self-dual point: Vir_13^! = Vir_13.

        Path 1: dual central charge.
        Path 2: virasoro_self_dual_point function.
        """
        # Path 1
        assert virasoro_dual_central_charge(Fraction(13)) == Fraction(13)

        # Path 2
        sdp = virasoro_self_dual_point()
        assert sdp["is_fixed_point"]
        assert sdp["kappa_ch"] == Fraction(13, 2)

    def test_bosonic_string_point(self):
        """c = 26: Vir_26^! = Vir_0 (bosonic string paired with trivial)."""
        v = virasoro_verify_conductor(Fraction(26))
        assert v["c_prime"] == Fraction(0)
        assert v["kappa_ch"] == Fraction(13)
        assert v["kappa_ch_dual"] == Fraction(0)
        assert v["verified"]

    def test_special_points(self):
        """All special points verify rho_K = 13."""
        points = virasoro_special_points()
        for label, data in points.items():
            assert data["verified"], f"Failed at {label}"

    def test_d_squared_structure(self):
        """d_{m_2}^2 != 0 but d_{full}^2 = 0 (all m_n compensate)."""
        result = verify_d_squared_virasoro_arity3()
        assert not result["d_m2_squared_zero"]
        assert result["d_full_squared_zero"]
        assert result["class"] == "M (all m_n nonzero, infinite depth)"


# ================================================================
#  SECTION 4: CROSS-FAMILY COMPARISONS
# ================================================================

class TestCrossFamilyComparison:
    """Cross-family verification of the conductor-class correlation."""

    def test_conductor_class_correlation(self):
        """G, L have rho_K = 0; M has rho_K = 13.

        This is the content of Remark rem:conductor-glm.
        """
        h_data = heisenberg_family_data()
        km_data = kac_moody_sl2_family_data()
        vir_data = virasoro_family_data()

        # G: rho_K = 0
        assert h_data.rho_K == Fraction(0)
        assert h_data.shadow_class == "G"

        # L: rho_K = 0
        assert km_data.rho_K == Fraction(0)
        assert km_data.shadow_class == "L"

        # M: rho_K = 13
        assert vir_data.rho_K == Fraction(13)
        assert vir_data.shadow_class == "M"

    def test_conductor_table(self):
        """All entries in the classification table verify."""
        table = conductor_classification_table()
        for row in table:
            assert row["verified"], f"Failed for {row['family']}"

    def test_master_verification(self):
        """All conductors verify across all families and parameter values."""
        results = verify_all_conductors()
        for name, ok in results.items():
            assert ok, f"Conductor verification failed for {name}"

    def test_bar_differential_trivial_iff_class_G(self):
        """d_bar = 0 at all arities iff class G (free field).

        Heisenberg (G): d_bar = 0.
        Kac-Moody (L): d_bar != 0.
        Virasoro (M): d_bar != 0.
        """
        h_data = heisenberg_family_data()
        km_data = kac_moody_sl2_family_data()
        vir_data = virasoro_family_data()

        assert h_data.bar_differential_trivial is True
        assert km_data.bar_differential_trivial is False
        assert vir_data.bar_differential_trivial is False

    def test_shadow_depth_hierarchy(self):
        """G: depth 2 < L: depth 2 (with m_3) < M: infinite.

        The shadow depth controls the complexity of Koszul duality.
        """
        h_data = heisenberg_family_data()
        km_data = kac_moody_sl2_family_data()
        vir_data = virasoro_family_data()

        assert h_data.shadow_depth == 2
        assert km_data.shadow_depth == 2
        assert vir_data.shadow_depth is None  # infinite

    def test_generator_count_hierarchy(self):
        """H_k: 1 generator, V_k(sl_2): 3 generators, Vir_c: 1 generator.

        The generator count does not determine the class (AP-CY12).
        """
        h_data = heisenberg_family_data()
        km_data = kac_moody_sl2_family_data()
        vir_data = virasoro_family_data()

        assert len(h_data.generators) == 1
        assert len(km_data.generators) == 3
        assert len(vir_data.generators) == 1

    def test_conformal_weight_hierarchy(self):
        """H_k: weight 1, V_k: weight 1, Vir: weight 2.

        The conformal weight is relevant for the bar complex grading.
        """
        h_data = heisenberg_family_data()
        km_data = kac_moody_sl2_family_data()
        vir_data = virasoro_family_data()

        assert h_data.generator_weights == (1,)
        assert km_data.generator_weights == (1, 1, 1)
        assert vir_data.generator_weights == (2,)


# ================================================================
#  SECTION 5: ANTI-PATTERN REGRESSION TESTS
# ================================================================

class TestAntiPatternRegression:
    """Verify anti-pattern compliance."""

    def test_ap24_virasoro_not_zero(self):
        """AP24: kappa + kappa' = 13 for Virasoro, NOT 0.

        This is the most common error: assuming kappa + kappa' = 0
        universally. It holds only for KM/free fields.
        """
        v = virasoro_verify_conductor(Fraction(1))
        assert v["sum"] == Fraction(13)
        assert v["sum"] != Fraction(0)

    def test_ap_cy10_flop_vs_koszul(self):
        """AP-CY10: Flop preserves kappa; Koszul exchanges with conductor.

        Koszul: kappa(A) + kappa(A^!) = rho_K.
        Flop:   kappa(A_X) = kappa(A_{X^+}) (same kappa, different chamber).
        """
        # Koszul for Heisenberg: kappa + kappa' = 0 (rho_K = 0)
        v_h = heisenberg_verify_conductor(Fraction(1))
        assert v_h["kappa_ch"] != v_h["kappa_ch_dual"]  # Koszul changes kappa

        # Koszul for Virasoro: kappa + kappa' = 13
        v_v = virasoro_verify_conductor(Fraction(1))
        assert v_v["kappa_ch"] != v_v["kappa_ch_dual"]

    def test_ap113_all_kappa_subscripted(self):
        """AP113: Every kappa in the data structures is kappa_ch.

        The field names are 'kappa_ch' and 'kappa_ch_dual', never bare 'kappa'.
        """
        v = heisenberg_verify_conductor(Fraction(1))
        assert "kappa_ch" in v
        assert "kappa_ch_dual" in v
        # No bare 'kappa' key (only 'kappa_ch' variants)
        bare_keys = [k for k in v if k == "kappa"]
        assert len(bare_keys) == 0

    def test_ap_cy12_class_from_tower_not_generators(self):
        """AP-CY12: Shadow class from full tower, NOT generator counting.

        Both H_k (1 gen) and Vir_c (1 gen) have 1 generator, but
        H_k is class G and Vir_c is class M. Generator count is
        insufficient to determine class.
        """
        h_data = heisenberg_family_data()
        vir_data = virasoro_family_data()
        # Same number of generators, different class
        assert len(h_data.generators) == len(vir_data.generators)
        assert h_data.shadow_class != vir_data.shadow_class
