#!/usr/bin/env python3
"""M16 ROT009 independent exact source-conditional two-setting Pauli-control gauge test.
No original PRF code imported. Standard-library Fractions only. No hardware.
"""
from fractions import Fraction as F
from itertools import product
import json, hashlib, math

R0=((F(-3,7),F(-2,7),F(6,7)),(F(6,7),F(-3,7),F(2,7)),(F(2,7),F(6,7),F(3,7)))
P=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)))
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
S=tuple(tuple(sum((P[i][k]*R0[k][j] for k in range(3)),F(0)) for j in range(3)) for i in range(3))
C0=((F(0),F(9,100),F(11,100)),(F(7,100),F(0),F(1,10)),(F(8,100),F(12,100),F(0)))
C=tuple(tuple(F(7,2)*v for v in row) for row in C0)
O=tuple((i,j) for i in range(3) for j in range(3) if i!=j)

def matmul(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(3)),F(0)) for j in range(3)) for i in range(3))
def trans(a):return tuple(zip(*a))
def det(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def proper(a):return matmul(a,trans(a))==I and det(a)==1
assert proper(S) and proper(P)

def chi(v):
    x=v&1; z=(v>>1)&1
    return (1-2*z,1-2*(x^z),1-2*x)

def law(c):
    return {(v,w): F(1,16)*(1+sum((c[i][j]*chi(v)[j]*chi(w)[i] for (i,j) in O),F(0))) for (v,w) in product(range(4),repeat=2)}

def fourier(p):
    return tuple(tuple(sum((pr*chi(v)[j]*chi(w)[i] for (v,w),pr in p.items()),F(0)) for j in range(3)) for i in range(3))

def channel(p,s,q):
    """Full Pauli mixture with middle gate q@s between the two noise intervals."""
    qs=matmul(q,s)
    return tuple(tuple(sum((pr*chi(w)[i]*qs[i][j]*chi(v)[j] for (v,w),pr in p.items()),F(0)) for j in range(3)) for i in range(3))

def tv(p,r):return sum((abs(p[k]-r[k]) for k in p),F(0))/2
p=law(C)
assert sum(p.values())==1 and min(p.values())==F(11,3200) and fourier(p)==C
p2=matmul(P,P)
t=F(1,1000)
Qx=((F(1),F(0),F(0)),(F(0),(1-t*t)/(1+t*t),-2*t/(1+t*t)),(F(0),2*t/(1+t*t),(1-t*t)/(1+t*t)))
# a second non-Clifford proper calibrated middle gate for an all-Q stress check
u=F(1,37)
Qz=(((1-u*u)/(1+u*u),-2*u/(1+u*u),F(0)),(2*u/(1+u*u),(1-u*u)/(1+u*u),F(0)),(F(0),F(0),F(1)))
Qs={'identity':I,'cyclic_P':P,'cyclic_P2':p2,'rational_Rx':Qx,'rational_Rz':Qz}
assert all(proper(q) for q in Qs.values())

# Reproduce PRF ROT024 original W0/W1 continuous ambiguity for a single unknown gate.
Sc=matmul(P,matmul(Qx,R0))
assert proper(Sc)
Cc=tuple(tuple(C[i][j]*S[i][j]/Sc[i][j] if i!=j else F(0) for j in range(3)) for i in range(3))
pc=law(Cc)
assert min(pc.values())>0 and sum(pc.values())==1
assert tv(p,pc)==F(41979,50199950)
assert channel(p,S,I)==channel(pc,Sc,I)
# A true calibrated intra-stage Clifford P, unlike a post-channel left-multiplication,
# BREAKS that continuous alias under SAME p across Q settings.
Delta=tuple(tuple(channel(pc,Sc,P)[i][j]-channel(p,S,P)[i][j] for j in range(3)) for i in range(3))
assert Delta!=tuple(tuple(F(0) for _ in range(3)) for _ in range(3))
nonzero={f'{i}{j}':Delta[i][j] for i in range(3) for j in range(3) if Delta[i][j]!=0}
max_entry=max(nonzero.items(),key=lambda item:abs(item[1]))
max_abs=abs(max_entry[1])
assert max_abs>0

# Two different MIDDLE controls suffice for the 3 *projective* SO3 columns under six-only,
# nonzero C_ij and all S_ij. For any column j, offdiagonal rows i != j yield
# T_P[i,j]/T_I[i,j]=S[(i-1) mod 3,j]/S[i,j]. The two edges connect all 3 rows.
TI=channel(p,S,I); TP=channel(p,S,P)
projective={}
for j in range(3):
    current={j:F(1)}
    ratios={i:TP[i][j]/TI[i][j] for i in range(3) if i!=j}
    for _ in range(3):
        for i,r in ratios.items():
            prev=(i-1)%3
            if i in current and prev not in current:current[prev]=r*current[i]
            if prev in current and i not in current:current[i]=current[prev]/r
    assert len(current)==3
    assert all(current[i]==S[i][j]/S[j][j] for i in range(3))
    norm_sq=sum((current[i]*current[i] for i in range(3)),F(0))
    assert norm_sq==1/S[j][j]**2
    projective[str(j)]=[str(current[i]) for i in range(3)]

# Original SO3 right-input Pauli sign gauge: 4 distinct signs (Klein four)
# allow 4 indistinguishable sources under ANY preannounced intra-stage q,
# even if p_UNIT is guaranteed common across q.
frame_results={}
for v0 in range(4):
    d=chi(v0)
    D=tuple(tuple(F(d[i]) if i==j else F(0) for j in range(3)) for i in range(3))
    assert proper(D)
    SD=matmul(S,D)
    ps={(v,w):p[(v^v0,w)] for (v,w) in product(range(4),repeat=2)}
    assert sum(ps.values())==1 and min(ps.values())==min(p.values()) and fourier(ps)==tuple(tuple(C[i][j]*d[j] for j in range(3)) for i in range(3))
    for nm,q in Qs.items():
        assert channel(p,S,q)==channel(ps,SD,q),(v0,nm)
    frame_results[str(v0)]={'input_pauli_signs':d,'source_TV_vs_BREAK':str(tv(p,ps)),'same_5_Q_channels':True,'min_probability':str(min(ps.values()))}
assert len({row['source_TV_vs_BREAK'] for row in frame_results.values()})>=2
assert all(tv(p,{(v,w):p[(v^v0,w)] for (v,w) in p})>0 for v0 in (1,2,3))

# Condition proof: no further ambiguity for identical I,P controlled transfer matrices
# under six-only fixed nonzero source C, proper S, all nonzero SO3 entries:
# same ratios -> same projective columns; unit columns -> signs; det=+1 -> 4 cases.
# Test the actual example W0/gauge variants, and count 4 exactly.

machine={
 'name':'IW_M16_ROT009_INTRA_STAGE_CLIFFORD_P_TWO_SETTING_PROJECTIVE_SO3_KLEIN_FOUR_GAUGE',
 'original_prf_ROT024_source_p_break_min':str(min(p.values())),
 'original_continuous_one_control_alias_tv':str(tv(p,pc)),
 'new_intra_stage_cyclic_control_nonzero_difference_count':len(nonzero),
 'new_intra_stage_max_coefficient':max_entry[0],
 'new_intra_stage_max_coefficient_signed_exact':str(max_entry[1]),
 'new_intra_stage_max_coefficient_abs_float':float(max_abs),
 'new_intra_stage_full_9_difference':[[str(x) for x in row] for row in Delta],
 'new_two_control_recovered_projective_columns':projective,
 'new_remaining_four_input_pauli_gauge_worlds':frame_results,
 'setting_groups':list(Qs),
 'theorem_scope':'Fixed six-offdiagonal source p_UNIT shared across I and P controls; Cij nonzero for i!=j; S in SO3 all entries nonzero; exact full 3x3 channels; P inter-stage not final postprocessing; distinguish up to input Pauli Klein-four group, not exact source equality; no physical sensor',
 'external_novelty':'NOT_ESTABLISHED: standard gate-set gauge / Pauli frame theory; no novel general SO3 theorem or hardware.'
}
with open('/mnt/data/m16_rot009/m16_rot009_machine.json','w',encoding='utf-8') as o:json.dump(machine,o,indent=2,ensure_ascii=False)
print(json.dumps(machine,indent=2,ensure_ascii=False))
