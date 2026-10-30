import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

# PREREG_KREISS.md sha256 7b33978aeb29bc962a72b1291537a6820de18b383b803f4507df08d975db0961
# NC-OPN-002: czy przy mu_2 > 0 sufit ekstrakcji jest skonczony i czy rowna sie M(G).
# Gramian odczytu W pochodzi od M13 (ROT11, zapisany w ART017): gamma^2 sup_{||v0||=1} ||c||_2^2 = lam_max(W).

GAM = 1.0
nrm = lambda M: np.linalg.norm(M, 2)
def mu2(G): return np.max(np.linalg.eigvalsh((G+G.T)/2))

def M_of(G, T=60.0, N=200000):
    """M(G) = sup_t ||e^{tG}||, gesto + zageszczenie wokol argmax"""
    ts = np.linspace(0, T, 3000)
    v = [nrm(expm(G*t)) for t in ts]
    i = int(np.argmax(v)); t0 = ts[i]
    lo, hi = max(0.0, t0-2*(ts[1]-ts[0])), t0+2*(ts[1]-ts[0])
    ts2 = np.linspace(lo, hi, 4000)
    v2 = [nrm(expm(G*t)) for t in ts2]
    j = int(np.argmax(v2))
    return max(max(v), max(v2)), ts2[j]

def gram(G, e, d, ts, ss, gam=GAM):
    """W = sum_j (1-u_j)^2 L_j^T e e^T L_j ; zwraca lam_max(W)/gam^2 -> (gamma||c||_2)^2"""
    o = np.argsort(ts); ts = np.asarray(ts)[o]; ss = np.asarray(ss)[o]
    n = G.shape[0]; L = np.eye(n); t = 0.0
    W = np.zeros((n, n))
    for tj, s in zip(ts, ss):
        if tj > t: L = expm(G*(tj-t)) @ L
        t = tj
        u = np.exp(-gam*s)
        w = (1.0-u)*(L.T @ e)
        W = W + np.outer(w, w)
        L = (np.eye(n) - (1.0-u)*np.outer(d, d)) @ L
    return np.max(np.linalg.eigvalsh((W+W.T)/2))/gam**2

def best(G, m, restarts=60, rng=None):
    """maksymalizuj sqrt(lam_max(W)) po czasach, silach, e, d; kandydaci strukturalni + losowe"""
    rng = rng or np.random.default_rng(0)
    n = G.shape[0]
    Mg, targ = M_of(G)
    kand = []
    # strukturalny: jeden mocny pomiar w argmax ||e^{tG}||, e wyrownane
    A = expm(G*targ); U, S, Vt = np.linalg.svd(A)
    e0 = U[:, 0]
    for S_ in (20.0, 8.0, 3.0):
        kand.append((np.array([targ]), np.array([S_]), e0, e0))
        kand.append((np.array([targ]), np.array([S_]), e0, U[:, -1]))
    # strukturalny: m rownoodstepowych wokol targ
    if m > 1:
        for span in (0.5, 1.0, 2.0):
            tt = np.linspace(max(1e-3, targ-span/2), targ+span/2, m)
            for S_ in (0.3, 1.0, 4.0):
                kand.append((tt, np.full(m, S_), e0, e0))
                kand.append((tt, np.full(m, S_), e0, U[:, -1]))
    bst = 0.0; arg = None
    for ts, ss, e, d in kand:
        v = np.sqrt(gram(G, e/np.linalg.norm(e), d/np.linalg.norm(d), ts, np.abs(ss)+1e-9))
        if v > bst: bst, arg = v, ("kand", ts, ss)
    # optymalizacja ciagla
    def neg(z):
        ts = np.abs(z[:m]); ss = np.abs(z[m:2*m])+1e-9
        e = z[2*m:2*m+n]; d = z[2*m+n:2*m+2*n]
        ne, nd = np.linalg.norm(e), np.linalg.norm(d)
        if ne < 1e-9 or nd < 1e-9: return 0.0
        return -np.sqrt(gram(G, e/ne, d/nd, ts, ss))
    for _ in range(restarts):
        if rng.random() < 0.5 and arg is not None:
            z0 = np.concatenate([np.abs(arg[1])+rng.normal(0,.1,m), np.abs(arg[2])+rng.normal(0,.3,m),
                                 e0+rng.normal(0,.2,n), e0+rng.normal(0,.3,n)])
        else:
            z0 = np.concatenate([rng.uniform(0, 2*targ+1, m), rng.uniform(0.05, 12, m),
                                 rng.normal(0,1,n), rng.normal(0,1,n)])
        r = minimize(neg, z0, method="Nelder-Mead",
                     options={"maxiter":30000,"maxfev":30000,"xatol":1e-10,"fatol":1e-13})
        if -r.fun > bst: bst = -r.fun
    return bst, Mg, targ

print("TABELA K1  F5 — KONTROLA SPOJNOSCI: przy mu_2 <= 0 maksimum MUSI byc <= 1")
rng = np.random.default_rng(20261024)
for nm, G in [("oscylator [[0,1],[-1,0]]", np.array([[0.,1],[-1,0]])),
              ("diag(-1,-2)", np.diag([-1.,-2.]))]:
    b, Mg, tg = best(G, 3, restarts=25, rng=rng)
    print(f"  {nm:<26} mu_2 = {mu2(G):+.6f}   M(G) = {Mg:.9f}   max gamma||c|| = {b:.9f}   "
          f"{'OK' if b <= 1+1e-6 else 'KOD ZLY'}")

print()
print("TABELA K2  F1 — czy optymalizator odtwarza ZNANE dolne ograniczenie M(G)")
print("  (jesli nie, jego wyniki powyzej nie dowodza niczego — lekcja z NC-OPN-024)")
mats = [("Metzler M13 [[-1.1,4],[1,-4.1]]", np.array([[-1.1,4.],[1.,-4.1]])),
        ("Hurwitz [[-1,4],[0,-1]]",          np.array([[-1.,4.],[0.,-1.]])),
        ("separator INT7 [[-1,100],[0,-1]]", np.array([[-1.,100.],[0.,-1.]]))]
print("  macierz                          mu_2        M(G)           max m=1        iloraz max/M")
for nm, G in mats:
    b1, Mg, tg = best(G, 1, restarts=40, rng=rng)
    print(f"  {nm:<32} {mu2(G):+.5f}  {Mg:<14.9f} {b1:<14.9f} {b1/Mg:.9f}")

print()
print("TABELA K3  F2/F3/F4 — czy WIECEJ pomiarow bije M(G)")
print("  macierz                        M(G)         m=1         m=2         m=3         m=5         m=8      max/M")
for nm, G in mats:
    Mg, _ = M_of(G)
    row = []
    for m in [1,2,3,5,8]:
        b, _, _ = best(G, m, restarts=30, rng=rng)
        row.append(b)
    print(f"  {nm:<30} {Mg:<12.6f} " + " ".join(f"{x:<11.6f}" for x in row) + f" {max(row)/Mg:.6f}")

print()
print("TABELA K4  rodzina [[-1,k],[0,-1]]: widmo STALE (-1,-1), M rosnie z k")
print("  k      mu_2        M(G)           max (m=4)      iloraz max/M")
for k in [1.,2.,4.,10.,30.,100.]:
    G = np.array([[-1.,k],[0.,-1.]])
    b, Mg, tg = best(G, 4, restarts=30, rng=rng)
    print(f"  {k:<6.0f} {mu2(G):+.6f}  {Mg:<14.9f} {b:<14.9f} {b/Mg:.9f}")
