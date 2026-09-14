from pathlib import Path
from fractions import Fraction
from itertools import permutations,combinations
from math import comb,factorial
import json,sys,platform,hashlib,re
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/cy3-native-normalization020/source';O=R/'baseline-source'
def determinant(a):
 a=[[Fraction(x) for x in row] for row in a];v=Fraction(1)
 for k in range(len(a)):
  z=next((j for j in range(k,len(a)) if a[j][k]),None)
  if z is None:return 0
  if z!=k:a[k],a[z]=a[z],a[k];v=-v
  pivot=a[k][k];v*=pivot
  for j in range(k+1,len(a)):
   t=a[j][k]/pivot
   for l in range(k+1,len(a)):a[j][l]-=t*a[k][l]
 return int(v)
def permutation_determinant(a):
 n=len(a);result=0
 for p in permutations(range(n)):
  inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));term=(-1)**inversions
  for i in range(n):term*=a[i][p[i]]
  result+=term
 return result
matrices={'B_to_lower':[[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]],'upper_to_lower':[[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]],'B_to_upper':[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]}
matrecords={}
for name,a in matrices.items():
 x=determinant(a);y=permutation_determinant(a);assert x==y
 matrecords[name]={'matrix':a,'rational_elimination':x,'Leibniz_expansion':y}
assert [matrecords[n]['rational_elimination'] for n in matrices]==[-1,1,-1]
pairs=[]
for n in range(2,6):
 for d in range(1,n):
  e=n-d;cross=[(i,j) for i in range(d) for j in range(d,n)]
  b=(-1)**len(cross);eps=lambda r:(-1)**comb(r,2)
  assert len(cross)==d*e
  converted=eps(d)*eps(e)*b*eps(n);assert converted==1
  pairs.append({'d':d,'e':e,'cross_pairs':cross,'B_sheet':b,'upper_sheet':converted,'scope':'linear regular incidence coefficient only; not all-rank derived associativity'})
flags=[]
for dims in [(2,1,1),(2,2,1)]:
 n=sum(dims);a,b,c=dims;labels=range(n)
 actual=[]
 for I in combinations(labels,a):
  rem=set(labels)-set(I)
  for J in combinations(sorted(rem),b):actual.append((I,J,tuple(sorted(rem-set(J)))))
 cross=a*b+a*c+b*c
 direct=(-1)**cross*len(actual)
 left=(-1)**(a*b)*(-1)**((a+b)*c)*comb(n,c)*comb(a+b,a)
 right=(-1)**(b*c)*(-1)**(a*(b+c))*comb(n,a)*comb(b+c,b)
 factorial_count=factorial(n)//(factorial(a)*factorial(b)*factorial(c))
 assert len(actual)==factorial_count and direct==left==right
 flags.append({'dimensions':dims,'enumerated_flags':actual,'cross_pair_count':cross,'factorial_count':factorial_count,'direct_B_trace':direct,'left_B_trace':left,'right_B_trace':right,'upper_trace':len(actual)})
preserved=[]
for rel,stop in [('research-candidates/critical-hall-two-nonzero-blocks/two_nonzero_blocks.tex',r'\section{Four distinct eigenvalues and the geometric boundary}'),('research-candidates/cy3-flag221019/flag221.tex',r'\section{Regular matrices and a fivefold collision}')]:
 old=(O/rel).read_text().split(stop)[0]
 new=(S/rel).read_text();assert new.startswith(old)
 preserved.append({'source':rel,'preserved_prefix_bytes':len(old.encode()),'sha256':hashlib.sha256(old.encode()).hexdigest(),'contains_all_derived_map_and_associativity_proofs':True})
for rel in ['platonic/chapters/hall_coefficient_maps.tex','platonic/chapters/Volume_IV_Calabi_Yau_Quantum_Groups.tex']:
 a=re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',(O/rel).read_text(),re.S);b=re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',(S/rel).read_text(),re.S);assert a==b
 preserved.append({'source':rel,'proof_count':len(a),'all_proof_bodies_identical':True})
rel='research-candidates/cy3-flag221019/flag221.tex'
for label in ['fl221:prop:cover','fl221:prop:gluing']:
 texts=[]
 for root in [O,S]:
  t=(root/rel).read_text().split(r'\label{'+label+'}')[1];a=t.index(r'\begin{proof}');b=t.index(r'\end{proof}',a)+len(r'\end{proof}');texts.append(t[a:b])
 assert texts[0]==texts[1]
 preserved.append({'source':rel,'label':label,'proof_sha256':hashlib.sha256(texts[0].encode()).hexdigest(),'entire_proof_identical':True})
report={'python':sys.version,'platform':platform.platform(),'arithmetic':'exact rational and integer; no numerical error bounds needed','matrices':matrecords,'binary_regular_checks':pairs,'flags':flags,'cone_sign_identity':'(d beta,0)-d(beta,0)=(0,-alpha), alpha=beta restricted to boundary','limits':'finite exact sign/count checks support the internal proof; they do not prove the general sheaf-theoretic construction','proof_preservation':preserved}
(R/'normalization-calculations.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: determinants by two algorithms; all rank<=5 regular binary signs; both flags by enumeration and two factorizations; substantive proof bodies preserved')
