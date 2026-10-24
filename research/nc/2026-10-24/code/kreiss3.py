import numpy as np
from scipy.optimize import minimize

# NC-OPN-002, RUNDA 2. PREREG_KREISS.md F5 WYSTRZELIL przy m=3 (max=sqrt(3)).
# HIPOTEZA DIAGNOSTYCZNA (D): F5 byl zle wyprowadzony, nie kod. Tozsamosc ksiegowa
#   (gamma c)^2 = (A^2 - A'^2) tanh(gamma s/2)
# wymaga e = d. Przy swobodnych e,d spadek normy mierzy d, zysk mierzy e, i gdy
# d _|_ v (pomiar bez back-action na ten stan) kazdy z m pomiarow daje pelny zysk.
# PRZEWIDYWANIA, ktore moga mnie zabic:
#   P1  przy mu_2 <= 0 i swobodnych (e,d): max = sqrt(m) DOKLADNIE (|max/sqrt(m) - 1| < 1e-6)
#   P2  w argmax: |e^T d| -> 0  ORAZ  u -> 0 (s duze)
#   P3  po narzuceniu e = d: przy mu_2 <= 0 max <= 1 (tozsamosc ksiegowa) - to jest
#       przywrocony F5. Jesli e=d NIE da <= 1, to kod JEST zly i wszystko wstrzymuje.
#   P4  przy e = d suma teleskopujaca sum (gamma c_j)^2 <= A_1^2 <= 1 wprost z przebiegu
# Jesli P1 zawiedzie (max != sqrt(m)), diagnoza D jest falszywa.

GAM = 1.0

def nrm2(M):
    return float(np.sqrt(max(np.linalg.eigvalsh(M.T @ M))))

def E(G, t):
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

def unpack(z, m, mode, G):
    """mode: 'free' (e,d osobno) | 'eq' (e=d) | theta (float: d = cos t e + sin t e_perp)"""
    ts = np.abs(z[:m]); ss = np.abs(z[m:2*m])+1e-9
    e = z[2*m:2*m+2]
    ne = np.linalg.norm(e)
    if ne < 1e-9:
        return None
    e = e/ne
    if mode == 'free':
        d = z[2*m+2:2*m+4]
        nd = np.linalg.norm(d)
        if nd < 1e-9:
            return None
        d = d/nd
    elif mode == 'eq':
        d = e
    else:
        ep = np.array([-e[1], e[0]])
        d = np.cos(mode)*e + np.sin(mode)*ep
    return ts, ss, e, d

def best(G, m, mode='free', restarts=22, rng=None, smax=40.0):
    rng = rng or np.random.default_rng(0)
    Mg, targ = M_of(G)
    nz = 2*m + (4 if mode == 'free' else 2)
    U, S, Vt = np.linalg.svd(E(G, targ))
    e0, e1 = U[:, 0], U[:, -1]
    bst = 0.0; barg = None

    def ev(z):
        p = unpack(z, m, mode, G)
        if p is None:
            return 0.0
        return np.sqrt(gram_max(G, p[2], p[3], p[0], p[1]))

    # jawne kandydaty: skupione czasy przy targ, silne pomiary, e _|_ d
    for span in (1e-3, 0.1, 0.5, 2.0, 3*targ+1e-3):
        tt = np.linspace(max(1e-5, targ-span/2), targ+span/2, m)
        for S_ in (0.5, 2., 10., 30.):
            for e_, d_ in ((e0, e0), (e0, e1), (e1, e0)):
                z = [tt, np.full(m, S_), e_] + ([d_] if mode == 'free' else [])
                z = np.concatenate(z)
                v = ev(z)
                if v > bst:
                    bst, barg = v, z.copy()
    for k in range(restarts):
        if barg is not None and k % 2 == 0:
            z0 = barg + np.concatenate([rng.normal(0, .05, m), rng.normal(0, .5, m),
                                        rng.normal(0, .15, nz-2*m)])
        else:
            z0 = np.concatenate([rng.uniform(0, 2*targ+1, m), rng.uniform(0.02, smax, m),
                                 rng.normal(0, 1, nz-2*m)])
        r = minimize(lambda z: -ev(z), z0, method="Nelder-Mead",
                     options={"maxiter": 6000, "maxfev": 6000, "xatol": 1e-10, "fatol": 1e-13})
        if -r.fun > bst:
            bst, barg = -r.fun, r.x.copy()
    return bst, Mg, barg, targ

rng = np.random.default_rng(20261024)
CONTR = [("G = 0 (mu_2 = 0)", np.zeros((2, 2))),
         ("oscylator [[0,1],[-1,0]]", np.array([[0., 1.], [-1., 0.]])),
         ("diag(-1,-2)", np.diag([-1., -2.]))]

print("TEST P1/P2  mu_2 <= 0, SWOBODNE (e,d): czy max = sqrt(m) i czy argmax ma e _|_ d, u -> 0")
print("  macierz                     m   max         sqrt(m)     max/sqrt(m)   |e.d|     max u    WERDYKT")
p1_ok = True
for nm, G in CONTR:
    for m in [1, 2, 3, 5, 8]:
        b, Mg, z, _ = best(G, m, 'free', 18, rng)
        ts, ss, e, d = unpack(z, m, 'free', G)
        dot = abs(float(e @ d)); umax = float(np.exp(-GAM*np.abs(ss)).max())
        ok = abs(b/np.sqrt(m) - 1.0) < 1e-6
        p1_ok = p1_ok and ok
        print(f"  {nm:<27} {m}   {b:<11.7f} {np.sqrt(m):<11.7f} {b/np.sqrt(m):<13.9f} {dot:<9.2e} {umax:<8.2e} "
              f"{'= sqrt(m)' if ok else 'ODBIEGA'}")
print(f"  P1 {'POTWIERDZONE' if p1_ok else 'ZALAMANE -> diagnoza D falszywa, kod podejrzany'}")

print()
print("TEST P3  F5 PRZYWROCONY: narzucam e = d, przy mu_2 <= 0 MUSI byc <= 1")
p3_ok = True
for nm, G in CONTR:
    for m in [1, 3, 8]:
        b, Mg, z, _ = best(G, m, 'eq', 14, rng)
        ok = b <= 1 + 1e-6
        p3_ok = p3_ok and ok
        print(f"  {nm:<27} m={m}  mu_2={mu2(G):+.4f}  max={b:.9f}  {'OK' if ok else 'KOD ZLY'}")
print(f"  P3 {'POTWIERDZONE - kod jest dobry, F5 byl zle wyprowadzony' if p3_ok else 'ZALAMANE - KOD ZLY'}")

print()
print("TEST P4  e = d: czy suma teleskopujaca trzyma sum (gamma c_j)^2 <= A_1^2 <= 1")
G = np.diag([-1., -2.]); e = np.array([1., 1.])/np.sqrt(2)
ts = np.array([0.05, 0.4, 1.1]); ss = np.array([0.7, 2.0, 0.3])
v = np.array([0.6, 0.8]); A = [float(np.linalg.norm(v))]
tot = 0.0; t = 0.0
for tj, s in zip(ts, ss):
    v = E(G, tj-t) @ v; t = tj
    u = np.exp(-GAM*s); Am = float(np.linalg.norm(v))
    c = (1.0-u)*float(e @ v)/GAM
    v = v - (1.0-u)*e*float(e @ v)
    Ap = float(np.linalg.norm(v))
    lhs = (GAM*c)**2; rhs = (Am**2 - Ap**2)*np.tanh(GAM*s/2)
    print(f"  pomiar t={tj:.2f} s={s:.2f}: (gc)^2={lhs:.12f}  (A^2-A'^2)tanh={rhs:.12f}  res={abs(lhs-rhs):.2e}")
    tot += lhs; A.append(Ap)
print(f"  suma (gc)^2 = {tot:.12f}   A_1^2 = {A[0]**2:.12f}   {'<=' if tot <= A[0]**2 + 1e-12 else 'NARUSZONE'}")

print()
print("TEST V5  SUFIT JAKO FUNKCJA KATA czytanie-back-action: d = cos(th) e + sin(th) e_perp")
print("  (th=0 to e=d, th=pi/2 to pomiar bez back-action na kierunek czytania)")
print("  macierz                     th/pi    m=1         m=3         m=8        m=8/sqrt(8)")
for nm, G in [("diag(-1,-2)", np.diag([-1., -2.])),
              ("Metzler M13", np.array([[-1.1, 4.], [1., -4.1]])),
              ("separator INT7", np.array([[-1., 100.], [0., -1.]]))]:
    for f in [0.0, 0.125, 0.25, 0.375, 0.5]:
        th = f*np.pi
        r = [best(G, m, th, 10, rng)[0] for m in (1, 3, 8)]
        print(f"  {nm:<27} {f:<8.3f} " + " ".join(f"{x:<11.6f}" for x in r)
              + f" {r[2]/np.sqrt(8):.6f}")
