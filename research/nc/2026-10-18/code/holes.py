import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm

# PROPONOWANI SWIADKOWIE dla trzech dziur z audytu 005.
# Tabele bez tekstu interpretacyjnego; odczyty dopisane po fakcie.

# =====================================================================
# DZIURA §1.10: "Nie wystarczy domagac sie analitycznosci tylko dla t>0"
# Swiadek: miara ZNAKOWANA o WSZYSTKICH momentach zerowych (nieoznaczonosc
# problemu moment. Stieltjesa, przyklad lognormalny), realizowana jako B e^{tD} C
# z D = mnozenie przez -lambda na L^2(0,inf).
#   g(x) = f(x) sin(2 pi ln x),  f = gestosc lognormalna
#   c(x) = |g|^{1/2},  b(x) = sgn(g)|g|^{1/2}  ->  b c = g,  oba w L^2 bo int|g|<inf
#   K(t) = int e^{-x t} g(x) dx   (transformata Laplace'a, ANALITYCZNA dla Re t>0)
#   B D^k C = (-1)^k int x^k g(x) dx = 0  dla kazdego k
# =====================================================================
f  = lambda x: np.exp(-(np.log(x))**2/2)/(x*np.sqrt(2*np.pi))
g  = lambda x: f(x)*np.sin(2*np.pi*np.log(x))

print("TABELA H1  momenty miary znakowanej g, int x^k g(x) dx   (przewidywane 0)")
print("  k    int x^k g dx        int x^k |g| dx (skala odniesienia)   iloraz")
for k in range(6):
    m  = quad(lambda x: x**k*g(x), 0, np.inf, limit=600, epsabs=1e-14, epsrel=1e-13)[0]
    ma = quad(lambda x: x**k*abs(g(x)), 0, np.inf, limit=600, epsabs=1e-14, epsrel=1e-13)[0]
    print(f"  {k}    {m:<19.9e} {ma:<34.9e} {abs(m)/ma:.3e}")

print()
print("TABELA H2  K(t) = int e^{-xt} g(x) dx   (przewidywane: NIEZEROWE)")
print("  t       K(t)                 int e^{-xt}|g| dx        iloraz")
for t in [0.25,0.5,1.0,2.0,4.0,8.0]:
    K  = quad(lambda x: np.exp(-x*t)*g(x), 0, np.inf, limit=600, epsabs=1e-16, epsrel=1e-13)[0]
    Ka = quad(lambda x: np.exp(-x*t)*abs(g(x)), 0, np.inf, limit=600, epsabs=1e-16, epsrel=1e-13)[0]
    print(f"  {t:<7.2f} {K:<20.9e} {Ka:<24.9e} {abs(K)/Ka:.3e}")

print()
print("TABELA H3  ograniczonosc B i C: ||c||_2^2 = ||b||_2^2 = int |g| dx")
nrm = quad(lambda x: abs(g(x)), 0, np.inf, limit=600)[0]
print(f"  int |g| dx = {nrm:.9f}   ||B|| = ||C|| = {np.sqrt(nrm):.9f}")
print(f"  int x^{{2k}} |g| dx dla k=1..4 (dziedzina D^k):")
for k in range(1,5):
    print(f"    k={k}: {quad(lambda x: x**(2*k)*abs(g(x)),0,np.inf,limit=600)[0]:.6e}")

# =====================================================================
# DZIURA §7.8: splatanie spektralne NIE daje splatania lancuchowego
# Swiadek: jeden kompleks dwustopniowy, d = diag(1,2), wiec Delta^0 = Delta^1 = diag(1,4)
# o widmie prostym. J_k przemienne z f(Delta) <=> J_k diagonalne.
# Biore J_0 = diag(1,1), J_1 = diag(1,2): splatanie spektralne zachodzi w obu
# stopniach dla KAZDEJ ograniczonej funkcji borelowskiej, a d J_0 != J_1 d.
# =====================================================================
print()
print("TABELA H4  splatanie spektralne a lancuchowe")
d  = np.diag([1.,2.])
D0 = d.T@d; D1 = d@d.T
J0 = np.diag([1.,1.]); J1 = np.diag([1.,2.])
print(f"  Delta^0 = {np.diag(D0).tolist()}   Delta^1 = {np.diag(D1).tolist()}")
rng = np.random.default_rng(5)
worst = 0.0
for _ in range(2000):
    v = rng.normal(size=2)                      # dowolny ograniczony mnoznik borelowski
    fD0 = np.diag(v); fD1 = np.diag(v)          # f(Delta) na widmie {1,4}
    worst = max(worst, np.linalg.norm(J0@fD0-fD0@J0,2), np.linalg.norm(J1@fD1-fD1@J1,2))
print(f"  max defekt splatania spektralnego po 2000 losowych mnoznikach: {worst:.3e}")
print(f"  d J_0      = {np.diag(d@J0).tolist()}")
print(f"  J_1 d      = {np.diag(J1@d).tolist()}")
print(f"  ||d J_0 - J_1 d|| = {np.linalg.norm(d@J0-J1@d,2):.6f}")

# =====================================================================
# DZIURA §3.10: rowne zbiory mozliwych trajektorii, rozne prawa na historiach
# Swiadek: dwa lancuchy Markowa na {0,1}, oba o PELNYM nosniku na {0,1}^n,
# rozna odleglosc calkowitego wahania miedzy prawami historii.
# =====================================================================
print()
print("TABELA H5  ten sam nosnik trajektorii, rozne prawa historii")
P1 = np.array([[.5,.5],[.5,.5]]); P2 = np.array([[2/3,1/3],[1/3,2/3]])
def law(P,n):
    pi = np.array([.5,.5]); out={}
    def rec(path,p):
        if len(path)==n+1: out[tuple(path)]=p; return
        for s in (0,1): rec(path+[s], p*P[path[-1],s])
    for s0 in (0,1): rec([s0], pi[s0])
    return out
print("  n   #trajektorii  min p (uklad 1)  min p (uklad 2)   TV(prawo1, prawo2)")
for n in [1,2,4,6,8,10]:
    L1=law(P1,n); L2=law(P2,n)
    assert set(L1)==set(L2)
    tv=0.5*sum(abs(L1[k]-L2[k]) for k in L1)
    print(f"  {n:<3} {len(L1):<13} {min(L1.values()):<16.3e} {min(L2.values()):<17.3e} {tv:.6f}")

# =====================================================================
# DZIURA §1.7: minimalizacja jadra przez (D,C,tau B) nie daje minimalnosci
# zamknietej odpowiedzi x0 -> tau x(t), bo uczestniczy takze A.
# Swiadek: X=R^2, Y=R^2, tau=(1,0). Mod ukryty nr 1 jest NIEWIDOCZNY w tau B,
# wiec minimalizacja po (D,C,tau B) go usuwa; ale wchodzi do x_2 przez B i wraca
# do x_1 przez A, wiec zmienia tau x(t).
# =====================================================================
print()
print("TABELA H6  redukcja jadra wzgledem celu usuwa mod, ktory cel widzi przez A")
A  = np.array([[0.,1.],[0.,0.]])          # x2 -> x1
B  = np.array([[0.,0.],[1.,0.]])          # mod ukryty 1 -> x2 ; tau B = (0,0)
C  = np.array([[1.,0.],[0.,0.]])          # x1 wzbudza mod 1
Dh = np.diag([-0.3,-5.0])
tau= np.array([[1.,0.]])
print(f"  tau B = {(tau@B).tolist()}   czyli mod 1 niewidoczny w jadrze wazonym celem")
print("  k    tau B D^k C (jadro wazone celem)")
M=np.eye(2)
for k in range(4):
    print(f"  {k}    {np.round(tau@B@M@C,12).tolist()}")
    M=M@Dh
L  = np.block([[A,B],[C,Dh]])
Lr = np.block([[A,np.zeros((2,2))],[np.zeros((2,2)),Dh]])   # po usunieciu sprzezenia B
x0 = np.array([1.,0.,0.,0.])
print()
print("  t      tau x(t) pelne        tau x(t) po redukcji   roznica")
for t in [0.5,1.0,2.0,4.0]:
    full=(expm(t*L)@x0)[0]; red=(expm(t*Lr)@x0)[0]
    print(f"  {t:<6.2f} {full:<21.12f} {red:<22.12f} {abs(full-red):.3e}")
