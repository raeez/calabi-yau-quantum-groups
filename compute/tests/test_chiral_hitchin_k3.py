r"""Tests for compute.lib.chiral_hitchin_k3.

Comprehensive verification of the chiral quantization of the Hitchin
system on curves C inside K3 surfaces.

Verifies:
  1. K3 linear system data: h^0(L), dim|L|, L^2 = 2g-2
  2. Hitchin system on K3 curves: dimensions, spectral curve, fibration
  3. Chiral differential operators on Bun_G(C): CDO data at critical level
  4. Spectral parameter identification: Hitchin lambda = K3 Yangian z
  5. Hitchin-to-Yangian module conjecture: three-step functor data
  6. Feigin-Frenkel center for K3 curves: oper = Hitchin base dimension
  7. Kappa analysis: genus-independence, Koszul conductor, critical vanishing
  8. Family over |L|: universal Hitchin data
  9. Explicit examples: SL_2 genus 2/3, E_8 genus 2
  10. ADE landscape: all standard types at genus 2
  11. Cross-volume bridge: consistency with existing engines
  12. Master verification

Ground truth (multi-path verified):
  - Hitchin (1987): dim M_H = 2*dim(G)*(g-1) for semisimple G [LT]
  - Riemann-Roch on K3: chi(L) = L^2/2 + 2, so h^0(L) = g+1 [DC][LT]
  - Spectral genus: g(Sigma) = n^2*(g-1) + 1 (Riemann-Hurwitz) [DC][LT]
  - Feigin-Frenkel (1992): Z(hat{g}_{-h^v}) = Fun(Op_{G^L}(C)) [LT]
  - Hitchin-BD: dim Op = dim Hitchin base [LT]
  - KM kappa: kappa_ch(hat{g}_k) = dim(g)*(k+h^v)/(2*h^v) [DC][LT]
  - Simply-laced c at k=1: c(hat{g}_1) = rank(g) [DC][LT]
  - Koszul conductor: kappa(k) + kappa(-k-2*h^v) = 0 [DC]
  - SL_2 casimirs: (2,). SL_3: (2,3). D_4: (2,4,4,6). E_8: (2,8,12,14,18,20,24,30) [LT]
  - Vol I: kappa(hat{g}_k) formula. Vol III: k3_geometric_langlands.py

85+ tests organized by mathematical structure.
"""

from fractions import Fraction as F

import pytest

from compute.lib.chiral_hitchin_k3 import (
    CDOData,
    FFCenterK3CurveData,
    HitchinK3FamilyData,
    HitchinOnK3Data,
    HitchinYangianModuleData,
    K3LinearSystemData,
    KappaAnalysisData,
    SpectralParameterData,
    cdo_on_k3,
    cross_volume_hitchin_bridge,
    dim_bun_g,
    e8_genus2_on_k3,
    ff_center_k3_curve,
    hitchin_k3_family,
    hitchin_k3_landscape,
    hitchin_on_k3,
    hitchin_to_yangian_module,
    k3_linear_system,
    kappa_analysis_hitchin_k3,
    sl2_genus2_on_k3,
    sl2_genus3_on_k3,
    spectral_parameter_k3,
    verify_all,
)


# ======================================================================
# 1. K3 LINEAR SYSTEM DATA
# ======================================================================

class TestK3LinearSystem:
    """K3 linear system |L| for curves of genus g."""

    def test_genus2_L_square(self):
        """L^2 = 2g-2 = 2 for g=2."""
        # VERIFIED [DC] 2*2-2=2 [LT] Riemann-Roch on K3
        ls = k3_linear_system(2)
        assert ls.L_square == 2

    def test_genus2_h0(self):
        """h^0(S, L) = g+1 = 3 for g=2."""
        # VERIFIED [DC] chi(L)=L^2/2+2=3 [LT] Riemann-Roch on K3
        ls = k3_linear_system(2)
        assert ls.h0_L == 3

    def test_genus2_dim_linear_system(self):
        """dim |L| = g = 2 for g=2."""
        # VERIFIED [DC] h^0-1=2 [DA] P^g
        ls = k3_linear_system(2)
        assert ls.dim_linear_system == 2

    def test_genus3_L_square(self):
        """L^2 = 4 for g=3."""
        # VERIFIED [DC] 2*3-2=4 [LT] Riemann-Roch on K3
        ls = k3_linear_system(3)
        assert ls.L_square == 4

    def test_genus3_h0(self):
        """h^0(S, L) = 4 for g=3."""
        # VERIFIED [DC] chi(L)=4/2+2=4 [LT] Riemann-Roch on K3
        ls = k3_linear_system(3)
        assert ls.h0_L == 4

    @pytest.mark.parametrize("g,expected_L2,expected_h0,expected_dim", [
        (2, 2, 3, 2),
        (3, 4, 4, 3),
        (4, 6, 5, 4),
        (5, 8, 6, 5),
        (10, 18, 11, 10),
    ])
    def test_linear_system_parametric(self, g, expected_L2, expected_h0,
                                      expected_dim):
        """Parametric test of K3 linear system data."""
        # VERIFIED [DC] direct computation [DA] dimensional analysis
        ls = k3_linear_system(g)
        assert ls.L_square == expected_L2
        assert ls.h0_L == expected_h0
        assert ls.dim_linear_system == expected_dim

    def test_genus2_is_ample(self):
        """L is ample for g >= 2."""
        # VERIFIED [LT] L^2 > 0 and nef implies ample on K3
        ls = k3_linear_system(2)
        assert ls.is_ample is True

    def test_genus0_not_ample(self):
        """L^2 = -2 for g=0: not ample."""
        # VERIFIED [DC] 2*0-2=-2 [LT] (-2)-curves on K3
        ls = k3_linear_system(0)
        assert ls.is_ample is False


# ======================================================================
# 2. HITCHIN SYSTEM ON K3 CURVES
# ======================================================================

class TestHitchinOnK3:
    """Hitchin system M_H(C, G) for C subset K3."""

    def test_sl2_genus2_hitchin_base(self):
        """SL_2, g=2: dim B = 3.

        Casimirs of A_1: (2,). H^0(K^2) = 3(g-1) = 3.
        """
        # VERIFIED [DC] 3*(2-1)=3 [LT] Hitchin 1987
        h = hitchin_on_k3(2, 'A', 1)
        assert h.dim_hitchin_base == 3

    def test_sl2_genus2_hitchin_moduli(self):
        """SL_2, g=2: dim M_H = 6 (Lagrangian, so 2*3)."""
        # VERIFIED [DC] 2*3=6 [LT] Lagrangian fibration
        h = hitchin_on_k3(2, 'A', 1)
        assert h.dim_hitchin_moduli == 6

    def test_sl2_genus2_spectral_genus(self):
        """SL_2, g=2: spectral genus = n^2(g-1)+1 = 4+1 = 5.

        The spectral curve for SL_2 is a degree-2 cover of C.
        Riemann-Hurwitz with 4 branch points: 2g(S)-2 = 2*(2)-2 + 4 = 6, g(S)=4.
        WAIT: n=2, g=2: 2g(S)-2 = n^2*(2g-2) = 4*2 = 8, so g(S)=5.

        Independent check: n*(n-1)*(2g-2) = 2*1*2 = 4 branch points.
        2g(S)-2 = 2*(2*2-2) + 4 = 2*2 + 4 = 8, g(S) = 5. Consistent.
        """
        # VERIFIED [DC] n^2(g-1)+1=5 [DC] Riemann-Hurwitz 2*4+4=8 -> g=5
        h = hitchin_on_k3(2, 'A', 1)
        assert h.spectral_genus == 5

    def test_sl2_genus2_n_branch(self):
        """SL_2, g=2: 4 branch points."""
        # VERIFIED [DC] n*(n-1)*(2g-2) = 2*1*2 = 4
        h = hitchin_on_k3(2, 'A', 1)
        assert h.spectral_n_branch == 4

    def test_sl3_genus2_hitchin_base(self):
        """SL_3, g=2: casimirs (2,3), dim B = H^0(K^2)+H^0(K^3) = 3+5 = 8.

        (n^2-1)(g-1) = 8*1 = 8.  Check: casimir sum gives same.
        """
        # VERIFIED [DC] 3+5=8 [DC] (9-1)*1=8 [LT] Hitchin base formula
        h = hitchin_on_k3(2, 'A', 2)
        assert h.dim_hitchin_base == 8

    def test_sl3_genus2_spectral_genus(self):
        """SL_3, g=2: spectral genus = 3^2*1+1 = 10."""
        # VERIFIED [DC] 9*1+1=10 [LT] standard formula
        h = hitchin_on_k3(2, 'A', 2)
        assert h.spectral_genus == 10

    def test_d4_genus2_hitchin_base(self):
        """D_4 = so_8, g=2: dim(D_4) = 28, dim B = 28.

        Casimirs of D_4: (2, 4, 4, 6).
        H^0(K^2) = 3, H^0(K^4) = 7, H^0(K^4) = 7, H^0(K^6) = 11.
        Sum = 3+7+7+11 = 28 = dim(D_4)*(g-1) = 28*1.
        """
        # VERIFIED [DC] 3+7+7+11=28 [DC] dim(D4)*(g-1)=28 [LT] Casimir sum rule
        h = hitchin_on_k3(2, 'D', 4)
        assert h.dim_hitchin_base == 28

    def test_e8_genus2_hitchin_base(self):
        """E_8, g=2: dim B = dim(E_8) = 248."""
        # VERIFIED [DC] sum of H^0(K^{d_i}) = 248 [LT] dim(E8)*(g-1) = 248
        h = hitchin_on_k3(2, 'E', 8)
        assert h.dim_hitchin_base == 248

    def test_lagrangian_property(self):
        """M_H is Lagrangian: dim M_H = 2 * dim B for all (G, g)."""
        # VERIFIED [DC] direct check [LT] Hitchin fibration is Lagrangian
        for gt, gr in [('A', 1), ('A', 2), ('D', 4), ('E', 6), ('E', 8)]:
            for g in [2, 3, 4]:
                h = hitchin_on_k3(g, gt, gr)
                assert h.dim_hitchin_moduli == 2 * h.dim_hitchin_base, \
                    f"Lagrangian failed for {gt}{gr}, g={g}"

    def test_adjunction_identification(self):
        """K3 adjunction: K_C = L|_C since K_S = O_S."""
        # VERIFIED [LT] adjunction formula K_C = (K_S tensor L)|_C = L|_C
        h = hitchin_on_k3(2, 'A', 1)
        assert 'K_C = L|_C' in h.adjunction_identification

    def test_genus_must_be_at_least_2(self):
        """Hitchin system requires genus >= 2."""
        with pytest.raises(ValueError, match="genus >= 2"):
            hitchin_on_k3(1, 'A', 1)

    @pytest.mark.parametrize("g,gt,gr,expected_base", [
        (2, 'A', 1, 3),
        (3, 'A', 1, 6),
        (4, 'A', 1, 9),
        (2, 'A', 2, 8),
        (3, 'A', 2, 16),
        (2, 'A', 3, 15),
        (2, 'D', 4, 28),
        (2, 'E', 6, 78),
        (2, 'E', 7, 133),
        (2, 'E', 8, 248),
    ])
    def test_hitchin_base_parametric(self, g, gt, gr, expected_base):
        """Parametric Hitchin base dimension check."""
        # VERIFIED [DC] direct computation [LT] dim(g)*(g-1) for semisimple G
        h = hitchin_on_k3(g, gt, gr)
        assert h.dim_hitchin_base == expected_base


# ======================================================================
# 3. CHIRAL DIFFERENTIAL OPERATORS ON Bun_G(C)
# ======================================================================

class TestCDO:
    """Chiral differential operators at the critical level."""

    def test_sl2_genus2_bun_dim(self):
        """dim Bun_{SL_2}(C) = dim(SL_2)*(g-1) = 3*1 = 3 for g=2."""
        # VERIFIED [DC] 3*(2-1)=3 [LT] standard formula
        cdo = cdo_on_k3(2, 'A', 1)
        assert cdo.dim_bun_g == 3

    def test_sl2_genus2_cdo_kappa(self):
        """kappa_ch = 0 at critical level."""
        # VERIFIED [DC] dim(g)*0/(2*h^v)=0 [LT] Feigin-Frenkel
        cdo = cdo_on_k3(2, 'A', 1)
        assert cdo.cdo_kappa == 0

    def test_sl2_genus2_center_dim(self):
        """dim Op_{PGL_2}(C) = 3 for g=2.

        The center Z(hat{sl}_2_{-2}) = Fun(Op_{PGL_2}(C)).
        dim Op = dim Hitchin base = 3.
        """
        # VERIFIED [DC] dim H^0(K^2)=3 [LT] Feigin-Frenkel + Hitchin-BD
        cdo = cdo_on_k3(2, 'A', 1)
        assert cdo.center_dim == 3

    def test_sl2_genus2_n_hamiltonians(self):
        """SL_2 has rank 1, so 1 independent Hitchin Hamiltonian."""
        # VERIFIED [LT] rank(SL_2)=1 [DC] rank(A_1)=1
        cdo = cdo_on_k3(2, 'A', 1)
        assert cdo.n_hitchin_hamiltonians == 1

    def test_sl2_genus2_family_base_dim(self):
        """Family base = dim |L| = g = 2 for genus 2."""
        # VERIFIED [DC] dim |L| = g [DA] dimensional consistency
        cdo = cdo_on_k3(2, 'A', 1)
        assert cdo.family_base_dim == 2

    def test_e8_genus2_bun_dim(self):
        """dim Bun_{E_8}(C) = 248*1 = 248 for g=2."""
        # VERIFIED [DC] dim(E8)*(2-1)=248 [LT] standard formula
        cdo = cdo_on_k3(2, 'E', 8)
        assert cdo.dim_bun_g == 248

    def test_e8_genus2_n_hamiltonians(self):
        """E_8 has rank 8, so 8 independent Hitchin Hamiltonians."""
        # VERIFIED [LT] rank(E_8)=8 [DC] direct
        cdo = cdo_on_k3(2, 'E', 8)
        assert cdo.n_hitchin_hamiltonians == 8


# ======================================================================
# 4. SPECTRAL PARAMETER IDENTIFICATION
# ======================================================================

class TestSpectralParameter:
    """Hitchin spectral parameter = K3 Yangian z (conjectural)."""

    def test_sl2_genus2_spectral_degree(self):
        """SL_2: spectral curve is a degree-2 cover."""
        # VERIFIED [DC] SL_2 = A_1 has n=rank+1=2 [LT] Hitchin spectral curve
        sp = spectral_parameter_k3(2, 'A', 1)
        assert sp.spectral_degree == 2

    def test_sl2_genus2_tautological_degree(self):
        """Tautological section degree = n*deg(K_C) = 2*2 = 4."""
        # VERIFIED [DC] 2*(2*2-2)=4 [DA] degree = n*deg(K)
        sp = spectral_parameter_k3(2, 'A', 1)
        assert sp.tautological_degree == 4

    def test_sl2_genus2_normal_bundle_degree(self):
        """deg(N_{C/K3}) = deg(L|_C) = L^2 = 2 for g=2."""
        # VERIFIED [DC] L^2=2g-2=2 [LT] adjunction formula
        sp = spectral_parameter_k3(2, 'A', 1)
        assert sp.normal_bundle_degree == 2

    def test_sl3_genus3_spectral_degree(self):
        """SL_3: spectral curve is a degree-3 cover."""
        # VERIFIED [DC] SL_3 = A_2 has n=3 [LT] standard
        sp = spectral_parameter_k3(3, 'A', 2)
        assert sp.spectral_degree == 3

    def test_contains_ap_cy31_warning(self):
        """AP-CY31 compliance: distinguish spectral from worldsheet z."""
        # VERIFIED [DC] string contains AP-CY31 warning
        sp = spectral_parameter_k3(2, 'A', 1)
        assert 'AP-CY31' in sp.yangian_spectral_parameter

    def test_genus_error(self):
        """Genus < 2 raises ValueError."""
        with pytest.raises(ValueError, match="genus >= 2"):
            spectral_parameter_k3(1, 'A', 1)


# ======================================================================
# 5. HITCHIN-TO-YANGIAN MODULE CONJECTURE
# ======================================================================

class TestHitchinToYangianModule:
    """Three-step functor: CDO -> hat{g}-mod -> D-mod -> Y(g_{K3})-mod."""

    def test_sl2_genus2_steps_status(self):
        """Steps 1,2 ProvedElsewhere; Step 3 Conjectured."""
        # VERIFIED [LT] BD=proved, FG=proved, K3 promotion=conjecture
        hym = hitchin_to_yangian_module(2, 'A', 1)
        assert hym.step1_status == 'ProvedElsewhere'
        assert hym.step2_status == 'ProvedElsewhere'
        assert hym.step3_status == 'Conjectured'

    def test_sl2_genus2_dim_checks(self):
        """Dimensional data for SL_2 genus 2."""
        # VERIFIED [DC] all dimensions from independent computation
        hym = hitchin_to_yangian_module(2, 'A', 1)
        assert hym.dim_oper_moduli == 3
        assert hym.dim_bun_g == 3
        assert hym.dim_linear_system == 2

    def test_sl2_genus2_langlands_dual(self):
        """SL_2 is self-dual: G^L = A1."""
        # VERIFIED [LT] A_1 is self-dual (simply-laced)
        hym = hitchin_to_yangian_module(2, 'A', 1)
        assert hym.langlands_dual_label == 'A1'

    def test_e6_genus2_langlands_dual(self):
        """E_6 is self-dual."""
        # VERIFIED [LT] E_6 is simply-laced, self-dual
        hym = hitchin_to_yangian_module(2, 'E', 6)
        assert hym.langlands_dual_label == 'E6'

    def test_non_ade_raises(self):
        """K3 enhancement requires ADE type."""
        with pytest.raises(ValueError, match="A, D, or E"):
            hitchin_to_yangian_module(2, 'B', 2)

    def test_genus1_raises(self):
        """Genus < 2 raises ValueError."""
        with pytest.raises(ValueError, match="genus >= 2"):
            hitchin_to_yangian_module(1, 'A', 1)


# ======================================================================
# 6. FEIGIN-FRENKEL CENTER FOR K3 CURVES
# ======================================================================

class TestFFCenterK3:
    """Feigin-Frenkel center: Z(hat{g}_{-h^v}) = Fun(Op_{G^L}(C))."""

    def test_sl2_genus2_oper_dim(self):
        """dim Op_{PGL_2}(C) = 3 for g=2.

        Independent: dim H^0(K^2) = 3(g-1) = 3.
        """
        # VERIFIED [DC] 3*(2-1)=3 [LT] Feigin-Frenkel + Hitchin-BD
        ff = ff_center_k3_curve(2, 'A', 1)
        assert ff.oper_dim == 3

    def test_sl2_genus3_oper_dim(self):
        """dim Op_{PGL_2}(C) = 6 for g=3.

        H^0(K^2) = 3*(3-1) = 6.
        """
        # VERIFIED [DC] 3*2=6 [LT] standard formula
        ff = ff_center_k3_curve(3, 'A', 1)
        assert ff.oper_dim == 6

    def test_oper_equals_hitchin_base(self):
        """dim Op = dim Hitchin base (Hitchin-BD correspondence)."""
        # VERIFIED [LT] Hitchin-BD theorem [DC] equality check
        for g in [2, 3, 4]:
            for gt, gr in [('A', 1), ('A', 2), ('D', 4), ('E', 8)]:
                ff = ff_center_k3_curve(g, gt, gr)
                assert ff.oper_equals_hitchin, \
                    f"Op != Hitchin base for {gt}{gr}, g={g}"

    def test_sl2_center_generators(self):
        """SL_2: rank(G^L) = rank(PGL_2) = 1 generator."""
        # VERIFIED [DC] rank(A_1)=1 [LT] Casimir parametrisation
        ff = ff_center_k3_curve(2, 'A', 1)
        assert ff.center_generators == 1

    def test_e8_center_generators(self):
        """E_8: rank(G^L) = 8 generators."""
        # VERIFIED [DC] rank(E_8)=8 [LT] self-dual
        ff = ff_center_k3_curve(2, 'E', 8)
        assert ff.center_generators == 8

    def test_family_dim(self):
        """Family dim = dim |L| + dim Op."""
        # VERIFIED [DC] g + dim_B [DA] dimensional count
        ff = ff_center_k3_curve(2, 'A', 1)
        assert ff.family_dim == 2 + 3  # g=2, dim B=3


# ======================================================================
# 7. KAPPA ANALYSIS
# ======================================================================

class TestKappaAnalysis:
    """kappa_ch analysis for the Hitchin-K3 family."""

    def test_sl2_kappa_critical(self):
        """kappa_ch(sl_2, k=-2) = 0."""
        # VERIFIED [DC] 3*0/(2*2)=0 [LT] Feigin-Frenkel
        ka = kappa_analysis_hitchin_k3('A', 1)
        assert ka.kappa_at_critical == 0

    def test_sl2_kappa_k1(self):
        """kappa_ch(sl_2, k=1) = 9/4.

        dim(sl_2)*(1+h^v)/(2*h^v) = 3*3/(2*2) = 9/4.
        """
        # VERIFIED [DC] 3*3/4=9/4 [LT] Vol I kappa formula
        ka = kappa_analysis_hitchin_k3('A', 1)
        assert ka.kappa_at_k1 == F(9, 4)

    def test_sl2_koszul_conductor(self):
        """kappa(k=1) + kappa(k'=-5) = 0 (Koszul conductor)."""
        # VERIFIED [DC] 9/4 + (-9/4) = 0 [LT] Vol I FF reflection
        ka = kappa_analysis_hitchin_k3('A', 1)
        assert ka.kappa_at_k1 + ka.kappa_at_ff_dual == 0

    def test_sl2_ff_dual_level(self):
        """FF dual of k=1 for sl_2: k' = -1-2*2 = -5."""
        # VERIFIED [DC] -1-4=-5 [LT] k'=-k-2*h^v
        ka = kappa_analysis_hitchin_k3('A', 1)
        assert ka.k_ff_dual_of_1 == F(-5)

    def test_sl2_kappa_slope(self):
        """d(kappa)/dk = dim(g)/(2*h^v) = 3/4 for sl_2."""
        # VERIFIED [DC] 3/(2*2)=3/4 [DA] dimensional
        ka = kappa_analysis_hitchin_k3('A', 1)
        assert ka.kappa_slope == F(3, 4)

    def test_kappa_genus_independent(self):
        """kappa_ch depends on (g, k) not on genus of C."""
        # VERIFIED [DC] formula has no genus dependence [LT] kappa is local
        ka = kappa_analysis_hitchin_k3('A', 1)
        assert ka.is_genus_independent is True

    def test_e8_kappa_k1(self):
        """kappa_ch(E_8, k=1) = 248*31/(2*30) = 1922/15."""
        # VERIFIED [DC] 248*31/60=7688/60=1922/15 [CF] matches k3_geometric_langlands
        ka = kappa_analysis_hitchin_k3('E', 8)
        assert ka.kappa_at_k1 == F(1922, 15)

    def test_e8_koszul_conductor(self):
        """E_8 Koszul conductor: kappa(1) + kappa(-61) = 0."""
        # VERIFIED [DC] k'=-1-60=-61, kappa(-61)=-1922/15 [LT] conductor
        ka = kappa_analysis_hitchin_k3('E', 8)
        assert ka.kappa_at_k1 + ka.kappa_at_ff_dual == 0

    def test_d4_kappa_k1(self):
        """kappa_ch(D_4, k=1) = 28*7/(2*6) = 49/3."""
        # VERIFIED [DC] 28*7/12=196/12=49/3 [CF] matches k3_geometric_langlands
        ka = kappa_analysis_hitchin_k3('D', 4)
        assert ka.kappa_at_k1 == F(49, 3)

    @pytest.mark.parametrize("gt,gr", [
        ('A', 1), ('A', 2), ('A', 3),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ])
    def test_koszul_conductor_all_ade(self, gt, gr):
        """Koszul conductor holds for all ADE types."""
        # VERIFIED [DC] algebraic identity [LT] Vol I FF reflection
        ka = kappa_analysis_hitchin_k3(gt, gr)
        assert ka.kappa_at_k1 + ka.kappa_at_ff_dual == 0

    @pytest.mark.parametrize("gt,gr", [
        ('A', 1), ('A', 2), ('A', 3),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ])
    def test_kappa_critical_zero_all_ade(self, gt, gr):
        """kappa_ch = 0 at critical level for all types."""
        # VERIFIED [DC] dim(g)*0/(2*h^v)=0 [LT] universal
        ka = kappa_analysis_hitchin_k3(gt, gr)
        assert ka.kappa_at_critical == 0


# ======================================================================
# 8. FAMILY OVER |L|
# ======================================================================

class TestHitchinK3Family:
    """Universal Hitchin family over the K3 linear system."""

    def test_sl2_genus2_total_base(self):
        """Total base dim = dim |L| + dim B = 2 + 3 = 5."""
        # VERIFIED [DC] 2+3=5 [DA] dimensional count
        fam = hitchin_k3_family(2, 'A', 1)
        assert fam.dim_total_base == 5

    def test_sl2_genus2_total_moduli(self):
        """Total moduli dim = dim |L| + dim M_H = 2 + 6 = 8."""
        # VERIFIED [DC] 2+6=8 [DA] dimensional count
        fam = hitchin_k3_family(2, 'A', 1)
        assert fam.dim_total_moduli == 8

    def test_sl2_genus2_universal_spectral(self):
        """Universal spectral dim = dim |L| + dim B = 2 + 3 = 5."""
        # VERIFIED [DC] 2+3=5 [DA] dimensional count
        fam = hitchin_k3_family(2, 'A', 1)
        assert fam.dim_universal_spectral == 5

    def test_family_status_conjectural(self):
        """Family factorization sheaf status is CONJECTURAL."""
        fam = hitchin_k3_family(2, 'A', 1)
        assert fam.status == 'CONJECTURAL'

    def test_sl2_genus3_total_base(self):
        """g=3: total base = 3 + 6 = 9."""
        # VERIFIED [DC] 3+6=9 [DA] dimensional count
        fam = hitchin_k3_family(3, 'A', 1)
        assert fam.dim_total_base == 9


# ======================================================================
# 9. EXPLICIT EXAMPLES
# ======================================================================

class TestExplicitExamples:
    """Detailed tests for explicit SL_2/E_8 examples."""

    def test_sl2_genus2_is_cy3_type(self):
        """SL_2 genus 2 is the unique 'CY3 type' Hitchin system.

        dim(SL_2)*(g-1) = 3*1 = 3 = dim base = dim fibre.
        """
        # VERIFIED [DC] 3*1=3 [LT] unique CY3-type Hitchin
        s = sl2_genus2_on_k3()['summary']
        assert s['is_cy3_type'] is True

    def test_sl2_genus2_oper_type(self):
        """SL_2 Langlands dual is PGL_2."""
        # VERIFIED [LT] SL_2^L = PGL_2 (dual group)
        s = sl2_genus2_on_k3()['summary']
        assert s['oper_type'] == 'PGL_2'

    def test_sl2_genus3_dim_base(self):
        """SL_2 genus 3: dim B = 6."""
        # VERIFIED [DC] H^0(K^2) = 3*(3-1) = 6
        s = sl2_genus3_on_k3()['summary']
        assert s['dim_hitchin_base'] == 6

    def test_sl2_genus3_spectral_genus(self):
        """SL_2 genus 3: spectral genus = 4*2+1 = 9."""
        # VERIFIED [DC] n^2(g-1)+1 = 4*2+1 = 9
        s = sl2_genus3_on_k3()['summary']
        assert s['spectral_genus'] == 9

    def test_e8_genus2_dim_base(self):
        """E_8 genus 2: dim B = 248."""
        # VERIFIED [DC] dim(E8)*(2-1) = 248 [LT] standard
        s = e8_genus2_on_k3()['summary']
        assert s['dim_hitchin_base'] == 248

    def test_e8_genus2_kappa_k1(self):
        """E_8 level 1: kappa_ch = 1922/15."""
        # VERIFIED [DC] 248*31/60 = 1922/15 [CF] k3_geometric_langlands
        s = e8_genus2_on_k3()['summary']
        assert s['kappa_ch_at_k1'] == F(1922, 15)


# ======================================================================
# 10. ADE LANDSCAPE
# ======================================================================

class TestADELandscape:
    """All standard ADE types at genus 2."""

    def test_landscape_has_9_entries(self):
        """9 standard ADE types: A1-A4, D4-D5, E6-E8."""
        # VERIFIED [DC] count of standard ADE types
        landscape = hitchin_k3_landscape(2)
        assert len(landscape) == 9

    def test_landscape_types(self):
        """Correct type labels."""
        landscape = hitchin_k3_landscape(2)
        types = [e['type'] for e in landscape]
        assert types == ['A1', 'A2', 'A3', 'A4', 'D4', 'D5', 'E6', 'E7', 'E8']

    def test_landscape_dim_g_monotone(self):
        """Group dimensions are monotonically increasing."""
        # VERIFIED [DC] A1=3 < A2=8 < ... < E8=248
        landscape = hitchin_k3_landscape(2)
        dims = [e['group_dim'] for e in landscape]
        assert dims == sorted(dims)

    def test_landscape_hitchin_base_equals_dim_g(self):
        """At g=2: dim B = dim(g)*(g-1) = dim(g) for all types.

        This is because g-1 = 1 for genus 2.
        """
        # VERIFIED [DC] dim(g)*1 = dim(g) [DA] genus-2 specialisation
        landscape = hitchin_k3_landscape(2)
        for e in landscape:
            assert e['dim_hitchin_base'] == e['group_dim'], \
                f"dim B != dim(g) for {e['type']}"

    def test_landscape_simply_laced_c_k1_rank(self):
        """c(hat{g}_1) = rank(g) for simply-laced types.

        For simply-laced g: dim(g) = rank(g)*(1+h^v), so
        c = dim(g)*1/(1+h^v) = rank(g).
        """
        # VERIFIED [DC] dim(g)/(1+h^v) = rank(g) [LT] standard KM identity
        for gt, gr in [('A', 1), ('A', 2), ('A', 3), ('A', 4),
                       ('D', 4), ('D', 5), ('E', 6), ('E', 7), ('E', 8)]:
            h = hitchin_on_k3(2, gt, gr)
            assert h.central_charge_at_k1 == F(gr), \
                f"c(hat{{{gt}{gr}}}_1) != {gr}"


# ======================================================================
# 11. CROSS-VOLUME BRIDGE
# ======================================================================

class TestCrossVolumeBridge:
    """Consistency with existing compute engines."""

    def test_all_bridge_checks_pass(self):
        """All cross-volume bridge checks pass."""
        # VERIFIED [CF] cross-engine consistency
        bridge = cross_volume_hitchin_bridge()
        for key, val in bridge.items():
            assert val['match'], f"Bridge check failed: {key}"

    def test_sl2_g2_hitchin_base_matches_spectral_curve_chiral(self):
        """SL_2, g=2: dim B = 3 matches spectral_curve_chiral formula."""
        # VERIFIED [CF] (n^2-1)*(g-1) = 3*1 = 3
        bridge = cross_volume_hitchin_bridge()
        assert bridge['sl2_g2_hitchin_base']['match']

    def test_sl2_g2_spectral_genus_matches(self):
        """SL_2, g=2: spectral genus = 5 matches."""
        # VERIFIED [CF] n^2*(g-1)+1 = 5
        bridge = cross_volume_hitchin_bridge()
        assert bridge['sl2_g2_spectral_genus']['match']

    def test_kappa_critical_matches(self):
        """kappa_ch at critical = 0 matches geometric_langlands_shadow."""
        # VERIFIED [CF] kappa(g, -h^v) = 0
        bridge = cross_volume_hitchin_bridge()
        assert bridge['sl2_kappa_critical']['match']

    def test_kappa_k1_matches(self):
        """kappa_ch(sl_2, k=1) = 9/4 matches k3_geometric_langlands."""
        # VERIFIED [CF] dim(sl2)*(1+h^v)/(2*h^v) = 9/4
        bridge = cross_volume_hitchin_bridge()
        assert bridge['sl2_kappa_k1']['match']

    def test_e8_central_charge_matches(self):
        """c(E_8, k=1) = 8 matches k3_geometric_langlands."""
        # VERIFIED [CF] rank(E8) = 8
        bridge = cross_volume_hitchin_bridge()
        assert bridge['e8_central_charge_k1']['match']


# ======================================================================
# 12. MASTER VERIFICATION
# ======================================================================

class TestMasterVerification:
    """Run all internal checks via verify_all()."""

    def test_all_checks_pass(self):
        """All 71+ internal checks pass."""
        results = verify_all()
        failed = {k: v for k, v in results.items() if not v}
        assert len(failed) == 0, f"Failed checks: {list(failed.keys())}"

    def test_sufficient_checks(self):
        """At least 70 checks are run."""
        results = verify_all()
        assert len(results) >= 70, f"Only {len(results)} checks (need >= 70)"


# ======================================================================
# 13. DIM_BUN_G STANDALONE
# ======================================================================

class TestDimBunG:
    """Standalone dim Bun_G tests."""

    @pytest.mark.parametrize("gt,gr,g,expected", [
        ('A', 1, 2, 3),    # dim(SL_2)*(2-1) = 3
        ('A', 1, 3, 6),    # dim(SL_2)*(3-1) = 6
        ('A', 2, 2, 8),    # dim(SL_3)*(2-1) = 8
        ('D', 4, 2, 28),   # dim(SO_8)*(2-1) = 28
        ('E', 8, 2, 248),  # dim(E_8)*(2-1) = 248
        ('E', 8, 3, 496),  # dim(E_8)*(3-1) = 496
    ])
    def test_dim_bun_g(self, gt, gr, g, expected):
        """dim Bun_G(C) = dim(G)*(g-1)."""
        # VERIFIED [DC] direct computation [LT] standard formula
        assert dim_bun_g(gt, gr, g) == expected
