"""Tests for the BLLPR--K3 connection engine.

Verifies the conjectural relationship between the Beem-Lemos-Liendo-
Peelaers-Rastelli (BLLPR) chiral algebra (4d N=2 Schur sector) and the
K3 Yangian (5d holomorphic CS boundary algebra).

Test organization (12 suites, 73 tests):

  1.  TestBLLPRAlgebra (9 tests): W_k(sl_2) central charge, level, properties
  2.  TestBLLPRCentralChargeFormula (8 tests): c(k) at known values
  3.  TestBLLPRVacuumCharacter (5 tests): Virasoro vacuum character coefficients
  4.  TestK3YangianData (8 tests): K3 invariants, Fock character
  5.  TestBLLPRComparison (8 tests): Central charge comparison, distinction
  6.  TestSugawaraEmbedding (6 tests): Sugawara Virasoro inside Heisenberg
  7.  TestOmegaDeformation (6 tests): Omega-background analysis
  8.  TestCharacterComparison (5 tests): Character coefficients at low order
  9.  TestCompactificationChain (5 tests): 6d -> 4d -> 2d chain
  10. TestRoute6 (4 tests): BLLPR route to G(K3 x E)
  11. TestCrossEngine (5 tests): Cross-engine consistency
  12. TestAPCompliance (4 tests): Anti-pattern checks

Ground truth:
  k = -3/2: c = -2  (A_1 class S, simplest)
  k = -1/2: c = 0   (beta-gamma system)
  k = 0:    c = -2   (coincides with k=-3/2 via level-rank duality)
  k = 1:    c = -7   (integrable)
  K3 Heisenberg: c = 24, kappa_ch = 2, kappa_fiber = 24

Manuscript references:
  chapters/examples/k3_times_e.tex:
    Section sec:k3e-five-routes (Routes 1-5, this adds Route 6)
    Remark rem:bllpr-k3-connection (new)
"""

import pytest
from sympy import Rational

from compute.lib.bllpr_k3_connection import (
    BLLPRAlgebra,
    BLLPRComparison,
    CompactificationChain,
    K3YangianData,
    bllpr_central_charge,
    bllpr_k3_pipeline,
    cross_engine_central_charge_check,
    cross_engine_fock_character_check,
    cross_engine_k3_mukai_rank_check,
    cross_engine_omega_at_self_dual,
    omega_interpolation_data,
    route_6_bllpr,
    verify_algebras_are_distinct,
    K3_MUKAI_RANK,
    K3_HOLOMORPHIC_EULER,
    K3_EULER_CHAR,
    K3_SIGMA_MODEL_C,
    SL2_H_DUAL_COXETER,
)
from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground


# =========================================================================
# 1. BLLPR algebra properties
# =========================================================================

class TestBLLPRAlgebra:
    """Test the BLLPR W_k(sl_2) algebra."""

    def test_lie_type_is_a1(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.lie_type == "A_1"

    def test_lie_algebra_is_sl2(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.lie_algebra == "sl_2"

    def test_h_dual_coxeter_is_2(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.h_dual_coxeter == 2

    def test_effective_level(self):
        """k + h^vee = k + 2."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.effective_level == Rational(1, 2)

    def test_is_w_algebra(self):
        """W_k(sl_2) = Virasoro (rank 1)."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.is_w_algebra is True

    def test_critical_level_raises(self):
        """k = -h^vee = -2 is the critical level: should raise."""
        with pytest.raises(ValueError, match="critical level"):
            BLLPRAlgebra(Rational(-2))

    def test_central_charge_at_k_minus_3_2(self):
        """k = -3/2: c = 13 - 6(1/2) - 6/(1/2) = 13 - 3 - 12 = -2."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.virasoro_central_charge == Rational(-2)

    def test_level_rank_dual_level(self):
        """Level-rank duality: k' = 1/(k+2) - 2."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k_prime = bllpr.level_rank_dual_level()
        # k+2 = 1/2, so k' = 1/(1/2) - 2 = 2 - 2 = 0
        assert k_prime == Rational(0)

    def test_level_rank_duality_preserves_c(self):
        """The Virasoro central charge is preserved under level-rank duality.

        k = -3/2: c = -2.  k' = 0: c = 13 - 12 - 3 = -2.
        """
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k_prime = bllpr.level_rank_dual_level()
        bllpr_dual = BLLPRAlgebra(k_prime)
        assert bllpr.virasoro_central_charge == bllpr_dual.virasoro_central_charge


# =========================================================================
# 2. Central charge formula
# =========================================================================

class TestBLLPRCentralChargeFormula:
    """Test c(k) = 13 - 6(k+2) - 6/(k+2) at known values."""

    def test_k_minus_3_2(self):
        """k=-3/2: c = -2."""
        assert bllpr_central_charge(Rational(-3, 2)) == Rational(-2)

    def test_k_minus_1_2(self):
        """k=-1/2: c = 0 (beta-gamma system)."""
        assert bllpr_central_charge(Rational(-1, 2)) == Rational(0)

    def test_k_0(self):
        """k=0: c = 13 - 12 - 3 = -2."""
        assert bllpr_central_charge(Rational(0)) == Rational(-2)

    def test_k_1(self):
        """k=1: c = 13 - 18 - 2 = -7."""
        assert bllpr_central_charge(Rational(1)) == Rational(-7)

    def test_k_minus_4_3(self):
        """k=-4/3: c = 13 - 4 - 9 = 0."""
        assert bllpr_central_charge(Rational(-4, 3)) == Rational(0)

    def test_k_minus_5_3(self):
        """k=-5/3: c = 13 - 6(1/3) - 6/(1/3) = 13 - 2 - 18 = -7."""
        assert bllpr_central_charge(Rational(-5, 3)) == Rational(-7)

    def test_symmetry_c_k_equals_c_k_prime(self):
        """c(k) = c(k') when (k+2)(k'+2) = 1."""
        for k in [Rational(-3, 2), Rational(-1, 2), Rational(1), Rational(-5, 3)]:
            bllpr = BLLPRAlgebra(k)
            kp = bllpr.level_rank_dual_level()
            if kp != Rational(-2):  # skip critical level
                assert bllpr_central_charge(k) == bllpr_central_charge(kp), \
                    f"c(k={k}) != c(k'={kp})"

    def test_c_is_rational(self):
        """c(k) is rational for rational k."""
        for k in [Rational(1, 3), Rational(-7, 5), Rational(2, 7)]:
            c = bllpr_central_charge(k)
            assert isinstance(c, Rational)


# =========================================================================
# 3. BLLPR vacuum character
# =========================================================================

class TestBLLPRVacuumCharacter:
    """Test Virasoro vacuum character coefficients."""

    def test_leading_coefficient_is_1(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        coeffs = bllpr.vacuum_character_coefficients(max_order=4)
        assert coeffs[0] == 1

    def test_q1_coefficient_is_0(self):
        """No states at energy 1 in the Virasoro vacuum (L_{-1}|0>=0)."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        coeffs = bllpr.vacuum_character_coefficients(max_order=4)
        assert coeffs[1] == 0

    def test_q2_coefficient_is_1(self):
        """One state at energy 2: L_{-2}|0>."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        coeffs = bllpr.vacuum_character_coefficients(max_order=4)
        assert coeffs[2] == 1

    def test_q3_coefficient_is_1(self):
        """One state at energy 3: L_{-3}|0>."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        coeffs = bllpr.vacuum_character_coefficients(max_order=4)
        assert coeffs[3] == 1

    def test_q4_coefficient_is_2(self):
        """Two states at energy 4: L_{-4}|0> and L_{-2}^2|0>."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        coeffs = bllpr.vacuum_character_coefficients(max_order=4)
        assert coeffs[4] == 2


# =========================================================================
# 4. K3 Yangian data
# =========================================================================

class TestK3YangianData:
    """Test K3 Yangian invariants."""

    def test_central_charge_is_24(self):
        k3 = K3YangianData()
        assert k3.central_charge == 24

    def test_sigma_model_c_is_6(self):
        k3 = K3YangianData()
        assert k3.sigma_model_central_charge == 6

    def test_kappa_ch_is_2(self):
        """kappa_ch(K3) = 2 = chi(O_{K3}). AP113: subscripted."""
        k3 = K3YangianData()
        assert k3.kappa_ch == 2

    def test_kappa_fiber_is_24(self):
        """kappa_fiber = chi_top(K3) = 24. AP113: subscripted."""
        k3 = K3YangianData()
        assert k3.kappa_fiber == 24

    def test_fock_character_leading(self):
        """1/eta^{24}: leading coefficient is 1."""
        k3 = K3YangianData()
        coeffs = k3.fock_character_coefficients(max_order=3)
        assert coeffs[0] == 1

    def test_fock_character_n1(self):
        """1/eta^{24}: coefficient of q^1 is 24."""
        k3 = K3YangianData()
        coeffs = k3.fock_character_coefficients(max_order=3)
        assert coeffs[1] == 24

    def test_fock_character_n2(self):
        """1/eta^{24}: coefficient of q^2 is 324."""
        k3 = K3YangianData()
        coeffs = k3.fock_character_coefficients(max_order=3)
        assert coeffs[2] == 324

    def test_fock_character_n3(self):
        """1/eta^{24}: coefficient of q^3 is 3200."""
        k3 = K3YangianData()
        coeffs = k3.fock_character_coefficients(max_order=3)
        assert coeffs[3] == 3200


# =========================================================================
# 5. BLLPR-K3 comparison
# =========================================================================

class TestBLLPRComparison:
    """Test the comparison between BLLPR and K3 Yangian."""

    def test_central_charges_are_different(self):
        """BLLPR c=-2 vs K3 c=24: different."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.central_charge_comparison()
        assert result['algebras_are_distinct'] is True

    def test_c_bllpr_is_minus_2(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.central_charge_comparison()
        assert result['c_bllpr'] == Rational(-2)

    def test_c_k3_is_24(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.central_charge_comparison()
        assert result['c_k3'] == Rational(24)

    def test_difference_is_26(self):
        """c_bllpr - c_k3 = -2 - 24 = -26."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.central_charge_comparison()
        assert result['difference'] == Rational(-26)

    def test_characters_are_different(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.character_comparison(max_order=4)
        assert result['are_equal'] is False

    def test_bllpr_character_is_smaller(self):
        """BLLPR dimensions <= K3 dimensions at each energy level."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.character_comparison(max_order=6)
        assert result['bllpr_is_much_smaller'] is True

    def test_dimension_ratio_grows(self):
        """dim_k3 / dim_bllpr grows with energy level."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        ratios = []
        for n in [2, 3, 4]:
            d = comp.dimension_comparison_at_energy(n)
            if d['ratio'] is not None:
                ratios.append(d['ratio'])
        # Ratios should be increasing
        for i in range(len(ratios) - 1):
            assert ratios[i] < ratios[i + 1], \
                f"Ratio not increasing: {ratios[i]} >= {ratios[i+1]}"

    def test_verify_algebras_distinct(self):
        result = verify_algebras_are_distinct()
        assert result['conclusion'] == 'DISTINCT_ALGEBRAIZATIONS'


# =========================================================================
# 6. Sugawara embedding
# =========================================================================

class TestSugawaraEmbedding:
    """Test the Sugawara Virasoro embedding inside K3 Heisenberg."""

    def test_sugawara_formula(self):
        """c_Sug = 24 * Psi / (Psi + 1)."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        # At Psi = 1: c_Sug = 24/2 = 12
        assert comp.sugawara_central_charge(Rational(1)) == Rational(12)

    def test_sugawara_at_psi_infinity(self):
        """As Psi -> infinity: c_Sug -> 24."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        c_large = comp.sugawara_central_charge(Rational(10000))
        # Should be close to 24
        assert abs(c_large - 24) < Rational(1, 100)

    def test_solve_for_psi(self):
        """Psi = c_bllpr / (24 - c_bllpr)."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))  # c = -2
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        psi = comp.solve_for_psi()
        # Psi = -2 / (24 - (-2)) = -2/26 = -1/13
        assert psi == Rational(-1, 13)

    def test_sugawara_roundtrip(self):
        """c_Sug(Psi) should equal c_bllpr when Psi = solve_for_psi."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        psi = comp.solve_for_psi()
        c_sug = comp.sugawara_central_charge(psi)
        assert c_sug == bllpr.virasoro_central_charge

    def test_embedding_exists(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.verify_sugawara_embedding()
        assert result['embedding_exists'] is True
        assert result['match'] is True

    def test_embedding_for_c_zero(self):
        """k=-1/2, c=0: Psi = 0/(24-0) = 0."""
        bllpr = BLLPRAlgebra(Rational(-1, 2))  # c = 0
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        psi = comp.solve_for_psi()
        assert psi == Rational(0)


# =========================================================================
# 7. Omega deformation
# =========================================================================

class TestOmegaDeformation:
    """Test Omega-background analysis."""

    def test_bllpr_does_not_depend_on_omega(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.omega_deformation_analysis()
        assert result['bllpr_depends_on_omega'] is False

    def test_yangian_depends_on_omega_at_generic(self):
        omega = OmegaBackground(Rational(1), Rational(-2))
        k3 = K3YangianData(omega)
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        comp = BLLPRComparison(bllpr, k3)
        result = comp.omega_deformation_analysis()
        assert result['yangian_depends_on_omega'] is True

    def test_yangian_degenerates_at_self_dual(self):
        omega = OmegaBackground(Rational(1), Rational(0))
        k3 = K3YangianData(omega)
        assert k3.is_self_dual is True
        assert k3.sigma3 == 0

    def test_omega_interpolation_includes_self_dual(self):
        data = omega_interpolation_data()
        has_self_dual = any(d['is_self_dual'] for d in data)
        assert has_self_dual

    def test_omega_interpolation_includes_generic(self):
        data = omega_interpolation_data(
            sigma3_values=[Rational(0), Rational(-2)],
        )
        has_generic = any(not d['is_self_dual'] for d in data)
        assert has_generic

    def test_bllpr_is_omega_independent_sector(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.omega_deformation_analysis()
        assert result['bllpr_is_omega_independent_sector'] is True


# =========================================================================
# 8. Character comparison
# =========================================================================

class TestCharacterComparison:
    """Test character coefficient comparisons."""

    def test_bllpr_vacuum_vs_k3_fock_at_n0(self):
        """Both have leading coefficient 1."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        b_coeffs = bllpr.vacuum_character_coefficients(4)
        k_coeffs = k3.fock_character_coefficients(4)
        assert b_coeffs[0] == k_coeffs[0] == 1

    def test_bllpr_dim_at_n2_is_1(self):
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        coeffs = bllpr.vacuum_character_coefficients(4)
        assert coeffs[2] == 1

    def test_k3_dim_at_n2_is_324(self):
        k3 = K3YangianData()
        coeffs = k3.fock_character_coefficients(4)
        assert coeffs[2] == 324

    def test_ratio_at_n2(self):
        """dim_k3 / dim_bllpr at n=2: 324/1 = 324."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        d = comp.dimension_comparison_at_energy(2)
        assert d['dim_bllpr'] == 1
        assert d['dim_k3'] == 324
        assert d['ratio'] == 324

    def test_schur_index_equals_vacuum_character(self):
        """Schur index = BLLPR vacuum character (BLLPR Theorem 1.1)."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        vac = bllpr.vacuum_character_coefficients(6)
        schur = bllpr.schur_index_coefficients(6)
        assert vac == schur


# =========================================================================
# 9. Compactification chain
# =========================================================================

class TestCompactificationChain:
    """Test the 6d -> 4d -> 2d compactification chain."""

    def test_6d_type(self):
        chain = CompactificationChain(genus_C=1, num_punctures=0)
        assert chain.six_d_type == "(2,0) of type A_1"

    def test_n4_sym_at_genus_1(self):
        chain = CompactificationChain(genus_C=1, num_punctures=0)
        assert "N=4 SYM" in chain.four_d_theory_type

    def test_nf4_at_genus_0_4_punctures(self):
        chain = CompactificationChain(genus_C=0, num_punctures=4)
        assert "N_f=4" in chain.four_d_theory_type

    def test_4d_anomaly_n4_sym(self):
        """N=4 SYM SU(2): a = c = 3/4."""
        chain = CompactificationChain(genus_C=1, num_punctures=0)
        assert chain.four_d_a_anomaly == Rational(3, 4)
        assert chain.four_d_c_anomaly == Rational(3, 4)

    def test_bllpr_c_from_4d_n4(self):
        """c_{2d} = -12 * c_{4d} = -12 * 3/4 = -9 for N=4 SYM."""
        chain = CompactificationChain(genus_C=1, num_punctures=0)
        assert chain.bllpr_central_charge_from_4d() == Rational(-9)


# =========================================================================
# 10. Route 6
# =========================================================================

class TestRoute6:
    """Test Route 6 (BLLPR) to G(K3 x E)."""

    def test_route_number(self):
        result = route_6_bllpr()
        assert result['route_number'] == 6

    def test_route_name(self):
        result = route_6_bllpr()
        assert result['route_name'] == 'BLLPR Schur sector'

    def test_status_is_conjectural(self):
        result = route_6_bllpr()
        assert 'CONJECTURAL' in result['status']

    def test_algebras_are_distinct(self):
        result = route_6_bllpr()
        assert result['algebras_distinct'] == 'DISTINCT_ALGEBRAIZATIONS'


# =========================================================================
# 11. Cross-engine checks
# =========================================================================

class TestCrossEngine:
    """Test cross-engine consistency."""

    def test_central_charge_consistency(self):
        assert cross_engine_central_charge_check() is True

    def test_fock_character_consistency(self):
        assert cross_engine_fock_character_check() is True

    def test_mukai_rank_consistency(self):
        assert cross_engine_k3_mukai_rank_check() is True

    def test_omega_self_dual_consistency(self):
        assert cross_engine_omega_at_self_dual() is True

    def test_full_pipeline(self):
        result = bllpr_k3_pipeline()
        assert result['cross_checks']['central_charge'] is True
        assert result['cross_checks']['fock_character'] is True
        assert result['cross_checks']['mukai_rank'] is True
        assert result['cross_checks']['omega_self_dual'] is True


# =========================================================================
# 12. AP compliance
# =========================================================================

class TestAPCompliance:
    """Test anti-pattern compliance."""

    def test_ap113_no_bare_kappa(self):
        """AP113: kappa is always subscripted in the engine.

        The K3YangianData class has kappa_ch, kappa_cat, kappa_fiber.
        No bare 'kappa' attribute.
        """
        k3 = K3YangianData()
        assert hasattr(k3, 'kappa_ch')
        assert hasattr(k3, 'kappa_cat')
        assert hasattr(k3, 'kappa_fiber')
        assert not hasattr(k3, 'kappa')

    def test_ap_cy14_status_conjectural(self):
        """AP-CY14: all results involving the K3 Yangian are conjectural."""
        from compute.lib.bllpr_k3_connection import STATUS
        assert STATUS == 'CONJECTURAL'

    def test_ap_cy7_bllpr_is_not_coha(self):
        """AP-CY7: BLLPR is a vertex algebra (chiral algebra), NOT a CoHA.

        The BLLPR algebra W_k(sl_2) is a genuine chiral algebra with OPE.
        The CoHA is associative (AP-CY7). They are different objects.
        """
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        assert bllpr.is_w_algebra is True
        # The BLLPR algebra is E_inf-chiral, NOT E_1 (which is CoHA).
        result = verify_algebras_are_distinct()
        assert result['bllpr_en_level'] == 'E_inf (vertex algebra)'

    def test_ap_cy20_omega_intermediary(self):
        """AP-CY20: the connection goes through the Omega-background,
        NOT through direct identification of parameters."""
        bllpr = BLLPRAlgebra(Rational(-3, 2))
        k3 = K3YangianData()
        comp = BLLPRComparison(bllpr, k3)
        result = comp.omega_deformation_analysis()
        assert 'Schur sector' in result['connection_mechanism']
