#!/usr/bin/env python3
"""PRF11 R22: public Wu-Xu table -> independent gamma/e+-neutrino EOS.
Usage: python reproduce_prf11_r22_wuxu_two_temperature_eos.py N_around_m_e.csv
Source: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
Data file: arXiv-2509.05618/data/ext/N_around_m_e.csv
Expected original Git blob: 93f2494f026c5d0587ea40fe08bb938dd9d01fa8
Only a conditional radiation/ideal-gas table test; NOT the Wu-Xu Julia simulation.
Requires NumPy and SciPy.
"""
import csv
import math
import sys
from bisect import bisect_right
import numpy as np
from scipy.integrate import quad

ME = 0.51099895000  # MeV, pinned source
TNUC = 0.078185270688319950
FACTOR = 60.0 / math.pi**4

def electron_degrees(T):
    x = ME/T
    def e_and_p(y):
        E = math.hypot(y,x)
        f = 1.0/(math.exp(E)+1.0)
        return y*y*E*f, y**4/E*f
    ge = FACTOR * quad(lambda y: e_and_p(y)[0], 0., 45., epsabs=1e-12)[0]
    gp = FACTOR * quad(lambda y: e_and_p(y)[1], 0., 45., epsabs=1e-12)[0]
    return ge, gp, (3*ge+gp)/4.

class Table:
    def __init__(self, filename):
        with open(filename,encoding="utf-8",newline="") as f:
            self.data = [list(map(float,r)) for r in csv.reader(f) if r]
        assert len(self.data)==1000, "Wrong source table"
        self.logT = [math.log(r[0]) for r in self.data]

    def sample(self, logT):
        i=max(0,min(len(self.data)-2,bisect_right(self.logT,logT)-1))
        L,R=self.data[i:i+2]
        span=self.logT[i+1]-self.logT[i]
        u=(logT-self.logT[i])/span
        gr=(1-u)*L[1]+u*R[1]
        gs=(1-u)*L[2]+u*R[2]
        r=(R[1]-L[1])/(span*gr)
        s=(R[2]-L[2])/(span*gs)
        return gr,gs,r,s

    def evaluate(self, logT):
        T=math.exp(logT)
        gr,gs,r,s=self.sample(logT)
        ge,gp,ges=electron_degrees(T)
        r_e=((gr-2-ge)/5.25)**.25
        r_s=((gs-2-ges)/5.25)**(1/3)
        w_m=(gr-ge+gp)/(3*gr)
        w_a=(4+r)/(3+s)-1
        w_c=(1-r/(3+s))/3
        return dict(T=T,Renergy=r_e,Rentropy=r_s,
                    w_micro=w_m,w_adiab=w_a,w_code=w_c,
                    deta_micro=-(4+r)/(3*(1+w_m)),
                    deta_adiab=-(3+s)/3,
                    deta_code=(4+r)/(-4+r/(3+s)))

    def integrate(self,start,end,order=4):
        lo,hi=math.log(end),math.log(start)
        cuts=[lo]+[v for v in self.logT if lo<v<hi]+[hi]
        x,w=np.polynomial.legendre.leggauss(order)
        sums=np.zeros(3)
        for a,b in zip(cuts[:-1],cuts[1:]):
            mid,half=(a+b)/2,(b-a)/2
            for xx,ww in zip(x,w):
                v=self.evaluate(mid+half*xx)
                sums+=half*ww*np.array([v["deta_micro"],v["deta_adiab"],v["deta_code"]])
        return -sums

def main(fn):
    tab=Table(fn)
    for T in [1.,.5,.2,.1,TNUC,.03]:
        v=tab.evaluate(math.log(T))
        print(f"T={T:.9f} Renergy={v['Renergy']:.10f} Rentropy={v['Rentropy']:.10f}"
              f" wmicro={v['w_micro']:.9f} wadiab={v['w_adiab']:.9f} wcode={v['w_code']:.9f}")
    a=tab.integrate(1.,TNUC,4)
    b=tab.integrate(1.,TNUC,8)
    assert np.max(np.abs(a-b))<2e-9,(a,b)
    expected=np.array([2.852685233674142,2.852690783081917,2.898273926161199])
    assert np.max(np.abs(b-expected))<2e-8,(b,expected)
    print("ln[a_micro,a_adiab,a_code] ratios:",b)
    print("a_code/a_micro:",math.exp(b[2]-b[0]))
    print("a_adiab/a_micro:",math.exp(b[1]-b[0]))
    print("R22 PINNED-TABLE TEST PASS; NOT A PBH/BBN PHYSICAL RUN.")

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit(__doc__)
    main(sys.argv[1])
