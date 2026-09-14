from itertools import combinations,product
from collections import Counter
import json,sys
import sympy as s
out={'python':sys.version,'sympy':s.__version__}
# Matrix-index enumeration is separate from the dimension formula.
rows=[]
for blocks in [(2,2),(2,1),(4,1),(2,3),(2,2,1)]:
 labels=[i for i,v in enumerate(blocks) for _ in range(v)];n=len(labels)
 lower=[(i,j) for i in range(n) for j in range(n) if labels[i]>labels[j]]
 q=sum(x*y for i,x in enumerate(blocks) for y in blocks[i+1:])
 assert len(lower)==q
 incidence=3*(n*n-len(lower))+q
 deg1=2*(3*n*n-incidence);deg2=6*len(lower)-2*q
 assert deg1==deg2==4*q
 rows.append({'blocks':blocks,'dimension':incidence,'normal_complex_rank':3*q,'flag_dimension':q,'Gysin':deg1})
out['dimensions']=rows
assert rows[-1]['Gysin']==rows[0]['Gysin']+rows[2]['Gysin']==rows[1]['Gysin']+rows[3]['Gysin']==32
# Expand the full three-block potential with all allowed upper entries.
labels=[0,0,1,1,2];M=[]
for name in 'ABC':
 M.append(s.Matrix(5,5,lambda i,j:0 if labels[i]>labels[j] else s.Symbol(f'{name}{i}{j}')))
f=lambda A,B,C:s.trace(A*(B*C-C*B))
f5=s.expand(f(*M));blocks=sum((f(*(m[k:k+2,k:k+2] for m in M)) for k in [0,2]),s.Integer(0))
assert s.expand(f5-blocks)==0
D=s.diag(1,-1);U=s.Matrix([[0,1],[0,0]]);L=U.T
assert f(D,U,L)==2
out['potential']={'upper_block_identity':True,'expanded_terms':len(s.Poly(f5).terms()),'two_nonzero_values':[int(f(D,U,L)),int(f(-D,U,L))]}
A=s.diag(0,0,1,1,2);B=s.zeros(5);B[0,2]=1
assert A*B-B*A==-B
out['critical_support_counterexample']='A=diag(0,0,1,1,2),B=e13,C=0 has commuting diagonal blocks and [A,B]=-e13.'
# Exact centralizer ranks for the companion matrices, including the Jordan collision.
ranks=[]
for n in [2,3,4,5]:
 for val in [0,1,2]:
  A=s.zeros(n)
  for i in range(n-1):A[i,i+1]=1
  A[n-1,0]=val;cols=[]
  for i in range(n):
   for j in range(n):
    E=s.zeros(n);E[i,j]=1;cols.append(s.Matrix(list(E*A-A*E)))
  r=s.Matrix.hstack(*cols).rank();assert r==n*n-n
  ranks.append({'n':n,'s':val,'commutator_rank':r,'quadratic_Hessian_rank':2*r,'coefficient_shift':2*n*n-2*r})
out['cyclic_ranks']=ranks
# Ordered flags and the two actual regular sheet-sum matrices.
universe=set(range(5));flags=[]
for h in combinations(range(5),2):
 for q in combinations(sorted(universe-set(h)),2):flags.append((tuple(h),tuple(q),tuple(sorted(universe-set(h)-set(q)))))
assert len(flags)==30
Ls=sorted({tuple(sorted(h+q)) for h,q,l in flags});Rs=sorted({h for h,q,l in flags})
CL=s.Matrix([[int(tuple(sorted(h+q))==k) for h,q,l in flags] for k in Ls]);CR=s.Matrix([[int(h==k) for h,q,l in flags] for k in Rs])
assert list(s.ones(1,5)*CL)==list(s.ones(1,10)*CR)==[1]*30
assert sorted([sum(CL.row(i)) for i in range(5)])==[6]*5
assert sorted([sum(CR.row(i)) for i in range(10)])==[3]*10
rot=lambda fl:tuple(tuple(sorted((x+1)%5 for x in block)) for block in fl)
perm=[flags.index(rot(f)) for f in flags];seen=set();cycles=[]
for i in range(30):
 if i in seen:continue
 cyc=[];j=i
 while j not in seen:cyc.append(j);seen.add(j);j=perm[j]
 cycles.append(cyc)
assert sorted(map(len,cycles))==[5]*6
T=s.zeros(30)
for i,j in enumerate(perm):T[j,i]=1
assert (T-s.eye(30)).rank()==24
out['regular_maps']={'left_group_sizes':[5,6],'right_group_sizes':[10,3],'same_row':[1]*30,'flags':flags,'base_monodromy_cycles':cycles,'augmentation_invariants':5,'augmentation_coinvariants':5}
# Monic division over Q[e], including all critical pairs; no inversion of e.
a,b,e,t=s.symbols('a b e t')
g1=a**3-a*a*e-2*a*b+a*e*e+b*e-e**3
g2=a*a*b-a*b*e-b*b+b*e*e-e**4
g3=s.expand(a*g2-b*g1);g4=s.expand(a*g3-b*g2);G=[g1,g2,g3,g4]
assert s.expand(b*g3-a*g4-(e**4*g1-e**3*g2+e*e*g3-e*g4))==0
order=lambda m:(m[0]+2*m[1],-m[1])
gb=s.groebner([g1,g2],a,b,domain=s.QQ.poly_ring(e),order=order)
assert set(gb)==set(G)
for i in range(4):
 for j in range(i+1,4):
  li=s.Poly(G[i],a,b,domain=s.QQ.poly_ring(e)).LM(order=order).exponents
  lj=s.Poly(G[j],a,b,domain=s.QQ.poly_ring(e)).LM(order=order).exponents
  lcm=tuple(max(x,y) for x,y in zip(li,lj));u=a**(lcm[0]-li[0])*b**(lcm[1]-li[1]);v=a**(lcm[0]-lj[0])*b**(lcm[1]-lj[1]);assert gb.reduce(s.expand(u*G[i]-v*G[j]))[1]==0
c=e-a;d=e*e-b-a*e+a*a
assert s.expand((t*t+a*t+b)*(t*t+c*t+d)-(t**4+e*t**3+e**2*t*t+e**3*t+e**4))==s.expand(g1*t+g2)
assert s.expand((t-e)*(t**4+e*t**3+e**2*t*t+e**3*t+e**4)-(t**5-e**5))==0
out['flag_algebra']={'monic_relations':[str(g) for g in G],'basis_over_Qe':['1','a','a^2','b','ab','b^2'],'basis_over_Qs':'e^i times each listed basis element,0<=i<5','degree':30,'all_six_S_pairs_reduce_to_zero':True}
# Input scalar degrees and the interchange sign are kept separate from output ranks.
pairs=[{'p':p,'q':q,'degree':p+q-16,'swap_sign':(-1)**((p-7)*(q-7))} for p,q in product([3,5,8],repeat=2)]
assert Counter(x['degree'] for x in pairs)=={-10:1,-8:2,-6:1,-5:2,-3:2,0:1}
assert pairs[-1]['swap_sign']==-1
out['scalar_input']=pairs;out['scope']='Exact finite checks. General derived-map equality is proved in flag221.tex; scalar output ranks are not computed.'
print(json.dumps(out,indent=2))
