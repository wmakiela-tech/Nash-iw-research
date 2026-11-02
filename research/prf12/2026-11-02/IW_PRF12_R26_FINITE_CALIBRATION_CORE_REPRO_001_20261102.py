#!/usr/bin/env python3
"""PRF12 R26 finite CP-calibration plus martingale source test (SciPy).
Example input counts are SYNTHETIC nominal, not measured. Complete R26
reproduction including independent Kraus/binomial-tail audit is in ZIP.
"""
import math
from scipy.stats import beta,binom

L=1.7783185307179588
TPAIR=1.8283185307179588
A=math.exp(-.02*L)*.576
B=.526
def cp(n,k,alpha):
    return (0 if k==0 else beta.ppf(alpha/2,k,n-k+1),
            1 if k==n else beta.ppf(1-alpha/2,k+1,n-k))
def certify(n0,k0,n1,k1,dc=.01,dt=.04):
    l0,u0=cp(n0,k0,dc/2);l1,u1=cp(n1,k1,dc/2)
    ch=k0/n0-k1/n1; dh=k0/n0+k1/n1-1
    cL=l0-u1;cU=u0-l1;dL=l0+l1-1;dU=u0+u1-1
    if ch<=0 or cL<=0: return {'status':'ABSTAIN_NONINVERTIBLE'}
    uc=max(ch-cL,cU-ch);ud=max(dh-dL,dU-dh)
    eps=(uc+ud)/ch;bias=eps+eps*eps/2
    D=A-B-2*bias
    if D<=0:return {'status':'ABSTAIN_NO_CERTIFIED_GAP','bias':bias}
    W=(1+abs(dh))/ch**2
    N=math.ceil(2*W**2*math.log(1/dt)/D**2)
    return {'status':'PASS_IF_MAIN_RUN_COMPLETED','N':N,'hat_c':ch,
            'hat_d':dh,'bias':bias,'gap':D,'score_width':W,
            'total_sensor_reads':n0+n1+2*N,'familywise_wrong_bound':dc+dt}
for record in ((46000,45540,69000,3705),(44850,44402,70150,3767)):
    out=certify(*record)
    print('SYNTHETIC CALIBRATION',record,'->',out)
assert certify(46000,45540,69000,3705)['N']==49215
assert certify(44850,44402,70150,3767)['N']==49147
eta_plus=.01;c=.9362975155471993;d=.043702484452800686
for eta_minus in (.02,.03,.04):
    g=c/(1-eta_plus-eta_minus)
    rate=-math.log(g)/.05
    d2=(1-g)*(1-eta_plus-eta_minus)+eta_minus-eta_plus
    assert abs(d-d2)<1e-13
    print('NONIDENTIFIABLE microscopic alternatives',eta_minus,rate)
print('PASS; CP intervals have fixed-sample exact joint >=99% coverage.')
