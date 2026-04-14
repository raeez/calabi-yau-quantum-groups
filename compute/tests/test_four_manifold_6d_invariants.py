r"""Tests for four-manifold invariants from 6d holomorphic Chern-Simons theory.

Claims tested:
    1. Topological invariants: chi, sigma, b_2^+/-, Noether formula
    2. VW modular weight = -chi(X)/2 for all surfaces
    3. K3 identification: 6d on K3 x T^2 = VW(K3) = 1/eta^{24}
    4. Mock modularity: b_2^+(X) = 1 => mock modular (P^2, Barlow)
    5. kappa-spectrum: kappa_ch = chi(X), kappa_cat = chi(O_X), kappa_fiber = b_2(X)
    6. Elliptic surface family E(n): chi = 12n, sigma = -8n
    7. Handle decomposition: n_two_handles = b_2(X)
    8. S-duality: G <-> G^L Langlands dual exchange
    9. Dimensional hierarchy: 3d/4d/5d/6d comparison
   10. Freedman/Donaldson constraints on intersection forms
   11. CY_3 = Tot(K_X) route: K3 -> K3 x C, P^2 -> local P^2

Ground truth:
    - Vafa-Witten (1994): modularity theorem, S-duality
    - Gottsche (1990): chi(Hilb^n(S)) from prod 1/(1-q^k)^{chi(S)}
    - Freedman (1982): topological classification of 4-manifolds
    - Donaldson (1983): definite forms are diagonal
    - Noether formula: chi(O_X) = (chi(X) + sigma(X))/12
    - DMVV (1997): second quantization, K3 x E DT partition function

Manuscript references:
    chapters/theory/en_factorization.tex: E_n hierarchy, E_1 stabilization
    chapters/connections/modular_koszul_bridge.tex: kappa = chi^CY
    notes/research_vafa_witten_qvcg.md: VW/QVCG research note
"""

import pytest
from fractions import Fraction

from compute.lib.four_manifold_6d_invariants import (
    # Data types
    FourManifoldData,
    # Surfaces
    K3, T4, CP2, CP2_BAR, S2_CROSS_S2, S4,
    E1_RATIONAL, ENRIQUES, BARLOW, CATALOGUE,
    en_elliptic_surface,
    # Topological invariants
    b2, euler_char, signature,
    holomorphic_euler_char, geometric_genus,
    # VW functions
    vw_modular_weight, vw_is_mock_modular, vw_is_trivial,
    vw_partition_function_coeffs, KNOWN_HILB_K3,
    # kappa-spectrum
    kappa_ch, kappa_cat, kappa_fiber, kappa_spectrum,
    # 6d compactification
    compactification_data,
    # Handle decomposition
    handle_decomposition, fh_e2_on_four_manifold,
    # CY_3 route
    tot_kx_cy3_data,
    # S-duality
    s_duality_data, LANGLANDS_DUAL,
    # Dimensional hierarchy
    dimensional_hierarchy_entry, full_hierarchy,
    # Verification
    verify_noether_formula, verify_vw_weight_formula,
    verify_freedman_constraints, verify_6d_k3_cross_t2,
    verify_mock_modularity_p2, verify_surface_table,
    verify_elliptic_surface_family, verify_k3_hilb_from_vw,
)


# ======================================================================
# 1. Topological invariants of standard four-manifolds
# ======================================================================

class TestTopologicalInvariants:
    """Verify basic topological invariants of four-manifolds."""

    def test_k3_euler_char(self):
        """chi(K3) = 24."""
        assert euler_char(K3) == 24

    def test_k3_signature(self):
        """sigma(K3) = 3 - 19 = -16."""
        assert signature(K3) == -16

    def test_k3_b2(self):
        """b_2(K3) = 3 + 19 = 22."""
        assert b2(K3) == 22

    def test_t4_euler_char(self):
        """chi(T^4) = 0 (flat torus)."""
        assert euler_char(T4) == 0

    def test_t4_signature(self):
        """sigma(T^4) = 0 (flat metric, no curvature)."""
        assert signature(T4) == 0

    def test_cp2_euler_char(self):
        """chi(CP^2) = 3."""
        assert euler_char(CP2) == 3

    def test_cp2_signature(self):
        """sigma(CP^2) = 1 (positive definite intersection form)."""
        assert signature(CP2) == 1

    def test_s4_euler_char(self):
        """chi(S^4) = 2 (sphere)."""
        assert euler_char(S4) == 2

    def test_s4_b2_is_zero(self):
        """S^4 has b_2 = 0, trivial intersection form."""
        assert b2(S4) == 0

    def test_s2xs2_euler_char(self):
        """chi(S^2 x S^2) = 4."""
        assert euler_char(S2_CROSS_S2) == 4

    def test_s2xs2_signature(self):
        """sigma(S^2 x S^2) = 0 (hyperbolic form U)."""
        assert signature(S2_CROSS_S2) == 0

    def test_barlow_euler_char(self):
        """chi(Barlow) = 11 (homeomorphic to CP^2 # 8 CP^2-bar, b_2 = 9)."""
        assert euler_char(BARLOW) == 11


# ======================================================================
# 2. Noether's formula
# ======================================================================

class TestNoetherFormula:
    """Verify chi(O_X) = (chi(X) + sigma(X)) / 12 for complex surfaces."""

    def test_k3_noether(self):
        """chi(O_{K3}) = (chi + sigma)/4 = (24 + (-16))/4 = 2.

        Derivation: Noether gives 12 chi(O) = c_1^2 + c_2.
        Hirzebruch: sigma = (c_1^2 - 2 c_2)/3, so c_1^2 = 3 sigma + 2 c_2.
        Substituting: 12 chi(O) = 3 sigma + 3 c_2 = 3(sigma + chi_top).
        Hence chi(O) = (chi_top + sigma)/4.

        For K3: c_1 = 0 (CY), c_2 = 24, so chi(O) = 24/12 = 2.
        Cross-check: h^0 - h^1 + h^2 = 1 - 0 + 1 = 2.
        """
        # VERIFIED [DC] Noether-Hirzebruch [LT] Barth-Hulek-Peters-Van de Ven
        result = verify_noether_formula(K3)
        assert result['noether_satisfied']
        assert result['chi_O'] == Fraction(2)
        # Cross-check via Hodge numbers: h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1
        assert result['chi_O'] == Fraction(1 - 0 + 1)

    def test_cp2_noether(self):
        """chi(O_{CP^2}) = (3 + 1)/4 = 1. Cross-check: h^0=1, h^1=h^2=0."""
        result = verify_noether_formula(CP2)
        assert result['noether_satisfied']
        assert result['chi_O'] == Fraction(1)
        assert result['chi_O'] == Fraction(1 - 0 + 0)  # Hodge: h^{0,0}-h^{0,1}+h^{0,2}

    def test_t4_noether(self):
        """chi(O_{T^4}) = (0 + 0)/4 = 0. Cross-check: h^0=1, h^1=2, h^2=1."""
        result = verify_noether_formula(T4)
        assert result['noether_satisfied']
        assert result['chi_O'] == Fraction(0)
        assert result['chi_O'] == Fraction(1 - 2 + 1)  # Hodge: 1 - 2 + 1 = 0

    def test_s2xs2_noether(self):
        """chi(O_{S^2 x S^2}) = (4 + 0)/4 = 1. Cross-check: P^1 x P^1, h^0=1, h^1=0, h^2=0."""
        result = verify_noether_formula(S2_CROSS_S2)
        assert result['noether_satisfied']
        assert result['chi_O'] == Fraction(1)
        assert result['chi_O'] == Fraction(1 - 0 + 0)  # Hodge: h^{0,0}-h^{0,1}+h^{0,2}

    def test_all_complex_surfaces(self):
        """Noether formula holds for all complex surfaces in the catalogue."""
        for name, X in CATALOGUE.items():
            if X.is_complex:
                result = verify_noether_formula(X)
                assert result['noether_satisfied'], f"Noether fails for {name}"


# ======================================================================
# 3. VW modular weight
# ======================================================================

class TestVWModularWeight:
    """Verify VW modular weight = -chi(X)/2."""

    def test_k3_weight(self):
        """VW weight on K3 = -12, matching eta^{-24}."""
        # VERIFIED [DC] modular weight [LT] Vafa-Witten (1994)
        assert vw_modular_weight(K3) == Fraction(-12)

    def test_t4_weight(self):
        """VW weight on T^4 = 0."""
        assert vw_modular_weight(T4) == Fraction(0)

    def test_cp2_weight(self):
        """VW weight on P^2 = -3/2 (half-integer => mock modular)."""
        assert vw_modular_weight(CP2) == Fraction(-3, 2)

    def test_s4_weight(self):
        """VW weight on S^4 = -1."""
        assert vw_modular_weight(S4) == Fraction(-1)

    def test_s2xs2_weight(self):
        """VW weight on S^2 x S^2 = -2."""
        assert vw_modular_weight(S2_CROSS_S2) == Fraction(-2)

    def test_barlow_weight(self):
        """VW weight on Barlow = -11/2 (chi = 11, exotic smooth structure)."""
        assert vw_modular_weight(BARLOW) == Fraction(-11, 2)

    def test_weight_formula_all_surfaces(self):
        """VW weight = -chi/2 for every surface in the catalogue."""
        for name, X in CATALOGUE.items():
            result = verify_vw_weight_formula(X)
            assert result['match'], f"Weight formula fails for {name}"


# ======================================================================
# 4. Mock modularity
# ======================================================================

class TestMockModularity:
    """Verify mock modular behavior when b_2^+ = 1."""

    def test_k3_not_mock(self):
        """K3 has b_2^+ = 3 > 1, so VW is genuinely modular."""
        assert not vw_is_mock_modular(K3)

    def test_cp2_is_mock(self):
        """P^2 has b_2^+ = 1, so VW is mock modular."""
        assert vw_is_mock_modular(CP2)

    def test_barlow_is_mock(self):
        """Barlow has b_2^+ = 1, so VW is mock modular."""
        assert vw_is_mock_modular(BARLOW)

    def test_e1_is_mock(self):
        """E(1) has b_2^+ = 1, so VW is mock modular."""
        assert vw_is_mock_modular(E1_RATIONAL)

    def test_t4_not_mock(self):
        """T^4 has b_2^+ = 3 > 1, so VW is genuinely modular."""
        assert not vw_is_mock_modular(T4)

    def test_s4_not_mock(self):
        """S^4 has b_2^+ = 0, VW is trivial (not mock)."""
        assert not vw_is_mock_modular(S4)
        assert vw_is_trivial(S4)

    def test_p2_mock_details(self):
        """Detailed mock modularity check for P^2."""
        result = verify_mock_modularity_p2()
        assert result['is_mock']
        assert result['weight'] == Fraction(-3, 2)
        assert result['chi_P2'] == 3
        assert result['b2_plus'] == 1
        assert result['hilb_match']


# ======================================================================
# 5. The central identification: 6d on K3 x T^2 = VW(K3) = 1/eta^{24}
# ======================================================================

class TestK3Identification:
    """The fundamental test: 6d invariant of K3 x T^2 = 1/eta^{24}."""

    def test_hilb_0(self):
        """chi(Hilb^0(K3)) = 1 (a point)."""
        coeffs = vw_partition_function_coeffs(K3, 0)
        assert int(coeffs[0]) == 1

    def test_hilb_1(self):
        """chi(Hilb^1(K3)) = 24 = chi(K3)."""
        coeffs = vw_partition_function_coeffs(K3, 1)
        assert int(coeffs[1]) == 24

    def test_hilb_2(self):
        """chi(Hilb^2(K3)) = 324."""
        coeffs = vw_partition_function_coeffs(K3, 2)
        assert int(coeffs[2]) == 324

    def test_hilb_3(self):
        """chi(Hilb^3(K3)) = 3200."""
        coeffs = vw_partition_function_coeffs(K3, 3)
        assert int(coeffs[3]) == 3200

    def test_all_known_hilb_k3(self):
        """All known chi(Hilb^n(K3)) match the eta product expansion."""
        # VERIFIED [DC] Hilbert scheme chi [LT] Gottsche (1990)
        max_n = max(KNOWN_HILB_K3.keys())
        coeffs = vw_partition_function_coeffs(K3, max_n)
        for n, expected in KNOWN_HILB_K3.items():
            computed = int(coeffs[n])
            assert computed == expected, f"chi(Hilb^{n}(K3)): got {computed}, expected {expected}"

    def test_master_verification(self):
        """Full multi-path verification of the K3 identification."""
        result = verify_6d_k3_cross_t2()
        assert result['all_pass']
        assert result['path_B_weight']['ok']
        assert result['path_C_hilb']['all_match']
        assert result['path_D_kappa']['ok']

    def test_k3_hilb_from_vw(self):
        """VW route to Hilbert scheme chi."""
        result = verify_k3_hilb_from_vw()
        assert result['all_known_match']
        assert result['weight_correct']


# ======================================================================
# 6. kappa-spectrum (AP113 compliance)
# ======================================================================

class TestKappaSpectrum:
    """Verify the kappa-spectrum for four-manifold invariants."""

    def test_k3_kappa_ch(self):
        """kappa_ch(K3) = 24."""
        # VERIFIED [DC] kappa_ch = chi(X) [LT] Vol I shadow tower
        assert kappa_ch(K3) == Fraction(24)

    def test_k3_kappa_cat(self):
        """kappa_cat(K3) = chi(O_{K3}) = 2."""
        assert kappa_cat(K3) == Fraction(2)

    def test_k3_kappa_fiber(self):
        """kappa_fiber(K3) = b_2(K3) = 22."""
        assert kappa_fiber(K3) == Fraction(22)

    def test_k3_full_spectrum(self):
        """Full kappa-spectrum for K3: {24, 2, 22}."""
        ks = kappa_spectrum(K3)
        assert ks['ch'] == Fraction(24)
        assert ks['cat'] == Fraction(2)
        assert ks['fiber'] == Fraction(22)

    def test_cp2_kappa_ch(self):
        """kappa_ch(P^2) = 3."""
        assert kappa_ch(CP2) == Fraction(3)

    def test_cp2_kappa_cat(self):
        """kappa_cat(P^2) = chi(O_{P^2}) = 1."""
        assert kappa_cat(CP2) == Fraction(1)

    def test_t4_kappa_ch(self):
        """kappa_ch(T^4) = chi(T^4) = 0."""
        assert kappa_ch(T4) == Fraction(0)

    def test_t4_kappa_cat(self):
        """kappa_cat(T^4) = chi(O_{T^4}) = 0."""
        assert kappa_cat(T4) == Fraction(0)

    def test_s4_kappa_ch(self):
        """kappa_ch(S^4) = 2."""
        assert kappa_ch(S4) == Fraction(2)


# ======================================================================
# 7. Elliptic surface family E(n)
# ======================================================================

class TestEllipticSurfaceFamily:
    """Verify the elliptic surface family E(n)."""

    def test_e1_chi(self):
        """chi(E(1)) = 12."""
        assert euler_char(en_elliptic_surface(1)) == 12

    def test_e2_is_k3(self):
        """E(2) = K3: chi = 24, sigma = -16."""
        E2 = en_elliptic_surface(2)
        assert euler_char(E2) == 24
        assert signature(E2) == -16
        assert E2.b2_plus == 3
        assert E2.b2_minus == 19

    def test_e3_chi(self):
        """chi(E(3)) = 36."""
        assert euler_char(en_elliptic_surface(3)) == 36

    def test_e_n_chi_formula(self):
        """chi(E(n)) = 12n for n = 1, ..., 5."""
        for n in range(1, 6):
            En = en_elliptic_surface(n)
            assert euler_char(En) == 12 * n, f"chi(E({n})) != {12*n}"

    def test_e_n_sigma_formula(self):
        """sigma(E(n)) = -8n for n = 1, ..., 5."""
        for n in range(1, 6):
            En = en_elliptic_surface(n)
            assert signature(En) == -8 * n, f"sigma(E({n})) != {-8*n}"

    def test_e_n_spin_parity(self):
        """E(n) is spin iff n is even."""
        for n in range(1, 6):
            En = en_elliptic_surface(n)
            assert En.is_spin == (n % 2 == 0), f"E({n}) spin wrong"

    def test_full_family_verification(self):
        """Full verification of E(n) family."""
        result = verify_elliptic_surface_family(5)
        assert result['all_ok']


# ======================================================================
# 8. Handle decomposition
# ======================================================================

class TestHandleDecomposition:
    """Verify handle decomposition for four-manifolds."""

    def test_k3_handles(self):
        """K3 has 1 + 0 + 22 + 0 + 1 handles."""
        hd = handle_decomposition(K3)
        assert hd.zero_handles == 1
        assert hd.one_handles == 0
        assert hd.two_handles == 22
        assert hd.three_handles == 0
        assert hd.four_handles == 1

    def test_cp2_handles(self):
        """P^2 has 1 + 0 + 1 + 0 + 1 handles."""
        hd = handle_decomposition(CP2)
        assert hd.two_handles == 1

    def test_s4_handles(self):
        """S^4 has 1 + 0 + 0 + 0 + 1 handles (no middle dimension)."""
        hd = handle_decomposition(S4)
        assert hd.two_handles == 0

    def test_s2xs2_handles(self):
        """S^2 x S^2 has 2 two-handles."""
        hd = handle_decomposition(S2_CROSS_S2)
        assert hd.two_handles == 2

    def test_handle_signature_k3(self):
        """K3 intersection form signature: (3, 19)."""
        hd = handle_decomposition(K3)
        assert hd.intersection_matrix_sig == (3, 19)

    def test_fh_k3(self):
        """FH of E_2-algebra on K3."""
        result = fh_e2_on_four_manifold(K3)
        assert result['euler_char'] == 24
        assert result['n_two_handles'] == 22
        assert result['fh_rank_einf'] == 24


# ======================================================================
# 9. CY_3 = Tot(K_X) route
# ======================================================================

class TestTotKXRoute:
    """Verify the Tot(K_X) -> CY_3 route."""

    def test_k3_tot_trivial(self):
        """Tot(K_{K3}) = K3 x C (trivial canonical bundle)."""
        result = tot_kx_cy3_data(K3)
        assert result['kx_trivial']
        assert result['tot_kx'] == 'K3 x C'

    def test_t4_tot_trivial(self):
        """Tot(K_{T^4}) = T^4 x C (trivial canonical bundle)."""
        result = tot_kx_cy3_data(T4)
        assert result['kx_trivial']
        assert result['tot_kx'] == 'T^4 x C'

    def test_cp2_tot_nontrivial(self):
        """Tot(K_{P^2}) = Tot(O(-3)) = local P^2."""
        result = tot_kx_cy3_data(CP2)
        assert not result['kx_trivial']
        assert 'O(-3)' in result['kx_description']

    def test_s4_not_complex(self):
        """S^4 is not complex, Tot(K_X) not applicable."""
        result = tot_kx_cy3_data(S4)
        assert not result['is_complex']

    def test_k3_status_proved(self):
        """K3 route: proved at d=2."""
        result = tot_kx_cy3_data(K3)
        assert 'proved' in result['chiral_algebra_status']

    def test_cp2_status_conjectural(self):
        """P^2 route: conjectural (CY-A_3)."""
        # AP-CY6: CY-A_3 is the programme
        result = tot_kx_cy3_data(CP2)
        assert 'conjectural' in result['chiral_algebra_status']


# ======================================================================
# 10. S-duality and Langlands duality
# ======================================================================

class TestSDuality:
    """Verify S-duality = Langlands = Koszul for VW invariants."""

    def test_su2_langlands_dual(self):
        """SU(2)^L = SO(3)."""
        assert LANGLANDS_DUAL['SU(2)'] == 'SO(3)'

    def test_so3_langlands_dual(self):
        """SO(3)^L = SU(2)."""
        assert LANGLANDS_DUAL['SO(3)'] == 'SU(2)'

    def test_e8_self_dual(self):
        """E_8 is Langlands self-dual."""
        assert LANGLANDS_DUAL['E_8'] == 'E_8'

    def test_k3_s_duality(self):
        """S-duality data for K3 with SU(2)."""
        result = s_duality_data(K3, 'SU(2)')
        assert result['modular_weight'] == Fraction(-12)
        assert result['langlands_dual'] == 'SO(3)'
        assert not result['is_mock_modular']

    def test_p2_s_duality_mock(self):
        """S-duality for P^2 is mock modular."""
        result = s_duality_data(CP2, 'SU(2)')
        assert result['is_mock_modular']
        assert result['modular_weight'] == Fraction(-3, 2)


# ======================================================================
# 11. Dimensional hierarchy
# ======================================================================

class TestDimensionalHierarchy:
    """Verify the 3d/4d/5d/6d dimensional hierarchy."""

    def test_3d_cs(self):
        """3d CS produces knot invariants (Jones polynomial)."""
        entry = dimensional_hierarchy_entry(3)
        assert entry['defect_dim'] == 1
        assert entry['n_parameters'] == 1
        assert 'proved' in entry['status']

    def test_4d_donaldson(self):
        """4d topological YM produces Donaldson invariants."""
        entry = dimensional_hierarchy_entry(4)
        assert entry['defect_dim'] == 2
        assert 'proved' in entry['status']

    def test_5d_hcs(self):
        """5d hCS produces affine Yangian (boundary algebra proved)."""
        entry = dimensional_hierarchy_entry(5)
        assert entry['defect_dim'] == 3
        assert entry['n_parameters'] == 1

    def test_6d_vw(self):
        """6d (2,0) produces VW invariants of 4-manifolds."""
        entry = dimensional_hierarchy_entry(6)
        assert entry['defect_dim'] == 4
        assert entry['n_parameters'] == 2

    def test_parameter_count_increases(self):
        """Number of parameters increases: 1 (3d) -> 0 (4d) -> 1 (5d) -> 2 (6d)."""
        h = full_hierarchy()
        assert h[3]['n_parameters'] == 1
        assert h[5]['n_parameters'] == 1
        assert h[6]['n_parameters'] == 2

    def test_defect_dim_pattern(self):
        """Defect dimension = theory dimension - 2."""
        h = full_hierarchy()
        for d in [3, 4, 5, 6]:
            assert h[d]['defect_dim'] == d - 2


# ======================================================================
# 12. Freedman/Donaldson constraints
# ======================================================================

class TestFreemanDonaldson:
    """Verify intersection form constraints."""

    def test_k3_spin(self):
        """K3 is spin (even intersection form)."""
        result = verify_freedman_constraints(K3)
        assert result['is_spin']

    def test_cp2_not_spin(self):
        """P^2 is not spin (odd form <1>)."""
        result = verify_freedman_constraints(CP2)
        assert not result['is_spin']

    def test_cp2_definite(self):
        """P^2 has definite form (b_2^- = 0)."""
        result = verify_freedman_constraints(CP2)
        assert result['is_definite']

    def test_k3_not_definite(self):
        """K3 has indefinite form (b_2^+ = 3, b_2^- = 19)."""
        result = verify_freedman_constraints(K3)
        assert not result['is_definite']


# ======================================================================
# 13. 6d compactification data
# ======================================================================

class TestCompactificationData:
    """Verify 6d compactification constructions."""

    def test_k3_t2_proved(self):
        """6d on K3 x T^2 is proved (CY-A_2)."""
        data = compactification_data(K3, genus=1)
        assert data.status == 'proved'
        assert data.vw_weight == Fraction(-12)

    def test_k3_higher_genus_conjectural(self):
        """6d on K3 x Sigma_2 is conjectural."""
        data = compactification_data(K3, genus=2)
        assert data.status == 'conjectural'

    def test_cp2_t2_programme(self):
        """6d on P^2 x T^2 is proved (localization)."""
        data = compactification_data(CP2, genus=1)
        assert data.status == 'proved'  # toric, localization works

    def test_mock_flag(self):
        """Mock modular flag set correctly."""
        k3_data = compactification_data(K3, genus=1)
        cp2_data = compactification_data(CP2, genus=1)
        assert not k3_data.is_mock
        assert cp2_data.is_mock


# ======================================================================
# 14. Surface data table verification
# ======================================================================

class TestSurfaceTable:
    """Verify the complete surface data table."""

    def test_all_surfaces(self):
        """All surfaces in the catalogue have consistent data."""
        results = verify_surface_table()
        for r in results:
            assert r['chi'] is not None
            assert r['weight'] == Fraction(-r['chi'], 2)

    def test_noether_all_complex(self):
        """Noether formula holds for all complex surfaces."""
        results = verify_surface_table()
        for r in results:
            if r['noether_ok'] is not None:
                assert r['noether_ok'], f"Noether fails for {r['name']}"


# ======================================================================
# 15. VW partition function coefficients for non-K3 surfaces
# ======================================================================

class TestVWCoefficients:
    """Verify VW partition function coefficients for various surfaces."""

    def test_t4_trivial(self):
        """T^4 has chi = 0, so Z_VW = 1 (constant)."""
        coeffs = vw_partition_function_coeffs(T4, 5)
        assert coeffs[0] == Fraction(1)
        for n in range(1, 6):
            assert coeffs.get(n, Fraction(0)) == Fraction(0)

    def test_cp2_first_coeffs(self):
        """P^2 partition function: prod 1/(1-q^k)^3.

        First coefficients: 1, 3, 6, 10, 15, 21, ...
        These are binomial(n+2, 2) = triangular numbers shifted.
        Actually: p_{-3}(n), the 3-colored partition function.
        p_{-3}(0) = 1, p_{-3}(1) = 3, p_{-3}(2) = 6+3 = 9... no.
        prod 1/(1-q)^3 = sum (n+1)(n+2)/2 q^n for the geometric series,
        but prod_{k>=1} 1/(1-q^k)^3 is different.

        Direct computation:
        prod_{k>=1} 1/(1-q^k)^3 = (1/(1-q))^3 * (1/(1-q^2))^3 * ...
        Coefficient of q^0: 1
        Coefficient of q^1: 3 (from 1/(1-q)^3)
        Coefficient of q^2: 3+6 = 9? No.
        1/(1-q)^3 = 1 + 3q + 6q^2 + 10q^3 + ...
        1/(1-q^2)^3 contributes at q^2: 3 more
        So at q^2: 6 + 3 = 9? Let me compute directly.

        Actually the coefficients of prod_{k>=1} 1/(1-q^k)^3:
        n=0: 1
        n=1: 3
        n=2: 9
        n=3: 22
        """
        coeffs = vw_partition_function_coeffs(CP2, 5)
        assert int(coeffs[0]) == 1
        assert int(coeffs[1]) == 3
        assert int(coeffs[2]) == 9
        assert int(coeffs[3]) == 22

    def test_s2xs2_first_coeffs(self):
        """S^2 x S^2 partition function: prod 1/(1-q^k)^4.
        n=0: 1
        n=1: 4
        """
        coeffs = vw_partition_function_coeffs(S2_CROSS_S2, 3)
        assert int(coeffs[0]) == 1
        assert int(coeffs[1]) == 4

    def test_integrality_k3(self):
        """All VW coefficients for K3 are positive integers."""
        coeffs = vw_partition_function_coeffs(K3, 6)
        for n in range(7):
            val = coeffs[n]
            assert val.denominator == 1, f"Non-integer at n={n}: {val}"
            assert val > 0, f"Non-positive at n={n}: {val}"

    def test_integrality_cp2(self):
        """All VW coefficients for P^2 are positive integers."""
        coeffs = vw_partition_function_coeffs(CP2, 10)
        for n in range(11):
            val = coeffs[n]
            assert val.denominator == 1, f"Non-integer at n={n}: {val}"
            assert val > 0, f"Non-positive at n={n}: {val}"
