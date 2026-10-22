"""INT8 ROT006: independent numerical/symbolic checks of the classical 2x2 examples."""
import math
import numpy as np
from scipy.linalg import expm

def resets(s,a,b):
    return np.array([[1-s,0.],[a*s,1.]]), np.array([[1.,b*s],[0.,1-s]])
def crit(s,g,h):
    z=math.exp(2*g*h)
    return (z-1+s)**2/(z*s*s)
def radius(s,a,b,g,h):
    x,y=resets(s,a,b)
    return max(abs(np.linalg.eigvals(math.exp(-2*g*h)*y@x)))
def energy(s,q,k):
    x,y=resets(s,q,q); mat=y@x
    eig,vecs=np.linalg.eig(mat)
    idx=int(np.argmax(eig.real));lam=float(eig[idx].real)
    v=vecs[:,idx].real;v=v/np.linalg.norm(v)
    ampl=(s*v[0])**2+(s*(x@v)[1])**2
    return ampl*math.expm1(2*k*math.log(lam))/math.expm1(2*math.log(lam))

a=b=1.44;g=.4
for s in (.1,.025,.005):
    x,y=resets(s,a,b)
    z=1.137
    assert np.isclose(np.linalg.det(z*np.eye(2)-y@x),(z-1+s)**2-a*b*s*s*z)
    lam=max(np.linalg.eigvals(y@x).real)
    hc=math.log(lam)/(2*g)
    assert np.isclose(crit(s,g,hc),a*b)
    assert radius(s,a,b,g,.98*hc)>1
    assert radius(s,a,b,g,1.02*hc)<1
    print("s",s,"hcrit/s",hc/s)
q=1.5;c=1/(q-1)
for s in (.03,.01,.003):
    k=math.floor(c*math.log(1/s)/(2*s))
    print("dose critical",s,k,energy(s,q,k))
rng=np.random.default_rng(6)
G=np.array([[-.9,2.],[-.4,-.3]])
mu=max(0,np.linalg.eigvalsh((G+G.T)/2).max())
x0=np.array([.4,.9]);state=x0.copy()
T=1.7;epsilon=.03;B=1.
S=0.;energy_out=0.;tprev=0.
for t in np.sort(rng.uniform(0,T,32)):
    state=expm(G*(t-tprev))@state;tprev=t
    e=rng.normal(size=2);e/=np.linalg.norm(e)
    d=rng.normal(size=2);d/=np.linalg.norm(d)
    s=epsilon*rng.random()
    if S+s>B:break
    S+=s;obs=s*(e@state);energy_out+=obs*obs;state-=d*obs
bound=epsilon*B*math.exp(2*(mu*T+B))*np.linalg.norm(x0)**2
assert energy_out<=bound
print("energy",energy_out,"bound",bound)
