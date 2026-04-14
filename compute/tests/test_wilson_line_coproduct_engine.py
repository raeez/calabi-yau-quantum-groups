"""Tests for the Wilson line coproduct engine.

Verifies:
  1. Wilson line collision (Miura product) = Drinfeld coproduct
  2. Bialgebra compatibility (algebra homomorphism property)
  3. E_2 R-matrix: YBE and unitarity at charge 1
  4. E_3 R-matrix: two-parameter unitarity and Miki exchange
  5. E_3 -> E_2 projection
  6. Dimensional consistency: 3d = z=0 limit of 5d
  7. Dimensional consistency: 5d from 6d projection
  8. kappa_ch preservation across dimensions
  9. Cross-engine: Miura verifier matches e1_chiral_bialgebra_engine
 10. Cross-engine: R-matrix matches e3_two_parameter_rmatrix
"""

import numpy as np
import pytest

from compute.lib.wilson_line_coproduct_engine import (
    DimensionalConsistencyVerifier,
    WilsonLineCoproduct,
    WilsonLineMiuraVerifier,
    WilsonLineOperator,
    WilsonLineRMatrix,
)


# ===================================================================
# Suite 1: Wilson line collision = Drinfeld coproduct
# ===================================================================

class TestWilsonLineMiura:
    """Verify Wilson line OPE produces the Drinfeld coproduct."""

    def test_miura_equals_drinfeld_psi2(self):
        r = WilsonLineMiuraVerifier(Psi=2.0, N_max=5).verify_miura_equals_drinfeld()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_miura_equals_drinfeld_psi1(self):
        """At Psi=1 (free boson): cross-term vanishes, Delta(T) = T^L + T^R."""
        r = WilsonLineMiuraVerifier(Psi=1.0, N_max=5).verify_miura_equals_drinfeld()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_miura_equals_drinfeld_psi3(self):
        r = WilsonLineMiuraVerifier(Psi=3.0, N_max=5).verify_miura_equals_drinfeld()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_miura_equals_drinfeld_complex_z(self):
        r = WilsonLineMiuraVerifier(Psi=2.0, N_max=5).verify_miura_equals_drinfeld(
            z=0.7 - 0.4j
        )
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_bialgebra_compatibility(self):
        r = WilsonLineMiuraVerifier(Psi=2.0, N_max=5).verify_bialgebra_compatibility()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"
        assert abs(r["c_eff"] - 4.0) < 1e-12

    def test_bialgebra_compatibility_psi1(self):
        r = WilsonLineMiuraVerifier(Psi=1.0, N_max=5).verify_bialgebra_compatibility()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"
        assert abs(r["c_eff"] - 2.0) < 1e-12  # Two decoupled copies


# ===================================================================
# Suite 2: E_2 R-matrix (one-parameter, Yangian)
# ===================================================================

class TestE2RMatrix:
    """Verify the E_2 (Yangian) R-matrix from Wilson line braiding."""

    def test_ybe_charge1(self):
        r = WilsonLineRMatrix(1.0, -2.0, 1.0).verify_ybe_charge1()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_unitarity_charge1(self):
        r = WilsonLineRMatrix(1.0, -2.0, 1.0).verify_unitarity_charge1()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_unitarity_charge1_generic(self):
        """Generic Omega-background: h = (3, -5, 2)."""
        r = WilsonLineRMatrix(3.0, -5.0, 2.0).verify_unitarity_charge1()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_charge2_diagonal(self):
        """R-matrix diagonal at charge 2 is a product over contents."""
        R = WilsonLineRMatrix(1.0, -2.0, 1.0)
        g = R.structure_function
        diag = R.r_matrix_e2_charge2_diagonal(3.5 + 0.7j)
        # R_{row,row}(u) = g(u) * g(u + h1)
        expected_row = g(3.5 + 0.7j) * g(3.5 + 0.7j + 1.0)
        assert abs(diag["R_row_row"] - expected_row) < 1e-12

    def test_classical_r_matrix(self):
        """Classical r-matrix: r(u) = -sigma_2 / u."""
        R = WilsonLineRMatrix(1.0, -2.0, 1.0)
        # sigma_2 = 1*(-2) + 1*1 + (-2)*1 = -2 + 1 - 2 = -3
        u = 10.0 + 0.5j
        r_cl = R.classical_r_matrix(u)
        assert abs(r_cl - (-(-3.0)) / u) < 1e-12  # -sigma_2 / u = 3/u

    def test_self_dual_trivial(self):
        """At self-dual point h = (1, 0, -1): g(u) = 1, R-matrix trivial."""
        R = WilsonLineRMatrix(1.0, 0.0, -1.0)
        for u in [0.5, 1.5, 3.0 + 1j]:
            assert abs(R.r_matrix_e2_charge1(u) - 1.0) < 1e-12


# ===================================================================
# Suite 3: E_3 R-matrix (two-parameter, quantum toroidal)
# ===================================================================

class TestE3RMatrix:
    """Verify the E_3 (quantum toroidal) R-matrix."""

    def test_e3_unitarity(self):
        r = WilsonLineRMatrix(1.0, -2.0, 1.0).verify_e3_unitarity_charge1()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_miki_exchange(self):
        r = WilsonLineRMatrix(1.0, -2.0, 1.0).verify_miki_exchange()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_e3_to_e2_projection(self):
        r = WilsonLineRMatrix(1.0, -2.0, 1.0).verify_e3_to_e2_projection()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_zamolodchikov_factorization(self):
        """G_ch(u,v) = g(u)*g(v)*g(u-v) (Zamolodchikov factorization)."""
        R = WilsonLineRMatrix(1.0, -2.0, 1.0)
        g = R.structure_function
        u, v = 3.5 + 0.7j, -2.3 + 1.1j
        G = R.r_matrix_e3_charge1(u, v)
        expected = g(u) * g(v) * g(u - v)
        assert abs(G - expected) < 1e-12

    def test_e3_generic_omega(self):
        """E_3 unitarity at generic Omega-background h = (3, -5, 2)."""
        r = WilsonLineRMatrix(3.0, -5.0, 2.0).verify_e3_unitarity_charge1()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_miki_exchange_generic(self):
        r = WilsonLineRMatrix(3.0, -5.0, 2.0).verify_miki_exchange()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"


# ===================================================================
# Suite 4: Dimensional consistency
# ===================================================================

class TestDimensionalConsistency:
    """Verify consistency across the 3d/5d/6d hierarchy."""

    def test_3d_is_z0_limit_of_5d(self):
        r = DimensionalConsistencyVerifier(Psi=2.0, N_max=5).verify_3d_is_z0_limit_of_5d()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_5d_from_6d_projection(self):
        r = DimensionalConsistencyVerifier(Psi=2.0, N_max=5).verify_5d_from_6d_projection()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_kappa_preserved(self):
        r = DimensionalConsistencyVerifier(Psi=2.0, N_max=5).verify_kappa_preserved()
        assert r["ok"]
        assert r["all_equal"]
        assert abs(r["value"] - 2.0) < 1e-12

    def test_3d_primitive_coproduct(self):
        """3d Wilson line collision gives primitive coproduct."""
        wlc = WilsonLineCoproduct(Psi=2.0, N_max=5)
        for n in [-2, -1, 0, 1, 2]:
            result = wlc.coproduct_3d(n)
            assert result["en_level"] == 1
            assert result["spectral_params"] == 0

    def test_5d_coproduct_has_spectral_param(self):
        """5d Wilson line collision carries spectral parameter."""
        wlc = WilsonLineCoproduct(Psi=2.0, N_max=5)
        result = wlc.coproduct_5d(0, z=0.5)
        assert result["en_level"] == 2
        assert result["spectral_params"] == 1

    def test_6d_coproduct_charge1(self):
        """6d Wilson line collision: two spectral parameters, charge 1."""
        wlc = WilsonLineCoproduct(Psi=2.0, N_max=5)
        result = wlc.coproduct_6d_charge1(
            u=3.5, v=2.1, h1=1.0, h2=-2.0, h3=1.0
        )
        assert result["en_level"] == 3
        assert result["spectral_params"] == 2
        # Zamolodchikov factorization
        assert abs(result["G_ch"] - result["g_u"] * result["g_v"] * result["g_u_minus_v"]) < 1e-12


# ===================================================================
# Suite 5: Cross-engine consistency
# ===================================================================

class TestCrossEngine:
    """Verify consistency with other compute engines."""

    def test_matches_e1_bialgebra_engine(self):
        """Wilson line Miura verifier agrees with e1_chiral_bialgebra_engine."""
        from compute.lib.e1_chiral_bialgebra_engine import BialgebraCompatibilityVerifier
        # Both should produce the same Delta_z(T_n)
        wlm = WilsonLineMiuraVerifier(Psi=2.0, N_max=5)
        bv = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)

        P = wlm.TH.safe_proj(3)
        z = 0.3 + 0.2j
        mx = 0.0
        for n in [0, -1, -2, 1]:
            wl_dt = wlm.TH.Delta_T(n, z)
            bv_dt = bv.TH.Delta_T(n, z)
            err = float(np.max(np.abs(P @ (wl_dt - bv_dt) @ P)))
            mx = max(mx, err)
        assert mx < 1e-12, f"max_error = {mx:.2e}"

    def test_matches_e3_two_param_rmatrix(self):
        """Wilson line R-matrix agrees with e3_two_parameter_rmatrix engine."""
        from compute.lib.e3_two_parameter_rmatrix import (
            two_param_structure_function_additive,
        )
        R = WilsonLineRMatrix(1.0, -2.0, 1.0)
        for j in range(8):
            u = 3.5 + 0.7j * (j + 1) / 8
            v = -2.3 + 1.1j * (j + 1) / 8
            G_wl = R.r_matrix_e3_charge1(u, v)
            G_e3 = two_param_structure_function_additive(u, v, 1.0, -2.0, 1.0)
            assert abs(G_wl - G_e3) < 1e-10, \
                f"j={j}: |G_wl - G_e3| = {abs(G_wl - G_e3):.2e}"

    def test_matches_holomorphic_cs_engine(self):
        """Wilson line R-matrix parameters match holomorphic CS engine."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        omega = OmegaBackground(1, -2)
        R = WilsonLineRMatrix(1.0, -2.0, 1.0)
        # sigma_2 must agree
        assert abs(float(omega.sigma2) - R.sigma2) < 1e-12
        # sigma_3 must agree
        assert abs(float(omega.sigma3) - R.sigma3) < 1e-12
        # Classical r-matrix residue
        assert abs(float(omega.classical_r_residue()) - (-R.sigma2)) < 1e-12


# ===================================================================
# Suite 6: Wilson line operator basics
# ===================================================================

class TestWilsonLineOperator:
    """Basic Wilson line operator tests."""

    def test_charge_operator(self):
        """J_0 on the vacuum Fock space."""
        wl = WilsonLineOperator(Psi=1.0, N_max=5)
        J0 = wl.charge_operator()
        vac = wl.H.vacuum()
        # Vacuum has charge 0
        assert abs(float(J0 @ vac)[0]) < 1e-12 if len(J0 @ vac) > 0 else True

    def test_transfer_matrix_spin1(self):
        """psi_{1,n} = J_n."""
        wl = WilsonLineOperator(Psi=2.0, N_max=5)
        for n in [-2, -1, 0, 1, 2]:
            psi1 = wl.transfer_matrix_mode(1, n)
            Jn = wl.H.J(n)
            assert np.max(np.abs(psi1 - Jn)) < 1e-12

    def test_transfer_matrix_spin0(self):
        """psi_{0,n} = delta_{n,0} * Id."""
        wl = WilsonLineOperator(Psi=2.0, N_max=5)
        psi0_0 = wl.transfer_matrix_mode(0, 0)
        assert np.max(np.abs(psi0_0 - np.eye(wl.H.dim))) < 1e-12
        psi0_1 = wl.transfer_matrix_mode(0, 1)
        assert np.max(np.abs(psi0_1)) < 1e-12
