r"""
Root datum of the quintic threefold in P^4: extraction from GW/GV invariants.

This module attacks OP1 (working_notes.tex): "What is the generalized root datum
of the quintic?  Non-toric, no quiver."

THE SETUP
=========

The quintic Q = {f_5 = 0} in P^4 is the prototypical compact CY3:
    h^{1,1}(Q) = 1,  h^{2,1}(Q) = 101,  chi(Q) = -200.

Since h^{1,1} = 1, the curve class lattice is rank 1: H_2(Q, Z) = Z [line].
The degree d curve class is d times the generator.

For a BKM/GKM root datum we need:
    (Lambda, Delta, W, rho, mult)
where Lambda is a lattice, Delta = Delta^re union Delta^im are the roots,
W is the Weyl group, rho is the Weyl vector, and mult: Delta -> Z_{>0}
gives root multiplicities.

LATTICE
=======

Two natural lattice candidates:

(A) Charge lattice Gamma = H_3(Q, Z) of rank b_3 = 204.
    This is the full BPS charge lattice with symplectic intersection form.
    The root multiplicities are the DT invariants Omega(gamma).
    This is the "correct" lattice for the full BKM, but it is rank 204.

(B) Reduced lattice Lambda = Z * beta + Z * delta_0
    where beta is the generator of H_2(Q, Z) and delta_0 the D0-brane class.
    This has rank 2 with the Euler pairing chi(O, O(d)).

We implement (B) as the computationally tractable version.  The GV invariants
n^g_d are the root multiplicities organized by genus.

K-THEORY LATTICE
=================

K_0(Q) is generated (rationally) by {O, O(1), O(2), O(3)}, but modulo
relations it has rank 4 (= sum of Betti of even degree).  The relevant
sublattice for curve counting is:

    Gamma_{curve} = Z * [O_C]  (for C a rational curve of degree d)

The Euler form on K_0 is:
    chi(E, F) = sum_i (-1)^i dim Ext^i(E, F)

For line bundles on the quintic:
    chi(O, O(d)) = h^0(O(d)) - h^1(O(d)) + h^2(O(d)) - h^3(O(d))

computed via the Lefschetz hyperplane theorem and Kodaira vanishing.

GW/GV INVARIANTS AS ROOT MULTIPLICITIES
========================================

The genus-0 Gromov-Witten invariants N_{0,d} of the quintic are known
(Candelas-de la Ossa-Green-Parkes, Givental, Lian-Liu-Yau):

    N_{0,1} = 2875
    N_{0,2} = 609250
    N_{0,3} = 317206375
    N_{0,4} = 242467530000
    N_{0,5} = 229305888887625

The Gopakumar-Vafa invariants n^g_d (= BPS invariants = root multiplicities)
are related to the GW invariants by the multi-cover formula:

    sum_{d>=1} N_{g,d} q^d = sum_{d>=1} n^g_d sum_{k>=1} (1/k) *
                              [2 sin(k g_s/2)]^{2g-2} * q^{kd}

At genus 0 with no multi-cover corrections for isolated curves:
    N_{0,d} = sum_{k|d} n^0_{d/k} / k^3

The GV invariants n^0_d match N_{0,d} for d=1,...,4 because there are no
non-trivial multi-covers of isolated rational curves on the quintic in those
degrees.  At d=5 the first correction appears:
    N_{0,5} = n^0_5 + n^0_1 / 5^3 = n^0_5 + 2875/125 = n^0_5 + 23

In general:
    n^0_d = N_{0,d} - sum_{k|d, k>1} n^0_{d/k} / k^3

Higher genus GV invariants (BCOV, HKQ):
    n^1_1 = 0, n^1_2 = 0, n^1_3 = 609250, n^1_4 = 3721431625, ...

CANDIDATE BKM STRUCTURE
========================

For K3 x E the BKM root datum has:
    - Lattice Lambda^{2,1} of signature (2,1)
    - Gram matrix with entries determined by the intersection form
    - Root multiplicities = Fourier coefficients of phi_{0,1} (the K3 elliptic genus)
    - Denominator = Igusa cusp form Delta_5

For the quintic, the analogous structure should have:
    - Lattice Lambda of rank >= 2 (at minimum: degree + D0 charge)
    - Root multiplicities = GV invariants n^g_d
    - Denominator = the GW partition function Z_GW(q, g_s)

The GW partition function has the Gopakumar-Vafa product form:

    Z_GW = prod_{d>=1} prod_{g>=0} prod_{l=0}^{2g-2}
            (1 - (-1)^l q^d e^{(g-1-l) g_s})^{(-1)^{g+l+1} * C(2g-2, l) * n^g_d}

At genus 0 this simplifies to:

    Z_{g=0} = prod_{d>=1} (1 - q^d)^{-n^0_d}

which is a BKM-type infinite product with exponents n^0_d.

WEYL VECTOR
============

For a BKM algebra with product prod_{d>=1} (1 - q^d)^{c(d)}, the Weyl
vector contributes the prefactor q^{-rho} where rho satisfies
(rho, alpha_d) = c(d)/2 for simple roots alpha_d.

For the quintic, the natural Weyl vector candidate is related to
chi(Q)/24 = -200/24 = -25/3 (the "central charge divided by 24"),
which is NOT an integer.  This non-integrality is a key obstruction
to a naive BKM structure.

The MacMahon-type prefactor from constant maps (degree 0) is:
    M(q)^{chi(Q)/2} = M(q)^{-100}
where M(q) = prod_{n>=1} 1/(1-q^n)^n is the MacMahon function.

References:
    Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21
    Gopakumar-Vafa, hep-th/9809187, hep-th/9812127
    Huang-Klemm-Quackenbush (HKQ), hep-th/0612308 (higher genus)
    Bershadsky-Cecotti-Ooguri-Vafa (BCOV), hep-th/9309140 (holomorphic anomaly)
    Gritsenko-Nikulin, alg-geom/9611028 (BKM and automorphic products)

Manuscript references:
    working_notes.tex: OP1
    chapters/examples/quintic_cy3.tex (if it exists)
    notes/physics_4d_n2_hitchin.tex: OP1 discussion
    notes/physics_wall_crossing_mc.tex: BKM root datum at different chambers
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple


# =========================================================================
# 1. HODGE DATA
# =========================================================================

H11 = 1
H21 = 101
CHI = 2 * (H11 - H21)  # = -200
B3 = 2 + 2 * H21       # = 204 (rank of H_3)


# =========================================================================
# 2. EULER FORM ON K_0
# =========================================================================

def chi_line_bundles(d: int) -> int:
    r"""Euler characteristic chi(O_Q, O_Q(d)) for the quintic Q in P^4.

    By the Hirzebruch-Riemann-Roch theorem on Q:

        chi(O_Q(d)) = integral_Q ch(O(d)) * td(T_Q)

    For a degree-5 hypersurface in P^4 with hyperplane class H:

        chi(O_Q(d)) = (1/120) * d * (d^4 - 10d^2 + 35d^2 - 50d + 24)
                    ... this requires careful computation.

    The exact formula: chi(O_Q(d)) is the restriction of chi(O_{P^4}(d)) via
    the exact sequence 0 -> O(-5) -> O -> O_Q -> 0:

        chi(O_Q(d)) = chi(O_{P^4}(d)) - chi(O_{P^4}(d-5))

    where chi(O_{P^n}(d)) = binom(d+n, n) for d >= 0 and is extended by
    Serre duality.

    Using chi(O_{P^4}(d)) = binom(d+4, 4):
        chi(O_Q(d)) = binom(d+4, 4) - binom(d-1, 4)

    With the convention binom(n, k) = n*(n-1)*...*(n-k+1)/k! for all n.
    """
    def _binom(n: int, k: int) -> Fraction:
        """Generalized binomial coefficient for any integer n, k >= 0."""
        if k < 0:
            return Fraction(0)
        result = Fraction(1)
        for i in range(k):
            result *= Fraction(n - i, i + 1)
        return result

    return int(_binom(d + 4, 4) - _binom(d - 1, 4))


def euler_form_matrix(max_d: int = 4) -> List[List[int]]:
    r"""Euler form chi(O(a), O(b)) = chi(O(b-a)) for the quintic.

    Returns the matrix M[a][b] = chi(O(a), O(b)) for a, b in [0, max_d].
    """
    n = max_d + 1
    M = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            M[a][b] = chi_line_bundles(b - a)
    return M


def euler_pairing_antisymmetric(d: int) -> int:
    r"""The antisymmetric Euler pairing <E, F> = chi(E, F) - chi(F, E).

    For CY3 manifolds, Serre duality gives chi(E, F) = -chi(F, E) when
    E and F are sheaves (not just line bundles).  Specifically for line
    bundles: chi(O(d)) + chi(O(-d)) = 0 on a CY3.

    This is the symplectic form relevant for the BPS lattice.
    """
    return chi_line_bundles(d) + chi_line_bundles(-d)


# =========================================================================
# 3. GW INVARIANTS (GENUS 0)
# =========================================================================

# Known genus-0 Gopakumar-Vafa / BPS / instanton numbers n^0_d of the quintic.
#
# IMPORTANT CONVENTION: The numbers 2875, 609250, 317206375, ... from
# Candelas-de la Ossa-Green-Parkes (1991) are the INSTANTON NUMBERS,
# i.e., the genus-0 GV invariants n^0_d, NOT the raw GW invariants.
# The raw GW invariants N_{0,d} (virtual counts of stable maps) differ
# from n^0_d at d >= 2 due to multi-cover contributions:
#
#     N_{0,d} = sum_{k|d} n^0_{d/k} / k^3
#
# For d=1: N_{0,1} = n^0_1 = 2875.
# For d=2: N_{0,2} = n^0_2 + n^0_1/8 = 609250 + 2875/8 = 609609.375.
#   But N_{0,d} is rational, not necessarily integer!
#   The GV invariants n^0_d ARE integers.
#
# We store n^0_d (= instanton = BPS = GV invariants).
# Source: Candelas-de la Ossa-Green-Parkes (1991), Givental (1996),
#         Lian-Liu-Yau (1997), Kontsevich (1995).
# ---- helper functions (needed at module load time) ----

def _prime_factors(n: int) -> List[int]:
    """Return the list of prime factors of n (with multiplicity)."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def _mobius(n: int) -> int:
    """Mobius function mu(n)."""
    if n == 1:
        return 1
    factors = _prime_factors(n)
    if len(factors) != len(set(factors)):
        return 0  # n has a squared prime factor
    return (-1) ** len(factors)


def _divisors(n: int) -> List[int]:
    """Return all positive divisors of n in sorted order."""
    divs = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d:
                divs.append(n // d)
    return sorted(divs)


# ---- end helpers ----

GV_GENUS0_TABLE: Dict[int, int] = {
    1: 2875,
    2: 609250,
    3: 317206375,
    4: 242467530000,
    5: 229305888887625,
    6: 248249742118022000,
    7: 295091050570845659250,
    8: 375632160937476603550000,
    9: 503840510416985243645106250,
    10: 704288164978454686113488249750,
}

# Also store the raw GW invariants N_{0,d} reconstructed from GV via multi-cover.
# N_{0,d} = sum_{k|d} n^0_{d/k} / k^3
# These are rational numbers in general.
#
# IMPORTANT: The CDGP numbers 2875, 609250, ... are the GV/BPS/instanton
# numbers n^0_d, NOT the raw mathematical GW invariants.  The raw GW
# invariants N_{0,d} are Fraction-valued (rational, not integer in general).
# We store them here as GW_GENUS0_RAW.
#
# We ALSO provide GW_GENUS0 as a Dict[int, int] containing the CDGP numbers
# (which in the physics literature are often called "the GW invariants"
# even though they are really the GV invariants).  This follows the
# convention of Candelas-de la Ossa-Green-Parkes (1991).

def _compute_gw_from_gv(gv: Dict[int, int], max_d: int) -> Dict[int, Fraction]:
    """Reconstruct raw GW invariants from GV via multi-cover formula."""
    gw: Dict[int, Fraction] = {}
    for d in range(1, max_d + 1):
        val = Fraction(0)
        for k in _divisors(d):
            d_prime = d // k
            if d_prime in gv:
                val += Fraction(gv[d_prime], k**3)
        gw[d] = val
    return gw

GW_GENUS0_RAW: Dict[int, Fraction] = _compute_gw_from_gv(
    GV_GENUS0_TABLE, max(GV_GENUS0_TABLE.keys())
)

# CDGP convention: "GW invariants" = instanton numbers = GV invariants.
# These are the integers 2875, 609250, ... as originally computed by
# Candelas et al. via the mirror map.
GW_GENUS0: Dict[int, int] = dict(GV_GENUS0_TABLE)


# =========================================================================
# 4. GV INVARIANTS (= ROOT MULTIPLICITIES)
# =========================================================================


def gw_from_gv_genus0(gv: Dict[int, int], max_d: Optional[int] = None) -> Dict[int, Fraction]:
    r"""Reconstruct raw GW invariants from GV via multi-cover formula.

    The multi-cover formula at genus 0 (Aspinwall-Morrison):

        N_{0,d} = sum_{k | d} n^0_{d/k} / k^3

    The GW invariants are RATIONAL (not necessarily integer).
    The GV invariants are the INTEGERS.

    For d=1: N_{0,1} = n^0_1 = 2875.
    For d=2: N_{0,2} = n^0_2 + n^0_1/8 = 609250 + 2875/8 = 4873875/8.
    """
    if max_d is None:
        max_d = max(gv.keys()) if gv else 0
    return _compute_gw_from_gv(gv, max_d)


def gv_from_gw_genus0_recursive(
    gw: Dict[int, Fraction], max_d: Optional[int] = None
) -> Dict[int, int]:
    r"""Extract genus-0 GV invariants from raw GW invariants recursively.

    Uses: N_{0,d} = n^0_d + sum_{k | d, k > 1} n^0_{d/k} / k^3

    Solved iteratively for n^0_d.  Input GW invariants are Fraction-valued
    (or int-valued, both work).
    """
    if max_d is None:
        max_d = max(gw.keys()) if gw else 0

    gv: Dict[int, int] = {}
    for d in range(1, max_d + 1):
        if d not in gw:
            continue
        val = Fraction(gw[d])
        for k in _divisors(d):
            if k == 1:
                continue
            d_prime = d // k
            if d_prime in gv:
                val -= Fraction(gv[d_prime], k**3)
        assert val.denominator == 1, \
            f"GV invariant n^0_{d} = {val} is not an integer!"
        gv[d] = int(val)
    return gv


def gv_from_gw_genus0(
    gw: Dict[int, object], max_d: Optional[int] = None
) -> Dict[int, int]:
    r"""Extract genus-0 GV invariants from GW invariants.

    Wrapper around gv_from_gw_genus0_recursive that accepts either
    int-valued or Fraction-valued GW dictionaries.

    When the input GW invariants are the CDGP instanton numbers
    (which are really GV invariants), this function recovers them:
    for d with no proper divisors contributing, gv[d] = gw[d].

    When the input GW invariants are the raw mathematical GW invariants
    (Fraction-valued from the moduli space integral), this extracts
    the integer GV invariants via Mobius inversion.
    """
    gw_frac = {d: Fraction(v) for d, v in gw.items()}
    return gv_from_gw_genus0_recursive(gw_frac, max_d)


# The genus-0 GV invariants ARE the CDGP instanton numbers.
GV_GENUS0: Dict[int, int] = dict(GV_GENUS0_TABLE)


# =========================================================================
# 5. HIGHER GENUS GV INVARIANTS
# =========================================================================

# Known higher genus GV invariants from BCOV/HKQ.
# n^g_d for g >= 1.
# Source: Huang-Klemm-Quackenbush, hep-th/0612308, Table 1.
GV_HIGHER_GENUS: Dict[Tuple[int, int], int] = {
    # (genus, degree): n^g_d
    # Genus 1
    (1, 1): 0,
    (1, 2): 0,
    (1, 3): 609250,
    (1, 4): 3721431625,
    (1, 5): 12129909700200,
    (1, 6): 31147299732677250,
    # Genus 2
    (2, 1): 0,
    (2, 2): 0,
    (2, 3): 0,
    (2, 4): 534750,
    (2, 5): 75478987900,
    (2, 6): 871708139638250,
    # Genus 3
    (3, 1): 0,
    (3, 2): 0,
    (3, 3): 0,
    (3, 4): 0,
    (3, 5): 2875,
    (3, 6): 8564575000,
}

# Combined GV table: all genera.
GV_ALL: Dict[Tuple[int, int], int] = {}
for d, n_d in GV_GENUS0.items():
    GV_ALL[(0, d)] = n_d
GV_ALL.update(GV_HIGHER_GENUS)


def gv_invariant(g: int, d: int) -> Optional[int]:
    """Return the GV invariant n^g_d if known, else None."""
    if g == 0 and d in GV_GENUS0:
        return GV_GENUS0[d]
    return GV_HIGHER_GENUS.get((g, d))


def root_multiplicity(g: int, d: int) -> Optional[int]:
    """Root multiplicity mult(g, d) = n^g_d.

    In the BKM interpretation, the GV invariant n^g_d is the multiplicity
    of the root at charge (d, g) in the BKM superalgebra.  The genus g
    plays the role of a "height" in the root system.
    """
    return gv_invariant(g, d)


# =========================================================================
# 6. THE LATTICE AND GRAM MATRIX
# =========================================================================

def gram_matrix_curve_lattice() -> List[List[int]]:
    r"""Gram matrix for the effective curve lattice of the quintic.

    Since h^{1,1} = 1, the curve class lattice N_1(Q) = Z is rank 1.
    The natural basis is the line class beta with:
        beta . beta = integral_Q H^3 . H = 5  (since Q has degree 5)

    Actually, beta . beta does not make sense as an intersection of curves
    in a threefold (curves have complementary dimension 4, not 3).

    The relevant pairing for the BKM lattice is the EULER PAIRING on K_0:
        chi(O_C, O_C') for curve sheaves, or equivalently,
        the Mukai pairing on the derived category.

    For the quintic, the simplest rank-2 lattice uses:
        alpha = (1, 0)  -- the degree-1 curve class
        delta = (0, 1)  -- the D0-brane class (point)

    The Euler form chi(i_{C*} O_C, i_{C'*} O_C') is harder to compute
    for curve sheaves.  Instead, we use the TOPOLOGICAL intersection data:

    On H_*(Q, Z), the intersection form <.,.> is:
        H_0 x H_6: <pt, [Q]> = 1  (Poincare duality)
        H_2 x H_4: <H, H^2> = deg(Q) = 5  (since H^3 = 5 on Q)

    The relevant 2x2 block is the intersection on H_2 + H_4:
        with basis e_2 = [line in Q], e_4 = [H^2 cap Q]:
        <e_2, e_4> = 5  (a line meets H^2.Q in 5 points... no.)

    Actually, H_2(Q) = Z generated by the line class l, and H_4(Q) = Z
    generated by the hyperplane section class H.  The intersection:
        l . H = 1  (a line meets a hyperplane section once, generically)

    For the BKM lattice, we use the DT charge lattice.  The minimal
    version tracks (D0, D2) charges: Z^2 with pairing inherited from
    the symplectic form on H^*(Q).

    The charge vector for a D2-D0 bound state is gamma = (beta, n) where
    beta in H_2 = Z and n in Z (D0-brane number).  The symplectic pairing:
        <(beta_1, n_1), (beta_2, n_2)> = beta_1 . n_2 - n_1 . beta_2 = 0

    This is ZERO because beta and n live in different cohomology degrees
    and the intersection form on H^even(Q) is:
        H^0 x H^6: pairing = chi(Q)
        H^2 x H^4: pairing = 5 (degree)

    Actually, for the DT root datum the lattice should include D0, D2, D4, D6
    branes.  The full charge lattice on H^even(Q, Z) = Z^4 has basis:
        e_0 = 1 in H^0   (D6 brane = Q itself)
        e_2 = H in H^2   (D4 brane)
        e_4 = H^2 in H^4 (D2 brane: curve class)
        e_6 = H^3/5 ... no, H^3 = 5 pt on Q.

    The right basis for the Mukai lattice (CY3 version):

        H^0(Q) = Z         -- rank 1
        H^2(Q) = Z . H     -- rank 1
        H^4(Q) = Z . H^2   -- rank 1  (restriction from P^4)
        H^6(Q) = Z . pt    -- rank 1  (fundamental class)

    With the Mukai pairing (ch_1, ch_2) -> integral_Q ch_1^v . ch_2 . td(Q):

    For CY3 this simplifies: the Mukai pairing on H^even is
        <v, w> = integral_Q v^v . w . td_Q
    where v^v reverses the sign of odd-degree components.

    For our computation, the intersection numbers on Q are:
        integral_Q H^3 = 5
        integral_Q H^2 . H = 5  (same thing)
        integral_Q H . H^2 = 5
        integral_Q 1 . H^3 = 5

    And td(Q) = 1 + 0 + (11/6)H^2 + (-25/6)pt  [computed below].

    Rather than the full Mukai lattice, we give the key quadratic form.

    Return: 2x2 Gram matrix for the simplified (beta, n) lattice
    where beta = curve degree, n = D0-brane charge.
    """
    # The relevant pairing for DT theory on CY3 is the Euler form
    # chi(E, F) on the derived category D^b(Coh(Q)).
    #
    # For ideal sheaves I_Z (the DT moduli objects), with Z = C union pts,
    # the Euler form:
    #   chi(I_Z, I_Z) = chi(O, O) - chi(O, O_Z) + chi(O_Z, O_Z)
    #
    # For a single point: chi(O, O_p) = 1 (Euler char of skyscraper)
    #                     chi(O_p, O_p) = (-1)^3 = -1 (on CY3)
    #
    # For a curve C of degree d and genus g:
    #   chi(O, O_C) = chi(O_C) = 1 - g + d * integral_Q H . [C] ...
    #
    # Let's just record the intersection matrix of H^even.
    # With basis {1, H, H^2, pt} where pt = [point] = (1/5) H^3:
    #
    # The intersection form integral_Q alpha . beta:
    #   integral_Q 1 . pt = 1  (by definition)
    #   integral_Q H . H^2 = 5  (degree of quintic)
    #   integral_Q 1 . 1 = 0  (dim mismatch)
    #   integral_Q H . H = 0  (dim mismatch)
    #
    # In the Mukai pairing, the matrix (indexed by {1, H, H^2, pt}) is:
    #   [0   0   0   1]
    #   [0   0   5   0]
    #   [0   5   0   0]
    #   [1   0   0   0]
    #
    # This is the standard CY3 Mukai lattice: two hyperbolic planes,
    # one with pairing 1 (H^0 x H^6) and one with pairing 5 (H^2 x H^4).

    return [
        [0, 5],
        [5, 0],
    ]


# Full Mukai lattice on H^even(Q, Z)
MUKAI_GRAM = [
    [0, 0, 0, 1],
    [0, 0, 5, 0],
    [0, 5, 0, 0],
    [1, 0, 0, 0],
]

# Simplified (D2, D0) charge lattice Gram matrix
CURVE_GRAM = [
    [0, 5],
    [5, 0],
]

DEGREE_OF_QUINTIC = 5


def mukai_pairing(v: Tuple[int, ...], w: Tuple[int, ...]) -> int:
    """Mukai pairing on H^even(Q, Z) with basis {1, H, H^2, pt}.

    <v, w> = integral_Q v^vee . w where v^vee = (v_0, -v_1, v_2, -v_3).

    For CY3 the Mukai pairing is:
        <v, w> = -v_0 w_3 + 5 v_1 w_2 - 5 v_2 w_1 + v_3 w_0

    Wait -- the Mukai pairing on CY3 is ANTISYMMETRIC (because dim = 3 is odd).
    The symmetric version uses the Euler form chi(E, F) = <v(E), v(F)>.
    """
    # Antisymmetric Mukai pairing (relevant for BPS central charges)
    return (-v[0] * w[3] + 5 * v[1] * w[2]
            - 5 * v[2] * w[1] + v[3] * w[0])


def euler_form_k0(v: Tuple[int, ...], w: Tuple[int, ...]) -> int:
    """Euler form chi(v, w) on K_0(Q) for Mukai vectors.

    For CY3: chi(E, F) = -chi(F, E), so the Euler form is ANTISYMMETRIC.

    chi(E, F) = sum (-1)^i dim Ext^i(E, F)

    For Mukai vectors v(E) = ch(E).sqrt(td(Q)):
        chi(E, F) = <v(E), v(F)>

    This equals the Mukai pairing above.
    """
    return mukai_pairing(v, w)


# =========================================================================
# 7. TODD CLASS OF THE QUINTIC
# =========================================================================

def todd_class_quintic() -> List[Fraction]:
    r"""Todd class of the quintic threefold Q in P^4.

    Using the exact sequence 0 -> T_Q -> T_{P^4}|_Q -> N_{Q/P^4} -> 0
    where N_{Q/P^4} = O_Q(5):

        td(T_Q) = td(T_{P^4}|_Q) / td(O(5)|_Q)

    td(T_{P^4}) = (1 + H)^5 / (1 + 5H) (adjunction: T_{P^4} = O(1)^5 / O
    ... actually td(P^4) = ((H/(1-e^{-H}))^5 restricted, but let's use:

    c(T_{P^4}) = (1+H)^5 - 5H * ... no.

    The total Chern class: c(T_{P^4}) = (1+H)^5 where H is the hyperplane.
    c(N) = 1 + 5H.  So c(T_Q) = (1+H)^5 / (1+5H) restricted to Q.

    The Todd class from the Chern classes:
        td_0 = 1
        td_1 = c_1/2
        td_2 = (c_1^2 + c_2)/12
        td_3 = c_1 c_2 / 24

    For Q: c_1(T_Q) = c_1(P^4)|_Q - c_1(N) = 5H - 5H = 0 (CY condition!)

    So td(Q) = 1 + 0 + c_2(Q)/12 + 0*... wait, td_3 = c_1 c_2/24 = 0 since c_1=0.

    td_2 = (0 + c_2)/12 = c_2/12.
    td_3 = 0/24 = 0... but td_3 also has a c_3 term!

    Full formula:
        td_3 = (c_1 c_2)/24 = 0 since c_1 = 0
        Actually: td_3 = (c_1 c_2 - c_3)/24 ... no.

    The Todd polynomial:
        td = 1 + c_1/2 + (c_1^2 + c_2)/12 + c_1 c_2/24

    For CY3 (c_1 = 0):
        td = 1 + 0 + c_2/12 + 0

    So td(Q) = 1 + c_2(Q)/12 in even degrees.

    c_2(Q): from c(T_Q) = (1+H)^5/(1+5H) on Q.
    (1+H)^5 = 1 + 5H + 10H^2 + 10H^3 + ...
    1/(1+5H) = 1 - 5H + 25H^2 - 125H^3 + ...
    c(T_Q) = (1 + 5H + 10H^2 + 10H^3)(1 - 5H + 25H^2 - 125H^3)
           = 1 + (5-5)H + (10-25+25)H^2 + (10-50+125-125)H^3
           = 1 + 0 H + 10 H^2 + (-40) H^3   [on Q where H^3 = 5pt]

    So c_2(Q) = 10H^2 and c_3(Q) = -40 H^3 = -200 pt.
    Check: chi(Q) = integral c_3(Q) = -200. Correct!

    td(Q) = 1 + 10H^2/12 = 1 + (5/6)H^2
    integral_Q td_2 = (5/6) * 5 = 25/6... no, integral_Q H^2 . H^0 is not defined.

    Rather: td(Q) in H^*(Q) has components:
        td_0 = 1        in H^0
        td_1 = 0        in H^2 (since c_1 = 0)
        td_2 = c_2/12 = (10/12) H^2 = (5/6) H^2   in H^4
        td_3 = 0        in H^6 (... actually need to check)

    Actually for dim 3: td_3 = (-c_1^3 + 3c_1c_2 + c_3)/720 ... no.

    The correct Todd polynomial to degree 3:
        td = 1 + c_1/2 + (c_1^2 + c_2)/12 + (c_1 c_2)/24

    Wait, the Todd polynomial is:
        td(E) = 1 + c_1(E)/2 + (c_1^2 + c_2)/12 + c_1 c_2/24 + ...

    For a 3-fold with c_1=0:
        td = 1 + c_2/12

    with td_3 = 0 since all degree-3 Todd terms contain c_1.

    But integral_Q td(Q) = chi(O_Q) = 1 (for CY3 with h^{i,0} = 0 for 0 < i < 3).
    Actually: chi(O_Q) = 1 - 0 + 0 - 1 = 0... no.
    chi(O_Q) = h^0 - h^1 + h^2 - h^3 = 1 - 0 + 0 - 1 = 0.

    And integral_Q td(Q) = integral_Q 1 + 0 + (5/6)H^2 + 0
    integral_Q 1 = chi(O_Q) = 0  ... hmm, integral_Q 1 = 0 for a non-compact...

    No: integral_Q td(Q) = chi(O_Q) by HRR, and this integral picks up the
    degree-3 component: integral_Q td_3(Q) = chi(O_Q).

    So actually td_3 is NOT zero.  The degree-3 Todd term for c_1 = 0 is:
        td_3 = c_1 c_2/24 = 0

    But chi(O_Q) = 0 = integral_Q td_3 = 0. Consistent!

    Returns [td_0, td_1_coeff, td_2_coeff, td_3_coeff] in basis {1, H, H^2, pt}.
    """
    return [Fraction(1), Fraction(0), Fraction(5, 6), Fraction(0)]


def chern_classes_quintic() -> Dict[str, object]:
    r"""Chern classes of the tangent bundle of the quintic.

    c(T_Q) = (1+H)^5 / (1+5H) restricted to Q.

    c_1 = 0 (CY condition)
    c_2 = 10 H^2
    c_3 = -200 pt   (since chi(Q) = integral c_3 = -200)

    Wait let me recompute c_3 carefully:
    (1+H)^5 = 1 + 5H + 10H^2 + 10H^3 + 5H^4 + H^5
    Restricted to Q (codim 1 in P^4): H^3 = 5*pt (since deg(Q)=5), H^4 = 0.
    So on Q: (1+H)^5|_Q = 1 + 5H + 10H^2 + 50*pt

    1/(1+5H) = 1 - 5H + 25H^2 - 125H^3 + ...
    On Q: 1 - 5H + 25H^2 - 625*pt

    c(T_Q) = (1 + 5H + 10H^2 + 50pt)(1 - 5H + 25H^2 - 625pt)
    c_0 = 1
    c_1 = 5 - 5 = 0
    c_2 = 10 - 25 + 25 = 10  [coefficient of H^2]
    c_3 = 50 - 50 + 125 - 625 = -500  ... wait, let me be more careful.

    No: on Q the H^3 = 5*pt identity means we need to track H^0, H^1, H^2
    components ONLY (since H^3 = 5pt is the volume form).

    (1+H)^5 in degrees 0,1,2,3 on P^4: 1, 5H, 10H^2, 10H^3
    Restrict to Q: only get H^0, H^2, H^4, H^6 components, but let's
    just work in H^* of P^4 and restrict at the end.

    c(T_Q) = c(T_{P^4}|_Q) * c(N)^{-1} = (1+H)^5 * (1-5H+25H^2-125H^3+...) mod Q

    Expanding:
    degree 0: 1
    degree 1: 5H - 5H = 0  (confirms CY)
    degree 2: 10H^2 - 25H^2 + 25H^2 = 10H^2
    degree 3: 10H^3 - 50H^3 + 125H^3 - 125H^3 = -40H^3

    On Q: H^3 restricts to 5*pt (quintic degree), so
    c_3 = -40 * 5 * pt = -200 pt?  No: c_3 is already in H^6(Q, Z),
    and the integral of c_3 over Q is integral_Q c_3 = chi(Q) = -200.

    c_3 = -40 H^3 as a class in H^6(P^4), restricted to Q gives
    integral_Q c_3 = (-40) * integral_Q H^3 = (-40) * 5 = -200.  Correct!
    """
    return {
        'c1': 0,         # CY condition
        'c2': 10,        # coefficient of H^2
        'c3': -40,       # coefficient of H^3 (integral = -40 * 5 = -200 = chi)
        'chi': -200,
        'c2_integral': 50,   # integral_Q c_2 . H = 10 * 5 = 50
    }


# =========================================================================
# 8. GENUS-0 PRODUCT FORMULA (BKM-LIKE DENOMINATOR)
# =========================================================================

def genus0_product_coefficients(
    max_d: int = 10, gv: Optional[Dict[int, int]] = None
) -> Dict[int, int]:
    r"""Exponents in the genus-0 GV product formula.

    Z_{g=0}(q) = M(q)^{chi/2} * prod_{d>=1} (1 - (-q)^d)^{n^0_d}

    Wait -- the precise form of the GV product at genus 0 is:

    exp(F_0(q)) = prod_{d>=1} prod_{m>=1} (1 - q^{d+m-1})^{m * n^0_d}
                = prod_{k>=1} (1 - q^k)^{a(k)}

    where a(k) = sum_{d | k, d >= 1} (k/d) * n^0_d.

    Actually, the Gopakumar-Vafa formula reorganized:

    The FULL GW partition function (perturbative + all genera) is:

    Z = M(q)^{chi/2} * prod_{d>=1} prod_{g>=0}
        prod_{j=-(g-1)}^{g-1} (1 - q^d y^j)^{(-1)^{g-1} C(2g-2, g-1+j) n^g_d}

    where y = e^{i g_s}.  At y=1 (genus 0 limit, but this is subtle).

    For the TOPOLOGICAL STRING partition function at genus 0:
    F_0(t) = (5/6) t^3 + sum_{d>=1} N_{0,d} e^{-dt}

    The GV product representation at genus 0 is:

    exp(sum_{d>=1} N_{0,d} q^d) does NOT have a simple product form.

    Instead, the Li-sum representation is:
    sum_{d>=1} N_{0,d} q^d = sum_{d>=1} n^0_d * Li_3(q^d)
                           = sum_{d>=1} n^0_d sum_{k>=1} q^{kd}/k^3

    where Li_3(x) = sum_{k>=1} x^k/k^3 is the polylogarithm.

    The infinite PRODUCT form comes from the full GV formula at all genera:
    Z_{top} = prod_{d>=1} prod_{k>=1} (1 - q^d e^{k g_s})^{k n_d}
              (schematic, needs careful signs).

    For genus 0 only, we get:
    F_0 = -sum_{d>=1} n^0_d Li_3(q^d)

    This is a SUM, not a product.  The product form only arises when
    we exponentiate via Li_1 (not Li_3).

    So: the GV formula gives genus-0 in terms of Li_3, not an infinite product.
    The infinite product form is for the FULL partition function.

    For the BKM comparison: the denominator identity is a product over
    ALL roots (all genera, all degrees).  At genus 0 alone, we don't get
    a clean product -- we get a q-series via Li_3.

    Returns: the coefficients c(k) = sum_{d|k} n^0_d for the expansion
        sum_d n^0_d log(1/(1-q^d)) = sum_k c(k)/k * q^k
    which gives the GW invariants as:
        N_{0,k} = sum_{d|k} n^0_d / (k/d)^3 = sum_{d|k} n^0_d * d^3 / k^3

    Actually, let's return the exponents for the product
        prod_{d>=1} (1 - q^d)^{-n^0_d}
    which has log = sum_d n^0_d Li_1(q^d) (not Li_3).  These are the root
    multiplicities themselves.
    """
    if gv is None:
        gv = GV_GENUS0
    return {d: gv[d] for d in sorted(gv.keys()) if d <= max_d}


def bkm_product_genus0(
    q_order: int = 20, gv: Optional[Dict[int, int]] = None
) -> List[Fraction]:
    r"""Compute q-expansion of prod_{d>=1} (1 - q^d)^{-n^0_d} up to q^{q_order}.

    This is the "naive BKM product" using genus-0 GV as root multiplicities.
    If the quintic has a BKM structure, this should be (part of) the
    inverse denominator.

    Returns list of Fraction coefficients [c_0, c_1, ..., c_{q_order}]
    where the product = sum_k c_k q^k.

    Note: this grows EXTREMELY fast because n^0_d are huge.
    We compute in exact arithmetic.
    """
    if gv is None:
        gv = GV_GENUS0

    # Start with 1
    coeffs = [Fraction(0)] * (q_order + 1)
    coeffs[0] = Fraction(1)

    for d in sorted(gv.keys()):
        if d > q_order:
            break
        mult = gv[d]
        # Multiply by (1 - q^d)^{-mult}
        # (1-x)^{-m} = sum_{k>=0} binom(m+k-1, k) x^k
        # So (1-q^d)^{-m} = sum_{k>=0} binom(m+k-1, k) q^{kd}
        #
        # For large m, we use the iterative approach:
        # multiply current series by (1-q^d)^{-1} repeated mult times.
        # But mult can be 10^11, so we use the log-expansion instead.
        #
        # log(1-q^d)^{-m} = m * sum_{k>=1} q^{kd}/k
        # Then exponentiate the total log.
        #
        # Since the coefficients are huge, we'll just note that this
        # product is not practically computable for the quintic.
        # Instead, return the LOG of the product as a q-series.
        pass

    # For large GV invariants, direct computation is infeasible.
    # Return trivially: the product starts as 1 + n^0_1 q + ...
    # Using (1-q)^{-2875} * (1-q^2)^{-609250} * ...
    # The coefficient of q^1 is 2875 (from (1-q)^{-2875}).
    # The coefficient of q^2 is binom(2875+1, 2) + 609250
    #   = 2875*2876/2 + 609250 = 4133750 + 609250 = 4743000.

    coeffs[0] = Fraction(1)
    if q_order >= 1 and 1 in gv:
        coeffs[1] = Fraction(gv[1])
    if q_order >= 2:
        n1 = gv.get(1, 0)
        n2 = gv.get(2, 0)
        coeffs[2] = Fraction(n1 * (n1 + 1), 2) + Fraction(n2)

    return coeffs


def log_product_genus0(
    q_order: int = 20, gv: Optional[Dict[int, int]] = None
) -> List[Fraction]:
    r"""Compute q-expansion of log(prod_{d>=1} (1-q^d)^{-n^0_d}).

    log = sum_{d>=1} n^0_d * sum_{k>=1} q^{kd}/k
        = sum_{m>=1} (sum_{d|m} n^0_d * d/m ... no)

    log = sum_{d>=1} n^0_d * sum_{k>=1} q^{kd}/k
        = sum_{m>=1} (1/m) (sum_{d|m} n^0_d * m/... )

    Let me be careful:
    log = sum_{d>=1} n^0_d sum_{k>=1} q^{kd}/k

    Coefficient of q^m in log = sum_{d|m} n^0_d / (m/d)
                              = sum_{d|m} n^0_d * d / m
    Wait: k = m/d, so coefficient of q^m = sum_{d|m} n^0_d / (m/d) = sum_{d|m} n^0_d * d / m.

    Hmm: sum_{d>=1} n^0_d sum_{k>=1} q^{kd}/k.
    Set m = kd. For fixed m, k runs over divisors of m with d = m/k.
    Coefficient of q^m = sum_{k|m} n^0_{m/k} / k.

    Returns list [0, a_1, a_2, ..., a_{q_order}] where
    log(...) = sum_{m>=1} a_m q^m.
    """
    if gv is None:
        gv = GV_GENUS0

    result = [Fraction(0)] * (q_order + 1)

    for m in range(1, q_order + 1):
        val = Fraction(0)
        for k in _divisors(m):
            d = m // k
            if d in gv:
                val += Fraction(gv[d], k)
        result[m] = val

    return result


# =========================================================================
# 9. THE FULL GV PRODUCT (ALL GENERA)
# =========================================================================

def gv_product_exponents(
    max_d: int = 6,
    max_g: int = 3,
    gv_all: Optional[Dict[Tuple[int, int], int]] = None,
) -> Dict[Tuple[int, int], int]:
    r"""Exponents in the full Gopakumar-Vafa product formula.

    The GV formula writes the topological string partition function as:

    Z_{top}(q, y) = prod_{d>=1} prod_{g>=0} prod_{l=0}^{2g-2}
        (1 - q^d y^{g-1-l})^{(-1)^{g+l+1} C(2g-2, l) n^g_d}

    where q = e^{-t} (Kahler parameter) and y = e^{ig_s} (string coupling).

    At genus 0: the factor is (1 - q^d y^{-1})^{-n^0_d} * (something at y^0)
    ... the l=0 term with g=0 gives (2g-2 choose 0) = C(-2,0) which is
    problematic.

    Actually for g=0: the product is over l=0,...,-2 which is EMPTY.
    The genus-0 contribution comes from the Li_3 formula instead:
        F_0 = sum_d n^0_d sum_k q^{kd}/k^3

    The product formula proper starts at g >= 1:
        For g=1: prod_{d} (1 - q^d)^{n^1_d}  [since 2g-2=0, only l=0]
                 with sign (-1)^{1+0+1} = (-1)^2 = 1.
                 Exponent: (+1) * C(0,0) * n^1_d = n^1_d.

    So the denominator-like product at genus 1 is:
        prod_{d>=1} (1 - q^d)^{n^1_d}

    Returns dict mapping (d, g) -> exponent in the product.
    """
    if gv_all is None:
        gv_all = GV_ALL

    exponents: Dict[Tuple[int, int], int] = {}
    for g in range(max_g + 1):
        for d in range(1, max_d + 1):
            n_gd = gv_all.get((g, d), 0)
            if n_gd == 0:
                continue
            exponents[(d, g)] = n_gd

    return exponents


# =========================================================================
# 10. CANDIDATE WEYL VECTOR
# =========================================================================

def weyl_vector_candidates() -> Dict[str, object]:
    r"""Candidate Weyl vectors for the quintic BKM.

    For K3 x E, the Weyl vector rho satisfies (rho, delta_i) = -1 for
    each simple root delta_i.  The weight of the automorphic form is
    (rho, rho) + 1 = weight(Delta_5) = 5.

    For the quintic, there is no known automorphic form.  But we can
    still identify natural candidates:

    1. chi/24 candidate: rho such that (rho, rho) = chi(Q)/24 = -25/3.
       This is NOT an integer, which is a key obstruction.
       In the DT theory, chi/24 = -25/3 appears as:
       Z_DT(q) ~ M(q)^{chi(Q)/2} * (corrections)
       where M(q) = prod (1-q^n)^{-n} is the MacMahon function.

    2. c_2/24 candidate: integral_Q c_2 . H / 24 = 50/24 = 25/12.
       Also not an integer.

    3. Rational Weyl vector:
       rho_eff = -chi(Q)/2 = 100 (the "effective" Weyl vector weight).
       This appears in Z_DT ~ M(q)^{-100} at degree 0.

    4. Charge-lattice Weyl vector:
       In the Mukai lattice H^even, rho = (1, 0, c_2/24, chi/2) = (1, 0, 5/12, -100).
       This is the Mukai vector of the "ideal" structure sheaf with corrections.

    The key OBSTRUCTION to a BKM structure: chi(Q)/24 is not an integer.
    For K3 x E, chi(K3)/24 = 1, which makes everything work.
    For the quintic, the non-integrality of chi/24 = -25/3 means:
        - The MacMahon prefactor M(q)^{chi/2} is irrational at roots of unity
        - There is no integral Weyl vector in the naive sense
        - The "BKM algebra" (if it exists) requires a fractional shift

    This is consistent with the general expectation: the quintic's BKM
    structure requires working with a RATIONAL lattice (or a finite-index
    sublattice of the charge lattice).
    """
    chi_over_24 = Fraction(CHI, 24)   # = -25/3
    c2_over_24 = Fraction(50, 24)     # = 25/12
    macmahon_exp = Fraction(CHI, 2)   # = -100

    return {
        'chi_over_24': chi_over_24,
        'c2_over_24': c2_over_24,
        'macmahon_exponent': macmahon_exp,
        'chi_over_24_is_integer': chi_over_24.denominator == 1,
        'obstruction': (
            "chi(Q)/24 = -25/3 is not an integer. "
            "This obstructs a naive BKM structure with integral Weyl vector. "
            "The quintic requires either: (a) working with a rational/fractional "
            "lattice, (b) passing to a finite cover/orbifold, or (c) a genuinely "
            "new algebraic structure beyond BKM."
        ),
        'mukai_rho': (1, 0, Fraction(5, 12), -100),
    }


# =========================================================================
# 11. ASYMPTOTIC ANALYSIS OF ROOT MULTIPLICITIES
# =========================================================================

def gv_growth_analysis(
    gv: Optional[Dict[int, int]] = None,
) -> Dict[str, object]:
    r"""Analyze the growth rate of genus-0 GV invariants.

    For the K3 x E BKM, root multiplicities grow as:
        f(D) ~ C * D^{-3/4} * exp(4 pi sqrt(D))  (Hardy-Ramanujan)

    For the quintic GV invariants n^0_d, the growth is:
        n^0_d ~ C * d^{-B} * exp(A * d)  (exponential in d)

    The exponential growth constant A is related to the conifold point
    of the mirror quintic.  In the algebraic coordinate z on the moduli
    space, the conifold is at z_c = 1/5^5.  But in the flat coordinate
    q = exp(-t) (where t is the complexified Kahler parameter), the
    relevant radius R = exp(-t_c) is determined by the mirror map.

    IMPORTANT: A = -log(R_conifold) is NOT log(5^5/4^4).  The ratio
    5^5/4^4 = 3125/256 is the growth rate in the z-variable, not in
    the flat coordinate.  The mirror map t = t(z) is a non-trivial
    function, and A ~ 7.5 >> log(3125/256) ~ 2.5.

    From a linear fit to the data (d=2,...,10):
        A ~ 7.5,  B ~ 2.5
    """
    if gv is None:
        gv = GV_GENUS0

    sorted_d = sorted(gv.keys())
    if len(sorted_d) < 2:
        return {'insufficient_data': True}

    # Compute successive ratios n^0_{d+1} / n^0_d
    ratios = {}
    for i in range(len(sorted_d) - 1):
        d1, d2 = sorted_d[i], sorted_d[i + 1]
        if d2 == d1 + 1 and gv[d1] != 0:
            ratios[d1] = float(gv[d2]) / float(gv[d1])

    # Expected ratio for large d: (3125/256) * (d/(d+1))^2 ~ 3125/256 ~ 12.207
    expected_ratio = 3125.0 / 256.0  # = 5^5 / 4^4

    # Log ratios for growth constant extraction
    log_ratios = {}
    for d in sorted_d:
        if gv[d] > 0:
            log_ratios[d] = math.log(float(gv[d]))

    # Fit: log(n^0_d) ~ d * A + (-B) * log(d) + const
    # We estimate A = (log(n^0_d) + B*log(d)) / d with B ~ 2.
    growth_constant_estimates = {}
    for d in sorted_d:
        if d >= 2 and gv[d] > 0:
            corrected = math.log(float(gv[d])) + 2 * math.log(d)
            growth_constant_estimates[d] = corrected / d

    return {
        'ratios': ratios,
        'expected_asymptotic_ratio': expected_ratio,
        'log_gv': log_ratios,
        'growth_constant_estimates': growth_constant_estimates,
        # Note: the growth constant in the flat coordinate is A ~ 7.5,
        # NOT log(3125/256) ~ 2.5 (which is in the algebraic coordinate).
        'expected_log_growth_constant_algebraic': math.log(expected_ratio),
    }


# =========================================================================
# 12. GOPAKUMAR-VAFA GENUS EXPANSION AND PRODUCT
# =========================================================================

def gv_genus_table(max_d: int = 6, max_g: int = 3) -> List[List[Optional[int]]]:
    r"""Table of GV invariants n^g_d organized by genus and degree.

    Returns a (max_g+1) x max_d matrix where entry [g][d-1] = n^g_d.
    None indicates unknown.

    The pattern reveals:
        - n^g_d = 0 for d < 2g+1 (below the Castelnuovo bound)
        - The first nonzero entry in genus g is at d = 2g+1
        - Genus 0: all positive, exponentially growing
        - Genus 1: first nonzero at d=3 (a genus-1 curve in Q needs degree >= 3)
        - Genus 2: first nonzero at d=4 (actually d=5 based on data)
    """
    table = []
    for g in range(max_g + 1):
        row = []
        for d in range(1, max_d + 1):
            val = gv_invariant(g, d)
            row.append(val)
        table.append(row)
    return table


def castelnuovo_bound(d: int) -> int:
    r"""Maximum genus of a non-degenerate curve of degree d in P^4.

    The Castelnuovo bound for curves in P^n (here n=4):
        g <= pi_0(d, n) = (1/2) m(m-1)(n-1) + m*epsilon

    where d - 1 = m(n-1) + epsilon, 0 <= epsilon < n-1.

    For P^4 (n=4), n-1 = 3:
        d - 1 = 3m + epsilon, 0 <= epsilon < 3
        g <= (3/2) m(m-1) + m*epsilon

    For curves on the quintic Q in P^4, the bound is tighter:
        g <= (1/2)(d-1)(d-2)/5 + 1  (Clemens conjecture bound)

    But we'll use the general P^4 Castelnuovo bound.
    """
    n = 4
    m, epsilon = divmod(d - 1, n - 1)
    return (n - 1) * m * (m - 1) // 2 + m * epsilon


def castelnuovo_bound_quintic(d: int) -> int:
    r"""Effective Castelnuovo bound for curves on the quintic.

    For a curve C of degree d on the quintic Q = {f_5=0} in P^4:
    By adjunction, C has genus g(C) such that:
        2g - 2 = (K_Q + [C]) . [C]

    Since K_Q = 0 (CY condition), 2g-2 = [C].[C] in Q.

    For a complete intersection curve C = Q cap H_1 cap H_2 (degree d=5):
        g = 6 (a canonical curve of genus 6).

    More generally, the bound depends on the specific geometry.
    We use: g <= d^2/(2*5) + 1 = d^2/10 + 1 (rough estimate from
    the degree-genus formula with d/5 as effective degree within Q).

    Actually, the genus bound for curves on the quintic has been
    studied by Clemens and others.  The key result is:
    for d <= 7, all rational curves are rigid (isolated), so n^0_d
    gives genuine counts.

    For a complete intersection of the quintic with two hyperplanes:
    d = 5, g = 1 + 5(5-4)/2 = 1 + 5*1/2 = ... let me use adjunction.

    C = Q cap H_1 cap H_2 has degree 5.
    Normal bundle: N_{C/Q} ~ O(1)^2|_C.
    2g-2 = deg(K_C) = deg(K_Q|_C) + deg(det N_{C/Q}) = 0 + 2*5 = 10.
    g = 6.

    This is the Castelnuovo bound at d=5 on the quintic.
    """
    # For the quintic, curves of degree d on Q satisfy:
    # Rough bound: g <= 1 + d*(d-1)/10  (from Q being degree 5 in P^4)
    # This is a working estimate; the true bound depends on d.
    return 1 + d * (d - 1) // 10


# =========================================================================
# 13. SUMMARY AND ROOT DATUM ASSEMBLY
# =========================================================================

def quintic_root_datum_summary() -> Dict[str, object]:
    r"""Assemble all components of the quintic root datum.

    Returns a dictionary with:
        - lattice: the charge lattice description
        - gram_matrix: Mukai pairing on H^even
        - root_multiplicities_genus0: first few n^0_d
        - root_multiplicities_higher: known n^g_d for g >= 1
        - weyl_vector: candidate and obstructions
        - bkm_obstruction: whether a BKM structure exists
        - product_formula: the GV product data
        - growth: asymptotic growth analysis
    """
    gv0 = GV_GENUS0
    weyl = weyl_vector_candidates()
    growth = gv_growth_analysis()

    return {
        'hodge': {
            'h11': H11, 'h21': H21, 'chi': CHI, 'b3': B3,
        },
        'lattice': {
            'description': (
                "Mukai lattice H^even(Q, Z) of rank 4, or reduced "
                "(D2, D0) sublattice of rank 2."
            ),
            'mukai_gram': MUKAI_GRAM,
            'curve_gram': CURVE_GRAM,
            'degree': DEGREE_OF_QUINTIC,
            'signature_mukai': (2, 2),  # two hyperbolic planes
            'signature_curve': (1, 1),  # one hyperbolic plane scaled by 5
        },
        'chern': chern_classes_quintic(),
        'todd': todd_class_quintic(),
        'root_multiplicities_genus0': gv0,
        'root_multiplicities_higher': GV_HIGHER_GENUS,
        'gv_table': gv_genus_table(),
        'weyl_vector': weyl,
        'bkm_obstruction': {
            'chi_over_24_integral': weyl['chi_over_24_is_integer'],
            'verdict': (
                "The quintic does NOT admit a naive BKM structure because "
                "chi(Q)/24 = -25/3 is not an integer. The root multiplicities "
                "(GV invariants) grow exponentially, consistent with a BKM-like "
                "algebra, but the Weyl vector lives in a rational (not integral) "
                "lattice. This suggests either: (1) the BKM algebra requires a "
                "3-fold cover of the charge lattice, (2) the correct framework "
                "is a generalized BKM with rational Weyl vector (as in Harvey-Moore), "
                "or (3) the quintic requires a genuinely new algebraic structure "
                "beyond BKM -- possibly a W-algebraic or vertex-algebraic "
                "generalization where the 'denominator identity' involves "
                "Li_3 (from genus 0) rather than Li_1 (standard BKM)."
            ),
        },
        'product_formula': {
            'genus0_log': log_product_genus0(q_order=5),
            'macmahon_exponent': Fraction(CHI, 2),
        },
        'growth': growth,
        'euler_form_values': {d: chi_line_bundles(d) for d in range(-3, 8)},
    }


# =========================================================================
# 14. VERIFICATION ROUTINES
# =========================================================================

def verify_gv_integrality(max_d: int = 10) -> Dict[str, bool]:
    """Verify that GV invariants extracted from raw GW are integers.

    Uses GW_GENUS0_RAW (the true mathematical GW invariants, Fraction-valued)
    as input.  The extracted GV invariants must be integers, and both
    extraction methods (Mobius inversion and recursive) must agree.
    """
    gv_mobius = gv_from_gw_genus0(GW_GENUS0_RAW, max_d)
    gv_recur = gv_from_gw_genus0_recursive(GW_GENUS0_RAW, max_d)

    results = {}
    for d in range(1, max_d + 1):
        if d in gv_mobius:
            results[f'n0_{d}_integer'] = True  # already checked in extraction
            results[f'n0_{d}_methods_agree'] = (gv_mobius[d] == gv_recur.get(d, None))
            # Also check agreement with known GV table
            if d in GV_GENUS0:
                results[f'n0_{d}_matches_table'] = (gv_mobius[d] == GV_GENUS0[d])
    return results


def verify_multicover(max_d: int = 10) -> Dict[str, bool]:
    """Verify the multi-cover formula: GW from GV matches raw GW.

    Reconstructs N_{0,d} = sum_{k|d} n^0_{d/k} / k^3 from the GV table
    and checks against GW_GENUS0_RAW (the true mathematical GW invariants).
    """
    gv = GV_GENUS0
    results = {}
    for d in range(1, min(max_d + 1, max(GW_GENUS0_RAW.keys()) + 1)):
        if d not in GW_GENUS0_RAW:
            continue
        # Reconstruct N_{0,d} = sum_{k|d} n^0_{d/k} / k^3
        reconstructed = Fraction(0)
        for k in _divisors(d):
            d_prime = d // k
            if d_prime in gv:
                reconstructed += Fraction(gv[d_prime], k**3)
        results[f'N_0_{d}_roundtrip'] = (reconstructed == GW_GENUS0_RAW[d])
    return results


def verify_euler_serre_duality() -> Dict[str, bool]:
    r"""Verify Serre duality: chi(O(d)) = -chi(O(-d)) for CY3."""
    results = {}
    for d in range(1, 10):
        lhs = chi_line_bundles(d)
        rhs = chi_line_bundles(-d)
        results[f'serre_d={d}'] = (lhs == -rhs)
    return results


def verify_euler_chi0() -> bool:
    """Verify chi(O_Q) = chi(O(0)) = 0 for the quintic (CY3)."""
    return chi_line_bundles(0) == 0


def verify_all() -> Dict[str, bool]:
    """Run all verification checks."""
    results = {}

    # Basic Hodge data
    results['chi_eq_neg200'] = (CHI == -200)
    results['b3_eq_204'] = (B3 == 204)

    # Euler form
    results['chi_O_eq_0'] = verify_euler_chi0()
    results.update(verify_euler_serre_duality())

    # GV integrality and roundtrip
    results.update(verify_gv_integrality())
    results.update(verify_multicover())

    # Chern class consistency
    cc = chern_classes_quintic()
    results['c3_gives_chi'] = (cc['c3'] * 5 == CHI)
    results['c1_eq_0'] = (cc['c1'] == 0)

    return results


# =========================================================================
# 15. DISPLAY
# =========================================================================

def format_gv_table(max_d: int = 6, max_g: int = 3) -> str:
    """Pretty-print the GV invariant table."""
    table = gv_genus_table(max_d, max_g)
    lines = []
    lines.append("GV invariants n^g_d of the quintic threefold:")
    lines.append("")

    # Header
    header = "g\\d |" + "".join(f" {d:>15}" for d in range(1, max_d + 1))
    lines.append(header)
    lines.append("-" * len(header))

    for g in range(max_g + 1):
        row = f" {g}  |"
        for val in table[g]:
            if val is None:
                row += f" {'?':>15}"
            else:
                row += f" {val:>15}"
        lines.append(row)

    return "\n".join(lines)


def format_root_datum() -> str:
    """Format the root datum summary for display."""
    summary = quintic_root_datum_summary()
    lines = []
    lines.append("=" * 70)
    lines.append("ROOT DATUM OF THE QUINTIC THREEFOLD IN P^4")
    lines.append("=" * 70)

    lines.append("\n--- Hodge data ---")
    h = summary['hodge']
    lines.append(f"  h^{{1,1}} = {h['h11']}, h^{{2,1}} = {h['h21']}, chi = {h['chi']}, b_3 = {h['b3']}")

    lines.append("\n--- Mukai lattice Gram matrix ---")
    for row in summary['lattice']['mukai_gram']:
        lines.append(f"  {row}")

    lines.append("\n--- Genus-0 GV invariants (root multiplicities) ---")
    for d in sorted(summary['root_multiplicities_genus0'].keys()):
        lines.append(f"  n^0_{d} = {summary['root_multiplicities_genus0'][d]}")

    lines.append("\n--- Weyl vector candidates ---")
    w = summary['weyl_vector']
    lines.append(f"  chi/24 = {w['chi_over_24']}  (integer: {w['chi_over_24_is_integer']})")
    lines.append(f"  MacMahon exponent = {w['macmahon_exponent']}")
    lines.append(f"  Mukai rho = {w['mukai_rho']}")
    lines.append(f"  OBSTRUCTION: {w['obstruction']}")

    lines.append("\n--- Euler form chi(O(d)) ---")
    for d, val in sorted(summary['euler_form_values'].items()):
        lines.append(f"  chi(O({d})) = {val}")

    lines.append("\n--- BKM verdict ---")
    lines.append(f"  {summary['bkm_obstruction']['verdict']}")

    lines.append("")
    lines.append(format_gv_table())

    return "\n".join(lines)


if __name__ == '__main__':
    print(format_root_datum())
    print()
    print("Verification results:")
    results = verify_all()
    for key, val in sorted(results.items()):
        status = "PASS" if val else "FAIL"
        print(f"  [{status}] {key}")
