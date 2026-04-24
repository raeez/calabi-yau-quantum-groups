r"""Shadow obstruction tower of W_{1+infinity} at c=1 and the MacMahon connection.

This module computes the shadow obstruction tower of the W_{1+infinity} algebra
at c=1 using the Vol I machinery (shadow_tower_recursive, full_shadow_landscape),
and establishes the precise bridge to the Donaldson-Thomas partition function
Z^{DT}_{C^3} = M(-q) where M(q) = prod_{n>=1} 1/(1-q^n)^n is the MacMahon function.

MATHEMATICAL CONTENT:

W_{1+infinity} at c=1 is the ONE CASE where both sides of the CY3-to-chiral
functor are completely explicit:
  - VOA side: W_{1+inf} = algebra of differential operators on the circle,
    equivalently the limit of W_N principal W-algebras as N -> infinity.
  - DT side: the critical CoHA Y^+(gl_hat_1) (Schiffmann-Vasserot 2013),
    with graded dimension given by the MacMahon function M(q).

CHANNEL DECOMPOSITION:

W_{1+infinity} has generators W_s of spin s = 1, 2, 3, ... (the spin-1
generator is the Heisenberg current, absent from finite W_N for N >= 2).
Each spin-s channel contributes independently at leading order:

  kappa_s = c/s = 1/s    (modular characteristic of spin-s channel)
  Total kappa = sum_{s>=1} 1/s = DIVERGENT (harmonic series)

This divergence is the VOA manifestation of the regularization problem
in DT theory of C^3. The regulated theory uses finite W_N truncation.

SHADOW TOWER PER CHANNEL (at c=1):

  Spin 1 (Heisenberg): kappa=1, alpha=0, S_4=0. Class G (Gaussian).
    Shadow terminates at arity 2: S_2=1/2, S_r=0 for r>=3.

  Spin 2 (Virasoro at c=1): kappa=1/2, alpha=2, S_4=10/27. Class M.
    Infinite tower, rho_T = 6.24, oscillatory.

  Spin s>=3: kappa_s=1/s, alpha_s depends on Z_2 parity.
    Odd s: alpha_s=0 (parity W_s -> -W_s). Even s: alpha_s nonzero.
    Generically class M for all s>=2.

MACMAHON CONNECTION:

  log M(q) = sum_{k>=1} sigma_2(k)/k * q^k

where sigma_2(k) = sum_{d|k} d^2 is the sum-of-squares-of-divisors function.
This identity is PROVED by expanding log(prod (1-q^n)^{-n}).

The channel decomposition gives:
  log M(q) = sum_{n>=1} n * log(1/(1-q^n))
           = sum_{n>=1} n * [contribution from spin-n channel]

The exponent n in (1-q^n)^{-n} means the spin-n factor contributes
RANK n, matching kappa_n = c*n/n = c = 1 for each n... wait, no.
Actually kappa_n = c/n = 1/n, but the n-fold multiplicity in M(q)
means n COPIES of the spin-n channel contribute, giving effective
kappa_n^{eff} = n * (1/n) = 1 per spin level.

This is the SHADOW-DT ROSETTA STONE:
  M(q) = prod_{n>=1} (1/(1-q^n))^n
  Each factor (1/(1-q^n))^n is the partition function of n bosons at energy n.
  The SHADOW tells us: total effective kappa PER ENERGY LEVEL = 1 (constant!).
  The MacMahon function is the partition function of a system where each
  energy level contributes equally to the modular characteristic.

GENUS EXPANSION:

  F_g(W_N, regulated) = kappa(W_N) * lambda_g^FP
  where kappa(W_N) = (H_N - 1) * (N-1) for W_N at c=N-1 (free field).

  As N -> inf, F_g diverges like N*log(N) * lambda_g^FP.
  This divergence maps under the DT correspondence to the non-compactness
  of C^3 (no finite Euler characteristic without framing/regularization).

CONVENTIONS:
  - Cohomological grading (|d|=+1), bar uses desuspension.
  - kappa_s = c/s for spin-s channel (AP1: family-specific formula).
  - The T-line (spin-2) shadow data is identical to Virasoro at same c (AP9).
  - alpha = cubic shadow on primary line. S_4 = quartic contact.
  - Delta = 8*kappa*S_4 (critical discriminant).
  - sigma_2(k) = sum_{d|k} d^2 (sum-of-squares-of-divisors).

CAUTION (AP1): kappa formulas are family-specific. NEVER copy between families.
CAUTION (AP48): kappa(W_{1+inf}) != c/2. The total kappa diverges.
CAUTION (AP9): kappa_T = c/2 is the T-LINE part only.

References:
  - Schiffmann-Vasserot (arXiv:1211.1287): CoHA = Y^+(gl_hat_1)
  - Prochazka-Rapcak (arXiv:1910.07997): W_{1+inf} = affine Yangian
  - MacMahon (1916): plane partition generating function
  - Vol I: higher_genus_modular_koszul.tex (shadow obstruction tower)
  - Vol I: w_infinity_shadow_limit.py, w_infinity_shadow_limit_deep.py
  - Vol III: c3_dt_partition.py, affine_yangian_gl1.py
"""

from __future__ import annotations

import math
import os
import sys
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Path setup for cross-volume imports
# ---------------------------------------------------------------------------

_VOL1_LIB = os.path.expanduser("~/chiral-bar-cobar/compute/lib")
_VOL3_LIB = os.path.expanduser("~/calabi-yau-quantum-groups/compute/lib")

for _p in [_VOL1_LIB, _VOL3_LIB]:
    if _p not in sys.path:
        sys.path.insert(0, _p)


# ===========================================================================
# 1. FUNDAMENTAL CONSTANTS AND FORMULAS
# ===========================================================================

def harmonic_number(n: int) -> Fraction:
    """H_n = 1 + 1/2 + ... + 1/n. H_0 = 0."""
    if n <= 0:
        return Fraction(0)
    return sum(Fraction(1, j) for j in range(1, n + 1))


def kappa_channel(s: int, c_val: Fraction = Fraction(1)) -> Fraction:
    r"""Channel curvature kappa_s = c/s for the spin-s generator.

    For W_{1+inf} at c=1: kappa_s = 1/s.

    CAUTION (AP1): This is the per-channel kappa, not the total.
    CAUTION (AP48): Total kappa = sum_{s>=1} 1/s = divergent.
    """
    return c_val / Fraction(s)


def kappa_ch_regulated(N: int, c_val: Fraction = Fraction(1)) -> Fraction:
    r"""Regulated total kappa of W_{1+inf} at spin cutoff N.

    kappa_ch(N) = sum_{s=1}^{N} c/s = c * H_N.

    For W_N (without spin-1): kappa(W_N) = c * (H_N - 1).
    For full W_{1+inf} (with spin-1): kappa = c * H_N.
    """
    return c_val * harmonic_number(N)


def kappa_wn_total(N: int, c_val: Fraction) -> Fraction:
    """Total kappa for the standard W_N algebra (generators at spins 2,...,N).

    kappa(W_N) = (H_N - 1) * c.
    """
    return (harmonic_number(N) - 1) * c_val


def c_wn_free_field(N: int) -> Fraction:
    """Central charge of W_N in the free-field realization (k -> infinity).

    c(W_N, k=inf) = N-1.
    This is the c-value where W_N is realized by N-1 free bosons.
    """
    return Fraction(N - 1)


# ===========================================================================
# 2. FABER-PANDHARIPANDE NUMBERS AND GENUS FREE ENERGIES
# ===========================================================================

def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    where B_{2g} is the 2g-th Bernoulli number.

    Values: lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680.
    """
    from sympy import bernoulli, factorial, Rational as SympyRational
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    num = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    den = 2 ** (2 * g - 1) * factorial(2 * g)
    # Convert sympy Rational to Fraction safely (int() truncates Rationals)
    result = SympyRational(num, den)
    return Fraction(int(result.p), int(result.q))


def genus_free_energy(kappa: Fraction, g: int) -> Fraction:
    """F_g(A) = kappa(A) * lambda_g^FP (genus-g free energy on scalar lane)."""
    return kappa * lambda_fp(g)


def genus_tower_regulated(N: int, max_genus: int = 5,
                          c_val: Fraction = Fraction(1)) -> Dict[int, Fraction]:
    """Regulated genus tower F_g(W_{1+inf}, cutoff N).

    F_g = kappa_ch(N) * lambda_g^FP
    where kappa_ch(N) = c * H_N (including spin-1 channel).

    Returns {g: F_g} for g = 1, ..., max_genus.
    """
    kappa = kappa_ch_regulated(N, c_val)
    return {g: kappa * lambda_fp(g) for g in range(1, max_genus + 1)}


# ===========================================================================
# 3. SHADOW TOWER COMPUTATION (per-channel, exact Fraction)
# ===========================================================================

def shadow_tower_single_channel(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
    max_r: int = 30,
) -> Dict[int, Fraction]:
    r"""Compute shadow obstruction tower on a single primary line.

    Uses the Vol I convolution recursion (full_shadow_landscape.py):
      Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
      f(t) = sqrt(Q_L(t)) = sum a_n t^n
      S_r = a_{r-2} / r

    Returns {r: S_r} for r = 2, ..., max_r.
    """
    if kappa == 0:
        raise ValueError("kappa = 0: shadow tower undefined (uncurved algebra)")

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    a0 = 2 * kappa  # signed square root
    a = [a0]

    max_n = max_r - 2
    if max_n >= 1:
        a1 = q1 / (2 * a0)
        a.append(a1)

    if max_n >= 2:
        a2 = (q2 - a[1] ** 2) / (2 * a0)
        a.append(a2)

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        an = -conv / (2 * a0)
        a.append(an)

    result = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = a[idx] / r

    return result


def shadow_class(kappa: Fraction, alpha: Fraction, S4: Fraction) -> str:
    """Shadow depth classification: G, L, C, or M.

    G: alpha=0, S4=0 (Gaussian, terminates at arity 2)
    L: alpha!=0, S4=0 (Lie/tree, terminates at arity 3)
    M: Delta=8*kappa*S4 != 0 (mixed, infinite tower)
    C: stratum separation (not detectable from single-line data)
    """
    Delta = 8 * kappa * S4
    if Delta == 0:
        if alpha == 0 and S4 == 0:
            return 'G'
        elif S4 == 0:
            return 'L'
        else:
            return 'L'
    else:
        return 'M'


def critical_discriminant(kappa: Fraction, S4: Fraction) -> Fraction:
    """Delta = 8 * kappa * S4."""
    return 8 * kappa * S4


def shadow_growth_rate(kappa: Fraction, alpha: Fraction,
                       S4: Fraction) -> float:
    r"""Shadow growth rate rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|).

    The shadow radius: |S_r| ~ C * rho^r * r^{-5/2}.
    For class G or L: rho = 0 (tower terminates).
    For class M: rho > 0 (infinite tower with geometric growth).
    """
    Delta = critical_discriminant(kappa, S4)
    val = 9 * alpha ** 2 + 2 * Delta
    val_float = float(val)
    kappa_float = float(kappa)
    if abs(kappa_float) < 1e-30:
        return float('inf')
    return math.sqrt(abs(val_float)) / (2 * abs(kappa_float))


# ===========================================================================
# 4. W_{1+INFINITY} AT c=1: CHANNEL-BY-CHANNEL SHADOW DATA
# ===========================================================================

def spin1_shadow_data() -> Dict[str, Any]:
    """Shadow data for the spin-1 channel (Heisenberg current) at c=1.

    The spin-1 generator has an abelian OPE: J(z)J(w) ~ 1/(z-w)^2.
    kappa_1 = 1 (the level), alpha = 0, S_4 = 0.
    Class G (Gaussian): the shadow terminates at arity 2.
    """
    return {
        'spin': 1,
        'kappa': Fraction(1),
        'alpha': Fraction(0),
        'S4': Fraction(0),
        'Delta': Fraction(0),
        'class': 'G',
        'r_max': 2,
        'growth_rate': 0.0,
        'tower': {2: Fraction(1)},  # S_2 = a_0/2 = 2*kappa/2 = kappa = 1
        'description': 'Heisenberg at k=1. Abelian OPE, no higher shadows.',
    }


def spin2_shadow_data(max_r: int = 20) -> Dict[str, Any]:
    """Shadow data for the spin-2 channel (Virasoro at c=1).

    kappa_T = c/2 = 1/2, alpha_T = 2, S_4 = 10/[c(5c+22)] = 10/27.
    Class M: infinite tower.
    """
    c = Fraction(1)
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    Delta = critical_discriminant(kappa, S4)
    rho = shadow_growth_rate(kappa, alpha, S4)
    tower = shadow_tower_single_channel(kappa, alpha, S4, max_r)
    return {
        'spin': 2,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'class': 'M',
        'r_max': None,  # infinite
        'growth_rate': rho,
        'tower': tower,
        'description': f'Virasoro at c=1. Class M, rho={rho:.4f}.',
    }


def spin_s_shadow_data(s: int, max_r: int = 20) -> Dict[str, Any]:
    r"""Shadow data for the spin-s channel of W_{1+inf} at c=1.

    kappa_s = 1/s.
    For odd s: alpha_s = 0 (Z_2 parity W_s -> -W_s forces odd arities to vanish).
    For even s: alpha_s = s (gravitational cubic from T-W_s-W_s vertex).

    The quartic contact S_{4,s} for general spin s at c=1:
    On the W_s-line, S_{4,s} comes from exchange of weight-4 quasi-primaries.
    For the T-line (s=2): S_4 = 10/[c(5c+22)] = 10/27.
    For the W-line of W_3 (s=3): S_4 = 2560/[c(5c+22)^3] at c=1.
    For general s >= 3: S_{4,s} depends on the full OPE structure of W_{1+inf}.

    SIMPLIFICATION: On the W_s-line with x_T = 0 and only W_s nonzero,
    the quartic self-coupling involves the exchange of weight-4 quasi-primaries
    in the W_s x W_s OPE. For a single free boson realization at c=1:
    W_s = :partial^s phi: and the self-coupling is explicitly computable.

    For this module, we use the known data for s=1,2,3 and a structural
    estimate for s >= 4 based on the free-boson OPE.
    """
    c = Fraction(1)
    kappa = c / Fraction(s)

    if s == 1:
        return spin1_shadow_data()
    if s == 2:
        return spin2_shadow_data(max_r)

    # Spin s >= 3
    # Parity: for odd s, Z_2 parity forces alpha = 0 on the self-coupling line
    # For even s, the gravitational cubic is nonzero
    if s % 2 == 1:
        alpha = Fraction(0)
    else:
        # Gravitational cubic: alpha_s from the T-W_s-W_s coupling
        # The Virasoro ward identity gives C(T, W_s, W_s) = s * <W_s W_s>
        # On the W_s-line (x_T = 0), the cubic is the SELF-coupling
        # For even s at c=1 in the free boson: alpha_s = s (from gravitational sector)
        alpha = Fraction(s)

    # Quartic contact: for s=3 at c=1, S_4 = 2560/(1*27^3)
    if s == 3:
        S4 = Fraction(2560) / (c * (5 * c + 22) ** 3)
    else:
        # For general s >= 4: the quartic involves exchange of weight-4 QPs.
        # In the free-boson realization W_s = :partial^s phi:,
        # the leading OPE coefficient is W_s(z)W_s(w) ~ s! * k^s / (z-w)^{2s}
        # At c=1 (k=1): norm = s!, pole order 2s.
        # The quartic arises from weight-4 exchange in the (2s-4)-th pole.
        # We use the structural formula: S_{4,s} scales as 1/s^2 for large s
        # (the quartic becomes dilute as the spin increases).
        #
        # Precise computation for the free boson:
        # The W_s(z)W_s(w) OPE for W_s = :partial^s phi: at k=1:
        #   ~ s! / (z-w)^{2s} + [subleading terms]
        # The r-matrix (AP19: one pole order lower) has pole order 2s-1.
        # The Hessian (inverse propagator on this line) is: H_s = kappa_s = 1/s.
        # So the propagator P_s = s.
        # S_4 = (structure constant)^2 * P_s / (normalization)
        #
        # For a precise estimate: at large s, the OPE truncates at simple
        # pole orders, and S_4 ~ Fraction(1, s**2) * const.
        # We use S_4 = 0 as the leading approximation for s >= 4 on the
        # diagonal (all higher quartics are parametrically small).
        # This gives class L or G depending on alpha.
        # CAVEAT: this is an APPROXIMATION. The true quartic for each s
        # requires the full W_{1+inf} OPE, which depends on the deformation
        # parameters (sigma_1, sigma_2).
        S4 = Fraction(0)  # leading approximation for s >= 4

    Delta = critical_discriminant(kappa, S4)
    cls = shadow_class(kappa, alpha, S4)

    rho = 0.0
    if cls == 'M':
        rho = shadow_growth_rate(kappa, alpha, S4)

    tower = shadow_tower_single_channel(kappa, alpha, S4, max_r)

    return {
        'spin': s,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'class': cls,
        'r_max': 2 if cls == 'G' else (3 if cls == 'L' else (4 if cls == 'C' else None)),
        'growth_rate': rho,
        'tower': tower,
        'description': (
            f'Spin-{s} channel at c=1. kappa={float(kappa):.6f}, '
            f'alpha={float(alpha)}, class {cls}.'
        ),
    }


def full_channel_census(max_spin: int = 10, max_r: int = 15) -> List[Dict[str, Any]]:
    """Compute shadow data for all channels of W_{1+inf} at c=1.

    Returns list of dicts, one per channel from spin 1 to max_spin.
    """
    return [spin_s_shadow_data(s, max_r) for s in range(1, max_spin + 1)]


# ===========================================================================
# 5. MACMAHON FUNCTION AND LOG-COEFFICIENT IDENTITY
# ===========================================================================

def sigma_2(k: int) -> int:
    """Sum-of-squares-of-divisors: sigma_2(k) = sum_{d|k} d^2."""
    return sum(d * d for d in range(1, k + 1) if k % d == 0)


def sigma_r(k: int, r: int) -> int:
    """Generalized divisor sum: sigma_r(k) = sum_{d|k} d^r."""
    return sum(d ** r for d in range(1, k + 1) if k % d == 0)


def log_macmahon_coefficients(N: int) -> List[Fraction]:
    r"""Coefficients of log M(q) = sum_{k>=1} c_k q^k, truncated at q^N.

    PROVED IDENTITY: c_k = sigma_2(k) / k.

    Derivation:
      log M(q) = sum_{n>=1} n * log(1/(1-q^n))
               = sum_{n>=1} n * sum_{m>=1} q^{mn}/m
               = sum_{k>=1} q^k * sum_{nm=k} n/m

    For k = nm, the coefficient is:
      c_k = sum_{d|k} (k/d) / d = (1/k) * sum_{d|k} (k/d)^2 ... no.
    Actually: for nm = k with n = k/m:
      c_k = sum_{m|k} (k/m) / m = sum_{m|k} k/m^2 = k * sum_{m|k} 1/m^2 ... no.

    Let me be precise. Each (n,m) with nm=k contributes n/m.
    For divisor d = m of k: n = k/d, contribution = (k/d)/d = k/d^2.
    So c_k = sum_{d|k} k/d^2 = k * sum_{d|k} 1/d^2 ... no.

    Let me redo: (n,m) with nm=k. n = k/m (m ranges over divisors of k).
    Contribution from (n,m) = n/m = (k/m)/m = k/m^2.
    So c_k = sum_{m|k} k/m^2 = k * sum_{m|k} 1/m^2.

    But also: sum_{m|k} 1/m^2 = (1/k^2) * sum_{m|k} (k/m)^2
            = (1/k^2) * sum_{d|k} d^2 = sigma_2(k)/k^2.

    So c_k = k * sigma_2(k)/k^2 = sigma_2(k)/k.

    Returns [0, c_1, c_2, ..., c_{N-1}] where c_0 = 0.
    """
    result = [Fraction(0)] * N
    for n in range(1, N):
        for m in range(1, N):
            nm = n * m
            if nm >= N:
                break
            result[nm] += Fraction(n, m)
    return result


def log_macmahon_via_divisor_sum(N: int) -> List[Fraction]:
    r"""Independent computation: c_k = sigma_2(k)/k.

    This is the second verification path for the log M(q) identity.
    """
    result = [Fraction(0)] * N
    for k in range(1, N):
        result[k] = Fraction(sigma_2(k), k)
    return result


def macmahon_coefficients_log_exp(N: int) -> List[Fraction]:
    r"""Compute M(q) coefficients via log M(q) = sum sigma_2(k)/k q^k, then exp.

    Third verification path: compute log, then exponentiate.
    """
    log_c = log_macmahon_via_divisor_sum(N)

    # Exponentiate: g[n] = (1/n) sum_{k=1}^{n} k*f[k]*g[n-k]
    g = [Fraction(0)] * N
    g[0] = Fraction(1)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += Fraction(k) * log_c[k] * g[n - k]
        g[n] = s / Fraction(n)

    return g


def macmahon_direct_product(N: int) -> List[Fraction]:
    r"""Compute M(q) = prod_{n=1}^{N-1} 1/(1-q^n)^n mod q^N by direct product.

    Fourth verification path.
    """
    result = [Fraction(0)] * N
    result[0] = Fraction(1)
    for n in range(1, N):
        for _ in range(n):
            for k in range(n, N):
                result[k] += result[k - n]
    return result


# ===========================================================================
# 6. SHADOW-MACMAHON BRIDGE: THE ROSETTA STONE
# ===========================================================================

def effective_kappa_per_level() -> Fraction:
    r"""Effective kappa contribution per energy level in the MacMahon decomposition.

    M(q) = prod_{n>=1} (1/(1-q^n))^n.
    The exponent n means n copies of the energy-n mode.
    Each copy at energy n has kappa_n = c/n = 1/n (at c=1).
    Effective kappa for energy level n: n * (1/n) = 1.

    This is CONSTANT across all energy levels: every energy level
    contributes equally to the total modular characteristic.

    Returns Fraction(1).
    """
    return Fraction(1)


def verify_effective_kappa_constancy(max_n: int = 50) -> List[Fraction]:
    """Verify that the effective kappa per level is constant = 1.

    For level n: n copies * kappa_n = n * (1/n) = 1.
    Returns list of effective kappas for n = 1, ..., max_n.
    """
    return [Fraction(n) * Fraction(1, n) for n in range(1, max_n + 1)]


def shadow_genus_macmahon_comparison(max_genus: int = 5,
                                     max_N: int = 50) -> Dict[str, Any]:
    """Compare the regulated genus tower with MacMahon asymptotics.

    The regulated F_g(W_{N}, c=N-1) should relate to the topological
    string genus expansion of log M(q).

    Returns comparison data.
    """
    result = {'genus_data': {}, 'N_values': list(range(2, max_N + 1))}

    for g in range(1, max_genus + 1):
        lam_g = lambda_fp(g)
        f_g_list = []
        for N in range(2, max_N + 1):
            c_val = Fraction(N - 1)
            kappa_ch = kappa_wn_total(N, c_val)
            f_g = kappa_ch * lam_g
            f_g_list.append(float(f_g))
        result['genus_data'][g] = {
            'lambda_g': lam_g,
            'F_g_sequence': f_g_list,
            'growth_type': 'N*log(N)*lambda_g',
        }

    return result


def log_macmahon_channel_decomposition(N: int) -> Dict[str, Any]:
    r"""Decompose log M(q) into channel contributions.

    log M(q) = sum_{n>=1} n * log(1/(1-q^n))

    Each factor n * log(1/(1-q^n)) is the contribution of n copies
    of a boson at energy n. In shadow language:
      channel n contributes kappa_n^{eff} = n * (1/n) = 1 to the total.

    Returns decomposition data through order q^N.
    """
    total = [Fraction(0)] * N
    channel_contributions = {}

    for n in range(1, N):
        # Contribution from channel n: n * log(1/(1-q^n)) = n * sum_{m>=1} q^{nm}/m
        chan = [Fraction(0)] * N
        for m in range(1, N):
            nm = n * m
            if nm >= N:
                break
            chan[nm] += Fraction(n, m)
        channel_contributions[n] = chan
        for k in range(N):
            total[k] += chan[k]

    return {
        'total': total,
        'channels': channel_contributions,
        'n_channels': N - 1,
    }


# ===========================================================================
# 7. SHADOW DEPTH AND GROWTH ANALYSIS
# ===========================================================================

def overall_shadow_classification() -> Dict[str, Any]:
    """Classify the overall shadow depth of W_{1+inf} at c=1.

    Channel-by-channel:
      Spin 1: class G (terminates at r=2)
      Spin 2: class M (infinite, rho = 6.24)
      Spin s >= 3 (odd): class G or L (alpha=0, S4 depends on OPE)
      Spin s >= 3 (even): class L (alpha=s, S4=0 at leading order) or M

    Overall: the algebra is class M (the Virasoro sub-tower is already
    class M, and this persists in the full algebra).

    The shadow depth is INFINITE: r_max = infinity.
    This is consistent with W_{1+inf} being a class M algebra.
    """
    return {
        'overall_class': 'M',
        'r_max': None,  # infinity
        'reason': (
            'The spin-2 channel (Virasoro at c=1) has nonzero critical '
            'discriminant Delta = 40/27, forcing class M (infinite tower). '
            'All even-spin channels also have alpha != 0, contributing to '
            'infinite tower depth. The full algebra inherits class M.'
        ),
        'spin1_class': 'G',
        'spin2_class': 'M',
        'spin_odd_class': 'G or L (depends on quartic)',
        'spin_even_class': 'L or M (depends on quartic)',
        'convergent_on_tline': False,
        'tline_growth_rate': shadow_growth_rate(
            Fraction(1, 2), Fraction(2), Fraction(10, 27)
        ),
    }


def shadow_tower_diagonal(
    max_spin: int = 10,
    max_r: int = 15,
    c_val: Fraction = Fraction(1),
) -> Dict[int, Fraction]:
    """Shadow tower on the diagonal (all channel amplitudes equal).

    This computes S_r^{diag} = sum_{s=1}^{max_spin} S_r^{(s)} where
    S_r^{(s)} is the spin-s channel's r-th shadow coefficient.

    CAUTION: The diagonal is NOT the same as the multi-channel metric tower.
    The full multi-channel computation involves cross-couplings (propagator
    variance, mixing polynomial). The diagonal sum is a LOWER BOUND on the
    full multi-channel tower complexity.
    """
    diagonal = {}
    for r in range(2, max_r + 1):
        diagonal[r] = Fraction(0)

    for s in range(1, max_spin + 1):
        data = spin_s_shadow_data(s, max_r)
        for r in range(2, max_r + 1):
            if r in data['tower']:
                diagonal[r] += data['tower'][r]

    return diagonal


# ===========================================================================
# 8. CROSS-VERIFICATION WITH DT/CoHA
# ===========================================================================

def plane_partition_counts(N: int) -> List[int]:
    """Plane partition counts p(0), ..., p(N-1) from MacMahon M(q).

    p(k) = # of plane partitions of k.
    Ground truth: OEIS A000219.
    """
    coeffs = macmahon_direct_product(N)
    return [int(c) for c in coeffs]


OEIS_A000219 = [
    1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500, 859, 1479,
    2485, 4167, 6879, 11297, 18334, 29601, 47330, 75278,
]


def verify_macmahon_against_oeis(N: int = 21) -> bool:
    """Verify MacMahon coefficients against OEIS A000219."""
    computed = plane_partition_counts(N)
    for k in range(min(N, len(OEIS_A000219))):
        if computed[k] != OEIS_A000219[k]:
            return False
    return True


def coha_graded_dimension_check(N: int = 21) -> Dict[str, Any]:
    """Verify that dim Y^+(gl_hat_1)_k = p(k) (plane partitions of k).

    The CoHA of C^3 has a basis indexed by plane partitions.
    The degree-k component has dimension p(k).
    """
    pp_counts = plane_partition_counts(N)
    oeis_ok = all(
        pp_counts[k] == OEIS_A000219[k]
        for k in range(min(N, len(OEIS_A000219)))
    )
    return {
        'pp_counts': pp_counts[:min(N, 21)],
        'oeis_match': oeis_ok,
        'formula': 'dim Y^+(gl_hat_1)_k = p(k)',
    }


# ===========================================================================
# 9. THE ROSETTA DICTIONARY
# ===========================================================================

def rosetta_stone() -> Dict[str, str]:
    """The W_{1+inf} / positive-half CoHA / DT / Shadow dictionary.

    Maps between four languages for the same mathematics.
    """
    return {
        # VOA language -> DT language
        'W_{1+inf} at c=1': 'Drinfeld double/center evaluation of CoHA Y^+(gl_hat_1)',
        'shadow tower Theta_{W_{1+inf}}': 'DT obstruction theory on C^3',
        'kappa_s = 1/s': 'virtual rank per spin channel',
        'total kappa (divergent)': 'non-compact Euler characteristic (regularize)',
        'F_g = kappa * lambda_g': 'genus-g GW/DT invariant of C^3',
        'shadow class M': 'non-trivial higher-genus corrections',
        'log M(q) = sum sigma_2(k)/k q^k': 'DT free energy decomposition',
        'effective kappa per level = 1': 'uniform DT weight per box-counting level',
        'regulated W_N cutoff': 'DT framing / box truncation',
        'shadow growth rate rho': 'DT convergence radius',
        'MacMahon M(q)': 'DT partition function Z^{DT}_{C^3}',
        'plane partition p(k)': 'dim Y^+(gl_hat_1)_k',
        'sigma_2(k)/k': 'MacMahon log coefficient at q^k',
    }


# ===========================================================================
# 10. SUMMARY AND MAIN RESULTS
# ===========================================================================

def main_results() -> Dict[str, Any]:
    """Compute and return all main results for the C^3 shadow tower.

    Returns a dictionary with all key quantities.
    """
    c = Fraction(1)

    # Channel data
    spin1 = spin1_shadow_data()
    spin2 = spin2_shadow_data(max_r=20)
    spin3 = spin_s_shadow_data(3, max_r=15)

    # Kappa values
    kappa_ch_10 = kappa_ch_regulated(10, c)
    kappa_ch_100 = kappa_ch_regulated(100, c)

    # MacMahon verification
    mac_ok = verify_macmahon_against_oeis()
    log_mac = log_macmahon_coefficients(21)
    log_mac_div = log_macmahon_via_divisor_sum(21)

    # Genus tower (regulated)
    genus_tower_10 = genus_tower_regulated(10, max_genus=5, c_val=c)
    genus_tower_100 = genus_tower_regulated(100, max_genus=5, c_val=c)

    return {
        'c': c,
        'algebra': 'W_{1+infinity}',
        'channels': {
            1: spin1,
            2: spin2,
            3: spin3,
        },
        'kappa': {
            'per_channel': {s: Fraction(1, s) for s in range(1, 11)},
            'total_regulated_10': kappa_ch_10,
            'total_regulated_100': kappa_ch_100,
            'total_divergent': True,
            'effective_per_level': Fraction(1),
        },
        'shadow_class': 'M',
        'r_max': None,  # infinity
        'macmahon': {
            'oeis_verified': mac_ok,
            'log_identity_verified': all(
                log_mac[k] == log_mac_div[k] for k in range(21)
            ),
        },
        'genus_tower': {
            'regulated_N10': genus_tower_10,
            'regulated_N100': genus_tower_100,
            'divergent_at_N_inf': True,
        },
        'rosetta': rosetta_stone(),
    }
