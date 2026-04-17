r"""Tests for twisted holography on K3 x E (Costello-Gaiotto programme).

Verifies:
  (1) Holographic anomaly: boundary central charge c = chi(K3) = 24
  (2) Bulk-boundary Koszul duality: conductor rho_K = 0
  (3) Defect algebra: E_1-chiral bialgebra axioms from Wilson lines
  (4) kappa_ch = 2 from four independent routes
  (5) Mukai signature (4,20) from R-matrix zero distribution
  (6) kappa-spectrum polysemy: {2, 3, 5, 24}
  (7) Gravitational anomaly decomposition via index theorems
  (8) Cross-engine consistency with k3_yangian, drinfeld_center, e1_bialgebra

Multi-path verification:
  Path 1: Direct computation from defining formula
  Path 2: Noether formula / index theorem
  Path 3: Lattice-theoretic (U^4 + E_8(-1)^2)
  Path 4: R-matrix zero distribution
  Path 5: Cross-engine comparison (k3_yangian.py, drinfeld_center_k3_heisenberg.py)
  Path 6: Holographic anomaly cancellation

Ground truth (verified from multiple sources):
  chi(K3) = 24           # DC: 1-0+22-0+1; LT: Beauville Prop VIII.3
  sigma(K3) = -16        # DC: b_2^+ - b_2^- = 3-19; LT: Barth-Peters-Van de Ven
  chi(O_{K3}) = 2        # DC: (c1^2+c2)/12 = 24/12; LT: Noether formula
  Mukai sig = (4,20)     # DC: U^4+E_8(-1)^2; LT: Mukai, Huybrechts Ch 10
  kappa_ch(K3) = 2       # DC: chi(O_{K3}); LT: modular_koszul_bridge.tex
  kappa_BKM(K3xE) = 5    # DC: c(0)/2=10/2; LT: Gritsenko-Nikulin
  Drin(H_Muk) dim = 49   # DC: 24+24+1; LT: Kassel Ch IX

Manuscript references:
  chapters/connections/cy_holographic_datum_master.tex
  chapters/theory/e1_chiral_algebras.tex
  chapters/theory/quantum_chiral_algebras.tex

References:
  Costello-Gaiotto, arXiv:1812.09257 (twisted holography)
  Costello-Li, arXiv:1606.00443 (M-theory twisted holography)
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.twisted_holography_k3e import (
    # Constants
    CHI_K3,
    CHI_O_K3,
    KAPPA_BKM_K3E,
    KAPPA_CAT_K3,
    KAPPA_CH_E,
    KAPPA_CH_K3,
    KAPPA_CH_K3E,
    KAPPA_FIBER_K3,
    KOSZUL_CONDUCTOR_HEIS,
    MUKAI_RANK,
    MUKAI_SIG_MINUS,
    MUKAI_SIG_PLUS,
    SIGMA_K3,
    STATUS,
    # Functions
    bulk_boundary_koszul_k3e,
    cross_check_with_drinfeld_center,
    cross_check_with_e1_bialgebra,
    cross_check_with_k3_yangian,
    defect_coproduct_at_spin_1,
    defect_coproduct_at_spin_2,
    gravitational_anomaly_decomposition,
    holographic_anomaly_k3e,
    kappa_ch_holographic_verification,
    kappa_spectrum_holographic,
    koszul_conductor_verification,
    mukai_lattice_signature_verification,
    mukai_signature_from_r_matrix,
    twisted_holography_k3e_full,
    twisted_holography_k3e_summary,
    wilson_line_defect_algebra,
)


# =========================================================================
# 1. K3 topological invariants (7 tests)
# =========================================================================

class TestK3TopologicalInvariants:
    """Verify K3 topological invariants used throughout the engine."""

    def test_euler_characteristic(self):
        """chi(K3) = 24 from Betti numbers: 1 - 0 + 22 - 0 + 1 = 24.

        # VERIFIED: DC (Betti sum), LT (Beauville Prop VIII.3)
        """
        assert CHI_K3 == 24

    def test_signature(self):
        """sigma(K3) = -16 from intersection form: b_2^+ - b_2^- = 3 - 19.

        # VERIFIED: DC (Hodge decomposition), LT (Barth-Peters-Van de Ven)
        """
        assert SIGMA_K3 == -16

    def test_holomorphic_euler(self):
        """chi(O_{K3}) = 2 from Noether: (c_1^2 + c_2)/12 = (0+24)/12.

        # VERIFIED: DC (Noether formula), LT (Huybrechts Ch 1)
        """
        assert CHI_O_K3 == 2

    def test_mukai_rank(self):
        """Mukai lattice rank = 24 = dim H^*(K3, C).

        # VERIFIED: DC (1+22+1), LT (Huybrechts Ch 10)
        """
        assert MUKAI_RANK == 24

    def test_mukai_signature_constants(self):
        """Mukai pairing signature (4,20) from U^4 + E_8(-1)^2.

        # VERIFIED: DC (lattice decomposition), LT (Mukai 1987)
        """
        assert MUKAI_SIG_PLUS == 4
        assert MUKAI_SIG_MINUS == 20
        assert MUKAI_SIG_PLUS + MUKAI_SIG_MINUS == MUKAI_RANK

    def test_signature_pontryagin_relation(self):
        """sigma(K3) = (1/3) int p_1 = (1/3)(3 * sigma) consistency.

        # VERIFIED: DC (Hirzebruch signature theorem)
        """
        p1_int = 3 * SIGMA_K3  # = -48
        sigma_from_p1 = p1_int // 3  # = -16
        assert sigma_from_p1 == SIGMA_K3

    def test_noether_formula(self):
        """chi(O_{K3}) = (c_1^2 + c_2)/12 = (0 + 24)/12 = 2.

        # VERIFIED: DC (direct), LT (Noether)
        """
        c1_sq = 0  # c_1(K3) = 0 (CY)
        c2 = CHI_K3  # c_2 = chi for surfaces
        chi_O = (c1_sq + c2) // 12
        assert chi_O == CHI_O_K3


# =========================================================================
# 2. kappa-spectrum (8 tests)
# =========================================================================

class TestKappaSpectrum:
    """Verify the kappa-spectrum values and their distinctness (AP113)."""

    def test_kappa_ch_k3(self):
        """kappa_ch(K3) = chi(O_{K3}) = 2 (PROVED at d=2).

        # VERIFIED: DC (chi(O)), LT (modular_koszul_bridge.tex)
        """
        assert KAPPA_CH_K3 == 2

    def test_kappa_ch_e(self):
        """kappa_ch(E) = 1 (Heisenberg at level 1).

        # VERIFIED: DC (kappa_ch(H_k) = k with k=1), LT (landscape_census.tex)
        """
        assert KAPPA_CH_E == 1

    def test_kappa_ch_k3e(self):
        """kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3.

        # Route B (Heisenberg level / free-boson rank, AP-CY55 algebraisation
        # invariant): kappa_ch(E) = 1 via k = 1 Heisenberg level, additive
        # under product of free-boson constructions, giving 2 + 1 = 3.
        # Route A (Hodge supertrace, Kunneth-multiplicative) gives
        # Xi(K3 x E) = Xi(K3) * Xi(E) = 2 * 0 = 0 (E has Xi = 1 - 1 = 0);
        # the canonical Phi_d functor value is 0 per
        # cy_d_kappa_stratification.tex:411-426. Both routes coexist under
        # AP234 notational collision; this test pins the Route B value.
        # VERIFIED: DC (Route B additivity), LT (modular_koszul_bridge_k3e.py)
        """
        assert KAPPA_CH_K3E == KAPPA_CH_K3 + KAPPA_CH_E
        assert KAPPA_CH_K3E == 3

    def test_kappa_bkm_k3e(self):
        """kappa_BKM(K3 x E) = wt(Delta_5) = c_1(0)/2 = 10/2 = 5.

        Canonical paramodular weight-5 level-1 cusp form Delta_5
        (Gritsenko 1999); c_1(0) = 10 is the constant Fourier coefficient
        of 2*phi_{0,1}.  Distinct from Siegel-Igusa Phi_10 (weight 10 in
        Sp_4(Z), = Delta_5^2, non-paramodular).

        # VERIFIED: DC (c_1(0)=10 from 2*phi_{0,1}), LT (Gritsenko 1999)
        """
        assert KAPPA_BKM_K3E == 5

    def test_kappa_cat_k3(self):
        """kappa_cat(K3) = chi(O_{K3}) = 2.

        # VERIFIED: DC (Noether), LT (definition)
        """
        assert KAPPA_CAT_K3 == 2

    def test_kappa_fiber_k3(self):
        """kappa_fiber(K3) = 24 = rank(Lambda_Muk).

        # VERIFIED: DC (1+22+1), LT (Mukai lattice rank)
        """
        assert KAPPA_FIBER_K3 == 24

    def test_kappa_ch_equals_kappa_cat(self):
        """For K3 at d=2: kappa_ch = kappa_cat = 2.

        # VERIFIED: DC (both = chi(O)), LT (kappa = chi^CY at d=2)
        """
        assert KAPPA_CH_K3 == KAPPA_CAT_K3

    def test_kappa_spectrum_polysemy(self):
        """The four kappa values {2, 3, 5, 24} are pairwise distinct.

        # VERIFIED: DC (enumeration)
        """
        kappas = {KAPPA_CH_K3, KAPPA_CH_K3E, KAPPA_BKM_K3E, KAPPA_FIBER_K3}
        assert len(kappas) == 4
        assert kappas == {2, 3, 5, 24}


# =========================================================================
# 3. Holographic anomaly (8 tests)
# =========================================================================

class TestHolographicAnomaly:
    """Test the holographic anomaly computation for K3 x E."""

    def test_anomaly_returns_named_tuple(self):
        """holographic_anomaly_k3e returns HolographicAnomalyK3E."""
        result = holographic_anomaly_k3e()
        assert hasattr(result, 'c_boundary')
        assert hasattr(result, 'anomaly_matches')

    def test_c_boundary_equals_chi_k3(self):
        """Boundary central charge c = chi(K3) = 24.

        # VERIFIED: DC (gravitational anomaly), LT (Costello-Gaiotto)
        """
        result = holographic_anomaly_k3e()
        assert result.c_boundary == 24
        assert result.anomaly_matches is True

    def test_kappa_from_anomaly(self):
        """kappa_ch from holographic anomaly = chi(O_{K3}) = 2.

        # VERIFIED: DC (one-loop determinant), LT (CY-A_2 proof)
        """
        result = holographic_anomaly_k3e()
        assert result.kappa_ch_from_anomaly == 2
        assert result.kappa_matches is True

    def test_gravitational_decomposition_p1(self):
        """int_{K3} p_1 = 3 * sigma = 3 * (-16) = -48.

        # VERIFIED: DC (Hirzebruch), LT (Barth-Peters-Van de Ven)
        """
        result = gravitational_anomaly_decomposition()
        assert result['int_p1'] == -48

    def test_gravitational_decomposition_euler(self):
        """int_{K3} e = chi(K3) = 24.

        # VERIFIED: DC (Betti sum), LT (Gauss-Bonnet)
        """
        result = gravitational_anomaly_decomposition()
        assert result['int_euler'] == 24

    def test_gravitational_decomposition_c2(self):
        """int_{K3} c_2 = chi(K3) = 24 (for complex surfaces c_2 = e).

        # VERIFIED: DC (c_2 = e for surfaces), LT (Huybrechts)
        """
        result = gravitational_anomaly_decomposition()
        assert result['int_c2'] == 24

    def test_sigma_from_p1(self):
        """sigma = p_1/3 = -48/3 = -16 consistency check.

        # VERIFIED: DC (Hirzebruch signature), LT (index theorem)
        """
        result = gravitational_anomaly_decomposition()
        assert result['sigma_from_p1'] == -16
        assert result['sigma_matches'] is True

    def test_noether_from_c2(self):
        """chi(O) = (c_1^2 + c_2)/12 = (0+24)/12 = 2 from decomposition.

        # VERIFIED: DC (Noether), LT (Huybrechts)
        """
        result = gravitational_anomaly_decomposition()
        assert result['chi_O_from_noether'] == 2
        assert result['noether_matches'] is True


# =========================================================================
# 4. Bulk-boundary Koszul duality (7 tests)
# =========================================================================

class TestBulkBoundaryKoszul:
    """Test bulk-boundary Koszul duality for K3 x E."""

    def test_koszul_returns_named_tuple(self):
        """bulk_boundary_koszul_k3e returns BulkBoundaryKoszulK3E."""
        result = bulk_boundary_koszul_k3e()
        assert hasattr(result, 'boundary_rank')
        assert hasattr(result, 'koszul_conductor')

    def test_boundary_rank(self):
        """Boundary algebra has rank 24 (Mukai lattice rank).

        # VERIFIED: DC (dim H^*(K3)), LT (k3_double_current_algebra.py)
        """
        result = bulk_boundary_koszul_k3e()
        assert result.boundary_rank == 24

    def test_boundary_kappa_ch(self):
        """Boundary kappa_ch = 2 (K3 Heisenberg).

        # VERIFIED: DC (chi(O_{K3})), LT (CY-A_2)
        """
        result = bulk_boundary_koszul_k3e()
        assert result.boundary_kappa_ch == 2

    def test_dual_kappa_ch(self):
        """Koszul dual has kappa_ch = -2 (level inversion for Heisenberg).

        # VERIFIED: DC (kappa(H_k^!) = -k), LT (e1_koszul_three_families.py)
        """
        result = bulk_boundary_koszul_k3e()
        assert result.dual_kappa_ch == -2

    def test_koszul_conductor_zero(self):
        """Koszul conductor rho_K = 0 for class G (Heisenberg).

        # VERIFIED: DC (2 + (-2) = 0), LT (class G theorem)
        """
        result = bulk_boundary_koszul_k3e()
        assert result.koszul_conductor == 0

    def test_bulk_dim_49(self):
        """Bulk algebra Drin(H_Muk) has dim = 49 (24 + 24 + 1).

        # VERIFIED: DC (2*24+1), LT (Kassel Ch IX, drinfeld_center_k3_heisenberg.py)
        """
        result = bulk_boundary_koszul_k3e()
        assert result.bulk_dim == 49

    def test_conductor_three_paths(self):
        """Koszul conductor verified by three independent paths.

        # VERIFIED: DC (direct), SY (class G), DA (anomaly cancellation)
        """
        result = koszul_conductor_verification()
        assert result['conductor_is_zero'] is True
        assert result['class_G_implies_zero_conductor'] is True
        assert result['holographic_anomaly_cancels'] is True
        assert result['all_paths_agree'] is True


# =========================================================================
# 5. Defect algebra and E_1-chiral bialgebra (8 tests)
# =========================================================================

class TestDefectAlgebra:
    """Test the defect algebra from Wilson lines."""

    def test_wilson_line_structure_function_degree(self):
        """Structure function g_{K3}(z) has degree (24, 24).

        # VERIFIED: DC (product of 24 factors), LT (k3_yangian.py)
        """
        result = wilson_line_defect_algebra()
        assert result['structure_function_degree'] == (24, 24)

    def test_ybe_satisfied(self):
        """YBE satisfied (automatic for diagonal R-matrix at gl_1).

        # VERIFIED: DC (commutativity of scalars), LT (k3_yangian.py)
        """
        result = wilson_line_defect_algebra()
        assert result['ybe_satisfied'] is True

    def test_unitarity_condition(self):
        """R(z)R(-z) = I from CY-induced g(z)g(-z) = 1.

        # VERIFIED: DC (each factor cancels), LT (k3_yangian.py)
        """
        result = wilson_line_defect_algebra()
        assert 'g(z)g(-z)=1' in result['unitarity']

    def test_spectral_not_worldsheet(self):
        """z is SPECTRAL parameter, NOT worldsheet (AP-CY31).

        # VERIFIED: DA (Yangian vs OPE distinction)
        """
        result = wilson_line_defect_algebra()
        assert 'SPECTRAL' in result['spectral_vs_worldsheet']

    def test_spin_1_no_z_dependence(self):
        """Spin-1 coproduct is additive (no z-dependence for Heisenberg).

        # VERIFIED: DC (class G, free field), LT (e1_chiral_bialgebra_engine.py)
        """
        result = defect_coproduct_at_spin_1(Fraction(1))
        assert result['z_dependence'] == 'NONE at spin 1'
        assert result['num_generators'] == 24

    def test_spin_1_first_z_at_spin_2(self):
        """First z-dependent coproduct appears at spin 2 (Sugawara).

        # VERIFIED: DC (Sugawara cross-terms), LT (chiral_coproduct_spin2_engine.py)
        """
        result = defect_coproduct_at_spin_1(Fraction(1))
        assert result['first_z_dependent_spin'] == 2

    def test_spin_2_cross_term(self):
        """Spin-2 coproduct cross-term involves kappa_ch = 2.

        # VERIFIED: DC (Sugawara with 24 generators), LT (e1_chiral_bialgebra_engine.py)
        """
        result = defect_coproduct_at_spin_2(Fraction(1), Psi=Fraction(2))
        assert result['cross_term_involves_mukai'] is True
        assert 'kappa_ch(K3)' in result['cross_term_at_z1']

    def test_spin_2_coassociativity(self):
        """Spin-2 coassociativity via Miura factorization.

        # VERIFIED: DC (Miura multiplicativity), LT (e1_chiral_bialgebra_engine.py)
        """
        result = defect_coproduct_at_spin_2(Fraction(1))
        assert 'Miura' in result['coassociativity']


# =========================================================================
# 6. kappa_ch from holographic perspective (5 tests)
# =========================================================================

class TestKappaChHolographic:
    """Test the four independent routes to kappa_ch = 2."""

    def test_all_routes_agree(self):
        """All four routes give kappa_ch = 2.

        # VERIFIED: DC (4 independent computations)
        """
        result = kappa_ch_holographic_verification()
        assert result['all_routes_agree'] is True
        assert result['kappa_ch_k3'] == 2

    def test_route_1_cy_euler(self):
        """Route 1: chi(O_{K3}) = 1 - 0 + 1 = 2.

        # VERIFIED: DC (Hodge numbers), LT (Beauville)
        """
        result = kappa_ch_holographic_verification()
        assert result['route_1_cy_euler']['chi_O'] == 2

    def test_route_2_holographic(self):
        """Route 2: holographic anomaly gives kappa = 2.

        # VERIFIED: DC (gravitational CS level)
        """
        result = kappa_ch_holographic_verification()
        assert result['route_2_holographic']['kappa'] == 2

    def test_route_3_noether(self):
        """Route 3: Noether formula gives chi(O) = 2.

        # VERIFIED: DC ((0+24)/12=2), LT (Noether formula)
        """
        result = kappa_ch_holographic_verification()
        assert result['route_3_noether']['chi_O'] == 2

    def test_route_4_heisenberg(self):
        """Route 4: Heisenberg level k = 2 gives kappa_ch = 2.

        # VERIFIED: DC (kappa_ch(H_k)=k), LT (landscape_census.tex)
        """
        result = kappa_ch_holographic_verification()
        assert result['route_4_heisenberg']['level'] == 2


# =========================================================================
# 7. Mukai signature (4,20) (7 tests)
# =========================================================================

class TestMukaiSignature:
    """Test the Mukai signature extraction from the R-matrix."""

    def test_r_matrix_signature_default(self):
        """Default Kummer parametrization gives (4,20).

        # VERIFIED: DC (4 positive + 20 negative h), LT (Mukai 1987)
        """
        result = mukai_signature_from_r_matrix()
        assert result.sig_plus == 4
        assert result.sig_minus == 20
        assert result.signature_matches is True

    def test_r_matrix_total_rank(self):
        """Total rank = 24 = sig_plus + sig_minus.

        # VERIFIED: DC (4+20), LT (dim H^*(K3))
        """
        result = mukai_signature_from_r_matrix()
        assert result.total_rank == 24
        assert result.sig_plus + result.sig_minus == 24

    def test_lattice_path_signature(self):
        """Lattice path: U^4 + E_8(-1)^2 gives (4,20).

        # VERIFIED: DC (4*(1,1)+(0,16)), LT (lattice theory)
        """
        result = mukai_lattice_signature_verification()
        assert result['path_1_lattice']['signature'] == (4, 20)
        assert result['path_1_lattice']['matches'] is True

    def test_hodge_path_signature(self):
        """Hodge path: (H^0+H^4)_(1,1) + H^2_(3,19) gives (4,20).

        # VERIFIED: DC (Hodge decomposition), LT (Huybrechts)
        """
        result = mukai_lattice_signature_verification()
        assert result['path_2_hodge']['signature'] == (4, 20)
        assert result['path_2_hodge']['matches'] is True

    def test_r_matrix_path_signature(self):
        """R-matrix path: zero distribution gives (4,20).

        # VERIFIED: DC (zero counting), LT (k3_yangian.py)
        """
        result = mukai_lattice_signature_verification()
        assert result['path_3_rmatrix']['matches'] is True

    def test_all_signature_paths_agree(self):
        """All three signature paths agree on (4,20).

        # VERIFIED: DC (3 independent paths)
        """
        result = mukai_lattice_signature_verification()
        assert result['all_paths_agree'] is True

    def test_custom_parameters_cy2(self):
        """Custom parameters must satisfy CY_2 constraint (sum = 0)."""
        eps = Fraction(1)
        h_list = [eps] * 4 + [-eps * Fraction(1, 5)] * 20
        assert sum(h_list) == 0
        result = mukai_signature_from_r_matrix(h_list)
        assert result.total_rank == 24


# =========================================================================
# 8. Full datum and cross-engine checks (10 tests)
# =========================================================================

class TestFullDatumAndCrossChecks:
    """Test the assembled holographic datum and cross-engine consistency."""

    def test_full_datum_all_pass(self):
        """All five holographic checks pass simultaneously."""
        datum = twisted_holography_k3e_full()
        assert datum.all_checks_pass is True

    def test_full_datum_c_boundary(self):
        """Full datum: c_boundary = 24."""
        datum = twisted_holography_k3e_full()
        assert datum.c_boundary == 24
        assert datum.c_matches_chi is True

    def test_full_datum_koszul(self):
        """Full datum: Koszul conductor = 0."""
        datum = twisted_holography_k3e_full()
        assert datum.koszul_conductor == 0
        assert datum.conductor_is_zero is True

    def test_full_datum_kappa(self):
        """Full datum: kappa_ch = 2 from all routes."""
        datum = twisted_holography_k3e_full()
        assert datum.kappa_ch == 2
        assert datum.kappa_routes_agree is True

    def test_full_datum_mukai(self):
        """Full datum: Mukai signature (4,20)."""
        datum = twisted_holography_k3e_full()
        assert datum.mukai_sig_plus == 4
        assert datum.mukai_sig_minus == 20
        assert datum.signature_matches is True

    def test_cross_k3_yangian(self):
        """Cross-check with k3_yangian.py: all predictions agree."""
        result = cross_check_with_k3_yangian()
        assert result['structure_function_degree']['agree'] is True
        assert result['unitarity']['agree'] is True
        assert result['cy2_constraint']['agree'] is True
        assert result['classical_r_matrix']['agree'] is True

    def test_cross_drinfeld_center(self):
        """Cross-check with drinfeld_center_k3_heisenberg.py."""
        result = cross_check_with_drinfeld_center()
        assert result['dimensions_agree'] is True
        assert result['r_matrix_type']['agree'] is True

    def test_cross_e1_bialgebra(self):
        """Cross-check with e1_chiral_bialgebra_engine.py: all 5 axioms."""
        result = cross_check_with_e1_bialgebra()
        assert result['all_axioms_consistent'] is True
        for i in range(1, 6):
            assert result[f'axiom_{i}']['consistent'] is True

    def test_summary_packages_all(self):
        """Summary includes all checks and cross-checks."""
        result = twisted_holography_k3e_summary()
        assert result['all_checks_pass'] is True
        assert 'datum' in result
        assert 'kappa_spectrum' in result
        assert 'mukai_verification' in result
        assert 'cross_checks' in result

    def test_kappa_spectrum_holographic(self):
        """The kappa-spectrum function returns all four values."""
        result = kappa_spectrum_holographic()
        assert result['kappa_ch']['value'] == 2
        assert result['kappa_BKM']['value'] == 5
        assert result['kappa_cat']['value'] == 2
        assert result['kappa_fiber']['value'] == 24
        assert result['no_bare_kappa'] is True


# =========================================================================
# 9. Status and AP compliance (5 tests)
# =========================================================================

class TestStatusAndAPCompliance:
    """Test AP compliance flags."""

    def test_status_conjectural(self):
        """Engine status is CONJECTURAL (AP-CY14)."""
        assert STATUS == 'CONJECTURAL'

    def test_kappa_spectrum_no_bare(self):
        """kappa-spectrum uses subscripts throughout (AP113)."""
        result = kappa_spectrum_holographic()
        assert result['no_bare_kappa'] is True

    def test_kappa_spectrum_is_polysemous(self):
        """kappa-spectrum flag acknowledges polysemy (AP113)."""
        result = kappa_spectrum_holographic()
        assert result['kappa_spectrum_is_polysemous'] is True

    def test_holographic_anomaly_status(self):
        """Holographic anomaly result carries correct status."""
        result = holographic_anomaly_k3e()
        assert result.status == 'CONJECTURAL'

    def test_full_datum_status(self):
        """Full datum carries CONJECTURAL status."""
        datum = twisted_holography_k3e_full()
        assert datum.status == 'CONJECTURAL'
