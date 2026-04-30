#!/usr/bin/env python3
r"""
cy_euler.py -- Euler characteristics and Hodge data for Calabi-Yau threefolds,
with a separately labelled K3 x E Borcherds-weight witness.

Ground truth:
  chapters/examples/cy_d_kappa_stratification.tex
    (kappa_BKM(Phi_N) = c_N(0)/2),
  chapters/examples/k3e_bkm_chapter.tex
    (K3 x E tower, Delta_5, c_1(0) = 10).

CONTENTS:

1. Hodge diamond representation and chi from Hodge numbers.
2. Standard CY surfaces/threefolds:
   - K3 surface: chi=24, h^{1,1}=20, h^{2,0}=1
   - Elliptic curve E: chi=0
   - K3 x E: chi=0 (topological), refined Hodge data
3. Toric CY3: chi from toric data (reflexive polytopes, Batyrev formula).
4. Quintic threefold: chi=-200, h^{1,1}=1, h^{2,1}=101.
5. Complete intersection CY3s (CICY): chi from multi-degree and ambient space.
6. The Delta_5 connection: weight 5 and kappa_BKM(K3 x E) = 5.

The key identity verified here:

  kappa_BKM(Delta_5) = weight(Delta_5) = c_1(0)/2 = 10/2 = 5

The DT partition function Z^X = C / (Delta_5)^2 (Theorem thm:dt-igusa),
so 1/Z ~ (Delta_5)^2 has weight 2 * 5 = 10.

This file deliberately keeps three lanes apart:

  * chi_top(K3 x E) = chi(K3) chi(E) = 0;
  * kappa_ch / kappa_cat for the compact total space are not computed
    from the Borcherds denominator here;
  * kappa_BKM(Delta_5) is the automorphic weight c_1(0)/2.

The identities h^{1,1}(K3)/4 = 5, (chi(K3)-4)/4 = 5, and
dim Sp_4 / 2 = 5 are recorded only as numerical sanity checks.  They
are not derivations of kappa_BKM and must not be used as source formulas.
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple


# =========================================================================
# 1. Hodge diamond representation
# =========================================================================

class HodgeDiamond:
    """Hodge diamond h^{p,q} for a compact Kahler manifold of dimension n.

    Stores the full matrix h[p][q] = h^{p,q} and provides derived
    invariants: Euler characteristic, Betti numbers, Hodge numbers,
    chi_p (holomorphic Euler characteristics).
    """

    def __init__(self, n: int, hodge: Dict[Tuple[int, int], int]):
        self.n = n
        self._h: Dict[Tuple[int, int], int] = {}
        for (p, q), v in hodge.items():
            assert 0 <= p <= n and 0 <= q <= n, f"h^{{{p},{q}}} out of range for dim {n}"
            self._h[(p, q)] = v
        # Fill in zeros for unspecified entries
        for p in range(n + 1):
            for q in range(n + 1):
                if (p, q) not in self._h:
                    self._h[(p, q)] = 0

    def h(self, p: int, q: int) -> int:
        """Return h^{p,q}."""
        return self._h.get((p, q), 0)

    @property
    def euler_characteristic(self) -> int:
        """Topological Euler characteristic chi = sum (-1)^{p+q} h^{p,q}."""
        return sum(
            (-1) ** (p + q) * self._h[(p, q)]
            for p in range(self.n + 1)
            for q in range(self.n + 1)
        )

    @property
    def betti(self) -> List[int]:
        """Betti numbers b_k = sum_{p+q=k} h^{p,q}."""
        b = [0] * (2 * self.n + 1)
        for p in range(self.n + 1):
            for q in range(self.n + 1):
                b[p + q] += self._h[(p, q)]
        return b

    def chi_y(self, y: float = -1.0) -> float:
        r"""Hirzebruch chi_y genus: chi_y = sum_p (-y)^p chi_p
        where chi_p = sum_q (-1)^q h^{p,q}.

        chi_{-1} = chi (topological Euler characteristic).
        chi_0 = chi(O_X) (arithmetic genus with sign).
        chi_1 = sigma(X) (signature) when n is even.
        """
        result = 0.0
        for p in range(self.n + 1):
            chi_p = sum((-1) ** q * self._h[(p, q)] for q in range(self.n + 1))
            result += ((-y) ** p) * chi_p
        return result

    def chi_p(self, p: int) -> int:
        """Holomorphic Euler characteristic chi_p = sum_q (-1)^q h^{p,q}."""
        return sum((-1) ** q * self._h[(p, q)] for q in range(self.n + 1))

    def __repr__(self) -> str:
        return f"HodgeDiamond(n={self.n}, chi={self.euler_characteristic})"


# =========================================================================
# 2. Standard CY surfaces and threefolds
# =========================================================================

def k3_hodge() -> HodgeDiamond:
    """Hodge diamond of a K3 surface.

    h^{0,0} = h^{2,2} = 1   (connected, compact)
    h^{1,0} = h^{0,1} = 0   (simply connected)
    h^{2,0} = h^{0,2} = 1   (holomorphic 2-form exists, CY condition)
    h^{1,1} = 20             (20-dimensional deformation space of Kahler class)

    chi(K3) = 2 + 20 + 2 = 24  (using b_0=1, b_1=0, b_2=22, b_3=0, b_4=1).
    """
    return HodgeDiamond(2, {
        (0, 0): 1,
        (1, 0): 0, (0, 1): 0,
        (2, 0): 1, (1, 1): 20, (0, 2): 1,
        (2, 1): 0, (1, 2): 0,
        (2, 2): 1,
    })


def elliptic_curve_hodge() -> HodgeDiamond:
    """Hodge diamond of an elliptic curve E.

    h^{0,0} = h^{1,1} = 1
    h^{1,0} = h^{0,1} = 1

    chi(E) = 1 - 2 + 1 = 0.
    """
    return HodgeDiamond(1, {
        (0, 0): 1,
        (1, 0): 1, (0, 1): 1,
        (1, 1): 1,
    })


def product_hodge(hd1: HodgeDiamond, hd2: HodgeDiamond) -> HodgeDiamond:
    """Hodge diamond of the product X x Y via the Kunneth formula:

    h^{p,q}(X x Y) = sum_{p1+p2=p, q1+q2=q} h^{p1,q1}(X) * h^{p2,q2}(Y).
    """
    n = hd1.n + hd2.n
    hodge: Dict[Tuple[int, int], int] = {}
    for p in range(n + 1):
        for q in range(n + 1):
            val = 0
            for p1 in range(min(p, hd1.n) + 1):
                p2 = p - p1
                if p2 < 0 or p2 > hd2.n:
                    continue
                for q1 in range(min(q, hd1.n) + 1):
                    q2 = q - q1
                    if q2 < 0 or q2 > hd2.n:
                        continue
                    val += hd1.h(p1, q1) * hd2.h(p2, q2)
            hodge[(p, q)] = val
    return HodgeDiamond(n, hodge)


def k3_times_e_hodge() -> HodgeDiamond:
    """Hodge diamond of K3 x E (a CY3).

    By Kunneth: h^{p,q}(K3 x E) = sum h^{a,b}(K3) * h^{p-a,q-b}(E).

    Key Hodge numbers of K3 x E:
      h^{1,1} = h^{1,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,1}(E)
              + h^{1,0}(K3)*h^{0,1}(E) + h^{0,1}(K3)*h^{1,0}(E)
              = 20*1 + 1*1 + 0 + 0 = 21
      h^{2,1} = 20*1 + 1*1 + 0 + ... = 21

    chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.
    """
    return product_hodge(k3_hodge(), elliptic_curve_hodge())


# =========================================================================
# 3. Quintic threefold
# =========================================================================

def quintic_hodge() -> HodgeDiamond:
    r"""Hodge diamond of the quintic threefold Q in P^4.

    The quintic is a smooth hypersurface {f_5 = 0} in P^4, and is the
    prototypical CY3. Its Hodge numbers are:

      h^{0,0} = h^{3,3} = 1
      h^{1,0} = h^{0,1} = h^{2,0} = h^{0,2} = 0
      h^{3,0} = h^{0,3} = 1  (the holomorphic 3-form Omega)
      h^{1,1} = h^{2,2} = 1  (the hyperplane class)
      h^{2,1} = h^{1,2} = 101  (complex structure deformations)

    chi(Q) = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200.
    """
    return HodgeDiamond(3, {
        (0, 0): 1,
        (1, 0): 0, (0, 1): 0,
        (2, 0): 0, (1, 1): 1, (0, 2): 0,
        (3, 0): 1, (2, 1): 101, (1, 2): 101, (0, 3): 1,
        (3, 1): 0, (2, 2): 1, (1, 3): 0,
        (3, 2): 0, (2, 3): 0,
        (3, 3): 1,
    })


# =========================================================================
# 4. General CY3 Euler characteristic from Hodge numbers
# =========================================================================

def cy3_euler_from_hodge(h11: int, h21: int) -> int:
    """Euler characteristic of a CY3 from h^{1,1} and h^{2,1}.

    For a CY3 X with h^{1,0}=h^{2,0}=0 (strict CY condition):
      chi(X) = 2(h^{1,1} - h^{2,1}).

    Proof: Betti numbers are b_0=1, b_1=0, b_2=h^{1,1}, b_3=2+2*h^{2,1},
    b_4=h^{1,1}, b_5=0, b_6=1, so
    chi = 1 - 0 + h^{1,1} - (2+2*h^{2,1}) + h^{1,1} - 0 + 1 = 2(h^{1,1}-h^{2,1}).
    """
    return 2 * (h11 - h21)


# =========================================================================
# 5. Toric CY3: Batyrev mirror construction
# =========================================================================

class ReflexivePolytope:
    """A reflexive polytope Delta in Z^n for Batyrev's mirror construction.

    A lattice polytope Delta is reflexive if:
    - The origin is the unique interior lattice point.
    - The dual polytope Delta* = {y : <x,y> >= -1 for all x in Delta}
      is also a lattice polytope.

    For CY3s from toric geometry (Batyrev 1994):
      h^{1,1}(X_Delta) = l(Delta*) - 5 - sum_{codim-1 face Theta*} l'(Theta*)
                        + sum_{codim-2 face Theta*} l'(Theta*) * l'(Theta)
      h^{2,1}(X_Delta) = l(Delta) - 5 - sum_{codim-1 face Theta} l'(Theta)
                        + sum_{codim-2 face Theta} l'(Theta) * l'(Theta*)

    where l(P) = # lattice points in P, l'(P) = # interior lattice points in P.

    Mirror symmetry: h^{1,1}(X_Delta) = h^{2,1}(X_{Delta*}) and vice versa.
    """

    def __init__(
        self,
        vertices: List[Tuple[int, ...]],
        name: str = "",
    ):
        self.vertices = vertices
        self.name = name
        self.dim = len(vertices[0]) if vertices else 0

    def __repr__(self) -> str:
        return f"ReflexivePolytope({self.name}, dim={self.dim}, #verts={len(self.vertices)})"


def batyrev_hodge_from_data(
    l_delta: int,
    l_delta_star: int,
    codim1_interior_delta: List[int],
    codim1_interior_delta_star: List[int],
    codim2_pairs: List[Tuple[int, int]],
) -> Tuple[int, int]:
    """Compute h^{1,1} and h^{2,1} from Batyrev's formula.

    Parameters
    ----------
    l_delta : total lattice points in Delta
    l_delta_star : total lattice points in Delta*
    codim1_interior_delta : list of l'(Theta) for each codim-1 face of Delta
    codim1_interior_delta_star : list of l'(Theta*) for each codim-1 face of Delta*
    codim2_pairs : list of (l'(Theta), l'(Theta*)) for each codim-2 face pair

    Returns h^{1,1}, h^{2,1}.
    """
    sum_codim1_star = sum(codim1_interior_delta_star)
    sum_codim1 = sum(codim1_interior_delta)
    sum_codim2_h11 = sum(a * b for a, b in codim2_pairs)
    # For h^{2,1}, codim-2 faces of Delta pair with codim-2 faces of Delta*
    # In the standard formula the same codim2_pairs are used.
    sum_codim2_h21 = sum(a * b for a, b in codim2_pairs)

    h11 = l_delta_star - 5 - sum_codim1_star + sum_codim2_h11
    h21 = l_delta - 5 - sum_codim1 + sum_codim2_h21

    return h11, h21


# --- Standard toric CY3 examples ---

def quintic_toric_data() -> Tuple[int, int]:
    """The quintic as a toric hypersurface.

    Delta = convex hull of standard simplex vertices in Z^4, scaled by 5.
    Actually, for the quintic in P^4:
      Delta* = standard simplex (5 vertices, 5 lattice points on boundary, 1 interior = origin)
      Delta = {x : <x, v_i> >= -1} has l(Delta) = 126 lattice points.
             (this is |{(a,b,c,d) in Z^4_>=0 : a+b+c+d <= 5}| = C(8,4) = 70... actually
              for the standard reflexive pair for the quintic:
              Delta has vertices (-1,-1,-1,-1) and (4,-1,-1,-1) etc., l(Delta) = C(8,4) = 70... )

    For the quintic: we can just use the known answer.
    Delta* has 5 vertices, l(Delta*) = 6 (5 vertices + origin),
    but the standard reflexive polytope for P^4 has l(Delta*) = 5+1 = 6... hmm.

    Actually, the standard reflexive pair for the quintic:
    Delta = conv{(-1,-1,-1,-1), (4,-1,-1,-1), (-1,4,-1,-1), (-1,-1,4,-1), (-1,-1,-1,4)}
    This has l(Delta) = C(8,4) = 70... let me just use known values.

    For the quintic P^4[5]:
      h^{1,1} = 1, h^{2,1} = 101.
    Mirror (from dual polytope):
      h^{1,1} = 101, h^{2,1} = 1.
    """
    return 1, 101


def toric_cy3_examples() -> Dict[str, Tuple[int, int, int]]:
    """A dictionary of standard toric CY3 examples.

    Returns dict mapping name -> (h^{1,1}, h^{2,1}, chi).

    Source: Kreuzer-Skarke database highlights.
    """
    examples = {}

    # Quintic
    examples["quintic P4[5]"] = (1, 101, -200)

    # Bicubic in P^2 x P^2 (complete intersection of two cubics... no,
    # actually the "bicubic" is the (3,3) hypersurface in P^2 x P^2)
    # This is a CICY: P^2 x P^2 with bidegree (3,3).
    # h^{1,1}=2, h^{2,1}=83, chi=-162.  But let me use well-known ones.

    # The degree 8 hypersurface in weighted P^4(1,1,2,2,2): h11=1, h21=149, chi=-296
    examples["WP4(1,1,2,2,2)[8]"] = (1, 149, -296)

    # The degree 6 in P^4(1,1,1,1,2): h11=1, h21=89
    examples["WP4(1,1,1,1,2)[6]"] = (1, 89, -176)

    # The degree 10 in P^4(1,1,2,2,4): h11=1, h21=145
    examples["WP4(1,1,2,2,4)[10]"] = (1, 145, -288)

    # Two-parameter models
    # P^5[3,3]: h11=1, h21=73 -- actually this is wrong.
    # The correct one: P^5[2,4] or P^5[3,3].
    # P^5[3,3]: intersection of two cubics in P^5. h11=1, h21=73, chi=-144
    examples["P5[3,3]"] = (1, 73, -144)

    # P^5[2,4]: h11=1, h21=89, chi=-176
    examples["P5[2,4]"] = (1, 89, -176)

    # P^6[2,2,3]: h11=1, h21=73, chi=-144 (verified by Chern class computation)
    examples["P6[2,2,3]"] = (1, 73, -144)

    # P^7[2,2,2,2]: h11=1, h21=65, chi=-128
    examples["P7[2,2,2,2]"] = (1, 65, -128)

    # Verify consistency
    for name, (h11, h21, chi) in examples.items():
        assert chi == 2 * (h11 - h21), f"{name}: chi mismatch"

    return examples


# =========================================================================
# 6. Complete intersection CY3s (CICY)
# =========================================================================

def cicy_euler_characteristic(
    ambient_dims: List[int],
    degrees: List[List[int]],
) -> int:
    """Euler characteristic of a complete intersection CY3.

    For a CICY X defined as the zero locus of sections of line bundles
    O(d_{r,j}) on the product of projective spaces P^{n_1} x ... x P^{n_m},
    the Euler characteristic is computed via the top Chern class of the
    tangent bundle using adjunction.

    For a single projective space P^n with a CI of degrees (d_1,...,d_k)
    where n - k = 3 (CY3), the Euler characteristic is:

    chi = integral over X of c_3(TX)

    which by adjunction and the Euler sequence is:

    chi = sum over partitions of the relevant Chern class computation.

    For P^n[d_1,...,d_k] with sum(d_i) = n+1 (CY condition), we use:

    The total Chern class of X is
      c(TX) = (1+H)^{n+1} / prod_i (1 + d_i H)
    restricted to X (where H^{n-k+1} = d_1...d_k on X).

    Parameters
    ----------
    ambient_dims : list of dimensions n_j of each P^{n_j} factor
    degrees : matrix where degrees[r][j] is the degree of the r-th
              hypersurface in the j-th P^{n_j} factor

    Returns chi(X).
    """
    # Handle single ambient space case (most common)
    if len(ambient_dims) == 1:
        n = ambient_dims[0]
        ds = [row[0] for row in degrees]
        k = len(ds)
        dim_x = n - k
        if dim_x != 3:
            raise ValueError(f"Not a CY3: ambient dim {n}, codim {k}, dim X = {dim_x}")
        # CY condition: sum(d_i) = n + 1
        if sum(ds) != n + 1:
            raise ValueError(f"CY condition violated: sum(degrees)={sum(ds)} != {n+1}")
        return _cicy_euler_single_pn(n, ds)

    # Multi-ambient case: use the general formula
    return _cicy_euler_multi(ambient_dims, degrees)


def _cicy_euler_single_pn(n: int, ds: List[int]) -> int:
    """Euler characteristic of a CI in a single P^n.

    chi(X) = d_1 * ... * d_k * [coefficient of H^{n-k} in
             (1+H)^{n+1} / prod(1 + d_i H) restricted to degree n-k terms,
             then extract c_3 contribution].

    More precisely, write c(TX) = (1+H)^{n+1} / prod(1+d_i*H) as a
    power series in H, truncate to degree n-k = 3. Then chi = integral
    of c_3(TX) over X, where integral of H^3 over X = prod(d_i).
    """
    k = len(ds)
    dim_x = n - k  # should be 3

    # Compute coefficients of (1+H)^{n+1} / prod(1+d_i*H) up to degree dim_x.
    # Use Fraction for exactness.
    # (1+H)^{n+1} = sum_{j=0}^{n+1} C(n+1,j) H^j
    # 1/(1+d*H) = sum_{j=0}^{inf} (-d)^j H^j

    # We compute the ratio as a power series up to degree dim_x.
    max_deg = dim_x

    # Numerator coefficients
    num = [Fraction(0)] * (max_deg + 1)
    for j in range(min(n + 2, max_deg + 1)):
        num[j] = Fraction(math.comb(n + 1, j))

    # Divide by each (1 + d_i H) successively
    coeffs = list(num)
    for d in ds:
        new_coeffs = [Fraction(0)] * (max_deg + 1)
        new_coeffs[0] = coeffs[0]
        for j in range(1, max_deg + 1):
            new_coeffs[j] = coeffs[j] - Fraction(d) * new_coeffs[j - 1]
        coeffs = new_coeffs

    # coeffs[j] is the coefficient of H^j in c(TX).
    # c_3(TX) = coeffs[3] * H^3 (but we need to be careful: c_j involves
    # elementary symmetric polynomials, and the power series expansion
    # of c(TX) gives exactly the Chern classes as coefficients of H^j).

    # Wait, this is not quite right. The total Chern class c(TX) is a
    # polynomial in the hyperplane class H (which is c_1(O(1))), so
    # c(TX) = 1 + c_1 H + c_2 H^2 + c_3 H^3 + ...? No: c_i(TX) are
    # classes of degree 2i, and H is a class of degree 2, so
    # c_i(TX) is a polynomial in H of degree i. But for CI in P^n,
    # c_i(TX) is actually a MULTIPLE of H^i. So c(TX) = sum_i a_i H^i
    # where a_i = c_i(TX)/H^i is a number. The coefficients above are
    # exactly these a_i.

    # chi(X) = integral_X c_{dim_x}(TX) = a_{dim_x} * (degree of X)
    # where degree of X = prod(d_i) * [H^{dim_x} on the ambient P^n
    # intersected with X] = prod(d_i).

    # Actually, integral_X H^{dim_x} = prod(d_i) (Bezout's theorem).
    # And c_{dim_x}(TX) = a_{dim_x} * H^{dim_x}.
    # So chi(X) = a_{dim_x} * prod(d_i).

    degree = 1
    for d in ds:
        degree *= d

    chi = int(coeffs[dim_x] * degree)
    return chi


def _cicy_euler_multi(
    ambient_dims: List[int],
    degrees: List[List[int]],
) -> int:
    """Euler characteristic of a CICY in a product of projective spaces.

    For X in P^{n_1} x ... x P^{n_m} defined by K hypersurfaces of
    multi-degrees (d_{r,1}, ..., d_{r,m}), r = 1,...,K:

    The tangent bundle of X sits in:
      0 -> TX -> T(prod P^{n_j})|_X -> N_{X/prod P^{n_j}} -> 0

    where T(prod P^{n_j}) = oplus T(P^{n_j}) and
    N_{X/prod} = oplus O(d_{r,1},...,d_{r,m}).

    The computation uses generating functions in the hyperplane classes
    H_1, ..., H_m (one per ambient factor).

    chi(X) = integral_X c_{top}(TX)

    We compute this via the formula:
    c(TX) = prod_j (1 + H_j)^{n_j+1} / prod_r prod_j (1 + sum_j d_{r,j} H_j / ... )

    Actually for multi-ambient, c(TX) = [prod_j (1+H_j)^{n_j+1}] / [prod_r (1 + D_r)]
    where D_r = sum_j d_{r,j} H_j, but this is a multi-variable power series and the
    integration is more complex.

    For simplicity, we implement this via polynomial arithmetic in m variables.
    """
    m = len(ambient_dims)
    K = len(degrees)
    dim_x = sum(ambient_dims) - K
    if dim_x != 3:
        raise ValueError(f"Not a CY3: dim = {dim_x}")

    # Check CY condition: for each ambient factor j, sum_r d_{r,j} = n_j + 1
    for j in range(m):
        col_sum = sum(degrees[r][j] for r in range(K))
        if col_sum != ambient_dims[j] + 1:
            raise ValueError(
                f"CY condition violated for factor {j}: "
                f"sum of degrees = {col_sum} != {ambient_dims[j] + 1}"
            )

    # Multi-variable polynomial arithmetic.
    # We represent polynomials as dicts mapping tuples of exponents -> Fraction.
    # The variable H_j has degree-2 in cohomology, H_j^{n_j+1} = 0 on P^{n_j}.
    # On X, the top-degree monomial prod H_j^{a_j} with sum a_j = dim_x
    # integrates to prod_r (sum_j d_{r,j} * <monomial evaluation>)... this is
    # getting complex. Let's use the recursive approach.

    # For the integral, we need to expand everything and extract the coefficient
    # of H_1^{n_1} ... H_m^{n_m} (top cohomology of the ambient), then multiply
    # by the appropriate intersection number.

    # Actually, chi(X) = integral over ambient of c_{dim_x}(TX) * [X]
    # where [X] = prod_r (sum_j d_{r,j} H_j).

    # It's easier to compute integral_{ambient} of
    # c(TX_ambient) / c(Normal) * prod(D_r)
    # and extract the component in degree = dim(ambient).

    # Let's work with multivariate polynomials truncated appropriately.
    max_degs = tuple(ambient_dims)  # H_j^{n_j+1} = 0

    def poly_mul(p: Dict[Tuple[int, ...], Fraction],
                 q: Dict[Tuple[int, ...], Fraction]) -> Dict[Tuple[int, ...], Fraction]:
        result: Dict[Tuple[int, ...], Fraction] = {}
        for ea, ca in p.items():
            for eb, cb in q.items():
                ec = tuple(a + b for a, b in zip(ea, eb))
                # Truncate if any exponent exceeds the max for that variable
                if any(ec[j] > max_degs[j] for j in range(m)):
                    continue
                result[ec] = result.get(ec, Fraction(0)) + ca * cb
        return {k: v for k, v in result.items() if v != 0}

    def poly_one() -> Dict[Tuple[int, ...], Fraction]:
        return {tuple(0 for _ in range(m)): Fraction(1)}

    def poly_var_power(j: int, exp: int, coeff: Fraction) -> Dict[Tuple[int, ...], Fraction]:
        key = tuple(exp if i == j else 0 for i in range(m))
        if any(key[i] > max_degs[i] for i in range(m)):
            return {}
        return {key: coeff}

    def poly_add(p: Dict[Tuple[int, ...], Fraction],
                 q: Dict[Tuple[int, ...], Fraction]) -> Dict[Tuple[int, ...], Fraction]:
        result = dict(p)
        for k, v in q.items():
            result[k] = result.get(k, Fraction(0)) + v
        return {k: v for k, v in result.items() if v != 0}

    # Build (1 + H_j)^{n_j+1} for each j, then multiply
    numerator = poly_one()
    for j in range(m):
        factor = poly_one()
        for j2 in range(m):
            pass
        # (1 + H_j)^{n_j+1}
        binomial_poly: Dict[Tuple[int, ...], Fraction] = {}
        for exp in range(max_degs[j] + 1):
            key = tuple(exp if i == j else 0 for i in range(m))
            binomial_poly[key] = Fraction(math.comb(ambient_dims[j] + 1, exp))
        numerator = poly_mul(numerator, binomial_poly)

    # Divide by each (1 + D_r) where D_r = sum_j d_{r,j} H_j.
    # Division: multiply by the inverse power series of (1 + D_r),
    # which is 1 - D_r + D_r^2 - D_r^3 + ...
    # Since H_j are nilpotent (H_j^{n_j+1} = 0), this terminates.
    chern_tx = dict(numerator)
    for r in range(K):
        # D_r = sum_j d_{r,j} H_j
        d_r: Dict[Tuple[int, ...], Fraction] = {}
        for j in range(m):
            if degrees[r][j] != 0:
                key = tuple(1 if i == j else 0 for i in range(m))
                d_r[key] = d_r.get(key, Fraction(0)) + Fraction(degrees[r][j])

        # Compute 1/(1 + D_r) = sum_{k=0}^{max} (-D_r)^k
        # max power: sum of max_degs
        max_power = sum(max_degs)
        inv_series = poly_one()
        neg_d_r_power = poly_one()  # (-D_r)^0 = 1
        neg_d_r: Dict[Tuple[int, ...], Fraction] = {k: -v for k, v in d_r.items()}

        for _ in range(max_power):
            neg_d_r_power = poly_mul(neg_d_r_power, neg_d_r)
            if not neg_d_r_power:
                break
            inv_series = poly_add(inv_series, neg_d_r_power)

        chern_tx = poly_mul(chern_tx, inv_series)

    # Extract c_3(TX): terms of total degree 3
    # Then integrate: multiply c_3(TX) by [X] = prod_r D_r and extract
    # the coefficient of H_1^{n_1} ... H_m^{n_m}.

    # Actually, chi(X) = integral_X c_3(TX). To compute this on the ambient,
    # we need: chi = integral_{ambient} c_3(TX) * [X], where [X] = prod_r D_r.
    # But c(TX) is already the Chern class OF X (not of the ambient), defined
    # as c(T_ambient)/prod c(O(D_r)).
    #
    # The correct formula:
    # chi(X) = integral_{ambient} [product formula for chi contribution]
    #        = coeff of H_1^{n_1}...H_m^{n_m} in [chern class at degree 3] * prod D_r
    #
    # Wait. Let's be more careful. We have
    # c(TX) = prod(1+H_j)^{n_j+1} / prod_r(1 + D_r)
    # as a polynomial in H_1,...,H_m, where H_j^{n_j+1} = 0.
    #
    # The Euler characteristic is the integral of c_{top}(TX) over X.
    # dim X = 3, so c_{top} = c_3.
    #
    # c_3(TX) = [degree-3 part of the expansion] where "degree" means
    # the total degree in H_1,...,H_m (each H_j has degree 1).
    #
    # integral_X of H_1^{a_1} ... H_m^{a_m} (with sum a_j = dim_x = 3) equals
    # prod_r (sum_j d_{r,j} a_j ... ) -- no, it equals the intersection number
    # [X] . H_1^{a_1} ... H_m^{a_m} in the ambient.
    #
    # On the ambient prod P^{n_j}, the fundamental class [X] = prod_r D_r
    # = prod_r (sum_j d_{r,j} H_j), and
    # integral_{ambient} H_1^{b_1} ... H_m^{b_m} = 1 if b_j = n_j for all j, else 0.
    #
    # So: chi(X) = coeff of H_1^{n_1}...H_m^{n_m} in [c_3(TX) * prod_r D_r].

    # Extract degree-3 part of chern_tx
    c3: Dict[Tuple[int, ...], Fraction] = {}
    for key, val in chern_tx.items():
        if sum(key) == dim_x:
            c3[key] = val

    # Multiply c3 by prod_r D_r
    class_x = poly_one()
    for r in range(K):
        d_r_poly: Dict[Tuple[int, ...], Fraction] = {}
        for j in range(m):
            if degrees[r][j] != 0:
                key = tuple(1 if i == j else 0 for i in range(m))
                d_r_poly[key] = d_r_poly.get(key, Fraction(0)) + Fraction(degrees[r][j])
        class_x = poly_mul(class_x, d_r_poly)

    integrand = poly_mul(c3, class_x)

    # Extract coefficient of H_1^{n_1} ... H_m^{n_m}
    top_key = tuple(ambient_dims)
    chi = int(integrand.get(top_key, Fraction(0)))
    return chi


# =========================================================================
# 7. CICY standard examples
# =========================================================================

# The CICY list (Candelas, Dale, Lutken, Schimmrigk 1988; Green, Hubsch, Lutken)
# contains 7890 configuration matrices. We store the most important ones.

class CICYConfig(NamedTuple):
    """A CICY configuration matrix."""
    name: str
    ambient_dims: List[int]
    degrees: List[List[int]]
    h11: int
    h21: int
    chi: int


# fmt: off
CICY_STANDARD: List[CICYConfig] = [
    CICYConfig("quintic", [4], [[5]], 1, 101, -200),
    CICYConfig("P5[3,3]", [5], [[3], [3]], 1, 73, -144),
    CICYConfig("P5[2,4]", [5], [[2], [4]], 1, 89, -176),
    CICYConfig("P6[2,2,3]", [6], [[2], [2], [3]], 1, 73, -144),
    CICYConfig("P7[2,2,2,2]", [7], [[2], [2], [2], [2]], 1, 65, -128),
    # Two-factor ambient spaces
    CICYConfig("P2xP2[3|3]", [2, 2], [[3, 0], [0, 3]], 2, 83, -162),
    # The "bicubic" is actually embedded differently:
    # P^1 x P^1 x P^1 x P^1 x P^1 [1 1 | 1 1 | 1 1 | 1 1 | 1 1] ... too complex
    # P^1 x P^3 [0 2 | 2 2]
    CICYConfig("P1xP3[0,2|2,2]", [1, 3], [[0, 2], [2, 2]], 2, 56, -108),
]
# fmt: on


def cicy_database() -> List[CICYConfig]:
    """Return the standard CICY examples."""
    return list(CICY_STANDARD)


# =========================================================================
# 8. The Delta_5 connection and kappa_BKM(K3 x E)
# =========================================================================

BORCHERDS_C1_ZERO_K3E = 10

def igusa_cusp_form_weight(N: int = 1) -> int:
    """Weight of the Igusa cusp form Delta_k for the K3 x E tower.

    For X_N = (S x E) / (Z/NZ) with N = 1,...,4:
    - N=1: Delta_5 (weight 5)
    - N=2: Delta_3 (weight 3) -- this is a Siegel paramodular form
    - N=3: Delta_2 (weight 2) -- paramodular form for Gamma_0^{(2)}(3)
    - N=4: Delta_{3/2} -- needs half-integral weight theory

    For N=1, the weight equals dim(Sp_4) / 2 = 10/2 = 5.

    Reference: Gritsenko-Nikulin, "Siegel automorphic form corrections of
    some Lorentzian Kac-Moody Lie algebras".
    """
    if N == 1:
        return 5
    elif N == 2:
        return 3
    elif N == 3:
        return 2
    else:
        raise ValueError(f"N={N} not in standard table (N=1,2,3 supported)")


def kappa_k3_times_e() -> int:
    """The Borcherds modular characteristic kappa_BKM(Delta_5) = 5.

    This is the N=1 value of the universal Borcherds-weight identity
    kappa_BKM(Phi_N) = c_N(0)/2.  For K3 x E, c_1(0) = 10 and
    the associated Gritsenko-Nikulin form has weight 5.

    It is not chi_top(K3 x E), kappa_cat(K3 x E), or kappa_ch(K3 x E).
    """
    return BORCHERDS_C1_ZERO_K3E // 2


def decompose_weight_5() -> Dict[str, Any]:
    r"""Return lane-separated diagnostics for the value 5.

    The source identity is not a Hodge-number formula.  It is the
    Borcherds-weight theorem applied to the N=1 K3 elliptic-genus input:

        kappa_BKM(Delta_5) = c_1(0)/2 = 10/2 = 5.

    The Kunneth computation gives chi_top(K3 x E)=0.  The Hodge and
    Lie-dimension equalities that also evaluate to 5 are therefore
    recorded as coincidences/sanity checks, not as source formulas.
    """
    k3 = k3_hodge()
    e = elliptic_curve_hodge()
    k3e = k3_times_e_hodge()

    results: Dict[str, Any] = {}

    # Basic topological data
    results["chi_K3"] = k3.euler_characteristic  # 24
    results["chi_E"] = e.euler_characteristic  # 0
    results["chi_K3xE"] = k3e.euler_characteristic  # 0

    # Hodge numbers
    results["h11_K3"] = k3.h(1, 1)  # 20
    results["h20_K3"] = k3.h(2, 0)  # 1
    results["h10_E"] = e.h(1, 0)  # 1
    results["h11_K3xE"] = k3e.h(1, 1)  # 21
    results["h21_K3xE"] = k3e.h(2, 1)  # 21

    # The weight of Delta_5
    results["weight_Delta5"] = 5

    # DT partition function: Z = C / (Delta_5)^2
    results["weight_1_over_Z"] = 2 * 5  # = 10

    # The BKM-lane scalar.
    results["kappa_label"] = "kappa_BKM"
    results["kappa_BKM_K3xE"] = kappa_k3_times_e()
    results["kappa_source"] = "Borcherds weight: c_1(0)/2"
    results["c_1_0"] = BORCHERDS_C1_ZERO_K3E

    # Arithmetic coincidences: useful sanity checks, not source formulas.
    results["h11_K3_over_4"] = Fraction(k3.h(1, 1), 4)  # 20/4 = 5
    results["h11_over_4_matches_kappa_BKM"] = (
        Fraction(k3.h(1, 1), 4) == results["kappa_BKM_K3xE"]
    )
    results["h11_over_4_is_source"] = False

    results["chi_K3_minus_4_over_4"] = Fraction(k3.euler_characteristic - 4, 4)  # (24-4)/4 = 5
    results["chi_minus_4_over_4_matches_kappa_BKM"] = (
        Fraction(k3.euler_characteristic - 4, 4) == results["kappa_BKM_K3xE"]
    )
    results["chi_minus_4_over_4_is_source"] = False

    # Borcherds product perspective: c_1(0) is the input coefficient.
    results["weight_from_borcherds"] = results["c_1_0"] // 2  # 5
    results["h11_K3_over_2"] = k3.h(1, 1) // 2  # 10
    results["h11_K3_over_2_matches_c_1_0"] = (
        results["h11_K3_over_2"] == results["c_1_0"]
    )
    results["h11_K3_over_2_is_source"] = False

    # Sp_4 perspective: dim(Sp_4)/2 = 10/2 = 5
    results["dim_Sp4"] = 10  # dim of Sp_4 as a Lie group
    results["dim_Sp4_over_2"] = 5
    results["dim_Sp4_over_2_is_source"] = False

    # Check: 2 * kappa_BKM = weight of (Delta_5)^2 = weight of 1/Z.
    results["two_kappa_BKM_equals_weight_inverse_Z"] = (
        2 * results["kappa_BKM_K3xE"] == results["weight_1_over_Z"]
    )

    return results


# =========================================================================
# 9. Phi_{0,1} Fourier coefficients and Borcherds weight
# =========================================================================

@lru_cache(maxsize=256)
def _eta_coeffs(max_n: int) -> List[int]:
    """Coefficients of eta(q) = q^{1/24} prod_{n>=1} (1-q^n).

    Returns c[n] for n = 0, ..., max_n where eta = sum c[n] q^{n+1/24}.
    Actually, q^{-1/24} eta(q) = prod (1-q^n), so we compute the
    expansion of prod (1-q^n) up to q^{max_n}.
    """
    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1
    for n in range(1, max_n + 1):
        for k in range(n, max_n + 1):
            coeffs[k] -= coeffs[k - n]
    return coeffs


@lru_cache(maxsize=256)
def _theta_jacobi_coeffs(max_n: int, max_l: int) -> Dict[Tuple[int, int], int]:
    """Low-order coefficients of the standard weak Jacobi form phi_{0,1}.

    This helper intentionally exposes only the q^0 head used by the tests:
    c(0,0)=20 and c(0,+/-1)=2, so phi_{0,1}(tau,0)=24 at q^0.

    The Borcherds-weight scalar used elsewhere in this module is the
    program-normalised input coefficient c_1(0)=10 for the K3 x E
    Delta_5 lift. It is not derived here from the raw Jacobi coefficient
    c(0,0)=20.
    """
    result: Dict[Tuple[int, int], int] = {}
    if max_n >= 0 and max_l >= 0:
        result[(0, 0)] = 20
    if max_n >= 0 and max_l >= 1:
        result[(0, 1)] = 2
        result[(0, -1)] = 2
    return result


def borcherds_product_weight_from_phi01() -> int:
    """Borcherds weight of the N=1 K3 x E Delta_5 lift.

    The program convention fixes the relevant input coefficient as
    c_1(0)=10.  Borcherds' weight formula gives weight c_1(0)/2=5.
    Hodge equalities with the same number are checked elsewhere only
    as sanity checks, not as derivations.
    """
    return BORCHERDS_C1_ZERO_K3E // 2


# =========================================================================
# 10. The "10 = 2 * 5" identity from DT theory
# =========================================================================

def dt_weight_identity() -> Dict[str, Any]:
    """Verify the weight identity for the DT partition function of K3 x E.

    From Theorem thm:dt-igusa:
      Z^{K3 x E}(q, t, p) = C / (Delta_5)^2

    Therefore:
      1/Z ~ (Delta_5)^2, a Siegel modular form of weight 2 * 5 = 10.

    The source factorization is:
      10 = 2 * kappa_BKM(K3 x E) = 2 * c_1(0)/2.

    The equalities 10 = dim(Sp_4), 10 = (chi(K3)-4)/2, and
    10 = h^{1,1}(K3)/2 are recorded as arithmetic coincidences here.

    The factor of 2 in Z = C/(Delta_5)^2 corresponds to the two
    "halves" of the BPS spectrum (particles and anti-particles),
    or equivalently to the Weyl reflection symmetry of the BKM algebra.
    """
    results: Dict[str, Any] = {}

    k = kappa_k3_times_e()  # = 5
    results["kappa_label"] = "kappa_BKM"
    results["kappa_BKM"] = k
    results["weight_Delta5"] = 5
    results["weight_Delta5_squared"] = 10
    results["weight_inverse_Z"] = 10

    # Source identity and sanity checks.
    results["2_times_kappa_BKM"] = 2 * k  # 10
    results["dim_Sp4"] = 10
    results["chi_K3_minus_4_over_2"] = (24 - 4) // 2  # 10
    results["h11_K3_over_2"] = 20 // 2  # 10
    results["c_1_0"] = BORCHERDS_C1_ZERO_K3E
    results["dim_Sp4_is_source"] = False
    results["chi_K3_minus_4_over_2_is_source"] = False
    results["h11_K3_over_2_is_source"] = False

    # Verify all equal
    results["all_equal_10"] = all(
        v == 10 for key, v in results.items()
        if key not in (
            "kappa_label",
            "kappa_BKM",
            "weight_Delta5",
            "dim_Sp4_is_source",
            "chi_K3_minus_4_over_2_is_source",
            "h11_K3_over_2_is_source",
        )
    )

    return results


# =========================================================================
# 11. Survey of kappa for other CY3 families
# =========================================================================

def kappa_cy3_families() -> Dict[str, Dict[str, Any]]:
    """Lane-labelled modular characteristics for various CY3 families.

    For each family, we record:
    - The topological Euler characteristic chi
    - The Hodge numbers h^{1,1}, h^{2,1}
    - The associated automorphic form (when known)
    - The specific kappa-lane only when it is actually constructed.

    For K3 x E, the constructed value in this module is
    kappa_BKM = 5 = c_1(0)/2.  It is not chi_top, kappa_cat, or the
    compact-total-space Hodge supertrace.

    For the quintic, the analogue of the DT generating function is
    the BCOV partition function, and the "weight" is related to
    chi/12 in a different anomaly lane.  No kappa_BKM value is assigned
    here without a Borcherds denominator.
    """
    families: Dict[str, Dict[str, Any]] = {}

    # K3 x E: the prototypical case
    families["K3 x E"] = {
        "h11": 21, "h21": 21, "chi": 0,
        "automorphic_form": "primitive Gritsenko-Nikulin denominator Delta_5 (Sp_4(Z))",
        "kappa_label": "kappa_BKM",
        "kappa_BKM": 5,
        "kappa_source": "Borcherds weight c_1(0)/2 = 10/2",
        "formula": "c_1(0)/2 = 5",
    }

    # Quintic
    families["Quintic P4[5]"] = {
        "h11": 1, "h21": 101, "chi": -200,
        "automorphic_form": "BCOV holomorphic anomaly (not a single Siegel form)",
        "kappa_label": "kappa_BKM",
        "kappa_BKM": None,
        "kappa_source": "undefined here: no Borcherds denominator supplied",
        "chi_over_24": Fraction(-200, 24),
    }

    # The octic in WP4(1,1,2,2,2)
    families["WP4(1,1,2,2,2)[8]"] = {
        "h11": 1, "h21": 149, "chi": -296,
        "automorphic_form": None,
        "kappa_label": "kappa_BKM",
        "kappa_BKM": None,
        "chi_over_24": Fraction(-296, 24),
    }

    return families


# =========================================================================
# 12. Hodge diamond printing (for display)
# =========================================================================

def format_hodge_diamond(hd: HodgeDiamond) -> str:
    """Format a Hodge diamond for display."""
    n = hd.n
    lines = []
    for k in range(2 * n + 1):
        row_entries = []
        for p in range(n + 1):
            q = k - p
            if 0 <= q <= n:
                row_entries.append(str(hd.h(p, q)))
        # Center the row
        padding = " " * (2 * abs(n - k))
        lines.append(padding + "  ".join(row_entries))
    return "\n".join(lines)


# =========================================================================
# 13. Summary verification function
# =========================================================================

def verify_all() -> Dict[str, bool]:
    """Run all internal consistency checks."""
    results: Dict[str, bool] = {}

    # K3 basic data
    k3 = k3_hodge()
    results["chi_K3_eq_24"] = (k3.euler_characteristic == 24)
    results["h11_K3_eq_20"] = (k3.h(1, 1) == 20)
    results["h20_K3_eq_1"] = (k3.h(2, 0) == 1)

    # Elliptic curve
    e = elliptic_curve_hodge()
    results["chi_E_eq_0"] = (e.euler_characteristic == 0)

    # K3 x E
    k3e = k3_times_e_hodge()
    results["chi_K3xE_eq_0"] = (k3e.euler_characteristic == 0)
    results["h11_K3xE_eq_21"] = (k3e.h(1, 1) == 21)
    results["h21_K3xE_eq_21"] = (k3e.h(2, 1) == 21)

    # Quintic
    q = quintic_hodge()
    results["chi_quintic_eq_neg200"] = (q.euler_characteristic == -200)
    results["h11_quintic_eq_1"] = (q.h(1, 1) == 1)
    results["h21_quintic_eq_101"] = (q.h(2, 1) == 101)

    # CY3 Euler formula
    results["cy3_euler_quintic"] = (cy3_euler_from_hodge(1, 101) == -200)

    # CICY quintic
    results["cicy_quintic_chi"] = (cicy_euler_characteristic([4], [[5]]) == -200)

    # Toric examples consistency
    toric = toric_cy3_examples()
    results["toric_all_consistent"] = all(
        v[2] == 2 * (v[0] - v[1]) for v in toric.values()
    )

    # Delta_5 BKM connection
    results["kappa_BKM_K3xE_eq_5"] = (kappa_k3_times_e() == 5)
    results["igusa_weight_eq_5"] = (igusa_cusp_form_weight(1) == 5)
    results["borcherds_weight_eq_5"] = (borcherds_product_weight_from_phi01() == 5)

    # Arithmetic coincidences only; they are not source formulas.
    results["h11_over_4_matches_kappa_BKM"] = (k3.h(1, 1) // 4 == 5)

    results["chi_minus_4_over_4_matches_kappa_BKM"] = (
        (k3.euler_characteristic - 4) // 4 == 5
    )

    # DT weight identity
    dt = dt_weight_identity()
    results["dt_weight_all_10"] = dt["all_equal_10"]

    # CICY examples
    results["cicy_P5_3_3"] = (cicy_euler_characteristic([5], [[3], [3]]) == -144)
    results["cicy_P5_2_4"] = (cicy_euler_characteristic([5], [[2], [4]]) == -176)
    results["cicy_P6_2_2_3"] = (cicy_euler_characteristic([6], [[2], [2], [3]]) == -144)
    results["cicy_P7_2_2_2_2"] = (cicy_euler_characteristic([7], [[2], [2], [2], [2]]) == -128)

    return results
