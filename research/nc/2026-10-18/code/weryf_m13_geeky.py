import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

# WERYFIKACJA KONSTRUKCJI Z AUDYTOW M13 ROT11 I GEEKY-S10 (2026-10-19)
# Nie przyjmuje liczb na slowo: MODEL AGREEMENT != PROOF dotyczy takze zgody z audytorem.
GAM = 1.0

def run(G, e, d, v0, ts, ss, gam=GAM):
    """impulsowy model NC: odczyt (1-u)/gam * e^T v^-, potem v^+ = (I-(1-u)dd^T) v^-"""
    v = np.array(v0, float); t = 0.0; acc = 0.0
    o = np.argsort(ts)
    for tj, s in zip(np.asarray(ts)[o], np.asarray(ss)[o]):
        if tj > t: v = expm(G*(tj-t)) @ v
        t = tj
        u = np.exp(-gam*s)
        acc += ((e @ v)*(1.0-u)/gam)**2
        v = v - (1.0-u)*(d @ v)*d
    return gam*np.sqrt(acc)

print("TABELA V1  M13: weryfikator Hurwitza. G=[[-1,4],[0,-1]], oba eigenvalues -1, ale mu_2 = 1")
G = np.array([[-1.0, 4.0],[0.0, -1.0]])
ev = np.linalg.eigvals(G); mu2 = np.max(np.linalg.eigvalsh((G+G.T)/2))
print(f"  eigenvalues = {np.round(ev,12).tolist()}   mu_2 = {mu2:.12f}")
v0 = np.array([0.0,1.0]); t = 0.25
w = expm(G*t) @ v0; m = np.linalg.norm(w)
print(f"  ||exp(G/4) v0|| = {m:.15f}   wzor sqrt(2)exp(-1/4) = {np.sqrt(2)*np.exp(-0.25):.15f}")
e = np.array([1.0,1.0])/np.sqrt(2); d = e
u = 1/20.0; s = -np.log(u)
val = run(G, e, d, v0, [t], [s])
pred = 19*np.sqrt(2)*np.exp(-0.25)/20
print(f"  gamma|c| zmierzone = {val:.16f}")
print(f"  gamma|c| wzor M13  = {pred:.16f}   roznica = {abs(val-pred):.2e}")
print(f"  czy > 1 : {'TAK' if val > 1 else 'NIE'}   -> konstrukcja M13 POTWIERDZONA" if val>1 else "  NIE POTWIERDZONA")

print()
print("TABELA V2  M13: dowod koniecznosci — JEDEN pomiar wystarcza, dla losowych G z mu_2 > 0")
rng = np.random.default_rng(401)
print("  n   prob   udanych konstrukcji   min gamma|c| wsrod udanych")
for n in [2,3,4]:
    ok = 0; tot = 0; mn = 1e9
    for _ in range(400):
        Gr = rng.normal(0,1.2,(n,n))
        S = (Gr+Gr.T)/2; lam, V = np.linalg.eigh(S)
        if lam[-1] <= 1e-9: continue
        tot += 1
        x = V[:,-1]                      # wektor wlasny S o najwiekszej wartosci
        # szukamy skonczonego t z ||exp(Gt)x|| > 1
        found = None
        for tt in np.linspace(1e-4, 2.0, 400):
            mm = np.linalg.norm(expm(Gr*tt) @ x)
            if mm > 1.0: found = (tt, mm); break
        if found is None: continue
        tt, mm = found
        ee = (expm(Gr*tt) @ x)/mm
        uu = max(0.5*(1-1.0/mm), 1e-12)   # u < 1 - 1/m
        ss = -np.log(uu)
        v = run(Gr, ee, ee, x, [tt], [ss])
        if v > 1+1e-12: ok += 1; mn = min(mn, v)
    print(f"  {n}   {tot:<6} {ok:<21} {mn:.9f}")

print()
print("TABELA V3  GEEKY-S10: USTALONY kierunek e — czy mu_2 <= 0 jest KONIECZNE?")
print("  G = diag(a, -b), e = d = e2 USTALONE. mu_2 = a > 0, ale mierzona skladowa jest kontraktywna.")
print("  a      b      mu_2     sup gamma||c||_2 (atak po v0, czasach, silach)   <= 1 ?")
for a, b in [(0.5,1.0),(2.0,1.0),(5.0,0.3),(20.0,2.0)]:
    G2 = np.diag([a,-b]); e2 = np.array([0.0,1.0])
    best = 0.0
    for _ in range(25):
        k = 6
        x0 = np.concatenate([rng.uniform(0,8,k), rng.uniform(0.1,25,k), [rng.uniform(0,2*np.pi)]])
        f = lambda z: -run(G2, e2, e2, (np.cos(z[-1]), np.sin(z[-1])), np.abs(z[:k]), np.abs(z[k:2*k])+1e-9)
        r = minimize(f, x0, method='Nelder-Mead', options={'maxiter':8000,'maxfev':8000,'xatol':1e-10,'fatol':1e-13})
        best = max(best, -r.fun)
    print(f"  {a:<6} {b:<6} {np.max(np.linalg.eigvalsh((G2+G2.T)/2)):<8.3f} {best:<46.9f} {'TAK' if best <= 1+1e-9 else 'NIE'}")
print("  -> jesli wszedzie TAK: globalne mu_2 <= 0 NIE jest konieczne przy ustalonym e.")
print("     Moje twierdzenie z 011 wymaga kwantyfikatora PO KIERUNKU ODCZYTU.")

print()
print("TABELA V4  GEEKY-S10: widmo CIAGLE — czy moj mechanizm jednak przezywa?")
print("  H = L^2([0,1]), D = M_x, (c1,f1) = (1, x), (c2,f2) = (x, 1)")
print("  z        int_0^1 x/(z-x)dx  dla (c1,f1)   dla (c2,f2)   roznica")
def tf(z, cfun, ffun, N=200000):
    x = (np.arange(N)+0.5)/N
    return np.sum(ffun(x)*cfun(x)/(z-x))/N
for z in [1.5, 2.0, 5.0, -1.0]:
    t1 = tf(z, lambda x: np.ones_like(x), lambda x: x)
    t2 = tf(z, lambda x: x, lambda x: np.ones_like(x))
    print(f"  {z:<8} {t1:<28.15f} {t2:<13.15f} {abs(t1-t2):.2e}")
print("  (oba sa tym samym calkowaniem int x/(z-x)dx — rownosc jest tozsamosciowa)")
print()
print("  T = M_x : ograniczony, iniektywny, obraz gesty, ale NIE ograniczony od dolu")
print("  h_n = sqrt(n) 1_[0,1/n] :  ||h_n|| = 1,  ||T h_n|| ma wynosic 1/(sqrt(3) n)")
print("  n        ||h_n||       ||T h_n|| zmierzone   wzor 1/(sqrt(3) n)   roznica")
for n in [1,2,5,10,50,200]:
    N = 2000000
    x = (np.arange(N)+0.5)/N
    h = np.where(x <= 1.0/n, np.sqrt(n), 0.0)
    nh = np.sqrt(np.sum(h*h)/N)
    nTh = np.sqrt(np.sum((x*h)**2)/N)
    pred = 1.0/(np.sqrt(3)*n)
    print(f"  {n:<8} {nh:<13.9f} {nTh:<21.12f} {pred:<19.12f} {abs(nTh-pred):.2e}")
