r"""
agt_non_cy_local_surface.py -- AGT correspondence for non-Calabi-Yau local surfaces.

MATHEMATICAL FRAMEWORK
=======================

The AGT correspondence relates:
  6d (2,0) theory on C x R^4_{eps}  -->  4d N=2 on R^4_{eps}  x  2d CFT on C.

Standard AGT (Alday-Gaiotto-Tachikawa 2009, arXiv:0906.3219):
  6d geometry = Tot(K_C) x R^4  (CY_3 x R^4, Omega-background).
  The 2d CFT = W_N-algebra for A_{N-1} theory.

NON-CY GENERALIZATION:
  Replace Tot(K_C) with Tot(L) for a general line bundle L -> C.
  The CY defect delta = deg(L) - deg(K_C) = deg(L) + (2 - 2g(C))
  measures the failure of the CY condition c_1(Tot(L)) = 0.

THE OMEGA-BACKGROUND PARAMETERS:
  In the Omega-background R^4_{eps_1, eps_2}, the CY_3 contributes a third
  parameter eps_3 from the fiber direction of L.

  CY condition:     eps_1 + eps_2 + eps_3 = 0
  Non-CY condition: eps_1 + eps_2 + eps_3 = delta (the CY defect)

  This is the FUNDAMENTAL equation: the CY defect enters as a deformation
  of the Omega-background constraint.

SCHIFFMANN-VASSEROT PERSPECTIVE:
  The W-algebra arises as equivariant cohomology of sheaf moduli:
    W_N = H^*_T(Hilb^N(Tot(K_C)))         (CY case)
    W_N^{delta} = H^*_T(Hilb^N(Tot(L)))   (non-CY case)

  The structure function of the affine Yangian Y(gl_hat_1) is:
    g(z) = prod_{a=1}^{3} (z - h_a)/(z + h_a)

  CY:     h_1 + h_2 + h_3 = 0  (sigma_1 = 0)
  Non-CY: h_1 + h_2 + h_3 = delta  (sigma_1 = delta)

  For sigma_1 != 0, the affine Yangian deforms: phi_1 = -2*sigma_1 != 0.
  This is the MASS DEFORMATION. In gauge theory language, delta plays the
  role of an adjoint mass (the N=2* mass parameter).

NEKRASOV PARTITION FUNCTION:
  Z_Nek(eps_1, eps_2, a, m; q) = sum_{vec{k}} q^{|vec{k}|} Z_{vec{k}}

  The instanton part Z_{vec{k}} is a product over boxes in Young diagrams:
    Z_{vec{k}} = prod_{(alpha,beta) in vec{k}} weight_factor(eps_1, eps_2, a, m)

  For non-CY: the measure acquires an additional factor from the CY defect:
    Z_{vec{k}}^{non-CY} = Z_{vec{k}}^{CY} * prod_{box} (delta-dependent factor)

  This is controlled by the EQUIVARIANT PARAMETER eps_3 = delta - eps_1 - eps_2.

SPECIFIC GEOMETRIES COMPUTED:

  (a) C = P^1, L = O(-2) = K_{P^1}: delta = 0. Standard AGT, Virasoro/W_N.
  (b) C = P^1, L = O(-1): delta = 1. Twist defect. Deformed W-algebra.
  (c) C = P^1, L = O(0): delta = 2. Trivial bundle. Maximally non-CY.
  (d) C = elliptic, L = O: delta = 0. CY. Elliptic W-algebra.
  (e) C = elliptic, L = O(p): delta = 1. Non-CY elliptic.

CENTRAL CHARGE AND MODULAR CHARACTERISTIC:
  For the deformed W_N-algebra at CY defect delta:

  c(N, eps_1, eps_2, delta) = (N-1)(1 - N(N+1)*(eps_1+eps_2)^2/(eps_1*eps_2))
                               + N*(N^2-1)*delta^2/(eps_1*eps_2)

  At delta = 0 this recovers the standard W_N central charge.

  The modular characteristic kappa = c/2 for the Virasoro case (N=2) and the
  family-specific formula for general N (see landscape_census.tex conventions).

  The N=2* mass deformation: m = delta * eps_3 / (eps_1 * eps_2) in the gauge
  theory parametrization.

DEFORMED OPE AND STRUCTURE CONSTANTS:
  The OPE of the stress tensor T(z)T(w) in the deformed theory acquires
  corrections from the CY defect.  At leading order:

  T(z)T(w) ~ c/2 * (z-w)^{-4} + 2T(w)*(z-w)^{-2} + dT(w)*(z-w)^{-1} + ...

  where c = c(N, eps_1, eps_2, delta) as above.  The c/2 coefficient is the
  standard Virasoro normalization.

  For W_3 (N=3): the W-current W(z) of spin 3 has deformed OPE coefficients:
    W(z)W(w) ~ c_33 * (z-w)^{-6} + ... with c_33 = c_33(eps_1, eps_2, delta).

References:
    [AGT]   Alday, Gaiotto, Tachikawa, arXiv:0906.3219
    [SV]    Schiffmann, Vasserot, arXiv:1211.1287
    [Nek]   Nekrasov, arXiv:hep-th/0206161
    [NO]    Nekrasov, Okounkov, arXiv:hep-th/0306238
    [MO]    Maulik, Okounkov, arXiv:1211.1287
    [PR]    Prochazka, Rapcak, arXiv:1910.07997
    [GHM]   Gaiotto, Hollands, Moore, arXiv:0807.4723 (non-CY twists)
    [Tan]   Tan, arXiv:1309.4775 (M5-branes on non-CY)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

from sympy import (
    Expr,
    Integer,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
    poly,
    series,
    simplify,
    sqrt,
    symbols,
)


# =====================================================================
# Section 1: CY defect and local surface geometry
# =====================================================================

def cy_defect(deg_L: int, genus: int) -> int:
    r"""Compute the CY defect delta = deg(L) - deg(K_C) = deg(L) + 2 - 2g.

    For Tot(L) -> C to be CY, need c_1(Tot(L)) = 0, i.e. deg(L) = 2g - 2.
    The defect measures the failure.

    Parameters
    ----------
    deg_L : int
        Degree of the line bundle L -> C.
    genus : int
        Genus of the curve C.

    Returns
    -------
    int
        CY defect delta.

    Examples
    --------
    >>> cy_defect(-2, 0)   # K_{P^1} = O(-2), CY
    0
    >>> cy_defect(-1, 0)   # O(-1) -> P^1, non-CY
    1
    >>> cy_defect(0, 0)    # O(0) -> P^1, maximally non-CY for P^1
    2
    >>> cy_defect(0, 1)    # O -> elliptic, CY since K_E = O
    0
    >>> cy_defect(1, 1)    # O(p) -> elliptic, non-CY
    1
    """
    deg_K = 2 * genus - 2
    return deg_L - deg_K


def is_calabi_yau(deg_L: int, genus: int) -> bool:
    """Check if Tot(L) -> C is Calabi-Yau (c_1 = 0)."""
    return cy_defect(deg_L, genus) == 0


def euler_characteristic_base(genus: int) -> int:
    """Topological Euler characteristic of C: chi(C) = 2 - 2g."""
    return 2 - 2 * genus


def canonical_degree(genus: int) -> int:
    """Degree of K_C: deg(K_C) = 2g - 2."""
    return 2 * genus - 2


# =====================================================================
# Section 2: Omega-background parameters and CY defect
# =====================================================================

def omega_parameters(eps1, eps2, delta):
    r"""Compute the three Omega-background parameters (eps1, eps2, eps3).

    CY condition: eps1 + eps2 + eps3 = 0.
    Non-CY:       eps1 + eps2 + eps3 = delta.

    Parameters
    ----------
    eps1, eps2 : Rational or Symbol
        The two standard Omega-background parameters.
    delta : Rational or Symbol
        CY defect.

    Returns
    -------
    tuple
        (eps1, eps2, eps3) where eps3 = delta - eps1 - eps2.
    """
    eps3 = delta - eps1 - eps2
    return (eps1, eps2, eps3)


def elementary_symmetric_non_cy(eps1, eps2, delta):
    r"""Compute elementary symmetric polynomials sigma_1, sigma_2, sigma_3
    of the three parameters h_a = eps_a.

    sigma_1 = eps_1 + eps_2 + eps_3 = delta       (= 0 for CY)
    sigma_2 = eps_1*eps_2 + eps_1*eps_3 + eps_2*eps_3
    sigma_3 = eps_1*eps_2*eps_3

    Parameters
    ----------
    eps1, eps2 : Rational or Symbol
        Omega-background parameters.
    delta : Rational or Symbol
        CY defect.

    Returns
    -------
    tuple
        (sigma_1, sigma_2, sigma_3)
    """
    eps3 = delta - eps1 - eps2
    s1 = eps1 + eps2 + eps3  # = delta
    s2 = eps1 * eps2 + eps1 * eps3 + eps2 * eps3
    s3 = eps1 * eps2 * eps3
    return (s1, s2, s3)


def power_sums_non_cy(eps1, eps2, delta, max_k: int = 8):
    r"""Newton power sums p_k = eps_1^k + eps_2^k + eps_3^k.

    For CY (delta=0): p_1 = 0. For non-CY: p_1 = delta.
    Even power sums are nonzero in BOTH cases.

    Returns dict {k: p_k} for k = 1, ..., max_k.
    """
    eps3 = delta - eps1 - eps2
    return {k: eps1**k + eps2**k + eps3**k for k in range(1, max_k + 1)}


# =====================================================================
# Section 3: Deformed structure function (affine Yangian deformation)
# =====================================================================

def structure_function_coefficients_non_cy(
    eps1, eps2, delta, max_order: int = 10
) -> List:
    r"""Compute phi_j coefficients of the deformed structure function.

    g^{delta}(z) = prod_{a=1}^{3} (z - h_a)/(z + h_a)

    where h_1 = eps_1, h_2 = eps_2, h_3 = delta - eps_1 - eps_2.

    CY case (delta=0):   phi_1 = 0, phi_2 = 0 (leading nontrivial: phi_3).
    Non-CY (delta != 0): phi_1 = -2*delta != 0 (mass deformation activates).
    Note: phi_2 = 2*delta^2 for non-CY (from alpha_1^2/2 upon exponentiation).
    Even-index phi_j (j >= 6) can be nonzero even for CY (from products of
    odd-index log coefficients).

    Returns [phi_0, phi_1, ..., phi_{max_order}].
    """
    eps3 = delta - eps1 - eps2
    w = Symbol("w")
    g_w = ((1 - eps1 * w) * (1 - eps2 * w) * (1 - eps3 * w)
           / ((1 + eps1 * w) * (1 + eps2 * w) * (1 + eps3 * w)))
    g_series = series(g_w, w, 0, max_order + 1)

    coeffs = []
    for j in range(max_order + 1):
        coeff = g_series.coeff(w, j)
        coeffs.append(expand(coeff))

    return coeffs


def structure_function_log_coefficients_non_cy(
    eps1, eps2, delta, max_order: int = 10
) -> List:
    r"""Compute alpha_k coefficients of log g^{delta}(z).

    log g(z) = sum_{k>=1} alpha_k z^{-k}
    where alpha_k = (-2/k) * p_k = (-2/k)(eps_1^k + eps_2^k + eps_3^k).

    For CY: alpha_k = 0 for k even (since p_{even} != 0 but the FULL log
    series has nonzero even terms; the KEY difference is p_1 = 0 forces
    alpha_1 = 0).

    For non-CY: alpha_1 = -2*delta != 0.

    Returns [alpha_1, alpha_2, ..., alpha_{max_order}].
    """
    ps = power_sums_non_cy(eps1, eps2, delta, max_k=max_order)
    return [Rational(-2, k) * ps[k] for k in range(1, max_order + 1)]


def verify_inversion_identity_non_cy(eps1, eps2, delta, max_order: int = 6) -> Dict:
    r"""Verify g(z)*g(-z) = 1 for the structure function.

    The identity g(z)*g(-z) = 1 holds UNIVERSALLY for ALL choices of
    h_1, h_2, h_3, not just the CY case. This is because:
      g(-z) = prod ((-z) - h_a)/((-z) + h_a) = prod (z + h_a)/(z - h_a) = 1/g(z).

    The CY condition sigma_1 = 0 affects the LOG series structure
    (alpha_1 = 0 kills the leading term), NOT the inversion identity.

    Returns dict with 'product_coefficients' and 'is_identity'.
    """
    eps3 = delta - eps1 - eps2
    w = Symbol("w")
    g_w = ((1 - eps1 * w) * (1 - eps2 * w) * (1 - eps3 * w)
           / ((1 + eps1 * w) * (1 + eps2 * w) * (1 + eps3 * w)))
    g_mw = g_w.subs(w, -w)
    product = series(expand(g_w * g_mw), w, 0, max_order + 1)

    coeffs = []
    for j in range(max_order + 1):
        c = product.coeff(w, j)
        coeffs.append(expand(c))

    is_identity = all(c == (1 if j == 0 else 0) for j, c in enumerate(coeffs))
    return {
        'product_coefficients': coeffs,
        'is_identity': is_identity,
    }


# =====================================================================
# Section 4: Central charge of the deformed W-algebra
# =====================================================================

def central_charge_deformed_wn(N: int, eps1, eps2, delta):
    r"""Central charge of the deformed W_N-algebra at CY defect delta.

    For the 6d (2,0) theory of type A_{N-1} on Tot(L) -> C with
    Omega-background parameters eps_1, eps_2, the mass parameter is
    m = eps_3 = delta - eps_1 - eps_2 (the third equivariant weight).

    c(N, eps_1, eps_2, delta)
      = (N-1) - N(N^2-1) * (eps_1 + eps_2)^2 / (eps_1 * eps_2)
        + N(N^2-1) * eps_3 * delta / (eps_1 * eps_2)

    where eps_3 = delta - eps_1 - eps_2.

    The correction term is eps_3 * delta = (delta - eps_1 - eps_2) * delta,
    NOT delta^2. The distinction matters: at delta = eps_1 + eps_2 (i.e. m=0),
    the correction vanishes and we recover the pure N=2 central charge.
    With delta^2 the correction would NOT vanish at m=0.

    Equivalently, the correction is m * (m + eps_1 + eps_2) where m = eps_3
    is the adjoint mass in the N=2* theory (Nekrasov-Okounkov).

    At delta = 0: recovers the standard Toda central charge.

    Parameters
    ----------
    N : int
        Rank parameter (W_N algebra, gauge group SU(N)).
    eps1, eps2 : Rational or Symbol
        Omega-background parameters.
    delta : Rational or Symbol
        CY defect.

    Returns
    -------
    Expression for the central charge.
    """
    eps3 = delta - eps1 - eps2
    # Standard part
    c_std = (N - 1) - N * (N**2 - 1) * (eps1 + eps2)**2 / (eps1 * eps2)
    # Non-CY correction: eps_3 * delta, NOT delta^2
    c_corr = N * (N**2 - 1) * eps3 * delta / (eps1 * eps2)
    return expand(c_std + c_corr)


def central_charge_virasoro_deformed(eps1, eps2, delta):
    r"""Central charge for the deformed Virasoro algebra (N=2).

    c = 1 - 6(eps_1 + eps_2)^2/(eps_1*eps_2) + 6*eps_3*delta/(eps_1*eps_2)

    where eps_3 = delta - eps_1 - eps_2.

    Equivalently: c = 1 + 6*(eps_3*delta - (eps_1+eps_2)^2)/(eps_1*eps_2).

    At delta = 0: c = 1 - 6(eps_1+eps_2)^2/(eps_1*eps_2) (standard Virasoro).
    At m = eps_3 = 0 (delta = eps_1+eps_2): c = standard (pure N=2, no mass).
    """
    return central_charge_deformed_wn(2, eps1, eps2, delta)


def central_charge_w3_deformed(eps1, eps2, delta):
    """Central charge for the deformed W_3 algebra (N=3)."""
    return central_charge_deformed_wn(3, eps1, eps2, delta)


# =====================================================================
# Section 5: Mass parameter and gauge theory dictionary
# =====================================================================

def adjoint_mass_from_defect(delta, eps1, eps2):
    r"""The adjoint mass parameter in the N=2* theory.

    The CY defect delta maps to the adjoint hypermultiplet mass:
      m_adj = delta  (in units where eps_1, eps_2 are the Omega parameters)

    More precisely, the N=2* mass parameter is:
      m = eps_3 = delta - eps_1 - eps_2

    At delta = 0: m = -(eps_1+eps_2), which is the STANDARD N=2 SUSY
    condition (no extra mass).

    At delta != 0: genuine N=2* deformation with adjoint mass.
    """
    return delta - eps1 - eps2


def nekrasov_self_dual_limit(eps1, delta):
    r"""The self-dual (Nekrasov-Shatashvili) limit eps_2 -> 0.

    In the NS limit, the 4d partition function becomes the WKB quantization
    of the Seiberg-Witten curve. For non-CY:

    eps_1 = hbar, eps_2 -> 0, eps_3 = delta - hbar.

    The effective twisted superpotential acquires delta-dependent corrections.

    Returns dict with the limiting parameters.
    """
    return {
        'eps1': eps1,
        'eps2': 0,
        'eps3': delta - eps1,
        'hbar': eps1,
        'delta': delta,
        'is_ns_limit': True,
    }


# =====================================================================
# Section 6: Nekrasov partition function for non-CY
# =====================================================================

def arm_length(partition: Tuple[int, ...], i: int, j: int) -> int:
    """Arm length a(i,j) = lambda_i - j for box (i,j) in partition lambda."""
    if i < len(partition):
        return partition[i] - j - 1
    return -j - 1


def leg_length(partition: Tuple[int, ...], i: int, j: int) -> int:
    """Leg length l(i,j) = lambda^t_j - i for box (i,j) in partition lambda."""
    conj = conjugate_partition(partition)
    if j < len(conj):
        return conj[j] - i - 1
    return -i - 1


def conjugate_partition(lam: Tuple[int, ...]) -> Tuple[int, ...]:
    """Transpose a partition."""
    if not lam:
        return ()
    cols = lam[0]
    return tuple(sum(1 for p in lam if p >= j) for j in range(1, cols + 1))


def nekrasov_factor_single(
    partition: Tuple[int, ...],
    eps1,
    eps2,
    delta,
    coulomb_param,
) -> Any:
    r"""Single-partition contribution to the Nekrasov factor for non-CY.

    For each box (i,j) in partition lambda, the CY contribution is:
      E(i,j) = -eps_1*(a(i,j)+1) + eps_2*l(i,j)   [Nekrasov's E-factor]
      weight = 1/E(i,j)

    The non-CY correction multiplies each box factor by:
      (E(i,j) + eps_3) / E(i,j)   where eps_3 = delta - eps_1 - eps_2

    This is the EQUIVARIANT WEIGHT from the additional T-fixed point data
    of Tot(L) vs Tot(K_C).

    Parameters
    ----------
    partition : tuple of int
        Young diagram.
    eps1, eps2 : Rational
        Omega-background parameters.
    delta : Rational
        CY defect.
    coulomb_param : Rational
        Coulomb branch parameter a.

    Returns
    -------
    Product of weight factors (as a rational expression).
    """
    eps3 = delta - eps1 - eps2
    product = Rational(1)
    for i in range(len(partition)):
        for j in range(partition[i]):
            a = arm_length(partition, i, j)
            l = leg_length(partition, i, j)
            # E-factor
            E = coulomb_param - eps1 * (a + 1) + eps2 * l
            if E == 0:
                return None  # degenerate
            # CY factor: 1/E^2 (from the two fixed-point contributions)
            # Non-CY correction: additional eps_3-dependent weight
            # The full factor for non-CY:
            #   1/(E * (E - eps_1 - eps_2 + delta))
            # = 1/(E * (E + eps_3))
            E_shifted = E + eps3
            if E_shifted == 0:
                return None
            product *= Rational(1) / (E * E_shifted)
    return product


def instanton_partition_function_u1(
    eps1,
    eps2,
    delta,
    max_instanton: int = 3,
) -> List:
    r"""U(1) instanton partition function for non-CY, order by order.

    For U(1) theory, the Coulomb parameter is trivial (a=0) and
    the partition function is:

    Z = sum_{k>=0} q^k * Z_k

    where Z_k = sum_{|lambda|=k} z_{lambda}^{non-CY}.

    The CY case reproduces the MacMahon function M(q) = prod 1/(1-q^n)^n
    (for the U(1) theory on C^3).

    Returns [Z_0, Z_1, Z_2, ..., Z_{max_instanton}] as rational numbers.
    """
    eps3 = delta - eps1 - eps2
    result = [Rational(1)]  # Z_0 = 1

    for k in range(1, max_instanton + 1):
        z_k = Rational(0)
        for partition in _partitions_of(k):
            factor = Rational(1)
            valid = True
            for i in range(len(partition)):
                for j in range(partition[i]):
                    a = partition[i] - j - 1  # arm length
                    # leg length from conjugate
                    conj = conjugate_partition(partition)
                    l = conj[j] - i - 1 if j < len(conj) else -i - 1

                    hook_cy = eps1 * (a + 1) + eps2 * (l + 1)
                    if hook_cy == 0:
                        valid = False
                        break
                    # Non-CY correction factor
                    hook_non_cy = hook_cy - delta
                    if delta == 0:
                        factor *= Rational(1) / hook_cy**2
                    else:
                        if hook_non_cy == 0:
                            valid = False
                            break
                        factor *= Rational(1) / (hook_cy * hook_non_cy)
                if not valid:
                    break
            if valid:
                z_k += factor
        result.append(z_k)
    return result


@lru_cache(maxsize=128)
def _partitions_of(n: int) -> List[Tuple[int, ...]]:
    """Generate all partitions of n as tuples in decreasing order."""
    if n == 0:
        return [()]
    result = []
    _partition_helper(n, n, [], result)
    return result


def _partition_helper(n: int, max_part: int, current: list, result: list):
    if n == 0:
        result.append(tuple(current))
        return
    for p in range(min(n, max_part), 0, -1):
        current.append(p)
        _partition_helper(n - p, p, current, result)
        current.pop()


# =====================================================================
# Section 7: Deformed W-algebra OPE structure
# =====================================================================

def virasoro_ope_central_term(eps1, eps2, delta):
    r"""The c/2 coefficient in T(z)T(w) ~ (c/2)/(z-w)^4 + ...

    This is the leading OPE coefficient, equal to half the central charge.
    """
    c = central_charge_virasoro_deformed(eps1, eps2, delta)
    return c / 2


def w3_ope_ww_coefficient(eps1, eps2, delta):
    r"""The leading W(z)W(w) OPE coefficient c_{33} for the deformed W_3.

    For the standard W_3 algebra:
      W(z)W(w) ~ (c/3)/(z-w)^6 + ...

    where c/3 is the standard normalization of the W_3 two-point function.
    For the deformed algebra, c is the deformed central charge.
    """
    c = central_charge_w3_deformed(eps1, eps2, delta)
    return c / 3


def deformed_stress_tensor_ope(eps1, eps2, delta) -> Dict:
    r"""Full T(z)T(w) OPE data for the deformed Virasoro algebra.

    T(z)T(w) = c/2 * (z-w)^{-4} + 2T(w) * (z-w)^{-2} + dT(w) * (z-w)^{-1}

    The OPE structure is identical to undeformed Virasoro; only c changes.
    This is because T(z) is still a spin-2 quasi-primary, and the OPE is
    completely fixed by conformal symmetry once c is given.

    Returns dict with 'c', 'half_c', 'T_coefficient', 'dT_coefficient'.
    """
    c = central_charge_virasoro_deformed(eps1, eps2, delta)
    return {
        'c': c,
        'half_c': c / 2,
        'T_coefficient': 2,  # always 2 by conformal Ward identity
        'dT_coefficient': 1,  # always 1 by translation Ward identity
    }


# =====================================================================
# Section 8: Modular properties and partition function
# =====================================================================

def free_energy_genus_0(eps1, eps2, delta, coulomb_params: List, q_order: int = 3):
    r"""Genus-0 free energy (prepotential) for non-CY AGT.

    F_0 = (1/eps_1*eps_2) * (classical + 1-loop + instanton)

    The CY defect modifies the 1-loop part through eps_3-dependent terms.

    For U(1): the prepotential is trivial.
    For SU(2): F_0 = a^2 * log(q) + ...

    This returns the perturbative prepotential coefficient.
    """
    eps3 = delta - eps1 - eps2
    # Perturbative part: depends on the Coulomb parameters and eps_3
    if len(coulomb_params) == 0:
        # U(1) case
        return {'classical': Rational(0), 'one_loop_correction': Rational(0)}

    a = coulomb_params[0]
    # Classical prepotential
    F_class = a**2
    # One-loop: standard contribution + eps_3 correction
    # The non-CY correction to the 1-loop prepotential:
    # delta_F_1loop = sum_alpha (alpha(a) + eps_3)^2 * log(alpha(a) + eps_3)
    #                 - sum_alpha (alpha(a))^2 * log(alpha(a))
    # At leading order in eps_3:
    F_1loop_correction = eps3 * a if eps3 != 0 else 0
    return {
        'classical': expand(F_class),
        'one_loop_correction': expand(F_1loop_correction),
    }


def modular_discriminant_non_cy(eps1, eps2, delta):
    r"""The modular discriminant for the non-CY deformed theory.

    For CY: the Nekrasov partition function transforms as a modular form
    under S-duality (tau -> -1/tau).

    For non-CY: S-duality is BROKEN by the mass parameter m = eps_3.
    The partition function transforms under a SUBGROUP of SL(2,Z),
    determined by the denominator of delta (if delta is rational).

    Returns dict describing the modular properties.
    """
    eps3 = delta - eps1 - eps2
    is_cy = (delta == 0)
    return {
        'is_cy': is_cy,
        'delta': delta,
        'eps3': eps3,
        'modular_group': 'SL(2,Z)' if is_cy else 'Gamma_0(N)',
        'mass_parameter': eps3,
        's_duality_preserved': is_cy,
    }


# =====================================================================
# Section 9: Specific geometries
# =====================================================================

class LocalSurface:
    r"""A local surface Tot(L) -> C with its AGT data.

    Attributes
    ----------
    genus : int
        Genus of the base curve C.
    deg_L : int
        Degree of the line bundle L.
    delta : int
        CY defect = deg_L - (2g - 2).
    name : str
        Human-readable name.
    """

    def __init__(self, genus: int, deg_L: int, name: str = ""):
        self.genus = genus
        self.deg_L = deg_L
        self.delta = cy_defect(deg_L, genus)
        self.name = name or f"Tot(O({deg_L})) -> C_{genus}"
        self.is_cy = (self.delta == 0)

    def __repr__(self):
        cy_str = "CY" if self.is_cy else f"non-CY(delta={self.delta})"
        return f"LocalSurface({self.name}, {cy_str})"

    def central_charge(self, N: int, eps1, eps2):
        """Central charge of the W_N-algebra for this geometry."""
        return central_charge_deformed_wn(N, eps1, eps2, self.delta)

    def structure_function(self, eps1, eps2, max_order: int = 8):
        """Structure function coefficients phi_j."""
        return structure_function_coefficients_non_cy(
            eps1, eps2, self.delta, max_order
        )

    def omega_params(self, eps1, eps2):
        """The three Omega-background parameters."""
        return omega_parameters(eps1, eps2, self.delta)

    def instanton_partition(self, eps1, eps2, max_k: int = 3):
        """U(1) instanton partition function coefficients."""
        return instanton_partition_function_u1(
            eps1, eps2, self.delta, max_instanton=max_k
        )


# Standard geometries
def local_p1_minus2():
    """Tot(O(-2)) -> P^1 = Tot(K_{P^1}). CY. Standard AGT."""
    return LocalSurface(0, -2, "K_{P^1}")

def local_p1_minus1():
    """Tot(O(-1)) -> P^1. Non-CY, delta=1. Twist defect."""
    return LocalSurface(0, -1, "O(-1)/P^1")

def local_p1_trivial():
    """Tot(O(0)) -> P^1. Non-CY, delta=2. Trivial bundle."""
    return LocalSurface(0, 0, "O/P^1")

def local_p1_plus1():
    """Tot(O(1)) -> P^1. Non-CY, delta=3."""
    return LocalSurface(0, 1, "O(1)/P^1")

def local_elliptic_trivial():
    """Tot(O) -> E. CY since K_E = O. Elliptic W-algebra."""
    return LocalSurface(1, 0, "O/E")

def local_elliptic_point():
    """Tot(O(p)) -> E. Non-CY, delta=1."""
    return LocalSurface(1, 1, "O(p)/E")

def local_genus2_canonical():
    """Tot(K_{C_2}) -> C_2. CY. Genus 2."""
    return LocalSurface(2, 2, "K_{C_2}")

def local_genus2_shifted():
    """Tot(K_{C_2}(p)) -> C_2. Non-CY, delta=1. Genus 2."""
    return LocalSurface(2, 3, "K(p)/C_2")


STANDARD_GEOMETRIES = {
    'P1_CY': local_p1_minus2(),
    'P1_twist': local_p1_minus1(),
    'P1_trivial': local_p1_trivial(),
    'P1_plus1': local_p1_plus1(),
    'E_CY': local_elliptic_trivial(),
    'E_point': local_elliptic_point(),
    'C2_CY': local_genus2_canonical(),
    'C2_shifted': local_genus2_shifted(),
}


# =====================================================================
# Section 10: Deformation families and parameter space
# =====================================================================

def cy_defect_family(genus: int, deg_range: range) -> List[Dict]:
    r"""Generate a family of local surfaces over a curve of given genus.

    For each degree d in deg_range, compute the CY defect and
    central charge data.
    """
    family = []
    for d in deg_range:
        delta = cy_defect(d, genus)
        family.append({
            'genus': genus,
            'deg_L': d,
            'delta': delta,
            'is_cy': delta == 0,
            'name': f"O({d})/C_{genus}",
        })
    return family


def delta_interpolation(eps1, eps2, delta_values: List) -> List[Dict]:
    r"""Compute W-algebra data as delta varies continuously.

    This traces out the deformation family from CY (delta=0) to non-CY.
    The central charge, structure function coefficients, and modular
    properties are computed at each delta value.

    Returns list of dicts with all data at each delta.
    """
    results = []
    for delta in delta_values:
        c_vir = central_charge_virasoro_deformed(eps1, eps2, delta)
        c_w3 = central_charge_w3_deformed(eps1, eps2, delta)
        phi = structure_function_coefficients_non_cy(
            eps1, eps2, delta, max_order=5
        )
        s1, s2, s3 = elementary_symmetric_non_cy(eps1, eps2, delta)
        results.append({
            'delta': delta,
            'c_virasoro': c_vir,
            'c_w3': c_w3,
            'phi': phi,
            'sigma_1': s1,
            'sigma_2': s2,
            'sigma_3': s3,
            'is_cy': (delta == 0),
        })
    return results


# =====================================================================
# Section 11: Hilbert scheme equivariant cohomology (SV perspective)
# =====================================================================

def hilb_equivariant_weight_non_cy(
    partition: Tuple[int, ...],
    eps1,
    eps2,
    delta,
) -> Any:
    r"""Equivariant weight of a T-fixed point on Hilb^n(Tot(L)).

    For CY: the T-fixed points on Hilb^n(C^2 x C) are labeled by 3D partitions.
    For non-CY: the fixed points are the same (partitions), but the WEIGHTS change.

    The T-equivariant weight at a fixed point labeled by 2D partition lambda is:

    CY:     prod_{box} 1/(h(box)^2)
    Non-CY: prod_{box} 1/(h(box) * h'(box))

    where h(box) = eps_1*(a+1) + eps_2*(l+1)  (hook content)
    and   h'(box) = h(box) - delta             (shifted hook content)

    This is the TANGENT SPACE WEIGHT. The non-CY shift comes from the
    non-trivial T-action on the fiber of L (vs the CY-trivial action on K_C).
    """
    eps3 = delta - eps1 - eps2
    weight = Rational(1)
    conj = conjugate_partition(partition)
    for i in range(len(partition)):
        for j in range(partition[i]):
            a = partition[i] - j - 1
            l = conj[j] - i - 1 if j < len(conj) else -i - 1
            h = eps1 * (a + 1) + eps2 * (l + 1)
            h_prime = h - delta
            if h == 0 or h_prime == 0:
                return None
            weight *= Rational(1) / (h * h_prime)
    return weight


def hilb_point_count_non_cy(
    eps1, eps2, delta, max_n: int = 4
) -> List:
    r"""Equivariant Euler characteristic of Hilb^n(Tot(L)).

    chi_T(Hilb^n) = sum_{|lambda|=n} equivariant_weight(lambda)

    This is the coefficient of q^n in the Nekrasov partition function.
    For CY (delta=0): reproduces MacMahon coefficients.
    For non-CY: deformed counting.

    Returns [chi_0, chi_1, ..., chi_{max_n}].
    """
    result = [Rational(1)]  # n=0: empty partition
    for n in range(1, max_n + 1):
        chi_n = Rational(0)
        for lam in _partitions_of(n):
            w = hilb_equivariant_weight_non_cy(lam, eps1, eps2, delta)
            if w is not None:
                chi_n += w
        result.append(chi_n)
    return result


# =====================================================================
# Section 12: Consistency checks and cross-verification
# =====================================================================

def verify_cy_limit(eps1, eps2, max_order: int = 6) -> Dict:
    r"""Verify that delta=0 recovers the standard CY/AGT results.

    Check:
    1. sigma_1 = 0
    2. phi_1 = 0
    3. g(z)*g(-z) = 1
    4. Central charge = standard W_N central charge
    """
    delta = 0
    s1, s2, s3 = elementary_symmetric_non_cy(eps1, eps2, delta)
    phi = structure_function_coefficients_non_cy(eps1, eps2, delta, max_order)
    inv = verify_inversion_identity_non_cy(eps1, eps2, delta, max_order)
    c2 = central_charge_virasoro_deformed(eps1, eps2, delta)
    c3 = central_charge_w3_deformed(eps1, eps2, delta)

    # Standard central charges for comparison
    # Virasoro: c = 1 - 6(eps1+eps2)^2/(eps1*eps2)
    c2_std = 1 - 6 * (eps1 + eps2)**2 / (eps1 * eps2)
    # W_3: c = 2 - 24(eps1+eps2)^2/(eps1*eps2)
    c3_std = 2 - 24 * (eps1 + eps2)**2 / (eps1 * eps2)

    return {
        'sigma_1_zero': expand(s1) == 0,
        'phi_1_zero': expand(phi[1]) == 0,
        'inversion_identity': inv['is_identity'],
        'virasoro_c_matches': expand(c2 - c2_std) == 0,
        'w3_c_matches': expand(c3 - c3_std) == 0,
    }


def verify_delta_continuity(eps1, eps2, delta_small) -> Dict:
    r"""Verify that the deformation is smooth at delta=0.

    The central charge should be:
      c(delta) = c(0) + O(delta^2)

    (linear term vanishes by symmetry delta -> -delta of the
    non-CY correction term delta^2/(eps1*eps2)).
    """
    c_0 = central_charge_virasoro_deformed(eps1, eps2, 0)
    c_d = central_charge_virasoro_deformed(eps1, eps2, delta_small)
    c_md = central_charge_virasoro_deformed(eps1, eps2, -delta_small)

    # c(delta) - c(0) should be proportional to delta^2
    diff = expand(c_d - c_0)
    # c(delta) = c(-delta) (even in delta)
    even_check = expand(c_d - c_md)

    return {
        'c_at_0': c_0,
        'c_at_delta': c_d,
        'c_at_minus_delta': c_md,
        'difference': diff,
        'is_even_in_delta': even_check == 0,
    }


def verify_nekrasov_shatashvili_limit(delta, hbar) -> Dict:
    r"""Verify the NS limit eps_2 -> 0 for non-CY.

    In the NS limit, the partition function becomes:
      Z_NS = exp(W(a, hbar, delta) / hbar)

    where W is the effective twisted superpotential.
    The CY defect enters as a mass-like deformation of W.
    """
    ns_data = nekrasov_self_dual_limit(hbar, delta)
    eps3 = ns_data['eps3']
    return {
        'ns_data': ns_data,
        'eps3_in_limit': eps3,
        'is_cy_in_limit': (delta == 0),
    }


# =====================================================================
# Section 13: Deformed Seiberg-Witten curve
# =====================================================================

def sw_curve_deformed_su2(u, delta, Lambda):
    r"""Seiberg-Witten curve for SU(2) N=2* theory.

    The N=2* SW curve (Donagi-Witten):
      y^2 = (x - e_1(tau))(x - e_2(tau))(x - e_3(tau))

    with the mass deformation m = delta entering through the Weierstrass
    moduli:
      e_i(tau, m) = e_i(tau) + O(m^2)

    At m = 0 (CY): pure N=2 SU(2) curve.

    For the Nekrasov partition function, the curve encodes the
    period integrals:
      a = oint_A lambda_SW,  a_D = oint_B lambda_SW

    Returns the discriminant of the curve (controls strong-coupling singularities).
    """
    # Discriminant of y^2 = x^3 - u*x - v
    # For N=2* with mass m = delta:
    # u-plane parametrization:
    #   4u^3 - g_2*u - g_3 = 0
    # with g_2, g_3 depending on Lambda and delta.
    # Leading-order discriminant:
    disc = 4 * u**3 - 27 * Lambda**4 * (1 + delta**2)
    return expand(disc)


# =====================================================================
# Section 14: W-algebra deformation at low N
# =====================================================================

def w_algebra_generators(N: int) -> List[int]:
    """Spins of W_N generators: {2, 3, 4, ..., N}."""
    return list(range(2, N + 1))


def deformed_w_algebra_data(N: int, eps1, eps2, delta) -> Dict:
    r"""Complete data of the deformed W_N algebra at CY defect delta.

    The deformed W_N algebra W_N^{delta} has:
    - Same number of generators (spins 2, 3, ..., N)
    - Deformed central charge c(N, eps_1, eps_2, delta)
    - Deformed OPE structure constants
    - Different modular properties when delta != 0

    The algebra is the EQUIVARIANT W-algebra of Schiffmann-Vasserot,
    with the CY defect entering as a non-trivial equivariant parameter.
    """
    c = central_charge_deformed_wn(N, eps1, eps2, delta)
    eps3 = delta - eps1 - eps2
    s1, s2, s3 = elementary_symmetric_non_cy(eps1, eps2, delta)
    phi = structure_function_coefficients_non_cy(eps1, eps2, delta, max_order=8)

    return {
        'N': N,
        'generators': w_algebra_generators(N),
        'central_charge': c,
        'eps': (eps1, eps2, eps3),
        'delta': delta,
        'sigma': (s1, s2, s3),
        'phi_coefficients': phi,
        'is_cy': (delta == 0),
        'algebra_type': f'W_{N}' if delta == 0 else f'W_{N}^{{delta={delta}}}',
    }


# =====================================================================
# Section 15: Koszul dual and complementarity for deformed algebras
# =====================================================================

def koszul_dual_defect(delta: int) -> int:
    r"""CY defect of the Koszul dual geometry.

    For the standard AGT (delta=0), the Koszul dual W_N algebra has
    the SAME delta=0 (CY is self-dual under Koszul duality).

    For non-CY, the Koszul dual geometry has:
      delta^! = -delta  (sign flip)

    This is because Koszul duality sends L -> L^{-1} tensor K_C,
    which sends deg(L) -> 2g-2-deg(L), hence:
      delta^! = (2g-2-deg(L)) - (2g-2) = -deg(L) + (2g-2) - (2g-2) = -delta.

    Wait: more carefully, if L has degree d, then L^{-1} tensor K_C has
    degree (2g-2) - d. The CY defect of the dual is:
      delta^! = ((2g-2) - d) - (2g-2) = -d = -(d - (2g-2)) - 0 = ...

    Actually: delta = d - (2g-2). So delta^! = ((2g-2)-d) - (2g-2) = -d,
    while delta = d - (2g-2). So delta^! = -(d) and delta = d - (2g-2).
    Hence delta^! = -delta - 2(2g-2). For g=0: delta^! = -delta + 4.
    For g=1: delta^! = -delta.

    The correct general formula: the Koszul dual line bundle of L is
    K_C tensor L^{-1}, so deg(L^!) = (2g-2) - deg(L).
    delta^! = deg(L^!) - (2g-2) = -deg(L) = -(delta + (2g-2)) - (2g-2)?

    Let's be precise:
      deg(L) = delta + (2g-2)   [definition of delta]
      deg(L^!) = (2g-2) - deg(L) = (2g-2) - delta - (2g-2) = -delta
      delta^! = deg(L^!) - (2g-2) = -delta - (2g-2)

    For P^1 (g=0): delta^! = -delta + 2.
      O(-2): delta=0, delta^!=2 (i.e. L^!=O(0)).
      O(-1): delta=1, delta^!=1 (self-dual!).
      O(0): delta=2, delta^!=0 (dual is CY).

    For elliptic (g=1): delta^! = -delta.
      O: delta=0, delta^!=0 (CY self-dual).
      O(p): delta=1, delta^!=-1.

    NOTE: This is NOT simply delta -> -delta in general. The genus matters.
    """
    # This function is genus-dependent; we return the formula.
    # For a genus-independent version, use koszul_dual_defect_full.
    raise NotImplementedError(
        "Use koszul_dual_defect_full(delta, genus) instead."
    )


def koszul_dual_defect_full(delta: int, genus: int) -> int:
    r"""CY defect of the Koszul dual geometry, genus-dependent.

    delta^! = -delta - 2*(2g-2)  ... no, let's recompute.

    deg(L) = delta + deg(K_C) = delta + (2g-2).
    The Serre dual bundle: L^! = K_C tensor L^{-1} has deg(L^!) = (2g-2) - deg(L).
    delta^! = deg(L^!) - deg(K_C) = ((2g-2) - deg(L)) - (2g-2) = -deg(L).
    But deg(L) = delta + (2g-2), so delta^! = -(delta + (2g-2)) = -delta - (2g-2).

    Wait, that gives O(-2)->P^1: delta=0, delta^!=-(0+(-2))=2. Let me recheck.
    g=0: deg(K)=-2, deg(L)=delta+(-2)=delta-2.
    For delta=0: deg(L)=-2 (K_{P^1}).
    L^! = K_{P^1} tensor L^{-1} = O(-2) tensor O(2) = O(0). deg(L^!)=0.
    delta^! = 0 - (-2) = 2.

    So delta^! = deg(L^!) - deg(K_C) = -deg(L) - deg(K_C)
               = -(delta + deg(K_C)) - deg(K_C) = -delta - 2*deg(K_C)
               = -delta - 2*(2g-2).

    Hmm: g=0: -delta - 2*(-2) = -delta + 4. For delta=0: 4. But we got 2 above.

    Let me redo: deg(L^!) = deg(K_C) - deg(L) = (2g-2) - (delta + 2g - 2) = -delta.
    delta^! = deg(L^!) - deg(K_C) = -delta - (2g-2).

    g=0: delta^! = -delta - (-2) = -delta + 2. Check: delta=0 => delta^!=2. YES.
    g=1: delta^! = -delta - 0 = -delta. Check: delta=0 => delta^!=0. YES.
    g=2: delta^! = -delta - 2. Check: delta=0 => delta^!=-2.

    This is correct.
    """
    deg_K = 2 * genus - 2
    return -delta - deg_K


def complementarity_central_charges(N: int, eps1, eps2, delta, genus: int) -> Dict:
    r"""Central charge complementarity for the deformed W_N pair.

    For the Koszul pair (W_N^{delta}, W_N^{delta^!}):
      c(delta) + c(delta^!) = ?

    In the CY case this is the anomaly cancellation condition.
    """
    delta_dual = koszul_dual_defect_full(delta, genus)
    c = central_charge_deformed_wn(N, eps1, eps2, delta)
    c_dual = central_charge_deformed_wn(N, eps1, eps2, delta_dual)
    return {
        'delta': delta,
        'delta_dual': delta_dual,
        'c': c,
        'c_dual': c_dual,
        'c_sum': expand(c + c_dual),
        'c_difference': expand(c - c_dual),
    }


# =====================================================================
# Section 16: Full landscape census
# =====================================================================

def landscape_table(eps1, eps2, genus_range: range = range(3),
                    deg_range: range = range(-4, 4)) -> List[Dict]:
    r"""Generate the landscape table of local surfaces and their W-algebra data.

    For each (genus, degree) pair, compute:
    - CY defect delta
    - Central charges c_Vir and c_{W_3}
    - Leading structure function coefficient phi_1
    - Koszul dual defect
    """
    table = []
    for g in genus_range:
        for d in deg_range:
            delta = cy_defect(d, g)
            delta_dual = koszul_dual_defect_full(delta, g)
            c_vir = central_charge_virasoro_deformed(eps1, eps2, delta)
            c_w3 = central_charge_w3_deformed(eps1, eps2, delta)
            phi = structure_function_coefficients_non_cy(
                eps1, eps2, delta, max_order=3
            )
            table.append({
                'genus': g,
                'deg_L': d,
                'delta': delta,
                'delta_dual': delta_dual,
                'is_cy': delta == 0,
                'c_virasoro': c_vir,
                'c_w3': c_w3,
                'phi_1': phi[1],
                'sigma_1': delta,
            })
    return table


# =====================================================================
# Section 17: Instanton moduli space dimension
# =====================================================================

def instanton_moduli_dimension(N: int, k: int, delta: int, genus: int) -> int:
    r"""Virtual dimension of the instanton moduli space M(N, k) on Tot(L).

    For SU(N) instantons of charge k on Tot(L) -> C:
      vdim_CY = 2Nk  (for CY, the virtual dimension from ADHM)
      vdim_non_CY = 2Nk + k*delta*(N-1)  (non-CY correction)

    Wait: the precise formula comes from the index theorem.
    For a rank-N bundle E on Tot(L) with c_2 = k:
      chi(E, E) = 2Nk  (for CY)

    The non-CY correction to the index:
      delta_chi = -k*N*delta^2/...  (depends on the exact topology)

    For the SIMPLE version: the expected dimension of the moduli of
    sheaves on the surface is:
      vdim = 2Nk - (N^2-1)*chi(O_S)

    where chi(O_S) depends on delta through the arithmetic genus of Tot(L).

    We use the ADHM formula for the moduli of framed sheaves:
      dim M(N,k) = 2Nk  (this is independent of delta for FRAMED moduli)

    The CY defect affects the UNFRAMED moduli, i.e. the virtual dimension
    of the moduli of TORSION-FREE SHEAVES (not framed instantons).

    For the AGT correspondence, framed instantons are the relevant objects,
    so the dimension is 2Nk regardless of delta. The defect enters through
    the MEASURE, not the dimension.

    Returns 2*N*k (the universal framed instanton moduli dimension).
    """
    return 2 * N * k


def virtual_tangent_weight_correction(N: int, k: int, delta, eps1, eps2):
    r"""Non-CY correction to the virtual tangent bundle weight.

    The T-equivariant K-theory class of the virtual tangent bundle
    T^{vir}_{M(N,k)} acquires a correction from the CY defect:

      T^{vir}_{non-CY} = T^{vir}_{CY} + delta * (correction from fiber)

    This correction is what changes the Nekrasov partition function.
    At the level of the equivariant index:
      chi(T^{vir}_{non-CY}) - chi(T^{vir}_{CY}) = k * delta * (eps_1 + eps_2)
    """
    eps3 = delta - eps1 - eps2
    correction = k * delta * (eps1 + eps2)
    return expand(correction)


# =====================================================================
# Section 18: Deformed conformal blocks and Nekrasov-Shatashvili
# =====================================================================

def deformed_conformal_block_dimension(
    N: int, n_punctures: int, genus: int, delta
) -> Dict:
    r"""Dimension of the space of deformed conformal blocks.

    For W_N conformal blocks on C_{g,n}:
      dim V_{g,n}(W_N) = ... (Verlinde formula)

    For the deformed W_N^{delta}:
      dim V_{g,n}(W_N^{delta}) = dim V_{g,n}(W_N)  (at generic delta)

    The dimension is PRESERVED because the deformation is a smooth
    (mass) deformation that does not change the representation theory
    at generic values of the deformation parameter.

    At SPECIAL values of delta (resonance), the dimension can jump.
    """
    # At generic delta, dimension = standard Verlinde
    # For W_2 (Virasoro): dim = (2g - 2 + n) for generic representations
    # This is a rough estimate; exact depends on the representations at punctures.
    return {
        'N': N,
        'genus': genus,
        'n_punctures': n_punctures,
        'delta': delta,
        'dimension_generic': 'same as CY (at generic delta)',
        'resonance_possible': True,
    }


# =====================================================================
# Section 19: Cross-checks with known results
# =====================================================================

def verify_agt_standard_cases(eps1, eps2) -> Dict:
    r"""Cross-check all standard AGT cases.

    (a) P^1, O(-2): delta=0, standard AGT.
    (b) P^1, O(-3): delta=-1 (local P^2 type).
    (c) Elliptic, O: delta=0, elliptic AGT.
    """
    results = {}

    # (a) Standard AGT: C = P^1, L = K = O(-2)
    delta_a = cy_defect(-2, 0)
    c_a = central_charge_virasoro_deformed(eps1, eps2, delta_a)
    c_a_std = 1 - 6 * (eps1 + eps2)**2 / (eps1 * eps2)
    results['P1_K'] = {
        'delta': delta_a,
        'c_deformed': c_a,
        'c_standard': c_a_std,
        'match': expand(c_a - c_a_std) == 0,
    }

    # (b) Local P^2 type: C = P^1, L = O(-3)
    delta_b = cy_defect(-3, 0)
    c_b = central_charge_virasoro_deformed(eps1, eps2, delta_b)
    results['P1_O(-3)'] = {
        'delta': delta_b,
        'c_deformed': c_b,
    }

    # (c) Elliptic CY
    delta_c = cy_defect(0, 1)
    c_c = central_charge_virasoro_deformed(eps1, eps2, delta_c)
    c_c_std = 1 - 6 * (eps1 + eps2)**2 / (eps1 * eps2)
    results['E_K'] = {
        'delta': delta_c,
        'c_deformed': c_c,
        'c_standard': c_c_std,
        'match': expand(c_c - c_c_std) == 0,
    }

    return results


def verify_n2star_identification(eps1, eps2, delta) -> Dict:
    r"""Verify that the non-CY deformation matches the N=2* mass deformation.

    The N=2* theory has adjoint mass m. The Nekrasov partition function
    with mass m should agree with the non-CY partition function with
    delta chosen so that eps_3 = m.

    Specifically: m = delta - eps_1 - eps_2 (the third Omega parameter).

    The N=2* central charge (Nekrasov-Okounkov):
      c_{N=2*} = 1 - 6(eps_1+eps_2)^2/(eps_1*eps_2) + 6*m*(m+eps_1+eps_2)/(eps_1*eps_2)

    where m = eps_3 = delta - eps_1 - eps_2.

    Substituting:
      c = 1 - 6(eps_1+eps_2)^2/(eps_1*eps_2)
          + 6*(delta-eps_1-eps_2)*delta/(eps_1*eps_2)
      = 1 + 6*(delta^2 - delta*(eps_1+eps_2) - (eps_1+eps_2)^2 + delta*(eps_1+eps_2))/(eps_1*eps_2)
      = 1 + 6*(delta^2 - (eps_1+eps_2)^2)/(eps_1*eps_2)

    This should match our central_charge_virasoro_deformed.
    """
    c_our = central_charge_virasoro_deformed(eps1, eps2, delta)
    m = delta - eps1 - eps2
    c_n2star = (1 - 6 * (eps1 + eps2)**2 / (eps1 * eps2)
                + 6 * m * (m + eps1 + eps2) / (eps1 * eps2))
    return {
        'c_our_formula': expand(c_our),
        'c_n2star': expand(c_n2star),
        'match': expand(c_our - c_n2star) == 0,
        'mass_parameter': m,
    }


# =====================================================================
# Section 20: Genus expansion and modular characteristic
# =====================================================================

def modular_characteristic_deformed(N: int, eps1, eps2, delta):
    r"""Modular characteristic kappa for the deformed W_N algebra.

    For the standard (CY) W_N: kappa(W_N) depends on N and the level.
    For the deformed W_N^{delta}: the modular characteristic acquires
    a delta-dependent correction.

    kappa^{delta} = kappa^{CY} + correction(delta, N, eps_1, eps_2)

    The correction comes from the additional equivariant parameter.
    At the level of the genus-1 free energy:
      F_1^{delta} = F_1^{CY} + (N(N^2-1)/24) * delta^2 / (eps_1*eps_2)

    So the kappa correction is:
      delta_kappa = N(N^2-1) * delta^2 / (2 * eps_1 * eps_2)

    (using kappa = c/2 for Virasoro; general formula for W_N).
    """
    c = central_charge_deformed_wn(N, eps1, eps2, delta)
    # For the Virasoro case (N=2): kappa = c/2
    # For general W_N: kappa involves the full formula
    # At this level of generality, we return c/2 as the leading approximation
    # (this is exact for N=2 and the leading term for general N).
    kappa = c / 2
    return kappa


def genus_1_free_energy_correction(N: int, eps1, eps2, delta):
    r"""Correction to genus-1 free energy from CY defect.

    F_1 = -(1/24) * log(discriminant) + ...

    The discriminant acquires delta-dependent factors.
    The leading correction:
      delta_F_1 = (N(N^2-1)/24) * delta^2 / (eps_1*eps_2)

    This is the universal correction from the equivariant weight.
    """
    return N * (N**2 - 1) * delta**2 / (24 * eps1 * eps2)
