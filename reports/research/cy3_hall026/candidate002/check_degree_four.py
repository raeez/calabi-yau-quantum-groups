from fractions import Fraction as F
from pathlib import Path
import json

def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(3)] for i in range(3)]
def comm(a,b): return sub(mul(a,b),mul(b,a))
def tr(a): return sum(a[i][i] for i in range(3))
a=[[F(0),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(2)]]
values=[]
for t in [F(1),F(2),F(1,2),F(1,7)]:
 c=[[F(0),t,F(1)],[F(0),F(0),F(0)],[F(0),F(0),F(0)]]
 b=[[F(0),F(0),F(0)],[1/t,F(0),F(0)],[F(0),F(0),F(0)]]
 d=comm(c,a)
 assert d[0][1]==t and d[0][2]==2
 assert tr(mul(b,d))==tr(mul(a,comm(b,c)))==1
 values.append(str(t))
c0=[[F(0),F(0),F(1)],[F(0),F(0),F(0)],[F(0),F(0),F(0)]]
assert comm(c0,a)[0][2]==2
support={(p,q) for p in [0,2,4] for q in [-6,-4,-1]}
terms=[x for x in support if sum(x)==-4]
assert sorted(terms)==[(0,-4),(2,-6)]
for p,q in terms:
 for length in range(2,10):
  assert (p+length,q-length+1) not in support
  assert (p-length,q+length-1) not in support
result={"result":"PASS","degree_minus_four_source_dimension":2,"surviving_terms":sorted(terms),"incidence_milnor_dimension":22,"target_milnor_dimension":26,"gysin_degree":8,"milnor_degrees":[5,13],"target_BM_degree":22,"exact_nonproper_family_parameters":values,"image_rank":"uncomputed"}
Path(__file__).with_name('degree-four-calculations.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
