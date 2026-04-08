r"""
Abelian (2,0) pushforward on K3 x E: shadow tower comparison.

OVERVIEW
========

The holomorphically twisted abelian (2,0) tensor multiplet on a CY3
X = K3 x E, pushed forward along K3 via Costello-Gwilliam, produces
a free-field chiral algebra A_free on E.  This module computes its
shadow tower (class G, depth 2) and compares with the K3 sigma model
VOA (class M, depth infinity) and the BKM root multiplicities from
phi_{0,1}.

KEY MATHEMATICAL CONTENT
========================

1. FREE-FIELD PUSHFORWARD.
   The chiral algebra A_free is a lattice/Heisenberg VA from the
   fiber cohomology of Omega^2_{X,cl}.  By the Vol I lattice curvature
   theorem: kappa(A_free) = rank(Lambda), S_3 = S_4 = 0, class G.

2. K3 SIGMA MODEL.
   The c=6 N=(4,4) superconformal VA has kappa = 2 = dim_C(K3),
   S_3 = 2, S_4 = 5/156, class M.  The MC recursion produces the
   full shadow tower.

3. THE KAPPA-COLLAPSE.
   rank(Lambda) -> 2: the non-linear sigma model constrains kappa
   to dim_C, not rank.  This is structural, not perturbative.

4. ROOT MULTIPLICITY CONSTANCY.
   sum_{ell(alpha)=L} mult(alpha) = 24 = chi(K3) at every level L.
   Proved from the modular constancy of phi_{0,1}(tau, 0) = 12.

MULTI-PATH VERIFICATION
=======================

Path 1: MC recursion from (kappa, S3, S4) initial data
Path 2: Cross-check S_r values against cy_bar_n4sca_engine.py
Path 3: Root multiplicity constancy by direct enumeration
Path 4: Interior cancellation at each level from phi_{0,1} table

CONVENTIONS
===========

- phi_{0,1} in Eichler-Zagier convention: phi_{0,1}(tau, 0) = 12 (AP38)
- kappa = modular characteristic of FULL algebra, not c/2 (AP48)
- Discriminant-indexed coefficients: c(D) from phi_{0,1}(tau, z) = sum c(4n-l^2) q^n y^l

References:
  working_notes.tex, Section "The abelian (2,0) pushforward on K3 x E"
  Eichler-Zagier, "The Theory of Jacobi Forms" (1985), p. 108
  Costello-Gwilliam, "Factorization algebras in quantum field theory" (2021), Ch. 6
  Vol I: thm:lattice:curvature-braiding-orthogonal (lattice_foundations.tex)
  Vol I: thm:obstruction-recursion (higher_genus_modular_koszul.tex)
  Vol I: thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Tuple

F = Fraction


# =========================================================================
# 0. phi_{0,1} Fourier data (Eichler-Zagier convention, AP38)
# =========================================================================

PHI01_DISCRIMINANT: Dict[int, int] = {
    -1: 1, 0: 10, 3: -64, 4: 108, 7: -513, 8: 808,
    11: -2752, 12: 4016, 15: -11775, 16: 16524,
    19: -43200, 20: 58640, 23: -141826, 24: 188304,
    27: -427264, 28: 556416, 31: -1201149, 32: 1541096,
    35: -3189120, 36: 4038780,
}


def phi01_coeff_D(D: int) -> int:
    """Discriminant-indexed coefficient c(D) of phi_{0,1}."""
    return PHI01_DISCRIMINANT.get(D, 0)


def phi01_coeff(n: int, l: int) -> int:
    """Fourier coefficient c(n, l) = c(D) where D = 4n - l^2."""
    return phi01_coeff_D(4 * n - l * l)


# =========================================================================
# 1. Shadow tower initial data
# =========================================================================

# Free-field pushforward (abelian (2,0), class G)
# Rank is not yet computed (depends on closure constraint long exact seq).
# Upper bound: 24 from fiber cohomology of Omega^2_X.
# Lower bound: 20 from H^{1,1}(K3) sector (survives closure).
KAPPA_FREE_UPPER = F(24)
KAPPA_FREE_LOWER = F(20)
S3_FREE = F(0)
S4_FREE = F(0)

# K3 sigma model (N=4 SCA at c=6, class M)
KAPPA_SIGMA = F(2)
S3_SIGMA = F(2)
S4_SIGMA = F(5, 156)
DELTA_SIGMA = F(8) * KAPPA_SIGMA * S4_SIGMA  # = 20/39


# =========================================================================
# 2. MC recursion (imported from Vol I or self-contained)
# =========================================================================

def mc_recursion(kappa: Fraction, S3: Fraction, S4: Fraction,
                 max_r: int = 30) -> Dict[int, Fraction]:
    """Shadow tower via Maurer-Cartan recursion (exact rational).

    S_r = -(1/(2r*kappa)) * sum_{j+k=r+2, 2<=j<=k<r} f(j,k)*j*k*S_j*S_k
    where f(j,k) = 1 if j<k, 1/2 if j=k.
    """
    S: Dict[int, Fraction] = {2: kappa, 3: S3, 4: S4}
    for r in range(5, max_r + 1):
        obs = F(0)
        target = r + 2
        for j in range(3, target // 2 + 1):
            k = target - j
            if k < j or k >= r:
                continue
            if j not in S or k not in S:
                continue
            bracket = F(j) * F(k) * S[j] * S[k]
            obs += bracket / F(2) if j == k else bracket
        S[r] = -obs / (F(2) * F(r) * kappa) if kappa != 0 else F(0)
    return S


# =========================================================================
# 3. BKM root multiplicity analysis
# =========================================================================

def bkm_positive_roots_at_level(level: int) -> List[Tuple[Tuple[int, int, int], int, int]]:
    """All positive roots at level n+m = level, with multiplicity.

    Returns list of ((n, l, m), D, mult).
    Positive root: n>0, or (n=0 and m>0), or (n=m=0 and l<0).
    """
    out = []
    for n in range(level + 1):
        m = level - n
        bound = int(math.isqrt(4 * n * m + 1)) + 2
        for l in range(-bound, bound + 1):
            D = 4 * n * m - l * l
            mult = phi01_coeff_D(D)
            if mult == 0:
                continue
            positive = (n > 0) or (n == 0 and m > 0) or (n == 0 and m == 0 and l < 0)
            if positive:
                out.append(((n, l, m), D, mult))
    return out


def bkm_total_mult_at_level(level: int) -> int:
    """Sum of multiplicities of positive roots at level n+m."""
    return sum(mult for _, _, mult in bkm_positive_roots_at_level(level))


def bkm_boundary_mult_at_level(level: int) -> int:
    """Sum of multiplicities of boundary roots (n=0 or m=0) at level."""
    total = 0
    for n in [0, level]:
        m = level - n
        bound = int(math.isqrt(4 * n * m + 1)) + 2
        for l in range(-bound, bound + 1):
            D = 4 * n * m - l * l
            mult = phi01_coeff_D(D)
            if mult == 0:
                continue
            positive = (n > 0) or (n == 0 and m > 0) or (n == 0 and m == 0 and l < 0)
            if positive:
                total += mult
    return total


def bkm_interior_mult_at_level(level: int) -> int:
    """Sum of multiplicities of interior roots (n>0 and m>0) at level."""
    total = 0
    for n in range(1, level):
        m = level - n
        if m < 1:
            continue
        bound = int(math.isqrt(4 * n * m + 1)) + 2
        for l in range(-bound, bound + 1):
            D = 4 * n * m - l * l
            mult = phi01_coeff_D(D)
            if mult != 0:
                total += mult
    return total


def max_discriminant_at_level(level: int) -> int:
    """Maximum D = 4nm - l^2 achievable at level n+m with n,m >= 1."""
    if level < 2:
        return -1
    # max of 4*n*(level-n) over n in [1, level-1]
    # This is maximized at n = level/2
    n_opt = level // 2
    m_opt = level - n_opt
    return 4 * n_opt * m_opt


def level_has_complete_data(level: int) -> bool:
    """Whether the phi_{0,1} table has all needed coefficients at this level."""
    max_D = max_discriminant_at_level(level)
    return max_D <= max(PHI01_DISCRIMINANT.keys())


# =========================================================================
# 4. Shadow tower computations
# =========================================================================

def sigma_model_shadow_tower(max_r: int = 20) -> Dict[int, Fraction]:
    """Shadow tower of the K3 sigma model VOA."""
    return mc_recursion(KAPPA_SIGMA, S3_SIGMA, S4_SIGMA, max_r=max_r)


def free_field_shadow_tower(kappa: Fraction, max_r: int = 20) -> Dict[int, Fraction]:
    """Shadow tower of the free-field pushforward (class G, terminates)."""
    return mc_recursion(kappa, S3_FREE, S4_FREE, max_r=max_r)


# =========================================================================
# 5. Comparison and analysis
# =========================================================================

def kappa_collapse_data() -> Dict[str, Any]:
    """Document the kappa-collapse from rank to dim_C."""
    return {
        'kappa_free_upper': KAPPA_FREE_UPPER,
        'kappa_free_lower': KAPPA_FREE_LOWER,
        'kappa_sigma': KAPPA_SIGMA,
        'kappa_bps': F(5),
        'collapse_ratio_upper': KAPPA_FREE_UPPER / KAPPA_SIGMA,
        'collapse_ratio_lower': KAPPA_FREE_LOWER / KAPPA_SIGMA,
        'second_quantization_ratio': F(5, 3),
        'note': ('kappa_free = rank(Lambda) in [20, 24]; '
                 'kappa_sigma = dim_C(K3) = 2; '
                 'kappa_BPS = 5 = weight(Delta_5). '
                 'The collapse is structural (AP48), not perturbative.'),
    }


def root_mult_constancy_verification(max_level: int = 6) -> Dict[int, Dict[str, Any]]:
    """Verify sum mult = 24 at each level.

    Returns per-level data: boundary sum, interior sum, total,
    and whether the phi_{0,1} table covers all needed discriminants.
    """
    results = {}
    for lev in range(1, max_level + 1):
        boundary = bkm_boundary_mult_at_level(lev)
        interior = bkm_interior_mult_at_level(lev)
        complete = level_has_complete_data(lev)
        results[lev] = {
            'boundary_mult': boundary,
            'interior_mult': interior,
            'total_mult': boundary + interior,
            'expected': 24,
            'data_complete': complete,
            'correct': (boundary + interior == 24) if complete else None,
        }
    return results
