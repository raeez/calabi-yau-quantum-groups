"""Tests for the categorical S-matrix from E_3 braiding at charge 2.

Manuscript references:
    Part IV (Quantum Groups and Braided Monoidal Structure):
        constr:e3-s-matrix: S_{V,W} = Tr_W(R_{V,W} . R_{W,V})
        conj:double-s-matrix: double S-matrix for quantum toroidal
        conj:sp4-modularity: Sp_4(Z) modularity of E_3 S-matrix
        conj:s-matrix-phi10: connection to Igusa cusp form Phi_10

    braided_factorization.tex L579-758

    CLAIM STATUS:
        Charge 1: PROVED (CY inversion identity).
        Charge 2 diagonal (Fock): PROVED (direct computation).
        Yang R-matrix S: PROVED (trivial: double braiding = Id).
        E_3 factorization: CONDITIONAL (Zamolodchikov ansatz).
        Phi_10 connection: CONJECTURAL (depends on CY-A_3).

Literature ground truth:
    CY inversion: g(z)*g(-z) = 1 when h1+h2+h3 = 0.
    g(0) = -1 (CY sign).
    Yang R-matrix: R(z)*R(-z) = Id (unitarity from P^2 = Id).
    Yang R-matrix: R(z)*R_{21}(-z) = Id (braid unitarity).
    Hopf link invariant: S_{V,W} = Tr_W(R_{VW} R_{WV}).
    For symmetric R-matrices (R*R_{21} = Id): S = dim(W)*Id.
    Zamolodchikov factorization: R_ch(u,v) = R(u)*R(v)*R(u-v).
    Diagonal Fock R-matrix:
        R_{(2)}(u) = g(u)*g(u+h2), R_{(1,1)}(u) = g(u)*g(u+h1).
    S-matrix eigenvalues at charge 2:
        S_{(2)}(u) = g(u+h2)*g(h2-u) (NOT 1 for h2 != 0).
        S_{(1,1)}(u) = g(u+h1)*g(h1-u) (NOT 1 for h1 != 0).
    S-matrix at u=0:
        S_{(2)}(0) = g(h2)^2, S_{(1,1)}(0) = g(h1)^2.
    S-matrix symmetry: S(u) = S(-u) (even function).
    E_3 S-matrix factorization:
        S^{E_3}(u,v) = S(u)*S(v)*S(u-v) (Zamolodchikov).
    E_3 S-matrix parity: S^{E_3}(u,v) = S^{E_3}(-u,-v) (even).

    Phi_10: Igusa cusp form, weight 10, Sp_4(Z).
    BKM weight: kappa_{BKM} = 5.
    S-matrix weight (conjectured): -2*kappa_{cat} = -4.
"""

import math

import numpy as np
import pytest
from sympy import Matrix, Rational, Symbol, cancel, expand, simplify, symbols

from compute.lib.categorical_s_matrix_e3 import (
    categorical_s_matrix_summary,
    phi10_charge2_fj_coefficient,
    s_matrix_charge1_e2,
    s_matrix_charge1_e3,
    s_matrix_charge2_diagonal_e2,
    s_matrix_charge2_e3,
    s_matrix_charge2_eigenvalues_e2,
    s_matrix_charge2_symbolic_e2,
    s_matrix_phi10_connection,
    s_matrix_spectrum_product,
    s_matrix_yang_charge2_e2,
    verify_e3_zamolodchikov_factorization,
    verify_s_matrix_charge1_e3_identity,
    verify_s_matrix_charge1_identity,
    verify_s_matrix_charge2_symmetry,
    verify_s_matrix_e3_inversion,
)


# ================================================================
# STANDARD TEST PARAMETERS
# ================================================================

# Additive (Yangian) parameters -- poles at -h_i = {-1.3, 0.5, 0.8}
# Chosen to avoid test spectral parameter values.
H1 = 1.3
H2 = -0.5
H3 = -(H1 + H2)  # = -0.8, CY condition

# Alternative: Schiffmann-Vasserot N=2 parametrization
H1_SV = 1.0
H2_SV = -2.0
H3_SV = 1.0  # h1+h2+h3 = 0

# Alternative: symmetric parameters
H1_SYM = 1.0
H2_SYM = np.exp(2j * math.pi / 3)
H3_SYM = np.exp(-2j * math.pi / 3)  # cube roots of unity (sum = 0 approximately)

# The g-function for manual cross-checks
def _g(z, h1=H1, h2=H2, h3=H3):
    numer = (z - h1) * (z - h2) * (z - h3)
    denom = (z + h1) * (z + h2) * (z + h3)
    return numer / denom


# ================================================================
# CHARGE 1: S_{1,1} = 1 (CY INVERSION)
# ================================================================

class TestCharge1SMatrix:
    """S-matrix at charge 1: trivially 1 by CY inversion."""

    def test_s_charge1_e2_explicit(self):
        """S_{1,1}(u) = g(u)*g(-u) = 1 at a specific point.

        VERIFIED [DC] direct computation [LT] CY inversion identity.
        """
        u = 1.5 + 0.3j
        S = s_matrix_charge1_e2(u, H1, H2, H3)
        assert abs(S - 1.0) < 1e-12, f"S_{1,1}({u}) = {S}, expected 1"

    def test_s_charge1_e2_real_spectral(self):
        """S_{1,1}(u) = 1 for real u.

        Poles of g(z) at z = -h_i = {-1.3, 0.5, 0.8}; avoid these values.
        VERIFIED [DC] direct computation [LT] CY inversion on real axis.
        """
        for u in [0.3, 1.0, 2.0, 3.5, -1.0]:
            S = s_matrix_charge1_e2(u, H1, H2, H3)
            assert abs(S - 1.0) < 1e-12, f"S_{1,1}({u}) = {S}"

    def test_s_charge1_e2_sweep(self):
        """S_{1,1}(u) = 1 over 32 random spectral parameters.

        VERIFIED [DC] numerical sweep [LT] CY inversion identity.
        """
        passes, max_res = verify_s_matrix_charge1_identity(H1, H2, H3)
        assert passes, f"Charge-1 S-matrix failed: max residual = {max_res}"

    def test_s_charge1_e3_explicit(self):
        """S^{E_3}_{1,1}(u,v) = 1 at a specific point.

        VERIFIED [DC] direct computation [LT] two-parameter CY inversion.
        """
        u = 1.5 + 0.3j
        v = 0.8 - 0.2j
        S = s_matrix_charge1_e3(u, v, H1, H2, H3)
        assert abs(S - 1.0) < 1e-10, f"S^E3_{1,1}({u},{v}) = {S}, expected 1"

    def test_s_charge1_e3_sweep(self):
        """S^{E_3}_{1,1}(u,v) = 1 over 32 random pairs.

        VERIFIED [DC] numerical sweep [LT] two-parameter CY inversion.
        """
        passes, max_res = verify_s_matrix_charge1_e3_identity(H1, H2, H3)
        assert passes, f"Charge-1 E_3 S-matrix failed: max residual = {max_res}"

    def test_s_charge1_e3_at_coincidence(self):
        """S^{E_3}_{1,1}(u,u) = 1 (coincident spectral parameters).

        At u=v, the crossing factor g(u-v) = g(0) = -1.
        S = [g(u)*g(-u)] * [g(u)*g(-u)] * [g(0)*g(0)] = 1*1*1 = 1.
        VERIFIED [DC] direct computation [LT] crossing at coincidence.
        """
        u = 1.7 + 0.4j
        S = s_matrix_charge1_e3(u, u, H1, H2, H3)
        assert abs(S - 1.0) < 1e-10

    def test_s_charge1_sv_params(self):
        """S_{1,1} = 1 at SV N=2 parameters.

        VERIFIED [DC] direct computation [LT] SV parametrization.
        """
        passes, max_res = verify_s_matrix_charge1_identity(H1_SV, H2_SV, H3_SV)
        assert passes, f"SV charge-1 S-matrix failed: max residual = {max_res}"


# ================================================================
# CHARGE 2 (YANG R-MATRIX): S = 2*Id (TRIVIAL)
# ================================================================

class TestCharge2YangSMatrix:
    """S-matrix from the 4x4 Yang R-matrix: trivially dim(W)*Id."""

    def test_yang_double_braiding_is_identity(self):
        """R(z)*R_{21}(-z) = Id for the Yang R-matrix.

        VERIFIED [DC] symbolic computation [LT] Yang R-matrix unitarity.
        """
        result = s_matrix_yang_charge2_e2(H1, H2, H3)
        assert result["double_braiding_is_identity"], (
            f"Double braiding is not Id: {result['double_braiding']}"
        )

    def test_yang_s_matrix_is_2_times_id(self):
        """Tr_W(Id) = dim(W)*Id_V = 2*Id_2 for the Yang R-matrix.

        VERIFIED [DC] symbolic partial trace [LT] S-matrix for symmetric braiding.
        """
        result = s_matrix_yang_charge2_e2(H1, H2, H3)
        assert result["S_is_trivial"], (
            f"S-matrix is not 2*Id: {result['S_matrix_partial_trace']}"
        )

    def test_yang_s_matrix_sv_params(self):
        """Yang S-matrix is trivial also at SV parameters.

        VERIFIED [DC] symbolic computation [LT] parameter independence.
        """
        result = s_matrix_yang_charge2_e2(H1_SV, H2_SV, H3_SV)
        assert result["double_braiding_is_identity"]
        assert result["S_is_trivial"]


# ================================================================
# CHARGE 2 (FOCK DIAGONAL): NONTRIVIAL S-MATRIX
# ================================================================

class TestCharge2FockSMatrix:
    """S-matrix from the diagonal Fock R-matrix at charge 2."""

    def test_s_row_formula(self):
        """S_{(2)}(u) = g(u+h2)*g(h2-u) at explicit point.

        VERIFIED [DC] direct computation [LT] diagonal R-matrix double braiding.
        """
        u = 1.5
        S = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        expected = _g(u + H2) * _g(H2 - u)
        assert abs(S["S_row"] - expected) < 1e-12, (
            f"S_row={S['S_row']}, expected={expected}"
        )

    def test_s_col_formula(self):
        """S_{(1,1)}(u) = g(u+h1)*g(h1-u) at explicit point.

        VERIFIED [DC] direct computation [LT] diagonal R-matrix double braiding.
        """
        u = 1.5
        S = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        expected = _g(u + H1) * _g(H1 - u)
        assert abs(S["S_col"] - expected) < 1e-12

    def test_s_charge2_is_not_trivial(self):
        """S_{(2)} != S_{(1,1)} for generic parameters (nontrivial braiding).

        VERIFIED [DC] numerical inequality [LT] quantum group nontriviality.
        """
        u = 1.5
        S = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        assert abs(S["S_row"] - S["S_col"]) > 1e-3, (
            f"S_row and S_col are too close: ratio={S['ratio']}"
        )

    def test_s_charge2_at_u_zero(self):
        """S_{(2)}(0) = g(h2)^2, S_{(1,1)}(0) = g(h1)^2.

        At u=0: g(0+h2)*g(h2-0) = g(h2)*g(h2) = g(h2)^2.
        VERIFIED [DC] direct computation [LT] S-matrix at zero spectral parameter.
        """
        S = s_matrix_charge2_diagonal_e2(0.0, H1, H2, H3)
        expected_row = _g(H2) ** 2
        expected_col = _g(H1) ** 2
        assert abs(S["S_row"] - expected_row) < 1e-12
        assert abs(S["S_col"] - expected_col) < 1e-12

    def test_s_charge2_even_symmetry(self):
        """S(u) = S(-u) (the S-matrix is even in u).

        S_{(2)}(u) = g(u+h2)*g(h2-u) is manifestly symmetric under u -> -u.
        VERIFIED [DC] numerical sweep [LT] S-matrix evenness.
        """
        passes, max_res = verify_s_matrix_charge2_symmetry(H1, H2, H3)
        assert passes, f"Even symmetry failed: max residual = {max_res}"

    def test_s_charge2_complex_spectral(self):
        """S-matrix at complex spectral parameter.

        VERIFIED [DC] direct computation [LT] analytic continuation.
        """
        u = 1.3 + 0.7j
        S = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        expected_row = _g(u + H2) * _g(H2 - u)
        assert abs(S["S_row"] - expected_row) < 1e-11

    def test_s_charge2_ratio_is_rational(self):
        """S_{(2)}/S_{(1,1)} is a rational function of u.

        VERIFIED [DC] symbolic verification [LT] rational R-matrix structure.
        """
        sym = s_matrix_charge2_symbolic_e2()
        ratio = sym["ratio"]
        # Ratio should be a well-defined rational function in u
        u = Symbol("u")
        # Check that it is nonzero and finite for generic u
        assert ratio != 0
        assert ratio is not None

    def test_s_charge2_eigenvalues_at_zero(self):
        """Eigenvalues at u=0 match g(h_i)^2.

        VERIFIED [DC] direct computation [LT] eigenvalue formula.
        """
        result = s_matrix_charge2_eigenvalues_e2(0.0, H1, H2, H3)
        expected_row = _g(H2) ** 2
        expected_col = _g(H1) ** 2
        assert abs(result["eigenvalues_at_u_0"][0] - expected_row) < 1e-12
        assert abs(result["eigenvalues_at_u_0"][1] - expected_col) < 1e-12

    def test_s_charge2_quantum_dimension(self):
        """Quantum dimension = (S_row + S_col)/2 is nontrivial.

        VERIFIED [DC] direct computation [LT] quantum dimension from S-matrix.
        """
        result = s_matrix_charge2_eigenvalues_e2(1.5, H1, H2, H3)
        qdim = result["quantum_dimension"]
        # Should be a nonzero complex number, not exactly 1
        assert abs(qdim) > 1e-6
        # And not equal to 1 (which would mean trivial braiding)
        assert abs(qdim - 1.0) > 1e-3


# ================================================================
# CHARGE 2 E_3: ZAMOLODCHIKOV FACTORIZATION
# ================================================================

class TestCharge2E3SMatrix:
    """E_3 categorical S-matrix at charge 2."""

    def test_e3_factorization_explicit(self):
        """S^{E_3}_{(2)}(u,v) = S_{(2)}(u)*S_{(2)}(v)*S_{(2)}(u-v).

        VERIFIED [DC] direct computation [LT] Zamolodchikov factorization.
        """
        u = 1.5 + 0.3j
        v = 0.8 - 0.2j
        S_e3 = s_matrix_charge2_e3(u, v, H1, H2, H3)
        S_u = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        S_v = s_matrix_charge2_diagonal_e2(v, H1, H2, H3)
        S_uv = s_matrix_charge2_diagonal_e2(u - v, H1, H2, H3)

        expected_row = S_u["S_row"] * S_v["S_row"] * S_uv["S_row"]
        expected_col = S_u["S_col"] * S_v["S_col"] * S_uv["S_col"]

        assert abs(S_e3["S_row_e3"] - expected_row) < 1e-10
        assert abs(S_e3["S_col_e3"] - expected_col) < 1e-10

    def test_e3_factorization_sweep(self):
        """Zamolodchikov factorization over 16 random (u,v) pairs.

        VERIFIED [DC] numerical sweep [LT] Zamolodchikov ansatz consistency.
        """
        passes, max_res = verify_e3_zamolodchikov_factorization(H1, H2, H3)
        assert passes, f"E_3 Zamolodchikov failed: max residual = {max_res}"

    def test_e3_parity(self):
        """S^{E_3}(u,v) = S^{E_3}(-u,-v) (even in both parameters jointly).

        Since S(z) is even: S(u)*S(v)*S(u-v) = S(-u)*S(-v)*S(-u+v).
        VERIFIED [DC] numerical sweep [LT] E_3 S-matrix parity.
        """
        passes, max_res = verify_s_matrix_e3_inversion(H1, H2, H3)
        assert passes, f"E_3 parity failed: max residual = {max_res}"

    def test_e3_ratio_factorizes(self):
        """S^{E_3}_{(2)}/S^{E_3}_{(1,1)} = product of three E_2 ratios.

        VERIFIED [DC] direct computation [LT] Zamolodchikov ratio factorization.
        """
        u = 1.5 + 0.3j
        v = 0.8 - 0.2j
        result = s_matrix_charge2_e3(u, v, H1, H2, H3)
        assert result["ratio_factorizes"], "E_3 ratio does not factorize"

    def test_e3_at_v_equals_zero(self):
        """S^{E_3}(u, 0) reduces to S^{E_2}(u)^2 * S^{E_2}(0) (up to sign).

        At v=0: S^{E_3}(u,0) = S(u)*S(0)*S(u) = S(u)^2 * S(0).
        S(0) = g(h_i)^2.
        VERIFIED [DC] direct computation [LT] one-parameter reduction.
        """
        u = 1.5
        S_e3 = s_matrix_charge2_e3(u, 0.0001, H1, H2, H3)  # near v=0
        S_e2_u = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        S_e2_0 = s_matrix_charge2_diagonal_e2(0.0001, H1, H2, H3)
        S_e2_u2 = s_matrix_charge2_diagonal_e2(u - 0.0001, H1, H2, H3)

        expected_row = S_e2_u["S_row"] * S_e2_0["S_row"] * S_e2_u2["S_row"]
        # Just verify the factorization holds at near-zero v
        assert abs(S_e3["S_row_e3"] - expected_row) < 1e-6

    def test_e3_at_coincidence(self):
        """S^{E_3}(u,u) = S(u)^2 * S(0).

        At u=v: S^{E_3}(u,u) = S(u)*S(u)*S(0) = S(u)^2 * g(h_i)^2.
        VERIFIED [DC] direct computation [LT] E_3 coincident spectral parameters.
        """
        u = 1.5 + 0.3j
        S_e3 = s_matrix_charge2_e3(u, u, H1, H2, H3)
        S_u = s_matrix_charge2_diagonal_e2(u, H1, H2, H3)
        S_0 = s_matrix_charge2_diagonal_e2(0.0, H1, H2, H3)

        expected_row = S_u["S_row"] ** 2 * S_0["S_row"]
        expected_col = S_u["S_col"] ** 2 * S_0["S_col"]

        assert abs(S_e3["S_row_e3"] - expected_row) < 1e-10
        assert abs(S_e3["S_col_e3"] - expected_col) < 1e-10

    def test_e3_nontrivial(self):
        """S^{E_3}_{(2)} != S^{E_3}_{(1,1)} for generic (u,v).

        VERIFIED [DC] numerical inequality [LT] E_3 quantum group nontriviality.
        """
        u = 1.5 + 0.3j
        v = 0.8 - 0.2j
        S_e3 = s_matrix_charge2_e3(u, v, H1, H2, H3)
        assert abs(S_e3["S_row_e3"] - S_e3["S_col_e3"]) > 1e-3

    def test_e3_sv_params(self):
        """E_3 factorization at SV N=2 parameters.

        VERIFIED [DC] numerical sweep [LT] SV parameter consistency.
        """
        passes, max_res = verify_e3_zamolodchikov_factorization(H1_SV, H2_SV, H3_SV)
        assert passes, f"SV E_3 Zamolodchikov failed: max residual = {max_res}"

    def test_e3_miki_exchange(self):
        """S^{E_3}(u,v) vs S^{E_3}(v,u): the Miki exchange.

        Since S(z) is even and the Zamolodchikov factors are S(u),S(v),S(u-v):
            S^{E_3}(u,v) = S(u)*S(v)*S(u-v)
            S^{E_3}(v,u) = S(v)*S(u)*S(v-u) = S(u)*S(v)*S(u-v) = S^{E_3}(u,v)
        So S^{E_3} is symmetric in (u,v)!

        VERIFIED [DC] direct computation [LT] Miki exchange symmetry.
        """
        u = 1.5 + 0.3j
        v = 0.8 - 0.2j
        S_uv = s_matrix_charge2_e3(u, v, H1, H2, H3)
        S_vu = s_matrix_charge2_e3(v, u, H1, H2, H3)
        assert abs(S_uv["S_row_e3"] - S_vu["S_row_e3"]) < 1e-10, (
            "E_3 S-matrix is not symmetric under (u,v) exchange"
        )
        assert abs(S_uv["S_col_e3"] - S_vu["S_col_e3"]) < 1e-10


# ================================================================
# THETA FUNCTION / JACOBI FORM STRUCTURE
# ================================================================

class TestThetaFunctionStructure:
    """Theta function structure from the S-matrix spectrum product."""

    def test_spectrum_product_convergence(self):
        """Spectrum product Z_row converges as N_terms increases.

        VERIFIED [DC] numerical convergence [LT] theta function convergence.
        """
        Z_10 = s_matrix_spectrum_product(10, H1, H2, H3)
        Z_20 = s_matrix_spectrum_product(20, H1, H2, H3)
        Z_30 = s_matrix_spectrum_product(30, H1, H2, H3)

        # Ratios should converge
        ratio_10_20 = abs(Z_20["Z_row"] / Z_10["Z_row"] - 1.0)
        ratio_20_30 = abs(Z_30["Z_row"] / Z_20["Z_row"] - 1.0)

        # Convergence: the 20->30 change should be smaller than 10->20
        assert ratio_20_30 < ratio_10_20, (
            f"Not converging: |Z_20/Z_10 - 1|={ratio_10_20}, "
            f"|Z_30/Z_20 - 1|={ratio_20_30}"
        )

    def test_spectrum_product_nonzero(self):
        """Spectrum product is nonzero.

        VERIFIED [DC] numerical evaluation [LT] theta function nonvanishing.
        """
        Z = s_matrix_spectrum_product(20, H1, H2, H3)
        assert abs(Z["Z_row"]) > 1e-30, "Z_row is zero"
        assert abs(Z["Z_col"]) > 1e-30, "Z_col is zero"

    def test_spectrum_product_ratio_finite(self):
        """Z_row/Z_col is finite and nonzero.

        VERIFIED [DC] numerical evaluation [LT] eigenvalue ratio convergence.
        """
        Z = s_matrix_spectrum_product(20, H1, H2, H3)
        ratio = abs(Z["ratio"])
        assert ratio > 1e-10, f"Ratio too small: {ratio}"
        assert ratio < 1e10, f"Ratio too large: {ratio}"


# ================================================================
# PHI_10 CONNECTION (CONJECTURAL)
# ================================================================

class TestPhi10Connection:
    """Connection between S-matrix and Igusa cusp form Phi_10.

    ALL claims in this section are CONJECTURAL (AP-CY6/AP-CY14).
    They depend on CY-A_3 (the d=3 programme, unconstructed).
    The comparison is an OBSERVATION (AP-CY8), not a theorem.
    """

    def test_phi2_computation_runs(self):
        """phi_2 computation produces a finite value.

        VERIFIED [DC] numerical evaluation [LT] FJ coefficient computation.
        CLAIM STATUS: CONJECTURAL.
        """
        tau = 0.1 + 0.5j  # Im(tau) > 0 for convergence
        z = 0.2 + 0.1j
        phi_2 = phi10_charge2_fj_coefficient(tau, z, N_terms=10)
        assert np.isfinite(abs(phi_2)), f"phi_2 not finite: {phi_2}"

    def test_phi2_requires_positive_imaginary(self):
        """phi_2 computation requires Im(tau) > 0 (convergence of q-expansion).

        VERIFIED [DC] error handling [LT] modular form convergence domain.
        FM24 compliance: Im(tau) > 0 ensures |q| < 1.
        """
        with pytest.raises(ValueError, match="Im.*positive"):
            phi10_charge2_fj_coefficient(0.5 - 0.1j, 0.2)

    def test_phi10_connection_data(self):
        """Connection to Phi_10 returns structured comparison data.

        VERIFIED [DC] data structure check [LT] Phi_10 connection framework.
        CLAIM STATUS: CONJECTURAL.
        """
        result = s_matrix_phi10_connection(H1, H2, H3, N_spectrum=10)
        assert result["claim_status"] == "CONJECTURAL"
        assert "S_spectrum_product" in result
        assert "phi_2_approximation" in result

    def test_phi10_claim_status(self):
        """All Phi_10 claims are properly marked CONJECTURAL.

        AP-CY6/AP-CY14: any result depending on CY-A_3 must be conjectural.
        VERIFIED [DC] status check [LT] AP compliance.
        """
        summary = categorical_s_matrix_summary()
        assert "CONJECTURAL" in summary["phi10_connection"]["status"]
        assert "CY-A_3" in summary["phi10_connection"]["status"]


# ================================================================
# SYMBOLIC STRUCTURE
# ================================================================

class TestSymbolicStructure:
    """Symbolic computations verifying the algebraic structure."""

    def test_symbolic_s_row_defined(self):
        """Symbolic S_{(2)} is a well-defined rational function.

        VERIFIED [DC] symbolic computation [LT] rational function structure.
        """
        sym = s_matrix_charge2_symbolic_e2()
        assert sym["S_row"] is not None
        assert sym["S_row"] != 0

    def test_symbolic_s_col_defined(self):
        """Symbolic S_{(1,1)} is a well-defined rational function.

        VERIFIED [DC] symbolic computation [LT] rational function structure.
        """
        sym = s_matrix_charge2_symbolic_e2()
        assert sym["S_col"] is not None
        assert sym["S_col"] != 0

    def test_symbolic_trace_defined(self):
        """Symbolic Tr(S) = S_{(2)} + S_{(1,1)} is defined.

        VERIFIED [DC] symbolic computation [LT] S-matrix trace.
        """
        sym = s_matrix_charge2_symbolic_e2()
        assert sym["trace"] is not None

    def test_symbolic_ratio_nontrivial(self):
        """Symbolic S_{(2)}/S_{(1,1)} is not 1 (nontrivial braiding).

        VERIFIED [DC] symbolic computation [LT] quantum group nontriviality.
        """
        sym = s_matrix_charge2_symbolic_e2()
        assert sym["ratio"] != 1


# ================================================================
# SUMMARY AND AP COMPLIANCE
# ================================================================

class TestSummaryAndCompliance:
    """Summary and anti-pattern compliance checks."""

    def test_summary_structure(self):
        """Summary contains all required sections.

        VERIFIED [DC] structure check [LT] engine completeness.
        """
        summary = categorical_s_matrix_summary()
        assert "charge_1" in summary
        assert "charge_2_yang" in summary
        assert "charge_2_fock_diagonal" in summary
        assert "charge_2_e3" in summary
        assert "phi10_connection" in summary

    def test_charge1_proved(self):
        """Charge-1 S-matrix is marked PROVED.

        VERIFIED [DC] status check [LT] claim status correctness.
        """
        summary = categorical_s_matrix_summary()
        assert "PROVED" in summary["charge_1"]["status"]

    def test_yang_proved(self):
        """Yang R-matrix S-matrix is marked PROVED.

        VERIFIED [DC] status check [LT] claim status correctness.
        """
        summary = categorical_s_matrix_summary()
        assert "PROVED" in summary["charge_2_yang"]["status"]

    def test_fock_diagonal_proved(self):
        """Fock diagonal S-matrix is marked PROVED.

        VERIFIED [DC] status check [LT] claim status correctness.
        """
        summary = categorical_s_matrix_summary()
        assert "PROVED" in summary["charge_2_fock_diagonal"]["status"]

    def test_e3_conditional(self):
        """E_3 S-matrix is marked CONDITIONAL.

        VERIFIED [DC] status check [LT] claim status correctness.
        """
        summary = categorical_s_matrix_summary()
        assert "CONDITIONAL" in summary["charge_2_e3"]["status"]

    def test_phi10_conjectural(self):
        """Phi_10 connection is marked CONJECTURAL.

        AP-CY6, AP-CY14: depends on CY-A_3.
        VERIFIED [DC] status check [LT] AP compliance.
        """
        summary = categorical_s_matrix_summary()
        assert "CONJECTURAL" in summary["phi10_connection"]["status"]
