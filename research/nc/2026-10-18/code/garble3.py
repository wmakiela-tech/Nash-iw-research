import numpy as np
from fractions import Fraction as F

# SWIADEK DLA par.2.8 — KONSTRUKCJA JAWNA, WYMIERNA
# poprzedza: garble.py  5924cdbcd6d077f699d1841b5274b43f4870081cedf194b612a1337c20b9e2c5 (odrzucony: dzialal przez slad)
#            garble2.py fefb47e8236358ef173624805697bebb646528430d5687cfa240e2a65ca5a154 (szukanie numeryczne, zle uwarunkowane, pusty wynik)
#
# ALGEBRA. P = I - n n^T, n = (1,1,1)/sqrt(3). Dla rho hermitowskiej 3x3:
#   (P rho P)_kk = rho_kk - (2/3) Re r_k + S/9,   r_k = suma k-tego wiersza, S = suma wszystkich
#   tr(P rho P)  = 1 - S/3
# Przezycie zalezy WYLACZNIE od S. Diagonala po postselekcji zalezy od poszczegolnych Re r_k.
# Wystarczy wiec para o tej samej diagonali i tym samym S, lecz innym ROZKLADZIE koherencji.
#
# Z d = (1/2, 3/10, 1/5) i rzeczywistymi koherencjami a = Re rho_01, b = Re rho_02, c = Re rho_12:
#   u_0 = a+b, u_1 = a+c, u_2 = b+c,  S = 1 + 2(a+b+c)
# Para:  rho1: (a,b,c) = (t,0,0)      rho2: (a,b,c) = (0,0,t)
# To samo S (bo ta sama suma a+b+c), rozne u_k. Dodatnia okreslonosc: t <= sqrt(6)/10 dla rho2.

t = F(1,5)
d = [F(1,2), F(3,10), F(1,5)]

def mk(a, b, c):
    return np.array([[float(d[0]), float(a), float(b)],
                     [float(a), float(d[1]), float(c)],
                     [float(b), float(c), float(d[2])]], dtype=float)

R1 = mk(t, 0, 0)
R2 = mk(0, 0, t)
n = np.ones(3)/np.sqrt(3)
P = np.eye(3) - np.outer(n, n)

def post(R, PP=P):
    S = PP @ R @ PP; tr = np.trace(S)
    return tr, np.diag(S)/tr

print("TABELA X1  para jawna, wspolczynniki wymierne, t = 1/5")
for nm, R in [("rho1", R1), ("rho2", R2)]:
    print(f"  {nm} = [[{R[0,0]:.1f}, {R[0,1]:.1f}, {R[0,2]:.1f}], [{R[1,0]:.1f}, {R[1,1]:.1f}, {R[1,2]:.1f}], [{R[2,0]:.1f}, {R[2,1]:.1f}, {R[2,2]:.1f}]]")
print("  wartosci wlasne (musza byc >= 0):")
for nm, R in [("rho1", R1), ("rho2", R2)]:
    ev = np.linalg.eigvalsh(R)
    print(f"  {nm}  " + "  ".join(f"{v:+.9f}" for v in ev) + f"   lambda_min = {ev.min():+.9f}   slad = {np.trace(R):.9f}")

print()
print("TABELA X2  warunek (a): IDENTYCZNA diagonala -> nierozroznialne przez kazdy garbling")
print("  stan    p(0)         p(1)         p(2)")
for nm, R in [("rho1", R1), ("rho2", R2)]:
    print(f"  {nm}    " + "  ".join(f"{v:.9f}" for v in np.diag(R)))
print(f"  max |roznica| = {np.max(np.abs(np.diag(R1)-np.diag(R2))):.3e}")

print()
print("TABELA X3  warunek (b): IDENTYCZNE prawdopodobienstwo przezycia -> slad nie pracuje")
tr1, q1 = post(R1); tr2, q2 = post(R2)
print(f"  tr(P rho1 P) = {tr1:.12f}")
print(f"  tr(P rho2 P) = {tr2:.12f}")
print(f"  roznica      = {abs(tr1-tr2):.3e}")
print(f"  wartosc dokladna 1 - S/3 przy S = 1 + 2t = {float(1+2*t)}:  {float(1-(1+2*t)/3):.12f}")

print()
print("TABELA X4  warunek (c): po POSTSELEKCJI eliminacja je rozroznia")
print("  stan    q(0)         q(1)         q(2)")
for nm, q in [("rho1", q1), ("rho2", q2)]:
    print(f"  {nm}    " + "  ".join(f"{v:.9f}" for v in q))
print(f"  max |q1 - q2| = {np.max(np.abs(q1-q2)):.9f}")
print(f"  wartosci dokladne: q1 = (17/48, 11/48, 20/48), q2 = (29/48, 11/48, 8/48)")
print(f"  sprawdzenie: {17/48:.9f} {11/48:.9f} {20/48:.9f} | {29/48:.9f} {11/48:.9f} {8/48:.9f}")
print(f"  roznica dokladna na q(0): 29/48 - 17/48 = 12/48 = 1/4 = {1/4:.9f}")

print()
print("TABELA X5  kontrola czulosci 1: rzut KOMUTUJACY z M nie moze rozrozniac")
Pc = np.diag([1.0,1.0,0.0])
a1 = post(R1, Pc); a2 = post(R2, Pc)
print(f"  P' = diag(1,1,0);  q1 = " + " ".join(f"{v:.9f}" for v in a1[1]))
print(f"                     q2 = " + " ".join(f"{v:.9f}" for v in a2[1]))
print(f"  max |q1-q2| = {np.max(np.abs(a1[1]-a2[1])):.3e}   <- ma byc 0")

print()
print("TABELA X6  kontrola czulosci 2: rzut rzedu 1 nie moze rozrozniac po postselekcji")
v = np.array([0.3, 0.5, 0.81]); v /= np.linalg.norm(v)
P1 = np.outer(v, v)
b1 = post(R1, P1); b2 = post(R2, P1)
print(f"  q1 = " + " ".join(f"{x:.9f}" for x in b1[1]))
print(f"  q2 = " + " ".join(f"{x:.9f}" for x in b2[1]))
print(f"  max |q1-q2| = {np.max(np.abs(b1[1]-b2[1])):.3e}   <- ma byc 0 (rzut rzedu 1 kasuje stan)")

print()
print("TABELA X7  kontrola pokrycia: pelna klasa garblingow 3x3 nie rozroznia pary")
rng = np.random.default_rng(121)
worst = 0.0
for _ in range(300000):
    L = rng.random((3,3)); L /= L.sum(axis=0, keepdims=True)
    worst = max(worst, np.max(np.abs(L @ np.diag(R1) - L @ np.diag(R2))))
print(f"  300000 losowych L (kolumny z pelnego sympleksu): max roznica = {worst:.3e}")
print("  kontrola czulosci tego skanu — para o ROZNYCH diagonalach:")
w2 = 0.0
for _ in range(3000):
    L = rng.random((3,3)); L /= L.sum(axis=0, keepdims=True)
    w2 = max(w2, np.max(np.abs(L @ np.array([0.5,0.3,0.2]) - L @ np.array([0.4,0.4,0.2]))))
print(f"  -> {w2:.6f}   (niezerowe: skan wykrywa roznice, gdy istnieje)")

print()
print("TABELA X8  ten sam swiadek nie dziala przez slad — porownanie z garble.py Q4")
print("  garble.py: rozroznienie znikalo po renormalizacji (tr 1.0 vs 0.5, q identyczne)")
print(f"  tutaj:     tr identyczne ({tr1:.6f} = {tr2:.6f}), a q rozne o {np.max(np.abs(q1-q2)):.6f}")
print("  czyli separacja jest WYLACZNIE o koherencji niewidocznej dla M, nie o sladzie.")
