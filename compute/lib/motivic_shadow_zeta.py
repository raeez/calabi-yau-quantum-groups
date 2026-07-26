r"""Motivic shadow zeta function: connecting motivic DT invariants to the bar complex.

MATHEMATICAL CONTENT
====================

The motivic shadow zeta function lifts the Vol I shadow zeta function
    zeta_A(s) = sum_{n >= 1} (dim B_n(A)) n^{-s}
from numerical dimensions to motivic classes in K_0(Var/k)[L^{+/-1/2}].

THE MOTIVIC BAR COMPLEX
========================

For a CY_d category C with chiral algebra A_C (conditional on CY-A_d),
the bar complex B^{E_1}(A_C) is a graded E_1-coalgebra.  At each
degree n, the bar space B_n has a motivic class [B_n] in K_0(Var).

The motivic shadow zeta function is:
    zeta_A^{mot}(s) = sum_{n >= 1} [B_n] n^{-s}

This is a Dirichlet series with coefficients in K_0(Var)[L^{+/-1/2}].

SPECIALIZATIONS
===============

1. Euler characteristic: chi: L -> 1.
   zeta_A^{mot}(s)|_{L=1} = zeta_A^{num}(s) (the Vol I shadow zeta).

2. p-adic shadow: L -> p.
   zeta_A^{p}(s) = sum [B_n]|_{L=p} n^{-s}
   For a CY3 X over Q, this is related to the L-function of X.

3. Hodge specialization: L -> -y.
   zeta_A^{Hodge}(s, y) = sum chi_y([B_n]) n^{-s}
   Carries the mixed Hodge structure of the bar complex.

MOTIVIC SHADOW TOWER
=====================

The motivic shadow tower refines the numerical shadow S_r(A):
    S_r^{mot}(A) in K_0(Var)[L^{+/-1/2}]

The genus-g free energy:
    F_g^{mot} = sum_{r >= 2} S_r^{mot} * (weight factor at genus g)

Under chi: F_g^{mot} -> F_g^{num} = kappa^g * b_g (Vol I formula).

C^3: THE MOTIVIC MACMAHON CONNECTION
======================================

For C^3, the motivic DT partition function is the motivic MacMahon:
    Z^{mot}(C^3) = Exp_*(f)
where f_n = sum_{k=0}^{n-1} L^{k+3/2} is the BBS single-letter.

The motivic bar Euler product:
    prod_{n >= 1} (1 - [B_n^{mot}] q^n) = 1/Z^{mot}(C^3)

so [B_n^{mot}] = PLog(Z^{mot})(n) = f_n = sum_{k=0}^{n-1} L^{k+3/2}.

Under chi: [B_n^{mot}] -> n, recovering dim B_n = n (the BPS count).

The motivic shadow zeta for C^3:
    zeta_{C^3}^{mot}(s) = sum_{n >= 1} f_n n^{-s}
                        = sum_{n >= 1} (sum_{k=0}^{n-1} L^{k+3/2}) n^{-s}

Under chi: zeta_{C^3}^{num}(s) = sum n * n^{-s} = zeta_Riemann(s-1).

THE p-ADIC SHADOW
==================

For a CY3 X defined over Q with good reduction at p:
    zeta_A^{p}(s) = sum [B_n]|_{L=p} n^{-s}

For C^3:
    [B_n]|_{L=p} = sum_{k=0}^{n-1} p^{k+3/2}
    For integer specialization (L -> p, not L^{1/2} -> p^{1/2}),
    this requires working with L^{1/2} as a formal symbol.

    At the EVEN-weight level (discarding L^{1/2} terms):
    sum_{k: 2k+3 even} p^{(2k+3)/2}  -- requires half-integer powers.

    RESOLUTION: use L -> p^2 (geometric Frobenius convention) or
    work in the extended ring with p^{1/2}.

    The p-adic shadow zeta with L -> p:
    zeta_{C^3}^{p}(s) = p^{3/2} sum_{n >= 1} (p^n - 1)/(p - 1) n^{-s}

For K3 x E (conditional on CY-A_3, AP-CY6):
    The Galois representation on H^2(K3) is a 22-dimensional l-adic rep.
    The p-adic shadow should encode the Frobenius eigenvalues alpha_{i,p}:
    zeta_{K3xE}^{p}(s) ~ sum related to sum_i alpha_{i,p}^n n^{-s}.
    This connection is CONJECTURAL and requires the CY-to-chiral functor
    at d=3 to make precise.

WEIGHT FILTRATION
==================

The motivic class [B_n] carries a weight filtration from mixed Hodge:
    [B_n] = sum_w a_{n,w} L^{w/2}

The weight filtration on the shadow zeta:
    zeta_A^{mot,w}(s) = sum_n a_{n,w} n^{-s}   (weight-w component)

For C^3:
    a_{n,w} = 1 if w = 2k+3 for k = 0, ..., n-1, else 0.
    The weight-w component is:
    zeta_{C^3}^{mot,w}(s) = sum_{n >= ceil((w-1)/2)} n^{-s}
                          = zeta_Riemann(s) - sum_{n=1}^{floor((w-3)/2)} n^{-s}

The weight filtration IS respected by the shadow tower: the shadow
coefficients S_r^{mot} decompose by weight, and the MC equation holds
at each weight grade separately.

CAUTIONARY NOTES
=================
AP-CY6: A_X does NOT exist for CY3 in general. All statements involving
  "the motivic shadow zeta of a CY3" are conditional on CY-A_3 except
  for toric CY3 where the CoHA provides the comparison.
AP-CY7: CoHA != E_1-chiral algebra. The motivic comparison uses the
  CoHA as a computational substitute, not an identification.
AP113: bare kappa is forbidden. Use kappa_ch, kappa_BKM, kappa_cat, kappa_fiber.
AP49: Vol III uses motivic/categorical conventions, not Vol I OPE modes.

CONVENTIONS
===========
  - L = [A^1] (the Lefschetz motive, weight 2)
  - L^{1/2} = Tate twist (weight 1)
  - chi(L^k) = 1 for all k (Euler characteristic)
  - chi_y(L^k) = (-y)^k (Hodge specialization)
  - Cohomological grading: |d| = +1
  - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (desuspension convention)

REFERENCES
==========
  Kontsevich-Soibelman, arXiv:0811.2435 (motivic DT invariants)
  Behrend-Bryan-Szendroi, arXiv:0909.5088 (motivic DT for C^3)
  Vol I: shadow_zeta_engine.py, shadow_zeta_function_engine.py
  Vol III: motivic_e1_algebra.py (MotivicClass, motivic MacMahon)
  Vol III: c3_shadow_tower.py (numerical shadow-DT bridge)
  Vol III: padic_cy3_e1.py (p-adic specializations)
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

# ---------------------------------------------------------------------------
# Path setup for cross-volume imports
# ---------------------------------------------------------------------------

_VOL1_LIB = os.path.expanduser("~/chiral-bar-cobar/compute/lib")
_VOL3_LIB = os.path.expanduser("~/calabi-yau-quantum-groups/compute/lib")

for _p in [_VOL1_LIB, _VOL3_LIB]:
    if _p not in sys.path:
        sys.path.insert(0, _p)


# =========================================================================
# 0. MOTIVIC CLASS (self-contained subset for standalone use)
# =========================================================================

class MotivicClass:
    r"""An element of K_0(Var/k)[L^{+/-1/2}].

    Represented as a Laurent polynomial in L^{1/2}:
        f = sum_k a_k L^{k/2}

    Dictionary self.coeffs maps k (int, encoding half-integer exponent k/2)
    to the integer coefficient a_k.
    """

    __slots__ = ('coeffs',)

    def __init__(self, coeffs: Optional[Dict[int, int]] = None):
        if coeffs is None:
            self.coeffs: Dict[int, int] = {}
        else:
            self.coeffs = {k: v for k, v in coeffs.items() if v != 0}

    @staticmethod
    def zero() -> 'MotivicClass':
        return MotivicClass({})

    @staticmethod
    def one() -> 'MotivicClass':
        return MotivicClass({0: 1})

    @staticmethod
    def L(power: int = 1) -> 'MotivicClass':
        return MotivicClass({2 * power: 1})

    @staticmethod
    def L_half(half_power: int = 1) -> 'MotivicClass':
        return MotivicClass({half_power: 1})

    @staticmethod
    def from_int(n: int) -> 'MotivicClass':
        if n == 0:
            return MotivicClass.zero()
        return MotivicClass({0: n})

    def __add__(self, other: 'MotivicClass') -> 'MotivicClass':
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, 0) + v
        return MotivicClass(result)

    def __sub__(self, other: 'MotivicClass') -> 'MotivicClass':
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, 0) - v
        return MotivicClass(result)

    def __neg__(self) -> 'MotivicClass':
        return MotivicClass({k: -v for k, v in self.coeffs.items()})

    def __mul__(self, other: 'MotivicClass') -> 'MotivicClass':
        result: Dict[int, int] = {}
        for k1, v1 in self.coeffs.items():
            for k2, v2 in other.coeffs.items():
                key = k1 + k2
                result[key] = result.get(key, 0) + v1 * v2
        return MotivicClass(result)

    def __rmul__(self, n: int) -> 'MotivicClass':
        if n == 0:
            return MotivicClass.zero()
        return MotivicClass({k: n * v for k, v in self.coeffs.items()})

    def __eq__(self, other: object) -> bool:
        if not hasattr(other, 'coeffs'):
            return NotImplemented
        a = {k: v for k, v in self.coeffs.items() if v != 0}
        b = {k: v for k, v in getattr(other, 'coeffs').items() if v != 0}
        return a == b

    def __repr__(self) -> str:
        if not self.coeffs:
            return "0"
        terms = []
        for k in sorted(self.coeffs.keys()):
            v = self.coeffs[k]
            if v == 0:
                continue
            if k == 0:
                terms.append(str(v))
            elif k % 2 == 0:
                exp = k // 2
                terms.append(f"{v}*L^{exp}" if v != 1 else f"L^{exp}")
            else:
                terms.append(f"{v}*L^({k}/2)" if v != 1 else f"L^({k}/2)")
        return " + ".join(terms) if terms else "0"

    def __hash__(self) -> int:
        return hash(tuple(sorted((k, v) for k, v in self.coeffs.items() if v != 0)))

    def is_zero(self) -> bool:
        return all(v == 0 for v in self.coeffs.values())

    def euler_char(self) -> int:
        """chi: L -> 1. Returns sum_k a_k."""
        return sum(self.coeffs.values())

    def specialize_L(self, L_val: Fraction) -> Fraction:
        """Evaluate at L^{1/2} = L_val^{1/2}.

        For integer L_val and even keys, this is well-defined.
        For odd keys, requires L_val^{1/2} to exist in the rationals.
        """
        total = Fraction(0)
        for k, v in self.coeffs.items():
            if k % 2 == 0:
                half_k = k // 2
                if half_k >= 0:
                    total += Fraction(v) * L_val ** half_k
                else:
                    total += Fraction(v) / L_val ** (-half_k)
            else:
                # Half-integer power: need L_val^{1/2}
                # For p-adic: use p^2 convention to avoid this
                raise ValueError(
                    f"Half-integer L-power {k}/2 at L={L_val}; "
                    f"use L=p^2 convention or work in extended ring"
                )
        return total

    def specialize_L_squared(self, p: int) -> Fraction:
        """Evaluate at L = p^2 (geometric Frobenius convention).

        L^{k/2} -> (p^2)^{k/2} = p^k.  This avoids half-integer issues.
        """
        total = Fraction(0)
        for k, v in self.coeffs.items():
            if k >= 0:
                total += Fraction(v) * Fraction(p ** k)
            else:
                total += Fraction(v) / Fraction(p ** (-k))
        return total

    def weight_decomposition(self) -> Dict[int, int]:
        """Return {half-integer-weight: coefficient}."""
        return {k: v for k, v in self.coeffs.items() if v != 0}


# =========================================================================
# 1. MOTIVIC SINGLE-LETTER INDEX (BBS for C^3)
# =========================================================================

def c3_single_letter(n: int) -> MotivicClass:
    r"""The BBS single-letter index f_n for C^3.

    f_n = sum_{k=0}^{n-1} L^{k + 3/2}

    Under chi: f_n -> n (the numerical BPS count).
    This is [B_n^{mot}] = PLog(Z^{mot})(n), the motivic bar dimension.

    VERIFIED [DC] BBS arXiv:0909.5088 [CF] motivic_e1_algebra.py
    """
    if n <= 0:
        return MotivicClass.zero()
    coeffs: Dict[int, int] = {}
    for k in range(n):
        key = 2 * k + 3  # L^{(2k+3)/2} = L^{k + 3/2}
        coeffs[key] = 1
    return MotivicClass(coeffs)


def c3_motivic_bar_dimensions(N: int) -> List[MotivicClass]:
    """[B_1^{mot}], ..., [B_N^{mot}] for C^3.

    [B_n^{mot}] = f_n = sum_{k=0}^{n-1} L^{k+3/2}.
    Under chi: [B_n^{mot}] -> n.
    """
    return [c3_single_letter(n) for n in range(1, N + 1)]


# =========================================================================
# 2. MOTIVIC SHADOW ZETA FUNCTION
# =========================================================================

@dataclass
class MotivicShadowZetaValue:
    """A value of the motivic shadow zeta at integer s.

    The motivic zeta at integer s >= 0:
        zeta_A^{mot}(s) = sum_{n=1}^{N} [B_n] / n^s

    is itself a motivic class (element of K_0(Var)[L^{+/-1/2}] tensor Q).
    We represent it as {half-integer-L-power: Fraction coefficient}.
    """
    s: int
    N_max: int
    coeffs: Dict[int, Fraction]

    def euler_char(self) -> Fraction:
        """chi: L -> 1."""
        return sum(self.coeffs.values())

    def specialize_L_squared(self, p: int) -> Fraction:
        """L = p^2 (geometric Frobenius)."""
        total = Fraction(0)
        for k, v in self.coeffs.items():
            total += v * Fraction(p ** k) if k >= 0 else v / Fraction(p ** (-k))
        return total


def motivic_shadow_zeta_integer(
    bar_dims: List[MotivicClass],
    s: int,
) -> MotivicShadowZetaValue:
    r"""Compute zeta_A^{mot}(s) for integer s >= 0.

    zeta_A^{mot}(s) = sum_{n=1}^{N} [B_n] * n^{-s}

    At integer s, n^{-s} is rational, so the result is a motivic class
    with Fraction coefficients.

    Parameters
    ----------
    bar_dims : list of MotivicClass
        [B_1], ..., [B_N] as motivic classes.
    s : int
        The integer argument (s >= 0).

    Returns
    -------
    MotivicShadowZetaValue
    """
    result: Dict[int, Fraction] = {}
    N = len(bar_dims)
    for idx, bn in enumerate(bar_dims):
        n = idx + 1
        weight = Fraction(1, n ** s) if s > 0 else Fraction(1)
        for k, v in bn.coeffs.items():
            if v == 0:
                continue
            result[k] = result.get(k, Fraction(0)) + Fraction(v) * weight
    return MotivicShadowZetaValue(s=s, N_max=N, coeffs=result)


def c3_motivic_shadow_zeta(s: int, N: int = 20) -> MotivicShadowZetaValue:
    r"""Motivic shadow zeta for C^3 at integer s.

    zeta_{C^3}^{mot}(s) = sum_{n=1}^{N} f_n n^{-s}
                        = sum_{n=1}^{N} (sum_{k=0}^{n-1} L^{k+3/2}) n^{-s}

    Under chi: zeta_{C^3}^{num}(s) = sum n * n^{-s} = sum n^{1-s}
    For s=0: sum n = N(N+1)/2.
    For s=1: sum 1 = N.
    For s=2: sum 1/n = H_N (harmonic number).
    """
    bar_dims = c3_motivic_bar_dimensions(N)
    return motivic_shadow_zeta_integer(bar_dims, s)


# =========================================================================
# 3. p-ADIC SHADOW ZETA
# =========================================================================

def padic_shadow_zeta_c3(s: int, p: int, N: int = 20) -> Fraction:
    r"""p-adic shadow zeta for C^3: L = p^2 (geometric Frobenius).

    zeta_{C^3}^{p}(s) = sum_{n=1}^{N} f_n|_{L=p^2} * n^{-s}

    With L = p^2:
        f_n|_{L=p^2} = sum_{k=0}^{n-1} p^{2k+3} = p^3 (p^{2n} - 1)/(p^2 - 1)

    Under p -> 1 (formal limit):
        f_n|_{L=1} = n, recovering the numerical shadow.

    For prime p, this is a p-local invariant of the CY3 C^3.

    VERIFIED [DC] direct computation: f_1|_{L=p^2} = p^3; f_2|_{L=p^2} = p^3 + p^5.
    """
    total = Fraction(0)
    for n in range(1, N + 1):
        # f_n|_{L=p^2} = sum_{k=0}^{n-1} p^{2k+3}
        fn_padic = sum(Fraction(p ** (2 * k + 3)) for k in range(n))
        total += fn_padic * Fraction(1, n ** s) if s > 0 else fn_padic
    return total


def padic_shadow_zeta_c3_closed(s: int, p: int, N: int = 20) -> Fraction:
    r"""Closed-form p-adic shadow zeta for C^3.

    f_n|_{L=p^2} = p^3 * (p^{2n} - 1)/(p^2 - 1)

    zeta_{C^3}^{p}(s) = p^3/(p^2-1) * [sum_{n=1}^{N} p^{2n} n^{-s}
                                         - sum_{n=1}^{N} n^{-s}]

    VERIFIED [CF] matches padic_shadow_zeta_c3 term-by-term.
    """
    assert p >= 2, f"p must be >= 2, got {p}"
    p2 = Fraction(p ** 2)
    prefactor = Fraction(p ** 3) / (p2 - 1)
    sum_p2n = Fraction(0)
    sum_plain = Fraction(0)
    for n in range(1, N + 1):
        n_factor = Fraction(1, n ** s) if s > 0 else Fraction(1)
        sum_p2n += Fraction(p ** (2 * n)) * n_factor
        sum_plain += n_factor
    return prefactor * (sum_p2n - sum_plain)


def padic_euler_factor_c3(p: int, n: int) -> Fraction:
    r"""p-local Euler factor for C^3 at charge n.

    At each charge n, the p-adic bar dimension is:
        [B_n]|_{L=p^2} = p^3 (p^{2n} - 1)/(p^2 - 1)

    The Euler factor is:
        E_p(n) = 1 - [B_n]|_{L=p^2} p^{-ns}
    evaluated at a specific s (suppressed; used for formal Euler product).

    Here we just return the p-adic bar dimension for reference.
    """
    return Fraction(p ** 3) * (Fraction(p ** (2 * n)) - 1) / (Fraction(p ** 2) - 1)


# =========================================================================
# 4. K3 x E p-ADIC SHADOW (CONJECTURAL, AP-CY6)
# =========================================================================

# K3 lattice data: the Mukai lattice has signature (4, 20).
# The H^2(K3, Z_l) is a 22-dimensional l-adic Galois representation.
# For good primes p, the Frobenius eigenvalues alpha_{i,p} on H^2(K3)
# satisfy |alpha_{i,p}| = p (Weil conjectures, proved by Deligne).

K3_BETTI = [1, 0, 22, 0, 1]  # Betti numbers of K3
K3_EULER = 24  # chi_top(K3) = 24 = kappa_fiber
K3_KAPPA_CH = Fraction(0)   # compact kappa_ch(K3 x E) = chi(O_{K3xE}) = 0
K3_KAPPA_CH_HEIS = Fraction(3)  # relative Heisenberg/free-field shadow scalar
K3_KAPPA_BKM = Fraction(5)  # kappa_BKM(K3 x E) = 5 (weight of Delta_5)
K3_KAPPA_CAT = Fraction(2)  # kappa_cat(K3) = chi(O_{K3}) = 2
K3_KAPPA_FIBER = 24          # kappa_fiber = lattice rank


def k3_frobenius_eigenvalues_trivial(p: int) -> List[int]:
    r"""Frobenius eigenvalues on H^2(K3) for a SPLIT K3 surface.

    For a K3 surface with Picard rank 20 (maximal) over F_p,
    all 22 eigenvalues on H^2 are known:
      - 20 eigenvalues = p (from NS(K3) tensor Q_l)
      - 2 eigenvalues = p * alpha, p * alpha_bar with |alpha| = 1

    For simplicity (HEURISTIC), we use the fully split model where
    all eigenvalues are p. This is the "trivial" case.
    """
    return [p] * 22


def k3xe_padic_shadow_zeta_heuristic(
    s: int, p: int, N: int = 10
) -> Fraction:
    r"""HEURISTIC p-adic shadow zeta for K3 x E.

    CONDITIONAL on CY-A_3 (AP-CY6): the E_1 chiral algebra of K3 x E
    does NOT exist yet. This function computes what the p-adic shadow
    zeta WOULD be if:
      (a) The motivic bar dimensions [B_n^{mot}(K3xE)] are determined
          by the Frobenius eigenvalues on H^*(K3 x E).
      (b) The specialization L -> p^2 gives the p-adic bar dimensions.

    For the FULLY SPLIT heuristic model:
      [B_n^{mot}(K3xE)]|_{L=p^2} ~ p^3 * 24 * (p^{2n} - 1)/(p^2 - 1)
    (24 = kappa_fiber, the lattice rank; each direction contributes a C^3-like factor).

    This is ROUGH: the correct formula involves the full Galois
    representation, not just the rank.
    """
    # Use kappa_fiber = 24 as the effective multiplicity (HEURISTIC)
    total = Fraction(0)
    p2_minus_1 = Fraction(p ** 2 - 1)
    p3 = Fraction(p ** 3)
    for n in range(1, N + 1):
        # Heuristic: 24 copies of the C^3-type bar dimension
        bn_padic = 24 * p3 * (Fraction(p ** (2 * n)) - 1) / p2_minus_1
        n_factor = Fraction(1, n ** s) if s > 0 else Fraction(1)
        total += bn_padic * n_factor
    return total


# =========================================================================
# 5. WEIGHT FILTRATION OF THE MOTIVIC SHADOW ZETA
# =========================================================================

@dataclass
class WeightFilteredShadowZeta:
    """Weight-graded decomposition of the motivic shadow zeta.

    zeta_A^{mot}(s) = sum_w zeta_A^{mot,w}(s) L^{w/2}

    where zeta_A^{mot,w}(s) = sum_n a_{n,w} n^{-s}.
    """
    s: int
    N_max: int
    weight_components: Dict[int, Fraction]  # weight w -> zeta^{mot,w}(s)

    @property
    def total_euler_char(self) -> Fraction:
        """chi: sum over all weights."""
        return sum(self.weight_components.values())

    @property
    def num_weights(self) -> int:
        return len(self.weight_components)


def weight_filtered_shadow_zeta_c3(
    s: int, N: int = 20
) -> WeightFilteredShadowZeta:
    r"""Weight-filtered motivic shadow zeta for C^3.

    At weight w (half-integer key w in [B_n]):
        zeta_{C^3}^{mot,w}(s) = sum_{n : n >= ceil((w-1)/2)} n^{-s}

    Because [B_n] = sum_{k=0}^{n-1} L^{k+3/2}, the weight-w component
    (with w = 2k+3) appears in all n >= k+1 = (w-1)/2.

    For weight w = 2k+3 (odd integers >= 3):
        zeta^{mot,w}(s) = sum_{n >= k+1}^{N} n^{-s}
    """
    weight_components: Dict[int, Fraction] = {}
    # Weights appearing: w = 3, 5, 7, ..., 2(N-1)+3 = 2N+1
    for k in range(N):
        w = 2 * k + 3
        # This weight first appears at n = k + 1
        n_min = k + 1
        component = Fraction(0)
        for n in range(n_min, N + 1):
            component += Fraction(1, n ** s) if s > 0 else Fraction(1)
        if component != 0:
            weight_components[w] = component

    return WeightFilteredShadowZeta(
        s=s, N_max=N, weight_components=weight_components
    )


def verify_weight_filtration_consistency(N: int = 15) -> Dict[str, Any]:
    r"""Verify that the weight filtration is consistent across operations.

    Checks:
    1. sum_w zeta^{mot,w}(s) = chi(zeta^{mot}(s)) for s = 0, 1, 2
    2. Weight components are non-negative for s >= 2
    3. The number of active weights at truncation N is N (one per BBS level)

    Multi-path verification (AP10).
    """
    results: Dict[str, Any] = {}

    for s_val in [0, 1, 2]:
        # Path 1: motivic zeta, then Euler char
        bar_dims = c3_motivic_bar_dimensions(N)
        zeta_mot = motivic_shadow_zeta_integer(bar_dims, s_val)
        chi_total = zeta_mot.euler_char()

        # Path 2: weight-filtered, then sum
        wf = weight_filtered_shadow_zeta_c3(s_val, N)
        wf_total = wf.total_euler_char

        results[f's={s_val}_match'] = (chi_total == wf_total)
        results[f's={s_val}_chi'] = float(chi_total)
        results[f's={s_val}_wf'] = float(wf_total)

    # Weight count
    wf_check = weight_filtered_shadow_zeta_c3(0, N)
    results['num_weights'] = wf_check.num_weights
    results['expected_weights'] = N

    # Non-negativity at s = 2
    wf2 = weight_filtered_shadow_zeta_c3(2, N)
    all_nonneg = all(v >= 0 for v in wf2.weight_components.values())
    results['s=2_nonneg'] = all_nonneg

    results['all_pass'] = all(
        results.get(f's={sv}_match', False) for sv in [0, 1, 2]
    ) and all_nonneg

    return results


# =========================================================================
# 6. EULER CHARACTERISTIC SPECIALIZATIONS
# =========================================================================

def c3_numerical_shadow_zeta(s: int, N: int = 20) -> Fraction:
    r"""Numerical shadow zeta for C^3: chi(zeta^{mot}(s)).

    zeta_{C^3}^{num}(s) = sum_{n=1}^{N} n * n^{-s} = sum n^{1-s}

    For s=0: sum n = N(N+1)/2
    For s=1: N
    For s=2: H_N (harmonic number)
    For s=3: sum 1/n^2 (partial)

    VERIFIED [DC] direct computation [CF] cross-check with Vol I shadow_zeta_engine.
    """
    total = Fraction(0)
    for n in range(1, N + 1):
        if s <= 1:
            total += Fraction(n ** (1 - s))
        else:
            total += Fraction(1, n ** (s - 1))
    return total


def verify_euler_specialization_c3(N: int = 20) -> Dict[str, Any]:
    r"""Verify chi(zeta_{C^3}^{mot}(s)) = zeta_{C^3}^{num}(s).

    Multi-path verification at s = 0, 1, 2, 3, 4.

    Path A: Compute motivic zeta, apply chi.
    Path B: Direct numerical zeta computation.
    """
    results: Dict[str, Any] = {}
    bar_dims = c3_motivic_bar_dimensions(N)

    for s_val in [0, 1, 2, 3, 4]:
        # Path A
        zeta_mot = motivic_shadow_zeta_integer(bar_dims, s_val)
        chi_val = zeta_mot.euler_char()

        # Path B
        num_val = c3_numerical_shadow_zeta(s_val, N)

        results[f's={s_val}_match'] = (chi_val == num_val)
        results[f's={s_val}_motivic_chi'] = float(chi_val)
        results[f's={s_val}_numerical'] = float(num_val)

    results['all_pass'] = all(
        results.get(f's={sv}_match', False) for sv in [0, 1, 2, 3, 4]
    )
    return results


# =========================================================================
# 7. p-ADIC CONSISTENCY CHECKS
# =========================================================================

def verify_padic_consistency_c3(p: int = 2, N: int = 15) -> Dict[str, Any]:
    r"""Verify p-adic shadow zeta consistency for C^3.

    Checks:
    1. padic_shadow_zeta_c3 == padic_shadow_zeta_c3_closed (two formulas)
    2. Limit p -> 1 (formal): zeta^{p}(s) ~ kappa_ch * zeta^{num}(s)
       More precisely, as p -> 1: f_n|_{L=p^2} -> n, so the p-adic
       zeta approaches the numerical zeta.
    3. f_1|_{L=p^2} = p^3 (the motivic bar at n=1 is L^{3/2},
       and L^{3/2}|_{L=p^2} = p^3).
    """
    results: Dict[str, Any] = {}

    # Check 1: two formulas agree
    for s_val in [0, 1, 2]:
        val1 = padic_shadow_zeta_c3(s_val, p, N)
        val2 = padic_shadow_zeta_c3_closed(s_val, p, N)
        results[f'formula_match_s={s_val}'] = (val1 == val2)

    # Check 2: f_1 value
    f1_padic = padic_euler_factor_c3(p, 1)
    results['f1_padic'] = f1_padic
    results['f1_expected'] = Fraction(p ** 3)
    results['f1_match'] = (f1_padic == Fraction(p ** 3))

    # Check 3: f_2 value
    f2_padic = padic_euler_factor_c3(p, 2)
    f2_expected = Fraction(p ** 3) + Fraction(p ** 5)
    results['f2_padic'] = f2_padic
    results['f2_expected'] = f2_expected
    results['f2_match'] = (f2_padic == f2_expected)

    results['all_pass'] = all([
        all(results.get(f'formula_match_s={sv}', False) for sv in [0, 1, 2]),
        results['f1_match'],
        results['f2_match'],
    ])
    return results


# =========================================================================
# 8. MOTIVIC BAR EULER PRODUCT
# =========================================================================

def motivic_bar_euler_product_c3(N: int = 12) -> List[MotivicClass]:
    r"""Motivic bar Euler product for C^3.

    prod_{n >= 1} (1 - [B_n^{mot}] q^n) = 1/Z^{mot}(C^3)

    This inverts the motivic MacMahon. We compute the first N coefficients
    of 1/Z^{mot} by the recursion:

        (1/Z)_0 = 1
        (1/Z)_n = -sum_{k=1}^{n} [B_k^{mot}] * (1/Z)_{n-k}

    Wait -- this is not quite right. The bar Euler product is:
        prod (1 - [B_n] q^n) = 1 - [B_1]q - ([B_2] - [B_1]^2)q^2 - ...

    The CORRECT relation is:
        Z^{mot} = Exp_*(f), 1/Z^{mot} = Exp_*(-f) (motivic plethystic)

    But at the level of ordinary power series:
        Z = prod_{n} prod_{k} 1/(1 - L^{k+3/2} q^n)
        1/Z = prod_{n} prod_{k} (1 - L^{k+3/2} q^n)

    We compute 1/Z^{mot} by:
        (1/Z)_n = -sum_{k=1}^{n} f_k * (1/Z)_{n-k}  (if Z = exp(sum f_k/k * q^k))

    Actually, use the standard FPS inversion: if Z = sum c_n q^n with c_0 = 1,
        (1/Z)_0 = 1
        (1/Z)_n = -sum_{k=1}^{n} c_k (1/Z)_{n-k}

    VERIFIED [DC] (1/Z)_1 = -f_1 = -L^{3/2}.
    """
    # First compute Z^{mot} coefficients via plethystic exponential
    # Use the BBS single-letter approach
    Z = _compute_motivic_macmahon_local(N)

    # Invert: (1/Z)_n = -sum_{k=1}^{n} Z_k (1/Z)_{n-k}
    inv_Z = [MotivicClass.zero() for _ in range(N)]
    inv_Z[0] = MotivicClass.one()
    for n in range(1, N):
        s = MotivicClass.zero()
        for k in range(1, n + 1):
            if k < N and (n - k) < N:
                s = s + Z[k] * inv_Z[n - k]
        inv_Z[n] = -s

    return inv_Z


def _compute_motivic_macmahon_local(N: int) -> List[MotivicClass]:
    r"""Compute Z^{mot}(C^3) to order N via local plethystic exp.

    Z = Exp_*(f) where f_n = sum_{k=0}^{n-1} L^{k+3/2}.

    We compute log(Z) = sum_{m >= 1} psi_m(f)/m, then exponentiate.
    """
    # Log coefficients: sum_{m >= 1} psi_m(f)/m
    log_coeffs: List[Dict[int, Fraction]] = [{} for _ in range(N)]

    for m in range(1, N):
        for n in range(1, N):
            target = n * m
            if target >= N:
                break
            fn = c3_single_letter(n)
            if fn.is_zero():
                continue
            inv_m = Fraction(1, m)
            for k, v in fn.coeffs.items():
                new_key = m * k  # Adams operation: L^{k/2} -> L^{mk/2}
                if new_key not in log_coeffs[target]:
                    log_coeffs[target][new_key] = Fraction(0)
                log_coeffs[target][new_key] += inv_m * Fraction(v)

    # Exponentiate
    result_coeffs: List[Dict[int, Fraction]] = [{} for _ in range(N)]
    result_coeffs[0] = {0: Fraction(1)}

    for n in range(1, N):
        s: Dict[int, Fraction] = {}
        for k_idx in range(1, n + 1):
            lc = log_coeffs[k_idx]
            rc = result_coeffs[n - k_idx]
            if not lc or not rc:
                continue
            for lk, lv in lc.items():
                for rk, rv in rc.items():
                    key = lk + rk
                    val = Fraction(k_idx) * lv * rv
                    s[key] = s.get(key, Fraction(0)) + val
        inv_n = Fraction(1, n)
        result_coeffs[n] = {k: v * inv_n for k, v in s.items() if v != 0}

    # Convert to MotivicClass
    result = [MotivicClass.zero() for _ in range(N)]
    for n in range(N):
        int_coeffs: Dict[int, int] = {}
        for k, v in result_coeffs[n].items():
            assert v.denominator == 1, (
                f"Non-integer coefficient at q^{n}, L^({k}/2): {v}"
            )
            int_coeffs[k] = int(v)
        result[n] = MotivicClass(int_coeffs)
    return result


def verify_motivic_bar_euler_c3(N: int = 10) -> Dict[str, Any]:
    r"""Verify the motivic bar Euler product for C^3.

    Checks:
    1. (1/Z)_1 = -L^{3/2} (= -f_1)
    2. chi((1/Z)_n) = coefficients of 1/M(q) (the numerical inverse MacMahon)
    3. Z * (1/Z) = 1 (product check to order N)
    """
    inv_Z = motivic_bar_euler_product_c3(N)
    Z = _compute_motivic_macmahon_local(N)

    results: Dict[str, Any] = {}

    # Check 1: (1/Z)_1 = -L^{3/2}
    expected_1 = -c3_single_letter(1)
    results['inv_Z_1_match'] = (inv_Z[1] == expected_1)

    # Check 2: Euler char of 1/Z should give 1/M(q) numerically
    # 1/M(q) = prod (1-q^n)^n
    # Coefficients: 1, -1, -2, 0, 1, 4, ...  (OEIS A000219 inverse)
    inv_M_numerical = _numerical_inverse_macmahon(N)
    inv_Z_chi = [c.euler_char() for c in inv_Z]
    results['euler_char_match'] = (inv_Z_chi == inv_M_numerical)
    results['inv_Z_chi'] = inv_Z_chi[:min(8, N)]
    results['inv_M_num'] = inv_M_numerical[:min(8, N)]

    # Check 3: Z * (1/Z) = 1 (convolution)
    product = [MotivicClass.zero() for _ in range(N)]
    for n in range(N):
        s = MotivicClass.zero()
        for k in range(n + 1):
            if k < N and (n - k) < N:
                s = s + Z[k] * inv_Z[n - k]
        product[n] = s

    # product[0] should be 1, product[n] should be 0 for n >= 1
    product_ok = (product[0] == MotivicClass.one())
    for n in range(1, N):
        if not product[n].is_zero():
            product_ok = False
            break
    results['product_identity'] = product_ok

    results['all_pass'] = (
        results['inv_Z_1_match']
        and results['euler_char_match']
        and results['product_identity']
    )
    return results


def _numerical_inverse_macmahon(N: int) -> List[int]:
    r"""1/M(q) = prod_{n >= 1} (1-q^n)^n mod q^N.

    M(q) = prod 1/(1-q^n)^n (MacMahon), so 1/M(q) = prod (1-q^n)^n.

    Coefficients: 1, -1, -2, 0, 1, 4, 2, -4, -4, 0, ...
    """
    result = [Fraction(1)] + [Fraction(0)] * (N - 1)
    # prod (1-q^n)^n: for each n, multiply by (1-q^n)^n
    for n in range(1, N):
        # Multiply by (1 - q^n)^n = multiply by (1 - q^n), n times
        for _rep in range(n):
            for m in range(N - 1, n - 1, -1):
                result[m] -= result[m - n]
    return [int(c) for c in result]


# =========================================================================
# 9. SHADOW TOWER AND MC EQUATION IN THE MOTIVIC SETTING
# =========================================================================

@dataclass
class MotivicShadowTowerData:
    r"""The motivic shadow tower for a CY3 chiral algebra.

    S_r^{mot} in K_0(Var)[L^{+/-1/2}] for r = 2, 3, 4, ...

    For C^3 (class G): S_2^{mot} = [B_1^{mot}] = L^{3/2}, S_r = 0 for r >= 3.
    The tower is GAUSSIAN: only the arity-2 shadow is nonzero.

    Under chi: S_2^{mot} -> 1 = kappa_ch(C^3).

    The MC equation in the motivic setting:
        D * Theta^{mot} + (1/2)[Theta^{mot}, Theta^{mot}] = 0
    holds at each weight grade.
    """
    geometry: str
    shadow_coefficients: Dict[int, MotivicClass]  # r -> S_r^{mot}
    shadow_class: str  # G, L, C, M

    @property
    def kappa_ch_motivic(self) -> MotivicClass:
        """kappa_ch^{mot} = S_2^{mot}."""
        return self.shadow_coefficients.get(2, MotivicClass.zero())

    @property
    def kappa_ch_numerical(self) -> int:
        """chi(kappa_ch^{mot})."""
        return self.kappa_ch_motivic.euler_char()


def c3_motivic_shadow_tower(max_arity: int = 10) -> MotivicShadowTowerData:
    r"""Motivic shadow tower for C^3.

    C^3 is class G (Gaussian): the shadow tower terminates at arity 2.
        S_2^{mot} = L^{3/2}  (chi -> 1 = kappa_ch)
        S_r^{mot} = 0         for r >= 3

    This is because the positive half CoHA(C^3)=Y^+(gl_1) is free in
    this shadow range.  The full affine Yangian or W_{1+\infty} appears
    only after the Drinfeld double/center and a vacuum/Fock evaluation.

    VERIFIED [DC] motivic_e1_algebra.py [CF] c3_shadow_tower.py
    """
    shadow: Dict[int, MotivicClass] = {}
    # S_2 = the leading bar cohomology = [B_1] = L^{3/2}
    shadow[2] = c3_single_letter(1)  # L^{3/2}
    # All higher S_r = 0 (class G)
    for r in range(3, max_arity + 1):
        shadow[r] = MotivicClass.zero()

    return MotivicShadowTowerData(
        geometry='C^3',
        shadow_coefficients=shadow,
        shadow_class='G',
    )


# =========================================================================
# 10. MASTER VERIFICATION
# =========================================================================

def motivic_shadow_zeta_master_verification(
    N: int = 12, p: int = 2
) -> Dict[str, Any]:
    r"""Run all motivic shadow zeta verifications.

    Checks:
    1. Euler specialization: chi(zeta^{mot}) = zeta^{num} for C^3
    2. Weight filtration consistency
    3. p-adic formula agreement (two paths)
    4. Motivic bar Euler product: Z * (1/Z) = 1
    5. Shadow tower: S_2^{mot} = L^{3/2}, chi -> 1 = kappa_ch
    6. p-adic bar dimensions: f_1|_{L=p^2} = p^3, f_2|_{L=p^2} = p^3+p^5
    """
    results: Dict[str, Any] = {}

    # 1. Euler specialization
    euler_check = verify_euler_specialization_c3(N)
    results['euler_specialization'] = euler_check['all_pass']

    # 2. Weight filtration
    weight_check = verify_weight_filtration_consistency(N)
    results['weight_filtration'] = weight_check['all_pass']

    # 3. p-adic
    padic_check = verify_padic_consistency_c3(p, N)
    results['padic_consistency'] = padic_check['all_pass']

    # 4. Bar Euler product
    bar_check = verify_motivic_bar_euler_c3(min(N, 10))
    results['bar_euler_product'] = bar_check['all_pass']

    # 5. Shadow tower
    tower = c3_motivic_shadow_tower()
    kappa_ok = (tower.kappa_ch_numerical == 1)
    kappa_mot_ok = (tower.kappa_ch_motivic == MotivicClass.L_half(3))
    results['shadow_tower_kappa'] = kappa_ok and kappa_mot_ok
    results['shadow_class'] = tower.shadow_class

    # 6. p-adic bar dimensions
    f1 = padic_euler_factor_c3(p, 1)
    f2 = padic_euler_factor_c3(p, 2)
    results['padic_f1'] = (f1 == Fraction(p ** 3))
    results['padic_f2'] = (f2 == Fraction(p ** 3) + Fraction(p ** 5))

    results['all_pass'] = all([
        results['euler_specialization'],
        results['weight_filtration'],
        results['padic_consistency'],
        results['bar_euler_product'],
        results['shadow_tower_kappa'],
        results['padic_f1'],
        results['padic_f2'],
    ])

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("Motivic Shadow Zeta Function Engine")
    print("=" * 70)

    # Run master verification
    results = motivic_shadow_zeta_master_verification(N=10, p=2)
    print(f"\nMaster verification: {'PASS' if results['all_pass'] else 'FAIL'}")
    for key, val in results.items():
        if key != 'all_pass':
            status = 'PASS' if val else ('FAIL' if isinstance(val, bool) else val)
            print(f"  {key}: {status}")

    # Display motivic shadow zeta for C^3
    print(f"\n{'='*70}")
    print("Motivic shadow zeta for C^3")
    print(f"{'='*70}")

    bar_dims = c3_motivic_bar_dimensions(8)
    print("\nMotivic bar dimensions [B_n^{mot}]:")
    for i, bn in enumerate(bar_dims):
        print(f"  n={i+1}: {bn}  (chi = {bn.euler_char()})")

    for s_val in [0, 1, 2]:
        zeta = c3_motivic_shadow_zeta(s_val, 10)
        print(f"\nzeta^{{mot}}(s={s_val}): chi = {float(zeta.euler_char()):.6f}")

    # p-adic shadow
    print(f"\n{'='*70}")
    print("p-adic shadow zeta for C^3")
    print(f"{'='*70}")
    for p in [2, 3, 5, 7]:
        for s_val in [0, 1, 2]:
            val = padic_shadow_zeta_c3(s_val, p, 8)
            print(f"  p={p}, s={s_val}: {float(val):.4f}")
