import numpy as np
from scipy.linalg import expm, expm_frechet

# PREREG_DUH.md sha256 01c3634dc90b8f0355fdbc740b0f0c1b50b6484e7dccdda555f511c6218f1403
# Wsparcie XH-S4 Q64. Pytanie i konstrukcja 3x3 naleza do XH-S4 (obrot 024).

def dexp_quad(A, E, n=4000):
    """Dexp(A)[E] = int_0^1 e^{sA} E e^{(1-s)A} ds — niezalezna kwadratura (Simpson)"""
    s = np.linspace(0, 1, n+1)
    w = np.ones(n+1); w[1:-1:2] = 4; w[2:-1:2] = 2; w = w/(3*n)
    out = np.zeros_like(A, dtype=complex)
    for si, wi in zip(s, w):
        out += wi*(expm(si*A) @ E @ expm((1-si)*A))
    return out

def err_quad(A, E, n=4000):
    """prawa strona P1: int_0^1 (1-u) e^{(1-u)A} [E,A] e^{uA} du"""
    C = E@A - A@E
    u = np.linspace(0, 1, n+1)
    w = np.ones(n+1); w[1:-1:2] = 4; w[2:-1:2] = 2; w = w/(3*n)
    out = np.zeros_like(A, dtype=complex)
    for ui, wi in zip(u, w):
        out += wi*(1-ui)*(expm((1-ui)*A) @ C @ expm(ui*A))
    return out

def mu2(A): return np.max(np.linalg.eigvalsh((A+A.conj().T)/2))
nrm = lambda M: np.linalg.norm(M, 2)

D = np.array([[-2.,1,1],[1,-2,1],[1,1,-2]])
print("TABELA D1  F1 — czy ODTWARZAM piec liczb XH-S4 (ich dane, ich konstrukcja)")
b = np.array([.15,.30,.42]); db = np.array([.01,-.018,.012])
A = np.diag(b)@D; E = np.diag(db)@D
dexp = expm_frechet(A, E, compute_expm=False)
naive = expm(A)@E
print(f"  ||[A,dA]||          = {nrm(A@E-E@A):.12f}   XH = 0.040626336286")
print(f"  ||Dexp(A)[dA]||     = {nrm(dexp):.12f}   XH = 0.032470731485")
print(f"  ||exp(A)dA - Dexp|| = {nrm(naive-dexp):.12f}   XH = 0.013382194757")
print(f"  blad wzgledny       = {100*nrm(naive-dexp)/nrm(dexp):.6f}%        XH = 41.2131%")
tau = 1e-6
fd = (expm(A+tau*E)-expm(A-tau*E))/(2*tau)
print(f"  ||fd - Dexp||       = {nrm(fd-dexp):.6e}      XH = 6.10379249e-11")
b0 = .2*np.ones(3); db0 = .015*np.ones(3)
A0 = np.diag(b0)@D; E0 = np.diag(db0)@D
print(f"  kontrola przemienna: ||[A,dA]|| = {nrm(A0@E0-E0@A0):.3e}   "
      f"blad naiwny = {nrm(expm(A0)@E0-expm_frechet(A0,E0,compute_expm=False)):.3e}   XH ~ 6.5e-18")

print()
print("TABELA D2  F2 — dokladna tozsamosc P1: blad = int_0^1 (1-u) e^{(1-u)A}[E,A]e^{uA} du")
print("  przypadek                 ||lewa - prawa||     ||blad||")
rng = np.random.default_rng(20261024)
kazusy = [("XH-S4 3x3", A, E)]
for k in range(4):
    n = rng.integers(2, 6)
    kazusy.append((f"losowy n={n} #{k+1}", rng.normal(0,.8,(n,n)), rng.normal(0,.8,(n,n))))
kazusy.append(("obrot pi/2", (np.pi/2)*np.array([[0.,-1],[1,0]]), np.array([[0.,1],[1,0]])))
for nazwa, Ax, Ex in kazusy:
    L = expm(Ax)@Ex - expm_frechet(Ax, Ex, compute_expm=False)
    R = err_quad(Ax, Ex)
    print(f"  {nazwa:<25} {nrm(L-R):.3e}            {nrm(L):.9f}")

print()
print("TABELA D3  F3 — oszacowanie P2: ||blad|| <= (1/2)||[A,E]|| e^{mu_2(A)}")
print(f"  mu_2(A) dla A = BD z XH-S4 = {mu2(A):.12f}")
print("  przypadek                 mu_2(A)      ||blad||      granica      iloraz   trzyma")
viol = 0
for nazwa, Ax, Ex in kazusy:
    L = expm(Ax)@Ex - expm_frechet(Ax, Ex, compute_expm=False)
    g = 0.5*nrm(Ax@Ex-Ex@Ax)*np.exp(max(mu2(Ax), 0.0)) if mu2(Ax) > 0 else 0.5*nrm(Ax@Ex-Ex@Ax)
    ok = nrm(L) <= g + 1e-9
    viol += 0 if ok else 1
    print(f"  {nazwa:<25} {mu2(Ax):<12.6f} {nrm(L):<13.9f} {g:<12.9f} {nrm(L)/g if g>0 else float('nan'):<8.4f} {'TAK' if ok else 'NIE'}")
print(f"  naruszen F3 = {viol}")
print("  zamiatanie losowe:")
print("  n   prob   max iloraz ||blad||/granica   naruszen")
for n in [2,3,4,5,6]:
    mx = 0.0; v = 0; tot = 0
    for _ in range(400):
        Ax = rng.normal(0,1.0,(n,n)); Ex = rng.normal(0,1.0,(n,n))
        L = expm(Ax)@Ex - expm_frechet(Ax, Ex, compute_expm=False)
        c = nrm(Ax@Ex-Ex@Ax)
        if c < 1e-12: continue
        tot += 1
        g = 0.5*c*np.exp(max(mu2(Ax), 0.0))
        r = nrm(L)/g
        mx = max(mx, r)
        if r > 1+1e-9: v += 1
    print(f"  {n}   {tot:<6} {mx:<29.9f} {v}")

print()
print("TABELA D4  F4/P3 — rezonans: prawdziwa pochodna ZNIKA, naiwna NIE")
print("  A = theta*[[0,-1],[1,0]], wartosci wlasne +-i*theta; Dexp singularna przy theta = pi")
Jm = np.array([[0.,-1],[1,0]])
Ew = np.array([[1.,0],[0,-1]])          # skladowa pozadiagonalna w bazie wlasnej J
print("  theta/pi   ||Dexp(A)[E]||     ||exp(A)E||    ||blad||       blad wzgledny")
for t in [0.5, 0.9, 0.99, 0.999, 1.0, 1.001, 1.5]:
    Ax = t*np.pi*Jm
    dx = expm_frechet(Ax, Ew, compute_expm=False)
    nv = expm(Ax)@Ew
    rel = nrm(nv-dx)/nrm(dx) if nrm(dx) > 1e-14 else float('inf')
    print(f"  {t:<10.3f} {nrm(dx):<18.3e} {nrm(nv):<14.9f} {nrm(nv-dx):<14.9f} "
          f"{'nieskonczony' if rel == float('inf') else f'{100*rel:.3f}%'}")
print(f"  przy theta = pi:  wartosci wlasne A = {np.round(np.linalg.eigvals(np.pi*Jm),9).tolist()}")
print(f"                    roznica wl. = {np.diff(np.linalg.eigvals(np.pi*Jm))[0]:.9f}  (ma byc ~ -2 pi i)")

print()
print("TABELA D5  F5 — czy dla A o widmie RZECZYWISTYM blad wzgledny pozostaje skonczony")
print("  n   prob   max blad wzgledny (%)   max ||[A,E]||")
for n in [2,3,4,6]:
    mx = 0.0; mc = 0.0; tot = 0
    for _ in range(400):
        S = rng.normal(0,1.2,(n,n)); Ax = (S+S.T)/2          # symetryczne -> widmo rzeczywiste
        Ex = rng.normal(0,1.2,(n,n))
        dx = expm_frechet(Ax, Ex, compute_expm=False)
        if nrm(dx) < 1e-12: continue
        tot += 1
        r = 100*nrm(expm(Ax)@Ex-dx)/nrm(dx)
        mx = max(mx, r); mc = max(mc, nrm(Ax@Ex-Ex@Ax))
    print(f"  {n}   {tot:<6} {mx:<23.6f} {mc:.6f}")
