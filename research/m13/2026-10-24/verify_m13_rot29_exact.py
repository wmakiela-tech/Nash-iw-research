#!/usr/bin/env python3
"""Pure-stdlib independent exact rational minimax certificate and constructive
low-band nonidentifiability sign proof (N=41 cosine lattice)."""
from fractions import Fraction as Q
from math import cos, pi, fsum
import json

KS=range(2,7)
q={k:Q((k-4)**2,2)-1 for k in KS}
w={2:Q(3),3:Q(0),4:Q(-3),5:Q(0),6:Q(1)}
assert max(abs(q[k]) for k in KS)==1
assert all(sum(w[k]*k**p for k in KS)==int(p==0) for p in range(3))
assert sum(w[k]*q[k] for k in KS)==7==sum(abs(w[k]) for k in KS)
assert Q((0-4)**2,2)-1==7
v={2:Q(3,2),6:Q(-1,2)}
assert sum(v.values())==1 and sum(k*vv for k,vv in v.items())==0
assert all(abs(Q(4-k,2))<=1 for k in KS)
assert Q(4,2)==2==sum(abs(a) for a in v.values())

# Cubic/full fourth-order correction moment identities.
for W,maxdegree in [({2:Q(6),3:Q(-8),4:Q(3)},2),
                    ({2:Q(10),3:Q(-20),4:Q(15),5:Q(-4)},3),
                    ({2:Q(15),3:Q(-40),4:Q(45),5:Q(-24),6:Q(5)},4)]:
    assert all(sum(a*k**p for k,a in W.items())==int(p==0) for p in range(maxdegree+1))

N=41; c=20;th=2*pi/N
f=lambda j: cos(th*(j-c))
roots=[f(k) for k in range(2,6)]
assert roots==sorted(roots)
H=lambda x: (x-roots[0])*(x-roots[1])*(x-roots[2])*(x-roots[3])
assert all(H(f(j))>0 for j in range(6,35))
lam=fsum(H(f(j))*f(j) for j in range(6,35))/fsum(H(f(j)) for j in range(6,35))
assert min(f(j) for j in range(6,35))<lam<max(f(j) for j in range(6,35))
V=lambda j: H(f(j))*(f(j)-lam)
assert max(abs(V(j)) for j in (2,3,4,5,35,36,37,38))<8e-15
assert abs(fsum(V(j) for j in range(6,35)))<6e-14
masked={k:fsum(V(j) for j in range(k,N-k)) for k in KS}
assert max(abs(z) for z in masked.values())<7e-14
boundary=[V(j) for j in (0,1,39,40)]
assert all(x<0 for x in boundary)
full=fsum(V(j) for j in range(N))
assert full<0 and abs(full-fsum(boundary))<8e-14

print(json.dumps({'two_mask_first_order_L1_min':2,'three_mask_second_order_L1_min':7,'dual_values':{str(k):str(q[k]) for k in KS},'nonmap_lambda':lam,'nonmap_interior_sum':fsum(V(j) for j in range(6,35)),'nonmap_max_mask_sum_residual':max(abs(z) for z in masked.values()),'nonmap_full_sum_negative':full,'proof_status':'MOMENTS_EXACT_FRACTIONS_AND_SIGN_CONSTRUCTION_NUMERIC_VERIFIED'},indent=2))