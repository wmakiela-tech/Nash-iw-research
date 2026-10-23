import numpy as np

# Dociaz do coll.py (d607c22db666d596ed35ea1197b317ed94e1f120a2ad8913a2d65c4ba70c8ef9):
# o ILE myli sie stara granica. Jesli o staly czynnik — to usterka stalej.
# Jesli o czynnik rosnacy z wymiarem — to blad TYPU, bo sup norm blokow nie jest norma.
# Rodzina: widma calkowite rozlaczne, h = cos(2 pi .) sklejajace wszystko (jak u REC9),
# J = (1/n) * ones -> ||J|| = 1, kazdy wpis 1/n.

print("TABELA G1  luka starej granicy na rodzinie J = (1/n) ones, widma rozlaczne")
print("  n    ||J||   kappa_h(J)=max|blok|   ||J_coll||   sup defektu   STARA gr.   NOWA gr.   sup/STARA")
for n in [2, 3, 4, 6, 8, 12, 16, 24, 32]:
    la = np.arange(0, n, dtype=float)
    mu = np.arange(n, 2*n, dtype=float)
    J = np.ones((n, n))/n
    # h = cos(2 pi lambda) na calkowitych => h == 1 wszedzie => kazda para to kolizja
    coll = J.copy()                      # brak par dopasowanych (widma rozlaczne)
    mA = np.ones(n); mB = -np.ones(n)    # m = +1 na widmie A, -1 na widmie B, ||m||_inf = 1
    D = J*mA[None, :] - mB[:, None]*J
    sup_d = np.linalg.norm(D, 2)
    stara = 2*np.max(np.abs(coll)); nowa = 2*np.linalg.norm(coll, 2)
    print(f"  {n:<4} {np.linalg.norm(J,2):<7.4f} {np.max(np.abs(coll)):<22.9f} "
          f"{np.linalg.norm(coll,2):<12.9f} {sup_d:<13.9f} {stara:<11.6f} {nowa:<10.6f} {sup_d/stara:.6f}")

print()
print("TABELA G2  ten sam test na losowym J (nie tylko ones), widma rozlaczne")
print("  n    max sup/STARA   max ||J_coll||/kappa_h   sup/NOWA (max)")
rng = np.random.default_rng(1024)
for n in [2, 4, 8, 16, 32]:
    r1 = 0.0; r2 = 0.0; r3 = 0.0
    for _ in range(60):
        la = np.arange(0, n, dtype=float); mu = np.arange(n, 2*n, dtype=float)
        J = rng.normal(0, 1, (n, n))
        coll = J.copy()
        mA = np.ones(n); mB = -np.ones(n)
        sup_d = np.linalg.norm(J*mA[None, :] - mB[:, None]*J, 2)
        stara = 2*np.max(np.abs(coll)); nowa = 2*np.linalg.norm(coll, 2)
        r1 = max(r1, sup_d/stara)
        r2 = max(r2, np.linalg.norm(coll, 2)/np.max(np.abs(coll)))
        r3 = max(r3, sup_d/nowa)
    print(f"  {n:<4} {r1:<15.6f} {r2:<24.6f} {r3:.9f}")

print()
print("TABELA G3  kontrola: czy luka skaluje sie jak sqrt(n) dla losowego J i jak n dla ones")
print("  n    ones: sup/STARA / n     losowy: max(sup/STARA) / sqrt(n)")
for n in [4, 8, 16, 32, 64]:
    la = np.arange(0, n, dtype=float); mu = np.arange(n, 2*n, dtype=float)
    J = np.ones((n, n))/n
    mA = np.ones(n); mB = -np.ones(n)
    s1 = np.linalg.norm(J*mA[None, :] - mB[:, None]*J, 2)/(2*np.max(np.abs(J)))
    best = 0.0
    for _ in range(40):
        Jr = rng.normal(0, 1, (n, n))
        s = np.linalg.norm(Jr*mA[None, :] - mB[:, None]*Jr, 2)/(2*np.max(np.abs(Jr)))
        best = max(best, s)
    print(f"  {n:<4} {s1/n:<22.9f} {best/np.sqrt(n):.9f}")
