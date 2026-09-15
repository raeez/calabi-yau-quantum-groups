from pathlib import Path
from functools import lru_cache
import itertools
import json
import platform
import random
import sympy as s

x,y,u,v=s.symbols("x y u v")
I=s.eye(2)
counts={}


def clean(a):
    return a.applyfunc(lambda z:s.expand(s.cancel(z)))


def eq(a,b,name):
    r=clean(a-b)
    assert r==s.zeros(*r.shape),(name,r)
    counts[name]=counts.get(name,0)+1


def dd(a,z,t):
    return clean((a-a.subs(z,t))/(t-z))


def model1(a,b):
    dy=s.Matrix([[0,a],[b,0]]);dx=dy.subs(y,x)
    potential=s.expand(a*b);g=s.cancel((potential.subs(y,x)-potential)/(x-y))
    q=dy.row_join((x-y)*I).col_join((g*I).row_join(-dy))
    inc=I.col_join(clean((dx-dy)/(x-y)))
    return {'N':dx,'M':q,'i':inc,
            'pi':lambda z:clean(z[:2,:].subs(y,x)),
            'h':lambda z:s.zeros(2,z.cols).col_join(dd(z[:2,:],y,x))}


def model2(a,b):
    dy=s.Matrix([[0,a],[b,0]]);w=s.expand(a*b)
    g1=s.cancel((w.subs(y,x)-w)/(x-y))
    g2=s.cancel((w.subs(y,x).subs(v,u)-w.subs(y,x))/(u-v))
    pre=dy.row_join((x-y)*I).col_join((g1*I).row_join(-dy))
    q=pre.row_join((u-v)*s.eye(4)).col_join((g2*s.eye(4)).row_join(-pre))
    j2=s.eye(4).col_join(clean((pre.subs(v,u)-pre)/(u-v)))
    d0=dy.subs(v,u);dx=d0.subs(y,x)
    j1=I.col_join(clean((dx-d0)/(x-y)))
    def p2(z):return clean(z[:4,:].subs(v,u))
    def hom(z):
        h2=s.zeros(4,z.cols).col_join(dd(z[:4,:],v,u))
        z2=p2(z)
        h1=s.zeros(2,z.cols).col_join(dd(z2[:2,:],y,x))
        return clean(h2+j2*h1)
    return {'N':dx,'M':q,'i':clean(j2*j1),
            'pi':lambda z:clean(p2(z)[:2,:].subs(y,x)),'h':hom}


def lift(f,p,kind):
    if kind=='N':return f
    fy=f.subs(dict(coordinates),simultaneous=True)
    return s.kronecker_product(s.diag(*[(-1)**(p*j) for j in exterior]),fy)


class Co:
    def __init__(self,p,source,target,function):
        self.p=p%2;self.source=source;self.target=target;self.function=function
    @lru_cache(None)
    def cached(self,fs,ps,objs,vec):
        return s.ImmutableMatrix(clean(self.function([s.Matrix(f) for f in fs],list(ps),list(objs),s.Matrix(vec))))
    def __call__(self,fs,ps,objs,vec):
        return s.Matrix(self.cached(tuple(s.ImmutableMatrix(f) for f in fs),tuple(ps),tuple(objs),s.ImmutableMatrix(vec)))
    def __mul__(self,other):
        assert other.target==self.source
        def function(fs,ps,objs,vec):
            out=s.zeros(objects[objs[0]][self.target].rows,vec.cols)
            for j in range(len(fs)+1):
                out+=(-1)**(other.p*sum(p+1 for p in ps[:j]))*self(
                    fs[:j],ps[:j],objs[:j+1],other(fs[j:],ps[j:],objs[j:],vec))
            return out
        return Co(self.p+other.p,other.source,self.target,function)


def constant(p,source,target,action):
    return Co(p,source,target,lambda fs,ps,objs,z:
              s.zeros(objects[objs[0]][target].rows,z.cols) if fs else action(objs[0],z))


def differential(co):
    tf=tau(co.source);tg=tau(co.target)
    left=tg*co;right=co*tf
    def function(fs,ps,objs,z):
        total=co.p+sum(p+1 for p in ps)
        out=objects[objs[0]][co.target]*co(fs,ps,objs,z)
        out-=(-1)**total*co(fs,ps,objs,objects[objs[-1]][co.source]*z)
        for j in range(len(fs)):
            df=clean(objects[objs[j]]['N']*fs[j]-(-1)**ps[j]*fs[j]*objects[objs[j+1]]['N'])
            newps=ps[:j]+[(ps[j]+1)%2]+ps[j+1:]
            out+=(-1)**(co.p+sum(p+1 for p in ps[:j]))*co(fs[:j]+[df]+fs[j+1:],newps,objs,z)
        for j in range(len(fs)-1):
            newfs=fs[:j]+[clean(fs[j]*fs[j+1])]+fs[j+2:]
            newps=ps[:j]+[(ps[j]+ps[j+1])%2]+ps[j+2:]
            out+=(-1)**(co.p+sum(p+1 for p in ps[:j])+ps[j])*co(newfs,newps,objs[:j+1]+objs[j+2:],z)
        return out-left(fs,ps,objs,z)+(-1)**co.p*right(fs,ps,objs,z)
    return Co(co.p+1,co.source,co.target,function)


def tau(kind):
    return Co(1,kind,kind,lambda fs,ps,objs,z:
              lift(fs[0],ps[0],kind)*z if len(fs)==1
              else s.zeros(objects[objs[0]][kind].rows,z.cols))


def make_contraction():
    pi=constant(0,'M','N',lambda o,z:objects[o]['pi'](z))
    def inc(fs,ps,objs,z):
        out=objects[objs[-1]]['i']*z
        for j in range(len(fs)-1,-1,-1):
            out=objects[objs[j]]['h'](lift(fs[j],ps[j],'M')*out)
        return out
    def hom(fs,ps,objs,z):
        out=objects[objs[-1]]['h'](z)
        for j in range(len(fs)-1,-1,-1):
            out=objects[objs[j]]['h'](lift(fs[j],ps[j],'M')*out)
        return (-1)**sum(p+1 for p in ps)*out
    return pi,Co(0,'N','M',inc),Co(1,'M','M',hom)


def bulk(a,p):
    return constant(p,'M','M',lambda o,z:s.kronecker_product(a,I)*z)


def phi(ops,ps):
    result=PI*bulk(ops[0],ps[0])
    for a,p in zip(ops[1:],ps[1:]):result=result*H*bulk(a,p)
    return result*J


def equation(ops,ps,fs,qs,objs,label):
    f=phi(ops,ps);lhs=differential(f)(fs,qs,objs,I)
    rhs=s.zeros(2)
    for j in range(1,len(ops)):
        lhs+=(-1)**(sum(ps[:j])+j-1)*(phi(ops[:j],ps[:j])*phi(ops[j:],ps[j:]))(fs,qs,objs,I)
    for j in range(len(ops)):
        da=clean(diagonal*ops[j]-(-1)**ps[j]*ops[j]*diagonal)
        newps=ps[:j]+[(ps[j]+1)%2]+ps[j+1:]
        rhs+=(-1)**(sum(ps[:j])+j)*phi(ops[:j]+[da]+ops[j+1:],newps)(fs,qs,objs,I)
    for j in range(len(ops)-1):
        newps=ps[:j]+[(ps[j]+ps[j+1])%2]+ps[j+2:]
        rhs+=(-1)**(sum(ps[:j+1])+j)*phi(ops[:j]+[clean(ops[j]*ops[j+1])]+ops[j+2:],newps)(fs,qs,objs,I)
    eq(lhs,rhs,label)


basis=[s.diag(1,0),s.diag(0,1),s.Matrix([[0,1],[0,0]]),s.Matrix([[0,0],[1,0]])]
parities=[0,0,1,1]
objects=[model1(y,y*y),model1(y*y,y)]
coordinates=[(x,y)];exterior=[0,1]
diagonal=s.Matrix([[0,x-y],[x*x+x*y+y*y,0]])
PI,J,H=make_contraction()
random.seed(460915)
for r in range(1,4):
    for m in range(3):
        for _ in range(12):
            bi=[random.randrange(4) for _ in range(r)]
            fi=[random.randrange(4) for _ in range(m)]
            ops=[random.choice([1,x-y,y,x])*basis[j] for j in bi]
            fs=[random.choice([1,x,x*x,x**3])*basis[j] for j in fi]
            equation(ops,[parities[j] for j in bi],fs,[parities[j] for j in fi],
                     [j%2 for j in range(m+1)],"one_variable_mixed_identity")

iota=basis[2]
for r in range(1,7):
    f=phi([iota]*r,[1]*r)
    for obj in range(2):
        eq(f([],[],[obj],I),(-1)**(r-1)*objects[obj]['N'].diff(x,r)/s.factorial(r),"derivative_nullary")
    for power in [r,r+1,r+2]:
        ff=x**power*I
        eq(f([ff],[0],[0,1],I),(-1)**r*ff.diff(x,r)/s.factorial(r),"derivative_unary")
    eq(f([x*I,x*I],[0,0],[0,1,0],I),s.zeros(2),"one_variable_higher_boundary_arity")

objects=[model2(y,y*y+v*v),model2(y*y+v*v,y)]
coordinates=[(x,y),(u,v)];exterior=[0,1,1,0]
g1=x*x+x*y+y*y+v*v;g2=x*(u+v)
diagonal=s.Matrix([[0,x-y,u-v,0],[g1,0,0,u-v],[g2,0,0,-(x-y)],[0,g2,-g1,0]])
PI,J,H=make_contraction()
big=[]
for i in range(4):
    for j in range(4):
        a=s.zeros(4);a[i,j]=1
        big.append((a,(exterior[i]+exterior[j])%2))
for r,m in [(1,2),(2,0),(2,1),(2,2),(3,0),(3,1)]:
    for _ in range(6):
        selected=[random.choice(big) for _ in range(r)]
        fi=[random.randrange(4) for _ in range(m)]
        fs=[random.choice([1,x,u,x*u])*basis[j] for j in fi]
        equation([a for a,p in selected],[p for a,p in selected],fs,
                 [parities[j] for j in fi],[random.randrange(2) for _ in range(m+1)],
                 "two_variable_mixed_identity")

# Strong contraction identities inside the coherent transformation category.
dpi,dj,dh=differential(PI),differential(J),differential(H)
pj,ph,hj,hh,jp=PI*J,PI*H,H*J,H*H,J*PI
for fs,ps,objs in [([],[],[0]),([x*I],[0],[0,1]),
                   ([u*basis[2],x*basis[3]],[1,1],[0,1,0])]:
    mn=objects[objs[-1]]['M'].rows
    vec=(1+y*v)*s.eye(mn)
    eq(dpi(fs,ps,objs,vec),s.zeros(2,mn),"closed_projection")
    eq(dj(fs,ps,objs,I),s.zeros(objects[objs[0]]['M'].rows,2),"closed_inclusion")
    eq(dh(fs,ps,objs,vec),(vec if not fs else s.zeros(mn))-jp(fs,ps,objs,vec),"coherent_homotopy")
    eq(pj(fs,ps,objs,I),I if not fs else s.zeros(2),"retraction")
    eq(ph(fs,ps,objs,vec),s.zeros(2,mn),"projection_homotopy")
    eq(hj(fs,ps,objs,I),s.zeros(mn,2),"homotopy_inclusion")
    eq(hh(fs,ps,objs,vec),s.zeros(mn),"square_zero_homotopy")
for r in range(2,4):
    for j in range(r):
        ops=[big[3][0]]*r;ps=[big[3][1]]*r;ops[j]=s.eye(4);ps[j]=0
        for fs,qs in [([],[]),([x*u*I],[0]),([x*I,u*I],[0,0])]:
            eq(phi(ops,ps)(fs,qs,[0]*(len(fs)+1),I),s.zeros(2),"strict_bulk_units")
for m in range(1,4):
    fs=[x*u*I]*m
    for j in range(m):
        ff=fs.copy();ff[j]=I
        eq(phi([big[3][0],big[12][0]],[big[3][1],big[12][1]])(
            ff,[0]*m,[0]*(m+1),I),s.zeros(2),"normalized_boundary_units")
result={'python':platform.python_version(),'sympy':s.__version__,'counts':counts,
        'assertions':sum(counts.values()),
        'scope':'Exact mixed A-infinity identities with nonclosed bulk and boundary inputs, two boundary objects, one and two variables; coherent strong contraction; strict bulk and boundary units; independent derivative formulas through six bulk inputs. General proofs carry all arities.',
        'acceptance':'Main-thread diagnostics. No fresh independent mathematical acceptance.'}
Path(__file__).with_name('checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
