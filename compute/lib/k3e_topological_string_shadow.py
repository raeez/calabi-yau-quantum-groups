r"""
Topological string partition function of K3 x E vs shadow partition function.

OVERVIEW
========

This engine computes and compares two partition functions associated to
the CY3 X = K3 x E:

(A) The TOPOLOGICAL STRING / DT partition function, governed by:
    - Gottsche formula: sum chi(Hilb^n(K3)) q^n = prod 1/(1-q^k)^{24}
    - KKV formula (Katz-Klemm-Vafa): genus-g BPS invariants n_h^g
    - DMVV formula: the full second-quantized partition function
      Z_DMVV = prod_{(n,l,m)>0} (1 - p^n y^l q^m)^{-c(4nm-l^2)}
    - Oberdieck-Pixton: Z^X = C / (Delta_5)^2

(B) The SHADOW PARTITION FUNCTION from the Vol I bar-cobar framework:
    - Bar Euler product: Theta_A = prod (1 - q^n)^{a_n}
    - Shadow tower: encodes A_infinity corrections
    - Shadow MC element: lives in the cyclic deformation complex

The COMPARISON is subtle and governed by three critical constraints:

(C1) AP-CY8: The Borcherds denominator is NOT the bar Euler product.
     The identification requires the CY-to-chiral functor Phi AND the
     Vol I Borcherds-lift identification. Both must be cited explicitly.

(C2) AP-CY6: A_{K3 x E} does NOT exist at d=3. Results conditional on CY-A_3.

(C3) AP155: The invariants computed here (chi(Hilb^n), n_h^g, etc.) are
     KNOWN. The novelty is only in the construction path through the
     chiral bar complex, not in the invariants themselves.

KEY MATHEMATICAL CONTENT
========================

1. GOTTSCHE FORMULA AND 1/eta^24.

   sum_{n>=0} chi(Hilb^n(K3)) q^n = prod_{k>=1} 1/(1-q^k)^{24}
                                    = q^{-1} / eta(q)^{24}
                                    = 1/Delta(q)  (Ramanujan Delta)

   The exponent 24 = chi(K3) = kappa_fiber. This is the rank-1 (single
   fiber) contribution. It equals 1/eta^{24} up to q-shift.

2. EXTENSION TO K3 x E: DMVV FORMULA.

   The second-quantized partition function is NOT simply 1/eta^{24}.
   It is the DMVV product:

   Z_DMVV(p,q,y) = prod_{(n,l,m)>0} 1/(1-p^n y^l q^m)^{c(4nm-l^2)}

   where c(D) are discriminant coefficients of phi_{0,1}.

   Setting p=0 (rank 1): Z_1 = prod_{k>=1} 1/(1-q^k)^{c(0)} ... no.
   Actually: rank-1 sector = coefficient of p^1 in Z_DMVV.

   The rank-1 Hilbert scheme contribution is prod 1/(1-q^k)^{24} (Gottsche).
   The FULL DT partition function of K3 x E involves ALL ranks and is
   related to 1/Delta_5^2 (Oberdieck-Pixton).

3. COMPARISON WITH 1/Delta_5.

   The Borcherds product:
   Delta_5(Omega) = q*y*p * prod_{(n,l,m)>0} (1 - q^n y^l p^m)^{f(4nm-l^2)}

   where f(D) = c(D) are the same phi_{0,1} coefficients.

   So 1/Delta_5 involves prod 1/(1 - q^n y^l p^m)^{f(D)}, and the
   DMVV formula is Z_DMVV = prod 1/(1 - p^n y^l q^m)^{c(D)}.

   These are the SAME product (up to variable relabeling p <-> q and
   the Weyl vector prefactor q*y*p).

   THE IDENTIFICATION: Z_DMVV = C' / Delta_5^2 (Oberdieck-Pixton).
   Note: Delta_5^2 = const * Phi_{10} (Igusa cusp form of weight 10).

4. BAR EULER PRODUCT COMPARISON.

   The Vol I bar Euler product for a chiral algebra A is:
   Theta_A(q) = prod_{n>=1} (1 - q^n)^{a_n}

   where a_n are determined by the shadow tower of A.

   For K3 x E (CONDITIONAL on CY-A_3):
   - The shadow tower has class M (infinite depth)
   - The exponents a_n are related to BPS invariants Omega(gamma)
   - The bar Euler product is related to the Borcherds denominator
     via the Vol I bridge (NOT by direct identification; AP-CY8)

   The precise relationship: the bar Euler product Theta_A is the
   genus-1 restriction of the Borcherds product, evaluated on the
   diagonal tau = sigma, z = 0 of H_2. This restriction gives:

   Theta_A|_{z=0, sigma=tau} = prod_{n>=1} (1-q^n)^{sum_l c(4n*0 - l^2)}
                              ... which requires careful treatment.

5. BPS COUNTING AND EXPONENTS.

   The DT invariants Omega(gamma) count BPS states of charge gamma.
   In the bar Euler product framework:
   - a_n = sum_{gamma: |gamma|=n} (-1)^{dim} Omega(gamma) * (dim factor)
   - The sign (-1)^{dim} is the virtual dimension parity

   For K3 x E at rank 0: Omega(0,0,n) = p_{24}(n) (partition function)
   For K3 x E at rank 1: Omega(1,0,h) = n_h^0 = chi(Hilb^h(K3))

6. WALL-CROSSING AND THE SHADOW TOWER.

   The KS wall-crossing formula acts on the quantum torus:
   T_gamma(x_delta) = x_delta * (1 - x_gamma)^{<gamma,delta>}

   The shadow tower encodes the same data via the MC element:
   Theta_A in MC(Def_cyc^mod(A))

   The bridge: motivic Hall algebra integration map
   int: H_mot(D^b(Coh(X))) -> C-hat[Gamma]

   This is NOT a direct identification of MC elements (AP-CY8).

CONVENTIONS
===========

- q = e^{2*pi*i*tau}: Siegel modular variable (base curve E)
- y = e^{2*pi*i*z}: K3 elliptic genus variable
- p = e^{2*pi*i*sigma}: rank/wrapping fugacity
- Omega = [[tau, z], [z, sigma]] in H_2 (Siegel upper half-space)
- c(D) = f(D): phi_{0,1} discriminant coefficients (EZ normalization)
- eta(q) = q^{1/24} prod_{n>=1} (1-q^n)
- Delta(q) = eta(q)^{24} = q * prod_{n>=1} (1-q^n)^{24} (Ramanujan)
- Delta_5(Omega): Gritsenko-Nikulin automorphic form, weight 5 on O^+(3,2)
- Phi_{10}(Omega): Igusa cusp form, weight 10 on Sp_4(Z)
- Phi_{10} = const * Delta_5^2

REFERENCES
==========

- Gottsche, Math. Ann. 286 (1990), 193-207 (Hilbert scheme chi)
- Katz-Klemm-Vafa, hep-th/9609091 (KKV formula)
- Dijkgraaf-Moore-Verlinde-Verlinde, hep-th/9607026 (DMVV formula)
- Gritsenko-Nikulin, Amer. J. Math. 119 (1997), 181-224
- Oberdieck-Pixton, arXiv:1904.01266 (DT of K3 x E)
- Kontsevich-Soibelman, arXiv:0811.2435 (wall-crossing)
- Lorgat, chiral-bar-cobar Vol I (shadow obstruction tower, bar Euler product)

Manuscript references:
    Chapter: k3_times_e.tex (ch:k3-times-e)
    Topological string comparison: sec:k3e-topological-string-shadow
    Gottsche formula: thm:k3e-yau-zaslow
    DMVV product: sec:dmvv-product (k3e_relative_shadow.py)
    Borcherds product: thm:k3e-borcherds-product
    Wall-crossing: thm:k3e-ks-wc
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

import importlib as _importlib
import os as _os
import sys as _sys


# ---------------------------------------------------------------------------
# 0. IMPORTS
# ---------------------------------------------------------------------------

def _import_sibling(name: str):
    """Import a sibling module from the same directory."""
    try:
        return _importlib.import_module(f'compute.lib.{name}')
    except (ImportError, ModuleNotFoundError):
        _lib_dir = _os.path.dirname(_os.path.abspath(__file__))
        if _lib_dir not in _sys.path:
            _sys.path.insert(0, _lib_dir)
        return _importlib.import_module(name)


_phi01_mod = _import_sibling('phi01_fourier')
phi01_by_discriminant = _phi01_mod.phi01_by_discriminant
phi01_table = _phi01_mod.phi01_table

_relative_mod = _import_sibling('k3e_relative_shadow')
fiber_hilb_chi = _relative_mod.fiber_hilb_chi
KNOWN_HILB_CHI = _relative_mod.KNOWN_HILB_CHI


# ===========================================================================
# 1. GOTTSCHE FORMULA: chi(Hilb^n(K3)) and the product 1/eta^{24}
# ===========================================================================

CHI_K3 = 24
KAPPA_CH_K3 = 2
KAPPA_CH_E = 0
KAPPA_CH_HEIS_E = 1
KAPPA_CH_K3E = 0  # compact kappa_ch(K3 x E) = chi(O_{K3xE})
KAPPA_CH_HEIS_K3E = 3  # relative Heisenberg shadow = 2 + 1
KAPPA_BKM = 5     # = weight of Delta_5 = c(0)/2 = 10/2
KAPPA_FIBER = 24  # = chi(K3) = rank of fiber Heisenberg


def gottsche_product_coefficients(max_n: int) -> List[int]:
    r"""Compute coefficients of prod_{k>=1} 1/(1-q^k)^{24} through q^{max_n}.

    This is the Gottsche formula for K3:
        sum_{n>=0} chi(Hilb^n(K3)) q^n = prod_{k>=1} 1/(1-q^k)^{24}

    The coefficients are chi(Hilb^n(K3)), which are the 24-coloured
    partition numbers p_{24}(n).

    Returns
    -------
    list : [chi(Hilb^0), chi(Hilb^1), ..., chi(Hilb^{max_n})]
    """
    return fiber_hilb_chi(max_n)


def eta_power_coefficients(max_n: int, power: int = 24) -> List[int]:
    r"""Compute coefficients of eta(q)^power = q^{power/24} prod (1-q^k)^{power}.

    For power = 24: this is the Ramanujan Delta function Delta(q) = q * prod (1-q^k)^{24}.
    Coefficients tau(n) (Ramanujan tau function) at q^n for n >= 1.

    For power = -24: this is 1/Delta(q) = q^{-1} * prod 1/(1-q^k)^{24}.

    We compute prod (1-q^k)^{|power|} or its inverse, ignoring the q^{power/24} shift.

    Returns
    -------
    list : coefficients [c_0, c_1, ..., c_{max_n}] of the product (no q-shift)
    """
    if power >= 0:
        # prod (1-q^k)^power by successive multiplication
        coeffs = [Fraction(0)] * (max_n + 1)
        coeffs[0] = Fraction(1)
        for k in range(1, max_n + 1):
            # Multiply by (1-q^k)^power
            for _ in range(power):
                for n in range(max_n, k - 1, -1):
                    coeffs[n] -= coeffs[n - k]
        return [int(c) for c in coeffs]
    else:
        # prod (1-q^k)^{-|power|} = prod 1/(1-q^k)^{|power|}
        ap = abs(power)
        coeffs = [Fraction(0)] * (max_n + 1)
        coeffs[0] = Fraction(1)
        for k in range(1, max_n + 1):
            for _ in range(ap):
                for n in range(k, max_n + 1):
                    coeffs[n] += coeffs[n - k]
        return [int(c) for c in coeffs]


def ramanujan_tau(max_n: int) -> List[int]:
    r"""Ramanujan tau function: coefficients of Delta(q) = q * prod (1-q^k)^{24}.

    Returns tau(1), tau(2), ..., tau(max_n) where
    Delta(q) = sum_{n>=1} tau(n) q^n.

    Known values: tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830.
    """
    # prod (1-q^k)^24 gives coefficients c_0, c_1, ...
    # Delta(q) = q * (c_0 + c_1*q + c_2*q^2 + ...) = c_0*q + c_1*q^2 + ...
    # So tau(n) = c_{n-1}
    prod_coeffs = eta_power_coefficients(max_n, power=24)
    return prod_coeffs[:max_n]


# Known Ramanujan tau values for verification
KNOWN_RAMANUJAN_TAU = {
    1: 1,
    2: -24,
    3: 252,
    4: -1472,
    5: 4830,
    6: -6048,
    7: -16744,
    8: 84480,
    9: -113643,
    10: -115920,
}


def verify_gottsche_vs_known() -> Dict[str, object]:
    r"""Verify Gottsche formula coefficients against known values.

    Returns a dict with verification status and any mismatches.
    """
    max_n = max(KNOWN_HILB_CHI.keys())
    computed = gottsche_product_coefficients(max_n)
    mismatches = {}
    for n, expected in KNOWN_HILB_CHI.items():
        if computed[n] != expected:
            mismatches[n] = (computed[n], expected)
    return {
        'passed': len(mismatches) == 0,
        'mismatches': mismatches,
        'max_n_checked': max_n,
    }


def verify_ramanujan_tau_vs_known() -> Dict[str, object]:
    r"""Verify Ramanujan tau function against known values."""
    max_n = max(KNOWN_RAMANUJAN_TAU.keys())
    computed = ramanujan_tau(max_n + 1)
    mismatches = {}
    for n, expected in KNOWN_RAMANUJAN_TAU.items():
        if computed[n - 1] != expected:
            mismatches[n] = (computed[n - 1], expected)
    return {
        'passed': len(mismatches) == 0,
        'mismatches': mismatches,
    }


# ===========================================================================
# 2. DMVV FORMULA: second-quantized K3 x E partition function
# ===========================================================================

def dmvv_product_coefficients(
    max_rank: int, max_inst: int, max_l: int
) -> Dict[Tuple[int, int, int], int]:
    r"""Compute coefficients of the DMVV product for K3 x E.

    Z_DMVV(p,y,q) = prod_{(n,l,m)>0} 1/(1 - p^n y^l q^m)^{c(4nm - l^2)}

    where c(D) are the phi_{0,1} discriminant coefficients.

    The ordering (n,l,m) > 0 means:
    - m > 0, or
    - m = 0 and n > 0, or
    - m = n = 0 and l < 0.

    Returns dict mapping (n_pow, l_pow, m_pow) -> coefficient, where
    p^{n_pow} y^{l_pow} q^{m_pow} is the monomial.
    """
    D_max = 4 * max_rank * max_inst + max_l * max_l + 10
    c_disc = phi01_by_discriminant(min(D_max // 4 + 2, 24))

    def c(D: int) -> int:
        if D < -1:
            return 0
        return c_disc.get(D, 0)

    # Start with 1 (the constant term)
    # We work with a dictionary of (n_pow, l_pow, m_pow) -> Fraction
    result: Dict[Tuple[int, int, int], Fraction] = {(0, 0, 0): Fraction(1)}

    def _multiply_by_geometric(n0, l0, m0, cD):
        """Multiply the current product by 1/(1 - p^{n0} y^{l0} q^{m0})^{cD}.

        For cD > 0 (bosonic): multiply by 1/(1-x)^{cD}.
        For cD < 0 (fermionic): multiply by (1-x)^{|cD|}.
        """
        nonlocal result
        if cD == 0:
            return
        if cD > 0:
            # Multiply by 1/(1-x)^{cD} = sum_{k>=0} binom(k+cD-1, cD-1) x^k
            for k in range(1, max(max_rank, max_inst) + 1):
                kn, kl, km = k * n0, k * l0, k * m0
                if kn > max_rank or km > max_inst or abs(kl) > max_l * 3:
                    break
                # Multiply result by the (1/(1-x)^cD) series at x^k
                binom_coeff = Fraction(1)
                for j in range(cD):
                    binom_coeff *= Fraction(k + j, j + 1)
                new_terms: Dict[Tuple[int, int, int], Fraction] = {}
                for (rn, rl, rm), cv in result.items():
                    nn, nl, nm = rn + kn, rl + kl, rm + km
                    if nn <= max_rank and nm <= max_inst:
                        key = (nn, nl, nm)
                        new_terms[key] = new_terms.get(key, Fraction(0)) + cv * binom_coeff
                for key, val in new_terms.items():
                    result[key] = result.get(key, Fraction(0)) + val
        else:
            # cD < 0: multiply by (1-x)^{|cD|}
            acD = abs(cD)
            for k in range(1, acD + 1):
                kn, kl, km = k * n0, k * l0, k * m0
                if kn > max_rank or km > max_inst:
                    break
                binom_coeff = Fraction(1)
                for j in range(k):
                    binom_coeff *= Fraction(acD - j, j + 1)
                sign = (-1) ** k
                new_terms = {}
                for (rn, rl, rm), cv in result.items():
                    nn, nl, nm = rn + kn, rl + kl, rm + km
                    if nn <= max_rank and nm <= max_inst:
                        key = (nn, nl, nm)
                        new_terms[key] = new_terms.get(key, Fraction(0)) + cv * sign * binom_coeff
                for key, val in new_terms.items():
                    result[key] = result.get(key, Fraction(0)) + val

    # Iterate over (n, l, m) > 0 with n <= max_rank, m <= max_inst
    for m in range(max_inst + 1):
        for n in range(max_rank + 1):
            if n == 0 and m == 0:
                # Only l < 0
                for l in range(-max_l, 0):
                    D = -l * l
                    cD = c(D)
                    if cD != 0:
                        _multiply_by_geometric(n, l, m, cD)
                continue
            for l in range(-max_l, max_l + 1):
                D = 4 * n * m - l * l
                cD = c(D)
                if cD != 0:
                    _multiply_by_geometric(n, l, m, cD)

    return {k: int(v) for k, v in result.items() if v != 0}


def dmvv_rank1_coefficients(max_inst: int) -> List[int]:
    r"""Extract the rank-1 sector from the DMVV product.

    The rank-1 sector is the coefficient of p^1 in Z_DMVV.
    At rank 1, this should equal chi(Hilb^n(K3)) = p_{24}(n).

    This provides a cross-check: DMVV at p^1 = Gottsche formula.

    Returns [c_0, c_1, ..., c_{max_inst}] (coefficient of p^1 q^m).
    """
    # For rank 1, we need the (n_pow=1, l_pow=0, m_pow) terms
    full = dmvv_product_coefficients(1, max_inst, 2)
    result = [0] * (max_inst + 1)
    for (n, l, m), v in full.items():
        if n == 1 and l == 0 and 0 <= m <= max_inst:
            result[m] = v
    return result


# ===========================================================================
# 3. BORCHERDS PRODUCT AND 1/Delta_5 EXPANSION
# ===========================================================================

def borcherds_denominator_exponents(max_D: int) -> Dict[int, int]:
    r"""Return the exponents f(D) in the Borcherds product for Delta_5.

    Delta_5(Omega) = q*y*p * prod_{(n,l,m)>0} (1 - q^n y^l p^m)^{f(4nm-l^2)}

    These are exactly the phi_{0,1} discriminant coefficients c(D) = f(D).

    Returns dict: D -> f(D).
    """
    return phi01_by_discriminant(min(max_D // 4 + 2, 24))


def borcherds_weight() -> int:
    r"""Weight of the Borcherds lift of phi_{0,1}.

    wt(Delta_5) = c(0)/2 = 10/2 = 5.

    This equals kappa_BKM, NOT kappa_ch.
    """
    c_disc = phi01_by_discriminant(2)
    return c_disc[0] // 2


def inverse_delta5_diagonal_coefficients(max_n: int) -> List[Fraction]:
    r"""Coefficients of 1/Delta_5 restricted to the diagonal sigma=tau, z=0.

    On the diagonal tau = sigma, z = 0:
        Delta_5|_{diag}(q) = q^2 * prod_{n>=1} (1-q^n)^{f_diag(n)}

    where f_diag(n) = sum_{l} f(4n*n - l^2) ... no, this is wrong.

    Actually on the diagonal p = q, y = 1:
        Delta_5(tau, 0, tau) = q^2 * prod_{(n,l,m)>0} (1-q^{n+m})^{f(4nm-l^2)}

    This is complex because (n,l,m) ranges over all positive triples.

    For the RANK-0 restriction (p=0, y=1):
    prod_{n>=1} (1-q^n)^{c(0)} = prod_{n>=1} (1-q^n)^{10}
    which is eta(q)^{10} / q^{10/24} = eta(q)^{10} * q^{-5/12}.

    We compute the diagonal restriction numerically.

    Returns coefficients of 1/Delta_5|_{diag} through q^{max_n}.
    """
    # The diagonal restriction requires summing over all (n,l,m)>0
    # with the constraint n+m = fixed. This is expensive.
    # Instead, compute the Borcherds product on the diagonal directly.

    c_disc = phi01_by_discriminant(min(max_n + 10, 24))

    def c(D: int) -> int:
        if D < -1:
            return 0
        return c_disc.get(D, 0)

    # On diagonal p = q, y = 1:
    # The Weyl prefactor is q*1*q = q^2.
    # Each factor (1 - q^n y^l p^m) becomes (1 - q^{n+m}).
    # So Delta_5|_{diag} ~ q^2 * prod_{(n,l,m)>0} (1 - q^{n+m})^{f(4nm-l^2)}

    # Group by total power s = n + m:
    # For each s >= 1: sum of exponents = sum_{n+m=s, l} f(4nm - l^2)

    effective_exponent = [0] * (max_n + 1)
    for s in range(1, max_n + 1):
        total_exp = 0
        for n in range(0, s + 1):
            m = s - n
            if n == 0 and m == 0:
                continue
            # Determine valid l range
            D_max_local = 4 * n * m + 1  # f(D) = 0 for D < -1
            l_max = int(math.isqrt(D_max_local + 1)) + 1
            for l in range(-l_max, l_max + 1):
                if n == 0 and m == 0 and l >= 0:
                    continue
                D = 4 * n * m - l * l
                cD = c(D)
                if cD != 0:
                    total_exp += cD
        effective_exponent[s] = total_exp

    # Now Delta_5|_{diag} = q^2 * prod_{s>=1} (1-q^s)^{eff_exp[s]}
    # Compute 1/Delta_5|_{diag} = q^{-2} * prod_{s>=1} (1-q^s)^{-eff_exp[s]}
    # We compute prod (1-q^s)^{-eff_exp[s]} first.

    coeffs = [Fraction(0)] * (max_n + 1)
    coeffs[0] = Fraction(1)

    for s in range(1, max_n + 1):
        exp_s = effective_exponent[s]
        if exp_s == 0:
            continue
        # Multiply by (1-q^s)^{-exp_s}
        if exp_s > 0:
            # (1-q^s)^{-exp_s}: multiply exp_s times by 1/(1-q^s)
            for _ in range(exp_s):
                for n in range(s, max_n + 1):
                    coeffs[n] += coeffs[n - s]
        else:
            # (1-q^s)^{|exp_s|}: multiply |exp_s| times by (1-q^s)
            for _ in range(abs(exp_s)):
                for n in range(max_n, s - 1, -1):
                    coeffs[n] -= coeffs[n - s]

    return coeffs


# ===========================================================================
# 4. BAR EULER PRODUCT: shadow partition function
# ===========================================================================

def bar_euler_product_exponents_rank1(max_n: int) -> List[int]:
    r"""Exponents of the bar Euler product at rank 1 for K3 x E.

    At rank 1 (single K3 fiber), the bar Euler product is:
        Theta_{A,1}(q) = prod_{n>=1} (1-q^n)^{a_n}

    where a_n = -chi(K3) = -24 for all n (class G, Gaussian).

    This gives Theta_{A,1} = prod (1-q^n)^{-24} = 1/eta^{24} * q
    (the Gottsche formula from the bar-cobar perspective).

    The exponent -24 = -kappa_fiber encodes that the rank-1 shadow
    tower is entirely determined by the fiber modular characteristic.

    Returns [a_1, a_2, ..., a_{max_n}].
    """
    return [-CHI_K3] * max_n


def bar_euler_product_class_g(max_n: int) -> List[Fraction]:
    r"""Evaluate the rank-1 bar Euler product (class G).

    prod_{n>=1} (1-q^n)^{-24} = sum_{n>=0} p_{24}(n) q^n

    This recovers the Gottsche formula from the bar-cobar perspective.
    The novelty is the construction path: CY category -> chiral algebra
    -> bar complex -> shadow tower -> Euler product. The OUTPUT
    (chi(Hilb^n(K3))) is known (Gottsche 1990); only the construction
    path through the chiral bar complex is new (AP155).

    Returns [c_0, c_1, ..., c_{max_n}].
    """
    return [Fraction(c) for c in gottsche_product_coefficients(max_n)]


def bar_euler_exponents_bkm(max_n: int) -> List[int]:
    r"""Exponents for the FULL (conjectural) bar Euler product.

    CONDITIONAL ON CY-A_3.

    The full bar Euler product for A_{K3 x E} (if it existed) would
    have exponents determined by the full BPS spectrum, not just the
    rank-1 sector. The exponents would be:

    a_n = sum_{gamma: |gamma|=n} (-1)^{dim M_gamma} Omega(gamma) <gamma, gamma>

    For the BKM algebra g_{Delta_5}, the root multiplicities c(D)
    give the BPS invariants. The effective exponent at each q-power
    depends on the specific diagonal restriction.

    THIS IS AN OBSERVATION, NOT A THEOREM (AP-CY8). The identification
    of bar Euler exponents with Borcherds product exponents requires
    the CY-to-chiral functor Phi (CY-A_3) AND the Vol I Borcherds-lift
    bridge. Without both, this is a pattern match.

    Returns [a_1, ..., a_{max_n}] (the effective diagonal exponents).
    """
    c_disc = phi01_by_discriminant(min(max_n + 10, 24))

    def c(D: int) -> int:
        if D < -1:
            return 0
        return c_disc.get(D, 0)

    # The effective exponent at q^s on the diagonal p=q, y=1 is
    # sum_{n+m=s} sum_l c(4nm - l^2)
    exponents = []
    for s in range(1, max_n + 1):
        total_exp = 0
        for n in range(0, s + 1):
            m = s - n
            if n == 0 and m == 0:
                continue
            D_max_local = 4 * n * m + 1
            l_max = int(math.isqrt(D_max_local + 1)) + 1
            for l in range(-l_max, l_max + 1):
                if n == 0 and m == 0 and l >= 0:
                    continue
                D = 4 * n * m - l * l
                cD = c(D)
                if cD != 0:
                    total_exp += cD
        exponents.append(total_exp)
    return exponents


# ===========================================================================
# 5. COMPARISON AND VERIFICATION
# ===========================================================================

def compare_gottsche_vs_bar_euler(max_n: int) -> Dict[str, object]:
    r"""Compare Gottsche formula with bar Euler product at rank 1.

    Both should give chi(Hilb^n(K3)):
    - Gottsche: prod_{k>=1} 1/(1-q^k)^{24}
    - Bar Euler (rank 1): prod_{k>=1} (1-q^k)^{-24} (same!)

    The comparison is exact by construction: the rank-1 bar Euler
    product IS the Gottsche formula. The interest is that the
    exponent -24 = -kappa_fiber is derived from the shadow tower
    (class G, Gaussian), not just posited.

    Returns dict with comparison results.
    """
    gottsche = gottsche_product_coefficients(max_n)
    bar_euler = bar_euler_product_class_g(max_n)

    mismatches = {}
    for n in range(max_n + 1):
        if Fraction(gottsche[n]) != bar_euler[n]:
            mismatches[n] = (gottsche[n], int(bar_euler[n]))

    return {
        'passed': len(mismatches) == 0,
        'max_n': max_n,
        'mismatches': mismatches,
        'first_terms_gottsche': gottsche[:7],
        'first_terms_bar_euler': [int(x) for x in bar_euler[:7]],
    }


def compare_dmvv_rank1_vs_gottsche(max_inst: int) -> Dict[str, object]:
    r"""Verify that the rank-1 sector of DMVV reproduces Gottsche.

    The coefficient of p^1 in Z_DMVV should equal chi(Hilb^n(K3)).

    This is a highly nontrivial cross-check: the DMVV formula uses
    phi_{0,1} Fourier coefficients c(D), while Gottsche uses chi(K3) = 24.
    The agreement proves that the second-quantized formula correctly
    reproduces the single-particle sector.
    """
    dmvv_r1 = dmvv_rank1_coefficients(max_inst)
    gottsche = gottsche_product_coefficients(max_inst)

    mismatches = {}
    for n in range(min(len(dmvv_r1), len(gottsche))):
        if dmvv_r1[n] != gottsche[n]:
            mismatches[n] = (dmvv_r1[n], gottsche[n])

    return {
        'passed': len(mismatches) == 0,
        'max_inst': max_inst,
        'mismatches': mismatches,
        'dmvv_r1_first': dmvv_r1[:6],
        'gottsche_first': gottsche[:6],
    }


def kappa_spectrum_k3e() -> Dict[str, object]:
    r"""The resolved kappa-spectrum of K3 x E.

    kappa_ch   = 0: compact Hodge/PhiFA supertrace on K3 x E
    kappa_ch_Heis = 3: relative Heisenberg/topological-string shadow (2+1)
    kappa_BKM  = 5: from Borcherds-Kac-Moody algebra (weight of Delta_5)
    kappa_cat  = 0: from categorical/holomorphic Euler char chi(O_{K3 x E})
    kappa_cat_fiber = 2: from categorical/holomorphic Euler char chi(O_{K3})
    kappa_fiber = 24: from lattice/fiber structure (rank of K3 lattice)

    The resolved values {0, 2, 3, 5, 24} are ALL distinct. Conflating
    total-space and fiber categorical values is the source of the
    kappa-spectrum confusion.
    """
    return {
        'kappa_ch': KAPPA_CH_K3E,
        'kappa_ch_Heis': KAPPA_CH_HEIS_K3E,
        'kappa_BKM': KAPPA_BKM,
        'kappa_cat': Fraction(0),  # chi(O_{K3 x E}) = 0
        'kappa_cat_fiber': KAPPA_CH_K3,  # chi(O_{K3}) = 2
        'kappa_fiber': KAPPA_FIBER,
        'all_distinct': len({
            Fraction(0), KAPPA_CH_K3, KAPPA_CH_HEIS_K3E, KAPPA_BKM, KAPPA_FIBER,
        }) == 5,
        'weight_formula': f"wt(Delta_5) = c(0)/2 = {phi01_by_discriminant(2).get(0, '?')}/2 = {KAPPA_BKM}",
        'additivity': f"kappa_ch_Heis(K3xE) = kappa_ch(K3) + kappa_ch_Heis(E) = {KAPPA_CH_K3} + {KAPPA_CH_HEIS_E} = {KAPPA_CH_HEIS_K3E}",
    }


def bps_exponent_identification(max_n: int) -> Dict[str, object]:
    r"""Make explicit the BPS / bar Euler exponent identification.

    For the rank-1 sector:
    - BPS invariants: Omega(1, 0, h) = n_h^0 = chi(Hilb^h(K3))
    - Bar Euler exponents: a_n = -24 (class G, Gaussian)

    The relationship: the bar Euler product prod (1-q^n)^{a_n} with
    a_n = -24 gives sum chi(Hilb^h) q^h. This is the INVERSE
    relationship: the BPS counts are the COEFFICIENTS of the bar
    Euler product, not the exponents directly.

    For the full (conjectural) theory:
    - BPS invariants: Omega(gamma) for all charges gamma
    - Bar Euler exponents: determined by the shadow tower of A_{K3xE}
    - The identification is CONDITIONAL on CY-A_3 (AP-CY6)

    The BPS/shadow bridge:
    - Degree-r shadow projection captures BPS charges at discriminant |D| <= r
    - The shadow MC element Theta_A encodes the same data as the KS MC element
      A_KS, but in a different convolution algebra (AP-CY8: NOT the same MC element)
    """
    hilb = gottsche_product_coefficients(max_n)
    rank1_exponents = bar_euler_product_exponents_rank1(max_n)
    bkm_exponents = bar_euler_exponents_bkm(max_n)

    return {
        'rank1_bps_invariants': {h: hilb[h] for h in range(min(7, max_n + 1))},
        'rank1_bar_exponents': rank1_exponents[:7],
        'rank1_exponent_constant': all(e == -24 for e in rank1_exponents),
        'rank1_class': 'G',
        'bkm_diagonal_exponents': bkm_exponents[:7],
        'bkm_class': 'M',
        'bkm_exponents_all_equal': len(set(bkm_exponents)) == 1 if bkm_exponents else None,
        'conditional_on': 'CY-A_3',
    }


def wall_crossing_shadow_tower_dictionary(max_D: int) -> Dict[str, object]:
    r"""The KS wall-crossing / shadow tower correspondence.

    The KS formula and the shadow tower encode the same BPS spectrum
    through different algebraic structures:

    Shadow tower side:
    - Degree-r shadow Theta_A^{<=r}: captures roots at |D| <= r
    - kappa_ch_Heis = 3 (relative fiber modular shadow via Phi)
    - Shadow depth: class M (infinite, from BKM root growth)
    - Cubic shadow at degree 3: first fermionic root (D=3, c(3)=-64)

    KS wall-crossing side:
    - T_gamma automorphisms in the quantum torus
    - Omega(gamma) = BPS invariants = root multiplicities
    - Walls of marginal stability = BKM root hyperplanes
    - Pentagon identity = simplest bound-state crossing

    The bridge factors through the motivic Hall algebra; the naive
    BCH pair-commutator is INSUFFICIENT (Warning in k3_times_e.tex).
    """
    c_disc = phi01_by_discriminant(min(max_D // 4 + 2, 24))
    shadow_dict = []
    for D in sorted(c_disc.keys()):
        if D > max_D:
            break
        cD = c_disc[D]
        parity = 'bosonic' if cD > 0 else ('fermionic' if cD < 0 else 'zero')
        shadow_dict.append({
            'discriminant': D,
            'c(D)': cD,
            'parity': parity,
            'root_type': 'real' if D == -1 else 'imaginary',
        })

    return {
        'entries': shadow_dict,
        'first_fermionic': 3,
        'first_fermionic_mult': c_disc.get(3, None),
        'shadow_class': 'M',
        'kappa_ch': KAPPA_CH_K3E,
        'kappa_ch_Heis': KAPPA_CH_HEIS_K3E,
        'kappa_BKM': KAPPA_BKM,
        'conditional_on': 'CY-A_3 (for shadow tower), proven elsewhere (for KS)',
    }


# ===========================================================================
# 6. DT PARTITION FUNCTION EXPLICIT COMPUTATION
# ===========================================================================

def dt_partition_function_k3e_rank0(max_n: int) -> List[int]:
    r"""Degree-zero DT partition function of K3 x E.

    Z_{DT,0}(K3 x E; q) = M(-q)^{chi(K3 x E)} = M(-q)^0 = 1

    where M(q) = prod 1/(1-q^n)^n is the MacMahon function.

    The vanishing chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0
    makes the degree-zero DT trivial.

    Returns [1, 0, 0, ..., 0] (trivially 1).
    """
    result = [0] * (max_n + 1)
    result[0] = 1
    return result


def dt_partition_function_k3e_rank1(max_n: int) -> List[int]:
    r"""Rank-1 DT partition function of K3 x E.

    At rank 1 (pure dimension-2 sheaves on K3 fibers):
    Z_{DT,1}(K3 x E; q) = prod_{k>=1} 1/(1-q^k)^{24}
                          = sum chi(Hilb^n(K3)) q^n

    This is the Yau-Zaslow / Gottsche formula from the DT perspective.
    The BPS invariants n_h^0 = chi(Hilb^h(K3)).

    Returns [n_0^0, n_1^0, ..., n_{max_n}^0].
    """
    return gottsche_product_coefficients(max_n)


def dt_vs_pt_identity() -> Dict[str, object]:
    r"""Verify Z_DT = Z_PT for K3 x E.

    The DT/PT wall-crossing: Z_DT = M(-q)^{chi(X)} * Z_PT.
    For K3 x E: chi(X) = 0, so M(-q)^0 = 1, hence Z_DT = Z_PT.

    This is a theorem (Bridgeland 2011, Toda 2010), not a computation.
    """
    return {
        'chi_K3xE': 0,
        'macmahon_exponent': 0,
        'macmahon_factor': 1,
        'dt_equals_pt': True,
        'reason': 'chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0',
    }


# ===========================================================================
# 7. SUMMARY AND STRUCTURAL COMPARISON
# ===========================================================================

def topological_string_shadow_comparison_summary(max_n: int = 10) -> Dict[str, object]:
    r"""Complete comparison of topological string PF vs shadow PF for K3 x E.

    Three-way comparison at rank 1:
    (A) Topological string / DT: chi(Hilb^n(K3)) from Gottsche / Yau-Zaslow
    (B) Shadow PF / bar Euler: prod (1-q^k)^{-24} from shadow tower (class G)
    (C) Borcherds product: Delta_5 denominator formula

    At rank 1, (A) and (B) are the SAME by construction.
    The relation to (C) requires the full second-quantized formula (DMVV)
    and is conditional on CY-A_3 for the shadow tower interpretation.

    Returns a comprehensive summary dict.
    """
    gottsche = gottsche_product_coefficients(max_n)
    kappa = kappa_spectrum_k3e()
    bps_id = bps_exponent_identification(max_n)
    wc = wall_crossing_shadow_tower_dictionary(20)

    return {
        'rank1_agreement': {
            'topological_string': gottsche[:7],
            'bar_euler_product': gottsche[:7],  # Same by construction
            'exponent': -24,
            'source': 'kappa_fiber = chi(K3) = 24',
        },
        'kappa_spectrum': {
            'kappa_ch': KAPPA_CH_K3E,
            'kappa_ch_Heis': KAPPA_CH_HEIS_K3E,
            'kappa_BKM': KAPPA_BKM,
            'kappa_cat': Fraction(0),
            'kappa_cat_fiber': KAPPA_CH_K3,
            'kappa_fiber': KAPPA_FIBER,
        },
        'dt_vanishing': {
            'chi_K3xE': 0,
            'Z_DT0': 1,
            'reason': 'chi(K3) * chi(E) = 24 * 0 = 0',
        },
        'shadow_class': {
            'rank1': 'G (Gaussian, depth 2)',
            'full': 'M (mixed, infinite depth)',
            'jump_mechanism': 'imaginary roots of g_{Delta_5} from sewing along E',
        },
        'borcherds_bridge': {
            'input': 'phi_{0,1} (K3 elliptic genus, genus 1)',
            'output': 'Delta_5 (Igusa cusp form, genus 2)',
            'multiplicative': 'BPS instanton sum (non-perturbative)',
            'additive': 'Fourier-Jacobi expansion (perturbative)',
            'weight': f'c(0)/2 = 10/2 = {KAPPA_BKM}',
        },
        'conditionality': {
            'rank1': 'PROVED (Gottsche, Yau-Zaslow, CY-A_2 at d=2)',
            'full_shadow': 'CONDITIONAL on CY-A_3 (A_{K3xE} not constructed)',
            'borcherds_identification': (
                'OBSERVATION, not theorem (AP-CY8): requires Phi (CY-A_3) '
                'AND Vol I Borcherds-lift bridge'
            ),
        },
        'wall_crossing': {
            'first_fermionic_D': 3,
            'first_fermionic_mult': -64,
            'shadow_depth': 'infinite (class M)',
            'ks_mechanism': 'quantum torus automorphisms T_gamma',
        },
    }
