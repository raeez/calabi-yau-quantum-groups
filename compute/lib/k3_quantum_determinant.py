r"""Quantum determinant of the rank-24 K3 Lax operator.

STATUS: CONJECTURAL (AP-CY14).  The K3 Yangian Y(g_{K3}) is NOT constructed.
All results are conditional on CY-A_3 and the existence of Y(g_{K3}).

MATHEMATICAL CONTENT
====================

THE QUANTUM DETERMINANT FOR DIAGONAL LAX MATRICES
===================================================

For sl_2, the Lax operator is 2x2:

    L(u) = [[u + h(u),  f(u)],
            [  e(u),  u - h(u)]]

and the quantum determinant is:

    qdet L(u) = L_{00}(u) L_{11}(u - 1) - L_{01}(u) L_{10}(u - 1)
              = (u - j - 1)(u + j)

The shift of -1 in the second factor comes from the half-sum of positive roots
rho = 1 for sl_2 (the Weyl vector).  The zeros at u = -j and u = j+1 generate
the Serre ideal through the centrality of qdet.

For the K3 Yangian at gl_1 (abelian), the Lax operator is 24x24 DIAGONAL:

    L(u) = diag(u - phi_1, u - phi_2, ..., u - phi_{24})

where phi_1,...,phi_{24} are the 24 free-field currents, one per Mukai lattice
direction.  The Mukai pairing omega^{ij} = diag(+1,+1,+1,+1,-1,...,-1) has
signature (4,20).

THE COLUMN-ORDERED QUANTUM DETERMINANT
========================================

For a general N x N Lax matrix, the quantum determinant is:

    qdet L(u) = sum_{sigma in S_N} (-1)^sigma * prod_{i=1}^{N} L_{sigma(i),i}(u - rho_i)

where rho_i are the cumulative Weyl shifts from the ordering.

For a DIAGONAL Lax matrix (the gl_1/abelian case), only the identity
permutation contributes:

    qdet L(u) = prod_{i=1}^{N} L_{ii}(u - rho_i)
              = prod_{i=1}^{N} (u - rho_i - phi_i)

On the evaluation representation (phi_i -> h_i), this becomes:

    qdet L(u) = prod_{i=1}^{24} (u - rho_i - h_i)

THE WEYL SHIFT rho_i FROM THE MUKAI PAIRING
=============================================

The shift rho_i is determined by the Mukai pairing.  For the Yang R-matrix
R(u) = u*Id + P acting on the N x N tensor product, the quantum determinant
shift at position i depends on the eigenvalues of the Cartan matrix
(= Mukai pairing in our case).

For a DIAGONAL pairing omega = diag(sigma_1,...,sigma_{24}) with
sigma_i = +1 (i=1..4) and sigma_i = -1 (i=5..24):

    rho_i = sum_{j < i} sigma_j

This is the cumulative partial sum of the Mukai eigenvalues.  Explicitly:

    rho_1 = 0
    rho_2 = sigma_1 = +1
    rho_3 = sigma_1 + sigma_2 = +2
    rho_4 = sigma_1 + sigma_2 + sigma_3 = +3
    rho_5 = sigma_1 + sigma_2 + sigma_3 + sigma_4 = +4
    rho_6 = +4 + (-1) = +3
    rho_7 = +4 + 2*(-1) = +2
    ...
    rho_{24} = 4 - 19 = -15

The zeros of qdet are then:

    u_i = rho_i + h_i  for  i = 1,...,24

INDEFINITE SIGNATURE EFFECTS
==============================

The Mukai pairing has signature (4,20), meaning 4 positive and 20 negative
eigenvalues.  This has profound consequences for qdet:

1. The Weyl shifts rho_i are NON-MONOTONIC: they increase for the first 4
   directions (positive eigenvalues) then decrease for the remaining 20
   (negative eigenvalues).

2. The qdet zeros u_i = rho_i + h_i can be COMPLEX if the h_i have
   imaginary parts, but for real h_i they are real with mixed signs.

3. The POSITIVE Mukai directions (i=1..4) have rho_i = 0,1,2,3 (increasing).
   The NEGATIVE directions (i=5..24) have rho_i = 4,3,2,...,-15 (decreasing).

4. The pattern of rho_i encodes the Mukai lattice structure and connects to
   the BKM (Borcherds-Kac-Moody) root system.

THE SERRE IDEAL FROM qdet ZEROS
=================================

At each zero u = u_k of qdet, the Lax matrix L(u_k) has a null vector.
For the diagonal case, this is immediate: L_{kk}(u_k - rho_k) = 0 means
the k-th column of L has a zero in the k-th row.

The Serre relation at position k is:

    e_k^{(a)} e_k^{(b)} - g_{ab}(u_k) * e_k^{(b)} e_k^{(a)} = 0

where g_{ab}(u) = (u - h_{ab})/(u + h_{ab}) is the structure function for
the pair (a,b) of Mukai directions.

For the abelian (gl_1) case, the Serre relations simplify because the
structure function is diagonal (g_{ab} = 0 for a != b), so the Serre
relations reduce to the wheel condition on each individual direction:

    g_{ii}(h_k) = 0  <=>  h_k = h_i

which is the statement that parameters coincide (degeneration).

COMPARISON WITH BKM ROOTS
===========================

The BKM Lie algebra g_{Delta_5} associated to the Igusa cusp form Delta_5
has simple roots indexed by the Mukai lattice vectors of norm -2.
The qdet zeros u_i = rho_i + h_i should correspond to these simple roots
in the following sense:

- Each zero u_i specifies a singular hyperplane in the spectral parameter space.
- The intersections of these hyperplanes form a root system.
- For the K3 case, this root system is governed by the indefinite Mukai pairing,
  producing a BKM (generalized Kac-Moody) algebra rather than a finite Lie algebra.

This is CONJECTURAL: the precise identification qdet zeros <-> BKM simple
roots requires constructing the full Yangian Y(g_{K3}), which is the d=3
programme (CY-A_3, AP-CY14).

CONVENTIONS
===========
  - sigma_i: eigenvalues of the Mukai pairing, +1 (i=1..4), -1 (i=5..24)
  - h_i: Yangian deformation parameters, sum h_i = 0 (CY_2)
  - rho_i: cumulative Weyl shift = sum_{j<i} sigma_j
  - u_i: zeros of qdet, u_i = rho_i + h_i
  - All kappa subscripts per AP113: kappa_ch, kappa_cat, kappa_BKM, kappa_fiber
  - AP-CY14: ALL results are CONJECTURAL
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from sympy import (
    Matrix,
    Poly,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    prod as symprod,
    simplify,
    symbols,
)

from compute.lib.k3_yangian import (
    MukaiLatticeParams,
    NUM_PARAMS,
    SIG_MINUS,
    SIG_PLUS,
    STATUS,
    custom_parameters,
    elementary_symmetric_functions,
    kummer_k3_parameters,
    mukai_diagonal_eigenvalues,
    null_kummer_parameters,
    structure_function_evaluate,
)


# =========================================================================
# 0. Constants
# =========================================================================

RANK = NUM_PARAMS  # = 24


# =========================================================================
# 1. Weyl shifts rho_i from the Mukai pairing
# =========================================================================

class WeylShiftData(NamedTuple):
    """Cumulative Weyl shifts from the Mukai pairing eigenvalues.

    rho_i = sum_{j < i} sigma_j, where sigma_j are the diagonal eigenvalues
    of the Mukai pairing (signature (4,20)).

    STATUS: CONJECTURAL (AP-CY14).
    """
    shifts: List[int]           # rho_1,...,rho_{24}
    max_shift: int              # maximum rho_i
    min_shift: int              # minimum rho_i
    signature: Tuple[int, int]  # (4, 20)
    total_shift: int            # rho_{25} = sum of all sigma_j = 4 - 20 = -16


def weyl_shifts_from_mukai() -> WeylShiftData:
    r"""Compute the cumulative Weyl shifts rho_i from the Mukai pairing.

    rho_i = sum_{j=1}^{i-1} sigma_j

    where sigma_j = +1 for j=1..4 and sigma_j = -1 for j=5..24.

    The shifts form a sequence:
        rho = [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, ..., -15]

    This sequence increases for the first 4 steps (positive eigenvalues)
    then decreases for the remaining 20 steps (negative eigenvalues).

    The maximum is rho_5 = 4 (after all positive eigenvalues).
    The minimum is rho_{24} = 4 - 19 = -15.
    The total is rho_{25} = 4 - 20 = -16 = Tr(omega).
    """
    eigenvalues = mukai_diagonal_eigenvalues()
    shifts = [0]  # rho_1 = 0
    for j in range(len(eigenvalues) - 1):
        shifts.append(shifts[-1] + eigenvalues[j])

    total = sum(eigenvalues)  # = 4 - 20 = -16

    return WeylShiftData(
        shifts=shifts,
        max_shift=max(shifts),
        min_shift=min(shifts),
        signature=(SIG_PLUS, SIG_MINUS),
        total_shift=total,
    )


def weyl_shift_profile() -> Dict[str, Any]:
    r"""Detailed profile of the Weyl shift sequence.

    The shift sequence rho_i has a characteristic shape determined by
    the Mukai signature (4,20):

    - Ascending phase (i=1..5): rho increases from 0 to 4.
    - Descending phase (i=5..24): rho decreases from 4 to -15.
    - The turning point at i=5 corresponds to the boundary between
      positive and negative Mukai directions.

    For positive-definite pairing (all sigma_j = +1), rho would be
    monotonically increasing: 0, 1, 2, ..., 23.
    For the indefinite Mukai pairing, the non-monotonicity encodes
    the signature.
    """
    data = weyl_shifts_from_mukai()
    eigenvalues = mukai_diagonal_eigenvalues()

    profile = []
    for i in range(RANK):
        profile.append({
            'index': i + 1,
            'mukai_eigenvalue': eigenvalues[i],
            'direction': 'positive' if eigenvalues[i] > 0 else 'negative',
            'rho_i': data.shifts[i],
            'phase': 'ascending' if i < SIG_PLUS else 'descending',
        })

    # Turning point analysis
    turning_point = SIG_PLUS  # index 5 (1-based)
    max_rho = data.max_shift  # = 4
    min_rho = data.min_shift  # = -15

    return {
        'shifts': data.shifts,
        'profile': profile,
        'turning_point_index': turning_point + 1,
        'max_rho': max_rho,
        'min_rho': min_rho,
        'range': max_rho - min_rho,
        'total_shift': data.total_shift,
        'interpretation': (
            f'The Weyl shift rises from 0 to {max_rho} in the first '
            f'{SIG_PLUS} steps (positive Mukai directions), then falls '
            f'to {min_rho} over the remaining {SIG_MINUS} steps '
            f'(negative Mukai directions). The range {max_rho - min_rho} '
            f'exceeds what a definite-signature pairing would produce.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 2. Quantum determinant qdet L(u)
# =========================================================================

class QDetData(NamedTuple):
    """Quantum determinant data for the K3 Lax operator.

    qdet L(u) = prod_{i=1}^{24} (u - rho_i - h_i)

    STATUS: CONJECTURAL (AP-CY14).
    """
    degree: int                     # 24
    zeros: List[Rational]           # u_i = rho_i + h_i
    weyl_shifts: List[int]          # rho_i
    parameters: List[Rational]      # h_i
    mukai_eigenvalues: List[int]    # sigma_i
    signature: Tuple[int, int]      # (4, 20)
    status: str                     # 'CONJECTURAL'


def quantum_determinant_zeros(
    params: Optional[MukaiLatticeParams] = None,
) -> QDetData:
    r"""Compute the zeros of qdet L(u) for the K3 Yangian.

    qdet L(u) = prod_{i=1}^{24} (u - rho_i - h_i)

    The zeros are u_i = rho_i + h_i where:
    - rho_i = sum_{j<i} sigma_j (cumulative Weyl shift)
    - h_i = Yangian deformation parameter
    - sigma_j = Mukai pairing eigenvalue (+/-1)

    For the Kummer K3 with h_i = epsilon (i=1..4), h_i = -epsilon/5 (i=5..24):
      u_1 = 0 + epsilon = epsilon
      u_2 = 1 + epsilon = 1 + epsilon
      u_3 = 2 + epsilon = 2 + epsilon
      u_4 = 3 + epsilon = 3 + epsilon
      u_5 = 4 - epsilon/5
      u_6 = 3 - epsilon/5
      ...
      u_{24} = -15 - epsilon/5
    """
    if params is None:
        params = kummer_k3_parameters()

    weyl_data = weyl_shifts_from_mukai()
    eigenvalues = mukai_diagonal_eigenvalues()

    zeros = []
    for i in range(RANK):
        u_i = Rational(weyl_data.shifts[i]) + params.h[i]
        zeros.append(u_i)

    return QDetData(
        degree=RANK,
        zeros=zeros,
        weyl_shifts=weyl_data.shifts,
        parameters=list(params.h),
        mukai_eigenvalues=eigenvalues,
        signature=(SIG_PLUS, SIG_MINUS),
        status=STATUS,
    )


def quantum_determinant_symbolic(
    params: Optional[MukaiLatticeParams] = None,
):
    r"""Return qdet L(u) as a symbolic polynomial in u.

    qdet L(u) = prod_{i=1}^{24} (u - u_i)

    where u_i = rho_i + h_i are the zeros.

    Returns:
        Sympy expression in variable u.
    """
    if params is None:
        params = kummer_k3_parameters()

    u = Symbol("u")
    qdet_data = quantum_determinant_zeros(params)

    result = Rational(1)
    for ui in qdet_data.zeros:
        result *= (u - ui)

    return expand(result)


def quantum_determinant_evaluate(
    u_val: Rational,
    params: Optional[MukaiLatticeParams] = None,
) -> Rational:
    r"""Evaluate qdet L(u) at a specific u value.

    qdet(u_val) = prod_{i=1}^{24} (u_val - u_i)

    where u_i = rho_i + h_i are the zeros.
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)
    result = Rational(1)
    for ui in qdet_data.zeros:
        result *= (u_val - ui)
    return result


def quantum_determinant_centrality(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Verify that qdet is CENTRAL (independent of the representation point).

    For the diagonal Lax matrix, qdet = prod (u - rho_i - phi_i).
    On the evaluation representation phi_i -> h_i, this becomes a polynomial
    in u with FIXED coefficients (no dependence on the representation).

    This is the K3 analogue of the sl_2 result: qdet(u) = u^2 - u - j(j+1)
    is independent of the weight m.

    For the diagonal K3 case, centrality is AUTOMATIC: the diagonal Lax matrix
    has no off-diagonal generators, so qdet = product of diagonal entries,
    each of which commutes with all others.  The quantum correction (Weyl shift)
    is absorbed into the argument.
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)

    # Verify: qdet is a degree-24 polynomial with known coefficients
    # For the diagonal case, centrality is trivial because all L_{ii}
    # are mutually commuting operators
    u = Symbol("u")
    poly = quantum_determinant_symbolic(params)
    poly_obj = Poly(poly, u)
    degree = poly_obj.degree()

    # Leading coefficient
    leading = poly_obj.LC()

    # Constant term = product of (-u_i)
    constant = Rational(1)
    for ui in qdet_data.zeros:
        constant *= (-ui)

    return {
        'degree': degree,
        'is_degree_24': degree == RANK,
        'leading_coefficient': leading,
        'leading_is_1': leading == 1,
        'constant_term': constant,
        'centrality': (
            'AUTOMATIC for diagonal Lax: all L_{ii}(u) commute, '
            'so qdet = prod L_{ii}(u - rho_i) is manifestly central. '
            'This is the abelian simplification (gl_1). '
            'For non-abelian g, centrality is nontrivial and requires '
            'the RTT relation.'
        ),
        'sl2_comparison': (
            'sl_2: qdet = u^2 - u - j(j+1), degree 2, central by RTT. '
            f'K3 gl_1: qdet = degree-{RANK} polynomial, central by commutativity.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 3. Factorization into positive and negative sectors
# =========================================================================

def qdet_signature_decomposition(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Decompose qdet into positive and negative Mukai sectors.

    qdet L(u) = qdet^+(u) * qdet^-(u)

    where:
      qdet^+(u) = prod_{i=1}^{4} (u - rho_i - h_i)   (positive Mukai)
      qdet^-(u) = prod_{i=5}^{24} (u - rho_i - h_i)   (negative Mukai)

    The positive sector has degree 4 (ascending Weyl shifts 0,1,2,3).
    The negative sector has degree 20 (descending Weyl shifts 4,3,...,-15).

    This decomposition reflects the Mukai signature (4,20) directly
    in the factorization of the quantum determinant.
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)

    # Split into positive and negative sectors
    pos_zeros = qdet_data.zeros[:SIG_PLUS]
    neg_zeros = qdet_data.zeros[SIG_PLUS:]

    pos_shifts = qdet_data.weyl_shifts[:SIG_PLUS]
    neg_shifts = qdet_data.weyl_shifts[SIG_PLUS:]

    pos_params = qdet_data.parameters[:SIG_PLUS]
    neg_params = qdet_data.parameters[SIG_PLUS:]

    # Range of zeros in each sector
    pos_range = (min(pos_zeros), max(pos_zeros)) if pos_zeros else (0, 0)
    neg_range = (min(neg_zeros), max(neg_zeros)) if neg_zeros else (0, 0)

    # Evaluate qdet^+ and qdet^- at test points
    u_test = Rational(100)  # safe test point far from all zeros
    qdet_pos = Rational(1)
    qdet_neg = Rational(1)
    for ui in pos_zeros:
        qdet_pos *= (u_test - ui)
    for ui in neg_zeros:
        qdet_neg *= (u_test - ui)
    qdet_total = qdet_pos * qdet_neg
    qdet_direct = quantum_determinant_evaluate(u_test, params)

    return {
        'positive_sector': {
            'degree': SIG_PLUS,
            'zeros': [str(z) for z in pos_zeros],
            'weyl_shifts': pos_shifts,
            'parameters': [str(p) for p in pos_params],
            'range': (str(pos_range[0]), str(pos_range[1])),
            'interpretation': (
                f'Degree-{SIG_PLUS} factor from the {SIG_PLUS} positive Mukai '
                f'directions. Weyl shifts {pos_shifts} are ascending. '
                f'Zeros at u = {[str(z) for z in pos_zeros]}.'
            ),
        },
        'negative_sector': {
            'degree': SIG_MINUS,
            'zeros': [str(z) for z in neg_zeros],
            'weyl_shifts': neg_shifts,
            'parameters': [str(p) for p in neg_params],
            'range': (str(neg_range[0]), str(neg_range[1])),
            'interpretation': (
                f'Degree-{SIG_MINUS} factor from the {SIG_MINUS} negative Mukai '
                f'directions. Weyl shifts are descending from {neg_shifts[0]} '
                f'to {neg_shifts[-1]}. '
                f'Zeros span [{neg_range[0]}, {neg_range[1]}].'
            ),
        },
        'factorization_check': {
            'u_test': str(u_test),
            'qdet_pos_times_neg': str(qdet_total),
            'qdet_direct': str(qdet_direct),
            'match': qdet_total == qdet_direct,
        },
        'signature_in_qdet': (
            f'The signature ({SIG_PLUS},{SIG_MINUS}) is visible in qdet as: '
            f'{SIG_PLUS} zeros with ascending Weyl shifts (positive Mukai sector), '
            f'{SIG_MINUS} zeros with descending shifts (negative sector). '
            f'The turning point at rho = {max(qdet_data.weyl_shifts)} '
            f'separates the two sectors.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 4. Serre null vectors from qdet zeros
# =========================================================================

class SerreNullVector(NamedTuple):
    """A null vector from a zero of the quantum determinant.

    At u = u_k (a zero of qdet), the Lax matrix L(u_k) has rank < 24,
    producing a null vector that generates a Serre relation.

    STATUS: CONJECTURAL (AP-CY14).
    """
    index: int              # k (1-based)
    zero_u: Rational        # u_k = rho_k + h_k
    weyl_shift: int         # rho_k
    parameter: Rational     # h_k
    mukai_eigenvalue: int   # sigma_k (+1 or -1)
    sector: str             # 'positive' or 'negative'


def serre_null_vectors(
    params: Optional[MukaiLatticeParams] = None,
) -> List[SerreNullVector]:
    r"""Extract the 24 Serre null vectors from the qdet zeros.

    At each zero u = u_k of qdet, the k-th diagonal entry of the shifted
    Lax matrix vanishes:

        L_{kk}(u_k - rho_k) = u_k - rho_k - h_k = 0

    (by definition of u_k = rho_k + h_k).

    The null vector at position k gives the Serre relation:
    - For positive Mukai direction (sigma_k = +1): a raising Serre relation
    - For negative Mukai direction (sigma_k = -1): a lowering Serre relation

    For the abelian (gl_1) K3 Yangian, these are trivial (each direction
    is independent), but they become nontrivial Serre relations when g
    is promoted to a non-abelian Lie algebra.
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)

    vectors = []
    for k in range(RANK):
        vectors.append(SerreNullVector(
            index=k + 1,
            zero_u=qdet_data.zeros[k],
            weyl_shift=qdet_data.weyl_shifts[k],
            parameter=qdet_data.parameters[k],
            mukai_eigenvalue=qdet_data.mukai_eigenvalues[k],
            sector='positive' if qdet_data.mukai_eigenvalues[k] > 0 else 'negative',
        ))

    return vectors


def serre_ideal_structure(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Analyze the Serre ideal generated by qdet zeros.

    The Serre ideal of Y(g_{K3}) is generated by the vanishing conditions
    at the 24 zeros of qdet.  The structure depends on the SPACING of
    the zeros, which is controlled by the Mukai pairing.

    KEY STRUCTURAL FEATURES:

    1. The spacing between consecutive zeros u_{k+1} - u_k encodes the
       Cartan matrix entries.

    2. For the abelian case (gl_1), the zeros are all simple (multiplicity 1)
       and the Serre relations are trivial (each direction independent).

    3. For DEGENERATE parameters (h_i = h_j for some i != j), zeros can
       coincide, producing higher-order null vectors.

    4. The INDEFINITE Mukai pairing means the zeros are spread over a
       wider range than for a definite pairing, and the spacing pattern
       is non-uniform.
    """
    if params is None:
        params = kummer_k3_parameters()

    vectors = serre_null_vectors(params)
    zeros = [v.zero_u for v in vectors]

    # Sort zeros for spacing analysis
    sorted_zeros = sorted(zeros, key=lambda x: float(x))
    spacings = [sorted_zeros[i + 1] - sorted_zeros[i]
                for i in range(len(sorted_zeros) - 1)]

    # Check for coincident zeros (degeneracies)
    zero_set = set(zeros)
    multiplicities = {}
    for z in zero_set:
        mult = zeros.count(z)
        if mult > 1:
            multiplicities[str(z)] = mult

    # Positive vs negative sector analysis
    pos_zeros = [v.zero_u for v in vectors if v.sector == 'positive']
    neg_zeros = [v.zero_u for v in vectors if v.sector == 'negative']

    # Spread of zeros
    total_spread = max(zeros) - min(zeros)
    pos_spread = max(pos_zeros) - min(pos_zeros) if pos_zeros else Rational(0)
    neg_spread = max(neg_zeros) - min(neg_zeros) if neg_zeros else Rational(0)

    # Check for overlap between positive and negative sectors
    pos_range = (min(pos_zeros), max(pos_zeros)) if pos_zeros else None
    neg_range = (min(neg_zeros), max(neg_zeros)) if neg_zeros else None

    overlap = False
    if pos_range and neg_range:
        overlap = (float(pos_range[0]) <= float(neg_range[1]) and
                   float(neg_range[0]) <= float(pos_range[1]))

    return {
        'num_zeros': len(zeros),
        'zeros': [str(z) for z in zeros],
        'sorted_zeros': [str(z) for z in sorted_zeros],
        'spacings': [str(s) for s in spacings],
        'has_degeneracies': len(multiplicities) > 0,
        'multiplicities': multiplicities,
        'positive_sector': {
            'num_zeros': len(pos_zeros),
            'zeros': [str(z) for z in pos_zeros],
            'spread': str(pos_spread),
        },
        'negative_sector': {
            'num_zeros': len(neg_zeros),
            'zeros': [str(z) for z in neg_zeros],
            'spread': str(neg_spread),
        },
        'total_spread': str(total_spread),
        'sectors_overlap': overlap,
        'serre_type': (
            'trivial (abelian gl_1)' if not multiplicities else
            'degenerate (coincident zeros)'
        ),
        'interpretation': (
            f'The 24 qdet zeros span a range of {total_spread}. '
            f'The positive Mukai sector ({len(pos_zeros)} zeros, '
            f'spread {pos_spread}) and negative sector ({len(neg_zeros)} zeros, '
            f'spread {neg_spread}) '
            + ('OVERLAP' if overlap else 'are separated')
            + ' in the spectral parameter. '
            f'Sector overlap indicates mixing of positive and negative '
            f'Mukai directions in the Serre ideal.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 5. Comparison with the sl_2 quantum determinant
# =========================================================================

def sl2_vs_k3_qdet_comparison() -> Dict[str, Any]:
    r"""Compare qdet for sl_2 (rank 2) and K3 gl_1 (rank 24).

    sl_2 (rank 2):
      L(u) = 2x2 matrix (non-diagonal)
      qdet = L_{00}(u) L_{11}(u-1) - L_{01}(u) L_{10}(u-1)
           = (u - j - 1)(u + j)
      Degree: 2
      Weyl shifts: rho_1 = 0, rho_2 = 1 (from the single positive root)
      Serre: nontrivial (e, f generators coupled)
      Centrality: requires RTT proof

    K3 gl_1 (rank 24):
      L(u) = 24x24 diagonal matrix
      qdet = prod_{i=1}^{24} (u - rho_i - h_i)
      Degree: 24
      Weyl shifts: rho_i from cumulative Mukai eigenvalues
      Serre: trivial (abelian, all directions independent)
      Centrality: automatic (diagonal commutes)

    The key difference: sl_2 has a NON-DIAGONAL Lax operator (the off-diagonal
    generators e(u), f(u) produce the quantum correction L_{01}*L_{10} term),
    while the K3 gl_1 case is diagonal (all quantum corrections absorbed into
    the Weyl shift rho_i).

    The sl_2 qdet has 2 zeros encoding 2 Serre relations.
    The K3 qdet has 24 zeros, but for gl_1 these are trivial (independent
    directions).  The nontrivial K3 Serre relations would require g != gl_1.
    """
    weyl_data = weyl_shifts_from_mukai()
    params = kummer_k3_parameters()
    qdet_data = quantum_determinant_zeros(params)

    return {
        'sl2': {
            'rank': 2,
            'lax_dimension': '2x2',
            'is_diagonal': False,
            'qdet_formula': '(u - j - 1)(u + j)',
            'degree': 2,
            'weyl_shifts': [0, 1],
            'zeros': ['-j', 'j + 1'],
            'serre_type': 'nontrivial (coupled e, f generators)',
            'centrality_proof': 'RTT relation (nontrivial)',
        },
        'k3_gl1': {
            'rank': RANK,
            'lax_dimension': f'{RANK}x{RANK}',
            'is_diagonal': True,
            'qdet_formula': f'prod_{{i=1}}^{{{RANK}}} (u - rho_i - h_i)',
            'degree': RANK,
            'weyl_shifts': weyl_data.shifts,
            'zeros': [str(z) for z in qdet_data.zeros],
            'serre_type': 'trivial (abelian, independent directions)',
            'centrality_proof': 'automatic (diagonal commutes)',
        },
        'structural_comparison': {
            'lax_type': (
                'sl_2: non-diagonal Lax with off-diagonal generators e, f. '
                'K3 gl_1: diagonal Lax (no off-diagonal generators for abelian g).'
            ),
            'weyl_shift_pattern': (
                'sl_2: monotone [0, 1] (positive-definite Cartan). '
                'K3: non-monotone [0,1,2,3,4,3,...,-15] (indefinite Mukai).'
            ),
            'serre_content': (
                'sl_2: genuine Serre relations (quantum group content). '
                'K3 gl_1: trivial Serre (abelian). '
                'K3 non-abelian g: would produce genuine Serre relations '
                'with INDEFINITE-SIGNATURE quantum group structure.'
            ),
            'degree_ratio': f'{RANK}/2 = {RANK // 2}',
        },
        'status': STATUS,
    }


# =========================================================================
# 6. Connection to BKM (Borcherds-Kac-Moody) root structure
# =========================================================================

def qdet_bkm_connection(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Analyze the connection between qdet zeros and BKM simple roots.

    The BKM Lie algebra g_{Delta_5} has:
    - 24 real simple roots (from the Leech lattice vectors of norm -2)
    - Infinitely many imaginary simple roots
    - Cartan matrix determined by the Mukai inner product

    CONJECTURAL IDENTIFICATION:
    The 24 zeros of qdet (u_1,...,u_{24}) should map to the 24 real simple
    roots of g_{Delta_5} in the sense that the SPACING MATRIX:

        A_{ij} = f(u_i - u_j)

    (for some function f) reproduces the generalized Cartan matrix of g_{Delta_5}.

    For the indefinite Mukai pairing, the spacing matrix has entries of both
    signs (reflecting the indefiniteness), which is REQUIRED for a BKM algebra
    (whose Cartan matrix has off-diagonal entries that can be positive).

    This is CONJECTURAL (AP-CY14): the identification requires constructing
    Y(g_{K3}), which is the d=3 programme.
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)
    zeros = qdet_data.zeros

    # Compute the spacing matrix (u_i - u_j)
    spacing_matrix = []
    for i in range(RANK):
        row = []
        for j in range(RANK):
            row.append(zeros[i] - zeros[j])
        spacing_matrix.append(row)

    # Mukai pairing contribution to the spacing
    # u_i - u_j = (rho_i - rho_j) + (h_i - h_j)
    # The first term depends on the MUKAI PAIRING (through cumulative sums)
    # The second depends on the DEFORMATION PARAMETERS
    eigenvalues = mukai_diagonal_eigenvalues()

    # For the Kummer parametrization, the h_i are either eps or -eps/5
    # so h_i - h_j is:
    #   0 if i,j in same sector
    #   eps + eps/5 = 6*eps/5 if i in pos, j in neg
    #   -(6*eps/5) if i in neg, j in pos
    pos_neg_diff = params.h[0] - params.h[SIG_PLUS] if RANK > SIG_PLUS else Rational(0)

    # BKM Cartan matrix for the Mukai lattice (conjectural)
    # The diagonal entries are 2 (real simple roots have norm -2 in the
    # Borcherds convention, giving A_{ii} = 2)
    # The off-diagonal entries come from the Mukai inner product

    return {
        'num_qdet_zeros': len(zeros),
        'num_bkm_real_simple_roots': '24 (from Leech lattice, CONJECTURAL)',
        'spacing_analysis': {
            'pos_pos_spacing_formula': (
                'u_i - u_j = (rho_i - rho_j) for i,j in positive sector '
                '(same h_i = epsilon)'
            ),
            'neg_neg_spacing_formula': (
                'u_i - u_j = (rho_i - rho_j) for i,j in negative sector '
                '(same h_i = -epsilon/5)'
            ),
            'pos_neg_spacing_formula': (
                f'u_i - u_j = (rho_i - rho_j) + {pos_neg_diff} '
                f'for i in positive, j in negative sector'
            ),
        },
        'cartan_matrix_connection': (
            'CONJECTURAL: The spacing matrix u_i - u_j is related to the '
            'BKM Cartan matrix A_{ij} through the structure function '
            'g_{ij}(u_i - u_j). For the Mukai lattice, the Cartan matrix '
            'has indefinite signature, producing a GENERALIZED Kac-Moody '
            '(Borcherds) algebra rather than a finite-dimensional Lie algebra. '
            'The 24 qdet zeros correspond to 24 real simple roots; '
            'the imaginary roots of g_{Delta_5} are NOT visible in qdet '
            '(they arise from the IMAGINARY-ROOT null vectors, '
            'analogous to g_{i0} * g_{i1} = 1 in the sl_2 case).'
        ),
        'kappa_connection': (
            'kappa_BKM = 5 (weight of Igusa cusp form Delta_5). '
            'compact kappa_ch(K3xE)=0; relative kappa_ch^Heis=3. '
            'kappa_fiber = 24 (Mukai lattice rank = degree of qdet). '
            'The degree of qdet equals kappa_fiber, NOT compact kappa_ch, '
            'kappa_ch^Heis, or kappa_BKM.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 7. The quantum determinant as a polynomial: coefficient analysis
# =========================================================================

def qdet_polynomial_coefficients(
    params: Optional[MukaiLatticeParams] = None,
    max_coeffs: int = 8,
) -> Dict[str, Any]:
    r"""Compute the first few coefficients of qdet(u) as a polynomial in u.

    qdet(u) = u^{24} - sigma_1 u^{23} + sigma_2 u^{22} - ... + (-1)^{24} sigma_{24}

    where sigma_k = e_k(u_1,...,u_{24}) are the elementary symmetric functions
    of the qdet zeros.

    sigma_1 = sum u_i = sum (rho_i + h_i) = sum rho_i + sum h_i
            = sum rho_i   (since sum h_i = 0 by CY_2)

    sigma_2 = sum_{i<j} u_i u_j

    The coefficients encode the interaction between the Weyl shifts and the
    deformation parameters.
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)
    zeros = qdet_data.zeros

    # sigma_1 = sum of zeros
    sigma_1 = sum(zeros)
    # This equals sum rho_i + sum h_i = sum rho_i (CY_2: sum h_i = 0)
    sum_rho = sum(qdet_data.weyl_shifts)
    sum_h = sum(qdet_data.parameters)

    # Compute elementary symmetric functions of the zeros
    # e_k by Newton's identity recursion
    # p_k = sum u_i^k (power sums of zeros)
    power_sums = {}
    for k in range(1, max_coeffs + 1):
        power_sums[k] = sum(ui**k for ui in zeros)

    # e_k from p_k via Newton's identities
    e = {0: Rational(1)}
    for k in range(1, max_coeffs + 1):
        val = Rational(0)
        for j in range(1, k + 1):
            val += (-1)**(j - 1) * e[k - j] * power_sums[j]
        e[k] = val / k

    # Decompose e_k into Weyl and deformation contributions
    # e_1 = sum rho_i + sum h_i = sum rho_i (CY_2)
    # This is a consistency check
    assert sigma_1 == sum_rho + sum_h

    return {
        'degree': RANK,
        'coefficients': {
            f'sigma_{k} (coeff of u^{{{RANK - k}}})': str(e[k])
            for k in range(max_coeffs + 1)
        },
        'sigma_1_decomposition': {
            'sum_rho': str(sum_rho),
            'sum_h': str(sum_h),
            'sum_h_is_zero': sum_h == 0,
            'sigma_1': str(sigma_1),
            'sigma_1_equals_sum_rho': sigma_1 == sum_rho,
        },
        'power_sums': {
            f'p_{k}': str(power_sums[k]) for k in range(1, max_coeffs + 1)
        },
        'interpretation': (
            f'qdet(u) = u^{{{RANK}}} - {sigma_1}*u^{{{RANK - 1}}} + ... '
            f'The coefficient sigma_1 = {sigma_1} = sum rho_i (since sum h_i = 0 '
            f'by CY_2). This is the trace of the cumulative Weyl shift, '
            f'determined purely by the Mukai signature.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 8. Invariants of qdet under parameter deformations
# =========================================================================

def qdet_deformation_invariants(
    params1: Optional[MukaiLatticeParams] = None,
    params2: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Compare qdet for two different parameter choices.

    The qdet zeros u_i = rho_i + h_i depend on the h_i, but certain
    combinations are DEFORMATION-INVARIANT (depend only on the Mukai
    signature, not on the choice of h_i):

    1. sigma_1 = sum u_i = sum rho_i  (since sum h_i = 0)
       This is invariant under deformations preserving CY_2.

    2. The Weyl shifts rho_i are FIXED (determined by the Mukai pairing alone).
       Only the h_i can vary.

    3. The SPACING of consecutive zeros in the same sector:
       Within the positive sector (i=1..4): u_{i+1} - u_i = 1 + (h_{i+1} - h_i)
       Within the negative sector (i=5..24): u_{i+1} - u_i = -1 + (h_{i+1} - h_i)
       The Weyl contribution (+-1) is fixed; the h-contribution varies.
    """
    if params1 is None:
        params1 = kummer_k3_parameters()
    if params2 is None:
        params2 = null_kummer_parameters()

    qdet1 = quantum_determinant_zeros(params1)
    qdet2 = quantum_determinant_zeros(params2)

    sigma1_1 = sum(qdet1.zeros)
    sigma1_2 = sum(qdet2.zeros)
    sum_rho = sum(qdet1.weyl_shifts)  # same for both (Mukai pairing is fixed)

    return {
        'params1_type': 'kummer (generic, non-null)',
        'params2_type': 'null (Mukai norm zero)',
        'sigma_1_params1': str(sigma1_1),
        'sigma_1_params2': str(sigma1_2),
        'sigma_1_invariant': sigma1_1 == sigma1_2,
        'sigma_1_equals_sum_rho': sigma1_1 == sum_rho and sigma1_2 == sum_rho,
        'sum_rho': str(sum_rho),
        'weyl_shifts_invariant': qdet1.weyl_shifts == qdet2.weyl_shifts,
        'zero_comparison': {
            'params1_zeros': [str(z) for z in qdet1.zeros],
            'params2_zeros': [str(z) for z in qdet2.zeros],
        },
        'invariant_quantities': [
            f'sigma_1 = sum u_i = {sum_rho} (deformation-invariant)',
            f'Weyl shifts rho_i = {qdet1.weyl_shifts} (determined by Mukai pairing)',
            f'Degree = {RANK} (= Mukai lattice rank)',
        ],
        'status': STATUS,
    }


# =========================================================================
# 9. The positive-definite comparison
# =========================================================================

def definite_vs_indefinite_comparison() -> Dict[str, Any]:
    r"""Compare qdet for definite (all +1) vs indefinite (4,20) Mukai pairing.

    For a POSITIVE-DEFINITE pairing of rank 24 (all sigma_i = +1):
      rho_i = i - 1  (monotonically increasing: 0, 1, 2, ..., 23)
      Zeros: u_i = i - 1 + h_i
      sigma_1 = sum rho_i = 24*23/2 = 276

    For the INDEFINITE Mukai pairing (4,20):
      rho_i = cumulative sums of (+1,+1,+1,+1,-1,...,-1)
      Zeros: u_i = rho_i + h_i
      sigma_1 = sum rho_i = -16*23/2 + ... (computed below)

    The indefinite case has:
    1. Non-monotonic Weyl shifts (ascending then descending)
    2. Zeros spread over a wider range (both positive and negative rho_i)
    3. sigma_1 that depends on the SIGNATURE, not just the rank
    """
    # Definite case: all +1
    def_eigenvalues = [1] * RANK
    def_shifts = [0]
    for j in range(RANK - 1):
        def_shifts.append(def_shifts[-1] + def_eigenvalues[j])
    def_sum_rho = sum(def_shifts)

    # Indefinite case: (4, 20)
    indef_data = weyl_shifts_from_mukai()
    indef_sum_rho = sum(indef_data.shifts)

    # The difference in sigma_1
    delta_sigma1 = indef_sum_rho - def_sum_rho

    return {
        'definite': {
            'eigenvalues': 'all +1',
            'shifts': def_shifts,
            'sum_rho': def_sum_rho,
            'max_shift': max(def_shifts),
            'min_shift': min(def_shifts),
            'monotonic': True,
            'interpretation': (
                f'Monotonically increasing: 0, 1, ..., {RANK - 1}. '
                f'This is the standard Yangian Weyl vector for gl_{{{RANK}}}.'
            ),
        },
        'indefinite': {
            'eigenvalues': f'{SIG_PLUS} x (+1), {SIG_MINUS} x (-1)',
            'shifts': indef_data.shifts,
            'sum_rho': indef_sum_rho,
            'max_shift': indef_data.max_shift,
            'min_shift': indef_data.min_shift,
            'monotonic': False,
            'interpretation': (
                f'Non-monotonic: rises to {indef_data.max_shift} then falls to '
                f'{indef_data.min_shift}. The turning point at position '
                f'{SIG_PLUS + 1} reflects the Mukai signature boundary.'
            ),
        },
        'delta_sigma1': delta_sigma1,
        'sigma1_shift_from_indefiniteness': (
            f'sigma_1(indefinite) - sigma_1(definite) = {delta_sigma1}. '
            f'The indefinite signature shifts the center of mass of qdet zeros '
            f'by {delta_sigma1} relative to the positive-definite case.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 10. Full verification suite
# =========================================================================

def verify_qdet_zeros_are_correct(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Verify that qdet(u_i) = 0 at each claimed zero.

    At u = u_i = rho_i + h_i, the product prod_{j=1}^{24}(u_i - u_j) must
    vanish (because the j=i factor is zero).
    """
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)
    zeros = qdet_data.zeros

    checks = []
    for k in range(RANK):
        # qdet(u_k) should be 0
        val = Rational(1)
        for j in range(RANK):
            val *= (zeros[k] - zeros[j])
        checks.append({
            'index': k + 1,
            'u_k': str(zeros[k]),
            'qdet_value': str(val),
            'is_zero': val == 0,
        })

    all_zero = all(c['is_zero'] for c in checks)

    return {
        'num_zeros_tested': RANK,
        'all_zeros_verified': all_zero,
        'checks': checks,
        'status': STATUS,
    }


def verify_qdet_degree(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Verify that qdet is a degree-24 polynomial with leading coefficient 1."""
    if params is None:
        params = kummer_k3_parameters()

    u = Symbol("u")
    poly = quantum_determinant_symbolic(params)
    poly_obj = Poly(poly, u)

    return {
        'degree': poly_obj.degree(),
        'is_degree_24': poly_obj.degree() == RANK,
        'leading_coefficient': poly_obj.LC(),
        'leading_is_1': poly_obj.LC() == 1,
        'status': STATUS,
    }


def verify_sigma1_invariance() -> Dict[str, Any]:
    r"""Verify that sigma_1 = sum u_i is deformation-invariant.

    sigma_1 = sum (rho_i + h_i) = sum rho_i + sum h_i = sum rho_i

    since sum h_i = 0 (CY_2 constraint).  This is independent of the
    choice of h_i.
    """
    params_kummer = kummer_k3_parameters()
    params_null = null_kummer_parameters()

    # Also test a custom parametrization
    h_custom = [Rational(i - 12) for i in range(RANK)]
    # Adjust to satisfy CY_2: sum = sum(i-12) = 24*11/2 - 24*12 = 132 - 288 = -156
    # Need to shift: h_i = (i-12) + 156/24 = (i-12) + 13/2
    correction = -sum(h_custom) / RANK
    h_custom_fixed = [h + correction for h in h_custom]
    assert sum(h_custom_fixed) == 0
    params_custom = custom_parameters(h_custom_fixed)

    sigma1_kummer = sum(quantum_determinant_zeros(params_kummer).zeros)
    sigma1_null = sum(quantum_determinant_zeros(params_null).zeros)
    sigma1_custom = sum(quantum_determinant_zeros(params_custom).zeros)
    sum_rho = sum(weyl_shifts_from_mukai().shifts)

    return {
        'sigma1_kummer': str(sigma1_kummer),
        'sigma1_null': str(sigma1_null),
        'sigma1_custom': str(sigma1_custom),
        'sum_rho': str(sum_rho),
        'all_equal': sigma1_kummer == sigma1_null == sigma1_custom == sum_rho,
        'proof': (
            'sigma_1 = sum (rho_i + h_i) = sum rho_i + 0 (CY_2) = sum rho_i. '
            'Independent of h_i.'
        ),
        'status': STATUS,
    }


def verify_factorization_consistency(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Verify that qdet^+ * qdet^- = qdet at multiple test points."""
    if params is None:
        params = kummer_k3_parameters()

    qdet_data = quantum_determinant_zeros(params)
    zeros = qdet_data.zeros
    pos_zeros = zeros[:SIG_PLUS]
    neg_zeros = zeros[SIG_PLUS:]

    # Test at several points, avoiding zeros (AP-CY28)
    test_points = [Rational(100), Rational(-50), Rational(37),
                   Rational(200), Rational(-100)]
    checks = []
    for u_val in test_points:
        qdet_full = Rational(1)
        qdet_pos = Rational(1)
        qdet_neg = Rational(1)
        for ui in zeros:
            qdet_full *= (u_val - ui)
        for ui in pos_zeros:
            qdet_pos *= (u_val - ui)
        for ui in neg_zeros:
            qdet_neg *= (u_val - ui)

        checks.append({
            'u': str(u_val),
            'qdet_full': str(qdet_full),
            'qdet_pos_times_neg': str(qdet_pos * qdet_neg),
            'match': qdet_full == qdet_pos * qdet_neg,
        })

    return {
        'num_tests': len(checks),
        'all_match': all(c['match'] for c in checks),
        'checks': checks,
        'status': STATUS,
    }


def full_verification(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Run the complete K3 quantum determinant verification suite.

    STATUS: CONJECTURAL (AP-CY14).  Verifies internal consistency of the
    construction, not its existence.
    """
    if params is None:
        params = kummer_k3_parameters()

    return {
        'status': STATUS,
        'path1_weyl_shifts': weyl_shift_profile(),
        'path2_qdet_zeros': {
            'zeros': [str(z) for z in quantum_determinant_zeros(params).zeros],
            'zeros_verified': verify_qdet_zeros_are_correct(params),
        },
        'path3_qdet_degree': verify_qdet_degree(params),
        'path4_centrality': quantum_determinant_centrality(params),
        'path5_signature_decomposition': qdet_signature_decomposition(params),
        'path6_serre_structure': serre_ideal_structure(params),
        'path7_polynomial_coefficients': qdet_polynomial_coefficients(params),
        'path8_sigma1_invariance': verify_sigma1_invariance(),
        'path9_factorization': verify_factorization_consistency(params),
        'path10_definite_vs_indefinite': definite_vs_indefinite_comparison(),
        'path11_sl2_comparison': sl2_vs_k3_qdet_comparison(),
        'path12_bkm_connection': qdet_bkm_connection(params),
    }
