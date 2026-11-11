#!/usr/bin/env python3
"""Geeky-S12 ROT001 scalar auxiliary Fourier-mode reachability check.
Not a TT/tensor/original masked DTC0a runtime or physical test. Stdlib only.
"""
import json, math
from collections import defaultdict
N, alpha = 7, 0.2
h = 2*math.pi/N
seed = (1,1,1)
target = (3,3,2)
# C=(cos z, cos x, cos y), L=sum C_j D_j, centered D.
shift_axis = (2,0,1)
def q(k):
    return 1-4*alpha*sum(math.sin(math.pi*i/N)**2 for i in k)
def L(v):
    w=defaultdict(complex)
    for k,a in v.items():
        for j,axis in enumerate(shift_axis):
            z=0.5j*math.sin(2*math.pi*k[j]/N)/h
            for sign in (-1,1):
                kk=list(k)
                kk[axis]=(kk[axis]+sign)%N
                w[tuple(kk)]+=a*z
    return {k:a for k,a in w.items() if abs(a)>1e-14}
def norm(v):
    return math.sqrt(sum(abs(a)**2 for a in v.values()))
f={seed:0.5, tuple(-i%N for i in seed):0.5}
v=f.copy()
layers=[]
for depth in range(7):
    unstable=[k for k in v if abs(q(k))>1+1e-12]
    layers.append([depth,len(v),len(unstable),max(abs(q(k)) for k in v)])
    if depth==5: at5=v.copy()
    if depth<6: v=L(v)
assert [x[2] for x in layers[:5]]==[0]*5
assert layers[5][2]>0 and abs(at5[target])>1e-9
assert abs(q(seed))<1 and abs(q(target))>1
low=min(math.sin(2*math.pi*j/N) for j in (1,2,3))
bound=15*(low/(2*h))**5
assert abs(at5[target])>=bound-1e-12
growth=[]
for m in (0,10,100,500,1000):
    vnorm=math.sqrt(sum(abs(a)**2*abs(q(k))**(2*m) for k,a in at5.items()))
    lower=math.sqrt(2)*abs(at5[target])*abs(q(target))**m
    assert vnorm+1e-10>=lower
    growth.append([m,vnorm,lower])
# C's jth coefficient depends on a coordinate other than j.
# Hence multiplication by C_j commutes with skew-adjoint D_j,
# so L is skew-adjoint and exp(tL) is exactly norm preserving.
t=0.5
v=f.copy()
u=defaultdict(complex)
for r in range(32):
    for k,a in v.items():
        u[k]+=(t**r/math.factorial(r))*a
    v=L(v)
assert abs(norm(u)-norm(f))<2e-12
assert abs(u[target])>1e-8
# Control C_source=(0,cos x,0): only x frequency shifts.
# A start with ky=kz=1 cannot reach an unstable E band.
src={}
for nn in (7,31,41):
    s=[1-4*alpha*(math.sin(math.pi*k/nn)**2+
                       2*math.sin(math.pi/nn)**2) for k in range(nn)]
    src[str(nn)]=max(abs(a) for a in s)
    assert src[str(nn)]<=1+1e-14
print(json.dumps(dict(N=N,alpha=alpha,first_unstable_depth=5,
    q_initial=q(seed),q_target=q(target),
    L5_target_abs=abs(at5[target]),analytic_lower=bound,
    layers=layers,growth=growth,
    unitary_transport_t=t,unitary_norm_check=[norm(f),norm(u)],
    unitary_target_abs=abs(u[target]),source_fiber_max_q=src,
    verdict="PASS_SCALAR_AUXILIARY_ONLY"),indent=2,sort_keys=True))
