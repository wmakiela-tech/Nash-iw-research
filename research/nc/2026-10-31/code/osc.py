import numpy as np
from scipy.optimize import minimize
# Czy dla oscylatora (izometria) kres sqrt(m) jest osiagany przy DOWOLNYCH czasach (twierdzenie T1a w ART029)?
# Czasy USTALONE (t1=0.3, odstep Delta), optymalizacja tylko po (e, d, u_j).
def R(t): c,s=np.cos(t),np.sin(t); return np.array([[c,s],[-s,c]])   # exp(tG), G=[[0,1],[-1,0]]
def lam(e,d,us,ts):
    L=np.eye(2); t=0.0; W=np.zeros((2,2))
    for tj,u in zip(ts,us):
        L=R(tj-t)@L; t=tj
        w=(1-u)*(L.T@e); W+=np.outer(w,w)
        L=(np.eye(2)-(1-u)*np.outer(d,d))@L
    return float(np.linalg.eigvalsh(W)[-1])
def best(m,Delta,restarts=60,seed=0):
    rng=np.random.default_rng(seed); ts=0.3+Delta*np.arange(m); b=0
    for _ in range(restarts):
        z0=np.concatenate([rng.uniform(0,np.pi,2),rng.uniform(-3,3,m)])
        f=lambda z: -lam(np.array([np.cos(z[0]),np.sin(z[0])]),np.array([np.cos(z[1]),np.sin(z[1])]),1/(1+np.exp(-z[2:])),ts)
        r=minimize(f,z0,method='Nelder-Mead',options={'maxiter':8000,'xatol':1e-11,'fatol':1e-13})
        b=max(b,-r.fun)
    # u w (0,1) przez sigmoid; dopisuje tez granice u->0 jawnie: e=(1,0), d=(0,1)
    b0=lam(np.array([1.,0]),np.array([0.,1]),np.zeros(m),ts)
    return np.sqrt(max(b,b0))
print(f"{'m':>2} {'Delta':>8} {'sup||c||_2':>12} {'sqrt(m)':>9} {'rowne?':>7}")
for m in (2,4):
    for D,lab in ((np.pi,'pi'),(np.pi/2,'pi/2'),(1.0,'1.0'),(0.3,'0.3'),(2*np.pi,'2pi')):
        v=best(m,D); print(f"{m:>2} {lab:>8} {v:>12.8f} {np.sqrt(m):>9.6f} {'TAK' if abs(v-np.sqrt(m))<1e-6 else 'NIE':>7}")
