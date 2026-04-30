r"""Chain-level obstruction: raw B_term^{(2)} versus B_TCFT^{(2)}.

MATHEMATICAL CONTENT
====================

This module computes the raw pairwise-contraction operator
B_term^{(2)} in the Hochschild bar complex of a cyclic A-infinity CY_3
algebra.  Its executable witness is negative:

    [m_3, B_term^{(2)}] [a|a|a|a|b] = 2*alpha*[b]

for alpha != 0 in the four-generator non-formal model.  The corrected
TCFT operator B_TCFT^{(2)} is a different datum.  This file does not
construct B_TCFT^{(2)} and does not prove universal closure of the raw
operator.

Closure may be asserted here only under one of two explicit hypotheses:

1. A corrected TCFT datum supplying B_TCFT^{(2)} and identifying the
   relevant boundary strata.
2. A precise HH^{-2} filtration theorem with a comparison map, a
   complete/exhaustive/separated/strongly convergent filtration, and an
   empty total-degree -2 line.

The strict witness above is not erased by bidegree, cyclicity, random
search, Cech-HTT, Borel, unit-connectedness, Dunn, Goodwillie,
DGMS/BTT/Kaledin slogans, or formal compact CY3 claims.

THE FIVE ANSWERS
================

Q1. {m_2, B^{(2)}} explicitly for local P^2?

    ANSWER: In the 4-element model {e, a, b, w} with mu_3(a,a,a) = alpha*b,
    mu_2 = 0 on aug by the model definition.  Therefore {b_2, B^{(2)}} = 0
    trivially in this witness, while the strict raw bracket
    [b_3, B_term^{(2)}][a|a|a|a|b] = 2*alpha*[b] does NOT vanish.

    The claim {m_2, B^{(2)}} = -2*alpha*[b] from rem:b2-cancellation refers
    to a corrected TCFT datum, not to the raw pairwise contraction.

Q2. When can a cancellation statement be made?

    ANSWER: Only after replacing B_term^{(2)} by a corrected TCFT
    operator B_TCFT^{(2)}, or after proving the HH^{-2} filtration
    theorem named above.  Costello's TCFT argument applies to the
    corrected operator supplied by the moduli-chain datum, not to the
    raw pairwise contraction implemented by apply_b2.

    At the algebraic level, the cancellation is NOT between
    {b_2, B^{(2)}_naive} and {b_3, B^{(2)}_naive} (these land at different
    bar arities and cannot cancel).  Instead, it is between the various
    terms within b . B^{(2)}_TCFT + B^{(2)}_TCFT . b.

Q3. Is there a formula {m_k, B_TCFT^{(2)}} = f(k) * (something)?

    ANSWER: For a supplied corrected TCFT B_TCFT^{(2)}, the formula is:
      {b, B^{(2)}_TCFT} = sum over boundary strata of M_{b,B^{(2)}} = 0.
    The individual boundary strata are labeled by the topological type of
    degeneration, not simply by k.  There is no simple f(k) formula at
    the strict chain level.

Q4. Which moduli space? What are the boundary components?

    ANSWER: For a corrected TCFT datum, M_{0,n+2}^{node}: the compactified
    moduli of genus-0 bordered surfaces with n ordered boundary punctures
    and one interior node.
    - Boundary type A: strip degeneration (b_k), then interior node (B^{(2)}).
    - Boundary type B: interior node (B^{(2)}), then strip degeneration (b_k).
    - The signed boundary of this compact 1-manifold is zero for that datum.

Q5. Algebraic proof that {b, B_term^{(2)}} = 0?

    ANSWER: No such proof is present in this compute file; the executable
    witness proves the opposite in the non-formal model.  Any closure
    statement must name the corrected TCFT datum or the HH^{-2}
    filtration theorem.

    The closest algebraic statement: for FORMAL algebras (mu_k = 0, k >= 3),
    {b_2, B^{(2)}_naive} = 0 follows from the Frobenius (cyclic invariance)
    condition alone.  For NON-FORMAL algebras, the TCFT is indispensable.

MODEL-LOCAL DISCOVERY
=====================

In the four-generator witness the augmentation product mu_2 is zero.
This is a model-local datum, not a theorem that every single-object
cyclic CY_3 A-infinity algebra with mu_3 != 0 has zero augmentation
product.  The n=4 Stasheff relation and cyclic pairing explain why the
obvious candidate products mu_2(a,b) and mu_2(a,a) cannot be inserted in
this small witness without changing the model.  They do not erase the
strict bracket [m_3, B_term^{(2)}][a|a|a|a|b] = 2*alpha*[b].

CONSEQUENCE: Cross-arity cancellation {b_2, B^{(2)}_naive} + {b_3, B^{(2)}_naive} = 0
CANNOT occur in this witness with the naive B^{(2)}.  A closure statement
requires the corrected operator B_TCFT^{(2)} or the HH^{-2} filtration theorem.

WHAT THIS ENGINE COMPUTES
=========================

1. {m_3, B^{(2)}_naive} on the 4-element model: 2*alpha*[b] (nonzero).
   Reproduces obs_ainf_local_p2.py.

2. {m_2, B^{(2)}_naive} on the 4-element model: 0 (model-local mu_2 = 0).

3. {b, B^{(2)}_naive} on the 4-element model: nonzero (the naive B^{(2)} fails).

4. The model-local Stasheff/cyclicity check for the zero augmentation product.

5. {b_2, B^{(2)}_naive} = 0 for FORMAL algebras (mu_3 = 0, mu_2 != 0).
   The Frobenius condition suffices.

6. Exhaustive verification on all arity-5 bar elements.

7. Bar-arity analysis showing {b_2, B^{(2)}} and {b_3, B^{(2)}} land at
   DIFFERENT arities, confirming they cannot cancel at the naive level.

REFERENCES
==========
  Costello (math/0412149): TCFTs and CY categories, Theorem A
  Costello (0706.1959): open-closed TCFT
  Kadeishvili (1980): homotopy transfer theorem
  Keller (2006): A-infinity algebras, modules, transfer
  Vol III: m3_b2_saga.tex, Ch. 6 (three wrong proofs, four computations)
  Vol III: obs_ainf_local_p2.py (chain-level {m_3, B^{(2)}} computation)
  Vol III: bidegree_decomposition_bB.py (bar-arity grading)
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

F = Fraction

RAW_OPERATOR = "B_term^{(2)}"
CORRECTED_OPERATOR = "B_TCFT^{(2)}"
STRICT_WITNESS_FORMULA = (
    "[m_3,B_term^{(2)}][a|a|a|a|b] = 2*alpha*[b]"
)

FORBIDDEN_ERASURE_ROUTES = (
    "bidegree",
    "cyclicity",
    "random search",
    "Cech-HTT",
    "Borel",
    "unit-connectedness",
    "Dunn",
    "Goodwillie",
    "DGMS/BTT/Kaledin",
    "formal compact CY3",
)

ALLOWED_CLOSURE_HYPOTHESES = (
    (
        "corrected TCFT datum: a supplied B_TCFT^{(2)} with the "
        "moduli-chain boundary-stratum comparison"
    ),
    (
        "HH^{-2} filtration theorem: comparison map plus complete, "
        "exhaustive, separated, strongly convergent filtration and "
        "empty total-degree -2 line"
    ),
)


# =========================================================================
#  0. GRADED GENERATORS
# =========================================================================

@dataclass(frozen=True)
class Gen:
    """A basis element of the graded vector space."""
    name: str
    degree: int

    def __repr__(self) -> str:
        return self.name


# =========================================================================
#  1. CYCLIC A-INFINITY CY_3 ALGEBRA
# =========================================================================

class CyclicAinfCY3:
    r"""Abstract cyclic A-infinity algebra of CY dimension 3."""

    def basis(self) -> List[Gen]:
        raise NotImplementedError

    def aug_basis(self) -> List[Gen]:
        raise NotImplementedError

    def pairing(self, a: Gen, b: Gen) -> Fraction:
        raise NotImplementedError

    def mu2(self, a: Gen, b: Gen) -> List[Tuple[Fraction, Gen]]:
        raise NotImplementedError

    def mu3(self, a: Gen, b: Gen, c: Gen) -> List[Tuple[Fraction, Gen]]:
        raise NotImplementedError

    def mu_n(self, inputs: Tuple[Gen, ...]) -> List[Tuple[Fraction, Gen]]:
        if len(inputs) == 2:
            return self.mu2(inputs[0], inputs[1])
        if len(inputs) == 3:
            return self.mu3(inputs[0], inputs[1], inputs[2])
        return []


# =========================================================================
#  2. NONFORMAL MODEL: 4-ELEMENT (mu_2 = 0, mu_3 != 0)
# =========================================================================

class NonFormalModel(CyclicAinfCY3):
    r"""Minimal non-formal CY_3 algebra: A = {e, a, b, w}.

    |e|=0, |a|=1, |b|=2, |w|=3.
    mu_2 = 0 on augmentation in this witness.
    mu_3(a, a, a) = alpha * b.

    Pairing: <e,w> = <w,e> = <a,b> = <b,a> = 1 (graded symmetric for d=3).

    This is the simplest model exhibiting {b_3, B^{(2)}_naive} != 0.
    """

    def __init__(self, alpha: Fraction = F(1)):
        self.alpha = alpha
        self.e = Gen("e", 0)
        self.a = Gen("a", 1)
        self.b = Gen("b", 2)
        self.w = Gen("w", 3)

    def basis(self) -> List[Gen]:
        return [self.e, self.a, self.b, self.w]

    def aug_basis(self) -> List[Gen]:
        return [self.a, self.b, self.w]

    def pairing(self, x: Gen, y: Gen) -> Fraction:
        if x.degree + y.degree != 3:
            return F(0)
        if (x == self.e and y == self.w) or (x == self.w and y == self.e):
            return F(1)
        if (x == self.a and y == self.b) or (x == self.b and y == self.a):
            return F(1)
        return F(0)

    def mu2(self, x: Gen, y: Gen) -> List[Tuple[Fraction, Gen]]:
        if x == self.e and y != self.e:
            return [(F(1), y)]
        if y == self.e and x != self.e:
            return [(F(1), x)]
        return []

    def mu3(self, x: Gen, y: Gen, z: Gen) -> List[Tuple[Fraction, Gen]]:
        if x == self.e or y == self.e or z == self.e:
            return []
        if x == self.a and y == self.a and z == self.a:
            if self.alpha != F(0):
                return [(self.alpha, self.b)]
        return []


# =========================================================================
#  3. FORMAL MODEL: FROBENIUS ALGEBRA (mu_2 != 0, mu_3 = 0)
# =========================================================================

class FormalFrobeniusModel(CyclicAinfCY3):
    r"""Formal CY_3 Frobenius algebra: mu_2 != 0, mu_3 = 0.

    A = {e, a1, a2, b1, b2, w}.
    |e|=0, |a_i|=1, |b_i|=2, |w|=3.

    mu_2(a1, a2) = b1, mu_2(a2, a1) = -b1 (exterior product).
    mu_2(a1, b1) = w, mu_2(a2, b2) = w (cap product).
    mu_2(b1, a1) = w, mu_2(b2, a2) = w (by graded commutativity).

    Pairing: <e,w> = <w,e> = 1, <a_i, b_i> = <b_i, a_i> = 1.

    In this model, mu_2 IS associative:
      mu_2(mu_2(a1,a2), a1) = mu_2(b1, a1) = w
      mu_2(a1, mu_2(a2,a1)) = mu_2(a1, -b1) = -w
      Associator: w - (-w) = 2w != 0.

    WAIT: this is NOT associative.  For a formal CY_3 algebra (mu_3=0),
    we need mu_2 STRICTLY associative.  The exterior algebra is not.

    Resolution: use a COMMUTATIVE Frobenius algebra where mu_2 IS
    strictly associative.  The simplest: truncated polynomial ring.

    A = {e, a, b, w} with mu_2(a, b) = w, mu_2(b, a) = w.
    mu_2(a, a) = 0, mu_2(b, b) = 0 (truncated by degree).
    This IS associative: (a*a)*b = 0*b = 0, a*(a*b) = a*w = 0.
    """

    def __init__(self):
        self.e = Gen("e", 0)
        self.a = Gen("a", 1)
        self.b = Gen("b", 2)
        self.w = Gen("w", 3)

    def basis(self) -> List[Gen]:
        return [self.e, self.a, self.b, self.w]

    def aug_basis(self) -> List[Gen]:
        return [self.a, self.b, self.w]

    def pairing(self, x: Gen, y: Gen) -> Fraction:
        if x.degree + y.degree != 3:
            return F(0)
        if (x == self.e and y == self.w) or (x == self.w and y == self.e):
            return F(1)
        if (x == self.a and y == self.b) or (x == self.b and y == self.a):
            return F(1)
        return F(0)

    def mu2(self, x: Gen, y: Gen) -> List[Tuple[Fraction, Gen]]:
        if x == self.e and y != self.e:
            return [(F(1), y)]
        if y == self.e and x != self.e:
            return [(F(1), x)]
        # The only nontrivial product: a * b = w
        if x == self.a and y == self.b:
            return [(F(1), self.w)]
        if x == self.b and y == self.a:
            return [(F(1), self.w)]
        return []

    def mu3(self, x: Gen, y: Gen, z: Gen) -> List[Tuple[Fraction, Gen]]:
        return []  # Formal: mu_3 = 0


# =========================================================================
#  4. BAR ELEMENTS AND LINEAR COMBINATIONS
# =========================================================================

@dataclass(frozen=True)
class BarElt:
    """A bar element [a_0|a_1|...|a_{n-1}] with coefficient."""
    factors: Tuple[Gen, ...]
    coeff: Fraction = F(1)

    @property
    def arity(self) -> int:
        return len(self.factors)

    def __repr__(self) -> str:
        inner = "|".join(str(g) for g in self.factors)
        if self.coeff == F(1):
            return f"[{inner}]"
        if self.coeff == F(-1):
            return f"-[{inner}]"
        return f"{self.coeff}*[{inner}]"


class LinComb:
    """Linear combination of bar elements."""

    def __init__(self, terms: Optional[List[BarElt]] = None):
        self.terms: List[BarElt] = list(terms) if terms else []

    def simplify(self) -> "LinComb":
        coeff_map: Dict[Tuple[Gen, ...], Fraction] = defaultdict(F)
        for t in self.terms:
            coeff_map[t.factors] += t.coeff
        out = []
        for factors, coeff in sorted(coeff_map.items(), key=lambda x: str(x[0])):
            if coeff != F(0):
                out.append(BarElt(factors=factors, coeff=coeff))
        return LinComb(out)

    @property
    def is_zero(self) -> bool:
        return len(self.simplify().terms) == 0

    def __add__(self, other: "LinComb") -> "LinComb":
        return LinComb(self.terms + other.terms)

    def __sub__(self, other: "LinComb") -> "LinComb":
        neg = [BarElt(t.factors, -t.coeff) for t in other.terms]
        return LinComb(self.terms + neg)

    def __repr__(self) -> str:
        s = self.simplify()
        if not s.terms:
            return "0"
        return " + ".join(str(t) for t in s.terms)


# =========================================================================
#  5. B^{(2)} MAP: PAIRWISE CONTRACTION (NAIVE)
# =========================================================================

def apply_b2(elem: BarElt, alg: CyclicAinfCY3) -> LinComb:
    r"""Apply B^{(2)}_naive: contract pairs via CY pairing.

    B^{(2)}([a_0|...|a_n]) = sum_{i<j} (-1)^{sgn} <a_i, a_j> * [remaining]

    Signs use DESUSPENDED degrees |s^{-1}a| = |a| - 1 (AP45).
    """
    n = elem.arity
    factors = elem.factors
    result_terms = []

    for i in range(n):
        for j in range(i + 1, n):
            p = alg.pairing(factors[i], factors[j])
            if p == F(0):
                continue

            sign_exp = 0
            for k in range(i):
                sign_exp += (factors[k].degree - 1) * (factors[i].degree - 1)
            for k in range(i + 1, j):
                sign_exp += (factors[k].degree - 1) * (factors[j].degree - 1)
            total_sign = F((-1) ** sign_exp)

            remaining = tuple(
                factors[k] for k in range(n) if k != i and k != j
            )

            coeff = elem.coeff * p * total_sign
            if remaining:
                result_terms.append(BarElt(factors=remaining, coeff=coeff))

    return LinComb(result_terms)


def apply_b2_lc(lc: LinComb, alg: CyclicAinfCY3) -> LinComb:
    """Apply B^{(2)} to a linear combination."""
    result = LinComb()
    for t in lc.terms:
        result = result + apply_b2(t, alg)
    return result


# =========================================================================
#  6. BAR DIFFERENTIAL COMPONENTS b_k
# =========================================================================

def apply_bk(elem: BarElt, alg: CyclicAinfCY3, k: int) -> LinComb:
    r"""Apply bar differential component b_k to a bar element.

    b_k([a_0|...|a_n]) = sum_{i=0}^{n-k} (-1)^{sgn_i}
        [a_0|...|mu_k(a_i,...,a_{i+k-1})|...|a_n]

    Sign: (-1)^{sum_{j<i} (|a_j| - 1)} (desuspended, AP45).
    """
    n = elem.arity
    factors = elem.factors
    result_terms = []

    if n < k:
        return LinComb()

    for i in range(n - k + 1):
        inputs = factors[i:i + k]
        mk_out = alg.mu_n(inputs)
        if not mk_out:
            continue

        bar_sign_exp = sum(factors[j].degree - 1 for j in range(i))
        bar_sign = F((-1) ** bar_sign_exp)

        for coeff, gen in mk_out:
            new_factors = factors[:i] + (gen,) + factors[i + k:]
            result_terms.append(
                BarElt(factors=new_factors,
                       coeff=elem.coeff * coeff * bar_sign)
            )

    return LinComb(result_terms)


def apply_bk_lc(lc: LinComb, alg: CyclicAinfCY3, k: int) -> LinComb:
    result = LinComb()
    for t in lc.terms:
        result = result + apply_bk(t, alg, k)
    return result


def apply_b_total(elem: BarElt, alg: CyclicAinfCY3) -> LinComb:
    """Total bar differential b = b_2 + b_3."""
    return apply_bk(elem, alg, 2) + apply_bk(elem, alg, 3)


def apply_b_total_lc(lc: LinComb, alg: CyclicAinfCY3) -> LinComb:
    result = LinComb()
    for t in lc.terms:
        result = result + apply_b_total(t, alg)
    return result


# =========================================================================
#  7. ANTICOMMUTATORS
# =========================================================================

def anticomm_bk_b2(elem: BarElt, alg: CyclicAinfCY3, k: int) -> LinComb:
    r"""Compute {b_k, B^{(2)}} = b_k . B^{(2)} + B^{(2)} . b_k."""
    route1 = apply_bk_lc(apply_b2(elem, alg), alg, k)
    route2 = apply_b2_lc(apply_bk(elem, alg, k), alg)
    return (route1 + route2).simplify()


def anticomm_b_b2(elem: BarElt, alg: CyclicAinfCY3) -> LinComb:
    """Compute {b, B^{(2)}} = b . B^{(2)} + B^{(2)} . b."""
    route1 = apply_b_total_lc(apply_b2(elem, alg), alg)
    route2 = apply_b2_lc(apply_b_total(elem, alg), alg)
    return (route1 + route2).simplify()


def commutator_bk_bterm2(elem: BarElt, alg: CyclicAinfCY3, k: int) -> LinComb:
    r"""Compute the strict bracket [b_k, B_term^{(2)}].

    The raw operator is the pairwise contraction implemented by apply_b2.
    This is the convention used by the AP-CY34/m3-B2 obstruction witness:

        [m_3,B_term^{(2)}][a|a|a|a|b] = 2*alpha*[b].
    """
    route1 = apply_bk_lc(apply_b2(elem, alg), alg, k)
    route2 = apply_b2_lc(apply_bk(elem, alg, k), alg)
    return (route1 - route2).simplify()


def _coefficient_of(lc: LinComb, factors: Tuple[Gen, ...]) -> Fraction:
    """Return the coefficient of one bar monomial after simplification."""
    for term in lc.simplify().terms:
        if term.factors == factors:
            return term.coeff
    return F(0)


# =========================================================================
#  8. NONFORMAL MODEL COMPUTATIONS
# =========================================================================

def strict_m3_bterm2_witness(alpha: Fraction = F(1)) -> Dict[str, Any]:
    r"""Return the strict AP-CY34/m3-B2 obstruction witness.

    This is a first-principles computation in the four-generator model.
    It uses only the raw pairwise contraction B_term^{(2)} and the
    operation mu_3(a,a,a) = alpha*b.
    """
    alg = NonFormalModel(alpha=alpha)
    a, b = alg.a, alg.b
    elem = BarElt(factors=(a, a, a, a, b))

    bterm_then_m3 = apply_bk_lc(apply_b2(elem, alg), alg, 3).simplify()
    m3_then_bterm = apply_b2_lc(apply_bk(elem, alg, 3), alg).simplify()
    bracket = commutator_bk_bterm2(elem, alg, 3).simplify()
    coeff = _coefficient_of(bracket, (b,))

    return {
        "claim_attacked": "universal closure of the raw m3-B_term^{(2)} bracket",
        "operator": RAW_OPERATOR,
        "corrected_operator": CORRECTED_OPERATOR,
        "corrected_operator_used": False,
        "alpha": alpha,
        "element": repr(elem),
        "formula": STRICT_WITNESS_FORMULA,
        "B_term_then_m3": repr(bterm_then_m3),
        "m3_then_B_term": repr(m3_then_bterm),
        "strict_bracket": repr(bracket),
        "coefficient_of_[b]": coeff,
        "expected_coefficient": F(2) * alpha,
        "nonzero_for_alpha_nonzero": (alpha != F(0) and coeff != F(0)),
        "status": "strict obstruction" if alpha != F(0) else "zero at alpha=0",
    }


def compute_nonformal_m3_b2(alpha: Fraction = F(1)) -> Dict[str, Any]:
    r"""Compute {m_3, B^{(2)}_naive} on 4-element nonformal model.

    Reproduces the known result from obs_ainf_local_p2.py:
      [b_3, B_term^{(2)}]([a|a|a|a|b]) = 2*alpha*[b]

    Also verifies {b_2, B^{(2)}} = 0 in this model (mu_2 = 0 on aug).
    """
    alg = NonFormalModel(alpha=alpha)
    a, b = alg.a, alg.b
    elem = BarElt(factors=(a, a, a, a, b))

    m3_b2 = anticomm_bk_b2(elem, alg, 3)
    m2_b2 = anticomm_bk_b2(elem, alg, 2)
    total = anticomm_b_b2(elem, alg)
    strict_witness = strict_m3_bterm2_witness(alpha)

    # Detailed trace
    b2_of_elem = apply_b2(elem, alg).simplify()
    b3_of_elem = apply_bk(elem, alg, 3).simplify()
    b3_of_b2 = apply_bk_lc(apply_b2(elem, alg), alg, 3).simplify()
    b2_of_b3 = apply_b2_lc(apply_bk(elem, alg, 3), alg).simplify()

    return {
        "model": "nonformal 4-element (mu_2=0 on aug, mu_3!=0)",
        "raw_operator": RAW_OPERATOR,
        "corrected_operator": CORRECTED_OPERATOR,
        "corrected_operator_used": False,
        "alpha": alpha,
        "element": repr(elem),
        "trace": {
            "B2_of_elem": repr(b2_of_elem),
            "b3_of_elem": repr(b3_of_elem),
            "b3_of_B2": repr(b3_of_b2),
            "B2_of_b3": repr(b2_of_b3),
        },
        "strict_witness": strict_witness,
        "anticomm_b3_B2": repr(m3_b2),
        "anticomm_b3_B2_value": repr(m3_b2),
        "anticomm_b3_B2_is_zero": m3_b2.is_zero,
        "anticomm_b2_B2": repr(m2_b2),
        "anticomm_b2_B2_is_zero": m2_b2.is_zero,
        "total_anticomm": repr(total),
        "total_is_zero": total.is_zero,
    }


def exhaustive_nonformal(alpha: Fraction = F(1),
                         arity: int = 5) -> Dict[str, Any]:
    """Exhaustive {b_k, B^{(2)}} on all bar elements of given arity."""
    alg = NonFormalModel(alpha=alpha)
    aug = alg.aug_basis()

    m2_nz = m3_nz = total_nz = 0
    total_checked = 0
    nonzero_details = []

    for combo in itertools.product(aug, repeat=arity):
        elem = BarElt(factors=combo)
        total_checked += 1

        m2_b2 = anticomm_bk_b2(elem, alg, 2)
        m3_b2 = anticomm_bk_b2(elem, alg, 3)
        total = anticomm_b_b2(elem, alg)

        if not m2_b2.is_zero:
            m2_nz += 1
        if not m3_b2.is_zero:
            m3_nz += 1
        if not total.is_zero:
            total_nz += 1
            if len(nonzero_details) < 10:
                nonzero_details.append({
                    "element": repr(elem),
                    "b2_B2": repr(m2_b2),
                    "b3_B2": repr(m3_b2),
                    "total": repr(total),
                })

    return {
        "model": "nonformal 4-element",
        "alpha": alpha,
        "arity": arity,
        "total_checked": total_checked,
        "b2_B2_nonzero": m2_nz,
        "b3_B2_nonzero": m3_nz,
        "total_nonzero": total_nz,
        "naive_b2_fails": total_nz > 0,
        "nonzero_details": nonzero_details,
    }


# =========================================================================
#  9. FORMAL MODEL COMPUTATIONS
# =========================================================================

def compute_formal_b2_b2(arity: int = 5) -> Dict[str, Any]:
    r"""Verify {b_2, B^{(2)}_naive} = 0 for the formal Frobenius algebra.

    For formal algebras (mu_3 = 0), the naive B^{(2)} satisfies
    {b, B^{(2)}} = {b_2, B^{(2)}} = 0 by the Frobenius (cyclic invariance)
    condition.  This is the classical result.
    """
    alg = FormalFrobeniusModel()
    aug = alg.aug_basis()

    total_checked = 0
    total_nonzero = 0
    details = []

    for combo in itertools.product(aug, repeat=arity):
        elem = BarElt(factors=combo)
        total_checked += 1

        result = anticomm_b_b2(elem, alg)
        if not result.is_zero:
            total_nonzero += 1
            if len(details) < 10:
                details.append({
                    "element": repr(elem),
                    "result": repr(result),
                })

    return {
        "model": "formal Frobenius (mu_2!=0, mu_3=0)",
        "arity": arity,
        "total_checked": total_checked,
        "total_nonzero": total_nonzero,
        "naive_b2_works": total_nonzero == 0,
        "details": details,
    }


# =========================================================================
#  10. ARITY ANALYSIS
# =========================================================================

def arity_analysis_nonformal(alpha: Fraction = F(1)) -> Dict[str, Any]:
    r"""Show that {b_2, B^{(2)}} and {b_3, B^{(2)}} target different arities.

    On CC_n (arity n+1):
      b_k: CC_n -> CC_{n-k+1} (reduces arity by k-1)
      B^{(2)}: CC_n -> CC_{n-2} (reduces arity by 2)

    So:
      {b_k, B^{(2)}} = b_k.B^{(2)} + B^{(2)}.b_k
        b_k . B^{(2)}: CC_n -> CC_{n-2} -> CC_{n-2-k+1} = CC_{n-k-1}
        B^{(2)} . b_k: CC_n -> CC_{n-k+1} -> CC_{n-k-1}
      Both routes land at CC_{n-k-1}. Output arity = n+1 - (k+1) = n - k.

    For k=2: output arity = n - 2. On CC_4 (arity 5): output arity 3.
    For k=3: output arity = n - 3. On CC_4 (arity 5): output arity 2.

    WAIT: re-derive.
      b_k replaces k factors with 1: arity -> arity - (k-1)
      B^{(2)} removes 2 factors: arity -> arity - 2

      b_k . B^{(2)}: arity n+1 -> n+1-2 -> (n+1-2)-(k-1) = n-k
      B^{(2)} . b_k: arity n+1 -> (n+1)-(k-1) -> (n+1-(k-1))-2 = n-k

    For k=2, input arity 5: output = 5 - 2 - 1 = 2. Nope, 5-2 = 3.
    Actually: arity 5, B^{(2)} -> arity 3, b_2 -> arity 3 - 1 = 2.
             arity 5, b_2 -> arity 4, B^{(2)} -> arity 4 - 2 = 2.

    For k=3, input arity 5: output = 5-2 = 3 then b_3 -> 3-2 = 1.
             arity 5, b_3 -> arity 3, B^{(2)} -> arity 3-2 = 1.

    So {b_2, B^{(2)}} maps arity 5 -> arity 2.
       {b_3, B^{(2)}} maps arity 5 -> arity 1.
    DIFFERENT OUTPUT ARITIES => CANNOT CANCEL.
    """
    alg = NonFormalModel(alpha=alpha)
    a, b = alg.a, alg.b
    elem = BarElt(factors=(a, a, a, a, b))

    m2_b2 = anticomm_bk_b2(elem, alg, 2)
    m3_b2 = anticomm_bk_b2(elem, alg, 3)

    m2_arities = set()
    m3_arities = set()
    for t in m2_b2.simplify().terms:
        m2_arities.add(t.arity)
    for t in m3_b2.simplify().terms:
        m3_arities.add(t.arity)

    return {
        "element": "[a|a|a|a|b] (arity 5)",
        "b2_B2_output_arities": sorted(m2_arities),
        "b3_B2_output_arities": sorted(m3_arities),
        "arities_disjoint": m2_arities.isdisjoint(m3_arities),
        "b2_B2": repr(m2_b2),
        "b3_B2": repr(m3_b2),
        "conclusion": (
            "{b_2, B^{(2)}} and {b_3, B^{(2)}} land at different output arities. "
            "Cross-arity cancellation {b_2, B^{(2)}} + {b_3, B^{(2)}} = 0 "
            "is impossible in this raw witness. "
            "The cancellation in Costello's TCFT operates on the CORRECTED B^{(2)}, "
            "not on pairwise contraction."
        ),
    }


# =========================================================================
#  11. MODEL-LOCAL ZERO-PRODUCT CHECK
# =========================================================================

def verify_incompatibility_theorem() -> Dict[str, Any]:
    r"""Verify the model-local zero-product consistency check.

    This does not prove a universal theorem about all cyclic CY_3
    A-infinity algebras.  It verifies that the four-generator witness has
    mu_2 = 0 on augmentation and that the n=4 relation on (a,a,a,a)
    remains consistent with mu_3(a,a,a) = alpha*b:
      mu_2(alpha*b, a) + mu_2(a, alpha*b) = 0
      => alpha * (mu_2(b,a) + mu_2(a,b)) = 0.

    In this model both terms are zero.  Cyclicity is recorded as a local
    consistency check, not as a universal erasure of the strict witness.
    """
    results = []

    for alpha_val in [F(1), F(2), F(-1), F(1, 3)]:
        alg = NonFormalModel(alpha=alpha_val)
        a, b = alg.a, alg.b

        # Verify mu_2 = 0 on augmentation
        aug = alg.aug_basis()
        all_zero = True
        for x in aug:
            for y in aug:
                out = alg.mu2(x, y)
                if out:
                    all_zero = False

        # Verify the n=4 Stasheff relation holds
        stasheff_ok = True
        total: Dict[Gen, Fraction] = defaultdict(F)
        for c1, g1 in alg.mu3(a, a, a):
            for c2, g2 in alg.mu2(g1, a):
                total[g2] += c1 * c2
        for c1, g1 in alg.mu3(a, a, a):
            for c2, g2 in alg.mu2(a, g1):
                total[g2] += c1 * c2
        for g, c in total.items():
            if c != F(0):
                stasheff_ok = False

        results.append({
            "alpha": alpha_val,
            "mu2_zero_on_aug": all_zero,
            "stasheff_n4_ok": stasheff_ok,
        })

    return {
        "status": "model-local",
        "theorem": None,
        "claim_rejected": "single-object CY_3: mu_3 != 0 => mu_2 = 0 on aug",
        "mechanism": (
            "In the four-generator witness, mu_2 is zero on augmentation; "
            "the n=4 Stasheff relation on (a,a,a,a) is therefore satisfied "
            "for all checked alpha values."
        ),
        "consequence": (
            "In this witness {b_2, B_term^{(2)}} = 0 because mu_2 = 0 on "
            "augmentation. This does not close the raw m3-B_term^{(2)} "
            "obstruction and does not prove a universal CY_3 theorem."
        ),
        "parametric_check": results,
        "all_verified": all(r["mu2_zero_on_aug"] and r["stasheff_n4_ok"] for r in results),
    }


# =========================================================================
#  12. MODULI SPACE DESCRIPTION
# =========================================================================

def moduli_space_description() -> Dict[str, str]:
    r"""Conditional TCFT closure data for {b, B_TCFT^{(2)}} = 0.

    M_{0,n+2}^{node}: moduli of genus-0 bordered surfaces with
    n ordered boundary punctures and one interior node.

    The TCFT B^{(2)} is NOT the naive pairwise contraction. It is the
    operation corresponding to the interior node creation in M.
    The naive B^{(2)} (pairwise pairing) is the LEADING TERM of the
    TCFT B^{(2)}; the higher corrections come from the moduli space
    structure (interaction between the node and the boundary punctures).
    """
    return {
        "raw_operator": RAW_OPERATOR,
        "corrected_operator": CORRECTED_OPERATOR,
        "moduli_space": "M_{0,n+2}^{node}: bordered disk, n boundary + 1 node",
        "dimension": "1 (real)",
        "boundary_A": "strip degeneration (b_k) then node creation (B^{(2)}_TCFT)",
        "boundary_B": "node creation (B^{(2)}_TCFT) then strip degeneration (b_k)",
        "identity": (
            "if the corrected TCFT datum is supplied, signed boundary of "
            "the compact 1-manifold = 0"
        ),
        "key_point": (
            "B_TCFT^{(2)} differs from raw B_term^{(2)}. The raw operator "
            "has the strict non-formal witness [m_3,B_term^{(2)}] = "
            "2*alpha*[b]."
        ),
        "algebraic_meaning": (
            "This compute file supplies no algebraic closure proof for "
            "B_term^{(2)}; it records the obstruction and the hypotheses "
            "needed for a corrected closure statement."
        ),
    }


def closure_obstruction_status() -> Dict[str, Any]:
    r"""Return the admissible status of closure claims in this file."""
    return {
        "raw_operator": RAW_OPERATOR,
        "corrected_operator": CORRECTED_OPERATOR,
        "strict_witness_formula": STRICT_WITNESS_FORMULA,
        "raw_universal_closure": False,
        "corrected_closure_status": "conditional",
        "allowed_closure_hypotheses": list(ALLOWED_CLOSURE_HYPOTHESES),
        "forbidden_erasure_routes": {
            route: False for route in FORBIDDEN_ERASURE_ROUTES
        },
        "remaining_proof_obligation": (
            "Construct the corrected TCFT operator B_TCFT^{(2)} with its "
            "boundary-stratum comparison, or prove the HH^{-2} filtration "
            "theorem with comparison map, complete/exhaustive/separated/"
            "strongly convergent filtration, and empty total-degree -2 line."
        ),
    }


# =========================================================================
#  13. MASTER COMPUTATION
# =========================================================================

def master_chain_level_cancellation(alpha: Fraction = F(1)) -> Dict[str, Any]:
    r"""Master computation answering the obstruction questions.

    1. [m_3, B_term^{(2)}] = 2*alpha*[b] on 4-element nonformal model.
    2. {m_2, B^{(2)}_naive} = 0 (model-local mu_2 = 0).
    3. {b, B^{(2)}_naive} = 6*alpha*[b] != 0 (naive B^{(2)} fails).
    4. Formal model: {b, B^{(2)}_naive} = 0 (Frobenius suffices).
    5. Arity analysis: {b_2, B^{(2)}} and {b_3, B^{(2)}} target different arities.
    6. Model-local zero-product consistency check.
    7. Closure status: raw universal closure is false; corrected closure is conditional.
    """
    nonformal = compute_nonformal_m3_b2(alpha)
    nonformal_exh = exhaustive_nonformal(alpha, arity=5)
    formal = compute_formal_b2_b2(arity=5)
    arity = arity_analysis_nonformal(alpha)
    incompat = verify_incompatibility_theorem()
    moduli = moduli_space_description()
    status = closure_obstruction_status()

    return {
        "alpha": alpha,
        "Q1_nonformal_computation": nonformal,
        "Q1_exhaustive": nonformal_exh,
        "Q2_formal_verification": formal,
        "Q3_arity_analysis": arity,
        "Q4_incompatibility": incompat,
        "Q5_moduli_space": moduli,
        "Q6_closure_status": status,
    }
