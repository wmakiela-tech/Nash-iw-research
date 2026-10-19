import numpy as np

# RE-WERYFIKACJA WLASNEGO CLAIMU PO LEKCJI REC9
# Claim z ART012 par.2: "progu tlumienia nie ma" — oparty na skanie do a = 2.0.
# REC9 (11 X) zdiagnozowal u NC: NONCONTRACTION != NONEXISTENCE, czyli zawodnosc
# jednej drogi wzieta za wlasnosc problemu. Niewykrycie progu do a=2.0 ma ten sam
# ksztalt. Sprawdzam analitycznie zamiast skanowac dalej.
#
# G = [[-a, 1], [-1, -a]] : e^{Gt} = e^{-at} R(t).  mu_2 = -a.
# Protokol zerokosztowy przy niewspolosiowosci phi: pomiary w chwilach v _|_ d,
# czyli co pi. Miedzy nimi amplituda maleje o e^{-a pi}. Wklad pomiaru j:
#     gamma c_j = |sin phi| sigma(s) e^{-a pi j}
# Suma kwadratow to szereg geometryczny o ilorazie e^{-2 a pi}:
#     gamma||c||_2 = |sin phi| sigma(s) / sqrt(1 - e^{-2 a pi})
# PREDYKCJA: to jest > 1 dla KAZDEGO skonczonego a > 0 przy sin phi = 1 i sigma -> 1,
# bo 1/sqrt(1 - e^{-2 a pi}) > 1 zawsze. Progu wiec NIE MA, ale nie dlatego, ze
# skan go nie znalazl — tylko dlatego, ze kres dazy do 1 OD GORY, nigdy go nie
# przekraczajac w dol. To jest inny i mocniejszy powod niz ten, ktory podalem.

GAM = 1.0

def zerocost(a, phi, s, k):
    """protokol zerokosztowy: pomiary co pi, zaczynajac tam gdzie v _|_ d"""
    ex, ey = 1.0, 0.0
    dx, dy = np.cos(phi), np.sin(phi)
    # v(t) = e^{-at}(sin t, cos t) przy v(0)=(0,1); e=(1,0), d=(cos phi, sin phi).
    # v.d = e^{-at}(sin t cos phi + cos t sin phi) = e^{-at} sin(t+phi) -> zero przy t = -phi + j*pi.
    # Bierzemy pierwsza taka chwile dodatnia; dla phi=pi/2 to t0 = pi/2, gdzie |v.e| jest maksymalne.
    t0 = (-phi) % np.pi
    if t0 < 1e-12: t0 += np.pi
    x, y = np.exp(-a*t0)*np.sin(t0), np.exp(-a*t0)*np.cos(t0)
    t = t0; acc = 0.0
    u = np.exp(-GAM*s)
    for j in range(k):
        if j > 0:
            dt = np.pi; ed = np.exp(-a*dt); ct, st = np.cos(dt), np.sin(dt)
            x, y = ed*(x*ct + y*st), ed*(-x*st + y*ct)
            t += dt
        acc += ((x*ex + y*ey)*(1.0-u)/GAM)**2
        p = x*dx + y*dy
        x += (u-1.0)*p*dx; y += (u-1.0)*p*dy
    return GAM*np.sqrt(acc)

print("TABELA P1  czy wzor zamkniety zgadza sie z protokolem, phi = pi/2, s = 40")
print("  a        k=200 zmierzone     wzor |sin phi| sigma /sqrt(1-e^{-2 a pi})   roznica")
s = 40.0; sig = (1-np.exp(-GAM*s))/GAM
for a in [0.05, 0.2, 1.0, 2.0, 5.0, 10.0]:
    v = zerocost(a, np.pi/2, s, 200)
    pred = sig/np.sqrt(1-np.exp(-2*a*np.pi))
    # protokol startuje po swobodnym zaniku do t0 = pi/2 (pierwsza chwila v _|_ d), skala e^{-a pi/2}
    t0 = (-np.pi/2) % np.pi or np.pi      # dla phi=pi/2 pierwsza chwila v _|_ d to t0 = pi/2
    pred_scaled = pred*np.exp(-a*(np.pi/2))
    print(f"  {a:<8} {v:<19.9f} {pred_scaled:<22.9f} {abs(v-pred_scaled):.2e}")

print()
print("TABELA P2  kres przy starcie bez zaniku wstepnego (pierwszy pomiar w t=pi/2 po obrocie o phi=0)")
print("  czyli najkorzystniejsze ustawienie fazy: ile wynosi sup przy duzym a")
print("  a          1/sqrt(1-e^{-2 a pi})    czy > 1 ?")
for a in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 200.0]:
    val = 1.0/np.sqrt(1-np.exp(-2*a*np.pi))
    print(f"  {a:<10} {val:<24.12f} {'TAK' if val > 1 else 'NIE'}")
print("  granica przy a -> inf wynosi dokladnie 1, osiagana tylko w granicy.")

print()
print("TABELA P3  ale protokol zerokosztowy to DOLNE oszacowanie — co daje optymalizacja")
print("  (porownanie z ART012 T1: tam optymalizacja dawala 1.61 przy a=0.2 i 1.73 przy a=2.0)")
from scipy.optimize import minimize
def val(a, phi, v0, ts, ss):
    ex, ey = 1.0, 0.0; dx, dy = np.cos(phi), np.sin(phi)
    x, y = v0; t = 0.0; acc = 0.0
    for tj, s_ in zip(np.sort(ts), np.asarray(ss)[np.argsort(ts)]):
        dt = tj - t; ed = np.exp(-a*dt); ct, st = np.cos(dt), np.sin(dt)
        x, y = ed*(x*ct + y*st), ed*(-x*st + y*ct); t = tj
        u = np.exp(-GAM*s_)
        acc += ((x*ex + y*ey)*(1.0-u)/GAM)**2
        p = x*dx + y*dy
        x += (u-1.0)*p*dx; y += (u-1.0)*p*dy
    return GAM*np.sqrt(acc)
rng = np.random.default_rng(301)
print("  a        sup (opt, k=8)   dolne oszac. zerokosztowe   czy sufit zlamany")
for a in [2.0, 5.0, 10.0, 20.0, 50.0]:
    best = 0.0
    for _ in range(14):
        k = 8
        x0 = np.concatenate([rng.uniform(0, 4*k, k), rng.uniform(0.1, 30, k), [rng.uniform(0, 2*np.pi)]])
        f = lambda z: -val(a, np.pi/2, (np.cos(z[-1]), np.sin(z[-1])), np.abs(z[:k]), np.abs(z[k:2*k])+1e-9)
        r = minimize(f, x0, method='Nelder-Mead', options={'maxiter':6000,'maxfev':6000,'xatol':1e-10,'fatol':1e-13})
        best = max(best, -r.fun)
    lo = 1.0/np.sqrt(1-np.exp(-2*a*np.pi))
    print(f"  {a:<8} {best:<16.9f} {lo:<27.12f} {'TAK' if best > 1+1e-9 else 'NIE'}")

print()
print("TABELA P4  kontrola czulosci: przy phi = 0 (wspolosiowo) sufit MUSI trzymac dla kazdego a")
for a in [2.0, 10.0, 50.0]:
    best = 0.0
    for _ in range(14):
        k = 8
        x0 = np.concatenate([rng.uniform(0, 4*k, k), rng.uniform(0.1, 30, k), [rng.uniform(0, 2*np.pi)]])
        f = lambda z: -val(a, 0.0, (np.cos(z[-1]), np.sin(z[-1])), np.abs(z[:k]), np.abs(z[k:2*k])+1e-9)
        r = minimize(f, x0, method='Nelder-Mead', options={'maxiter':6000,'maxfev':6000,'xatol':1e-10,'fatol':1e-13})
        best = max(best, -r.fun)
    print(f"  a = {a:<7} sup = {best:.9f}   {'OK (<= 1)' if best <= 1+1e-9 else 'NARUSZENIE'}")
