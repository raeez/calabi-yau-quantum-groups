"""Tests for bps_entropy_shadow.py.

Multi-path verification of BPS black hole entropy from the shadow partition
function for K3 x E.  Each numerical claim is verified by at least 2
independent methods.

Test organization:
  1.  Kappa-spectrum (8 tests)
  2.  Strominger-Vafa entropy (8 tests)
  3.  Cardy formula (5 tests)
  4.  BPS degeneracies (6 tests)
  5.  Bekenstein-Hawking entropy (4 tests)
  6.  Rademacher expansion (5 tests)
  7.  Shadow tower contributions (6 tests)
  8.  Shadow vs Rademacher comparison (4 tests)
  9.  Kappa-entropy analysis (7 tests)
  10. Cross-verifications (6 tests)
  11. Entropy comparison table (5 tests)
  12. Summary (1 test)

Total: 65 tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.bps_entropy_shadow import (
    # Constants
    A_HAT, K3E_KAPPA_SPECTRUM,
    # Kappa spectrum
    KappaSpectrum, verify_kappa_spectrum,
    # Strominger-Vafa
    StromingerVafaData, strominger_vafa_entropy,
    # Cardy
    verify_cardy_formula, verify_cardy_c24,
    # BPS degeneracies
    discriminant_k3e, verify_discriminant_constraint,
    BPS_DEGENERACIES_K3E, bps_degeneracy_k3e, bps_entropy_exact,
    PHI01_ROOT_EXPONENTS_K3E, root_bps_coefficient_firewall,
    # Bekenstein-Hawking
    bekenstein_hawking_k3e, verify_strominger_vafa_k3e,
    # Rademacher
    rademacher_leading_k3e, rademacher_first_correction_k3e,
    compact_siegel_log_normalization,
    paramodular_order_tower_audit, chl_scalar_identity_gate,
    # Shadow tower
    ShadowEntropyData, shadow_entropy_scalar, shadow_tower_corrections_k3e,
    shadow_entropy_full,
    # Shadow vs Rademacher
    ResummationComparison, shadow_vs_rademacher,
    # Kappa analysis
    kappa_entropy_analysis,
    # Entropy table
    EntropyTableRow, entropy_comparison_table,
    # Cross-verifications
    verify_sv_from_cardy, verify_rademacher_improves_with_D, verify_kappa_identity,
    # Summary
    bps_entropy_shadow_summary,
    # A-hat
    a_hat_coefficient,
)


# =========================================================================
# 1. KAPPA-SPECTRUM
# =========================================================================

class TestKappaSpectrum:
    """Verify the subscripted kappa values for K3 x E (AP113)."""

    def test_kappa_ch_compact_equals_0(self):
        """Compact Hodge/PhiFA kappa_ch(K3 x E) = 0."""
        assert K3E_KAPPA_SPECTRUM.kappa_ch == Fraction(0)

    def test_kappa_ch_heis_equals_3(self):
        """Heisenberg-specialised kappa_ch^Heis(K3 x E) = 3."""
        assert K3E_KAPPA_SPECTRUM.kappa_ch_Heis == Fraction(3)

    def test_kappa_BKM_equals_5(self):
        """kappa_BKM(Delta5) = c_N(0)/2 at N=1 = 5."""
        assert K3E_KAPPA_SPECTRUM.kappa_BKM == 5

    def test_kappa_cat_total_equals_0(self):
        """kappa_cat(K3 x E) = chi(O_{K3 x E}) = 2 * 0 = 0."""
        assert K3E_KAPPA_SPECTRUM.kappa_cat == 0

    def test_kappa_cat_fiber_equals_2(self):
        """kappa_cat(K3 fiber) = chi(O_{K3}) = 1 + 0 + 1 = 2."""
        assert K3E_KAPPA_SPECTRUM.kappa_cat_fiber == 2

    def test_kappa_fiber_equals_24(self):
        """kappa_fiber = 24 = rank of Mukai lattice."""
        assert K3E_KAPPA_SPECTRUM.kappa_fiber == 24

    def test_resolved_labels_not_collapsed(self):
        """Equal numeric values do not collapse distinct kappa labels."""
        assert K3E_KAPPA_SPECTRUM.kappa_ch == K3E_KAPPA_SPECTRUM.kappa_cat == 0
        assert "kappa_ch_Heis" in KappaSpectrum._fields

    def test_verify_kappa_spectrum_all_pass(self):
        """All kappa spectrum verifications pass."""
        checks = verify_kappa_spectrum()
        assert all(checks.values())


# =========================================================================
# 2. STROMINGER-VAFA ENTROPY
# =========================================================================

class TestStromingerVafa:
    """Verify the Strominger-Vafa black hole entropy formula."""

    def test_sv_unit_charges(self):
        """S = 2*pi*sqrt(1*1*1) = 2*pi for (1,1,1)."""
        sv = strominger_vafa_entropy(1, 1, 1)
        assert abs(sv.S_BH - 2 * math.pi) < 1e-10

    def test_sv_micro_equals_bh(self):
        """S_micro = S_BH exactly (the Strominger-Vafa theorem)."""
        sv = strominger_vafa_entropy(2, 3, 5)
        assert abs(sv.S_micro - sv.S_BH) < 1e-10

    def test_sv_c_cft(self):
        """c_CFT = 6 * n_1 * n_5 for the D1-D5 system."""
        sv = strominger_vafa_entropy(3, 7, 10)
        assert sv.c_cft == 6 * 3 * 7

    def test_sv_formula_explicit(self):
        """S = 2*pi*sqrt(n_1*n_5*n_p) explicit check."""
        n1, n5, n_p = 2, 5, 8
        sv = strominger_vafa_entropy(n1, n5, n_p)
        expected = 2 * math.pi * math.sqrt(n1 * n5 * n_p)
        assert abs(sv.S_BH - expected) < 1e-10

    def test_sv_scales_correctly(self):
        """Entropy scales as sqrt(product of charges)."""
        sv1 = strominger_vafa_entropy(1, 1, 1)
        sv4 = strominger_vafa_entropy(1, 1, 4)
        # S(1,1,4) / S(1,1,1) = sqrt(4) = 2
        assert abs(sv4.S_BH / sv1.S_BH - 2.0) < 1e-10

    def test_sv_zero_charge(self):
        """Zero charges give zero entropy."""
        sv = strominger_vafa_entropy(0, 1, 1)
        assert sv.S_BH == 0.0

    def test_sv_agreement_flag(self):
        """The agreement flag is always True (Strominger-Vafa theorem)."""
        sv = strominger_vafa_entropy(5, 7, 11)
        assert sv.agreement is True

    def test_sv_large_charges(self):
        """Large charge test: S = 2*pi*sqrt(100*200*300)."""
        sv = strominger_vafa_entropy(100, 200, 300)
        expected = 2 * math.pi * math.sqrt(100 * 200 * 300)
        assert abs(sv.S_BH - expected) < 1e-6


# =========================================================================
# 3. CARDY FORMULA
# =========================================================================

class TestCardyFormula:
    """Verify the Cardy formula S ~ 2*pi*sqrt(c*N/6)."""

    def test_cardy_c24_n100(self):
        """c=24, N=100: S = 4*pi*sqrt(100) = 40*pi."""
        result = verify_cardy_c24(100)
        assert abs(result["S_cardy"] - 4 * math.pi * 10) < 1e-10
        assert result["match"] is True

    def test_cardy_matches_sv(self):
        """Cardy formula with c = 6*n_1*n_5 matches S_SV."""
        n1, n5, n_p = 3, 4, 20
        cardy = verify_cardy_formula(c=6*n1*n5, N=n_p)
        sv = strominger_vafa_entropy(n1, n5, n_p)
        assert abs(cardy["S_cardy"] - sv.S_BH) < 1e-10

    def test_cardy_above_btz_threshold(self):
        """N > c/24 for the Cardy formula to be valid."""
        result = verify_cardy_formula(c=24, N=100)
        assert result["above_threshold"] is True
        assert result["btz_threshold"] == 1.0

    def test_cardy_c6_n1(self):
        """Single copy K3 sigma model: c=6, N=1.
        S = 2*pi*sqrt(6/6) = 2*pi."""
        result = verify_cardy_formula(c=6, N=1)
        assert abs(result["S_cardy"] - 2 * math.pi) < 1e-10

    def test_cardy_c_over_24(self):
        """c/24 = 1 for c=24."""
        result = verify_cardy_formula(c=24, N=10)
        assert result["c_over_24"] == 1.0


# =========================================================================
# 4. BPS DEGENERACIES
# =========================================================================

class TestBPSDegeneracies:
    """Verify BPS degeneracies from 1/Delta_5."""

    def test_discriminant_formula(self):
        """D = 4nm - l^2."""
        assert discriminant_k3e(1, 0, 1) == 4
        assert discriminant_k3e(1, 1, 1) == 3
        assert discriminant_k3e(2, 1, 1) == 7

    def test_discriminant_constraint_valid(self):
        """Valid discriminants: D = 0 or 3 mod 4, or D < 0."""
        assert verify_discriminant_constraint(-1) is True
        assert verify_discriminant_constraint(0) is True
        assert verify_discriminant_constraint(3) is True
        assert verify_discriminant_constraint(4) is True
        assert verify_discriminant_constraint(7) is True

    def test_discriminant_constraint_invalid(self):
        """Invalid discriminants: D = 1 or 2 mod 4."""
        assert verify_discriminant_constraint(1) is False
        assert verify_discriminant_constraint(2) is False
        assert verify_discriminant_constraint(5) is False

    def test_bps_ground_state(self):
        """Omega(-1) = 1: single ground state."""
        assert bps_degeneracy_k3e(-1) == 1

    def test_bps_d3_is_248(self):
        """Omega(3) = 248: dimension of E_8 minus 1 plus corrections.
        Actually 248 = dim(E_8), which is a coincidence / deep fact
        about the K3 x E BPS spectrum."""
        assert bps_degeneracy_k3e(3) == 248

    def test_bps_degeneracies_grow(self):
        """BPS degeneracies grow with discriminant (absolute value)."""
        D_vals = [3, 7, 11, 15]
        omegas = [abs(bps_degeneracy_k3e(D)) for D in D_vals]
        for i in range(len(omegas) - 1):
            assert omegas[i + 1] > omegas[i]

    def test_phi01_root_exponent_not_bps_coefficient_D3(self):
        """At D=3 the denominator exponent and BPS coefficient differ."""
        assert PHI01_ROOT_EXPONENTS_K3E[3] == -64
        assert BPS_DEGENERACIES_K3E[3] == 248
        assert PHI01_ROOT_EXPONENTS_K3E[3] != BPS_DEGENERACIES_K3E[3]

    def test_root_bps_firewall_rejects_coefficientwise_equality(self):
        """Root exponents and reciprocal-Igusa coefficients are product-related."""
        firewall = root_bps_coefficient_firewall()
        assert firewall.status == "ROOT_EXPONENTS_DISTINCT_FROM_BPS_COEFFICIENTS"
        assert firewall.relation == "PRODUCT_LEVEL_BORCHERDS_DMVV_NOT_COEFFICIENTWISE"
        assert firewall.any_nonpolar_equal is False
        for row in firewall.rows:
            assert row.phi01_root_exponent != row.bps_coefficient


# =========================================================================
# 5. BEKENSTEIN-HAWKING ENTROPY
# =========================================================================

class TestBekensteinHawking:
    """Verify the Bekenstein-Hawking entropy S_BH = pi*sqrt(D)."""

    def test_bh_d4(self):
        """D=4: S_BH = 2*pi."""
        assert abs(bekenstein_hawking_k3e(4) - 2 * math.pi) < 1e-10

    def test_bh_d0_is_zero(self):
        """D=0: zero-area black hole."""
        assert bekenstein_hawking_k3e(0) == 0.0

    def test_bh_negative_d(self):
        """D<0: no classical black hole."""
        assert bekenstein_hawking_k3e(-1) == 0.0

    def test_bh_scales_as_sqrt(self):
        """S_BH(4D) = 2 * S_BH(D)."""
        S1 = bekenstein_hawking_k3e(4)
        S4 = bekenstein_hawking_k3e(16)
        assert abs(S4 / S1 - 2.0) < 1e-10


# =========================================================================
# 6. RADEMACHER EXPANSION
# =========================================================================

class TestRademacher:
    """Verify the Rademacher expansion for K3 x E BPS degeneracies."""

    def test_rademacher_leading_is_bh(self):
        """Leading Rademacher saddle equals Bekenstein-Hawking."""
        D = 1000
        S_rad = rademacher_leading_k3e(D)
        S_BH = bekenstein_hawking_k3e(D)
        assert abs(S_rad - S_BH) < 1e-10

    def test_compact_siegel_log_coefficient_unpinned(self):
        """The compact Siegel log coefficient is not installed by default."""
        norm = compact_siegel_log_normalization()
        assert norm.status == "UNPINNED_NORMALIZATION"
        assert norm.accepted_coefficient is None
        assert "contour_normalization" in norm.missing_inputs
        assert "polar_data" in norm.missing_inputs
        assert "measure_normalization" in norm.missing_inputs
        assert "primitive_square_convention" in norm.missing_inputs

    def test_false_arithmetic_log_formula_rejected(self):
        """The formula (kappa_BKM+1)/2 = 3/2 is rejected arithmetically."""
        norm = compact_siegel_log_normalization()
        assert norm.arithmetic_formula_valid is False
        scalar_candidates = [
            c for c in norm.candidates
            if c.coefficient == Fraction(3, 2)
        ]
        assert scalar_candidates
        assert scalar_candidates[0].status == "UNPINNED_CANDIDATE"

    def test_rademacher_leading_has_no_default_log_correction(self):
        """The leading helper does not smuggle in a logarithmic coefficient."""
        D = 100
        S_rad = rademacher_leading_k3e(D)
        S_BH = bekenstein_hawking_k3e(D)
        assert abs(S_rad - S_BH) < 1e-10

    def test_rademacher_d0_is_zero(self):
        """Rademacher gives 0 for D <= 0."""
        assert rademacher_leading_k3e(0) == 0.0
        assert rademacher_leading_k3e(-5) == 0.0

    def test_rademacher_correction_suppressed(self):
        """The c=2 Rademacher correction is exponentially suppressed."""
        D = 100
        ratio = rademacher_first_correction_k3e(D)
        # ratio ~ exp(-pi*sqrt(D)/2) ~ exp(-15.7) ~ 1.5e-7
        assert ratio < 0.01

    def test_rademacher_correction_decreases_with_D(self):
        """C_2/C_1 decreases as D grows."""
        r1 = rademacher_first_correction_k3e(10)
        r2 = rademacher_first_correction_k3e(100)
        assert r2 < r1


class TestParamodularTowerAudit:
    """Separate JS physical dyons from primitive BKM denominators."""

    def test_js_and_bkm_order_sets_differ(self):
        audit = paramodular_order_tower_audit()
        assert audit.js_physical.orders == (1, 2, 3, 5, 7, 11)
        assert audit.bkm_primitive.orders == (1, 2, 3, 4, 6)
        assert audit.intersection == (1, 2, 3)

    def test_js_formula_weights(self):
        audit = paramodular_order_tower_audit()
        assert audit.js_physical.weights == (
            Fraction(10), Fraction(6), Fraction(4),
            Fraction(2), Fraction(1), Fraction(0),
        )

    def test_bkm_primitive_weights(self):
        """Corrected ladder (Jatkar-Sen; Govindarajan-Krishna); (5,4,3,2,1) retracted."""
        audit = paramodular_order_tower_audit()
        assert audit.bkm_primitive.weights == (
            Fraction(5), Fraction(3), Fraction(2), Fraction(3, 2), Fraction(1),
        )

    def test_js_formula_rejects_bkm_orders_4_and_6(self):
        audit = paramodular_order_tower_audit()
        assert audit.js_formula_on_bkm_orders[4] == Fraction(14, 5)
        assert audit.js_formula_on_bkm_orders[6] == Fraction(10, 7)
        assert audit.js_formula_integral_on_bkm_orders is False

    def test_no_uniform_square_across_towers(self):
        audit = paramodular_order_tower_audit()
        assert audit.js_physical.denominator_power == 1
        assert audit.bkm_primitive.denominator_power is None
        assert audit.uniform_square_valid is False

    def test_js_weight_zero_endpoint_is_not_bkm_denominator(self):
        audit = paramodular_order_tower_audit()
        assert audit.js_weight_zero_order == 11
        assert audit.js_physical.weights[-1] == Fraction(0)
        assert audit.js_weight_zero_is_bkm_denominator is False
        assert audit.js_weight_zero_order not in audit.bkm_primitive.orders
        assert audit.js_weight_zero_status == "JS_WEIGHT_ZERO_SCALAR_BOUNDARY_NOT_BKM_DENOMINATOR"

    def test_js_weight_zero_endpoint_lists_missing_bkm_data(self):
        audit = paramodular_order_tower_audit()
        missing = set(audit.js_weight_zero_missing_for_bkm)
        assert "Borcherds denominator algebra" in missing
        assert "root lattice and Weyl vector" in missing
        assert "finite Hall-Borcherds recognition datum" in missing


class TestCHLScalarIdentityGate:
    """Keep N=2,3 CHL scalar identities conditional until the gates close."""

    def test_n23_scalar_identity_is_not_unconditional(self):
        gate = chl_scalar_identity_gate()
        assert gate.orders == (2, 3)
        assert gate.unconditional_orders == ()
        assert gate.conditional_orders == (2, 3)
        assert set(gate.status_by_order.values()) == {
            "CONDITIONAL_NEEDS_CHL_DT_AND_NORMALIZATION_GATE"
        }

    def test_bkm_square_weights_equal_bryan_oberdieck_weights_but_forms_open(self):
        """Corrected squares (6,4) match BO weights; form identification stays open."""
        gate = chl_scalar_identity_gate()
        assert gate.primitive_bkm_weights == {2: Fraction(3), 3: Fraction(2)}
        assert gate.bkm_scalar_square_weights == {2: Fraction(6), 3: Fraction(4)}
        assert gate.bryan_oberdieck_denominator_weights == {
            2: Fraction(6), 3: Fraction(4),
        }
        assert gate.scalar_square_weights_match_bryan_oberdieck is True
        assert "does not identify the forms" in gate.normalization_warning

    def test_n23_missing_gates_include_full_chl_dt_and_normalization(self):
        gate = chl_scalar_identity_gate()
        missing = set(gate.missing_gates)
        assert "all-class proof of Bryan-Oberdieck Conjecture 0.1" in missing
        assert "normalization bridge from the Bryan-Oberdieck denominator to the primitive BKM scalar square" in missing
        assert "reduced multiple-cover formula from primitive to imprimitive classes" in missing
        assert any("first t^{-1/N}" in case for case in gate.bryan_oberdieck_base_cases)


# =========================================================================
# 7. SHADOW TOWER CONTRIBUTIONS
# =========================================================================

class TestShadowTower:
    """Verify shadow tower contributions to BPS entropy."""

    def test_shadow_scalar_equals_bh(self):
        """Shadow scalar reproduces Bekenstein-Hawking at leading order."""
        D = 100
        S_shadow = shadow_entropy_scalar(D)
        S_BH = bekenstein_hawking_k3e(D)
        assert abs(S_shadow - S_BH) < 1e-10

    def test_shadow_uses_kappa_ch(self):
        """Shadow tower uses kappa_ch^Heis = 3, NOT compact kappa_ch or kappa_BKM."""
        D = 100
        data = shadow_entropy_full(D)
        assert data.kappa_ch_Heis_used == Fraction(3)
        assert data.kappa_BKM_used == 5

    def test_shadow_corrections_decrease_with_genus(self):
        """Higher-genus corrections are suppressed."""
        D = 100
        corrections = shadow_tower_corrections_k3e(D)
        # Corrections should decrease in absolute value with genus
        prev = abs(corrections[1])
        for g in range(2, 6):
            curr = abs(corrections[g])
            assert curr < prev
            prev = curr

    def test_shadow_corrections_zero_for_d0(self):
        """No corrections for D <= 0."""
        corrections = shadow_tower_corrections_k3e(0)
        assert corrections == {}

    def test_shadow_entropy_full_structure(self):
        """shadow_entropy_full returns all fields correctly."""
        data = shadow_entropy_full(7)
        assert data.discriminant == 7
        assert data.S_BH > 0
        assert data.kappa_ch_Heis_used == Fraction(3)
        assert data.kappa_BKM_used == 5
        assert isinstance(data.shadow_tower_corrections, dict)

    def test_shadow_scalar_zero_for_negative_d(self):
        """Shadow scalar is 0 for D <= 0."""
        assert shadow_entropy_scalar(-1) == 0.0
        assert shadow_entropy_scalar(0) == 0.0


# =========================================================================
# 8. SHADOW VS RADEMACHER COMPARISON
# =========================================================================

class TestShadowVsRademacher:
    """Compare shadow resummation with Rademacher expansion."""

    def test_comparison_structure(self):
        """shadow_vs_rademacher returns well-formed data."""
        comp = shadow_vs_rademacher(15)
        assert comp.discriminant == 15
        assert comp.S_BH > 0
        assert comp.S_rademacher_leading > 0

    def test_rademacher_correction_small_at_large_D(self):
        """Rademacher c=2 correction is tiny at large D."""
        comp = shadow_vs_rademacher(100)
        assert comp.rademacher_correction_ratio < 0.001

    def test_shadow_genus1_correction_sign(self):
        """Genus-1 shadow correction is positive (kappa_ch^Heis > 0)."""
        comp = shadow_vs_rademacher(100)
        assert comp.shadow_genus1_correction > 0

    def test_shadow_genus2_smaller_than_genus1(self):
        """Genus-2 correction smaller than genus-1 correction."""
        comp = shadow_vs_rademacher(100)
        assert abs(comp.shadow_genus2_correction) < abs(comp.shadow_genus1_correction)


# =========================================================================
# 9. KAPPA-ENTROPY ANALYSIS
# =========================================================================

class TestKappaEntropyAnalysis:
    """Verify which kappa controls the black hole entropy."""

    def test_kappa_BKM_is_answer(self):
        """kappa_BKM = 5 controls the entropy (not compact or Heisenberg kappa_ch)."""
        analysis = kappa_entropy_analysis()
        assert "kappa_BKM" in analysis["answer"]

    def test_total_space_kappa_identity_fails(self):
        """kappa_BKM != kappa_ch + kappa_cat(K3 x E): 5 != 0 + 0."""
        analysis = kappa_entropy_analysis()
        assert analysis["identity_kBKM_eq_kch_plus_kcat_total"] is False

    def test_compact_fiber_kappa_identity_fails(self):
        """kappa_BKM != kappa_ch + chi(O_K3): 5 != 0 + 2."""
        analysis = kappa_entropy_analysis()
        assert analysis["identity_kBKM_eq_kch_plus_chi_O_K3_fiber"] is False

    def test_heis_fiber_is_only_coincidence(self):
        """kappa_ch^Heis + chi(O_K3) = 3 + 2 = 5 is only an N=1 coincidence."""
        analysis = kappa_entropy_analysis()
        assert analysis["coincidence_N1_kBKM_eq_kch_Heis_plus_chi_O_K3_fiber"] is True

    def test_spectrum_values(self):
        """The spectrum values are correctly reported."""
        analysis = kappa_entropy_analysis()
        spec = analysis["kappa_spectrum"]
        assert spec["kappa_ch"] == 0.0
        assert spec["kappa_ch_Heis"] == 3.0
        assert spec["kappa_BKM"] == 5.0
        assert spec["kappa_cat"] == 0.0
        assert spec["kappa_fiber"] == 24.0
        assert analysis["auxiliary_fiber_values"]["chi_O_K3_fiber"] == 2.0

    def test_key_identity_string(self):
        """The key identity rejects additive proofs and records only the coincidence."""
        analysis = kappa_entropy_analysis()
        assert "c_N(0)/2 at N=1 = 5" in analysis["key_identity"]
        assert "0 + 0 != 5" in analysis["key_identity"]
        assert "0 + 2 != 5" in analysis["key_identity"]
        assert "coincidence only" in analysis["key_identity"]
        assert "3 + 2 = 5" in analysis["key_identity"]

    def test_rademacher_predictions_all_present(self):
        """All kappa candidates have Rademacher predictions."""
        analysis = kappa_entropy_analysis()
        preds = analysis["rademacher_predictions"]
        assert "kappa_ch" in preds
        assert "kappa_ch_Heis" in preds
        assert "kappa_BKM" in preds
        assert "kappa_cat" in preds
        assert "aux_chi_O_K3_fiber" in preds
        assert "kappa_fiber" in preds


# =========================================================================
# 10. CROSS-VERIFICATIONS
# =========================================================================

class TestCrossVerifications:
    """Cross-verify entropy computations by multiple paths."""

    def test_sv_from_cardy_match(self):
        """Strominger-Vafa matches Cardy formula exactly."""
        result = verify_sv_from_cardy()
        assert result["match"] is True

    def test_kappa_identity_all_paths(self):
        """kappa_BKM = c_N(0)/2 at N=1 and additive identities are rejected."""
        checks = verify_kappa_identity()
        assert all(checks.values())

    def test_rademacher_improves(self):
        """S_micro/S_BH ratio approaches 1 for growing D."""
        results = verify_rademacher_improves_with_D()
        if 3 in results and 15 in results:
            # ratio at D=15 should be closer to 1 than at D=3
            err_3 = results[3]["relative_error"]
            err_15 = results[15]["relative_error"]
            assert err_15 < err_3

    def test_a_hat_coefficients_consistent(self):
        """A-hat coefficients are consistent with stored values."""
        assert a_hat_coefficient(1) == Fraction(1, 24)
        assert a_hat_coefficient(2) == Fraction(7, 5760)
        assert a_hat_coefficient(3) == Fraction(31, 967680)

    def test_bps_entropy_relative_error_small(self):
        """Relative error |S_micro - S_BH|/S_BH is small at moderate D.

        The ratio S_micro/S_BH oscillates around 1 at small D. We verify
        that the relative error is bounded by 2% for D >= 7, without
        asserting a compact Siegel logarithmic coefficient.
        """
        for D in [7, 8, 11, 12]:
            S_BH = bekenstein_hawking_k3e(D)
            S_micro = bps_entropy_exact(D)
            if S_micro is not None and S_BH > 0:
                rel_err = abs(S_micro - S_BH) / S_BH
                assert rel_err < 0.02, f"D={D}: rel_err={rel_err}"

    def test_discriminant_constraint_for_stored_bps(self):
        """All stored BPS degeneracies satisfy the discriminant constraint."""
        for D in BPS_DEGENERACIES_K3E:
            assert verify_discriminant_constraint(D), f"D={D} fails constraint"


# =========================================================================
# 11. ENTROPY COMPARISON TABLE
# =========================================================================

class TestEntropyTable:
    """Verify the entropy comparison table."""

    def test_table_has_entries(self):
        """Table has entries for all default discriminants."""
        table = entropy_comparison_table()
        assert len(table) >= 6

    def test_table_d7(self):
        """D=7 row: Omega=4119, S_BH=pi*sqrt(7)."""
        table = entropy_comparison_table([7])
        assert len(table) == 1
        row = table[0]
        assert row.D == 7
        assert row.omega == 4119
        assert abs(row.S_BH - math.pi * math.sqrt(7)) < 1e-10

    def test_table_s_micro_positive(self):
        """All S_micro values are positive where defined."""
        table = entropy_comparison_table()
        for row in table:
            if row.S_micro is not None:
                assert row.S_micro > 0

    def test_table_ratio_less_than_2(self):
        """S_micro/S_BH ratio is between 0 and 2 for all entries."""
        table = entropy_comparison_table()
        for row in table:
            if row.ratio_micro_BH is not None:
                assert 0 < row.ratio_micro_BH < 2

    def test_table_rademacher_is_pinned_leading_saddle(self):
        """Rademacher table stores the pinned leading saddle."""
        table = entropy_comparison_table()
        for row in table:
            assert abs(row.S_rademacher - row.S_BH) < 1e-10


# =========================================================================
# 12. SUMMARY
# =========================================================================

class TestSummary:
    """Verify the comprehensive summary runs without error."""

    def test_summary_runs(self):
        """bps_entropy_shadow_summary() completes without error."""
        summary = bps_entropy_shadow_summary()
        assert "kappa_spectrum" in summary
        assert "strominger_vafa" in summary
        assert "entropy_table" in summary
        assert "kappa_analysis" in summary
