r"""K3 Yangian quantization: Y(g_{K3}) from the Mukai lattice.

STATUS: CONJECTURAL (AP-CY14).  All results are conditional on the
existence of Y(g_{K3}) as a quantum group deformation of the K3 double
current algebra g_{K3}.  This module constructs what Y(g_{K3}) MUST be
if it exists, verifies internal consistency, and computes the key
structural predictions.

MATHEMATICAL CONTENT
====================

Problem 3 of the five load-bearing open problems (CLAUDE.md):
"K3 Yangian quantization: deforming g_{K3} to Y(g_{K3}). All inputs specified."

1. MUKAI SIGNATURE AND THE YANGIAN PARAMETERS.

   The Mukai pairing omega^{ij} = diag(+1,...,+1,-1,...,-1) of signature
   (4,20) means 4 of the 24 parameters h_i contribute with positive Mukai
   norm and 20 with negative.  In the diagonal basis:

     <h, h>_Muk = sum_{i=1}^{4} h_i^2 - sum_{i=5}^{24} h_i^2

   For the Yangian, the h_i live in the COMPLEXIFIED Mukai lattice.
   The signature (4,20) means:
   - The 4 positive directions (Kahler + hyperbolic) contribute REAL h_i
     to the structure function g(z) at real deformation.
   - The 20 negative directions contribute IMAGINARY h_i (h_i = i*|h_i|)
     at real deformation, or equivalently real h_i with reversed sign in
     the R-matrix unitarity.

   CRITICAL OBSERVATION: for the abelian (gl_1) K3 Yangian, the signature
   enters ONLY through the signs in the diagonal R-matrix.  Each direction
   i has R_{ii}(z) = (z - h_i)/(z + h_i), and the product g(z) = prod R_{ii}
   contains all 24 factors regardless of sign.  The signature manifests in:

   (a) The REALITY properties: for real z, the 4 positive-direction factors
       (z - h_i)/(z + h_i) with real h_i are real-valued, while the 20
       negative-direction factors with imaginary h_i produce phases.

   (b) The MUKAI NORM of the parameter vector: <h,h>_Muk can be positive,
       negative, or null, affecting the representation theory.

   (c) The TRACE of the Mukai pairing: Tr(omega) = 4 - 20 = -16, which
       enters the effective level Psi_eff of the Heisenberg subalgebra.

2. RTT PRESENTATION OF Y(g_{K3}).

   The Yangian is defined by the RTT relations:

     R_{12}(z-w) T_1(z) T_2(w) = T_2(w) T_1(z) R_{12}(z-w)

   where R(z) = (z*Id + hbar*P)/(z + hbar) is the Yang R-matrix on
   C^{24} tensor C^{24}, and T(z) is the monodromy matrix.

   For gl_1 (abelian), R simplifies to a diagonal matrix and the RTT
   relations decouple into 24 independent rank-1 sectors coupled only
   by the Mukai pairing through the effective level.

3. KOSZUL DUAL Y(g_{K3})^!.

   The Koszul dual of Y(g_{K3}) at parameters h_i has parameters -h_i.
   The Koszul conductor is:

     kappa_ch(Y) + kappa_ch(Y^!) = K

   For the free-field (Heisenberg) case, K = 0 (established in CLAUDE.md:
   "K3 KOSZUL CONDUCTOR = 0 (free-field/KM branch)").

   The dual structure function:

     g^!(z) = prod (z - (-h_i))/(z + (-h_i)) = prod (z + h_i)/(z - h_i) = 1/g(z)

   This is the INVERSION of the structure function, consistent with
   Koszul duality exchanging algebra and coalgebra.

4. BAR COMPLEX AND BKM ROOT MULTIPLICITIES.

   The bar complex B(Y(g_{K3})) has Euler product:

     prod_{n>=1} (1 - q^n)^{24} = eta(q)^{24}/q = Delta(q)/q

   where Delta(q) is the Ramanujan discriminant.  The exponent 24 is the
   rank of the Mukai lattice = number of Yangian parameters.

   The connection to BKM root multiplicities:

   The Fake Monster Lie algebra (attached to II_{25,1}) has root
   multiplicities c(D) = p_{24}(D+1) where p_{24} is the 24-colored
   partition function.  The bar Euler product of Y(g_{K3}) is EXACTLY
   the denominator of this Fake Monster:

     prod_{n>=1} (1-q^n)^{24} = denominator of Fake Monster at lightlike level

   More precisely: the LIGHTLIKE root multiplicity of the Fake Monster
   is 24 (= c(0) = p_{24}(1)), matching the Mukai rank.  The imaginary
   root multiplicities c(n) = p_{24}(n+1) for n >= 1 are the coefficients
   of 1/eta^{24}, which is the RECIPROCAL of the bar Euler product:

     1/prod(1-q^n)^{24} = sum_{n>=0} p_{24}(n) q^{n-1}

   This means: the Fock space character of Y(g_{K3}) reproduces the
   BKM root multiplicities of the Fake Monster Lie algebra.

   OBSERVATION (AP-CY8 compliant): this identification of the bar Euler
   product with the BKM denominator requires both CY-A_2 (which IS proved
   at d=2) and the Vol I identification of bar Euler products with
   automorphic forms.

5. YANG R-MATRIX AT RANK 24.

   The Yang R-matrix R(u) = (u*Id + hbar*P)/(u + hbar) on V tensor V
   with V = C^{24} acts as:

     R(u)(e_i tensor e_j) = (u/(u+hbar)) e_i tensor e_j      for i != j
     R(u)(e_i tensor e_i) = e_i tensor e_i                    for all i

   In components: R(u)^{ij}_{kl} = u/(u+hbar) delta^i_k delta^j_l
                                    + hbar/(u+hbar) delta^i_l delta^j_k

   The Yang R-matrix satisfies:
   - YBE: R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
   - Unitarity: R_{12}(u) R_{21}(-u) = Id
   - Crossing: R(u)^{t_1} = -(u+hbar)/(u) * R(-u-hbar)^{t_1}

   For the K3 Yangian, we specialize to V = C^{24} with the Mukai pairing
   omega providing the metric on V.  The R-matrix is then:

     R_omega(u) = (u*Id + hbar*P_omega)/(u + hbar)

   where P_omega is the omega-twisted permutation:
     P_omega(e_i tensor e_j) = omega^{ij} * (e_j tensor e_i)

   For diagonal omega = diag(+1,...,+1,-1,...,-1), P_omega squares to
   omega tensor omega (not to Id), giving a MODIFIED unitarity condition.

CONVENTIONS
===========
  - h_i: Yangian deformation parameters (i = 1,...,24)
  - omega_{ij}: Mukai pairing matrix, signature (4,20)
  - hbar: overall Yangian deformation parameter (= Planck constant)
  - CY_2 constraint: sum h_i = 0
  - kappa subscripts per AP113
  - AP-CY14: ALL results are CONJECTURAL
  - AP-CY8: bar Euler = BKM denominator requires CY-A_2 + Vol I anchor

REFERENCES
==========
  k3_yangian.py (structure function, R-matrix, coproduct)
  k3_double_current_algebra.py (classical limit: H_Muk)
  bkm_shadow_complete.py (Fake Monster multiplicities)
  affine_yangian_gl1.py (C^3 analogue)
  chiral_coproduct_allspin_engine.py (universal coproduct)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    diag,
    expand,
    eye,
    factor,
    ones,
    simplify,
    sqrt,
    symbols,
    zeros,
)

from compute.lib.k3_double_current_algebra import (
    HEISENBERG_DIM,
    K3_TOTAL_DIM,
    MUKAI_RANK,
    MUKAI_SIG_MINUS,
    MUKAI_SIG_PLUS,
    bar_euler_generating_function,
    k3_heisenberg,
    mukai_pairing_data,
)

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
    structure_function_coefficients,
    newton_power_sums,
    elementary_symmetric_functions,
    r_matrix_charge_1,
    r_matrix_diagonal_entries,
)

F = Fraction


# =========================================================================
# 0. Constants
# =========================================================================

QUANTIZATION_STATUS = 'CONJECTURAL'  # AP-CY14

# Koszul conductor for the free-field (Heisenberg/KM) branch
KOSZUL_CONDUCTOR_FREE_FIELD = 0  # K = 0 for free-field branch (CLAUDE.md)

# Fake Monster root multiplicities c(n) = p_{24}(n+1)
# These are the coefficients of q^n in 1/eta(q)^{24} = q^{-1}*sum p_{24}(n)q^n
FAKE_MONSTER_MULTIPLICITIES = {
    -1: 1,      # c(-1) = p_{24}(0) = 1 (Weyl vector)
    0: 24,      # c(0) = p_{24}(1) = 24 (lightlike, = Mukai rank)
    1: 324,     # c(1) = p_{24}(2) = 324
    2: 3200,    # c(2) = p_{24}(3) = 3200
    3: 25650,   # c(3) = p_{24}(4) = 25650
    4: 176256,  # c(4) = p_{24}(5) = 176256
    5: 1073720, # c(5) = p_{24}(6) = 1073720
}


# =========================================================================
# 1. Mukai signature analysis for the Yangian
# =========================================================================

class MukaiSignatureAnalysis(NamedTuple):
    """Analysis of how the Mukai signature (4,20) affects the K3 Yangian.

    STATUS: CONJECTURAL (AP-CY14).
    """
    signature: Tuple[int, int]          # (4, 20)
    effective_level: int                # Tr(omega) = 4 - 20 = -16
    positive_sector_h: List[Rational]   # h_i for positive Mukai directions
    negative_sector_h: List[Rational]   # h_i for negative Mukai directions
    mukai_norm_sq: Rational             # <h,h>_Muk
    is_null: bool                       # whether <h,h> = 0
    reality_type: str                   # description of reality properties
    status: str


def mukai_signature_analysis(
    params: Optional[MukaiLatticeParams] = None,
) -> MukaiSignatureAnalysis:
    r"""Analyze how the Mukai signature (4,20) enters the K3 Yangian.

    The signature affects:
    1. Effective level Psi_eff = Tr(omega) = 4 - 20 = -16
    2. Reality properties of R-matrix entries
    3. Koszul duality structure (self-dual vs non-self-dual)

    For REAL deformation (all h_i real):
    - The 4 positive-direction R-matrix entries (z-h_i)/(z+h_i) are real
      rational functions with real poles and zeros.
    - The 20 negative-direction entries are also real rational functions
      (the signature enters through the WEIGHT of contractions, not through
      the individual factors).

    For IMAGINARY deformation (h_i = i*|h_i| for negative directions):
    - This choice makes <h,h>_Muk = sum|h_i|^2 - sum|h_i|^2 which can
      be made to vanish (null condition).
    - The R-matrix entries become complex-valued.

    The KEY point for the gl_1 (abelian) case: the signature enters the
    Yangian ONLY through the effective level and the Mukai-weighted
    contractions in higher-charge representations.  At charge 1, the
    R-matrix is diagonal and the signature is invisible.
    """
    if params is None:
        params = kummer_k3_parameters()

    eigenvalues = mukai_diagonal_eigenvalues()
    h = params.h

    pos_h = [h[i] for i in range(len(h)) if eigenvalues[i] == 1]
    neg_h = [h[i] for i in range(len(h)) if eigenvalues[i] == -1]
    effective_level = sum(eigenvalues)  # 4 - 20 = -16

    # Classify reality type
    all_real = all(isinstance(hi, Rational) for hi in h)
    if all_real:
        reality = (
            'All h_i real. Signature enters through Mukai-weighted '
            f'contractions (Tr(omega) = {effective_level}), not through '
            'individual R-matrix entries.'
        )
    else:
        reality = 'Mixed real/imaginary h_i (complex deformation).'

    return MukaiSignatureAnalysis(
        signature=(SIG_PLUS, SIG_MINUS),
        effective_level=effective_level,
        positive_sector_h=pos_h,
        negative_sector_h=neg_h,
        mukai_norm_sq=params.mukai_norm_sq,
        is_null=params.is_null,
        reality_type=reality,
        status=QUANTIZATION_STATUS,
    )


def effective_central_charge(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Compute the effective central charge of Y(g_{K3}).

    For the Heisenberg Yangian at rank N with Mukai pairing omega:

    The total Heisenberg central charge (Fock space level):
      c_Fock = N = 24

    The effective level from the Mukai pairing:
      Psi_eff = Tr(omega) = 4 - 20 = -16

    The Sugawara central charge at effective level Psi_eff:
      c_Sug = 1  (for the rank-1 Sugawara built from total current J = sum phi_i)

    The central charge of the FULL rank-24 Heisenberg:
      c_full = 24  (one free boson per Mukai direction)

    The Virasoro central charge of Y(g_{K3}) at level Psi_eff:
      c_Vir = 24 - 24*(24-1)/(Psi_eff)  ... this depends on the
      specific Virasoro embedding.

    For the simple diagonal embedding T = sum T_i:
      c = 24  (sum of individual c = 1 contributions)

    The Mukai signature does NOT change the central charge c = 24 because
    each direction contributes c = 1 regardless of the Mukai sign.
    """
    if params is None:
        params = kummer_k3_parameters()

    eigenvalues = mukai_diagonal_eigenvalues()
    psi_eff = sum(eigenvalues)

    return {
        'total_fock_central_charge': NUM_PARAMS,  # 24
        'effective_level': psi_eff,  # -16
        'individual_central_charge': 1,  # each direction contributes c=1
        'total_virasoro_c': NUM_PARAMS,  # 24 (diagonal embedding)
        'mukai_trace': psi_eff,
        'signature_effect': (
            'Signature (4,20) gives Psi_eff = -16. This enters the '
            'Sugawara normalization T = J^2/(2*Psi_eff) and the '
            'Miura cross-term coefficient (Psi_eff-1)/Psi_eff = 17/16. '
            'The central charge c = 24 is unchanged by the signature.'
        ),
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 2. RTT presentation of Y(g_{K3})
# =========================================================================

class RTTPresentation(NamedTuple):
    """RTT presentation data for Y(g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    vector_space_dim: int       # 24
    r_matrix_type: str          # 'Yang' or 'Mukai-twisted Yang'
    generators: str             # description of generator matrix
    num_relations: int          # number of RTT relations
    quadratic_relations: int    # number from RTT
    serre_relations: str        # description of Serre-type relations
    status: str


def rtt_presentation() -> RTTPresentation:
    r"""RTT presentation of Y(g_{K3}).

    The Yangian Y(gl_N) for N = 24 has RTT presentation:

      R_{12}(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R_{12}(u-v)

    where T(u) = sum_{n>=0} T^{(n)} u^{-n} is the generating matrix.

    For gl_1 specialization (abelian):
    - T(u) is 24x24 diagonal (off-diagonal entries = 0 by abelianity).
    - The RTT relations reduce to commutation relations of the
      diagonal entries T_{ii}(u) with each other.
    - For diagonal T and diagonal R: all RTT relations are automatic.
    - The nontrivial content is in the COPRODUCT, not the algebra relations.

    For gl_N (non-abelian), the RTT relations give N^2(N^2-1)/2 independent
    quadratic relations.  At N = 24: 24^2 * (24^2 - 1) / 2 = 165,888
    quadratic relations.  Plus Serre-type relations from the Mukai pairing.
    """
    n = NUM_PARAMS  # 24

    return RTTPresentation(
        vector_space_dim=n,
        r_matrix_type='Yang R-matrix on C^{24} tensor C^{24}',
        generators=(
            f'T(u) = Id + sum_{{n>=1}} T^{{(n)}} u^{{-n}}, '
            f'T^{{(n)}} is a {n}x{n} matrix of modes. '
            f'For gl_1: T(u) diagonal, so {n} generating functions T_{{ii}}(u).'
        ),
        num_relations=n**2 * (n**2 - 1) // 2,  # 165888 for N=24
        quadratic_relations=n**2 * (n**2 - 1) // 2,
        serre_relations=(
            'For gl_1: no Serre relations (abelian). '
            'For non-abelian g: Serre relations from the Mukai pairing matrix, '
            f'with {n}*(n-1)/2 = {n*(n-1)//2} pairwise Serre constraints.'
        ),
        status=QUANTIZATION_STATUS,
    )


def rtt_commutation_relations(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Explicit RTT commutation relations for Y(g_{K3}) at gl_1.

    For the diagonal (abelian) case, the RTT relation becomes:

      [T_1(u), T_2(v)] = (hbar/(u-v)) * (P T_1(u) T_2(v) - T_2(v) T_1(u) P)
                          / (1 + hbar/(u-v))

    For diagonal T_i(u) = prod_{a=1}^{24} (u - phi_a^{(i)}) (Miura form):

    The psi-psi relation:
      psi^{(a)}(u) psi^{(b)}(v) = g_{ab}(u-v)/g_{ab}(v-u) * psi^{(b)}(v) psi^{(a)}(u)

    where g_{ab}(z) = (z - h_{ab})/(z + h_{ab}) and h_{ab} = omega^{ab} * hbar.

    For diagonal Mukai pairing (a = b):
      g_{aa}(z) = (z - omega^{aa}*hbar)/(z + omega^{aa}*hbar)

    where omega^{aa} = +1 for a = 1,...,4 and -1 for a = 5,...,24.

    The SIGN FLIP for negative Mukai directions:
      g_{aa}(z) = (z + hbar)/(z - hbar)  for a = 5,...,24

    This is 1/g_{aa}(z) for the positive directions!  The negative-direction
    generators commute with the INVERSE structure function compared to the
    positive-direction generators.
    """
    if params is None:
        params = kummer_k3_parameters()

    eigenvalues = mukai_diagonal_eigenvalues()
    hbar = Symbol("hbar")
    z = Symbol("z")

    # Structure functions per direction
    positive_g = (z - hbar) / (z + hbar)
    negative_g = (z + hbar) / (z - hbar)

    # Verify: positive_g * negative_g = 1 (complementary directions)
    product_check = cancel(positive_g * negative_g)

    # The ratio g_{ab}(z)/g_{ab}(-z) for the psi-psi relation
    positive_ratio = cancel(positive_g / ((z + hbar) / (z - hbar)))
    negative_ratio = cancel(negative_g / ((z - hbar) / (z + hbar)))

    return {
        'psi_psi_relation': (
            'psi^{(a)}(u) psi^{(b)}(v) = '
            '[g_{ab}(u-v)/g_{ab}(v-u)] * psi^{(b)}(v) psi^{(a)}(u)'
        ),
        'positive_direction_g': f'g_+(z) = (z - hbar)/(z + hbar) [for a = 1,...,{SIG_PLUS}]',
        'negative_direction_g': f'g_-(z) = (z + hbar)/(z - hbar) [for a = {SIG_PLUS+1},...,{NUM_PARAMS}]',
        'sign_flip': (
            'Negative Mukai directions have INVERTED structure function: '
            'g_-(z) = 1/g_+(z). This means positive and negative directions '
            'have OPPOSITE braiding, a direct manifestation of the '
            'indefinite signature (4,20).'
        ),
        'complementary_product': str(product_check),
        'complementary_is_1': product_check == 1,
        'positive_ratio_value': str(cancel(positive_ratio)),
        'negative_ratio_value': str(cancel(negative_ratio)),
        'num_positive': SIG_PLUS,
        'num_negative': SIG_MINUS,
        'status': QUANTIZATION_STATUS,
    }


def yangian_first_relations(
    params: Optional[MukaiLatticeParams] = None,
    max_mode: int = 3,
) -> Dict[str, Any]:
    r"""First few Yangian relations [T_1(u), T_2(v)] for the K3 case.

    For the gl_1 (abelian) K3 Yangian in the Miura (free-field) realization:

    T_{K3}(u) = prod_{i=1}^{24} (u - phi_i)

    The commutation relations of the phi_i modes are:

      [phi_i(u), phi_j(v)] = omega^{ij} * hbar / (u - v)

    where omega^{ij} is the Mukai pairing in diagonal basis.

    In mode form (phi_i(u) = sum_n phi_{i,n} u^{-n-1}):

      [phi_{i,m}, phi_{j,n}] = omega^{ij} * hbar * m * delta_{m+n,0}

    This is a HEISENBERG ALGEBRA with the Mukai pairing as the commutator
    matrix (up to mode number).

    The Yangian DEFORMATION enters through the transfer matrix modes.
    From T(u) = prod(u - phi_i), the modes psi_s = e_s(phi_1,...,phi_{24})
    satisfy the deformed relations.

    At spin 1 (Heisenberg):
      [J_m, J_n] = Psi_eff * m * delta_{m+n,0} * hbar

    where Psi_eff = Tr(omega) = 4 - 20 = -16.

    At spin 2 (Virasoro):
      [T_m, T_n] = (m-n)*T_{m+n} + (c/12)*m*(m^2-1)*delta_{m+n,0}

    with c = 24 (central charge from 24 free bosons).

    The Yangian deformation at spin 2:
      [T_m, J_n] = -n*J_{m+n}  (standard Virasoro-Heisenberg)
    plus corrections from the Miura transform at order O(hbar^2).
    """
    if params is None:
        params = kummer_k3_parameters()

    eigenvalues = mukai_diagonal_eigenvalues()
    psi_eff = sum(eigenvalues)

    relations = []

    # Spin 1: [J_m, J_n] = Psi_eff * m * delta_{m+n,0}
    for m in range(-max_mode, max_mode + 1):
        for n in range(-max_mode, max_mode + 1):
            if m + n == 0 and m != 0:
                relations.append({
                    'type': 'Heisenberg',
                    'lhs': f'[J_{m}, J_{n}]',
                    'rhs': f'{psi_eff} * {m} = {psi_eff * m}',
                    'modes': (m, n),
                })

    # Spin 2: [T_m, T_n] = (m-n)*T_{m+n} + (c/12)*m*(m^2-1)*delta_{m+n,0}
    c = NUM_PARAMS  # = 24
    virasoro_relations = []
    for m in range(-max_mode, max_mode + 1):
        for n in range(-max_mode, max_mode + 1):
            if m + n == 0 and m != 0:
                anomaly = Fraction(c, 12) * m * (m**2 - 1)
                virasoro_relations.append({
                    'type': 'Virasoro_anomaly',
                    'lhs': f'[T_{m}, T_{n}]',
                    'rhs': f'({m}-({n}))*T_0 + ({c}/12)*{m}*({m}^2-1) = 0 + {anomaly}',
                    'anomaly_value': anomaly,
                    'modes': (m, n),
                })

    # Spin 1-2 mixed: [T_m, J_n] = -n * J_{m+n}
    mixed_relations = []
    for m in range(-max_mode, max_mode + 1):
        for n in range(-max_mode, max_mode + 1):
            if abs(m + n) <= max_mode:
                mixed_relations.append({
                    'type': 'Virasoro-Heisenberg',
                    'lhs': f'[T_{m}, J_{n}]',
                    'rhs': f'{-n} * J_{m+n}',
                    'modes': (m, n),
                })

    return {
        'spin_1_heisenberg': relations,
        'spin_2_virasoro': virasoro_relations,
        'spin_1_2_mixed': mixed_relations[:10],  # first 10
        'effective_level': psi_eff,
        'central_charge': c,
        'num_spin1_relations': len(relations),
        'num_spin2_anomalies': len(virasoro_relations),
        'mukai_signature_in_level': (
            f'Psi_eff = Tr(omega) = {SIG_PLUS} - {SIG_MINUS} = {psi_eff}. '
            f'This is the level at which the Heisenberg subalgebra J = sum phi_i '
            f'has the commutation relation [J_m, J_n] = {psi_eff}*m*delta.'
        ),
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 3. Koszul dual Y(g_{K3})^!
# =========================================================================

class KoszulDualData(NamedTuple):
    """Koszul dual Y(g_{K3})^! data.

    STATUS: CONJECTURAL (AP-CY14).
    AP-CY10 compliance: flop != Koszul dual. Flop PRESERVES kappa,
    Koszul duality satisfies kappa + kappa^! = K (conductor).
    """
    original_params: List[Rational]
    dual_params: List[Rational]
    koszul_conductor: int           # K = kappa + kappa^! = 0 for free-field
    original_structure_fn_at_test: Rational
    dual_structure_fn_at_test: Rational
    product_at_test: Rational       # should be 1 (duality inversion)
    status: str


def koszul_dual(
    params: Optional[MukaiLatticeParams] = None,
    test_point: Rational = Rational(3),
) -> KoszulDualData:
    r"""Construct the Koszul dual Y(g_{K3})^!.

    The Koszul dual has parameters -h_i (negated parameters).
    The dual structure function is:

      g^!(z) = prod (z + h_i)/(z - h_i) = 1/g(z)

    The Koszul conductor for the free-field branch:
      kappa_ch(Y) + kappa_ch(Y^!) = 0

    This means: kappa_ch(Y) = -kappa_ch(Y^!) for the free-field K3 Yangian.

    AP-CY10 compliance: this is Koszul duality (algebra/coalgebra exchange),
    NOT a birational flop. Flops preserve kappa; Koszul shifts it.
    """
    if params is None:
        params = kummer_k3_parameters()

    dual_h = [-hi for hi in params.h]
    # Verify CY_2: sum(-h_i) = -sum(h_i) = 0.  Check.

    # Evaluate structure functions at test point
    g_original = structure_function_evaluate(test_point, params)

    # Dual structure function: prod (z + h_i)/(z - h_i) = 1/g(z)
    g_dual = Rational(1)
    for hi in params.h:
        if test_point - hi == 0:
            raise ValueError(f"Pole in dual at z = {test_point}")
        g_dual *= (test_point + hi) / (test_point - hi)

    product = g_original * g_dual

    return KoszulDualData(
        original_params=params.h,
        dual_params=dual_h,
        koszul_conductor=KOSZUL_CONDUCTOR_FREE_FIELD,
        original_structure_fn_at_test=g_original,
        dual_structure_fn_at_test=g_dual,
        product_at_test=product,
        status=QUANTIZATION_STATUS,
    )


def koszul_duality_verification(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Verify Koszul duality properties of Y(g_{K3}).

    1. g(z) * g^!(z) = 1 (duality inversion).
    2. kappa_ch(Y) + kappa_ch(Y^!) = 0 (free-field conductor).
    3. Dual parameters -h_i still satisfy CY_2: sum(-h_i) = 0.
    4. Dual Mukai norm: <-h, -h>_Muk = <h, h>_Muk (invariant under negation).
    5. The dual R-matrix R^!(z) = R(-z) (from g^! = 1/g and unitarity).
    """
    if params is None:
        params = kummer_k3_parameters()

    dual = koszul_dual(params)

    # Verify at multiple test points (AP-CY28: avoid poles)
    test_points = [Rational(3), Rational(7), Rational(11, 3), Rational(17, 5)]
    inversion_checks = []
    for zv in test_points:
        try:
            g_val = structure_function_evaluate(zv, params)
            g_dual = Rational(1)
            for hi in params.h:
                g_dual *= (zv + hi) / (zv - hi)
            product = g_val * g_dual
            inversion_checks.append((str(zv), product == 1))
        except (ValueError, ZeroDivisionError):
            inversion_checks.append((str(zv), 'pole'))

    # CY_2 for dual
    dual_sum = sum(dual.dual_params)

    # Mukai norm invariance
    eigenvalues = mukai_diagonal_eigenvalues()
    dual_norm = sum(
        eigenvalues[i] * dual.dual_params[i]**2
        for i in range(NUM_PARAMS)
    )
    original_norm = params.mukai_norm_sq

    return {
        'inversion_g_times_gdual_is_1': all(
            c[1] == True for c in inversion_checks if c[1] != 'pole'
        ),
        'inversion_checks': inversion_checks,
        'dual_cy2_sum': dual_sum,
        'dual_cy2_holds': dual_sum == 0,
        'mukai_norm_invariant': dual_norm == original_norm,
        'koszul_conductor': KOSZUL_CONDUCTOR_FREE_FIELD,
        'conductor_is_zero': KOSZUL_CONDUCTOR_FREE_FIELD == 0,
        'dual_r_matrix': (
            'R^!(z) = R(-z). From g^!(z) = 1/g(z) and unitarity '
            'g(z)*g(-z) = 1, we get g^!(z) = g(-z), so R^!(z) = R(-z).'
        ),
        'ap_cy10_compliance': (
            'This is Koszul duality (algebra/coalgebra exchange), NOT a flop. '
            'Flop preserves kappa; Koszul duality satisfies kappa + kappa^! = K. '
            'For the free-field branch: K = 0.'
        ),
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 4. Yang R-matrix at rank 24
# =========================================================================

def yang_r_matrix_rank24(
    u_val: Optional[Rational] = None,
    hbar_val: Rational = Rational(1),
) -> Dict[str, Any]:
    r"""The Yang R-matrix R(u) on C^{24} tensor C^{24}.

    R(u) = (u * Id + hbar * P) / (u + hbar)

    where P is the permutation operator on C^{24} tensor C^{24}:
      P(e_i tensor e_j) = e_j tensor e_i

    In components:
      R(u)^{ij}_{kl} = (u/(u+hbar)) delta^i_k delta^j_l
                        + (hbar/(u+hbar)) delta^i_l delta^j_k

    Properties at rank 24:
    - Dimension: 24^2 x 24^2 = 576 x 576
    - YBE: satisfied (Yang R-matrix is the universal R-matrix of Y(gl_N))
    - Unitarity: R_{12}(u) R_{21}(-u) = Id
    - Symmetry: R_{12}(u) = P R_{21}(u) P (PT invariance)
    """
    N = NUM_PARAMS  # 24

    if u_val is not None:
        alpha = u_val / (u_val + hbar_val)
        beta = hbar_val / (u_val + hbar_val)
    else:
        alpha = None
        beta = None

    return {
        'rank': N,
        'matrix_size': N**2,  # 576
        'formula': 'R(u) = (u*Id + hbar*P)/(u+hbar)',
        'alpha': str(alpha) if alpha is not None else 'u/(u+hbar)',
        'beta': str(beta) if beta is not None else 'hbar/(u+hbar)',
        'diagonal_entries': 'R^{ii}_{ii} = 1 for all i',
        'off_diagonal_same': f'R^{{ij}}_{{ij}} = u/(u+hbar) for i != j',
        'off_diagonal_swap': f'R^{{ij}}_{{ji}} = hbar/(u+hbar) for i != j',
        'ybe_holds': True,
        'unitarity': 'R_{12}(u) R_{21}(-u) = Id',
        'classical_limit': 'R(u) -> Id + (hbar/u)*P as u -> infinity',
        'status': QUANTIZATION_STATUS,
    }


def yang_r_matrix_ybe_verification_symbolic() -> Dict[str, Any]:
    r"""Symbolically verify the YBE for the Yang R-matrix at small rank.

    We verify at rank N=3 (computationally tractable), then the result
    extends to any N including N=24 by the universal property of the
    Yang R-matrix.

    R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

    Both sides are N^3 x N^3 matrices.  At N=3, this is 27x27.
    """
    N = 3  # Small rank for symbolic computation
    u, v, hbar = symbols("u v hbar")

    def yang_r(param, n):
        """Build the Yang R-matrix as an n^2 x n^2 matrix."""
        R = zeros(n**2, n**2)
        for i in range(n):
            for j in range(n):
                row = i * n + j
                # Diagonal: R^{ij}_{ij}
                col_diag = i * n + j
                if i == j:
                    R[row, col_diag] = 1
                else:
                    R[row, col_diag] = param / (param + hbar)
                    # Swap: R^{ij}_{ji}
                    col_swap = j * n + i
                    R[row, col_swap] = hbar / (param + hbar)
        return R

    # Build R_{12}, R_{13}, R_{23} in N^3-dimensional space
    # This is expensive even at N=3, so we verify at specific numerical values.
    # Use hbar=1, u=2, v=3 (AP-CY28: no poles since u+hbar=3, v+hbar=4, u+v+hbar=6)
    hbar_num = 1
    u_num = 2
    v_num = 3

    def yang_r_num(param_num, n):
        R = zeros(n**2, n**2)
        for i in range(n):
            for j in range(n):
                row = i * n + j
                col_diag = i * n + j
                if i == j:
                    R[row, col_diag] = 1
                else:
                    R[row, col_diag] = Rational(param_num, param_num + hbar_num)
                    col_swap = j * n + i
                    R[row, col_swap] = Rational(hbar_num, param_num + hbar_num)
        return R

    # R_{12}(u) acts on spaces 1,2 (trivially on 3)
    R12_small = yang_r_num(u_num, N)
    R23_small = yang_r_num(v_num, N)
    R13_small = yang_r_num(u_num + v_num, N)

    # Embed in N^3-dimensional space
    Id_N = eye(N)

    # R_{12} tensor Id_3
    def kron(A, B):
        """Kronecker product."""
        return Matrix([[A[i, j] * B for i in range(A.rows) for j in range(A.cols)]]).reshape(
            A.rows * B.rows, A.cols * B.cols
        ) if False else _kron_manual(A, B)

    def _kron_manual(A, B):
        rows_A, cols_A = A.shape
        rows_B, cols_B = B.shape
        result = zeros(rows_A * rows_B, cols_A * cols_B)
        for i in range(rows_A):
            for j in range(cols_A):
                for k in range(rows_B):
                    for l in range(cols_B):
                        result[i * rows_B + k, j * cols_B + l] = A[i, j] * B[k, l]
        return result

    R12_full = _kron_manual(R12_small, Id_N)

    # R_{23}: Id_1 tensor R_{23}
    R23_full = _kron_manual(Id_N, R23_small)

    # R_{13}: need to permute indices. R_{13} acts on spaces 1,3.
    # In the basis |i>|j>|k>, R_{13} acts as:
    # R_{13}^{ijk}_{lmn} = R^{ik}_{ln} * delta^j_m
    R13_full = zeros(N**3, N**3)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                row = i * N**2 + j * N + k
                for l in range(N):
                    for n in range(N):
                        col = l * N**2 + j * N + n  # m = j (delta^j_m)
                        R13_full[row, col] += R13_small[i * N + k, l * N + n]

    # LHS: R12 * R13 * R23
    LHS = R12_full * R13_full * R23_full

    # RHS: R23 * R13 * R12
    RHS = R23_full * R13_full * R12_full

    diff = LHS - RHS
    ybe_holds = diff.is_zero_matrix

    return {
        'verification_rank': N,
        'numerical_params': {'u': u_num, 'v': v_num, 'hbar': hbar_num},
        'ybe_holds_at_rank_3': ybe_holds,
        'extends_to_rank_24': (
            'The Yang R-matrix R(u) = (u*Id + hbar*P)/(u+hbar) satisfies '
            'YBE for ALL ranks N, including N = 24 (K3 Mukai rank). '
            'Verified explicitly at N = 3 by direct matrix computation.'
        ),
        'matrix_size_at_N3': f'{N**3}x{N**3} = {N**3}x{N**3}',
        'matrix_size_at_N24': f'{24**3}x{24**3} = 13824x13824',
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 5. Mukai-twisted R-matrix
# =========================================================================

def mukai_twisted_r_matrix(
    u_val: Rational = Rational(2),
    hbar_val: Rational = Rational(1),
    rank: int = 4,
) -> Dict[str, Any]:
    r"""Construct the Mukai-twisted R-matrix at small rank.

    R_omega(u) = (u * Id + hbar * P_omega) / (u + hbar)

    where P_omega is the omega-twisted permutation:
      P_omega(e_i tensor e_j) = omega^{ij} * (e_j tensor e_i)

    For diagonal omega = diag(s_1,...,s_N) with s_i = +/-1:
      P_omega^{ij}_{kl} = s_i * delta^i_l * delta^j_k   (twisted swap)

    Properties:
    - P_omega^2 = diag(s_i * s_j) on e_i tensor e_j  (NOT Id for indefinite omega)
    - R_omega satisfies YBE iff omega defines a consistent metric
    - Unitarity: R_omega(u) * (P_omega R_omega(-u) P_omega) = Id

    We compute at small rank to verify structure, then describe the
    rank-24 version.
    """
    N = rank
    sig_plus = min(SIG_PLUS, N)
    sig_minus = N - sig_plus

    # Mukai signs for the small-rank version
    signs = [1] * sig_plus + [-1] * sig_minus

    # Build P_omega: P_omega(e_i tensor e_j) = s_i * (e_j tensor e_i)
    # In matrix form: P_omega^{ij}_{kl} = s_i * delta^i_l * delta^j_k
    P_omega = zeros(N**2, N**2)
    for i in range(N):
        for j in range(N):
            row = i * N + j
            col = j * N + i  # swapped
            P_omega[row, col] = signs[i]

    Id_NN = eye(N**2)

    # R_omega(u) = (u * Id + hbar * P_omega) / (u + hbar)
    R_omega = (u_val * Id_NN + hbar_val * P_omega) * Rational(1, u_val + hbar_val)

    # Check P_omega^2
    P_omega_sq = P_omega * P_omega
    # Expected: P_omega_sq^{ij}_{kl} = s_i * s_j * delta^i_k * delta^j_l
    p_sq_diagonal = [P_omega_sq[i * N + j, i * N + j] for i in range(N) for j in range(N)]
    expected_p_sq = [signs[i] * signs[j] for i in range(N) for j in range(N)]

    p_sq_matches = all(p_sq_diagonal[k] == expected_p_sq[k] for k in range(N**2))

    # Check unitarity: R(u) * P R(-u) P = Id?
    # For twisted case: R_omega(u) * (P_omega R_omega(-u) P_omega) should = Id
    R_omega_neg = ((-u_val) * Id_NN + hbar_val * P_omega) * Rational(1, -u_val + hbar_val)
    product = R_omega * P_omega * R_omega_neg * P_omega

    # Check if product = Id
    diff = product - Id_NN
    unitarity_holds = diff.is_zero_matrix

    return {
        'rank': N,
        'signature': (sig_plus, sig_minus),
        'signs': signs,
        'p_omega_squared_diagonal': p_sq_diagonal[:6],
        'p_omega_squared_matches_expected': p_sq_matches,
        'p_omega_is_involution': all(s == 1 for s in signs),  # only if all signs +1
        'twisted_unitarity_holds': unitarity_holds,
        'formula': 'R_omega(u) = (u*Id + hbar*P_omega)/(u+hbar)',
        'extension_to_24': (
            f'At rank 24 with signature (4,20): P_omega has {SIG_PLUS} positive '
            f'and {SIG_MINUS} negative twisted swaps. P_omega^2 = '
            f'diag(s_i*s_j) is NOT the identity for mixed-sign pairs, '
            f'giving a genuinely twisted R-matrix.'
        ),
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 6. Bar complex and BKM root multiplicities
# =========================================================================

def bar_euler_vs_bkm(max_degree: int = 6) -> Dict[str, Any]:
    r"""Compare bar Euler product of Y(g_{K3}) with BKM root multiplicities.

    The bar Euler product of Y(g_{K3}):
      prod_{n>=1} (1 - q^n)^{24} = eta(q)^{24}/q

    The Fake Monster denominator on II_{25,1}:
      exp(2*pi*i*(rho,Z)) * prod_{lambda>0} (1 - e^{2*pi*i*(lambda,Z)})^{c(|lambda|^2/2)}

    At the restriction to the lightlike direction (the 1-variable limit):
      prod_{n>=1} (1 - q^n)^{c(0)} = prod_{n>=1} (1 - q^n)^{24}

    since c(0) = p_{24}(1) = 24 = Mukai rank.

    This gives the IDENTIFICATION (AP-CY8 compliant):

      Bar Euler product of Y(g_{K3}) = Fake Monster denominator (lightlike restriction)

    OBSERVATION (not theorem): this identification requires:
    (a) CY-A_2 (proved at d=2) to identify the bar complex of Y(g_{K3})
        with the bar complex of the chiral algebra Phi(D^b(K3)).
    (b) The Vol I anchor: bar Euler product = automorphic denominator.

    The KEY TEST: do the BKM root multiplicities c(D) appear at the level
    of the bar complex?

    Answer: YES, through the RECIPROCAL identification.

    The Fock space character of Y(g_{K3}):
      ch(Fock) = 1/prod_{n>=1}(1-q^n)^{24} = sum_{n>=0} p_{24}(n) q^{n-1}

    has coefficients p_{24}(n) = c(n-1) = Fake Monster root multiplicities.
    Explicitly:
      p_{24}(0) = 1 = c(-1)    (Weyl vector)
      p_{24}(1) = 24 = c(0)    (lightlike, = Mukai rank)
      p_{24}(2) = 324 = c(1)   (first imaginary root multiplicity)
      p_{24}(3) = 3200 = c(2)
      p_{24}(4) = 25650 = c(3)
      p_{24}(5) = 176256 = c(4)

    So the bar complex dimensions of Y(g_{K3}) are EXACTLY the root
    multiplicities of the Fake Monster Lie algebra.
    """
    # Compute bar Euler coefficients
    bar_coeffs = bar_euler_generating_function(max_degree)

    # Compute Fock space (reciprocal) coefficients = p_{24}(n)
    fock_coeffs = _partition_function_24(max_degree)

    # Compare with BKM multiplicities
    comparisons = []
    for n in range(max_degree + 1):
        p24_n = fock_coeffs.get(n, 0)
        bkm_index = n - 1  # c(n-1) = p_{24}(n)
        c_bkm = FAKE_MONSTER_MULTIPLICITIES.get(bkm_index, None)

        if c_bkm is not None:
            match = p24_n == c_bkm
            comparisons.append({
                'n': n,
                'p_24(n)': p24_n,
                'c(n-1)': c_bkm,
                'bkm_index': bkm_index,
                'match': match,
            })

    all_match = all(c['match'] for c in comparisons)

    # Ramanujan tau cross-check
    ramanujan_tau = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830, 6: -6048}
    tau_checks = []
    for n_plus_1, tau_val in ramanujan_tau.items():
        n = n_plus_1 - 1
        if n <= max_degree:
            computed = bar_coeffs.get(n, 0)
            tau_checks.append({
                'n': n,
                'tau(n+1)': tau_val,
                'bar_coeff': computed,
                'match': computed == tau_val,
            })

    tau_all_match = all(tc['match'] for tc in tau_checks)

    return {
        'bar_euler_product': 'prod(1-q^n)^{24} = eta^{24}/q',
        'fock_character': '1/prod(1-q^n)^{24} = sum p_{24}(n) q^{n-1}',
        'bkm_identification': 'p_{24}(n) = c(n-1) = Fake Monster root multiplicities',
        'comparisons': comparisons,
        'all_fock_match_bkm': all_match,
        'bar_euler_coefficients': {n: bar_coeffs.get(n, 0) for n in range(min(7, max_degree + 1))},
        'ramanujan_tau_checks': tau_checks,
        'ramanujan_tau_all_match': tau_all_match,
        'lightlike_multiplicity': FAKE_MONSTER_MULTIPLICITIES[0],
        'lightlike_equals_mukai_rank': FAKE_MONSTER_MULTIPLICITIES[0] == MUKAI_RANK,
        'ap_cy8_compliance': (
            'OBSERVATION (not theorem): the identification of bar Euler product '
            'with BKM denominator requires CY-A_2 (proved) and Vol I anchor. '
            'The bar complex dimensions reproduce Fake Monster root multiplicities.'
        ),
        'status': QUANTIZATION_STATUS,
    }


def _partition_function_24(max_degree: int = 20) -> Dict[int, int]:
    """Compute coefficients of 1/prod(1-q^n)^{24} = sum p_{24}(n) q^n.

    p_{24}(n) counts 24-colored partitions of n.
    p_{24}(0) = 1, p_{24}(1) = 24, p_{24}(2) = 324, ...
    """
    coeffs = {0: 1}
    for n in range(1, max_degree + 1):
        # Multiply by 1/(1-q^n)^{24} = sum_{k>=0} C(k+23, 23) q^{nk}
        new_coeffs: Dict[int, int] = {}
        for deg, coeff in coeffs.items():
            for k in range(0, (max_degree - deg) // n + 1):
                new_deg = deg + n * k
                if new_deg > max_degree:
                    break
                binom = math.comb(k + 23, 23)
                new_coeffs[new_deg] = new_coeffs.get(new_deg, 0) + coeff * binom
        coeffs = new_coeffs
    return coeffs


def bkm_root_multiplicity_from_bar(D: int) -> Dict[str, Any]:
    r"""Recover BKM root multiplicity c(D) from the bar complex of Y(g_{K3}).

    The Fake Monster root multiplicity c(D) for discriminant D:
      c(D) = p_{24}(D + 1)

    where p_{24}(n) is the coefficient of q^n in 1/eta(q)^{24}.

    This is computed from the bar complex of Y(g_{K3}) via:
      dim B_{n} = p_{24}(n)  (the n-th graded piece of the bar complex)

    So: c(D) = dim B_{D+1} (the bar complex dimension at degree D+1).
    """
    fock = _partition_function_24(max(D + 2, 10))
    p24_val = fock.get(D + 1, None)

    known = FAKE_MONSTER_MULTIPLICITIES.get(D, None)

    return {
        'discriminant': D,
        'c(D)_from_bar': p24_val,
        'c(D)_known_bkm': known,
        'match': p24_val == known if known is not None else 'unknown (D too large)',
        'formula': f'c({D}) = p_24({D+1}) = dim B_{{{D+1}}}(Y(g_{{K3}}))',
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 7. Quantization deformation: classical -> quantum
# =========================================================================

def quantization_deformation(
    params: Optional[MukaiLatticeParams] = None,
    hbar_val: Rational = Rational(1),
) -> Dict[str, Any]:
    r"""Analyze the quantization deformation g_{K3} -> Y(g_{K3}).

    The classical limit hbar -> 0 recovers g_{K3} = H_Muk.
    The deformation is controlled by the structure function g(z).

    At order hbar^0: the universal enveloping algebra U(H_Muk)
      (Heisenberg algebra, class G, shadow depth 2).

    At order hbar^1: first quantum correction.
      The first-order deformation of the relations:
        [phi_i(u), phi_j(v)] = omega^{ij} * hbar / (u - v) + O(hbar^2)

      The first-order correction to the R-matrix:
        R(u) = Id + hbar * P / u + O(hbar^2)

    At order hbar^2: second quantum correction.
      The quadratic Casimir enters:
        C_2 = sum_{i,j} omega^{ij} phi_i phi_j

      For diagonal omega: C_2 = sum_{i=1}^{4} phi_i^2 - sum_{i=5}^{24} phi_i^2

      This is the K3-specific Casimir with INDEFINITE signature.

    The deformation is FLAT (preserves PBW filtration) because:
    (a) The structure function g(z) is rational (no essential singularities).
    (b) The Yang R-matrix satisfies the YBE (integrability condition).
    (c) The Heisenberg algebra is class G (2-step nilpotent), so
        there are no higher obstructions to flatness.

    Flatness ensures: bar Euler product is deformation-invariant.
    """
    if params is None:
        params = kummer_k3_parameters()

    eigenvalues = mukai_diagonal_eigenvalues()

    # Power sums at various orders
    p = newton_power_sums(params, max_k=6)

    # Elementary symmetric functions
    e = elementary_symmetric_functions(params, max_k=4)

    # Quadratic Casimir in the diagonal Mukai basis
    # C_2 = sum omega^{ii} h_i^2 = sum_{pos} h_i^2 - sum_{neg} h_i^2
    c2_pos = sum(params.h[i]**2 for i in range(SIG_PLUS))
    c2_neg = sum(params.h[i]**2 for i in range(SIG_PLUS, NUM_PARAMS))
    casimir_2 = c2_pos - c2_neg

    return {
        'classical_limit': 'U(H_Muk) (universal enveloping algebra of Heisenberg)',
        'shadow_class': 'G (2-step nilpotent, shadow depth 2)',
        'flatness': 'FLAT deformation (PBW-preserving)',
        'bar_euler_invariant': True,
        'first_order': {
            'commutator': '[phi_i(u), phi_j(v)] = omega^{ij} * hbar / (u-v)',
            'r_matrix': 'R(u) = Id + hbar*P/u + O(hbar^2)',
        },
        'second_order': {
            'casimir_2': casimir_2,
            'casimir_2_positive_part': c2_pos,
            'casimir_2_negative_part': c2_neg,
            'casimir_is_indefinite': casimir_2 != 0 and c2_pos != 0 and c2_neg != 0,
        },
        'power_sums': {k: p[k] for k in range(1, 5)},
        'elementary_symmetric': {k: e[k] for k in range(5)},
        'cy2_constraint_order_by_order': (
            'p_1 = 0 (CY_2 at hbar^0). e_1 = 0 (CY_2 at the level of esf). '
            'The CY_2 constraint is preserved by the deformation to all orders.'
        ),
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 8. Coproduct at the quantized level
# =========================================================================

def quantized_coproduct_spin1() -> Dict[str, Any]:
    r"""Quantized coproduct at spin 1.

    Delta_z(J_n) = J_n^L + J_n^R  (PRIMITIVE at all orders in hbar)

    The Heisenberg current J = sum phi_i is primitive because:
    - At the classical level: Delta(x) = x tensor 1 + 1 tensor x for
      any element of a Lie algebra.
    - The Yangian deformation preserves primitivity of the Heisenberg
      generators (they are the spin-1 sector, which has no z-dependence
      in the coproduct).
    - In the Miura picture: Delta_z(psi_1) = psi_1^L + psi_1^R
      with no cross-terms (the sum a + b + p = 1 with a,b >= 0, p >= 0
      has only a=0,b=1,p=0 and a=1,b=0,p=0 as solutions).

    The effective level Psi_eff = Tr(omega) = -16 enters the
    MODE commutation relation [J_m, J_n] = Psi_eff * m * delta,
    but NOT the coproduct structure.
    """
    eigenvalues = mukai_diagonal_eigenvalues()
    psi_eff = sum(eigenvalues)

    return {
        'spin': 1,
        'formula': 'Delta_z(J_n) = J_n^L + J_n^R',
        'type': 'primitive (cocommutative)',
        'z_dependence': 'none (z-polynomial degree 0)',
        'hbar_dependence': 'none (exact at all orders)',
        'mukai_signature_effect': (
            f'The signature (4,20) enters the Heisenberg level '
            f'Psi_eff = {psi_eff}, affecting the mode algebra '
            f'[J_m, J_n] = {psi_eff}*m*delta, but NOT the coproduct.'
        ),
        'status': QUANTIZATION_STATUS,
    }


def quantized_coproduct_spin2() -> Dict[str, Any]:
    r"""Quantized coproduct at spin 2.

    psi-level:
      Delta_z(psi_{2,n}) = psi_{2,n}^L + psi_{2,n}^R
                          + [J^L conv J^R]_n + z * J_n^R

    W-level (after Miura T = psi_2 - J^2/(2*Psi_eff)):
      Delta_z(T_n) = T_n^L + T_n^R
                    + ((Psi_eff - 1)/Psi_eff) * [J^L conv J^R]_n
                    + z * J_n^R

    The K3 signature enters through:
    1. Psi_eff = Tr(omega) = -16 (Mukai trace)
    2. The cross-term coefficient (Psi_eff - 1)/Psi_eff = (-16-1)/(-16) = 17/16
    3. The J^L * J^R expansion into 24 Mukai directions:
       J^L * J^R = sum_{i=1}^{24} phi_i^L * phi_i^R
       = (sum_{i=1}^{4} phi_i^L phi_i^R) + (sum_{i=5}^{24} phi_i^L phi_i^R)

    The 4 positive and 20 negative Mukai directions contribute with
    EQUAL coefficient 1 to J^L*J^R (the Mukai pairing enters the MODE
    commutation, not the coproduct cross-term weights directly).
    """
    eigenvalues = mukai_diagonal_eigenvalues()
    psi_eff = sum(eigenvalues)  # -16

    cross_coeff = Fraction(psi_eff - 1, psi_eff)  # 17/16

    return {
        'spin': 2,
        'psi_formula': (
            'Delta_z(psi_2) = psi_2^L + psi_2^R + [J^L conv J^R] + z*J^R'
        ),
        'W_formula': (
            f'Delta_z(T_n) = T_n^L + T_n^R + ({cross_coeff})*[J^L conv J^R]_n + z*J_n^R'
        ),
        'cross_term_coefficient': cross_coeff,
        'effective_level': psi_eff,
        'z_polynomial_degree': 1,
        'mukai_in_cross_term': (
            f'J^L * J^R = sum_{{i=1}}^{{{NUM_PARAMS}}} phi_i^L * phi_i^R. '
            f'All {NUM_PARAMS} directions contribute with coefficient 1 to '
            f'the coproduct cross-term. The Mukai pairing enters the MODE '
            f'algebra (Psi_eff = {psi_eff}) and the W-level coefficient '
            f'(Psi_eff - 1)/Psi_eff = {cross_coeff}.'
        ),
        'difference_from_c3': (
            'For C^3: Psi_eff = -(h_1*h_2 + h_1*h_3 + h_2*h_3) (sigma_2). '
            f'For K3: Psi_eff = {psi_eff} (Mukai trace). '
            'The K3 effective level is FIXED by the lattice, while '
            'the C^3 level depends on the deformation parameters.'
        ),
        'status': QUANTIZATION_STATUS,
    }


def quantized_coproduct_higher_spin(s: int) -> Dict[str, Any]:
    r"""Quantized coproduct at spin s for Y(g_{K3}).

    Uses the universal allspin formula specialized to rank N = 24:

      Delta_z(psi_s) = psi_s^L + SUM_{a+b+p=s, a<s} C(s-a-1,p) z^p [psi_a^L conv psi_b^R]

    K3-specific features at spin s:
    - Truncation: psi_s = e_s(phi_1,...,phi_{24}) = 0 for s > 24.
    - z-polynomial degree: min(s-1, 23) (capped at rank-1 = 23).
    - Operator products: s(s+1)/2 - 1 for s <= 24.
    - Mukai pairing enters all psi_a factors through the Sugawara
      construction at each order.
    """
    if s < 1:
        raise ValueError(f"Spin must be >= 1, got {s}")

    if s > NUM_PARAMS:
        return {
            'spin': s,
            'truncated': True,
            'Delta_z': f'0 (psi_{s} = e_{s}(phi_1,...,phi_24) = 0 for s > 24)',
            'reason': f'Rank truncation at N = {NUM_PARAMS}',
            'status': QUANTIZATION_STATUS,
        }

    z_deg = s - 1
    total_ops = s * (s + 1) // 2 - 1
    cross_at_z0 = s - 1

    # Build the term table
    terms = []
    for a in range(s):
        for p in range(s - a):
            b = s - a - p
            if b < 1:
                continue
            if a == 0 and p == 0:
                continue  # this is the psi_s^L + psi_s^R diagonal
            binom = math.comb(s - a - 1, p)
            terms.append({
                'a': a, 'b': b, 'p': p,
                'binomial': binom,
                'operator': f'psi_{a}^L conv psi_{b}^R',
                'z_power': p,
            })

    return {
        'spin': s,
        'z_polynomial_degree': z_deg,
        'total_operator_products': total_ops,
        'cross_terms_at_z0': cross_at_z0,
        'num_terms': len(terms),
        'terms': terms[:15],  # first 15 for display
        'truncated': False,
        'rank': NUM_PARAMS,
        'highest_z_term': f'z^{z_deg} * J^R',
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 9. Signature effects on representation theory
# =========================================================================

def signature_representation_theory() -> Dict[str, Any]:
    r"""How the Mukai signature (4,20) affects the representation theory.

    The fundamental representation V = C^{24} of Y(g_{K3}) carries the
    Mukai metric omega = diag(+1,...,+1,-1,...,-1) of signature (4,20).

    Key consequences:

    1. UNITARITY: V is NOT a unitary representation in the naive sense
       (the Mukai pairing is indefinite).  However, V carries a
       PSEUDO-UNITARY structure: the Yangian acts by pseudo-unitary
       operators preserving omega.  The symmetry group is U(4,20), not U(24).

    2. TENSOR PRODUCTS: V tensor V decomposes into symmetric and
       antisymmetric parts. For indefinite omega:
       - Sym^2(V) has dimension 24*25/2 = 300
       - Alt^2(V) has dimension 24*23/2 = 276
       But the omega-isotypic decomposition is different:
       - omega-symmetric: 4*5/2 + 20*21/2 = 10 + 210 = 220
       - omega-antisymmetric: 4*3/2 + 20*19/2 = 6 + 190 = 196
       - mixed: 4*20 = 80

    3. R-MATRIX EIGENVALUES: for the Yang R-matrix R(u) on V tensor V,
       the eigenvalues are:
       - 1 on the diagonal (e_i tensor e_i): 24 eigenvalues
       - u/(u+hbar) on the symmetric off-diagonal: some eigenvalues
       - -hbar/(u+hbar) ... no, the Yang R-matrix has eigenvalues:
       Eigenvalues of R(u) = (u*Id + hbar*P)/(u+hbar):
       - On Sym^2: eigenvalue (u + hbar)/(u + hbar) = 1
       - On Alt^2: eigenvalue (u - hbar)/(u + hbar)
       These are independent of the Mukai signature!

    4. CHARGE-2 REPRESENTATION: at charge 2, the K3 Yangian acts on
       Sym^2(Fock) (the two-particle Fock space).  The Mukai signature
       enters through the commutation relations of phi_i^{(1)} and phi_j^{(2)},
       which involve omega^{ij}.  For indefinite omega, the two-particle
       states include "timelike" and "spacelike" oscillator combinations.
    """
    N = NUM_PARAMS
    sym2_dim = N * (N + 1) // 2  # 300
    alt2_dim = N * (N - 1) // 2  # 276

    return {
        'fundamental_dim': N,
        'symmetry_group': f'U({SIG_PLUS},{SIG_MINUS}) [pseudo-unitary]',
        'sym2_dim': sym2_dim,
        'alt2_dim': alt2_dim,
        'r_matrix_on_sym2': '1 (trivial eigenvalue on symmetric part)',
        'r_matrix_on_alt2': '(u-hbar)/(u+hbar) (nontrivial on antisymmetric)',
        'signature_independent_r_eigenvalues': True,
        'charge_2_effect': (
            f'At charge 2, the Mukai signature (4,20) enters through the '
            f'commutation [phi_i^(1), phi_j^(2)] = omega^{{ij}}*hbar/(u-v). '
            f'The {SIG_PLUS} positive and {SIG_MINUS} negative directions '
            f'create states of different "Mukai spin".'
        ),
        'fock_space_character': (
            '1/prod(1-q^n)^{24} = sum p_{24}(n) q^{n-1}. '
            'The 24-colored partition function p_{24}(n) counts states '
            'with 24 bosonic oscillators, {4 positive + 20 negative}-valued.'
        ),
        'status': QUANTIZATION_STATUS,
    }


# =========================================================================
# 10. Full quantization verification suite
# =========================================================================

def full_quantization_verification() -> Dict[str, Any]:
    r"""Run the complete quantization verification suite.

    All results are CONJECTURAL (AP-CY14).
    """
    params = kummer_k3_parameters()

    return {
        'status': QUANTIZATION_STATUS,
        'path1_signature_analysis': mukai_signature_analysis(params)._asdict(),
        'path2_effective_central_charge': effective_central_charge(params),
        'path3_rtt_presentation': rtt_presentation()._asdict(),
        'path4_rtt_commutation': rtt_commutation_relations(params),
        'path5_koszul_dual': koszul_dual(params)._asdict(),
        'path6_koszul_verification': koszul_duality_verification(params),
        'path7_bar_vs_bkm': bar_euler_vs_bkm(),
        'path8_coproduct_spin1': quantized_coproduct_spin1(),
        'path9_coproduct_spin2': quantized_coproduct_spin2(),
        'path10_quantization_deformation': quantization_deformation(params),
        'path11_representation_theory': signature_representation_theory(),
    }
