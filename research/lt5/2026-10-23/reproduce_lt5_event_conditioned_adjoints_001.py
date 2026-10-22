"""LT5 turnover 9: source-typed fixed-event target and adjoint regression. Requires numpy/scipy."""
import numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss

Z0=np.array([.23,2.])
def f(z,t):
    x=float(z[0]);return np.array([(.35+.17*t)*x*(1-x)+.07+.07*t,-(1+.4*t)*(1+.1*x)])
def A(z,t):
    return np.array([[ (.35+.17*t)*(1-2*z[0]),0.],[-.1*(1+.4*t),0.]])
def b(z):
    x=float(z[0]);return np.array([.17*x*(1-x)+.07,-.4*(1+.1*x)])
def event(time,z):return z[1]-1.
event.direction=-1
event.terminal=False

def quad(fun,a,b,n=100):
    nodes,ws=leggauss(n)
    return (b-a)/2.*sum(float(w)*fun(float((b+a)/2.+(b-a)*node/2.))
                         for node,w in zip(nodes,ws))

def calc(t):
    def ode(time,v):
        z=v[:2]
        return np.r_[f(z,t),A(z,t)@v[2:]+b(z)]
    sol=solve_ivp(ode,(0.,1.2),np.r_[Z0,[0.,0.]],events=event,
                  method="DOP853",dense_output=True,rtol=1e-12,atol=1e-14)
    assert sol.success and len(sol.t_events[0])==1
    tau=float(sol.t_events[0][0]);z=sol.sol(tau)[:2]
    slope=f(z,t)
    q=np.array([1.,-slope[0]/slope[1]])
    ds=float(q@sol.sol(tau)[2:])
    adj=solve_ivp(lambda time,p:-A(sol.sol(time)[:2],t).T@p,
                  (tau,0.),q,method="DOP853",dense_output=True,
                  rtol=1e-12,atol=1e-14)
    da=quad(lambda time:adj.sol(time)@b(sol.sol(time)[:2]),0.,tau)
    assert abs(ds-da)<5e-11
    return tau,float(z[0]),ds,da,sol

if __name__=="__main__":
    for th in [0.,.2,.5,.8,1.]:
        tau,j,d,da,_=calc(th)
        eps=1e-5;lo=max(0,th-eps);hi=min(1,th+eps)
        fd=(calc(hi)[1]-calc(lo)[1])/(hi-lo)
        assert abs(fd-d)<(1e-6 if th in [0.,1.] else 2e-8)
        print("theta",th,"event_t",tau,"J",j,"adjoint",da,"finite_diff",fd)
    nodes,ws=leggauss(16)
    integ=.5*sum(float(w)*calc(float((p+1)/2.))[2] for p,w in zip(nodes,ws))
    delta=calc(1.)[1]-calc(0.)[1]
    assert abs(integ-delta)<1e-11
    lo=calc(0.);hi=calc(1.);t0,t1=lo[0],hi[0]
    e=hi[4].sol(t0)[:2]-lo[4].sol(t0)[:2]
    avx=quad(lambda tm:f(hi[4].sol(tm)[:2],1.)[0],t0,t1)/(t1-t0)
    avt=quad(lambda tm:f(hi[4].sol(tm)[:2],1.)[1],t0,t1)/(t1-t0)
    finite=e[0]-(avx/avt)*e[1]
    assert abs(finite-delta)<3e-12
    print("event direct",delta,"adjoint homotopy",integ,"event secant",finite)
    print("EVENT_ADJOINT_REGRESSION_PASS")
