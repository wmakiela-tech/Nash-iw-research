#!/usr/bin/env python3
"""PRF12 R34 short standalone core; Python standard library only.
Rechecks the RECORDED synthetic stopped radii, familywise alpha, global
R31 source margins and exact N9500/K2765 binomial science tails.
Complete adaptive sampling trajectory, independent 2x2/4x4 audit and
original R31/R33 full source replays are provided in R34 ZIP.
NO empirical hardware; exogenous nu=1e-8 and latent-Xi source guards.
"""
import math
lam=(.06,.085,.12,.17,.24,.34,.48,.68)
psi=lambda x:-math.log1p(-x)-x
pstar=(.99,3705/69000)
A0=.3106993896688963; B0=.27161358975207756
S=.59514;alpha=.01;nu=1e-8
a=.2995;b=.2828
limit=min((A0-a)/(2*S),(b-B0)/(2*S))
# In each tuple: epoch, arm, n, successes, observed predictable V,
# physically timed drift relocation nu*(science_end - average_ref_time).
stops=[
(1,0,3372,3339,32.73372491559245,.00010006703175120635),
(1,1,18923,1054,995.5944319268812,.00009762298047068208),
(2,0,4573,4535,37.72422738243444,.00010079894269548586),
(2,1,19187,1061,1002.5964082491167,.00009823086093828834)]
for j,i,n,k,V,drift in stops:
    L=math.log(4*len(lam)*j*(j+1)/alpha)
    rad=min((L+psi(x)*V)/(x*n) for x in lam)
    delta=abs(k/n-pstar[i])+rad+drift
    assert delta<limit
    print('epoch',j,'arm',i,'n',n,'r',round(rad,10),'delta',round(delta,10))
# Since sum_{j>=1} 1/[j(j+1)]=1, Ville+union bound spends alpha ONCE
# over arbitrarily many complete epochs and ALL n within each epoch.
def exact_cdf(N,K,P,Q):
    term=pow(Q-P,N);total=term
    for i in range(K):
        term,rem=divmod(term*(N-i)*P,(i+1)*(Q-P))
        assert rem==0
        total+=term
    return total,pow(Q,N)
N,K=9500,2765
fa,den=exact_cdf(N,K-1,599,2000)
fb_cdf,den2=exact_cdf(N,K-1,707,2500)
assert den==den2
assert 25*fa<den and 25*(den2-fb_cdf)<den2
assert fa/den+.01<.05 and (den2-fb_cdf)/den2+.01<.05
print('PASS both science errors <.04 by exact integers + cal risk <.01')
print('synthetic reference readings',sum(z[2] for z in stops),
      'total observations',sum(z[2] for z in stops)+19000,
      'wall gammaT',sum(z[2] for z in stops)*.1+9500*1.8283185307179588)
print('NO same-source 3q LOCC closure; no uniform bound on calibration duration')
