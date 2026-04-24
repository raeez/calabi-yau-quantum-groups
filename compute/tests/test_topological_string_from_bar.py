r"""Tests for topological_string_from_bar.py -- Z_top from the bar complex shadow tower.

Covers:
  1. F_1 = S_2/24 (Task 1, 7 tests)
  2. F_2 from BCOV and S_3 (Task 2, 6 tests)
  3. GV multicover kernel and GW invariants (Task 3, 8 tests)
  4. K3 x E: DMVV as bar complex GF (Task 4, 6 tests)
  5. Holomorphic anomaly from shadow class (Task 5, 6 tests)
  6. Shadow genus expansion (4 tests)
  7. Grand verification (2 tests)

Total: 39 tests

Verification paths:
  1. Direct computation from defining formula
  2. Alternative formula / independent derivation
  3. Literature comparison (OEIS, BCOV, GV, DMVV)
  4. Cross-geometry consistency
  5. Structural properties (integrality, positivity, universality)

AP compliance:
  AP-CY6: CY3 results marked CONDITIONAL where needed
  AP-CY8: Borcherds != bar Euler; bridge cited
  AP113: All kappa values subscripted
  AP155: Known invariants noted; novelty is construction path
  AP-CY24: All numerical values verified against function output
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction

import pytest

_ROOT = os.path.expanduser("~/calabi-yau-quantum-groups")
_LIB = os.path.join(_ROOT, "compute", "lib")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

from topological_string_from_bar import (
    # Fundamentals
    bernoulli_numbers,
    lambda_fp,
    constant_map_fg_bcov,
    # Task 1
    genus_1_from_shadow,
    genus_1_verification_all_cases,
    Genus1Data,
    # Task 2
    genus_2_from_bcov_and_shadow,
    genus_2_shadow_feynman_comparison,
    Genus2Data,
    # Task 3
    _csc2_expansion_coefficients,
    gv_multicover_kernel,
    gw_from_gv,
    gv_integrality_check,
    # Task 4
    K3E_KAPPA_SPECTRUM,
    dmvv_as_bar_complex,
    gottsche_from_bar_exponents,
    KNOWN_HILB_CHI_K3,
    # Task 5
    holomorphic_anomaly_from_shadow_class,
    anomaly_shadow_dictionary,
    mock_modular_from_class_m,
    HolomorphicAnomalyData,
    # Genus expansion
    shadow_genus_amplitudes,
    full_genus_expansion,
    HEISENBERG_SHADOW,
    VIRASORO_C1_SHADOW,
    c3_genus_expansion,
    conifold_genus_expansion,
    k3e_genus_expansion,
    # Grand
    grand_verification,
)


# =====================================================================
# Section 1: F_1 = S_2/24 (Task 1, 7 tests)
# =====================================================================

class TestGenus1Seed:
    """F_1 = S_2/24 = kappa_ch/24: the genus-1 seed of the BCOV recursion."""

    def test_lambda_1_equals_1_over_24(self):
        """Path 1 (direct): lambda_1^FP = 1/24."""
        # VERIFIED [DC] structural property [LT] Faber-Pandharipande
        assert lambda_fp(1) == Fraction(1, 24)

    def test_f1_c3(self):
        """Path 1 (direct): F_1(C^3) = 1/24 (kappa_ch = 1)."""
        data = genus_1_from_shadow(Fraction(1))
        # VERIFIED [DC] genus free energy [LT] topological string
        assert data.F_1 == Fraction(1, 24)
        assert data.identity_holds

    def test_f1_conifold(self):
        """Path 1 (direct): F_1(conifold) = 1/24 (kappa_ch = 1)."""
        data = genus_1_from_shadow(Fraction(1))
        # VERIFIED [DC] genus free energy [LT] topological string
        assert data.F_1 == Fraction(1, 24)

    def test_f1_k3xe(self):
        """Path 1 (direct): F_1(K3 x E) = 3/24 = 1/8 (kappa_ch = 3, AP113)."""
        data = genus_1_from_shadow(Fraction(3))
        # VERIFIED [DC] genus free energy [LT] topological string
        assert data.F_1 == Fraction(1, 8)
        assert data.identity_holds

    def test_f1_quintic(self):
        """Path 1 (direct): F_1(quintic) = -25/72 (kappa_ch = -25/3, CONDITIONAL).

        CONDITIONAL on CY-A_3 (AP-CY6).
        """
        data = genus_1_from_shadow(Fraction(-25, 3))
        # VERIFIED [DC] genus free energy [LT] BCOV
        assert data.F_1 == Fraction(-25, 72)
        assert data.identity_holds

    def test_f1_virasoro_c1(self):
        """Path 1 (direct): F_1(Virasoro c=1) = 1/48 (kappa_ch = 1/2)."""
        data = genus_1_from_shadow(Fraction(1, 2))
        # VERIFIED [DC] genus free energy [LT] topological string
        assert data.F_1 == Fraction(1, 48)
        assert data.identity_holds

    def test_f1_all_cases(self):
        """Path 4 (cross-check): F_1 = S_2/24 holds for all standard geometries."""
        cases = genus_1_verification_all_cases()
        for name, data in cases.items():
            assert data.identity_holds, f"F_1 = S_2/24 failed for {name}"


# =====================================================================
# Section 2: F_2 from BCOV and S_3 (Task 2, 6 tests)
# =====================================================================

class TestGenus2BCOV:
    """F_2 from BCOV: ratio F_2/F_1 = 7/240 is universal; S_3 controls off-diagonal."""

    def test_lambda_2_equals_7_over_5760(self):
        """Path 1 (direct): lambda_2^FP = 7/5760."""
        # VERIFIED [DC] structural property [LT] Faber-Pandharipande
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_f2_virasoro_c1(self):
        """Path 1 (direct): F_2(Virasoro c=1) = 7/11520 (kappa_ch = 1/2)."""
        data = genus_2_from_bcov_and_shadow(Fraction(1, 2), Fraction(2))
        # VERIFIED [DC] genus free energy [LT] BCOV shadow tower
        assert data.F_2 == Fraction(7, 11520)

    def test_f2_c3(self):
        """Path 1 (direct): F_2(C^3) = 7/5760 (kappa_ch = 1)."""
        data = genus_2_from_bcov_and_shadow(Fraction(1), Fraction(0))
        # VERIFIED [DC] genus free energy [LT] topological string
        assert data.F_2 == Fraction(7, 5760)

    def test_ratio_f2_f1_virasoro(self):
        """Path 5 (structural): F_2/F_1 = 7/240 for Virasoro c=1."""
        data = genus_2_from_bcov_and_shadow(Fraction(1, 2), Fraction(2))
        # VERIFIED [DC] universality [LT] shadow tower recursion
        assert data.ratio_F2_F1 == Fraction(7, 240)
        assert data.ratio_is_universal

    def test_ratio_f2_f1_c3(self):
        """Path 5 (structural): F_2/F_1 = 7/240 for C^3 (universal ratio)."""
        data = genus_2_from_bcov_and_shadow(Fraction(1), Fraction(0))
        # VERIFIED [DC] universality [LT] shadow tower recursion
        assert data.ratio_F2_F1 == Fraction(7, 240)
        assert data.ratio_is_universal

    def test_ratio_universality_across_kappa(self):
        """Path 5 (structural): ratio F_2/F_1 = 7/240 for multiple kappa values.

        The universality of this ratio is the shadow tower prediction:
        on the scalar lane, the BCOV recursion ratio depends only on
        the A-hat genus, not on the specific algebra or geometry.
        """
        for kappa in [Fraction(1), Fraction(1, 2), Fraction(3),
                      Fraction(-25, 3), Fraction(7, 4)]:
            data = genus_2_from_bcov_and_shadow(kappa, Fraction(2))
            assert data.ratio_F2_F1 == Fraction(7, 240), (
                f"Ratio not 7/240 at kappa_ch = {kappa}"
            )


# =====================================================================
# Section 3: GV multicover kernel and GW invariants (Task 3, 8 tests)
# =====================================================================

class TestGVMulticoverKernel:
    """GV multicover kernel from (2*sin(u/2))^{-2} expansion."""

    def test_csc2_coeff_a0(self):
        """Path 1 (direct): a_0 = 1 (coefficient of u^{-2})."""
        coeffs = _csc2_expansion_coefficients(4)
        # VERIFIED [DC] series expansion [LT] csc^2 Laurent expansion
        assert coeffs[0] == Fraction(1)

    def test_csc2_coeff_a1(self):
        """Path 1 (direct): a_1 = 1/12 (coefficient of u^0)."""
        coeffs = _csc2_expansion_coefficients(4)
        # VERIFIED [DC] series expansion [LT] csc^2 Laurent expansion
        assert coeffs[1] == Fraction(1, 12)

    def test_csc2_coeff_a2(self):
        """Path 1 (direct): a_2 = 1/240 (coefficient of u^2)."""
        coeffs = _csc2_expansion_coefficients(4)
        # VERIFIED [DC] series expansion [LT] csc^2 Laurent expansion
        assert coeffs[2] == Fraction(1, 240)

    def test_csc2_coeff_a3(self):
        """Path 1 (direct): a_3 = 1/6048 (coefficient of u^4)."""
        coeffs = _csc2_expansion_coefficients(4)
        # VERIFIED [DC] series expansion [LT] csc^2 Laurent expansion
        assert coeffs[3] == Fraction(1, 6048)

    def test_kernel_genus0_trilogarithm(self):
        """Path 1 (direct): genus-0 kernel at k=1 is 1 (Li_3 coefficient)."""
        # VERIFIED [DC] GV formula [LT] Gopakumar-Vafa
        assert gv_multicover_kernel(0, 1) == Fraction(1)
        assert gv_multicover_kernel(0, 2) == Fraction(1, 8)
        assert gv_multicover_kernel(0, 3) == Fraction(1, 27)

    def test_kernel_genus1(self):
        """Path 1 (direct): genus-1 kernel at k=1 is 1/12."""
        # VERIFIED [DC] GV formula [LT] Gopakumar-Vafa
        assert gv_multicover_kernel(1, 1) == Fraction(1, 12)
        assert gv_multicover_kernel(1, 2) == Fraction(1, 24)

    def test_kernel_genus2(self):
        """Path 1 (direct): genus-2 kernel at k=1 is 1/240.

        (2*sin(u/2))^{-2} = u^{-2} + 1/12 + (1/240)*u^2 + ...
        All coefficients are POSITIVE (manifestly, since csc^2 > 0).
        """
        # VERIFIED [DC] GV formula [LT] csc^2 expansion
        assert gv_multicover_kernel(2, 1) == Fraction(1, 240)
        assert gv_multicover_kernel(2, 2) == Fraction(2, 240)

    def test_conifold_gw_from_gv(self):
        """Path 2 (alternative): conifold GW from GV with n_0^1 = 1.

        F_0 at Q^1 = 1 (trilogarithm: Li_3(Q) at Q^1 = 1/1^3 = 1)
        F_1 at Q^1 = 1/12 (genus-1 propagator)
        F_2 at Q^1 = 1/240 (genus-2 propagator)
        """
        gv = {(0, 1): 1}
        gw = gw_from_gv(gv, max_g=2, max_d=3)
        # VERIFIED [DC] genus free energy [LT] Gopakumar-Vafa
        assert gw[(0, 1)] == Fraction(1)
        assert gw[(1, 1)] == Fraction(1, 12)
        assert gw[(2, 1)] == Fraction(1, 240)


# =====================================================================
# Section 4: K3 x E: DMVV as bar complex GF (Task 4, 6 tests)
# =====================================================================

class TestK3xEDMVV:
    """K3 x E: DMVV formula as bar complex generating function.

    ALL results CONDITIONAL on CY-A_3 (AP-CY6).
    AP-CY8: bridge steps cited explicitly in dmvv_as_bar_complex().
    AP113: kappa_ch = 3, kappa_BKM = 5 (subscripted).
    AP155: DMVV, Gottsche, Delta_5 are known; construction path is new.
    """

    def test_kappa_spectrum(self):
        """Path 3: K3 x E total and fiber kappa labels are separated."""
        # VERIFIED [DC] kappa-spectrum [LT] Vol III CLAUDE.md
        assert K3E_KAPPA_SPECTRUM["kappa_ch"] == Fraction(3)
        assert K3E_KAPPA_SPECTRUM["kappa_BKM"] == 5
        assert K3E_KAPPA_SPECTRUM["kappa_cat"] == Fraction(0)
        assert K3E_KAPPA_SPECTRUM["kappa_cat_fiber"] == 2
        assert K3E_KAPPA_SPECTRUM["kappa_fiber"] == 24

    def test_gottsche_hilb0(self):
        """Path 1 (direct): chi(Hilb^0(K3)) = 1 from bar exponents."""
        g = gottsche_from_bar_exponents(5)
        # VERIFIED [DC] partition function [LT] Gottsche 1990
        assert g[0] == 1

    def test_gottsche_hilb1(self):
        """Path 1 (direct): chi(Hilb^1(K3)) = chi(K3) = 24."""
        g = gottsche_from_bar_exponents(5)
        # VERIFIED [DC] partition function [LT] Gottsche 1990
        assert g[1] == 24

    def test_gottsche_known_values(self):
        """Path 3 (literature): Gottsche formula matches known chi(Hilb^n(K3)).

        Known: {0:1, 1:24, 2:324, 3:3200, 4:25650, 5:176256}.
        These are 24-coloured partition numbers p_{24}(n).
        """
        g = gottsche_from_bar_exponents(5)
        for n, expected in KNOWN_HILB_CHI_K3.items():
            assert g[n] == expected, (
                f"chi(Hilb^{n}(K3)) = {g[n]}, expected {expected}"
            )

    def test_dmvv_bridge_structure(self):
        """Path 5 (structural): DMVV-bar bridge has all 4 required steps.

        AP-CY8: the Borcherds denominator is NOT the bar Euler product.
        The identification requires all 4 steps to be cited explicitly.
        """
        data = dmvv_as_bar_complex()
        bridge = data["bar_complex_bridge"]
        assert "step_1" in bridge  # Phi: K3xE -> A
        assert "step_2" in bridge  # Bar Euler product
        assert "step_3" in bridge  # Borcherds lift
        assert "step_4" in bridge  # Oberdieck-Pixton

    def test_dmvv_conditional_marking(self):
        """Path 5 (structural): DMVV result marked CONDITIONAL on CY-A_3.

        AP-CY6: A_{K3xE} does NOT exist at d=3.
        """
        data = dmvv_as_bar_complex()
        assert "CY-A_3" in data["full"]["conditional_on"]
        assert "AP-CY6" in data["ap_compliance"]


# =====================================================================
# Section 5: Holomorphic anomaly from shadow class (Task 5, 6 tests)
# =====================================================================

class TestHolomorphicAnomaly:
    """Holomorphic anomaly = shadow non-termination.

    Class G: no anomaly. Class M: mock modular, Gevrey-1.
    """

    def test_class_g_holomorphic(self):
        """Path 5 (structural): class G has no holomorphic anomaly."""
        data = holomorphic_anomaly_from_shadow_class("G")
        assert data.dbar_Fg_vanishes is True
        assert data.mock_modular is False

    def test_class_l_finite_anomaly(self):
        """Path 5 (structural): class L has finite anomaly."""
        data = holomorphic_anomaly_from_shadow_class("L")
        assert data.dbar_Fg_vanishes is False
        assert data.mock_modular is False
        assert "polynomial" in data.genus_expansion_type

    def test_class_c_convergent_anomaly(self):
        """Path 5 (structural): class C has convergent anomaly."""
        data = holomorphic_anomaly_from_shadow_class("C")
        assert data.dbar_Fg_vanishes is False
        assert data.mock_modular is False
        assert data.borel_summable is True
        assert "convergent" in data.genus_expansion_type

    def test_class_m_mock_modular(self):
        """Path 5 (structural): class M produces mock modular forms.

        The holomorphic anomaly IS the shadow tower's non-termination.
        """
        data = holomorphic_anomaly_from_shadow_class("M")
        assert data.dbar_Fg_vanishes is False
        assert data.mock_modular is True
        assert data.borel_summable is True  # Borel SUMMABLE, just not convergent
        assert "Gevrey-1" in data.genus_expansion_type

    def test_anomaly_dictionary_complete(self):
        """Path 5 (structural): all four shadow classes present in dictionary."""
        d = anomaly_shadow_dictionary()
        assert set(d.keys()) == {"G", "L", "C", "M"}

    def test_mock_modular_k3xe(self):
        """Path 5 (structural): K3 x E mock modular structure.

        kappa_ch = 3, kappa_fiber = 24. Shadow = 24*eta^3.
        Polar coefficient: h|_{q^{-1/8}} = -3.
        """
        data = mock_modular_from_class_m(Fraction(3), kappa_fiber=24)
        assert data["kappa_ch"] == Fraction(3)
        assert data["kappa_fiber"] == 24
        assert data["shadow_class"] == "M"
        assert "-3" in data["polar_coefficient"]


# =====================================================================
# Section 6: Shadow genus expansion (4 tests)
# =====================================================================

class TestShadowGenusExpansion:
    """Shadow genus amplitudes F_g = kappa_ch * lambda_g on scalar lane."""

    def test_c3_genus_expansion_positive(self):
        """Path 5 (structural): F_g(C^3) > 0 for all g >= 1."""
        amps = shadow_genus_amplitudes(Fraction(1), max_g=5)
        for g in range(1, 6):
            # VERIFIED [DC] genus free energy [LT] A-hat positivity (AP22)
            assert amps[g] > 0, f"F_{g}(C^3) = {amps[g]} not positive"

    def test_c3_genus_exact_values(self):
        """Path 1 (direct): F_g(C^3) matches exact A-hat coefficients."""
        amps = shadow_genus_amplitudes(Fraction(1), max_g=5)
        # VERIFIED [DC] genus free energy [LT] operadic Koszul theory
        assert amps[1] == Fraction(1, 24)
        assert amps[2] == Fraction(7, 5760)
        assert amps[3] == Fraction(31, 967680)
        assert amps[4] == Fraction(127, 154828800)
        assert amps[5] == Fraction(73, 3503554560)

    def test_conifold_deg0_twice_c3(self):
        """Path 4 (cross-check): conifold deg-0 = 2 * C^3 genus amplitudes."""
        c3 = shadow_genus_amplitudes(Fraction(1), max_g=3)
        con = shadow_genus_amplitudes(Fraction(2), max_g=3)
        for g in range(1, 4):
            assert con[g] == 2 * c3[g], f"Conifold deg-0 mismatch at g={g}"

    def test_k3xe_genus_expansion_conditional(self):
        """Path 5 (structural): K3 x E genus expansion is conditional.

        CONDITIONAL on CY-A_3 (AP-CY6).
        """
        result = k3e_genus_expansion(3)
        assert "CY-A_3" in result["conditional_on"]
        assert result["kappa_spectrum"]["kappa_ch"] == Fraction(3)


# =====================================================================
# Section 7: Grand verification (2 tests)
# =====================================================================

class TestGrandVerification:
    """Grand verification: all 5 tasks pass."""

    def test_grand_verification_all_pass(self):
        """All 5 tasks pass in the grand verification."""
        result = grand_verification()
        assert result["all_pass"]

    def test_grand_verification_individual_tasks(self):
        """Each task passes individually."""
        result = grand_verification()
        assert result["task_1_F1_eq_S2_over_24"]["all_pass"]
        assert result["task_2_F2_from_BCOV"]["universality_verified"]
        assert result["task_3_GW_from_bar"]["pass"]
        assert result["task_4_K3xE_DMVV"]["gottsche_match"]
        assert result["task_5_holomorphic_anomaly"]["pass"]
