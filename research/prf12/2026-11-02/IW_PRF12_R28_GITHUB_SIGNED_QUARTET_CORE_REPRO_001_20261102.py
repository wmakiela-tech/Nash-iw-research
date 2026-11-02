#!/usr/bin/env python3
"""PRF12 R28 standalone CORE. Full all-Xi mpmath.iv + independent matrix
audits are provided in the R28 ZIP, not in this abbreviated GitHub script.
SYNTHETIC calibration data, source-A latent conditional hazard, no CANON/EXEC.
Dependencies: scipy, numpy.
"""
import math
from scipy.stats import beta,binom

N0,K0,N1,K1=46000,45540,69000,3705
W=(.18,.20,.62)
ALPHA=(.94,.88,.36)
BETA=(1.,.96,.02)
def cp(n,k,al=.005):
    return (0 if k==0 else beta.ppf(al/2,k,n-k+1)-1e-12,
            1 if k==n else beta.ppf(1-al/2,k+1,n-k)+1e-12)
p0=cp(N0,K0);p1=cp(N1,K1)
cl=p0[0]-p1[1];cu=p0[1]-p1[0]
dl=p0[0]+p1[0]-1;du=p0[1]+p1[1]-1
assert cl>.9324 and cu<.940 and dl>.0399
def score(u,j):
    return (ALPHA[j]*(1+u)**2+BETA[j]*(1-u)**2)/4
def two_scores(u,v,j):
    return (ALPHA[j]*(1+u)*(1+v)+BETA[j]*(1-u)*(1-v))/4
floor=sum(W[j]*min(two_scores(c*m+d,c*n+d,j)
    for c in (cl,cu) for d in (dl,du)
    for m in (-1,1) for n in (-1,1)) for j in range(3))
assert floor>.030
# The GLOBAL all-real-Xi source bound .3158551297 and B upper .2718681462
# are proven by interval nodes + analytic tails in full ZIP source.
s=math.exp(-.02*1.7783185307179588)
A=s*.3158551297099383+(1-s)*.030322723118821438
B=.271868146204745
a,b=.3055,.272
assert A>a and B<b
N,k=2251,650
eA=binom.cdf(k-1,N,a);eB=binom.sf(k-1,N,b)
assert max(eA,eB)<.04
for N2 in range(1,N):
    la=math.log(a/b);lb=math.log((1-b)/(1-a))
    th=math.ceil(N2*lb/(la+lb)-1e-12)
    assert max(binom.cdf(th-1,N2,a),binom.sf(th-1,N2,b))>=.04
print('R28 PASS calibration',cl,cu,dl,du)
print('all-Xi global A lower',A,'B upper',B)
print('pair threshold N,K',N,k,'conditional errors',eA,eB)
print('calibration + science single readouts',115000+2*N)
print('model gamma-time',11500+N*1.8283185307179588)
