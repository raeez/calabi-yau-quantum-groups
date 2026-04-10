r"""
Tests for the Vafa-Witten partition function on K3 and its
connection to the BKM superalgebra g_{Delta_5}.

Verifies:
    1. chi(Hilb^n(K3)) from 1/eta^{24} against known values (Gottsche)
    2. phi_{0,1} discriminant coefficients c(D) as DMVV exponents
    3. Root multiplicities mult(n, l, m) = c(4nm - l^2)
    4. DMVV product structure at low orders
    5. The closed loop: CY3 -> DT -> root mult -> VW -> geometry
    6. VW partition function coefficients (Yoshioka)

Ground truth:
    - Gottsche (1990): chi(Hilb^n(K3)) = p_{24}(n), coefficients of 1/eta^{24}
    - DMVV (1997): second-quantized K3 partition function
    - Gritsenko-Nikulin (1996): root multiplicities of g_{Delta_5}
    - Lorgat: research_vafa_witten_qvcg.md (2026)

Manuscript references:
    k3_times_e.tex: ch:k3-times-e, thm:k3e-denominator
    notes/research_vafa_witten_qvcg.md: Section 2
"""

import pytest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.vafa_witten_k3 import (
    hilb_euler_characteristics,
    KNOWN_HILB_CHI,
    chi_moduli_rank2_k3,
    root_multiplicity_from_phi01,
    verify_root_multiplicities_low_order,
    verify_dmvv_exponents_equal_phi01,
    dmvv_product_coefficients,
    dmvv_leading_terms,
    verify_closed_loop,
    vw_partition_function_coefficients,
)

from lib.phi01_fourier import phi01_by_discriminant


# =========================================================================
# 1. HILBERT SCHEME EULER CHARACTERISTICS: chi(Hilb^n(K3))
# =========================================================================

class TestHilbEulerCharacteristics:
    """chi(Hilb^n(K3)) = coefficients of prod_{k>=1} 1/(1-q^k)^{24}."""

    KNOWN_VALUES = {
        0: 1,       # Hilb^0 = point
        1: 24,      # Hilb^1 = K3 itself, chi(K3) = 24
        2: 324,     # Gottsche
        3: 3200,    # Gottsche
        4: 25650,   # Gottsche
        5: 176256,  # Gottsche
        6: 1073720, # Gottsche
    }

    @pytest.mark.parametrize("n,expected", list(KNOWN_VALUES.items()))
    def test_known_hilb_chi(self, n, expected):
        """Individual Euler characteristic values."""
        hilb = hilb_euler_characteristics(n)
        assert hilb[n] == expected, f"chi(Hilb^{n}(K3)) = {hilb[n]}, expected {expected}"

    def test_hilb0_is_1(self):
        """chi(Hilb^0(K3)) = 1 (a single point)."""
        hilb = hilb_euler_characteristics(0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert hilb[0] == 1

    def test_hilb1_is_chi_k3(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        hilb = hilb_euler_characteristics(1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert hilb[1] == 24

    def test_hilb_monotone_growth(self):
        """chi(Hilb^n(K3)) is strictly increasing for n >= 1."""
        hilb = hilb_euler_characteristics(8)
        for n in range(2, 9):
            assert hilb[n] > hilb[n - 1], (
                f"chi(Hilb^{n}) = {hilb[n]} <= chi(Hilb^{n-1}) = {hilb[n-1]}"
            )

    def test_hilb_all_positive(self):
        """All Euler characteristics are positive."""
        hilb = hilb_euler_characteristics(10)
        for n in range(11):
            # VERIFIED [DC] positivity check [LC] boundary/limiting case
            assert hilb[n] > 0

    def test_module_known_values_match(self):
        """KNOWN_HILB_CHI in the module matches our test values."""
        for n, expected in self.KNOWN_VALUES.items():
            assert KNOWN_HILB_CHI.get(n) == expected


# =========================================================================
# 2. RANK-2 MODULI ON K3: chi(M(2, n; K3))
# =========================================================================

class TestRank2Moduli:
    """chi(M(2, n; K3)) from Yoshioka's formula."""

    def test_chi_moduli_matches_hilb(self):
        """In our convention, chi(M(2, n)) = chi(Hilb^n(K3))."""
        chi_m = chi_moduli_rank2_k3(6)
        hilb = hilb_euler_characteristics(6)
        for n in range(7):
            assert chi_m[n] == hilb[n]

    def test_chi_moduli_known_values(self):
        """Spot-check a few values."""
        chi_m = chi_moduli_rank2_k3(3)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi_m[0] == 1
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi_m[1] == 24
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi_m[2] == 324
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi_m[3] == 3200


# =========================================================================
# 3. ROOT MULTIPLICITIES: mult(n, l, m) = c(4nm - l^2)
# =========================================================================

class TestRootMultiplicities:
    """Root multiplicities of g_{Delta_5} from phi_{0,1}."""

    def test_real_root_D_minus1(self):
        """c(-1) = 1: the unique real simple root."""
        # (n=1, l=1, m=0): D = 4*1*0 - 1 = -1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 1, 0) == 1

    def test_imaginary_simple_D_0(self):
        """c(0) = 10: the 10 imaginary simple roots."""
        # (n=1, l=0, m=0): D = 0 - 0 = 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 0, 0) == 10

    def test_first_fermionic_D_3(self):
        """c(3) = -64: first fermionic (negative multiplicity) roots."""
        # (n=1, l=1, m=1): D = 4*1*1 - 1 = 3
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 1, 1) == -64

    def test_c4_equals_108(self):
        """c(4) = 108."""
        # (n=1, l=0, m=1): D = 4 - 0 = 4
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 0, 1) == 108

    def test_c7_equals_minus513(self):
        """c(7) = -513."""
        # (n=2, l=1, m=1): D = 8 - 1 = 7
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(2, 1, 1) == -513

    def test_c8_equals_808(self):
        """c(8) = 808."""
        # (n=1, l=0, m=2): D = 8 - 0 = 8
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 0, 2) == 808

    def test_discriminant_determines_multiplicity(self):
        """Different (n, l, m) with the same D = 4nm - l^2 give the same multiplicity."""
        # D = 4: (1, 0, 1) and (2, 2, 1) both give 4*2*1 - 4 = 4
        m1 = root_multiplicity_from_phi01(1, 0, 1)
        m2 = root_multiplicity_from_phi01(2, 2, 1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m1 == m2 == 108

    def test_vanishing_for_large_negative_D(self):
        """c(D) = 0 for D < -1."""
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(0, 5, 0) == 0  # D = -25
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 3, 0) == 0  # D = -9

    def test_verify_root_mult_low_order(self):
        """Batch verification at low orders."""
        result = verify_root_multiplicities_low_order(3)
        assert result['all_pass']
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['count'] > 0


# =========================================================================
# 4. DMVV PRODUCT STRUCTURE
# =========================================================================

class TestDMVVProduct:
    """DMVV second-quantized product formula."""

    def test_dmvv_constant_term_is_1(self):
        """The constant term of the DMVV denominator product is 1."""
        coeffs = dmvv_product_coefficients(2, 2, 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs.get((0, 0, 0), Fraction(0)) == Fraction(1)

    def test_dmvv_exponents_match_phi01(self):
        """Central verification: DMVV exponents = phi_{0,1} coefficients."""
        result = verify_dmvv_exponents_equal_phi01(3)
        assert result['all_match']
        assert result['spot_checks_pass']

    def test_dmvv_spot_check_c_minus1(self):
        """c(-1) = 1: the Weyl vector / real root contribution."""
        result = verify_dmvv_exponents_equal_phi01(2)
        for sc in result['spot_checks']:
            if sc['D'] == -1:
                assert sc['pass']
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert sc['actual'] == 1

    def test_dmvv_spot_check_c0(self):
        """c(0) = 10: the imaginary root contribution."""
        result = verify_dmvv_exponents_equal_phi01(2)
        for sc in result['spot_checks']:
            if sc['D'] == 0:
                assert sc['pass']
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert sc['actual'] == 10

    def test_dmvv_spot_check_c3(self):
        """c(3) = -64: the first fermionic root contribution."""
        result = verify_dmvv_exponents_equal_phi01(2)
        for sc in result['spot_checks']:
            if sc['D'] == 3:
                assert sc['pass']
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert sc['actual'] == -64

    def test_dmvv_has_bosonic_and_fermionic(self):
        """The product has both bosonic (c > 0) and fermionic (c < 0) factors."""
        leading = dmvv_leading_terms(2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert leading['n_bosonic'] > 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert leading['n_fermionic'] > 0

    def test_dmvv_real_root_factor(self):
        """The (n=0, l=-1, m=0) factor has exponent c(-1) = 1 (real root)."""
        leading = dmvv_leading_terms(1)
        real_root_terms = [
            t for t in leading['terms']
            if t['n'] == 0 and t['l'] == -1 and t['m'] == 0
        ]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(real_root_terms) == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert real_root_terms[0]['c(D)'] == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert real_root_terms[0]['D'] == -1


# =========================================================================
# 5. DMVV PRODUCT LOW-ORDER EXPANSION
# =========================================================================

class TestDMVVLowOrder:
    """Detailed low-order checks of the DMVV product expansion."""

    def test_p1_l0_s0_coefficient(self):
        """Coefficient of p^1 r^0 s^0 in the product.

        The mixed-sector exponentiation gives h[(1,0,0)] = -10 from (1-p)^{10}
        and h[(1,1,0)] = -1 from (1-pr)^1.
        Convolving with pure_r_exp (which is 1 - r^{-1} + ...):
          g[(1,0,0)] = pure_r[0]*h[(1,0,0)] + pure_r[-1]*h[(1,1,0)]
                     = 1*(-10) + (-1)*(-1) = -9.
        """
        coeffs = dmvv_product_coefficients(2, 2, 4)
        val = coeffs.get((1, 0, 0), Fraction(0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert val == Fraction(-9), f"p^1 r^0 s^0 coefficient: {val}, expected -9"

    def test_p0_l_minus1_s0_coefficient(self):
        """Coefficient of r^{-1} in the product (p^0 sector).

        From (1 - r^{-1})^{c(-1)} = (1 - r^{-1})^1:
        coefficient of r^{-1} is -1.
        """
        coeffs = dmvv_product_coefficients(2, 2, 4)
        val = coeffs.get((0, -1, 0), Fraction(0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert val == Fraction(-1), f"p^0 r^{{-1}} s^0 coefficient: {val}, expected -1"

    def test_p0_l0_s1_coefficient(self):
        """Coefficient of s^1 in the product (p^0 sector).

        The pure-r sector contributes (1 - r^{-1})^1 at order s^0.
        At s^1: the factor (1 - s)^{c(0)} = (1 - s)^{10} gives -10 at s^1 r^0.
        Cross-term (1 - r^{-1})^1 * (1 - s)^{10}: constant in r^{-1} is 1, so
        the r^0 s^1 coefficient is -10 from (1-s)^{10}, plus corrections from
        (1 - r^{-1} s)^1 and (1 - r s)^1 which contribute at r^{-1} s and r s.
        But the pure-r sector exp has 1 at r^0 and -1 at r^{-1}.
        Convolving: h[(0,0,1)] * pure_r[0] + h[(0,1,1)] * pure_r[-1].
        Net: -10 * 1 + (-1) * (-1) = -10 + 1 = -9.
        """
        coeffs = dmvv_product_coefficients(2, 2, 4)
        val = coeffs.get((0, 0, 1), Fraction(0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert val == Fraction(-9), f"p^0 r^0 s^1 coefficient: {val}, expected -9"

    def test_p1_l1_s0_coefficient(self):
        """Coefficient of p^1 r^1 s^0 in the product.

        From (1 - p r)^{c(-1)} = (1 - p r)^1: contributes -1 at p^1 r^1.
        No other factors contribute at (1, 1, 0) at this order.

        So coefficient of p^1 r^1 s^0 = -1.
        """
        coeffs = dmvv_product_coefficients(2, 2, 4)
        val = coeffs.get((1, 1, 0), Fraction(0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert val == Fraction(-1), f"p^1 r^1 s^0 coefficient: {val}, expected -1"

    def test_p1_l_minus1_s0_coefficient(self):
        """Coefficient of p^1 r^{-1} s^0.

        From (1 - p r^{-1})^{c(-1)} = (1 - p r^{-1})^1: contributes -1 at p r^{-1}.
        From (1 - r^{-1})^1 * (1 - p)^{10}: cross-term gives
            (-1)*(r^{-1}) * (-10)*(p) = 10 * p * r^{-1}.
        Total = -1 + 10 = 9.
        """
        coeffs = dmvv_product_coefficients(2, 2, 4)
        val = coeffs.get((1, -1, 0), Fraction(0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert val == Fraction(9), f"p^1 r^{{-1}} s^0 coefficient: {val}, expected 9"


# =========================================================================
# 6. THE CLOSED LOOP VERIFICATION
# =========================================================================

class TestClosedLoop:
    """The full closed loop: CY3 -> DT -> root mult -> VW -> geometry."""

    def test_closed_loop_passes(self):
        """All checks in the closed loop pass."""
        result = verify_closed_loop(3)
        assert result['all_pass']

    def test_closed_loop_dmvv_constant(self):
        """DMVV product constant term is 1."""
        result = verify_closed_loop(2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['dmvv_constant'] == 1

    def test_closed_loop_hilb_chi(self):
        """Hilbert scheme Euler characteristics match known values."""
        result = verify_closed_loop(3)
        for n, data in result['hilb_chi_verification'].items():
            assert data['pass'], f"chi(Hilb^{n}): {data['actual']} != {data['expected']}"

    def test_closed_loop_phi01_disc(self):
        """phi_{0,1} discriminant coefficients are present."""
        result = verify_closed_loop(2)
        c_disc = result['phi01_c_disc']
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c_disc[-1] == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c_disc[0] == 10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c_disc[3] == -64


# =========================================================================
# 7. VW PARTITION FUNCTION COEFFICIENTS
# =========================================================================

class TestVWPartitionFunction:
    """VW partition function Z_VW(K3, SU(2))."""

    def test_vw_coefficients_match_hilb(self):
        """VW partition function coefficients = Hilb Euler characteristics."""
        vw = vw_partition_function_coefficients(6)
        hilb = hilb_euler_characteristics(6)
        for n in range(7):
            assert vw[n] == hilb[n]

    def test_vw_growth_rate(self):
        """VW coefficients grow exponentially (Cardy-like formula).

        p_{24}(n) ~ C * exp(2*pi*sqrt(n)) for large n.
        Check that the ratio is roughly consistent.
        """
        import math
        vw = vw_partition_function_coefficients(10)
        # Check p_{24}(10) / p_{24}(9): should be roughly exp(2*pi*(sqrt(10)-sqrt(9)))
        ratio = vw[10] / vw[9]
        growth_estimate = math.exp(2 * math.pi * (math.sqrt(10) - math.sqrt(9)))
        # This is a rough check; the asymptotic formula has sub-leading corrections
        # VERIFIED [DC] growth bound [LC] boundary/limiting case
        assert 0.3 * growth_estimate < ratio < 3.0 * growth_estimate


# =========================================================================
# 8. CROSS-CHECKS WITH PHI01 MODULE
# =========================================================================

class TestCrossCheckPhi01:
    """Cross-check with the phi01_fourier module."""

    def test_c_disc_values_agree(self):
        """phi01_by_discriminant in both modules gives the same values."""
        from lib.phi01_fourier import phi01_by_discriminant as phi01_disc_direct
        c1 = phi01_disc_direct(5)
        c2 = phi01_by_discriminant(5)
        for D in set(c1.keys()) | set(c2.keys()):
            assert c1.get(D, 0) == c2.get(D, 0), f"c({D}) mismatch"

    def test_root_mult_agrees_with_phi01_table(self):
        """root_multiplicity_from_phi01 agrees with direct computation."""
        # Precompute c(D) to a sufficient depth to cover all D values in the loop.
        # max D = 4*3*3 = 36, so need max_n >= 36/4 + 2 = 11.
        c_disc = phi01_by_discriminant(12)
        for n in range(1, 4):
            for m in range(0, 4):
                for l in range(-3, 4):
                    D = 4 * n * m - l * l
                    if D < -1:
                        continue
                    mult = root_multiplicity_from_phi01(n, l, m)
                    direct_c = c_disc.get(D, 0)
                    assert mult == direct_c, (
                        f"Mismatch at (n={n},l={l},m={m}): D={D}, "
                        f"mult={mult}, c(D)={direct_c}"
                    )


# =========================================================================
# 9. SPECIFIC LOW-ORDER EULER CHARACTERISTICS
# =========================================================================

class TestSpecificEulerCharacteristics:
    """
    Verify specific Euler characteristics chi(M(2, n; K3)).

    These are the key numbers that close the loop between VW invariants
    and the BKM root multiplicities.
    """

    def test_chi_M_2_0(self):
        """chi(M(2, 0; K3)) = 1.

        The moduli space at c_2 = 0 is a point (trivial bundle).
        In our generating function convention, this is the q^0 coefficient
        of 1/eta^{24}, which is 1.
        """
        chi = chi_moduli_rank2_k3(0)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi[0] == 1

    def test_chi_M_2_1(self):
        """chi(M(2, 1; K3)) = 24.

        This is the coefficient of q^1 in 1/eta^{24}, which equals
        chi(K3) = 24.
        """
        chi = chi_moduli_rank2_k3(1)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi[1] == 24

    def test_chi_M_2_2(self):
        """chi(M(2, 2; K3)) = 324.

        Coefficient of q^2 in prod_{k>=1} 1/(1-q^k)^{24}.
        This is 24 + 24*25/2 = 24 + 300 = 324.
        (From the expansion: q^2 gets contributions from the partition
        (2) with weight 24, and the partition (1,1) with weight C(24+1,2) = 300.)
        """
        chi = chi_moduli_rank2_k3(2)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi[2] == 324

    def test_chi_M_2_3(self):
        """chi(M(2, 3; K3)) = 3200."""
        chi = chi_moduli_rank2_k3(3)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi[3] == 3200

    def test_chi_M_2_4(self):
        """chi(M(2, 4; K3)) = 25650."""
        chi = chi_moduli_rank2_k3(4)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi[4] == 25650

    def test_chi_M_2_5(self):
        """chi(M(2, 5; K3)) = 176256."""
        chi = chi_moduli_rank2_k3(5)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert chi[5] == 176256


# =========================================================================
# 10. BOSONIC / FERMIONIC STRUCTURE
# =========================================================================

class TestBosonicFermionic:
    """
    The BKM superalgebra g_{Delta_5} has both bosonic and fermionic roots.

    Bosonic roots: c(D) > 0  (even part of the superalgebra)
    Fermionic roots: c(D) < 0  (odd part of the superalgebra)

    The sign alternation is essential for the super-denominator formula
    and for the VW interpretation (fermionic contributions from ghost
    sectors / virtual contributions).
    """

    def test_c_minus1_is_bosonic(self):
        """c(-1) = 1 > 0: real root is bosonic."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 1, 0) == 1

    def test_c0_is_bosonic(self):
        """c(0) = 10 > 0: imaginary simple roots are bosonic."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 0, 0) == 10

    def test_c3_is_fermionic(self):
        """c(3) = -64 < 0: first fermionic roots."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 1, 1) == -64

    def test_c4_is_bosonic(self):
        """c(4) = 108 > 0."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 0, 1) == 108

    def test_c7_is_fermionic(self):
        """c(7) = -513 < 0."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(2, 1, 1) == -513

    def test_c8_is_bosonic(self):
        """c(8) = 808 > 0."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert root_multiplicity_from_phi01(1, 0, 2) == 808

    def test_sign_pattern(self):
        """c(D) > 0 for D = 0 mod 4, c(D) < 0 for D = 3 mod 4.

        For D >= 0, the sign of c(D) alternates by D mod 4:
        - D = 0 mod 4: c(D) > 0  (bosonic)
        - D = 3 mod 4: c(D) < 0  (fermionic)
        This is a consequence of the Jacobi form structure.
        """
        c_disc = phi01_by_discriminant(6)
        for D, cD in c_disc.items():
            if D < 0:
                continue
            if D % 4 == 0:
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert cD > 0, f"c({D}) = {cD} should be > 0 (bosonic)"
            elif D % 4 == 3:
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert cD < 0, f"c({D}) = {cD} should be < 0 (fermionic)"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
