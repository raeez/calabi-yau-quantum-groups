r"""E1 partition function of W_{1+infty} at generic sigma_3.

THEOREM (E1 Refined MacMahon):

The E1 partition function of W_{1+infty} at the Schiffmann-Vasserot point
h = (1, -(alpha+1), alpha) with h_1 + h_2 + h_3 = 0 is:

    Z^{E1}(q; alpha) = prod_{n >= 1} 1/(1 - q^n)^{mu(n; alpha)}

where the STAIRCASE MULTIPLICITY is:

    mu(n; alpha) = floor((n-1)/alpha) + 1

This is a one-parameter family interpolating between two classical objects:

    alpha = 1:       Z = M(q) = prod 1/(1-q^n)^n    (MacMahon, plane partitions)
    alpha -> infty:  Z = P(q) = prod 1/(1-q^n)       (Euler, ordinary partitions)

PARAMETRIZATION:

    sigma_2 = -(alpha^2 + alpha + 1)
    sigma_3 = -alpha * (alpha + 1)
    kappa   = alpha^2 + alpha + 1

    At alpha = 1: kappa = 3, sigma_3 = -2 (isotropic C^3).
    At alpha -> infty: kappa -> infty, sigma_3 -> -infty.

NEKRASOV IDENTIFICATION:

    Z^{E1}(q; alpha) = Z_Nek(C^3; eps_1 = 1, eps_2 = alpha)

where Z_Nek is the Nekrasov partition function with Omega-background
parameters (eps_1, eps_2).  The ratio alpha = eps_2/eps_1 measures the
anisotropy of the equivariant action on C^3.

DERIVATION:

The refined MacMahon function is M(q, t) = prod_{i>=1, j>=0} 1/(1-q^i t^j).
Specializing t = q^alpha gives:

    M(q, q^alpha) = prod_{i>=1, j>=0} 1/(1 - q^{i + alpha*j})

The exponent i + alpha*j = n has solutions #{(i,j) : i>=1, j>=0, i+alpha*j=n},
which for integer alpha equals floor((n-1)/alpha) + 1.  The product becomes:

    M(q, q^alpha) = prod_{n>=1} 1/(1-q^n)^{mu(n; alpha)}

recovering the staircase multiplicity formula.

THE E1 CORRECTION:

    Delta^{E1}(q; alpha) = Z^{E1}(q; alpha) - M(q)

is negative at every degree >= 2 for alpha >= 2.  The correction STABILIZES:

    lim_{alpha -> infty} Delta^{E1}(q; alpha) = P(q) - M(q)

where P(q) - M(q) = 0, 0, -1, -3, -8, -17, -37, -71, -138, -252, -458, ...

MULTI-PATH VERIFICATION:
    Path 1: Direct product formula with staircase multiplicities
    Path 2: Binomial coefficient method (independent implementation)
    Path 3: Specialization of bigraded M(q,t) at t = q^alpha
    Path 4: Engine cross-check with macmahon_shadow_decomposition
    Path 5: Limiting cases alpha=1 (MacMahon) and alpha->inf (partitions)

CONVENTIONS:
    - q = e^{-beta} with |q| < 1
    - alpha >= 1 integer (extends to real alpha > 0 by analytic continuation)
    - Bernoulli numbers: B_2 = 1/6, B_4 = -1/30
    - MacMahon numbers: OEIS A000219
    - Partition numbers: OEIS A000041

REFERENCES:
    - MacMahon, "Combinatory Analysis" (1916)
    - Iqbal-Kozcaz-Vafa, arXiv:0910.1195 (refined topological vertex)
    - Nekrasov, arXiv:hep-th/0206161 (Omega-background)
    - Schiffmann-Vasserot, arXiv:1211.1287 (elliptic Hall algebra)
    - Okounkov-Reshetikhin-Vafa, hep-th/0309208 (crystal melting)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple


# =========================================================================
# 1. Staircase multiplicity
# =========================================================================

def staircase_multiplicity(n: int, alpha: int) -> int:
    r"""The staircase multiplicity mu(n; alpha) = floor((n-1)/alpha) + 1.

    This counts #{(i,j) : i >= 1, j >= 0, i + alpha*j = n} for integer alpha.

    At alpha=1: mu(n;1) = n.
    At alpha=inf: mu(n;inf) = 1 for all n >= 1.

    Parameters
    ----------
    n : int
        The degree (n >= 1).
    alpha : int
        The anisotropy parameter (alpha >= 1).

    Returns
    -------
    int
        The multiplicity mu(n; alpha).
    """
    if n < 1 or alpha < 1:
        raise ValueError(f"Need n >= 1 and alpha >= 1, got n={n}, alpha={alpha}")
    return (n - 1) // alpha + 1


def staircase_multiplicities(alpha: int, max_n: int) -> List[int]:
    """List of mu(n; alpha) for n = 0, 1, ..., max_n.

    mu(0; alpha) = 0 by convention (no degree-0 generators).
    """
    return [0] + [staircase_multiplicity(n, alpha) for n in range(1, max_n + 1)]


# =========================================================================
# 2. Shadow tower invariants
# =========================================================================

def shadow_invariants(alpha: int) -> Dict[str, object]:
    r"""Shadow tower data at the SV point h = (1, -(alpha+1), alpha).

    Returns
    -------
    dict with keys:
        'alpha': the anisotropy parameter
        'h': tuple (h1, h2, h3) with h1+h2+h3 = 0
        'sigma2': h1*h2 + h1*h3 + h2*h3
        'sigma3': h1*h2*h3 = -alpha*(alpha+1)
        'kappa': -sigma2 = alpha^2 + alpha + 1
        'depth': 'G' if sigma3 = 0, else 'M'
    """
    h1, h2, h3 = 1, -(alpha + 1), alpha
    sigma2 = h1 * h2 + h1 * h3 + h2 * h3
    sigma3 = h1 * h2 * h3
    kappa = -sigma2
    # VERIFIED: sigma2 = -(alpha^2 + alpha + 1), sigma3 = -alpha*(alpha+1)
    # At alpha=1: sigma2=-3, sigma3=-2, kappa=3.  Check.
    # At alpha=2: sigma2=-7, sigma3=-6, kappa=7.  Check.
    return {
        'alpha': alpha,
        'h': (h1, h2, h3),
        'sigma2': sigma2,
        'sigma3': sigma3,
        'kappa': kappa,
        'depth': 'G' if sigma3 == 0 else 'M',
    }


# =========================================================================
# 3. E1 partition function (primary implementation)
# =========================================================================

def e1_partition_function(alpha: int, max_q: int = 25) -> List[int]:
    r"""Z^{E1}(q; alpha) = prod_{n>=1} 1/(1-q^n)^{mu(n;alpha)} mod q^{max_q+1}.

    Primary implementation via in-place cumulative-sum product.
    Multiplying by 1/(1-q^n) = sum_{k>=0} q^{nk} is implemented as:
        for k = n, n+1, ..., max_q:  c[k] += c[k-n]
    (low-to-high traversal).  Repeating mu(n) times gives 1/(1-q^n)^{mu(n)}.

    Parameters
    ----------
    alpha : int
        Anisotropy parameter (>= 1).
    max_q : int
        Compute coefficients mod q^{max_q+1}.

    Returns
    -------
    list of int
        Coefficients [c_0, c_1, ..., c_{max_q}].
    """
    mult = staircase_multiplicities(alpha, max_q)
    c = [Fraction(0)] * (max_q + 1)
    c[0] = Fraction(1)
    for n in range(1, max_q + 1):
        for _ in range(mult[n]):
            for k in range(n, max_q + 1):
                c[k] += c[k - n]
    return [int(c[k]) for k in range(max_q + 1)]


# =========================================================================
# 4. E1 partition function (binomial verification path)
# =========================================================================

def e1_partition_function_binomial(alpha: int, max_q: int = 25) -> List[int]:
    r"""Z^{E1}(q; alpha) via binomial-coefficient product expansion.

    Independent implementation: multiply by
        1/(1-q^n)^m = sum_{k>=0} C(k+m-1, m-1) * q^{nk}
    using the multinomial convolution.

    This is Path 2 of the multi-path verification.
    """
    mult = staircase_multiplicities(alpha, max_q)
    # Polynomial as dict: degree -> Fraction coefficient
    poly: Dict[int, Fraction] = {0: Fraction(1)}
    for n in range(1, max_q + 1):
        m = mult[n]
        if m == 0:
            continue
        new_poly: Dict[int, Fraction] = {}
        for deg_p, coeff_p in poly.items():
            if coeff_p == 0:
                continue
            k = 0
            while True:
                new_deg = deg_p + n * k
                if new_deg > max_q:
                    break
                # C(k + m - 1, m - 1)
                binom = Fraction(1)
                for i in range(m - 1):
                    binom = binom * Fraction(k + m - 1 - i) / Fraction(i + 1)
                new_poly[new_deg] = new_poly.get(new_deg, Fraction(0)) + coeff_p * binom
                k += 1
        poly = new_poly
    return [int(poly.get(k, Fraction(0))) for k in range(max_q + 1)]


# =========================================================================
# 5. Classical limiting cases
# =========================================================================

def macmahon_coefficients(max_q: int = 25) -> List[int]:
    """M(q) = prod 1/(1-q^n)^n (plane partitions, OEIS A000219)."""
    return e1_partition_function(1, max_q)


def partition_coefficients(max_q: int = 25) -> List[int]:
    """P(q) = prod 1/(1-q^n) (ordinary partitions, OEIS A000041)."""
    c = [Fraction(0)] * (max_q + 1)
    c[0] = Fraction(1)
    for n in range(1, max_q + 1):
        for k in range(n, max_q + 1):
            c[k] += c[k - n]
    return [int(c[k]) for k in range(max_q + 1)]


# =========================================================================
# 6. E1 correction
# =========================================================================

def e1_correction(alpha: int, max_q: int = 25) -> List[int]:
    r"""Delta^{E1}(q; alpha) = Z^{E1}(q; alpha) - M(q).

    The E1 correction is negative at every degree >= 2 for alpha >= 2.

    Returns
    -------
    list of int
        Correction coefficients [0, 0, delta_2, delta_3, ...].
    """
    Z = e1_partition_function(alpha, max_q)
    M = macmahon_coefficients(max_q)
    return [Z[k] - M[k] for k in range(max_q + 1)]


def limiting_correction(max_q: int = 25) -> List[int]:
    r"""Delta_infty(q) = P(q) - M(q) = lim_{alpha->infty} Delta^{E1}(q; alpha).

    This is the maximal E1 correction, obtained in the dimensional reduction
    limit C^3 -> C^2 x C.
    """
    P = partition_coefficients(max_q)
    M = macmahon_coefficients(max_q)
    return [P[k] - M[k] for k in range(max_q + 1)]


# =========================================================================
# 7. Bar Euler characteristic
# =========================================================================

def bar_euler_characteristic(alpha: int, max_q: int = 25) -> List[int]:
    r"""chi^{E1}(q; alpha) = 1/Z^{E1}(q; alpha) mod q^{max_q+1}.

    The bar Euler characteristic encodes the alternating sum of bar
    complex dimensions.
    """
    Z = e1_partition_function(alpha, max_q)
    Z_frac = [Fraction(z) for z in Z]
    inv = [Fraction(0)] * (max_q + 1)
    inv[0] = Fraction(1)
    for n in range(1, max_q + 1):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += Z_frac[k] * inv[n - k]
        inv[n] = -s
    return [int(inv[k]) for k in range(max_q + 1)]


# =========================================================================
# 8. Reduction factor
# =========================================================================

def reduction_factor(alpha: int, max_q: int = 20) -> List[Optional[float]]:
    r"""M(q)/Z^{E1}(q; alpha) coefficient-by-coefficient.

    Measures what fraction of plane partitions survive the anisotropic
    weighting at each degree.
    """
    Z = e1_partition_function(alpha, max_q)
    M = macmahon_coefficients(max_q)
    result = []
    for k in range(max_q + 1):
        if Z[k] > 0:
            result.append(float(M[k]) / float(Z[k]))
        else:
            result.append(None)
    return result


# =========================================================================
# 9. Asymptotic analysis
# =========================================================================

def log_Z_numerical(alpha: int, beta: float, max_n: int = 100) -> float:
    r"""Evaluate log Z^{E1}(e^{-beta}; alpha) numerically.

    log Z = sum_{n>=1} mu(n; alpha) * log(1/(1 - e^{-n*beta}))
    """
    import math
    total = 0.0
    for n in range(1, max_n + 1):
        mu = staircase_multiplicity(n, alpha)
        x = math.exp(-n * beta)
        if x > 0.9999999:
            continue
        total += mu * math.log(1.0 / (1.0 - x))
    return total


def total_multiplicity(alpha: int, max_n: int = 30) -> int:
    r"""sum_{n=1}^{max_n} mu(n; alpha).

    At alpha=1: sum = max_n*(max_n+1)/2.
    At alpha=inf: sum = max_n.
    """
    return sum(staircase_multiplicity(n, alpha) for n in range(1, max_n + 1))
