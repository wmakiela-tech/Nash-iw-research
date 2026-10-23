import numpy as np
from scipy.optimize import brentq

# PREREG_MT13_NONLIN.md sha256 58209d2b3233bc8147b371fb2b448eb38f304bd63fee4ff78ea6b0da4a7a0b9b
# Pytanie otwarte MT13: czy twierdzenie o rownych plonach przezywa ubytek zalezny od stanu.
# H1: w in span{1,q} dokladnie dla lambda = 0.
# H2: przy lambda = 0 i stalym kappa teza przezywa dowolne Gamma(t,n).
# H3: przy lambda > 0 plon sie zmienia takze przy beta > 0.

T, G0, KAP = 2.0, 2.0, 0.1
A, D = [0.0, 0.7, 1.4], 0.1
n0, X0 = 0.0, 0.1

# ---------- H1: odleglosc w od span{1,q} w L^2([0,T]) ----------
print("TABELA H1a  odleglosc w od span{1,q} w L^2([0,T]);  gamma =", G0)
print("  lambda     ||w - P w|| / ||w||        det[1,q,w] na wezlach MT13")
sg = np.linspace(0.0, T, 20001)          # sigma = T - s
qg = np.exp(-G0*sg)
def Q(r, a):
    return np.exp(-r*(T-a))*(np.exp(r*D)-1.0)/(r*D) if r > 0 else 1.0
for lam in [0.0, 0.25, 0.5, 1.0, 1.9, 2.0, 2.1, 3.0, 5.0]:
    if abs(lam-G0) < 1e-12:
        wg = KAP*G0*sg*np.exp(-G0*sg)
    elif lam == 0.0:
        wg = KAP*(1.0-np.exp(-G0*sg))
    else:
        wg = KAP*G0*(np.exp(-lam*sg)-np.exp(-G0*sg))/(G0-lam)
    M = np.column_stack([np.ones_like(sg), qg])
    res = wg - M @ np.linalg.lstsq(M, wg, rcond=None)[0]
    rel = np.sqrt(np.sum(res**2))/np.sqrt(np.sum(wg**2))
    q3 = np.array([Q(G0, a) for a in A])
    if lam == 0.0:
        w3 = np.array([KAP*(1.0-Q(G0, a)) for a in A])
    elif abs(lam-G0) < 1e-12:
        w3 = np.array([KAP*G0*(T-a-D/2)*np.exp(-G0*(T-a-D/2)) for a in A])
    else:
        w3 = np.array([KAP*G0/(G0-lam)*(Q(lam, a)-Q(G0, a)) for a in A])
    det3 = np.linalg.det(np.column_stack([np.ones(3), q3, w3]))
    print(f"  {lam:<10.2f} {rel:<28.3e} {det3:+.6e}")

# ---------- calkowanie ODE z ubytkiem Gamma(t,n) = G0 (1 + beta n) n ----------
def Sfun(t, wag):
    s = 0.0
    for a, wg in zip(A, wag):
        if a <= t < a+D: s += wg/D
    return s

def integruj(wag, beta, lam, N):
    h = T/N
    n, X, I = n0, X0, 0.0
    def f(t, n, X):
        Gam = G0*(1.0+beta*n)*n
        return (Sfun(t, wag) - Gam, -lam*X + KAP*Gam, Gam)
    for i in range(N):
        t = i*h
        k1 = f(t, n, X); k2 = f(t+h/2, n+h/2*k1[0], X+h/2*k1[1])
        k3 = f(t+h/2, n+h/2*k2[0], X+h/2*k2[1]); k4 = f(t+h, n+h*k3[0], X+h*k3[1])
        n += h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        X += h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        I += h/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
    return n, X, I

def wagi(th, rho):
    return np.array([1.0+th, 1.0-th+rho, 1.0-rho])

def rodzina(beta, lam, N, thetas):
    nt = integruj(wagi(0.0, 0.0), beta, lam, N)[0]
    out = []
    for th in thetas:
        g = lambda r: integruj(wagi(th, r), beta, lam, N)[0] - nt
        lo, hi = -0.9, 0.9
        while g(lo)*g(hi) > 0 and hi < 3.0:
            lo, hi = lo*1.5, hi*1.5
        if g(lo)*g(hi) > 0: continue
        r = brentq(g, lo, hi, xtol=1e-14, rtol=1e-15)
        wg = wagi(th, r)
        if np.any(wg < 0): continue
        nT, XT, I = integruj(wg, beta, lam, N)
        out.append((th, r, wg, nT, XT, I))
    return out

THS = [-0.4, -0.2, 0.0, 0.2, 0.4]
print()
print("TABELA H2  rodzina o ustalonych int S = 3 i ustalonym n(T);  N = 2000 (h = 1e-3)")
print("  beta   lambda   theta    rho           wagi S (wszystkie >= 0)        n(T)             X(T)")
pak = {}
for beta in [0.0, 1.5]:
    for lam in [0.0, 1.0]:
        r = rodzina(beta, lam, 2000, THS)
        pak[(beta, lam)] = r
        for th, rho, wg, nT, XT, I in r:
            print(f"  {beta:<6.1f} {lam:<8.1f} {th:<+8.2f} {rho:<+13.9f} "
                  f"[{wg[0]:.6f} {wg[1]:.6f} {wg[2]:.6f}]  {nT:.12f}  {XT:.12f}")

print()
print("TABELA H3  rozrzut X(T) na rodzinie i jego zachowanie przy zageszczeniu kroku")
print("  beta   lambda   max-min X(T) @ h=1e-3    max-min X(T) @ h=2.5e-4    iloraz")
for beta in [0.0, 1.5]:
    for lam in [0.0, 1.0]:
        a = pak[(beta, lam)]
        b = rodzina(beta, lam, 8000, THS)
        da = max(x[4] for x in a) - min(x[4] for x in a)
        db = max(x[4] for x in b) - min(x[4] for x in b)
        il = db/da if da > 0 else float('nan')
        print(f"  {beta:<6.1f} {lam:<8.1f} {da:<24.3e} {db:<26.3e} {il:.4f}")

print()
print("TABELA H2b  kontrola bilansu masy: int Gamma  wobec  int S - n(T) + n(0)")
print("  beta   lambda   theta    int Gamma         int S - n(T)      roznica      X(T) - X0 - kappa*intGamma")
for beta in [0.0, 1.5]:
    for lam in [0.0]:
        for th, rho, wg, nT, XT, I in pak[(beta, lam)]:
            bal = wg.sum() - nT + n0
            print(f"  {beta:<6.1f} {lam:<8.1f} {th:<+8.2f} {I:<17.12f} {bal:<17.12f} "
                  f"{abs(I-bal):<12.2e} {abs(XT-X0-KAP*I):.2e}")
