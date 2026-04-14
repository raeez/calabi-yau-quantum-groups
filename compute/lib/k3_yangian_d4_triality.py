r"""K3 Yangian at the D_4 triality enhancement point.

STATUS: CONJECTURAL (AP-CY14).  The K3 Yangian Y(g_{K3}) is not constructed.
All results are conditional on the existence of Y(g_{K3}).  The D_4 Yangian
Y(so_8) at level 1 is an unconditionally defined mathematical object; its
EMBEDDING as a subalgebra of Y(g_{K3}) is what requires CY-A_2.

MATHEMATICAL CONTENT
====================

D_4 is the richest ADE enhancement on K3: the only simply-laced Dynkin
diagram with a nontrivial outer automorphism group.  The outer automorphism
group Out(D_4) = S_3 (triality) acts by permuting the three legs of the
tristar diagram:

    Dynkin diagram of D_4:
        0
         \
          1 -- 2
         /
        3

    Node 1 is the branching node with valence 3.
    Legs: {0, 2, 3} are the three endpoints.
    S_3 permutes {0, 2, 3} while fixing 1.

At a D_4 singularity on K3:
  - dim(so_8) = 28 root generators enter the chiral algebra
  - 4 Mukai directions merge into the D_4 root lattice
  - 20 abelian complement directions remain
  - The K3 Yangian DECOMPOSES as Y(so_8) x Heis^{20}
  - S_3 triality acts on Y(so_8), permuting the three 8-dim basic reps

THE THREE 8-DIMENSIONAL REPRESENTATIONS
========================================

so_8 has three 8-dimensional fundamental representations:

  8_v = V(omega_1): vector representation        (weights: +/- e_i)
  8_s = V(omega_3): positive spinor              (weights: 1/2(+/-e_1+/-e_2+/-e_3+/-e_4), even # of minus)
  8_c = V(omega_4): negative spinor              (weights: 1/2(+/-e_1+/-e_2+/-e_3+/-e_4), odd # of minus)

All three are 8-dimensional, minuscule, and self-dual.  Triality permutes
them cyclically: sigma: 8_v -> 8_s -> 8_c -> 8_v.

The tensor products:
  8_v x 8_v = 1 + 28 + 35_v     (symmetric: 1+35_v, antisymmetric: 28)
  8_s x 8_s = 1 + 28 + 35_s
  8_c x 8_c = 1 + 28 + 35_c
  8_v x 8_s = 8_c + 56_s
  8_v x 8_c = 8_s + 56_c
  8_s x 8_c = 8_v + 56_v

The cross-products show the triality algebra: V x S^+ = S^-.

THE YANG R-MATRIX ON 8 x 8
============================

R(u) = u * Id_{64} + P  (Yang R-matrix on C^8 tensor C^8)

This is a 64 x 64 matrix.  Under triality sigma, the R-matrix transforms
covariantly:
  (sigma x sigma) R_{V x V}(u) (sigma^{-1} x sigma^{-1}) = R_{S^+ x S^+}(u)

The NUMBER of nonzero entries in the full 64x64 R-matrix:
  - At generic u: ALL 64^2 = 4096 entries can be nonzero
    (because u*Id has 64 nonzero diagonal entries, and P has 64 nonzero entries,
     giving 128 nonzero entries total -- not 4096).
  Actually: R(u) = u*Id + P.
  - Id_{64} has 64 nonzero entries (diagonal)
  - P (permutation) has 64 nonzero entries: P_{(ia),(jb)} = delta_{ib}*delta_{ja}
    These are at positions ((i,a),(a,i)) for all i,a in {0,...,7}.
  - For u != 0: nonzero entries = union of Id support and P support
  - |supp(Id) union supp(P)| = 64 + 64 - 8 = 120
    (overlap: Id and P agree on the 8 diagonal entries (i,i),(i,i))
  - So the 64x64 R-matrix has exactly 120 nonzero entries at generic u.

For the K3 R-matrix at D_4: the FULL 24x24 (charge 1) R-matrix has:
  - D_4 sector: 8x8 block with Yang R-matrix (120 nonzero in 64x64)
  - Abelian sector: 20x20 diagonal block
  - Cross-sector: zero (orthogonality in Mukai lattice)

THE TRIALITY-MIKI QUESTION (AP-CY22)
=====================================

Per AP-CY22: Miki automorphism is algebra-specific (quantum toroidal gl_1),
NOT operadic.  The D_4 triality S_3 is a DIAGRAM automorphism of the Dynkin
diagram, hence an outer automorphism of so_8 and of Y(so_8).

These are DIFFERENT symmetries:
  - Miki: S_3 from Weyl group of CY torus (q_1,q_2,q_3) with q_1*q_2*q_3=1
  - Triality: S_3 = Out(D_4), permuting omega_1, omega_3, omega_4

However, at the D_4 enhancement point on K3, they may COMBINE:
  - The Miki S_3 acts on the abelian (toroidal) sector
  - The triality S_3 acts on the non-abelian (D_4) sector
  - The total symmetry group contains BOTH but they act on DIFFERENT sectors
  - Whether they extend to a common S_3 action on all of Y(g_{K3}) is OPEN

This is stated as a conjecture (AP-CY14 compliance).

CONVENTIONS
===========
  - Cartan of D_4: 4x4, branching node at index 1, legs at {0, 2, 3}
  - Weights: e_i basis of R^4 for the Cartan of so_8
  - Vector rep: +/- e_i (8 weights)
  - Spinor reps: half-integer weights with even/odd number of minus signs
  - AP-CY28: test points avoid poles at z = +/- h_i
  - AP113: all kappa subscripted (kappa_ch, kappa_BKM, kappa_cat, kappa_fiber)

REFERENCES
==========
  ade_yangian_level1.py (ADE Yangian data, RTT, Lax operators)
  k3_serre_relations.py (K3 Serre at enhanced symmetry)
  k3_yangian.py (K3 structure function, R-matrix)
  Conway-Sloane, Sphere Packings (D_4 lattice)
  Kac, Infinite-dimensional Lie algebras (triality)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.ade_yangian_level1 import (
    ADEData,
    ADEMukaiEmbedding,
    DrinfeldsNewRealization,
    RTTVerifierGeneral,
    ade_data,
    all_weights_defining_rep,
    d4_lax_operator,
    d4_triality_data,
    defining_rep_weights,
    lax_diagonal_evaluation,
    yang_r_matrix_NxN,
    yang_r_matrix_unitarity,
)

F = Fraction

# =========================================================================
# 0. Constants and D_4 root system data
# =========================================================================

STATUS = 'CONJECTURAL'  # AP-CY14: K3 Yangian not constructed

# D_4 Lie algebra constants
D4_RANK = 4
D4_DIM_G = 28          # dim(so_8) = 4*(2*4-1) = 28
D4_DIM_V = 8           # dim of vector (and spinor) representations
D4_DUAL_COXETER = 6    # h^vee(D_4) = 2*4-2 = 6
D4_LEVEL1_CC = F(4)    # c(so_8, k=1) = 28/(1+6) = 4
D4_NUM_POS_ROOTS = 12  # (28-4)/2 = 12

# K3 embedding
MUKAI_RANK = 24
COMPLEMENT_RANK = MUKAI_RANK - D4_RANK  # = 20

# Branching node in our Cartan numbering
BRANCHING_NODE = 1      # node 1 connects to 0, 2, 3
LEG_NODES = (0, 2, 3)   # the three S_3-permutable endpoints


# =========================================================================
# 1. D_4 root system
# =========================================================================

def d4_cartan_matrix() -> np.ndarray:
    """D_4 Cartan matrix (4x4).

    Dynkin diagram:
        0
         \\
          1 -- 2
         /
        3

    Node 1 (branching) connects to 0, 2, 3.
    Nodes 0, 2, 3 do NOT connect to each other.
    """
    C = np.array([
        [ 2, -1,  0,  0],
        [-1,  2, -1, -1],
        [ 0, -1,  2,  0],
        [ 0, -1,  0,  2],
    ], dtype=int)
    return C


def d4_simple_roots() -> np.ndarray:
    """Simple roots of D_4 in the e_i basis of R^4.

    Standard Bourbaki convention for D_4:
      alpha_1 = e_1 - e_2
      alpha_2 = e_2 - e_3
      alpha_3 = e_3 - e_4
      alpha_4 = e_3 + e_4

    Our reindexing to match the Cartan matrix numbering:
      alpha_0 = e_1 - e_2     (leg)
      alpha_1 = e_2 - e_3     (branching node)
      alpha_2 = e_3 - e_4     (leg)
      alpha_3 = e_3 + e_4     (leg)

    Check Cartan matrix: <alpha_i, alpha_j> / <alpha_j, alpha_j> * 2 = C_{ij}.
    For simply-laced: <alpha_i, alpha_j> = C_{ij} since all roots have norm 2.
    """
    roots = np.array([
        [1, -1,  0,  0],   # alpha_0 = e_1 - e_2
        [0,  1, -1,  0],   # alpha_1 = e_2 - e_3
        [0,  0,  1, -1],   # alpha_2 = e_3 - e_4
        [0,  0,  1,  1],   # alpha_3 = e_3 + e_4
    ], dtype=float)
    return roots


def d4_positive_roots() -> np.ndarray:
    """All 12 positive roots of D_4.

    The positive roots of D_4 (so_8) are:
      e_i - e_j  for 1 <= i < j <= 4  (6 roots)
      e_i + e_j  for 1 <= i < j <= 4  (6 roots)
    Total: 12 positive roots.

    In our e-basis (0-indexed: e_0, e_1, e_2, e_3):
      e_i - e_j for 0 <= i < j <= 3: 6 roots
      e_i + e_j for 0 <= i < j <= 3: 6 roots
    """
    roots = []
    for i in range(4):
        for j in range(i + 1, 4):
            # e_i - e_j
            r = np.zeros(4)
            r[i] = 1.0
            r[j] = -1.0
            roots.append(r)
            # e_i + e_j
            r2 = np.zeros(4)
            r2[i] = 1.0
            r2[j] = 1.0
            roots.append(r2)
    return np.array(roots)


def verify_d4_root_system() -> Dict[str, Any]:
    """Verify the D_4 root system data.

    Checks:
    1. Simple roots reproduce the Cartan matrix
    2. Correct number of positive roots (12)
    3. All roots have norm 2 (simply-laced)
    4. Branching node has valence 3
    """
    C = d4_cartan_matrix()
    alphas = d4_simple_roots()
    pos_roots = d4_positive_roots()

    # Check 1: Cartan matrix from simple roots
    C_computed = alphas @ alphas.T
    cartan_match = np.allclose(C_computed, C)

    # Check 2: Number of positive roots
    num_pos = len(pos_roots)

    # Check 3: All roots have norm 2
    norms = np.array([np.dot(r, r) for r in pos_roots])
    all_norm_2 = np.allclose(norms, 2.0)

    # Check 4: Branching node valence
    valence_1 = sum(1 for j in range(4) if j != BRANCHING_NODE and C[BRANCHING_NODE, j] == -1)

    return {
        'cartan_matrix_matches': cartan_match,
        'num_positive_roots': num_pos,
        'expected_positive_roots': D4_NUM_POS_ROOTS,
        'positive_roots_correct': num_pos == D4_NUM_POS_ROOTS,
        'all_norm_2': all_norm_2,
        'branching_node_valence': valence_1,
        'branching_node_is_3': valence_1 == 3,
        'dim_g': D4_DIM_G,
        'dim_g_from_roots': 2 * num_pos + D4_RANK,
        'dim_correct': 2 * num_pos + D4_RANK == D4_DIM_G,
    }


# =========================================================================
# 2. The three 8-dimensional representations
# =========================================================================

def vector_rep_weights() -> np.ndarray:
    """Weights of the vector representation 8_v = V(omega_1) of so_8.

    The 8 weights are +/- e_i for i = 0,...,3.
    Standard ordering: e_0, e_1, e_2, e_3, -e_3, -e_2, -e_1, -e_0.

    Returns shape (8, 4) array of weight vectors.
    """
    W = np.zeros((8, 4))
    for i in range(4):
        W[i, i] = 1.0         # +e_i
        W[7 - i, i] = -1.0    # -e_i
    return W


def spinor_plus_weights() -> np.ndarray:
    r"""Weights of the positive spinor representation 8_s = V(omega_3) of so_8.

    The 8 weights are (1/2)(+/-e_0 +/- e_1 +/- e_2 +/- e_3) with an
    EVEN number of minus signs.

    Even number of minus signs among 4 entries: C(4,0)+C(4,2)+C(4,4) = 1+6+1 = 8.
    """
    weights = []
    for s0 in [1, -1]:
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                for s3 in [1, -1]:
                    signs = [s0, s1, s2, s3]
                    num_minus = sum(1 for s in signs if s == -1)
                    if num_minus % 2 == 0:
                        weights.append([0.5 * s for s in signs])
    return np.array(weights)


def spinor_minus_weights() -> np.ndarray:
    r"""Weights of the negative spinor representation 8_c = V(omega_4) of so_8.

    The 8 weights are (1/2)(+/-e_0 +/- e_1 +/- e_2 +/- e_3) with an
    ODD number of minus signs.

    Odd number of minus signs: C(4,1)+C(4,3) = 4+4 = 8.
    """
    weights = []
    for s0 in [1, -1]:
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                for s3 in [1, -1]:
                    signs = [s0, s1, s2, s3]
                    num_minus = sum(1 for s in signs if s == -1)
                    if num_minus % 2 == 1:
                        weights.append([0.5 * s for s in signs])
    return np.array(weights)


def verify_three_reps() -> Dict[str, Any]:
    """Verify properties of the three 8-dimensional representations.

    Checks:
    1. Each has exactly 8 weights
    2. Weight norms: vector has norm 1, spinors have norm 1
    3. Weight sums = 0 (trace-free)
    4. All three are distinct
    5. Highest weights correspond to omega_1, omega_3, omega_4
    """
    W_v = vector_rep_weights()
    W_s = spinor_plus_weights()
    W_c = spinor_minus_weights()

    # Dimensions
    dim_v = len(W_v)
    dim_s = len(W_s)
    dim_c = len(W_c)

    # Weight norms
    norms_v = np.array([np.dot(w, w) for w in W_v])
    norms_s = np.array([np.dot(w, w) for w in W_s])
    norms_c = np.array([np.dot(w, w) for w in W_c])

    # Weight sums (should be zero for each representation)
    sum_v = np.sum(W_v, axis=0)
    sum_s = np.sum(W_s, axis=0)
    sum_c = np.sum(W_c, axis=0)

    # Highest weights (first entry in standard ordering for vector;
    # for spinors, HW is (1/2, 1/2, 1/2, 1/2) for 8_s
    # and (1/2, 1/2, 1/2, -1/2) for 8_c)
    hw_v = np.array([1.0, 0.0, 0.0, 0.0])   # omega_1
    hw_s = np.array([0.5, 0.5, 0.5, 0.5])    # omega_3
    hw_c = np.array([0.5, 0.5, 0.5, -0.5])   # omega_4

    has_hw_v = any(np.allclose(w, hw_v) for w in W_v)
    has_hw_s = any(np.allclose(w, hw_s) for w in W_s)
    has_hw_c = any(np.allclose(w, hw_c) for w in W_c)

    # Distinctness: check that weight sets are different
    # (They differ because vector has integer weights, spinors have half-integer)
    v_set = set(tuple(np.round(w, 10)) for w in W_v)
    s_set = set(tuple(np.round(w, 10)) for w in W_s)
    c_set = set(tuple(np.round(w, 10)) for w in W_c)
    all_distinct = (v_set != s_set) and (s_set != c_set) and (v_set != c_set)
    no_overlap = len(v_set & s_set) == 0 and len(s_set & c_set) == 0

    return {
        'dim_8v': dim_v,
        'dim_8s': dim_s,
        'dim_8c': dim_c,
        'all_dim_8': dim_v == 8 and dim_s == 8 and dim_c == 8,
        'vector_norms': list(np.unique(np.round(norms_v, 10))),
        'spinor_plus_norms': list(np.unique(np.round(norms_s, 10))),
        'spinor_minus_norms': list(np.unique(np.round(norms_c, 10))),
        'vector_norm_1': np.allclose(norms_v, 1.0),
        'spinor_norms_1': np.allclose(norms_s, 1.0) and np.allclose(norms_c, 1.0),
        'sum_v_zero': np.allclose(sum_v, 0.0),
        'sum_s_zero': np.allclose(sum_s, 0.0),
        'sum_c_zero': np.allclose(sum_c, 0.0),
        'has_hw_v': has_hw_v,
        'has_hw_s': has_hw_s,
        'has_hw_c': has_hw_c,
        'all_distinct': all_distinct,
        'no_weight_overlap': no_overlap,
    }


# =========================================================================
# 3. S_3 triality automorphism
# =========================================================================

def triality_permutation_matrix() -> np.ndarray:
    r"""The triality permutation sigma as a 4x4 matrix on R^4 (Cartan space).

    Triality sigma acts on the D_4 Dynkin diagram by cyclically permuting
    the three legs {0, 2, 3} while fixing the branching node 1.  On the
    simple roots, sigma acts as:

        sigma(alpha_0) = alpha_2
        sigma(alpha_2) = alpha_3
        sigma(alpha_3) = alpha_0
        sigma(alpha_1) = alpha_1  (branching node fixed)

    In the e-basis, this translates to:
        alpha_0 = e_0 - e_1   ->  alpha_2 = e_2 - e_3
        alpha_1 = e_1 - e_2   ->  alpha_1 = e_1 - e_2
        alpha_2 = e_2 - e_3   ->  alpha_3 = e_2 + e_3
        alpha_3 = e_2 + e_3   ->  alpha_0 = e_0 - e_1

    The map sigma on the Cartan is the linear map sending:
        (alpha_0, alpha_1, alpha_2, alpha_3) -> (alpha_2, alpha_1, alpha_3, alpha_0)

    As a permutation matrix on the simple root indices:
        0 -> 2, 1 -> 1, 2 -> 3, 3 -> 0

    Returns the 4x4 permutation matrix P_sigma in the simple root basis.
    """
    # Permutation: 0->2, 1->1, 2->3, 3->0
    P = np.zeros((4, 4), dtype=int)
    P[2, 0] = 1   # alpha_0 -> alpha_2
    P[1, 1] = 1   # alpha_1 -> alpha_1
    P[3, 2] = 1   # alpha_2 -> alpha_3
    P[0, 3] = 1   # alpha_3 -> alpha_0
    return P


def verify_triality_automorphism() -> Dict[str, Any]:
    r"""Verify that sigma is an order-3 outer automorphism of D_4.

    Checks:
    1. sigma preserves the Cartan matrix: sigma^T C sigma = C
    2. sigma^3 = Id (order 3)
    3. sigma != Id and sigma^2 != Id (genuinely order 3)
    4. sigma fixes the branching node (index 1)
    5. sigma permutes the three legs cyclically
    """
    C = d4_cartan_matrix()
    P = triality_permutation_matrix()

    # Check 1: Cartan preservation
    C_transformed = P.T @ C @ P
    preserves_cartan = np.array_equal(C_transformed, C)

    # Check 2: Order 3
    P2 = P @ P
    P3 = P2 @ P
    is_order_3 = np.array_equal(P3, np.eye(4, dtype=int))

    # Check 3: Not identity or order 2
    not_id = not np.array_equal(P, np.eye(4, dtype=int))
    not_order_2 = not np.array_equal(P2, np.eye(4, dtype=int))

    # Check 4: Fixes branching node
    fixes_node_1 = P[1, 1] == 1 and sum(P[1, :]) == 1

    # Check 5: Cyclic permutation of legs
    # sigma: 0 -> 2, 2 -> 3, 3 -> 0
    legs_cycle = (P[2, 0] == 1 and P[3, 2] == 1 and P[0, 3] == 1)

    return {
        'preserves_cartan': preserves_cartan,
        'is_order_3': is_order_3,
        'not_identity': not_id,
        'not_order_2': not_order_2,
        'genuine_order_3': is_order_3 and not_id and not_order_2,
        'fixes_branching_node': fixes_node_1,
        'cyclic_on_legs': legs_cycle,
        'sigma_squared': P2.tolist(),
        'sigma_cubed': P3.tolist(),
    }


def triality_on_representations() -> Dict[str, Any]:
    r"""How triality permutes the three 8-dimensional representations.

    sigma: 8_v -> 8_s -> 8_c -> 8_v

    This permutation is INDUCED by the Dynkin diagram automorphism:
      sigma(omega_1) = omega_3,  sigma(omega_3) = omega_4,  sigma(omega_4) = omega_1

    where omega_i are the fundamental weights.

    For the Yangian Y(so_8): triality permutes the three Lax operators
    built on the three basic representations.  The RTT relation is
    COVARIANT: if R_{VV}(u) L_V(u) L_V(v) = L_V(v) L_V(u) R_{VV}(u)
    then R_{SS}(u) L_S(u) L_S(v) = L_S(v) L_S(u) R_{SS}(u) where
    L_S and R_{SS} are the triality images of L_V and R_{VV}.

    At level 1 on K3: all three 8-dimensional representations are
    integrable (k=1 implies basic representations are exactly
    V(omega_1), V(omega_3), V(omega_4) for D_4).
    """
    W_v = vector_rep_weights()
    W_s = spinor_plus_weights()
    W_c = spinor_minus_weights()

    # Highest weights in the Dynkin label basis
    # omega_1 = e_1 in e-basis, omega_3 = (e_1+e_2+e_3+e_4)/2,
    # omega_4 = (e_1+e_2+e_3-e_4)/2
    hw_v = np.array([1.0, 0.0, 0.0, 0.0])
    hw_s = np.array([0.5, 0.5, 0.5, 0.5])
    hw_c = np.array([0.5, 0.5, 0.5, -0.5])

    # Dynkin labels: [<lambda, alpha_i^vee>] for each simple coroot
    # For simply-laced: alpha_i^vee = alpha_i (norm 2, so coroot = root)
    alphas = d4_simple_roots()

    dynkin_v = alphas @ hw_v  # should be (1, 0, 0, 0) = omega_1
    dynkin_s = alphas @ hw_s  # should be (0, 0, 1, 0) = omega_3
    dynkin_c = alphas @ hw_c  # should be (0, 0, 0, 1) = omega_4

    # Under triality sigma: (0->2, 1->1, 2->3, 3->0) on Dynkin labels
    # omega_1 (Dynkin [1,0,0,0]) -> omega_3 (Dynkin [0,0,1,0])
    # omega_3 (Dynkin [0,0,1,0]) -> omega_4 (Dynkin [0,0,0,1])
    # omega_4 (Dynkin [0,0,0,1]) -> omega_1 (Dynkin [1,0,0,0])

    P = triality_permutation_matrix()
    dynkin_v_sigma = P @ dynkin_v
    dynkin_s_sigma = P @ dynkin_s
    dynkin_c_sigma = P @ dynkin_c

    # Verify the cycle: sigma(8_v) = 8_s, sigma(8_s) = 8_c, sigma(8_c) = 8_v
    v_to_s = np.allclose(dynkin_v_sigma, dynkin_s)
    s_to_c = np.allclose(dynkin_s_sigma, dynkin_c)
    c_to_v = np.allclose(dynkin_c_sigma, dynkin_v)

    # Tensor product structure
    # 8_v x 8_s = 8_c + 56_s
    # This is the TRIALITY ALGEBRA: V x S^+ contains S^-
    # Dimension check: 8 x 8 = 64 = 8 + 56

    return {
        'representations': {
            '8_v': {'hw': list(hw_v), 'dynkin': list(np.round(dynkin_v, 10)),
                    'omega': 'omega_1', 'type': 'vector'},
            '8_s': {'hw': list(hw_s), 'dynkin': list(np.round(dynkin_s, 10)),
                    'omega': 'omega_3', 'type': 'positive spinor'},
            '8_c': {'hw': list(hw_c), 'dynkin': list(np.round(dynkin_c, 10)),
                    'omega': 'omega_4', 'type': 'negative spinor'},
        },
        'triality_cycle': {
            'sigma_8v_eq_8s': v_to_s,
            'sigma_8s_eq_8c': s_to_c,
            'sigma_8c_eq_8v': c_to_v,
            'full_cycle': v_to_s and s_to_c and c_to_v,
        },
        'tensor_products': {
            '8v_x_8v': '1 + 28 + 35_v',
            '8s_x_8s': '1 + 28 + 35_s',
            '8c_x_8c': '1 + 28 + 35_c',
            '8v_x_8s': '8_c + 56_s',
            '8v_x_8c': '8_s + 56_c',
            '8s_x_8c': '8_v + 56_v',
            'dim_check': '8 x 8 = 64 = 1 + 28 + 35 = 8 + 56',
        },
        'level_1_integrable': {
            'num_basic_reps': 3,
            'reps': ['8_v', '8_s', '8_c'],
            'all_dim_8': True,
        },
    }


def full_s3_group() -> Dict[str, Any]:
    r"""The full S_3 outer automorphism group of D_4.

    S_3 is generated by:
      sigma = (0 2 3): the 3-cycle (triality)
      tau = (0 2): a transposition (charge conjugation)

    Elements:
      e    = identity
      sigma   = (0 2 3): order 3
      sigma^2 = (0 3 2): order 3
      tau     = (0 2): order 2  (swaps 8_v <-> 8_s, fixes 8_c)
      tau*sigma = (2 3): order 2
      sigma*tau = (0 3): order 2

    |S_3| = 6.

    For the Yangian: S_3 acts as outer automorphisms, permuting the
    three evaluation representations and hence the three Lax operators.
    """
    P = triality_permutation_matrix()
    I4 = np.eye(4, dtype=int)

    # sigma = (0 2 3)
    sigma = P
    sigma2 = sigma @ sigma
    sigma3 = sigma2 @ sigma
    assert np.array_equal(sigma3, I4), "sigma should have order 3"

    # tau = transposition swapping legs 0 and 2 (fixing 1 and 3)
    # In simple root indices: 0 <-> 2, 1 fixed, 3 fixed
    tau = np.eye(4, dtype=int)
    tau[0, 0] = 0
    tau[2, 2] = 0
    tau[0, 2] = 1
    tau[2, 0] = 1

    # Verify tau preserves Cartan
    C = d4_cartan_matrix()
    tau_preserves = np.array_equal(tau.T @ C @ tau, C)
    tau_order_2 = np.array_equal(tau @ tau, I4)

    # Generate all 6 elements
    elements = {
        'e': I4,
        'sigma': sigma,
        'sigma2': sigma2,
        'tau': tau,
        'tau_sigma': tau @ sigma,
        'sigma_tau': sigma @ tau,
    }

    # Verify all distinct
    all_distinct = True
    names = list(elements.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if np.array_equal(elements[names[i]], elements[names[j]]):
                all_distinct = False

    # Verify all preserve Cartan
    all_preserve_cartan = all(
        np.array_equal(g.T @ C @ g, C) for g in elements.values()
    )

    # Orders
    def matrix_order(M, max_n=12):
        acc = np.eye(4, dtype=int)
        for n in range(1, max_n + 1):
            acc = acc @ M
            if np.array_equal(acc, I4):
                return n
        return None

    orders = {name: matrix_order(g) for name, g in elements.items()}

    return {
        'group': 'S_3',
        'order': 6,
        'num_elements': len(elements),
        'all_distinct': all_distinct,
        'all_preserve_cartan': all_preserve_cartan,
        'tau_preserves_cartan': tau_preserves,
        'tau_order_2': tau_order_2,
        'element_orders': orders,
        'generators': ['sigma (order 3)', 'tau (order 2)'],
        'presentation': '<sigma, tau | sigma^3 = tau^2 = (sigma*tau)^2 = e>',
    }


# =========================================================================
# 4. The Yang R-matrix on 8 x 8
# =========================================================================

def d4_yang_r_matrix(u: float) -> np.ndarray:
    """Yang R-matrix R(u) = u * Id_{64} + P on C^8 tensor C^8.

    This is the 64x64 R-matrix for the vector representation of so_8.
    The SAME R-matrix structure applies to 8_s and 8_c by triality
    covariance: (sigma x sigma) R_{VV}(u) = R_{SS}(u) (sigma x sigma).

    Parameters
    ----------
    u : float
        Spectral parameter.

    Returns
    -------
    np.ndarray
        64x64 matrix R(u).
    """
    return yang_r_matrix_NxN(u, D4_DIM_V)


def d4_r_matrix_nonzero_count(u: float = 1.0) -> Dict[str, Any]:
    """Count nonzero entries in the 64x64 D_4 Yang R-matrix.

    R(u) = u * Id_{64} + P.

    Nonzero structure:
    - Id_{64}: 64 diagonal entries
    - P: 64 entries at positions ((i,a),(a,i)) for 0 <= i,a <= 7
    - Overlap: P_{(i,i),(i,i)} = 1 = Id_{(i,i),(i,i)} for the 8 diagonal entries
      where the tensor index pair (i,a) has i=a.
    - At u != 0, u != -1: entries from both Id and P are nonzero.
      Union of supports: 64 + 64 - 8 = 120.
    - At u = 0: R = P, so 64 nonzero entries.
    - At u = -1: entries with both Id and P overlap: R_{(i,i),(i,i)} = -1 + 1 = 0,
      so we LOSE the 8 overlap entries: 120 - 8 = 112 nonzero.

    For the FULL K3 R-matrix at charge 1 (24x24 tensor 24x24 = 576x576):
    - D_4 block: 8x8 tensor 8x8 = 64x64, with 120 nonzero at generic u
    - Abelian block: 20x20 diagonal R-matrix = 20 nonzero entries
    - Cross blocks: 0 (Mukai orthogonality)
    - Total in K3 R-matrix: 120 + 20 = 140 nonzero out of 576^2 = 331776.
    """
    R = d4_yang_r_matrix(u)
    d = D4_DIM_V * D4_DIM_V  # = 64

    # Count nonzero entries
    nonzero = np.count_nonzero(R)

    # Decompose: count Id entries, P entries, overlap
    Id_entries = d  # always 64
    P = yang_r_matrix_NxN(0.0, D4_DIM_V)
    P_nonzero = np.count_nonzero(P)

    # Overlap: positions where both Id and P are nonzero
    Id_mask = np.eye(d, dtype=bool)
    P_mask = np.abs(P) > 1e-15
    overlap = int(np.sum(Id_mask & P_mask))

    # Verify union formula
    expected_union = Id_entries + P_nonzero - overlap

    # For the full K3 at charge 1
    abelian_nonzero = COMPLEMENT_RANK  # 20 diagonal entries
    cross_nonzero = 0  # orthogonality
    total_k3 = nonzero + abelian_nonzero + cross_nonzero
    total_k3_size = (MUKAI_RANK ** 2) ** 2  # 576^2 = 331776

    return {
        'd4_r_matrix_size': f'{d}x{d}',
        'u': u,
        'nonzero_entries': nonzero,
        'total_entries': d * d,
        'sparsity': 1.0 - nonzero / (d * d),
        'id_support': Id_entries,
        'P_support': P_nonzero,
        'overlap': overlap,
        'expected_by_union': expected_union,
        'matches_union': nonzero == expected_union,
        'k3_charge1_d4_sector': nonzero,
        'k3_charge1_abelian_sector': abelian_nonzero,
        'k3_charge1_cross_sector': cross_nonzero,
        'k3_charge1_total_nonzero': total_k3,
        'k3_charge1_total_entries': total_k3_size,
    }


def d4_r_matrix_triality_covariance(u: float = 3.7) -> Dict[str, Any]:
    r"""Verify triality covariance of the Yang R-matrix.

    The Yang R-matrix R(u) = u*Id + P on C^N x C^N is UNIVERSAL: it does
    not depend on which 8-dimensional representation we use.  This is
    because the permutation operator P acts the same way on any C^8 x C^8.

    Therefore: (sigma x sigma) R(u) (sigma^{-1} x sigma^{-1}) = R(u)
    is AUTOMATIC for the Yang R-matrix (it commutes with any permutation
    of basis vectors).

    This is a WEAKER form of triality covariance: the Yang R-matrix is
    the UNIVERSAL (representation-independent) R-matrix.  The representation-
    DEPENDENT corrections (at higher orders in 1/u) would break this
    universality, but at level 1, the Yang R-matrix suffices.

    More precisely: for the Yangian at level 1, the evaluation R-matrix
    on V(omega_i) x V(omega_i) depends on the representation through the
    Casimir eigenvalue, which is the SAME for all three 8-dimensional
    representations (triality maps them to each other, preserving
    the Casimir).
    """
    R = d4_yang_r_matrix(u)
    d = D4_DIM_V * D4_DIM_V

    # The sigma on C^8 is a permutation of the basis.
    # For triality covariance, we need sigma_V on C^8 (vector) and
    # sigma_S on C^8 (spinor) such that
    # (sigma_S x sigma_S) R_{VV}(u) = R_{SS}(u) (sigma_S x sigma_S).
    #
    # But since R_{VV}(u) = R_{SS}(u) = u*Id+P for the Yang R-matrix,
    # this is trivially satisfied: R(u) commutes with (A x A) for any A.
    #
    # Check: [R(u), A tensor A] = 0 for any 8x8 matrix A?
    # R = u*Id + P. [u*Id, AoA] = 0. [P, AoA] = 0 iff AoA commutes with P.
    # P(v ot w) = w ot v. AoA(v ot w) = Av ot Aw.
    # P AoA (v ot w) = P(Av ot Aw) = Aw ot Av.
    # AoA P (v ot w) = AoA(w ot v) = Aw ot Av.
    # So [P, AoA] = 0 for ANY A. The Yang R-matrix is universal.

    # Numerical verification with a random A
    rng = np.random.RandomState(42)
    A = rng.randn(D4_DIM_V, D4_DIM_V)
    AoA = np.kron(A, A)
    commutator = R @ AoA - AoA @ R
    max_comm = float(np.max(np.abs(commutator)))

    # Also check unitarity
    R_neg = d4_yang_r_matrix(-u)
    product = R @ R_neg
    expected = (1.0 - u * u) * np.eye(d)
    unitarity_dev = float(np.max(np.abs(product - expected)))

    # YBE check (partial): R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
    # This requires 8^3 = 512 dimensional space; compute for consistency
    v = 2.3  # different from u, AP-CY28 safe
    N = D4_DIM_V
    d3 = N * N * N

    # R_{12}: acts on spaces 1,2 (tensor with Id on space 3)
    R12 = np.kron(yang_r_matrix_NxN(u - v, N), np.eye(N))
    # R_{13}: acts on spaces 1,3 (tensor with Id on space 2)
    # R_{13}_{(iab),(jcd)} = R_{(ia),(jc)} * delta_{bd}
    R13_base = yang_r_matrix_NxN(u, N)
    R13 = np.zeros((d3, d3))
    for i in range(N):
        for a in range(N):
            for b in range(N):
                row = i * N * N + a * N + b
                for j in range(N):
                    for c in range(N):
                        col = j * N * N + c * N + b
                        R13[row, col] += R13_base[i * N + a, j * N + c]
    # R_{23}: acts on spaces 2,3 (tensor with Id on space 1)
    R23 = np.kron(np.eye(N), yang_r_matrix_NxN(v, N))

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    ybe_dev = float(np.max(np.abs(lhs - rhs)))

    return {
        'u': u,
        'triality_covariance': True,
        'reason': (
            'Yang R-matrix R(u) = u*Id + P commutes with A tensor A '
            'for ANY matrix A. This is because [P, A tensor A] = 0 '
            'is an identity (P swaps tensor factors, A tensor A acts '
            'on each factor independently). Therefore triality covariance '
            'is AUTOMATIC and does not constrain the R-matrix.'
        ),
        'universal_commutativity_deviation': max_comm,
        'universal_commutativity_holds': max_comm < 1e-10,
        'unitarity_deviation': unitarity_dev,
        'unitarity_holds': unitarity_dev < 1e-10,
        'ybe_deviation': ybe_dev,
        'ybe_holds': ybe_dev < 1e-10,
    }


# =========================================================================
# 5. K3 embedding at D_4 enhancement
# =========================================================================

def d4_k3_embedding_parameters(
    epsilon: float = 1.0,
) -> Dict[str, Any]:
    """K3 Yangian parameters at the D_4 enhancement point.

    At the D_4 singularity on K3:
    - 4 Mukai directions merge into the D_4 root lattice (rank 4)
    - 20 remaining directions are abelian (Heisenberg complement)
    - Total: 4 + 20 = 24 = Mukai rank

    The D_4 sector parameters h_1,...,h_4 are constrained by:
    (a) The D_4 Cartan matrix: <alpha_i, alpha_j> = C_{ij}
    (b) The CY_2 constraint: sum_{i=1}^{24} h_i = 0

    Parametrization:
    - h_D4 = epsilon * (vector rep weights projected to Cartan)
    - h_ab chosen to satisfy CY_2

    Central charge: c(so_8, k=1) + c_Heis(20) = 4 + 20 = 24.
    """
    data = ade_data('D4')
    embedding = ADEMukaiEmbedding(data)
    decomp = embedding.mukai_decomposition()

    # D_4 Cartan sector: 4 parameters
    # Use the weights centered and satisfying sum = 0
    h_d4 = [epsilon * (4 + 1 - 2 * k) / 4.0 for k in range(1, 5)]
    # h_d4 = [3/4, 1/4, -1/4, -3/4] * epsilon
    # sum = 0. Check.

    # Abelian complement: 20 parameters with sum = 0
    h_ab = [epsilon * 0.05] * 10 + [-epsilon * 0.05] * 10
    # sum = 0. Check.

    h_all = h_d4 + h_ab
    cy2_sum = sum(h_all)

    return {
        'epsilon': epsilon,
        'h_d4': h_d4,
        'h_abelian': h_ab[:5],  # first 5 for display
        'num_d4': len(h_d4),
        'num_abelian': len(h_ab),
        'total': len(h_all),
        'cy2_sum': cy2_sum,
        'cy2_satisfied': abs(cy2_sum) < 1e-15,
        'c_d4_level1': float(D4_LEVEL1_CC),
        'c_heisenberg': float(COMPLEMENT_RANK),
        'c_total': float(D4_LEVEL1_CC + COMPLEMENT_RANK),
        'mukai_decomposition': decomp,
    }


def d4_structure_function_factored(z: float, epsilon: float = 1.0) -> Dict[str, Any]:
    """Factored structure function g_{K3}(z) at the D_4 enhancement.

    g_{K3}(z) = g_{D_4}(z) * g_{compl}(z)

    where:
      g_{D_4}(z) = prod_{i=1}^{4} (z - h_i)/(z + h_i)  (D_4 sector)
      g_{compl}(z) = prod_{j=5}^{24} (z - h_j)/(z + h_j)  (complement)

    AP-CY28: z must avoid +/- h_i for all i.
    """
    params = d4_k3_embedding_parameters(epsilon)
    h_d4 = params['h_d4']
    # Reconstruct full abelian sector
    h_ab = [epsilon * 0.05] * 10 + [-epsilon * 0.05] * 10

    # Check poles (AP-CY28)
    all_h = h_d4 + h_ab
    for h in all_h:
        if abs(z + h) < 1e-15:
            raise ValueError(f"Pole at z={z}: z + h = 0 for h = {h}")
        if abs(z - h) < 1e-15:
            raise ValueError(f"Zero at z={z}: z - h = 0 for h = {h}")

    # D_4 sector
    g_d4 = 1.0
    for h in h_d4:
        g_d4 *= (z - h) / (z + h)

    # Abelian sector
    g_ab = 1.0
    for h in h_ab:
        g_ab *= (z - h) / (z + h)

    g_total = g_d4 * g_ab

    # Unitarity: g(z) * g(-z) = 1
    g_neg_d4 = 1.0
    for h in h_d4:
        g_neg_d4 *= (-z - h) / (-z + h)
    g_neg_ab = 1.0
    for h in h_ab:
        g_neg_ab *= (-z - h) / (-z + h)
    g_neg_total = g_neg_d4 * g_neg_ab

    unitarity_product = g_total * g_neg_total

    return {
        'z': z,
        'g_d4': g_d4,
        'g_complement': g_ab,
        'g_total': g_total,
        'factored': abs(g_d4 * g_ab - g_total) < 1e-15,
        'unitarity_product': unitarity_product,
        'unitarity_holds': abs(unitarity_product - 1.0) < 1e-10,
        'g_d4_degree': (4, 4),
        'g_complement_degree': (20, 20),
        'g_total_degree': (24, 24),
    }


# =========================================================================
# 6. Off-diagonal R-matrix analysis
# =========================================================================

def d4_offdiagonal_rmatrix() -> Dict[str, Any]:
    r"""Analysis of off-diagonal entries in the D_4 R-matrix.

    For the ABELIAN K3 Yangian (generic point), the 24x24 charge-1 R-matrix
    is DIAGONAL: R(z) = diag((z-h_1)/(z+h_1), ..., (z-h_{24})/(z+h_{24})).

    At the D_4 enhancement point, the R-matrix acquires OFF-DIAGONAL entries
    in the 8x8 D_4 block.  The abelian complement stays diagonal.

    For the Yang R-matrix R(u) = u*Id_{64} + P on C^8 x C^8:
    - Diagonal entries: R_{(i,a),(i,a)} = u + delta_{ia} (from u*Id + P)
    - Off-diagonal entries: R_{(i,a),(j,b)} with (i,a) != (j,b)
      From P: P_{(i,a),(a,i)} = 1 for all (i,a). These are off-diagonal
      when i != a: R_{(i,a),(a,i)} = 1 (from P) + u*delta_{ia}*delta_{ai}
      Wait, (i,a) != (a,i) iff i != a.
      So off-diagonal entries from P: {((i,a),(a,i)) : i != a}.
      Number: N^2 - N = 64 - 8 = 56.

    At generic u != 0:
    - 8 diagonal entries where i=a: R_{(i,i),(i,i)} = u + 1
    - 56 diagonal entries where i!=a: R_{(i,a),(i,a)} = u
    - 56 off-diagonal entries from P: R_{(i,a),(a,i)} = 1 for i != a
    Total nonzero: 64 + 56 = 120.

    For the FULL K3 charge-1 R-matrix (576 x 576):
    The 8x8 D_4 sector contributes the 64x64 Yang R-matrix block.
    The 20x20 abelian sector contributes 20 diagonal entries.
    Cross-sector: 0 entries (Mukai orthogonality).

    Nonzero entries: 120 (D_4 block) + 20 (abelian diagonal) = 140.
    Total entries: 576^2 = 331776.
    Off-diagonal nonzero in D_4 block: 56.
    """
    N = D4_DIM_V
    d = N * N  # = 64

    # Count off-diagonal entries in the D_4 R-matrix
    off_diag_from_P = N * (N - 1)  # = 56: entries (i,a) -> (a,i) with i != a

    # These become entries in the D_4 sector of the K3 R-matrix.
    # In the K3 R-matrix, these are at positions (i,a), (a,i) within
    # the D_4 block, hence they represent genuine non-abelian coupling.

    # The 576x576 K3 R-matrix at charge 1:
    K3_d = MUKAI_RANK * MUKAI_RANK  # = 576

    # D_4 block
    d4_diag = d       # 64 diagonal entries
    d4_offdiag = off_diag_from_P  # 56 off-diagonal
    d4_total_nz = d4_diag + d4_offdiag  # 120

    # Abelian block: 20x20 diagonal = 20 entries
    ab_diag = COMPLEMENT_RANK
    ab_offdiag = 0
    ab_total_nz = ab_diag

    # Cross-sector: 0 (orthogonality)
    cross_nz = 0

    # Full K3 R-matrix
    k3_total_nz = d4_total_nz + ab_total_nz + cross_nz
    k3_total_entries = K3_d * K3_d

    # Fraction of entries that are nonzero
    k3_density = k3_total_nz / k3_total_entries

    # The 56 off-diagonal entries are the SIGNATURE of non-abelian enhancement.
    # At the generic (abelian) point, these 56 entries are all zero.
    # At D_4 enhancement, they "turn on" and encode the so_8 structure.

    return {
        'd4_sector': {
            'block_size': f'{d}x{d} = {d*d} entries',
            'diagonal_nonzero': d4_diag,
            'offdiagonal_nonzero': d4_offdiag,
            'total_nonzero': d4_total_nz,
            'offdiag_fraction': d4_offdiag / (d * d),
        },
        'abelian_sector': {
            'block_size': f'{COMPLEMENT_RANK**2}x{COMPLEMENT_RANK**2}',
            'diagonal_nonzero': ab_diag,
            'offdiagonal_nonzero': ab_offdiag,
            'total_nonzero': ab_total_nz,
        },
        'cross_sector': {
            'nonzero': cross_nz,
            'reason': 'Mukai orthogonality: omega^{ab} = 0',
        },
        'k3_charge1_rmatrix': {
            'size': f'{K3_d}x{K3_d} = {k3_total_entries} entries',
            'total_nonzero': k3_total_nz,
            'density': k3_density,
            'sparsity': 1.0 - k3_density,
            'offdiagonal_from_d4': d4_offdiag,
        },
        'interpretation': (
            f'The D_4 enhancement turns on {d4_offdiag} off-diagonal entries '
            f'in the K3 R-matrix (from the permutation operator P in the Yang '
            f'R-matrix). At the generic abelian point, the K3 R-matrix has 0 '
            f'off-diagonal entries. The {d4_offdiag} new entries encode the '
            f'so_8 non-abelian structure.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 7. Triality vs Miki (AP-CY22)
# =========================================================================

def triality_vs_miki() -> Dict[str, Any]:
    r"""Analysis of D_4 triality vs Miki automorphism (AP-CY22).

    AP-CY22 states: Miki automorphism is algebra-specific (quantum toroidal
    gl_1), NOT operadic.  It comes from the Weyl group of the CY torus,
    not from the E_3 operad.

    D_4 triality S_3 is DIFFERENT:
    - Source: outer automorphism of the D_4 Dynkin diagram
    - Action: permutes the three 8-dim representations
    - Scope: acts on Y(so_8), not on all of Y(g_{K3})

    Comparison:

    | Property | Miki S_3 | D_4 triality S_3 |
    |----------|----------|-------------------|
    | Source | CY torus Weyl group | Dynkin diagram Out(D_4) |
    | Acts on | quantum toroidal gl_1 | Y(so_8) subalgebra |
    | Parameters | (q_1,q_2,q_3) with product=1 | (omega_1,omega_3,omega_4) |
    | Scope | full algebra | D_4 sector only |
    | E_3 origin | NO (AP-CY22) | NO |
    | CY dependence | CY_3 (q_1q_2q_3=1) | CY_2 (K3 lattice) |

    CONJECTURE (conj:combined-s3, AP-CY14):
    At the D_4 enhancement point of a CY_3 containing K3 (e.g. K3 x E),
    the Miki S_3 (from the CY_3 torus) and the triality S_3 (from D_4)
    may combine into a LARGER symmetry group acting on the full Yangian.
    This is OPEN and CONJECTURAL.
    """
    return {
        'miki_s3': {
            'source': 'CY torus Weyl group',
            'acts_on': 'quantum toroidal gl_1 (U_{q,t}(gl_hat_hat_1))',
            'parameters': '(q_1, q_2, q_3) with q_1*q_2*q_3 = 1',
            'scope': 'full algebra',
            'e3_origin': False,
            'cy_dimension': 3,
        },
        'd4_triality_s3': {
            'source': 'Dynkin diagram outer automorphism Out(D_4)',
            'acts_on': 'Y(so_8) subalgebra of Y(g_{K3})',
            'parameters': '(omega_1, omega_3, omega_4) fundamental weights',
            'scope': 'D_4 sector only (4 of 24 Mukai directions)',
            'e3_origin': False,
            'cy_dimension': 2,
        },
        'are_same': False,
        'why_different': (
            'Miki S_3 permutes the CY_3 torus directions (q_1,q_2,q_3); '
            'D_4 triality S_3 permutes the three 8-dim reps of so_8. '
            'They act on different sectors and have different origins. '
            'Miki requires CY_3 (q_1*q_2*q_3=1); triality requires only '
            'the D_4 Dynkin diagram (CY_2 for the K3 embedding).'
        ),
        'combined_symmetry': {
            'status': 'CONJECTURAL (AP-CY14)',
            'statement': (
                'At a D_4 enhancement of K3 x E (a CY_3), both S_3 groups '
                'act simultaneously: Miki on the toroidal sector, triality '
                'on the D_4 sector. Whether they extend to a common S_3 '
                'or combine into S_3 x S_3 is an open question.'
            ),
        },
        'ap_cy22_compliance': (
            'AP-CY22: neither S_3 derives from the E_3 operad. '
            'Both are algebra-specific symmetries.'
        ),
    }


# =========================================================================
# 8. D_4 Serre relations in the K3 context
# =========================================================================

def d4_serre_in_k3() -> Dict[str, Any]:
    """D_4 Serre relations within the K3 Yangian.

    The D_4 Cartan matrix:
        C = [[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]]

    Serre relations come from edges in the Dynkin diagram:
    - (0,1): C_{01} = -1, Serre degree = 2
    - (1,2): C_{12} = -1, Serre degree = 2
    - (1,3): C_{13} = -1, Serre degree = 2

    All three are adjacent to the branching node 1.
    The three Serre relations are PERMUTED by triality:
      sigma: Serre(0,1) -> Serre(2,1) -> Serre(3,1) -> Serre(0,1)

    Mixing Serre: TRIVIAL (I_mix = 0) by Mukai orthogonality.
    This follows from the I_ADE + I_ab decomposition (k3_serre_relations.py).
    """
    C = d4_cartan_matrix()

    # Find all edges (Serre pairs)
    serre_pairs = []
    for i in range(D4_RANK):
        for j in range(i + 1, D4_RANK):
            if C[i, j] == -1:
                serre_pairs.append((i, j))

    # Verify: all three pairs involve the branching node
    all_involve_branching = all(BRANCHING_NODE in pair for pair in serre_pairs)

    # The Serre relation for adjacent simply-laced nodes:
    # E_i^2 E_j - [2]_q E_i E_j E_i + E_j E_i^2 = 0
    # (quantum Serre at q = 1 for the classical Yangian limit)

    # Triality permutation of Serre relations
    P = triality_permutation_matrix()
    # sigma: 0->2, 2->3, 3->0, 1->1
    # Serre(0,1) -> Serre(2,1), Serre(1,2) -> Serre(1,3), Serre(1,3) -> Serre(1,0)
    serre_cycle_holds = True
    for (i, j) in serre_pairs:
        # Apply sigma to (i, j)
        sigma_i = int(np.argmax(P[:, i]))
        sigma_j = int(np.argmax(P[:, j]))
        mapped = tuple(sorted((sigma_i, sigma_j)))
        if mapped not in [(min(p), max(p)) for p in serre_pairs]:
            serre_cycle_holds = False

    return {
        'num_serre_pairs': len(serre_pairs),
        'serre_pairs': serre_pairs,
        'expected_num_edges': D4_RANK - 1,  # = 3
        'correct_num_edges': len(serre_pairs) == D4_RANK - 1,
        'all_involve_branching': all_involve_branching,
        'serre_relation_form': (
            'E_i^2 E_j - [2]_q E_i E_j E_i + E_j E_i^2 = 0 '
            '(simply-laced quantum Serre, degree 1 - C_{ij} = 2)'
        ),
        'triality_permutes_serre': serre_cycle_holds,
        'mixing_serre_trivial': True,
        'mixing_reason': 'Mukai orthogonality: I_ADE + I_ab, no I_mix',
        'status': STATUS,
    }


# =========================================================================
# 9. Full summary
# =========================================================================

def d4_triality_summary() -> Dict[str, Any]:
    """Complete summary of the K3 Yangian at the D_4 enhancement point.

    This is the main entry point for the D_4 triality analysis.

    STATUS: CONJECTURAL (AP-CY14).  The numerical data (Lie algebra,
    R-matrix, triality) are mathematical facts about Y(so_8).  The
    K3 embedding is conditional on CY-A_2 (proved at d=2).
    """
    root_sys = verify_d4_root_system()
    three_reps = verify_three_reps()
    triality_aut = verify_triality_automorphism()
    s3_group = full_s3_group()
    rep_data = triality_on_representations()
    r_matrix = d4_r_matrix_nonzero_count()
    offdiag = d4_offdiagonal_rmatrix()
    serre = d4_serre_in_k3()
    miki = triality_vs_miki()

    return {
        'algebra': {
            'type': 'D_4 = so_8',
            'rank': D4_RANK,
            'dim_g': D4_DIM_G,
            'dim_V': D4_DIM_V,
            'dual_coxeter': D4_DUAL_COXETER,
            'c_level1': str(D4_LEVEL1_CC),
            'num_positive_roots': D4_NUM_POS_ROOTS,
        },
        'root_system_ok': root_sys['cartan_matrix_matches'] and root_sys['dim_correct'],
        'three_reps_ok': three_reps['all_dim_8'] and three_reps['all_distinct'],
        'triality': {
            'group': 'S_3 = Out(D_4)',
            'order': 6,
            'genuine_order_3': triality_aut['genuine_order_3'],
            'preserves_cartan': triality_aut['preserves_cartan'],
            'permutes_reps': rep_data['triality_cycle']['full_cycle'],
            'permutes_serre': serre['triality_permutes_serre'],
        },
        'r_matrix': {
            'type': 'Yang R(u) = u*Id + P on C^8 x C^8',
            'size': '64x64',
            'nonzero_entries': r_matrix['nonzero_entries'],
            'offdiagonal_d4': offdiag['d4_sector']['offdiagonal_nonzero'],
            'triality_covariant': True,
        },
        'k3_embedding': {
            'd4_rank': D4_RANK,
            'complement_rank': COMPLEMENT_RANK,
            'total': MUKAI_RANK,
            'c_total': str(D4_LEVEL1_CC + F(COMPLEMENT_RANK)),
            'mixing_serre_trivial': True,
        },
        'triality_vs_miki': {
            'are_same': False,
            'miki_source': 'CY torus',
            'triality_source': 'Dynkin Out(D_4)',
        },
        'status': STATUS,
    }
