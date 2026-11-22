#!/usr/bin/env python3
"""Independent SECOND implementation: random exact rational SO3 and source pauli tester.
No import of the primary M16 ROT009 code; tests 100 source and gate examples.
"""
from fractions import Fraction as Q
from random import Random
from itertools import product
import json
r=Random(982241)
P=((Q(0),Q(0),Q(1)),(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)))
def mm(a,b):return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(3)),Q(0)) for j in range(3)) for i in range(3))
def xform(q):
    w,x,y,z=q;n=w*w+x*x+y*y+z*z
    return (((w*w+x*x-y*y-z*z)/n, 2*(x*y-w*z)/n,2*(x*z+w*y)/n),
            (2*(x*y+w*z)/n,(w*w-x*x+y*y-z*z)/n,2*(y*z-w*x)/n),
            (2*(x*z-w*y)/n,2*(y*z+w*x)/n,(w*w-x*x-y*y+z*z)/n))
def ch(v):return ((-1)**((v>>1)&1),(-1)**(((v>>1)&1)^(v&1)),(-1)**(v&1))
def prob(C):return {(v,w):(1+sum((C[i][j]*ch(v)[j]*ch(w)[i] for i in range(3) for j in range(3) if i!=j),Q(0)))/16 for v,w in product(range(4),repeat=2)}
def e(p,S,B):
    QS=mm(B,S)
    return tuple(tuple(sum((val*ch(v)[j]*ch(w)[i]*QS[i][j] for (v,w),val in p.items()),Q(0)) for j in range(3)) for i in range(3))
def proj(t0,t1,j):
    nodes={j:Q(1)}
    for _ in range(3):
        for i in range(3):
            if i==j:continue
            k=(i+2)%3;ratio=t1[i][j]/t0[i][j]
            if i in nodes:nodes[k]=nodes[i]*ratio
            if k in nodes:nodes[i]=nodes[k]/ratio
    return [nodes[i] for i in range(3)]

I=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
passes=0;all_one_alias=0;all_p_separates=0;all_group_orbit=0
for trial in range(100):
    while True:
        vals=(Q(1),Q(r.randint(1,6),10),Q(r.randint(1,6),11),Q(r.randint(1,6),13))
        S=xform(vals)
        if all(x for row in S for x in row) and all(S[i][i] for i in range(3)):break
    C=tuple(tuple(Q(r.randint(1,6),100) if i!=j else Q(0) for j in range(3)) for i in range(3))
    p=prob(C)
    assert min(p.values())>0
    a=e(p,S,I); b=e(p,S,P)
    for j in range(3):
        ans=proj(a,b,j)
        assert ans==[S[k][j]/S[j][j] for k in range(3)],(trial,j,ans)
    passes+=1
    u=Q(r.randint(1,5),1000)
    Snew=mm(xform((Q(1),u,Q(0),Q(0))),S)
    if any(Snew[i][j]==0 for i,j in product(range(3),repeat=2) if i!=j):continue
    Cnew=tuple(tuple(C[i][j]*S[i][j]/Snew[i][j] if i!=j else Q(0) for j in range(3)) for i in range(3))
    pnew=prob(Cnew)
    if min(pnew.values())<=0:continue
    assert e(pnew,Snew,I)==a
    all_one_alias+=1
    assert e(pnew,Snew,P)!=b
    all_p_separates+=1
    D=(Q(-1),Q(-1),Q(1))
    SD=tuple(tuple(S[i][j]*D[j] for j in range(3)) for i in range(3))
    Dsrc=tuple(tuple(C[i][j]*D[j] for j in range(3)) for i in range(3))
    shifted=prob(Dsrc)
    assert min(shifted.values())>0
    assert e(shifted,SD,I)==a and e(shifted,SD,P)==b
    all_group_orbit+=1
assert passes==100 and all_one_alias>=90 and all_p_separates==all_one_alias and all_group_orbit==all_one_alias
out={'exact_rational_randomized_source_cases':passes,'positive_one_control_continuous_alias_cases':all_one_alias,'two_control_P_breaks_nontrivial_continuous_alias_cases':all_p_separates,'two_control_P_does_not_break_input_Pauli_sign_gauge_cases':all_group_orbit,'scope':'100 exact Rational matrices with 6 offdiag Fourier sources; no instrument; not a theorem proof'}
with open('/mnt/data/m16_rot009/m16_rot009_independent_stress.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
