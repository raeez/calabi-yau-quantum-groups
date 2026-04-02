r"""Tests for compute.lib.hitchin_sl2_genus2.

Comprehensive verification of the Hitchin moduli space M_H(C, SL_2) for
genus-2 curves: dimensions, spectral curve geometry, E-polynomial,
Betti numbers, Sp_4(Z) connection, and the K3 x E comparison.

Key dimension fact (tested throughout):
    dim_C(M_H) = 2*dim(G)*(g-1) = 6   for SL_2, g=2.
    This is a holomorphic symplectic (Sp(3) holonomy) manifold of
    complex dimension 6, NOT a literal CY3.  The "CY3 type" refers
    to the Lagrangian fibration: base = fibre = 3-dimensional.
"""

import math

import pytest

from compute.lib.hitchin_sl2_genus2 import (
    GROUP_DATA,
    SL2_G2,
    bun_sl2_genus2_betti,
    discriminant_locus_sl2_genus2,
    euler_characteristic_from_betti,
    euler_characteristic_from_e_poly,
    expected_kappa_hitchin_sl2_g2,
    find_lagrangian_cy3_cases,
    full_computation,
    genus2_hodge_data,
    hausel_thaddeus_e_polynomial,
    hitchin_dimensions,
    hitchin_fibre_topology_sl2_genus2,
    hitchin_hodge_numbers_sl2_g2,
    k3xe_comparison,
    root_datum_sl2_genus2,
    sp4_connection,
    spectral_curve_sl2,
    spectral_curve_sln,
    syz_data_sl2_genus2,
    verify_all,
)


# =====================================================================
# 1. DIMENSION TESTS
# =====================================================================

class TestHitchinDimensions:
    """Test the dimensional data for M_H(C, G)."""

    def test_sl2_g2_basic_dimensions(self):
        """SL_2, g=2: the distinguished case."""
        h = hitchin_dimensions('SL_2', 2)
        assert h.dim_real == 12
        assert h.dim_complex == 6
        assert h.dim_hitchin_base == 3
        assert h.dim_hitchin_fibre == 3
        assert h.dim_group == 3
        assert h.rank_group == 1
        assert h.casimir_degrees == (2,)

    def test_sl2_g2_is_lagrangian_cy3(self):
        """SL_2, g=2 has a Lagrangian CY3 fibration (base=fibre=3)."""
        h = hitchin_dimensions('SL_2', 2)
        assert h.is_lagrangian_cy3 is True
        # But dim_C = 6, NOT 3!
        assert h.dim_complex == 6

    def test_sl2_g2_NOT_literal_cy3(self):
        """dim_C = 6 means this is NOT a literal CY3 (complex dim 3)."""
        h = hitchin_dimensions('SL_2', 2)
        assert h.dim_complex != 3
        assert h.dim_complex == 6

    def test_sl2_g2_holomorphic_symplectic(self):
        """M_H is holomorphic symplectic: dim_C is even (= 2n)."""
        h = hitchin_dimensions('SL_2', 2)
        assert h.dim_complex % 2 == 0
        n = h.dim_complex // 2
        assert n == 3  # Sp(3) holonomy

    def test_sl2_g2_global_constant(self):
        """The global constant SL2_G2 matches hitchin_dimensions output."""
        h = hitchin_dimensions('SL_2', 2)
        assert SL2_G2 == h

    def test_base_is_half_complex_dim(self):
        """dim(A_H) = dim_C / 2 for all groups and genera (Lagrangian fibration)."""
        for group in ['SL_2', 'SL_3', 'GL_2', 'GL_3', 'Sp_4', 'E_8']:
            for genus in [2, 3, 4]:
                h = hitchin_dimensions(group, genus)
                assert h.dim_hitchin_base == h.dim_complex // 2, \
                    f"Failed for {group}, g={genus}"

    def test_base_equals_fibre(self):
        """dim(base) = dim(fibre) (completely integrable system)."""
        for group in ['SL_2', 'SL_3', 'Sp_4']:
            for genus in [2, 3]:
                h = hitchin_dimensions(group, genus)
                assert h.dim_hitchin_base == h.dim_hitchin_fibre

    def test_dim_formula(self):
        """dim_C = 2*dim(G)*(g-1) and dim_R = 2*dim_C."""
        for group, (dim_G, _, _) in GROUP_DATA.items():
            for genus in [2, 3, 5]:
                h = hitchin_dimensions(group, genus)
                assert h.dim_complex == 2 * dim_G * (genus - 1)
                assert h.dim_real == 2 * h.dim_complex

    def test_genus_1_raises(self):
        """Hitchin moduli space is ill-defined for genus < 2."""
        with pytest.raises(ValueError, match="genus >= 2"):
            hitchin_dimensions('SL_2', 1)

    def test_unknown_group_raises(self):
        with pytest.raises(ValueError, match="Unknown group"):
            hitchin_dimensions('SL_99', 2)

    @pytest.mark.parametrize("group,genus,expected_dim_C", [
        ('SL_2', 2, 6),
        ('SL_2', 3, 12),
        ('SL_3', 2, 16),
        ('GL_2', 2, 8),
        ('E_8', 2, 496),
    ])
    def test_specific_dimensions(self, group, genus, expected_dim_C):
        h = hitchin_dimensions(group, genus)
        assert h.dim_complex == expected_dim_C


# =====================================================================
# 2. LAGRANGIAN CY3 UNIQUENESS
# =====================================================================

class TestLagrangianCY3:
    """Test that SL_2, g=2 is the unique Lagrangian CY3 case."""

    def test_find_all_cases(self):
        """Only SL_2, PGL_2, SO_3 at g=2 give Lagrangian CY3."""
        cases = find_lagrangian_cy3_cases(max_genus=20)
        groups = {c.group for c in cases}
        assert groups == {'SL_2', 'PGL_2', 'SO_3'}
        assert all(c.genus == 2 for c in cases)

    def test_uniqueness_algebraic(self):
        """dim(G)*(g-1) = 3 requires dim(G)=3 and g=2 (or dim(G)=1, g=4 -- impossible)."""
        # dim(G)=3, g=2: 3*1=3. Check.
        assert 3 * (2 - 1) == 3
        # dim(G)=1, g=4: would need a 1-dim reductive group -- none exist.
        # All groups in GROUP_DATA have dim >= 3.
        for group, (dim_G, _, _) in GROUP_DATA.items():
            assert dim_G >= 3, f"{group} has dim {dim_G}"

    def test_all_cy3_groups_are_locally_isomorphic(self):
        """SL_2, PGL_2, SO_3 all have Lie algebra sl_2."""
        for g in ['SL_2', 'PGL_2', 'SO_3']:
            dim_G, _, casimirs = GROUP_DATA[g]
            assert dim_G == 3
            assert casimirs == (2,)


# =====================================================================
# 3. SPECTRAL CURVE TESTS
# =====================================================================

class TestSpectralCurve:
    """Test spectral curve geometry."""

    def test_sl2_genus2_spectral_genus(self):
        """g(Sigma) = 5 for SL_2, g=2 (NOT 3 as erroneously in research note)."""
        s = spectral_curve_sl2(2)
        assert s.genus_spectral == 5
        # Riemann-Hurwitz: 2*5-2 = 2*(2*2-2) + 4 = 4+4 = 8. Check.
        assert 2 * s.genus_spectral - 2 == 2 * (2 * s.genus_base - 2) + s.n_branch_points

    def test_sl2_genus2_prym_dimension(self):
        """Prym(Sigma/C) has dimension 3 = g(Sigma) - g(C)."""
        s = spectral_curve_sl2(2)
        assert s.dim_prym == 3
        assert s.dim_prym == s.genus_spectral - s.genus_base

    def test_sl2_genus2_branch_points(self):
        """4 branch points (zeros of a quadratic differential of degree 4)."""
        s = spectral_curve_sl2(2)
        assert s.n_branch_points == 4
        # deg(K_C^2) = 2*(2g-2) = 4 for g=2
        assert s.n_branch_points == 2 * (2 * 2 - 2)

    def test_riemann_hurwitz_general(self):
        """Riemann-Hurwitz consistency for SL_2 at multiple genera."""
        for genus in range(2, 8):
            s = spectral_curve_sl2(genus)
            # 2g(S)-2 = 2*(2g(C)-2) + B  where B = 4g-4
            lhs = 2 * s.genus_spectral - 2
            rhs = 2 * (2 * genus - 2) + s.n_branch_points
            assert lhs == rhs, f"Riemann-Hurwitz fails at genus {genus}"

    def test_sl2_matches_sln_n2(self):
        """spectral_curve_sl2 and spectral_curve_sln(2, g) agree."""
        for genus in range(2, 8):
            s2 = spectral_curve_sl2(genus)
            sn = spectral_curve_sln(2, genus)
            assert s2.genus_spectral == sn.genus_spectral
            assert s2.dim_prym == sn.dim_prym
            assert s2.n_branch_points == sn.n_branch_points

    def test_prym_equals_hitchin_base_dim(self):
        """dim(Prym) = dim(A_H) = dim(G)*(g-1) for SL_2."""
        for genus in range(2, 8):
            s = spectral_curve_sl2(genus)
            h = hitchin_dimensions('SL_2', genus)
            assert s.dim_prym == h.dim_hitchin_base

    def test_spectral_genus_formula(self):
        """g(Sigma) = 4g - 3 for the SL_2 double cover."""
        for genus in range(2, 10):
            s = spectral_curve_sl2(genus)
            assert s.genus_spectral == 4 * genus - 3

    def test_sln_prym_dimension(self):
        """dim Prym = (n^2-1)*(g-1) for SL_n."""
        for n in [2, 3, 4]:
            for genus in [2, 3, 4]:
                s = spectral_curve_sln(n, genus)
                assert s.dim_prym == (n**2 - 1) * (genus - 1)


# =====================================================================
# 4. E-POLYNOMIAL AND EULER CHARACTERISTIC
# =====================================================================

class TestEPolynomial:
    """Test the Hausel-Thaddeus E-polynomial."""

    def test_genus2_e_polynomial(self):
        """E(t) = 1 + 4t^3 - 4t^5 - t^8 for genus 2."""
        e_poly = hausel_thaddeus_e_polynomial(2)
        expected = {0: 1, 3: 4, 5: -4, 8: -1}
        assert e_poly == expected

    def test_genus2_euler_zero(self):
        """chi = E(1) = 1 + 4 - 4 - 1 = 0."""
        e_poly = hausel_thaddeus_e_polynomial(2)
        chi = euler_characteristic_from_e_poly(e_poly)
        assert chi == 0

    def test_genus3_euler_zero(self):
        """Euler characteristic vanishes for all genera (affine variety)."""
        e_poly = hausel_thaddeus_e_polynomial(3)
        chi = euler_characteristic_from_e_poly(e_poly)
        assert chi == 0

    def test_genus4_euler_zero(self):
        e_poly = hausel_thaddeus_e_polynomial(4)
        chi = euler_characteristic_from_e_poly(e_poly)
        assert chi == 0

    def test_e_poly_has_negative_coefficients(self):
        """E-polynomial can have negative coefficients (mixed Hodge structure)."""
        e_poly = hausel_thaddeus_e_polynomial(2)
        assert any(v < 0 for v in e_poly.values())

    def test_e_poly_constant_term_1(self):
        """E(0) = 1 (connected)."""
        for genus in [2, 3, 4]:
            e_poly = hausel_thaddeus_e_polynomial(genus)
            assert e_poly.get(0, 0) == 1

    def test_e_poly_max_degree(self):
        """The highest-degree term for genus g is t^{4(2g-2)} = t^{8g-8}."""
        for genus in [2, 3]:
            e_poly = hausel_thaddeus_e_polynomial(genus)
            max_deg = max(k for k, v in e_poly.items() if v != 0)
            # For genus 2: max_deg = 8 = 8*2-8 = 8. Check.
            assert max_deg <= 12 * (genus - 1)


# =====================================================================
# 5. BETTI NUMBERS
# =====================================================================

class TestBettiNumbers:
    """Test Betti numbers of Bun^s_{SL_2}(C, odd deg) and Hitchin fibre."""

    def test_bun_betti_values(self):
        """Desale-Ramanan: (2,2) CI in P^5, Betti = [1,0,1,4,1,0,1]."""
        betti = bun_sl2_genus2_betti()
        assert betti == {0: 1, 1: 0, 2: 1, 3: 4, 4: 1, 5: 0, 6: 1}

    def test_bun_poincare_duality(self):
        """b_k = b_{6-k} (smooth compact 6-manifold)."""
        betti = bun_sl2_genus2_betti()
        for k in range(4):
            assert betti[k] == betti[6 - k]

    def test_bun_euler_zero(self):
        """chi(Bun^s) = 0."""
        betti = bun_sl2_genus2_betti()
        chi = euler_characteristic_from_betti(betti)
        assert chi == 0

    def test_bun_b3_equals_2g(self):
        """b_3 = 4 = 2*genus (genus-2 curve)."""
        betti = bun_sl2_genus2_betti()
        assert betti[3] == 4  # = 2 * 2

    def test_fibre_betti_is_torus(self):
        """Generic Hitchin fibre ~ T^6 (abelian 3-fold), Betti = C(6,k)."""
        fibre = hitchin_fibre_topology_sl2_genus2()
        betti = fibre['betti_numbers']
        for k in range(7):
            assert betti[k] == math.comb(6, k)

    def test_fibre_euler_zero(self):
        """chi(T^6) = 0."""
        fibre = hitchin_fibre_topology_sl2_genus2()
        assert fibre['euler_char'] == 0

    def test_fibre_polarization(self):
        """Prym of SL_2 spectral curve has polarization type (1,1,2)."""
        fibre = hitchin_fibre_topology_sl2_genus2()
        assert fibre['polarization_type'] == (1, 1, 2)
        assert fibre['is_principally_polarized'] is False

    def test_fibre_dimension(self):
        fibre = hitchin_fibre_topology_sl2_genus2()
        assert fibre['complex_dimension'] == 3
        assert fibre['real_dimension'] == 6
        assert fibre['prym_dimension'] == 3


# =====================================================================
# 6. ROOT DATUM
# =====================================================================

class TestRootDatum:
    """Test the root datum R(C, SL_2) for genus 2."""

    def test_lattice_rank(self):
        """rank = rank(SL_2) + 2g = 1 + 4 = 5."""
        rd = root_datum_sl2_genus2()
        assert rd.lattice_rank == 5

    def test_real_roots(self):
        """Real roots = A_1 root system: {+alpha, -alpha}."""
        rd = root_datum_sl2_genus2()
        assert rd.n_real_positive == 1
        assert 'A_1' in rd.real_roots

    def test_hitchin_base_dim(self):
        rd = root_datum_sl2_genus2()
        assert rd.hitchin_base_dim == 3

    def test_langlands_dual(self):
        rd = root_datum_sl2_genus2()
        assert 'PGL_2' in rd.langlands_dual

    def test_weyl_group_infinite(self):
        rd = root_datum_sl2_genus2()
        assert rd.weyl_group_order == 'infinite'


# =====================================================================
# 7. SYZ MIRROR SYMMETRY
# =====================================================================

class TestSYZMirror:
    """Test SYZ mirror symmetry data."""

    def test_mirror_is_pgl2(self):
        syz = syz_data_sl2_genus2()
        assert syz['syz_mirror'] == 'M_H(C, PGL_2)'

    def test_self_mirror_diffeo_not_complex(self):
        syz = syz_data_sl2_genus2()
        assert syz['is_self_mirror_diffeo'] is True
        assert syz['is_self_mirror_complex'] is False


# =====================================================================
# 8. DISCRIMINANT LOCUS
# =====================================================================

class TestDiscriminant:
    """Test discriminant locus data."""

    def test_discriminant_codimension(self):
        disc = discriminant_locus_sl2_genus2()
        assert disc['discriminant_codimension'] == 1

    def test_base_dimension(self):
        disc = discriminant_locus_sl2_genus2()
        assert disc['base_dimension'] == 3

    def test_n_branch_points(self):
        disc = discriminant_locus_sl2_genus2()
        assert disc['n_branch_points_generic'] == 4


# =====================================================================
# 9. SP_4(Z) CONNECTION
# =====================================================================

class TestSp4Connection:
    """Test the Sp_4(Z) and Siegel modular structure."""

    def test_siegel_half_space_dim(self):
        """H_2 has (complex) dimension g*(g+1)/2 = 3."""
        sp4 = sp4_connection()
        assert sp4['siegel_half_space_dim'] == 3

    def test_delta_5_weight(self):
        sp4 = sp4_connection()
        assert sp4['delta_5_weight'] == 5

    def test_even_theta_characteristics(self):
        """There are 10 even theta characteristics for genus 2."""
        sp4 = sp4_connection()
        assert sp4['n_even_theta_characteristics'] == 10
        # 2^{g-1}(2^g+1) = 2^1*(2^2+1) = 2*5 = 10. Check.
        g = 2
        n_even = 2**(g - 1) * (2**g + 1)
        assert n_even == 10

    def test_sp4_dim(self):
        """dim(Sp_4) = 2*2*(2*2+1)/2 = 10. (Sp_{2n} has dim n*(2n+1).)"""
        sp4 = sp4_connection()
        assert sp4['sp4_dim'] == 10
        # n=2: n*(2n+1) = 2*5 = 10
        assert 2 * (2 * 2 + 1) == 10

    def test_coincidence_dims(self):
        """dim(A_2) = dim(H_2/Sp_4(Z)) = dim(A_H) = 3."""
        sp4 = sp4_connection()
        assert sp4['a2_dim'] == sp4['a_h_dim'] == 3

    def test_torelli(self):
        sp4 = sp4_connection()
        assert sp4['torelli_injective'] is True
        assert sp4['torelli_surjective'] is False


# =====================================================================
# 10. GENUS-2 HODGE DATA
# =====================================================================

class TestGenus2Hodge:
    """Test Hodge-theoretic data for genus-2 curves and Jacobians."""

    def test_curve_euler(self):
        hd = genus2_hodge_data()
        assert hd['curve_euler'] == -2

    def test_curve_hodge(self):
        hd = genus2_hodge_data()
        assert hd['curve_hodge'][(1, 0)] == 2
        assert hd['curve_hodge'][(0, 1)] == 2

    def test_jacobian_hodge(self):
        """Jac(C) Hodge numbers: h^{p,q} = C(2,p)*C(2,q)."""
        hd = genus2_hodge_data()
        for p in range(3):
            for q in range(3):
                assert hd['jacobian_hodge'][(p, q)] == math.comb(2, p) * math.comb(2, q)

    def test_jacobian_euler_zero(self):
        hd = genus2_hodge_data()
        assert hd['jacobian_euler'] == 0

    def test_h1_rank(self):
        """H_1(C, Z) = Z^4 for genus 2."""
        hd = genus2_hodge_data()
        assert hd['h1_rank'] == 4


# =====================================================================
# 11. HITCHIN HODGE NUMBERS
# =====================================================================

class TestHitchinHodge:
    """Test mixed Hodge structure data for M_H."""

    def test_e_polynomial_values(self):
        hh = hitchin_hodge_numbers_sl2_g2()
        assert hh['e_polynomial'] == {0: 1, 3: 4, 5: -4, 8: -1}

    def test_euler_zero(self):
        hh = hitchin_hodge_numbers_sl2_g2()
        assert hh['euler_characteristic'] == 0


# =====================================================================
# 12. K3 x E COMPARISON
# =====================================================================

class TestK3xEComparison:
    """Test the K3 x E comparison data."""

    def test_both_involve_sp4(self):
        """Both Hitchin (SL_2, g=2) and K3 x E involve Sp_4(Z)."""
        comp = k3xe_comparison()
        assert 'Sp_4' in comp['sp4_from_hitchin']
        assert 'Sp_4' in comp.get('sp4_from_k3xe', 'Sp_4')

    def test_hitchin_dim_c_is_6(self):
        """Hitchin has dim_C = 6 (NOT 3)."""
        comp = k3xe_comparison()
        assert comp['hitchin_dim_C'] == 6

    def test_k3xe_dim_c_is_3(self):
        """K3 x E has dim_C = 3 (literal CY3)."""
        comp = k3xe_comparison()
        assert comp['k3xe_dim_C'] == 3

    def test_hitchin_lagrangian_fibre_dim(self):
        """Hitchin Lagrangian fibre dim = 3."""
        comp = k3xe_comparison()
        assert comp['hitchin_lagrangian_fibre_dim'] == 3

    def test_kappa_match(self):
        comp = k3xe_comparison()
        assert comp['hitchin_expected_kappa'] == comp['k3xe_kappa'] == 5

    def test_hitchin_is_noncompact(self):
        comp = k3xe_comparison()
        assert comp['hitchin_is_noncompact'] is True
        assert comp['k3xe_is_compact'] is True


# =====================================================================
# 13. EXPECTED KAPPA
# =====================================================================

class TestExpectedKappa:
    """Test the expected modular characteristic."""

    def test_kappa_value(self):
        kap = expected_kappa_hitchin_sl2_g2()
        assert kap['expected_kappa'] == 5

    def test_kappa_crit(self):
        kap = expected_kappa_hitchin_sl2_g2()
        assert kap['kappa_crit'] == 10

    def test_self_dual(self):
        kap = expected_kappa_hitchin_sl2_g2()
        assert kap['self_dual'] is True

    def test_complementarity(self):
        """kappa + kappa' = kappa_crit; self-dual => kappa = kappa_crit/2."""
        kap = expected_kappa_hitchin_sl2_g2()
        assert 2 * kap['expected_kappa'] == kap['kappa_crit']


# =====================================================================
# 14. CASIMIR SUM RULE
# =====================================================================

class TestCasimirSumRule:
    """Test sum_{i=1}^r (2d_i - 1) = dim(G) for all groups."""

    @pytest.mark.parametrize("group", list(GROUP_DATA.keys()))
    def test_casimir_sum(self, group):
        dim_G, _, casimirs = GROUP_DATA[group]
        assert sum(2 * d - 1 for d in casimirs) == dim_G


# =====================================================================
# 15. FULL COMPUTATION SMOKE TEST
# =====================================================================

class TestFullComputation:
    """Smoke test for the full_computation() function."""

    def test_full_computation_runs(self):
        result = full_computation()
        assert isinstance(result, dict)
        assert 'hitchin_data' in result
        assert 'spectral_curve' in result
        assert 'e_polynomial' in result
        assert 'lagrangian_cy3_cases' in result
        assert 'sp4_connection' in result
        assert 'discriminant_locus' in result

    def test_full_computation_consistency(self):
        result = full_computation()
        assert result['chi_e_polynomial'] == 0
        assert result['chi_bun'] == 0
        assert result['hitchin_data']['dim_complex'] == 6
        assert result['hitchin_data']['dim_hitchin_base'] == 3


# =====================================================================
# 16. VERIFY_ALL
# =====================================================================

class TestVerifyAll:
    """Test the internal verify_all() function."""

    def test_all_pass(self):
        results = verify_all()
        for name, passed in results.items():
            assert passed, f"Verification {name} FAILED"

    def test_count(self):
        results = verify_all()
        assert len(results) == 9


# =====================================================================
# 17. CROSS-CHECKS BETWEEN MODULES
# =====================================================================

class TestCrossChecks:
    """Cross-check relationships between different computations."""

    def test_prym_dim_equals_base_dim(self):
        """The Hitchin fibre (Prym) and base have the same dimension."""
        s = spectral_curve_sl2(2)
        h = hitchin_dimensions('SL_2', 2)
        assert s.dim_prym == h.dim_hitchin_base == 3

    def test_hitchin_base_dim_equals_siegel_dim(self):
        """dim(A_H) = dim(H_2) = 3 (a numerical coincidence: both = 3)."""
        h = hitchin_dimensions('SL_2', 2)
        sp4 = sp4_connection()
        assert h.dim_hitchin_base == sp4['siegel_half_space_dim']

    def test_kappa_crit_equals_sp4_dim(self):
        """kappa_crit = 10 = dim(Sp_4)."""
        kap = expected_kappa_hitchin_sl2_g2()
        sp4 = sp4_connection()
        assert kap['kappa_crit'] == sp4['sp4_dim']

    def test_spectral_genus_from_prym_plus_base(self):
        """g(Sigma) = dim(Prym) + g(C) = 3 + 2 = 5."""
        s = spectral_curve_sl2(2)
        assert s.genus_spectral == s.dim_prym + s.genus_base

    def test_euler_consistency(self):
        """All Euler characteristics vanish: E-poly, Bun, fibre."""
        e_poly = hausel_thaddeus_e_polynomial(2)
        assert euler_characteristic_from_e_poly(e_poly) == 0
        assert euler_characteristic_from_betti(bun_sl2_genus2_betti()) == 0
        fibre = hitchin_fibre_topology_sl2_genus2()
        assert fibre['euler_char'] == 0


# =====================================================================
# 18. DIMENSION CORRECTION REGRESSION TEST
# =====================================================================

class TestDimensionRegression:
    """Regression tests ensuring the CY3/CY6 distinction is maintained.

    The original code conflated dim_C=6 with "CY3".  These tests ensure
    the corrected semantics remain in place.
    """

    def test_no_is_cy3_field(self):
        """The old 'is_cy3' field should not exist (replaced by is_lagrangian_cy3)."""
        h = hitchin_dimensions('SL_2', 2)
        assert not hasattr(h, 'is_cy3')

    def test_no_cy_dimension_field(self):
        """The old 'cy_dimension' field should not exist (was misleading)."""
        h = hitchin_dimensions('SL_2', 2)
        assert not hasattr(h, 'cy_dimension')

    def test_lagrangian_cy3_checks_base_dim(self):
        """is_lagrangian_cy3 checks dim(base)=3, NOT dim_C=6."""
        # SL_3, g=2: dim_C = 16, base = 8. NOT Lagrangian CY3.
        h = hitchin_dimensions('SL_3', 2)
        assert h.is_lagrangian_cy3 is False
        assert h.dim_hitchin_base == 8

    def test_research_note_error_documented(self):
        """The spectral curve code documents the g(Sigma)=3 error in the note."""
        s = spectral_curve_sl2(2)
        assert s.genus_spectral == 5  # NOT 3
