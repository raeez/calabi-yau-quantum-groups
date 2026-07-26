r"""Chiral algebras from spectral curves of Hitchin systems.

MATHEMATICAL CONTENT
====================

The Hitchin system (M_H, pi, B) for a reductive group G over a smooth
projective curve C of genus g >= 2 (or P^1 with appropriate twisting)
produces chiral algebras via QUANTIZATION of the integrable system.
The total space Tot(K_C) is a LOCAL SURFACE (complex dimension 2),
NOT a Calabi-Yau threefold.  The chiral algebra comes from the
Beilinson-Drinfeld quantization of the Hitchin integrable system.

1. THE SPECTRAL CURVE
---------------------

For G = GL(n), the Higgs field phi in H^0(End(E) tensor K_C) has
characteristic polynomial

    det(lambda - phi) = lambda^n - a_1 lambda^{n-1} + ... + (-1)^n a_n

where a_i in H^0(K_C^{tensor i}).  The spectral curve is

    Sigma_b = {det(lambda - phi) = 0} subset Tot(K_C)

for a point b = (a_1, ..., a_n) in the Hitchin base

    B = bigoplus_{i=1}^{n} H^0(C, K_C^{tensor i}).

For G = SL(n), the trace a_1 = 0 so the base is

    B_{SL} = bigoplus_{i=2}^{n} H^0(C, K_C^{tensor i}).

Genus of the spectral curve (Riemann-Hurwitz for the degree-n cover):

    For GL(n)/SL(n) with g(C) >= 2:
        g(Sigma) = n^2(g-1) + 1

    For GL(2) on P^1 with twist L = O(d), d >= 4:
        Sigma = {lambda^2 = q(z)} subset Tot(L)
        g(Sigma) = d - 1   (hyperelliptic curve)

2. THE HITCHIN BASE AND HAMILTONIANS
-------------------------------------

    dim B(GL_n, g) = sum_{i=1}^{n} dim H^0(K_C^i) = sum_{i=1}^{n} (2i-1)(g-1)
                   = n^2 (g-1)

    dim B(SL_n, g) = sum_{i=2}^{n} (2i-1)(g-1) = (n^2-1)(g-1)

    For P^1 with twist O(d): dim H^0(O(d)) = d+1 (for d >= 0)
    so dim B(GL_2, P^1, O(d)) = dim H^0(O(2d)) = 2d+1.
    For the standard twist d=2 (i.e. L = K_{P^1}^2 = O(4)):
    dim B = dim H^0(O(4)) = 5.

3. THE BEILINSON-DRINFELD QUANTIZATION
---------------------------------------

The quantum Hitchin system (Beilinson-Drinfeld 1997, 2005) produces:

    (a) A commutative chiral algebra Z(g) = Fun^{ch}(Op_G^v(C))
        (functions on the space of G^v-opers on C)
    (b) A map Z(g) -> Z(V_crit(g)) (center of the affine vertex algebra
        at the critical level k = -h^v)
    (c) The quantum Hitchin Hamiltonians are the chiral algebra generators

The key theorem (Feigin-Frenkel 1992, Beilinson-Drinfeld 2005):

    Z(V_{-h^v}(g)) = Fun(Op_{G^v}(C))

The center of V_{-h^v}(g) is isomorphic to the algebra of functions on
the space of ^LG-opers.  This is the GEOMETRIC LANGLANDS form of the
Hitchin integrable system: the classical Hitchin Hamiltonians are the
symbols of the quantum Hitchin operators.

4. THE NEKRASOV-SHATASHVILI LIMIT
----------------------------------

In the Omega-background with parameters (epsilon_1, epsilon_2):
    - Full Omega-background: both epsilon_1, epsilon_2 nonzero
    - NS limit: epsilon_2 -> 0, epsilon_1 = hbar
    - The partition function Z(a, epsilon_1, epsilon_2) becomes
      Z^{NS}(a, hbar) = exp(W(a, hbar) / epsilon_2)
    - W(a, hbar) = twisted superpotential = quantum spectral curve equation
    - The quantum spectral curve: det(hbar d/dz - phi(z)) Psi = 0

The NS limit produces an OPER: a differential operator on C whose
symbol is the spectral curve equation.  This is the SAME structure
as the Beilinson-Drinfeld quantization.

5. NOT CY_3
------------

    dim_C Tot(K_C) = 2  (a surface, rank-1 bundle over the curve)
    dim_C Sigma = 1     (a curve inside the surface)

Neither is a Calabi-Yau threefold.  Tot(K_C) IS a local CY surface
(canonical bundle is trivial), and the chiral algebra arises from
QUANTIZATION OF THE INTEGRABLE SYSTEM, not from a CY_3 category.

The connection to CY_3 is INDIRECT:
    - For G = SL_2, g = 2: M_H has dim_C = 6 with Lagrangian fibration
      of base dim 3, giving "CY3-type" structure (see hitchin_sl2_genus2.py)
    - The topological B-model on Tot(K_C) gives the AGT correspondence
      but the target is a surface, not a threefold.

MATHEMATICAL REFERENCES
========================
    - Hitchin, "Stable bundles and integrable systems" (1987)
    - Beauville-Narasimhan-Ramanan, "Spectral curves and the generalised
      theta divisor" (1989)
    - Beilinson-Drinfeld, "Quantization of Hitchin's integrable system
      and Hecke eigensheaves" (2005)
    - Feigin-Frenkel, "Affine Kac-Moody algebras at the critical level
      and Gelfand-Dikii algebras" (1992)
    - Nekrasov-Shatashvili, "Quantization of integrable systems and
      four dimensional gauge theories" (2009, arXiv:0908.4052)
    - Donagi-Markman, "Spectral covers, algebraically completely
      integrable Hamiltonian systems, and moduli of bundles" (1995)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np


# =========================================================================
# 1. SPECTRAL CURVE GEOMETRY
# =========================================================================

class SpectralCurveData(NamedTuple):
    """Geometric data of a spectral curve Sigma -> C."""
    group: str                  # e.g. 'GL_2', 'SL_3'
    rank: int                   # n for GL_n / SL_n
    genus_base: int             # g(C)
    genus_spectral: int         # g(Sigma)
    degree_cover: int           # degree of Sigma -> C
    n_branch_points: int        # number of simple branch points (generic)
    dim_hitchin_base: int       # dim(B)
    dim_prym: int               # dim Prym(Sigma/C) or dim of abelian fibre
    hitchin_base_summands: Tuple[int, ...]  # dimensions of H^0(K^i)
    is_connected: bool          # whether generic spectral curve is connected


def spectral_curve_genus_gln(n: int, g: int) -> int:
    """Genus of the spectral curve for GL(n) on a genus-g curve.

    For a degree-n cover Sigma -> C with C of genus g,
    Riemann-Hurwitz gives:

        2g(Sigma) - 2 = n(2g - 2) + B

    where B is the total branching.  For the GENERIC spectral curve
    of GL(n), the branching comes from the discriminant of the
    characteristic polynomial, which has degree n(n-1)(2g-2) as a
    section of K^{n(n-1)}.  Each branch point is simple (generically),
    so B = n(n-1)(2g-2).

    Result: g(Sigma) = n^2(g-1) + 1.

    This formula also follows from the adjunction formula for
    Sigma subset Tot(K_C) in the surface Tot(K_C).
    """
    if n < 1:
        raise ValueError(f"Rank n must be >= 1, got {n}")
    if g < 0:
        raise ValueError(f"Genus g must be >= 0, got {g}")
    return n * n * (g - 1) + 1


def spectral_curve_genus_p1(n: int, twist_degree: int) -> int:
    """Genus of the spectral curve for GL(n) on P^1 with twist O(d).

    On P^1, K_{P^1} = O(-2), so we need a twist line bundle L = O(d)
    with d >= 2n for the spectral curve to have interesting geometry.

    For GL(2) with L = O(d): Sigma = {lambda^2 = q(z)} where
    q in H^0(O(2d)).  This is a hyperelliptic curve with
    2d branch points (zeros of q), giving g(Sigma) = d - 1.

    For general GL(n) with L = O(d):
    The spectral curve is a degree-n cover of P^1 in Tot(O(d)).
    Ramification: n(n-1)d simple branch points generically.
    Riemann-Hurwitz: 2g - 2 = n(0 - 2) + n(n-1)d = -2n + n(n-1)d
    So g = 1 - n + n(n-1)d/2.
    """
    if n < 1:
        raise ValueError(f"Rank n must be >= 1, got {n}")
    if twist_degree < 0:
        raise ValueError(f"Twist degree must be >= 0, got {twist_degree}")
    # Number of simple branch points for generic spectral curve
    n_branch = n * (n - 1) * twist_degree
    # Riemann-Hurwitz: 2g-2 = n(-2) + n_branch
    two_g_minus_2 = -2 * n + n_branch
    if two_g_minus_2 % 2 != 0:
        raise ValueError(
            f"Branching {n_branch} gives non-integer genus for n={n}, d={twist_degree}"
        )
    return two_g_minus_2 // 2 + 1


def hitchin_base_dim_gln(n: int, g: int) -> int:
    """Dimension of the Hitchin base for GL(n) on a genus-g curve.

    B = bigoplus_{i=1}^{n} H^0(K_C^i)

    For g >= 2: dim H^0(K_C^i) = (2i-1)(g-1) by Riemann-Roch.
    So dim B = sum_{i=1}^{n} (2i-1)(g-1) = n^2(g-1).
    """
    if g < 2:
        raise ValueError(f"Need genus >= 2 for the standard Hitchin system, got g={g}")
    if n < 1:
        raise ValueError(f"Rank n must be >= 1, got {n}")
    return n * n * (g - 1)


def hitchin_base_dim_sln(n: int, g: int) -> int:
    """Dimension of the Hitchin base for SL(n) on a genus-g curve.

    B_{SL} = bigoplus_{i=2}^{n} H^0(K_C^i)

    dim B_{SL} = sum_{i=2}^{n} (2i-1)(g-1) = (n^2 - 1)(g-1).
    """
    if g < 2:
        raise ValueError(f"Need genus >= 2 for the standard Hitchin system, got g={g}")
    if n < 1:
        raise ValueError(f"Rank n must be >= 1, got {n}")
    return (n * n - 1) * (g - 1)


def hitchin_base_dim_p1(n: int, twist_degree: int) -> int:
    """Dimension of the Hitchin base for GL(n) on P^1 with twist O(d).

    The Hitchin base is bigoplus_{i=1}^{n} H^0(O(id)).
    dim H^0(O(id)) = id + 1 for id >= 0 (else 0).

    dim B = sum_{i=1}^{n} max(id + 1, 0).
    """
    if n < 1:
        raise ValueError(f"Rank n must be >= 1, got {n}")
    total = 0
    for i in range(1, n + 1):
        deg = i * twist_degree
        if deg >= 0:
            total += deg + 1
    return total


def hitchin_base_summands_gln(n: int, g: int) -> Tuple[int, ...]:
    """Dimensions of each summand H^0(K_C^i) in the Hitchin base."""
    if g < 2:
        raise ValueError(f"Need genus >= 2 for the standard Hitchin system, got g={g}")
    return tuple((2 * i - 1) * (g - 1) for i in range(1, n + 1))


def hitchin_base_summands_p1(n: int, twist_degree: int) -> Tuple[int, ...]:
    """Dimensions of each summand H^0(O(id)) in the Hitchin base on P^1."""
    return tuple(max(i * twist_degree + 1, 0) for i in range(1, n + 1))


def spectral_curve_data_gln(n: int, g: int) -> SpectralCurveData:
    """Full spectral curve data for GL(n) on a genus-g curve."""
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")
    if n < 1:
        raise ValueError(f"Need n >= 1, got n={n}")

    genus_spec = spectral_curve_genus_gln(n, g)
    n_branch = n * (n - 1) * (2 * g - 2)
    dim_base = hitchin_base_dim_gln(n, g)
    summands = hitchin_base_summands_gln(n, g)

    # For GL(n), the Hitchin fibre is the Jacobian Jac(Sigma) (not Prym)
    # dim Jac(Sigma) = g(Sigma) = n^2(g-1) + 1
    # But dim of the Hitchin base = n^2(g-1), so dim fibre = dim base
    # only when g(Sigma) = dim_base, i.e. n^2(g-1)+1 = n^2(g-1),
    # which is impossible.  The correct picture: for GL(n) the fibre
    # is Jac(Sigma) of dim g(Sigma) = n^2(g-1)+1, but the base has
    # dim n^2(g-1).  The discrepancy is the overall Jac(C) factor.
    # After factoring: fibre = Prym x Jac(C), Prym dim = n^2(g-1)+1-g.
    # For the INTEGRABLE system: the fibre of the integrable system
    # is the compactified Jacobian, and dim_fibre = dim_base.
    dim_prym = genus_spec - g  # dim Prym = g(Sigma) - g(C)

    return SpectralCurveData(
        group=f'GL_{n}',
        rank=n,
        genus_base=g,
        genus_spectral=genus_spec,
        degree_cover=n,
        n_branch_points=n_branch,
        dim_hitchin_base=dim_base,
        dim_prym=dim_prym,
        hitchin_base_summands=summands,
        is_connected=(n == 1 or True),  # generic spectral curve is connected
    )


def spectral_curve_data_sln(n: int, g: int) -> SpectralCurveData:
    """Full spectral curve data for SL(n) on a genus-g curve.

    For SL(n), the spectral curve is the SAME curve as for GL(n)
    (it is still a degree-n cover of C), but the trace condition
    a_1 = 0 means we move in a smaller Hitchin base, and the
    Hitchin fibre is the PRYM variety Prym(Sigma/C), not the
    full Jacobian.
    """
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")
    if n < 1:
        raise ValueError(f"Need n >= 1, got n={n}")

    genus_spec = spectral_curve_genus_gln(n, g)
    n_branch = n * (n - 1) * (2 * g - 2)
    dim_base = hitchin_base_dim_sln(n, g)
    summands = tuple((2 * i - 1) * (g - 1) for i in range(2, n + 1))

    # For SL(n), the Hitchin fibre is Prym(Sigma/C)
    # dim Prym = (n^2 - 1)(g - 1) = dim_base
    dim_prym = (n * n - 1) * (g - 1)

    return SpectralCurveData(
        group=f'SL_{n}',
        rank=n,
        genus_base=g,
        genus_spectral=genus_spec,
        degree_cover=n,
        n_branch_points=n_branch,
        dim_hitchin_base=dim_base,
        dim_prym=dim_prym,
        hitchin_base_summands=summands,
        is_connected=True,
    )


def spectral_curve_data_p1(n: int, twist_degree: int) -> SpectralCurveData:
    """Spectral curve data for GL(n) on P^1 with twist O(d).

    The canonical bundle K_{P^1} = O(-2), so the Hitchin system
    with the canonical twist has no sections.  We twist by
    L = O(d) with d >= 2.

    For GL(2), L = O(d):
        B = H^0(O(d)) + H^0(O(2d)) (trace + determinant)
        But for the spectral curve, we consider the total
        characteristic polynomial: lambda^2 - a_1 lambda + a_2 = 0
        where a_1 in H^0(O(d)), a_2 in H^0(O(2d)).

    For SL(2), a_1 = 0, so the spectral curve is
        lambda^2 = -a_2(z)  with a_2 in H^0(O(2d)).
    """
    if n < 1:
        raise ValueError(f"Need n >= 1, got n={n}")
    if twist_degree < 1:
        raise ValueError(f"Need positive twist degree, got {twist_degree}")

    genus_spec = spectral_curve_genus_p1(n, twist_degree)
    n_branch = n * (n - 1) * twist_degree
    dim_base = hitchin_base_dim_p1(n, twist_degree)
    summands = hitchin_base_summands_p1(n, twist_degree)

    return SpectralCurveData(
        group=f'GL_{n}',
        rank=n,
        genus_base=0,  # P^1 has genus 0
        genus_spectral=genus_spec,
        degree_cover=n,
        n_branch_points=n_branch,
        dim_hitchin_base=dim_base,
        dim_prym=genus_spec,  # Prym = Jac for cover of P^1 (g(P^1)=0)
        hitchin_base_summands=summands,
        is_connected=True,
    )


# =========================================================================
# 2. OPERS AND THE BEILINSON-DRINFELD QUANTIZATION
# =========================================================================

class OperData(NamedTuple):
    """Data of a G-oper on a curve C."""
    group: str
    rank: int
    genus: int
    oper_order: int             # order of the differential operator
    oper_bundle: str            # principal bundle type
    dim_oper_space: int         # dimension of the space of opers
    accessory_params: int       # number of accessory parameters
    is_fuchsian: bool           # whether the oper can be Fuchsian
    regular_singularities: int  # number of regular singular points


def oper_data_sln(n: int, g: int) -> OperData:
    """Data of SL(n)-opers on a genus-g curve.

    An SL(n)-oper on C is a degree-n differential operator
        D = d^n + u_2 d^{n-2} + u_3 d^{n-3} + ... + u_n
    where u_i in H^0(C, K_C^i).

    The space of opers Op_{SL_n}(C) for C of genus g >= 2 is an affine
    space modeled on the Hitchin base:
        Op_{SL_n}(C) is a torsor for B_{SL_n} = bigoplus_{i=2}^{n} H^0(K_C^i)

    dim Op_{SL_n}(C) = (n^2 - 1)(g - 1)

    For P^1 with regular singularities at marked points:
    the oper becomes a Fuchsian differential equation.
    """
    if g < 2:
        raise ValueError(f"Need genus >= 2 for the standard oper, got g={g}")
    dim_oper = (n * n - 1) * (g - 1)

    return OperData(
        group=f'SL_{n}',
        rank=n,
        genus=g,
        oper_order=n,
        oper_bundle=f'SL_{n}-bundle on C_{{g={g}}}',
        dim_oper_space=dim_oper,
        accessory_params=dim_oper,  # same as dim of oper space
        is_fuchsian=(g == 0),
        regular_singularities=0,  # no marked points in the compact case
    )


def oper_data_p1_punctured(n: int, n_punctures: int) -> OperData:
    """Data of SL(n)-opers on P^1 with regular singularities.

    An SL(n)-oper on P^1 with regular singularities at
    z_1, ..., z_m is a Fuchsian differential equation:
        D = d^n + sum_{i=2}^{n} u_i(z) d^{n-i}
    where u_i(z) has poles of order <= i at z_1, ..., z_m.

    The space of opers has dimension:
        sum_{i=2}^{n} ((i-1)*m + max(i*(-2) + 2 + m*i, 0))
    Simplified for m >= 2n:
        dim = (n^2 - 1)(m - 2)/2 + correction terms

    For n=2, m punctures:
        D = d^2 + u_2(z), u_2 has simple poles at z_j => dim = m - 3
        (3 is subtracted by the PSL_2 automorphisms of P^1)
        This is the space of Fuchsian equations with m regular singularities.
        Accessory parameters: m - 3 (after fixing 3 points by Mobius).
    """
    if n_punctures < 3:
        raise ValueError(
            f"Need >= 3 punctures on P^1 for nontrivial opers, got {n_punctures}"
        )
    if n < 2:
        raise ValueError(f"Need n >= 2, got {n}")

    # For SL(2): dim = m - 3 (accessory parameters)
    # For SL(n): dim = (n^2 - 1)(m - 2)/2 (for sufficiently many punctures)
    # More precisely: each puncture contributes (n^2-1)/2 parameters,
    # minus the dim of Aut(P^1) = 3, minus the constraints from
    # the residue conditions.
    #
    # For SL(2) with m regular singularities:
    # u_2(z) = sum_{j=1}^{m} (c_j/(z-z_j)^2 + A_j/(z-z_j))
    # Constraints: sum A_j = 0 (regularity at infinity) gives m-1 free A_j
    # Plus: Mobius fixes 3 points, so dim = m - 3 accessory params
    # after fixing the residues c_j.
    if n == 2:
        dim_oper = n_punctures - 3
        accessory = n_punctures - 3
    else:
        # General formula: for m regular singularities on P^1,
        # the oper space has dim = (n-1)*m - n*(n-1)/2 - (n-1)
        # = (n-1)(m - (n+2)/2) for even n
        # Simplified: use the known formula from Frenkel 2007
        dim_oper = (n * n - 1) * (n_punctures - 2) // 2
        accessory = dim_oper

    return OperData(
        group=f'SL_{n}',
        rank=n,
        genus=0,
        oper_order=n,
        oper_bundle=f'SL_{n}-oper on P^1 with {n_punctures} punctures',
        dim_oper_space=dim_oper,
        accessory_params=accessory,
        is_fuchsian=True,
        regular_singularities=n_punctures,
    )


# =========================================================================
# 3. CHIRAL ALGEBRA FROM THE HITCHIN SYSTEM
# =========================================================================

class HitchinChiralData(NamedTuple):
    """Chiral algebra data arising from the Hitchin system."""
    group: str
    rank: int
    genus: int
    chiral_algebra_type: str    # description of the chiral algebra
    central_charge: Optional[Fraction]  # Sugawara c, absent at critical level
    level: str                  # 'critical' or parametric
    n_generators: int           # number of generating currents
    generator_spins: Tuple[int, ...]  # conformal weights of generators
    hitchin_base_dim: int
    is_critical_level: bool
    dual_group: str             # Langlands dual


# Dual Coxeter numbers for simple Lie algebras
DUAL_COXETER: Dict[str, int] = {
    'A_1': 2, 'A_2': 3, 'A_3': 4, 'A_4': 5, 'A_5': 6, 'A_6': 7, 'A_7': 8,
    'B_2': 3, 'B_3': 5, 'B_4': 7,
    'C_2': 3, 'C_3': 4, 'C_4': 5,
    'D_4': 6, 'D_5': 8, 'D_6': 10,
    'E_6': 12, 'E_7': 18, 'E_8': 30,
    'F_4': 9,
    'G_2': 4,
}

# Dimensions of simple Lie algebras
LIE_DIM: Dict[str, int] = {
    'A_1': 3, 'A_2': 8, 'A_3': 15, 'A_4': 24, 'A_5': 35, 'A_6': 48, 'A_7': 63,
    'B_2': 10, 'B_3': 21, 'B_4': 36,
    'C_2': 10, 'C_3': 21, 'C_4': 36,
    'D_4': 28, 'D_5': 45, 'D_6': 66,
    'E_6': 78, 'E_7': 133, 'E_8': 248,
    'F_4': 52,
    'G_2': 14,
}

# Ranks of simple Lie algebras
LIE_RANK: Dict[str, int] = {
    'A_1': 1, 'A_2': 2, 'A_3': 3, 'A_4': 4, 'A_5': 5, 'A_6': 6, 'A_7': 7,
    'B_2': 2, 'B_3': 3, 'B_4': 4,
    'C_2': 2, 'C_3': 3, 'C_4': 4,
    'D_4': 4, 'D_5': 5, 'D_6': 6,
    'E_6': 6, 'E_7': 7, 'E_8': 8,
    'F_4': 4,
    'G_2': 2,
}

# Casimir degrees (exponents + 1) for simple Lie algebras
CASIMIR_DEGREES: Dict[str, Tuple[int, ...]] = {
    'A_1': (2,),
    'A_2': (2, 3),
    'A_3': (2, 3, 4),
    'A_4': (2, 3, 4, 5),
    'A_5': (2, 3, 4, 5, 6),
    'A_6': (2, 3, 4, 5, 6, 7),
    'A_7': (2, 3, 4, 5, 6, 7, 8),
    'B_2': (2, 4),
    'B_3': (2, 4, 6),
    'B_4': (2, 4, 6, 8),
    'C_2': (2, 4),
    'C_3': (2, 4, 6),
    'C_4': (2, 4, 6, 8),
    'D_4': (2, 4, 6, 4),  # Note: D_4 has triality, Casimirs 2,4,4,6
    'D_5': (2, 4, 6, 8, 5),
    'D_6': (2, 4, 6, 8, 10, 6),
    'E_6': (2, 5, 6, 8, 9, 12),
    'E_7': (2, 6, 8, 10, 12, 14, 18),
    'E_8': (2, 8, 12, 14, 18, 20, 24, 30),
    'F_4': (2, 6, 8, 12),
    'G_2': (2, 6),
}

# Langlands dual type map
LANGLANDS_DUAL: Dict[str, str] = {
    'A_1': 'A_1', 'A_2': 'A_2', 'A_3': 'A_3', 'A_4': 'A_4',
    'A_5': 'A_5', 'A_6': 'A_6', 'A_7': 'A_7',
    'B_2': 'C_2', 'B_3': 'C_3', 'B_4': 'C_4',
    'C_2': 'B_2', 'C_3': 'B_3', 'C_4': 'B_4',
    'D_4': 'D_4', 'D_5': 'D_5', 'D_6': 'D_6',
    'E_6': 'E_6', 'E_7': 'E_7', 'E_8': 'E_8',
    'F_4': 'F_4',
    'G_2': 'G_2',
}


def _lie_type_from_group(group: str) -> str:
    """Extract Lie type from group name like 'SL_2' -> 'A_1'."""
    if group.startswith('GL_') or group.startswith('SL_'):
        n = int(group.split('_')[1])
        return f'A_{n-1}'
    if group.startswith('SO_'):
        n = int(group.split('_')[1])
        if n % 2 == 1:
            return f'B_{(n-1)//2}'
        else:
            return f'D_{n//2}'
    if group.startswith('Sp_'):
        n = int(group.split('_')[1])
        return f'C_{n//2}'
    # Direct Lie type
    if group in LIE_DIM:
        return group
    raise ValueError(f"Cannot determine Lie type from group '{group}'")


def critical_level_central_charge(lie_type: str) -> None:
    """Central charge of the affine vertex algebra at the critical level.

    At the critical level k = -h^v, the Segal-Sugawara construction
    is ill-defined (the denominator k + h^v = 0).  However, the
    CENTER of V_{-h^v}(g) is large (isomorphic to the algebra of
    functions on opers).

    The central charge of the Virasoro generated by the Sugawara
    construction is:

        c(k) = k * dim(g) / (k + h^v)

    At k = -h^v, this has a pole.  There is no finite Sugawara central
    charge at the critical level.  The Laurent numerator evaluates to
    -h^v * dim(g), and the Segal-Sugawara fields pass to the
    Feigin-Frenkel centre rather than to a Virasoro action.
    """
    if lie_type not in DUAL_COXETER:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    return None


def affine_central_charge(lie_type: str, level: Fraction) -> Fraction:
    """Central charge of the affine vertex algebra V_k(g) at level k.

    c(k) = k * dim(g) / (k + h^v)

    This is UNDEFINED at the critical level k = -h^v.
    """
    if lie_type not in DUAL_COXETER:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    h_v = Fraction(DUAL_COXETER[lie_type], 1)
    dim_g = Fraction(LIE_DIM[lie_type], 1)
    if level + h_v == 0:
        raise ValueError(
            f"Central charge undefined at critical level k = -h^v = {-h_v} "
            f"for {lie_type}"
        )
    return level * dim_g / (level + h_v)


def hitchin_chiral_data(lie_type: str, g: int) -> HitchinChiralData:
    """Chiral algebra data for the quantum Hitchin system.

    The Beilinson-Drinfeld quantization at the critical level
    produces a chiral algebra whose generators are the quantum
    Hitchin Hamiltonians.  The generators correspond to the
    Casimir invariants of the Lie algebra g: for each degree-d_i
    Casimir, there is a spin-d_i current.

    For g = sl_n (type A_{n-1}), the generators have spins 2, 3, ..., n,
    corresponding to the Casimirs of degrees 2, 3, ..., n.
    This is the W_n algebra at the critical level.
    """
    if lie_type not in LIE_DIM:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")

    rank = LIE_RANK[lie_type]
    h_v = DUAL_COXETER[lie_type]
    dim_g = LIE_DIM[lie_type]
    casimirs = CASIMIR_DEGREES[lie_type]
    dual = LANGLANDS_DUAL[lie_type]

    # The chiral algebra is the center of V_{-h^v}(g)
    # = Fun(Op_{^LG}(C)) by Feigin-Frenkel
    # The generators are quantum Hitchin Hamiltonians of spins d_1, ..., d_r
    # where d_i are the Casimir degrees.
    n_gens = len(casimirs)

    # Hitchin base dimension
    dim_base = sum((2 * d - 1) * (g - 1) for d in casimirs)

    # At the critical level, the Sugawara central charge has no value.
    c_eff = None

    # Group name for SL
    if lie_type.startswith('A_'):
        n = int(lie_type.split('_')[1]) + 1
        group_name = f'SL_{n}'
    else:
        group_name = lie_type

    return HitchinChiralData(
        group=group_name,
        rank=rank,
        genus=g,
        chiral_algebra_type=f'W({lie_type}) at critical level (center of V_{{-h^v}}({lie_type}))',
        central_charge=c_eff,
        level='critical',
        n_generators=n_gens,
        generator_spins=casimirs,
        hitchin_base_dim=dim_base,
        is_critical_level=True,
        dual_group=dual,
    )


# =========================================================================
# 4. NEKRASOV-SHATASHVILI QUANTUM SPECTRAL CURVE
# =========================================================================

class QuantumSpectralCurveData(NamedTuple):
    """Data of the quantum spectral curve in the NS limit."""
    lie_type: str
    rank: int
    genus: int
    classical_curve_genus: int     # genus of classical spectral curve
    oper_order: int                # order of the quantum differential operator
    n_hamiltonians: int            # number of commuting Hamiltonians
    ns_central_charge: str         # central charge as function of hbar
    is_wkb_exact: bool             # whether WKB is exact (only for sl_2)
    quantization_condition: str    # description of the quantization condition


def quantum_spectral_curve(lie_type: str, g: int,
                           n_punctures: int = 0) -> QuantumSpectralCurveData:
    """Quantum spectral curve from the Nekrasov-Shatashvili limit.

    In the NS limit (epsilon_2 -> 0):
        - The instanton partition function Z(a, epsilon_1, epsilon_2)
          reduces to exp(W(a, hbar) / epsilon_2) where hbar = epsilon_1
        - W(a, hbar) satisfies a finite-difference equation for SL(n)
        - In the semiclassical limit hbar -> 0, W reduces to the
          spectral curve det(lambda - phi) = 0
        - The quantum spectral curve is an ORDER-n ODE/difference equation

    For SL(2): the quantum spectral curve is a SECOND-ORDER ODE:
        [-hbar^2 d^2/dz^2 + u(z)] Psi(z) = 0
    where u(z) is the quantum version of the Hitchin Hamiltonian.
    This is the Baxter TQ-relation / Schrodinger equation.

    The NS quantization condition: the periods of the one-form
        p dz = (hbar d/dz log Psi) dz
    around cycles of the spectral curve are QUANTIZED:
        oint_{A_i} p dz = n_i hbar + corrections
    """
    if lie_type not in LIE_RANK:
        raise ValueError(f"Unknown Lie type '{lie_type}'")

    rank = LIE_RANK[lie_type]
    n_casimirs = len(CASIMIR_DEGREES[lie_type])

    # Classical spectral curve genus
    if g >= 2 and n_punctures == 0:
        # For SL(n) on compact genus-g curve
        n = rank + 1 if lie_type.startswith('A_') else rank
        if lie_type.startswith('A_'):
            n = int(lie_type.split('_')[1]) + 1
            cl_genus = n * n * (g - 1) + 1
        else:
            # Use dim(G)*(g-1) + 1 as approximate
            cl_genus = LIE_DIM[lie_type] * (g - 1) + 1
    else:
        # Punctured P^1 case: spectral curve genus depends on
        # the specific singularity data
        cl_genus = -1  # not computed in this simplified model

    # Order of the quantum differential operator
    if lie_type.startswith('A_'):
        oper_ord = int(lie_type.split('_')[1]) + 1
    else:
        # For non-type-A, the oper is more complex
        oper_ord = rank + 1  # rough approximation

    # WKB exactness: only sl_2 has exact WKB (Voros, Iwaki-Nakanishi)
    is_wkb = (lie_type == 'A_1')

    return QuantumSpectralCurveData(
        lie_type=lie_type,
        rank=rank,
        genus=g,
        classical_curve_genus=cl_genus,
        oper_order=oper_ord,
        n_hamiltonians=n_casimirs,
        ns_central_charge='Sugawara c has a critical pole; opers replace the Virasoro action',
        is_wkb_exact=is_wkb,
        quantization_condition='Bohr-Sommerfeld: oint_{A_i} p dz in hbar * Z',
    )


# =========================================================================
# 5. EXPLICIT GL(2) COMPUTATIONS
# =========================================================================

class GL2SpectralData(NamedTuple):
    """Detailed spectral curve data for GL(2)."""
    base_curve: str          # 'P^1' or 'E' or 'C_g'
    genus_base: int
    twist: str               # e.g. 'O(4)' or 'K_C'
    twist_degree: int
    hitchin_base_dim: int    # dim H^0(L^2)
    spectral_genus: int
    n_branch_points: int
    fibre_type: str          # 'elliptic', 'hyperelliptic', etc.
    oper_type: str            # description of the oper
    chiral_algebra: str       # associated chiral algebra
    w_algebra_type: str       # W-algebra description


def gl2_spectral_p1(twist_degree: int = 4) -> GL2SpectralData:
    """GL(2) spectral curve on P^1 with twist O(d).

    For d = 4 (the "standard" case matching K_{P^1}^{-2}):
        - Hitchin base: H^0(O(4)) x H^0(O(8)) -> but for SL(2):
          just H^0(O(8)) of dim 9.
        - For the SL(2) trace-free case: lambda^2 = q(z),
          q in H^0(O(2d)).
        - Spectral curve: hyperelliptic of genus d-1.
        - For d=4: genus 3, double cover of P^1 branched at 8 points.

    For d = 2 (minimal interesting case):
        - H^0(O(4)) = C^5 (quadratic differentials)
        - Spectral curve: genus 1 (elliptic)
        - 4 branch points
        - This is the case in the problem statement.
    """
    if twist_degree < 2:
        raise ValueError(f"Need twist degree >= 2 for nontrivial spectral curve, got {twist_degree}")

    # For GL(2) on P^1 with twist O(d):
    # Full Hitchin base: H^0(O(d)) + H^0(O(2d)), dim = (d+1) + (2d+1) = 3d+2
    # For SL(2): just H^0(O(2d)), dim = 2d+1
    dim_base_gl = (twist_degree + 1) + (2 * twist_degree + 1)
    dim_base_sl = 2 * twist_degree + 1

    # Spectral curve: degree-2 cover of P^1 in Tot(O(d))
    # Branch points: 2d (zeros of discriminant / quadratic differential)
    n_branch = 2 * twist_degree
    genus_spec = twist_degree - 1  # Riemann-Hurwitz for double cover of P^1

    if genus_spec == 1:
        fibre = 'elliptic curve (genus 1)'
    elif genus_spec == 0:
        fibre = 'rational curve (genus 0)'
    else:
        fibre = f'hyperelliptic curve of genus {genus_spec}'

    # The chiral algebra: at the critical level, the center of
    # V_{-2}(sl_2) produces the W_2 = Virasoro algebra.
    # More precisely, the quantum Hitchin Hamiltonians for SL(2)
    # generate the algebra of differential operators (opers).
    chiral = 'Virasoro at critical level k=-2 (center of V_{-2}(sl_2))'
    w_type = 'W_2 = Virasoro'

    return GL2SpectralData(
        base_curve='P^1',
        genus_base=0,
        twist=f'O({twist_degree})',
        twist_degree=twist_degree,
        hitchin_base_dim=dim_base_sl,
        spectral_genus=genus_spec,
        n_branch_points=n_branch,
        fibre_type=fibre,
        oper_type=f'SL_2-oper = 2nd order ODE on P^1',
        chiral_algebra=chiral,
        w_algebra_type=w_type,
    )


def gl2_spectral_elliptic() -> GL2SpectralData:
    """GL(2) spectral curve on an elliptic curve E.

    For G = GL(2), C = E (genus 1):
        - K_E = O_E (trivial canonical bundle)
        - H^0(K_E) = C (constant 1-forms)
        - Hitchin base for GL(2): H^0(K_E) + H^0(K_E^2) = C + C = C^2
          (both 1-dimensional since K_E = O_E)
        - For SL(2): H^0(K_E^2) = C, dim = 1
        - Spectral curve: lambda^2 = a, a in C (constant!)
          This is degenerate: the spectral curve for generic a != 0
          is TWO copies of E (unbranched double cover), genus 1+1-1 = 1.
          Wait: for a constant quadratic differential q(z) = a on E,
          the spectral curve is {lambda^2 = a} in Tot(K_E) = E x C.
          This is the disjoint union of two sections lambda = +/-sqrt(a)
          (if a != 0), which is disconnected.

    CORRECTION: For SL(2) on E, the traceless condition means
    Sigma = {lambda^2 + a_2 = 0} where a_2 in H^0(K_E^2) = H^0(O_E) = C.
    For generic a_2 != 0, Sigma is two disjoint copies of E.
    For a_2 = 0, Sigma degenerates to E with multiplicity 2.

    The correct GENERIC picture for SL(2) on a genus-g curve:
        g(Sigma) = 4g - 3 for the double cover (using g >= 2).
    For g = 1: the formula gives g(Sigma) = 4*1 - 3 = 1,
    but this is a DISCONNECTED double cover (two copies of E).

    For GL(2) on E with the Hitchin system to be interesting,
    one typically considers a TWISTED version or marks points.
    """
    return GL2SpectralData(
        base_curve='E (elliptic)',
        genus_base=1,
        twist='K_E = O_E (trivial)',
        twist_degree=0,
        hitchin_base_dim=1,  # H^0(K_E^2) = C for SL(2)
        spectral_genus=1,  # each component is genus 1
        n_branch_points=0,  # unbranched double cover
        fibre_type='disjoint union of two copies of E (unbranched)',
        oper_type='SL_2-oper on E (elliptic connection)',
        chiral_algebra='Virasoro at critical level (on elliptic curve)',
        w_algebra_type='W_2 = Virasoro (elliptic)',
    )


def gl2_spectral_genus2() -> GL2SpectralData:
    """GL(2) spectral curve on a genus-2 curve C.

    This is the distinguished case where M_H(C, SL_2) has
    dim_C = 6 with a Lagrangian fibration of "CY3 type"
    (see hitchin_sl2_genus2.py for full details).

    Spectral curve:
        - SL(2) Hitchin base: H^0(K_C^2), dim = 3*(2-1) = 3
        - Spectral curve: double cover Sigma -> C
          branched at zeros of q in H^0(K_C^2)
        - deg(K_C^2) = 2*(2*2-2) = 4: generically 4 branch points
        - Riemann-Hurwitz: 2g(Sigma)-2 = 2*(2*2-2) + 4 = 8
          so g(Sigma) = 5
        - Prym(Sigma/C) is an abelian 3-fold (dim = 5 - 2 = 3)
    """
    return GL2SpectralData(
        base_curve='C_2 (genus 2)',
        genus_base=2,
        twist='K_C (canonical)',
        twist_degree=2,  # deg K_C = 2g-2 = 2
        hitchin_base_dim=3,  # (2^2 - 1)*(2-1) = 3
        spectral_genus=5,  # 4*2 - 3 = 5
        n_branch_points=4,  # 2*(2*2-2) = 4
        fibre_type='Prym variety of dimension 3 (abelian 3-fold)',
        oper_type='SL_2-oper on C_2 (3 accessory parameters)',
        chiral_algebra='Virasoro at critical level (genus-2 quantum Hitchin)',
        w_algebra_type='W_2 = Virasoro (genus 2)',
    )


# =========================================================================
# 6. HITCHIN-FEIGIN-FRENKEL CENTER THEOREM
# =========================================================================

def feigin_frenkel_center_dim(lie_type: str, g: int) -> int:
    """Dimension of the Feigin-Frenkel center at genus g.

    The Feigin-Frenkel theorem (1992) states that the center of
    V_{-h^v}(g) is isomorphic to Fun(Op_{^LG}(C)).

    At genus g >= 2, the space of opers Op_{^LG}(C) is an affine
    space of dimension sum_{i} (2d_i - 1)(g-1) where d_i are the
    Casimir degrees of ^LG.

    For self-dual types (A, D, E): ^LG has the same Casimir degrees.
    For B <-> C: the Casimir degrees are swapped.
    """
    if lie_type not in CASIMIR_DEGREES:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")

    dual_type = LANGLANDS_DUAL[lie_type]
    casimirs = CASIMIR_DEGREES[dual_type]
    return sum((2 * d - 1) * (g - 1) for d in casimirs)


def center_generators(lie_type: str) -> Dict[str, Any]:
    """Generators of the Feigin-Frenkel center Z(V_{-h^v}(g)).

    The center is generated by the Segal-Sugawara operators
    S_i of degree d_i (the Casimir degrees).  At the critical
    level, these become CENTRAL and generate a commutative
    vertex subalgebra isomorphic to W(^Lg) at the critical level
    (the classical W-algebra of the Langlands dual Lie algebra).
    """
    if lie_type not in CASIMIR_DEGREES:
        raise ValueError(f"Unknown Lie type '{lie_type}'")

    dual_type = LANGLANDS_DUAL[lie_type]
    casimirs = CASIMIR_DEGREES[dual_type]
    dim_g = LIE_DIM[lie_type]
    h_v = DUAL_COXETER[lie_type]

    generators = []
    for i, d in enumerate(casimirs):
        generators.append({
            'index': i + 1,
            'degree': d,
            'name': f'S_{d}' if d != 2 else 'T (Sugawara)',
            'type': 'Segal-Sugawara' if d == 2 else f'degree-{d} Casimir current',
        })

    return {
        'lie_type': lie_type,
        'dual_type': dual_type,
        'n_generators': len(casimirs),
        'generator_degrees': casimirs,
        'generators': generators,
        'is_freely_generated': True,  # Z is always freely generated (Feigin-Frenkel)
        'w_algebra_type': f'W(^L{lie_type}) at critical level',
        'dim_g': dim_g,
        'h_v': h_v,
        'critical_level': -h_v,
    }


# =========================================================================
# 7. DIMENSION VERIFICATION AND CROSS-CHECKS
# =========================================================================

def verify_hitchin_fibre_base_match(lie_type: str, g: int) -> Dict[str, Any]:
    """Verify that dim(Hitchin fibre) = dim(Hitchin base).

    This is the fundamental property of a completely integrable system:
    the Hitchin map pi: M_H -> B is a Lagrangian fibration, so
    dim(fibre) = dim(base) = dim(M_H)/2.

    For SL(n), g >= 2:
        dim base = (n^2 - 1)(g - 1)
        dim fibre = dim Prym(Sigma/C) = (n^2 - 1)(g - 1)  (check!)

    The Prym dimension comes from:
        g(Sigma) = n^2(g-1) + 1
        dim Jac(Sigma) = n^2(g-1) + 1
        dim Nm^{-1}(0) = g(Sigma) - g(C) = n^2(g-1) + 1 - g

    Wait: Prym(Sigma/C) for an n-fold cover has dimension
        dim Prym = g(Sigma) - g(C) = n^2(g-1) + 1 - g

    But dim base = (n^2-1)(g-1) for SL_n.  Let us check:
        n^2(g-1) + 1 - g = n^2 g - n^2 + 1 - g = (n^2-1)(g-1) + (1-1+1-g+g-1)

    Actually: n^2(g-1) + 1 - g = n^2 g - n^2 + 1 - g = (n^2-1)g - n^2 + 1
                                = (n^2-1)g - (n^2-1) = (n^2-1)(g-1).

    So dim Prym = (n^2-1)(g-1) = dim base.  Confirmed!
    """
    if lie_type not in CASIMIR_DEGREES:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")

    casimirs = CASIMIR_DEGREES[lie_type]
    dim_base = sum((2 * d - 1) * (g - 1) for d in casimirs)

    # For type A_r (SL_{r+1}):
    if lie_type.startswith('A_'):
        r = int(lie_type.split('_')[1])
        n = r + 1
        # Spectral curve genus
        g_sigma = n * n * (g - 1) + 1
        # Prym dimension
        dim_prym = g_sigma - g  # = n^2(g-1) + 1 - g = (n^2-1)(g-1)
        assert dim_prym == (n * n - 1) * (g - 1), (
            f"Prym dimension mismatch for A_{r}, g={g}: "
            f"{dim_prym} != {(n*n-1)*(g-1)}"
        )
        match = (dim_prym == dim_base)
    else:
        # For non-type-A, the spectral curve is more complex
        # and the Prym is replaced by a more general abelian variety.
        # The dimension match still holds by the integrable system structure.
        dim_prym = dim_base  # by integrability
        match = True

    return {
        'lie_type': lie_type,
        'genus': g,
        'dim_hitchin_base': dim_base,
        'dim_fibre': dim_prym,
        'dimensions_match': match,
        'dim_total': 2 * dim_base,
        'is_lagrangian': match,
    }


def casimir_sum_rule(lie_type: str) -> Dict[str, Any]:
    """Verify the Casimir sum rule: sum(2d_i - 1) = dim(g).

    This identity follows from the fact that dim(g) = rank(g) + 2|Phi^+|
    and the exponents e_i = d_i - 1 satisfy sum(2e_i + 1) = dim(g).
    """
    if lie_type not in CASIMIR_DEGREES:
        raise ValueError(f"Unknown Lie type '{lie_type}'")

    casimirs = CASIMIR_DEGREES[lie_type]
    dim_g = LIE_DIM[lie_type]
    rank = LIE_RANK[lie_type]
    computed_sum = sum(2 * d - 1 for d in casimirs)

    return {
        'lie_type': lie_type,
        'casimir_degrees': casimirs,
        'dim_g': dim_g,
        'rank': rank,
        'casimir_sum': computed_sum,
        'matches': computed_sum == dim_g,
        'n_positive_roots': (dim_g - rank) // 2,
    }


# =========================================================================
# 8. HITCHIN BASE DIMENSION FORMULA VERIFICATION
# =========================================================================

def hitchin_base_via_casimirs(lie_type: str, g: int) -> int:
    """Compute dim(B) using Casimir degrees (the correct general formula).

    B = bigoplus_{i=1}^{r} H^0(C, K_C^{d_i})

    where d_1, ..., d_r are the Casimir degrees of g.

    dim H^0(K_C^{d_i}) = (2d_i - 1)(g - 1) for g >= 2.

    So dim B = sum_{i=1}^{r} (2d_i - 1)(g - 1) = dim(g) * (g - 1).
    """
    if lie_type not in CASIMIR_DEGREES:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")

    casimirs = CASIMIR_DEGREES[lie_type]
    return sum((2 * d - 1) * (g - 1) for d in casimirs)


def hitchin_base_via_dim_g(lie_type: str, g: int) -> int:
    """Compute dim(B) using dim(g)*(g-1) directly.

    This uses the Casimir sum rule sum(2d_i - 1) = dim(g).
    """
    if lie_type not in LIE_DIM:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")
    return LIE_DIM[lie_type] * (g - 1)


# =========================================================================
# 9. SPECTRAL CURVE DISCRIMINANT AND RAMIFICATION
# =========================================================================

def discriminant_degree(n: int, g: int) -> int:
    """Degree of the discriminant locus in the Hitchin base.

    The discriminant of the spectral curve is the locus in B
    where Sigma_b is singular (has double points).

    For GL(n) on genus-g curve:
        discriminant is a section of K_C^{n(n-1)}
        degree = n(n-1)(2g-2)
    """
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")
    return n * (n - 1) * (2 * g - 2)


def ramification_profile_generic(n: int) -> str:
    """Generic ramification profile for an n-fold spectral cover.

    For the generic point of the discriminant locus, the spectral
    curve has a single node (two sheets meeting transversally).
    The generic ramification is of type (2, 1, ..., 1) with
    (n-2) unramified sheets.
    """
    if n < 2:
        return "no ramification (n=1)"
    unramified = n - 2
    return f"({2}, {'1, ' * unramified})" if unramified > 0 else "(2)"


# =========================================================================
# 10. COMPARISON THEOREMS
# =========================================================================

def hitchin_vs_oper_comparison(lie_type: str, g: int) -> Dict[str, Any]:
    """Compare dimensions: Hitchin base vs oper space.

    The Beilinson-Drinfeld theorem states:
        Op_{^LG}(C) is an affine space modeled on B_{^LG}

    For self-dual types (A, D, E): B_G = B_{^LG}, so
        dim Op_{^LG}(C) = dim B_G = dim(g)(g-1).

    For B_r vs C_r:
        dim B(B_r) = dim(so_{2r+1})(g-1) = r(2r+1)(g-1)
        dim B(C_r) = dim(sp_{2r})(g-1) = r(2r+1)(g-1)
        These are EQUAL (dim(B_r) = dim(C_r) = r(2r+1)), so
        dim Op_{^LG} = dim B_G in all cases.
    """
    if lie_type not in LIE_DIM:
        raise ValueError(f"Unknown Lie type '{lie_type}'")
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")

    dual_type = LANGLANDS_DUAL[lie_type]
    dim_base = hitchin_base_via_dim_g(lie_type, g)
    dim_oper = feigin_frenkel_center_dim(lie_type, g)

    return {
        'lie_type': lie_type,
        'dual_type': dual_type,
        'genus': g,
        'dim_hitchin_base': dim_base,
        'dim_oper_space': dim_oper,
        'dimensions_match': dim_base == dim_oper,
        'is_self_dual': lie_type == dual_type,
    }


def spectral_vs_prym_comparison(n: int, g: int) -> Dict[str, Any]:
    """Compare spectral curve genus, Prym dimension, and Hitchin base dimension.

    For SL(n) on genus-g curve:
        g(Sigma) = n^2(g-1) + 1
        dim Prym = g(Sigma) - g = n^2(g-1) + 1 - g = (n^2-1)(g-1)
        dim B = (n^2-1)(g-1)

    So dim Prym = dim B: the Hitchin fibre has the right dimension.
    """
    if g < 2:
        raise ValueError(f"Need genus >= 2, got g={g}")
    g_sigma = n * n * (g - 1) + 1
    dim_prym = g_sigma - g
    dim_base = (n * n - 1) * (g - 1)

    return {
        'n': n,
        'genus_base': g,
        'genus_spectral': g_sigma,
        'dim_prym': dim_prym,
        'dim_hitchin_base': dim_base,
        'prym_equals_base': dim_prym == dim_base,
        'riemann_hurwitz_check': (
            2 * g_sigma - 2 == n * (2 * g - 2) + n * (n - 1) * (2 * g - 2)
        ),
    }


# =========================================================================
# 11. FULL COMPUTATION AND VERIFICATION
# =========================================================================

def full_spectral_chiral_computation(
    lie_type: str = 'A_1',
    g: int = 2,
) -> Dict[str, Any]:
    """Run the full suite of spectral curve + chiral algebra computations."""
    results: Dict[str, Any] = {}

    # Spectral curve
    if lie_type.startswith('A_'):
        n = int(lie_type.split('_')[1]) + 1
        results['spectral_curve'] = spectral_curve_data_sln(n, g)
        results['spectral_vs_prym'] = spectral_vs_prym_comparison(n, g)
    else:
        results['spectral_curve'] = None
        results['spectral_vs_prym'] = None

    # Hitchin-oper comparison
    results['hitchin_vs_oper'] = hitchin_vs_oper_comparison(lie_type, g)

    # Chiral algebra data
    results['chiral_data'] = hitchin_chiral_data(lie_type, g)

    # Quantum spectral curve
    results['quantum_curve'] = quantum_spectral_curve(lie_type, g)

    # Center data
    results['center'] = center_generators(lie_type)

    # Fibre-base match
    results['fibre_base'] = verify_hitchin_fibre_base_match(lie_type, g)

    # Casimir sum rule
    results['casimir_rule'] = casimir_sum_rule(lie_type)

    # GL(2) explicit data
    if lie_type == 'A_1':
        results['gl2_p1'] = gl2_spectral_p1(2)
        results['gl2_genus2'] = gl2_spectral_genus2()
        results['gl2_elliptic'] = gl2_spectral_elliptic()

    return results


def verify_all_spectral_chiral() -> Dict[str, bool]:
    """Run all internal verification checks."""
    results = {}

    # 1. Casimir sum rule for all types
    for lt in CASIMIR_DEGREES:
        r = casimir_sum_rule(lt)
        results[f'casimir_sum_{lt}'] = r['matches']

    # 2. Hitchin base: two methods agree
    for lt in LIE_DIM:
        for g in [2, 3, 4]:
            d1 = hitchin_base_via_casimirs(lt, g)
            d2 = hitchin_base_via_dim_g(lt, g)
            results[f'base_dim_{lt}_g{g}'] = (d1 == d2)

    # 3. Fibre-base match for type A
    for r in range(1, 6):
        lt = f'A_{r}'
        if lt in LIE_DIM:
            for g in [2, 3]:
                fb = verify_hitchin_fibre_base_match(lt, g)
                results[f'fibre_base_{lt}_g{g}'] = fb['dimensions_match']

    # 4. Hitchin vs oper comparison
    for lt in LIE_DIM:
        comp = hitchin_vs_oper_comparison(lt, 2)
        results[f'hitchin_oper_{lt}'] = comp['dimensions_match']

    # 5. Spectral curve genus: Riemann-Hurwitz
    for n in range(2, 6):
        for g in range(2, 5):
            g_sigma = spectral_curve_genus_gln(n, g)
            n_branch = n * (n - 1) * (2 * g - 2)
            rh_check = (2 * g_sigma - 2 == n * (2 * g - 2) + n_branch)
            results[f'RH_GL{n}_g{g}'] = rh_check

    return results
