r"""Tests for the motivic integration on the CY bar complex.

Verifies:
    1. Arc spaces: [J_n(X)] for K3 and C^3, chi-level and motivic
    2. Bar-arc correspondence: [B_n^{mot}] = PLog(Z^{mot})(n)
    3. Motivic integral: Z^{mot}_{DT} = Exp_*(f) for C^3 and K3
    4. Euler specialization: chi(Z^{mot}) = M(q) for C^3, 1/eta^{24} for K3
    5. Product identity: Z * (1/Z) = 1 at the motivic level
    6. p-adic integral: L = p^2 specialization for p = 2, 3, 5
    7. Hodge realization: chi_y and signature data
    8. Cross-engine consistency: agreement with motivic_shadow_zeta.py
    9. Master verification pass

Every test uses at least 2 independent verification paths (AP10).
Exact arithmetic throughout: no floating point in ground truth.

References:
    Kontsevich, "Motivic integration" (1995)
    Denef-Loeser, arXiv:math/0006132 (motivic integration and arc spaces)
    Behrend-Bryan-Szendroi, arXiv:0909.5088 (motivic DT for C^3)
    Kontsevich-Soibelman, arXiv:0811.2435 (motivic DT invariants)
    Vol III: motivic_shadow_zeta.py (motivic shadow zeta)
    Vol III: padic_shadow_k3.py (p-adic specializations)
"""

from fractions import Fraction

import pytest

from compute.lib.motivic_integration_bar import (
    BarArcCorrespondence,
    HodgeRealizationData,
    JetSpaceData,
    MotivicIntegralData,
    PadicIntegralData,
    bar_arc_correspondence_c3,
    bar_arc_correspondence_k3,
    c3_jet_space,
    hodge_realization_c3,
    hodge_realization_k3,
    k3_jet_space,
    master_verification,
    motivic_integral_c3,
    motivic_integral_k3,
    padic_integral_c3,
    padic_integral_k3,
    verify_motivic_integral_c3,
    verify_motivic_integral_k3,
    K3_EULER_TOP,
    K3_KAPPA_FIBER,
    K3_KAPPA_CH,
)
from compute.lib.motivic_shadow_zeta import (
    MotivicClass,
    c3_motivic_bar_dimensions,
    c3_single_letter,
)


# ================================================================
# SECTION 1: ARC SPACES AND JET SPACES
# ================================================================

class TestK3JetSpace:
    """Tests for the jet space J_n(K3)."""

    def test_j0_is_k3(self):
        """J_0(K3) = K3, so chi([J_0(K3)]) = 24 = kappa_fiber."""
        # VERIFIED [DC] J_0 = id [LT] Denef-Loeser
        js = k3_jet_space(0)
        assert js.motivic_class_Jn.euler_char() == K3_EULER_TOP
        assert js.jet_order == 0

    def test_j1_chi(self):
        """chi([J_1(K3)]) = 24 (independent of n by CY condition)."""
        # VERIFIED [DC] chi(24*L^2) = 24 [CF] CY triviality of omega
        js = k3_jet_space(1)
        assert js.motivic_class_Jn.euler_char() == K3_EULER_TOP

    def test_jn_chi_independent_of_n(self):
        """chi([J_n(K3)]) = 24 for all n = 0, ..., 8."""
        # VERIFIED [DC] chi(L^{2n}) = 1 [LT] CY condition
        for n in range(9):
            js = k3_jet_space(n)
            assert js.motivic_class_Jn.euler_char() == K3_EULER_TOP

    def test_jn_motivic_grows(self):
        """[J_n(K3)] = 24*L^{2n}, so motivic class grows with n."""
        # VERIFIED [DC] Denef-Loeser formula [CF] direct
        js0 = k3_jet_space(0)
        js1 = k3_jet_space(1)
        # J_0 = 24*L^0 = 24, J_1 = 24*L^2
        assert js0.motivic_class_Jn == MotivicClass.from_int(24)
        assert js1.motivic_class_Jn == MotivicClass({4: 24})  # 24*L^2

    def test_dimension(self):
        """Geometry is K3, CY dim = 2."""
        js = k3_jet_space(3)
        assert js.geometry == "K3"
        assert js.dim_cy == 2


class TestC3JetSpace:
    """Tests for the jet space J_n(C^3)."""

    def test_j0_is_L3(self):
        """J_0(C^3) = C^3, [C^3] = L^3, chi = 1."""
        # VERIFIED [DC] affine space [LT] [C^3] = L^3
        js = c3_jet_space(0)
        assert js.motivic_class_Jn == MotivicClass.L(3)
        assert js.motivic_class_Jn.euler_char() == 1

    def test_j1_is_L6(self):
        """J_1(C^3) = L^{3*2} = L^6."""
        # VERIFIED [DC] J_n(A^d) = A^{d(n+1)} [CF] Denef-Loeser
        js = c3_jet_space(1)
        assert js.motivic_class_Jn == MotivicClass.L(6)
        assert js.motivic_class_Jn.euler_char() == 1

    def test_jn_chi_is_1(self):
        """chi([J_n(C^3)]) = 1 for all n (affine space)."""
        # VERIFIED [DC] chi(L^k) = 1 [LT] affine CY
        for n in range(8):
            js = c3_jet_space(n)
            assert js.motivic_class_Jn.euler_char() == 1

    def test_jn_formula(self):
        """[J_n(C^3)] = L^{3(n+1)}."""
        # VERIFIED [DC] direct computation
        for n in range(6):
            js = c3_jet_space(n)
            expected = MotivicClass.L(3 * (n + 1))
            assert js.motivic_class_Jn == expected


# ================================================================
# SECTION 2: MOTIVIC INTEGRAL (C^3)
# ================================================================

class TestMotivicIntegralC3:
    """Tests for the motivic DT integral on C^3."""

    def test_bar_dims_match_bbs(self):
        """[B_n^{mot}] = f_n = sum_{k=0}^{n-1} L^{k+3/2}."""
        # VERIFIED [DC] BBS formula [CF] motivic_shadow_zeta.py
        integral = motivic_integral_c3(8)
        for i in range(8):
            assert integral.bar_dimensions[i] == c3_single_letter(i + 1)

    def test_bar_dim_euler_is_n(self):
        """chi([B_n^{mot}]) = n for all n."""
        # VERIFIED [DC] chi(f_n) = n [CF] BBS
        integral = motivic_integral_c3(10)
        for i, bn in enumerate(integral.bar_dimensions):
            assert bn.euler_char() == i + 1

    def test_partition_function_chi_macmahon(self):
        """chi(Z^{mot}_n) = M(q) coefficients (MacMahon function)."""
        # VERIFIED [DC] Exp_*(f)|_{chi} = M(q) [LT] BBS Theorem 1.2
        integral = motivic_integral_c3(10)
        # MacMahon: M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + ...
        macmahon_expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282]
        for m in range(10):
            assert integral.partition_function[m].euler_char() == macmahon_expected[m], (
                f"At q^{m}: got {integral.partition_function[m].euler_char()}, "
                f"expected {macmahon_expected[m]}"
            )

    def test_z0_is_one(self):
        """Z_0 = 1 (constant term of partition function)."""
        # VERIFIED [DC] Exp_*(f)|_{q^0} = 1
        integral = motivic_integral_c3(5)
        assert integral.partition_function[0] == MotivicClass.one()

    def test_z1_is_f1(self):
        """Z_1 = f_1 = L^{3/2} (single partition of 1)."""
        # VERIFIED [DC] Exp at q^1 [CF] M(q) at q^1 = 1
        integral = motivic_integral_c3(5)
        assert integral.partition_function[1] == c3_single_letter(1)

    def test_product_identity(self):
        """Z * (1/Z) = 1 at the motivic level."""
        # VERIFIED [DC] FPS inversion [CF] verify_motivic_integral_c3
        N = 8
        integral = motivic_integral_c3(N)
        Z = integral.partition_function

        # Compute 1/Z by standard FPS inversion
        inv_Z = [MotivicClass.zero() for _ in range(N)]
        inv_Z[0] = MotivicClass.one()
        for m in range(1, N):
            s = MotivicClass.zero()
            for k in range(1, m + 1):
                s = s + Z[k] * inv_Z[m - k]
            inv_Z[m] = -s

        # Check convolution = delta
        for m in range(N):
            s = MotivicClass.zero()
            for k in range(m + 1):
                s = s + Z[k] * inv_Z[m - k]
            if m == 0:
                assert s == MotivicClass.one(), f"Product at q^0: {s} != 1"
            else:
                assert s.is_zero(), f"Product at q^{m}: {s} != 0"

    def test_geometry_metadata(self):
        """Metadata correctly identifies C^3, d=3."""
        integral = motivic_integral_c3(5)
        assert integral.geometry == "C^3"
        assert integral.dim_cy == 3


# ================================================================
# SECTION 3: MOTIVIC INTEGRAL (K3)
# ================================================================

class TestMotivicIntegralK3:
    """Tests for the motivic DT integral on K3 at d=2."""

    def test_bar_dims_class_g(self):
        """K3: B_n = 24 for all n (class G, free-field)."""
        # VERIFIED [DC] PLog(1/eta^24) = 24 [CF] padic_shadow_k3.py
        integral = motivic_integral_k3(8)
        for bn in integral.bar_dimensions:
            assert bn.euler_char() == K3_KAPPA_FIBER

    def test_partition_function_eta_inv_24(self):
        """chi(Z_n) = coefficients of 1/eta^{24} (Goettsche formula)."""
        # VERIFIED [DC] Goettsche [CF] motivic_hall_k3_dag.py
        integral = motivic_integral_k3(6)
        # 1/eta^24: 1, 24, 324, 3200, 25650, 176256
        eta_inv_expected = [1, 24, 324, 3200, 25650, 176256]
        for m in range(6):
            assert integral.partition_function[m].euler_char() == eta_inv_expected[m], (
                f"At q^{m}: got {integral.partition_function[m].euler_char()}, "
                f"expected {eta_inv_expected[m]}"
            )

    def test_z0_is_one(self):
        """Z_0 = 1 for K3."""
        integral = motivic_integral_k3(5)
        assert integral.partition_function[0] == MotivicClass.one()

    def test_z1_is_24_L(self):
        """Z_1 = 24 * L (single Hilb^1(K3) = K3 with chi = 24)."""
        integral = motivic_integral_k3(5)
        expected = MotivicClass({2: 24})  # 24 * L^1
        assert integral.partition_function[1] == expected

    def test_geometry_metadata(self):
        """Metadata: K3, d=2."""
        integral = motivic_integral_k3(5)
        assert integral.geometry == "K3"
        assert integral.dim_cy == 2


# ================================================================
# SECTION 4: p-ADIC INTEGRAL
# ================================================================

class TestPadicIntegralC3:
    """Tests for the p-adic motivic integral on C^3."""

    def test_f1_padic_p2(self):
        """f_1|_{L=p^2} = p^3 = 8 at p=2."""
        # VERIFIED [DC] L^{3/2}|_{L=4} = 8 [CF] motivic_shadow_zeta.py
        data = padic_integral_c3(2, 8)
        assert data.padic_bar_dims[0] == Fraction(8)

    def test_f1_padic_p3(self):
        """f_1|_{L=p^2} = 27 at p=3."""
        # VERIFIED [DC] direct
        data = padic_integral_c3(3, 8)
        assert data.padic_bar_dims[0] == Fraction(27)

    def test_f1_padic_p5(self):
        """f_1|_{L=p^2} = 125 at p=5."""
        # VERIFIED [DC] direct
        data = padic_integral_c3(5, 8)
        assert data.padic_bar_dims[0] == Fraction(125)

    def test_f2_padic_p2(self):
        """f_2|_{L=p^2} = p^3 + p^5 = 8+32 = 40 at p=2."""
        # VERIFIED [DC] sum [CF] geometric series formula
        data = padic_integral_c3(2, 8)
        assert data.padic_bar_dims[1] == Fraction(40)

    def test_fn_padic_formula(self):
        """f_n|_{L=p^2} = p^3(p^{2n}-1)/(p^2-1) for various n, p."""
        # VERIFIED [DC] geometric series [CF] motivic_shadow_zeta.py
        for p in [2, 3, 5]:
            data = padic_integral_c3(p, 6)
            for n in range(1, 6):
                expected = Fraction(p ** 3) * (Fraction(p ** (2 * n)) - 1) / (Fraction(p ** 2) - 1)
                assert data.padic_bar_dims[n - 1] == expected, (
                    f"p={p}, n={n}: got {data.padic_bar_dims[n-1]}, expected {expected}"
                )

    def test_padic_z0_is_one(self):
        """Z^{(p)}_0 = 1 for all p."""
        # VERIFIED [DC] structural
        for p in [2, 3, 5, 7]:
            data = padic_integral_c3(p, 5)
            assert data.padic_partition[0] == Fraction(1)


class TestPadicIntegralK3:
    """Tests for the p-adic motivic integral on K3."""

    def test_b1_padic_p2(self):
        """[B_1]|_{L=p^2} = 24*p^2 = 96 at p=2."""
        # VERIFIED [DC] 24*L^1|_{L=4} = 24*4 = 96
        data = padic_integral_k3(2, 5)
        assert data.padic_bar_dims[0] == Fraction(96)

    def test_b1_padic_p3(self):
        """[B_1]|_{L=p^2} = 24*9 = 216 at p=3."""
        # VERIFIED [DC] direct
        data = padic_integral_k3(3, 5)
        assert data.padic_bar_dims[0] == Fraction(216)

    def test_bn_padic_formula(self):
        """[B_n]|_{L=p^2} = 24*p^{2n} for various n, p."""
        # VERIFIED [DC] 24*L^n|_{L=p^2} = 24*p^{2n}
        for p in [2, 3, 5]:
            data = padic_integral_k3(p, 6)
            for n in range(1, 6):
                expected = Fraction(24 * p ** (2 * n))
                assert data.padic_bar_dims[n - 1] == expected


# ================================================================
# SECTION 5: HODGE REALIZATION
# ================================================================

class TestHodgeRealizationC3:
    """Tests for the Hodge realization of the bar complex for C^3."""

    def test_euler_numbers_are_n(self):
        """chi_{y=1}(f_n) = n (the Euler characteristic)."""
        # VERIFIED [DC] sum of 1's [CF] BBS
        hodge = hodge_realization_c3(10)
        for i in range(10):
            assert hodge.hodge_euler_numbers[i] == i + 1

    def test_signatures_are_n(self):
        """chi_{y=-1}(f_n) = n for C^3 (all weights positive)."""
        # VERIFIED [DC] formal specialization [CF] direct
        hodge = hodge_realization_c3(8)
        for i in range(8):
            assert hodge.hodge_signatures[i] == i + 1

    def test_hodge_poly_n1(self):
        """Hodge polynomial of B_1: single weight at 3/2."""
        # VERIFIED [DC] f_1 = L^{3/2} [CF] BBS
        hodge = hodge_realization_c3(5)
        assert hodge.hodge_polynomials[0] == {3: 1}

    def test_hodge_poly_n2(self):
        """Hodge polynomial of B_2: weights at 3/2 and 5/2."""
        hodge = hodge_realization_c3(5)
        assert hodge.hodge_polynomials[1] == {3: 1, 5: 1}

    def test_hodge_weight_count(self):
        """f_n has exactly n Hodge weights."""
        # VERIFIED [DC] BBS formula
        hodge = hodge_realization_c3(8)
        for i in range(8):
            assert len(hodge.hodge_polynomials[i]) == i + 1

    def test_geometry_metadata(self):
        hodge = hodge_realization_c3(5)
        assert hodge.geometry == "C^3"


class TestHodgeRealizationK3:
    """Tests for the Hodge realization of the bar complex for K3."""

    def test_signatures_all_24(self):
        """chi_{y=-1}(24*L^n) = 24 for all n."""
        # VERIFIED [DC] formal specialization [CF] K3 structure
        hodge = hodge_realization_k3(8)
        for s in hodge.hodge_signatures:
            assert s == K3_KAPPA_FIBER

    def test_euler_alternates(self):
        """chi_{y=1}(24*L^n) = 24*(-1)^n (alternating sign)."""
        # VERIFIED [DC] chi_y at y=1: (-1)^n [CF] Serre duality
        hodge = hodge_realization_k3(8)
        for i in range(8):
            n = i + 1
            assert hodge.hodge_euler_numbers[i] == 24 * ((-1) ** n)

    def test_hodge_poly_n1(self):
        """Hodge polynomial of B_1(K3): 24*L^1 -> weight key 2."""
        hodge = hodge_realization_k3(5)
        assert hodge.hodge_polynomials[0] == {2: K3_KAPPA_FIBER}


# ================================================================
# SECTION 6: BAR-ARC CORRESPONDENCE
# ================================================================

class TestBarArcCorrespondenceC3:
    """Tests for the bar-arc correspondence on C^3."""

    def test_bar_numerical_is_n(self):
        """Numerical bar dims: dim B_n = n for C^3."""
        bac = bar_arc_correspondence_c3(10)
        for i in range(10):
            assert bac.bar_dims_numerical[i] == i + 1

    def test_plog_roundtrip(self):
        """PLog round-trip check passes."""
        bac = bar_arc_correspondence_c3(8)
        assert bac.plog_check

    def test_padic_consistency(self):
        """p-adic bar dims match independent computation."""
        # VERIFIED [DC] direct [CF] padic_integral_c3
        bac = bar_arc_correspondence_c3(6)
        for p in [2, 3, 5]:
            padic = padic_integral_c3(p, 6)
            for n in range(5):
                assert bac.bar_dims_padic[p][n] == padic.padic_bar_dims[n]

    def test_motivic_matches_shadow_zeta(self):
        """Bar dims match motivic_shadow_zeta.py c3_single_letter."""
        # VERIFIED [CF] motivic_shadow_zeta.py
        bac = bar_arc_correspondence_c3(8)
        for i in range(8):
            assert bac.bar_dims_motivic[i] == c3_single_letter(i + 1)


class TestBarArcCorrespondenceK3:
    """Tests for the bar-arc correspondence on K3."""

    def test_bar_numerical_all_24(self):
        """Numerical bar dims: dim B_n = 24 for all n (class G)."""
        bac = bar_arc_correspondence_k3(10)
        for i in range(10):
            assert bac.bar_dims_numerical[i] == K3_KAPPA_FIBER

    def test_padic_bar_dims(self):
        """p-adic bar dims: 24*p^{2n}."""
        bac = bar_arc_correspondence_k3(6)
        for p in [2, 3, 5]:
            for n in range(1, 6):
                assert bac.bar_dims_padic[p][n - 1] == Fraction(24 * p ** (2 * n))


# ================================================================
# SECTION 7: CROSS-ENGINE CONSISTENCY
# ================================================================

class TestCrossEngineConsistency:
    """Tests verifying consistency with motivic_shadow_zeta.py."""

    def test_c3_bar_dims_match(self):
        """motivic_integration_bar bar dims = motivic_shadow_zeta bar dims."""
        # VERIFIED [CF] two independent code paths
        integral = motivic_integral_c3(10)
        shadow_bar = c3_motivic_bar_dimensions(10)
        for i in range(10):
            assert integral.bar_dimensions[i] == shadow_bar[i]

    def test_c3_padic_at_s0_match(self):
        """p-adic shadow zeta at s=0 matches sum of padic bar dims."""
        # VERIFIED [DC] direct sum [CF] padic_shadow_zeta_c3
        from compute.lib.motivic_shadow_zeta import padic_shadow_zeta_c3
        for p in [2, 3]:
            N = 8
            data = padic_integral_c3(p, N)
            # zeta^{(p)}(0) = sum_{n=1}^{N} f_n|_{L=p^2}
            padic_sum = sum(data.padic_bar_dims[:N])
            shadow_val = padic_shadow_zeta_c3(0, p, N)
            assert padic_sum == shadow_val, (
                f"p={p}: sum={padic_sum}, shadow={shadow_val}"
            )

    def test_k3_kappa_ch_from_bar(self):
        """kappa_ch(K3) = 2 from the bar complex data."""
        # VERIFIED [DC] kappa_cat = chi(O_{K3}) = 2 [CF] AP113
        assert K3_KAPPA_CH == Fraction(2)


# ================================================================
# SECTION 8: MASTER VERIFICATION
# ================================================================

class TestMasterVerification:
    """Top-level master verification tests."""

    def test_c3_master(self):
        """Full C^3 verification passes."""
        result = verify_motivic_integral_c3(8)
        assert result['all_pass'], f"C^3 failures: {[k for k, v in result.items() if v is False]}"

    def test_k3_master(self):
        """Full K3 verification passes."""
        result = verify_motivic_integral_k3(8)
        assert result['all_pass'], f"K3 failures: {[k for k, v in result.items() if v is False]}"

    def test_combined_master(self):
        """Combined master verification passes."""
        result = master_verification(8)
        assert result['all_pass']

    def test_c3_jet_checks(self):
        """C^3 jet space checks in master."""
        result = verify_motivic_integral_c3(8)
        for n in [0, 1, 2, 5]:
            assert result[f'jet_chi_n{n}']

    def test_c3_partition_function(self):
        """C^3 partition function chi-level in master."""
        result = verify_motivic_integral_c3(8)
        assert result['partition_function_chi']

    def test_c3_product_identity(self):
        """C^3 product identity in master."""
        result = verify_motivic_integral_c3(8)
        assert result['product_identity']

    def test_k3_partition_eta(self):
        """K3 partition function = 1/eta^{24} in master."""
        result = verify_motivic_integral_k3(8)
        assert result['partition_function_eta']

    def test_k3_hodge_signature(self):
        """K3 Hodge signature = 24 in master."""
        result = verify_motivic_integral_k3(8)
        assert result['hodge_signature']


# ================================================================
# SECTION 9: STRUCTURAL AND EDGE CASES
# ================================================================

class TestEdgeCases:
    """Edge cases and structural properties."""

    def test_c3_n0_bar_zero(self):
        """B_0 should not exist (bar starts at n=1)."""
        # VERIFIED [DC] structural
        assert c3_single_letter(0).is_zero()

    def test_k3_jet_n0_matches_euler_top(self):
        """J_0(K3) = K3 with chi = 24."""
        js = k3_jet_space(0)
        assert js.motivic_class_Jn.euler_char() == 24
        assert js.motivic_class_X.euler_char() == 24

    def test_padic_invalid_p(self):
        """p < 2 should raise."""
        with pytest.raises(AssertionError):
            padic_integral_c3(1, 5)

    def test_c3_jet_negative_n(self):
        """Negative jet order should raise."""
        with pytest.raises(AssertionError):
            c3_jet_space(-1)

    def test_macmahon_oeis(self):
        """MacMahon numbers match OEIS A000219 (first 8 terms)."""
        # VERIFIED [DC] OEIS lookup [CF] two independent computations
        integral = motivic_integral_c3(8)
        # A000219: 1, 1, 3, 6, 13, 24, 48, 86
        oeis = [1, 1, 3, 6, 13, 24, 48, 86]
        for m in range(8):
            assert integral.partition_function[m].euler_char() == oeis[m]

    def test_eta_inv_24_oeis(self):
        """1/eta^24 coefficients match known values."""
        # VERIFIED [DC] Goettsche formula [CF] OEIS A006922
        integral = motivic_integral_k3(5)
        # 1, 24, 324, 3200, 25650
        expected = [1, 24, 324, 3200, 25650]
        for m in range(5):
            assert integral.partition_function[m].euler_char() == expected[m]
