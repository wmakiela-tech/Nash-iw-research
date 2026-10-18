import numpy as np

# ATAK NA TW. 1 Z ART009 PRZEZ ZMIANE MODELU SZUMU
# prerejestracja: PREREG_L2.md sha256 5399acbcf0c908009dbb6cfadca2df82ce42902fca2ce4f843f622ae619fb591
#
# b_j = y0 c_j + eta_j,  c_j = y(t_j) sigma(s_j),  sigma(s) = (1-e^{-gamma s})/gamma
# pomiar mnozy y przez u_j = e^{-gamma s_j}; x nietkniete; ewolucja swobodna zachowuje x^2+y^2
#
# szum adwersarialny per pomiar |eta_j|<=delta  -> figura ||c||_inf  (ART009 Tw.1: < 1/gamma)
# szum iid N(0,delta^2) albo adwersarialny ||eta||_2<=delta -> figura ||c||_2
#
# PREDYKCJA Z ART009 par.5.4: sufit UPADNIE (usrednianie zaczyna dzialac, zysk sqrt(k))
# PREDYKCJA Z WYPROWADZENIA par.2 PREREG: sufit ZOSTAJE, (gamma c_j)^2 <= A_j^2 - A_{j+1}^2

GAM = 1.0

def trace(times, strengths, gam=GAM):
    """zwraca (c, A2) : wzmocnienia znakowane oraz kwadrat amplitudy PRZED kazdym pomiarem
       plus A2_end po ostatnim pomiarze"""
    x, y, t = 0.0, 1.0, 0.0
    c, A2 = [], []
    for tj, s in zip(times, strengths):
        dt = tj - t
        xn = x*np.cos(dt) + y*np.sin(dt)
        yn = -x*np.sin(dt) + y*np.cos(dt)
        x, y, t = xn, yn, tj
        A2.append(x*x + y*y)
        u = np.exp(-gam*s)
        c.append(y*(1.0-u)/gam)
        y = y*u
    return np.array(c), np.array(A2), x*x + y*y

def linf(times, strengths, gam=GAM):
    c, _, _ = trace(times, strengths, gam); return np.max(np.abs(c))

def l2(times, strengths, gam=GAM):
    c, _, _ = trace(times, strengths, gam); return np.sqrt(np.sum(c*c))

print("TABELA L1  czy gamma*||c||_2 <= 1 ? skan losowy, gamma=1, czasy [0,20], sily [0.001,60]")
print("  k    prob      max gamma||c||_2    max gamma||c||_inf   naruszen (>1+1e-9)")
rng = np.random.default_rng(11)
for k in [1,2,3,4,6,8,12]:
    N = 40000
    b2 = b8 = 0.0; viol = 0
    for _ in range(N):
        ts = np.sort(rng.uniform(0, 20.0, k))
        ss = np.exp(rng.uniform(np.log(1e-3), np.log(60.0), k))
        v2 = l2(ts, ss); v8 = linf(ts, ss)
        if v2 > b2: b2 = v2
        if v8 > b8: b8 = v8
        if v2 > 1.0 + 1e-9: viol += 1
    print(f"  {k:<4} {N:<9} {b2:<19.9f} {b8:<20.9f} {viol}")

print()
print("TABELA L2  nierownosc termwise (gamma c_j)^2 <= A_j^2 - A_(j+1)^2 ; 200000 pomiarow")
rng = np.random.default_rng(12)
worst = -1e9; nviol = 0; ntot = 0
for _ in range(25000):
    k = int(rng.integers(1, 9))
    ts = np.sort(rng.uniform(0, 20.0, k))
    ss = np.exp(rng.uniform(np.log(1e-3), np.log(60.0), k))
    c, A2, A2e = trace(ts, ss)
    dec = np.append(A2[1:], A2e)
    d = (GAM*c)**2 - (A2 - dec)
    ntot += k; nviol += int(np.sum(d > 1e-12))
    if d.max() > worst: worst = d.max()
print(f"  pomiarow sprawdzonych   {ntot}")
print(f"  naruszen (>1e-12)       {nviol}")
print(f"  najwiekszy nadmiar      {worst:.3e}")

print()
print("TABELA L3  czy wiele slabych bije jeden silny? pomiary w ANTYWEZLACH predkosci")
print("  stan poczatkowy (x,y)=(0,1) daje y(t)=cos t, wiec |y| max w t=j*pi, a t=pi/2 to WEZEL")
print("  kontrola: |y(0)|=%.6f  |y(pi/2)|=%.6f  |y(pi)|=%.6f" % (abs(np.cos(0)), abs(np.cos(np.pi/2)), abs(np.cos(np.pi))))
print("  (rowne sily s, budzet calkowity k*s)")
print("  k    s=0.05      s=0.2       s=1.0       s=5.0       s=40.0")
for k in [1,2,3,5,10,20,50]:
    ts = np.array([j*np.pi for j in range(k)])
    row = []
    for s in [0.05,0.2,1.0,5.0,40.0]:
        row.append(l2(ts, np.full(k, s)))
    print("  %-4d " % k + " ".join(f"{v:<11.7f}" for v in row))

print()
print("TABELA L4  optymalizacja ||c||_2 bez wiezow czasowych (wielostart, Nelder-Mead)")
from scipy.optimize import minimize
print("  k    gamma||c||_2 opt    czasy                      sily")
for k in [1,2,3,4]:
    best = (0.0, None)
    for _ in range(60):
        t0 = np.sort(rng.uniform(0, 12.0, k)); s0 = np.exp(rng.uniform(np.log(.01), np.log(30), k))
        f = lambda p: -l2(np.sort(np.abs(p[:k])), np.abs(p[k:]) + 1e-9)
        r = minimize(f, np.concatenate([t0, s0]), method='Nelder-Mead',
                     options={'maxiter':8000,'xatol':1e-10,'fatol':1e-12})
        if -r.fun > best[0]:
            best = (-r.fun, (np.sort(np.abs(r.x[:k])), np.abs(r.x[k:])+1e-9))
    tt, sr = best[1]
    print(f"  {k:<4} {best[0]:<19.9f} {np.round(tt,4).tolist()!s:<26} {np.round(sr,2).tolist()}")

print()
print("TABELA L5  wysycenie: jeden pomiar w antywezle t=pi, sila rosnaca")
print("  s        gamma||c||_2     1 - gamma||c||_2   dla porownania t=pi/2 (wezel)")
for s in [1,2,5,10,20,40,80]:
    v = l2([np.pi],[s]); w = l2([np.pi/2],[s])
    print(f"  {s:<8} {v:<16.12f} {1-v:<18.3e} {w:.3e}")

print()
print("TABELA L6  podloga bledu znormalizowanego dla obu modeli szumu")
print("  (ART009: inf-> gamma delta/R ; tutaj: 2 -> delta/(R||c||_2) >= gamma delta/R)")
print("  gamma   sup||c||_inf (skan)   sup||c||_2 (skan)   1/gamma")
rng2 = np.random.default_rng(13)
for gam in [0.25,0.5,1.0,2.0,4.0]:
    b8 = b2 = 0.0
    for _ in range(60000):
        k = int(rng2.integers(1,6))
        ts = np.sort(rng2.uniform(0,20.0,k)); ss = np.exp(rng2.uniform(np.log(1e-3),np.log(80.0),k))
        c,_,_ = trace(ts,ss,gam)
        b8 = max(b8, np.max(np.abs(c))); b2 = max(b2, np.sqrt(np.sum(c*c)))
    print(f"  {gam:<7} {b8:<20.9f} {b2:<19.9f} {1/gam:.6f}")

print()
print("TABELA L7  Tw.2 ART009 (pomiar ofiarny) przy figurze ||c||_2 zamiast ||c||_inf")
print("  okienko            inf: 1pom   inf: 2pom   zysk    L2: 1pom   L2: 2pom   zysk")
for lo,hi in [(1.50,1.65),(1.45,1.70),(1.40,1.75),(1.30,1.85),(1.10,2.05),(0.80,2.35)]:
    S = [0.5,1,2,4,8,20,50]
    a1 = max(linf([t],[s]) for t in np.linspace(lo,hi,900) for s in S)
    g1 = max(l2([t],[s]) for t in np.linspace(lo,hi,900) for s in S)
    a2 = g2 = 0.0
    for t1 in np.linspace(lo,hi-0.005,90):
        for t2 in np.linspace(t1+0.005,hi,90):
            for s1 in S:
                for s2 in S:
                    a2 = max(a2, linf([t1,t2],[s1,s2])); g2 = max(g2, l2([t1,t2],[s1,s2]))
    print(f"  [{lo:.2f}, {hi:.2f}]       {a1:<11.6f} {a2:<11.6f} {a2/a1:<7.4f} {g1:<10.6f} {g2:<10.6f} {g2/g1:.4f}")
