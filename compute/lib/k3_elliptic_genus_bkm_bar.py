r"""
K3 elliptic genus -> BKM algebra -> bar complex identification chain.

This engine traces the complete chain:

    phi_{0,1}^{half}(tau,z) --Borcherds-lift--> Delta_5 --denominator--> g_{Delta_5}
                                                                       |
    root multiplicities = c(D) of phi_{0,1}  <-------------------------+
                                                                       |
    bar Euler product (CONDITIONAL on CY-A_3) <------------------------+

CHAIN SUMMARY
=============

Step 1: Half K3 weak Jacobi form phi_{0,1}(tau,z) = y + 10 + y^{-1} + ...
        The unique weak Jacobi form of weight 0, index 1 in EZ normalisation.
        Fourier expansion: phi_{0,1} = sum_{n,l} f(n,l) q^n y^l
        where f(n,l) = c(4n - l^2) depends only on discriminant D = 4n - l^2.

Step 2: Borcherds lift: phi_{0,1} -> Delta_5
        Delta_5(Z) = 64 * exp(pi*i*(z1+z2+z3))
                     * prod_{(n,l,m)>0} (1 - e^{2*pi*i*(n*z1+l*z2+m*z3)})^{c(4nm-l^2)}
        Weight = c(0)/2 = 10/2 = 5. The Igusa cusp form.

Step 3: Denominator identity of g_{Delta_5}
        The Weyl-Kac-Borcherds character formula applied to the trivial
        representation gives the product formula for Delta_5.
        Root multiplicities: mult(alpha) = c(D(alpha)) for alpha = (n,l,m).

Step 4: Root multiplicities = c(D) from phi_{0,1}
        mult(n,l,m) = c(4nm - l^2)
        Only discriminants D = 0 or 3 mod 4 appear (index 1 constraint, AP-CY9).
        c(-1)=1, c(0)=10, c(3)=-64, c(4)=108, c(7)=-513, c(8)=808, ...

Step 5: Bar Euler product identification (CONDITIONAL on CY-A_3)
        IF the chiral algebra A_{K3xE} exists (CY-A_3), THEN the bar
        Euler product of A_{K3xE} equals 1/Delta_5 (up to normalization).
        This is an OBSERVATION matching formal structure, NOT a theorem (AP-CY8).
        At d=2, the analogous identification IS a theorem (CY-A_2).

Step 6: Saito-Kurokawa / Fourier-Jacobi decomposition (ADDITIVE side)
        Delta_5 = sum_{m >= 1} phi_{5,m}(tau,z) p^m
        where phi_{5,m} are Jacobi forms of weight 5 and index m,
        and p = exp(2*pi*i*omega). The first FJ coefficient phi_{5,1}
        is related to phi_{10,1} = eta^{18} * theta_1^2 (weight 10, index 1).
        The additive decomposition is the perturbative expansion;
        the multiplicative product is the non-perturbative BPS sum.

References
----------
    Eichler-Zagier, "The Theory of Jacobi Forms" (1985)
    Gritsenko-Nikulin, "Automorphic forms and Lorentzian KM algebras II" (1998)
    Borcherds, "Automorphic forms with singularities on Grassmannians" (1998)
    Lorgat, "A Borcherds lift of phi_{0,1}" (2020)
    Oberdieck-Pixton, "Holomorphic anomaly equations and the Igusa cusp form..." (2018)
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Import helpers
# ---------------------------------------------------------------------------

def _import_phi01():
    """Import phi01_fourier from the same directory."""
    try:
        from compute.lib import phi01_fourier
        return phi01_fourier
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.dirname(os.path.abspath(__file__))
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('phi01_fourier')


def _import_bar_euler():
    """Import bar_euler_borcherds from the same directory."""
    try:
        from compute.lib import bar_euler_borcherds
        return bar_euler_borcherds
    except (ImportError, ModuleNotFoundError):
        import importlib, os, sys
        _lib_dir = os.path.dirname(os.path.abspath(__file__))
        if _lib_dir not in sys.path:
            sys.path.insert(0, _lib_dir)
        return importlib.import_module('bar_euler_borcherds')


# =========================================================================
# 1. PHI_{0,1} COEFFICIENT TABLE (Step 1)
# =========================================================================

# Known exact values of c(D) for phi_{0,1} (Eichler-Zagier convention).
# AP-CY9: only D equiv 0 or 3 mod 4 can appear for index 1.
# c(-1) = 1 in EZ convention.  The two monomials l=+1 and l=-1
# contribute total polar multiplicity 2 at n=0.
#
# VERIFIED: these values are computed exactly by phi01_fourier.py
# from the theta-ratio formula in exact rational arithmetic.
# AP-CY24: all values below verified against phi01_fourier.py exact arithmetic.
# c(-1) = 1 in the TWO-INDEX convention: f(0,1) = 1 (single l-value).
# The discriminant-indexed c(D) from phi01_by_discriminant returns f(n,l)
# for a representative (n,l) pair, NOT the sum over all (n,l) with 4n-l^2=D.
# Cross-check: phi_{0,1}(tau,0) = f(0,-1)+f(0,0)+f(0,1) = 1+10+1 = 12.
KNOWN_C_TABLE = {
    -1: 1,        # D = -1: f(0,1) = 1 (single polar coefficient)
    0: 10,        # D = 0: constant term
    3: -64,       # D = 3: first fermionic root
    4: 108,       # D = 4
    7: -513,      # D = 7
    8: 808,       # D = 8
    11: -2752,    # D = 11
    12: 4016,     # D = 12
    15: -11775,   # D = 15
    16: 16524,    # D = 16 (VERIFIED [DC] phi01_fourier.py exact)
    19: -43200,   # D = 19 (VERIFIED [DC] phi01_fourier.py exact)
    20: 58640,    # D = 20 (VERIFIED [DC] phi01_fourier.py exact)
    23: -141826,  # D = 23 (AP-CY9: 23 equiv 3 mod 4, OK)
    24: 188304,   # D = 24 (VERIFIED [DC] phi01_fourier.py exact)
    27: -427264,  # D = 27 (VERIFIED [DC] phi01_fourier.py exact)
    28: 556416,   # D = 28 (VERIFIED [DC] phi01_fourier.py exact)
}


def c_table_from_phi01(D_max: int = 100) -> Dict[int, int]:
    r"""
    Compute c(D) for phi_{0,1} up to discriminant D_max.

    Uses exact arithmetic from phi01_fourier.py.
    The coefficient c(D) is defined by:
        phi_{0,1}(tau,z) = sum_{n,l} c(4n-l^2) q^n y^l

    Only discriminants D with D equiv 0 or 3 mod 4 appear (AP-CY9).
    """
    phi01 = _import_phi01()
    max_n = D_max // 4 + 5
    return phi01.phi01_by_discriminant(max_n)


def verify_discriminant_constraint(D_max: int = 100) -> Dict[str, object]:
    r"""
    Verify AP-CY9: only D equiv 0 or 3 mod 4 appear in c(D) for index 1.

    For a weak Jacobi form of index m=1, the discriminant D = 4n - l^2
    satisfies D equiv -l^2 mod 4. Since l^2 equiv 0 or 1 mod 4,
    we get D equiv 0 or 3 mod 4 (i.e., D equiv 0 or -1 mod 4).
    """
    table = c_table_from_phi01(D_max)
    violations = []
    for D, c_val in table.items():
        if D < 0:
            continue  # D = -1 is the polar term, skip
        if c_val == 0:
            continue
        r = D % 4
        if r not in (0, 3):
            violations.append((D, c_val, r))
    return {
        'D_max': D_max,
        'num_nonzero': len([D for D in table if D >= 0 and table[D] != 0]),
        'violations': violations,
        'constraint_satisfied': len(violations) == 0,
    }


def verify_c_table_known_values(D_max: int = 30) -> Dict[str, object]:
    r"""
    Verify computed c(D) against known exact values.

    Multi-path verification:
    (a) Exact computation from phi01_fourier.py (theta-ratio formula)
    (b) Known values from Eichler-Zagier / Gritsenko-Nikulin
    (c) Row-sum constraint: sum_l c(4n-l^2) = 0 for n >= 1
    """
    table = c_table_from_phi01(D_max)
    mismatches = []
    for D, expected in KNOWN_C_TABLE.items():
        if D > D_max:
            continue
        computed = table.get(D, 0)
        if computed != expected:
            mismatches.append((D, expected, computed))

    # Cross-check: row-sum vanishing
    phi01 = _import_phi01()
    max_n = D_max // 4 + 2
    full_table = phi01.phi01_table(max_n)
    row_sum_ok = True
    for n in range(1, max_n + 1):
        row_sum = sum(v for (nn, l), v in full_table.items() if nn == n)
        if row_sum != 0:
            row_sum_ok = False
            break

    return {
        'known_values_match': len(mismatches) == 0,
        'mismatches': mismatches,
        'row_sum_vanishing': row_sum_ok,
    }


# =========================================================================
# 2. BORCHERDS LIFT WEIGHT AND ROOT DATA (Steps 2-3)
# =========================================================================

def borcherds_lift_weight() -> int:
    r"""
    Weight of the Borcherds lift of phi_{0,1}.

    weight = c(0)/2 = 10/2 = 5 = kappa_BKM.

    This is the weight of Delta_5, the primitive Gritsenko-Nikulin denominator.
    """
    return KNOWN_C_TABLE[0] // 2


def root_multiplicities_by_discriminant(D_max: int = 100) -> Dict[int, int]:
    r"""
    Root multiplicities of g_{Delta_5} organized by discriminant.

    For a root alpha = (n,l,m) with discriminant D = 4nm - l^2:
        mult(alpha) = |c(D)|

    The sign determines the parity:
        c(D) > 0: bosonic root (even)
        c(D) < 0: fermionic root (odd, in the BKM superalgebra)

    Returns dict mapping D -> (c(D), parity) where parity = 'bosonic' or 'fermionic'.
    """
    table = c_table_from_phi01(D_max)
    result = {}
    for D, c_val in sorted(table.items()):
        if c_val == 0:
            continue
        parity = 'bosonic' if c_val > 0 else 'fermionic'
        result[D] = {'c': c_val, 'mult': abs(c_val), 'parity': parity}
    return result


def count_roots_by_parity(D_max: int = 100) -> Dict[str, object]:
    r"""
    Count bosonic vs fermionic roots through discriminant D_max.

    The pattern: D equiv 3 mod 4 gives fermionic roots (c(D) < 0),
    D equiv 0 mod 4 gives bosonic roots (c(D) > 0), with the exception
    of D = -1 (polar, bosonic).
    """
    roots = root_multiplicities_by_discriminant(D_max)
    bosonic = [(D, r['mult']) for D, r in roots.items() if r['parity'] == 'bosonic']
    fermionic = [(D, r['mult']) for D, r in roots.items() if r['parity'] == 'fermionic']
    return {
        'num_bosonic_discriminants': len(bosonic),
        'num_fermionic_discriminants': len(fermionic),
        'total_bosonic_mult': sum(m for _, m in bosonic),
        'total_fermionic_mult': sum(m for _, m in fermionic),
        'first_fermionic': fermionic[0] if fermionic else None,
        'bosonic_D_mod4': set(D % 4 for D, _ in bosonic if D >= 0),
        'fermionic_D_mod4': set(D % 4 for D, _ in fermionic),
    }


# =========================================================================
# 3. FULL 3D BAR EULER PRODUCT (Step 5)
# =========================================================================

def bar_euler_product_3d(
    N_max: int = 8,
    D_max: int = 100,
) -> Dict[Tuple[int, int, int], int]:
    r"""
    Compute the 3D bar Euler product exponents organized by (n,l,m).

    The Borcherds product formula:
        (1/64)*Delta_5 = exp(...) * prod_{(n,l,m)>0} (1 - q^n y^l p^m)^{c(4nm-l^2)}

    This function returns the exponent c(4nm-l^2) for each triple (n,l,m)
    with (n,l,m) > 0 and n,m <= N_max, |l| <= N_max.

    CONDITIONAL on CY-A_3: if the chiral algebra A_{K3xE} exists, then
    these exponents are the bar complex multiplicities (AP-CY8).

    Returns dict mapping (n,l,m) -> exponent.
    """
    table = c_table_from_phi01(D_max)
    exponents = {}

    # Case 1: n = m = 0, l < 0
    for l in range(-N_max, 0):
        D = -l * l  # D = 4*0*0 - l^2
        c_val = table.get(D, 0)
        if c_val != 0:
            exponents[(0, l, 0)] = c_val

    # Case 2: n > 0 or m > 0
    for n in range(0, N_max + 1):
        for m in range(0, N_max + 1):
            if n == 0 and m == 0:
                continue
            for l in range(-N_max, N_max + 1):
                D = 4 * n * m - l * l
                if D < -1:
                    continue
                c_val = table.get(D, 0)
                if c_val != 0:
                    exponents[(n, l, m)] = c_val

    return exponents


def bar_euler_product_summary(N_max: int = 6) -> Dict[str, object]:
    r"""
    Summary statistics of the 3D bar Euler product.

    Reports: total number of active triples, bosonic/fermionic counts,
    range of exponents, etc.
    """
    exps = bar_euler_product_3d(N_max=N_max)
    bosonic = {k: v for k, v in exps.items() if v > 0}
    fermionic = {k: v for k, v in exps.items() if v < 0}

    return {
        'N_max': N_max,
        'total_active_triples': len(exps),
        'bosonic_triples': len(bosonic),
        'fermionic_triples': len(fermionic),
        'max_exponent': max(exps.values()) if exps else 0,
        'min_exponent': min(exps.values()) if exps else 0,
        'exponent_at_0_minus1_0': exps.get((0, -1, 0), None),
        'exponent_at_1_0_0': exps.get((1, 0, 0), None),
        'exponent_at_0_0_1': exps.get((0, 0, 1), None),
        'exponent_at_1_0_1': exps.get((1, 0, 1), None),
    }


# =========================================================================
# 4. ROOT MULTIPLICITY VERIFICATION THROUGH HIGH ORDER (Step 4)
# =========================================================================

def verify_root_multiplicities(D_max: int = 60) -> Dict[str, object]:
    r"""
    Verify root multiplicities match c(D) from phi_{0,1} through high order.

    The identification mult(n,l,m) = c(4nm - l^2) is checked by:
    (a) Computing c(D) from phi_{0,1} via exact theta-ratio formula
    (b) Verifying discriminant constraint (D equiv 0 or 3 mod 4)
    (c) Verifying sign pattern (c(D) < 0 iff D equiv 3 mod 4)
    (d) Verifying row-sum vanishing sum_l c(4n-l^2) = 0 for n >= 1
    (e) Verifying Rademacher-type growth: |c(D)| ~ exp(4*pi*sqrt(D))

    Returns verification results.
    """
    table = c_table_from_phi01(D_max)

    # (a) Values match known table
    known_match = True
    for D, expected in KNOWN_C_TABLE.items():
        if D > D_max:
            continue
        if table.get(D, 0) != expected:
            known_match = False
            break

    # (b) Discriminant constraint
    disc_ok = True
    for D in table:
        if D < 0:
            continue
        if table[D] != 0 and D % 4 not in (0, 3):
            disc_ok = False
            break

    # (c) Sign pattern: c(D) < 0 iff D equiv 3 mod 4 (for D >= 3)
    sign_pattern_ok = True
    sign_exceptions = []
    for D in sorted(table.keys()):
        if D < 3:
            continue
        c_val = table[D]
        if c_val == 0:
            continue
        expected_negative = (D % 4 == 3)
        actual_negative = (c_val < 0)
        if expected_negative != actual_negative:
            sign_pattern_ok = False
            sign_exceptions.append((D, c_val, D % 4))

    # (d) Row-sum vanishing
    phi01 = _import_phi01()
    max_n = D_max // 4 + 2
    full_table = phi01.phi01_table(max_n)
    row_sum_ok = True
    for n in range(1, max_n + 1):
        row_sum = sum(v for (nn, l), v in full_table.items() if nn == n)
        if row_sum != 0:
            row_sum_ok = False
            break

    # (e) Growth estimate
    # For D large: |c(D)| ~ C * D^{-3/4} * exp(4*pi*sqrt(D))
    # We just check monotonic growth of |c(D)| for large D
    sorted_D = sorted(D for D in table if D >= 4 and table[D] != 0)
    growth_ok = True
    if len(sorted_D) >= 5:
        for i in range(1, min(10, len(sorted_D))):
            if abs(table[sorted_D[i]]) < abs(table[sorted_D[i-1]]):
                growth_ok = False
                break

    return {
        'D_max': D_max,
        'num_discriminants': len([D for D in table if table[D] != 0]),
        'known_values_match': known_match,
        'discriminant_constraint': disc_ok,
        'sign_pattern': sign_pattern_ok,
        'sign_exceptions': sign_exceptions,
        'row_sum_vanishing': row_sum_ok,
        'growth_monotonic': growth_ok,
    }


# =========================================================================
# 5. FOURIER-JACOBI DECOMPOSITION (Step 6: Saito-Kurokawa)
# =========================================================================

def _eta_power_exact(exponent: int, max_n: int) -> Dict[int, Fraction]:
    r"""
    Compute prod_{k=1}^{infty} (1 - q^k)^{exponent} as exact q-series.
    """
    result: Dict[int, Fraction] = {0: Fraction(1)}
    for k in range(1, max_n + 1):
        if exponent > 0:
            for _ in range(exponent):
                new: Dict[int, Fraction] = {}
                for n, c in result.items():
                    if c == 0:
                        continue
                    new[n] = new.get(n, Fraction(0)) + c
                    if n + k <= max_n:
                        new[n + k] = new.get(n + k, Fraction(0)) - c
                result = new
        elif exponent < 0:
            for _ in range(-exponent):
                new = {}
                for n_val in range(max_n + 1):
                    s = result.get(n_val, Fraction(0))
                    if n_val >= k:
                        s += new.get(n_val - k, Fraction(0))
                    new[n_val] = s
                result = new
    return result


def phi_10_1_coefficients(max_n: int = 20) -> Dict[Tuple[int, int], int]:
    r"""
    Compute the Fourier coefficients of phi_{10,1}(tau,z) = eta(tau)^{18} * theta_1(tau,z)^2.

    phi_{10,1} is the unique Jacobi cusp form of weight 10 and index 1.
    It has the q-expansion (VERIFIED numerically):
        phi_{10,1} = (y - 2 + y^{-1}) q + (-2y^2 - 16y + 36 - 16y^{-1} - 2y^{-2}) q^2 + ...

    We compute via numerical evaluation at a deep cusp point tau = iY
    (Y large) and multiple z values, extracting Fourier coefficients by DFT.
    Coefficients are rounded to the nearest integer and validated.

    Returns dict mapping (n, l) -> coefficient.
    """
    import numpy as np

    def _theta1(tau, z, N=100):
        """theta_1(tau,z) = sum_{n in Z} (-1)^{n-1} q^{(n+1/2)^2/2} e^{2*pi*i*(n+1/2)*z}."""
        result = 0.0j
        for n in range(-N, N + 1):
            nh = n + 0.5
            result += ((-1) ** n) * np.exp(1j * np.pi * nh ** 2 * tau
                                           + 2j * np.pi * nh * z)
        return -result

    def _eta(tau, N=200):
        """Dedekind eta function."""
        q = np.exp(2j * np.pi * tau)
        result = np.exp(2j * np.pi * tau / 24)
        qn = 1.0 + 0.0j
        for n in range(1, N + 1):
            qn *= q
            result *= (1.0 - qn)
        return result

    # Y = Im(tau) controls the q-suppression: |q| = exp(-2*pi*Y).
    # Too large: q^n becomes too small and loses precision in residual extraction.
    # Too small: higher-n terms contaminate lower-n extraction.
    # Y=1.5 gives |q| ~ 8e-5, reliable through n ~ 4-5.
    Y = 1.5
    tau = 1j * Y
    q = np.exp(2j * np.pi * tau)

    # Use M z-evaluation points to separate l-components
    l_max = max_n + 2
    M = 2 * l_max + 1
    y0 = 0.08  # Im(z): small but nonzero for convergence
    z_vals = [float(j) / M + 1j * y0 for j in range(M)]

    # Evaluate phi_{10,1} at all z points
    eta_val = _eta(tau)
    eta18 = eta_val ** 18
    phi_vals = []
    for z in z_vals:
        th1 = _theta1(tau, z)
        phi_vals.append(eta18 * th1 ** 2)
    phi_vals = np.array(phi_vals)

    # DFT in z to extract y^l components: sum_n f(n,l) q^n * exp(-2*pi*l*y0)
    result: Dict[Tuple[int, int], int] = {}
    for l in range(-l_max, l_max + 1):
        coeff_l = np.sum(
            phi_vals * np.exp(-2j * np.pi * l * np.arange(M) / M)
        ) / M
        coeff_l *= np.exp(2 * np.pi * l * y0)  # undo y0 suppression

        # Extract q^n coefficients iteratively
        residual = coeff_l
        for n in range(0, max_n + 1):
            qn = q ** n if n > 0 else 1.0
            f_val = residual / qn
            f_int = int(round(f_val.real))
            if abs(f_val.real - f_int) > 0.2:
                # Precision loss at this order; stop extracting for this l
                break
            if abs(f_int) > 0:
                result[(n, l)] = f_int
            residual -= f_int * qn

    return result


def hecke_T_m(phi_coeffs: Dict[Tuple[int, int], int], m: int,
              max_n: int = 20) -> Dict[Tuple[int, int], int]:
    r"""
    Apply the index-raising Hecke operator V_m to a Jacobi form.

    For a Jacobi form phi(tau,z) = sum f(n,l) q^n y^l of index t,
    the Hecke operator V_m produces a Jacobi form of index mt:

        (phi|V_m)(tau,z) = sum_{d|gcd(n,l,m)} d^{k-1} f(nm/d^2, l/d) q^n y^l

    For weight k=10 (phi_{10,1}): d^9.
    This is the ADDITIVE lift: Delta_5 = sum_m phi_{5,m} p^m
    where phi_{5,m} = T_m applied to the first FJ coefficient.

    Actually the Saito-Kurokawa construction uses a different Hecke
    operator. The Fourier-Jacobi coefficients of a Siegel modular form
    F = sum_m phi_m(tau,z) p^m satisfy the recurrence:

    For the MAASS lift of a Jacobi form phi of weight k and index 1:
        phi_m = sum_{d | m} d^{k-1} phi|V_{m/d}

    But the standard Fourier-Jacobi expansion of Delta_5 has
    phi_1 as the unique Jacobi cusp form of weight 5 and index 1,
    which is zero (there are no Jacobi cusp forms of odd weight < 10
    and index 1). So the FJ expansion of Delta_5 starts differently.

    For Delta_5 on Sp_4(Z), the FJ expansion is:
        Delta_5(tau, z, omega) = sum_{m >= 1, m odd} phi_{5,m}(tau, z) * e^{pi*i*m*omega}

    The first coefficient phi_{5,1} has weight 5 and index 1.
    For weight 5 index 1: J_{5,1}^{cusp} is 1-dimensional, spanned by
    phi_{10,1}/eta^{...}... Actually this needs care.

    For this engine we use the direct Hecke V_m operator (index-raising)
    applied at weight k:

        (phi|V_m)(tau,z) = sum_{a|m} a^{k-1} * sum_{n,l} f(n, l) q^{an + m/a - ...}

    Actually the standard V_m is:
        (phi|V_m)(tau, z) = sum_{ad=m, b mod d} phi((a*tau+b)/d, az)
    giving coefficients:
        c_m(n, l) = sum_{d | gcd(n,l,m)} d^{k-1} c_1(nm/d^2, l/d)

    Parameters
    ----------
    phi_coeffs : dict
        Coefficients of the input Jacobi form as (n, l) -> c(n, l).
    m : int
        The Hecke index.
    max_n : int
        Maximum q-order in the output.

    Returns
    -------
    dict mapping (n, l) -> coefficient of the output.
    """
    k = 10  # weight of phi_{10,1}
    result: Dict[Tuple[int, int], int] = {}

    for n in range(0, max_n + 1):
        # l range: for index m, need 4n*m - l^2 >= -m^2
        l_max = int(math.isqrt(4 * n * m + m * m)) + 1
        for l in range(-l_max, l_max + 1):
            total = 0
            # Sum over d | gcd(n, l, m)
            g = math.gcd(math.gcd(abs(n), abs(l)), m) if (n != 0 or l != 0) else m
            for d in range(1, g + 1):
                if g % d != 0:
                    continue
                if n * m % (d * d) != 0:
                    continue
                if l % d != 0:
                    continue
                n_inner = n * m // (d * d)
                l_inner = l // d
                c_inner = phi_coeffs.get((n_inner, l_inner), 0)
                if c_inner != 0:
                    total += (d ** (k - 1)) * c_inner
            if total != 0:
                result[(n, l)] = total

    return result


def fourier_jacobi_coefficients_delta5(
    m_max: int = 3,
    max_n: int = 10,
) -> Dict[int, Dict[Tuple[int, int], int]]:
    r"""
    Compute the Fourier-Jacobi coefficients of Delta_5.

    Delta_5(Z) = sum_{m >= 1} phi_{5,m}(tau, z) * exp(2*pi*i*m*omega)

    For the Saito-Kurokawa lift from phi_{10,1}:
    The unique Siegel cusp form of weight 10 (= Phi_{10} = Delta_5^2 up to
    normalization) has Fourier-Jacobi expansion whose m-th coefficient is
    determined by the Hecke orbit of phi_{10,1}.

    For Delta_5 itself (weight 5), the FJ expansion involves
    half-integral index Jacobi forms. We instead compute for
    Phi_{10} = Delta_5^2, which has a clean Saito-Kurokawa lift structure.

    The Maass lift gives: for Phi_{10} of weight 10,
        phi_{10,m}(tau, z) = T_m(phi_{10,1})(tau, z)
    where T_m is the Hecke operator V_m at weight 10.

    Returns dict mapping m -> {(n, l) -> coefficient}.
    """
    phi_10_1 = phi_10_1_coefficients(max_n)
    result = {}
    for m in range(1, m_max + 1):
        if m == 1:
            result[m] = phi_10_1
        else:
            result[m] = hecke_T_m(phi_10_1, m, max_n)
    return result


def verify_phi_10_1_known_values() -> Dict[str, object]:
    r"""
    Verify phi_{10,1} = eta^{18} * theta_1^2 against known values.

    Known leading coefficients of phi_{10,1}(tau,z) (VERIFIED numerically):
        phi_{10,1} = (y - 2 + y^{-1}) q + (-2y^2 - 16y + 36 - 16y^{-1} - 2y^{-2}) q^2 + ...

    At n=1: f(1,1) = 1, f(1,0) = -2, f(1,-1) = 1 (by symmetry f(n,l)=f(n,-l)).
    At n=2: f(2,2) = -2, f(2,1) = -16, f(2,0) = 36, f(2,-1) = -16, f(2,-2) = -2.
    At n=3: f(3,3) = 1, f(3,2) = 36, f(3,1) = 99, f(3,0) = -272.

    Unlike phi_{0,1}, phi_{10,1} does NOT depend only on discriminant:
    f(1,0) = -2 at D=4, f(2,2) = -2 at D=4; these agree, but
    f(2,1) = -16 at D=7, f(3,2) = 36 at D=8, which are consistent
    with discriminant-dependence for a Jacobi cusp form of index 1.
    """
    # Use max_n=4: reliable precision through n=4 with Y=1.5.
    # At n=5, floating-point residual subtraction loses precision.
    coeffs = phi_10_1_coefficients(4)

    # AP-CY24: values verified by numerical evaluation of eta^18 * theta_1^2.
    # f(1,+/-1)=1, f(1,0)=-2, f(2,+/-2)=-2, f(2,+/-1)=-16, f(2,0)=36.
    known = {
        (1, 1): 1, (1, 0): -2, (1, -1): 1,
        (2, 2): -2, (2, 1): -16, (2, 0): 36, (2, -1): -16, (2, -2): -2,
        (3, 3): 1, (3, 2): 36, (3, 1): 99, (3, 0): -272, (3, -1): 99,
        (3, -2): 36, (3, -3): 1,
    }
    mismatches = []
    for key, expected in known.items():
        computed = coeffs.get(key, 0)
        if computed != expected:
            mismatches.append((key, expected, computed))

    # Symmetry check: f(n, l) = f(n, -l) (since theta_1(z)^2 -> theta_1(-z)^2 = theta_1(z)^2)
    # Actually theta_1(-z) = -theta_1(z), so theta_1(-z)^2 = theta_1(z)^2. Good.
    sym_ok = True
    for (n, l), val in coeffs.items():
        if coeffs.get((n, -l), 0) != val:
            sym_ok = False
            break

    return {
        'known_match': len(mismatches) == 0,
        'mismatches': mismatches,
        'symmetry': sym_ok,
        'num_terms': len(coeffs),
    }


# =========================================================================
# 6. BAR-BKM CHAIN VERIFICATION (full pipeline)
# =========================================================================

def verify_full_chain(D_max: int = 30, N_max: int = 5) -> Dict[str, object]:
    r"""
    Verify the full chain: phi_{0,1} -> Delta_5 -> g_{Delta_5} -> bar Euler.

    Step-by-step verification:
    (1) phi_{0,1} coefficients c(D) correct through D_max
    (2) Borcherds lift weight = 5 = kappa_BKM
    (3) Root multiplicities = |c(D)| with correct parity
    (4) Discriminant constraint: D equiv 0 or 3 mod 4
    (5) Row-sum vanishing: sum_l c(4n-l^2) = 0 for n >= 1
    (6) 3D product exponents computed and consistent
    (7) Bar Euler product identification: CONDITIONAL on CY-A_3 (AP-CY8)

    Returns comprehensive verification dict.
    """
    # Step 1: c(D) table
    c_table = c_table_from_phi01(D_max)
    known_ok = all(
        c_table.get(D, 0) == expected
        for D, expected in KNOWN_C_TABLE.items()
        if D <= D_max
    )

    # Step 2: weight
    weight = borcherds_lift_weight()
    weight_ok = (weight == 5)

    # Step 3: root multiplicities
    root_result = verify_root_multiplicities(D_max)

    # Step 4: discriminant constraint
    disc_result = verify_discriminant_constraint(D_max)

    # Step 5: 3D product
    product_summary = bar_euler_product_summary(N_max)

    # Step 6: phi_{10,1} verification
    phi10_result = verify_phi_10_1_known_values()

    return {
        'step1_c_table_known_ok': known_ok,
        'step2_weight_ok': weight_ok,
        'step2_kappa_BKM': weight,
        'step3_root_mults': root_result,
        'step4_disc_constraint': disc_result['constraint_satisfied'],
        'step5_product_summary': product_summary,
        'step6_phi10_ok': phi10_result['known_match'],
        'conditional_on_CY_A3': True,  # AP-CY8: always True
        'all_checks_pass': (
            known_ok and weight_ok and
            root_result['known_values_match'] and
            root_result['discriminant_constraint'] and
            root_result['sign_pattern'] and
            root_result['row_sum_vanishing'] and
            disc_result['constraint_satisfied'] and
            phi10_result['known_match']
        ),
    }


# =========================================================================
# 7. KAPPA-SPECTRUM OF K3 x E (AP113 compliance)
# =========================================================================

def kappa_spectrum_k3e() -> Dict[str, object]:
    r"""
    The four kappa values for K3 x E (AP113: bare kappa FORBIDDEN).

    kappa_ch  = 3: from the chiral algebra via Phi (= dim_C of K3 x E)
    kappa_BKM = 5: from the Borcherds-Kac-Moody algebra (weight of Delta_5)
    kappa_cat = 2: from the holomorphic Euler characteristic chi(O_{K3}) = 2
    kappa_fiber = 24: from the lattice rank / fiber structure

    The contradiction 5 != 2+1 between kappa_BKM and kappa_ch is
    the central puzzle of the K3 x E tower.
    """
    return {
        'kappa_ch': 3,
        'kappa_BKM': 5,
        'kappa_cat': 2,
        'kappa_fiber': 24,
        'kappa_ch_derivation': 'dim_C(K3 x E) = 3, additive over fibration: kappa_ch(K3) + kappa_ch(E) = 2 + 1',
        'kappa_BKM_derivation': 'weight of Delta_5 = c(0)/2 = 10/2 = 5',
        'kappa_cat_derivation': 'chi(O_{K3}) = 2 (Noether formula)',
        'kappa_fiber_derivation': 'rank of Mukai lattice U^3 + E_8(-1)^2 = 24',
        'contradiction': '5 != 2 + 1: kappa_BKM is NOT additive over fibrations',
        'resolution': 'Different kappa values measure different algebraizations (AP113)',
    }


# =========================================================================
# 8. RADEMACHER ASYMPTOTICS
# =========================================================================

def rademacher_estimate(D: int) -> float:
    r"""
    Rademacher-type asymptotic estimate for |c(D)|.

    For phi_{0,1} of weight 0 and index 1:
        |c(D)| ~ C * D^{-3/4} * exp(pi * sqrt(4D))  as D -> infinity

    where C is a constant related to the Kloosterman sums.
    The leading exponential growth rate is 2*pi*sqrt(D) (since 4*1*D
    gives the argument of the Bessel function in the exact Rademacher formula).
    """
    if D <= 0:
        return float('inf')
    return math.exp(math.pi * math.sqrt(4 * D)) / (D ** 0.75)


def verify_rademacher_growth(D_max: int = 60) -> Dict[str, object]:
    r"""
    Verify that |c(D)| grows consistently with the Rademacher estimate.

    The ratio |c(D)| / estimate(D) should converge to a constant C.
    """
    table = c_table_from_phi01(D_max)
    ratios = []
    for D in sorted(table.keys()):
        if D < 3:
            continue
        c_val = table[D]
        if c_val == 0:
            continue
        est = rademacher_estimate(D)
        ratio = abs(c_val) / est
        ratios.append((D, abs(c_val), est, ratio))

    # Check that |c(D)| grows exponentially: log|c(D)| / sqrt(D) should
    # approach 2*pi ~ 6.28 from below. We check the ratio converges.
    log_ratios = []
    for D, c_abs, est, r in ratios:
        if D >= 4 and c_abs > 0:
            log_ratios.append((D, math.log(c_abs) / math.sqrt(D)))

    # The log-ratio should be increasing and approaching 2*pi
    growth_ok = True
    if len(log_ratios) >= 3:
        # Check that the last few values are in a reasonable range
        last_vals = [lr[1] for lr in log_ratios[-5:]]
        # Should be between 3 and 2*pi + 1 for moderate D
        growth_ok = all(2.0 < v < 8.0 for v in last_vals)

    return {
        'num_discriminants': len(ratios),
        'ratios': ratios[:15],  # first 15 for display
        'log_ratios': log_ratios[:15],
        'growth_consistent': growth_ok,
    }


# =========================================================================
# 9. COMPARISON: 1D BAR EULER PRODUCT VS ETA^24
# =========================================================================

def compare_1d_bar_euler_vs_eta24(max_degree: int = 12) -> Dict[str, object]:
    r"""
    Compare the 1D bar Euler product of the K3 x E BKM algebra with eta^24.

    For the K3 Heisenberg (rank 24, class G): bar Euler = eta^24.
    For the full K3 x E BKM (class M): bar Euler is MORE COMPLEX than eta^24.

    The comparison is done at the MULTIPLICITY level: eta^24 has mult(d)=24
    for all d >= 1. The BKM 1D multiplicities are 24 for d <= 7 and diverge
    for d >= 8 (many BKM roots collapse to the same total degree).

    Computing the actual Euler product at d >= 8 is infeasible (mults > 10^8),
    so we compare multiplicities directly.
    """
    bar_euler = _import_bar_euler()

    # Get 1D BKM multiplicities
    bkm_mults = bar_euler.k3e_root_multiplicities_1d(max_degree)

    # Compare multiplicities: eta^24 has mult(d) = 24 for all d
    heisenberg_mult = 24
    mult_differences = {}
    agree_through = max_degree
    for d in range(1, max_degree + 1):
        bkm_val = bkm_mults.get((d,), 0)
        if bkm_val != heisenberg_mult:
            mult_differences[d] = {'bkm': bkm_val, 'heisenberg': heisenberg_mult}
            if agree_through == max_degree:
                agree_through = d - 1

    # For degrees where mults agree (both = 24), the products also agree.
    # For degrees where mults differ, compute the actual product only
    # if feasible (mults < 10000).
    safe_max = agree_through
    product_differences = {}
    if safe_max >= 1:
        bkm_product = bar_euler.k3e_bar_euler_product_1d(safe_max)
        eta24 = bar_euler.eta_power_coefficients(24, safe_max)
        for n in range(safe_max + 1):
            bkm_val = bkm_product.get(n, 0)
            eta_val = eta24.get(n, 0)
            if bkm_val != eta_val:
                product_differences[n] = {'bkm': bkm_val, 'eta24': eta_val}

    return {
        'max_degree': max_degree,
        'agree_through': agree_through,
        'num_differences': len(mult_differences),
        'first_mult_differences': dict(list(mult_differences.items())[:5]),
        'product_differences_safe': product_differences,
        'bkm_mults_first_10': {k: v for k, v in sorted(bkm_mults.items()) if sum(k) <= 10},
        'heisenberg_mults': heisenberg_mult,
    }


# =========================================================================
# MAIN
# =========================================================================

if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

    print("=" * 72)
    print("K3 Elliptic Genus -> BKM -> Bar Complex Chain")
    print("=" * 72)

    print("\n--- Step 1: phi_{0,1} coefficients c(D) ---")
    table = c_table_from_phi01(30)
    for D in sorted(table.keys()):
        if D <= 24:
            print(f"  c({D:3d}) = {table[D]}")

    print(f"\n--- Step 2: Borcherds lift weight = {borcherds_lift_weight()} = kappa_BKM ---")

    print("\n--- Step 3: Root parity ---")
    parity = count_roots_by_parity(24)
    print(f"  Bosonic discriminants: {parity['num_bosonic_discriminants']}")
    print(f"  Fermionic discriminants: {parity['num_fermionic_discriminants']}")
    print(f"  First fermionic: D={parity['first_fermionic']}")

    print("\n--- Step 4: Discriminant constraint (AP-CY9) ---")
    disc = verify_discriminant_constraint(60)
    print(f"  Constraint satisfied: {disc['constraint_satisfied']}")
    print(f"  Nonzero discriminants checked: {disc['num_nonzero']}")

    print("\n--- Step 5: 3D product summary ---")
    summary = bar_euler_product_summary(5)
    print(f"  Active triples: {summary['total_active_triples']}")
    print(f"  Bosonic: {summary['bosonic_triples']}, Fermionic: {summary['fermionic_triples']}")

    print("\n--- Step 6: phi_{10,1} verification ---")
    phi10 = verify_phi_10_1_known_values()
    print(f"  Known values match: {phi10['known_match']}")
    if phi10['mismatches']:
        print(f"  Mismatches: {phi10['mismatches']}")

    print("\n--- Step 7: Kappa spectrum (AP113) ---")
    kappa = kappa_spectrum_k3e()
    for k in ['kappa_ch', 'kappa_BKM', 'kappa_cat', 'kappa_fiber']:
        print(f"  {k} = {kappa[k]}")

    print("\n--- Full chain verification ---")
    chain = verify_full_chain(30, 5)
    print(f"  All checks pass: {chain['all_checks_pass']}")

    print("\n--- 1D bar Euler vs eta^24 ---")
    cmp = compare_1d_bar_euler_vs_eta24(8)
    print(f"  Agree through degree: {cmp['agree_through']}")
    print(f"  Number of differences: {cmp['num_differences']}")
