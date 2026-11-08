#!/usr/bin/env python3
"""PRF12 R33 public compact reproducibility core, Python standard library.
R31 all-real-Xi source bounds are inherited; the FULL quantum R31 runner,
R33 physical source audit, and all SHA256 logs are in the R33 ZIP bundle.
Two complete 115000-shot synthetic calibration epochs are predeclared.
No hardware, no inferred drift rate, no novelty, NO_CANON/NO_EXEC.
"""
import math
A0=0.3106993896688963
B0=0.27161358975207756
S=.18*1+.20*1+.62*.347
N0,N1=46000,69000
K0,K1=45540,3705
alpha=.01
nu=1e-8  # per dimensionless gamma*t, EXOGENOUS pathwise drift assumption
wall_pair=1.8283185307179588
science_per_epoch=4750
n_epoch=2
assert abs(S-.59514)<1e-14
def eps(j,n):
    # alpha/(j(j+1)) per epoch, split between TWO streams
    return math.sqrt(math.log(4*j*(j+1)/alpha)/(2*n))
def cp_interval_relocation(j):
    # Physically feasible deterministic 2:3 interleaving; exact reference
    # mean times for each source reference stream in gamma*time units.
    centers=(5750.1,5749.933333333333)
    science_end=11500+science_per_epoch*wall_pair
    D=max(
        abs(K0/N0-.99)+eps(j,N0)+nu*(science_end-centers[0]),
        abs(K1/N1-3705/69000)+eps(j,N1)+nu*(science_end-centers[1]))
    return D,A0-2*S*D,B0+2*S*D
bounds=[cp_interval_relocation(j) for j in range(1,n_epoch+1)]
assert max(v[0] for v in bounds)<.009343
a,b=.2995,.2828
assert min(x[1] for x in bounds)>a
assert max(x[2] for x in bounds)<b
assert A0-B0-4*S*max(x[0] for x in bounds)>0

# Exact RATIONAL binomial tails:
# P_A=false B = CDF(K-1;N,a), P_B=false A = SF(K-1;N,b).
def exact_cdf(n,k,P,Q):
    term=pow(Q-P,n)
    total=term
    for i in range(k):
        term,r=divmod(term*(n-i)*P,(i+1)*(Q-P))
        assert r==0
        total+=term
    return total,pow(Q,n)
N=9500;K=2765
Aerr,Ad=exact_cdf(N,K-1,599,2000)
Bcdf,Bd=exact_cdf(N,K-1,707,2500)
assert 25*Aerr<Ad and 25*(Bd-Bcdf)<Bd # both science errors <4%
assert Aerr/Ad+.01<.05 and (Bd-Bcdf)/Bd+.01<.05

# Composite-null test factors for optional SCIENCE stopping, after each
# completed calibration epoch with separately allocated alpha spending.
for _,ap,bp in bounds:
    assert bp<ap
    ga1=ap/bp;ga0=(1-ap)/(1-bp)
    gb1=bp/ap;gb0=(1-bp)/(1-ap)
    assert abs(bp*ga1+(1-bp)*ga0-1)<1e-14
    assert abs(ap*gb1+(1-ap)*gb0-1)<1e-14

print('R33 PASS interleaved completed-epoch reference confidence')
print('epoch worst-case drift+stat bounds',bounds)
print('science N,K',N,K,'A/B errors',Aerr/Ad,(Bd-Bcdf)/Bd)
print('reads',2*(N0+N1)+2*N,'gamma_wall',
      2*(N0+N1)*.1+N*wall_pair)
print('unrestricted-drift no-go: if p0=p1=1/2 during science,'
      ' source A/B recorded quartet laws identical')
