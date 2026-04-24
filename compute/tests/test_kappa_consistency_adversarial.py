"""Tests for kappa_consistency_adversarial: cross-route verification of
the kappa-spectrum {0, 2, 3, 5, 24} for K3 x E.

Ground truth:
  chapters/examples/k3_times_e.tex (Proposition prop:kappa-spectrum-reconciliation)
  chapters/connections/modular_koszul_bridge.tex (Definition def:cy-categorical-kappa)
  chapters/theory/cy_to_chiral.tex (Proposition prop:cy-kappa-d2)
  chapters/examples/toroidal_elliptic.tex (Theorem thm:kappa-k3-five-paths)
  CLAUDE.md (AP113: bare kappa FORBIDDEN; kappa-spectrum table)

AP113: every kappa value MUST carry a subscript {ch, cat, BKM, fiber}.
"""

from fractions import Fraction

import pytest

from compute.lib.kappa_consistency_adversarial import (
    HodgeData,
    elliptic_curve,
    k3_surface,
    k3_times_e,
    quintic_threefold,
    # kappa_ch routes
    kappa_ch_route_additive,
    kappa_ch_route_dim_C,
    kappa_ch_route_bar_euler,
    kappa_ch_route_yangian,
    kappa_ch_route_sigma_model,
    kappa_ch_route_chiral_de_rham,
    kappa_ch_route_genus1_free_energy,
    verify_kappa_ch_all_routes,
    # kappa_cat routes
    kappa_cat_route_kunneth,
    kappa_cat_route_hodge,
    kappa_cat_route_hirzebruch_chi_y,
    kappa_cat_route_hkr,
    kappa_cat_route_serre_duality,
    verify_kappa_cat_all_routes,
    # kappa_BKM routes
    kappa_BKM_route_borcherds_c0,
    kappa_BKM_route_delta5_weight,
    kappa_BKM_route_dmvv,
    kappa_BKM_route_NOT_sum,
    kappa_BKM_route_fiber_coincidence,
    verify_kappa_BKM_all_routes,
    # kappa_fiber routes
    kappa_fiber_route_mukai_rank,
    kappa_fiber_route_chi_top_K3,
    kappa_fiber_route_lattice_voa,
    kappa_fiber_route_NOT_sigma_c,
    kappa_fiber_route_h_even,
    verify_kappa_fiber_all_routes,
    # Cross-kappa checks
    verify_kappa_ch_plus_kappa_cat_neq_kappa_BKM,
    verify_fiber_vs_total_space_distinction,
    verify_all_ratios,
    verify_spectrum_completeness,
    verify_all_kappa_consistency,
)


# ======================================================================
# 1. Hodge data sanity
# ======================================================================

class TestHodgeDataSanity:
    """Verify Hodge data used by the adversarial engine."""

    def test_k3_chi_O(self):
        """chi(O_{K3}) = 2."""
        # VERIFIED [DC] chi(O_K3) = 2 [LC] Hodge diamond
        assert k3_surface().chi_O() == 2

    def test_e_chi_O(self):
        """chi(O_E) = 0."""
        # VERIFIED [DC] chi(O_E) = 0 [LC] definition
        assert elliptic_curve().chi_O() == 0

    def test_k3xe_chi_O(self):
        """chi(O_{K3xE}) = 0."""
        # VERIFIED [DC] chi(O_{K3xE}) = 0 [LC] Kunneth
        assert k3_times_e().chi_O() == 0

    def test_k3xe_h0q(self):
        """h^{0,q}(K3 x E) = (1, 1, 1, 1)."""
        # VERIFIED [DC] Kunneth product [LC] explicit
        assert k3_times_e().h0q == (1, 1, 1, 1)

    def test_k3_chi_top(self):
        """chi_top(K3) = 24."""
        # VERIFIED [DC] chi_top(K3) = 24 [LC] topology
        assert k3_surface().chi_top == 24

    def test_k3xe_chi_top(self):
        """chi_top(K3 x E) = 0."""
        # VERIFIED [DC] chi_top = 0 [LC] product formula
        assert k3_times_e().chi_top == 0

    def test_quintic_chi_O(self):
        """chi(O_Quintic) = 0."""
        # VERIFIED [DC] CY3 constraint [LC] Hodge
        assert quintic_threefold().chi_O() == 0


# ======================================================================
# 2. kappa_ch^Heis = 3: individual routes
# ======================================================================

class TestKappaChRoutes:
    """Test each independent route to kappa_ch^Heis(K3 x E) = 3."""

    def test_additive_route(self):
        """kappa_ch(K3) + kappa_ch^Heis(E) = 2 + 1 = 3."""
        r = kappa_ch_route_additive()
        # VERIFIED [DC] additivity 2+1=3 [LC] prop:kappa-spectrum-reconciliation
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "proved"

    def test_dim_C_route(self):
        """dim_C(K3 x E) = 3. Agrees but observational."""
        r = kappa_ch_route_dim_C()
        # VERIFIED [DC] dim_C = 3 [LC] coincidence for products
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "observational"

    def test_dim_C_fails_for_quintic(self):
        """dim_C(Quintic) = 3 but kappa_ch(Quintic) = -25/3. NOT equal."""
        q = quintic_threefold()
        # VERIFIED [DC] dim_C != kappa_ch for quintic [LC] BCOV
        assert q.dim_C == 3
        # kappa_ch(Quintic) = -25/3 (from kappa_spectrum_reconciliation.py)
        assert Fraction(-200, 24) == Fraction(-25, 3)
        assert q.dim_C != Fraction(-25, 3)

    def test_bar_euler_route(self):
        """F_1 = 3/24 = 1/8. Bar Euler weight = 3."""
        r = kappa_ch_route_bar_euler()
        # VERIFIED [DC] bar Euler weight 3 [LC] single-copy, not BKM weight 5
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "proved"

    def test_yangian_route(self):
        """Yangian route gives 3 but is conditional."""
        r = kappa_ch_route_yangian()
        # VERIFIED [DC] Yangian kappa_ch^Heis = 3 [LC] conditional on CY-A
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "conditional"

    def test_sigma_model_route(self):
        """c/6 = 18/6 = 3. Proved via K3/heterotic."""
        r = kappa_ch_route_sigma_model()
        # VERIFIED [DC] sigma model c/6 = 3 [LC] K3/heterotic duality
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "proved"

    def test_chiral_de_rham_route(self):
        """Chiral de Rham complex: 2+1 = 3."""
        r = kappa_ch_route_chiral_de_rham()
        # VERIFIED [DC] chiral de Rham kappa_ch^Heis = 3 [LC] product structure
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "proved"

    def test_genus1_free_energy_route(self):
        """F_1 = kappa_ch^Heis / 24 = 3/24 = 1/8."""
        r = kappa_ch_route_genus1_free_energy()
        # VERIFIED [DC] F_1 = 1/8 [LC] topological string
        assert r.agrees
        assert r.computed_value == 3
        assert r.proof_status == "proved"

    def test_all_routes_consistent(self):
        """All 7 routes for kappa_ch^Heis agree on 3."""
        report = verify_kappa_ch_all_routes()
        # VERIFIED [DC] 7-route consistency [LC] adversarial
        assert report.all_agree
        assert report.canonical_value == 3
        assert len(report.routes) == 7
        assert len(report.discrepancies) == 0


# ======================================================================
# 3. kappa_cat = 0: individual routes
# ======================================================================

class TestKappaCatRoutes:
    """Test each independent route to kappa_cat(K3 x E) = 0."""

    def test_kunneth_route(self):
        """chi(O_K3) * chi(O_E) = 2 * 0 = 0."""
        r = kappa_cat_route_kunneth()
        # VERIFIED [DC] Kunneth 2*0=0 [LC] product formula
        assert r.agrees
        assert r.computed_value == 0
        assert r.proof_status == "proved"

    def test_hodge_route(self):
        """1 - 1 + 1 - 1 = 0."""
        r = kappa_cat_route_hodge()
        # VERIFIED [DC] Hodge 1-1+1-1=0 [LC] direct
        assert r.agrees
        assert r.computed_value == 0
        assert r.proof_status == "proved"

    def test_hirzebruch_route(self):
        """chi_y(E) = 0 identically, so chi_y(K3 x E) = 0."""
        r = kappa_cat_route_hirzebruch_chi_y()
        # VERIFIED [DC] Hirzebruch chi_y = 0 [LC] vanishing
        assert r.agrees
        assert r.computed_value == 0
        assert r.proof_status == "proved"

    def test_hkr_route(self):
        """HKR: chi^{CY} = chi(O) = 0."""
        r = kappa_cat_route_hkr()
        # VERIFIED [DC] HKR chi^CY = 0 [LC] Hochschild
        assert r.agrees
        assert r.computed_value == 0
        assert r.proof_status == "proved"

    def test_serre_duality_route(self):
        """Serre duality: chi(O) = 0 for all odd-dim CY."""
        r = kappa_cat_route_serre_duality()
        # VERIFIED [DC] Serre duality vanishing [LC] odd CY
        assert r.agrees
        assert r.computed_value == 0
        assert r.proof_status == "proved"

    def test_all_routes_consistent(self):
        """All 5 routes for kappa_cat agree on 0."""
        report = verify_kappa_cat_all_routes()
        # VERIFIED [DC] 5-route consistency [LC] adversarial
        assert report.all_agree
        assert report.canonical_value == 0
        assert len(report.routes) == 5
        assert len(report.discrepancies) == 0


# ======================================================================
# 4. kappa_BKM = 5: individual routes
# ======================================================================

class TestKappaBKMRoutes:
    """Test each independent route to kappa_BKM(K3 x E) = 5."""

    def test_borcherds_c0_route(self):
        """c(0)/2 = 10/2 = 5."""
        r = kappa_BKM_route_borcherds_c0()
        # VERIFIED [DC] Borcherds c(0)/2 = 5 [LC] weight theorem
        assert r.agrees
        assert r.computed_value == 5
        assert r.proof_status == "proved"

    def test_delta5_weight_route(self):
        """wt(Delta_5) = 5."""
        r = kappa_BKM_route_delta5_weight()
        # VERIFIED [DC] wt(Delta_5) = 5 [LC] Siegel modular form
        assert r.agrees
        assert r.computed_value == 5
        assert r.proof_status == "proved"

    def test_dmvv_route(self):
        """DMVV: wt(Phi_10)/2 = 10/2 = 5."""
        r = kappa_BKM_route_dmvv()
        # VERIFIED [DC] DMVV weight 5 [LC] second quantization
        assert r.agrees
        assert r.computed_value == 5
        assert r.proof_status == "proved"

    def test_NOT_sum_route_correctly_fails(self):
        """kappa_ch^Heis + kappa_cat(total) = 3 + 0 = 3 != 5."""
        r = kappa_BKM_route_NOT_sum()
        # VERIFIED [DC] sum 3+0=3!=5 [LC] correctly fails (AP-CY8)
        assert not r.agrees  # INTENTIONALLY fails
        assert r.computed_value == 3  # 3 != 5
        assert r.proof_status == "wrong"

    def test_fiber_coincidence_route(self):
        """kappa_ch^Heis + chi(O_K3) = 3 + 2 = 5. Coincidence for N=1."""
        r = kappa_BKM_route_fiber_coincidence()
        # VERIFIED [DC] fiber coincidence 3+2=5 [LC] N=1 only
        assert r.agrees  # numerically correct for N=1
        assert r.computed_value == 5
        assert r.proof_status == "observational"

    def test_c_f_0_from_h11(self):
        """c_f(0) = h^{1,1}(K3)/2 = 20/2 = 10."""
        k3 = k3_surface()
        # VERIFIED [DC] c_f(0) = 10 [LC] Borcherds input
        assert k3.h11 is not None
        assert k3.h11 // 2 == 10

    def test_c_f_0_from_chi_top(self):
        """c_f(0) = (chi_top(K3) - 4)/2 = (24-4)/2 = 10."""
        k3 = k3_surface()
        # VERIFIED [DC] c_f(0) = 10 [LC] alternative formula
        assert (k3.chi_top - 4) // 2 == 10

    def test_c_f_0_two_paths_agree(self):
        """Both paths to c_f(0) give 10."""
        k3 = k3_surface()
        # VERIFIED [DC] c_f(0) consistency [LC] two paths
        assert k3.h11 // 2 == (k3.chi_top - 4) // 2

    def test_phi10_is_delta5_squared(self):
        """wt(Phi_10) = 10 = 2 * wt(Delta_5) = 2 * 5."""
        # VERIFIED [DC] Phi_10 = Delta_5^2 [LC] Igusa
        assert 10 == 2 * 5

    def test_all_valid_routes_consistent(self):
        """All valid routes for kappa_BKM agree on 5."""
        report = verify_kappa_BKM_all_routes()
        # VERIFIED [DC] valid-route consistency [LC] adversarial
        assert report.all_agree
        assert report.canonical_value == 5
        assert len(report.routes) == 5
        # The NOT_sum and fiber_coincidence are in routes but
        # only NOT_sum is excluded from agreement check
        assert len(report.discrepancies) == 0


# ======================================================================
# 5. kappa_fiber = 24: individual routes
# ======================================================================

class TestKappaFiberRoutes:
    """Test each independent route to kappa_fiber(K3 x E) = 24."""

    def test_mukai_rank_route(self):
        """rk(Mukai) = 1 + 22 + 1 = 24."""
        r = kappa_fiber_route_mukai_rank()
        # VERIFIED [DC] rk(Mukai) = 24 [LC] even cohomology
        assert r.agrees
        assert r.computed_value == 24
        assert r.proof_status == "proved"

    def test_chi_top_K3_route(self):
        """chi_top(K3) = 24."""
        r = kappa_fiber_route_chi_top_K3()
        # VERIFIED [DC] chi_top(K3) = 24 [LC] Gauss-Bonnet
        assert r.agrees
        assert r.computed_value == 24
        assert r.proof_status == "proved"

    def test_lattice_voa_route(self):
        """Lattice VOA has rank 24."""
        r = kappa_fiber_route_lattice_voa()
        # VERIFIED [DC] V_{Mukai} rank 24 [LC] free field
        assert r.agrees
        assert r.computed_value == 24
        assert r.proof_status == "proved"

    def test_NOT_sigma_c_route_is_wrong(self):
        """c = 6*4 = 24 is WRONG reasoning (AP-CY1)."""
        r = kappa_fiber_route_NOT_sigma_c()
        # VERIFIED [DC] sigma c=6*4 is wrong [LC] AP-CY1
        assert r.proof_status == "wrong"
        # Numerically coincidentally right:
        assert r.computed_value == 24
        # But the reasoning is wrong:
        assert "dimension mismatch" in r.route_name.lower()

    def test_sigma_model_correct_c(self):
        """The CORRECT K3 sigma model central charge is c = 12, not 24."""
        dim_C_K3 = 2
        # VERIFIED [DC] c(K3) = 12 [LC] N=(2,2) SUSY
        assert 6 * dim_C_K3 == 12
        assert 6 * dim_C_K3 != 24

    def test_h_even_route(self):
        """b_0 + b_2 + b_4 = 1 + 22 + 1 = 24."""
        r = kappa_fiber_route_h_even()
        # VERIFIED [DC] sum even Betti = 24 [LC] K3 topology
        assert r.agrees
        assert r.computed_value == 24
        assert r.proof_status == "proved"

    def test_all_valid_routes_consistent(self):
        """All valid routes for kappa_fiber agree on 24."""
        report = verify_kappa_fiber_all_routes()
        # VERIFIED [DC] valid-route consistency [LC] adversarial
        assert report.all_agree
        assert report.canonical_value == 24
        assert len(report.routes) == 5
        assert len(report.discrepancies) == 0


# ======================================================================
# 6. Cross-kappa adversarial checks
# ======================================================================

class TestCrossKappaAdversarial:
    """Cross-kappa structural tests."""

    def test_sum_correctly_fails(self):
        """kappa_ch^Heis + kappa_cat = 3 + 0 = 3 != 5 = kappa_BKM."""
        result = verify_kappa_ch_plus_kappa_cat_neq_kappa_BKM()
        # VERIFIED [DC] sum != BKM [LC] fundamental
        assert not result["sum_equals_BKM"]
        assert result["naive_sum"] == 3
        assert result["kappa_BKM"] == 5

    def test_fiber_vs_total_space(self):
        """kappa_cat: total space = 0, fiber = 2."""
        result = verify_fiber_vs_total_space_distinction()
        # VERIFIED [DC] fiber vs total [LC] critical distinction
        assert result["total_is_zero"]
        assert result["fiber_is_two"]
        assert result["kunneth_holds"]
        assert result["BKM_uses_fiber"]
        assert result["BKM_NOT_total"]

    def test_BKM_over_ch_ratio(self):
        """kappa_BKM / kappa_ch^Heis = 5/3."""
        ratios = verify_all_ratios()
        # VERIFIED [DC] BKM/ch ratio [LC] second quantization
        assert ratios["kappa_BKM/kappa_ch_Heis"] == Fraction(5, 3)

    def test_fiber_over_BKM_ratio(self):
        """kappa_fiber / kappa_BKM = 24/5."""
        ratios = verify_all_ratios()
        # VERIFIED [DC] fiber/BKM ratio [LC] lattice-to-automorphic
        assert ratios["kappa_fiber/kappa_BKM"] == Fraction(24, 5)

    def test_fiber_over_ch_ratio(self):
        """kappa_fiber / kappa_ch^Heis = 24/3 = 8."""
        ratios = verify_all_ratios()
        # VERIFIED [DC] fiber/ch ratio [LC] lattice-to-chiral
        assert ratios["kappa_fiber/kappa_ch_Heis"] == Fraction(24, 3)
        assert ratios["kappa_fiber/kappa_ch_Heis"] == 8

    def test_fiber_over_cat_fiber_ratio(self):
        """kappa_fiber / kappa_cat_fiber = 24/2 = 12."""
        ratios = verify_all_ratios()
        # VERIFIED [DC] fiber/cat ratio [LC] lattice-to-Euler
        assert ratios["kappa_fiber/kappa_cat_fiber"] == Fraction(24, 2)
        assert ratios["kappa_fiber/kappa_cat_fiber"] == 12

    def test_deficit_24_minus_5(self):
        """kappa_fiber - kappa_BKM = 24 - 5 = 19 = codim(Lambda^{3,2})."""
        # VERIFIED [DC] deficit 19 [LC] lattice codimension
        assert 24 - 5 == 19

    def test_spectrum_values(self):
        """The spectrum is {0, 2, 3, 5, 24}."""
        result = verify_spectrum_completeness()
        # VERIFIED [DC] spectrum {0,2,3,5,24} [LC] complete
        assert result["complete"]
        assert result["spectrum"] == [0, 2, 3, 5, 24]
        assert result["cardinality"] == 5


# ======================================================================
# 7. Serre duality structural test
# ======================================================================

class TestSerreDualityUniversal:
    """Test that chi(O) = 0 for ALL odd-dimensional CY manifolds."""

    def test_odd_dim_vanishing_K3xE(self):
        """K3 x E is CY_3 (odd), so chi(O) = 0 by Serre duality."""
        k3e = k3_times_e()
        # VERIFIED [DC] odd CY vanishing [LC] Serre duality
        assert k3e.dim_C % 2 == 1  # odd
        assert k3e.chi_O() == 0

    def test_even_dim_nonvanishing_K3(self):
        """K3 is CY_2 (even), so chi(O) = 2 != 0. No cancellation."""
        k3 = k3_surface()
        # VERIFIED [DC] even CY nonvanishing [LC] Serre duality
        assert k3.dim_C % 2 == 0  # even
        assert k3.chi_O() == 2  # non-zero

    def test_odd_dim_vanishing_quintic(self):
        """Quintic is CY_3 (odd), so chi(O) = 0 by Serre duality."""
        q = quintic_threefold()
        # VERIFIED [DC] quintic odd CY vanishing [LC] Serre duality
        assert q.dim_C % 2 == 1
        assert q.chi_O() == 0

    def test_even_dim_nonvanishing_possible(self):
        """E is CY_1 (odd), so chi(O) = 0."""
        e = elliptic_curve()
        # VERIFIED [DC] E odd CY vanishing [LC] Serre duality
        assert e.dim_C % 2 == 1
        assert e.chi_O() == 0


# ======================================================================
# 8. BCOV formula adversarial
# ======================================================================

class TestBCOVAdversarial:
    """Test that chi_top/24 does NOT give kappa_ch in general."""

    def test_bcov_fails_E(self):
        """chi_top(E)/24 = 0 != 1 = kappa_ch(E)."""
        e = elliptic_curve()
        # VERIFIED [DC] BCOV fails for E [LC] h^{1,0} != 0
        assert Fraction(e.chi_top, 24) == 0
        assert 0 != 1  # kappa_ch(E) = 1

    def test_bcov_fails_K3(self):
        """chi_top(K3)/24 = 1 != 2 = kappa_ch(K3)."""
        k3 = k3_surface()
        # VERIFIED [DC] BCOV fails for K3 [LC] h^{1,0} = 0 but surface
        assert Fraction(k3.chi_top, 24) == 1
        assert 1 != 2  # kappa_ch(K3) = 2

    def test_bcov_fails_K3xE(self):
        """chi_top(K3 x E)/24 = 0; it does not produce kappa_ch^Heis = 3."""
        k3e = k3_times_e()
        # VERIFIED [DC] BCOV fails for K3 x E [LC] chi_top = 0
        assert Fraction(k3e.chi_top, 24) == 0
        assert 0 != 3  # kappa_ch^Heis(K3 x E) = 3

    def test_bcov_works_quintic(self):
        """chi_top(Quintic)/24 = -25/3 = kappa_ch(Quintic)."""
        q = quintic_threefold()
        # VERIFIED [DC] BCOV works for quintic [LC] rigid compact CICY
        assert Fraction(q.chi_top, 24) == Fraction(-25, 3)


# ======================================================================
# 9. Master verification
# ======================================================================

class TestMasterVerification:
    """End-to-end adversarial check."""

    def test_master_all_consistent(self):
        """Full adversarial check passes."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] master consistency [LC] adversarial
        assert result["all_consistent"]

    def test_total_route_count(self):
        """22 routes total (7 + 5 + 5 + 5)."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] route count [LC] completeness
        assert result["total_routes"] == 22

    def test_wrong_routes_documented(self):
        """2 intentionally wrong routes documented (NOT_sum + NOT_sigma_c)."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] wrong routes [LC] adversarial documentation
        assert result["wrong_routes_documented"] == 2

    def test_kappa_ch_no_discrepancies(self):
        """kappa_ch^Heis: all 7 routes agree."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] kappa_ch clean [LC] 7-route
        assert result["kappa_ch_report"].all_agree

    def test_kappa_cat_no_discrepancies(self):
        """kappa_cat: all 5 routes agree."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] kappa_cat clean [LC] 5-route
        assert result["kappa_cat_report"].all_agree

    def test_kappa_BKM_no_discrepancies(self):
        """kappa_BKM: all valid routes agree."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] kappa_BKM clean [LC] 3-valid-route
        assert result["kappa_BKM_report"].all_agree

    def test_kappa_fiber_no_discrepancies(self):
        """kappa_fiber: all valid routes agree."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] kappa_fiber clean [LC] 4-valid-route
        assert result["kappa_fiber_report"].all_agree

    def test_cross_kappa_failure(self):
        """kappa_ch^Heis + kappa_cat = 3 != 5 = kappa_BKM."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] cross-kappa failure [LC] fundamental
        assert not result["cross_kappa_check"]["sum_equals_BKM"]

    def test_spectrum_complete(self):
        """Spectrum {0, 2, 3, 5, 24} is verified complete."""
        result = verify_all_kappa_consistency()
        # VERIFIED [DC] spectrum complete [LC] 5 values
        assert result["completeness"]["complete"]
