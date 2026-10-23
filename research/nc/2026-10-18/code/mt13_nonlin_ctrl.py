import numpy as np
from scipy.optimize import brentq

# KONTROLA do mt13_nonlin.py (7e751c7b64c063bc65b8192becfa4d97de732f01d0ef0c6cb14e8244d36d9545).
# Tam rozrzut X(T) przy lambda = 0 wynosil 1.3e-4 i malal jak O(h) (iloraz 0.2500 przy h -> h/4),
# a bilans masy pekal o 1e-3. Podejrzenie: zrodlo prostokatne ma nieciaglosc na krawedzi,
# wiec RK4 jest tam pierwszego, nie czwartego rzedu. Test: to samo na zrodle C^1
# (podniesiony cosinus o tej samej calce). Jesli rozrzut spadnie do rzedu maszynowego,
# rozrzut z poprzedniego przebiegu byl artefaktem kwadratury, a teza przy lambda = 0 jest exact.

T, G0, KAP = 2.0, 2.0, 0.1
A, D = [0.0, 0.7, 1.4], 0.1
n0, X0 = 0.0, 0.1

def Sfun(t, wag):
    s = 0.0
    for a, wg in zip(A, wag):
        if a <= t <= a+D:
            s += (wg/D)*(1.0-np.cos(2.0*np.pi*(t-a)/D))
    return s

def integruj(wag, beta, lam, N):
    h = T/N
    n, X, I, J = n0, X0, 0.0, 0.0
    def f(t, n, X):
        Gam = G0*(1.0+beta*n)*n
        S = Sfun(t, wag)
        return (S - Gam, -lam*X + KAP*Gam, Gam, S)
    for i in range(N):
        t = i*h
        k1 = f(t, n, X); k2 = f(t+h/2, n+h/2*k1[0], X+h/2*k1[1])
        k3 = f(t+h/2, n+h/2*k2[0], X+h/2*k2[1]); k4 = f(t+h, n+h*k3[0], X+h*k3[1])
        n += h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        X += h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        I += h/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
        J += h/6*(k1[3]+2*k2[3]+2*k3[3]+k4[3])
    return n, X, I, J

def wagi(th, rho): return np.array([1.0+th, 1.0-th+rho, 1.0-rho])

def rodzina(beta, lam, N, thetas):
    nt = integruj(wagi(0.0, 0.0), beta, lam, N)[0]
    out = []
    for th in thetas:
        g = lambda r: integruj(wagi(th, r), beta, lam, N)[0] - nt
        r = brentq(g, -0.9, 0.9, xtol=1e-14, rtol=1e-15)
        wg = wagi(th, r)
        if np.any(wg < 0): continue
        nT, XT, I, J = integruj(wg, beta, lam, N)
        out.append((th, r, wg, nT, XT, I, J))
    return out

THS = [-0.4, -0.2, 0.0, 0.2, 0.4]
print("TABELA C1  zrodlo C^1; rodzina o ustalonych int S = 3 i ustalonym n(T); N = 2000")
print("  beta   lambda   theta    n(T)             X(T)                int S numerycznie")
pak = {}
for beta in [0.0, 1.5]:
    for lam in [0.0, 1.0]:
        r = rodzina(beta, lam, 2000, THS); pak[(beta, lam)] = r
        for th, rho, wg, nT, XT, I, J in r:
            print(f"  {beta:<6.1f} {lam:<8.1f} {th:<+8.2f} {nT:.12f}  {XT:.15f}  {J:.14f}")

print()
print("TABELA C2  rozrzut X(T) na rodzinie przy zrodle C^1")
print("  beta   lambda   max-min X(T) @ h=1e-3    max-min X(T) @ h=2.5e-4    iloraz")
for beta in [0.0, 1.5]:
    for lam in [0.0, 1.0]:
        a = pak[(beta, lam)]; b = rodzina(beta, lam, 8000, THS)
        da = max(x[4] for x in a) - min(x[4] for x in a)
        db = max(x[4] for x in b) - min(x[4] for x in b)
        print(f"  {beta:<6.1f} {lam:<8.1f} {da:<24.3e} {db:<26.3e} "
              f"{(db/da if da>0 else float('nan')):.4f}")

print()
print("TABELA C3  bilans masy przy zrodle C^1:  int Gamma  wobec  int S - n(T) + n(0)")
print("  beta   theta    int Gamma          int S - n(T)       roznica")
for beta in [0.0, 1.5]:
    for th, rho, wg, nT, XT, I, J in pak[(beta, 0.0)]:
        print(f"  {beta:<6.1f} {th:<+8.2f} {I:<18.14f} {J-nT+n0:<18.14f} {abs(I-(J-nT+n0)):.2e}")
