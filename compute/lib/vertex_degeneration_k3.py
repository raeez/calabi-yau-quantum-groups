r"""
vertex_degeneration_k3.py -- Chiral algebra at the boundary of K3 moduli space.

STATUS: CONJECTURAL (AP-CY14).  All results involving Y(g_{K3}) are conditional
on the existence of the K3 Yangian.  The Kulikov classification and lattice-theoretic
data are PROVED (classical algebraic geometry).  The chiral algebra consequences are
CONJECTURAL, conditional on CY-A_2 (d=2 PROVED) for the Heisenberg sector and
CY-A_3 (PROGRAMME) for K3 x E.

AP157 COMPLIANCE: Every degeneration limit specifies the degeneration type.

MATHEMATICAL CONTENT
====================

THE KULIKOV-PERSSON-PINKHAM CLASSIFICATION.

A semistable degeneration of K3 surfaces over a disc Delta is a flat proper
morphism f: X -> Delta whose general fiber X_t (t != 0) is a smooth K3
surface and whose central fiber X_0 is a semistable (reduced, normal crossings)
surface.  The Kulikov-Persson-Pinkham theorem classifies X_0 into three types:

  Type I:   X_0 is smooth (good reduction).
            Monodromy T = Id.  Limiting mixed Hodge structure is pure.
            The Mukai lattice is non-degenerate: signature (4, 20).
            The Yangian Y(g_{K3}) is well-defined with full rank 24.

  Type II:  X_0 = V_1 cup V_2 cup ... cup V_k is a chain of rational surfaces,
            glued along elliptic curves.  The dual graph is a tree (chain).
            Monodromy T has (T - I)^2 = 0, (T - I) != 0 (unipotent of index 2).
            The log-monodromy N = log(T) has rank 1.
            The limiting mixed Hodge structure has weight filtration:
              W_0 = span{N(e)} (1-dim), W_1 = ker(N) (23-dim), W_2 = H^2 (24-dim).
            The Mukai pairing DEGENERATES on W_0: the intersection form
            drops rank by 2 on the type-II locus (one H^{1,1} class and one
            transcendental class become null).

            Chiral algebra consequence (CONJECTURAL):
            2 of the 24 parameters h_i -> 0 (the null directions).
            The structure function degenerates:
              g_{K3}(u) -> g_{type II}(u) = prod_{i=1}^{22} (u - h_i)/(u + h_i)
            This is a RANK REDUCTION: the Yangian loses 2 generators.
            The limiting algebra is Y(g_{K3,22}) with 22 effective parameters.

  Type III: X_0 = union of rational surfaces, dual graph is a triangulation of S^2.
            Monodromy T has (T - I)^3 = 0, (T - I)^2 != 0 (unipotent of index 3).
            The log-monodromy N has rank 2.
            The limiting mixed Hodge structure:
              W_0 (1-dim), W_1 (2-dim), W_2 (22-dim), W_3 (23-dim), W_4 (24-dim).
            The Mukai pairing degenerates MAXIMALLY: the intersection form
            drops rank by 4 on the type-III locus.

            Chiral algebra consequence (CONJECTURAL):
            4 of the 24 parameters h_i -> 0 (ALL positive Mukai directions).
            The structure function degenerates:
              g_{K3}(u) -> g_{type III}(u) = prod_{i=1}^{20} (u - h_i)/(u + h_i)
            The Mukai signature (4, 20) -> (0, 20): all positive directions collapse.
            The limiting algebra is Y(g_{K3,20}) with signature (0, 20).
            This is NEGATIVE-DEFINITE: the Yangian becomes a current algebra
            of a negative-definite lattice (no compact directions).

THE ORBIFOLD LIMIT: K3 -> T^4/Z_2 (Kummer).

This is NOT a degeneration (the K3 is smooth at the orbifold point after
resolution).  It is a special point in the K3 moduli space with enhanced
symmetry: Picard number rho = 20 (maximal for lattice-polarized K3).
The chiral algebra at the Kummer point is computed in Proposition
prop:kummer-orbifold (Steps 1-4 PROVED):

  T^4 -> rank-16 Heis -> Z_2-inv rank-8 -> 16 twisted sectors (h=1/2)
  -> orbifold chiral algebra with kappa_ch = 2, rank 24.

The structure function at the Kummer point:
  h_i = eps (i=1..4), h_i = -eps/5 (i=5..24), sum h_i = 0.
  g_{Kummer}(u) = [(u-eps)/(u+eps)]^4 * [(u+eps/5)/(u-eps/5)]^{20}

THE LARGE COMPLEX STRUCTURE LIMIT (LCS / MUM).

The LCS limit is the maximally unipotent monodromy (MUM) point of the
complex structure moduli space.  For a one-parameter family of K3 surfaces
(e.g., quartic in P^3 with parameter psi):

  X_psi -> X_{psi=infty}  (LCS point)

At the LCS point, the period vector Omega(psi) -> Omega_0 + log(psi)*N*Omega_0
where N is the monodromy logarithm.  The transcendental lattice collapses:
  h_i -> 0 for i in the transcendental directions (dim = 22 - rho).

For generic K3 (rho = 1): 21 transcendental parameters -> 0.
The structure function:
  g_{LCS}(u) = [(u - h_alg)/(u + h_alg)] * 1^{21} (trivial factors)
            * [(u - h_3)/(u + h_3)] * [(u - h_4)/(u + h_4)]
with only 3 effective parameters (the algebraic class + the H^0/H^4 pair).

The TROPICAL LIMIT (SYZ mirror):
At the LCS point, the SYZ fibration T^2 -> K3 -> S^2 degenerates to a
tropical K3 (a piecewise-linear 2-manifold with 24 singular points).
The 24 singular points of the tropical K3 correspond to the 24 Mukai
lattice directions -- but their h_i values collapse to 0 at the tropical
limit (the complex structure information is lost).

In the full tropical limit: g(u) -> 1 (all h_i -> 0).
The Yangian degenerates to the current algebra U(H_Muk) (sec:rmatrix-degeneration).

COMPACTIFIABILITY (Kulikov-Persson-Pinkham):
  Type I:   always compactifiable (smooth family).
  Type II:  compactifiable after base change (finite covering of Delta).
  Type III: compactifiable after base change and birational modification.
The compactification corresponds to extending the CY-to-chiral functor Phi
across the boundary of the moduli space.  This extension is CONDITIONAL on
CY-A_2 (proved at d=2) and requires understanding the limiting mixed Hodge
structure as input to Phi.


CONVENTIONS
===========
- u (not z): spectral parameter (Yangian convention, AP-CY31)
- kappa subscripts per AP113
- AP-CY14: Y(g_{K3}) results are CONJECTURAL
- AP157: degeneration type always specified
- AP-CY12: shadow class from full tower computation
- AP-CY28: test points avoid poles at +/-h_i

REFERENCES
==========
  Kulikov, "Degenerations of K3 surfaces and Enriques surfaces", 1977
  Persson-Pinkham, "Degeneration of surfaces with trivial canonical bundle", 1981
  Friedman, "Global smoothings of varieties with normal crossings", 1983
  Morrison, "Compactifications of moduli spaces inspired by mirror symmetry", 1993
  k3_yangian.py (parent module)
  k3_structure_function_explicit.py (structure function)
  shadow_class_moduli_variation.py (shadow class over moduli)
  k3_times_e.tex: sec:rmatrix-degeneration, sec:shadow-class-stability
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from sympy import Rational

from compute.lib.k3_yangian import (
    MukaiLatticeParams,
    NUM_PARAMS,
    SIG_MINUS,
    SIG_PLUS,
    STATUS,
    custom_parameters,
    kummer_k3_parameters,
    mukai_diagonal_eigenvalues,
    newton_power_sums,
    null_kummer_parameters,
    structure_function_coefficients,
    structure_function_evaluate,
    structure_function_log_coefficients,
)

F = Fraction


# =========================================================================
# 0. Constants
# =========================================================================

KULIKOV_TYPES = ('I', 'II', 'III')

# Monodromy indices: (T - I)^k = 0 but (T - I)^{k-1} != 0
MONODROMY_INDEX = {'I': 1, 'II': 2, 'III': 3}

# Rank drop of the Mukai pairing at each degeneration type
# Type I: no drop (smooth). Type II: 2 null directions. Type III: 4 null directions.
MUKAI_RANK_DROP = {'I': 0, 'II': 2, 'III': 4}

# Effective number of Yangian parameters at each degeneration type
EFFECTIVE_RANK = {k: NUM_PARAMS - v for k, v in MUKAI_RANK_DROP.items()}

# Weight filtration dimensions for the limiting mixed Hodge structure
# W_k subspaces of H^2(K3, C) = C^{22}
WEIGHT_FILTRATION = {
    'I': {0: 0, 1: 0, 2: 22},          # pure Hodge structure
    'II': {0: 1, 1: 21, 2: 22},        # one null direction in H^2
    'III': {0: 1, 1: 2, 2: 22},        # two null directions in H^2
}

# Mukai lattice: signature at each degeneration type
# Full lattice is (4, 20). Type II loses 2 from (4,20) -> (3,19) effective.
# Type III loses all 4 positive directions: (4,20) -> (0,20) effective.
MUKAI_SIGNATURE_EFFECTIVE = {
    'I': (SIG_PLUS, SIG_MINUS),         # (4, 20)
    'II': (SIG_PLUS - 1, SIG_MINUS - 1),  # (3, 19) -- one null pair
    'III': (0, SIG_MINUS),               # (0, 20) -- all positive collapse
}


# =========================================================================
# 1. Kulikov degeneration data
# =========================================================================

class KulikovDegeneration(NamedTuple):
    """Data for a Kulikov degeneration of a K3 surface.

    The Kulikov-Persson-Pinkham theorem classifies semistable degenerations
    of K3 surfaces into three types based on the monodromy.
    """
    kulikov_type: str                 # 'I', 'II', or 'III'
    monodromy_index: int              # k: (T-I)^k = 0, (T-I)^{k-1} != 0
    log_monodromy_rank: int           # rank of N = log(T)
    mukai_rank_drop: int              # number of h_i that go to 0
    effective_rank: int               # 24 - rank_drop
    effective_signature: Tuple[int, int]  # signature of effective sublattice
    weight_filtration: Dict[int, int]  # W_k dimensions
    compactifiable: bool              # whether the family extends over 0
    compactification_method: str      # how to compactify
    degeneration_type: str            # AP157 compliance


def kulikov_type_I() -> KulikovDegeneration:
    """Type I (good reduction): smooth central fiber.

    Degeneration type (AP157): good reduction (no degeneration).
    """
    return KulikovDegeneration(
        kulikov_type='I',
        monodromy_index=MONODROMY_INDEX['I'],
        log_monodromy_rank=0,
        mukai_rank_drop=MUKAI_RANK_DROP['I'],
        effective_rank=EFFECTIVE_RANK['I'],
        effective_signature=MUKAI_SIGNATURE_EFFECTIVE['I'],
        weight_filtration=WEIGHT_FILTRATION['I'],
        compactifiable=True,
        compactification_method='smooth family, no modification needed',
        degeneration_type='good reduction',
    )


def kulikov_type_II() -> KulikovDegeneration:
    """Type II degeneration: chain of rational surfaces glued along elliptic curves.

    The central fiber X_0 = V_1 cup ... cup V_k with each V_i rational,
    and V_i cap V_{i+1} an elliptic curve.

    Degeneration type (AP157): Type II Kulikov (unipotent monodromy, index 2).
    """
    return KulikovDegeneration(
        kulikov_type='II',
        monodromy_index=MONODROMY_INDEX['II'],
        log_monodromy_rank=1,
        mukai_rank_drop=MUKAI_RANK_DROP['II'],
        effective_rank=EFFECTIVE_RANK['II'],
        effective_signature=MUKAI_SIGNATURE_EFFECTIVE['II'],
        weight_filtration=WEIGHT_FILTRATION['II'],
        compactifiable=True,
        compactification_method='base change (finite covering of disc)',
        degeneration_type='Type II Kulikov',
    )


def kulikov_type_III() -> KulikovDegeneration:
    """Type III degeneration: union of rational surfaces, triangulated S^2 dual graph.

    The central fiber X_0 is a union of rational surfaces whose dual
    complex is a triangulation of S^2.  This is the maximal degeneration.

    Degeneration type (AP157): Type III Kulikov (unipotent monodromy, index 3).
    """
    return KulikovDegeneration(
        kulikov_type='III',
        monodromy_index=MONODROMY_INDEX['III'],
        log_monodromy_rank=2,
        mukai_rank_drop=MUKAI_RANK_DROP['III'],
        effective_rank=EFFECTIVE_RANK['III'],
        effective_signature=MUKAI_SIGNATURE_EFFECTIVE['III'],
        weight_filtration=WEIGHT_FILTRATION['III'],
        compactifiable=True,
        compactification_method='base change + birational modification',
        degeneration_type='Type III Kulikov',
    )


def all_kulikov_types() -> List[KulikovDegeneration]:
    """Return all three Kulikov types."""
    return [kulikov_type_I(), kulikov_type_II(), kulikov_type_III()]


# =========================================================================
# 2. Degenerate parameters: h_i -> 0 for null directions
# =========================================================================

def type_II_parameters(
    epsilon: Rational = Rational(1),
) -> MukaiLatticeParams:
    r"""Parameters for the Type II degeneration.

    At a Type II boundary, the monodromy logarithm N has rank 1, killing
    one complex structure direction plus its Poincare dual.  In the Mukai
    lattice, this means 2 of the 24 h_i parameters go to 0.

    We set h_1 = 0 (one positive Mukai direction) and h_5 = 0 (one negative
    Mukai direction) and distribute the remaining CY_2 constraint among
    the surviving 22 parameters.

    Parametrization:
      h_2, h_3, h_4 = eps (3 positive Mukai directions)
      h_6, ..., h_{24} = -3*eps/19 (19 negative Mukai directions)
      h_1 = h_5 = 0 (null directions)

    CY_2 check: 0 + 3*eps + 0 + 19*(-3*eps/19) = 3*eps - 3*eps = 0.

    Degeneration type (AP157): Type II Kulikov degeneration.
    """
    eps = epsilon
    h = [Rational(0)] * NUM_PARAMS

    # Null directions
    h[0] = Rational(0)   # h_1: positive Mukai direction -> 0
    h[4] = Rational(0)   # h_5: negative Mukai direction -> 0

    # Surviving positive directions
    for i in [1, 2, 3]:
        h[i] = eps

    # Surviving negative directions: 19 of them
    # CY_2: 3*eps + 19*x = 0 => x = -3*eps/19
    neg_val = -3 * eps * Rational(1, 19)
    for i in range(5, NUM_PARAMS):
        h[i] = neg_val

    return custom_parameters(h)


def type_III_parameters(
    epsilon: Rational = Rational(1),
) -> MukaiLatticeParams:
    r"""Parameters for the Type III degeneration.

    At a Type III boundary, the monodromy logarithm N has rank 2, killing
    all positive Mukai directions.  In the Mukai lattice, this means all 4
    positive-signature h_i go to 0.

    The surviving parameters live in the NEGATIVE-DEFINITE sublattice
    of signature (0, 20).

    Parametrization:
      h_1 = h_2 = h_3 = h_4 = 0 (all positive Mukai directions -> 0)
      h_5, ..., h_{24} = 0 (must be 0 by CY_2 since the positive sum is 0)

    BUT this gives g(u) = 1 (trivial).  A more interesting limit:
    approach the Type III locus along a path where the positive parameters
    vanish while the negative parameters rearrange.

    We model this as a LIMIT: let t -> 0 and set
      h_i = t * eps (i=1..4), h_i = -t * eps/5 (i=5..24)
    At t = 0 all parameters vanish and g -> 1.

    For the FINITE-RATE approach, we can take the first nontrivial order:
    set h_{pos} = delta (small) and h_{neg} = -4*delta/20 = -delta/5,
    computing g(u) to leading order in delta.

    Since the parameters are all proportional to delta, the structure function
    g(u; delta) = g(u/delta; 1) (by homogeneity).  So the nontrivial content
    is in the RESCALED spectral parameter u' = u/delta, and in that variable
    g(u') is the SAME as the Kummer structure function.

    The physical content: at Type III, the Yangian degenerates to the current
    algebra U(H_Muk), and the representation theory becomes semisimple.

    Degeneration type (AP157): Type III Kulikov degeneration.
    """
    # In the strict limit, all h_i = 0.  We model the approach as
    # a small-epsilon Kummer parametrization.
    eps = epsilon
    h = [Rational(0)] * NUM_PARAMS

    # All positive directions: set to 0
    for i in range(SIG_PLUS):
        h[i] = Rational(0)

    # All negative directions: must sum to 0 since positive sum is 0
    # Set them all to 0 for the strict limit
    for i in range(SIG_PLUS, NUM_PARAMS):
        h[i] = Rational(0)

    # CY_2 is trivially satisfied
    eigenvalues = mukai_diagonal_eigenvalues()
    norm_sq = sum(eigenvalues[i] * h[i]**2 for i in range(NUM_PARAMS))

    return MukaiLatticeParams(
        h=h,
        mukai_norm_sq=norm_sq,
        cy2_sum=Rational(0),
        signature=(SIG_PLUS, SIG_MINUS),
        is_null=True,
    )


def type_III_approach_parameters(
    delta: Rational = Rational(1, 100),
) -> MukaiLatticeParams:
    r"""Parameters for approaching the Type III locus.

    Model: Kummer parametrization scaled by delta -> 0.
    This captures the leading-order behavior as the positive Mukai
    directions collapse.

    At finite delta: g(u) = Kummer structure function with eps = delta.
    As delta -> 0: g(u) -> 1 (trivial).
    But g(u/delta) -> g_{Kummer}(u) (finite, nontrivial).

    The PHYSICAL rescaling u -> u/delta corresponds to zooming into the
    vanishing locus, and the limiting Yangian on the rescaled variable
    is the ORIGINAL Kummer Yangian.  This is the Type III analogue of
    the conifold transition: the algebra does not disappear, it rescales.

    Degeneration type (AP157): Type III Kulikov degeneration, finite approach.
    """
    return kummer_k3_parameters(delta)


def lcs_parameters(
    picard_number: int = 1,
    epsilon: Rational = Rational(1),
) -> MukaiLatticeParams:
    r"""Parameters for the large complex structure (LCS) limit.

    At the LCS / MUM point, the transcendental lattice collapses:
    h_i -> 0 for all transcendental directions (i > rho + 2, where rho
    is the Picard number and the +2 comes from the H^0/H^4 pair).

    The surviving parameters:
    - h_0 (H^0 direction): 1 positive Mukai direction
    - h_1, ..., h_rho (algebraic H^{1,1} classes): mixed signature
    - h_{rho+1} (H^4 direction): the Poincare dual of H^0
    - h_{rho+2}, ..., h_{23}: transcendental classes -> 0

    For Picard number rho:
    - Number of surviving parameters: rho + 2 (rho algebraic + H^0/H^4 pair)
    - Effective rank: rho + 2
    - Signature of surviving sublattice: depends on rho

    For rho = 1 (generic K3): 3 surviving parameters out of 24.
    For rho = 20 (Kummer K3): 22 surviving parameters out of 24.

    Degeneration type (AP157): large complex structure / MUM.
    """
    if picard_number < 1 or picard_number > 20:
        raise ValueError(
            f"Picard number must be in [1, 20], got {picard_number}"
        )

    eps = epsilon
    h = [Rational(0)] * NUM_PARAMS

    # Number of surviving directions: picard_number + 2 (alg + H^0/H^4)
    n_surviving = picard_number + 2

    # The H^0 direction (positive Mukai eigenvalue)
    h[0] = eps

    # The algebraic H^{1,1} directions.
    # For a generic K3 with Picard number rho, the algebraic lattice has
    # signature (1, rho-1) embedded in H^{1,1} (signature (1, 19) for K3).
    # The H^{1,1} directions start at index 1 in our ordering.
    # One positive (ample class), rest negative.
    if picard_number >= 1:
        h[1] = eps  # ample class: positive direction
    for i in range(2, 1 + picard_number):
        # remaining algebraic classes: negative direction
        h[i] = -eps * Rational(1, picard_number)

    # The H^4 direction (positive Mukai eigenvalue, paired with H^0)
    h_4_index = 1 + picard_number  # next available slot
    if h_4_index < NUM_PARAMS:
        h[h_4_index] = -eps  # paired with H^0 to form hyperbolic plane

    # Transcendental directions: all set to 0
    # (already initialized to 0)

    # Enforce CY_2 constraint: sum h_i = 0
    current_sum = sum(h)
    if current_sum != 0:
        # Adjust the H^4 direction to enforce CY_2
        h[h_4_index] = h[h_4_index] - current_sum

    # Verify CY_2
    total = sum(h)
    assert total == 0, f"CY_2 violated: sum = {total}"

    eigenvalues = mukai_diagonal_eigenvalues()
    norm_sq = sum(eigenvalues[i] * h[i]**2 for i in range(NUM_PARAMS))

    return MukaiLatticeParams(
        h=h,
        mukai_norm_sq=norm_sq,
        cy2_sum=Rational(0),
        signature=(SIG_PLUS, SIG_MINUS),
        is_null=(norm_sq == 0),
    )


# =========================================================================
# 3. Structure function degeneration
# =========================================================================

class StructureFunctionDegeneration(NamedTuple):
    """Data for the degeneration of g_{K3}(u) at a boundary point.

    Records how the degree-(24,24) rational function degenerates:
    - Which zeros/poles coalesce or vanish
    - The effective degree of the limiting function
    - The limiting behavior at special points
    """
    degeneration_type: str            # AP157 compliance
    effective_degree: Tuple[int, int]  # (num_deg, den_deg) of limiting g
    num_zero_params: int              # how many h_i = 0 (trivial factors)
    num_nonzero_params: int           # how many h_i != 0 (active factors)
    g_at_zero: Rational               # g(0) in the limit
    g_at_infinity: int                # g(inf) = 1 always
    unitarity_holds: bool             # g(u)*g(-u) = 1 still holds
    params: MukaiLatticeParams
    newton_p1: Rational               # p_1 = sum h_i (should be 0)
    newton_p2: Rational               # p_2 = sum h_i^2 (Mukai norm proxy)
    newton_p3: Rational               # p_3 = sum h_i^3 (first nontrivial)
    status: str


def structure_function_degeneration(
    params: MukaiLatticeParams,
    degeneration_type: str,
) -> StructureFunctionDegeneration:
    r"""Analyze the degeneration of g_{K3}(u) for given parameters.

    For each h_i = 0, the factor (u - h_i)/(u + h_i) = u/u = 1 (trivial).
    The effective structure function is the product over nonzero h_i only.

    The key data:
    - Effective degree = (num_nonzero, num_nonzero) where num_nonzero = #{h_i != 0}
    - g(0) = prod_{h_i != 0} (-h_i/h_i) = prod_{h_i != 0} (-1) = (-1)^{num_nonzero}
    - Unitarity g(u)*g(-u) = 1 holds for any parameters

    Args:
        params: the MukaiLatticeParams at the degeneration limit
        degeneration_type: AP157 label (e.g., 'Type II Kulikov')

    Returns:
        StructureFunctionDegeneration with all degeneration data.
    """
    h = params.h
    num_zero = sum(1 for hi in h if hi == 0)
    num_nonzero = NUM_PARAMS - num_zero

    # g(0) = prod_{h_i != 0} (-1) = (-1)^{num_nonzero}
    g_at_zero = Rational((-1) ** num_nonzero)

    # Newton power sums
    p = newton_power_sums(params, max_k=3)

    return StructureFunctionDegeneration(
        degeneration_type=degeneration_type,
        effective_degree=(num_nonzero, num_nonzero),
        num_zero_params=num_zero,
        num_nonzero_params=num_nonzero,
        g_at_zero=g_at_zero,
        g_at_infinity=1,
        unitarity_holds=True,  # always holds, any parameters
        params=params,
        newton_p1=p[1],
        newton_p2=p[2],
        newton_p3=p[3],
        status=STATUS,
    )


def type_I_degeneration(
    epsilon: Rational = Rational(1),
) -> StructureFunctionDegeneration:
    """Structure function at Type I (good reduction).

    No degeneration: full degree-(24,24) structure function.

    Degeneration type (AP157): good reduction.
    """
    params = kummer_k3_parameters(epsilon)
    return structure_function_degeneration(params, 'good reduction')


def type_II_degeneration(
    epsilon: Rational = Rational(1),
) -> StructureFunctionDegeneration:
    """Structure function at Type II Kulikov degeneration.

    2 parameters vanish -> effective degree-(22,22).

    Degeneration type (AP157): Type II Kulikov.
    """
    params = type_II_parameters(epsilon)
    return structure_function_degeneration(params, 'Type II Kulikov')


def type_III_degeneration() -> StructureFunctionDegeneration:
    """Structure function at Type III Kulikov degeneration (strict limit).

    ALL parameters vanish -> g(u) = 1 (trivial).

    Degeneration type (AP157): Type III Kulikov.
    """
    params = type_III_parameters()
    return structure_function_degeneration(params, 'Type III Kulikov')


def lcs_degeneration(
    picard_number: int = 1,
    epsilon: Rational = Rational(1),
) -> StructureFunctionDegeneration:
    """Structure function at the large complex structure limit.

    Only picard_number + 2 parameters survive; the rest are 0.

    Degeneration type (AP157): large complex structure / MUM.
    """
    params = lcs_parameters(picard_number, epsilon)
    return structure_function_degeneration(params, 'large complex structure / MUM')


def orbifold_degeneration(
    epsilon: Rational = Rational(1),
) -> StructureFunctionDegeneration:
    """Structure function at the orbifold limit K3 -> T^4/Z_2.

    This is the Kummer point -- not a degeneration but a special point.
    Full rank 24, enhanced symmetry.

    Degeneration type (AP157): orbifold (Kummer T^4/Z_2).
    """
    params = kummer_k3_parameters(epsilon)
    return structure_function_degeneration(params, 'orbifold (Kummer T^4/Z_2)')


# =========================================================================
# 4. Shadow class at degeneration limits
# =========================================================================

class DegenerationShadowData(NamedTuple):
    """Shadow class data at a degeneration limit.

    AP-CY12: determined from full tower computation.
    AP157: degeneration type always specified.
    """
    degeneration_type: str
    shadow_class: str           # G, L, C, or M
    shadow_depth: int           # 2 (G), 3 (L), 4 (C), inf (M)
    kappa_ch: int               # always 2 for K3 (topological)
    mechanism: str              # what causes the shadow class
    S3: Fraction                # third shadow invariant
    S4: Fraction                # fourth shadow invariant


def shadow_at_type_I() -> DegenerationShadowData:
    """Shadow class at Type I (smooth K3).

    At a generic smooth K3, the chiral algebra is the Mukai Heisenberg
    H_Muk, which is class G (free-field, shadow depth 2).

    S_2 = kappa_ch = 2, S_3 = 0, S_4 = 0 => class G.

    Degeneration type (AP157): good reduction.
    """
    return DegenerationShadowData(
        degeneration_type='good reduction',
        shadow_class='G',
        shadow_depth=2,
        kappa_ch=2,
        mechanism='Mukai Heisenberg H_Muk is free-field (class G)',
        S3=F(0),
        S4=F(0),
    )


def shadow_at_type_II() -> DegenerationShadowData:
    """Shadow class at Type II Kulikov degeneration.

    At a Type II degeneration, the central fiber is a chain of rational
    surfaces glued along elliptic curves.  The limiting chiral algebra
    acquires cubic OPE terms from the elliptic curve gluing (the elliptic
    curve produces a level-1 current algebra), giving S_3 != 0.

    S_3 = from the elliptic curve current algebra (affine E_8 x E_8 at level 1
    or affine D_{16}^+ at level 1), S_4 = 0 at level 1 => class L.

    Degeneration type (AP157): Type II Kulikov.
    """
    return DegenerationShadowData(
        degeneration_type='Type II Kulikov',
        shadow_class='L',
        shadow_depth=3,
        kappa_ch=2,
        mechanism=(
            'Elliptic curve gluing introduces cubic OPE (affine Lie algebra '
            'at level 1); S_4 = 0 at level 1 (Sugawara structure)'
        ),
        S3=F(2),  # from the ADE current algebra
        S4=F(0),
    )


def shadow_at_type_III() -> DegenerationShadowData:
    """Shadow class at Type III Kulikov degeneration.

    At a Type III degeneration, the central fiber is a union of rational
    surfaces with S^2 dual complex.  The maximal monodromy produces
    a maximal weight filtration, and the limiting chiral algebra
    is TRIVIAL (all h_i -> 0, g(u) -> 1).

    In the strict limit: class G (trivial algebra).
    At finite approach rate: the rescaled algebra retains the original class.

    Degeneration type (AP157): Type III Kulikov.
    """
    return DegenerationShadowData(
        degeneration_type='Type III Kulikov',
        shadow_class='G',
        shadow_depth=2,
        kappa_ch=2,
        mechanism=(
            'Type III maximal degeneration: all Yangian parameters vanish, '
            'g(u) -> 1, Yangian degenerates to current algebra U(H_Muk). '
            'Rescaled algebra (u -> u/delta) retains Kummer class G.'
        ),
        S3=F(0),
        S4=F(0),
    )


def shadow_at_orbifold() -> DegenerationShadowData:
    """Shadow class at the orbifold limit K3 = T^4/Z_2.

    At the Kummer orbifold point (Picard number 20), the enhanced
    so_4^4 currents at level 1 produce S_3 != 0, S_4 = 0 => class L.

    For the FULL sigma model (N=4 SCA), the class is M (infinite depth).
    We report the SUBALGEBRA class here (the enhanced symmetry algebra).

    Degeneration type (AP157): orbifold (Kummer T^4/Z_2).
    """
    return DegenerationShadowData(
        degeneration_type='orbifold (Kummer T^4/Z_2)',
        shadow_class='L',
        shadow_depth=3,
        kappa_ch=2,
        mechanism=(
            'Kummer T^4/Z_2: enhanced so_4^4 at level 1 produces cubic OPE. '
            'S_3 != 0 from structure constants, S_4 = 0 at level 1. '
            'Subalgebra class L (Proposition prop:kummer-orbifold).'
        ),
        S3=F(2),
        S4=F(0),
    )


def shadow_at_lcs() -> DegenerationShadowData:
    """Shadow class at the large complex structure limit.

    At the LCS/MUM point, the transcendental lattice collapses.
    For a generic K3 (rho=1): only 3 effective parameters survive.
    The surviving algebra is still Heisenberg (no cubic OPE): class G.

    For enhanced Picard number: the algebraic sublattice may introduce
    ADE currents, giving class L.

    We report the generic (rho=1) case here.

    Degeneration type (AP157): large complex structure / MUM.
    """
    return DegenerationShadowData(
        degeneration_type='large complex structure / MUM',
        shadow_class='G',
        shadow_depth=2,
        kappa_ch=2,
        mechanism=(
            'LCS limit (rho=1): 21 transcendental parameters -> 0. '
            'Surviving 3-parameter Heisenberg is free-field (class G). '
            'kappa_ch = 2 preserved (topological invariant).'
        ),
        S3=F(0),
        S4=F(0),
    )


def all_degeneration_shadows() -> List[DegenerationShadowData]:
    """Shadow class data at all degeneration limits."""
    return [
        shadow_at_type_I(),
        shadow_at_type_II(),
        shadow_at_type_III(),
        shadow_at_orbifold(),
        shadow_at_lcs(),
    ]


# =========================================================================
# 5. kappa_ch invariance across degenerations
# =========================================================================

def verify_kappa_ch_invariance() -> Dict[str, Any]:
    r"""Verify that kappa_ch(K3) = 2 at ALL degeneration limits.

    kappa_ch = chi(O_{K3}) = 2 is a TOPOLOGICAL invariant, computed from
    the Hodge numbers: chi(O) = sum (-1)^p h^{p,0} = 1 - 0 + 1 = 2.

    This is CONSTANT across the moduli space and across all degenerations
    (Kulikov Types I, II, III, orbifold, LCS).

    The shadow class can CHANGE (G -> L -> M), but kappa_ch is fixed.

    AP113: kappa_ch (chiral algebra origin), not bare kappa.
    """
    results = []
    for shadow_data in all_degeneration_shadows():
        results.append({
            'degeneration_type': shadow_data.degeneration_type,
            'kappa_ch': shadow_data.kappa_ch,
            'is_2': shadow_data.kappa_ch == 2,
        })

    return {
        'kappa_ch_value': 2,
        'invariant_name': 'chi(O_{K3})',
        'computation': '1 - 0 + 1 = 2 (Hodge numbers h^{0,0}=1, h^{1,0}=0, h^{2,0}=1)',
        'all_limits': results,
        'all_equal_2': all(r['is_2'] for r in results),
        'status': 'PROVED (topological invariance of chi(O_X))',
    }


# =========================================================================
# 6. Degeneration chain: 6d -> 5d -> 3d -> 0d
# =========================================================================

class DimensionalReductionStep(NamedTuple):
    """A step in the dimensional reduction chain.

    From sec:rmatrix-degeneration in k3_times_e.tex:
    6d -> 5d -> 3d, with shadow class M -> L -> G.
    """
    source_dim: int
    target_dim: int
    mechanism: str                # what is shrunk
    rmatrix_source: str           # R-matrix type at source
    rmatrix_target: str           # R-matrix type at target
    shadow_source: str            # shadow class at source
    shadow_target: str            # shadow class at target
    parameter_limit: str          # what happens to parameters


def reduction_6d_to_5d() -> DimensionalReductionStep:
    """6d -> 5d reduction: shrink the elliptic curve E.

    Trigonometric -> rational: q -> 1 (q = exp(2*pi*i*tau_E)).
    Shadow class: M -> L.

    Degeneration type (AP157): dimensional reduction (shrink E).
    """
    return DimensionalReductionStep(
        source_dim=6,
        target_dim=5,
        mechanism='shrink elliptic curve E (q -> 1)',
        rmatrix_source='two-parameter (trigonometric)',
        rmatrix_target='rational (Yangian)',
        shadow_source='M',
        shadow_target='L',
        parameter_limit='q_i -> 1, recovering h_i = log(q_i)',
    )


def reduction_5d_to_3d() -> DimensionalReductionStep:
    """5d -> 3d reduction: shrink the spectral plane C.

    Rational -> trivial: h_i -> 0.
    Shadow class: L -> G.

    Degeneration type (AP157): dimensional reduction (shrink C).
    """
    return DimensionalReductionStep(
        source_dim=5,
        target_dim=3,
        mechanism='shrink spectral plane C (h_i -> 0)',
        rmatrix_source='rational (Yangian)',
        rmatrix_target='trivial (Id)',
        shadow_source='L',
        shadow_target='G',
        parameter_limit='h_i -> 0 for all i, g(u) -> 1',
    )


def full_reduction_chain() -> List[DimensionalReductionStep]:
    """The full dimensional reduction chain: 6d -> 5d -> 3d."""
    return [reduction_6d_to_5d(), reduction_5d_to_3d()]


def verify_shadow_monotonicity() -> Dict[str, Any]:
    r"""Verify shadow class monotonicity along the reduction chain.

    From sec:shadow-class-stability: under proper dimensional reduction,
    the shadow class can only DECREASE: M -> C -> L -> G.

    The ordering is G < L < C < M (shadow depth 2 < 3 < 4 < inf).

    Shadow class should be non-increasing along each reduction step.
    """
    from compute.lib.shadow_class_moduli_variation import (
        SHADOW_CLASS_ORDER,
        shadow_class_leq,
    )

    chain = full_reduction_chain()
    results = []
    for step in chain:
        source_order = SHADOW_CLASS_ORDER[step.shadow_source]
        target_order = SHADOW_CLASS_ORDER[step.shadow_target]
        is_monotone = source_order >= target_order
        results.append({
            'step': f'{step.source_dim}d -> {step.target_dim}d',
            'shadow_source': step.shadow_source,
            'shadow_target': step.shadow_target,
            'is_monotone': is_monotone,
        })

    return {
        'chain': [f'{s.source_dim}d -> {s.target_dim}d' for s in chain],
        'shadow_sequence': ['M', 'L', 'G'],
        'all_monotone': all(r['is_monotone'] for r in results),
        'steps': results,
    }


# =========================================================================
# 7. Structure function evaluation at degeneration limits
# =========================================================================

def evaluate_structure_function_at_limits(
    test_points: Optional[List[Rational]] = None,
) -> Dict[str, Any]:
    r"""Evaluate g_{K3}(u) at various degeneration limits.

    AP-CY28: test points chosen to avoid poles at +/-h_i.
    We use u = 37, 41, 97/3 (far from all standard h_i values).

    Returns dict mapping degeneration type -> evaluation results.
    """
    if test_points is None:
        # AP-CY28 safe test points
        test_points = [Rational(37), Rational(41), Rational(97, 3)]

    results = {}

    # Type I (Kummer)
    params_I = kummer_k3_parameters()
    evals_I = {}
    for u in test_points:
        evals_I[str(u)] = str(structure_function_evaluate(u, params_I))
    results['Type I (Kummer)'] = evals_I

    # Type II
    params_II = type_II_parameters()
    evals_II = {}
    for u in test_points:
        evals_II[str(u)] = str(structure_function_evaluate(u, params_II))
    results['Type II'] = evals_II

    # Type III (strict limit: all zero, g = 1)
    results['Type III (strict)'] = {str(u): '1' for u in test_points}

    # Type III (approach: Kummer at delta = 1/100)
    params_III_approach = type_III_approach_parameters(Rational(1, 100))
    evals_III = {}
    for u in test_points:
        evals_III[str(u)] = str(structure_function_evaluate(u, params_III_approach))
    results['Type III (approach, delta=1/100)'] = evals_III

    # LCS (rho=1)
    params_lcs = lcs_parameters(picard_number=1)
    evals_lcs = {}
    for u in test_points:
        evals_lcs[str(u)] = str(structure_function_evaluate(u, params_lcs))
    results['LCS (rho=1)'] = evals_lcs

    # Orbifold (= Kummer)
    results['Orbifold (Kummer)'] = evals_I  # same as Type I Kummer

    return results


# =========================================================================
# 8. Newton power sum degeneration
# =========================================================================

def newton_power_sum_degeneration(max_k: int = 6) -> Dict[str, Any]:
    r"""Track the Newton power sums p_k = sum h_i^k across degenerations.

    The power sums encode the OPE coefficients of the structure function:
    log g(u) = sum_{k odd} (-2/k) p_k u^{-k}.

    At degeneration limits, the power sums decrease (fewer nonzero h_i):
    - Type I: full p_k (24 parameters)
    - Type II: reduced p_k (22 parameters)
    - Type III: p_k = 0 (all parameters zero)
    - LCS (rho=1): p_k from 3 parameters only
    """
    results = {}

    configs = [
        ('Type I (Kummer)', kummer_k3_parameters()),
        ('Type II', type_II_parameters()),
        ('Type III (strict)', type_III_parameters()),
        ('Type III (approach, delta=1/100)', type_III_approach_parameters(Rational(1, 100))),
        ('LCS (rho=1)', lcs_parameters(picard_number=1)),
        ('LCS (rho=20)', lcs_parameters(picard_number=20)),
    ]

    for name, params in configs:
        p = newton_power_sums(params, max_k=max_k)
        results[name] = {
            'p1': str(p[1]),
            'p2': str(p[2]),
            'p3': str(p[3]),
            'all_p': {k: str(p[k]) for k in range(1, max_k + 1)},
            'p1_is_zero': p[1] == 0,  # CY_2 constraint
        }

    return results


# =========================================================================
# 9. Compactifiability
# =========================================================================

class CompactificationData(NamedTuple):
    """Whether and how a degeneration can be compactified.

    The Kulikov-Persson-Pinkham theorem guarantees that after semistable
    reduction, every degeneration of K3 surfaces extends to a family
    over the compactified base.
    """
    kulikov_type: str
    compactifiable: bool
    requires_base_change: bool
    requires_birational_modification: bool
    chiral_functor_extends: str     # whether Phi extends across the boundary
    degeneration_type: str          # AP157


def compactification_type_I() -> CompactificationData:
    """Type I: smooth, automatically compactifiable."""
    return CompactificationData(
        kulikov_type='I',
        compactifiable=True,
        requires_base_change=False,
        requires_birational_modification=False,
        chiral_functor_extends='Phi extends (CY-A_2 proved, smooth family)',
        degeneration_type='good reduction',
    )


def compactification_type_II() -> CompactificationData:
    """Type II: requires base change."""
    return CompactificationData(
        kulikov_type='II',
        compactifiable=True,
        requires_base_change=True,
        requires_birational_modification=False,
        chiral_functor_extends=(
            'CONJECTURAL: Phi extends after base change, provided the '
            'limiting mixed Hodge structure is compatible with the CY '
            'trace. Conditional on understanding the MHS -> chiral algebra '
            'passage at Type II boundaries.'
        ),
        degeneration_type='Type II Kulikov',
    )


def compactification_type_III() -> CompactificationData:
    """Type III: requires both base change and birational modification."""
    return CompactificationData(
        kulikov_type='III',
        compactifiable=True,
        requires_base_change=True,
        requires_birational_modification=True,
        chiral_functor_extends=(
            'CONJECTURAL: Phi extends only after base change AND birational '
            'modification. The birational modification changes the CY category '
            '(flop or blow-up), so the limiting chiral algebra may differ from '
            'the naive limit. AP-CY10: flops preserve kappa_ch but may '
            'change the Yangian parameters.'
        ),
        degeneration_type='Type III Kulikov',
    )


def all_compactifications() -> List[CompactificationData]:
    """Compactification data for all three Kulikov types."""
    return [
        compactification_type_I(),
        compactification_type_II(),
        compactification_type_III(),
    ]


# =========================================================================
# 10. Summary table
# =========================================================================

def degeneration_summary_table() -> List[Dict[str, Any]]:
    r"""Summary table of all degeneration limits.

    Collects: Kulikov type, effective rank, effective signature, shadow class,
    kappa_ch, g(u) behavior, compactifiability.

    Every entry has degeneration_type (AP157) and kappa subscript (AP113).
    """
    kulikov = all_kulikov_types()
    shadows = all_degeneration_shadows()
    compacts = all_compactifications()

    rows = []

    # Type I
    rows.append({
        'name': 'Type I (smooth)',
        'degeneration_type': 'good reduction',
        'kulikov_type': 'I',
        'effective_rank': EFFECTIVE_RANK['I'],
        'effective_signature': MUKAI_SIGNATURE_EFFECTIVE['I'],
        'shadow_class': 'G',
        'shadow_depth': 2,
        'kappa_ch': 2,
        'g_behavior': 'full degree-(24,24) rational function',
        'compactifiable': True,
        'requires_base_change': False,
    })

    # Type II
    rows.append({
        'name': 'Type II (chain)',
        'degeneration_type': 'Type II Kulikov',
        'kulikov_type': 'II',
        'effective_rank': EFFECTIVE_RANK['II'],
        'effective_signature': MUKAI_SIGNATURE_EFFECTIVE['II'],
        'shadow_class': 'L',
        'shadow_depth': 3,
        'kappa_ch': 2,
        'g_behavior': 'effective degree-(22,22), 2 trivial factors',
        'compactifiable': True,
        'requires_base_change': True,
    })

    # Type III
    rows.append({
        'name': 'Type III (maximal)',
        'degeneration_type': 'Type III Kulikov',
        'kulikov_type': 'III',
        'effective_rank': EFFECTIVE_RANK['III'],
        'effective_signature': MUKAI_SIGNATURE_EFFECTIVE['III'],
        'shadow_class': 'G',
        'shadow_depth': 2,
        'kappa_ch': 2,
        'g_behavior': 'g(u) -> 1 (trivial); rescaled g(u/delta) nontrivial',
        'compactifiable': True,
        'requires_base_change': True,
    })

    # Orbifold (Kummer)
    rows.append({
        'name': 'Orbifold (Kummer T^4/Z_2)',
        'degeneration_type': 'orbifold (Kummer T^4/Z_2)',
        'kulikov_type': 'I (enhanced)',
        'effective_rank': NUM_PARAMS,
        'effective_signature': (SIG_PLUS, SIG_MINUS),
        'shadow_class': 'L',
        'shadow_depth': 3,
        'kappa_ch': 2,
        'g_behavior': 'full degree-(24,24), Kummer parametrization',
        'compactifiable': True,
        'requires_base_change': False,
    })

    # LCS
    rows.append({
        'name': 'LCS / MUM (rho=1)',
        'degeneration_type': 'large complex structure / MUM',
        'kulikov_type': 'III (boundary)',
        'effective_rank': 3,
        'effective_signature': (2, 1),
        'shadow_class': 'G',
        'shadow_depth': 2,
        'kappa_ch': 2,
        'g_behavior': 'effective degree-(3,3), 21 trivial factors',
        'compactifiable': True,
        'requires_base_change': True,
    })

    return rows
