import numpy as np
from scipy.optimize import minimize

# SWIADEK DLA par.2.8 — WERSJA ODPORNA NA POSTSELEKCJE
# poprzedza: garble.py sha256 5924cdbcd6d077f699d1841b5274b43f4870081cedf194b612a1337c20b9e2c5
#
# garble.py Q4 pokazala, ze moj pierwszy swiadek rozroznial stany WYLACZNIE przez
# prawdopodobienstwo przezycia, czyli przez slad. To jest obserwacja z rozdz.1 par.8
# monografii, a nie nowy swiadek dla par.2.8. Odrzucam go.
#
# Mocniejsze pytanie: czy MODULO NORMALIZACJE (postselekcja na przezyciu, gdzie utrata
# sladu jest nieobserwowalna) eliminacja sektora jest garblingiem? Rzut rzedu 1 zawsze
# daje |theta><theta| niezaleznie od rho, wiec swiadek wymaga rzutu rzedu >= 2,
# czyli wymiaru >= 3.
#
# CEL: rho1, rho2 w C^3 z
#   (a) IDENTYCZNA diagonala w bazie M  -> nierozroznialne przez kazdy garbling M
#   (b) IDENTYCZNYM tr(P rho P)         -> slad NIE wykonuje pracy, roznica nie jest o nim
#   (c) ROZNA diagonala P rho P / tr    -> eliminacja rozroznia je PO postselekcji

d = np.array([0.5, 0.3, 0.2])           # wspolna diagonala obu stanow

def build(c01, c02, c12):
    R = np.diag(d).astype(complex)
    R[0,1] = c01; R[1,0] = np.conj(c01)
    R[0,2] = c02; R[2,0] = np.conj(c02)
    R[1,2] = c12; R[2,1] = np.conj(c12)
    return R

# rzut na 2-wymiarowa podprzestrzen NIEWSPOLOSIOWA z baza obliczeniowa:
# usuwamy kierunek n, zostawiamy jego dopelnienie
n = np.array([1.0, 1.0, 1.0])/np.sqrt(3)
P = np.eye(3) - np.outer(n, n)

def postsel(R):
    S = P @ R @ P
    tr = np.real(np.trace(S))
    return tr, (np.real(np.diag(S))/tr if tr > 1e-12 else np.full(3, np.nan))

def psd(R):
    return np.min(np.linalg.eigvalsh(R))

def unpack(x):
    return build(x[0]+1j*x[1], x[2]+1j*x[3], x[4]+1j*x[5])

def obj(x):
    R1 = unpack(x[:6]); R2 = unpack(x[6:])
    pen = 0.0
    for R in (R1, R2):
        e = psd(R)
        if e < 0: pen += 1e4*e*e
    t1, q1 = postsel(R1); t2, q2 = postsel(R2)
    pen += 1e4*(t1-t2)**2                      # warunek (b): rowne przezycie
    return -np.max(np.abs(q1-q2)) + pen

print("TABELA W1  szukam pary stanow spelniajacej (a), (b), (c)")
rng = np.random.default_rng(111)
best = (0.0, None)
for _ in range(400):
    x0 = rng.normal(0, 0.18, 12)
    r = minimize(obj, x0, method='Nelder-Mead',
                 options={'maxiter':30000,'maxfev':30000,'xatol':1e-12,'fatol':1e-14})
    R1 = unpack(r.x[:6]); R2 = unpack(r.x[6:])
    if min(psd(R1), psd(R2)) < -1e-9: continue
    t1, q1 = postsel(R1); t2, q2 = postsel(R2)
    if abs(t1-t2) > 1e-7: continue
    v = np.max(np.abs(q1-q2))
    if v > best[0]: best = (v, (R1, R2))
R1, R2 = best[1]
t1, q1 = postsel(R1); t2, q2 = postsel(R2)
print(f"  najwieksza znaleziona roznica diagonali po postselekcji: {best[0]:.9f}")

print()
print("TABELA W2  weryfikacja warunku (a): identyczna diagonala, czyli nierozroznialne")
print("           przez KAZDY garbling pomiaru M")
print("  stan    p(0)         p(1)         p(2)")
for nm, R in [("rho1", R1), ("rho2", R2)]:
    print(f"  {nm}    " + "  ".join(f"{v:.9f}" for v in np.real(np.diag(R))))
print(f"  max |diag(rho1) - diag(rho2)| = {np.max(np.abs(np.real(np.diag(R1))-np.real(np.diag(R2)))):.3e}")
print("  oba stany dodatnio okreslone: lambda_min = %.9f, %.9f" % (psd(R1), psd(R2)))

print()
print("TABELA W3  weryfikacja warunku (b): SLAD NIE wykonuje pracy")
print(f"  tr(P rho1 P) = {t1:.12f}")
print(f"  tr(P rho2 P) = {t2:.12f}")
print(f"  roznica       = {abs(t1-t2):.3e}   <- prawdopodobienstwo przezycia IDENTYCZNE")

print()
print("TABELA W4  weryfikacja warunku (c): po POSTSELEKCJI eliminacja je rozroznia")
print("  stan    q(0)         q(1)         q(2)      (diagonala P rho P / tr)")
for nm, q in [("rho1", q1), ("rho2", q2)]:
    print(f"  {nm}    " + "  ".join(f"{v:.9f}" for v in q))
print(f"  max |q1 - q2| = {np.max(np.abs(q1-q2)):.9f}")

print()
print("TABELA W5  kontrola czulosci: swiadek MUSI zawodzic, gdy rzut komutuje z M")
print("  P' = rzut na span{|0>,|1>} (diagonalny, komutuje z M)")
Pc = np.diag([1.0,1.0,0.0])
def postsel_P(R, PP):
    S = PP @ R @ PP; tr = np.real(np.trace(S))
    return tr, (np.real(np.diag(S))/tr if tr>1e-12 else np.full(3,np.nan))
for nm, R in [("rho1", R1), ("rho2", R2)]:
    tt, qq = postsel_P(R, Pc)
    print(f"  {nm}   tr = {tt:.9f}   q = " + "  ".join(f"{v:.9f}" for v in qq))
tc1 = postsel_P(R1,Pc); tc2 = postsel_P(R2,Pc)
print(f"  max |q1-q2| przy rzucie komutujacym = {np.max(np.abs(tc1[1]-tc2[1])):.3e}  <- ma byc 0")

print()
print("TABELA W6  kontrola pokrycia garblingow: skan po PELNEJ klasie macierzy")
print("           stochastycznych 3x3 (nie podzbiorze) — zadna nie rozroznia rho1 od rho2")
rng2 = np.random.default_rng(112)
worst = 0.0
for _ in range(300000):
    L = rng2.random((3,3)); L = L/L.sum(axis=0, keepdims=True)
    worst = max(worst, np.max(np.abs(L @ np.real(np.diag(R1)) - L @ np.real(np.diag(R2)))))
print(f"  300000 losowych L stochastycznych: najwieksza roznica wyjsc = {worst:.3e}")
print("  kontrola pokrycia: kolumny L losowane z pelnego sympleksu, wiec klasa pokryta")
print("  kontrola czulosci tego skanu: ta sama petla na parze o ROZNYCH diagonalach")
Rx = build(0,0,0); Ry = np.diag([0.4,0.4,0.2]).astype(complex)
w2 = 0.0
for _ in range(2000):
    L = rng2.random((3,3)); L = L/L.sum(axis=0, keepdims=True)
    w2 = max(w2, np.max(np.abs(L @ np.real(np.diag(Rx)) - L @ np.real(np.diag(Ry)))))
print(f"  -> {w2:.6f}  (niezerowe: skan potrafi wykryc roznice, gdy istnieje)")

print()
print("TABELA W7  jawna para do zapisania w zwrocie (zaokraglona, przeliczona od nowa)")
A1 = np.round(R1, 6); A2 = np.round(R2, 6)
for nm, R in [("rho1", A1), ("rho2", A2)]:
    print(f"  {nm} =")
    for row in R:
        print("     [" + ", ".join(f"{v.real:+.6f}{v.imag:+.6f}j" for v in row) + "]")
for nm, R in [("rho1", A1), ("rho2", A2)]:
    tt, qq = postsel(R)
    print(f"  {nm}: lambda_min = {psd(R):+.9f}  diag = " + " ".join(f"{v:.6f}" for v in np.real(np.diag(R)))
          + f"  tr(PrhoP) = {tt:.9f}  q = " + " ".join(f"{v:.6f}" for v in qq))
