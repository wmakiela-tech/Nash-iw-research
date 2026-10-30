import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

# CZY ISTNIEJE PROG TLUMIENIA, PRZY KTORYM SUFIT WRACA MIMO NIEWSPOLOSIOWOSCI?
# poprzedza: cross.py sha256 83a18bbdd64797ae12e7fdd0bf28a3d5cde31db45c93041ece87893fd576a961
#
# C1 pokazala, ze przy a = 0.2 protokol regularny daje 0.8206 < 1, a przy a = 0.05 atak
# ukierunkowany daje 2.154 > 1. C3 nie testowala a = 0.2. Pytanie: czy komorka 2x2
# "phi != 0, mu_2 <= 0 => brak sufitu" jest prawdziwa dla KAZDEGO tlumienia, czy tylko
# dla slabego. Jesli istnieje prog a*(phi), tabela 2x2 jest zla i trzeba ja zastapic
# krzywa w plaszczyznie (phi, a).

GAM = 1.0

def val(G, e, d, v0, ts, ss, gam=GAM):
    v = np.array(v0, float); t = 0.0; c = []
    o = np.argsort(ts)
    for tj, s in zip(np.array(ts)[o], np.array(ss)[o]):
        v = expm(G*(tj-t)) @ v; t = tj
        u = np.exp(-gam*s)
        c.append((v @ e)*(1.0-u)/gam)
        p = v @ d
        v = v - p*d + p*u*d
    c = np.array(c); return gam*np.sqrt(np.sum(c*c))

def rot2(th): return np.array([[np.cos(th), -np.sin(th)],[np.sin(th), np.cos(th)]])

def attack(a, phi, k, nstart, rng):
    G = np.array([[-a, 1.0],[-1.0, -a]]); e = np.array([1.0,0.0]); d = rot2(phi) @ e
    best = 0.0
    for _ in range(nstart):
        x0 = np.concatenate([rng.uniform(0, 6*k, k), rng.uniform(0.1, 25, k), [rng.uniform(0,2*np.pi)]])
        f = lambda x: -val(G, e, d, np.array([np.cos(x[-1]), np.sin(x[-1])]),
                           np.abs(x[:k]), np.abs(x[k:2*k])+1e-9)
        r = minimize(f, x0, method='Nelder-Mead',
                     options={'maxiter':25000,'maxfev':25000,'xatol':1e-11,'fatol':1e-14})
        best = max(best, -r.fun)
    return best

print("TABELA T1  atak ukierunkowany przy phi = pi/2, rosnace tlumienie a = -mu_2")
print("  k = 8; 16 restartow; szukam progu, przy ktorym sufit wraca")
rng = np.random.default_rng(91)
for a in [0.0, 0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.8, 1.2, 2.0]:
    v = attack(a, np.pi/2, 8, 16, rng)
    print(f"  a = {a:<6} mu_2 = {-a:<8.3f} sup gamma||c||_2 = {v:<12.6f} {'ZLAMANY' if v>1+1e-9 else 'sufit trzyma'}")

print()
print("TABELA T2  czy wiecej pomiarow odwraca wynik przy duzym tlumieniu? a = 0.8 i 2.0")
print("  a       k=2        k=4        k=8        k=16       k=32")
for a in [0.8, 2.0]:
    row = [attack(a, np.pi/2, k, 8, rng) for k in [2,4,8,16,32]]
    print(f"  {a:<7} " + " ".join(f"{v:<10.6f}" for v in row))

print()
print("TABELA T3  granica w plaszczyznie (phi, a): najmniejsze a lamiace sufit przy danym phi")
print("  dla kazdego phi bisekcja po a, k = 8")
def breaks(a, phi, rng):
    return attack(a, phi, 8, 10, rng) > 1 + 1e-9
print("  phi/pi    a_prog (bisekcja)   sup przy a_prog/2   sup przy a_prog*2")
for fr in [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]:
    phi = fr*np.pi
    lo, hi = 0.0, 4.0
    if not breaks(lo, phi, rng):
        print(f"  {fr:<9.3f} brak lamania nawet przy a=0"); continue
    for _ in range(11):
        mid = (lo+hi)/2
        if breaks(mid, phi, rng): lo = mid
        else: hi = mid
    print(f"  {fr:<9.3f} {lo:<19.5f} {attack(lo/2,phi,8,8,rng):<19.6f} {attack(min(lo*2,4.0),phi,8,8,rng):.6f}")

print()
print("TABELA T4  kontrola czulosci: przy phi = 0 atak nie moze przebic 1 dla zadnego a")
print("  a       sup gamma||c||_2 (k=8, 16 restartow)")
for a in [0.0, 0.05, 0.2, 0.8, 2.0]:
    print(f"  {a:<7} {attack(a, 0.0, 8, 16, rng):.9f}")
