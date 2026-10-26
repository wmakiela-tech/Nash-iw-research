# M14 ROT002 — deterministic numerical controls, numpy
import math
import numpy as np
def r(a):
 return np.array([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]])
def kl(w,ds):
 return sum(2*(1-math.cos(math.remainder(w*d,2*math.pi)))/math.expm1(2*d) for d in ds)
def fi(ds):
 return sum(2*d*d/math.expm1(2*d) for d in ds)
ts=[0,.37,1.19,2.04]
ds=np.diff(ts)
cov=lambda w: np.block([[math.exp(-abs(t-u))*r(w*(t-u)) for u in ts] for t in ts])
a,b=cov(.37),cov(1.26)
_,da=np.linalg.slogdet(a)
_,db=np.linalg.slogdet(b)
k=(np.trace(np.linalg.solve(b,a))-len(a)+db-da)/2
assert abs(k-kl(.89,ds))<1e-12
assert abs(fi(ds)-2*kl(.001,ds)/.001**2)<1e-6
for n in [2,10,50,200,1000]:
 d=[1/n]*n
 assert 0<=1-fi(d)<=sum(x*x for x in d)+1e-12
near=[kl(2*math.pi*q,[1,math.sqrt(2)]) for q in [12,70,408,2378,13860]]
assert all(x>y for x,y in zip(near,near[1:]))
assert kl(2*math.pi,[1])<1e-29
assert fi([.6,9.4])>fi([5,5])
print("M14_ROT002_PASS",k,fi(ds),near)
