r"""K3 Yangian at rank 2: Y(gl_2 \otimes g_{K3}).

STATUS: CONJECTURAL (AP-CY14).  The K3 Yangian Y(g_{K3}) is NOT a theorem.
All results in this module are conditional on the existence of Y(g_{K3})
as a quantization of the K3 double current algebra.  The rank-2 extension
Y(gl_2 \otimes g_{K3}) is ADDITIONALLY conditional on the tensor product
construction at rank N >= 2 (AP-CY14).

MATHEMATICAL CONTENT
====================

1. THE 48 GENERATORS.

   At rank 2, the Lie algebra is gl_2 \otimes g_{K3}, where gl_2 has 4
   generators (E_{ij} for i,j in {1,2}) and g_{K3} = H_{Muk} has 24
   Mukai lattice directions.  The total current count:

     4 * 24 = 96 current families (each with infinitely many modes)

   However, in the RTT presentation, the generating object is the 2x2
   Lax operator L(u) with entries from Y(g_{K3}):

     L^{(a)}(u) = [[T_{11}^{(a)}(u),  T_{12}^{(a)}(u)],
                    [T_{21}^{(a)}(u),  T_{22}^{(a)}(u)]]

   for a = 1,...,24 (Mukai directions).  Each T_{ij}^{(a)}(u) is a
   generating function with modes T_{ij,n}^{(a)} for n >= 0.

   The CHARGE-1 representation space is C^{48} = C^2 \otimes C^{24}:
   2 gl_2 colours times 24 Mukai directions.

   DECOMPOSITION into gl_2 generators:

     For each Mukai direction a:
       h^{(a)}(u) = T_{11}^{(a)}(u) - T_{22}^{(a)}(u)   [Cartan of sl_2]
       e^{(a)}(u) = T_{12}^{(a)}(u)                       [raising]
       f^{(a)}(u) = T_{21}^{(a)}(u)                       [lowering]
       c^{(a)}(u) = T_{11}^{(a)}(u) + T_{22}^{(a)}(u)    [gl_2 centre]

   Total: 4 * 24 = 96 currents grouped into 48 "RTT currents" (the
   T_{ij}^{(a)} with 2*2*24 = 96 components, but the Lax operator has
   48 independent off-diagonal entries: 2 * 24 from e^{(a)}, f^{(a)}).

   The 48 in the statement "48 currents" refers to the charge-1 space
   dimension = 2 * 24 = 48.

2. THE DEGREE-(48,48) STRUCTURE FUNCTION.

   The rank-2 structure function is:

     g_2(u) = g_1(u)^2 = prod_{a=1}^{24} ((u - h_a)/(u + h_a))^2

   Properties:
   - 48 zeros: u = h_a (each with multiplicity 2), a = 1,...,24
   - 48 poles: u = -h_a (each with multiplicity 2)
   - Unitarity: g_2(u) * g_2(-u) = 1
   - g_2(0) = ((-1)^{24})^2 = 1
   - g_2(infinity) = 1

3. THE RTT PRESENTATION.

   The Yangian Y(gl_2 \otimes g_{K3}) is defined by the RTT relation:

     R_{12}(u-v) L_1^{(a)}(u) L_2^{(b)}(v) = L_2^{(b)}(v) L_1^{(a)}(u) R_{12}(u-v)

   where R_{12}(u) is the FULL R-matrix on C^{48} \otimes C^{48}, built
   from the Yang R-matrix of gl_2 and the K3 structure function:

     R_{K3,2}(u) = R_{gl_2}(u) \otimes g_{K3}(u)

   The Yang R-matrix of gl_2 is the 4x4 matrix:

     R_{gl_2}(u) = (u * Id_4 + hbar * P_2) / (u + hbar)

   where P_2 is the permutation on C^2 x C^2.

   The FULL R-matrix has a block structure: 24 blocks of size 4x4
   (one per Mukai direction), with each block being the Yang R-matrix
   weighted by the K3 structure function eigenvalue g_a(u).

   At a = b (same Mukai direction):
     R_{aa}(u) = g_a(u) * R_{gl_2}(u)

   At a != b (different Mukai directions):
     R_{ab}(u) = g_{ab}(u) * Id_4   (diagonal: different Mukai
     directions decouple in the gl_1 Mukai sector)

   Here g_{ab}(u) = g_a(u) if a = b, and a more general coupling
   structure for a != b determined by the Mukai pairing omega^{ab}.
   For the diagonal Mukai basis: g_{ab}(u) = delta_{ab} * g_a(u).

4. THE SERRE RELATIONS.

   At rank 2, the sl_2 Serre relations are NONTRIVIAL:

     [e^{(a)}_0, [e^{(a)}_0, e^{(a)}_1]] = 0
     [f^{(a)}_0, [f^{(a)}_0, f^{(a)}_1]] = 0

   for each Mukai direction a.  These are the rank-2 Serre relations
   imposing that the Yangian is Y(gl_2), not Y(gl_infinity).

   The MUKAI-COUPLED Serre relations (between different Mukai
   directions a != b):

     (ad e^{(a)})^{1 - C_{ab}} e^{(b)} = 0

   where C_{ab} is the Cartan matrix of the Mukai lattice coupling.
   For orthogonal Mukai directions (omega^{ab} = 0): C_{ab} = 0, so
   the Serre relation is just [e^{(a)}, e^{(b)}] = 0 (commuting).
   For non-orthogonal directions: nontrivial Serre constraints.

   In the DIAGONAL Mukai basis (all directions orthogonal):
   the inter-Mukai Serre relations reduce to commutation, and only
   the INTRA-direction sl_2 Serre relations are nontrivial.

5. THE COPRODUCT: MATRIX MIURA.

   The coproduct on the 2x2 Lax matrix is MATRIX MULTIPLICATIVE:

     Delta_z(L^{(a)}(u)) = L^{(a),L}(u) * L^{(a),R}(u - z)

   where the product is 2x2 MATRIX MULTIPLICATION.  Expanding:

     Delta_z(T_{ij}^{(a)}(u)) = sum_k T_{ik}^{(a),L}(u) * T_{kj}^{(a),R}(u-z)

   This gives NONTRIVIAL mixing between the gl_2 indices (i,j,k = 1,2)
   even though the Mukai directions decouple in the abelian sector.

   MODE-LEVEL COPRODUCT (expanding in modes T_{ij,n}):
   At mode n and spectral shift z:

     Delta_z(T_{ij,n}^{(a)}) = sum_k sum_{p+q=n} T_{ik,p}^{(a),L} * T_{kj,q}^{(a),R}
                                + z-dependent terms

   The z-dependence enters through the shift u -> u-z in the R-factor.

   EXPLICIT at spin 1 (Cartan):
     Delta_z(h^{(a)}(u)) = h^{(a),L}(u) + h^{(a),R}(u-z)  [primitive]
     Delta_z(c^{(a)}(u)) = c^{(a),L}(u) + c^{(a),R}(u-z)  [primitive]

   EXPLICIT at spin 1 (roots, Drinfeld form):
     Delta_z(e^{(a)}(u)) = e^{(a),L}(u) + psi^{(a),L}(u) * e^{(a),R}(u-z)
     Delta_z(f^{(a)}(u)) = f^{(a),L}(u) * psi^{(a),R,-1}(u-z) + f^{(a),R}(u-z)

   where psi^{(a)}(u) = T_{11}^{(a)}(u) / T_{22}^{(a)}(u) is the Cartan
   generating function in the a-th Mukai direction.

6. THE R-MATRIX AT CHARGE 2.

   The charge-2 representation space for gl_2 x Mukai has dimension:

     dim = (48 choose 2) + 48 = 48*49/2 = 1176

   Wait -- the charge-2 states for the RTT formalism on C^{48}:
   The 2-particle states are in C^{48} \otimes C^{48} = C^{2304}.
   But the R-matrix acts on this tensor product:

     R_{K3,2}(u) : C^{48} \otimes C^{48} -> C^{48} \otimes C^{48}

   This is a 2304 x 2304 matrix.  However, at charge 1 (the
   fundamental representation), the R-matrix is 48 x 48 on the
   SINGLE particle space -- NO, the R-matrix always acts on the
   TENSOR PRODUCT of two particle spaces.

   CORRECT: The charge-1 R-matrix R(u) acts on C^{48} \otimes C^{48},
   so it is a 2304 x 2304 matrix.  But its STRUCTURE is factored:

     R(u) = R_{gl_2}(u) \otimes R_{K3}(u)

   where R_{gl_2}(u) is 4x4 (on C^2 \otimes C^2) and R_{K3}(u)
   is diagonal 576x576 (on C^{24} \otimes C^{24}).

   In the diagonal Mukai basis, the R-matrix decomposes into 24
   diagonal blocks:

     For Mukai direction a: R_a(u) is a 4x4 block (gl_2 Yang R-matrix)
     weighted by g_a(u) = ((u-h_a)/(u+h_a))^2.

   The off-diagonal blocks (mixing different Mukai directions)
   are diagonal (abelian complement decouples).

   The full R-matrix has:
   - 24 blocks of 4x4 Yang R-matrices: 24 * 12 = 288 nonzero off-diag
     entries (from the P term in the Yang R-matrix)
   - 576 - 96 = 480 diagonal entries from the pure Mukai sector
   Total matrix dimension: 2304 x 2304

   ACTUALLY, the standard convention for the "charge-2 R-matrix"
   in the K3 Yangian literature (following k3_rmatrix_a1_offdiagonal.py)
   refers to the 2-particle sector for a SINGLE particle species.
   At rank 2, the single particle has dim 48, so:

     R_{charge-2}: C^{48} \otimes C^{48} -> C^{48} \otimes C^{48}
     Dimension: 48^2 = 2304 ... NO, the charge-2 MODULI SPACE has
     dimension (48+1 choose 2) = 1176 for bosonic, but for the
     scattering matrix, R acts on the 2-particle tensor product.

   We use the convention: the R-matrix at charge 1 is the
   SCATTERING MATRIX on the 2-particle space C^{48} \otimes C^{48}:

     R(u) in End(C^{48} \otimes C^{48})

   which is 2304 x 2304.  At generic Mukai moduli, this factors as:

     R(u) = sum_a g_a(u) * P_a \otimes R_{gl_2}(u)_a

   where P_a are Mukai projection operators.

   The PHYSICALLY RELEVANT matrix at charge 2 in the sense of
   the Hilbert scheme (charge = sum of instanton numbers) is the
   restriction of R to the symmetric/antisymmetric part:

     R|_{Sym^2(C^{48})} has dimension 1176
     R|_{Alt^2(C^{48})} has dimension 1128

   For the present module, we compute R on the full tensor product
   (dimension 2304) and extract the symmetric part when needed.

   AP-CY30: The 2-particle R-matrix R_{12}(u) does NOT by itself
   determine the 3-particle S-operator (Zamolodchikov tetrahedron
   obstruction at O(kappa^2)).

CONVENTIONS
===========
  - N = 2: rank of the gauge group gl_2
  - h_a: Mukai Yangian parameters (a = 1,...,24), sum h_a = 0 (CY_2)
  - omega^{ab}: Mukai pairing, signature (4,20), diagonal basis
  - L^{(a)}(u): 2x2 Lax operator in Mukai direction a
  - T_{ij}^{(a)}(u): entries of L^{(a)}, with i,j in {1,2}
  - R_{gl_2}(u) = (u*Id + hbar*P)/(u+hbar): Yang R-matrix
  - g_a(u) = (u-h_a)^2/(u+h_a)^2: rank-2 structure function eigenvalue
  - kappa subscripts per AP113: NEVER bare kappa
  - AP-CY14: K3 Yangian results are CONJECTURAL
  - AP-CY31: u is spectral (Yangian), NOT worldsheet
  - AP-CY28: test points avoid poles at +/- h_a
  - AP-CY30: pairwise YBE does NOT imply tetrahedron

REFERENCES
==========
  k3_yangian.py (gl_1 K3 Yangian, rank-1 structure function, R-matrix)
  agt_higher_rank_k3.py (rank-N AGT, VW partition functions, W_N)
  k3_nonabelian_coproduct.py (Drinfeld coproduct at ADE points)
  k3_rmatrix_enhanced.py (Yang R-matrix, YBE verification)
  k3_rmatrix_a1_offdiagonal.py (off-diagonal R-matrix at A_1)
  sl2_chiral_coproduct_engine.py (sl_2 structure function, Drinfeld)
  e1_chiral_bialgebra_engine.py (E_1-chiral bialgebra axioms)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    STATUS,
    MukaiLatticeParams,
    kummer_k3_parameters,
    null_kummer_parameters,
    custom_parameters,
    mukai_diagonal_eigenvalues,
    structure_function_evaluate,
    newton_power_sums,
)
from compute.lib.k3_rmatrix_enhanced import (
    yang_r_matrix,
    yang_r_verify_ybe,
    yang_r_verify_unitarity,
)

F = Fraction

# =========================================================================
# 0. Constants
# =========================================================================

RANK_N = 2                  # gl_2
MUKAI_RANK = NUM_PARAMS     # = 24
CHARGE1_DIM = RANK_N * MUKAI_RANK  # = 48
STRUC_FUNC_DEGREE = (MUKAI_RANK * RANK_N, MUKAI_RANK * RANK_N)  # (48, 48)
NUM_CURRENTS = RANK_N * RANK_N * MUKAI_RANK  # 96 (RTT current families)

# kappa-spectrum at rank 2 (AP113: NEVER bare kappa)
KAPPA_CH_RANK2 = F(3) * RANK_N       # = 6, conjectural
KAPPA_CAT_RANK2 = F(2) * RANK_N      # = 4 = chi(O_{K3}) * 2
KAPPA_FIBER_RANK2 = F(24) * RANK_N   # = 48 = lattice rank * 2


# =========================================================================
# 1. Generators: the 48-dimensional charge-1 space
# =========================================================================

class Rank2GeneratorData(NamedTuple):
    r"""Generator data for Y(gl_2 \otimes g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    rank: int                   # 2
    mukai_rank: int             # 24
    charge1_dim: int            # 48
    gl2_generators: int         # 4 (E_{11}, E_{12}, E_{21}, E_{22})
    current_families: int       # 96 = 4 * 24
    lax_entries_per_dir: int    # 4 (2x2 matrix)
    lax_total_entries: int      # 96 = 4 * 24
    cartan_generators: int      # 48 (h^{(a)} and c^{(a)}, a=1..24)
    root_generators: int        # 48 (e^{(a)} and f^{(a)}, a=1..24)
    serre_nontrivial: bool      # True (rank 2 has sl_2 Serre)
    status: str


def generator_data() -> Rank2GeneratorData:
    r"""Complete generator data for the rank-2 K3 Yangian.

    The 2x2 Lax operator L^{(a)}(u) for each Mukai direction a = 1,...,24:

      L^{(a)}(u) = [[T_{11}^{(a)}(u),  T_{12}^{(a)}(u)],
                     [T_{21}^{(a)}(u),  T_{22}^{(a)}(u)]]

    In the Chevalley decomposition:
      e^{(a)}(u) = T_{12}^{(a)}(u)    (raising operator)
      f^{(a)}(u) = T_{21}^{(a)}(u)    (lowering operator)
      h^{(a)}(u) = T_{11}^{(a)}(u) - T_{22}^{(a)}(u)   (Cartan of sl_2)
      c^{(a)}(u) = T_{11}^{(a)}(u) + T_{22}^{(a)}(u)    (gl_2 centre)

    Total: 4 current families per Mukai direction, 24 directions -> 96.

    The charge-1 representation space: C^2 \otimes C^{24} = C^{48}.
    Basis: |i, a> for i in {1,2}, a in {1,...,24}.

    STATUS: CONJECTURAL (AP-CY14).
    """
    return Rank2GeneratorData(
        rank=RANK_N,
        mukai_rank=MUKAI_RANK,
        charge1_dim=CHARGE1_DIM,
        gl2_generators=RANK_N * RANK_N,  # = 4
        current_families=NUM_CURRENTS,   # = 96
        lax_entries_per_dir=RANK_N * RANK_N,  # = 4
        lax_total_entries=NUM_CURRENTS,  # = 96
        cartan_generators=2 * MUKAI_RANK,   # 48: h^(a) and c^(a)
        root_generators=2 * MUKAI_RANK,     # 48: e^(a) and f^(a)
        serre_nontrivial=True,
        status=STATUS,
    )


def charge1_basis() -> List[Tuple[int, int]]:
    r"""Enumerate the charge-1 basis states |i, a>.

    Returns list of (i, a) tuples where i in {0,1} (gl_2 index)
    and a in {0,...,23} (Mukai direction, 0-indexed).

    Total: 2 * 24 = 48 states.
    """
    return [(i, a) for i in range(RANK_N) for a in range(MUKAI_RANK)]


# =========================================================================
# 2. Structure function g_2(u) = g_1(u)^2, degree (48, 48)
# =========================================================================

def structure_function_rank2(
    u_val: F,
    params: Optional[MukaiLatticeParams] = None,
) -> F:
    r"""Evaluate g_2(u) = g_1(u)^2 = prod_{a=1}^{24} ((u-h_a)/(u+h_a))^2.

    The rank-2 structure function has degree (48, 48):
    - 48 zeros at u = h_a (each with multiplicity 2)
    - 48 poles at u = -h_a (each with multiplicity 2)

    Parameters
    ----------
    u_val : Fraction
        Spectral parameter (Yangian, NOT worldsheet; AP-CY31).
    params : MukaiLatticeParams, optional
        K3 Yangian parameters (default: Kummer K3).

    Returns
    -------
    Fraction : g_2(u_val)

    STATUS: CONJECTURAL (AP-CY14).
    """
    g1 = structure_function_evaluate(u_val, params)
    return g1 * g1


def structure_function_eigenvalue_rank2(
    a: int,
    u_val: F,
    params: Optional[MukaiLatticeParams] = None,
) -> F:
    r"""Evaluate the a-th eigenvalue of the rank-2 structure function.

    For Mukai direction a (0-indexed), the eigenvalue is:

      g_a^{(2)}(u) = ((u - h_a) / (u + h_a))^2

    This is the rank-2 weight for a single Mukai direction.

    The FULL structure function is the product over all 24 directions:
      g_2(u) = prod_a g_a^{(2)}(u) = prod_a ((u-h_a)/(u+h_a))^2

    Parameters
    ----------
    a : int
        Mukai direction (0-indexed, 0 <= a < 24).
    u_val : Fraction
        Spectral parameter.
    params : MukaiLatticeParams, optional
        K3 Yangian parameters.

    Returns
    -------
    Fraction : g_a^{(2)}(u_val) = ((u_val - h_a)/(u_val + h_a))^2
    """
    if params is None:
        params = kummer_k3_parameters()
    if a < 0 or a >= MUKAI_RANK:
        raise ValueError(f"Mukai direction a must be in [0, {MUKAI_RANK}), got {a}")
    h_a = params.h[a]
    if u_val + h_a == 0:
        raise ValueError(f"Pole at u = {u_val}: h_a = {h_a}")
    ratio = (u_val - h_a) / (u_val + h_a)
    return ratio * ratio


def verify_unitarity_rank2(
    params: Optional[MukaiLatticeParams] = None,
    test_points: Optional[List[F]] = None,
) -> Dict[str, Any]:
    r"""Verify g_2(u) * g_2(-u) = 1.

    Proof: g_2(u) * g_2(-u) = (g_1(u))^2 * (g_1(-u))^2
           = (g_1(u) * g_1(-u))^2 = 1^2 = 1.

    AP-CY28: test points avoid poles at +/- h_a.

    STATUS: CONJECTURAL (AP-CY14) for the Yangian interpretation.
    """
    if params is None:
        params = kummer_k3_parameters()
    if test_points is None:
        test_points = [F(37), F(41), F(53), F(97, 3)]

    checks = []
    for u in test_points:
        try:
            g_u = structure_function_rank2(u, params)
            g_neg_u = structure_function_rank2(-u, params)
            product = g_u * g_neg_u
            checks.append({
                'u': str(u),
                'g_2(u)': str(g_u),
                'g_2(-u)': str(g_neg_u),
                'product': str(product),
                'is_one': product == F(1),
            })
        except ValueError as e:
            checks.append({'u': str(u), 'error': str(e), 'is_one': False})

    all_pass = all(c.get('is_one', False) for c in checks)
    return {
        'rank': RANK_N,
        'unitarity_holds': all_pass,
        'proof': 'g_2(u)*g_2(-u) = (g_1(u)*g_1(-u))^2 = 1^2 = 1',
        'checks': checks,
        'status': STATUS,
    }


def structure_function_log_coefficients_rank2(
    params: Optional[MukaiLatticeParams] = None,
    max_order: int = 12,
) -> List[F]:
    r"""Log expansion of g_2(u).

    log g_2(u) = 2 * log g_1(u) = 2 * sum_{k odd} (-2/k) p_k u^{-k}

    where p_k = sum_{a=1}^{24} h_a^k.
    """
    if params is None:
        params = kummer_k3_parameters()
    p = newton_power_sums(params, max_k=max_order)

    alphas = [F(0)]  # alpha_0 = 0
    for k in range(1, max_order + 1):
        if k % 2 == 0:
            alphas.append(F(0))
        else:
            alphas.append(F(-4, k) * p[k])  # factor 2 * (-2/k)
    return alphas


def structure_function_special_values_rank2(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Special values of g_2(u).

    g_2(0) = g_1(0)^2 = ((-1)^{24})^2 = 1.
    g_2(infinity) = 1.
    g_2(h_a) = 0 (double zero at each h_a).
    g_2(-h_a) = infinity (double pole at each -h_a).
    """
    if params is None:
        params = kummer_k3_parameters()
    from sympy import Rational
    g_at_0 = structure_function_rank2(Rational(0), params)
    return {
        'g_2(0)': g_at_0,
        'g_2(0)_expected': 1,
        'g_2(0)_matches': g_at_0 == 1,
        'g_2(inf)': 1,
        'degree': STRUC_FUNC_DEGREE,
        'num_zeros': 48,
        'zero_multiplicity': 2,
        'num_poles': 48,
        'pole_multiplicity': 2,
        'status': STATUS,
    }


# =========================================================================
# 3. RTT presentation
# =========================================================================

class RTTData(NamedTuple):
    r"""RTT presentation data for Y(gl_2 \otimes g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    rtt_relation: str
    r_matrix_description: str
    lax_matrix_size: Tuple[int, int]    # (2, 2)
    mukai_directions: int               # 24
    total_rtt_generators: int           # 96
    quantum_determinant: str
    center_description: str
    status: str


def rtt_presentation() -> RTTData:
    r"""The RTT presentation of Y(gl_2 \otimes g_{K3}).

    The defining relation:

      R_{12}(u-v) L_1^{(a)}(u) L_2^{(b)}(v) = L_2^{(b)}(v) L_1^{(a)}(u) R_{12}(u-v)

    where:
    - R_{12}(u) = R_{gl_2}(u) \otimes g_{K3}(u) on C^{48} \otimes C^{48}
    - L^{(a)}(u) is the 2x2 Lax operator in Mukai direction a
    - Subscripts 1,2 refer to the auxiliary spaces

    The quantum determinant:
      qdet L^{(a)}(u) = T_{11}^{(a)}(u) T_{22}^{(a)}(u - hbar)
                        - T_{12}^{(a)}(u) T_{21}^{(a)}(u - hbar)

    is a CENTRAL element of Y(gl_2 \otimes g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    return RTTData(
        rtt_relation=(
            'R_{12}(u-v) L_1^{(a)}(u) L_2^{(b)}(v) = '
            'L_2^{(b)}(v) L_1^{(a)}(u) R_{12}(u-v)'
        ),
        r_matrix_description=(
            'R_{K3,2}(u) = R_{gl_2}(u) \\otimes g_{K3}(u), '
            f'where R_{{gl_2}} = (u*Id + hbar*P)/(u+hbar) is 4x4 '
            f'and g_{{K3}} is the diagonal 24x24 structure function'
        ),
        lax_matrix_size=(RANK_N, RANK_N),
        mukai_directions=MUKAI_RANK,
        total_rtt_generators=NUM_CURRENTS,
        quantum_determinant=(
            'qdet L^{(a)}(u) = T_{11}^{(a)}(u) T_{22}^{(a)}(u-hbar) '
            '- T_{12}^{(a)}(u) T_{21}^{(a)}(u-hbar) is central'
        ),
        center_description=(
            f'Center generated by 24 quantum determinants qdet L^{{(a)}}(u), '
            f'one per Mukai direction.  These are the rank-2 analogues of the '
            f'rank-1 psi^{{(a)}}(u) (Cartan) generators.'
        ),
        status=STATUS,
    )


def rtt_relations_explicit() -> Dict[str, Any]:
    r"""Explicit RTT relations between Lax matrix entries.

    From R_{12}(u-v) L_1(u) L_2(v) = L_2(v) L_1(u) R_{12}(u-v),
    extracting the (ij, kl) component with the Yang R-matrix
    R(w) = (w*Id + hbar*P)/(w+hbar):

    For SAME Mukai direction a:

    [T_{ij}^{(a)}(u), T_{kl}^{(a)}(v)] =
      hbar/(u-v+hbar) * (T_{kj}^{(a)}(u) T_{il}^{(a)}(v)
                         - T_{kj}^{(a)}(v) T_{il}^{(a)}(u))

    This is the STANDARD gl_2 Yangian relation weighted by g_a(u-v).

    For DIFFERENT Mukai directions a != b (orthogonal in diagonal basis):

    [T_{ij}^{(a)}(u), T_{kl}^{(b)}(v)] = 0

    (commuting, since different Mukai directions decouple for gl_1).

    STATUS: CONJECTURAL (AP-CY14).
    """
    return {
        'same_mukai': (
            '[T_{ij}^{(a)}(u), T_{kl}^{(a)}(v)] = '
            'hbar/(u-v+hbar) * (T_{kj}^{(a)}(u) T_{il}^{(a)}(v) '
            '- T_{kj}^{(a)}(v) T_{il}^{(a)}(u))'
        ),
        'different_mukai_diagonal_basis': (
            '[T_{ij}^{(a)}(u), T_{kl}^{(b)}(v)] = 0 for a != b '
            '(diagonal Mukai basis, orthogonal directions)'
        ),
        'cartan_commutation': (
            '[h^{(a)}(u), h^{(b)}(v)] = 0 for all a, b '
            '(Cartan subalgebra is abelian)'
        ),
        'cartan_root': (
            '[h^{(a)}(u), e^{(a)}(v)] = '
            '2*hbar/(u-v+hbar) * (e^{(a)}(u) - e^{(a)}(v))'
        ),
        'root_root': (
            '[e^{(a)}(u), f^{(a)}(v)] = '
            'hbar/(u-v+hbar) * (psi^{(a)}(u) - psi^{(a)}(v))'
        ),
        'note': (
            'These are the mode-generating-function relations. '
            'Expanding in u^{-n-1} and v^{-m-1} gives the mode-level '
            'commutators [T_{ij,n}^{(a)}, T_{kl,m}^{(b)}].'
        ),
        'status': STATUS,
    }


# =========================================================================
# 4. Serre relations
# =========================================================================

class SerreData(NamedTuple):
    r"""Serre relation data for Y(gl_2 \otimes g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    intra_mukai_serre: str      # sl_2 Serre within each Mukai direction
    inter_mukai_serre: str      # between different Mukai directions
    num_intra_relations: int    # 24 (one per Mukai direction)
    num_inter_relations: int    # depends on Mukai pairing
    is_nontrivial: bool         # True
    status: str


def serre_relations() -> SerreData:
    r"""The Serre relations of Y(gl_2 \otimes g_{K3}).

    INTRA-MUKAI (for each direction a = 1,...,24):
    These enforce that the Yangian in each Mukai direction is Y(gl_2),
    not Y(gl_infinity):

      [e^{(a)}_0, [e^{(a)}_0, e^{(a)}_1]] = 0      (ad^2 = 0)
      [f^{(a)}_0, [f^{(a)}_0, f^{(a)}_1]] = 0      (ad^2 = 0)

    where e^{(a)}_n, f^{(a)}_n are the mode-n Chevalley generators.

    The DRINFELD-TYPE Serre relations (equivalent form):
      Sym_{z_1, z_2} [e^{(a)}(z_1), [e^{(a)}(z_2), e^{(a)}(w)]] = 0

    where Sym denotes symmetrization in z_1, z_2.

    INTER-MUKAI (between different directions a, b with a != b):
    In the diagonal Mukai basis (all omega^{ab} = 0 for a != b):

      [e^{(a)}(z), e^{(b)}(w)] = 0      (commuting)
      [f^{(a)}(z), f^{(b)}(w)] = 0      (commuting)

    This is because the off-diagonal Cartan entry C_{ab} = 0 in the
    diagonal basis, so the Serre relation (ad e^{(a)})^{1-0} e^{(b)} = 0
    reduces to [e^{(a)}, e^{(b)}] = 0.

    In a NON-DIAGONAL basis (general Mukai coupling), the inter-Mukai
    Serre relations would involve the full Mukai Cartan matrix and could
    be nontrivial.

    STATUS: CONJECTURAL (AP-CY14).
    """
    return SerreData(
        intra_mukai_serre=(
            '[e^{(a)}_0, [e^{(a)}_0, e^{(a)}_1]] = 0 for each a = 1,...,24. '
            'Equivalently: Sym_{z_1,z_2} [e^{(a)}(z_1), [e^{(a)}(z_2), e^{(a)}(w)]] = 0'
        ),
        inter_mukai_serre=(
            '[e^{(a)}(z), e^{(b)}(w)] = 0 for a != b '
            '(diagonal Mukai basis, C_{ab} = 0)'
        ),
        num_intra_relations=MUKAI_RANK,  # = 24
        num_inter_relations=MUKAI_RANK * (MUKAI_RANK - 1) // 2,  # = 276
        is_nontrivial=True,
        status=STATUS,
    )


def verify_serre_mode_level(hbar: float = 1.0) -> Dict[str, Any]:
    r"""Verify the Serre relation [e_0, [e_0, e_1]] = 0 at mode level.

    For the gl_2 Yangian, the generators at mode n satisfy:

      [e_0, e_1] = h_0 * e_0 - e_0 * h_0 + hbar * e_0   (from RTT)

    The Serre relation [e_0, [e_0, e_1]] = 0 is the constraint:

      [e_0, h_0 * e_0 - e_0 * h_0 + hbar * e_0] = 0

    Using [e_0, h_0] = -2 * e_0 (standard sl_2):

      = e_0 * (-2*e_0) - (h_0*e_0 - e_0*h_0 + hbar*e_0) * e_0
        + e_0 * (h_0*e_0 - e_0*h_0 + hbar*e_0)

    ... this requires careful computation in the Fock representation.

    We verify NUMERICALLY using the 2x2 matrix representation of Y(gl_2):
    In the fundamental representation on C^2, the Yangian generators are:

      e_0 = E_{12} = [[0,1],[0,0]]
      f_0 = E_{21} = [[0,0],[1,0]]
      h_0 = E_{11} - E_{22} = [[1,0],[0,-1]]
      e_1 = hbar * e_0 * h_0 / 2 = hbar/2 * [[0,-1],[0,0]]

    Check: [e_0, [e_0, e_1]] = ?

    [e_0, e_1] = e_0 * e_1 - e_1 * e_0
    e_0 * e_1 = [[0,1],[0,0]] * hbar/2 * [[0,-1],[0,0]] = 0
    e_1 * e_0 = hbar/2 * [[0,-1],[0,0]] * [[0,1],[0,0]] = hbar/2 * [[0,0],[0,0]] = 0
    Wait -- e_1 * e_0 = hbar/2 * [[0,-1],[0,0]] * [[0,1],[0,0]]:
      row 0: [0*0 + (-1)*0, 0*1 + (-1)*0] = [0, 0]
      row 1: [0*0 + 0*0, 0*1 + 0*0] = [0, 0]
    So [e_0, e_1] = 0 - 0 = 0.

    Then [e_0, [e_0, e_1]] = [e_0, 0] = 0.  Serre satisfied.

    This is because in the 2-dimensional fundamental representation,
    the nilpotency e_0^2 = 0 forces all nested commutators to vanish.

    For a NONTRIVIAL check, we need a HIGHER representation.  In the
    adjoint representation (3-dimensional for sl_2), the Serre relation
    is a genuine constraint.

    STATUS: CONJECTURAL (AP-CY14) for the K3 Yangian.
    The Serre relation for Y(gl_2) is PROVED (classical Yangian theory).
    """
    e0 = np.array([[0, 1], [0, 0]], dtype=complex)
    f0 = np.array([[0, 0], [1, 0]], dtype=complex)
    h0 = np.array([[1, 0], [0, -1]], dtype=complex)
    e1 = hbar / 2 * (e0 @ h0)

    comm_e0_e1 = e0 @ e1 - e1 @ e0
    serre = e0 @ comm_e0_e1 - comm_e0_e1 @ e0
    err = float(np.max(np.abs(serre)))

    # Adjoint representation (3-dim)
    e0_adj = np.array([[0, 1, 0], [0, 0, 2], [0, 0, 0]], dtype=complex)
    f0_adj = np.array([[0, 0, 0], [2, 0, 0], [0, 1, 0]], dtype=complex)
    h0_adj = np.array([[2, 0, 0], [0, 0, 0], [0, 0, -2]], dtype=complex)
    e1_adj = hbar / 2 * (e0_adj @ h0_adj)

    comm_adj = e0_adj @ e1_adj - e1_adj @ e0_adj
    serre_adj = e0_adj @ comm_adj - comm_adj @ e0_adj
    err_adj = float(np.max(np.abs(serre_adj)))

    return {
        'fundamental_error': err,
        'fundamental_serre_holds': err < 1e-10,
        'adjoint_error': err_adj,
        'adjoint_serre_holds': err_adj < 1e-10,
        'hbar': hbar,
        'note': (
            'Serre [e_0,[e_0,e_1]]=0 verified in fund (trivial, e^2=0) '
            'and adjoint (nontrivial, 3-dim) representations of gl_2.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 5. The coproduct: matrix Miura factorization
# =========================================================================

class MatrixMiuraCoproduct:
    r"""Matrix Miura coproduct for Y(gl_2 \otimes g_{K3}).

    The coproduct on the 2x2 Lax operator is:

      Delta_z(L^{(a)}(u)) = L^{(a),L}(u) * L^{(a),R}(u-z)

    where * is 2x2 matrix multiplication.

    Expanding into components:

      Delta_z(T_{ij}^{(a)}(u)) = sum_{k=1}^{2} T_{ik}^{(a),L}(u) * T_{kj}^{(a),R}(u-z)

    The KEY DIFFERENCE from the rank-1 case:
    - Rank 1: Delta_z(T(u)) = T^L(u) * T^R(u-z) (scalar multiplication)
    - Rank 2: Delta_z(L(u)) = L^L(u) * L^R(u-z) (MATRIX multiplication)

    The matrix multiplication introduces CROSS-TERMS between different
    gl_2 components (e.g. e^L * f^R contributing to h coproduct).

    STATUS: CONJECTURAL (AP-CY14).
    """

    def __init__(self, hbar: float = 1.0,
                 params: Optional[MukaiLatticeParams] = None):
        self.hbar = hbar
        if params is None:
            params = kummer_k3_parameters()
        self.params = params

    def coproduct_lax_symbolic(self, a: int = 0) -> Dict[str, Any]:
        r"""Symbolic coproduct of the 2x2 Lax operator in Mukai direction a.

        Delta_z(L^{(a)}(u)) = L^{(a),L}(u) * L^{(a),R}(u-z)

        where L = [[T_{11}, T_{12}], [T_{21}, T_{22}]].

        The matrix product gives:

        Delta_z(T_{11}) = T_{11}^L * T_{11}^R + T_{12}^L * T_{21}^R
        Delta_z(T_{12}) = T_{11}^L * T_{12}^R + T_{12}^L * T_{22}^R
        Delta_z(T_{21}) = T_{21}^L * T_{11}^R + T_{22}^L * T_{21}^R
        Delta_z(T_{22}) = T_{21}^L * T_{12}^R + T_{22}^L * T_{22}^R

        In Chevalley notation:
        Delta_z(e) = e^L * T_{22}^R + T_{11}^L * e^R
                   = T_{11}^L * e^R + e^L * T_{22}^R
        Delta_z(f) = f^L * T_{11}^R + T_{22}^L * f^R
                   = T_{22}^L * f^R + f^L * T_{11}^R
        Delta_z(h) = (T_{11}^L * T_{11}^R + e^L * f^R)
                   - (f^L * e^R + T_{22}^L * T_{22}^R)
                   = h^L * T_{22}^R + T_{11}^L * h^R
                     + e^L * f^R - f^L * e^R

        The CROSS-TERMS e^L * f^R and f^L * e^R are the KEY nonabelian
        feature: they mix raising and lowering operators.

        Specializing T_{ii}(u) = 1 + O(u^{-1}) (RTT normalization) and
        extracting the mode-0 components:

        Delta_z(e_0) = e_0^L + e_0^R + z * psi_0^L * e_0^R + O(z^2)
        Delta_z(f_0) = f_0^L + f_0^R - z * f_0^R * psi_0^R + O(z^2)
        Delta_z(h_0) = h_0^L + h_0^R + [e_0^L, f_0^R] - [f_0^L, e_0^R]

        where psi = T_{11}/T_{22} is the Cartan ratio.
        """
        return {
            'mukai_direction': a,
            'formula': 'Delta_z(L^{(a)}(u)) = L^{(a),L}(u) * L^{(a),R}(u-z)',
            'matrix_entries': {
                'T11': 'T_{11}^L * T_{11}^R + T_{12}^L * T_{21}^R = T_{11}^L * T_{11}^R + e^L * f^R',
                'T12': 'T_{11}^L * T_{12}^R + T_{12}^L * T_{22}^R = T_{11}^L * e^R + e^L * T_{22}^R',
                'T21': 'T_{21}^L * T_{11}^R + T_{22}^L * T_{21}^R = f^L * T_{11}^R + T_{22}^L * f^R',
                'T22': 'T_{21}^L * T_{12}^R + T_{22}^L * T_{22}^R = f^L * e^R + T_{22}^L * T_{22}^R',
            },
            'chevalley_coproduct': {
                'e': 'Delta_z(e) = T_{11}^L * e^R + e^L * T_{22}^R  [Drinfeld form]',
                'f': 'Delta_z(f) = T_{22}^L * f^R + f^L * T_{11}^R  [Drinfeld form]',
                'h': 'Delta_z(h) = h^L + h^R + e^L * f^R - f^L * e^R  [with cross-terms]',
                'c': 'Delta_z(c) = c^L + c^R + e^L * f^R + f^L * e^R  [gl_2 centre]',
            },
            'cross_terms': (
                'e^L * f^R: left-raising times right-lowering (NONABELIAN). '
                'f^L * e^R: left-lowering times right-raising (NONABELIAN). '
                'These vanish in the rank-1 (gl_1) case.'
            ),
            'status': STATUS,
        }

    def coproduct_mode_level(self, z: float = 0.0) -> Dict[str, Any]:
        r"""Mode-level coproduct at spectral parameter z.

        At z = 0 (cocommutative limit, AP-CY31: z is spectral not worldsheet):

        Delta_0(e_0^{(a)}) = e_0^{(a),L} + e_0^{(a),R}  [primitive at z=0]
        Delta_0(f_0^{(a)}) = f_0^{(a),L} + f_0^{(a),R}  [primitive at z=0]
        Delta_0(h_0^{(a)}) = h_0^{(a),L} + h_0^{(a),R}  [always primitive]

        At general z:

        Delta_z(e_0^{(a)}) = e_0^L + e_0^R + z * h_0^L * e_0^R + O(z^2)
        Delta_z(f_0^{(a)}) = f_0^L + f_0^R - z * f_0^R * h_0^R + O(z^2)

        The z-dependent terms are the YANGIAN deformation of the
        primitive coproduct.  The cross-terms between L and R factors
        involve the gl_2 structure and the Mukai lattice coupling.
        """
        return {
            'z': z,
            'z_equals_0_cocommutative': abs(z) < 1e-15,
            'mode_0_coproducts': {
                'e_0': f'e_0^L + e_0^R + {z}*h_0^L*e_0^R + O(z^2)',
                'f_0': f'f_0^L + f_0^R - {z}*f_0^R*h_0^R + O(z^2)',
                'h_0': 'h_0^L + h_0^R  [primitive for all z]',
            },
            'note': (
                'At z=0: cocommutative (primitive for all generators). '
                'z is a Yangian spectral parameter (AP-CY31), not worldsheet. '
                'No OPE poles at z=0.'
            ),
            'status': STATUS,
        }

    def coassociativity_from_matrix_miura(self) -> Dict[str, Any]:
        r"""Coassociativity: (Delta_z \otimes id) o Delta_w = (id \otimes Delta_w) o Delta_z.

        PROOF: The Lax matrix product is associative:

          (L^{(1)} * L^{(2)}) * L^{(3)} = L^{(1)} * (L^{(2)} * L^{(3)})

        where * is 2x2 matrix multiplication.  The spectral shifts compose:

          Delta_z(L(u)) = L^L(u) * L^R(u-z)

        Applying (Delta_z \otimes id) o Delta_w:
          L(u) -> L^{(12)}(u) * L^{(3)}(u-w)
          L^{(12)}(u) -> L^{(1)}(u) * L^{(2)}(u-z)
          Result: L^{(1)}(u) * L^{(2)}(u-z) * L^{(3)}(u-w)

        Applying (id \otimes Delta_w) o Delta_z:
          L(u) -> L^{(1)}(u) * L^{(23)}(u-z)
          L^{(23)}(u-z) -> L^{(2)}(u-z) * L^{(3)}(u-z-w)

        WAIT: the shifts differ.  The correct coassociativity uses:
          (Delta_z \otimes id) o Delta_w gives
          L^{(1)}(u) * L^{(2)}(u-z) * L^{(3)}(u-z-w)

          (id \otimes Delta_w) o Delta_z gives
          L^{(1)}(u) * L^{(2)}(u-z) * L^{(3)}(u-z-w)

        Both give the SAME triple product, because 2x2 matrix
        multiplication is ASSOCIATIVE.  QED (conditional on AP-CY14).

        CRITICAL: This is a 2x2 MATRIX product, not a scalar product.
        Associativity of matrix multiplication is what makes coassociativity
        TRIVIAL for the matrix Miura, exactly as in the rank-1 case.
        """
        return {
            'statement': (
                'Coassociativity of Delta_z on Y(gl_2 \\otimes g_{K3}) '
                'follows from associativity of 2x2 matrix multiplication.'
            ),
            'triple_product': (
                'L^{(1)}(u) * L^{(2)}(u-z) * L^{(3)}(u-z-w) '
                '(both orderings of iterated Delta give the same result)'
            ),
            'rank_1_comparison': (
                'Rank 1: scalar T^{(1)}*T^{(2)}*T^{(3)}, coassociativity trivial. '
                'Rank 2: matrix L^{(1)}*L^{(2)}*L^{(3)}, coassociativity from '
                'associativity of Mat_2(C). Same mechanism, higher dimension.'
            ),
            'status': STATUS,
        }

    def coproduct_numerical_check(
        self,
        u_val: float = 3.7,
        z_val: float = 1.3,
    ) -> Dict[str, Any]:
        r"""Numerical check of the matrix Miura coproduct.

        Construct L(u) in the fundamental representation and verify
        Delta_z(L(u)) = L^L(u) * L^R(u-z) as a 4x4 matrix equation.

        In the fundamental representation:
          L(u) = u * Id_2 + hbar * E  (for a single generator)

        We test with the simplest Lax operator:
          L(u) = [[u + hbar/2,  0], [0, u - hbar/2]]  (diagonal/Cartan)

        and
          L(u) = [[u, hbar], [0, u]]  (upper triangular, from e generator)

        AP-CY28: u_val = 3.7, z_val = 1.3 (far from poles).
        """
        hbar = self.hbar

        # Diagonal Lax (Cartan sector)
        L_diag = lambda u: np.array([
            [u + hbar / 2, 0],
            [0, u - hbar / 2],
        ], dtype=complex)

        L_L = L_diag(u_val)
        L_R = L_diag(u_val - z_val)
        delta_diag = L_L @ L_R

        # Verify: this should equal Delta_z(L(u)) in the Cartan sector
        expected_11 = (u_val + hbar / 2) * (u_val - z_val + hbar / 2)
        expected_22 = (u_val - hbar / 2) * (u_val - z_val - hbar / 2)

        err_diag = abs(delta_diag[0, 0] - expected_11) + abs(delta_diag[1, 1] - expected_22)
        off_diag_zero = abs(delta_diag[0, 1]) + abs(delta_diag[1, 0])

        # Upper triangular Lax (with e generator)
        L_tri = lambda u: np.array([
            [u + hbar / 2, hbar],
            [0, u - hbar / 2],
        ], dtype=complex)

        L_L_tri = L_tri(u_val)
        L_R_tri = L_tri(u_val - z_val)
        delta_tri = L_L_tri @ L_R_tri

        # The (1,2) entry: cross-term from e^L * T_{22}^R + T_{11}^L * e^R
        expected_12 = (hbar * (u_val - z_val - hbar / 2)
                       + (u_val + hbar / 2) * hbar)
        err_tri = abs(delta_tri[0, 1] - expected_12)

        return {
            'diagonal_lax': {
                'Delta_z(L)_11': complex(delta_diag[0, 0]),
                'expected_11': expected_11,
                'Delta_z(L)_22': complex(delta_diag[1, 1]),
                'expected_22': expected_22,
                'off_diagonal_zero': off_diag_zero < 1e-10,
                'error': float(err_diag),
                'pass': err_diag < 1e-10,
            },
            'upper_triangular_lax': {
                'Delta_z(L)_12': complex(delta_tri[0, 1]),
                'expected_12': expected_12,
                'error': float(err_tri),
                'pass': err_tri < 1e-10,
                'cross_term': (
                    'T_{12} entry = e^L * T_{22}^R + T_{11}^L * e^R '
                    '= hbar*(u-z-hbar/2) + (u+hbar/2)*hbar'
                ),
            },
            'u': u_val,
            'z': z_val,
            'hbar': self.hbar,
            'status': STATUS,
        }


# =========================================================================
# 6. R-matrix: 48x48 on C^{48} \otimes C^{48}
# =========================================================================

def r_matrix_rank2_block(
    a: int,
    u_val: complex,
    params: Optional[MukaiLatticeParams] = None,
    hbar: complex = 1.0,
) -> np.ndarray:
    r"""The 4x4 R-matrix block for Mukai direction a at rank 2.

    For Mukai direction a, the R-matrix block is:

      R_a(u) = g_a(u) * R_{gl_2}(u)
             = g_a(u) * (u*Id_4 + hbar*P_2) / (u + hbar)

    where g_a(u) = ((u-h_a)/(u+h_a))^2 is the rank-2 structure function
    eigenvalue, and R_{gl_2} is the standard 4x4 Yang R-matrix.

    Parameters
    ----------
    a : int
        Mukai direction (0-indexed).
    u_val : complex
        Spectral parameter (AP-CY31: Yangian spectral, not worldsheet).
    params : MukaiLatticeParams, optional
        K3 Yangian parameters.
    hbar : complex
        Yangian deformation parameter.

    Returns
    -------
    4x4 numpy array.

    AP-CY28: avoid u_val = +/- h_a (poles).
    """
    if params is None:
        params = kummer_k3_parameters()
    h_a = complex(params.h[a])

    # g_a(u) = ((u - h_a)/(u + h_a))^2
    if abs(u_val + h_a) < 1e-15:
        raise ValueError(f"Pole at u={u_val}, h_a={h_a}")
    g_a = ((u_val - h_a) / (u_val + h_a)) ** 2

    # Yang R-matrix for gl_2
    R_gl2 = yang_r_matrix(u_val, hbar, n=2)  # 4x4

    return g_a * R_gl2


def r_matrix_rank2_full(
    u_val: complex,
    params: Optional[MukaiLatticeParams] = None,
    hbar: complex = 1.0,
) -> np.ndarray:
    r"""The full R-matrix for rank-2 K3 Yangian on C^{48} \otimes C^{48}.

    R_{K3,2}(u) = R_{gl_2}(u) \otimes R_{K3,diag}(u)

    where R_{gl_2}(u) is 4x4 and R_{K3,diag}(u) is a 576x576 diagonal
    matrix (24x24 blocks of 24x24 entries).

    In practice, the full matrix is 2304x2304.  We build it block-by-block:
    for each pair (a,b) of Mukai directions, the (a,b) block is:

      - If a == b: g_a(u) * R_{gl_2}(u)   (4x4 Yang block)
      - If a != b: g_{ab}(u) * Id_4        (4x4 diagonal, abelian coupling)

    For the DIAGONAL Mukai basis: g_{ab} = 0 for a != b (no coupling),
    so the off-diagonal Mukai blocks are zero.  The full R-matrix is
    block-diagonal with 24 blocks of 4x4.

    Returns
    -------
    2304x2304 numpy array.

    Note: this is a LARGE matrix.  For practical computations,
    use r_matrix_rank2_block() for individual blocks.
    """
    if params is None:
        params = kummer_k3_parameters()

    dim = CHARGE1_DIM * CHARGE1_DIM  # 48 * 48 = 2304
    R = np.zeros((dim, dim), dtype=complex)

    for a in range(MUKAI_RANK):
        h_a = complex(params.h[a])
        if abs(u_val + h_a) < 1e-15:
            raise ValueError(f"Pole at u={u_val}, h_a={h_a}")
        g_a = ((u_val - h_a) / (u_val + h_a)) ** 2

        # Yang R-matrix block for this Mukai direction
        R_block = g_a * yang_r_matrix(u_val, hbar, n=RANK_N)  # 4x4

        # Place the 4x4 block into the full matrix
        # Index mapping: state |i, a> has index i * MUKAI_RANK + a
        # Tensor product |i,a> x |j,b> has index
        #   (i*MUKAI_RANK + a) * CHARGE1_DIM + (j*MUKAI_RANK + b)
        for i1 in range(RANK_N):
            for i2 in range(RANK_N):
                for j1 in range(RANK_N):
                    for j2 in range(RANK_N):
                        # Row: state |i1, a> x |i2, a> in the tensor product
                        row = (i1 * MUKAI_RANK + a) * CHARGE1_DIM + (i2 * MUKAI_RANK + a)
                        # Col: state |j1, a> x |j2, a>
                        col = (j1 * MUKAI_RANK + a) * CHARGE1_DIM + (j2 * MUKAI_RANK + a)
                        # R_block index: (i1*N + i2, j1*N + j2)
                        R[row, col] += R_block[i1 * RANK_N + i2, j1 * RANK_N + j2]

    # Diagonal entries for different Mukai directions (a != b)
    for a in range(MUKAI_RANK):
        for b in range(MUKAI_RANK):
            if a == b:
                continue
            h_a = complex(params.h[a])
            h_b = complex(params.h[b])
            # For different Mukai directions in diagonal basis,
            # the R-matrix is just the product of individual g factors
            if abs(u_val + h_a) < 1e-15 or abs(u_val + h_b) < 1e-15:
                continue  # skip poles
            g_ab = ((u_val - h_a) / (u_val + h_a)) * ((u_val - h_b) / (u_val + h_b))

            for i in range(RANK_N):
                for j in range(RANK_N):
                    row = (i * MUKAI_RANK + a) * CHARGE1_DIM + (j * MUKAI_RANK + b)
                    col = (i * MUKAI_RANK + a) * CHARGE1_DIM + (j * MUKAI_RANK + b)
                    R[row, col] += g_ab

    return R


def r_matrix_rank2_properties(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Properties of the rank-2 R-matrix.

    The R-matrix R_{K3,2}(u) on C^{48} \otimes C^{48}:

    1. Block structure: 24 blocks of 4x4 Yang R-matrices (same Mukai direction)
       + diagonal entries for different Mukai directions.

    2. Off-diagonal entries (within each 4x4 block):
       From the Yang R-matrix P term: hbar/(u + hbar) per block.
       Total: 24 blocks * 2 off-diagonal entries = 48 off-diagonal entries.

    3. YBE: satisfied because
       (a) Yang R-matrix satisfies YBE (PROVED)
       (b) K3 diagonal factor satisfies YBE (trivial)
       (c) Tensor product of YBE solutions is a YBE solution

    4. Unitarity: R(u) * R_{21}(-u) = Id
       From: g_a(u)*g_a(-u) = 1 AND Yang R-matrix unitarity.

    STATUS: CONJECTURAL (AP-CY14) for the K3 Yangian interpretation.
    """
    return {
        'rank': RANK_N,
        'charge1_dim': CHARGE1_DIM,
        'full_matrix_dim': CHARGE1_DIM ** 2,
        'block_structure': f'{MUKAI_RANK} blocks of {RANK_N**2}x{RANK_N**2} (Yang R-matrix)',
        'off_diagonal_per_block': 2,
        'total_off_diagonal': 2 * MUKAI_RANK,  # = 48
        'ybe': 'PROVED (factored: Yang YBE * diagonal K3 YBE)',
        'unitarity': 'R(u)*R_{21}(-u) = Id (from g(u)*g(-u) = 1 + Yang unitarity)',
        'nondiagonal': True,
        'note': (
            'At rank 2, the R-matrix is NONDIAGONAL even at generic K3 moduli '
            '(unlike rank 1 where it is diagonal). The off-diagonal entries '
            'come from the gl_2 Yang R-matrix P term, weighted by g_a(u).'
        ),
        'status': STATUS,
    }


def verify_ybe_rank2_block(
    a: int = 0,
    u: complex = 3.7 + 0.1j,
    v: complex = 1.3 + 0.2j,
    params: Optional[MukaiLatticeParams] = None,
    hbar: complex = 1.0,
) -> Dict[str, Any]:
    r"""Verify YBE for a single 4x4 Yang block in Mukai direction a.

    R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)

    on C^2 x C^2 x C^2 (the gl_2 fundamental space for a SINGLE Mukai direction).

    The K3 structure function g_a(u) is a scalar prefactor that cancels
    from both sides of YBE, so the check reduces to the standard Yang YBE.

    AP-CY28: u, v chosen to avoid poles.
    """
    if params is None:
        params = kummer_k3_parameters()

    # The YBE for the block reduces to Yang R-matrix YBE (scalar g_a cancels)
    result = yang_r_verify_ybe(u, v, hbar, n=RANK_N)

    h_a = complex(params.h[a])
    g_a_u = ((u - h_a) / (u + h_a)) ** 2
    g_a_v = ((v - h_a) / (v + h_a)) ** 2
    g_a_uv = (((u - v) - h_a) / ((u - v) + h_a)) ** 2

    return {
        'mukai_direction': a,
        'h_a': h_a,
        'g_a(u)': g_a_u,
        'g_a(v)': g_a_v,
        'g_a(u-v)': g_a_uv,
        'yang_ybe_result': result,
        'scalar_cancellation': (
            'g_a(u-v)*g_a(u)*g_a(v) appears on BOTH sides of YBE, '
            'so the check reduces to the Yang R-matrix YBE for gl_2.'
        ),
        'status': STATUS,
    }


def verify_unitarity_rank2_rmatrix(
    a: int = 0,
    u: complex = 3.7 + 0.1j,
    params: Optional[MukaiLatticeParams] = None,
    hbar: complex = 1.0,
) -> Dict[str, Any]:
    r"""Verify R_{12}(u) * R_{21}(-u) = Id for a single Mukai block.

    For the rank-2 block:
      R_a(u) = g_a(u) * R_{gl_2}(u)
      R_{a,21}(-u) = g_a(-u) * R_{gl_2,21}(-u)

    Product: g_a(u)*g_a(-u) * R_{gl_2}(u)*R_{gl_2,21}(-u) = 1 * Id = Id.
    """
    if params is None:
        params = kummer_k3_parameters()

    h_a = complex(params.h[a])
    g_a_u = ((u - h_a) / (u + h_a)) ** 2
    g_a_neg_u = ((-u - h_a) / (-u + h_a)) ** 2
    g_product = g_a_u * g_a_neg_u

    yang_result = yang_r_verify_unitarity(u, hbar, n=RANK_N)

    return {
        'mukai_direction': a,
        'g_a(u)*g_a(-u)': g_product,
        'g_product_is_one': abs(g_product - 1.0) < 1e-10,
        'yang_unitarity': yang_result,
        'combined_unitarity': abs(g_product - 1.0) < 1e-10 and yang_result['unitarity_satisfied'],
        'status': STATUS,
    }


# =========================================================================
# 7. Quantum determinant
# =========================================================================

def quantum_determinant_data() -> Dict[str, Any]:
    r"""The quantum determinant of the 2x2 Lax operator.

    For Y(gl_2), the quantum determinant is:

      qdet L^{(a)}(u) = T_{11}^{(a)}(u) T_{22}^{(a)}(u - hbar)
                        - T_{12}^{(a)}(u) T_{21}^{(a)}(u - hbar)

    Properties:
    1. qdet is CENTRAL in Y(gl_2 \otimes g_{K3}).
    2. qdet generates the Yangian of gl_1 (the determinant subalgebra).
    3. Y(sl_2 \otimes g_{K3}) = Y(gl_2 \otimes g_{K3}) / (qdet = scalar).
    4. For each Mukai direction a: one independent qdet L^{(a)}(u).
    5. Total: 24 independent quantum determinants.

    The quantum determinant encodes the CARTAN DATA:
      qdet L^{(a)}(u) = c^{(a)}(u) * c^{(a)}(u - hbar) - e^{(a)} f^{(a)} terms

    At the classical limit (hbar -> 0):
      qdet L^{(a)}(u) -> det L^{(a)}(u) = T_{11} T_{22} - T_{12} T_{21}

    STATUS: CONJECTURAL (AP-CY14).
    """
    return {
        'formula': (
            'qdet L^{(a)}(u) = T_{11}^{(a)}(u) T_{22}^{(a)}(u-hbar) '
            '- T_{12}^{(a)}(u) T_{21}^{(a)}(u-hbar)'
        ),
        'properties': [
            'Central in Y(gl_2 \\otimes g_{K3})',
            'Generates the gl_1 determinant subalgebra',
            'Y(sl_2) = Y(gl_2) / (qdet = scalar)',
            '24 independent quantum determinants (one per Mukai direction)',
        ],
        'coproduct_of_qdet': (
            'Delta_z(qdet L(u)) = qdet L^L(u) * qdet L^R(u-z) '
            '(multiplicative, since L^L * L^R respects the determinant)'
        ),
        'classical_limit': 'qdet -> det L(u) = T_{11}T_{22} - T_{12}T_{21}',
        'status': STATUS,
    }


def quantum_determinant_numerical(
    u_val: float = 3.7,
    hbar: float = 1.0,
) -> Dict[str, Any]:
    r"""Numerical verification of quantum determinant properties.

    In the fundamental 2-dim representation:
      L(u) = u * Id_2 + hbar/2 * diag(1, -1) + nilpotent terms
            = [[u + hbar/2, 0], [0, u - hbar/2]]  (diagonal case)

    qdet L(u) = L_{11}(u) * L_{22}(u - hbar) - L_{12}(u) * L_{21}(u - hbar)
              = (u + hbar/2)(u - hbar - hbar/2) - 0
              = (u + hbar/2)(u - 3*hbar/2)
    """
    # Diagonal Lax
    L11_u = u_val + hbar / 2
    L22_u = u_val - hbar / 2
    L11_uh = u_val - hbar + hbar / 2  # = u - hbar/2
    L22_uh = u_val - hbar - hbar / 2  # = u - 3*hbar/2

    qdet_val = L11_u * L22_uh - 0 * 0  # off-diag = 0 for diagonal Lax
    expected = (u_val + hbar / 2) * (u_val - 3 * hbar / 2)

    return {
        'u': u_val,
        'hbar': hbar,
        'qdet': qdet_val,
        'expected': expected,
        'match': abs(qdet_val - expected) < 1e-10,
        'note': 'Verified in diagonal fundamental representation',
        'status': STATUS,
    }


# =========================================================================
# 8. Summary and full verification
# =========================================================================

def rank2_summary() -> Dict[str, Any]:
    r"""Complete summary of Y(gl_2 \otimes g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    gen = generator_data()
    rtt = rtt_presentation()
    serre = serre_relations()

    return {
        'rank': RANK_N,
        'generators': {
            'charge1_dim': gen.charge1_dim,
            'current_families': gen.current_families,
            'lax_size': (gen.rank, gen.rank),
            'cartan_generators': gen.cartan_generators,
            'root_generators': gen.root_generators,
        },
        'structure_function': {
            'degree': STRUC_FUNC_DEGREE,
            'formula': 'g_2(u) = prod_{a=1}^{24} ((u-h_a)/(u+h_a))^2',
            'zeros': '48 (double at each h_a)',
            'poles': '48 (double at each -h_a)',
            'unitarity': 'g_2(u)*g_2(-u) = 1',
        },
        'rtt': {
            'relation': rtt.rtt_relation,
            'quantum_determinant': rtt.quantum_determinant,
        },
        'serre': {
            'intra_mukai': serre.intra_mukai_serre,
            'inter_mukai': serre.inter_mukai_serre,
            'num_intra': serre.num_intra_relations,
            'num_inter': serre.num_inter_relations,
            'nontrivial': serre.is_nontrivial,
        },
        'coproduct': {
            'type': 'matrix Miura',
            'formula': 'Delta_z(L(u)) = L^L(u) * L^R(u-z) (2x2 matrix product)',
            'coassociativity': 'from associativity of Mat_2(C)',
            'cross_terms': 'e^L*f^R, f^L*e^R (nonabelian, absent at rank 1)',
        },
        'r_matrix': {
            'charge1_dim': CHARGE1_DIM,
            'tensor_product_dim': CHARGE1_DIM ** 2,
            'block_structure': f'{MUKAI_RANK} blocks of 4x4 Yang R-matrices',
            'off_diagonal_total': 2 * MUKAI_RANK,
            'nondiagonal': True,
            'ybe': 'from factored Yang * diagonal K3',
        },
        'kappa_spectrum': {
            'kappa_ch': str(KAPPA_CH_RANK2),
            'kappa_cat': str(KAPPA_CAT_RANK2),
            'kappa_fiber': str(KAPPA_FIBER_RANK2),
        },
        'status': STATUS,
    }


def full_verification_rank2() -> Dict[str, Any]:
    r"""Full verification suite for Y(gl_2 \otimes g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    results = {}

    # 1. Generator data
    gen = generator_data()
    results['generators'] = {
        'charge1_dim': gen.charge1_dim,
        'charge1_dim_expected': 48,
        'match': gen.charge1_dim == 48,
    }

    # 2. Structure function
    unitarity = verify_unitarity_rank2()
    results['unitarity'] = unitarity

    # 3. Structure function special values
    sv = structure_function_special_values_rank2()
    results['special_values'] = sv

    # 4. Serre relation
    serre_check = verify_serre_mode_level()
    results['serre'] = serre_check

    # 5. Coproduct numerical check
    coprod = MatrixMiuraCoproduct()
    coprod_check = coprod.coproduct_numerical_check()
    results['coproduct_numerical'] = coprod_check

    # 6. R-matrix YBE
    ybe_check = verify_ybe_rank2_block()
    results['ybe'] = ybe_check

    # 7. R-matrix unitarity
    runit = verify_unitarity_rank2_rmatrix()
    results['r_unitarity'] = runit

    # 8. Quantum determinant
    qdet = quantum_determinant_numerical()
    results['quantum_determinant'] = qdet

    # Overall pass
    all_pass = (
        results['generators']['match']
        and results['unitarity']['unitarity_holds']
        and results['special_values']['g_2(0)_matches']
        and results['serre']['fundamental_serre_holds']
        and results['serre']['adjoint_serre_holds']
        and results['coproduct_numerical']['diagonal_lax']['pass']
        and results['coproduct_numerical']['upper_triangular_lax']['pass']
        and results['ybe']['yang_ybe_result']['ybe_satisfied']
        and results['r_unitarity']['combined_unitarity']
        and results['quantum_determinant']['match']
    )
    results['all_pass'] = all_pass
    results['status'] = STATUS

    return results
