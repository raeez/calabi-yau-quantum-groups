from pathlib import Path
from functools import lru_cache
import itertools
import json
import platform
import random
import sympy as s

x,y,u,v=s.symbols("x y u v")
I=s.eye(2); O=s.zeros(2); counts={}

def clean(M):
    return M.applyfunc(lambda f:s.expand(s.cancel(f)))

def eq(A,B,name):
    C=clean(A-B)
    assert C==s.zeros(*C.shape),(name,C)
    counts[name]=counts.get(name,0)+1

def divdiff(M,z,t):
    return clean((M-M.subs(z,t))/(t-z))

def one_variable(a,b):
    W=s.expand(a*b)
    D=s.Matrix([[0,a],[b,0]])
    Dx=D.subs(y,x)
    r=x-y;g=s.cancel((W.subs(y,x)-W)/r)
    Q=D.row_join(r*I).col_join((g*I).row_join(-D))
    A=clean((Dx-D)/r); J=I.col_join(A)
    def pi(F):return clean(F[:2,:].subs(y,x))
    def h(F):return s.zeros(2,F.cols).col_join(divdiff(F[:2,:],y,x))
    eq(Q*Q,W.subs(y,x)*s.eye(4),"one_square")
    eq(Q*J,J*Dx,"one_inclusion")
    eq(pi(J),I,"one_retraction")
    eq(h(J),s.zeros(4,2),"one_hi")
    for degree in range(5):
        for idx in range(4):
            z=s.zeros(4,1);z[idx]=y**degree
            eq(Q*h(z)+h(Q*z),z-J*pi(z),"one_homotopy")
            eq(pi(Q*z),Dx*pi(z),"one_projection")
            eq(pi(h(z)),s.zeros(2,1),"one_ph")
            eq(h(h(z)),s.zeros(4,1),"one_h_square")
    return D,Dx,Q,J,pi,h,g

for a,b in [(y,0),(1,1),(y,y),(y,y**2),(y**2,y**3),(1,y*y+1),
            (y-1,(y-1)*(y+2)),(y*y+1,y*y-2)]:
    one_variable(a,b)

# Two variables: independent block assembly with the outer theta_2 order.
for a,b in [(y,y*y+v*v),(y*v,y*v)]:
    D=s.Matrix([[0,a],[b,0]]);W=s.expand(a*b)
    W_xv=W.subs(y,x);W_xu=W_xv.subs(v,u)
    r1=x-y;r2=u-v
    g1=s.cancel((W_xv-W)/r1);g2=s.cancel((W_xu-W_xv)/r2)
    pre=D.row_join(r1*I).col_join((g1*I).row_join(-D))
    Q=pre.row_join(r2*s.eye(4)).col_join((g2*s.eye(4)).row_join(-pre))
    pre0=pre.subs(v,u)
    A2=clean((pre0-pre)/r2);J2=s.eye(4).col_join(A2)
    def p2(F):return clean(F[:4,:].subs(v,u))
    def h2(F):return s.zeros(4,F.cols).col_join(divdiff(F[:4,:],v,u))
    D0=D.subs(v,u);Dx=D0.subs(y,x)
    A1=clean((Dx-D0)/r1);J1=I.col_join(A1)
    def p1(F):return clean(F[:2,:].subs(y,x))
    def h1(F):return s.zeros(2,F.cols).col_join(divdiff(F[:2,:],y,x))
    J=clean(J2*J1)
    def pi(F):return p1(p2(F))
    def h(F):return clean(h2(F)+J2*h1(p2(F)))
    eq(Q*Q,W_xu*s.eye(8),"two_square")
    eq(Q*J,J*Dx,"two_inclusion")
    eq(pi(J),I,"two_retraction")
    for ay,av in [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)]:
        for idx in range(8):
            z=s.zeros(8,1);z[idx]=y**ay*v**av
            eq(Q*h(z)+h(Q*z),z-J*pi(z),"two_homotopy")
            eq(pi(Q*z),Dx*pi(z),"two_projection")
            eq(h(h(z)),s.zeros(8,1),"two_h_square")
            eq(pi(h(z)),s.zeros(2,1),"two_ph")
    if a==y:
        N=s.Matrix([[0,0],[u+v,0]]);P0=s.diag(1,0)
        displayed=I.col_join(s.Matrix([[0,1],[x+y,0]])).col_join(N).col_join((u+v)*P0)
        eq(J,displayed,"mixed_display")
        omitted=J.copy();omitted[6:8,:]=s.zeros(2)
        defect=clean(Q*omitted-omitted*Dx)
        eq(defect[2:4,:],-(u*u-v*v)*P0,"mixed_omission_defect")

# A-infinity identity tested with source differentials retained.
D,Dx,Q,J,pi,h,g=one_variable(y,y*y)
DK=s.Matrix([[0,x-y],[g,0]])
def L(a):return s.kronecker_product(a,I)
@lru_cache(None)
def component(args):
    out=J
    for idx in range(len(args)-1,-1,-1):
        out=clean(L(s.Matrix(args[idx]))*out)
        if idx:out=h(out)
    return s.ImmutableMatrix(pi(out))

def phi(ops):
    return s.Matrix(component(tuple(s.ImmutableMatrix(a) for a in ops)))

def delta(a,p):return clean(DK*a-(-1)**p*a*DK)
def equation(ops,parities):
    n=len(ops);F=phi(ops);p=sum(parities)+n-1
    lhs=clean(Dx*F-(-1)**p*F*Dx)
    rhs=s.zeros(2)
    for j in range(1,n):
        lhs+=(-1)**(sum(parities[:j])+j-1)*phi(ops[:j])*phi(ops[j:])
    for j in range(n):
        modified=ops[:j]+[delta(ops[j],parities[j])]+ops[j+1:]
        rhs+=(-1)**(sum(parities[:j])+j)*phi(modified)
    for j in range(n-1):
        modified=ops[:j]+[clean(ops[j]*ops[j+1])]+ops[j+2:]
        rhs+=(-1)**(sum(parities[:j+1])+j)*phi(modified)
    eq(lhs,rhs,"ainfinity_identity")

basis=[s.diag(1,0),s.diag(0,1),s.Matrix([[0,1],[0,0]]),s.Matrix([[0,0],[1,0]])]
par=[0,0,1,1]
for n in range(1,5):
    for word in itertools.product(range(4),repeat=n):
        equation([basis[j] for j in word],[par[j] for j in word])
random.seed(44015)
for _ in range(80):
    n=random.randint(2,4);word=[random.randrange(4) for j in range(n)]
    coeff=[random.choice([y,x-y,y*y,x+y,1]) for j in range(n)]
    equation([coeff[j]*basis[word[j]] for j in range(n)],[par[j] for j in word])

for n in range(2,5):
    for j in range(n):
        for a in basis:
            word=[a]*n;word[j]=I
            eq(phi(word),s.zeros(2),"strict_units")
eq(phi([I]),I,"linear_unit")
iota,epsilon=basis[2:]
eq(phi([iota]),s.Matrix([[0,1],[2*x,0]]),"operator_example")
eq(phi([epsilon]),s.zeros(2),"operator_example")
eq(phi([iota*epsilon]),I,"operator_example")
eq(phi([iota,(x-y)*I]),I,"operator_example")
eq(phi([iota,epsilon]),s.zeros(2),"operator_example")

# Closed source and boundary operators for the stated central homotopy.
eta=(x-y)*iota-g*epsilon
boundary_eta=s.Matrix([[0,1],[-y,0]])
for aa,p in [(I,0),(y*I,0),(eta,1)]:
    for ff,q in [(I,0),(y*I,0),(boundary_eta,1)]:
        Fx=ff.subs(y,x)
        TF=s.diag(1,(-1)**q)
        TF=s.kronecker_product(TF,ff)
        chi=(-1)**(p+1)*pi(L(aa)*h(TF*J))
        dchi=clean(Dx*chi-(-1)**(p+q+1)*chi*Dx)
        eq(dchi,phi([aa])*Fx-(-1)**(p*q)*Fx*phi([aa]),"central_homotopy")

result={"python":platform.python_version(),"sympy":s.__version__,"counts":counts,
        "assertions":sum(counts.values()),
        "scope":"One- and two-variable finite polynomial cases; all four matrix units through arity four plus 80 variable-coefficient words. Nonclosed source differentials are included. Written proofs, not these finite cases, establish all variables and all arities.",
        "independence":"Main-thread diagnostic checks using separately assembled matrices; no fresh independent acceptance."}
Path(__file__).with_name("checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
