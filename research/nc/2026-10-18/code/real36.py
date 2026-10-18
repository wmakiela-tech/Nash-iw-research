import numpy as np

# SWIADEK DLA NON-MAPA par.3.6 MONOGRAFII:
# "w nieskonczonym wymiarze sama minimalnosc przyblizona nie zapewnia ograniczonego
#  izomorfizmu z ograniczona odwrotnoscia"
#
# KONSTRUKCJA. Przestrzen stanu l^2(N). D diagonalne, lambda_n = 1/(n+2):
# rozne, niezerowe, ||D|| = 1/2. Realizacja: Sigma(z) = B (zI - D)^{-1} C,
# C = c w l^2 (wejscie skalarne), B = <f, .> (wyjscie skalarne).
# Parametry Markowa:  B D^k C = sum_n f_n lambda_n^k c_n.
#
#   REALIZACJA 1:  c_n = 2^{-n},          f_n = 2^{-n}
#   REALIZACJA 2:  c'_n = 4^{-n}(n+1),    f'_n = 1/(n+1)
#
# Iloczyny: f_n c_n = 4^{-n} = f'_n c'_n TERMWISE, wiec parametry Markowa identyczne.
# Splot:    T_n = c'_n/c_n = 2^{-n}(n+1).  T ograniczone, T^{-1}_n = 2^n/(n+1) -> inf.
#
# MINIMALNOSC PRZYBLIZONA. Niech x _|_ D^k c dla kazdego k: sum_n conj(x_n) c_n lam_n^k = 0.
# Z g_n = conj(x_n) c_n w l^1 funkcja G(z) = sum_n g_n/(1 - lam_n z) = sum_k z^k sum_n g_n lam_n^k
# znika tozsamosciowo, a ma bieguny proste w 1/lam_n = n+2, parami rozne, wiec wszystkie
# residua g_n/lam_n sa zerowe => g = 0 => x = 0, bo c_n != 0. Tak samo dla obserwowalnosci
# z f_n != 0. Obie realizacje sa wiec przyblizenie sterowalne i przyblizenie obserwowalne.
#
# JEDNOZNACZNOSC SPLOTU. Jesli S ograniczone, S D = D S, to przy roznych lambda_n S jest
# diagonalne; z S c = c' wynika S = T. Innego splotu nie ma, a T^{-1} jest nieograniczone,
# wiec ograniczonego izomorfizmu o ograniczonej odwrotnosci NIE MA. [koniec dowodu]
#
# Ponizej kontrola numeryczna kazdego kroku plus kontrola czulosci.

N = 4000
n = np.arange(N, dtype=float)
lam = 1.0/(n+2.0)

c1 = 2.0**(-n)
f1 = 2.0**(-n)
c2 = 4.0**(-n)*(n+1.0)
f2 = 1.0/(n+1.0)

print("TABELA R1  obie realizacje leza w l^2, a D jest ograniczone")
for nm, v in [("c  ", c1), ("f  ", f1), ("c' ", c2), ("f' ", f2)]:
    print(f"  ||{nm}||_2 = {np.linalg.norm(v):.9f}")
print(f"  ||D|| = sup|lambda_n| = {lam.max():.9f}   lambda rozne: {len(set(np.round(lam,15)))==N}")
print(f"  lambda_n != 0 dla wszystkich n: {np.all(lam!=0)}")

print()
print("TABELA R2  parametry Markowa — policzone OSOBNO dla kazdej realizacji")
print("  k    B D^k C (real. 1)        B' D^k C' (real. 2)      roznica")
for k in range(9):
    m1 = np.sum(f1*(lam**k)*c1); m2 = np.sum(f2*(lam**k)*c2)
    print(f"  {k:<4} {m1:<24.16e} {m2:<24.16e} {abs(m1-m2):.3e}")
mx = max(abs(np.sum(f1*(lam**k)*c1) - np.sum(f2*(lam**k)*c2)) for k in range(200))
print(f"  najwieksza roznica dla k = 0..199: {mx:.3e}")

print()
print("TABELA R3  splot T i jego odwrotnosc")
T = c2/c1
print(f"  T_n = c'_n/c_n = 2^{{-n}}(n+1);  sup_n T_n = ||T|| = {T.max():.9f}")
print(f"  T jest injektywne: min_n T_n > 0 na kazdym skonczonym odcinku, T_n -> 0")
print("  n       T_n              1/T_n")
for k in [0,1,2,5,10,20,40,80]:
    print(f"  {k:<7} {T[k]:<16.9e} {1.0/T[k]:.9e}")
print(f"  1/T_n przy n = {N-1}: {1.0/T[N-1]:.6e}   -> T^{{-1}} NIEOGRANICZONE")

print()
print("TABELA R4  warunki splotu: T c = c', T f' = f, T D T^{-1} = D")
print(f"  max |T*c - c'|   = {np.max(np.abs(T*c1 - c2)):.3e}")
print(f"  max |T*f' - f|   = {np.max(np.abs(T*f2 - f1)):.3e}")
print("  T D T^{-1} = D zachodzi tozsamosciowo: oba operatory diagonalne")

print()
print("TABELA R5  minimalnosc przyblizona — kontrola warunku z dowodu")
print(f"  wszystkie c_n  != 0 : {np.all(c1>0)}    min na odcinku = {c1.min():.3e}")
print(f"  wszystkie f_n  != 0 : {np.all(f1>0)}    min na odcinku = {f1.min():.3e}")
print(f"  wszystkie c'_n != 0 : {np.all(c2>0)}    min na odcinku = {c2.min():.3e}")
print(f"  wszystkie f'_n != 0 : {np.all(f2>0)}    min na odcinku = {f2.min():.3e}")
print("  (zera pojawiaja sie dopiero przez underflow zmiennoprzecinkowy, nie w konstrukcji)")

print()
print("TABELA R6  cien skonczeniewymiarowy: uwarunkowanie gramianow na odcinkach")
print("  gramian sterowalnosci W_c = sum_k D^k c c^T D^k (odciety na K wyrazach)")
print("  M      cond(W_c) real.1      cond(W_c) real.2      iloraz")
for M in [4, 6, 8, 10, 12]:
    K = 400
    L = lam[:M]
    V = np.array([[L[i]**k for i in range(M)] for k in range(K)])
    for tag, cc in [("", c1[:M])]:
        W1 = (V*cc).T @ (V*cc)
        W2 = (V*c2[:M]).T @ (V*c2[:M])
        k1 = np.linalg.cond(W1); k2 = np.linalg.cond(W2)
        print(f"  {M:<6} {k1:<21.6e} {k2:<21.6e} {k2/k1:.3e}")

print()
print("TABELA R7  KONTROLA CZULOSCI: para, dla ktorej splot JEST odwracalny ograniczenie")
print("  bierzemy a_n ograniczone z gory i z dolu: a_n = 2 + sin(n), wiec T_n w [1,3]")
a = 2.0 + np.sin(n)
c3 = 4.0**(-n)*a / (2.0**(-n))    # c3_n = 2^{-n} a_n  -> T_n = a_n
c3 = 2.0**(-n)*a
f3 = 2.0**(-n)/a
T3 = c3/c1
m3 = max(abs(np.sum(f1*(lam**k)*c1) - np.sum(f3*(lam**k)*c3)) for k in range(200))
print(f"  parametry Markowa nadal identyczne: max roznica = {m3:.3e}")
print(f"  sup T3 = {T3.max():.9f}   inf T3 = {T3.min():.9f}   sup 1/T3 = {(1.0/T3).max():.9f}")
print("  -> tutaj splot JEST ograniczony z ograniczona odwrotnoscia, realizacje sa podobne.")
print("  Swiadek musi zawodzic w tym przypadku i zawodzi: test rozroznia oba scenariusze.")

print()
print("TABELA R8  KONTROLA: czy roznica nie jest artefaktem skalowania c wobec f")
print("  normy obu realizacji sa porownywalne, wiec nie chodzi o trywialne przeskalowanie")
print(f"  ||c||*||f||   = {np.linalg.norm(c1)*np.linalg.norm(f1):.9f}")
print(f"  ||c'||*||f'|| = {np.linalg.norm(c2)*np.linalg.norm(f2):.9f}")
print(f"  iloraz        = {(np.linalg.norm(c2)*np.linalg.norm(f2))/(np.linalg.norm(c1)*np.linalg.norm(f1)):.9f}")
print("  obie skonczone i tego samego rzedu — nieograniczonosc T^{-1} nie bierze sie")
print("  z rozdmuchania norm, tylko z ROZKLADU masy miedzy c i f po modach.")
