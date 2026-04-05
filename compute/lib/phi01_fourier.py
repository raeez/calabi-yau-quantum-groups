"""
Fourier coefficients f(n, l) of the weak Jacobi form phi_{0,1} of weight 0, index 1.

    phi_{0,1}(tau, z) = sum_{n >= 0, l in Z, 4n - l^2 >= -1} f(n, l) q^n r^l

where q = exp(2 pi i tau), r = exp(2 pi i z).  The coefficient f(n, l)
depends only on the discriminant D = 4n - l^2 >= -1.

These are root multiplicities of the Borcherds--Kac--Moody superalgebra
g_{Delta_5} associated to the weight-5 Siegel paramodular form.

Computation uses the classical identity

    phi_{0,1}(tau, z) = 4 [ (theta_2(tau,z)/theta_2(tau,0))^2
                           + (theta_3(tau,z)/theta_3(tau,0))^2
                           + (theta_4(tau,z)/theta_4(tau,0))^2 ]

evaluated via lattice sums over Z^2 in exact rational arithmetic.

References:
    Eichler--Zagier, "The Theory of Jacobi Forms" (1985), Thm 9.3
    Gritsenko--Nikulin, "Automorphic forms and Lorentzian KM algebras II"
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, Tuple


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _invert_q_series(a: Dict[int, Fraction], max_n: int) -> Dict[int, Fraction]:
    """Invert a univariate q-series truncated to order max_n.  Requires a_0 != 0."""
    a0 = a.get(0, Fraction(0))
    if a0 == 0:
        raise ValueError("Leading coefficient is zero; series not invertible")
    inv_a0 = Fraction(1) / a0
    inv: Dict[int, Fraction] = {0: inv_a0}
    for n in range(1, max_n + 1):
        s = Fraction(0)
        for k in range(1, n + 1):
            ak = a.get(k, Fraction(0))
            if ak != 0:
                s += ak * inv.get(n - k, Fraction(0))
        inv[n] = -s * inv_a0
    return inv


def _mul_bivar_by_univar(
    bivar: Dict[Tuple[int, int], Fraction],
    univar: Dict[int, Fraction],
    max_ord: int,
) -> Dict[Tuple[int, int], Fraction]:
    """Multiply a bivariate (u, r)-series by a univariate u-series."""
    result: Dict[Tuple[int, int], Fraction] = {}
    for (n1, l1), c1 in bivar.items():
        if c1 == 0:
            continue
        for n2, c2 in univar.items():
            if c2 == 0:
                continue
            n = n1 + n2
            if n > max_ord:
                continue
            key = (n, l1)
            if key in result:
                result[key] += c1 * c2
            else:
                result[key] = c1 * c2
    return result


def _phi01_via_theta(max_n: int) -> Dict[Tuple[int, int], Fraction]:
    r"""
    Compute phi_{0,1} to q-order max_n using squared ratios of Jacobi theta functions.

    Works in the intermediate variable u = q^{1/2} so that all theta-squared lattice
    sums have integer u-powers.  The three squared ratios individually may have both
    even and odd u-powers, but their sum (times 4) has only even u-powers, yielding
    integer q-powers as required by modularity.

    Lattice sums run over (n1, n2) in Z^2 with n1^2 + n2^2 <= max_u.
    """
    # u = q^{1/2}: need u-order 2*max_n; add margin for series inversion stability.
    max_u = 2 * max_n + 10
    n_range = int(math.isqrt(max_u)) + 1

    # theta_3(tau,z)^2 = sum_{(n1,n2) in Z^2} u^{n1^2+n2^2} r^{n1+n2}
    # theta_4(tau,z)^2 = sum  (-1)^{n1+n2} u^{n1^2+n2^2} r^{n1+n2}
    # theta_2(tau,z)^2 = sum  u^{n1^2+n2^2+n1+n2} r^{n1+n2+1}
    #   (the q^{1/4} and r^{1/2} factors in theta_2 combine to integer u,r powers
    #    after squaring)

    t3sq:  Dict[Tuple[int, int], Fraction] = {}
    t3sq0: Dict[int, Fraction] = {}
    t4sq:  Dict[Tuple[int, int], Fraction] = {}
    t4sq0: Dict[int, Fraction] = {}
    t2sq:  Dict[Tuple[int, int], Fraction] = {}
    t2sq0: Dict[int, Fraction] = {}

    ONE = Fraction(1)

    for n1 in range(-n_range, n_range + 1):
        for n2 in range(-n_range, n_range + 1):
            ss = n1 * n1 + n2 * n2
            l = n1 + n2

            # --- theta_3^2 and theta_4^2 use u-power ss ---
            if ss <= max_u:
                key = (ss, l)
                t3sq[key] = t3sq.get(key, Fraction(0)) + ONE
                t3sq0[ss] = t3sq0.get(ss, Fraction(0)) + ONE

                sign4 = ONE if (n1 + n2) % 2 == 0 else -ONE
                t4sq[key] = t4sq.get(key, Fraction(0)) + sign4
                t4sq0[ss] = t4sq0.get(ss, Fraction(0)) + sign4

            # --- theta_2^2 uses u-power ss2 = ss + l, which can be <= max_u
            #     even when ss > max_u (when l < 0) ---
            ss2 = ss + l
            if 0 <= ss2 <= max_u:
                key2 = (ss2, l + 1)
                t2sq[key2] = t2sq.get(key2, Fraction(0)) + ONE
                t2sq0[ss2] = t2sq0.get(ss2, Fraction(0)) + ONE

    # Invert the z = 0 specializations
    inv_t3sq0 = _invert_q_series(t3sq0, max_u)
    inv_t4sq0 = _invert_q_series(t4sq0, max_u)
    inv_t2sq0 = _invert_q_series(t2sq0, max_u)

    # Squared ratios R_i(u, r) = theta_i(z)^2 / theta_i(0)^2
    R3 = _mul_bivar_by_univar(t3sq, inv_t3sq0, max_u)
    R4 = _mul_bivar_by_univar(t4sq, inv_t4sq0, max_u)
    R2 = _mul_bivar_by_univar(t2sq, inv_t2sq0, max_u)

    # phi_{0,1} = 4 * (R2 + R3 + R4)
    phi01_u: Dict[Tuple[int, int], Fraction] = {}
    FOUR = Fraction(4)
    for d in (R2, R3, R4):
        for key, val in d.items():
            if val != 0:
                phi01_u[key] = phi01_u.get(key, Fraction(0)) + FOUR * val

    # Convert u = q^{1/2} -> q: only even u-powers survive.
    phi01: Dict[Tuple[int, int], Fraction] = {}
    for (u_pow, l), val in phi01_u.items():
        if val == 0:
            continue
        if u_pow % 2 != 0:
            # Odd u-powers must cancel in the sum; assert near-zero.
            assert abs(val) < Fraction(1, 10**10), (
                f"Nonzero odd u-power: u^{u_pow} r^{l} coeff = {val}"
            )
            continue
        n = u_pow // 2
        if n > max_n:
            continue
        key = (n, l)
        phi01[key] = phi01.get(key, Fraction(0)) + val

    return phi01


def _eta_power_series(exponent: int, max_n: int) -> Dict[int, Fraction]:
    r"""
    Compute prod_{k=1}^{infinity} (1 - q^k)^{exponent} truncated to q^{max_n}.

    Uses exact arithmetic (Fraction).
    """
    from math import comb
    result: Dict[int, Fraction] = {0: Fraction(1)}
    abs_exp = abs(exponent)

    for k in range(1, max_n + 1):
        if exponent >= 0:
            # Multiply by (1 - q^k)^exponent = sum_{j=0}^{exponent} C(exp,j)(-1)^j q^{jk}
            factor: Dict[int, Fraction] = {}
            for j in range(exponent + 1):
                p = j * k
                if p > max_n:
                    break
                factor[p] = Fraction(comb(exponent, j) * ((-1) ** j))
            new: Dict[int, Fraction] = {}
            for n1, c1 in result.items():
                if c1 == 0:
                    continue
                for n2, c2 in factor.items():
                    n = n1 + n2
                    if n > max_n:
                        continue
                    new[n] = new.get(n, Fraction(0)) + c1 * c2
            result = new
        else:
            # Multiply by 1/(1-q^k)^|exponent|, done |exponent| times.
            for _ in range(abs_exp):
                new = {}
                for n_val in range(max_n + 1):
                    s = Fraction(0)
                    # 1/(1-q^k) acts as: coeff[n] = coeff[n] + coeff[n-k]
                    s = result.get(n_val, Fraction(0))
                    if n_val >= k:
                        s += new.get(n_val - k, Fraction(0))
                    new[n_val] = s
                result = new
    return result


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def phi01_coefficient(n: int, l: int, max_n: int | None = None) -> int:
    """
    Return the Fourier coefficient f(n, l) of phi_{0,1}.

    Parameters
    ----------
    n : int >= 0
        The q-exponent.
    l : int
        The r-exponent.  f(n, l) = 0 unless 4n - l^2 >= -1 (weak Jacobi bound).
    max_n : int, optional
        Truncation order for the internal q-expansion.  Defaults to n.

    Returns
    -------
    int
    """
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    if 4 * n - l * l < -1:
        # For a weak Jacobi form of index m=1, D = 4n - l^2 >= -m^2 = -1.
        return 0
    if max_n is None:
        max_n = n
    if max_n < n:
        max_n = n
    coeffs = _phi01_via_theta(max_n)
    val = coeffs.get((n, l), Fraction(0))
    result = int(val)
    assert val == result, f"Non-integer coefficient: f({n}, {l}) = {val}"
    return result


def phi01_table(max_n: int) -> Dict[Tuple[int, int], int]:
    """
    Return all nonzero Fourier coefficients f(n, l) with 0 <= n <= max_n.

    Returns
    -------
    dict mapping (n, l) -> f(n, l)
    """
    coeffs = _phi01_via_theta(max_n)
    result: Dict[Tuple[int, int], int] = {}
    for (n, l), val in sorted(coeffs.items()):
        if n < 0 or n > max_n or val == 0:
            continue
        iv = int(val)
        assert val == iv, f"Non-integer coefficient: f({n}, {l}) = {val}"
        result[(n, l)] = iv
    return result


def phi01_by_discriminant(max_n: int) -> Dict[int, int]:
    """
    Return c(D) where f(n, l) = c(4n - l^2) for phi_{0,1}.

    The coefficient depends only on the discriminant D = 4n - l^2 >= -1.

    Returns
    -------
    dict mapping D -> c(D)
    """
    table = phi01_table(max_n)
    by_disc: Dict[int, int] = {}
    for (n, l), val in table.items():
        D = 4 * n - l * l
        if D in by_disc:
            assert by_disc[D] == val, (
                f"Inconsistency: c({D}) = {by_disc[D]} vs {val} from ({n}, {l})"
            )
        else:
            by_disc[D] = val
    return by_disc


def verify_bkm_identity(max_t: int) -> bool:
    r"""
    Check whether the eta^9 identity holds for phi_{0,1} coefficients.

    The identity

        1 + (1/64) * sum_{t >= 0} f(1 + 2t, 1) * q^t  =  prod_{k >= 1} (1 - q^k)^9

    is FALSE for phi_{0,1} Fourier coefficients (it fails at q^0).
    The correct eta^9 identity involves the Fourier-Jacobi coefficients of the
    Igusa cusp form Delta_5, NOT those of phi_{0,1}.  See igusa_product_formula.py
    for a verified numerical version using Delta_5 FJ coefficients.

    This function returns False (documenting the failure), and is retained
    for regression testing to confirm that the identity is indeed false for
    phi_{0,1}.
    """
    max_n_needed = 1 + 2 * max_t
    table = phi01_table(max_n_needed)

    # LHS: 1 + (1/64) sum_{t>=0} f(1+2t, 1) q^t
    lhs: Dict[int, Fraction] = {0: Fraction(1)}
    for t in range(max_t + 1):
        n = 1 + 2 * t
        f_val = table.get((n, 1), 0)
        if f_val != 0:
            lhs[t] = lhs.get(t, Fraction(0)) + Fraction(f_val, 64)

    # RHS: prod_{k>=1} (1 - q^k)^9
    rhs = _eta_power_series(9, max_t)

    for t in range(max_t + 1):
        if lhs.get(t, Fraction(0)) != rhs.get(t, Fraction(0)):
            return False
    return True


def verify_row_sum(max_n: int) -> bool:
    """
    Verify that sum_l f(n, l) = 12 if n = 0, and 0 if n >= 1.

    This follows from phi_{0,1}(tau, 0) = 12 (a weight-0 Jacobi form evaluated
    at z = 0 equals a constant, which is 12 = 2 * (index + 1) * ... for phi_{0,1}).
    """
    table = phi01_table(max_n)
    for n in range(max_n + 1):
        row_sum = sum(v for (nn, l), v in table.items() if nn == n)
        expected = 12 if n == 0 else 0
        if row_sum != expected:
            return False
    return True


def verify_symmetry(max_n: int) -> bool:
    """Verify f(n, l) = f(n, -l) for all computed coefficients."""
    table = phi01_table(max_n)
    for (n, l), v in table.items():
        if table.get((n, -l), 0) != v:
            return False
    return True


def verify_discriminant_dependence(max_n: int) -> bool:
    """Verify f(n, l) depends only on D = 4n - l^2."""
    table = phi01_table(max_n)
    by_disc: Dict[int, int] = {}
    for (n, l), v in table.items():
        D = 4 * n - l * l
        if D in by_disc:
            if by_disc[D] != v:
                return False
        else:
            by_disc[D] = v
    return True


if __name__ == "__main__":
    print("phi_{0,1} Fourier coefficients up to q^5:\n")
    table = phi01_table(5)
    print(f"{'n':>3} {'l':>3} {'f(n,l)':>10} {'D=4n-l^2':>10}")
    print("-" * 35)
    for (n, l), val in sorted(table.items()):
        D = 4 * n - l * l
        print(f"{n:3d} {l:3d} {val:10d} {D:10d}")

    print("\nCoefficients by discriminant:")
    by_d = phi01_by_discriminant(5)
    for D in sorted(by_d):
        print(f"  c({D:3d}) = {by_d[D]}")

    print(f"\nRow sum check (n <= 5):   {verify_row_sum(5)}")
    print(f"Symmetry check (n <= 5):  {verify_symmetry(5)}")
    print(f"Discriminant dep (n <= 5): {verify_discriminant_dependence(5)}")
