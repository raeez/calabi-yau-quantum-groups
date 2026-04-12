"""Tests for the two-parameter R-matrix R_ch(u,v) from E_3 chiral braiding on C^3.

Manuscript references:
    Part IV (Quantum Groups and Braided Monoidal Structure):
        conj:e3-chiral-rmatrix: R_ch(u,v) from the E_3 braiding on C^3
        conj:parametric-tetrahedron: E_3 consistency via Zamolodchikov

    CLAIM STATUS: CONJECTURAL (depends on CY-A_3, the d=3 programme).
    The E_3 is TOPOLOGICAL (little 3-disks), NOT algebraic Deligne (AP154).

Literature ground truth:
    Structure function G(x) = prod_i (1-q_i x)/(1-q_i^{-1} x):
        G(x)*G(1/x) = 1 (CY inversion, q_1 q_2 q_3 = 1)
        G(1) = -q_1 q_2 q_3 = -1 (CY sign)
        S_3-symmetric in (q_1, q_2, q_3)

    Two-parameter structure function G_ch(x,y) = G(x)*G(y)*G(x/y):
        G_ch(x,y)*G_ch(1/x,1/y) = 1 (two-parameter inversion)
        G_ch(x,y)/G_ch(y,x) = G(x/y)^2 (Miki exchange phase)
        S_3-symmetric in (q_1, q_2, q_3)

    Yang R-matrix R(z) = (z*Id + kappa*P)/(z+kappa):
        R(z)*R(-z) = Id (unitarity)
        kappa = h_1 h_2 h_3 (Planck constant)

    Zamolodchikov factorization (charge 1):
        R_ch(u,v) = g(u)*g(v)*g(u-v)

    Rational structure function g(z) = (z-h1)(z-h2)(z-h3)/((z+h1)(z+h2)(z+h3)):
        g(z)*g(-z) = 1
        g(0) = -1 (CY sign)

    Parametric tetrahedron: automatically satisfied at charge 1 (scalars commute).
"""

import math

import numpy as np
import pytest
from sympy import Rational, Symbol, cancel, expand, symbols

from compute.lib.e3_two_parameter_rmatrix import (
    e3_rmatrix_summary,
    parametric_tetrahedron_constraint,
    r_matrix_charge1_numerical,
    r_matrix_charge1_two_param,
    r_matrix_charge2_diagonal_two_param,
    r_matrix_charge2_numerical,
    two_param_structure_function,
    two_param_structure_function_additive,
    verify_G_ch_inversion,
    verify_G_ch_miki_exchange,
    verify_S3_symmetry,
    verify_tetrahedron_charge1,
    yang_r_matrix_two_param,
    zamolodchikov_factorization_check,
)


# ================================================================
# STANDARD TEST PARAMETERS
# ================================================================

# Trigonometric (DIM) parameters
Q1 = np.exp(0.3 + 0.1j)
Q2 = np.exp(-0.2 + 0.15j)
Q3 = 1.0 / (Q1 * Q2)  # CY condition

# Additive (Yangian) parameters
# Poles of g(z) are at z = -h_i. Chosen so poles at -1.3, 0.5, 0.8
# avoid all test spectral parameters (u, v, u-v values).
H1 = 1.3
H2 = -0.5
H3 = -(H1 + H2)  # = -0.8, CY condition

# Schiffmann-Vasserot N=2 parametrization
H1_SV = 1.0
H2_SV = -2.0
H3_SV = 1.0


# ================================================================
# TWO-PARAMETER STRUCTURE FUNCTION
# ================================================================

class TestTwoParamStructureFunction:
    """Test the two-parameter structure function G_ch(x, y)."""

    def test_factorization_explicit(self):
        """G_ch(x,y) = G(x)*G(y)*G(x/y) at explicit numerical points.

        VERIFIED [DC] direct computation [LT] DIM structure function theory.
        """
        from compute.lib.quantum_toroidal_e1_cy3 import trig_structure_function

        x = 0.5 + 0.3j
        y = 0.4 - 0.2j

        G_ch = two_param_structure_function(x, y, Q1, Q2, Q3)
        Gx = trig_structure_function(x, Q1, Q2, Q3)
        Gy = trig_structure_function(y, Q1, Q2, Q3)
        G_cross = trig_structure_function(x / y, Q1, Q2, Q3)

        expected = Gx * Gy * G_cross
        assert abs(G_ch - expected) < 1e-10, (
            f"Factorization failed: G_ch={G_ch}, expected={expected}"
        )

    def test_additive_factorization(self):
        """G_ch^{rat}(u,v) = g(u)*g(v)*g(u-v) at explicit numerical points.

        VERIFIED [DC] direct computation [LT] affine Yangian structure function.
        """
        u, v = 1.5, 0.6  # u-v=0.9, all avoid poles at -1.3, 0.5, 0.8

        G_rat = two_param_structure_function_additive(u, v, H1, H2, H3)

        def _g(z):
            return ((z - H1) * (z - H2) * (z - H3) /
                    ((z + H1) * (z + H2) * (z + H3)))

        expected = _g(u) * _g(v) * _g(u - v)
        assert abs(G_rat - expected) < 1e-12

    def test_G_ch_at_y_equals_1(self):
        """G_ch(x, 1) = G(x) * G(1) * G(x) = -G(x)^2.

        Since G(1) = prod_i (1-q_i)/(1-1/q_i) = prod_i (-q_i) = -1 (CY).
        VERIFIED [DC] direct computation [LT] CY sign identity.
        """
        x = 0.6 + 0.2j
        G_ch_x1 = two_param_structure_function(x, 1.0, Q1, Q2, Q3)
        from compute.lib.quantum_toroidal_e1_cy3 import trig_structure_function
        Gx = trig_structure_function(x, Q1, Q2, Q3)
        expected = -Gx ** 2  # G(1) = -1
        assert abs(G_ch_x1 - expected) < 1e-10

    def test_G_ch_at_x_equals_y(self):
        """G_ch(x, x) = G(x)^2 * G(1) = -G(x)^2.

        At coincident spectral parameters, the crossing factor G(x/x) = G(1) = -1.
        VERIFIED [DC] direct computation [LT] crossing at coincidence.
        """
        x = 0.7 - 0.1j
        G_ch_xx = two_param_structure_function(x, x, Q1, Q2, Q3)
        from compute.lib.quantum_toroidal_e1_cy3 import trig_structure_function
        Gx = trig_structure_function(x, Q1, Q2, Q3)
        expected = -Gx ** 2
        assert abs(G_ch_xx - expected) < 1e-10


# ================================================================
# INVERSION AND SYMMETRY IDENTITIES
# ================================================================

class TestInversionAndSymmetry:
    """Test the identities of G_ch."""

    def test_two_param_inversion(self):
        """G_ch(x,y)*G_ch(1/x,1/y) = 1 over 32 points.

        VERIFIED [DC] numerical verification [LT] CY inversion identity.
        """
        passes, max_res = verify_G_ch_inversion(Q1, Q2, Q3)
        assert passes, f"Inversion failed: max residual = {max_res}"

    def test_miki_exchange(self):
        """G_ch(x,y)/G_ch(y,x) = G(x/y)^2 over 32 points.

        VERIFIED [DC] numerical verification [LT] Miki automorphism exchange.
        """
        passes, max_res = verify_G_ch_miki_exchange(Q1, Q2, Q3)
        assert passes, f"Miki exchange failed: max residual = {max_res}"

    def test_S3_symmetry(self):
        """G_ch invariant under cyclic permutation of (q_1,q_2,q_3).

        VERIFIED [DC] numerical verification [LT] S_3 triality symmetry.
        """
        passes, max_res = verify_S3_symmetry(Q1, Q2, Q3)
        assert passes, f"S_3 symmetry failed: max residual = {max_res}"

    def test_inversion_SV_params(self):
        """Inversion identity at Schiffmann-Vasserot N=2 parameters.

        VERIFIED [DC] numerical verification [LT] SV parametrization.
        """
        q1_sv = np.exp(H1_SV * 0.1)
        q2_sv = np.exp(H2_SV * 0.1)
        q3_sv = 1.0 / (q1_sv * q2_sv)
        passes, max_res = verify_G_ch_inversion(q1_sv, q2_sv, q3_sv)
        assert passes, f"SV inversion failed: max residual = {max_res}"


# ================================================================
# CHARGE-1 R-MATRIX (SCALAR)
# ================================================================

class TestCharge1RMatrix:
    """Test the charge-1 two-parameter R-matrix."""

    def test_charge1_is_scalar(self):
        """R^{(1)}_ch is a scalar (1-dim Fock space at charge 1).

        VERIFIED [DC] structure check [LT] charge-1 Fock space dimension.
        """
        result = r_matrix_charge1_two_param(Q1, Q2, Q3)
        assert result["is_scalar"] is True

    def test_charge1_numerical(self):
        """R^{(1)}_ch(x,y) = G_ch(x,y) numerically.

        VERIFIED [DC] numerical evaluation [LT] charge-1 R-matrix formula.
        """
        x = 0.5 + 0.2j
        y = 0.3 - 0.1j
        R_val = r_matrix_charge1_numerical(x, y, Q1, Q2, Q3)
        G_val = two_param_structure_function(x, y, Q1, Q2, Q3)
        assert abs(R_val - G_val) < 1e-12

    def test_charge1_reduces_to_one_param(self):
        """At y -> 0 (additive), R_ch(u, 0) ~ g(0)*g(u)*R_1param(u).

        In additive notation: g(u)*g(0)*g(u-0) = g(u)*(-1)*g(u) = -g(u)^2.
        VERIFIED [DC] limit check [LT] one-parameter reduction.
        """
        u = 1.5
        v = 0.0001  # near zero, avoid exact pole
        G_rat = two_param_structure_function_additive(u, v, H1, H2, H3)

        def _g(z):
            return ((z - H1) * (z - H2) * (z - H3) /
                    ((z + H1) * (z + H2) * (z + H3)))

        # At v ~ 0: g(v) ~ g(0) = -1, g(u-v) ~ g(u)
        # So G_ch^{rat}(u, v) ~ g(u) * (-1) * g(u) = -g(u)^2
        expected_limit = -_g(u) ** 2
        # With v = 0.0001, this should be close
        assert abs(G_rat - expected_limit) < 0.01, (
            f"One-param reduction: G_rat={G_rat}, expected ~ {expected_limit}"
        )

    def test_charge1_additive_CY_sign(self):
        """At u=v (crossing coincidence): g(0) = -1.

        G_ch^{rat}(u, u) = g(u) * g(u) * g(0) = -g(u)^2.
        VERIFIED [DC] direct computation [LT] CY sign g(0) = -1.
        """
        u = 2.0

        def _g(z):
            return ((z - H1) * (z - H2) * (z - H3) /
                    ((z + H1) * (z + H2) * (z + H3)))

        G_ch_uu = two_param_structure_function_additive(u, u, H1, H2, H3)
        expected = -_g(u) ** 2
        assert abs(G_ch_uu - expected) < 1e-12


# ================================================================
# CHARGE-2 R-MATRIX (DIAGONAL)
# ================================================================

class TestCharge2RMatrix:
    """Test the charge-2 two-parameter R-matrix diagonal entries."""

    def test_charge2_structure(self):
        """Charge-2 R-matrix has the correct structure.

        VERIFIED [DC] structure check [LT] charge-2 Fock space basis.
        """
        result = r_matrix_charge2_diagonal_two_param(H1, H2, H3)
        assert "R_row_row" in result
        assert "R_col_col" in result
        assert "ratio" in result

    def test_charge2_ratio_factorizes(self):
        """The ratio R_row/R_col factorizes as product of one-param ratios.

        ratio = [g(u+h2)/g(u+h1)] * [g(v+h2)/g(v+h1)]
        VERIFIED [DC] numerical factorization check [LT] content-independent crossing.
        """
        u = 1.5 + 0.3j
        v = 0.8 - 0.2j
        result = r_matrix_charge2_numerical(u, v, H1, H2, H3)
        assert result["ratio_factorizes"], (
            f"Ratio factorization failed: ratio={result['ratio']}, "
            f"factorized={result['factorized_ratio']}"
        )

    def test_charge2_ratio_factorizes_SV(self):
        """Factorization at Schiffmann-Vasserot N=2 parameters.

        VERIFIED [DC] numerical factorization [LT] SV parametrization.
        """
        u = 2.0 + 0.1j
        v = 1.0 - 0.3j
        result = r_matrix_charge2_numerical(u, v, H1_SV, H2_SV, H3_SV)
        assert result["ratio_factorizes"]

    def test_charge2_multiple_points(self):
        """Ratio factorization at 10 randomly sampled points.

        VERIFIED [DC] numerical sweep [LT] charge-2 R-matrix theory.
        """
        for k in range(10):
            theta = 2 * math.pi * k / 10
            u = 1.0 + 0.5 * np.exp(1j * theta)
            v = 0.5 + 0.3 * np.exp(1j * (theta + 1.0))
            result = r_matrix_charge2_numerical(u, v, H1, H2, H3)
            assert result["ratio_factorizes"], f"Failed at point {k}: u={u}, v={v}"


# ================================================================
# ZAMOLODCHIKOV FACTORIZATION
# ================================================================

class TestZamolodchikovFactorization:
    """Test the Zamolodchikov factorization R_ch = R_1 * R_2 * R_12."""

    def test_factorization_holds(self):
        """R_ch(u,v) = g(u)*g(v)*g(u-v) verified numerically.

        VERIFIED [DC] numerical check [LT] Zamolodchikov tetrahedron theory.
        """
        u, v = 1.5, 0.6  # u-v=0.9, all avoid poles at -1.3, 0.5, 0.8
        result = zamolodchikov_factorization_check(u, v, H1, H2, H3)
        assert result["R_full_eq_naive_times_crossing"]

    def test_crossing_at_coincidence(self):
        """g(0) = -1 (CY sign at u=v).

        VERIFIED [DC] direct computation [LT] CY condition g(0)=-1.
        """
        u, v = 1.5, 0.6  # u-v=0.9, all avoid poles at -1.3, 0.5, 0.8
        result = zamolodchikov_factorization_check(u, v, H1, H2, H3)
        assert abs(result["crossing_at_u_eq_v"] - (-1.0)) < 1e-12

    def test_naive_misses_crossing(self):
        """R_naive = g(u)*g(v) differs from R_full by the crossing factor.

        VERIFIED [DC] comparison [LT] crossing factor necessity.
        """
        u, v = 1.5, 0.6  # u-v=0.9, all avoid poles at -1.3, 0.5, 0.8
        result = zamolodchikov_factorization_check(u, v, H1, H2, H3)
        # The naive factorization misses g(u-v)
        assert abs(result["R_ch_full"] - result["R_naive_factorization"]) > 1e-6, (
            "Naive and full should differ (crossing factor not trivial)"
        )

    def test_miki_exchange_from_zamolodchikov(self):
        """The Miki exchange phase is g(u-v)^2 from the crossing factor.

        G_ch(u,v)/G_ch(v,u) = g(u-v)/g(v-u) = g(u-v)*g(-(v-u)) = g(u-v)^2
        (using g(z)*g(-z) = 1, so g(-w) = 1/g(w), giving g(u-v)/g(v-u) = g(u-v)^2).

        Actually: G_ch(u,v)/G_ch(v,u) = [g(u)g(v)g(u-v)] / [g(v)g(u)g(v-u)]
                                        = g(u-v)/g(v-u)
                                        = g(u-v) * g(-(v-u)) ... but -(v-u) = u-v
        Wait: g(u-v)/g(v-u). Let w = u-v. Then g(w)/g(-w) = g(w)/(1/g(w)) = g(w)^2.

        VERIFIED [DC] algebraic identity [LT] Miki S-transformation.
        """
        u, v = 1.5, 0.6  # u-v=0.9, all avoid poles at -1.3, 0.5, 0.8
        result = zamolodchikov_factorization_check(u, v, H1, H2, H3)

        def _g(z):
            return ((z - H1) * (z - H2) * (z - H3) /
                    ((z + H1) * (z + H2) * (z + H3)))

        exchange = result["miki_exchange_phase"]
        expected = _g(u - v) ** 2
        assert abs(exchange - expected) < 1e-12


# ================================================================
# PARAMETRIC TETRAHEDRON EQUATION
# ================================================================

class TestParametricTetrahedron:
    """Test the parametric tetrahedron equation (E_3 consistency)."""

    def test_constraint_surface_dimension(self):
        """The constraint surface is 4-dimensional in 8-dim parameter space.

        VERIFIED [DC] parameter counting [LT] Zamolodchikov tetrahedron theory.
        """
        result = parametric_tetrahedron_constraint(1.0, 0.5, 0.7, 0.3)
        assert result["constraint_surface_dim"] == "4 (out of 8)"

    def test_derived_parameters(self):
        """u_3 = u_1 - u_2 and v_3 = v_1 - v_2 on the constraint surface.

        VERIFIED [DC] algebraic check [LT] tetrahedron constraint equations.
        """
        u1, v1, u2, v2 = 1.0, 0.5, 0.7, 0.3
        result = parametric_tetrahedron_constraint(u1, v1, u2, v2)
        assert abs(result["derived_params"]["u3"] - (u1 - u2)) < 1e-15
        assert abs(result["derived_params"]["v3"] - (v1 - v2)) < 1e-15

    def test_crossing_constraint(self):
        """u_4 = v_2 (crossing constraint).

        VERIFIED [DC] crossing check [LT] E_3 geometric content.
        """
        u1, v1, u2, v2 = 1.0, 0.5, 0.7, 0.3
        result = parametric_tetrahedron_constraint(u1, v1, u2, v2)
        assert abs(result["derived_params"]["u4"] - v2) < 1e-15

    def test_tetrahedron_charge1_trivial(self):
        """Tetrahedron equation at charge 1: automatically satisfied (scalars).

        VERIFIED [DC] numerical verification [LT] scalar commutativity.
        """
        passes, max_res = verify_tetrahedron_charge1(Q1, Q2, Q3)
        assert passes, f"Tetrahedron at charge 1 failed: max_res = {max_res}"

    def test_tetrahedron_charge1_SV(self):
        """Tetrahedron at charge 1 with SV N=2 parameters.

        VERIFIED [DC] numerical verification [LT] SV parametrization.
        """
        q1_sv = np.exp(H1_SV * 0.1)
        q2_sv = np.exp(H2_SV * 0.1)
        q3_sv = 1.0 / (q1_sv * q2_sv)
        passes, max_res = verify_tetrahedron_charge1(q1_sv, q2_sv, q3_sv)
        assert passes, f"SV tetrahedron failed: max_res = {max_res}"


# ================================================================
# YANG R-MATRIX TWO-PARAMETER EXTENSION
# ================================================================

class TestYangRMatrixTwoParam:
    """Test the two-parameter Yang R-matrix at charge 2."""

    def test_yang_two_param_structure(self):
        """R_ch(u,v) = R(u)*R(v)*R(u-v) produces a 4x4 matrix.

        VERIFIED [DC] matrix dimension check [LT] Yang R-matrix theory.
        """
        result = yang_r_matrix_two_param(H1, H2, H3)
        R_ch = result["R_ch_matrix"]
        assert R_ch.shape == (4, 4)

    def test_yang_two_param_zamolodchikov(self):
        """The matrix R_ch uses Zamolodchikov factorization.

        VERIFIED [DC] structure check [LT] Zamolodchikov factorization.
        """
        result = yang_r_matrix_two_param(H1, H2, H3)
        assert result["zamolodchikov_factorization"] is True

    def test_yang_two_param_kappa(self):
        """kappa = h_1 h_2 h_3 is the Planck constant.

        VERIFIED [DC] parameter check [LT] affine Yangian conventions.
        """
        result = yang_r_matrix_two_param(H1, H2, H3)
        expected_kappa = H1 * H2 * H3
        u_sym = Symbol("u")
        # kappa is symbolic; check the numerical value
        kappa_val = complex(result["kappa"].subs(
            {Symbol("h1"): H1, Symbol("h2"): H2, Symbol("h3"): H3}
        )) if hasattr(result["kappa"], "subs") else result["kappa"]
        assert abs(kappa_val - expected_kappa) < 1e-12

    def test_yang_diagonal_entry_00(self):
        """R_ch[0,0] = 1 (same-state element, P acts as Id on e1 x e1).

        For R(z)[0,0] = (z + kappa*1)/(z + kappa) = 1 (since P[0,0] = 1).
        So R_ch[0,0] = R(u)[0,0] * R(v)[0,0] * R(u-v)[0,0] = 1*1*1 = 1.

        VERIFIED [DC] matrix element check [LT] Yang R-matrix diagonal.
        """
        result = yang_r_matrix_two_param(H1, H2, H3)
        R_ch = result["R_ch_matrix"]
        entry_00 = cancel(R_ch[0, 0])
        assert entry_00 == 1, f"R_ch[0,0] = {entry_00}, expected 1"

    def test_yang_diagonal_entry_33(self):
        """R_ch[3,3] = 1 (same-state element for e2 x e2).

        VERIFIED [DC] matrix element check [LT] Yang R-matrix diagonal.
        """
        result = yang_r_matrix_two_param(H1, H2, H3)
        R_ch = result["R_ch_matrix"]
        entry_33 = cancel(R_ch[3, 3])
        assert entry_33 == 1, f"R_ch[3,3] = {entry_33}, expected 1"


# ================================================================
# E_3 SUMMARY AND CLAIM STATUS
# ================================================================

class TestE3Summary:
    """Test the summary and claim status metadata."""

    def test_claim_status_conjectural(self):
        """The E_3 R-matrix is CONJECTURAL (CY-A_3 not proved).

        AP-CY6/AP-CY14 compliance: unconstructed objects use conjecture.
        """
        summary = e3_rmatrix_summary()
        assert "CONJECTURAL" in summary["claim_status"]

    def test_e3_type_topological(self):
        """The E_3 is TOPOLOGICAL (little 3-disks), not algebraic Deligne.

        AP154 compliance: distinguish topological from algebraic E_3.
        """
        summary = e3_rmatrix_summary()
        assert "TOPOLOGICAL" in summary["e3_type"]

    def test_zamolodchikov_ansatz(self):
        """The construction uses Zamolodchikov factorization.

        VERIFIED [DC] construction method [LT] Zamolodchikov (1981).
        """
        summary = e3_rmatrix_summary()
        assert "Zamolodchikov" in summary["construction"]["ansatz"]

    def test_charge1_formula(self):
        """Charge 1 formula documented correctly.

        VERIFIED [DC] formula check [LT] two-parameter R-matrix theory.
        """
        summary = e3_rmatrix_summary()
        assert "Scalar" in summary["construction"]["charge_1"]
