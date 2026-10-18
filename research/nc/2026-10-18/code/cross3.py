import numpy as np
from scipy.optimize import minimize

# CZY ISTNIEJE PROG TLUMIENIA PRZYWRACAJACY SUFIT MIMO NIEWSPOLOSIOWOSCI
# poprzedza: cross.py 83a18bbdd64797ae12e7fdd0bf28a3d5cde31db45c93041ece87893fd576a961
# Poprzednia wersja liczyla expm w petli i nie konczyla. Tu postac zamknieta:
#   G = [[-a, 1],[-1, -a]]  =>  e^{Gt} = e^{-at} * [[cos t, sin t],[-sin t, cos t]]
#   mu_2(G) = -a
GAM = 1.0

def val(a, phi, v0, ts, ss):
    ex, ey = 1.0, 0.0
    dx, dy = np.cos(phi), np.sin(phi)
    x, y = v0; t = 0.0; acc = 0.0
    o = np.argsort(ts)
    for tj, s in zip(np.asarray(ts)[o], np.asarray(ss)[o]):
        dt = tj - t; ed = np.exp(-a*dt); ct, st = np.cos(dt), np.sin(dt)
        x, y = ed*(x*ct + y*st), ed*(-x*st + y*ct)
        t = tj
        u = np.exp(-GAM*s)
        acc += ((x*ex + y*ey)*(1.0-u)/GAM)**2
        p = x*dx + y*dy
        x += (u-1.0)*p*dx; y += (u-1.0)*p*dy
    return GAM*np.sqrt(acc)

def attack(a, phi, k, nstart, rng):
    best = 0.0
    for _ in range(nstart):
        x0 = np.concatenate([rng.uniform(0, 4*k, k), rng.uniform(0.1, 20, k), [rng.uniform(0, 2*np.pi)]])
        f = lambda z: -val(a, phi, (np.cos(z[-1]), np.sin(z[-1])), np.abs(z[:k]), np.abs(z[k:2*k])+1e-9)
        r = minimize(f, x0, method='Nelder-Mead',
                     options={'maxiter':4000,'maxfev':4000,'xatol':1e-9,'fatol':1e-12})
        best = max(best, -r.fun)
    return best

print("TABELA T1  atak ukierunkowany przy phi = pi/2, rosnace tlumienie a = -mu_2 ; k = 8")
rng = np.random.default_rng(91)
for a in [0.0, 0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.8, 1.2, 2.0]:
    v = attack(a, np.pi/2, 8, 12, rng)
    print(f"  a = {a:<6} mu_2 = {-a:<8.3f} sup = {v:<12.6f} {'ZLAMANY' if v>1+1e-9 else 'sufit trzyma'}")

print()
print("TABELA T2  czy wiecej pomiarow odwraca wynik przy duzym tlumieniu?")
print("  a       k=2        k=4        k=8        k=16       k=32")
for a in [0.5, 0.8, 2.0]:
    row = [attack(a, np.pi/2, k, 8, rng) for k in [2,4,8,16,32]]
    print(f"  {a:<7} " + " ".join(f"{v:<10.6f}" for v in row))

print()
print("TABELA T3  granica w plaszczyznie (phi, a): najwieksze a lamiace sufit przy danym phi")
print("  phi/pi    a_prog (bisekcja, k=16)")
for fr in [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]:
    phi = fr*np.pi; lo, hi = 0.0, 3.0
    if attack(0.0, phi, 16, 6, rng) <= 1+1e-9:
        print(f"  {fr:<9.3f} brak lamania nawet przy a = 0"); continue
    for _ in range(9):
        mid = (lo+hi)/2
        if attack(mid, phi, 16, 6, rng) > 1+1e-9: lo = mid
        else: hi = mid
    print(f"  {fr:<9.3f} {lo:.4f}")

print()
print("TABELA T4  kontrola czulosci: przy phi = 0 atak nie moze przebic 1 dla zadnego a")
print("  a       sup (k=8, 12 restartow)")
for a in [0.0, 0.05, 0.2, 0.8, 2.0]:
    print(f"  {a:<7} {attack(a, 0.0, 8, 12, rng):.9f}")
