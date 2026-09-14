from itertools import combinations, permutations
from math import factorial
from fractions import Fraction as F
from pathlib import Path
import json

records=[]
for n in range(2,6):
 decorations=[0]*n
 for positions in combinations(range(n),2):
  for singles in permutations(range(n-2)):
   decorations[positions[0]]-=1
   decorations[positions[1]]+=1
 predicted=[(2*k-n-1)*factorial(n-2) for k in range(1,n+1)]
 assert decorations==predicted
 assert decorations[-1]==factorial(n-1)
 pairs=[]
 for d in range(1,n):
  e=n-d
  direct=[F(sum(decorations[d:]),factorial(d)*factorial(e))]
  formula=[F(factorial(n-2),factorial(d-1)*factorial(e-1))]
  if d>=2:
   direct.append(F(decorations[d-1],factorial(d-1)*factorial(e)))
   formula.append(F((d-e-1)*factorial(n-2),factorial(d-1)*factorial(e)))
  if e>=2:
   direct.append(F(decorations[-1],factorial(d)*factorial(e-1)))
   formula.append(F(factorial(n-1),factorial(d)*factorial(e-1)))
  assert direct==formula and direct[0]>0
  pairs.append({'ranks':[d,e],'image':[str(x) for x in direct]})
 # Every basis wedge of two edge classes has a vertex permutation swapping its edges.
 edges=list(combinations(range(n),2));witnesses=0
 for e,f in combinations(edges,2):
  found=False
  for p in permutations(range(n)):
   if tuple(sorted(p[i] for i in e))==f and tuple(sorted(p[i] for i in f))==e:
    found=True;break
  assert found;witnesses+=1
 records.append({'n':n,'decoration_values':decorations,'pairs':pairs,'edge_wedge_swap_witnesses':witnesses})
triples=[]
for d,e,f in [(1,1,1),(2,1,1),(2,2,1)]:
 n=d+e+f;v=[(2*k-n-1)*factorial(n-2) for k in range(1,n+1)];den=factorial(d)*factorial(e)*factorial(f)
 values=[F(sum(v[d:]),den),F(sum(v[d+e:]),den)]
 if d>=2:values.append(F(v[d-1],factorial(d-1)*factorial(e)*factorial(f)))
 if e>=2:values.append(F(v[d+e-1],factorial(d)*factorial(e-1)*factorial(f)))
 if f>=2:values.append(F(v[-1],factorial(d)*factorial(e)*factorial(f-1)))
 triples.append({'ranks':[d,e,f],'image':[str(x) for x in values]})
assert [t['image'] for t in triples]==[['2','2'],['4','3','-2'],['9','6','-6','6']]
result={'result':'PASS','ranks':records,'triples':triples,'scope':'Exact component counts, rational normalization, and finite symmetric-group witnesses. The topology and Hall support maps are proved in the TeX.'}
Path(__file__).with_name('first-higher-calculations.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
