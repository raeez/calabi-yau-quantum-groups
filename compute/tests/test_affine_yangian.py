"""Tests for the affine Yangian Y(gl_hat_1) / W_{1+infinity} module.

Manuscript references:
    thm:sv-c3 (toric_cy3_coha.tex): CoHA(C^3) = Y^+(gl_hat_1)
    thm:rsyz (toric_cy3_coha.tex): General toric CY3 gives affine super Yangians
    sec:c3-yangian (toric_cy3_coha.tex): The C^3 / affine Yangian connection

Literature:
    Schiffmann-Vasserot arXiv:1211.1287 (CoHA = positive Yangian)
    Tsymbaliuk arXiv:1404.5240 (affine Yangian presentation)
    Prochazka-Rapcak arXiv:1910.07997 (W_{1+infinity} and Yangian)
    Maulik-Okounkov arXiv:1211.1287 (quantum groups from geometry)

Ground truth values:
    h = (1, 2, -3): sigma_2 = -7, sigma_3 = -6
    phi = [1, 0, 0, 12, 0, 84, 72, 588, 1008, 4548, ...]
    The phi are determined by alpha_k = -2*p_k/k (k odd) via exponentiation.

    Schiffmann-Vasserot GL_N parametrization:
    N=1: h=(1,-1,0), sigma_2=-1, sigma_3=0, phi=[1,0,0,0,...] (abelian)
    N=2: h=(1,-2,1), sigma_2=-3, sigma_3=-2
    N=3: h=(1,-3,2), sigma_2=-7, sigma_3=-6
"""

import pytest
from sympy import Rational, simplify, Symbol, symbols

from compute.lib.affine_yangian_gl1 import (
    crystal_melting_character,
    ef_commutator_coefficient,
    elementary_symmetric_from_h,
    ope_structure_constants_low_order,
    phi_explicit,
    power_sums_from_h,
    psi_e_structure_constants,
    schiffmann_vasserot_parametrization,
    serre_relation_data,
    structure_constant_table,
    structure_function_coefficients,
    structure_function_coefficients_symbolic,
    verify_antisymmetry_parity,
    verify_cy_condition_on_phi,
    verify_g_inversion,
    w_infinity_limit,
)


# ================================================================
# STRUCTURE FUNCTION BASICS
# ================================================================

class TestStructureFunctionCoefficients:
    """Test phi_j computation from the structure function g(z)."""

    def test_phi_0_is_one(self):
        """phi_0 = 1 (normalization of g(z))."""
        phi = structure_function_coefficients(Rational(1), Rational(2), max_order=3)
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert phi[0] == 1

    def test_phi_1_vanishes_cy_condition(self):
        """phi_1 = 0 by the CY condition h1+h2+h3=0."""
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(3), Rational(-1)),
                        (Rational(1, 2), Rational(1, 3))]:
            phi = structure_function_coefficients(h1, h2, max_order=3)
            # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
            assert phi[1] == 0, (
                f"phi_1 should vanish for h=({h1},{h2}), got {phi[1]}"
            )

    def test_phi_2_vanishes(self):
        """phi_2 = 0 because log g has only odd power terms.

        From g(-z) = 1/g(z), the inversion identity forces phi_2 = 0.
        More precisely: log g(z) = sum_{k odd} alpha_k z^{-k}, so
        phi_2 = alpha_1^2/2 = 0 (since alpha_1 = -2*p_1 = 0).
        """
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(5), Rational(-3)),
                        (Rational(1, 7), Rational(2, 7))]:
            phi = structure_function_coefficients(h1, h2, max_order=3)
            # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
            assert phi[2] == 0, (
                f"phi_2 should vanish for h=({h1},{h2}), got {phi[2]}"
            )

    def test_phi_4_vanishes(self):
        """phi_4 = 0 because 4 has no partition into odd parts >= 3."""
        phi = structure_function_coefficients(Rational(1), Rational(2), max_order=5)
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert phi[4] == 0

    def test_phi_3_equals_neg2_sigma3(self):
        """phi_3 = -2*sigma_3 where sigma_3 = h1*h2*h3.

        Derivation: alpha_3 = -2*p_3/3 where p_3 = 3*sigma_3 (Newton).
        phi_3 = alpha_3 = -2*sigma_3.
        """
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(3), Rational(-1)),
                        (Rational(1, 2), Rational(1, 3))]:
            h3 = -(h1 + h2)
            phi = structure_function_coefficients(h1, h2, max_order=4)
            sigma3 = h1 * h2 * h3
            # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
            assert phi[3] == -2 * sigma3, (
                f"phi_3={phi[3]} should equal -2*sigma_3={-2*sigma3} "
                f"for h=({h1},{h2},{h3})"
            )

    def test_phi_6_from_alpha3_squared(self):
        """phi_6 = alpha_3^2 / 2 (from partition 6 = 3+3).

        alpha_3 = -2*sigma_3, so phi_6 = 2*sigma_3^2.
        """
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        phi = structure_function_coefficients(h1, h2, max_order=7)
        sigma3 = h1 * h2 * h3
        alpha3 = -2 * sigma3
        expected = alpha3 ** 2 / 2
        assert phi[6] == expected, (
            f"phi_6={phi[6]} should equal alpha_3^2/2={expected}"
        )

    def test_phi_8_from_alpha3_alpha5(self):
        """phi_8 = alpha_3 * alpha_5 (from partition 8 = 3+5)."""
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        phi = structure_function_coefficients(h1, h2, max_order=9)
        p3 = h1**3 + h2**3 + h3**3
        p5 = h1**5 + h2**5 + h3**5
        alpha3 = Rational(-2) * p3 / 3
        alpha5 = Rational(-2) * p5 / 5
        expected = alpha3 * alpha5
        assert phi[8] == expected, (
            f"phi_8={phi[8]} should equal alpha_3*alpha_5={expected}"
        )

    def test_phi_9_from_two_partitions(self):
        """phi_9 = alpha_9 + alpha_3^3/6 (partitions 9 and 3+3+3)."""
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        phi = structure_function_coefficients(h1, h2, max_order=10)
        p3 = h1**3 + h2**3 + h3**3
        p9 = h1**9 + h2**9 + h3**9
        alpha3 = Rational(-2) * p3 / 3
        alpha9 = Rational(-2) * p9 / 9
        expected = alpha9 + alpha3**3 / 6
        assert phi[9] == expected, (
            f"phi_9={phi[9]} should equal alpha_9+alpha_3^3/6={expected}"
        )

    def test_generic_values_h_1_2_neg3(self):
        """Ground truth values for h=(1,2,-3)."""
        phi = structure_function_coefficients(Rational(1), Rational(2), max_order=9)
        expected = [1, 0, 0, 12, 0, 84, 72, 588, 1008, 4548]
        for j in range(10):
            assert phi[j] == expected[j], (
                f"phi_{j}={phi[j]}, expected {expected[j]}"
            )


# ================================================================
# TWO INDEPENDENT COMPUTATION METHODS AGREE
# ================================================================

class TestPhiExplicitMatchesSeries:
    """Verify phi_explicit (exponential of log) matches series expansion."""

    def test_agreement_at_generic_point(self):
        """phi_explicit and structure_function_coefficients agree for h=(1,2,-3)."""
        h1, h2 = Rational(1), Rational(2)
        phi_exp = phi_explicit(h1, h2, max_order=12)
        phi_ser = structure_function_coefficients(h1, h2, max_order=12)
        for j in range(13):
            assert phi_exp[j] == phi_ser[j], (
                f"Mismatch at j={j}: explicit={phi_exp[j]}, series={phi_ser[j]}"
            )

    def test_agreement_at_rational_point(self):
        """Agreement for h=(1/2, 1/3, -5/6)."""
        h1, h2 = Rational(1, 2), Rational(1, 3)
        phi_exp = phi_explicit(h1, h2, max_order=10)
        phi_ser = structure_function_coefficients(h1, h2, max_order=10)
        for j in range(11):
            assert phi_exp[j] == phi_ser[j], (
                f"Mismatch at j={j}: explicit={phi_exp[j]}, series={phi_ser[j]}"
            )

    def test_agreement_sv_n2(self):
        """Agreement for Schiffmann-Vasserot GL_2: h=(1,-2,1)."""
        h1, h2 = Rational(1), Rational(-2)
        phi_exp = phi_explicit(h1, h2, max_order=8)
        phi_ser = structure_function_coefficients(h1, h2, max_order=8)
        for j in range(9):
            assert phi_exp[j] == phi_ser[j]


# ================================================================
# ELEMENTARY SYMMETRIC AND POWER SUMS
# ================================================================

class TestElementarySymmetric:
    """Test elementary symmetric polynomial computations."""

    def test_sigma1_vanishes(self):
        """sigma_1 = h1+h2+h3 = 0 when h3 = -(h1+h2)."""
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(-5), Rational(3))]:
            s1, _, _ = elementary_symmetric_from_h(h1, h2)
            # VERIFIED [DC] vanishing check [LT] Drinfeld Yangian theory
            assert s1 == 0

    def test_sigma2_h_1_2_neg3(self):
        """sigma_2 = -(1^2 + 1*2 + 2^2) = -7 for h=(1,2,-3)."""
        _, s2, _ = elementary_symmetric_from_h(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s2 == -7

    def test_sigma3_h_1_2_neg3(self):
        """sigma_3 = 1*2*(-3) = -6."""
        _, _, s3 = elementary_symmetric_from_h(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s3 == -6

    def test_sigma2_sv_n2(self):
        """GL_2: h=(1,-2,1), sigma_2 = 1*(-2)+1*1+(-2)*1 = -3."""
        _, s2, _ = elementary_symmetric_from_h(Rational(1), Rational(-2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s2 == -3

    def test_sigma3_sv_n2(self):
        """GL_2: h=(1,-2,1), sigma_3 = 1*(-2)*1 = -2."""
        _, _, s3 = elementary_symmetric_from_h(Rational(1), Rational(-2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s3 == -2


class TestPowerSums:
    """Test Newton power sum computations."""

    def test_p1_vanishes(self):
        """p_1 = 0 by CY condition."""
        p = power_sums_from_h(Rational(1), Rational(2))
        # VERIFIED [DC] vanishing check [LT] Drinfeld Yangian theory
        assert p[1] == 0

    def test_p2_h_1_2_neg3(self):
        """p_2 = 1^2 + 2^2 + (-3)^2 = 14."""
        p = power_sums_from_h(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert p[2] == 14

    def test_p3_equals_3_sigma3(self):
        """p_3 = 3*sigma_3 (Newton's identity with sigma_1=0, p_1=0)."""
        h1, h2 = Rational(1), Rational(2)
        h3 = -(h1 + h2)
        p = power_sums_from_h(h1, h2)
        sigma3 = h1 * h2 * h3
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert p[3] == 3 * sigma3


# ================================================================
# G(Z) INVERSION IDENTITY
# ================================================================

class TestGInversion:
    """Test the key identity g(z)*g(-z) = 1."""

    def test_inversion_generic(self):
        """g(z)*g(-z) = 1 for h=(1,2,-3)."""
        result = verify_g_inversion(Rational(1), Rational(2), max_order=10)
        assert result["all_pass"], (
            f"Inversion failed: {result['checks']}"
        )

    def test_inversion_rational_params(self):
        """g(z)*g(-z) = 1 for h=(1/2, 1/3, -5/6)."""
        result = verify_g_inversion(Rational(1, 2), Rational(1, 3), max_order=8)
        assert result["all_pass"]

    def test_inversion_sv_n2(self):
        """g(z)*g(-z) = 1 for Schiffmann-Vasserot GL_2."""
        result = verify_g_inversion(Rational(1), Rational(-2), max_order=8)
        assert result["all_pass"]

    def test_cauchy_product_explicit_n2(self):
        """Explicit check: sum_{a+b=2} (-1)^b phi_a phi_b = 0."""
        phi = structure_function_coefficients(Rational(1), Rational(2), max_order=3)
        # n=2: phi_0*phi_2*1 + phi_1*phi_1*(-1) + phi_2*phi_0*1
        val = phi[0] * phi[2] - phi[1] * phi[1] + phi[2] * phi[0]
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert val == 0

    def test_cauchy_product_explicit_n6(self):
        """Explicit check: sum_{a+b=6} (-1)^b phi_a phi_b = 0.

        phi_0*phi_6 - phi_1*phi_5 + phi_2*phi_4 - phi_3^2 + phi_4*phi_2
        - phi_5*phi_1 + phi_6*phi_0 = 72 - 0 + 0 - 144 + 0 - 0 + 72 = 0.
        """
        phi = structure_function_coefficients(Rational(1), Rational(2), max_order=7)
        val = sum(phi[a] * phi[6 - a] * ((-1) ** (6 - a))
                  for a in range(7))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert val == 0


class TestAntisymmetryParity:
    """Test parity of phi under h_i -> -h_i."""

    def test_parity_generic(self):
        """phi_j(-h) = (-1)^j phi_j(h)."""
        result = verify_antisymmetry_parity(Rational(1), Rational(2), max_order=10)
        assert result["all_pass"]

    def test_parity_rational(self):
        result = verify_antisymmetry_parity(Rational(1, 3), Rational(2, 5), max_order=8)
        assert result["all_pass"]


# ================================================================
# CY CONDITION ON STRUCTURE CONSTANTS
# ================================================================

class TestCYCondition:
    """Test consequences of the Calabi-Yau condition h1+h2+h3=0."""

    def test_phi_1_vanishes(self):
        result = verify_cy_condition_on_phi(Rational(1), Rational(2))
        assert result["phi_1_zero"]

    def test_phi_2_vanishes(self):
        result = verify_cy_condition_on_phi(Rational(1), Rational(2))
        assert result["phi_2_zero"]

    def test_phi_3_identity(self):
        result = verify_cy_condition_on_phi(Rational(1), Rational(2))
        assert result["phi_3_check"]

    def test_phi_4_vanishes(self):
        result = verify_cy_condition_on_phi(Rational(1), Rational(2), max_order=5)
        assert result["phi_4_zero"]


# ================================================================
# SYMBOLIC COEFFICIENTS
# ================================================================

class TestSymbolicCoefficients:
    """Test symbolic phi computation in terms of h1, h2."""

    def test_phi_0_is_one_symbolic(self):
        phi = structure_function_coefficients_symbolic(max_order=3)
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert phi[0] == 1

    def test_phi_1_vanishes_symbolic(self):
        phi = structure_function_coefficients_symbolic(max_order=3)
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert simplify(phi[1]) == 0

    def test_phi_2_vanishes_symbolic(self):
        phi = structure_function_coefficients_symbolic(max_order=3)
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert simplify(phi[2]) == 0

    def test_phi_3_symbolic_matches_neg2_sigma3(self):
        """phi_3 = -2*h1*h2*(h1+h2) symbolically."""
        h1, h2 = symbols("h1 h2")
        phi = structure_function_coefficients_symbolic(max_order=4)
        sigma3 = h1 * h2 * (-(h1 + h2))
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert simplify(phi[3] + 2 * sigma3) == 0


# ================================================================
# SCHIFFMANN-VASSEROT PARAMETRIZATION
# ================================================================

class TestSchiffmannVasserot:
    """Test the GL_N parametrization h=(1,-N,N-1)."""

    def test_cy_condition(self):
        """h1+h2+h3 = 1+(-N)+(N-1) = 0 for all N."""
        for N in range(1, 6):
            sv = schiffmann_vasserot_parametrization(N)
            # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
            assert sv["sigma_1"] == 0

    def test_gl1_abelian(self):
        """GL_1: h=(1,-1,0), sigma_3=0, all phi_j=0 for j>=1."""
        sv = schiffmann_vasserot_parametrization(1)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_3"] == 0
        for j in range(1, len(sv["phi"])):
            # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
            assert sv["phi"][j] == 0, (
                f"GL_1 phi_{j}={sv['phi'][j]} should be 0"
            )

    def test_gl1_sigma2(self):
        """GL_1: sigma_2 = 1*(-1)+1*0+(-1)*0 = -1."""
        sv = schiffmann_vasserot_parametrization(1)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_2"] == -1

    def test_gl2_sigma(self):
        """GL_2: sigma_2=-3, sigma_3=-2."""
        sv = schiffmann_vasserot_parametrization(2)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_2"] == -3
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_3"] == -2

    def test_gl3_sigma(self):
        """GL_3: sigma_2=-7, sigma_3=-6."""
        sv = schiffmann_vasserot_parametrization(3)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_2"] == -7
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_3"] == -6

    def test_gl_n_sigma2_formula(self):
        """sigma_2 = -(N^2 - N + 1) for the SV parametrization."""
        for N in range(1, 8):
            sv = schiffmann_vasserot_parametrization(N)
            expected = -(N**2 - N + 1)
            assert sv["sigma_2"] == expected, (
                f"GL_{N}: sigma_2={sv['sigma_2']}, expected {expected}"
            )

    def test_gl_n_sigma3_formula(self):
        """sigma_3 = N(1-N) = -N(N-1) for the SV parametrization."""
        for N in range(1, 8):
            sv = schiffmann_vasserot_parametrization(N)
            expected = N * (1 - N)
            assert sv["sigma_3"] == expected, (
                f"GL_{N}: sigma_3={sv['sigma_3']}, expected {expected}"
            )

    def test_gl_n_phi3(self):
        """phi_3 = -2*sigma_3 = 2*N*(N-1) for the SV parametrization."""
        for N in range(1, 6):
            sv = schiffmann_vasserot_parametrization(N)
            expected = 2 * N * (N - 1)
            assert sv["phi"][3] == expected, (
                f"GL_{N}: phi_3={sv['phi'][3]}, expected {expected}"
            )


# ================================================================
# W_{1+INFINITY} LIMIT
# ================================================================

class TestWInfinityLimit:
    """Test the epsilon -> 0 limit at h=(1,eps,-1-eps)."""

    def test_eps_zero_is_abelian(self):
        """At eps=0: h=(1,0,-1), sigma_3=0, g(z)=1 (trivial/abelian)."""
        lim = w_infinity_limit(eps_values=[Rational(0)])
        data = lim[Rational(0)]
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert data["sigma_3"] == 0
        # All phi vanish for j >= 1
        for j in range(1, len(data["phi"])):
            # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
            assert data["phi"][j] == 0

    def test_eps_zero_sigma2(self):
        """At eps=0: sigma_2 = -1."""
        lim = w_infinity_limit(eps_values=[Rational(0)])
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert lim[Rational(0)]["sigma_2"] == -1

    def test_phi3_proportional_to_eps(self):
        """phi_3 = -2*sigma_3 = 2*eps*(1+eps) is O(eps) as eps->0."""
        lim = w_infinity_limit(eps_values=[Rational(1, 10), Rational(1, 100)])
        # phi_3 at eps=1/10: -2 * (1)*(1/10)*(-1-1/10) = -2*(-11/100) = 11/50
        phi3_10 = lim[Rational(1, 10)]["phi"][3]
        assert phi3_10 == Rational(11, 50)

        # phi_3 at eps=1/100: -2*(1)*(1/100)*(-101/100) = 101/5000
        phi3_100 = lim[Rational(1, 100)]["phi"][3]
        assert phi3_100 == Rational(101, 5000)

        # Exact ratio: phi_3 = 2*eps*(1+eps), so
        # ratio = (1/10 * 11/10) / (1/100 * 101/100) = 1100/101 ~ 10.89
        ratio = phi3_10 / phi3_100
        assert ratio == Rational(1100, 101), (
            f"phi_3 ratio {ratio} should be 1100/101"
        )
        # As eps -> 0, phi_3 ~ 2*eps, so the ratio of phi_3 values
        # at eps and eps/10 approaches 10. Here eps is not infinitesimal,
        # so the ratio is 10.89 (the 1+eps correction is visible).
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert abs(float(ratio) - 10) < 1, (
            f"phi_3 ratio {ratio} should be near 10 (within O(eps) correction)"
        )

    def test_deformation_from_abelian(self):
        """The structure constants smoothly deform from the abelian point."""
        eps_vals = [Rational(0), Rational(1, 1000), Rational(1, 100),
                    Rational(1, 10)]
        lim = w_infinity_limit(eps_values=eps_vals)

        # sigma_3 increases monotonically in |eps|
        s3_vals = [abs(lim[e]["sigma_3"]) for e in eps_vals]
        for i in range(len(s3_vals) - 1):
            assert s3_vals[i] <= s3_vals[i + 1]


# ================================================================
# PSI-E STRUCTURE CONSTANTS
# ================================================================

class TestPsiEStructure:
    """Test the psi-e OPE coefficients gamma_n = (phi*phi)_n."""

    def test_gamma_0_is_one(self):
        """gamma_0 = phi_0^2 = 1."""
        result = psi_e_structure_constants(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert result["gamma"][0] == 1

    def test_gamma_1_vanishes(self):
        """gamma_1 = 2*phi_0*phi_1 = 0."""
        result = psi_e_structure_constants(Rational(1), Rational(2))
        # VERIFIED [DC] vanishing check [LT] Drinfeld Yangian theory
        assert result["gamma"][1] == 0

    def test_gamma_2_vanishes(self):
        """gamma_2 = phi_1^2 + 2*phi_0*phi_2 = 0 + 0 = 0."""
        result = psi_e_structure_constants(Rational(1), Rational(2))
        # VERIFIED [DC] vanishing check [LT] Drinfeld Yangian theory
        assert result["gamma"][2] == 0

    def test_gamma_3_equals_2phi3(self):
        """gamma_3 = 2*phi_0*phi_3 + 2*phi_1*phi_2 = 2*phi_3."""
        result = psi_e_structure_constants(Rational(1), Rational(2))
        phi = result["phi"]
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert result["gamma"][3] == 2 * phi[3]

    def test_gamma_is_cauchy_product(self):
        """gamma_n = sum_{a+b=n} phi_a * phi_b (definition of convolution)."""
        h1, h2 = Rational(1), Rational(2)
        result = psi_e_structure_constants(h1, h2, max_mode=8)
        phi = result["phi"]
        gamma = result["gamma"]
        for n in range(len(gamma)):
            expected = sum(phi[a] * phi[n - a]
                          for a in range(n + 1)
                          if a < len(phi) and (n - a) < len(phi))
            assert gamma[n] == expected, (
                f"gamma_{n}={gamma[n]}, expected {expected}"
            )


# ================================================================
# E-F COMMUTATOR
# ================================================================

class TestEFCommutator:
    """Test the [e_i, f_j] = psi_{i+j} normalization."""

    def test_ef_normalization_h_1_2_neg3(self):
        """sigma_3 = -6 for h=(1,2,-3)."""
        s3 = ef_commutator_coefficient(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s3 == -6

    def test_ef_normalization_gl1(self):
        """sigma_3 = 0 for GL_1 (abelian: [e,f]=0)."""
        s3 = ef_commutator_coefficient(Rational(1), Rational(-1))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s3 == 0

    def test_ef_normalization_gl2(self):
        """sigma_3 = -2 for GL_2."""
        s3 = ef_commutator_coefficient(Rational(1), Rational(-2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert s3 == -2


# ================================================================
# OPE STRUCTURE CONSTANTS
# ================================================================

class TestOPEStructureConstants:
    """Test the W_{1+infty} OPE structure constants."""

    def test_phi_2_is_zero(self):
        """phi_2 = 0 (not -2*sigma_2 as one might naively expect)."""
        result = ope_structure_constants_low_order(Rational(1), Rational(2))
        assert result["phi_2_is_zero"]

    def test_phi_3_identity(self):
        """phi_3 = -2*sigma_3."""
        result = ope_structure_constants_low_order(Rational(1), Rational(2))
        assert result["phi_3_equals_neg2_sigma3"]

    def test_sigma_values(self):
        """sigma_2 and sigma_3 are correctly computed."""
        result = ope_structure_constants_low_order(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert result["sigma_2"] == -7
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert result["sigma_3"] == -6


# ================================================================
# SERRE RELATIONS
# ================================================================

class TestSerreRelations:
    """Test the cubic Serre relation data."""

    def test_phi_1_vanishes_in_serre(self):
        """The leading term phi_1 = 0 in the Serre relation."""
        data = serre_relation_data(Rational(1), Rational(2))
        assert data["phi_1_vanishes"]

    def test_serre_phi_values(self):
        """Structure constants in the Serre relation for h=(1,2,-3)."""
        data = serre_relation_data(Rational(1), Rational(2))
        # VERIFIED [DC] duality relation [LT] Drinfeld Yangian theory
        assert data["phi_1"] == 0
        # VERIFIED [DC] duality relation [LT] Drinfeld Yangian theory
        assert data["phi_2"] == 0
        # VERIFIED [DC] duality relation [LT] Drinfeld Yangian theory
        assert data["phi_3"] == 12


# ================================================================
# STRUCTURE CONSTANT TABLE
# ================================================================

class TestStructureConstantTable:
    """Test the comprehensive structure constant table."""

    def test_table_sigma_values(self):
        """Table contains correct sigma values."""
        table = structure_constant_table(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert table["sigma_1"] == 0
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert table["sigma_2"] == -7
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert table["sigma_3"] == -6

    def test_table_phi_0(self):
        table = structure_constant_table(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert table["identities"]["phi_0"] == 1

    def test_table_phi_1_zero(self):
        table = structure_constant_table(Rational(1), Rational(2))
        assert table["identities"]["phi_1_zero"]

    def test_table_phi_2_zero(self):
        table = structure_constant_table(Rational(1), Rational(2))
        assert table["identities"]["phi_2_is_zero"]

    def test_table_gamma_0(self):
        table = structure_constant_table(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert table["identities"]["gamma_0"] == 1

    def test_table_gamma_1_zero(self):
        table = structure_constant_table(Rational(1), Rational(2))
        assert table["identities"]["gamma_1_zero"]

    def test_table_gamma_2_eq_2phi2(self):
        """gamma_2 = 2*phi_2 = 0 (both sides vanish)."""
        table = structure_constant_table(Rational(1), Rational(2))
        assert table["identities"]["gamma_2_eq_2phi2"]

    def test_ef_normalization_in_table(self):
        table = structure_constant_table(Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert table["ef_normalization"] == -6


# ================================================================
# CRYSTAL MELTING / PLANE PARTITIONS
# ================================================================

class TestCrystalMelting:
    """Test the crystal melting character (DT partition function)."""

    def test_n1_leading_coefficients(self):
        """N=1: Z_1(q) = MacMahon function, first coefficients.

        M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + ...
        (OEIS A000219: number of plane partitions of n)
        """
        coeffs = crystal_melting_character(1, max_order=5)
        expected = [1, 1, 3, 6, 13, 24]
        for n in range(6):
            assert coeffs[n] == expected[n], (
                f"MacMahon d_{n}={coeffs[n]}, expected {expected[n]}"
            )

    def test_n1_coefficient_0(self):
        """Constant term is always 1 (empty partition)."""
        for N in range(1, 4):
            coeffs = crystal_melting_character(N, max_order=3)
            # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
            assert coeffs[0] == 1

    def test_n2_first_coefficient(self):
        """N=2: d_1 = 2 (two colors for a single box).

        Z_2(q) = prod_{k>=1} 1/(1-q^k)^{2k}, so
        d_1 = 2 (multiplicity of q in the product at k=1 is 2).
        """
        coeffs = crystal_melting_character(2, max_order=3)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert coeffs[1] == 2

    def test_n3_first_coefficient(self):
        """N=3: d_1 = 3."""
        coeffs = crystal_melting_character(3, max_order=3)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert coeffs[1] == 3


# ================================================================
# CROSS-CHECKS: INTERNAL CONSISTENCY
# ================================================================

class TestInternalConsistency:
    """Cross-family consistency checks between different computation paths."""

    def test_sv_n3_equals_generic_1_neg3(self):
        """SV at N=3 has h=(1,-3,2), same sigma as generic h=(1,2,-3) by
        permutation invariance of sigma_2, sigma_3.

        NOTE: h=(1,-3,2) and h=(1,2,-3) are NOT the same h-parameters
        but they DO have the same sigma_2, sigma_3 (which are symmetric
        in h1,h2,h3). So the phi coefficients must agree.
        """
        sv = schiffmann_vasserot_parametrization(3)
        gen = structure_function_coefficients(Rational(1), Rational(2), max_order=8)
        # Both have sigma_2 = -7, sigma_3 = -6
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_2"] == -7
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_3"] == -6
        # phi values must agree (they depend only on h1^k+h2^k+h3^k)
        for j in range(len(sv["phi"])):
            assert sv["phi"][j] == gen[j], (
                f"Mismatch at j={j}: SV={sv['phi'][j]}, generic={gen[j]}"
            )

    def test_phi_determines_gamma(self):
        """gamma is uniquely determined by phi via Cauchy product."""
        table = structure_constant_table(Rational(3), Rational(-1))
        phi = table["phi"]
        gamma = table["gamma"]
        for n in range(min(len(gamma), len(phi))):
            expected = sum(phi[a] * phi[n - a]
                          for a in range(n + 1)
                          if a < len(phi) and (n - a) < len(phi))
            assert gamma[n] == expected

    def test_even_phi_from_odd_alphas(self):
        """All even phi are generated from products of odd alpha.

        Specifically: phi_{2k} = 0 for 2k < 6, phi_6 = alpha_3^2/2, etc.
        """
        phi = structure_function_coefficients(Rational(2), Rational(3), max_order=6)
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert phi[2] == 0
        # VERIFIED [DC] partition function coefficient [LT] Drinfeld Yangian theory
        assert phi[4] == 0
        # phi_6 should be nonzero unless sigma_3 = 0
        h1, h2 = Rational(2), Rational(3)
        h3 = -(h1 + h2)
        sigma3 = h1 * h2 * h3
        alpha3 = -2 * sigma3
        assert phi[6] == alpha3**2 / 2

    def test_gl1_is_abelian_limit(self):
        """GL_1 gives g(z) = 1 (completely abelian structure function).

        h=(1,-1,0): one of the h_i vanishes, making sigma_3=0 and
        the structure function trivial.
        """
        sv = schiffmann_vasserot_parametrization(1)
        for j in range(1, len(sv["phi"])):
            # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
            assert sv["phi"][j] == 0

    def test_permutation_invariance(self):
        """phi_j depends on h_i only through symmetric functions.

        phi(h1,h2,h3) = phi(h2,h1,h3) = phi(h3,h1,h2) = ...
        """
        perms = [
            (Rational(1), Rational(2), Rational(-3)),
            (Rational(2), Rational(1), Rational(-3)),
            (Rational(-3), Rational(1), Rational(2)),
            (Rational(2), Rational(-3), Rational(1)),
        ]
        phi_ref = structure_function_coefficients(
            perms[0][0], perms[0][1], perms[0][2], max_order=8
        )
        for h1, h2, h3 in perms[1:]:
            phi = structure_function_coefficients(h1, h2, h3, max_order=8)
            for j in range(9):
                assert phi[j] == phi_ref[j], (
                    f"Permutation invariance fails at j={j}: "
                    f"h=({h1},{h2},{h3}) gives {phi[j]}, "
                    f"reference gives {phi_ref[j]}"
                )


# ================================================================
# TORIC CY3 CONNECTION
# ================================================================

class TestToricCY3Connection:
    """Tests connecting to the toric CY3 / CoHA story."""

    def test_c3_is_gl1(self):
        """C^3 corresponds to the Jordan quiver, giving GL_1 DT theory.

        The CoHA of C^3 = Y^+(gl_hat_1) at the GL_1 point:
        h = (1, -1, 0) (the N=1 Schiffmann-Vasserot parametrization).
        """
        sv = schiffmann_vasserot_parametrization(1)
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["h_params"] == (Rational(1), Rational(-1), Rational(0))
        # VERIFIED [DC] structural property [LT] Drinfeld Yangian theory
        assert sv["sigma_3"] == 0

    def test_resolved_conifold_is_gl2(self):
        """The resolved conifold (two vertices) gives GL_2 structure.

        h = (1, -2, 1) (N=2 SV parametrization).
        sigma_3 = -2 is nonzero: the algebra is non-abelian.
        """
        sv = schiffmann_vasserot_parametrization(2)
        assert sv["sigma_3"] != 0
        assert sv["phi"][3] != 0

    def test_crystal_melting_reproduces_dt(self):
        """N-colored crystal melting = DT invariants of C^3 with N D-branes.

        The MacMahon function (N=1) starts 1 + q + 3q^2 + 6q^3 + ...
        """
        coeffs = crystal_melting_character(1, max_order=3)
        # VERIFIED [DC] DT invariant [LT] Drinfeld Yangian theory
        assert coeffs == [1, 1, 3, 6]

    def test_sigma2_formula_from_n(self):
        """sigma_2(N) = -(N^2-N+1) encodes the "level" of the W-algebra.

        This is the key formula connecting the rank of the gauge group
        (N D-branes on C^3) to the deformation parameter of the Yangian.
        """
        for N in [1, 2, 3, 4, 5]:
            sv = schiffmann_vasserot_parametrization(N)
            assert sv["sigma_2"] == -(N**2 - N + 1)
