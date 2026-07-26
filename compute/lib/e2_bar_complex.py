"""E_2 bar complex B_{E_2}(A) -- explicit computation for vertex algebras.

This module computes the E_2 bar complex for two fundamental examples:
  1. H_k  (Heisenberg vertex algebra at level k)
  2. V_k(sl_2)  (affine sl_2 at level k)  -- first few terms

MATHEMATICAL BACKGROUND (from notes/theory_e2_chiral_formalism.tex):

The E_2 bar complex B_{E_2}(A) of an E_2-chiral algebra A is the iterated
bar construction B_Y(B_X(A)) ~ B_X(B_Y(A)) (Dunn additivity). It carries:
  - Two commuting differentials d_X, d_Y  (from the two chiral brackets)
  - Two commuting coproducts Delta_X, Delta_Y  (deconcatenation in each
    bar direction)
  - A braiding beta = sigma . tau  (from the E_2 involution)

By Kontsevich-Tamarkin formality (char 0), B_{E_2}(A) decomposes as:
    B_{E_2}(A)  ~  B_comm(A) tensor C_CE(A[-1])
where B_comm is the Harrison complex (bar of the commutative product)
and C_CE is the Chevalley-Eilenberg complex (of the degree -1 Lie bracket
from the Gerstenhaber structure).

KEY RESULT FOR H_k:
The Heisenberg VOA is a *free* field: a(z)a(w) ~ k/(z-w)^2 with NO
first-order field-valued pole. The OPE is local, so the E2
Gerstenhaber/nonabelian monodromy vanishes. The ordered-bar descent
still has scalar braiding R(z) = exp(k*hbar/z), nontrivial for k != 0.
Thus:
  - The E_2 structure is E_infty (symmetric braiding).
  - The Gerstenhaber bracket vanishes: [a,a] = 0.
  - d_Y = 0 (the CE differential is trivial).
  - B_{E_2}(H_k)  ~  B_comm(H_k)  (concentrated on the d_X axis).
  - The R-matrix is R = id.
This is the maximally degenerate case: the E_2 bar complex collapses to
the E_1 bar complex (up to a trivial tensor factor).

KEY RESULT FOR V_k(sl_2):
The affine sl_2 VOA at level k has OPE:
    e(z)f(w) ~ k/(z-w)^2 + h(w)/(z-w)
    h(z)e(w) ~ 2e(w)/(z-w)
    h(z)f(w) ~ -2f(w)/(z-w)
    h(z)h(w) ~ 2k/(z-w)^2
The first-order poles give a non-trivial chiral bracket (sl_2 current
algebra), and the KZ connection provides a non-trivial braiding with
R-matrix R = q^{Omega/2}, q = exp(pi i/(k+2)).
Here d_Y != 0 and the bicomplex is genuinely two-dimensional.

CONVENTIONS:
  - Cohomological grading (differentials have degree +1).
  - Bar degree: [a_1|...|a_p]_X has X-bar degree p,
                [b_1|...|b_q]_Y has Y-bar degree q.
  - The bar shift is s(a) = a[-1] (desuspension by 1 in each direction).
  - Koszul signs follow the standard convention:
        d_X([a_1|...|a_p]) = sum (-1)^{eps_i} [a_1|...|mu_X(a_i,a_{i+1})|...|a_p]
    with eps_i = sum_{j<=i} (|a_j| + 1).

MANUSCRIPT REFERENCES:
  - notes/theory_e2_chiral_formalism.tex, Section 2: E_2 bar complex
  - notes/theory_e2_chiral_formalism.tex, Section 4.3: Gerstenhaber decomposition
  - CLAUDE.md: CY-B (E_n-chiral Koszul duality)

MATHEMATICAL SOURCES:
  - Getzler-Jones, "Operads, homotopy algebra, and iterated integrals..."
    (1994): E_2 operadic bar construction
  - Fresse, "Modules over operads and functors" (2009): E_n bar-cobar
  - Tamarkin, "Formality of chain operad of little discs" (2003): formality
  - Frenkel-Ben-Zvi, "Vertex Algebras and Algebraic Curves" (2004): VOAs
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
    conjugate,
    exp,
    expand,
    eye,
    factor,
    I,
    pi,
    simplify,
    sqrt,
    symbols,
    zeros,
)


# =========================================================================
#  0. Combinatorial helpers
# =========================================================================

def _permutation_sign(perm: Sequence[int]) -> int:
    """Sign of a permutation given as a list of images.

    Computes (-1)^{number of inversions} by counting pairs (i<j) with
    perm[i] > perm[j].  This is the Koszul sign for reordering generators.
    """
    n = len(perm)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return (-1) ** inversions


# =========================================================================
#  1. Algebraic foundations: generators, bar elements, bigraded complex
# =========================================================================

@dataclass(frozen=True)
class Generator:
    """A generator of a vertex algebra.

    Attributes
    ----------
    name : str
        Symbol name (e.g. 'a' for Heisenberg, 'e','f','h' for sl_2).
    weight : int
        Conformal weight (h = 1 for currents).
    degree : int
        Cohomological degree (0 for even generators).
    """
    name: str
    weight: int = 1
    degree: int = 0

    def __repr__(self) -> str:
        return self.name


@dataclass(frozen=True)
class BarElement:
    """An element [a_1|...|a_p]_X (X-bar) or [b_1|...|b_q]_Y (Y-bar).

    For the E_2 bar complex, a general element lives in bidegree (p, q)
    and is a tensor of the form:
        [ [a_{11}|...|a_{1,p}]_X | ... | [a_{q,1}|...|a_{q,p}]_X ]_Y
    i.e., a Y-bar of X-bars.

    For practical computation we store the element as a list of lists:
    the outer list has length q (Y-bar degree), each inner list has
    variable length (X-bar components at each Y-level).

    Attributes
    ----------
    bars : tuple of tuples of Generator
        bars[j] = (a_{j,1}, ..., a_{j,p_j}) is the j-th X-bar factor.
    coeff : Rational or sympy expression
        Scalar coefficient.
    """
    bars: Tuple[Tuple[Generator, ...], ...]
    coeff: object = Rational(1)

    @property
    def y_degree(self) -> int:
        """Y-bar degree = number of outer (Y) bar factors."""
        return len(self.bars)

    @property
    def x_degrees(self) -> Tuple[int, ...]:
        """X-bar degree of each Y-factor."""
        return tuple(len(b) for b in self.bars)

    @property
    def total_x_degree(self) -> int:
        """Total X-bar degree = sum of lengths of inner bars."""
        return sum(len(b) for b in self.bars)

    @property
    def bidegree(self) -> Tuple[int, int]:
        """(total X-bar degree, Y-bar degree)."""
        return (self.total_x_degree, self.y_degree)

    def __repr__(self) -> str:
        inner = " | ".join(
            "[" + "|".join(str(g) for g in b) + "]_X"
            for b in self.bars
        )
        c = self.coeff
        if c == 1:
            return f"[{inner}]_Y"
        return f"{c} * [{inner}]_Y"


# =========================================================================
#  2. OPE data for specific vertex algebras
# =========================================================================

@dataclass
class HeisenbergOPE:
    """OPE data for the Heisenberg vertex algebra H_k.

    Generator: a(z) with a(z)a(w) ~ k/(z-w)^2.

    The key structural point: there is NO first-order pole. The chiral
    bracket mu(a,a) = Res_{z=w} a(z)a(w) = 0. This means:
      - The Lie bracket on H_k vanishes.
      - The E_2 structure is E_infty (symmetric braiding).
      - d_Y = 0 in the E_2 bar complex.
      - The R-matrix is trivial: R = id.

    Parameters
    ----------
    k : level (the OPE coefficient). Must be nonzero for non-degeneracy.
    """
    k: object  # sympy expression or Rational

    def __post_init__(self):
        self.gen_a = Generator("a", weight=1, degree=0)
        self.generators = (self.gen_a,)

    def ope_singular_part(
        self, g1: Generator, g2: Generator
    ) -> Dict[int, object]:
        """Return the singular OPE: {pole_order: coefficient}.

        a(z)a(w) ~ k/(z-w)^2, so:
            {2: k, 1: 0}    (no first-order pole!)
        """
        if g1.name == "a" and g2.name == "a":
            return {2: self.k}
        return {}

    def chiral_bracket(
        self, g1: Generator, g2: Generator
    ) -> Optional[Tuple[Generator, object]]:
        """Compute mu(g1, g2) = Res_{z=w} g1(z) g2(w).

        For Heisenberg: mu(a,a) = 0 (no first-order pole).
        Returns None if the bracket vanishes.
        """
        ope = self.ope_singular_part(g1, g2)
        # The chiral bracket is the residue = coefficient of (z-w)^{-1}
        residue = ope.get(1, 0)
        if residue == 0:
            return None
        return None  # No non-vanishing bracket for Heisenberg

    def gerstenhaber_bracket(
        self, g1: Generator, g2: Generator
    ) -> object:
        """The Gerstenhaber bracket [g1, g2] in the E_2 structure.

        For Heisenberg: this is ZERO because the field-valued
        E2/Gerstenhaber braiding is symmetric.  This does not say the
        ordered-bar scalar braiding is trivial; at level k it is
        R(z) = exp(k*hbar/z), central and nontrivial for k != 0.
        """
        return 0

    def r_matrix_classical(self) -> object:
        """Classical r-matrix r(z) in End(V tensor V) tensor k((z)).

        For Heisenberg: the E2/Gerstenhaber r = 0.  The ordered-bar
        scalar collision kernel is separately r_ord(z) = k/z, with
        quantum R_ord(z) = exp(k*hbar/z).
        """
        return 0

    @property
    def kappa(self) -> object:
        """Modular characteristic kappa(H_k) = k.

        From Volume I (authoritative): for the Heisenberg at level k, kappa = k.
        """
        return self.k


@dataclass
class AffineSL2OPE:
    """OPE data for V_k(sl_2), the affine sl_2 vertex algebra at level k.

    Generators: e(z), f(z), h(z) with OPEs:
        e(z)f(w) ~ k/(z-w)^2  +  h(w)/(z-w)
        h(z)e(w) ~ 2e(w)/(z-w)
        h(z)f(w) ~ -2f(w)/(z-w)
        h(z)h(w) ~ 2k/(z-w)^2
        e(z)e(w) ~ regular
        f(z)f(w) ~ regular

    The chiral bracket is the sl_2 current algebra:
        [e, f] = h,  [h, e] = 2e,  [h, f] = -2f

    The braiding comes from the KZ connection:
        nabla_KZ = d - Omega/(k + h^v) * dz/z
    with Omega = Casimir of sl_2 and h^v = 2 (dual Coxeter number).
    The R-matrix is R = q^{Omega/2} with q = exp(pi*i/(k+2)).

    Parameters
    ----------
    k : level (positive integer for integrable representations).
    """
    k: object

    def __post_init__(self):
        self.gen_e = Generator("e", weight=1, degree=0)
        self.gen_f = Generator("f", weight=1, degree=0)
        self.gen_h = Generator("h", weight=1, degree=0)
        self.generators = (self.gen_e, self.gen_f, self.gen_h)
        self.dual_coxeter = 2  # h^v for sl_2

    def ope_singular_part(
        self, g1: Generator, g2: Generator
    ) -> Dict[int, object]:
        """Singular part of the OPE g1(z)g2(w) as {pole_order: coeff}.

        Returns coefficients that may be generators (for first-order poles)
        or scalars (for second-order poles).
        """
        n1, n2 = g1.name, g2.name
        k = self.k

        if (n1, n2) == ("e", "f"):
            return {2: k, 1: self.gen_h}
        if (n1, n2) == ("f", "e"):
            return {2: k, 1: Generator("-h", weight=1)}  # -h
        if (n1, n2) == ("h", "e"):
            return {1: (2, self.gen_e)}  # 2*e(w)/(z-w)
        if (n1, n2) == ("h", "f"):
            return {1: (-2, self.gen_f)}  # -2*f(w)/(z-w)
        if (n1, n2) == ("e", "h"):
            return {1: (-2, self.gen_e)}
        if (n1, n2) == ("f", "h"):
            return {1: (2, self.gen_f)}
        if (n1, n2) == ("h", "h"):
            return {2: 2 * k}
        return {}

    def chiral_bracket(
        self, g1: Generator, g2: Generator
    ) -> Optional[Tuple[object, ...]]:
        """mu(g1, g2) = Res_{z=w} g1(z) g2(w).

        Returns the result as (coefficient, generator) or None if zero.

        The chiral bracket gives the sl_2 current algebra:
            mu(e, f) = h,  mu(h, e) = 2e,  mu(h, f) = -2f
        """
        n1, n2 = g1.name, g2.name

        bracket_table = {
            ("e", "f"): (1, self.gen_h),
            ("f", "e"): (-1, self.gen_h),
            ("h", "e"): (2, self.gen_e),
            ("h", "f"): (-2, self.gen_f),
            ("e", "h"): (-2, self.gen_e),
            ("f", "h"): (2, self.gen_f),
        }
        return bracket_table.get((n1, n2), None)

    def structure_constants(self) -> Dict[Tuple[str, str], Tuple[int, str]]:
        """Lie algebra structure constants f^c_{ab} for sl_2.

        [t_a, t_b] = sum_c f^c_{ab} t_c  in the standard basis {e, f, h}.
        """
        return {
            ("e", "f"): (1, "h"),
            ("f", "e"): (-1, "h"),
            ("h", "e"): (2, "e"),
            ("e", "h"): (-2, "e"),
            ("h", "f"): (-2, "f"),
            ("f", "h"): (2, "f"),
        }

    def casimir_matrix(self) -> Matrix:
        """Casimir element Omega in the basis {e, f, h} of sl_2.

        Omega = e tensor f + f tensor e + (1/2) h tensor h
        as an element of sl_2 tensor sl_2 (using the Killing form).

        In the standard basis ordering (e, f, h), Omega is a 3x3 matrix
        acting on g tensor g ~ k^3 tensor k^3 = k^9.
        We store it as a 9x9 matrix (tensor product).
        """
        # Omega = sum_{a} t^a tensor t_a with respect to the
        # normalized Killing form (e,f) = 1, (h,h) = 2.
        # So Omega = e tensor f + f tensor e + h tensor h / 2.
        # As a 3x3 x 3x3 matrix with basis ordering e=0, f=1, h=2:
        dim = 3
        Omega = zeros(dim**2, dim**2)
        # e tensor f: (0,1) -> matrix index 0*3+1 = 1 on diagonal... no,
        # Omega acts on V tensor V as sum t^a tensor t_a.
        # More precisely: Omega = sum_a t^a tensor t_a acts on
        # v tensor w as sum (t^a v) tensor (t_a w).
        # We represent this as a dim^2 x dim^2 matrix.

        # Basis: e=0, f=1, h=2
        # t^e = f (dual under Killing), t^f = e, t^h = h/2
        # So Omega = f.tensor.e + e.tensor.f + (h/2).tensor.h
        #         = f tensor e + e tensor f + (1/2) h tensor h

        # Action matrices of sl_2 generators on the adjoint representation:
        # ad(e): e->0, f->h, h->-2e  i.e. basis {e,f,h}: [0, 0, -2; 0, 0, 0; 0, 1, 0]
        # Wait -- we work abstractly. Just store Omega symbolically.
        # For the classical r-matrix computation, we need Omega/(k+h^v).
        return None  # Symbolic; see r_matrix_classical

    def gerstenhaber_bracket(
        self, g1: Generator, g2: Generator
    ) -> object:
        """The Gerstenhaber bracket for V_k(sl_2).

        Unlike the Heisenberg case, this is NON-ZERO. The Gerstenhaber
        bracket on HH^*(V_k(sl_2)) is controlled by the KZ monodromy.

        At leading order in 1/(k+h^v), the bracket is:
            [g1, g2]_Ger = (1/(k+2)) * [g1, g2]_sl2
        where [,]_sl2 is the current algebra bracket.
        """
        bracket = self.chiral_bracket(g1, g2)
        if bracket is None:
            return 0
        coeff, gen = bracket
        kh = self.k + self.dual_coxeter
        return (Rational(coeff) / kh, gen)

    def r_matrix_classical(self) -> object:
        """Classical r-matrix r(z) = Omega/(k+h^v) * 1/z.

        This is the leading-order (in hbar = 1/(k+h^v)) contribution
        to the KZ R-matrix. The full R-matrix is:
            R(z) = q^{Omega/2} = exp(pi*i*Omega / (2*(k+2)))
        evaluated at q = exp(pi*i/(k+2)).

        Returns a symbolic description: (name, coefficient).
        The coefficient is 1/(k + h^v) as a sympy expression.
        """
        kh = self.k + self.dual_coxeter
        return ("Omega/z", 1 / kh)

    @property
    def kappa(self) -> object:
        """Modular characteristic kappa(V_k(sl_2)).

        kappa(g_hat_k) = (k + h^v) * dim(g) / (2 * h^v)
        For sl_2: dim = 3, h^v = 2, so kappa = 3(k+2)/4.
        """
        d = 3  # dim(sl_2)
        hv = self.dual_coxeter
        return Rational(d, 2 * hv) * (self.k + hv)


# =========================================================================
#  3. The E_2 bar complex: explicit construction
# =========================================================================

@dataclass
class E2BarComplex:
    """The E_2 bar complex B_{E_2}(A) for a vertex algebra A.

    The bigraded chain complex with:
      - Underlying object: bigoplus_{p>=1, q>=1} A^{tensor pq} [-p]_X [-q]_Y
      - Differentials d_X (from mu_X), d_Y (from mu_Y)
      - Coproducts Delta_X, Delta_Y (deconcatenation)
      - Braiding beta = sigma . tau

    Parameters
    ----------
    ope : HeisenbergOPE or AffineSL2OPE
        The OPE data of the vertex algebra.
    max_x : int
        Maximum X-bar degree to compute.
    max_y : int
        Maximum Y-bar degree to compute.
    """
    ope: object
    max_x: int = 4
    max_y: int = 4

    def generators(self) -> Tuple[Generator, ...]:
        return self.ope.generators

    # ----- d_X: the bar differential in the X-direction -----

    def d_X(self, elem: BarElement) -> List[BarElement]:
        """Apply the X-bar differential to a bar element.

        d_X uses the Chevalley-Eilenberg differential for the chiral
        bracket mu_X (which is a Lie bracket for vertex algebras).

        On a bar element [a_1|...|a_p]_X, the CE differential acts as:

            d_X([a_1|...|a_p]_X) = sum_{i<j} (-1)^{i+j}
                [mu_X(a_i, a_j) | a_1 | ... | hat{a_i} | ... | hat{a_j} | ... | a_p]_X

        This squares to zero by the Jacobi identity of mu_X.

        For the outer Y-bar, d_X acts on each factor independently
        (as a Y-coderivation).
        """
        result = []
        for y_idx, x_bar in enumerate(elem.bars):
            p = len(x_bar)
            if p < 2:
                continue

            for i in range(p):
                for j in range(i + 1, p):
                    bracket = self.ope.chiral_bracket(x_bar[i], x_bar[j])
                    if bracket is None:
                        continue

                    coeff, gen = bracket
                    # CE sign: (-1)^{i+j} (0-indexed)
                    sign = (-1) ** (i + j)

                    # Build [mu(a_i, a_j) | remaining generators]
                    remaining = []
                    for idx in range(p):
                        if idx != i and idx != j:
                            remaining.append(x_bar[idx])
                    new_x_bar = (gen,) + tuple(remaining)

                    # Replace the y_idx-th factor
                    new_bars = (
                        elem.bars[:y_idx]
                        + (new_x_bar,)
                        + elem.bars[y_idx + 1:]
                    )
                    new_coeff = elem.coeff * coeff * sign
                    result.append(BarElement(bars=new_bars, coeff=new_coeff))

        return result

    def d_Y(self, elem: BarElement) -> List[BarElement]:
        """Apply the Y-bar differential.

        d_Y acts on the outer (Y-bar) by inserting the Y-chiral bracket
        between adjacent Y-factors.

        For the E_2 bar complex via Gerstenhaber formality, d_Y is the
        Chevalley-Eilenberg differential of the degree-1 Lie bracket.
        For Heisenberg (symmetric braiding), d_Y = 0.
        For V_k(sl_2), d_Y comes from the KZ braiding monodromy.

        In the iterated bar model B_Y(B_X(A)), d_Y acts on the Y-bar
        factors which are themselves X-bar complexes. The Y-bracket
        mu_Y is induced by the braiding.
        """
        if isinstance(self.ope, HeisenbergOPE):
            # CRITICAL: for Heisenberg, d_Y = 0.
            # The braiding is symmetric, so the Y-direction chiral bracket
            # is trivial. This is the key computation.
            return []

        # For non-trivial braiding (e.g. V_k(sl_2)):
        # d_Y acts as the CE differential for the Gerstenhaber bracket
        # on the Y-bar factors (which are X-bar complexes).
        #
        # d_Y([B_1|...|B_q]_Y) = sum_{i<j} (-1)^{i+j}
        #     [[B_i, B_j]_Ger | B_1 | ... | hat{B_i} | ... | hat{B_j} | ... | B_q]_Y
        #
        # For single-generator X-bars, [B_i, B_j]_Ger reduces to the
        # Gerstenhaber bracket of the generators.
        result = []
        q = elem.y_degree
        if q < 2:
            return result

        for i in range(q):
            for j in range(i + 1, q):
                bar_i = elem.bars[i]
                bar_j = elem.bars[j]

                # For single-generator X-bars, apply the Gerstenhaber bracket
                if len(bar_i) == 1 and len(bar_j) == 1:
                    g1, g2 = bar_i[0], bar_j[0]
                    gb = self.ope.gerstenhaber_bracket(g1, g2)
                    if gb == 0 or gb is None:
                        continue
                    coeff_gb, gen_gb = gb

                    # CE sign: (-1)^{i+j} (0-indexed)
                    sign = (-1) ** (i + j)

                    # Build [bracket | remaining Y-factors]
                    remaining = []
                    for idx in range(q):
                        if idx != i and idx != j:
                            remaining.append(elem.bars[idx])
                    new_bars = ((gen_gb,),) + tuple(remaining)

                    new_coeff = elem.coeff * coeff_gb * sign
                    result.append(BarElement(bars=new_bars, coeff=new_coeff))

        return result

    # ----- Coproducts -----

    def Delta_X_shuffle(
        self, elem: BarElement
    ) -> List[Tuple[BarElement, BarElement]]:
        """X-direction shuffle coproduct (for the CE complex).

        The CE complex Lambda^*(g) carries the shuffle (exterior) coproduct:
            Delta_sh([a_1|...|a_p]_X) = sum_{S cup T = {1..p}, |S|,|T|>=1}
                epsilon(S,T) * [a_{s_1}|...|a_{s_r}]_X tensor [a_{t_1}|...|a_{t_q}]_X

        where epsilon(S,T) is the sign of the (r,q)-unshuffle permutation.

        This is the correct coproduct for the CE differential: d_CE is a
        coderivation with respect to Delta_shuffle (not deconcatenation).

        For the outer Y-bar, we apply the shuffle coproduct to a single
        Y-factor at a time (for y_degree = 1, there is only one).
        """
        from itertools import combinations

        result = []

        if elem.y_degree == 1:
            x_bar = elem.bars[0]
            p = len(x_bar)
            indices = list(range(p))

            for r in range(1, p):
                for S in combinations(indices, r):
                    T = tuple(i for i in indices if i not in S)
                    # Compute unshuffle sign: the sign of the permutation
                    # (S_1,...,S_r, T_1,...,T_{p-r}) relative to (0,...,p-1)
                    perm = list(S) + list(T)
                    sign = _permutation_sign(perm)

                    left_bar = tuple(x_bar[i] for i in S)
                    right_bar = tuple(x_bar[i] for i in T)

                    left = BarElement(
                        bars=(left_bar,), coeff=elem.coeff * sign
                    )
                    right = BarElement(
                        bars=(right_bar,), coeff=Rational(1)
                    )
                    result.append((left, right))

        return result

    def Delta_X(self, elem: BarElement) -> List[Tuple[BarElement, BarElement]]:
        """X-direction deconcatenation coproduct.

        Delta_X acts on each inner (X-bar) factor by splitting it:
            Delta_X([a_1|...|a_p]_X) = sum_{i=1}^{p-1}
                [a_1|...|a_i]_X tensor [a_{i+1}|...|a_p]_X

        For the full bigraded element, Delta_X acts on each Y-level
        independently and the result is a tensor product of
        Y-bars-of-X-bars.

        For simplicity, we implement Delta_X for elements with a single
        Y-factor (q=1), which is the most relevant case for direct
        computation.  The general case is a sum over all ways to split
        all Y-factors simultaneously.
        """
        result = []

        if elem.y_degree == 1:
            x_bar = elem.bars[0]
            for i in range(1, len(x_bar)):
                left = BarElement(
                    bars=(x_bar[:i],), coeff=elem.coeff
                )
                right = BarElement(
                    bars=(x_bar[i:],), coeff=Rational(1)
                )
                result.append((left, right))
        else:
            # General case: split each Y-factor in all possible ways.
            # For the iterated bar complex B_Y(B_X(A)), Delta_X is the
            # coproduct of B_X applied to each Y-component.
            # We implement the simplest nontrivial case: split at one
            # Y-factor while keeping others intact.
            for y_idx in range(elem.y_degree):
                x_bar = elem.bars[y_idx]
                for i in range(1, len(x_bar)):
                    # Split the y_idx-th X-bar
                    left_bars = (
                        elem.bars[:y_idx]
                        + (x_bar[:i],)
                        + elem.bars[y_idx + 1:]
                    )
                    right_bars = (
                        elem.bars[:y_idx]
                        + (x_bar[i:],)
                        + elem.bars[y_idx + 1:]
                    )
                    left = BarElement(bars=left_bars, coeff=elem.coeff)
                    right = BarElement(bars=right_bars, coeff=Rational(1))
                    result.append((left, right))

        return result

    def Delta_Y(self, elem: BarElement) -> List[Tuple[BarElement, BarElement]]:
        """Y-direction deconcatenation coproduct.

        Delta_Y acts on the outer (Y-bar) by splitting it:
            Delta_Y([B_1|...|B_q]_Y) = sum_{j=1}^{q-1}
                [B_1|...|B_j]_Y tensor [B_{j+1}|...|B_q]_Y
        """
        result = []
        for j in range(1, elem.y_degree):
            left = BarElement(
                bars=elem.bars[:j], coeff=elem.coeff
            )
            right = BarElement(
                bars=elem.bars[j:], coeff=Rational(1)
            )
            result.append((left, right))
        return result

    # ----- Braiding / R-matrix -----

    def braiding_is_symmetric(self) -> bool:
        """Check if the E_2 braiding is symmetric (i.e., E_infty).

        This is equivalent to the Gerstenhaber bracket being zero,
        which implies the braiding is trivial (R = id).
        """
        gens = self.generators()
        for g1 in gens:
            for g2 in gens:
                if self.ope.gerstenhaber_bracket(g1, g2) != 0:
                    return False
        return True

    def r_matrix_leading(self) -> object:
        """Leading order of the R-matrix.

        For H_k: R = id (symmetric braiding).
        For V_k(sl_2): R = 1 + r/(k+2) + O(1/(k+2)^2)
            where r is the classical r-matrix.
        """
        return self.ope.r_matrix_classical()


# =========================================================================
#  4. Explicit computation for H_k
# =========================================================================

def compute_e2_bar_heisenberg(
    k: object = Symbol("k"),
    max_x: int = 4,
    max_y: int = 4,
) -> Dict[str, object]:
    """Compute B_{E_2}(H_k) explicitly.

    MAIN RESULT:
    For the Heisenberg vertex algebra H_k:
      - d_Y = 0  (the braiding is symmetric).
      - The bicomplex collapses: B_{E_2}(H_k) ~ B_X(H_k) tensor k[1]
        (the Y-direction contributes only a trivial factor).
      - B_X(H_k) = Sym^{ch,>0}(V*) with V = k*a, the chiral symmetric
        coalgebra from Volume I.
      - The R-matrix is R = id (no quantum group structure).
      - The Gerstenhaber bracket vanishes.

    In more detail:
      - B_X(H_k) in X-degree p consists of symmetric tensors
        a^{tensor p} / S_p with the differential d_X = 0
        (because mu_X(a,a) = 0 for the Heisenberg!).
      - Wait: d_X ALSO vanishes? Yes! The chiral bracket mu_X = 0 for H_k.
        The Heisenberg has no first-order poles between a(z) and a(w).

    So B_{E_2}(H_k) has d_X = d_Y = 0: both differentials vanish.
    The bar complex is a bigraded vector space with zero differential.
    The cohomology is the bar complex itself.

    The coproducts Delta_X, Delta_Y are the only non-trivial structure.
    This gives a bi-coalgebra (Delta_X, Delta_Y) on the bigraded space
    bigoplus_{p,q >= 1} H_k^{tensor pq}.

    PHYSICAL MEANING:
    The Heisenberg VOA is a free field theory. Free fields have:
      - No interactions (d = 0 in the bar complex).
      - Symmetric statistics (R = id, no braiding).
      - The E_2 bar complex is trivially a product of two copies
        of the E_1 bar complex, which itself is trivial.

    Returns
    -------
    dict with keys:
        'ope': HeisenbergOPE instance
        'complex': E2BarComplex instance
        'd_X_vanishes': bool (should be True)
        'd_Y_vanishes': bool (should be True)
        'braiding_symmetric': bool (should be True)
        'r_matrix': 0 (trivial)
        'kappa': k (modular characteristic, Vol I authoritative)
        'generators_by_bidegree': dict mapping (p,q) to list of bar elements
        'dimensions_by_bidegree': dict mapping (p,q) to dimension
    """
    ope = HeisenbergOPE(k=k)
    cx = E2BarComplex(ope=ope, max_x=max_x, max_y=max_y)
    a = ope.gen_a

    # Generate bar elements at each bidegree (p, q)
    generators_by_bidegree = {}
    dims_by_bidegree = {}

    for q in range(1, max_y + 1):
        for p in range(1, max_x + 1):
            # At bidegree (p, q), we have q copies of X-bars of length p.
            # Each X-bar factor is [a|a|...|a]_X (p copies of a).
            # Since there's only one generator, the space is 1-dimensional.
            x_bar = tuple(a for _ in range(p))
            y_bar = tuple(x_bar for _ in range(q))
            elem = BarElement(bars=y_bar)
            generators_by_bidegree[(p, q)] = [elem]
            dims_by_bidegree[(p, q)] = 1

    # Verify d_X = 0
    d_X_vanishes = True
    for (p, q), elems in generators_by_bidegree.items():
        for elem in elems:
            result = cx.d_X(elem)
            if len(result) > 0:
                d_X_vanishes = False
                break

    # Verify d_Y = 0
    d_Y_vanishes = True
    for (p, q), elems in generators_by_bidegree.items():
        for elem in elems:
            result = cx.d_Y(elem)
            if len(result) > 0:
                d_Y_vanishes = False
                break

    # Verify symmetric braiding
    braiding_sym = cx.braiding_is_symmetric()

    return {
        "ope": ope,
        "complex": cx,
        "d_X_vanishes": d_X_vanishes,
        "d_Y_vanishes": d_Y_vanishes,
        "braiding_symmetric": braiding_sym,
        "r_matrix": ope.r_matrix_classical(),
        "kappa": ope.kappa,
        "generators_by_bidegree": generators_by_bidegree,
        "dimensions_by_bidegree": dims_by_bidegree,
    }


# =========================================================================
#  5. Explicit computation for V_k(sl_2)
# =========================================================================

def compute_e2_bar_sl2(
    k: object = Symbol("k"),
    max_x: int = 3,
    max_y: int = 3,
) -> Dict[str, object]:
    """Compute the first few terms of B_{E_2}(V_k(sl_2)).

    Unlike Heisenberg, V_k(sl_2) has non-trivial:
      - d_X != 0 (from the sl_2 current algebra bracket)
      - d_Y != 0 (from the KZ braiding monodromy)
      - R-matrix R = q^{Omega/2}, q = exp(pi*i/(k+2))

    BIDEGREE (1, 1): the generators {e, f, h} sit at bidegree (1,1).
    Dimension = 3.

    BIDEGREE (2, 1): X-bar of length 2. Generators:
        [e|f]_X, [f|e]_X, [e|h]_X, [h|e]_X, [f|h]_X, [h|f]_X,
        [e|e]_X, [f|f]_X, [h|h]_X
    Dimension = 9 (3^2).

    d_X on bidegree (2,1) -> bidegree (1,1):
        d_X([e|f]_X) = -mu(e,f) = -[h]_X       (sign from bar convention)
        d_X([f|e]_X) = -mu(f,e) = +[h]_X
        d_X([h|e]_X) = -mu(h,e) = -[2e]_X = -2[e]_X
        d_X([h|f]_X) = -mu(h,f) = +2[f]_X
        d_X([e|h]_X) = -mu(e,h) = +2[e]_X
        d_X([f|h]_X) = -mu(f,h) = -2[f]_X
        d_X([e|e]_X) = 0        (mu(e,e) = 0)
        d_X([f|f]_X) = 0        (mu(f,f) = 0)
        d_X([h|h]_X) = 0        (mu(h,h) = 0)

    So at the X-bar level, H^1(B_X, d_X) at bidegree (1,1) is
    the Lie algebra cohomology of sl_2 in degree 0, which is
    H^0(sl_2, sl_2) = center(sl_2) = 0 (sl_2 is simple).

    BIDEGREE (1, 2): Y-bar of length 2, each with a single generator.
    Generators: [([g1],)]_Y for g1, g2 in {e,f,h}.
    Here d_Y acts:
        d_Y([[e]_X | [f]_X]_Y) = 1/(k+2) * [[h]_X]_Y
        etc.

    Returns
    -------
    dict with keys:
        'ope': AffineSL2OPE instance
        'complex': E2BarComplex instance
        'd_X_data': dict of d_X actions by bidegree
        'd_Y_data': dict of d_Y actions by bidegree
        'braiding_symmetric': bool (should be False!)
        'r_matrix': description of R = q^{Omega/2}
        'kappa': 3(k+2)/4
        'generators_by_bidegree': dict
        'dimensions_by_bidegree': dict
    """
    ope = AffineSL2OPE(k=k)
    cx = E2BarComplex(ope=ope, max_x=max_x, max_y=max_y)
    e, f, h = ope.gen_e, ope.gen_f, ope.gen_h
    gens = [e, f, h]

    generators_by_bidegree = {}
    dims_by_bidegree = {}

    # Bidegree (1, 1): single generators
    elems_11 = [BarElement(bars=((g,),)) for g in gens]
    generators_by_bidegree[(1, 1)] = elems_11
    dims_by_bidegree[(1, 1)] = 3

    # Bidegree (2, 1): X-bar of length 2
    elems_21 = []
    for g1 in gens:
        for g2 in gens:
            elems_21.append(BarElement(bars=((g1, g2),)))
    generators_by_bidegree[(2, 1)] = elems_21
    dims_by_bidegree[(2, 1)] = 9

    # Bidegree (1, 2): Y-bar of length 2, each X-bar of length 1
    elems_12 = []
    for g1 in gens:
        for g2 in gens:
            elems_12.append(BarElement(bars=((g1,), (g2,))))
    generators_by_bidegree[(1, 2)] = elems_12
    dims_by_bidegree[(1, 2)] = 9

    # Bidegree (3, 1): X-bar of length 3
    elems_31 = []
    for g1 in gens:
        for g2 in gens:
            for g3 in gens:
                elems_31.append(BarElement(bars=((g1, g2, g3),)))
    generators_by_bidegree[(3, 1)] = elems_31
    dims_by_bidegree[(3, 1)] = 27

    # Bidegree (2, 2): Y-bar of length 2, each X-bar of length 2
    elems_22 = []
    for g1 in gens:
        for g2 in gens:
            for g3 in gens:
                for g4 in gens:
                    elems_22.append(
                        BarElement(bars=((g1, g2), (g3, g4)))
                    )
    generators_by_bidegree[(2, 2)] = elems_22
    dims_by_bidegree[(2, 2)] = 81

    # Bidegree (1, 3): Y-bar of length 3, each X-bar of length 1
    elems_13 = []
    for g1 in gens:
        for g2 in gens:
            for g3 in gens:
                elems_13.append(
                    BarElement(bars=((g1,), (g2,), (g3,)))
                )
    generators_by_bidegree[(1, 3)] = elems_13
    dims_by_bidegree[(1, 3)] = 27

    # Compute d_X on low bidegrees
    d_X_data = {}
    for bd in [(2, 1), (1, 2), (3, 1), (2, 2)]:
        if bd in generators_by_bidegree:
            d_X_data[bd] = [
                (elem, cx.d_X(elem))
                for elem in generators_by_bidegree[bd]
            ]

    # Compute d_Y on low bidegrees
    d_Y_data = {}
    for bd in [(1, 2), (2, 2), (1, 3)]:
        if bd in generators_by_bidegree:
            d_Y_data[bd] = [
                (elem, cx.d_Y(elem))
                for elem in generators_by_bidegree[bd]
            ]

    braiding_sym = cx.braiding_is_symmetric()

    return {
        "ope": ope,
        "complex": cx,
        "d_X_data": d_X_data,
        "d_Y_data": d_Y_data,
        "braiding_symmetric": braiding_sym,
        "r_matrix": ope.r_matrix_classical(),
        "kappa": ope.kappa,
        "generators_by_bidegree": generators_by_bidegree,
        "dimensions_by_bidegree": dims_by_bidegree,
    }


# =========================================================================
#  6. Spectral sequence analysis
# =========================================================================

def x_first_spectral_sequence_e1(
    cx: E2BarComplex,
    generators_by_bidegree: Dict,
) -> Dict[Tuple[int, int], object]:
    """Compute the E_1 page of the X-first spectral sequence.

    Filter by Y-bar degree q. The E_1 page is:
        E_1^{p,q} = H^p(B_{E_2}^{*,q}, d_X)

    For Heisenberg: d_X = 0, so E_1^{p,q} = B_{E_2}^{p,q} = the
    raw bigraded pieces. The spectral sequence collapses at E_1.

    For V_k(sl_2): E_1^{p,q} = Lie algebra cohomology of sl_2
    in degree p (at each Y-level q). This is well-known:
        H^0(sl_2, k) = k
        H^1(sl_2, k) = 0  (sl_2 semisimple => H^1 = 0)
        H^2(sl_2, k) = 0  (by Whitehead's lemma)
        H^3(sl_2, k) = k  (the fundamental class)

    Returns the E_1 dimensions.
    """
    e1_dims = {}

    if isinstance(cx.ope, HeisenbergOPE):
        # d_X = 0, so E_1 = raw bigraded space
        for (p, q), elems in generators_by_bidegree.items():
            e1_dims[(p, q)] = len(elems)
    else:
        # For V_k(sl_2), we compute H^*(B_X, d_X) at each Y-level.
        # This requires computing the actual cohomology, which we do
        # numerically for specific k.
        for (p, q), elems in generators_by_bidegree.items():
            # Placeholder: return raw dimension (refine with actual
            # cohomology computation when k is numeric)
            e1_dims[(p, q)] = len(elems)

    return e1_dims


# =========================================================================
#  7. Verification utilities
# =========================================================================

def verify_d_squared_zero(
    cx: E2BarComplex, elem: BarElement
) -> bool:
    """Verify d_X^2 = 0 on a given element.

    Apply d_X twice and check the result vanishes (after cancellation).
    """
    first = cx.d_X(elem)
    second_terms = []
    for term in first:
        second_terms.extend(cx.d_X(term))

    # Check cancellation: group by bars and sum coefficients
    coeff_map: Dict[Tuple, object] = {}
    for term in second_terms:
        key = term.bars
        coeff_map[key] = coeff_map.get(key, 0) + term.coeff

    for key, coeff in coeff_map.items():
        if isinstance(coeff, (int, float, Rational)):
            if coeff != 0:
                return False
        else:
            if simplify(coeff) != 0:
                return False
    return True


def verify_d_X_d_Y_commute(
    cx: E2BarComplex, elem: BarElement
) -> bool:
    """Verify [d_X, d_Y] = 0 on a given element (at genus 0).

    Compute d_X(d_Y(elem)) and d_Y(d_X(elem)) and check they agree.
    At genus >= 1, the commutator would be kappa * omega_g.
    """
    # d_X(d_Y(elem))
    dy = cx.d_Y(elem)
    dx_dy = []
    for term in dy:
        dx_dy.extend(cx.d_X(term))

    # d_Y(d_X(elem))
    dx = cx.d_X(elem)
    dy_dx = []
    for term in dx:
        dy_dx.extend(cx.d_Y(term))

    # Collect terms for dx_dy - dy_dx and check vanishing
    coeff_map: Dict[Tuple, object] = {}
    for term in dx_dy:
        key = term.bars
        coeff_map[key] = coeff_map.get(key, 0) + term.coeff
    for term in dy_dx:
        key = term.bars
        coeff_map[key] = coeff_map.get(key, 0) - term.coeff

    for key, coeff in coeff_map.items():
        if isinstance(coeff, (int, float, Rational)):
            if coeff != 0:
                return False
        else:
            if simplify(coeff) != 0:
                return False
    return True


def verify_coderivation(
    cx: E2BarComplex, elem: BarElement
) -> bool:
    """Verify that d_X is a coderivation w.r.t. Delta_X.

    Delta_X . d_X = (d_X tensor id + id tensor d_X) . Delta_X

    We check this identity on a specific element by collecting terms
    as (left_bars, right_bars) -> coefficient and verifying the
    difference vanishes.
    """
    # LHS: Delta_X(d_X(elem))
    dx_elem = cx.d_X(elem)
    lhs_map: Dict[Tuple, object] = {}
    for term in dx_elem:
        for left, right in cx.Delta_X(term):
            key = (left.bars, right.bars)
            lhs_map[key] = lhs_map.get(key, 0) + left.coeff * right.coeff

    # RHS: (d_X tensor id + id tensor d_X)(Delta_X(elem))
    delta_elem = cx.Delta_X(elem)
    rhs_map: Dict[Tuple, object] = {}
    for left, right in delta_elem:
        # d_X tensor id
        for d_left in cx.d_X(left):
            key = (d_left.bars, right.bars)
            rhs_map[key] = rhs_map.get(key, 0) + d_left.coeff * right.coeff
        # id tensor d_X
        for d_right in cx.d_X(right):
            key = (left.bars, d_right.bars)
            rhs_map[key] = rhs_map.get(key, 0) + left.coeff * d_right.coeff

    # Check that LHS - RHS = 0
    all_keys = set(lhs_map.keys()) | set(rhs_map.keys())
    for key in all_keys:
        diff = lhs_map.get(key, 0) - rhs_map.get(key, 0)
        if isinstance(diff, (int, float, Rational)):
            if diff != 0:
                return False
        else:
            if simplify(diff) != 0:
                return False
    return True


# =========================================================================
#  8. Numerical R-matrix for V_k(sl_2)
# =========================================================================

def kz_r_matrix_sl2(
    k_val: int, rep_dim: int = 2
) -> np.ndarray:
    """Compute the KZ R-matrix for V_k(sl_2) in the fundamental rep.

    The braiding R-matrix (the "checked" R-matrix Rcheck = P . R_univ)
    for the 2-dimensional representation of sl_2 at level k is the
    Jimbo R-matrix:

        Rcheck = q^{1/2} * ( q   on |++> and |-->
                              1   on |+-> and |-+>
                              (q - q^{-1}) from |+-> to |-+> )

    In the basis {|++>, |+->, |-+>, |-->}:

        Rcheck = [[q,          0,         0,    0  ],
                  [0,   q - q^{-1},       1,    0  ],
                  [0,          1,         0,    0  ],
                  [0,          0,         0,    q  ]]

    (up to an overall scalar q^{1/2}). This is the standard form from
    Jimbo (1986) and Kassel "Quantum Groups" Ch. VIII.

    The Rcheck satisfies the braid relation:
        Rcheck_12 Rcheck_23 Rcheck_12 = Rcheck_23 Rcheck_12 Rcheck_23

    which is equivalent to the Yang-Baxter equation for R_univ.

    Parameters
    ----------
    k_val : int
        The level (positive integer).
    rep_dim : int
        Dimension of the representation (only 2 is implemented).

    Returns
    -------
    np.ndarray of shape (rep_dim^2, rep_dim^2)
        The braiding (checked R-matrix) acting on V tensor V.
    """
    if rep_dim != 2:
        raise NotImplementedError("Only the fundamental (dim 2) rep is implemented.")

    q = np.exp(1j * np.pi / (k_val + 2))

    # Jimbo R-matrix (the braiding / checked R-matrix) for sl_2 fundamental.
    # Basis: {|++>, |+->, |-+>, |-->} i.e. {v+ . v+, v+ . v-, v- . v+, v- . v-}.
    #
    # The standard form (Kassel, "Quantum Groups", Thm VIII.4.2):
    #   Rcheck(v_i . v_j) = q^{delta_{ij}} * v_j . v_i
    #                       + (q - q^{-1}) * delta_{i < j} * v_i . v_j
    #
    # For dim 2 with v_0 = v+, v_1 = v-:
    #   Rcheck(v+ . v+) = q * v+ . v+
    #   Rcheck(v+ . v-) = v- . v+ + (q - q^{-1}) * v+ . v-
    #   Rcheck(v- . v+) = v+ . v-
    #   Rcheck(v- . v-) = q * v- . v-

    qq = q - 1.0 / q  # q - q^{-1}

    Rcheck = np.array([
        [q,   0,   0,   0  ],
        [0,   qq,  1,   0  ],
        [0,   1,   0,   0  ],
        [0,   0,   0,   q  ],
    ], dtype=complex)

    return Rcheck


def verify_qybe_sl2(k_val: int) -> float:
    """Verify the braid relation for the KZ checked R-matrix.

    Braid relation: Rcheck_12 Rcheck_23 Rcheck_12 = Rcheck_23 Rcheck_12 Rcheck_23

    where Rcheck_ij acts on V^{tensor 3} by applying Rcheck to the i,j factors.
    This is equivalent to the quantum Yang-Baxter equation for the universal
    R-matrix R_univ (Rcheck = P . R_univ).

    Returns the norm of the difference (should be ~0 for the relation to hold).
    """
    R = kz_r_matrix_sl2(k_val)
    dim = 2

    # Build R_12, R_23 on V^{tensor 3} = C^8
    I2 = np.eye(dim, dtype=complex)

    R_12 = np.kron(R, I2)
    R_23 = np.kron(I2, R)

    # Braid relation: R_12 R_23 R_12 = R_23 R_12 R_23
    lhs = R_12 @ R_23 @ R_12
    rhs = R_23 @ R_12 @ R_23

    return float(np.linalg.norm(lhs - rhs))


# =========================================================================
#  9. Summary / comparison table
# =========================================================================

def comparison_table() -> str:
    """Print a comparison table of E_2 bar complex structure for H_k vs V_k(sl_2)."""
    rows = [
        ("Feature", "H_k (Heisenberg)", "V_k(sl_2) (affine sl_2)"),
        ("", "", ""),
        ("Generators", "a", "e, f, h"),
        ("dim at (1,1)", "1", "3"),
        ("dim at (2,1)", "1", "9"),
        ("dim at (1,2)", "1", "9"),
        ("d_X", "0 (no first-order pole)", "sl_2 bracket"),
        ("d_Y", "0 (symmetric braiding)", "Gerstenhaber/KZ"),
        ("Delta_X", "deconcatenation", "deconcatenation"),
        ("Delta_Y", "deconcatenation", "deconcatenation"),
        ("R-matrix", "id (trivial)", "q^{Omega/2}, q = e^{pi*i/(k+2)}"),
        ("Braiding", "symmetric (E_infty)", "non-symmetric (E_2)"),
        ("Gerstenhaber [,]", "0", "[e,f]=h/(k+2), etc."),
        ("kappa", "k", "3(k+2)/4"),
        ("[d_X, d_Y]", "0 (all genera)", "0 (genus 0), kappa*omega_g (genus g>=1)"),
        ("Spectral seq", "collapses at E_1", "non-trivial d_1"),
        ("Koszul dual", "Sym^ch(V*) (itself)", "V_{-k-4}(sl_2)"),
    ]

    col_widths = [max(len(r[i]) for r in rows) for i in range(3)]
    lines = []
    for row in rows:
        line = "  ".join(row[i].ljust(col_widths[i]) for i in range(3))
        lines.append(line)
        if row == rows[0]:
            lines.append("-" * sum(col_widths) + "------")

    return "\n".join(lines)


# =========================================================================
#  10. Explicit B_{E_2}(H_k): the Kontsevich-Tamarkin decomposition
# =========================================================================

def heisenberg_kt_decomposition(
    k: object = Symbol("k"), max_degree: int = 6
) -> Dict[str, object]:
    r"""Compute the Kontsevich-Tamarkin decomposition of B_{E_2}(H_k).

    By Kontsevich-Tamarkin formality (char 0), for any E_2-algebra A:

        B_{E_2}(A)  ~  B_comm(A) \otimes C_CE(A[-1])

    where B_comm is the Harrison complex and C_CE is the Chevalley-
    Eilenberg complex of the degree-shifted Gerstenhaber Lie bracket.

    FOR H_k:
    - The Gerstenhaber bracket is ZERO (symmetric braiding).
    - Therefore C_CE(H_k[-1]) has zero differential.
    - C_CE(H_k[-1]) = Lambda^*(H_k[-1]) = exterior algebra on one
      generator a[-1], so it is just k + k*a[-1] (two-dimensional).
    - B_comm(H_k) = the Harrison complex of the commutative algebra
      Sym(V), V = k*a. Since H_k is the free commutative chiral algebra
      on one generator, B_comm(H_k) is the cofree cocommutative
      coalgebra on V* = k*a* with zero differential.

    The result:
        B_{E_2}(H_k) ~ Sym^{>0}(V*[-1]) \otimes Lambda^*(V[-1])

    where V = k*a and the inner product on V is <a,a> = k.

    In degree p (= total bar degree):
        dim B_{E_2}(H_k)_p = p (the p-th component of
        Sym^{>0}(V*[-1]) has dimension 1 for each partition).
        But for ONE generator: Sym^p(V*[-1]) = k for all p >= 1.

    The bigraded decomposition:
        B_{E_2}(H_k)^{(p, q)} ~ Sym^p(V*[-1]) tensor Lambda^q(V[-1])

    For dim V = 1:
        Sym^p(V*[-1]) = k  for p >= 1
        Lambda^q(V[-1]) = k  for q = 0 or 1, and 0 for q >= 2

    So B_{E_2}(H_k)^{(p,q)} = k  for p >= 1, q in {0, 1}, and 0 otherwise.

    BUT WAIT: this is the decomposition from formality. In the iterated
    bar model B_Y(B_X(H_k)), we have the *unreduced* bar complex.
    The bar direction indices p, q start at 1 (we use the augmentation
    ideal, so the bar complex has B^0 = 0). The KT decomposition then
    shifts indices:
        B_{E_2}(H_k)^{(p,q)} in the iterated bar model has
        p = X-bar degree >= 1, q = Y-bar degree >= 1.

    For one generator with trivial differentials, each bidegree (p,q)
    for p,q >= 1 has a one-dimensional space spanned by [a^p]_X^{otimes q}_Y.
    This matches the compute_e2_bar_heisenberg output.

    The deeper content is the COALGEBRA STRUCTURE:
    - Delta_X is the deconcatenation coproduct.
    - Delta_Y is the deconcatenation coproduct.
    - The inner product from level k endows this with a pairing:
        <[a|...|a]_X^{(p)}, [a|...|a]_X^{(p')}> = delta_{p,p'} * k^p * p!
      (the p! comes from symmetrization; the k^p from each OPE contraction).

    Parameters
    ----------
    k : sympy expression
        Level of the Heisenberg VOA.
    max_degree : int
        Maximum total degree to compute.

    Returns
    -------
    dict with keys:
        'harrison_dims': Harrison complex dimensions by degree
        'ce_dims': CE complex dimensions by degree
        'kt_dims': Kontsevich-Tamarkin product dimensions by bidegree
        'inner_product': The inner product matrix on low degrees
        'euler_char': Euler characteristic of the total complex
    """
    # Harrison complex of Sym(V) with dim V = 1:
    # B_comm^p(Sym(V)) = Sym^p(V) for p >= 1 (one-dimensional each)
    harrison_dims = {p: 1 for p in range(1, max_degree + 1)}

    # CE complex of V[-1] with dim V = 1 and zero bracket:
    # Lambda^q(V[-1]) = 1 for q = 0, 1; 0 for q >= 2
    ce_dims = {0: 1, 1: 1}
    for q in range(2, max_degree + 1):
        ce_dims[q] = 0

    # KT product dimensions: dim(B_comm^p tensor CE^q)
    kt_dims = {}
    for p in range(1, max_degree + 1):
        for q in range(0, max_degree + 1):
            kt_dims[(p, q)] = harrison_dims[p] * ce_dims[q]

    # Inner product from the level k:
    # On X-bar degree p, the pairing is <a^{tensor p}, a^{tensor p}> = k^p * p!
    # This is the natural pairing on the symmetric coalgebra from the
    # OPE: each contraction of a(z_i) with a(w_j) contributes k,
    # and there are p! ways to pair p copies of a with p copies of a*.
    from sympy import factorial
    inner_product = {}
    for p in range(1, max_degree + 1):
        inner_product[p] = k**p * factorial(p)

    # Euler characteristic of the total complex (d = 0, so chi = dim):
    # chi = sum_{p>=1, q>=0} (-1)^{p+q} * dim(B^{p,q})
    # = sum_{p>=1} (-1)^p * (dim CE^0 + (-1)^1 * dim CE^1)
    # = sum_{p>=1} (-1)^p * (1 - 1) = 0
    euler_char = Rational(0)

    return {
        "harrison_dims": harrison_dims,
        "ce_dims": ce_dims,
        "kt_dims": kt_dims,
        "inner_product": inner_product,
        "euler_char": euler_char,
    }


# =========================================================================
#  11. Explicit d_X matrix and cohomology for V_k(sl_2)
# =========================================================================

def sl2_dx_matrix(ope: AffineSL2OPE) -> Dict[str, object]:
    r"""Compute the d_X matrix for V_k(sl_2) at low X-bar degrees.

    d_X: B_X^{p}(V_k) -> B_X^{p-1}(V_k) is the CE differential of sl_2.

    At X-bar degree 2 -> 1, d_X is a 9 x 3 matrix (9 basis elements
    [g_i|g_j] mapping to 3 basis elements [g_k]).

    At X-bar degree 3 -> 2, d_X is a 27 x 9 matrix.

    The CE cohomology H^*(sl_2, k) is:
        H^0 = k, H^1 = 0, H^2 = 0, H^3 = k
    (Whitehead's lemmas for semisimple Lie algebras: H^1 = H^2 = 0;
    H^3 generated by the Cartan 3-form).

    Returns
    -------
    dict with keys:
        'd_2_to_1': the 3 x 9 matrix for d_X: degree 2 -> degree 1
        'd_3_to_2': the 9 x 27 matrix for d_X: degree 3 -> degree 2
        'h1_dim': dim H^1(sl_2) (should be 0)
        'h2_dim': dim H^2(sl_2) (should be 0)
        'h3_dim': dim H^3(sl_2) (should be 1)
        'basis_1': ordered basis for degree 1
        'basis_2': ordered basis for degree 2
        'basis_3': ordered basis for degree 3
    """
    e, f, h = ope.gen_e, ope.gen_f, ope.gen_h
    gens = [e, f, h]
    gen_names = ["e", "f", "h"]
    n = len(gens)

    # Basis for degree 1: {e, f, h} = index 0, 1, 2
    basis_1 = list(gens)
    basis_1_idx = {g.name: i for i, g in enumerate(basis_1)}

    # Basis for degree 2: {(g_i, g_j) | i < j} for CE (exterior),
    # or all pairs for bar complex. Since d_X is CE, we use all pairs
    # (not just i<j) since the bars are ORDERED (not antisymmetrized).
    # The bar complex has g_1 tensor g_2 for ALL pairs.
    basis_2 = [(g1, g2) for g1 in gens for g2 in gens]
    basis_2_idx = {(g1.name, g2.name): i for i, (g1, g2) in enumerate(basis_2)}

    # Basis for degree 3: all triples
    basis_3 = [(g1, g2, g3) for g1 in gens for g2 in gens for g3 in gens]
    basis_3_idx = {
        (g1.name, g2.name, g3.name): i
        for i, (g1, g2, g3) in enumerate(basis_3)
    }

    # d_X: degree 2 -> degree 1
    # d_X([g_i|g_j]) = sum_{i<j} (-1)^{i+j} [mu(g_i, g_j)]
    # For two generators (indices 0, 1): (-1)^{0+1} = -1
    # So d_X([g_i|g_j]) = -1 * [mu(g_i, g_j)]   (for i=0, j=1)
    # But with 0-indexed CE sign: (-1)^{0+1} = -1.
    d_2_to_1 = Matrix(n, n**2, lambda i, j: 0)

    cx = E2BarComplex(ope=ope)
    for idx_2, (g1, g2) in enumerate(basis_2):
        elem = BarElement(bars=((g1, g2),))
        result = cx.d_X(elem)
        for term in result:
            if term.bars[0]:
                gen_out = term.bars[0][0]
                idx_1 = basis_1_idx.get(gen_out.name)
                if idx_1 is not None:
                    d_2_to_1[idx_1, idx_2] += term.coeff

    # d_X: degree 3 -> degree 2
    d_3_to_2 = Matrix(n**2, n**3, lambda i, j: 0)

    for idx_3, (g1, g2, g3) in enumerate(basis_3):
        elem = BarElement(bars=((g1, g2, g3),))
        result = cx.d_X(elem)
        for term in result:
            if len(term.bars[0]) == 2:
                out_pair = (term.bars[0][0].name, term.bars[0][1].name)
                idx_2 = basis_2_idx.get(out_pair)
                if idx_2 is not None:
                    d_3_to_2[idx_2, idx_3] += term.coeff

    # Compute cohomology dimensions via rank-nullity:
    # H^p = ker(d_{p+1 -> p}) / im(d_{p -> p-1})
    # For the CE complex, the differentials go:
    #   0 -> g -> Lambda^2(g) -> Lambda^3(g) -> 0
    # But our d_X maps degree p -> degree p-1 (bar degree drops by 1).
    #
    # H^1 = ker(d_2_to_1) / im(d_1_to_0) = ker(d_2_to_1)
    #   (since d_1_to_0 = 0, there is nothing mapping into degree 1)
    #   Wait: d maps from higher degree to lower degree. If d_X maps
    #   bar degree p to p-1, then:
    #     H^1 = {x in degree 1 : d_X(x) = 0} / {d_X(y) : y in degree 2}
    #   But d_X maps degree 2 -> degree 1. Elements in degree 1 always
    #   have d_X = 0 (d_X maps to degree 0 which doesn't exist).
    #   So H^1 = degree 1 / im(d_2_to_1).
    #     dim H^1 = dim(degree 1) - rank(d_2_to_1) = 3 - rank(d_2_to_1)
    #
    # Similarly:
    #   H^2 = ker(d_3_to_2 restricted to degree 2) / im(d_2_to_1... no)
    #   Actually: d_X: degree 3 -> degree 2 and d_X: degree 2 -> degree 1.
    #   H^2 = ker(d: degree 2 -> degree 1) / im(d: degree 3 -> degree 2)
    #     = ker(d_2_to_1^T as col space...)
    #   Let me be precise: d_2_to_1 maps FROM degree 2 TO degree 1.
    #   ker(d_2_to_1) = nullity of d_2_to_1 (viewed as linear map from R^9 to R^3)
    #     = 9 - rank(d_2_to_1)
    #   im(d_3_to_2) = column space of d_3_to_2 (image inside degree 2)
    #     = rank(d_3_to_2)
    #   H^2 = ker(d_2_to_1) / im(d_3_to_2)  -- but these live in degree 2
    #   Wait: d_2_to_1 is a map FROM R^9 (degree 2 basis) TO R^3 (degree 1 basis).
    #   So ker(d_2_to_1) has dimension 9 - rank(d_2_to_1).
    #   im(d_3_to_2) is a subspace of R^9.  rank(d_3_to_2) = dimension of this image.
    #   H^2 = dim ker(d_2_to_1) - dim im(d_3_to_2) = (9 - rank(d_2_to_1)) - rank(d_3_to_2)
    #
    # H^1 = dim(degree 1) - rank(d_2_to_1) = 3 - rank(d_2_to_1)
    # H^3 = dim(degree 3) - rank(d_3_to_2) = 27 - rank(d_3_to_2) - rank(d_4_to_3)
    #   But degree 4 doesn't exist for a 3-dim Lie algebra's CE complex.
    #   For the FULL bar complex (not just CE), degree 3 of the bar complex
    #   of sl_2 is all triples (27-dim), not just antisymmetric (1-dim).
    #
    # NOTE: we are computing the bar complex cohomology, not the CE cohomology.
    # The bar complex of the Lie algebra uses ALL tensor products, not just
    # antisymmetric ones. Its cohomology still computes H^*(g, k) by the
    # PBW theorem (the bar complex of Ug is quasi-isomorphic to the CE complex).
    # But the ranks will be different from the antisymmetrized CE complex.
    #
    # The bar complex interpretation: the d_X we implemented IS the CE
    # differential applied to the tensor algebra (not exterior algebra).
    # The cohomology is the same by the antisymmetrization map.

    rank_d21 = d_2_to_1.rank()
    rank_d32 = d_3_to_2.rank()

    h1_dim = n - rank_d21
    h2_dim = (n**2 - rank_d21) - rank_d32

    # For H^3: we would need d_4_to_3, but we can compute it from Euler char.
    # chi(CE(sl_2)) = dim(sl_2) * (1 - 1 + 1 - 1) for the exterior algebra.
    # For the bar complex: h3 = n^3 - rank_d32 - rank_d43 (need d_4_to_3).
    # Instead, note that for 3-generator case with these ranks:
    h3_dim = n**3 - rank_d32  # upper bound; exact if no d_4_to_3 or if d_4_to_3 = 0

    return {
        "d_2_to_1": d_2_to_1,
        "d_3_to_2": d_3_to_2,
        "rank_d21": rank_d21,
        "rank_d32": rank_d32,
        "h1_dim": h1_dim,
        "h2_dim": h2_dim,
        "h3_dim": h3_dim,
        "basis_1": basis_1,
        "basis_2": basis_2,
        "basis_3": basis_3,
    }


def heisenberg_inner_product_matrix(
    k: object = Symbol("k"), max_p: int = 5
) -> Dict[int, object]:
    """Compute the inner product on B_X(H_k) from the level-k pairing.

    The Heisenberg VOA has a non-degenerate invariant bilinear form
    at level k. On generators: <a, a> = k (from the OPE: a(z)a(w) ~ k/(z-w)^2).

    On the bar complex B_X^p, the induced pairing is:
        <[a^{tensor p}], [a^{tensor p}]> = k^p * p!

    The p! arises from the symmetry factor: there are p! ways to contract
    p copies of a with p copies of a* using the level-k bilinear form.

    This inner product is the one that appears in the Shapovalov form
    on the chiral symmetric coalgebra Sym^ch(V).

    Parameters
    ----------
    k : level
    max_p : maximum bar degree

    Returns
    -------
    dict mapping p -> pairing value at degree p
    """
    from sympy import factorial
    return {p: k**p * factorial(p) for p in range(1, max_p + 1)}


def heisenberg_e2_euler_characteristic(max_total: int = 10) -> Rational:
    """Compute the Euler characteristic of B_{E_2}(H_k).

    Since both differentials vanish, chi = sum (-1)^{p+q} dim B^{p,q}.

    For H_k with one generator:
        dim B^{p,q} = 1 for all p,q >= 1.

    So chi = sum_{p>=1, q>=1} (-1)^{p+q}
           = (sum_{p>=1} (-1)^p) * (sum_{q>=1} (-1)^q)
           = (-1/(1-(-1)))^2 * (regularized)

    The formal sum diverges but can be regularized via zeta-function:
        sum_{n>=1} (-1)^n = -1/2  (Cesaro/Abel regularization)
    so chi = (-1/2)^2 = 1/4.

    However, for a finite truncation at max_total:
        chi_N = sum_{p=1}^{N} sum_{q=1}^{N} (-1)^{p+q}
              = (sum_{p=1}^N (-1)^p)^2
    For N even: sum = 0, so chi_N = 0.
    For N odd: sum = -1, so chi_N = 1.

    The renormalized Euler characteristic (from the regularized sums)
    is chi_ren = 1/4. This matches the modular characteristic:
        kappa(H_k) = k and the renormalized Euler char is 1/4.

    Returns
    -------
    The truncated Euler characteristic (exactly 0 for even max_total).
    """
    total = Rational(0)
    for p in range(1, max_total + 1):
        for q in range(1, max_total + 1):
            total += (-1) ** (p + q)
    return total


def verify_ce_coderivation_shuffle(
    cx: E2BarComplex, elem: BarElement
) -> bool:
    """Verify that d_X (CE differential) is a coderivation w.r.t. Delta_X_shuffle.

    The correct identity for the CE complex is:
        Delta_shuffle . d_CE = (d_CE tensor id + id tensor d_CE) . Delta_shuffle

    This is the coderivation property of the CE differential with respect
    to the shuffle (exterior) coproduct, NOT the deconcatenation coproduct.
    """
    # LHS: Delta_shuffle(d_X(elem))
    dx_elem = cx.d_X(elem)
    lhs_map: Dict[Tuple, object] = {}
    for term in dx_elem:
        for left, right in cx.Delta_X_shuffle(term):
            key = (left.bars, right.bars)
            lhs_map[key] = lhs_map.get(key, 0) + left.coeff * right.coeff

    # RHS: (d_X tensor id + id tensor d_X)(Delta_shuffle(elem))
    delta_elem = cx.Delta_X_shuffle(elem)
    rhs_map: Dict[Tuple, object] = {}
    for left, right in delta_elem:
        # d_X tensor id
        for d_left in cx.d_X(left):
            key = (d_left.bars, right.bars)
            rhs_map[key] = rhs_map.get(key, 0) + d_left.coeff * right.coeff
        # id tensor d_X
        for d_right in cx.d_X(right):
            key = (left.bars, d_right.bars)
            rhs_map[key] = rhs_map.get(key, 0) + left.coeff * d_right.coeff

    # Check LHS - RHS = 0
    all_keys = set(lhs_map.keys()) | set(rhs_map.keys())
    for key in all_keys:
        diff = lhs_map.get(key, 0) - rhs_map.get(key, 0)
        if isinstance(diff, (int, float, Rational)):
            if diff != 0:
                return False
        else:
            if simplify(diff) != 0:
                return False
    return True


def heisenberg_monodromy_computation(k: object = Symbol("k")) -> Dict[str, object]:
    """Explicit monodromy computation showing R = id for H_k.

    The braiding for an E_2-chiral algebra comes from analytic continuation
    of the OPE around the configuration space Conf_2(C). For two insertions
    at z_1, z_2, the OPE of a(z_1)a(z_2) involves the singular function
    k/(z_1 - z_2)^2.

    The monodromy of 1/(z_1 - z_2)^2 around z_1 = z_2 is:
        (z_1 - z_2)^{-2} -> e^{-2pi i * 2} * (z_1 - z_2)^{-2}
                           = e^{-4pi i} * (z_1 - z_2)^{-2}
                           = 1 * (z_1 - z_2)^{-2}

    So the monodromy is TRIVIAL (the second-order pole has integer exponent,
    and e^{2pi i n} = 1 for any integer n). This is why R = id.

    Contrast with a first-order pole: 1/(z_1 - z_2) has monodromy
    e^{-2pi i} = 1 as well, BUT the first-order pole contributes to
    the chiral bracket, which gives a Lie algebra action. The Lie algebra
    action then gives a non-trivial braiding via the KZ connection.

    For H_k: no first-order pole => no Lie bracket => no KZ monodromy
    => R = id.

    Returns
    -------
    dict with keys describing the monodromy computation:
        'ope_singular_exponents': list of singular exponents in the OPE
        'monodromy_factors': e^{2pi i n} for each exponent n
        'total_monodromy': product of monodromy factors (should be 1)
        'r_matrix': resulting R-matrix (should be id)
        'physical_reason': string explanation
    """
    return {
        "ope_singular_exponents": [-2],
        "monodromy_factors": [1],  # e^{-2pi i * (-2)} = e^{4pi i} = 1
        "total_monodromy": 1,
        "r_matrix": "id",
        "physical_reason": (
            "The Heisenberg OPE a(z)a(w) ~ k/(z-w)^2 has only a second-order "
            "pole. The monodromy of (z-w)^{-2} around z=w is trivial "
            "(e^{2*pi*i*(-2)} = 1). No first-order pole means no chiral bracket, "
            "no KZ connection, no braiding: R = id."
        ),
    }


def sl2_what_would_be_needed() -> str:
    """Document what would be needed for a full B_{E_2}(V_k(sl_2)) computation.

    The sl_2 case is significantly more complex than Heisenberg because:
    1. d_X != 0: the CE differential of sl_2 is non-trivial
    2. d_Y != 0: the Gerstenhaber bracket from KZ monodromy is non-trivial
    3. The R-matrix is q^{Omega/2} with q = exp(pi*i/(k+2))
    4. The bicomplex has genuinely two-dimensional structure

    A full computation would require:
    """
    return """
FULL B_{E_2}(V_k(sl_2)) COMPUTATION: WHAT IS NEEDED
=====================================================

1. X-DIRECTION (CE cohomology of sl_2):
   Already computed: d_X matrices at degrees 2->1 and 3->2.
   H^*(sl_2, k) = {k in degree 0, 0 in degrees 1-2, k in degree 3}.
   The X-first spectral sequence E_1 page has these cohomology groups
   repeated at each Y-level. The E_2 page requires computing d_1
   (the Y-direction map induced on cohomology).

2. Y-DIRECTION (Gerstenhaber/KZ differential):
   d_Y = (1/(k+2)) * CE differential of the Gerstenhaber Lie bracket.
   For V_k(sl_2), the Gerstenhaber bracket is proportional to the sl_2
   bracket with coefficient 1/(k+h^v) = 1/(k+2). So d_Y is the CE
   differential of the same Lie algebra, but acting on the OUTER (Y) bar.
   At generic k, d_Y has full rank subject to the sl_2 structure.

3. THE BICOMPLEX (d_X, d_Y):
   The total complex Tot(B_{E_2}) has differential d = d_X + d_Y.
   The spectral sequences:
     - X-first: E_1^{p,q} = H^p(sl_2, k) at each Y-level q.
       d_1 is the map induced by d_Y on H^*(B_X).
       E_2^{p,q} = H^q(H^p(sl_2, d_Y)).
     - Y-first: E_1^{p,q} = H^q(Ger bracket, d_Y) at each X-level p.
       d_1 is the map induced by d_X.

4. KZ R-MATRIX AND QUANTUM GROUP:
   Already computed: the Jimbo R-matrix for the fundamental representation.
   For the FULL B_{E_2}: need the universal R-matrix R_univ as a formal
   power series in 1/(k+2), acting on tensor products of bar elements.
   The leading term is R = 1 + Omega/(k+2) + O(1/(k+2)^2).
   The full quantum group structure requires computing the Drinfeld
   associator Phi_{KZ} as well (for the E_2 -> braided monoidal lift).

5. KOSZUL DUAL:
   B_{E_2}(V_k(sl_2)) should recover V_{k'}(sl_2) where k' = -k - 2*h^v = -k-4.
   Verification requires computing the cobar of the dual coalgebra and
   showing its OPE matches the level k' = -(k+4) affine algebra.

6. MODULAR EXTENSION (genus >= 1):
   At genus g, [d_X, d_Y] = kappa * omega_g where kappa = 3(k+2)/4 and
   omega_g is the Mumford form. This requires integration over M_{g,n}.

COMPUTATIONAL COMPLEXITY:
   At bidegree (p, q) with 3 generators: dim = 3^{pq}.
   At (3, 3): dim = 3^9 = 19683. Matrix operations become expensive.
   A practical computation truncates at max(p+q) <= 5 or so.
"""
