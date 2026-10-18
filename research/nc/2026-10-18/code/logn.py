import numpy as np
from scipy.integrate import solve_ivp
# Chapter's Thm 7.3 / eq (7.1) uses a LIPSCHITZ constant L.
# Standard sharpening: the one-sided Lipschitz constant = LOGARITHMIC NORM (Dahlquist)
#   mu(Jg) = sup_{v!=0} <v, Jg v>/||v||^2   (euclidean case: largest eigenvalue of sym part)
# always mu <= L, and mu may be NEGATIVE -> bound CONTRACTS instead of growing.
R=np.array([[1.0,0.0,0.0],[0.0,1.0,0.0]])
def f(t,x): return np.array([-x[0], x[2], 0.0])
Jg=np.array([[-1.0,0.0],[0.0,0.0]])            # jacobian of g(y)=(-y0, 0)
def g(t,y): return Jg@y
L   = np.linalg.norm(Jg,2)                      # Lipschitz constant (operator norm)
mu  = np.max(np.linalg.eigvalsh((Jg+Jg.T)/2))   # logarithmic norm
print("CHAPTER'S OWN EXAMPLE FROM section 7.3,  g(y)=(-y0,0)")
print(f"  Lipschitz constant L  = {L:.6f}   (what eq (7.1) uses)")
print(f"  logarithmic norm mu   = {mu:.6f}   (the sharp one-sided constant)")
print()
T=2.0
print(f"{'h0':>5} {'actual ||e(T)||':>16} {'bound with L':>14} {'ratio':>8} {'bound with mu':>14} {'ratio':>8}")
for h0 in [0.3,1.0,3.0,10.0]:
    x0=np.array([1.0,0.5,h0]); y0=R@x0
    sx=solve_ivp(f,[0,T],x0,rtol=1e-12,atol=1e-14,dense_output=True)
    sy=solve_ivp(g,[0,T],y0,rtol=1e-12,atol=1e-14,dense_output=True)
    eT=np.linalg.norm(R@sx.sol(T)-sy.sol(T))
    ts=np.linspace(0,T,8001)
    eps=np.array([np.linalg.norm(R@f(t,sx.sol(t))-g(t,R@sx.sol(t))) for t in ts])
    bL =np.trapezoid(np.exp(L *(T-ts))*eps,ts)
    bMu=np.trapezoid(np.exp(mu*(T-ts))*eps,ts)
    print(f"{h0:>5.1f} {eT:>16.9f} {bL:>14.6f} {bL/eT:>8.3f} {bMu:>14.9f} {bMu/eT:>8.5f}")
print()
print("  -> with the logarithmic norm the bound is ATTAINED (ratio 1.00000) on the")
print("     chapter's own example; with the Lipschitz constant it is loose by (e^2-1)/2 = "
      f"{(np.e**2-1)/2:.4f}.")
print()
print("TABLE  a case where mu < 0 and the Lipschitz bound is QUALITATIVELY wrong")
Jg2=np.array([[-3.0,0.0],[0.0,-2.0]])
def g2(t,y): return Jg2@y
def f2(t,x): return np.array([-3*x[0], -2*x[1]+x[2], 0.0])
L2=np.linalg.norm(Jg2,2); mu2=np.max(np.linalg.eigvalsh((Jg2+Jg2.T)/2))
print(f"  L = {L2:.4f}  (positive, bound grows like e^{{{L2:.0f}T}})   mu = {mu2:.4f}  (negative, bound decays)")
print(f"{'T':>5} {'actual':>14} {'bound with L':>16} {'bound with mu':>16} {'L-bound / actual':>18}")
for T2 in [1.0,3.0,6.0]:
    x0=np.array([1.0,0.0,1.0]); y0=R@x0
    sx=solve_ivp(f2,[0,T2],x0,rtol=1e-12,atol=1e-14,dense_output=True)
    sy=solve_ivp(g2,[0,T2],y0,rtol=1e-12,atol=1e-14,dense_output=True)
    eT=np.linalg.norm(R@sx.sol(T2)-sy.sol(T2))
    ts=np.linspace(0,T2,8001)
    eps=np.array([np.linalg.norm(R@f2(t,sx.sol(t))-g2(t,R@sx.sol(t))) for t in ts])
    bL =np.trapezoid(np.exp(L2 *(T2-ts))*eps,ts)
    bMu=np.trapezoid(np.exp(mu2*(T2-ts))*eps,ts)
    print(f"{T2:>5.1f} {eT:>14.9f} {bL:>16.4f} {bMu:>16.9f} {bL/eT:>18.1f}")
