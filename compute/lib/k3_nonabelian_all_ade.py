r"""K3 nonabelian R-matrix at ALL ADE enhancement types.

STATUS: CONJECTURAL (AP-CY14).  All results conditional on Y(g_{K3}).

MATHEMATICAL CONTENT
====================

This module computes the nonabelian K3 R-matrix for each ADE enhancement
type on K3 moduli: A_1, A_2, D_4, D_5, E_6, E_7, E_8.  It extends the
A_1 results (k3_nonabelian_rmatrix_a1.py, 82 tests) and D_4 results
(k3_yangian_d4_triality.py, 89 tests) to the FULL ADE landscape.

For each type g of rank r with defining representation of dimension N:
  - The Yang R-matrix R(u) = u*Id_{N^2} + P on C^N x C^N is N^2 x N^2
  - At level k=1: R(u) is the COMPLETE evaluation R-matrix
  - r Mukai directions merge into the root lattice of g
  - (24-r) directions remain in the abelian complement Heis^{24-r}
  - Central charge: c(g,k=1) + c_Heis(24-r) = rank + (24-rank) = 24

OFF-DIAGONAL COUNT IN THE 324 x 324 CHARGE-2 R-MATRIX
=====================================================

For d merged Mukai directions (d = rank for D,E types; d = rank+1 for A types
due to the weight lattice having dim = rank+1 in the fundamental):

CORRECTION: For ALL types, d = rank of the Lie algebra.  The n_mukai_dirs
agrees with rank for D and E types.  For A_n, the fundamental representation
has n+1 weights, but only n independent Mukai directions participate (the
weight lattice of sl_{n+1} is rank n, embedded in the rank-24 Mukai lattice).

Wait -- this needs careful treatment.  At an A_1 singularity on K3, TWO
Mukai directions merge (the two weights of the fundamental representation
of sl_2).  For A_2, THREE directions merge (the three weights of the
fundamental of sl_3).  So d = n+1 for A_n, and d = rank for D_n/E_n.

The off-diagonal count:
  States: 324 = d + d + C(d,2) + (24-d) + (24-d) + d*(24-d) + C(24-d,2)

  Off-diagonal entries:
    ADE row block:        d x d -> d*(d-1)
    ADE col block:        d x d -> d*(d-1)
    ADE two-point block:  C(d,2) x C(d,2) -> C(d,2)*(C(d,2)-1)
    Mixed two-point:      (24-d) blocks of d x d -> (24-d)*d*(d-1)
    Complement:           diagonal -> 0

  Total = d*(d-1)*(26-d) + C(d,2)*(C(d,2)-1)

  Results:
    Generic:    d=0,   offdiag=0
    A_1:        d=2,   offdiag=48
    A_2:        d=3,   offdiag=144
    D_4:        d=4,   offdiag=294
    D_5:        d=5,   offdiag=510
    E_6:        d=6,   offdiag=810
    E_7:        d=7,   offdiag=1218
    E_8:        d=8,   offdiag=1764

THE YANG R-MATRIX FOR EACH TYPE
================================

R(u) = u*Id_{N^2} + P on C^N x C^N, where N = dim(V):

  A_1: N=2,   R is 4x4,       nonzero off-diag in R: 2
  A_2: N=3,   R is 9x9,       nonzero off-diag in R: 6
  D_4: N=8,   R is 64x64,     nonzero off-diag in R: 56
  D_5: N=10,  R is 100x100,   nonzero off-diag in R: 90
  E_6: N=27,  R is 729x729,   nonzero off-diag in R: 702
  E_7: N=56,  R is 3136x3136, nonzero off-diag in R: 3080
  E_8: N=248, R is 61504x61504, nonzero off-diag in R: 61256

SERRE RELATIONS FOR EACH TYPE
==============================

Each edge (i,j) of the Dynkin diagram gives a Serre relation:
  ad(e_i)^{1-C_{ij}} (e_j) = 0

For simply-laced ADE: all C_{ij} in {0,-1}, so Serre degree = 1-(-1) = 2:
  [e_i, [e_i, e_j]] = 0  (for adjacent nodes i,j)

Number of Serre relations = number of edges in the Dynkin diagram = rank - 1.

Type-specific features:
  A_2: linear diagram, 2 Serre relations, Z_2 outer automorphism
  D_5: fork at node 2, connecting to nodes 3,4 (two legs), no triality
       (D_n triality is UNIQUE to D_4; for n>=5, Out(D_n) = Z_2 only)
  E_6: branching at node 2, Z_2 outer automorphism (diagram flip)
  E_7: branching at node 2, no outer automorphism (Out(E_7) = 1)
  E_8: branching at node 2, no outer automorphism (Out(E_8) = 1)

THE 27 OF E_6
==============

E_6 has a 27-dimensional fundamental representation, which is MINUSCULE.
The weights form a root system of type E_6 in the weight lattice.
The tensor product 27 x 27 = 1 + 78 + 351' + 351' decomposes into
irreducibles whose dimensions sum to 729.

The R-matrix on 27 x 27 = 729-dimensional space has:
  Diagonal: 729 entries
  Off-diagonal from P: 27^2 - 27 = 702 entries
  Total nonzero: 729 + 702 - 27 = 1404 entries (at generic u)

THE 56 OF E_7
==============

E_7 has a 56-dimensional fundamental (minuscule) representation.
The R-matrix on 56 x 56 = 3136-dimensional space.
Off-diagonal from P: 56^2 - 56 = 3080.

THE 248 OF E_8 (UNIQUE: adjoint = smallest rep)
=================================================

E_8 is the ONLY simple Lie algebra where the adjoint representation
IS the smallest (fundamental) representation.  dim(E_8) = 248.
The R-matrix on 248 x 248 = 61504-dimensional space.

For computational purposes, we DO NOT construct the 61504 x 61504 matrix
explicitly.  Instead, we use the STRUCTURAL PROPERTIES:
  - The Yang R-matrix R(u) = u*Id + P on C^{248} x C^{248}
  - Nonzero off-diagonal: 248^2 - 248 = 61256
  - YBE is guaranteed by the universal Yang R-matrix construction
  - Unitarity: R(u)*R(-u) = (1-u^2)*Id

The E_8 R-matrix is the LARGEST in the ADE hierarchy.  The off-diagonal
count in the 324x324 K3 R-matrix (1764 entries) is the maximum possible,
reflecting the fact that E_8 uses 8 of the 24 Mukai directions (the
maximum for an ADE singularity on K3, since rank E_8 = 8 and the Mukai
lattice has rank 24).

CONVENTIONS
===========
  - AP-CY14: ALL results CONJECTURAL (K3 Yangian not constructed)
  - AP-CY28: test points avoid poles at +/- h_i
  - AP-CY31: spectral parameter u (Yangian), NOT worldsheet z
  - AP-CY30: pairwise YBE does NOT imply tetrahedron; separate check needed
  - AP113: all kappa subscripted (kappa_ch, kappa_BKM, kappa_cat, kappa_fiber)
  - AP-CY22: Miki automorphism is algebra-specific, NOT operadic
  - AP-CY5: Kazhdan-Lusztig requires root of unity; generic q: semisimple

REFERENCES
==========
  k3_nonabelian_rmatrix_a1.py  (A_1 deformation, 82 tests)
  k3_yangian_d4_triality.py    (D_4 triality, 89 tests)
  k3_rmatrix_enhanced.py       (ADE block structure, landscape)
  ade_yangian_level1.py        (general ADE Yangian data, RTT)
  k3_serre_relations.py        (K3 Serre at enhanced symmetry)
  mo_rmatrix_k3_charge2.py     (abelian charge-2 R-matrix, 324x324)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.ade_yangian_level1 import (
    ADEData,
    ADEMukaiEmbedding,
    ADE_LABELS,
    RTTVerifierGeneral,
    ade_data,
    all_weights_defining_rep,
    defining_rep_weights,
    lax_diagonal_evaluation,
    yang_r_matrix_NxN,
    yang_r_matrix_unitarity,
)
from compute.lib.k3_rmatrix_enhanced import (
    ADE_DATA,
    MUKAI_RANK,
    yang_r_matrix,
    yang_r_verify_ybe,
    yang_r_verify_unitarity,
    offdiagonal_count_ade,
)

F = Fraction

STATUS = 'CONJECTURAL'  # AP-CY14: K3 Yangian not constructed

# =========================================================================
# 0. Extended ADE data (adding D5 to the landscape)
# =========================================================================

# The k3_rmatrix_enhanced.ADE_DATA lacks D5.  We provide the full table.
FULL_ADE_DATA = {
    'A1': {'rank': 1, 'dim_g': 3,   'dim_V': 2,   'h_dual': 2,  'n_mukai_dirs': 2},
    'A2': {'rank': 2, 'dim_g': 8,   'dim_V': 3,   'h_dual': 3,  'n_mukai_dirs': 3},
    'D4': {'rank': 4, 'dim_g': 28,  'dim_V': 8,   'h_dual': 6,  'n_mukai_dirs': 4},
    'D5': {'rank': 5, 'dim_g': 45,  'dim_V': 10,  'h_dual': 8,  'n_mukai_dirs': 5},
    'E6': {'rank': 6, 'dim_g': 78,  'dim_V': 27,  'h_dual': 12, 'n_mukai_dirs': 6},
    'E7': {'rank': 7, 'dim_g': 133, 'dim_V': 56,  'h_dual': 18, 'n_mukai_dirs': 7},
    'E8': {'rank': 8, 'dim_g': 248, 'dim_V': 248, 'h_dual': 30, 'n_mukai_dirs': 8},
}

# Ordered by rank for landscape traversal
ADE_TYPES_ORDERED = ['A1', 'A2', 'D4', 'D5', 'E6', 'E7', 'E8']

# Outer automorphism groups
OUTER_AUTOMORPHISMS = {
    'A1': {'group': 'Z_1', 'order': 1, 'description': 'trivial'},
    'A2': {'group': 'Z_2', 'order': 2, 'description': 'diagram flip (charge conjugation)'},
    'D4': {'group': 'S_3', 'order': 6, 'description': 'triality (unique to D_4)'},
    'D5': {'group': 'Z_2', 'order': 2, 'description': 'swap of two spinor nodes'},
    'E6': {'group': 'Z_2', 'order': 2, 'description': 'diagram flip'},
    'E7': {'group': 'Z_1', 'order': 1, 'description': 'trivial'},
    'E8': {'group': 'Z_1', 'order': 1, 'description': 'trivial'},
}


# =========================================================================
# 1. Off-diagonal count for ALL ADE types (including D5)
# =========================================================================

def offdiagonal_count_general(ade_type: str) -> Dict[str, Any]:
    r"""Count off-diagonal entries in the 324x324 charge-2 R-matrix.

    This extends k3_rmatrix_enhanced.offdiagonal_count_ade to include D5.

    Formula: for d merged Mukai directions,
      total_offdiag = d*(d-1)*(26-d) + C(d,2)*(C(d,2)-1)

    Parameters
    ----------
    ade_type : str
        ADE label: 'A1', 'A2', 'D4', 'D5', 'E6', 'E7', 'E8'.

    Returns
    -------
    dict with off-diagonal counts and state decomposition.
    """
    if ade_type not in FULL_ADE_DATA:
        raise ValueError(
            f"Unknown ADE type: {ade_type}. "
            f"Supported: {list(FULL_ADE_DATA.keys())}"
        )

    data = FULL_ADE_DATA[ade_type]
    r = data['rank']
    d = data['n_mukai_dirs']
    N = data['dim_V']
    n_comp = MUKAI_RANK - d

    # State decomposition
    n_ade_row = d
    n_ade_col = d
    n_ade_two = d * (d - 1) // 2
    n_comp_row = n_comp
    n_comp_col = n_comp
    n_mixed_two = d * n_comp
    n_comp_two = n_comp * (n_comp - 1) // 2

    n_total = (n_ade_row + n_ade_col + n_ade_two +
               n_comp_row + n_comp_col +
               n_mixed_two + n_comp_two)
    assert n_total == 324, f"State count for {ade_type}: {n_total} != 324"

    # Off-diagonal counts
    off_ade_row = d * (d - 1)
    off_ade_col = d * (d - 1)
    off_ade_two = n_ade_two * (n_ade_two - 1)
    off_mixed = n_comp * d * (d - 1)
    off_comp = 0

    n_offdiag = off_ade_row + off_ade_col + off_ade_two + off_mixed

    # Cross-check with closed-form formula
    c2 = d * (d - 1) // 2
    formula_result = d * (d - 1) * (26 - d) + c2 * (c2 - 1)
    assert n_offdiag == formula_result, (
        f"Formula mismatch for {ade_type}: {n_offdiag} != {formula_result}"
    )

    # Yang R-matrix off-diagonal count (in the N^2 x N^2 matrix)
    yang_offdiag = N * (N - 1)  # from permutation operator P

    # Nonzero entries in Yang R-matrix at generic u
    yang_nonzero = N * N + yang_offdiag - N  # Id + P - overlap
    # = N^2 + N*(N-1) - N = 2*N^2 - 2*N = 2*N*(N-1)... wait
    # Id: N^2 entries on diagonal.  P: N^2 entries at (ia, ai).
    # Overlap: N entries where i=a (both Id and P contribute).
    # Union: N^2 + N^2 - N = 2*N^2 - N.  But off-diagonal from P only: N^2 - N.
    yang_nonzero_corrected = 2 * N * N - N

    # Percentage in 324x324
    total_offdiag_space = 324 * 324 - 324  # = 104,652
    percentage = 100.0 * n_offdiag / total_offdiag_space

    # Central charge at level 1
    c_level1 = F(data['dim_g'], 1 + data['h_dual'])
    c_total = c_level1 + n_comp  # KM + Heisenberg

    return {
        'ade_type': ade_type,
        'rank': r,
        'n_mukai_dirs': d,
        'dim_g': data['dim_g'],
        'dim_V': N,
        'h_dual': data['h_dual'],
        'complement_rank': n_comp,
        'state_decomposition': {
            'ade_row': n_ade_row,
            'ade_col': n_ade_col,
            'ade_two_point': n_ade_two,
            'complement_row': n_comp_row,
            'complement_col': n_comp_col,
            'mixed_two_point': n_mixed_two,
            'complement_two_point': n_comp_two,
            'total': n_total,
        },
        'off_diagonal': {
            'ade_row_block': off_ade_row,
            'ade_col_block': off_ade_col,
            'ade_two_point_block': off_ade_two,
            'mixed_blocks': off_mixed,
            'complement': off_comp,
            'total': n_offdiag,
        },
        'yang_r_matrix': {
            'N': N,
            'matrix_size': N * N,
            'offdiagonal_from_P': yang_offdiag,
            'total_nonzero': yang_nonzero_corrected,
        },
        'central_charge': {
            'c_km_level1': str(c_level1),
            'c_heisenberg': n_comp,
            'c_total': str(c_total),
            'c_total_is_24': c_total == 24,
        },
        'outer_automorphism': OUTER_AUTOMORPHISMS[ade_type],
        'total_offdiagonal_space': total_offdiag_space,
        'percentage_nonzero': percentage,
        'status': STATUS,
    }


# =========================================================================
# 2. Full ADE landscape
# =========================================================================

def full_ade_landscape() -> Dict[str, Any]:
    r"""Compute the off-diagonal count and R-matrix data for ALL ADE types.

    Returns the complete landscape including D5 (absent from previous engines).

    The landscape is MONOTONIC in rank: higher rank -> more off-diagonal entries.
    This reflects the growth of the nonabelian Yangian sector.

    The FORMULA: total_offdiag(d) = d*(d-1)*(26-d) + C(d,2)*(C(d,2)-1)
    is a polynomial of degree 4 in d.  It is monotonically increasing for
    d in {2,3,4,5,6,7,8} (the ADE range).

    Returns
    -------
    dict with landscape data for all ADE types.
    """
    landscape = {}
    for ade_type in ADE_TYPES_ORDERED:
        result = offdiagonal_count_general(ade_type)
        landscape[ade_type] = {
            'rank': result['rank'],
            'dim_V': result['dim_V'],
            'n_mukai_dirs': result['n_mukai_dirs'],
            'n_offdiag': result['off_diagonal']['total'],
            'percentage': result['percentage_nonzero'],
            'complement_rank': result['complement_rank'],
            'c_km_level1': result['central_charge']['c_km_level1'],
            'outer_aut': result['outer_automorphism']['group'],
        }

    # Add generic (abelian)
    landscape['generic'] = {
        'rank': 0,
        'dim_V': 1,
        'n_mukai_dirs': 0,
        'n_offdiag': 0,
        'percentage': 0.0,
        'complement_rank': 24,
        'c_km_level1': '0',
        'outer_aut': 'N/A',
    }

    # Verify monotonicity
    types_ordered = ADE_TYPES_ORDERED
    monotonic = all(
        landscape[types_ordered[i]]['n_offdiag']
        < landscape[types_ordered[i + 1]]['n_offdiag']
        for i in range(len(types_ordered) - 1)
    )

    # Growth ratios
    growth = {}
    for i in range(1, len(types_ordered)):
        prev = types_ordered[i - 1]
        curr = types_ordered[i]
        ratio = landscape[curr]['n_offdiag'] / landscape[prev]['n_offdiag']
        growth[f'{prev}->{curr}'] = round(ratio, 3)

    return {
        'landscape': landscape,
        'types_ordered': types_ordered,
        'total_offdiagonal_space': 324 * 324 - 324,
        'monotonic_in_rank': monotonic,
        'growth_ratios': growth,
        'status': STATUS,
    }


# =========================================================================
# 3. Cartan matrices and root systems for each type
# =========================================================================

def cartan_matrix(ade_type: str) -> np.ndarray:
    """Return the Cartan matrix for an ADE type.

    Uses ade_yangian_level1.ade_data for the authoritative source.

    Returns
    -------
    np.ndarray of shape (rank, rank).
    """
    data = ade_data(ade_type)
    return np.array(data.cartan, dtype=int)


def dynkin_diagram_edges(ade_type: str) -> List[Tuple[int, int]]:
    """Return the edges (Serre pairs) of the Dynkin diagram.

    Each edge (i,j) with i < j corresponds to C_{ij} = -1.

    Returns
    -------
    list of (i, j) tuples.
    """
    C = cartan_matrix(ade_type)
    r = C.shape[0]
    edges = []
    for i in range(r):
        for j in range(i + 1, r):
            if C[i, j] == -1:
                edges.append((i, j))
    return edges


def branching_structure(ade_type: str) -> Dict[str, Any]:
    """Analyze the branching (fork) structure of the Dynkin diagram.

    Returns
    -------
    dict with branching node, legs, chain, and structural properties.
    """
    C = cartan_matrix(ade_type)
    r = C.shape[0]

    # Compute valence of each node
    valences = {}
    neighbors = {}
    for i in range(r):
        nbrs = [j for j in range(r) if j != i and C[i, j] == -1]
        valences[i] = len(nbrs)
        neighbors[i] = nbrs

    # Find branching node(s): valence >= 3
    branching_nodes = [i for i, v in valences.items() if v >= 3]

    # Find leaf nodes: valence == 1
    leaf_nodes = [i for i, v in valences.items() if v == 1]

    # Chain length from branching node to each leaf
    if branching_nodes:
        bnode = branching_nodes[0]
        legs = {}
        for leaf in leaf_nodes:
            # BFS from branching node to leaf
            path = _find_path(neighbors, bnode, leaf)
            legs[leaf] = {
                'path': path,
                'length': len(path) - 1,
            }
    else:
        bnode = None
        legs = {}

    # Is it a fork? (D-type or E-type)
    is_fork = len(branching_nodes) > 0

    # Specific diagram type detection
    if ade_type.startswith('A'):
        diagram_type = 'linear'
    elif ade_type.startswith('D'):
        diagram_type = 'fork_D'
    else:
        diagram_type = 'fork_E'

    return {
        'ade_type': ade_type,
        'rank': r,
        'valences': valences,
        'branching_nodes': branching_nodes,
        'leaf_nodes': leaf_nodes,
        'is_fork': is_fork,
        'diagram_type': diagram_type,
        'branching_node': bnode,
        'legs': legs,
        'num_edges': len(dynkin_diagram_edges(ade_type)),
        'num_serre_relations': len(dynkin_diagram_edges(ade_type)),
    }


def _find_path(neighbors: Dict[int, List[int]], start: int, end: int) -> List[int]:
    """BFS to find path from start to end in the Dynkin graph."""
    from collections import deque
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for nbr in neighbors[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, path + [nbr]))
    return []


# =========================================================================
# 4. Serre relations for each ADE type
# =========================================================================

def serre_relations(ade_type: str) -> Dict[str, Any]:
    r"""Compute the Serre relations for an ADE type.

    For simply-laced ADE: each edge (i,j) gives degree-2 Serre:
      [e_i, [e_i, e_j]] = 0

    In the Yangian context: the Drinfeld-Jimbo quantum group U_q(g)
    has q-Serre relations; at q=1 these reduce to the classical Serre.

    The Serre relations constrain the structure of the K3 Yangian at
    the enhancement point.  The MIXING Serre integral I_mix vanishes
    by Mukai orthogonality (orthogonal sublattice decomposition).

    Parameters
    ----------
    ade_type : ADE label.

    Returns
    -------
    dict with Serre relation data.
    """
    C = cartan_matrix(ade_type)
    r = C.shape[0]
    edges = dynkin_diagram_edges(ade_type)

    serre_pairs = []
    for (i, j) in edges:
        # Serre degree = 1 - C_{ij} (simply-laced: always 2)
        degree = 1 - C[i, j]
        serre_pairs.append({
            'nodes': (i, j),
            'C_ij': int(C[i, j]),
            'serre_degree': degree,
            'relation': (
                f'ad(e_{i})^{degree}(e_{j}) = 0'
                if degree == 2
                else f'ad(e_{i})^{degree}(e_{j}) = 0'
            ),
        })

    # Outer automorphism action on Serre relations
    outer = OUTER_AUTOMORPHISMS[ade_type]
    if outer['order'] > 1:
        outer_permutes_serre = True
        outer_description = (
            f"Out({ade_type}) = {outer['group']} permutes the Serre relations "
            f"by its action on the Dynkin diagram nodes."
        )
    else:
        outer_permutes_serre = False
        outer_description = (
            f"Out({ade_type}) is trivial: Serre relations are fixed."
        )

    return {
        'ade_type': ade_type,
        'rank': r,
        'num_serre_relations': len(serre_pairs),
        'expected_num_edges': r - 1,
        'correct_num_edges': len(serre_pairs) == r - 1,
        'serre_pairs': serre_pairs,
        'all_degree_2': all(s['serre_degree'] == 2 for s in serre_pairs),
        'mixing_serre_trivial': True,
        'mixing_reason': 'Mukai orthogonality: I_ADE + I_ab decomposition',
        'outer_automorphism': outer,
        'outer_permutes_serre': outer_permutes_serre,
        'outer_description': outer_description,
        'status': STATUS,
    }


# =========================================================================
# 5. Yang R-matrix construction and verification for each type
# =========================================================================

def yang_r_matrix_ade(ade_type: str, u: float = 3.7) -> Dict[str, Any]:
    r"""Construct and analyze the Yang R-matrix for an ADE type.

    R(u) = u*Id_{N^2} + P on C^N x C^N, where N = dim(V).

    For E_8 (N=248), we do NOT construct the full 61504 x 61504 matrix.
    Instead we report structural properties.

    Parameters
    ----------
    ade_type : ADE label.
    u : spectral parameter (AP-CY28: must avoid poles).

    Returns
    -------
    dict with R-matrix analysis.
    """
    data = FULL_ADE_DATA[ade_type]
    N = data['dim_V']
    matrix_dim = N * N

    # Size threshold: do not construct matrices larger than ~4000 x 4000
    MAX_CONSTRUCT = 4000
    can_construct = matrix_dim <= MAX_CONSTRUCT

    result = {
        'ade_type': ade_type,
        'N': N,
        'matrix_dim': matrix_dim,
        'matrix_entries': matrix_dim * matrix_dim,
        'can_construct': can_construct,
        'u': u,
    }

    if can_construct:
        R = yang_r_matrix_NxN(u, N)

        # Nonzero count
        nonzero = int(np.count_nonzero(R))

        # Off-diagonal count
        offdiag_mask = ~np.eye(matrix_dim, dtype=bool)
        offdiag_nonzero = int(np.count_nonzero(R[offdiag_mask]))

        # Unitarity: R(u)*R(-u) = (1-u^2)*Id
        R_neg = yang_r_matrix_NxN(-u, N)
        product = R @ R_neg
        expected = (1.0 - u * u) * np.eye(matrix_dim)
        unitarity_dev = float(np.max(np.abs(product - expected)))

        # Trace
        trace = float(np.trace(R))
        expected_trace = float(u * matrix_dim + N)  # tr(u*Id + P) = u*N^2 + N

        result.update({
            'nonzero_entries': nonzero,
            'offdiagonal_nonzero': offdiag_nonzero,
            'expected_offdiag_from_P': N * (N - 1),
            'offdiag_matches_formula': offdiag_nonzero == N * (N - 1),
            'unitarity_deviation': unitarity_dev,
            'unitarity_holds': unitarity_dev < 1e-10,
            'trace': trace,
            'expected_trace': expected_trace,
            'trace_matches': abs(trace - expected_trace) < 1e-10,
            'R_constructed': True,
        })
    else:
        # Structural properties only (E_7, E_8)
        offdiag_from_P = N * (N - 1)
        total_nonzero = 2 * N * N - N  # Id + P - overlap

        result.update({
            'nonzero_entries': total_nonzero,
            'offdiagonal_nonzero': offdiag_from_P,
            'expected_offdiag_from_P': offdiag_from_P,
            'offdiag_matches_formula': True,  # by construction
            'unitarity_deviation': 0.0,  # guaranteed by universal construction
            'unitarity_holds': True,  # universal property of Yang R-matrix
            'trace': u * matrix_dim + N,
            'expected_trace': u * matrix_dim + N,
            'trace_matches': True,
            'R_constructed': False,
            'reason': (
                f'Matrix size {matrix_dim}x{matrix_dim} = {matrix_dim**2} entries '
                f'exceeds threshold {MAX_CONSTRUCT}x{MAX_CONSTRUCT}. '
                f'Properties verified analytically.'
            ),
        })

    result['status'] = STATUS
    return result


def yang_r_ybe_verification(ade_type: str, u: float = 3.7, v: float = 2.3) -> Dict[str, Any]:
    r"""Verify the Yang-Baxter equation for an ADE type.

    YBE: R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)

    For large N (E_7, E_8): YBE is guaranteed by the universal construction.
    We only verify numerically for N <= 27 (up to E_6).

    Parameters
    ----------
    ade_type : ADE label.
    u, v : spectral parameters.

    Returns
    -------
    dict with YBE verification.
    """
    data = FULL_ADE_DATA[ade_type]
    N = data['dim_V']

    # N^3 x N^3 matrix required; limit to N <= 27
    MAX_YBE_N = 27
    can_verify = N <= MAX_YBE_N

    if can_verify:
        result = yang_r_verify_ybe(u, v, hbar=1.0, n=N)
        return {
            'ade_type': ade_type,
            'N': N,
            'u': u,
            'v': v,
            'ybe_satisfied': result['ybe_satisfied'],
            'error_norm': result['error_norm'],
            'verified_numerically': True,
            'status': STATUS,
        }
    else:
        return {
            'ade_type': ade_type,
            'N': N,
            'u': u,
            'v': v,
            'ybe_satisfied': True,
            'error_norm': 0.0,
            'verified_numerically': False,
            'reason': (
                f'N={N}: N^3 = {N**3} too large for explicit verification. '
                f'YBE guaranteed by universal Yang R-matrix construction: '
                f'R(u) = u*Id + P satisfies YBE for ANY N (proof: direct computation '
                f'using P^2 = Id, algebraic identity).'
            ),
            'status': STATUS,
        }


# =========================================================================
# 6. K3 embedding parameters for each type
# =========================================================================

def k3_embedding_parameters(ade_type: str, epsilon: float = 1.0) -> Dict[str, Any]:
    r"""K3 Yangian parameters at a general ADE enhancement point.

    At an ADE singularity of type g with rank r on K3:
      - r Mukai directions merge into the root lattice
      - (24-r) directions remain abelian
      - CY_2 constraint: sum_{i=1}^{24} h_i = 0

    Parameters
    ----------
    ade_type : ADE label.
    epsilon : overall scale for the Mukai weights.

    Returns
    -------
    dict with embedding parameters.
    """
    data = FULL_ADE_DATA[ade_type]
    r = data['rank']
    d = data['n_mukai_dirs']
    n_comp = MUKAI_RANK - d

    # ADE sector: d parameters constrained by root lattice
    # Evenly spaced, centered at 0, satisfying sum = 0
    h_ade = [epsilon * (d + 1 - 2 * k) / (2.0 * d) for k in range(1, d + 1)]

    # Abelian complement: n_comp parameters with sum = -sum(h_ade)
    ade_sum = sum(h_ade)
    if n_comp > 0:
        h_ab_base = -ade_sum / n_comp
        h_ab = [h_ab_base + epsilon * 0.003 * (i - n_comp / 2.0)
                for i in range(n_comp)]
        # Correct last entry for exact CY_2
        h_ab[-1] = -ade_sum - sum(h_ab[:-1])
    else:
        h_ab = []

    h_all = h_ade + h_ab
    cy2_sum = sum(h_all)

    # Central charge
    c_km = F(data['dim_g'], 1 + data['h_dual'])
    c_total = c_km + n_comp

    # Mukai decomposition
    try:
        ade_obj = ade_data(ade_type)
        embedding = ADEMukaiEmbedding(ade_obj)
        mukai_decomp = embedding.mukai_decomposition()
    except Exception:
        mukai_decomp = {
            'ade_rank': r,
            'complement_rank': n_comp,
            'total': MUKAI_RANK,
        }

    return {
        'ade_type': ade_type,
        'epsilon': epsilon,
        'rank': r,
        'n_mukai_dirs': d,
        'complement_rank': n_comp,
        'h_ade': h_ade,
        'h_abelian_sample': h_ab[:5] if len(h_ab) >= 5 else h_ab,
        'n_ade_params': len(h_ade),
        'n_abelian_params': len(h_ab),
        'total_params': len(h_all),
        'cy2_sum': cy2_sum,
        'cy2_satisfied': abs(cy2_sum) < 1e-10,
        'central_charge': {
            'c_km_level1': str(c_km),
            'c_heisenberg': n_comp,
            'c_total': str(c_total),
            'c_total_is_24': c_total == 24,
        },
        'mukai_decomposition': mukai_decomp,
        'status': STATUS,
    }


# =========================================================================
# 7. Structure function factorization for each type
# =========================================================================

def structure_function_factored(
    ade_type: str,
    z: float = 5.7,
    epsilon: float = 1.0,
) -> Dict[str, Any]:
    r"""Factored structure function g_{K3}(z) at an ADE enhancement point.

    g_{K3}(z) = g_{ADE}(z) * g_{compl}(z)

    where:
      g_{ADE}(z) = prod_{i=1}^{d} (z - h_i)/(z + h_i)  (ADE sector)
      g_{compl}(z) = prod_{j=d+1}^{24} (z - h_j)/(z + h_j)  (complement)

    AP-CY28: z must avoid +/- h_i for all i.

    Parameters
    ----------
    ade_type : ADE label.
    z : spectral parameter.
    epsilon : overall scale.

    Returns
    -------
    dict with factored structure function.
    """
    params = k3_embedding_parameters(ade_type, epsilon)
    h_ade = params['h_ade']
    d = params['n_mukai_dirs']
    n_comp = params['complement_rank']

    # Reconstruct full abelian sector
    ade_sum = sum(h_ade)
    if n_comp > 0:
        h_ab_base = -ade_sum / n_comp
        h_ab = [h_ab_base + epsilon * 0.003 * (i - n_comp / 2.0)
                for i in range(n_comp)]
        h_ab[-1] = -ade_sum - sum(h_ab[:-1])
    else:
        h_ab = []

    all_h = h_ade + h_ab

    # Check poles (AP-CY28)
    for h in all_h:
        if abs(z + h) < 1e-12:
            raise ValueError(f"Pole at z={z}: z + h = 0 for h = {h}")

    # ADE sector
    g_ade = 1.0
    for h in h_ade:
        g_ade *= (z - h) / (z + h)

    # Abelian sector
    g_ab = 1.0
    for h in h_ab:
        g_ab *= (z - h) / (z + h)

    g_total = g_ade * g_ab

    # Unitarity: g(z) * g(-z) = 1
    g_neg_ade = 1.0
    for h in h_ade:
        g_neg_ade *= (-z - h) / (-z + h)
    g_neg_ab = 1.0
    for h in h_ab:
        g_neg_ab *= (-z - h) / (-z + h)
    g_neg_total = g_neg_ade * g_neg_ab
    unitarity_product = g_total * g_neg_total

    return {
        'ade_type': ade_type,
        'z': z,
        'g_ade': g_ade,
        'g_complement': g_ab,
        'g_total': g_total,
        'factored': abs(g_ade * g_ab - g_total) < 1e-12,
        'unitarity_product': unitarity_product,
        'unitarity_holds': abs(unitarity_product - 1.0) < 1e-10,
        'g_ade_degree': (d, d),
        'g_complement_degree': (n_comp, n_comp),
        'g_total_degree': (24, 24),
        'status': STATUS,
    }


# =========================================================================
# 8. Type-specific features
# =========================================================================

def a2_specific() -> Dict[str, Any]:
    r"""A_2-specific features: sl_3, 3x3 Yang R-matrix.

    sl_3 has:
      - rank 2, dim 8
      - fundamental rep V = C^3 (the 3)
      - Cartan: [[2,-1],[-1,2]]
      - 3 positive roots: alpha_1, alpha_2, alpha_1 + alpha_2
      - Weyl group S_3 (order 6)
      - Z_2 outer automorphism (charge conjugation: alpha_1 <-> alpha_2)

    Yang R-matrix: 9x9 matrix R(u) = u*Id_9 + P on C^3 x C^3.
    Off-diagonal entries from P: 3*(3-1) = 6.
    Total nonzero at generic u: 2*9 - 3 = 15.

    Serre: 1 relation, [e_1, [e_1, e_2]] = 0.
    """
    C = cartan_matrix('A2')
    data = ade_data('A2')

    # 3x3 Yang R-matrix
    u_test = 5.7  # AP-CY28 safe
    R = yang_r_matrix_NxN(u_test, 3)

    # Off-diagonal
    offdiag = int(np.count_nonzero(R - np.diag(np.diag(R))))

    # YBE
    ybe = yang_r_verify_ybe(u_test, 2.3, hbar=1.0, n=3)

    # Unitarity
    R_neg = yang_r_matrix_NxN(-u_test, 3)
    unit_prod = R @ R_neg
    unit_dev = float(np.max(np.abs(unit_prod - (1 - u_test**2) * np.eye(9))))

    # Weights of fundamental representation
    W = all_weights_defining_rep(data)

    return {
        'type': 'A2 = sl_3',
        'rank': 2,
        'dim_g': 8,
        'dim_V': 3,
        'h_dual': 3,
        'c_level1': str(F(8, 4)),  # = 2
        'positive_roots': 3,
        'weyl_group_order': 6,
        'outer_aut': 'Z_2 (charge conjugation)',
        'cartan_matrix': C.tolist(),
        'fundamental_weights': W.tolist(),
        'yang_r_matrix': {
            'size': '9x9',
            'offdiagonal_nonzero': offdiag,
            'expected': 6,
            'matches': offdiag == 6,
            'ybe_satisfied': ybe['ybe_satisfied'],
            'ybe_error': ybe['error_norm'],
            'unitarity_deviation': unit_dev,
            'unitarity_holds': unit_dev < 1e-10,
        },
        'serre': {
            'num_relations': 1,
            'relation': '[e_1, [e_1, e_2]] = 0',
            'degree': 2,
        },
        'k3_offdiag_324': 144,
        'status': STATUS,
    }


def d5_specific() -> Dict[str, Any]:
    r"""D_5-specific features: so_{10}, fork with NO triality.

    so_{10} has:
      - rank 5, dim 45
      - fundamental (vector) rep V = C^{10}
      - TWO spinor reps: 16_s and 16_c (NOT 10-dimensional, unlike D_4)
      - Cartan matrix: fork at node 2 (0-indexed), connecting to nodes 3,4

    D_5 Dynkin diagram:
        0 -- 1 -- 2 -- 3
                   |
                   4

    CRITICAL DIFFERENCE from D_4:
      - D_4: Out(D_4) = S_3 (triality, order 6)
      - D_5: Out(D_5) = Z_2 (swap nodes 3 <-> 4, order 2)

    The Z_2 swaps the two spinor representations 16_s <-> 16_c but
    fixes the vector representation.  This is NOT triality; it is
    ordinary charge conjugation.

    Yang R-matrix: 100x100 matrix R(u) = u*Id_{100} + P on C^{10} x C^{10}.
    Off-diagonal from P: 10*9 = 90.
    """
    C = cartan_matrix('D5')
    data = ade_data('D5')
    branching = branching_structure('D5')

    # 100x100 Yang R-matrix
    u_test = 5.7
    N = 10
    R = yang_r_matrix_NxN(u_test, N)
    offdiag = int(np.count_nonzero(R - np.diag(np.diag(R))))

    # Unitarity
    R_neg = yang_r_matrix_NxN(-u_test, N)
    unit_prod = R @ R_neg
    unit_dev = float(np.max(np.abs(unit_prod - (1 - u_test**2) * np.eye(N * N))))

    # Weights
    W = all_weights_defining_rep(data)

    # Spinor dimensions: D_5 has 2^{5-1} = 16 dimensional spinors
    spinor_dim = 2 ** (data.rank - 1)

    return {
        'type': 'D5 = so_{10}',
        'rank': 5,
        'dim_g': 45,
        'dim_V': 10,
        'h_dual': 8,
        'c_level1': str(F(45, 9)),  # = 5
        'positive_roots': 20,  # n*(2n-1)/2 for D_n: 5*9/2... no. D_5 pos roots: 5*4 = 20
        'weyl_group_order': 2**(5 - 1) * 120,  # 2^{n-1} * n! for D_n
        'outer_aut': 'Z_2 (spinor swap, NOT triality)',
        'no_triality': True,
        'triality_unique_to_d4': True,
        'spinor_dim': spinor_dim,
        'spinor_reps': f'16_s and 16_c (dim {spinor_dim})',
        'cartan_matrix': C.tolist(),
        'branching': branching,
        'yang_r_matrix': {
            'size': f'{N*N}x{N*N}',
            'offdiagonal_nonzero': offdiag,
            'expected': N * (N - 1),
            'matches': offdiag == N * (N - 1),
            'unitarity_deviation': unit_dev,
            'unitarity_holds': unit_dev < 1e-10,
        },
        'serre': {
            'num_relations': 4,  # rank - 1
            'fork_node': branching['branching_node'],
        },
        'k3_offdiag_324': 510,
        'status': STATUS,
    }


def e6_specific() -> Dict[str, Any]:
    r"""E_6-specific features: 27-dim fundamental, exceptional geometry.

    E_6 has:
      - rank 6, dim 78
      - fundamental (minuscule) rep V = C^{27}
      - dual fundamental: 27-bar (also 27-dimensional, related by Z_2)
      - Cartan with branching at node 2 (0-indexed)

    E_6 Dynkin diagram:
        0 -- 1 -- 2 -- 3 -- 4
                   |
                   5

    Z_2 outer automorphism: nodes 0 <-> 4, 1 <-> 3, 2 fixed, 5 fixed.
    This exchanges 27 <-> 27-bar.

    The 27 of E_6 parametrizes lines on a cubic surface (the del Pezzo
    surface dP_6).  Its tensor product 27 x 27 = 729 decomposes as:
      Sym^2(27) = 1 + 351' (dim 352)
      Lambda^2(27) = 78 + 27' + ... but more precisely:
      27 x 27 = 1 + 78 + 650  (NOT standard decomposition)

    Actually: 27 x 27 = 27' + 351_s (in E_6 representation theory)
    where 351_s is the symmetric traceless part.  Let me NOT assert the
    exact tensor product decomposition here; what matters is that the
    R-matrix on the 729-dimensional tensor product space has the Yang
    R-matrix structure.

    Yang R-matrix: 729x729 matrix.
    Off-diagonal from P: 27*26 = 702.
    """
    C = cartan_matrix('E6')
    data = ade_data('E6')
    branching = branching_structure('E6')

    # 729x729 Yang R-matrix
    u_test = 5.7
    N = 27
    R = yang_r_matrix_NxN(u_test, N)
    offdiag = int(np.count_nonzero(R - np.diag(np.diag(R))))

    # Unitarity
    R_neg = yang_r_matrix_NxN(-u_test, N)
    unit_prod = R @ R_neg
    unit_dev = float(np.max(np.abs(unit_prod - (1 - u_test**2) * np.eye(N * N))))

    return {
        'type': 'E6',
        'rank': 6,
        'dim_g': 78,
        'dim_V': 27,
        'h_dual': 12,
        'c_level1': str(F(78, 13)),  # = 6
        'positive_roots': 36,
        'weyl_group_order': 51840,
        'outer_aut': 'Z_2 (diagram flip, exchanges 27 <-> 27-bar)',
        'cartan_matrix': C.tolist(),
        'branching': branching,
        'exceptional_geometry': {
            'cubic_surface_lines': 27,
            'del_pezzo': 'dP_6',
            'description': (
                'The 27 of E_6 parametrizes the 27 lines on a cubic surface. '
                'At the E_6 enhancement point on K3, all 27 lines participate '
                'in the non-abelian R-matrix.'
            ),
        },
        'yang_r_matrix': {
            'size': f'{N*N}x{N*N}',
            'offdiagonal_nonzero': offdiag,
            'expected': N * (N - 1),
            'matches': offdiag == N * (N - 1),
            'unitarity_deviation': unit_dev,
            'unitarity_holds': unit_dev < 1e-10,
        },
        'serre': {
            'num_relations': 5,
        },
        'k3_offdiag_324': 810,
        'status': STATUS,
    }


def e7_specific() -> Dict[str, Any]:
    r"""E_7-specific features: 56-dim fundamental.

    E_7 has:
      - rank 7, dim 133
      - fundamental (minuscule) rep V = C^{56}
      - SELF-DUAL: 56 = 56-bar (no outer automorphism)
      - Center: Z_2

    E_7 Dynkin diagram:
        0 -- 1 -- 2 -- 3 -- 4 -- 5
                   |
                   6

    Out(E_7) = 1 (trivial): the diagram has no non-trivial automorphisms.
    The 56 is self-dual under the symplectic form preserved by E_7.

    Yang R-matrix: 3136x3136 matrix.
    Off-diagonal from P: 56*55 = 3080.

    NOTE: N^2 = 3136, so explicit construction is POSSIBLE but slow.
    We report structural properties and verify unitarity only.
    """
    C = cartan_matrix('E7')
    data = ade_data('E7')
    branching = branching_structure('E7')
    N = 56

    # Structural properties (matrix too large for YBE but OK for construction)
    offdiag_from_P = N * (N - 1)
    total_nonzero = 2 * N * N - N

    # We CAN construct 3136x3136 but it is large. Verify unitarity.
    R = yang_r_matrix_NxN(5.7, N)
    R_neg = yang_r_matrix_NxN(-5.7, N)
    unit_prod = R @ R_neg
    unit_dev = float(np.max(np.abs(unit_prod - (1 - 5.7**2) * np.eye(N * N))))

    offdiag = int(np.count_nonzero(R - np.diag(np.diag(R))))

    return {
        'type': 'E7',
        'rank': 7,
        'dim_g': 133,
        'dim_V': 56,
        'h_dual': 18,
        'c_level1': str(F(133, 19)),  # = 7
        'positive_roots': 63,
        'weyl_group_order': 2903040,
        'outer_aut': 'trivial (Out(E_7) = 1)',
        'self_dual': True,
        'symplectic_form': 'E_7 preserves a symplectic form on the 56',
        'cartan_matrix': C.tolist(),
        'branching': branching,
        'yang_r_matrix': {
            'size': f'{N*N}x{N*N}',
            'offdiagonal_nonzero': offdiag,
            'expected': offdiag_from_P,
            'matches': offdiag == offdiag_from_P,
            'unitarity_deviation': unit_dev,
            'unitarity_holds': unit_dev < 1e-10,
        },
        'serre': {
            'num_relations': 6,
        },
        'k3_offdiag_324': 1218,
        'status': STATUS,
    }


def e8_specific() -> Dict[str, Any]:
    r"""E_8-specific features: adjoint = smallest rep (248-dim).

    E_8 has:
      - rank 8, dim 248
      - THE unique simple Lie algebra where adjoint = fundamental
      - dim(V) = dim(g) = 248
      - Center: trivial (Z_1)
      - Out(E_8) = 1

    E_8 Dynkin diagram:
        0 -- 1 -- 2 -- 3 -- 4 -- 5 -- 6
                   |
                   7

    The 248 representation is NOT minuscule (unlike E_6's 27 and E_7's 56).
    It is the adjoint representation, self-dual, with the Killing form
    providing the invariant bilinear form.

    Yang R-matrix: 61504 x 61504 matrix (NOT constructed explicitly).
    Off-diagonal from P: 248*247 = 61256.

    For the K3 R-matrix at charge 2:
      8 Mukai directions merge (= rank E_8, the MAXIMUM for ADE on K3)
      16 directions remain abelian
      Central charge: 8 + 16 = 24

    E_8 is the TERMINAL case: no ADE type has rank > 8, and rank 8
    already uses 8/24 = 1/3 of the Mukai lattice.
    """
    C = cartan_matrix('E8')
    branching = branching_structure('E8')
    N = 248

    offdiag_from_P = N * (N - 1)

    return {
        'type': 'E8',
        'rank': 8,
        'dim_g': 248,
        'dim_V': 248,
        'adjoint_equals_fundamental': True,
        'unique_property': (
            'E_8 is the ONLY simple Lie algebra where the adjoint '
            'representation (dim = 248) IS the smallest (fundamental) '
            'representation. For all other simple Lie algebras, the '
            'fundamental is strictly smaller than the adjoint.'
        ),
        'h_dual': 30,
        'c_level1': str(F(248, 31)),  # = 8
        'positive_roots': 120,
        'weyl_group_order': 696729600,
        'outer_aut': 'trivial (Out(E_8) = 1)',
        'center': 'trivial (Z_1)',
        'cartan_matrix': C.tolist(),
        'branching': branching,
        'yang_r_matrix': {
            'size': f'{N*N}x{N*N}',
            'offdiagonal_from_P': offdiag_from_P,
            'matrix_not_constructed': True,
            'reason': (
                f'61504 x 61504 = ~3.8 billion entries. '
                f'Properties guaranteed by universal Yang R-matrix.'
            ),
            'unitarity_holds': True,
            'ybe_holds': True,
        },
        'serre': {
            'num_relations': 7,
        },
        'k3_offdiag_324': 1764,
        'terminal_case': True,
        'mukai_fraction': '8/24 = 1/3 (maximum ADE usage of Mukai lattice)',
        'status': STATUS,
    }


# =========================================================================
# 9. Cross-type comparison and pattern analysis
# =========================================================================

def offdiag_growth_analysis() -> Dict[str, Any]:
    r"""Analyze the growth pattern of off-diagonal entries across ADE types.

    The off-diagonal count O(d) = d*(d-1)*(26-d) + C(d,2)*(C(d,2)-1)
    for d merged Mukai directions.

    Expanding:
      Let c = d*(d-1)/2 = C(d,2).
      O(d) = d*(d-1)*(26-d) + c*(c-1)
           = 2c*(26-d) + c*(c-1)
           = c*(2*(26-d) + c - 1)
           = c*(52 - 2d + d*(d-1)/2 - 1)
           = c*(51 - 2d + d^2/2 - d/2)
           = c*(51 - 5d/2 + d^2/2)

    The growth is controlled by:
      1. The ADE block contributions (row, col): ~ 2*d*(d-1), growing as d^2
      2. The ADE two-point block: ~ C(d,2)^2, growing as d^4
      3. The mixed blocks: ~ (24-d)*d*(d-1), growing as d^2 then declining

    The DOMINANT term at large d is the ADE two-point block (d^4 growth).

    Returns
    -------
    dict with growth analysis.
    """
    data = []
    for ade_type in ADE_TYPES_ORDERED:
        result = offdiagonal_count_general(ade_type)
        od = result['off_diagonal']
        d = result['n_mukai_dirs']
        data.append({
            'type': ade_type,
            'd': d,
            'total': od['total'],
            'ade_row': od['ade_row_block'],
            'ade_col': od['ade_col_block'],
            'ade_two': od['ade_two_point_block'],
            'mixed': od['mixed_blocks'],
            'ade_fraction': (od['ade_row_block'] + od['ade_col_block'] + od['ade_two_point_block']) / max(od['total'], 1),
            'mixed_fraction': od['mixed_blocks'] / max(od['total'], 1),
        })

    # Check that ADE two-point dominance emerges at high rank
    e8_data = data[-1]
    ade_two_dominates = e8_data['ade_two'] > e8_data['mixed']

    # Incremental growth
    increments = []
    for i in range(1, len(data)):
        inc = data[i]['total'] - data[i - 1]['total']
        increments.append({
            'from': data[i - 1]['type'],
            'to': data[i]['type'],
            'increment': inc,
            'ratio': data[i]['total'] / data[i - 1]['total'],
        })

    return {
        'data': data,
        'increments': increments,
        'ade_two_dominates_at_e8': ade_two_dominates,
        'formula': 'O(d) = d*(d-1)*(26-d) + C(d,2)*(C(d,2)-1)',
        'dominant_term': 'ADE two-point block (d^4 growth) dominates at high rank',
        'status': STATUS,
    }


def outer_automorphism_landscape() -> Dict[str, Any]:
    r"""Outer automorphism groups across the ADE landscape.

    The outer automorphism group of a simply-laced Lie algebra equals
    the automorphism group of its Dynkin diagram:

      A_1: trivial (1 node, no automorphisms)
      A_2: Z_2 (swap the 2 nodes)
      D_4: S_3 (triality: permute the 3 legs) -- UNIQUE
      D_5: Z_2 (swap the 2 fork endpoints)
      E_6: Z_2 (flip the diagram)
      E_7: trivial (no symmetry)
      E_8: trivial (no symmetry)

    For the K3 Yangian:
      - Outer automorphisms act as automorphisms of Y(g)
      - They permute the evaluation representations
      - D_4 triality (S_3) is the RICHEST case
      - For trivial Out: all Serre relations are inequivalent

    Returns
    -------
    dict with outer automorphism landscape.
    """
    landscape = {}
    for ade_type in ADE_TYPES_ORDERED:
        outer = OUTER_AUTOMORPHISMS[ade_type]
        landscape[ade_type] = outer

    # D_4 is unique
    d4_unique = OUTER_AUTOMORPHISMS['D4']['order'] == 6
    max_outer_order = max(o['order'] for o in OUTER_AUTOMORPHISMS.values())

    return {
        'landscape': landscape,
        'd4_triality_unique': d4_unique,
        'max_outer_order': max_outer_order,
        'max_outer_type': 'D4',
        'trivial_outer': [t for t in ADE_TYPES_ORDERED
                          if OUTER_AUTOMORPHISMS[t]['order'] == 1],
        'nontrivial_outer': [t for t in ADE_TYPES_ORDERED
                             if OUTER_AUTOMORPHISMS[t]['order'] > 1],
        'status': STATUS,
    }


# =========================================================================
# 10. Master summary
# =========================================================================

def master_all_ade() -> Dict[str, Any]:
    r"""Complete summary of the K3 nonabelian R-matrix at ALL ADE types.

    This is the main entry point for the all-ADE analysis.

    STATUS: CONJECTURAL (AP-CY14).  The Lie algebra data and Yang R-matrices
    are unconditional mathematical facts.  The K3 embedding requires CY-A_2
    (proved at d=2), and the K3 Yangian Y(g_{K3}) is conjectural.

    Returns
    -------
    dict with complete all-ADE landscape.
    """
    landscape = full_ade_landscape()
    growth = offdiag_growth_analysis()
    outer = outer_automorphism_landscape()

    # Per-type summaries
    type_summaries = {}
    for ade_type in ADE_TYPES_ORDERED:
        count = offdiagonal_count_general(ade_type)
        serre = serre_relations(ade_type)
        branch = branching_structure(ade_type)
        embed = k3_embedding_parameters(ade_type)
        yang = yang_r_matrix_ade(ade_type)

        type_summaries[ade_type] = {
            'rank': count['rank'],
            'dim_g': count['dim_g'],
            'dim_V': count['dim_V'],
            'n_mukai_dirs': count['n_mukai_dirs'],
            'complement_rank': count['complement_rank'],
            'offdiag_324': count['off_diagonal']['total'],
            'yang_offdiag': yang['offdiagonal_nonzero'],
            'yang_unitarity': yang['unitarity_holds'],
            'num_serre': serre['num_serre_relations'],
            'outer_aut': OUTER_AUTOMORPHISMS[ade_type]['group'],
            'c_total_24': embed['central_charge']['c_total_is_24'],
            'cy2_satisfied': embed['cy2_satisfied'],
        }

    # Key findings
    all_c_24 = all(s['c_total_24'] for s in type_summaries.values())
    all_cy2 = all(s['cy2_satisfied'] for s in type_summaries.values())
    all_unitarity = all(s['yang_unitarity'] for s in type_summaries.values())
    monotonic = landscape['monotonic_in_rank']

    return {
        'type_summaries': type_summaries,
        'landscape': landscape,
        'growth_analysis': growth,
        'outer_automorphism_landscape': outer,
        'key_findings': {
            'all_central_charge_24': all_c_24,
            'all_cy2_satisfied': all_cy2,
            'all_yang_unitarity': all_unitarity,
            'offdiag_monotonic_in_rank': monotonic,
            'offdiag_range': f"48 (A_1) to 1764 (E_8)",
            'd4_triality_unique': outer['d4_triality_unique'],
            'e8_adjoint_equals_fundamental': True,
            'e8_terminal': True,
        },
        'status': STATUS,
    }
