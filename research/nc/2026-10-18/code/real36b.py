import numpy as np
from fractions import Fraction as F

# SWIADEK DLA par.3.6 — WERSJA BEZ UNDERFLOW
# poprzedza: real36.py sha256 1f669f48ed48dd18fde482ee905f3c98bc23cada50e445f70cc14887c8e0c289
#   (tamta liczyla T jako iloraz c'/c przy n do 4000; 2^{-n} schodzi pod zakres float
#    okolo n = 1075, wiec iloraz dawal 0/0 = nan, a ja wydrukowalem zastrzezenie
#    zamiast naprawic rachunek. Tutaj: tozsamosci w arytmetyce DOKLADNEJ (Fraction),
#    wielkosci analityczne z wzorow zamknietych, normy na odcinku bez underflow.)
#
# KONSTRUKCJA (l^2(N), wejscie i wyjscie skalarne, Sigma(z) = B (zI-D)^{-1} C):
#   D diagonalne, lambda_n = 1/(n+2)
#   REAL. 1:  c_n = 2^{-n}         f_n = 2^{-n}
#   REAL. 2:  c'_n = 4^{-n}(n+1)   f'_n = 1/(n+1)
#   T_n = 2^{-n}(n+1)

NEX = 120           # zakres arytmetyki dokladnej
NFL = 400           # zakres float bez underflow (4^-400 ~ 6.7e-241)

def c1F(k): return F(1, 2**k)
def f1F(k): return F(1, 2**k)
def c2F(k): return F(k+1, 4**k)
def f2F(k): return F(1, k+1)
def TF(k):  return F(k+1, 2**k)
def lamF(k): return F(1, k+2)

print("TABELA E1  tozsamosci splotu w ARYTMETYCE DOKLADNEJ, n = 0..%d" % (NEX-1))
e_tc = max(abs(TF(k)*c1F(k) - c2F(k)) for k in range(NEX))
e_tf = max(abs(TF(k)*f2F(k) - f1F(k)) for k in range(NEX))
e_pr = max(abs(f1F(k)*c1F(k) - f2F(k)*c2F(k)) for k in range(NEX))
print(f"  max |T_n c_n - c'_n|        = {e_tc}   (dokladnie zero: {e_tc == 0})")
print(f"  max |T_n f'_n - f_n|        = {e_tf}   (dokladnie zero: {e_tf == 0})")
print(f"  max |f_n c_n - f'_n c'_n|   = {e_pr}   (dokladnie zero: {e_pr == 0})")
print(f"  wspolny iloczyn f_n c_n = 4^(-n): {all(f1F(k)*c1F(k) == F(1,4**k) for k in range(NEX))}")

print()
print("TABELA E2  parametry Markowa w arytmetyce dokladnej, k = 0..11, suma po n < %d" % NEX)
print("  k    |sum_n f_n lam^k c_n  -  sum_n f'_n lam^k c'_n|   (dokladnie)")
for k in range(12):
    m1 = sum(f1F(j)*lamF(j)**k*c1F(j) for j in range(NEX))
    m2 = sum(f2F(j)*lamF(j)**k*c2F(j) for j in range(NEX))
    print(f"  {k:<4} {m1-m2}")
print("  rownosc jest TERMWISE, nie tylko w sumie — wiec zachodzi dla kazdego obciecia")

print()
print("TABELA E3  T jest ograniczone, T^{-1} nie — z wzoru, nie z ilorazu")
Tv = np.array([(k+1)*2.0**(-k) for k in range(NFL)])
print(f"  ||T|| = sup_n (n+1)2^(-n) = {Tv.max():.12f}  (osiagane przy n = {int(np.argmax(Tv))} i 1)")
print("  n        T_n                1/T_n")
for k in [0,1,2,5,10,20,40,80,160,320]:
    t = (k+1)*2.0**(-k)
    print(f"  {k:<8} {t:<18.6e} {1.0/t:.6e}")
print(f"  1/T_n rosnie jak 2^n/(n+1) -> nieskonczonosc: przy n=320 to {2.0**320/321:.3e}")
print("  T injektywne (T_n > 0 dla kazdego n), obraz gesty, ale NIE surjektywne")

print()
print("TABELA E4  wszystkie wspolrzedne niezerowe — sprawdzone w arytmetyce dokladnej")
print(f"  c_n  != 0 dla n < {NEX}: {all(c1F(k) != 0 for k in range(NEX))}")
print(f"  f_n  != 0 dla n < {NEX}: {all(f1F(k) != 0 for k in range(NEX))}")
print(f"  c'_n != 0 dla n < {NEX}: {all(c2F(k) != 0 for k in range(NEX))}")
print(f"  f'_n != 0 dla n < {NEX}: {all(f2F(k) != 0 for k in range(NEX))}")
print("  (wzory sa jawnie niezerowe dla kazdego n; sprawdzenie potwierdza brak bledu zapisu)")
print(f"  lambda_n parami rozne, niezerowe: {len({lamF(k) for k in range(NEX)}) == NEX}")

print()
print("TABELA E5  obie realizacje leza w l^2 (normy na odcinku n < %d, ogon pomijalny)" % NFL)
k = np.arange(NFL, dtype=float)
nc1 = np.sqrt(np.sum((2.0**(-k))**2)); nf1 = nc1
nc2 = np.sqrt(np.sum((4.0**(-k)*(k+1))**2)); nf2 = np.sqrt(np.sum((1.0/(k+1))**2))
print(f"  ||c||  = {nc1:.9f}   wartosc dokladna sqrt(4/3) = {np.sqrt(4/3):.9f}")
print(f"  ||f||  = {nf1:.9f}")
print(f"  ||c'|| = {nc2:.9f}")
print(f"  ||f'|| = {nf2:.9f}   wartosc dokladna sqrt(pi^2/6) = {np.sqrt(np.pi**2/6):.9f}")
print("  wszystkie skonczone: obie realizacje sa dopuszczalne (B, C ograniczone)")

print()
print("TABELA E6  KONTROLA CZULOSCI: para o splocie ODWRACALNYM ograniczenie")
print("  a_n = 2 + sin(n) w [1,3];  c''_n = 2^(-n) a_n,  f''_n = 2^(-n)/a_n")
a = 2.0 + np.sin(k)
print(f"  iloczyn f''_n c''_n = 4^(-n): max odchylenie = {np.max(np.abs((2.0**(-k)/a)*(2.0**(-k)*a) - 4.0**(-k))):.3e}")
print(f"  T''_n = a_n:  sup = {a.max():.9f}   inf = {a.min():.9f}   sup 1/T'' = {(1.0/a).max():.9f}")
print("  -> splot ograniczony Z ograniczona odwrotnoscia; realizacje SA podobne.")
print("  Swiadek musi tu zawodzic i zawodzi — test rozroznia oba scenariusze.")

print()
print("TABELA E7  KONTROLA: czy to nie trywialne przeskalowanie norm")
print(f"  ||c||*||f||   = {nc1*nf1:.9f}")
print(f"  ||c'||*||f'|| = {nc2*nf2:.9f}")
print(f"  iloraz        = {(nc2*nf2)/(nc1*nf1):.9f}   (rzedu 1)")
print("  Nieograniczonosc T^{-1} nie bierze sie z rozdmuchania norm, lecz z ROZKLADU")
print("  masy miedzy c i f po modach: real.1 dzieli 4^(-n) rowno, real.2 przesuwa ja")
print("  do c i odbiera f, coraz mocniej z n.")

print()
print("TABELA E8  cien skonczeniewymiarowy: uwarunkowanie gramianow sterowalnosci")
print("  W = sum_{k<K} (D^k c)(D^k c)^T na pierwszych M modach, K = 400")
K = 400
for M in [4, 6, 8, 10, 12]:
    L = np.array([1.0/(j+2) for j in range(M)])
    V = np.array([[L[i]**kk for i in range(M)] for kk in range(K)])
    W1 = (V*(2.0**(-np.arange(M)))).T @ (V*(2.0**(-np.arange(M))))
    W2 = (V*(4.0**(-np.arange(M))*(np.arange(M)+1))).T @ (V*(4.0**(-np.arange(M))*(np.arange(M)+1)))
    print(f"  M = {M:<4} cond(W) real.1 = {np.linalg.cond(W1):<14.4e}  real.2 = {np.linalg.cond(W2):<14.4e}  iloraz = {np.linalg.cond(W2)/np.linalg.cond(W1):.3e}")
print("  Uwarunkowanie rozjezdza sie z M. To jest skonczeniewymiarowy slad tego, ze")
print("  w granicy splot przestaje miec ograniczona odwrotnosc. NIE jest to dowod —")
print("  dowod jest analityczny, powyzej; to tylko ilustracja.")
