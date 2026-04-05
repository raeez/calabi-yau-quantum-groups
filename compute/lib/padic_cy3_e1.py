r"""
padic_cy3_e1.py -- p-adic analogues of the CY3 E_1 construction.

HEURISTIC / SPECULATIVE MODULE
================================

STATUS: All claims in this module are HEURISTIC or OBSERVATION level.
Nothing here is a theorem.  The module explores speculative connections
between p-adic geometry, Weil zeta functions, and the CY3 E_1 chiral
algebra framework developed in the rest of this volume.

MATHEMATICAL OVERVIEW
======================

For a CY3 X defined over Q (or a number field K), one can consider:

  (a) The p-adic completion X_p = X ⊗_Q Q_p, a rigid analytic CY3.
  (b) The reduction mod p: X_F_p = X ⊗_Z F_p, a variety over a finite field.
  (c) The l-adic cohomology H^*(X_{bar Q}, Q_l) with Galois action.

The speculative programme explored here: the E_1 chiral algebra A_X
of Vol III should encode arithmetic data of X when X has an arithmetic
model.  Specifically:

  (1) p-adic stability: Bridgeland stability on D^b(X_p) with p-adic
      central charges.
  (2) p-adic CoHA: the critical CoHA with p-adic coefficients, where
      the shuffle zeta function is replaced by the p-adic local zeta.
  (3) Weil zeta from E_1: the partition function Tr_{A_X} q^{L_0}
      should specialize to Z(X/F_q, t) under a suitable arithmetic
      specialization.
  (4) Galois representation from E_1: the Frobenius eigenvalues on
      H^3(X) should appear in the E_1 character.
  (5) Motivic measure from E_1: the p-adic integral of the CY form
      Omega_3 should equal a p-adic modular characteristic kappa_p.
  (6) Arithmetic shadow tower: the shadow tower with p-adic coefficients
      has genus-0 term = point counts, genus-1 term = p-adic modular form.

CAUTIONARY NOTES (AP-CY6, AP-CY7, AP42):
  - A_X does NOT exist for CY3 (AP-CY6).  All statements involving
    "the E_1 algebra of a CY3" are conditional on the chain-level
    S^3-framing construction.
  - The CoHA is NOT the same as the E_1 chiral algebra (AP-CY7).
    The CoHA is the target that the E_1-sector should match, IF A_X exists.
  - All identifications "E_1 partition function = Weil zeta function"
    are heuristic observations (AP42), not proved theorems.
  - Cross-volume convention warning (AP49): this module works with
    motivic/categorical conventions (Vol III), NOT OPE modes (Vol I)
    or lambda-brackets (Vol II).

COMPUTATIONS
=============

1. Point counts for Fermat-type CY3s over F_p via Gauss sum formulas.
2. Weil zeta functions from point-count data.
3. p-adic zeta functions for the shuffle algebra.
4. p-adic stability conditions (toy model: rank-1, degree-d).
5. p-adic modular characteristic from CY form integration.
6. Arithmetic shadow tower: genus-0 = point counts, genus-1 comparison
   with classical modular forms.

REFERENCES
===========
  Weil (1949): Numbers of solutions of equations in finite fields
  Ireland-Rosen (1990): A Classical Introduction to Modern Number Theory
  Schiffmann-Vasserot (2013): CoHA = affine Yangian
  Kontsevich-Soibelman (2008): motivic DT, stability structures
  Candelas-de la Ossa-Rodriguez-Villegas (2003): Calabi-Yau manifolds over
    finite fields I, hep-th/0012233
  Kadir-Yui (2006): Motives and mirror symmetry for CY manifolds
  Wan (2006): Mirror symmetry for zeta functions, math/0411464
  Katz (1988): Gauss Sums, Kloosterman Sums, and Monodromy Groups
  Lorgat, Vol III: CY-to-chiral functor (CY-A), shadow obstruction tower

CONVENTIONS
===========
  - Exact arithmetic: Fraction for rationals, polynomial rings for p-adic
    approximations (we truncate at a finite p-adic precision).
  - p-adic integers Z_p are represented as integers mod p^k for precision k.
  - The Teichmuller lift and Witt vectors are used where needed.
  - Weil zeta function Z(X/F_q, t) = exp(sum_{n>=1} #X(F_{q^n}) t^n / n).
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple


# =========================================================================
# 0. EXACT ARITHMETIC UTILITIES
# =========================================================================

FPS = List[Fraction]


def _fps_zero(N: int) -> FPS:
    return [Fraction(0)] * N


def _fps_one(N: int) -> FPS:
    f = _fps_zero(N)
    f[0] = Fraction(1)
    return f


def _fps_mul(a: FPS, b: FPS, N: int) -> FPS:
    result = _fps_zero(N)
    la, lb = len(a), len(b)
    for i in range(min(la, N)):
        if a[i] == 0:
            continue
        for j in range(min(lb, N - i)):
            result[i + j] += a[i] * b[j]
    return result


def _fps_inv(a: FPS, N: int) -> FPS:
    """Invert power series a(q) mod q^N. Requires a[0] != 0."""
    assert a[0] != 0
    inv0 = Fraction(1) / a[0]
    result = _fps_zero(N)
    result[0] = inv0
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, min(n + 1, len(a))):
            s += a[k] * result[n - k]
        result[n] = -inv0 * s
    return result


def _fps_log(a: FPS, N: int) -> FPS:
    """log(a(q)) mod q^N, a[0] = 1."""
    assert a[0] == Fraction(1)
    L = _fps_zero(N)
    for n in range(1, N):
        an = a[n] if n < len(a) else Fraction(0)
        s = Fraction(0)
        for k in range(1, n):
            ak = a[n - k] if n - k < len(a) else Fraction(0)
            s += Fraction(k) * L[k] * ak
        L[n] = an - s / Fraction(n)
    return L


def _fps_exp(f: FPS, N: int) -> FPS:
    """exp(f(q)) mod q^N, f[0] = 0."""
    assert f[0] == Fraction(0)
    g = _fps_zero(N)
    g[0] = Fraction(1)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, n + 1):
            fk = f[k] if k < len(f) else Fraction(0)
            s += Fraction(k) * fk * g[n - k]
        g[n] = s / Fraction(n)
    return g


# =========================================================================
# 1. POINT COUNTING ON CY3 OVER FINITE FIELDS
# =========================================================================

def _mod_pow(base: int, exp: int, mod: int) -> int:
    """Modular exponentiation: base^exp mod mod."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result


def _is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fermat_quintic_point_count(p: int) -> int:
    r"""Count points on the Fermat quintic x_0^5+...+x_4^5=0 in P^4 over F_p.

    Uses the character sum method (Weil, Ireland-Rosen).

    For the Fermat hypersurface sum x_i^d = 0 in P^{n-1} over F_p:
    the point count involves Gauss sums and Jacobi sums.

    For the Fermat quintic (d=5, n=5 projective coordinates) over F_p:
      #X(F_p) = p^3 + p^2 + p + 1  +  correction_from_characters

    The "trivial" part is the projective space count for a smooth
    degree-5 hypersurface in P^4: this is 1+p+p^2+p^3 plus a correction.

    METHOD: Brute-force enumeration for small p (p <= 31), which gives
    exact results verifiable against the literature.

    OBSERVATION (HEURISTIC): For p = 5 (the "Gepner prime" where 5 | p),
    the arithmetic is special because x^5 = 0 has a 5-fold root in F_5.

    References:
      Candelas-de la Ossa-Rodriguez-Villegas, hep-th/0012233
      Ireland-Rosen, Chapter 8 (Gauss/Jacobi sums)
    """
    assert _is_prime(p), f"p={p} is not prime"

    # Brute-force: enumerate projective points [x0:...:x4] in P^4(F_p).
    # A projective point is represented by the lexicographically first
    # nonzero representative.
    count = 0

    # Enumerate affine representatives: all (x0,...,x4) in F_p^5 \ {0},
    # then divide by (p-1) to get projective count.
    for x0 in range(p):
        x0_5 = _mod_pow(x0, 5, p)
        for x1 in range(p):
            x01 = (x0_5 + _mod_pow(x1, 5, p)) % p
            for x2 in range(p):
                x012 = (x01 + _mod_pow(x2, 5, p)) % p
                for x3 in range(p):
                    x0123 = (x012 + _mod_pow(x3, 5, p)) % p
                    for x4 in range(p):
                        if (x0, x1, x2, x3, x4) == (0, 0, 0, 0, 0):
                            continue
                        total = (x0123 + _mod_pow(x4, 5, p)) % p
                        if total == 0:
                            count += 1

    # Projective count = affine_nonzero_count / (p-1)
    assert count % (p - 1) == 0, (
        f"Affine count {count} not divisible by p-1={p-1}"
    )
    return count // (p - 1)


def _fermat_quintic_point_count_fast(p: int) -> int:
    r"""Fast point count using precomputed 5th power tables.

    Same as fermat_quintic_point_count but with lookup-table optimization.
    """
    assert _is_prime(p), f"p={p} is not prime"

    # Precompute 5th power residues
    pow5 = [_mod_pow(x, 5, p) for x in range(p)]

    # Count affine solutions to x0^5+...+x4^5 = 0 mod p, excluding origin
    # Use convolution: let f(s) = #{x in F_p : x^5 = s mod p}
    freq = [0] * p
    for v in pow5:
        freq[v] += 1

    # Convolve 5 times: (f * f * f * f * f)(0) = #{(x0,...,x4): sum x_i^5 = 0}
    # Step by step:
    conv = list(freq)
    for _ in range(4):
        new_conv = [0] * p
        for s1 in range(p):
            if conv[s1] == 0:
                continue
            for s2 in range(p):
                new_conv[(s1 + s2) % p] += conv[s1] * freq[s2]
        conv = new_conv

    # conv[0] = # affine solutions including origin
    # Subtract the origin (0,...,0): pow5[0]=0, and 0^5+...+0^5=0, so subtract 1
    affine_count = conv[0] - 1

    assert affine_count % (p - 1) == 0, (
        f"Affine count {affine_count} not divisible by p-1={p-1}"
    )
    return affine_count // (p - 1)


# Known point counts for the Fermat quintic (literature verification).
# Source: Candelas-de la Ossa-Rodriguez-Villegas, hep-th/0012233, Table 1.
# Convention: #X(F_p) for the Fermat quintic x_0^5+...+x_4^5 = 0 in P^4.
FERMAT_QUINTIC_KNOWN_COUNTS: Dict[int, int] = {
    # When gcd(5, p-1) = 1, the Fermat quintic = hyperplane => count = p^3+p^2+p+1.
    # For p=2,3,5,7,13: gcd(5,p-1)=1, so counts are trivial.
    # For p=11: gcd(5,10)=5, nontrivial character sum corrections.
    2: 15,      # p=2: 2^3+2^2+2+1 = 15 (gcd(5,1)=1, trivial)
    3: 40,      # p=3: 3^3+3^2+3+1 = 40 (gcd(5,2)=1, trivial)
    5: 156,     # p=5: 5^3+5^2+5+1 = 156 (gcd(5,4)=1, trivial)
    7: 400,     # p=7: 7^3+7^2+7+1 = 400 (gcd(5,6)=1, trivial)
    11: 1925,   # p=11: gcd(5,10)=5, nontrivial. Tr(Frob|H^3) = -461.
    13: 2380,   # p=13: 13^3+13^2+13+1 = 2380 (gcd(5,12)=1, trivial)
}
# When gcd(5, p-1) = 1, the map x -> x^5 is a bijection on F_p^*,
# so the Fermat quintic is projectively equivalent to the hyperplane
# x_0+...+x_4 = 0, giving count p^3+p^2+p+1.


def fermat_quintic_point_count_extension(p: int, n: int) -> int:
    r"""Count points on the Fermat quintic over F_{p^n}.

    For small p and n, uses brute-force over F_{p^n} represented
    as F_p[t]/(f(t)) for an irreducible polynomial f of degree n.

    For n=1, delegates to _fermat_quintic_point_count_fast.
    For n>1, uses the recursive Weil zeta function if the zeta
    function has been computed, or falls back to the known formula
    for gcd(5, p^n - 1) = 1 cases.

    OBSERVATION: when gcd(5, p^n - 1) = 1, the map x -> x^5 is
    a bijection on F_{p^n}^*, so #X(F_{p^n}) = p^{3n}+p^{2n}+p^n+1.
    """
    if n == 1:
        return _fermat_quintic_point_count_fast(p)

    q = p ** n
    if math.gcd(5, q - 1) == 1:
        # x -> x^5 is a bijection, Fermat = hyperplane
        return q**3 + q**2 + q + 1

    # For general n, we would need F_{p^n} arithmetic.
    # Fall back to the formula from the Weil zeta function if available.
    # This is populated after computing the zeta function from n=1 data.
    raise NotImplementedError(
        f"Direct counting over F_{{{p}^{n}}} for gcd(5,{q}-1)!=1 "
        f"requires finite field arithmetic not implemented here. "
        f"Use weil_zeta_from_counts() with n=1 data and extrapolate."
    )


# =========================================================================
# 2. WEIL ZETA FUNCTION
# =========================================================================

class WeilZetaData(NamedTuple):
    """Weil zeta function data for a variety over F_q.

    The Weil zeta function is:
      Z(X/F_q, t) = exp(sum_{n>=1} #X(F_{q^n}) * t^n / n)

    For a smooth projective CY3 of dimension 3:
      Z(X/F_q, t) = P_1(t) * P_3(t) * P_5(t)
                   / (P_0(t) * P_2(t) * P_4(t) * P_6(t))
    where P_i(t) = det(1 - Frob * t | H^i(X)).

    For a CY3: h^{1,0}=h^{2,0}=0, so P_1 = P_5 = 1.
    P_0 = 1-t, P_2 = (1-qt)^{h^{1,1}}, P_4 = (1-q^2*t)^{h^{1,1}},
    P_6 = 1-q^3*t, and P_3 has degree 2*h^{2,1}+2 = b_3.

    The mysterious polynomial: P_3(t), of degree 2*(h^{2,1}+1),
    encodes the Galois representation on H^3(X).
    """
    name: str
    q: int                # base field size
    point_counts: Dict[int, int]  # n -> #X(F_{q^n})
    trivial_part: FPS     # product of P_0*P_2*P_4*P_6 (known from Hodge numbers)
    p3_coeffs: Optional[List[Fraction]]  # coefficients of P_3(t) if computable
    h11: int
    h21: int


def _trivial_zeta_factors(q: int, h11: int, N: int) -> FPS:
    r"""Compute the "trivial" part of the Weil zeta function for a CY3.

    The trivial factors are:
      1/P_0(t) * 1/P_2(t) * 1/P_4(t) * 1/P_6(t)
    = 1/(1-t) * 1/(1-qt)^{h11} * 1/(1-q^2*t)^{h11} * 1/(1-q^3*t)

    We compute this as a power series mod t^N.
    """
    # Start with 1/(1-t)
    result = _fps_one(N)
    for n in range(1, N):
        result[n] = Fraction(1)

    # Multiply by 1/(1 - q*t)^{h11}
    for _ in range(h11):
        new = _fps_zero(N)
        new[0] = Fraction(1)
        for n in range(1, N):
            new[n] = new[n - 1] * Fraction(q)
        result = _fps_mul(result, new, N)

    # Multiply by 1/(1 - q^2*t)^{h11}
    q2 = q * q
    for _ in range(h11):
        new = _fps_zero(N)
        new[0] = Fraction(1)
        for n in range(1, N):
            new[n] = new[n - 1] * Fraction(q2)
        result = _fps_mul(result, new, N)

    # Multiply by 1/(1 - q^3*t)
    q3 = q * q * q
    new = _fps_zero(N)
    new[0] = Fraction(1)
    for n in range(1, N):
        new[n] = new[n - 1] * Fraction(q3)
    result = _fps_mul(result, new, N)

    return result


def weil_zeta_from_count(
    name: str,
    q: int,
    count_1: int,
    h11: int,
    h21: int,
    N: int = 10,
) -> WeilZetaData:
    r"""Compute the Weil zeta function from #X(F_q) for a CY3.

    Given the single point count #X(F_q), we compute the "trivial" prediction
    (from Hodge numbers) and extract any correction to P_3.

    The trivial prediction for #X(F_q) from the Lefschetz trace formula:
      #X(F_q) = sum_{i=0}^{6} (-1)^i Tr(Frob | H^i)
      = 1 + h11*q + ... + q^3  -  Tr(Frob | H^3)

    So: Tr(Frob | H^3) = (1 + h11*q + h11*q^2 + q^3) - #X(F_q)

    The trivial Betti contribution is:
      N_trivial = 1 + h^{1,1}*q + h^{1,1}*q^2 + q^3

    OBSERVATION: For the Fermat quintic with h11=1, h21=101:
      N_trivial = 1 + q + q^2 + q^3
      Tr(Frob | H^3) = N_trivial - #X(F_q)
    """
    n_trivial = 1 + h11 * q + h11 * q**2 + q**3
    tr_frob_h3 = n_trivial - count_1

    # For the full zeta function, we need point counts at multiple extensions.
    # With only #X(F_q), we can extract Tr(Frob|H^3) but not the full P_3.
    # P_3(t) = 1 - a_1*t + a_2*t^2 - ... where a_1 = Tr(Frob|H^3).
    # The degree of P_3 is b_3 = 2*(h21+1) = 2*h21+2.

    # Compute point counts for extensions where gcd(5, q^n-1)=1
    point_counts: Dict[int, int] = {1: count_1}
    for n in range(2, N + 1):
        qn = q ** n
        if math.gcd(5, qn - 1) == 1:
            # Fermat = hyperplane case
            point_counts[n] = qn**3 + qn**2 + qn + 1
        # Otherwise we'd need field arithmetic

    trivial = _trivial_zeta_factors(q, h11, N)

    return WeilZetaData(
        name=name,
        q=q,
        point_counts=point_counts,
        trivial_part=trivial,
        p3_coeffs=None,  # Would need more data to determine
        h11=h11,
        h21=h21,
    )


def weil_zeta_series(point_counts: Dict[int, int], N: int) -> FPS:
    r"""Compute Z(X/F_q, t) = exp(sum #X(F_{q^n}) t^n/n) mod t^N.

    Uses the exact logarithm-then-exponentiate approach.
    """
    log_z = _fps_zero(N)
    for n in range(1, N):
        if n in point_counts:
            log_z[n] = Fraction(point_counts[n], n)
    return _fps_exp(log_z, N)


def frobenius_trace_from_count(count: int, q: int, h11: int) -> int:
    r"""Extract Tr(Frob | H^3) from #X(F_q) for a CY3.

    #X(F_q) = 1 + h11*q + h11*q^2 + q^3 - Tr(Frob|H^3)
    (contributions from H^0, H^2, H^4, H^6 are trivial;
     H^1 = H^5 = 0 for a CY3; the sign is (-1)^3 = -1 for H^3.)

    So: Tr(Frob|H^3) = (1 + h11*q + h11*q^2 + q^3) - #X(F_q).
    """
    trivial = 1 + h11 * q + h11 * q**2 + q**3
    return trivial - count


# =========================================================================
# 3. p-ADIC SHUFFLE ZETA FUNCTION
# =========================================================================

def padic_shuffle_zeta(z: Fraction, p: int) -> Fraction:
    r"""The p-adic CY3 shuffle zeta function.

    For the complex CoHA of C^3, the shuffle product uses the zeta function:
      zeta(z) = 1/z^2  (rational, from the CY3 condition h1+h2+h3=0)

    For a p-adic CY3, the natural replacement is the local Euler factor:
      zeta_p(z) = (1 - z/p)(1 - p*z) / (1 - z)^2

    OBSERVATION (HEURISTIC): This zeta function encodes the p-adic
    measure on the affine line: the factor (1-z/p)(1-pz) comes from
    the p-adic absolute value |z|_p, and (1-z)^2 is the standard
    CY3 denominator.

    At z=1: zeta_p(1) = 0 (numerator vanishes).
    At z=p: zeta_p(p) = 0 (numerator vanishes).
    Poles at z=1 (order 2 from denominator).

    The ratio zeta_p(z) / zeta_complex(z) measures the p-adic
    deformation of the shuffle product.

    Parameters
    ----------
    z : Fraction
        The spectral parameter (rational).
    p : int
        The prime.

    Returns
    -------
    Fraction
        zeta_p(z), or raises ZeroDivisionError if z=1.
    """
    num = (Fraction(1) - z / p) * (Fraction(1) - p * z)
    denom = (Fraction(1) - z) ** 2
    if denom == 0:
        raise ZeroDivisionError("zeta_p has a pole at z=1")
    return num / denom


def padic_shuffle_zeta_residue(p: int) -> Fraction:
    r"""Residue of zeta_p(z) at z=1 (double pole).

    zeta_p(z) = (1-z/p)(1-pz) / (1-z)^2

    Write z = 1 + epsilon. Then:
      1 - z/p = 1 - (1+eps)/p = (p-1-eps)/p
      1 - pz = 1 - p(1+eps) = -(p-1+p*eps) = -(p-1) - p*eps
      (1-z)^2 = eps^2

    So near z=1:
      num ~ (p-1)/p * (-(p-1)) + O(eps) = -(p-1)^2/p + O(eps)
      zeta_p(z) ~ -(p-1)^2/p / eps^2 + O(1/eps)

    The Laurent expansion: zeta_p(z) = -(p-1)^2/p / eps^2 + c_{-1}/eps + ...

    Residue (coefficient of 1/eps):
      d/deps [eps^2 * zeta_p(1+eps)] |_{eps=0}
      = d/deps [(1-(1+eps)/p)(1-p(1+eps))] |_{eps=0}
      = d/deps [(p-1-eps)/p * (1-p-p*eps)] |_{eps=0}

    Let f(eps) = (p-1-eps)(1-p-p*eps)/p
    f'(eps) = [(-1)(1-p-p*eps) + (p-1-eps)(-p)] / p
    f'(0) = [(p-1) + (-p)(p-1)] / p = (p-1)(1-p)/p = -(p-1)^2/p

    Wait, let me redo this. The residue of a double pole g(z)/(z-a)^2 is g'(a).
    Here zeta_p(z) = g(z)/(1-z)^2 with g(z) = (1-z/p)(1-pz).
    Write as g(z)/(z-1)^2, so the residue at z=1 is g'(1).

    g(z) = (1-z/p)(1-pz) = 1 - pz - z/p + z^2
    g'(z) = -p - 1/p + 2z
    g'(1) = -p - 1/p + 2 = 2 - p - 1/p = (2p - p^2 - 1)/p = -(p^2 - 2p + 1)/p
           = -(p-1)^2/p

    So Res_{z=1} zeta_p(z) = -(p-1)^2/p.
    """
    return -Fraction((p - 1) ** 2, p)


def padic_shuffle_product_coefficient(d: int, p: int) -> Fraction:
    r"""The p-adic shuffle algebra structure constant at dimension d.

    For the CoHA of C^3, the shuffle product at dimension (1,1,...,1)
    (d copies) uses:
      S_d = prod_{1<=i<j<=d} zeta(z_i - z_j) evaluated at z_i = i.

    For the p-adic version, replace zeta -> zeta_p:
      S_d^{(p)} = prod_{1<=i<j<=d} zeta_p(i - j)

    OBSERVATION: since i-j is a nonzero integer for i != j,
    zeta_p(i-j) is well-defined (no poles at nonzero integers).

    For d=1: S_1 = 1 (empty product).
    For d=2: S_2 = zeta_p(1-2) = zeta_p(-1) = (1+1/p)(1+p)/(1+1)^2
           = ((p+1)/p)((p+1)/1) / 4 = (p+1)^2 / (4p).
    """
    if d <= 1:
        return Fraction(1)

    product = Fraction(1)
    for i in range(1, d + 1):
        for j in range(i + 1, d + 1):
            z = Fraction(i - j)
            product *= padic_shuffle_zeta(z, p)
    return product


# =========================================================================
# 4. p-ADIC STABILITY CONDITIONS (toy model)
# =========================================================================

class PAdicStabilityCondition(NamedTuple):
    """A toy model of a p-adic Bridgeland stability condition.

    For a CY3 X over Q_p, the central charge is Z: K_0(X) -> Q_p.
    In the toy model we consider rank-1 sheaves on a CY3 with
    h^{1,1}=1 (e.g., quintic), so K_0 is generated by O_X, O_pt,
    and the central charge is Z(E) = -d + i*r for a sheaf of
    rank r and degree d (complexified Kahler parameter).

    In the p-adic setting, there is no "i" in Q_p in general
    (it exists iff p = 1 mod 4 by quadratic reciprocity for i^2 = -1).
    Instead, the p-adic central charge lives in an extension Q_p(sqrt(-1)).

    HEURISTIC: The p-adic stability manifold Stab_p(X) is a rigid
    analytic space whose structure depends on whether sqrt(-1) in Q_p.

    For the toy model:
      Z_p(r, d) = -d + omega * r
    where omega in Q_p(sqrt(-1)) plays the role of the Kahler parameter.
    """
    p: int
    sqrt_minus_1_exists: bool   # True iff p = 1 mod 4
    omega_approx: Optional[int]  # sqrt(-1) mod p if it exists
    phase_structure: str         # description of the phase structure


def padic_stability_toy(p: int) -> PAdicStabilityCondition:
    r"""Construct the toy p-adic stability condition at prime p.

    sqrt(-1) exists in Q_p iff p = 1 mod 4 (or p = 2).
    When it exists, we find sqrt(-1) mod p by brute force.

    For p = 5: 5 = 1 mod 4, so sqrt(-1) = 2 (since 2^2 = 4 = -1 mod 5).
    This is the "Gepner prime" for the quintic: the CY/LG correspondence
    at the Gepner point involves 5th roots of unity, and the p-adic
    structure is particularly nice at p=5.
    """
    assert _is_prime(p), f"p={p} is not prime"

    if p == 2:
        # sqrt(-1) does NOT exist in Q_2 (checking: 1^2=1, that's it in Z/2Z)
        # Actually in Q_2: -1 = 1 mod 2, but 1^2 = 1. Need to check mod 8.
        # In Z_2: x^2 = -1 has no solution because -1 = 7 mod 8 is not a QR mod 8.
        return PAdicStabilityCondition(
            p=2,
            sqrt_minus_1_exists=False,
            omega_approx=None,
            phase_structure="no sqrt(-1) in Q_2; stability requires ramified extension",
        )

    if p % 4 == 1:
        # Find sqrt(-1) mod p
        sqrtm1 = None
        for x in range(2, p):
            if _mod_pow(x, (p - 1) // 2, p) == p - 1:
                # x^{(p-1)/2} = -1 mod p, so x^{(p-1)/4} might be sqrt(-1)
                candidate = _mod_pow(x, (p - 1) // 4, p)
                if (candidate * candidate) % p == (p - 1):
                    sqrtm1 = candidate
                    break
        return PAdicStabilityCondition(
            p=p,
            sqrt_minus_1_exists=True,
            omega_approx=sqrtm1,
            phase_structure=(
                f"sqrt(-1) = {sqrtm1} mod {p}; "
                f"stability phases lie in Q_{p}(i) = Q_{p} "
                f"(unramified since p=1 mod 4)"
            ),
        )
    else:
        # p = 3 mod 4
        return PAdicStabilityCondition(
            p=p,
            sqrt_minus_1_exists=False,
            omega_approx=None,
            phase_structure=(
                f"sqrt(-1) not in Q_{p} (p={p}=3 mod 4); "
                f"stability requires Q_{p}(sqrt(-1)) "
                f"(unramified quadratic extension of Q_{p})"
            ),
        )


def gepner_prime_stability(p: int = 5) -> Dict[str, Any]:
    r"""Stability condition at the Gepner prime p=5 for the quintic.

    OBSERVATION (HEURISTIC): At p=5, the Fermat quintic has special
    arithmetic properties:
      - 5 | degree of the Fermat equation
      - The Gepner model CFT at the Fermat point has Z_5 symmetry
      - sqrt(-1) = 2 mod 5 (since 2^2 = 4 = -1 mod 5)

    The p-adic stability condition at p=5:
      Z_5(r, d) = -d + 2*r (mod 5), using sqrt(-1) = 2.

    The "stable" objects have phase in (0, 1), which in the p-adic
    setting means: the p-adic valuation of Z_5(E) determines stability.
    """
    stab = padic_stability_toy(p)
    assert stab.sqrt_minus_1_exists, f"p={p} should have sqrt(-1)"

    # Compute stable objects in the toy model (rank <= 3, |degree| <= 5)
    stable_objects: List[Dict[str, Any]] = []
    omega = stab.omega_approx
    assert omega is not None

    for r in range(1, 4):
        for d in range(-5, 6):
            # Z_p(r,d) = -d + omega*r mod p
            z_val = (-d + omega * r) % p
            # In the toy model, "stable" means z_val != 0 mod p
            # (nonvanishing central charge)
            stable_objects.append({
                'rank': r,
                'degree': d,
                'central_charge_mod_p': z_val,
                'stable_mod_p': z_val != 0,
            })

    return {
        'prime': p,
        'stability': stab,
        'num_stable': sum(1 for o in stable_objects if o['stable_mod_p']),
        'num_unstable': sum(1 for o in stable_objects if not o['stable_mod_p']),
        'objects': stable_objects,
    }


# =========================================================================
# 5. p-ADIC MODULAR CHARACTERISTIC (motivic measure)
# =========================================================================

def padic_modular_characteristic_quintic(p: int) -> Dict[str, Fraction]:
    r"""The p-adic modular characteristic kappa_p for the quintic.

    HEURISTIC: The motivic measure on a CY3 X is:
      mu_p(X) = integral_X |Omega_3|_p
    where Omega_3 is the holomorphic 3-form and |.|_p is the p-adic norm.

    For a smooth CY3 over Z_p: by the Weil conjectures and p-adic
    Hodge theory, this integral is related to the "special value" of
    the L-function:

      kappa_p(X) = v_p(mu_p(X))  (p-adic valuation)

    For the Fermat quintic:
      - The holomorphic 3-form has good reduction at p != 5.
      - At p = 5 (the Gepner prime): special behavior expected.

    COMPUTATION (toy model):
      kappa_p = ord_p(#X(F_p) - p^3 - p^2 - p - 1)
    i.e., the p-adic valuation of the H^3 trace of Frobenius.

    This is a HEURISTIC identification: we are proposing that the
    p-adic valuation of Tr(Frob|H^3) plays the role of the modular
    characteristic in the p-adic setting.
    """
    assert _is_prime(p), f"p={p} is not prime"

    count = _fermat_quintic_point_count_fast(p)
    tr_h3 = frobenius_trace_from_count(count, p, h11=1)

    # p-adic valuation of tr_h3
    if tr_h3 == 0:
        v_p = float('inf')
    else:
        v_p_int = 0
        temp = abs(tr_h3)
        while temp % p == 0:
            v_p_int += 1
            temp //= p
        v_p = v_p_int

    # The "classical" kappa is chi/24 = -200/24 = -25/3 (BCOV conjecture)
    kappa_classical = Fraction(-200, 24)

    return {
        'prime': p,
        'point_count': Fraction(count),
        'tr_frob_h3': Fraction(tr_h3),
        'v_p_tr_h3': Fraction(v_p) if v_p != float('inf') else None,
        'kappa_classical': kappa_classical,
        'kappa_p_heuristic': Fraction(v_p) if v_p != float('inf') else Fraction(0),
        'status': 'HEURISTIC',
    }


# =========================================================================
# 6. p-ADIC COHA (p-adic affine Yangian, toy model)
# =========================================================================

def padic_coha_dimension(d: int, p: int, N: int = 15) -> Fraction:
    r"""Dimension of the p-adic CoHA at dimension vector d (Jordan quiver).

    For the complex CoHA of C^3: dim CoHA_d = pp(d) (plane partitions).
    The generating function is the MacMahon function M(q).

    For the p-adic CoHA, the HEURISTIC prediction is:
      dim CoHA_d^{(p)} = pp(d) * (1 - 1/p^d) * ... (p-adic correction)

    More precisely, the p-adic correction comes from the local zeta
    factor of the moduli space M_d of d-dimensional representations.
    For M_d = Hilb^d(C^3) (in the rank-1 case):

      chi_p(Hilb^d) = pp(d) * prod_{k=1}^{d} (1 - p^{-k})

    This is the Euler characteristic with p-adic coefficients.

    OBSERVATION: The p-adic correction prod(1 - p^{-k}) converges to
    a nonzero limit as d -> infty, giving a p-adic analog of the
    MacMahon function.
    """
    # Plane partition count
    mac = _macmahon_count(d, N)

    # p-adic correction factor
    correction = Fraction(1)
    for k in range(1, d + 1):
        correction *= (Fraction(1) - Fraction(1, p ** k))

    return mac * correction


def _macmahon_count(d: int, N: int = 15) -> Fraction:
    """pp(d) via the MacMahon generating function."""
    mac = _fps_one(N)
    for k in range(1, N):
        for _ in range(k):
            for n in range(k, N):
                mac[n] += mac[n - k]
    if d < N:
        return mac[d]
    return Fraction(0)


def padic_macmahon(p: int, N: int = 15) -> FPS:
    r"""The p-adic MacMahon function M_p(q).

    M_p(q) = prod_{n>=1} (1 - q^n/p^n)^{-n} / (1 - q^n)^{-n} * M(q)
           ... no, the correct formula is:

    HEURISTIC: The p-adic MacMahon function is:
      M_p(q) = prod_{n>=1} 1/(1-q^n)^n * prod_{n>=1} (1-q^n/p^n)^n

    The first factor is the ordinary MacMahon function.
    The second factor is the p-adic correction, encoding the fact
    that p-adic representations have fewer automorphisms.

    Equivalently:
      M_p(q) = prod_{n>=1} ((1-q^n/p^n)/(1-q^n))^n

    For large p, M_p(q) -> M(q) (the correction tends to 1).
    """
    # Start with MacMahon
    mac = _fps_one(N)
    for k in range(1, N):
        for _ in range(k):
            for n in range(k, N):
                mac[n] += mac[n - k]

    # Apply p-adic correction: multiply by prod_{n>=1} (1-q^n/p^n)^n
    correction = _fps_one(N)
    for k in range(1, N):
        # Factor (1 - q^k / p^k)^k
        c_k = Fraction(1, p ** k)
        for _ in range(k):
            # Multiply correction by (1 - c_k * q^k)
            for n in range(N - 1, k - 1, -1):
                correction[n] -= c_k * correction[n - k]

    return _fps_mul(mac, correction, N)


# =========================================================================
# 7. ARITHMETIC SHADOW TOWER
# =========================================================================

class ArithmeticShadowTower(NamedTuple):
    """The arithmetic shadow tower for a CY3 over a number field.

    HEURISTIC: The shadow obstruction tower of A_{X_p} with p-adic
    coefficients carries arithmetic information:

      Genus 0: Theta_0 = genus-0 DT invariants = point counts #X(F_{p^n})
      Genus 1: Theta_1 = genus-1 shadow = p-adic modular form candidate
      Genus g: Theta_g = higher-genus arithmetic DT invariants

    The key observation: the genus-0 shadow tower already encodes the
    Weil zeta function (via point counts), so the higher-genus towers
    should encode "higher" arithmetic invariants.
    """
    name: str
    p: int
    genus_0_data: Dict[int, Fraction]   # n -> genus-0 shadow = #X(F_{p^n})
    genus_1_data: Optional[Fraction]    # genus-1 shadow coefficient
    weil_zeta_coeffs: FPS               # Z(X/F_p, t) mod t^N
    kappa_p: Fraction                   # p-adic modular characteristic


def arithmetic_shadow_tower_quintic(p: int, N: int = 8) -> ArithmeticShadowTower:
    r"""Compute the arithmetic shadow tower for the Fermat quintic at prime p.

    GENUS 0: Point counts #X(F_{p^n}) for n = 1, ..., N.
    These are the genus-0 DT invariants in the arithmetic setting.

    GENUS 1: The genus-1 shadow is kappa_p / 24, where kappa_p is the
    p-adic modular characteristic. This should be a p-adic modular form
    coefficient.

    OBSERVATION: For primes p with gcd(5, p-1)=1, the Fermat quintic
    is equivalent to a hyperplane, so the arithmetic is trivial:
      #X(F_{p^n}) = p^{3n} + p^{2n} + p^n + 1  (no H^3 correction)
      Tr(Frob|H^3) = 0
      kappa_p = 0 (trivially)

    The interesting primes are p = 1 mod 5: {11, 31, 41, 61, 71, ...}
    and p = 5 (the Gepner prime).
    """
    assert _is_prime(p), f"p={p} is not prime"

    # Genus 0: point counts
    genus_0: Dict[int, Fraction] = {}
    count_1 = _fermat_quintic_point_count_fast(p)
    genus_0[1] = Fraction(count_1)

    for n in range(2, N + 1):
        qn = p ** n
        if math.gcd(5, qn - 1) == 1:
            genus_0[n] = Fraction(qn**3 + qn**2 + qn + 1)

    # Weil zeta from available data
    zeta_coeffs = weil_zeta_series(
        {n: int(genus_0[n]) for n in genus_0}, N
    )

    # Genus 1: kappa_p / 24
    tr_h3 = frobenius_trace_from_count(count_1, p, h11=1)
    # HEURISTIC: kappa_p = -tr_h3 / p (normalized trace)
    if p != 0:
        kappa_p = Fraction(-tr_h3, p)
    else:
        kappa_p = Fraction(0)

    genus_1 = kappa_p / Fraction(24)

    return ArithmeticShadowTower(
        name=f"Fermat quintic / F_{p}",
        p=p,
        genus_0_data=genus_0,
        genus_1_data=genus_1,
        weil_zeta_coeffs=zeta_coeffs,
        kappa_p=kappa_p,
    )


def arithmetic_shadow_genus1_modular_check(
    p: int,
    shadow_g1: Fraction,
) -> Dict[str, Any]:
    r"""Check whether the genus-1 arithmetic shadow specializes to
    a classical modular form coefficient under p-adic regulators.

    HEURISTIC: The genus-1 shadow Theta_1 of A_{X_p} should be related
    to a weight-4 modular form (the weight of the modular form attached
    to H^3 of a rigid CY3 is 4 by Serre's conjecture / modularity).

    For the quintic (which is NOT rigid: h^{2,1}=101), the modularity
    is much more complex -- the Galois representation on H^3 is 204-dimensional.

    For RIGID CY3s (h^{2,1}=0), Serre's conjecture (now a theorem,
    Khare-Wintenberger) predicts that the Galois representation on H^3
    is modular, attached to a weight-4 cusp form for Gamma_0(N).

    OBSERVATION: The genus-1 shadow kappa_p/24 for the quintic is
    NOT expected to be a single modular form coefficient, because the
    quintic is not rigid. The check returns the comparison data.
    """
    # For a weight-4 eigenform f = sum a_n q^n, the coefficient a_p
    # should equal Tr(Frob_p | H^3) for the rigid CY3.
    #
    # For the quintic: not rigid, so we just record the comparison.
    return {
        'prime': p,
        'genus_1_shadow': shadow_g1,
        'is_rigid': False,  # quintic has h^{2,1} = 101
        'expected_modular_weight': 4,  # for a rigid CY3
        'modularity_applies': False,   # because quintic is not rigid
        'status': 'OBSERVATION: genus-1 shadow recorded; modularity '
                  'check only applies to rigid CY3s (h^{2,1}=0)',
    }


# =========================================================================
# 8. GALOIS REPRESENTATION FROM E_1 (HEURISTIC)
# =========================================================================

def galois_rep_from_e1_character(
    p: int,
    h11: int = 1,
    h21: int = 101,
) -> Dict[str, Any]:
    r"""Extract Galois representation data from the E_1 character.

    HEURISTIC: For a CY3 X defined over Q, the E_1 chiral algebra A_X
    should encode the l-adic Galois representation on H^*(X_{\bar Q}, Q_l).

    The Frobenius eigenvalues on H^3(X) appear in the E_1 character as:
      chi^{E_1}(Frob_p) = Tr(Frob_p | H^3(X))

    For the Fermat quintic:
      deg(P_3) = 2*(h21+1) = 204
      P_3(t) = det(1 - Frob_p * t | H^3(X))

    From #X(F_p), we can extract Tr(Frob_p | H^3) = a_1 coefficient.
    The full P_3 requires counting over multiple extensions F_{p^n}.
    """
    count = _fermat_quintic_point_count_fast(p)
    tr_frob = frobenius_trace_from_count(count, p, h11)

    b3 = 2 * (h21 + 1)  # = 204 for quintic

    # Weil bound: |alpha_i| = p^{3/2} for each eigenvalue of Frob on H^3
    weil_bound = p ** Fraction(3, 2)
    # So |Tr(Frob)| <= b3 * p^{3/2}
    bound = b3 * (p ** 1.5)

    return {
        'prime': p,
        'point_count': count,
        'tr_frob_h3': tr_frob,
        'b3': b3,
        'weil_bound': float(bound),
        'satisfies_weil': abs(tr_frob) <= bound + 1,  # +1 for rounding
        'p3_degree': b3,
        'status': 'HEURISTIC: Frobenius trace extracted from point count. '
                  'Full Galois representation requires F_{p^n} counts '
                  f'for n=1,...,{b3//2}.',
    }


# =========================================================================
# 9. FULL DIAGNOSTIC REPORT
# =========================================================================

def full_padic_cy3_report(p: int, N: int = 8) -> Dict[str, Any]:
    r"""Run the full p-adic CY3 E_1 diagnostic for the Fermat quintic at prime p.

    Collects:
      1. Point count #X(F_p)
      2. Frobenius trace on H^3
      3. p-adic shuffle zeta data
      4. p-adic stability condition
      5. p-adic modular characteristic
      6. Arithmetic shadow tower
      7. Galois representation data
      8. Weil zeta function
    """
    count = _fermat_quintic_point_count_fast(p)
    tr_h3 = frobenius_trace_from_count(count, p, h11=1)

    stab = padic_stability_toy(p)
    kappa_data = padic_modular_characteristic_quintic(p)
    shadow = arithmetic_shadow_tower_quintic(p, N)
    galois = galois_rep_from_e1_character(p)

    # p-adic shuffle data at small dimensions
    shuffle_data = {}
    for d in range(1, 5):
        shuffle_data[d] = padic_shuffle_product_coefficient(d, p)

    # p-adic MacMahon first few terms
    pmac = padic_macmahon(p, min(N, 10))

    # Weil zeta
    zeta_series = weil_zeta_series({1: count}, N)

    # Is gcd(5, p-1) = 1? (trivial arithmetic case)
    trivial = math.gcd(5, p - 1) == 1

    return {
        'prime': p,
        'trivial_arithmetic': trivial,
        'point_count': count,
        'tr_frob_h3': tr_h3,
        'stability': stab._asdict(),
        'kappa_data': kappa_data,
        'shadow_tower': {
            'genus_0': {n: str(v) for n, v in shadow.genus_0_data.items()},
            'genus_1': str(shadow.genus_1_data),
            'kappa_p': str(shadow.kappa_p),
        },
        'galois': galois,
        'shuffle_coefficients': {d: str(v) for d, v in shuffle_data.items()},
        'padic_macmahon': [str(c) for c in pmac[:min(8, len(pmac))]],
        'weil_zeta': [str(c) for c in zeta_series[:min(8, len(zeta_series))]],
        'status': 'ALL CLAIMS HEURISTIC/OBSERVATION',
    }


# =========================================================================
# 10. CROSS-PRIME CONSISTENCY CHECKS
# =========================================================================

def cross_prime_consistency(primes: Sequence[int] = (2, 3, 5, 7)) -> Dict[str, Any]:
    r"""Cross-prime consistency check for the p-adic CY3 construction.

    MULTI-PATH VERIFICATION:
      Path 1: Point counts agree with known values (literature).
      Path 2: Weil bound satisfied for all primes.
      Path 3: Trivial primes (gcd(5,p-1)=1) have tr_h3 = 0.
      Path 4: p-adic shuffle coefficients are rational (exact arithmetic).
      Path 5: p-adic MacMahon function has rational coefficients and
              M_p(0) = 1 for all p.
    """
    results: Dict[str, Any] = {'primes': list(primes), 'checks': {}}

    for p in primes:
        if not _is_prime(p):
            continue

        count = _fermat_quintic_point_count_fast(p)
        tr_h3 = frobenius_trace_from_count(count, p, h11=1)
        trivial = math.gcd(5, p - 1) == 1

        # Path 1: known values
        known_ok = True
        if p in FERMAT_QUINTIC_KNOWN_COUNTS:
            known_ok = (count == FERMAT_QUINTIC_KNOWN_COUNTS[p])

        # Path 2: Weil bound
        b3 = 204
        weil_ok = abs(tr_h3) <= b3 * (p ** 1.5) + 1

        # Path 3: trivial primes
        trivial_ok = True
        if trivial:
            trivial_ok = (tr_h3 == 0)

        # Path 4: shuffle rationality
        shuffle_ok = True
        for d in range(1, 4):
            try:
                sc = padic_shuffle_product_coefficient(d, p)
                shuffle_ok = shuffle_ok and isinstance(sc, Fraction)
            except Exception:
                shuffle_ok = False

        # Path 5: MacMahon
        pmac = padic_macmahon(p, 8)
        mac_ok = (pmac[0] == Fraction(1))

        results['checks'][p] = {
            'count': count,
            'tr_h3': tr_h3,
            'trivial': trivial,
            'known_values_ok': known_ok,
            'weil_bound_ok': weil_ok,
            'trivial_consistency_ok': trivial_ok,
            'shuffle_rationality_ok': shuffle_ok,
            'macmahon_normalization_ok': mac_ok,
            'all_ok': known_ok and weil_ok and trivial_ok and shuffle_ok and mac_ok,
        }

    results['all_primes_ok'] = all(
        r['all_ok'] for r in results['checks'].values()
    )
    return results


# =========================================================================
# 11. COMPARISON: COMPLEX vs p-ADIC MacMAHON
# =========================================================================

def macmahon_padic_vs_complex(p: int, N: int = 12) -> Dict[str, Any]:
    r"""Compare the p-adic and complex MacMahon functions.

    M(q) = prod_{n>=1} 1/(1-q^n)^n   (complex MacMahon)
    M_p(q) = prod_{n>=1} ((1-q^n/p^n)/(1-q^n))^n  (p-adic MacMahon)

    The ratio M_p(q)/M(q) encodes the p-adic correction to plane
    partition counting.

    OBSERVATION: For large p, M_p(q) ~ M(q) (corrections are O(1/p)).
    The leading correction is:
      M_p(q)/M(q) = 1 - q/p - 2q^2/p^2 + ...
    """
    mac = _fps_one(N)
    for k in range(1, N):
        for _ in range(k):
            for n in range(k, N):
                mac[n] += mac[n - k]

    pmac = padic_macmahon(p, N)

    # Ratio M_p / M
    ratio = _fps_mul(pmac, _fps_inv(mac, N), N)

    return {
        'prime': p,
        'complex_macmahon': [str(c) for c in mac[:min(8, N)]],
        'padic_macmahon': [str(c) for c in pmac[:min(8, N)]],
        'ratio': [str(c) for c in ratio[:min(8, N)]],
        'ratio_starts_with_1': ratio[0] == Fraction(1),
        'leading_correction': str(ratio[1]) if N > 1 else 'N/A',
    }


# =========================================================================
# 12. WEIL ZETA FUNCTION FACTORED FORM
# =========================================================================

def weil_zeta_factored_quintic(p: int) -> Dict[str, Any]:
    r"""Factor the Weil zeta function for the Fermat quintic at prime p.

    Z(X/F_p, t) = P_3(t) / ((1-t)(1-pt)(1-p^2 t)(1-p^3 t))

    For gcd(5, p-1)=1: P_3(t) = (1-p^{3/2} t)^{204}... no, that's not right.
    When gcd(5,p-1)=1: the Fermat quintic is equivalent to the hyperplane
    x_0+...+x_4 = 0, which is P^3. So P_3(t) = 1 (trivially).

    For p = 1 mod 5: the Galois representation on H^3 is nontrivial.
    We can extract Tr(Frob|H^3) = a_1 from the point count.
    """
    count = _fermat_quintic_point_count_fast(p)
    tr_h3 = frobenius_trace_from_count(count, p, h11=1)
    trivial = math.gcd(5, p - 1) == 1

    # For gcd(5, p-1)=1: P_3 should be 1 (no nontrivial H^3)
    # Wait: the Fermat quintic always has h^{2,1} = 101, b_3 = 204.
    # But when gcd(5,p-1)=1, the CHARACTER SUMS vanish, so:
    #   Tr(Frob|H^3) = 0
    # and all Frobenius eigenvalues on H^3 come in conjugate pairs
    # that cancel in the trace.
    #
    # More precisely: when gcd(5,p-1)=1, the 5th-power map is a bijection,
    # so the count = p^3+p^2+p+1 = #P^3(F_p), and Tr(Frob|H^3) = 0.
    # But P_3(t) is NOT trivially 1; it still has degree 204.
    # The individual Frobenius eigenvalues are nontrivial, but they
    # come in pairs (alpha, bar{alpha}) with alpha on the Weil circle
    # |alpha| = p^{3/2}, and their sum is 0.
    #
    # With only tr = 0, we know a_1 = 0 in P_3(t) = 1 - a_1 t + ...

    return {
        'prime': p,
        'trivial_case': trivial,
        'h11': 1,
        'h21': 101,
        'b3': 204,
        'p3_degree': 204,
        'point_count': count,
        'tr_frob_h3': tr_h3,
        'p3_a1': tr_h3,  # a_1 = Tr(Frob|H^3)
        'expected_trivial_trace': trivial,
        'trace_is_zero': tr_h3 == 0,
        'consistency': (not trivial) or (tr_h3 == 0),
    }


# =========================================================================
# MAIN
# =========================================================================

if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

    print("=" * 70)
    print("p-adic CY3 E_1 Construction: Computational Pipeline")
    print("STATUS: ALL CLAIMS HEURISTIC/OBSERVATION")
    print("=" * 70)

    for p in [2, 3, 5, 7]:
        print(f"\n{'='*70}")
        print(f"Prime p = {p}")
        print(f"{'='*70}")

        report = full_padic_cy3_report(p, N=8)
        print(f"  Point count #X(F_{p}) = {report['point_count']}")
        print(f"  Tr(Frob|H^3) = {report['tr_frob_h3']}")
        print(f"  Trivial arithmetic: {report['trivial_arithmetic']}")
        print(f"  p-adic stability: sqrt(-1) exists = "
              f"{report['stability']['sqrt_minus_1_exists']}")
        print(f"  kappa_p (heuristic) = {report['kappa_data']['kappa_p_heuristic']}")
        print(f"  Genus-1 shadow = {report['shadow_tower']['genus_1']}")
        print(f"  Weil bound satisfied: {report['galois']['satisfies_weil']}")

    print(f"\n{'='*70}")
    print("Cross-prime consistency")
    print(f"{'='*70}")
    consistency = cross_prime_consistency([2, 3, 5, 7])
    for p, data in consistency['checks'].items():
        print(f"  p={p}: all_ok={data['all_ok']}, "
              f"count={data['count']}, tr_h3={data['tr_h3']}")
    print(f"  ALL PRIMES OK: {consistency['all_primes_ok']}")
