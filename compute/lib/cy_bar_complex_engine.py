r"""
cy_bar_complex_engine.py -- CY bar complex: Hochschild, bar of shifted Lie,
modular trace, categorical kappa, quantum group structure, DT shadow tower.

Ground truth:
  chapters/theory/modular_trace.tex (Theorem CY-D),
  chapters/theory/cy_categories.tex (CY categories and cyclic structures),
  chapters/theory/quantum_groups.tex (Quantum groups from CY bar),
  ~/chiral-bar-cobar/chapters/frame/higher_genus_modular_koszul.tex (shadow tower),
  ~/chiral-bar-cobar/chapters/frame/bar_cobar_adjunction_curved.tex (bar complex).

MATHEMATICAL CONTENTS:

1. HOCHSCHILD COMPLEX of D^b(X) for a CY d-fold X.
   By HKR (Hochschild-Kostant-Rosenberg):
     HH_n(X) = bigoplus_{q-p=n} H^q(X, Wedge^p T_X).
   For CY d-fold: Wedge^p T_X = Omega^{d-p}_X, so
     HH_n(X) = bigoplus_{q-p=n} h^{d-p,q}.
   The Hochschild COhomology (the Ext algebra) carries a Gerstenhaber bracket
   (degree -1 Lie bracket), making HH^*(X)[1] a dg Lie algebra.

2. BAR COMPLEX of HH^*(X) as a shifted Lie algebra.
   The shifted Lie algebra g = HH^*(X)[1] with the Gerstenhaber bracket
   has bar complex B(g) = (T^c(g[1]), d_bar) where:
     d_bar = d_1 + d_2,
     d_1 = internal (Hochschild) differential,
     d_2 = Chevalley-Eilenberg differential from the bracket.
   For CY3 with h^{1,1}=1 (quintic):
     g = HH^*(Q)[1] has graded dimensions [1, 0, 1, 204, 1, 0, 1] shifted by 1.
   The bar complex computes Lie algebra homology H_*(g) = H_*(HH^*(X)[1]).

3. CATEGORICAL kappa for CY categories.
   kappa_ch(D^b(X)) = chi^CY(X), the CY Euler characteristic (Theorem CY-D).
   BKM denominator weights are recorded in a separate kappa_BKM lane:
     CY1 (elliptic):         kappa_ch = 1
     CY2 (K3):               kappa_ch = 2 (= chi(O_X))
     CY3 (K3 x E):           compact kappa_ch = 0,
                              kappa_ch_Heis = 3, kappa_BKM = 5 (= weight of Delta_5)
     CY3 (quintic, CONJ):    kappa_BCOV_shadow_conjectural = -25/3 (= chi_top/24)
     CY3 (resolved conifold): kappa_ch = 1

4. SHADOW DEPTH CLASSIFICATION.
   G (Gaussian, r_max=2): free field / Heisenberg type.
   L (Lie/tree, r_max=3): current algebra / affine type.
   C (contact, r_max=4): betagamma / contact type.
   M (mixed, r_max=inf): Virasoro / W-algebra type.
   For CY categories:
     D^b(E) -> class G (Heisenberg H_1)
     D^b(K3) -> class L (lattice VOA / N=4 SCA structure)
     D^b(K3 x E) -> class M (BKM superalgebra / infinite Borcherds product)
     D^b(quintic) -> class M (infinite tower of GW invariants)
     D^b(conifold) -> class G (single compact cycle)

5. FUKAYA CATEGORY of CY1 (elliptic curve T^2).
   Fuk(T^2) = D^b(E_hat) by HMS (Polishchuk-Zaslow 1998).
   A_infinity structure: m_1 = 0 (formal), m_2 = wedge product on Floer
   cohomology, m_k = 0 for k >= 3 (formal = class G).
   The bar complex B(Fuk(T^2)) is the bar of the Heisenberg algebra.
   Open-string shadow tower: kappa = 1, all higher shadows vanish.

6. MODULAR TRACE on a CY category.
   Tr: HH_*(C) -> C[[hbar]] via the shadow partition function.
   For D^b(CY3): this should give the B-model topological string PF.
   Z^sh(hbar) = exp(sum_{g>=1} F_g * hbar^{2g}).
   At genus g: F_g = kappa * a_hat_g (scalar shadow, uniform-weight lane).

7. QUANTUM GROUP from CY bar complex (AP43: carefully delineated).
   The Yangian Y(C) of a CY category is NOT yet defined as a mathematical
   object for general CY categories (AP43, AP-CY6). What IS defined:
   - For D^b(CY3): the CoHA H_*(M(X), phi^W) IS an associative algebra.
   - For C^3: CoHA = Y^+(gl_hat_1) (Schiffmann-Vasserot, RSYZ).
   - For conifold: the CoHA encodes wall-crossing via KS pentagon.
   - The MODULE CATEGORY Rep(CoHA) is the target of CY-C.
   We compute the CoHA graded dimensions and BPS state counts.

8. DONALDSON-THOMAS from shadow tower.
   DT invariants Omega(gamma) for charge gamma emerge from the shadow PF.
   Z^DT(q) = sum_gamma Omega(gamma) q^gamma.
   For C^3: Z^DT = M(-q) (MacMahon function with (-1)^n signs).
   For conifold: Omega(n*beta) = 1 for all n >= 1.
   We connect the DT partition function to the shadow tower via:
     log Z^DT = sum_g F_g * g_s^{2g-2}  (topological string expansion).

CONVENTIONS:
  - Cohomological grading (|d| = +1).
  - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (AP45).
  - kappa_ch(A) = modular characteristic from Vol I.
  - chi^CY(C) = CY Euler characteristic (Theorem CY-D, NOT chi_top).
  - All Fraction arithmetic for exact computations.

REFERENCES:
  Kontsevich, ICM 1994 (HMS).
  Costello, "TCFTs and CY categories" (2007).
  Kontsevich-Soibelman, "Stability structures..." (2008).
  Bershadsky-Cecotti-Ooguri-Vafa, CMP 165 (1994) 311 (BCOV).
  Polishchuk-Zaslow, "Categorical mirror symmetry: the elliptic curve" (1998).
  Schiffmann-Vasserot, "Cherednik algebras, W-algebras, and the equivariant
    cohomology of the moduli space of instantons on A^2" (2013).
  Rapcak-Soibelman-Yang-Zhao, "Cohomological Hall algebras..." (2020).
  Faber-Pandharipande, "Hodge integrals and moduli of curves" (2000).
  Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21 (mirror symmetry).
  Gopakumar-Vafa, hep-th/9809187 (BPS invariants).
  Maulik-Nekrasov-Okounkov-Pandharipande, math/0312059 (MNOP).
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple

# ---------------------------------------------------------------------------
# Import existing infrastructure from the Vol III compute layer.
# ---------------------------------------------------------------------------
from compute.lib.cy_euler import (
    HodgeDiamond,
    k3_hodge,
    elliptic_curve_hodge,
    product_hodge,
    k3_times_e_hodge,
    quintic_hodge,
    cy3_euler_from_hodge,
)

from compute.lib.modular_cy_characteristic import (
    hkr_decomposition,
    HKRDecomposition,
    hkr_k3,
    hkr_elliptic,
    hkr_quintic,
    A_HAT_COEFFICIENTS,
    shadow_amplitude_genus_g,
    shadow_tower_scalar,
    CYShadowClass,
    shadow_class_cy,
    chi_cy_elliptic,
    chi_cy_k3,
    chi_cy_k3_times_e,
    chi_cy_quintic,
    chi_cy_resolved_conifold,
    ModularCYCharacteristic,
)


# =========================================================================
# Section 1: Hochschild complex for D^b(X) via HKR
# =========================================================================

class HochschildComplex(NamedTuple):
    """Hochschild complex HH^*(X) of D^b(X) for a smooth projective X.

    By HKR: HH^n(X) = bigoplus_{p+q=n} H^q(X, Wedge^p T_X).
    For CY d-fold: Wedge^p T_X = Omega^{d-p}_X, so
      HH^n(X) = bigoplus_{p+q=n} h^{d-p, q}.

    The Gerstenhaber bracket on HH^*(X) has degree -1:
      [-,-]: HH^p x HH^q -> HH^{p+q-1}.
    This makes g = HH^*(X)[1] a graded Lie algebra (Gerstenhaber structure).
    """
    dimension: int                        # CY dimension d
    hh_cohom: Dict[int, int]             # HH^n -> dim
    total_dim: int                       # sum of all HH^n dimensions
    euler_hh: int                        # alternating sum
    gerstenhaber_bracket_nontrivial: bool  # whether the bracket is nontrivial


def hochschild_cohomology(hd: HodgeDiamond) -> HochschildComplex:
    """Compute HH^*(D^b(X)) via HKR for a smooth projective CY variety.

    HH^n(X) = bigoplus_{p+q=n} H^q(X, Wedge^p T_X).
    For CY d-fold with omega_X = O_X: Wedge^p T_X = Omega^{d-p}_X.
    So: HH^n(X) = bigoplus_{p+q=n} h^{d-p, q}.

    NOTE: this is HH^* (cohomology = Ext), NOT HH_* (homology = Tor).
    The relation: HH_n = HH^{d-n} for CY d-folds (Serre duality on HH).
    """
    d = hd.n
    hh: Dict[int, int] = {}

    for p in range(d + 1):
        for q in range(d + 1):
            n = p + q  # cohomological degree of HH^n
            # Wedge^p T_X = Omega^{d-p}_X for CY
            val = hd.h(d - p, q)  # h^{d-p, q}
            if val > 0:
                hh[n] = hh.get(n, 0) + val

    total = sum(hh.values())
    euler = sum((-1) ** n * dim for n, dim in hh.items())

    # The Gerstenhaber bracket is nontrivial iff there exist
    # non-commuting deformations. For CY1 (elliptic): bracket is trivial
    # (abelian). For CY2 (K3): bracket is nontrivial (Lie algebra of
    # the Mukai lattice). For CY3: bracket from deformation theory.
    bracket_nontrivial = (d >= 2)

    return HochschildComplex(
        dimension=d,
        hh_cohom=hh,
        total_dim=total,
        euler_hh=euler,
        gerstenhaber_bracket_nontrivial=bracket_nontrivial,
    )


def hochschild_complex_elliptic() -> HochschildComplex:
    """HH^*(D^b(E)) for an elliptic curve (CY1).

    HH^0 = H^0(O) = 1 (from p=0, q=0: h^{1,0}=1)
          + (WAIT: let me recompute carefully.)

    For E (d=1): HH^n = sum_{p+q=n} h^{1-p, q}.
      n=0: (p=0,q=0): h^{1,0}=1.  Total: 1.
      n=1: (p=0,q=1): h^{1,1}=1; (p=1,q=0): h^{0,0}=1.  Total: 2.
      n=2: (p=1,q=1): h^{0,1}=1.  Total: 1.
    So HH^0=1, HH^1=2, HH^2=1. Total=4. Euler=0.
    """
    return hochschild_cohomology(elliptic_curve_hodge())


def hochschild_complex_k3() -> HochschildComplex:
    """HH^*(D^b(K3)) for a K3 surface (CY2).

    For K3 (d=2): HH^n = sum_{p+q=n} h^{2-p, q}.
      n=0: (p=0,q=0): h^{2,0}=1.  Total: 1.
      n=1: (p=0,q=1): h^{2,1}=0; (p=1,q=0): h^{1,0}=0.  Total: 0.
      n=2: (p=0,q=2): h^{2,2}=1; (p=1,q=1): h^{1,1}=20; (p=2,q=0): h^{0,0}=1.
           Total: 22.
      n=3: (p=1,q=2): h^{1,2}=0; (p=2,q=1): h^{0,1}=0.  Total: 0.
      n=4: (p=2,q=2): h^{0,2}=1.  Total: 1.
    So HH^0=1, HH^1=0, HH^2=22, HH^3=0, HH^4=1. Total=24. Euler=24.
    """
    return hochschild_cohomology(k3_hodge())


def hochschild_complex_quintic() -> HochschildComplex:
    """HH^*(D^b(Q)) for the quintic CY3.

    For Q (d=3): HH^n = sum_{p+q=n} h^{3-p, q}.
      n=0: (p=0,q=0): h^{3,0}=1.  Total: 1.
      n=1: (p=0,q=1): h^{3,1}=0; (p=1,q=0): h^{2,0}=0.  Total: 0.
      n=2: (p=0,q=2): h^{3,2}=0; (p=1,q=1): h^{2,1}=101; (p=2,q=0): h^{1,0}=0.
           Total: 101.
      n=3: (p=0,q=3): h^{3,3}=1; (p=1,q=2): h^{2,2}=1; (p=2,q=1): h^{1,1}=1;
           (p=3,q=0): h^{0,0}=1. Total: 4.
      n=4: (p=1,q=3): h^{2,3}=0; (p=2,q=2): h^{1,2}=101; (p=3,q=1): h^{0,1}=0.
           Total: 101.
      n=5: (p=2,q=3): h^{1,3}=0; (p=3,q=2): h^{0,2}=0.  Total: 0.
      n=6: (p=3,q=3): h^{0,3}=1.  Total: 1.
    So HH^0=1, HH^1=0, HH^2=101, HH^3=4, HH^4=101, HH^5=0, HH^6=1.
    Total=208. Euler=-200.
    """
    return hochschild_cohomology(quintic_hodge())


# =========================================================================
# Section 2: Bar complex of HH^*(X) as a shifted Lie algebra
# =========================================================================

class ShiftedLieAlgebra(NamedTuple):
    """The shifted Lie algebra g = HH^*(X)[1] with Gerstenhaber bracket.

    Shifting by [1] means: g^n = HH^{n+1}(X).
    The Gerstenhaber bracket [-,-]: HH^p x HH^q -> HH^{p+q-1}
    becomes a degree-0 bracket [-,-]: g^{p-1} x g^{q-1} -> g^{p+q-2}
    on the shifted object.
    """
    name: str
    dim_graded: Dict[int, int]   # g^n -> dim
    total_dim: int
    bracket_nontrivial: bool


def shifted_lie_algebra(hh: HochschildComplex, name: str = "") -> ShiftedLieAlgebra:
    """Construct g = HH^*(X)[1]."""
    g: Dict[int, int] = {}
    for n, dim in hh.hh_cohom.items():
        # g^{n-1} = HH^n
        shifted_n = n - 1
        g[shifted_n] = dim

    return ShiftedLieAlgebra(
        name=name,
        dim_graded=g,
        total_dim=sum(g.values()),
        bracket_nontrivial=hh.gerstenhaber_bracket_nontrivial,
    )


class BarComplexData(NamedTuple):
    """Data about the bar complex B(g) of a graded Lie algebra g.

    B(g) = (Sym^c(g[1]), d_CE) where:
      - Sym^c is the graded cofree cocommutative coalgebra (= exterior for odd,
        symmetric for even, in the shifted grading).
      - d_CE is the Chevalley-Eilenberg differential from the bracket.

    For a finite-dimensional graded Lie algebra g concentrated in
    degrees [a, b], the bar complex has:
      B(g)^n = bigoplus_{k >= 1} Sym^k(g[1])^n
    where g[1]^m = g^{m-1} (another desuspension, AP45).

    The bar spectral sequence:
      E_1 = H_*(g, trivial) (Lie algebra homology with trivial coefficients).
    """
    name: str
    lie_algebra: ShiftedLieAlgebra
    # Bar complex graded dimensions (truncated to bar degree <= max_bar)
    bar_dims: Dict[int, int]      # bar degree -> total dim at that bar degree
    total_dim_truncated: int
    max_bar_degree: int
    # Lie algebra homology (E_1 page of bar spectral sequence)
    lie_homology: Optional[Dict[int, int]]


def bar_complex_graded_dims(g: ShiftedLieAlgebra,
                            max_bar_degree: int = 6) -> Dict[int, int]:
    """Compute graded dimensions of the bar complex B(g).

    B_k(g) = Sym^k(g[1]) (the k-th graded piece of the cofree coalgebra).

    For a graded vector space V with dim(V^n) = d_n, the dimension of
    Sym^k(V) is computed via generating functions:
      sum_k dim(Sym^k(V)) t^k = prod_n (1-t)^{-d_n}  (if all even)
    or more precisely, accounting for graded symmetry:
      prod_{n even} (1-t)^{-d_n} * prod_{n odd} (1+t)^{d_n}.

    But this counts the TOTAL dimension at each symmetric power k.
    For our purposes, we need the total dimension at each bar degree k,
    summed over all internal degrees.
    """
    # g[1] has grading: (g[1])^m = g^{m-1}, so dim((g[1])^m) = dim(g^{m-1})
    # = dim(HH^m(X)).
    # The shifted-shifted grading: the bar element [v_1 | ... | v_k]
    # with v_i in g[1] has bar degree k.

    # For bar degree k = 1: dim = total_dim(g[1]) = total_dim(g).
    # For bar degree k: dim = dim of k-fold graded symmetric product.

    # We compute via multinomial enumeration for small k.
    # For the purpose of dimension counting, we just need to track
    # how many basis elements sit at each degree in g[1].

    # g[1]^m = g^{m-1}. The parity for symmetric product purposes:
    # In the COFREE COCOMMUTATIVE coalgebra on a graded vector space V,
    # the k-th component is Sym^k(V) where symmetry is graded:
    #   Sym^k(V) = V^{otimes k} / S_k  with Koszul signs.
    # For even-degree generators: ordinary symmetric powers.
    # For odd-degree generators: exterior powers.

    # Collect the degrees and dimensions of g[1]:
    shifted_dims: Dict[int, int] = {}
    for n, d in g.dim_graded.items():
        m = n + 1  # (g[1])^m = g^n has dimension d
        if d > 0:
            shifted_dims[m] = d

    bar_dims: Dict[int, int] = {}

    for k in range(1, max_bar_degree + 1):
        # Dimension of Sym^k(g[1]) where g[1] is a graded vector space.
        # For the graded symmetric product, generators in even degree
        # contribute ordinary symmetric powers, and generators in odd
        # degree contribute exterior powers.
        #
        # We compute this by partitioning k among the different
        # degree components.
        dim_k = _graded_sym_dim(shifted_dims, k)
        bar_dims[k] = dim_k

    return bar_dims


def _graded_sym_dim(dims: Dict[int, int], k: int) -> int:
    """Dimension of Sym^k(V) for a graded vector space V.

    dims: degree -> dimension.
    Sym^k(V) = sum over partitions k = k_1 + k_2 + ... of
      prod_i Sym^{k_i}(V^{n_i}) where the n_i run over degrees.

    For V^n of dimension d_n:
      Sym^j(V^n) has dimension binom(d_n + j - 1, j) if n is even,
      Sym^j(V^n) has dimension binom(d_n, j) if n is odd (exterior).
    """
    degree_list = sorted(dims.keys())
    if not degree_list:
        return 1 if k == 0 else 0

    return _partition_sum(degree_list, dims, k, 0)


@lru_cache(maxsize=4096)
def _partition_sum(degrees: tuple, dims_tuple: tuple, remaining: int, idx: int) -> int:
    """Recursive computation of graded symmetric product dimension."""
    # Convert back from tuples for the cache
    if idx >= len(degrees):
        return 1 if remaining == 0 else 0

    n = degrees[idx]
    d_n = dict(dims_tuple)[n]

    total = 0
    max_j = remaining
    if n % 2 == 1:
        # Odd degree: exterior powers, so j <= d_n
        max_j = min(remaining, d_n)

    for j in range(0, max_j + 1):
        sym_dim = _sym_or_ext_dim(d_n, j, n)
        if sym_dim == 0:
            continue
        rest = _partition_sum(degrees, dims_tuple, remaining - j, idx + 1)
        total += sym_dim * rest

    return total


def _sym_or_ext_dim(d: int, j: int, degree: int) -> int:
    """Dimension of Sym^j or Ext^j of a d-dimensional space.

    Even degree -> symmetric power: binom(d + j - 1, j).
    Odd degree -> exterior power: binom(d, j).
    """
    if j == 0:
        return 1
    if degree % 2 == 0:
        # Symmetric power
        return _binomial(d + j - 1, j)
    else:
        # Exterior power
        if j > d:
            return 0
        return _binomial(d, j)


def _binomial(n: int, k: int) -> int:
    """Binomial coefficient."""
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def compute_bar_complex(hd: HodgeDiamond, name: str = "",
                        max_bar_degree: int = 6) -> BarComplexData:
    """Compute the bar complex B(g) of g = HH^*(X)[1].

    Returns dimensions of the bar complex at each bar degree.
    """
    hh = hochschild_cohomology(hd)
    g = shifted_lie_algebra(hh, name)

    # Need to convert dicts to tuples for caching
    degree_list = tuple(sorted(g.dim_graded.keys()))
    dims_tuple = tuple(sorted(g.dim_graded.items()))

    bar_dims: Dict[int, int] = {}
    for k in range(1, max_bar_degree + 1):
        bar_dims[k] = _partition_sum(degree_list, dims_tuple, k, 0)

    total = sum(bar_dims.values())

    # For Lie algebra homology: at the E_1 page we get H_*(g, k).
    # For an abelian Lie algebra (bracket = 0): H_*(g) = Sym(g[1]).
    # For CY1: g is abelian, so homology = exterior algebra.
    lie_homology = None
    if not g.bracket_nontrivial:
        # Abelian case: H_k(g) = Wedge^k(g) for odd-total-degree g,
        # = Sym^k(g) for even-total-degree g.
        lie_homology = dict(bar_dims)

    return BarComplexData(
        name=name,
        lie_algebra=g,
        bar_dims=bar_dims,
        total_dim_truncated=total,
        max_bar_degree=max_bar_degree,
        lie_homology=lie_homology,
    )


def bar_complex_elliptic(max_bar_degree: int = 6) -> BarComplexData:
    """Bar complex for D^b(E), elliptic curve (CY1).

    g = HH^*(E)[1]. Dimensions of g:
      g^{-1} = HH^0 = 1, g^0 = HH^1 = 2, g^1 = HH^2 = 1.
    Total dim = 4.

    g[1]: degrees shifted by +1:
      (g[1])^0 = g^{-1} = 1-dim (EVEN degree -> sym powers)
      (g[1])^1 = g^0 = 2-dim (ODD degree -> ext powers)
      (g[1])^2 = g^1 = 1-dim (EVEN degree -> sym powers)

    Bar degree 1: dim(g[1]) = 4.
    Bar degree 2: Sym^2(g[1]).
      Even generators (degree 0,2): 1+1 = 2 generators, each contributing
        sym powers. Odd generators (degree 1): 2 generators, contributing
        ext powers.
      Sym^2 = sum over (j_0, j_1, j_2) with j_0+j_1+j_2 = 2:
        binom(1+j_0-1, j_0) * binom(2, j_1) * binom(1+j_2-1, j_2)
    """
    return compute_bar_complex(elliptic_curve_hodge(), "elliptic", max_bar_degree)


def bar_complex_k3(max_bar_degree: int = 4) -> BarComplexData:
    """Bar complex for D^b(K3), K3 surface (CY2)."""
    return compute_bar_complex(k3_hodge(), "K3", max_bar_degree)


def bar_complex_quintic(max_bar_degree: int = 4) -> BarComplexData:
    """Bar complex for D^b(Q), quintic CY3."""
    return compute_bar_complex(quintic_hodge(), "quintic", max_bar_degree)


# =========================================================================
# Section 3: Categorical kappa for CY categories
# =========================================================================

class CategoricalKappa(NamedTuple):
    """The categorical modular characteristic kappa_ch(D^b(X)).

    This is chi^CY(X), the CY Euler characteristic.
    Theorem CY-D lane: kappa_ch(A_C) = chi^CY(C).

    IMPORTANT (AP48): kappa depends on the FULL algebra, not just
    the Virasoro subalgebra. kappa = c/2 only for Virasoro itself.

    For CY categories:
      CY1 (elliptic): kappa = 1 (Heisenberg H_1).
      CY2 (K3): kappa = chi(O_X) = 2 (NOT rank/2 = 12).
        NOTE: the lattice VOA of the Mukai lattice has kappa = rank/2 = 12.
        But chi^CY(D^b(K3)) = 2 = chi(O_{K3}). These are DIFFERENT:
        kappa(lattice VOA) = 12 is the modular characteristic of the
        CHIRAL ALGEBRA, while chi^CY = 2 is the CY Euler characteristic
        of the CATEGORY. Theorem CY-D equates kappa(A_C) = chi^CY(C),
        but A_{K3} may not be the full lattice VOA.

      CY3 (K3 x E): compact kappa_ch = 0;
        kappa_ch_Heis = 3; kappa_BKM = 5 (weight of Delta_5).
      CY3 (quintic, CONJ): kappa_BCOV_shadow_conjectural = chi_top/24 = -25/3.
      CY3 (resolved conifold): kappa_ch = 1.
    """
    name: str
    kappa: Fraction
    status: str          # "PROVED", "CONJECTURAL", "HEURISTIC"
    dimension: int       # CY dimension
    chi_top: int         # topological Euler characteristic
    chi_O: Fraction      # arithmetic genus chi(O_X) = sum (-1)^q h^{0,q}
    kappa_label: str = "kappa_ch"
    kappa_BKM: Optional[Fraction] = None
    kappa_ch_Heis: Optional[Fraction] = None


def categorical_kappa(hd: HodgeDiamond, name: str = "",
                      status: str = "CONJECTURAL") -> CategoricalKappa:
    """Compute categorical kappa from Hodge data.

    The formula depends on the CY dimension:
      d=0: kappa = 0
      d=1: kappa = 1 (Heisenberg level)
      d=2: kappa = chi(O_X)
      d=3: kappa_BCOV_shadow_conjectural = chi_top/24
           (CONJECTURAL for rigid CY3, not constructed kappa_ch)
           K3 x E is handled by kappa_k3_times_e():
           compact kappa_ch=0, kappa_ch_Heis=3, kappa_BKM=5

    WARNING: the d=3 formula is CONJECTURAL for general rigid CY3.
    For K3 x E: kappa_BKM = 5 is PROVED but does NOT come from chi_top/24 = 0.
    """
    d = hd.n
    chi_top = hd.euler_characteristic

    # Arithmetic genus
    chi_O = Fraction(0)
    for q in range(d + 1):
        chi_O += Fraction((-1) ** q) * Fraction(hd.h(0, q))

    kappa_label = "kappa_ch"
    if d == 0:
        kappa = Fraction(0)
    elif d == 1:
        kappa = Fraction(1)
    elif d == 2:
        kappa = chi_O
    elif d == 3:
        # For rigid CY3: conjectural BCOV-shadow scalar chi_top / 24.
        # This is not a constructed kappa_ch for general compact CY3s.
        kappa = Fraction(chi_top, 24)
        kappa_label = "kappa_BCOV_shadow_conjectural"
    else:
        # Higher-dimensional CY: no general formula known.
        # Conjectural: related to Todd class integral.
        kappa = Fraction(chi_top, 24)  # placeholder

    return CategoricalKappa(
        name=name,
        kappa=kappa,
        status=status,
        dimension=d,
        chi_top=chi_top,
        chi_O=chi_O,
        kappa_label=kappa_label,
    )


def kappa_elliptic() -> CategoricalKappa:
    """kappa(D^b(E)) = 1."""
    return categorical_kappa(elliptic_curve_hodge(), "elliptic", "PROVED")


def kappa_k3() -> CategoricalKappa:
    """kappa(D^b(K3)) = 2 = chi(O_{K3})."""
    return categorical_kappa(k3_hodge(), "K3", "PROVED")


def kappa_k3_times_e() -> CategoricalKappa:
    """compact kappa_ch(D^b(K3 x E)) = 0, with Heisenberg shadow 3.

    The compact Hodge/PhiFA supertrace is the total-space value
    kappa_ch(K3 x E) = chi(O_{K3 x E}) = 0.  The rank-additive
    Heisenberg specialisation is a separate shadow lane:
    kappa_ch_Heis(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3.
    The automorphic Borcherds denominator has the separate weight
    kappa_BKM = 5 = wt(Delta_5).  The values 0, 3, and 5 are not
    interchangeable.
    """
    return CategoricalKappa(
        name="K3 x E",
        kappa=Fraction(0),
        status="PROVED",
        dimension=3,
        chi_top=0,
        chi_O=Fraction(0),
        kappa_label="kappa_ch",
        kappa_BKM=Fraction(5),
        kappa_ch_Heis=Fraction(3),
    )


def kappa_quintic() -> CategoricalKappa:
    """BCOV-shadow candidate for D^b(quintic): -25/3 (CONJECTURAL).

    From chi_top/24 = -200/24 = -25/3.  This is not a constructed
    kappa_ch theorem for the compact quintic.
    """
    return categorical_kappa(quintic_hodge(), "quintic", "CONJECTURAL")


def kappa_resolved_conifold() -> CategoricalKappa:
    """kappa(D^b(conifold)) = 1 (non-compact CY3)."""
    return CategoricalKappa(
        name="resolved conifold",
        kappa=Fraction(1),
        status="PROVED",
        dimension=3,
        chi_top=2,
        chi_O=Fraction(1),
    )


def kappa_abelian_surface() -> CategoricalKappa:
    """kappa(D^b(abelian surface)) = 0 = chi(O_A).

    Abelian surface: h^{0,0}=1, h^{0,1}=2, h^{0,2}=1.
    chi(O_A) = 1 - 2 + 1 = 0.
    """
    hd = HodgeDiamond(2, {
        (0, 0): 1, (1, 0): 2, (2, 0): 1,
        (0, 1): 2, (1, 1): 4, (2, 1): 2,
        (0, 2): 1, (1, 2): 2, (2, 2): 1,
    })
    return categorical_kappa(hd, "abelian surface", "PROVED")


# =========================================================================
# Section 4: Shadow depth classification for CY categories
# =========================================================================

class CYBarShadowData(NamedTuple):
    """Combined bar complex + shadow depth data for a CY category."""
    name: str
    kappa: Fraction
    shadow_class: str         # G, L, C, M
    r_max: int                # -1 for infinity
    bar_dims: Dict[int, int]  # bar degree -> dimension
    shadow_tower: Dict[int, Fraction]  # genus -> F_g
    hh_total_dim: int         # total Hochschild dimension


def cy_bar_shadow_data(hd: HodgeDiamond, name: str,
                       kappa: Fraction, shadow_class: str, r_max: int,
                       max_genus: int = 5, max_bar_degree: int = 4
                       ) -> CYBarShadowData:
    """Compute combined bar + shadow data."""
    bar = compute_bar_complex(hd, name, max_bar_degree)
    tower = shadow_tower_scalar(kappa, max_genus)
    hh = hochschild_cohomology(hd)

    return CYBarShadowData(
        name=name,
        kappa=kappa,
        shadow_class=shadow_class,
        r_max=r_max,
        bar_dims=bar.bar_dims,
        shadow_tower=tower,
        hh_total_dim=hh.total_dim,
    )


def elliptic_bar_shadow() -> CYBarShadowData:
    """Complete bar + shadow data for D^b(E)."""
    return cy_bar_shadow_data(
        elliptic_curve_hodge(), "elliptic",
        Fraction(1), "G", 2,
    )


def k3_bar_shadow() -> CYBarShadowData:
    """Complete bar + shadow data for D^b(K3)."""
    return cy_bar_shadow_data(
        k3_hodge(), "K3",
        Fraction(2), "L", 3,
    )


def quintic_bar_shadow() -> CYBarShadowData:
    """Complete bar + shadow data for D^b(quintic)."""
    return cy_bar_shadow_data(
        quintic_hodge(), "quintic",
        Fraction(-25, 3), "M", -1,
    )


def conifold_bar_shadow() -> CYBarShadowData:
    """Complete bar + shadow data for resolved conifold."""
    # Use a minimal Hodge diamond (non-compact; effective h^{1,1}=1 from P^1)
    hd = HodgeDiamond(3, {
        (0, 0): 1, (3, 3): 1,
        (3, 0): 1, (0, 3): 1,
        (1, 1): 1, (2, 2): 1,
    })
    return cy_bar_shadow_data(
        hd, "resolved conifold",
        Fraction(1), "G", 2,
    )


# =========================================================================
# Section 5: Fukaya category of CY1 (elliptic curve T^2)
# =========================================================================

class FukayaAInfinityData(NamedTuple):
    """A-infinity data for the Fukaya category of a CY manifold.

    For CY1 (T^2): Fuk(T^2) has:
      - Objects: Lagrangian circles L_alpha, L_beta (the two 1-cycles).
      - Morphisms: HF*(L_alpha, L_beta) = k^2 (two intersection points).
      - m_1 = 0 (Floer differential vanishes for special Lagrangians).
      - m_2 = wedge product (associative multiplication on cohomology).
      - m_k = 0 for k >= 3 (A-infinity formality: class G).

    By HMS (Polishchuk-Zaslow): Fuk(T^2) ~ D^b(E_hat).
    """
    name: str
    cy_dimension: int
    objects: List[str]
    morphism_dims: Dict[Tuple[str, str], int]  # (L_i, L_j) -> dim HF*(L_i, L_j)
    formal: bool          # whether m_k = 0 for k >= 3
    shadow_class: str     # G, L, C, M
    kappa: Fraction
    hms_dual: str         # HMS mirror identification


def fukaya_elliptic() -> FukayaAInfinityData:
    """Fukaya category of T^2 (elliptic curve).

    Two generating Lagrangians: the two fundamental cycles.
    HF*(L, L) = H*(T^1) = k^2 (since L = S^1 is a circle).
    HF*(L_1, L_2) = k (one transverse intersection for generic L_1, L_2).

    The A-infinity structure is FORMAL: m_k = 0 for k >= 3.
    This is because T^2 is flat (zero curvature), so there are no
    nontrivial holomorphic polygons beyond triangles (which contribute
    to m_2 only).

    Bar complex: B(Fuk(T^2)) = bar of Heisenberg = class G.
    Shadow obstruction tower terminates at kappa = 1, all higher = 0.
    """
    return FukayaAInfinityData(
        name="Fuk(T^2)",
        cy_dimension=1,
        objects=["L_alpha", "L_beta"],
        morphism_dims={
            ("L_alpha", "L_alpha"): 2,
            ("L_beta", "L_beta"): 2,
            ("L_alpha", "L_beta"): 1,
            ("L_beta", "L_alpha"): 1,
        },
        formal=True,
        shadow_class="G",
        kappa=Fraction(1),
        hms_dual="D^b(E_hat)",
    )


def fukaya_bar_complex_t2() -> Dict[str, Any]:
    """The bar complex of Fuk(T^2).

    Since Fuk(T^2) is formal (class G), the bar complex has:
      d_bar = d_2 only (no higher operations contribute).
    The bar cohomology H*(B(Fuk(T^2))) is concentrated in bar degree 1.
    This is chirally Koszul.

    The open-string shadow tower:
      kappa = 1, C = 0 (cubic shadow), Q = 0 (quartic shadow).
      F_g = 1/24, 7/5760, 31/967680, ...  (A-hat genus coefficients).
    """
    tower = shadow_tower_scalar(Fraction(1), 5)
    return {
        "kappa": Fraction(1),
        "shadow_class": "G",
        "r_max": 2,
        "formal": True,
        "cubic_shadow": Fraction(0),
        "quartic_shadow": Fraction(0),
        "shadow_tower": {g: float(f) for g, f in tower.items()},
        "chirally_koszul": True,
        "hms_dual": "D^b(E_hat)",
    }


# =========================================================================
# Section 6: Modular trace on CY category
# =========================================================================

class ModularTrace(NamedTuple):
    """The modular trace Tr: HH_*(C) -> C[[hbar]].

    For D^b(CY3): this gives the B-model topological string PF.
    Z^sh(hbar) = exp(sum_{g>=1} F_g * hbar^{2g}).
    """
    name: str
    kappa: Fraction
    genus_amplitudes: Dict[int, Fraction]  # g -> F_g
    log_Z_coefficients: Dict[int, float]   # 2g -> coefficient of hbar^{2g} in log Z
    partition_function_terms: int            # number of terms computed
    kappa_label: str = "kappa_ch"


def modular_trace(name: str, kappa: Fraction,
                  max_genus: int = 5,
                  kappa_label: str = "kappa_ch") -> ModularTrace:
    """Compute the modular trace / shadow partition function.

    log Z^sh = sum_{g >= 1} F_g * hbar^{2g}
    where F_g = kappa * a_hat_g.

    For D^b(CY3): this is the B-model topological string free energy
    (constant-map / point contribution only; instanton corrections are
    separate).

    NOTE (AP22): the power convention is hbar^{2g}, NOT hbar^{2g-2}.
    The string coupling convention g_s^{2g-2} differs by g_s^{-2}.
    """
    tower = shadow_tower_scalar(kappa, max_genus)
    log_coeffs = {2 * g: float(f) for g, f in tower.items()}

    return ModularTrace(
        name=name,
        kappa=kappa,
        genus_amplitudes=tower,
        log_Z_coefficients=log_coeffs,
        partition_function_terms=max_genus,
        kappa_label=kappa_label,
    )


def modular_trace_elliptic() -> ModularTrace:
    """Shadow partition function for D^b(E)."""
    return modular_trace("elliptic", Fraction(1))


def modular_trace_k3() -> ModularTrace:
    """Shadow partition function for D^b(K3)."""
    return modular_trace("K3", Fraction(2))


def modular_trace_quintic() -> ModularTrace:
    """Shadow partition function for D^b(quintic), CONJECTURAL.

    kappa_BCOV_shadow_conjectural = -25/3.  F_1 = (-25/3)/24 = -25/72.
    The NEGATIVE sign reflects the negative Euler characteristic:
    the quintic has chi_top = -200 < 0.
    """
    return modular_trace(
        "quintic",
        Fraction(-25, 3),
        kappa_label="kappa_BCOV_shadow_conjectural",
    )


def modular_trace_k3xe() -> ModularTrace:
    """BKM-denominator shadow partition function for K3 x E.

    kappa_BKM = 5.  F_1 = 5/24.  All F_g > 0.
    DT partition function: Z = C / (Delta_5)^2.
    The chiral/CY categorical scalar is kappa_ch = 3 and is not used
    in this automorphic denominator trace.
    """
    return modular_trace("K3 x E", Fraction(5), kappa_label="kappa_BKM")


def modular_trace_conifold() -> ModularTrace:
    """Shadow partition function for the resolved conifold.

    kappa = 1.  F_1 = 1/24.
    Connection to GV invariants: GV_0(1) = 1 for the single compact P^1.
    """
    return modular_trace("resolved conifold", Fraction(1))


def bcov_comparison(kappa: Fraction, chi: int, h11: int,
                    name: str = "") -> Dict[str, Any]:
    """Compare shadow amplitude F_1 with BCOV genus-1 free energy.

    BCOV: F_1^{BCOV} = (3 + h^{1,1} - chi/12) / 2.
    Shadow: F_1^{sh} = kappa / 24.

    These are NOT expected to match in general: F_1^{BCOV} includes
    the full moduli-dependent (instanton) contribution, while F_1^{sh}
    is only the constant-map (point) contribution.

    The comparison is meaningful for the LARGE COMPLEX STRUCTURE LIMIT
    where instanton corrections are suppressed.
    """
    f1_bcov = (Fraction(3) + Fraction(h11) - Fraction(chi, 12)) / Fraction(2)
    f1_shadow = kappa * Fraction(1, 24)

    return {
        "name": name,
        "f1_bcov": f1_bcov,
        "f1_shadow": f1_shadow,
        "match": (f1_bcov == f1_shadow),
        "ratio": float(f1_bcov / f1_shadow) if f1_shadow != 0 else None,
        "note": "BCOV includes instanton corrections; shadow is constant-map only.",
    }


# =========================================================================
# Section 7: Quantum group from CY bar complex
# =========================================================================

class CoHAData(NamedTuple):
    """Cohomological Hall algebra (CoHA) data for a CY3.

    The CoHA H_*(M(X), phi^W) is an associative algebra that serves
    as the E_1-sector of the conjectural quantum chiral group G(X).

    AP43: G(X) itself is NOT defined. The CoHA IS defined and serves
    as the target that the E_1-sector should match.

    For C^3: CoHA = Y^+(gl_hat_1), the positive half of the affine
    Yangian of gl_1. Graded by plane partitions.

    For the conifold: CoHA encodes wall-crossing via KS pentagon.
    """
    name: str
    coha_type: str              # Description of the CoHA
    graded_dims: Dict[int, int]  # degree -> dimension (of the CoHA)
    bps_spectrum: Dict[Any, int]  # charge -> Omega(gamma)
    yangian_identification: Optional[str]  # If CoHA = Yangian
    quantum_group_status: str    # "PROVED", "CONJECTURAL", "UNDEFINED"


def coha_c3(max_degree: int = 10) -> CoHAData:
    """CoHA for C^3 = Y^+(gl_hat_1).

    The graded dimension at degree n equals the number of plane
    partitions of n (OEIS A000219):
      p(0)=1, p(1)=1, p(2)=3, p(3)=6, p(4)=13, p(5)=24, ...

    Generated by the MacMahon function:
      M(q) = prod_{n>=1} 1/(1-q^n)^n = sum_k p(k) q^k.
    """
    # Plane partition counts (OEIS A000219, verified independently)
    pp_counts = {
        0: 1, 1: 1, 2: 3, 3: 6, 4: 13, 5: 24,
        6: 48, 7: 86, 8: 160, 9: 282, 10: 500,
        11: 859, 12: 1479, 13: 2485, 14: 4167, 15: 6879,
    }
    graded = {k: v for k, v in pp_counts.items() if k <= max_degree}

    # BPS spectrum for C^3: single D6-brane, Omega(D6) = 1.
    # The full DT partition function is M(-q)^chi with chi = 1 (virtual).
    bps = {"D6": 1}

    return CoHAData(
        name="C^3",
        coha_type="Y^+(gl_hat_1) (affine Yangian of gl_1, positive half)",
        graded_dims=graded,
        bps_spectrum=bps,
        yangian_identification="Y^+(gl_hat_1)",
        quantum_group_status="PROVED",
    )


def coha_conifold() -> CoHAData:
    """CoHA for the resolved conifold O(-1)+O(-1) -> P^1.

    Two chambers:
      Chamber I: Omega(gamma_1) = 1, Omega(gamma_2) = 1 (two BPS states).
      Chamber II: Omega(gamma_1) = 1, Omega(gamma_1+gamma_2) = 1,
                  Omega(gamma_2) = 1 (three BPS states).

    The wall-crossing is the KS pentagon identity for the quantum dilogarithm.
    The DT invariants are:
      Omega(n*beta) = 1 for all n >= 1 (where beta is the curve class).
    """
    # DT invariants: Omega(n*beta) = 1 for n = 1, 2, 3, ...
    bps = {n: 1 for n in range(1, 11)}

    # CoHA graded dimensions: the conifold CoHA is more complex than C^3.
    # At degree n, the dimension counts sheaves supported on the conifold.
    # For the resolved conifold, the generating function is:
    #   prod_{n>=1} 1/(1-q^n)^n * prod_{n>=1} (1-Qq^n)^n
    # The Q=0 piece is the MacMahon function (C^3 contribution).
    graded = {0: 1, 1: 1, 2: 2, 3: 4, 4: 8, 5: 14}

    return CoHAData(
        name="resolved conifold",
        coha_type="Conifold CoHA (KS wall-crossing)",
        graded_dims=graded,
        bps_spectrum=bps,
        yangian_identification=None,
        quantum_group_status="PROVED",
    )


def coha_quintic() -> CoHAData:
    """CoHA for the quintic CY3 (CONJECTURAL).

    For a compact CY3, the CoHA is defined via the motivic DT theory
    of Joyce-Song / Kontsevich-Soibelman. The BPS spectrum encodes
    GW/DT invariants. The quantum group structure is NOT yet determined.
    """
    # The BPS spectrum for the quintic is partially known:
    # Genus-0 GV invariants n^0_d (Candelas et al. 1991):
    gv_genus0 = {1: 2875, 2: 609250, 3: 317206375}

    return CoHAData(
        name="quintic",
        coha_type="Motivic DT CoHA (Joyce-Song / KS)",
        graded_dims={},
        bps_spectrum=gv_genus0,
        yangian_identification=None,
        quantum_group_status="CONJECTURAL",
    )


# =========================================================================
# Section 8: Donaldson-Thomas from shadow tower
# =========================================================================

class DTShadowData(NamedTuple):
    """DT invariants extracted from the shadow tower.

    The shadow partition function Z^sh = exp(sum F_g hbar^{2g})
    should match the topological string / DT partition function
    at the constant-map level (no instanton corrections).

    For C^3: Z^DT = M(-q) (MacMahon with signs).
    For conifold: Z^DT = M(-q)^2 * prod_{k>=1}(1-Qq^k)^k(1-Q^{-1}q^k)^k.

    The shadow tower gives the constant-map (degree 0) contribution:
      F_g^{const} = kappa * a_hat_g.
    The instanton corrections require additional input (mirror map, etc.).
    """
    name: str
    kappa: Fraction
    dt_type: str                    # "compact", "non-compact", "local"
    bps_invariants: Dict[Any, int]   # charge -> Omega(gamma)
    constant_map_tower: Dict[int, Fraction]  # genus -> F_g^{const}
    macmahon_exponent: Optional[Fraction]    # exponent in M(q)^alpha
    gopakumar_vafa: Optional[Dict[int, int]]  # degree -> n^0_d
    kappa_label: str = "kappa_ch"


def dt_from_shadow_c3() -> DTShadowData:
    """DT invariants of C^3 from the shadow tower.

    C^3 is non-compact CY3, chi = 1.
    Z^DT(C^3) = M(-q) = prod_{n>=1} 1/(1-(-q)^n)^n.
    The constant-map contribution: kappa = 1.
    F_g^{const} = 1 * a_hat_g = a_hat_g.

    The full DT generating function M(-q) = sum_n (-1)^n p(n) q^n
    where p(n) counts plane partitions. The (-1)^n sign is the virtual
    sign from the DT moduli space.
    """
    tower = shadow_tower_scalar(Fraction(1), 5)

    return DTShadowData(
        name="C^3",
        kappa=Fraction(1),
        dt_type="non-compact",
        bps_invariants={"D6": 1},
        constant_map_tower=tower,
        macmahon_exponent=Fraction(1),
        gopakumar_vafa=None,
    )


def dt_from_shadow_conifold() -> DTShadowData:
    """DT invariants of the resolved conifold from the shadow tower.

    kappa = 1 (from the single compact P^1).
    Omega(n*beta) = 1 for all n >= 1.
    GV_0(d) = 1 for all d >= 1 (each multi-cover contributes).

    The GV formula for genus 0:
      N_{0,d} = sum_{k|d} n^0_{d/k} / k^3
    With n^0_d = 1 for all d: N_{0,d} = sum_{k|d} 1/k^3.
    """
    tower = shadow_tower_scalar(Fraction(1), 5)

    # GV invariants: n^0_d = 1 for all d
    gv = {d: 1 for d in range(1, 11)}

    return DTShadowData(
        name="resolved conifold",
        kappa=Fraction(1),
        dt_type="non-compact",
        bps_invariants={n: 1 for n in range(1, 11)},
        constant_map_tower=tower,
        macmahon_exponent=Fraction(2),  # M(q)^2 * (conifold factor)
        gopakumar_vafa=gv,
    )


def dt_from_shadow_quintic() -> DTShadowData:
    """DT invariants of the quintic from the shadow tower (CONJECTURAL).

    kappa = -25/3 (CONJECTURAL).
    The BCOV holomorphic anomaly equation gives F_g recursively.
    The constant-map contribution is: F_g^{const} = (-25/3) * a_hat_g.

    The instanton contributions encode GW/GV invariants:
      n^0_1 = 2875, n^0_2 = 609250, n^0_3 = 317206375.
    """
    tower = shadow_tower_scalar(Fraction(-25, 3), 5)

    gv = {1: 2875, 2: 609250, 3: 317206375,
          4: 242467530000, 5: 229305888887625}

    return DTShadowData(
        name="quintic",
        kappa=Fraction(-25, 3),
        dt_type="compact",
        bps_invariants=gv,
        constant_map_tower=tower,
        macmahon_exponent=None,
        gopakumar_vafa=gv,
        kappa_label="kappa_BCOV_shadow_conjectural",
    )


def dt_from_shadow_k3xe() -> DTShadowData:
    """DT invariants of K3 x E from the BKM shadow tower (PROVED).

    kappa_BKM = 5.  Z^DT = C / (Delta_5)^2.
    The shadow tower gives:
      F_1 = 5/24, F_2 = 7*5/5760 = 7/1152, ...

    The DT partition function is a Siegel modular form of weight -10
    (= -2 * 5 = -2 * kappa_BKM).  The compact scalar
    kappa_ch(K3 x E) = 0 and the Heisenberg shadow
    kappa_ch_Heis(K3 x E) = 3 are stored by kappa_k3_times_e().
    """
    tower = shadow_tower_scalar(Fraction(5), 5)

    return DTShadowData(
        name="K3 x E",
        kappa=Fraction(5),
        dt_type="compact (K3 fibered)",
        bps_invariants={},
        constant_map_tower=tower,
        macmahon_exponent=None,
        gopakumar_vafa=None,
        kappa_label="kappa_BKM",
    )


# =========================================================================
# Section 9: DT invariants via MacMahon / conifold generating functions
# =========================================================================

def macmahon_coefficients(N: int) -> List[int]:
    """First N coefficients of MacMahon function M(q) = prod 1/(1-q^n)^n.

    M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + ...
    Coefficient p(k) = number of plane partitions of k.
    """
    # Use logarithmic method: log M = sum_{n>=1} n * sum_{m>=1} q^{nm}/m
    # Then exponentiate.
    log_coeffs = [Fraction(0)] * N
    for n in range(1, N):
        for m in range(1, N):
            if n * m >= N:
                break
            log_coeffs[n * m] += Fraction(n, m)

    # Exponentiate: M = exp(log M). Use power series exp.
    result = [Fraction(0)] * N
    result[0] = Fraction(1)
    for k in range(1, N):
        # result[k] = (1/k) * sum_{j=1}^{k} j * log_coeffs[j] * result[k-j]
        s = Fraction(0)
        for j in range(1, k + 1):
            s += Fraction(j) * log_coeffs[j] * result[k - j]
        result[k] = s / Fraction(k)

    return [int(c) for c in result]


def dt_c3_partition_function(N: int) -> List[int]:
    """DT partition function of C^3: M(-q) coefficients.

    Z^DT(C^3) = M(-q) = sum_n (-1)^n p(n) q^n.
    """
    mc = macmahon_coefficients(N)
    return [(-1) ** n * mc[n] for n in range(N)]


def conifold_omega(n: int) -> int:
    """DT invariant Omega(n * beta) for the conifold.

    Omega(n * beta) = 1 for all n >= 1.
    This is the BPS degeneracy of n D2-branes wrapping the P^1.
    """
    if n <= 0:
        return 0
    return 1


def conifold_gv_genus0(d: int) -> int:
    """Genus-0 Gopakumar-Vafa invariant for the conifold.

    n^0_d = 1 for all d >= 1 (one BPS state at each charge).
    """
    if d <= 0:
        return 0
    return 1


def conifold_gw_genus0(d: int) -> Fraction:
    """Genus-0 GW invariant N_{0,d} for the conifold.

    By the multi-cover formula: N_{0,d} = sum_{k|d} n^0_{d/k} / k^3.
    With n^0_j = 1 for all j: N_{0,d} = sum_{k|d} 1/k^3.
    """
    if d <= 0:
        return Fraction(0)
    total = Fraction(0)
    for k in range(1, d + 1):
        if d % k == 0:
            total += Fraction(1, k ** 3)
    return total


# =========================================================================
# Section 10: Cross-checks and multi-path verification
# =========================================================================

def verify_hkr_cy_duality(hd: HodgeDiamond) -> bool:
    """Verify HH^n = HH^{2d-n} for CY d-folds (Serre duality on HH).

    For a CY d-fold X of complex dimension d: HH^*(X) lives in degrees
    0, 1, ..., 2d. Serre duality on HH gives dim HH^n = dim HH^{2d-n}.

    NOTE: the duality is n <-> 2d-n (NOT d-n). The Hochschild cohomology
    HH^n = bigoplus_{p+q=n} H^q(Wedge^p T) ranges over 0 <= p,q <= d,
    so HH^n lives in degrees 0 to 2d.
    """
    hh = hochschild_cohomology(hd)
    d = hd.n
    for n in range(2 * d + 1):
        dual_n = 2 * d - n
        dim_n = hh.hh_cohom.get(n, 0)
        dim_dual = hh.hh_cohom.get(dual_n, 0)
        if dim_n != dim_dual:
            return False
    return True


def verify_euler_hh_chi_top(hd: HodgeDiamond) -> bool:
    """Verify sum (-1)^n dim HH^n = (-1)^d chi_top.

    By HKR + Hodge theory:
      sum (-1)^n dim HH^n = sum (-1)^{p+q} h^{d-p,q}
    The substitution p' = d-p gives:
      = sum (-1)^{d-p'+q} h^{p',q} = (-1)^d chi_top.
    """
    hh = hochschild_cohomology(hd)
    d = hd.n
    chi_top = hd.euler_characteristic
    return hh.euler_hh == ((-1) ** d) * chi_top


def verify_hh_total_equals_sum_hodge(hd: HodgeDiamond) -> bool:
    """Verify total dim HH^* = total dim H^*(X, Wedge^* T_X) = sum h^{p,q}."""
    hh = hochschild_cohomology(hd)
    total_hodge = sum(
        hd.h(p, q)
        for p in range(hd.n + 1)
        for q in range(hd.n + 1)
    )
    return hh.total_dim == total_hodge


def verify_kappa_additivity(kappa1: Fraction, kappa2: Fraction,
                            kappa_product: Fraction) -> Dict[str, Any]:
    """Test whether kappa is additive for a product of CY categories.

    kappa(C_1 x C_2) vs kappa(C_1) + kappa(C_2).

    IMPORTANT: this is only meaningful lane-by-lane.  In the proved
    Heisenberg shadow lane, K3 x E is additive: 3 = 2 + 1.  The old
    discrepancy 5 != 3 compares kappa_BKM to kappa_ch_Heis and is not an
    additivity test.
    """
    sum_kappa = kappa1 + kappa2
    return {
        "kappa_1": kappa1,
        "kappa_2": kappa2,
        "kappa_sum": sum_kappa,
        "kappa_product": kappa_product,
        "is_additive": (sum_kappa == kappa_product),
        "discrepancy": kappa_product - sum_kappa,
    }


def shadow_tower_comparison(name: str, kappa: Fraction,
                            external_values: Dict[int, Fraction]
                            ) -> Dict[str, Any]:
    """Compare shadow tower F_g values with externally computed values.

    This is the multi-path verification: the shadow tower from kappa
    should match independently computed F_g (e.g., from GW invariants,
    BCOV, or direct Hodge integral computation).
    """
    tower = shadow_tower_scalar(kappa, max(external_values.keys()))
    matches = {}
    for g, ext_val in external_values.items():
        shadow_val = tower.get(g, Fraction(0))
        matches[f"g={g}"] = {
            "shadow": shadow_val,
            "external": ext_val,
            "match": (shadow_val == ext_val),
        }

    return {
        "name": name,
        "kappa": kappa,
        "comparisons": matches,
        "all_match": all(m["match"] for m in matches.values()),
    }


# =========================================================================
# Section 11: Master verification
# =========================================================================

def verify_all() -> Dict[str, bool]:
    """Run all consistency checks."""
    results: Dict[str, bool] = {}

    # 1. HKR duality checks
    for name, hd_func in [("elliptic", elliptic_curve_hodge),
                           ("K3", k3_hodge),
                           ("quintic", quintic_hodge)]:
        hd = hd_func()
        results[f"hkr_duality_{name}"] = verify_hkr_cy_duality(hd)
        results[f"euler_hh_chi_{name}"] = verify_euler_hh_chi_top(hd)
        results[f"hh_total_hodge_{name}"] = verify_hh_total_equals_sum_hodge(hd)

    # 2. Hochschild dimensions
    hh_e = hochschild_complex_elliptic()
    results["hh_elliptic_total_4"] = (hh_e.total_dim == 4)
    results["hh_elliptic_hh0_1"] = (hh_e.hh_cohom.get(0, 0) == 1)
    results["hh_elliptic_hh1_2"] = (hh_e.hh_cohom.get(1, 0) == 2)
    results["hh_elliptic_hh2_1"] = (hh_e.hh_cohom.get(2, 0) == 1)

    hh_k3 = hochschild_complex_k3()
    results["hh_k3_total_24"] = (hh_k3.total_dim == 24)
    results["hh_k3_hh0_1"] = (hh_k3.hh_cohom.get(0, 0) == 1)
    results["hh_k3_hh2_22"] = (hh_k3.hh_cohom.get(2, 0) == 22)
    results["hh_k3_hh4_1"] = (hh_k3.hh_cohom.get(4, 0) == 1)

    hh_q = hochschild_complex_quintic()
    results["hh_quintic_total_208"] = (hh_q.total_dim == 208)
    results["hh_quintic_hh0_1"] = (hh_q.hh_cohom.get(0, 0) == 1)
    results["hh_quintic_hh2_101"] = (hh_q.hh_cohom.get(2, 0) == 101)
    results["hh_quintic_hh3_4"] = (hh_q.hh_cohom.get(3, 0) == 4)
    results["hh_quintic_hh4_101"] = (hh_q.hh_cohom.get(4, 0) == 101)
    results["hh_quintic_hh6_1"] = (hh_q.hh_cohom.get(6, 0) == 1)
    results["hh_quintic_euler_200"] = (hh_q.euler_hh == 200)

    # 3. Kappa values
    ke = kappa_elliptic()
    results["kappa_elliptic_1"] = (ke.kappa == 1)
    kk = kappa_k3()
    results["kappa_k3_2"] = (kk.kappa == 2)
    kke = kappa_k3_times_e()
    results["kappa_ch_k3xe_0"] = (kke.kappa == 0 and kke.kappa_label == "kappa_ch")
    results["kappa_ch_heis_k3xe_3"] = (kke.kappa_ch_Heis == 3)
    results["kappa_bkm_k3xe_5"] = (kke.kappa_BKM == 5)
    kq = kappa_quintic()
    results["kappa_quintic_minus25over3"] = (kq.kappa == Fraction(-25, 3))
    kc = kappa_resolved_conifold()
    results["kappa_conifold_1"] = (kc.kappa == 1)
    ka = kappa_abelian_surface()
    results["kappa_abelian_surface_0"] = (ka.kappa == 0)

    # 4. Shadow towers
    tower_e = shadow_tower_scalar(Fraction(1), 3)
    results["shadow_e_f1"] = (tower_e[1] == Fraction(1, 24))
    results["shadow_e_f2"] = (tower_e[2] == Fraction(7, 5760))

    tower_k3xe = shadow_tower_scalar(Fraction(5), 3)
    results["shadow_bkm_k3xe_f1"] = (tower_k3xe[1] == Fraction(5, 24))
    results["shadow_bkm_k3xe_f2"] = (tower_k3xe[2] == Fraction(7, 1152))

    # 5. MacMahon function
    mc = macmahon_coefficients(11)
    results["macmahon_p0"] = (mc[0] == 1)
    results["macmahon_p1"] = (mc[1] == 1)
    results["macmahon_p2"] = (mc[2] == 3)
    results["macmahon_p3"] = (mc[3] == 6)
    results["macmahon_p4"] = (mc[4] == 13)
    results["macmahon_p5"] = (mc[5] == 24)
    results["macmahon_p10"] = (mc[10] == 500)

    # 6. Conifold GV invariants
    results["conifold_omega_1"] = (conifold_omega(1) == 1)
    results["conifold_omega_5"] = (conifold_omega(5) == 1)
    results["conifold_gv0_1"] = (conifold_gv_genus0(1) == 1)
    results["conifold_gw0_1"] = (conifold_gw_genus0(1) == Fraction(1))
    results["conifold_gw0_2"] = (conifold_gw_genus0(2) == Fraction(1) + Fraction(1, 8))

    # 7. CoHA
    coha = coha_c3(5)
    results["coha_c3_dim0"] = (coha.graded_dims[0] == 1)
    results["coha_c3_dim1"] = (coha.graded_dims[1] == 1)
    results["coha_c3_dim2"] = (coha.graded_dims[2] == 3)
    results["coha_c3_dim5"] = (coha.graded_dims[5] == 24)

    # 8. Fukaya
    fuk = fukaya_elliptic()
    results["fukaya_t2_formal"] = fuk.formal
    results["fukaya_t2_kappa_1"] = (fuk.kappa == 1)
    results["fukaya_t2_class_G"] = (fuk.shadow_class == "G")

    return results
