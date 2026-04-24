r"""E_3 bar cohomology for class M (Virasoro) at higher genus.

MAIN RESULT (Theorem: Higher-Genus Class M E_3 Bar Cohomology):

  For g independent copies of the Virasoro VOA at c != 0 (class M),
  the E_3 bar spectral sequence gives:

    E_4 = (3t(1+t))^g  (Poincare polynomial)

  Equivalently:
    E_4^n = 3^g * C(g, n-g)      for g <= n <= 2g
    E_4^n = 0                    otherwise

  Total dimension: dim E_4 = 6^g. For g <= 3, degree reasons give
  E_4 = E_inf. For g >= 4, d_5 may act, so E_inf = E_4 is not proved.

  This follows from the Kunneth theorem applied to the d_4 differential,
  which decomposes as a sum of independent per-copy contractions.

COMPARISON BY SHADOW CLASS (at genus g):

  Class G (Heisenberg): E_inf = P(q)^{3g}  (formal, infinite-dim)
  Class L (Yangian):    E_inf = (1+t)^{3g}  (dim = 2^{3g} = 8^g)
  Class C (betagamma):  E_inf = (1+t)^{3g}  (dim = 2^{3g}, d_4 killed by charge)
  Class M (Virasoro):   E_4 = (3t(1+t))^g (dim = 6^g);
                        E_inf is proved equal only for g <= 3

  Deficit: class L dim - class M dim = 8^g - 6^g (exponentially growing).

PROOF STRUCTURE:

The E_3 page at genus g is Lambda*(k^{3g}) with Poincare (1+t)^{3g}.
The algebra decomposes as tensor^g Lambda*(k^3), one per copy.

The d_4 differential decomposes by Leibniz:
  d_4 = sum_{i=1}^g (1 tensor ... tensor d_4^{(i)} tensor ... tensor 1)
where each d_4^{(i)}: Lambda^3(V_i) -> Lambda^0(V_i) is the genus-1
scalar (= 40/(5c+22) at central charge c).

Since the d_4^{(i)} act on independent tensor factors, the Kunneth
theorem (over a field) gives:
  H(tensor^g C_i, sum d_i) = tensor^g H(C_i, d_i)

At genus 1: H(Lambda*(k^3), d_4) = [0, 3, 3, 0] (prop:virasoro-d4).
At genus g: H = tensor^g [0, 3, 3, 0] with Poincare (3t+3t^2)^g.

HIGHER DIFFERENTIALS (d_5 AND BEYOND):

The shadow tower of the Virasoro has S_5 = -16/9, S_6 = 19040/2187, ...
(infinite depth, class M). These induce potentially nonzero d_r on the
E_4 page. However:

  d_r: E_4^n -> E_4^{n-(r-1)}

Since E_4 is supported in degrees [g, 2g] (a band of width g), the
differential d_r can act nontrivially only when both n and n-(r-1) lie
in [g, 2g], requiring r-1 <= g, i.e. r <= g+1. In particular:

  g=1: d_5+ = 0 (support in {1,2}, shift >= 4 exits range)
  g=2: d_5+ = 0 (support in {2,3,4}, shift >= 4 exits range)
  g=3: d_5+ = 0 (support in {3,...,6}, shift >= 4 exits range)
  g>=4: d_5 can potentially act (support width = g+1 >= 5 >= shift 4)

For g=1,2,3: E_4 = E_inf UNCONDITIONALLY (degree reasons, no S_5 dependence).
For g>=4: E_4 may not be E_inf. The spectral sequence terminates at
E_{g+2} at the latest (d_r = 0 for r >= g+2 by degree).

This module computes E_4 for all g (which equals E_inf for g <= 3),
and provides the explicit d_4 rank computation via matrix methods.

CONVENTIONS:
  - Cohomological grading (|d| = +1).
  - kappa_ch = c/2 (AP113: always subscripted).
  - Delta = 8*kappa_ch*S_4 = 40/(5c+22), the d_4 coefficient.
  - Genus g surface: g independent copies of the Virasoro generator.
  - Each copy contributes 3 exterior generators (one per E_3 direction).
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from sympy import Rational


# =========================================================================
# Core class
# =========================================================================


class E3BarHigherGenusClassM:
    r"""E_3 bar spectral sequence for class M (Virasoro) at genus g.

    At genus g, the algebra has g independent copies of the Virasoro
    generator, each contributing 3 exterior generators to the E_3 page.
    The d_4 differential decomposes as a sum of per-copy contractions.

    The Kunneth theorem then gives:
      E_4 = tensor^g [0, 3, 3, 0]
    with Poincare polynomial (3t + 3t^2)^g = (3t(1+t))^g.

    For g <= 3: E_4 = E_inf (higher d_r vanish for degree reasons).
    For g >= 4: E_4 is computed; higher d_r may be nonzero.

    Attributes:
        g: genus (number of independent Virasoro copies)
        c: central charge (default 1)
        N: total number of exterior generators = 3g
        kappa_ch: kappa_ch = c/2 (AP113: subscripted)
        S4: quartic shadow S_4 = 10/(c(5c+22))
        Delta: critical discriminant 8*kappa_ch*S_4 = 40/(5c+22)
    """

    def __init__(self, g: int = 1, c: Rational = Rational(1)):
        """Initialize the higher-genus class M E_3 bar computation.

        Args:
            g: genus (number of independent copies). Must be >= 1.
            c: central charge. Default c=1.
        """
        if g < 1:
            raise ValueError(f"Genus g must be >= 1, got {g}")
        self.g = g
        self.c = Rational(c)
        self.N = 3 * g

        # Shadow data (AP113: kappa always subscripted)
        self.kappa_ch = self.c / 2
        self.S4 = Rational(10) / (self.c * (5 * self.c + 22))
        self.Delta = 8 * self.kappa_ch * self.S4  # = 40/(5c+22)

    @property
    def shadow_class(self) -> str:
        """Virasoro is class M (infinite shadow depth)."""
        return "M"

    # -----------------------------------------------------------------
    # E_3 page: (1+t)^{3g}
    # -----------------------------------------------------------------

    def e3_page(self, n: int) -> int:
        """Dimension of E_3^n = C(3g, n)."""
        if n < 0 or n > self.N:
            return 0
        return comb(self.N, n)

    def e3_poincare(self) -> List[int]:
        """Poincare polynomial of the E_3 page: (1+t)^{3g}."""
        return [self.e3_page(n) for n in range(self.N + 1)]

    def e3_total(self) -> int:
        """Total dimension of the E_3 page: 2^{3g}."""
        return 2 ** self.N

    # -----------------------------------------------------------------
    # d_4 differential: exact computation via matrix rank
    # -----------------------------------------------------------------

    @staticmethod
    def _multi_degrees(g: int, n: int):
        """All tuples (a_1,...,a_g) with 0 <= a_i <= 3, sum = n."""
        if g == 0:
            if n == 0:
                yield ()
            return
        for a in range(min(3, n) + 1):
            for rest in E3BarHigherGenusClassM._multi_degrees(g - 1, n - a):
                yield (a,) + rest

    @staticmethod
    def _block_dim(md: Tuple[int, ...]) -> int:
        """Dimension of the multi-degree block: prod_i C(3, a_i)."""
        d = 1
        for a in md:
            d *= comb(3, a)
        return d

    def d4_rank(self, n: int) -> int:
        """Rank of d_4: Lambda^n(k^{3g}) -> Lambda^{n-3}(k^{3g}).

        Computed by building the explicit matrix representation of d_4
        in the multi-degree basis and computing its rank.

        d_4 = sum_i d_4^{(i)} where d_4^{(i)} contracts the volume
        form of copy i, with Koszul sign (-1)^{sum_{j<i} a_j}.
        """
        tn = n - 3
        if tn < 0 or tn > self.N:
            return 0

        g = self.g

        src_blocks = list(self._multi_degrees(g, n))
        tgt_blocks = list(self._multi_degrees(g, tn))

        # Build offset maps
        src_offset = {}
        off = 0
        for md in src_blocks:
            src_offset[md] = off
            off += self._block_dim(md)
        src_total = off

        tgt_offset = {}
        off = 0
        for md in tgt_blocks:
            tgt_offset[md] = off
            off += self._block_dim(md)
        tgt_total = off

        # Build the d_4 matrix (integer, Delta normalized to 1 for rank)
        mat = np.zeros((tgt_total, src_total), dtype=np.int64)

        for md in src_blocks:
            for i in range(g):
                if md[i] != 3:
                    continue
                # d_4^{(i)}: (a_1,...,3,...,a_g) -> (a_1,...,0,...,a_g)
                md_target = tuple(0 if j == i else md[j] for j in range(g))
                sign = (-1) ** sum(md[j] for j in range(i))
                bd = self._block_dim(md)
                s_off = src_offset[md]
                t_off = tgt_offset[md_target]
                for k in range(bd):
                    mat[t_off + k, s_off + k] += sign

        return int(np.linalg.matrix_rank(mat))

    def d4_ranks_all(self) -> List[int]:
        """Ranks of d_4 at each degree n = 0, ..., 3g."""
        return [self.d4_rank(n) for n in range(self.N + 1)]

    # -----------------------------------------------------------------
    # E_4 page (= E_inf for g <= 3)
    # -----------------------------------------------------------------

    def e4_page_exact(self, n: int) -> int:
        """E_4^n computed from the exact d_4 rank (matrix method).

        E_4^n = ker(d_4: E_3^n -> E_3^{n-3}) / im(d_4: E_3^{n+3} -> E_3^n)
              = (dim E_3^n - rank_out(n)) - rank_in(n)
        where rank_out(n) = rank(d_4 from degree n) and
              rank_in(n)  = rank(d_4 from degree n+3 into degree n).
        """
        ker_dim = self.e3_page(n) - self.d4_rank(n)
        im_dim = self.d4_rank(n + 3) if (n + 3) <= self.N else 0
        return ker_dim - im_dim

    def e4_poincare_exact(self) -> List[int]:
        """E_4 Poincare polynomial from exact matrix computation."""
        return [self.e4_page_exact(n) for n in range(self.N + 1)]

    # -----------------------------------------------------------------
    # E_4 page: closed-form via Kunneth
    # -----------------------------------------------------------------

    def e4_page(self, n: int) -> int:
        """E_4^n from the Kunneth closed form: 3^g * C(g, n-g).

        By the Kunneth theorem:
          E_4 = tensor^g [0, 3, 3, 0]
        Poincare: (3t + 3t^2)^g = 3^g * t^g * (1+t)^g.
        So E_4^n = 3^g * C(g, n-g) for g <= n <= 2g, else 0.
        """
        k = n - self.g
        if k < 0 or k > self.g:
            return 0
        return 3 ** self.g * comb(self.g, k)

    def e4_poincare(self) -> List[int]:
        """E_4 Poincare polynomial from the Kunneth closed form."""
        return [self.e4_page(n) for n in range(self.N + 1)]

    def e4_total(self) -> int:
        """Total dimension of E_4: 6^g."""
        return 6 ** self.g

    # -----------------------------------------------------------------
    # E_inf (whether E_4 = E_inf depends on genus)
    # -----------------------------------------------------------------

    def e4_is_einf(self) -> bool:
        """Whether E_4 = E_inf (degree reasons kill all d_r for r >= 5).

        E_4 is supported in degrees [g, 2g]. The differential d_r maps
        degree n to degree n - (r-1). For d_r to be nonzero on E_4,
        both n and n-(r-1) must lie in [g, 2g], requiring r-1 <= g.
        So d_5 requires g >= 4.

        For g <= 3: E_4 = E_inf unconditionally.
        For g >= 4: E_4 may not equal E_inf.
        """
        return self.g <= 3

    def einf_poincare(self) -> List[int]:
        """E_inf Poincare polynomial.

        For g <= 3: E_inf = E_4 = (3t(1+t))^g (proved).
        For g >= 4: returns E_4 with a caveat (d_5+ may act).
        """
        return self.e4_poincare()

    def einf_total(self) -> int:
        """Total dimension of E_inf.

        For g <= 3: 6^g (proved).
        For g >= 4: at most 6^g (d_5+ may reduce further).
        """
        return self.e4_total()

    # -----------------------------------------------------------------
    # Euler characteristic
    # -----------------------------------------------------------------

    def euler_characteristic_e3(self) -> int:
        """Euler characteristic of E_3: 0."""
        return sum((-1) ** n * self.e3_page(n) for n in range(self.N + 1))

    def euler_characteristic_e4(self) -> int:
        """Euler characteristic of E_4: 0 (preserved by d_4)."""
        return sum((-1) ** n * self.e4_page(n) for n in range(self.N + 1))

    # -----------------------------------------------------------------
    # Poincare duality
    # -----------------------------------------------------------------

    def poincare_duality_holds(self) -> bool:
        """Check E_4^n = E_4^{N-n} (Poincare duality)."""
        poinc = self.e4_poincare()
        N = self.N
        return all(poinc[n] == poinc[N - n] for n in range(N + 1))

    # -----------------------------------------------------------------
    # Comparison with class L
    # -----------------------------------------------------------------

    def class_l_total(self) -> int:
        """Total dimension of class L E_inf at genus g: 2^{3g} = 8^g."""
        return 8 ** self.g

    def deficit(self) -> int:
        """Dimension deficit: class L dim - class M dim = 8^g - 6^g."""
        return self.class_l_total() - self.e4_total()

    def deficit_ratio(self) -> float:
        """Ratio class L / class M = (8/6)^g = (4/3)^g."""
        return (4 / 3) ** self.g

    def compare_with_class_l(self) -> Dict[str, Any]:
        """Full comparison with class L (Yangian/betagamma)."""
        class_l_poinc = [comb(self.N, n) for n in range(self.N + 1)]
        class_m_poinc = self.e4_poincare()
        deficit_per_degree = [
            class_l_poinc[n] - class_m_poinc[n] for n in range(self.N + 1)
        ]
        return {
            "genus": self.g,
            "class_L_poincare": class_l_poinc,
            "class_M_poincare": class_m_poinc,
            "deficit_per_degree": deficit_per_degree,
            "class_L_total": self.class_l_total(),
            "class_M_total": self.e4_total(),
            "deficit_total": self.deficit(),
            "deficit_ratio": self.deficit_ratio(),
        }

    # -----------------------------------------------------------------
    # Higher differential analysis
    # -----------------------------------------------------------------

    def first_possible_higher_differential(self) -> Optional[int]:
        """First r >= 5 where d_r could act on E_4.

        Returns None if no d_r for r >= 5 can act (g <= 3).
        Otherwise returns 5 (the first candidate).
        """
        if self.g <= 3:
            return None
        return 5

    def last_possible_differential(self) -> int:
        """Last r where d_r could act on E_4: r = g + 1.

        d_r maps degree n to n - (r-1). On E_4 supported in [g, 2g],
        the most extreme map is d_{g+1}: E_4^{2g} -> E_4^g.
        For r >= g + 2, the shift r-1 > g exceeds the support width,
        so the target degree falls below g.
        """
        return self.g + 1

    def d5_potential_maps(self) -> List[Tuple[int, int]]:
        """Source/target degree pairs where d_5 could act on E_4.

        d_5: E_4^n -> E_4^{n-4}. Both n and n-4 must be in [g, 2g].
        """
        support = range(self.g, 2 * self.g + 1)
        return [(n, n - 4) for n in support if (n - 4) in support]

    def higher_dr_analysis(self) -> Dict[str, Any]:
        """Analysis of all potentially nonzero d_r for r >= 5."""
        result = {}
        for r in range(5, self.g + 3):
            shift = r - 1
            support = range(self.g, 2 * self.g + 1)
            pairs = [(n, n - shift) for n in support if (n - shift) in support]
            if pairs:
                dims = [
                    (self.e4_page(n), self.e4_page(n - shift))
                    for n, _ in pairs
                ]
                result[r] = {"degree_pairs": pairs, "dimensions": dims}
        return result

    # -----------------------------------------------------------------
    # Full investigation
    # -----------------------------------------------------------------

    def full_investigation(self) -> Dict[str, Any]:
        """Complete investigation of the higher-genus class M computation."""
        return {
            "genus": self.g,
            "central_charge": self.c,
            "shadow_class": self.shadow_class,
            "N": self.N,
            "kappa_ch": self.kappa_ch,
            "S4": self.S4,
            "Delta": self.Delta,
            "e3_poincare": self.e3_poincare(),
            "e3_total": self.e3_total(),
            "e4_poincare": self.e4_poincare(),
            "e4_total": self.e4_total(),
            "e4_is_einf": self.e4_is_einf(),
            "euler_char_e3": self.euler_characteristic_e3(),
            "euler_char_e4": self.euler_characteristic_e4(),
            "poincare_duality": self.poincare_duality_holds(),
            "class_L_comparison": self.compare_with_class_l(),
            "first_possible_higher_diff": self.first_possible_higher_differential(),
            "last_possible_diff": self.last_possible_differential(),
            "higher_dr_analysis": self.higher_dr_analysis(),
            "closed_form": (
                f"E_4 = (3t(1+t))^{self.g}, dim = 6^{self.g} = {self.e4_total()}"
            ),
        }


# =========================================================================
# Standalone functions
# =========================================================================


def class_m_einf_dimension(g: int) -> int:
    """Total E_4 dimension for class M at genus g: 6^g.

    This is also the E_inf dimension for g <= 3 (degree reasons kill d_5+).
    For g >= 4 it is an upper bound unless the higher differentials vanish.
    """
    return 6 ** g


def class_m_einf_poincare(g: int) -> List[int]:
    """E_4 Poincare polynomial for class M at genus g.

    This equals E_inf only for g <= 3 unless higher differentials vanish.
    E_4^n = 3^g * C(g, n-g) for g <= n <= 2g, else 0.
    """
    N = 3 * g
    result = []
    for n in range(N + 1):
        k = n - g
        if 0 <= k <= g:
            result.append(3 ** g * comb(g, k))
        else:
            result.append(0)
    return result


def class_m_deficit(g: int) -> int:
    """Dimension deficit: class L dim (8^g) - class M dim (6^g)."""
    return 8 ** g - 6 ** g


def class_comparison_table(max_g: int = 7) -> List[Dict[str, Any]]:
    """Comparison table across genera.

    Returns list of dicts with genus, class L dim, class M dim, deficit, ratio.
    """
    rows = []
    for g in range(1, max_g + 1):
        L = 8 ** g
        M = 6 ** g
        rows.append({
            "genus": g,
            "class_L_dim": L,
            "class_M_dim": M,
            "deficit": L - M,
            "ratio": L / M,
        })
    return rows


def verify_kunneth_against_matrix(g: int) -> bool:
    """Verify the Kunneth closed form against exact matrix rank computation.

    Returns True if the two methods agree at all degrees.
    """
    engine = E3BarHigherGenusClassM(g=g)
    kunneth = engine.e4_poincare()
    exact = engine.e4_poincare_exact()
    return kunneth == exact
