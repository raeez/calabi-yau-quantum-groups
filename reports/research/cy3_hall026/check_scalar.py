"""Exact finite checks for the scalar Hall coefficient calculation."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import factorial
from pathlib import Path
import json
import platform


def zeros(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def subtract(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def commutator(a, b):
    return subtract(multiply(a, b), multiply(b, a))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def potential(a, b, c):
    return trace(multiply(a, commutator(b, c)))


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    height = len(a)
    width = len(a[0]) if height else 0
    pivot_row = 0
    for column in range(width):
        pivot = next((i for i in range(pivot_row, height) if a[i][column]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][column]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(height):
            if i != pivot_row:
                scale = a[i][column]
                a[i] = [x - scale*y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def determinant(a):
    a = [[Fraction(x) for x in row] for row in a]
    result = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result *= -1
        scale = a[j][j]
        result *= scale
        for i in range(j+1, len(a)):
            factor = a[i][j]/scale
            for k in range(j, len(a)):
                a[i][k] -= factor*a[j][k]
    return result


def partitions(n, lower=1):
    if n == 0:
        yield ()
    for first in range(lower, n+1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def jordan(types):
    n = sum(map(sum, types))
    a = zeros(n)
    offset = 0
    for eigenvalue, partition in enumerate(types):
        for length in partition:
            for i in range(length):
                a[offset+i][offset+i] = Fraction(eigenvalue)
                if i+1 < length:
                    a[offset+i][offset+i+1] = Fraction(1)
            offset += length
    return a


def commutator_rank(a):
    n = len(a)
    columns = []
    for i in range(n):
        for j in range(n):
            unit = zeros(n)
            unit[i][j] = Fraction(1)
            columns.append([x for row in commutator(a, unit) for x in row])
    return rank(list(map(list, zip(*columns))))


def ordered_flags(n, sizes):
    counts = Counter()
    for ordering in permutations(range(n)):
        start = 0
        flag = []
        for size in sizes:
            flag.append(tuple(sorted(ordering[start:start+size])))
            start += size
        counts[tuple(flag)] += 1
    return counts


def subset_flags(items, sizes):
    if not sizes:
        return int(not items)
    return sum(subset_flags(tuple(x for x in items if x not in chosen), sizes[1:])
               for chosen in combinations(items, sizes[0]))


def block(a, start, size):
    return [row[start:start+size] for row in a[start:start+size]]


def preserving(n, sizes, seed):
    labels = [k for k, size in enumerate(sizes) for _ in range(size)]
    return [[Fraction(((i+1)*(j+seed+2)+seed) % 7 - 3)
             if labels[i] <= labels[j] else Fraction(0)
             for j in range(n)] for i in range(n)]


results = {"python": platform.python_version(), "arithmetic": "fractions.Fraction"}
pair_records = []
triple_records = []
normal_one = [[0, 0, 1, 0], [0, 0, 0, 1],
              [1, 0, 0, 0], [0, -1, 0, 0]]
assert determinant(normal_one) == -1
for n in range(2, 6):
    for d in range(1, n):
        e = n-d
        counts = ordered_flags(n, (d, e))
        formula = factorial(n)//(factorial(d)*factorial(e))
        recursive = subset_flags(tuple(range(n)), (d, e))
        assert len(counts) == recursive == formula
        assert set(counts.values()) == {factorial(d)*factorial(e)}
        normal = zeros(4*d*e)
        for pair in range(d*e):
            for i in range(4):
                for j in range(4):
                    normal[4*pair+i][4*pair+j] = Fraction(normal_one[i][j])
        sign = determinant(normal)
        assert sign == (-1)**(d*e)
        eps = lambda m: (-1)**(m*(m-1)//2)
        assert eps(d)*eps(e)*sign/eps(n) == 1
        a, b, c = [preserving(n, (d, e), seed) for seed in (1, 2, 4)]
        assert potential(a, b, c) == (
            potential(block(a, 0, d), block(b, 0, d), block(c, 0, d))
            + potential(block(a, d, e), block(b, d, e), block(c, d, e)))
        assert 2*d*d+2*e*e+4*d*e == 2*n*n
        pair_records.append({"ranks": [d, e], "degree": -2*n,
                             "permutation_count": len(counts),
                             "recursive_subset_count": recursive,
                             "factorial_value": formula,
                             "normal_real_determinant": int(sign),
                             "e_sheet_coefficient": 1})
    for d in range(1, n-1):
        for e in range(1, n-d):
            f = n-d-e
            sizes = (d, e, f)
            counts = ordered_flags(n, sizes)
            formula = factorial(n)//(factorial(d)*factorial(e)*factorial(f))
            recursive = subset_flags(tuple(range(n)), sizes)
            left = factorial(d+e)//(factorial(d)*factorial(e))
            left *= factorial(n)//(factorial(d+e)*factorial(f))
            right = factorial(e+f)//(factorial(e)*factorial(f))
            right *= factorial(n)//(factorial(d)*factorial(e+f))
            assert len(counts) == recursive == formula == left == right
            assert d*e+(d+e)*f == e*f+d*(e+f)
            a, b, c = [preserving(n, sizes, seed) for seed in (1, 2, 4)]
            start = 0
            expected = Fraction(0)
            for size in sizes:
                expected += potential(*(block(x, start, size) for x in (a, b, c)))
                start += size
            assert potential(a, b, c) == expected
            triple_records.append({"ranks": sizes, "left": left, "right": right,
                                   "permutation_count": len(counts),
                                   "recursive_subset_count": recursive})
results["pairs"] = pair_records
results["triples"] = triple_records

jordan_records = []
affine_records = []
for n in range(1, 6):
    choices = [p for m in range(1, n+1) for p in partitions(m)]
    types_checked = 0
    dimensions = Counter()
    for r in range(1, n+1):
        for types in combinations_with_replacement(choices, r):
            if sum(map(sum, types)) != n:
                continue
            a = jordan(types)
            centralizer = sum(sum(min(x, y) for x in p for y in p) for p in types)
            measured_rank = commutator_rank(a)
            assert measured_rank == n*n-centralizer
            dimension = n*n-centralizer+r+centralizer
            assert dimension == n*n+r
            dimensions[dimension] += 1
            types_checked += 1
    assert max(dimensions) == n*n+n
    assert dimensions[n*n+n] == 1
    jordan_records.append({"rank": n, "types_checked": types_checked,
                           "pair_stratum_dimensions": dict(sorted(dimensions.items())),
                           "bottom_coefficient_degree": 2*n*n-2*(n*n+n),
                           "first_milnor_degree": 2*(n*n-n)-1 if n > 1 else None})
    if n > 1:
        a = zeros(n)
        c = zeros(n)
        for i in range(n):
            a[i][i] = Fraction(i)
        c[0][1] = Fraction(1)
        d = commutator(c, a)
        norm = sum(x*x for row in d for x in row)
        b0 = [[d[j][i]/norm for j in range(n)] for i in range(n)]
        assert trace(multiply(b0, d)) == potential(a, b0, c) == 1
        kernel = zeros(n)
        for i in range(n):
            kernel[i][i] = Fraction(i+1)
        for t in (Fraction(0), Fraction(1, 3), Fraction(1)):
            b = [[b0[i][j]+t*kernel[i][j] for j in range(n)] for i in range(n)]
            assert potential(a, b, c) == 1
        affine_records.append({"rank": n, "affine_fibre_dimension": n*n-1,
                               "section_trace": 1, "homotopy_samples": 3})
results["jordan"] = jordan_records
results["affine_fibres"] = affine_records

# A full critical source excludes an off-diagonal noncommuting pair.
a = [[Fraction(int(i == j)*i) for j in range(3)] for i in range(3)]
b = zeros(3)
b[0][2] = Fraction(1)
c = zeros(3)
assert all(commutator(block(a, start, size), block(b, start, size)) == zeros(size)
           for start, size in ((0, 2), (2, 1)))
assert commutator(a, b) != zeros(3)
results["full_critical_source_counterexample"] = {
    "A": "diag(0,1,2)", "B": "e_13", "C": "0",
    "diagonal_blocks_commute": True, "total_triple_commutes": False}
results["scope"] = (
    "Exact arithmetic checks of finite formulas, incidence identities, normal signs, "
    "and Jordan centralizer ranks. The topological and sheaf proofs are in the TeX module. "
    "No numerical computation certifies higher scalar Hall images.")
out = Path(__file__).with_name("calculation-results.json")
out.write_text(json.dumps(results, indent=2)+"\n")
print(json.dumps({"result": "PASS", "pair_checks": len(pair_records),
                  "triple_checks": len(triple_records),
                  "jordan_types": sum(r["types_checked"] for r in jordan_records),
                  "output": str(out)}, indent=2))
