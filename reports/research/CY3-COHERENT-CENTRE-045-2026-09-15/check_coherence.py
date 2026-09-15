from pathlib import Path
from functools import lru_cache
import itertools
import json
import platform
import random
import sympy as s

x, y, u, v = s.symbols("x y u v")
I = s.eye(2)
counts = {}


def clean(a):
    return a.applyfunc(lambda z: s.expand(s.cancel(z)))


def equal(a, b, label):
    residual = clean(a - b)
    assert residual == s.zeros(*residual.shape), (label, residual)
    counts[label] = counts.get(label, 0) + 1


def dd(a, variable, replacement):
    return clean((a - a.subs(variable, replacement)) / (replacement - variable))


def one(a, b):
    dy = s.Matrix([[0, a], [b, 0]])
    dx = dy.subs(y, x)
    inc = I.col_join(clean((dx - dy) / (x - y)))
    def pi(z):
        return clean(z[:2, :].subs(y, x))
    def hom(z):
        return s.zeros(2, z.cols).col_join(dd(z[:2, :], y, x))
    return dx, inc, pi, hom


def two(a, b):
    dy = s.Matrix([[0, a], [b, 0]])
    potential = s.expand(a * b)
    g1 = s.cancel((potential.subs(y, x) - potential) / (x - y))
    pre = dy.row_join((x - y) * I).col_join((g1 * I).row_join(-dy))
    inc2 = s.eye(4).col_join(clean((pre.subs(v, u) - pre) / (u - v)))
    dyu = dy.subs(v, u)
    dx = dyu.subs(y, x)
    inc1 = I.col_join(clean((dx - dyu) / (x - y)))
    def pi2(z):
        return clean(z[:4, :].subs(v, u))
    def h2(z):
        return s.zeros(4, z.cols).col_join(dd(z[:4, :], v, u))
    def pi(z):
        return clean(pi2(z)[:2, :].subs(y, x))
    def hom(z):
        z2 = pi2(z)
        h1 = s.zeros(2, z2.cols).col_join(dd(z2[:2, :], y, x))
        return clean(h2(z) + inc2 * h1)
    return dx, clean(inc2 * inc1), pi, hom


basis = [s.diag(1, 0), s.diag(0, 1),
         s.Matrix([[0, 1], [0, 0]]), s.Matrix([[0, 0], [1, 0]])]
parity = [0, 0, 1, 1]
diagonal = s.Matrix([[0, x-y], [x*x+x*y+y*y, 0]])
objects = [one(y, y*y), one(y*y, y)]
variables = [(x, y)]
exterior_parities = [0, 1]


def lift(f, degree):
    fy = f.subs(dict(variables), simultaneous=True)
    return s.kronecker_product(s.diag(*[(-1)**(degree*j) for j in exterior_parities]), fy)


@lru_cache(None)
def component(a, maps, degrees, labels):
    out = objects[labels[-1]][1]
    for j in range(len(maps)-1, -1, -1):
        out = objects[labels[j]][3](clean(lift(s.Matrix(maps[j]), degrees[j]) * out))
    return s.ImmutableMatrix(objects[labels[0]][2](s.kronecker_product(s.Matrix(a), I)*out))


def eta(a, maps, degrees, labels):
    return s.Matrix(component(s.ImmutableMatrix(a),
                    tuple(s.ImmutableMatrix(f) for f in maps), tuple(degrees), tuple(labels)))


def delta_map(f, degree, target, source):
    return clean(objects[target][0]*f - (-1)**degree*f*objects[source][0])


def equation(a, p, maps, degrees, labels, label):
    n = len(maps)
    value = eta(a, maps, degrees, labels)
    lhs = delta_map(value, p+sum(degrees)+n, labels[0], labels[-1])
    if n:
        lhs += (-1)**(p+sum(degrees[:-1])+n-1) * eta(a, maps[:-1], degrees[:-1], labels[:-1])*maps[-1]
        lhs += (-1)**((p+1)*(degrees[0]+1)+degrees[0]) * maps[0]*eta(a, maps[1:], degrees[1:], labels[1:])
    for j in range(n):
        changed = maps[:j]+[delta_map(maps[j], degrees[j], labels[j], labels[j+1])]+maps[j+1:]
        changed_degrees = degrees[:j]+[(degrees[j]+1)%2]+degrees[j+1:]
        lhs += (-1)**(p+sum(degrees[:j])+j)*eta(a, changed, changed_degrees, labels)
    for j in range(n-1):
        changed = maps[:j]+[clean(maps[j]*maps[j+1])]+maps[j+2:]
        changed_degrees = degrees[:j]+[(degrees[j]+degrees[j+1])%2]+degrees[j+2:]
        changed_labels = labels[:j+1]+labels[j+2:]
        lhs += (-1)**(p+sum(degrees[:j+1])+j)*eta(a, changed, changed_degrees, changed_labels)
    da = clean(diagonal*a - (-1)**p*a*diagonal)
    equal(lhs, eta(da, maps, degrees, labels), label)


for n in range(4):
    for word in itertools.product(range(4), repeat=n):
        degrees = [parity[j] for j in word]
        maps = [(1+x+x*x)*basis[j] for j in word]
        labels = [j%2 for j in range(n+1)]
        for a, p in zip(basis, parity):
            equation(a, p, maps, degrees, labels, "one_variable_cochain_equation")

# The cubic primitive, computed both by the diagonal contraction and differentiation.
a = (basis[2]+(2*x+y)*basis[3])/3
for obj in range(2):
    equal(eta(a, [], [], [obj]), objects[obj][0].diff(x)/3, "cubic_primitive_nullary")
for j, f in enumerate(basis):
    f = (1+x+x*x)*f
    equal(eta(a, [f], [parity[j]], [0, 1]), -f.diff(x)/3, "cubic_primitive_unary")
    equal(eta(a, [f, f], [parity[j]]*2, [0, 1, 0]), s.zeros(2), "cubic_primitive_higher")
b, beta = s.symbols("b beta")
h = s.Matrix([[0, b], [beta-x*b, 0]])
e = s.Matrix([[0, 1], [-x, 0]])
equal(delta_map(h, 1, 0, 0), beta*x*I, "general_cubic_nullary_equation")
equal(h*e+e*h, (beta-2*x*b)*I, "general_cubic_unary_obstruction")

# Two variables include nonzero quadratic cochain components.
objects = [two(y, y*y+v*v), two(y*y+v*v, y)]
variables = [(x, y), (u, v)]
exterior_parities = [0, 1, 1, 0]
r1, r2 = x-y, u-v
g1, g2 = x*x+x*y+y*y+v*v, x*(u+v)
diagonal = s.Matrix([[0,r1,r2,0], [g1,0,0,r2],
                     [g2,0,0,-r1], [0,g2,-g1,0]])
component.cache_clear()
bulk = []
for i in range(4):
    for j in range(4):
        z = s.zeros(4); z[i,j] = 1
        bulk.append((z, (exterior_parities[i]+exterior_parities[j])%2))
random.seed(450915)
for n in range(5):
    for _ in range(16):
        a, p = random.choice(bulk)
        inds = [random.randrange(4) for _ in range(n)]
        maps = [random.choice([x,u,x*u,x*x+u,1])*basis[j] for j in inds]
        degrees = [parity[j] for j in inds]
        labels = [random.randrange(2) for _ in range(n+1)]
        equation(a, p, maps, degrees, labels, "two_variable_cochain_equation")

extract_top = s.zeros(4); extract_top[0,3] = 1
nonzero = eta(extract_top, [u*I,x*I], [0,0], [0,0,0])
assert nonzero != s.zeros(2), nonzero
equal(nonzero, I, "nonzero_binary_component")
for n in range(1,5):
    for pos in range(n):
        maps = [x*u*I for _ in range(n)]; maps[pos] = I
        equal(eta(extract_top, maps, [0]*n, [0]*(n+1)), s.zeros(2), "normalization")
result = {"python":platform.python_version(), "sympy":s.__version__, "counts":counts,
          "assertions":sum(counts.values()), "binary_example":str(nonzero),
          "scope":"Exact cochain commutator equations with nonclosed bulk and boundary matrices, two distinct boundary objects, arities zero through four, and an actual nonzero binary component. Finite diagnostics supplement the general written proof.",
          "acceptance":"Main-thread checks, not fresh independent mathematical acceptance."}
Path(__file__).with_name("checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
