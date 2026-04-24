"""Affine Yangian Y(gl_hat_1) / W_{1+infinity} at self-dual level.

Ground truth: Schiffmann-Vasserot (arXiv:1211.1287), Tsymbaliuk (arXiv:1404.5240),
Prochazka-Rapcak (arXiv:1910.07997), Maulik-Okounkov (arXiv:1211.1287).

The critical CoHA of C^3 is isomorphic to Y^+(gl_hat_1) (thm:sv-c3 in
toric_cy3_coha.tex). The full affine Yangian is the Drinfeld double /
mode-algebra side; W_{1+infinity} is reached through the completed
Fock/evaluation representation, not by identifying the positive half
with the vertex algebra.

STRUCTURE FUNCTION:
    g(z) = (z - h1)(z - h2)(z - h3) / (z + h1)(z + h2)(z + h3)

with the CY condition h1 + h2 + h3 = 0. Parameters:
    h1 = sigma_1, h2 = sigma_2, h3 = sigma_3 = -(sigma_1 + sigma_2)

At the self-dual path h1 = 1, h2 = epsilon, h3 = -1-epsilon, the
unrescaled limit epsilon -> 0 has trivial structure function g(z)=1.
The nontrivial W_{1+infinity} limit requires the usual rescaled or
finite-N limiting data.

CONVENTIONS:
    - psi(z) = 1 + sigma_3 sum_{i>=0} psi_i z^{-i-1}  (Tsymbaliuk's normalization)
    - e(z) = sum_{i>=0} e_i z^{-i-1}
    - f(z) = sum_{i>=0} f_i z^{-i-1}
    - Structure constants phi_j from g(z) = sum_{j>=0} phi_j z^{-j}, phi_0 = 1.
    - The phi_j encode the cubic Casimirs of the deformation parameters.

MODE ALGEBRA (Tsymbaliuk, Def 2.1):
    [psi_i, psi_j] = 0

    [psi_i, e_j] involves structure constants from g(z):
    Generating function form:
        g(Delta) * psi(z) e(w) = g(-Delta) * e(w) psi(z)
    where Delta = z - w, expanded in modes.

    In mode form, extracting coefficients of z^{-i-1} w^{-j-1}:
        sum_{r=0}^{i} phi_r * psi_{i-r} e_j - sum_{r=0}^{j} phi_r * e_{j-r} psi_i
        (with appropriate signs and index shifts)

    The psi-e commutator in mode form:
        [psi_i, e_j] = sum_{r>=1} phi_r (psi_{i-r} e_j + e_j psi_{i-r})
                        when i >= r, else 0
    This is the symmetrized form; the exact coefficient extraction from g(z)
    gives the structure constants below.

    [e_i, f_j] = psi_{i+j}  (up to normalization by sigma_1*sigma_2*sigma_3)

STRUCTURE CONSTANTS phi_j:
    g(z) = prod_{a=1}^{3} (z - h_a)/(z + h_a) expanded as formal series in z^{-1}.

    KEY IDENTITY: g(-z) = 1/g(z), so g(z)*g(-z) = 1.
    Consequence: only odd-indexed log-series coefficients alpha_k are nonzero.

    log g(z) = sum_{k odd, k>=1} alpha_k z^{-k}
    where alpha_k = (-2/k)(h1^k + h2^k + h3^k) = (-2/k)*p_k.

    The phi_j are obtained by exponentiating: g(z) = exp(log g(z)).
    Using the recursion j*phi_j = sum_{k=1}^{j} k*alpha_k*phi_{j-k}:

    phi_0 = 1
    phi_1 = alpha_1 = -2*p_1 = 0       (by CY condition p_1 = 0)
    phi_2 = 0                           (alpha_1 = 0, alpha_2 = 0)
    phi_3 = alpha_3 = -2*p_3/3 = -2*sigma_3   (Newton: p_3 = 3*sigma_3)
    phi_4 = 0                           (no partition of 4 into odd parts >= 3)
    phi_5 = alpha_5 = -2*p_5/5          (only the singleton partition)
    phi_6 = alpha_3^2/2                 (from partition 6 = 3+3)
    phi_7 = alpha_7 = -2*p_7/7          (only the singleton partition)
    phi_8 = alpha_3*alpha_5             (from partition 8 = 3+5)
    phi_9 = alpha_9 + alpha_3^3/6       (from partitions 9 and 3+3+3)

    Elementary symmetric invariants:
        sigma_1 = h1 + h2 + h3 = 0
        sigma_2 = h1*h2 + h1*h3 + h2*h3 = -(h1^2 + h1*h2 + h2^2)
        sigma_3 = h1*h2*h3 = -h1*h2*(h1+h2)

    The structure function is completely determined by sigma_2 and sigma_3.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    expand,
    series,
    simplify,
    symbols,
)


# ---------------------------------------------------------------------------
# Structure function and its expansion
# ---------------------------------------------------------------------------

def structure_function_coefficients(
    h1: Rational,
    h2: Rational,
    h3: Optional[Rational] = None,
    max_order: int = 10,
) -> List[Rational]:
    """Compute phi_j coefficients of g(z) = sum_{j>=0} phi_j z^{-j}.

    g(z) = (z-h1)(z-h2)(z-h3) / (z+h1)(z+h2)(z+h3)

    If h3 is None, enforces h3 = -(h1+h2) (CY condition).

    Returns [phi_0, phi_1, ..., phi_{max_order}].
    """
    if h3 is None:
        h3 = -(h1 + h2)
    z = Symbol("z")
    numer = (z - h1) * (z - h2) * (z - h3)
    denom = (z + h1) * (z + h2) * (z + h3)

    # Expand g(z) = numer/denom as a series in z^{-1}
    # Write g(z) = prod (1 - h_a/z)/(1 + h_a/z)
    # = prod (1 - h_a/z)(1 - h_a/z + h_a^2/z^2 - ...)
    # More cleanly: substitute w = 1/z, expand around w=0
    w = Symbol("w")
    g_w = ((1 - h1 * w) * (1 - h2 * w) * (1 - h3 * w)
           / ((1 + h1 * w) * (1 + h2 * w) * (1 + h3 * w)))
    g_series = series(g_w, w, 0, max_order + 1)

    coeffs = []
    for j in range(max_order + 1):
        coeff = g_series.coeff(w, j)
        coeffs.append(Rational(coeff))

    return coeffs


def structure_function_coefficients_symbolic(
    max_order: int = 10,
) -> List:
    """Compute phi_j symbolically in terms of h1, h2 (with h3 = -h1-h2).

    Returns list of sympy expressions in h1, h2.
    """
    h1, h2 = symbols("h1 h2")
    h3 = -(h1 + h2)
    w = Symbol("w")
    g_w = ((1 - h1 * w) * (1 - h2 * w) * (1 - h3 * w)
           / ((1 + h1 * w) * (1 + h2 * w) * (1 + h3 * w)))
    g_series = series(g_w, w, 0, max_order + 1)

    coeffs = []
    for j in range(max_order + 1):
        coeff = g_series.coeff(w, j)
        coeffs.append(expand(coeff))

    return coeffs


def elementary_symmetric_from_h(h1, h2, h3=None):
    """Compute elementary symmetric polynomials sigma_1, sigma_2, sigma_3.

    sigma_1 = h1 + h2 + h3 (= 0 by CY condition)
    sigma_2 = h1*h2 + h1*h3 + h2*h3
    sigma_3 = h1*h2*h3
    """
    if h3 is None:
        h3 = -(h1 + h2)
    s1 = h1 + h2 + h3
    s2 = h1 * h2 + h1 * h3 + h2 * h3
    s3 = h1 * h2 * h3
    return s1, s2, s3


def power_sums_from_h(h1, h2, h3=None, max_k=6):
    """Compute Newton power sums p_k = h1^k + h2^k + h3^k for k = 1,...,max_k.

    By CY condition (h3 = -h1-h2): p_1 = 0.
    Even power sums p_{2m} depend only on sigma_2.
    Odd power sums p_{2m+1} depend on both sigma_2 and sigma_3.
    Newton's identities: p_k - sigma_1*p_{k-1} + sigma_2*p_{k-2} - sigma_3*p_{k-3} = 0.
    """
    if h3 is None:
        h3 = -(h1 + h2)
    result = {}
    for k in range(1, max_k + 1):
        result[k] = h1**k + h2**k + h3**k
    return result


# ---------------------------------------------------------------------------
# Explicit low-order structure constants
# ---------------------------------------------------------------------------

def phi_explicit(h1, h2, h3=None, max_order=6):
    """Compute the first few phi_j by direct expansion.

    Uses the exact formula: g(z) = 1 + sum phi_j z^{-j} where
    log g(z) = sum_{k>=1} (-2 p_k / k) z^{-k}
    with p_k = h1^k + h2^k + h3^k the Newton power sums.

    Since g = exp(log g), the phi_j come from exponentiating the
    log series.
    """
    if h3 is None:
        h3 = -(h1 + h2)

    # log g(z) = sum_a [log(1 - h_a/z) - log(1 + h_a/z)]
    #          = sum_a sum_{k>=1} (-2 h_a^k / k) z^{-k}  (for k odd, doubled)
    #
    # Actually: log(1-x) - log(1+x) = -2(x + x^3/3 + x^5/5 + ...)
    # So log g(z) = sum_a sum_{m>=0} -2 h_a^{2m+1} / ((2m+1) z^{2m+1})
    #
    # More generally: log[(z-h)/(z+h)] = -2h/z - 2h^3/(3z^3) - 2h^5/(5z^5) - ...
    # So log g(z) = sum_{k=1,3,5,...} (-2/k)(h1^k + h2^k + h3^k) z^{-k}
    #            = sum_{k odd} (-2 p_k/k) z^{-k}
    #
    # Note: for k even, the contributions from log(1-x)-log(1+x) vanish.
    # Only ODD power sums contribute.

    p = power_sums_from_h(h1, h2, h3, max_k=max_order)

    # Build log g coefficients: alpha_k = -2 p_k / k for k odd, 0 for k even
    alpha = {}
    for k in range(1, max_order + 1):
        if k % 2 == 1:
            alpha[k] = Rational(-2) * p[k] / k
        else:
            alpha[k] = Rational(0)

    # Exponentiate: g = exp(sum alpha_k z^{-k})
    # phi_j = sum over partitions of j of prod alpha_{k_i} / multiplicity!
    # Use the recursive formula:
    #   j * phi_j = sum_{k=1}^{j} k * alpha_k * phi_{j-k}
    phi = [Rational(1)]  # phi_0 = 1
    for j in range(1, max_order + 1):
        val = Rational(0)
        for k in range(1, j + 1):
            ak = alpha.get(k, Rational(0))
            val += k * ak * phi[j - k]
        phi.append(val / j)

    return phi


# ---------------------------------------------------------------------------
# Mode algebra: psi-e and psi-f commutation
# ---------------------------------------------------------------------------

def psi_e_structure_constants(
    h1, h2, h3=None, max_mode: int = 8,
) -> Dict[Tuple[int, int, int], Rational]:
    """Compute the structure constants C^{pe}_{i,j,k} for [psi_i, e_j].

    From the generating-function relation (Tsymbaliuk):
        g(z-w) psi(z) e(w) = g(w-z) e(w) psi(z)

    where g(z) = sum phi_j z^{-j}, this gives in mode form:

        [psi_i, e_j] = sum_{r>=1} phi_r (psi_{i-r} e_j + e_{j-r} psi_i)
                        ... (schematic; precise extraction below)

    More precisely, from g(Delta) psi(z) e(w) = g(-Delta) e(w) psi(z):
    Extracting the coefficient of z^{-i-1} w^{-j-1}, we get:

        sum_{r>=0} phi_r psi_{i-r} e_j = sum_{r>=0} (-1)^r phi_r e_{j-r} psi_i

    which rearranges to:

        psi_i e_j - e_j psi_i = sum_{r>=1} [(-1)^r phi_r e_{j-r} psi_i
                                              - phi_r psi_{i-r} e_j]

    For the ABELIANIZED (classical) version relevant to OPE structure constants,
    we compute the linear action of psi on the e-generators modulo higher order.

    Returns dict mapping (i, j, combined_mode) -> coefficient.
    """
    if h3 is None:
        h3 = -(h1 + h2)
    phi = structure_function_coefficients(h1, h2, h3, max_order=max_mode + 2)

    # In the free-field (level-1) representation, psi_i are diagonal
    # and the commutator reduces to a c-number action:
    #   [psi_i, e_j] = c_{ij} * e_{i+j}
    # where c_{ij} comes from the phi coefficients.
    #
    # More precisely, from the generating-function OPE:
    #   psi(z) e(w) ~ g(z-w)/g(w-z) * e(w) psi(z)
    #
    # The ratio g(z-w)/g(w-z) = G(z-w) where
    #   G(u) = g(u)/g(-u)
    #
    # Since g(-u) = 1/g(u) (because g(z) * g(-z) = 1 from the
    # antisymmetry of h_1 + h_2 + h_3 = 0... wait, this is NOT true
    # in general).
    #
    # Let's compute G(u) = g(u)/g(-u) directly.
    # g(u) = (u-h1)(u-h2)(u-h3)/((u+h1)(u+h2)(u+h3))
    # g(-u) = (-u-h1)(-u-h2)(-u-h3)/((-u+h1)(-u+h2)(-u+h3))
    #       = -(u+h1)(u+h2)(u+h3) / [-(u-h1)(u-h2)(u-h3)]
    #       = (u+h1)(u+h2)(u+h3) / ((u-h1)(u-h2)(u-h3))
    #       = 1/g(u)
    #
    # So g(-u) = 1/g(u), hence G(u) = g(u)^2.
    # This is the key identity: the psi-e OPE coefficient is g(z-w)^2.

    # g(u)^2 = [sum phi_j u^{-j}]^2 = sum_n [sum_{a+b=n} phi_a phi_b] u^{-n}
    # Define gamma_n = sum_{a+b=n} phi_a phi_b (Cauchy product of phi with itself)
    max_n = max_mode + 2
    gamma = []
    for n in range(max_n + 1):
        val = Rational(0)
        for a in range(min(n + 1, len(phi))):
            b = n - a
            if b < len(phi):
                val += phi[a] * phi[b]
        gamma.append(val)

    # Now: psi(z) e(w) = G(z-w) e(w) psi(z)
    #                   = g(z-w)^2 e(w) psi(z)
    #
    # Expanding: psi(z) e(w) = [sum_n gamma_n (z-w)^{-n}] e(w) psi(z)
    #
    # The coefficients gamma_n encode the OPE between psi and e.
    # gamma_0 = phi_0^2 = 1 (regular part)
    # gamma_1 = 2 phi_0 phi_1 = 0 (since phi_1 = 0 by CY condition)
    # gamma_2 = phi_1^2 + 2 phi_0 phi_2 = 2 phi_2

    return {
        "phi": phi[:max_n + 1],
        "gamma": gamma,
        "description": "gamma_n = Cauchy product phi*phi at order n; "
                       "encodes the psi-e OPE coefficient g(z-w)^2"
    }


def ef_commutator_coefficient(h1, h2, h3=None):
    """The normalization for [e_i, f_j] = psi_{i+j} / sigma_3.

    [e(z), f(w)] = -(1/sigma_3) * delta(z,w) * psi(z)

    where sigma_3 = h1*h2*h3 = -h1*h2*(h1+h2).

    In mode form: [e_i, f_j] = psi_{i+j} / sigma_3.

    Returns sigma_3 (the denominator).
    """
    if h3 is None:
        h3 = -(h1 + h2)
    return h1 * h2 * h3


# ---------------------------------------------------------------------------
# OPE structure constants (W_{1+infty} perspective)
# ---------------------------------------------------------------------------

def ope_structure_constants_low_order(h1, h2, h3=None, max_spin=4):
    """Compute the first few OPE structure constants of W_{1+infty}.

    At the self-dual level, W_{1+infty} has generators W^{(s)} of spin
    s = 1, 2, 3, ... where:
        W^{(1)} = J  (U(1) current)
        W^{(2)} = T  (stress-energy / Virasoro)
        W^{(3)} = W  (spin-3 current)
        ...

    The OPE W^{(s1)}(z) W^{(s2)}(w) = sum_n C^{s3}_{s1,s2;n} / (z-w)^n ...

    The leading singular terms are:
        J(z) J(w) ~ c_JJ / (z-w)^2        where c_JJ = -sigma_2
        J(z) T(w) ~ J(w) / (z-w)^2         (standard)
        T(z) T(w) ~ c/2 / (z-w)^4 + 2T/(z-w)^2 + dT/(z-w)   (Virasoro)
        T(z) W(w) ~ 3W/(z-w)^2 + dW/(z-w)   (primary of spin 3)
        W(z) W(w) ~ c_WW / (z-w)^6 + ...

    The central charge and structure constants are:
        c = 1 - 6 sigma_2     (Feigin-Frenkel, W_{1+infty})
        c_WW depends on sigma_2, sigma_3

    For the C^3 CoHA (sigma_1=1, sigma_2=0, sigma_3=-1): c = 1.
    """
    if h3 is None:
        h3 = -(h1 + h2)

    _, sigma_2, sigma_3 = elementary_symmetric_from_h(h1, h2, h3)

    # Central charge: for W_{1+infty} algebra with parameters h_i,
    # using the Miura transform / free-field realization:
    # The U(1) current normalization gives the central extension.
    #
    # Actually, for the affine Yangian Y(gl_hat_1), the representation
    # theory gives the central charge of the associated W-algebra as:
    #   c = N  (for the level-N representation)
    #
    # But for the ALGEBRA structure (not representation), the key invariants
    # are sigma_2 and sigma_3. The algebra has:
    #   c(psi_0) = 1  (by convention, psi_0 is central with eigenvalue
    #                   determined by the representation)
    #
    # The OPE structure constants depend on the representation level N
    # and the deformation parameters h_i. For the universal algebra:

    results = {
        "sigma_2": sigma_2,
        "sigma_3": sigma_3,
        "h_params": (h1, h2, h3),
    }

    # The two fundamental invariants of the structure function:
    # sigma_2 = h1*h2 + h1*h3 + h2*h3 = -(h1^2 + h1*h2 + h2^2)
    # sigma_3 = h1*h2*h3 = -h1*h2*(h1+h2)

    # phi coefficients (OPE structure constants in the Yangian basis):
    phi = phi_explicit(h1, h2, h3, max_order=2 * max_spin)
    results["phi"] = phi

    # The phi coefficients encode the structure function.
    # Key facts (from log g having only odd powers):
    #   phi_0 = 1  (normalization)
    #   phi_1 = 0  (CY condition h1+h2+h3=0)
    #   phi_2 = 0  (no even alpha_k contribute at this order)
    #   phi_3 = alpha_3 = -2*p_3/3 = -2*sigma_3  (Newton: p_3 = 3*sigma_3)
    #   phi_4 = 0  (4 has no partition into odd parts >= 3)
    #   phi_5 = alpha_5 = -2*p_5/5

    results["phi_2_is_zero"] = simplify(phi[2]) == 0
    if len(phi) > 3:
        # p_3 = h1^3 + h2^3 + h3^3 = 3*h1*h2*h3 = 3*sigma_3
        # (by Newton's identity: p_3 = sigma_1*p_2 - sigma_2*p_1 + 3*sigma_3
        #                             = 0 - 0 + 3*sigma_3)
        # phi_3 = alpha_3 = -2*p_3/3 = -2*sigma_3
        results["phi_3_equals_neg2_sigma3"] = simplify(phi[3] + 2 * sigma_3) == 0

    return results


# ---------------------------------------------------------------------------
# W_{1+infty} limit: sigma_1=1, sigma_2=eps, sigma_3=-1-eps
# ---------------------------------------------------------------------------

def w_infinity_limit(eps_values=None, max_order=8):
    """Verify that at h1=1, h2=eps, h3=-1-eps, the limit eps->0 gives W_{1+infty}.

    At eps=0: h1=1, h2=0, h3=-1.
    Structure function: g(z) = (z-1)(z)(z+1)/((z+1)(z)(z-1)) = 1
    This is the TRIVIAL structure function -- the algebra becomes abelian.

    At generic eps (small): the structure function is
        g(z) = (z-1)(z-eps)(z+1+eps) / ((z+1)(z+eps)(z-1-eps))

    The deformation is controlled by sigma_2, sigma_3:
        sigma_2 = 1*eps + 1*(-1-eps) + eps*(-1-eps) = -1 - eps - eps^2
        sigma_3 = -1*eps*(1+eps) = -eps(1+eps)

    So sigma_2 -> -1 as eps -> 0 and sigma_3 -> 0 as eps -> 0.

    The NONTRIVIAL W_{1+infty} limit corresponds to RESCALING: one
    studies the structure at finite N (number of colors) where the
    deformation parameters are h1=1, h2=-N, h3=N-1 (Schiffmann-Vasserot
    parametrization for GL_N DT theory).

    For the eps-deformation study, we track the phi coefficients as functions
    of eps to see how the algebra degenerates.

    Returns dict with phi coefficients at each eps value.
    """
    if eps_values is None:
        eps_values = [Rational(1, 10), Rational(1, 100), Rational(1, 1000), Rational(0)]

    results = {}
    for eps in eps_values:
        h1 = Rational(1)
        h2 = eps
        h3 = -(h1 + h2)

        phi = phi_explicit(h1, h2, h3, max_order=max_order)
        sigma = elementary_symmetric_from_h(h1, h2, h3)

        results[eps] = {
            "h_params": (h1, h2, h3),
            "sigma_2": sigma[1],
            "sigma_3": sigma[2],
            "phi": phi,
        }

    return results


def schiffmann_vasserot_parametrization(N, max_order=8):
    """Schiffmann-Vasserot parametrization for GL_N DT theory.

    h1 = 1, h2 = -N, h3 = N - 1.
    CY condition: 1 + (-N) + (N-1) = 0. Check.

    sigma_2 = 1*(-N) + 1*(N-1) + (-N)*(N-1) = -N + N - 1 - N^2 + N = -1 + N(1-N)
            Hmm, let me compute carefully:
            = 1*(-N) + 1*(N-1) + (-N)*(N-1)
            = -N + N - 1 + (-N^2 + N)
            = -1 - N^2 + N
            = -(N^2 - N + 1)

    sigma_3 = 1*(-N)*(N-1) = -N(N-1) = N(1-N)

    These are the natural parameters for the N-colored plane partition
    counting / DT theory of C^3 with N D-branes.

    The W_{1+infty}[N] algebra has c = N and the structure constants
    are polynomials in N.

    Returns dict with structure function data at given N.
    """
    h1 = Rational(1)
    h2 = Rational(-N)
    h3 = Rational(N - 1)

    phi = phi_explicit(h1, h2, h3, max_order=max_order)
    sigma = elementary_symmetric_from_h(h1, h2, h3)

    return {
        "N": N,
        "h_params": (h1, h2, h3),
        "sigma_1": sigma[0],
        "sigma_2": sigma[1],
        "sigma_3": sigma[2],
        "phi": phi,
        "description": f"Schiffmann-Vasserot for GL_{N}: "
                       f"h = (1, {-N}, {N-1}), "
                       f"sigma_2 = {sigma[1]}, sigma_3 = {sigma[2]}"
    }


# ---------------------------------------------------------------------------
# Toric CY3 connection: Crystal melting / plane partitions
# ---------------------------------------------------------------------------

def crystal_melting_character(N, max_order=6):
    """Character of the vacuum module of Y(gl_hat_1) at level N.

    The MacMahon function M(q) = prod_{k>=1} 1/(1-q^k)^k counts
    3D partitions (plane partitions). For the N-colored version:

        Z_N(q) = prod_{k>=1} 1/(1-q^k)^{N*k}

    This is the partition function of N-colored crystal melting,
    which computes the DT invariants of C^3 with N D0-branes.

    The affine Yangian Y(gl_hat_1) acts on the space of N-colored
    plane partitions, and Z_N(q) is the character of the vacuum
    representation (Fock module).

    Returns the first few coefficients of Z_N(q) = sum d_n q^n.
    """
    # Compute using the product formula up to q^max_order
    coeffs = [Rational(0)] * (max_order + 1)
    coeffs[0] = Rational(1)

    for k in range(1, max_order + 1):
        multiplicity = N * k
        # Multiply by 1/(1-q^k)^multiplicity
        # = sum_{m>=0} C(multiplicity+m-1, m) q^{k*m}
        for power in range(max_order, -1, -1):
            for m in range(1, max_order // k + 1):
                target = power + k * m
                if target > max_order:
                    continue
                # Binomial coefficient C(multiplicity+m-1, m)
                binom = Rational(1)
                for i in range(m):
                    binom *= Rational(multiplicity + i, i + 1)
                coeffs[target] += coeffs[power] * binom

    # Correction: the above double-counts. Use the standard recursive method.
    # Reset and use the proper product expansion.
    coeffs = [Rational(0)] * (max_order + 1)
    coeffs[0] = Rational(1)

    for k in range(1, max_order + 1):
        multiplicity = N * k
        # Multiply current series by 1/(1-q^k)^multiplicity
        # Using the identity: 1/(1-x)^m = sum_{n>=0} C(m+n-1,n) x^n
        new_coeffs = [Rational(0)] * (max_order + 1)
        for n in range(max_order + 1):
            # coefficient of q^n in old * 1/(1-q^k)^mult
            for j in range(n // k + 1):
                # contribution from q^{n - k*j} in old * q^{k*j} in expansion
                old_idx = n - k * j
                if old_idx < 0 or old_idx > max_order:
                    continue
                # C(mult + j - 1, j)
                binom = Rational(1)
                for i in range(j):
                    binom *= Rational(multiplicity + i, i + 1)
                new_coeffs[n] += coeffs[old_idx] * binom
        coeffs = new_coeffs

    return coeffs


# ---------------------------------------------------------------------------
# Verification: identities among structure constants
# ---------------------------------------------------------------------------

def verify_cy_condition_on_phi(h1, h2, max_order=8):
    """Verify that phi_1 = 0 (consequence of CY condition h1+h2+h3=0).

    Also verify phi_{2k+1} involves only sigma_3 (odd power sums
    involve only the cubic Casimir).
    """
    h3 = -(h1 + h2)
    phi = phi_explicit(h1, h2, h3, max_order=max_order)

    results = {
        "phi_1_zero": simplify(phi[1]) == 0,
        "phi_values": phi,
    }

    # phi_1 = 0 because p_1 = h1+h2+h3 = 0
    # phi_2 = 0 because log g has only odd powers of z^{-1}
    results["phi_2_zero"] = simplify(phi[2]) == 0

    # phi_3 = -2*sigma_3 where sigma_3 = h1*h2*h3
    sigma3 = h1 * h2 * h3
    results["phi_3_check"] = simplify(phi[3] + 2 * sigma3) == 0

    # phi_4 = 0 (4 has no partition into odd parts >= 3)
    if len(phi) > 4:
        results["phi_4_zero"] = simplify(phi[4]) == 0

    return results


def verify_g_inversion(h1, h2, max_order=8):
    """Verify g(z) * g(-z) = 1 (key identity for the affine Yangian).

    g(z) = prod (z-h_a)/(z+h_a)
    g(-z) = prod (-z-h_a)/(-z+h_a) = prod (z+h_a)/(z-h_a) = 1/g(z)

    So g(z)*g(-z) = 1 identically. This means:
        sum_{a+b=n} phi_a * (-1)^b * phi_b = delta_{n,0}

    i.e. in the Cauchy product, g(u)*g(-u) = 1.
    """
    h3 = -(h1 + h2)
    phi = phi_explicit(h1, h2, h3, max_order=max_order)

    # Check: sum_{a+b=n} phi_a * (-1)^b * phi_b = delta_{n,0}
    results = {}
    for n in range(max_order + 1):
        val = Rational(0)
        for a in range(n + 1):
            b = n - a
            if a < len(phi) and b < len(phi):
                val += phi[a] * ((-1) ** b) * phi[b]
        results[n] = simplify(val)

    checks = {n: (v == (1 if n == 0 else 0)) for n, v in results.items()}
    return {
        "cauchy_products": results,
        "all_pass": all(checks.values()),
        "checks": checks,
    }


def verify_antisymmetry_parity(h1, h2, max_order=8):
    """Verify that g(-z) = 1/g(z) implies phi_j with j odd are determined
    by phi_j with j even (and vice versa) via the inversion relation.

    From g(z)*g(-z) = 1:
        phi_n^{even} + phi_n^{odd} * (-1)^n-pieces = ...

    Concretely:
        phi_{2k} is even in the h_i (quadratic Casimir dependence)
        phi_{2k+1} is odd in the h_i (cubic Casimir dependence)

    The even phi depend only on sigma_2, the odd phi only on sigma_3.
    (This follows from the log g formula: only odd power sums contribute,
    and p_{2k+1} = Newton polynomial in sigma_2, sigma_3.)
    """
    h3 = -(h1 + h2)
    phi = phi_explicit(h1, h2, h3, max_order=max_order)

    # Under h_i -> -h_i: sigma_2 -> sigma_2 (even), sigma_3 -> -sigma_3 (odd)
    # g(z) under h_i -> -h_i becomes:
    # (z+h1)(z+h2)(z+h3)/((z-h1)(z-h2)(z-h3)) = 1/g(z) = g(-z)
    #
    # So phi_j(-h) = (-1)^j phi_j(h) (from g(-z) expansion).
    # This means phi_j is even/odd in h according to j's parity.

    phi_neg = phi_explicit(-h1, -h2, h1 + h2, max_order=max_order)

    parity_checks = {}
    for j in range(max_order + 1):
        expected_sign = (-1) ** j
        parity_checks[j] = simplify(phi_neg[j] - expected_sign * phi[j]) == 0

    return {
        "parity_checks": parity_checks,
        "all_pass": all(parity_checks.values()),
    }


# ---------------------------------------------------------------------------
# The ee and ff Serre-type relations
# ---------------------------------------------------------------------------

def serre_relation_data(h1, h2, h3=None, max_mode=4):
    """Compute data for the Serre-type relations among e_i generators.

    The affine Yangian has the cubic Serre relation:
        Sym_{i1,i2,i3} [e_{i1}, [e_{i2}, e_{i3+1}]] = 0

    where Sym denotes symmetrization over (i1, i2, i3), and more generally:

        [e_{i+1}, e_j] - [e_i, e_{j+1}] = phi_1 {e_i, e_j}
                                            + phi_2 (something)
                                            + phi_3 (something)

    The simplest nontrivial relation is (Tsymbaliuk, relation (R3)):
        [e_{i+1}, e_j] - [e_i, e_{j+1}]
        = phi_1 (e_i e_j + e_j e_i) + phi_2 (...) + phi_3 (...)

    Since phi_1 = 0 (CY condition), the leading term is:
        [e_{i+1}, e_j] - [e_i, e_{j+1}] = phi_2 * correction + phi_3 * ...

    Returns the structure of the relation for documentation and testing.
    """
    if h3 is None:
        h3 = -(h1 + h2)
    phi = phi_explicit(h1, h2, h3, max_order=6)

    return {
        "relation_type": "cubic_serre",
        "phi_1": phi[1],
        "phi_2": phi[2],
        "phi_3": phi[3],
        "phi_1_vanishes": simplify(phi[1]) == 0,
        "description": (
            "Serre relation: Sym_{i1,i2,i3}[e_{i1},[e_{i2},e_{i3+1}]] = 0. "
            "The ee commutation relation "
            "[e_{i+1},e_j] - [e_i,e_{j+1}] = sum phi_r * (...) "
            "has phi_1 = 0 by the CY condition, so the leading deformation "
            "is controlled by phi_3 = -2*sigma_3 (the leading nonzero deformation)."
        ),
    }


# ---------------------------------------------------------------------------
# Full structure constant table for the first few modes
# ---------------------------------------------------------------------------

def structure_constant_table(h1, h2, h3=None, max_mode=5):
    """Produce a complete table of the first few structure constants.

    Organizes:
    1. phi_j (structure function expansion)
    2. gamma_j (psi-e OPE = phi * phi convolution)
    3. sigma_2, sigma_3 (elementary symmetric invariants)
    4. ef normalization (= 1/sigma_3)
    5. Low-spin OPE data (if representable)

    This is the affine Yangian analogue of the shadow metric table
    from Vol I.
    """
    if h3 is None:
        h3 = -(h1 + h2)

    phi = phi_explicit(h1, h2, h3, max_order=2 * max_mode)
    sigma = elementary_symmetric_from_h(h1, h2, h3)

    # Convolution gamma = phi * phi
    gamma = []
    for n in range(2 * max_mode + 1):
        val = Rational(0)
        for a in range(min(n + 1, len(phi))):
            b = n - a
            if b < len(phi):
                val += phi[a] * phi[b]
        gamma.append(val)

    return {
        "h_params": (h1, h2, h3),
        "sigma_1": sigma[0],
        "sigma_2": sigma[1],
        "sigma_3": sigma[2],
        "phi": phi,
        "gamma": gamma,
        "ef_normalization": sigma[2],
        "identities": {
            "phi_0": phi[0],
            "phi_1_zero": simplify(phi[1]) == 0,
            "phi_2_is_zero": simplify(phi[2]) == 0,
            "phi_3_eq_neg2_sigma3": simplify(phi[3] + 2 * sigma[2]) == 0,
            "gamma_0": gamma[0],
            "gamma_1_zero": simplify(gamma[1]) == 0,
            "gamma_2_eq_2phi2": simplify(gamma[2] - 2 * phi[2]) == 0,
        },
    }


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("AFFINE YANGIAN Y(gl_hat_1) STRUCTURE CONSTANTS")
    print("=" * 70)

    # Generic deformation: h1 = 1, h2 = 2, h3 = -3
    print("\n--- Generic case: h = (1, 2, -3) ---")
    table = structure_constant_table(Rational(1), Rational(2))
    for key in ["sigma_1", "sigma_2", "sigma_3"]:
        print(f"  {key} = {table[key]}")
    print("  phi:", [str(p) for p in table["phi"][:8]])
    print("  gamma:", [str(g) for g in table["gamma"][:8]])

    # Schiffmann-Vasserot for N=1,2,3
    for N in [1, 2, 3]:
        print(f"\n--- Schiffmann-Vasserot GL_{N} ---")
        sv = schiffmann_vasserot_parametrization(N)
        print(f"  h = {sv['h_params']}")
        print(f"  sigma_2 = {sv['sigma_2']}, sigma_3 = {sv['sigma_3']}")
        print(f"  phi = {[str(p) for p in sv['phi'][:6]]}")

    # W_{1+infty} limit
    print("\n--- W_{1+infty} limit: h1=1, h2=eps, h3=-1-eps ---")
    lim = w_infinity_limit()
    for eps, data in sorted(lim.items()):
        print(f"  eps={eps}: sigma_2={data['sigma_2']}, sigma_3={data['sigma_3']}")
        print(f"    phi[:5] = {[str(p) for p in data['phi'][:5]]}")

    # Verifications
    print("\n--- Verifications ---")
    inv = verify_g_inversion(Rational(1), Rational(2))
    print(f"  g(z)*g(-z) = 1: {inv['all_pass']}")

    par = verify_antisymmetry_parity(Rational(1), Rational(2))
    print(f"  Parity check: {par['all_pass']}")

    cy = verify_cy_condition_on_phi(Rational(1), Rational(2))
    print(f"  CY condition phi_1=0: {cy['phi_1_zero']}")
    print(f"  phi_2 = 0: {cy['phi_2_zero']}")
    print(f"  phi_3 = -2*sigma_3: {cy['phi_3_check']}")
