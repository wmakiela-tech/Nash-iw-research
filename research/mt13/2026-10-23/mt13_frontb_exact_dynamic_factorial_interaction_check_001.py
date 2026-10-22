#!/usr/bin/env python3
"""MT13 source-typed exact 2x2 interaction test. SYNTHETIC ONLY; no Wu-Xu/Julia rerun."""
from math import exp,sin,cos
import numpy as np
from scipy.integrate import solve_ivp

rates_toy={(0,0):(.2,.4),(1,0):(.3,.5),(0,1):(.4,.2),(1,1):(.5,.3)}
def tx(a,b,t):
    r=a+b
    return a/r+(.5-a/r)*exp(-r*t)
def toy_check(t):
    x={k:tx(*a,t) for k,a in rates_toy.items()}
    le=x[(1,0)]-x[(0,0)];ls=x[(1,1)]-x[(0,1)]
    iy=ls-le
    f=lambda r:(1-exp(-r*t))/r
    assert abs(iy-.2*(f(.8)-f(.6)))<2e-15
    assert le>0>ls and iy<0
    for i in (0,1):
        assert abs(rates_toy[(1,1)][i]-rates_toy[(1,0)][i]-rates_toy[(0,1)][i]+rates_toy[(0,0)][i])<1e-15
    return le,ls,iy
def u(t):return .25+.05*sin(t)
def lam(t):return 1+.07*cos(t)
def rates(t):
    A=.3+.05*sin(2*t); B=.4+.03*cos(2*t)
    la=.07+.02*sin(t);lb=.12+.01*cos(t)
    ma=.13+.015*cos(t);mb=-.07+.01*sin(2*t)
    ca=.025*sin(1.5*t);cb=-.012*cos(1.3*t)
    return ((A,B),(A+la,B+lb),(A+ma,B+mb),
            (A+la+ma+ca,B+lb+mb+cb))
def joint(t,y):
    r=rates(t); xx=y[:4]
    derivatives=[u(t)+a-(lam(t)+a+b)*x for x,(a,b) in zip(xx,r)]
    x00,x10,x01,x11=xx
    L=x10-x00;M=x01-x00
    rr=[a+b for a,b in r]
    direct=(1-x00)*(r[3][0]-r[2][0]-r[1][0]+r[0][0])-x00*(r[3][1]-r[2][1]-r[1][1]+r[0][1])
    feedbackM=-M*(rr[3]-rr[2])
    feedbackL=-L*(rr[3]-rr[1])
    d=-(lam(t)+rr[3])
    return derivatives+[d*y[4]+direct,d*y[5]+feedbackM,d*y[6]+feedbackL]
def single(t,y,j):
    a,b=rates(t)[j]
    return [u(t)+a-(lam(t)+a+b)*y[0]]
def solve(fn,initial):
    z=solve_ivp(fn,(0,2.3),initial,method='DOP853',rtol=1e-12,atol=1e-14,max_step=.02,dense_output=True)
    assert z.success
    return z
def main():
    le,ls,I=toy_check(1)
    print('TOY law effects, interaction:',le,ls,I)
    assert abs(I+.0127283623312964)<1e-13
    joint_solution=solve(joint,[.41]*4+[0]*3)
    separate=[solve(lambda t,y,j=j:single(t,y,j),[.41]) for j in range(4)]
    eledger=[];esingle=[]
    for t in np.linspace(0,2.3,101):
        v=joint_solution.sol(t)
        eledger.append(abs(v[3]-v[1]-v[2]+v[0]-sum(v[4:])))
        xs=[q.sol(t)[0] for q in separate]
        esingle.append(abs(xs[3]-xs[1]-xs[2]+xs[0]-(v[3]-v[1]-v[2]+v[0])))
        assert all(a>=0 and b>=0 for a,b in rates(t))
    e1=max(eledger);e2=max(esingle)
    print('I(T), ledger contributions:',(joint_solution.y[3,-1]-joint_solution.y[1,-1]-joint_solution.y[2,-1]+joint_solution.y[0,-1]),joint_solution.y[4:,-1])
    print('max errors',e1,e2)
    assert e1<3e-12 and e2<3e-12
    assert joint_solution.y[4,-1]>0 and joint_solution.y[4:,-1].sum()<0
    print('PASS exact toy, zero mixed A/B effects, four independent dynamic trajectories, full 3-component ledger')
if __name__=='__main__':main()
