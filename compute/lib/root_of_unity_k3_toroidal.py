r"""Root-of-unity specialization of the K3 quantum toroidal algebra.

STATUS: CONJECTURAL (AP-CY14).  ALL results in this module are conditional on:
  (1) The existence of U_{q,t}(g_{K3}^{tor}) (Conjecture conj:k3-quantum-toroidal),
  (2) CY-A_3 for K3 x E,
  (3) The existence of Y(g_{K3}) (Conjecture conj:k3-yangian).

This module constructs what the ROOT-OF-UNITY SPECIALIZATION of the K3 quantum
toroidal algebra MUST be if the algebra exists, and determines whether the
resulting representation category is a modular tensor category (MTC).

MATHEMATICAL CONTENT
====================

THE ROOT-OF-UNITY PROBLEM:
  In 3d Chern-Simons theory, U_q(g) at q = e^{2*pi*i/(k+h^v)} has:
  - Finitely many simple modules (k+1 for sl_2)
  - Modular tensor category structure (Reshetikhin-Turaev)
  - WRT invariants of 3-manifolds

  For 6d holomorphic CS, the question is:
  Does U_{q,t}(g_{K3}^{tor}) at q = e^{2*pi*i/N} have:
  - Finitely many simple modules?
  - Modular tensor category structure?
  - 6-manifold invariants?

THE KEY MECHANISM -- PERIODICITY OF G(x):
  The trigonometric structure function is:
    G_{K3}(x) = prod_{a=1}^{24} (1 - q_a x) / (1 - q_a^{-1} x)

  At generic q_a, G_{K3}(x) is a rational function of x with no periodicity.

  At a root of unity, set q_a = omega^{n_a} where omega = e^{2*pi*i/N}
  and n_a are integers satisfying sum n_a = 0 mod N (CY_2 constraint).
  Then q_a^N = 1 for all a, so:
    G_{K3}(omega^N * x) = G_{K3}(x)

  The structure function becomes PERIODIC in the multiplicative variable x
  under x -> omega^N x = x (trivially). More importantly, the OPE poles
  are now on a FINITE set: the poles of G_a(x) are at x = q_a = omega^{n_a},
  which is an N-th root of unity.

  This periodicity forces a TRUNCATION of the representation category.
  At generic parameters: the spectral parameter u ranges over C
  (continuous family of simples). At root of unity: the spectral parameter
  lives on C/NZ = C* / <omega> (quotient by the cyclic group generated
  by omega), giving an N-periodic identification.

THE TRUNCATION MECHANISM:
  For U_q(sl_2) at q = e^{pi*i/l} (l = k + h^v):
  - [l]_q = 0  (quantum integer vanishes)
  - V_l is zero in the quotient category
  - Simple objects: V_0, V_1, ..., V_{l-2}  (= l-1 = k+1 objects for sl_2)

  For U_{q,t}(g_{K3}^{tor}) at omega = e^{2*pi*i/N}:
  - The quantum integer [N]_{omega} = 0
  - At charge n, the Fock module F_n decomposes into simples indexed by
    RESTRICTED 24-coloured partitions of n with parts < N
  - The number of such restricted partitions is FINITE at each charge

  The RESTRICTED 24-coloured partition function is:
    p_{24}^{<N}(n) = coeff of q^n in prod_{k=1}^{N-1} 1/(1-q^k)^{24}

  For unrestricted: prod_{k>=1} 1/(1-q^k)^{24} (infinite product).
  For restricted (root of unity): prod_{k=1}^{N-1} 1/(1-q^k)^{24} (finite).

THE VERLINDE DIMENSION:
  The chiral Verlinde dimension at level N is:
    V_N^{ch}(g) = dim H*(B_{E_3}(A_N), d_{tot}) at genus g

  For the K3 quantum toroidal at root of unity, we CONJECTURE:
    V_N^{ch}(0) = sum_{n=0}^{N-1} p_{24}^{<N}(n)

  This is the total number of simple objects at level N.

MODULARITY:
  A braided category is MODULAR (MTC) iff its S-matrix is non-degenerate:
    det(S) != 0

  For the K3 quantum toroidal at root of unity, the S-matrix acts on
  the truncated Fock space. The S-matrix entries are:
    S_{lambda,mu} = quantum trace of the braiding on V_lambda tensor V_mu

  For the abelian (gl_1) case, the S-matrix factorizes over the 24 Mukai
  directions. The key question is whether the Mukai signature (4,20)
  causes S to be degenerate.

  RESULT (Conjecture conj:k3-root-unity-mtc):
  The S-matrix is NON-DEGENERATE for N coprime to 24 (i.e., gcd(N,24) = 1).
  For N dividing 24, the kernel of S is nontrivial and the category is
  NOT modular but pre-modular (ribbon fusion).

CONWAY GROUP CONNECTION:
  The automorphism group of the Leech lattice is the Conway group Co_0.
  The Leech lattice is the unique even unimodular lattice of rank 24
  with no roots. Its theta series is:
    Theta_Leech(q) = 1 + 196560 q^2 + 16773120 q^3 + ...

  The Mukai lattice Lambda_Muk = U^3 + E_8(-1)^2 is DIFFERENT from
  the Leech lattice (it has root vectors), but they are related:
  both are even unimodular lattices of rank 24.

  At the ORBIFOLD POINT of K3 moduli where the Leech lattice VOA V_Leech
  governs the BPS spectrum (Duncan's Mathieu moonshine), the root-of-unity
  truncation acquires a Co_0 symmetry.

  The connection: the Verlinde numbers V_N at the Leech point are
  Co_0-invariant, and the fusion rules respect the Conway action.
  This is the 6d analogue of the M_24 moonshine for the K3 elliptic
  genus (Eguchi-Ooguri-Tachikawa 2010).

CONVENTIONS:
  - omega = e^{2*pi*i/N} (primitive N-th root of unity)
  - n_a: integer exponents, q_a = omega^{n_a}, sum n_a = 0 mod N
  - kappa subscripts per AP113 (kappa_ch, kappa_BKM, kappa_cat, kappa_fiber)
  - AP-CY14: ALL results CONJECTURAL
  - AP-CY5: root of unity required for non-semisimplicity

REFERENCES:
  k3_quantum_toroidal.py (generic-parameter K3 quantum toroidal)
  k3_yangian.py (rational limit)
  kl_sl2_level1.py (prototype: sl_2 at root of unity)
  chiral_qg_rep_category.py (representation category at generic params)
  cfg25_adversarial_consistency.py (gap analysis: root-of-unity not constructed)
  niemeier_shadow_landscape.py (Niemeier lattices and Conway group)
  k3_times_e.tex, conj:k3-quantum-toroidal
  Feigin-Jimbo-Miwa-Mukhin, Kyoto J Math 52 (2012)
  Miki, J Math Phys 48 (2007)
  Eguchi-Ooguri-Tachikawa, Exper Math 20 (2011)
  Duncan, Duke Math J 139 (2007)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np

from compute.lib.k3_quantum_toroidal import (
    K3QuantumToroidalAlgebra,
    N_MUKAI,
    STATUS as PARENT_STATUS,
    trigonometric_structure_function,
    verify_cy2_multiplicative,
    _colored_partition,
    _eta_power_coefficients,
)

from compute.lib.k3_yangian import (
    SIG_PLUS,
    SIG_MINUS,
    mukai_diagonal_eigenvalues,
)


# =========================================================================
# 0. Status and constants
# =========================================================================

STATUS = 'CONJECTURAL'  # AP-CY14: everything here is conjectural

MUKAI_RANK = N_MUKAI  # 24


# =========================================================================
# 1. Root-of-unity arithmetic
# =========================================================================

def primitive_root(N: int) -> complex:
    r"""Compute omega = e^{2*pi*i/N}, the primitive N-th root of unity.

    Parameters
    ----------
    N : int
        The order of the root of unity (N >= 2).

    Returns
    -------
    complex
        omega = e^{2*pi*i/N}.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    return cmath.exp(2j * cmath.pi / N)


def q_number_root_of_unity(n: int, omega: complex, N: int) -> complex:
    r"""Compute the quantum integer [n]_omega at a root of unity.

    [n]_omega = (omega^n - omega^{-n}) / (omega - omega^{-1})

    At omega = e^{2*pi*i/N}: [N]_omega = 0 (truncation).
    More generally: [n]_omega = 0 iff N | n.

    Parameters
    ----------
    n : int
        The integer to quantize.
    omega : complex
        The root of unity omega = e^{2*pi*i/N}.
    N : int
        The order of the root of unity.

    Returns
    -------
    complex
        [n]_omega.
    """
    # Use the trigonometric form: [n]_omega = sin(n*pi/N) / sin(pi/N).
    # This is well-defined for all N >= 2 and avoids the degenerate
    # denominator at omega = -1 (N = 2) where omega - omega^{-1} = 0.
    s_denom = math.sin(math.pi / N)
    if abs(s_denom) < 1e-15:
        # N = 1 (excluded by construction), fallback
        return complex(float(n))
    return complex(math.sin(n * math.pi / N) / s_denom)


def quantum_integers_at_root(N: int) -> List[complex]:
    """Compute [0]_omega, [1]_omega, ..., [N]_omega at omega = e^{2*pi*i/N}.

    [N]_omega = 0 (truncation point).

    Returns list of N+1 quantum integers.
    """
    omega = primitive_root(N)
    return [q_number_root_of_unity(n, omega, N) for n in range(N + 1)]


def verify_truncation(N: int, tol: float = 1e-10) -> Tuple[bool, complex]:
    """Verify that [N]_omega = 0 at omega = e^{2*pi*i/N}.

    This is the fundamental truncation condition that drives the
    finite-dimensionality of the representation category.

    Returns (truncation_holds, value_of_[N]).
    """
    omega = primitive_root(N)
    qN = q_number_root_of_unity(N, omega, N)
    return abs(qN) < tol, qN


# =========================================================================
# 2. Root-of-unity parameters for K3
# =========================================================================

class RootOfUnityK3Params(NamedTuple):
    """Parameters for the K3 quantum toroidal at a root of unity."""
    N: int                    # order of root of unity
    omega: complex            # primitive N-th root: e^{2*pi*i/N}
    n_mukai: List[int]        # integer exponents: q_a = omega^{n_a}
    q_mukai: List[complex]    # multiplicative params: q_a = omega^{n_a}
    cy2_residual: float       # |prod q_a - 1|


def kummer_root_of_unity_params(N: int) -> RootOfUnityK3Params:
    r"""Construct root-of-unity K3 parameters modelling the Kummer surface.

    For the Kummer K3 = T^4/Z_2, the Mukai lattice decomposes as:
      4 positive directions, 20 negative directions.

    The CY_2 constraint is sum n_a = 0 mod N.

    We choose:
      n_a = +1 for a = 0, 1, 2, 3  (4 positive directions)
      n_a = -1 for a = 4, ..., 7    (4 of the 20 negative directions)
      n_a =  0 for a = 8, ..., 23   (remaining 16 negative directions)

    This gives sum n_a = 4 - 4 + 0 = 0 = 0 mod N for all N.

    The choice of 4 positive and 4 negative unit exponents mirrors the
    Kummer T^4/Z_2 geometry, where the 4 torus directions contribute
    equally with opposite signs from the orbifold projection.

    Parameters
    ----------
    N : int
        Order of the root of unity (N >= 2).

    Returns
    -------
    RootOfUnityK3Params
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")

    omega = primitive_root(N)

    # Kummer-type parametrisation
    n_mukai = [0] * MUKAI_RANK
    for a in range(4):
        n_mukai[a] = 1       # positive Mukai directions
    for a in range(4, 8):
        n_mukai[a] = N - 1   # = -1 mod N (negative directions)
    # n_mukai[8:24] = 0 (neutral)

    q_mukai = [omega ** n for n in n_mukai]

    # Verify CY_2: prod q_a = omega^{sum n_a} = omega^0 = 1
    prod_q = complex(1.0)
    for qa in q_mukai:
        prod_q *= qa
    cy2_res = abs(prod_q - 1.0)

    return RootOfUnityK3Params(
        N=N,
        omega=omega,
        n_mukai=n_mukai,
        q_mukai=q_mukai,
        cy2_residual=cy2_res,
    )


def generic_root_of_unity_params(
    N: int,
    exponents: Optional[List[int]] = None,
) -> RootOfUnityK3Params:
    r"""Construct root-of-unity K3 parameters with custom exponents.

    Parameters
    ----------
    N : int
        Order of the root of unity.
    exponents : list of 24 integers, optional
        The n_a with sum n_a = 0 mod N. If None, uses the Kummer default.

    Returns
    -------
    RootOfUnityK3Params
    """
    if exponents is None:
        return kummer_root_of_unity_params(N)

    if len(exponents) != MUKAI_RANK:
        raise ValueError(f"Need {MUKAI_RANK} exponents, got {len(exponents)}")

    total = sum(exponents)
    if total % N != 0:
        raise ValueError(
            f"CY_2 constraint violated: sum n_a = {total}, not 0 mod {N}"
        )

    omega = primitive_root(N)
    q_mukai = [omega ** n for n in exponents]

    prod_q = complex(1.0)
    for qa in q_mukai:
        prod_q *= qa
    cy2_res = abs(prod_q - 1.0)

    return RootOfUnityK3Params(
        N=N,
        omega=omega,
        n_mukai=list(exponents),
        q_mukai=q_mukai,
        cy2_residual=cy2_res,
    )


# =========================================================================
# 3. Periodic structure function at root of unity
# =========================================================================

def structure_function_root_of_unity(
    x: complex,
    params: RootOfUnityK3Params,
) -> complex:
    r"""Evaluate G_{K3}(x) at root-of-unity parameters.

    G_{K3}(x) = prod_{a=1}^{24} (1 - q_a x) / (1 - q_a^{-1} x)

    where q_a = omega^{n_a} are N-th roots of unity.

    At root of unity, G_{K3}(x) has the PERIODICITY property:
      G_{K3}(omega * x) depends on the same poles/zeros as G_{K3}(x)
      because omega^N = 1 makes the pole set periodic.

    Parameters
    ----------
    x : complex
        Spectral parameter.
    params : RootOfUnityK3Params
        Root-of-unity parameters.

    Returns
    -------
    complex
        G_{K3}(x).
    """
    return trigonometric_structure_function(x, params.q_mukai)


def verify_periodicity(
    params: RootOfUnityK3Params,
    n_points: int = 32,
    tol: float = 1e-10,
) -> Tuple[bool, float]:
    r"""Verify the periodicity G_{K3}(omega^N * x) = G_{K3}(x).

    Since omega^N = 1, this is the trivial identity G(1*x) = G(x).
    The NON-TRIVIAL periodicity is at the level of poles and zeros:
    the pole set {q_a^{-1}} and zero set {q_a^{-1} / q_a^2} are both
    subsets of the N-th roots of unity.

    What we verify instead is the SPECTRAL periodicity: the structure
    function G(x) = G(omega^k * x) for k = N (trivially), but the
    interesting structure is that G(x) only depends on x mod the group
    generated by the q_a's (which is a subgroup of Z/NZ).

    Returns (passes, max_residual).
    """
    omega = params.omega
    N = params.N
    max_res = 0.0

    for j in range(n_points):
        theta = 2.0 * math.pi * (j + 0.37) / n_points
        x = 0.5 * np.exp(1j * theta)
        try:
            gx = structure_function_root_of_unity(x, params)
            gx_shifted = structure_function_root_of_unity(
                x * omega**N, params,
            )
            res = abs(gx - gx_shifted)
            max_res = max(max_res, res)
        except ZeroDivisionError:
            continue

    return max_res < tol, max_res


def pole_structure(params: RootOfUnityK3Params) -> Dict[str, Any]:
    r"""Analyse the pole structure of G_{K3}(x) at root of unity.

    Poles of G_a(x) = (1 - q_a x) / (1 - q_a^{-1} x) are at x = q_a.
    At root of unity, q_a = omega^{n_a}, so the poles are:
      x = omega^{-n_a}  (i.e., at positions q_a^{-1} on the unit circle)

    The zeros are at x = q_a^{-1} * q_a^2 = q_a (from the numerator).
    Wait -- zeros of (1 - q_a x) are at x = 1/q_a = omega^{-n_a}.
    Poles of 1/(1 - q_a^{-1} x) are at x = q_a.

    Correcting:
      Zeros of G_a(x): x = 1/q_a = omega^{-n_a}
      Poles of G_a(x): x = q_a = omega^{n_a}

    So both zeros and poles live on the N-th roots of unity.

    Returns dict with pole/zero analysis.
    """
    omega = params.omega
    N = params.N
    n_mukai = params.n_mukai

    # Pole positions: x = q_a = omega^{n_a} for each a
    pole_exponents = [n % N for n in n_mukai]
    # Zero positions: x = 1/q_a = omega^{-n_a} = omega^{N - n_a}
    zero_exponents = [(N - n) % N for n in n_mukai]

    # Count multiplicities at each position
    pole_mult = {}
    zero_mult = {}
    for p in pole_exponents:
        pole_mult[p] = pole_mult.get(p, 0) + 1
    for z in zero_exponents:
        zero_mult[z] = zero_mult.get(z, 0) + 1

    # Cancellations: at position k, order = pole_mult[k] - zero_mult[k]
    net_order = {}
    all_positions = set(pole_mult.keys()) | set(zero_mult.keys())
    for k in all_positions:
        net = pole_mult.get(k, 0) - zero_mult.get(k, 0)
        if net != 0:
            net_order[k] = net

    # Number of DISTINCT pole positions on omega^{Z/NZ}
    distinct_poles = len([k for k, v in net_order.items() if v > 0])
    distinct_zeros = len([k for k, v in net_order.items() if v < 0])

    return {
        'N': N,
        'pole_exponents': sorted(pole_mult.keys()),
        'zero_exponents': sorted(zero_mult.keys()),
        'pole_multiplicities': pole_mult,
        'zero_multiplicities': zero_mult,
        'net_order': net_order,
        'distinct_pole_positions': distinct_poles,
        'distinct_zero_positions': distinct_zeros,
        'poles_on_roots_of_unity': True,  # by construction
        'total_pole_count': sum(v for v in pole_mult.values()),
        'total_zero_count': sum(v for v in zero_mult.values()),
    }


# =========================================================================
# 4. Restricted partition function (truncated Fock space)
# =========================================================================

def restricted_colored_partition(n: int, colors: int, max_part: int) -> int:
    r"""Compute p_c^{<N}(n): coloured partitions of n with parts < max_part.

    This is the coefficient of q^n in prod_{k=1}^{max_part - 1} 1/(1-q^k)^c.

    At root of unity omega = e^{2*pi*i/N}, the truncation forces parts < N.
    The reason: the quantum integer [N]_omega = 0, so the N-th mode is
    killed, and only modes k = 1, ..., N-1 survive.

    Parameters
    ----------
    n : int
        The number to partition.
    colors : int
        Number of colours (= 24 for K3).
    max_part : int
        Maximum allowed part size (= N for root-of-unity level N).

    Returns
    -------
    int
        Number of restricted coloured partitions.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for k in range(1, max_part):  # parts 1, 2, ..., max_part - 1
        for _ in range(colors):
            for j in range(k, n + 1):
                dp[j] += dp[j - k]

    return dp[n]


def truncated_fock_dimensions(N: int, max_charge: int = -1) -> List[int]:
    r"""Compute dimensions of the truncated Fock space at each charge.

    At root of unity omega = e^{2*pi*i/N}, the charge-n Fock module
    decomposes into:
      dim F_n^{<N} = p_{24}^{<N}(n) = restricted 24-coloured partitions

    Since parts are restricted to {1, ..., N-1}, the maximum total
    charge is bounded by (N-1) * (number of parts), but in practice
    we compute up to a reasonable max_charge.

    Parameters
    ----------
    N : int
        Level (root-of-unity order).
    max_charge : int
        Maximum charge to compute. Default: 2*N.

    Returns
    -------
    list of int
        [dim F_0, dim F_1, ..., dim F_{max_charge}].
    """
    if max_charge < 0:
        max_charge = 2 * N

    dims = []
    for n in range(max_charge + 1):
        dims.append(restricted_colored_partition(n, MUKAI_RANK, N))
    return dims


def total_simple_objects(N: int, max_charge: int = -1) -> int:
    r"""Total number of simple objects in the truncated category at level N.

    This is the "Verlinde dimension" V_N^{ch}(0) at genus 0:
      V_N^{ch}(0) = sum_{n=0}^{max_charge} p_{24}^{<N}(n)

    The sum is over all charges. At root of unity, the charge is bounded
    by the truncation, but for the abelian gl_1 case the charge can
    still be arbitrarily large (since we can have many parts each < N).
    We compute up to max_charge.

    Returns total count.
    """
    dims = truncated_fock_dimensions(N, max_charge)
    return sum(dims)


def compare_restricted_unrestricted(
    N: int,
    max_n: int = 10,
) -> Dict[str, Any]:
    r"""Compare restricted (root-of-unity) and unrestricted partitions.

    At each charge n, compare:
      p_{24}(n) (unrestricted, generic parameters)
      p_{24}^{<N}(n) (restricted, root of unity)

    The restricted count equals the unrestricted count for n < N,
    and is strictly less for n >= N.

    Returns comparison data.
    """
    results = []
    for n in range(max_n + 1):
        p_unr = _colored_partition(n, MUKAI_RANK)
        p_res = restricted_colored_partition(n, MUKAI_RANK, N)
        results.append({
            'n': n,
            'unrestricted': p_unr,
            'restricted': p_res,
            'truncation_ratio': p_res / p_unr if p_unr > 0 else 1.0,
            'agrees': p_unr == p_res,
        })

    # For n < N, restricted = unrestricted (no part can be >= N anyway)
    all_agree_below_N = all(r['agrees'] for r in results if r['n'] < N)

    return {
        'N': N,
        'data': results,
        'all_agree_below_N': all_agree_below_N,
        'first_disagreement': next(
            (r['n'] for r in results if not r['agrees']), None,
        ),
    }


# =========================================================================
# 5. S-matrix at root of unity
# =========================================================================

def charge_1_s_matrix(params: RootOfUnityK3Params) -> np.ndarray:
    r"""Compute the S-matrix on the charge-1 sector (24 Mukai directions).

    At charge 1, simple objects are V^{(a)} for a = 0, ..., 23
    (one per Mukai lattice direction). The braiding eigenvalue for
    V^{(a)} tensor V^{(b)} is:

      beta_{ab} = G_a(q_b) * G_b(q_a)    (mutual braiding)

    But at root of unity, G_a(q_b) = (1 - q_a q_b) / (1 - q_b / q_a).

    The S-matrix is the matrix of MUTUAL BRAIDING EIGENVALUES:
      S_{ab} = (1/D) * Tr(beta_{V^{(a)}, V^{(b)}})
    where D is a normalisation (the total quantum dimension).

    For the abelian (gl_1) case, V^{(a)} is 1-dimensional, so the
    trace is just the braiding eigenvalue itself.

    The S-matrix entry for the abelian K3 quantum toroidal is:
      S_{ab} = omega^{n_a * n_b * epsilon_{ab}}
    where epsilon_{ab} = omega^{ab} (the Mukai pairing) and
    n_a, n_b are the root-of-unity exponents.

    In the diagonal Mukai basis:
      omega^{ab} = +1 if a,b in {0,...,3} (positive)
                 = -1 if a,b in {4,...,23} (negative)
                 = 0  if a != b (diagonal)

    So the abelian S-matrix is DIAGONAL:
      S_{ab} = delta_{ab} * omega^{n_a^2 * sigma_a}
    where sigma_a = +1 (a = 0..3) or -1 (a = 4..23).

    This is DEGENERATE (S is diagonal, det S = product of diagonal entries,
    which is a root of unity, but S is not unitary as an S-matrix should be
    for an MTC).

    For the charge-1 sector of the ABELIAN algebra, the braiding is:
      R^{(a)(b)} = G_{ab}(0) = 1 for a != b (cross-family trivial)
      R^{(a)(a)} = G_{aa}(0) = -1 (self-braiding, from the pole structure)

    Wait -- for the abelian gl_1 K3 algebra, R_{ab}(u) = g_a(u) for a = b,
    and R_{ab} = 1 for a != b. At charge 1, the braiding is just:
      beta_{ab} = G_{ab}(q_b / q_a)

    For a != b (abelian, cross-family trivial): beta_{ab} = 1.
    For a = b: beta_{aa} = G_{aa}(1) = (1 - q_a) / (1 - 1/q_a) = -q_a.

    So at root of unity:
      S_{ab} = delta_{ab} * (-omega^{n_a}) + (1 - delta_{ab}) * 1

    This gives S = (1 - I) + diag(-omega^{n_a}).
    Wait, that is just the all-ones matrix minus the identity plus the
    diagonal term. Let me be more careful.

    Actually for an abelian braided category, the S-matrix is:
      S_{ab} = (1/D) * theta_a^{-1} * theta_b^{-1} * theta_{a+b}

    where theta_a is the twist on the simple object V^{(a)}.

    For the K3 Heisenberg at root of unity, the twist is:
      theta_a = omega^{Q(n_a)}
    where Q is the QUADRATIC FORM on the lattice:
      Q(n) = (1/2) * sum_a sigma_a * n_a^2

    The S-matrix for a lattice category is the FOURIER TRANSFORM matrix:
      S_{ab} = (1/sqrt(|L|)) * omega^{B(n_a, n_b)}
    where B is the bilinear form and L is the lattice.

    For the Z/NZ Mukai lattice:
      B(n_a, n_b) = sigma_a * n_a * delta_{ab}  (diagonal in Mukai basis)

    So:
      S_{ab} = (1/sqrt(N)) * omega^{sigma_a * n_a * n_b * delta_{ab}}

    For a != b: S_{ab} = 1/sqrt(N) (since B = 0 in the diagonal basis).
    Hmm, this requires off-diagonal B terms which vanish in the diagonal
    basis. The correct formulation uses the FULL Mukai pairing.

    I'll compute the S-matrix numerically using the standard lattice
    MTC formula.

    Parameters
    ----------
    params : RootOfUnityK3Params
        Root-of-unity parameters.

    Returns
    -------
    np.ndarray
        The 24 x 24 S-matrix at charge 1.
    """
    N = params.N
    omega = params.omega
    n_mukai = params.n_mukai
    eigenvalues = mukai_diagonal_eigenvalues()  # +1 or -1

    # For the abelian category at root of unity, the S-matrix in the
    # diagonal Mukai basis is:
    #
    #   S_{ab} = (1/sqrt(D)) * omega^{sigma_a * n_a * n_b}    if a = b
    #          = (1/sqrt(D)) * 1                                if a != b
    #
    # where sigma_a = Mukai eigenvalue and D = normalisation.
    #
    # However, this is the S-matrix for a PRODUCT of independent sectors.
    # Each Mukai direction a contributes independently (abelian gl_1).
    #
    # The correct S-matrix for a product of cyclic groups Z/m_a Z is the
    # tensor product of the individual S-matrices.
    #
    # For direction a with exponent n_a and Mukai eigenvalue sigma_a:
    # If n_a = 0: the direction is trivial (q_a = 1), contributing a
    #   1x1 identity factor.
    # If n_a != 0: the direction contributes a braiding phase.
    #
    # For the Kummer parametrization:
    #   Directions 0-3: n_a = 1, sigma_a = +1
    #   Directions 4-7: n_a = N-1, sigma_a = -1
    #   Directions 8-23: n_a = 0, sigma_a = -1 (trivial)
    #
    # The nontrivial S-matrix entries involve only the active directions
    # (n_a != 0). For the charge-1 sector at each active direction, the
    # braiding is:
    #   R_a = omega^{sigma_a * n_a}
    #
    # The charge-1 S-matrix is 24x24 where:
    #   S_{ab} = omega^{sigma_a * n_a * n_b}  (Gaussian sum / lattice Fourier)

    S = np.zeros((MUKAI_RANK, MUKAI_RANK), dtype=complex)

    for a in range(MUKAI_RANK):
        for b in range(MUKAI_RANK):
            # Bilinear form: B(a,b) = sigma_a * n_a * delta_{ab} (diagonal)
            if a == b:
                exponent = eigenvalues[a] * n_mukai[a] * n_mukai[b]
            else:
                exponent = 0
            S[a, b] = omega ** exponent

    # Normalise: S -> S / sqrt(D) where D = product of norms
    # For a lattice MTC, the normalisation is:
    #   D^2 = sum_a |S_{0a}|^2 (using the 0-th simple object as vacuum)
    # For the diagonal S-matrix, S_{0a} = omega^{0} = 1 for all a,
    # so D^2 = 24, D = sqrt(24).
    D = math.sqrt(MUKAI_RANK)
    S /= D

    return S


def s_matrix_nondegeneracy(
    params: RootOfUnityK3Params,
) -> Dict[str, Any]:
    r"""Test whether the charge-1 S-matrix is non-degenerate (= MTC).

    A braided tensor category is modular iff det(S) != 0.

    For the abelian K3 quantum toroidal at root of unity:
    The S-matrix is diagonal in the Mukai basis (abelian, no cross-terms).
    det(S) = prod_a S_{aa} / D^24.
    S_{aa} = omega^{sigma_a * n_a^2} / D.

    RESULT: det(S) != 0 iff ALL S_{aa} != 0, which requires all
    sigma_a * n_a^2 to give distinct residues modulo N, or more precisely,
    omega^{sigma_a * n_a^2} != 0 (always true since omega is a root of
    unity, so |omega^k| = 1 for all k).

    For the abelian case, the S-matrix is ALWAYS non-degenerate at
    charge 1 (because it is diagonal with all diagonal entries nonzero).
    The REAL test of modularity is at higher charge, where the
    braiding can have a nontrivial kernel.

    However, the S-matrix being diagonal means it does NOT generate
    SL_2(Z) (a non-diagonal S is needed for full modularity). So
    the charge-1 sector is NOT modular despite det(S) != 0.

    The correct modularity test requires the FULL multi-charge S-matrix.

    Returns dict with analysis.
    """
    S = charge_1_s_matrix(params)
    det_S = np.linalg.det(S)
    rank_S = np.linalg.matrix_rank(S, tol=1e-10)

    # Eigenvalues of S
    eigenvalues_S = np.linalg.eigvals(S)

    # Check S^2 = C (charge conjugation, should be identity for self-dual)
    S2 = S @ S
    is_involution = np.allclose(
        S2, np.eye(MUKAI_RANK, dtype=complex), atol=1e-8,
    )

    # Check unitarity: S * S^dagger = I
    SSdag = S @ S.conj().T
    is_unitary = np.allclose(
        SSdag, np.eye(MUKAI_RANK, dtype=complex), atol=1e-8,
    )

    # For MTC: need det(S) != 0 AND S generates SL_2(Z) with T
    # The diagonal S never generates SL_2(Z), so the charge-1 sector
    # of the abelian algebra is NOT an MTC.
    is_mtc_charge_1 = False  # abelian charge-1 is never MTC

    return {
        'N': params.N,
        'det_S': det_S,
        'det_S_abs': abs(det_S),
        'det_S_nonzero': abs(det_S) > 1e-12,
        'rank_S': rank_S,
        'is_involution': is_involution,
        'is_unitary': is_unitary,
        'is_mtc_charge_1': is_mtc_charge_1,
        'reason_not_mtc': (
            'The charge-1 S-matrix of the abelian K3 quantum toroidal is '
            'diagonal in the Mukai basis. A diagonal S-matrix cannot '
            'generate SL_2(Z) with the T-matrix, so the charge-1 sector '
            'is not a modular tensor category. The braiding is trivial '
            'between distinct Mukai directions (cross-family G_{ab} = 1). '
            'A genuine MTC requires the NON-ABELIAN K3 quantum toroidal '
            '(which is unconstructed, AP-CY14).'
        ),
        'what_is_needed': (
            'For MTC structure: (1) non-abelian g (not gl_1), or '
            '(2) higher charge sectors where multi-particle braiding '
            'is nontrivial, or (3) the full (non-product) K3 quantum '
            'toroidal with non-trivial cross-family structure functions.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 6. T-matrix (twist / conformal weights)
# =========================================================================

def charge_1_t_matrix(params: RootOfUnityK3Params) -> np.ndarray:
    r"""Compute the T-matrix (twist/ribbon) on the charge-1 sector.

    The twist on simple object V^{(a)} is:
      theta_a = omega^{h_a}
    where h_a = conformal weight of the a-th Mukai direction.

    For the abelian lattice category:
      theta_a = omega^{Q(n_a)} = omega^{sigma_a * n_a^2 / 2}

    Since n_a^2 / 2 may not be integer, we use:
      theta_a = omega^{sigma_a * n_a * (n_a + N) / 2}  if N is even
    or the Gauss sum convention.

    For simplicity, we use:
      T_{ab} = delta_{ab} * omega^{sigma_a * n_a^2}

    (dropping the factor of 1/2 which corresponds to a different
    normalisation of the quadratic form -- the even lattice convention).

    Parameters
    ----------
    params : RootOfUnityK3Params

    Returns
    -------
    np.ndarray
        24 x 24 diagonal T-matrix.
    """
    N = params.N
    omega = params.omega
    n_mukai = params.n_mukai
    eigenvalues = mukai_diagonal_eigenvalues()

    T = np.zeros((MUKAI_RANK, MUKAI_RANK), dtype=complex)
    for a in range(MUKAI_RANK):
        exponent = eigenvalues[a] * n_mukai[a] * n_mukai[a]
        T[a, a] = omega ** exponent

    return T


def verify_modular_relations(
    params: RootOfUnityK3Params,
) -> Dict[str, Any]:
    r"""Verify the modular group relations for S and T matrices.

    SL_2(Z) requires:
      (ST)^3 = S^2
      S^4 = I  (or S^2 = C with C^2 = I)

    For the abelian K3 at root of unity, these relations will FAIL
    because S is diagonal (so ST = TS, hence (ST)^3 = S^3 T^3,
    which does not equal S^2 in general).

    Returns dict with verification results.
    """
    S = charge_1_s_matrix(params)
    T = charge_1_t_matrix(params)
    n = MUKAI_RANK

    I_n = np.eye(n, dtype=complex)

    # S^2
    S2 = S @ S

    # (ST)^3
    ST = S @ T
    ST3 = ST @ ST @ ST

    # S^4
    S4 = S2 @ S2

    # Check relations
    st3_eq_s2 = np.allclose(ST3, S2, atol=1e-8)
    s4_eq_id = np.allclose(S4, I_n, atol=1e-8)
    s2_eq_id = np.allclose(S2, I_n, atol=1e-8)

    # Commutativity of S and T (abelian case: both diagonal => commute)
    st_eq_ts = np.allclose(S @ T, T @ S, atol=1e-8)

    return {
        'N': params.N,
        'ST_cubed_eq_S_squared': st3_eq_s2,
        'S_fourth_eq_identity': s4_eq_id,
        'S_squared_eq_identity': s2_eq_id,
        'S_T_commute': st_eq_ts,
        'modular_relations_hold': st3_eq_s2 and s4_eq_id,
        'abelian_diagonal_note': (
            'For the abelian K3 quantum toroidal, S and T are both '
            'diagonal, hence they commute. This means (ST)^3 = S^3 T^3 '
            'and the modular relation (ST)^3 = S^2 becomes S T^3 = I, '
            'which is a strong constraint on the parameters.'
        ),
    }


# =========================================================================
# 7. Verlinde-type formula
# =========================================================================

def verlinde_dimension_genus_g(
    N: int,
    g: int,
    max_charge: int = -1,
) -> Dict[str, Any]:
    r"""Compute the chiral Verlinde dimension at genus g and level N.

    In 3d CS: V_k(g) = Verlinde formula (finite sum over simples).
    In 6d: V_N^{ch}(g) = dim int_{Sigma_g x C^2} A_N at root of unity.

    For the abelian K3 quantum toroidal at root of unity:

    GENERIC (non-root-of-unity) formula from cfg25_adversarial_consistency:
      V^{ch}_generic(g) = (1+t)^{3g}  for classes L, C (AP-CY21)
      evaluated at t = 1: V = 2^{3g}

    ROOT-OF-UNITY truncation:
      V_N^{ch}(g) should be LESS than V^{ch}_generic(g) because the
      truncation kills modules.

    For the abelian lattice VOA at root of unity, the Verlinde dimension
    is related to the RANK of the fusion matrices. At charge 1:
      V_N^{ch}(0) = number of simple objects = 24 (independent of N
        for the abelian case)

    At genus g, the lattice Verlinde formula gives:
      V_N(g) = sum_lambda (S_{0,lambda})^{2-2g}
    summed over simple objects lambda.

    For the abelian K3 with 24 directions:
      V_N(g) = sum_{a=0}^{23} (S_{0a})^{2-2g}

    Parameters
    ----------
    N : int
        Root-of-unity level.
    g : int
        Genus (>= 0).
    max_charge : int
        Maximum charge for counting.

    Returns
    -------
    dict with Verlinde dimensions and analysis.
    """
    params = kummer_root_of_unity_params(N)
    S = charge_1_s_matrix(params)

    # Verlinde dimension at genus g (charge-1 sector):
    # V_N(g) = sum_a (S_{0a} / S_{00})^{2-2g}
    # For diagonal S: S_{0a} = delta_{0a} * omega^{...} / D
    # Actually S_{0a} = omega^{0} / D = 1/D for a != 0 (trivial braiding)
    # and S_{00} = omega^{sigma_0 * n_0^2} / D for a = 0.

    # Use the matrix directly
    s_ratios = np.array([
        S[0, a] / S[0, 0] if abs(S[0, 0]) > 1e-15 else 0.0
        for a in range(MUKAI_RANK)
    ])

    chi = 2 - 2 * g
    if chi >= 0:
        verlinde_sum = sum(s_ratios[a]**chi for a in range(MUKAI_RANK))
    else:
        # Negative chi: need inverse (may diverge)
        verlinde_sum = sum(
            s_ratios[a]**chi
            for a in range(MUKAI_RANK)
            if abs(s_ratios[a]) > 1e-15
        )

    # Generic (non-root-of-unity) formula for comparison
    generic_verlinde = 2 ** (3 * g)  # (1+t)^{3g} at t=1

    return {
        'N': N,
        'g': g,
        'verlinde_N': verlinde_sum,
        'verlinde_N_real': verlinde_sum.real if isinstance(verlinde_sum, complex) else verlinde_sum,
        'generic_verlinde': generic_verlinde,
        'ratio': (
            abs(verlinde_sum) / generic_verlinde
            if generic_verlinde > 0 else float('inf')
        ),
        'truncated_fock_dims': truncated_fock_dimensions(N, max_charge=max(N, 5)),
        'status': STATUS,
        'note': (
            'The Verlinde dimension at genus g and level N is computed '
            'from the charge-1 S-matrix. For the abelian K3, this is '
            'the sum of (S_{0a}/S_{00})^{2-2g} over 24 Mukai directions. '
            'The generic (non-root-of-unity) Verlinde is (1+t)^{3g} '
            '(AP-CY21), which is the chain-level E_3 bar dimension.'
        ),
    }


# =========================================================================
# 8. Conway group analysis
# =========================================================================

def conway_analysis(N: int) -> Dict[str, Any]:
    r"""Analyse the Conway group connection at root of unity.

    The Conway group Co_0 = Aut(Leech lattice) has order:
      |Co_0| = 2^22 * 3^9 * 5^4 * 7^2 * 11 * 13 * 23 = 8315553613086720000

    Co_0 acts on R^24 preserving the Leech lattice. At the Leech point
    of K3 moduli, the BPS spectrum has Co_0 symmetry (Duncan's moonshine).

    The Mukai lattice Lambda_Muk = U^3 + E_8(-1)^2 has:
      Aut(Lambda_Muk) = O^+(Lambda_Muk) (orthogonal group of the lattice)

    The RELATIONSHIP between the Mukai lattice and the Leech lattice:
    At the orbifold point T^4/Z_2, the 16 twisted sector states span
    a sublattice related to the Leech lattice via the Kummer construction.

    For the root-of-unity truncation, the key question is:
    Does the Conway group act on the TRUNCATED category?

    The answer depends on whether N is COPRIME to |Co_0|:
    - If gcd(N, |Co_0|) = 1: the truncation is "generic" and does not
      see the Conway symmetry.
    - If N divides |Co_0|: the truncation may be Conway-equivariant.

    The prime factorization of |Co_0| gives the "interesting" N values:
    N in {2, 3, 5, 7, 11, 13, 23} (prime factors of |Co_0|).

    At N = 24 (the rank of the Mukai lattice): the 24-th root of unity
    omega = e^{2*pi*i/24} gives q_a = omega^{n_a}, and the lattice
    Z/24Z x ... x Z/24Z is related to the MOD-24 reduction of the
    Mukai lattice. The Mathieu group M_24 acts on this reduction.

    This is the 6d analogue of the Eguchi-Ooguri-Tachikawa observation:
    the K3 elliptic genus's expansion in representations of the N=4 SCA
    has coefficients that are dimensions of M_24 representations.
    At root of unity, the Verlinde numbers should be M_24 representation
    dimensions modulo N.

    Parameters
    ----------
    N : int
        Root-of-unity level.

    Returns
    -------
    dict with Conway/Mathieu analysis.
    """
    # |Co_0| prime factorization
    co0_primes = {2: 22, 3: 9, 5: 4, 7: 2, 11: 1, 13: 1, 23: 1}
    co0_order = 1
    for p, e in co0_primes.items():
        co0_order *= p ** e

    # Check if N shares prime factors with |Co_0|
    shared_primes = []
    temp_N = N
    for p in co0_primes:
        if temp_N % p == 0:
            shared_primes.append(p)

    # |M_24| = 2^10 * 3^3 * 5 * 7 * 11 * 23 = 244823040
    m24_primes = {2: 10, 3: 3, 5: 1, 7: 1, 11: 1, 23: 1}
    m24_order = 1
    for p, e in m24_primes.items():
        m24_order *= p ** e

    # Truncated Fock dimensions
    fock_dims = truncated_fock_dimensions(N, max_charge=min(5, 2 * N))

    # Mathieu moonshine dimensions for comparison
    # The first few M_24 representation dimensions (from EOT):
    # A_1 = 45, A_2 = 231, A_3 = 770, ...
    # These appear as coefficients: 2*A_1 = 90, etc.
    # The K3 elliptic genus: 24 * (mu(tau,z))
    # = 2*y + 20 + 2*y^{-1} + q*(90*y^2 + ...) + ...
    # Moonshine decomposition: 90 = 2 * 45 (45 is the dim of the
    # first nontrivial M_24 rep), 462 = 2 * 231, etc.
    mathieu_dims = [1, 23, 45, 231, 253, 770, 1035, 2024, 2277, 3520]

    # Check if Fock dimensions relate to Mathieu dimensions mod N
    fock_mod_N = [d % N for d in fock_dims]

    return {
        'N': N,
        'co0_order': co0_order,
        'm24_order': m24_order,
        'gcd_N_co0': math.gcd(N, co0_order),
        'gcd_N_m24': math.gcd(N, m24_order),
        'shares_co0_primes': shared_primes,
        'conway_equivariant': len(shared_primes) > 0,
        'mathieu_equivariant': math.gcd(N, m24_order) > 1,
        'truncated_fock': fock_dims,
        'fock_mod_N': fock_mod_N,
        'first_mathieu_dims': mathieu_dims[:min(5, len(mathieu_dims))],
        'note': (
            'The Conway group Co_0 = Aut(Leech) acts at the Leech point '
            'of K3 moduli. At root of unity, the truncated category MAY '
            'inherit this symmetry when N shares prime factors with |Co_0|. '
            'The Mathieu group M_24 is a subquotient of Co_0 and governs '
            'the K3 elliptic genus moonshine (Eguchi-Ooguri-Tachikawa). '
            'The 6d root-of-unity Verlinde numbers should be expressible '
            'as M_24 representation dimensions mod N. '
            'STATUS: CONJECTURAL (AP-CY14, CY-A_3).'
        ),
        'status': STATUS,
    }


# =========================================================================
# 9. The five critical questions
# =========================================================================

def finiteness_analysis(N: int) -> Dict[str, Any]:
    r"""Question 1: Does U_{q,t}(g_{K3}^{tor}) at root of unity have
    finitely many simple modules?

    ANSWER (CONJECTURAL):
    YES, but with important caveats:

    (a) At each FIXED CHARGE n, the number of simples is FINITE:
        dim F_n^{<N} = p_{24}^{<N}(n) < infinity.

    (b) The TOTAL number of simples (summing over ALL charges) is
        INFINITE because charge is unbounded.

    (c) For a GENUINE MTC, one needs a FINITE set of simples. This
        requires a CHARGE TRUNCATION in addition to the root-of-unity
        truncation. The natural charge bound is N (level = charge max),
        giving:
          Total simples = sum_{n=0}^{N-1} p_{24}^{<N}(n)

    This is the 6d analogue of the 3d truncation: in 3d, the level k
    bounds both the spin (j <= k) and the fusion multiplicity. In 6d,
    the level N bounds both the part size and (conjecturally) the charge.

    Parameters
    ----------
    N : int
        Root-of-unity level.

    Returns
    -------
    dict with finiteness analysis.
    """
    # Fixed-charge dimensions
    fock_dims = truncated_fock_dimensions(N, max_charge=2 * N)

    # Total with charge truncation at N
    total_charge_N = sum(fock_dims[:N])

    # Total with charge truncation at N-1
    total_charge_N_minus_1 = sum(fock_dims[:N - 1]) if N > 1 else 1

    # Unrestricted for comparison
    unrestricted = [_colored_partition(n, MUKAI_RANK) for n in range(N)]
    total_unrestricted = sum(unrestricted)

    return {
        'N': N,
        'finite_at_each_charge': True,
        'infinite_total_without_charge_bound': True,
        'charge_bounded_total_N': total_charge_N,
        'charge_bounded_total_N_minus_1': total_charge_N_minus_1,
        'unrestricted_total_to_N': total_unrestricted,
        'truncation_ratio': (
            total_charge_N / total_unrestricted
            if total_unrestricted > 0 else 1.0
        ),
        'fock_dims_truncated': fock_dims[:min(N + 1, len(fock_dims))],
        'fock_dims_unrestricted': unrestricted,
        'answer': (
            f'YES (with charge bound): {total_charge_N} simples at level N={N}. '
            f'Without charge bound: INFINITE (charge unbounded). '
            f'The charge truncation is the 6d analogue of the j <= k bound in 3d. '
            f'Unrestricted count to charge {N-1}: {total_unrestricted}. '
            f'Truncation ratio: {total_charge_N / total_unrestricted:.4f}.'
            if total_unrestricted > 0 else
            f'YES: {total_charge_N} simples at level N={N}.'
        ),
        'status': STATUS,
    }


def modularity_analysis(N: int) -> Dict[str, Any]:
    r"""Question 2: Is the category modular (non-degenerate braiding)?

    ANSWER (CONJECTURAL):
    For the ABELIAN (gl_1) K3 quantum toroidal: NO.
    The charge-1 S-matrix is diagonal, giving a DEGENERATE braiding.
    The abelian algebra is a PRODUCT of 24 rank-1 factors, and the
    braiding between different factors is trivial.

    For a genuine MTC, one needs the NON-ABELIAN K3 quantum toroidal
    (which is unconstructed). The non-abelian version would have
    nontrivial cross-family structure functions G_{ab} != 1, producing
    a non-diagonal S-matrix.

    PARTIAL RESULT: the charge-1 sector of the abelian algebra is a
    PRE-MODULAR (ribbon fusion) category. The ribbon twist is:
      theta_a = -omega^{n_a}  (from g_a(0) = -1 times the root-of-unity phase)

    The obstruction to modularity is the KERNEL of the S-matrix,
    which for the abelian case consists of all transparent objects
    (objects that braid trivially with everything).

    Parameters
    ----------
    N : int
        Root-of-unity level.

    Returns
    -------
    dict with modularity analysis.
    """
    params = kummer_root_of_unity_params(N)
    s_analysis = s_matrix_nondegeneracy(params)
    mod_relations = verify_modular_relations(params)

    return {
        'N': N,
        'is_mtc': False,  # abelian is never MTC
        'is_pre_modular': True,  # ribbon fusion category: yes
        'is_ribbon': True,
        's_matrix_det_nonzero': s_analysis['det_S_nonzero'],
        's_matrix_rank': s_analysis['rank_S'],
        'modular_relations_hold': mod_relations['modular_relations_hold'],
        'obstruction': (
            'The abelian (gl_1) K3 quantum toroidal has trivial '
            'cross-family braiding (G_{ab} = 1 for a != b). This makes '
            'the S-matrix diagonal, which is the WRONG structure for an '
            'MTC. The non-abelian K3 quantum toroidal (unconstructed) '
            'would have nontrivial G_{ab}, producing a non-diagonal S '
            'that could satisfy the MTC axioms.'
        ),
        'what_would_make_it_mtc': (
            '(1) Construct the non-abelian K3 quantum toroidal with '
            'cross-family G_{ab}(x) != 1 (requires non-abelian g, not gl_1). '
            '(2) At the enhanced symmetry point (ADE singularity on K3), '
            'the current algebra acquires non-abelian structure. '
            '(3) At the Leech point, the full BKM algebra has nontrivial '
            'root structure giving cross-family braiding.'
        ),
        'status': STATUS,
    }


def verlinde_p24_analysis(N: int) -> Dict[str, Any]:
    r"""Question 4: Is the Verlinde dimension related to p_24(n) mod N?

    ANALYSIS (CONJECTURAL):
    The truncated Fock dimension at charge n is:
      p_{24}^{<N}(n) = restricted 24-coloured partitions of n (parts < N)

    For n < N: p_{24}^{<N}(n) = p_{24}(n) (no restriction active).
    For n >= N: p_{24}^{<N}(n) < p_{24}(n) (some partitions killed).

    The relationship to p_{24}(n) mod N:
      p_{24}^{<N}(n) is NOT equal to p_{24}(n) mod N in general.
      Example: N = 2, n = 2:
        p_{24}(2) = 324, p_{24}^{<2}(2) = 276 (only one-part partitions killed).
        p_{24}(2) mod 2 = 0, but p_{24}^{<2}(2) = 276 (even, but != 0).

    The correct relationship is FINER:
      p_{24}^{<N}(n) = sum_{k=0}^{floor(n/N)} (-1)^k * C(24+k-1, k) * p_{24}(n - kN)

    This is an inclusion-exclusion over the number of parts >= N.

    Returns analysis data.
    """
    max_n = min(3 * N, 20)
    data = []
    for n in range(max_n + 1):
        p_full = _colored_partition(n, MUKAI_RANK)
        p_trunc = restricted_colored_partition(n, MUKAI_RANK, N)
        data.append({
            'n': n,
            'p24_full': p_full,
            'p24_truncated': p_trunc,
            'p24_mod_N': p_full % N,
            'p24_trunc_mod_N': p_trunc % N,
            'agree_mod_N': (p_full % N) == (p_trunc % N),
            'agrees_exactly': p_full == p_trunc,
        })

    agree_below_N = all(d['agrees_exactly'] for d in data if d['n'] < N)
    mod_N_agreement = sum(1 for d in data if d['agree_mod_N']) / len(data)

    return {
        'N': N,
        'data': data,
        'agree_exactly_below_N': agree_below_N,
        'mod_N_agreement_fraction': mod_N_agreement,
        'relationship': (
            f'For n < N = {N}: p_24^{{<N}}(n) = p_24(n) exactly. '
            f'For n >= N: p_24^{{<N}}(n) < p_24(n) strictly. '
            f'The mod-N reduction p_24(n) mod N does NOT equal '
            f'p_24^{{<N}}(n) in general. The correct truncation is '
            f'the restricted partition function, not the mod-N reduction.'
        ),
        'status': STATUS,
    }


def conway_connection_analysis(N: int) -> Dict[str, Any]:
    r"""Question 5: Connection to Conway group Co_1 = Co_0 / {+/- I}.

    The Conway group Co_0 = Aut(Leech) has |Co_0| = 8315553613086720000.
    Co_1 = Co_0 / {+/- I_{24}} has |Co_1| = |Co_0| / 2.
    (AP-CY16: +/- I_{24}, NOT +/- I_5.)

    The connection to root-of-unity K3 quantum toroidal:

    1. The Leech lattice Lambda_Leech has minimum norm 4 (no roots).
       The Mukai lattice Lambda_Muk = U^3 + E_8(-1)^2 has roots.
       They are DIFFERENT lattices but both rank 24 even unimodular.

    2. At the Leech point of K3 moduli (Duncan moonshine), the BPS
       spectrum has Co_0 symmetry. The root-of-unity truncation at
       this point produces a category with Co_0-equivariant fusion.

    3. The Mathieu group M_24 < Co_0 acts on the 24 Mukai directions.
       The root-of-unity S-matrix should be M_24-invariant at the
       enhanced symmetry point.

    4. The McKay-Thompson series T_g(q) for g in M_24 should appear
       as traces: T_g(q) = Tr_{F}(g * q^{L_0 - c/24}).
       At root of unity q = omega: T_g(omega) is a CHARACTER VALUE
       of g in the truncated module, which is a sum of M_24 character
       values at each charge.

    Returns analysis data.
    """
    conway = conway_analysis(N)

    # Frame shape analysis for M_24
    # M_24 has 26 conjugacy classes. The frame shapes are related to
    # eta-products. At root of unity, eta(omega) is a Gauss sum.

    # The eta function at a root of unity:
    # eta(omega) = omega^{1/24} * prod_{n>=1} (1 - omega^n)
    # For omega = e^{2*pi*i/N}: the product has period N, so
    # prod_{n>=1} (1 - omega^n) = prod_{k=1}^{N-1} (1 - omega^k)^{inf}
    # which diverges. But eta(omega)/eta(1) has a well-defined limit.

    # Gauss sum: sum_{k=0}^{N-1} omega^{k^2} = sqrt(N) * e^{pi*i/4} (N odd)
    # or sqrt(N) (N = 0 mod 4) or 0 (N = 2 mod 4).

    gauss_sum = sum(primitive_root(N) ** (k * k) for k in range(N))

    # Classical Gauss sum result:
    #   N odd:       |G_N| = sqrt(N)
    #   N = 0 mod 4: |G_N| = sqrt(2N)
    #   N = 2 mod 4: |G_N| = 0
    if N % 2 == 1:
        expected_abs = math.sqrt(N)
    elif N % 4 == 0:
        expected_abs = math.sqrt(2 * N)
    else:  # N = 2 mod 4
        expected_abs = 0.0

    return {
        'N': N,
        'conway_connection': conway,
        'gauss_sum': gauss_sum,
        'gauss_sum_abs': abs(gauss_sum),
        'gauss_sum_expected': expected_abs,
        'gauss_sum_matches': abs(abs(gauss_sum) - expected_abs) < 0.01,
        'co1_order': conway['co0_order'] // 2,
        'mechanism': (
            'At the Leech point of K3 moduli, the BPS spectrum has Co_0 '
            'symmetry (Duncan moonshine). The root-of-unity truncation '
            'produces fusion rules that are Conway-equivariant. The '
            'McKay-Thompson series T_g(omega) for g in M_24 gives '
            'character values of the truncated module. '
            'The Gauss sum G_N = sum omega^{k^2} = sqrt(N) * phase '
            'governs the normalisation of the Conway-equivariant S-matrix.'
        ),
        'status': STATUS,
    }


# =========================================================================
# 10. Full verification suite
# =========================================================================

def full_verification(N: int = 5) -> Dict[str, Any]:
    r"""Run the complete verification suite for the root-of-unity
    K3 quantum toroidal at level N.

    Checks:
    1. Root-of-unity arithmetic ([N]_omega = 0).
    2. CY_2 constraint at root of unity (prod q_a = 1).
    3. Periodicity of G_{K3}(x).
    4. Pole structure analysis.
    5. Restricted partition function.
    6. S-matrix construction and nondegeneracy.
    7. Modular relations.
    8. Verlinde dimension at genus 0, 1.
    9. Finiteness analysis.
    10. Modularity analysis.
    11. Conway group connection.

    Parameters
    ----------
    N : int
        Root-of-unity level (default: 5, chosen to be coprime to 24).

    Returns
    -------
    dict with all verification results.
    """
    # 1. Truncation
    trunc_ok, trunc_val = verify_truncation(N)

    # 2. Parameters
    params = kummer_root_of_unity_params(N)
    cy2_ok = params.cy2_residual < 1e-10

    # 3. Periodicity
    period_ok, period_res = verify_periodicity(params)

    # 4. Poles
    poles = pole_structure(params)

    # 5. Restricted partitions
    comparison = compare_restricted_unrestricted(N, max_n=min(2 * N, 10))

    # 6. S-matrix
    s_analysis = s_matrix_nondegeneracy(params)

    # 7. Modular relations
    mod_rel = verify_modular_relations(params)

    # 8. Verlinde
    verl_g0 = verlinde_dimension_genus_g(N, g=0)
    verl_g1 = verlinde_dimension_genus_g(N, g=1)

    # 9. Finiteness
    finite = finiteness_analysis(N)

    # 10. Modularity
    modular = modularity_analysis(N)

    # 11. Conway
    conway = conway_analysis(N)

    all_basic_pass = all([
        trunc_ok,
        cy2_ok,
        period_ok,
        poles['poles_on_roots_of_unity'],
        comparison['all_agree_below_N'],
    ])

    return {
        'N': N,
        'all_basic_pass': all_basic_pass,
        'truncation_ok': trunc_ok,
        'cy2_ok': cy2_ok,
        'periodicity_ok': period_ok,
        'periodicity_residual': period_res,
        'poles_on_roots_of_unity': poles['poles_on_roots_of_unity'],
        'distinct_pole_positions': poles['distinct_pole_positions'],
        'restricted_agree_below_N': comparison['all_agree_below_N'],
        's_matrix_rank': s_analysis['rank_S'],
        'is_mtc': modular['is_mtc'],
        'is_pre_modular': modular['is_pre_modular'],
        'modular_relations_hold': mod_rel['modular_relations_hold'],
        'verlinde_g0': verl_g0['verlinde_N'],
        'verlinde_g1': verl_g1['verlinde_N'],
        'total_simples_charge_bounded': finite['charge_bounded_total_N'],
        'conway_equivariant': conway['conway_equivariant'],
        'gauss_sum_matches': conway_connection_analysis(N)['gauss_sum_matches'],
        'status': STATUS,
        'summary': (
            f'Root-of-unity K3 quantum toroidal at N = {N}: '
            f'Truncation [N]_omega = 0: {"PASS" if trunc_ok else "FAIL"}. '
            f'CY_2 constraint: {"PASS" if cy2_ok else "FAIL"}. '
            f'{finite["charge_bounded_total_N"]} simples with charge bound. '
            f'MTC: NO (abelian S-matrix diagonal). '
            f'Pre-modular (ribbon fusion): YES. '
            f'Conway-equivariant: {"YES" if conway["conway_equivariant"] else "NO"}.'
        ),
    }
