r"""K3 x E  E_1-chiral Yangian: generators, relations, coproduct, R-matrix.

STATUS: ALL RESULTS IN THIS MODULE ARE CONJECTURAL (AP-CY14, AP-CY6).
The chiral algebra A_{K3 x E} does NOT exist.  The CY-A_3 programme is
OPEN.  This module constructs what the K3 x E E_1-chiral Yangian MUST be
if CY-A_3 holds, verifies internal consistency, and makes structural
predictions conditional on CY-A_3.

MATHEMATICAL CONTENT
====================

K3 x E is CY_3 (AP-CY1: CY dimension = complex dimension n = 3, not
real dimension 6).  The CY_3 framing is S^3, which gives E_1 structure
(not E_2, not E_inf).  The E_1 ordering comes from the R-direction in
C^2 x R (the 5d/6d holomorphic CS perspective, Costello 2013).

The K3 x E E_1-chiral Yangian is a DEFORMATION of the K3 Heisenberg
Yangian Y(g_{K3}) (which is E_2-chiral at d=2) by the CY_3 structure.
The deformation parameter is hbar = sigma_3 (the third elementary
symmetric function of the Omega-background parameters epsilon_1, epsilon_2,
epsilon_3 with epsilon_1 + epsilon_2 + epsilon_3 = 0).

At hbar = 0 (the CY_2 limit):
  - epsilon_3 = -(epsilon_1 + epsilon_2) = 0 forces epsilon_2 = -epsilon_1
  - The structure function g(u) = 1 (self-dual K3, see mo_rmatrix_k3e.py)
  - The R-matrix is trivial (no quantum group structure)
  - The K3 x E Yangian degenerates to the K3 Heisenberg (E_2-chiral)
  - The E_1 ordering is lost (all commutators vanish)

At hbar != 0 (the CY_3 regime):
  - The three Omega parameters are generic (epsilon_1, epsilon_2, epsilon_3)
  - The structure function g(u) is a degree-(3,3) rational function
  - The R-matrix is nontrivial (quantum group structure emerges)
  - The algebra is E_1-chiral (ordered, non-commutative)
  - The Drinfeld coproduct Delta_z is z-dependent

THE GENERATORS (conditional on CY-A_3)
=======================================

The K3 x E E_1-chiral Yangian has THREE families of generators, indexed
by the CY_3 weights (epsilon_1, epsilon_2, epsilon_3):

  (G1) K3 tangent generators: e^{(a)}(z), f^{(a)}(z), psi^{(a)}(z)
       for a = 1,...,24 (Mukai lattice directions), with OPE controlled
       by the structure function g(z-w).

  (G2) E-direction current: J^E(z) = sum J^E_n z^{-n-1}, the Heisenberg
       current of the elliptic curve direction.

  (G3) Mixed generators: W_s(z) for s >= 3, the W-algebra currents
       arising from the Sugawara-type construction on the product.

The FULL character at rank 1 (single K3 fiber) is the Goettsche formula:

  ch_{rank 1}(q) = prod_{n >= 1} 1/(1-q^n)^{24}

This matches the K3 Heisenberg Yangian character = 1/eta(q)^{24}.
The FULL K3 x E character including all ranks is the DMVV product:

  sum_{N >= 0} p^N Z_N(q,y) = prod_{n>0,l,m} 1/(1-p^n q^l y^m)^{c(4nm-l^2)}

where c(D) are the coefficients of phi_{0,1} (the K3 elliptic genus).

THE RELATIONS (conditional on CY-A_3)
======================================

(R1) Cartan subalgebra:
     [psi^{(a)}_i, psi^{(b)}_j] = 0   (all a,b,i,j)

(R2) psi-e OPE (structure-function weighted):
     psi^{(a)}(z) e^{(b)}(w) = g_{ab}(z-w) e^{(b)}(w) psi^{(a)}(z)
     where g_{ab}(u) is the Mukai-pairing-weighted structure function.

(R3) e-e exchange:
     g_{ab}(z-w) e^{(a)}(z) e^{(b)}(w) = g_{ba}(w-z) e^{(b)}(w) e^{(a)}(z)

(R4) e-f pairing:
     [e^{(a)}(z), f^{(b)}(w)] = delta_{ab} delta(z-w) psi^{(a)}(z)

(R5) Cubic Serre:
     Sym_{z_1,z_2,z_3} [e^{(a)}(z_1), [e^{(a)}(z_2), e^{(a)}(z_3+1)]] = 0
     (with the +1 shift from the Yangian level)

These relations are the AFFINE YANGIAN relations of Tsymbaliuk
(arXiv:1404.5240), specialized to the K3 x E structure function.

For the abelian (gl_1) K3 sector, the structure constants vanish and
the relations simplify to 24 independent Heisenberg sectors coupled
through the Mukai pairing omega^{ab}.

THE STRUCTURE FUNCTION
======================

The K3 x E structure function (from mo_rmatrix_k3e.py) is:

  g_{K3xE}(u) = (u - epsilon_1)(u - epsilon_2)(u - epsilon_3)
                / ((u + epsilon_1)(u + epsilon_2)(u + epsilon_3))

with epsilon_1 + epsilon_2 + epsilon_3 = 0 (CY condition).

Key properties:
  - Degree (3,3) as a rational function
  - Unitarity: g(u) * g(-u) = 1
  - CY condition: g(0) = (-1)^3 = -1 (odd parity, unlike K3 where g(0) = +1)
  - Self-dual limit: epsilon_1 = -epsilon_2, epsilon_3 = 0 gives g(u) = 1

The DEFORMATION parameter hbar = sigma_3(epsilon_1, epsilon_2, epsilon_3)
= epsilon_1 * epsilon_2 * epsilon_3 controls the deviation from the CY_2
limit.  When hbar = 0 (which requires some epsilon_i = 0), the structure
function degenerates.

THE COPRODUCT (conditional on CY-A_3)
======================================

The Drinfeld coproduct on the transfer matrix T(u) is MULTIPLICATIVE:

  Delta_z(T(u)) = T^L(u) * T^R(u - z)

This is the Miura factorization.  At the mode level:

  Delta_z(psi_{s,n}) = psi_{s,n}^L
    + sum_{a=0}^{s-1} sum_{p=0}^{s-1-a} C(s-a-1, p) z^p
        [psi_a^L conv psi_{s-a-p}^R]_n

This is the SAME universal formula as for C^3 (chiral_coproduct_universal_engine),
specialized to the K3 x E setting where:
  - The transfer matrix is T(u) = (u - phi_1)(u - phi_2)(u - phi_3) at rank 3
  - phi_1, phi_2 are K3 tangent free fields
  - phi_3 is the E-direction free field
  - The CY condition phi_1 + phi_2 + phi_3 = 0 constrains the spectrum

SPIN-BY-SPIN COPRODUCT:

  s=1 (Heisenberg): Delta_z(J_n) = J_n^L + J_n^R  (primitive)

  s=2 (Virasoro): Delta_z(T_n) = T_n^L + T_n^R
                   + ((Psi-1)/Psi) [J^L conv J^R]_n + z J_n^R
    where Psi is the Heisenberg level.

  s=3 (W_3): Delta_z(W_n) = W_n^L + W_n^R
              + [J^L conv T^R + T^L conv J^R]_n
              + z [J^L conv J^R + T^R]_n
              + z^2 J_n^R

THE R-MATRIX (conditional on CY-A_3)
=====================================

The Maulik-Okounkov R-matrix for K3 x E on Hilb^n is governed by the
structure function g_{K3xE}(u).  At charge 1:

  R(u) = g_{K3xE}(u) = (u-eps1)(u-eps2)(u-eps3) / ((u+eps1)(u+eps2)(u+eps3))

This is a SCALAR at charge 1 (the vector representation is 1-dimensional
for the gl_1 case).

At charge n, the R-matrix acts on the Fock space indexed by partitions
of n, with:

  R(u)_{lambda,mu} = prod_{s in lambda, t in mu} g(u + c(s) - c(t))

where c(i,j) = epsilon_1 * i + epsilon_2 * j is the content of box (i,j).

The R-matrix satisfies:
  - Yang-Baxter equation
  - Unitarity: R(u) R(-u) = 1
  - Crossing symmetry (from CY structure)

The K3 x E R-matrix DIFFERS from the pure K3 R-matrix:
  - K3 R-matrix: degree-(24,24), diagonal, trivial at self-dual limit
  - K3 x E R-matrix: degree-(3,3), scalar at charge 1, nontrivial E-direction

AP-CY20 COMPLIANCE: The (q,t) parameters of the quantum toroidal algebra
relate to the Omega-background parameters (epsilon_1, epsilon_2) via
equivariant localization on the Omega-background (NOT directly from the
normal bundle grading N_{C/Y}).  The intermediary is the Nekrasov partition
function.

CONVENTIONS
===========
  - epsilon_1, epsilon_2: Omega-background parameters (K3 tangent weights)
  - epsilon_3 = -(epsilon_1 + epsilon_2): E-direction weight (CY condition)
  - sigma_k = e_k(epsilon_1, epsilon_2, epsilon_3): elementary symmetric funcs
  - hbar = sigma_3 = epsilon_1 * epsilon_2 * epsilon_3: deformation parameter
  - z: spectral parameter (Yangian, NOT worldsheet; AP-CY31)
  - kappa subscripts per AP113: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber
  - AP-CY6/AP-CY14: ALL results conditional on CY-A_3

REFERENCES
==========
  k3_yangian.py (CY_2 limit: K3 Heisenberg Yangian)
  mo_rmatrix_k3e.py (MO R-matrix comparison)
  affine_yangian_e1_cy3.py (C^3 affine Yangian)
  chiral_coproduct_universal_engine.py (universal coproduct formula)
  e1_chiral_bialgebra_engine.py (E_1-chiral bialgebra axioms)
  k3e_coha_structure.py (CoHA of K3 x E)
  k3e_e1_product_chain.py (E_1 product chain)
  Maulik-Okounkov, arXiv:1211.1287 (stable envelopes, quantum groups)
  Tsymbaliuk, arXiv:1404.5240 (affine Yangian presentation)
  Schiffmann-Vasserot, arXiv:1212.5535 (CoHA = Y^+)
  Costello, arXiv:1303.2632 (5d holomorphic CS and Yangian)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    prod as symprod,
    simplify,
    symbols,
)

# ---------------------------------------------------------------------------
# Status
# ---------------------------------------------------------------------------

STATUS = "CONJECTURAL"  # AP-CY6/AP-CY14: A_{K3 x E} does NOT exist


# ---------------------------------------------------------------------------
# 0. Omega-background parameters and CY_3 condition
# ---------------------------------------------------------------------------

class OmegaParams(NamedTuple):
    """Omega-background parameters for K3 x E.

    The CY condition: epsilon_1 + epsilon_2 + epsilon_3 = 0.
    The deformation parameter: hbar = sigma_3 = eps1 * eps2 * eps3.

    STATUS: CONJECTURAL (AP-CY14).
    """
    eps1: Rational        # first K3 tangent weight
    eps2: Rational        # second K3 tangent weight
    eps3: Rational        # E-direction weight (= -(eps1 + eps2))
    sigma1: Rational      # = 0 (CY condition)
    sigma2: Rational      # = eps1*eps2 + eps1*eps3 + eps2*eps3
    sigma3: Rational      # = eps1 * eps2 * eps3 (= hbar)
    hbar: Rational        # = sigma_3, the deformation parameter
    is_selfdual: bool     # True if eps1 = -eps2 (=> eps3 = 0, hbar = 0)


def omega_params(
    eps1: Rational = Rational(1),
    eps2: Rational = Rational(-2),
) -> OmegaParams:
    r"""Construct Omega-background parameters satisfying the CY condition.

    Parameters:
        eps1: first K3 tangent weight
        eps2: second K3 tangent weight (must have eps1 != -eps2 for
              nontrivial deformation)

    The E-direction weight is forced by CY:
        eps3 = -(eps1 + eps2)

    Default (eps1, eps2) = (1, -2) gives:
        eps3 = 1, sigma_2 = -2 - 1 + 2 = -1? NO:
        sigma_2 = eps1*eps2 + eps1*eps3 + eps2*eps3
                = 1*(-2) + 1*1 + (-2)*1 = -2 + 1 - 2 = -3
        sigma_3 = 1*(-2)*1 = -2

    AP-CY28: test points MUST avoid poles at z = +/- h_i.
    With (eps1, eps2, eps3) = (1, -2, 1): poles at z = +/-1, +/-2.
    Safe test points: z = 3, 5, 7, etc.

    Returns:
        OmegaParams with all symmetric functions computed.
    """
    eps3 = -(eps1 + eps2)
    sigma1 = eps1 + eps2 + eps3  # = 0 by construction
    sigma2 = eps1 * eps2 + eps1 * eps3 + eps2 * eps3
    sigma3 = eps1 * eps2 * eps3
    is_selfdual = (eps1 + eps2 == 0)

    return OmegaParams(
        eps1=eps1,
        eps2=eps2,
        eps3=eps3,
        sigma1=sigma1,
        sigma2=sigma2,
        sigma3=sigma3,
        hbar=sigma3,
        is_selfdual=is_selfdual,
    )


def omega_params_safe() -> OmegaParams:
    r"""Safe Omega parameters with poles far from small integers.

    AP-CY28: (eps1, eps2, eps3) = (37, 41, -78) avoids all pole collisions
    with standard test points.
    """
    return omega_params(Rational(37), Rational(41))


# ---------------------------------------------------------------------------
# 1. Structure function g_{K3 x E}(u)
# ---------------------------------------------------------------------------

def structure_function(params: Optional[OmegaParams] = None):
    r"""The K3 x E structure function as a sympy expression in u.

    g(u) = (u - eps1)(u - eps2)(u - eps3)
           / ((u + eps1)(u + eps2)(u + eps3))

    with eps1 + eps2 + eps3 = 0 (CY_3 condition).

    STATUS: CONJECTURAL (AP-CY14).
    """
    if params is None:
        params = omega_params()
    u = Symbol("u")
    numer = (u - params.eps1) * (u - params.eps2) * (u - params.eps3)
    denom = (u + params.eps1) * (u + params.eps2) * (u + params.eps3)
    return cancel(numer / denom)


def structure_function_evaluate(
    u_val: Rational,
    params: Optional[OmegaParams] = None,
) -> Rational:
    """Evaluate g(u) at a specific rational point.

    Raises ValueError if u_val is a pole (u_val = -eps_i).
    """
    if params is None:
        params = omega_params()
    for ep in [params.eps1, params.eps2, params.eps3]:
        if u_val + ep == 0:
            raise ValueError(f"Pole at u = {u_val} (eps = {ep})")
    numer = (u_val - params.eps1) * (u_val - params.eps2) * (u_val - params.eps3)
    denom = (u_val + params.eps1) * (u_val + params.eps2) * (u_val + params.eps3)
    return Rational(numer, denom)


def verify_unitarity(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""Verify g(u) * g(-u) = 1 (unitarity / crossing symmetry).

    Proof: g(u)*g(-u) = prod_i [(u-eps_i)(u+eps_i)] / [(u+eps_i)(u-eps_i)] = 1.
    Each factor cancels its partner under u -> -u.

    STATUS: CONJECTURAL (AP-CY14) -- the structure function itself is conjectural.
    """
    if params is None:
        params = omega_params()

    # Symbolic verification
    u = Symbol("u")
    g_u = structure_function(params)
    g_neg_u = g_u.subs(u, -u)
    product = cancel(g_u * g_neg_u)
    symbolic_ok = (product == 1)

    # Numerical verification at safe test points (AP-CY28)
    safe_points = [Rational(3), Rational(5), Rational(7), Rational(11)]
    numerical_checks = []
    for zv in safe_points:
        try:
            gv = structure_function_evaluate(zv, params)
            gnv = structure_function_evaluate(-zv, params)
            prod_val = gv * gnv
            numerical_checks.append((str(zv), str(prod_val), prod_val == 1))
        except ValueError:
            numerical_checks.append((str(zv), "pole", False))

    return {
        "symbolic_product": str(product),
        "symbolic_ok": symbolic_ok,
        "numerical_checks": numerical_checks,
        "all_numerical_pass": all(c[2] for c in numerical_checks),
        "proof": (
            "Each factor (u-eps_i)/(u+eps_i) * (-u-eps_i)/(-u+eps_i) "
            "= (u-eps_i)(u+eps_i) / ((u+eps_i)(u-eps_i)) = 1. "
            "Product of 1s is 1."
        ),
        "status": STATUS,
    }


def verify_cy3_parity(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""Verify g(0) = (-1)^3 = -1 (CY_3 parity).

    For CY_d: g(0) = (-1)^d where d = number of weights.
    CY_2 (K3): g(0) = (-1)^{24} = +1 (even number of weights).
    CY_3 (K3 x E): g(0) = (-1)^3 = -1 (three weights).
    CY_3 (C^3): g(0) = (-1)^3 = -1 (same).
    """
    if params is None:
        params = omega_params()

    g_at_0 = structure_function_evaluate(Rational(0), params)
    expected = Rational(-1)  # (-1)^3 for CY_3

    return {
        "g_at_0": g_at_0,
        "expected": expected,
        "match": g_at_0 == expected,
        "explanation": "g(0) = prod (-eps_i / eps_i) = (-1)^3 = -1 for CY_3",
        "status": STATUS,
    }


def selfdual_degeneration() -> Dict[str, Any]:
    r"""The self-dual limit eps1 = -eps2, eps3 = 0.

    In this limit:
    - hbar = sigma_3 = eps1 * (-eps1) * 0 = 0
    - g(u) = (u - eps1)(u + eps1)(u - 0) / ((u + eps1)(u - eps1)(u + 0)) = 1
    - The R-matrix is trivial (no quantum group structure)
    - The E_1 ordering is lost
    - The K3 x E Yangian degenerates to the K3 Heisenberg (E_2-chiral)

    This is the CY_2 limit: the E-direction decouples.
    """
    eps = Rational(1)
    params = omega_params(eps, -eps)

    u = Symbol("u")
    g_u = structure_function(params)

    return {
        "params": {
            "eps1": params.eps1,
            "eps2": params.eps2,
            "eps3": params.eps3,
        },
        "hbar": params.hbar,
        "hbar_is_zero": params.hbar == 0,
        "g_u": str(cancel(g_u)),
        "g_is_trivial": cancel(g_u) == 1,
        "is_selfdual": params.is_selfdual,
        "interpretation": (
            "At hbar = 0 (self-dual limit), the K3 x E Yangian degenerates "
            "to the K3 Heisenberg Y(g_{K3}) which is E_2-chiral. "
            "The E_1 structure (non-commutativity, R-matrix, coproduct "
            "asymmetry) is lost. The E-direction decouples."
        ),
        "status": STATUS,
    }


# ---------------------------------------------------------------------------
# 2. Generators and character
# ---------------------------------------------------------------------------

class K3EYangianGenerators(NamedTuple):
    """Generator data for the K3 x E E_1-chiral Yangian.

    STATUS: CONJECTURAL (AP-CY6/AP-CY14).
    """
    num_mukai_directions: int          # 24
    generator_families: List[str]      # ['e', 'f', 'psi']
    modes_per_family: str              # 'n >= 0'
    e_direction_current: str           # 'J^E(z)'
    total_generators: str              # description
    rank1_character: str               # '1/eta(q)^{24}'
    full_character: str                # 'DMVV product'
    structure_function_degree: Tuple[int, int]  # (3, 3)
    deformation_parameter: str         # 'hbar = sigma_3'
    cy2_limit: str                     # 'K3 Heisenberg Y(g_{K3})'
    status: str                        # 'CONJECTURAL'


def generators() -> K3EYangianGenerators:
    r"""Describe the conjectural generators of the K3 x E E_1-chiral Yangian.

    The generators are organized by the CY_3 = CY_2 x CY_1 product structure:

    (G1) 24 Mukai-lattice currents J^{(a)}(z) for a = 1,...,24:
         These are the rank-1 Heisenberg currents, one per Mukai direction.
         At the CY_2 level (K3 alone), they generate Y(g_{K3}).

    (G2) The E-direction current J^E(z):
         This is the Heisenberg current for the elliptic curve factor.
         It commutes with all K3 currents at the CY_2 level.

    (G3) W-algebra currents W_s(z) for s >= 2:
         These are the higher-spin generators from the Sugawara construction
         on the product.  W_2 = T (Virasoro), W_3 (cubic Casimir), etc.

    At rank 1 (single K3 fiber), the generating function is:
      ch_{rank 1} = prod_{n >= 1} 1/(1-q^n)^{24}
    This is the Goettsche formula for chi(Hilb^n(K3)).

    The FULL character (all ranks, DMVV formula):
      Z(q,y,p) = prod_{n>0,l,m>=0} 1/(1-p^n q^l y^m)^{c(4nm-l^2)}
    where c(D) are the discriminant coefficients of phi_{0,1}.

    STATUS: CONJECTURAL (AP-CY6/AP-CY14).
    """
    return K3EYangianGenerators(
        num_mukai_directions=24,
        generator_families=["e^{(a)}", "f^{(a)}", "psi^{(a)}", "J^E"],
        modes_per_family="n >= 0 (non-negative integers)",
        e_direction_current="J^E(z) = sum J^E_n z^{-n-1}",
        total_generators=(
            "24 Mukai families x (e, f, psi) + 1 E-direction current. "
            "Total: 73 generating currents (= 3*24 + 1) with countably "
            "many modes each."
        ),
        rank1_character="prod_{n >= 1} 1/(1-q^n)^{24} = 1/eta(q)^{24} * q",
        full_character=(
            "DMVV: prod_{n>0,l,m>=0} 1/(1-p^n q^l y^m)^{c(4nm-l^2)} "
            "where c(D) are the phi_{0,1} coefficients"
        ),
        structure_function_degree=(3, 3),
        deformation_parameter="hbar = sigma_3 = eps1 * eps2 * eps3",
        cy2_limit="K3 Heisenberg Y(g_{K3}) (E_2-chiral, 24 abelian currents)",
        status=STATUS,
    )


def rank1_character_coefficients(max_n: int = 10) -> Dict[int, int]:
    r"""Compute coefficients of 1/eta(q)^{24} * q = prod 1/(1-q^n)^{24}.

    This is the rank-1 character of the K3 x E Yangian, matching the
    Goettsche formula for chi(Hilb^n(K3)).

    The coefficients p_{24}(n) count 24-colored partitions of n:
      p_{24}(0) = 1, p_{24}(1) = 24, p_{24}(2) = 324, p_{24}(3) = 3200, ...

    These are also the BKM root multiplicities of the Fake Monster Lie algebra
    at lightlike level: mult(n*delta) = p_{24}(n).

    # VERIFIED: OEIS A000935 (first 6 terms), cross-check with
    # k3_double_current_algebra.py bar_euler_generating_function.
    """
    # Compute via recursion: prod 1/(1-q^n)^{24} = sum p(n) q^n
    # Using the Euler product expansion
    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1
    for k in range(1, max_n + 1):
        # Contribution of factor 1/(1-q^k)^{24}: expand as
        # sum_{m >= 0} C(m+23, 23) q^{km}
        for n in range(max_n, k - 1, -1):
            # Add contributions from q^k through q^{max_n}
            for m in range(1, n // k + 1):
                binom = math.comb(m + 23, 23)
                if k * m <= n:
                    coeffs[n] += coeffs[n - k * m] * binom

    # The above double-counting fix: use the standard method
    # Reset and compute cleanly
    p = [0] * (max_n + 1)
    p[0] = 1
    for k in range(1, max_n + 1):
        # Factor 1/(1-q^k)^{24}: multiply the current series by this factor
        # 1/(1-x)^{24} = sum_{m >= 0} C(m+23,23) x^m with x = q^k
        new_p = p[:]
        for n in range(k, max_n + 1):
            # Accumulate: p[n] += sum_{m >= 1} C(m+23,23) * p[n - m*k]
            m = 1
            while m * k <= n:
                binom = math.comb(m + 23, 23)
                new_p[n] += binom * p[n - m * k]
                m += 1
        p = new_p

    return {n: p[n] for n in range(max_n + 1)}


# ---------------------------------------------------------------------------
# 3. Relations
# ---------------------------------------------------------------------------

class K3EYangianRelations(NamedTuple):
    """Relations of the K3 x E E_1-chiral Yangian.

    STATUS: CONJECTURAL (AP-CY6/AP-CY14).
    """
    cartan_commutes: str         # (R1)
    psi_e_ope: str               # (R2)
    e_e_exchange: str            # (R3)
    e_f_pairing: str             # (R4)
    cubic_serre: str             # (R5)
    cy_condition: str            # eps1 + eps2 + eps3 = 0
    mukai_pairing_role: str      # how omega^{ab} enters
    status: str


def relations(params: Optional[OmegaParams] = None) -> K3EYangianRelations:
    r"""Describe the conjectural relations of the K3 x E E_1-chiral Yangian.

    These are the affine Yangian relations (Tsymbaliuk, arXiv:1404.5240)
    specialized to the K3 x E structure function.

    For the gl_1 (abelian) case, the structure function decomposes:
      g_{ab}(u) = omega^{ab} * g_{K3xE}(u) for a != b
      g_{aa}(u) = g_{K3xE}(u) for a = a (diagonal)

    The Mukai pairing omega^{ab} = diag(+1,...,+1,-1,...,-1) of signature
    (4,20) enters through the cross-relations between different Mukai
    directions.

    STATUS: CONJECTURAL (AP-CY6/AP-CY14).
    """
    if params is None:
        params = omega_params()

    return K3EYangianRelations(
        cartan_commutes=(
            "(R1) [psi^{(a)}_i, psi^{(b)}_j] = 0 for all a, b, i, j. "
            "The Cartan subalgebra is abelian (as in all Yangians)."
        ),
        psi_e_ope=(
            "(R2) psi^{(a)}(z) e^{(b)}(w) = g_{ab}(z-w) e^{(b)}(w) psi^{(a)}(z). "
            f"Structure function: g(u) = (u-{params.eps1})(u-{params.eps2})"
            f"(u-{params.eps3}) / ((u+{params.eps1})(u+{params.eps2})"
            f"(u+{params.eps3})). "
            "For a != b: g_{ab} involves the Mukai pairing omega^{ab}."
        ),
        e_e_exchange=(
            "(R3) g_{ab}(z-w) e^{(a)}(z) e^{(b)}(w) "
            "= g_{ba}(w-z) e^{(b)}(w) e^{(a)}(z). "
            "Using unitarity g(u)*g(-u) = 1: the exchange is involutive."
        ),
        e_f_pairing=(
            "(R4) [e^{(a)}(z), f^{(b)}(w)] = delta_{ab} delta(z-w) psi^{(a)}(z). "
            "The e-f pairing is diagonal in the Mukai index (for gl_1)."
        ),
        cubic_serre=(
            "(R5) Sym_{z_1,z_2,z_3} [e^{(a)}(z_1), [e^{(a)}(z_2), "
            "e^{(a)}(z_3 + sigma_3)]] = 0. "
            f"The sigma_3 shift = hbar = {params.sigma3}. "
            "At hbar = 0: trivial (all commutators vanish in CY_2 limit)."
        ),
        cy_condition=(
            f"eps1 + eps2 + eps3 = {params.eps1} + {params.eps2} + "
            f"{params.eps3} = {params.sigma1} (= 0 by CY condition)"
        ),
        mukai_pairing_role=(
            "omega^{ab} = diag(+1,...,+1,-1,...,-1) of signature (4,20). "
            "Enters R2, R3 through g_{ab}(u) for a != b: "
            "the cross-direction OPE is omega-weighted. "
            "Enters R4 through the delta_{ab}: e-f pairing is diagonal. "
            "Does NOT enter R1 (Cartan commutes trivially) or R5 "
            "(Serre is within a single direction)."
        ),
        status=STATUS,
    )


# ---------------------------------------------------------------------------
# 4. Coproduct
# ---------------------------------------------------------------------------

def coproduct_spin1() -> Dict[str, Any]:
    r"""Spin-1 coproduct: Delta_z(J_n) = J_n^L + J_n^R.

    The Heisenberg current J = psi_1 is PRIMITIVE: the coproduct has no
    z-dependent terms.  This is the same as for C^3 and for K3 alone.

    STATUS: CONJECTURAL (AP-CY14).
    """
    return {
        "spin": 1,
        "formula": "Delta_z(J_n) = J_n^L + J_n^R",
        "type": "primitive",
        "z_degree": 0,
        "cross_terms": "none",
        "hbar_dependence": "none (primitive at all hbar)",
        "cy2_limit": "same (primitive is universal)",
        "status": STATUS,
    }


def coproduct_spin2(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""Spin-2 coproduct: Delta_z(T_n) with Virasoro cross-terms.

    In the psi-basis:
      Delta_z(psi_2) = psi_2^L + psi_2^R + [J^L conv J^R] + z * J^R

    In the W-basis (T = psi_2 - J^2/(2*Psi)):
      Delta_z(T_n) = T_n^L + T_n^R + ((Psi-1)/Psi) [J^L conv J^R]_n + z J_n^R

    The cross-term [J^L conv J^R] at z^0 couples the K3 and E directions
    through the Mukai pairing omega^{ab}.

    The z^1 term (z * J^R) is the spectral shift from the E-direction.
    It has coefficient 1 regardless of hbar.

    STATUS: CONJECTURAL (AP-CY14).
    """
    if params is None:
        params = omega_params()

    return {
        "spin": 2,
        "psi_formula": (
            "Delta_z(psi_{2,n}) = psi_{2,n}^L + psi_{2,n}^R "
            "+ [psi_1^L conv psi_1^R]_n + z * psi_{1,n}^R"
        ),
        "W_formula": (
            "Delta_z(T_n) = T_n^L + T_n^R "
            "+ ((Psi-1)/Psi) [J^L conv J^R]_n + z J_n^R"
        ),
        "z_degree": 1,
        "cross_terms": [
            {
                "z_power": 0,
                "operator": "[J^L conv J^R]_n = sum_m J_m^L J_{n-m}^R",
                "psi_coefficient": 1,
                "W_coefficient": "(Psi-1)/Psi",
                "mukai_role": (
                    "J = sum_a J^{(a)}: sum over 24 Mukai directions. "
                    "Cross-contraction weighted by omega^{ab}."
                ),
            },
            {
                "z_power": 1,
                "operator": "J_n^R",
                "coefficient": 1,
                "hbar_dependence": "none (spectral shift is universal)",
            },
        ],
        "hbar_sensitivity": (
            f"The sigma_3 = hbar = {params.sigma3} enters ONLY through "
            "the commutation relations of J^L and J^R (via the structure "
            "function), NOT through the coproduct formula itself. "
            "The coproduct formula is hbar-independent at all spins."
        ),
        "status": STATUS,
    }


def coproduct_spin3(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""Spin-3 coproduct: first W-algebra current.

    Delta_z(psi_3) = psi_3^L + psi_3^R
      + [psi_1^L conv psi_2^R + psi_2^L conv psi_1^R]  (z^0)
      + z * [psi_1^L conv psi_1^R + psi_2^R]            (z^1)
      + z^2 * psi_1^R                                     (z^2)

    Total: 5 operator products (after subtracting the diagonal terms).
    z-polynomial degree: 2 (= s - 1 = 3 - 1).

    The spin-3 coproduct is the first to see the FULL CY_3 structure:
    all three weights (eps1, eps2, eps3) enter through the psi_2 factors.

    STATUS: CONJECTURAL (AP-CY14).
    """
    if params is None:
        params = omega_params()

    return {
        "spin": 3,
        "formula": (
            "Delta_z(psi_{3,n}) = psi_{3,n}^L + psi_{3,n}^R "
            "+ [psi_1^L conv psi_2^R + psi_2^L conv psi_1^R] "
            "+ z [psi_1^L conv psi_1^R + psi_{2,n}^R] "
            "+ z^2 psi_{1,n}^R"
        ),
        "z_degree": 2,
        "cross_terms": [
            {"z_power": 0, "left": "psi_1=J", "right": "psi_2=T+J^2/(2Psi)",
             "binomial": 1},
            {"z_power": 0, "left": "psi_2=T+J^2/(2Psi)", "right": "psi_1=J",
             "binomial": 1},
            {"z_power": 1, "left": "psi_1=J", "right": "psi_1=J",
             "binomial": 1},
            {"z_power": 1, "left": "psi_0=Id", "right": "psi_2",
             "binomial": 1},
            {"z_power": 2, "left": "psi_0=Id", "right": "psi_1=J",
             "binomial": 1},
        ],
        "total_operator_products": 5,
        "mukai_involvement": (
            "The psi_2 factors carry the full CY_3 structure through the "
            f"Sugawara construction T = psi_2 - J^2/(2*Psi). All three "
            f"weights ({params.eps1}, {params.eps2}, {params.eps3}) enter."
        ),
        "status": STATUS,
    }


def coproduct_general_spin(s: int) -> Dict[str, Any]:
    r"""General spin-s coproduct structure for the K3 x E Yangian.

    Delta_z(psi_s) = psi_s^L + sum_{a=0}^{s-1} sum_{p=0}^{s-1-a}
        C(s-a-1, p) z^p [psi_a^L conv psi_{s-a-p}^R]

    This is the UNIVERSAL formula (from chiral_coproduct_universal_engine.py).
    For K3 x E: the psi_s generators are nonzero only for 1 <= s <= 3
    in the RANK-3 (MO framework) description of K3 x E, with:
      psi_1 = J (total Heisenberg)
      psi_2 = T + J^2/(2*Psi) (Sugawara)
      psi_3 = W_3 + ... (cubic Casimir)

    The coproduct formula TERMINATES at s = 3 for the rank-3 case:
    Delta_z(psi_s) = 0 for s > 3.

    In the RANK-24 (K3 Mukai lattice) description, psi_s is nonzero for
    1 <= s <= 24, and the coproduct formula extends to s = 24.

    STATUS: CONJECTURAL (AP-CY14).
    """
    if s < 1:
        raise ValueError(f"Spin must be >= 1, got {s}")

    z_degree = s - 1
    total_ops = s * (s + 1) // 2 - 1

    # Build cross-term table
    terms = []
    for a in range(0, s):
        for p in range(0, s - a):
            b = s - a - p
            if b < 1:
                continue
            if a == 0 and p == 0:
                continue  # skip the psi_s^R diagonal
            binom_coeff = math.comb(s - a - 1, p)
            terms.append({
                "left_spin": a,
                "right_spin": b,
                "z_power": p,
                "binomial": binom_coeff,
            })

    # Rank-3 truncation check
    rank3_truncated = (s > 3)

    return {
        "spin": s,
        "z_degree": z_degree,
        "total_operator_products": total_ops,
        "terms": terms,
        "highest_z_term": f"z^{z_degree} * J^R",
        "rank3_truncated": rank3_truncated,
        "rank3_note": (
            f"In the rank-3 (MO) framework, psi_s = 0 for s > 3. "
            f"{'This coproduct is identically zero.' if rank3_truncated else ''}"
        ),
        "rank24_note": (
            f"In the rank-24 (Mukai) framework, psi_s is nonzero for "
            f"1 <= s <= 24. This coproduct is {'active' if s <= 24 else 'zero'}."
        ),
        "coassociativity": (
            "Follows from Miura multiplicativity: "
            "T^{(1)}(u) T^{(2)}(u-z) T^{(3)}(u-w) is associative "
            "(product of commuting factors). Proved in e1_chiral_bialgebra_engine."
        ),
        "status": STATUS,
    }


def coproduct_term_count(s: int) -> Dict[str, int]:
    r"""Count the coproduct terms at spin s.

    N(s, p) = s - p terms at z^p.
    Total terms: s(s+1)/2.
    Leading z^{s-1}: 1 term (J^R).

    GF: F(x,y) = x / ((1-x)^2 (1-xy)).
    """
    if s < 1:
        raise ValueError(f"Spin must be >= 1, got {s}")

    terms_by_zpower = {}
    for p in range(s):
        terms_by_zpower[p] = s - p

    return {
        "spin": s,
        "z_degree": s - 1,
        "terms_by_zpower": terms_by_zpower,
        "total_terms": s * (s + 1) // 2,
        "leading_z_term_count": 1,
    }


# ---------------------------------------------------------------------------
# 5. R-matrix
# ---------------------------------------------------------------------------

def rmatrix_charge1(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""R-matrix at charge 1 for the K3 x E E_1-chiral Yangian.

    At charge 1, the Fock space has a single state |box>.
    The R-matrix is a SCALAR (1x1 matrix) equal to the structure function:

      R(u) = g_{K3xE}(u) = (u-eps1)(u-eps2)(u-eps3)
                            / ((u+eps1)(u+eps2)(u+eps3))

    This is the Maulik-Okounkov R-matrix restricted to the charge-1 sector
    of Hilb^1(K3 x E) = K3 x E.

    STATUS: CONJECTURAL (AP-CY14).

    AP-CY20: the identification of MO parameters with Omega-background
    parameters passes through equivariant localization, NOT through direct
    normal bundle identification.
    """
    if params is None:
        params = omega_params()

    g = structure_function(params)

    return {
        "charge": 1,
        "dimension": "1x1 (scalar)",
        "formula": str(g),
        "degree": (3, 3),
        "satisfies_ybe": True,
        "ybe_reason": "Scalar R-matrix: YBE is trivially satisfied (commutativity).",
        "unitarity": "R(u) R(-u) = g(u) g(-u) = 1",
        "classical_limit": (
            f"R(u) ~ 1 - 2*(eps1 + eps2 + eps3)/u + O(u^{{-2}}) "
            f"= 1 + O(u^{{-2}}) (sigma_1 = 0 by CY)"
        ),
        "status": STATUS,
    }


def rmatrix_charge2(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""R-matrix at charge 2 for the K3 x E E_1-chiral Yangian.

    At charge 2, the Fock space has 2 states indexed by partitions of 2:
      |2>   = row partition (two boxes in a row)
      |1,1> = column partition (two boxes in a column)

    The R-matrix is DIAGONAL on the partition basis:

      R(u)|2>   = g(u) * g(u + eps2) * |2>
      R(u)|1,1> = g(u) * g(u + eps1) * |1,1>

    where g(u + eps_k) is the structure function shifted by the content of
    the second box:
      - For (2): second box at position (0,1), content = eps2
      - For (1,1): second box at position (1,0), content = eps1

    STATUS: CONJECTURAL (AP-CY14).
    """
    if params is None:
        params = omega_params()

    u = Symbol("u")
    g = structure_function(params)

    # R-matrix elements on the two charge-2 states
    r_row = cancel(g * g.subs(u, u + params.eps2))
    r_col = cancel(g * g.subs(u, u + params.eps1))

    # The ratio encodes the charge-2 braiding asymmetry
    ratio = cancel(r_row / r_col)

    return {
        "charge": 2,
        "dimension": "2x2 (diagonal)",
        "partitions": ["(2)", "(1,1)"],
        "R_row": str(r_row),
        "R_col": str(r_col),
        "ratio": str(ratio),
        "satisfies_ybe": True,
        "ybe_reason": "Diagonal: reduces to component-wise scalar YBE.",
        "content_formula": "R(u)_lambda = prod_{s in lambda} g(u + content(s))",
        "eps1_role": f"eps1 = {params.eps1}: first K3 tangent weight",
        "eps2_role": f"eps2 = {params.eps2}: second K3 tangent weight",
        "status": STATUS,
    }


def rmatrix_charge_n_diagonal(
    partition: List[int],
    params: Optional[OmegaParams] = None,
) -> Dict[str, Any]:
    r"""Diagonal R-matrix element for a partition lambda in Hilb^n(K3 x E).

    R(u)_lambda = prod_{(i,j) in lambda} g(u + eps1*i + eps2*j)

    where the product runs over all boxes (i,j) of the Young diagram lambda
    (0-indexed rows and columns).

    STATUS: CONJECTURAL (AP-CY14).
    """
    if params is None:
        params = omega_params()

    u = Symbol("u")
    g = structure_function(params)

    result = Rational(1)
    box_contents = []
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            content = params.eps1 * i + params.eps2 * j
            result = cancel(result * g.subs(u, u + content))
            box_contents.append({
                "box": (i, j),
                "content": str(content),
            })

    n = sum(partition)

    return {
        "partition": partition,
        "charge": n,
        "num_boxes": n,
        "R_element": str(result),
        "box_contents": box_contents,
        "degree": (3 * n, 3 * n),
        "status": STATUS,
    }


# ---------------------------------------------------------------------------
# 6. Degeneration analysis: CY_2 limit vs CY_3
# ---------------------------------------------------------------------------

def cy2_vs_cy3_comparison() -> Dict[str, Any]:
    r"""Compare the K3 Yangian (CY_2) with the K3 x E Yangian (CY_3).

    CY_2 (K3 alone):
      - Structure function: g_{K3}(z) = prod_{i=1}^{24} (z-h_i)/(z+h_i)
      - Degree: (24, 24)
      - R-matrix: 24x24 diagonal (for gl_1)
      - E_n level: E_2 (braided)
      - Bar Euler product: eta(q)^{24}/q
      - Shadow class: G (depth 2, Heisenberg)
      - kappa_ch = 2 (Serre duality at d=2)

    CY_3 (K3 x E):
      - Structure function: g(u) = (u-eps1)(u-eps2)(u-eps3)/((u+eps1)(u+eps2)(u+eps3))
      - Degree: (3, 3)
      - R-matrix: scalar at charge 1 (1x1 for gl_1)
      - E_n level: E_1 (ordered, NOT braided)
      - Bar Euler product: controlled by DMVV (class M)
      - Shadow class: M (infinite depth)
      - kappa_ch = 3 (complex dimension)

    The PASSAGE K3 -> K3 x E:
      - Adds the E-direction weight eps3 = -(eps1 + eps2)
      - Breaks E_2 to E_1 (the S^3 framing is NOT S^2 x S^1)
      - Introduces hbar = sigma_3 as the deformation parameter
      - At hbar = 0: recovers K3 (E_2, self-dual limit)

    STATUS: CONJECTURAL (AP-CY6/AP-CY14) for the CY_3 column.
    The CY_2 column is proved (CY-A_2).
    """
    return {
        "k3_cy2": {
            "cy_dimension": 2,
            "structure_function_degree": (24, 24),
            "en_level": "E_2 (braided)",
            "r_matrix_charge1_dim": "24x24 diagonal",
            "bar_euler": "eta(q)^{24}/q = Delta(q)/q",
            "shadow_class": "G (depth 2)",
            "kappa_ch": 2,
            "status": "PROVED (CY-A_2)",
        },
        "k3e_cy3": {
            "cy_dimension": 3,
            "structure_function_degree": (3, 3),
            "en_level": "E_1 (ordered)",
            "r_matrix_charge1_dim": "1x1 (scalar)",
            "bar_euler": "DMVV product (class M, infinite depth)",
            "shadow_class": "M (infinite depth)",
            "kappa_ch": 3,
            "status": "CONJECTURAL (CY-A_3)",
        },
        "degeneration": {
            "parameter": "hbar = sigma_3 = eps1 * eps2 * eps3",
            "cy2_limit": "hbar -> 0 (eps3 -> 0, self-dual)",
            "e_n_breaking": "E_2 -> E_1 at hbar != 0",
            "framing": "S^3 != S^2 x S^1 (Hopf fibration nontrivial)",
        },
        "status": STATUS,
    }


# ---------------------------------------------------------------------------
# 7. Symmetric functions of Omega parameters
# ---------------------------------------------------------------------------

def omega_symmetric_functions(
    params: Optional[OmegaParams] = None,
) -> Dict[str, Rational]:
    r"""Compute the symmetric functions of (eps1, eps2, eps3).

    sigma_1 = eps1 + eps2 + eps3 = 0 (CY condition)
    sigma_2 = eps1*eps2 + eps1*eps3 + eps2*eps3
    sigma_3 = eps1 * eps2 * eps3 (= hbar)

    The structure function in terms of sigma_k:
      g(u) = (u^3 + sigma_2*u - sigma_3) / (u^3 + sigma_2*u + sigma_3)

    (using sigma_1 = 0 and the Vieta expansion
    (u-e1)(u-e2)(u-e3) = u^3 - sigma_1*u^2 + sigma_2*u - sigma_3).
    """
    if params is None:
        params = omega_params()

    return {
        "sigma_1": params.sigma1,
        "sigma_2": params.sigma2,
        "sigma_3": params.sigma3,
        "hbar": params.hbar,
        "sigma_1_is_zero": params.sigma1 == 0,
        "g_in_sigma": (
            f"g(u) = (u^3 + ({params.sigma2})*u - ({params.sigma3})) "
            f"/ (u^3 + ({params.sigma2})*u + ({params.sigma3}))"
        ),
    }


def structure_function_in_sigma(params: Optional[OmegaParams] = None):
    r"""Express g(u) in terms of sigma_2 and sigma_3 (sigma_1 = 0).

    g(u) = (u^3 + sigma_2*u - sigma_3) / (u^3 + sigma_2*u + sigma_3)

    This follows from (u-e1)(u-e2)(u-e3) = u^3 - sigma_1*u^2 + sigma_2*u - sigma_3
    with sigma_1 = 0 (CY condition).

    This form makes manifest that hbar = sigma_3 is the deformation parameter:
    at sigma_3 = 0, g(u) = 1 (trivial).
    """
    if params is None:
        params = omega_params()

    u = Symbol("u")
    s2 = params.sigma2
    s3 = params.sigma3
    numer = u**3 + s2 * u - s3
    denom = u**3 + s2 * u + s3
    return cancel(numer / denom)


def verify_sigma_form(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""Verify that the sigma-form of g(u) matches the product form.

    This cross-checks the identity:
      (u-eps1)(u-eps2)(u-eps3) = u^3 - sigma_2*u - sigma_3
    where sigma_1 = 0 (CY condition).
    """
    if params is None:
        params = omega_params()

    u = Symbol("u")
    product_form = structure_function(params)
    sigma_form = structure_function_in_sigma(params)

    diff = cancel(product_form - sigma_form)

    return {
        "product_form": str(product_form),
        "sigma_form": str(sigma_form),
        "difference": str(diff),
        "match": diff == 0,
        "status": STATUS,
    }


# ---------------------------------------------------------------------------
# 8. Full verification
# ---------------------------------------------------------------------------

def full_verification(params: Optional[OmegaParams] = None) -> Dict[str, Any]:
    r"""Run the complete verification suite for the K3 x E E_1-chiral Yangian.

    All results are CONJECTURAL (AP-CY6/AP-CY14).
    This verifies INTERNAL CONSISTENCY of the construction, not existence.
    """
    if params is None:
        params = omega_params()

    return {
        "status": STATUS,
        "disclaimer": (
            "ALL results are CONDITIONAL on CY-A_3. "
            "The chiral algebra A_{K3 x E} does NOT exist (AP-CY6). "
            "This verifies what the Yangian MUST be IF it exists."
        ),
        "path1_cy_condition": {
            "sigma_1": params.sigma1,
            "is_zero": params.sigma1 == 0,
        },
        "path2_unitarity": verify_unitarity(params),
        "path3_cy3_parity": verify_cy3_parity(params),
        "path4_selfdual": selfdual_degeneration(),
        "path5_sigma_form": verify_sigma_form(params),
        "path6_generators": generators()._asdict(),
        "path7_relations": relations(params)._asdict(),
        "path8_coproduct_s1": coproduct_spin1(),
        "path9_coproduct_s2": coproduct_spin2(params),
        "path10_coproduct_s3": coproduct_spin3(params),
        "path11_rmatrix_c1": rmatrix_charge1(params),
        "path12_rmatrix_c2": rmatrix_charge2(params),
        "path13_cy2_vs_cy3": cy2_vs_cy3_comparison(),
    }
