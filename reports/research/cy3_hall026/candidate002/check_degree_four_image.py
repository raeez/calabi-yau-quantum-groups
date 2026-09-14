"""Exact deciding calculations for the first higher scalar image."""

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, value):
    return trim([value*x for x in a])


def mul(a, b):
    result = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return trim(result)


def power(a, exponent):
    result = [1]
    for _ in range(exponent):
        result = mul(result, a)
    return result


def parity(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def polynomial_determinant(matrix):
    result = [0]
    for p in permutations(range(len(matrix))):
        term = [parity(p)]
        for i, j in enumerate(p):
            term = mul(term, matrix[i][j])
        result = add(result, term)
    return result


def cubic_discriminant(b, c, d):
    return add(add(add(add(mul(power(b, 2), power(c, 2)), scale(power(c, 3), -4)),
                       scale(mul(power(b, 3), d), -4)), scale(power(d, 2), -27)),
               scale(mul(mul(b, c), d), 18))


def resultant_discriminant(b, c, d):
    one, zero = [1], [0]
    matrix = [[one, b, c, d, zero], [zero, one, b, c, d],
              [[3], scale(b, 2), c, zero, zero],
              [zero, [3], scale(b, 2), c, zero],
              [zero, zero, [3], scale(b, 2), c]]
    return scale(polynomial_determinant(matrix), -1)


def substitute_square(p):
    result = [0]*(2*len(p)-1)
    for i, x in enumerate(p):
        result[2*i] = x
    return trim(result)


def matrix_product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def matrix_rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    position = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(position, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[position], a[pivot] = a[pivot], a[position]
        value = a[position][column]
        a[position] = [x/value for x in a[position]]
        for i in range(len(a)):
            if i != position:
                value = a[i][column]
                a[i] = [x-value*y for x, y in zip(a[i], a[position])]
        position += 1
    return position


def fixed_dimension(matrices):
    rows = []
    n = len(matrices[0])
    for m in matrices:
        rows.extend([[m[i][j]-int(i == j) for j in range(n)] for i in range(n)])
    return n-matrix_rank(rows)


records = []
for name, parameter in [('Jordan', [0, 1]), ('semisimple', [0, 0, 1])]:
    b, c, d = [-2], scale(parameter, -1), scale(parameter, 2)
    by_coefficients = cubic_discriminant(b, c, d)
    by_resultant = resultant_discriminant(b, c, d)
    factored = scale(mul(parameter, power(add([4], scale(parameter, -1)), 2)), 4)
    assert by_coefficients == by_resultant == factored
    order = next(i for i, x in enumerate(factored) if x)
    records.append({'stratum': name, 'discriminant_coefficients': factored,
                    'order': order, 'resultant_agrees': True})
root_product = mul(power([0, 2], 2), mul(power([-2, 1], 2), power([-2, -1], 2)))
assert substitute_square(records[0]['discriminant_coefficients']) == root_product
assert records[1]['discriminant_coefficients'] == root_product
assert [record['order'] for record in records] == [1, 2]

s = [[0, 1], [1, 0]]
t = [[-1, -1], [0, 1]]
identity = [[1, 0], [0, 1]]
assert matrix_product(s, s) == matrix_product(t, t) == identity
st = matrix_product(s, t)
assert matrix_product(matrix_product(st, st), st) == identity
assert fixed_dimension([s, t]) == 0
flag_s = [[0, 1], [1, 0]]
flag_t = [[1, 0], [-1, -1]]
assert fixed_dimension([flag_s, flag_t]) == 0
h1_s = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
h1_t = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
assert fixed_dimension([h1_s, h1_t]) == 1

# In H*(P(U)), q^2=-z*q-z^2. Therefore q^3=z^3=0.
constant, coefficient_q = [1], [0]
for _ in range(3):
    constant, coefficient_q = (scale(mul([0, 0, 1], coefficient_q), -1),
                               add(constant, scale(mul([0, 1], coefficient_q), -1)))
    constant, coefficient_q = trim(constant[:3]), trim(coefficient_q[:3])
assert constant == [0] and coefficient_q == [0]

# Actual Chern restrictions on the three complete-flag components.
restriction = [[0, -1, 1], [-1, 0, 1], [-1, 1, 0]]
decoration_images = [sum(row[i] for row in restriction) for i in range(3)]
assert decoration_images == [-2, 0, 2]
assert Fraction(decoration_images[2], 2) == 1

result = {'result': 'PASS', 'discriminant_checks': records,
          'configuration_H2_fixed_dimension': 0, 'flag_H2_fixed_dimension': 0,
          'configuration_H1_fixed_dimension': 1, 'boundary_vector': [1, 2],
          'target_BM22_dimension': 2-matrix_rank([[1, 2]]),
          'exceptional_cycle_projective_pushforward': 0,
          'three_decoration_images_in_w2': decoration_images,
          'scalar_image_in_geometric_basis': [[1, 0]],
          'scope': 'Exact finite formulas and linear algebra. Geometric identifications and map nonvanishing require the TeX proofs.'}
Path(__file__).with_name('degree-four-image-calculations.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
