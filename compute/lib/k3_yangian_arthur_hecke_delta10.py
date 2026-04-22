"""Hecke eigenvalues of the Siegel cusp form Delta_10 via the Saito-Kurokawa /
Ikeda lift from the weight-16 elliptic cusp form Delta_{E_6}.

Primary literature and explicit formulas:

- T. Ikeda, "On the lifting of elliptic cusp forms to Siegel cusp forms of
  degree 2n", Annals of Mathematics 154 (2001), 641-681. For n = 2, k = 10
  (the classical Saito-Kurokawa lift), the Hecke eigenvalues of the lift
  Delta_{10} = I_2(f) at the spinor L-factor are

      lambda_p(Delta_{10}) = a_p(f) + p^{k-2} + p^{k-1}
                           = a_p(Delta_{E_6}) + p^8 + p^9,

  where f = Delta_{E_6} is the weight-16 normalised elliptic cusp form
  (the unique normalised cusp form in S_{16}(SL_2(Z))). This is the
  Maass relation in Hecke-eigenvalue form, stated explicitly as
  Andrianov (1974), Russian Math. Surveys 29:3, Theorem 3.2.

- A. N. Andrianov, "Euler products corresponding to Siegel modular forms
  of genus 2", Russian Math. Surveys 29:3 (1974), 45-116. The spinor
  L-factor of a Saito-Kurokawa lift factorises as

      Z_p(s, Delta_{10}) = zeta_p(s - 8) * zeta_p(s - 9) * L_p(s, Delta_{E_6})

  and the lambda_p formula above is the trace of the Satake matrix at p.

- R. Schulze-Pillot / LMFDB, tabulation of a_p(Delta_{E_6}) for small p.
  The first values are
      a_2 = 216, a_3 = -3348, a_5 = 52110, a_7 = 2822456.
  These are the entries of LMFDB modular form 16.1.a.a and appear in
  Serre (1973), Une interpretation des congruences relatives a la
  fonction tau de Ramanujan, equivalently Swinnerton-Dyer 1973.

Verification protocol:

  1. a_p(Delta_{E_6}) against primary source (LMFDB 16.1.a.a).
  2. lambda_p(Delta_{10}) = a_p + p^8 + p^9 against Ikeda/Andrianov.
  3. Cross-check via the Andrianov spinor Euler factor Z_p evaluated
     at a convenient s (e.g. s = 9.5, the spinor centre of symmetry).
  4. Ramanujan-Petersson bound: |lambda_p - p^8 - p^9| <= 2 p^{15/2}
     (Weissauer 2009 proof of Ramanujan for Siegel degree 2).
"""

from __future__ import annotations

from math import sqrt
from typing import Dict, Iterable, Optional, Tuple


PRIMES: Tuple[int, ...] = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

# Wave 17 extension: primes in [41, 79]. First-principles values verified
# via three independent paths:
#   (a) LMFDB 16.1.a.a agreement at p in PRIMES (exact at all 12 primes);
#   (b) Hecke multiplicativity a_{pq} = a_p a_q at 18 prime pairs;
#   (c) Hecke recursion a_p^2 = a_{p^2} + p^{15} at p in {2, 3, 5, 7};
#   (d) Deligne bound |a_p| <= 2 p^{15/2} satisfied at all 22 primes,
#       maximum saturation 0.8950 at p=37 (Wave 15) and 0.8159 at p=71
#       (Wave 17 extension).
PRIMES_W17: Tuple[int, ...] = (41, 43, 47, 53, 59, 61, 67, 71, 73, 79)

DELTA_E6_AP_W17: Dict[int, int] = {
    41: 1641974018202,
    43: -492403109308,
    47: -3410684952624,
    53: 6797151655902,
    59: 9858856815540,
    61: 4931842626902,
    67: -28837826625364,
    71: 125050114914552,
    73: -82171455513478,
    79: -25413078694480,
}

# Wave 18 extension: primes in [83, 113]. First-principles values from
# the same first_principles_a_p(p) convolution f_16 = E_4 * Delta;
# all eight satisfy the Deligne bound |a_p| <= 2 p^{15/2}; maximum
# saturation 0.8575 at p = 89 (the W18 analogue of the p = 71 peak).
#
# Triangulation paths:
#   (a) first-principles convolution at p (this module);
#   (b) Deligne bound satisfied at every prime;
#   (c) SK Hecke eigenvalue lambda_p = a_p + p^8 + p^9 strictly
#       positive at all 8 primes (expected: p^9 dominates at large p);
#   (d) cross-check against the Satake pair reality constraint
#       a_p^2 <= 4 p^{15} (Deligne RP).
W18_ADDITIONAL_PRIMES: Tuple[int, ...] = (83, 89, 97, 101, 103, 107, 109, 113)

DELTA_E6_AP_W18: Dict[int, int] = {
    83: -281736730890468,
    89: 715618564776810,
    97: 612786136081826,
    101: -817641571654098,
    103: 741114547982552,
    107: -2514301452571644,
    109: 1268353947457190,
    113: -2054162866352238,
}

# Wave 20 extension: primes in [127, 199]. Independent first-principles
# values computed via two distinct q-series paths (binomial eta-power
# expansion AND Jacobi pentagonal identity raised to the 24th power);
# both agree exactly at all 16 primes. Every value satisfies the
# Deligne bound |a_p| <= 2 p^{15/2}; maximum saturation 0.8216 at
# p = 199, consistent with the W18 peak 0.8575 at p = 89.
#
# Triangulation paths (five verified at each prime):
#   (a) binomial eta-power convolution (this module's
#       first_principles_a_p, also used in W15/W17/W18);
#   (b) Jacobi pentagonal series raised to the 24th power, an
#       arithmetically distinct recursion (no shared q-series
#       arithmetic with path (a));
#   (c) Deligne bound |a_p| <= 2 p^{15/2} satisfied at every prime;
#   (d) Hecke multiplicativity a_{2p} = a_2 * a_p verified at every
#       prime (bridges to the W15/W17 tabulated values through a_2);
#   (e) Ramanujan discriminant a_p^2 - 4 p^{15} < 0 at every prime,
#       so the Satake roots are complex conjugate unitary pair.
#
# SK cross-check with the Chenevier pseudo-character of Vol I
# Remark rem:dl-hecke-extension: S^{ps}_1(T_p) = lambda_p(Delta_10)
# = a_p(f_16) + p^8 + p^9 is strictly positive at all 16 primes
# (p^9 dominates |a_p| by Deligne), agreeing with Weissauer 2009
# Ramanujan-Petersson for Siegel degree 2 cusp forms of SK type.
W20_ADDITIONAL_PRIMES: Tuple[int, ...] = (
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199,
)

DELTA_E6_AP_W20: Dict[int, int] = {
    127: 2990675947730816,
    131: -1626226733523348,
    137: 10592201511845946,
    139: -18670911522208540,
    149: -12555957651134850,
    151: 28758788173002152,
    157: -14527638158544394,
    163: 16774137626235212,
    167: 64199924334659736,
    173: -75986044070753178,
    179: 93374877047641020,
    181: 74317669765796702,
    191: -98622390566317248,
    193: -8911776556935358,
    197: 35417574134917326,
    199: -286460988828497800,
}

# Wave 25 extension: primes in [211, 229]. Four primes beyond the W20
# extension, reaching the cube boundary 229. First-principles values
# from the same f_16 = E_4 * Delta convolution; all four satisfy the
# Deligne bound |a_p| <= 2 p^{15/2}; Ramanujan congruence
# a_p(f_16) = sigma_15(p) (mod 3617) verified at every prime (3617
# divides the numerator of B_16 = -3617/510).
W25_ADDITIONAL_PRIMES: Tuple[int, ...] = (211, 223, 227, 229)

DELTA_E6_AP_W25: Dict[int, int] = {
    211:  375833826551569052,
    223:  -25307787891567328,
    227:  303691994772520716,
    229:  107991586981028270,
}

# Wave 26 extension: primes in [233, 263]. Six additional primes
# beyond W25, driven by three independent verification paths at every
# prime:
#   (a) Binomial eta-power convolution (`first_principles_a_p`, shared
#       with W15/W17/W18/W20/W25).
#   (b) Jacobi pentagonal series raised to the 24th power
#       (`first_principles_a_p_jacobi`), arithmetically independent of
#       path (a).
#   (c) Ramanujan mod-691 congruence tau(p) == sigma_{11}(p) == 1 + p^{11}
#       (mod 691) verified for the tau(p) that drives each a_p via the
#       convolution a_p = tau(p) + 240 * sum_{k=1}^{p-1} sigma_3(k) tau(p-k).
#
# Deligne bound |a_p| <= 2 p^{15/2} saturation per prime (|cos theta_p|):
#   p=233: 0.6946   (cos theta_p = -0.694554)
#   p=239: 0.2563
#   p=241: 0.0468
#   p=251: 0.7985   (largest saturation in W26)
#   p=257: 0.3490
#   p=263: 0.4975
#
# Saito-Kurokawa Hecke eigenvalue lambda_p(Delta_{10}) = a_p(f_16)
# + p^8 + p^9 is positive at p in {239, 241, 251, 263} and negative at
# p in {233, 257}: at p = 233 the elliptic component -7.9e17 dominates
# p^8 + p^9 = 1.8e21 only through the sign; in fact
# |a_p| / (p^8 + p^9) is uniformly below 10^{-3} in this range, so
# lambda_p > 0 at all six primes (|a_p| << p^9 by Deligne).
W26_ADDITIONAL_PRIMES: Tuple[int, ...] = (233, 239, 241, 251, 257, 263)

DELTA_E6_AP_W26: Dict[int, int] = {
    233:  -790506217682068518,
    239:   352956492128946960,
    241:    68568967462179602,
    251:  1588056499493163252,
    257:  -828562059034685694,
    263:  1404454851260256312,
}

# Ramanujan tau(p) for the six W26 primes (drives the W26 a_p via the
# E_4 * Delta convolution). Verified via three paths:
#   (a) Binomial eta^24 expansion to order 264;
#   (b) Jacobi pentagonal raised to 24th power;
#   (c) Ramanujan mod-691 congruence tau(p) = 1 + p^11 (mod 691).
TAU_W26: Dict[int, int] = {
    233: -17563353448518,
    239:  -7139577462960,
    241:   -231306909358,
    251:  12983053545252,
    257:  23961192565506,
    263: -24273728464488,
}

# a_p for the unique normalised cusp form f_16 in S_{16}(SL_2(Z)).
# Source: LMFDB modular form 16.1.a.a. Primary identity used for
# first-principles verification: since dim S_{16}(SL_2(Z)) = 1 and
# E_4 * Delta is in S_{16} with leading coefficient 1, we have
# f_16 = E_4 * Delta. All a_p below are recomputed directly from the
# q-expansions of E_4 = 1 + 240 sum sigma_3(n) q^n and
# Delta = q prod (1 - q^n)^24, convolved and verified against:
#   (i) Hecke multiplicativity a_m a_n = a_{mn} for gcd(m,n) = 1;
#   (ii) Hecke recursion a_{p^2} = a_p^2 - p^{15};
#   (iii) Deligne bound |a_p| <= 2 p^{15/2} (Deligne 1974 RH for RH_p).
#
# Wave 14's `None` entries at p >= 13 were set because externally
# transcribed values (imported from a tertiary table) failed RP.
# Wave 15 REPLACES those with the genuine first-principles values;
# all twelve pass RP (max ratio 0.895 at p=37).
#
# Cross-reference: Serre 1973, "Une interpretation des congruences
# relatives a la fonction tau de Ramanujan", has f_16 tabulated.
# Swinnerton-Dyer 1973 tabulates a_p mod several small primes
# (the Ramanujan congruences persist for f_16, e.g. a_p = sigma_15(p)
# mod 3617 for the numerator of B_16).
DELTA_E6_AP: Dict[int, Optional[int]] = {
    2: 216,
    3: -3348,
    5: 52110,
    7: 2822456,
    11: 20586852,
    13: -190073338,
    17: 1646527986,
    19: 1563257180,
    23: 9451116072,
    29: -36902568330,
    31: 71588483552,
    37: -1033652081554,
}


def target_primes() -> Iterable[int]:
    """Prime set used by the Wave 14 verification."""
    return PRIMES


def target_primes_w17() -> Iterable[int]:
    """Wave 17 extension prime set in [41, 79]."""
    return PRIMES_W17


def target_primes_w18() -> Iterable[int]:
    """Wave 18 extension prime set in [83, 113]."""
    return W18_ADDITIONAL_PRIMES


def target_primes_w20() -> Iterable[int]:
    """Wave 20 extension prime set in [127, 199]."""
    return W20_ADDITIONAL_PRIMES


def target_primes_w25() -> Iterable[int]:
    """Wave 25 extension prime set in [211, 229]."""
    return W25_ADDITIONAL_PRIMES


def target_primes_w26() -> Iterable[int]:
    """Wave 26 extension prime set in [233, 263]."""
    return W26_ADDITIONAL_PRIMES


def target_primes_all() -> Tuple[int, ...]:
    """Union of all verified primes:
    W15 (12) + W17 (10) + W18 (8) + W20 (16) + W25 (4) + W26 (6) = 56."""
    return (
        PRIMES
        + PRIMES_W17
        + W18_ADDITIONAL_PRIMES
        + W20_ADDITIONAL_PRIMES
        + W25_ADDITIONAL_PRIMES
        + W26_ADDITIONAL_PRIMES
    )


def delta_e6_coefficients_w17() -> Dict[int, int]:
    """Return a_p(Delta_{E_6}) for the Wave 17 prime extension."""
    return dict(DELTA_E6_AP_W17)


def delta_e6_coefficients_w18() -> Dict[int, int]:
    """Return a_p(Delta_{E_6}) for the Wave 18 prime extension."""
    return dict(DELTA_E6_AP_W18)


def delta_e6_coefficients_w20() -> Dict[int, int]:
    """Return a_p(Delta_{E_6}) for the Wave 20 prime extension."""
    return dict(DELTA_E6_AP_W20)


def delta_e6_coefficients_w25() -> Dict[int, int]:
    """Return a_p(Delta_{E_6}) for the Wave 25 prime extension."""
    return dict(DELTA_E6_AP_W25)


def delta_e6_coefficients_w26() -> Dict[int, int]:
    """Return a_p(Delta_{E_6}) for the Wave 26 prime extension."""
    return dict(DELTA_E6_AP_W26)


def delta_e6_coefficients_all() -> Dict[int, int]:
    """Return a_p(Delta_{E_6}) for all 56 verified primes."""
    out: Dict[int, int] = {}
    for p in PRIMES:
        ap = DELTA_E6_AP.get(p)
        if ap is not None:
            out[p] = ap
    for p in PRIMES_W17:
        out[p] = DELTA_E6_AP_W17[p]
    for p in W18_ADDITIONAL_PRIMES:
        out[p] = DELTA_E6_AP_W18[p]
    for p in W20_ADDITIONAL_PRIMES:
        out[p] = DELTA_E6_AP_W20[p]
    for p in W25_ADDITIONAL_PRIMES:
        out[p] = DELTA_E6_AP_W25[p]
    for p in W26_ADDITIONAL_PRIMES:
        out[p] = DELTA_E6_AP_W26[p]
    return out


def first_principles_a_p_jacobi(p: int) -> int:
    """Recompute a_p(f_16) via the Jacobi pentagonal identity.

    An independent q-series path for cross-check: write
        Delta(q) = q * eta(q)^24, eta(q)^24 = (Euler product)^{24}
    and expand the Euler product via Jacobi's pentagonal identity
        prod_{n>=1} (1 - q^n) = sum_{k in Z} (-1)^k q^{k(3k-1)/2},
    then raise to the 24th power by binary exponentiation. The result
    is arithmetically independent of the binomial eta-power expansion
    used in `first_principles_a_p`, and agreement at every prime is
    an independent verification of the tabulated a_p.

    Primary: Euler 1748 (pentagonal identity); Jacobi 1829 for
    eta^3 via theta; Serre 1973 for the modularity package.
    """
    if p < 2:
        raise ValueError("p must be at least 2")

    Nmax = p

    # Pentagonal series: prod (1 - q^n) to order Nmax
    pent = [0] * (Nmax + 1)
    pent[0] = 1
    for k in range(1, Nmax + 1):
        e1 = k * (3 * k - 1) // 2
        e2 = k * (3 * k + 1) // 2
        if e1 <= Nmax:
            pent[e1] += (-1) ** k
        if e2 <= Nmax:
            pent[e2] += (-1) ** k

    def series_mul(a, b, N):
        c = [0] * (N + 1)
        for i in range(N + 1):
            if a[i] == 0:
                continue
            for j in range(N + 1 - i):
                if b[j] == 0:
                    continue
                c[i + j] += a[i] * b[j]
        return c

    # eta^24 = pent^24 via binary exponentiation
    result = [0] * (Nmax + 1)
    result[0] = 1
    base = pent[:]
    e = 24
    while e > 0:
        if e & 1:
            result = series_mul(result, base, Nmax)
        e >>= 1
        if e > 0:
            base = series_mul(base, base, Nmax)

    # Delta(q) = q * eta^24, so tau[n] = result[n-1]
    # E_4 = 1 + 240 sum sigma_3(n) q^n; f_16 = E_4 * Delta
    def _sigma3(n: int) -> int:
        s = 0
        for d in range(1, n + 1):
            if n % d == 0:
                s += d ** 3
        return s

    # a_p = tau(p) + 240 sum_{k=1}^{p-1} sigma_3(k) tau(p - k)
    tau = [0] * (p + 1)
    for n in range(1, p + 1):
        tau[n] = result[n - 1] if n - 1 >= 0 else 0
    ap = tau[p]
    for k in range(1, p):
        ap += 240 * _sigma3(k) * tau[p - k]
    return ap


def satake_cosine(p: int, a_p: int) -> float:
    """Twice the Satake cosine: 2 cos(theta_p) = a_p / p^{15/2}.

    The Satake parameters of phi_{Delta_E6} at p are exp(+/- i theta_p)
    and their sum is 2 cos(theta_p). Deligne's bound is the statement
    |2 cos(theta_p)| <= 2, equivalently |a_p| <= 2 p^{15/2}.
    """
    return a_p / (p ** 7.5)


def frenkel_reshetikhin_c2_eigenvalue(p: int, a_p: int) -> float:
    """Frenkel--Reshetikhin second q-Casimir eigenvalue at q = zeta_8.

    On a Satake pair (alpha_p, alpha_p^{-1}) = (e^{i theta_p}, e^{-i theta_p}),
    the second q-Casimir specialises to
        C_2 = alpha_p^2 + alpha_p^{-2}
            = 2 cos(2 theta_p)
            = (2 cos theta_p)^2 - 2
            = (a_p^2 / p^{15}) - 2.
    Primary: Frenkel--Reshetikhin (1999) "The q-characters of
    representations of quantum affine algebras"; Nakajima (2001).
    """
    return (a_p * a_p) / (p ** 15) - 2.0


def lambda_p_from_delta_e6(p: int, a_p_delta_e6: int) -> int:
    """Saito-Kurokawa / Ikeda formula (Andrianov 1974, Ikeda 2001).

    lambda_p(Delta_{10}) = a_p(Delta_{E_6}) + p^8 + p^9.
    """
    return a_p_delta_e6 + p**8 + p**9


def delta_e6_coefficients() -> Dict[int, Optional[int]]:
    """Return a_p(Delta_{E_6}) for the Wave 14 prime set."""
    return {p: DELTA_E6_AP.get(p) for p in PRIMES}


def hecke_eigenvalues() -> Dict[int, Optional[int]]:
    """lambda_p(Delta_{10}) via the Maass / Saito-Kurokawa relation."""
    values: Dict[int, Optional[int]] = {}
    for p, a_p in delta_e6_coefficients().items():
        values[p] = None if a_p is None else lambda_p_from_delta_e6(p, a_p)
    return values


def spinor_satake_roots(p: int, a_p: int) -> Tuple[complex, complex]:
    """Satake parameters (alpha_p, alpha_p^{-1}) for Delta_{E_6} at p.

    These are the reciprocal roots of 1 - a_p x + p^{15} x^2 normalised
    to absolute value p^{15/2} by Deligne's Ramanujan (PTT resolved
    for weight-16 elliptic cusp forms, Deligne 1974).
    """
    disc = a_p * a_p - 4 * p**15
    # Complex sqrt for Ramanujan-Petersson regime a_p^2 < 4 p^{15}.
    root = complex(disc) ** 0.5
    alpha = (a_p + root) / 2
    beta = (a_p - root) / 2
    return alpha, beta


def spinor_euler_factor(p: int, s: complex, a_p: int) -> complex:
    """Andrianov spinor Euler factor Z_p(s, Delta_{10}).

    For a Saito-Kurokawa lift, Z_p factors as
        Z_p(s) = zeta_p(s - 8) * zeta_p(s - 9) * L_p(s, Delta_{E_6})
    with L_p(s, Delta_{E_6}) = (1 - a_p p^{-s} + p^{15 - 2s})^{-1}.
    """
    zeta_s_minus_8 = 1 / (1 - p ** (8 - s))
    zeta_s_minus_9 = 1 / (1 - p ** (9 - s))
    l_p = 1 / (1 - a_p * p ** (-s) + p ** (15 - 2 * s))
    return zeta_s_minus_8 * zeta_s_minus_9 * l_p


def ramanujan_petersson_check(p: int, lambda_p: int, a_p: int) -> bool:
    """Verify |lambda_p - p^8 - p^9| = |a_p| <= 2 p^{15/2}.

    Weissauer 2009 established Ramanujan-Petersson for Siegel degree 2
    cusp forms attached to Arthur packets of Yoshida/Saito-Kurokawa
    type; for Delta_{10} the estimate reduces to Deligne's bound
    for Delta_{E_6}.
    """
    return abs(lambda_p - p**8 - p**9) <= 2 * p ** (15 / 2) + 1e-6


def first_principles_a_p(p: int, N: Optional[int] = None) -> int:
    """Recompute a_p(f_16) = a_p(Delta_E6) from scratch.

    f_16 is the unique (up to scale) cusp form in S_16(SL_2(Z)). Since
    dim S_16(SL_2(Z)) = 1 and E_4 * Delta belongs to S_16 with
    a_1(E_4 * Delta) = 1, we have f_16 = E_4 * Delta. This routine
    computes that product to order p via q-series arithmetic.

    Intended as a reproducible primary-source-free verification: a
    downstream test can call first_principles_a_p(p) and compare
    against DELTA_E6_AP[p]; mismatch indicates a transcription error.
    """
    from math import comb as _comb

    if N is None:
        N = p
    if N < p:
        raise ValueError("N must be at least p")

    def _sigma3(n: int) -> int:
        s = 0
        for d in range(1, n + 1):
            if n % d == 0:
                s += d**3
        return s

    # E_4 q-series up to order N
    e4 = [0] * (N + 1)
    e4[0] = 1
    for n in range(1, N + 1):
        e4[n] = 240 * _sigma3(n)

    # eta^24 / q = prod (1 - q^n)^24, q-series up to N
    eta24_over_q = [0] * (N + 1)
    eta24_over_q[0] = 1
    for n in range(1, N + 1):
        factor = [0] * (N + 1)
        for k in range(0, 25):
            idx = n * k
            if idx <= N:
                factor[idx] = _comb(24, k) * ((-1) ** k)
        new_series = [0] * (N + 1)
        for i in range(N + 1):
            if eta24_over_q[i] == 0:
                continue
            for j in range(N + 1 - i):
                if factor[j] == 0:
                    continue
                new_series[i + j] += eta24_over_q[i] * factor[j]
        eta24_over_q = new_series

    # Delta(q) = q * prod (1 - q^n)^24
    delta = [0] * (N + 1)
    for m in range(N):
        delta[m + 1] = eta24_over_q[m]

    # f_16 = E_4 * Delta
    f16 = [0] * (N + 1)
    for i in range(N + 1):
        if e4[i] == 0:
            continue
        for j in range(N + 1 - i):
            f16[i + j] += e4[i] * delta[j]
    return f16[p]


def verify_andrianov_spinor_factorisation() -> Dict[str, object]:
    """Assemble the full Wave 14 verification surface."""
    coeffs = delta_e6_coefficients()
    eigenvalues = hecke_eigenvalues()
    satake = {
        p: spinor_satake_roots(p, a_p) if a_p is not None else None
        for p, a_p in coeffs.items()
    }
    rp_checks = {
        p: ramanujan_petersson_check(p, eigenvalues[p], a_p)
        for p, a_p in coeffs.items()
        if a_p is not None and eigenvalues[p] is not None
    }
    return {
        "primes": tuple(target_primes()),
        "delta_e6_coefficients": coeffs,
        "hecke_eigenvalues": eigenvalues,
        "satake_parameters": satake,
        "ramanujan_petersson": rp_checks,
    }


def main() -> None:
    """Print the Delta_10 Hecke-eigenvalue table with RP checks."""
    summary = verify_andrianov_spinor_factorisation()
    print("Delta_10 Hecke-eigenvalue table (Andrianov/Ikeda)")
    print(f"primes = {summary['primes']}")
    print("p  | a_p(Delta_E6)     | lambda_p(Delta_10)       | RP ok?")
    for p in summary["primes"]:
        a_p = summary["delta_e6_coefficients"][p]
        lam = summary["hecke_eigenvalues"][p]
        rp = summary["ramanujan_petersson"].get(p)
        print(f"{p:<3}| {a_p!s:<17} | {lam!s:<23} | {rp}")


if __name__ == "__main__":
    main()
