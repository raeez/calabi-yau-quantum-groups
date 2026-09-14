#!/usr/bin/env python3
"""Exact finite arithmetic for the stated two-block construction."""
from itertools import product,permutations
from collections import Counter
from fractions import Fraction as Q
import json,random,sys

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def sub(a,b):return [[x-y for x,y in zip(row,other)] for row,other in zip(a,b)]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def f(a,b,c):return tr(mm(a,sub(mm(b,c),mm(c,b))))
def block(a,lo,hi):return [r[lo:hi] for r in a[lo:hi]]
def det3(m):return sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))*m[0][p[0]]*m[1][p[1]]*m[2][p[2]] for p in permutations(range(3)))
random.seed(221121)
for _ in range(1000):
 ms=[[[random.randrange(-3,4) if not(i>=2 and j<2) else 0 for j in range(4)] for i in range(4)] for k in range(3)]
 assert f(*ms)==f(*[block(m,0,2) for m in ms])+f(*[block(m,2,4) for m in ms])
 col=[[random.randrange(-3,4) for j in range(3)] for k in range(3)]
 mats=[[[x,y],[z,-x]] for x,y,z in col]
 assert f(*mats)==2*det3(list(map(list,zip(*col))))
D=[[1,0],[0,-1]];U=[[0,1],[0,0]];L=[[0,0],[1,0]]
assert f(D,U,L)==2
# The value deformation stays in the complement and ends in the positive half-plane.
wall_checks=0
for u,v,t in product(range(-8,9),range(-8,9),[Q(i,10) for i in range(11)]):
 if u<=0 and v<=0:continue
 x,y=Q(u),Q(v)
 if u>0 and v<0:y=(1-t)*v+t*max(Q(v),-Q(u,2))
 if v>0 and u<0:x=(1-t)*u+t*max(Q(u),-Q(v,2))
 assert x>0 or y>0
 assert abs(x)<=abs(u) and abs(y)<=abs(v)
 if u+v>0:assert x+y>0
 if t==1:assert x+y>0
 wall_checks+=1
# Dimensions and normalization from two independent entry counts.
for blocks,gysin in [((2,2),16),((2,1,1),20),((3,1),12),((2,1),8),((1,1),4)]:
 n=sum(blocks);flag=sum(blocks[i]*blocks[j] for i in range(len(blocks)) for j in range(i+1,len(blocks)))
 ambient=3*n*n;incidence=3*(n*n-flag)+flag
 assert 2*(ambient-incidence)==4*flag==gysin
assert 12+8+12==12+4+16==12+20==32
# Complete scalar sum stalk, not the scalar rank4 target.
pairs=list(product((3,5,8),repeat=2))
ranks=Counter(p+q-14 for p,q in pairs)
assert ranks=={-8:1,-6:2,-4:1,-3:2,-1:2,2:1}
assert (-1)**((8-7)*(8-7))==-1
assert all(((-1)**((p-7)*(q-7)))==((-1)**((p+1)*(q+1))) for p,q in pairs)
# Associative relative tensor differential signs, for all parity triples.
for p,q,r in product(range(2),repeat=3):
 assert [1,(-1)**p,(-1)**(p+q)]==[1,(-1)**p,(-1)**p*(-1)**q]
 assert (-1)**(16*p)==(-1)**(20*p)==1
# Ordered (2,1,1) flags on four distinct eigenlines.
flags={(tuple(sorted(p[:2])),p[2],p[3]) for p in permutations(range(4))}
assert len(flags)==12 and 4*3==6*2==12
print(json.dumps({'result':'PASS','python':sys.version.split()[0],'arithmetic':'exact integers and rational arithmetic','seed':221121,'block_potential_tests':1000,'trace_determinant_tests':1000,'support_deformation_tests':wall_checks,'gysin_degrees':{'22':16,'211':20,'31':12,'21':8,'11':4},'scalar_pair_normalized_ranks':dict(sorted(ranks.items())),'scalar_pair_odd_interchange_sign':-1,'regular_flag_trace':12,'scope':'These finite checks verify polynomial, shift, support-plane and sign arithmetic. The sheaf comparison, local tube transport, proper exchange and Gysin compatibility are proved in the mathematical source. Scalar rank4 target cohomology is not calculated.'},indent=2))
