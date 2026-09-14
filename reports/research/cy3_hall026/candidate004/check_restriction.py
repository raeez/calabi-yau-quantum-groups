"""Exact checks for the block restriction and its first decorated images."""

from pathlib import Path
from itertools import permutations
from fractions import Fraction
import hashlib
import json
import platform

import sympy as sp


report = Path(__file__).resolve().parent
c1, c2, y, u, z = sp.symbols("c1 c2 y u z")
l1, l2, l3 = sp.symbols("l1 l2 l3")
x1, x2, x3 = sp.symbols("x1 x2 x3")
disc = c1**2 - 4*c2
resultant = y**2 - c1*y + c2
euler = resultant**2


def reduce_plane(poly):
    """Use the projective bundle relation for the quotient line."""
    reduced = sp.rem(sp.Poly(sp.expand(poly), u), sp.Poly(u*u-c1*u+c2, u))
    a, b = reduced.nth(0), reduced.nth(1)
    free = sp.expand(2*a+c1*b)
    torsion = sp.expand(b.subs(c2, c1*c1/4))
    return free, torsion


def fixed_component_sum(poly):
    substitutions = [(y, c1-u, u), (c1-u, y, u), (c1-u, u, y)]
    values = [reduce_plane(poly.subs(dict(zip((l1, l2, l3), item)), simultaneous=True))
              for item in substitutions]
    return tuple(sp.expand(sum(item[i] for item in values)) for i in (0, 1))


def root_and_collision_sum(poly):
    """Compute the free part by six roots and the torsion by a double-root derivative."""
    roots = (x1, x2, y)
    free = sp.expand(sum(poly.subs(dict(zip((l1, l2, l3), order)), simultaneous=True)
                         for order in permutations(roots)))
    free = sp.symmetrize(free, (x1, x2), formal=True)
    assert free[1] == 0
    free = free[0].subs({free[2][0][0]: c1, free[2][1][0]: c2}, simultaneous=True)
    eps = sp.Symbol("eps")
    torsion = 0
    for order in ((y, z-eps, z+eps), (z-eps, y, z+eps), (z-eps, z+eps, y)):
        collision = poly.subs(dict(zip((l1, l2, l3), order)), simultaneous=True)
        torsion += sp.diff(collision, eps).subs(eps, 0)
    return sp.expand(free), sp.expand(torsion.subs(z, c1/2))


monomial_checks = 0
for a in range(5):
    for b in range(5-a):
        for c in range(5-a-b):
            p = l1**a*l2**b*l3**c
            geometric = fixed_component_sum(p)
            algebraic = root_and_collision_sum(p)
            assert all(sp.expand(g-a) == 0 for g, a in zip(geometric, algebraic))
            monomial_checks += 1

values = {}
for label, p in {"sigma3": sp.Rational(1, 6), "kappa31": l1,
                 "kappa32": l2, "tau3": l3/2,
                 "z3": l3/2-(l1+l2+l3)/6,
                 "flag_X": l2+l3, "flag_Y": l3}.items():
    values[label] = tuple(map(str, fixed_component_sum(p)))
assert values == {
    "sigma3": ("1", "0"), "kappa31": ("2*c1 + 2*y", "-2"),
    "kappa32": ("2*c1 + 2*y", "0"), "tau3": ("c1 + y", "1"),
    "z3": ("0", "1"), "flag_X": ("4*c1 + 4*y", "2"),
    "flag_Y": ("2*c1 + 2*y", "2")}

# A direct exact determinant computes the cross-block Euler polynomial.
companion = sp.Matrix([[0, -c2], [1, c1]])
determinant = sp.factor((y*sp.eye(2)-companion).det())
assert sp.expand(determinant-resultant) == 0
assert sp.expand(euler.subs(c2, c1*c1/4)-(y-c1/2)**4) == 0
assert sp.Poly((y-c1/2)**4, y).degree() == 4

# The three nonfixed flag stabilizers each have a plane character equal to Q.
ga, gb, gd, gq = sp.symbols("ga gb gd gq")
stabilizers = [sp.Matrix([[ga, gb], [0, gq]]),
               sp.Matrix([[gq, gb], [0, gd]]),
               sp.Matrix([[gq, 0], [0, gd]])]
assert all((gq*sp.eye(2)-matrix).det() == 0 for matrix in stabilizers)

# Complex real determinants are positive for every nonzero complex multiplier.
orientation_checks = 0
for real, imag in ((1, 0), (0, 1), (-2, 3), (Fraction(1, 3), Fraction(-2, 5))):
    determinant_real = real*real+imag*imag
    assert determinant_real > 0
    orientation_checks += 1

# The two flags give the same denominator, without using an image formula.
vandermonde = (x2-x1)**2*(x3-x1)**2*(x3-x2)**2
left = (x2-x1)**2*euler.subs({c1: x1+x2, c2: x1*x2, y: x3}, simultaneous=True)
right = (x3-x2)**2*euler.subs({c1: x2+x3, c2: x2*x3, y: x1}, simultaneous=True)
assert sp.expand(left-vandermonde) == sp.expand(right-vandermonde) == 0

# Verify the actual potential and its critical upper-block equations.
a = sp.Matrix(2, 2, sp.symbols("a0:4"))
b = sp.Matrix(2, 2, sp.symbols("b0:4"))
c = sp.Matrix(2, 2, sp.symbols("c0:4"))
alpha, beta, gamma = sp.symbols("alpha beta gamma")
upper_a = sp.Matrix(sp.symbols("ua0:2"))
upper_b = sp.Matrix(sp.symbols("ub0:2"))
upper_c = sp.Matrix(sp.symbols("uc0:2"))


def block(matrix, upper, scalar):
    return matrix.row_join(upper).col_join(sp.Matrix([[0, 0, scalar]]))


A, B, C = block(a, upper_a, alpha), block(b, upper_b, beta), block(c, upper_c, gamma)
potential3 = sp.expand(sp.trace(A*(B*C-C*B)))
potential2 = sp.expand(sp.trace(a*(b*c-c*b)))
assert sp.expand(potential3-potential2) == 0
cross_ab = a*upper_b + beta*upper_a - b*upper_a-alpha*upper_b
assert all(sp.expand(entry) == 0 for entry in (A*B-B*A)[:2, 2]-cross_ab)

# A rank (2,1) extension with commuting blocks can fail the critical equations.
noncritical = {a[0, 0]: 0, a[0, 1]: 0, a[1, 0]: 0, a[1, 1]: 1,
               b[0, 0]: 0, b[0, 1]: 0, b[1, 0]: 0, b[1, 1]: 0,
               alpha: 2, beta: 0, upper_a[0]: 0, upper_a[1]: 0,
               upper_b[0]: 1, upper_b[1]: 0}
assert cross_ab.subs(noncritical) == sp.Matrix([-2, 0])

output = {
    "status": "passed_exact_finite_checks",
    "python": platform.python_version(), "sympy": sp.__version__,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "coefficient_field": "Q", "arithmetic": "exact symbolic polynomials and rational numbers",
    "monomials_total_degree_at_most_four": monomial_checks,
    "calculation_paths": ["projective bundle remainder", "six-root symmetrization and double-root derivative",
                          "direct determinant of the companion matrix"],
    "images_as_free_and_torsion_coefficients": values,
    "euler": str(euler), "torsion_euler": str(sp.factor(euler.subs(c2, c1*c1/4))),
    "coassociative_euler_identity": True, "upper_triangular_potential_identity": True,
    "nonfixed_flag_stabilizer_resultants_zero": len(stabilizers),
    "critical_incidence_counterexample": [-2, 0], "orientation_examples": orientation_checks,
    "limits": ["Finite algebra checks do not prove the support comparison or concentration argument.",
               "No independent review or proof-assistant certification.",
               "No assertion of full-source polynomial cancellation."]}
(report/"calculation-results.json").write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, indent=2))
