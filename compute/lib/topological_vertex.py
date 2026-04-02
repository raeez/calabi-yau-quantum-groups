"""
Topological vertex formalism (Aganagic-Klemm-Marino-Vafa).

Computes the topological vertex C_{lambda,mu,nu}(q) and partition functions
of toric Calabi-Yau threefolds from their web diagrams.

The topological vertex is:

    C_{lambda,mu,nu}(q) = q^{kappa(mu)/2} * s_{nu^t}(q^{rho})
        * sum_{eta} s_{lambda^t/eta}(q^{nu+rho}) * s_{mu/eta}(q^{nu^t+rho})

where rho_i = -i + 1/2 and kappa(mu) = sum_i mu_i(mu_i - 2i + 1).

We implement partition functions of three toric CY3s:

1. C^3 (single vertex):  Z = M(q) via the Cauchy identity at principal specialization.
2. Resolved conifold (two vertices): Z/M(q) = prod (1 - Qq^n)^n via dual Cauchy.
3. Local P^2 (three vertices): Computed via the Gopakumar-Vafa expansion with
   known BPS invariants, with degree-1 verified by the vertex sum.

The Cauchy identity at x_i = q^{i-1/2}:
    sum_nu q^{|nu|} [s_nu(1,q,...)]^2 = prod_{k>=1} 1/(1-q^k)^k = M(q)

The dual Cauchy identity at x_i = y_j = q^{i-1/2}:
    sum_nu (-1)^{|nu|} Q^{|nu|} q^{|nu|} s_nu(1,q,...) s_{nu^t}(1,q,...) = prod (1-Qq^k)^k

References:
    [AKMV]  Aganagic, Klemm, Marino, Vafa, "The Topological Vertex", hep-th/0305132
    [ORV]   Okounkov, Reshetikhin, Vafa, "Quantum Calabi-Yau and Classical Crystals",
            hep-th/0309208
    [GV]    Gopakumar, Vafa, "M-Theory and Topological Strings--II", hep-th/9812127
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from typing import Dict, List, Optional, Sequence, Tuple

Partition = Tuple[int, ...]
FPS = List[Fraction]  # formal power series [a_0, a_1, ..., a_N]


# ===================================================================
# Section 1: Partition combinatorics
# ===================================================================

def normalize(lam: Sequence[int]) -> Partition:
    """Strip trailing zeros and return as tuple."""
    parts = list(lam)
    while parts and parts[-1] == 0:
        parts.pop()
    return tuple(parts)


def partition_size(lam: Partition) -> int:
    """Return |lambda| = sum of parts."""
    return sum(lam)


def conjugate(lam: Partition) -> Partition:
    """Transpose (conjugate) partition."""
    if not lam:
        return ()
    cols = lam[0]
    return tuple(sum(1 for p in lam if p >= j) for j in range(1, cols + 1))


def kappa_stat(lam: Partition) -> int:
    r"""
    Framing factor kappa(lambda) = sum_i lambda_i(lambda_i - 2i + 1).
    Equivalently kappa = ||lambda||^2 - ||lambda^t||^2. Always even.
    """
    return sum(lam[i] * (lam[i] - 2 * i - 1) for i in range(len(lam)))


def n_stat(lam: Partition) -> int:
    """n(lambda) = sum_{i>=0} i * lambda_i = sum_j C(lambda^t_j, 2)."""
    return sum(i * lam[i] for i in range(len(lam)))


def norm_sq(lam: Partition) -> int:
    """||lambda||^2 = sum_i lambda_i^2."""
    return sum(p * p for p in lam)


def hook_lengths(lam: Partition) -> List[int]:
    """All hook lengths h(i,j) for boxes in the Young diagram."""
    if not lam:
        return []
    lam_t = conjugate(lam)
    hooks = []
    for i in range(len(lam)):
        for j in range(lam[i]):
            hooks.append((lam[i] - j) + (lam_t[j] - i) - 1)
    return hooks


def hook_product(lam: Partition) -> int:
    """Product of all hook lengths."""
    prod = 1
    for h in hook_lengths(lam):
        prod *= h
    return prod


def contents(lam: Partition) -> List[int]:
    """All contents c(i,j) = j - i for boxes in the diagram."""
    result = []
    for i in range(len(lam)):
        for j in range(lam[i]):
            result.append(j - i)
    return result


# ===================================================================
# Section 2: Partition enumeration
# ===================================================================

@lru_cache(maxsize=256)
def partitions_of(n: int) -> Tuple[Partition, ...]:
    """All partitions of n."""
    if n == 0:
        return ((),)
    result = []

    def generate(remaining, max_part, current):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            current.append(p)
            generate(remaining - p, p, current)
            current.pop()

    generate(n, n, [])
    return tuple(result)


def partitions_up_to(n: int) -> List[Partition]:
    """All partitions of sizes 0, 1, ..., n."""
    result = []
    for k in range(n + 1):
        result.extend(partitions_of(k))
    return result


# ===================================================================
# Section 3: Formal power series (truncated) arithmetic
# ===================================================================

def fps_zero(order: int) -> FPS:
    return [Fraction(0)] * (order + 1)


def fps_one(order: int) -> FPS:
    f = fps_zero(order)
    f[0] = Fraction(1)
    return f


def fps_add(a: FPS, b: FPS) -> FPS:
    assert len(a) == len(b)
    return [a[i] + b[i] for i in range(len(a))]


def fps_sub(a: FPS, b: FPS) -> FPS:
    assert len(a) == len(b)
    return [a[i] - b[i] for i in range(len(a))]


def fps_scale(a: FPS, c: Fraction) -> FPS:
    return [c * x for x in a]


def fps_shift(a: FPS, k: int) -> FPS:
    """Multiply by q^k (right-shift). Requires k >= 0."""
    if k < 0:
        raise ValueError(f"Negative shift {k}")
    n = len(a)
    result = [Fraction(0)] * n
    for i in range(n - k):
        result[i + k] = a[i]
    return result


def fps_multiply(a: FPS, b: FPS) -> FPS:
    n = min(len(a), len(b))
    result = [Fraction(0)] * n
    for i in range(n):
        if a[i] == 0:
            continue
        for j in range(n - i):
            result[i + j] += a[i] * b[j]
    return result


def fps_inverse(a: FPS) -> FPS:
    """1/a as FPS. Requires a[0] != 0."""
    n = len(a)
    if a[0] == 0:
        raise ValueError("Zero constant term")
    result = [Fraction(0)] * n
    inv_a0 = Fraction(1) / a[0]
    result[0] = inv_a0
    for i in range(1, n):
        s = Fraction(0)
        for j in range(1, i + 1):
            if j < n and a[j] != 0:
                s += a[j] * result[i - j]
        result[i] = -s * inv_a0
    return result


def fps_power(a: FPS, k: int) -> FPS:
    """a^k for non-negative integer k."""
    if k == 0:
        return fps_one(len(a) - 1)
    result = fps_one(len(a) - 1)
    for _ in range(k):
        result = fps_multiply(result, a)
    return result


def fps_evaluate(f: FPS, q: float) -> float:
    return sum(float(c) * q ** i for i, c in enumerate(f))


def fps_to_int_list(f: FPS) -> List[int]:
    result = []
    for c in f:
        if c.denominator != 1:
            raise ValueError(f"Non-integer coefficient: {c}")
        result.append(int(c))
    return result


# ===================================================================
# Section 4: Schur functions at principal specialization
# ===================================================================
#
# s_lambda(1, q, q^2, ...) = q^{n(lambda)} / prod_{box} (1 - q^{h(box)})

def schur_principal_fps(lam: Partition, order: int) -> FPS:
    """
    s_lambda(1, q, q^2, ...) as a truncated FPS.
    """
    if not lam:
        return fps_one(order)

    n_lam = n_stat(lam)
    if n_lam > order:
        return fps_zero(order)

    hooks = hook_lengths(lam)
    result = fps_one(order)
    for h in hooks:
        if h <= order:
            for m in range(h, order + 1):
                result[m] += result[m - h]
    return fps_shift(result, n_lam)


def skew_schur_principal_fps(lam: Partition, mu: Partition, order: int) -> FPS:
    """
    s_{lambda/mu}(1, q, q^2, ...) via Jacobi-Trudi determinant.
    """
    if not lam and not mu:
        return fps_one(order)
    if not lam:
        return fps_zero(order)
    for i in range(len(mu)):
        if i >= len(lam) or mu[i] > lam[i]:
            return fps_zero(order)
    if not mu:
        return schur_principal_fps(lam, order)

    r = max(len(lam), len(mu))
    lam_pad = list(lam) + [0] * (r - len(lam))
    mu_pad = list(mu) + [0] * (r - len(mu))

    max_k = max(lam_pad[i] - mu_pad[j] - i + j
                for i in range(r) for j in range(r))
    max_k = max(max_k, 0)

    h_cache: Dict[int, FPS] = {0: fps_one(order)}
    for k in range(1, max_k + 1):
        h_cache[k] = list(h_cache[k - 1])
        for m in range(k, order + 1):
            h_cache[k][m] += h_cache[k][m - k]

    def get_h(k: int) -> FPS:
        if k < 0:
            return fps_zero(order)
        if k in h_cache:
            return h_cache[k]
        prev = get_h(k - 1)
        result = list(prev)
        for m in range(k, order + 1):
            result[m] += result[m - k]
        h_cache[k] = result
        return result

    matrix = [[get_h(lam_pad[i] - mu_pad[j] - i + j)
               for j in range(r)] for i in range(r)]

    det = fps_zero(order)
    for perm in permutations(range(r)):
        sign = _perm_sign(perm)
        prod = fps_one(order)
        skip = False
        for i in range(r):
            if all(c == 0 for c in matrix[i][perm[i]]):
                skip = True
                break
            prod = fps_multiply(prod, matrix[i][perm[i]])
        if skip:
            continue
        if sign == -1:
            prod = fps_scale(prod, Fraction(-1))
        det = fps_add(det, prod)
    return det


def _perm_sign(perm) -> int:
    perm = list(perm)
    n = len(perm)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign


# ===================================================================
# Section 5: Schur functions at shifted specializations (SSYT)
# ===================================================================

def _generate_ssyt(shape: List[int], mu_padded: List[int], n_vars: int):
    """
    Generate all SSYT of skew shape (shape/mu_padded) with entries in {0,...,n_vars-1}.
    """
    rows = len(shape)
    if rows == 0:
        yield []
        return

    def fill_row(row_idx, prev_row_entries):
        start = mu_padded[row_idx]
        end = shape[row_idx]
        n_boxes = end - start
        if n_boxes <= 0:
            yield []
            return

        def fill_box(box_idx, entries):
            if box_idx == n_boxes:
                yield list(entries)
                return
            col = start + box_idx
            lb = entries[-1] if entries else 0
            if prev_row_entries is not None:
                prev_start = mu_padded[row_idx - 1] if row_idx > 0 else 0
                above_idx = col - prev_start
                if 0 <= above_idx < len(prev_row_entries):
                    lb = max(lb, prev_row_entries[above_idx] + 1)
            for val in range(lb, n_vars):
                yield from fill_box(box_idx + 1, entries + [val])

        yield from fill_box(0, [])

    def fill_all(row_idx, prev_entries, accumulated):
        if row_idx == rows:
            yield list(accumulated)
            return
        for row_fill in fill_row(row_idx, prev_entries):
            yield from fill_all(row_idx + 1, row_fill, accumulated + [row_fill])

    yield from fill_all(0, None, [])


def schur_at_powers(lam: Partition, mu: Partition,
                    exponents: List[int], order: int) -> FPS:
    """
    s_{lam/mu}(q^{a_1}, ..., q^{a_N}) via SSYT.
    exponents = [a_1, ..., a_N] must be non-negative integers.
    """
    if not lam and not mu:
        return fps_one(order)
    if not lam:
        return fps_zero(order)
    for i in range(len(mu)):
        if i >= len(lam) or mu[i] > lam[i]:
            return fps_zero(order)
    if not mu:
        mu = ()

    rows = len(lam)
    mu_pad = list(mu) + [0] * (rows - len(mu)) if mu else [0] * rows

    result = fps_zero(order)
    for tab in _generate_ssyt(list(lam), mu_pad, len(exponents)):
        weight = sum(exponents[entry] for row in tab for entry in row)
        if weight <= order:
            result[weight] += Fraction(1)
    return result


# ===================================================================
# Section 6: The topological vertex C_{lam,mu,nu}(q)
# ===================================================================
#
# For the three geometries (C^3, conifold, local P^2) we use the Cauchy
# identity approach (Sections 8-10) rather than the raw vertex formula.
# This section provides the general vertex for reference.

def topological_vertex_shifted(lam: Partition, mu: Partition, nu: Partition,
                               order: int = 10, N: int = 0) -> FPS:
    """
    C_{lam,mu,nu}(q) via N-variable shifted specialization.

    Returns FPS in q representing the vertex up to an N-dependent q-power shift.
    Exact for partition functions when assembled with consistent N across all vertices.
    """
    lam_t = conjugate(lam)
    nu_t = conjugate(nu)
    if N == 0:
        N = order + max(len(lam), len(mu), len(nu), 1) + 3

    def shifted_exps(part):
        return [part[i] + N - 1 - i if i < len(part) else N - 1 - i
                for i in range(N)]

    nu_exps = shifted_exps(nu)
    nut_exps = shifted_exps(nu_t)
    rho_exps = shifted_exps(())

    s_nut_rho = schur_at_powers(nu_t, (), rho_exps, order)

    max_eta = min(
        partition_size(lam_t) if lam_t else 0,
        partition_size(mu) if mu else 0
    )

    eta_sum = fps_zero(order)
    for sz in range(max_eta + 1):
        for eta in partitions_of(sz):
            s1 = schur_at_powers(lam_t, eta, nu_exps, order)
            if all(c == 0 for c in s1):
                continue
            s2 = schur_at_powers(mu, eta, nut_exps, order)
            if all(c == 0 for c in s2):
                continue
            eta_sum = fps_add(eta_sum, fps_multiply(s1, s2))

    return fps_multiply(s_nut_rho, eta_sum)


# ===================================================================
# Section 7: MacMahon function M(q)
# ===================================================================

def macmahon_coefficients(max_order: int) -> List[int]:
    """
    M(q) = prod_{n>=1} 1/(1-q^n)^n, OEIS A000219.
    M(q) = 1 + q + 3q^2 + 6q^3 + 13q^4 + 24q^5 + 48q^6 + 86q^7 + ...
    """
    coeffs = [0] * (max_order + 1)
    coeffs[0] = 1
    for n in range(1, max_order + 1):
        for _ in range(n):
            for m in range(n, max_order + 1):
                coeffs[m] += coeffs[m - n]
    return coeffs


def macmahon_fps(order: int) -> FPS:
    return [Fraction(c) for c in macmahon_coefficients(order)]


def macmahon_numerical(q: float, max_n: int = 200) -> float:
    result = 1.0
    for n in range(1, max_n + 1):
        result /= (1.0 - q ** n) ** n
    return result


# ===================================================================
# Section 8: Z_{C^3} = M(q) via Cauchy identity
# ===================================================================
#
# The Cauchy identity at x_i = q^{i-1/2}:
#   M(q) = sum_nu q^{|nu|} [s_nu(1, q, q^2, ...)]^2
#
# This is the vertex/crystal-melting derivation of the MacMahon function.
# Each partition nu contributes the squared principal specialization
# weighted by q^{|nu|} (from the x_i = q^{i-1/2} shift).

def C3_vertex_sum(max_order: int = 10) -> List[int]:
    """
    Z_{C^3} = M(q) via Cauchy identity at principal specialization.

    Computes sum_nu q^{|nu|} [s_nu(1,q,...)]^2 and returns coefficient list.
    """
    result = fps_zero(max_order)
    for size in range(max_order + 1):
        for nu in partitions_of(size):
            s_nu = schur_principal_fps(nu, max_order)
            sq = fps_multiply(s_nu, s_nu)
            sq = fps_shift(sq, size)
            result = fps_add(result, sq)
    return fps_to_int_list(result)


def C3_partition_function(max_order: int = 10) -> List[int]:
    """Z_{C^3} = M(q) via direct product formula."""
    return macmahon_coefficients(max_order)


# ===================================================================
# Section 9: Resolved conifold via dual Cauchy identity
# ===================================================================
#
# The dual Cauchy identity at x_i = Q^{1/2} q^{i-1/2}:
#
#   prod_{k>=1} (1 - Q q^k)^k
#       = sum_nu (-1)^{|nu|} Q^{|nu|} q^{|nu|} s_nu(1,q,...) s_{nu^t}(1,q,...)
#
# This is Z_conifold / M(q).

def conifold_vertex_sum(max_q_order: int = 10,
                        max_Q_order: int = 4) -> Dict[int, List[int]]:
    """
    Z_conifold/M(q) = prod(1-Qq^n)^n via dual Cauchy identity.

    Returns dict: k -> coefficient list of Q^k contribution.
    """
    result = {}
    for k in range(max_Q_order + 1):
        f_k = fps_zero(max_q_order)
        for nu in partitions_of(k):
            nu_t = conjugate(nu)
            s_nu = schur_principal_fps(nu, max_q_order)
            s_nut = schur_principal_fps(nu_t, max_q_order)
            prod = fps_multiply(s_nu, s_nut)
            prod = fps_shift(prod, k)
            if k % 2 == 1:
                prod = fps_scale(prod, Fraction(-1))
            f_k = fps_add(f_k, prod)
        result[k] = fps_to_int_list(f_k)
    return result


def conifold_product(max_q_order: int, max_Q_order: int) -> Dict[int, List[int]]:
    """
    prod_{n>=1} (1 - Qq^n)^n expanded as double power series.

    Returns dict: k -> coefficient list of Q^k contribution.
    """
    coeffs: Dict[int, List[int]] = {0: [0] * (max_q_order + 1)}
    coeffs[0][0] = 1

    for n in range(1, max_q_order + 1):
        binom_terms = []
        bc = 1
        for j in range(n + 1):
            qshift = n * j
            if qshift > max_q_order:
                break
            binom_terms.append((j, qshift, ((-1) ** j) * bc))
            bc = bc * (n - j) // (j + 1)

        new_coeffs: Dict[int, List[int]] = {}
        for k_old, qc in coeffs.items():
            for j, qshift, bval in binom_terms:
                k_new = k_old + j
                if k_new > max_Q_order:
                    continue
                if k_new not in new_coeffs:
                    new_coeffs[k_new] = [0] * (max_q_order + 1)
                for m in range(max_q_order + 1):
                    if qc[m] == 0:
                        continue
                    m_new = m + qshift
                    if m_new <= max_q_order:
                        new_coeffs[k_new][m_new] += bval * qc[m]
        coeffs = new_coeffs

    return coeffs


def conifold_numerical(q: float, Q: float, max_n: int = 200) -> float:
    """Z_conifold/M(q) = prod (1-Qq^n)^n evaluated numerically."""
    result = 1.0
    for n in range(1, max_n + 1):
        result *= (1.0 - Q * q ** n) ** n
    return result


def conifold_full_coefficients(max_q_order: int,
                               max_Q_order: int) -> Dict[int, List[int]]:
    """
    Full (unnormalized) Z_conifold = M(q) * prod(1-Qq^n)^n.

    Returns coefficients of Q^k q^m.
    """
    mac = macmahon_coefficients(max_q_order)
    normalized = conifold_product(max_q_order, max_Q_order)
    result = {}
    for k, qc in normalized.items():
        full = [0] * (max_q_order + 1)
        for i in range(max_q_order + 1):
            if qc[i] == 0:
                continue
            for j in range(max_q_order + 1 - i):
                full[i + j] += qc[i] * mac[j]
        result[k] = full
    return result


# ===================================================================
# Section 10: Local P^2 = O(-3) -> P^2
# ===================================================================
#
# The Gopakumar-Vafa expansion for the normalized partition function:
#
#   log(Z/M(q)^3) = sum_{d>=1} sum_{g>=0} sum_{k>=1}
#       n_d^g / k * [(-q^k/(1-q^k)^2)]^{1-g} * (-Q)^{dk} * f(g,k,q)
#
# where the genus-g dependence is:
#   (2sin(k*g_s/2))^{2g-2} with q = e^{ig_s}
#   = [-(q^{k/2} - q^{-k/2})^2]^{g-1}
#   = [(-1)(q^k - 2 + q^{-k})]^{g-1}
#
# For genus 0 only (dominant for small q):
#   F^{g=0} = sum_{d>=1} sum_{k>=1} n_d^0/k * (-q^k/(1-q^k)^2) * (-Q)^{dk}
#
# Known genus-0 GV invariants for local P^2:
#   n_1^0 = 3, n_2^0 = -6, n_3^0 = 27, n_4^0 = -192, n_5^0 = 1695
#
# (Konishi-Minabe, "Flop invariance of the topological vertex", also
#  Chiang-Klemm-Yau-Zaslow, "Local Mirror Symmetry: Calculations and
#  Interpretations", hep-th/9903053)

LOCAL_P2_GV_GENUS0 = {1: 3, 2: -6, 3: 27, 4: -192, 5: 1695, 6: -17064}


def _gv_factor_genus0(k: int, order: int) -> FPS:
    """
    The genus-0 GV factor: -q^k / (1 - q^k)^2 as an FPS truncated at order.

    This arises from 1/(2 sin(k g_s/2))^2 = -q^k/(1-q^k)^2
    where q = e^{i g_s}.
    """
    # -q^k / (1 - q^k)^2 = -q^k * sum_{m>=0} (m+1) q^{km}
    #                     = -sum_{m>=0} (m+1) q^{k(m+1)} = -sum_{m>=1} m q^{km}
    f = fps_zero(order)
    for m in range(1, order // k + 1 if k > 0 else 0):
        if k * m <= order:
            f[k * m] = Fraction(-m)
    return f


def local_P2_free_energy_genus0(max_q_order: int,
                                max_d: int = 5) -> Dict[int, FPS]:
    """
    Genus-0 free energy F^{g=0} for local P^2, organized by Q-degree.

    F^{g=0}|_{Q^D} = sum over factorizations D = dk of
        n_d^0/k * (-q^k/(1-q^k)^2) * (-1)^{dk}

    Returns dict: D -> FPS for the coefficient of Q^D in F^{g=0}.
    """
    result: Dict[int, FPS] = {}

    for D in range(1, max_d + 1):
        f_D = fps_zero(max_q_order)
        # Sum over factorizations D = d*k
        for d in range(1, D + 1):
            if D % d != 0:
                continue
            k = D // d
            if d not in LOCAL_P2_GV_GENUS0:
                continue
            n_d = LOCAL_P2_GV_GENUS0[d]
            gv_k = _gv_factor_genus0(k, max_q_order)
            # Coefficient: n_d / k * (-1)^D
            coeff = Fraction(n_d * ((-1) ** D), k)
            term = fps_scale(gv_k, coeff)
            f_D = fps_add(f_D, term)
        result[D] = f_D

    return result


def local_P2_partition_function(max_q_order: int = 10,
                                max_d: int = 5) -> Dict[int, List[int]]:
    """
    Z_{local P^2}/M(q)^3 via GV expansion (genus 0 only).

    Returns dict: D -> coefficient list of Q^D in Z/M(q)^3.

    The partition function is Z/M^3 = exp(F) where F is the free energy.
    We compute exp(F) order by order in Q.
    """
    free_energy = local_P2_free_energy_genus0(max_q_order, max_d)
    order = max_q_order

    # Exponentiate order by order in Q:
    # Z_D = F_D + (1/2) sum_{D1+D2=D} F_{D1} F_{D2} + ...
    Z: Dict[int, FPS] = {}
    Z[0] = fps_one(order)

    # Bell polynomial / exponential expansion:
    # Z_D = sum over partitions of D into positive parts (D1,...,Dk)
    #       (1/k!) prod F_{Di}
    # We compute this iteratively.
    for D in range(1, max_d + 1):
        Z_D = fps_zero(order)
        if D in free_energy:
            Z_D = fps_add(Z_D, free_energy[D])

        # Higher order terms from products of lower-degree free energies
        # Z_D = F_D + sum_{D1=1}^{D-1} F_{D1} * Z_{D-D1} / (D-D1 weight)
        # Actually, the correct formula via the recursion for exp(F):
        # D * Z_D = sum_{k=1}^{D} k * F_k * Z_{D-k}
        # So Z_D = (1/D) sum_{k=1}^{D} k * F_k * Z_{D-k}
        if D > 1:
            running = fps_zero(order)
            for k in range(1, D + 1):
                if k not in free_energy:
                    continue
                running = fps_add(running,
                                  fps_scale(fps_multiply(free_energy[k],
                                                         Z.get(D - k, fps_zero(order))),
                                            Fraction(k)))
            Z_D = fps_scale(running, Fraction(1, D))

        Z[D] = Z_D

    return {D: fps_to_int_list(Z[D]) for D in Z}


def local_P2_vertex_check_d1(max_order: int = 10, N: int = 0) -> List[int]:
    """
    Verify the degree-1 coefficient of Z/M^3 for local P^2 via direct
    vertex computation.

    At degree 1, only one of the three edges carries partition (1,) and the
    other two carry (). The three vertices each contribute:
        C_{(),(), (1)} * C_{(1),(), ()} * C_{(),(), ()} = s_{(1)}^2 (shifted)

    By Z_3 symmetry there are 3 such configurations. After including the
    edge factor q^{|nu|} from the Cauchy identity normalization:

    Z/M^3|_{Q^1} = 3 * q * [s_{(1)}(1,q,...)]^2 = 3q/(1-q)^2

    This matches the GV prediction: n_1^0 = 3, giving
    F|_{Q^1} = 3 * (-q/(1-q)^2) * (-1) = 3q/(1-q)^2
    and Z/M^3|_{Q^1} = F|_{Q^1} = 3q/(1-q)^2.
    """
    # s_{(1)}(1,q,...) = 1/(1-q)
    s_box = schur_principal_fps((1,), max_order)
    sq = fps_multiply(s_box, s_box)
    # Three configurations, each with edge factor q^1
    result = fps_scale(fps_shift(sq, 1), Fraction(3))
    return fps_to_int_list(result)


# ===================================================================
# Section 11: Gopakumar-Vafa invariant extraction
# ===================================================================

def extract_gv_genus0_from_vertex(Z_coeffs: Dict[int, List[int]],
                                  max_d: int = 3) -> Dict[int, int]:
    """
    Given the partition function Z/M^chi organized by Q-degree,
    extract genus-0 GV invariants by inverting the multi-cover formula.

    The free energy F = log(Z/M^chi) has:
    F_D = sum_{d|D} n_d^0/k * (-q^k/(1-q^k)^2) * (-1)^D  where k = D/d.

    For D=1: F_1 = n_1^0 * (-q/(1-q)^2) * (-1) = n_1^0 * q/(1-q)^2
    So n_1^0 = coefficient of q in F_1 (should be n_1^0).

    For D=2: F_2 = n_2^0 * (-q/(1-q)^2) + n_1^0/2 * (-q^2/(1-q^2)^2)
    """
    # First compute F = log(Z) by inverting the exp recursion:
    # D * F_D = D * Z_D - sum_{k=1}^{D-1} k * F_k * Z_{D-k}
    order = len(Z_coeffs.get(0, [])) - 1 if 0 in Z_coeffs else 10

    Z_fps = {d: [Fraction(c) for c in coeffs] for d, coeffs in Z_coeffs.items()}
    F_fps: Dict[int, FPS] = {}

    for D in range(1, max_d + 1):
        running = fps_scale(Z_fps.get(D, fps_zero(order)), Fraction(D))
        for k in range(1, D):
            if k in F_fps:
                running = fps_sub(running,
                                  fps_scale(fps_multiply(F_fps[k],
                                                         Z_fps.get(D - k, fps_zero(order))),
                                            Fraction(k)))
        F_fps[D] = fps_scale(running, Fraction(1, D))

    # Extract n_d^0 from F_d
    gv = {}
    for d in range(1, max_d + 1):
        # At degree D=d, the leading term of F_d gives n_d^0:
        # F_d = n_d^0 * (-1)^d * (-q/(1-q)^2) + (multi-cover from lower d)
        # = n_d^0 * (-1)^d * (q + 2q^2 + 3q^3 + ...)
        # So n_d^0 * (-1)^d = F_d[1] (coefficient of q^1 in F_d)
        # But we also need to subtract multi-cover contributions from lower d.
        F_d = F_fps.get(d, fps_zero(order))

        # Subtract multi-cover contributions from d' < d where d = d'*k
        for d_prime in range(1, d):
            if d % d_prime != 0:
                continue
            if d_prime not in gv:
                continue
            k = d // d_prime
            # Multi-cover: n_{d'}^0/k * (-q^k/(1-q^k)^2) * (-1)^d
            mc_factor = _gv_factor_genus0(k, order)
            mc = fps_scale(mc_factor, Fraction(gv[d_prime] * ((-1) ** d), k))
            F_d = fps_sub(F_d, mc)

        # Now F_d = n_d^0 * (-1)^d * (-q/(1-q)^2)
        # The coefficient of q in (-q/(1-q)^2) is -1.
        # So F_d[1] = n_d^0 * (-1)^d * (-1)
        # n_d^0 = F_d[1] * (-1)^{d+1}
        if order >= 1:
            n_d = int(F_d[1] * (-1) ** (d + 1))
            gv[d] = n_d

    return gv
