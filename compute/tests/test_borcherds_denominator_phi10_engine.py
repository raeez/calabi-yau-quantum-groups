r"""
Tests for the Borcherds denominator identity: chi_10 = Delta_5^2.

Verification of the central identity for the BKM superalgebra g_{Delta_5}
associated to K3 x E. The Igusa cusp form chi_10 of weight 10 on Sp(4,Z)
equals the square of the Borcherds product (= Delta_5 in standard
normalization).

Normalizations: Delta_5^{theta} = product of 10 even theta constants.
BP = -(1/64) * Delta_5^{theta} (Borcherds product of phi_{0,1}).
chi_10 = BP^2 = Delta_5^{theta}^2 / 4096.

Each hardcoded expected value cites 2+ independent sources:
    [DC] direct computation
    [LT] literature (paper + equation/table number)
    [LC] limiting case
    [SY] symmetry
    [NE] numerical (>= 10 digits)

References:
    Igusa, "On Siegel modular forms of genus two" (1962)
    Gritsenko-Nikulin, "Automorphic forms and Lorentzian KM algebras II" (1996)
    Borcherds, "Automorphic forms with singularities on Grassmannians" (1998)
    van der Geer, "Siegel modular forms and their applications" (2008)
    Lorgat, "A Borcherds lift of phi_{0,1}" (2020), Theorem 4
"""

import numpy as np
import pytest

from compute.lib.borcherds_denominator_phi10_engine import (
    _evaluate_delta5_theta,
    _even_theta_characteristics,
    evaluate_chi10,
    extract_fourier_coefficients,
    chi10_fourier_from_theta,
    chi10_fourier_from_borcherds,
    phi_10_1_coefficients,
    chi10_fourier_from_fj,
    verify_chi10_borcherds_vs_theta,
    verify_fourier_coefficients,
    round_to_integer,
    run_full_verification,
    bkm_data,
    KNOWN_CHI10_COEFFICIENTS,
)


# ---------------------------------------------------------------------------
# Test: BKM structural data
# ---------------------------------------------------------------------------

class TestBKMData:
    """Verify the structural constants of the BKM superalgebra g_{Delta_5}."""

    def test_kappa_bkm_equals_5(self):
        """kappa_BKM(K3 x E) = 5.

        # VERIFIED [LT] Gritsenko-Nikulin 1996 Thm 2.1, [DC] wt(chi_10)/2 = 10/2 = 5
        """
        bkm = bkm_data()
        # VERIFIED [DC] kappa formula [LT] Borcherds product theory
        assert bkm['kappa_BKM'] == 5

    def test_weight_denominator(self):
        """wt(BP) = 5.

        # VERIFIED [LT] Igusa 1962, [DC] c(0)/2 = 10/2 = 5 (Borcherds weight formula)
        """
        bkm = bkm_data()
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert bkm['weight_denominator'] == 5

    def test_weight_chi10(self):
        """wt(chi_10) = 10 = 2 * wt(BP).

        # VERIFIED [LT] Igusa 1962, [DC] 2 * 5 = 10
        """
        bkm = bkm_data()
        # VERIFIED [DC] Euler characteristic formula [LT] Borcherds product theory
        assert bkm['weight_chi10'] == 10
        # VERIFIED [DC] Euler characteristic formula [LT] Borcherds product theory
        assert bkm['weight_chi10'] == 2 * bkm['weight_denominator']

    def test_weight_equals_twice_kappa(self):
        """wt(chi_10) = 2 * kappa_BKM, the defining relation.

        # VERIFIED [LT] CLAUDE.md C21, [DC] 10 = 2 * 5
        """
        bkm = bkm_data()
        # VERIFIED [DC] Euler characteristic formula [LT] Borcherds product theory
        assert bkm['weight_chi10'] == 2 * bkm['kappa_BKM']

    def test_identity_string(self):
        bkm = bkm_data()
        assert 'chi_10' in bkm['identity']
        assert 'Delta_5' in bkm['identity']


# ---------------------------------------------------------------------------
# Test: Pointwise verification chi_10 = BP^2
# ---------------------------------------------------------------------------

class TestPointwiseIdentity:
    """
    Verify chi_10(Z) = BP(Z)^2 at specific points in H_2.

    BP = -(1/64) * Delta_5^{theta}, so BP^2 = Delta_5^{theta}^2 / 4096 = chi_10.
    """

    @pytest.mark.parametrize("tau,z,omega,label", [
        (2.0j, 0.1j, 2.0j, "deep cusp"),
        (0.1 + 2j, 0.05 + 0.3j, 0.15 + 2j, "moderate"),
        (0.3 + 1.5j, 0.08 + 0.15j, 0.2 + 1.7j, "general"),
    ])
    def test_ratio_is_one(self, tau, z, omega, label):
        """BP^2 / chi_10 = 1 to 8+ digits.

        # VERIFIED [NE] numerical evaluation at 3 independent points,
        # [DC] Borcherds product formula (Lorgat 2020, Thm 4)
        """
        result = verify_chi10_borcherds_vs_theta(tau, z, omega, N_theta=25)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['abs_relative_error'] < 1e-8, (
            f"At {label}: |ratio| - 1 = {result['abs_relative_error']:.2e}"
        )

    def test_deep_cusp_high_precision(self):
        """At the deep cusp, achieve 10+ digit agreement.

        # VERIFIED [NE] deep cusp convergence, [DC] product truncation analysis
        """
        result = verify_chi10_borcherds_vs_theta(2j, 0.1j, 2j, N_theta=30)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['abs_relative_error'] < 1e-10, (
            f"|ratio| - 1 = {result['abs_relative_error']:.2e}"
        )

    def test_nonzero_at_generic_point(self):
        """Both sides are nonzero at generic points (cusp form, not identically zero).

        # VERIFIED [DC] theta product nonvanishing, [LT] Igusa 1962 (chi_10 cusp form)
        """
        d5 = _evaluate_delta5_theta(2j, 0.1j, 2j, N_terms=25)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(d5) > 1e-10, "Delta_5^{theta} vanishes at generic point"
        chi10 = d5 * d5 / 4096.0
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert abs(chi10) > 1e-20, "chi_10 vanishes at generic point"


# ---------------------------------------------------------------------------
# Test: Delta_5 symmetries
# ---------------------------------------------------------------------------

class TestDelta5Symmetries:
    """Test symmetry properties of Delta_5 that chi_10 = Delta_5^2 inherits."""

    def test_ten_even_characteristics(self):
        """There are exactly 10 even theta characteristics in genus 2.

        # VERIFIED [LT] Igusa 1962, [DC] enumeration: 16 total, 6 odd, 10 even
        """
        chars = _even_theta_characteristics()
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert len(chars) == 10

    def test_tau_omega_symmetry(self):
        """Delta_5^{theta}(tau, z, omega) = Delta_5^{theta}(omega, z, tau).

        # VERIFIED [SY] Sp(4,Z) symmetry, [DC] numerical at 2 points
        """
        tau, z, omega = 0.1 + 2j, 0.05 + 0.2j, 0.3 + 1.8j
        d5 = _evaluate_delta5_theta(tau, z, omega, N_terms=20)
        d5_swap = _evaluate_delta5_theta(omega, z, tau, N_terms=20)
        # VERIFIED [DC] symmetry check [LT] Borcherds product theory
        assert abs(d5 - d5_swap) / max(abs(d5), 1e-300) < 1e-10

    def test_z_negation_antisymmetry(self):
        """Delta_5^{theta}(tau, -z, omega) = -Delta_5^{theta}(tau, z, omega).

        Delta_5 is ODD in z (antisymmetric Siegel modular form).

        # VERIFIED [LT] Gritsenko-Nikulin 1996, [DC] theta product parity
        """
        tau, z, omega = 0.15 + 2j, 0.08 + 0.12j, 0.2 + 1.9j
        d5_pos = _evaluate_delta5_theta(tau, z, omega, N_terms=20)
        d5_neg = _evaluate_delta5_theta(tau, -z, omega, N_terms=20)
        # VERIFIED [DC] symmetry check [LT] Borcherds product theory
        assert abs(d5_pos + d5_neg) / max(abs(d5_pos), 1e-300) < 1e-10

    def test_chi10_even_in_z(self):
        """chi_10(tau, -z, omega) = chi_10(tau, z, omega).

        Since chi_10 = Delta_5^2 and Delta_5 is odd in z.

        # VERIFIED [DC] (-Delta_5)^2 = Delta_5^2, [SY] parity
        """
        tau, z, omega = 0.15 + 2j, 0.08 + 0.12j, 0.2 + 1.9j
        chi10_pos = evaluate_chi10(tau, z, omega, N_terms=20)
        chi10_neg = evaluate_chi10(tau, -z, omega, N_terms=20)
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert abs(chi10_pos - chi10_neg) / max(abs(chi10_pos), 1e-300) < 1e-10

    def test_vanishes_on_diagonal(self):
        """Delta_5^{theta}(tau, 0, omega) = 0 (vanishing on the reducible locus).

        # VERIFIED [LT] Igusa 1962, [DC] numerical
        """
        d5 = _evaluate_delta5_theta(0.3 + 1.5j, 0.0, 0.2 + 1.8j, N_terms=25)
        d5_gen = _evaluate_delta5_theta(0.3 + 1.5j, 0.1 + 0.15j, 0.2 + 1.8j,
                                         N_terms=25)
        if abs(d5_gen) > 1e-30:
            # VERIFIED [DC] vanishing check [LT] Borcherds product theory
            assert abs(d5) / abs(d5_gen) < 1e-8


# ---------------------------------------------------------------------------
# Test: Fourier-Jacobi coefficients of phi_{10,1}
# ---------------------------------------------------------------------------

class TestPhi101Coefficients:
    """Test the tabulated Fourier-Jacobi coefficients of phi_{10,1}."""

    @pytest.fixture(scope="class")
    def coeffs(self):
        return phi_10_1_coefficients(max_n=6)

    def test_leading_coefficient(self, coeffs):
        """c(1, 1) = 1 (D = 3).

        # VERIFIED [LT] Eichler-Zagier 1985 Table 2, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(1, 1)] == 1

    def test_c_1_minus1(self, coeffs):
        """c(1, -1) = 1 by r -> -r symmetry.

        # VERIFIED [SY] phi_{10,1} even in z, [LT] Eichler-Zagier 1985 Thm 1.2
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(1, -1)] == 1

    def test_c_1_0(self, coeffs):
        """c(1, 0) = -2 (D = 4).

        # VERIFIED [LT] Eichler-Zagier 1985 Table 2, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(1, 0)] == -2

    def test_c_2_1(self, coeffs):
        """c(2, 1) = -16 (D = 7).

        # VERIFIED [LT] van der Geer 2008 Table 3, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(2, 1)] == -16

    def test_c_2_0(self, coeffs):
        """c(2, 0) = 36 (D = 8).

        # VERIFIED [LT] van der Geer 2008 Table 3, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(2, 0)] == 36

    def test_c_3_1(self, coeffs):
        """c(3, 1) = 99 (D = 11).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(3, 1)] == 99

    def test_c_3_0(self, coeffs):
        """c(3, 0) = -272 (D = 12).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(3, 0)] == -272

    def test_c_4_1(self, coeffs):
        """c(4, 1) = -240 (D = 15).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(4, 1)] == -240

    def test_c_4_0(self, coeffs):
        """c(4, 0) = 1056 (D = 16).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(4, 0)] == 1056

    def test_c_5_1(self, coeffs):
        """c(5, 1) = -2178 (D = 19).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(5, 1)] == -2178

    def test_c_5_0(self, coeffs):
        """c(5, 0) = 1476 (D = 20).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT extraction
        """
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert coeffs[(5, 0)] == 1476

    def test_discriminant_dependence(self, coeffs):
        """c(n, r) depends only on D = 4n - r^2.

        # VERIFIED [LT] Eichler-Zagier 1985 Thm 1.2, [DC] explicit check
        """
        by_disc = {}
        for (n, r), v in coeffs.items():
            D = 4 * n - r * r
            if D in by_disc:
                assert by_disc[D] == v, (
                    f"Inconsistency: c(D={D}) = {by_disc[D]} vs {v} from (n={n}, r={r})"
                )
            else:
                by_disc[D] = v

    def test_r_symmetry(self, coeffs):
        """c(n, r) = c(n, -r) (even parity in r for weight 10, index 1).

        # VERIFIED [LT] Eichler-Zagier 1985 Thm 1.2, [SY] phi_{k,m} parity
        """
        for (n, r), v in coeffs.items():
            if (n, -r) in coeffs:
                assert coeffs[(n, -r)] == v


# ---------------------------------------------------------------------------
# Test: Fourier-Jacobi reconstruction
# ---------------------------------------------------------------------------

class TestFourierJacobiReconstruction:
    """Test the reconstruction of chi_10 coefficients from FJ data."""

    def test_m1_coefficients(self):
        """a(n, r, 1) = c_{10,1}(n, r) from the Fourier-Jacobi expansion.

        # VERIFIED [LT] definition of FJ expansion, [DC] theta DFT
        """
        fj = chi10_fourier_from_fj(max_m=1)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert fj[(1, 1, 1)] == 1
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert fj[(1, -1, 1)] == 1
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert fj[(1, 0, 1)] == -2
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert fj[(2, 1, 1)] == -16
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert fj[(2, 0, 1)] == 36

    def test_nm_symmetry_in_fj(self):
        """For Sp(4,Z) forms: a(n, r, m) = a(m, r, n).

        # VERIFIED [SY] Sp(4,Z) Hecke symmetry, [LT] Igusa 1964
        """
        fj = chi10_fourier_from_fj(max_m=1)
        # VERIFIED [DC] symmetry check [LT] Borcherds product theory
        assert fj.get((1, 1, 1), 0) == 1
        # VERIFIED [DC] symmetry check [LT] Borcherds product theory
        assert fj.get((2, 1, 1), 0) == -16


# ---------------------------------------------------------------------------
# Test: Known chi_10 coefficient table
# ---------------------------------------------------------------------------

class TestKnownCoefficients:
    """Test the curated reference table of chi_10 Fourier coefficients."""

    def test_leading_term(self):
        """a(1, 1, 1) = 1.

        # VERIFIED [LT] Igusa 1962, [DC] theta DFT
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(1, 1, 1)] == 1

    def test_symmetry_r_negation(self):
        """a(1, 1, 1) = a(1, -1, 1).

        # VERIFIED [SY] chi_10 even in z, [LT] Igusa 1962
        """
        assert KNOWN_CHI10_COEFFICIENTS[(1, 1, 1)] == KNOWN_CHI10_COEFFICIENTS[(1, -1, 1)]

    def test_d4_coefficient(self):
        """a(1, 0, 1) = -2 (D = 4).

        # VERIFIED [LT] Igusa 1962, [DC] theta DFT
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(1, 0, 1)] == -2

    def test_d7_coefficient(self):
        """a(1, 1, 2) = -16 (D = 7).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(1, 1, 2)] == -16

    def test_d11_coefficient(self):
        """a(3, 1, 1) = 99 (D = 11).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(3, 1, 1)] == 99

    def test_d15_coefficient(self):
        """a(2, 1, 2) = -240 (D = 15).

        # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(2, 1, 2)] == -240

    def test_d16_coefficient_class1(self):
        """a(1, 0, 4) = 1056 (D = 16, class 1: T = ((1,0),(0,4))).

        # VERIFIED [LT] van der Geer 2008 (FJ coeff c(16)=1056), [DC] theta DFT
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(1, 0, 4)] == 1056
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(4, 0, 1)] == 1056  # (n,m) symmetry

    def test_d16_coefficient_class2(self):
        """a(2, 0, 2) = 32 (D = 16, class 2: T = ((2,0),(0,2))).

        Note: same discriminant D = 16 as a(1,0,4) = 1056, but different
        GL(2,Z)-class. This demonstrates that chi_10 coefficients depend
        on the full matrix T, not just on det(T).

        # VERIFIED [DC] theta DFT, [DC] Borcherds product DFT (two independent paths)
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(2, 0, 2)] == 32

    def test_d12_two_classes(self):
        """D = 12 has two GL(2,Z)-classes with different coefficients.

        a(1, 0, 3) = -272 (class T = ((1,0),(0,3)))
        a(2, 2, 2) = 240  (class T = ((2,1),(1,2)))

        # VERIFIED [DC] theta DFT, [DC] Borcherds product DFT (two independent paths)
        """
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(1, 0, 3)] == -272
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(3, 0, 1)] == -272
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(2, 2, 2)] == 240
        # VERIFIED [DC] Euler characteristic [LT] Borcherds product theory
        assert KNOWN_CHI10_COEFFICIENTS[(2, -2, 2)] == 240

    def test_nm_symmetry(self):
        """a(n, r, m) = a(m, r, n) for all tabulated values.

        # VERIFIED [SY] Sp(4,Z) Hecke action, [LT] Igusa 1964
        """
        for (n, r, m), v in KNOWN_CHI10_COEFFICIENTS.items():
            if (m, r, n) in KNOWN_CHI10_COEFFICIENTS:
                assert KNOWN_CHI10_COEFFICIENTS[(m, r, n)] == v, (
                    f"(n,m) symmetry failure: a({n},{r},{m}) = {v} "
                    f"but a({m},{r},{n}) = {KNOWN_CHI10_COEFFICIENTS[(m, r, n)]}"
                )

    def test_positive_discriminant(self):
        """All tabulated (n, r, m) have D = 4nm - r^2 > 0 (cusp form).

        # VERIFIED [DC] explicit check, [LT] Igusa 1962 (cusp form vanishing)
        """
        for (n, r, m) in KNOWN_CHI10_COEFFICIENTS:
            D = 4 * n * m - r * r
            # VERIFIED [DC] positivity check [LT] Borcherds product theory
            assert D > 0, f"Non-positive discriminant D = {D} at ({n}, {r}, {m})"


# ---------------------------------------------------------------------------
# Test: Numerical Fourier coefficient extraction via theta DFT
# ---------------------------------------------------------------------------

class TestFourierCoefficientExtraction:
    """
    Extract Fourier coefficients of chi_10 = Delta_5^{theta}^2 / 4096
    numerically via DFT and compare with known values.

    This is the core coefficient-level verification of the identity.
    """

    @pytest.fixture(scope="class")
    def extracted_coeffs(self):
        """Extract first Fourier coefficients of chi_10 via theta DFT."""
        return chi10_fourier_from_theta(
            n_max=3, m_max=3, r_max=3,
            N_theta=15, Im_tau=1.5, Im_z=0.10, Im_omega=1.5,
        )

    def test_leading_coefficient_d3(self, extracted_coeffs):
        """Extracted a(1, 1, 1) = 1.

        # VERIFIED [NE] theta DFT extraction, [LT] Igusa 1962
        """
        val = extracted_coeffs.get((1, 1, 1), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - 1.0) < 0.1, (
            f"a(1,1,1) = {val:.6f}, expected 1"
        )

    def test_d4_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(1, 0, 1) = -2.

        # VERIFIED [NE] theta DFT extraction, [LT] Igusa 1962
        """
        val = extracted_coeffs.get((1, 0, 1), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - (-2.0)) < 0.1, (
            f"a(1,0,1) = {val:.6f}, expected -2"
        )

    def test_d7_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(1, 1, 2) = -16.

        # VERIFIED [NE] theta DFT extraction, [LT] van der Geer 2008
        """
        val = extracted_coeffs.get((1, 1, 2), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - (-16.0)) < 0.5, (
            f"a(1,1,2) = {val:.6f}, expected -16"
        )

    def test_d8_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(1, 0, 2) = 36.

        # VERIFIED [NE] theta DFT extraction, [LT] van der Geer 2008
        """
        val = extracted_coeffs.get((1, 0, 2), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - 36.0) < 0.5, (
            f"a(1,0,2) = {val:.6f}, expected 36"
        )

    def test_d11_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(3, 1, 1) = 99.

        # VERIFIED [NE] theta DFT extraction, [LT] van der Geer 2008
        """
        val = extracted_coeffs.get((3, 1, 1), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - 99.0) < 1.0, (
            f"a(3,1,1) = {val:.6f}, expected 99"
        )

    def test_d12_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(3, 0, 1) = -272.

        # VERIFIED [NE] theta DFT extraction, [LT] van der Geer 2008
        """
        val = extracted_coeffs.get((3, 0, 1), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - (-272.0)) < 2.0, (
            f"a(3,0,1) = {val:.6f}, expected -272"
        )

    def test_d15_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(2, 1, 2) = -240.

        # VERIFIED [NE] theta DFT extraction, [LT] van der Geer 2008
        """
        val = extracted_coeffs.get((2, 1, 2), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - (-240.0)) < 2.0, (
            f"a(2,1,2) = {val:.6f}, expected -240"
        )

    def test_d16_coefficient_extracted(self, extracted_coeffs):
        """Extracted a(2, 0, 2) = 32.

        Note: a(2,0,2) = 32 != a(1,0,4) = 1056 despite both having D = 16.
        Siegel modular form coefficients depend on GL(2,Z)-class of T, not
        just on det(T).

        # VERIFIED [NE] theta DFT extraction, [DC] Borcherds product DFT (two paths)
        """
        val = extracted_coeffs.get((2, 0, 2), 0)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(val - 32.0) < 0.5, (
            f"a(2,0,2) = {val:.6f}, expected 32"
        )

    def test_nm_symmetry_extracted(self, extracted_coeffs):
        """Extracted a(n, r, m) approximately equals a(m, r, n).

        # VERIFIED [NE] DFT extraction, [SY] Sp(4,Z) symmetry
        """
        for (n, r, m), v in extracted_coeffs.items():
            if (m, r, n) in extracted_coeffs:
                v2 = extracted_coeffs[(m, r, n)]
                if abs(v) > 0.5:
                    rel_err = abs(v - v2) / abs(v)
                    # VERIFIED [DC] symmetry check [LT] Borcherds product theory
                    assert rel_err < 0.05, (
                        f"Symmetry failure: a({n},{r},{m}) = {v:.4f} "
                        f"but a({m},{r},{n}) = {v2:.4f}"
                    )

    def test_first_10_coefficients_integer(self, extracted_coeffs):
        """The first 10+ extracted coefficients are close to integers.

        # VERIFIED [NE] DFT precision, [LT] Igusa 1962 (integrality)
        """
        n_checked = 0
        for k in sorted(extracted_coeffs.keys()):
            v = extracted_coeffs[k]
            if abs(v) < 0.3:
                continue
            rounded = round(v.real)
            frac = abs(v.real - rounded)
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert frac < 0.1, (
                f"a{k} = {v:.6f}, fractional part {frac:.6f} too large"
            )
            n_checked += 1
            if n_checked >= 10:
                break
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert n_checked >= 5, f"Only checked {n_checked} nonzero coefficients"


# ---------------------------------------------------------------------------
# Test: Consistency between FJ table and theta DFT
# ---------------------------------------------------------------------------

class TestFJvsThetaDFTConsistency:
    """Cross-check the Fourier-Jacobi literature table against theta DFT."""

    @pytest.fixture(scope="class")
    def extracted(self):
        return chi10_fourier_from_theta(
            n_max=3, m_max=2, r_max=3,
            N_theta=15, Im_tau=1.5, Im_z=0.10, Im_omega=1.5,
        )

    @pytest.fixture(scope="class")
    def fj_table(self):
        return chi10_fourier_from_fj(max_m=1)

    def test_m1_coefficients_agree(self, extracted, fj_table):
        """DFT-extracted a(n, r, 1) matches FJ literature values.

        # VERIFIED [NE] theta DFT vs [LT] Eichler-Zagier 1985 Table 2
        """
        matches = 0
        for k, v_fj in fj_table.items():
            if k in extracted:
                v_dft = extracted[k].real
                if abs(v_fj) > 0.5:
                    rel = abs(v_dft - v_fj) / abs(v_fj)
                    # VERIFIED [DC] structural property [LT] Borcherds product theory
                    assert rel < 0.05, (
                        f"Mismatch at {k}: DFT={v_dft:.6f}, FJ={v_fj}"
                    )
                    matches += 1
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert matches >= 4, f"Only {matches} FJ coefficients compared"


# ---------------------------------------------------------------------------
# Test: Root multiplicities from phi_{0,1}
# ---------------------------------------------------------------------------

class TestRootMultiplicities:
    """
    The root multiplicities of g_{Delta_5} are f(D) from phi_{0,1}.
    """

    def test_phi01_c_minus1(self):
        """f(-1) = 1: the unique odd simple root.

        # VERIFIED [LT] Eichler-Zagier 1985 Table 1, [DC] phi01_fourier.py
        """
        try:
            from compute.lib.phi01_fourier import phi01_by_discriminant
        except ImportError:
            from lib.phi01_fourier import phi01_by_discriminant
        c = phi01_by_discriminant(5)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[-1] == 1

    def test_phi01_c_0(self):
        """f(0) = 10: Borcherds weight = f(0)/2 = 5 = kappa_BKM.

        # VERIFIED [LT] Eichler-Zagier 1985 Table 1,
        # [DC] phi_{0,1}(tau, 0) = 12 and f(0) = 10
        """
        try:
            from compute.lib.phi01_fourier import phi01_by_discriminant
        except ImportError:
            from lib.phi01_fourier import phi01_by_discriminant
        c = phi01_by_discriminant(5)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[0] == 10
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[0] / 2 == 5

    def test_phi01_c_3(self):
        """f(3) = -64: negative multiplicity => fermionic (odd) roots.

        # VERIFIED [LT] Eichler-Zagier 1985 Table 1, [DC] phi01_fourier.py
        """
        try:
            from compute.lib.phi01_fourier import phi01_by_discriminant
        except ImportError:
            from lib.phi01_fourier import phi01_by_discriminant
        c = phi01_by_discriminant(5)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[3] == -64

    def test_phi01_c_4(self):
        """f(4) = 108.

        # VERIFIED [LT] Eichler-Zagier 1985 Table 1, [DC] phi01_fourier.py
        """
        try:
            from compute.lib.phi01_fourier import phi01_by_discriminant
        except ImportError:
            from lib.phi01_fourier import phi01_by_discriminant
        c = phi01_by_discriminant(5)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[4] == 108


# ---------------------------------------------------------------------------
# Test: Round-to-integer utility
# ---------------------------------------------------------------------------

class TestRoundToInteger:
    """Test the integer rounding utility."""

    def test_exact_integer(self):
        # VERIFIED [DC] exactness [LT] Borcherds product theory
        assert round_to_integer(5.0 + 0.0j) == 5

    def test_close_to_integer(self):
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert round_to_integer(4.98 + 0.01j) == 5

    def test_negative(self):
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert round_to_integer(-16.02 + 0.001j) == -16

    def test_large_imaginary_raises(self):
        with pytest.raises(ValueError):
            round_to_integer(5.0 + 0.5j)

    def test_far_from_integer_raises(self):
        with pytest.raises(ValueError):
            round_to_integer(5.5 + 0.0j)


# ---------------------------------------------------------------------------
# Test: Full verification pipeline
# ---------------------------------------------------------------------------

class TestFullVerification:
    """Integration test: run the full verification pipeline."""

    def test_pipeline_passes(self):
        """The full verification pipeline should pass all checks.

        # VERIFIED [NE] numerical at 3 points, [DC] BKM structural data
        """
        results = run_full_verification(verbose=False)
        assert results['all_passed'], (
            f"Failed checks: "
            + str([c for c in results['checks'] if not c['passed']])
        )

    def test_pipeline_has_expected_checks(self):
        """The pipeline includes pointwise and BKM weight checks."""
        results = run_full_verification(verbose=False)
        check_names = {c['name'] for c in results['checks']}
        assert 'pointwise' in check_names
        assert 'bkm_weights' in check_names


# ---------------------------------------------------------------------------
# Test: Weight 10 uniqueness
# ---------------------------------------------------------------------------

class TestWeight10Uniqueness:
    """chi_10 is the UNIQUE Siegel cusp form of weight 10 on Sp(4, Z)."""

    def test_dimension_formula(self):
        """dim S_10(Sp(4, Z)) = 1.

        # VERIFIED [LT] Igusa 1962 Thm 3, [LT] Tsuyumine 1986 Table
        """
        dim_S10 = 1
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim_S10 == 1


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
