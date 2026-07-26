r"""
General Borcherds multiplicative lift: Jacobi forms -> Siegel modular forms.

The Borcherds multiplicative lift takes a weakly holomorphic Jacobi form
phi of weight 0 and index 1 and produces an automorphic form Phi on the
Siegel upper half-space H_2 of weight c(0)/2, where c(D) denotes the
Fourier coefficient of phi indexed by discriminant D = 4n - l^2.

THE LIFT FORMULA (Lorgat, Theorem 4)
=====================================

Given phi(tau, z) = sum_{n,l} c(4n-l^2) q^n r^l, the Borcherds lift is:

    Phi(Z) = exp(c(-1) * pi*i * (tau + z + omega))
             * prod_{(n,l,m)>0} (1 - exp(2*pi*i*(n*tau + l*z + m*omega)))^{c(4nm - l^2)}

where Z = ((tau, z), (z, omega)) in H_2, and the ordering (n,l,m) > 0 means:
    - n >= 0, m >= 0, l in Z   when n > 0 or m > 0
    - n = m = 0, l < 0

Equivalently, writing this in the standard form Phi = exp(-2*pi*i*(rho,Z)) * prod ...,
the Weyl vector rho in the (n,l,m) parametrization has (rho,Z) = -(tau+z+omega)/2.

MAIN RESULT
===========

For phi = phi_{0,1}: c(0) = 10, so the lift has weight 5. The lift equals
(1/64) * Delta_5 up to a sign (see igusa_product_formula.py for sign discussion).

ADDITIONAL LIFTS
================

(a) phi = 12 (constant): c(0)=12, all other c(D)=0. Weight 6.
    The product reduces to eta(tau)^12 * eta(omega)^12 * corrections.

(b) 2*phi_{0,1}: c'(D) = 2*c(D), so c'(0) = 20, weight = 10.
    The lift equals the SQUARE of the lift of phi_{0,1}, i.e., Delta_5^2/4096.

(c) For M_2(Gamma_2, nu_4): requires a vector-valued modular form of weight 1/2
    for the Weil representation (Borcherds' original framework).

References
----------
    Borcherds, "Automorphic forms with singularities on Grassmannians" (1998)
    Gritsenko-Nikulin, "Automorphic forms and Lorentzian KM algebras, Part II" (1998)
    Lorgat, "A Borcherds lift of phi_{0,1}" (2020), Theorem 4
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np
from typing import Dict, Optional, Tuple, Callable


# ---------------------------------------------------------------------------
# 1. Core Borcherds lift engine
# ---------------------------------------------------------------------------

def borcherds_lift(
    c_table: Dict[int, int],
    tau: complex,
    z: complex,
    omega: complex,
    N_prod: int = 15,
) -> complex:
    r"""
    Evaluate the Borcherds multiplicative lift at a point Z in H_2.

    The general formula for an index-1 Jacobi form with coefficients c(D):

        Phi(Z) = exp(c(-1) * pi*i * (tau + z + omega))
                 * prod_{(n,l,m)>0} (1 - e^{2*pi*i*(n*tau + l*z + m*omega)})^{c(4nm - l^2)}

    The Weyl vector contribution (leading exponential) is proportional to
    c(-1), the coefficient at the polar discriminant D = -1. For phi_{0,1}
    with c(-1) = 1, this reproduces the formula from Lorgat, Theorem 4.

    Parameters
    ----------
    c_table : dict
        Mapping D -> c(D), the Fourier coefficients indexed by discriminant.
        For phi_{0,1}: c(-1)=1, c(0)=10, c(3)=-64, c(4)=108, ...
    tau : complex
        Upper-left entry of Z (Im > 0).
    z : complex
        Off-diagonal entry of Z.
    omega : complex
        Lower-right entry of Z (Im > 0).
    N_prod : int
        Truncation bound: n, m in [0, N_prod], |l| <= N_prod.

    Returns
    -------
    complex
        The value Phi(Z) of the Borcherds lift.
    """
    # Validate H_2 condition
    Y = np.array([[tau.imag, z.imag], [z.imag, omega.imag]])
    assert Y[0, 0] > 0 and np.linalg.det(Y) > 0, \
        "Z must be in the Siegel upper half-space H_2"

    def _c(D: int) -> int:
        return c_table.get(D, 0)

    # Leading exponential: exp(c(-1) * pi*i * (tau + z + omega))
    # The Weyl vector rho contributes c(-1)/2 to each coordinate.
    c_neg1 = _c(-1)
    log_sum = c_neg1 * 1j * np.pi * (tau + z + omega)

    # Case 1: n = m = 0, l < 0
    for l in range(-N_prod, 0):
        D = -l * l  # D = 4*0*0 - l^2
        exponent = _c(D)
        if exponent == 0:
            continue
        X = np.exp(2j * np.pi * l * z)
        if abs(1.0 - X) < 1e-300:
            continue
        log_sum += exponent * np.log(1.0 - X)

    # Case 2: n > 0 or m > 0
    for n in range(0, N_prod + 1):
        for m in range(0, N_prod + 1):
            if n == 0 and m == 0:
                continue
            nm = n * m
            for l in range(-N_prod, N_prod + 1):
                D = 4 * nm - l * l
                exponent = _c(D)
                if exponent == 0:
                    continue
                X = np.exp(2j * np.pi * (n * tau + l * z + m * omega))
                if abs(X) > 1e200:
                    continue
                if abs(1.0 - X) < 1e-300:
                    continue
                log_sum += exponent * np.log(1.0 - X)

    return np.exp(log_sum)


def borcherds_lift_weight(c_table: Dict[int, int]) -> float:
    r"""
    Weight of the Borcherds lift, read off the Jacobi-side input: c(0)/2.

    This is the Borcherds weight formula (Borcherds 1998, Theorem 13.3;
    Gritsenko-Nikulin 1998): the multiplicative lift of a weakly
    holomorphic weight-0 index-1 Jacobi form with Fourier coefficients
    c(D) is a Siegel modular form of weight c(0)/2.

    HONESTY NOTE.  As implemented, this function is DEFINITIONAL: it
    reads the constant term of the input table and halves it.  It does
    not derive the weight.  A test asserting
    ``borcherds_lift_weight(c) == c[0]/2`` verifies nothing.

    The independent computation of the same weight, on the CHL ladder
    N in {1, 2, 3, 4, 6}, is the frame-shape half-sum route:
    ``chl_square_root_weight(N)`` derives the weight from the M24 frame
    shape of the Z/N orbifold generator, with no reference to Fourier
    coefficients.  The test suite compares the two routes; see the
    frame-shape section below for exactly what that comparison does and
    does not establish at each N.
    """
    return c_table.get(0, 0) / 2.0


# ---------------------------------------------------------------------------
# 1b. CHL frame shapes: the frame-shape route to the lift weight
# ---------------------------------------------------------------------------
#
# The CHL Z/N orbifolds of K3 x E (N in {1, 2, 3, 4, 6}, the orders of
# automorphisms an elliptic curve carries) have orbifold generators
# acting on the 24-dimensional K3 lattice representation with M24 frame
# (cycle) shapes
#
#     N = 1:  1^24              N = 2:  1^8 2^8        N = 3:  1^6 3^6
#     N = 4:  1^4 2^2 4^4       N = 6:  1^2 2^2 3^2 6^2
#
# (Jatkar-Sen, "Dyon spectrum in CHL models", arXiv:hep-th/0510147;
# Govindarajan-Krishna, "BKM Lie superalgebras from dyon spectra in
# Z_N CHL orbifolds", arXiv:0907.1410.  In-manuscript anchors:
# chapters/theory/gluing/sec_7_lattice_automorphic.tex and
# chapters/theory/phi_universal_trace_platonic.tex, which record the
# same frame shapes and both ladder weight tuples.)
#
# A frame shape prod_i d_i^{r_i} determines the eta product
# eta_rho(tau) = prod_i eta(d_i * tau)^{r_i}, a modular form of weight
# (1/2) * sum_i r_i.  The Jatkar-Sen dyon form Phi_k attached to the
# Z/N CHL orbifold has weight
#
#     k(N) = (1/2) * sum_i r_i - 2,
#
# giving k = (10, 6, 4, 3, 2) for N = (1, 2, 3, 4, 6).  The
# Govindarajan-Krishna square roots Delta_{k/2} (N = 1 member: Delta_5,
# the lift of phi_{0,1}) have weight k/2 = (5, 3, 2, 3/2, 1); the
# weight-0 Jacobi seed of Delta_{k/2} has constant term c_N(0) = k(N),
# so the frame-shape route reproduces the universal Borcherds-weight
# identity kappa_BKM(Phi_N) = c_N(0)/2 on this ladder.
#
# LADDER DISCIPLINE.  Two ladders live on the same CHL slice and are
# never mixed: this square-root ladder (weights (5, 3, 2, 3/2, 1),
# seed constants (10, 6, 4, 3, 2)) and the Mathieu-twined ladder
# (weights (10, 4, 3, 2, 1), constants (20, 8, 6, 4, 2)).  The
# geometric-orbifold table in kappa_bkm_adversarial.py (c_N(0) =
# (10, 8, 6, 4, 2)) is a third, distinct family (Enriques-type
# quotients); its N >= 2 rows are NOT the CHL square-root rows here.
#
# NOTE ON THE FAKE MONSTER.  For the Leech/II_{25,1} lift Phi_12 the
# eta-product weight of the frame shape 1^24 (namely 12) equals the
# lift weight directly, with no "-2" shift: the shift is specific to
# the Jatkar-Sen K3 x E dyon-form normalisation, not a universal law.

CHL_FRAME_SHAPES: Dict[int, Dict[int, int]] = {
    1: {1: 24},
    2: {1: 8, 2: 8},
    3: {1: 6, 3: 6},
    4: {1: 4, 2: 2, 4: 4},
    6: {1: 2, 2: 2, 3: 2, 6: 2},
}

# Constant terms c_N(0) of the weight-0 Jacobi seeds of the square-root
# forms Delta_{k/2}.  For N = 1 the value 10 is computed exactly
# in-repo (phi01_fourier.py, constant term of phi_{0,1}); for N >= 2
# the values are recorded from Jatkar-Sen / Govindarajan-Krishna --
# no in-repo Fourier computation of the twisted seeds exists yet, so
# comparisons against them at N >= 2 are literature-consistency
# checks, not two-sided computations.

CHL_SQUARE_ROOT_SEED_C0: Dict[int, int] = {1: 10, 2: 6, 3: 4, 4: 3, 6: 2}


def frame_shape_degree(frame_shape: Dict[int, int]) -> int:
    r"""
    Degree sum_i r_i * d_i of a frame shape prod_i d_i^{r_i}.

    Every CHL frame shape arises from an action on the 24-dimensional
    lattice representation, so its degree must equal 24.
    """
    return sum(d * r for d, r in frame_shape.items())


def eta_product_weight(frame_shape: Dict[int, int]) -> Fraction:
    r"""
    Weight of the eta product eta_rho(tau) = prod_i eta(d_i*tau)^{r_i}
    attached to the frame shape prod_i d_i^{r_i}:

        wt(eta_rho) = (1/2) * sum_i r_i.

    (Each eta factor has weight 1/2 regardless of its argument
    rescaling.)  Exact rational output.
    """
    return Fraction(sum(frame_shape.values()), 2)


def jatkar_sen_dyon_weight(N: int) -> Fraction:
    r"""
    Weight k(N) of the Jatkar-Sen dyon form Phi_k for the Z/N CHL
    orbifold, computed from the frame shape alone:

        k(N) = (1/2) * sum_i r_i - 2.

    Yields k = (10, 6, 4, 3, 2) for N = (1, 2, 3, 4, 6).  Validates
    that the frame shape has degree 24 before using it.
    """
    frame_shape = CHL_FRAME_SHAPES[N]
    deg = frame_shape_degree(frame_shape)
    assert deg == 24, (
        f"CHL frame shape for N={N} has degree {deg}, expected 24"
    )
    return eta_product_weight(frame_shape) - 2


def chl_square_root_weight(N: int) -> Fraction:
    r"""
    kappa_BKM on the CHL square-root ladder: the weight of the
    Govindarajan-Krishna square root Delta_{k/2} of the Jatkar-Sen
    dyon form Phi_k, computed from the frame shape alone:

        wt(Delta_{k/2}) = k(N)/2 = ((1/2) * sum_i r_i - 2) / 2.

    Yields (5, 3, 2, 3/2, 1) for N = (1, 2, 3, 4, 6).  This function
    never consults a Fourier coefficient table, so at N = 1 -- where
    the seed constant c_1(0) = 10 is computed independently and
    exactly by phi01_fourier.py -- the agreement
    ``chl_square_root_weight(1) == borcherds_lift_weight(phi01_c_table())``
    is a genuine two-path verification of kappa_BKM = c(0)/2.  At
    N >= 2 the seed constants in CHL_SQUARE_ROOT_SEED_C0 are
    literature values, so the same comparison is a consistency check
    of the frame-shape computation against the recorded constants.
    """
    return jatkar_sen_dyon_weight(N) / 2


# ---------------------------------------------------------------------------
# 2. Genus-2 theta constants and Delta_5
# ---------------------------------------------------------------------------

def _even_theta_characteristics():
    """Return the 10 even theta characteristics for genus 2."""
    chars = []
    for a0 in [0, 1]:
        for a1 in [0, 1]:
            for b0 in [0, 1]:
                for b1 in [0, 1]:
                    if (a0 * b0 + a1 * b1) % 2 == 0:
                        chars.append(((a0, a1), (b0, b1)))
    return chars


def _genus2_theta(Z, a, b, N_terms=30):
    """Genus-2 theta constant with characteristic [a; b]."""
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    Y = Z.imag
    result = 0.0j
    for n1 in range(-N_terms, N_terms + 1):
        for n2 in range(-N_terms, N_terms + 1):
            v = np.array([n1 + a[0] / 2.0, n2 + a[1] / 2.0])
            decay = np.pi * (v[0]**2 * Y[0, 0] + 2 * v[0] * v[1] * Y[0, 1]
                             + v[1]**2 * Y[1, 1])
            if decay > 500:
                continue
            quad = (v[0]**2 * Z[0, 0] + 2.0 * v[0] * v[1] * Z[0, 1]
                    + v[1]**2 * Z[1, 1])
            lin = b[0] * v[0] + b[1] * v[1]
            exponent = 1j * np.pi * (quad + lin)
            if exponent.real > 500:
                continue
            result += np.exp(exponent)
    return result


def delta5_theta(tau: complex, z: complex, omega: complex,
                 N_terms: int = 30) -> complex:
    r"""
    Compute Delta_5(Z) as the product of 10 even genus-2 theta constants.

    Delta_5(Z) = prod_{[a;b] even} theta[a,b](Z)
    """
    Z = np.array([[tau, z], [z, omega]], dtype=complex)
    chars = _even_theta_characteristics()
    log_result = 0.0j
    for (a, b) in chars:
        theta_val = _genus2_theta(Z, a, b, N_terms)
        if abs(theta_val) < 1e-300:
            return 0.0j
        log_result += np.log(theta_val)
    return np.exp(log_result)


# ---------------------------------------------------------------------------
# 3. Jacobi form coefficient tables
# ---------------------------------------------------------------------------

def phi01_c_table(D_max: int = 100) -> Dict[int, int]:
    r"""
    Compute c(D) for phi_{0,1} up to discriminant D_max.

    Uses the exact arithmetic implementation from phi01_fourier.py.
    """
    try:
        from compute.lib.phi01_fourier import phi01_by_discriminant
    except ImportError:  # pragma: no cover
        from lib.phi01_fourier import phi01_by_discriminant
    max_n = D_max // 4 + 2
    return phi01_by_discriminant(max_n)


def constant_jacobi_c_table(value: int = 12) -> Dict[int, int]:
    r"""
    c(D) table for the constant Jacobi form phi = value.

    c(0) = value, c(D) = 0 for D != 0. Lift weight = value/2.

    For value=12: this is the trivial Jacobi form. The Borcherds
    product collapses to factors involving only terms with 4nm = l^2.
    """
    return {0: value}


def doubled_phi01_c_table(D_max: int = 100) -> Dict[int, int]:
    r"""
    c(D) table for 2*phi_{0,1}: c'(D) = 2*c(D).

    c'(0) = 20, giving weight 10. The Borcherds lift of 2*phi_{0,1}
    equals the SQUARE of the lift of phi_{0,1}, since exponentiating
    the log-product with doubled exponents squares the result:

        Phi_{2*phi}(Z) = [Phi_{phi}(Z)]^2

    So this lift equals ((1/64)*Delta_5)^2 = Delta_5^2 / 4096.
    """
    base = phi01_c_table(D_max)
    return {D: 2 * v for D, v in base.items()}


# ---------------------------------------------------------------------------
# 4. Modular forms for the constant-lift analysis
# ---------------------------------------------------------------------------

def _eta_function(tau: complex, N: int = 200) -> complex:
    r"""Dedekind eta function: eta(tau) = q^{1/24} prod_{n>=1} (1-q^n)."""
    q = np.exp(2j * np.pi * tau)
    result = np.exp(2j * np.pi * tau / 24)
    q_n = 1.0 + 0.0j
    for n in range(1, N + 1):
        q_n *= q
        result *= (1.0 - q_n)
    return result


def phi01_numerical(tau: complex, z: complex, N: int = 100) -> complex:
    r"""
    Evaluate phi_{0,1}(tau, z) numerically via the theta-ratio formula.
    """
    def _theta(j, tau, z, N):
        result = 0.0j
        for n in range(-N, N + 1):
            if j == 2:
                nh = n + 0.5
                result += np.exp(1j * np.pi * nh**2 * tau + 2j * np.pi * nh * z)
            elif j == 3:
                result += np.exp(1j * np.pi * n**2 * tau + 2j * np.pi * n * z)
            elif j == 4:
                result += ((-1)**n) * np.exp(1j * np.pi * n**2 * tau
                                              + 2j * np.pi * n * z)
        return result

    th2_z = _theta(2, tau, z, N)
    th2_0 = _theta(2, tau, 0, N)
    th3_z = _theta(3, tau, z, N)
    th3_0 = _theta(3, tau, 0, N)
    th4_z = _theta(4, tau, z, N)
    th4_0 = _theta(4, tau, 0, N)

    return 4.0 * ((th2_z / th2_0)**2 + (th3_z / th3_0)**2 + (th4_z / th4_0)**2)


# ---------------------------------------------------------------------------
# 5. Verification routines
# ---------------------------------------------------------------------------

def verify_phi01_lift_equals_delta5(
    tau: complex, z: complex, omega: complex,
    N_prod: int = 15, N_theta: int = 30, D_max: int = 100,
) -> dict:
    r"""
    Verify that the Borcherds lift of phi_{0,1} equals (1/64)*Delta_5
    at a given point Z in H_2.

    The identity holds up to a sign of -1 arising from the branch
    of log at the (n=0, l=-1, m=0) factor. We verify |ratio| = 1.
    """
    c_table = phi01_c_table(D_max)

    weight = borcherds_lift_weight(c_table)
    assert weight == 5.0, f"Expected weight 5, got {weight}"

    bp = borcherds_lift(c_table, tau, z, omega, N_prod=N_prod)
    d5 = delta5_theta(tau, z, omega, N_terms=N_theta)
    lhs = d5 / 64.0

    if abs(bp) < 1e-300:
        return {
            'borcherds_lift': bp, 'delta5_over_64': lhs, 'delta5': d5,
            'ratio': float('inf'), 'abs_relative_error': float('inf'),
            'weight': weight,
        }

    ratio = lhs / bp
    abs_ratio = abs(lhs) / abs(bp)

    return {
        'borcherds_lift': bp,
        'delta5_over_64': lhs,
        'delta5': d5,
        'ratio': ratio,
        'abs_ratio': abs_ratio,
        'abs_relative_error': abs(abs_ratio - 1.0),
        'phase_ratio': ratio / abs(ratio) if abs(ratio) > 0 else None,
        'weight': weight,
    }


def verify_constant_lift(
    tau: complex, z: complex, omega: complex,
    N_prod: int = 15,
) -> dict:
    r"""
    Compute the Borcherds lift of the constant Jacobi form phi = 12.

    c(0) = 12, c(D) = 0 for D != 0. Weight 6.

    For n=m=0, l<0: c(-l^2) = 0 for l != 0. No contribution.
    For n>0, m=0: c(0 - l^2). Only l=0 => c(0) = 12. Factor: prod(1-q^n)^12.
    For n=0, m>0: similarly prod(1-s^m)^12.
    For n,m>0: c(4nm - l^2). Need l^2 = 4nm for c(0) contribution;
               otherwise c(D) = 0 for D != 0.

    So the dominant terms give:
        Phi ~ exp(pi*i*(tau+z+omega)) * prod_{n>=1}(1-q^n)^12 * prod_{m>=1}(1-s^m)^12
              * [corrections from l^2 = 4nm terms]

    The eta factors: prod(1-q^n)^12 = eta(tau)^12 / q^{1/2} (since eta = q^{1/24}*prod).
    """
    c_table = constant_jacobi_c_table(12)
    weight = borcherds_lift_weight(c_table)

    bp = borcherds_lift(c_table, tau, z, omega, N_prod=N_prod)

    eta_tau = _eta_function(tau)
    eta_omega = _eta_function(omega)

    # For c(-1)=0: the leading exponential is exp(0) = 1.
    # The only surviving factors have 4nm - l^2 = 0 (since c(D)=0 for D != 0).
    # For (n>0, m=0, l=0): c(0) = 12, giving prod(1-q^n)^12.
    # For (n=0, m>0, l=0): c(0) = 12, giving prod(1-s^m)^12.
    # For (n>0, m>0): need l^2 = 4nm (nm perfect square, l = +/-2*sqrt(nm)).
    #   Each such pair gives (1-q^n*r^l*s^m)^12.
    #
    # The eta-product approximation (ignoring nm > 0 corrections):
    #   prod(1-q^n)^12 * prod(1-s^m)^12
    q = np.exp(2j * np.pi * tau)
    s = np.exp(2j * np.pi * omega)
    eta_prod_approx = 1.0 + 0.0j
    for n in range(1, 201):
        eta_prod_approx *= (1.0 - q**n)**12 * (1.0 - s**n)**12

    results = {
        'borcherds_lift': bp,
        'weight': weight,
        'eta_product_approx': eta_prod_approx,
    }

    if abs(bp) > 1e-300 and abs(eta_prod_approx) > 1e-300:
        ratio = bp / eta_prod_approx
        results['ratio_vs_eta_approx'] = ratio
        results['ratio_abs'] = abs(ratio)

    return results


def verify_doubled_lift_vs_square(
    tau: complex, z: complex, omega: complex,
    N_prod: int = 15, N_theta: int = 30, D_max: int = 100,
) -> dict:
    r"""
    Verify that the Borcherds lift with c'(D) = 2*c(D) equals
    the square of the original lift.

    Since the log-sum doubles, we have:
        Phi_{2*phi}(Z) = Phi_{phi}(Z)^2

    And hence Phi_{2*phi} = ((1/64)*Delta_5)^2 = Delta_5^2 / 4096.
    """
    c_table = phi01_c_table(D_max)
    c_doubled = doubled_phi01_c_table(D_max)

    bp = borcherds_lift(c_table, tau, z, omega, N_prod=N_prod)
    bp_doubled = borcherds_lift(c_doubled, tau, z, omega, N_prod=N_prod)

    bp_squared = bp ** 2
    d5 = delta5_theta(tau, z, omega, N_terms=N_theta)
    d5_sq = d5 ** 2

    results = {
        'weight_original': borcherds_lift_weight(c_table),
        'weight_doubled': borcherds_lift_weight(c_doubled),
        'borcherds_original': bp,
        'borcherds_doubled': bp_doubled,
        'borcherds_original_squared': bp_squared,
        'delta5_squared': d5_sq,
    }

    if abs(bp_doubled) > 1e-300 and abs(bp_squared) > 1e-300:
        ratio = bp_doubled / bp_squared
        results['ratio_doubled_vs_squared'] = ratio
        results['ratio_abs_error'] = abs(abs(ratio) - 1.0)

    if abs(bp_doubled) > 1e-300 and abs(d5_sq) > 1e-300:
        ratio_d5 = d5_sq / (4096.0 * bp_doubled)
        results['ratio_d5sq_vs_4096_doubled'] = ratio_d5

    return results


# ---------------------------------------------------------------------------
# 6. Fourier-Jacobi extraction (reverse engineering)
# ---------------------------------------------------------------------------

def fourier_jacobi_expansion(
    target_form: Callable[[complex, complex, complex], complex],
    tau: complex,
    z_values: list,
    A: float = 8.0,
    m_max: int = 3,
) -> Dict[int, np.ndarray]:
    r"""
    Extract the Fourier-Jacobi expansion of a Siegel modular form:

        F(Z) = sum_{m >= 0} phi_m(tau, z) * exp(2*pi*i*m*omega)

    by evaluating at omega = j/M + i*A for multiple j (DFT extraction).

    Returns dict mapping m -> array of phi_m(tau, z_j) values.
    """
    M = 2 * m_max + 2
    omega_vals = [float(j) / M + 1j * A for j in range(M)]

    F_grid = np.zeros((len(z_values), M), dtype=complex)
    for i, z_val in enumerate(z_values):
        for j, omega_val in enumerate(omega_vals):
            F_grid[i, j] = target_form(tau, z_val, omega_val)

    phi_m = {}
    for m in range(m_max + 1):
        vals = np.zeros(len(z_values), dtype=complex)
        for i in range(len(z_values)):
            s = 0.0j
            for j in range(M):
                s += F_grid[i, j] * np.exp(-2j * np.pi * m * float(j) / M)
            vals[i] = s / M * np.exp(2 * np.pi * m * A)
        phi_m[m] = vals

    return phi_m


# ---------------------------------------------------------------------------
# 7. Analysis of M_2(Gamma_2, nu_4)
# ---------------------------------------------------------------------------

def analyze_weight2_multiplier():
    r"""
    Analysis of the Borcherds lift question for M_2(Gamma_2, nu_4).

    For Siegel modular forms of weight 2 with multiplier system nu_4:
    - Required c(0) = 2*2 = 4 for weight 2.
    - phi_{0,1} has c(0) = 10 (weight 5 lift).
    - No scalar multiple of phi_{0,1} gives c(0) = 4 while preserving
      integrality of all other c(D).

    The correct framework: Borcherds' original construction uses a
    vector-valued modular form of weight 1/2 for the Weil representation
    of SL_2(Z) associated to a lattice. The scalar-valued lift
    (Gritsenko-Nikulin version) applies to specific lattices and Jacobi
    forms; the general case requires vector-valued inputs.

    For M_2(Gamma_2, nu_4): the input is the unique nearly holomorphic
    vector-valued form of weight 1/2 with principal part q^{-1/4}
    in one component, related to the theta function of the D_4 lattice.
    """
    return {
        'target_weight': 2,
        'required_c0': 4,
        'phi01_c0': 10,
        'obstruction': (
            'No scalar multiple of phi_{0,1} gives c(0)=4. '
            'The input must be a vector-valued modular form for the '
            'Weil representation, as in Borcherds (1998) Theorem 13.3.'
        ),
        'candidate_input': (
            'Weight-1/2 nearly holomorphic form for the Weil '
            'representation of SL_2(Z) associated to the lattice '
            'Z with quadratic form x -> x^2. The relevant component '
            'has principal part q^{-1/4} and constant term 4.'
        ),
    }


# ---------------------------------------------------------------------------
# 8. Known Borcherds lifts catalog
# ---------------------------------------------------------------------------

KNOWN_BORCHERDS_LIFTS = {
    'Delta_5': {
        'input': 'phi_{0,1}',
        'weight': 5,
        'c(-1)': 1,
        'c(0)': 10,
        'description': 'Igusa cusp form, product of 10 even theta constants',
    },
    'Delta_5_squared': {
        'input': '2 * phi_{0,1}',
        'weight': 10,
        'c(-1)': 2,
        'c(0)': 20,
        'description': 'Square of Delta_5 (up to constant)',
    },
    'Phi_12_fake_monster': {
        'input': 'j(tau) - 744 (weight 0 for II_{25,1})',
        'weight': 12,
        'c(-1)': 1,
        'c(0)': 24,
        'description': 'Fake monster denominator (Borcherds 1995)',
    },
}


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

    print("=" * 70)
    print("Borcherds Multiplicative Lift: Computational Pipeline")
    print("=" * 70)

    # 1. Compute phi_{0,1} coefficients
    print("\n--- phi_{0,1} coefficients c(D) ---")
    c_table = phi01_c_table(30)
    for D in sorted(c_table.keys()):
        if D <= 20:
            print(f"  c({D:3d}) = {c_table[D]}")
    print(f"  Weight of lift: {borcherds_lift_weight(c_table)}")

    # 2. Verify lift = Delta_5 at deep cusp
    print("\n--- Borcherds lift vs Delta_5 (deep cusp) ---")
    result = verify_phi01_lift_equals_delta5(
        2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80,
    )
    print(f"  |lift|           = {abs(result['borcherds_lift']):.6e}")
    print(f"  |Delta_5 / 64|   = {abs(result['delta5_over_64']):.6e}")
    print(f"  |ratio| - 1      = {result['abs_relative_error']:.2e}")
    print(f"  phase(ratio)     = {result.get('phase_ratio', 'N/A')}")

    # 3. Constant lift
    print("\n--- Constant Jacobi form phi=12 ---")
    result_const = verify_constant_lift(2j, 0.1j, 2j, N_prod=12)
    print(f"  Weight = {result_const['weight']}")
    print(f"  |lift| = {abs(result_const['borcherds_lift']):.6e}")
    if 'ratio_vs_eta_approx' in result_const:
        print(f"  ratio vs eta approx = {result_const['ratio_vs_eta_approx']:.6f}")
        print(f"  |ratio| = {result_const['ratio_abs']:.6f}")

    # 4. Doubled lift
    print("\n--- Doubled lift: 2*phi_{0,1} ---")
    result_dbl = verify_doubled_lift_vs_square(
        2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80,
    )
    print(f"  Weight = {result_dbl['weight_doubled']}")
    if 'ratio_doubled_vs_squared' in result_dbl:
        print(f"  Phi(2c)/Phi(c)^2 = {result_dbl['ratio_doubled_vs_squared']:.8f}")
        print(f"  |ratio| - 1 = {result_dbl['ratio_abs_error']:.2e}")

    # 5. Weight-2 analysis
    print("\n--- M_2(Gamma_2, nu_4) analysis ---")
    analysis = analyze_weight2_multiplier()
    print(f"  {analysis['obstruction']}")
    print(f"  {analysis['candidate_input']}")
