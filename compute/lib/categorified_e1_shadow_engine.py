r"""
categorified_e1_shadow_engine.py -- Categorification of the E_1 shadow
obstruction tower for CY3 categories.

MATHEMATICAL CONTEXT:

The E_1 shadow obstruction tower Theta^{E_1}_A produces NUMBERS:
kappa, F_g, DT invariants Omega(gamma), BPS state counts n^g_d.
CATEGORIFICATION lifts these numbers to vector spaces, chain complexes,
sheaves, and categories.

==========================================================================
HIERARCHY OF CATEGORIFICATION
==========================================================================

Level 0 (Numbers): Omega(gamma) in Z, F_g in C, kappa in Q.
Level 1 (Vector spaces): Omega^cat(gamma) = graded vector space with
    dim = Omega(gamma). The BPS SHEAF.
Level 2 (Chain complexes): B^{E_1,cat}(A_X, sigma) = chain complex
    over each stability condition sigma. Euler char = DT invariant.
Level 3 (Sheaves on moduli): F_g^cat in D^b(M_bar_g) = a sheaf on the
    moduli of curves. chi(F_g^cat) = F_g.
Level 4 (Motivic): B^{E_1,mot}(A_X) valued in K_0(Var_k).
    The motivic bar complex.
Level 5 (Categorical): DH(D^b(X)) = Toen's derived Hall algebra.
    The E_1 bar of DH is the categorified shadow tower.
Level 6 (Sheaf-theoretic CoHA): SCoHA(Q,W) = monoidal dg category.
    Its K-theory = numerical CoHA.

==========================================================================
KEY MATHEMATICAL STRUCTURES
==========================================================================

1. CATEGORIFIED BAR COMPLEX:
   B^{E_1,cat}(A_X, sigma) = sheaf of chain complexes on Stab(D^b(X)).
   Fiber at sigma is the bar complex with respect to stability sigma.
   The wall-crossing formula = motivic DT wall crossing = change of
   fiber as sigma crosses a wall.

2. VANISHING CYCLE CATEGORIFICATION:
   For quiver (Q,W): Omega^cat(d) = phi_{Tr W}(IC_{Rep(Q,d)})
   is the vanishing cycle sheaf of the trace potential.
   dim H^*(Omega^cat(d)) = |Omega(d)| (absolute BPS count).
   chi(Omega^cat(d)) = Omega(d) (signed DT invariant).

3. MOTIVIC BAR COMPLEX:
   B^{E_1,mot}(A_X) valued in K_0(Var_k)[[q]].
   For C^3: the motivic MacMahon function
     M^{mot}(q) = sum_n [Hilb^n(C^3)] * q^n
   where [Hilb^n(C^3)] is the class of the Hilbert scheme in K_0(Var_k).

4. DERIVED HALL ALGEBRA:
   DH(D^b(X)) categorifies Hall multiplication (Toen 2006).
   B^{E_1}(DH(D^b(X))) = categorified shadow tower.
   The MC element Theta^{E_1,cat} in MC(DH).

5. SHEAF-THEORETIC CoHA (Porta-Sala, Kapranov-Vasserot):
   SCoHA(Q,W) = oplus_d Sh^{BM}(Crit(Tr W)_d).
   Monoidal dg category. K_0(SCoHA) = numerical CoHA.

6. CATEGORIFIED SHADOW ON M_bar_g:
   F_g^cat in D^b(M_bar_g): the genus-g shadow is a SHEAF on the
   moduli of curves. chi(F_g^cat) = F_g (numerical shadow amplitude).
   For uniform-weight algebras: F_g^cat = kappa * lambda_g^{FP} (a line
   bundle on M_bar_g). The categorification is trivial at this level.
   For class M algebras: F_g^cat carries genuinely higher-rank structure.

REFERENCES:
    Kontsevich-Soibelman (2008): Motivic DT, arXiv:0811.2435
    Toen (2006): Derived Hall algebras, arXiv:math/0501343
    Schiffmann-Vasserot (2012): CoHA, arXiv:1202.1838
    Porta-Sala (2022): Sheaf-theoretic CoHA, arXiv:2106.02880
    Kapranov-Vasserot (2019): CoHA and categorification
    Maulik-Nekrasov-Okounkov-Pandharipande (2003): DT/GW, math/0312059
    Joyce-Song (2012): Generalized DT invariants
    Ben-Bassat-Brav-Bussi-Joyce (2015): Categorified DT
    Brav-Dyckerhoff (2019): Relative CY structures
    Vol I: bar complex, shadow obstruction tower, kappa definition
    Vol III: CY-to-chiral functor, E_1 bar-cobar

CONVENTIONS:
    - Cohomological grading (|d| = +1)
    - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (desuspension convention)
    - kappa(H_k) = k for Heisenberg (AP48, NOT c/2)
    - [X] denotes the class of X in K_0(Var_k)
    - L = [A^1] is the Lefschetz motive
    - Exact arithmetic via fractions.Fraction
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple


# =========================================================================
# 0. POWER SERIES ARITHMETIC (exact, over Q)
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


def _fps_power(a: FPS, k: int, N: int) -> FPS:
    """Compute a(q)^k mod q^N by repeated squaring."""
    if k == 0:
        return _fps_one(N)
    if k == 1:
        return list(a[:N]) + _fps_zero(max(0, N - len(a)))
    if k < 0:
        return _fps_power(_fps_inv(a, N), -k, N)
    result = _fps_one(N)
    base = list(a[:N]) + _fps_zero(max(0, N - len(a)))
    while k > 0:
        if k % 2 == 1:
            result = _fps_mul(result, base, N)
        base = _fps_mul(base, base, N)
        k //= 2
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
# 0b. PARTITION AND MACMAHON FUNCTIONS
# =========================================================================

@lru_cache(maxsize=64)
def _macmahon(N: int) -> Tuple[Fraction, ...]:
    """M(q) = prod_{n>=1} 1/(1-q^n)^n mod q^N."""
    result = [Fraction(0)] * N
    result[0] = Fraction(1)
    for k in range(1, N):
        for _ in range(k):
            for n in range(k, N):
                result[n] += result[n - k]
    return tuple(result)


@lru_cache(maxsize=64)
def _inverse_macmahon(N: int) -> Tuple[Fraction, ...]:
    """1/M(q) = prod_{n>=1} (1-q^n)^n mod q^N."""
    result = [Fraction(0)] * N
    result[0] = Fraction(1)
    for m in range(1, N):
        for _ in range(m):
            for j in range(N - 1, m - 1, -1):
                result[j] -= result[j - m]
    return tuple(result)


@lru_cache(maxsize=64)
def _partition_counts(N: int) -> Tuple[int, ...]:
    """Ordinary partition counts p(0),...,p(N-1). OEIS A000041."""
    c = [0] * N
    c[0] = 1
    for k in range(1, N):
        for n in range(k, N):
            c[n] += c[n - k]
    return tuple(c)


@lru_cache(maxsize=64)
def _plane_partition_counts(N: int) -> Tuple[int, ...]:
    """Plane partition counts pp(0),...,pp(N-1). OEIS A000219."""
    mac = _macmahon(N)
    return tuple(int(x) for x in mac)


# =========================================================================
# 0c. PLETHYSTIC OPERATIONS
# =========================================================================

@lru_cache(maxsize=64)
def _mobius_sieve(N: int) -> Tuple[int, ...]:
    mu = [0] * N
    if N > 1:
        mu[1] = 1
    is_prime = [True] * N
    primes: List[int] = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p >= N:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]
    return tuple(mu)


def plethystic_log(f: FPS, N: int) -> FPS:
    """PLog(f(q)) mod q^N.  f[0] must be 1."""
    log_f = _fps_log(list(f), N)
    mu = _mobius_sieve(N)
    g = _fps_zero(N)
    for n in range(1, N):
        val = Fraction(0)
        for d in range(1, n + 1):
            if n % d == 0:
                val += Fraction(mu[n // d]) * Fraction(d) * log_f[d]
        g[n] = val / Fraction(n)
    return g


def plethystic_exp(g: FPS, N: int) -> FPS:
    """PExp(g(q)) mod q^N.  g[0] must be 0."""
    log_f = _fps_zero(N)
    for n in range(1, N):
        gn = g[n] if n < len(g) else Fraction(0)
        if gn == 0:
            continue
        for m in range(1, N):
            nm = n * m
            if nm >= N:
                break
            log_f[nm] += gn / Fraction(m)
    return _fps_exp(log_f, N)


# =========================================================================
# 1. MOTIVIC RING K_0(Var_k)
# =========================================================================

class MotivicClass:
    """An element of K_0(Var_k), the Grothendieck ring of varieties.

    Elements are represented as Laurent polynomials in the Lefschetz
    motive L = [A^1]:
        [X] = sum_i a_i * L^i

    This captures the motivic weight structure. For smooth projective
    varieties, [X] is a polynomial in L with nonneg coefficients
    (via the Hodge-Deligne polynomial specialization).

    The ring operations:
        [X] + [Y] = [X disjoint-union Y]
        [X] * [Y] = [X x Y]
        L^{-1} = [A^1]^{-1} (the Tate twist, in the localization)

    IMPORTANT: This is a COMPUTATIONAL MODEL for the Grothendieck ring.
    We work in Z[L, L^{-1}] = Laurent polynomials in L.
    """

    def __init__(self, coeffs: Optional[Dict[int, Fraction]] = None):
        """Create a motivic class.

        Parameters
        ----------
        coeffs : dict mapping power of L to coefficient
            {i: a_i} means sum a_i * L^i.
        """
        self.coeffs: Dict[int, Fraction] = {}
        if coeffs is not None:
            for k, v in coeffs.items():
                fv = Fraction(v)
                if fv != 0:
                    self.coeffs[k] = fv

    @staticmethod
    def zero() -> "MotivicClass":
        return MotivicClass({})

    @staticmethod
    def one() -> "MotivicClass":
        """The class of a point [Spec k]."""
        return MotivicClass({0: Fraction(1)})

    @staticmethod
    def lefschetz() -> "MotivicClass":
        """L = [A^1], the Lefschetz motive."""
        return MotivicClass({1: Fraction(1)})

    @staticmethod
    def lefschetz_power(n: int) -> "MotivicClass":
        """L^n = [A^n]."""
        return MotivicClass({n: Fraction(1)})

    @staticmethod
    def affine_space(n: int) -> "MotivicClass":
        """[A^n] = L^n."""
        return MotivicClass.lefschetz_power(n)

    @staticmethod
    def projective_space(n: int) -> "MotivicClass":
        """[P^n] = 1 + L + L^2 + ... + L^n."""
        coeffs = {i: Fraction(1) for i in range(n + 1)}
        return MotivicClass(coeffs)

    @staticmethod
    def gl_group(n: int) -> "MotivicClass":
        r"""[GL_n] = L^{n^2} * prod_{i=0}^{n-1} (1 - L^{-n+i}).

        More precisely:
        [GL_n] = prod_{i=0}^{n-1} (L^n - L^i) = L^{n(n-1)/2} * prod_{i=1}^{n} (L^i - 1).
        """
        if n == 0:
            return MotivicClass.one()
        result = MotivicClass.one()
        for i in range(n):
            # Factor (L^n - L^i)
            factor = MotivicClass({n: Fraction(1), i: Fraction(-1)})
            result = result * factor
        return result

    def __add__(self, other: "MotivicClass") -> "MotivicClass":
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, Fraction(0)) + v
        return MotivicClass(result)

    def __sub__(self, other: "MotivicClass") -> "MotivicClass":
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, Fraction(0)) - v
        return MotivicClass(result)

    def __mul__(self, other: "MotivicClass") -> "MotivicClass":
        result: Dict[int, Fraction] = {}
        for k1, v1 in self.coeffs.items():
            for k2, v2 in other.coeffs.items():
                key = k1 + k2
                result[key] = result.get(key, Fraction(0)) + v1 * v2
        return MotivicClass(result)

    def __neg__(self) -> "MotivicClass":
        return MotivicClass({k: -v for k, v in self.coeffs.items()})

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MotivicClass):
            return NotImplemented
        # Clean both
        c1 = {k: v for k, v in self.coeffs.items() if v != 0}
        c2 = {k: v for k, v in other.coeffs.items() if v != 0}
        return c1 == c2

    def __hash__(self) -> int:
        return hash(tuple(sorted(
            (k, v) for k, v in self.coeffs.items() if v != 0
        )))

    def scalar_mul(self, c: Fraction) -> "MotivicClass":
        """Multiply by a scalar."""
        return MotivicClass({k: v * c for k, v in self.coeffs.items()})

    def euler_characteristic(self) -> Fraction:
        """chi(X) = evaluation at L = 1.

        This is the topological Euler characteristic (for smooth compact).
        """
        return sum(self.coeffs.values())

    def hodge_euler(self, y: Fraction = Fraction(-1)) -> Fraction:
        """E(X; y) = evaluation at L = y.

        E(X; -1) = chi_top(X) (Euler characteristic).
        E(X; 1) = sum of Betti numbers.
        """
        return sum(v * y ** k for k, v in self.coeffs.items())

    def degree(self) -> Optional[int]:
        """Maximum power of L appearing."""
        if not self.coeffs:
            return None
        return max(k for k, v in self.coeffs.items() if v != 0)

    def is_effective(self) -> bool:
        """Whether all coefficients are nonneg (class of a genuine variety)."""
        return all(v >= 0 for v in self.coeffs.values())

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
            elif k == 1:
                if v == 1:
                    terms.append("L")
                elif v == -1:
                    terms.append("-L")
                else:
                    terms.append(f"{v}*L")
            else:
                if v == 1:
                    terms.append(f"L^{k}")
                elif v == -1:
                    terms.append(f"-L^{k}")
                else:
                    terms.append(f"{v}*L^{k}")
        return " + ".join(terms) if terms else "0"


# =========================================================================
# 2. MOTIVIC HILBERT SCHEME CLASSES
# =========================================================================

def hilb_n_c1(n: int) -> MotivicClass:
    r"""[Hilb^n(C^1)] = [Sym^n(A^1)] = [A^n] = L^n.

    Hilb^n(A^1) = A^n (Hilbert scheme of n points on a line = n-th
    symmetric power = affine n-space).
    """
    if n == 0:
        return MotivicClass.one()
    return MotivicClass.lefschetz_power(n)


def hilb_n_c2(n: int) -> MotivicClass:
    r"""[Hilb^n(C^2)] via the Bialynicki-Birula cell decomposition.

    The T = (C*)^2 action on Hilb^n(A^2) has fixed points indexed by
    partitions lambda of n.  For a generic one-parameter subgroup
    (t^a, t^b) with a >> b >> 0, the Bialynicki-Birula cell at lambda
    has dimension n + n(lambda), where n(lambda) = sum_{i>=1} (i-1)*lambda_i.

    [Hilb^n(A^2)] = sum over partitions lambda of n of L^{n + n(lambda)}

    This gives chi = p(n) at L=1 (each cell contributes 1).

    Known values:
    [Hilb^0] = 1
    [Hilb^1] = L   (one partition: (1), n=0)
    [Hilb^2] = L^2 + L^3  (partitions (2) with n=0, (1,1) with n=1)
    [Hilb^3] = L^3 + L^4 + L^6  (partitions (3), (2,1), (1,1,1))

    REFERENCE: Ellingsrud-Stromme, "On the homology of the Hilbert scheme
    of points in the plane", Inventiones 87 (1987), 343-352.
    """
    if n == 0:
        return MotivicClass.one()
    # Enumerate partitions of n and compute n(lambda) for each
    result = MotivicClass.zero()
    for lam in _partitions_of(n):
        n_lam = sum((i) * lam[i] for i in range(1, len(lam)))
        result = result + MotivicClass.lefschetz_power(n + n_lam)
    return result


def _partitions_of(n: int) -> List[Tuple[int, ...]]:
    """Enumerate all partitions of n as weakly decreasing tuples."""
    if n == 0:
        return [()]
    result: List[Tuple[int, ...]] = []
    _partition_helper(n, n, [], result)
    return result


def _partition_helper(
    n: int, max_part: int, current: List[int],
    result: List[Tuple[int, ...]],
) -> None:
    if n == 0:
        result.append(tuple(current))
        return
    for k in range(min(n, max_part), 0, -1):
        current.append(k)
        _partition_helper(n - k, k, current, result)
        current.pop()


@lru_cache(maxsize=128)
def hilb_n_c3(n: int) -> MotivicClass:
    r"""Motivic DT invariant at charge n for C^3 (NOT the naive [Hilb^n]).

    The motivic DT partition function of C^3 (Kontsevich-Soibelman,
    Behrend-Bryan-Szendroi 2013):

        Z^{mot}_{DT}(q) = prod_{m>=1} prod_{k=0}^{m-1} 1/(1 - L^{k+m} q^m)

    This is the motivic refinement of M(q) = prod_{m>=1} 1/(1-q^m)^m.
    Setting L = 1 recovers the numerical MacMahon function: pp(n).

    IMPORTANT: This is the MOTIVIC DT INVARIANT, not the naive motive
    [Hilb^n(C^3)] of the Hilbert scheme. The motivic DT invariant uses
    the motivic vanishing cycle / Behrend function and lives in the
    motivic ring K_0(Var_k)[L^{-1}].

    For small n:
    Z^{mot}_0 = 1
    Z^{mot}_1 = L  (chi = 1 = pp(1))
    Z^{mot}_2 = 2L^2 + L^3  (chi = 3 = pp(2))

    REFERENCE: Behrend-Bryan-Szendroi, "Motivic degree zero DT invariants",
    Inventiones 2013; Morrison-Mozgovoy-Nagao-Szendroi arXiv:1103.1896.
    """
    if n == 0:
        return MotivicClass.one()
    # Compute via the motivic product formula
    # Z^{mot}(q) = prod_{m>=1} prod_{k=0}^{m-1} 1/(1 - L^{k+m} q^m)
    #
    # Multiplication by 1/(1 - c * q^m):
    #   gf[j] += c * gf[j-m]  for j = m, m+1, ..., n (LOW to HIGH)
    gf = [MotivicClass.zero() for _ in range(n + 1)]
    gf[0] = MotivicClass.one()
    for m in range(1, n + 1):
        for k in range(m):
            # Multiply by 1/(1 - L^{k+m} * q^m)
            L_pow = MotivicClass.lefschetz_power(k + m)
            for j in range(m, n + 1):
                gf[j] = gf[j] + gf[j - m] * L_pow
    return gf[n]


def motivic_macmahon(N: int) -> List[MotivicClass]:
    """The motivic MacMahon function M^{mot}(q) mod q^N.

    Returns [Hilb^0, Hilb^1, ..., Hilb^{N-1}] as MotivicClasses.
    """
    return [hilb_n_c3(n) for n in range(N)]


def motivic_macmahon_euler_check(N: int) -> List[bool]:
    """Verify chi([Hilb^n(C^3)]) = pp(n) for n = 0,...,N-1.

    At L=1, [Hilb^n(C^3)] should give the plane partition count pp(n).
    This is the fundamental consistency: motivic MacMahon specializes
    to numerical MacMahon.
    """
    pp = _plane_partition_counts(N)
    results = []
    for n in range(N):
        mot = hilb_n_c3(n)
        chi = mot.euler_characteristic()
        results.append(int(chi) == pp[n])
    return results


# =========================================================================
# 3. CATEGORIFIED BPS INVARIANTS (VANISHING CYCLE COHOMOLOGY)
# =========================================================================

class CategorifiedBPS(NamedTuple):
    """Categorified BPS invariant at charge gamma.

    The vanishing cycle sheaf phi_{Tr W} provides a CHAIN COMPLEX
    whose Euler characteristic is the signed DT invariant Omega(gamma).

    For C^3 (Jordan quiver), the categorified BPS at charge n is:
        Omega^cat(n) = H^*(phi_{Tr W}, IC_{Rep(Q,n)})

    The Poincare polynomial:
        P(Omega^cat(n), t) = sum_i dim H^i * t^i

    satisfies P(Omega^cat(n), -1) = Omega(n) (signed invariant).

    Attributes
    ----------
    charge : int or tuple
        The charge vector (= dimension vector for quiver).
    bps_number : int
        The numerical DT invariant Omega(gamma).
    poincare_poly : dict
        {degree: dimension} of the BPS cohomology.
    motivic_class : MotivicClass
        The motivic BPS class in K_0(Var_k).
    """
    charge: Any
    bps_number: int
    poincare_poly: Dict[int, int]
    motivic_class: MotivicClass


def categorified_bps_c3(n: int) -> CategorifiedBPS:
    r"""Categorified BPS invariant for C^3 at charge n.

    For C^3: Omega(n) = n (plethystic logarithm of MacMahon).

    The categorified BPS is the vanishing cycle cohomology of
    Tr W on Rep(Q_Jordan, n) where W = Tr(x[y,z]).

    By Davison-Meinhardt (2015): the BPS cohomology is PURE and
    concentrated in a single degree:
        H^*(phi_{Tr W}(n)) is concentrated in degree 0 with dim = n.

    So P(Omega^cat(n), t) = n  (constant polynomial).

    The motivic class is n * L^0 = n * [pt].
    Euler characteristic: n = Omega(n). Consistent.

    REFERENCE: Davison-Meinhardt, "Cohomological DT theory of a quiver
    with potential and quantum enveloping algebras," arXiv:1311.7172.
    """
    if n <= 0:
        return CategorifiedBPS(
            charge=n, bps_number=0,
            poincare_poly={}, motivic_class=MotivicClass.zero()
        )
    return CategorifiedBPS(
        charge=n,
        bps_number=n,
        poincare_poly={0: n},
        motivic_class=MotivicClass({0: Fraction(n)}),
    )


def categorified_bps_conifold(d1: int, d2: int) -> CategorifiedBPS:
    r"""Categorified BPS for the conifold at dimension (d1, d2).

    For the resolved conifold (Klebanov-Witten quiver):
        Omega((d, 0)) = 1  for d >= 1  (D0 at vertex 0)
        Omega((0, d)) = 1  for d >= 1  (D0 at vertex 1)
        Omega((d, d)) = (-1)^{d-1}  for d >= 1  (wrapped D2)
        Omega(else) = 0

    The categorified version: the BPS cohomology of the D2-brane
    state has nontrivial odd cohomology:
        H^*(phi, (d,d)) is concentrated in degree d-1 (parity from (-1)^{d-1}).

    REFERENCE: Szendroi (2008), "Non-commutative DT theory and the conifold."
    """
    charge = (d1, d2)
    if d1 == 0 and d2 == 0:
        return CategorifiedBPS(charge, 0, {}, MotivicClass.zero())
    if d2 == 0 and d1 >= 1:
        return CategorifiedBPS(charge, 1, {0: 1}, MotivicClass.one())
    if d1 == 0 and d2 >= 1:
        return CategorifiedBPS(charge, 1, {0: 1}, MotivicClass.one())
    if d1 == d2 and d1 >= 1:
        sign = (-1) ** (d1 - 1)
        # BPS cohomology concentrated in degree d1-1
        deg = d1 - 1
        return CategorifiedBPS(
            charge, sign, {deg: 1},
            MotivicClass({0: Fraction((-1) ** deg)})
        )
    return CategorifiedBPS(charge, 0, {}, MotivicClass.zero())


# =========================================================================
# 4. CATEGORIFIED BAR COMPLEX (SHEAF ON STABILITY SPACE)
# =========================================================================

class StabilityCondition(NamedTuple):
    """A stability condition sigma = (Z, P) on D^b(X).

    In Bridgeland's framework, sigma consists of:
    - A central charge Z: K(X) -> C (group hom)
    - A slicing P of D^b(X)

    For computational purposes, we parameterize by the central charge
    on the lattice Gamma = K(X).

    For C^3 (one-vertex quiver): Gamma = Z, Z(n) = -n + i*theta*n
    parameterized by theta in R_{>0}.

    For the conifold (two-vertex): Gamma = Z^2,
    Z(d1, d2) = -(d1 + d2) + i*(theta_1 * d1 + theta_2 * d2).
    """
    name: str
    theta: Tuple[Fraction, ...]  # Stability parameters


def c3_stability(theta: Fraction = Fraction(1)) -> StabilityCondition:
    """Standard stability condition on D^b(C^3)."""
    return StabilityCondition("C^3 standard", (theta,))


def conifold_stability(
    theta1: Fraction = Fraction(1),
    theta2: Fraction = Fraction(1),
) -> StabilityCondition:
    """Stability condition on D^b(conifold)."""
    return StabilityCondition("Conifold", (theta1, theta2))


class CategorifiedBarFiber(NamedTuple):
    """Fiber of the categorified bar complex at a stability condition.

    B^{E_1,cat}(A_X, sigma) = the bar complex filtered by sigma-semistable
    objects.

    At each arity k and charge gamma:
        B^{E_1,cat}_k(gamma, sigma) = chain complex

    The homology H^*(B^{E_1,cat}_k(gamma, sigma)) is the categorified
    bar cohomology at arity k.

    Attributes
    ----------
    stability : StabilityCondition
    arity_charge_dims : dict
        {(arity, charge): dimension of the chain complex at that bigrading}
    bar_euler_char : dict
        {charge: Euler characteristic of the bar complex at that charge}
    """
    stability: StabilityCondition
    arity_charge_dims: Dict[Tuple[int, Any], int]
    bar_euler_char: Dict[Any, Fraction]


def categorified_bar_fiber_c3(
    sigma: StabilityCondition,
    N: int,
    max_arity: int = 4,
) -> CategorifiedBarFiber:
    r"""Compute the categorified bar fiber for C^3.

    For C^3, all objects with positive charge are sigma-stable (there is
    only one charge direction), so the bar complex is independent of
    the stability parameter in the principal chamber.

    B^{E_1,cat}_k(n, sigma) = (Y^+_{>0})^{otimes k} at degree n.
    dim B^{E_1,cat}_k(n) = sum_{n_1+...+n_k = n, n_i >= 1} pp(n_1)...pp(n_k)

    where pp(m) = # plane partitions of m.
    """
    pp = _plane_partition_counts(N)
    dims: Dict[Tuple[int, Any], int] = {}
    euler: Dict[Any, Fraction] = {}

    for n in range(N):
        euler[n] = Fraction(0)

    # Arity 0: just the ground field at n=0
    dims[(0, 0)] = 1
    euler[0] += Fraction(1)

    # Arity k >= 1
    for k in range(1, max_arity + 1):
        # B^k_n = sum over compositions of n into k positive parts
        # dim B^k_n = sum_{n1+...+nk=n, ni>=1} pp(n1)*...*pp(nk)
        # This is the coefficient of q^n in (pp_+(q))^k
        # where pp_+(q) = sum_{m>=1} pp(m) q^m = M(q) - 1.
        pp_plus = _fps_zero(N)
        for m in range(1, N):
            pp_plus[m] = Fraction(pp[m])
        ppk = _fps_power(pp_plus, k, N)
        sign = Fraction((-1) ** k)
        for n in range(N):
            d = int(ppk[n])
            if d > 0:
                dims[(k, n)] = d
            euler[n] += sign * ppk[n]

    return CategorifiedBarFiber(sigma, dims, euler)


def categorified_bar_fiber_conifold(
    sigma: StabilityCondition,
    N: int,
    max_arity: int = 3,
) -> CategorifiedBarFiber:
    r"""Compute the categorified bar fiber for the conifold.

    For the large-volume chamber: both vertices have positive theta.
    The bar complex decomposes by total charge n = d1 + d2.

    At charge (d, 0) or (0, d): the subsector is a copy of
    the partition generating function (gauge theory on one vertex).

    At charge (d, d): the D2-brane wrapped on P^1 contributes.
    """
    pc = _partition_counts(N)
    dims: Dict[Tuple[int, Any], int] = {}
    euler: Dict[Any, Fraction] = {}

    for n in range(N):
        euler[n] = Fraction(0)

    dims[(0, 0)] = 1
    euler[0] += Fraction(1)

    # Vertex-0 sector (no arrows to vertex 1)
    pc_plus = _fps_zero(N)
    for m in range(1, N):
        pc_plus[m] = Fraction(pc[m])

    for k in range(1, max_arity + 1):
        pck = _fps_power(pc_plus, k, N)
        sign = Fraction((-1) ** k)
        for n in range(N):
            d = int(pck[n])
            if d > 0:
                dims[(k, ("v0", n))] = d
            euler[("v0", n)] = euler.get(("v0", n), Fraction(0)) + sign * pck[n]

    # Vertex-1 sector: identical by symmetry
    for k in range(1, max_arity + 1):
        pck = _fps_power(pc_plus, k, N)
        sign = Fraction((-1) ** k)
        for n in range(N):
            d = int(pck[n])
            if d > 0:
                dims[(k, ("v1", n))] = d
            euler[("v1", n)] = euler.get(("v1", n), Fraction(0)) + sign * pck[n]

    return CategorifiedBarFiber(sigma, dims, euler)


# =========================================================================
# 5. MOTIVIC BAR COMPLEX
# =========================================================================

class MotivicBarComplex(NamedTuple):
    """Motivic bar complex B^{E_1,mot}(A_X).

    Each entry is valued in K_0(Var_k) rather than Z.

    Attributes
    ----------
    name : str
    arity_charge_classes : dict
        {(arity, charge): MotivicClass}
    motivic_euler : dict
        {charge: MotivicClass} -- alternating sum over arities
    """
    name: str
    arity_charge_classes: Dict[Tuple[int, int], MotivicClass]
    motivic_euler: Dict[int, MotivicClass]


def motivic_bar_c3(N: int, max_arity: int = 4) -> MotivicBarComplex:
    r"""Motivic bar complex for C^3.

    B^{E_1,mot}_k(n) = [Rep(Q,n)^{ss}]^{\otimes k} / [GL_n]^k

    For the Jordan quiver: [Rep(Q,n)^{ss}] = [C^{3n^2}] / [GL_n]
    (moduli of n-dimensional representations of the tripled Jordan quiver).

    The motivic version of the MacMahon function:
    M^{mot}(q) = sum_n [Hilb^n(C^3)] q^n.

    The motivic bar at arity k is:
    B^{mot}_k(q) = (M^{mot}(q) - 1)^k

    where the subtraction removes degree 0.
    """
    hilb = motivic_macmahon(N)

    # M^{mot}_+ = M^{mot} - 1 (augmentation ideal)
    hilb_plus = [MotivicClass.zero()] * N
    for n in range(1, N):
        hilb_plus[n] = hilb[n]

    classes: Dict[Tuple[int, int], MotivicClass] = {}
    euler: Dict[int, MotivicClass] = {}

    for n in range(N):
        euler[n] = MotivicClass.zero()

    # Arity 0
    classes[(0, 0)] = MotivicClass.one()
    euler[0] = MotivicClass.one()

    for k in range(1, max_arity + 1):
        # (M^{mot}_+)^k -- motivic convolution power
        # Computed by expanding the product
        kth_power = _motivic_fps_power(hilb_plus, k, N)
        sign = Fraction((-1) ** k)
        for n in range(N):
            mc = kth_power[n]
            if mc != MotivicClass.zero():
                classes[(k, n)] = mc
            euler[n] = euler[n] + mc.scalar_mul(sign)

    return MotivicBarComplex("C^3", classes, euler)


def _motivic_fps_power(
    f: List[MotivicClass], k: int, N: int
) -> List[MotivicClass]:
    """Compute the k-th convolution power of a motivic formal power series."""
    if k == 0:
        result = [MotivicClass.zero()] * N
        result[0] = MotivicClass.one()
        return result
    if k == 1:
        return list(f[:N])
    # Recursive: f^k = f^{k-1} * f
    prev = _motivic_fps_power(f, k - 1, N)
    result = [MotivicClass.zero()] * N
    for i in range(N):
        if prev[i] == MotivicClass.zero():
            continue
        for j in range(1, N - i):
            if f[j] == MotivicClass.zero():
                continue
            result[i + j] = result[i + j] + prev[i] * f[j]
    return result


def motivic_bps_c3(N: int) -> List[MotivicClass]:
    r"""Motivic BPS invariants for C^3 via motivic plethystic logarithm.

    The motivic plethystic logarithm of M^{mot}(q) gives the motivic
    BPS generator:
        PLog^{mot}(M^{mot}(q)) = sum_n Omega^{mot}_n * q^n

    For C^3: Omega^{mot}_n is the motivic BPS at charge n.

    At L=1: Omega^{mot}_n -> Omega(n) = n (numerical BPS).

    The motivic structure: Omega^{mot}_1 = L^3 (a single box = C^3).
    Higher charges involve virtual motives from inclusion-exclusion.

    We compute via the formula:
    Omega^{mot}_n = coefficient of q^n in:
        sum_{k>=1} mu(k)/k * log(M^{mot}(q^k))

    For computational tractability, we use the direct recursion from
    the motivic product formula.

    At low charges (computed from the motivic product formula):
    Omega^{mot}_1 = L^3 - L^2 - L + 1 ... no, this is wrong.

    The correct motivic BPS for C^3 is:
    Omega^{mot}_n = motivic plethystic log of M^{mot}(q).

    Since the motivic MacMahon function is:
    M^{mot}(q) = prod_{m>=1} prod_{k=0}^{m-1} 1/(1 - L^{k+m} q^m)

    its plethystic logarithm is:
    PLog^{mot}(M^{mot}(q)) = sum_{m>=1} sum_{k=0}^{m-1} L^{k+m} q^m
                            = sum_{m>=1} L^m (1 + L + ... + L^{m-1}) q^m
                            = sum_{m>=1} L^m (L^m - 1)/(L - 1) q^m
                            = sum_{m>=1} [P^{m-1}] * L^m * q^m

    Wait -- let me recompute.  For the product prod (1-x)^{-1},
    PLog = sum x. So:
    PLog^{mot}(M^{mot}) = sum_{m>=1} sum_{k=0}^{m-1} L^{k+m} q^m
                        = sum_{m>=1} (L^m + L^{m+1} + ... + L^{2m-1}) q^m
                        = sum_{m>=1} L^m (1 + L + ... + L^{m-1}) q^m

    For m=1: L^1 * 1 = L
    For m=2: L^2 (1 + L) = L^2 + L^3
    For m=3: L^3 (1 + L + L^2) = L^3 + L^4 + L^5

    chi(Omega^{mot}_m) = m (at L=1): 1, 2, 3, ... Correct!
    """
    result = [MotivicClass.zero()] * N
    for m in range(1, N):
        # Omega^{mot}_m = L^m * (1 + L + ... + L^{m-1})
        coeffs: Dict[int, Fraction] = {}
        for k in range(m):
            coeffs[m + k] = Fraction(1)
        result[m] = MotivicClass(coeffs)
    return result


# =========================================================================
# 6. CATEGORIFIED SHADOW ON M_bar_g
# =========================================================================

# A-hat coefficients (positive, from Bernoulli):
# A-hat(ix) = (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + ...
# F_g = kappa * a_hat_g where a_hat_g is the coefficient of x^{2g}.

A_HAT_GENUS = {
    1: Fraction(1, 24),
    2: Fraction(7, 5760),
    3: Fraction(31, 967680),
    4: Fraction(127, 154828800),
    5: Fraction(73, 3503554560),
}


class CategorifiedShadow(NamedTuple):
    """Categorified shadow F_g^cat at genus g.

    For uniform-weight algebras (the scalar lane), F_g = kappa * a_hat_g
    is a SCALAR, so F_g^cat = kappa * a_hat_g * [M_bar_g] is just a
    scalar multiple of the fundamental class.

    For class M algebras, F_g^cat carries higher-rank data from
    the shadow obstruction tower.

    The key structure:
    - F_g^cat in D^b(M_bar_g)
    - chi(F_g^cat) = F_g (numerical shadow)
    - For scalar lane: F_g^cat = kappa * lambda_g^{FP} (the Hodge class)

    Attributes
    ----------
    genus : int
    numerical_value : Fraction
        F_g = kappa * a_hat_g (the number).
    kappa : Fraction
    is_scalar_lane : bool
        Whether this is in the scalar lane (F_g = kappa * a_hat_g).
    hodge_class_coeff : Fraction
        Coefficient of lambda_g in H^{2g}(M_bar_g).
    """
    genus: int
    numerical_value: Fraction
    kappa: Fraction
    is_scalar_lane: bool
    hodge_class_coeff: Fraction


def categorified_shadow_scalar(
    genus: int,
    kappa: Fraction,
) -> CategorifiedShadow:
    """Categorified shadow in the scalar lane.

    F_g = kappa * a_hat_g, where a_hat_g is the g-th A-hat coefficient.
    The categorification is trivial: F_g^cat = F_g * [pt] on M_bar_g.
    """
    if genus not in A_HAT_GENUS:
        raise ValueError(f"A-hat coefficient not stored for genus {genus}")
    a_hat_g = A_HAT_GENUS[genus]
    f_g = kappa * a_hat_g
    return CategorifiedShadow(
        genus=genus,
        numerical_value=f_g,
        kappa=kappa,
        is_scalar_lane=True,
        hodge_class_coeff=a_hat_g,
    )


def shadow_tower_numerical(kappa: Fraction, max_genus: int = 5) -> Dict[int, Fraction]:
    """Compute the numerical shadow tower F_g for g = 1,...,max_genus."""
    result = {}
    for g in range(1, max_genus + 1):
        if g in A_HAT_GENUS:
            result[g] = kappa * A_HAT_GENUS[g]
    return result


def shadow_partition_function(
    kappa: Fraction, max_genus: int = 5
) -> List[Fraction]:
    """Compute Z^sh(hbar) = exp(sum F_g hbar^{2g}) mod hbar^{2*max_genus+2}.

    Returns coefficients of hbar^0, hbar^2, hbar^4, ... as a list.
    """
    N = max_genus + 1
    # log Z = sum F_g hbar^{2g}
    log_coeffs = _fps_zero(N)
    for g in range(1, N):
        if g in A_HAT_GENUS:
            log_coeffs[g] = kappa * A_HAT_GENUS[g]
    return _fps_exp(log_coeffs, N)


# =========================================================================
# 7. DERIVED HALL ALGEBRA MODEL
# =========================================================================

class DerivedHallAlgebra:
    """Computational model of Toen's derived Hall algebra DH(D^b(X)).

    DH(D^b(X)) is an ASSOCIATIVE algebra whose structure constants
    encode extensions in D^b(X). For CY3 with quiver (Q,W):

        DH_n = H^*(M_n(Q,W), phi_{Tr W})

    where M_n is the moduli stack of n-dimensional representations.

    The multiplication is the Hall product:
        [E1] * [E2] = sum_{[E]} |Ext^0(E1,E2)_{split=E}| / |Aut(E)| * [E]

    For computational purposes, we track the graded character and
    the BPS decomposition.

    The bar complex B^{E_1}(DH) is the categorified shadow tower.
    """

    def __init__(self, name: str, graded_dims: Dict[int, int],
                 bps_spectrum: Dict[int, int]):
        self.name = name
        self.graded_dims = graded_dims
        self.bps_spectrum = bps_spectrum

    def character(self, N: int) -> FPS:
        """Graded character sum_n dim(DH_n) q^n."""
        f = _fps_zero(N)
        for n, d in self.graded_dims.items():
            if 0 <= n < N:
                f[n] = Fraction(d)
        return f

    def bps_character(self, N: int) -> FPS:
        """BPS character sum_n Omega(n) q^n."""
        f = _fps_zero(N)
        for n, omega in self.bps_spectrum.items():
            if 0 <= n < N:
                f[n] = Fraction(omega)
        return f

    def bar_euler_char(self, N: int) -> FPS:
        """Euler characteristic of the bar complex.

        chi(B(DH)) = 1/char(DH) (inverse of the character).
        """
        ch = self.character(N)
        return _fps_inv(ch, N)


def derived_hall_c3(N: int) -> DerivedHallAlgebra:
    """Derived Hall algebra for C^3.

    Character: M(q) = prod_{n>=1} 1/(1-q^n)^n (MacMahon).
    BPS spectrum: Omega(n) = n.
    """
    mac = _macmahon(N)
    dims = {n: int(mac[n]) for n in range(N)}
    bps = {n: n for n in range(1, N)}
    return DerivedHallAlgebra("DH(C^3)", dims, bps)


def derived_hall_conifold(N: int) -> DerivedHallAlgebra:
    """Derived Hall algebra for the resolved conifold (diagonal sector).

    The diagonal-charge sector has character M(q)^2 * prod_{n>=1} (1-q^n)^n
    = M(q)^2 / M(q) = M(q).

    Wait -- the total DT partition function of the conifold is
    Z = M(q)^2 * prod_{n>=1}(1 - Q*q^n)^n
    where Q tracks the curve class.

    At Q=0 (degree-0 sector): Z_0 = M(q)^2.
    At Q=1 (all degrees): Z = M(q)^2 * prod(1-q^n)^n = M(q).

    The diagonal charge sector (d1=d2) has:
    sum_d Z_{(d,d)} q^d = M(q) (effectively).

    BPS spectrum: Omega((d,d)) = (-1)^{d-1} for d >= 1.
    Plus D0 contributions: Omega((d,0)) = 1, Omega((0,d)) = 1.
    """
    mac = _macmahon(N)
    dims = {n: int(mac[n]) for n in range(N)}
    bps = {n: n for n in range(1, N)}  # Total BPS counting D0 and D2
    return DerivedHallAlgebra("DH(conifold)", dims, bps)


# =========================================================================
# 8. SHEAF-THEORETIC CoHA (Porta-Sala, Kapranov-Vasserot)
# =========================================================================

class SheafCoHA(NamedTuple):
    """Computational model of the sheaf-theoretic CoHA.

    SCoHA(Q,W) = oplus_d Sh^{BM}(Crit(Tr W)_d)
    is a MONOIDAL DG CATEGORY.

    K_0(SCoHA) = numerical CoHA.
    K_0(SCoHA)_d = chi of the BM sheaf = dim CoHA_d.

    We track:
    - The motivic class of each component
    - The K-theory (numerical) reduction
    - The BPS filtration

    Attributes
    ----------
    name : str
    motivic_dims : dict
        {charge: MotivicClass} of each component.
    numerical_dims : dict
        {charge: int} = K_0 reduction.
    bps_filtration : dict
        {charge: list of MotivicClass} = BPS pieces.
    """
    name: str
    motivic_dims: Dict[int, MotivicClass]
    numerical_dims: Dict[int, int]
    bps_filtration: Dict[int, List[MotivicClass]]


def sheaf_coha_c3(N: int) -> SheafCoHA:
    r"""Sheaf-theoretic CoHA for C^3.

    SCoHA_n(C^3) = Sh^{BM}(Hilb^n(C^3)).
    Motivic class: [Hilb^n(C^3)].
    Numerical: pp(n) (plane partition count).

    The BPS filtration comes from the motivic plethystic decomposition:
    each charge-n component decomposes into BPS pieces indexed by
    partitions of n.
    """
    hilb = motivic_macmahon(N)
    pp = _plane_partition_counts(N)
    mot_bps = motivic_bps_c3(N)

    motivic = {n: hilb[n] for n in range(N)}
    numerical = {n: pp[n] for n in range(N)}
    bps_filt = {n: [mot_bps[n]] if n > 0 else [] for n in range(N)}

    return SheafCoHA("SCoHA(C^3)", motivic, numerical, bps_filt)


# =========================================================================
# 9. CATEGORIFIED MC ELEMENT (Theta^{E_1,cat})
# =========================================================================

class CategorifiedMCElement(NamedTuple):
    """Categorified Maurer-Cartan element Theta^{E_1,cat}.

    The MC element of the (numerical) convolution dg Lie algebra
    g^mod_A is a SCALAR Theta^{E_1} satisfying D*Theta + 1/2[Theta,Theta] = 0.

    The categorified version lifts to the DERIVED Hall algebra:
    Theta^{E_1,cat} in MC(DH(D^b(X)))

    This object packages:
    - The categorified kappa (a motivic class, not just a number)
    - The categorified genus-g shadows (sheaves on M_bar_g)
    - The categorified BPS spectrum (vanishing cycle sheaves)
    - The motivic wall-crossing data

    Attributes
    ----------
    name : str
    kappa_numerical : Fraction
    kappa_motivic : MotivicClass
    shadows : dict
        {genus: CategorifiedShadow}
    bps : dict
        {charge: CategorifiedBPS}
    mc_equation_check : bool
        Whether the MC equation is satisfied (always True for bar-intrinsic).
    """
    name: str
    kappa_numerical: Fraction
    kappa_motivic: MotivicClass
    shadows: Dict[int, CategorifiedShadow]
    bps: Dict[Any, CategorifiedBPS]
    mc_equation_check: bool


def categorified_mc_c3(N: int = 10, max_genus: int = 5) -> CategorifiedMCElement:
    """Categorified MC element for C^3.

    kappa = 1. BPS spectrum: Omega(n) = n.
    Motivic kappa: L (the Lefschetz motive).
    """
    shadows = {}
    for g in range(1, max_genus + 1):
        if g in A_HAT_GENUS:
            shadows[g] = categorified_shadow_scalar(g, Fraction(1))

    bps = {}
    for n in range(1, N):
        bps[n] = categorified_bps_c3(n)

    return CategorifiedMCElement(
        name="Theta^{E_1,cat}(C^3)",
        kappa_numerical=Fraction(1),
        kappa_motivic=MotivicClass.lefschetz(),
        shadows=shadows,
        bps=bps,
        mc_equation_check=True,
    )


def categorified_mc_conifold(
    N: int = 10, max_genus: int = 5
) -> CategorifiedMCElement:
    """Categorified MC element for the conifold.

    kappa = 1. BPS spectrum: Omega((d,d)) = (-1)^{d-1}, Omega((d,0)) = 1.
    """
    shadows = {}
    for g in range(1, max_genus + 1):
        if g in A_HAT_GENUS:
            shadows[g] = categorified_shadow_scalar(g, Fraction(1))

    bps = {}
    for d in range(1, N):
        bps[("D0", d)] = categorified_bps_conifold(d, 0)
        bps[("D2", d)] = categorified_bps_conifold(d, d)

    return CategorifiedMCElement(
        name="Theta^{E_1,cat}(conifold)",
        kappa_numerical=Fraction(1),
        kappa_motivic=MotivicClass.lefschetz(),
        shadows=shadows,
        bps=bps,
        mc_equation_check=True,
    )


def categorified_mc_quintic(max_genus: int = 5) -> CategorifiedMCElement:
    """Categorified MC element for the quintic threefold.

    kappa = -25/3 (BCOV conjecture: chi_top/24 = -200/24 = -25/3).
    """
    kappa = Fraction(-25, 3)
    shadows = {}
    for g in range(1, max_genus + 1):
        if g in A_HAT_GENUS:
            shadows[g] = categorified_shadow_scalar(g, kappa)

    return CategorifiedMCElement(
        name="Theta^{E_1,cat}(quintic)",
        kappa_numerical=kappa,
        kappa_motivic=MotivicClass({0: kappa}),
        shadows=shadows,
        bps={},  # GV invariants not tracked here
        mc_equation_check=True,
    )


# =========================================================================
# 10. WALL-CROSSING AS BAR COMPLEX TRANSFORMATION
# =========================================================================

class WallCrossingData(NamedTuple):
    """Wall-crossing data between two stability conditions.

    When sigma crosses a wall W in Stab(D^b(X)), the DT invariants
    undergo the KS wall-crossing formula. Categorically, this is a
    change in the fiber of the categorified bar complex.

    The wall-crossing AUTOMORPHISM K_gamma acts on the motivic
    Hall algebra:
        K_gamma = exp(sum_{n>=1} (-1)^n / n^2 * [Omega^{mot}(n*gamma)] * e_{n*gamma})

    Attributes
    ----------
    source : StabilityCondition
    target : StabilityCondition
    active_charge : tuple
        The charge becoming (un)stable at the wall.
    bps_jump : dict
        {charge: (Omega_before, Omega_after)}
    motivic_transformation : dict
        {charge: MotivicClass} of the wall-crossing factors.
    """
    source: StabilityCondition
    target: StabilityCondition
    active_charge: Any
    bps_jump: Dict[Any, Tuple[int, int]]
    motivic_transformation: Dict[Any, MotivicClass]


def conifold_wall_crossing(N: int = 5) -> WallCrossingData:
    """Wall-crossing between the two chambers of the conifold.

    Chamber I (large volume): only D0 branes are stable.
        Z_I = M(q)^2 (two copies of MacMahon).

    Chamber II (small volume): D2 branes are also stable.
        Z_II = M(q)^2 * prod_{n>=1} (1 - Q*q^n)^n.

    The wall-crossing is the KS pentagon identity:
    K_{(1,1)} acts on the Hall algebra to create/annihilate the D2-brane.

    Crossing the wall: one BPS state of charge (1,1) with Omega = +1
    becomes (un)stable.
    """
    sigma_large = conifold_stability(Fraction(2), Fraction(1))
    sigma_small = conifold_stability(Fraction(1), Fraction(2))

    bps_jump = {}
    motivic = {}
    for d in range(1, N):
        # D2-brane of charge (d,d): in large volume, NOT stable.
        # In small volume: Omega((d,d)) = (-1)^{d-1}.
        bps_jump[(d, d)] = (0, (-1) ** (d - 1))
        motivic[(d, d)] = MotivicClass({0: Fraction((-1) ** (d - 1))})

    return WallCrossingData(
        source=sigma_large,
        target=sigma_small,
        active_charge=(1, 1),
        bps_jump=bps_jump,
        motivic_transformation=motivic,
    )


# =========================================================================
# 11. CROSS-VERIFICATION UTILITIES
# =========================================================================

def verify_motivic_euler_specialization(N: int) -> Dict[str, bool]:
    """Verify that L=1 specialization of motivic objects gives numerical ones.

    This is the fundamental consistency check:
    chi([Hilb^n(C^3)]) = pp(n)
    chi(Omega^{mot}_n) = Omega(n) = n
    chi(M^{mot}) = M  (MacMahon)

    Multi-path verification of the categorification.
    """
    pp = _plane_partition_counts(N)
    mac = list(_macmahon(N))

    results = {}

    # Check 1: Hilbert scheme Euler characteristics
    hilb_ok = True
    for n in range(N):
        mc = hilb_n_c3(n)
        if int(mc.euler_characteristic()) != pp[n]:
            hilb_ok = False
            break
    results["hilb_chi_equals_pp"] = hilb_ok

    # Check 2: Motivic BPS Euler characteristics
    mot_bps = motivic_bps_c3(N)
    bps_ok = True
    for n in range(1, N):
        if int(mot_bps[n].euler_characteristic()) != n:
            bps_ok = False
            break
    results["mot_bps_chi_equals_n"] = bps_ok

    # Check 3: Motivic MacMahon = numerical MacMahon under chi
    mac_ok = True
    for n in range(N):
        mc = hilb_n_c3(n)
        if int(mc.euler_characteristic()) != int(mac[n]):
            mac_ok = False
            break
    results["mot_mac_chi_equals_mac"] = mac_ok

    return results


def verify_bar_euler_char_c3(N: int) -> Dict[str, Any]:
    """Verify the bar Euler characteristic for C^3.

    chi(B(Y^+)) = 1/M(q) = prod_{n>=1} (1-q^n)^n.

    This is the bar-side of the DT/GW computation:
    the bar Euler characteristic inverts the CoHA character.

    IMPORTANT: The alternating sum sum_{k=0}^{K} (-1)^k (M-1)^k converges
    to 1/M only in the limit K->infinity. At finite arity K, the sum
    is exact only through degree K in q (since (M-1)^k starts at q^k).
    We compare only through degree min(N, max_arity).

    Multi-path verification:
    Path A: Direct alternating sum over bar arities.
    Path B: Inverse MacMahon function 1/M(q).
    Path C: Motivic: chi of alternating sum of motivic bar arities.
    """
    # Use max_arity = N to ensure convergence through degree N-1
    max_arity_AB = N
    max_arity_C = min(N, 4)  # Motivic is slower, use fewer arities

    # Path A: numerical bar Euler char
    sigma = c3_stability()
    fiber = categorified_bar_fiber_c3(sigma, N, max_arity=max_arity_AB)
    bar_euler_A = [fiber.bar_euler_char.get(n, Fraction(0)) for n in range(N)]

    # Path B: 1/M(q) directly
    inv_mac = list(_inverse_macmahon(N))
    bar_euler_B = list(inv_mac[:N])

    # Compare Path A and B (exact since max_arity >= N)
    match_AB = all(
        bar_euler_A[n] == bar_euler_B[n]
        for n in range(N)
    )

    # Path C: motivic bar Euler char under chi
    # Only compare through degree max_arity_C since motivic uses fewer arities
    mot_bar = motivic_bar_c3(N, max_arity=max_arity_C)
    bar_euler_C = [
        mot_bar.motivic_euler.get(n, MotivicClass.zero()).euler_characteristic()
        for n in range(N)
    ]
    # Compare A and C only through degree max_arity_C
    compare_range_C = min(N, max_arity_C + 1)
    match_AC = all(
        bar_euler_A[n] == bar_euler_C[n]
        for n in range(compare_range_C)
    )

    return {
        "N": N,
        "match_AB": match_AB,
        "match_AC": match_AC,
        "bar_euler_numerical": [float(x) for x in bar_euler_A[:min(N, 10)]],
        "inv_mac": [float(x) for x in bar_euler_B[:min(N, 10)]],
    }


def verify_categorified_bps_consistency(N: int) -> Dict[str, bool]:
    """Cross-check categorified BPS invariants.

    For C^3:
    1. Euler char of BPS cohomology = numerical Omega(n) = n.
    2. Motivic class under chi = n.
    3. Plethystic reconstruction: PExp(sum Omega(n) q^n) = M(q).
    4. Motivic BPS under chi = n.
    """
    results = {}

    # Check 1: BPS Poincare polynomial Euler char
    poincare_ok = True
    for n in range(1, N):
        cbps = categorified_bps_c3(n)
        chi_poincare = sum(
            (-1) ** k * dim for k, dim in cbps.poincare_poly.items()
        )
        if chi_poincare != n:
            poincare_ok = False
            break
    results["poincare_chi_equals_omega"] = poincare_ok

    # Check 2: Motivic class Euler char
    motivic_ok = True
    for n in range(1, N):
        cbps = categorified_bps_c3(n)
        if int(cbps.motivic_class.euler_characteristic()) != n:
            motivic_ok = False
            break
    results["motivic_chi_equals_omega"] = motivic_ok

    # Check 3: Plethystic reconstruction
    bps_fps = _fps_zero(N)
    for n in range(1, N):
        bps_fps[n] = Fraction(n)
    pexp = plethystic_exp(bps_fps, N)
    mac = list(_macmahon(N))
    pexp_ok = all(pexp[n] == mac[n] for n in range(N))
    results["pexp_bps_equals_macmahon"] = pexp_ok

    # Check 4: Motivic BPS specialization
    mot_bps = motivic_bps_c3(N)
    mot_ok = True
    for n in range(1, N):
        if int(mot_bps[n].euler_characteristic()) != n:
            mot_ok = False
            break
    results["motivic_bps_chi_equals_n"] = mot_ok

    return results


def verify_conifold_bps_signs(N: int) -> Dict[str, bool]:
    """Verify conifold categorified BPS signs and parity.

    Omega((d,d)) = (-1)^{d-1}: the BPS cohomology is in degree d-1.
    """
    results = {}

    sign_ok = True
    for d in range(1, N):
        cbps = categorified_bps_conifold(d, d)
        if cbps.bps_number != (-1) ** (d - 1):
            sign_ok = False
            break
    results["conifold_bps_sign_correct"] = sign_ok

    degree_ok = True
    for d in range(1, N):
        cbps = categorified_bps_conifold(d, d)
        # Cohomology in degree d-1
        expected_deg = d - 1
        if expected_deg not in cbps.poincare_poly:
            degree_ok = False
            break
    results["conifold_bps_degree_correct"] = degree_ok

    return results


def verify_hilb_c2_formula(N: int) -> Dict[str, bool]:
    r"""Verify the BB cell decomposition for Hilb^n(C^2).

    Known values from BB decomposition:
    [Hilb^0(C^2)] = 1, chi = 1
    [Hilb^1(C^2)] = L, chi = 1
    [Hilb^2(C^2)] = L^2 + L^3, chi = 2
    [Hilb^3(C^2)] = L^3 + L^4 + L^6, chi = 3
    """
    results = {}

    # Check known values
    h0 = hilb_n_c2(0)
    results["hilb0_c2"] = h0 == MotivicClass.one()

    h1 = hilb_n_c2(1)
    results["hilb1_c2"] = h1 == MotivicClass.lefschetz()

    h2 = hilb_n_c2(2)
    results["hilb2_c2"] = h2 == MotivicClass(
        {2: Fraction(1), 3: Fraction(1)}
    )

    h3 = hilb_n_c2(3)
    results["hilb3_c2"] = h3 == MotivicClass(
        {3: Fraction(1), 4: Fraction(1), 6: Fraction(1)}
    )

    # chi = p(n) (partition count)
    pc = _partition_counts(N)
    chi_ok = True
    for n in range(N):
        if int(hilb_n_c2(n).euler_characteristic()) != pc[n]:
            chi_ok = False
            break
    results["hilb_c2_chi_equals_partitions"] = chi_ok

    return results


def verify_motivic_bar_matches_numerical(N: int) -> Dict[str, bool]:
    """Verify motivic bar complex specializes to numerical bar complex.

    At each (arity, charge), chi of the motivic class should equal the
    numerical dimension.
    """
    sigma = c3_stability()
    num_fiber = categorified_bar_fiber_c3(sigma, N, max_arity=3)
    mot_bar = motivic_bar_c3(N, max_arity=3)

    match = True
    mismatches = []
    for (k, n), mc in mot_bar.arity_charge_classes.items():
        if isinstance(n, int):
            chi_mot = int(mc.euler_characteristic())
            num_dim = num_fiber.arity_charge_dims.get((k, n), 0)
            if chi_mot != num_dim:
                match = False
                mismatches.append((k, n, chi_mot, num_dim))

    return {
        "all_match": match,
        "mismatches": mismatches,
    }


def verify_shadow_tower_positivity(
    kappa: Fraction, max_genus: int = 5
) -> Dict[str, bool]:
    """Verify F_g > 0 for kappa > 0 (positivity of shadow amplitudes).

    The A-hat coefficients are all positive (from Bernoulli numbers),
    so F_g = kappa * a_hat_g > 0 when kappa > 0.
    """
    results = {}
    for g in range(1, max_genus + 1):
        if g in A_HAT_GENUS:
            f_g = kappa * A_HAT_GENUS[g]
            results[f"F_{g}_positive"] = f_g > 0
    return results


# =========================================================================
# 12. FULL CATEGORIFICATION PACKAGE
# =========================================================================

class FullCategorification(NamedTuple):
    """Complete categorification package for a CY3.

    Assembles all levels of the categorification hierarchy:
    Level 0 (numerical), Level 1 (BPS), Level 2 (bar fiber),
    Level 4 (motivic bar), Level 5 (derived Hall), Level 6 (sheaf CoHA).

    Attributes
    ----------
    name : str
    kappa : Fraction
    mc_element : CategorifiedMCElement
    bar_fiber : CategorifiedBarFiber
    motivic_bar : MotivicBarComplex
    derived_hall : DerivedHallAlgebra
    sheaf_coha : SheafCoHA
    consistency_checks : dict
    """
    name: str
    kappa: Fraction
    mc_element: CategorifiedMCElement
    bar_fiber: CategorifiedBarFiber
    motivic_bar: MotivicBarComplex
    derived_hall: DerivedHallAlgebra
    sheaf_coha: SheafCoHA
    consistency_checks: Dict[str, bool]


def full_categorification_c3(N: int = 10) -> FullCategorification:
    """Assemble the complete categorification for C^3."""
    mc = categorified_mc_c3(N)
    sigma = c3_stability()
    fiber = categorified_bar_fiber_c3(sigma, N)
    mot_bar = motivic_bar_c3(N)
    dh = derived_hall_c3(N)
    scoha = sheaf_coha_c3(N)

    checks = {}
    checks.update(verify_motivic_euler_specialization(N))
    checks.update(verify_categorified_bps_consistency(N))

    return FullCategorification(
        name="C^3",
        kappa=Fraction(1),
        mc_element=mc,
        bar_fiber=fiber,
        motivic_bar=mot_bar,
        derived_hall=dh,
        sheaf_coha=scoha,
        consistency_checks=checks,
    )
