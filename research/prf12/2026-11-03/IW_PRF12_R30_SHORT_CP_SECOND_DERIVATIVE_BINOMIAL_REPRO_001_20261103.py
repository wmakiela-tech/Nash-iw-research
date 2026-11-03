#!/usr/bin/env python3
"""PRF12 R30 short standalone SciPy exact scalar reproduction.
The full 7001-node mpmath.iv source A + Lindblad B certificate, separate
2x2/4x4 audit and full report are in the R30 ZIP. Does NOT rerun global
phase interval arithmetic here. SYNTHETIC reference data. No 3q LOCC claim.
"""
import math
from scipy.stats import beta,binom
W=(.18,.20,.62)
AA=(.94,.88,.36)
BB=(1.,.96,.02)
def cp(n,k,alpha=.005):
    lo=beta.ppf(alpha/2,k,n-k+1)-1e-12
    hi=beta.ppf(1-alpha/2,k+1,n-k)+1e-12
    assert binom.sf(k-1,n,lo)<alpha/2 and binom.cdf(k,n,hi)<alpha/2
    return lo,hi
p0=cp(46000,45540)
p1=cp(69000,3705)
cl=min(p0[0]-p1[1],.932477929662237)-1e-10
cu=max(p0[1]-p1[0],.939937817637063)+1e-10
dl=min(p0[0]+p1[0]-1,.039941802242004)-1e-10
du=max(p0[1]+p1[1]-1,.04740169021683)+1e-10
hcp=sum(w*(aa+bb) for w,aa,bb in zip(W,AA,BB)) * ((cu-cl)**2+(du-dl)**2)/16+1e-10
txy=.5+math.pi/10;tz=.5+math.pi/20
M2=sum(w*(cu*max(aa,bb)+.5*(aa+bb)*cu*cu)*t*t
       for w,aa,bb,t in zip(W,AA,BB,(txy,txy,tz)))+1e-8
h=.01
# Validated SOURCE A min of four CP corners on 7001 directed interval nodes:
min_node=.31960671935925755
compact=min_node-hcp-M2*h*h/8
# Independent ANALYTIC source A off-resonance bound |xi|>=35:
tail=.39116545038768846
def clip(z,l,r):return max(l,min(r,z))
floors=[]
for aa,bb in zip(AA,BB):
    ustar=(bb-aa)/(aa+bb)
    F=lambda u:(aa*(1+u)**2+bb*(1-u)**2)/4
    pos=F(clip(ustar,cl+dl,cu+du))
    neg=F(clip(ustar,dl-cu,du-cl))
    d=clip(ustar,dl,du)
    mixed=((aa+bb)*(1+d*d-cu*cu)+2*(aa-bb)*d)/4
    floors.append(min(pos,neg,mixed)-1e-10)
r=sum(w*f for w,f in zip(W,floors))
s=math.exp(-.02*1.7783185307179588)-1e-12
amin=s*min(compact,tail)+(1-s)*r-2e-10
# From independent 120-term interval Lindblad channel and CP-corner convexity:
bmax=.2706612016991532
a,b=.3095,.2707
assert amin>a and bmax<b
n,k=1682,488
eA=binom.cdf(k-1,n,a);eB=binom.sf(k-1,n,b)
assert max(eA,eB)<.04
assert eA+.01<.05 and eB+.01<.05
r1=a/b;r0=(1-a)/(1-b);s1=b/a;s0=(1-b)/(1-a)
assert abs(r0+(r1-r0)*b-1)<1e-14
assert abs(s0+(s1-s0)*a-1)<1e-14
pZ_A=s*.62*((1+dl)/2)**2
pZ_B=.62*((1+dl+cl*.04809737884883814)/2)**2
ka=(r1-r0)**2/(2*max(r1,r0)**2)
kb=(s1-s0)**2/(2*max(s1,s0)**2)
driftA=a*math.log(r1)+(1-a)*math.log(r0)+ka*pZ_A*.36*.64
driftB=b*math.log(s1)+(1-b)*math.log(s0)+kb*pZ_B*.36*.64
assert driftA>.00425 and driftB>.00423
print('CP c,d',cl,cu,dl,du,'quadratic CP penalty',hcp)
print('Source A compact',compact,'floor',r,'A>=',amin,'B<=',bmax)
print('N',n,'K',k,'science errors A/B',eA,eB)
print('full-alphabet anytime certified log growth A/B',driftA,driftB)
print('PASS. Full rigorous-style Xi interval checks in R30 ZIP.')
