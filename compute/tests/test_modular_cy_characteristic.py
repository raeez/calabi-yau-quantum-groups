"""Tests for modular_cy_characteristic: kappa(A_C) = chi^CY(C).

Ground truth:
  chapters/theory/modular_trace.tex (Theorem CY-D),
  chapters/examples/k3_times_e.tex (K3 x E tower, Delta_5),
  ~/chiral-bar-cobar/chapters/frame/higher_genus_modular_koszul.tex (shadow obstruction tower),
  Bershadsky-Cecotti-Ooguri-Vafa (BCOV, 1993),
  Gritsenko-Nikulin (BKM superalgebras and Siegel forms).

Tests organized by mathematical topic, each independently verifiable.
"""

from fractions import Fraction

import pytest

from compute.lib.modular_cy_characteristic import (
    HKRDecomposition,
    hkr_decomposition,
    hkr_k3,
    hkr_elliptic,
    hkr_quintic,
    hkr_k3_times_e,
    CYTrace,
    ModularCYCharacteristic,
    chi_cy_point,
    chi_cy_elliptic,
    chi_cy_k3,
    chi_cy_k3_times_e,
    chi_cy_quintic,
    chi_cy_resolved_conifold,
    categorical_trace_vect,
    categorical_trace_db_elliptic,
    categorical_trace_db_k3,
    categorical_trace_half_hh0,
    chi_cy_additivity_test,
    kappa_product_elliptic,
    kappa_additive_for_direct_sum,
    CYShadowClass,
    shadow_class_cy,
    A_HAT_COEFFICIENTS,
    shadow_amplitude_genus_g,
    shadow_amplitude_genus1,
    shadow_amplitude_genus2,
    shadow_amplitude_genus3,
    shadow_tower_scalar,
    BCOVData,
    bcov_genus1_coefficient,
    bcov_quintic,
    bcov_k3_times_e,
    HHShadowE2Page,
    spectral_sequence_genus1,
    spectral_sequence_genus2,
    GWComparison,
    QUINTIC_GW_GENUS0,
    QUINTIC_F1_CONST_MAP,
    gw_comparison_k3_times_e,
    gw_comparison_quintic,
    quintic_genus0_gw_data,
    topological_string_comparison,
    resolved_conifold_hodge,
    kappa_from_k3_fibration,
    kappa_from_arithmetic_genus_cy2,
    kappa_conjectural_cy3,
    verify_all_cy_characteristics,
)
from compute.lib.cy_euler import (
    k3_hodge,
    elliptic_curve_hodge,
    k3_times_e_hodge,
    quintic_hodge,
)


# ======================================================================
# 1. HKR decomposition
# ======================================================================

class TestHKRDecomposition:
    """Test the Hochschild-Kostant-Rosenberg decomposition for D^b(X)."""

    def test_hkr_k3_total_dimension(self):
        """Total dim HH_*(K3) = 24 = chi_top(K3).

        Sum of all HH_n dimensions equals the sum of all Hodge numbers,
        which for K3 is 1 + 0 + 0 + 1 + 20 + 1 + 0 + 0 + 1 = 24.
        """
        hkr = hkr_k3()
        assert hkr.total_dim == 24

    def test_hkr_k3_euler(self):
        """Euler char of HH = sum (-1)^n dim HH_n = (-1)^d * chi_top.

        For d=2 (even): euler_hh = chi_top(K3) = 24.
        The sign rule: euler_hh = (-1)^d * chi_top.
        """
        hkr = hkr_k3()
        assert hkr.euler_hh == 24

    def test_hkr_k3_hh0_is_22(self):
        """HH_0(K3) = H^0(O) + H^1(T) + H^2(wedge^2 T) = 1 + 20 + 1 = 22.

        For K3 (d=2): HH_0 = bigoplus_{p} H^p(Omega^{2-p}).
        p=0: H^0(Omega^2) = H^0(O) = 1 (since omega_K3 = O).
        p=1: H^1(Omega^1) = H^1(T^*) = h^{1,1} = 20.
        p=2: H^2(Omega^0) = H^2(O) = h^{0,2} = 1.
        Total: 1 + 20 + 1 = 22.
        """
        hkr = hkr_k3()
        assert hkr.hh[0] == 22

    def test_hkr_k3_hh_minus2(self):
        """HH_{-2}(K3) = H^0(Omega^0) = h^{0,0} = 1."""
        hkr = hkr_k3()
        assert hkr.hh[-2] == 1

    def test_hkr_k3_hh_plus2(self):
        """HH_2(K3) = H^2(Omega^2) = h^{2,2} = 1."""
        hkr = hkr_k3()
        assert hkr.hh[2] == 1

    def test_hkr_k3_hh_pm1_vanish(self):
        """HH_{+/-1}(K3) = 0 (K3 is simply connected)."""
        hkr = hkr_k3()
        assert hkr.hh.get(-1, 0) == 0
        assert hkr.hh.get(1, 0) == 0

    def test_hkr_elliptic_total_4(self):
        """Total dim HH_*(E) = 4 for an elliptic curve."""
        hkr = hkr_elliptic()
        assert hkr.total_dim == 4

    def test_hkr_elliptic_hh0_is_2(self):
        """HH_0(E) = 2 for an elliptic curve.

        d=1: HH_0 = H^0(Omega^1) + H^1(Omega^0) = h^{1,0} + h^{0,1} = 1 + 1 = 2.
        """
        hkr = hkr_elliptic()
        assert hkr.hh[0] == 2

    def test_hkr_elliptic_hh_minus1(self):
        """HH_{-1}(E) = H^0(O) = 1."""
        hkr = hkr_elliptic()
        assert hkr.hh[-1] == 1

    def test_hkr_elliptic_hh_plus1(self):
        """HH_1(E) = H^1(Omega^1) = h^{1,1} = 1."""
        hkr = hkr_elliptic()
        assert hkr.hh[1] == 1

    def test_hkr_elliptic_euler_0(self):
        """Euler of HH_*(E) = 1 - 2 + 1 = 0 = chi_top(E)."""
        hkr = hkr_elliptic()
        assert hkr.euler_hh == 0

    def test_hkr_quintic_hh0_is_204(self):
        """HH_0(quintic) = 204.

        d=3: HH_0 = H^0(Omega^3) + H^1(Omega^2) + H^2(Omega^1) + H^3(O)
                   = h^{3,0} + h^{2,1} + h^{1,2} + h^{0,3}
                   = 1 + 101 + 101 + 1 = 204.
        """
        hkr = hkr_quintic()
        assert hkr.hh[0] == 204

    def test_hkr_quintic_euler_200(self):
        """Euler of HH_*(quintic) = (-1)^d * chi_top = (-1)^3 * (-200) = 200.

        The sign rule for the HKR Euler characteristic:
          sum_n (-1)^n dim HH_n = (-1)^d * chi_top(X).
        For d=3 (odd): euler_hh = -chi_top = -(-200) = 200.
        """
        hkr = hkr_quintic()
        assert hkr.euler_hh == 200

    def test_hkr_quintic_hh_minus3(self):
        """HH_{-3}(quintic) = h^{0,0} = 1."""
        hkr = hkr_quintic()
        assert hkr.hh[-3] == 1

    def test_hkr_quintic_hh_plus3(self):
        """HH_3(quintic) = h^{3,3} = 1."""
        hkr = hkr_quintic()
        assert hkr.hh[3] == 1

    def test_hkr_quintic_hh_minus1(self):
        """HH_{-1}(quintic) = h^{1,1} = 1."""
        hkr = hkr_quintic()
        assert hkr.hh[-1] == 1

    def test_hkr_quintic_hh_plus1(self):
        """HH_1(quintic) = h^{2,2} = 1."""
        hkr = hkr_quintic()
        assert hkr.hh[1] == 1

    def test_hkr_k3xe_euler_0(self):
        """Euler of HH_*(K3 x E) = chi_top(K3 x E) = 0."""
        hkr = hkr_k3_times_e()
        assert hkr.euler_hh == 0

    def test_hkr_dimension_matches_cy(self):
        """HKR dimension field matches the CY dimension."""
        assert hkr_k3().dim == 2
        assert hkr_elliptic().dim == 1
        assert hkr_quintic().dim == 3
        assert hkr_k3_times_e().dim == 3


# ======================================================================
# 2. CY trace
# ======================================================================

class TestCYTrace:
    """Test the CY trace on Hochschild homology."""

    def test_trace_identity_k3(self):
        """Tr_CY(id) = 1 for K3."""
        tr = CYTrace(k3_hodge())
        assert tr.trace_identity == 1

    def test_trace_identity_elliptic(self):
        """Tr_CY(id) = 1 for elliptic curve."""
        tr = CYTrace(elliptic_curve_hodge())
        assert tr.trace_identity == 1

    def test_trace_identity_quintic(self):
        """Tr_CY(id) = 1 for the quintic."""
        tr = CYTrace(quintic_hodge())
        assert tr.trace_identity == 1

    def test_hh0_dim_k3(self):
        """dim HH_0(K3) = 22."""
        tr = CYTrace(k3_hodge())
        assert tr.hh0_dim == 22

    def test_hh0_dim_quintic(self):
        """dim HH_0(quintic) = 204."""
        tr = CYTrace(quintic_hodge())
        assert tr.hh0_dim == 204


# ======================================================================
# 3. Modular CY characteristic: chi^CY
# ======================================================================

class TestModularCYCharacteristic:
    """Test chi^CY = kappa(A_C) for standard families."""

    def test_point_kappa_0(self):
        """chi^CY(Vect) = 0 = kappa(trivial algebra)."""
        data = chi_cy_point()
        assert data.chi_cy == 0
        assert data.kappa == 0
        assert data.match is True

    def test_elliptic_kappa_1(self):
        """chi^CY(D^b(E)) = 1 = kappa(H_1) (rank-1 Heisenberg)."""
        data = chi_cy_elliptic()
        assert data.chi_cy == 1
        assert data.kappa == 1
        assert data.match is True

    def test_k3_kappa_2(self):
        """chi^CY(D^b(K3)) = 2 = chi(O_{K3})."""
        data = chi_cy_k3()
        assert data.chi_cy == 2
        assert data.kappa == 2
        assert data.match is True

    def test_k3_times_e_kappa_5(self):
        """chi^CY(D^b(K3 x E)) = 5 = weight(Delta_5). Core result."""
        data = chi_cy_k3_times_e()
        assert data.chi_cy == 5
        assert data.kappa == 5
        assert data.match is True
        assert data.source == "Theorem CY-D + Borcherds product (Delta_5)"

    def test_quintic_conjectural(self):
        """chi^CY(quintic) = -25/3 (CONJECTURAL, from chi/24)."""
        data = chi_cy_quintic()
        assert data.chi_cy == Fraction(-25, 3)
        assert "CONJECTURAL" in data.source

    def test_resolved_conifold_kappa_1(self):
        """chi^CY(resolved conifold) = 1 from single compact cycle."""
        data = chi_cy_resolved_conifold()
        assert data.chi_cy == 1
        assert data.match is True

    def test_chi_top_not_chi_cy(self):
        """chi^CY != chi_top in general. K3 x E: chi_top = 0, chi^CY = 5."""
        k3e = chi_cy_k3_times_e()
        assert k3e.chi_top == 0
        assert k3e.chi_cy == 5
        assert k3e.chi_top != k3e.chi_cy

    def test_elliptic_chi_top_vs_chi_cy(self):
        """Elliptic: chi_top = 0, chi^CY = 1."""
        e = chi_cy_elliptic()
        assert e.chi_top == 0
        assert e.chi_cy == 1

    def test_k3_chi_top_vs_chi_cy(self):
        """K3: chi_top = 24, chi^CY = 2."""
        k3 = chi_cy_k3()
        assert k3.chi_top == 24
        assert k3.chi_cy == 2

    def test_dimension_recorded(self):
        """Each CY characteristic records the correct CY dimension."""
        assert chi_cy_point().dimension == 0
        assert chi_cy_elliptic().dimension == 1
        assert chi_cy_k3().dimension == 2
        assert chi_cy_k3_times_e().dimension == 3
        assert chi_cy_quintic().dimension == 3


# ======================================================================
# 4. Additivity of chi^CY
# ======================================================================

class TestAdditivity:
    """Test additivity and non-additivity of chi^CY."""

    def test_direct_sum_additive(self):
        """kappa is additive for direct sums: kappa(A + B) = kappa(A) + kappa(B)."""
        data = chi_cy_additivity_test()
        assert data["kappa_additivity_direct_sum"] is True

    def test_k3xe_not_additive(self):
        """kappa(K3 x E) != kappa(K3) + kappa(E): 5 != 2 + 1 = 3."""
        data = chi_cy_additivity_test()
        assert data["product_is_additive_K3xE"] is False
        assert data["kappa_K3xE"] == 5
        assert data["kappa_K3_plus_E"] == 3

    def test_k3xe_discrepancy(self):
        """The discrepancy kappa(K3xE) - kappa(K3) - kappa(E) = 2."""
        data = chi_cy_additivity_test()
        assert data["K3xE_discrepancy"] == 2

    def test_product_elliptic_n1(self):
        """kappa(E^1) = 1."""
        assert kappa_product_elliptic(1) == 1

    def test_product_elliptic_n2(self):
        """kappa(E^2) = 2 (abelian surface, rank-2 Heisenberg)."""
        assert kappa_product_elliptic(2) == 2

    def test_product_elliptic_n3(self):
        """kappa(E^3) = 3 (abelian 3-fold, rank-3 Heisenberg)."""
        assert kappa_product_elliptic(3) == 3

    def test_product_elliptic_additive(self):
        """kappa(E^n) = n for all n (additive for abelian varieties)."""
        for n in range(1, 8):
            assert kappa_product_elliptic(n) == n


# ======================================================================
# 5. Shadow depth classification
# ======================================================================

class TestShadowDepth:
    """Test shadow depth classification for CY categories."""

    def test_point_gaussian(self):
        """Point is class G (Gaussian)."""
        sc = shadow_class_cy("point")
        assert sc.shadow_class == "G"
        assert sc.r_max == 2

    def test_elliptic_gaussian(self):
        """Elliptic curve -> Heisenberg -> class G."""
        sc = shadow_class_cy("elliptic curve")
        assert sc.shadow_class == "G"
        assert sc.r_max == 2

    def test_k3_lie(self):
        """K3 surface -> class L (Lie-type from lattice)."""
        sc = shadow_class_cy("K3")
        assert sc.shadow_class == "L"
        assert sc.r_max == 3

    def test_k3xe_mixed(self):
        """K3 x E -> class M (infinite BKM tower)."""
        sc = shadow_class_cy("K3 x E")
        assert sc.shadow_class == "M"
        assert sc.r_max == -1  # infinity

    def test_quintic_mixed(self):
        """Quintic -> class M (infinite GW tower)."""
        sc = shadow_class_cy("quintic")
        assert sc.shadow_class == "M"
        assert sc.r_max == -1

    def test_conifold_gaussian(self):
        """Resolved conifold -> class G (single Heisenberg)."""
        sc = shadow_class_cy("resolved conifold")
        assert sc.shadow_class == "G"
        assert sc.r_max == 2

    def test_unknown_raises(self):
        """Unknown CY category raises ValueError."""
        with pytest.raises(ValueError, match="Unknown CY category"):
            shadow_class_cy("nonexistent")


# ======================================================================
# 6. Shadow obstruction tower amplitudes
# ======================================================================

class TestShadowTower:
    """Test genus-g shadow amplitudes F_g = kappa * A-hat coefficients."""

    def test_f1_formula(self):
        """F_1 = kappa/24 (first Bernoulli number contribution)."""
        assert shadow_amplitude_genus1(Fraction(1)) == Fraction(1, 24)
        assert shadow_amplitude_genus1(Fraction(5)) == Fraction(5, 24)
        assert shadow_amplitude_genus1(Fraction(0)) == 0

    def test_f2_formula(self):
        """F_2 = 7 * kappa / 5760."""
        assert shadow_amplitude_genus2(Fraction(1)) == Fraction(7, 5760)
        assert shadow_amplitude_genus2(Fraction(5)) == Fraction(7, 1152)

    def test_f3_formula(self):
        """F_3 = 31 * kappa / 967680."""
        assert shadow_amplitude_genus3(Fraction(1)) == Fraction(31, 967680)

    def test_f1_k3xe(self):
        """F_1(K3 x E) = 5/24."""
        assert shadow_amplitude_genus1(Fraction(5)) == Fraction(5, 24)

    def test_f1_elliptic(self):
        """F_1(E) = 1/24."""
        assert shadow_amplitude_genus1(Fraction(1)) == Fraction(1, 24)

    def test_tower_positivity_positive_kappa(self):
        """F_g > 0 for all g when kappa > 0 (AP22: Bernoulli signs)."""
        tower = shadow_tower_scalar(Fraction(5), 5)
        for g in range(1, 6):
            assert tower[g] > 0, f"F_{g} should be positive for kappa > 0"

    def test_tower_linearity_in_kappa(self):
        """F_g(2*kappa) = 2 * F_g(kappa) (linearity at scalar level)."""
        tower1 = shadow_tower_scalar(Fraction(1), 5)
        tower2 = shadow_tower_scalar(Fraction(2), 5)
        for g in range(1, 6):
            assert tower2[g] == 2 * tower1[g], f"F_{g} not linear in kappa"

    def test_tower_vanishes_at_kappa_zero(self):
        """F_g = 0 for all g when kappa = 0 (uncurved algebra)."""
        tower = shadow_tower_scalar(Fraction(0), 5)
        for g in range(1, 6):
            assert tower[g] == 0

    def test_tower_monotone_decreasing(self):
        """|F_g| > |F_{g+1}| for kappa = 1 (A-hat coefficients decrease).

        The A-hat coefficients a_g decrease rapidly:
        a_1 = 1/24, a_2 = 7/5760, a_3 = 31/967680, ...
        Each is much smaller than the previous.
        """
        tower = shadow_tower_scalar(Fraction(1), 5)
        for g in range(1, 5):
            assert tower[g] > tower[g + 1], (
                f"|F_{g}| = {tower[g]} should exceed |F_{g+1}| = {tower[g+1]}"
            )

    def test_f2_over_f1_ratio(self):
        """F_2/F_1 = 7/240 (independent of kappa).

        F_2/F_1 = (7/5760) / (1/24) = 7*24/5760 = 168/5760 = 7/240.
        """
        kappa = Fraction(5)
        f1 = shadow_amplitude_genus1(kappa)
        f2 = shadow_amplitude_genus2(kappa)
        assert f2 / f1 == Fraction(7, 240)


# ======================================================================
# 7. BCOV comparison
# ======================================================================

class TestBCOV:
    """Test BCOV holomorphic anomaly data."""

    def test_bcov_genus1_coefficient_quintic(self):
        """c_1^{BCOV}(quintic) = 31/3.

        c_1 = (3 + h^{1,1} - chi/12) / 2 = (3 + 1 - (-200/12)) / 2
            = (4 + 50/3) / 2 = (62/3) / 2 = 31/3.
        """
        c1 = bcov_genus1_coefficient(-200, 1)
        assert c1 == Fraction(31, 3)

    def test_bcov_genus1_coefficient_k3xe(self):
        """c_1^{BCOV}(K3 x E) = 12.

        c_1 = (3 + 21 - 0) / 2 = 24/2 = 12.
        """
        c1 = bcov_genus1_coefficient(0, 21)
        assert c1 == 12

    def test_bcov_quintic_data(self):
        """BCOV data for quintic is internally consistent."""
        data = bcov_quintic()
        assert data.chi == -200
        assert data.h11 == 1
        assert data.h21 == 101
        assert data.c1_bcov == Fraction(31, 3)

    def test_bcov_k3xe_data(self):
        """BCOV data for K3 x E: c_1 = 12, F_1 = 5/24."""
        data = bcov_k3_times_e()
        assert data.c1_bcov == 12
        assert data.f1_large_cx == Fraction(5, 24)

    def test_bcov_c1_formula_general(self):
        """The BCOV formula c_1 = (3 + h^{1,1} - chi/12)/2 for various CY3s."""
        # Self-mirror CY3 with h11 = h21 = 11, chi = 0
        c1 = bcov_genus1_coefficient(0, 11)
        assert c1 == Fraction(14, 2)  # = 7

        # Generic one-parameter model: h11 = 1
        c1_generic = bcov_genus1_coefficient(-200, 1)
        assert c1_generic == Fraction(31, 3)

    def test_bcov_c1_not_equal_kappa(self):
        """c_1^{BCOV} != kappa in general. For K3xE: c_1 = 12, kappa = 5."""
        data = bcov_k3_times_e()
        k3e = chi_cy_k3_times_e()
        assert data.c1_bcov != k3e.kappa
        assert data.c1_bcov == 12
        assert k3e.kappa == 5


# ======================================================================
# 8. Spectral sequence
# ======================================================================

class TestSpectralSequence:
    """Test the HH-to-shadow spectral sequence."""

    def test_ss_genus1_k3_target(self):
        """E_2 page at genus 1 for K3: target F_1 = 2/24 = 1/12."""
        hkr = hkr_k3()
        ss = spectral_sequence_genus1(hkr, Fraction(2))
        assert ss.genus == 1
        assert ss.target == Fraction(2, 24)  # = 1/12

    def test_ss_genus1_quintic_target(self):
        """E_2 page at genus 1 for quintic: target F_1 = (-25/3)/24 = -25/72."""
        hkr = hkr_quintic()
        ss = spectral_sequence_genus1(hkr, Fraction(-25, 3))
        assert ss.target == Fraction(-25, 72)

    def test_ss_genus1_e2_has_hh0_at_q0(self):
        """E_2^{0,0} = dim HH_0 for the K3 case."""
        hkr = hkr_k3()
        ss = spectral_sequence_genus1(hkr, Fraction(2))
        assert ss.e2_entries[(0, 0)] == 22

    def test_ss_genus1_e2_has_hh0_at_q2(self):
        """E_2^{0,2} = dim HH_0 (tensor with H^2(M_1))."""
        hkr = hkr_k3()
        ss = spectral_sequence_genus1(hkr, Fraction(2))
        assert ss.e2_entries[(0, 2)] == 22

    def test_ss_genus2_target(self):
        """E_2 page at genus 2 for K3 x E: target F_2 = 7*5/5760."""
        hkr = hkr_k3_times_e()
        ss = spectral_sequence_genus2(hkr, Fraction(5))
        assert ss.genus == 2
        assert ss.target == Fraction(7, 1152)  # = 7*5/5760

    def test_ss_genus2_total_nonzero(self):
        """The E_2 page at genus 2 has nonzero total dimension."""
        hkr = hkr_k3_times_e()
        ss = spectral_sequence_genus2(hkr, Fraction(5))
        assert ss.total > 0


# ======================================================================
# 9. GW invariant comparison
# ======================================================================

class TestGWComparison:
    """Test comparison of shadow amplitudes with GW data."""

    def test_gw_k3xe_genus1(self):
        """K3 x E genus-1 comparison: F_1 = 5/24, PROVED."""
        comps = gw_comparison_k3_times_e()
        g1 = comps[0]
        assert g1.genus == 1
        assert g1.shadow_F_g == Fraction(5, 24)
        assert g1.match_status == "PROVED"

    def test_gw_k3xe_genus2(self):
        """K3 x E genus-2 comparison: F_2 = 7/1152, CONJECTURAL."""
        comps = gw_comparison_k3_times_e()
        g2 = comps[1]
        assert g2.genus == 2
        assert g2.shadow_F_g == Fraction(7, 1152)
        assert g2.match_status == "CONJECTURAL"

    def test_gw_quintic_conjectural(self):
        """Quintic GW comparison is CONJECTURAL."""
        comps = gw_comparison_quintic()
        assert len(comps) >= 1
        assert comps[0].match_status == "CONJECTURAL"

    def test_gw_k3xe_three_genera(self):
        """K3 x E comparison exists for 3 genera."""
        comps = gw_comparison_k3_times_e()
        assert len(comps) == 3
        genera = [c.genus for c in comps]
        assert genera == [1, 2, 3]


# ======================================================================
# 10. String theory comparison
# ======================================================================

class TestStringComparison:
    """Test comparison with topological string partition function."""

    def test_positive_kappa_positive_f(self):
        """For kappa > 0, all F_g > 0 (no alternating signs in A-hat(ix))."""
        result = topological_string_comparison(Fraction(5))
        assert result["all_F_g_positive"] is True

    def test_tower_values(self):
        """Shadow obstruction tower values are correct for kappa = 5."""
        result = topological_string_comparison(Fraction(5))
        assert abs(result["shadow_tower"][1] - 5 / 24) < 1e-15
        assert abs(result["shadow_tower"][2] - 7 * 5 / 5760) < 1e-15

    def test_convention_string(self):
        """Convention: g_s = hbar."""
        result = topological_string_comparison(Fraction(1))
        assert result["string_coupling"] == "g_s = hbar"


# ======================================================================
# 11. Resolved conifold
# ======================================================================

class TestResolvedConifold:
    """Test the resolved conifold (local CY3 model)."""

    def test_conifold_hodge(self):
        """Resolved conifold effective Hodge diamond has h^{1,1} = 1."""
        hd = resolved_conifold_hodge()
        assert hd.h(1, 1) == 1
        assert hd.n == 3

    def test_conifold_kappa_1(self):
        """kappa(conifold) = 1 from single compact cycle."""
        data = chi_cy_resolved_conifold()
        assert data.kappa == 1

    def test_conifold_shadow_tower(self):
        """Shadow obstruction tower for conifold matches rank-1 Heisenberg."""
        tower = shadow_tower_scalar(Fraction(1), 3)
        assert tower[1] == Fraction(1, 24)
        assert tower[2] == Fraction(7, 5760)


# ======================================================================
# 12. Cross-consistency checks
# ======================================================================

class TestCrossConsistency:
    """Cross-consistency between different computations."""

    def test_hkr_euler_matches_signed_chi_top(self):
        """Euler(HH_*) = (-1)^d * chi_top for all standard families.

        The sign rule for the HKR Euler characteristic:
          sum_n (-1)^n dim HH_n = (-1)^d * chi_top(X).
        """
        # K3 (d=2, even): euler_hh = chi_top = 24
        assert hkr_k3().euler_hh == 24
        # Elliptic (d=1, odd): euler_hh = -chi_top = 0 (chi_top = 0)
        assert hkr_elliptic().euler_hh == 0
        # Quintic (d=3, odd): euler_hh = -chi_top = -(-200) = 200
        assert hkr_quintic().euler_hh == 200
        # K3 x E (d=3, odd): euler_hh = -chi_top = 0 (chi_top = 0)
        assert hkr_k3_times_e().euler_hh == 0

    def test_chi_cy_matches_kappa_for_proved(self):
        """chi^CY = kappa for all proved cases."""
        proved = [chi_cy_point, chi_cy_elliptic, chi_cy_k3,
                  chi_cy_k3_times_e, chi_cy_resolved_conifold]
        for func in proved:
            data = func()
            assert data.match is True, f"Mismatch for {data.name}"

    def test_shadow_f1_from_chi_cy(self):
        """F_1 computed from chi^CY matches direct computation."""
        for func, expected_f1 in [(chi_cy_elliptic, Fraction(1, 24)),
                                   (chi_cy_k3, Fraction(2, 24)),
                                   (chi_cy_k3_times_e, Fraction(5, 24))]:
            data = func()
            f1 = shadow_amplitude_genus1(data.kappa)
            assert f1 == expected_f1, f"F_1 mismatch for {data.name}"

    def test_k3xe_weight_5_from_cy_euler(self):
        """kappa(K3 x E) = 5 consistent with cy_euler.py."""
        from compute.lib.cy_euler import kappa_k3_times_e as kappa_from_cy_euler
        assert kappa_from_cy_euler() == 5
        assert chi_cy_k3_times_e().kappa == 5

    def test_bcov_c1_positive_for_standard_cy3(self):
        """c_1^{BCOV} > 0 for all standard CY3s (physical requirement).

        c_1 = (3 + h^{1,1} - chi/12) / 2.
        For CY3s: chi <= 0 typically (quintic: -200), h^{1,1} >= 1.
        So 3 + h^{1,1} - chi/12 >= 3 + 1 + 0 = 4 > 0.
        """
        # Quintic
        assert bcov_genus1_coefficient(-200, 1) > 0
        # K3 x E
        assert bcov_genus1_coefficient(0, 21) > 0
        # Self-mirror chi = 0
        assert bcov_genus1_coefficient(0, 11) > 0

    def test_shadow_tower_first_three_values(self):
        """Verify F_1, F_2, F_3 for kappa = 1 against A-hat series."""
        tower = shadow_tower_scalar(Fraction(1), 3)
        assert tower[1] == Fraction(1, 24)
        assert tower[2] == Fraction(7, 5760)
        assert tower[3] == Fraction(31, 967680)

    def test_a_hat_coefficient_ratios(self):
        """Ratios between consecutive A-hat coefficients.

        a_2/a_1 = (7/5760) / (1/24) = 7/240.
        a_3/a_2 = (31/967680) / (7/5760) = 31*5760 / (7*967680) = 31/1176.

        Wait: 31 * 5760 = 178560. 7 * 967680 = 6773760. 178560/6773760 = 31/1176.
        Hmm: 6773760 / 178560 = 37.94... let me recompute.
        7 * 967680 = 6773760. 31 * 5760 = 178560. 178560 / 6773760 = 31 / (7*168)
        = 31/1176. Check: 1176 = 7 * 168.
        """
        a1 = Fraction(1, 24)
        a2 = Fraction(7, 5760)
        a3 = Fraction(31, 967680)
        assert a2 / a1 == Fraction(7, 240)
        assert a3 / a2 == Fraction(31 * 5760, 7 * 967680)

    def test_hkr_serre_duality(self):
        """HKR satisfies Serre duality: dim HH_n = dim HH_{-n} for CY d-folds.

        For CY d-fold: Serre functor S = [d], so HH_n(X) = HH_{-n}(X)^*.
        In particular, dim HH_n = dim HH_{-n}.
        """
        for hkr_func in [hkr_k3, hkr_elliptic, hkr_quintic]:
            hkr = hkr_func()
            all_n = set(hkr.hh.keys())
            for n in all_n:
                dim_n = hkr.hh.get(n, 0)
                dim_neg_n = hkr.hh.get(-n, 0)
                assert dim_n == dim_neg_n, (
                    f"Serre duality fails: HH_{n} = {dim_n} != HH_{-n} = {dim_neg_n}"
                )


# ======================================================================
# 13. Master verification
# ======================================================================

class TestMasterVerification:
    """Run the master verification suite."""

    def test_verify_all(self):
        """All internal consistency checks pass."""
        results = verify_all_cy_characteristics()
        for key, val in results.items():
            assert val is True, f"Verification failed: {key}"


# ======================================================================
# 14. Categorical trace: Tr_C on HH gives kappa
# ======================================================================

class TestCategoricalTrace:
    """Categorical trace computation for standard families."""

    def test_trace_vect_is_1(self):
        """Categorical dimension of Vect = 1."""
        assert categorical_trace_vect() == Fraction(1)

    def test_trace_db_elliptic_is_1(self):
        """kappa(D^b(E)) = 1."""
        assert categorical_trace_db_elliptic() == Fraction(1)

    def test_trace_db_k3_is_2(self):
        """kappa(D^b(K3)) = 2, NOT dim(HH_0)/2 = 11."""
        assert categorical_trace_db_k3() == Fraction(2)

    def test_half_hh0_k3_is_11_not_kappa(self):
        """dim(HH_0(K3))/2 = 22/2 = 11, which is NOT kappa = 2."""
        val = categorical_trace_half_hh0(k3_hodge())
        assert val == Fraction(11)
        assert val != chi_cy_k3().kappa

    def test_half_hh0_elliptic_coincidence(self):
        """For E: dim(HH_0)/2 = 1 = kappa (coincidence for CY1)."""
        val = categorical_trace_half_hh0(elliptic_curve_hodge())
        assert val == Fraction(1)
        assert val == chi_cy_elliptic().kappa  # happens to coincide

    def test_half_hh0_quintic_not_kappa(self):
        """For quintic: dim(HH_0)/2 = 102, far from kappa = -25/3."""
        val = categorical_trace_half_hh0(quintic_hodge())
        assert val == Fraction(102)
        assert val != chi_cy_quintic().kappa


# ======================================================================
# 15. Quintic GW genus-0 data
# ======================================================================

class TestQuinticGW:
    """Genus-0 GW invariants n_0(d) for the quintic."""

    def test_n0_1_lines(self):
        """2875 lines on the quintic."""
        assert QUINTIC_GW_GENUS0[1] == 2875

    def test_n0_2_conics(self):
        """609250 conics on the quintic."""
        assert QUINTIC_GW_GENUS0[2] == 609250

    def test_n0_3_cubics(self):
        """317206375 twisted cubics."""
        assert QUINTIC_GW_GENUS0[3] == 317206375

    def test_n0_4(self):
        assert QUINTIC_GW_GENUS0[4] == 242467530000

    def test_n0_5(self):
        assert QUINTIC_GW_GENUS0[5] == 229305888887625

    def test_n0_rapidly_growing(self):
        """GW invariants grow rapidly with degree."""
        vals = [QUINTIC_GW_GENUS0[d] for d in range(1, 6)]
        for i in range(len(vals) - 1):
            assert vals[i + 1] > vals[i]

    def test_f1_const_map(self):
        """BCOV constant map coefficient = 25/6."""
        assert QUINTIC_F1_CONST_MAP == Fraction(25, 6)

    def test_quintic_genus0_data_structure(self):
        data = quintic_genus0_gw_data()
        assert data["n_0_1"] == 2875
        assert data["n_0_2"] == 609250
        assert data["chi_top"] == -200


# ======================================================================
# 16. Hodge-to-kappa formulas
# ======================================================================

class TestHodgeToKappa:
    """Various kappa formulas from Hodge data."""

    def test_k3_fibration_standard(self):
        """(chi(K3) - 4) / 4 = (24 - 4) / 4 = 5."""
        assert kappa_from_k3_fibration(24) == Fraction(5)

    def test_k3_fibration_matches_chi_cy(self):
        """K3 fibration formula matches chi^CY(K3 x E)."""
        assert kappa_from_k3_fibration() == chi_cy_k3_times_e().kappa

    def test_k3_fibration_hypothetical(self):
        """Hypothetical K3 with chi=16: (16-4)/4 = 3."""
        assert kappa_from_k3_fibration(16) == Fraction(3)

    def test_arithmetic_genus_k3(self):
        """chi(O_{K3}) = 2 for K3."""
        assert kappa_from_arithmetic_genus_cy2(k3_hodge()) == Fraction(2)

    def test_arithmetic_genus_matches_kappa(self):
        """chi(O_{K3}) = kappa(K3)."""
        assert kappa_from_arithmetic_genus_cy2(k3_hodge()) == chi_cy_k3().kappa

    def test_conjectural_cy3_quintic(self):
        """chi_top/24 = -200/24 = -25/3 for quintic."""
        assert kappa_conjectural_cy3(-200) == Fraction(-25, 3)

    def test_conjectural_cy3_fails_for_k3xe(self):
        """chi_top/24 = 0/24 = 0 for K3 x E, but kappa = 5. Formula fails."""
        assert kappa_conjectural_cy3(0) == Fraction(0)
        assert kappa_conjectural_cy3(0) != chi_cy_k3_times_e().kappa

    def test_arithmetic_genus_requires_surface(self):
        """Formula should reject non-surfaces."""
        with pytest.raises(AssertionError):
            kappa_from_arithmetic_genus_cy2(quintic_hodge())


# ======================================================================
# 17. Direct sum additivity
# ======================================================================

class TestDirectSumAdditivity:
    """kappa is additive for direct sums of independent chiral algebras."""

    def test_direct_sum_basic(self):
        assert kappa_additive_for_direct_sum(Fraction(3), Fraction(7)) == Fraction(10)

    def test_direct_sum_zero(self):
        assert kappa_additive_for_direct_sum(Fraction(0), Fraction(5)) == Fraction(5)

    def test_direct_sum_negative(self):
        assert kappa_additive_for_direct_sum(Fraction(-1), Fraction(3)) == Fraction(2)

    def test_direct_sum_fractions(self):
        assert kappa_additive_for_direct_sum(
            Fraction(1, 3), Fraction(2, 3)) == Fraction(1)

    def test_direct_sum_commutative(self):
        k1, k2 = Fraction(5), Fraction(3)
        assert kappa_additive_for_direct_sum(k1, k2) == \
               kappa_additive_for_direct_sum(k2, k1)


# ======================================================================
# 18. A-hat coefficient verification
# ======================================================================

class TestAHatCoefficients:
    """Verify the A-hat genus coefficients used in the shadow obstruction tower."""

    def test_a1_exact(self):
        assert A_HAT_COEFFICIENTS[1] == Fraction(1, 24)

    def test_a2_exact(self):
        assert A_HAT_COEFFICIENTS[2] == Fraction(7, 5760)

    def test_a3_exact(self):
        assert A_HAT_COEFFICIENTS[3] == Fraction(31, 967680)

    def test_a4_exact(self):
        assert A_HAT_COEFFICIENTS[4] == Fraction(127, 154828800)

    def test_a5_exact(self):
        assert A_HAT_COEFFICIENTS[5] == Fraction(73, 3503554560)

    def test_all_positive(self):
        """AP22: all A-hat coefficients after i-rotation are positive."""
        for g, coeff in A_HAT_COEFFICIENTS.items():
            assert coeff > 0, f"A-hat coeff at g={g} not positive"

    def test_strictly_decreasing(self):
        """Coefficients decrease: a_1 > a_2 > a_3 > a_4 > a_5."""
        for g in range(1, 5):
            assert A_HAT_COEFFICIENTS[g] > A_HAT_COEFFICIENTS[g + 1]

    def test_invalid_genus_raises(self):
        with pytest.raises(ValueError, match="genus must be >= 1"):
            shadow_amplitude_genus_g(Fraction(1), 0)

    def test_high_genus_raises(self):
        with pytest.raises(ValueError, match="not tabulated"):
            shadow_amplitude_genus_g(Fraction(1), 10)

    def test_linearity_in_kappa(self):
        """F_g(2*kappa) = 2 * F_g(kappa) for each g."""
        k = Fraction(7)
        for g in range(1, 6):
            assert shadow_amplitude_genus_g(2 * k, g) == 2 * shadow_amplitude_genus_g(k, g)
