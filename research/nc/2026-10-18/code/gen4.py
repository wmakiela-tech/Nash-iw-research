import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize, differential_evolution

# ATAK UKIERUNKOWANY NA WLASNY WNIOSEK GLOWNY: mu_2(G) <= 0  =>  gamma||c||_2 <= 1
# poprzedza: gen3.py sha256 e005ad71922e00e9b356307f17c8c006f03276eaa71c6a24f89c8e52d4ec9f36
#
# Powod tego skryptu: R2 oparla wniosek na skanie LOSOWYM po e. Ta sama sesja pokazala
# dwa razy, ze skan losowy/siatkowy potrafi przeoczyc obszar lamiacy teze (cwiartka
# zamiast polkola w H1; niedomiarowa probka w R3). Zanim zapisze wniosek, atakuje go
# optymalizacja po WSZYSTKICH parametrach naraz: kierunek odczytu, stan poczatkowy,
# czasy, sily. Jesli sufit da sie przebic, to tu.

GAM = 1.0

def val(G, e, v0, ts, ss, gam=GAM):
    v = np.array(v0, float); t = 0.0; c = []
    order = np.argsort(ts)
    for tj, s in zip(np.array(ts)[order], np.array(ss)[order]):
        v = expm(G*(tj-t)) @ v; t = tj
        u = np.exp(-gam*s); pe = v @ e
        c.append(pe*(1.0-u)/gam)
        v = v - (1.0-u)*pe*e
    c = np.array(c); return gam*np.sqrt(np.sum(c*c))

def pack(x, n, k):
    e = x[:n]; e = e/max(np.linalg.norm(e),1e-12)
    v0 = x[n:2*n]; v0 = v0/max(np.linalg.norm(v0),1e-12)
    ts = np.abs(x[2*n:2*n+k]); ss = np.abs(x[2*n+k:2*n+2*k])+1e-9
    return e, v0, ts, ss

def attack(G, k, nstart, rng):
    n = G.shape[0]; best = 0.0
    f = lambda x: -val(G, *pack(x, n, k))
    for _ in range(nstart):
        x0 = np.concatenate([rng.normal(0,1,n), rng.normal(0,1,n),
                             rng.uniform(0,10,k), rng.uniform(0.1,30,k)])
        r = minimize(f, x0, method='Nelder-Mead',
                     options={'maxiter':20000,'maxfev':20000,'xatol':1e-11,'fatol':1e-14})
        best = max(best, -r.fun)
    return best

print("TABELA S1  mu_2 <= 0 : optymalizacja po (e, v0, czasy, sily). Czy da sie przebic 1?")
print("  n   mu_2        k=1        k=2        k=3        k=4        MAX        > 1 ?")
rng = np.random.default_rng(71)
mx = 0.0
got = 0
for trial in range(26):
    n = int(rng.integers(2,5))
    # konstrukcja G z mu_2 <= 0: skosnie symetryczne + ujemnie okreslona czesc symetryczna
    S = rng.normal(0,1.5,(n,n)); S = (S - S.T)/2
    D = rng.normal(0,1,(n,n)); D = (D + D.T)/2
    D = D - (np.max(np.linalg.eigvalsh(D)) + rng.uniform(0.0,1.0))*np.eye(n)
    G = S + D
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    if m > 0: continue
    row = [attack(G, k, 6, rng) for k in [1,2,3,4]]
    mm = max(row); mx = max(mx, mm); got += 1
    flag = 'TAK' if mm > 1+1e-9 else 'nie'
    if got <= 12 or mm > 1+1e-9:
        print(f"  {n}   {m:<11.6f} " + " ".join(f"{v:<10.7f}" for v in row) + f" {mm:<10.7f} {flag}")
print(f"  zbadanych: {got};  NAJWIEKSZE gamma||c||_2 w calym ataku: {mx:.9f}")

print()
print("TABELA S2  kontrola czulosci ataku: ten sam atak na generatorach z mu_2 TUZ POWYZEJ 0")
print("  (jesli atak jest sprawny, musi tu lamac sufit — inaczej S1 nic nie dowodzi)")
print("  n   mu_2        MAX gamma||c||_2   > 1 ?")
rng2 = np.random.default_rng(72)
found = 0; tried = 0
for trial in range(14):
    n = int(rng2.integers(2,4))
    S = rng2.normal(0,1.5,(n,n)); S = (S - S.T)/2
    D = rng2.normal(0,1,(n,n)); D = (D + D.T)/2
    eps = rng2.uniform(0.005, 0.15)
    D = D - (np.max(np.linalg.eigvalsh(D)) - eps)*np.eye(n)
    G = S + D
    if np.max(np.real(np.linalg.eigvals(G))) >= -1e-4: continue
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    if m <= 0: continue
    tried += 1
    mm = max(attack(G, k, 6, rng2) for k in [2,3,4])
    if mm > 1+1e-9: found += 1
    print(f"  {n}   {m:<11.6f} {mm:<18.9f} {'TAK' if mm>1+1e-9 else 'nie'}")
print(f"  generatorow z mu_2 > 0 zbadanych: {tried};  sufit zlamany w: {found}")

print()
print("TABELA S3  kontrola pokrycia kierunkow — reguła po bledzie H1")
print("  sprawdzam, czy zbior kierunkow e wygenerowany w S1 pokrywa pelna sfere,")
print("  a nie tylko stozek: najwiekszy kat miedzy para kierunkow (ma byc bliski 180 deg)")
rng3 = np.random.default_rng(73)
for n in [2,3,4]:
    E = rng3.normal(0,1,(400,n)); E = E/np.linalg.norm(E,axis=1,keepdims=True)
    cosmin = np.min(E @ E.T)
    print(f"  n={n}  min cos(kat) = {cosmin:.6f}  -> max kat = {np.degrees(np.arccos(np.clip(cosmin,-1,1))):.2f} deg")
print("  dla porownania, cwiartka z H1: alpha w [0,90] deg")
VQ = np.array([[np.cos(a), np.sin(a)] for a in np.radians(np.arange(0,91,10))])
print(f"  min cos(kat) = {np.min(VQ @ VQ.T):.6f}  -> max kat = {np.degrees(np.arccos(np.clip(np.min(VQ@VQ.T),-1,1))):.2f} deg  (NIEPELNE)")
