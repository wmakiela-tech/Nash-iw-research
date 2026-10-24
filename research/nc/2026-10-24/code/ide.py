import numpy as np
from scipy.optimize import linprog

# PREREG_IDE.md sha256 0f05736e743386192afe021a6cac9d5348c9605ce295503a8452eef38cbe0620
# Wsparcie XH-S4 Q80. Pytanie i kontrola B naleza do XH-S4 (obrot 026).

def splot(dK, u, h):
    """(dK * u)(T) na siatce: sum dK(T-s) u(s) ds, trapezy"""
    w = np.full(len(u), h); w[0] *= .5; w[-1] *= .5
    return float(np.sum(w*dK[::-1]*u))

def widocznosc_num(dKf, T, N, klasa):
    """sup |(dK*u)(T)| po u w zadanej klasie, przez LP (klasa inf) albo wzor (2, 1)"""
    s = np.linspace(0, T, N+1); h = T/N
    dK = dKf(s)
    w = np.full(N+1, h); w[0] *= .5; w[-1] *= .5
    c = w*dK[::-1]                       # funkcjonal liniowy: c . u
    if klasa == "inf":                   # |u|<=1 -> maksimum to sum |c|
        r = linprog(-c, bounds=[(-1,1)]*(N+1), method="highs")
        return -r.fun, np.sum(np.abs(c))
    if klasa == "2":                     # ||u||_2<=1 -> ||c||_2 / sqrt(w) w sensie ciaglym
        return float(np.sqrt(np.sum(w*dK**2))), float(np.sqrt(np.sum(w*dK**2)))
    if klasa == "1":                     # ||u||_1<=1 -> max |dK|
        return float(np.max(np.abs(dK))), float(np.max(np.abs(dK)))

print("TABELA I1  F1 — czy ODTWARZAM kontrole B z XH-S4 obrot 026")
print("  K1 = e^{-t}, K2 = K1 + 0.2 e^{-20t}; dK = 0.2 e^{-20t}")
dKf = lambda t: 0.2*np.exp(-20*np.asarray(t))
print(f"  dK(0) = {dKf(0.0):.6f}   XH podaje K2(0)-K1(0) = 0.2")
print("  t      ||dK||_L1(0,t)      wzor 0.01(1-e^{-20t})   roznica     wyjscie dla u==1   roznica")
for T in [0.05,0.1,0.25,0.5,1.0,2.0]:
    s = np.linspace(0,T,20001); h = T/20000
    w = np.full(len(s),h); w[0]*=.5; w[-1]*=.5
    l1 = float(np.sum(w*np.abs(dKf(s))))
    wz = 0.01*(1-np.exp(-20*T))
    u1 = splot(dKf(s), np.ones_like(s), h)
    print(f"  {T:<6.2f} {l1:<18.12f} {wz:<22.12f} {abs(l1-wz):<11.2e} {u1:<18.12f} {abs(u1-wz):.2e}")
print("  (u == 1 wysyca, bo dK > 0, wiec sign(dK) == 1 — przypadek szczegolny P1)")

print()
print("TABELA I2  F2 — prawo widocznosci: sup_{|u|<=1} |(dK*u)(T)| = ||dK||_L1(0,T)")
print("  jadro                      T     LP sup           ||dK||_L1        roznica")
kaz = [("0.2 e^{-20t}", lambda t: 0.2*np.exp(-20*np.asarray(t))),
       ("e^{-t} - 0.4 e^{-4t}", lambda t: np.exp(-np.asarray(t))-0.4*np.exp(-4*np.asarray(t))),
       ("sin(6t) e^{-t}  (zmienny znak)", lambda t: np.sin(6*np.asarray(t))*np.exp(-np.asarray(t))),
       ("1/sqrt(pi t) obciete", lambda t: 1/np.sqrt(np.pi*np.maximum(np.asarray(t),1e-9))*(np.asarray(t)>1e-9))]
for nm, f in kaz:
    for T in [0.5, 2.0]:
        lp, l1 = widocznosc_num(f, T, 3000, "inf")
        print(f"  {nm:<27} {T:<5.1f} {lp:<16.12f} {l1:<16.12f} {abs(lp-l1):.2e}")

print()
print("TABELA I3  F3 — tabela dualnosci: klasa wzbudzenia dobiera norme bledu jadra")
print("  dK = e^{-t} - 0.4 e^{-4t} na [0,2]")
f2 = lambda t: np.exp(-np.asarray(t))-0.4*np.exp(-4*np.asarray(t))
for klasa, etyk in [("inf","||u||_inf <= 1  ->  ||dK||_L1"),
                    ("2","||u||_2 <= 1    ->  ||dK||_L2"),
                    ("1","||u||_1 <= 1    ->  ||dK||_Linf")]:
    v, w = widocznosc_num(f2, 2.0, 4000, klasa)
    print(f"  {etyk:<34} widocznosc = {v:.12f}")
print()
print("  TE SAME dwie liczby XH-S4 jako dwa wiersze tej tabeli, dla dK = 0.2 e^{-20t}, T = 2:")
for klasa, etyk in [("1","||u||_1 <= 1   -> ||dK||_Linf"),("inf","||u||_inf <= 1 -> ||dK||_L1")]:
    v, _ = widocznosc_num(dKf, 2.0, 4000, klasa)
    print(f"  {etyk:<32} = {v:.12f}")
print("  -> 0.2 i 0.01 sa OBIE poprawne; odpowiadaja na ROZNE pytania")

print()
print("TABELA I4  F4 — niewidoczna skladowa jest NIEOGRANICZONA w amplitudzie")
print("  dK_n(t) = n e^{-n^2 t}:  dK_n(0) = n,  ||dK_n||_L1(0,inf) = 1/n")
print("  n      dK_n(0)     ||dK_n||_L1 zmierzone   wzor 1/n      roznica    LP sup")
for n in [1,2,5,10,50,200,1000]:
    g = lambda t,n=n: n*np.exp(-n*n*np.asarray(t))
    T = min(20.0/(n*n)+1e-6, 5.0)
    s = np.linspace(0,T,60001); h=T/60000
    w = np.full(len(s),h); w[0]*=.5; w[-1]*=.5
    l1 = float(np.sum(w*np.abs(g(s))))
    lp,_ = widocznosc_num(g, T, 3000, "inf")
    print(f"  {n:<6} {g(0.0):<11.4f} {l1:<23.12f} {1.0/n:<13.12f} {abs(l1-1.0/n):<10.2e} {lp:.9f}")
print("  -> amplituda rosnie bez ograniczenia, widocznosc maleje jak 1/n")
