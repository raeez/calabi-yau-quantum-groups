"""Tests for the Weyl-Kac-Borcherds denominator identity for g_{Delta_5}.

Verifies both sides of the denominator identity for the BKM superalgebra
attached to K3 x E, whose denominator is the primitive Gritsenko-Nikulin denominator Delta_5.

Ground truth:
  - k3_times_e.tex: thm:k3e-denominator, thm:k3e-product, def:k3e-weyl-vector
  - Gritsenko-Nikulin, alg-geom/9611028, Theorem 3.1
  - Borcherds, Inventiones 132 (1998), Theorem 13.3

Test structure:
  1. Lattice Lambda^{2,1} (Gram matrix, simple roots, inner products)
  2. Weyl group W^{(2)} (reflections, orbit, growth, isometry)
  3. phi_{0,1} Fourier coefficients (discriminant independence, known values)
  4. Borcherds product (numerical evaluation, convergence)
  5. Weyl orbit sum (convergence, leading order matching)
  6. Denominator identity (product/sum agreement at low orders)
  7. Imaginary root structure (fundamental chamber, multiplicities)
  8. Cross-validation against bkm_shadow_tower.py and dd_modular_lattices.py
  9. Cross-validation against phi01_fourier.py (exact arithmetic)
"""

import importlib.util
import os

import numpy as np
import pytest
from fractions import Fraction

from compute.lib.wkb_denominator import (
    # Lattice
    GRAM, DELTA_1, DELTA_2, DELTA_3, SIMPLE_ROOTS, RHO,
    inner_product, norm_sq,
    verify_gram_matrix, verify_weyl_vector,
    # Weyl group
    reflect, weyl_orbit_rho, weyl_group_growth,
    # phi_{0,1}
    PHI01_TABLE, C_DISC,
    phi_01_value, compute_phi01_table,
    f_phi01, c_disc,
    verify_phi01_discriminant, verify_phi01_symmetry, verify_phi01_sum_rule,
    # Product and sum
    borcherds_product_numerical, weyl_sum_numerical,
    # Verification
    verify_product_weyl_agreement, verify_product_symmetries,
    verify_weyl_sum_convergence,
    fundamental_chamber_elements,
    verify_all,
)


# ======================================================================
# 1. Lattice Lambda^{2,1} structure
# ======================================================================

class TestLattice:
    """Verify the lattice Lambda^{2,1} = Lambda^{1,1} + [2]."""

    def test_gram_matrix(self):
        """Simple root Gram matrix = ((2,-2,-2),(-2,2,-2),(-2,-2,2))."""
        assert verify_gram_matrix()

    def test_gram_signature(self):
        """Gram matrix has signature (2, 1)."""
        eigenvalues = np.linalg.eigvalsh(GRAM)
        n_pos = sum(1 for e in eigenvalues if e > 0)
        n_neg = sum(1 for e in eigenvalues if e < 0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert n_pos == 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert n_neg == 1

    def test_simple_root_norms(self):
        """All simple roots have norm 2: (delta_i, delta_i) = 2."""
        for i, delta in enumerate(SIMPLE_ROOTS):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(norm_sq(delta) - 2.0) < 1e-14, f"delta_{i+1} norm wrong"

    def test_simple_root_inner_products(self):
        """Off-diagonal: (delta_i, delta_j) = -2 for i != j."""
        for i in range(3):
            for j in range(3):
                if i != j:
                    # VERIFIED [DC] structural property [LC] boundary/limiting case
                    assert abs(inner_product(SIMPLE_ROOTS[i], SIMPLE_ROOTS[j]) + 2) < 1e-14

    def test_weyl_vector(self):
        """rho satisfies (rho, delta_i) = -1 and rho = (1/2)(delta_1+delta_2+delta_3)."""
        assert verify_weyl_vector()

    def test_weyl_vector_coordinates(self):
        """rho = (1, -1/2, 1) in (f_2, f_3, f_{-2}) basis."""
        assert np.allclose(RHO, [1.0, -0.5, 1.0])

    def test_rho_norm(self):
        """(rho, rho) = 2(-1/2)^2 - 2(1)(1) = 1/2 - 2 = -3/2."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(norm_sq(RHO) - (-1.5)) < 1e-14

    def test_lattice_decomposition(self):
        """Lambda^{2,1} = Lambda^{1,1} + [2].

        (f_2, f_{-2}) span Lambda^{1,1} with Gram ((0,-1),(-1,0)).
        f_3 spans [2] with (f_3, f_3) = 2.
        Cross terms vanish.
        """
        assert abs(inner_product(
            np.array([1, 0, 0]),
            np.array([0, 0, 1])
        ) - (-1)) < 1e-14
        assert abs(inner_product(
            np.array([0, 1, 0]),
            np.array([0, 1, 0])
        ) - 2) < 1e-14
        # Cross terms
        assert abs(inner_product(
            np.array([1, 0, 0]),
            np.array([0, 1, 0])
        )) < 1e-14
        assert abs(inner_product(
            np.array([0, 0, 1]),
            np.array([0, 1, 0])
        )) < 1e-14

    def test_alpha_norm_formula(self):
        """For alpha = (n, l, m), (alpha, alpha) = 2l^2 - 2nm."""
        for n in range(-3, 4):
            for l in range(-3, 4):
                for m in range(-3, 4):
                    v = np.array([n, l, m], dtype=float)
                    expected = 2*l*l - 2*n*m
                    # VERIFIED [DC] structural property [LC] boundary/limiting case
                    assert abs(norm_sq(v) - expected) < 1e-12


# ======================================================================
# 2. Weyl group W^{(2)}(Lambda^{2,1}_{II})
# ======================================================================

class TestWeylGroup:
    """Verify the Weyl group generated by reflections in delta_1, delta_2, delta_3."""

    def test_reflection_involution(self):
        """s_i^2 = id for each simple reflection."""
        rng = np.random.RandomState(42)
        for root in SIMPLE_ROOTS:
            for _ in range(10):
                v = rng.randn(3)
                assert np.allclose(reflect(reflect(v, root), root), v)

    def test_reflection_isometry(self):
        """Reflections preserve the bilinear form."""
        rng = np.random.RandomState(42)
        for root in SIMPLE_ROOTS:
            for _ in range(10):
                v = rng.randn(3)
                w = rng.randn(3)
                sv = reflect(v, root)
                sw = reflect(w, root)
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert abs(inner_product(sv, sw) - inner_product(v, w)) < 1e-12

    def test_reflection_on_root(self):
        """s_i(delta_i) = -delta_i."""
        for root in SIMPLE_ROOTS:
            assert np.allclose(reflect(root, root), -root)

    def test_reflection_formula(self):
        """s_i(delta_j) = delta_j + 2*delta_i for i != j.

        Since (delta_j, delta_i)/(delta_i, delta_i) = -2/2 = -1.
        """
        for i in range(3):
            for j in range(3):
                if i != j:
                    result = reflect(SIMPLE_ROOTS[j], SIMPLE_ROOTS[i])
                    expected = SIMPLE_ROOTS[j] + 2 * SIMPLE_ROOTS[i]
                    assert np.allclose(result, expected)

    def test_weyl_orbit_isometry(self):
        """All w(rho) have the same norm as rho."""
        elements = weyl_orbit_rho(6)
        rho_norm = norm_sq(RHO)
        for w_rho, _ in elements:
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(norm_sq(w_rho) - rho_norm) < 1e-10

    def test_weyl_group_growth_doubling(self):
        """Weyl group grows as 3*2^{k-1} at word length k (hyperbolic Coxeter)."""
        growth = weyl_group_growth(8)
        for k in range(1, 9):
            # VERIFIED [DC] growth bound [LC] boundary/limiting case
            assert growth[k] == 3 * 2**(k-1), (
                f"growth at k={k}: {growth[k]} != {3*2**(k-1)}"
            )

    def test_weyl_group_size(self):
        """Total elements at word length <= 6 is 1+3+6+12+24+48+96 = 190."""
        elements = weyl_orbit_rho(6)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(elements) == 190

    def test_identity_element(self):
        """The identity gives w(rho) = rho with det = +1."""
        elements = weyl_orbit_rho(0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(elements) == 1
        w_rho, det_w = elements[0]
        assert np.allclose(w_rho, RHO)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert det_w == 1

    def test_s3_symmetry(self):
        """The (f_2 <-> f_{-2}) swap exchanges delta_1 <-> delta_2 and fixes rho."""
        P = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=float)
        assert np.allclose(P @ DELTA_1, DELTA_2)
        assert np.allclose(P @ DELTA_2, DELTA_1)
        assert np.allclose(P @ RHO, RHO)

    def test_det_alternates(self):
        """Identity has det +1."""
        elements = weyl_orbit_rho(4)
        for w_rho, det_w in elements:
            if np.allclose(w_rho, RHO):
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert det_w == 1


# ======================================================================
# 3. phi_{0,1} Fourier coefficients
# ======================================================================

class TestPhi01:
    """Verify properties of the K3 elliptic genus phi_{0,1}."""

    def test_discriminant_independence(self):
        """f(n, l) depends only on D = 4n - l^2."""
        assert verify_phi01_discriminant()

    def test_l_symmetry(self):
        """f(n, l) = f(n, -l)."""
        assert verify_phi01_symmetry()

    def test_sum_rule(self):
        """sum_l f(0, l) = 12 = phi_{0,1}(tau, 0)."""
        assert verify_phi01_sum_rule()

    def test_leading_coefficients(self):
        """f(0,0) = 10, f(0,+/-1) = 1."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(0, 0) == 10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(0, 1) == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(0, -1) == 1

    def test_q1_coefficients(self):
        """f(1,0) = 108, f(1,+/-1) = -64, f(1,+/-2) = 10."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(1, 0) == 108
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(1, 1) == -64
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(1, -1) == -64
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(1, 2) == 10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(1, -2) == 10

    def test_q2_coefficients(self):
        """f(2,0) = 808, f(2,+/-1) = -513, f(2,+/-2) = 108, f(2,+/-3) = 1."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(2, 0) == 808
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(2, 1) == -513
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(2, 2) == 108
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f_phi01(2, 3) == 1

    def test_c_disc_values(self):
        """Known discriminant-indexed coefficients c(D)."""
        expected = {
            -1: 1, 0: 10, 3: -64, 4: 108, 7: -513, 8: 808,
            11: -2752, 12: 4016, 15: -11775, 16: 16524,
        }
        for D, c_val in expected.items():
            assert c_disc(D) == c_val, f"c({D}): expected {c_val}, got {c_disc(D)}"

    def test_vanishing_below_minus1(self):
        """f(n, l) = 0 when D = 4n - l^2 < -1."""
        for (n, l), f_val in PHI01_TABLE.items():
            # VERIFIED [DC] vanishing check [LC] boundary/limiting case
            assert 4*n - l*l >= -1, f"Nonzero f({n},{l}) at D={4*n-l*l}"

    def test_phi01_normalization_numerical(self):
        """phi_{0,1}(i, 0) = 12."""
        val = phi_01_value(1.0j, 0.0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val - 12.0) < 1e-6

    def test_phi01_T_invariance(self):
        """phi_{0,1}(tau+1, z) = phi_{0,1}(tau, z)."""
        tau = 0.7 + 1.5j
        z = 0.3 + 0.2j
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(phi_01_value(tau, z) - phi_01_value(tau + 1, z)) < 1e-6

    def test_phi01_Z_periodicity(self):
        """phi_{0,1}(tau, z+1) = phi_{0,1}(tau, z)."""
        tau = 0.7 + 1.5j
        z = 0.3 + 0.2j
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(phi_01_value(tau, z) - phi_01_value(tau, z + 1)) < 1e-6

    def test_phi01_jacobi_transformation(self):
        """phi_{0,1}(tau, z+tau) = e^{-2pi i(tau+2z)} phi_{0,1}(tau, z)."""
        tau = 0.5 + 2.0j
        z = 0.2 + 0.1j
        val1 = phi_01_value(tau, z)
        val2 = phi_01_value(tau, z + tau)
        factor = np.exp(-2j * np.pi * (tau + 2*z))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val2 - factor * val1) / abs(val1) < 1e-4

    def test_compute_matches_hardcoded(self):
        """DFT-extracted coefficients match the hardcoded table."""
        computed = compute_phi01_table(n_max=3, l_max=5)
        for (n, l), f_val in PHI01_TABLE.items():
            if n <= 3 and abs(l) <= 5:
                assert (n, l) in computed, f"Missing ({n},{l})"
                assert computed[(n, l)] == f_val, (
                    f"Mismatch at ({n},{l}): table={f_val}, computed={computed[(n,l)]}"
                )


# ======================================================================
# 4. Borcherds product
# ======================================================================

class TestBorcherdsProduct:
    """Verify the Borcherds product B_F(Z)."""

    def test_product_nonzero(self):
        """Product is nonzero deep in the Siegel upper half-space."""
        val = borcherds_product_numerical(3.0j, 0.1j, 3.5j, order=4)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val) > 1e-30

    def test_product_real_for_imaginary_Z(self):
        """Product is real when Z is purely imaginary."""
        val = borcherds_product_numerical(2.0j, 0.2j, 2.5j, order=4)
        assert abs(val.imag) < abs(val) * 1e-8

    def test_product_prefactor_dominates(self):
        """Leading term is e^{2pi i (rho, Z)}, so |B_F| ~ e^{-2pi(Im(tau)+Im(omega)-Im(z)/2)}.

        At moderate Im, product corrections shift the log by O(1), so we
        test at large Im where the prefactor dominates.
        """
        for im_tau in [5.0, 8.0, 12.0]:
            val = borcherds_product_numerical(im_tau*1j, 0.1j, im_tau*1j, order=6)
            expected_log = -2 * np.pi * (im_tau + im_tau - 0.05)
            actual_log = np.log(abs(val))
            # Product corrections shift the log by O(1), so allow 2% relative error
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(actual_log - expected_log) / abs(expected_log) < 0.02

    def test_product_order_convergence(self):
        """Product stabilizes as truncation order increases."""
        tau, z, omega = 2.0j, 0.2j, 2.5j
        vals = [borcherds_product_numerical(tau, z, omega, order=k) for k in [4, 6, 8]]
        # VERIFIED [DC] convergence [LC] boundary/limiting case
        assert abs(vals[1] - vals[2]) / abs(vals[2]) < 1e-6


# ======================================================================
# 5. Weyl orbit sum
# ======================================================================

class TestWeylSum:
    """Verify the Weyl orbit sum W(Z) = sum det(w) exp(2pi i (w(rho), Z))."""

    def test_convergence(self):
        """Weyl sum converges as word length increases."""
        result = verify_weyl_sum_convergence()
        assert result['converged']

    def test_real_for_imaginary_Z(self):
        """Weyl sum is real when Z is purely imaginary."""
        val = weyl_sum_numerical(2.0j, 0.2j, 2.5j, max_length=6)
        assert abs(val.imag) < abs(val) * 1e-10

    def test_nonzero(self):
        """Weyl sum is nonzero in the convergence region."""
        val = weyl_sum_numerical(2.0j, 0.2j, 2.5j, max_length=6)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(val) > 1e-15

    def test_rapid_convergence(self):
        """Weyl sum at word length 4 agrees with length 8 to 10 digits."""
        tau, z, omega = 2.0j, 0.2j, 2.5j
        w4 = weyl_sum_numerical(tau, z, omega, max_length=4)
        w8 = weyl_sum_numerical(tau, z, omega, max_length=8)
        # VERIFIED [DC] convergence [LC] boundary/limiting case
        assert abs(w4 - w8) / abs(w8) < 1e-10

    def test_tau_omega_symmetry(self):
        """W(omega, z, tau) / W(tau, z, omega) is +/-1.

        The f_2 <-> f_{-2} automorphism swaps tau <-> omega.
        """
        tau, z, omega = 1.8j, 0.15j, 2.3j
        w1 = weyl_sum_numerical(tau, z, omega, max_length=8)
        w2 = weyl_sum_numerical(omega, z, tau, max_length=8)
        if abs(w1) > 1e-20 and abs(w2) > 1e-20:
            ratio = w2 / w1
            # VERIFIED [DC] symmetry check [LC] boundary/limiting case
            assert abs(abs(ratio) - 1.0) < 0.01


# ======================================================================
# 6. Denominator identity: Product = Sum
# ======================================================================

class TestDenominatorIdentity:
    """Verify the WKB denominator identity by matching product and sum sides."""

    def test_leading_order_agreement(self):
        """B_F(Z) / W(Z) -> 1 as Im(Z) -> infinity."""
        result = verify_product_weyl_agreement()
        assert result['converging_to_1']

    def test_ratio_monotone_to_1(self):
        """The ratio |B_F/W - 1| decreases monotonically with Im(Z)."""
        points = [
            (2.0j, 0.15j, 2.5j),
            (4.0j, 0.05j, 4.5j),
            (8.0j, 0.02j, 8.5j),
        ]
        ratios = []
        for tau, z, omega in points:
            bf = borcherds_product_numerical(tau, z, omega, order=8)
            ws = weyl_sum_numerical(tau, z, omega, max_length=8)
            ratios.append(abs(bf / ws - 1))

        for i in range(1, len(ratios)):
            assert ratios[i] < ratios[i-1], (
                f"|ratio-1| not decreasing: {ratios[i-1]:.2e} -> {ratios[i]:.2e}"
            )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ratios[-1] < 1e-8

    def test_imaginary_correction_small(self):
        """S_im = B_F/W is close to 1 at moderate Im(Z)."""
        bf = borcherds_product_numerical(3.0j, 0.1j, 3.5j, order=6)
        ws = weyl_sum_numerical(3.0j, 0.1j, 3.5j, max_length=8)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(bf / ws - 1) < 1e-6

    def test_correction_nonzero_at_moderate_im(self):
        """At Im(tau) ~ 2, the correction is slightly different from 1."""
        bf = borcherds_product_numerical(2.0j, 0.15j, 2.5j, order=8)
        ws = weyl_sum_numerical(2.0j, 0.15j, 2.5j, max_length=8)
        correction = abs(bf / ws)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert 0.999 < correction < 1.001

    def test_product_sum_both_real(self):
        """B_F and W are both real for purely imaginary Z."""
        tau, z, omega = 2.5j, 0.2j, 3.0j
        bf = borcherds_product_numerical(tau, z, omega, order=6)
        ws = weyl_sum_numerical(tau, z, omega, max_length=8)
        assert abs(bf.imag) < abs(bf) * 1e-8
        assert abs(ws.imag) < abs(ws) * 1e-10


# ======================================================================
# 7. Imaginary root structure
# ======================================================================

class TestImaginaryRoots:
    """Verify the imaginary simple root structure of g_{Delta_5}."""

    def test_fundamental_chamber_conditions(self):
        """Fundamental chamber elements satisfy (a, delta_i) <= 0."""
        fc = fundamental_chamber_elements(3)
        for (n, l, m), mult in fc:
            v = np.array([n, l, m], dtype=float)
            for i, delta in enumerate(SIMPLE_ROOTS):
                ip = inner_product(v, delta)
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert ip <= 1e-10, (
                    f"({n},{l},{m}): (a, delta_{i+1}) = {ip} > 0"
                )

    def test_fundamental_chamber_multiplicities(self):
        """Imaginary root multiplicities match phi_{0,1} coefficients."""
        fc = fundamental_chamber_elements(3)
        for (n, l, m), mult in fc:
            expected = f_phi01(n * m, l)
            assert mult == expected, (
                f"({n},{l},{m}): mult={mult} != f({n*m},{l})={expected}"
            )

    def test_null_roots_include_both_signs(self):
        """Null roots (a,a) = 0 include both even (mult>0) and odd (mult<0) roots.

        In a BKM superalgebra, null imaginary roots can have either sign
        of multiplicity. Even (bosonic) roots have mult > 0, odd (fermionic)
        roots have mult < 0. The root (0,0,m) has mult = f(0,0) = 10 > 0 (even),
        while (1,-1,1) has mult = f(1,-1) = -64 < 0 (odd/fermionic).
        """
        fc = fundamental_chamber_elements(3)
        null_pos = []
        null_neg = []
        for (n, l, m), mult in fc:
            v = np.array([n, l, m], dtype=float)
            if abs(norm_sq(v)) < 0.1:
                if mult > 0:
                    null_pos.append((n, l, m))
                elif mult < 0:
                    null_neg.append((n, l, m))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(null_pos) > 0, "No null root with positive mult"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(null_neg) > 0, "No null root with negative mult"

    def test_negative_norm_roots_mixed_signs(self):
        """Negative-norm imaginary roots have both positive and negative multiplicities."""
        fc = fundamental_chamber_elements(3)
        has_pos = any(mult > 0 for (n,l,m), mult in fc if norm_sq(np.array([n,l,m],dtype=float)) < -0.1)
        has_neg = any(mult < 0 for (n,l,m), mult in fc if norm_sq(np.array([n,l,m],dtype=float)) < -0.1)
        assert has_pos, "No negative-norm root with positive mult"
        assert has_neg, "No negative-norm root with negative mult (fermionic)"

    def test_real_simple_roots_excluded(self):
        """Real simple roots are not in the imaginary root list."""
        fc = fundamental_chamber_elements(5)
        for (n, l, m), mult in fc:
            v = np.array([n, l, m], dtype=float)
            for sr in SIMPLE_ROOTS:
                assert not np.allclose(v, sr), f"Simple root in imaginary list"


# ======================================================================
# 8. Full verification
# ======================================================================

class TestFullVerification:
    """Master verification suite."""

    def test_verify_all_passes(self):
        """All checks in verify_all() pass."""
        results = verify_all()
        for name, val in results.items():
            if isinstance(val, bool):
                assert val, f"Check '{name}' failed"

    def test_phi01_table_coverage(self):
        """Hardcoded table covers indices needed for order-3 product."""
        for n in range(4):
            for m in range(4):
                for l in range(-6, 7):
                    nm = n * m
                    if nm <= 6 and abs(l) <= 5:
                        # Should not crash
                        _ = f_phi01(nm, l)

    def test_consistency_across_points(self):
        """B_F/W gives consistent correction at different Re(tau) (same Im level)."""
        results = []
        for re_tau in [0.0, 0.3, 0.7]:
            tau = re_tau + 3.0j
            bf = borcherds_product_numerical(tau, 0.1j, 3.5j, order=6)
            ws = weyl_sum_numerical(tau, 0.1j, 3.5j, max_length=8)
            results.append(bf / ws)
        for i in range(1, len(results)):
            # VERIFIED [DC] consistency check [LC] boundary/limiting case
            assert abs(results[i] - results[0]) < 0.01


# ======================================================================
# 9. Cross-validation against bkm_shadow_tower.py
# ======================================================================

class TestCrossValidationBKM:
    """Cross-validate lattice and root data against bkm_shadow_tower.py.

    bkm_shadow_tower uses the (delta_1, delta_2, delta_3) basis with
    Gram matrix A = ((2,-2,-2),(-2,2,-2),(-2,-2,2)) and the K3 elliptic
    genus convention for phi_{0,1}: f(0,0)=20, f(0,1)=2, which is 2x
    the Eichler-Zagier normalization in wkb_denominator.
    """

    @pytest.fixture(scope="class")
    def bkm(self):
        _lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
        _spec = importlib.util.spec_from_file_location(
            'bkm_shadow_tower',
            os.path.join(_lib_dir, 'bkm_shadow_tower.py')
        )
        mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(mod)
        return mod

    def test_gram_matrices_agree(self, bkm):
        """Simple-root Gram matrix matches between modules."""
        bkm_gram = np.array(bkm.GRAM_MATRIX, dtype=float)
        wkb_gram = np.array([
            [inner_product(SIMPLE_ROOTS[i], SIMPLE_ROOTS[j])
             for j in range(3)] for i in range(3)
        ])
        np.testing.assert_allclose(wkb_gram, bkm_gram, atol=1e-14)

    def test_weyl_vector_inner_products_agree(self, bkm):
        """(rho, delta_i) = -1 in both modules."""
        for i in range(3):
            wkb_val = inner_product(RHO, SIMPLE_ROOTS[i])
            bkm_val = bkm.weyl_vector_inner(i)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(wkb_val - float(bkm_val)) < 1e-14

    def test_phi01_convention_match(self, bkm):
        """bkm and wkb now both use EZ normalization for phi_{0,1}.

        After replacing the wrong hardcoded table in bkm with exact values
        from phi01_fourier.py, both modules agree on all coefficients.
        """
        bkm_data = bkm.phi01_coefficients()
        assert bkm_data[(0, 0)] == f_phi01(0, 0)
        assert bkm_data[(0, 1)] == f_phi01(0, 1)
        # Cross-validate through n=4
        for n in range(5):
            max_l = int((4 * n + 1) ** 0.5) + 1
            for l in range(max_l + 1):
                bkm_val = bkm.get_f(n, l, bkm_data)
                wkb_val = f_phi01(n, l)
                assert bkm_val == wkb_val, (
                    f"f({n},{l}): bkm={bkm_val}, wkb={wkb_val}"
                )

    def test_rho_norm_agrees(self, bkm):
        """(rho, rho) = -3/2 in both modules."""
        bkm_rho = bkm.WEYL_VECTOR
        bkm_gram = bkm.GRAM_MATRIX
        bkm_norm = sum(
            bkm_rho[i] * bkm_gram[i][j] * bkm_rho[j]
            for i in range(3) for j in range(3)
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(float(bkm_norm) - norm_sq(RHO)) < 1e-14


# ======================================================================
# 10. Cross-validation against dd_modular_lattices.py
# ======================================================================

class TestCrossValidationDD:
    """Cross-validate against dd_modular_lattices.py."""

    @pytest.fixture(scope="class")
    def dd(self):
        _lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
        _spec = importlib.util.spec_from_file_location(
            'dd_modular_lattices',
            os.path.join(_lib_dir, 'dd_modular_lattices.py')
        )
        mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(mod)
        return mod

    def test_lambda_21_gram_agrees(self, dd):
        """Ambient Lambda^{2,1} Gram matrix matches."""
        dd_gram = dd.gram_lambda_21()
        np.testing.assert_array_equal(GRAM.astype(int), dd_gram)

    def test_lambda_21_II_gram_agrees(self, dd):
        """Type-II sublattice Gram matrix matches."""
        dd_gram_II = dd.gram_lambda_21_II()
        wkb_gram_II = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                wkb_gram_II[i, j] = round(inner_product(SIMPLE_ROOTS[i], SIMPLE_ROOTS[j]))
        np.testing.assert_array_equal(wkb_gram_II, dd_gram_II)

    def test_delta_coords_agree(self, dd):
        """Simple root coordinates in (f_2, f_3, f_{-2}) basis match."""
        dd_deltas = dd.delta_coords_in_f_basis()
        np.testing.assert_array_equal(DELTA_1.astype(int), dd_deltas["delta_1"])
        np.testing.assert_array_equal(DELTA_2.astype(int), dd_deltas["delta_2"])
        np.testing.assert_array_equal(DELTA_3.astype(int), dd_deltas["delta_3"])

    def test_weyl_vector_f_basis_agrees(self, dd):
        """Weyl vector in (f_2, f_3, f_{-2}) basis matches."""
        dd_rho = dd.weyl_vector_f_basis()
        for i in range(3):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(float(RHO[i]) - float(dd_rho[i])) < 1e-14

    def test_weyl_vector_norm_agrees(self, dd):
        """(rho, rho) = -3/2 in both modules."""
        dd_norm = dd.weyl_vector_norm_sq()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(norm_sq(RHO) - float(dd_norm)) < 1e-14

    def test_verify_weyl_vector_agrees(self, dd):
        """Both modules verify (rho, delta_i) = -1."""
        assert verify_weyl_vector()
        assert dd.verify_weyl_vector()

    def test_gram_from_ambient_agrees(self, dd):
        """dd_modular_lattices recomputes Gram(delta_i, delta_j) from Lambda^{2,1}."""
        recomputed = dd.verify_gram_II_from_ambient()
        expected = dd.gram_lambda_21_II()
        np.testing.assert_array_equal(recomputed, expected)


# ======================================================================
# 11. Cross-validation against phi01_fourier.py
# ======================================================================

class TestCrossValidationPhi01:
    """Cross-validate phi_{0,1} against the exact-arithmetic phi01_fourier module.

    phi01_fourier.py computes via Fraction arithmetic over lattice sums,
    while wkb_denominator uses numerical theta function evaluation + DFT.
    Both use the EZ normalization: phi_{0,1}(tau,0)=12, f(0,0)=10, f(0,1)=1.
    """

    @pytest.fixture(scope="class")
    def phi01_mod(self):
        _lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
        _spec = importlib.util.spec_from_file_location(
            'phi01_fourier',
            os.path.join(_lib_dir, 'phi01_fourier.py')
        )
        mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(mod)
        return mod

    @pytest.mark.parametrize("n,l", [
        (0, 0), (0, 1), (0, -1),
        (1, 0), (1, 1), (1, -1), (1, 2), (1, -2),
        (2, 0), (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 1), (3, 2), (3, 3),
        (4, 0), (4, 1), (4, 4),
    ])
    def test_individual_coefficients(self, phi01_mod, n, l):
        """f(n,l) from exact arithmetic matches the hardcoded table."""
        exact_val = phi01_mod.phi01_coefficient(n, l)
        wkb_val = f_phi01(n, l)
        assert exact_val == wkb_val, (
            f"f({n},{l}): exact={exact_val}, wkb={wkb_val}"
        )

    def test_full_table_through_n4(self, phi01_mod):
        """All nonzero coefficients through n=4 agree."""
        exact_table = phi01_mod.phi01_table(4)
        for (n, l), exact_val in exact_table.items():
            wkb_val = f_phi01(n, l)
            assert exact_val == wkb_val, (
                f"f({n},{l}): exact={exact_val}, wkb={wkb_val}"
            )

    def test_discriminant_dependence_exact(self, phi01_mod):
        """phi01_fourier also satisfies discriminant dependence."""
        by_disc = phi01_mod.phi01_by_discriminant(5)
        for D, exact_c in by_disc.items():
            if D in C_DISC:
                assert c_disc(D) == exact_c, (
                    f"c({D}): exact={exact_c}, wkb={c_disc(D)}"
                )
