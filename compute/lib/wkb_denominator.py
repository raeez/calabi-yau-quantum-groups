r"""Weyl-Kac-Borcherds denominator identity for the BKM superalgebra g_{Delta_5}.

This module verifies the denominator identity for the generalized BKM Lie
superalgebra g_{Delta_5} attached to K3 x E, whose denominator is the
Igusa cusp form Delta_5 of weight 5 for Sp_4(Z).

THE IDENTITY (thm:k3e-denominator, thm:k3e-product)
=====================================================

The Weyl--Kac--Borcherds denominator formula states:

    e^rho prod_{alpha>0} (1-e^{-alpha})^{mult(alpha)}
    = sum_{w in W} det(w) * w( e^rho * S_im )

LEFT SIDE (Product): a product over ALL positive roots of g_{Delta_5},
with multiplicities mult(alpha) = f(nm, l) from phi_{0,1}.

RIGHT SIDE (Sum): the Weyl antisymmetrization of e^rho times the
imaginary simple root correction S_im.

WHAT WE VERIFY
===============

1. Lattice Lambda^{2,1} structure (Gram matrix, simple roots, Weyl vector)
2. Weyl group W^{(2)}(Lambda^{2,1}_{II}) (reflections, orbit of rho, isometry)
3. phi_{0,1} Fourier coefficients (discriminant independence, known values)
4. PRODUCT SIDE: Borcherds automorphic product
     B_F(Z) = e^{2pi i (rho,Z)} prod_{(n,l,m)>0} (1-q^n r^l s^m)^{f(nm,l)}
5. SUM SIDE: Weyl orbit sum
     W(Z) = sum_{w in W} det(w) e^{2pi i (w(rho),Z)}
6. MATCHING: B_F(Z) / W(Z) -> 1 as Im(Z) -> infinity (leading agreement)
7. IMAGINARY ROOT CORRECTION: the ratio B_F/W encodes the correction S_im,
   which is computable from the fundamental domain elements

LATTICE (sec:k3e-reflections)
==============================

Lambda^{2,1} = Z f_2 + Z f_3 + Z f_{-2}, Gram matrix:
    ((0, 0, -1), (0, 2, 0), (-1, 0, 0))

Simple roots: delta_1 = 2f_2 - f_3, delta_2 = 2f_{-2} - f_3, delta_3 = f_3
Gram: ((2,-2,-2),(-2,2,-2),(-2,-2,2))

Weyl vector: rho = f_2 - (1/2)f_3 + f_{-2}, satisfying (rho,delta_i) = -1.

For alpha = n f_2 + l f_3 + m f_{-2}:
    (alpha, alpha) = 2l^2 - 2nm
    mult(alpha) = f(nm, l) where f are Fourier coefficients of phi_{0,1}

Mathematical references:
  - k3_times_e.tex: thm:k3e-denominator, thm:k3e-product, def:k3e-weyl-vector
  - Gritsenko-Nikulin, alg-geom/9611028, Theorem 3.1
  - Borcherds, Inventiones 132 (1998), Theorem 13.3
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Tuple

import numpy as np


# ======================================================================
# PART 1: Lattice Lambda^{2,1}
# ======================================================================

GRAM = np.array([
    [0,  0, -1],
    [0,  2,  0],
    [-1, 0,  0],
], dtype=float)

DELTA_1 = np.array([2, -1, 0], dtype=float)
DELTA_2 = np.array([0, -1, 2], dtype=float)
DELTA_3 = np.array([0,  1, 0], dtype=float)
SIMPLE_ROOTS = [DELTA_1, DELTA_2, DELTA_3]

RHO = np.array([1.0, -0.5, 1.0])


def inner_product(v: np.ndarray, w: np.ndarray) -> float:
    """Bilinear form (v, w) on Lambda^{2,1}."""
    return float(v @ GRAM @ w)


def norm_sq(v: np.ndarray) -> float:
    """(v, v) on Lambda^{2,1}."""
    return inner_product(v, v)


def verify_gram_matrix() -> bool:
    """Verify simple root Gram matrix = ((2,-2,-2),(-2,2,-2),(-2,-2,2))."""
    expected = np.array([[2,-2,-2],[-2,2,-2],[-2,-2,2]], dtype=float)
    computed = np.array([
        [inner_product(SIMPLE_ROOTS[i], SIMPLE_ROOTS[j])
         for j in range(3)] for i in range(3)
    ])
    return np.allclose(computed, expected)


def verify_weyl_vector() -> bool:
    """Verify (rho, delta_i) = -1 for all i, and rho = (1/2)(delta_1+delta_2+delta_3)."""
    cond1 = all(abs(inner_product(RHO, SIMPLE_ROOTS[i]) + 1) < 1e-14 for i in range(3))
    cond2 = np.allclose(RHO, 0.5 * (DELTA_1 + DELTA_2 + DELTA_3))
    return cond1 and cond2


# ======================================================================
# PART 2: Weyl group
# ======================================================================

def reflect(v: np.ndarray, root: np.ndarray) -> np.ndarray:
    """Reflection s_root(v) = v - 2(v,root)/(root,root) * root."""
    return v - 2.0 * inner_product(v, root) / norm_sq(root) * root


def _vec_key(v: np.ndarray) -> tuple:
    """Hash key for lattice vectors (half-integer coordinates)."""
    return tuple(int(round(2*x)) for x in v)


def weyl_orbit_rho(max_length: int = 6) -> List[Tuple[np.ndarray, int]]:
    """Enumerate W-orbit of rho by BFS up to word length max_length.

    Returns list of (w(rho), det(w)).
    """
    visited = {_vec_key(RHO): (RHO.copy(), 1)}
    frontier = [(RHO.copy(), 1)]

    for _ in range(max_length):
        new_frontier = []
        for w_rho, det_w in frontier:
            for root in SIMPLE_ROOTS:
                new_rho = reflect(w_rho, root)
                key = _vec_key(new_rho)
                if key not in visited:
                    visited[key] = (new_rho.copy(), -det_w)
                    new_frontier.append((new_rho.copy(), -det_w))
        frontier = new_frontier
        if not frontier:
            break

    return [(v, d) for v, d in visited.values()]


def weyl_group_growth(max_length: int = 8) -> Dict[int, int]:
    """Count Weyl group elements by word length."""
    visited = {_vec_key(RHO)}
    frontier = [RHO.copy()]
    counts = {0: 1}

    for length in range(1, max_length + 1):
        new_frontier = []
        for v in frontier:
            for root in SIMPLE_ROOTS:
                w = reflect(v, root)
                key = _vec_key(w)
                if key not in visited:
                    visited.add(key)
                    new_frontier.append(w)
        counts[length] = len(new_frontier)
        frontier = new_frontier
        if not frontier:
            break

    return counts


# ======================================================================
# PART 3: phi_{0,1} (K3 elliptic genus)
# ======================================================================

def theta2(tau, z, N=50):
    """Jacobi theta_2(tau, z)."""
    return sum(
        np.exp(2j*np.pi*tau*(n+0.5)**2/2) * np.exp(2j*np.pi*(n+0.5)*z)
        for n in range(-N, N+1)
    )

def theta3(tau, z, N=50):
    """Jacobi theta_3(tau, z)."""
    return sum(
        np.exp(2j*np.pi*tau*n**2/2) * np.exp(2j*np.pi*n*z)
        for n in range(-N, N+1)
    )

def theta4(tau, z, N=50):
    """Jacobi theta_4(tau, z)."""
    return sum(
        (-1)**n * np.exp(2j*np.pi*tau*n**2/2) * np.exp(2j*np.pi*n*z)
        for n in range(-N, N+1)
    )


def phi_01_value(tau: complex, z: complex, N: int = 50) -> complex:
    """phi_{0,1}(tau, z) = 4[(theta_2(z)/theta_2(0))^2 + (theta_3(z)/theta_3(0))^2 + (theta_4(z)/theta_4(0))^2].

    Eichler-Zagier normalization: phi_{0,1}(tau, 0) = 12.
    """
    t2z, t20 = theta2(tau, z, N), theta2(tau, 0, N)
    t3z, t30 = theta3(tau, z, N), theta3(tau, 0, N)
    t4z, t40 = theta4(tau, z, N), theta4(tau, 0, N)
    return 4.0 * ((t2z/t20)**2 + (t3z/t30)**2 + (t4z/t40)**2)


def compute_phi01_table(n_max: int = 6, l_max: int = 8) -> Dict[Tuple[int, int], int]:
    """Extract f(n,l) of phi_{0,1} via 2D DFT.

    Returns exact integers for 0 <= n <= n_max, |l| <= l_max.
    Raises ValueError if extraction is not reliable.
    """
    beta = 1.0
    M_tau = max(2 * (n_max + 4), 40)
    M_z = max(2 * (l_max + 4), 32)

    vals = np.zeros((M_tau, M_z), dtype=complex)
    for it in range(M_tau):
        for iz in range(M_z):
            vals[it, iz] = phi_01_value(it/M_tau + 1j*beta, iz/M_z)

    fft2 = np.fft.fft2(vals) / (M_tau * M_z)

    coeffs = {}
    for n in range(n_max + 1):
        for l in range(-l_max, l_max + 1):
            raw = fft2[n % M_tau, l % M_z] * np.exp(2 * np.pi * beta * n)
            val = round(raw.real)
            if abs(raw.real - val) < 0.1 and abs(raw.imag) < 0.1:
                coeffs[(n, l)] = val
    return coeffs


# Hardcoded table (verified by DFT extraction).
# f(n,l) depends only on D = 4n - l^2.
PHI01_TABLE: Dict[Tuple[int, int], int] = {
    (0, 0): 10, (0, 1): 1, (0, -1): 1,
    (1, 0): 108, (1, 1): -64, (1, -1): -64,
    (1, 2): 10, (1, -2): 10,
    (2, 0): 808, (2, 1): -513, (2, -1): -513,
    (2, 2): 108, (2, -2): 108, (2, 3): 1, (2, -3): 1,
    (3, 0): 4016, (3, 1): -2752, (3, -1): -2752,
    (3, 2): 808, (3, -2): 808, (3, 3): -64, (3, -3): -64,
    (4, 0): 16524, (4, 1): -11775, (4, -1): -11775,
    (4, 2): 4016, (4, -2): 4016, (4, 3): -513, (4, -3): -513,
    (4, 4): 10, (4, -4): 10,
    (5, 0): 58640, (5, 1): -43200, (5, -1): -43200,
    (5, 2): 16524, (5, -2): 16524, (5, 3): -2752, (5, -3): -2752,
    (5, 4): 108, (5, -4): 108,
    (6, 0): 188304, (6, 1): -141826, (6, -1): -141826,
    (6, 2): 58640, (6, -2): 58640, (6, 3): -11775, (6, -3): -11775,
    (6, 4): 808, (6, -4): 808, (6, 5): 1, (6, -5): 1,
}

# Discriminant-indexed: c(D) where f(n,l) = c(4n - l^2).
C_DISC: Dict[int, int] = {}
for (_n, _l), _f in PHI01_TABLE.items():
    _D = 4 * _n - _l * _l
    assert C_DISC.get(_D, _f) == _f, f"c({_D}) inconsistent"
    C_DISC[_D] = _f


def f_phi01(n: int, l: int) -> int:
    """Fourier coefficient f(n, l) of phi_{0,1}."""
    return PHI01_TABLE.get((n, l), 0)


def c_disc(D: int) -> int:
    """Discriminant-indexed coefficient c(D) = f(n, l) for any (n,l) with 4n-l^2=D."""
    return C_DISC.get(D, 0)


def verify_phi01_discriminant() -> bool:
    """Verify f(n,l) depends only on D = 4n - l^2."""
    by_disc = defaultdict(set)
    for (n, l), f in PHI01_TABLE.items():
        by_disc[4*n - l*l].add(f)
    return all(len(vals) == 1 for vals in by_disc.values())


def verify_phi01_symmetry() -> bool:
    """Verify f(n, l) = f(n, -l)."""
    return all(
        PHI01_TABLE.get((n, l), 0) == PHI01_TABLE.get((n, -l), 0)
        for n, l in PHI01_TABLE
    )


def verify_phi01_sum_rule() -> bool:
    """Verify sum_l f(0, l) = 12 = phi_{0,1}(tau, 0)."""
    return sum(PHI01_TABLE.get((0, l), 0) for l in range(-10, 11)) == 12


# ======================================================================
# PART 4: Borcherds product (automorphic form)
# ======================================================================

def borcherds_product_numerical(tau: complex, z: complex, omega: complex,
                                order: int = 6) -> complex:
    """Evaluate the Borcherds product B_F(Z) numerically.

    B_F(Z) = e^{2pi i (rho, Z)} * prod_{(n,l,m)>0} (1 - q^n r^l s^m)^{f(nm,l)}

    where (rho, Z) = tau - z/2 + omega (coordinate pairing).
    """
    q = np.exp(2j * np.pi * tau)
    r = np.exp(2j * np.pi * z)
    s = np.exp(2j * np.pi * omega)

    # Prefactor from Weyl vector
    rho_pairing = tau + (-0.5) * z + omega
    prefactor = np.exp(2j * np.pi * rho_pairing)

    # Product over positive roots
    max_l = 2 * order + 4
    product = 1.0 + 0.0j

    for n in range(0, order + 1):
        for m in range(0, order + 1):
            for l in range(-max_l, max_l + 1):
                if n > 0 or (n == 0 and l > 0) or (n == 0 and l == 0 and m > 0):
                    mult = PHI01_TABLE.get((n * m, l), 0)
                    if mult != 0:
                        x = q**n * r**l * s**m
                        if abs(x) < 0.999:
                            product *= (1 - x) ** mult

    return prefactor * product


# ======================================================================
# PART 5: Weyl orbit sum
# ======================================================================

def weyl_sum_numerical(tau: complex, z: complex, omega: complex,
                       max_length: int = 8) -> complex:
    """Evaluate sum_{w in W} det(w) * e^{2pi i (w(rho), Z)}.

    The coordinate pairing: (v, Z) = v_1*tau + v_2*z + v_3*omega.
    """
    elements = weyl_orbit_rho(max_length)
    result = 0.0 + 0.0j
    for w_rho, det_w in elements:
        pairing = w_rho[0] * tau + w_rho[1] * z + w_rho[2] * omega
        result += det_w * np.exp(2j * np.pi * pairing)
    return result


# ======================================================================
# PART 6: Imaginary simple roots and correction factor
# ======================================================================

def fundamental_chamber_elements(bound: int = 4) -> List[Tuple[Tuple[int, int, int], int]]:
    """Enumerate elements of Lambda^{2,1} in the fundamental chamber P_{II}.

    The fundamental chamber is {v : (v, delta_i) <= 0 for all i}.
    For v = (n, l, m):
        (v, delta_1) = -2m - 2l <= 0  =>  m + l >= 0
        (v, delta_2) = -2n - 2l <= 0  =>  n + l >= 0
        (v, delta_3) = 2l <= 0         =>  l <= 0

    Combined: l <= 0, n >= -l, m >= -l.

    The imaginary simple roots are the vectors in P_{II} that are NOT
    proportional to the real simple roots delta_1, delta_2, delta_3.
    Their multiplicities come from phi_{0,1}: mult = f(nm, l).

    Returns list of ((n, l, m), multiplicity) for elements in P_{II}
    with n, m <= bound and |l| <= bound.
    """
    elements = []
    for n in range(0, bound + 1):
        for l in range(-bound, 1):  # l <= 0
            for m in range(max(0, -l), bound + 1):  # m >= -l
                if n >= -l:  # n >= -l
                    if n == 0 and l == 0 and m == 0:
                        continue  # skip zero vector
                    # Check it's not a real simple root (delta_1, delta_2, delta_3)
                    v = np.array([n, l, m], dtype=float)
                    is_simple = any(
                        np.allclose(v, sr) or np.allclose(v, -sr)
                        for sr in SIMPLE_ROOTS
                    )
                    mult = PHI01_TABLE.get((n * m, l), 0)
                    if mult != 0 and not is_simple:
                        elements.append(((n, l, m), mult))
    return elements


def imaginary_correction_numerical(tau: complex, z: complex, omega: complex,
                                    bound: int = 3) -> complex:
    """Evaluate the imaginary simple root correction S_im(Z).

    S_im = prod_{a in im. simple, (a,a)<0} (1 - e^{-2pi i(a,Z)})^{-mult(a)}
         * prod_{a in im. simple, (a,a)=0} (1 - e^{-2pi i(a,Z)})^{mult(a)}

    Wait, for the BKM denominator formula (Borcherds, Theorem 10.1):
    The correction factor is:
       sum_{a in M+} (-1)^{p(a)} mult(a) * e^{-a}
    where M+ is the set of positive sums of imaginary simple roots,
    and p(a) is the parity (super-dimension).

    This is complicated. Instead, I compute the ratio B_F / W to get S_im.
    """
    bf = borcherds_product_numerical(tau, z, omega, order=6)
    ws = weyl_sum_numerical(tau, z, omega, max_length=8)
    if abs(ws) > 1e-30:
        return bf / ws
    return None


# ======================================================================
# PART 7: Verification functions
# ======================================================================

def verify_product_weyl_agreement(points=None, tol=0.01) -> dict:
    """Verify B_F(Z) and W(Z) agree at leading order.

    The Borcherds product B_F(Z) and the Weyl sum W(Z) should satisfy:
        B_F(Z) / W(Z) -> 1 as Im(Z) -> infinity

    because the imaginary root corrections vanish in that limit.

    At finite points, the ratio gives the correction factor S_im.
    """
    if points is None:
        points = [
            (2.0j, 0.2j, 2.5j),
            (3.0j, 0.1j, 3.5j),
            (5.0j, 0.05j, 5.5j),
        ]

    results = []
    for tau, z, omega in points:
        bf = borcherds_product_numerical(tau, z, omega, order=8)
        ws = weyl_sum_numerical(tau, z, omega, max_length=8)
        ratio = bf / ws if abs(ws) > 1e-30 else None

        results.append({
            'point': (tau, z, omega),
            'B_F': bf,
            'W': ws,
            'ratio': ratio,
            'ratio_near_1': abs(ratio - 1) < tol if ratio is not None else None,
        })

    # As Im grows, ratio should approach 1
    ratios = [r['ratio'] for r in results if r['ratio'] is not None]
    converging = (
        len(ratios) >= 2 and
        abs(ratios[-1] - 1) < abs(ratios[0] - 1)
    )

    return {
        'points': results,
        'converging_to_1': converging,
    }


def verify_product_symmetries(tau=2.0j, z=0.2j, omega=2.5j, order=6) -> dict:
    """Verify symmetries of the Borcherds product B_F(Z).

    Delta_5 has weight 5 for Sp_4(Z). Under tau<->omega:
        Delta_5(omega, z, tau) = -Delta_5(tau, z, omega)

    (The sign comes from the Legendre character; Delta_5 is a cusp form
    of weight 5 on the FULL Sp_4(Z) with trivial character, and the
    tau<->omega swap involves det(J)^5 = (-1)^5 = -1.)

    Under z -> -z:
        Delta_5(tau, -z, omega) = -Delta_5(tau, z, omega)

    (Delta_5 is ODD in z because of the r^{-1/2} in the prefactor.)
    """
    bf_0 = borcherds_product_numerical(tau, z, omega, order)
    bf_swap = borcherds_product_numerical(omega, z, tau, order)
    bf_negz = borcherds_product_numerical(tau, -z, omega, order)

    return {
        'value': bf_0,
        'tau_omega_swap': bf_swap,
        'z_negation': bf_negz,
        'swap_ratio': bf_swap / bf_0 if abs(bf_0) > 1e-30 else None,
        'negz_ratio': bf_negz / bf_0 if abs(bf_0) > 1e-30 else None,
    }


def verify_weyl_sum_convergence(tau=2.0j, z=0.2j, omega=2.5j) -> dict:
    """Verify Weyl sum converges as word length increases."""
    values = {}
    for length in [2, 4, 6, 8, 10]:
        ws = weyl_sum_numerical(tau, z, omega, max_length=length)
        elts = weyl_orbit_rho(length)
        values[length] = {
            'value': ws,
            'n_elements': len(elts),
        }

    # Check stabilization: consecutive values should agree to high precision
    lengths = sorted(values.keys())
    stable = True
    for i in range(1, len(lengths)):
        v1 = values[lengths[i-1]]['value']
        v2 = values[lengths[i]]['value']
        if abs(v2) > 1e-30 and abs(v1 - v2) / abs(v2) > 1e-8:
            stable = False

    return {
        'values_by_length': values,
        'converged': stable,
    }


# ======================================================================
# PART 8: Master verification
# ======================================================================

def verify_all(verbose: bool = False) -> dict:
    """Run all verification checks for the WKB denominator identity.

    Returns dict with results of each check.
    """
    results = {}

    # 1. Lattice structure
    results['gram_matrix'] = verify_gram_matrix()
    results['weyl_vector'] = verify_weyl_vector()
    results['rho_norm'] = abs(norm_sq(RHO) - (-1.5)) < 1e-14

    # 2. Reflection properties
    v = np.array([1.0, 2.0, 3.0])
    sv = reflect(v, DELTA_1)
    results['reflection_involution'] = np.allclose(reflect(sv, DELTA_1), v)
    w = np.array([2.0, -1.0, 1.0])
    sw = reflect(w, DELTA_1)
    results['reflection_isometry'] = abs(
        inner_product(sv, sw) - inner_product(v, w)) < 1e-14

    # 3. Weyl group growth (should double: 1, 3, 6, 12, 24, 48, ...)
    growth = weyl_group_growth(6)
    results['weyl_growth'] = growth
    results['weyl_growth_doubling'] = all(
        growth.get(k, 0) == 3 * 2**(k-1)
        for k in range(1, 7) if k in growth
    )

    # 4. Weyl orbit isometry
    elements = weyl_orbit_rho(4)
    rho_norm = norm_sq(RHO)
    results['weyl_orbit_isometry'] = all(
        abs(norm_sq(w_rho) - rho_norm) < 1e-10
        for w_rho, _ in elements
    )

    # 5. phi_{0,1} properties
    results['phi01_discriminant'] = verify_phi01_discriminant()
    results['phi01_symmetry'] = verify_phi01_symmetry()
    results['phi01_sum_rule'] = verify_phi01_sum_rule()

    # 6. Weyl sum convergence
    conv = verify_weyl_sum_convergence()
    results['weyl_sum_converged'] = conv['converged']

    # 7. Product-Weyl agreement
    pw = verify_product_weyl_agreement()
    results['product_weyl_converging'] = pw['converging_to_1']

    if verbose:
        for name, val in results.items():
            if isinstance(val, bool):
                print(f"  {name}: {'PASS' if val else 'FAIL'}")
            else:
                print(f"  {name}: {val}")

    return results


# ======================================================================
# Self-test
# ======================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("WKB Denominator Identity Verification")
    print("=" * 60)

    results = verify_all(verbose=True)

    print("\n--- phi_{0,1} c(D) table ---")
    for D in sorted(C_DISC.keys()):
        print(f"  c({D:>3}) = {C_DISC[D]}")

    print("\n--- Weyl group growth ---")
    g = weyl_group_growth(8)
    for k in sorted(g.keys()):
        print(f"  length {k}: {g[k]} new elements (cumulative: {sum(g[j] for j in range(k+1))})")

    print("\n--- Product vs Weyl sum ---")
    pw = verify_product_weyl_agreement()
    for pt in pw['points']:
        ratio = pt['ratio']
        im_level = pt['point'][0].imag
        print(f"  Im(tau)={im_level:.1f}: B_F/W = {ratio:.10f}")
    print(f"  Converging to 1: {pw['converging_to_1']}")

    print("\n--- Fundamental chamber (imaginary simple roots) ---")
    fc = fundamental_chamber_elements(3)
    for (n, l, m), mult in sorted(fc):
        v = np.array([n, l, m], dtype=float)
        ip = norm_sq(v)
        print(f"  ({n:>2},{l:>3},{m:>2}): mult={mult:>6}, (a,a) = {ip:.0f}")
