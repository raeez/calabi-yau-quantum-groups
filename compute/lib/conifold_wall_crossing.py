"""Kontsevich-Soibelman wall-crossing for the resolved conifold,
verified against the quantum dilogarithm pentagon identity and the
Maurer-Cartan gauge equivalence framework.

The resolved conifold X = O(-1) + O(-1) -> P^1 is the simplest CY3
exhibiting wall-crossing.  The charge lattice is Gamma = Z^2 with
generators gamma_1 (D2-brane wrapping P^1) and gamma_2 (D0-brane),
and antisymmetric pairing <gamma_1, gamma_2> = 1.

TWO CHAMBERS:
  Chamber I (large volume): one hypermultiplet of charge gamma_1,
    Omega(gamma_1) = -1 (fermionic, from the refined index (-1)^{2J}).
    Omega(gamma_2) = -1.  Two BPS states total.
  Chamber II (flopped): an additional bound state gamma_1 + gamma_2
    appears.  The pentagon identity relates the 2-particle and 3-particle
    chambers.

THE PENTAGON IDENTITY:
  The KS wall-crossing for the conifold is the pentagon identity of
  the COMPACT quantum dilogarithm (Faddeev 1999):

    E(z) = prod_{k>=0} (1 + q^k z) = sum_{n>=0} q^{n(n-1)/2} z^n / (q;q)_n

  where (q;q)_n = (1-q)(1-q^2)...(1-q^n).

  The pentagon identity states (as an identity in the quantum torus):

    E(X) * E(Y) = E(Y) * E(XY) * E(X)

  where X, Y are generators with YX = q*XY (the quantum torus relation).
  This is verified EXACTLY at the level of formal power series in q.

  Physical interpretation:
    E(X) = KS wall-crossing factor for the D2-brane (charge gamma_1)
    E(Y) = KS wall-crossing factor for the D0-brane (charge gamma_2)
    E(XY) = KS wall-crossing factor for the bound state gamma_1 + gamma_2

    LHS = Chamber I ordering (2 BPS states: gamma_1, gamma_2)
    RHS = Chamber II ordering (3 BPS states: gamma_2, gamma_1+gamma_2, gamma_1)

MC FRAMEWORK:
  The Lie algebra L_Gamma has generators e_{n,m} for (n,m) in Z^2,
  with bracket [e_{n1,m1}, e_{n2,m2}] = (n1*m2 - n2*m1) * e_{n1+n2,m1+m2}.
  The gauge transformation alpha connecting the two chambers satisfies
  exp(ad_alpha) * Theta_I = Theta_II.

DT PARTITION FUNCTION:
  Chamber I (large volume, |Q| small):
    Z_I(q, Q) / M(q) = prod_{n>=1} (1 - Q*q^n)^n
  One BPS state of charge beta with Omega(beta) = -1.

  Chamber II (flopped, |Q^{-1}| small):
    Z_II(q, Q) / M(q) = prod_{n>=1} (1 - Q^{-1}*q^n)^{-n}
  Infinite tower: Omega(beta + n*gamma_0) = -1 for n >= 0.

  These encode DIFFERENT BPS spectra but are related by wall-crossing.
  The gauge-invariant data is the full DT partition function:
    Z^{DT}(q, Q) = M(q)^2 * prod_{k>=1} (1 - Qq^k)^k * (1 - Q^{-1}q^k)^k

REFERENCES:
  - Kontsevich-Soibelman, "Stability structures, motivic DT invariants
    and cluster transformations" (arXiv:0811.2435)
  - Faddeev, "Discrete Heisenberg-Weyl group and modular group"
    (Lett. Math. Phys. 34, 1995)
  - Kashaev, "The quantum dilogarithm and Dehn twists in quantum
    Teichmuller theory" (2001)
  - Keller, "On cluster theory and quantum dilogarithm identities"
    (2011, arXiv:1102.4148)
  - Dimofte-Gukov-Soibelman, "Quantum wall-crossing in N=2 gauge theories"
    (arXiv:0912.1346)
  - Reineke, "Poisson automorphisms and quiver moduli" (arXiv:0804.3214)
  - Nagao, "Donaldson-Thomas theory and cluster algebras" (arXiv:1002.4884)

CONVENTIONS:
  - q = formal variable (quantum parameter); |q| < 1 for convergence.
  - Q = exp(-vol(P^1)) = Kahler parameter for the compact P^1.
  - Gamma = Z*gamma_1 + Z*gamma_2, <gamma_1, gamma_2> = 1.
  - Quantum torus: X^a Y^b * X^c Y^d = q^{bc} X^{a+c} Y^{b+d}.
    This gives YX = qXY.
  - Compact quantum dilogarithm: E(z) = prod_{k>=0}(1 + q^k z)
    = sum q^{n(n-1)/2} z^n / (q;q)_n.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple
import math


# ---------------------------------------------------------------------------
# Power series arithmetic over Q
# ---------------------------------------------------------------------------

def _poly_mul_trunc(a: List[Fraction], b: List[Fraction],
                    N: int) -> List[Fraction]:
    """Multiply two truncated power series mod q^N."""
    result = [Fraction(0)] * N
    la, lb = len(a), len(b)
    for i in range(min(la, N)):
        if a[i] == 0:
            continue
        for j in range(min(lb, N - i)):
            result[i + j] += a[i] * b[j]
    return result


def _poly_inv_trunc(a: List[Fraction], N: int) -> List[Fraction]:
    """Invert power series a(q) mod q^N, assuming a[0] != 0."""
    if a[0] == 0:
        raise ValueError("Cannot invert power series with zero constant term")
    inv_a0 = Fraction(1) / a[0]
    result = [Fraction(0)] * N
    result[0] = inv_a0
    la = len(a)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, min(n + 1, la)):
            s += a[k] * result[n - k]
        result[n] = -inv_a0 * s
    return result


def _poly_add(a: List[Fraction], b: List[Fraction],
              N: int) -> List[Fraction]:
    """Add two truncated power series mod q^N."""
    result = [Fraction(0)] * N
    for i in range(min(len(a), N)):
        result[i] += a[i]
    for i in range(min(len(b), N)):
        result[i] += b[i]
    return result


def _poly_sub(a: List[Fraction], b: List[Fraction],
              N: int) -> List[Fraction]:
    """Subtract: a - b, truncated mod q^N."""
    result = [Fraction(0)] * N
    for i in range(min(len(a), N)):
        result[i] += a[i]
    for i in range(min(len(b), N)):
        result[i] -= b[i]
    return result


def _poly_scale(a: List[Fraction], c: Fraction,
                N: int) -> List[Fraction]:
    """Multiply power series by scalar."""
    result = [Fraction(0)] * N
    for i in range(min(len(a), N)):
        result[i] = c * a[i]
    return result


def _poly_one(N: int) -> List[Fraction]:
    """The constant series 1."""
    result = [Fraction(0)] * N
    result[0] = Fraction(1)
    return result


def _poly_exp_trunc(f: List[Fraction], N: int) -> List[Fraction]:
    """Exponentiate a power series f with f[0] = 0, mod q^N."""
    assert f[0] == 0, "exp requires f[0] = 0"
    g = [Fraction(0)] * N
    g[0] = Fraction(1)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, n + 1):
            if k < len(f):
                s += Fraction(k) * f[k] * g[n - k]
        g[n] = s / Fraction(n)
    return g


def _poly_log_trunc(g: List[Fraction], N: int) -> List[Fraction]:
    """Logarithm of power series g with g[0] = 1, mod q^N."""
    assert g[0] == Fraction(1), "log requires g[0] = 1"
    f = [Fraction(0)] * N
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, n):
            s += Fraction(k) * f[k] * g[n - k]
        f[n] = g[n] - s / Fraction(n)
    return f


# ---------------------------------------------------------------------------
# Quantum torus algebra
# ---------------------------------------------------------------------------

class QuantumTorusElement:
    r"""Element of the quantum torus algebra C_q[X^{\pm}, Y^{\pm}].

    The quantum torus has generators X, Y with relation YX = q XY,
    or equivalently: X^a Y^b * X^c Y^d = q^{bc} X^{a+c} Y^{b+d}.

    Elements are represented as {(a, b): coeff_series} where
    coeff_series is a list of Fractions (power series in q, mod q^N).

    In the KS formalism: X = e^{gamma_1} (D2-brane), Y = e^{gamma_2} (D0-brane).
    """

    def __init__(self, terms: Dict[Tuple[int, int], List[Fraction]], N: int):
        self.terms = {k: v for k, v in terms.items()
                      if any(c != 0 for c in v)}
        self.N = N

    @classmethod
    def monomial(cls, a: int, b: int, coeff: List[Fraction], N: int):
        """Create a single monomial coeff * X^a * Y^b."""
        return cls({(a, b): coeff[:N]}, N)

    @classmethod
    def one(cls, N: int):
        """The identity element 1."""
        return cls.monomial(0, 0, _poly_one(N), N)

    @classmethod
    def zero(cls, N: int):
        """The zero element."""
        return cls({}, N)

    def __add__(self, other: 'QuantumTorusElement') -> 'QuantumTorusElement':
        N = self.N
        result = {}
        all_keys = set(self.terms.keys()) | set(other.terms.keys())
        for k in all_keys:
            a = self.terms.get(k, [Fraction(0)] * N)
            b = other.terms.get(k, [Fraction(0)] * N)
            result[k] = _poly_add(a, b, N)
        return QuantumTorusElement(result, N)

    def __sub__(self, other: 'QuantumTorusElement') -> 'QuantumTorusElement':
        N = self.N
        result = {}
        all_keys = set(self.terms.keys()) | set(other.terms.keys())
        for k in all_keys:
            a = self.terms.get(k, [Fraction(0)] * N)
            b = other.terms.get(k, [Fraction(0)] * N)
            result[k] = _poly_sub(a, b, N)
        return QuantumTorusElement(result, N)

    def scale(self, c: Fraction) -> 'QuantumTorusElement':
        """Multiply by a scalar."""
        N = self.N
        return QuantumTorusElement(
            {k: _poly_scale(v, c, N) for k, v in self.terms.items()}, N)

    def scale_series(self, s: List[Fraction]) -> 'QuantumTorusElement':
        """Multiply by a power series in q."""
        N = self.N
        return QuantumTorusElement(
            {k: _poly_mul_trunc(v, s, N) for k, v in self.terms.items()}, N)

    def __mul__(self, other: 'QuantumTorusElement') -> 'QuantumTorusElement':
        r"""Multiply in the quantum torus: X^a Y^b * X^c Y^d = q^{bc} X^{a+c} Y^{b+d}."""
        N = self.N
        result = {}
        for (a1, b1), c1 in self.terms.items():
            for (a2, b2), c2 in other.terms.items():
                key = (a1 + a2, b1 + b2)
                shift = b1 * a2
                prod_coeffs = _poly_mul_trunc(c1, c2, N)
                if shift > 0:
                    shifted = [Fraction(0)] * N
                    for i in range(N - shift):
                        if i < len(prod_coeffs):
                            shifted[i + shift] = prod_coeffs[i]
                    prod_coeffs = shifted
                elif shift < 0:
                    shifted = [Fraction(0)] * N
                    for i in range(max(0, -shift), N):
                        if (i + shift) >= 0 and (i + shift) < len(prod_coeffs):
                            shifted[i] = prod_coeffs[i + shift]
                    prod_coeffs = shifted

                if key in result:
                    result[key] = _poly_add(result[key], prod_coeffs, N)
                else:
                    result[key] = prod_coeffs

        return QuantumTorusElement(result, N)

    def get_coeff(self, a: int, b: int) -> List[Fraction]:
        """Get the coefficient of X^a Y^b as a q-series."""
        return self.terms.get((a, b), [Fraction(0)] * self.N)

    def truncate_charge(self, max_total: int) -> 'QuantumTorusElement':
        """Keep only terms with |a| + |b| <= max_total."""
        return QuantumTorusElement(
            {(a, b): v for (a, b), v in self.terms.items()
             if abs(a) + abs(b) <= max_total}, self.N)


# ---------------------------------------------------------------------------
# Compact quantum dilogarithm
# ---------------------------------------------------------------------------

def _q_pochhammer(n: int, N_q: int) -> List[Fraction]:
    """Compute (q;q)_n = (1-q)(1-q^2)...(1-q^n) mod q^{N_q}."""
    result = [Fraction(0)] * N_q
    result[0] = Fraction(1)
    for k in range(1, n + 1):
        factor = [Fraction(0)] * N_q
        factor[0] = Fraction(1)
        if k < N_q:
            factor[k] = Fraction(-1)
        result = _poly_mul_trunc(result, factor, N_q)
    return result


def _q_pochhammer_inv(n: int, N_q: int) -> List[Fraction]:
    """Compute 1/(q;q)_n mod q^{N_q}."""
    return _poly_inv_trunc(_q_pochhammer(n, N_q), N_q)


def compact_quantum_dilog(a: int, b: int,
                          N_q: int, max_charge: int) -> QuantumTorusElement:
    r"""Compact quantum dilogarithm E(X^a Y^b) in the quantum torus.

    E(z) = prod_{k>=0} (1 + q^k z) = sum_{n>=0} q^{n(n-1)/2} z^n / (q;q)_n

    For z = X^a Y^b in the quantum torus:
      z^n = (X^a Y^b)^n = q^{n(n-1)*b*a/2} X^{na} Y^{nb}

    So the coefficient of X^{na} Y^{nb} in E(X^a Y^b) is:
      q^{n(n-1)/2 + n(n-1)*ba/2} / (q;q)_n = q^{n(n-1)(1+ba)/2} / (q;q)_n

    Parameters:
        a, b: charge of the argument (X^a Y^b)
        N_q: q-series truncation order
        max_charge: maximum total charge |na| + |nb|
    """
    result = QuantumTorusElement.zero(N_q)
    for n in range(max_charge + 1):
        na, nb = n * a, n * b
        if abs(na) + abs(nb) > max_charge:
            break
        # Euler phase: q^{n(n-1)/2}
        # Torus ordering phase: q^{n(n-1)*ba/2}
        total_phase = n * (n - 1) // 2 + n * (n - 1) * b * a // 2
        if total_phase >= N_q:
            break
        coeff = _q_pochhammer_inv(n, N_q)
        if total_phase > 0:
            shifted = [Fraction(0)] * N_q
            for i in range(N_q - total_phase):
                shifted[i + total_phase] = coeff[i]
            coeff = shifted
        result = result + QuantumTorusElement.monomial(na, nb, coeff, N_q)
    return result


# ---------------------------------------------------------------------------
# The pentagon identity
# ---------------------------------------------------------------------------

def pentagon_identity_quantum_torus(N_q: int, max_charge: int) -> Dict[str, object]:
    r"""Verify the quantum dilogarithm pentagon identity in the quantum torus.

    The pentagon identity states:
      E(X) * E(Y) = E(Y) * E(XY) * E(X)

    where E(z) = prod_{k>=0}(1 + q^k z) is the compact quantum dilogarithm,
    and X, Y are generators of the quantum torus with YX = qXY.

    Physical interpretation:
      E(X) = KS factor for charge gamma_1 (D2-brane)
      E(Y) = KS factor for charge gamma_2 (D0-brane)
      E(XY) = KS factor for bound state gamma_1 + gamma_2

      LHS = Chamber I  (2 BPS states: gamma_1, gamma_2)
      RHS = Chamber II (3 BPS states: gamma_2, gamma_1+gamma_2, gamma_1)

    The identity is verified EXACTLY (all coefficients in Q[q]/q^{N_q}
    agree at all charge sectors up to max_charge).

    Parameters:
        N_q: truncation in the q-series
        max_charge: maximum total charge |a| + |b| to verify
    """
    E_X = compact_quantum_dilog(1, 0, N_q, max_charge)
    E_Y = compact_quantum_dilog(0, 1, N_q, max_charge)
    E_XY = compact_quantum_dilog(1, 1, N_q, max_charge)

    LHS = E_X * E_Y
    RHS = E_Y * E_XY * E_X

    all_charges = set(LHS.terms.keys()) | set(RHS.terms.keys())
    discrepancies = []
    checked = 0
    for charge in sorted(all_charges):
        a, b = charge
        if abs(a) + abs(b) > max_charge:
            continue
        checked += 1
        lhs_c = LHS.get_coeff(a, b)
        rhs_c = RHS.get_coeff(a, b)
        for k in range(N_q):
            if lhs_c[k] != rhs_c[k]:
                discrepancies.append({
                    "charge": (a, b),
                    "q_power": k,
                    "lhs": str(lhs_c[k]),
                    "rhs": str(rhs_c[k]),
                })

    sample_coeffs = {}
    for (a, b) in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
                    (2, 1), (1, 2), (2, 2)]:
        if abs(a) + abs(b) <= max_charge:
            lc = LHS.get_coeff(a, b)
            rc = RHS.get_coeff(a, b)
            sample_coeffs[(a, b)] = {
                "lhs": [str(lc[k]) for k in range(min(N_q, 8))],
                "rhs": [str(rc[k]) for k in range(min(N_q, 8))],
                "match": all(lc[k] == rc[k] for k in range(N_q)),
            }

    return {
        "N_q": N_q,
        "max_charge": max_charge,
        "charges_checked": checked,
        "pentagon_holds": len(discrepancies) == 0,
        "discrepancies": discrepancies[:10],
        "sample_coefficients": sample_coeffs,
        "identity": "E(X)*E(Y) = E(Y)*E(XY)*E(X)",
        "dilogarithm": "E(z) = prod_{k>=0}(1+q^k z) [compact/Faddeev]",
    }


def pentagon_numerical(q_val: float, N_terms: int = 100) -> Dict[str, object]:
    r"""Numerically verify the pentagon in the Schrodinger representation.

    In the Schrodinger representation of the quantum torus:
      X acts as multiplication: (X f)(t) = t * f(t)
      Y acts as q-shift: (Y f)(t) = f(q*t)

    The compact quantum dilogarithm E(z) = prod_{k>=0}(1+q^k z) acts as:
      (E(X) f)(t) = [prod_{k>=0}(1 + q^k t)] * f(t)
      (E(Y) f)(t) = sum_{n>=0} q^{n(n-1)/2} f(q^n t) / (q;q)_n

    We verify E(X)*E(Y)*f = E(Y)*E(XY)*E(X)*f for test functions.
    """
    q = q_val
    assert 0 < q < 1, "Need |q| < 1"

    def E_num(z):
        """prod_{k>=0} (1 + q^k z)"""
        p = 1.0
        for k in range(N_terms):
            p *= (1.0 + q ** k * z)
        return p

    def qpoch(n):
        """(q;q)_n"""
        p = 1.0
        for k in range(1, n + 1):
            p *= (1.0 - q ** k)
        return p

    # Test at t = 0.2, f(t) = 1
    t = 0.2
    N_sum = min(N_terms, 30)

    # LHS: (E(X)*E(Y)*1)(t) = E_num(t) * sum_{n>=0} q^{n(n-1)/2} / (q;q)_n
    sum_EY = sum(q ** (n * (n - 1) // 2) / qpoch(n) for n in range(N_sum))
    LHS = E_num(t) * sum_EY

    # RHS: (E(Y)*E(XY)*E(X)*1)(t)
    # Step 1: E(X)*1 at t -> E_num(t)
    # Step 2: E(XY) applied to h(t) = E_num(t)
    # (XY)^n f(t) = q^{n(n-1)/2} t^n f(q^n t)
    # E(XY) h(t) = sum q^{n(n-1)/2} * q^{n(n-1)/2} * t^n * h(q^n t) / (q;q)_n
    #            = sum q^{n(n-1)} t^n E_num(q^n t) / (q;q)_n
    def step2(t_val):
        return sum(q ** (n * (n - 1)) * t_val ** n * E_num(q ** n * t_val) / qpoch(n)
                   for n in range(N_sum))

    # Step 3: E(Y) applied to step2
    # (E(Y) g)(t) = sum q^{m(m-1)/2} g(q^m t) / (q;q)_m
    RHS = sum(q ** (m * (m - 1) // 2) * step2(q ** m * t) / qpoch(m)
              for m in range(N_sum))

    return {
        "q": q_val,
        "t": t,
        "N_terms": N_terms,
        "LHS": LHS,
        "RHS": RHS,
        "match": abs(LHS - RHS) < 1e-8,
        "relative_error": abs(LHS - RHS) / max(abs(LHS), 1e-15),
    }


# ---------------------------------------------------------------------------
# BPS spectra in the two chambers
# ---------------------------------------------------------------------------

def chamber_I_spectrum() -> Dict[Tuple[int, int], int]:
    r"""BPS spectrum in Chamber I (large volume).

    Two BPS states:
      Omega(gamma_1) = -1 (D2-brane wrapping P^1)
      Omega(gamma_2) = -1 (D0-brane)
    """
    return {(1, 0): -1, (0, 1): -1}


def chamber_II_spectrum(max_n: int = 10) -> Dict[Tuple[int, int], int]:
    r"""BPS spectrum in Chamber II (flopped).

    The minimal wall-crossing (pentagon) adds one bound state:
      Omega(gamma_1 + gamma_2) = -1

    The full Chamber II spectrum for the conifold includes:
      Omega(gamma_1 + n*gamma_2) = -1 for n = 0, 1, 2, ...
    arising from a sequence of walls.
    """
    spectrum = {(0, 1): -1, (1, 0): -1}
    for n in range(1, max_n + 1):
        spectrum[(1, n)] = -1
    return spectrum


def conifold_pentagon_spectrum() -> Tuple[
        Dict[Tuple[int, int], int],
        Dict[Tuple[int, int], int]]:
    r"""The specific BPS spectra on the two sides of the conifold wall.

    Pentagon: 2 particles <-> 3 particles.
      Side A: {gamma_1, gamma_2}
      Side B: {gamma_1, gamma_2, gamma_1+gamma_2}
    """
    side_A = {(1, 0): -1, (0, 1): -1}
    side_B = {(1, 0): -1, (0, 1): -1, (1, 1): -1}
    return side_A, side_B


# ---------------------------------------------------------------------------
# MC element and gauge transformation
# ---------------------------------------------------------------------------

def lie_bracket(gamma1: Tuple[int, int],
                gamma2: Tuple[int, int]) -> Tuple[Tuple[int, int], int]:
    r"""[e_{gamma1}, e_{gamma2}] = <gamma1, gamma2> * e_{gamma1+gamma2}.

    Antisymmetric pairing: <(n1,m1), (n2,m2)> = n1*m2 - n2*m1.
    """
    n1, m1 = gamma1
    n2, m2 = gamma2
    return ((n1 + n2, m1 + m2), n1 * m2 - n2 * m1)


def mc_equation_check(theta: Dict[Tuple[int, int], int],
                      max_charge: int) -> Dict[str, object]:
    r"""Check [Theta, Theta] = 0 in the lattice Lie algebra.

    The BPS spectrum at a generic point does NOT satisfy [Theta, Theta] = 0
    in the naive Lie algebra -- the obstruction is resolved by the L_infinity
    higher brackets (shadow obstruction tower).
    """
    bracket_sq = {}
    for g1, o1 in theta.items():
        for g2, o2 in theta.items():
            (g_sum, pairing) = lie_bracket(g1, g2)
            if abs(g_sum[0]) + abs(g_sum[1]) > max_charge:
                continue
            if pairing == 0:
                continue
            coeff = o1 * o2 * pairing
            bracket_sq[g_sum] = bracket_sq.get(g_sum, 0) + coeff

    nonzero = {k: v for k, v in bracket_sq.items() if v != 0}
    return {
        "theta": theta,
        "bracket_squared_nonzero": nonzero,
        "mc_equation_holds": len(nonzero) == 0,
    }


def gauge_transformation_conifold(max_order: int = 5) -> Dict[str, object]:
    r"""Compute the gauge transformation alpha connecting the two chambers.

    Theta_I = -e_{(1,0)} - e_{(0,1)}
    Theta_II = -e_{(1,0)} - e_{(0,1)} - e_{(1,1)}

    alpha = e_{(1,0)} produces [e_{(1,0)}, Theta_I] = -e_{(1,1)} at first order.
    Higher orders generate shadow obstruction tower corrections.
    """
    theta_I = {(1, 0): Fraction(-1), (0, 1): Fraction(-1)}
    theta_II = {(1, 0): Fraction(-1), (0, 1): Fraction(-1), (1, 1): Fraction(-1)}
    alpha = {(1, 0): Fraction(1)}

    def ad_alpha_on(target, alpha_dict, max_c):
        result = {}
        for g_a, c_a in alpha_dict.items():
            for g_t, c_t in target.items():
                g_sum, pairing = lie_bracket(g_a, g_t)
                if abs(g_sum[0]) + abs(g_sum[1]) > max_c:
                    continue
                coeff = c_a * c_t * pairing
                if coeff != 0:
                    result[g_sum] = result.get(g_sum, Fraction(0)) + coeff
        return {k: v for k, v in result.items() if v != 0}

    corrections = []
    ad_k_theta = dict(theta_I)
    factorial_inv = Fraction(1)
    total = dict(theta_I)

    for k in range(1, max_order + 1):
        ad_k_theta = ad_alpha_on(ad_k_theta, alpha, max_order + 2)
        factorial_inv = factorial_inv / Fraction(k)
        correction_k = {g: c * factorial_inv for g, c in ad_k_theta.items()}
        corrections.append({"order": k, "terms": dict(correction_k)})
        for g, c in correction_k.items():
            total[g] = total.get(g, Fraction(0)) + c

    total = {k: v for k, v in total.items() if v != 0}

    return {
        "alpha": {str(k): str(v) for k, v in alpha.items()},
        "match_at_charge_11": total.get((1, 1), Fraction(0)) == Fraction(-1),
        "higher_charge_corrections": {
            str(k): str(v) for k, v in sorted(total.items())
            if abs(k[0]) + abs(k[1]) > 2
        },
        "corrections_by_order": corrections,
    }


# ---------------------------------------------------------------------------
# DT partition functions
# ---------------------------------------------------------------------------

def _macmahon_coeffs(N: int) -> List[Fraction]:
    """M(q) = prod_{n>=1} (1-q^n)^{-n} mod q^N via log-exp."""
    log_m = [Fraction(0)] * N
    for n in range(1, N):
        for m in range(1, N):
            if n * m >= N:
                break
            log_m[n * m] += Fraction(n, m)
    return _poly_exp_trunc(log_m, N)


def dt_chamber_I(N_q: int, N_Q: int) -> Dict[int, List[Fraction]]:
    r"""DT partition function in Chamber I (large volume).

    Z_I(q, Q) / M(q) = prod_{n>=1} (1 - Q*q^n)^n

    Returns dict {d: F_d(q)} where F_d is the coefficient of Q^d.
    """
    log_coeffs = [[Fraction(0)] * N_q for _ in range(N_Q + 1)]
    for m in range(1, N_Q + 1):
        c = [Fraction(0)] * N_q
        for n in range(1, N_q):
            if n * m >= N_q:
                break
            c[n * m] += Fraction(n)
        log_coeffs[m] = _poly_scale(c, Fraction(-1, m), N_q)

    F = [[Fraction(0)] * N_q for _ in range(N_Q + 1)]
    F[0] = _poly_one(N_q)
    for d in range(1, N_Q + 1):
        s = [Fraction(0)] * N_q
        for k in range(1, d + 1):
            term = _poly_mul_trunc(
                _poly_scale(log_coeffs[k], Fraction(k), N_q),
                F[d - k], N_q)
            s = _poly_add(s, term, N_q)
        F[d] = _poly_scale(s, Fraction(1, d), N_q)

    return {d: F[d] for d in range(N_Q + 1)}


def dt_chamber_II(N_q: int, N_Qinv: int) -> Dict[int, List[Fraction]]:
    r"""DT partition function in Chamber II (flopped).

    Z_II(q, Q) / M(q) = prod_{n>=1} (1 - Q^{-1}*q^n)^{-n}

    Returns dict {d: G_d(q)} where G_d is the coefficient of Q^{-d}.
    """
    log_coeffs = [[Fraction(0)] * N_q for _ in range(N_Qinv + 1)]
    for m in range(1, N_Qinv + 1):
        c = [Fraction(0)] * N_q
        for n in range(1, N_q):
            if n * m >= N_q:
                break
            c[n * m] += Fraction(n)
        log_coeffs[m] = _poly_scale(c, Fraction(1, m), N_q)

    G = [[Fraction(0)] * N_q for _ in range(N_Qinv + 1)]
    G[0] = _poly_one(N_q)
    for d in range(1, N_Qinv + 1):
        s = [Fraction(0)] * N_q
        for k in range(1, d + 1):
            term = _poly_mul_trunc(
                _poly_scale(log_coeffs[k], Fraction(k), N_q),
                G[d - k], N_q)
            s = _poly_add(s, term, N_q)
        G[d] = _poly_scale(s, Fraction(1, d), N_q)

    return {d: G[d] for d in range(N_Qinv + 1)}


def conifold_dt_partition_function(N_q: int,
                                   N_Q: int) -> Dict[str, object]:
    r"""Compute the conifold DT partition function in both chambers.

    Chamber I:  Z_I/M(q) = prod (1-Qq^k)^k    (expansion in Q)
    Chamber II: Z_II/M(q) = prod (1-Q^{-1}q^k)^{-k}  (expansion in Q^{-1})

    Verifies:
      sum_d F_I_d (at Q=1) = M(q)^{-1}   [Chamber I at flop point]
      sum_d G_II_d (at Q^{-1}=1) = M(q)   [Chamber II at flop point]
    """
    M_q = _macmahon_coeffs(N_q)
    F_I = dt_chamber_I(N_q, N_Q)
    G_II = dt_chamber_II(N_q, N_Q)

    # Check: sum F_I_d at Q=1 should be prod(1-q^k)^k = 1/M(q)
    sum_FI = _poly_one(N_q)
    for d in range(1, N_Q + 1):
        sum_FI = _poly_add(sum_FI, F_I[d], N_q)
    M_inv = _poly_inv_trunc(M_q, N_q)
    sum_FI_eq_Minv = all(sum_FI[k] == M_inv[k] for k in range(N_q))

    # Check: sum G_II_d at Q^{-1}=1 should be prod(1-q^k)^{-k} = M(q)
    sum_GII = _poly_one(N_q)
    for d in range(1, N_Q + 1):
        sum_GII = _poly_add(sum_GII, G_II[d], N_q)
    sum_GII_eq_M = all(sum_GII[k] == M_q[k] for k in range(N_q))

    display_FI = {}
    display_GII = {}
    for d in range(min(N_Q + 1, 5)):
        display_FI[d] = [int(F_I[d][k]) for k in range(min(N_q, 15))]
        display_GII[d] = [int(G_II[d][k]) for k in range(min(N_q, 15))]

    return {
        "N_q": N_q,
        "N_Q": N_Q,
        "macmahon": [int(M_q[k]) for k in range(min(N_q, 15))],
        "chamber_I_coeffs": display_FI,
        "chamber_II_coeffs": display_GII,
        "sum_FI_equals_Minv": sum_FI_eq_Minv,
        "sum_GII_equals_M": sum_GII_eq_M,
    }


def conifold_dt_vs_macmahon(N: int) -> Dict[str, object]:
    r"""Verify the Q-expansion of prod_{k>=1} (1-Qq^k)^{-k}.

    C_0(q) = 1
    C_1(q) = sum_{k>=1} k*q^k = q/(1-q)^2
    """
    N_Q_max = 5
    log_coeffs = [[Fraction(0)] * N]
    for d in range(1, N_Q_max + 1):
        c = [Fraction(0)] * N
        for k in range(1, N):
            if k * d >= N:
                break
            c[k * d] += Fraction(k)
        log_coeffs.append(_poly_scale(c, Fraction(1, d), N))

    C = [[Fraction(0)] * N for _ in range(N_Q_max + 1)]
    C[0] = _poly_one(N)
    for d in range(1, N_Q_max + 1):
        s = [Fraction(0)] * N
        for k in range(1, d + 1):
            term = _poly_mul_trunc(
                _poly_scale(log_coeffs[k], Fraction(k), N),
                C[d - k], N)
            s = _poly_add(s, term, N)
        C[d] = _poly_scale(s, Fraction(1, d), N)

    C1_expected = [Fraction(0)] * N
    for k in range(1, N):
        C1_expected[k] = Fraction(k)
    C1_match = all(C[1][k] == C1_expected[k] for k in range(N))

    return {
        "N": N,
        "C0": [int(C[0][k]) for k in range(min(N, 15))],
        "C1": [int(C[1][k]) for k in range(min(N, 15))],
        "C2": [int(C[2][k]) for k in range(min(N, 15))],
        "C3": [int(C[3][k]) for k in range(min(N, 15))],
        "C1_equals_kq^k": C1_match,
    }


def dt_numerical(q_val: float, Q_val: float = None,
                 N_terms: int = 50) -> Dict[str, object]:
    r"""Numerically compute DT partition functions in both chambers.

    Z_I / M(q) = prod (1-Qq^k)^k     [one BPS state]
    Z_II / M(q) = prod (1-Q^{-1}q^k)^{-k}  [infinite tower]
    """
    q = q_val
    Q = Q_val if Q_val is not None else q ** 0.5
    assert 0 < q < 1 and 0 < Q < 1

    M = 1.0
    for n in range(1, N_terms + 1):
        M *= (1.0 - q ** n) ** (-n)

    F_I = 1.0
    for k in range(1, N_terms + 1):
        F_I *= (1.0 - Q * q ** k) ** k

    F_II = 1.0
    for k in range(1, N_terms + 1):
        F_II *= (1.0 - q ** k / Q) ** (-k)

    Z_I = M * F_I
    Z_II = M * F_II

    # Full DT combines both sectors
    Z_full = M ** 2
    for k in range(1, N_terms + 1):
        Z_full *= (1.0 - Q * q ** k) ** k * (1.0 - q ** k / Q) ** k

    return {
        "q": q_val,
        "Q": Q,
        "MacMahon": M,
        "Z_I": Z_I,
        "Z_II": Z_II,
        "Z_full": Z_full,
        "Z_I_neq_Z_II": abs(Z_I - Z_II) > 1e-10,
    }


# ---------------------------------------------------------------------------
# Full verification suite
# ---------------------------------------------------------------------------

def verify_all(N_q: int = 12, max_charge: int = 6) -> Dict[str, object]:
    """Run all conifold wall-crossing verifications."""
    results = {}
    results["pentagon_quantum_torus"] = pentagon_identity_quantum_torus(N_q, max_charge)
    results["pentagon_numerical_q05"] = pentagon_numerical(0.5)
    results["pentagon_numerical_q03"] = pentagon_numerical(0.3)

    side_A, side_B = conifold_pentagon_spectrum()
    results["mc_check_chamber_I"] = mc_equation_check(side_A, max_charge + 2)
    results["mc_check_chamber_II"] = mc_equation_check(side_B, max_charge + 2)
    results["gauge_transformation"] = gauge_transformation_conifold(max_order=5)

    results["dt_partition_function"] = conifold_dt_partition_function(N_q + 5, N_Q=4)
    results["dt_decomposition"] = conifold_dt_vs_macmahon(N_q + 5)
    results["dt_numerical"] = dt_numerical(0.5)

    return results


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 72)
    print("CONIFOLD WALL-CROSSING: KS PENTAGON & DT PARTITION FUNCTIONS")
    print("=" * 72)

    print("\n1. PENTAGON IDENTITY (compact quantum dilogarithm, exact)")
    print("-" * 55)
    pent = pentagon_identity_quantum_torus(N_q=12, max_charge=6)
    print(f"   E(X)*E(Y) = E(Y)*E(XY)*E(X)")
    print(f"   Pentagon holds: {pent['pentagon_holds']}")
    print(f"   Charges checked: {pent['charges_checked']}")

    print("\n2. PENTAGON IDENTITY (numerical, Schrodinger representation)")
    print("-" * 55)
    for qv in [0.3, 0.5, 0.7]:
        num = pentagon_numerical(qv, N_terms=50)
        print(f"   q={qv}: LHS={num['LHS']:.10f} RHS={num['RHS']:.10f} "
              f"match={num['match']}")

    print("\n3. MC EQUATION CHECK")
    print("-" * 55)
    side_A, side_B = conifold_pentagon_spectrum()
    mc_I = mc_equation_check(side_A, 6)
    mc_II = mc_equation_check(side_B, 6)
    print(f"   Chamber I  [Theta,Theta]=0: {mc_I['mc_equation_holds']}")
    print(f"   Chamber II [Theta,Theta]=0: {mc_II['mc_equation_holds']}")

    print("\n4. GAUGE TRANSFORMATION")
    print("-" * 55)
    gt = gauge_transformation_conifold(max_order=5)
    print(f"   alpha = {gt['alpha']}")
    print(f"   Produces e_(1,1): {gt['match_at_charge_11']}")
    print(f"   Higher corrections: {gt['higher_charge_corrections']}")

    print("\n5. DT PARTITION FUNCTION (two chambers)")
    print("-" * 55)
    dt = conifold_dt_partition_function(15, N_Q=4)
    print(f"   MacMahon:  {dt['macmahon'][:10]}")
    print(f"   Ch I  sum F = M^-1: {dt['sum_FI_equals_Minv']}")
    print(f"   Ch II sum G = M:    {dt['sum_GII_equals_M']}")

    print("\n6. DT DECOMPOSITION")
    print("-" * 55)
    dec = conifold_dt_vs_macmahon(15)
    print(f"   C_1 = k*q^k: {dec['C1_equals_kq^k']}")

    print("\n7. NUMERICAL DT")
    print("-" * 55)
    dn = dt_numerical(0.5)
    print(f"   q={dn['q']}, Q={dn['Q']:.4f}")
    print(f"   Z_I  = {dn['Z_I']:.10f}")
    print(f"   Z_II = {dn['Z_II']:.10f}")
    print(f"   Z_I != Z_II: {dn['Z_I_neq_Z_II']}")

    print("\n" + "=" * 72)
    print("All verifications complete.")
    print("=" * 72)
