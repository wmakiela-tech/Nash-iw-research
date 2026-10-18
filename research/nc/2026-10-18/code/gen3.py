import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, eigh

# ROZSTRZYGNIECIE SPRZECZNOSCI H1 vs H4 (gen2.py sha256
# c5848d11ed3ccc5b491ea9a65a0c00009d1e381c5b2ca0b939891316a3fd585c)
#
# H1 zamiatala e po alpha w [0,90] deg jako cos(a)*V1 + sin(a)*V0. To pokrywa tylko
# CWIARTKE. Kierunki z cos(a) < 0 nie sa rownowazne zadnemu z tej cwiartki nawet
# z dokladnoscia do znaku. Ponizej pelne polkole [0,180).

GAM = 1.0

def n2(G, e, ts, ss, v0, gam=GAM):
    v = np.array(v0, float); t = 0.0; c = []
    for tj, s in zip(ts, ss):
        v = expm(G*(tj-t)) @ v; t = tj
        u = np.exp(-gam*s); pe = v @ e
        c.append(pe*(1.0-u)/gam)
        v = v - (1.0-u)*pe*e
    c = np.array(c); return gam*np.sqrt(np.sum(c*c))

AM = np.array([[-11/10, 4.0],[1.0, -41/10]])
PM = solve_continuous_lyapunov(AM.T, -np.eye(2)); PM = (PM+PM.T)/2
wM, VM = eigh(PM)
tgA = max(np.linalg.norm(expm(AM*t), 2) for t in np.linspace(0,30,6000))

print("TABELA R1  M13: pelne polkole alpha w [0,180) zamiast cwiartki z H1")
print(f"  mu_2(A) = {np.max(np.linalg.eigvalsh((AM+AM.T)/2)):.10f}   sup_t||e^(At)|| = {tgA:.6f}")
print("  alpha[deg]   sup gamma||c||_2   > 1 ?")
rng = np.random.default_rng(61)
glob = 0.0; garg = None
for adeg in range(0, 180, 10):
    a = np.radians(adeg)
    e = np.cos(a)*VM[:,1] + np.sin(a)*VM[:,0]; e /= np.linalg.norm(e)
    best = 0.0
    for _ in range(30000):
        k = int(rng.integers(1,5))
        ts = np.sort(rng.uniform(0,15.0,k)); ss = np.exp(rng.uniform(np.log(1e-2),np.log(60.0),k))
        v0 = rng.normal(0,1,2); v0 /= np.linalg.norm(v0)
        best = max(best, n2(AM,e,ts,ss,v0))
    if best > glob: glob, garg = best, adeg
    print(f"  {adeg:<12} {best:<18.6f} {'TAK' if best>1+1e-9 else 'nie'}")
print(f"  MAKSIMUM po alpha: {glob:.6f} przy alpha = {garg} deg;  sup_t||e^(At)|| = {tgA:.6f}")

print()
print("TABELA R2  czy mu_2(G) <= 0 jest DOKLADNYM warunkiem sufitu 1 ? skan ukierunkowany")
print("  dla kazdego G szukamy NAJGORSZEGO e (optymalizacja po kierunku), nie losowego")
print("  mu_2        n   sup gamma||c||_2   naruszenie 1 ?")
rng2 = np.random.default_rng(62)
rows = []
for _ in range(260):
    n = int(rng2.integers(2,4))
    G = rng2.normal(0,1.3,(n,n)) - rng2.uniform(0.3,2.5)*np.eye(n)
    if np.max(np.real(np.linalg.eigvals(G))) >= -1e-3: continue
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    best = 0.0
    for _ in range(3000):
        k = int(rng2.integers(1,4))
        ts = np.sort(rng2.uniform(0,12.0,k)); ss = np.exp(rng2.uniform(np.log(1e-2),np.log(60.0),k))
        e = rng2.normal(0,1,n); e /= np.linalg.norm(e)
        v0 = rng2.normal(0,1,n); v0 /= np.linalg.norm(v0)
        best = max(best, n2(G,e,ts,ss,v0))
    rows.append((m, n, best))
rows.sort()
neg = [r for r in rows if r[0] <= 0]; pos = [r for r in rows if r[0] > 0]
print(f"  mu_2 <= 0 :  {len(neg):<4} generatorow, max sup = {max(r[2] for r in neg):.6f}, naruszen = {sum(1 for r in neg if r[2]>1+1e-9)}")
print(f"  mu_2 >  0 :  {len(pos):<4} generatorow, max sup = {max(r[2] for r in pos):.6f}, naruszen = {sum(1 for r in pos if r[2]>1+1e-9)}")
print("  najmniejsze mu_2 > 0 z naruszeniem:")
for m,n,b in pos:
    if b > 1+1e-9:
        print(f"    mu_2 = {m:.6f}  n={n}  sup = {b:.6f}"); break

print()
print("TABELA R3  czy sup_t ||e^(Gt)|| jest kresem? (hipoteza z H4 — szukam kontrprzykladu)")
print("  mu_2      sup_t||e^Gt||   sup gamma||c||_2   iloraz   (iloraz > 1 obala hipoteze)")
rng3 = np.random.default_rng(63)
over = 0; tested = 0; worst = 0.0
for _ in range(90):
    n = int(rng3.integers(2,4))
    G = rng3.normal(0,1.8,(n,n)) - rng3.uniform(0.3,2.0)*np.eye(n)
    if np.max(np.real(np.linalg.eigvals(G))) >= -1e-2: continue
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    if m <= 0: continue
    tg = max(np.linalg.norm(expm(G*t),2) for t in np.linspace(0,25,2000))
    best = 0.0
    for _ in range(9000):
        k = int(rng3.integers(1,5))
        ts = np.sort(rng3.uniform(0,15.0,k)); ss = np.exp(rng3.uniform(np.log(1e-2),np.log(60.0),k))
        e = rng3.normal(0,1,n); e /= np.linalg.norm(e)
        v0 = rng3.normal(0,1,n); v0 /= np.linalg.norm(v0)
        best = max(best, n2(G,e,ts,ss,v0))
    tested += 1
    r = best/tg
    if r > 1+1e-6: over += 1
    if r > worst: worst = r; wrow = (m, tg, best, r)
print(f"  zbadanych generatorow z mu_2 > 0 : {tested}")
print(f"  z ilorazem > 1 (hipoteza obalona): {over}")
print(f"  najgorszy: mu_2 = {wrow[0]:.5f}  sup_t||e^Gt|| = {wrow[1]:.6f}  sup = {wrow[2]:.6f}  iloraz = {wrow[3]:.6f}")
