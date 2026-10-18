import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, eigh

# UOGOLNIENIE KSIEGOWANIA NA DOWOLNY GENERATOR
# prerejestracja: PREREG_GEN.md sha256 9241090d1d5e1267b1c544f6fef697bc9374661f2da790cd1d20c8ff197b96a5
#
# v' = G v ; czujnik czyta (v.e) z sigma(s) i tlumi skladowa wzdluz e przez u = e^{-gamma s}
# Q(v) = v^T P v, P > 0 certyfikat Lapunowa: G^T P + P G <= 0
# p = e^T P e, m = e^T P v
#   dQ = 2 (gamma c) m - (gamma c)^2 p
# przy P e = p e :  (gamma c)^2 = dQ * tanh(gamma s/2)/p  oraz  gamma||c||_2 <= sqrt(lmax(P)/p)

GAM = 1.0

def protocol(G, e, P, times, strengths, v0, gam=GAM):
    """zwraca (c, dQ) ; e znormalizowane euklidesowo"""
    v = np.array(v0, dtype=float); t = 0.0
    c, dQ = [], []
    for tj, s in zip(times, strengths):
        v = expm(G*(tj-t)) @ v; t = tj
        u = np.exp(-gam*s)
        pe = v @ e
        c.append(pe*(1.0-u)/gam)
        Qo = v @ P @ v
        v = v - (1.0-u)*pe*e
        dQ.append(Qo - v @ P @ v)
    return np.array(c), np.array(dQ)

def lyap_cert(G):
    """P > 0 z G^T P + P G = -I  (istnieje gdy G Hurwitz); zwraca None gdy nie Hurwitz"""
    if np.max(np.real(np.linalg.eigvals(G))) >= -1e-12: return None
    P = solve_continuous_lyapunov(G.T, -np.eye(G.shape[0]))
    P = (P+P.T)/2
    return P if np.min(np.linalg.eigvalsh(P)) > 1e-12 else None

def rand_hurwitz(rng, n):
    while True:
        G = rng.normal(0, 1, (n,n)) - 1.2*np.eye(n)
        if np.max(np.real(np.linalg.eigvals(G))) < -1e-3: return G

print("TABELA G1  e = wektor wlasny P : czy gamma||c||_2 <= sqrt(lmax(P)/p) ?")
print("  P z rownania Lapunowa G^T P + P G = -I ; e kolejne wektory wlasne P ; v0 losowe, |v0|=1")
print("  n    prob     max (gamma||c||_2) / sqrt(lmax/p)    naruszen (>1+1e-9)")
rng = np.random.default_rng(41)
for n in [2,3,4,5]:
    worst = 0.0; viol = 0; N = 0
    for _ in range(900):
        G = rand_hurwitz(rng, n); P = lyap_cert(G)
        if P is None: continue
        w, V = eigh(P)
        for idx in range(n):
            e = V[:, idx]; p = w[idx]
            cap = np.sqrt(w[-1]/p)
            for _ in range(4):
                k = int(rng.integers(1,6))
                ts = np.sort(rng.uniform(0, 12.0, k))
                ss = np.exp(rng.uniform(np.log(1e-3), np.log(40.0), k))
                v0 = rng.normal(0,1,n); v0 /= np.linalg.norm(v0)
                c,_ = protocol(G, e, P, ts, ss, v0)
                r = GAM*np.sqrt(np.sum(c*c))/cap
                N += 1
                if r > worst: worst = r
                if r > 1+1e-9: viol += 1
    print(f"  {n:<4} {N:<8} {worst:<35.9f} {viol}")

print()
print("TABELA G2  tozsamosc (gamma c)^2 = dQ tanh(gamma s/2)/p  przy P e = p e")
print("  n    pomiarow   max |lewa - prawa|   max (gamma c)^2 - dQ*tanh/p")
rng = np.random.default_rng(42)
for n in [2,3,4,5]:
    dev = 0.0; exc = -1e9; tot = 0
    for _ in range(500):
        G = rand_hurwitz(rng, n); P = lyap_cert(G)
        if P is None: continue
        w, V = eigh(P); idx = int(rng.integers(0,n)); e = V[:,idx]; p = w[idx]
        k = int(rng.integers(1,7))
        ts = np.sort(rng.uniform(0,12.0,k)); ss = np.exp(rng.uniform(np.log(1e-3),np.log(40.0),k))
        v0 = rng.normal(0,1,n); v0 /= np.linalg.norm(v0)
        c,dQ = protocol(G,e,P,ts,ss,v0)
        rhs = dQ*np.tanh(GAM*ss/2.0)/p
        dev = max(dev, np.max(np.abs((GAM*c)**2 - rhs)))
        exc = max(exc, np.max((GAM*c)**2 - rhs)); tot += k
    print(f"  {n:<4} {tot:<10} {dev:<20.3e} {exc:.3e}")

print()
print("TABELA G3  ciasnosc: czy skan dochodzi do sqrt(lmax(P)/p)? (pary obserwowalne)")
print("  G skosnie symetryczne + male tlumienie; e wektor wlasny P; optymalizacja po protokole")
rng = np.random.default_rng(43)
from scipy.optimize import minimize
for n in [2,3,4]:
    G = rand_hurwitz(rng, n); P = lyap_cert(G)
    w, V = eigh(P)
    for idx in [0, n-1]:
        e = V[:,idx]; p = w[idx]; cap = np.sqrt(w[-1]/p)
        # obserwowalnosc pary (G, e^T)
        Ob = np.vstack([e @ np.linalg.matrix_power(G,i) for i in range(n)])
        rk = np.linalg.matrix_rank(Ob, tol=1e-10)
        best = 0.0
        v0 = V[:,-1]
        for _ in range(25):
            k = 4
            x0 = np.concatenate([np.sort(rng.uniform(0,10,k)), np.full(k, 5.0)])
            f = lambda x: -GAM*np.sqrt(np.sum(protocol(G,e,P,np.sort(np.abs(x[:k])),np.abs(x[k:])+1e-9,v0)[0]**2))
            r = minimize(f, x0, method='Nelder-Mead', options={'maxiter':4000,'xatol':1e-9,'fatol':1e-12})
            best = max(best, -r.fun)
        print(f"  n={n} idx={idx}  rank(Ob)={rk}/{n}  osiagniete {best:.6f}  sufit {cap:.6f}  iloraz {best/cap:.6f}")

print()
print("TABELA G4  e NIE jest wektorem wlasnym P : czy sufit znika?")
print("  wprost: P = [[1,0.9],[0.9,1]], v = (1,-1), tlumienie 1. wspolrzednej do zera")
P4 = np.array([[1.0,0.9],[0.9,1.0]]); v = np.array([1.0,-1.0])
vp = np.array([0.0,-1.0])
print(f"  Q przed = {v @ P4 @ v:.6f}   Q po = {vp @ P4 @ vp:.6f}   dQ = {v@P4@v - vp@P4@vp:.6f}  (ujemne = pompa)")
print()
print("  protokol powtarzany, G skosnie symetryczne (obrot), e = (1,0), P jak wyzej")
print("  k        gamma||c||_2    suma dQ        Q koncowe")
Grot = np.array([[0.0,1.0],[-1.0,0.0]])
e4 = np.array([1.0,0.0])
for k in [1,2,4,16,64,256]:
    best = 0.0; bt = None
    rng4 = np.random.default_rng(44)
    for _ in range(300):
        ts = np.sort(rng4.uniform(0, 3.2*k, k)); ss = np.full(k, 3.0)
        c,dQ = protocol(Grot, e4, P4, ts, ss, np.array([1.0,0.0]))
        val = GAM*np.sqrt(np.sum(c*c))
        if val > best: best = val; bt = (np.sum(dQ),)
    # protokol regularny co pi/2 (stan wraca pod katem, przy ktorym dQ<0)
    ts = np.array([j*np.pi/2 for j in range(k)])
    c,dQ = protocol(Grot, e4, P4, ts, np.full(k,3.0), np.array([1.0,-1.0])/np.sqrt(2))
    print(f"  {k:<8} {max(best, GAM*np.sqrt(np.sum(c*c))):<15.6f} {np.sum(dQ):<14.6f} {0.0:.3f}")

print()
print("TABELA G5  brak certyfikatu: klatka Jordana [[0,1],[0,0]] (defektywna, granica stabilnosci)")
print("  jeden pomiar w chwili t, e = (1,0), v0 = (0,1)")
print("  t        |v.e|        gamma|c| przy s=20")
GJ = np.array([[0.0,1.0],[0.0,0.0]]); eJ = np.array([1.0,0.0])
for t in [1,10,100,1000,10000]:
    c,_ = protocol(GJ, eJ, np.eye(2), [float(t)], [20.0], np.array([0.0,1.0]))
    print(f"  {t:<8} {abs(c[0]/(1-np.exp(-20))):<12.1f} {abs(c[0]):.1f}")

print()
print("TABELA G6  kontrprzyklad M13: A = [[-11/10,4],[1,-41/10]]")
AM = np.array([[-11/10, 4.0],[1.0, -41/10]])
PM = lyap_cert(AM); wM, VM = eigh(PM)
print(f"  mu_2(A) = {np.max(np.linalg.eigvalsh((AM+AM.T)/2)):.10f}   (dodatnia: P=I nie jest certyfikatem)")
print(f"  wartosci wlasne P: {wM[0]:.6f}, {wM[1]:.6f}   cond(P) = {wM[1]/wM[0]:.6f}")
print("  e = wektor wlasny P   p         sufit sqrt(lmax/p)   osiagniete (skan)   iloraz")
rngM = np.random.default_rng(46)
for idx in range(2):
    e = VM[:,idx]; p = wM[idx]; cap = np.sqrt(wM[-1]/p); best = 0.0
    for _ in range(40000):
        k = int(rngM.integers(1,5))
        ts = np.sort(rngM.uniform(0,15.0,k)); ss = np.exp(rngM.uniform(np.log(1e-2),np.log(60.0),k))
        v0 = VM[:,-1] if rngM.random() < 0.5 else (lambda z: z/np.linalg.norm(z))(rngM.normal(0,1,2))
        c,_ = protocol(AM, e, PM, ts, ss, v0)
        best = max(best, GAM*np.sqrt(np.sum(c*c)))
    print(f"  idx={idx}                {p:<9.6f} {cap:<20.6f} {best:<19.6f} {best/cap:.6f}")
