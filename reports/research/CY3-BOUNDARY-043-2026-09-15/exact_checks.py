from pathlib import Path
import itertools
import json
import platform
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

x, y = s.symbols("x y")
I = s.eye(2)
zero = s.zeros(2)
counts = {}

def equal(A, B, name):
    if isinstance(A, s.MatrixBase):
        ok = all(s.expand(v) == 0 for v in A - B)
    else:
        ok = s.expand(A - B) == 0
    assert ok, (name, A, B)
    counts[name] = counts.get(name, 0) + 1

def delta(D, A, parity):
    return D * A - (-1)**parity * A * D

# Arbitrary coefficient variables check the two general differentials
# independently of the polynomial examples.
a,b,p,q,u,v=s.symbols("a b p q u v")
D=s.Matrix([[0,a],[b,0]])
even=s.diag(p,q); odd=s.Matrix([[0,u],[v,0]])
equal(delta(D,even,0), s.Matrix([[0,a*(q-p)],[b*(p-q),0]]), "differentials")
equal(delta(D,odd,1),(a*v+b*u)*I, "differentials")
equal(delta(D,delta(D,even,0),1),zero, "square_zero")
equal(delta(D,delta(D,odd,1),0),zero, "square_zero")

# Rank-one products, Bezout primitives, and expected scalar ideals.
potentials=[x**m for m in range(1,10)]
potentials += [x**m*(x-1)**n for m in range(1,6) for n in range(1,6)]
for W in potentials:
    factors=s.factor_list(W)[1]
    intersection=s.Poly(1,x,domain=s.QQ)
    for js in itertools.product(*[range(m+1) for f,m in factors]):
        aa=s.prod(f**j for (f,m),j in zip(factors,js))
        bb=s.cancel(W/aa)
        gg=s.gcd(aa,bb)
        a0=s.cancel(aa/gg); b0=s.cancel(bb/gg)
        DD=s.Matrix([[0,aa],[bb,0]])
        eta=s.Matrix([[0,a0],[-b0,0]])
        equal(delta(DD,eta,1),zero,"odd_cycles")
        equal(eta*eta,-a0*b0*I,"odd_products")
        equal(delta(DD,s.diag(0,1),0),gg*eta,"odd_boundaries")
        aa_coef,bb_coef,gcd=s.gcdex(aa,bb,x)
        primitive=s.Matrix([[0,bb_coef],[aa_coef,0]])
        equal(delta(DD,primitive,1),gcd*I,"bezout_primitives")
        intersection=s.lcm(intersection,s.Poly(gg,x,domain=s.QQ)).monic()
    expected=s.prod(f**(m//2) for f,m in factors)
    equal(intersection.as_expr(),expected,"common_scalar_ideal")

# Matrix factorizations with genuine polynomial change-of-basis mixing.
# Smith diagonal invariants computed by an independent library algorithm.
for m in range(2,9):
    W=x**m*(x-1)**2
    aa=[x, x**min(m,2)*(x-1), x**m*(x-1)**2]
    A0=s.diag(*aa); B0=s.diag(*[s.cancel(W/f) for f in aa])
    U=s.Matrix([[1,x,x*x],[0,1,x+1],[0,0,1]])
    V=s.Matrix([[1,0,0],[x+2,1,0],[x,x*x,1]])
    A=U*A0*V; B=V.inv()*B0*U.inv()
    equal(A*B,W*s.eye(3),"mixed_factorizations")
    equal(B*A,W*s.eye(3),"mixed_factorizations")
    smith=smith_normal_form(A,domain=s.QQ[x])
    for j,expected in enumerate(aa):
        actual=s.Poly(smith[j,j],x,domain=s.QQ).monic().as_expr()
        equal(actual,expected,"smith_invariants")

# Diagonal formulas, including both retained scalar actions.
for W in [x**m for m in range(1,10)]+[x*x+1,x**3-3*x+2,(x-1)**2*(x+2)**3]:
    r=x-y; g=s.cancel((W-W.subs(x,y))/r)
    DD=s.Matrix([[0,r],[g,0]])
    H=DD.diff(x); Hr=-DD.diff(y)
    equal(DD*DD,(W-W.subs(x,y))*I,"diagonal_square")
    equal(delta(DD,H,1),s.diff(W,x)*I,"left_primitive")
    equal(delta(DD,Hr,1),s.diff(W,x).subs(x,y)*I,"right_primitive")
    equal((H*H).subs(y,x),s.diff(W,x,2)*I/2,"left_hessian")
    equal((Hr*Hr).subs(y,x),-s.diff(W,x,2)*I/2,"right_hessian")
    equal(g.subs(y,x),s.diff(W,x),"diagonal_restriction")
    assert s.gcd(r,g)==1
    counts["regular_diagonal_pair"]=counts.get("regular_diagonal_pair",0)+1

# A rank-one realization of x^2+1; the general contraction is proved
# by differentiating D^2 and does not depend on this representation.
DD=s.Matrix([[0,1],[x*x+1,0]])
h=DD/2-x*DD.diff(x)/2
equal(delta(DD,h,1),I,"nonzero_critical_value_contraction")

# Exact critical-value idempotents, checked in the quotient and with
# actual polynomial matrix homotopies.
for W,values in [(x**3-3*x+2,[s.Integer(0),s.Integer(4)]),
                 ((x*x-1)**2,[s.Integer(0),s.Integer(1)]),
                 (x**4,[s.Integer(0)])]:
    prime=s.diff(W,x)
    r=x-y; g=s.cancel((W-W.subs(x,y))/r)
    DD=s.Matrix([[0,r],[g,0]]); H=DD.diff(x)
    pc={c:s.prod((W-d)/(c-d) for d in values if d!=c) for c in values}
    for c in values:
        equal(s.rem((W-c)*pc[c],prime,x),0,"value_components")
        for d in values:
            defect=s.expand(pc[c]*pc[d]-(pc[c] if c==d else 0))
            quotient,remainder=s.div(defect,prime,x)
            equal(remainder,0,"projector_remainders")
            equal(delta(DD,quotient*H,1),defect*I,"projector_homotopies")
    equal(s.rem(sum(pc.values())-1,prime,x),0,"complete_projectors")

out={"python":platform.python_version(),"sympy":s.__version__,
     "counts":counts,"assertions":sum(counts.values()),
     "scope":"Exact symbolic formulas and stated finite families only; the general theorem is the written proof.",
     "independence":"Separate encodings and Smith library check, all executed by the same main thread; not independent acceptance."}
Path(__file__).with_name("exact-checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
