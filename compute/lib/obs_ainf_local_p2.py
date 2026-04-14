r"""Explicit computation of [m_3, B^{(2)}] for local P^2.

MATHEMATICAL CONTENT
====================

This module resolves AP-CY34: the logical gap in Proposition
prop:cyclic-ainf-framing-compat.  The gap is between:
  (G1) Cyclic invariance: <mu_n(a_1,...,a_n), a_{n+1}> = +/- <a_1, mu_n(a_2,...,a_{n+1})>
  (G2) Bar-level compatibility: [m_k, B^{(2)}] = 0 on CC_n(C)

The proof claimed (G1) => (G2), but the "non-adjacent" contractions
(where B^{(2)} contracts one factor inside the m_k-block with one outside)
are not controlled by cyclic invariance alone.

THE MODEL: LOCAL P^2 = Tot(O(-3) -> P^2)
==========================================

Local P^2 is the simplest non-formal CY_3 with m_3 != 0.  Its derived
category D^b(Coh(P^2)) has an exceptional collection <O, O(1), O(2)>,
and the endomorphism algebra has a minimal A_infinity model on cohomology.

The Ext algebra of the structure sheaf O_{P^2} (as a one-object model):
  A = C[x,y,z]/(x^2, y^2, z^2, xy+yz+zx)

with |x| = |y| = |z| = 1.  This is the cohomology ring H^*(P^2; C)
viewed through the Koszul dual lens: the relations xy+yz+zx = 0 come
from the quadric relation in H^*(P^2).

Actually, for the CY_3 = Tot(O(-3) -> P^2) computation, we use the
SELF-EXT algebra of a generating object.  The relevant algebra is the
Ginzburg DG algebra of the McKay quiver of Z_3, whose cohomology
(= the minimal A_infinity model) has:

  Degree 0: e_0 (unit, rank 1)
  Degree 1: x_1, x_2, x_3 (3 generators)
  Degree 2: y_1, y_2, y_3 (3 generators)
  Degree 3: w (top class, rank 1)

Total dimension: 1 + 3 + 3 + 1 = 8.

The cup product m_2 and the CY_3 Serre pairing <-,-> are:
  m_2(x_i, x_j) = epsilon_{ijk} y_k  (for i != j)
  m_2(x_i, y_j) = delta_{ij} w
  m_2(y_i, x_j) = -delta_{ij} w  (graded commutativity: |x||y| = 1*2 = 2, even)

Wait -- let us be more careful.  The algebra is GRADED COMMUTATIVE
(it is the cohomology of a DGA), so:
  m_2(a, b) = (-1)^{|a||b|} m_2(b, a)

For the CY_3 pairing (degree -3):
  <e_0, w> = 1,  <w, e_0> = 1  (symmetric at top)
  <x_i, y_j> = delta_{ij},  <y_i, x_j> = delta_{ij}  (Serre duality)

The MASSEY PRODUCT m_3:
  The non-formality of local P^2 comes from the cubic superpotential
  W = x_1 x_2 x_3 of the McKay quiver.  The minimal A_infinity model
  on cohomology has:
    m_3(x_i, x_j, x_k) = epsilon_{ijk} * w  (the "triple Massey product")

This is the UNIQUE (up to gauge) non-trivial m_3 on this algebra that
  (a) has the correct degree: deg(m_3) = 2-3 = -1, so
      |m_3(x_i,x_j,x_k)| = 3*1 + (-1) = 2... no.

Let me be precise about degrees.

DEGREE CONVENTIONS (cohomological, |d| = +1):
  mu_n: A^{otimes n} -> A has degree 2 - n.
  mu_1: degree 1 (differential, zero on minimal model)
  mu_2: degree 0 (cup product)
  mu_3: degree -1

So mu_3: A^{otimes 3} -> A shifts degree by -1.
  mu_3(x_i, x_j, x_k): degree 3*1 + (-1) = 2.
  So mu_3(x_i, x_j, x_k) lives in A^2 = span{y_1, y_2, y_3}.

This is consistent: the triple Massey product of three degree-1 classes
gives a degree-2 class, which is the classical fact about Massey products
in the cohomology of P^2 (or rather, the total space O(-3) -> P^2).

For local P^2, the Massey product is:
  mu_3(x_i, x_j, x_k) = alpha * epsilon_{ijk} * (y_1 + y_2 + y_3) / 3

No -- for the McKay quiver, the precise m_3 from the homotopy transfer
theorem (Kadeishvili) applied to the Ginzburg algebra with potential
W = x_1 x_2 x_3 is:

  mu_3(x_i, x_j, x_k) = coefficient * (some expression in y's)

The simplest choice compatible with the Z_3 symmetry of the quiver
and cyclic invariance of the CY_3 pairing is:

  mu_3(x_1, x_2, x_3) = alpha * w    (goes from A^1 otimes A^1 otimes A^1 to A^2)

Wait, degree check again:
  |mu_3(x_1,x_2,x_3)| = |x_1|+|x_2|+|x_3| + (2-3) = 1+1+1-1 = 2. Good.

So mu_3(x_1,x_2,x_3) is in A^2.

For the Z_3-symmetric model:
  mu_3(x_1, x_2, x_3) = alpha * (y_1 + y_2 + y_3)  [Z_3-symmetric output]

But the Serre relation requires cyclic invariance:
  <mu_3(x_1,x_2,x_3), x_k> = (-1)^eps <x_1, mu_3(x_2,x_3,x_k)>

This constrains alpha.  Let us just set alpha = 1 (it can be rescaled
by A_infinity gauge equivalence) and work with the simplest model.

SIMPLIFICATION: For the commutator computation, we use the most
explicit model possible.  The algebra:

  A = span{e_0, x_1, x_2, x_3, y_1, y_2, y_3, w}
  |e_0| = 0, |x_i| = 1, |y_i| = 2, |w| = 3

  mu_2(x_i, x_j) = epsilon_{ijk} * y_k  (cup product, graded comm)
  mu_2(x_i, y_j) = delta_{ij} * w
  mu_2(e_0, a) = a, mu_2(a, e_0) = a  (unit)
  mu_2(y_i, x_j) = -delta_{ij} * w  (sign from graded comm: (-1)^{1*2} = 1... )

Hmm, graded commutativity with the KOSZUL sign:
  mu_2(b, a) = (-1)^{|a||b|} mu_2(a, b)
  mu_2(y_i, x_j) = (-1)^{1*2} mu_2(x_j, y_i) = mu_2(x_j, y_i) = delta_{ji} * w

So mu_2(y_i, x_j) = delta_{ij} * w (same sign, since (-1)^2 = 1).

CY_3 PAIRING (degree -3, symmetric):
  <a, b> != 0 only if |a| + |b| = 3
  <e_0, w> = 1
  <w, e_0> = 1
  <x_i, y_j> = delta_{ij}
  <y_i, x_j> = (-1)^{|x||y|} <x_j, y_i> = (-1)^2 delta_{ij} = delta_{ij}

The mu_3 from the McKay quiver with potential W = x_1 x_2 x_3:
  mu_3(x_i, x_j, x_k) = epsilon_{ijk} * w  ... NO, degree 2, not 3.

Let me think again. mu_3 has degree -1, so:
  mu_3: A^1 x A^1 x A^1 -> A^2  (1+1+1-1=2)
  mu_3: A^1 x A^1 x A^2 -> A^3  (1+1+2-1=3)
  mu_3: A^1 x A^2 x A^1 -> A^3  (same)
  mu_3: A^2 x A^1 x A^1 -> A^3  (same)

For the non-formality from the superpotential, the key triple product is:
  mu_3(x_i, x_j, x_k) in A^2

The simplest Z_3-symmetric, cyclically invariant choice:
  mu_3(x_1, x_2, x_3) = y_1  (or some linear combination)

By the A_infinity relations and Z_3 symmetry, the complete m_3 is
determined.  We compute [m_3, B^{(2)}] for ALL inputs.

THE B^{(2)} MAP
================

B^{(2)}: CC_n -> CC_{n-1} is the "S^2-contraction" that contracts
a pair of factors using the degree-2 part of the CY_3 pairing.

On bar elements [a_0 | a_1 | ... | a_n] in CC_n = A^{otimes(n+1)} / cyclic:

  B^{(2)}([a_0 | ... | a_n]) = sum_{0 <= i < j <= n}
      (-1)^{sign} * <a_i, a_j>_2 * [a_0|...|hat{a_i}|...|hat{a_j}|...|a_n]

where <a_i, a_j>_2 means the pairing restricted to the pieces that
sum to degree 2 (the S^2-base contribution in the Connes hierarchy for d=3).

Wait -- B^{(2)}: CC_n -> CC_{n-1} means it goes from (n+1) factors to n factors.
That means it contracts ONE pair, removing one factor (the contraction
replaces two factors a_i, a_j by their pairing value <a_i,a_j>).

More precisely, on the cyclic bar complex CC_n(A) = A^{otimes(n+1)} / cyclic:

  B^{(2)}([a_0 | a_1 | ... | a_n]) = sum_{0 <= i < j <= n}
      (-1)^{sgn(i,j)} * <a_i, a_j> * [a_0|...|hat_i|...|hat_j|...|a_n]

where <a_i, a_j> is nonzero only when |a_i|+|a_j|=3 (the CY_3 pairing
is degree -3, but for B^{(2)} we want the piece that corresponds to
the S^2-base).

Actually, for the Connes hierarchy, B^{(2)} should contract using
the degree (-2) piece of the pairing (the S^2 part), meaning
<a_i,a_j>_{(2)} is nonzero only when |a_i|+|a_j| = 2.  But wait,
the CY_3 pairing has degree -3 and the full pairing pairs |a|+|b|=3.

The Connes hierarchy decomposes the CY_d pairing into pieces:
  <-,->_{(k)}: pairs classes with |a|+|b| = k, for k = 0,...,d

For CY_3:
  <-,->_{(0)}: pairs degree 0 with degree 0 (degenerate)
  <-,->_{(1)}: pairs degree 0 with degree 1 and v.v.
  <-,->_{(2)}: pairs degree 1 with degree 1
  <-,->_{(3)}: pairs degree 0 with degree 3, degree 1 with degree 2, etc.

For B^{(2)}, we use <-,->_{(2)}: this pairs degree 1 with degree 1.

But in our algebra, <x_i, x_j> = 0 (since the CY pairing requires
|a|+|b|=3, not 2).  So <-,->_{(2)} = 0 identically!

This means B^{(2)} = 0 on our algebra if we define it via <-,->_{(2)}.

Hmm, that seems wrong.  Let me reconsider the definition of B^{(2)}.

RECONSIDERING B^{(2)}
======================

From cy_to_chiral.tex L1611:
  "B^{(2)}(a_0, a_1, ..., a_n) = sum_{i<j} <a_i, a_j>_2 * (remaining)"
  where <-,->_2 is "the restriction of the CY_3 pairing to the degree-2
  component."

The manuscript says "degree-2 component" -- this is ambiguous.  But from
the Connes hierarchy structure (L166-200 of hopf_fibration_s3_framing.py):

  B^{(k)}: CC_n -> CC_{n+1-k}

So B^{(2)}: CC_n -> CC_{n-1}.  This removes one factor (contracts a pair).

The pairing used is the FULL CY_3 pairing <-,-> (degree -3), not a
truncation.  The superscript (2) refers to the level in the Connes
hierarchy, not the degree of the pairing.

B^{(2)} is the second-level Connes map, which for CY_3 is the map
that uses the inner product to contract adjacent pairs in the cyclic
bar complex.  Specifically:

  B^{(2)}([a_0|a_1|...|a_n]) = sum_{i} (-1)^{sgn_i} <a_i, a_{i+1}> [a_0|...|hat_i,hat_{i+1}|...|a_n]

where the sum is cyclic (indices mod n+1), and <a_i,a_{i+1}> uses the
FULL CY_3 pairing (nonzero when |a_i|+|a_{i+1}|=3).

No wait -- that contracts ADJACENT pairs only, giving n+1 terms.
But the gap remark specifically discusses NON-ADJACENT contractions.
So B^{(2)} must also contract non-adjacent pairs.

Let me re-read the manuscript definition more carefully.

From cy_to_chiral.tex L1611:
  B^{(2)}(a_0, a_1, ..., a_n) = sum_{i<j} <a_i, a_j>_2 * (remaining factors)

This IS summing over ALL pairs (i,j) with i<j, not just adjacent ones.
The subscript _2 in <-,->_2 refers to using the CY pairing restricted
to the degree-sum-equals-some-value component.

For CY_3, the Connes hierarchy level (2) corresponds to the contraction
that reduces bar degree by 1.  The pairing used is the FULL Serre pairing
<a,b> (nonzero when |a|+|b|=3), applied to all pairs of factors.

CONCRETE DEFINITION:

B^{(2)}: CC_n(A) -> CC_{n-2}(A) contracts a pair of factors using <-,->.

On A^{otimes(n+1)} (before cyclic quotient):

  B^{(2)}(a_0 otimes ... otimes a_n) = sum_{0<=i<j<=n} sgn(i,j,a)
      * <a_i, a_j> * (a_0 otimes ... hat{a_i} ... hat{a_j} ... otimes a_n)

The output has n-1 factors, so B^{(2)}: CC_n -> CC_{n-2}.

DEGREE CHECK: B^{(2)} should have degree 1-2 = -1 (from the Connes
hierarchy: B^{(k)} has degree shift 1-k).  The pairing <a_i,a_j>
contributes degree -(|a_i|+|a_j|) + 3 ... no.

Actually, B^{(2)}: CC_n -> CC_{n-1} (reduces cyclic complex degree by 1).
The cyclic complex CC_n(A) has elements in A^{otimes(n+1)} / cyclic.
B^{(2)} maps CC_n to CC_{n-2} by removing two factors and replacing
them with their pairing value.

For the computation [m_3, B^{(2)}] on CC_3:
  CC_3 has elements a_0 otimes a_1 otimes a_2 otimes a_3 (4 factors)
  m_3 on CC_3: applies m_3 to 3 consecutive factors, giving CC_1
  B^{(2)} on CC_3: contracts a pair, giving CC_1

So [m_3, B^{(2)}] maps CC_3 -> CC_0 = A (via two different routes).

Route 1: m_3 . B^{(2)}: CC_3 -B^{(2)}-> CC_1 -m_3-> impossible
  (m_3 needs 3 inputs, CC_1 has 2 factors)

Hmm, let me reconsider.  m_3 acts on the bar complex as part of the
bar differential.  On B(A) = T^c(sA), the operation m_3 applies to
3 consecutive factors and replaces them with one.

So m_3: CC_n -> CC_{n-2} (replaces 3 factors with 1).
And B^{(2)}: CC_n -> CC_{n-2} (removes 2 factors via pairing).

The commutator [m_3, B^{(2)}]: CC_n -> CC_{n-4}.

For CC_4 (5 factors): [m_3, B^{(2)}]: CC_4 -> CC_0 = A.

For CC_3 (4 factors):
  m_3: CC_3 -> CC_1 (3->1, so 4 factors -> 2 factors)
  B^{(2)}: CC_3 -> CC_1 (4 factors -> 2 factors)

  m_3 . B^{(2)}: CC_3 -> CC_1 -> CC_{-1} = 0  (can't apply m_3 to 2 factors and get fewer than 0)

Actually wait: m_3 on CC_1 (which has 2 factors) cannot apply because
m_3 needs at least 3 inputs.  So m_3 . B^{(2)} = 0 on CC_3.

And B^{(2)} . m_3: CC_3 -> CC_1 -> CC_{-1} = 0.  B^{(2)} on CC_1
(2 factors) contracts both, giving CC_{-1} which is... a scalar.
Actually CC_{-1} doesn't exist (negative cyclic degree).

So [m_3, B^{(2)}] = 0 on CC_3 trivially for degree reasons.

The first nontrivial case is CC_4 (5 factors):
  m_3: CC_4 -> CC_2 (5 -> 3 factors)
  B^{(2)}: CC_4 -> CC_2 (5 -> 3 factors)

  [m_3, B^{(2)}] = m_3 . B^{(2)} - B^{(2)} . m_3: CC_4 -> CC_0 = A

  m_3 . B^{(2)}: CC_4 -B^{(2)}-> CC_2 -m_3-> CC_0
  B^{(2)} . m_3: CC_4 -m_3-> CC_2 -B^{(2)}-> CC_0

This IS the nontrivial computation.

ACTUAL IMPLEMENTATION
======================

We work with the graded vector space A = span{e_0, x_1, x_2, x_3, y_1, y_2, y_3, w}
and compute [m_3, B^{(2)}] on CC_4(A) = A^{otimes 5} explicitly.

The algebra operations:
  mu_2: the cup product (see above)
  mu_3: the Massey product, nonzero only on certain triples of degree-1 elements

The CY_3 pairing:
  <e_0, w> = <w, e_0> = 1
  <x_i, y_j> = <y_j, x_i> = delta_{ij}

B^{(2)} contracts a pair using this pairing.
m_3 applies the ternary operation to 3 consecutive factors.

We compute both compositions and check if they agree.

REFERENCES
==========
  cy_to_chiral.tex: Prop cyclic-ainf-framing-compat, Rem adversarial-audit-cyclic-ainf
  hopf_fibration_s3_framing.py: Obs_Ainf component
  Bridgeland (2005): derived categories of coherent sheaves on CY manifolds
  Aspinwall-Katz (2006): local P^2 and McKay quivers
  Kadeishvili (1980): homotopy transfer theorem
  Costello (2005): TCFTs and CY categories
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, FrozenSet, List, Optional, Sequence, Tuple

F = Fraction


# =========================================================================
#  0. GRADED VECTOR SPACE OF LOCAL P^2
# =========================================================================

@dataclass(frozen=True)
class ExtGenerator:
    """A basis element of the Ext algebra of local P^2.

    The minimal A_infinity model on cohomology has:
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
    r"""The ternary A_infinity operation mu_3(a, b, c).

    mu_3 has degree 2-3 = -1, so |mu_3(a,b,c)| = |a|+|b|+|c|-1.

    For local P^2, the nonzero mu_3 comes from the superpotential
    W = x_1 x_2 x_3 of the McKay quiver, via the homotopy transfer
    theorem (Kadeishvili).

    The only nontrivial mu_3's (up to the A_infinity gauge) are on
    triples of degree-1 elements:

      mu_3(x_i, x_j, x_k): degree 3*1 - 1 = 2, lives in A^2

    Specifically, from the superpotential W = x_1 x_2 x_3:
      mu_3(x_1, x_2, x_3) = y_1   [from partial_1 W = x_2 x_3]
      mu_3(x_2, x_3, x_1) = y_2   [from partial_2 W = x_1 x_3]
      mu_3(x_3, x_1, x_2) = y_3   [from partial_3 W = x_1 x_2]

    The A_infinity sign conventions give:
      mu_3(x_{sigma(1)}, x_{sigma(2)}, x_{sigma(3)}) = sign(sigma) * y_{sigma(1)}

    for even permutations, and antisymmetric for odd permutations.

    Wait -- let me be precise.  The homotopy transfer from the Ginzburg
    DG algebra gives a specific answer.  For the CY_3 quiver with
    potential W, the m_3 on the cohomology algebra is:

      mu_3(x_i, x_j, x_k) = delta_{ijk ~ cyclic perm of 123} * y_i

    More precisely: mu_3 is nonzero only on inputs that form a cyclic
    permutation of (x_1, x_2, x_3), and the output is determined by
    the first input.

    CORRECTED FORMULA (from cyclic invariance + Z_3 symmetry):

    The most general Z_3-symmetric, cyclically invariant m_3 on
    degree-1 triples is:
      mu_3(x_i, x_j, x_k) = alpha * epsilon_{ijk} * y_m  for some y_m

    Cyclic invariance of the CY_3 pairing requires:
      <mu_3(a, b, c), d> = -<a, mu_3(b, c, d)>  (with appropriate sign)

    The simplest model (alpha=1): for each EVEN permutation (i,j,k) of (1,2,3),
      mu_3(x_i, x_j, x_k) = y_i  (indexed by the FIRST entry)

    And for ODD permutations:
      mu_3(x_i, x_j, x_k) = -y_i

    This is equivalent to:
      mu_3(x_i, x_j, x_k) = epsilon_{ijk} * y_i

    But this is NOT graded symmetric in the inputs -- it shouldn't be,
    because mu_3 is NOT (graded) symmetric.

    Let me verify the A_infinity relation at n=3:
      mu_2(mu_2(a,b), c) - mu_2(a, mu_2(b,c)) = mu_1(mu_3(a,b,c)) + ...
    Since mu_1 = 0 on the minimal model:
      mu_2(mu_2(a,b), c) - mu_2(a, mu_2(b,c)) = mu_3(mu_1(a),b,c) + mu_3(a,mu_1(b),c) + ...
    All terms with mu_1 vanish.  So:
      ASSOCIATOR(a,b,c) := mu_2(mu_2(a,b), c) - mu_2(a, mu_2(b,c)) should equal
      d(mu_3(a,b,c)) = 0 on the minimal model.

    Wait, the n=3 A_infinity relation is:
      sum over decompositions: mu_2(mu_2(a,b),c) + mu_2(a,mu_2(b,c))
        + mu_1(mu_3(a,b,c)) + mu_3(mu_1(a),b,c) + mu_3(a,mu_1(b),c)
        + mu_3(a,b,mu_1(c)) = 0

    With mu_1 = 0:
      mu_2(mu_2(a,b),c) + mu_2(a,mu_2(b,c)) = 0

    Hmm, this says mu_2 IS strictly associative on the cohomology.
    But that's the UNDEFORMED A_infinity relation.  Let me reconsider.

    The A_infinity relation at n=3 (with correct signs, following
    Keller's conventions):

      mu_2(mu_2(a,b), c) - mu_2(a, mu_2(b,c)) + mu_1(mu_3(a,b,c))
        + mu_3(mu_1(a), b, c) - mu_3(a, mu_1(b), c) + mu_3(a, b, mu_1(c)) = 0

    With mu_1 = 0 on the minimal model:
      mu_2(mu_2(a,b), c) - mu_2(a, mu_2(b,c)) = 0

    So mu_2 is STRICTLY ASSOCIATIVE on the minimal model, and mu_3 is
    a DEFORMATION, not an associator correction!

    The role of mu_3 is as a HIGHER OPERATION that encodes the homotopy
    type of the original DGA.  The associator of mu_2 on cohomology
    vanishes, but mu_3 records the chain-level homotopy.

    The n=4 relation then involves:
      mu_2(mu_3(...), ...) + mu_3(mu_2(...), ..., ...) + mu_4(...) = 0

    So mu_3 appears in the n=4 A_infinity relation as a genuine
    correction.  The point is that for NON-FORMAL algebras, mu_3 != 0
    even though the ASSOCIATOR of mu_2 vanishes on cohomology.

    For local P^2, the explicit mu_3 from the HTT applied to the
    Ginzburg DG algebra (with potential W = x_1 x_2 x_3) gives:

      mu_3(x_1, x_2, x_3) = w  (the top class)

    Degree check: |mu_3(x_1,x_2,x_3)| = 1+1+1-1 = 2.  But |w| = 3.
    CONTRADICTION.  So mu_3(x_1,x_2,x_3) != w.

    CORRECTED: mu_3(x_1,x_2,x_3) must have degree 2.  The degree-2
    generators are y_1, y_2, y_3.

    The HTT formula: Starting from the Ginzburg DG algebra with:
      - generators a_1, a_2, a_3 (degree 1) for arrows
      - generators a_1*, a_2*, a_3* (degree 2) for dual arrows
      - generator phi (degree 3) for the potential loop
      - differential: d(a_i*) = partial_i W = sum of monomials

    The homotopy transfer to cohomology gives mu_3 from the failure
    of the obvious projection to be a DGA map.  For W = a_1 a_2 a_3:

    d(a_1*) = a_2 a_3
    d(a_2*) = a_1 a_3  (with sign: actually a_3 a_1 or -a_1 a_3)
    d(a_3*) = a_1 a_2

    The transferred mu_3 is (schematically):
      mu_3(x_i, x_j, x_k) = p . h . m_2(m_2(i(x_i), i(x_j)), i(x_k))

    where p = projection, h = contracting homotopy, i = inclusion.

    For the specific case of the exterior algebra (which IS the Ext
    algebra of local P^2), the mu_3 is:

      mu_3(x_i, x_j, x_k) = 0  when any two indices agree
      mu_3(x_1, x_2, x_3) = c * y  for some specific y in A^2 and c != 0

    The Z_3 symmetry of the quiver (cyclic permutation of vertices)
    gives:
      mu_3(x_1, x_2, x_3) = alpha * (y_1 + y_2 + y_3)  [Z_3-invariant]

    Or, breaking the Z_3 to the specific HTT choice of homotopy:
      mu_3(x_1, x_2, x_3) = alpha * y_1

    For our computation, the SPECIFIC CHOICE does not matter for the
    question of whether [m_3, B^{(2)}] = 0 -- we need it to be nonzero,
    and we compute the commutator for a GENERAL mu_3.

    We use the simplest nontrivial model:
      mu_3(x_i, x_j, x_k) = epsilon_{ijk} * y_1  (breaks Z_3 but simplest)

    or the Z_3-symmetric version:
      mu_3(x_1, x_2, x_3) = y_1
      mu_3(x_2, x_3, x_1) = y_2
      mu_3(x_3, x_1, x_2) = y_3
      (odd permutations get a minus sign)

    i.e. mu_3(x_i, x_j, x_k) = sgn(i,j,k) * y_i  for (i,j,k) a perm of (1,2,3).

    Let us verify CYCLIC INVARIANCE of this mu_3:
      <mu_3(x_1, x_2, x_3), a_4> = <y_1, a_4>
    This is nonzero only if a_4 = x_1 (pairing degree 2 with degree 1).
      <y_1, x_1> = 1.  So <mu_3(x_1,x_2,x_3), x_1> = 1.

    Cyclic invariance requires (with sign epsilon_3):
      <mu_3(x_1,x_2,x_3), x_1> = (-1)^{epsilon_3} <x_1, mu_3(x_2,x_3,x_1)>
      = (-1)^{epsilon_3} <x_1, y_2>
      = (-1)^{epsilon_3} * delta_{12} = 0.

    But the LHS is 1 and the RHS is 0.  CONTRADICTION.

    So the formula mu_3(x_i, x_j, x_k) = sgn * y_i does NOT satisfy
    cyclic invariance!

    Let me reconsider.  Cyclic invariance says:
      <mu_3(a_1,a_2,a_3), a_4> = (-1)^{eps} <a_1, mu_3(a_2,a_3,a_4)>

    For this to work with <y_i, x_j> = delta_{ij}, we need:
      LHS: <mu_3(x_1,x_2,x_3), x_k> = <output, x_k>
      RHS: (-1)^eps <x_1, mu_3(x_2,x_3,x_k)>

    For k=1: LHS = <output, x_1>, RHS = (-1)^eps <x_1, mu_3(x_2,x_3,x_1)>
    For k=2: LHS = <output, x_2>, RHS = (-1)^eps <x_1, mu_3(x_2,x_3,x_2)>
    For k=3: LHS = <output, x_3>, RHS = (-1)^eps <x_1, mu_3(x_2,x_3,x_3)>

    k=2: RHS has mu_3(x_2,x_3,x_2) which has two equal indices -> 0
    k=3: RHS has mu_3(x_2,x_3,x_3) which has two equal indices -> 0

    So only k=1 can be nonzero on the RHS:
      RHS = (-1)^eps <x_1, mu_3(x_2,x_3,x_1)>

    mu_3(x_2,x_3,x_1) should be the cyclic permutation of (2,3,1).
    This is an EVEN permutation of (1,2,3), so sign = +1.
    mu_3(x_2,x_3,x_1) = y_2  (in our formula above).
    <x_1, y_2> = delta_{12} = 0.

    So RHS = 0 for all k, meaning LHS must also be 0 for all k.
    But if mu_3(x_1,x_2,x_3) != 0, then <output, x_k> != 0 for some k.

    This means: mu_3(x_1,x_2,x_3) must pair to zero with ALL x_k.
    So mu_3(x_1,x_2,x_3) must be orthogonal to all of A^1 = {x_1,x_2,x_3}.

    But the degree-2 space A^2 = {y_1,y_2,y_3} pairs ONLY with A^1
    via <y_i, x_j> = delta_{ij}.  So being orthogonal to all x_k means
    mu_3(x_1,x_2,x_3) = 0.

    WAIT.  This would mean mu_3 = 0 on degree-1 triples.  But local P^2
    is NON-FORMAL, so mu_3 != 0.  What's going on?

    The resolution: mu_3 is nonzero on MIXED-DEGREE inputs.

    mu_3 has degree -1, so:
      mu_3(A^1, A^1, A^1) -> A^2: as we just showed, must be 0 by cyclic inv.
      mu_3(A^0, A^1, A^1) -> A^1: degree 0+1+1-1 = 1. Possible!
      mu_3(A^1, A^0, A^1) -> A^1: possible.
      mu_3(A^1, A^1, A^0) -> A^1: possible.
      mu_3(A^0, A^0, A^1) -> A^0: degree 0+0+1-1 = 0. Possible.
      etc.

    But e is the UNIT, and A_infinity units satisfy:
      mu_n(a_1,...,e,...,a_n) = 0 for n >= 3

    (strict unitality of the minimal model).  So any mu_3 with e as
    an input vanishes.

    Then we're left with: mu_3 on pure degree-1 triples must be zero.

    The non-formality of local P^2 must come from mu_3 on triples
    involving HIGHER-DEGREE inputs (degree 1 and 2 mixed), or from mu_4.

    Let me reconsider the degree analysis:
      mu_3(A^1, A^1, A^2): degree 1+1+2-1 = 3, output in A^3 = span{w}.
      mu_3(A^1, A^2, A^1): degree 1+2+1-1 = 3, output in A^3 = span{w}.
      mu_3(A^2, A^1, A^1): degree 2+1+1-1 = 3, output in A^3 = span{w}.

    These are possible! And the cyclic invariance test:
      <mu_3(x_i, x_j, y_k), e_0> = ... (pairing with the unit)
    Since <w, e> = 1, mu_3(x_i, x_j, y_k) = alpha * w gives
      <alpha * w, e> = alpha.

    Cyclic invariance:
      <mu_3(x_i, x_j, y_k), e> = (-1)^eps <x_i, mu_3(x_j, y_k, e)>
    But mu_3(..., e, ...) = 0 (strict unitality for n>=3).

    Hmm, that gives RHS = 0 but LHS = alpha.  So alpha = 0 again?

    No -- the cyclic invariance identity uses (n+1) elements cyclically:
      <mu_3(a_1, a_2, a_3), a_4>

    For a_1=x_i, a_2=x_j, a_3=y_k, a_4 must have degree 0 (to pair with
    degree 3 output w).  So a_4 = e.  Then:

    RHS = (-1)^eps <x_i, mu_3(x_j, y_k, e)> = 0 (unitality).

    So LHS = 0, meaning mu_3(x_i, x_j, y_k) = 0.

    Similarly, mu_3(x_i, y_j, x_k) = 0 and mu_3(y_i, x_j, x_k) = 0.

    What about mu_3(y_i, y_j, x_k)? Degree: 2+2+1-1 = 4 > 3. Zero.

    So ALL mu_3 on the augmentation ideal vanish, because:
      - Pure degree-1 triples: forced to 0 by cyclic invariance
      - Mixed degree (1,1,2), (1,2,1), (2,1,1): forced to 0 by cyclic + unitality
      - Higher degree: zero for degree reasons

    This seems to say mu_3 = 0 on the MINIMAL model of local P^2!

    But local P^2 IS non-formal. The resolution:

    The non-formality appears at the level of mu_4 (or higher), not mu_3.
    Or: the non-formality is visible in the DGA model but not in the
    cohomology algebra with the transferred structure.

    Actually, let me reconsider.  The Ext algebra of local P^2 is
    NOT the exterior algebra (1+t)^3.  The exterior algebra is the
    Ext algebra of P^2 itself (the compact surface).  For LOCAL P^2
    = Tot(O(-3) -> P^2), the relevant algebra is different.

    For the derived category of local P^2, we should consider the
    Ext algebra of the EXCEPTIONAL COLLECTION, not just a single sheaf.
    The exceptional collection is {O, O(1), O(2)}, and the total Ext
    algebra is a 3x3 matrix of Ext groups.

    For the ONE-OBJECT model (Ext*(O, O)):
      Ext^0(O, O) = C (identity)
      Ext^1(O, O) = H^1(O) = 0 (for P^2, H^1 = 0!)
      Ext^2(O, O) = H^2(O) = C (by Serre duality... wait)

    For P^2: H^0(P^2, O) = C, H^1(P^2, O) = 0, H^2(P^2, O) = 0.
    So Ext^*(O, O) = C in degree 0 only!  This is formal.

    The non-formality comes from the FULL exceptional collection.
    The relevant A_infinity CATEGORY has objects {O, O(1), O(2)} and
    the mu_3 maps are between DIFFERENT Hom-spaces.

    For the commutator computation, we should work with the
    A_infinity CATEGORY, not a single algebra.  But for the bar complex
    and cyclic complex, we can use the TOTAL Ext algebra
      A = End(O ⊕ O(1) ⊕ O(2))
    which is a 3-object A_infinity category collapsed to a single algebra
    (with idempotents).

    Actually, for a CY category the relevant invariant is the
    Hochschild complex, which is Morita-invariant.  So we can use
    any generator.

    Let me reconsider the model.  For the GINZBURG DG ALGEBRA of the
    McKay quiver of Z_3 (which is the model for local P^2):

    Quiver Q: 3 vertices {0, 1, 2}, arrows:
      a_{ij}: i -> j for each pair (corresponding to the 3 coordinate directions)
    With potential W = a_{01} a_{12} a_{20} + cyclic.

    The Ginzburg algebra has:
      Degree 0: paths in Q (including idempotents e_0, e_1, e_2)
      Degree 1: arrows a_{ij}  (9 of them: 3 loops + 6 between vertices)
      Degree 2: dual arrows a_{ij}^*
      Degree 3: vertex loops phi_i

    The COHOMOLOGY of the Ginzburg algebra (= the Ext algebra of the
    quiver category) is:
      H^0 = path algebra / (relations from W) = Jacobi algebra Jac(Q, W)

    For the Z_3 McKay quiver with CY potential:
      Jac(Q, W) is infinite-dimensional (this is a CY_3 algebra).

    So the cohomology is NOT finite-dimensional, and the "8-dimensional"
    model I was using is WRONG.

    THE CORRECT MODEL: we should use a COMPACT object in the CY_3 category,
    whose Ext algebra IS finite-dimensional.

    For local P^2, the compact objects are the coherent sheaves on P^2
    (supported on the zero section).  The Ext algebra of the structure
    sheaf O_{P^2} (as a sheaf on the total space of O(-3)):

      Ext^i_{local P^2}(O_{P^2}, O_{P^2}) = H^i(P^2, O_{P^2}) for i <= 2
      plus contributions from the normal bundle O(-3).

    Actually, by Koszul duality, Ext*(O_{P^2}, O_{P^2}) as a module
    over the local P^2 is:
      = Ext*(O_{P^2}, O_{P^2}) computed in D^b(Tot(O(-3) -> P^2))

    Using the Koszul resolution of O_{P^2} as a sheaf on the total space:
      0 -> O(-3)[-1] -> O -> O_{P^2} -> 0

    gives Ext^*(O_{P^2}, O_{P^2}) = H^*(P^2, O) ⊕ H^*(P^2, O(3))[1]
    = C ⊕ C^{10}[1] ... this is getting complicated.

    Let me use a SIMPLER MODEL.  The key point is:

    For a CYCLIC A_infinity algebra of dimension 3 with mu_3 != 0,
    does [m_3, B^{(2)}] = 0?

    We don't need the specific model of local P^2.  We need ANY
    cyclic A_infinity algebra of CY dimension 3 with nontrivial mu_3.

    The SIMPLEST such algebra is:

    A = span{a, b} with |a| = 1, |b| = 2.
    CY_3 pairing: <a, b> = 1, <b, a> = 1.
    mu_1 = 0, mu_2 = 0 (no binary product on the augmentation ideal).
    mu_3(a, a, a) = c * b for some c.  Degree: 3*1 - 1 = 2 = |b|. OK.

    Cyclic invariance check:
      <mu_3(a,a,a), a> = c * <b, a> = c
      (-1)^eps <a, mu_3(a,a,a)> = (-1)^eps * c * <a, b> = (-1)^eps * c

    The sign: eps = 3 + |a|(|a|+|a|+|a|) = 3 + 1*3 = 6.  (-1)^6 = 1.
    So cyclic invariance gives c = c.  SATISFIED for any c.

    But this algebra has dim(A) = 2 with augmentation bar{A} = A
    (no unit... we need a unit).

    Let me add the unit and the top:
    A = span{e, a, b, w} with |e|=0, |a|=1, |b|=2, |w|=3.
    Pairing: <e, w> = <w, e> = 1, <a, b> = <b, a> = 1.
    mu_2(e, -) = id, mu_2(-, e) = id (unit).
    mu_2(a, a) = 0 (degree 2, but only b is there... actually mu_2(a,a) COULD be b).

    Wait, let me think about this differently.  For a 1-dimensional CY_3
    example (augmentation ideal has generators in degrees 1 and 2 only):

    A = span{e, a, b, w}, |e|=0, |a|=1, |b|=2, |w|=3.
    mu_2(a, a) = 0 or nonzero?

    If mu_2(a,a) = lambda * b for some lambda:
      mu_2(a,a) has degree 2. mu_2(a,b) has degree 3, so mu_2(a,b) = mu * w.
      mu_2(b,a) = (-1)^{1*2} mu_2(a,b) = mu * w.
      mu_2(b,b) has degree 4 > 3, so = 0.
      mu_2(a,w) has degree 4 > 3, so = 0.

    Let me take lambda = 0 (no binary product) to isolate the mu_3 effect.

    Then:
      mu_2 = 0 on augmentation ideal (except unit maps).
      mu_3(a, a, a) = c * b, c != 0.
      mu_3(a, a, b) has degree 1+1+2-1 = 3, so mu_3(a,a,b) = d * w.

    Cyclic invariance for mu_3(a,a,b) with fourth input e:
      <mu_3(a,a,b), e> = d * <w, e> = d
      (-1)^eps <a, mu_3(a,b,e)> = (-1)^eps <a, 0> = 0  (unitality: mu_3(...,e) = 0)

    So d = 0.  mu_3(a,a,b) = 0.

    Similarly mu_3(a,b,a) = 0 and mu_3(b,a,a) = 0.

    So the only nontrivial mu_3 is mu_3(a,a,a) = c * b.

    Now we have a MINIMAL example: A = {e, a, b, w} with:
      CY_3 pairing: <e,w>=<w,e>=1, <a,b>=<b,a>=1.
      mu_2 = 0 on bar(A).
      mu_3(a,a,a) = c * b (c = 1 WLOG).
      All other mu_n = 0 for n >= 4 (we can check the A_infinity relations).

    THE A_INFINITY RELATIONS:
    n=1: mu_1^2 = 0. OK (mu_1 = 0).
    n=2: mu_1.mu_2 + mu_2.(mu_1 x 1 + 1 x mu_1) = 0. OK.
    n=3: mu_2(mu_2(a,a),a) - mu_2(a,mu_2(a,a)) + mu_1(mu_3(a,a,a)) = 0
         = mu_2(0,a) - mu_2(a,0) + 0 = 0. OK.
    n=4: mu_2(mu_3(a,a,a),a) + mu_3(mu_2(a,a),a,a) - mu_3(a,mu_2(a,a),a)
         + mu_3(a,a,mu_2(a,a)) + mu_2(a,mu_3(a,a,a)) + mu_4(...) + mu_1.mu_4 = 0
         = mu_2(b,a) + 0 + 0 + 0 + mu_2(a,b) + 0
         = mu_2(b,a) + mu_2(a,b)

    mu_2(b,a) = 0 (we said mu_2 = 0 on augmentation ideal, except through unit).
    Actually wait: I set mu_2 = 0 on the augmentation ideal, which includes
    mu_2(b,a) = 0 and mu_2(a,b) = 0.  Then the n=4 relation gives 0 = 0. OK.

    But wait: mu_2(a,b) should perhaps be nonzero.  In the CY_3 algebra,
    the product a * b could be w (degree 1+2=3).  Let me keep mu_2(a,b) = mu * w.

    Then n=4 with inputs (a,a,a,a):
      mu_2(mu_3(a,a,a),a) + mu_2(a,mu_3(a,a,a)) = mu_2(b,a) + mu_2(a,b)
      = mu * w + mu * w = 2*mu*w

    For this to vanish (assuming mu_4 = 0), we need mu = 0.
    So mu_2(a,b) = 0 is FORCED by the A_infinity relations when mu_3(a,a,a) = b.

    Great.  So the model is self-consistent with mu_2 = 0 on bar(A).

    NOW THE COMPUTATION
    ====================

    We compute [m_3, B^{(2)}] on CC_n for this minimal cyclic A_infinity algebra.

    Augmentation ideal bar(A) = span{a, b, w}.  (Or maybe just {a, b}?  w = ab = 0
    so w is not generated by products, but it IS in the augmentation ideal.)

    The cyclic bar complex:
      CC_n(A) has elements [a_0 | a_1 | ... | a_n] with a_i in bar(A),
      modulo cyclic rotation.

    For the commutator [m_3, B^{(2)}]:
      m_3 acts on 3 consecutive factors, replacing them with one: CC_n -> CC_{n-2}.
      B^{(2)} contracts a pair via the pairing: CC_n -> CC_{n-2}.

    Both reduce the cyclic bar degree by 2.  Their commutator:
      [m_3, B^{(2)}] = m_3 . B^{(2)} - B^{(2)} . m_3: CC_n -> CC_{n-4}

    First nontrivial case: CC_4 -> CC_0 = A (or rather bar(A)).

    CC_4 elements: [a_0|a_1|a_2|a_3|a_4] with a_i in {a, b, w}.

    For the computation to be nontrivial, we need B^{(2)} to be nonzero.
    B^{(2)} contracts a pair using <-,->:
      <a, b> = 1 (degrees 1+2=3=d). NONZERO!
      <b, a> = 1.
      <a, a> = 0 (degrees 1+1=2 != 3).
      <b, b> = 0 (degrees 2+2=4 != 3).

    So B^{(2)} only contracts (a,b) or (b,a) pairs.

    Now let's compute on CC_4:

    Take the element [a|a|a|a|b] (cyclic class).  This has 5 factors.

    Route 1: B^{(2)} first, then m_3.
      B^{(2)}([a|a|a|a|b]): contract all pairs (i,j) with <a_i,a_j> != 0.
      The only nonzero pairing pairs are where one is a and one is b.
      Factor 4 is b, all others are a.
      Nonzero contractions: (i,4) for i=0,1,2,3 where a_i=a and a_4=b.
      <a, b> = 1 for each.

      Contraction (0,4): remove positions 0 and 4, remaining [a|a|a] = CC_2.
        Sign: (-1)^{sum of degrees before position 0 * ... } -- need to be careful.
      Contraction (1,4): remove positions 1 and 4, remaining [a|a|a] = CC_2.
      Contraction (2,4): remaining [a|a|a] = CC_2.
      Contraction (3,4): remaining [a|a|a] = CC_2.

      In the CYCLIC bar complex, all of these give the same class [a|a|a].
      So B^{(2)}([a|a|a|a|b]) = 4 * sgn * [a|a|a]  (up to signs).

      Then m_3([a|a|a]) = m_3 applied to 3 consecutive factors of [a|a|a]:
      m_3(a,a,a) = b.  In CC_2 -> CC_0:
      There are 3 cyclic positions to apply m_3 to a 3-factor element:
        m_3 on positions (0,1,2): m_3(a,a,a) = b, giving [b] in CC_0.
      Since CC_2 has 3 factors and m_3 takes 3 inputs to 1 output, we get CC_0.

      Result of route 1: some multiple of [b].

    Route 2: m_3 first, then B^{(2)}.
      m_3 on CC_4 = [a|a|a|a|b] (5 factors):
      Apply m_3 to each set of 3 consecutive factors (cyclically):
        (0,1,2): m_3(a,a,a) = b -> [b|a|b] in CC_2.  WAIT: positions 0,1,2 give
          m_3(a,a,a) = b, remaining factors a_3=a, a_4=b.  So [b|a|b].
        (1,2,3): m_3(a,a,a) = b -> [a|b|b] which cyclically = [b|b|a].
        (2,3,4): m_3(a,a,b) = 0 (as we showed above). -> 0.
        (3,4,0): m_3(a,b,a) = 0. -> 0.
        (4,0,1): m_3(b,a,a) = 0. -> 0.

      So m_3([a|a|a|a|b]) = sgn_1 [b|a|b] + sgn_2 [b|b|a].

      Now B^{(2)} on [b|a|b]:
        Pairs: (0,1): <b,a>=1 -> remove, get [b] in CC_0.
               (0,2): <b,b>=0.
               (1,2): <a,b>=1 -> remove, get [b] in CC_0.
        So B^{(2)}([b|a|b]) = sgn * [b] + sgn' * [b] = some_coeff * [b].

      And B^{(2)} on [b|b|a]:
        Pairs: (0,1): <b,b>=0.
               (0,2): <b,a>=1 -> remove, get [b] in CC_0.
               (1,2): <b,a>=1 -> remove, get [b] in CC_0.
        So B^{(2)}([b|b|a]) = some_coeff * [b].

      Result of route 2: some multiple of [b].

    The COMMUTATOR [m_3, B^{(2)}]([a|a|a|a|b]) = route 1 - route 2 = ? * [b].

    If this is zero, the gap is closed.  If nonzero, the gap is real.

    THE KEY QUESTION IS WHETHER THE COEFFICIENTS MATCH.

    We need to compute ALL the Koszul signs carefully.

    THIS IS WHAT THE ENGINE DOES.
    """
    # Strict unitality: mu_3(anything with unit) = 0
    if a == e or b == e or c == e:
        return []

    out_degree = a.degree + b.degree + c.degree - 1

    # Output degree must be in {0, 1, 2, 3}
    if out_degree < 0 or out_degree > 3:
        return []

    # The only nontrivial mu_3 on the minimal model is:
    # mu_3(a, a, a) = b (in the 4-element model)
    # For the 8-element P^2 model: mu_3 is trivially zero by cyclic invariance
    # (as shown in the docstring analysis above).

    # For the GENERAL model, we parametrize by a constant ALPHA:
    # mu_3(a, a, a) = ALPHA * b
    # All other mu_3 = 0 (forced by cyclic invariance + unitality).

    # This function uses the 4-element model {e, a, b, w} only.
    # See make_mu_3() for the parametrized version.
    return []  # placeholder; actual computation via the engine below


# =========================================================================
#  4. THE MINIMAL CYCLIC A_INFINITY CY_3 ALGEBRA
# =========================================================================

@dataclass
class MinimalCyclicCY3:
    """A minimal cyclic A_infinity algebra of CY dimension 3.

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
    alpha != 0 gives the non-formal case.

    This is the simplest cyclic A_infinity algebra with nontrivial mu_3
    that satisfies all A_infinity relations AND cyclic invariance.
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
    r"""Apply B^{(2)} to a bar element.

    B^{(2)} contracts a pair of factors using the CY_3 pairing:

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
    BarLinComb : the result of applying B^{(2)}.
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
    """Apply B^{(2)} to a linear combination of bar elements."""
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
    r"""Compute [m_3, B^{(2)}](elem) = (m_3 . B^{(2)} - B^{(2)} . m_3)(elem).

    This is the central computation of the module.  It measures the
    A_infinity obstruction Obs_Ainf for the cyclic A_infinity algebra.

    Parameters
    ----------
    elem : BarElement
        Input bar element.
    alg : MinimalCyclicCY3
        The cyclic A_infinity algebra.

    Returns
    -------
    BarLinComb : the commutator [m_3, B^{(2)}] applied to elem.
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
    r"""Compute [m_3, B^{(2)}] on ALL elements of CC_4.

    CC_4(A) consists of bar elements [a_0|a_1|a_2|a_3|a_4] with
    a_i in aug(A) = {a, b, w}.

    The computation checks whether the commutator vanishes identically
    on CC_4, which is the first nontrivial bar degree.

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
    r"""Compute [m_3, B^{(2)}] on CC_5 (6-fold tensors).

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
    r"""Detailed computation of [m_3, B^{(2)}] on [a|a|a|a|b].

    This is the KEY element where m_3 and B^{(2)} both act nontrivially:
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
    r"""Master computation of Obs_Ainf for the minimal CY_3 algebra.

    Computes [m_3, B^{(2)}] exhaustively on CC_4 and CC_5, with
    detailed breakdowns of key elements.

    Parameters
    ----------
    alpha : Fraction
        The mu_3 coefficient: mu_3(a,a,a) = alpha * b.
        alpha = 0: formal case (commutator trivially zero).
        alpha != 0: non-formal case (the interesting case).

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
      - 'obs_ainf_vanishes': the VERDICT
      - 'gap_status': "CLOSED" or "REAL"
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

    # Verdict
    obs_vanishes = cc4["commutator_vanishes"] and cc5["commutator_vanishes"]

    return {
        "alpha": alpha,
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
        "obs_ainf_vanishes": obs_vanishes,
        "gap_status": "CLOSED" if obs_vanishes else "REAL",
    }


# =========================================================================
#  12. EXTENDED MODEL: 8-GENERATOR EXTERIOR ALGEBRA
# =========================================================================

@dataclass
class ExtendedCyclicCY3:
    """The 8-generator model A = Lambda(V) with dim V = 3.

    A = span{e, x_1, x_2, x_3, y_1, y_2, y_3, w}
    with |e|=0, |x_i|=1, |y_i|=2, |w|=3.

    Product: exterior algebra (x_i x_j = -x_j x_i, x_i^2 = 0).
    CY_3 pairing: Serre duality.

    For this algebra, mu_3 = 0 on the cohomology by the cyclic invariance
    argument (see the analysis in the mu_3 docstring).  The non-formality
    of local P^2 appears at the CATEGORY level (multiple objects), not
    at the single-object algebra level.

    However, we can ARTIFICIALLY add a mu_3 that violates cyclic invariance
    to see what happens (testing tool).

    Or: we work with the 4-generator minimal model where mu_3 IS nonzero
    and cyclically invariant.
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

        For the true local P^2 model on cohomology (8 generators),
        cyclic invariance forces mu_3 = 0 on the augmentation ideal.
        This function returns 0 accordingly.
        """
        return []

    def verify_8gen_mu3_forced_zero(self) -> Dict[str, Any]:
        """Demonstrate that mu_3 = 0 is forced on the 8-generator model.

        For each triple (x_i, x_j, x_k) of degree-1 elements, cyclic
        invariance with the Serre pairing forces the output to be zero.

        This is the key observation: on the cohomology H^*(P^2) = Lambda^*(V),
        the Serre pairing is too constraining for any nonzero mu_3 to exist.

        The non-formality of local P^2 must therefore be encoded differently:
        either in the CATEGORY (multi-object) level, or in higher mu_n (n >= 4),
        or in a DIFFERENT choice of generating object.
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
    r"""Complete analysis of the [m_3, B^{(2)}] commutator.

    Runs the master computation on the minimal CY_3 algebra and
    provides the verdict on whether Obs_Ainf = 0.

    Returns the full analysis including:
    - The minimal model computation (4 generators, alpha=1)
    - The 8-generator model analysis (forced mu_3 = 0)
    - Cross-checks for alpha = 0 (formal, trivial) and alpha = 2
    - The verdict on AP-CY34
    """
    # Formal case: alpha = 0 (trivial)
    formal = master_obs_ainf_computation(alpha=F(0))

    # Non-formal case: alpha = 1
    nonformal_1 = master_obs_ainf_computation(alpha=F(1))

    # Non-formal case: alpha = 2 (check universality)
    nonformal_2 = master_obs_ainf_computation(alpha=F(2))

    # 8-generator model: mu_3 forced to zero
    ext_model = ExtendedCyclicCY3()
    ext_analysis = ext_model.verify_8gen_mu3_forced_zero()

    return {
        "formal_case": {
            "alpha": 0,
            "obs_vanishes": formal["obs_ainf_vanishes"],
            "gap_status": formal["gap_status"],
        },
        "nonformal_alpha1": {
            "alpha": 1,
            "cyclic_invariance_ok": nonformal_1["cyclic_invariance_ok"],
            "ainf_relations_ok": nonformal_1["ainf_relations_ok"],
            "cc4_vanishes": nonformal_1["cc4_result"]["vanishes"],
            "cc4_nonzero": nonformal_1["cc4_result"]["num_nonzero"],
            "cc5_vanishes": nonformal_1["cc5_result"]["vanishes"],
            "cc5_nonzero": nonformal_1["cc5_result"]["num_nonzero"],
            "obs_vanishes": nonformal_1["obs_ainf_vanishes"],
            "gap_status": nonformal_1["gap_status"],
            "key_aaaab": nonformal_1["key_aaaab"],
            "key_aabaa": nonformal_1["key_aabaa"],
        },
        "nonformal_alpha2": {
            "alpha": 2,
            "obs_vanishes": nonformal_2["obs_ainf_vanishes"],
            "gap_status": nonformal_2["gap_status"],
        },
        "extended_8gen_model": ext_analysis,
        "verdict": {
            "obs_ainf_vanishes_formal": formal["obs_ainf_vanishes"],
            "obs_ainf_vanishes_nonformal": nonformal_1["obs_ainf_vanishes"],
            "gap_status": nonformal_1["gap_status"],
            "explanation": (
                "The commutator [m_3, B^{(2)}] is computed exhaustively "
                "on CC_4 and CC_5 for the minimal cyclic A_infinity CY_3 "
                "algebra with mu_3(a,a,a) = alpha * b.  The result determines "
                "whether Obs_Ainf = 0 (gap CLOSED) or Obs_Ainf != 0 (gap REAL)."
            ),
        },
    }
