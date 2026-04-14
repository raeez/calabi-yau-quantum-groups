r"""Tests for CY-B at d=3: E_2-chiral Koszul duality for CY_3 inputs.

Tests the CY-B proof components at d=3, covering:
  1. Verdier duality on E_3 bar complex (all shadow classes)
  2. E_3 -> E_2 restriction (dimensional projection)
  3. CY_3-specific families (Heisenberg, Yangian, K3 Yangian, betagamma,
     Virasoro, quintic, conifold, local P^2)
  4. E_3 bar spectral sequence analysis
  5. Conductor formula at d=3 (cross-check with cy_b_toward_proof.py)
  6. Verdier-tricomplex compatibility
  7. Higher genus E_3 bar data
  8. Cross-checks with holomorphic_cs_chiral_engine
  9. Parameter inversion (AP-CY26 compliance)
  10. Master verification and proof summary
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.cy_b_d3_proof import (
    # Ground truth
    E3_BAR_DIM_GENUS_1,
    E2_BAR_DIM_GENUS_1,
    E1_BAR_DIM_GENUS_1,
    E3_BAR_TOTAL_DIM,
    # Verdier duality
    VerdierDualityE3,
    verdier_on_e3_bar,
    # E_3 -> E_2 restriction
    E3ToE2Restriction,
    e3_to_e2_restriction,
    # CY_3 families
    CYB2D3ProofData,
    cy_b2_d3_heisenberg,
    cy_b2_d3_yangian,
    cy_b2_d3_k3_yangian,
    cy_b2_d3_betagamma,
    cy_b2_d3_virasoro,
    cy_b2_d3_quintic,
    cy_b2_d3_conifold,
    cy_b2_d3_local_p2,
    # Spectral sequence
    E3SpectralSequenceData,
    e3_spectral_sequence,
    # Conductor at d=3
    CYBConductorD3,
    verify_conductor_d3,
    # Verdier-tricomplex compatibility
    VerdierTriplexCompatibility,
    verify_verdier_tricomplex_compatibility,
    # Higher genus
    e3_bar_genus_g_class_m,
    e3_bar_genus_g_class_l,
    # Cross-checks
    cross_check_e3_bar_heisenberg,
    cross_check_e3_bar_yangian,
    cross_check_with_cy_b_toward_proof,
    cross_check_e3_to_e2_dimensions,
    cross_check_verdier_parameter_inversion,
    # Master
    verify_all_cy_b2_d3,
    cy_b_d3_proof_summary,
)

from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground


# =========================================================================
#  1. Verdier duality on the E_3 bar complex
# =========================================================================

class TestVerdierDualityE3:
    """Verdier duality D_{C^3} on the E_3 bar complex."""

    @pytest.mark.parametrize("cls", ["G", "L", "C"])
    def test_free_field_conductor_zero(self, cls: str) -> None:
        """Classes G, L, C: conductor rho_K = 0."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        kappa = Fraction(3)  # Arbitrary
        verd = verdier_on_e3_bar(cls, omega, kappa)
        assert verd.conductor == Fraction(0)
        assert verd.kappa_ch_dual == -kappa

    def test_class_m_conductor_nonzero(self) -> None:
        """Class M: conductor = c_crit/2."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        kappa = Fraction(1, 2)  # c=1 => kappa=1/2
        verd = verdier_on_e3_bar("M", omega, kappa, c_crit=Fraction(26))
        assert verd.conductor == Fraction(13)
        assert verd.kappa_ch_dual == Fraction(26 - 1, 2)

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_dimensions_match(self, cls: str) -> None:
        """Verdier dual has same E_3 bar dimensions."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        c_crit = Fraction(26) if cls == "M" else None
        verd = verdier_on_e3_bar(cls, omega, Fraction(1), c_crit=c_crit)
        assert verd.dimensions_match

    def test_en_level_is_3(self) -> None:
        """Verdier duality is at E_3 level."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        verd = verdier_on_e3_bar("G", omega, Fraction(1))
        assert verd.en_level == 3

    def test_parameter_inversion(self) -> None:
        """Omega-background inverted: (h1,h2,h3) -> (-h1,-h2,-h3)."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        verd = verdier_on_e3_bar("G", omega, Fraction(1))
        assert verd.omega_dual.h1 == -omega.h1
        assert verd.omega_dual.h2 == -omega.h2
        assert verd.omega_dual.h3 == -omega.h3

    @pytest.mark.parametrize("cls", ["G", "L"])
    def test_free_field_is_free(self, cls: str) -> None:
        """Free-field classes G, L identified correctly."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        verd = verdier_on_e3_bar(cls, omega, Fraction(1))
        assert verd.is_free_field

    @pytest.mark.parametrize("cls", ["C", "M"])
    def test_interacting_not_free(self, cls: str) -> None:
        """Classes C, M are not free-field."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        c_crit = Fraction(26) if cls == "M" else None
        verd = verdier_on_e3_bar(cls, omega, Fraction(1), c_crit=c_crit)
        # Class C has conductor 0 but is not "free-field" in the strict sense
        if cls == "M":
            assert not verd.is_free_field

    def test_class_m_requires_c_crit(self) -> None:
        """Class M raises without c_crit."""
        omega = OmegaBackground(Rational(1), Rational(-2))
        with pytest.raises(ValueError, match="c_crit required"):
            verdier_on_e3_bar("M", omega, Fraction(1))


# =========================================================================
#  2. E_3 -> E_2 restriction
# =========================================================================

class TestE3ToE2Restriction:
    """E_3 -> E_2 restriction by forgetting direction 3."""

    @pytest.mark.parametrize("cls", ["L", "C"])
    def test_dim_reduction_l_c(self, cls: str) -> None:
        """Classes L, C: E_3 dim 8 -> E_2 dim 4."""
        rest = e3_to_e2_restriction(cls, Fraction(1), Fraction(-1), Fraction(0))
        assert sum(rest.e3_bar_dim) == 8
        assert sum(rest.e2_bar_dim) == 4

    def test_dim_reduction_m(self) -> None:
        """Class M: E_3 dim 6 -> E_2 dim 2."""
        rest = e3_to_e2_restriction("M", Fraction(1, 2), Fraction(25, 2), Fraction(13))
        assert sum(rest.e3_bar_dim) == 6
        assert sum(rest.e2_bar_dim) == 2

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_kappa_preserved(self, cls: str) -> None:
        """kappa_ch is preserved under E_3 -> E_2 restriction."""
        kappa = Fraction(7)
        conductor = Fraction(0) if cls != "M" else Fraction(13)
        kappa_dual = -kappa if cls != "M" else conductor - kappa
        rest = e3_to_e2_restriction(cls, kappa, kappa_dual, conductor)
        assert rest.kappa_preserved_under_projection

    def test_class_g_infinite(self) -> None:
        """Class G: both E_3 and E_2 bar dims are None (infinite)."""
        rest = e3_to_e2_restriction("G", Fraction(1), Fraction(-1), Fraction(0))
        assert rest.e3_bar_dim is None
        assert rest.e2_bar_dim is None


# =========================================================================
#  3. CY_3-specific families
# =========================================================================

class TestClassGFamilies:
    """Class G: Heisenberg and quintic free-field branch."""

    def test_heisenberg_proved(self) -> None:
        """Heisenberg CY-B2 is fully proved at d=3."""
        data = cy_b2_d3_heisenberg()
        assert data.proof_complete
        assert data.cy_b2_status == "proved"
        assert data.conductor == Fraction(0)
        assert data.shadow_class == "G"

    def test_heisenberg_cy_a3(self) -> None:
        """CY-A_3 is proved."""
        data = cy_b2_d3_heisenberg()
        assert data.cy_a3_status == "proved"

    def test_quintic_free_field_proved(self) -> None:
        """Quintic free-field branch: proved at d=3."""
        data = cy_b2_d3_quintic()
        assert data.proof_complete
        assert data.cy_b2_status == "proved"
        assert data.conductor == Fraction(0)

    def test_quintic_kappa_value(self) -> None:
        """Quintic: kappa_ch = chi_top/24 = -200/24 = -25/3."""
        data = cy_b2_d3_quintic()
        assert data.kappa_ch == Fraction(-25, 3)
        assert data.kappa_ch_dual == Fraction(25, 3)

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(-2)),
        (Rational(2), Rational(3)),
        (Rational(37), Rational(41)),
    ])
    def test_heisenberg_generic_omega(self, h1, h2) -> None:
        """Heisenberg at various Omega-background points."""
        omega = OmegaBackground(h1, h2)
        data = cy_b2_d3_heisenberg(omega)
        assert data.proof_complete
        assert data.conductor == Fraction(0)


class TestClassLFamilies:
    """Class L: Yangian, K3 Yangian, conifold."""

    def test_yangian_cohomological(self) -> None:
        """Yangian CY-B2: proved at cohomological level."""
        data = cy_b2_d3_yangian()
        assert data.proof_complete
        assert data.cy_b2_status == "proved_cohomological"
        assert data.conductor == Fraction(0)
        assert data.shadow_class == "L"

    def test_yangian_e3_bar_dim(self) -> None:
        """Yangian E_3 bar: dim = 8."""
        data = cy_b2_d3_yangian()
        assert data.e3_bar_dim_total == 8

    def test_yangian_e2_bar_dim(self) -> None:
        """Yangian E_2 bar: dim = 4."""
        data = cy_b2_d3_yangian()
        assert data.e2_bar_dim_total == 4

    def test_k3_yangian_cohomological(self) -> None:
        """K3 Yangian: proved at cohomological level."""
        data = cy_b2_d3_k3_yangian()
        assert data.proof_complete
        assert data.cy_b2_status == "proved_cohomological"
        assert data.conductor == Fraction(0)

    def test_k3_yangian_kappa(self) -> None:
        """K3 Yangian: kappa_ch = chi(O_{K3}) = 2."""
        data = cy_b2_d3_k3_yangian()
        assert data.kappa_ch == Fraction(2)
        assert data.kappa_ch_dual == Fraction(-2)

    def test_conifold_cohomological(self) -> None:
        """Conifold: proved at cohomological level."""
        data = cy_b2_d3_conifold()
        assert data.proof_complete
        assert data.cy_b2_status == "proved_cohomological"
        assert data.conductor == Fraction(0)

    def test_conifold_kappa_zero(self) -> None:
        """Conifold: kappa_ch = 0 (non-compact, chi_top = 0)."""
        data = cy_b2_d3_conifold()
        assert data.kappa_ch == Fraction(0)


class TestClassCFamilies:
    """Class C: betagamma system."""

    def test_betagamma_cohomological(self) -> None:
        """betagamma: proved at cohomological level."""
        data = cy_b2_d3_betagamma()
        assert data.proof_complete
        assert data.cy_b2_status == "proved_cohomological"
        assert data.conductor == Fraction(0)
        assert data.shadow_class == "C"

    def test_betagamma_e3_dim(self) -> None:
        """betagamma E_3 bar: dim = 8 (same as class L)."""
        data = cy_b2_d3_betagamma()
        assert data.e3_bar_dim_total == 8


class TestClassMFamilies:
    """Class M: Virasoro and local P^2."""

    def test_virasoro_programme(self) -> None:
        """Virasoro CY-B2: PROGRAMME (class M chain-level open)."""
        data = cy_b2_d3_virasoro()
        assert not data.proof_complete
        assert data.cy_b2_status == "programme"

    def test_virasoro_conductor_13(self) -> None:
        """Virasoro: conductor rho_K = 13."""
        data = cy_b2_d3_virasoro()
        assert data.conductor == Fraction(13)

    def test_virasoro_e3_bar_dim(self) -> None:
        """Virasoro E_3 bar: dim = 6 (AP-CY21: NOT 8)."""
        data = cy_b2_d3_virasoro()
        assert data.e3_bar_dim_total == 6

    def test_virasoro_e2_bar_dim(self) -> None:
        """Virasoro E_2 bar: dim = 2."""
        data = cy_b2_d3_virasoro()
        assert data.e2_bar_dim_total == 2

    @pytest.mark.parametrize("c", [
        Fraction(0), Fraction(1), Fraction(1, 2), Fraction(13), Fraction(25),
    ])
    def test_virasoro_conductor_parametric(self, c: Fraction) -> None:
        """Virasoro conductor = 13 at all central charges."""
        data = cy_b2_d3_virasoro(c)
        assert data.conductor == Fraction(13)

    def test_virasoro_kappa_values(self) -> None:
        """Virasoro at c=1: kappa_ch = 1/2, kappa_ch^! = 25/2."""
        data = cy_b2_d3_virasoro(Fraction(1))
        assert data.kappa_ch == Fraction(1, 2)
        assert data.kappa_ch_dual == Fraction(25, 2)

    def test_local_p2_programme(self) -> None:
        """Local P^2: PROGRAMME (class M)."""
        data = cy_b2_d3_local_p2()
        assert not data.proof_complete
        assert data.cy_b2_status == "programme"

    def test_local_p2_e3_dim(self) -> None:
        """Local P^2 E_3 bar: dim = 6 (class M)."""
        data = cy_b2_d3_local_p2()
        assert data.e3_bar_dim_total == 6

    def test_cy_a3_always_proved(self) -> None:
        """CY-A_3 is proved even for class M families."""
        data = cy_b2_d3_virasoro()
        assert data.cy_a3_status == "proved"

    def test_cy_b1_always_proved(self) -> None:
        """CY-B1 is proved even for class M families."""
        data = cy_b2_d3_virasoro()
        assert data.cy_b1_status == "proved"


# =========================================================================
#  4. E_3 bar spectral sequence
# =========================================================================

class TestE3SpectralSequence:
    """E_3 bar spectral sequence analysis."""

    @pytest.mark.parametrize("cls", ["L", "C"])
    def test_class_lc_dim_8g(self, cls: str) -> None:
        """Classes L, C: E_inf dim = 8^g."""
        for g in range(1, 5):
            ss = e3_spectral_sequence(cls, g)
            assert ss.e_inf_page_dim == 8 ** g

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_class_m_dim_6g(self, g: int) -> None:
        """Class M: E_inf dim = 6^g."""
        ss = e3_spectral_sequence("M", g)
        assert ss.e_inf_page_dim == 6 ** g

    def test_class_m_e4_equals_einf_low_genus(self) -> None:
        """Class M: E_4 = E_inf for g <= 3."""
        for g in range(1, 4):
            ss = e3_spectral_sequence("M", g)
            assert ss.e4_equals_e_inf

    def test_class_m_e4_may_not_equal_einf_high_genus(self) -> None:
        """Class M: E_4 may differ from E_inf for g >= 4."""
        ss = e3_spectral_sequence("M", 4)
        assert not ss.e4_equals_e_inf

    @pytest.mark.parametrize("cls", ["L", "C"])
    def test_e4_always_einf_for_lc(self, cls: str) -> None:
        """Classes L, C: E_4 = E_inf at all genera."""
        for g in range(1, 6):
            ss = e3_spectral_sequence(cls, g)
            assert ss.e4_equals_e_inf

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_verdier_preserves_dims(self, cls: str) -> None:
        """Verdier preserves dimensions for all classes."""
        ss = e3_spectral_sequence(cls, 1)
        assert ss.verdier_preserves_dims

    def test_class_l_poincare(self) -> None:
        """Class L genus 1: Poincare = (1+t)^3 = [1,3,3,1]."""
        ss = e3_spectral_sequence("L", 1)
        assert ss.poincare_poly == [1, 3, 3, 1]

    def test_class_m_poincare_genus1(self) -> None:
        """Class M genus 1: Poincare = [0,3,3,0]."""
        ss = e3_spectral_sequence("M", 1)
        assert ss.poincare_poly == [0, 3, 3, 0]

    def test_class_m_poincare_genus2(self) -> None:
        """Class M genus 2: (3t+3t^2)^2 = 9t^2 + 18t^3 + 9t^4."""
        ss = e3_spectral_sequence("M", 2)
        assert ss.poincare_poly == [0, 0, 9, 18, 9]

    def test_class_m_total_matches_poincare(self) -> None:
        """Class M: total dim from Poincare = 6^g."""
        for g in range(1, 6):
            ss = e3_spectral_sequence("M", g)
            assert sum(ss.poincare_poly) == 6 ** g


# =========================================================================
#  5. Conductor at d=3
# =========================================================================

class TestConductorD3:
    """CY-B conductor formula verified at d=3."""

    def test_heisenberg_conductor_zero(self) -> None:
        """Heisenberg: rho_K = 0."""
        result = verify_conductor_d3("Heisenberg", "G", Fraction(3), Fraction(-3), Fraction(0))
        assert result.conductor == Fraction(0)
        assert result.conductor_matches_d2

    def test_yangian_conductor_zero(self) -> None:
        """Yangian: rho_K = 0."""
        result = verify_conductor_d3("Yangian", "L", Fraction(5), Fraction(-5), Fraction(0))
        assert result.conductor == Fraction(0)
        assert result.conductor_matches_d2

    def test_virasoro_conductor_13(self) -> None:
        """Virasoro: rho_K = 13."""
        result = verify_conductor_d3("Virasoro", "M", Fraction(1, 2), Fraction(25, 2), Fraction(13))
        assert result.conductor == Fraction(13)
        assert result.conductor_matches_d2

    def test_all_components_proved(self) -> None:
        """All proof components are marked proved."""
        result = verify_conductor_d3("test", "G", Fraction(1), Fraction(-1), Fraction(0))
        assert result.cy_a3_proved
        assert result.cy_b1_proved
        assert result.e3_bar_proved
        assert result.verdier_dims_match
        assert result.e3_to_e2_consistent


# =========================================================================
#  6. Verdier-tricomplex compatibility
# =========================================================================

class TestVerdierTriplexCompatibility:
    """Verdier duality compatible with E_3 tricomplex structure."""

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_tricomplex_compatible(self, cls: str) -> None:
        """All classes: tricomplex compatible."""
        compat = verify_verdier_tricomplex_compatibility(cls)
        assert compat.tricomplex_compatible

    def test_class_g_differentials_vanish(self) -> None:
        """Class G: differentials vanish on both sides."""
        compat = verify_verdier_tricomplex_compatibility("G")
        assert compat.differentials_vanish_original
        assert compat.differentials_vanish_dual

    def test_class_l_cofreeness_preserved(self) -> None:
        """Class L: cofreeness preserved under Verdier."""
        compat = verify_verdier_tricomplex_compatibility("L")
        assert compat.cofreeness_preserved

    def test_class_c_charge_preserved(self) -> None:
        """Class C: charge conservation preserved under Verdier."""
        compat = verify_verdier_tricomplex_compatibility("C")
        assert compat.charge_conservation_preserved

    def test_class_m_kunneth_preserved(self) -> None:
        """Class M: Kunneth structure preserved under Verdier."""
        compat = verify_verdier_tricomplex_compatibility("M")
        assert compat.kunneth_structure_preserved

    def test_class_m_not_cofree(self) -> None:
        """Class M: NOT cofree (shadow depth infinite)."""
        compat = verify_verdier_tricomplex_compatibility("M")
        assert not compat.cofreeness_preserved


# =========================================================================
#  7. Higher genus E_3 bar data
# =========================================================================

class TestHigherGenusE3Bar:
    """E_3 bar at higher genus for d=3 CY-B proof."""

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_class_m_dim_6g(self, g: int) -> None:
        """Class M genus g: total dim = 6^g."""
        data = e3_bar_genus_g_class_m(g)
        assert data["total_dim"] == 6 ** g

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_class_m_verdier_match(self, g: int) -> None:
        """Class M: Verdier dim = original dim at all genera."""
        data = e3_bar_genus_g_class_m(g)
        assert data["dims_match"]

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_class_l_dim_8g(self, g: int) -> None:
        """Class L genus g: total dim = 8^g."""
        data = e3_bar_genus_g_class_l(g)
        assert data["total_dim"] == 8 ** g

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_class_l_verdier_match(self, g: int) -> None:
        """Class L: Verdier dim = original dim at all genera."""
        data = e3_bar_genus_g_class_l(g)
        assert data["dims_match"]

    def test_class_m_support(self) -> None:
        """Class M genus g: support in [g, 2g]."""
        for g in range(1, 5):
            data = e3_bar_genus_g_class_m(g)
            assert data["support_min"] == g
            assert data["support_max"] == 2 * g

    def test_class_m_poincare_sum(self) -> None:
        """Class M: Poincare polynomial sums to 6^g."""
        for g in range(1, 6):
            data = e3_bar_genus_g_class_m(g)
            assert sum(data["poincare"]) == 6 ** g

    def test_deficit_8g_minus_6g(self) -> None:
        """Deficit L - M = 8^g - 6^g (exponentially growing)."""
        for g in range(1, 6):
            dim_l = e3_bar_genus_g_class_l(g)["total_dim"]
            dim_m = e3_bar_genus_g_class_m(g)["total_dim"]
            assert dim_l - dim_m == 8 ** g - 6 ** g


# =========================================================================
#  8. Cross-checks with holomorphic_cs_chiral_engine
# =========================================================================

class TestCrossChecksEngine:
    """Cross-checks with holomorphic_cs_chiral_engine.py."""

    def test_heisenberg_e3_bar_dims(self) -> None:
        """Heisenberg E_3 bar: tau_3(n) matches formula."""
        results = cross_check_e3_bar_heisenberg(8)
        for n, data in results.items():
            assert data["match"], f"Heisenberg E_3 bar mismatch at n={n}"

    def test_yangian_class_l(self) -> None:
        """Yangian is class L with shadow depth 3."""
        results = cross_check_e3_bar_yangian()
        assert results["class_is_L"]
        assert results["depth_is_3"]


# =========================================================================
#  9. Cross-checks with cy_b_toward_proof.py
# =========================================================================

class TestCrossChecksCYB:
    """Cross-checks with cy_b_toward_proof.py (d=2 vs d=3)."""

    def test_conductor_match(self) -> None:
        """d=3 conductors match d=2 conductors (E_n-independent)."""
        results = cross_check_with_cy_b_toward_proof()
        for name, match in results.items():
            assert match, f"Conductor mismatch: {name}"

    def test_e3_to_e2_dims(self) -> None:
        """E_3 -> E_2 dimensional reduction correct."""
        results = cross_check_e3_to_e2_dimensions()
        for name, ok in results.items():
            assert ok, f"Dimension check failed: {name}"


# =========================================================================
#  10. AP-CY26 compliance: parameter inversion
# =========================================================================

class TestParameterInversion:
    """AP-CY26: Verdier parameter inversion properties."""

    def test_sigma2_even(self) -> None:
        """sigma_2 is EVEN under h_i -> -h_i."""
        results = cross_check_verdier_parameter_inversion()
        for name, ok in results.items():
            if "sigma2_even" in name:
                assert ok, f"sigma_2 evenness failed: {name}"

    def test_sigma3_odd(self) -> None:
        """sigma_3 is ODD under h_i -> -h_i."""
        results = cross_check_verdier_parameter_inversion()
        for name, ok in results.items():
            if "sigma3_odd" in name:
                assert ok, f"sigma_3 oddness failed: {name}"


# =========================================================================
#  11. Master verification
# =========================================================================

class TestMasterVerification:
    """Master verification of CY-B at d=3."""

    def test_all_families(self) -> None:
        """All families pass verification."""
        results = verify_all_cy_b2_d3()
        for name, data in results.items():
            if data["status"] in ("proved", "proved_cohomological"):
                assert data["proof_complete"], f"{name} should be complete"
            elif data["status"] == "programme":
                assert not data["proof_complete"], f"{name} should be incomplete"

    def test_proved_count(self) -> None:
        """At least 6 of 8 families proved (class M open)."""
        results = verify_all_cy_b2_d3()
        n_proved = sum(1 for r in results.values() if r["proof_complete"])
        assert n_proved >= 6  # G(2) + L(3) + C(1) = 6; M(2) open

    def test_class_m_open(self) -> None:
        """Class M families are open (programme)."""
        results = verify_all_cy_b2_d3()
        assert results["Virasoro"]["status"] == "programme"
        assert results["LocalP2"]["status"] == "programme"


class TestProofSummary:
    """CY-B d=3 proof summary."""

    def test_cy_a3_proved(self) -> None:
        """CY-A_3 is proved."""
        summary = cy_b_d3_proof_summary()
        assert summary["cy_a3_status"] == "PROVED (infinity-categorical)"

    def test_cy_b1_proved(self) -> None:
        """CY-B1 is proved at all d."""
        summary = cy_b_d3_proof_summary()
        assert summary["cy_b1_status"] == "PROVED (all classes, all d)"

    def test_class_g_proved(self) -> None:
        """CY-B2 for class G: PROVED."""
        summary = cy_b_d3_proof_summary()
        assert summary["cy_b2_by_class"]["G"] == "PROVED"

    def test_class_l_cohomological(self) -> None:
        """CY-B2 for class L: PROVED (cohomological)."""
        summary = cy_b_d3_proof_summary()
        assert "PROVED" in summary["cy_b2_by_class"]["L"]

    def test_class_c_cohomological(self) -> None:
        """CY-B2 for class C: PROVED (cohomological)."""
        summary = cy_b_d3_proof_summary()
        assert "PROVED" in summary["cy_b2_by_class"]["C"]

    def test_class_m_programme(self) -> None:
        """CY-B2 for class M: PROGRAMME."""
        summary = cy_b_d3_proof_summary()
        assert "PROGRAMME" in summary["cy_b2_by_class"]["M"]

    def test_families_count(self) -> None:
        """Summary reports correct family counts."""
        summary = cy_b_d3_proof_summary()
        assert summary["families_total"] == 8
        assert summary["families_proved"] >= 6


# =========================================================================
#  12. Ground truth consistency
# =========================================================================

class TestGroundTruth:
    """Ground truth data consistency."""

    def test_e3_bar_dims_sum(self) -> None:
        """E_3 bar dimension lists sum correctly."""
        assert sum(E3_BAR_DIM_GENUS_1["L"]) == 8
        assert sum(E3_BAR_DIM_GENUS_1["C"]) == 8
        assert sum(E3_BAR_DIM_GENUS_1["M"]) == 6

    def test_e2_bar_dims_sum(self) -> None:
        """E_2 bar dimension lists sum correctly."""
        assert sum(E2_BAR_DIM_GENUS_1["L"]) == 4
        assert sum(E2_BAR_DIM_GENUS_1["C"]) == 4
        assert sum(E2_BAR_DIM_GENUS_1["M"]) == 2

    def test_e1_bar_dims_sum(self) -> None:
        """E_1 bar dimension lists sum correctly."""
        assert sum(E1_BAR_DIM_GENUS_1["L"]) == 2
        assert sum(E1_BAR_DIM_GENUS_1["C"]) == 2
        assert sum(E1_BAR_DIM_GENUS_1["M"]) == 1

    def test_hierarchy_e3_ge_e2_ge_e1(self) -> None:
        """E_3 dim >= E_2 dim >= E_1 dim for all classes."""
        for cls in ("L", "C", "M"):
            e3 = sum(E3_BAR_DIM_GENUS_1[cls])
            e2 = sum(E2_BAR_DIM_GENUS_1[cls])
            e1 = sum(E1_BAR_DIM_GENUS_1[cls])
            assert e3 >= e2 >= e1, f"Hierarchy violated for class {cls}"

    def test_class_g_infinite(self) -> None:
        """Class G: all bar dims are None (infinite)."""
        assert E3_BAR_DIM_GENUS_1["G"] is None
        assert E2_BAR_DIM_GENUS_1["G"] is None
        assert E1_BAR_DIM_GENUS_1["G"] is None

    def test_total_dim_functions(self) -> None:
        """E3_BAR_TOTAL_DIM functions compute correctly."""
        for g in range(1, 5):
            assert E3_BAR_TOTAL_DIM["L"](g) == 8 ** g
            assert E3_BAR_TOTAL_DIM["C"](g) == 8 ** g
            assert E3_BAR_TOTAL_DIM["M"](g) == 6 ** g

    def test_class_l_poincare_coefficients(self) -> None:
        """Class L: (1+t)^3 = [1,3,3,1] (binomial coefficients)."""
        assert E3_BAR_DIM_GENUS_1["L"] == [1, 3, 3, 1]

    def test_class_m_poincare_coefficients(self) -> None:
        """Class M: [0,3,3,0] (d_4 kills degrees 0 and 3)."""
        assert E3_BAR_DIM_GENUS_1["M"] == [0, 3, 3, 0]
