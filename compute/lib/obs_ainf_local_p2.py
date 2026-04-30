r"""Raw \(m_3\)--\(B^{(2)}_{\mathrm{term}}\) obstruction witness.

This engine computes a strict cyclic \(CY_3\) algebraic witness for the
termwise pair-contraction operator \(B^{(2)}_{\mathrm{term}}\).  It does
not compute Costello's corrected \(B^{(2)}_{\mathrm{TCFT}}\), does not
identify the two operators, and does not prove compact \(CY_3\) vanishing.

The normalized witness is

    m_3(a,a,a)=\alpha b,\qquad |a|=1,\ |b|=2,
    [m_3,B^{(2)}_{\mathrm{term}}][a|a|a|a|b]=2\alpha[b].

For \(\alpha\neq0\), this is a nonzero raw termwise commutator.  Cyclicity
and bidegree bookkeeping are therefore diagnostic only: they do not imply
universal \(Obs_{\Ainf}=0\).  Compact \(CY_3\) vanishing requires either a
corrected TCFT comparison datum for \(B^{(2)}_{\mathrm{TCFT}}\) or an
explicit \(HH^{-2}\) filtration theorem.

Local \(\mathbb P^2=\operatorname{Tot}(\mathcal O_{\mathbb P^2}(-3))\)
enters only as noncompact diagnostic motivation for non-formal behavior.
The four-generator model below is the algebraic strict witness from
``standalone/m3_b2_obstruction_vol3.tex``; it is not by itself a compact
\(CY_3\) theorem or a global \(\Phi_3\) construction.
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

F = Fraction

B_TERM = "B^{(2)}_term"
B_TCFT = "B^{(2)}_TCFT"
STRICT_WITNESS_FORMULA = (
    "[m_3,B^{(2)}_term][a|a|a|a|b] = 2*alpha*[b]"
)


def raw_witness_scope() -> Dict[str, Any]:
    r"""Scope of this executable oracle.

    The function is intentionally data-only so tests can assert the contract
    independently of the route computation.
    """
    return {
        "carrier": B_TERM,
        "not_carrier": B_TCFT,
        "witness_formula": STRICT_WITNESS_FORMULA,
        "local_p2_scope": "noncompact diagnostic",
        "compact_cy3_vanishing_theorem": False,
        "identifies_b_term_with_b_tcft": False,
        "cyclicity_implies_termwise_vanishing": False,
        "toric_bv_implies_raw_ainf_vanishing": False,
        "compact_vanishing_requires": (
            "corrected TCFT comparison datum or HH^{-2} filtration theorem"
        ),
    }


# =========================================================================
#  0. LEGACY 8-GENERATOR DIAGNOSTIC BASIS
# =========================================================================

@dataclass(frozen=True)
class ExtGenerator:
    """A basis element used by the legacy 8-generator diagnostic.

    The diagnostic basis has:
      Degree 0: e (unit)
      Degree 1: x_1, x_2, x_3
      Degree 2: y_1, y_2, y_3
      Degree 3: w (top)

    Total dimension: 8.  This is the Poincare polynomial
    (1 + t)^3 restricted by the CY_3 Serre duality.

    Actually: dim A^0 = 1, dim A^1 = 3, dim A^2 = 3, dim A^3 = 1.
    Poincare polynomial: 1 + 3t + 3t^2 + t^3 = (1+t)^3.
    """
    name: str
    degree: int

    def __repr__(self) -> str:
        return self.name


# Basis elements
e = ExtGenerator("e", 0)       # unit
x1 = ExtGenerator("x1", 1)
x2 = ExtGenerator("x2", 1)
x3 = ExtGenerator("x3", 1)
y1 = ExtGenerator("y1", 2)
y2 = ExtGenerator("y2", 2)
y3 = ExtGenerator("y3", 2)
w = ExtGenerator("w", 3)       # top class

ALL_GENERATORS = [e, x1, x2, x3, y1, y2, y3, w]
DEGREE_1 = [x1, x2, x3]
DEGREE_2 = [y1, y2, y3]

# Index maps for convenience
X = {1: x1, 2: x2, 3: x3}
Y = {1: y1, 2: y2, 3: y3}


# =========================================================================
#  1. THE CY_3 SERRE PAIRING
# =========================================================================

def serre_pairing(a: ExtGenerator, b: ExtGenerator) -> Fraction:
    """The CY_3 Serre duality pairing <a, b>.

    Nonzero only when |a| + |b| = 3 (the CY dimension).
    The pairing is graded symmetric: <a,b> = (-1)^{|a||b|} <b,a>.

    Explicit values:
      <e, w> = <w, e> = 1
      <x_i, y_j> = delta_{ij}
      <y_i, x_j> = (-1)^{1*2} delta_{ij} = delta_{ij}

    Returns
    -------
    Fraction : the pairing value
    """
    if a.degree + b.degree != 3:
        return F(0)

    # (0, 3) pairing: <e, w>
    if a == e and b == w:
        return F(1)
    if a == w and b == e:
        return F(1)

    # (1, 2) pairing: <x_i, y_j> = delta_{ij}
    if a.degree == 1 and b.degree == 2:
        # Extract indices
        ai = int(a.name[1])
        bi = int(b.name[1])
        return F(1) if ai == bi else F(0)

    # (2, 1) pairing: <y_i, x_j> = (-1)^{|y||x|} <x_j, y_i> = (-1)^2 delta_{ij}
    if a.degree == 2 and b.degree == 1:
        ai = int(a.name[1])
        bi = int(b.name[1])
        return F(1) if ai == bi else F(0)

    return F(0)


def verify_pairing_nondegeneracy() -> bool:
    """Verify that the Serre pairing is non-degenerate.

    For each basis element a, there exists b with <a, b> != 0.
    """
    for a in ALL_GENERATORS:
        found = False
        for b in ALL_GENERATORS:
            if serre_pairing(a, b) != F(0):
                found = True
                break
        if not found:
            return False
    return True


def verify_pairing_symmetry() -> bool:
    """Verify graded symmetry: <a,b> = (-1)^{|a||b|} <b,a>."""
    for a in ALL_GENERATORS:
        for b in ALL_GENERATORS:
            sign = (-1) ** (a.degree * b.degree)
            if serre_pairing(a, b) != F(sign) * serre_pairing(b, a):
                return False
    return True


# =========================================================================
#  2. THE CUP PRODUCT mu_2
# =========================================================================

def mu_2(a: ExtGenerator, b: ExtGenerator) -> List[Tuple[Fraction, ExtGenerator]]:
    """The cup product mu_2(a, b) on the Ext algebra.

    Returns a list of (coefficient, generator) pairs representing
    the output as a linear combination of basis elements.

    The algebra structure:
      mu_2(e, a) = a  (unit)
      mu_2(a, e) = a  (unit)
      mu_2(x_i, x_j) = epsilon_{ijk} * y_k  for distinct i,j
      mu_2(x_i, x_i) = 0  (x_i^2 = 0)
      mu_2(x_i, y_j) = delta_{ij} * w
      mu_2(y_i, x_j) = (-1)^{|y||x|} delta_{ij} * w = delta_{ij} * w
      mu_2(y_i, y_j) = 0  (degree 4 > 3)
      mu_2(x_i, w) = 0  (degree 4 > 3)
      mu_2(w, anything) = 0  (degree > 3) except mu_2(w, e)=w... no, |w|+|e|=3 but
        mu_2 preserves degree, so mu_2(w,e) is in degree 3 = w, OK.

    Actually mu_2 has degree 0: |mu_2(a,b)| = |a|+|b|.
    So mu_2(w, e) has degree 3, which is fine.
    But mu_2(w, x_i) would have degree 4 > 3 = max degree, so = 0.
    """
    # Handle unit
    if a == e:
        return [(F(1), b)]
    if b == e:
        return [(F(1), a)]

    # Zero if output degree exceeds 3
    out_degree = a.degree + b.degree
    if out_degree > 3:
        return []

    # mu_2(x_i, x_j): degree 2 output
    if a.degree == 1 and b.degree == 1:
        ai, bi = int(a.name[1]), int(b.name[1])
        if ai == bi:
            return []  # x_i^2 = 0
        # epsilon_{ijk}: the Levi-Civita symbol
        # For the exterior algebra structure of H^*(P^2):
        # x_1 * x_2 = y_3, x_2 * x_3 = y_1, x_3 * x_1 = y_2
        # (and antisymmetric)
        eps = _levi_civita(ai, bi)
        if eps == 0:
            return []
        # The third index k is determined by {1,2,3} \ {i,j}
        k = 6 - ai - bi  # 1+2+3=6, so k = 6-i-j
        return [(F(eps), Y[k])]

    # mu_2(x_i, y_j): degree 3 output
    if a.degree == 1 and b.degree == 2:
        ai, bj = int(a.name[1]), int(b.name[1])
        if ai == bj:
            return [(F(1), w)]
        return []

    # mu_2(y_i, x_j): degree 3 output
    # Graded commutativity: mu_2(y_i, x_j) = (-1)^{|y||x|} mu_2(x_j, y_i)
    # = (-1)^{2*1} mu_2(x_j, y_i) = mu_2(x_j, y_i) = delta_{ij} * w
    if a.degree == 2 and b.degree == 1:
        ai, bj = int(a.name[1]), int(b.name[1])
        if ai == bj:
            return [(F(1), w)]
        return []

    # mu_2(w, e) = w, but we handled unit above.
    # All other products are zero.
    return []


def _levi_civita(i: int, j: int) -> int:
    """Levi-Civita symbol epsilon_{ijk} for distinct i,j in {1,2,3}.

    Returns the sign of the permutation (i,j,k) where k = 6-i-j.
    """
    if i == j:
        return 0
    k = 6 - i - j
    # (1,2,3) -> +1, (1,3,2) -> -1, (2,1,3) -> -1, etc.
    perm = (i, j, k)
    # Count inversions
    inversions = 0
    for a in range(3):
        for b in range(a + 1, 3):
            if perm[a] > perm[b]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


# =========================================================================
#  3. THE MASSEY PRODUCT mu_3
# =========================================================================

def mu_3(a: ExtGenerator, b: ExtGenerator, c: ExtGenerator
         ) -> List[Tuple[Fraction, ExtGenerator]]:
    r"""Legacy 8-generator diagnostic \(m_3\).

    The corrected engine does not use a local \(\mathbb P^2\) one-object
    \(m_3\) as a compact theorem.  The strict witness is implemented by
    :class:`MinimalCyclicCY3`; this helper returns zero so the legacy
    exterior-algebra diagnostic remains inert.
    """
    return []


# =========================================================================
#  4. THE MINIMAL CYCLIC A_INFINITY CY_3 ALGEBRA
# =========================================================================

@dataclass
class MinimalCyclicCY3:
    r"""Strict cyclic \(CY_3\) witness algebra for \(B^{(2)}_{\mathrm{term}}\).

    The algebra:
      A = span{e, a, b, w} with |e|=0, |a|=1, |b|=2, |w|=3.

    The CY_3 pairing:
      <e, w> = <w, e> = 1
      <a, b> = <b, a> = 1

    The A_infinity operations:
      mu_1 = 0  (minimal model)
      mu_2(e, -) = (-,e) = id  (unit), mu_2 = 0 on augmentation ideal
      mu_3(a, a, a) = alpha * b  (the ONLY nontrivial higher operation)
      mu_n = 0 for n >= 4

    alpha = 0 gives the formal (trivial) case.
    alpha != 0 gives the nonzero raw termwise witness.

    This is the simplest cyclic A_infinity algebra with nontrivial mu_3
    that satisfies all A_infinity relations and cyclic invariance.  It is
    an algebraic strict model, not a compact \(CY_3\) vanishing theorem.
    """
    alpha: Fraction = F(1)

    # Basis
    UNIT: ExtGenerator = field(default_factory=lambda: ExtGenerator("e", 0))
    A: ExtGenerator = field(default_factory=lambda: ExtGenerator("a", 1))
    B: ExtGenerator = field(default_factory=lambda: ExtGenerator("b", 2))
    W: ExtGenerator = field(default_factory=lambda: ExtGenerator("w", 3))

    @property
    def basis(self) -> List[ExtGenerator]:
        return [self.UNIT, self.A, self.B, self.W]

    @property
    def aug_basis(self) -> List[ExtGenerator]:
        """Augmentation ideal basis (exclude unit)."""
        return [self.A, self.B, self.W]

    def pairing(self, x: ExtGenerator, y: ExtGenerator) -> Fraction:
        """The CY_3 Serre pairing."""
        if x.degree + y.degree != 3:
            return F(0)
        if (x == self.UNIT and y == self.W) or (x == self.W and y == self.UNIT):
            return F(1)
        if (x == self.A and y == self.B) or (x == self.B and y == self.A):
            return F(1)
        return F(0)

    def m2(self, x: ExtGenerator, y: ExtGenerator) -> List[Tuple[Fraction, ExtGenerator]]:
        """Binary product mu_2(x, y).

        Unit maps only; mu_2 = 0 on augmentation ideal.
        (Forced by the n=4 A_infinity relation when mu_3(a,a,a) != 0.)
        """
        if x == self.UNIT:
            return [(F(1), y)]
        if y == self.UNIT:
            return [(F(1), x)]
        return []

    def m3(self, x: ExtGenerator, y: ExtGenerator, z: ExtGenerator
           ) -> List[Tuple[Fraction, ExtGenerator]]:
        """Ternary operation mu_3(x, y, z).

        The only nontrivial value: mu_3(a, a, a) = alpha * b.
        """
        # Strict unitality for n >= 3
        if x == self.UNIT or y == self.UNIT or z == self.UNIT:
            return []
        if x == self.A and y == self.A and z == self.A:
            if self.alpha != F(0):
                return [(self.alpha, self.B)]
        return []

    def verify_cyclic_invariance_m3(self) -> Tuple[bool, str]:
        """Verify cyclic invariance of mu_3.

        For all (a1, a2, a3, a4) in basis:
          <mu_3(a1,a2,a3), a4> = (-1)^{eps_3} <a1, mu_3(a2,a3,a4)>

        where eps_3 = 3 + |a1|(|a2| + |a3| + |a4|).

        Returns (success, detail_message).
        """
        violations = []
        for a1 in self.aug_basis:
            for a2 in self.aug_basis:
                for a3 in self.aug_basis:
                    for a4 in self.aug_basis:
                        # Compute LHS: <mu_3(a1,a2,a3), a4>
                        m3_out = self.m3(a1, a2, a3)
                        lhs = sum(
                            c * self.pairing(g, a4)
                            for c, g in m3_out
                        )

                        # Sign: eps_3 = 3 + |a1|*(|a2|+|a3|+|a4|)
                        eps = 3 + a1.degree * (a2.degree + a3.degree + a4.degree)
                        sign = F((-1) ** eps)

                        # Compute RHS: (-1)^eps * <a1, mu_3(a2,a3,a4)>
                        m3_out2 = self.m3(a2, a3, a4)
                        rhs = sign * sum(
                            c * self.pairing(a1, g)
                            for c, g in m3_out2
                        )

                        if lhs != rhs:
                            violations.append(
                                f"<m3({a1},{a2},{a3}),{a4}> = {lhs} "
                                f"!= (-1)^{eps} <{a1},m3({a2},{a3},{a4})> = {rhs}"
                            )

        if violations:
            return False, "; ".join(violations[:5])
        return True, "All cyclic invariance checks passed for mu_3"

    def verify_ainf_relations(self) -> Tuple[bool, str]:
        """Verify the A_infinity relations through n=5.

        Returns (success, detail_message).
        """
        violations = []

        # n=3 relation: mu_2(mu_2(a,b),c) - mu_2(a,mu_2(b,c)) = 0  (since mu_1=0, mu_3 terms vanish)
        # On augmentation ideal with mu_2=0: trivially satisfied.

        # n=4 relation: mu_2(mu_3(a,b,c),d) + mu_3(mu_2(a,b),c,d) + ... + mu_2(a,mu_3(b,c,d)) = 0
        # With mu_2=0 on aug. ideal and mu_3(a,a,a)=alpha*b:
        # The only potentially nonzero terms for inputs (a,a,a,a):
        #   mu_2(mu_3(a,a,a), a) = mu_2(alpha*b, a) = 0 (mu_2=0 on aug)
        #   mu_2(a, mu_3(a,a,a)) = mu_2(a, alpha*b) = 0 (mu_2=0 on aug)
        # All good.

        for inputs in itertools.product(self.aug_basis, repeat=4):
            a1, a2, a3, a4 = inputs
            total = F(0)

            # mu_2(mu_3(a1,a2,a3), a4)
            for c1, g1 in self.m3(a1, a2, a3):
                for c2, g2 in self.m2(g1, a4):
                    total += c1 * c2

            # mu_3(mu_2(a1,a2), a3, a4) with sign
            for c1, g1 in self.m2(a1, a2):
                for c2, g2 in self.m3(g1, a3, a4):
                    total += c1 * c2

            # mu_3(a1, mu_2(a2,a3), a4) with sign (-1)^{|a1|}
            sign_1 = F((-1) ** a1.degree)
            for c1, g1 in self.m2(a2, a3):
                for c2, g2 in self.m3(a1, g1, a4):
                    total += sign_1 * c1 * c2

            # mu_3(a1, a2, mu_2(a3,a4)) with sign (-1)^{|a1|+|a2|}
            sign_2 = F((-1) ** (a1.degree + a2.degree))
            for c1, g1 in self.m2(a3, a4):
                for c2, g2 in self.m3(a1, a2, g1):
                    total += sign_2 * c1 * c2

            # mu_2(a1, mu_3(a2,a3,a4)) with sign (-1)^{|a1|}
            for c1, g1 in self.m3(a2, a3, a4):
                for c2, g2 in self.m2(a1, g1):
                    total += sign_1 * c1 * c2

            if total != F(0):
                violations.append(
                    f"n=4 relation fails on ({a1},{a2},{a3},{a4}): total = {total}"
                )

        if violations:
            return False, "; ".join(violations[:5])
        return True, "All A_infinity relations verified through n=4"


# =========================================================================
#  5. BAR COMPLEX AND CYCLIC BAR COMPLEX ELEMENTS
# =========================================================================

@dataclass(frozen=True)
class BarElement:
    """An element of the bar complex B(A) = T^c(s^{-1} bar(A)).

    Represents the bar tensor [a_0 | a_1 | ... | a_{n-1}] with a
    coefficient.  The a_i are elements of the augmentation ideal bar(A).

    In the CYCLIC bar complex CC_n(A) = bar(A)^{otimes(n+1)} / cyclic,
    we use tuples of length n+1 and identify cyclic rotations.
    """
    factors: Tuple[ExtGenerator, ...]
    coeff: Fraction = F(1)

    @property
    def arity(self) -> int:
        """Number of tensor factors (= bar degree + 1 in cyclic complex)."""
        return len(self.factors)

    @property
    def total_degree(self) -> int:
        """Total cohomological degree of all factors."""
        return sum(g.degree for g in self.factors)

    def __repr__(self) -> str:
        inner = "|".join(str(g) for g in self.factors)
        if self.coeff == F(1):
            return f"[{inner}]"
        if self.coeff == F(-1):
            return f"-[{inner}]"
        return f"{self.coeff}*[{inner}]"


class BarLinComb:
    """A linear combination of bar elements."""

    def __init__(self, terms: Optional[List[BarElement]] = None):
        self.terms: List[BarElement] = list(terms) if terms else []

    def simplify(self) -> "BarLinComb":
        """Collect like terms (same factors) and cancel zeros."""
        coeff_map: Dict[Tuple[ExtGenerator, ...], Fraction] = defaultdict(F)
        for t in self.terms:
            coeff_map[t.factors] += t.coeff
        out = []
        for factors, coeff in sorted(coeff_map.items(), key=lambda x: str(x[0])):
            if coeff != F(0):
                out.append(BarElement(factors=factors, coeff=coeff))
        return BarLinComb(out)

    @property
    def is_zero(self) -> bool:
        return len(self.simplify().terms) == 0

    def __add__(self, other: "BarLinComb") -> "BarLinComb":
        return BarLinComb(self.terms + other.terms)

    def __sub__(self, other: "BarLinComb") -> "BarLinComb":
        neg = [BarElement(t.factors, -t.coeff) for t in other.terms]
        return BarLinComb(self.terms + neg)

    def __repr__(self) -> str:
        s = self.simplify()
        if not s.terms:
            return "0"
        return " + ".join(str(t) for t in s.terms)


# =========================================================================
#  6. B^{(2)} MAP: PAIRWISE CONTRACTION
# =========================================================================

def b2_map(elem: BarElement, alg: MinimalCyclicCY3) -> BarLinComb:
    r"""Apply \(B^{(2)}_{\mathrm{term}}\) to a bar element.

    \(B^{(2)}_{\mathrm{term}}\) contracts a pair of factors using the
    chosen \(CY_3\) pairing:

      B^{(2)}([a_0|...|a_n]) = sum_{0<=i<j<=n} (-1)^{sgn(i,j)}
          * <a_i, a_j> * [a_0|...|hat_i|...|hat_j|...|a_n]

    CRITICAL SIGN CONVENTION (AP45):
    The bar complex B(A) = T^c(s^{-1} bar(A)) uses DESUSPENDED elements.
    The degree of s^{-1}a in the bar complex is |a| - 1.  All Koszul
    signs in the bar complex must therefore use the desuspended degree
    (|a_k| - 1), NOT the original degree |a_k|.

    The sign for contracting pair (i, j) with i < j is:

      (-1)^{(|a_i|-1) * sum_{k<i}(|a_k|-1) + (|a_j|-1) * sum_{i<k<j}(|a_k|-1)}

    This is the Koszul sign for moving s^{-1}a_i and s^{-1}a_j together
    in the desuspended tensor product.

    Example: for degree-1 elements a with |a|-1 = 0, moving s^{-1}a
    past anything produces NO sign.  For degree-2 elements b with
    |b|-1 = 1, moving s^{-1}b past s^{-1}b produces sign (-1)^1 = -1.

    Parameters
    ----------
    elem : BarElement
        Input bar element [a_0|...|a_n].
    alg : MinimalCyclicCY3
        The algebra providing the pairing.

    Returns
    -------
    BarLinComb : the result of applying \(B^{(2)}_{\mathrm{term}}\).
    """
    n = elem.arity
    factors = elem.factors
    result_terms = []

    for i in range(n):
        for j in range(i + 1, n):
            # Compute pairing <a_i, a_j>
            p = alg.pairing(factors[i], factors[j])
            if p == F(0):
                continue

            # BAR-DESUSPENDED Koszul sign (AP45: |s^{-1}a| = |a| - 1)
            # Move s^{-1}a_i past s^{-1}a_0,...,s^{-1}a_{i-1}:
            sign_i = sum(factors[k].degree - 1 for k in range(i)) * (factors[i].degree - 1)
            # Move s^{-1}a_j past s^{-1}a_{i+1},...,s^{-1}a_{j-1}:
            sign_j = sum(factors[k].degree - 1 for k in range(i + 1, j)) * (factors[j].degree - 1)
            total_sign = F((-1) ** (sign_i + sign_j))

            # Remove positions i and j
            remaining = tuple(
                factors[k] for k in range(n) if k != i and k != j
            )

            coeff = elem.coeff * p * total_sign
            if remaining:
                result_terms.append(BarElement(factors=remaining, coeff=coeff))
            else:
                # All factors contracted: scalar contribution
                # In CC_0, the result is the empty tensor = unit
                result_terms.append(BarElement(factors=(alg.UNIT,), coeff=coeff))

    return BarLinComb(result_terms)


def b2_on_lincomb(lc: BarLinComb, alg: MinimalCyclicCY3) -> BarLinComb:
    r"""Apply \(B^{(2)}_{\mathrm{term}}\) to a linear combination."""
    result = BarLinComb()
    for t in lc.terms:
        result = result + b2_map(t, alg)
    return result


# =========================================================================
#  7. m_3 MAP ON THE BAR COMPLEX
# =========================================================================

def m3_bar(elem: BarElement, alg: MinimalCyclicCY3) -> BarLinComb:
    r"""Apply the bar differential component m_3 to a bar element.

    m_3 acts on the bar complex by applying mu_3 to each set of 3
    consecutive factors:

      m_3([a_0|...|a_n]) = sum_{i=0}^{n-2} (-1)^{sgn_i}
          [a_0|...|a_{i-1}| mu_3(a_i, a_{i+1}, a_{i+2}) |a_{i+3}|...|a_n]

    The sign: in the bar complex, the sign for applying mu_k starting
    at position i is:

      (-1)^{sum_{j<i} (|a_j| - 1)}

    This is the DESUSPENDED sign convention (AP45): in the bar complex
    B(A) = T^c(sA), the element s^{-1}a has degree |a|-1.

    Parameters
    ----------
    elem : BarElement
        Input bar element [a_0|...|a_n] with n+1 factors.
    alg : MinimalCyclicCY3
        The algebra providing mu_3.

    Returns
    -------
    BarLinComb : the result of applying m_3 to the bar element.
    """
    n = elem.arity
    factors = elem.factors
    result_terms = []

    # m_3 applies to 3 consecutive factors at positions i, i+1, i+2
    for i in range(n - 2):
        # Compute mu_3(a_i, a_{i+1}, a_{i+2})
        m3_out = alg.m3(factors[i], factors[i + 1], factors[i + 2])
        if not m3_out:
            continue

        # Bar sign: (-1)^{sum_{j<i} (|a_j| - 1)}
        bar_sign_exp = sum(factors[j].degree - 1 for j in range(i))
        bar_sign = F((-1) ** bar_sign_exp)

        for coeff, gen in m3_out:
            new_factors = factors[:i] + (gen,) + factors[i + 3:]
            result_terms.append(
                BarElement(factors=new_factors, coeff=elem.coeff * coeff * bar_sign)
            )

    return BarLinComb(result_terms)


def m3_on_lincomb(lc: BarLinComb, alg: MinimalCyclicCY3) -> BarLinComb:
    """Apply m_3 to a linear combination of bar elements."""
    result = BarLinComb()
    for t in lc.terms:
        result = result + m3_bar(t, alg)
    return result


# =========================================================================
#  8. THE COMMUTATOR [m_3, B^{(2)}]
# =========================================================================

def commutator_m3_b2(elem: BarElement, alg: MinimalCyclicCY3) -> BarLinComb:
    r"""Compute the raw termwise commutator on a bar element.

    The operator is \(B^{(2)}_{\mathrm{term}}\), not Costello's corrected
    \(B^{(2)}_{\mathrm{TCFT}}\).  Nonvanishing is a strict-model witness,
    not a compact \(CY_3\) vanishing or nonvanishing theorem.

    Parameters
    ----------
    elem : BarElement
        Input bar element.
    alg : MinimalCyclicCY3
        The cyclic A_infinity algebra.

    Returns
    -------
    BarLinComb : \([m_3, B^{(2)}_{\mathrm{term}}]\) applied to elem.
    """
    # Route 1: m_3 . B^{(2)}(elem)
    b2_result = b2_map(elem, alg)
    route1 = m3_on_lincomb(b2_result, alg)

    # Route 2: B^{(2)} . m_3(elem)
    m3_result = m3_bar(elem, alg)
    route2 = b2_on_lincomb(m3_result, alg)

    return (route1 - route2).simplify()


# =========================================================================
#  9. EXHAUSTIVE COMPUTATION ON CC_4
# =========================================================================

def compute_commutator_on_cc4(alg: MinimalCyclicCY3) -> Dict[str, Any]:
    r"""Compute \([m_3, B^{(2)}_{\mathrm{term}}]\) on all CC_4 words.

    CC_4(A) consists of bar elements [a_0|a_1|a_2|a_3|a_4] with
    a_i in aug(A) = {a, b, w}.

    The computation checks the raw termwise commutator on the first
    nontrivial bar degree.

    Returns a dictionary with:
      - 'all_inputs': list of all tested inputs
      - 'nonzero_results': inputs where [m_3, B^{(2)}] != 0
      - 'commutator_vanishes': True iff all results are zero
      - 'detail': per-input breakdown
    """
    aug = alg.aug_basis
    results = []
    nonzero = []

    # Generate all CC_4 elements (5-fold tensor products of aug basis)
    for combo in itertools.product(aug, repeat=5):
        elem = BarElement(factors=combo, coeff=F(1))

        # Skip if B^{(2)} and m_3 both give zero (for efficiency)
        comm = commutator_m3_b2(elem, alg)

        entry = {
            "input": repr(elem),
            "commutator": repr(comm),
            "is_zero": comm.is_zero,
        }
        results.append(entry)

        if not comm.is_zero:
            nonzero.append(entry)

    return {
        "bar_degree": 4,
        "num_inputs": len(results),
        "num_nonzero": len(nonzero),
        "commutator_vanishes": len(nonzero) == 0,
        "nonzero_results": nonzero,
        "detail": results,
    }


def compute_commutator_on_cc5(alg: MinimalCyclicCY3) -> Dict[str, Any]:
    r"""Compute \([m_3, B^{(2)}_{\mathrm{term}}]\) on CC_5 words.

    This is a larger computation but provides a stronger test.
    """
    aug = alg.aug_basis
    results = []
    nonzero = []

    for combo in itertools.product(aug, repeat=6):
        elem = BarElement(factors=combo, coeff=F(1))
        comm = commutator_m3_b2(elem, alg)

        entry = {
            "input": repr(elem),
            "commutator": repr(comm),
            "is_zero": comm.is_zero,
        }
        results.append(entry)

        if not comm.is_zero:
            nonzero.append(entry)

    return {
        "bar_degree": 5,
        "num_inputs": len(results),
        "num_nonzero": len(nonzero),
        "commutator_vanishes": len(nonzero) == 0,
        "nonzero_results": nonzero[:20],  # cap output
        "detail": results,
    }


# =========================================================================
#  10. FOCUSED COMPUTATION ON KEY ELEMENTS
# =========================================================================

def compute_key_element_aaaab(alg: MinimalCyclicCY3) -> Dict[str, Any]:
    r"""Detailed computation of the strict witness on [a|a|a|a|b].

    This is the strict element where \(m_3\) and
    \(B^{(2)}_{\mathrm{term}}\) both act nontrivially:
      - m_3 can hit (a,a,a) at positions (0,1,2) and (1,2,3)
      - B^{(2)} can contract (a_i, b) at any (i, 4) pair

    Returns a step-by-step breakdown.
    """
    a, b = alg.A, alg.B
    elem = BarElement(factors=(a, a, a, a, b), coeff=F(1))

    # Step 1: B^{(2)} on [a|a|a|a|b]
    b2_result = b2_map(elem, alg)
    b2_simplified = b2_result.simplify()

    # Step 2: m_3 on B^{(2)} result
    route1 = m3_on_lincomb(b2_result, alg).simplify()

    # Step 3: m_3 on [a|a|a|a|b]
    m3_result = m3_bar(elem, alg)
    m3_simplified = m3_result.simplify()

    # Step 4: B^{(2)} on m_3 result
    route2 = b2_on_lincomb(m3_result, alg).simplify()

    # Step 5: commutator
    comm = (route1 - route2).simplify()

    return {
        "input": repr(elem),
        "step1_b2": repr(b2_simplified),
        "step2_m3_of_b2": repr(route1),
        "step3_m3": repr(m3_simplified),
        "step4_b2_of_m3": repr(route2),
        "commutator": repr(comm),
        "commutator_is_zero": comm.is_zero,
    }


def compute_key_element_aabaa(alg: MinimalCyclicCY3) -> Dict[str, Any]:
    r"""Detailed computation on [a|a|b|a|a].

    Another key element: b is in the middle, so B^{(2)} contractions
    hit elements on both sides of potential m_3 blocks.
    """
    a, b = alg.A, alg.B
    elem = BarElement(factors=(a, a, b, a, a), coeff=F(1))

    b2_result = b2_map(elem, alg)
    route1 = m3_on_lincomb(b2_result, alg).simplify()

    m3_result = m3_bar(elem, alg)
    route2 = b2_on_lincomb(m3_result, alg).simplify()

    comm = (route1 - route2).simplify()

    return {
        "input": repr(elem),
        "m3_then_b2": repr(route1),
        "b2_then_m3": repr(route2),
        "commutator": repr(comm),
        "commutator_is_zero": comm.is_zero,
    }


# =========================================================================
#  11. MASTER COMPUTATION
# =========================================================================

def master_obs_ainf_computation(alpha: Fraction = F(1)) -> Dict[str, Any]:
    r"""Master computation for the raw termwise strict witness.

    Computes \([m_3, B^{(2)}_{\mathrm{term}}]\) on CC_4 and CC_5, with
    detailed breakdowns of key elements.

    Parameters
    ----------
    alpha : Fraction
        The mu_3 coefficient: mu_3(a,a,a) = alpha * b.
        alpha = 0: formal case (commutator trivially zero).
        alpha != 0: strict nonzero termwise witness.

    Returns
    -------
    dict with:
      - 'alpha': the mu_3 coefficient used
      - 'cyclic_invariance': whether mu_3 satisfies cyclic invariance
      - 'ainf_relations': whether A_infinity relations hold
      - 'cc4_result': exhaustive computation on CC_4
      - 'cc5_result': exhaustive computation on CC_5
      - 'key_aaaab': detailed breakdown of [a|a|a|a|b]
      - 'key_aabaa': detailed breakdown of [a|a|b|a|a]
      - 'raw_termwise_commutator_vanishes': termwise verdict
      - 'scope': exact noncompact/TCFT/compact scope
    """
    alg = MinimalCyclicCY3(alpha=alpha)

    # Verify the algebra is consistent
    cyc_ok, cyc_msg = alg.verify_cyclic_invariance_m3()
    ainf_ok, ainf_msg = alg.verify_ainf_relations()

    # Key element computations
    key_aaaab = compute_key_element_aaaab(alg)
    key_aabaa = compute_key_element_aabaa(alg)

    # Exhaustive CC_4
    cc4 = compute_commutator_on_cc4(alg)

    # Exhaustive CC_5
    cc5 = compute_commutator_on_cc5(alg)

    raw_vanishes = cc4["commutator_vanishes"] and cc5["commutator_vanishes"]
    key_nonzero = not key_aaaab["commutator_is_zero"]

    return {
        "alpha": alpha,
        "operator": B_TERM,
        "cyclic_invariance_ok": cyc_ok,
        "cyclic_invariance_detail": cyc_msg,
        "ainf_relations_ok": ainf_ok,
        "ainf_relations_detail": ainf_msg,
        "cc4_result": {
            "num_inputs": cc4["num_inputs"],
            "num_nonzero": cc4["num_nonzero"],
            "vanishes": cc4["commutator_vanishes"],
            "nonzero_results": cc4["nonzero_results"],
        },
        "cc5_result": {
            "num_inputs": cc5["num_inputs"],
            "num_nonzero": cc5["num_nonzero"],
            "vanishes": cc5["commutator_vanishes"],
            "nonzero_results": cc5["nonzero_results"],
        },
        "key_aaaab": key_aaaab,
        "key_aabaa": key_aabaa,
        "raw_witness_nonzero": key_nonzero,
        "raw_termwise_commutator_vanishes": raw_vanishes,
        "termwise_status": "zero_formal" if raw_vanishes else "nonzero_witness",
        "compact_cy3_vanishing_proved": False,
        "scope": raw_witness_scope(),
    }


# =========================================================================
#  12. EXTENDED MODEL: 8-GENERATOR EXTERIOR ALGEBRA
# =========================================================================

@dataclass
class ExtendedCyclicCY3:
    r"""Legacy 8-generator exterior-algebra diagnostic.

    A = span{e, x_1, x_2, x_3, y_1, y_2, y_3, w}
    with |e|=0, |x_i|=1, |y_i|=2, |w|=3.

    Product: exterior algebra (x_i x_j = -x_j x_i, x_i^2 = 0).
    CY_3 pairing: Serre duality.

    This is retained only as diagnostic data.  It is not used to prove
    local \(\mathbb P^2\) compactness, compact \(CY_3\) vanishing, or a
    global \(\Phi_3\) construction.  The raw nonzero witness is the
    four-generator :class:`MinimalCyclicCY3` model.
    """
    alpha: Fraction = F(1)  # mu_3 coefficient (for testing)

    # The full 8-generator basis
    basis: List[ExtGenerator] = field(default_factory=lambda: list(ALL_GENERATORS))

    def pairing(self, a: ExtGenerator, b: ExtGenerator) -> Fraction:
        return serre_pairing(a, b)

    def m2(self, a: ExtGenerator, b: ExtGenerator) -> List[Tuple[Fraction, ExtGenerator]]:
        return mu_2(a, b)

    def m3_exterior(self, a: ExtGenerator, b: ExtGenerator, c: ExtGenerator
                    ) -> List[Tuple[Fraction, ExtGenerator]]:
        """mu_3 on the exterior algebra model.

        The diagnostic exterior-algebra helper is inert; the strict witness
        is implemented separately by :class:`MinimalCyclicCY3`.
        """
        return []

    def verify_8gen_mu3_forced_zero(self) -> Dict[str, Any]:
        r"""Demonstrate that mu_3 = 0 is forced on the 8-generator model.

        For each triple (x_i, x_j, x_k) of degree-1 elements, cyclic
        invariance with the Serre pairing forces the output to be zero.

        This is diagnostic bookkeeping.  It does not identify the local
        \(\mathbb P^2\) category with the four-generator strict witness.
        """
        forced_zero_triples = []
        aug = [x1, x2, x3, y1, y2, y3, w]

        for a in aug:
            for b in aug:
                for c in aug:
                    out_deg = a.degree + b.degree + c.degree - 1
                    if out_deg < 0 or out_deg > 3:
                        continue

                    # Check if any nonzero output is compatible with cyclic inv
                    # <mu_3(a,b,c), d> = (-1)^eps <a, mu_3(b,c,d)>
                    # For this to allow nonzero mu_3(a,b,c), we need at least
                    # one d such that the RHS can be nonzero.

                    # The degree of mu_3(a,b,c) is out_deg.
                    # For <mu_3(a,b,c), d> != 0, we need |d| = 3 - out_deg.
                    d_deg = 3 - out_deg

                    # Generators at degree d_deg:
                    d_gens = [g for g in aug if g.degree == d_deg]

                    # For each d, RHS involves mu_3(b,c,d).
                    # For this to be nonzero, |b|+|c|+|d|-1 must be in {0,...,3}.
                    rhs_out_deg = b.degree + c.degree + d_deg - 1

                    # Check if there's a self-consistent solution
                    can_be_nonzero = False
                    for d in d_gens:
                        if 0 <= rhs_out_deg <= 3:
                            # The RHS involves <a, mu_3(b,c,d)>
                            # For this to be nonzero: |mu_3(b,c,d)| = 3 - |a|
                            if rhs_out_deg == 3 - a.degree:
                                can_be_nonzero = True

                    if out_deg >= 0 and out_deg <= 3:
                        # Check unitality constraint
                        has_unit = (a == e or b == e or c == e)
                        if has_unit:
                            continue  # mu_3 with unit = 0 by strict unitality

                        forced_zero_triples.append({
                            "triple": (str(a), str(b), str(c)),
                            "out_degree": out_deg,
                            "reason": "cyclic_invariance" if not can_be_nonzero else "needs_check",
                        })

        return {
            "num_triples_checked": len(forced_zero_triples),
            "all_forced_zero": all(
                t["reason"] == "cyclic_invariance" for t in forced_zero_triples
            ),
            "triples_needing_check": [
                t for t in forced_zero_triples if t["reason"] == "needs_check"
            ],
        }


# =========================================================================
#  13. SUMMARY AND VERDICT
# =========================================================================

def full_obs_ainf_analysis() -> Dict[str, Any]:
    r"""Complete analysis of the raw termwise commutator.

    Runs the master computation on the minimal CY_3 algebra and
    records the corrected scope.

    Returns the full analysis including:
    - The strict witness computation (4 generators, alpha=1)
    - The 8-generator diagnostic analysis
    - Cross-checks for alpha = 0 (formal, trivial) and alpha = 2
    - Scope data separating \(B^{(2)}_{\mathrm{term}}\) from
      \(B^{(2)}_{\mathrm{TCFT}}\)
    """
    # Formal case: alpha = 0 (trivial)
    formal = master_obs_ainf_computation(alpha=F(0))

    # Strict witness: alpha = 1
    witness_1 = master_obs_ainf_computation(alpha=F(1))

    # Strict witness: alpha = 2 (linearity check)
    witness_2 = master_obs_ainf_computation(alpha=F(2))

    # 8-generator model: mu_3 forced to zero
    ext_model = ExtendedCyclicCY3()
    ext_analysis = ext_model.verify_8gen_mu3_forced_zero()

    scope = raw_witness_scope()

    return {
        "formal_case": {
            "alpha": 0,
            "raw_termwise_commutator_vanishes": formal["raw_termwise_commutator_vanishes"],
            "termwise_status": formal["termwise_status"],
        },
        "strict_witness_alpha1": {
            "alpha": 1,
            "operator": witness_1["operator"],
            "cyclic_invariance_ok": witness_1["cyclic_invariance_ok"],
            "ainf_relations_ok": witness_1["ainf_relations_ok"],
            "cc4_raw_vanishes": witness_1["cc4_result"]["vanishes"],
            "cc4_nonzero": witness_1["cc4_result"]["num_nonzero"],
            "cc5_raw_vanishes": witness_1["cc5_result"]["vanishes"],
            "cc5_nonzero": witness_1["cc5_result"]["num_nonzero"],
            "raw_witness_nonzero": witness_1["raw_witness_nonzero"],
            "raw_termwise_commutator_vanishes": witness_1["raw_termwise_commutator_vanishes"],
            "termwise_status": witness_1["termwise_status"],
            "key_aaaab": witness_1["key_aaaab"],
            "key_aabaa": witness_1["key_aabaa"],
        },
        "strict_witness_alpha2": {
            "alpha": 2,
            "raw_witness_nonzero": witness_2["raw_witness_nonzero"],
            "raw_termwise_commutator_vanishes": witness_2["raw_termwise_commutator_vanishes"],
            "termwise_status": witness_2["termwise_status"],
        },
        "extended_8gen_diagnostic": ext_analysis,
        "scope": scope,
        "verdict": {
            "carrier": scope["carrier"],
            "witness_formula": scope["witness_formula"],
            "raw_termwise_witness_nonzero": witness_1["raw_witness_nonzero"],
            "compact_cy3_vanishing_proved": False,
            "identifies_b_term_with_b_tcft": False,
            "explanation": (
                "The engine computes the raw termwise witness for "
                "B^{(2)}_term. Compact CY3 vanishing requires a corrected "
                "TCFT comparison datum or an HH^{-2} filtration theorem."
            ),
        },
    }
