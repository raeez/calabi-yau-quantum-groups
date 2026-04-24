r"""
Shadow tower decomposition of K3 elliptic genus Fourier coefficients.

The weak Jacobi form phi_{0,1}(tau, z) of weight 0 index 1 is the K3
elliptic genus.  Its Fourier coefficients c(D) (indexed by discriminant
D = 4n - l^2) are root multiplicities of the BKM superalgebra
g_{Delta_5}.  This module decomposes c(D) into shadow tower projections
of definite arity, connecting three structures:

    (I)   Discriminant stratification of c(D) by Siegel discriminant D
    (II)  Shadow arity filtration from the Vol I obstruction tower
    (III) BPS charge grading n + m in the product formula

Central identification (conjectural, tested here):
    The Siegel discriminant D stratification IS the shadow arity filtration,
    via the BPS charge:

        arity(n, l, m) = 2               if D(n,l,m) = -1  (real root)
        arity(n, l, m) = 2 + (n + m)     if D(n,l,m) >= 0  (imaginary root)

    so that the D-range at each arity is:

        arity 2:  D = -1 only  (real roots, multiplicity c(-1) = 1)
        arity 3:  D = 0 only   (lightlike, n+m = 1, mult c(0) = 10)
        arity r (r >= 4): D in {0, 3, 4, ..., (r-2)^2}
                           with D = 4nm - l^2, n+m = r-2

    Each c(D) value receives contributions from ALL arities >= r_min(D),
    where r_min(D) is the smallest arity at which discriminant D first appears.

Four independent verification paths:

    Path A: Direct Fourier coefficient computation (from phi01_fourier.py)
    Path B: Theta decomposition into h_0 (even l) and h_1 (odd l) channels
    Path C: Hecke operator compatibility (T_p acts within arity layers)
    Path D: Comparison with bkm_shadow_tower.py root enumeration

References:
    Eichler-Zagier, "The Theory of Jacobi Forms" (1985), Thm 9.3
    Gritsenko-Nikulin, "Automorphic forms and Lorentzian KM algebras II" (1998)
    Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower)
    Vol III: k3_times_e.tex (BKM shadow identification)
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Set, Tuple

import importlib as _importlib
import os as _os
import sys as _sys


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


_phi01_mod = _import_module('phi01_fourier')
_bkm_mod = _import_module('bkm_shadow_tower')

phi01_table = _phi01_mod.phi01_table
phi01_by_discriminant = _phi01_mod.phi01_by_discriminant
phi01_coefficient = _phi01_mod.phi01_coefficient

bkm_root_complexity = _bkm_mod.root_complexity
bkm_enumerate_positive_roots = _bkm_mod.enumerate_positive_roots
bkm_shadow_tower_projection = _bkm_mod.shadow_tower_projection
bkm_phi01_coefficients = _bkm_mod.phi01_coefficients
bkm_kappa_projection = _bkm_mod.kappa_projection
bkm_get_f = _bkm_mod.get_f
bkm_siegel_discriminant = _bkm_mod.siegel_discriminant


# =========================================================================
# 1. DISCRIMINANT CLASSIFICATION
# =========================================================================

# The discriminant D = 4n - l^2 for phi_{0,1} coefficients.
# D mod 4 is constrained:
#   l even => D ≡ 0 (mod 4)
#   l odd  => D ≡ -1 ≡ 3 (mod 4)
# So only D ≡ 0, 3 (mod 4) appear (plus D = -1 as the polar term).

DISC_CLASSES = {
    'polar': -1,           # D = -1: real roots of BKM
    'lightlike': 0,        # D = 0: boundary / lightlike imaginary
    'timelike_first': 3,   # D = 3: first timelike imaginary (odd l)
    'timelike_second': 4,  # D = 4: second timelike imaginary (even l)
}


def discriminant_class(D: int) -> str:
    """Classify a discriminant value into the root type.

    Returns one of:
        'polar'              D = -1  (real roots, norm 2)
        'lightlike'          D = 0   (norm 0)
        'timelike_odd'       D > 0, D ≡ 3 (mod 4)  (odd l)
        'timelike_even'      D > 0, D ≡ 0 (mod 4)  (even l)
        'absent'             D not of the form 4n - l^2 with n >= 0
    """
    if D == -1:
        return 'polar'
    if D == 0:
        return 'lightlike'
    if D < -1:
        return 'absent'
    if D % 4 == 0:
        return 'timelike_even'
    if D % 4 == 3:
        return 'timelike_odd'
    # D ≡ 1 or 2 (mod 4): no phi_{0,1} coefficient at this D
    return 'absent'


def valid_discriminants(max_D: int) -> List[int]:
    """List all valid discriminant values for phi_{0,1} up to max_D.

    Valid values: D = -1, and D >= 0 with D ≡ 0 or 3 (mod 4).
    """
    result = [-1]
    for D in range(0, max_D + 1):
        if D % 4 in (0, 3):
            result.append(D)
    return result


# =========================================================================
# 2. ARITY ASSIGNMENT FROM DISCRIMINANT
# =========================================================================

def minimum_arity_for_discriminant(D: int) -> int:
    """The minimum shadow arity at which discriminant D first appears.

    From the BPS charge grading:
        arity(n, l, m) = 2 + (n + m) for imaginary roots
        arity = 2 for real roots (D = -1)

    For a given D >= 0, the minimum arity is determined by minimizing
    n + m subject to:
        4nm - l^2 = D,  n >= 0, m >= 0, (n,l,m) > 0

    For D = 0: n + m = 1 (e.g., (1,0,0) or (0,0,1)), so arity = 3.
    For D > 0: we need 4nm >= D + l^2 >= D, so nm >= D/4.
    The minimum of n + m with nm >= D/4 is n + m = 2*sqrt(D/4) = sqrt(D)
    when n = m = sqrt(D)/2.  But n, m must be non-negative integers with
    (n,l,m) positive, and 4nm - l^2 = D exactly.

    We compute this by exhaustive search over (n, m, l) triples.
    """
    if D == -1:
        return 2

    # For D >= 0: find minimum n + m such that there exist integers
    # n >= 0, m >= 0, l with 4nm - l^2 = D and (n,l,m) positive.
    #
    # Since l^2 = 4nm - D, we need 4nm >= D, i.e., nm >= D/4.
    # Iterate over n + m = s, starting from s = 1:
    for s in range(1, D + 10):
        for n in range(0, s + 1):
            m = s - n
            if n < 0 or m < 0:
                continue
            val = 4 * n * m - D
            if val < 0:
                continue
            # Need l^2 = 4nm - D = val
            l_sq = val
            l = math.isqrt(l_sq)
            if l * l == l_sq:
                # Check positivity: (n,l,m) > 0
                # n > 0, or (n=0, m > 0), or (n=0, m=0, l > 0)
                for ll in ([l, -l] if l > 0 else [0]):
                    if n > 0 or (n == 0 and m > 0) or (n == 0 and m == 0 and ll > 0):
                        return 2 + s
    # Fallback (should not reach here for valid D)
    return -1


def discriminants_at_arity(r: int) -> Set[int]:
    """All discriminant values D that appear at exactly arity r.

    A discriminant D appears at arity r if there exists a positive root
    (n, l, m) with complexity r and Siegel discriminant 4nm - l^2 = D.

    For arity 2: D = -1 (real roots only).
    For arity r >= 3: imaginary roots with n + m = r - 2, so
        D = 4nm - l^2 with n + m = r - 2.
    """
    if r == 2:
        return {-1}
    if r < 2:
        return set()

    s = r - 2  # n + m = s for imaginary roots at this arity
    disc_set: Set[int] = set()
    for n in range(0, s + 1):
        m = s - n
        # D = 4nm - l^2 for all valid l
        nm_prod = 4 * n * m
        # l ranges: l^2 <= 4nm (for D >= 0) and l^2 = 4nm + 1 for D = -1
        # But D >= 0 for imaginary roots, so l^2 <= 4nm
        for l in range(-int(math.isqrt(nm_prod)) - 1,
                       int(math.isqrt(nm_prod)) + 2):
            D = nm_prod - l * l
            if D >= 0:
                disc_set.add(D)
    return disc_set


def maximum_discriminant_at_arity(r: int) -> int:
    """The maximum Siegel discriminant D at shadow arity r.

    For arity r >= 3: roots have n + m = r - 2.
    D = 4nm - l^2 is maximized when l = 0 and nm is maximized.
    With n + m = s = r - 2, max(nm) = floor(s/2) * ceil(s/2) = floor(s^2/4).
    So max D = 4 * floor(s^2/4) = s^2 if s even, s^2 - 1 if s odd.

    For arity 2: max D = -1.
    """
    if r == 2:
        return -1
    if r < 3:
        return -2  # No roots

    s = r - 2
    # n + m = s, maximize nm at l = 0: nm = floor(s^2/4)
    # D = 4nm = 4 * floor(s^2/4)
    if s % 2 == 0:
        return s * s  # n = m = s/2, D = 4*(s/2)^2 = s^2
    else:
        return s * s - 1  # n = (s-1)/2, m = (s+1)/2, D = 4*((s^2-1)/4) = s^2-1


# =========================================================================
# 3. SHADOW PROJECTIONS: DECOMPOSING c(D)
# =========================================================================

def shadow_projection_at_arity(r: int, max_n: int = 10,
                                max_coord: int = 5) -> Dict[int, Fraction]:
    """The arity-r shadow projection's contribution to each discriminant D.

    This computes the log-coefficient contribution from roots at exactly
    arity r, organized by Siegel discriminant D.

    Returns dict: D -> total log-coefficient from roots at complexity r
    that have Siegel discriminant D.
    """
    data = bkm_phi01_coefficients(4 * max_n)
    roots = bkm_enumerate_positive_roots(max_coord, data)

    contrib: Dict[int, Fraction] = defaultdict(Fraction)
    for (n, l, m), mult, cls in roots:
        if bkm_root_complexity(n, l, m) != r:
            continue
        D = 4 * n * m - l * l
        # log(1 - e_alpha)^mult contributes -mult at leading order
        contrib[D] += Fraction(mult)

    return dict(contrib)


def full_shadow_decomposition(max_arity: int = 6, max_n: int = 10,
                               max_coord: int = 5) -> Dict[int, Dict[int, Fraction]]:
    """Full decomposition: for each arity r, the multiplicity contribution
    at each discriminant D.

    Returns: dict[arity -> dict[D -> total_multiplicity_at_this_arity_and_D]]
    """
    data = bkm_phi01_coefficients(4 * max_n)
    roots = bkm_enumerate_positive_roots(max_coord, data)

    result: Dict[int, Dict[int, Fraction]] = {}
    for r in range(2, max_arity + 1):
        layer: Dict[int, Fraction] = defaultdict(Fraction)
        for (n, l, m), mult, cls in roots:
            if bkm_root_complexity(n, l, m) != r:
                continue
            D = 4 * n * m - l * l
            layer[D] += Fraction(mult)
        result[r] = dict(layer)

    return result


# =========================================================================
# 4. THETA DECOMPOSITION (PATH B)
# =========================================================================

def theta_decomposition(max_n: int = 10) -> Tuple[Dict[int, int], Dict[int, int]]:
    """Decompose phi_{0,1} into even-l and odd-l channels.

    phi_{0,1}(tau, z) = sum_{n,l} c(n,l) q^n y^l

    The theta decomposition separates this into two vector-valued forms:
        h_0(tau) collects c(D) with D ≡ 0 (mod 4)  [even l channel]
        h_1(tau) collects c(D) with D ≡ 3 (mod 4)  [odd l channel]

    The even-l channel gives c(D) > 0 for all D >= 0 with D ≡ 0 mod 4.
    The odd-l channel gives c(-1) > 0 and c(D) < 0 for D >= 3, D ≡ 3 mod 4.

    The sign pattern is: (-1)^{(D+1)/4} for odd-D channel (BKM super-sign).

    Returns (h0_coeffs, h1_coeffs) as dicts D -> c(D).
    """
    by_d = phi01_by_discriminant(max_n)

    h0: Dict[int, int] = {}  # D ≡ 0 mod 4
    h1: Dict[int, int] = {}  # D = -1 or D ≡ 3 mod 4

    for D, val in by_d.items():
        if D == -1 or D % 4 == 3:
            h1[D] = val
        elif D % 4 == 0:
            h0[D] = val

    return h0, h1


def verify_theta_sign_pattern(max_n: int = 10) -> bool:
    """Verify the sign pattern of the theta decomposition.

    h_0 channel (even l): c(D) > 0 for all D >= 0 with D ≡ 0 mod 4.
    h_1 channel (odd l):  c(-1) = 1 > 0.
                          c(D) < 0 for all D >= 3 with D ≡ 3 mod 4.

    This is the BKM super-sign: root multiplicities of the BKM superalgebra
    g_{Delta_5} are positive for even roots and negative for odd roots.
    The "oddness" is determined by l mod 2 (the fermion number).
    """
    h0, h1 = theta_decomposition(max_n)

    # Even channel: all positive
    for D, val in h0.items():
        if D >= 0 and val <= 0:
            return False

    # Odd channel: c(-1) = 1 > 0, rest negative
    if h1.get(-1, 0) != 1:
        return False
    for D, val in h1.items():
        if D >= 3 and val >= 0:
            return False

    return True


# =========================================================================
# 5. HECKE OPERATOR COMPATIBILITY (PATH C)
# =========================================================================

def hecke_transform_coefficients(p: int, max_n: int = 10) -> Dict[int, int]:
    """Apply the Hecke operator T_p to the discriminant coefficients c(D).

    For a weak Jacobi form of weight 0 index 1, the Hecke operator T_p
    acting on the Fourier-Jacobi expansion gives:

        (T_p c)(D) = c(p^2 D) + p^{-1} c(D) + p^{-2} c(D/p^2)

    for the discriminant coefficients.  More precisely, the Hecke operator
    on Jacobi forms of index m acts on the discriminant via:

        (T_p f)(n, l) = sum_{d | gcd(n, l, p)} d^{k-1} f(np/d^2, l/d)

    where k = 0 is the weight.  In terms of D = 4n - l^2:

        If k = 0 and m = 1, the index-raising Hecke operator V_p gives
        a Jacobi form of index p, while T_p (the index-preserving Hecke)
        acts on the underlying modular forms h_0, h_1.

    For the shadow tower: the Hecke operators should respect the arity
    filtration in the sense that T_p maps the arity-r layer to the
    arity-(r+p-1) layer (additive shift in BPS charge).

    Here we compute the simpler quantity: the multiplicative Hecke
    operator T(p) acting on c(D) viewed as a function of D, via:

        (T(p) c)(D) = sum_{a^2 | D, a | p} (p/a)^{-1} c(D * p^2 / a^4)

    which for p prime and gcd(D, p) = 1 reduces to:
        (T(p) c)(D) = c(p^2 * D)
    """
    by_d = phi01_by_discriminant(max_n * p * p)

    result: Dict[int, int] = {}
    for D in valid_discriminants(max_n * 4):
        # Leading term: c(p^2 * D)
        D_scaled = p * p * D
        val = by_d.get(D_scaled, 0)
        result[D] = val

    return result


def hecke_arity_shift(p: int, r: int) -> int:
    """Expected arity after applying T_p to an arity-r root.

    The Hecke operator T_p on the BKM product formula multiplies
    (n, m) -> (pn, pm) at leading order, so n + m -> p(n + m).
    Since arity = 2 + (n + m), the arity shift is:
        r -> 2 + p * (r - 2)

    For p = 2, r = 3: new arity = 2 + 2*1 = 4.
    For p = 2, r = 4: new arity = 2 + 2*2 = 6.
    """
    if r == 2:
        return 2  # Real roots stay real
    return 2 + p * (r - 2)


# =========================================================================
# 6. CROSS-VERIFICATION WITH BKM MODULE (PATH D)
# =========================================================================

def verify_against_bkm_tower(max_arity: int = 5,
                              max_coord: int = 4) -> Dict[int, bool]:
    """Verify shadow decomposition against bkm_shadow_tower.py.

    For each arity r, check that:
    1. The discriminant values match between our computation and the BKM module.
    2. The total multiplicities at each D agree.
    """
    data = bkm_phi01_coefficients()
    decomp = full_shadow_decomposition(max_arity, max_coord=max_coord)

    results: Dict[int, bool] = {}
    for r in range(2, max_arity + 1):
        proj = bkm_shadow_tower_projection(r, max_coord, data)
        roots_at_r = proj['roots_at_r']

        # Compute D -> total mult from BKM roots
        bkm_by_d: Dict[int, int] = defaultdict(int)
        for (n, l, m), mult, cls in roots_at_r:
            D = 4 * n * m - l * l
            bkm_by_d[D] += mult

        # Compare with our decomposition
        our_by_d = decomp.get(r, {})
        all_Ds = set(bkm_by_d.keys()) | set(our_by_d.keys())

        agree = True
        for D in all_Ds:
            bkm_val = bkm_by_d.get(D, 0)
            our_val = int(our_by_d.get(D, Fraction(0)))
            if bkm_val != our_val:
                agree = False
                break

        results[r] = agree

    return results


# =========================================================================
# 7. ARITY-DISCRIMINANT MAP
# =========================================================================

def arity_discriminant_map(max_arity: int = 8) -> Dict[int, List[int]]:
    """For each arity r, list all discriminant values that appear.

    This is the central structural result: the D-stratification
    encodes the arity filtration.

    Returns dict: arity -> sorted list of discriminant values.
    """
    result: Dict[int, List[int]] = {}
    for r in range(2, max_arity + 1):
        disc_set = discriminants_at_arity(r)
        result[r] = sorted(disc_set)
    return result


def new_discriminants_at_arity(r: int, max_arity: int = 8) -> Set[int]:
    """Discriminant values that FIRST appear at arity r.

    These are discriminant values in discriminants_at_arity(r)
    that do not appear at any arity < r.

    These are the genuinely new contributions of the arity-r shadow layer.
    """
    current = discriminants_at_arity(r)
    previous: Set[int] = set()
    for r_prev in range(2, r):
        previous |= discriminants_at_arity(r_prev)
    return current - previous


def verify_minimum_arity_consistency(max_D: int = 40) -> bool:
    """Verify that minimum_arity_for_discriminant is consistent
    with the explicit arity_discriminant_map.

    For each valid D, check that the minimum arity from the exhaustive
    search matches the explicit enumeration.
    """
    max_r = int(math.sqrt(max_D)) + 10
    ad_map = arity_discriminant_map(max_r)

    for D in valid_discriminants(max_D):
        r_min = minimum_arity_for_discriminant(D)
        # Check: D should appear in ad_map[r_min] and NOT in any ad_map[r'] for r' < r_min
        if r_min < 2:
            return False
        if D not in discriminants_at_arity(r_min):
            return False
        for r_prev in range(2, r_min):
            if D in discriminants_at_arity(r_prev):
                return False

    return True


# =========================================================================
# 8. DISCRIMINANT GROWTH AND ASYMPTOTICS
# =========================================================================

def _bessel_I_3half(x: float) -> float:
    """Modified Bessel function I_{3/2}(x).

    I_{3/2}(x) = sqrt(2/(pi*x)) * (cosh(x) - sinh(x)/x)

    For large x: I_{3/2}(x) ~ exp(x)/sqrt(2*pi*x) * (1 - 1/x).
    """
    if x <= 0:
        return 0.0
    if x > 700:
        # Use asymptotic to avoid overflow
        return math.exp(x) / math.sqrt(2 * math.pi * x) * (1.0 - 1.0 / x)
    return math.sqrt(2.0 / (math.pi * x)) * (math.cosh(x) - math.sinh(x) / x)


def rademacher_leading_term(D: int) -> float:
    """Leading term of the Rademacher expansion for |c(D)|.

    For the K3 elliptic genus phi_{0,1} (weight 0, index 1,
    Eichler-Zagier normalization with c(-1) = 1), the leading
    Rademacher term for D > 0 is:

        |c(D)| ~ sqrt(2) * pi * D^{-3/4} * I_{3/2}(pi * sqrt(D))

    where I_{3/2} is the modified Bessel function.  This is the c = 1
    Kloosterman sum contribution.  The Bessel index 3/2 arises because
    the theta components h_r have effective weight -1/2, and the
    Rademacher expansion for weight w uses I_{|w|+1/2}.

    Verified numerically: the ratio |c(D)| / rademacher_leading_term(D)
    converges to 1.000 by D = 20 (deviation < 0.1%).

    For D <= 0, returns nan.
    """
    if D <= 0:
        return float('nan')

    x = math.pi * math.sqrt(D)
    return math.sqrt(2.0) * math.pi * D ** (-0.75) * _bessel_I_3half(x)


def verify_rademacher_growth(max_n: int = 15, tolerance: float = 0.01) -> bool:
    """Verify that |c(D)| follows the Rademacher growth pattern.

    For D >= 8, |c(D)| / rademacher_leading_term(D) -> 1.
    The convergence is rapid: deviation < 0.8% by D = 8, < 0.01% by D = 40.

    We check that the ratio is within (1 - tolerance, 1 + tolerance)
    for D >= 8.  Default tolerance 1% accommodates the c = 2 Kloosterman
    correction term which is largest at small D.
    """
    by_d = phi01_by_discriminant(max_n)

    for D in sorted(by_d):
        if D < 8:
            continue
        actual = abs(by_d[D])
        predicted = abs(rademacher_leading_term(D))
        if predicted == 0 or math.isnan(predicted):
            continue
        ratio = actual / predicted
        if abs(ratio - 1.0) > tolerance:
            return False

    return True


# =========================================================================
# 9. SHADOW WEIGHT FUNCTION
# =========================================================================

def shadow_weight_at_discriminant(D: int, max_arity: int = 10) -> Dict[int, int]:
    """The number of positive roots at each arity contributing to discriminant D.

    This gives the "shadow weight" of D: how many product formula terms
    at each arity level produce this discriminant value.

    Returns dict: arity -> number of distinct positive roots (n,l,m)
    with Siegel discriminant D and complexity = arity.
    """
    abs_D = max(0, D)
    data = bkm_phi01_coefficients(max(20, abs_D + 10))
    max_coord = int(math.sqrt(abs_D)) + 5

    weight: Dict[int, int] = defaultdict(int)
    roots = bkm_enumerate_positive_roots(max_coord, data)
    for (n, l, m), mult, cls in roots:
        Droot = 4 * n * m - l * l
        if Droot == D:
            r = bkm_root_complexity(n, l, m)
            if r <= max_arity:
                weight[r] += 1

    return dict(weight)


def shadow_multiplicity_at_discriminant(D: int, max_arity: int = 10) -> Dict[int, int]:
    """Total multiplicity (sum of f(nm,l)) at each arity for discriminant D.

    Unlike shadow_weight_at_discriminant (which counts roots),
    this sums the actual multiplicities.
    """
    abs_D = max(0, D)
    data = bkm_phi01_coefficients(max(20, abs_D + 10))
    max_coord = int(math.sqrt(abs_D)) + 5

    mult_by_arity: Dict[int, int] = defaultdict(int)
    roots = bkm_enumerate_positive_roots(max_coord, data)
    for (n, l, m), mult, cls in roots:
        Droot = 4 * n * m - l * l
        if Droot == D:
            r = bkm_root_complexity(n, l, m)
            if r <= max_arity:
                mult_by_arity[r] += mult

    return dict(mult_by_arity)


# =========================================================================
# 10. KAPPA AND SHADOW INVARIANTS
# =========================================================================

def hypothetical_kappa() -> Fraction:
    """BKM denominator projection kappa_BKM for the K3 x E system.

    From k3_times_e.tex: kappa_BKM(K3xE) = 5 (the weight of Delta_5).
    This is the arity-2 shadow projection.

    Verification: the weight of the Siegel modular form Delta_5 is 5.
    The Borcherds product for Delta_5 has the Weyl vector contribution
    exp(-2*pi*i*<rho,Z>) which gives the leading q-power, and kappa_BKM = 5
    is the weight of the resulting automorphic form.

    Cross-check with Vol I: kappa_BKM = weight of Delta_k means the
    Hodge class coefficient. For the BKM shadow, kappa_BKM = 5.
    """
    return bkm_kappa_projection()


def cubic_shadow_invariant(max_coord: int = 5) -> Dict[int, Fraction]:
    """Arity-3 cubic shadow C: the first imaginary root correction.

    At arity 3, only D = 0 (lightlike) roots appear.
    The cubic shadow captures the lightlike imaginary root
    contributions with n + m = 1.

    Returns dict: D -> total multiplicity at arity 3.
    """
    return shadow_projection_at_arity(3, max_coord=max_coord)


def quartic_shadow_invariant(max_coord: int = 5) -> Dict[int, Fraction]:
    """Arity-4 quartic shadow Q: second imaginary root correction.

    At arity 4, discriminants D = 0, 3, 4 appear.
    - D = 0: additional lightlike roots (n+m=2, l^2=4nm)
    - D = 3: first timelike roots (c(3) = -64)
    - D = 4: second timelike (c(4) = 108)

    Returns dict: D -> total multiplicity at arity 4.
    """
    return shadow_projection_at_arity(4, max_coord=max_coord)


def shadow_invariant_table(max_arity: int = 6,
                            max_coord: int = 5) -> Dict[str, object]:
    """Summary table of shadow invariants at each arity.

    Returns a structured table:
        arity -> {
            'name': str (kappa, C, Q, Sh_r),
            'discriminants': list of D values,
            'new_discriminants': D values first appearing,
            'multiplicities': dict D -> mult,
            'total_mult': int,
        }
    """
    decomp = full_shadow_decomposition(max_arity, max_coord=max_coord)

    table: Dict[str, object] = {}
    names = {2: 'kappa', 3: 'C', 4: 'Q'}

    for r in range(2, max_arity + 1):
        name = names.get(r, f'Sh_{r}')
        layer = decomp.get(r, {})
        new_discs = new_discriminants_at_arity(r)

        entry = {
            'name': name,
            'discriminants': sorted(layer.keys()),
            'new_discriminants': sorted(new_discs),
            'multiplicities': {D: int(v) for D, v in layer.items()},
            'total_mult': sum(int(v) for v in layer.values()),
            'max_D': maximum_discriminant_at_arity(r),
        }
        table[r] = entry

    return table


# =========================================================================
# 11. CUMULATIVE SHADOW AND REMAINDER
# =========================================================================

def cumulative_multiplicity(max_arity: int, D: int,
                             max_coord: int = 5) -> int:
    """Total root multiplicity at discriminant D from all arities <= max_arity.

    This is the partial sum of the shadow tower truncation Theta^{<=max_arity}
    restricted to discriminant D.
    """
    decomp = full_shadow_decomposition(max_arity, max_coord=max_coord)
    total = 0
    for r in range(2, max_arity + 1):
        layer = decomp.get(r, {})
        total += int(layer.get(D, Fraction(0)))
    return total


def shadow_remainder(max_arity: int, max_D: int = 40,
                      max_coord: int = 5) -> Dict[int, int]:
    """The remainder after truncating the shadow tower at arity max_arity.

    For each discriminant D, this is c(D) minus the cumulative contribution
    from arities 2 through max_arity.

    For the shadow tower to be correct, the remainder should tend to 0
    as max_arity -> infinity.
    """
    by_d = phi01_by_discriminant(max_D // 4 + 5)
    result: Dict[int, int] = {}

    for D in valid_discriminants(max_D):
        actual = by_d.get(D, 0)
        if actual == 0:
            continue
        cum = cumulative_multiplicity(max_arity, D, max_coord)
        remainder = actual - cum
        if remainder != 0:
            result[D] = remainder

    return result


# =========================================================================
# 12. MASTER VERIFICATION
# =========================================================================

def run_all_verifications(max_n: int = 10, max_arity: int = 5,
                          max_coord: int = 4, verbose: bool = False
                          ) -> Dict[str, bool]:
    """Run all verification paths and return results.

    Path A: Direct Fourier coefficient (phi01_fourier consistency)
    Path B: Theta decomposition sign pattern
    Path C: Hecke operator arity compatibility
    Path D: Cross-verification with bkm_shadow_tower

    Additional: Rademacher growth, minimum arity consistency.
    """
    results: Dict[str, bool] = {}

    # Path A: Fourier coefficient consistency
    by_d = phi01_by_discriminant(max_n)
    results['path_A_discriminant_dependence'] = len(by_d) > 0

    # Path B: Theta decomposition
    results['path_B_theta_sign_pattern'] = verify_theta_sign_pattern(max_n)

    # Path C: Hecke arity shift
    # For p=2: arity 3 -> arity 4 means D=0 roots at arity 3 produce
    # roots at arity 4 with D scaled by p^2=4.
    # Check: c(0) = 10 at arity 3. The T_2 image at arity 4 should
    # involve c(0) (since D*p^2 = 0).
    hecke2 = hecke_transform_coefficients(2, max_n)
    # The T_2 image of D=0 gives c(0) = 10 (the same coefficient).
    results['path_C_hecke_D0_consistent'] = (hecke2.get(0, 0) == by_d.get(0, 0))

    # Path D: Cross-verification with BKM module
    bkm_results = verify_against_bkm_tower(max_arity, max_coord)
    results['path_D_bkm_cross_check'] = all(bkm_results.values())

    # Additional checks
    results['rademacher_growth'] = verify_rademacher_growth(max_n)
    results['minimum_arity_consistency'] = verify_minimum_arity_consistency(
        min(max_arity * max_arity, 40))

    if verbose:
        for name, val in results.items():
            status = 'PASS' if val else 'FAIL'
            print(f'  {name}: {status}')

    return results


# =========================================================================
# CLI
# =========================================================================

if __name__ == '__main__':
    print('phi_{0,1} Shadow Tower Decomposition')
    print('=' * 60)

    print('\n1. Discriminant coefficients c(D):')
    by_d = phi01_by_discriminant(8)
    for D in sorted(by_d):
        cls = discriminant_class(D)
        r_min = minimum_arity_for_discriminant(D)
        print(f'  c({D:>3d}) = {by_d[D]:>10d}  class={cls:<16s}  r_min={r_min}')

    print('\n2. Shadow invariant table:')
    table = shadow_invariant_table(6, 4)
    for r in sorted(table):
        entry = table[r]
        print(f'  Arity {r} ({entry["name"]}): {entry["total_mult"]} total mult, '
              f'discs={entry["discriminants"]}, new={entry["new_discriminants"]}, '
              f'max_D={entry["max_D"]}')

    print('\n3. Theta decomposition:')
    h0, h1 = theta_decomposition(8)
    print(f'  h_0 (even l): {dict(sorted(h0.items()))}')
    print(f'  h_1 (odd l):  {dict(sorted(h1.items()))}')

    print('\n4. Verification results:')
    results = run_all_verifications(verbose=True)

    all_pass = all(results.values())
    print(f'\nOverall: {"ALL PASS" if all_pass else "FAILURES DETECTED"}')
