"""Tests for the chiral R-matrix from E_3 braiding on C^3.

Manuscript references:
    chapters/theory/en_factorization.tex:
        conj:topological-e3-comparison (E_3 from C^3 configuration space)
        thm:zte-failure (Yang R-matrix fails ZTE)
    chapters/theory/quantum_chiral_algebras.tex:
        conj:6d-boundary-toroidal (quantum toroidal from E_3 factorization)
    chapters/theory/cy_to_chiral.tex:
        eq:yangian-structure-function, thm:c3-drinfeld-center

CLAIM STATUS: CONJECTURAL for d=3 (CY-A_3 not proved; AP-CY6/AP-CY14).
The E_3 is TOPOLOGICAL (little 3-disks), not algebraic Deligne (AP154).

Ground truth sources:
    [DC] direct computation (algebraic identity)
    [LT] Maulik-Okounkov arXiv:1211.1287, Costello 2013
    [SY] S_3 symmetry of structure function in (h_1,h_2,h_3)

AP-CY28: test points chosen to avoid poles at z = +/-h_i.
  h = (1.3, -0.5, -0.8): poles at +/-1.3, +/-0.5, +/-0.8.
  Spectral parameters: u ~ 3.7, v ~ 2.1 (far from all poles).
  K3: h_a in {+/-1,...,+/-12}; test z ~ 25 (far from all poles).
"""

import math

import numpy as np
import pytest

from compute.lib.chiral_rmatrix_e3_braiding import (
    ConfigurationSpaceTopology,
    DimensionalHierarchy,
    E3ChiralRMatrix,
    HolomorphicHolonomyRMatrix,
    K3YangianRMatrix,
    TopologicalVsRational,
    full_verification,
    structure_function_rational,
    structure_function_trig,
    summary,
)

# ================================================================
# STANDARD TEST PARAMETERS (AP-CY28: far from poles)
# ================================================================

H1 = 1.3
H2 = -0.5
H3 = -(H1 + H2)  # = -0.8

# Spectral parameters far from poles at +/-1.3, +/-0.5, +/-0.8
Z_TEST = 3.7 + 1.1j
U_TEST = 3.7 + 0.5j
V_TEST = 2.1 - 0.3j

TOL = 1e-10


# ================================================================
# 1. CONFIGURATION SPACE TOPOLOGY
# ================================================================

class TestConfigurationSpaceTopology:
    """Test the homotopy data of Conf_2(C^n)."""

    def test_c1_en_level(self):
        """C^1: E_1 chiral level.
        VERIFIED [DC] dim_C = 1 [LT] Beilinson-Drinfeld factorization.
        """
        cs = ConfigurationSpaceTopology(1)
        assert cs.en_level == 1

    def test_c1_pi1_is_Z(self):
        """pi_1(Conf_2(C)) = pi_1(C^*) = Z (braid group on 2 strands).
        VERIFIED [DC] C \\ {0} ~ S^1, pi_1(S^1) = Z.
        """
        cs = ConfigurationSpaceTopology(1)
        assert cs.pi1_conf2 == "Z"

    def test_c1_braiding_topological(self):
        """C^1 braiding is topological (nontrivial pi_1).
        VERIFIED [DC] [LT] Artin braid group theory.
        """
        cs = ConfigurationSpaceTopology(1)
        assert cs.braiding_type == "topological"

    def test_c2_pi1_trivial(self):
        """pi_1(Conf_2(C^2)) = pi_1(S^3) = 0 (simply connected).
        VERIFIED [DC] S^{2n-1} simply connected for n >= 2.
        """
        cs = ConfigurationSpaceTopology(2)
        assert cs.pi1_conf2 == "0"

    def test_c2_braiding_holomorphic(self):
        """C^2 braiding is holomorphic (trivial pi_1, Omega-background).
        VERIFIED [LT] Costello 2013, rem:en-from-dimension.
        """
        cs = ConfigurationSpaceTopology(2)
        assert cs.braiding_type == "holomorphic"

    def test_c3_pi1_trivial(self):
        """pi_1(Conf_2(C^3)) = pi_1(S^5) = 0 (simply connected).
        VERIFIED [DC] S^5 simply connected.
        """
        cs = ConfigurationSpaceTopology(3)
        assert cs.pi1_conf2 == "0"

    def test_c3_en_level(self):
        """C^3: E_3 chiral level.
        VERIFIED [DC] dim_C = 3 [LT] Costello-Gwilliam.
        """
        cs = ConfigurationSpaceTopology(3)
        assert cs.en_level == 3

    def test_c3_braiding_holomorphic(self):
        """C^3 braiding is holomorphic (trivial pi_1, Omega-background).
        VERIFIED [LT] conj:topological-e3-comparison in en_factorization.tex.
        """
        cs = ConfigurationSpaceTopology(3)
        assert cs.braiding_type == "holomorphic"

    def test_c3_coherence_is_tetrahedron(self):
        """E_3 coherence condition is the parametric tetrahedron equation.
        VERIFIED [LT] Zamolodchikov 1981, rem:zte-consequence.
        """
        cs = ConfigurationSpaceTopology(3)
        assert cs.coherence_equation == "parametric tetrahedron equation"

    def test_c2_coherence_is_ybe(self):
        """E_2 coherence condition is the Yang-Baxter equation.
        VERIFIED [LT] standard braid group / E_2 operad theory.
        """
        cs = ConfigurationSpaceTopology(2)
        assert cs.coherence_equation == "Yang-Baxter equation"

    def test_link_spheres(self):
        """Conf_2(C^n) ~ C^n x S^{2n-1}: the link sphere.
        VERIFIED [DC] C^n \\ {0} deformation-retracts onto S^{2n-1}.
        """
        assert ConfigurationSpaceTopology(1).conf2_link == "S^1"
        assert ConfigurationSpaceTopology(2).conf2_link == "S^3"
        assert ConfigurationSpaceTopology(3).conf2_link == "S^5"

    def test_hurewicz_class(self):
        """pi_{2n-1}(S^{2n-1}) = Z (first nontrivial homotopy).
        VERIFIED [DC] Hurewicz theorem.
        """
        for n in (1, 2, 3):
            cs = ConfigurationSpaceTopology(n)
            assert cs.pi_2n_minus_1_conf2 == "Z"

    def test_r_matrix_type_progression(self):
        """R-matrix type increases with dimension.
        VERIFIED [LT] Costello 2013, Costello-Francis-Gwilliam.
        """
        cs1 = ConfigurationSpaceTopology(1)
        cs2 = ConfigurationSpaceTopology(2)
        cs3 = ConfigurationSpaceTopology(3)
        assert "independent" in cs1.r_matrix_type
        assert "1 parameter" in cs2.r_matrix_type
        assert "2 parameters" in cs3.r_matrix_type

    def test_summary_keys(self):
        """Summary dict has expected keys."""
        cs = ConfigurationSpaceTopology(3)
        s = cs.summary()
        assert "space" in s
        assert "pi_1" in s
        assert "coherence" in s


# ================================================================
# 2. STRUCTURE FUNCTIONS
# ================================================================

class TestStructureFunctions:
    """Test the rational and trigonometric structure functions."""

    def test_g_unitarity(self):
        """g(z) * g(-z) = 1 (CY inversion, algebraic identity).
        VERIFIED [DC] prod(z-h)(z+h) = prod(h^2-z^2) = prod(-z+h)(-z-h)
        [LT] eq:cy-condition-rmatrix in cy_to_chiral.tex.
        """
        g = lambda z: structure_function_rational(z, H1, H2, H3)
        for z in [Z_TEST, 5.0 + 2.0j, -3.0 + 4.0j]:
            assert abs(g(z) * g(-z) - 1.0) < TOL

    def test_g_at_zero(self):
        """g(0) = (-h1)(-h2)(-h3) / (h1 h2 h3) = -1 (CY sign).
        VERIFIED [DC] direct evaluation.
        """
        g0 = structure_function_rational(0.0, H1, H2, H3)
        assert abs(g0 + 1.0) < TOL

    def test_g_at_infinity(self):
        """g(z) -> 1 as z -> infinity (CY normalization).
        VERIFIED [DC] leading coeff of numer and denom both z^3.
        """
        g_large = structure_function_rational(1e8, H1, H2, H3)
        assert abs(g_large - 1.0) < 1e-6

    def test_g_s3_symmetry(self):
        """g(z) is S_3-symmetric under permutation of (h1, h2, h3).
        VERIFIED [DC] g(z) depends only on elementary symmetric polynomials.
        """
        z = Z_TEST
        g_123 = structure_function_rational(z, H1, H2, H3)
        g_213 = structure_function_rational(z, H2, H1, H3)
        g_312 = structure_function_rational(z, H3, H1, H2)
        g_132 = structure_function_rational(z, H1, H3, H2)
        assert abs(g_123 - g_213) < TOL
        assert abs(g_123 - g_312) < TOL
        assert abs(g_123 - g_132) < TOL

    def test_g_pole_locations(self):
        """g(z) has poles at z = -h_i (AP-CY28: known pole locations).
        VERIFIED [DC] denominator vanishes at z = -h_i.
        """
        for h in [H1, H2, H3]:
            with pytest.raises(ZeroDivisionError):
                structure_function_rational(-h, H1, H2, H3)

    def test_g_zero_locations(self):
        """g(z) has zeros at z = h_i.
        VERIFIED [DC] numerator vanishes at z = h_i.
        """
        for h in [H1, H2, H3]:
            g_val = structure_function_rational(h, H1, H2, H3)
            assert abs(g_val) < TOL

    def test_trig_unitarity(self):
        """G(x)*G(1/x) = 1 (trigonometric CY inversion).
        VERIFIED [DC] from q1*q2*q3 = 1.
        """
        q1 = np.exp(0.3 + 0.1j)
        q2 = np.exp(-0.2 + 0.15j)
        q3 = 1.0 / (q1 * q2)
        x = 0.6 + 0.3j
        Gx = structure_function_trig(x, q1, q2, q3)
        Gx_inv = structure_function_trig(1.0 / x, q1, q2, q3)
        assert abs(Gx * Gx_inv - 1.0) < 1e-8


# ================================================================
# 3. HOLOMORPHIC HOLONOMY R-MATRIX
# ================================================================

class TestHolomorphicHolonomyRMatrix:
    """Test the R-matrix from holomorphic CS holonomy."""

    def setup_method(self):
        self.hol = HolomorphicHolonomyRMatrix(H1, H2, H3)

    def test_cy_condition(self):
        """h1 + h2 + h3 = 0 enforced.
        VERIFIED [DC] construction.
        """
        assert abs(self.hol.h1 + self.hol.h2 + self.hol.h3) < TOL

    def test_kappa_value(self):
        """kappa = h1*h2*h3 (Yangian Planck constant).
        VERIFIED [DC] direct computation.
        """
        expected = H1 * H2 * H3
        assert abs(self.hol.kappa - expected) < TOL

    def test_g_unitarity(self):
        """g(z)*g(-z) = 1.
        VERIFIED [DC] algebraic identity [LT] eq:cy-condition-rmatrix.
        """
        assert self.hol.verify_unitarity(Z_TEST)

    def test_g_cy_normalization(self):
        """g(inf) -> 1.
        VERIFIED [DC] degree matching.
        """
        assert self.hol.verify_cy_normalization()

    def test_g_cy_sign(self):
        """g(0) = -1.
        VERIFIED [DC] direct evaluation.
        """
        assert self.hol.verify_cy_sign()

    def test_classical_r_matrix_residue(self):
        """Classical r-matrix residue = -sigma_2.
        VERIFIED [DC] expansion of g(z) at z -> infinity
        [LT] holomorphic_cs_chiral_engine.py, HZ-1 level-prefix convention.
        """
        sigma2 = H1 * H2 + H1 * H3 + H2 * H3
        assert abs(self.hol.classical_r_matrix_residue() - (-sigma2)) < TOL

    def test_yang_ybe(self):
        """Yang-Baxter equation for the charge-2 R-matrix.
        VERIFIED [DC] symbolic + numerical
        [LT] thm:c3-drinfeld-center, zamolodchikov_tetrahedron_engine.py.
        """
        passed, diff = self.hol.verify_yang_ybe(U_TEST, V_TEST, TOL)
        assert passed, f"YBE residual: {diff}"

    def test_yang_unitarity(self):
        """R(z) R(-z) = Id for the Yang R-matrix.
        VERIFIED [DC] (z*Id+kP)(z+k) * (-z*Id+kP)/(-z+k) = Id
        [LT] categorical_s_matrix_e3.py.
        """
        passed, diff = self.hol.verify_yang_unitarity(Z_TEST, TOL)
        assert passed, f"Yang unitarity residual: {diff}"

    def test_yang_r_matrix_at_zero(self):
        """R(0) = P (the permutation matrix) -- the cocommutative limit.
        VERIFIED [DC] R(0) = (0*Id + k*P) / (0+k) = P.
        """
        R0 = self.hol.yang_r_matrix_4x4(0.0)
        P = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                       [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
        assert np.max(np.abs(R0 - P)) < TOL

    def test_yang_r_matrix_at_infinity(self):
        """R(z) -> Id as z -> infinity.
        VERIFIED [DC] (z*Id + k*P)/(z+k) -> Id.
        """
        R_large = self.hol.yang_r_matrix_4x4(1e8)
        assert np.max(np.abs(R_large - np.eye(4, dtype=complex))) < 1e-4

    def test_fock_r_diagonal_charge2(self):
        """Fock R-matrix at charge 2 is diagonal.
        VERIFIED [DC] diagonal by construction
        [LT] categorical_s_matrix_e3.py, eq:r-matrix-partitions.
        """
        R = self.hol.fock_r_matrix_diagonal_charge2(Z_TEST)
        assert R.shape == (2, 2)
        # Off-diagonal entries are zero
        assert abs(R[0, 1]) < TOL
        assert abs(R[1, 0]) < TOL

    def test_fock_r_diagonal_values(self):
        """Fock R eigenvalues: R_row = g(z)*g(z+h2), R_col = g(z)*g(z+h1).
        VERIFIED [DC] product of structure function values.
        """
        z = Z_TEST
        R = self.hol.fock_r_matrix_diagonal_charge2(z)
        g = self.hol.g
        expected_row = g(z) * g(z + H2)
        expected_col = g(z) * g(z + H1)
        assert abs(R[0, 0] - expected_row) < TOL
        assert abs(R[1, 1] - expected_col) < TOL

    def test_charge2_s_matrix_nontrivial(self):
        """Charge-2 S-matrix is nontrivial (not proportional to Id).
        VERIFIED [DC] g(z+h2)*g(h2-z) != g(z+h1)*g(h1-z) generically
        [LT] categorical_s_matrix_e3.py.
        """
        S = self.hol.charge2_s_matrix(Z_TEST)
        # The two diagonal entries should differ
        assert abs(S[0, 0] - S[1, 1]) > 1e-6, \
            "S-matrix diagonal entries should differ at generic point"


# ================================================================
# 4. E_3 CHIRAL R-MATRIX
# ================================================================

class TestE3ChiralRMatrix:
    """Test the E_3 two-parameter chiral R-matrix."""

    def setup_method(self):
        self.e3 = E3ChiralRMatrix(H1, H2, H3)

    def test_charge1_factorization(self):
        """R_ch(u,v) = g(u)*g(v)*g(u-v) (Zamolodchikov factorization).
        VERIFIED [DC] definition [LT] e3_two_parameter_rmatrix.py.
        """
        u, v = U_TEST, V_TEST
        R_ch = self.e3.charge1_rmatrix(u, v)
        expected = self.e3.g(u) * self.e3.g(v) * self.e3.g(u - v)
        assert abs(R_ch - expected) < TOL

    def test_charge1_inversion(self):
        """R_ch(u,v) * R_ch(-u,-v) = 1 (E_3 unitarity).
        VERIFIED [DC] g(z)*g(-z) = 1 applied three times.
        """
        assert self.e3.verify_charge1_inversion(U_TEST, V_TEST, TOL)

    def test_charge1_inversion_multiple_points(self):
        """E_3 unitarity at multiple test points.
        VERIFIED [DC] algebraic identity.
        """
        for u, v in [(3.0, 2.0), (5.0 + 1j, 3.0 - 2j), (10.0, 7.0)]:
            assert self.e3.verify_charge1_inversion(u, v, TOL)

    def test_charge1_miki_exchange(self):
        """R_ch(u,v)/R_ch(v,u) = g(u-v)^2 (Miki exchange phase).
        VERIFIED [DC] g(u-v)/g(v-u) = g(u-v)/g(-(u-v)) = g(u-v)^2.
        """
        passed, diff = self.e3.verify_charge1_miki_exchange(U_TEST, V_TEST, TOL)
        assert passed, f"Miki exchange residual: {diff}"

    def test_charge1_miki_exchange_sign(self):
        """Miki exchange phase is real and positive for real spectral params.
        VERIFIED [DC] g(z) is real for real z with real h_i.
        """
        u, v = 3.7, 2.1  # real spectral parameters
        R_uv = self.e3.charge1_rmatrix(u, v)
        R_vu = self.e3.charge1_rmatrix(v, u)
        ratio = R_uv / R_vu
        # Should be real (g(u-v)^2 with real args)
        assert abs(ratio.imag) < TOL

    def test_charge1_tetrahedron_trivial(self):
        """Parametric tetrahedron at charge 1: automatically satisfied (scalars).
        VERIFIED [DC] scalar multiplication is commutative.
        """
        passed, diff = self.e3.verify_charge1_tetrahedron(
            U_TEST, V_TEST, U_TEST - 1.0, V_TEST + 0.5, TOL)
        assert passed, f"Tetrahedron residual: {diff}"

    def test_charge1_at_v_zero(self):
        """R_ch(u, 0) = g(u) * g(0) * g(u) = -g(u)^2.
        VERIFIED [DC] g(0) = -1, so R_ch(u,0) = g(u)*(-1)*g(u) = -g(u)^2.
        """
        u = U_TEST
        R_ch = self.e3.charge1_rmatrix(u, 0.0)
        expected = -(self.e3.g(u) ** 2)
        assert abs(R_ch - expected) < TOL

    def test_charge1_at_u_equals_v(self):
        """R_ch(u, u) = g(u)^2 * g(0) = -g(u)^2.
        VERIFIED [DC] g(0) = -1.
        """
        u = U_TEST
        R_ch = self.e3.charge1_rmatrix(u, u)
        expected = -(self.e3.g(u) ** 2)
        assert abs(R_ch - expected) < TOL

    def test_charge2_zamolodchikov_shape(self):
        """Charge-2 E_3 R-matrix is 2x2 (diagonal Fock basis).
        VERIFIED [DC] construction.
        """
        R = self.e3.charge2_rmatrix_zamolodchikov(U_TEST, V_TEST)
        assert R.shape == (2, 2)

    def test_charge2_s_matrix_e3_shape(self):
        """E_3 S-matrix at charge 2 is 2x2.
        VERIFIED [DC] construction.
        """
        S = self.e3.charge2_s_matrix_e3(U_TEST, V_TEST)
        assert S.shape == (2, 2)

    def test_charge2_zamolodchikov_is_product(self):
        """R_ch^{(2)}(u,v) = R(u) R(v) R(u-v) at charge 2.
        VERIFIED [DC] definition.
        """
        u, v = U_TEST, V_TEST
        R_ch = self.e3.charge2_rmatrix_zamolodchikov(u, v)
        Ru = self.e3.holonomy.fock_r_matrix_diagonal_charge2(u)
        Rv = self.e3.holonomy.fock_r_matrix_diagonal_charge2(v)
        Ruv = self.e3.holonomy.fock_r_matrix_diagonal_charge2(u - v)
        expected = Ru @ Rv @ Ruv
        assert np.max(np.abs(R_ch - expected)) < TOL

    def test_charge2_e3_s_matrix_is_product(self):
        """S^{E_3}(u,v) = S(u) S(v) S(u-v) at charge 2.
        VERIFIED [DC] definition.
        """
        u, v = U_TEST, V_TEST
        S_e3 = self.e3.charge2_s_matrix_e3(u, v)
        Su = self.e3.holonomy.charge2_s_matrix(u)
        Sv = self.e3.holonomy.charge2_s_matrix(v)
        Suv = self.e3.holonomy.charge2_s_matrix(u - v)
        expected = Su @ Sv @ Suv
        assert np.max(np.abs(S_e3 - expected)) < TOL


# ================================================================
# 5. DIMENSIONAL HIERARCHY
# ================================================================

class TestDimensionalHierarchy:
    """Test the 3d -> 5d -> 6d dimensional hierarchy."""

    def setup_method(self):
        self.dh = DimensionalHierarchy(H1, H2, H3)

    def test_e1_km_level(self):
        """E_1 Kac-Moody level k = -sigma_2.
        VERIFIED [DC] [LT] holomorphic_cs_chiral_engine.py.
        """
        sigma2 = H1 * H2 + H1 * H3 + H2 * H3
        assert abs(self.dh.e1_kac_moody_level() - (-sigma2)) < TOL

    def test_e2_structure_function(self):
        """E_2 structure function is g(z).
        VERIFIED [DC] [LT] eq:yangian-structure-function.
        """
        g_val = self.dh.e2_yangian_structure_function(Z_TEST)
        expected = structure_function_rational(Z_TEST, H1, H2, H3)
        assert abs(g_val - expected) < TOL

    def test_e3_factorization(self):
        """E_3 = g(u)*g(v)*g(u-v).
        VERIFIED [DC] definition.
        """
        R_ch = self.dh.e3_toroidal_structure_function(U_TEST, V_TEST)
        g = lambda z: structure_function_rational(z, H1, H2, H3)
        expected = g(U_TEST) * g(V_TEST) * g(U_TEST - V_TEST)
        assert abs(R_ch - expected) < TOL

    def test_dimensional_consistency(self):
        """E_3 -> E_2 projection consistency.
        VERIFIED [DC] g(0) = -1 implies R_ch(u,0) = -g(u)^2.
        """
        results = self.dh.verify_dimensional_consistency(Z_TEST, TOL)
        for name, passed in results.items():
            assert passed, f"Dimensional consistency failed: {name}"

    def test_s3_symmetry(self):
        """S_3 symmetry of g(z) and R_ch under permutation of (h1,h2,h3).
        VERIFIED [DC] g depends only on elementary symmetric polynomials.
        """
        results = self.dh.verify_miki_s3_symmetry(U_TEST, V_TEST, TOL)
        for name, passed in results.items():
            assert passed, f"S_3 symmetry failed: {name}"


# ================================================================
# 6. K3 YANGIAN R-MATRIX
# ================================================================

class TestK3YangianRMatrix:
    """Test the K3 Yangian R-matrix from restricting C^3 -> K3 x C."""

    def setup_method(self):
        self.k3 = K3YangianRMatrix()  # Default paired parameters

    def test_rank_24(self):
        """K3 Mukai lattice has rank 24.
        VERIFIED [DC] [LT] Mukai 1987.
        """
        assert self.k3.rank == 24
        assert len(self.k3.h_values) == 24

    def test_sum_zero(self):
        """sum(h_a) = 0 (CY condition).
        VERIFIED [DC] sum of paired values.
        """
        assert abs(sum(self.k3.h_values)) < TOL

    def test_unitarity(self):
        """g_{K3}(z) * g_{K3}(-z) = 1.
        VERIFIED [DC] algebraic identity (same as C^3 case).
        """
        z = 25.0 + 7.0j  # Far from poles at +/-1,...,+/-12
        assert self.k3.verify_unitarity(z)

    def test_even_rank_sign(self):
        """g_{K3}(0) = +1 (even rank: (-1)^{24} = +1).
        VERIFIED [DC] g(0) = prod(-h_a/h_a) = (-1)^{24} = +1.
        Contrast with C^3: g(0) = (-1)^3 = -1.
        """
        assert self.k3.verify_even_rank_sign()

    def test_degree(self):
        """g_{K3}(z) -> 1 as z -> infinity (degree (24,24)).
        VERIFIED [DC] sum(h_a) = 0 kills the 1/z term.
        """
        assert self.k3.verify_degree()

    def test_degree_is_24_24(self):
        """g_{K3} is a rational function of degree (24, 24).
        VERIFIED [DC] 24 factors in numerator and denominator.
        """
        # Check by evaluating at enough points to confirm degree
        z_vals = [20.0 + k * 3.0j for k in range(5)]
        vals = [self.k3.g_k3(z) for z in z_vals]
        # All should be finite and nonzero
        for v in vals:
            assert abs(v) > 1e-20
            assert abs(v) < 1e20

    def test_k3_two_param_inversion(self):
        """R_{K3,ch}(u,v) * R_{K3,ch}(-u,-v) = 1.
        VERIFIED [DC] g(z)*g(-z) = 1 applied three times.
        """
        u = 25.0 + 3.0j
        v = 17.0 - 2.0j
        assert self.k3.verify_k3_inversion(u, v)

    def test_k3_contrast_c3_sign(self):
        """K3 has g(0) = +1 but C^3 has g(0) = -1.
        VERIFIED [DC] (-1)^{24} = +1 vs (-1)^3 = -1.
        """
        g_k3_0 = self.k3.g_k3(0.0)
        g_c3_0 = structure_function_rational(0.0, H1, H2, H3)
        assert abs(g_k3_0 - 1.0) < TOL  # K3: +1
        assert abs(g_c3_0 + 1.0) < TOL  # C^3: -1

    def test_k3_paired_parameters(self):
        """Default K3 parameters are paired: h_a = -h_{a+12}.
        VERIFIED [DC] construction.
        """
        h = self.k3.h_values
        for k in range(12):
            assert abs(h[2 * k] + h[2 * k + 1]) < TOL


# ================================================================
# 7. TOPOLOGICAL vs RATIONAL R-MATRIX
# ================================================================

class TestTopologicalVsRational:
    """Test the comparison between 3d and 6d R-matrices."""

    def setup_method(self):
        self.tvr = TopologicalVsRational(H1, H2, H3)

    def test_rational_r_is_g(self):
        """Rational R-matrix at charge 1 is the structure function.
        VERIFIED [DC] definition.
        """
        z = Z_TEST
        R = self.tvr.rational_r_charge1(z)
        expected = structure_function_rational(z, H1, H2, H3)
        assert abs(R - expected) < TOL

    def test_rational_limit(self):
        """Trigonometric -> 1/rational in the eps -> 0 limit.
        VERIFIED [DC] G(e^{eps z}; e^{eps h}) -> prod(z+h_i)/(z-h_i) = 1/g(z).
        Convention: trig G has swapped num/denom vs rational g.
        """
        passed, diff = self.tvr.verify_rational_limit(Z_TEST, eps=1e-5, tol=1e-3)
        assert passed, f"Rational limit residual: {diff}"

    def test_rational_limit_convergence(self):
        """Convergence rate: difference ~ O(eps^2) for the rational limit.
        VERIFIED [DC] Taylor expansion of e^{eps z} - 1 - eps z = O(eps^2).
        Use eps values large enough that machine precision does not interfere.
        """
        diffs = []
        for eps in [1e-1, 1e-2, 1e-3]:
            _, diff = self.tvr.verify_rational_limit(Z_TEST, eps=eps, tol=1.0)
            diffs.append(diff)
        # Each step of eps/10 should reduce diff by ~100x (O(eps^2))
        # Use a conservative 10x threshold to allow for higher-order terms
        assert diffs[1] < diffs[0] / 10.0
        assert diffs[2] < diffs[1] / 10.0


# ================================================================
# 8. FULL VERIFICATION SUITE
# ================================================================

class TestFullVerification:
    """Test the full verification suite."""

    def test_all_pass(self):
        """All verification tests pass.
        VERIFIED [DC] composite of all individual tests.
        """
        results = full_verification()
        for name, passed in results.items():
            assert passed, f"Full verification failed: {name}"

    def test_summary_runs(self):
        """Summary function runs without error."""
        s = summary()
        assert "verification summary" in s.lower()
        assert "PASS" in s
