r"""Tests for compute.lib.hitchin_spectral_yangian.

Comprehensive verification of the explicit Hitchin--Yangian spectral
parameter identification: Sigma -> z = lambda -> R(z) -> Bethe ansatz.

Verifies:
  1. Spectral curve geometry: genus formula, branch points, embeddings
  2. Spectral identification: z = lambda, geometric reason, AP compliance
  3. R-matrix on the spectral curve: unitarity, YBE, zeros/poles
  4. Bethe ansatz on Sigma: transfer matrix, magnon space, BAE geometry
  5. A_1 double cover: genus = 4g-3, Prym = 3(g-1), CY3-type at g=2
  6. Full identification chain: all five steps, consistency checks
  7. Transfer matrix as function on Sigma: normalisation, asymptotics
  8. Cross-engine bridge: consistency with existing engines
  9. Master verification: 100+ internal checks
  10. Parametric landscape: all standard types and genera

Ground truth (multi-path verified):
  - Riemann-Hurwitz: g(Sigma) = n^2*(g-1)+1 for degree-n cover [DC][LT]
  - Branch points: B = n*(n-1)*(2g-2) [DC][LT]
  - K3 adjunction: K_C = L|_C since K_S = O_S [LT]
  - Structure function: g(z)*g(-z) = 1 (algebraic unitarity) [DC]
  - CY_2 constraint: sum h_i = 0 [DC]
  - Kummer: h_i = eps (i=1..4), -eps/5 (i=5..24) [DC]
  - A_1 Prym: dim = g(Sigma) - g(C) = 3(g-1) [DC][LT]
  - Hitchin base: dim B = dim(g)*(g-1) [LT]
  - Transfer normalisation: T(z) -> 1 as z -> inf [DC]
  - AP-CY31: z is Yangian spectral, NOT worldsheet [LT]

113 tests organised by mathematical structure.
"""

from fractions import Fraction as F

import pytest

from compute.lib.hitchin_spectral_yangian import (
    A1DoubleCoverData,
    BetheOnSpectralCurveData,
    HitchinYangianChainData,
    RMatrixSpectralData,
    SpectralCurveK3Data,
    SpectralIdentificationData,
    _kummer_h_params,
    _structure_function,
    _transfer_matrix_eigenvalue,
    _verify_bae_residual,
    a1_double_cover,
    bethe_on_spectral_curve,
    branch_points_generic,
    cross_engine_bridge,
    full_identification_chain,
    rmatrix_on_spectral_curve,
    spectral_curve_genus,
    spectral_curve_k3,
    spectral_identification,
    transfer_matrix_on_sigma,
    verify_all,
)

# Cross-engine imports for multi-path verification [CF]
from compute.lib.chiral_hitchin_k3 import (
    hitchin_on_k3 as chk3_hitchin_on_k3,
    spectral_parameter_k3 as chk3_spectral_parameter,
)
from compute.lib.spectral_curve_chiral import (
    spectral_curve_genus_gln as scc_genus_gln,
    spectral_curve_data_gln as scc_data_gln,
    hitchin_base_dim_sln as scc_base_sln,
)
from compute.lib.geometric_langlands_shadow import (
    lie_data as gls_lie_data,
)


# ======================================================================
# 1. SPECTRAL CURVE GEOMETRY
# ======================================================================

class TestSpectralCurveGenus:
    """Spectral curve genus: g(Sigma) = n^2*(g-1) + 1."""

    def test_sl2_genus2(self):
        """SL_2, g=2: g(Sigma) = 4*1+1 = 5."""
        # VERIFIED [DC] 4*1+1=5 [LT] Riemann-Hurwitz
        assert spectral_curve_genus(2, 2) == 5

    def test_sl2_genus3(self):
        """SL_2, g=3: g(Sigma) = 4*2+1 = 9."""
        # VERIFIED [DC] 4*2+1=9 [LT] Riemann-Hurwitz
        assert spectral_curve_genus(2, 3) == 9

    def test_sl2_genus4(self):
        """SL_2, g=4: g(Sigma) = 4*3+1 = 13."""
        # VERIFIED [DC] 4*3+1=13
        assert spectral_curve_genus(2, 4) == 13

    def test_sl3_genus2(self):
        """SL_3, g=2: g(Sigma) = 9*1+1 = 10."""
        # VERIFIED [DC] 9*1+1=10
        assert spectral_curve_genus(3, 2) == 10

    def test_sl4_genus2(self):
        """SL_4, g=2: g(Sigma) = 16*1+1 = 17."""
        # VERIFIED [DC] 16+1=17
        assert spectral_curve_genus(4, 2) == 17

    @pytest.mark.parametrize("n,g,expected", [
        (2, 2, 5), (2, 3, 9), (2, 4, 13), (2, 5, 17),
        (3, 2, 10), (3, 3, 19), (3, 4, 28),
        (4, 2, 17), (4, 3, 33),
        (5, 2, 26), (5, 3, 51),
    ])
    def test_spectral_genus_parametric(self, n, g, expected):
        """Parametric check: g(Sigma) = n^2*(g-1)+1."""
        # VERIFIED [DC] direct computation
        assert spectral_curve_genus(n, g) == expected

    def test_genus_n1(self):
        """n=1: trivial cover, g(Sigma) = g(C)."""
        # VERIFIED [DC] 1^2*(g-1)+1 = g
        for g in range(2, 6):
            assert spectral_curve_genus(1, g) == g

    def test_invalid_n(self):
        """n < 1 raises ValueError."""
        with pytest.raises(ValueError, match="Cover degree"):
            spectral_curve_genus(0, 2)


class TestBranchPoints:
    """Branch points: B = n*(n-1)*(2g-2)."""

    def test_sl2_genus2(self):
        """SL_2, g=2: B = 2*1*2 = 4."""
        # VERIFIED [DC] 2*1*2=4 [LT] discriminant of char poly
        assert branch_points_generic(2, 2) == 4

    def test_sl2_genus3(self):
        """SL_2, g=3: B = 2*1*4 = 8."""
        # VERIFIED [DC] 2*1*4=8
        assert branch_points_generic(2, 3) == 8

    def test_sl3_genus2(self):
        """SL_3, g=2: B = 3*2*2 = 12."""
        # VERIFIED [DC] 3*2*2=12
        assert branch_points_generic(3, 2) == 12

    @pytest.mark.parametrize("n,g,expected", [
        (2, 2, 4), (2, 3, 8), (2, 4, 12),
        (3, 2, 12), (3, 3, 24),
        (4, 2, 24), (4, 3, 48),
    ])
    def test_branch_parametric(self, n, g, expected):
        """Parametric branch point check."""
        # VERIFIED [DC] direct computation
        assert branch_points_generic(n, g) == expected


class TestSpectralCurveK3:
    """Full spectral curve data for C subset K3."""

    def test_sl2_genus2_embedding(self):
        """Spectral curve embeds in Tot(L|_C)."""
        # VERIFIED [LT] K3 adjunction K_C = L|_C
        sc = spectral_curve_k3(2, 'A', 1)
        assert 'Tot(L|_C)' in sc.spectral_embeds_in

    def test_sl2_genus2_adjunction(self):
        """Adjunction: K_C = L|_C."""
        sc = spectral_curve_k3(2, 'A', 1)
        assert 'K_C = L|_C' in sc.adjunction

    def test_sl2_genus2_char_poly_degree(self):
        """SL_2: char poly has degree 2 in lambda."""
        # VERIFIED [DC] det of 2x2 matrix is degree 2
        sc = spectral_curve_k3(2, 'A', 1)
        assert sc.char_poly_degree == 2

    def test_sl3_genus2_char_poly_degree(self):
        """SL_3: char poly has degree 3."""
        sc = spectral_curve_k3(2, 'A', 2)
        assert sc.char_poly_degree == 3

    def test_sl2_genus2_hitchin_base(self):
        """dim B(SL_2, g=2) = 3."""
        # VERIFIED [DC] dim(sl2)*(2-1) = 3 [CF] chiral_hitchin_k3
        sc = spectral_curve_k3(2, 'A', 1)
        assert sc.dim_hitchin_base == 3

    def test_e8_genus2_hitchin_base(self):
        """dim B(E_8, g=2) = 248."""
        # VERIFIED [DC] dim(E8)*(2-1) = 248 [CF] chiral_hitchin_k3
        sc = spectral_curve_k3(2, 'E', 8)
        assert sc.dim_hitchin_base == 248

    def test_L_square(self):
        """L^2 = 2g-2 for all genera."""
        for g in [2, 3, 4, 5]:
            sc = spectral_curve_k3(g, 'A', 1)
            assert sc.L_square == 2 * g - 2

    def test_genus_error(self):
        """genus < 2 raises."""
        with pytest.raises(ValueError, match="genus >= 2"):
            spectral_curve_k3(1, 'A', 1)


# ======================================================================
# 2. SPECTRAL PARAMETER IDENTIFICATION
# ======================================================================

class TestSpectralIdentification:
    """z = lambda identification (conjectural)."""

    def test_status_conjectured(self):
        """Identification is conjectural (AP-CY14)."""
        ident = spectral_identification(2, 'A', 1)
        assert ident.status == 'Conjectured'

    def test_hitchin_fibre_dim(self):
        """Fibre dimension = 1 (line bundle L|_C)."""
        # VERIFIED [DC] rank-1 bundle [LT] L is a line bundle
        ident = spectral_identification(2, 'A', 1)
        assert ident.hitchin_fibre_dim == 1

    def test_depends_on_cya2(self):
        """Depends on CY-A_2."""
        ident = spectral_identification(2, 'A', 1)
        assert any('CY-A_2' in d for d in ident.depends_on)

    def test_depends_on_ygk3(self):
        """Depends on Y(g_{K3}) existence."""
        ident = spectral_identification(2, 'A', 1)
        assert any('Y(g_{K3})' in d for d in ident.depends_on)

    def test_ap_cy31_compliance(self):
        """AP-CY31: z is spectral, not worldsheet."""
        ident = spectral_identification(2, 'A', 1)
        assert 'AP-CY31' in ident.yangian_parameter

    def test_geometric_reason_adjunction(self):
        """Geometric reason mentions K3 adjunction."""
        ident = spectral_identification(2, 'A', 1)
        assert 'adjunction' in ident.geometric_reason.lower()

    def test_identification_text(self):
        """Identification text contains z = lambda."""
        ident = spectral_identification(2, 'A', 1)
        assert 'z = lambda' in ident.identification

    def test_genus_error(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            spectral_identification(1, 'A', 1)


# ======================================================================
# 3. R-MATRIX ON THE SPECTRAL CURVE
# ======================================================================

class TestRMatrixSpectral:
    """R-matrix evaluated at spectral points on Sigma."""

    def test_unitarity(self):
        """g(z)*g(-z) = 1 (algebraic unitarity)."""
        # VERIFIED [DC] factorwise cancellation [LT] CY structure
        rm = rmatrix_on_spectral_curve(2)
        assert rm.unitarity is True

    def test_unitarity_explicit(self):
        """Explicit unitarity check at sample point."""
        rm = rmatrix_on_spectral_curve(2)
        assert abs(rm.g_reflection - 1.0) < 1e-10

    def test_diagonal(self):
        """R-matrix is diagonal for gl_1 (abelian)."""
        rm = rmatrix_on_spectral_curve(2)
        assert rm.is_diagonal is True

    def test_ybe(self):
        """YBE satisfied (trivially for diagonal)."""
        rm = rmatrix_on_spectral_curve(2)
        assert rm.satisfies_ybe is True

    def test_24_zeros(self):
        """24 zeros of g(z) at z = h_i."""
        rm = rmatrix_on_spectral_curve(2)
        assert len(rm.zeros_of_g) == 24

    def test_24_poles(self):
        """24 poles of g(z) at z = -h_i."""
        rm = rmatrix_on_spectral_curve(2)
        assert len(rm.poles_of_g) == 24

    def test_n_params_24(self):
        """24 Mukai lattice parameters."""
        rm = rmatrix_on_spectral_curve(2)
        assert rm.n_params == 24

    def test_cy2_constraint(self):
        """sum h_i = 0 (CY_2 constraint)."""
        # VERIFIED [DC] 4*eps + 20*(-eps/5) = 0
        rm = rmatrix_on_spectral_curve(2)
        assert abs(sum(rm.h_params)) < 1e-10

    @pytest.mark.parametrize("eps", [0.5, 1.0, 2.0, 3.7])
    def test_unitarity_multiple_eps(self, eps):
        """Unitarity holds for all eps (CY property)."""
        rm = rmatrix_on_spectral_curve(2, eps=eps)
        assert rm.unitarity is True

    def test_genus_error(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            rmatrix_on_spectral_curve(1)


# ======================================================================
# 4. STRUCTURE FUNCTION PROPERTIES
# ======================================================================

class TestStructureFunction:
    """Direct tests of g(z) = prod (z-h_i)/(z+h_i)."""

    def test_g_at_infinity(self):
        """g(z) -> 1 as z -> infinity."""
        # VERIFIED [DC] leading coefficient ratio = 1
        h = _kummer_h_params(1.0)
        g_large = _structure_function(10000.0 + 0.0j, h)
        assert abs(g_large - 1.0) < 1e-4

    def test_g_at_zero_exact(self):
        """g(0) = (-1)^24 = 1 computed exactly via limit.

        g(0) = prod_i (0-h_i)/(0+h_i) = prod_i (-1) = (-1)^24 = 1.
        We evaluate at z=0 directly (no offset needed since z=0 is
        not a pole; poles are at z=-h_i, not z=0).
        """
        # VERIFIED [DC] prod(-h_i/h_i) = prod(-1) = (-1)^24 = 1
        h = _kummer_h_params(1.0)
        # z=0 is not a pole (poles are at z = -h_i = -1 and +0.2)
        g0 = _structure_function(0.0, h)
        assert abs(g0 - 1.0) < 1e-10

    def test_g_at_zero_multiple_eps(self):
        """g(0) = 1 for all eps (exact evaluation)."""
        # VERIFIED [DC] (-1)^24 = 1, independent of eps
        for eps in [0.3, 1.0, 2.5]:
            h = _kummer_h_params(eps)
            g0 = _structure_function(0.0, h)
            assert abs(g0 - 1.0) < 1e-10

    def test_g_reflection_identity(self):
        """g(z)*g(-z) = 1 for multiple z values."""
        h = _kummer_h_params(1.0)
        for z in [2.5 + 0.3j, 5.0 - 1.0j, 0.7 + 3.0j, 10.0 + 0.1j]:
            g1 = _structure_function(z, h)
            g2 = _structure_function(-z, h)
            assert abs(g1 * g2 - 1.0) < 1e-10, f"Failed at z={z}"

    def test_kummer_cy2(self):
        """CY_2 constraint: sum h_i = 0."""
        for eps in [0.5, 1.0, 2.0, 5.0]:
            h = _kummer_h_params(eps)
            assert abs(sum(h)) < 1e-10

    def test_kummer_4_positive_20_negative(self):
        """Kummer: 4 positive h_i, 20 negative h_i."""
        h = _kummer_h_params(1.0)
        n_pos = sum(1 for x in h if x > 0)
        n_neg = sum(1 for x in h if x < 0)
        assert n_pos == 4
        assert n_neg == 20


# ======================================================================
# 5. BETHE ANSATZ ON SIGMA
# ======================================================================

class TestBetheOnSpectralCurve:
    """Bethe ansatz with magnons living on the spectral curve."""

    def test_spectral_genus(self):
        """Bethe data carries correct spectral genus."""
        ba = bethe_on_spectral_curve(2, n_magnons=2)
        assert ba.genus_spectral == 5

    def test_magnon_count(self):
        """Correct number of magnons."""
        ba = bethe_on_spectral_curve(2, n_magnons=3)
        assert ba.n_magnons == 3

    def test_status_conjectured(self):
        """K3 Bethe ansatz is conjectural."""
        ba = bethe_on_spectral_curve(2)
        assert ba.status == 'Conjectured'

    def test_cover_degree_2(self):
        """SL_2 spectral cover has degree 2."""
        ba = bethe_on_spectral_curve(2)
        assert ba.cover_degree == 2

    def test_transfer_eigenvalue_nonzero(self):
        """Transfer matrix eigenvalue is nonzero at generic point."""
        ba = bethe_on_spectral_curve(2, n_magnons=2)
        assert abs(ba.transfer_eigenvalue) > 1e-10

    def test_genus_error(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            bethe_on_spectral_curve(1)


class TestTransferMatrix:
    """Transfer matrix T(z) as a function on Sigma."""

    def test_normalisation_at_infinity(self):
        """T(z) -> 1 as z -> infinity."""
        # VERIFIED [DC] g(inf)=1 => product of g(inf-u_i) -> 1
        h = _kummer_h_params(1.0)
        bethe_roots = (10.0 + 0.5j, 13.0 + 0.5j)
        t_inf = _transfer_matrix_eigenvalue(10000.0 + 0.0j, bethe_roots, h)
        assert abs(t_inf - 1.0) < 0.01

    def test_transfer_on_sigma(self):
        """Transfer matrix at multiple points."""
        z_pts = (5.3 + 0.2j, 7.1 - 0.3j, 12.0 + 1.0j)
        bethe_roots = (10.0 + 0.5j, 13.0 + 0.5j)
        result = transfer_matrix_on_sigma(z_pts, bethe_roots)
        assert len(result['eigenvalues']) == 3
        assert result['normalised'] is True

    def test_transfer_nonzero(self):
        """Eigenvalues are nonzero at generic points."""
        z_pts = (5.3 + 0.2j,)
        bethe_roots = (10.0 + 0.5j,)
        result = transfer_matrix_on_sigma(z_pts, bethe_roots)
        assert abs(result['eigenvalues'][0]) > 1e-10

    def test_no_bethe_roots_trivial(self):
        """With no Bethe roots, T(z) = 1 (empty product)."""
        z_pts = (5.0 + 0.1j,)
        result = transfer_matrix_on_sigma(z_pts, ())
        assert abs(result['eigenvalues'][0] - 1.0) < 1e-10


class TestBAEResidual:
    """BAE residual computation."""

    def test_single_magnon_trivial(self):
        """Single magnon: no BAE constraint (empty product)."""
        h = _kummer_h_params(1.0)
        res = _verify_bae_residual((10.0 + 0.5j,), h)
        assert res == 0.0

    def test_zero_magnons_trivial(self):
        """Zero magnons: trivially satisfied."""
        h = _kummer_h_params(1.0)
        res = _verify_bae_residual((), h)
        assert res == 0.0


# ======================================================================
# 6. A_1 DOUBLE COVER
# ======================================================================

class TestA1DoubleCover:
    """A_1 (SL_2) spectral curve: double cover Sigma -> C."""

    def test_genus2_spectral_genus(self):
        """g=2: g(Sigma) = 4*2-3 = 5."""
        # VERIFIED [DC] 4g-3 = 5 [DC] n^2(g-1)+1 = 5
        a1 = a1_double_cover(2)
        assert a1.genus_spectral == 5

    def test_genus3_spectral_genus(self):
        """g=3: g(Sigma) = 4*3-3 = 9."""
        # VERIFIED [DC] 4g-3 = 9
        a1 = a1_double_cover(3)
        assert a1.genus_spectral == 9

    def test_genus4_spectral_genus(self):
        """g=4: g(Sigma) = 4*4-3 = 13."""
        a1 = a1_double_cover(4)
        assert a1.genus_spectral == 13

    @pytest.mark.parametrize("g,expected", [
        (2, 5), (3, 9), (4, 13), (5, 17), (6, 21), (10, 37),
    ])
    def test_genus_formula_parametric(self, g, expected):
        """g(Sigma) = 4g - 3 for all g >= 2."""
        # VERIFIED [DC] 4g-3
        a1 = a1_double_cover(g)
        assert a1.genus_spectral == expected

    def test_genus2_branch_points(self):
        """g=2: 4 branch points."""
        # VERIFIED [DC] 4g-4 = 4
        a1 = a1_double_cover(2)
        assert a1.n_branch_points == 4

    def test_genus3_branch_points(self):
        """g=3: 8 branch points."""
        a1 = a1_double_cover(3)
        assert a1.n_branch_points == 8

    @pytest.mark.parametrize("g", [2, 3, 4, 5])
    def test_branch_formula(self, g):
        """B = 4g-4 for A_1."""
        # VERIFIED [DC] n(n-1)(2g-2) = 2*1*(2g-2) = 4g-4
        a1 = a1_double_cover(g)
        assert a1.n_branch_points == 4 * g - 4

    def test_genus2_prym_dim(self):
        """g=2: Prym dim = 3 (CY3-type Hitchin fibre)."""
        # VERIFIED [DC] g(Sigma)-g(C) = 5-2 = 3 [LT] Lagrangian fibre dim
        a1 = a1_double_cover(2)
        assert a1.prym_dim == 3

    @pytest.mark.parametrize("g", [2, 3, 4, 5])
    def test_prym_formula(self, g):
        """Prym dim = 3*(g-1) = dim(SL_2)*(g-1)."""
        # VERIFIED [DC] 3(g-1) [LT] Hitchin fibre = Prym
        a1 = a1_double_cover(g)
        assert a1.prym_dim == 3 * (g - 1)

    def test_genus2_cy3_type(self):
        """g=2 is CY3-type (unique case with Prym dim = 3)."""
        # VERIFIED [DC] 3*(2-1) = 3 [LT] unique CY3-type Hitchin
        a1 = a1_double_cover(2)
        assert a1.is_cy3_type is True

    def test_genus3_not_cy3_type(self):
        """g=3 is NOT CY3-type (Prym dim = 6)."""
        a1 = a1_double_cover(3)
        assert a1.is_cy3_type is False

    def test_hyperelliptic(self):
        """A_1 spectral curve is a degree-2 cover (hyperelliptic)."""
        a1 = a1_double_cover(2)
        assert a1.is_hyperelliptic_cover is True

    def test_deg_quadratic_diff(self):
        """deg(K_C^2) = 4g-4."""
        for g in [2, 3, 4]:
            a1 = a1_double_cover(g)
            assert a1.deg_quadratic_diff == 4 * g - 4

    def test_hitchin_base_dim(self):
        """dim H^0(K_C^2) = 3(g-1)."""
        for g in [2, 3, 4]:
            a1 = a1_double_cover(g)
            assert a1.hitchin_base_dim == 3 * (g - 1)

    def test_sheet_exchange_lambda_neg(self):
        """Galois involution: lambda -> -lambda."""
        a1 = a1_double_cover(2)
        assert '-lambda' in a1.sheet_exchange

    def test_eigenvalue_interpretation(self):
        """Eigenvalue interpretation mentions phi."""
        a1 = a1_double_cover(2)
        assert 'eigenvalue' in a1.eigenvalue_interpretation.lower()

    def test_genus_error(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            a1_double_cover(1)


# ======================================================================
# 7. FULL IDENTIFICATION CHAIN
# ======================================================================

class TestFullChain:
    """Complete chain: spectral curve -> z=lambda -> R(z) -> Bethe."""

    def test_sl2_genus2_all_checks_pass(self):
        """SL_2 genus 2: all chain checks pass."""
        chain = full_identification_chain(2, 'A', 1)
        failed = {k: v for k, v in chain.checks.items() if not v}
        assert len(failed) == 0, f"Failed: {list(failed.keys())}"

    def test_sl2_genus3_all_checks_pass(self):
        """SL_2 genus 3: all chain checks pass."""
        chain = full_identification_chain(3, 'A', 1)
        failed = {k: v for k, v in chain.checks.items() if not v}
        assert len(failed) == 0, f"Failed: {list(failed.keys())}"

    def test_sl3_genus2_all_checks_pass(self):
        """SL_3 genus 2: all chain checks pass."""
        chain = full_identification_chain(2, 'A', 2)
        failed = {k: v for k, v in chain.checks.items() if not v}
        assert len(failed) == 0, f"Failed: {list(failed.keys())}"

    def test_d4_genus2_all_checks_pass(self):
        """D_4 genus 2: all chain checks pass."""
        chain = full_identification_chain(2, 'D', 4)
        failed = {k: v for k, v in chain.checks.items() if not v}
        assert len(failed) == 0, f"Failed: {list(failed.keys())}"

    def test_summary_status_conjectural(self):
        """Summary status is CONJECTURAL."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.summary['status'] == 'CONJECTURAL'

    def test_summary_all_checks(self):
        """Summary reports all checks pass."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.summary['all_checks_pass'] is True

    def test_a1_data_present_for_sl2(self):
        """A_1 double cover data present for SL_2."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.a1_data is not None

    def test_a1_data_absent_for_sl3(self):
        """A_1 data absent for SL_3."""
        chain = full_identification_chain(2, 'A', 2)
        assert chain.a1_data is None

    def test_chain_spectral_genus_sl2_g2(self):
        """Chain spectral genus = 5 for SL_2 g=2."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.spectral_curve.genus_spectral == 5

    def test_chain_spectral_genus_sl2_g3(self):
        """Chain spectral genus = 9 for SL_2 g=3."""
        chain = full_identification_chain(3, 'A', 1)
        assert chain.spectral_curve.genus_spectral == 9

    def test_chain_rmatrix_unitarity(self):
        """R-matrix unitarity in chain."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.rmatrix.unitarity is True

    def test_chain_identification_conjectured(self):
        """Identification status in chain."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.identification.status == 'Conjectured'

    def test_chain_hitchin_base_dim(self):
        """Hitchin base dim in chain."""
        chain = full_identification_chain(2, 'A', 1)
        assert chain.spectral_curve.dim_hitchin_base == 3

    def test_genus_error(self):
        with pytest.raises(ValueError, match="genus >= 2"):
            full_identification_chain(1, 'A', 1)


# ======================================================================
# 8. CROSS-ENGINE BRIDGE
# ======================================================================

class TestCrossEngineBridge:
    """Consistency with existing compute engines."""

    def test_all_bridge_checks_pass(self):
        """All cross-engine checks pass."""
        bridge = cross_engine_bridge()
        for key, val in bridge.items():
            assert val['match'], f"Bridge check failed: {key}"

    def test_sl2_g2_spectral_genus(self):
        """SL_2 g=2 spectral genus = 5 matches chiral_hitchin_k3."""
        bridge = cross_engine_bridge()
        assert bridge['sl2_g2_spectral_genus']['match']

    def test_sl2_g2_branch_points(self):
        """SL_2 g=2 branch points = 4 matches."""
        bridge = cross_engine_bridge()
        assert bridge['sl2_g2_branch_points']['match']

    def test_sl2_g2_hitchin_base(self):
        """SL_2 g=2 Hitchin base = 3 matches."""
        bridge = cross_engine_bridge()
        assert bridge['sl2_g2_hitchin_base']['match']

    def test_unitarity(self):
        """Structure function unitarity matches k3_yangian."""
        bridge = cross_engine_bridge()
        assert bridge['unitarity_g_g_neg']['match']

    def test_cy2_constraint(self):
        """CY_2 sum=0 matches."""
        bridge = cross_engine_bridge()
        assert bridge['cy2_sum_zero']['match']

    def test_a1_prym(self):
        """A_1 g=2 Prym=3 matches hitchin_sl2_genus2."""
        bridge = cross_engine_bridge()
        assert bridge['a1_g2_prym_eq_fibre']['match']

    def test_e8_hitchin_base(self):
        """E_8 g=2 Hitchin base = 248 matches."""
        bridge = cross_engine_bridge()
        assert bridge['e8_g2_hitchin_base']['match']


# ======================================================================
# 9. MULTI-PATH CROSS-CHECKS [CF]
# ======================================================================

class TestMultiPathCrossChecks:
    """Cross-engine verification against chiral_hitchin_k3, spectral_curve_chiral,
    and geometric_langlands_shadow.  Every hardcoded value in this engine is
    verified against at least one independent computation path."""

    # --- Spectral genus: our formula vs spectral_curve_chiral ---

    @pytest.mark.parametrize("n,g", [
        (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2),
    ])
    def test_spectral_genus_vs_scc(self, n, g):
        """g(Sigma) matches spectral_curve_chiral.spectral_curve_genus_gln.

        Two independent implementations of Riemann-Hurwitz.
        """
        # [CF] spectral_curve_chiral uses the same formula independently
        ours = spectral_curve_genus(n, g)
        theirs = scc_genus_gln(n, g)
        assert ours == theirs, (
            f"Genus mismatch for n={n}, g={g}: ours={ours}, scc={theirs}"
        )

    # --- Hitchin base dim: our formula vs chiral_hitchin_k3 ---

    @pytest.mark.parametrize("gt,gr,g", [
        ('A', 1, 2), ('A', 1, 3), ('A', 2, 2), ('D', 4, 2), ('E', 8, 2),
    ])
    def test_hitchin_base_vs_chk3(self, gt, gr, g):
        """Hitchin base dim matches chiral_hitchin_k3.hitchin_on_k3.

        Our spectral_curve_k3 computes dim B independently from
        chiral_hitchin_k3.hitchin_on_k3.  Both use Casimir degrees
        but through different code paths.
        """
        # [CF] two independent implementations
        ours = spectral_curve_k3(g, gt, gr).dim_hitchin_base
        theirs = chk3_hitchin_on_k3(g, gt, gr).dim_hitchin_base
        assert ours == theirs, (
            f"Base dim mismatch for {gt}{gr} g={g}: ours={ours}, chk3={theirs}"
        )

    # --- Spectral genus: our formula vs chiral_hitchin_k3 ---

    @pytest.mark.parametrize("gt,gr,g", [
        ('A', 1, 2), ('A', 1, 3), ('A', 2, 2), ('A', 3, 2),
    ])
    def test_spectral_genus_vs_chk3(self, gt, gr, g):
        """Spectral genus matches chiral_hitchin_k3.hitchin_on_k3."""
        # [CF] two independent implementations
        ours = spectral_curve_k3(g, gt, gr).genus_spectral
        theirs = chk3_hitchin_on_k3(g, gt, gr).spectral_genus
        assert ours == theirs, (
            f"Spectral genus mismatch for {gt}{gr} g={g}: ours={ours}, chk3={theirs}"
        )

    # --- Branch points: our formula vs chiral_hitchin_k3 ---

    @pytest.mark.parametrize("gt,gr,g", [
        ('A', 1, 2), ('A', 1, 3), ('A', 2, 2), ('D', 4, 2),
    ])
    def test_branch_points_vs_chk3(self, gt, gr, g):
        """Branch points match chiral_hitchin_k3."""
        # [CF] independent Riemann-Hurwitz implementations
        ours = spectral_curve_k3(g, gt, gr).n_branch_points
        theirs = chk3_hitchin_on_k3(g, gt, gr).spectral_n_branch
        assert ours == theirs, (
            f"Branch mismatch for {gt}{gr} g={g}: ours={ours}, chk3={theirs}"
        )

    # --- Hitchin base: our formula vs geometric_langlands_shadow Lie data ---

    @pytest.mark.parametrize("gt,gr,g", [
        ('A', 1, 2), ('A', 2, 2), ('D', 4, 2), ('E', 6, 2), ('E', 8, 2),
    ])
    def test_hitchin_base_vs_lie_data(self, gt, gr, g):
        """dim B = dim(g)*(g-1) verified via geometric_langlands_shadow.lie_data.

        Third independent path: Lie algebra dimension times (g-1).
        """
        # [CF] geometric_langlands_shadow provides dim(g) independently
        d = gls_lie_data(gt, gr)
        expected = d.dim * (g - 1)
        ours = spectral_curve_k3(g, gt, gr).dim_hitchin_base
        assert ours == expected, (
            f"Base dim vs lie_data for {gt}{gr} g={g}: ours={ours}, expected={expected}"
        )

    # --- SL_n Hitchin base: vs spectral_curve_chiral ---

    @pytest.mark.parametrize("n,g", [
        (2, 2), (2, 3), (3, 2), (3, 3),
    ])
    def test_sln_base_vs_scc(self, n, g):
        """SL_n Hitchin base dim matches spectral_curve_chiral.hitchin_base_dim_sln."""
        # [CF] spectral_curve_chiral has independent formula (n^2-1)*(g-1)
        ours = spectral_curve_k3(g, 'A', n - 1).dim_hitchin_base
        theirs = scc_base_sln(n, g)
        assert ours == theirs, (
            f"SL_{n} base dim mismatch at g={g}: ours={ours}, scc={theirs}"
        )

    # --- A_1 Prym: vs Riemann-Hurwitz cross-check ---

    @pytest.mark.parametrize("g", [2, 3, 4, 5])
    def test_a1_prym_vs_riemann_hurwitz(self, g):
        """Prym(Sigma/C) = g(Sigma) - g(C) via two independent formulas.

        Path 1: a1_double_cover.prym_dim (computed as g_spec - g).
        Path 2: 3*(g-1) (from dim(SL_2)*(g-1) = Lagrangian fibre).
        Path 3: spectral_curve_genus(2, g) - g.
        """
        a1 = a1_double_cover(g)
        # Path 2: Lagrangian fibre dimension
        lagrangian = 3 * (g - 1)
        # Path 3: explicit genus subtraction
        genus_sub = spectral_curve_genus(2, g) - g
        assert a1.prym_dim == lagrangian == genus_sub, (
            f"Prym mismatch at g={g}: a1={a1.prym_dim}, "
            f"lagrangian={lagrangian}, genus_sub={genus_sub}"
        )

    # --- Normal bundle degree: vs chiral_hitchin_k3 spectral parameter ---

    @pytest.mark.parametrize("g", [2, 3, 4])
    def test_L_square_vs_chk3(self, g):
        """L^2 = 2g-2 matches chiral_hitchin_k3.spectral_parameter_k3."""
        # [CF] chiral_hitchin_k3 computes normal_bundle_degree independently
        ours = spectral_curve_k3(g, 'A', 1).L_square
        theirs = chk3_spectral_parameter(g, 'A', 1).normal_bundle_degree
        assert ours == theirs, (
            f"L^2 mismatch at g={g}: ours={ours}, chk3={theirs}"
        )

    # --- Structure function unitarity: algebraic identity ---

    @pytest.mark.parametrize("z", [
        2.5 + 0.3j, 5.0 - 1.0j, 0.7 + 3.0j, 10.0 + 0.1j, 50.0 + 7.0j,
    ])
    def test_unitarity_algebraic_identity(self, z):
        """g(z)*g(-z) = 1 is an algebraic identity (factorwise cancellation).

        Independent verification: for each i, (z-h_i)/(z+h_i) * (-z-h_i)/(-z+h_i)
        = (z-h_i)(z+h_i) / ((z+h_i)(z-h_i)) = 1.  So the product is 1.
        """
        h = _kummer_h_params(1.0)
        g_z = _structure_function(z, h)
        g_neg_z = _structure_function(-z, h)
        # Path 1: direct product
        product = g_z * g_neg_z
        # Path 2: factorwise cancellation (each factor gives 1)
        factorwise = 1.0
        for hi in h:
            fwd = (z - hi) / (z + hi)
            bwd = (-z - hi) / (-z + hi)
            factorwise *= fwd * bwd
        assert abs(product - 1.0) < 1e-10
        assert abs(factorwise - 1.0) < 1e-10

    # --- Spectral curve genus: Riemann-Hurwitz direct computation ---

    @pytest.mark.parametrize("n,g", [(2, 2), (2, 3), (3, 2)])
    def test_genus_via_riemann_hurwitz_direct(self, n, g):
        """Verify g(Sigma) by direct Riemann-Hurwitz computation.

        Path 1: spectral_curve_genus(n, g) = n^2*(g-1)+1.
        Path 2: 2g(S)-2 = n*(2g-2) + B, B = n*(n-1)*(2g-2).
                 2g(S)-2 = n^2*(2g-2), g(S) = n^2*(g-1)+1.
        """
        # Path 1
        formula = spectral_curve_genus(n, g)
        # Path 2: Riemann-Hurwitz explicit
        B = branch_points_generic(n, g)
        two_gS_minus_2 = n * (2 * g - 2) + B
        gS_rh = two_gS_minus_2 // 2 + 1
        assert formula == gS_rh, (
            f"RH mismatch for n={n}, g={g}: formula={formula}, RH={gS_rh}"
        )


# ======================================================================
# 10. MASTER VERIFICATION
# ======================================================================

class TestMasterVerification:
    """Run all internal checks via verify_all()."""

    def test_all_checks_pass(self):
        """All 100+ internal checks pass."""
        results = verify_all()
        failed = {k: v for k, v in results.items() if not v}
        assert len(failed) == 0, f"Failed: {list(failed.keys())}"

    def test_sufficient_checks(self):
        """At least 100 checks are run."""
        results = verify_all()
        assert len(results) >= 100, f"Only {len(results)} checks (need >= 100)"


# ======================================================================
# 10. PARAMETRIC LANDSCAPE
# ======================================================================

class TestParametricLandscape:
    """Landscape tests across types and genera."""

    @pytest.mark.parametrize("gt,gr,g,expected_base", [
        ('A', 1, 2, 3), ('A', 1, 3, 6), ('A', 1, 4, 9),
        ('A', 2, 2, 8), ('A', 2, 3, 16),
        ('A', 3, 2, 15),
        ('D', 4, 2, 28), ('D', 4, 3, 56),
        ('E', 6, 2, 78),
        ('E', 8, 2, 248),
    ])
    def test_hitchin_base_dims(self, gt, gr, g, expected_base):
        """Hitchin base dim = dim(g)*(g-1) for all types."""
        # VERIFIED [DC] direct computation [CF] chiral_hitchin_k3
        sc = spectral_curve_k3(g, gt, gr)
        assert sc.dim_hitchin_base == expected_base

    @pytest.mark.parametrize("g", [2, 3, 4, 5, 6])
    def test_a1_spectral_genus_landscape(self, g):
        """A_1 spectral genus across genera."""
        a1 = a1_double_cover(g)
        assert a1.genus_spectral == 4 * g - 3

    @pytest.mark.parametrize("g", [2, 3, 4, 5])
    def test_full_chain_landscape(self, g):
        """Full chain passes for all genera."""
        chain = full_identification_chain(g, 'A', 1)
        assert chain.summary['all_checks_pass'] is True
