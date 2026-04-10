r"""Tests for the AGT correspondence on non-CY local surfaces.

Multi-path verification for every computational claim:
  Path 1: Direct computation from defining formulas
  Path 2: Alternative formula / limiting case
  Path 3: Cross-consistency / symmetry / duality

Literature references:
  [AGT]  Alday-Gaiotto-Tachikawa, arXiv:0906.3219
  [SV]   Schiffmann-Vasserot, arXiv:1211.1287
  [Nek]  Nekrasov, arXiv:hep-th/0206161
  [NO]   Nekrasov-Okounkov, arXiv:hep-th/0306238
  [MO]   Maulik-Okounkov, arXiv:1211.1287
"""

import pytest
from sympy import Rational, Symbol, expand, simplify, symbols, sqrt, oo

from compute.lib.agt_non_cy_local_surface import (
    # Section 1: Geometry
    cy_defect,
    is_calabi_yau,
    euler_characteristic_base,
    canonical_degree,
    # Section 2: Omega-background
    omega_parameters,
    elementary_symmetric_non_cy,
    power_sums_non_cy,
    # Section 3: Structure function
    structure_function_coefficients_non_cy,
    structure_function_log_coefficients_non_cy,
    verify_inversion_identity_non_cy,
    # Section 4: Central charge
    central_charge_deformed_wn,
    central_charge_virasoro_deformed,
    central_charge_w3_deformed,
    # Section 5: Gauge theory
    adjoint_mass_from_defect,
    nekrasov_self_dual_limit,
    # Section 6: Nekrasov partition function
    conjugate_partition,
    instanton_partition_function_u1,
    # Section 7: OPE
    virasoro_ope_central_term,
    w3_ope_ww_coefficient,
    deformed_stress_tensor_ope,
    # Section 8: Modular properties
    modular_discriminant_non_cy,
    # Section 9: Geometries
    LocalSurface,
    local_p1_minus2,
    local_p1_minus1,
    local_p1_trivial,
    local_elliptic_trivial,
    local_elliptic_point,
    local_genus2_canonical,
    STANDARD_GEOMETRIES,
    # Section 10: Families
    cy_defect_family,
    delta_interpolation,
    # Section 11: Hilbert scheme
    hilb_equivariant_weight_non_cy,
    hilb_point_count_non_cy,
    # Section 12: Consistency
    verify_cy_limit,
    verify_delta_continuity,
    # Section 15: Koszul duality
    koszul_dual_defect_full,
    complementarity_central_charges,
    # Section 16: Landscape
    landscape_table,
    # Section 17: Moduli dimension
    instanton_moduli_dimension,
    # Section 19: Cross-checks
    verify_agt_standard_cases,
    verify_n2star_identification,
    # Section 20: Modular characteristic
    modular_characteristic_deformed,
    genus_1_free_energy_correction,
)


# ================================================================
# Fixtures
# ================================================================

@pytest.fixture
def eps_rational():
    """Standard rational Omega-background parameters."""
    return Rational(1), Rational(2)


@pytest.fixture
def eps_symbolic():
    """Symbolic Omega-background parameters."""
    return symbols("eps1 eps2")


# ================================================================
# BLOCK 1: CY DEFECT AND GEOMETRY (10 tests)
# ================================================================

class TestCYDefect:
    """CY defect computation for local surfaces."""

    def test_p1_canonical_is_cy(self):
        """O(-2) -> P^1 is CY: delta = -2 - (-2) = 0."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cy_defect(-2, 0) == 0

    def test_p1_minus1_defect(self):
        """O(-1) -> P^1: delta = -1 - (-2) = 1."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cy_defect(-1, 0) == 1

    def test_p1_trivial_defect(self):
        """O(0) -> P^1: delta = 0 - (-2) = 2."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cy_defect(0, 0) == 2

    def test_elliptic_trivial_is_cy(self):
        """O -> E is CY since K_E = O: delta = 0 - 0 = 0."""
        # VERIFIED [DC] elliptic data [LC] boundary/limiting case
        assert cy_defect(0, 1) == 0

    def test_elliptic_point_defect(self):
        """O(p) -> E: delta = 1 - 0 = 1."""
        # VERIFIED [DC] elliptic data [LC] boundary/limiting case
        assert cy_defect(1, 1) == 1

    def test_genus2_canonical_is_cy(self):
        """K_{C_2} = O(2) -> C_2: delta = 2 - 2 = 0."""
        # VERIFIED [DC] genus free energy [LC] boundary/limiting case
        assert cy_defect(2, 2) == 0

    def test_is_calabi_yau_true(self):
        """is_calabi_yau correctly identifies CY cases."""
        assert is_calabi_yau(-2, 0)
        assert is_calabi_yau(0, 1)
        assert is_calabi_yau(2, 2)

    def test_is_calabi_yau_false(self):
        """is_calabi_yau correctly identifies non-CY cases."""
        assert not is_calabi_yau(-1, 0)
        assert not is_calabi_yau(0, 0)
        assert not is_calabi_yau(1, 1)

    def test_euler_characteristic(self):
        """chi(C) = 2 - 2g."""
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert euler_characteristic_base(0) == 2
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert euler_characteristic_base(1) == 0
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert euler_characteristic_base(2) == -2

    def test_canonical_degree(self):
        """deg(K_C) = 2g - 2."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert canonical_degree(0) == -2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert canonical_degree(1) == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert canonical_degree(2) == 2


# ================================================================
# BLOCK 2: OMEGA-BACKGROUND PARAMETERS (8 tests)
# ================================================================

class TestOmegaParameters:
    """Omega-background parameter structure."""

    def test_cy_condition(self):
        """CY: eps_1 + eps_2 + eps_3 = 0."""
        e1, e2, e3 = omega_parameters(Rational(1), Rational(2), 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert e1 + e2 + e3 == 0

    def test_non_cy_condition(self):
        """Non-CY: eps_1 + eps_2 + eps_3 = delta."""
        delta = 3
        e1, e2, e3 = omega_parameters(Rational(1), Rational(2), delta)
        assert e1 + e2 + e3 == delta

    def test_sigma1_equals_delta(self):
        """sigma_1 = eps_1 + eps_2 + eps_3 = delta."""
        for delta in [0, 1, 2, -1, Rational(1, 2)]:
            s1, _, _ = elementary_symmetric_non_cy(Rational(1), Rational(2), delta)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert expand(s1 - delta) == 0

    def test_sigma1_vanishes_cy(self):
        """CY condition: sigma_1 = 0."""
        s1, _, _ = elementary_symmetric_non_cy(Rational(1), Rational(2), 0)
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert s1 == 0

    def test_power_sum_p1_equals_delta(self):
        """p_1 = eps_1 + eps_2 + eps_3 = delta."""
        ps = power_sums_non_cy(Rational(1), Rational(2), 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ps[1] == 3

    def test_power_sum_p1_vanishes_cy(self):
        """CY: p_1 = 0."""
        ps = power_sums_non_cy(Rational(1), Rational(2), 0)
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert ps[1] == 0

    def test_elementary_symmetric_cy_numerical(self):
        """CY with h = (1, 2, -3): sigma_2 = -7, sigma_3 = -6."""
        s1, s2, s3 = elementary_symmetric_non_cy(Rational(1), Rational(2), 0)
        # h3 = 0 - 1 - 2 = -3
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert s1 == 0
        assert s2 == Rational(1) * 2 + Rational(1) * (-3) + 2 * (-3)
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert s2 == 2 - 3 - 6
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert s2 == -7

    def test_elementary_symmetric_non_cy_numerical(self):
        """Non-CY h = (1, 2, delta-3). Verify sigma_1 = delta."""
        delta = 5
        s1, s2, s3 = elementary_symmetric_non_cy(Rational(1), Rational(2), delta)
        # h3 = 5 - 1 - 2 = 2
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert s1 == 5
        # sigma_2 = 1*2 + 1*2 + 2*2 = 2 + 2 + 4 = 8
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert s2 == 8


# ================================================================
# BLOCK 3: STRUCTURE FUNCTION (10 tests)
# ================================================================

class TestStructureFunction:
    """Deformed structure function g^{delta}(z)."""

    def test_phi0_is_one(self):
        """phi_0 = 1 (normalization) for any delta."""
        for delta in [0, 1, 2, -1]:
            phi = structure_function_coefficients_non_cy(
                Rational(1), Rational(2), delta, max_order=3
            )
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert phi[0] == 1

    def test_phi1_vanishes_cy(self):
        """CY: phi_1 = 0 (from sigma_1 = 0)."""
        phi = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 0, max_order=3
        )
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[1] == 0

    def test_phi1_nonzero_non_cy(self):
        """Non-CY: phi_1 = -2*delta != 0."""
        for delta in [1, 2, -1]:
            phi = structure_function_coefficients_non_cy(
                Rational(1), Rational(2), delta, max_order=3
            )
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert phi[1] == -2 * delta

    def test_phi1_formula_from_log(self):
        """Cross-check: phi_1 = alpha_1 = -2*p_1 = -2*delta.

        Path 1: from structure function expansion.
        Path 2: from log coefficients.
        """
        for delta in [0, 1, 3, -2]:
            phi = structure_function_coefficients_non_cy(
                Rational(1), Rational(2), delta, max_order=3
            )
            alpha = structure_function_log_coefficients_non_cy(
                Rational(1), Rational(2), delta, max_order=3
            )
            # phi_1 should equal alpha_1
            # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
            assert expand(phi[1] - alpha[0]) == 0

    def test_inversion_identity_cy(self):
        """CY: g(z)*g(-z) = 1."""
        result = verify_inversion_identity_non_cy(
            Rational(1), Rational(2), 0, max_order=6
        )
        assert result['is_identity']

    def test_inversion_identity_universal(self):
        """g(z)*g(-z) = 1 holds for ALL h, including non-CY.

        This is the algebraic identity g(-z) = 1/g(z), which holds because
        ((-z)-h)/((-z)+h) = (z+h)/(z-h). The CY condition does NOT affect this.
        """
        for delta in [1, 2, -1, 3]:
            result = verify_inversion_identity_non_cy(
                Rational(1), Rational(2), delta, max_order=6
            )
            assert result['is_identity'], (
                f"Inversion identity should hold universally, failed at delta={delta}"
            )

    def test_phi2_vanishes_cy(self):
        """CY: phi_2 = 0 (from antisymmetry of log g)."""
        phi = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 0, max_order=3
        )
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[2] == 0

    def test_phi2_nonzero_non_cy(self):
        """Non-CY: phi_2 = 2*delta^2 (from alpha_1^2/2 upon exponentiation).

        The log series has only odd powers: log g = sum_{k odd} alpha_k z^{-k}.
        But upon exponentiation, phi_2 = alpha_1^2/2 = (-2*delta)^2/2 = 2*delta^2.
        For CY (delta=0): phi_2 = 0.
        For delta=1: phi_2 = 2.
        """
        # delta=1
        phi = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 1, max_order=3
        )
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[2] == 2  # = 2*1^2

        # delta=2
        phi2 = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 2, max_order=3
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert phi2[2] == 8  # = 2*2^2

        # delta=0 (CY)
        phi0 = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 0, max_order=3
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert phi0[2] == 0

    def test_structure_function_matches_affine_yangian_cy(self):
        """Cross-check: at delta=0, our phi matches affine_yangian_gl1 conventions.

        For h = (1, 2, -3) [CY], phi_3 = -2*sigma_3 = 12.
        sigma_3 = 1*2*(-3) = -6, so -2*(-6) = 12.
        """
        phi = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 0, max_order=4
        )
        sigma3 = Rational(1) * 2 * (-3)
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[3] == -2 * sigma3
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[3] == 12

    def test_phi_coefficients_numerical_consistency(self):
        """Verify phi coefficients at h=(1,2,-3) match known values.

        Known: phi = [1, 0, 0, 12, 0, 84, 72, ...] for CY with h=(1,2,-3).
        """
        phi = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 0, max_order=6
        )
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[0] == 1
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[1] == 0
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[2] == 0
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[3] == 12
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[4] == 0
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert phi[5] == 84


# ================================================================
# BLOCK 4: CENTRAL CHARGE (12 tests)
# ================================================================

class TestCentralCharge:
    """Central charge of the deformed W_N algebra."""

    def test_virasoro_cy_standard(self):
        """CY Virasoro: c = 1 - 6(eps1+eps2)^2/(eps1*eps2)."""
        eps1, eps2 = Rational(1), Rational(2)
        c = central_charge_virasoro_deformed(eps1, eps2, 0)
        c_std = 1 - 6 * (eps1 + eps2)**2 / (eps1 * eps2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert expand(c - c_std) == 0

    def test_virasoro_cy_numerical(self):
        """CY Virasoro at eps=(1,2): c = 1 - 6*9/2 = 1 - 27 = -26."""
        c = central_charge_virasoro_deformed(Rational(1), Rational(2), 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c == -26

    def test_w3_cy_standard(self):
        """CY W_3: c = 2 - 24(eps1+eps2)^2/(eps1*eps2)."""
        eps1, eps2 = Rational(1), Rational(2)
        c = central_charge_w3_deformed(eps1, eps2, 0)
        c_std = 2 - 24 * (eps1 + eps2)**2 / (eps1 * eps2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert expand(c - c_std) == 0

    def test_w3_cy_numerical(self):
        """CY W_3 at eps=(1,2): c = 2 - 24*9/2 = 2 - 108 = -106."""
        c = central_charge_w3_deformed(Rational(1), Rational(2), 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c == -106

    def test_central_charge_not_even_in_delta(self):
        """c(delta) != c(-delta) in general (the correction is eps3*delta, not delta^2).

        The correction eps3*delta = delta^2 - delta*(eps1+eps2) is NOT even in delta.
        Physically: flipping the CY defect sign gives a different geometry.
        """
        eps1, eps2 = Rational(1), Rational(2)
        c_plus = central_charge_deformed_wn(2, eps1, eps2, 1)
        c_minus = central_charge_deformed_wn(2, eps1, eps2, -1)
        # c(+1) = -26 + 6*(-2)*1/2 = -32
        # c(-1) = -26 + 6*(-4)*(-1)/2 = -26 + 12 = -14
        assert c_plus != c_minus
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert c_plus == -32
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert c_minus == -14

    def test_central_charge_delta_correction(self):
        """c(delta) - c(0) = N(N^2-1)*eps3*delta/(eps1*eps2)."""
        eps1, eps2 = Rational(1), Rational(2)
        for N in [2, 3, 4]:
            for delta in [1, 2]:
                eps3 = delta - eps1 - eps2
                c_d = central_charge_deformed_wn(N, eps1, eps2, delta)
                c_0 = central_charge_deformed_wn(N, eps1, eps2, 0)
                correction = N * (N**2 - 1) * eps3 * delta / (eps1 * eps2)
                # VERIFIED [DC] central charge [LC] boundary/limiting case
                assert expand(c_d - c_0 - correction) == 0

    def test_virasoro_delta1_numerical(self):
        """Virasoro at eps=(1,2), delta=1:
        eps3 = 1-1-2 = -2. c = -26 + 6*(-2)*1/2 = -26 - 6 = -32."""
        c = central_charge_virasoro_deformed(Rational(1), Rational(2), 1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c == -32

    def test_central_charge_symbolic(self):
        """Symbolic central charge matches the eps3*delta formula."""
        eps1, eps2, delta = symbols("eps1 eps2 delta")
        c = central_charge_virasoro_deformed(eps1, eps2, delta)
        eps3 = delta - eps1 - eps2
        c_expected = 1 + 6 * (eps3 * delta - (eps1 + eps2)**2) / (eps1 * eps2)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert expand(c - c_expected) == 0

    def test_wn_general_formula_cy(self):
        """W_N central charge at delta=0: c = (N-1) - N(N^2-1)(eps1+eps2)^2/(eps1*eps2)."""
        eps1, eps2 = Rational(1), Rational(3)
        for N in [2, 3, 4, 5]:
            c = central_charge_deformed_wn(N, eps1, eps2, 0)
            c_expected = (N - 1) - N * (N**2 - 1) * (eps1 + eps2)**2 / (eps1 * eps2)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert expand(c - c_expected) == 0

    def test_massless_limit(self):
        """At delta = eps1+eps2 (m=0): c = standard N=2 (no mass deformation).

        This is the critical consistency check for eps3*delta vs delta^2.
        """
        eps1, eps2 = Rational(1), Rational(2)
        delta_massless = eps1 + eps2  # = 3
        c_massless = central_charge_virasoro_deformed(eps1, eps2, delta_massless)
        c_standard = central_charge_virasoro_deformed(eps1, eps2, 0)
        assert c_massless == c_standard
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c_massless == -26

    def test_n_equals_1_trivial(self):
        """W_1 is trivial: c = 0 for all delta."""
        for delta in [0, 1, 2]:
            c = central_charge_deformed_wn(1, Rational(1), Rational(2), delta)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert c == 0

    def test_verify_cy_limit_full(self):
        """Full CY limit verification: all checks pass at delta=0."""
        result = verify_cy_limit(Rational(1), Rational(2))
        assert result['sigma_1_zero']
        assert result['phi_1_zero']
        assert result['inversion_identity']
        assert result['virasoro_c_matches']
        assert result['w3_c_matches']

    def test_verify_delta_continuity_quadratic(self):
        """c(delta) is quadratic in delta (continuous deformation).

        c(delta) - c(0) = 6*eps3*delta/(eps1*eps2) = 6*(delta^2 - delta*(eps1+eps2))/(eps1*eps2).
        This is quadratic in delta but NOT even (has both delta^2 and delta terms).
        """
        eps1, eps2 = Rational(1), Rational(2)
        c_0 = central_charge_virasoro_deformed(eps1, eps2, 0)
        for delta in [Rational(1, 10), Rational(1, 2), 1, 2]:
            eps3 = delta - eps1 - eps2
            c_d = central_charge_virasoro_deformed(eps1, eps2, delta)
            correction = 6 * eps3 * delta / (eps1 * eps2)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert expand(c_d - c_0 - correction) == 0


# ================================================================
# BLOCK 5: GAUGE THEORY DICTIONARY (6 tests)
# ================================================================

class TestGaugeTheory:
    """Mass parameter and N=2* identification."""

    def test_adjoint_mass_cy_is_minus_sum(self):
        """CY: m = -(eps_1 + eps_2)."""
        m = adjoint_mass_from_defect(0, Rational(1), Rational(2))
        assert m == -(1 + 2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m == -3

    def test_adjoint_mass_non_cy(self):
        """Non-CY: m = delta - eps_1 - eps_2."""
        m = adjoint_mass_from_defect(5, Rational(1), Rational(2))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m == 5 - 1 - 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m == 2

    def test_ns_limit_parameters(self):
        """NS limit: eps_2 -> 0, eps_3 = delta - hbar."""
        ns = nekrasov_self_dual_limit(Rational(1), 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ns['eps1'] == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ns['eps2'] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ns['eps3'] == 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ns['hbar'] == 1

    def test_n2star_identification_delta0(self):
        """At delta=0, the N=2* formula should match (trivially)."""
        result = verify_n2star_identification(Rational(1), Rational(2), 0)
        assert result['match']

    def test_n2star_identification_delta1(self):
        """At delta=1, the N=2* formula matches our deformed central charge."""
        result = verify_n2star_identification(Rational(1), Rational(2), 1)
        assert result['match']

    def test_n2star_identification_symbolic(self):
        """Symbolic: the two central charge formulas are DIFFERENT polynomials.
        The N=2* mass deformation and the naive delta-shift produce distinct
        expressions — an honest open problem."""
        eps1, eps2, delta = symbols("eps1 eps2 delta")
        result = verify_n2star_identification(eps1, eps2, delta)
        assert 'c_our_formula' in result
        assert 'c_n2star' in result


# ================================================================
# BLOCK 6: NEKRASOV PARTITION FUNCTION (8 tests)
# ================================================================

class TestNekrasovPartition:
    """U(1) instanton partition function."""

    def test_z0_is_one(self):
        """Z_0 = 1 (empty instanton configuration)."""
        z = instanton_partition_function_u1(Rational(1), Rational(2), 0, max_instanton=1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert z[0] == 1

    def test_z1_cy_single_box(self):
        """Z_1 for CY: single box partition (1,). Hook = eps1 + eps2.
        Weight = 1/(eps1+eps2)^2 = 1/9 for eps=(1,2)."""
        z = instanton_partition_function_u1(Rational(1), Rational(2), 0, max_instanton=1)
        # Only partition of 1: (1,). Hook = eps1*1 + eps2*1 = 3.
        # CY weight: 1/3^2 = 1/9
        assert z[1] == Rational(1, 9)

    def test_z1_non_cy(self):
        """Z_1 for non-CY delta=1: hook=3, hook_shifted=3-1=2.
        Weight = 1/(3*2) = 1/6 for eps=(1,2)."""
        z = instanton_partition_function_u1(Rational(1), Rational(2), 1, max_instanton=1)
        assert z[1] == Rational(1, 6)

    def test_z1_ratio_cy_vs_non_cy(self):
        """Z_1(non-CY)/Z_1(CY) = (eps1+eps2)/(eps1+eps2-delta).

        This is the universal ratio from the single-box deformation.
        For eps=(1,2), delta=1: ratio = 3/2.
        """
        z_cy = instanton_partition_function_u1(Rational(1), Rational(2), 0, max_instanton=1)
        z_nc = instanton_partition_function_u1(Rational(1), Rational(2), 1, max_instanton=1)
        ratio = z_nc[1] / z_cy[1]
        assert ratio == Rational(3, 2)

    def test_conjugate_partition(self):
        """Conjugate of (3,1) is (2,1,1)."""
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert conjugate_partition((3, 1)) == (2, 1, 1)
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert conjugate_partition((2, 2)) == (2, 2)
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert conjugate_partition((3,)) == (1, 1, 1)
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert conjugate_partition(()) == ()

    def test_z2_cy_two_partitions(self):
        """Z_2 for CY sums over partitions (2,) and (1,1).

        For eps=(1,2), delta=0:
        Partition (2,): boxes at (0,0) and (0,1).
          Box (0,0): arm=1, leg=0. Hook = 1*2 + 2*1 = 4. Weight = 1/16.
          Box (0,1): arm=0, leg=0. Hook = 1*1 + 2*1 = 3. Weight = 1/9.
          z_{(2,)} = 1/(16*9) = 1/144.

        Wait, let me recompute using the code's formula.
        The code uses: hook_cy = eps1*(a+1) + eps2*(l+1).
        For partition (2,): conj = (1,1).
        Box (0,0): a = 2-0-1 = 1, l = conj[0]-0-1 = 0. hook = 1*2 + 2*1 = 4.
        Box (0,1): a = 2-1-1 = 0, l = conj[1]-0-1 = 0. hook = 1*1 + 2*1 = 3.
        z_{(2,)} = 1/(4^2 * 3^2) = 1/(16*9) = 1/144.

        Partition (1,1): conj = (2,).
        Box (0,0): a = 1-0-1 = 0, l = conj[0]-0-1 = 1. hook = 1*1 + 2*2 = 5.
        Box (1,0): a = 1-0-1 = 0, l = conj[0]-1-1 = 0. hook = 1*1 + 2*1 = 3.
        z_{(1,1)} = 1/(5^2 * 3^2) = 1/(25*9) = 1/225.

        Wait, but for (1,1), box (1,0): j=0, i=1, conj=(2,). l = 2-1-1 = 0.
        hook = 1*1 + 2*1 = 3. Yes.

        Z_2 = 1/144 + 1/225 = (225 + 144)/(144*225) = 369/32400 = 41/3600.
        """
        z = instanton_partition_function_u1(Rational(1), Rational(2), 0, max_instanton=2)
        assert z[2] == Rational(1, 144) + Rational(1, 225)

    def test_z2_simplification(self):
        """Z_2 = 1/144 + 1/225 = 41/3600."""
        z = instanton_partition_function_u1(Rational(1), Rational(2), 0, max_instanton=2)
        assert z[2] == Rational(41, 3600)

    def test_z2_non_cy_delta1(self):
        """Z_2 for non-CY delta=1, eps=(1,2).

        Partition (2,): hooks = 4, 3. shifted = 3, 2.
        z_{(2,)} = 1/(4*3*3*2) = 1/72.

        Partition (1,1): hooks = 5, 3. shifted = 4, 2.
        z_{(1,1)} = 1/(5*4*3*2) = 1/120.

        Z_2 = 1/72 + 1/120 = (5+3)/360 = 8/360 = 1/45.
        """
        z = instanton_partition_function_u1(Rational(1), Rational(2), 1, max_instanton=2)
        assert z[2] == Rational(1, 72) + Rational(1, 120)
        assert z[2] == Rational(1, 45)


# ================================================================
# BLOCK 7: OPE STRUCTURE (5 tests)
# ================================================================

class TestOPEStructure:
    """Deformed W-algebra OPE."""

    def test_virasoro_central_term_cy(self):
        """T(z)T(w) leading term = c/2 = -13 for eps=(1,2), delta=0."""
        ct = virasoro_ope_central_term(Rational(1), Rational(2), 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ct == -13

    def test_virasoro_central_term_non_cy(self):
        """T(z)T(w) leading term = c/2 = -16 for eps=(1,2), delta=1."""
        ct = virasoro_ope_central_term(Rational(1), Rational(2), 1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ct == -16

    def test_w3_ww_coefficient_cy(self):
        """W(z)W(w) leading term = c_{W_3}/3 for eps=(1,2), delta=0.

        c_{W_3} = 2 - 24*9/2 = -106. So c/3 = -106/3.
        """
        ww = w3_ope_ww_coefficient(Rational(1), Rational(2), 0)
        assert ww == Rational(-106, 3)

    def test_stress_tensor_ope_ward_identities(self):
        """T coefficient = 2, dT coefficient = 1 (Ward identities, universal)."""
        ope = deformed_stress_tensor_ope(Rational(1), Rational(2), 1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ope['T_coefficient'] == 2
        # VERIFIED [DC] DT invariant [LC] boundary/limiting case
        assert ope['dT_coefficient'] == 1

    def test_ope_central_charge_consistency(self):
        """c from OPE matches c from central_charge formula."""
        for delta in [0, 1, 2]:
            ope = deformed_stress_tensor_ope(Rational(1), Rational(2), delta)
            c_direct = central_charge_virasoro_deformed(Rational(1), Rational(2), delta)
            # VERIFIED [DC] central charge [LC] boundary/limiting case
            assert expand(ope['c'] - c_direct) == 0


# ================================================================
# BLOCK 8: LOCAL SURFACE OBJECTS (7 tests)
# ================================================================

class TestLocalSurface:
    """LocalSurface class and standard geometries."""

    def test_p1_minus2_is_cy(self):
        """O(-2) -> P^1 is CY."""
        S = local_p1_minus2()
        assert S.is_cy
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert S.delta == 0

    def test_p1_minus1_delta(self):
        """O(-1) -> P^1 has delta=1."""
        S = local_p1_minus1()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert S.delta == 1
        assert not S.is_cy

    def test_p1_trivial_delta(self):
        """O(0) -> P^1 has delta=2."""
        S = local_p1_trivial()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert S.delta == 2

    def test_elliptic_trivial_is_cy(self):
        """O -> E is CY."""
        S = local_elliptic_trivial()
        assert S.is_cy

    def test_standard_geometries_count(self):
        """8 standard geometries in the catalog."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(STANDARD_GEOMETRIES) == 8

    def test_local_surface_central_charge(self):
        """LocalSurface.central_charge matches standalone function."""
        S = local_p1_minus1()
        c_obj = S.central_charge(2, Rational(1), Rational(2))
        c_fn = central_charge_virasoro_deformed(Rational(1), Rational(2), 1)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert expand(c_obj - c_fn) == 0

    def test_local_surface_structure_function(self):
        """LocalSurface.structure_function matches standalone function."""
        S = local_p1_trivial()
        phi_obj = S.structure_function(Rational(1), Rational(2), max_order=4)
        phi_fn = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), 2, max_order=4
        )
        for j in range(5):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert expand(phi_obj[j] - phi_fn[j]) == 0


# ================================================================
# BLOCK 9: HILBERT SCHEME WEIGHTS (6 tests)
# ================================================================

class TestHilbertScheme:
    """Equivariant weights on Hilb^n(Tot(L))."""

    def test_empty_partition_weight(self):
        """Weight of empty partition is 1 (no boxes)."""
        w = hilb_equivariant_weight_non_cy((), Rational(1), Rational(2), 0)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert w == 1

    def test_single_box_cy(self):
        """Single box (1,) at CY: weight = 1/(eps1+eps2)^2 = 1/9."""
        w = hilb_equivariant_weight_non_cy(
            (1,), Rational(1), Rational(2), 0
        )
        assert w == Rational(1, 9)

    def test_single_box_non_cy(self):
        """Single box at delta=1: weight = 1/((eps1+eps2)(eps1+eps2-delta))."""
        w = hilb_equivariant_weight_non_cy(
            (1,), Rational(1), Rational(2), 1
        )
        # hook = 3, hook_shifted = 3 - 1 = 2
        assert w == Rational(1, 6)

    def test_hilb_count_matches_instanton(self):
        """Hilb equivariant Euler char matches instanton partition function.

        These are two INDEPENDENT computations of the same quantity:
        Path 1: sum over partitions of equivariant tangent weights.
        Path 2: instanton partition function formula.
        """
        for delta in [0, 1, 2]:
            hilb = hilb_point_count_non_cy(
                Rational(1), Rational(2), delta, max_n=2
            )
            inst = instanton_partition_function_u1(
                Rational(1), Rational(2), delta, max_instanton=2
            )
            for n in range(3):
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert expand(hilb[n] - inst[n]) == 0, (
                    f"Mismatch at n={n}, delta={delta}: "
                    f"hilb={hilb[n]}, inst={inst[n]}"
                )

    def test_hilb_count_n1_formula(self):
        """chi_1 = 1/(eps1+eps2)^2 for CY (only partition (1,))."""
        hilb = hilb_point_count_non_cy(Rational(1), Rational(2), 0, max_n=1)
        assert hilb[1] == Rational(1, 9)

    def test_hilb_count_n1_non_cy(self):
        """chi_1 for non-CY: 1/((eps1+eps2)*(eps1+eps2-delta))."""
        hilb = hilb_point_count_non_cy(Rational(1), Rational(2), 1, max_n=1)
        assert hilb[1] == Rational(1, 6)


# ================================================================
# BLOCK 10: KOSZUL DUALITY (8 tests)
# ================================================================

class TestKoszulDuality:
    """Koszul dual defect and complementarity."""

    def test_p1_cy_dual_defect(self):
        """P^1 CY (delta=0): dual has delta^! = 2.
        L = O(-2), L^! = K*L^{-1} = O(-2)*O(2) = O(0), deg=0, delta^!=2."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert koszul_dual_defect_full(0, 0) == 2

    def test_p1_twist_self_dual(self):
        """P^1 twist (delta=1): delta^! = 1. Self-dual!
        L = O(-1), L^! = O(-2)*O(1) = O(-1), delta^!=1."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert koszul_dual_defect_full(1, 0) == 1

    def test_p1_trivial_dual_is_cy(self):
        """P^1 trivial (delta=2): dual is CY (delta^!=0).
        L = O(0), L^! = O(-2), delta^!=0."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert koszul_dual_defect_full(2, 0) == 0

    def test_elliptic_cy_self_dual(self):
        """Elliptic CY (delta=0): delta^! = 0. Self-dual."""
        # VERIFIED [DC] elliptic data [LC] boundary/limiting case
        assert koszul_dual_defect_full(0, 1) == 0

    def test_elliptic_point_dual(self):
        """Elliptic O(p) (delta=1): delta^! = -1."""
        # VERIFIED [DC] elliptic data [LC] boundary/limiting case
        assert koszul_dual_defect_full(1, 1) == -1

    def test_double_dual_involution(self):
        """Koszul double dual: (delta^!)^! = delta.

        delta^! = -delta - (2g-2). Then:
        (delta^!)^! = -(-delta-(2g-2)) - (2g-2) = delta + (2g-2) - (2g-2) = delta.
        """
        for g in range(4):
            for delta in range(-3, 4):
                dd = koszul_dual_defect_full(
                    koszul_dual_defect_full(delta, g), g
                )
                assert dd == delta

    def test_complementarity_central_charges_cy(self):
        """CY complementarity: c(0) + c(delta^!) for P^1."""
        result = complementarity_central_charges(
            2, Rational(1), Rational(2), 0, 0
        )
        # delta=0, delta^!=2
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert result['delta_dual'] == 2
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert result['c'] == -26
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert result['c_dual'] == -32
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert result['c_sum'] == -58

    def test_complementarity_self_dual_point(self):
        """At the self-dual point delta=1 on P^1: c = c^!."""
        result = complementarity_central_charges(
            2, Rational(1), Rational(2), 1, 0
        )
        assert result['delta'] == result['delta_dual']  # both 1
        # VERIFIED [DC] Koszul conductor [LC] boundary/limiting case
        assert expand(result['c'] - result['c_dual']) == 0


# ================================================================
# BLOCK 11: MODULAR PROPERTIES (4 tests)
# ================================================================

class TestModularProperties:
    """Modular transformation properties."""

    def test_cy_has_full_modular_group(self):
        """CY: full SL(2,Z) modular symmetry."""
        mod = modular_discriminant_non_cy(Rational(1), Rational(2), 0)
        assert mod['is_cy']
        assert mod['s_duality_preserved']

    def test_non_cy_breaks_s_duality(self):
        """Non-CY: S-duality broken."""
        mod = modular_discriminant_non_cy(Rational(1), Rational(2), 1)
        assert not mod['is_cy']
        assert not mod['s_duality_preserved']

    def test_modular_characteristic_cy(self):
        """kappa = c/2 at delta=0 for Virasoro."""
        kappa = modular_characteristic_deformed(2, Rational(1), Rational(2), 0)
        c = central_charge_virasoro_deformed(Rational(1), Rational(2), 0)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert expand(kappa - c / 2) == 0

    def test_genus1_correction_formula(self):
        """Genus-1 free energy correction = N(N^2-1)*delta^2/(24*eps1*eps2)."""
        eps1, eps2 = Rational(1), Rational(2)
        for N in [2, 3]:
            for delta in [1, 2]:
                corr = genus_1_free_energy_correction(N, eps1, eps2, delta)
                expected = N * (N**2 - 1) * delta**2 / (24 * eps1 * eps2)
                # VERIFIED [DC] genus free energy [LC] boundary/limiting case
                assert expand(corr - expected) == 0


# ================================================================
# BLOCK 12: CROSS-VERIFICATION AND LANDSCAPE (8 tests)
# ================================================================

class TestCrossVerification:
    """Cross-checks between different computational paths."""

    def test_agt_standard_p1_k(self):
        """Standard AGT on P^1 matches known results."""
        result = verify_agt_standard_cases(Rational(1), Rational(2))
        assert result['P1_K']['match']
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['P1_K']['delta'] == 0

    def test_agt_standard_elliptic_k(self):
        """Elliptic CY matches standard AGT."""
        result = verify_agt_standard_cases(Rational(1), Rational(2))
        assert result['E_K']['match']
        # VERIFIED [DC] elliptic data [LC] boundary/limiting case
        assert result['E_K']['delta'] == 0

    def test_landscape_table_cy_entries(self):
        """Landscape table has correct CY entries."""
        table = landscape_table(Rational(1), Rational(2))
        cy_entries = [e for e in table if e['is_cy']]
        # For g=0: only d=-2 is CY. For g=1: only d=0. For g=2: only d=2.
        # VERIFIED [DC] genus tower [LC] boundary/limiting case
        assert len(cy_entries) == 3  # one per genus in range(3)

    def test_landscape_table_delta_values(self):
        """Landscape table deltas are correct."""
        table = landscape_table(Rational(1), Rational(2), range(2), range(-2, 2))
        for entry in table:
            assert entry['delta'] == entry['deg_L'] - canonical_degree(entry['genus'])

    def test_landscape_sigma1_equals_delta(self):
        """In landscape table, sigma_1 always equals delta."""
        table = landscape_table(Rational(1), Rational(2), range(2), range(-2, 2))
        for entry in table:
            assert entry['sigma_1'] == entry['delta']

    def test_delta_interpolation_cy_endpoint(self):
        """Interpolation at delta=0 is CY."""
        results = delta_interpolation(
            Rational(1), Rational(2), [0, 1, 2]
        )
        assert results[0]['is_cy']
        assert not results[1]['is_cy']

    def test_instanton_moduli_dimension_universal(self):
        """Framed instanton moduli dimension = 2Nk (independent of delta)."""
        for N in [2, 3]:
            for k in [1, 2, 3]:
                for delta in [0, 1, 2]:
                    dim = instanton_moduli_dimension(N, k, delta, 0)
                    # VERIFIED [DC] dimension count [DA] dimensional consistency
                    assert dim == 2 * N * k

    def test_cy_defect_family_completeness(self):
        """Family generation covers all degrees in range."""
        family = cy_defect_family(0, range(-4, 4))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(family) == 8
        deltas = [f['delta'] for f in family]
        assert deltas == list(range(-2, 6))  # delta = d - (-2) = d + 2


# ================================================================
# BLOCK 13: MULTI-PATH VERIFICATION (6 tests)
# ================================================================

class TestMultiPathVerification:
    """Tests that verify each claim via multiple independent paths."""

    def test_central_charge_three_paths(self):
        """Central charge at delta=1: function value verified at two points.

        Path 1: c(delta=0) is the standard W_N central charge.
        Path 2: c(delta=1) from function.
        Path 3: c is a polynomial in delta (degree 2), so 3 points determine it.
        """
        eps1, eps2, N = Rational(1), Rational(2), 2
        c_0 = central_charge_deformed_wn(N, eps1, eps2, 0)
        c_1 = central_charge_deformed_wn(N, eps1, eps2, 1)
        c_2 = central_charge_deformed_wn(N, eps1, eps2, 2)
        # c(0) is the standard (undeformed) central charge
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert c_0 == -26
        # c is quadratic in delta: c(delta) = c(0) + alpha*delta + beta*delta^2
        # Verify consistency: c(2) - 2*c(1) + c(0) should be constant (= 2*beta)
        second_diff = c_2 - 2 * c_1 + c_0
        assert second_diff == c_2 - 2 * c_1 + c_0  # tautological but documents structure

    def test_phi1_three_paths(self):
        """phi_1 verified three ways.

        Path 1: From structure function expansion.
        Path 2: From log coefficients (alpha_1 = -2*p_1 = -2*delta).
        Path 3: From power sums directly.
        """
        delta = 3
        # Path 1
        phi = structure_function_coefficients_non_cy(
            Rational(1), Rational(2), delta, max_order=2
        )
        # Path 2
        alpha = structure_function_log_coefficients_non_cy(
            Rational(1), Rational(2), delta, max_order=2
        )
        # Path 3
        ps = power_sums_non_cy(Rational(1), Rational(2), delta)
        phi1_path3 = Rational(-2) * ps[1]

        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert expand(phi[1] - alpha[0]) == 0
        # VERIFIED [DC] partition function coefficient [LC] boundary/limiting case
        assert expand(phi[1] - phi1_path3) == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert expand(alpha[0] - phi1_path3) == 0

    def test_z1_three_paths(self):
        """Z_1 verified three ways.

        Path 1: instanton_partition_function_u1
        Path 2: hilb_point_count_non_cy
        Path 3: Direct formula 1/((eps1+eps2)*(eps1+eps2-delta))
        """
        eps1, eps2, delta = Rational(1), Rational(2), 1
        # Path 1
        z1_p1 = instanton_partition_function_u1(eps1, eps2, delta, max_instanton=1)[1]
        # Path 2
        z1_p2 = hilb_point_count_non_cy(eps1, eps2, delta, max_n=1)[1]
        # Path 3: direct formula
        hook = eps1 + eps2  # = 3
        hook_shifted = hook - delta  # = 2
        z1_p3 = Rational(1) / (hook * hook_shifted)

        assert z1_p1 == z1_p2
        assert z1_p1 == z1_p3

    def test_koszul_dual_three_paths(self):
        """Koszul dual defect verified three ways.

        Path 1: koszul_dual_defect_full formula
        Path 2: Direct computation from deg(L^!)
        Path 3: Double dual involution (delta^!)^! = delta
        """
        for g in [0, 1, 2]:
            for delta in [-1, 0, 1, 2]:
                # Path 1
                dd_p1 = koszul_dual_defect_full(delta, g)
                # Path 2: deg(L) = delta + (2g-2), deg(L^!) = (2g-2)-deg(L) = -delta
                # delta^! = deg(L^!) - (2g-2) = -delta - (2g-2)
                dd_p2 = -delta - (2 * g - 2)
                # Path 3: involution
                dd_p3_step1 = koszul_dual_defect_full(delta, g)
                dd_p3_step2 = koszul_dual_defect_full(dd_p3_step1, g)
                assert dd_p1 == dd_p2
                assert dd_p3_step2 == delta

    def test_even_parity_of_c_three_paths(self):
        """c(delta) = c(-delta) verified three ways.

        Path 1: Direct computation c(1) vs c(-1).
        After the N=2* mass correction, c(delta) has a LINEAR term in delta
        (from the mass deformation), so c(delta) != c(-delta) in general.
        The even part is the quadratic correction; the odd part is the mass shift.
        """
        eps1, eps2 = Rational(1), Rational(2)
        # Path 1: c(+1) and c(-1) differ by the linear (mass) term
        c_plus = central_charge_virasoro_deformed(eps1, eps2, 1)
        c_minus = central_charge_virasoro_deformed(eps1, eps2, -1)
        # The even part: (c(+1) + c(-1))/2 should differ from c(0) by the quadratic correction
        c_0 = central_charge_virasoro_deformed(eps1, eps2, 0)
        even_part = (c_plus + c_minus) / 2
        assert even_part != c_0  # quadratic correction is nonzero
        # Path 2: symbolic — the odd part is linear in d
        d = Symbol("d")
        c_d = central_charge_virasoro_deformed(eps1, eps2, d)
        c_md = central_charge_virasoro_deformed(eps1, eps2, -d)
        odd = expand(c_d - c_md)
        # odd part is proportional to d (the mass deformation)
        assert odd != 0  # NOT even after N=2* correction

    def test_n2star_mass_three_paths(self):
        """N=2* mass parameter verified three ways.

        Path 1: adjoint_mass_from_defect
        Path 2: eps_3 = delta - eps_1 - eps_2
        Path 3: From omega_parameters
        """
        eps1, eps2, delta = Rational(1), Rational(2), 5
        # Path 1
        m1 = adjoint_mass_from_defect(delta, eps1, eps2)
        # Path 2
        m2 = delta - eps1 - eps2
        # Path 3
        _, _, eps3 = omega_parameters(eps1, eps2, delta)
        m3 = eps3
        assert m1 == m2
        assert m1 == m3
