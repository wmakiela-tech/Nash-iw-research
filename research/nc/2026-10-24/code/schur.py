import numpy as np
from scipy.optimize import minimize

# PREREG_SCHUR.md sha256 5ffd8d686f0a62545c43ec0bd5c010af44ab88d050271a558fbbb37b33c0df7c
# Domkniecie NC-OPN-017: sup ||J_coll||/||J|| = norma mnoznika Schura maski pozadiagonalnej.
nrm = lambda M: np.linalg.norm(M, 2)
rng = np.random.default_rng(20261024)

print("TABELA S1  F3/P2 — realizowalnosc: pelna konstrukcja A, B, h, J wobec offdiag")
print("  sigma(A) = sigma(B) = {0..n-1}, h = cos(2 pi lambda) -> h == 1, hipoteza dla KAZDEGO J")
print("  n   ||J h(A) - h(B) J||   ||J_coll|| (z konstrukcji)   ||offdiag(J)||   roznica")
for n in [2,3,4,6]:
    la = np.arange(n, dtype=float); mu = np.arange(n, dtype=float)
    h = lambda x: np.cos(2*np.pi*np.asarray(x))
    J = rng.normal(0,1,(n,n))
    hip = nrm(J@np.diag(h(la)) - np.diag(h(mu))@J)
    coll = J.copy()
    for j in range(n):
        for i in range(n):
            if abs(mu[j]-la[i]) <= 1e-12: coll[j,i] = 0.0   # para dopasowana wypada
    print(f"  {n}   {hip:<21.3e} {nrm(coll):<28.12f} {nrm(J-np.diag(np.diag(J))):<16.12f} "
          f"{abs(nrm(coll)-nrm(J-np.diag(np.diag(J)))):.2e}")

print()
print("TABELA S2  F1/P3 — jawny swiadek X = (a-b)I + b*ones, t = a-b = -b n/2")
print("  n    ||X||          ||X - diag X||   iloraz           wzor 2 - 2/n    roznica")
for n in [2,3,4,6,8,16,32,64]:
    b = 1.0; t = -b*n/2
    X = t*np.eye(n) + b*np.ones((n,n))
    r = nrm(X-np.diag(np.diag(X)))/nrm(X)
    wz = 2-2/n
    print(f"  {n:<4} {nrm(X):<14.9f} {nrm(X-np.diag(np.diag(X))):<16.9f} {r:<16.12f} {wz:<15.12f} {abs(r-wz):.2e}")

print()
print("TABELA S3  F2/F4/F5 — czy cokolwiek przekracza swiadka; losowe vs optymalizacja")
print("  n    max iloraz LOSOWY   max iloraz OPTYM.   swiadek 2-2/n   przekroczen swiadka   > 2")
for n in [2,3,4,5,6,8]:
    mxr = 0.0
    for _ in range(4000):
        X = rng.normal(0,1,(n,n))
        if nrm(X) < 1e-12: continue
        mxr = max(mxr, nrm(X-np.diag(np.diag(X)))/nrm(X))
    def neg(v):
        X = v.reshape(n,n)
        q = nrm(X)
        return 0.0 if q < 1e-12 else -nrm(X-np.diag(np.diag(X)))/q
    mxo = 0.0
    for _ in range(30):
        x0 = rng.normal(0,1,n*n)
        r = minimize(neg, x0, method="Nelder-Mead",
                     options={"maxiter":40000,"maxfev":40000,"xatol":1e-10,"fatol":1e-13})
        mxo = max(mxo, -r.fun)
    wz = 2-2/n
    print(f"  {n:<4} {mxr:<19.12f} {mxo:<19.12f} {wz:<15.12f} "
          f"{'TAK' if mxo > wz+1e-7 else 'nie':<21} {'TAK' if mxo > 2+1e-9 else 'nie'}")

print()
print("TABELA S4  F4/P5 — korekta mojego raportowania z ART020 par.7")
print("  tamta liczba 1.097 pochodzila z LOSOWYCH J; swiadek przy tym samym n daje wiecej")
print("  n    losowy max (4000 prob)   swiadek 2-2/n   iloraz swiadek/losowy")
for n in [2,3,4,6,8]:
    mxr = 0.0
    for _ in range(4000):
        X = rng.normal(0,1,(n,n))
        if nrm(X) < 1e-12: continue
        mxr = max(mxr, nrm(X-np.diag(np.diag(X)))/nrm(X))
    wz = 2-2/n
    print(f"  {n:<4} {mxr:<24.9f} {wz:<15.9f} {wz/mxr:.6f}")
print()
print("  dla porownania: w ART020 par.7 zamiatalem losowe J z WZORCEM dopasowan losowym,")
print("  czyli czesciowa permutacja, a nie pelna przekatna — to osobny powod, dla ktorego")
print("  1.097 nie bylo oszacowaniem supremum")
