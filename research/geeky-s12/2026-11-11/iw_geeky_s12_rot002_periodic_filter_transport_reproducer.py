#!/usr/bin/env python3
"""ROT002: exact rational two-mode periodic filter/orthogonal transport phase.
PUBLIC synthetic mathematical witness, not actual DTC0a TT/masked producer.
"""
from fractions import Fraction as F
import json, math

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(2)) for i in range(2)]
def norm(v):
    return math.sqrt(sum(float(x)**2 for x in v))
def fractions(A):
    return [[str(x) for x in row] for row in A]
def eigens(c):
    disc=(1*c)**2+4*F(6,25)
    return [(-float(c)+math.sqrt(float(disc)))/2,(-float(c)-math.sqrt(float(disc)))/2]

a,b=F(6,5),F(1,5)
E=[[-a,F(0)],[F(0),b]]
threshold=(F(1)-a*b)/(a-b)
assert threshold==F(19,25)
rows=[]
for name,c,s in [('quarter_swap',F(0),F(1)),('stable_3_5',F(3,5),F(4,5)),('unstable_4_5',F(4,5),F(3,5)),('unmixed_1',F(1),F(0))]:
    assert c*c+s*s==1
    U=[[c,-s],[s,c]]
    M=mm(E,U)
    tr=M[0][0]+M[1][1]
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert tr==-(a-b)*c and det==-a*b
    p1=F(1)-tr+det
    pm1=F(1)+tr+det
    assert pm1>0 if c<threshold else pm1<=0
    v=[F(0),F(1)]
    norms={}
    for k in range(0,251):
        if k in (0,1,2,5,10,30,60,120,200,250):norms[str(k)]=norm(v)
        if k<250:v=mv(M,v)
    lam=eigens(c)
    assert ((max(map(abs,lam))<1) == (c<threshold)) or c==1
    rows.append(dict(name=name,c=str(c),s=str(s),U=fractions(U),M=fractions(M),tr=str(tr),det=str(det),p_plus1=str(p1),p_minus1=str(pm1),eigenvalues=lam,spectral_radius=max(map(abs,lam)),initial_stable_mode='e2',one_step_vec=[str(x) for x in mv(M,[F(0),F(1)])],norms_of_M_power_e2=norms))
assert rows[0]['norms_of_M_power_e2']['1']==1.2
assert rows[0]['norms_of_M_power_e2']['2']<1.0
assert rows[1]['norms_of_M_power_e2']['250']<1e-11
assert rows[2]['norms_of_M_power_e2']['250']>100
out=dict(artifact_id='IW_GEEKY_S12_ROT002_ALTERNATING_FILTER_TRANSPORT_PHASE_001_20261111',NCDG_source_role='ABSTRACT_SIGNED_GAIN_LOSS_TWO_MODE_ANALOGUE_ONLY',a=str(a),b=str(b),filter_E=fractions(E),sharp_threshold_cos=str(threshold),cases=rows,assertions='PASS')
print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
