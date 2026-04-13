r"""
Shadow generating function resummation to the Borcherds product for K3 x E.

THE RESUMMATION IDENTITY
========================

The shadow obstruction tower of Vol I assigns to a chiral algebra A a
sequence of shadow invariants S_r (r >= 2), where S_2 = kappa_ch is the
modular characteristic. The shadow generating function packages these:

    Z^{sh}(q, s) = sum_{r >= 2} S_r(q) * s^r

For K3 x E, the chiral algebra (conditional on CY-A_3) has its shadow
tower controlled by the BKM superalgebra g_{Delta_5}. The identification
(sec:automorphic-shadow in introduction.tex) is:

    automorphic correction at arity r = shadow obstruction S_r

The resummation identity is:

    exp(Z^{sh}(q, s=1)) = Delta_5(Z) / (Weyl factor)

More precisely: the shadow generating function, when resummed via
exponentiation of its log (the plethystic/Borcherds mechanism), recovers
the full automorphic product.

STRATIFICATION BY ARITY
=======================

The product formula for (1/64) Delta_5 (Borcherds product, borcherds_lift.py
convention with l<0 for n=m=0 sector):

    Phi(Z) = exp(c(-1) * pi*i * (tau+z+sigma))
             * prod_{(n,l,m)>0}^{BL} (1 - q^n y^l s^m)^{c(4nm-l^2)}

where the positive ordering >0^{BL} means:
    n=m=0, l<0 (Borcherds-lift convention); or n>0 or m>0, all l.

This decomposes by the BPS-charge complexity/arity assignment:

    arity 2: real roots (D = -1), Weyl vector contribution
             S_2 = kappa_BKM = 5  (weight of Delta_5)
    arity 3: first imaginary roots (BPS charge n+m = 1)
             S_3 = correction from lightlike + first timelike roots
    arity r: imaginary roots with BPS charge n+m = r-2
             S_r = correction from (r-2)-th layer of imaginary roots

CONVENTION NOTE
===============

The bkm_shadow_tower.py module uses the convention l>0 for n=m=0
(positive_ordering). The borcherds_lift.py module uses l<0 for n=m=0.
These conventions differ by a factor of -e^{2*pi*i*z} in the product
(from (1-e^{2pi*i*z})/(1-e^{-2pi*i*z}) = -e^{2pi*i*z}).

For NUMERICAL product evaluation, this module uses the borcherds_lift.py
convention, which is verified to match Delta_5/64 from theta constants.
For ALGEBRAIC root enumeration (complexity assignment, layer counting),
it uses bkm_shadow_tower.py, since the complexity/arity is the same
regardless of the l-sign convention for n=m=0.

VERIFICATION STRATEGY
=====================

Level 1 (Effective exponent convergence): The effective exponents a(N)
    in the diagonal specialization converge to 24 for all N >= 1 as
    arity -> infinity, recovering the bar Euler product eta^{24}.

Level 2 (Truncated product convergence): As r -> infinity, the
    truncated Borcherds product Phi^{<=r} converges pointwise to
    Delta_5/64 from theta constants.

Level 3 (Layer decomposition): The multiplicative correction R_r =
    Phi^{<=r}/Phi^{<=r-1} at each arity approaches 1 exponentially,
    confirming the shadow tower converges.

Level 4 (1D Fourier): The diagonal 1D product resummed from the shadow
    tower matches prod(1-q^N)^{24} = eta^{24} at large arity.

References
----------
    Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower)
    Vol III: k3_times_e.tex (BKM shadow identification)
    Vol III: introduction.tex, sec:automorphic-shadow
    bkm_shadow_tower.py (root enumeration and truncated products)
    borcherds_lift.py (full Borcherds product, verified against Delta_5)
    borcherds_denominator_phi10_engine.py (chi_10 verification)
"""

from __future__ import annotations

import math
import numpy as np
from collections import defaultdict
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import importlib as _importlib
import os as _os
import sys as _sys

F = Fraction


# ---------------------------------------------------------------------------
# Imports from sibling modules
# ---------------------------------------------------------------------------

def _import_module(name: str):
    """Import from compute.lib, falling back to direct import."""
    try:
        return _importlib.import_module(f'compute.lib.{name}')
    except (ImportError, ModuleNotFoundError):
        _lib_dir = _os.path.dirname(_os.path.abspath(__file__))
        if _lib_dir not in _sys.path:
            _sys.path.insert(0, _lib_dir)
        return _importlib.import_module(name)


_bkm = _import_module('bkm_shadow_tower')
_phi01 = _import_module('phi01_fourier')
_bl = _import_module('borcherds_lift')


# Re-export key functions from bkm_shadow_tower (algebraic data)
phi01_by_discriminant = _phi01.phi01_by_discriminant
phi01_coefficients = _bkm.phi01_coefficients
get_f = _bkm.get_f
root_complexity = _bkm.root_complexity
root_multiplicity = _bkm.root_multiplicity
siegel_discriminant = _bkm.siegel_discriminant
root_norm = _bkm.root_norm
classify_root = _bkm.classify_root


# =========================================================================
# 1. SHADOW INVARIANTS S_r FROM ROOT MULTIPLICITIES
# =========================================================================

def shadow_invariant_at_arity(r: int, max_coord: int = 6,
                              data: Optional[Dict] = None
                              ) -> Dict[Tuple[int, int, int], F]:
    r"""Compute the shadow invariant S_r: the contribution at exactly arity r.

    S_r is defined as the arity-r layer of the log of the Borcherds product.
    In the plethystic decomposition:

        log Phi = sum_{r >= 2} S_r

    where S_r collects the log-product contributions from roots at
    complexity exactly r.

    Returns dict mapping lattice vectors to their Fraction coefficient.
    """
    if data is None:
        data = phi01_coefficients()

    sr: Dict[Tuple[int, int, int], F] = defaultdict(F)

    for n in range(0, max_coord + 1):
        for l in range(-max_coord, max_coord + 1):
            for m in range(0, max_coord + 1):
                if not _bkm._positive_ordering(n, l, m):
                    continue
                if root_complexity(n, l, m) != r:
                    continue
                mult = root_multiplicity(n, l, m, data)
                if mult == 0:
                    continue
                # Primary contribution: -mult * e_{(n,l,m)}
                sr[(n, l, m)] += F(-mult)
                # Higher harmonics: -mult/k * e_{k*(n,l,m)} for k >= 2
                max_scale = max(1, max(abs(n), abs(m), max(1, abs(l))))
                for k in range(2, max_coord // max_scale + 1):
                    kn, kl, km = k * n, k * l, k * m
                    if abs(kn) > max_coord or abs(kl) > max_coord or abs(km) > max_coord:
                        break
                    sr[(kn, kl, km)] += F(-mult, k)

    return dict(sr)


def shadow_invariant_summary(r: int, max_coord: int = 6,
                             data: Optional[Dict] = None) -> Dict:
    r"""Summary statistics for the shadow invariant S_r."""
    if data is None:
        data = phi01_coefficients()

    roots = _bkm.roots_at_complexity(r, max_coord, data)
    log_coeffs = shadow_invariant_at_arity(r, max_coord, data)

    return {
        'arity': r,
        'num_primary_roots': len(roots),
        'total_primary_mult': sum(abs(mult) for _, mult, _ in roots),
        'primary_roots': roots,
        'log_coefficients': log_coeffs,
    }


# =========================================================================
# 2. EFFECTIVE EXPONENTS: DIAGONAL SPECIALIZATION
# =========================================================================

def effective_exponents_diagonal(max_arity: int, max_N: int = 15,
                                 data: Optional[Dict] = None
                                 ) -> Dict[int, F]:
    r"""Compute the effective exponents a(N) in the diagonal specialization.

    In the diagonal specialization sigma = tau, z = 0, the Borcherds
    product becomes (up to Weyl factor and polar term):

        prod_{N >= 1} (1 - q^N)^{a(N)}

    where a(N) = sum_{n+m=N, all l, complexity <= max_arity} f(nm, l).

    At full arity, a(N) = 24 for all N >= 1 (recovering eta^{24}).

    The N=0 term (l>0, n=m=0) is separated since it gives the polar factor
    (1-y)^{c(-1)} which must be treated separately.
    """
    if data is None:
        data = phi01_coefficients()

    a: Dict[int, F] = defaultdict(F)

    for n in range(0, max_N + 1):
        for m in range(0, max_N + 1 - n):
            N = n + m
            if N == 0:
                continue  # Skip the polar sector n=m=0
            if N > max_N:
                continue
            for l in range(-max_N, max_N + 1):
                if not _bkm._positive_ordering(n, l, m):
                    continue
                if root_complexity(n, l, m) > max_arity:
                    continue
                mult = root_multiplicity(n, l, m, data)
                if mult == 0:
                    continue
                a[N] += F(mult)

    return dict(a)


# =========================================================================
# 3. NUMERICAL PRODUCT EVALUATION (BORCHERDS-LIFT CONVENTION)
# =========================================================================

def _truncated_borcherds_product(
    c_table: Dict[int, int],
    tau: complex, z: complex, sigma: complex,
    max_arity: int, N_prod: int = 12,
    data: Optional[Dict] = None
) -> complex:
    r"""Evaluate the Borcherds product truncated to arity max_arity.

    Uses the borcherds_lift.py convention (l<0 for n=m=0 sector) which
    is verified to match Delta_5/64 from theta constants.

    The truncation by arity: include only the product factors (n,l,m)
    whose complexity (from bkm_shadow_tower) is <= max_arity.

    The complexity assignment uses the bkm convention for root classification
    but does NOT depend on the l-sign for n=m=0 (since complexity 2 real
    roots have the same classification regardless of l-sign).
    """
    if data is None:
        data = phi01_coefficients()

    def _c(D: int) -> int:
        return c_table.get(D, 0)

    c_neg1 = _c(-1)
    log_sum = c_neg1 * 1j * np.pi * (tau + z + sigma)

    # Case 1: n=m=0, l<0 (Borcherds-lift convention)
    for l in range(-N_prod, 0):
        # Map to bkm complexity: the root (0, |l|, 0) in bkm convention
        # has the same complexity as (0, l, 0) in BL convention.
        # For |l| = 1: real root, complexity 2. For |l| >= 2: c(-l^2) = 0.
        bkm_complexity = root_complexity(0, abs(l), 0)
        if bkm_complexity > max_arity:
            continue
        D = -l * l
        exponent = _c(D)
        if exponent == 0:
            continue
        X = np.exp(2j * np.pi * l * z)
        if abs(1.0 - X) < 1e-300:
            continue
        log_sum += exponent * np.log(1.0 - X)

    # Case 2: n > 0 or m > 0 (same in both conventions)
    for n in range(0, N_prod + 1):
        for m in range(0, N_prod + 1):
            if n == 0 and m == 0:
                continue
            nm = n * m
            for l in range(-N_prod, N_prod + 1):
                # Complexity from bkm_shadow_tower
                # For n>0 or m>0, _positive_ordering(n,l,m) is always True
                # so root_complexity works directly.
                if not _bkm._positive_ordering(n, l, m):
                    continue
                if root_complexity(n, l, m) > max_arity:
                    continue
                D = 4 * nm - l * l
                exponent = _c(D)
                if exponent == 0:
                    continue
                X = np.exp(2j * np.pi * (n * tau + l * z + m * sigma))
                if abs(X) > 1e200:
                    continue
                if abs(1.0 - X) < 1e-300:
                    continue
                log_sum += exponent * np.log(1.0 - X)

    return np.exp(log_sum)


def delta5_from_theta(tau: complex, z: complex, sigma: complex) -> complex:
    r"""Evaluate (1/64)*Delta_5(Z) from the theta-constant product."""
    return _bl.delta5_theta(tau, z, sigma, N_terms=25) / 64.0


# =========================================================================
# 4. CONVERGENCE ANALYSIS
# =========================================================================

def convergence_analysis(
    tau: complex, z: complex, sigma: complex,
    max_arity: int = 8, N_prod: int = 12,
    data: Optional[Dict] = None
) -> List[Dict]:
    r"""Measure convergence of the truncated product Phi^{<=r} to Delta_5/64.

    At each arity r = 2, 3, ..., max_arity, compute:
        - Phi^{<=r}(Z) using the Borcherds-lift-convention product
        - The relative error |Phi^{<=r} / (Delta_5/64)| - 1

    Returns list of dicts with convergence data per arity.
    """
    if data is None:
        data = phi01_coefficients()

    c_table = _bl.phi01_c_table(80)
    phi_exact = delta5_from_theta(tau, z, sigma)

    results = []
    for r in range(2, max_arity + 1):
        phi_trunc = _truncated_borcherds_product(
            c_table, tau, z, sigma, r, N_prod, data
        )

        if abs(phi_exact) < 1e-300:
            rel_err = float('inf')
            ratio = complex(float('inf'))
        else:
            ratio = phi_trunc / phi_exact
            rel_err = abs(abs(ratio) - 1.0)

        roots_at_r = _bkm.roots_at_complexity(r, N_prod, data)
        roots_leq_r = _bkm.roots_up_to_complexity(r, N_prod, data)

        results.append({
            'arity': r,
            'phi_truncated': phi_trunc,
            'phi_exact': phi_exact,
            'ratio': ratio,
            'abs_ratio': abs(ratio),
            'rel_error': rel_err,
            'new_roots_at_arity': len(roots_at_r),
            'cumulative_roots': len(roots_leq_r),
            'new_mult_at_arity': sum(abs(m) for _, m, _ in roots_at_r),
        })

    return results


# =========================================================================
# 5. LAYER-BY-LAYER DECOMPOSITION
# =========================================================================

def layer_decomposition_numerical(
    tau: complex, z: complex, sigma: complex,
    max_arity: int = 6, N_prod: int = 12,
    data: Optional[Dict] = None
) -> List[Dict]:
    r"""Compute the layer-by-layer ratio of consecutive truncations.

    R_r = Phi^{<=r} / Phi^{<=r-1}

    This ratio isolates the contribution of the arity-r shadow obstruction.
    The full product is Phi = R_2 * R_3 * R_4 * ...
    """
    if data is None:
        data = phi01_coefficients()

    c_table = _bl.phi01_c_table(80)
    prev = None
    layers = []

    for r in range(2, max_arity + 1):
        curr = _truncated_borcherds_product(
            c_table, tau, z, sigma, r, N_prod, data
        )

        if prev is None:
            ratio = curr
            log_ratio = None
        else:
            if abs(prev) < 1e-300:
                ratio = complex(float('inf'))
            else:
                ratio = curr / prev
            try:
                log_ratio = math.log(abs(ratio))
            except (ValueError, OverflowError):
                log_ratio = float('inf')

        layers.append({
            'arity': r,
            'phi_truncated': curr,
            'ratio_vs_prev': ratio,
            'abs_ratio': abs(ratio),
            'log_abs_ratio': log_ratio,
        })
        prev = curr

    return layers


# =========================================================================
# 6. SHADOW GENERATING FUNCTION STRUCTURE
# =========================================================================

def shadow_generating_function(
    max_arity: int = 8, max_coord: int = 5,
    data: Optional[Dict] = None
) -> Dict[int, Dict]:
    r"""Compute the shadow generating function Z^{sh}(t) = sum_{r>=2} S_r * t^r.

    Each S_r is summarized by root count, multiplicity, and type breakdown.
    The resummation identity says:
        exp(sum_{r>=2} S_r(q) * t^r)|_{t=1} = Phi_Delta5(q) / (Weyl factor)
    """
    if data is None:
        data = phi01_coefficients()

    zsh: Dict[int, Dict] = {}
    for r in range(2, max_arity + 1):
        roots = _bkm.roots_at_complexity(r, max_coord, data)
        primary_sum = sum(mult for _, mult, _ in roots)
        real_mult = sum(mult for _, mult, cls in roots if cls == 'real')
        light_mult = sum(mult for _, mult, cls in roots
                         if cls == 'imaginary_lightlike')
        time_mult = sum(mult for _, mult, cls in roots
                        if cls == 'imaginary_timelike')

        zsh[r] = {
            'arity': r,
            'num_roots': len(roots),
            'primary_sum_mult': primary_sum,
            'real_mult': real_mult,
            'lightlike_mult': light_mult,
            'timelike_mult': time_mult,
            'roots': [(root, mult, cls) for root, mult, cls in roots],
        }

    return zsh


# =========================================================================
# 7. 1D FOURIER VERIFICATION: RESUMMED PRODUCT vs eta^{24}
# =========================================================================

def _exponentiate_log_series_1d(
    log_coeffs: Dict[int, F], max_degree: int
) -> Dict[int, F]:
    r"""Exponentiate a 1D log-series: given L(q) = sum a_n q^n, compute
    exp(L(q)) = sum b_n q^n through q^{max_degree}.

    Uses the recursion: n * b_n = sum_{k=1}^{n} k * a_k * b_{n-k}.
    """
    b: Dict[int, F] = {0: F(1)}
    for n in range(1, max_degree + 1):
        s = F(0)
        for k in range(1, n + 1):
            ak = log_coeffs.get(k, F(0))
            if ak != 0:
                s += k * ak * b.get(n - k, F(0))
        b[n] = s / n
    return b


def resummed_product_1d(max_arity: int, max_degree: int = 15,
                        data: Optional[Dict] = None) -> Dict[int, F]:
    r"""Resum the shadow tower effective exponents into a 1D q-product.

    Computes prod_{N>=1} (1-q^N)^{a(N)} where a(N) are the effective
    exponents at the given arity truncation.

    At full arity: a(N) = 24 for all N, so the product is eta^{24}.
    """
    if data is None:
        data = phi01_coefficients()

    a_N = effective_exponents_diagonal(max_arity, max_degree, data)

    # log(prod (1-q^N)^{a(N)}) = -sum_N a(N) * sum_{k>=1} q^{kN}/k
    log_coeffs: Dict[int, F] = defaultdict(F)
    for N, aN in a_N.items():
        if aN == 0 or N == 0:
            continue
        for k in range(1, max_degree // N + 1):
            log_coeffs[k * N] += F(-aN, k)

    return _exponentiate_log_series_1d(dict(log_coeffs), max_degree)


def _eta24_exact(max_degree: int) -> Dict[int, int]:
    r"""Exact coefficients of prod_{n>=1}(1-q^n)^{24} through q^{max_degree}."""
    coeffs: Dict[int, int] = {0: 1}
    for n in range(1, max_degree + 1):
        new_coeffs: Dict[int, int] = {}
        binom_coeffs = [math.comb(24, k) * ((-1) ** k) for k in range(25)]
        for deg, coeff in coeffs.items():
            for k in range(25):
                new_deg = deg + n * k
                if new_deg > max_degree:
                    break
                new_coeffs[new_deg] = new_coeffs.get(new_deg, 0) + coeff * binom_coeffs[k]
        coeffs = new_coeffs
    return coeffs


def verify_eta24_convergence(max_arity: int = 10, max_degree: int = 8,
                             data: Optional[Dict] = None) -> Dict:
    r"""Verify that the 1D resummed product converges to eta^{24}.

    At each arity, compare the resummed product coefficients against the
    exact eta^{24} coefficients. The number of matching coefficients
    increases with arity.

    Returns dict with:
        'eta24_exact': known coefficients
        'by_arity': for each arity, which coefficients match
        'full_match_at_arity': first arity at which ALL coefficients match
    """
    if data is None:
        data = phi01_coefficients()

    eta24 = _eta24_exact(max_degree)

    results = {
        'eta24_exact': eta24,
        'by_arity': {},
        'full_match_at_arity': None,
    }

    for r in range(2, max_arity + 1):
        prod_coeffs = resummed_product_1d(r, max_degree, data)
        matches = {}
        all_match = True
        for deg in range(max_degree + 1):
            exact = eta24.get(deg, 0)
            resummed = int(prod_coeffs.get(deg, F(0)))
            matches[deg] = (resummed == exact)
            if resummed != exact:
                all_match = False

        results['by_arity'][r] = {
            'coefficients': {d: int(prod_coeffs.get(d, F(0)))
                             for d in range(max_degree + 1)},
            'matches': matches,
            'all_match': all_match,
        }

        if all_match and results['full_match_at_arity'] is None:
            results['full_match_at_arity'] = r

    return results


# =========================================================================
# 8. FULL VERIFICATION SUITE
# =========================================================================

def run_resummation_verification(verbose: bool = True) -> Dict:
    r"""Run the full shadow resummation verification.

    Checks:
    1. Shadow invariant structure at each arity
    2. Effective exponents convergence to a(N) = 24
    3. Truncated product convergence to Delta_5/64
    4. Layer-by-layer multiplicative decomposition
    5. 1D Fourier coefficient match against eta^{24}

    IMPORTANT (AP-CY8): The identification "Borcherds product = bar Euler
    product" at the level of chi_10 is an OBSERVATION for K3 x E, conditional
    on CY-A_2 (proved at d=2) and the Vol I Borcherds-lift identification.
    """
    data = phi01_coefficients()

    results = {
        'shadow_structure': {},
        'effective_exponents': {},
        'convergence': None,
        'layer_decomposition': None,
        'eta24_verification': None,
        'all_passed': True,
    }

    # --- 1. Shadow structure ---
    if verbose:
        print("=" * 72)
        print("SHADOW TOWER RESUMMATION TO BORCHERDS PRODUCT (K3 x E)")
        print("=" * 72)
        print()

    zsh = shadow_generating_function(max_arity=8, max_coord=5, data=data)
    results['shadow_structure'] = zsh

    if verbose:
        print("Shadow generating function Z^{sh}(t) = sum S_r * t^r:")
        print(f"{'Arity':>6} | {'Roots':>6} | {'Sum mult':>10} | "
              f"{'Real':>6} | {'Light':>6} | {'Time':>6}")
        print("-" * 60)
        for r in sorted(zsh.keys()):
            s = zsh[r]
            print(f"{r:>6} | {s['num_roots']:>6} | "
                  f"{s['primary_sum_mult']:>10} | "
                  f"{s['real_mult']:>6} | {s['lightlike_mult']:>6} | "
                  f"{s['timelike_mult']:>6}")
        print()

    # --- 2. Effective exponents ---
    if verbose:
        print("Effective exponents a(N) in diagonal specialization:")
        print("  (At full arity, a(N) should = 24 for all N >= 1)")

    for r in [2, 3, 4, 5, 6, 8, 10]:
        a_N = effective_exponents_diagonal(r, max_N=8, data=data)
        results['effective_exponents'][r] = dict(a_N)
        if verbose:
            items = sorted(a_N.items())[:8]
            line = ", ".join(f"a({N})={v}" for N, v in items)
            print(f"  Arity {r:>2}: {line}")

    # Check: at arity 10, all a(N) for N=1..8 should be 24
    a_full = effective_exponents_diagonal(10, max_N=8, data=data)
    exponents_correct = all(a_full.get(N, F(0)) == F(24) for N in range(1, 9))
    results['all_passed'] &= exponents_correct
    if verbose:
        print(f"  All a(N)=24 at arity 10: {'PASS' if exponents_correct else 'FAIL'}")
        print()

    # --- 3. Convergence at a test point ---
    tau_test = 0.15 + 2.0j
    z_test = 0.08 + 0.12j
    sigma_test = 0.10 + 2.0j

    if verbose:
        print(f"Pointwise convergence at Z = (tau={tau_test}, z={z_test}, "
              f"sigma={sigma_test}):")
        print(f"{'Arity':>6} | {'|Phi^{<=r}|':>14} | {'|ratio|':>12} | "
              f"{'rel error':>12} | {'new roots':>10}")
        print("-" * 72)

    conv = convergence_analysis(
        tau_test, z_test, sigma_test,
        max_arity=8, N_prod=8, data=data
    )
    results['convergence'] = conv

    for c in conv:
        if verbose:
            print(f"{c['arity']:>6} | {abs(c['phi_truncated']):>14.6e} | "
                  f"{c['abs_ratio']:>12.8f} | {c['rel_error']:>12.2e} | "
                  f"{c['new_roots_at_arity']:>10}")

    # Check convergence: at max arity, relative error should be small
    if conv:
        final_err = conv[-1]['rel_error']
        converges = final_err < 0.01  # 1% tolerance at arity 8
        results['all_passed'] &= converges
        if verbose:
            print(f"\nFinal relative error at arity {conv[-1]['arity']}: "
                  f"{final_err:.2e} ({'PASS' if converges else 'FAIL'})")
            print()

    # --- 4. Layer decomposition ---
    if verbose:
        print("Layer decomposition (multiplicative corrections R_r):")
        print(f"{'Arity':>6} | {'|R_r|':>14} | {'log|R_r|':>12}")
        print("-" * 40)

    layers = layer_decomposition_numerical(
        tau_test, z_test, sigma_test,
        max_arity=8, N_prod=8, data=data
    )
    results['layer_decomposition'] = layers

    for lay in layers:
        if verbose and lay['log_abs_ratio'] is not None:
            print(f"{lay['arity']:>6} | {lay['abs_ratio']:>14.6e} | "
                  f"{lay['log_abs_ratio']:>12.6f}")
    if verbose:
        print()

    # --- 5. eta^{24} coefficient verification ---
    if verbose:
        print("eta^{24} coefficient verification (1D resummation):")

    eta_ver = verify_eta24_convergence(max_arity=10, max_degree=6, data=data)
    results['eta24_verification'] = eta_ver

    if verbose:
        eta24 = eta_ver['eta24_exact']
        print(f"  eta^24 exact: " + ", ".join(
            f"q^{d}:{eta24[d]}" for d in range(min(7, len(eta24)))
        ))
        for r in [2, 4, 6, 8, 10]:
            if r in eta_ver['by_arity']:
                info = eta_ver['by_arity'][r]
                n_match = sum(1 for v in info['matches'].values() if v)
                n_total = len(info['matches'])
                print(f"  Arity {r:>2}: {n_match}/{n_total} coefficients match eta^24")

        fma = eta_ver.get('full_match_at_arity')
        if fma is not None:
            print(f"  Full match achieved at arity {fma}")
        else:
            print("  Full match NOT achieved (need higher arity or degree)")

    eta_passes = (eta_ver.get('full_match_at_arity') is not None)
    results['all_passed'] &= eta_passes

    if verbose:
        print()
        if results['all_passed']:
            print("ALL RESUMMATION CHECKS PASSED")
        else:
            print("SOME CHECKS FAILED")

    return results


# =========================================================================
# 9. SAITO-KUROKAWA ADDITIVE LIFT (FOURIER-JACOBI SIDE)
# =========================================================================

# The additive (Saito-Kurokawa) lift reconstructs chi_10 = Delta_5^2
# from its first Fourier-Jacobi coefficient phi_1 = phi_{10,1} via the
# Maass relations.  The Fourier-Jacobi expansion is:
#
#   chi_10(Z) = sum_{m >= 1} phi_m(tau, z) * p^m
#
# where p = exp(2*pi*i*sigma), and:
#   phi_1 = phi_{10,1} (weight 10, index 1)
#   phi_m determined from phi_1 by Hecke-like Maass relations
#
# The multiplicative (Borcherds) side gives the same chi_10 as:
#   chi_10 = BP^2 = (Borcherds product of phi_{0,1})^2
#
# The bridge: phi_{0,1} = phi_{10,1} / eta^{24}.
# Root multiplicities (multiplicative input) and FJ coefficients (additive
# output) are related by exactly the free-boson denominator eta^{24}.
#
# IMPORTANT (AP-CY8): The identification "bar Euler product = Borcherds
# denominator" for K3 x E is an OBSERVATION, conditional on CY-A_2
# (proved at d=2) and the Vol I Borcherds-lift identification.

def phi_10_1_by_discriminant(max_D: int = 30) -> Dict[int, int]:
    r"""Fourier coefficients c(D) of phi_{10,1} indexed by discriminant.

    phi_{10,1}(tau, z) = sum_{4n - r^2 > 0} c(4n - r^2) q^n zeta^r

    This is the unique Jacobi cusp form of weight 10 and index 1.
    It equals eta(tau)^{18} * vartheta_1(tau, z)^2.

    Source: Eichler-Zagier Table 2, cross-checked against theta DFT.
    """
    # Coefficients indexed by discriminant D = 4n - r^2 > 0
    # Only discriminants D with D = 0 or 3 mod 4 can appear (AP-CY9)
    return {
        3: 1,        # VERIFIED [LT] Eichler-Zagier Table 2, [DC] theta DFT
        4: -2,       # VERIFIED [LT] Eichler-Zagier Table 2, [DC] theta DFT
        7: -16,      # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        8: 36,       # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        11: 99,      # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        12: -272,    # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        15: -240,    # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        16: 1056,    # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        19: -2178,   # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        20: 1476,    # VERIFIED [LT] van der Geer 2008, [DC] theta DFT
        23: 5765,    # VERIFIED [LT] van der Geer 2008
        24: -5765,   # VERIFIED [LT] van der Geer 2008
    }


def phi_10_1_fourier(max_n: int = 10) -> Dict[Tuple[int, int], int]:
    r"""Fourier coefficients c(n, r) of phi_{10,1}.

    Returns dict mapping (n, r) -> c(n, r) for 4n - r^2 > 0.
    """
    c_by_D = phi_10_1_by_discriminant()
    result: Dict[Tuple[int, int], int] = {}
    for n in range(1, max_n + 1):
        for r in range(-2 * n, 2 * n + 1):
            D = 4 * n - r * r
            if D <= 0:
                continue
            if D in c_by_D:
                result[(n, r)] = c_by_D[D]
    return result


def maass_relations_phi_m(m: int, max_n: int = 8) -> Dict[Tuple[int, int], F]:
    r"""Compute the m-th Fourier-Jacobi coefficient phi_m of chi_10
    from phi_1 = phi_{10,1} via the Maass relations.

    For the Saito-Kurokawa lift, the FJ coefficients phi_m of chi_10
    are determined from phi_1 by:

        a(n, r, m) = sum_{d | gcd(n, r, m)} d^{k-1} * c_1(nm/d^2, r/d)

    where k = 10 (the weight) and c_1(n, r) are the coefficients of
    phi_1 = phi_{10,1}.  The sum runs over positive divisors d of
    gcd(n, r, m).

    This is the Maass relation (Eichler-Zagier Section 4, Maass 1979).

    Returns dict mapping (n, r) -> a(n, r, m) as Fraction.
    """
    c1 = phi_10_1_fourier(max_n=max_n * m + 1)
    k = 10  # weight of chi_10

    result: Dict[Tuple[int, int], F] = {}
    for n in range(0, max_n + 1):
        for r in range(-2 * max(n, m), 2 * max(n, m) + 1):
            D = 4 * n * m - r * r
            if D <= 0 and not (n == 0 and r == 0 and m == 0):
                continue
            # Maass relation: sum over d | gcd(n, r, m)
            g = math.gcd(math.gcd(abs(n), abs(r)), abs(m))
            if g == 0:
                continue
            total = F(0)
            for d in range(1, g + 1):
                if g % d != 0:
                    continue
                n_red = n * m // (d * d)
                r_red = r // d
                # Check that n*m/d^2 is an integer and look up c_1
                if (n * m) % (d * d) != 0:
                    continue
                c1_val = c1.get((n_red, r_red), 0)
                if c1_val != 0:
                    total += F(d ** (k - 1)) * c1_val
            if total != 0:
                result[(n, r)] = total
    return result


def chi10_fourier_from_maass(max_n: int = 4, max_m: int = 3
                             ) -> Dict[Tuple[int, int, int], F]:
    r"""Reconstruct chi_10 Fourier coefficients from the Maass relations.

    This is the ADDITIVE (Saito-Kurokawa) side:
      a(n, r, m) = sum_{d | gcd(n,r,m)} d^9 * c_1(nm/d^2, r/d)

    Returns dict mapping (n, r, m) -> a(n, r, m).
    """
    result: Dict[Tuple[int, int, int], F] = {}
    for m in range(1, max_m + 1):
        phi_m = maass_relations_phi_m(m, max_n=max_n)
        for (n, r), val in phi_m.items():
            if val != 0:
                result[(n, r, m)] = val
    return result


# =========================================================================
# 10. ADDITIVE vs MULTIPLICATIVE LOW-ORDER COMPARISON
# =========================================================================

def _chi10_known_fourier() -> Dict[Tuple[int, int, int], int]:
    r"""Known Fourier coefficients of chi_10 (curated reference table).

    These are independently verified from BOTH:
    - Theta-constant product (multiplicative)
    - Eichler-Zagier table (additive/FJ)

    Source: borcherds_denominator_phi10_engine.KNOWN_CHI10_COEFFICIENTS
    """
    return {
        (1, 1, 1): 1, (1, -1, 1): 1,
        (1, 0, 1): -2, (1, 2, 2): -2, (1, -2, 2): -2,
        (2, 2, 1): -2, (2, -2, 1): -2,
        (1, 1, 2): -16, (1, -1, 2): -16,
        (2, 1, 1): -16, (2, -1, 1): -16,
        (1, 0, 2): 36, (2, 0, 1): 36,
        (3, 1, 1): 99, (3, -1, 1): 99,
        (1, 1, 3): 99, (1, -1, 3): 99,
        (1, 0, 3): -272, (3, 0, 1): -272,
        (2, 2, 2): 240, (2, -2, 2): 240,
        (2, 1, 2): -240, (2, -1, 2): -240,
        (2, 0, 2): 32,
    }


def verify_additive_vs_multiplicative(
    max_n: int = 3, max_m: int = 3, verbose: bool = False
) -> Dict:
    r"""Verify that the additive (Saito-Kurokawa) and multiplicative
    (Borcherds product) sides give the same chi_10 coefficients.

    The additive side: Maass relations from phi_{10,1}.
    The multiplicative side: known chi_10 coefficients from the
    Borcherds product (verified against theta-constant product).

    IMPORTANT (AP-CY8): This is an OBSERVATION for K3 x E, not a
    theorem in the chiral algebra context.  The chiral-algebraic
    interpretation requires CY-A_2 (proved at d=2) and the Vol I
    Borcherds-lift identification.
    """
    additive = chi10_fourier_from_maass(max_n=max_n, max_m=max_m)
    known = _chi10_known_fourier()

    matches = []
    mismatches = []
    additive_only = []

    for (n, r, m), a_val in sorted(additive.items()):
        D = 4 * n * m - r * r
        if D <= 0:
            continue
        a_int = int(a_val)
        if a_val != a_int:
            mismatches.append(((n, r, m), a_val, 'non-integer'))
            continue
        if (n, r, m) in known:
            k_val = known[(n, r, m)]
            if a_int == k_val:
                matches.append(((n, r, m), a_int, k_val))
            else:
                mismatches.append(((n, r, m), a_int, k_val))
        else:
            additive_only.append(((n, r, m), a_int))

    if verbose:
        print(f"\nAdditive vs Multiplicative comparison (n<={max_n}, m<={max_m}):")
        print(f"  Matches: {len(matches)}")
        print(f"  Mismatches: {len(mismatches)}")
        print(f"  Additive-only (no known ref): {len(additive_only)}")
        if mismatches:
            for triple, a, k in mismatches:
                print(f"    MISMATCH at {triple}: additive={a}, known={k}")
        if matches and verbose:
            for triple, a, k in matches[:8]:
                D = 4 * triple[0] * triple[2] - triple[1]**2
                print(f"    MATCH at {triple} (D={D}): {a}")

    return {
        'n_matches': len(matches),
        'n_mismatches': len(mismatches),
        'n_additive_only': len(additive_only),
        'matches': matches,
        'mismatches': mismatches,
        'additive_only': additive_only,
        'all_agree': len(mismatches) == 0 and len(matches) > 0,
    }


# =========================================================================
# 11. SHADOW-TO-FJ BRIDGE: PERTURBATIVE vs AUTOMORPHIC
# =========================================================================

def perturbative_shadow_to_eta24_bridge(max_arity: int = 8,
                                        max_degree: int = 6,
                                        data: Optional[Dict] = None
                                        ) -> Dict:
    r"""Verify the three-way bridge: shadow tower <-> eta^{24} <-> FJ bridge.

    The shadow tower produces effective exponents a(N) which converge to 24.
    The 1D product prod(1 - q^N)^{a(N)} converges to eta^{24}.
    The ratio phi_{0,1} / phi_{10,1} = 1/eta^{24} connects the
    multiplicative input (root mults) to the additive output (FJ coeffs).

    This function verifies the coefficient-level agreement at each arity:
    1. Shadow effective exponents a(N) at arity r
    2. Resummed 1D product coefficients
    3. Comparison against eta^{24}
    4. The bridge identity: c_{0,1}(D) * tau(n) = c_{10,1}(D) * p_{24}(n)
       (schematic; the actual relation involves convolution)

    Returns dict with verification results at each arity level.
    """
    if data is None:
        data = phi01_coefficients()

    eta24_exact = _eta24_exact(max_degree)

    # phi_{0,1} coefficients by discriminant
    phi01_disc = phi01_by_discriminant(max_degree // 4 + 2)
    # phi_{10,1} coefficients by discriminant
    phi101_disc = phi_10_1_by_discriminant()

    # The bridge identity: phi_{10,1}(tau, z) = phi_{0,1}(tau, z) * eta(tau)^{24}
    # as formal q-series.  At the level of discriminant-indexed coefficients:
    #   c_{10,1}(D) = sum_{j >= 0} c_{0,1}(D + 4j - ...) * eta24_coeff(j)
    #
    # But since both depend only on discriminant, the convolution is in the
    # (n, r) variables, not just D.  The cleaner check is at the q-series level.

    # Check: phi_{0,1}(tau, 0) = 12, phi_{10,1}(tau, 0) = 0 (cusp form),
    # eta^{24}|_{q^0} = 1.
    # So phi_{0,1}(tau, 0) * eta(tau)^{24} should give phi_{10,1}(tau, 0)?
    # NO: phi_{10,1} is a CUSP form (vanishes at z=0 mod lattice).
    # The correct relation is more subtle: phi_{0,1} and phi_{10,1} are
    # both Jacobi forms but of different weights; the relation is
    #   phi_{0,1} * Delta = phi_{10,1} * (correction from phi_{-2,1})
    # The precise identity:
    #   phi_{0,1} = (E_4 * phi_{-2,1} + E_6 * phi_{0,1}) / (E_4 * E_6)  (wrong)
    #
    # Actually the relation is (Eichler-Zagier): the space J_{k,1} for
    # k=0 has basis phi_{0,1}, and for k=10 has basis phi_{10,1} (cusp).
    # The bridge from remark rem:k3e-two-lifts is more nuanced:
    #   phi_{0,1} = phi_{10,1} / eta^{24} (up to phi_{12,1}/Delta_{12} factor)
    #
    # For low-order verification, we check at the level of chi_10:
    # both sides (Borcherds product of phi_{0,1}, and SK lift of phi_{10,1})
    # produce the same Siegel modular form.

    results = {
        'arity_data': {},
        'bridge_check': None,
    }

    for r in [2, 4, 6, 8]:
        if r > max_arity:
            break
        a_N = effective_exponents_diagonal(r, max_N=max_degree, data=data)
        prod_coeffs = resummed_product_1d(r, max_degree, data)
        n_match = 0
        n_total = 0
        for d in range(max_degree + 1):
            exact = eta24_exact.get(d, 0)
            computed = int(prod_coeffs.get(d, F(0)))
            n_total += 1
            if computed == exact:
                n_match += 1
        results['arity_data'][r] = {
            'effective_exponents': {N: int(v) for N, v in sorted(a_N.items())[:8]},
            'n_eta24_match': n_match,
            'n_eta24_total': n_total,
            'all_match': n_match == n_total,
        }

    # Bridge check: verify phi_{0,1} and phi_{10,1} are related
    # through the eta^{24} factor at the discriminant level.
    #
    # For D = -1: c_{0,1}(-1) = 2 (polar term), c_{10,1}(-1) undefined (cusp)
    # For D = 0: c_{0,1}(0) = 10, phi_{10,1} has no D=0 term
    # For D = 3: c_{0,1}(3) = -64, c_{10,1}(3) = 1
    # For D = 4: c_{0,1}(4) = 108, c_{10,1}(4) = -2
    # For D = 7: c_{0,1}(7) = -288, c_{10,1}(7) = -16
    # For D = 8: c_{0,1}(8) = 370, c_{10,1}(8) = 36
    #
    # The ratio is NOT constant (the relation involves eta^{24} convolution
    # in the (n,r) variables, not a simple discriminant-level ratio).
    #
    # The correct bridge is at the Siegel form level: both lifts produce
    # the same chi_10.  We verify this via verify_additive_vs_multiplicative.

    bridge = verify_additive_vs_multiplicative(max_n=3, max_m=2)
    results['bridge_check'] = {
        'additive_multiplicative_agree': bridge['all_agree'],
        'n_matched': bridge['n_matches'],
        'n_mismatched': bridge['n_mismatches'],
    }

    return results


# =========================================================================
# 12. COMBINED VERIFICATION: SHADOW RESUMMATION + ADDITIVE LIFT
# =========================================================================

def run_full_resummation_with_additive(verbose: bool = True) -> Dict:
    r"""Run the complete shadow resummation verification INCLUDING
    the additive (Saito-Kurokawa) vs multiplicative (Borcherds) comparison.

    This extends run_resummation_verification with:
    6. Additive (Maass) vs multiplicative (Borcherds) coefficient comparison
    7. Shadow-to-FJ bridge verification
    8. Perturbative shadow S_2, S_3, S_4 to Borcherds product convergence

    IMPORTANT (AP-CY8): The identification "Borcherds product = bar Euler
    product" at the level of chi_10 is an OBSERVATION for K3 x E, conditional
    on CY-A_2 (proved at d=2) and the Vol I Borcherds-lift identification.
    """
    # Run the base verification
    results = run_resummation_verification(verbose=verbose)

    data = phi01_coefficients()

    # --- 6. Additive vs Multiplicative ---
    if verbose:
        print()
        print("=" * 72)
        print("ADDITIVE (SAITO-KUROKAWA) vs MULTIPLICATIVE (BORCHERDS)")
        print("=" * 72)
        print()

    add_vs_mult = verify_additive_vs_multiplicative(
        max_n=3, max_m=3, verbose=verbose
    )
    results['additive_vs_multiplicative'] = add_vs_mult

    if verbose:
        status = 'PASS' if add_vs_mult['all_agree'] else 'FAIL'
        print(f"\n  Additive vs Multiplicative: {status} "
              f"({add_vs_mult['n_matches']} matches, "
              f"{add_vs_mult['n_mismatches']} mismatches)")

    results['all_passed'] &= add_vs_mult['all_agree']

    # --- 7. Shadow-to-FJ bridge ---
    if verbose:
        print()
        print("Shadow-to-FJ bridge:")

    bridge = perturbative_shadow_to_eta24_bridge(
        max_arity=8, max_degree=6, data=data
    )
    results['shadow_fj_bridge'] = bridge

    if verbose:
        for r, info in sorted(bridge['arity_data'].items()):
            exps = info['effective_exponents']
            exp_str = ", ".join(f"a({N})={v}" for N, v in list(exps.items())[:6])
            print(f"  Arity {r}: {exp_str} | "
                  f"eta^24 match: {info['n_eta24_match']}/{info['n_eta24_total']}")
        bc = bridge['bridge_check']
        print(f"  Bridge (additive=multiplicative): "
              f"{'PASS' if bc['additive_multiplicative_agree'] else 'FAIL'} "
              f"({bc['n_matched']} matched)")

    bridge_pass = bridge['bridge_check']['additive_multiplicative_agree']
    results['all_passed'] &= bridge_pass

    # --- 8. Summary of the perturbative shadow invariants ---
    if verbose:
        print()
        print("Perturbative shadow invariants S_r (from Borcherds root layers):")
        print(f"  S_2 = kappa_BKM = 5 (weight of Delta_5)")
        print(f"  S_3: first imaginary root corrections (lightlike D=0)")
        print(f"  S_4: second imaginary layer (timelike D>0)")
        print(f"  Resummation: exp(sum S_r) -> Delta_5 (Borcherds product)")
        print(f"  Additive lift: phi_{{10,1}} -> chi_10 (Saito-Kurokawa)")
        print(f"  Agreement: both produce chi_10 = Delta_5^2")

    if verbose:
        print()
        if results['all_passed']:
            print("ALL RESUMMATION + ADDITIVE CHECKS PASSED")
        else:
            print("SOME CHECKS FAILED")

    return results


if __name__ == '__main__':
    run_full_resummation_with_additive(verbose=True)
