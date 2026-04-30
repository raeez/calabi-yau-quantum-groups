r"""Bar-length diagnostics for the failed bidegree proof.

MATHEMATICAL CONTENT:

On the Hochschild chain complex CC_n(A) of a cyclic A_infinity algebra A,
the bar differential b = sum_{k >= 1} b_k and the formal Connes hierarchy
operators B^{(j)} carry bar-length shifts.  The older version of this
module claimed that the mixed-complex identity [b, B^{(j)}] = 0 separates
by bar length and gives per-k vanishing.  That proof is
false.

THE DIAGNOSTIC OBSERVATION:

  b_k has bar-length degree -(k-1):  CC_n -> CC_{n-k+1}
  B^{(j)} has bar-length degree 1-2j: CC_n -> CC_{n+1-2j}

  Therefore [b_k, B^{(j)}] has bar-length degree -(k-1) + (1-2j) = 2-k-2j.

  For fixed j, different values of k produce distinct bar-length shifts.
  This remains a useful diagnostic.  It is not a proof that the termwise
  commutators vanish.  The strict cyclic CY_3 witness in
  spectral_seq_obs_ainf.py gives

      [m_3, B^{(2)}_term][a|a|a|a|b] = 2 alpha [b] != 0.

  Thus the per-k conclusion is rejected.  Costello's theorem gives the
  total corrected TCFT identity for B^{(2)}_TCFT, after the moduli-chain
  correction datum is included; it does not identify the corrected TCFT
  operator with the termwise pair contraction.

THE TWO-STEP PROOF:

  The rejected proof had two steps.  Step 1 used Costello's total TCFT
  identity as if it were an identity for the termwise operator.  Step 2
  projected by bar length as if the corrected TCFT representative had no
  higher correction faces.  The strict witness disproves the conclusion.

RELATION TO THE ADVERSARIAL AUDIT (rem:adversarial-audit-cyclic-ainf):

The audit correctly identified that cyclic invariance of mu_n (a statement
about the pairing of mu_n-output with ONE additional element) does not
directly control "non-adjacent" contractions in [m_k, B^{(2)}].

The resolution is not bidegree separation.  The valid statements are:

  (a) the termwise operator has strict nonzero witnesses;
  (b) the corrected TCFT operator satisfies a total boundary identity;
  (c) the derived obstruction vanishes only under an explicit HH^{-2}
      filtration theorem or an equivalent corrected TCFT comparison.

CONVENTIONS:
  - CC_n has bar length n (n+1 tensor factors: a_0, a_1, ..., a_n).
  - b_k applies mu_k to k consecutive factors: CC_n -> CC_{n-k+1}.
  - B^{(0)} = B (standard Connes operator): CC_n -> CC_{n+1}.
  - B^{(j)} contracts j pairs using CY pairing: CC_n -> CC_{n+1-2j}.
  - For CY_3: j in {0,1,2,3}; B^{(3)} = F (S^3-framing map).

REFERENCES:
  - Costello (2005, 2007): Open TCFT and CY A-infinity algebras.
  - Kontsevich-Soibelman (2009): CY structures and mixed complexes.
  - Loday (1992): Cyclic Homology, Ch. 2 (mixed complexes).
  - Vol III: cy_to_chiral.tex Sec. 8 (Hopf fibration decomposition).
  - Vol III: cyclic_ainf.tex (cyclic A-infinity definitions).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


# =========================================================================
#  0. Bar-length degree computations
# =========================================================================

def bar_length_degree_b_k(k: int) -> int:
    r"""Bar-length degree of the operation b_k on CC_bullet.

    b_k applies mu_k to k consecutive factors in the bar complex:
        b_k: CC_n -> CC_{n - k + 1}

    This replaces k adjacent tensor factors by their mu_k-image (one factor),
    reducing the number of factors by k-1.

    Parameters
    ----------
    k : int
        Arity of the A-infinity operation mu_k (k >= 1).

    Returns
    -------
    int
        Bar-length degree = -(k-1).

    Examples
    --------
    >>> bar_length_degree_b_k(1)  # m_1: internal differential, preserves length
    0
    >>> bar_length_degree_b_k(2)  # m_2: binary product, reduces by 1
    -1
    >>> bar_length_degree_b_k(3)  # m_3: ternary, reduces by 2
    -2
    """
    if k < 1:
        raise ValueError(f"Arity k must be >= 1, got {k}")
    return -(k - 1)


def bar_length_degree_B_j(j: int) -> int:
    r"""Bar-length degree of the Connes hierarchy operator B^{(j)}.

    B^{(j)} is the j-th operator in the Connes hierarchy for a CY_d algebra.
    It acts on CC_n by inserting the identity (gaining +1) and contracting
    j pairs via the CY pairing (each contraction removes 2 factors):
        B^{(j)}: CC_n -> CC_{n + 1 - 2j}

    Parameters
    ----------
    j : int
        Hierarchy index (0 <= j <= d for CY_d).
        j=0: standard Connes B operator.
        j=d: S^d-framing map F.

    Returns
    -------
    int
        Bar-length degree = 1 - 2j.

    Examples
    --------
    >>> bar_length_degree_B_j(0)  # B = Connes operator: CC_n -> CC_{n+1}
    1
    >>> bar_length_degree_B_j(1)  # B^{(1)}: CC_n -> CC_{n-1}
    -1
    >>> bar_length_degree_B_j(2)  # B^{(2)}: CC_n -> CC_{n-3}
    -3
    >>> bar_length_degree_B_j(3)  # F = S^3-framing: CC_n -> CC_{n-5}
    -5
    """
    if j < 0:
        raise ValueError(f"Hierarchy index j must be >= 0, got {j}")
    return 1 - 2 * j


def bar_length_degree_commutator(k: int, j: int) -> int:
    r"""Bar-length degree of the commutator [b_k, B^{(j)}].

    [b_k, B^{(j)}] = b_k circ B^{(j)} + B^{(j)} circ b_k

    Both compositions have the same bar-length degree (sum of individual
    degrees), since bar-length degree is additive under composition:

        deg([b_k, B^{(j)}]) = deg(b_k) + deg(B^{(j)})
                             = -(k-1) + (1-2j)
                             = 2 - k - 2j.

    Parameters
    ----------
    k : int
        Arity of the A-infinity operation (k >= 1).
    j : int
        Connes hierarchy index (j >= 0).

    Returns
    -------
    int
        Bar-length degree = 2 - k - 2j.

    Examples
    --------
    >>> bar_length_degree_commutator(2, 0)  # [m_2, B]: preserves length
    0
    >>> bar_length_degree_commutator(3, 0)  # [m_3, B]: reduces by 1
    -1
    >>> bar_length_degree_commutator(2, 2)  # [m_2, B^{(2)}]
    -4
    >>> bar_length_degree_commutator(3, 2)  # [m_3, B^{(2)}]: the target
    -5
    """
    return bar_length_degree_b_k(k) + bar_length_degree_B_j(j)


# =========================================================================
#  1. Bidegree table and decomposition verification
# =========================================================================

@dataclass(frozen=True)
class BidegreeEntry:
    """A single entry in the bidegree table for [b_k, B^{(j)}].

    Attributes
    ----------
    k : int
        Arity of the A-infinity operation.
    j : int
        Connes hierarchy index.
    bar_length_degree : int
        Bar-length degree of [b_k, B^{(j)}].
    """
    k: int
    j: int
    bar_length_degree: int

    def __repr__(self) -> str:
        return (f"[b_{self.k}, B^({self.j})]: "
                f"bar-length degree = {self.bar_length_degree}")


def bidegree_table(k_max: int = 6, j_max: int = 3
                   ) -> List[BidegreeEntry]:
    r"""Compute the full bidegree table for [b_k, B^{(j)}].

    Parameters
    ----------
    k_max : int
        Maximum arity to include (default: 6).
    j_max : int
        Maximum hierarchy index to include (default: 3, for CY_3).

    Returns
    -------
    List[BidegreeEntry]
        All bidegree entries for 1 <= k <= k_max, 0 <= j <= j_max.
    """
    entries = []
    for j in range(j_max + 1):
        for k in range(1, k_max + 1):
            deg = bar_length_degree_commutator(k, j)
            entries.append(BidegreeEntry(k=k, j=j, bar_length_degree=deg))
    return entries


def check_decomposition_at_fixed_j(j: int, k_max: int = 10
                                   ) -> Dict[str, Any]:
    r"""Report fixed-j bar-length distinctness.

    For fixed j, the commutator [b, B^{(j)}] = sum_{k>=1} [b_k, B^{(j)}].
    Each term [b_k, B^{(j)}] has bar-length degree 2 - k - 2j.
    Since this is a strictly decreasing function of k (for fixed j),
    all terms have DISTINCT bar-length degrees.

    This degree separation is only a diagnostic.  It does not prove
    [b_k, B^{(j)}_term] = 0, because Costello's chain-map theorem applies
    to the corrected TCFT operator rather than the raw termwise contraction.

    Parameters
    ----------
    j : int
        Fixed Connes hierarchy index.
    k_max : int
        Maximum arity to check (default: 10).

    Returns
    -------
    dict
        Verification results.
    """
    degrees = []
    entries = []
    for k in range(1, k_max + 1):
        deg = bar_length_degree_commutator(k, j)
        degrees.append(deg)
        entries.append(BidegreeEntry(k=k, j=j, bar_length_degree=deg))

    # Check all degrees are distinct
    all_distinct = len(set(degrees)) == len(degrees)

    # Check that degrees are strictly decreasing
    strictly_decreasing = all(
        degrees[i] > degrees[i + 1] for i in range(len(degrees) - 1)
    )

    # Backward-compatible key: this records degree distinctness only.
    decomposition_holds = all_distinct

    return {
        "j": j,
        "k_range": list(range(1, k_max + 1)),
        "degrees": degrees,
        "all_distinct": all_distinct,
        "strictly_decreasing": strictly_decreasing,
        "decomposition_holds": decomposition_holds,
        "termwise_vanishing_established": False,
        "entries": entries,
        "conclusion": (
            f"Fixed-j bar-length shifts for B^({j}) are distinct for "
            f"k = 1, ..., {k_max}; this does not establish termwise "
            f"vanishing for B_term^({j})."
            if decomposition_holds
            else f"FAILED: bidegrees collide at j = {j}"
        ),
    }


def check_full_bidegree_decomposition(k_max: int = 6, j_max: int = 3
                                      ) -> Dict[str, Any]:
    r"""Full fixed-j bar-length diagnostic for all j.

    For each j in {0, 1, ..., j_max}, verify that the bidegrees of
    [b_k, B^{(j)}] are distinct across k.  The result is not a proof of
    the old per-k vanishing claim.

    Parameters
    ----------
    k_max : int
        Maximum arity to check.
    j_max : int
        Maximum hierarchy index to check.

    Returns
    -------
    dict
        Full verification results.
    """
    results_by_j = {}
    all_pass = True
    for j in range(j_max + 1):
        result = check_decomposition_at_fixed_j(j, k_max)
        results_by_j[j] = result
        if not result["decomposition_holds"]:
            all_pass = False

    return {
        "k_max": k_max,
        "j_max": j_max,
        "results_by_j": results_by_j,
        "all_decompositions_hold": all_pass,
        "total_entries": (k_max) * (j_max + 1),
    }


# =========================================================================
#  2. Cross-bidegree collision analysis
# =========================================================================

def collision_analysis(k_max: int = 6, j_max: int = 3
                       ) -> Dict[str, Any]:
    r"""Analyze whether different (k, j) pairs can have the same bidegree.

    For the FULL identity sum_{k,j} ... = 0, we need to check whether
    (k, j) != (k', j') can give the same bar-length degree.

    The bar-length degree is 2 - k - 2j.  Two pairs (k, j) and (k', j')
    have the same degree iff k + 2j = k' + 2j', i.e., k - k' = 2(j' - j).

    This CAN happen: e.g., (k=3, j=0) and (k=1, j=1) both have degree -1.

    These collisions do not affect the fixed-j arity diagnostic.  They also
    do not repair the old proof: Costello's theorem supplies a corrected
    TCFT chain-map identity, not a raw termwise vanishing statement.

    Parameters
    ----------
    k_max : int
        Maximum arity.
    j_max : int
        Maximum hierarchy index.

    Returns
    -------
    dict
        Collision analysis.
    """
    # Map degree -> list of (k, j) pairs
    degree_to_pairs: Dict[int, List[Tuple[int, int]]] = {}
    for j in range(j_max + 1):
        for k in range(1, k_max + 1):
            deg = bar_length_degree_commutator(k, j)
            if deg not in degree_to_pairs:
                degree_to_pairs[deg] = []
            degree_to_pairs[deg].append((k, j))

    # Find collisions (same degree, different (k,j))
    collisions = {
        deg: pairs for deg, pairs in degree_to_pairs.items()
        if len(pairs) > 1
    }

    # Check: within each j, degrees are distinct
    within_j_distinct = True
    for j in range(j_max + 1):
        j_degrees = [
            bar_length_degree_commutator(k, j) for k in range(1, k_max + 1)
        ]
        if len(set(j_degrees)) != len(j_degrees):
            within_j_distinct = False
            break

    return {
        "degree_to_pairs": degree_to_pairs,
        "cross_j_collisions": collisions,
        "num_cross_j_collisions": len(collisions),
        "within_j_all_distinct": within_j_distinct,
        "conclusion": (
            "Cross-j collisions exist. Within each fixed j, all bidegrees "
            "are distinct; this is a degree diagnostic, not a termwise "
            "vanishing proof."
            if within_j_distinct
            else "FAILURE: within-j collision detected."
        ),
    }


# =========================================================================
#  3. The rejected target result: [m_3, B^{(2)}] = 0
# =========================================================================

@dataclass
class ObsAinfResolution:
    r"""Verdict for the failed bidegree proof of Obs_Ainf.

    The bar-length computations below remain correct as arity diagnostics.
    They do not prove [b_3, B^{(2)}_term]=0.  The strict cyclic CY_3
    witness gives a nonzero commutator, so this engine now records the
    bidegree proof as rejected.  A valid obstruction theorem must use the
    corrected TCFT operator or an explicit HH^{-2} filtration argument.

    Attributes
    ----------
    target_k : int
        Target arity (3 for the Obs_Ainf question).
    target_j : int
        Target hierarchy index (2 for B^{(2)}).
    step1_holds : bool
        Whether Step 1 (Costello's theorem) applies.
    step2_holds : bool
        Whether Step 2 (bar-length decomposition) succeeds.
    obs_ainf_vanishes : bool
        Whether Obs_Ainf = 0 is established.
    bidegree_of_target : int
        Bar-length degree of [b_3, B^{(2)}].
    nearest_bidegree : int
        Nearest bar-length degree from another k value (to show distinctness).
    proof_chain : List[str]
        Human-readable proof steps.
    """
    target_k: int = 3
    target_j: int = 2
    step1_holds: bool = False
    step2_holds: bool = False
    obs_ainf_vanishes: bool = False
    bidegree_of_target: int = 0
    nearest_bidegree: int = 0
    proof_chain: List[str] = field(default_factory=list)


def resolve_obs_ainf(cy_dim: int = 3, k_max: int = 10
                     ) -> ObsAinfResolution:
    r"""Reject the bidegree proof for the termwise Obs_Ainf target.

    Parameters
    ----------
    cy_dim : int
        CY dimension (default: 3).
    k_max : int
        Maximum arity for verification (default: 10).

    Returns
    -------
    ObsAinfResolution
        Complete resolution with proof chain.
    """
    target_k = 3
    target_j = 2
    proof_chain = []

    # Step 1: Costello's theorem gives a total corrected TCFT identity.
    # It does not identify the corrected operator with B_term^{(2)}.
    step1_holds = False
    proof_chain.append(
        f"Step 1 rejected for the termwise target: Costello's theorem "
        f"applies to the corrected TCFT operator when d={cy_dim}, but "
        f"does not prove [b, B_term^({target_j})] = 0."
    )

    # Step 2: the degree table is true, but the proof inference is false.
    decomp = check_decomposition_at_fixed_j(target_j, k_max)
    step2_holds = False
    proof_chain.append(
        f"Step 2 diagnostic at j={target_j}. "
        f"Degrees for k=1..{k_max}: {decomp['degrees'][:k_max]}. "
        f"All distinct: {decomp['all_distinct']}. "
        f"Strictly decreasing: {decomp['strictly_decreasing']}. "
        f"Distinct shifts do not imply termwise vanishing."
    )

    # Target bidegree
    bidegree = bar_length_degree_commutator(target_k, target_j)
    proof_chain.append(
        f"Target: [b_{target_k}, B^({target_j})] has bar-length degree "
        f"{bidegree}."
    )

    # Nearest bidegree (from k = target_k +/- 1)
    neighbors = []
    if target_k > 1:
        neighbors.append(bar_length_degree_commutator(target_k - 1, target_j))
    neighbors.append(bar_length_degree_commutator(target_k + 1, target_j))
    nearest = min(neighbors, key=lambda x: abs(x - bidegree))
    proof_chain.append(
        f"Nearest neighbor bidegree: {nearest} "
        f"(from k={target_k - 1} or k={target_k + 1}). "
        f"Gap = {abs(nearest - bidegree)} > 0, confirming distinctness."
    )

    # Conclusion
    obs_ainf_vanishes = False
    proof_chain.append(
        f"Conclusion: the bidegree proof is rejected. "
        f"The strict witness has [m_{target_k}, B_term^({target_j})] != 0; "
        f"the corrected TCFT or HH^(-2) theorem is a separate input."
    )

    return ObsAinfResolution(
        target_k=target_k,
        target_j=target_j,
        step1_holds=step1_holds,
        step2_holds=step2_holds,
        obs_ainf_vanishes=obs_ainf_vanishes,
        bidegree_of_target=bidegree,
        nearest_bidegree=nearest,
        proof_chain=proof_chain,
    )


# =========================================================================
#  4. Explicit bar-complex verification (symbolic)
# =========================================================================

@dataclass(frozen=True)
class BarElement:
    """A symbolic bar element [a_0 | a_1 | ... | a_n].

    Attributes
    ----------
    factors : tuple of str
        Names of the tensor factors.
    coeff : Fraction
        Scalar coefficient.
    """
    factors: Tuple[str, ...]
    coeff: Fraction = Fraction(1)

    @property
    def bar_length(self) -> int:
        """Bar length = number of factors - 1 (CC_n has n+1 factors)."""
        return len(self.factors) - 1

    def __repr__(self) -> str:
        inner = " | ".join(self.factors)
        if self.coeff == Fraction(1):
            return f"[{inner}]"
        return f"{self.coeff} * [{inner}]"


def symbolic_b_k_action(element: BarElement, k: int) -> List[BarElement]:
    r"""Symbolically apply b_k to a bar element.

    b_k applies mu_k to each consecutive k-tuple of factors:
        b_k([a_0|...|a_n]) = sum_{i=0}^{n-k+1} +/- [a_0|...|mu_k(a_i,...,a_{i+k-1})|...|a_n]

    For this symbolic computation, we produce elements with factors
    replaced by "mu_k(a_i,...,a_{i+k-1})" strings.

    Parameters
    ----------
    element : BarElement
        Input bar element.
    k : int
        Arity of the A_infinity operation.

    Returns
    -------
    List[BarElement]
        Output terms (symbolic).
    """
    factors = element.factors
    n = len(factors)
    if k > n:
        return []

    result = []
    for i in range(n - k + 1):
        new_factors = (
            factors[:i]
            + (f"mu_{k}({','.join(factors[i:i+k])})",)
            + factors[i+k:]
        )
        result.append(BarElement(
            factors=new_factors,
            coeff=element.coeff,  # signs suppressed in symbolic version
        ))
    return result


def symbolic_B_j_action(element: BarElement, j: int) -> List[BarElement]:
    r"""Symbolically apply B^{(j)} to a bar element.

    B^{(0)} = B: insert identity and cyclically rotate.
    B^{(j)} for j >= 1: insert identity, then contract j pairs using the
    CY pairing.

    For this symbolic computation, we show the structural effect:
    - B^{(0)}: CC_n -> CC_{n+1} (inserts 1, rotates)
    - B^{(j)}: CC_n -> CC_{n+1-2j} (inserts 1, contracts j pairs)

    Parameters
    ----------
    element : BarElement
        Input bar element.
    j : int
        Connes hierarchy index.

    Returns
    -------
    List[BarElement]
        Output terms (symbolic, showing structure).
    """
    factors = element.factors
    n = len(factors)

    if j == 0:
        # Standard Connes B: insert 1 and cyclically rotate
        result = []
        for i in range(n):
            rotated = factors[i:] + factors[:i]
            new_factors = ("1",) + rotated
            result.append(BarElement(
                factors=new_factors, coeff=element.coeff
            ))
        return result
    elif j == 1:
        # B^{(1)}: insert 1, contract one pair with pairing
        result = []
        for i in range(n):
            for p in range(n):
                if p == i:
                    continue
                contracted_name = f"<{factors[i]},{factors[p]}>_1"
                remaining = [f for idx, f in enumerate(factors)
                             if idx != i and idx != p]
                new_factors = ("1",) + tuple(remaining)
                # Prefix with the pairing scalar
                result.append(BarElement(
                    factors=(contracted_name,) + tuple(remaining),
                    coeff=element.coeff,
                ))
        return result
    elif j == 2:
        # B^{(2)}: contract two pairs with CY pairing (degree 2 component)
        result = []
        for i in range(n):
            for p in range(i + 1, n):
                contracted = f"<{factors[i]},{factors[p]}>_2"
                remaining = tuple(
                    f for idx, f in enumerate(factors)
                    if idx != i and idx != p
                )
                # Insert identity among the remaining
                new_factors = ("1",) + remaining
                result.append(BarElement(
                    factors=(contracted,) + remaining,
                    coeff=element.coeff,
                ))
        return result
    else:
        # Higher j: structural placeholder
        return [BarElement(
            factors=(f"B^({j})({','.join(factors)})",),
            coeff=element.coeff,
        )]


def verify_bar_length_change(k: int, j: int, input_length: int = 5
                             ) -> Dict[str, Any]:
    r"""Verify the bar-length change of [b_k, B^{(j)}] on a specific input.

    Creates a symbolic bar element of the given length and computes
    the bar lengths of b_k(B^{(j)}(x)) and B^{(j)}(b_k(x)) to
    verify they match the predicted degree.

    Parameters
    ----------
    k : int
        Arity of A-infinity operation.
    j : int
        Connes hierarchy index.
    input_length : int
        Bar length of input element (default: 5).

    Returns
    -------
    dict
        Verification results.
    """
    # Create symbolic input
    n = input_length
    factors = tuple(f"a_{i}" for i in range(n + 1))
    x = BarElement(factors=factors)

    # Predicted degrees
    predicted_bk = bar_length_degree_b_k(k)
    predicted_Bj = bar_length_degree_B_j(j)
    predicted_comm = bar_length_degree_commutator(k, j)

    # Compute b_k(B^{(j)}(x))
    bj_results = symbolic_B_j_action(x, j)
    bk_of_bj_lengths = set()
    for term in bj_results:
        bk_results = symbolic_b_k_action(term, k)
        for r in bk_results:
            bk_of_bj_lengths.add(r.bar_length)

    # Compute B^{(j)}(b_k(x))
    bk_results = symbolic_b_k_action(x, k)
    bj_of_bk_lengths = set()
    for term in bk_results:
        bj_results2 = symbolic_B_j_action(term, j)
        for r in bj_results2:
            bj_of_bk_lengths.add(r.bar_length)

    # Expected output bar length
    expected_output_length = n + predicted_comm

    return {
        "input_bar_length": n,
        "k": k,
        "j": j,
        "predicted_bk_degree": predicted_bk,
        "predicted_Bj_degree": predicted_Bj,
        "predicted_commutator_degree": predicted_comm,
        "expected_output_length": expected_output_length,
        "bk_of_Bj_lengths": bk_of_bj_lengths,
        "Bj_of_bk_lengths": bj_of_bk_lengths,
        "bk_of_Bj_consistent": (
            len(bk_of_bj_lengths) <= 1
            or all(l == expected_output_length for l in bk_of_bj_lengths)
        ),
        "Bj_of_bk_consistent": (
            len(bj_of_bk_lengths) <= 1
            or all(l == expected_output_length for l in bj_of_bk_lengths)
        ),
    }


# =========================================================================
#  5. Extension to general [b, B^{(j)}] = 0 from Costello's theorem
# =========================================================================

@dataclass
class CostelloChainMapVerification:
    r"""Verification that Costello's theorem applies for given CY dimension.

    Costello's theorem (2005, 2007): For a cyclic A-infinity algebra of
    CY dimension d, the S^d-framing of the cyclic bar complex produces
    corrected TCFT operators B^{(0)}_TCFT, ..., B^{(d)}_TCFT that are
    chain maps of (CC_bullet, b).

    The theorem applies when:
    (1) A is a cyclic A-infinity algebra (cyclically invariant pairing).
    (2) The CY dimension d >= 1.
    (3) The pairing is non-degenerate.

    Attributes
    ----------
    cy_dim : int
        CY dimension d.
    j_values : List[int]
        Valid hierarchy indices 0, ..., d.
    chain_map_identity : str
        The corrected identity [b, B^{(j)}_TCFT] = 0 for each j.
    """
    cy_dim: int
    j_values: List[int] = field(default_factory=list)
    applies: bool = False
    chain_map_identity: str = ""
    conditions: List[str] = field(default_factory=list)

    @classmethod
    def for_cy_dim(cls, d: int) -> "CostelloChainMapVerification":
        """Create verification for a given CY dimension."""
        applies = d >= 1
        j_values = list(range(d + 1))
        return cls(
            cy_dim=d,
            j_values=j_values,
            applies=applies,
            chain_map_identity=(
                f"[b, B_TCFT^(j)] = 0 for j = 0, 1, ..., {d}"
                if applies else "Does not apply"
            ),
            conditions=[
                f"CY dimension d = {d} >= 1: {'YES' if d >= 1 else 'NO'}",
                "Cyclic A-infinity structure: REQUIRED (hypothesis)",
                "Non-degenerate pairing: REQUIRED (hypothesis)",
                f"Costello's theorem applies: {'YES' if applies else 'NO'}",
            ],
        )


# =========================================================================
#  6. Master verification
# =========================================================================

def master_verification(cy_dim: int = 3, k_max: int = 6
                        ) -> Dict[str, Any]:
    r"""Complete diagnostic rejecting the old AP-CY34 bidegree proof.

    Parameters
    ----------
    cy_dim : int
        CY dimension (default: 3).
    k_max : int
        Maximum arity to verify (default: 6).

    Returns
    -------
    dict
        Complete verification results.
    """
    # Step 1: Costello's theorem
    costello = CostelloChainMapVerification.for_cy_dim(cy_dim)

    # Step 2: Full fixed-j degree distinctness diagnostic
    full_decomp = check_full_bidegree_decomposition(k_max, cy_dim)

    # Step 3: Collision analysis
    collisions = collision_analysis(k_max, cy_dim)

    # Step 4: Target resolution (Obs_Ainf)
    resolution = resolve_obs_ainf(cy_dim, k_max)

    # Step 5: Symbolic bar-length verification for target (k=3, j=2)
    bar_verify = verify_bar_length_change(3, 2, input_length=6)

    # Collect all bidegree entries for the target j=2
    j2_table = [
        BidegreeEntry(k=k, j=2,
                      bar_length_degree=bar_length_degree_commutator(k, 2))
        for k in range(1, k_max + 1)
    ]

    return {
        "cy_dimension": cy_dim,
        "k_max": k_max,
        "costello_theorem": {
            "applies": costello.applies,
            "identity": costello.chain_map_identity,
            "conditions": costello.conditions,
        },
        "full_decomposition": {
            "all_hold": full_decomp["all_decompositions_hold"],
            "total_entries": full_decomp["total_entries"],
        },
        "collision_analysis": {
            "within_j_all_distinct": collisions["within_j_all_distinct"],
            "cross_j_collisions": len(collisions["cross_j_collisions"]),
            "conclusion": collisions["conclusion"],
        },
        "obs_ainf_resolution": {
            "vanishes": resolution.obs_ainf_vanishes,
            "bidegree_of_target": resolution.bidegree_of_target,
            "nearest_bidegree": resolution.nearest_bidegree,
            "proof_chain": resolution.proof_chain,
        },
        "j2_bidegree_table": [
            {"k": e.k, "degree": e.bar_length_degree}
            for e in j2_table
        ],
        "bar_length_verification": {
            "k": 3,
            "j": 2,
            "input_length": bar_verify["input_bar_length"],
            "predicted_degree": bar_verify["predicted_commutator_degree"],
            "expected_output_length": bar_verify["expected_output_length"],
        },
        "final_conclusion": (
            "REJECTED. The bidegree proof does not establish "
            "vanishing of the termwise Obs_Ainf commutator. Costello's theorem gives "
            "a total corrected TCFT identity, and the strict witness gives "
            "[m_3, B^{(2)}_term] != 0."
            if resolution.obs_ainf_vanishes
            else "REJECTED. The bidegree proof is false; see proof chain."
        ),
    }
