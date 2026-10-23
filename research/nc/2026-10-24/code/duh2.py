import numpy as np
from scipy.linalg import expm, expm_frechet

# PREREG_DUH.md sha256 01c3634dc90b8f0355fdbc740b0f0c1b50b6484e7dccdda555f511c6218f1403
# Przebieg po diagnozie: F1 wymagal normy Frobeniusa (konwencja XH-S4), F2 wykryl moj blad
# znaku w P1, F5 obalil moje nazwanie mechanizmu. Tu wersja poprawiona + prawo luki widmowej.

fr = lambda M: np.linalg.norm(M, 'fro')
sp = lambda M: np.linalg.norm(M, 2)
def mu2(A): return np.max(np.linalg.eigvalsh((A+A.conj().T)/2))

print("TABELA K1  F1 po diagnozie: konwencja XH-S4 to norma FROBENIUSA (A = BD, E = dB D)")
D = np.array([[-2.,1,1],[1,-2,1],[1,1,-2]])
b = np.array([.15,.30,.42]); db = np.array([.01,-.018,.012])
A = np.diag(b)@D; E = np.diag(db)@D
dx = expm_frechet(A,E,compute_expm=False); nv = expm(A)@E
print(f"  ||[A,dA]||_F   = {fr(A@E-E@A):.12f}   XH = 0.040626336286   roznica = {abs(fr(A@E-E@A)-0.040626336286):.1e}")
print(f"  ||Dexp||_F     = {fr(dx):.12f}   XH = 0.032470731485   roznica = {abs(fr(dx)-0.032470731485):.1e}")
print(f"  ||blad||_F     = {fr(nv-dx):.12f}   XH = 0.013382194757   roznica = {abs(fr(nv-dx)-0.013382194757):.1e}")
print(f"  blad wzgledny  = {100*fr(nv-dx)/fr(dx):.6f}%         XH = 41.2131%")
print(f"  ta sama wielkosc w normie SPEKTRALNEJ = {100*sp(nv-dx)/sp(dx):.6f}%  (inna liczba, ta sama tresc)")

print()
print("TABELA K2  P1 po korekcie znaku:  e^A E - Dexp(A)[E] = int_0^1 (1-u) e^{(1-u)A} [A,E] e^{uA} du")
def rhs(A,E,n=6000):
    C = A@E-E@A
    u = np.linspace(0,1,n+1); w=np.ones(n+1); w[1:-1:2]=4; w[2:-1:2]=2; w=w/(3*n)
    return sum(wi*(1-ui)*(expm((1-ui)*A)@C@expm(ui*A)) for ui,wi in zip(u,w))
rng = np.random.default_rng(20261024)
kaz = [("XH-S4 3x3", A, E), ("obrot pi/2", (np.pi/2)*np.array([[0.,-1],[1,0]]), np.array([[0.,1],[1,0]]))]
for k in range(4):
    n = int(rng.integers(2,6)); kaz.append((f"losowy n={n}", rng.normal(0,.8,(n,n)), rng.normal(0,.8,(n,n))))
print("  przypadek        ||lewa - prawa||_F    ||blad||_F")
for nm,Ax,Ex in kaz:
    L = expm(Ax)@Ex - expm_frechet(Ax,Ex,compute_expm=False)
    print(f"  {nm:<16} {fr(L-rhs(Ax,Ex)):.3e}             {fr(L):.9f}")

print()
print("TABELA K3  P2 — oszacowanie ||blad|| <= (1/2)||[A,E]|| e^{mu_2(A)}; norma spektralna")
print("  n   prob   max iloraz   naruszen   (mu_2(A) XH-S4 = %.9f)" % mu2(A))
for n in [2,3,4,5,6]:
    mx=0.0; v=0; tot=0
    for _ in range(400):
        Ax = rng.normal(0,1.,(n,n)); Ex = rng.normal(0,1.,(n,n))
        c = sp(Ax@Ex-Ex@Ax)
        if c < 1e-12: continue
        tot += 1
        L = expm(Ax)@Ex - expm_frechet(Ax,Ex,compute_expm=False)
        g = 0.5*c*np.exp(max(mu2(Ax),0.0)); r = sp(L)/g
        mx = max(mx,r); v += 1 if r > 1+1e-9 else 0
    print(f"  {n}   {tot:<6} {mx:<12.9f} {v}")

print()
print("TABELA K4  P3 — rezonans 2 pi i: prawdziwa pochodna ZNIKA, naiwna nie")
Jm = np.array([[0.,-1],[1,0]]); Ew = np.array([[1.,0],[0,-1]])
print("  theta/pi   ||Dexp||_F        ||e^A E||_F   blad wzgledny")
for t in [0.5,0.9,0.99,1.0,1.01,1.5]:
    Ax = t*np.pi*Jm; d2 = expm_frechet(Ax,Ew,compute_expm=False); n2 = expm(Ax)@Ew
    rel = fr(n2-d2)/fr(d2) if fr(d2) > 1e-14 else float('inf')
    print(f"  {t:<10.2f} {fr(d2):<17.3e} {fr(n2):<13.9f} "
          f"{'NIESKONCZONY' if rel==float('inf') else f'{100*rel:.3f}%'}")

print()
print("TABELA K5  F5 obalony jak postawiony — PRAWO LUKI WIDMOWEJ dla A samosprzezonego")
print("  w bazie wlasnej: (e^A E)_ij / Dexp_ij = (l_i - l_j)/(1 - e^{l_j - l_i}) -> d dla duzego d")
print("  wiec blad wzgledny rosnie LINIOWO z luka widmowa; rezonans NIE jest potrzebny")
print("  d      iloraz wzor d/(1-e^{-d})   zmierzony iloraz   roznica")
for d in [0.5,1.,2.,4.,8.,16.,32.]:
    A2 = np.diag([d,0.]); E2 = np.array([[0.,0.],[1.,0.]])   # wpis (2,1): l_i=0, l_j=d
    d2 = expm_frechet(A2,E2,compute_expm=False); n2 = expm(A2)@E2
    zm = fr(n2)/fr(d2)
    wz = d/(np.exp(d)-1)*np.exp(0) if False else abs(0-d)/abs(1-np.exp(d-0))
    print(f"  {d:<6.1f} {d/(1-np.exp(d)) if False else abs(d/(1-np.exp(d))):<23.9f} {zm:<18.9f} "
          f"{abs(abs(d/(1-np.exp(d)))-zm):.2e}")
print("  (wpis (2,1): l_i = 0, l_j = d, iloraz = |d/(1-e^{d})| -> 0; wpis (1,2) daje -> d)")
print()
print("  d      wpis (1,2): wzor d/(1-e^{-d})   zmierzony   roznica")
for d in [0.5,1.,2.,4.,8.,16.,32.]:
    A2 = np.diag([d,0.]); E2 = np.array([[0.,1.],[0.,0.]])   # wpis (1,2): l_i=d, l_j=0
    d2 = expm_frechet(A2,E2,compute_expm=False); n2 = expm(A2)@E2
    zm = fr(n2)/fr(d2); wz = d/(1-np.exp(-d))
    print(f"  {d:<6.1f} {wz:<28.9f} {zm:<11.9f} {abs(wz-zm):.2e}")
