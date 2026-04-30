r"""Falsification search for raw ``[m_3, B^{(2)}_term]`` obstructions.

MATHEMATICAL CONTENT
====================

This engine is not a proof engine for universal vanishing.  It is a
falsification and witness-search tool for the raw bar-desuspended
pair-contraction operator

    B^{(2)}_term.

The corrected fact is that termwise raw vanishing is false: the strict
cyclic CY3 witness with ``m_3(a,a,a)=alpha b`` satisfies

    [m_3, B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0

in characteristic zero.  A finite random search can find candidate
nonvanishing behaviour, but a run with no candidate witness proves
nothing universal.  Corrected TCFT cancellation requires additional
Costello/open-closed comparison data and is not asserted here.

SETUP
=====

A cyclic A_infinity algebra (with m_1 = 0, m_k = 0 for k >= 4) consists of:

  (V, m_2, m_3, <-,->)

where V = k^d is a finite-dimensional graded vector space,

  m_2: V^{otimes 2} -> V          (binary product)
  m_3: V^{otimes 3} -> V          (ternary operation, the associator)
  <-,->: V otimes V -> k          (nondegenerate cyclic pairing)

subject to:

(S1) Stasheff identity at n=3 (m_1=0, m_4=0):

    m_2(m_2(a,b),c) - m_2(a, m_2(b,c)) = 0

    i.e. m_2 is STRICTLY ASSOCIATIVE when m_3 is the only correction
    and m_4=0.  (More precisely: the Stasheff identity at arity 3 with
    m_1=m_4=0 forces m_2 to be associative.  m_3 is then a Hochschild
    3-cocycle.)

(S2) Stasheff identity at n=4 (m_1=0, m_4=0):

    m_2(m_3(a,b,c),d) - m_3(m_2(a,b),c,d) + m_3(a,m_2(b,c),d)
    - m_3(a,b,m_2(c,d)) + m_2(a,m_3(b,c,d)) = 0

    This says m_3 is a Hochschild 3-cocycle for m_2.

(C1) Cyclic invariance of m_2:

    <m_2(a,b), c> = (-1)^{|a|(|b|+|c|)} <a, m_2(b,c)>

    For degree-0 elements this simplifies to: <m_2(a,b),c> = <a, m_2(b,c)>.

(C2) Cyclic invariance of m_3:

    <m_3(a,b,c), d> + <m_3(b,c,d), a> + <m_3(c,d,a), b> + <m_3(d,a,b), c> = 0

    (Full cyclic sum vanishes, with sign (-1)^{(d-1)(|a|+|b|+|c|-1)} for CY_d.)
    For d=3 and degree-0 elements: the 4-fold cyclic sum vanishes.

THE CONNES OPERATOR B^{(2)}
============================

The raw terminal-slot operator used by the standalone witness is:

    B^{(2)}_term[u_1|...|u_r|v]
      = sum_i <u_i, v> [u_1|...|hat{u_i}|...|u_r].

The exact graded signs of a genuine CY3 model are recorded by the strict
witness helper below.  The numerical matrix model is an ungraded
terminal-slot contraction, useful for falsification and regression tests,
not a replacement for the graded proof.

THE COMMUTATOR [m_3, B^{(2)}_term]
====================================

The induced m_3 on Hochschild chains acts as:

    m_3^{CC}(a_0 | a_1 | ... | a_n)
      = sum_{consecutive triples (i,i+1,i+2)}
           (a_0 | ... | m_3(a_i, a_{i+1}, a_{i+2}) | ... | a_n)

with appropriate signs.  The commutator

    [m_3^{CC}, B^{(2)}_term]
      = m_3^{CC} circ B^{(2)}_term - B^{(2)}_term circ m_3^{CC}

is the raw termwise object tested here.  Nonzero output is a witness.
Zero output in a finite sample is only absence of a witness in that sample.

IMPLEMENTATION STRATEGY
========================

1. Generate random m_2 (associative): random structure constants, then
   project onto the associative cone via repeated averaging.
2. Generate random m_3: random Hochschild 3-cocycle for m_2, via the
   kernel of the Hochschild coboundary.
3. Generate random cyclic pairing: random nondegenerate symmetric form,
   then enforce cyclic invariance with m_2 and m_3.
4. Construct the raw terminal-slot B^{(2)}_term matrix using the pairing.
5. Compute [m_3^{CC}, B^{(2)}_term] and record candidate witnesses.

For efficiency, we work with structure constants stored as numpy arrays.

CONVENTIONS
===========
  - Cohomological grading (|d| = +1).
  - Numerical search: degree-0 vector space throughout.
  - Strict witness: graded CY3 convention from
    standalone/m3_b2_obstruction_vol3.tex.
  - m_1 = 0, m_k = 0 for k >= 4 (minimal A_infinity).
  - kappa_ch subscript: always from the chiral algebra (AP113).
  - CY_3 pairing in degree 3: the inner product pairs total degree to d.

REFERENCES
==========
  - Keller (2006): A-infinity algebras, modules and transfer.
  - Kontsevich-Soibelman (2000): A_infinity categories.
  - Costello (math/0412149): TCFTs and Calabi-Yau categories.
  - Tradler (2008): The BV algebra on Hochschild cohomology.
  - Vol III: hopf_fibration_s3_framing.py (B^{(2)} and Obs_Ainf).
  - Vol III: a_infinity_bar_w1inf.py (A_infinity bar complex).
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, Tuple

import numpy as np
from numpy.typing import NDArray

Word = Tuple[str, ...]


# =========================================================================
#  Exact strict CY3 witness
# =========================================================================

_STRICT_PAIRING: Dict[Tuple[str, str], Fraction] = {
    ("a", "b"): Fraction(1),
}


def _clean_counter(counter: Counter[Word]) -> Dict[Word, Fraction]:
    """Return a plain dict with zero coefficients removed."""
    return {word: coeff for word, coeff in counter.items() if coeff != 0}


def _terminal_slot_b2_term_exact(word: Word) -> Dict[Word, Fraction]:
    r"""Terminal-slot raw ``B^{(2)}_term`` for the strict witness.

    The terminal input is contracted with each earlier input.  The signs
    are the normalized signs of the standalone strict CY3 witness on
    ``[a|a|a|a|b]``.
    """
    terminal = word[-1]
    out: Counter[Word] = Counter()
    for idx, entry in enumerate(word[:-1]):
        coeff = _STRICT_PAIRING.get((entry, terminal), Fraction(0))
        if coeff:
            reduced = word[:idx] + word[idx + 1:-1]
            out[reduced] += coeff
    return _clean_counter(out)


def _m3_bar_exact(word: Word, alpha: Fraction) -> Dict[Word, Fraction]:
    """Minimal strict witness operation ``m_3(a,a,a)=alpha b``."""
    out: Counter[Word] = Counter()
    for start in range(len(word) - 2):
        if word[start:start + 3] == ("a", "a", "a"):
            reduced = word[:start] + ("b",) + word[start + 3:]
            out[reduced] += alpha
    return _clean_counter(out)


def _compose_exact(first, second, word: Word) -> Dict[Word, Fraction]:
    """Apply ``first`` and then ``second`` to a word."""
    total: Counter[Word] = Counter()
    for mid, coeff_mid in first(word).items():
        for out, coeff_out in second(mid).items():
            total[out] += coeff_mid * coeff_out
    return _clean_counter(total)


def _subtract_exact(
    left: Dict[Word, Fraction], right: Dict[Word, Fraction]
) -> Dict[Word, Fraction]:
    total: Counter[Word] = Counter(left)
    for word, coeff in right.items():
        total[word] -= coeff
    return _clean_counter(total)


@dataclass(frozen=True)
class StrictCyclicCY3Witness:
    """Exact strict witness for raw ``[m_3, B^{(2)}_term]`` nonvanishing."""

    alpha: Fraction
    input_word: Word
    b2_term_of_input: Dict[Word, Fraction]
    m3_after_b2_term: Dict[Word, Fraction]
    m3_of_input: Dict[Word, Fraction]
    b2_term_after_m3: Dict[Word, Fraction]
    commutator: Dict[Word, Fraction]
    convention: str

    @property
    def coefficient_on_b(self) -> Fraction:
        return self.commutator.get(("b",), Fraction(0))

    @property
    def nonzero(self) -> bool:
        return any(coeff != 0 for coeff in self.commutator.values())


def strict_cyclic_cy3_witness(alpha: Fraction = Fraction(1)) -> StrictCyclicCY3Witness:
    r"""Return the exact strict cyclic CY3 witness.

    With the terminal-slot normalization,

    * ``B^{(2)}_term [a|a|a|a|b] = 4 [a|a|a]``;
    * ``m_3 B^{(2)}_term`` gives ``4 alpha [b]``;
    * ``m_3`` first gives ``alpha([b|a|b] + [a|b|b])``;
    * ``B^{(2)}_term m_3`` gives ``2 alpha [b]``.
    """
    alpha = Fraction(alpha)
    input_word = ("a", "a", "a", "a", "b")
    b2_term_of_input = _terminal_slot_b2_term_exact(input_word)
    m3_after_b2_term = _compose_exact(
        _terminal_slot_b2_term_exact,
        lambda word: _m3_bar_exact(word, alpha),
        input_word,
    )
    m3_of_input = _m3_bar_exact(input_word, alpha)
    b2_term_after_m3 = _compose_exact(
        lambda word: _m3_bar_exact(word, alpha),
        _terminal_slot_b2_term_exact,
        input_word,
    )
    commutator = _subtract_exact(m3_after_b2_term, b2_term_after_m3)

    return StrictCyclicCY3Witness(
        alpha=alpha,
        input_word=input_word,
        b2_term_of_input=b2_term_of_input,
        m3_after_b2_term=m3_after_b2_term,
        m3_of_input=m3_of_input,
        b2_term_after_m3=b2_term_after_m3,
        commutator=commutator,
        convention="terminal-slot B^(2)_term, strict graded CY3 witness",
    )


# =========================================================================
#  0.  Random cyclic A_infinity algebra generator
# =========================================================================

def _random_associative_product(d: int, rng: np.random.Generator) -> NDArray:
    r"""Generate a random associative product m_2 on k^d.

    Strategy: embed V = k^d into Mat_n(k) via a random injective linear
    map, use matrix multiplication as the product, then express back in
    the original basis.

    Key insight: we need n large enough that n^2 >= d (so that d vectors
    can be linearly independent in Mat_n).  We choose n = d to guarantee
    this with room to spare.

    The product is EXACTLY associative because it inherits associativity
    from Mat_n(k), and we express products exactly in the original basis
    via Moore-Penrose pseudoinverse (no projection error).

    Parameters
    ----------
    d : int
        Dimension of the vector space.
    rng : np.random.Generator
        Random number generator.

    Returns
    -------
    m2 : ndarray of shape (d, d, d)
        Structure constants: m2[i,j,k] = coefficient of e_k in m_2(e_i, e_j).
    """
    # Choose n = d: the ambient matrix algebra is Mat_d(k),
    # and we embed d basis vectors as random d x d matrices.
    n = d

    # Generate d random n x n matrices as basis elements
    basis_flat = rng.standard_normal((d, n * n))

    # Orthonormalize: now basis_flat[i] are orthonormal in R^{n^2}
    Q, _ = np.linalg.qr(basis_flat.T)
    # Q is (n^2, d) with orthonormal columns, take first d columns
    basis_flat = Q[:, :d].T  # (d, n^2), orthonormal rows

    basis = basis_flat.reshape(d, n, n)

    # Compute structure constants.
    # m_2(e_i, e_j) = basis[i] @ basis[j] (matrix product).
    # Express the product in the basis: since the basis is orthonormal
    # in R^{n^2}, the coefficient of e_k is <basis_flat[k], prod_flat>.
    # The product basis[i]@basis[j] may have components OUTSIDE span(basis),
    # so we project onto the subspace.  The projected product is still
    # associative because projection onto a subalgebra of an associative
    # algebra is associative IF AND ONLY IF the subspace is closed under
    # the product.
    #
    # Since a random d-dim subspace of Mat_d is NOT closed under multiplication,
    # we use a different approach: use the FULL structure constants, including
    # the truncation.  To guarantee exact associativity, we instead construct
    # an actual d-dimensional subalgebra.
    #
    # CORRECT APPROACH: use the path algebra of a random quiver, or
    # a direct sum of 1-dim algebras, or truncated polynomial rings.
    #
    # Most reliable: direct sum of 1-dim algebras k^d with componentwise
    # multiplication, conjugated by a random invertible matrix.

    # e_i * e_j = delta_{ij} * e_i in the standard basis of k^d.
    # Conjugate by a random invertible P: new basis f_i = P e_i.
    # Then f_i * f_j = P (P^{-1} f_i * P^{-1} f_j) = P (e_i * e_j)
    #               = delta_{ij} * P e_i = delta_{ij} * f_i.
    # Structure constants: m2'[i,j,k] = (P^{-1})_{ki} * delta_{ij}... no.
    #
    # Actually, let the multiplication be: mu(a,b) = P (P^{-1}a . P^{-1}b)
    # where . is componentwise multiplication.
    # In components: mu(e_i, e_j)_l = sum_m P_{lm} * (P^{-1})_{mi} * (P^{-1})_{mj}
    # i.e. m2[i,j,l] = sum_m P[l,m] * Pinv[m,i] * Pinv[m,j]
    #
    # This is associative because componentwise mult is associative and
    # P is just a change of basis.

    P = rng.standard_normal((d, d))
    # Ensure invertibility
    while abs(np.linalg.det(P)) < 1e-6:
        P = rng.standard_normal((d, d))
    Pinv = np.linalg.inv(P)

    # m2[i,j,l] = sum_m P[l,m] * Pinv[m,i] * Pinv[m,j]
    m2 = np.einsum('lm,mi,mj->ijl', P, Pinv, Pinv)

    return m2


def _verify_associativity(m2: NDArray, tol: float = 1e-10) -> float:
    r"""Verify associativity: m_2(m_2(a,b),c) = m_2(a, m_2(b,c)).

    Returns the maximum associator norm.
    """
    d = m2.shape[0]
    max_err = 0.0
    for i in range(d):
        for j in range(d):
            for k in range(d):
                # m_2(m_2(e_i, e_j), e_k)
                lhs = np.zeros(d)
                for p in range(d):
                    lhs += m2[i, j, p] * m2[p, k, :]

                # m_2(e_i, m_2(e_j, e_k))
                rhs = np.zeros(d)
                for p in range(d):
                    rhs += m2[j, k, p] * m2[i, p, :]

                err = np.max(np.abs(lhs - rhs))
                max_err = max(max_err, err)
    return max_err


def _random_hochschild_3cocycle(
    m2: NDArray, rng: np.random.Generator, scale: float = 1.0
) -> NDArray:
    r"""Generate a random Hochschild 3-cocycle m_3 for the associative product m_2.

    The Hochschild coboundary delta^3: Hom(V^3, V) -> Hom(V^4, V) is:

        (delta m_3)(a,b,c,d) = m_2(a, m_3(b,c,d)) - m_3(m_2(a,b),c,d)
                                + m_3(a, m_2(b,c), d) - m_3(a, b, m_2(c,d))
                                + m_2(m_3(a,b,c), d)

    A cocycle satisfies delta m_3 = 0, which is exactly the Stasheff
    identity (S2) at arity 4 with m_1 = m_4 = 0.

    Strategy: generate a random element of Hom(V^3, V), then project
    onto the kernel of delta^3 using the SVD.

    Parameters
    ----------
    m2 : ndarray of shape (d, d, d)
        Associative product structure constants.
    rng : np.random.Generator
        Random number generator.
    scale : float
        Scale of the random m_3.

    Returns
    -------
    m3 : ndarray of shape (d, d, d, d)
        Structure constants: m3[i,j,k,l] = coeff of e_l in m_3(e_i, e_j, e_k).
    """
    d = m2.shape[0]

    # Build the coboundary matrix delta^3 as a linear map
    # from Hom(V^3, V) = R^{d^4} to Hom(V^4, V) = R^{d^5}.
    #
    # For each (a,b,c,d,l) in {0,...,d-1}^5, the coboundary applied to
    # m_3 (viewed as a d^4-vector indexed by (i,j,k,l)) gives:
    #
    # (delta m_3)[a,b,c,d,l] = sum_p m2[a,p,l] * m3[b,c,d,p]
    #                         - sum_p m3[p,c,d,l] * m2[a,b,p]
    #                         + sum_p m3[a,p,d,l] * m2[b,c,p]
    #                         - sum_p m3[a,b,p,l] * m2[c,d,p]
    #                         + sum_p m2[p,d,l] * m3[a,b,c,p]  -- WRONG indices
    #
    # Let me be careful. The coboundary is:
    # (delta m_3)(a,b,c,d) = m_2(a, m_3(b,c,d)) - m_3(m_2(a,b), c, d)
    #                       + m_3(a, m_2(b,c), d) - m_3(a, b, m_2(c,d))
    #                       + m_2(m_3(a,b,c), d)
    #
    # In components (output index l):
    # (delta m_3)[a,b,c,d,l]
    #   = sum_p m2[a,p,l] * (sum_q m3[b,c,d,q] delta_{p,q})   -- no, simpler
    #   = sum_p m2[a,p,l] * m3[b,c,d,p]                       (term 1)
    #   - sum_p m3[p,c,d,l] * m2[a,b,p]                       (term 2)
    #   + sum_p m3[a,p,d,l] * m2[b,c,p]                       (term 3)
    #   - sum_p m3[a,b,p,l] * m2[c,d,p]                       (term 4)
    #   + sum_p m2[p,d,l] * m3[a,b,c,p]                       (term 5)

    # Build delta as a matrix: delta[out_idx, in_idx] where
    # out_idx = (a,b,c,d,l) -> a*d^4 + b*d^3 + c*d^2 + d_idx*d + l
    # in_idx  = (i,j,k,l)   -> i*d^3 + j*d^2 + k*d + l

    n_in = d ** 4   # dimension of Hom(V^3, V)
    n_out = d ** 5  # dimension of Hom(V^4, V)

    # For large d, building the full matrix is expensive. For d <= 8,
    # d^5 <= 32768 which is manageable.
    delta = np.zeros((n_out, n_in))

    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    for l in range(d):
                        out_idx = ((a * d + b) * d + c) * d * d + dd * d + l

                        # Term 1: +m2[a,p,l] * m3[b,c,dd,p]
                        for p in range(d):
                            in_idx = ((b * d + c) * d + dd) * d + p
                            delta[out_idx, in_idx] += m2[a, p, l]

                        # Term 2: -m3[p,c,dd,l] * m2[a,b,p]
                        for p in range(d):
                            in_idx = ((p * d + c) * d + dd) * d + l
                            delta[out_idx, in_idx] -= m2[a, b, p]

                        # Term 3: +m3[a,p,dd,l] * m2[b,c,p]
                        for p in range(d):
                            in_idx = ((a * d + p) * d + dd) * d + l
                            delta[out_idx, in_idx] += m2[b, c, p]

                        # Term 4: -m3[a,b,p,l] * m2[c,dd,p]
                        for p in range(d):
                            in_idx = ((a * d + b) * d + p) * d + l
                            delta[out_idx, in_idx] -= m2[c, dd, p]

                        # Term 5: +m2[p,dd,l] * m3[a,b,c,p]
                        for p in range(d):
                            in_idx = ((a * d + b) * d + c) * d + p
                            delta[out_idx, in_idx] += m2[p, dd, l]

    # Find the kernel of delta using SVD
    U, S, Vt = np.linalg.svd(delta, full_matrices=True)
    # Kernel = rows of Vt corresponding to zero singular values
    tol = 1e-8 * max(S[0], 1.0)
    kernel_mask = np.arange(len(S), Vt.shape[0])
    # Also include singular values below tolerance
    kernel_mask2 = np.where(S < tol)[0]
    kernel_indices = np.concatenate([kernel_mask2, kernel_mask])
    kernel_indices = np.unique(kernel_indices)

    if len(kernel_indices) == 0:
        # No cocycles exist (only for very degenerate algebras)
        return np.zeros((d, d, d, d))

    # Random combination of kernel vectors
    kernel_basis = Vt[kernel_indices]  # shape (n_kernel, d^4)
    coeffs = rng.standard_normal(len(kernel_indices))
    m3_flat = scale * (coeffs @ kernel_basis)
    m3 = m3_flat.reshape(d, d, d, d)

    return m3


def _verify_hochschild_cocycle(m2: NDArray, m3: NDArray, tol: float = 1e-8) -> float:
    r"""Verify the Stasheff identity (S2): delta m_3 = 0.

    Returns the maximum error.
    """
    d = m2.shape[0]
    max_err = 0.0

    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    # (delta m_3)(a,b,c,dd) should be zero (as a vector in V)
                    result = np.zeros(d)

                    # Term 1: m_2(e_a, m_3(e_b, e_c, e_dd))
                    for p in range(d):
                        result += m3[b, c, dd, p] * m2[a, p, :]

                    # Term 2: -m_3(m_2(e_a, e_b), e_c, e_dd)
                    for p in range(d):
                        result -= m2[a, b, p] * m3[p, c, dd, :]

                    # Term 3: +m_3(e_a, m_2(e_b, e_c), e_dd)
                    for p in range(d):
                        result += m2[b, c, p] * m3[a, p, dd, :]

                    # Term 4: -m_3(e_a, e_b, m_2(e_c, e_dd))
                    for p in range(d):
                        result -= m2[c, dd, p] * m3[a, b, p, :]

                    # Term 5: +m_2(m_3(e_a, e_b, e_c), e_dd)
                    for p in range(d):
                        result += m3[a, b, c, p] * m2[p, dd, :]

                    err = np.max(np.abs(result))
                    max_err = max(max_err, err)

    return max_err


def _make_cyclic_pairing(
    d: int, m2: NDArray, m3: NDArray, rng: np.random.Generator
) -> NDArray:
    r"""Generate a nondegenerate cyclic pairing compatible with m_2 and m_3.

    Strategy:
    1. Start with a random nondegenerate symmetric bilinear form eta.
    2. Symmetrize m_2 cyclicity: solve for eta such that
       eta[m_2(a,b), c] = eta[a, m_2(b,c)] for all a,b,c.
    3. Then verify/enforce the m_3 cyclic invariance.

    For the matrix algebra approach used in _random_associative_product,
    the trace form Tr(AB) is automatically cyclic for m_2.  We use this
    plus a random perturbation projected onto the cyclic constraint.

    Parameters
    ----------
    d : int
        Dimension.
    m2 : ndarray of shape (d, d, d)
        Associative product.
    m3 : ndarray of shape (d, d, d, d)
        Hochschild 3-cocycle.
    rng : np.random.Generator
        Random number generator.

    Returns
    -------
    eta : ndarray of shape (d, d)
        Nondegenerate symmetric bilinear form satisfying cyclic invariance.
    """
    # Build the cyclic constraint for m_2:
    # eta[sum_k m2[i,j,k] * e_k, e_l] = eta[e_i, sum_k m2[j,l,k] * e_k]
    # i.e. sum_k m2[i,j,k] * eta[k,l] = sum_k m2[j,l,k] * eta[i,k]
    # This is a linear constraint on the d^2 entries of eta (symmetric).

    # Number of unknowns: d*(d+1)/2 (symmetric matrix)
    n_unk = d * (d + 1) // 2

    # Map (i,j) with i <= j to index
    def sym_idx(i: int, j: int) -> int:
        a, b = min(i, j), max(i, j)
        return a * d - a * (a - 1) // 2 + (b - a)

    # Build constraint matrix for m_2 cyclicity
    # For each (i,j,l): sum_k m2[i,j,k]*eta[k,l] - sum_k m2[j,l,k]*eta[i,k] = 0
    constraints_m2 = []
    for i in range(d):
        for j in range(d):
            for l in range(d):
                row = np.zeros(n_unk)
                for k in range(d):
                    row[sym_idx(k, l)] += m2[i, j, k]
                    row[sym_idx(i, k)] -= m2[j, l, k]
                constraints_m2.append(row)

    A_m2 = np.array(constraints_m2)

    # Find the kernel of the m_2-cyclic constraint
    U, S, Vt = np.linalg.svd(A_m2, full_matrices=True)
    tol = 1e-8 * max(S[0] if len(S) > 0 else 1.0, 1.0)
    kernel_mask = np.arange(len(S), Vt.shape[0])
    kernel_mask2 = np.where(S < tol)[0] if len(S) > 0 else np.array([], dtype=int)
    kernel_indices = np.unique(np.concatenate([kernel_mask2, kernel_mask]))

    if len(kernel_indices) == 0:
        # No cyclic pairing exists for m_2 -- degenerate case
        return np.eye(d)

    kernel_basis = Vt[kernel_indices]

    # Try random combinations until we get a nondegenerate pairing
    for _attempt in range(100):
        coeffs = rng.standard_normal(len(kernel_indices))
        eta_flat = coeffs @ kernel_basis
        eta = np.zeros((d, d))
        for i in range(d):
            for j in range(i, d):
                idx = sym_idx(i, j)
                eta[i, j] = eta_flat[idx]
                eta[j, i] = eta_flat[idx]

        if abs(np.linalg.det(eta)) > 1e-6:
            return eta

    # Fallback: identity + small perturbation
    return np.eye(d)


def _verify_m2_cyclic(m2: NDArray, eta: NDArray, tol: float = 1e-8) -> float:
    r"""Verify cyclic invariance of m_2: <m_2(a,b), c> = <a, m_2(b,c)>.

    Returns the maximum error.
    """
    d = m2.shape[0]
    max_err = 0.0
    for i in range(d):
        for j in range(d):
            for k in range(d):
                # <m_2(e_i, e_j), e_k> = sum_p m2[i,j,p] * eta[p,k]
                lhs = np.dot(m2[i, j, :], eta[:, k])
                # <e_i, m_2(e_j, e_k)> = sum_p m2[j,k,p] * eta[i,p]
                rhs = np.dot(eta[i, :], m2[j, k, :])
                err = abs(lhs - rhs)
                max_err = max(max_err, err)
    return max_err


def _verify_m3_cyclic(m3: NDArray, eta: NDArray, tol: float = 1e-8) -> float:
    r"""Verify cyclic invariance of m_3:

    <m_3(a,b,c), d> + <m_3(b,c,d), a> + <m_3(c,d,a), b> + <m_3(d,a,b), c> = 0

    (for degree-0 elements, the signs are all +1).

    Returns the maximum error.
    """
    d = m3.shape[0]
    max_err = 0.0
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    # <m_3(i,j,k), l> + <m_3(j,k,l), i>
                    # + <m_3(k,l,i), j> + <m_3(l,i,j), k>
                    val = (np.dot(m3[i, j, k, :], eta[:, l])
                           + np.dot(m3[j, k, l, :], eta[:, i])
                           + np.dot(m3[k, l, i, :], eta[:, j])
                           + np.dot(m3[l, i, j, :], eta[:, k]))
                    max_err = max(max_err, abs(val))
    return max_err


def _project_m3_cyclic(m3: NDArray, eta: NDArray) -> NDArray:
    r"""Project m_3 onto the subspace satisfying cyclic invariance with eta.

    The cyclic constraint is linear in m_3:
        sum over (i,j,k,l) cyclic rotations of <m_3(e_i, e_j, e_k), e_l> = 0

    We project m_3 (as a d^4-vector) onto the kernel of this constraint.
    """
    d = m3.shape[0]

    # Build constraint matrix for the 4-fold cyclic sum
    # For each (i,j,k,l):
    #   sum_p m3[i,j,k,p]*eta[p,l] + sum_p m3[j,k,l,p]*eta[p,i]
    #   + sum_p m3[k,l,i,p]*eta[p,j] + sum_p m3[l,i,j,p]*eta[p,k] = 0
    #
    # This is linear in the d^4 entries of m3.
    # Constraint: for each (i,j,k,l), we get a row of a matrix C
    # such that C @ m3_flat = 0.

    n_vars = d ** 4
    constraints = []

    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    row = np.zeros(n_vars)
                    for p in range(d):
                        # Term 1: m3[i,j,k,p] * eta[p,l]
                        idx1 = ((i * d + j) * d + k) * d + p
                        row[idx1] += eta[p, l]
                        # Term 2: m3[j,k,l,p] * eta[p,i]
                        idx2 = ((j * d + k) * d + l) * d + p
                        row[idx2] += eta[p, i]
                        # Term 3: m3[k,l,i,p] * eta[p,j]
                        idx3 = ((k * d + l) * d + i) * d + p
                        row[idx3] += eta[p, j]
                        # Term 4: m3[l,i,j,p] * eta[p,k]
                        idx4 = ((l * d + i) * d + j) * d + p
                        row[idx4] += eta[p, k]
                    constraints.append(row)

    C = np.array(constraints)

    # Project m3_flat onto ker(C)
    m3_flat = m3.reshape(-1)
    U, S, Vt = np.linalg.svd(C, full_matrices=True)
    tol = 1e-8 * max(S[0] if len(S) > 0 else 1.0, 1.0)
    n_sing = len(S)
    kernel_indices = list(range(n_sing, Vt.shape[0]))
    kernel_indices.extend(i for i in range(n_sing) if S[i] < tol)
    kernel_indices = sorted(set(kernel_indices))

    if len(kernel_indices) == 0:
        return np.zeros_like(m3)

    V_ker = Vt[kernel_indices].T  # (d^4, n_kernel)
    # Project: m3_proj = V_ker @ V_ker^T @ m3_flat
    m3_proj = V_ker @ (V_ker.T @ m3_flat)
    return m3_proj.reshape(d, d, d, d)


# =========================================================================
#  1.  Hochschild chain complex operations
# =========================================================================

def _cc_basis(d: int, n: int) -> int:
    r"""Dimension of CC_n(A) = A^{otimes(n+1)} for dim(A) = d."""
    return d ** (n + 1)


def _cc_index(indices: Tuple[int, ...], d: int) -> int:
    r"""Flat index for a Hochschild chain a_0 | a_1 | ... | a_n.

    indices = (a_0, a_1, ..., a_n), each in {0, ..., d-1}.
    """
    idx = 0
    for i in indices:
        idx = idx * d + i
    return idx


def _cc_indices(flat_idx: int, d: int, n: int) -> Tuple[int, ...]:
    r"""Recover (a_0, ..., a_n) from a flat index."""
    result = []
    for _ in range(n + 1):
        result.append(flat_idx % d)
        flat_idx //= d
    return tuple(reversed(result))


def build_b2_matrix(d: int, n: int, eta: NDArray) -> NDArray:
    r"""Build the matrix of raw terminal-slot ``B^{(2)}_term``.

    On a Hochschild word with terminal input,

        B^{(2)}_term[u_1|...|u_r|v]
          = sum_i <u_i, v> [u_1|...|hat{u_i}|...|u_r].

    Thus ``B^{(2)}_term`` removes two slots and maps ``CC_n`` to
    ``CC_{n-2}``.  The strict graded CY3 signs are encoded by
    ``strict_cyclic_cy3_witness``; this matrix uses the ungraded
    terminal-slot convention for numerical falsification searches.

    Parameters
    ----------
    d : int
        Dimension of A.
    n : int
        Hochschild chain degree (B^{(2)}_term: CC_n -> CC_{n-2}).
    eta : ndarray of shape (d, d)
        The cyclic pairing.

    Returns
    -------
    B2 : ndarray of shape (dim(CC_{n-2}), dim(CC_n))
        Matrix of raw ``B^{(2)}_term``.
    """
    if n < 1:
        # There is no earlier slot to pair with the terminal input.
        return np.zeros((1, d))

    dim_in = d ** (n + 1)  # CC_n
    dim_out = d ** max(n - 1, 0)  # CC_{n-2}

    B2 = np.zeros((dim_out, dim_in))

    # Iterate over all basis elements of CC_n
    for flat_in in range(dim_in):
        indices = _cc_indices(flat_in, d, n)
        terminal = indices[-1]

        # Contract the terminal slot with each earlier slot.
        for i in range(n):
            pairing_val = eta[indices[i], terminal]
            if abs(pairing_val) < 1e-15:
                continue

            out_indices = indices[:i] + indices[i + 1:-1]
            flat_out = _cc_index(out_indices, d) if out_indices else 0
            B2[flat_out, flat_in] += pairing_val

    return B2


def build_m3_cc_matrix(d: int, n: int, m3: NDArray) -> NDArray:
    r"""Build the matrix of m_3^{CC}: CC_n -> CC_{n-2}.

    The induced m_3 on Hochschild chains acts by applying m_3 to
    consecutive triples:

        m_3^{CC}(a_0 | a_1 | ... | a_n)
          = sum_{i=0}^{n-2} (-1)^{...}
              (a_0 | ... | a_{i-1} | m_3(a_i, a_{i+1}, a_{i+2}) | a_{i+3} | ... | a_n)

    The matrix uses the same ungraded signless convention as the
    terminal-slot witness-search surface.

    Parameters
    ----------
    d : int
        Dimension of A.
    n : int
        Hochschild chain degree (m_3^{CC}: CC_n -> CC_{n-2}).
    m3 : ndarray of shape (d, d, d, d)
        Structure constants of m_3.

    Returns
    -------
    M3 : ndarray of shape (dim(CC_{n-2}), dim(CC_n))
        Matrix of m_3^{CC}.
    """
    if n < 2:
        # m_3 needs at least 3 consecutive elements; CC_n has n+1 slots
        # m_3^{CC}: CC_n -> CC_{n-2} needs n+1 >= 3, i.e. n >= 2
        dim_in = d ** (n + 1)
        dim_out = d ** max(n - 1, 0)
        return np.zeros((dim_out, dim_in))

    dim_in = d ** (n + 1)   # CC_n
    dim_out = d ** (n - 1)  # CC_{n-2}

    M3 = np.zeros((dim_out, dim_in))

    for flat_in in range(dim_in):
        indices = _cc_indices(flat_in, d, n)

        # Apply m_3 to each consecutive triple (i, i+1, i+2)
        for i in range(n - 1):  # i ranges from 0 to n-2
            a_i, a_ip1, a_ip2 = indices[i], indices[i + 1], indices[i + 2]

            # m_3(a_i, a_{i+1}, a_{i+2}) = sum_p m3[a_i, a_ip1, a_ip2, p] * e_p
            for p in range(d):
                coeff = m3[a_i, a_ip1, a_ip2, p]
                if abs(coeff) < 1e-15:
                    continue

                # Output: (a_0, ..., a_{i-1}, p, a_{i+3}, ..., a_n)
                out_indices = indices[:i] + (p,) + indices[i + 3:]
                flat_out = _cc_index(out_indices, d)
                M3[flat_out, flat_in] += coeff

    return M3


# =========================================================================
#  2.  The commutator [m_3, B^{(2)}_term]
# =========================================================================

def compute_commutator_m3_b2(
    d: int, n: int, m3: NDArray, eta: NDArray
) -> NDArray:
    r"""Compute raw ``[m_3^{CC}, B^{(2)}_term]`` on ``CC_n``.

    The graded commutator is:

        [m_3^{CC}, B^{(2)}_term]
          = m_3^{CC} circ B^{(2)}_term
            - B^{(2)}_term circ m_3^{CC}.

    Both ``m_3`` and this raw terminal-slot ``B^{(2)}_term`` lower bar
    length by two, so both compositions land in ``CC_{n-4}``.  For the
    strict witness this is the map from ``[a|a|a|a|b]`` to ``[b]``.

    Parameters
    ----------
    d : int
        Dimension of A.
    n : int
        Hochschild chain degree.
    m3 : ndarray of shape (d, d, d, d)
        Structure constants of m_3.
    eta : ndarray of shape (d, d)
        Cyclic pairing.

    Returns
    -------
    comm : ndarray of shape (dim(CC_{n-4}), dim(CC_n))
        Matrix of raw ``[m_3^{CC}, B^{(2)}_term]``.
    """
    # m_3 o B^{(2)}_term: CC_n -> CC_{n-2} -> CC_{n-4}
    B2_n = build_b2_matrix(d, n, eta)
    M3_nm2 = build_m3_cc_matrix(d, n - 2, m3)

    # B^{(2)}_term o m_3: CC_n -> CC_{n-2} -> CC_{n-4}
    M3_n = build_m3_cc_matrix(d, n, m3)
    B2_nm2 = build_b2_matrix(d, n - 2, eta)

    term1 = M3_nm2 @ B2_n
    term2 = B2_nm2 @ M3_n

    return term1 - term2


# =========================================================================
#  3.  Random cyclic A_infinity algebra: combined generator
# =========================================================================

@dataclass
class RandomCyclicAInfAlgebra:
    r"""A random cyclic A_infinity algebra (V, m_2, m_3, eta).

    Attributes
    ----------
    d : int
        Dimension of V.
    m2 : ndarray of shape (d, d, d)
        Associative product structure constants.
    m3 : ndarray of shape (d, d, d, d)
        Hochschild 3-cocycle structure constants.
    eta : ndarray of shape (d, d)
        Nondegenerate cyclic pairing.
    assoc_error : float
        Maximum associativity error of m2.
    cocycle_error : float
        Maximum Hochschild cocycle error of m3.
    m2_cyclic_error : float
        Maximum m2 cyclic invariance error.
    m3_cyclic_error : float
        Maximum m3 cyclic invariance error.
    m3_norm : float
        Frobenius norm of m3 (to distinguish from trivial m3=0).
    """
    d: int
    m2: NDArray
    m3: NDArray
    eta: NDArray
    assoc_error: float
    cocycle_error: float
    m2_cyclic_error: float
    m3_cyclic_error: float
    m3_norm: float


def generate_random_cyclic_ainf(
    d: int, rng: np.random.Generator, m3_scale: float = 1.0
) -> RandomCyclicAInfAlgebra:
    r"""Generate a random cyclic A_infinity algebra of dimension d.

    Parameters
    ----------
    d : int
        Dimension of V.
    rng : np.random.Generator
        Random number generator.
    m3_scale : float
        Scale factor for m_3 (larger = more non-formal).

    Returns
    -------
    RandomCyclicAInfAlgebra
        The generated algebra with all structure constants and error metrics.
    """
    # Step 1: random associative product
    m2 = _random_associative_product(d, rng)
    assoc_err = _verify_associativity(m2)

    # Step 2: random Hochschild 3-cocycle
    m3_raw = _random_hochschild_3cocycle(m2, rng, scale=m3_scale)

    # Step 3: random cyclic pairing compatible with m_2
    eta = _make_cyclic_pairing(d, m2, m3_raw, rng)
    m2_cyc_err = _verify_m2_cyclic(m2, eta)

    # Step 4: project m_3 onto cyclic invariance
    m3 = _project_m3_cyclic(m3_raw, eta)

    # Re-verify cocycle condition (projection should preserve it
    # if both constraints are compatible)
    cocycle_err = _verify_hochschild_cocycle(m2, m3)
    m3_cyc_err = _verify_m3_cyclic(m3, eta)

    # If projection broke the cocycle condition, re-project onto cocycle
    # AND cyclic simultaneously
    if cocycle_err > 1e-6:
        # Joint projection: intersect cocycle kernel with cyclic kernel
        m3 = _joint_project_cocycle_cyclic(m2, eta, m3_raw, rng)
        cocycle_err = _verify_hochschild_cocycle(m2, m3)
        m3_cyc_err = _verify_m3_cyclic(m3, eta)

    m3_norm = float(np.linalg.norm(m3))

    return RandomCyclicAInfAlgebra(
        d=d,
        m2=m2,
        m3=m3,
        eta=eta,
        assoc_error=assoc_err,
        cocycle_error=cocycle_err,
        m2_cyclic_error=m2_cyc_err,
        m3_cyclic_error=m3_cyc_err,
        m3_norm=m3_norm,
    )


def _joint_project_cocycle_cyclic(
    m2: NDArray, eta: NDArray, m3_raw: NDArray, rng: np.random.Generator
) -> NDArray:
    r"""Project m_3 onto the intersection of cocycle and cyclic constraints.

    This builds both constraint matrices and finds their joint kernel,
    then projects m3_raw onto it.
    """
    d = m2.shape[0]
    n_vars = d ** 4

    # Build cocycle constraint matrix (Stasheff S2)
    cocycle_rows = []
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    for l in range(d):
                        row = np.zeros(n_vars)
                        for p in range(d):
                            # Term 1: +m2[a,p,l] * m3[b,c,dd,p]
                            row[((b * d + c) * d + dd) * d + p] += m2[a, p, l]
                            # Term 2: -m2[a,b,p] * m3[p,c,dd,l]
                            row[((p * d + c) * d + dd) * d + l] -= m2[a, b, p]
                            # Term 3: +m2[b,c,p] * m3[a,p,dd,l]
                            row[((a * d + p) * d + dd) * d + l] += m2[b, c, p]
                            # Term 4: -m2[c,dd,p] * m3[a,b,p,l]
                            row[((a * d + b) * d + p) * d + l] -= m2[c, dd, p]
                            # Term 5: +m2[p,dd,l] * m3[a,b,c,p]
                            row[((a * d + b) * d + c) * d + p] += m2[p, dd, l]
                        cocycle_rows.append(row)

    # Build cyclic constraint matrix (m_3 cyclic invariance)
    cyclic_rows = []
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    row = np.zeros(n_vars)
                    for p in range(d):
                        row[((i * d + j) * d + k) * d + p] += eta[p, l]
                        row[((j * d + k) * d + l) * d + p] += eta[p, i]
                        row[((k * d + l) * d + i) * d + p] += eta[p, j]
                        row[((l * d + i) * d + j) * d + p] += eta[p, k]
                    cyclic_rows.append(row)

    # Stack both constraint matrices
    C_cocycle = np.array(cocycle_rows)
    C_cyclic = np.array(cyclic_rows)
    C_joint = np.vstack([C_cocycle, C_cyclic])

    # Find kernel
    U, S, Vt = np.linalg.svd(C_joint, full_matrices=True)
    tol = 1e-8 * max(S[0] if len(S) > 0 else 1.0, 1.0)
    n_sing = len(S)
    kernel_indices = list(range(n_sing, Vt.shape[0]))
    kernel_indices.extend(i for i in range(n_sing) if S[i] < tol)
    kernel_indices = sorted(set(kernel_indices))

    if len(kernel_indices) == 0:
        return np.zeros((d, d, d, d))

    V_ker = Vt[kernel_indices].T
    m3_flat = m3_raw.reshape(-1)
    m3_proj = V_ker @ (V_ker.T @ m3_flat)
    return m3_proj.reshape(d, d, d, d)


# =========================================================================
#  4.  Main experiment: [m_3, B^{(2)}_term] on random cyclic A_inf algebras
# =========================================================================

@dataclass
class TrialResult:
    r"""Result of a single raw [m_3, B^{(2)}_term] trial."""
    trial_idx: int
    d: int
    m3_norm: float
    commutator_norm: float
    assoc_error: float
    cocycle_error: float
    m2_cyclic_error: float
    m3_cyclic_error: float
    is_nontrivial: bool    # m_3 != 0 (above threshold)
    commutator_vanishes: bool  # |[m_3, B^{(2)}_term]| < tolerance


@dataclass
class ExperimentResult:
    r"""Result of the full random search experiment."""
    n_trials: int
    n_dimensions: Dict[int, int]   # d -> count
    n_nontrivial: int              # trials with m_3 != 0
    n_vanishing: int               # trials with raw [m_3, B^{(2)}_term] = 0
    n_nonvanishing: int            # trials with raw [m_3, B^{(2)}_term] != 0
    max_commutator_norm: float
    mean_commutator_norm: float
    max_assoc_error: float
    max_cocycle_error: float
    max_m2_cyclic_error: float
    max_m3_cyclic_error: float
    trials: List[TrialResult]
    conclusion: str

    @property
    def found_candidate_witness(self) -> bool:
        """Whether the finite search found a nonzero numerical commutator."""
        return self.n_nonvanishing > 0

    @property
    def proves_universal_vanishing(self) -> bool:
        """Finite random search never proves universal vanishing."""
        return False


def run_experiment(
    n_trials: int = 100,
    dimensions: Tuple[int, ...] = (3, 4),
    cc_degree: int = 4,
    m3_scale: float = 1.0,
    nontrivial_threshold: float = 1e-8,
    vanishing_tolerance: float = 1e-7,
    seed: int = 42,
    verbose: bool = False,
) -> ExperimentResult:
    r"""Run the finite falsification search.

    For each trial:
    1. Pick a random dimension d from the list.
    2. Generate a random cyclic A_infinity algebra.
    3. Compute raw [m_3^{CC}, B^{(2)}_term] on CC_{cc_degree}.
    4. Record whether the commutator vanishes.

    Parameters
    ----------
    n_trials : int
        Number of random algebras to test (default 100).
    dimensions : tuple of int
        Dimensions to sample from (default (3, 4)).
    cc_degree : int
        Hochschild chain degree to test on (default 4, the degree of the
        strict witness word ``[a|a|a|a|b]``).
    m3_scale : float
        Scale of random m_3 (default 1.0).
    nontrivial_threshold : float
        m_3 is nontrivial if ||m_3|| > this threshold.
    vanishing_tolerance : float
        Raw [m_3, B^{(2)}_term] vanishes if norm < this tolerance.
    seed : int
        Random seed for reproducibility.
    verbose : bool
        Print progress.

    Returns
    -------
    ExperimentResult
        Full results of the experiment.
    """
    rng = np.random.default_rng(seed)
    trials = []
    dim_counts: Dict[int, int] = {d: 0 for d in dimensions}

    for trial_idx in range(n_trials):
        # Pick random dimension
        d = int(rng.choice(dimensions))
        dim_counts[d] = dim_counts.get(d, 0) + 1

        # Generate random cyclic A_infinity algebra
        alg = generate_random_cyclic_ainf(d, rng, m3_scale=m3_scale)

        # Compute raw [m_3, B^{(2)}_term] on CC_{cc_degree}.
        comm = compute_commutator_m3_b2(d, cc_degree, alg.m3, alg.eta)
        comm_norm = float(np.max(np.abs(comm)))

        is_nontrivial = alg.m3_norm > nontrivial_threshold
        comm_vanishes = bool(np.isfinite(comm_norm) and comm_norm < vanishing_tolerance)

        result = TrialResult(
            trial_idx=trial_idx,
            d=d,
            m3_norm=alg.m3_norm,
            commutator_norm=comm_norm,
            assoc_error=alg.assoc_error,
            cocycle_error=alg.cocycle_error,
            m2_cyclic_error=alg.m2_cyclic_error,
            m3_cyclic_error=alg.m3_cyclic_error,
            is_nontrivial=is_nontrivial,
            commutator_vanishes=comm_vanishes,
        )
        trials.append(result)

        if verbose and (trial_idx + 1) % 100 == 0:
            n_nt = sum(1 for t in trials if t.is_nontrivial)
            n_van = sum(1 for t in trials if t.is_nontrivial and t.commutator_vanishes)
            print(
                f"Trial {trial_idx + 1}/{n_trials}: "
                f"{n_nt} nontrivial, {n_van} vanishing "
                f"(max |[m_3,B_term^(2)]| = "
                f"{max(t.commutator_norm for t in trials if t.is_nontrivial):.2e})"
                if n_nt > 0
                else f"Trial {trial_idx + 1}/{n_trials}: {n_nt} nontrivial"
            )

    # Aggregate statistics
    nontrivial_trials = [t for t in trials if t.is_nontrivial]
    n_nontrivial = len(nontrivial_trials)
    n_vanishing = sum(1 for t in nontrivial_trials if t.commutator_vanishes)
    n_nonvanishing = n_nontrivial - n_vanishing

    comm_norms = [t.commutator_norm for t in nontrivial_trials if not np.isnan(t.commutator_norm)]
    max_comm = max(comm_norms) if comm_norms else 0.0
    mean_comm = float(np.mean(comm_norms)) if comm_norms else 0.0

    max_assoc = max((t.assoc_error for t in trials), default=0.0)
    max_cocycle = max((t.cocycle_error for t in trials), default=0.0)
    max_m2_cyc = max((t.m2_cyclic_error for t in trials), default=0.0)
    max_m3_cyc = max((t.m3_cyclic_error for t in trials), default=0.0)

    if n_nonvanishing == 0 and n_nontrivial > 0:
        conclusion = (
            f"NO CANDIDATE WITNESS FOUND in {n_nontrivial} nontrivial "
            f"random cyclic A_infinity samples (out of {n_trials} total trials). "
            f"Maximum commutator norm: {max_comm:.2e}. "
            f"This finite search does not prove universal vanishing."
        )
    elif n_nonvanishing > 0:
        conclusion = (
            f"CANDIDATE WITNESS FOUND: raw [m_3, B_term^(2)] != 0 for "
            f"{n_nonvanishing} / {n_nontrivial} nontrivial samples. "
            f"Maximum commutator norm: {max_comm:.2e}. "
            f"Validate any numerical witness against exact graded signs before use. "
            f"This finite search does not prove universal vanishing."
        )
    else:
        conclusion = (
            f"NO NONTRIVIAL SAMPLE: no nontrivial m_3 found in {n_trials} trials. "
            f"This finite search does not prove universal vanishing."
        )

    return ExperimentResult(
        n_trials=n_trials,
        n_dimensions=dim_counts,
        n_nontrivial=n_nontrivial,
        n_vanishing=n_vanishing,
        n_nonvanishing=n_nonvanishing,
        max_commutator_norm=max_comm,
        mean_commutator_norm=mean_comm,
        max_assoc_error=max_assoc,
        max_cocycle_error=max_cocycle,
        max_m2_cyclic_error=max_m2_cyc,
        max_m3_cyclic_error=max_m3_cyc,
        trials=trials,
        conclusion=conclusion,
    )


# =========================================================================
#  5.  CY_3-specific variant
# =========================================================================

def generate_random_cy3_algebra(
    d: int, rng: np.random.Generator, m3_scale: float = 1.0
) -> RandomCyclicAInfAlgebra:
    r"""Generate a random CY_3 A_infinity algebra.

    A CY_3 algebra has:
    - A nondegenerate pairing of degree 3: <V_i, V_{3-i}> -> k
    - For the graded case, this requires V to be graded.

    For this numerical test, we work in the ungraded case (all generators
    in degree 0), which corresponds to the CY_3 condition on the Hochschild
    chain level.  The key CY_3-specific constraint is that the cyclic
    pairing should be ANTISYMMETRIC (for odd d=3):

        <a, b> = -(-1)^{|a||b|} <b, a>

    For degree-0 elements this means <a,b> = -<b,a> (antisymmetric).

    However, for dim V even, an antisymmetric nondegenerate form exists.
    For dim V odd, we need symmetric (as in CY_2).

    For CY_3 with degree-0 generators: the relevant pairing is
    antisymmetric. So we restrict to even d.

    Parameters
    ----------
    d : int
        Dimension (must be even for CY_3 antisymmetric pairing).
    rng : np.random.Generator
        Random number generator.
    m3_scale : float
        Scale of m_3.

    Returns
    -------
    RandomCyclicAInfAlgebra
        The generated CY_3 algebra.
    """
    if d % 2 != 0:
        raise ValueError(f"CY_3 antisymmetric pairing requires even d, got {d}")

    # Step 1: random associative product
    m2 = _random_associative_product(d, rng)
    assoc_err = _verify_associativity(m2)

    # Step 2: construct an antisymmetric cyclic pairing for m_2
    eta = _make_antisymmetric_cyclic_pairing(d, m2, rng)
    m2_cyc_err = _verify_m2_cyclic(m2, eta)

    # Step 3: random m_3 satisfying BOTH cocycle AND cyclic with antisymmetric eta
    m3 = _random_cocycle_cyclic_m3(m2, eta, rng, scale=m3_scale, antisymmetric=True)
    cocycle_err = _verify_hochschild_cocycle(m2, m3)
    m3_cyc_err = _verify_m3_cyclic_antisym(m3, eta)
    m3_norm = float(np.linalg.norm(m3))

    return RandomCyclicAInfAlgebra(
        d=d,
        m2=m2,
        m3=m3,
        eta=eta,
        assoc_error=assoc_err,
        cocycle_error=cocycle_err,
        m2_cyclic_error=m2_cyc_err,
        m3_cyclic_error=m3_cyc_err,
        m3_norm=m3_norm,
    )


def _make_antisymmetric_cyclic_pairing(
    d: int, m2: NDArray, rng: np.random.Generator
) -> NDArray:
    r"""Generate a nondegenerate antisymmetric pairing cyclic w.r.t. m_2.

    For CY_3: <a,b> = -<b,a>.

    The cyclic condition with antisymmetric pairing:
        <m_2(a,b), c> = -<a, m_2(c,b)>    (CY_3 sign)

    Actually, for CY_d the cyclic invariance is:
        <m_2(a,b), c> = (-1)^{d|a|} <a, m_2(b,c)>

    For d=3 and |a|=0: (-1)^0 = 1, so same as symmetric case.
    The antisymmetry is in the pairing itself, not the cyclic relation.

    Parameters
    ----------
    d : int
        Dimension (must be even).
    m2 : ndarray of shape (d, d, d)
        Associative product.
    rng : np.random.Generator
        Random number generator.

    Returns
    -------
    eta : ndarray of shape (d, d)
        Nondegenerate antisymmetric cyclic pairing.
    """
    # Number of unknowns: d*(d-1)/2 (antisymmetric matrix, upper triangle)
    n_unk = d * (d - 1) // 2

    def asym_idx(i: int, j: int) -> int:
        """Map (i,j) with i < j to index."""
        return i * d - i * (i + 1) // 2 + (j - i - 1)

    # Build constraint matrix for m_2 cyclicity with antisymmetric eta:
    # <m_2(e_i, e_j), e_k> = <e_i, m_2(e_j, e_k)>
    # sum_p m2[i,j,p] * eta[p,k] = sum_p eta[i,p] * m2[j,k,p]
    # where eta[p,k] = -eta[k,p] for p > k, etc.
    constraints = []
    for i in range(d):
        for j in range(d):
            for k in range(d):
                row = np.zeros(n_unk)
                for p in range(d):
                    # eta[p,k] contribution from term 1
                    if p < k:
                        row[asym_idx(p, k)] += m2[i, j, p]
                    elif p > k:
                        row[asym_idx(k, p)] -= m2[i, j, p]
                    # else p == k: eta[p,p] = 0

                    # -eta[i,p] contribution from term 2
                    if i < p:
                        row[asym_idx(i, p)] -= m2[j, k, p]
                    elif i > p:
                        row[asym_idx(p, i)] += m2[j, k, p]
                    # else i == p: eta[i,i] = 0
                constraints.append(row)

    A = np.array(constraints)
    U, S, Vt = np.linalg.svd(A, full_matrices=True)
    tol = 1e-8 * max(S[0] if len(S) > 0 else 1.0, 1.0)
    n_sing = len(S)
    kernel_indices = list(range(n_sing, Vt.shape[0]))
    kernel_indices.extend(i for i in range(n_sing) if S[i] < tol)
    kernel_indices = sorted(set(kernel_indices))

    if len(kernel_indices) == 0:
        # Fallback: standard symplectic form
        eta = np.zeros((d, d))
        for i in range(d // 2):
            eta[2 * i, 2 * i + 1] = 1.0
            eta[2 * i + 1, 2 * i] = -1.0
        return eta

    kernel_basis = Vt[kernel_indices]

    for _attempt in range(100):
        coeffs = rng.standard_normal(len(kernel_indices))
        eta_flat = coeffs @ kernel_basis
        eta = np.zeros((d, d))
        for i in range(d):
            for j in range(i + 1, d):
                idx = asym_idx(i, j)
                eta[i, j] = eta_flat[idx]
                eta[j, i] = -eta_flat[idx]

        # Check nondegeneracy via Pfaffian (det of antisymmetric = Pf^2)
        if abs(np.linalg.det(eta)) > 1e-6:
            return eta

    # Fallback
    eta = np.zeros((d, d))
    for i in range(d // 2):
        eta[2 * i, 2 * i + 1] = 1.0
        eta[2 * i + 1, 2 * i] = -1.0
    return eta


def _random_cocycle_cyclic_m3(
    m2: NDArray, eta: NDArray, rng: np.random.Generator,
    scale: float = 1.0, antisymmetric: bool = False
) -> NDArray:
    r"""Generate m_3 satisfying both cocycle and cyclic constraints jointly.

    For CY_3 with antisymmetric pairing, the cyclic constraint is:
        <m_3(a,b,c), d> - <m_3(b,c,d), a> + <m_3(c,d,a), b> - <m_3(d,a,b), c> = 0

    (Signs alternate due to antisymmetry of the pairing.)

    For the ungraded case with antisymmetric eta, the cyclic constraint
    remains the same 4-fold sum = 0 as before (the signs from the pairing
    antisymmetry and the cyclic rotation cancel).
    """
    d = m2.shape[0]
    m3_raw = rng.standard_normal((d, d, d, d)) * scale
    return _joint_project_cocycle_cyclic(m2, eta, m3_raw, rng)


def _verify_m3_cyclic_antisym(m3: NDArray, eta: NDArray, tol: float = 1e-8) -> float:
    r"""Verify m_3 cyclic invariance with antisymmetric pairing.

    Same formula as symmetric case (the pairing antisymmetry is already
    encoded in eta).
    """
    return _verify_m3_cyclic(m3, eta, tol)


# =========================================================================
#  6.  Full CY_3 experiment
# =========================================================================

def run_cy3_experiment(
    n_trials: int = 50,
    dimensions: Tuple[int, ...] = (4,),
    cc_degree: int = 4,
    m3_scale: float = 1.0,
    nontrivial_threshold: float = 1e-8,
    vanishing_tolerance: float = 1e-7,
    seed: int = 137,
    verbose: bool = False,
) -> ExperimentResult:
    r"""Run the CY_3-specific falsification search.

    Parameters are the same as run_experiment, but uses CY_3 algebras
    with antisymmetric pairing.
    """
    rng = np.random.default_rng(seed)
    trials = []
    dim_counts: Dict[int, int] = {d: 0 for d in dimensions}

    for trial_idx in range(n_trials):
        d = int(rng.choice(dimensions))
        dim_counts[d] = dim_counts.get(d, 0) + 1

        alg = generate_random_cy3_algebra(d, rng, m3_scale=m3_scale)
        comm = compute_commutator_m3_b2(d, cc_degree, alg.m3, alg.eta)
        comm_norm = float(np.max(np.abs(comm)))

        is_nontrivial = alg.m3_norm > nontrivial_threshold
        comm_vanishes = bool(np.isfinite(comm_norm) and comm_norm < vanishing_tolerance)

        result = TrialResult(
            trial_idx=trial_idx,
            d=d,
            m3_norm=alg.m3_norm,
            commutator_norm=comm_norm,
            assoc_error=alg.assoc_error,
            cocycle_error=alg.cocycle_error,
            m2_cyclic_error=alg.m2_cyclic_error,
            m3_cyclic_error=alg.m3_cyclic_error,
            is_nontrivial=is_nontrivial,
            commutator_vanishes=comm_vanishes,
        )
        trials.append(result)

        if verbose and (trial_idx + 1) % 50 == 0:
            n_nt = sum(1 for t in trials if t.is_nontrivial)
            n_van = sum(1 for t in trials if t.is_nontrivial and t.commutator_vanishes)
            print(f"CY3 trial {trial_idx + 1}/{n_trials}: {n_nt} nontrivial, {n_van} vanishing")

    nontrivial_trials = [t for t in trials if t.is_nontrivial]
    n_nontrivial = len(nontrivial_trials)
    n_vanishing = sum(1 for t in nontrivial_trials if t.commutator_vanishes)
    n_nonvanishing = n_nontrivial - n_vanishing

    comm_norms = [t.commutator_norm for t in nontrivial_trials if not np.isnan(t.commutator_norm)]
    max_comm = max(comm_norms) if comm_norms else 0.0
    mean_comm = float(np.mean(comm_norms)) if comm_norms else 0.0

    max_assoc = max((t.assoc_error for t in trials), default=0.0)
    max_cocycle = max((t.cocycle_error for t in trials), default=0.0)
    max_m2_cyc = max((t.m2_cyclic_error for t in trials), default=0.0)
    max_m3_cyc = max((t.m3_cyclic_error for t in trials), default=0.0)

    if n_nonvanishing == 0 and n_nontrivial > 0:
        conclusion = (
            f"CY_3 NO CANDIDATE WITNESS FOUND in {n_nontrivial} nontrivial "
            f"random cyclic A_infinity samples. "
            f"Maximum commutator norm: {max_comm:.2e}. "
            f"This finite search does not prove universal vanishing."
        )
    elif n_nonvanishing > 0:
        conclusion = (
            f"CY_3 CANDIDATE WITNESS: raw [m_3, B_term^(2)] != 0 for "
            f"{n_nonvanishing} / {n_nontrivial} nontrivial samples. "
            f"Maximum commutator norm: {max_comm:.2e}. "
            f"This finite search does not prove universal vanishing."
        )
    else:
        conclusion = (
            f"CY_3 NO NONTRIVIAL SAMPLE: no nontrivial m_3 found in {len(trials)} trials. "
            f"This finite search does not prove universal vanishing."
        )

    return ExperimentResult(
        n_trials=len(trials),
        n_dimensions=dim_counts,
        n_nontrivial=n_nontrivial,
        n_vanishing=n_vanishing,
        n_nonvanishing=n_nonvanishing,
        max_commutator_norm=max_comm,
        mean_commutator_norm=mean_comm,
        max_assoc_error=max_assoc,
        max_cocycle_error=max_cocycle,
        max_m2_cyclic_error=max_m2_cyc,
        max_m3_cyclic_error=max_m3_cyc,
        trials=trials,
        conclusion=conclusion,
    )


# =========================================================================
#  7.  Diagnostic: dimension-by-dimension breakdown
# =========================================================================

def run_dimension_sweep(
    dimensions: Tuple[int, ...] = (3, 4, 5, 6),
    trials_per_dim: int = 50,
    cc_degree: int = 4,
    seed: int = 271,
) -> Dict[int, Dict[str, Any]]:
    r"""Run the experiment separately for each dimension.

    Returns a dict mapping d -> {n_nontrivial, n_vanishing, max_comm, ...}.
    """
    results = {}
    for d in dimensions:
        exp = run_experiment(
            n_trials=trials_per_dim,
            dimensions=(d,),
            cc_degree=cc_degree,
            seed=seed + d,
        )
        results[d] = {
            "n_trials": exp.n_trials,
            "n_nontrivial": exp.n_nontrivial,
            "n_vanishing": exp.n_vanishing,
            "n_nonvanishing": exp.n_nonvanishing,
            "max_commutator_norm": exp.max_commutator_norm,
            "mean_commutator_norm": exp.mean_commutator_norm,
            "max_assoc_error": exp.max_assoc_error,
            "max_cocycle_error": exp.max_cocycle_error,
            "conclusion": exp.conclusion,
        }
    return results
