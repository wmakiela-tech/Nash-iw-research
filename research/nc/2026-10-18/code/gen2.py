import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, eigh
from scipy.optimize import minimize

# ROZSTRZYGNIECIE G4: gdzie NAPRAWDE znika sufit
# poprzedza: gen.py sha256 f4980fed2d8f0014a4137613891c2e37ce915f595f588adefd197d3eaaef3977
#
# Predykcja G4 ("e nie jest wektorem wlasnym P => sufit znika") byla FALSZYWA.
# Powod wykryty po fakcie: pomiar jest kontrakcja EUKLIDESOWA niezaleznie od P, wiec
# gdy mu_2(G) <= 0, dziala ksiegowanie z P = I — a tam KAZDE e jest wektorem wlasnym.
# Sufit znika wiec dopiero, gdy ZADEN dopuszczalny certyfikat nie ma e jako wektora
# wlasnego, czyli w szczegolnosci gdy mu_2(G) > 0 I e jest niewspolosiowe z P.
# Ponizej test tego przypadku na generatorze M13.

GAM = 1.0

def protocol(G, e, P, times, strengths, v0, gam=GAM):
    v = np.array(v0, dtype=float); t = 0.0; c = []; dQ = []; nrm = []
    for tj, s in zip(times, strengths):
        v = expm(G*(tj-t)) @ v; t = tj
        u = np.exp(-gam*s); pe = v @ e
        c.append(pe*(1.0-u)/gam)
        Qo = v @ P @ v; no = v @ v
        v = v - (1.0-u)*pe*e
        dQ.append(Qo - v @ P @ v); nrm.append(no - v @ v)
    return np.array(c), np.array(dQ), np.array(nrm)

def n2(G,e,ts,ss,v0):
    c,_,_ = protocol(G,e,np.eye(len(e)),ts,ss,v0); return GAM*np.sqrt(np.sum(c*c))

AM = np.array([[-11/10, 4.0],[1.0, -41/10]])
PM = solve_continuous_lyapunov(AM.T, -np.eye(2)); PM = (PM+PM.T)/2
wM, VM = eigh(PM)
mu2 = np.max(np.linalg.eigvalsh((AM+AM.T)/2))

print("TABELA H1  generator M13: mu_2 > 0, wiec P = I NIE jest certyfikatem")
print(f"  mu_2(A) = {mu2:.10f} > 0 ; wartosci wlasne P: {wM[0]:.6f} {wM[1]:.6f}")
print("  e dobrane MIEDZY wektorami wlasnymi P (kat alpha od wektora idx=1)")
print("  alpha[deg]  e^T P e    Pe-parallel? (resid)   sup gamma||c||_2 (skan 60000)   > 1 ?")
rng = np.random.default_rng(51)
for adeg in [0, 15, 30, 45, 60, 75, 90]:
    a = np.radians(adeg)
    e = np.cos(a)*VM[:,1] + np.sin(a)*VM[:,0]; e /= np.linalg.norm(e)
    Pe = PM @ e; resid = np.linalg.norm(Pe - (e @ Pe)*e)
    best = 0.0
    for _ in range(60000):
        k = int(rng.integers(1,6))
        ts = np.sort(rng.uniform(0,15.0,k)); ss = np.exp(rng.uniform(np.log(1e-2),np.log(60.0),k))
        v0 = rng.normal(0,1,2); v0 /= np.linalg.norm(v0)
        best = max(best, n2(AM,e,ts,ss,v0))
    print(f"  {adeg:<11} {e@PM@e:<10.6f} {resid:<22.6f} {best:<31.6f} {'TAK' if best>1 else 'nie'}")

print()
print("TABELA H2  to samo, ale z optymalizacja (nie losowo) — czy da sie przebic 1")
print("  alpha[deg]  optimum k=1   k=2        k=3        k=4        max")
for adeg in [0, 30, 45, 60, 90]:
    a = np.radians(adeg)
    e = np.cos(a)*VM[:,1] + np.sin(a)*VM[:,0]; e /= np.linalg.norm(e)
    row = []
    for k in [1,2,3,4]:
        best = 0.0
        for _ in range(30):
            th = rng.uniform(0, 2*np.pi); v0 = np.array([np.cos(th), np.sin(th)])
            x0 = np.concatenate([np.sort(rng.uniform(0,8,k)), np.full(k,6.0), [th]])
            def f(x):
                v = np.array([np.cos(x[-1]), np.sin(x[-1])])
                return -n2(AM,e,np.sort(np.abs(x[:k])),np.abs(x[k:2*k])+1e-9,v)
            r = minimize(f, x0, method='Nelder-Mead', options={'maxiter':6000,'xatol':1e-10,'fatol':1e-13})
            best = max(best, -r.fun)
        row.append(best)
    print("  %-11d " % adeg + " ".join(f"{v:<10.6f}" for v in row) + f" {max(row):.6f}")

print()
print("TABELA H3  czy sufit = 1 zachodzi dokladnie wtedy, gdy mu_2(G) <= 0 ?")
print("  losowe G, sprawdzamy sup gamma||c||_2 przy e losowym (NIE wektorze wlasnym niczego)")
print("  mu_2 przedzial     prob    sup gamma||c||_2   naruszen 1")
rng3 = np.random.default_rng(52)
buckets = {'mu2 <= 0':[], '0 < mu2 <= 0.5':[], '0.5 < mu2 <= 2':[], 'mu2 > 2':[]}
for _ in range(4000):
    n = int(rng3.integers(2,5))
    G = rng3.normal(0,1,(n,n)) - rng3.uniform(0.5,3.0)*np.eye(n)
    if np.max(np.real(np.linalg.eigvals(G))) >= -1e-3: continue
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    e = rng3.normal(0,1,n); e /= np.linalg.norm(e)
    best = 0.0
    for _ in range(25):
        k = int(rng3.integers(1,5))
        ts = np.sort(rng3.uniform(0,12.0,k)); ss = np.exp(rng3.uniform(np.log(1e-2),np.log(60.0),k))
        v0 = rng3.normal(0,1,n); v0 /= np.linalg.norm(v0)
        best = max(best, n2(G,e,ts,ss,v0))
    key = ('mu2 <= 0' if m<=0 else '0 < mu2 <= 0.5' if m<=0.5 else '0.5 < mu2 <= 2' if m<=2 else 'mu2 > 2')
    buckets[key].append(best)
for key, vals in buckets.items():
    if not vals: continue
    v = np.array(vals)
    print(f"  {key:<18} {len(v):<7} {v.max():<18.6f} {int(np.sum(v>1+1e-9))}")

print()
print("TABELA H4  wzmocnienie przejsciowe jako wlasciwy sufit przy mu_2 > 0")
print("  hipoteza po fakcie: sufit = sup_t ||e^{Gt}||_2  (maksymalne wzmocnienie przejsciowe)")
print("  G                       mu_2        sup_t||e^Gt||   sup gamma||c||_2   iloraz")
rng4 = np.random.default_rng(53)
tests = [AM]
for _ in range(7):
    n = int(rng4.integers(2,4))
    while True:
        G = rng4.normal(0,1.5,(n,n)) - rng4.uniform(0.5,2.0)*np.eye(n)
        if np.max(np.real(np.linalg.eigvals(G))) < -1e-2 and np.max(np.linalg.eigvalsh((G+G.T)/2))>0: break
    tests.append(G)
for G in tests:
    n = G.shape[0]
    m = np.max(np.linalg.eigvalsh((G+G.T)/2))
    tg = max(np.linalg.norm(expm(G*t), 2) for t in np.linspace(0, 30, 3000))
    best = 0.0
    for _ in range(25000):
        k = int(rng4.integers(1,5))
        ts = np.sort(rng4.uniform(0,15.0,k)); ss = np.exp(rng4.uniform(np.log(1e-2),np.log(60.0),k))
        e = rng4.normal(0,1,n); e /= np.linalg.norm(e)
        v0 = rng4.normal(0,1,n); v0 /= np.linalg.norm(v0)
        best = max(best, n2(G,e,ts,ss,v0))
    print(f"  n={n} {str(np.round(G.ravel(),2).tolist())[:20]:<22} {m:<11.5f} {tg:<15.6f} {best:<18.6f} {best/tg:.6f}")
