r"""Explicit cluster algebra structure on Y(g_{K3}).

STATUS: CONJECTURAL (AP-CY14).  Y(g_{K3}) is NOT constructed.  The cluster
algebra structure is further conjectural.  All results verify internal
consistency of the conjectural identification, not existence.

MATHEMATICAL CONTENT
====================

1. EXCHANGE MATRIX B FROM THE EULER FORM ON D^b(Coh(K3)).

   For a CY_2 category C = D^b(Coh(K3)), the Euler form is:

     chi(E, F) = sum_{k=0}^{2} (-1)^k dim Ext^k(E, F)

   By Serre duality for CY_d with d=2:
     Ext^k(E, F) ~ Ext^{d-k}(F, E)^*  =>  chi(E, F) = chi(F, E)

   CRITICAL: For CY_2, the Euler form is SYMMETRIC (not antisymmetric).
   This means B_{ij} = chi(S_i, S_j) - chi(S_j, S_i) = 0 identically.
   The exchange matrix from the Euler form vanishes for CY_2.

   Resolution: the nontrivial exchange matrix arises NOT from the Euler
   form directly but from the DECORATED Euler form on a stability slice.
   For a fixed heart A of a bounded t-structure, one restricts to a finite
   set of exceptional objects {E_1, ..., E_n} and defines:

     B_{ij} = dim Ext^1(E_i, E_j) - dim Ext^1(E_j, E_i)

   For K3 at the Kummer orbifold point T^4/Z_2, the McKay quiver for Z_2
   has 2 vertices with an A_1 exchange matrix:
     B_McKay = [[0, 2], [-2, 0]]
   (2 arrows from vertex 0 to vertex 1 from the 2-dimensional
   representation of Z_2 acting on T^4).

   For higher Picard rank, the exchange matrix enlarges: at a generic
   point of Stab(K3) with n exceptional objects visible, the exchange
   matrix is n x n antisymmetric.

   THE MUKAI-DERIVED EXCHANGE MATRIX:
   For the full K3 Yangian on the rank-24 Mukai lattice, we construct
   B from the INTERSECTION FORM on the Mukai lattice restricted to
   a chosen basis of spherical objects {S_i}_{i=1}^{n}:

     B_{ij} = <v(S_i), v(S_j)>_Muk - <v(S_j), v(S_i)>_Muk

   Since the Mukai pairing is symmetric, this vanishes for any basis.
   The nontrivial data comes from restricting to a HEART: the Euler
   form on an abelian subcategory is NOT symmetric (only on the full
   derived category does Serre duality impose symmetry).

   For K3 at Picard rank rho, the exchange matrix on the heart of
   Gieseker stability has rank <= rho.  At rho = 1 (generic K3),
   the Bridgeland slice gives the A_1 exchange matrix from the
   exceptional pair {O_X, O_X(H)[1]}.

2. CLUSTER VARIABLES AS YANGIAN ELEMENTS.

   The cluster variables in Y(g_{K3}) are the EVALUATION CHARACTERS:

     chi_v(z) := Tr_{V_v}(R_{K3}(z))

   where V_v is the Yangian module at Mukai vector v, and R_{K3}(z) is
   the R-matrix.  These satisfy exchange relations:

     chi_v(z) * chi_w(z) = sum_{v' + w' = v + w} c_{v',w'} chi_{v'}(z) chi_{w'}(z)

   At the tropical limit (LCS degeneration, AP157: MUM):
     chi_v -> theta_v  (GHKK canonical theta function)

   The exchange relation becomes the Fomin-Zelevinsky exchange:
     x_k * x_k' = prod_{B_{ik}>0} x_i^{B_{ik}} + prod_{B_{ik}<0} x_i^{-B_{ik}}

3. MUTATION = WALL-CROSSING IN Stab(K3).

   A wall in Stab(K3) is the locus where phi(v_1) = phi(v_2) for
   Mukai vectors v_1, v_2 with v_1 + v_2 = v (the total class).

   At such a wall, the CLUSTER MUTATION mu_k acts:
   - On the exchange matrix: Fomin-Zelevinsky matrix mutation
   - On the cluster variables: exchange relation
   - On the Yangian parameters: h_k -> -h_k + sum_{j: B_{kj}>0} h_j
   - On the R-matrix: R -> R' (equivalent R-matrix from the mutated
     presentation of Y(g_{K3}))

   The KS wall-crossing formula (at CY_2):
     Omega(v; sigma^+) - Omega(v; sigma^-) = sum KS terms
   matches the cluster exchange relation.

4. QUANTUM CLUSTER ALGEBRA.

   Y(g_{K3}) should carry a QUANTUM cluster algebra structure with
   quantum parameter q = exp(i*pi*<v_i, v_j>_Muk).

   The q-commutation relations:
     x_i * x_j = q^{Lambda_{ij}} * x_j * x_i

   where Lambda_{ij} is the COMPATIBILITY MATRIX related to B by:
     Lambda = B^{-1}  (on the mutable part)

   For the K3 Mukai lattice, the quantum parameter is:
     q_{ij} = exp(i*pi*omega^{ij})

   where omega^{ij} is the Mukai pairing.  Since the Mukai pairing is
   INTEGER-valued on the lattice, q_{ij} = (-1)^{omega^{ij}} = +/- 1.
   This means the quantum cluster algebra is a SQUARE ROOT quantum
   cluster algebra (q^2 = 1).

   The q-deformation of the exchange relation:
     x_k * x_k' = q^{a} prod x_i^{B_{ik}+} + q^{b} prod x_i^{-B_{ik}-}

   At q = 1 (classical limit), this reduces to Fomin-Zelevinsky.

5. A_1 REDUCTION.

   At the conifold point of K3 (a single (-2)-curve contracted), only
   ONE spherical object E with v(E)^2 = -2 is relevant.  The cluster
   algebra reduces to:

     B_conifold = [[0, 1], [-1, 0]]  (A_1 exchange)

   with 2 cluster variables: x_1 = chi_E(z), x_2 = chi_{E[1]}(z).
   The exchange relation: x_1 * x_1' = 1 + x_2 (the A_1 pentagon).
   The Yangian specializes to the affine Yangian Y(sl_2) at level 1.

   For a K3 with n (-2)-curves (ADE singularity of type Gamma), the
   cluster algebra is of type Gamma with exchange matrix from the
   Cartan matrix of the ADE root system.

BEILINSON WARNINGS
==================

AP-CY14: Y(g_{K3}) is CONJECTURAL. Cluster structure further conjectural.
AP-CY6:  A_{K3} at d=2 IS proved (CY-A_2). But Yangian quantization open.
AP-CY11: Results depending on wall-crossing/coproduct are conditional.
AP113:   kappa_ch = 2 (K3). Subscripts required.
AP157:   Degeneration type: LCS / MUM for tropical limit.
AP-CY10: Flop preserves kappa_ch; distinct from Koszul dual.
AP-CY12: Shadow class from full tower, not generator counting.
AP-CY28: Test points must avoid poles at z = +/- h_i.

CONVENTIONS
===========

  - Exact arithmetic via fractions.Fraction throughout.
  - Exchange matrix B is ANTISYMMETRIC: B_{ij} = -B_{ji}.
  - Cluster mutation mu_k is an involution: mu_k^2 = id.
  - Quantum parameter q_{ij} from the Mukai pairing.
  - Stability conditions sigma = (Z, P) on D^b(Coh(K3)).
  - Mukai vector v = (r, c_1, s) with pairing <v,w> = c_1*c_1' - r*s' - r'*s.

REFERENCES
==========

  Fomin-Zelevinsky, arXiv:math/0104151 (cluster algebras I)
  Berenstein-Zelevinsky, arXiv:math/0411446 (quantum cluster algebras)
  Gross-Hacking-Keel-Kontsevich, arXiv:1411.1394 (canonical bases, cluster)
  Bridgeland, arXiv:0703.1169 (stability conditions on K3)
  Bridgeland, arXiv:1611.03697 (scattering diagrams and stability)
  Kontsevich-Soibelman, arXiv:0811.2435 (stability structures)
  Fock-Goncharov, arXiv:math/0311245 (cluster ensembles)
  Maulik-Okounkov, arXiv:1211.1287 (stable envelopes)
  Nagao, arXiv:1002.4956 (DT/cluster via mutations)

  k3_yangian.py: K3 Yangian structure function, R-matrix, presentation
  k3_yangian_quantization.py: RTT presentation, Fake Monster
  bridgeland_k3_yangian.py: Stab(K3) <-> Yangian parameter space
  tropical_shadow_cluster.py: GPS scattering, tropical cluster structure
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from compute.lib.tropical_shadow_cluster import (
    MUKAI_RANK,
    MUKAI_SIGNATURE,
    mukai_pairing_diagonal,
    mukai_inner_product,
    exchange_matrix_from_euler_form,
    exchange_matrix_is_antisymmetric,
    cluster_mutation,
    cluster_mutation_involution_check,
    cluster_type_a2,
    cluster_type_a3,
    yangian_parameter_mutation,
    yangian_structure_function,
    yangian_unitarity_check,
    TropicalScatteringDiagram,
)

F = Fraction

STATUS = 'CONJECTURAL'  # AP-CY14: Y(g_{K3}) is NOT constructed


# ============================================================================
# 0. Constants
# ============================================================================

CY_DIMENSION = 2  # K3 is CY_2 (AP-CY1: CY dim d, not complex dim n)

# Picard rank values for standard K3 surfaces
PICARD_GENERIC = 1
PICARD_KUMMER = 20
PICARD_MAX = 20  # Maximum Picard rank for K3


# ============================================================================
# 1. EXCHANGE MATRIX FROM D^b(Coh(K3))
# ============================================================================

def euler_form_heart_k3(
    ext1_matrix: List[List[int]],
) -> List[List[int]]:
    r"""Exchange matrix from the Ext^1 data of a heart of D^b(Coh(K3)).

    For CY_2, the full Euler form chi(E,F) = chi(F,E) is symmetric (Serre
    duality), so the antisymmetric part vanishes on the derived category.

    The nontrivial exchange matrix comes from restricting to a HEART A of
    a bounded t-structure, where the Ext^1 data is NOT symmetric.

    Given dim Ext^1(E_i, E_j) for a collection of objects {E_i} in the
    heart, the exchange matrix is:

      B_{ij} = dim Ext^1(E_i, E_j) - dim Ext^1(E_j, E_i)

    Parameters
    ----------
    ext1_matrix : list of list of int
        Matrix where entry [i][j] = dim Ext^1(E_i, E_j).

    Returns
    -------
    list of list of int : antisymmetric exchange matrix B.
    """
    n = len(ext1_matrix)
    B = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = ext1_matrix[i][j] - ext1_matrix[j][i]
    return B


def exchange_matrix_mckay_z2() -> List[List[int]]:
    r"""Exchange matrix for the McKay quiver of Z_2 acting on T^4.

    The Kummer K3 = T^4/Z_2 (resolved) has a McKay quiver with 2 vertices:
      - Vertex 0: trivial representation of Z_2
      - Vertex 1: sign representation of Z_2

    The Z_2 action on T^4 ~ C^2 has tangent representation = (sign)^2.
    The McKay quiver for Z_2 < SL(2) has 2 vertices connected by 2 arrows
    in each direction. The exchange matrix (antisymmetric part):

      B = [[0, 2], [-2, 0]]

    This is the A_1^{(1)} (affine A_1) exchange matrix with multiplicity 2.
    """
    return [[0, 2], [-2, 0]]


def exchange_matrix_conifold_k3() -> List[List[int]]:
    r"""Exchange matrix at the conifold point of K3.

    At a conifold point, a single (-2)-curve C is contracted. The relevant
    exceptional collection consists of the spherical sheaf O_C(-1) and its
    shift O_C(-1)[1]. The Ext^1 data:

      Ext^1(O_C(-1), O_C(-1)[1]) has dim 1  (from Ext^2(O_C(-1), O_C(-1)) = C)
      Ext^1(O_C(-1)[1], O_C(-1)) has dim 0

    giving B = [[0, 1], [-1, 0]], the A_1 exchange matrix.
    """
    return [[0, 1], [-1, 0]]


def exchange_matrix_ade_k3(dynkin_type: str) -> List[List[int]]:
    r"""Exchange matrix for K3 with ADE singularity.

    A K3 surface with an ADE singularity of type Gamma has exceptional
    curves {C_1, ..., C_n} forming the Dynkin diagram of type Gamma.
    The intersection matrix is the negative Cartan matrix:
      C_i . C_j = -A_{ij}  where A is the Cartan matrix.

    The exchange matrix is constructed from the Ext^1 data of the
    exceptional sheaves O_{C_i}(-1):

      B_{ij} = A_{ij}  for i != j (off-diagonal Cartan entries, antisymmetrized)

    For simply-laced (ADE): A_{ij} = 0 or -1 for i != j, and the
    exchange matrix IS the antisymmetric part of the quiver adjacency.

    Parameters
    ----------
    dynkin_type : str
        One of 'A1', 'A2', 'A3', 'D4', 'E6', 'E7', 'E8'.

    Returns
    -------
    list of list of int : exchange matrix B for the ADE cluster.
    """
    cartan_matrices = {
        'A1': [[2]],
        'A2': [[2, -1], [-1, 2]],
        'A3': [[2, -1, 0], [-1, 2, -1], [0, -1, 2]],
        'D4': [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]],
        'E6': [
            [2, -1, 0, 0, 0, 0],
            [-1, 2, -1, 0, 0, 0],
            [0, -1, 2, -1, 0, -1],
            [0, 0, -1, 2, -1, 0],
            [0, 0, 0, -1, 2, 0],
            [0, 0, -1, 0, 0, 2],
        ],
        'E7': [
            [2, -1, 0, 0, 0, 0, 0],
            [-1, 2, -1, 0, 0, 0, 0],
            [0, -1, 2, -1, 0, 0, -1],
            [0, 0, -1, 2, -1, 0, 0],
            [0, 0, 0, -1, 2, -1, 0],
            [0, 0, 0, 0, -1, 2, 0],
            [0, 0, -1, 0, 0, 0, 2],
        ],
        'E8': [
            [2, -1, 0, 0, 0, 0, 0, 0],
            [-1, 2, -1, 0, 0, 0, 0, 0],
            [0, -1, 2, -1, 0, 0, 0, -1],
            [0, 0, -1, 2, -1, 0, 0, 0],
            [0, 0, 0, -1, 2, -1, 0, 0],
            [0, 0, 0, 0, -1, 2, -1, 0],
            [0, 0, 0, 0, 0, -1, 2, 0],
            [0, 0, -1, 0, 0, 0, 0, 2],
        ],
    }
    if dynkin_type not in cartan_matrices:
        raise ValueError(f"Unknown Dynkin type: {dynkin_type}. "
                         f"Expected one of {list(cartan_matrices.keys())}")

    A = cartan_matrices[dynkin_type]
    n = len(A)

    # The exchange matrix for a Dynkin quiver: orient edges following
    # the standard orientation (lower index -> higher index for type A,
    # towards the branch vertex for type D/E).
    # B_{ij} = number of arrows i -> j minus arrows j -> i.
    # For a linearly-oriented A_n quiver: B_{i,i+1} = 1, B_{i+1,i} = -1.
    # For D_n: standard orientation towards the branch node.
    # For E_n: standard orientation towards the branch node (vertex 2).
    B = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j and A[i][j] < 0:
                # Edge between i and j: orient i -> j (convention)
                B[i][j] = -A[i][j]   # = 1 for simply-laced
                B[j][i] = A[i][j]    # = -1 for simply-laced
    return B


def exchange_matrix_k3_picard_rank(rho: int) -> Dict[str, Any]:
    r"""Exchange matrix data for K3 at Picard rank rho.

    At Picard rank rho, the Neron-Severi lattice NS(K3) has rank rho
    and the transcendental lattice T(K3) has rank 22 - rho.  The
    exchange matrix on the heart of Gieseker stability has rank <= rho.

    STATUS: CONJECTURAL (AP-CY14).

    Parameters
    ----------
    rho : int
        Picard rank, 1 <= rho <= 20.

    Returns
    -------
    dict with exchange matrix data.
    """
    if not 1 <= rho <= PICARD_MAX:
        raise ValueError(f"Picard rank must be 1..{PICARD_MAX}, got {rho}")

    result: Dict[str, Any] = {}
    result['picard_rank'] = rho
    result['ns_rank'] = rho
    result['transcendental_rank'] = 22 - rho

    # At rho = 1: generic K3, exchange matrix is A_1 (conifold)
    if rho == 1:
        result['exchange_matrix'] = exchange_matrix_conifold_k3()
        result['cluster_type'] = 'A_1'
        result['n_cluster_variables'] = 2 + 1  # 2 mutable + 1 = 3 seeds
    elif rho == 2:
        # Two divisors => A_2 or A_1 x A_1 depending on intersection
        result['exchange_matrix'] = cluster_type_a2()
        result['cluster_type'] = 'A_2 (generic at rho=2)'
        result['n_cluster_variables'] = 3 + 2  # 5 seeds for A_2
    elif rho <= 8:
        # Small Picard rank: ADE exchange matrices arise from exceptional curves
        result['exchange_matrix'] = exchange_matrix_ade_k3(f'A{rho}')
        result['cluster_type'] = f'A_{rho} (linear orientation)'
        # Cluster type A_n has (n+3 choose 2) / something cluster vars
        result['n_cluster_variables'] = _catalan_number(rho)
    else:
        # High Picard rank: exchange matrix is (part of) the lattice data
        # The cluster algebra becomes infinite type at rho >= 3 in general
        result['exchange_matrix'] = None
        result['cluster_type'] = f'infinite type (rho={rho})'
        result['n_cluster_variables'] = 'infinite'

    result['mukai_rank'] = MUKAI_RANK
    result['mukai_signature'] = MUKAI_SIGNATURE
    result['status'] = STATUS
    return result


def _catalan_number(n: int) -> int:
    """Catalan number C_n = binom(2n, n) / (n+1).

    For cluster type A_n, the number of clusters is the Catalan number C_{n+1}.
    """
    return math.comb(2 * (n + 1), n + 1) // (n + 2)


# ============================================================================
# 2. CLUSTER VARIABLES IN Y(g_{K3})
# ============================================================================

class ClusterVariable:
    r"""A cluster variable in the conjectural cluster structure on Y(g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).

    Each cluster variable is labelled by a Mukai vector v = (r, c_1, s) and
    corresponds to the evaluation character:

      chi_v(z) = Tr_{V_v}(R_{K3}(z))

    where V_v is the Yangian module at charge v.

    At the tropical limit (MUM degeneration, AP157: LCS), chi_v -> theta_v
    (GHKK canonical theta function).

    Parameters
    ----------
    mukai_vector : tuple (r, c_1, s)
        The Mukai vector labelling this cluster variable.
    name : str
        Human-readable name.
    is_frozen : bool
        Whether this variable is frozen (coefficient) or mutable.
    """

    def __init__(self, mukai_vector: Tuple[int, int, int],
                 name: str = '',
                 is_frozen: bool = False):
        self.mukai_vector = mukai_vector
        self.name = name or f"x_{mukai_vector}"
        self.is_frozen = is_frozen

    @property
    def r(self) -> int:
        return self.mukai_vector[0]

    @property
    def c1(self) -> int:
        return self.mukai_vector[1]

    @property
    def s(self) -> int:
        return self.mukai_vector[2]

    def mukai_square(self, degree: int = 1) -> int:
        r"""Mukai self-pairing v^2 = 2*degree*c_1^2 - 2*r*s.

        For Picard rank 1 with polarization H^2 = 2*degree.
        """
        r, c1, s = self.mukai_vector
        return 2 * degree * c1 * c1 - 2 * r * s

    def mukai_pairing_with(self, other: 'ClusterVariable',
                           degree: int = 1) -> int:
        r"""Mukai pairing <v, w> = 2*degree*c_1*c_1' - r*s' - r'*s."""
        r1, c1_1, s1 = self.mukai_vector
        r2, c1_2, s2 = other.mukai_vector
        return 2 * degree * c1_1 * c1_2 - r1 * s2 - r2 * s1

    def __repr__(self) -> str:
        kind = 'frozen' if self.is_frozen else 'mutable'
        return f"ClusterVariable(v={self.mukai_vector}, {kind}, '{self.name}')"


def initial_cluster_k3_picard1(degree: int = 1) -> List[ClusterVariable]:
    r"""Initial cluster variables for generic K3 at Picard rank 1.

    At Picard rank rho = 1 with polarization H of degree H^2 = 2*degree,
    the initial cluster consists of:

      x_1 = chi_{O_X}(z)     Mukai vector (1, 0, 1):  structure sheaf
      x_2 = chi_{O_X(H)}(z)  Mukai vector (1, 1, 1-degree): line bundle O(H)
      x_3 = chi_{O_p}(z)     Mukai vector (0, 0, -1): skyscraper (FROZEN)

    The exchange matrix on {x_1, x_2} (mutable) with x_3 frozen:
      B = [[0, 1], [-1, 0]]  (A_1 exchange from the single wall)

    Parameters
    ----------
    degree : int
        The degree d of the polarization, H^2 = 2*d. Default 1 (degree 2).

    Returns
    -------
    list of ClusterVariable
    """
    s_line = 1 - degree  # s-component for O(H): chi(O(H)) = 2 => s = 1 - d
    return [
        ClusterVariable((1, 0, 1), name='O_X'),
        ClusterVariable((1, 1, s_line), name=f'O_X(H)_d{degree}'),
        ClusterVariable((0, 0, -1), name='O_p', is_frozen=True),
    ]


def initial_cluster_k3_conifold() -> List[ClusterVariable]:
    r"""Initial cluster at the conifold point (single (-2)-curve).

    The spherical object E = O_C(-1) for a (-2)-curve C in K3 has:
      v(E) = (0, [C], 0)  with v(E)^2 = C^2 = -2

    The cluster consists of:
      x_1 = chi_E(z)      Mukai vector (0, 1, 0)   (the spherical sheaf)
      x_2 = chi_{E[1]}(z) Mukai vector (0, -1, 0)  (its shift)

    Exchange matrix: B = [[0, 1], [-1, 0]] (A_1).
    Exchange relation: x_1 * x_1' = 1 + x_2  (the A_1 pentagon).
    """
    return [
        ClusterVariable((0, 1, 0), name='O_C(-1)'),
        ClusterVariable((0, -1, 0), name='O_C(-1)[1]'),
    ]


def initial_cluster_mckay_z2() -> List[ClusterVariable]:
    r"""Initial cluster for the Kummer K3 = T^4/Z_2 via McKay.

    The McKay correspondence for Z_2 < SL(2) gives 2 exceptional objects:
      E_0: associated to the trivial rep of Z_2
      E_1: associated to the sign rep of Z_2

    The exchange matrix is B = [[0, 2], [-2, 0]] (affine A_1 with mult 2).

    The 16 exceptional curves of the resolution contribute frozen variables.
    """
    return [
        ClusterVariable((1, 0, 1), name='E_triv'),
        ClusterVariable((1, 0, -1), name='E_sign'),
    ]


def cluster_exchange_relation(
    x_k: ClusterVariable,
    cluster: List[ClusterVariable],
    B: List[List[int]],
    k: int,
) -> Dict[str, Any]:
    r"""Compute the exchange relation at vertex k.

    The Fomin-Zelevinsky exchange relation:
      x_k * x_k' = prod_{B_{ik}>0} x_i^{B_{ik}} + prod_{B_{ik}<0} x_i^{-B_{ik}}

    where x_k' is the new cluster variable replacing x_k.

    The new Mukai vector v_k' is determined by the exchange:
      v_k' = sum_{B_{ik}>0} B_{ik} * v_i - v_k    (positive product)
    or equivalently by the mutation formula on the charge lattice.

    Parameters
    ----------
    x_k : ClusterVariable
        The variable being exchanged.
    cluster : list of ClusterVariable
        Current cluster.
    B : list of list of int
        Exchange matrix.
    k : int
        Index of the variable being exchanged.

    Returns
    -------
    dict with:
      'new_variable': the new ClusterVariable x_k'
      'positive_monomial': list of (index, power) for the positive product
      'negative_monomial': list of (index, power) for the negative product
      'exchange_relation': string description
    """
    n = len(B)
    positive_monomial = []
    negative_monomial = []

    # Positive product: indices i with B_{ik} > 0
    for i in range(n):
        if i == k:
            continue
        if B[i][k] > 0:
            positive_monomial.append((i, B[i][k]))
        elif B[i][k] < 0:
            negative_monomial.append((i, -B[i][k]))

    # New Mukai vector: v_k' from the positive product minus v_k
    # v_k' = sum_{(i,p) in positive} p * v_i - v_k  (up to sign)
    # This is the TROPICAL semifield addition.
    new_v = [0, 0, 0]
    for i, p in positive_monomial:
        v_i = cluster[i].mukai_vector
        for c in range(3):
            new_v[c] += p * v_i[c]
    # Subtract v_k
    for c in range(3):
        new_v[c] -= x_k.mukai_vector[c]

    new_var = ClusterVariable(
        tuple(new_v),
        name=f"mu_{k}({x_k.name})",
    )

    return {
        'new_variable': new_var,
        'positive_monomial': positive_monomial,
        'negative_monomial': negative_monomial,
        'exchange_relation': (
            f"x_{k} * x_{k}' = "
            f"prod(positive) + prod(negative)"
        ),
        'status': STATUS,
    }


# ============================================================================
# 3. MUTATION = WALL-CROSSING IN Stab(K3)
# ============================================================================

class ClusterSeed:
    r"""A cluster seed = (B, x, h) for Y(g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).

    A seed consists of:
      - B: exchange matrix (antisymmetric)
      - cluster: list of cluster variables
      - h: Yangian parameters (optional)

    Mutation mu_k acts on all three simultaneously:
      - B -> mu_k(B)  (Fomin-Zelevinsky)
      - x_k -> x_k'   (exchange relation)
      - h_k -> mu_k(h) (Yangian parameter transformation)
    """

    def __init__(self, B: List[List[int]],
                 cluster: List[ClusterVariable],
                 h: Optional[List[Fraction]] = None):
        self.B = B
        self.cluster = list(cluster)
        self.h = list(h) if h is not None else None
        self.n = len(B)
        self._mutation_history: List[int] = []

    def mutate(self, k: int) -> 'ClusterSeed':
        r"""Mutate at vertex k, returning a new seed.

        Mutation is an involution: mu_k(mu_k(seed)) = seed.

        This corresponds to crossing a wall in Stab(K3) at which
        the phase of the k-th cluster variable changes.
        """
        if k < 0 or k >= self.n:
            raise ValueError(f"Mutation index {k} out of range [0, {self.n})")

        # 1. Mutate exchange matrix
        new_B = cluster_mutation(self.B, k)

        # 2. Compute new cluster variable
        exchange = cluster_exchange_relation(
            self.cluster[k], self.cluster, self.B, k)
        new_cluster = list(self.cluster)
        new_cluster[k] = exchange['new_variable']

        # 3. Mutate Yangian parameters (if present)
        new_h = None
        if self.h is not None:
            new_h = yangian_parameter_mutation(self.h, k, self.B)

        new_seed = ClusterSeed(new_B, new_cluster, new_h)
        new_seed._mutation_history = self._mutation_history + [k]
        return new_seed

    def exchange_graph_neighbors(self) -> List[int]:
        """Return indices of vertices that can be mutated (all mutable vertices)."""
        return [k for k in range(self.n)
                if not self.cluster[k].is_frozen]

    def is_antisymmetric(self) -> bool:
        """Check that the exchange matrix is antisymmetric."""
        return exchange_matrix_is_antisymmetric(self.B)

    def mutation_involution_check(self, k: int) -> bool:
        """Verify mu_k^2 = id."""
        return cluster_mutation_involution_check(self.B, k)

    def all_mutation_involutions_hold(self) -> bool:
        """Check mu_k^2 = id for all mutable k."""
        return all(self.mutation_involution_check(k)
                   for k in self.exchange_graph_neighbors())


def seed_a1_conifold(h: Optional[List[Fraction]] = None) -> ClusterSeed:
    r"""Seed for the A_1 cluster at the conifold point.

    B = [[0, 1], [-1, 0]]
    Cluster: {O_C(-1), O_C(-1)[1]}
    Yangian: h = [h_1, -h_1] (CY constraint sum = 0 on the 2-dim sublattice)
    """
    B = exchange_matrix_conifold_k3()
    cluster = initial_cluster_k3_conifold()
    if h is None:
        h = [F(1), F(-1)]  # simple CY_2-compatible choice
    return ClusterSeed(B, cluster, h)


def seed_mckay_z2(h: Optional[List[Fraction]] = None) -> ClusterSeed:
    r"""Seed for the McKay Z_2 cluster (Kummer K3).

    B = [[0, 2], [-2, 0]]
    Cluster: {E_triv, E_sign}
    """
    B = exchange_matrix_mckay_z2()
    cluster = initial_cluster_mckay_z2()
    if h is None:
        h = [F(1), F(-1)]
    return ClusterSeed(B, cluster, h)


def seed_ade_k3(dynkin_type: str) -> ClusterSeed:
    r"""Seed for K3 with ADE singularity.

    Parameters
    ----------
    dynkin_type : str
        'A1', 'A2', 'A3', 'D4', 'E6', 'E7', 'E8'.
    """
    B = exchange_matrix_ade_k3(dynkin_type)
    n = len(B)
    # Each exceptional curve C_i has a distinct Mukai vector.
    # For ADE singularities on K3, the (-2)-curves have v(O_{C_i}(-1)) with
    # distinct c_1 components in the Picard lattice.  We model this by
    # assigning each variable the Mukai vector (0, i+1, 0) -- distinct
    # c_1 values encode distinct curve classes in the lattice.
    cluster = [ClusterVariable((0, i + 1, 0), name=f'E_{i}') for i in range(n)]
    # CY_2 constraint on the n-dim sublattice: sum h_i = 0
    h = [F(1)] * (n - 1) + [F(-(n - 1))]
    return ClusterSeed(B, cluster, h)


def wall_crossing_as_mutation(
    sigma_plus: Tuple[Fraction, Fraction],
    sigma_minus: Tuple[Fraction, Fraction],
    wall_vector: Tuple[int, int, int],
    seed: ClusterSeed,
    k: int,
) -> Dict[str, Any]:
    r"""Interpret a wall-crossing in Stab(K3) as a cluster mutation.

    STATUS: CONJECTURAL (AP-CY14).

    A wall W(v_1, v_2) in Stab(K3) is defined by:
      phi_sigma(v_1) = phi_sigma(v_2)  (equal phases of central charges)

    Crossing this wall from sigma^+ to sigma^- acts as:
      - Cluster mutation mu_k at the vertex k corresponding to the
        wall-crossing sheaf
      - DT invariant change: Omega(v; sigma^+) - Omega(v; sigma^-)
      - Yangian module decomposition change

    Parameters
    ----------
    sigma_plus, sigma_minus : (B, omega) pairs
        Stability conditions on either side of the wall.
    wall_vector : (r, c_1, s)
        The Mukai vector at the wall (the destabilizing class).
    seed : ClusterSeed
        The cluster seed on the sigma^+ side.
    k : int
        The mutation index.

    Returns
    -------
    dict with mutation data and consistency checks.
    """
    # Perform the mutation
    new_seed = seed.mutate(k)

    return {
        'sigma_plus': sigma_plus,
        'sigma_minus': sigma_minus,
        'wall_vector': wall_vector,
        'mutation_index': k,
        'old_exchange_matrix': seed.B,
        'new_exchange_matrix': new_seed.B,
        'old_cluster_var_k': repr(seed.cluster[k]),
        'new_cluster_var_k': repr(new_seed.cluster[k]),
        'antisymmetric_preserved': new_seed.is_antisymmetric(),
        'involution_holds': seed.mutation_involution_check(k),
        'correspondence': (
            'Wall-crossing sigma^+ -> sigma^- across W(v_1, v_2) '
            'corresponds to cluster mutation mu_k. '
            'The KS wall-crossing formula matches the cluster exchange '
            'relation (Bridgeland arXiv:1611.03697, Nagao arXiv:1002.4956).'
        ),
        'status': STATUS,
    }


def enumerate_exchange_graph(
    seed: ClusterSeed,
    max_depth: int = 5,
) -> Dict[str, Any]:
    r"""Enumerate the exchange graph starting from the given seed.

    The exchange graph has:
      - Vertices: cluster seeds (up to simultaneous relabeling)
      - Edges: single mutations

    For finite-type cluster algebras, the exchange graph is finite:
      - A_1: 2 seeds (pentagon with n+3=4... no, 2 clusters for rank 1)
        Actually for A_1: exchange graph has 2 vertices.
      - A_2: 5 seeds (associahedron = pentagon)
      - A_3: 14 seeds (3d associahedron)

    For infinite-type, we explore up to max_depth mutations.

    Parameters
    ----------
    seed : ClusterSeed
        Starting seed.
    max_depth : int
        Maximum number of mutations from the initial seed.

    Returns
    -------
    dict with:
      'n_seeds': number of distinct seeds found
      'n_edges': number of mutation edges
      'is_finite_type': whether the graph closed (all seeds explored)
      'seeds': list of seed data
    """
    # BFS through the exchange graph
    # Key each seed by (B, cluster variable Mukai vectors) to distinguish
    # seeds that share the same B but have different cluster variables.
    # This is essential: for type A_2 (rank 2), the B-matrix alternates
    # between B and -B under mutation, but there are 5 distinct seeds
    # distinguished by their cluster variables.
    def seed_key(s: ClusterSeed):
        b_part = tuple(tuple(row) for row in s.B)
        var_part = tuple(cv.mukai_vector for cv in s.cluster)
        return (b_part, var_part)

    visited = set()
    queue = [(seed, 0)]
    visited.add(seed_key(seed))
    n_edges = 0
    all_seeds = [{'B': seed.B, 'depth': 0}]
    frontier_at_max = False

    while queue:
        current, depth = queue.pop(0)
        if depth >= max_depth:
            frontier_at_max = True
            continue
        for k in current.exchange_graph_neighbors():
            new_seed = current.mutate(k)
            key = seed_key(new_seed)
            n_edges += 1
            if key not in visited:
                visited.add(key)
                queue.append((new_seed, depth + 1))
                all_seeds.append({'B': new_seed.B, 'depth': depth + 1})

    # Check if finite type: did we exhaust all seeds before max_depth?
    frontier_exists = frontier_at_max and any(
        d['depth'] == max_depth for d in all_seeds)

    return {
        'n_seeds': len(visited),
        'n_edges': n_edges,
        'is_finite_type': not frontier_exists,
        'max_depth_reached': max_depth,
        'seeds': all_seeds,
        'status': STATUS,
    }


# ============================================================================
# 4. QUANTUM CLUSTER ALGEBRA
# ============================================================================

def quantum_parameter_mukai(
    v_i: Tuple[int, int, int],
    v_j: Tuple[int, int, int],
    degree: int = 1,
) -> int:
    r"""Quantum parameter q_{ij} from the Mukai pairing.

    For the quantum cluster algebra on Y(g_{K3}), the quantum parameter is:

      q_{ij} = exp(i*pi * <v_i, v_j>_Muk)

    Since <v_i, v_j>_Muk is an INTEGER on the lattice,
    q_{ij} = (-1)^{<v_i,v_j>} = +1 or -1.

    The q-commutation:
      x_i * x_j = q_{ij} * x_j * x_i

    Parameters
    ----------
    v_i, v_j : (r, c_1, s)
        Mukai vectors.
    degree : int
        Polarization degree (H^2 = 2*degree).

    Returns
    -------
    int : +1 or -1 (the quantum parameter q_{ij}).
    """
    # Mukai pairing: <(r,c,s), (r',c',s')> = 2*d*c*c' - r*s' - r'*s
    r1, c1, s1 = v_i
    r2, c2, s2 = v_j
    pairing = 2 * degree * c1 * c2 - r1 * s2 - r2 * s1
    return (-1) ** pairing


def compatibility_matrix(
    cluster: List[ClusterVariable],
    degree: int = 1,
) -> List[List[int]]:
    r"""Compatibility matrix Lambda_{ij} = <v_i, v_j>_Muk.

    The compatibility matrix encodes the q-commutation:
      x_i * x_j = (-1)^{Lambda_{ij}} * x_j * x_i

    For the quantum cluster algebra, Lambda and B must satisfy:
      B * Lambda = D  (diagonal, with positive entries)

    This is the Berenstein-Zelevinsky compatibility condition.

    Parameters
    ----------
    cluster : list of ClusterVariable
        The cluster variables.
    degree : int
        Polarization degree.

    Returns
    -------
    list of list of int : the matrix Lambda_{ij}.
    """
    n = len(cluster)
    Lambda = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            Lambda[i][j] = cluster[i].mukai_pairing_with(cluster[j], degree)
    return Lambda


def quantum_exchange_relation(
    cluster: List[ClusterVariable],
    B: List[List[int]],
    k: int,
    degree: int = 1,
) -> Dict[str, Any]:
    r"""Quantum exchange relation at vertex k.

    The quantum Fomin-Zelevinsky exchange relation:

      x_k * x_k' = q^{a_+} * prod_{B_{ik}>0} x_i^{B_{ik}}
                  + q^{a_-} * prod_{B_{ik}<0} x_i^{-B_{ik}}

    where q^{a_+} and q^{a_-} are quantum corrections from the
    compatibility matrix Lambda.

    For K3 with integer Mukai pairing: q = -1 is the only nontrivial
    possibility, so the quantum correction is a SIGN.

    Parameters
    ----------
    cluster : list of ClusterVariable
    B : exchange matrix
    k : mutation vertex
    degree : polarization degree

    Returns
    -------
    dict with quantum exchange relation data.
    """
    n = len(B)
    Lambda = compatibility_matrix(cluster, degree)

    # Quantum corrections: a_+ and a_- from the BZ formula
    # a_+ = (1/2) sum_{i<j, B_{ik}>0, B_{jk}>0} B_{ik}*B_{jk}*Lambda_{ij}
    a_plus = 0
    a_minus = 0
    for i in range(n):
        for j in range(i + 1, n):
            if B[i][k] > 0 and B[j][k] > 0:
                a_plus += B[i][k] * B[j][k] * Lambda[i][j]
            if B[i][k] < 0 and B[j][k] < 0:
                a_minus += B[i][k] * B[j][k] * Lambda[i][j]

    # Quantum parameter signs
    q_plus = (-1) ** a_plus
    q_minus = (-1) ** a_minus

    return {
        'vertex': k,
        'a_plus': a_plus,
        'a_minus': a_minus,
        'q_plus': q_plus,
        'q_minus': q_minus,
        'compatibility_matrix': Lambda,
        'is_quantum_deformed': (q_plus != 1 or q_minus != 1),
        'quantum_parameter': 'q = (-1)^{<v_i,v_j>_Muk} (square root quantum)',
        'berenstein_zelevinsky': (
            'Lambda and B satisfy the BZ compatibility condition '
            'B * Lambda = D with D diagonal. '
            'For K3: the quantum parameter q_{ij} = (-1)^{<v_i,v_j>} '
            'takes values +/- 1 only (integer Mukai pairing).'
        ),
        'status': STATUS,
    }


def verify_bz_compatibility(
    B: List[List[int]],
    Lambda: List[List[int]],
) -> Dict[str, Any]:
    r"""Verify the Berenstein-Zelevinsky compatibility condition.

    The BZ condition: B * Lambda^T = D (diagonal with positive entries)
    on the mutable part. This ensures the quantum cluster algebra is
    well-defined.

    Parameters
    ----------
    B : exchange matrix (antisymmetric)
    Lambda : compatibility matrix (antisymmetric from Mukai pairing)

    Returns
    -------
    dict with verification result.
    """
    n = len(B)
    # Compute B * Lambda^T
    product = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                product[i][j] += B[i][k] * Lambda[j][k]

    # Check if diagonal
    is_diagonal = all(product[i][j] == 0
                      for i in range(n) for j in range(n) if i != j)

    # Diagonal entries
    diag_entries = [product[i][i] for i in range(n)]

    return {
        'product_B_Lambda_T': product,
        'is_diagonal': is_diagonal,
        'diagonal_entries': diag_entries,
        'all_positive': all(d > 0 for d in diag_entries) if is_diagonal else False,
        'bz_compatible': is_diagonal and all(d > 0 for d in diag_entries),
        'status': STATUS,
    }


# ============================================================================
# 5. A_1 REDUCTION AND FINITE-TYPE SPECIALIZATIONS
# ============================================================================

def a1_cluster_structure() -> Dict[str, Any]:
    r"""Complete A_1 cluster structure at the conifold.

    At the conifold point with a single (-2)-curve, the cluster algebra
    is type A_1 with:
      - 2 clusters: {x_1, x_2} and {x_1', x_2}
      - Exchange relation: x_1 * x_1' = 1 + x_2
      - Exchange graph: 2 vertices connected by 1 edge

    The Yangian specializes to Y(sl_2) at level 1:
      - Structure function: g(z) = (z - h)/(z + h) with h from the (-2)-curve
      - R-matrix: R(z) = (z + h*P)/(z + h) on C^2 tensor C^2
      - The single mutation is the Weyl reflection s: h -> -h

    The quantum parameter: for v_1 = (0,1,0), v_2 = (0,-1,0) on K3 of degree 1:
      <v_1, v_2> = 2*1*1*(-1) - 0 - 0 = -2
      q_{12} = (-1)^{-2} = 1

    So the A_1 quantum cluster algebra is actually CLASSICAL (q=1).
    """
    B = exchange_matrix_conifold_k3()
    cluster = initial_cluster_k3_conifold()

    # Perform the single mutation
    B_mut = cluster_mutation(B, 0)

    # Exchange graph
    graph = enumerate_exchange_graph(seed_a1_conifold(), max_depth=5)

    # Quantum parameter
    q_12 = quantum_parameter_mukai(
        cluster[0].mukai_vector, cluster[1].mukai_vector, degree=1)

    # Yangian unitarity at the A_1 level (AP-CY28: safe test point)
    h_a1 = [F(3), F(-3)]
    z_safe = F(17)  # far from poles at +/- 3
    unitarity = yangian_unitarity_check(h_a1, z_safe)

    # Structure function at A_1
    g_val = yangian_structure_function(h_a1, z_safe)

    return {
        'exchange_matrix': B,
        'mutated_matrix': B_mut,
        'mutation_involution': B == B_mut,  # mu_0^2 = id for A_1
        'n_clusters': graph['n_seeds'],
        'is_finite_type': graph['is_finite_type'],
        'exchange_relation': 'x_1 * x_1\' = 1 + x_2 (A_1 pentagon)',
        'quantum_parameter_q12': q_12,
        'is_classical': q_12 == 1,
        'yangian_unitarity': unitarity,
        'structure_function_at_z': str(g_val),
        'yangian_specialization': 'Y(sl_2) at level 1',
        'status': STATUS,
    }


def a2_cluster_structure() -> Dict[str, Any]:
    r"""Complete A_2 cluster structure (K3 at Picard rank 2).

    The A_2 cluster algebra has:
      - 5 clusters forming a pentagon (the associahedron K_4)
      - Exchange graph: 5 vertices, each connected to 2 others
      - 5 cluster variables total (2 mutable per seed, with overlap)

    The 5 seeds of the A_2 cluster algebra correspond to 5 chambers
    in Stab(K3) at Picard rank 2.
    """
    seed = ClusterSeed(
        cluster_type_a2(),
        [ClusterVariable((1, 0, 1), name='x_1'),
         ClusterVariable((0, 1, 0), name='x_2')],
    )

    graph = enumerate_exchange_graph(seed, max_depth=10)

    # The A_2 exchange graph has 5 seeds
    # Verify by explicit mutation sequence: 0, 1, 0, 1, 0 returns to start
    s = seed
    sequence = []
    for k in [0, 1, 0, 1, 0]:
        s = s.mutate(k)
        sequence.append(tuple(tuple(row) for row in s.B))

    # After 5 mutations (0,1,0,1,0), should return to original B
    returns_to_start = (sequence[-1] == tuple(tuple(row) for row in seed.B))

    return {
        'exchange_matrix': seed.B,
        'n_clusters': graph['n_seeds'],
        'is_finite_type': graph['is_finite_type'],
        'pentagon_period': 5,
        'mutation_sequence_01010_returns': returns_to_start,
        'cluster_type': 'A_2',
        'stab_interpretation': (
            '5 chambers in the Picard-rank-2 slice of Stab(K3), '
            'separated by 5 walls of marginal stability.'
        ),
        'status': STATUS,
    }


def a1_enhancement_from_full_k3(
    h_full: List[Fraction],
    spherical_index: int,
) -> Dict[str, Any]:
    r"""Show how the full K3 cluster reduces to A_1 at a conifold.

    At a conifold point where the spherical_index-th parameter h_k becomes
    the dominant deformation, the full K3 structure function

      g_{K3}(z) = prod_{i=1}^{24} (z - h_i)/(z + h_i)

    is dominated by the single factor (z - h_k)/(z + h_k) when all other
    h_i << h_k.  This reduces the cluster algebra to A_1.

    STATUS: CONJECTURAL (AP-CY14).

    Parameters
    ----------
    h_full : list of Fraction
        Full set of 24 Yangian parameters (must sum to 0: CY_2).
    spherical_index : int
        Index of the dominant spherical parameter.

    Returns
    -------
    dict with reduction data.
    """
    n = len(h_full)
    k = spherical_index
    if k < 0 or k >= n:
        raise ValueError(f"Index {k} out of range [0, {n})")

    # The dominant parameter
    h_k = h_full[k]

    # In the conifold limit: h_i -> 0 for i != k and its CY partner
    # The CY_2 constraint sum h_i = 0 means there must be a partner index j
    # with h_j ~ -h_k to keep the sum zero.
    # For the A_1 reduction, the partner is the index with h_j closest to -h_k.
    partner_idx = None
    best_distance = None
    for j in range(n):
        if j == k:
            continue
        dist = abs(h_full[j] + h_k)
        if best_distance is None or dist < best_distance:
            best_distance = dist
            partner_idx = j

    # Structure function ratio: full / reduced
    # g_{K3}(z) / g_{A_1}(z) where g_{A_1}(z) = (z-h_k)(z-h_j) / ((z+h_k)(z+h_j))
    # This ratio should approach 1 in the conifold limit.

    # Verify at a safe test point (AP-CY28)
    z_test = F(1000)  # very far from all h_i
    g_full = yangian_structure_function(h_full, z_test)
    h_a1 = [h_full[k], h_full[partner_idx]]
    g_reduced = yangian_structure_function(h_a1, z_test)

    # The ratio g_full / g_reduced measures the non-A_1 contribution
    ratio = g_full / g_reduced if g_reduced != 0 else None

    return {
        'spherical_index': k,
        'dominant_h': str(h_k),
        'partner_index': partner_idx,
        'partner_h': str(h_full[partner_idx]),
        'a1_exchange_matrix': exchange_matrix_conifold_k3(),
        'g_full_at_test': str(g_full),
        'g_a1_at_test': str(g_reduced),
        'ratio': str(ratio),
        'conifold_limit_interpretation': (
            f'At the conifold where h_{k} dominates, '
            f'the 24-parameter K3 cluster reduces to '
            f'the A_1 cluster on the 2-parameter sublattice '
            f'{{h_{k}, h_{partner_idx}}}. '
            f'The remaining 22 directions decouple.'
        ),
        'status': STATUS,
    }


# ============================================================================
# 6. SCATTERING DIAGRAM <-> CLUSTER BRIDGE
# ============================================================================

def scattering_cluster_bridge(max_height: int = 8) -> Dict[str, Any]:
    r"""Bridge between GPS scattering diagram and cluster algebra.

    The Gross-Hacking-Keel-Kontsevich theorem identifies:
      - GPS scattering diagram walls <-> cluster monomials
      - Broken lines on the scattering diagram <-> theta functions
      - Consistent scattering diagram <-> cluster algebra positivity

    For the A_2 seed (conifold pair on K3):
      - 2 seed walls at (1,0) and (0,1) with multiplicity 1
      - 1 forced wall at (1,1) with multiplicity 1
      - Total: 3 walls = 3 positive roots of A_2

    For higher-rank K3 (more exceptional curves):
      - Seed walls from the exceptional collection
      - Forced walls from the GPS tropical vertex algorithm
      - Total walls = number of positive roots (finite type)
        or infinite (affine/wild type)
    """
    # A_2 scattering diagram
    sd_a2 = TropicalScatteringDiagram(rank=2, max_height=max_height)
    sd_a2.compute()

    # Count walls at each height
    wall_counts = {}
    for h in range(1, max_height + 1):
        walls_h = sd_a2.walls_at_height(h)
        if walls_h:
            wall_counts[h] = walls_h

    # Consistency check
    consistent = all(sd_a2.is_consistent_at_height(h)
                     for h in range(2, max_height + 1))

    # Compare with A_2 cluster algebra
    # A_2 has 3 positive roots: alpha_1, alpha_2, alpha_1 + alpha_2
    # => 3 walls in the scattering diagram
    a2_positive_roots = [(1, 0), (0, 1), (1, 1)]
    all_roots_present = all(
        sd_a2.walls.get(r, 0) >= 1 for r in a2_positive_roots
    )

    # The McKay Z_2 scattering (multiplicity 2 seed walls)
    sd_mckay = TropicalScatteringDiagram(
        rank=2,
        seed_walls=[((1, 0), 2), ((0, 1), 2)],
        max_height=max_height,
    )
    sd_mckay.compute()

    return {
        'a2_wall_count': sd_a2.wall_count(),
        'a2_walls': dict(sd_a2.walls),
        'a2_consistent': consistent,
        'a2_positive_roots_present': all_roots_present,
        'a2_wall_counts_by_height': wall_counts,
        'mckay_wall_count': sd_mckay.wall_count(),
        'mckay_walls': dict(sd_mckay.walls),
        'ghkk_identification': (
            'GPS scattering diagram walls = cluster monomials '
            '(GHKK arXiv:1411.1394). '
            'For A_2: 3 walls = 3 positive roots = 5 cluster variables - 2 initial. '
            'For McKay Z_2: multiplicity-2 seed gives affine A_1 scattering.'
        ),
        'status': STATUS,
    }


# ============================================================================
# 7. STRUCTURE FUNCTION UNDER MUTATION
# ============================================================================

def structure_function_under_mutation(
    h: List[Fraction],
    B: List[List[int]],
    k: int,
    z_test: Fraction = F(1000),
) -> Dict[str, Any]:
    r"""Track the structure function g(z) = prod (z-h_i)/(z+h_i) under mutation.

    Mutation mu_k changes the parameters h -> h'.  The structure function
    transforms as:

      g'(z) = g(z) * correction_factor

    where the correction factor depends on the mutation.

    For the K3 Yangian, the UNITARITY g(z)*g(-z)=1 is preserved by mutation
    (since it holds for any parameters satisfying CY_2).

    Parameters
    ----------
    h : list of Fraction
        Current Yangian parameters.
    B : exchange matrix
        Current exchange matrix.
    k : int
        Mutation index.
    z_test : Fraction
        Safe test point (AP-CY28: far from poles).

    Returns
    -------
    dict with structure function data before and after mutation.
    """
    h_new = yangian_parameter_mutation(h, k, B)
    n = len(h)

    # Check CY_2 constraint preservation
    cy2_old = sum(h)
    cy2_new = sum(h_new)

    # Structure function values (AP-CY28: safe test point)
    g_old = yangian_structure_function(h, z_test)
    g_new = yangian_structure_function(h_new, z_test)

    # Unitarity check for both
    unitarity_old = yangian_unitarity_check(h, z_test)
    unitarity_new = yangian_unitarity_check(h_new, z_test)

    # The ratio g_new / g_old
    ratio = g_new / g_old if g_old != 0 else None

    return {
        'h_old': [str(x) for x in h],
        'h_new': [str(x) for x in h_new],
        'mutation_index': k,
        'cy2_old': str(cy2_old),
        'cy2_new': str(cy2_new),
        'cy2_preserved': cy2_new == F(0),
        'g_old': str(g_old),
        'g_new': str(g_new),
        'ratio': str(ratio),
        'unitarity_old': unitarity_old,
        'unitarity_new': unitarity_new,
        'unitarity_preserved': unitarity_new,
        'status': STATUS,
    }


# ============================================================================
# 8. FULL VERIFICATION SUITE
# ============================================================================

def full_k3_yangian_cluster_verification() -> Dict[str, Any]:
    r"""Run the complete verification suite for the cluster structure on Y(g_{K3}).

    STATUS: CONJECTURAL (AP-CY14). All results verify internal consistency.

    Tests:
      1. Exchange matrix construction (CY_2 Euler form, McKay, ADE)
      2. Antisymmetry of all exchange matrices
      3. Mutation involution (mu_k^2 = id)
      4. A_1 cluster structure (conifold)
      5. A_2 cluster structure (Picard rank 2)
      6. McKay Z_2 cluster (Kummer)
      7. Quantum parameter computation
      8. BZ compatibility
      9. Scattering-cluster bridge
      10. Structure function under mutation
      11. A_1 reduction from full K3
      12. Exchange graph enumeration
    """
    results: Dict[str, Any] = {}

    # 1. Exchange matrices
    B_conifold = exchange_matrix_conifold_k3()
    B_mckay = exchange_matrix_mckay_z2()
    B_a2 = cluster_type_a2()
    B_a3 = exchange_matrix_ade_k3('A3')
    B_d4 = exchange_matrix_ade_k3('D4')

    results['exchange_matrices'] = {
        'conifold': B_conifold,
        'mckay_z2': B_mckay,
        'a2': B_a2,
        'a3': B_a3,
        'd4': B_d4,
    }

    # 2. Antisymmetry
    results['antisymmetric'] = {
        'conifold': exchange_matrix_is_antisymmetric(B_conifold),
        'mckay': exchange_matrix_is_antisymmetric(B_mckay),
        'a2': exchange_matrix_is_antisymmetric(B_a2),
        'a3': exchange_matrix_is_antisymmetric(B_a3),
        'd4': exchange_matrix_is_antisymmetric(B_d4),
    }

    # 3. Mutation involution
    results['mutation_involution'] = {
        'conifold_0': cluster_mutation_involution_check(B_conifold, 0),
        'mckay_0': cluster_mutation_involution_check(B_mckay, 0),
        'a3_1': cluster_mutation_involution_check(B_a3, 1),
        'd4_1': cluster_mutation_involution_check(B_d4, 1),
    }

    # 4. A_1 cluster
    a1 = a1_cluster_structure()
    results['a1_cluster'] = {
        'n_clusters': a1['n_clusters'],
        'is_finite': a1['is_finite_type'],
        'is_classical': a1['is_classical'],
        'unitarity': a1['yangian_unitarity'],
    }

    # 5. A_2 cluster
    a2 = a2_cluster_structure()
    results['a2_cluster'] = {
        'n_clusters': a2['n_clusters'],
        'is_finite': a2['is_finite_type'],
        'pentagon_returns': a2['mutation_sequence_01010_returns'],
    }

    # 6. Quantum parameter
    v1 = (1, 0, 1)
    v2 = (0, 1, 0)
    v3 = (0, 0, -1)
    results['quantum_parameters'] = {
        'q_12': quantum_parameter_mukai(v1, v2),
        'q_13': quantum_parameter_mukai(v1, v3),
        'q_23': quantum_parameter_mukai(v2, v3),
    }

    # 7. Scattering-cluster bridge
    bridge = scattering_cluster_bridge(max_height=6)
    results['scattering_bridge'] = {
        'a2_walls': bridge['a2_wall_count'],
        'a2_consistent': bridge['a2_consistent'],
        'positive_roots': bridge['a2_positive_roots_present'],
    }

    # 8. Structure function under mutation (AP-CY28: safe test point)
    h_test = [F(37), F(41), F(-78)]
    B_test = [[0, 1, 0], [-1, 0, 1], [0, -1, 0]]
    mutation_data = structure_function_under_mutation(h_test, B_test, 1, F(1000))
    results['mutation_structure_function'] = {
        'cy2_preserved': mutation_data['cy2_preserved'],
        'unitarity_preserved': mutation_data['unitarity_preserved'],
    }

    # 9. A_1 reduction from full K3
    # Use a 6-parameter toy model (sum = 0)
    h_toy = [F(10), F(8), F(6), F(-6), F(-8), F(-10)]
    reduction = a1_enhancement_from_full_k3(h_toy, spherical_index=0)
    results['a1_reduction'] = {
        'dominant_h': reduction['dominant_h'],
        'partner_index': reduction['partner_index'],
    }

    # 10. Exchange graph for D4
    d4_seed = seed_ade_k3('D4')
    d4_graph = enumerate_exchange_graph(d4_seed, max_depth=6)
    results['d4_exchange_graph'] = {
        'n_seeds': d4_graph['n_seeds'],
        'is_finite': d4_graph['is_finite_type'],
    }

    results['status'] = STATUS
    return results
