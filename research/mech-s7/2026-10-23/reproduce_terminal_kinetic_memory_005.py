#!/usr/bin/env python3
"""Mech-S7 ROT005 minimal numerical reproduction: frozen Wu-Xu subedge kinetics.
No Julia 10D solve, no source-valid low-mass hadronisation, no BBN bound.
The full independent-audit package also contains the expanded executable.
"""
import math
import numpy as np
from scipy.special import gamma, gammainc
from scipy.optimize import brentq

GAMMA_M3=4.207579833788249e27          # g^3/s, Mech-S7 ROT004
M0=1e9; MC=6e9*math.exp(-20)
T=.1447372646; ETA_B=6.1e-10; LIGHT=299792458.0
ALPHA=1/137.035999084; PROTON=938.27208816
ZETA3=1.202056903159594; HBARC=197.3269804
MBARN=1e-31
M1,M2=5.609588603804452e32,6.099798045788406e32
Q1=np.array([489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596])
Q2=np.array([442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213])
S=np.log(Q2/Q1)/math.log(M2/M1)
IDX=[0,0,1,2,3,4]
NAMES=["pi_minus","pi_plus","K_minus","K0L","pbar","nbar"]
CUT=(MC/M0)**3

def fc(m):
    v=math.sqrt(T/m)+math.sqrt(T/PROTON)
    x=2*math.pi*ALPHA/v
    return x/(-math.expm1(-x))

def linear_block(X):
    nb=ETA_B*2*ZETA3/math.pi**2*(T/HBARC*1e15)**3
    fpi,fk=fc(139.57039),fc(493.677)
    A=np.array([1.5*fpi,0,31*fk,7,0,28.])
    B=np.array([0,1.7,26,7,28,0.])
    D=np.array([1/2.6033e-8,1/2.6033e-8,8.1e7,2e7,0.,0.])
    D+=nb*MBARN*LIGHT*np.array([
      (1-X)*A[0],X*B[1],
      X*(34+26)+(1-X)*(31+14.5)*fk,
      X*(10+7)+(1-X)*(7+10),
      X*28+(1-X)*37, X*37+(1-X)*28])
    coeff=nb*MBARN*LIGHT*((1-X)*A-X*B)
    return D,coeff

def total_count(i,s): # common positive factor 3*M0^3/GAMMA omitted
    k=3+s
    return Q1[i]*(1-CUT**(k/3))/k

def survivor(i,s,D): # same factor 3*M0^3/GAMMA omitted
    a=1+s/3; lam=D*M0**3/GAMMA_M3
    gam=gamma(a)*(gammainc(a,lam)-gammainc(a,lam*CUT))
    return Q1[i]*math.exp(lam*CUT)*gam/(3*lam**a)

def calc(X,charge):
    D,C=linear_block(X)
    factors=np.array([1.,1.,1.,1.,1.,1.]) if charge=="exec" else np.array([.5,.5,.5,1.,.5,.5])
    N0=np.array([total_count(i,S[i]) for i in IDX])*factors
    N1=np.array([total_count(i,-1.3) for i in IDX])*factors
    R0=np.array([survivor(i,S[i],d) for i,d in zip(IDX,D)])*factors
    R1=np.array([survivor(i,-1.3,d) for i,d in zip(IDX,D)])*factors
    W=C/D
    return {"total":N1/N0,"survivors":R1/R0,
            "impulse0":float(W@N0),"impulse1":float(W@N1),
            "impulse_delta":float(W@(N1-N0)),
            "D":D,"Mstar":(GAMMA_M3/D)**(1/3)}

if __name__=="__main__":
    for name,X in [("exec",.497967914),("sym",.496214275)]:
        out=calc(X,name)
        root=brentq(lambda x:calc(x,name)["impulse_delta"],.49,.51)
        print(name,"X",X,"Xcrit",root,"impulse_ratio",out["impulse1"]/out["impulse0"])
        for j,sp in enumerate(NAMES):
            print(" ",sp,"emitted",out["total"][j],"surviving",out["survivors"][j],"Mstar_g",out["Mstar"][j])
        assert abs(out["survivors"][4]-(1.42596 if name=="exec" else 1.42598))<1e-4
        assert abs(root-.498235)<3e-6
    print("CONDITIONAL FROZEN-KINETICS CONTROL PASS; NO PHYSICAL PBH/BBN CLAIM")
