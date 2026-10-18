import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

# DOMKNIECIE TABELI 2x2: (phi = 0 ?) x (mu_2 <= 0 ?)
# poprzedza: l2c.py c677751a318fb2ed409991172cc56ffc53b0b9522102344ea07912e065a2b43a (phi != 0)
#            gen4.py 1642682fc21ca3b37252c66255c0c633782e4ed5e191d1481e181e39d1d2cd10 (mu_2)
#
# ART011 par.6.4 zapisalem jako OTWARTE pytanie, czy mu_2 <= 0 ratuje sufit przy phi != 0.
# To bylo bledne: oscylator z ART010 par.3 MA mu_2 = 0, a sufit tam znika. Ponizej
# sprawdzam, czy to nie jest przypadek brzegowy mu_2 = 0 dokladnie, biorac mu_2 OSTRO ujemne.
#
# Zgodnie z regula z ART011 par.5: kazda tabela ma kontrole pokrycia i kontrole czulosci.

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

print("TABELA C1  phi != 0 przy mu_2 OSTRO ujemnym: czy sufit nadal znika?")
print("  G = [[-a, 1],[-1, -a]] (obrot + izotropowe tlumienie), mu_2 = -a < 0")
print("  e = (1,0); d obrocone o phi; protokol co pi (tam gdzie v _|_ d przy a=0)")
print("  a       mu_2      phi/pi   k=4        k=64       k=1024     k=16384    rosnie?")
for a in [0.0, 0.001, 0.01, 0.05, 0.2]:
    G = np.array([[-a, 1.0],[-1.0, -a]])
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    for fr in [0.5]:
        phi = fr*np.pi
        e = np.array([1.0, 0.0]); d = rot2(phi) @ e
        row = []
        for k in [4, 64, 1024, 16384]:
            ts = np.array([np.pi/2 + j*np.pi for j in range(k)])
            row.append(val(G, e, d, np.array([0.0,1.0]), ts, np.full(k, 3.0)))
        gr = 'TAK' if row[-1] > row[0]*1.5 else 'nasyca'
        print(f"  {a:<7} {m:<9.4f} {fr:<8.2f} " + " ".join(f"{v:<10.4f}" for v in row) + f" {gr}")

print()
print("TABELA C2  kontrola czulosci: ten sam uklad przy phi = 0 MUSI dac sufit 1")
print("  a       mu_2      k=4        k=64       k=1024     k=16384")
for a in [0.0, 0.001, 0.01, 0.05, 0.2]:
    G = np.array([[-a, 1.0],[-1.0, -a]])
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    e = np.array([1.0, 0.0]); d = e
    row = []
    for k in [4, 64, 1024, 16384]:
        ts = np.array([np.pi/2 + j*np.pi for j in range(k)])
        row.append(val(G, e, d, np.array([0.0,1.0]), ts, np.full(k, 3.0)))
    print(f"  {a:<7} {m:<9.4f} " + " ".join(f"{v:<10.6f}" for v in row))

print()
print("TABELA C3  atak ukierunkowany na cwiartke (phi != 0, mu_2 < 0), pelne pokrycie phi")
print("  a = 0.05 (mu_2 = -0.05 < 0); optymalizacja po (phi, czasy, sily, v0), k = 6")
print("  phi/pi    sup gamma||c||_2 (k=6)   > 1 ?")
a = 0.05; G = np.array([[-a, 1.0],[-1.0, -a]]); e = np.array([1.0,0.0])
rng = np.random.default_rng(81)
glob = 0.0
for fr in np.arange(0.0, 1.0, 0.125):
    phi = fr*np.pi; d = rot2(phi) @ e
    best = 0.0
    for _ in range(14):
        k = 6
        x0 = np.concatenate([rng.uniform(0, 20, k), rng.uniform(0.1, 20, k), [rng.uniform(0,2*np.pi)]])
        f = lambda x: -val(G, e, d, np.array([np.cos(x[-1]), np.sin(x[-1])]),
                           np.abs(x[:k]), np.abs(x[k:2*k])+1e-9)
        r = minimize(f, x0, method='Nelder-Mead', options={'maxiter':20000,'maxfev':20000,'xatol':1e-10,'fatol':1e-13})
        best = max(best, -r.fun)
    glob = max(glob, best)
    print(f"  {fr:<9.3f} {best:<23.6f} {'TAK' if best > 1+1e-9 else 'nie'}")
print(f"  kontrola pokrycia: phi zamiecione na [0, pi), czyli pelny zakres niewspolosiowosci")
print(f"  MAKSIMUM: {glob:.6f}")

print()
print("TABELA C4  domknieta tabela 2x2 (wartosci z tej sesji)")
print("  phi      mu_2      sufit gamma||c||_2 <= 1 ?   zrodlo")
print("  = 0      <= 0      TAK (dowod)                ART011 par.1, gen4 S1: 26 gen., max 1.000000000")
print("  = 0      >  0      NIE                        ART011 par.2, gen4 S2: 12/12 zlaman")
print("  != 0     <= 0      NIE                        ART010 par.3 + C1/C3 wyzej")
print("  != 0     >  0      NIE (a fortiori)           zawiera sie w obu powyzszych")
