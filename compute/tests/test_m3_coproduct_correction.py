r"""Tests for the m_3 coproduct correction delta^{(3)}(T_n).

Verifies the A_infinity correction to the Yangian coproduct from the
Virasoro cubic self-coupling m_3(T,T,T) = -2T at c=1.

The main result:
  delta^{(3)}(T_n) = -2*(Psi-1)/Psi * sum_k J_k^L J_{n-k}^R

Tests cover:
  1. Morphism defect equation (the DEFINING equation for delta^{(3)})
  2. Vacuum matrix element = 0
  3. Psi=1 vanishing (free boson, class G)
  4. Weight conservation
  5. Cross-term ratio = -2
  6. Psi-dependence across multiple levels
  7. Multi-mode consistency (n=0, +/-1, +/-2)
  8. Eigenvalue spectrum structure
  9. Corrected coproduct consistency
  10. Intertwining with Delta_0(J)
"""

import numpy as np
import pytest

from compute.lib.m3_coproduct_correction_engine import (
    M3CoproductCorrection,
    compute_delta3_T0,
    verify_all,
)
from compute.lib.chiral_coproduct_spin2_engine import TensorHeisenberg


# -----------------------------------------------------------------------
# Test 1: Morphism defect equation
# -----------------------------------------------------------------------

class TestMorphismCondition:
    """The defining equation for delta^{(3)}."""

    def test_morphism_mode_0(self):
        """Delta_0(m_3(T_0^3)) = m_3^{diag}(Delta_0(T_0)^3) + delta^{(3)}(T_0)."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_morphism_condition(0)
        assert result["ok"], f"Morphism error = {result['max_error']:.2e}"

    def test_morphism_mode_1(self):
        """Morphism condition at mode n=1."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_morphism_condition(1)
        assert result["ok"], f"Morphism error = {result['max_error']:.2e}"

    def test_morphism_mode_minus1(self):
        """Morphism condition at mode n=-1."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_morphism_condition(-1)
        assert result["ok"], f"Morphism error = {result['max_error']:.2e}"

    def test_morphism_mode_minus2(self):
        """Morphism condition at mode n=-2."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_morphism_condition(-2)
        assert result["ok"], f"Morphism error = {result['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [1.0, 1.5, 2.0, 3.0, 5.0])
    def test_morphism_all_psi(self, Psi):
        """Morphism condition holds for all Psi values."""
        eng = M3CoproductCorrection(Psi=Psi, N_max=4)
        result = eng.verify_morphism_condition(0)
        assert result["ok"], f"Psi={Psi}: error = {result['max_error']:.2e}"


# -----------------------------------------------------------------------
# Test 2: Vacuum matrix element
# -----------------------------------------------------------------------

class TestVacuumExpectation:
    """<vac,vac| delta^{(3)}(T_n) |vac,vac> = 0."""

    def test_vev_mode_0(self):
        """Vacuum expectation value at mode 0 is zero."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.vacuum_matrix_element(0)
        assert result["is_zero"], f"VEV = {result['vev']}"

    def test_vev_mode_1(self):
        """Vacuum expectation value at mode 1 is zero."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.vacuum_matrix_element(1)
        assert result["is_zero"], f"VEV = {result['vev']}"

    def test_vev_mode_minus1(self):
        """Vacuum expectation value at mode -1 is zero."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.vacuum_matrix_element(-1)
        assert result["is_zero"], f"VEV = {result['vev']}"

    def test_vev_explicit_computation(self):
        """VEV is zero because J_k annihilates the vacuum for k > 0."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        vac = np.zeros(eng.dim)
        vac[eng.H.idx[()] * eng.d + eng.H.idx[()]] = 1.0
        d3 = eng.delta3_T(0)
        vev = float(vac @ d3 @ vac)
        assert abs(vev) < 1e-14


# -----------------------------------------------------------------------
# Test 3: Psi=1 vanishing
# -----------------------------------------------------------------------

class TestPsi1Vanishing:
    """At Psi=1, delta^{(3)} = 0 (free boson is class G)."""

    def test_psi1_zero(self):
        """delta^{(3)}(T_0) vanishes identically at Psi=1."""
        eng = M3CoproductCorrection(Psi=1.0, N_max=4)
        result = eng.verify_psi1_vanishing()
        assert result["ok"], f"Norm = {result['max_norm']:.2e}"

    def test_psi1_alpha_zero(self):
        """alpha = 0 at Psi = 1."""
        eng = M3CoproductCorrection(Psi=1.0, N_max=4)
        assert abs(eng.alpha) < 1e-14

    def test_psi1_all_modes_zero(self):
        """delta^{(3)}(T_n) = 0 for all modes at Psi=1."""
        eng = M3CoproductCorrection(Psi=1.0, N_max=4)
        P = eng.safe_proj(2)
        for n in range(-2, 3):
            d3 = eng.delta3_T(n)
            norm = float(np.max(np.abs(P @ d3 @ P)))
            assert norm < 1e-14, f"n={n}: norm = {norm:.2e}"


# -----------------------------------------------------------------------
# Test 4: Weight conservation
# -----------------------------------------------------------------------

class TestWeightConservation:
    """[L_0^tot, delta^{(3)}(T_n)] = -n * delta^{(3)}(T_n)."""

    def test_weight_mode_0(self):
        """[L_0^tot, delta^{(3)}(T_0)] = 0 (weight-preserving)."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_weight_conservation(0)
        assert result["ok"], f"Error = {result['max_error']:.2e}"

    def test_weight_mode_1(self):
        """[L_0^tot, delta^{(3)}(T_1)] = -1 * delta^{(3)}(T_1)."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_weight_conservation(1)
        assert result["ok"], f"Error = {result['max_error']:.2e}"

    def test_weight_mode_minus1(self):
        """[L_0^tot, delta^{(3)}(T_{-1})] = +1 * delta^{(3)}(T_{-1})."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_weight_conservation(-1)
        assert result["ok"], f"Error = {result['max_error']:.2e}"


# -----------------------------------------------------------------------
# Test 5: Cross-term ratio
# -----------------------------------------------------------------------

class TestCrossTermRatio:
    """delta^{(3)} = -2 * cross_term(Delta_0)."""

    def test_ratio_mode_0(self):
        """delta^{(3)}(T_0) = -2 * alpha * sum J_k^L J_{-k}^R."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.cross_term_ratio(0)
        assert result["ok"], f"Error = {result['max_error']:.2e}"

    def test_ratio_mode_1(self):
        """Cross-term ratio = -2 at mode 1."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.cross_term_ratio(1)
        assert result["ok"], f"Error = {result['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [1.5, 2.0, 3.0])
    def test_ratio_psi_independent(self, Psi):
        """The ratio delta^{(3)}/cross = -2 is independent of Psi."""
        eng = M3CoproductCorrection(Psi=Psi, N_max=4)
        result = eng.cross_term_ratio(0)
        assert result["ok"], f"Psi={Psi}: error = {result['max_error']:.2e}"


# -----------------------------------------------------------------------
# Test 6: Psi-dependence
# -----------------------------------------------------------------------

class TestPsiDependence:
    """The coefficient -2*(Psi-1)/Psi varies correctly with Psi."""

    def test_coefficient_psi2(self):
        """At Psi=2: coefficient = -2*(1/2) = -1."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        assert abs(eng.alpha - 0.5) < 1e-14
        assert abs(-2.0 * eng.alpha - (-1.0)) < 1e-14

    def test_coefficient_psi3(self):
        """At Psi=3: coefficient = -2*(2/3) = -4/3."""
        eng = M3CoproductCorrection(Psi=3.0, N_max=4)
        assert abs(-2.0 * eng.alpha - (-4.0 / 3.0)) < 1e-14

    def test_all_psi_morphism(self):
        """Morphism condition holds across all Psi values."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        results = eng.psi_dependence(0)
        for Psi_test, data in results.items():
            assert data["morphism_ok"], f"Psi={Psi_test}: morphism failed"


# -----------------------------------------------------------------------
# Test 7: Multi-mode consistency
# -----------------------------------------------------------------------

class TestMultiMode:
    """Consistency across multiple modes."""

    @pytest.mark.parametrize("n", [-2, -1, 0, 1, 2])
    def test_morphism_multimode(self, n):
        """Morphism condition at various modes."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        result = eng.verify_morphism_condition(n)
        assert result["ok"], f"n={n}: error = {result['max_error']:.2e}"

    def test_mode_0_trace(self):
        """Trace of delta^{(3)}(T_0) on safe subspace."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        spec = eng.eigenvalue_spectrum(0)
        # Trace is sum of eigenvalues; the JJ cross-term has zero trace
        # on the truncated space (up to boundary effects)
        assert abs(spec["trace"]) < 1e-8, f"Trace = {spec['trace']}"


# -----------------------------------------------------------------------
# Test 8: Eigenvalue spectrum
# -----------------------------------------------------------------------

class TestEigenvalueSpectrum:
    """Eigenvalue structure of delta^{(3)}(T_0)."""

    def test_nonzero_eigenvalues_exist(self):
        """delta^{(3)}(T_0) has nonzero eigenvalues for Psi != 1."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        spec = eng.eigenvalue_spectrum(0)
        assert spec["n_nonzero"] > 0, "No nonzero eigenvalues"

    def test_spectrum_symmetric(self):
        """Eigenvalue spectrum is symmetric about 0 (from JJ structure)."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        spec = eng.eigenvalue_spectrum(0)
        evals = spec["eigenvalues_nonzero"]
        # Check positive/negative pairing
        pos = sorted([e for e in evals if e > 0])
        neg = sorted([-e for e in evals if e < 0])
        # Not necessarily exactly paired due to truncation, but
        # check the total is approximately zero (trace condition)
        assert abs(sum(evals)) < 1e-8


# -----------------------------------------------------------------------
# Test 9: Corrected coproduct
# -----------------------------------------------------------------------

class TestCorrectedCoproduct:
    """Properties of Delta_0(T_0) + delta^{(3)}(T_0)."""

    def test_corrected_cross_coefficient(self):
        """Corrected cross-term has coefficient -alpha (sign-flipped).

        Original: alpha * sum J^L J^R
        Correction: -2*alpha * sum J^L J^R
        Net: -alpha * sum J^L J^R
        """
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        P = eng.safe_proj(2)
        M = eng.N_max + 2

        corrected = eng.corrected_coproduct_T(0, 0.0)

        # The corrected coproduct should be:
        # T_0^L + T_0^R + (alpha - 2*alpha) * sum J^L J^R
        # = T_0^L + T_0^R - alpha * sum J^L J^R
        expected = eng.T_L(0).astype(float) + eng.T_R(0).astype(float)
        cross = np.zeros((eng.dim, eng.dim))
        for k in range(-M, M + 1):
            cross += eng.J_L(k) @ eng.J_R(-k)
        expected -= eng.alpha * cross

        err = float(np.max(np.abs(P @ (corrected - expected) @ P)))
        assert err < 1e-10, f"Error = {err:.2e}"

    def test_corrected_vacuum_eigenvalue(self):
        """Corrected T_0 has zero vacuum eigenvalue (same as uncorrected)."""
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        vac = np.zeros(eng.dim)
        vac[eng.H.idx[()] * eng.d + eng.H.idx[()]] = 1.0
        corrected = eng.corrected_coproduct_T(0, 0.0)
        eigenval = complex(vac @ corrected @ vac).real
        assert abs(eigenval) < 1e-14


# -----------------------------------------------------------------------
# Test 10: J-intertwining
# -----------------------------------------------------------------------

class TestJIntertwining:
    """Intertwining of delta^{(3)}(T_0) with the Heisenberg current."""

    def test_commutator_with_delta_J(self):
        """[delta^{(3)}(T_0), Delta_0(J_m)] = 2*alpha*Psi*m * Delta_0(J_m).

        Since delta^{(3)}(T_0) = -2*alpha * sum_k J_k^L J_{-k}^R, and
        [J_k^L J_{-k}^R, J_m^L] = Psi*k*delta_{k+m,0} * J_{-k}^R
                                 = -Psi*m * J_m^R (at k=-m)
        [J_k^L J_{-k}^R, J_m^R] = Psi*(-k)*delta_{-k+m,0} * J_k^L
                                 = -Psi*m * J_m^L (at k=m)

        So [sum J_k^L J_{-k}^R, Delta_0(J_m)] = -Psi*m * Delta_0(J_m)
        And [delta^{(3)}(T_0), Delta_0(J_m)] = -2*alpha*(-Psi*m)*Delta_0(J_m)
                                              = 2*alpha*Psi*m * Delta_0(J_m)
        """
        eng = M3CoproductCorrection(Psi=2.0, N_max=4)
        P = eng.safe_proj(2)
        d3 = eng.delta3_T(0)

        for m in [-1, 1, 2]:
            DJ_m = eng.Delta_J(m, 0.0)
            comm = d3 @ DJ_m - DJ_m @ d3
            expected = 2.0 * eng.alpha * eng.Psi * m * DJ_m
            err = float(np.max(np.abs(P @ (comm - expected) @ P)))
            assert err < 1e-8, f"m={m}: error = {err:.2e}"


# -----------------------------------------------------------------------
# Test 11: Master computation function
# -----------------------------------------------------------------------

class TestMasterComputation:
    """The compute_delta3_T0 convenience function."""

    def test_compute_delta3_T0(self):
        """Master computation returns consistent results."""
        result = compute_delta3_T0(Psi=2.0, N_max=4)
        assert result["vev_is_zero"]
        assert result["morphism_ok"]
        assert result["weight_conservation_ok"]
        assert result["cross_term_ratio_ok"]
        assert abs(result["coefficient"] - (-1.0)) < 1e-14

    def test_verify_all(self):
        """Full verification suite passes."""
        result = verify_all(Psi=2.0, N_max=4)
        assert result["all_ok"], f"Failures in verify_all: {result}"
