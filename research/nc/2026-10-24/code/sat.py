import numpy as np
from scipy.integrate import solve_ivp

# PREREG_SAT.md — NC-OPN-010. Kolejnosc F1 -> F5/F6 -> F2 -> F3 -> F4 obowiazujaca.
KAP = 1.0
T = 4.0
NS = 1.0          # prog nasycenia
G0 = 0.5          # Gamma_0 w rezimie nasycenia
ATOL, RTOL = 1e-13, 1e-12

def rc(t, a, b, area):
    """podniesiony cosinus C^1 na [a,b] o zadanej calce; 0 poza"""
    if t <= a or t >= b:
        return 0.0
    w = b - a
    return area*(1.0 - np.cos(2*np.pi*(t-a)/w))/w

def S_early(t):  return rc(t, 0.2, 1.4, 2.0)
def S_late(t):   return rc(t, 2.6, 3.8, 2.0)
def S_split(t):  return rc(t, 0.2, 1.0, 1.0) + rc(t, 3.0, 3.8, 1.0)

def sstep(x):
    """C^1 gladki krok: 0 dla x<=0, DOKLADNIE 1 dla x>=1"""
    if x <= 0.0: return 0.0
    if x >= 1.0: return 1.0
    return x*x*(3.0 - 2.0*x)

def G_sat(n):   return G0*sstep(n/NS)          # dokladnie G0 dla n >= NS
def G_lin(n):   return 0.5*max(n, 0.0)/10.0*1.0  # liniowe, nienasycone

def run(S, G, lam, n0):
    def f(t, y):
        n, X, I = y
        g = G(n)
        return [S(t) - g, -lam*X + KAP*g, g]
    r = solve_ivp(f, (0.0, T), [n0, 0.0, 0.0], method="DOP853",
                  rtol=RTOL, atol=ATOL, dense_output=True)
    assert r.success, r.message
    n, X, I = r.y[:, -1]
    nmin = min(float(r.sol(t)[0]) for t in np.linspace(0, T, 4001))
    return dict(nT=float(n), XT=float(X), intG=float(I), nmin=nmin, sol=r.sol)

def intS(S):
    t = np.linspace(0, T, 200001)
    v = np.array([S(x) for x in t])
    return float(np.trapezoid(v, t))

print(f"int S_early = {intS(S_early):.12f}   int S_late = {intS(S_late):.12f}   "
      f"int S_split = {intS(S_split):.12f}")

print()
print("F1  KONTROLA: lambda>0, Gamma LINIOWE -> X(T) musza byc ROZNE")
for lam in (0.5, 1.0):
    a = run(S_early, G_lin, lam, 10.0); b = run(S_late, G_lin, lam, 10.0)
    dn = abs(a["nT"] - b["nT"]); dx = abs(a["XT"] - b["XT"])
    print(f"  lambda={lam}: n(T) {a['nT']:.12f} vs {b['nT']:.12f} (roznica {dn:.2e}); "
          f"X(T) {a['XT']:.12f} vs {b['XT']:.12f} (roznica {dx:.3e})")
    print(f"    F1 {'OK — rozne, jak wymaga MT13' if dx > 1e-6 else 'ZALAMANE -> WSTRZYMUJE WNIOSKI'}")

print()
print("F5  bilans masy int Gamma = int S - Delta n  (kontrola integratora)")
for nm, S, G, n0 in [("early/sat", S_early, G_sat, 10.0), ("late/sat", S_late, G_sat, 10.0),
                     ("early/lin", S_early, G_lin, 10.0)]:
    r = run(S, G, 1.0, n0)
    res = abs(r["intG"] - (intS(S) - (r["nT"] - n0)))
    print(f"  {nm:<12} int Gamma={r['intG']:.12f}  reszta bilansu={res:.3e}  "
          f"{'OK' if res < 1e-9 else 'ZLE'}")

print()
print("F2  NASYCENIE: n(t) >= n_s przez cale [0,T] -> X(T) musi byc ROWNE")
print("  lambda   n_min(early) n_min(late)  X(T) early        X(T) late         |roznica|   rel")
f2 = True
for lam in (0.1, 0.5, 1.0, 3.0):
    a = run(S_early, G_sat, lam, 10.0); b = run(S_late, G_sat, lam, 10.0)
    d = abs(a["XT"] - b["XT"]); rel = d/max(abs(a["XT"]), 1e-30)
    ok = rel < 1e-10
    f2 = f2 and ok
    print(f"  {lam:<8} {a['nmin']:<12.6f} {b['nmin']:<12.6f} {a['XT']:<17.12f} {b['XT']:<17.12f} "
          f"{d:<11.2e} {rel:.2e} {'OK' if ok else 'H-SAT PADA'}")
# trzecie zrodlo o tej samej calce, inny ksztalt
print("  trzecie zrodlo (dwa rozlaczne garby, ta sama calka):")
for lam in (0.5, 3.0):
    a = run(S_early, G_sat, lam, 10.0); c = run(S_split, G_sat, lam, 10.0)
    print(f"    lambda={lam}: X(T) {a['XT']:.12f} vs {c['XT']:.12f}  rel={abs(a['XT']-c['XT'])/abs(a['XT']):.2e}")
print(f"  F2 {'POTWIERDZONE' if f2 else 'ZALAMANE'}")

print()
print("F4  zgodnosc z postacia zamknieta kappa*Gamma_0*(1-e^{-lambda T})/lambda")
dn = run(S_early, G_sat, 1.0, 10.0)["nT"] - 10.0
Gamma0 = (intS(S_early) - dn)/T
print(f"  Gamma_0 z bilansu = (int S - Delta n)/T = {Gamma0:.12f}   (zadane G0 = {G0})")
for lam in (0.1, 0.5, 1.0, 3.0):
    a = run(S_early, G_sat, lam, 10.0)
    cf = KAP*Gamma0*(1.0 - np.exp(-lam*T))/lam
    print(f"  lambda={lam:<5} X(T)={a['XT']:.12f}  postac zamknieta={cf:.12f}  "
          f"rel={abs(a['XT']-cf)/abs(cf):.2e} {'OK' if abs(a['XT']-cf)/abs(cf) < 1e-10 else 'ZLE'}")

print()
print("F3  ANTY-ARTEFAKT: zrodlo wypychajace n PONIZEJ n_s -> X(T) musi byc ROZNE")
# n0 male, zrodlo pozno => n schodzi ponizej progu i Gamma przestaje byc stale
for lam in (0.5, 1.0):
    a = run(S_early, G_sat, lam, 1.6); b = run(S_late, G_sat, lam, 1.6)
    d = abs(a["XT"] - b["XT"]); rel = d/max(abs(a["XT"]), 1e-30)
    print(f"  lambda={lam}: n_min {a['nmin']:.6f} vs {b['nmin']:.6f} "
          f"(prog n_s={NS}; wyszlo ponizej: {a['nmin'] < NS or b['nmin'] < NS})")
    print(f"    X(T) {a['XT']:.12f} vs {b['XT']:.12f}  rel={rel:.3e}  "
          f"{'OK — rozne, wiec zgodnosc w F2 pochodzi z nasycenia' if rel > 1e-6 else 'F3 ZALAMANE'}")

print()
print("F6  zbieznosc / brak artefaktu kwadratury: zageszczanie tolerancji")
for rt, at in ((1e-8, 1e-9), (1e-10, 1e-11), (1e-12, 1e-13)):
    RTOL, ATOL = rt, at
    a = run(S_early, G_sat, 1.0, 10.0); b = run(S_late, G_sat, 1.0, 10.0)
    print(f"  rtol={rt:.0e}: |X_early - X_late| = {abs(a['XT']-b['XT']):.3e}")
