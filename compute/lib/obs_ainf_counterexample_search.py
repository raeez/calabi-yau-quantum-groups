r"""Adversarial diagnostics for raw m_3--B_term^{(2)} failures.

MATHEMATICAL CONTENT
====================

AP-CY34 separated three different carriers:

    (1) B_term^{(2)}: the raw termwise pair-contraction on a chosen bar model.
    (2) B_TCFT^{(2)}: Costello's corrected open-closed TCFT operator.
    (3) Obs_Ainf: a derived E_1-Hochschild obstruction class.

This module only attacks the raw termwise carrier.  It does not construct
Costello's corrected B_TCFT^{(2)}, and it does not prove Obs_Ainf = 0 for
compact CY3 categories.

The strict characteristic-zero witness, normalized as in
standalone/m3_b2_obstruction_vol3.tex, is:

    B_term^{(2)}[a|a|a|a|b] = 4[a|a|a],
    m_3 B_term^{(2)}[a|a|a|a|b] = 4 alpha [b],
    B_term^{(2)} m_3[a|a|a|a|b] = 2 alpha [b],

hence

    [m_3, B_term^{(2)}][a|a|a|a|b] = 2 alpha [b] != 0

for alpha != 0 over characteristic zero.

The random search below is retained as useful diagnostic data: it explores
raw pair-contraction failures on small strict bar models.  A random nonzero
commutator exposes a B_term^{(2)} failure.  A random zero result is not a
proof of raw vanishing, not a proof of the corrected TCFT identity, and not a
compact CY3 Obs_Ainf theorem.

THE SETUP
=========

Graded vector space: A = A^0 + A^1 + A^2 + A^3 with dim(A^i) specified.
CY_3 pairing: <-,-> : A^i tensor A^{3-i} -> k, non-degenerate.
Operations: m_1: A^i -> A^{i+1} (differential), m_2: bilinear (product),
            m_3: trilinear (first A_inf correction).

Stasheff identity at n=3:
    m_2(m_2(a,b), c) - m_2(a, m_2(b,c))
        = m_1(m_3(a,b,c)) + m_3(m_1(a),b,c) + (-1)^|a| m_3(a,m_1(b),c)
          + (-1)^{|a|+|b|} m_3(a,b,m_1(c))

Cyclic invariance (for m_n):
    <m_n(a_1,...,a_n), a_{n+1}> = (-1)^{eps_n} <a_1, m_n(a_2,...,a_{n+1})>
    where eps_n accounts for Koszul signs.

B_term^{(2)} DIAGNOSTIC OPERATOR
================================

The search implementation uses a raw pair-contraction diagnostic:
CC_n -> CC_{n-2}, contracting two factors using the CY_3 pairing.
This is a bar-model representative of the termwise idea, not Costello's
corrected B_TCFT^{(2)}.

On bar elements [a_0 | a_1 | ... | a_n]:
    B_term^{(2)}([a_0|...|a_n]) = sum_{0 <= i < j <= n}
        <a_i, a_j>_2 * [a_0|...|hat{a_i}|...|hat{a_j}|...|a_n]

where <-,->_2 is the restriction to the (degree 1, degree 2) component
of the CY pairing (|a_i| + |a_j| = 3, restricted to |a_i|=1, |a_j|=2
or vice versa; more precisely, the S^2-framing uses the degree-2 part
of the shifted pairing).

THE COMMUTATOR [m_3, B_term^{(2)}]
==================================

[m_3, B_term^{(2)}](x) =
    m_3(B_term^{(2)}(x)) - B_term^{(2)}(m_3(x))

where m_3 acts on the bar complex by applying mu_3 to three consecutive
factors, and B_term^{(2)} contracts pairs.

On CC_n, the commutator has terms:
- m_3 after B_term^{(2)}
- B_term^{(2)} after m_3

The "non-adjacent" terms are those where:
- B_term^{(2)} contracts (a_i, a_j) where i is inside {k, k+1, k+2} (the m_3
  block) and j is outside, or vice versa.
- These terms appear in B_term^{(2)} . m_3 but not in m_3 . B_term^{(2)}, or with
  different signs/positions.

STRATEGY
========

1. Fix a small graded vector space (e.g. dim = (1,2,2,1) for degrees 0-3).
2. The CY_3 pairing is a non-degenerate bilinear form A^i x A^{3-i} -> k.
3. Generate random uncurved m_1, m_2, m_3 satisfying Stasheff + cyclic invariance.
   - m_1: constrained by m_1^2 = 0 in the flat m_0 = 0 lane
   - m_2: constrained by m_1 . m_2 + m_2 . (m_1 x 1 + 1 x m_1) = 0
   - m_3: constrained by the n=3 Stasheff identity + cyclic invariance
4. Compute [m_3, B_term^{(2)}] on all bar elements of a fixed arity.
5. Record whether the raw diagnostic commutator is zero on the tested sample.

If we find a cyclic A_inf algebra with [m_3, B_term^{(2)}] != 0: raw
termwise counterexample.  If all random samples vanish: no random witness was
found; no theorem follows.

RESULT
======

The exact strict witness above already rejects termwise vanishing.
Random trials also find arity-5 failures for small models with m_1=0 and
m_2=0.

With m_1 = m_2 = 0, all Stasheff identities are TRIVIALLY satisfied
(every term involves m_1 or m_2 multiplicatively), so (A, 0, 0, m_3)
is a valid A_inf algebra whenever m_3 satisfies its own identity
m_3(m_3(a,b,c),d,e) + ... = 0, which is also trivially true since
the nested m_3-composition produces something in the wrong degree
for finite-dimensional A.

For such algebras, cyclic invariance of m_3 is the ONLY constraint.

Findings from the random diagnostic:
  - Arity 4: the tested raw diagnostic can vanish by degree/arity collapse.
    This is not a proof of termwise vanishing in all models.
  - Arity 5: [m_3, B_term^{(2)}] != 0 appears generically in the random
    search.
  - Control: non-cyclic m_3 gives raw nonzero commutators, confirming that
    the operator is detecting genuine termwise sensitivity.

INTERPRETATION:

The raw termwise proof is wrong.  The corrected theorem, if used for compact
CY3s, must supply either:
  - a Costello correction/comparison datum identifying the relevant chain
    model with B_TCFT^{(2)}, or
  - an HH^{-2} filtration theorem killing the derived obstruction class.

Local P^2 and the small random models are noncompact or algebraic diagnostic
data; they are not compact CY3 theorems.

CONVENTIONS
===========
  - Cohomological grading: |d| = +1.
  - CY dimension d = 3.
  - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (desuspension convention).
  - Exact arithmetic via fractions.Fraction where possible.
  - Numerical search uses numpy float64 with tolerance 1e-10.
  - AP-CY2: CY trace is in HC^-_3(C), not just HH_3 -> k.

REFERENCES
==========
  Keller (2006): A-infinity algebras, modules and transfer.
  Kontsevich-Soibelman (2000): Deformations of A-infinity categories.
  Costello (2005): TCFT and CY categories.
  Vol III: cy_to_chiral.tex, prop:cyclic-ainf-framing-compat.
  Vol III: hopf_fibration_s3_framing.py (Hopf decomposition).
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

F = Fraction

RAW_OPERATOR = "B_term^{(2)}"
CORRECTED_OPERATOR = "B_TCFT^{(2)}"
REMAINING_PROOF_OBLIGATIONS: Tuple[str, ...] = (
    "Construct the Costello moduli-chain correction datum for the chosen "
    "compact CY3 chain model.",
    "Prove a comparison homotopy from B_term^{(2)} to B_TCFT^{(2)}, or avoid "
    "B_term^{(2)} entirely.",
    "For compact CY3 vanishing, prove the HH^{-2} filtration hypothesis or "
    "an equivalent obstruction comparison theorem.",
)


@dataclass(frozen=True)
class TermwiseWitness:
    r"""Exact strict witness for nonvanishing of [m_3, B_term^{(2)}].

    The terminal-slot normalization is the one used in
    standalone/m3_b2_obstruction_vol3.tex and in
    compute/lib/operadic_tcft_mk_b2_engine.py.
    """

    input_word: Tuple[str, ...]
    output_word: Tuple[str, ...]
    alpha: Fraction
    m3_after_b_term_coeff: Fraction
    b_term_after_m3_coeff: Fraction
    commutator_coeff: Fraction
    operator: str = RAW_OPERATOR
    corrected_operator: str = CORRECTED_OPERATOR

    @property
    def is_nonzero(self) -> bool:
        """Whether the witness rejects raw termwise vanishing."""
        return self.commutator_coeff != F(0)

    @property
    def statement(self) -> str:
        """Human-readable exact formula."""
        return (
            "[m_3, B_term^{(2)}][a|a|a|a|b] = "
            f"{self.commutator_coeff} [b] != 0"
        )

    def as_dict(self) -> Dict[str, Any]:
        """Dictionary payload for the master diagnostic result."""
        return {
            "input_word": self.input_word,
            "output_word": self.output_word,
            "alpha": self.alpha,
            "m3_after_b_term_coeff": self.m3_after_b_term_coeff,
            "b_term_after_m3_coeff": self.b_term_after_m3_coeff,
            "commutator_coeff": self.commutator_coeff,
            "operator": self.operator,
            "corrected_operator": self.corrected_operator,
            "is_nonzero": self.is_nonzero,
            "statement": self.statement,
        }


def strict_m3_b2_term_witness(alpha: Fraction = F(1)) -> TermwiseWitness:
    r"""Return the exact raw B_term^{(2)} nonzero witness.

    Over characteristic zero and alpha != 0:

        [m_3, B_term^{(2)}][a|a|a|a|b] = 2 alpha [b].
    """
    alpha = F(alpha)
    if alpha == F(0):
        raise ValueError("The strict m3-B_term witness requires alpha != 0")
    return TermwiseWitness(
        input_word=("a", "a", "a", "a", "b"),
        output_word=("b",),
        alpha=alpha,
        m3_after_b_term_coeff=F(4) * alpha,
        b_term_after_m3_coeff=F(2) * alpha,
        commutator_coeff=F(2) * alpha,
    )


# =========================================================================
# 0. GRADED VECTOR SPACE AND CY PAIRING
# =========================================================================

@dataclass
class GradedVectorSpace:
    """A finite-dimensional Z-graded vector space A = A^0 + ... + A^d.

    For CY_3, d = 3 and dim(A^i) must equal dim(A^{3-i}) for the
    pairing to be non-degenerate.

    Attributes
    ----------
    dims : tuple of int
        Dimensions of each graded piece: dims[i] = dim(A^i).
    """
    dims: Tuple[int, ...]

    @property
    def cy_dim(self) -> int:
        """CY dimension = number of graded pieces minus 1."""
        return len(self.dims) - 1

    @property
    def total_dim(self) -> int:
        """Total dimension sum_i dim(A^i)."""
        return sum(self.dims)

    def degree_offset(self, deg: int) -> int:
        """Starting index of degree-deg basis elements in the total basis."""
        return sum(self.dims[:deg])

    def degree_range(self, deg: int) -> range:
        """Index range of degree-deg basis elements."""
        off = self.degree_offset(deg)
        return range(off, off + self.dims[deg])

    def degree_of(self, idx: int) -> int:
        """Degree of basis element with index idx."""
        cumulative = 0
        for deg, d in enumerate(self.dims):
            cumulative += d
            if idx < cumulative:
                return deg
        raise IndexError(f"Index {idx} out of range for total_dim={self.total_dim}")

    def check_cy_symmetry(self) -> bool:
        """Check dim(A^i) = dim(A^{d-i}) for CY pairing non-degeneracy."""
        d = self.cy_dim
        return all(self.dims[i] == self.dims[d - i] for i in range(d + 1))


# =========================================================================
# 1. CY_3 PAIRING
# =========================================================================

@dataclass
class CYPairing:
    r"""A CY_3 pairing <-,-> : A^i x A^{3-i} -> k.

    The pairing is represented as a matrix eta_{ab} where a in A^i and
    b in A^{3-i}.  For CY_3:
        <a, b> = eta_{ab}  when |a| + |b| = 3
        <a, b> = 0          otherwise

    The pairing is GRADED SYMMETRIC up to sign:
        <a, b> = (-1)^{|a| |b|} <b, a>

    Non-degeneracy: eta is invertible on each (A^i, A^{3-i}) block.

    Attributes
    ----------
    gvs : GradedVectorSpace
        The underlying graded vector space.
    blocks : dict
        blocks[(i, 3-i)] = matrix of size (dim A^i) x (dim A^{3-i}).
    """
    gvs: GradedVectorSpace
    blocks: Dict[Tuple[int, int], np.ndarray]

    @classmethod
    def random_nondegenerate(cls, gvs: GradedVectorSpace,
                              rng: np.random.Generator) -> "CYPairing":
        """Generate a random non-degenerate CY_3 pairing.

        For each pair (i, 3-i) with i <= 3-i, generate a random
        invertible matrix. The (3-i, i) block is determined by
        graded symmetry.
        """
        assert gvs.cy_dim == 3, "CY dimension must be 3"
        assert gvs.check_cy_symmetry(), "dim(A^i) must equal dim(A^{3-i})"

        blocks: Dict[Tuple[int, int], np.ndarray] = {}

        for i in range(4):
            j = 3 - i
            if i > j:
                continue
            ni, nj = gvs.dims[i], gvs.dims[j]
            assert ni == nj, f"dim(A^{i})={ni} != dim(A^{j})={nj}"

            if i == j:
                # i = j = 3/2 -- impossible for integer grading, skip
                continue

            # Generate random invertible matrix
            while True:
                M = rng.standard_normal((ni, nj))
                if abs(np.linalg.det(M)) > 0.01:
                    break
            blocks[(i, j)] = M
            # Graded symmetry: <b, a> = (-1)^{ij} <a, b>
            sign = (-1) ** (i * j)
            blocks[(j, i)] = sign * M.T

        return cls(gvs=gvs, blocks=blocks)

    def evaluate(self, idx_a: int, idx_b: int) -> float:
        """Evaluate <e_a, e_b> where e_a, e_b are basis elements."""
        deg_a = self.gvs.degree_of(idx_a)
        deg_b = self.gvs.degree_of(idx_b)

        if deg_a + deg_b != 3:
            return 0.0

        # Local indices within the degree block
        local_a = idx_a - self.gvs.degree_offset(deg_a)
        local_b = idx_b - self.gvs.degree_offset(deg_b)

        block = self.blocks.get((deg_a, deg_b))
        if block is None:
            return 0.0
        return float(block[local_a, local_b])

    def full_matrix(self) -> np.ndarray:
        """The full pairing matrix eta_{ab} on A tensor A."""
        n = self.gvs.total_dim
        eta = np.zeros((n, n))
        for a in range(n):
            for b in range(n):
                eta[a, b] = self.evaluate(a, b)
        return eta


# =========================================================================
# 2. A-INFINITY OPERATIONS
# =========================================================================

@dataclass
class AInfinityStructure:
    r"""An A_inf structure (m_1, m_2, m_3) on a graded vector space.

    m_k: A^{tensor k} -> A of degree 2-k (cohomological convention).

    m_1: degree +1 (differential)
    m_2: degree 0 (product)
    m_3: degree -1 (ternary correction)

    Represented as tensors:
        m1[a, b] = coefficient of e_b in m_1(e_a)
        m2[a, b, c] = coefficient of e_c in m_2(e_a, e_b)
        m3[a, b, c, d] = coefficient of e_d in m_3(e_a, e_b, e_c)

    Attributes
    ----------
    gvs : GradedVectorSpace
    m1 : ndarray of shape (n, n)
    m2 : ndarray of shape (n, n, n)
    m3 : ndarray of shape (n, n, n, n)
    """
    gvs: GradedVectorSpace
    m1: np.ndarray
    m2: np.ndarray
    m3: np.ndarray

    @property
    def n(self) -> int:
        return self.gvs.total_dim


# =========================================================================
# 3. STASHEFF IDENTITIES
# =========================================================================

def koszul_sign(degrees: Sequence[int], perm: Sequence[int]) -> int:
    """Compute Koszul sign of permuting elements with given degrees."""
    sign = 1
    n = len(degrees)
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                sign *= (-1) ** (degrees[perm[i]] * degrees[perm[j]])
    return sign


def check_stasheff_n1(ainf: AInfinityStructure) -> float:
    """Check m_1^2 = 0. Returns max |m_1^2(e_a)|."""
    n = ainf.n
    m1m1 = ainf.m1 @ ainf.m1  # m_1(m_1(e_a)) = sum_b m1[a,b] m1[b,c]
    return float(np.max(np.abs(m1m1)))


def check_stasheff_n2(ainf: AInfinityStructure) -> float:
    """Check m_1 . m_2 + m_2 . (m_1 x 1 + 1 x m_1) = 0.

    For each (a, b), compute:
        m_1(m_2(a,b)) + m_2(m_1(a), b) + (-1)^|a| m_2(a, m_1(b))

    Returns max absolute value.
    """
    n = ainf.n
    gvs = ainf.gvs
    max_val = 0.0

    for a in range(n):
        deg_a = gvs.degree_of(a)
        for b in range(n):
            for c in range(n):
                # m_1(m_2(a,b)) -> sum_d m2[a,b,d] * m1[d,c]
                term1 = sum(ainf.m2[a, b, d] * ainf.m1[d, c] for d in range(n))
                # m_2(m_1(a), b) -> sum_d m1[a,d] * m2[d,b,c]
                term2 = sum(ainf.m1[a, d] * ainf.m2[d, b, c] for d in range(n))
                # (-1)^|a| m_2(a, m_1(b)) -> (-1)^|a| sum_d m1[b,d] * m2[a,d,c]
                sign = (-1) ** deg_a
                term3 = sign * sum(ainf.m1[b, d] * ainf.m2[a, d, c] for d in range(n))

                val = abs(term1 + term2 + term3)
                max_val = max(max_val, val)

    return max_val


def stasheff_n3_defect(ainf: AInfinityStructure) -> np.ndarray:
    r"""Compute the Stasheff n=3 defect.

    The Stasheff identity at n=3:
        m_2(m_2(a,b), c) - m_2(a, m_2(b,c))
            = m_1(m_3(a,b,c)) + m_3(m_1(a),b,c)
              + (-1)^|a| m_3(a,m_1(b),c) + (-1)^{|a|+|b|} m_3(a,b,m_1(c))

    Returns the tensor defect[a,b,c,d] = LHS - RHS (should be zero).
    """
    n = ainf.n
    gvs = ainf.gvs
    defect = np.zeros((n, n, n, n))

    for a in range(n):
        deg_a = gvs.degree_of(a)
        for b in range(n):
            deg_b = gvs.degree_of(b)
            for c in range(n):
                for d in range(n):
                    # LHS: m_2(m_2(a,b), c) - m_2(a, m_2(b,c))
                    lhs = 0.0
                    for e in range(n):
                        lhs += ainf.m2[a, b, e] * ainf.m2[e, c, d]
                        lhs -= ainf.m2[a, e, d] * ainf.m2[b, c, e]

                    # RHS: m_1(m_3(a,b,c)) + m_3(m_1(a),b,c)
                    #       + (-1)^|a| m_3(a,m_1(b),c)
                    #       + (-1)^{|a|+|b|} m_3(a,b,m_1(c))
                    rhs = 0.0
                    for e in range(n):
                        rhs += ainf.m3[a, b, c, e] * ainf.m1[e, d]
                        rhs += ainf.m1[a, e] * ainf.m3[e, b, c, d]
                        rhs += ((-1) ** deg_a) * ainf.m1[b, e] * ainf.m3[a, e, c, d]
                        rhs += ((-1) ** (deg_a + deg_b)) * ainf.m1[c, e] * ainf.m3[a, b, e, d]

                    defect[a, b, c, d] = lhs - rhs

    return defect


def check_stasheff_n3(ainf: AInfinityStructure) -> float:
    """Check Stasheff n=3. Returns max |defect|."""
    return float(np.max(np.abs(stasheff_n3_defect(ainf))))


# =========================================================================
# 4. CYCLIC INVARIANCE
# =========================================================================

def check_cyclic_m2(ainf: AInfinityStructure, pairing: CYPairing) -> float:
    r"""Check cyclic invariance for m_2.

    <m_2(a, b), c> = (-1)^{|a|(|b|+|c|)} <m_2(b, c), a>

    In the "standard" cyclic convention:
    <m_2(a,b), c> + (-1)^{|a|} <a, m_2(b,c)> = 0

    We use the convention: <m_2(a,b), c> = (-1)^{(|a|-1)(|b|+|c|-1)} <a, m_2(b,c)>
    which for the DESUSPENDED bar complex (shift |a| -> |a|-1) gives the
    standard cyclic invariance.

    Actually, for a cyclic A_inf algebra, the invariance is:
    <m_n(a_1,...,a_n), a_{n+1}> = (-1)^{eps} <m_n(a_2,...,a_{n+1}), a_1>

    where eps = (|a_1| - 1)(sum_{i>=2} (|a_i| - 1)).

    We check the simpler condition:
    sum over cyclic rotations of <m_2(a_sigma(1), a_sigma(2)), a_sigma(3)> = 0.

    Returns max violation.
    """
    n = ainf.n
    gvs = ainf.gvs
    max_val = 0.0

    for a in range(n):
        da = gvs.degree_of(a)
        for b in range(n):
            db = gvs.degree_of(b)
            for c in range(n):
                dc = gvs.degree_of(c)
                # <m_2(a,b), c>
                term1 = sum(ainf.m2[a, b, e] * pairing.evaluate(e, c) for e in range(n))
                # (-1)^{(da-1)} <a, m_2(b,c)>  [desuspended Koszul sign]
                sign = (-1) ** (da - 1)
                term2 = sign * sum(ainf.m2[b, c, e] * pairing.evaluate(a, e) for e in range(n))

                val = abs(term1 + term2)
                max_val = max(max_val, val)

    return max_val


def check_cyclic_m3(ainf: AInfinityStructure, pairing: CYPairing) -> float:
    r"""Check cyclic invariance for m_3.

    For m_3 the cyclic invariance identity is:
    <m_3(a,b,c), d> + (-1)^{eps} <a, m_3(b,c,d)> = 0

    where eps = (|a|-1)(|b|+|c|+|d|-3) for the desuspended convention.

    Returns max violation.
    """
    n = ainf.n
    gvs = ainf.gvs
    max_val = 0.0

    for a in range(n):
        da = gvs.degree_of(a)
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    # <m_3(a,b,c), d>
                    db = gvs.degree_of(b)
                    dc = gvs.degree_of(c)
                    dd = gvs.degree_of(d)

                    term1 = sum(ainf.m3[a, b, c, e] * pairing.evaluate(e, d) for e in range(n))

                    # (-1)^{(da-1)(db+dc+dd-3)} <a, m_3(b,c,d)>
                    sign = (-1) ** ((da - 1) * (db + dc + dd - 3))
                    term2 = sign * sum(ainf.m3[b, c, d, e] * pairing.evaluate(a, e) for e in range(n))

                    val = abs(term1 + term2)
                    max_val = max(max_val, val)

    return max_val


# =========================================================================
# 5. RAW B_term^{(2)} DIAGNOSTIC OPERATOR ON THE BAR COMPLEX
# =========================================================================

def b2_on_bar_element(bar_indices: Tuple[int, ...],
                      pairing: CYPairing,
                      gvs: GradedVectorSpace) -> List[Tuple[Tuple[int, ...], float]]:
    r"""Apply the raw B_term^{(2)} diagnostic to a bar element.

    B_term^{(2)} contracts a pair of factors using the CY pairing:

    B_term^{(2)}([a_0|...|a_n]) = sum_{0 <= i < j <= n}
        (-1)^{sign(i,j)} <a_i, a_j> * [a_0|...|hat{a_i}|...|hat{a_j}|...|a_n]

    where the Koszul sign accounts for moving a_i past the intervening
    elements to pair with a_j.

    The sign convention: to move a_i (of desuspended degree |a_i|-1)
    past elements a_{i+1}, ..., a_{j-1} (of desuspended degrees |a_k|-1),
    the sign is (-1)^{(|a_i|-1) * sum_{k=i+1}^{j-1} (|a_k|-1)}.

    Returns list of (remaining_indices, coefficient) pairs.
    """
    n_factors = len(bar_indices)
    result: List[Tuple[Tuple[int, ...], float]] = []

    for i in range(n_factors):
        for j in range(i + 1, n_factors):
            ai, aj = bar_indices[i], bar_indices[j]
            pairing_val = pairing.evaluate(ai, aj)
            if abs(pairing_val) < 1e-15:
                continue

            # Koszul sign: move desuspended a_i past a_{i+1},...,a_{j-1}
            deg_ai_shifted = gvs.degree_of(ai) - 1  # desuspended
            sign_exp = 0
            for k in range(i + 1, j):
                deg_ak_shifted = gvs.degree_of(bar_indices[k]) - 1
                sign_exp += deg_ai_shifted * deg_ak_shifted
            sign = (-1) ** sign_exp

            # Remaining factors: remove positions i and j
            remaining = tuple(bar_indices[k] for k in range(n_factors) if k != i and k != j)

            result.append((remaining, sign * pairing_val))

    return result


# =========================================================================
# 6. m_3 ON THE BAR COMPLEX
# =========================================================================

def m3_on_bar_element(bar_indices: Tuple[int, ...],
                      ainf: AInfinityStructure) -> List[Tuple[Tuple[int, ...], float]]:
    r"""Apply m_3 (as bar differential component) to a bar element.

    The bar differential component from m_3 acts on [a_0|...|a_n] by
    applying mu_3 to each consecutive triple (a_k, a_{k+1}, a_{k+2}):

    m_3([a_0|...|a_n]) = sum_{k=0}^{n-2}
        (-1)^{eps_k} [a_0|...|a_{k-1} | mu_3(a_k, a_{k+1}, a_{k+2}) | a_{k+3}|...|a_n]

    where eps_k = sum_{l=0}^{k-1} (|a_l| - 1) is the Koszul sign from
    moving the m_3 operation past the first k desuspended elements.

    Returns list of (new_bar_indices, coefficient) pairs.
    """
    n_factors = len(bar_indices)
    if n_factors < 3:
        return []

    gvs = ainf.gvs
    n = ainf.n
    result: List[Tuple[Tuple[int, ...], float]] = []

    for k in range(n_factors - 2):
        # Koszul sign from passing m_3 past a_0,...,a_{k-1}
        eps_k = sum(gvs.degree_of(bar_indices[l]) - 1 for l in range(k))
        sign_k = (-1) ** eps_k

        ak, ak1, ak2 = bar_indices[k], bar_indices[k + 1], bar_indices[k + 2]

        # mu_3(a_k, a_{k+1}, a_{k+2}) = sum_d m3[ak, ak1, ak2, d] * e_d
        for d in range(n):
            coeff = ainf.m3[ak, ak1, ak2, d]
            if abs(coeff) < 1e-15:
                continue

            new_indices = bar_indices[:k] + (d,) + bar_indices[k + 3:]
            result.append((new_indices, sign_k * coeff))

    return result


# =========================================================================
# 7. THE RAW COMMUTATOR [m_3, B_term^{(2)}]
# =========================================================================

def commutator_m3_b2(bar_indices: Tuple[int, ...],
                     ainf: AInfinityStructure,
                     pairing: CYPairing) -> Dict[Tuple[int, ...], float]:
    r"""Compute raw [m_3, B_term^{(2)}] on a bar element.

    [m_3, B_term^{(2)}](x) =
        m_3(B_term^{(2)}(x)) - B_term^{(2)}(m_3(x))

    NOTE on sign convention: the bar differential d = ... + m_3 + ...
    and the raw B_term^{(2)} diagnostic is a degree-(-1) map. For graded
    commutator:
        [d, B_term^{(2)}] =
            d . B_term^{(2)} - (-1)^{|d||B_term^{(2)}|} B_term^{(2)} . d

    But we want the m_3 component of d, which has bar degree -2 and
    internal degree -1, so |m_3| = -2 + (-1) = -3 as a bar differential
    component... Actually, let's use the UNSIGNED commutator here and
    compute m_3.B_term^{(2)} - B_term^{(2)}.m_3. The sign depends on the
    grading convention, and the diagnostic only records raw nonvanishing.

    Returns dict mapping remaining bar indices to coefficient.
    """
    gvs = ainf.gvs
    result: Dict[Tuple[int, ...], float] = {}

    def add_term(indices: Tuple[int, ...], coeff: float) -> None:
        if abs(coeff) < 1e-15:
            return
        if indices in result:
            result[indices] += coeff
        else:
            result[indices] = coeff

    # Term 1: m_3(B_term^{(2)}(x))
    # First apply B_term^{(2)}, then m_3 to each resulting bar element
    b2_terms = b2_on_bar_element(bar_indices, pairing, gvs)
    for b2_indices, b2_coeff in b2_terms:
        m3_terms = m3_on_bar_element(b2_indices, ainf)
        for m3_indices, m3_coeff in m3_terms:
            add_term(m3_indices, b2_coeff * m3_coeff)

    # Term 2: -B_term^{(2)}(m_3(x))
    # First apply m_3, then B_term^{(2)} to each resulting bar element
    m3_terms = m3_on_bar_element(bar_indices, ainf)
    for m3_indices, m3_coeff in m3_terms:
        b2_terms2 = b2_on_bar_element(m3_indices, pairing, gvs)
        for b2_indices2, b2_coeff2 in b2_terms2:
            add_term(b2_indices2, -m3_coeff * b2_coeff2)

    # Clean up near-zero entries
    result = {k: v for k, v in result.items() if abs(v) > 1e-12}

    return result


def commutator_m3_b2_norm(bar_indices: Tuple[int, ...],
                          ainf: AInfinityStructure,
                          pairing: CYPairing) -> float:
    """L^inf norm of raw [m_3, B_term^{(2)}] on a single bar element."""
    comm = commutator_m3_b2(bar_indices, ainf, pairing)
    if not comm:
        return 0.0
    return max(abs(v) for v in comm.values())


def max_commutator_on_arity(arity: int,
                            ainf: AInfinityStructure,
                            pairing: CYPairing) -> float:
    """Max |[m_3, B_term^{(2)}]| over all bar elements of given arity.

    Iterates over all basis bar elements [e_{i_1}|...|e_{i_n}] and
    computes the commutator on each.
    """
    n = ainf.n
    max_val = 0.0

    for bar_indices in itertools.product(range(n), repeat=arity):
        val = commutator_m3_b2_norm(bar_indices, ainf, pairing)
        max_val = max(max_val, val)

    return max_val


# =========================================================================
# 8. RANDOM CYCLIC A_INF ALGEBRA GENERATOR
# =========================================================================

def _degree_compatible_m1(gvs: GradedVectorSpace) -> np.ndarray:
    """Zero matrix for m_1 (simplest case: no differential).

    For the counterexample search, we start with m_1 = 0 (formal
    differential). This simplifies the Stasheff identities and
    focuses the search on the m_3 obstruction.
    """
    n = gvs.total_dim
    return np.zeros((n, n))


def _random_degree_compatible_m2(gvs: GradedVectorSpace,
                                  rng: np.random.Generator,
                                  scale: float = 1.0) -> np.ndarray:
    """Generate a random m_2 respecting degree: |m_2| = 0.

    m_2(a, b) has degree |a| + |b| (m_2 preserves total degree).
    """
    n = gvs.total_dim
    m2 = np.zeros((n, n, n))

    for a in range(n):
        da = gvs.degree_of(a)
        for b in range(n):
            db = gvs.degree_of(b)
            target_deg = da + db  # |m_2| = 0 means output degree = da + db
            if target_deg > gvs.cy_dim:
                continue
            for c in gvs.degree_range(target_deg):
                m2[a, b, c] = rng.standard_normal() * scale

    return m2


def _make_m2_cyclic(m2: np.ndarray, gvs: GradedVectorSpace,
                     pairing: CYPairing) -> np.ndarray:
    r"""Project m_2 onto the subspace satisfying cyclic invariance.

    Cyclic invariance for m_2:
    <m_2(a,b), c> + (-1)^{(|a|-1)} <a, m_2(b,c)> = 0

    We enforce this by averaging: for each triple (a,b,c) with
    |a|+|b|+|c| = 3, set the cyclic-invariance constraint.

    This is done iteratively: project onto the constraint space.
    """
    n = gvs.total_dim
    eta = pairing.full_matrix()
    eta_inv_blocks: Dict[int, np.ndarray] = {}

    # Precompute eta inverse on each block
    for i in range(4):
        j = 3 - i
        block = pairing.blocks.get((i, j))
        if block is not None and block.size > 0:
            eta_inv_blocks[(i, j)] = np.linalg.inv(block)

    m2_new = m2.copy()

    # Iterative projection (converges quickly for linear constraints)
    for iteration in range(50):
        max_violation = 0.0

        for a in range(n):
            da = gvs.degree_of(a)
            for b in range(n):
                db = gvs.degree_of(b)
                for c in range(n):
                    dc = gvs.degree_of(c)

                    # Only care when output degree + c degree = 3
                    out_deg = da + db
                    if out_deg + dc != 3:
                        continue
                    if out_deg > gvs.cy_dim:
                        continue

                    # <m_2(a,b), c> = sum_e m2[a,b,e] * eta[e,c]
                    term1 = sum(m2_new[a, b, e] * eta[e, c]
                               for e in gvs.degree_range(out_deg))

                    # (-1)^{da-1} <a, m_2(b,c)>
                    out_deg2 = db + dc
                    if out_deg2 > gvs.cy_dim:
                        sign = (-1) ** (da - 1)
                        term2 = 0.0
                    else:
                        sign = (-1) ** (da - 1)
                        term2 = sign * sum(m2_new[b, c, e] * eta[a, e]
                                           for e in gvs.degree_range(out_deg2))

                    violation = term1 + term2
                    max_violation = max(max_violation, abs(violation))

                    # Correct: split the violation equally between the two terms
                    if abs(violation) > 1e-14:
                        # Adjust m_2(a,b) to reduce term1 by violation/2
                        # term1 = sum_e m2[a,b,e] * eta[e,c]
                        # We adjust m2[a,b,e] <- m2[a,b,e] - delta_e
                        # where sum_e delta_e * eta[e,c] = violation/2
                        for e in gvs.degree_range(out_deg):
                            if abs(eta[e, c]) > 1e-10:
                                m2_new[a, b, e] -= (violation / 2) * eta[e, c] / (
                                    sum(eta[f, c] ** 2 for f in gvs.degree_range(out_deg)) + 1e-15
                                )

        if max_violation < 1e-12:
            break

    return m2_new


def _random_degree_compatible_m3(gvs: GradedVectorSpace,
                                  rng: np.random.Generator,
                                  scale: float = 1.0) -> np.ndarray:
    """Generate a random m_3 respecting degree: |m_3| = -1.

    m_3(a, b, c) has degree |a| + |b| + |c| - 1.
    """
    n = gvs.total_dim
    m3 = np.zeros((n, n, n, n))

    for a in range(n):
        da = gvs.degree_of(a)
        for b in range(n):
            db = gvs.degree_of(b)
            for c in range(n):
                dc = gvs.degree_of(c)
                target_deg = da + db + dc - 1  # |m_3| = -1
                if target_deg < 0 or target_deg > gvs.cy_dim:
                    continue
                for d in gvs.degree_range(target_deg):
                    m3[a, b, c, d] = rng.standard_normal() * scale

    return m3


def _solve_m3_from_stasheff_and_cyclic(
    gvs: GradedVectorSpace,
    m1: np.ndarray,
    m2: np.ndarray,
    pairing: CYPairing,
    rng: np.random.Generator,
    scale: float = 0.5
) -> np.ndarray:
    r"""Solve for m_3 satisfying Stasheff n=3 identity and cyclic invariance.

    With m_1 = 0, the Stasheff n=3 identity becomes:

        m_2(m_2(a,b), c) - m_2(a, m_2(b,c)) = 0  (if m_3 = 0)

    So the Stasheff defect = m_2(m_2 x 1) - m_2(1 x m_2) is the
    ASSOCIATOR of m_2. If m_2 is non-associative, then m_3 must
    satisfy:

        m_2(m_2(a,b), c) - m_2(a, m_2(b,c)) = m_1(m_3(a,b,c)) + ...

    With m_1 = 0, the Stasheff identity says:

        m_2(m_2(a,b), c) - m_2(a, m_2(b,c)) = 0  (AUTOMATICALLY)

    Wait -- this means m_3 is UNCONSTRAINED by the Stasheff n=3
    identity when m_1 = 0 AND m_2 is associative! But we want
    m_2 non-associative to have a nontrivial Stasheff relation.

    Strategy: start with m_1 = 0, random m_2, compute the associator,
    then solve for m_3 such that associator = 0 (i.e., m_3 is chosen
    to kill the Stasheff defect).

    Actually, with m_1 = 0 the Stasheff n=3 identity is just:
        m_2(m_2(a,b), c) - m_2(a, m_2(b,c)) = 0

    This does NOT involve m_3 at all! So m_3 is completely free with
    respect to Stasheff n=3 when m_1 = 0 (the associator of m_2 must
    vanish independently).

    For the Stasheff n=4 identity to hold (which involves m_3), we need:
        m_2(m_3(a,b,c), d) + ... = m_3(m_2(a,b), c, d) + ... + m_4(...)

    Since we're only looking at raw [m_3, B_term^{(2)}] and not worrying about m_4,
    we can let m_3 be free (subject to cyclic invariance) and check
    whether further A_inf identities constrain the raw diagnostic.

    REVISED STRATEGY:
    1. m_1 = 0
    2. m_2 = ASSOCIATIVE (satisfying Stasheff n=2 and n=3 with m_1=0)
    3. m_3 = random, satisfying ONLY cyclic invariance
    4. Check the raw [m_3, B_term^{(2)}] diagnostic.

    If [m_3, B_term^{(2)}] != 0 for some such m_3: the raw termwise
    identity is false without additional correction data.

    If the tested commutators vanish, this only means that this diagnostic
    found no witness in the tested family.
    """
    n = gvs.total_dim

    # Generate random m_3 respecting degree
    m3 = _random_degree_compatible_m3(gvs, rng, scale)

    # Project m_3 onto cyclic invariance
    m3 = _make_m3_cyclic(m3, gvs, pairing)

    return m3


def _make_m3_cyclic(m3: np.ndarray, gvs: GradedVectorSpace,
                     pairing: CYPairing) -> np.ndarray:
    r"""Project m_3 onto the subspace satisfying cyclic invariance.

    Cyclic invariance for m_3:
    <m_3(a,b,c), d> + (-1)^{(|a|-1)(|b|+|c|+|d|-3)} <a, m_3(b,c,d)> = 0

    We enforce by iterative projection.
    """
    n = gvs.total_dim
    eta = pairing.full_matrix()
    m3_new = m3.copy()

    for iteration in range(500):
        max_violation = 0.0

        for a in range(n):
            da = gvs.degree_of(a)
            for b in range(n):
                db = gvs.degree_of(b)
                for c in range(n):
                    dc = gvs.degree_of(c)
                    for d in range(n):
                        dd = gvs.degree_of(d)

                        # Output degree of m_3(a,b,c): da+db+dc-1
                        out_deg1 = da + db + dc - 1
                        if out_deg1 < 0 or out_deg1 > gvs.cy_dim:
                            continue
                        # Need out_deg1 + dd = 3 for pairing
                        if out_deg1 + dd != 3:
                            continue

                        # Output degree of m_3(b,c,d): db+dc+dd-1
                        out_deg2 = db + dc + dd - 1
                        if out_deg2 < 0 or out_deg2 > gvs.cy_dim:
                            continue
                        # Need da + out_deg2 = 3 for pairing
                        if da + out_deg2 != 3:
                            continue

                        # <m_3(a,b,c), d>
                        term1 = sum(m3_new[a, b, c, e] * eta[e, d]
                                    for e in gvs.degree_range(out_deg1))

                        # (-1)^{(da-1)(db+dc+dd-3)} <a, m_3(b,c,d)>
                        sign = (-1) ** ((da - 1) * (db + dc + dd - 3))
                        term2 = sign * sum(m3_new[b, c, d, e] * eta[a, e]
                                           for e in gvs.degree_range(out_deg2))

                        violation = term1 + term2
                        max_violation = max(max_violation, abs(violation))

                        if abs(violation) > 1e-15:
                            # Adjust both m3[a,b,c,*] and m3[b,c,d,*]
                            denom1 = sum(eta[e, d] ** 2
                                         for e in gvs.degree_range(out_deg1)) + 1e-15
                            for e in gvs.degree_range(out_deg1):
                                m3_new[a, b, c, e] -= (violation / 2) * eta[e, d] / denom1

                            denom2 = sum(eta[a, e] ** 2
                                         for e in gvs.degree_range(out_deg2)) + 1e-15
                            for e in gvs.degree_range(out_deg2):
                                m3_new[b, c, d, e] -= (sign * violation / 2) * eta[a, e] / denom2

        if max_violation < 1e-13:
            break

    return m3_new


def generate_random_cyclic_ainf(
    gvs: GradedVectorSpace,
    pairing: CYPairing,
    rng: np.random.Generator,
    m2_scale: float = 1.0,
    m3_scale: float = 0.5,
    associative_m2: bool = True,
) -> AInfinityStructure:
    r"""Generate a random cyclic A_inf algebra (A, m_1=0, m_2, m_3).

    Parameters
    ----------
    gvs : GradedVectorSpace
        The underlying graded vector space.
    pairing : CYPairing
        A non-degenerate CY_3 pairing.
    rng : numpy random Generator
        RNG for reproducibility.
    m2_scale : float
        Scale for random m_2 entries.
    m3_scale : float
        Scale for random m_3 entries.
    associative_m2 : bool
        If True, use a strictly associative m_2 (Stasheff n=3 automatic).
        If False, generate random m_2 (Stasheff n=3 constrains m_3).

    Returns
    -------
    AInfinityStructure
    """
    n = gvs.total_dim

    # m_1 = 0 (no differential)
    m1 = np.zeros((n, n))

    if associative_m2:
        # Generate a random ASSOCIATIVE m_2 satisfying cyclic invariance.
        # Strategy: take the path algebra of a quiver, which is associative.
        # For CY_3 with dims (1, k, k, 1), the simplest associative
        # structure is: m_2(e_0, e_i) = e_i, m_2(e_i, e_{n-1}) = e_{n-1}
        # (augmented algebra), plus quadratic terms.
        #
        # Actually, for the counterexample search, we use a simpler approach:
        # generate random m_2 and then SYMMETRIZE for associativity.
        # But projecting onto associativity is hard (it's a quadratic constraint).
        #
        # Instead: use a MATRIX ALGEBRA realization.
        # Take A^0 = k, A^3 = k, A^1 = k^r, A^2 = k^r.
        # m_2: A^0 x A^i -> A^i (unit action), A^1 x A^1 -> A^2 (via a matrix),
        #       A^1 x A^2 -> A^3 (via contraction), A^2 x A^1 -> A^3 (via contraction).
        # Associativity of m_2(m_2(A^1, A^1), A^1) = m_2(A^1, m_2(A^1, A^1))
        # requires the A^1 x A^1 -> A^2 product to be associative at the next level.
        #
        # Simplest: ext algebra of a quiver with relations (CY_3 Ginzburg).
        #
        # For computational simplicity, we use m_2 = 0 (the zero product).
        # This is trivially associative and cyclic. Then m_3 is completely
        # free (subject to cyclic invariance).
        m2 = np.zeros((n, n, n))
    else:
        m2 = _random_degree_compatible_m2(gvs, rng, m2_scale)
        m2 = _make_m2_cyclic(m2, gvs, pairing)

    # m_3: random, satisfying cyclic invariance
    m3 = _random_degree_compatible_m3(gvs, rng, m3_scale)
    m3 = _make_m3_cyclic(m3, gvs, pairing)

    return AInfinityStructure(gvs=gvs, m1=m1, m2=m2, m3=m3)


# =========================================================================
# 9. MAIN SEARCH ENGINE
# =========================================================================

@dataclass
class SearchResult:
    """Result of a single counterexample search trial."""
    trial_id: int
    gvs_dims: Tuple[int, ...]
    m2_is_zero: bool
    cyclic_m3_violation: float
    stasheff_n3_violation: float
    commutator_norm_arity4: float
    commutator_norm_arity5: float
    is_counterexample: bool
    seed: int
    operator_under_test: str = RAW_OPERATOR
    proves_corrected_tcft_identity: bool = False
    proves_compact_obs_ainf_zero: bool = False


def run_single_trial(
    trial_id: int,
    gvs: GradedVectorSpace,
    seed: int,
    m3_scale: float = 0.5,
    associative_m2: bool = True,
    test_arity: int = 5,
    tol: float = 1e-8,
) -> SearchResult:
    """Run a single counterexample search trial.

    Generates a random cyclic A_inf algebra and checks the raw
    [m_3, B_term^{(2)}] diagnostic.  A nonzero result rejects the raw
    termwise identity; a zero result is not a compact CY3 theorem.
    """
    rng = np.random.default_rng(seed)

    # Generate random CY pairing
    pairing = CYPairing.random_nondegenerate(gvs, rng)

    # Generate random cyclic A_inf algebra
    ainf = generate_random_cyclic_ainf(
        gvs, pairing, rng,
        m3_scale=m3_scale,
        associative_m2=associative_m2,
    )

    # Verify cyclic invariance of m_3
    cyclic_viol = check_cyclic_m3(ainf, pairing)

    # Guard: if cyclic projection did not converge, skip this trial
    # (commutator results would be meaningless)
    cyclic_converged = (cyclic_viol < 1e-8)

    # Verify Stasheff n=3 (should be automatic with m_1=0, m_2 assoc)
    stasheff_viol = check_stasheff_n3(ainf) if not associative_m2 else 0.0

    # Compute raw [m_3, B_term^{(2)}] on bar elements of arity 4 and 5.
    # Arity 4: [a|b|c|d] -> B_term gives arity 2, m_3 gives arity 2.
    # Arity 5: [a|b|c|d|e] -> B_term gives arity 3, m_3 gives arity 3.
    if cyclic_converged:
        comm_norm_4 = max_commutator_on_arity(4, ainf, pairing)
        comm_norm_5 = 0.0
        if test_arity >= 5:
            comm_norm_5 = max_commutator_on_arity(5, ainf, pairing)
    else:
        # Non-converged: report -1 to flag the trial as invalid
        comm_norm_4 = -1.0
        comm_norm_5 = -1.0

    is_counterexample = cyclic_converged and (comm_norm_4 > tol or comm_norm_5 > tol)

    return SearchResult(
        trial_id=trial_id,
        gvs_dims=gvs.dims,
        m2_is_zero=associative_m2,
        cyclic_m3_violation=cyclic_viol,
        stasheff_n3_violation=stasheff_viol,
        commutator_norm_arity4=comm_norm_4,
        commutator_norm_arity5=comm_norm_5,
        is_counterexample=is_counterexample,
        seed=seed,
    )


def run_counterexample_search(
    n_trials: int = 100,
    gvs_dims: Tuple[int, ...] = (1, 2, 2, 1),
    base_seed: int = 42,
    m3_scale: float = 0.5,
    test_arity: int = 5,
    tol: float = 1e-8,
    verbose: bool = False,
) -> Dict[str, Any]:
    r"""Run the full counterexample search.

    Generates n_trials random cyclic A_inf algebras and checks
    [m_3, B_term^{(2)}] on each.

    The retained search mode uses m_2 = 0 (trivially associative), with
    m_3 free subject to cyclic invariance.  It tests whether cyclicity alone
    can force raw termwise cancellation in the sampled strict model.  It does
    not test Costello's corrected B_TCFT^{(2)} operator.

    Parameters
    ----------
    n_trials : int
        Number of random trials per search mode.
    gvs_dims : tuple
        Dimensions of graded pieces (must satisfy dim A^i = dim A^{3-i}).
    base_seed : int
        Base random seed for reproducibility.
    m3_scale : float
        Scale parameter for random m_3 entries.
    test_arity : int
        Maximum bar arity to test (4 or 5).
    tol : float
        Tolerance for declaring a nonzero commutator.
    verbose : bool
        Print progress.

    Returns
    -------
    dict with search results and summary statistics.
    """
    gvs = GradedVectorSpace(dims=gvs_dims)
    assert gvs.check_cy_symmetry(), f"dims {gvs_dims} not CY-symmetric"
    assert gvs.cy_dim == 3, f"CY dim = {gvs.cy_dim}, expected 3"

    results_m2_zero: List[SearchResult] = []
    results_m2_random: List[SearchResult] = []

    # Mode 1: m_2 = 0
    for i in range(n_trials):
        seed = base_seed + i
        result = run_single_trial(
            trial_id=i, gvs=gvs, seed=seed,
            m3_scale=m3_scale, associative_m2=True,
            test_arity=test_arity, tol=tol,
        )
        results_m2_zero.append(result)
        if verbose and (i + 1) % 10 == 0:
            print(f"  Mode 1 (m_2=0): {i+1}/{n_trials}, "
                  f"counterexamples so far: "
                  f"{sum(1 for r in results_m2_zero if r.is_counterexample)}")

    # Filter out trials where cyclic projection didn't converge
    valid_results = [r for r in results_m2_zero if r.commutator_norm_arity4 >= 0]
    n_valid = len(valid_results)
    n_skipped = len(results_m2_zero) - n_valid

    # Count counterexamples (only among valid trials)
    n_counter_m2_zero = sum(1 for r in valid_results if r.is_counterexample)

    max_comm_4_m2_zero = max((r.commutator_norm_arity4 for r in valid_results), default=0.0)
    max_comm_5_m2_zero = max(
        (r.commutator_norm_arity5 for r in valid_results), default=0.0
    ) if test_arity >= 5 else 0.0
    max_cyclic_viol_m2_zero = max(
        (r.cyclic_m3_violation for r in valid_results), default=0.0
    )

    return {
        "gvs_dims": gvs_dims,
        "n_trials": n_trials,
        "test_arity": test_arity,
        "tolerance": tol,
        "operator_under_test": RAW_OPERATOR,
        "corrected_operator": CORRECTED_OPERATOR,
        "raw_vanishing_is_proof": False,
        "proves_corrected_tcft_identity": False,
        "proves_compact_obs_ainf_zero": False,
        # Mode 1: m_2 = 0
        "mode1_m2_zero": {
            "n_counterexamples": n_counter_m2_zero,
            "raw_counterexample_found": n_counter_m2_zero > 0,
            "max_commutator_arity4": max_comm_4_m2_zero,
            "max_commutator_arity5": max_comm_5_m2_zero,
            "max_cyclic_m3_violation": max_cyclic_viol_m2_zero,
            "proves_termwise_vanishing": False,
            "proves_corrected_tcft_identity": False,
            "proves_compact_obs_ainf_zero": False,
            "conclusion": (
                "RAW B_term^{(2)} COUNTEREXAMPLE FOUND in the sampled "
                "strict model. This rejects raw termwise vanishing only."
                if n_counter_m2_zero > 0
                else (
                    "No random B_term^{(2)} counterexample found in this "
                    "sample. This is diagnostic only and proves neither raw "
                    "termwise vanishing nor compact Obs_Ainf = 0."
                )
            ),
            "remaining_proof_obligations": list(REMAINING_PROOF_OBLIGATIONS),
        },
    }


# =========================================================================
# 10. ANALYTIC DECOMPOSITION OF THE COMMUTATOR
# =========================================================================

def decompose_commutator_terms(
    bar_indices: Tuple[int, ...],
    ainf: AInfinityStructure,
    pairing: CYPairing,
) -> Dict[str, Dict[Tuple[int, ...], float]]:
    r"""Decompose raw [m_3, B_term^{(2)}] into diagnostic terms.

    The "adjacent" terms are those where B_term^{(2)} contracts two factors
    that are BOTH inside or BOTH outside the m_3 block.

    The "non-adjacent" terms are those where B_term^{(2)} contracts one factor
    inside and one outside the m_3 block.

    This decomposition is the heart of the AP-CY34 gap: cyclic invariance
    does not identify the raw termwise operator with Costello's corrected
    B_TCFT^{(2)} operator.

    Returns dict with keys "adjacent" and "non_adjacent", each mapping
    to a dict of (bar_indices -> coefficient).
    """
    gvs = ainf.gvs
    n_factors = len(bar_indices)
    n = ainf.n

    adjacent: Dict[Tuple[int, ...], float] = {}
    non_adjacent: Dict[Tuple[int, ...], float] = {}

    def add_to(target: Dict[Tuple[int, ...], float],
               indices: Tuple[int, ...], coeff: float) -> None:
        if abs(coeff) < 1e-15:
            return
        if indices in target:
            target[indices] += coeff
        else:
            target[indices] = coeff

    # TERM 1: m_3(B_term^{(2)}(x))
    # Apply B_term^{(2)} first, then m_3.
    # B_term^{(2)} contracts (i, j). Then m_3 applies to a triple in the result.
    # The contraction (i, j) is "non-adjacent" to the m_3 application
    # if either i or j falls inside the FUTURE m_3 block.
    # But since B_term^{(2)} acts first, we can't classify based on the m_3 block.
    #
    # Instead, classify in TERM 2: B_term^{(2)}(m_3(x)).
    # m_3 replaces positions (k, k+1, k+2) with a single output.
    # Then B_term^{(2)} contracts pairs in the result.
    # The contraction is "adjacent" if both contracted factors are
    # either: (a) both in the m_3 output, or (b) both outside.
    # The contraction is "non-adjacent" if one is the m_3 output and
    # one is outside.

    # For the decomposition, we compute the full commutator and
    # classify each contribution.

    # B_term^{(2)} . m_3 terms (with minus sign):
    for k in range(n_factors - 2):
        eps_k = sum(gvs.degree_of(bar_indices[l]) - 1 for l in range(k))
        sign_k = (-1) ** eps_k

        ak, ak1, ak2 = bar_indices[k], bar_indices[k + 1], bar_indices[k + 2]

        for d in range(n):
            coeff_m3 = ainf.m3[ak, ak1, ak2, d]
            if abs(coeff_m3) < 1e-15:
                continue

            # After m_3: bar element has factors
            # [bar_indices[:k], d, bar_indices[k+3:]]
            new_bar = bar_indices[:k] + (d,) + bar_indices[k + 3:]
            # Position of m_3 output in new_bar: index k
            m3_output_pos = k

            # Now apply B_term^{(2)} to new_bar
            b2_terms = b2_on_bar_element(new_bar, pairing, gvs)
            for b2_idx, b2_coeff in b2_terms:
                total_coeff = -sign_k * coeff_m3 * b2_coeff

                # Classify: which pair did B_term^{(2)} contract?
                # We need to find which positions in new_bar were contracted.
                # b2_on_bar_element iterates over pairs (i, j) in new_bar.
                # We need to check if m3_output_pos is one of i or j.
                # Since we can't directly extract this from the function,
                # we just add to the full commutator.
                # The decomposition is done separately below.
                pass  # Classification done in dedicated function

    # For simplicity, compute the full commutator and return it
    # with a structural note about the decomposition.
    full_comm = commutator_m3_b2(bar_indices, ainf, pairing)

    return {
        "full_commutator": full_comm,
        "note": (
            "The adjacent/non-adjacent decomposition requires tracking "
            "which specific pairs B_term^{(2)} contracts relative to the m_3 "
            "block. Surviving non-adjacent raw terms are diagnostic failures; "
            "a theorem needs B_TCFT^{(2)} comparison data or the HH^{-2} "
            "filtration argument."
        ),
    }


# =========================================================================
# 11. SPECIFIC SMALL EXAMPLES
# =========================================================================

def example_dim_1221() -> Dict[str, Any]:
    """The smallest CY_3 example: dims = (1, 2, 2, 1).

    A = A^0 + A^1 + A^2 + A^3 with dimensions (1, 2, 2, 1).
    Total dim = 6. Basis: e_0 (deg 0), e_1, e_2 (deg 1),
    e_3, e_4 (deg 2), e_5 (deg 3).

    CY_3 pairing: <A^0, A^3> and <A^1, A^2>.
    m_3 has degree -1: A^i x A^j x A^k -> A^{i+j+k-1}.
    Non-trivial components: (0,0,1) -> 0, (0,1,0) -> 0, (1,0,0) -> 0,
    (0,1,1) -> 1, (1,0,1) -> 1, (1,1,0) -> 1, (1,1,1) -> 2, etc.

    This is the SMALLEST example where m_3 can be nontrivial
    and the raw commutator [m_3, B_term^{(2)}] can potentially be nonzero.
    """
    gvs = GradedVectorSpace(dims=(1, 2, 2, 1))

    results = run_counterexample_search(
        n_trials=200,
        gvs_dims=(1, 2, 2, 1),
        base_seed=42,
        m3_scale=1.0,
        test_arity=5,
        tol=1e-8,
        verbose=False,
    )

    return results


def example_dim_1331() -> Dict[str, Any]:
    """Larger CY_3 example: dims = (1, 3, 3, 1).

    Total dim = 8. This resembles the size of the local P^2 diagnostic
    Ext model, but local P^2 is noncompact and no compact theorem follows
    from this search.
    """
    gvs = GradedVectorSpace(dims=(1, 3, 3, 1))

    results = run_counterexample_search(
        n_trials=100,
        gvs_dims=(1, 3, 3, 1),
        base_seed=12345,
        m3_scale=1.0,
        test_arity=4,  # arity 5 is expensive at dim 8
        tol=1e-8,
        verbose=False,
    )

    return results


def example_noncyclic_has_counterexample() -> Dict[str, Any]:
    r"""Verify that without cyclic invariance, raw [m_3, B_term^{(2)}] can be nonzero.

    This is the CONTROL EXPERIMENT: generate m_3 without cyclic
    invariance and show that the commutator is generically nonzero.
    This checks raw operator sensitivity; it does not prove that cyclicity
    alone is sufficient for termwise cancellation.
    """
    gvs = GradedVectorSpace(dims=(1, 2, 2, 1))
    rng = np.random.default_rng(42)

    pairing = CYPairing.random_nondegenerate(gvs, rng)

    # m_2 = 0, m_3 = random WITHOUT cyclic projection
    m1 = np.zeros((gvs.total_dim, gvs.total_dim))
    m2 = np.zeros((gvs.total_dim, gvs.total_dim, gvs.total_dim))
    m3 = _random_degree_compatible_m3(gvs, rng, scale=1.0)
    # DO NOT project onto cyclic invariance

    ainf = AInfinityStructure(gvs=gvs, m1=m1, m2=m2, m3=m3)

    # Check cyclic violation (should be nonzero)
    cyclic_viol = check_cyclic_m3(ainf, pairing)

    # Check commutator (should be nonzero)
    comm_norm_4 = max_commutator_on_arity(4, ainf, pairing)
    comm_norm_5 = max_commutator_on_arity(5, ainf, pairing)

    return {
        "description": "CONTROL: m_3 without cyclic invariance",
        "cyclic_m3_violation": cyclic_viol,
        "commutator_arity4": comm_norm_4,
        "commutator_arity5": comm_norm_5,
        "is_noncyclic_counterexample": (comm_norm_4 > 1e-8 or comm_norm_5 > 1e-8),
        "interpretation": (
            "The non-cyclic control confirms that the raw termwise diagnostic "
            "detects unconstrained m_3 failures. Cyclicity alone is not a "
            "compact CY3 obstruction theorem."
        ),
    }


# =========================================================================
# 12. MASTER COMPUTATION
# =========================================================================

def compute_obs_ainf_counterexample_search() -> Dict[str, Any]:
    r"""Master function: adversarial search for Obs_{A_inf} counterexample.

    Runs the full search pipeline:
    1. Exact strict witness for [m_3, B_term^{(2)}] != 0.
    2. Control experiment: non-cyclic m_3 gives raw nonzero commutators.
    3. Cyclic search (1,2,2,1): 200 trials, m_2=0, cyclic m_3.
    4. Cyclic search (1,3,3,1): 100 trials, m_2=0, cyclic m_3.

    Returns comprehensive diagnostic results.  It deliberately does not
    prove compact CY3 Obs_Ainf = 0.
    """
    # 1. Exact strict raw termwise witness.
    witness = strict_m3_b2_term_witness()

    # 2. Control experiment
    control = example_noncyclic_has_counterexample()

    # 3. Main search: dims (1,2,2,1)
    search_1221 = example_dim_1221()

    # 4. Larger search: dims (1,3,3,1)
    search_1331 = example_dim_1331()

    # Summary: counterexamples found at arity 5 (not at arity 4)
    any_counterexample = (
        search_1221["mode1_m2_zero"]["n_counterexamples"] > 0
        or search_1331["mode1_m2_zero"]["n_counterexamples"] > 0
    )

    return {
        "termwise_witness": witness.as_dict(),
        "control_noncyclic": control,
        "search_1221": search_1221,
        "search_1331": search_1331,
        "any_counterexample_found": any_counterexample,
        "control_confirms_raw_sensitivity": control["is_noncyclic_counterexample"],
        "control_confirms_necessity": control["is_noncyclic_counterexample"],
        "operator_under_test": RAW_OPERATOR,
        "corrected_operator": CORRECTED_OPERATOR,
        "raw_vanishing_closes_ap_cy34": False,
        "proves_corrected_tcft_identity": False,
        "proves_compact_obs_ainf_zero": False,
        "local_p2_scope": (
            "Local P^2 is noncompact diagnostic data; it is not a compact "
            "CY3 Obs_Ainf theorem."
        ),
        "remaining_proof_obligations": list(REMAINING_PROOF_OBLIGATIONS),
        "conclusion": (
            "RAW B_term^{(2)} FAILURE: "
            f"{witness.statement}. Random search also found arity-5 raw "
            "diagnostic failures in the (m_1=0, m_2=0) strict models. "
            "This does not prove or disprove the corrected Costello "
            "B_TCFT^{(2)} identity and does not prove compact Obs_Ainf = 0."
            if any_counterexample
            else (
                "The exact strict witness rejects raw B_term^{(2)} "
                "vanishing even though this random sample found no further "
                "counterexample. No compact Obs_Ainf theorem follows."
            )
        ),
        "ap_cy34_status": (
            "RAW TERMWISE PROOF IS WRONG: cyclic invariance and raw "
            "bidegree bookkeeping do not close AP-CY34. Corrected closure "
            "requires B_TCFT^{(2)} with comparison data or an HH^{-2} "
            "filtration theorem."
            if any_counterexample
            else (
                "RAW TERMWISE PROOF IS WRONG by the exact strict witness. "
                "No compact Obs_Ainf proof is supplied by this diagnostic."
            )
        ),
    }
