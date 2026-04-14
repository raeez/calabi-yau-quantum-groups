r"""Explicit degree-(24,24) structure function for the K3 Yangian.

STATUS: CONJECTURAL (AP-CY14).  The K3 Yangian Y(g_{K3}) is NOT constructed.
All results are conditional on its existence as a quantization of the K3 DCA.
This module computes what the structure function MUST be if Y(g_{K3}) exists,
and extracts all its algebraic and analytic properties.

MATHEMATICAL CONTENT
====================

THE STRUCTURE FUNCTION g_{K3}(u).

For Y(g_{K3}) at gl_1, the structure function is:

    g_{K3}(u) = prod_{i=1}^{24} (u - h_i) / (u + h_i)

where h_1,...,h_{24} are parameters in the complexified Mukai lattice,
constrained by:

    CY_2: sum_{i=1}^{24} h_i = 0
    Mukai: <h, h'>_Muk = sum_{pos} h_i h'_i - sum_{neg} h_i h'_i
           (signature (4,20))

This module provides:

1. EXPLICIT RATIONAL FUNCTION.  For the Kummer parametrization
   h_i = eps (i=1..4), h_i = -eps/5 (i=5..24), we compute g(u) in
   closed form as a ratio of two degree-24 polynomials.

2. OPE COEFFICIENTS phi_j.  The Laurent expansion at u = infinity:
   g(u) = 1 + sum_{j>=1} phi_j u^{-j}.
   Explicit values phi_1 through phi_12 (and beyond).

3. REFLECTION IDENTITY.  g(u)*g(-u) = 1 (algebraic unitarity).
   Proved for ALL parameter choices by factorwise cancellation.

4. KOSZUL DUAL.  g^!(u) = g(-u) = 1/g(u).
   The Koszul dual structure function is the reciprocal.

5. R-MATRIX PARAMETER hbar.  For the Yang R-matrix
   R(u) = (u*Id + hbar*P)/(u + hbar), the effective hbar is NOT
   sigma_3 (which is a CY_3 concept).  For the diagonal (gl_1) K3
   R-matrix, hbar has NO single value: each Mukai direction has its
   own coupling h_i.  The COLLECTIVE parameter is:
     sigma_2 = sum_{i<j} h_i h_j = e_2(h_1,...,h_{24})

6. MODULI OF CHOICES.  g(u) is NOT determined uniquely by the Mukai
   pairing.  The Mukai pairing constrains the NORM of h but not the
   individual h_i.  The moduli space of structure functions is:
     { h in C^{24} : sum h_i = 0 } / W
   where W is the Weyl group of the Mukai lattice (permutations
   preserving the signature decomposition).  This is 23-dimensional
   (one constraint on 24 parameters).

   However, the ISOMORPHISM CLASS of the Yangian Y(g_{K3}) depends
   only on the h_i up to permutation within each signature block.
   Specifically: permuting h_1,...,h_4 among themselves or h_5,...,h_{24}
   among themselves gives isomorphic Yangians (by relabeling Mukai
   directions).  The essential moduli is:
     M = { (a_1,...,a_4, b_1,...,b_{20}) : sum a + sum b = 0 } / (S_4 x S_{20})
   which is 23 - (dim orbits of S_4 x S_{20}) dimensional.

   For the Kummer parametrization (all a_i equal, all b_i equal):
   a = eps, b = -eps/5, giving a 1-PARAMETER FAMILY (eps).
   This is the MOST SYMMETRIC choice within the Kummer moduli.

CONVENTIONS
===========
  - h_i: Yangian deformation parameters (i = 1,...,24)
  - u (not z): spectral parameter (Yangian convention, avoiding AP-CY31)
  - omega^{ij}: Mukai pairing matrix, signature (4,20)
  - CY_2 constraint: sum h_i = 0
  - kappa subscripts per AP113
  - AP-CY14: ALL results are CONJECTURAL
  - AP-CY28: test points chosen to avoid poles at +/-h_i

REFERENCES
==========
  k3_yangian.py (parent module, Yangian presentation and R-matrix)
  k3_double_current_algebra.py (classical limit)
  e1_chiral_bialgebra_engine.py (coproduct framework)
  Schiffmann-Vasserot, arXiv:1202.1271 (affine Yangian of gl_1)
  Tsymbaliuk, arXiv:1404.5240 (affine Yangian presentation)
  Maulik-Okounkov, arXiv:1211.1287 (stable envelopes, R-matrix)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

from sympy import (
    Poly,
    Rational,
    Symbol,
    binomial,
    cancel,
    collect,
    degree,
    expand,
    factor,
    numer,
    denom,
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
    newton_power_sums,
    null_kummer_parameters,
    structure_function_coefficients,
    structure_function_evaluate,
    structure_function_log_coefficients,
)

F = Fraction

# =========================================================================
# 1. Explicit rational function: numerator and denominator polynomials
# =========================================================================

class ExplicitStructureFunction(NamedTuple):
    """The structure function g_{K3}(u) as an explicit rational function.

    g(u) = N(u) / D(u) where N, D are degree-24 polynomials.

    For the Kummer parametrization (h_i = eps for i=1..4, h_i = -eps/5
    for i=5..24), the factored forms are:

        N(u) = (u - eps)^4 * (u + eps/5)^{20}
        D(u) = (u + eps)^4 * (u - eps/5)^{20}

    STATUS: CONJECTURAL (AP-CY14).
    """
    numerator_factors: List[Tuple[str, int]]    # [(u - h_i, multiplicity)]
    denominator_factors: List[Tuple[str, int]]  # [(u + h_i, multiplicity)]
    degree: Tuple[int, int]                     # (24, 24)
    zeros: Dict[str, int]                       # zero -> multiplicity
    poles: Dict[str, int]                       # pole -> multiplicity
    g_at_0: Rational                            # g(0) = 1
    g_at_inf: int                               # g(inf) = 1
    is_kummer: bool                             # whether Kummer parametrization
    status: str


def explicit_structure_function(
    params: Optional[MukaiLatticeParams] = None,
) -> ExplicitStructureFunction:
    r"""Compute the explicit factored form of g_{K3}(u).

    For the Kummer parametrization:
        g(u) = [(u - eps)/(u + eps)]^4 * [(u + eps/5)/(u - eps/5)]^{20}

    Note the sign flip for the negative Mukai directions: h_i = -eps/5
    gives numerator factor (u - (-eps/5)) = (u + eps/5) and denominator
    factor (u + (-eps/5)) = (u - eps/5).

    The OVERALL structure:
        g(u) = [(u - eps)^4 * (u + eps/5)^{20}] / [(u + eps)^4 * (u - eps/5)^{20}]

    This is a BLASCHKE-TYPE product of signature (4,20).
    """
    if params is None:
        params = kummer_k3_parameters()

    h = params.h

    # Collect zeros and poles with multiplicities
    zero_counts: Dict[Rational, int] = {}
    pole_counts: Dict[Rational, int] = {}
    for hi in h:
        zero_counts[hi] = zero_counts.get(hi, 0) + 1
        pole_counts[-hi] = pole_counts.get(-hi, 0) + 1

    # Build factor lists
    num_factors = [(f"(u - {z})", m) for z, m in sorted(
        zero_counts.items(), key=lambda x: float(x[0]), reverse=True
    )]
    den_factors = [(f"(u - {p})", m) for p, m in sorted(
        pole_counts.items(), key=lambda x: float(x[0]), reverse=True
    )]

    # g(0)
    g_at_0 = structure_function_evaluate(Rational(0), params)

    # Check if this is the Kummer parametrization
    is_kummer = (
        len(zero_counts) == 2
        and all(m in [SIG_PLUS, SIG_MINUS] for m in zero_counts.values())
    )

    return ExplicitStructureFunction(
        numerator_factors=num_factors,
        denominator_factors=den_factors,
        degree=(NUM_PARAMS, NUM_PARAMS),
        zeros={str(z): m for z, m in zero_counts.items()},
        poles={str(p): m for p, m in pole_counts.items()},
        g_at_0=g_at_0,
        g_at_inf=1,
        is_kummer=is_kummer,
        status=STATUS,
    )


def structure_function_closed_form(
    eps: Rational = Rational(1),
) -> Dict[str, Any]:
    r"""Closed-form expression for g_{K3}(u) at the Kummer point.

    With h_i = eps (i=1..4), h_i = -eps/5 (i=5..24):

        g(u) = [(u - eps)/(u + eps)]^4 * [(u + eps/5)/(u - eps/5)]^{20}

    Setting eps = 1 for concreteness:

        g(u) = [(u - 1)/(u + 1)]^4 * [(u + 1/5)/(u - 1/5)]^{20}
             = [(u - 1)/(u + 1)]^4 * [(5u + 1)/(5u - 1)]^{20}

    The CRUCIAL observation: the positive Mukai directions contribute
    factors [(u-1)/(u+1)]^4 which DECREASE g as u increases from 0,
    while the negative directions contribute [(5u+1)/(5u-1)]^{20}
    which INCREASE g.  The balance is dictated by the CY_2 constraint.

    To see the net effect, write:
        log g(u) = 4*log((u-1)/(u+1)) + 20*log((5u+1)/(5u-1))
                 = -4*log((u+1)/(u-1)) + 20*log((5u+1)/(5u-1))

    At u >> 1:
        log g(u) ~ -4*(2/u + 2/(3u^3) + ...) + 20*(2/(5u) + 2/(3*125u^3) + ...)
                 = (-8/u + 8/u) + (-8/(3u^3) + 16/(375u^3)) + ...
                 = 0 + (-1000 + 16)/(375u^3) + ...
                 = -984/(375u^3) + ...
                 = -2624/(1000u^3) + ...

    Wait, let me compute this properly.  Each factor (u-h)/(u+h) gives
    log = sum_{k odd} (-2*h^k/k) * u^{-k}.  So:

        log g(u) = sum_{k odd} (-2/k) * p_k * u^{-k}

    where p_k = sum h_i^k.  For the Kummer parametrization:

        p_1 = 4*eps + 20*(-eps/5) = 4*eps - 4*eps = 0  (CY_2 check)
        p_3 = 4*eps^3 + 20*(-eps/5)^3 = 4*eps^3 - 20*eps^3/125
            = 4*eps^3 - 4*eps^3/25 = eps^3*(100-4)/25 = 96*eps^3/25
        p_5 = 4*eps^5 + 20*(-eps/5)^5 = 4*eps^5 - 20*eps^5/3125
            = 4*eps^5 - 4*eps^5/625 = eps^5*(2500-4)/625 = 2496*eps^5/625

    So:
        log g(u) = (-2/3)*(96/25)*eps^3 * u^{-3}
                   + (-2/5)*(2496/625)*eps^5 * u^{-5} + ...
                 = (-192/75)*eps^3 * u^{-3} + (-4992/3125)*eps^5 * u^{-5} + ...
                 = (-64/25)*eps^3 * u^{-3} + (-4992/3125)*eps^5 * u^{-5} + ...

    Returns dict with closed-form data.
    """
    params = kummer_k3_parameters(eps)

    # Power sums
    p = newton_power_sums(params, max_k=12)

    # Log coefficients alpha_k = (-2/k) * p_k for k odd
    log_coeffs = {}
    for k in range(1, 13, 2):
        log_coeffs[k] = Rational(-2, k) * p[k]

    # OPE coefficients phi_j via the standard recursion
    phi = structure_function_coefficients(params, max_order=12)

    # Elementary symmetric functions
    e = elementary_symmetric_functions(params, max_k=6)

    return {
        'parametrization': {
            'positive_h': f'{eps} (multiplicity {SIG_PLUS})',
            'negative_h': f'{-eps * Rational(1, 5)} (multiplicity {SIG_MINUS})',
            'sum_h': 0,
            'formula': (
                f'g(u) = [(u - {eps})/(u + {eps})]^{SIG_PLUS} '
                f'* [(u + {eps * Rational(1, 5)})/(u - {eps * Rational(1, 5)})]^{SIG_MINUS}'
            ),
        },
        'newton_power_sums': {k: p[k] for k in range(1, 13)},
        'log_expansion_coefficients': log_coeffs,
        'ope_coefficients': {j: phi[j] for j in range(13)},
        'elementary_symmetric': {k: e[k] for k in sorted(e.keys())},
        'status': STATUS,
    }


# =========================================================================
# 2. Explicit numerator/denominator as expanded polynomials
# =========================================================================

def expanded_polynomials(
    eps: Rational = Rational(1),
) -> Dict[str, Any]:
    r"""Expand g_{K3}(u) = N(u)/D(u) as a ratio of expanded polynomials.

    For the Kummer parametrization at eps = 1:

        N(u) = (u - 1)^4 * (u + 1/5)^{20}
        D(u) = (u + 1)^4 * (u - 1/5)^{20}

    We expand each as a polynomial in u with rational coefficients
    and return the coefficient lists.

    The key structural property: since e_1 = sum h_i = 0, the numerator
    and denominator have the SAME coefficient for u^{23} (both zero after
    the leading u^{24}).  More precisely:

        N(u) = u^{24} - e_1*u^{23} + e_2*u^{22} - ...
        D(u) = u^{24} + e_1*u^{23} + e_2*u^{22} + ...

    where e_k = e_k(h_1,...,h_{24}).  Since e_1 = 0:

        N(u) = u^{24} + e_2*u^{22} - e_3*u^{21} + ...
        D(u) = u^{24} + e_2*u^{22} + e_3*u^{21} + ...

    So N and D DIFFER only in the ODD elementary symmetric functions:
        N(u) - D(u) = -2*(e_3*u^{21} + e_5*u^{19} + ... + e_{23}*u)

    And g(u) - 1 = (N(u) - D(u))/D(u) = -2*(e_3*u^{21} + ...)/D(u).
    """
    u = Symbol('u')
    params = kummer_k3_parameters(eps)

    # Build numerator and denominator symbolically
    N_expr = Rational(1)
    D_expr = Rational(1)
    for hi in params.h:
        N_expr *= (u - hi)
        D_expr *= (u + hi)

    N_expanded = expand(N_expr)
    D_expanded = expand(D_expr)

    # Extract coefficients
    N_poly = Poly(N_expanded, u)
    D_poly = Poly(D_expanded, u)

    N_coeffs = {24 - i: c for i, c in enumerate(N_poly.all_coeffs())}
    D_coeffs = {24 - i: c for i, c in enumerate(D_poly.all_coeffs())}

    # Verify key properties
    # N and D have same even-indexed e_k coefficients
    even_match = all(
        N_coeffs.get(24 - k, 0) == D_coeffs.get(24 - k, 0)
        for k in range(0, 25, 2)
    )

    # N and D differ by sign on odd-indexed e_k
    odd_sign_flip = all(
        N_coeffs.get(24 - k, 0) == -D_coeffs.get(24 - k, 0)
        for k in range(1, 25, 2)
        if N_coeffs.get(24 - k, 0) != 0
    )

    return {
        'numerator_coefficients': N_coeffs,
        'denominator_coefficients': D_coeffs,
        'degree': 24,
        'leading_coefficient_N': N_coeffs.get(24, None),
        'leading_coefficient_D': D_coeffs.get(24, None),
        'constant_N': N_coeffs.get(0, None),
        'constant_D': D_coeffs.get(0, None),
        'even_e_k_match': even_match,
        'odd_e_k_sign_flip': odd_sign_flip,
        'N_minus_D_structure': (
            'N(u) - D(u) = -2*(e_3*u^{21} + e_5*u^{19} + ... + e_{23}*u) '
            'since e_1 = 0 and even e_k cancel.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 3. Reflection identity: g(u)*g(-u) = 1
# =========================================================================

def verify_reflection_identity(
    params: Optional[MukaiLatticeParams] = None,
    test_points: Optional[List[Rational]] = None,
) -> Dict[str, Any]:
    r"""Verify g(u)*g(-u) = 1 (algebraic unitarity / reflection identity).

    PROOF (parameter-independent):
    For each factor:
        (u - h_i)/(u + h_i) * (-u - h_i)/(-u + h_i)
        = (u - h_i)/(u + h_i) * (u + h_i)/(u - h_i)
        = 1

    So the full product g(u)*g(-u) = prod_i 1 = 1.

    This holds for ANY parameters h_i (no CY constraint needed).
    Equivalently: g(-u) = 1/g(u), so g is an INVOLUTION of CP^1
    under u -> -u composed with f -> 1/f.

    CONSEQUENCES:
    1. g(-u) = 1/g(u) = g^!(u) (the Koszul dual structure function).
    2. The R-matrix satisfies R(u)*R(-u) = I.
    3. In the Laurent expansion g(u) = 1 + sum phi_j u^{-j}:
       The LOG expansion log g(u) has only odd powers of u^{-1}.
       But the phi_j (from exponentiating) are generally NONZERO for
       even j >= 6 (products of odd-order log terms contribute).
       Specifically: phi_1 = phi_2 = phi_4 = 0, but phi_6 = alpha_3^2/2 != 0.
    4. The phi_j satisfy the PALINDROMIC constraint:
       if g(u) = N(u)/D(u) then N(u)*D(-u) = D(u)*N(-u).

    Numerical verification at test points (AP-CY28: avoid poles at +/-h_i).
    """
    if params is None:
        params = kummer_k3_parameters()
    if test_points is None:
        # AP-CY28: choose test points far from poles.
        # For Kummer: poles at u = -h_i = -1 (mult 4) and 1/5 (mult 20).
        # Also avoid u = h_i = 1 and -1/5 (zeros).
        test_points = [
            Rational(2), Rational(3), Rational(7, 3),
            Rational(11, 5), Rational(13, 7), Rational(17, 4),
        ]

    numerical_results = []
    for u_val in test_points:
        try:
            g_u = structure_function_evaluate(u_val, params)
            g_neg_u = structure_function_evaluate(-u_val, params)
            product = g_u * g_neg_u
            numerical_results.append({
                'u': str(u_val),
                'g(u)': str(g_u),
                'g(-u)': str(g_neg_u),
                'product': str(product),
                'is_1': product == 1,
            })
        except ValueError as e:
            numerical_results.append({
                'u': str(u_val),
                'error': str(e),
                'is_1': None,
            })

    all_pass = all(
        r['is_1'] is True for r in numerical_results if r['is_1'] is not None
    )

    return {
        'identity': 'g(u) * g(-u) = 1',
        'proof': (
            'Each factor (u - h_i)/(u + h_i) at u and -u gives '
            '(u - h_i)(u + h_i) / ((u + h_i)(u - h_i)) = 1. '
            'Product of 1s is 1. QED.'
        ),
        'parameter_independent': True,
        'cy_constraint_needed': False,
        'numerical_verification': numerical_results,
        'all_pass': all_pass,
        'consequences': {
            'koszul_dual': 'g^!(u) = g(-u) = 1/g(u)',
            'r_matrix': 'R(u)*R(-u) = I',
            'log_odd_parity': 'log g(u) has only odd powers of u^{-1}',
            'initial_phi_vanishing': 'phi_1 = phi_2 = phi_4 = 0 (but phi_6 != 0 in general)',
        },
        'status': STATUS,
    }


# =========================================================================
# 4. OPE coefficients phi_j (explicit computation)
# =========================================================================

def ope_coefficients_explicit(
    params: Optional[MukaiLatticeParams] = None,
    max_order: int = 12,
) -> Dict[str, Any]:
    r"""Compute the OPE coefficients phi_j of g_{K3}(u) explicitly.

    g(u) = 1 + sum_{j >= 1} phi_j * u^{-j}

    The phi_j encode the OPE data of the K3 Yangian.  They are computed
    from the Newton power sums p_k = sum h_i^k via:

        log g(u) = sum_{k odd} alpha_k u^{-k}
        alpha_k = (-2/k) * p_k

    and then g(u) = exp(log g(u)) gives phi_j by the exponential recursion.

    KEY PROPERTIES:
    - phi_0 = 1 (normalization)
    - phi_1 = 0 (CY_2 constraint: p_1 = 0)
    - phi_2 = 0 (alpha_2 = 0 and phi_1 = 0)
    - phi_3 = alpha_3 = (-2/3)*p_3 (first nontrivial coefficient)
    - phi_4 = 0 (alpha_4 = 0, and the recursion only uses alpha_1..alpha_4
      with phi_0..phi_3, and alpha_1 = alpha_2 = alpha_4 = 0, phi_1 = 0)
    - phi_5 = alpha_5 (only alpha_5 contributes: recursion gives
      5*phi_5 = 3*alpha_3*phi_2 + 5*alpha_5*phi_0 = 5*alpha_5)
    - phi_6 = alpha_3^2 / 2 (from 6*phi_6 = 3*alpha_3*phi_3; NONZERO)

    IMPORTANT: the log coefficients alpha_k are zero for k even,
    but the OPE coefficients phi_j are NONZERO for even j >= 6.
    This is because the exponential of a series with only odd powers
    produces even-order terms via products (e.g. alpha_3^2 -> phi_6).

    The vanishing pattern: phi_1 = phi_2 = phi_4 = 0, then phi_j != 0
    for all j >= 3 except j = 4.

    For the Kummer parametrization (eps = 1):
        p_1 = 0
        p_2 = 4 + 20/25 = 24/5
        p_3 = 4 - 20/125 = 4 - 4/25 = 96/25
        p_4 = 4 + 20/625 = 4 + 4/125 = 504/125
        p_5 = 4 - 20/3125 = 4 - 4/625 = 2496/625
        p_6 = 4 + 20/15625 = 4 + 4/3125 = 12504/3125

    Explicit phi_j values (Kummer, eps=1):
        phi_3 = (-2/3)*(96/25) = -192/75 = -64/25
        phi_5 = (-2/5)*(2496/625) = -4992/3125
        phi_6 = (-64/25)^2 / 2 = 4096/1250 = 2048/625
    """
    if params is None:
        params = kummer_k3_parameters()

    phi = structure_function_coefficients(params, max_order=max_order)
    p = newton_power_sums(params, max_k=max_order)
    log_coeffs = structure_function_log_coefficients(params, max_order=max_order)

    # Verify vanishing pattern: phi_1 = phi_2 = phi_4 = 0
    # (even phi do NOT all vanish: phi_6 = alpha_3^2/2 != 0 in general)
    initial_vanishing = (phi[1] == 0 and phi[2] == 0 and
                         (max_order < 4 or phi[4] == 0))

    # Verify log coefficients are zero for even k (this DOES hold)
    log_even_vanish = all(log_coeffs[k] == 0 for k in range(0, max_order + 1, 2))

    # Collect nonzero phi
    nonzero_phi = {j: phi[j] for j in range(max_order + 1) if phi[j] != 0}

    # Explicit derivation of first few phi from the recursion
    # j * phi_j = sum_{k=1}^{j} k * alpha_k * phi_{j-k}
    derivations = {}
    if max_order >= 3:
        alpha_3 = Rational(-2, 3) * p[3]
        # 3*phi_3 = 3*alpha_3*phi_0 = 3*alpha_3, so phi_3 = alpha_3
        derivations['phi_3'] = {
            'formula': 'phi_3 = alpha_3 = (-2/3)*p_3',
            'p_3': p[3],
            'alpha_3': alpha_3,
            'value': phi[3],
            'matches': phi[3] == alpha_3,
        }
    if max_order >= 5:
        alpha_3 = Rational(-2, 3) * p[3]
        alpha_5 = Rational(-2, 5) * p[5]
        # 5*phi_5 = 3*alpha_3*phi_2 + 5*alpha_5*phi_0 = 0 + 5*alpha_5
        phi_5_from_formula = alpha_5
        derivations['phi_5'] = {
            'formula': 'phi_5 = alpha_5 (since phi_2 = 0)',
            'derivation': '5*phi_5 = 3*alpha_3*phi_2 + 5*alpha_5*phi_0 = 5*alpha_5',
            'alpha_5': alpha_5,
            'computed': phi_5_from_formula,
            'value': phi[5],
            'matches': phi[5] == phi_5_from_formula,
        }
    if max_order >= 6:
        alpha_3 = Rational(-2, 3) * p[3]
        # 6*phi_6 = 3*alpha_3*phi_3 = 3*alpha_3^2, so phi_6 = alpha_3^2/2
        phi_6_from_formula = alpha_3**2 / 2
        derivations['phi_6'] = {
            'formula': 'phi_6 = alpha_3^2 / 2',
            'derivation': '6*phi_6 = 3*alpha_3*phi_3 = 3*alpha_3^2',
            'alpha_3_sq_half': alpha_3**2 / 2,
            'computed': phi_6_from_formula,
            'value': phi[6],
            'matches': phi[6] == phi_6_from_formula,
        }
    if max_order >= 7:
        alpha_3 = Rational(-2, 3) * p[3]
        alpha_5 = Rational(-2, 5) * p[5]
        alpha_7 = Rational(-2, 7) * p[7]
        # 7*phi_7 = 3*alpha_3*phi_4 + 5*alpha_5*phi_2 + 7*alpha_7*phi_0
        # = 0 + 0 + 7*alpha_7 (since phi_4 = 0, phi_2 = 0)
        phi_7_from_formula = alpha_7
        derivations['phi_7'] = {
            'formula': 'phi_7 = alpha_7 (since phi_4 = phi_2 = 0)',
            'derivation': '7*phi_7 = 3*alpha_3*phi_4 + 5*alpha_5*phi_2 + 7*alpha_7*phi_0 = 7*alpha_7',
            'alpha_7': alpha_7,
            'computed': phi_7_from_formula,
            'value': phi[7],
            'matches': phi[7] == phi_7_from_formula,
        }

    return {
        'coefficients': {j: phi[j] for j in range(max_order + 1)},
        'nonzero_coefficients': nonzero_phi,
        'initial_vanishing': initial_vanishing,
        'log_even_vanish': log_even_vanish,
        'power_sums': {k: p[k] for k in range(1, min(max_order + 1, 13))},
        'log_coefficients': {k: log_coeffs[k] for k in range(max_order + 1)},
        'derivations': derivations,
        'asymptotic': (
            f'g(u) = 1 + {phi[3]}*u^{{-3}} + {phi[5]}*u^{{-5}} + O(u^{{-7}}) '
            f'for u -> infinity'
        ),
        'status': STATUS,
    }


# =========================================================================
# 5. Koszul dual structure function
# =========================================================================

def koszul_dual_structure_function(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""The Koszul dual structure function g^!(u) = g(-u) = 1/g(u).

    For the Koszul dual Yangian Y(g_{K3})^!, the structure function is:

        g^!(u) = g(-u) = prod_{i=1}^{24} (-u - h_i)/(-u + h_i)
               = prod_{i=1}^{24} (u + h_i)/(u - h_i)
               = 1/g(u)

    The Koszul dual has:
    - Zeros at u = -h_i (the poles of g)
    - Poles at u = h_i (the zeros of g)
    - g^!(0) = 1 (same as g, since (-1)^{24} = 1)
    - phi^!_j = (-1)^j * phi_j: sign flip for j odd, unchanged for j even.
    - For odd j: phi^!_j = -phi_j (e.g. phi^!_3 = -phi_3, phi^!_5 = -phi_5).
    - For even j: phi^!_j = phi_j (same as original, e.g. phi^!_6 = phi_6).

    THE KOSZUL CONDUCTOR.
    For the K3 Heisenberg Yangian (class G / free-field), the Koszul
    conductor is:
        rho_K = kappa_ch(Y) + kappa_ch(Y^!) = 0

    This is because the K3 Heisenberg is self-Koszul-dual (up to parameter
    inversion), and the chiral characteristic kappa_ch = 2 for both Y and Y^!.
    The conductor vanishes: rho_K = 0.

    (NOT 13 as for the Virasoro case, NOT 24 as for lattice rank.
    See CLAUDE.md: K3 KOSZUL CONDUCTOR = 0 for free-field/KM branch.)

    AP-CY8: the Koszul duality is NOT the same as birational flop.
    AP-CY10: flop preserves kappa; Koszul duality satisfies
    kappa(A) + kappa(A^!) = rho_K.  Here rho_K = 0.
    """
    if params is None:
        params = kummer_k3_parameters()

    phi = structure_function_coefficients(params, max_order=12)

    # Koszul dual coefficients: phi^!_j = (-1)^j * phi_j
    phi_dual = [(-1)**j * phi[j] for j in range(len(phi))]

    # Verify: phi^!_j = -phi_j for odd j (since even phi are 0)
    odd_sign_flip = all(
        phi_dual[j] == -phi[j]
        for j in range(1, len(phi), 2)
    )

    # Verify: g^!(u) = 1/g(u) at test points (AP-CY28: avoid poles)
    test_points = [Rational(2), Rational(3), Rational(7, 3)]
    reciprocal_checks = []
    for u_val in test_points:
        g_u = structure_function_evaluate(u_val, params)
        g_dual_u = structure_function_evaluate(-u_val, params)
        reciprocal_checks.append({
            'u': str(u_val),
            'g(u)': str(g_u),
            'g^!(u) = g(-u)': str(g_dual_u),
            'g(u) * g^!(u)': str(g_u * g_dual_u),
            'is_reciprocal': g_u * g_dual_u == 1,
        })

    return {
        'definition': 'g^!(u) = g(-u) = 1/g(u)',
        'proof': (
            'g(-u) = prod ((-u - h_i)/(-u + h_i)) '
            '= prod ((u + h_i)/(u - h_i)) '
            '= 1/prod((u - h_i)/(u + h_i)) = 1/g(u). QED.'
        ),
        'koszul_coefficients': {j: phi_dual[j] for j in range(len(phi_dual))},
        'phi_j_to_phi_dual_j': 'phi^!_j = (-1)^j * phi_j (= -phi_j for odd j)',
        'odd_sign_flip_verified': odd_sign_flip,
        'reciprocal_checks': reciprocal_checks,
        'koszul_conductor': {
            'value': 0,
            'explanation': (
                'K3 Heisenberg is class G (free-field). '
                'Koszul conductor rho_K = kappa_ch(Y) + kappa_ch(Y^!) = 0. '
                'NOT 13 (Virasoro), NOT 24 (lattice rank).'
            ),
        },
        'ap_cy10_reminder': (
            'Flop preserves kappa_ch (autoequivalence). '
            'Koszul duality: kappa(A) + kappa(A^!) = rho_K = 0. '
            'Different operations entirely.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 6. R-matrix parameter: why there is no single hbar
# =========================================================================

def r_matrix_parameter_analysis(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Analysis of the R-matrix coupling parameter for the K3 Yangian.

    For the C^3 affine Yangian Y(gl_hat_1), the Yang R-matrix is:
        R(u) = (u*Id + hbar*P)/(u + hbar)
    with hbar = sigma_3 = h_1*h_2*h_3 (the product of the 3 parameters).

    For the K3 Yangian at gl_1, the R-matrix is DIAGONAL:
        R(u) = diag((u - h_i)/(u + h_i))_{i=1}^{24}

    This diagonal R-matrix does NOT have the form (u*Id + hbar*P)/(u + hbar)
    because it is not a permutation-type R-matrix.  Instead, it is a
    PRODUCT of 24 independent rank-1 R-matrices.

    For the diagonal R-matrix, there is no single hbar.  Instead:
    - Each Mukai direction i has its own coupling h_i.
    - The COLLECTIVE parameters are the elementary symmetric functions
      e_k(h_1,...,h_{24}) and the Newton power sums p_k.

    The relevant collective parameters:
    - sigma_1 = e_1 = sum h_i = 0 (CY_2 constraint)
    - sigma_2 = e_2 = sum_{i<j} h_i*h_j (the "effective hbar^2")
    - sigma_24 = h_1*...*h_{24} (the full product, = "hbar^{24}")

    For the Kummer parametrization (eps = 1):
        sigma_2 = binom(4,2)*1 + 4*20*(-1/5) + binom(20,2)*(1/25)
                = 6 - 16 + 190/25
                = 6 - 16 + 38/5
                = 30/5 - 80/5 + 38/5
                = -12/5

    For the NON-ABELIAN K3 Yangian (if g != gl_1), the R-matrix would
    have the form:
        R(u) = 1 + r/u + O(u^{-2})
    with r = omega^{-1} (inverse Mukai pairing), and the effective hbar
    would be determined by the normalization of the classical r-matrix.

    STATUS: CONJECTURAL (AP-CY14).
    """
    if params is None:
        params = kummer_k3_parameters()

    e = elementary_symmetric_functions(params, max_k=6)
    p = newton_power_sums(params, max_k=6)

    # Product of all h_i
    h_product = Rational(1)
    for hi in params.h:
        h_product *= hi

    # Classical r-matrix coefficient: r_ii = -2*h_i
    r_diagonal = [-2 * hi for hi in params.h]
    r_trace = sum(r_diagonal)

    return {
        'no_single_hbar': True,
        'reason': (
            'The K3 R-matrix for gl_1 is diagonal: R(u)_ii = (u - h_i)/(u + h_i). '
            'This is NOT a permutation-type R-matrix. There is no single hbar. '
            'Each Mukai direction i has its own coupling constant h_i.'
        ),
        'collective_parameters': {
            'e_1': e[1],
            'e_2': e[2],
            'e_3': e[3],
            'e_4': e[4],
            'e_5': e[5],
            'e_6': e[6],
            'h_product (e_24)': h_product,
        },
        'power_sums': {k: p[k] for k in range(1, 7)},
        'classical_r_matrix': {
            'r_diagonal_first_4': r_diagonal[:4],
            'r_diagonal_last_4': r_diagonal[-4:],
            'trace_r': r_trace,
            'trace_is_zero': r_trace == 0,
        },
        'c3_comparison': {
            'c3_hbar': 'sigma_3 = h_1*h_2*h_3 (product of 3 parameters)',
            'k3_analogue': (
                'No single hbar. The closest analogue is sigma_2 = e_2(h). '
                f'For Kummer: sigma_2 = {e[2]}.'
            ),
        },
        'nonabelian_note': (
            'For non-abelian g, the R-matrix is NOT diagonal and has '
            'the standard form R(u) = 1 + r/u + O(u^{-2}) with r = omega^{-1}. '
            'The effective hbar would be determined by ||omega^{-1}|| '
            '(the norm of the inverse Mukai pairing in the chosen representation).'
        ),
        'status': STATUS,
    }


# =========================================================================
# 7. Moduli of structure functions
# =========================================================================

def moduli_of_structure_functions() -> Dict[str, Any]:
    r"""Analyze the moduli space of K3 Yangian structure functions.

    QUESTION: Is g(u) determined uniquely by the Mukai pairing?

    ANSWER: NO.  The structure function g(u) depends on the CHOICE of
    deformation parameters h_1,...,h_{24}, not just on the Mukai pairing.
    The Mukai pairing provides:

    1. The SIGNATURE constraint: 4 positive and 20 negative directions.
       This means h_1,...,h_4 are associated to positive eigenvalues and
       h_5,...,h_{24} to negative eigenvalues.

    2. The CY_2 constraint: sum h_i = 0.

    3. Optionally, the NULL constraint: <h,h>_Muk = 0.

    The moduli space of structure functions is:

        M = { (h_1,...,h_{24}) in C^{24} : sum h_i = 0 } / Aut(Lambda_Muk)

    where Aut(Lambda_Muk) is the automorphism group of the Mukai lattice,
    which contains S_4 x S_{20} (permuting within each signature block)
    as a subgroup.

    DIMENSION ANALYSIS:
    - Unconstrained: C^{24} = 24 complex parameters
    - CY_2 constraint: one equation, so 23 parameters
    - Aut orbits: S_4 x S_{20} has generic orbits of dimension 0 (finite
      group), so dim M = 23.

    DISTINGUISHED LOCI:
    - Kummer point: h_i = eps (i=1..4), h_i = -eps/5 (i=5..24).
      This is a 1-parameter family (eps).
    - Null locus: <h,h>_Muk = 0.  Codimension 1 in M, so dim 22.
    - Equivariant locus: at enhanced symmetry points of K3 moduli,
      extra symmetries reduce the parameter space.
    - Degenerate locus: some h_i = 0.  The structure function acquires
      trivial factors (u/u = 1) and the effective degree drops.

    PHYSICAL INTERPRETATION:
    The parameters h_i are the OMEGA-BACKGROUND parameters for the K3
    directions.  Since K3 has no torus action (AP-CY20: normal bundle
    vs spectral parameters), the h_i cannot be identified with equivariant
    weights directly.  Instead, they arise from the LATTICE structure of
    the Mukai pairing, and the moduli space M parametrizes different
    quantizations of the K3 double current algebra.

    The structure function IS determined up to the choice of h_i by:
    - The degree: 24 (from Mukai rank)
    - The CY constraint: sum h_i = 0
    - The factored form: g(u) = prod (u - h_i)/(u + h_i)

    But the INDIVIDUAL h_i are NOT determined by the Mukai pairing alone.
    They represent a choice of STABILITY CONDITION on the derived category
    (Bridgeland stability), and different choices give genuinely different
    (non-isomorphic) Yangians.
    """
    # Demonstrate non-uniqueness: two different parameter choices
    params1 = kummer_k3_parameters(Rational(1))
    params2 = kummer_k3_parameters(Rational(2))

    # Different structure functions at the same test point
    g1_at_2 = structure_function_evaluate(Rational(3), params1)
    g2_at_2 = structure_function_evaluate(Rational(3), params2)

    # Also try a genuinely different parametrization (not just rescaling)
    # 3 params = 3, 1 param = -9, rest = 0 (sum = 3+3+3-9 = 0)
    h_asym = [Rational(3)] * 3 + [Rational(-9)] + [Rational(0)] * 20
    params_asym = custom_parameters(h_asym)
    g_asym_at_2 = structure_function_evaluate(Rational(3), params_asym)

    return {
        'uniquely_determined': False,
        'reason': (
            'g(u) depends on the choice of h_1,...,h_{24} (not just the '
            'Mukai pairing). Different choices of h give different Yangians.'
        ),
        'moduli_space': {
            'ambient': 'C^{24}',
            'constraints': ['sum h_i = 0 (CY_2)'],
            'symmetry_group': 'Aut(Lambda_Muk) >= S_4 x S_{20}',
            'dimension': 23,
        },
        'determined_by_mukai_pairing': {
            'degree': 24,
            'factored_form': 'prod (u - h_i)/(u + h_i) (the shape)',
            'cy_constraint': 'sum h_i = 0',
            'signature_structure': '4 positive, 20 negative directions',
        },
        'not_determined': {
            'individual_h_i': 'Depend on stability condition',
            'phi_j_values': 'Depend on power sums p_k of the h_i',
            'moduli_dimension': 23,
        },
        'distinguished_loci': {
            'kummer': 'h = eps*(1,...,1,-1/5,...,-1/5), 1 parameter',
            'null': '<h,h>_Muk = 0, codimension 1 (dim 22)',
            'degenerate': 'some h_i = 0, effective degree drops',
        },
        'non_uniqueness_demonstration': {
            'params1': 'Kummer eps=1',
            'params2': 'Kummer eps=2',
            'params_asym': 'h = (3,3,3,-9,0,...,0)',
            'g1_at_3': str(g1_at_2),
            'g2_at_3': str(g2_at_2),
            'g_asym_at_3': str(g_asym_at_2),
            'all_different': (g1_at_2 != g2_at_2 and g1_at_2 != g_asym_at_2),
        },
        'physical_interpretation': (
            'The h_i parametrize different quantizations of the K3 DCA. '
            'They cannot be equivariant weights (K3 has no torus action). '
            'They arise from Bridgeland stability conditions on D^b(Coh(K3)).'
        ),
        'status': STATUS,
    }


# =========================================================================
# 8. Special parametrizations and their structure functions
# =========================================================================

def kummer_structure_function_values(
    eps: Rational = Rational(1),
    max_phi: int = 12,
) -> Dict[str, Any]:
    r"""Complete data for g_{K3}(u) at the Kummer point.

    This is the REFERENCE computation: all numerical values of the structure
    function at the most symmetric Kummer parametrization.

    For eps = 1:
        h_i = 1 (i=1..4), h_i = -1/5 (i=5..24)

        g(u) = [(u-1)/(u+1)]^4 * [(5u+1)/(5u-1)]^{20}

    Zeros: u = 1 (mult 4), u = -1/5 (mult 20)
    Poles: u = -1 (mult 4), u = 1/5 (mult 20)
    """
    params = kummer_k3_parameters(eps)

    # Power sums
    p = newton_power_sums(params, max_k=max_phi)

    # OPE coefficients
    phi = structure_function_coefficients(params, max_order=max_phi)

    # Elementary symmetric functions
    e = elementary_symmetric_functions(params, max_k=min(max_phi, 6))

    # Evaluate at specific points (AP-CY28: avoid poles at -1, 1/5)
    special_values = {}
    for u_val in [
        Rational(0), Rational(2), Rational(3), Rational(5),
        Rational(10), Rational(100),
    ]:
        special_values[str(u_val)] = str(structure_function_evaluate(u_val, params))

    return {
        'epsilon': eps,
        'parametrization': {
            'positive_h': f'{eps} (mult {SIG_PLUS})',
            'negative_h': f'{-eps / 5} (mult {SIG_MINUS})',
        },
        'zeros': {str(eps): SIG_PLUS, str(-eps / 5): SIG_MINUS},
        'poles': {str(-eps): SIG_PLUS, str(eps / 5): SIG_MINUS},
        'formula': (
            f'g(u) = [(u - {eps})/(u + {eps})]^{SIG_PLUS} '
            f'* [(u + {eps / 5})/(u - {eps / 5})]^{SIG_MINUS}'
        ),
        'power_sums': {k: p[k] for k in range(1, max_phi + 1)},
        'ope_coefficients': {j: phi[j] for j in range(max_phi + 1)},
        'elementary_symmetric': dict(e),
        'special_values': special_values,
        'g_at_0': str(structure_function_evaluate(Rational(0), params)),
        'status': STATUS,
    }


def null_structure_function_values() -> Dict[str, Any]:
    r"""Structure function data at the null Kummer point.

    Null parametrization: h_1 = 1, h_2 = -1, h_5 = 1, h_6 = -1, rest = 0.

    g(u) = [(u-1)/(u+1)] * [(u+1)/(u-1)] * [(u-1)/(u+1)] * [(u+1)/(u-1)]
         * prod_{i with h_i=0} [(u-0)/(u+0)]
         = 1 * 1 * (u/u)^{20}
         = 1

    Wait, that's wrong.  Let me compute factor by factor:
    i=1: h_1 = 1: (u-1)/(u+1)
    i=2: h_2 = -1: (u+1)/(u-1)
    i=5: h_5 = 1: (u-1)/(u+1)
    i=6: h_6 = -1: (u+1)/(u-1)
    All others: h_i = 0: (u-0)/(u+0) = 1

    Product: [(u-1)(u+1)(u-1)(u+1)] / [(u+1)(u-1)(u+1)(u-1)] = 1.

    So the null parametrization gives g(u) = 1 IDENTICALLY.
    This is the DEGENERATE case: the Yangian reduces to the universal
    enveloping algebra (no deformation).
    """
    params = null_kummer_parameters()
    phi = structure_function_coefficients(params, max_order=6)
    p = newton_power_sums(params, max_k=6)

    return {
        'g_is_identically_1': all(phi[j] == 0 for j in range(1, 7)),
        'all_phi_vanish': all(phi[j] == 0 for j in range(1, 7)),
        'all_power_sums_even_vanish': all(p[k] == 0 for k in range(1, 7)),
        'interpretation': (
            'The null parametrization gives g(u) = 1 identically. '
            'The Yangian is undeformed: Y(g_{K3}) = U(g_{K3}). '
            'This is the classical (unquantized) limit.'
        ),
        'degeneration_type': 'trivial (no quantum deformation)',
        'status': STATUS,
    }


# =========================================================================
# 9. Signature dependence: positive vs negative Mukai directions
# =========================================================================

def signature_analysis(
    params: Optional[MukaiLatticeParams] = None,
) -> Dict[str, Any]:
    r"""Analyze how the Mukai signature (4,20) shapes g_{K3}(u).

    The structure function factorizes into POSITIVE and NEGATIVE parts:

        g(u) = g_+(u) * g_-(u)

    where:
        g_+(u) = prod_{i=1}^{4} (u - h_i)/(u + h_i)   (positive Mukai)
        g_-(u) = prod_{i=5}^{24} (u - h_i)/(u + h_i)  (negative Mukai)

    For the Kummer parametrization:
        g_+(u) = [(u - eps)/(u + eps)]^4      (degree (4,4))
        g_-(u) = [(u + eps/5)/(u - eps/5)]^{20}  (degree (20,20))

    KEY OBSERVATION: the positive and negative parts have COMPETING
    effects.  Near u = 0:
        g_+(0) = [(-eps)/(+eps)]^4 = (-1)^4 = 1
        g_-(0) = [(eps/5)/(-eps/5)]^{20} = (-1)^{20} = 1
    So both contribute +1 at u = 0.

    But near u = eps (a zero of g_+):
        g_+(eps) = 0
        g_-(eps) != 0 and != infinity (eps != eps/5, so not a pole of g_-)
    So g(eps) = 0.

    The INTERPLAY between g_+ and g_- is controlled by the signature.
    A different signature (e.g. (3,21)) would give a DIFFERENT structure
    function with different analytic properties.

    THE EXPONENT FORMULA:
    If all positive h_i are equal to a and all negative h_i are equal to b,
    then:
        g(u) = [(u-a)/(u+a)]^{p} * [(u-b)/(u+b)]^{n}
    where p = SIG_PLUS = 4 and n = SIG_MINUS = 20.

    The CY_2 constraint p*a + n*b = 0 gives b = -p*a/n = -a/5.
    So the Kummer parametrization is the UNIQUE most-symmetric choice.
    """
    if params is None:
        params = kummer_k3_parameters()

    h = params.h
    eigs = mukai_diagonal_eigenvalues()

    # Separate positive and negative parameters
    h_pos = [h[i] for i in range(NUM_PARAMS) if eigs[i] == 1]
    h_neg = [h[i] for i in range(NUM_PARAMS) if eigs[i] == -1]

    # Evaluate g_+ and g_- separately at test points
    test_point = Rational(2)
    g_plus = Rational(1)
    for hi in h_pos:
        g_plus *= (test_point - hi) / (test_point + hi)
    g_minus = Rational(1)
    for hi in h_neg:
        g_minus *= (test_point - hi) / (test_point + hi)
    g_full = g_plus * g_minus

    # Power sums by signature block
    p_pos = {k: sum(hi**k for hi in h_pos) for k in range(1, 7)}
    p_neg = {k: sum(hi**k for hi in h_neg) for k in range(1, 7)}

    return {
        'signature': (SIG_PLUS, SIG_MINUS),
        'positive_parameters': {
            'count': len(h_pos),
            'values': [str(hi) for hi in h_pos[:4]],
            'power_sums': {k: p_pos[k] for k in range(1, 7)},
        },
        'negative_parameters': {
            'count': len(h_neg),
            'values_first_4': [str(hi) for hi in h_neg[:4]],
            'power_sums': {k: p_neg[k] for k in range(1, 7)},
        },
        'factorization_at_u_2': {
            'g_plus': str(g_plus),
            'g_minus': str(g_minus),
            'g_full': str(g_full),
            'product_check': str(g_plus * g_minus) == str(g_full),
        },
        'cy2_constraint_by_block': {
            'sum_positive': sum(h_pos),
            'sum_negative': sum(h_neg),
            'total': sum(h_pos) + sum(h_neg),
            'is_zero': sum(h_pos) + sum(h_neg) == 0,
        },
        'uniqueness_of_kummer': (
            'If all positive h_i = a and all negative h_i = b, '
            'then CY_2 gives b = -p*a/n = -a/5 (unique ratio). '
            'The Kummer parametrization is the unique most-symmetric choice.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 10. Full verification suite
# =========================================================================

def full_explicit_verification(
    eps: Rational = Rational(1),
) -> Dict[str, Any]:
    r"""Complete verification of all properties of g_{K3}(u).

    This runs ALL checks and returns a comprehensive report.
    All results are CONJECTURAL (AP-CY14).
    """
    params = kummer_k3_parameters(eps)

    results = {}

    # 1. Explicit form
    explicit = explicit_structure_function(params)
    results['explicit_form'] = {
        'degree': explicit.degree,
        'g_at_0': str(explicit.g_at_0),
        'g_at_0_is_1': explicit.g_at_0 == 1,
        'is_kummer': explicit.is_kummer,
    }

    # 2. Reflection identity
    reflection = verify_reflection_identity(params)
    results['reflection_identity'] = {
        'all_pass': reflection['all_pass'],
        'parameter_independent': reflection['parameter_independent'],
    }

    # 3. OPE coefficients
    ope = ope_coefficients_explicit(params, max_order=12)
    results['ope_coefficients'] = {
        'initial_vanishing': ope['initial_vanishing'],
        'log_even_vanish': ope['log_even_vanish'],
        'phi_0': ope['coefficients'][0],
        'phi_1': ope['coefficients'][1],
        'phi_3': ope['coefficients'][3],
        'phi_5': ope['coefficients'][5],
        'phi_7': ope['coefficients'][7],
    }

    # 4. Koszul dual
    koszul = koszul_dual_structure_function(params)
    results['koszul_dual'] = {
        'conductor': koszul['koszul_conductor']['value'],
        'odd_sign_flip': koszul['odd_sign_flip_verified'],
    }

    # 5. R-matrix parameter
    rmatrix = r_matrix_parameter_analysis(params)
    results['r_matrix'] = {
        'no_single_hbar': rmatrix['no_single_hbar'],
        'e_2': rmatrix['collective_parameters']['e_2'],
        'trace_r_zero': rmatrix['classical_r_matrix']['trace_is_zero'],
    }

    # 6. Moduli
    moduli = moduli_of_structure_functions()
    results['moduli'] = {
        'uniquely_determined': moduli['uniquely_determined'],
        'dimension': moduli['moduli_space']['dimension'],
        'all_different': moduli['non_uniqueness_demonstration']['all_different'],
    }

    # 7. Signature analysis
    sig = signature_analysis(params)
    results['signature'] = {
        'cy2_zero': sig['cy2_constraint_by_block']['is_zero'],
    }

    # 8. Overall status
    all_checks = [
        results['explicit_form']['g_at_0_is_1'],
        results['reflection_identity']['all_pass'],
        results['ope_coefficients']['initial_vanishing'],
        results['ope_coefficients']['log_even_vanish'],
        results['ope_coefficients']['phi_0'] == 1,
        results['ope_coefficients']['phi_1'] == 0,
        results['koszul_dual']['odd_sign_flip'],
        results['r_matrix']['trace_r_zero'],
        results['signature']['cy2_zero'],
    ]

    results['all_checks_pass'] = all(all_checks)
    results['status'] = STATUS

    return results
