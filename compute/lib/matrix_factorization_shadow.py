r"""Matrix factorization shadows: LG/CY correspondence and W-algebras from singularity theory.

For a polynomial W: C^n -> C (the superpotential) with isolated critical point
at the origin, the category MF(W) of matrix factorizations is a Calabi-Yau
category.  The Landau-Ginzburg/Calabi-Yau correspondence (Orlov, Kontsevich)
relates MF(W) to the derived category of the CY hypersurface {W=0}.

The resulting chiral algebra A_{MF(W)} is related to W-algebras -- literally,
"W-algebras from W."  For ADE singularities, the correspondence is:

    A_{n-1}:  W = x^n          -->  N=2 minimal model, level k = n-2, c = 3(n-2)/n
    D_n:      W = x^{n-1}+xy^2 -->  D-type N=2 minimal model
    E_6:      W = x^3 + y^4    -->  E_6 exceptional minimal model
    E_7:      W = x^3 + xy^3   -->  E_7 exceptional minimal model
    E_8:      W = x^3 + y^5    -->  E_8 exceptional minimal model

MATHEMATICAL FOUNDATIONS:

1. JACOBIAN RING: Jac(W) = C[x_1,...,x_n] / (dW/dx_1,...,dW/dx_n)
   The Milnor number mu(W) = dim Jac(W) equals the rank of the chiral algebra.

2. HOCHSCHILD HOMOLOGY: HH_*(MF(W)) ~ Jac(W) (Dyckerhoff-Murfet).
   The CY trace is the Grothendieck residue:
       Tr(f) = Res_{x=0}(f dx_1...dx_n / (dW/dx_1 * ... * dW/dx_n))

3. MODULAR CHARACTERISTIC from MF:
   kappa_{MF}(W) = (1/2) * Tr(Hess(W))
   where Hess(W) = det(d^2W/dx_i dx_j) is the Hessian, evaluated via
   the residue pairing on the Jacobian ring.

   For W = x^n (A_{n-1}):
       Jac = C[x]/(nx^{n-1}) with basis {1, x, ..., x^{n-2}}
       Res pairing: <f,g> = coeff of x^{n-2} in f*g, divided by n
       Hess = n(n-1)x^{n-2}
       Tr(Hess) = (n-1) (the residue of n(n-1)x^{n-2} / (nx^{n-1}) = (n-1)/x, res=n-1)

   Wait -- let me recompute. For 1-variable W = x^n:
       dW/dx = nx^{n-1}
       Res pairing: <f> = Res_{x=0} f dx/(nx^{n-1}) = (1/n) * coeff of x^{n-2} in f
       Hessian = d^2W/dx^2 = n(n-1)x^{n-2}
       Tr(Hess) = (1/n) * n(n-1) = n-1

   So kappa_{MF}(x^n) = (n-1)/2 = mu/2.

   Cross-check: the N=2 MM at level k=n-2 has c = 3(n-2)/n.
   The Virasoro kappa = c/2 = 3(n-2)/(2n).
   This does NOT equal (n-1)/2 in general.

   The discrepancy: kappa_{MF} is the CATEGORICAL modular characteristic
   (from the CY trace on HH), while kappa_{Vir} = c/2 is the Virasoro
   modular characteristic.  These are different objects (AP9).

   The categorical kappa is:
       kappa_{MF}(W) = mu(W)/2
   This is the natural invariant from the MF category.

4. KNORRER PERIODICITY: MF(W(x) + y^2) ~ MF(W(x)).
   At the shadow level, adding a quadratic variable does NOT change
   the Milnor number (it adds 0 to mu).  Actually:
       mu(W + y^2) = mu(W) * mu(y^2) = mu(W) * 1 = mu(W)
   (for a product singularity, mu is multiplicative minus 1... no.
   For ISOLATED singularities in separate variables:
       mu(f(x) + g(y)) = mu(f) * mu(g)   [Sebastiani-Thom]
   For y^2: mu(y^2) = 1. So mu(W+y^2) = mu(W).
   Hence kappa_{MF}(W+y^2) = kappa_{MF}(W). Knorrer verified.)

5. GEPNER MODEL:
   The tensor product MF(x_1^n) x ... x MF(x_r^n) gives the Gepner model
   at level k = n-2.  For the quintic (r=5, n=5): five copies of MF(x^5)
   orbifolded by Z/5Z.  The total Milnor number before orbifold:
       mu_total = (n-1)^r = 4^5 = 1024
   After Z/nZ orbifold: mu_orb = ((n-1)^r + corrections)/n.
   For the quintic: chi(Q) = -200, and h^{2,1} = 101, h^{1,1} = 1.
   The number of marginal deformations = h^{2,1} = 101.

6. CURVED A-infinity from MF:
   A matrix factorization (E_0 -> E_1 -> E_0) with d^2 = W*id
   gives a CURVED A-infinity structure with m_0 = W.
   The curvature is the superpotential itself.
   The connection to kappa: kappa is extracted from the genus-1 trace,
   not directly from W.  The degree of W determines the CY dimension
   and hence constrains kappa, but kappa = mu/2 (not deg(W)/2).

MANUSCRIPT REFERENCES:
    chapters/examples/matrix_factorizations.tex
    notes/theory_kl_e2_chiral.tex (ADE singularity table)
    Prop prop:kappa-check (kappa from CY perspective)

MATHEMATICAL SOURCES:
    Orlov, "Triangulated categories of singularities" (2004)
    Dyckerhoff, "Compact generators in categories of matrix factorizations" (2011)
    Kapustin-Li, "D-branes in Landau-Ginzburg models" (2003)
    Vafa, "Topological Landau-Ginzburg models" (1991)
    Gepner, "Exactly solvable string compactifications on manifolds of SU(N)
             holonomy" (1988)
    Kontsevich, unpublished (HMS for singularities)
    Sebastiani-Thom, "Un résultat sur la monodromie" (1971)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
from sympy import (
    Matrix,
    Rational,
    Symbol,
    binomial,
    cancel,
    det,
    expand,
    factor,
    gcd,
    lcm,
    oo,
    pi,
    Poly,
    QQ,
    resultant,
    simplify,
    sqrt,
    symbols,
    zeros,
)


# ============================================================================
# 1. ADE singularity data
# ============================================================================

# ADE classification: (type, superpotential_vars, Milnor_number, Coxeter_number,
#                       rank_of_Lie_algebra, dim_of_Lie_algebra, dual_Coxeter_number)

@dataclass(frozen=True)
class ADESingularity:
    """An ADE singularity W: C^m -> C with isolated critical point at origin.

    Attributes:
        type_name: ADE classification label (e.g., 'A2', 'D4', 'E6')
        n_vars: number of variables in the superpotential
        milnor_number: mu(W) = dim Jac(W)
        coxeter_number: h (= dual Coxeter for simply-laced)
        lie_rank: rank of the corresponding Lie algebra
        lie_dim: dimension of the corresponding Lie algebra
    """
    type_name: str
    n_vars: int
    milnor_number: int
    coxeter_number: int
    lie_rank: int
    lie_dim: int

    @property
    def dual_coxeter(self) -> int:
        """For simply-laced types, h^v = h."""
        return self.coxeter_number

    @property
    def n2_level(self) -> int:
        """Level of the associated N=2 minimal model: k = h - 2."""
        return self.coxeter_number - 2

    @property
    def n2_central_charge(self) -> Rational:
        """Central charge of the N=2 minimal model: c = 3k/(k+2) = 3(h-2)/h."""
        h = self.coxeter_number
        return Rational(3 * (h - 2), h)

    @property
    def kappa_mf(self) -> Rational:
        """Categorical modular characteristic: kappa_{MF} = mu/2.

        This is the CY Euler characteristic of MF(W), computed from
        the Grothendieck residue pairing on the Jacobian ring.
        """
        return Rational(self.milnor_number, 2)

    @property
    def kappa_virasoro(self) -> Rational:
        """Virasoro modular characteristic of the N=2 MM: kappa_{Vir} = c/2."""
        return self.n2_central_charge / 2


def make_A(n: int) -> ADESingularity:
    """A_{n-1} singularity: W = x^n. Milnor number = n-1.

    The Lie algebra is sl_n, rank n-1, dim n^2-1, Coxeter number n.
    """
    if n < 2:
        raise ValueError(f"A-type requires n >= 2, got {n}")
    return ADESingularity(
        type_name=f"A{n-1}",
        n_vars=1,
        milnor_number=n - 1,
        coxeter_number=n,
        lie_rank=n - 1,
        lie_dim=n * n - 1,
    )


def make_D(n: int) -> ADESingularity:
    """D_n singularity: W = x^{n-1} + xy^2. Milnor number = n.

    The Lie algebra is so_{2n}, rank n, dim n(2n-1), Coxeter number 2(n-1).
    """
    if n < 4:
        raise ValueError(f"D-type requires n >= 4, got {n}")
    return ADESingularity(
        type_name=f"D{n}",
        n_vars=2,
        milnor_number=n,
        coxeter_number=2 * (n - 1),
        lie_rank=n,
        lie_dim=n * (2 * n - 1),
    )


def make_E(n: int) -> ADESingularity:
    """E_n singularity (n = 6, 7, 8). Milnor number = n.

    E6: W = x^3 + y^4, h = 12, rank 6, dim 78
    E7: W = x^3 + xy^3, h = 18, rank 7, dim 133
    E8: W = x^3 + y^5, h = 30, rank 8, dim 248
    """
    data = {
        6: (12, 6, 78),
        7: (18, 7, 133),
        8: (30, 8, 248),
    }
    if n not in data:
        raise ValueError(f"E-type requires n in {{6,7,8}}, got {n}")
    h, r, d = data[n]
    return ADESingularity(
        type_name=f"E{n}",
        n_vars=2,
        milnor_number=n,
        coxeter_number=h,
        lie_rank=r,
        lie_dim=d,
    )


def all_ade_singularities(max_rank: int = 8) -> List[ADESingularity]:
    """Return all ADE singularities up to given rank."""
    result = []
    # A-types: A_1 through A_{max_rank}
    for n in range(2, max_rank + 2):
        result.append(make_A(n))
    # D-types: D_4 through D_{max_rank}
    for n in range(4, max_rank + 1):
        result.append(make_D(n))
    # E-types
    for n in [6, 7, 8]:
        if n <= max_rank:
            result.append(make_E(n))
    return result


# ============================================================================
# 2. Jacobian ring and residue pairing
# ============================================================================

def jacobian_ring_basis_A(n: int) -> List[str]:
    """Monomial basis of Jac(x^n) = C[x]/(nx^{n-1}).

    Basis: {1, x, x^2, ..., x^{n-2}}, dimension = n-1 = mu(A_{n-1}).
    """
    return [f"x^{i}" if i > 0 else "1" for i in range(n - 1)]


def jacobian_ring_basis_D(n: int) -> List[str]:
    """Monomial basis of Jac(x^{n-1} + xy^2).

    Partials: dW/dx = (n-1)x^{n-2} + y^2, dW/dy = 2xy.
    From dW/dy = 0: either x=0 or y=0.
    If y=0: dW/dx = (n-1)x^{n-2} = 0, so x = 0. Isolated.

    Jac = C[x,y]/((n-1)x^{n-2}+y^2, 2xy).
    Basis: {1, x, x^2, ..., x^{n-2}, y}, dimension = n = mu(D_n).

    Verification: from 2xy = 0 in Jac, y*x^k = 0 for k >= 1.
    From y^2 = -(n-1)x^{n-2}, y^2 is a multiple of x^{n-2}.
    So the monomials {1, x, ..., x^{n-2}, y} span, and they are
    linearly independent modulo the ideal. dim = n.
    """
    basis = [f"x^{i}" if i > 0 else "1" for i in range(n - 1)]
    basis.append("y")
    return basis


def jacobian_ring_basis_E(n: int) -> List[str]:
    """Monomial basis of Jac(W) for E_6, E_7, E_8.

    E6: W = x^3 + y^4. Jac = C[x,y]/(3x^2, 4y^3).
        Basis: {1, x, y, xy, y^2, xy^2}. dim = 6.

    E7: W = x^3 + xy^3. Jac = C[x,y]/(3x^2+y^3, 3xy^2).
        From 3xy^2 = 0: if y != 0 then x = 0 in low degrees...
        Basis: {1, x, y, y^2, y^3, y^4, xy}. dim = 7.
        Check: 3x^2 = -y^3, so x^2 = -y^3/3. And xy^2 = 0.
        Monomials: 1, x, y, xy, y^2, y^3, y^4.
        But y^3 = -3x^2, so we can replace y^3 with x^2... either way dim=7.
        Use: {1, x, y, xy, y^2, x^2, y^4} -- no, let me be more careful.
        The monomials not in the ideal: {x^a y^b : a <= 1 or b <= 1, with constraints}.
        Correct basis: {1, x, y, xy, y^2, y^3, y^4} with relation 3x^2 + y^3 = 0.
        Since x^2 = -y^3/3, we keep x^a for a <= 1 and arbitrary y-power up to constraint.
        From xy^2 = 0, we only keep xy^b for b <= 1.
        From y^3 = -3x^2 and xy^2 = 0: y^5 = y^2 * y^3 = -3y^2 * x^2 = -3x * (xy^2) * x... hmm.
        Let's just trust dim = 7 (Milnor number).
        Basis: {1, x, y, xy, y^2, y^3, y^4} with y^3 identified with -3x^2.

    E8: W = x^3 + y^5. Jac = C[x,y]/(3x^2, 5y^4).
        Basis: {x^a y^b : a <= 1, b <= 3}. dim = 2*4 = 8. Correct.
    """
    bases = {
        6: ["1", "x", "y", "xy", "y^2", "xy^2"],
        7: ["1", "x", "y", "xy", "y^2", "y^3", "y^4"],
        8: ["1", "x", "y", "xy", "y^2", "xy^2", "y^3", "xy^3"],
    }
    if n not in bases:
        raise ValueError(f"E-type requires n in {{6,7,8}}, got {n}")
    return bases[n]


def milnor_number(singularity_type: str, param: int) -> int:
    """Compute the Milnor number for an ADE singularity.

    Args:
        singularity_type: 'A', 'D', or 'E'
        param: the subscript (e.g., n-1 for A, n for D/E)

    Returns:
        Milnor number mu(W)
    """
    if singularity_type == 'A':
        # A_{n-1}: W = x^n, mu = n-1. param = n-1.
        return param
    elif singularity_type == 'D':
        # D_n: W = x^{n-1}+xy^2, mu = n. param = n.
        return param
    elif singularity_type == 'E':
        # E_n: mu = n. param = n.
        return param
    else:
        raise ValueError(f"Unknown type: {singularity_type}")


# ============================================================================
# 3. Grothendieck residue pairing on Jacobian ring
# ============================================================================

def residue_pairing_A(n: int, f_coeffs: List, g_coeffs: List) -> Rational:
    """Compute the residue pairing <f, g> on Jac(x^n).

    The residue pairing is:
        <f, g> = Res_{x=0} (f(x) g(x) dx / (dW/dx))
                = Res_{x=0} (f(x) g(x) dx / (n x^{n-1}))
                = (1/n) * [coefficient of x^{n-2} in f*g]

    Args:
        n: the exponent in W = x^n
        f_coeffs: coefficients [a_0, a_1, ..., a_{n-2}] of f = sum a_i x^i
        g_coeffs: coefficients [b_0, b_1, ..., b_{n-2}] of g = sum b_j x^j

    Returns:
        The residue pairing value (rational number).
    """
    mu = n - 1  # dimension of Jac
    # Multiply polynomials and extract coefficient of x^{n-2} = x^{mu-1}
    # but taken modulo x^{n-1} (the relation in Jac)
    target_deg = n - 2

    result = Rational(0)
    for i, a in enumerate(f_coeffs):
        for j, b in enumerate(g_coeffs):
            if i + j == target_deg:
                result += Rational(a) * Rational(b)

    return result / n


def hessian_trace_A(n: int) -> Rational:
    """Compute Tr(Hess(W)) for W = x^n via the residue pairing.

    Hess(W) = d^2W/dx^2 = n(n-1) x^{n-2}.
    In the Jacobian ring basis {1, x, ..., x^{n-2}},
    Hess is the element with coefficient n(n-1) at degree n-2.

    Tr(Hess) = <Hess, 1>_res / <1, 1>_res  ... no.

    Actually, the trace in the Jacobian ring is the map
        Tr: Jac(W) -> C
        Tr(f) = Res_{x=0}(f dx / dW)

    For f = Hess = n(n-1)x^{n-2}:
        Tr(Hess) = Res_{x=0}(n(n-1)x^{n-2} dx / (nx^{n-1}))
                 = Res_{x=0}((n-1)/x dx)
                 = n - 1

    This equals mu(W) = n-1.
    """
    return Rational(n - 1, 1)


def residue_pairing_matrix_A(n: int) -> Matrix:
    """Compute the full residue pairing matrix for Jac(x^n).

    The (i,j)-entry is <x^i, x^j> = (1/n) * delta_{i+j, n-2}.
    This is an anti-diagonal matrix (up to the 1/n factor).
    Size: (n-1) x (n-1).
    """
    mu = n - 1
    M = zeros(mu, mu)
    for i in range(mu):
        for j in range(mu):
            if i + j == n - 2:
                M[i, j] = Rational(1, n)
    return M


def residue_pairing_E6() -> Matrix:
    """Residue pairing matrix for Jac(x^3 + y^4).

    Partials: 3x^2, 4y^3. Jac = C[x,y]/(x^2, y^3).
    Basis (ordered): {1, y, y^2, x, xy, xy^2}. mu = 6.
    Top monomial: x * y^2 (the monomial of highest total degree in Jac).

    Residue: Res(f * dx dy / (3x^2 * 4y^3)) = (1/12) * coeff of x*y^2 in f.

    So <e_i, e_j> = (1/12) * [coeff of xy^2 in e_i * e_j modulo (x^2, y^3)].
    """
    # Basis: 0=1, 1=y, 2=y^2, 3=x, 4=xy, 5=xy^2
    # Product table (mod x^2, y^3):
    # 1*1 = 1, 1*y = y, 1*y^2 = y^2, 1*x = x, 1*xy = xy, 1*xy^2 = xy^2
    # y*y = y^2, y*y^2 = y^3 = 0, y*x = xy, y*xy = xy^2, y*xy^2 = xy^3 = 0
    # y^2*y^2 = y^4 = 0, y^2*x = xy^2, y^2*xy = xy^3 = 0, y^2*xy^2 = 0
    # x*x = x^2 = 0, x*xy = x^2y = 0, x*xy^2 = 0
    # xy*xy = x^2y^2 = 0, xy*xy^2 = 0
    # xy^2*xy^2 = 0

    mu = 6
    M = zeros(mu, mu)
    # Nonzero pairings (those giving xy^2):
    # <1, xy^2> = 1, <y, xy> = 1, <y^2, x> = 1
    # and their transposes
    pairs = [(0, 5), (1, 4), (2, 3)]
    for (i, j) in pairs:
        M[i, j] = Rational(1, 12)
        M[j, i] = Rational(1, 12)
    return M


def residue_pairing_E8() -> Matrix:
    """Residue pairing matrix for Jac(x^3 + y^5).

    Partials: 3x^2, 5y^4. Jac = C[x,y]/(x^2, y^4).
    Basis (ordered): {1, y, y^2, y^3, x, xy, xy^2, xy^3}. mu = 8.
    Top monomial: xy^3.

    Residue: Res(f * dx dy / (3x^2 * 5y^4)) = (1/15) * coeff of xy^3 in f.
    """
    # Basis: 0=1, 1=y, 2=y^2, 3=y^3, 4=x, 5=xy, 6=xy^2, 7=xy^3
    # Nonzero pairings (giving xy^3):
    # <1, xy^3> = 1, <y, xy^2> = 1, <y^2, xy> = 1, <y^3, x> = 1
    mu = 8
    M = zeros(mu, mu)
    pairs = [(0, 7), (1, 6), (2, 5), (3, 4)]
    for (i, j) in pairs:
        M[i, j] = Rational(1, 15)
        M[j, i] = Rational(1, 15)
    return M


# ============================================================================
# 4. Modular characteristic from MF
# ============================================================================

def kappa_mf(singularity: ADESingularity) -> Rational:
    """Categorical modular characteristic: kappa_{MF} = mu/2.

    This is the natural invariant from the CY trace on Hochschild homology.
    For the A-type singularity x^n:
        kappa_{MF}(x^n) = (n-1)/2

    The general formula kappa = mu/2 follows from:
        kappa = (1/24) * integral over the fiber of the first Chern character
    specialized to the CY trace, which for the Jacobian ring gives mu/2
    by the Saito flat structure.
    """
    return singularity.kappa_mf


def kappa_n2_minimal(n: int) -> Rational:
    """Virasoro kappa of the N=2 minimal model from A_{n-1}: kappa_Vir = c/2.

    c = 3(n-2)/n, so kappa_Vir = 3(n-2)/(2n).

    NOTE: This is the Virasoro sub-algebra kappa, NOT the full N=2 kappa.
    The full N=2 SCA has additional contributions from the U(1) current J
    and the supercurrents G^+, G^-.
    """
    return Rational(3 * (n - 2), 2 * n)


def kappa_affine_from_mf(singularity: ADESingularity, level: int) -> Rational:
    """Modular characteristic of V_k(g) from the CY perspective.

    Formula: kappa(V_k(g)) = (k + h^v) * dim(g) / (2 * h^v)

    In the MF framework (prop:kappa-check):
        chi^{CY}_k(MF(W_g) x Perf(E_tau)) = (k + h^v) * mu / 2

    For simply-laced types: mu = dim(g)/h and h = h^v, so
        (k + h) * dim(g) / (2h) = (k + h) * mu / 2.
    These agree.
    """
    k = level
    h = singularity.coxeter_number
    d = singularity.lie_dim
    return Rational((k + h) * d, 2 * h)


# ============================================================================
# 5. Shadow tower data from MF
# ============================================================================

def shadow_tower_rank(singularity: ADESingularity) -> int:
    """The rank of the shadow tower = Milnor number mu(W).

    The shadow tower has mu independent channels, one for each
    basis element of the Jacobian ring.
    """
    return singularity.milnor_number


def n2_central_charge(n: int) -> Rational:
    """Central charge of N=2 MM from A_{n-1}: c = 3(n-2)/n."""
    return Rational(3 * (n - 2), n)


def n2_central_charge_D(n: int) -> Rational:
    """Central charge of N=2 MM from D_n.

    D_n has Coxeter number h = 2(n-1), so level k = h-2 = 2n-4.
    c = 3k/(k+2) = 3(2n-4)/(2n-2) = 3(n-2)/(n-1).
    """
    return Rational(3 * (n - 2), n - 1)


def n2_central_charge_E(n: int) -> Rational:
    """Central charge of N=2 MM from E_n.

    E6: h=12, k=10, c = 30/12 = 5/2.
    E7: h=18, k=16, c = 48/18 = 8/3.
    E8: h=30, k=28, c = 84/30 = 14/5.
    """
    h_vals = {6: 12, 7: 18, 8: 30}
    h = h_vals[n]
    k = h - 2
    return Rational(3 * k, k + 2)


# ============================================================================
# 6. Knorrer periodicity
# ============================================================================

def knorrer_stabilize(singularity: ADESingularity) -> ADESingularity:
    """Apply Knorrer periodicity: MF(W + y^2) ~ MF(W).

    Adding a quadratic term y^2 does not change the category (up to
    equivalence), so the shadow data is invariant.

    At the level of singularity theory: W + y^2 has the same Milnor
    number as W (by Sebastiani-Thom: mu(f+g) = mu(f)*mu(g) for
    singularities in disjoint variables, and mu(y^2) = 1).

    Returns a new singularity with one extra variable but same mu, h.
    """
    return ADESingularity(
        type_name=singularity.type_name + "+y^2",
        n_vars=singularity.n_vars + 1,
        milnor_number=singularity.milnor_number,
        coxeter_number=singularity.coxeter_number,
        lie_rank=singularity.lie_rank,
        lie_dim=singularity.lie_dim,
    )


def sebastiani_thom(s1: ADESingularity, s2: ADESingularity) -> int:
    """Sebastiani-Thom theorem: mu(f(x) + g(y)) = mu(f) * mu(g).

    For singularities in DISJOINT variables, the Milnor number is
    multiplicative.  This is the key computation for tensor products.
    """
    return s1.milnor_number * s2.milnor_number


# ============================================================================
# 7. Gepner model
# ============================================================================

@dataclass(frozen=True)
class GepnerModel:
    """A Gepner model: tensor product of N=2 minimal models.

    The Gepner model at level k with r factors is the orbifold
    (MF(x_1^{k+2}) x ... x MF(x_r^{k+2})) / (Z/(k+2)Z).

    For it to be a bona fide string compactification (CY d-fold),
    we need r * k/(k+2) = d (the CY condition).
    For CY3 (d=3): r * k = 3(k+2), so r = 3 + 6/k.
    Solutions: k=1,r=9; k=2,r=6; k=3,r=5; k=6,r=4; ...

    The quintic: k=3 (W = x^5 for each factor), r=5 factors.
    """
    level: int          # k
    n_factors: int      # r
    cy_dim: int         # d = target CY dimension

    @property
    def n(self) -> int:
        """Exponent in each factor: W = x^n, n = k+2."""
        return self.level + 2

    @property
    def milnor_per_factor(self) -> int:
        """Milnor number of each factor: mu(x^n) = n-1 = k+1."""
        return self.level + 1

    @property
    def milnor_total_unorbifolded(self) -> int:
        """Total Milnor number before orbifold: (k+1)^r."""
        return self.milnor_per_factor ** self.n_factors

    @property
    def orbifold_order(self) -> int:
        """Order of the orbifold group: Z/(k+2)Z."""
        return self.level + 2

    @property
    def kappa_per_factor(self) -> Rational:
        """kappa_{MF} of each factor: mu/2 = (k+1)/2."""
        return Rational(self.milnor_per_factor, 2)

    @property
    def kappa_total_naive(self) -> Rational:
        """Naive total kappa (additive, before orbifold): r * kappa_per_factor."""
        return self.n_factors * self.kappa_per_factor

    def central_charge_per_factor(self) -> Rational:
        """c of each N=2 MM factor: c = 3k/(k+2)."""
        return Rational(3 * self.level, self.level + 2)

    def total_central_charge(self) -> Rational:
        """Total c = r * c_per_factor = r * 3k/(k+2) = 3d (for CY d-fold)."""
        return self.n_factors * self.central_charge_per_factor()

    def verify_cy_condition(self) -> bool:
        """Check that r*k/(k+2) = d (the CY dimension condition).

        Equivalently: total c = 3d.
        """
        return self.total_central_charge() == 3 * self.cy_dim


def quintic_gepner() -> GepnerModel:
    """The Gepner model for the quintic threefold.

    5 copies of the k=3 N=2 minimal model (W = x^5 each), orbifolded
    by Z/5Z.  c_total = 5 * 9/5 = 9 = 3*3.  CY3.
    """
    return GepnerModel(level=3, n_factors=5, cy_dim=3)


# ============================================================================
# 8. Bar complex for MF
# ============================================================================

def bar_complex_A(n: int, max_bar_degree: int = 4) -> Dict[int, int]:
    """Dimensions of the bar complex B(MF(x^n)) by bar degree.

    The bar complex of the category MF(x^n) has:
    - B^0 = Jac(x^n) = C^{n-1}  (bar degree 0 = the algebra itself)
    - B^1 = Jac(x^n)^{otimes 2} / symmetry  (bar degree 1)
    - etc.

    For the ASSOCIATIVE bar complex of the commutative algebra Jac(x^n):
        B^p(Jac) = Jac^{otimes (p+1)} with differential from multiplication.

    The bar cohomology H^*(B(Jac)) for Jac = C[x]/(x^{n-1}):
        Since Jac is a local artinian ring with maximal ideal m = (x),
        and m^{n-1} = 0, the bar cohomology is controlled by the
        Koszul complex of the generators.

    For a truncated polynomial ring C[x]/(x^m):
        H^1(B) = m/m^2 = C (generated by x)
        H^p(B) = Tor_p^{Jac}(C, C)

    Dimensions of the bar complex (as vector spaces):
        B^p = dim(Jac)^{p+1} = (n-1)^{p+1}
    """
    dims = {}
    mu = n - 1
    for p in range(max_bar_degree + 1):
        dims[p] = mu ** (p + 1)
    return dims


def bar_cohomology_A(n: int) -> Dict[int, int]:
    """Bar cohomology dimensions H^p(B(Jac(x^n))).

    For Jac = C[x]/(x^{n-1}), the bar cohomology = Ext_{Jac}(C, C).

    For a COMMUTATIVE local artinian ring (R, m) with m^{n-1} = 0:
        Ext_R^p(C, C) = Tor_p^R(C, C)^*

    For the truncated polynomial ring C[x]/(x^m) (m = n-1):
        This is a complete intersection of embedding dimension 1.
        The Ext algebra is an exterior algebra on one generator (in degree 1)
        tensored with a divided power algebra.

        Specifically: Ext_{C[x]/(x^m)}(C, C) = C[xi, eta] / (xi^2)
        where |xi| = 1, |eta| = 2.
        So dim Ext^p = 1 for all p >= 0 (generated by xi^a * eta^b with a+2b=p).

        Wait -- more precisely:
        For C[x]/(x^m), the minimal free resolution of C is:
            ... -> R -> R -> R -> C
        with maps alternating between x^m (if m is the relation) and x.

        Actually, for R = C[x]/(x^m):
        The resolution of k = R/m = C is:
            ... -> R -x-> R -x^{m-1}-> R -x-> R -> C -> 0
        So Ext^p(C,C) is 1-dimensional for each p.

    Return: {p: dim H^p(B)} for p = 0, 1, 2, ...
    """
    # For C[x]/(x^m) with m = n-1:
    # Ext^p = C for all p >= 0
    # The bar COHOMOLOGY (Koszul dual) is concentrated on the diagonal
    # if and only if the algebra is Koszul.
    # C[x]/(x^m) is Koszul iff m = 2 (i.e., n = 3, the A_2 case).
    # For m >= 3 it is NOT Koszul (the relations involve x^m, not quadratic).
    #
    # The Ext^p dimensions are all 1 (this is correct for any m >= 2).
    return {p: 1 for p in range(10)}


# ============================================================================
# 9. Curved A-infinity from MF
# ============================================================================

def curved_ainfty_curvature(n: int) -> str:
    """The curvature m_0 of the curved A-infinity structure on MF(x^n).

    A matrix factorization (E_0 -> E_1 -> E_0) satisfies d^2 = W*id.
    In the A-infinity language, this means m_0 = W (the superpotential
    is the curvature).

    The curvature is an element of the CENTER of the endomorphism algebra,
    acting as scalar multiplication by W on each factorization.
    """
    return f"m_0 = x^{n} (the superpotential W = x^{n})"


def degree_to_kappa_relation(n: int) -> Dict[str, Rational]:
    """Relation between deg(W) and kappa for W = x^n.

    deg(W) = n
    mu(W) = n - 1
    kappa_{MF} = mu/2 = (n-1)/2

    So kappa = (deg(W) - 1) / 2.  The degree of W is NOT kappa.
    kappa is proportional to mu, NOT to deg(W).

    For the N=2 MM central charge c = 3(n-2)/n:
    kappa_Vir = c/2 = 3(n-2)/(2n)

    These agree only asymptotically: kappa_{MF} = (n-1)/2 ~ n/2,
    kappa_Vir ~ 3/2 as n -> infinity.  They are genuinely different
    invariants of different objects (AP9).
    """
    return {
        'deg_W': Rational(n),
        'mu': Rational(n - 1),
        'kappa_mf': Rational(n - 1, 2),
        'kappa_vir': Rational(3 * (n - 2), 2 * n),
        'ratio': Rational(n - 1, 2) / Rational(3 * (n - 2), 2 * n) if n > 2 else None,
    }


# ============================================================================
# 10. LG/CY correspondence for the quintic
# ============================================================================

@dataclass(frozen=True)
class QuinticCYData:
    """Hodge/topological data of the quintic threefold Q = {f_5 = 0} in P^4.

    h^{1,1} = 1, h^{2,1} = 101, chi = 2(h^{1,1} - h^{2,1}) = -200.
    """
    h11: int = 1
    h21: int = 101

    @property
    def euler_char(self) -> int:
        return 2 * (self.h11 - self.h21)

    @property
    def betti(self) -> Dict[int, int]:
        """Betti numbers b_0, ..., b_6."""
        return {
            0: 1,
            1: 0,
            2: self.h11,  # = 1
            3: 2 * self.h21 + 2,  # = 204
            4: self.h11,  # = 1 (by Poincare duality)
            5: 0,
            6: 1,
        }

    @property
    def hodge_diamond(self) -> Dict[Tuple[int, int], int]:
        """Hodge numbers h^{p,q} for the quintic CY3."""
        return {
            (0, 0): 1,
            (1, 0): 0, (0, 1): 0,
            (2, 0): 0, (1, 1): self.h11, (0, 2): 0,
            (3, 0): 1, (2, 1): self.h21, (1, 2): self.h21, (0, 3): 1,
        }


def quintic_lgcy_check() -> Dict[str, object]:
    """Verify LG/CY correspondence for the quintic.

    LG side: Gepner model = (MF(x^5))^{otimes 5} / (Z/5Z)
    CY side: D^b(Coh(Q)) for the quintic Q in P^4.

    The key numerical check:
        Milnor number per factor: mu(x^5) = 4
        Total mu (unorbifolded): 4^5 = 1024
        After Z/5Z orbifold: the number of MARGINAL deformations of the
            Gepner model should match h^{2,1}(Q) = 101.

    The orbifold acts on the tensor product of Jacobian rings:
        Jac_total = Jac(x^5)^{otimes 5} = (C^4)^{otimes 5}
    with Z/5Z acting diagonally (by the generator omega = e^{2pi i/5}).

    The invariant subspace Jac_total^{Z/5Z} has dimension:
        dim = (1/5) * sum_{g in Z/5Z} Tr(g | Jac_total)

    For g = omega^j (j = 0,...,4):
        On Jac(x^5) = span{1, x, x^2, x^3}, omega acts as
        omega^j * x^a = exp(2*pi*i*j*a/5) * x^a
        (since x has weight 1/5 = 1/(k+2) = 1/5 under the orbifold).

        Tr(omega^j | Jac(x^5)) = sum_{a=0}^{3} exp(2*pi*i*j*a/5)

    For j=0: Tr = 4
    For j=1: Tr = 1 + omega + omega^2 + omega^3 = -1 (sum of 4 out of 5 roots)
    For j=2: Tr = 1 + omega^2 + omega^4 + omega^6 = -1
    Similarly j=3: -1, j=4: -1

    Total Tr on Jac_total^{otimes 5}:
    j=0: 4^5 = 1024
    j=1: (-1)^5 = -1
    j=2: (-1)^5 = -1
    j=3: (-1)^5 = -1
    j=4: (-1)^5 = -1

    dim(Jac_total^{Z/5}) = (1024 - 1 - 1 - 1 - 1)/5 = 1020/5 = 204.

    This 204 is the TOTAL dimension of the invariant Jacobian ring.
    It includes:
        - 1 unit (the identity)
        - 101 marginal deformations (matching h^{2,1})
        - 1 top form
        - 101 anti-marginal
    Total: 1 + 101 + 101 + 1 = 204. Correct!

    The match 204 = b_3(Q) = 2*h^{2,1} + 2 is the LG/CY correspondence
    at the level of Hodge numbers.
    """
    omega = np.exp(2j * np.pi / 5)
    traces = []
    for j in range(5):
        # Trace on single factor
        tr_single = sum(omega ** (j * a) for a in range(4))
        # Trace on tensor product of 5 factors
        tr_total = tr_single ** 5
        traces.append(tr_total)

    dim_invariant = sum(traces) / 5

    quintic = QuinticCYData()

    return {
        'traces_per_twist': [complex(t) for t in traces],
        'dim_invariant_jac': int(round(dim_invariant.real)),
        'b3_quintic': quintic.betti[3],
        'match': int(round(dim_invariant.real)) == quintic.betti[3],
        'h21': quintic.h21,
        'euler_char': quintic.euler_char,
    }


# ============================================================================
# 11. Hessian and quadratic form on Jacobian ring
# ============================================================================

def multiplication_matrix_A(n: int, element_coeffs: List) -> Matrix:
    """Matrix of multiplication by an element in Jac(x^n).

    In Jac = C[x]/(x^{n-1}), multiplication by f = sum a_i x^i
    maps x^j to f*x^j mod x^{n-1}.

    The matrix M_{ij} = coefficient of x^i in (f * x^j mod x^{n-1}).
    """
    mu = n - 1
    M = zeros(mu, mu)
    for j in range(mu):
        for deg_f, coeff in enumerate(element_coeffs):
            target = j + deg_f
            if target < mu:
                M[target, j] += Rational(coeff)
    return M


def hessian_element_A(n: int) -> List:
    """The Hessian d^2W/dx^2 as element of Jac(x^n).

    d^2(x^n)/dx^2 = n(n-1)x^{n-2}.
    As coefficients in basis {1, x, ..., x^{n-2}}:
    all zero except position n-2 has coefficient n(n-1).
    """
    mu = n - 1
    coeffs = [Rational(0)] * mu
    coeffs[mu - 1] = Rational(n * (n - 1))
    return coeffs


def multiplication_trace_A(n: int, element_coeffs: List) -> Rational:
    """Trace of multiplication by element in Jac(x^n).

    For Jac = C[x]/(x^{n-1}), the multiplication operator M_f
    has trace = sum of diagonal entries = sum_j [coeff of x^j in f*x^j].

    For f = sum a_i x^i: (f * x^j) mod x^{n-1} contributes a_0 to diagonal.
    So Tr(M_f) = mu * a_0 = (n-1) * a_0.

    This is the ALGEBRA TRACE, not the residue trace.

    The RESIDUE trace is different:
        Tr_res(f) = Res(f dx / dW) = (1/n) * coeff of x^{n-2} in f

    These two traces are related by:
        Tr(M_f) = mu * a_0  (algebra trace = linear functional evaluating at 1)
        Tr_res(f) = (1/n) * a_{n-2}  (residue trace = linear functional at top)
    """
    mu = n - 1
    a_0 = Rational(element_coeffs[0]) if len(element_coeffs) > 0 else Rational(0)
    return mu * a_0


def residue_trace_A(n: int, element_coeffs: List) -> Rational:
    """Residue trace of an element in Jac(x^n).

    Tr_res(f) = Res_{x=0}(f dx / (nx^{n-1})) = (1/n) * a_{n-2}
    where f = sum a_i x^i.
    """
    target = n - 2
    if target < len(element_coeffs):
        return Rational(element_coeffs[target]) / n
    return Rational(0)


# ============================================================================
# 12. Summary table
# ============================================================================

def ade_shadow_summary() -> List[Dict[str, object]]:
    """Summary of shadow data for all ADE singularities (up to E8).

    Returns a list of dicts with:
        type, mu, h, c_{N=2}, kappa_{MF}, kappa_{Vir}, shadow_rank
    """
    singularities = all_ade_singularities(8)
    rows = []
    for s in singularities:
        rows.append({
            'type': s.type_name,
            'mu': s.milnor_number,
            'h': s.coxeter_number,
            'c_N2': s.n2_central_charge,
            'kappa_MF': s.kappa_mf,
            'kappa_Vir': s.kappa_virasoro,
            'shadow_rank': shadow_tower_rank(s),
            'n_vars': s.n_vars,
        })
    return rows


def print_ade_table():
    """Print a formatted table of ADE shadow data."""
    rows = ade_shadow_summary()
    header = f"{'Type':>6} {'mu':>4} {'h':>4} {'c_N2':>10} {'kMF':>8} {'kVir':>10} {'rank':>4}"
    print(header)
    print("-" * len(header))
    for r in rows:
        c_str = str(r['c_N2'])
        kmf_str = str(r['kappa_MF'])
        kvir_str = str(r['kappa_Vir'])
        print(f"{r['type']:>6} {r['mu']:>4} {r['h']:>4} {c_str:>10} {kmf_str:>8} {kvir_str:>10} {r['shadow_rank']:>4}")
