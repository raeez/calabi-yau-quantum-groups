r"""
crystal_bar_identification.py -- Crystal melting / bar complex identification for C^3.

MATHEMATICAL CONTEXT:

For the Calabi-Yau threefold C^3, Donaldson-Thomas invariants count 3D partitions
(plane partitions) via crystal melting (Okounkov-Reshetikhin-Vafa). The partition
function is MacMahon's:

    M(q) = prod_{n>=1} (1 - q^n)^{-n} = sum_{n>=0} p(n) q^n

where p(n) counts plane partitions of n.

The positive half of the affine Yangian Y^+(gl_hat_1), identified with CoHA(C^3)
by Schiffmann-Vasserot, has the bar complex B(Y^+) with:

    char(B^k(Y^+))(q) = (M(q) - 1)^k

The bar Euler characteristic is:

    sum_{k>=0} (-1)^k (M(q)-1)^k = 1/(1 + (M(q)-1)) = 1/M(q) = prod_{n>=1} (1-q^n)^n

The BPS invariants Omega(n) are extracted via the plethystic logarithm:

    PLog(M(q)) = sum_{n>=1} n q^n     =>     Omega(n) = n

This module investigates the connection between:
  (a) Crystal melting (3D partition enumeration and classification)
  (b) The bar complex filtration (arity decomposition)
  (c) The plethystic/BPS decomposition

KEY RESULTS:

1. No single "arity" function on individual 3D partitions matches B^k_n,
   because B^k_n counts ORDERED k-TUPLES of partitions (tensor factors),
   not individual partitions with a label.

2. The three natural dimensions of a 3D partition (max_height, num_rows,
   num_cols) give identical distributions by the S_3 symmetry of C^3.

3. The plethystic logarithm PLog(M(q)) = sum n q^n gives the BPS generator
   count Omega(n) = n, which matches the arity-1 bar cohomology H^1_n.

4. The plethystic exponential recovers M(q) from Omega(n) = n, establishing
   the crystal-to-bar-generator identification.

5. The restricted generating functions by each arity notion provide a
   decomposition of M(q) that is mathematically consistent but does NOT
   match the bar arity filtration (which is a tensor-algebraic, not
   combinatorial-geometric, decomposition).

LITERATURE:
    Okounkov-Reshetikhin-Vafa arXiv:hep-th/0309208: crystal melting
    Schiffmann-Vasserot arXiv:1211.1287: CoHA(C^3) = Y^+(gl_hat_1)
    Kontsevich-Soibelman arXiv:0811.2435: motivic DT / plethystic
    MNOP arXiv:math/0312059: DT/GW for C^3

MULTI-PATH VERIFICATION:
    Path A: Direct 3D partition enumeration and classification
    Path B: Generating function comparison (restricted GF vs (M-1)^k)
    Path C: Plethystic logarithm/exponential round-trip
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from typing import Callable, Dict, List, Optional, Tuple

from compute.lib.c3_dt_partition import (
    enumerate_plane_partitions,
    macmahon_coefficients,
    macmahon_coefficients_product,
    plane_partition_counts,
)
from compute.lib.yangian_bar_complex import (
    bar_arity_k_dims,
    bar_euler_char_by_degree,
    bps_invariants_c3,
    bps_invariants_from_macmahon,
    plethystic_log_coefficients,
    symmetric_model_cohomology_dims,
)


# ===========================================================================
# 3D partition arity notions
# ===========================================================================

def arity_max_height(pp: List[List[int]]) -> int:
    """Arity = maximum entry (height of tallest column in crystal)."""
    if not pp or pp == [[]]:
        return 0
    return max(max(row) for row in pp)


def arity_num_rows(pp: List[List[int]]) -> int:
    """Arity = number of rows in the 2D base (spread along axis 1)."""
    if not pp or pp == [[]]:
        return 0
    return len(pp)


def arity_num_cols(pp: List[List[int]]) -> int:
    """Arity = number of columns (spread along axis 2)."""
    if not pp or pp == [[]]:
        return 0
    return max(len(row) for row in pp)


def arity_footprint(pp: List[List[int]]) -> int:
    """Arity = total number of nonzero entries in the 2D base (support size)."""
    if not pp or pp == [[]]:
        return 0
    return sum(len(row) for row in pp)


def arity_trace(pp: List[List[int]]) -> int:
    """Arity = min(num_rows, num_cols), the diagonal length."""
    if not pp or pp == [[]]:
        return 0
    return min(len(pp), max(len(row) for row in pp))


def arity_max_spread(pp: List[List[int]]) -> int:
    """Arity = max(max_height, num_rows, num_cols), the 3D bounding box side."""
    if not pp or pp == [[]]:
        return 0
    h = max(max(row) for row in pp)
    r = len(pp)
    c = max(len(row) for row in pp)
    return max(h, r, c)


def arity_removable_boxes(pp: List[List[int]]) -> int:
    """Arity = number of removable boxes (outer corners of the crystal).

    A box at position (i, j) with height pp[i][j] is removable if
    pp[i+1][j] < pp[i][j] (or i is last row) AND
    pp[i][j+1] < pp[i][j] (or j is last column in that row).
    """
    if not pp or pp == [[]]:
        return 0
    count = 0
    nrows = len(pp)
    for i in range(nrows):
        for j in range(len(pp[i])):
            h = pp[i][j]
            if h == 0:
                continue
            below_ok = (i + 1 >= nrows) or (j >= len(pp[i + 1])) or (pp[i + 1][j] < h)
            right_ok = (j + 1 >= len(pp[i])) or (pp[i][j + 1] < h)
            if below_ok and right_ok:
                count += 1
    return count


def arity_distinct_heights(pp: List[List[int]]) -> int:
    """Arity = number of distinct nonzero height values."""
    if not pp or pp == [[]]:
        return 0
    heights = set()
    for row in pp:
        for h in row:
            if h > 0:
                heights.add(h)
    return len(heights)


def arity_largest_cube(pp: List[List[int]]) -> int:
    """Arity = side length of the largest cube that fits inside the crystal.

    Largest k such that the top-left k x k subarray has all entries >= k.
    """
    if not pp or pp == [[]]:
        return 0
    nrows = len(pp)
    max_possible = min(nrows, max(len(row) for row in pp),
                       max(max(row) for row in pp))
    for k in range(max_possible, 0, -1):
        if nrows >= k and all(
            len(pp[i]) >= k and all(pp[i][j] >= k for j in range(k))
            for i in range(k)
        ):
            return k
    return 0


ALL_ARITY_NOTIONS: Dict[str, Callable] = {
    'max_height': arity_max_height,
    'num_rows': arity_num_rows,
    'num_cols': arity_num_cols,
    'footprint': arity_footprint,
    'trace': arity_trace,
    'max_spread': arity_max_spread,
    'removable_boxes': arity_removable_boxes,
    'distinct_heights': arity_distinct_heights,
    'largest_cube': arity_largest_cube,
}


# ===========================================================================
# Classification engine
# ===========================================================================

def classify_partitions_by_arity(
    n: int,
    arity_fn: Callable[[List[List[int]]], int],
) -> Dict[int, int]:
    """Classify all plane partitions of n by the given arity function.

    Returns {arity_value: count}.
    """
    pps = enumerate_plane_partitions(n)
    counts: Dict[int, int] = Counter()
    for pp in pps:
        a = arity_fn(pp)
        counts[a] += 1
    return dict(counts)


def arity_distribution_table(
    max_n: int,
    arity_fn: Callable[[List[List[int]]], int],
) -> Dict[int, Dict[int, int]]:
    """For each n = 0, ..., max_n-1, compute the arity distribution.

    Returns {n: {arity: count}}.
    """
    result = {}
    for n in range(max_n):
        result[n] = classify_partitions_by_arity(n, arity_fn)
    return result


def restricted_generating_function(
    max_n: int,
    arity_fn: Callable[[List[List[int]]], int],
    arity_value: int,
) -> List[int]:
    """Generating function restricted to partitions with given arity value.

    Returns [c_0, c_1, ..., c_{max_n-1}] where c_n is the number of
    plane partitions of n with arity_fn(pp) == arity_value.
    """
    result = [0] * max_n
    for n in range(max_n):
        counts = classify_partitions_by_arity(n, arity_fn)
        result[n] = counts.get(arity_value, 0)
    return result


# ===========================================================================
# S_3 symmetry verification
# ===========================================================================

def verify_s3_symmetry(max_n: int) -> Dict[str, object]:
    """Verify that max_height, num_rows, num_cols give identical distributions.

    The S_3 symmetry of C^3 (permuting the three coordinate axes) acts on
    plane partitions by transposing the 2D base and/or interchanging height
    with a base direction. Under this symmetry, the three dimension-statistics
    (max_height, num_rows, num_cols) are permuted, so their distributions
    over all plane partitions of n must be identical.

    Returns verification dict.
    """
    match = True
    first_failure = None
    details = {}

    for n in range(max_n):
        d_h = classify_partitions_by_arity(n, arity_max_height)
        d_r = classify_partitions_by_arity(n, arity_num_rows)
        d_c = classify_partitions_by_arity(n, arity_num_cols)
        details[n] = {
            'max_height': d_h,
            'num_rows': d_r,
            'num_cols': d_c,
        }
        if d_h != d_r or d_h != d_c:
            match = False
            if first_failure is None:
                first_failure = n

    return {
        'match': match,
        'first_failure': first_failure,
        'max_n': max_n,
        'details': details,
    }


# ===========================================================================
# Comparison with bar complex dimensions
# ===========================================================================

def compare_arity_with_bar(
    max_n: int,
    arity_fn: Callable[[List[List[int]]], int],
    notion_name: str = 'unknown',
) -> Dict[str, object]:
    """Compare an arity distribution on 3D partitions with B^k_n.

    B^k_n = dim of (Y^+_{>0})^{tensor k} at degree n
           = sum_{n1+...+nk=n, ni>=1} p(n1)*...*p(nk)

    This counts ordered k-tuples, so no single-partition arity can match
    it exactly. But we check whether any arity notion reproduces the
    SAME generating function or has interesting structure.

    Returns comparison dict with match information.
    """
    dist_table = arity_distribution_table(max_n, arity_fn)

    # Get bar dims
    bar_dims = {}
    for k in range(max_n):
        bar_dims[k] = bar_arity_k_dims(k, max_n)

    # For each arity value k, compare the restricted GF with B^k
    matches = {}
    for k in range(max_n):
        crystal_at_k = [dist_table[n].get(k, 0) for n in range(max_n)]
        bar_at_k = bar_dims[k]
        is_match = all(crystal_at_k[n] == bar_at_k[n] for n in range(max_n))
        matches[k] = {
            'crystal': crystal_at_k,
            'bar': bar_at_k,
            'match': is_match,
        }

    any_match = any(m['match'] for m in matches.values())

    return {
        'notion_name': notion_name,
        'any_exact_match': any_match,
        'matches': matches,
        'max_n': max_n,
    }


def compare_all_notions_with_bar(max_n: int) -> Dict[str, Dict[str, object]]:
    """Compare all arity notions with bar complex dimensions."""
    results = {}
    for name, fn in ALL_ARITY_NOTIONS.items():
        results[name] = compare_arity_with_bar(max_n, fn, name)
    return results


# ===========================================================================
# Plethystic decomposition
# ===========================================================================

def plethystic_exp_from_bps(bps: List[int], N: int) -> List[Fraction]:
    """Compute PExp(sum_{n>=1} bps[n] q^n) mod q^N.

    PExp(f(q)) = prod_{n>=1} (1 - q^n)^{-f_n}
    where f(q) = sum_{n>=1} f_n q^n.

    For C^3: bps[n] = n, giving PExp = M(q).
    """
    # log(PExp(f)) = sum_{n>=1} f_n * sum_{m>=1} q^{mn}/m
    log_coeffs = [Fraction(0)] * N
    for n in range(1, N):
        if n >= len(bps) or bps[n] == 0:
            continue
        for m in range(1, N):
            if n * m >= N:
                break
            log_coeffs[n * m] += Fraction(bps[n], m)

    # Exponentiate
    g = [Fraction(0)] * N
    g[0] = Fraction(1)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += Fraction(k) * log_coeffs[k] * g[n - k]
        g[n] = s / Fraction(n)

    return g


def verify_plethystic_round_trip(N: int) -> Dict[str, object]:
    """Verify PExp(PLog(M(q))) = M(q) and PLog(PExp(sum n q^n)) = sum n q^n.

    This is the fundamental identity connecting crystal melting to the BPS
    decomposition.

    Multi-path verification:
      Path A: PLog(M(q)) via Mobius inversion
      Path B: Direct formula Omega(n) = n
      Path C: PExp reconstruction from BPS = n
    """
    mac = macmahon_coefficients(N)

    # Path A: PLog of M(q)
    plog = plethystic_log_coefficients(mac, N)

    # Path B: Direct BPS
    bps_direct = bps_invariants_c3(N)

    # Path C: PExp from BPS
    bps_list = [0] * N
    for n in range(1, N):
        bps_list[n] = n
    pexp = plethystic_exp_from_bps(bps_list, N)

    # Compare
    plog_matches_bps = all(
        abs(float(plog[n]) - bps_direct[n]) < 1e-10
        for n in range(N)
    )
    pexp_matches_mac = all(
        abs(float(pexp[n]) - float(mac[n])) < 1e-10
        for n in range(N)
    )

    return {
        'N': N,
        'plog_matches_bps': plog_matches_bps,
        'pexp_matches_macmahon': pexp_matches_mac,
        'plog_values': [float(plog[n]) for n in range(min(N, 15))],
        'bps_values': bps_direct[:min(N, 15)],
        'pexp_vs_mac': [
            (int(pexp[n]), int(mac[n]))
            for n in range(min(N, 15))
        ],
    }


# ===========================================================================
# Generator (BPS) identification
# ===========================================================================

def bps_as_bar_generators(N: int) -> Dict[str, object]:
    """Verify that BPS invariants Omega(n) = n match bar cohomology H^1_n.

    The bar cohomology at arity 1 computes the indecomposables of Y^+,
    which are the algebra generators. For the commutative (associated graded)
    model Sym(V_BPS):
        H^1(B(Sym(V_BPS)))_n = dim(V_BPS)_n = Omega(n) = n

    This is the crystal-to-bar generator identification: each BPS state
    of charge n corresponds to a generator of the bar complex.

    Multi-path verification:
        Path A: PLog(M(q)) = sum n q^n
        Path B: dim H^1(B(Y^+)) from bar complex computation
        Path C: Direct BPS formula Omega(n) = n
    """
    # Path A: plethystic logarithm
    mac = macmahon_coefficients(N)
    plog = plethystic_log_coefficients(mac, N)

    # Path B: bar cohomology arity 1
    cohom = symmetric_model_cohomology_dims(N, 1)
    h1 = cohom[1]

    # Path C: direct BPS
    bps = bps_invariants_c3(N)

    # Compare all three
    all_match = True
    mismatches = []
    for n in range(N):
        plog_val = int(round(float(plog[n])))
        h1_val = h1[n]
        bps_val = bps[n]
        if not (plog_val == h1_val == bps_val):
            all_match = False
            mismatches.append((n, plog_val, h1_val, bps_val))

    return {
        'all_match': all_match,
        'N': N,
        'mismatches': mismatches,
        'plog': [int(round(float(plog[n]))) for n in range(N)],
        'h1': h1[:N],
        'bps': bps[:N],
    }


# ===========================================================================
# Crystal melting restricted generating functions
# ===========================================================================

def crystal_restricted_gf(
    max_n: int,
    arity_fn: Callable[[List[List[int]]], int],
    max_arity: int,
) -> Dict[int, List[int]]:
    """Compute restricted generating functions M_k(q) for each arity value k.

    M_k(q) = sum_{n>=0} #{pp of n with arity_fn(pp) = k} q^n

    The full MacMahon function decomposes:
        M(q) = sum_k M_k(q)

    Returns {k: [c_0, c_1, ..., c_{max_n-1}]}.
    """
    dist_table = arity_distribution_table(max_n, arity_fn)
    result = {}
    for k in range(max_arity + 1):
        result[k] = [dist_table[n].get(k, 0) for n in range(max_n)]
    return result


def verify_gf_decomposition(
    max_n: int,
    arity_fn: Callable[[List[List[int]]], int],
    notion_name: str = 'unknown',
) -> Dict[str, object]:
    """Verify that the sum of restricted GFs equals M(q).

    sum_k M_k(q) = M(q) (each partition has exactly one arity value).
    """
    dist_table = arity_distribution_table(max_n, arity_fn)
    mac = macmahon_coefficients(max_n)

    match = True
    mismatches = []
    for n in range(max_n):
        total = sum(dist_table[n].values())
        expected = int(mac[n])
        if total != expected:
            match = False
            mismatches.append((n, total, expected))

    return {
        'notion_name': notion_name,
        'match': match,
        'mismatches': mismatches,
        'max_n': max_n,
    }


# ===========================================================================
# Bar complex as crystal melting decomposition
# ===========================================================================

def bar_as_ordered_crystal_compositions(
    n: int,
    k: int,
) -> int:
    """Compute B^k_n by explicitly enumerating ordered k-tuples.

    B^k_n = #{ordered k-tuples (n_1, ..., n_k) with n_i >= 1, sum = n}
            weighted by prod p(n_i).

    This is a direct enumeration (Path A) that provides an independent
    verification of the convolution formula.
    """
    if k == 0:
        return 1 if n == 0 else 0
    if n < k:
        return 0

    pp = plane_partition_counts(n + 1)

    # Enumerate compositions of n into k positive parts
    total = 0

    def _recurse(remaining: int, parts_left: int) -> int:
        nonlocal total
        if parts_left == 1:
            if remaining >= 1:
                total += pp[remaining]
            return
        for ni in range(1, remaining - parts_left + 2):
            old = total
            _recurse(remaining - ni, parts_left - 1)
            # Multiply the contribution by pp[ni]
            # Actually we need to restructure: compute product as we go
            pass

    # Better: recursive with accumulator
    def _count(remaining: int, parts_left: int, weight: int):
        nonlocal total
        if parts_left == 0:
            if remaining == 0:
                total += weight
            return
        for ni in range(1, remaining - parts_left + 2):
            _count(remaining - ni, parts_left - 1, weight * pp[ni])

    _count(n, k, 1)
    return total


def verify_bar_dims_by_enumeration(max_n: int, max_k: int) -> Dict[str, object]:
    """Cross-verify B^k_n by two methods: convolution vs explicit enumeration.

    Path A: bar_arity_k_dims (convolution of augmentation ideal dimensions)
    Path B: bar_as_ordered_crystal_compositions (enumerate k-tuples)
    """
    match = True
    mismatches = []

    for k in range(max_k + 1):
        dims_conv = bar_arity_k_dims(k, max_n)
        for n in range(max_n):
            dim_enum = bar_as_ordered_crystal_compositions(n, k)
            if dims_conv[n] != dim_enum:
                match = False
                mismatches.append((k, n, dims_conv[n], dim_enum))

    return {
        'match': match,
        'mismatches': mismatches,
        'max_n': max_n,
        'max_k': max_k,
    }


# ===========================================================================
# Inverse MacMahon from crystal melting
# ===========================================================================

def inverse_macmahon_from_crystal(N: int) -> List[Fraction]:
    """Compute 1/M(q) = prod_{n>=1} (1-q^n)^n from BPS data.

    Since Omega(n) = n, we have:
        1/M(q) = prod_{n>=1} (1-q^n)^{Omega(n)} = prod_{n>=1} (1-q^n)^n

    This is the bar Euler characteristic: chi_n = [q^n] 1/M(q).
    """
    result = [Fraction(0)] * N
    result[0] = Fraction(1)

    for m in range(1, N):
        # Multiply by (1 - q^m)^m
        for _ in range(m):
            for j in range(N - 1, m - 1, -1):
                result[j] -= result[j - m]

    return result


def verify_inverse_macmahon_three_paths(N: int) -> Dict[str, object]:
    """Cross-verify 1/M(q) by three independent methods.

    Path A: Direct product prod (1-q^n)^n
    Path B: Bar Euler characteristic sum (-1)^k (M-1)^k
    Path C: Power series inversion of M(q)
    """
    # Path A: crystal-based
    inv_crystal = inverse_macmahon_from_crystal(N)

    # Path B: bar Euler characteristic
    inv_bar = bar_euler_char_by_degree(N)

    # Path C: power series inversion
    mac = macmahon_coefficients(N)
    inv_series = _poly_inv_trunc(mac, N)

    # Compare
    ab_match = all(inv_crystal[n] == inv_bar[n] for n in range(N))
    ac_match = all(inv_crystal[n] == inv_series[n] for n in range(N))
    bc_match = all(inv_bar[n] == inv_series[n] for n in range(N))

    return {
        'N': N,
        'crystal_vs_bar': ab_match,
        'crystal_vs_series_inv': ac_match,
        'bar_vs_series_inv': bc_match,
        'all_agree': ab_match and ac_match and bc_match,
        'values': [int(inv_crystal[n]) for n in range(min(N, 15))],
    }


def _poly_inv_trunc(a: List[Fraction], N: int) -> List[Fraction]:
    """Invert a power series mod q^N."""
    if a[0] == 0:
        raise ValueError("Cannot invert: constant term is zero")
    inv_a0 = Fraction(1) / a[0]
    result = [Fraction(0)] * N
    result[0] = inv_a0
    la = len(a)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, min(n + 1, la)):
            s += a[k] * result[n - k]
        result[n] = -inv_a0 * s
    return result


# ===========================================================================
# Comprehensive crystal-bar comparison report
# ===========================================================================

def crystal_bar_comparison_report(max_n: int = 8) -> Dict[str, object]:
    """Full comparison of all arity notions with the bar complex.

    Returns a comprehensive report with:
    - Each arity notion's distribution table
    - Whether it matches B^k_n
    - The S_3 symmetry verification
    - Plethystic round-trip
    - BPS-generator identification
    """
    report = {
        'max_n': max_n,
        's3_symmetry': verify_s3_symmetry(max_n),
        'plethystic_round_trip': verify_plethystic_round_trip(max_n),
        'bps_generators': bps_as_bar_generators(max_n),
        'inverse_macmahon': verify_inverse_macmahon_three_paths(max_n),
        'notion_comparisons': {},
    }

    for name, fn in ALL_ARITY_NOTIONS.items():
        comparison = compare_arity_with_bar(max_n, fn, name)
        decomp_check = verify_gf_decomposition(max_n, fn, name)
        report['notion_comparisons'][name] = {
            'bar_match': comparison['any_exact_match'],
            'gf_decomposition': decomp_check['match'],
        }

    return report


# ===========================================================================
# Arity notion generating functions as power series
# ===========================================================================

def notion_generating_functions(
    max_n: int,
    notion_name: str,
) -> Dict[int, List[int]]:
    """Get the restricted generating functions for a named arity notion.

    Returns {k: [c_0, ..., c_{max_n-1}]} where c_n counts
    partitions of n with the given arity value k.
    """
    if notion_name not in ALL_ARITY_NOTIONS:
        raise ValueError(f"Unknown arity notion: {notion_name}")
    fn = ALL_ARITY_NOTIONS[notion_name]
    dist = arity_distribution_table(max_n, fn)

    # Find max arity
    max_k = 0
    for n in range(max_n):
        if dist[n]:
            max_k = max(max_k, max(dist[n].keys()))

    return crystal_restricted_gf(max_n, fn, max_k)


def total_arity_distribution(max_n: int, notion_name: str) -> List[List[int]]:
    """Full (n, k) distribution table for a named arity notion.

    Returns list of lists: result[n][k] = count of pp of size n with arity k.
    """
    if notion_name not in ALL_ARITY_NOTIONS:
        raise ValueError(f"Unknown arity notion: {notion_name}")
    fn = ALL_ARITY_NOTIONS[notion_name]
    dist = arity_distribution_table(max_n, fn)

    # Find max arity
    max_k = 0
    for n in range(max_n):
        if dist[n]:
            max_k = max(max_k, max(dist[n].keys()))

    result = []
    for n in range(max_n):
        row = [0] * (max_k + 1)
        for k, count in dist[n].items():
            row[k] = count
        result.append(row)

    return result


# ===========================================================================
# Exterior power dimensions (bar cohomology for commutative model)
# ===========================================================================

def wedge_k_bps_dims(N: int, max_k: int) -> Dict[int, List[int]]:
    """Dimensions of Wedge^k(V_BPS) at each degree.

    For V_BPS with dim(V_n) = n (BPS invariants of C^3):
        Wedge^k(V)_n = sum over k-element subsets of the graded pieces
                       of V, choosing vectors with exterior constraints.

    These are the bar cohomology dimensions for the commutative model:
        H^k(B(Sym(V_BPS))) = Wedge^k(V_BPS)
    """
    return symmetric_model_cohomology_dims(N, max_k)


# ===========================================================================
# Crystal statistics
# ===========================================================================

def crystal_statistics(n: int) -> Dict[str, object]:
    """Compute all arity statistics for plane partitions of n.

    Returns a comprehensive dict of statistics.
    """
    pps = enumerate_plane_partitions(n)
    stats = {
        'n': n,
        'count': len(pps),
        'distributions': {},
    }

    for name, fn in ALL_ARITY_NOTIONS.items():
        counts = Counter()
        for pp in pps:
            a = fn(pp)
            counts[a] += 1
        max_k = max(counts.keys()) if counts else 0
        dist = [counts.get(k, 0) for k in range(max_k + 1)]
        stats['distributions'][name] = {
            'values': dist,
            'mean': sum(k * c for k, c in counts.items()) / len(pps) if pps else 0,
            'max': max(counts.keys()) if counts else 0,
        }

    return stats
