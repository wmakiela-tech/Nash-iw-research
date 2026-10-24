import numpy as np
from scipy.optimize import minimize

# PREREG_KREISS.md sha256 7b33978aeb29bc962a72b1291537a6820de18b383b803f4507df08d975db0961
# NC-OPN-002. Forma ZAMKNIETA exp(tG) dla 2x2 — dokladna, obsluguje przypadek zdegenerowany.
# Gramian odczytu W pochodzi od M13 (ROT11, zapisany w ART017):
#   gamma^2 sup_{||v0||=1} ||c||_2^2 = lam_max(W).

GAM = 1.0

def nrm2(M):
    return float(np.sqrt(max(np.linalg.eigvalsh(M.T @ M))))

def E(G, t):
    """exp(tG) dokladnie dla 2x2: lam = a +- b; e^{at}[cosh(bt) I + sinh(bt)/b (G-aI)]"""
    a = 0.5*(G[0, 0] + G[1, 1])
    N = G - a*np.eye(2)
    b2 = -(N[0, 0]*N[1, 1] - N[0, 1]*N[1, 0])
    I = np.eye(2)
    if abs(b2) < 1e-14:
        return np.exp(a*t)*(I + t*N)
    if b2 > 0:
        b = np.sqrt(b2)
        return np.exp(a*t)*(np.cosh(b*t)*I + (np.sinh(b*t)/b)*N)
    b = np.sqrt(-b2)
    return np.exp(a*t)*(np.cos(b*t)*I + (np.sin(b*t)/b)*N)

def mu2(G):
    return float(max(np.linalg.eigvalsh((G + G.T)/2)))

def M_of(G):
    ts = np.linspace(0, 40, 4000)
    v = np.array([nrm2(E(G, t)) for t in ts])
    i = int(np.argmax(v)); h = ts[1]-ts[0]
    ts2 = np.linspace(max(0.0, ts[i]-2*h), ts[i]+2*h, 2000)
    v2 = np.array([nrm2(E(G, t)) for t in ts2])
    if v2.max() >= v.max():
        return float(v2.max()), float(ts2[int(np.argmax(v2))])
    return float(v.max()), float(ts[i])

def gram_max(G, e, d, ts, ss, gam=GAM):
    o = np.argsort(ts); ts = np.asarray(ts)[o]; ss = np.asarray(ss)[o]
    L = np.eye(2); t = 0.0; W = np.zeros((2, 2))
    for tj, s in zip(ts, ss):
        if tj > t:
            L = E(G, tj-t) @ L
        t = tj
        u = np.exp(-gam*s)
        w = (1.0-u)*(L.T @ e)
        W = W + np.outer(w, w)
        L = (np.eye(2) - (1.0-u)*np.outer(d, d)) @ L
    return float(max(np.linalg.eigvalsh((W + W.T)/2)))/gam**2

def best(G, m, restarts=14, rng=None):
    rng = rng or np.random.default_rng(0)
    Mg, targ = M_of(G)
    U, S, Vt = np.linalg.svd(E(G, targ))
    e0, e1 = U[:, 0], U[:, -1]
    kand = []
    for S_ in (30., 10., 3., 1.):
        kand += [(np.array([targ]), np.array([S_]), e0, e0),
                 (np.array([targ]), np.array([S_]), e0, e1)]
    if m > 1:
        for span in (0.3, 1.0, 3.0):
            tt = np.linspace(max(1e-4, targ-span/2), targ+span/2, m)
            for S_ in (0.1, 0.5, 2., 8.):
                kand += [(tt, np.full(m, S_), e0, e0), (tt, np.full(m, S_), e0, e1)]
        for S_ in (0.05, 0.2, 1.0):
            tt = np.linspace(1e-4, 3*targ+1e-3, m)
            kand += [(tt, np.full(m, S_), e0, e0), (tt, np.full(m, S_), e0, e1)]
    bst = 0.0; barg = None
    for ts, ss, e, d in kand:
        v = np.sqrt(gram_max(G, e/np.linalg.norm(e), d/np.linalg.norm(d), ts, np.abs(ss)+1e-9))
        if v > bst:
            bst, barg = v, (np.asarray(ts, float).copy(), np.abs(ss).copy(), e.copy(), d.copy())
    def neg(z):
        ts = np.abs(z[:m]); ss = np.abs(z[m:2*m])+1e-9
        e = z[2*m:2*m+2]; d = z[2*m+2:2*m+4]
        ne, nd = np.linalg.norm(e), np.linalg.norm(d)
        if ne < 1e-9 or nd < 1e-9:
            return 0.0
        return -np.sqrt(gram_max(G, e/ne, d/nd, ts, ss))
    for k in range(restarts):
        if barg is not None and k % 2 == 0:
            z0 = np.concatenate([barg[0]+rng.normal(0, .05, m), barg[1]+rng.normal(0, .2, m),
                                 barg[2]+rng.normal(0, .15, 2), barg[3]+rng.normal(0, .2, 2)])
        else:
            z0 = np.concatenate([rng.uniform(0, 2*targ+1, m), rng.uniform(0.02, 15, m),
                                 rng.normal(0, 1, 2), rng.normal(0, 1, 2)])
        r = minimize(neg, z0, method="Nelder-Mead",
                     options={"maxiter": 4000, "maxfev": 4000, "xatol": 1e-9, "fatol": 1e-12})
        if -r.fun > bst:
            bst = -r.fun
    return bst, Mg, targ

rng = np.random.default_rng(20261024)
print("TABELA K1  F5 — KONTROLA SPOJNOSCI: przy mu_2 <= 0 maksimum MUSI byc <= 1")
for nm, G in [("oscylator [[0,1],[-1,0]]", np.array([[0., 1.], [-1., 0.]])),
              ("diag(-1,-2)", np.diag([-1., -2.]))]:
    b, Mg, _ = best(G, 3, 10, rng)
    print(f"  {nm:<26} mu_2={mu2(G):+.6f}  M(G)={Mg:.9f}  max={b:.9f}  "
          f"{'OK' if b <= 1+1e-6 else 'KOD ZLY'}")

mats = [("Metzler M13", np.array([[-1.1, 4.], [1., -4.1]])),
        ("Hurwitz [[-1,4],[0,-1]]", np.array([[-1., 4.], [0., -1.]])),
        ("separator INT7 [[-1,100],[0,-1]]", np.array([[-1., 100.], [0., -1.]]))]

print()
print("TABELA K2  F1 — czy optymalizator odtwarza ZNANE dolne ograniczenie M(G) przy m=1")
print("  macierz                          mu_2        M(G)           max m=1        max/M")
for nm, G in mats:
    b, Mg, _ = best(G, 1, 16, rng)
    print(f"  {nm:<32} {mu2(G):+.5f}  {Mg:<14.9f} {b:<14.9f} {b/Mg:.9f}")

print()
print("TABELA K3  F2/F3/F4 — czy WIECEJ pomiarow bije M(G)")
print("  macierz                        M(G)        m=1        m=2        m=3        m=5        m=8     max/M")
for nm, G in mats:
    Mg, _ = M_of(G); row = []
    for m in [1, 2, 3, 5, 8]:
        b, _, _ = best(G, m, 12, rng); row.append(b)
    print(f"  {nm:<30} {Mg:<11.6f} " + " ".join(f"{x:<10.6f}" for x in row) + f" {max(row)/Mg:.6f}")

print()
print("TABELA K4  rodzina [[-1,k],[0,-1]]: widmo STALE (-1,-1), M rosnie z k")
print("  k      mu_2        M(G)           max (m=4)      max/M")
for k in [1., 2., 4., 10., 30., 100.]:
    G = np.array([[-1., k], [0., -1.]])
    b, Mg, _ = best(G, 4, 12, rng)
    print(f"  {k:<6.0f} {mu2(G):+.6f}  {Mg:<14.9f} {b:<14.9f} {b/Mg:.9f}")
