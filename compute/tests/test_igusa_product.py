"""
Tests for the Borcherds product formula for the Igusa cusp form Delta_5.

Verifies:
1. Fourier coefficients f(D) of the weak Jacobi form phi_{0,1}
2. The Borcherds infinite product matches Delta_5 (via theta constants)
3. The key identity: 1 + (1/64)*sum f(1+2t,1,1)*q^t = prod (1-q^k)^9

All numerical agreements are checked to at least 10 digits where possible.
"""

import numpy as np
import pytest

from compute.lib.igusa_product_formula import (
    compute_f_disc,
    f_coeff,
    phi_01_numerical,
    borcherds_product,
    delta5_theta,
    verify_product_formula,
    verify_eta9_identity,
    _even_theta_characteristics,
    _eta_power_series,
)


# ---------------------------------------------------------------------------
# Tests for phi_{0,1} Fourier coefficients
# ---------------------------------------------------------------------------

class TestPhi01Coefficients:
    """Test the Fourier coefficients f(D) of the weak Jacobi form phi_{0,1}."""

    @pytest.fixture(scope="class")
    def f_table(self):
        """Compute f(D) table once for all tests (auto-precision)."""
        return compute_f_disc(60)

    def test_known_coefficients(self, f_table):
        """
        Verify f(D) against the known values from the paper and
        Eichler-Zagier tables.

        phi_{0,1} = (r^{-1} + 10 + r) + q*(10r^{-2} - 64r^{-1} + 108 - 64r + 10r^2) + ...
        """
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_table[-1] == 1,   f"f(-1) = {f_table[-1]}, expected 1"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_table[0]  == 10,  f"f(0) = {f_table[0]}, expected 10"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_table[3]  == -64, f"f(3) = {f_table[3]}, expected -64"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_table[4]  == 108, f"f(4) = {f_table[4]}, expected 108"

    def test_d_dependence_only(self, f_table):
        """
        The coefficient f(n, l) depends only on D = 4n - l^2.
        This is verified implicitly by compute_f_disc (which raises
        ValueError on inconsistency), but we double-check some cases.
        """
        # f(0, 1) and f(0, -1) both have D = -1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_coeff(0, 1) == f_coeff(0, -1) == 1

        # f(1, 0) has D=4, f(2, 2) has D=4*2-4=4
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_coeff(1, 0) == f_coeff(2, 2) == 108

        # f(1, 1) and f(1, -1) both have D=3
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_coeff(1, 1) == f_coeff(1, -1) == -64

    def test_vanishing_for_d_below_minus_one(self):
        """f(n, l) = 0 when 4n - l^2 < -1."""
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert f_coeff(0, 2) == 0   # D = -4
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert f_coeff(0, 3) == 0   # D = -9
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert f_coeff(1, 3) == 0   # D = 4 - 9 = -5
        # VERIFIED [DC] vanishing check [LC] boundary/limiting case
        assert f_coeff(0, 10) == 0  # D = -100

    def test_sum_over_l_vanishes(self, f_table):
        """
        Consistency check: sum_{l} f(n, l) = 0 for all n >= 1.

        This follows from phi_{0,1}(tau, 0) = 12 being independent of tau,
        so only the n=0 term contributes.
        """
        for n in range(1, 5):
            l_max = int(np.sqrt(4 * n + 1)) + 1
            total = sum(f_coeff(n, l) for l in range(-l_max, l_max + 1))
            # VERIFIED [DC] vanishing check [LC] boundary/limiting case
            assert total == 0, f"sum_l f({n}, l) = {total}, expected 0"

    def test_phi01_at_z_zero(self):
        """phi_{0,1}(tau, 0) = 12 for any tau in the upper half-plane."""
        for tau in [1j, 0.3 + 2j, 0.5 + 1j]:
            val = phi_01_numerical(tau, 0, N_terms=80)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(val - 12.0) < 1e-10, \
                f"phi_01(tau={tau}, 0) = {val}, expected 12"

    def test_phi01_direct_expansion(self):
        """
        Verify phi_{0,1}(tau, z) against its direct q,r-expansion
        at a specific point with large Im(tau).
        """
        tau = 3j  # |q| = exp(-6*pi) ~ 5.2e-9
        z = 0.25
        q = np.exp(2j * np.pi * tau)
        r = np.exp(2j * np.pi * z)

        # Direct expansion (n=0 and n=1 terms):
        direct = ((1/r + 10 + r)
                  + q * (10/r**2 - 64/r + 108 - 64*r + 10*r**2))

        numerical = phi_01_numerical(tau, z, N_terms=80)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(numerical - direct) < 1e-6, \
            f"|phi_01 - direct| = {abs(numerical - direct):.2e}"

    def test_higher_coefficients(self, f_table):
        """
        Verify f(D=7) = -513.

        This is the correct value (not -512): the consistency check
        sum_l f(n,l) = 0 for n=2 requires exactly -513:
            f(2,0) + 2*f(2,1) + 2*f(2,2) + 2*f(2,3) = 808 - 2*513 + 2*108 + 2*1 = 0
        """
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_table[7] == -513, f"f(7) = {f_table[7]}, expected -513"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_table[8] == 808,  f"f(8) = {f_table[8]}, expected 808"


# ---------------------------------------------------------------------------
# Tests for genus-2 theta constants and Delta_5
# ---------------------------------------------------------------------------

class TestDelta5Theta:
    """Test the computation of Delta_5 via genus-2 theta constants."""

    def test_ten_even_characteristics(self):
        """There are exactly 10 even theta characteristics for genus 2."""
        chars = _even_theta_characteristics()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(chars) == 10

    def test_delta5_symmetry(self):
        """
        Delta_5 is invariant under z1 <-> z3 (transposition of the
        diagonal elements of Z).
        """
        z1, z2, z3 = 0.1 + 2j, 0.05 + 0.2j, 0.3 + 1.8j
        d5_original = delta5_theta(z1, z2, z3, N_terms=20)
        d5_swapped = delta5_theta(z3, z2, z1, N_terms=20)
        # VERIFIED [DC] symmetry check [LC] boundary/limiting case
        assert abs(d5_original - d5_swapped) / abs(d5_original) < 1e-10, \
            "Delta_5 should be symmetric under z1 <-> z3"

    def test_delta5_vanishes_on_diagonal(self):
        """
        Delta_5 vanishes on the diagonal locus z2 = 0.
        This follows because Delta_5 is the unique (up to scalar) Siegel
        cusp form of weight 5 with its multiplier, vanishing exactly on
        Sp_4(Z)-translates of the diagonal.
        """
        z1 = 0.3 + 1.5j
        z3 = 0.2 + 1.8j
        d5_diag = delta5_theta(z1, 0, z3, N_terms=25)
        d5_gen = delta5_theta(z1, 0.1 + 0.15j, z3, N_terms=25)
        if abs(d5_gen) > 1e-30:
            # VERIFIED [DC] vanishing check [LC] boundary/limiting case
            assert abs(d5_diag) / abs(d5_gen) < 1e-8, \
                f"|Delta_5(diag)| / |Delta_5(gen)| = {abs(d5_diag)/abs(d5_gen):.2e}"

    def test_delta5_nonzero_generic(self):
        """Delta_5 is nonzero at a generic point."""
        d5 = delta5_theta(2j, 0.1j, 2j, N_terms=20)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(d5) > 1e-10, f"|Delta_5| = {abs(d5):.2e}, expected nonzero"


# ---------------------------------------------------------------------------
# Tests for the Borcherds product formula
# ---------------------------------------------------------------------------

class TestBorcherdsProduct:
    """
    Test the Borcherds product identity:
        |(1/64) * Delta_5(Z)| = |Borcherds product|

    The identity holds up to a global sign (ratio = -1), which is a
    branch-of-log convention for the Borcherds product of a GKM
    superalgebra. We verify |ratio| = 1 to high precision.
    """

    @pytest.mark.parametrize("z1,z2,z3", [
        (2.0j, 0.1j, 2.0j),
        (0.1 + 2j, 0.05 + 0.3j, 0.15 + 2j),
        (0.3 + 1.5j, 0.1 - 0.1j, 0.2 + 1.7j),
    ])
    def test_product_formula_abs_agreement(self, z1, z2, z3):
        """
        Verify |(1/64)*Delta_5| = |Borcherds product| to at least 10 digits.
        """
        result = verify_product_formula(
            z1, z2, z3, N_prod=12, N_theta=25, D_max=80
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['abs_relative_error'] < 1e-10, \
            (f"Abs relative error = {result['abs_relative_error']:.2e} "
             f"at z1={z1}, z2={z2}, z3={z3}")

    def test_product_formula_deep_cusp(self):
        """
        At the deep cusp point (large Im), both sides converge very fast.
        """
        result = verify_product_formula(
            2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['abs_relative_error'] < 1e-12, \
            f"Deep cusp abs error = {result['abs_relative_error']:.2e}"

    def test_product_formula_generic_point(self):
        """
        Verify at a generic point with nonzero real parts.
        """
        z1 = 0.2 + 1.3j
        z2 = 0.1 + 0.15j
        z3 = 0.25 + 1.4j
        result = verify_product_formula(
            z1, z2, z3, N_prod=15, N_theta=30, D_max=120
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['abs_relative_error'] < 1e-6, \
            f"Generic point abs error = {result['abs_relative_error']:.2e}"

    def test_product_consistent_sign(self):
        """
        The ratio (1/64)*Delta_5 / BP is consistently -1 at all test points.
        This sign arises from the Borcherds product for the GKM superalgebra
        structure of the automorphic correction algebra.
        """
        test_points = [
            (2j, 0.1j, 2j),
            (0.1 + 2j, 0.05 + 0.3j, 0.15 + 2j),
            (0.3 + 1.5j, 0.1 - 0.1j, 0.2 + 1.7j),
        ]
        for z1, z2, z3 in test_points:
            result = verify_product_formula(
                z1, z2, z3, N_prod=12, N_theta=25, D_max=80
            )
            ratio = result['lhs_over_rhs']
            # VERIFIED [DC] consistency check [LC] boundary/limiting case
            assert abs(ratio + 1) < 1e-8, \
                f"Expected ratio ~ -1, got {ratio} at ({z1},{z2},{z3})"


# ---------------------------------------------------------------------------
# Tests for the eta^9 identity
# ---------------------------------------------------------------------------

class TestEta9Identity:
    """
    Test the identity:
        1 + (1/64)*sum_{t>=1} f(1+2t,1,1)*q^t = prod_{k>=1} (1-q^k)^9

    Verified by extracting the (l=1, m=1) Fourier-Jacobi sector of
    Delta_5 via DFT in the z2 variable, then comparing with eta(tau)^9.
    """

    def test_eta9_identity_numerical(self):
        """
        Verify the identity at several tau values. The agreement is
        limited by the l=3 contamination from the DFT extraction.
        """
        result = verify_eta9_identity(N_terms=50)
        for r in result['test_results']:
            abs_ratio = abs(r['ratio'])
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(abs_ratio - 1.0) < 1e-3, \
                (f"eta^9 identity: |ratio| = {abs_ratio:.6f} at tau={r['tau']}, "
                 f"expected ~1.0 (rel err = {abs(abs_ratio - 1.0):.2e})")

    def test_eta_power_series_first_coefficients(self):
        """
        prod_{k>=1} (1-q^k)^9 = 1 - 9q + 27q^2 - 12q^3 + ...
        """
        c = _eta_power_series(9, 10)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c[0] == 1.0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c[1] == -9.0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c[2] == 27.0

    def test_eta9_via_direct_evaluation(self):
        """
        Compare prod_{k=1}^N (1-q^k)^9 (direct) with the power series
        at a specific q value. Agreement to 10+ digits.
        """
        tau = 0.3 + 1j
        q = np.exp(2j * np.pi * tau)

        product = 1.0 + 0.0j
        for k in range(1, 80):
            product *= (1.0 - q**k)**9

        coeffs = _eta_power_series(9, 80)
        series = sum(coeffs[n] * q**n for n in range(len(coeffs)))

        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(product - series) / abs(product) < 1e-10, \
            f"eta^9 product vs series: rel error = {abs(product-series)/abs(product):.2e}"


# ---------------------------------------------------------------------------
# Integration test: full pipeline
# ---------------------------------------------------------------------------

class TestFullPipeline:
    """End-to-end tests combining all components."""

    def test_phi01_times_delta12_gives_phi12(self):
        """
        Verify phi_{12,1} = phi_{0,1} * Delta_{12} by checking Fourier
        coefficients. The first few Fourier coefficients of phi_{12,1}
        are given in the paper:

            phi_{12,1} = (r^{-1} + 10 + r)*q
                       + (10r^{-2} - 88r^{-1} - 132 - 88r + 10r^2)*q^2 + ...
        """
        tau_ram = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830}

        # n=1: c_{12}(1, l) = f(0, l) * tau(1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_coeff(0, 0) * tau_ram[1] == 10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_coeff(0, 1) * tau_ram[1] == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_coeff(0, -1) * tau_ram[1] == 1

        # n=2: c_{12}(2, l) = f(1, l)*tau(1) + f(0, l)*tau(2)
        c12_2_0 = f_coeff(1, 0) * tau_ram[1] + f_coeff(0, 0) * tau_ram[2]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c12_2_0 == -132, f"c_12(2, 0) = {c12_2_0}, expected -132"

        c12_2_1 = f_coeff(1, 1) * tau_ram[1] + f_coeff(0, 1) * tau_ram[2]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c12_2_1 == -88, f"c_12(2, 1) = {c12_2_1}, expected -88"

        c12_2_2 = f_coeff(1, 2) * tau_ram[1] + f_coeff(0, 2) * tau_ram[2]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert c12_2_2 == 10, f"c_12(2, 2) = {c12_2_2}, expected 10"

    def test_borcherds_and_eta9_consistent(self):
        """
        Both the Borcherds product and the eta^9 identity derive from
        the same formula. Verify consistent sign convention.
        """
        z1, z2, z3 = 2j, 0.1j, 2j
        d5 = delta5_theta(z1, z2, z3, N_terms=20)
        bp = borcherds_product(z1, z2, z3, N_prod=12, D_max=80)
        ratio_borcherds = (d5 / 64.0) / bp

        result = verify_eta9_identity(N_terms=50)
        ratio_eta9 = result['test_results'][0]['ratio']

        # Both should be approximately -1
        # VERIFIED [DC] consistency check [LC] boundary/limiting case
        assert abs(ratio_borcherds + 1) < 1e-10, \
            f"Borcherds ratio = {ratio_borcherds}"
        # VERIFIED [DC] consistency check [LC] boundary/limiting case
        assert abs(abs(ratio_eta9) - 1) < 1e-3, \
            f"eta^9 |ratio| = {abs(ratio_eta9)}"


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
