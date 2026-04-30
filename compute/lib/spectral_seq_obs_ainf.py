r"""Combinatorics for the m_k--B^{(2)} obstruction.

The earlier version of this module stated a universal spectral-sequence
exactness theorem for the termwise pair-contraction operator.  That theorem
is false.  The repaired theorem separates three carriers:

  (1) B^{(2)}_term, a termwise bar operator with strict nonzero witnesses;
  (2) B^{(2)}_TCFT, Costello's corrected operator satisfying the total
      TCFT boundary identity with b = sum_k b_k;
  (3) the derived E_1-Hochschild obstruction class, which vanishes only
      under an explicit HH^{-2} filtration hypothesis.

This module still enumerates adjacent and non-adjacent configurations and
records the old filtration-page heuristic.  Those integers are diagnostic
data.  They do not prove that B^{(2)}_term is exact, zero in the abutment,
or sufficient for a framing theorem.

The strict witness used by the standalone is the cyclic CY_3 model with
m_3(a,a,a)=alpha b, |a|=1, |b|=2, and terminal-slot pair contractions:

    [m_3,B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0.

Consequently, any result returned by this module with a name containing
"exact", "vanishes", or "sufficient" is a legacy compatibility field unless
it is explicitly tied to the corrected TCFT operator or to the HH^{-2}
filtration theorem.

CONVENTIONS
===========
  - Cohomological grading: |d| = +1
  - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1 (AP45)
  - CY dimension d=3: Serre functor S = [3]
  - AP-CY2: CY trace is HC^-_3(C), NOT just HH_3 -> k
  - AP113: kappa always subscripted (kappa_ch, kappa_cat, etc.)
  - AP-CY6: results are for the PROGRAMME (d=3 conditional)

REFERENCES
==========
  Stasheff, TAMS 108 (1963): homotopy associativity, A_inf
  Keller (2006): A-infinity transfer theorem
  Costello (2005): TCFTs and CY categories
  Kontsevich-Soibelman (2009): Notes on A-infinity algebras
  Vol III: cy_to_chiral.tex, Prop ref:prop:cyclic-ainf-framing-compat
  Vol III: en_factorization.tex, Prop ref:prop:virasoro-d4
  Vol III: a_infinity_bar_w1inf.py (A_inf bar complex of W_{1+inf})
  Vol III: hopf_fibration_s3_framing.py (Hopf decomposition)
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

F = Fraction


# =========================================================================
# 0. FILTRATION DATA FOR THE BAR SPECTRAL SEQUENCE
# =========================================================================

@dataclass(frozen=True)
class ArityFiltration:
    r"""The arity filtration on the bar complex B^{ord}(A).

    F_p B = {elements with <= p tensor factors}.

    The bar differential d = m_1 + m_2 + ... respects this filtration:
      m_k: F_p -> F_{p-k+1}  (consumes k factors, produces 1)

    The associated spectral sequence has d_r from m_{r+1}:
      d_r: E_r^{p,q} -> E_r^{p-r, q+r-1}

    The B^{(2)} operator (S^2-framing map) has:
      B^{(2)}: F_p -> F_{p-1}  (contracts 2 factors to a scalar, net -1)

    Attributes:
        p: arity (number of tensor factors)
        q: internal degree (cohomological degree after desuspension)
    """
    p: int  # arity
    q: int  # internal degree

    @property
    def total_degree(self) -> int:
        """Total degree p + q in the spectral sequence."""
        return self.p + self.q


def mk_filtration_shift(k: int) -> int:
    r"""Filtration shift of m_k on the arity filtration.

    m_k: A^{\otimes k} -> A maps k factors to 1 factor.
    On the bar complex, it replaces k consecutive factors by 1 output.
    Net arity change: -(k-1).

    In the spectral sequence: m_k contributes to d_{k-1}.
    """
    return -(k - 1)


def b2_filtration_shift() -> int:
    r"""Filtration shift of B^{(2)} on the arity filtration.

    B^{(2)} contracts a pair of factors using the CY pairing:
      B^{(2)}(a_0, ..., a_n) = sum_{i<j} <a_i, a_j>_2 * (remaining)

    Each contraction removes 2 factors and produces the scalar pairing,
    reducing arity by 1 (2 factors removed, replaced by nothing, but the
    remaining factors form a bar element of arity n-2+0 = n-2... no:
    the scalar multiplies the remaining n-2 factors, giving arity n-2).

    Wait: B^{(2)}: CC_n -> CC_{n-1} as stated in the manuscript.
    This means it lowers degree on the cyclic bar complex by 1.
    In arity terms: contracting 2 factors and the cyclic rotation gives
    net arity n-1.

    Filtration shift: -1.
    """
    return -1


# =========================================================================
# 1. COMMUTATOR TERM CLASSIFICATION
# =========================================================================

@dataclass(frozen=True)
class CommutatorTerm:
    r"""A single term in the commutator [m_k, B^{(2)}].

    Attributes:
        mk_positions: tuple of positions where m_k acts (consecutive)
        b2_positions: tuple of 2 positions where B^{(2)} contracts
        is_adjacent: whether both B^{(2)} positions are inside or
                     both outside the m_k block
        order: "mk_first" or "b2_first" (which operation acts first)
        sign: Koszul sign of this term
        input_arity: arity of the input bar element
    """
    mk_positions: Tuple[int, ...]
    b2_positions: Tuple[int, int]
    is_adjacent: bool
    order: str  # "mk_first" or "b2_first"
    sign: int
    input_arity: int

    @property
    def mk_block_start(self) -> int:
        return min(self.mk_positions)

    @property
    def mk_block_end(self) -> int:
        return max(self.mk_positions)

    @property
    def output_arity(self) -> int:
        """Output arity after both operations."""
        k = len(self.mk_positions)
        # m_k lowers by k-1, B^{(2)} lowers by 1 (on cyclic bar)
        # Total: input_arity - k + 1 - 1 = input_arity - k
        # But this depends on whether the pairing absorbs factors.
        # B^{(2)} removes 2 factors via pairing -> arity drops by 2
        # m_k removes k factors, produces 1 -> arity drops by k-1
        # BUT: if one paired factor is inside the m_k block, the
        # count is different.
        if self.is_adjacent:
            # Both inside: m_k acts on a block that includes the
            # paired factors. Net: arity - (k-1) - 2 + correction
            # Both outside: m_k acts on its block, B^{(2)} contracts
            # two outside factors. Net: arity - (k-1) - 2
            return self.input_arity - (k - 1) - 2
        else:
            # Non-adjacent: one factor from m_k block, one from outside.
            # The pairing removes both, but one was an m_k input.
            # m_k now acts on k-1 inputs (one was consumed by pairing)
            # plus the scalar from the pairing.
            # Net: arity - 2 (from pairing) - (k-2) (from reduced m_k)
            # = arity - k
            return self.input_arity - len(self.mk_positions)

    @property
    def filtration_shift(self) -> int:
        """Net filtration shift from input arity."""
        return self.output_arity - self.input_arity

    def classify_spectral_page(self) -> str:
        """Which spectral sequence page this term belongs to.

        Adjacent terms: filtration shift = -(k-1) - 2 = -(k+1).
        These are at the d_{k+1} level of the arity spectral sequence.
        But they cancel by cyclic invariance (chain-level identity).

        Non-adjacent terms: the pairing "reaches across" the m_k
        boundary.  In the refined bigrading, this is a mixing operation
        that belongs to the d_{k-1} level.

        The key insight: the non-adjacent terms involve the Stasheff
        identity at arity k+1, which is the defining relation of the
        bar differential.  They are therefore in im(d_{k-1}).
        """
        k = len(self.mk_positions)
        if self.is_adjacent:
            return f"chain-level (cyclic invariance)"
        else:
            return f"d_{k-1} (Stasheff identity at arity {k+1})"


def enumerate_commutator_terms(
    n: int, k: int
) -> List[CommutatorTerm]:
    r"""Enumerate all terms in [m_k, B^{(2)}] on CC_n.

    The commutator [m_k, B^{(2)}] = m_k circ B^{(2)} - B^{(2)} circ m_k
    acts on a cyclic bar element [a_0 | a_1 | ... | a_n].

    Parameters:
        n: arity of the input (number of factors)
        k: arity of the m_k operation

    Returns:
        list of CommutatorTerm instances
    """
    if n < k or n < 2:
        return []

    terms = []

    # m_k acts on positions [start, start+1, ..., start+k-1]
    for start in range(n - k + 1):
        mk_pos = tuple(range(start, start + k))

        # B^{(2)} contracts positions (i, j) with i < j
        for i in range(n):
            for j in range(i + 1, n):
                # Classify adjacency
                inside_i = (start <= i < start + k)
                inside_j = (start <= j < start + k)

                if inside_i and inside_j:
                    is_adj = True  # both inside
                elif (not inside_i) and (not inside_j):
                    is_adj = True  # both outside
                else:
                    is_adj = False  # one inside, one outside

                # Sign from Koszul convention (simplified for degree-0 gens)
                sign = (-1) ** (start + i + j)

                # m_k first, then B^{(2)}
                terms.append(CommutatorTerm(
                    mk_positions=mk_pos,
                    b2_positions=(i, j),
                    is_adjacent=is_adj,
                    order="mk_first",
                    sign=sign,
                    input_arity=n,
                ))

                # B^{(2)} first, then m_k
                terms.append(CommutatorTerm(
                    mk_positions=mk_pos,
                    b2_positions=(i, j),
                    is_adjacent=is_adj,
                    order="b2_first",
                    sign=-sign,  # commutator sign
                    input_arity=n,
                ))

    return terms


# =========================================================================
# 2. FILTRATION DEGREE COMPUTATION
# =========================================================================

@dataclass
class FiltrationAnalysis:
    r"""Analysis of filtration degrees in [m_k, B^{(2)}].

    For an input bar element of arity n, the commutator [m_k, B^{(2)}]
    produces terms at various filtration degrees.  The key finding:

    ADJACENT terms:
      - Filtration shift: -(k-1) from m_k, -2 from B^{(2)} = -(k+1)
      - But B^{(2)} contracts 2 of the n factors to scalar; m_k acts
        on k of the remaining n-2 factors (if both outside) or k factors
        including the contracted ones (if both inside).
      - Net output arity: n - (k-1) - 2 = n - k - 1.
      - Filtration shift: -(k+1).

    NON-ADJACENT terms:
      - One factor a_i is inside the m_k block, one a_j is outside.
      - The pairing <a_i, a_j>_2 converts two factors to a scalar.
      - m_k now acts on k-1 genuine factors + 1 scalar insertion.
      - For unital A_inf algebras: m_k(..., 1, ...) may be nonzero
        (only m_2(1, a) = a is guaranteed).
      - Net output arity: n - k (same as adjacent for k=3: n - 4,
        which is n - (k+1) = n - 4 for k=3, matching).
      - Actually: for the commutator [m_k, B^{(2)}], the B^{(2)} circ m_k
        term has output arity n - (k-1) - 2 = n - k - 1 (B^{(2)} contracts
        2 factors from the n-(k-1) remaining).
        The m_k circ B^{(2)} term has output arity n - 2 - (k'-1) where
        k' depends on how many m_k-inputs survive the pairing.
      - The MISMATCH in arity grading between the two commutator terms
        is the signal that non-adjacent terms are at a different page.

    RESOLUTION:
      The correct analysis uses the bar BICOMPLEX structure.  The bar
      complex has the binary differential d_1 = m_2 and higher corrections
      d_r = m_{r+1}.  The B^{(2)} operator interacts with each d_r
      differently.  The [m_k, B^{(2)}] commutator decomposes as:

      [m_k, B^{(2)}] = [m_k, B^{(2)}]_adj + [m_k, B^{(2)}]_non-adj

      where:
        [m_k, B^{(2)}]_adj is in ker(d_1) / im(d_1) by cyclic invariance
            => it defines a class on E_1 that vanishes (cyclic invariance
            is a d_1-cocycle condition AND the class is zero).
        [m_k, B^{(2)}]_non-adj is in im(d_{k-1})
            => it is exact at E_{k-1} and zero in the abutment.

    Attributes:
        n: input arity
        k: m_k arity
        num_adjacent: count of adjacent terms
        num_nonadjacent: count of non-adjacent terms
        adjacent_filtration: filtration shift of adjacent terms
        nonadjacent_spectral_page: page where non-adj terms become exact
    """
    n: int
    k: int
    num_adjacent: int
    num_nonadjacent: int
    adjacent_filtration: int
    nonadjacent_spectral_page: int

    @property
    def nonadjacent_exact(self) -> bool:
        """Whether termwise non-adjacent terms are proved exact here."""
        return self.num_nonadjacent == 0

    @property
    def total_terms(self) -> int:
        return self.num_adjacent + self.num_nonadjacent

    @property
    def adjacent_cancel_by_cyclic(self) -> bool:
        """Adjacent terms cancel by cyclic invariance (always True)."""
        return True

    @property
    def commutator_vanishes_in_abutment(self) -> bool:
        """Whether this helper proves the termwise commutator vanishes."""
        return self.adjacent_cancel_by_cyclic and self.nonadjacent_exact


def compute_filtration_analysis(n: int, k: int) -> FiltrationAnalysis:
    r"""Compute the filtration analysis for [m_k, B^{(2)}] on CC_n.

    Parameters:
        n: arity of input bar element (must be >= k and >= 2)
        k: arity of m_k operation (must be >= 2)

    Returns:
        FiltrationAnalysis with term counts and filtration data.
    """
    if n < k or n < 2 or k < 2:
        return FiltrationAnalysis(
            n=n, k=k,
            num_adjacent=0, num_nonadjacent=0,
            adjacent_filtration=0,
            nonadjacent_spectral_page=0,
        )

    # Count adjacent vs non-adjacent terms
    num_adj = 0
    num_nonadj = 0

    for start in range(n - k + 1):
        for i in range(n):
            for j in range(i + 1, n):
                inside_i = (start <= i < start + k)
                inside_j = (start <= j < start + k)

                if (inside_i and inside_j) or (not inside_i and not inside_j):
                    num_adj += 2  # mk_first and b2_first
                else:
                    num_nonadj += 2

    # Filtration data
    adjacent_filt = -(k + 1)  # net shift from m_k and B^{(2)}
    nonadj_page = k - 1       # legacy diagnostic page

    return FiltrationAnalysis(
        n=n, k=k,
        num_adjacent=num_adj,
        num_nonadjacent=num_nonadj,
        adjacent_filtration=adjacent_filt,
        nonadjacent_spectral_page=nonadj_page,
    )


# =========================================================================
# 3. LOCAL P^2 EXPLICIT COMPUTATION
# =========================================================================

@dataclass(frozen=True)
class LocalP2Generator:
    r"""A generator of the Ext algebra of local P^2.

    local P^2 = Tot(O(-3) -> P^2) has 3 exceptional objects E_0, E_1, E_2
    from the McKay quiver of Z_3.

    Generators:
      e_a in Ext^0(E_a, E_a): identity endomorphisms (a = 0,1,2)
      x_{ab} in Ext^1(E_a, E_b): arrows (a != b, 6 generators)
      y_{ab} in Ext^2(E_a, E_b): dual arrows (a != b, 6 generators)
      f_a in Ext^3(E_a, E_a): Serre dual of identity (a = 0,1,2)

    Total: 3 + 6 + 6 + 3 = 18 generators.
    (The actual quiver has 24 generators with multiplicity; we use the
    minimal generating set for the spectral sequence analysis.)

    Attributes:
        name: string identifier
        source: source vertex (0, 1, or 2)
        target: target vertex (0, 1, or 2)
        ext_degree: Ext degree (0, 1, 2, or 3)
    """
    name: str
    source: int
    target: int
    ext_degree: int


def local_p2_generators() -> List[LocalP2Generator]:
    """Generate the minimal Ext algebra generators for local P^2."""
    gens = []

    # Ext^0: identity endomorphisms
    for a in range(3):
        gens.append(LocalP2Generator(f"e_{a}", a, a, 0))

    # Ext^1: arrows around the McKay quiver
    for a in range(3):
        for b in range(3):
            if a != b:
                gens.append(LocalP2Generator(f"x_{a}{b}", a, b, 1))

    # Ext^2: dual arrows (Serre dual to Ext^1)
    for a in range(3):
        for b in range(3):
            if a != b:
                gens.append(LocalP2Generator(f"y_{a}{b}", a, b, 2))

    # Ext^3: Serre dual of identity
    for a in range(3):
        gens.append(LocalP2Generator(f"f_{a}", a, a, 3))

    return gens


def local_p2_cy_pairing(
    g1: LocalP2Generator, g2: LocalP2Generator
) -> Fraction:
    r"""CY_3 pairing <g1, g2>_2 for local P^2.

    The CY_3 pairing <-,->: Ext^p(E_a,E_b) x Ext^{3-p}(E_b,E_a) -> k
    pairs Ext^p with Ext^{3-p} (Serre duality at d=3).

    The degree-2 component <-,->_2 pairs:
      Ext^1(E_a, E_b) x Ext^2(E_b, E_a) -> k

    Convention: <x_{ab}, y_{ba}>_2 = 1 if they are dual.
    """
    # Check composability: g1: E_a -> E_b, g2: E_b -> E_a
    if g1.target != g2.source or g2.target != g1.source:
        return F(0)

    # Check degree: must pair Ext^1 with Ext^2 (for degree-2 component)
    if not ((g1.ext_degree == 1 and g2.ext_degree == 2) or
            (g1.ext_degree == 2 and g2.ext_degree == 1)):
        return F(0)

    # Pairing: <x_{ab}, y_{ba}>_2 = 1 (normalized)
    return F(1)


def local_p2_m3(
    g1: LocalP2Generator, g2: LocalP2Generator, g3: LocalP2Generator
) -> Optional[Tuple[LocalP2Generator, Fraction]]:
    r"""Compute m_3(g1, g2, g3) for local P^2.

    The only nonzero m_3 is on composable triples of Ext^1 generators:
      m_3(x_{01}, x_{12}, x_{20}) = e_0  (and cyclic permutations)

    This comes from the Ginzburg potential W = x_{01} x_{12} x_{20}
    (the cubic superpotential of the McKay quiver).

    Returns None if m_3 = 0, or (output_gen, coefficient) if nonzero.
    """
    # Check all three are Ext^1
    if not all(g.ext_degree == 1 for g in [g1, g2, g3]):
        return None

    # Check composability: g1: a->b, g2: b->c, g3: c->a
    if g1.target != g2.source or g2.target != g3.source or g3.target != g1.source:
        return None

    # m_3(x_{ab}, x_{bc}, x_{ca}) = e_a
    a = g1.source
    return (LocalP2Generator(f"e_{a}", a, a, 0), F(1))


def local_p2_nonadjacent_analysis() -> Dict[str, Any]:
    r"""Compute [m_3, B^{(2)}] non-adjacent terms for local P^2.

    For each composable triple (g1, g2, g3) with m_3 != 0, and each
    generator g4 outside the block, compute the non-adjacent terms
    where B^{(2)} pairs one of (g1, g2, g3) with g4.

    This finite enumeration is retained as diagnostic data.  It does not
    prove that all termwise non-adjacent contributions are d_1-exact.

    Returns:
        dict with counts, examples, and verification status.
    """
    gens = local_p2_generators()
    ext1_gens = [g for g in gens if g.ext_degree == 1]

    # Find composable triples with nonzero m_3
    nonzero_triples = []
    for g1 in ext1_gens:
        for g2 in ext1_gens:
            if g1.target != g2.source:
                continue
            for g3 in ext1_gens:
                if g2.target != g3.source or g3.target != g1.source:
                    continue
                m3_result = local_p2_m3(g1, g2, g3)
                if m3_result is not None:
                    nonzero_triples.append((g1, g2, g3, m3_result))

    # For each nonzero triple, enumerate non-adjacent pairings
    nonadj_terms = []
    nonadj_exact_count = 0
    nonadj_total = 0

    for g1, g2, g3, (m3_out, m3_coeff) in nonzero_triples:
        block = [g1, g2, g3]

        for g4 in gens:
            # Skip if g4 is in the block
            if g4 in block:
                continue

            # Check each non-adjacent pairing: g_i (inside) with g4 (outside)
            for idx, g_inside in enumerate(block):
                pairing = local_p2_cy_pairing(g_inside, g4)
                if pairing == F(0):
                    continue

                nonadj_total += 1

                # Term 1: B^{(2)} circ m_3
                # m_3(g1, g2, g3) = m3_out, then <m3_out, g4>_2
                pairing_with_output = local_p2_cy_pairing(m3_out, g4)

                # Term 2: m_3 circ B^{(2)}
                # Replace g_inside by scalar <g_inside, g4>_2 in the m_3 input
                # m_3(..., <g_inside, g4>_2, ...) = <g_inside, g4>_2 * m_3(...)
                # The old oracle marked this exact by a Stasheff heuristic.
                # The strict m3-B2 witness shows that this is not a theorem
                # for the termwise operator without a correction homotopy.
                is_exact = False

                nonadj_terms.append({
                    "triple": (g1.name, g2.name, g3.name),
                    "outside": g4.name,
                    "inside_idx": idx,
                    "inside_gen": g_inside.name,
                    "pairing": pairing,
                    "pairing_with_output": pairing_with_output,
                    "is_d1_exact": is_exact,
                })

    return {
        "num_nonzero_triples": len(nonzero_triples),
        "num_nonadj_nonzero_pairings": nonadj_total,
        "num_nonadj_exact": nonadj_exact_count,
        "all_nonadj_exact": nonadj_exact_count == nonadj_total,
        "spectral_page_of_exactness": None,
        "mechanism": (
            "finite term enumeration only; termwise exactness requires a "
            "TCFT correction homotopy or the HH^{-2} obstruction theorem"
        ),
        "terms": nonadj_terms,
    }


# =========================================================================
# 4. SPECTRAL SEQUENCE COMPARISON WITH PROP:VIRASORO-D4
# =========================================================================

@dataclass
class SpectralPageComparison:
    r"""Comparison of non-adjacent [m_k, B^{(2)}] with the d_r differentials.

    The d_r differential on the E_{r-1} page of the bar spectral sequence
    comes from m_{r+1}.  The non-adjacent terms of [m_k, B^{(2)}] are
    related to d_{k-1} (they are killed on the E_{k-1} page).

    For each shadow class, the relevant spectral page differs:

    Class G (m_k = 0 for k >= 3):
      [m_k, B^{(2)}] = 0 chain-level.  No spectral sequence needed.

    Class L (d_r = 0 for r >= 2 on E_1, by cofreeness):
      [m_3, B^{(2)}]_non-adj is in im(d_2).  d_2 = 0 on E_1 for class L
      by cofreeness, so the terms are automatically zero on E_1.

    Class C (charge conservation blocks non-adjacent pairings):
      B^{(2)} pairs Ext^p with Ext^{3-p}.  The charge grading is
      additive: charge(g1) + charge(g2) must be zero for nonzero pairing.
      For betagamma: charge(beta) = +1, charge(gamma) = -1.  A non-adj
      pairing requires one beta inside and one gamma outside (or vice
      versa), but this CHANGES the charge of the m_k block by +/- 1.
      The Stasheff identity at the new charge is trivially zero.

    Class M (non-adj terms are genuine d_2 corrections):
      [m_3, B^{(2)}]_non-adj is in im(d_2).  On the E_1 page, d_2 may
      be nonzero.  On the E_2 page (after d_2-cohomology), these terms
      are killed.  Since the abutment is computed from the E_2 page
      (and beyond), the terms are zero in H^*(B(A), d).

    Attributes:
        shadow_class: G, L, C, or M
        mk_arity: k
        nonadj_page: spectral page where non-adj terms become exact
        mechanism: description of the cancellation mechanism
    """
    shadow_class: str
    mk_arity: int
    nonadj_page: int
    mechanism: str

    @property
    def vanishes_in_abutment(self) -> bool:
        """Whether this class proves termwise abutment vanishing."""
        return self.shadow_class in ("G", "C")

    @property
    def chain_level_vanishing(self) -> bool:
        """Whether vanishing holds at the chain level (stronger)."""
        return self.shadow_class in ("G",)  # Only class G has chain-level

    @property
    def sufficient_for_obs_ainf(self) -> bool:
        """Whether the termwise analysis suffices for a framing theorem."""
        return self.vanishes_in_abutment


def spectral_comparison_by_class(k: int = 3) -> Dict[str, SpectralPageComparison]:
    r"""Compare non-adjacent term behaviour across shadow classes.

    Parameters:
        k: arity of m_k (default 3, the first non-trivial case)

    Returns:
        dict mapping shadow class to SpectralPageComparison.
    """
    return {
        "G": SpectralPageComparison(
            shadow_class="G",
            mk_arity=k,
            nonadj_page=0,  # m_k = 0, no terms to begin with
            mechanism="m_k = 0 chain-level (formal algebra)",
        ),
        "L": SpectralPageComparison(
            shadow_class="L",
            mk_arity=k,
            nonadj_page=1,  # legacy diagnostic page
            mechanism=(
                f"legacy d_{k-1} diagnostic page; termwise exactness "
                f"requires a correction homotopy or a separate HH theorem"
            ),
        ),
        "C": SpectralPageComparison(
            shadow_class="C",
            mk_arity=k,
            nonadj_page=1,  # charge conservation blocks the pairing
            mechanism=(
                "charge conservation: B^{(2)} pairing changes charge of "
                "m_k-block by +/- 1, Stasheff identity at wrong charge = 0"
            ),
        ),
        "M": SpectralPageComparison(
            shadow_class="M",
            mk_arity=k,
            nonadj_page=k - 1,  # legacy diagnostic page
            mechanism=(
                f"legacy d_{k-1} diagnostic page from arity {k+1}; "
                f"the strict witness blocks universal termwise exactness"
            ),
        ),
    }


# =========================================================================
# 5. THE STASHEFF IDENTITY MECHANISM (DETAILED)
# =========================================================================

def stasheff_identity_at_arity(n: int) -> Dict[str, Any]:
    r"""The Stasheff (A_inf) identity at arity n.

    The A_inf relation at arity n is:

        sum_{i+j=n+1} sum_{r=1}^{n-j+1}
            (-1)^{eps} m_i(a_1, ..., a_{r-1}, m_j(a_r,...,a_{r+j-1}),
                        a_{r+j}, ..., a_n) = 0

    This identity has:
      - Terms with (i,j) = (n, 1): m_n(... m_1 ...) (m_1 insertion)
      - Terms with (i,j) = (1, n): m_1(m_n(...)) (m_1 of m_n)
      - Mixed terms: m_i(... m_j ...) for 2 <= j <= n-1

    For the non-adjacent [m_k, B^{(2)}] analysis at arity k+1:

    The relevant Stasheff identity at n = k+1 relates:
      m_k(a_1,..., m_2(a_i, a_{k+1}), ..., a_k) +  (i inside, k+1 outside)
      m_2(m_k(a_1,...,a_k), a_{k+1}) +               (m_k first, then m_2)
      ... other terms ...  = 0

    When we apply the CY pairing <a_i, a_{k+1}>_2, this identity becomes
    exactly the cancellation between the two non-adjacent commutator terms.

    Parameters:
        n: arity (number of inputs)

    Returns:
        dict describing the identity and its terms.
    """
    terms = []
    for j in range(1, n + 1):
        i = n + 1 - j
        for r in range(1, n - j + 2):
            terms.append({
                "outer_arity": i,
                "inner_arity": j,
                "insertion_pos": r,
            })

    # Count terms by (i, j) pair
    ij_counts = defaultdict(int)
    for t in terms:
        ij_counts[(t["outer_arity"], t["inner_arity"])] += 1

    return {
        "arity": n,
        "total_terms": len(terms),
        "ij_distribution": dict(ij_counts),
        "terms": terms,
        "relevance_to_nonadj": (
            f"At arity {n}, the (m_{n-1}, m_2) terms relate "
            f"m_{n-1}(... m_2(a_i, a_n) ...) to m_2(m_{n-1}(...), a_n). "
            f"Under CY pairing <a_i, a_n>_2, this is the non-adjacent "
            f"commutator [m_{n-1}, B^{{(2)}}]_{{non-adj}}."
        ),
    }


# =========================================================================
# 6. SUFFICIENCY ANALYSIS
# =========================================================================

@dataclass
class SufficiencyAnalysis:
    r"""Analysis of whether a termwise calculation suffices.

    The repaired theorem says the termwise calculation is not sufficient in
    class M.  A framing statement requires either the corrected TCFT
    operator or an explicit HH^{-2} obstruction calculation.

    Attributes:
        chain_level: whether [m_k, B^{(2)}] = 0 at chain level
        cohomological: whether [m_k, B^{(2)}] = 0 in cohomology
        sufficient_for_framing: whether the vanishing suffices
        mechanism: description of the sufficiency argument
    """
    chain_level: bool
    cohomological: bool
    sufficient_for_framing: bool
    mechanism: str

    @property
    def upgrades_prop_status(self) -> bool:
        """Whether this analysis upgrades the proposition status.

        A termwise spectral-page heuristic alone does not upgrade a theorem.
        """
        return self.sufficient_for_framing and self.cohomological


def analyze_sufficiency(shadow_class: str = "M") -> SufficiencyAnalysis:
    r"""Analyze whether this termwise helper proves a framing statement.

    Parameters:
        shadow_class: G, L, C, or M

    Returns:
        SufficiencyAnalysis with the verdict.
    """
    if shadow_class == "G":
        return SufficiencyAnalysis(
            chain_level=True,
            cohomological=True,
            sufficient_for_framing=True,
            mechanism="m_k = 0 for k >= 3 (formal). Chain-level vanishing.",
        )
    elif shadow_class == "L":
        return SufficiencyAnalysis(
            chain_level=False,
            cohomological=False,
            sufficient_for_framing=False,
            mechanism=(
                "The old cofreeness page count is only a diagnostic. "
                "A correction homotopy or HH^{-2} theorem is required."
            ),
        )
    elif shadow_class == "C":
        return SufficiencyAnalysis(
            chain_level=True,  # charge conservation gives chain-level
            cohomological=True,
            sufficient_for_framing=True,
            mechanism=(
                "Charge conservation blocks non-adjacent pairings. "
                "Chain-level vanishing from charge grading."
            ),
        )
    elif shadow_class == "M":
        return SufficiencyAnalysis(
            chain_level=False,
            cohomological=False,
            sufficient_for_framing=False,
            mechanism=(
                "The strict m3-B2 witness has a nonzero termwise "
                "commutator. Use B_TCFT or the HH^{-2} filtration theorem."
            ),
        )
    else:
        raise ValueError(f"Unknown shadow class: {shadow_class}")


# =========================================================================
# 7. MAIN COMPUTATION: FULL ANALYSIS
# =========================================================================

def compute_spectral_seq_obs_ainf(
    n_max: int = 8,
    k_max: int = 5,
) -> Dict[str, Any]:
    r"""Full diagnostic analysis of [m_k, B^{(2)}_term] configurations.

    Computes:
    (1) Filtration analysis for [m_k, B^{(2)}] at various arities
    (2) Term counts (adjacent vs non-adjacent)
    (3) Spectral page of exactness for each shadow class
    (4) Local P^2 explicit verification
    (5) Sufficiency analysis for Obs_Ainf
    (6) Comparison with prop:virasoro-d4

    Parameters:
        n_max: maximum arity to analyze
        k_max: maximum m_k to consider

    Returns:
        dict with all results.
    """
    # (1) Filtration analysis for various (n, k)
    filtration_data = {}
    for k in range(3, min(k_max + 1, n_max + 1)):
        for n in range(k, n_max + 1):
            analysis = compute_filtration_analysis(n, k)
            filtration_data[(n, k)] = {
                "n": n,
                "k": k,
                "num_adjacent": analysis.num_adjacent,
                "num_nonadjacent": analysis.num_nonadjacent,
                "total_terms": analysis.total_terms,
                "nonadj_fraction": (
                    F(analysis.num_nonadjacent, analysis.total_terms)
                    if analysis.total_terms > 0 else F(0)
                ),
                "nonadj_spectral_page": analysis.nonadjacent_spectral_page,
                "vanishes_in_abutment": analysis.commutator_vanishes_in_abutment,
            }

    # (2) Spectral comparison by shadow class
    class_comparison = {}
    for k in range(3, min(k_max + 1, 6)):
        comp = spectral_comparison_by_class(k)
        class_comparison[k] = {
            cls: {
                "nonadj_page": c.nonadj_page,
                "mechanism": c.mechanism,
                "vanishes_in_abutment": c.vanishes_in_abutment,
                "chain_level": c.chain_level_vanishing,
            }
            for cls, c in comp.items()
        }

    # (3) Local P^2 explicit computation
    lp2_analysis = local_p2_nonadjacent_analysis()

    # (4) Sufficiency analysis for each class
    sufficiency = {}
    for cls in ["G", "L", "C", "M"]:
        s = analyze_sufficiency(cls)
        sufficiency[cls] = {
            "chain_level": s.chain_level,
            "cohomological": s.cohomological,
            "sufficient_for_framing": s.sufficient_for_framing,
            "upgrades_prop": s.upgrades_prop_status,
            "mechanism": s.mechanism,
        }

    # (5) Stasheff identity data
    stasheff_data = {}
    for n in range(3, min(k_max + 2, 7)):
        stasheff_data[n] = stasheff_identity_at_arity(n)

    # (6) Summary
    all_vanish = all(
        fd["vanishes_in_abutment"] for fd in filtration_data.values()
    )
    all_classes_ok = all(
        s["sufficient_for_framing"] for s in sufficiency.values()
    )

    return {
        "filtration_data": filtration_data,
        "class_comparison": class_comparison,
        "local_p2": lp2_analysis,
        "sufficiency": sufficiency,
        "stasheff_identities": stasheff_data,
        "main_result": {
            "statement": (
                "The termwise operator B^{(2)}_term has nonzero strict "
                "witnesses. Filtration-page data are diagnostic only. "
                "The corrected TCFT identity and the HH^{-2} obstruction "
                "theorem are separate inputs."
            ),
            "all_filtrations_consistent": all_vanish,
            "all_classes_sufficient": all_classes_ok,
            "upgrades_proposition": False,
            "new_claim_status": "termwise universal exactness rejected",
            "chain_level_open": (
                "Termwise chain-level vanishing is false in class M by "
                "the strict m3-B2 witness."
            ),
        },
    }


# =========================================================================
# 8. VIRASORO d_4 CONNECTION
# =========================================================================

def virasoro_d4_connection() -> Dict[str, Any]:
    r"""Diagnostic relation between page bookkeeping and the d_4 differential.

    The d_4 differential on the E_3 page of the E_3 bar spectral sequence
    (prop:virasoro-d4) comes from m_4.  The non-adjacent terms of
    [m_3, B^{(2)}] are related to d_2.

    The hierarchy:
      d_1 = m_2  (binary bar differential)
      d_2 = m_3  (ternary correction, associator)
      d_3 = m_4  (quartic shadow, Delta = 40/27 at c=1)
      d_4 = m_5  (quintic shadow)

    The old diagnostic places non-adjacent [m_k, B^{(2)}_term] terms at the
    same arity shift as d_{k-1}.  That page bookkeeping is not a proof that
    the termwise operator is killed there.

    Comparison with prop:virasoro-d4:
      The d_4 differential kills Lambda^0 and Lambda^3 (the volume
      class and the scalar class) on the E_3 page, giving E_4 = [0,3,3,0].
      This d_4 comes from S_4 = 10/27 (quartic shadow).

      The corrected TCFT or HH^{-2} obstruction theorem must be supplied
      before claiming that the non-adjacent terms do not interfere with a
      later d_4 computation.

    This means:
      (a) The old non-adjacent-exactness argument is not an input to
          prop:virasoro-d4.
      (b) The d_4 coefficient Delta = 40/27 is a separate quartic-shadow
          computation.
      (c) The page hierarchy is bookkeeping for arity shifts until the
          corrected TCFT or HH^{-2} theorem is supplied.

    Returns:
        dict with the connection analysis.
    """
    return {
        "d_r_from_mk": {
            "d_1": "m_2 (binary OPE bracket)",
            "d_2": "m_3 (associator / Massey product)",
            "d_3": "m_4 (quartic shadow, Delta = 8*kappa_ch*S_4)",
            "d_4": "m_5 (quintic shadow, S_5 = -16/9 at c=1)",
        },
        "nonadj_mk_page": {
            "[m_3, B^{(2)}]_non-adj": "legacy d_2 diagnostic page; not a termwise exactness proof",
            "[m_4, B^{(2)}]_non-adj": "legacy d_3 diagnostic page; not a termwise exactness proof",
            "[m_5, B^{(2)}]_non-adj": "legacy d_4 diagnostic page; not a termwise exactness proof",
        },
        "virasoro_d4": {
            "page": "E_3 -> E_4",
            "differential": "d_4: Lambda^3 -> Lambda^0",
            "coefficient": "Delta = 40/(5c+22) = 40/27 at c=1",
            "from_shadow": "S_4 = 10/(c(5c+22)) = 10/27 at c=1",
        },
        "independence": (
            "A later d_4 computation is independent only after the "
            "corrected TCFT identity or the HH^{-2} obstruction theorem "
            "has removed the termwise obstruction."
        ),
        "consistency": (
            "The page hierarchy is useful bookkeeping, not a vanishing "
            "theorem for B^{(2)}_term."
        ),
    }
