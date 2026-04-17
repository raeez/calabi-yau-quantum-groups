r"""
Spectral structure of the elliptic-tower iteration on the
anti-symmetric subspace of the V_4 Klein-four group algebra.

This module formalises the case-(2) anti-symmetric branch of the
elliptic-tower iteration, where T_E acts as scalar 2*Id on the
anti-symmetric subspace and the natural "fixed point" is PROJECTIVE
(equivalently: integral after rescaling by the eigenvalue lambda = 2).

Companion note: notes/wave_anti_symmetric_doubling_fixed_point.md.

Mathematical content
--------------------
- Z[V_4] = Z[(Z/2)^2] with regular-representation arithmetic.
- The antipodal involution sigma_tot* (a, b, c, d) -> (d, c, b, a)
  decomposes Z[V_4] = E^+ \oplus E^- (over Q):
    E^+ = ker(sigma - id) = symmetric subspace  (basis e_0+e_3, e_1+e_2)
    E^- = ker(sigma + id) = anti-symm subspace  (basis e_0-e_3, e_1-e_2)
- The E-multiplication operator T_E(M) := M *_{V_4} M_E satisfies
    T_E = id - sigma_tot*    (Lemma 1.1 in the wave note)
  and has spectrum {0, 0, 2, 2}:
    T_E|_{E^+} = 0      (symmetric kernel)
    T_E|_{E^-} = 2 * id (anti-symm scaled)

Key theorems exposed
--------------------
- decompose_into_eigenspaces(M)       : split M = M^+ + M^- in E^+ \oplus E^-
- T_E(M)                              : Klein-four convolution with M_E
- T_E_via_id_minus_sigma(M)           : same operator computed as id - sigma
- T_E_eigenvalue_on(M)                : returns 0 if M in E^+, 2 if M in E^-
- rescaled_iteration(M, lam)          : H_E^{(lam)}(M) = T_E(M) / lam
- projective_orbit(M, k)              : T_E^k(M) = lam^k * M for M in E^-
- is_projective_fixed_point(M)        : True iff M in E^- \ {0}
- generated_Z_algebra_action(a, b, M) : (a*id + b*sigma)(M)
- eigenvalue_classification(M)        : returns "symm", "antisymm", "generic"

Independent verification anchor
-------------------------------
The library is verified against TWO independent routes:
  (R1) direct Klein-four convolution arithmetic on Z[V_4];
  (R2) spectral computation via projection onto eigenspaces of sigma_tot*.

Tests in compute/tests/test_anti_symmetric_iteration.py cross-check
both routes and decorate the load-bearing claims with
@independent_verification.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Tuple

# =========================================================================
# V_4 group algebra primitives
# =========================================================================

V4Vec = Tuple[int, int, int, int]
"""V_4-character vector: (Pi_++, Pi_+-, Pi_-+, Pi_--).

Index convention: 0 = (+,+), 1 = (+,-), 2 = (-,+), 3 = (-,-).
"""

# Canonical inputs
M_E: V4Vec = (1, 0, 0, -1)
"""M_{E} = (1, 0, 0, -1) -- bigraded Lefschetz matrix of the elliptic curve."""

M_T4: V4Vec = (2, 0, 0, -2)
"""M_{T^4} = (2, 0, 0, -2) -- bigraded Lefschetz matrix of T^4 = E x E."""


def _xor(a: int, b: int) -> int:
    """V_4 group operation as XOR on (Z/2)^2 indexing 0..3."""
    a_high, a_low = a >> 1, a & 1
    b_high, b_low = b >> 1, b & 1
    return ((a_high ^ b_high) << 1) | (a_low ^ b_low)


def v4_convolve(M, N):
    """Klein-four convolution in the regular representation of V_4.

    (M *_{V_4} N)^{eps} = sum_{delta in V_4} M^{delta} * N^{eps + delta}.

    Accepts integer or Fraction entries.
    """
    result = [0, 0, 0, 0]
    for eps in range(4):
        for delta in range(4):
            result[eps] = result[eps] + M[delta] * N[_xor(eps, delta)]
    return tuple(result)


def sigma_tot_star(M):
    """Antipodal involution sigma_tot^*((a, b, c, d)) = (d, c, b, a)."""
    return (M[3], M[2], M[1], M[0])


def negate(M):
    """Component-wise negation."""
    return tuple(-x for x in M)


def add_vec(M, N):
    """Component-wise addition."""
    return tuple(M[i] + N[i] for i in range(4))


def scale_vec(c, M):
    """Scalar multiplication."""
    return tuple(c * x for x in M)


# =========================================================================
# Eigenspace classification (over Q)
# =========================================================================


def is_anti_symmetric(M) -> bool:
    """True if sigma_tot^*(M) = -M (in -1 eigenspace E^-)."""
    return sigma_tot_star(M) == negate(M)


def is_symmetric(M) -> bool:
    """True if sigma_tot^*(M) = +M (in +1 eigenspace E^+)."""
    return sigma_tot_star(M) == M


def is_generic(M) -> bool:
    """True if M is neither in E^+ nor E^- (i.e. has nonzero projection on both)."""
    return not (is_symmetric(M) or is_anti_symmetric(M))


def eigenvalue_classification(M) -> str:
    """Classify M relative to the sigma_tot^* eigenspaces."""
    if all(x == 0 for x in M):
        return "zero"
    if is_anti_symmetric(M):
        return "antisymm"
    if is_symmetric(M):
        return "symm"
    return "generic"


def project_plus(M):
    """P^+(M) = (M + sigma_tot^*(M)) / 2 in E^+_Q.

    Returns a tuple of Fraction entries.
    """
    flipped = sigma_tot_star(M)
    return tuple(Fraction(M[i] + flipped[i], 2) for i in range(4))


def project_minus(M):
    """P^-(M) = (M - sigma_tot^*(M)) / 2 in E^-_Q.

    Returns a tuple of Fraction entries.
    """
    flipped = sigma_tot_star(M)
    return tuple(Fraction(M[i] - flipped[i], 2) for i in range(4))


def decompose_into_eigenspaces(M):
    """Return (M^+, M^-) with M = M^+ + M^- in E^+ + E^-.

    Both M^+ and M^- have rational (Fraction) entries.
    """
    return (project_plus(M), project_minus(M))


# =========================================================================
# The E-multiplication operator T_E
# =========================================================================


def T_E(M):
    """Klein-four convolution with M_E: T_E(M) = M *_{V_4} M_E.

    Independent route (R1): direct convolution arithmetic.
    """
    return v4_convolve(M, M_E)


def T_E_via_id_minus_sigma(M):
    """Spectral / closed-form computation: T_E(M) = M - sigma_tot^*(M).

    Independent route (R2): direct evaluation of the closed-form expression
    (id - sigma_tot^*)(M).
    """
    flipped = sigma_tot_star(M)
    return tuple(M[i] - flipped[i] for i in range(4))


def T_E_eigenvalue_on(M):
    """Return the T_E eigenvalue on the invariant subspace containing M.

    - 0 if M in E^+ \\ {0}
    - 2 if M in E^- \\ {0}
    - None if M is generic (not in a single eigenspace; iteration may not
      diagonalise on the orbit)
    - 0 if M = 0 (degenerate case)
    """
    if all(x == 0 for x in M):
        return 0
    cls = eigenvalue_classification(M)
    if cls == "symm":
        return 0
    if cls == "antisymm":
        return 2
    return None


# =========================================================================
# Rescaled iteration
# =========================================================================


def rescaled_iteration(M, lam):
    """H_E^{(lam)}(M) := T_E(M) / lam.

    Works over Q (lam may be int; result entries are Fractions).

    For M in E^- and lam = 2: H_E^{(2)}(M) = M.
    """
    if lam == 0:
        raise ValueError("rescaled_iteration requires lam != 0; "
                         "for M in E^+ the eigenvalue is 0 and rescaling is undefined")
    raw = T_E(M)
    return tuple(Fraction(raw[i], lam) for i in range(4))


def projective_orbit(M, k):
    """Return T_E^k(M).

    For M in E^-, this is 2^k * M (Theorem 2.1).
    For M in E^+, this is 0.
    For generic M, computed by direct iteration.
    """
    out = M
    for _ in range(k):
        out = T_E(out)
    return out


def is_projective_fixed_point(M):
    """True iff M in E^- \\ {0}.

    Equivalently: there exists a nonzero rational scalar c such that
    T_E(M) = c * M (so that [M] is a fixed point in P(Z[V_4]_Q)).
    """
    if all(x == 0 for x in M):
        return False
    return is_anti_symmetric(M)


def projective_eigenvalue(M):
    """Scalar c such that T_E(M) = c * M (when defined).

    Returns 0 for M in E^+ \\ {0}, 2 for M in E^- \\ {0}, None otherwise.
    """
    if all(x == 0 for x in M):
        return 0
    if is_symmetric(M):
        return 0
    if is_anti_symmetric(M):
        return 2
    return None


# =========================================================================
# Z-algebra generated by T_E, sigma_tot^*, id
# =========================================================================


def generated_Z_algebra_action(a, b, M):
    """Apply (a * id + b * sigma_tot^*) to M.

    The Z-algebra generated by id, T_E = id - sigma, sigma is
    Z[sigma] / (sigma^2 - 1). Every element has the form a*id + b*sigma.
    On E^+: acts as (a + b)*id (sigma|_{E^+} = +id).
    On E^-: acts as (a - b)*id (sigma|_{E^-} = -id).

    For M_T4 in E^- to be a fixed point (eigenvalue 1 on E^-), we need
    a - b = 1. This is consistent with id (a=1, b=0) but no other
    "natural" combination produces a non-trivial new fixed point, since
    every element in this Z-algebra acts as a scalar on each eigenspace.

    See Theorem 6.1 of the wave note.
    """
    flipped = sigma_tot_star(M)
    return tuple(a * M[i] + b * flipped[i] for i in range(4))


def list_natural_fixed_point_operators_on_E_minus():
    """Enumerate (a, b) with a - b = 1 (so the operator fixes E^-).

    Returns a list of (a, b) pairs for the smallest representatives.
    Used in tests to confirm that the only operator in this family that
    is the IDENTITY on Z[V_4] is (a, b) = (1, 0).
    """
    return [(1, 0), (2, 1), (0, -1), (-1, -2), (3, 2)]


# =========================================================================
# T^4-iterated tower (rescaled)
# =========================================================================


def T_T4(M):
    """T^4-multiplication: T_{T^4}(M) := M *_{V_4} M_{T^4} = 2 T_E(M)."""
    return v4_convolve(M, M_T4)


def T_T4_eigenvalue_on(M):
    """Eigenvalue of T_{T^4} on the orbit of M.

    Spectrum: {0, 0, 4, 4}. Kernel = E^+. On E^-: scalar 4.
    """
    val = T_E_eigenvalue_on(M)
    if val is None:
        return None
    return 2 * val


def rescaled_T4_iteration(M, lam=4):
    """H_{T^4}^{(lam)}(M) := T_{T^4}(M) / lam.

    For M in E^- and lam = 4: returns M (Theorem 4.2).
    """
    if lam == 0:
        raise ValueError("rescaled_T4_iteration requires lam != 0")
    raw = T_T4(M)
    return tuple(Fraction(raw[i], lam) for i in range(4))


# =========================================================================
# Trichotomy summary
# =========================================================================


def trichotomy_branch(M):
    """Return one of "kernel", "integral", "projective" for the
    eigenvalue branch containing M.

    - "kernel"      : lambda = 0, M in E^+
    - "integral"    : lambda = 1, M generic (case (3) of dichotomy)
    - "projective"  : lambda = 2, M in E^- (case (2) of dichotomy)

    See Theorem 5.1 of the wave note.
    """
    if all(x == 0 for x in M):
        return "zero"
    cls = eigenvalue_classification(M)
    if cls == "symm":
        return "kernel"
    if cls == "antisymm":
        return "projective"
    return "integral"


def trichotomy_eigenvalue(M):
    """Lambda(X) for the eigenvalue trichotomy.

    - 0 for M in E^+ (kernel branch)
    - 1 for M generic, case (3) (integral branch)
    - 2 for M in E^- (projective branch)
    """
    branch = trichotomy_branch(M)
    return {"zero": 0, "kernel": 0, "integral": 1, "projective": 2}[branch]
