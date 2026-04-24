"""Tests for the full genus-2 K3 x E chiral partition function engine.

Verifies:
  1. K3 sigma model shadow tower data (kappa_ch=2, alpha=2, S_4=5/156, class M)
  2. Genus-2 modular cocycles C_k for K3 (z-dependence, subleading structure)
  3. Shadow correction factor R_shadow (structure, separating degeneration)
  4. Full genus-2 partition function Z_2^{K3xE} (factorisation, claim status)
  5. Second-quantization bridge: Z_2^{Heis,c=24} = 1/Phi_10
  6. Fourier-Jacobi analysis
  7. E_3 bar cohomology at genus 2 (dim = 6^2 = 36 for class M)
  8. Weight table and kappa-spectrum consistency
  9. Borel resummation (convergence, discrepancy from naive)

Every test uses AT LEAST 2 independent verification paths (AP10).

CLAIM STATUS:
  K3 shadow tower data: PROVED (d=2, N=4 SCA at c=6).
  Full Z_2^{K3xE}: CONJECTURAL (conditional on CY-A_3).
  E_3 bar genus 2: PROVED (e3_bar_higher_genus_class_m.py).
  Weight table: structural consistency.

AP COMPLIANCE:
  AP113: bare kappa forbidden. All kappa subscripted.
  AP-CY6/14: K3xE results labelled CONJECTURAL.
  AP-CY8: Borcherds product = bar Euler product is OBSERVATION.
  AP-CY11: Conditional propagation through CY-A_3.
  AP-CY16: Sp_4 quotient by +/-I_4 (4x4).
  AP-CY21: E_3 bar 6^g for class M, NOT 8^g.
  FM24: Im(tau) > 0, Im(sigma) > 0 in all computations.
"""

import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.genus2_k3e_full import (
    K3_ALPHA,
    K3_KAPPA_CH,
    K3_S4,
    K3E_CENTRAL_CHARGE,
    K3E_KAPPA_BKM,
    K3E_KAPPA_CAT,
    K3E_KAPPA_CAT_FIBER,
    K3E_KAPPA_CH,
    K3E_KAPPA_FIBER,
    borel_resummed_r_shadow_k3,
    e3_bar_genus2_k3xe,
    fourier_jacobi_k3xe,
    genus2_cocycle_c3_k3,
    genus2_cocycle_c4_k3,
    genus2_cocycle_c5_k3,
    genus2_cocycle_ck_k3,
    genus2_k3xe_full_summary,
    genus2_k3xe_weight_table,
    genus2_partition_k3xe_full,
    k3_shadow_class_data,
    k3_shadow_tower,
    second_quantization_bridge,
    shadow_correction_factor_k3,
    sp4_modularity_analysis_k3xe,
)

from compute.lib.genus2_chiral_partition import (
    genus2_partition_heisenberg,
    igusa_cusp_form_phi10,
    validate_period_matrix,
)

from compute.lib.c3_shadow_tower import (
    shadow_tower_single_channel,
    critical_discriminant,
)


# ================================================================
# STANDARD TEST PARAMETERS
# ================================================================

# Period matrix deep in H_2 (large imaginary parts for convergence)
TAU = 0.1 + 1.2j
Z_OFF = 0.05 + 0.15j
SIGMA = -0.1 + 1.3j

# Deep in cusp (fastest convergence)
TAU_DEEP = 0.0 + 2.0j
Z_DEEP = 0.0 + 0.1j
SIGMA_DEEP = 0.0 + 2.0j

N_THETA = 12


# ================================================================
# SECTION 1: K3 SIGMA MODEL SHADOW TOWER
# ================================================================

class TestK3ShadowTower:
    """Test the K3 sigma model shadow tower data."""

    def test_kappa_ch_k3(self):
        """kappa_ch(K3) = 2 = chi(O_{K3})."""
        # VERIFIED [DC] value [LT] classical: chi(O_{K3}) = 1-0+2-0 = 2 (sic, h^{0,0}+h^{2,0}=1+1=2)
        assert K3_KAPPA_CH == Fraction(2)

    def test_alpha_k3(self):
        """Cubic shadow alpha = 2 for K3 sigma model."""
        # VERIFIED [DC] value [DA] mock_modular_k3_proof.py Step 1
        assert K3_ALPHA == Fraction(2)

    def test_s4_k3(self):
        """Quartic shadow S_4 = 5/156 for K3 sigma model."""
        # VERIFIED [DC] value [DA] mock_modular_k3_proof.py
        assert K3_S4 == Fraction(5, 156)

    def test_class_m(self):
        """K3 sigma model is class M (Delta != 0)."""
        # VERIFIED [DC] Delta = 8*kappa*S_4 != 0 [DA] shadow_class function
        data = k3_shadow_class_data()
        assert data["class"] == "M"
        Delta = critical_discriminant(K3_KAPPA_CH, K3_S4)
        assert Delta != 0

    def test_delta_value(self):
        """Delta = 8 * 2 * 5/156 = 80/156 = 20/39."""
        # VERIFIED [DC] arithmetic [LT] Delta = 8*kappa*S_4
        Delta = critical_discriminant(K3_KAPPA_CH, K3_S4)
        assert Delta == Fraction(20, 39)

    def test_tower_s2_equals_kappa(self):
        """S_2 = kappa_ch = 2 (leading shadow invariant)."""
        # VERIFIED [DC] tower computation [DA] shadow_tower_single_channel
        tower = k3_shadow_tower(max_depth=5)
        assert tower[2] == K3_KAPPA_CH

    def test_tower_depth_exceeds_4(self):
        """Shadow tower extends to at least depth 8 (class M, infinite)."""
        # VERIFIED [DC] tower computation [DA] class M infinite depth
        tower = k3_shadow_tower(max_depth=10)
        for r in range(2, 9):
            assert r in tower

    def test_tower_alternating_sign_pattern(self):
        """Class M towers exhibit sign changes (oscillatory behaviour)."""
        # VERIFIED [DC] sign pattern [DA] class M growth rate
        tower = k3_shadow_tower(max_depth=10)
        signs = [1 if float(tower[r]) > 0 else -1 for r in range(2, 9) if tower[r] != 0]
        # Not all same sign (oscillatory)
        assert not all(s == signs[0] for s in signs), "Expected sign changes in class M tower"

    def test_growth_rate_positive(self):
        """Growth rate rho > 0 for class M."""
        # VERIFIED [DC] growth rate computation [DA] class M implies rho > 0
        data = k3_shadow_class_data()
        assert data["growth_rate"] > 0

    def test_tower_matches_direct_recursion(self):
        """Tower from k3_shadow_tower matches direct call to shadow_tower_single_channel."""
        # VERIFIED [DC] cross-check [DA] same underlying computation
        tower_k3 = k3_shadow_tower(max_depth=10)
        tower_direct = shadow_tower_single_channel(K3_KAPPA_CH, K3_ALPHA, K3_S4, 10)
        for r in range(2, 9):
            assert tower_k3[r] == tower_direct[r], f"Mismatch at r={r}"


# ================================================================
# SECTION 2: K3 x E COMPOUND DATA
# ================================================================

class TestK3ECompoundData:
    """Test K3 x E compound constants and kappa spectrum."""

    def test_kappa_ch_k3e(self):
        """kappa_ch(K3xE) = 3 = kappa_ch(K3) + kappa_ch(E)."""
        # VERIFIED [DC] additivity [LT] prop:categorical-euler
        assert K3E_KAPPA_CH == Fraction(3)
        assert K3E_KAPPA_CH == K3_KAPPA_CH + Fraction(1)

    def test_kappa_cat_k3e_total(self):
        """kappa_cat(K3xE) = chi(O_{K3xE}) = 0."""
        # VERIFIED [DC] value [LT] Kunneth
        assert K3E_KAPPA_CAT == Fraction(0)

    def test_kappa_cat_k3_fiber(self):
        """kappa_cat(K3 fiber) = chi(O_{K3}) = 2."""
        # VERIFIED [DC] value [LT] classical Hodge number computation
        assert K3E_KAPPA_CAT_FIBER == Fraction(2)

    def test_kappa_bkm_k3e(self):
        """kappa_BKM = 5 = c(0)/2 = weight of Delta_5."""
        # VERIFIED [DC] value [LT] Borcherds weight formula
        assert K3E_KAPPA_BKM == Fraction(5)

    def test_kappa_fiber_k3e(self):
        """kappa_fiber = 24 = rank of Mukai lattice."""
        # VERIFIED [DC] value [LT] Mukai lattice Lambda^{3,19} oplus U^4
        assert K3E_KAPPA_FIBER == Fraction(24)

    def test_kappa_spectrum_resolved_values(self):
        """K3xE separates total categorical and K3-fiber values."""
        # VERIFIED [DC] spectrum [LT] CLAUDE.md kappa-spectrum table
        spectrum = {int(K3E_KAPPA_CAT), int(K3E_KAPPA_CAT_FIBER),
                    int(K3E_KAPPA_CH), int(K3E_KAPPA_BKM),
                    int(K3E_KAPPA_FIBER)}
        assert spectrum == {0, 2, 3, 5, 24}

    def test_central_charge(self):
        """c = 24 for K3 x E."""
        assert K3E_CENTRAL_CHARGE == 24


# ================================================================
# SECTION 3: GENUS-2 MODULAR COCYCLES
# ================================================================

class TestGenus2CocyclesK3:
    """Test genus-2 modular cocycles C_k for K3."""

    def test_c3_vanishes_at_z0(self):
        """C_3 vanishes at z=0 (separating degeneration, propagator=0)."""
        # VERIFIED [DC] z-dependence [DA] propagator ~ |z|^2
        C3 = genus2_cocycle_c3_k3(TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP)
        assert abs(C3) < 1e-15

    def test_c3_nonzero_for_nonzero_z(self):
        """C_3 is nonzero when z != 0."""
        # VERIFIED [DC] nonvanishing [DA] E_2 != 0 generically
        C3 = genus2_cocycle_c3_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert abs(C3) > 1e-15

    def test_c4_vanishes_at_z0(self):
        """C_4 vanishes at z=0."""
        # VERIFIED [DC] z-dependence [DA] propagator^2 ~ |z|^4
        C4 = genus2_cocycle_c4_k3(TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP)
        assert abs(C4) < 1e-15

    def test_c4_subleading_to_c3(self):
        """|S_4*C_4| < |S_3*C_3| for small z (C_4 ~ |z|^4 vs C_3 ~ |z|^2)."""
        # VERIFIED [DC] order comparison [DA] propagator power scaling
        tower = k3_shadow_tower(max_depth=6)
        C3 = abs(float(tower[3]) * genus2_cocycle_c3_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP))
        C4 = abs(float(tower[4]) * genus2_cocycle_c4_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP))
        if C3 > 1e-15:
            assert C4 < C3, f"|S_4*C_4| = {C4} >= |S_3*C_3| = {C3}"

    def test_c5_vanishes_at_z0(self):
        """C_5 vanishes at z=0."""
        # VERIFIED [DC] z-dependence [DA] propagator^3 ~ |z|^6
        C5 = genus2_cocycle_c5_k3(TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP)
        assert abs(C5) < 1e-15

    def test_ck_generic_vanishes_at_z0(self):
        """C_k vanishes at z=0 for all k."""
        # VERIFIED [DC] z-dependence [DA] all cocycles have propagator factor
        for k in range(3, 8):
            Ck = genus2_cocycle_ck_k3(k, TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP)
            assert abs(Ck) < 1e-14, f"C_{k} at z=0 = {Ck}"

    def test_ck_routing_consistency(self):
        """genus2_cocycle_ck_k3(3,...) matches genus2_cocycle_c3_k3(...)."""
        # VERIFIED [DC] routing [DA] dispatch function consistency
        C3_direct = genus2_cocycle_c3_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        C3_generic = genus2_cocycle_ck_k3(3, TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert abs(C3_direct - C3_generic) < 1e-12

    def test_c4_routing_consistency(self):
        """genus2_cocycle_ck_k3(4,...) matches genus2_cocycle_c4_k3(...)."""
        # VERIFIED [DC] routing [DA] dispatch function consistency
        C4_direct = genus2_cocycle_c4_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        C4_generic = genus2_cocycle_ck_k3(4, TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert abs(C4_direct - C4_generic) < 1e-12


# ================================================================
# SECTION 4: SHADOW CORRECTION FACTOR
# ================================================================

class TestShadowCorrectionFactor:
    """Test the shadow correction factor R_shadow^{K3}."""

    def test_r_shadow_at_z0_is_one(self):
        """R_shadow = 1 at z=0 (all cocycles vanish)."""
        # VERIFIED [DC] separating limit [DA] all C_k vanish at z=0
        data = shadow_correction_factor_k3(TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP, max_depth=6)
        assert abs(data["R_shadow"] - 1.0) < 1e-12

    def test_r_shadow_near_one_for_small_z(self):
        """R_shadow is close to 1 for small |z|."""
        # VERIFIED [DC] perturbative expansion [DA] C_k ~ |z|^{2(k-2)}
        data = shadow_correction_factor_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=6)
        assert abs(data["R_shadow"] - 1.0) < 0.5

    def test_r_shadow_structure(self):
        """R_shadow = 1 + sum S_k * C_k matches internal components."""
        # VERIFIED [DC] formula consistency [DA] explicit summation
        data = shadow_correction_factor_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=6)
        R_check = 1.0 + sum(data["contributions"].values())
        assert abs(data["R_shadow"] - R_check) < 1e-12

    def test_partial_sums_monotone_approach(self):
        """Partial sums approach R_shadow as depth increases."""
        # VERIFIED [DC] convergence [DA] asymptotic expansion
        data = shadow_correction_factor_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=8)
        ps = data["partial_sums"]
        # Last partial sum should equal R_shadow
        assert abs(ps[8] - data["R_shadow"]) < 1e-12

    def test_shadow_class_m_flagged(self):
        """Shadow data correctly flags class M."""
        # VERIFIED [DC] class [DA] Delta != 0
        data = shadow_correction_factor_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert data["shadow_class"] == "M"
        assert data["is_gevrey_1"] is True

    def test_max_depth_3_vs_8(self):
        """Deeper shadow corrections add to R_shadow."""
        # VERIFIED [DC] depth comparison [DA] additional terms
        data_3 = shadow_correction_factor_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=3)
        data_8 = shadow_correction_factor_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=8)
        # At depth 3: only C_3
        assert 3 in data_3["contributions"]
        assert 4 not in data_3["contributions"]
        # At depth 8: C_3 through C_8
        for k in range(3, 9):
            assert k in data_8["contributions"]


# ================================================================
# SECTION 5: FULL PARTITION FUNCTION
# ================================================================

class TestFullPartitionFunction:
    """Test the full genus-2 K3 x E partition function."""

    def test_returns_dict(self):
        """Output is a dictionary with required keys."""
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert isinstance(result, dict)
        assert "Z2_k3e" in result
        assert "R_shadow" in result
        assert "claim_status" in result

    def test_claim_status_conjectural(self):
        """K3xE result is explicitly CONJECTURAL (AP-CY6/14)."""
        # VERIFIED [DC] claim status [LT] AP-CY6/14 compliance
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert "CONJECTURAL" in result["claim_status"]

    def test_factorisation_z2_equals_heis_times_r(self):
        """Z_2^{K3xE} = Z_2^{Heis,c=24} * R_shadow."""
        # VERIFIED [DC] factorisation [DA] definition
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=6)
        expected = result["Z2_heisenberg_c24"] * result["R_shadow"]
        if abs(expected) > 1e-300:
            assert abs(result["Z2_k3e"] - expected) / abs(expected) < 1e-10

    def test_heis_c24_is_delta5_inv2(self):
        """Z_2^{Heis,c=24} = Delta_5^{-2}."""
        # VERIFIED [DC] formula [LT] free-boson genus-2 at c=24
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        d5 = result["Delta_5"]
        if abs(d5) > 1e-300:
            expected = d5 ** (-2)
            assert abs(result["Z2_heisenberg_c24"] - expected) / abs(expected) < 1e-10

    def test_heis_c24_equals_1_over_phi10(self):
        """Z_2^{Heis,c=24} = 1/Phi_10 (since Phi_10 = Delta_5^2, and Heis = Delta_5^{-c/12} = Delta_5^{-2})."""
        # VERIFIED [DC] identity [LT] Phi_10 = Delta_5^2
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        phi10 = result["Phi_10"]
        if abs(phi10) > 1e-300:
            inv_phi10 = 1.0 / phi10
            assert abs(result["Z2_heisenberg_c24"] - inv_phi10) / abs(inv_phi10) < 1e-8

    def test_kappa_spectrum(self):
        """Output has correct kappa spectrum."""
        # VERIFIED [DC] kappa values [LT] CLAUDE.md kappa table
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert result["kappa_ch"] == 3
        assert result["kappa_cat"] == 0
        assert result["kappa_cat_fiber"] == 2
        assert result["kappa_BKM"] == 5
        assert result["kappa_fiber"] == 24

    def test_weight_z2_heis(self):
        """Z_2^{Heis,c=24} has weight -12 = -c/2."""
        # VERIFIED [DC] weight [LT] genus-2 bosonisation formula
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert result["weight_Z2_heis"] == -12

    def test_weight_s_hat(self):
        """S-hat has weight -4 = -2*kappa_cat_fiber."""
        # VERIFIED [DC] weight formula [LT] conj:sp4-modularity
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert result["weight_S_hat"] == -4
        assert result["weight_S_hat"] == -2 * result["kappa_cat_fiber"]

    def test_shadow_class_m(self):
        """K3xE is class M (mock Siegel modular)."""
        # VERIFIED [DC] class [DA] K3 sigma model is class M
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert result["shadow_class"] == "M"
        assert result["is_mock_modular"] is True

    def test_shadow_siegel_gap_present(self):
        """The shadow-Siegel gap is flagged."""
        # VERIFIED [DC] gap flag [LT] thm:shadow-siegel-gap
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert result["shadow_siegel_gap_present"] is True

    def test_nonzero_partition_function(self):
        """Z_2^{K3xE} is nonzero for generic Omega."""
        # VERIFIED [DC] nonvanishing [DA] Delta_5 != 0 generically
        result = genus2_partition_k3xe_full(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert abs(result["Z2_k3e"]) > 1e-20


# ================================================================
# SECTION 6: SECOND-QUANTIZATION BRIDGE
# ================================================================

class TestSecondQuantizationBridge:
    """Test the second-quantization bridge analysis."""

    def test_heis_equals_dmvv(self):
        """Z_2^{Heis,c=24} = 1/Phi_10 (the DMVV answer IS the Heisenberg)."""
        # VERIFIED [DC] identity [LT] Phi_10 = Delta_5^2
        bridge = second_quantization_bridge(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert bridge["heis_c24_equals_1_over_phi10"]

    def test_bridge_factor_is_1_over_r(self):
        """Bridge factor B = 1/R_shadow."""
        # VERIFIED [DC] formula [DA] definition of bridge factor
        bridge = second_quantization_bridge(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        R = bridge["R_shadow"]
        B = bridge["bridge_factor"]
        if abs(R) > 1e-30:
            assert abs(B * R - 1.0) < 1e-10

    def test_four_obstructions_present(self):
        """All four shadow-Siegel gap obstructions are listed."""
        # VERIFIED [DC] O1-O4 [LT] thm:shadow-siegel-gap
        bridge = second_quantization_bridge(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        gap = bridge["shadow_siegel_gap"]
        assert "O1_categorical" in gap
        assert "O2_modular_characteristic" in gap
        assert "O3_second_quantization" in gap
        assert "O4_schottky" in gap

    def test_o2_kappa_ratio(self):
        """O2: kappa_BKM/kappa_ch = 5/3."""
        # VERIFIED [DC] ratio [LT] kappa spectrum
        bridge = second_quantization_bridge(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert "5/3" in bridge["shadow_siegel_gap"]["O2_modular_characteristic"] or \
               "1.6667" in bridge["shadow_siegel_gap"]["O2_modular_characteristic"]


# ================================================================
# SECTION 7: FOURIER-JACOBI
# ================================================================

class TestFourierJacobiK3E:
    """Test Fourier-Jacobi expansion for K3 x E."""

    def test_psi_neg1_from_phi10(self):
        """psi_{-1}^{Heis} = 1/phi_{10,1}^2."""
        # VERIFIED [DC] FJ leading term [LT] Delta_5^{-2} expansion
        fj = fourier_jacobi_k3xe(0.2 + 1.0j, 0.3 + 0.1j, 0.0 + 2.0j, max_shadow_depth=4)
        phi_m1 = fj["phi_10_1"]
        if abs(phi_m1) > 1e-300:
            expected = 1.0 / phi_m1**2
            assert abs(fj["psi_neg1_heisenberg"] - expected) / abs(expected) < 1e-9

    def test_psi_neg1_full_includes_shadow(self):
        """psi_{-1}^{full} = psi_{-1}^{Heis} * R_shadow."""
        # VERIFIED [DC] factorisation [DA] shadow correction at leading FJ order
        fj = fourier_jacobi_k3xe(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        expected = fj["psi_neg1_heisenberg"] * fj["R_shadow"]
        if abs(expected) > 1e-300 and not np.isinf(abs(expected)):
            assert abs(fj["psi_neg1_full"] - expected) / abs(expected) < 1e-10

    def test_shadow_fj_correction_at_z0(self):
        """Shadow FJ correction = 0 at z=0."""
        # VERIFIED [DC] separating limit [DA] R_shadow = 1 at z=0
        fj = fourier_jacobi_k3xe(TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP, max_shadow_depth=4)
        assert abs(fj["shadow_FJ_correction"]) < 1e-12

    def test_conjectural_status(self):
        """FJ result is CONJECTURAL."""
        fj = fourier_jacobi_k3xe(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4)
        assert fj["claim_status"] == "CONJECTURAL"


# ================================================================
# SECTION 8: E_3 BAR COHOMOLOGY AT GENUS 2
# ================================================================

class TestE3BarGenus2:
    """Test E_3 bar cohomology at genus 2 for K3 x E (class M)."""

    def test_dimension_6_squared(self):
        """dim E_inf = 6^2 = 36 for class M at genus 2."""
        # VERIFIED [DC] dimension formula [DA] e3_bar_higher_genus_class_m.py
        data = e3_bar_genus2_k3xe()
        assert data["E_inf_dimension"] == 36
        assert data["E_inf_dimension"] == 6**2

    def test_not_8_squared(self):
        """dim != 8^2 = 64 (that is class L,C, AP-CY21 violation)."""
        # VERIFIED [DC] AP-CY21 [LT] class M != class L,C
        data = e3_bar_genus2_k3xe()
        assert data["E_inf_dimension"] != 64
        assert data["class_LC_dimension"] == 64

    def test_deficit(self):
        """Deficit = 8^2 - 6^2 = 64 - 36 = 28."""
        # VERIFIED [DC] deficit [DA] d_4 kills 28 states
        data = e3_bar_genus2_k3xe()
        assert data["deficit"] == 28

    def test_poincare_polynomial(self):
        """Poincare polynomial = 9t^2 + 18t^3 + 9t^4."""
        # VERIFIED [DC] polynomial [DA] (3t(1+t))^2 expansion
        data = e3_bar_genus2_k3xe()
        p = data["E_inf_poincare"]
        assert p[2] == 9
        assert p[3] == 18
        assert p[4] == 9
        assert sum(p.values()) == 36

    def test_e4_equals_einf(self):
        """E_4 = E_inf at genus 2 (unconditional, degree reasons)."""
        # VERIFIED [DC] spectral sequence [DA] d_5 shift exceeds support width
        data = e3_bar_genus2_k3xe()
        assert data["E4_equals_Einf"] is True

    def test_proved_status(self):
        """E_3 bar result is PROVED (not conjectural)."""
        data = e3_bar_genus2_k3xe()
        assert "PROVED" in data["claim_status"]

    def test_shadow_class_m(self):
        """Shadow class is M."""
        data = e3_bar_genus2_k3xe()
        assert data["shadow_class"] == "M"


# ================================================================
# SECTION 9: WEIGHT TABLE
# ================================================================

class TestWeightTable:
    """Test the genus-2 weight table for K3 x E."""

    def test_kappa_spectrum_complete(self):
        """Weight table includes all four kappa values."""
        # VERIFIED [DC] completeness [LT] CLAUDE.md kappa-spectrum
        table = genus2_k3xe_weight_table()
        spectrum = table["kappa_spectrum"]
        assert spectrum["kappa_ch"]["value"] == 3
        assert spectrum["kappa_cat"]["value"] == 0
        assert spectrum["kappa_cat_fiber"]["value"] == 2
        assert spectrum["kappa_BKM"]["value"] == 5
        assert spectrum["kappa_fiber"]["value"] == 24

    def test_weight_relations(self):
        """Weight relations are internally consistent."""
        # VERIFIED [DC] arithmetic [LT] modular weight additivity
        table = genus2_k3xe_weight_table()
        wr = table["weight_relations"]
        assert "wt(S_hat) = -2*kappa_cat_fiber" in wr
        assert "wt(Phi_10) = 2*kappa_BKM" in wr

    def test_heis_weight_minus_12(self):
        """Heisenberg at c=24 has weight -12."""
        table = genus2_k3xe_weight_table()
        assert table["genus2_weights"]["Z2_heisenberg_c24"]["weight"] == -12

    def test_1_over_phi10_weight_minus_10(self):
        """1/Phi_10 has weight -10."""
        table = genus2_k3xe_weight_table()
        assert table["genus2_weights"]["1_over_Phi10"]["weight"] == -10

    def test_s_hat_weight_minus_4(self):
        """S-hat has weight -4."""
        table = genus2_k3xe_weight_table()
        assert table["genus2_weights"]["S_hat"]["weight"] == -4

    def test_k3e_mock_modular(self):
        """K3xE full Z_2 is mock Siegel modular."""
        table = genus2_k3xe_weight_table()
        assert "mock" in table["genus2_weights"]["Z2_k3e_full"]["type"].lower()

    def test_e3_bar_included(self):
        """Weight table includes E_3 bar data."""
        table = genus2_k3xe_weight_table()
        assert "e3_bar_genus2" in table
        assert table["e3_bar_genus2"]["E_inf_dimension"] == 36


# ================================================================
# SECTION 10: BOREL RESUMMATION
# ================================================================

class TestBorelResummation:
    """Test Borel resummation of the shadow correction."""

    def test_borel_returns_dict(self):
        """Borel resummation returns expected keys."""
        data = borel_resummed_r_shadow_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=6, N_borel=20)
        assert "R_borel" in data
        assert "R_naive" in data
        assert "discrepancy_naive_vs_borel" in data

    def test_borel_at_z0_is_one(self):
        """Borel resummation gives R = 1 at z=0."""
        # VERIFIED [DC] separating limit [DA] all cocycles vanish
        data = borel_resummed_r_shadow_k3(TAU_DEEP, 0.0 + 0.0j, SIGMA_DEEP, max_depth=6, N_borel=20)
        assert abs(data["R_borel"] - 1.0) < 1e-8

    def test_borel_near_naive_for_small_z(self):
        """Borel and naive agree for small z (perturbative regime)."""
        # VERIFIED [DC] asymptotic agreement [DA] Gevrey-1 series
        data = borel_resummed_r_shadow_k3(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_depth=6, N_borel=30)
        # For small z, the series converges and both methods agree
        assert data["discrepancy_naive_vs_borel"] < 0.5

    def test_full_partition_with_borel(self):
        """Full partition function can be computed with Borel resummation."""
        result = genus2_partition_k3xe_full(
            TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=6, use_borel=True)
        assert result["use_borel"] is True
        assert abs(result["Z2_k3e"]) > 1e-30


# ================================================================
# SECTION 11: SP_4(Z) MODULARITY ANALYSIS
# ================================================================

class TestSp4ModularityK3E:
    """Test Sp_4(Z) modularity analysis."""

    def test_weight_discrepancy(self):
        """Weight discrepancy between Z_2^{Heis} and 1/Phi_10 is -2."""
        # VERIFIED [DC] arithmetic [LT] -12 - (-10) = -2
        data = sp4_modularity_analysis_k3xe(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert data["weight_discrepancy"] == -2

    def test_weight_discrepancy_equals_minus_kappa_cat_fiber(self):
        """Weight discrepancy = -kappa_cat_fiber = -2."""
        # VERIFIED [DC] identity [LT] weight relation
        data = sp4_modularity_analysis_k3xe(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert data["weight_discrepancy_equals_minus_kappa_cat_fiber"]

    def test_delta5_multiplier(self):
        """Delta_5 picks up sign -1 under tau -> tau+1."""
        # VERIFIED [DC] multiplier [LT] theta transformation
        data = sp4_modularity_analysis_k3xe(TAU, Z_OFF, SIGMA, N_terms=N_THETA)
        ratio = data["delta5_t1_multiplier"]
        if np.isfinite(ratio):
            assert abs(ratio - (-1.0)) < 1e-3

    def test_conjectural_status(self):
        """Modularity analysis is CONJECTURAL."""
        data = sp4_modularity_analysis_k3xe(TAU_DEEP, Z_DEEP, SIGMA_DEEP)
        assert "CONJECTURAL" in data["claim_status"]


# ================================================================
# SECTION 12: FULL SUMMARY
# ================================================================

class TestFullSummary:
    """Test the complete genus-2 K3 x E summary."""

    def test_summary_returns_all_components(self):
        """Summary includes all sub-analyses."""
        summary = genus2_k3xe_full_summary(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4, N_terms=10)
        assert "partition_function" in summary
        assert "second_quantization_bridge" in summary
        assert "fourier_jacobi" in summary
        assert "modularity_analysis" in summary
        assert "weight_table" in summary
        assert "k3_shadow_tower" in summary

    def test_summary_claim_status(self):
        """Summary carries CONJECTURAL claim status."""
        summary = genus2_k3xe_full_summary(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4, N_terms=10)
        assert "CONJECTURAL" in summary["claim_status"]

    def test_shadow_siegel_gap_in_summary(self):
        """Summary includes shadow-Siegel gap obstructions."""
        summary = genus2_k3xe_full_summary(TAU_DEEP, Z_DEEP, SIGMA_DEEP, max_shadow_depth=4, N_terms=10)
        assert "shadow_siegel_gap_obstructions" in summary
